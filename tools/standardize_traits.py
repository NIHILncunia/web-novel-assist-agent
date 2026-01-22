import os
import re

TRAIT_DIR = "data/traits"

# Configuration for files that use specific logic
SECTION_MODE_FILES = ["03_신체.md", "05_군집.md", "09_생활.md"]

# Default categories mapping for flat files (keyword based)
# If a keyword matches the name or description, assign that category.
# Order matters: first match wins.
CATEGORY_MAPPINGS = {
    "00_유형.md": [
        ("이형체|슬라임|괴물", "이형"),
        ("야수|식물", "자연"),
        ("천사|악마|정령|요정", "신비"),
        ("구조물|기계", "인공"),
        ("드래곤|거인", "초월"),
        ("인간형", "일반"),
        ("언데드", "불사"),
        ("", "기타"),  # Default
    ],
    "01_크기.md": [
        ("초소형|벌레", "초소형"),
        ("소형|작은", "소형"),
        ("중형|인간", "중형"),
        ("대형|곰|말", "대형"),
        ("거대|용|건물", "초거대"),
        ("", "일반"),
    ],
    "02_기원.md": [
        ("자연|돌연변이|알", "자연"),
        ("인공|기계|실험", "인공"),
        ("이계|차원|별|우주", "이계"),
        ("신|악마|정령|마법|고대", "신비"),
        ("저주|타락|비극", "저주"),
        ("", "기타"),
    ],
    "04_지성.md": [
        ("천재|고지능", "천재"),
        ("인간|학습", "지성"),
        ("짐승|본능", "본능"),
        ("집단|군집", "집단"),
        ("", "일반"),
    ],
    "06_이동.md": [
        ("날개|비행|부유", "비행"),
        ("수영|잠수|물", "수중"),
        ("지하|굴", "지하"),
        ("텔레포트|차원", "특수"),
        ("", "지상"),
    ],
    "07_감각.md": [
        ("시각|눈", "시각"),
        ("청각|소리", "청각"),
        ("후각|냄새", "후각"),
        ("마력|기운", "마력"),
        ("", "육감"),
    ],
    "08_약점.md": [
        ("불|물|얼음|번개", "속성"),
        ("은|철|나무", "재질"),
        ("정신|공포", "정신"),
        ("태양|물|환경", "환경"),
        ("", "물리"),
    ],
    "12_외교.md": [
        ("공격|전쟁|약탈", "공격"),
        ("동맹|평화|무역", "우호"),
        ("중립|고립", "중립"),
        ("", "특수"),
    ],
}


def determine_category_by_mapping(filename, name, desc):
    mappings = CATEGORY_MAPPINGS.get(filename, [("", "일반")])
    text = (name + " " + desc).lower()

    for pattern, category in mappings:
        if not pattern:  # Default case
            return category
        if re.search(pattern, text):
            return category
    return "기타"


def process_file(filename):
    filepath = os.path.join(TRAIT_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    current_section = "일반"

    # Check if file already has 3 columns (roughly)
    # We look at the separator line. If it has 3 or more pipes like |---|---|---|, it's likely done.
    # But wait, some have 4 columns. We target 2-column files to upgrade to 3.
    # Typical header: | 키워드 | 설명 | -> | 키워드 | 분류 | 설명 |

    separator_idx = -1
    for i, line in enumerate(lines):
        if "| :---" in line or "|---" in line:
            separator_idx = i
            break

    if separator_idx == -1:
        print(f"Skipping {filename}: No table found.")
        return

    # Check column count
    header_line = lines[separator_idx - 1]
    col_count = header_line.count("|") - 1
    if col_count >= 3:
        print(f"Skipping {filename}: Already has {col_count} columns.")
        return

    print(f"Processing {filename}...")

    i = 0
    while i < len(lines):
        line = lines[i]

        # Update section if in Section Mode
        if filename in SECTION_MODE_FILES:
            if line.strip().startswith("###"):
                current_section = line.strip().replace("#", "").strip()
                # Remove common prefixes like "01. " if present? No, keep it simple.
                # Just take the first word or two? "사회성 및 관계" -> "사회성"
                current_section = current_section.split(" ")[0]

        # Process Table Header
        if i == separator_idx - 1:
            # Add "분류" column
            # Assumes format: | Name | Desc |
            parts = [p.strip() for p in line.strip().split("|") if p]
            new_header = f"| {parts[0]} | 분류 | {parts[1]} |\n"
            new_lines.append(new_header)
        elif i == separator_idx:
            # Add separator
            parts = [p.strip() for p in line.strip().split("|") if p]
            new_sep = "| :--- | :---: | :--- |\n"
            new_lines.append(new_sep)
        # Process Table Row
        elif (
            line.strip().startswith("|")
            and not line.strip().startswith("|-")
            and "---" not in line
        ):
            parts = [p.strip() for p in line.strip().split("|") if p]
            if len(parts) >= 2:
                name = parts[0]
                desc = parts[1]

                # Determine Category
                category = "기타"
                if filename in SECTION_MODE_FILES:
                    category = current_section
                else:
                    category = determine_category_by_mapping(filename, name, desc)

                # Reconstruct line
                # Handle cases where description contains pipes? unlikely for this dataset but good to know.
                # Just naive join.
                new_row = f"| {name} | {category} | {desc} |\n"
                new_lines.append(new_row)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

        i += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"Updated {filename}")


def main():
    files = sorted([f for f in os.listdir(TRAIT_DIR) if f.endswith(".md")])
    targets = SECTION_MODE_FILES + list(CATEGORY_MAPPINGS.keys())

    for f in files:
        if f in targets:
            process_file(f)


if __name__ == "__main__":
    main()
