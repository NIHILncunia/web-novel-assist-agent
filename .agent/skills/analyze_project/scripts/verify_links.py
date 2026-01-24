import os
import re
from pathlib import Path


def find_md_files(root_dir):
    return list(Path(root_dir).rglob("*.md"))


def check_links(files, project_root):
    # Regex to capture [text](path)
    link_pattern = re.compile(r"\[.*?\]\((.*?)\)")
    # Regex to capture raw paths like 'data/word_list/...' or 'manuals/...'
    # This is a bit looser, trying to catch references that aren't hyperlinked
    path_pattern = re.compile(
        r'(?:["\'`])((?:data|manuals|prompt|_templates|library)/[\w\-\./]+)(?:["\'`])'
    )

    broken_links = []

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 1. Check Markdown Links
            for match in link_pattern.finditer(content):
                link = match.group(1)
                # Ignore anchors and external links
                if (
                    link.startswith("#")
                    or link.startswith("http")
                    or link.startswith("mailto")
                ):
                    continue

                # Handling file:/// absolute paths (often used by Agent)
                if link.startswith("file:///"):
                    target = link.replace("file:///", "")
                    # Normalize Windows paths
                    if os.name == "nt" and target.startswith("/"):
                        # e.g. /c:/Users... -> c:/Users...
                        target = target.lstrip("/")

                    if not os.path.exists(target):
                        broken_links.append(
                            (str(file_path), link, "File not found (Absolute)")
                        )
                    continue

                # Clean up link (remove anchors like #section)
                clean_link = link.split("#")[0]
                if not clean_link:
                    continue

                # Resolve relative path
                if os.path.isabs(clean_link):
                    target_path = Path(clean_link)
                else:
                    target_path = (file_path.parent / clean_link).resolve()

                if not target_path.exists():
                    # Try resolving from project root if relative resolution failed
                    # Many prompts reference 'data/...' assuming project root CWD
                    root_target = (project_root / clean_link).resolve()
                    if not root_target.exists():
                        broken_links.append((str(file_path), link, "File not found"))

            # 2. Check Raw Path References (quoted paths in instructions)
            for match in path_pattern.finditer(content):
                path_str = match.group(1)
                # Assume these are relative to project root
                target_path = (project_root / path_str).resolve()
                if not target_path.exists():
                    broken_links.append(
                        (str(file_path), path_str, "Raw Path Reference not found")
                    )

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    return broken_links


def main():
    project_root = Path.cwd()
    print(f"Scanning project from: {project_root}")

    # Define directories to scan
    scan_dirs = ["manuals", "prompt", "_templates"]
    all_md_files = []
    for d in scan_dirs:
        if (project_root / d).exists():
            all_md_files.extend(find_md_files(project_root / d))

    # Also scan reports if needed, but user focused on system files.
    # Let's stick to system files first.

    broken = check_links(all_md_files, project_root)

    if broken:
        print(f"Found {len(broken)} broken links:")
        for source, target, reason in broken:
            # Make source relative for cleaner output
            rel_source = os.path.relpath(source, project_root)
            try:
                print(f"[{rel_source}] -> '{target}' ({reason})")
            except UnicodeEncodeError:
                print(
                    f"[{rel_source}] -> '{target.encode('utf-8', 'replace')}' ({reason})"
                )
    else:
        print("No broken links found.")


if __name__ == "__main__":
    main()
