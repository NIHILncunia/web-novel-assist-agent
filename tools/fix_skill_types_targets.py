FILES = ["data/skill/발동.md", "data/skill/지속.md"]


def normalize_type(val):
    val = val.replace("*", "").strip()
    if not val:
        return "특수"

    # Priority mapping
    if any(k in val for k in ["치유", "회복", "의료"]):
        return "치유"
    if any(k in val for k in ["소환", "영혼"]):
        return "소환"
    if any(k in val for k in ["생산", "제작", "건설", "생활", "요리", "대장"]):
        return "생산"
    if any(
        k in val
        for k in [
            "정신",
            "감각",
            "지성",
            "지식",
            "매력",
            "심리",
            "운명",
            "지배",
            "정보",
            "탐색",
            "도발",
            "예지",
        ]
    ):
        return "정신"
    if any(
        k in val
        for k in [
            "원소",
            "화염",
            "냉기",
            "번개",
            "바람",
            "대지",
            "어둠",
            "빛",
            "신성",
            "흑마법",
            "마법",
            "주술",
        ]
    ):
        return "원소"
    if any(
        k in val
        for k in [
            "물리",
            "신체",
            "기술",
            "전투",
            "무구",
            "도구",
            "설치",
            "기교",
            "이동",
            "은신",
            "암살",
            "방어",
            "생존",
            "격투",
            "사격",
        ]
    ):
        return "물리"

    return "특수"


def normalize_target(val):
    val = val.replace("*", "").strip()
    if not val or val in ["해당 없음", "없음", "-"]:
        return "해당 없음"

    if any(k in val for k in ["자신", "본인"]):
        return "자신"
    if any(
        k in val
        for k in [
            "범위",
            "지역",
            "전장",
            "지점",
            "직선",
            "전역",
            "월드",
            "광역",
            "환경",
            "공간",
            "세계",
        ]
    ):
        return "범위"
    if any(k in val for k in ["다수", "군단", "모두"]):
        return "다수"
    if any(k in val for k in ["탈것", "탑승"]):
        return "탈것"

    # Default to single for specific entities
    return "단일"


def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header_idx = -1
    col_map = {}

    new_lines = []

    for i, line in enumerate(lines):
        if header_idx == -1 and line.strip().startswith("|") and "이름" in line:
            header_idx = i
            headers = [h.strip() for h in line.strip().split("|")[1:-1]]
            try:
                col_map["계통"] = headers.index("계통")
                col_map["대상"] = headers.index("대상")
            except ValueError:
                pass
            new_lines.append(line)
            continue

        if header_idx != -1 and i > header_idx + 1:  # Data rows
            if not line.strip().startswith("|"):
                new_lines.append(line)
                continue

            parts = [
                p.strip() for p in line.strip().split("|")[1:-1]
            ]  # Split and strip
            original_parts = line.strip().split(
                "|"
            )  # Split to keep original spacing if possible, but hard.
            # Reconstructing based on parts is safer for consistency.

            # Update values
            if "계통" in col_map and col_map["계통"] < len(parts):
                parts[col_map["계통"]] = f" {normalize_type(parts[col_map['계통']])} "
            if "대상" in col_map and col_map["대상"] < len(parts):
                parts[col_map["대상"]] = f" {normalize_target(parts[col_map['대상']])} "

            # Reconstruct row
            # Need to handle empty first/last slots from split
            # | val | val | -> split('|') gives ['', 'val', 'val', '']
            # My logic used split('|')[1:-1] which gives ['val', 'val']
            # So reconstruction is:
            new_row = "| " + " | ".join(parts) + " |\n"
            new_lines.append(new_row)

        else:
            new_lines.append(line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


for f in FILES:
    process_file(f)
