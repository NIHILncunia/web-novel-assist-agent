import glob
import os
import re

TRAITS_DIR = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\traits"

# Category mapping based on filename
CATEGORY_MAP = {
    "00_유형.md": "유형",
    "01_크기.md": "크기",
    "02_기원.md": "기원",
    "03_신체.md": "신체",
    "04_지식_지혜.md": "지식",
    "05_군집.md": "군집",
    "06_이동.md": "이동",
    "07_감각.md": "감각",
    "08_약점.md": "약점",
    "09_생활.md": "생활",
    "10_정신.md": "정신",
    "11_지역환경.md": "환경",
    "12_외교.md": "외교",
    "13_경영.md": "경영",
    "14_제작.md": "제작",
    "15_속성.md": "속성",
    "16_전투.md": "전투",
    "17_관계.md": "관계",
}


def clean_cell(cell):
    return cell.strip()


def format_file(filepath):
    filename = os.path.basename(filepath)
    default_cat = CATEGORY_MAP.get(filename, "기타")

    print(f"Processing {filename} (Default Category: {default_cat})")

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    in_table = False

    for line in lines:
        stripped = line.strip()

        # Detect table separator
        if re.match(r"^\|\s*:?-+\s*\|\s*:?-+:?\s*\|\s*:?-+\s*\|", stripped):
            new_lines.append("| :--- | :---: | :--- |\n")
            in_table = True
            continue

        # Detect table row
        if stripped.startswith("|") and stripped.endswith("|"):
            # Skip specific duplicate if found in 03_신체.md
            if filename == "03_신체.md" and "전투 적응" in stripped:
                print("  [INFO] Skipping duplicate '전투 적응'")
                continue

            cells = [clean_cell(c) for c in stripped.split("|") if c]

            # Header row check
            if "키워드" in cells[0] or "트레잇 이름" in cells[0]:
                new_lines.append(f"| {cells[0]} | 분류 | 설명 |\n")
                continue

            # Data row
            keyword = cells[0]

            # Handle 2 columns vs 3 columns
            if len(cells) == 2:
                # Missing category
                category = default_cat
                desc = cells[1]
            elif len(cells) >= 3:
                category = cells[1]
                # If category looks like description (too long), fix it
                if len(category) > 10 and default_cat not in category:
                    # Heuristic: if 2nd col is long, assume it's description and cat is missing
                    category = default_cat
                    desc = cells[1]
                else:
                    desc = cells[2]
            else:
                # 1 column? Just keep as is or skip
                new_lines.append(line)
                continue

            # Normalize category if empty
            if not category:
                category = default_cat

            # Reconstruct line
            new_line = f"| {keyword} | {category} | {desc} |\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def main():
    files = glob.glob(os.path.join(TRAITS_DIR, "*.md"))
    for f in files:
        format_file(f)


if __name__ == "__main__":
    main()
