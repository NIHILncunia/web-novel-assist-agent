ALLOWED_VALUES = {
    "계통": ["물리", "원소", "정신", "소환", "치유", "생산", "특수"],
    "대상": ["자신", "단일", "다수", "범위", "탈것", "해당 없음"],
    "피해 유형": [
        "해당 없음",
        "참격",
        "관통",
        "타격",
        "화염",
        "냉기",
        "전기",
        "산성",
        "독",
        "광휘",
        "폭풍",
        "수류",
        "플라즈마",
        "정신",
        "사령",
        "방사능",
        "역장",
        "공허",
        "고정",
    ],
    "상태 이상 유형": [
        "해당 없음",
        "출혈",
        "심층 창상",
        "신체 훼손",
        "방어구 관통",
        "기절",
        "골절",
        "넉백",
        "침묵",
        "화상",
        "공포",
        "부식",
        "동상",
        "동결",
        "둔화",
        "마비",
        "감전",
        "중독",
        "실명",
        "혼란",
        "표적",
        "젖음",
        "질식",
        "수면",
        "광분",
        "부패",
        "허약",
        "오염",
        "변이",
        "속박",
        "소멸",
        "처형",
    ],
}

FILES = {
    "data/skill/발동.md": ["계통", "대상", "피해 유형", "상태 이상 유형"],
    "data/skill/지속.md": ["계통", "대상", "피해 유형", "상태 이상 유형"],
}

with open("validation_report.md", "w", encoding="utf-8") as out:
    for file, cols in FILES.items():
        out.write(f"Checking {file}...\n")
        try:
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            out.write(f"File not found: {file}\n")
            continue

        # Find table header to map columns
        header_idx = -1
        col_map = {}

        for i, line in enumerate(lines):
            if line.strip().startswith("|") and "이름" in line:
                header_idx = i
                headers = [h.strip() for h in line.strip().split("|")[1:-1]]
                for col in cols:
                    try:
                        col_map[col] = headers.index(col)
                    except ValueError:
                        out.write(f"Warning: Column '{col}' not found in header.\n")
                break

        if header_idx == -1:
            out.write("No table found.\n")
            continue

        issues_found = 0
        # Check data rows (skip separator line)
        for i, line in enumerate(lines[header_idx + 2 :], start=header_idx + 3):
            if not line.strip().startswith("|"):
                continue

            parts = [p.strip() for p in line.strip().split("|")[1:-1]]

            row_issues = []
            name = parts[0] if parts else "Unknown"

            for col_name, col_idx in col_map.items():
                if col_idx < len(parts):
                    val = parts[col_idx]
                    clean_val = val.replace("*", "").strip()

                    if clean_val not in ALLOWED_VALUES[col_name]:
                        row_issues.append(f"{col_name}: '{clean_val}'")
                else:
                    row_issues.append(f"{col_name}: Missing")

            if row_issues:
                issues_found += 1
                out.write(f"  [Line {i}] **{name}**: {', '.join(row_issues)}\n")

        if issues_found == 0:
            out.write("  No issues found.\n")
        else:
            out.write(f"  Total issues: {issues_found}\n")
        out.write("-" * 40 + "\n")
