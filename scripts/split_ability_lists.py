import os
import re

# 소스 파일 경로
SOURCE_DIR = "data/ability"
OUTPUT_DIR = "data/ability/detailed_lists"
SOURCE_FILES = ["마법.md", "물리.md", "정신.md", "특수.md", "생산.md", "어빌리티.md"]

# 정규식 패턴 (테이블 행 파싱)
# | 이름 | 구조 | 계통 | 대상 | 피해 유형 | 상태 이상 유형 | 설명 |
ROW_PATTERN = re.compile(
    r"\|\s*\*\*(.*?)\*\*\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|"
)

# 구조 파싱 패턴: [권역:원천]-[계통]-[형태]
STRUCTURE_PATTERN = re.compile(r"\[(.*?):(.*?)]-\[(.*?)]-\[(.*?)]")


def get_all_combinations():
    guide_path = "manuals/99-1_ability_syntax.md"
    if not os.path.exists(guide_path):
        return {}

    with open(guide_path, "r", encoding="utf-8") as f:
        content = f.read()

    combinations = {}

    # 권역별 섹션 분리
    domain_sections = re.split(r"### \*\*[A-Z]\. ", content)[1:]

    for section in domain_sections:
        lines = section.split("\n")
        domain_match = re.search(r"^(.*?) 권역", lines[0])
        if not domain_match:
            continue
        domain_name = domain_match.group(1).strip()

        # 계통별 섹션 분리 (① ~ ⑥)
        l_sections = re.split(r"#### \*\*(?:[①-⑥]) ", section)[1:]
        for l_section in l_sections:
            l_lines = l_section.split("\n")
            # l_lines[0] 예: "방출계 (Emission)**"
            # 계통명 추출 (괄호 전까지 가져오고 '계' 삭제)
            lineage_line = l_lines[0].strip()
            lineage_match = re.search(
                r"^(.*?)(?:계)?(?:\s*\(.*?\))?\*\*?", lineage_line
            )

            if not lineage_match:
                continue

            lineage_name = lineage_match.group(1).strip()
            if not lineage_name:
                continue

            # 형태 추출: *   **[구체 (Orb)]** 등
            forms = re.findall(r"\*   \*\*\[(.*?)(?:\s*\(.*?\))?\]\*\*", l_section)
            for form_name in forms:
                safe_domain = re.sub(r'[\\/:*?"<>|]', "_", domain_name)
                safe_lineage = re.sub(r'[\\/:*?"<>|]', "_", lineage_name)
                safe_form = re.sub(r'[\\/:*?"<>|]', "_", form_name.strip())

                key = f"{safe_domain}_{safe_lineage}_{safe_form}"
                combinations[key] = []

    return combinations


def parse_abilities(combinations):
    abilities = combinations.copy()

    for filename in SOURCE_FILES:
        filepath = os.path.join(SOURCE_DIR, filename)
        if not os.path.exists(filepath):
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            match = ROW_PATTERN.search(line)
            if match:
                name = match.group(1).strip()
                structure = match.group(2).strip()
                lineage_col = match.group(3).strip()  # 테이블의 계통 컬럼 (참고용)
                target = match.group(4).strip()
                dmg_type = match.group(5).strip()
                status_effect = match.group(6).strip()
                desc = match.group(7).strip()

                # 구조 파싱
                struct_match = STRUCTURE_PATTERN.match(structure)
                if struct_match:
                    domain = struct_match.group(1).strip()
                    source = struct_match.group(2).strip()
                    lineage = struct_match.group(3).strip()
                    form = struct_match.group(4).strip()

                    # 계통명 정문화: '방출계' -> '방출'
                    lineage = re.sub(r"계$", "", lineage)

                    # 키 생성: 권역_계통_형태 (파일명에 적합하게)
                    # 예: 마법_방출_구체
                    safe_domain = re.sub(r'[\\/:*?"<>|]', "_", domain)
                    safe_lineage = re.sub(r'[\\/:*?"<>|]', "_", lineage)
                    safe_form = re.sub(r'[\\/:*?"<>|]', "_", form)

                    key = f"{safe_domain}_{safe_lineage}_{safe_form}"

                    if key not in abilities:
                        abilities[key] = []

                    abilities[key].append(
                        {
                            "name": name,
                            "structure": structure,
                            "source": source,
                            "form": form,
                            "target": target,
                            "dmg_type": dmg_type,
                            "status_effect": status_effect,
                            "desc": desc,
                        }
                    )

    return abilities


def write_files(abilities):
    for key, items in abilities.items():
        # 권역, 계통, 형태 분리 (파일명용)
        parts = key.split("_")
        if len(parts) < 3:
            continue
        domain = parts[0]
        lineage = parts[1]
        form = parts[2]

        filename = f"{key}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        content = f"# {domain} 권역 - {lineage} ({form})\n\n"
        content += f"> **권역:** {domain}\n"
        content += f"> **계통:** {lineage}\n"
        content += f"> **형태:** {form}\n\n"
        content += "---\n\n"
        content += "| 이름 | 원천 (Source) | 대상 | 피해 유형 | 상태 이상 | 설명 |\n"
        content += "| :--- | :---: | :---: | :---: | :---: | :--- |\n"

        if not items:
            content += "| - | - | - | - | - | 아직 정의된 어빌리티가 없습니다. |\n"
        else:
            for item in items:
                content += f"| **{item['name']}** | {item['source']} | {item['target']} | {item['dmg_type']} | {item['status_effect']} | {item['desc']} |\n"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"Successfully created {len(abilities)} list files.")


if __name__ == "__main__":
    initial_data = get_all_combinations()
    data = parse_abilities(initial_data)
    write_files(data)
