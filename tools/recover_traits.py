import os
import re

TRAIT_DIR = "data/traits"
ARCHIVE_DIR = "archive/report/concept_analyze/nations"

TARGET_FILES = ["05_군집.md", "09_생활.md", "12_외교.md"]


def load_traits_from_report(filepath):
    traits = {}
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Simple parser for list format in reports: * **[특성] 이름 (Eng)** ... * **설명:** ...
    # Or extracting from the structure.
    # The structure in report is:
    # * **[특성] 이름 (Meiwaku / Nuisance)**
    #     * **분류:** `05_군집.md`
    #     * **제안 사유:** ...
    #     * **설명:** 타인에게 불쾌감이나 번거로움을 주는 것을 극도로 경계하며...

    current_name = None

    for line in lines:
        line = line.strip()
        name_match = re.search(r"\* \*\*\[특성\] (.+?)\*\*", line)
        if name_match:
            # Extract just the name part before any parenthesis?
            # In database we used "민폐 혐오" but report might have "민폐 혐오 (Nuisance Aversion)"
            # We need to normalize.
            full_name = name_match.group(1)
            # Remove parenthesis and english if present?
            # The database has "민폐 혐오". Report has "민폐 혐오 (Nuisance Aversion)"
            if "(" in full_name:
                simple_name = full_name.split("(")[0].strip()
            else:
                simple_name = full_name
            current_name = simple_name
            continue

        if current_name and line.startswith("* **설명:**"):
            desc = line.replace("* **설명:**", "").strip()
            traits[current_name] = desc
            current_name = None

    return traits


def recover_files():
    # 1. Load all traits from archives
    all_traits = {}
    if not os.path.exists(ARCHIVE_DIR):
        print("Archive directory not found!")
        return

    for f in os.listdir(ARCHIVE_DIR):
        if f.endswith(".md"):
            print(f"Loading from {f}...")
            traits = load_traits_from_report(os.path.join(ARCHIVE_DIR, f))
            all_traits.update(traits)

    print(f"Loaded {len(all_traits)} traits from archive.")

    # 2. Fix target files
    for filename in TARGET_FILES:
        filepath = os.path.join(TRAIT_DIR, filename)
        if not os.path.exists(filepath):
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        fixed_count = 0

        for line in lines:
            if (
                line.strip().startswith("|")
                and "---" not in line
                and "분류" not in line
            ):
                parts = [p.strip() for p in line.strip().split("|") if p]
                if len(parts) >= 3:
                    name = parts[0]
                    category = parts[1]
                    desc = parts[2]

                    # Check if desc is suspicious (same as filename keyword or just category name)
                    # In 05_군집.md, desc became "군집"
                    # In 09_생활.md, desc became "생활"
                    # In 12_외교.md, desc became "외교"

                    suspicious_keywords = ["군집", "생활", "외교", "정신"]
                    if desc in suspicious_keywords or len(desc) < 5:
                        # Try to recover
                        # Recover name might have (Eng) in report but not in DB?
                        # DB name is "민폐 혐오". Report name is "민폐 혐오 (Nuisance Aversion)" -> Key became "민폐 혐오"
                        if name in all_traits:
                            new_desc = all_traits[name]
                            new_line = f"| {name} | {category} | {new_desc} |\n"
                            new_lines.append(new_line)
                            fixed_count += 1
                            continue
                        else:
                            # Try fuzzy match? (remove parens from DB name if any)
                            simple_db_name = name.split("(")[0].strip()
                            if simple_db_name in all_traits:
                                new_desc = all_traits[simple_db_name]
                                new_line = f"| {name} | {category} | {new_desc} |\n"
                                new_lines.append(new_line)
                                fixed_count += 1
                                continue

                            print(f"Could not recover: {name}")

                new_lines.append(line)
            else:
                new_lines.append(line)

        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"Fixed {fixed_count} lines in {filename}")


if __name__ == "__main__":
    recover_files()
