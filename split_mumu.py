import os
import re

# Configuration
input_path = r"c:\Users\nihil\coding\novel\novel-assist-agent\library\novel_sample_texts\무무 무적.txt"
output_dir = r"c:\Users\nihil\coding\novel\novel-assist-agent\library\novel_sample_texts\무무_무적"

# Ensure output directory exists (clearing old files is safer)
if os.path.exists(output_dir):
    for f in os.listdir(output_dir):
        os.remove(os.path.join(output_dir, f))
os.makedirs(output_dir, exist_ok=True)

# Regex patterns
# Pattern for Prologue: "서장"
# Pattern for Regular Chapters: "N화 Title (M)"
header_pattern = re.compile(r"(^서장)|(^\d+화.*\(\d+\))")
separator_pattern = re.compile(r"^─+$")


def split_novel():
    current_lines = []

    # Episode counter
    episode_count = 0

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        stripped_line = line.strip()

        # Skip separator
        if separator_pattern.match(stripped_line):
            continue

        # Check if line is a header
        if header_pattern.match(stripped_line):
            # If we have gathered content for the previous episode, save it
            if current_lines:
                save_chapter(episode_count, current_lines)
                current_lines = []

            # Increment counter (Start from 1)
            # Even Prologue counts as episode 1 in this sequential scheme?
            # Or Prologue is 0? Use sequential 1..30 as per User's hint "11화(2) is 30화".
            # If Prologue is 1, then we reach 30.
            episode_count += 1
            current_lines.append(line)
        else:
            # content
            if episode_count > 0:
                current_lines.append(line)
            else:
                # Content before first header?
                # If there's content before '서장', usually metadata, ignore or append if needed.
                pass

    # Save last chapter
    if current_lines:
        save_chapter(episode_count, current_lines)


def save_chapter(number, lines):
    # Format: 01화.txt, 02화.txt ... 30화.txt
    filename = f"{number:02d}화.txt"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"Created {filename} with {len(lines)} lines. (Header: {lines[0].strip()})")


if __name__ == "__main__":
    split_novel()
