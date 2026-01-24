import collections

FILES = ["data/ability/발동.md", "data/ability/지속.md"]

ALLOWED_VALUES = {
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


def analyze_file(filepath, out):
    out.write(f"\n### Analyzing {filepath}...\n")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        out.write("File not found.\n")
        return

    header_idx = -1
    col_map = {}

    damage_counts = collections.Counter()
    status_counts = collections.Counter()

    for i, line in enumerate(lines):
        if line.strip().startswith("|") and "이름" in line:
            header_idx = i
            headers = [h.strip() for h in line.strip().split("|")[1:-1]]
            try:
                col_map["피해 유형"] = headers.index("피해 유형")
                col_map["상태 이상 유형"] = headers.index("상태 이상 유형")
            except ValueError:
                pass
            continue

        if header_idx != -1 and i > header_idx + 1:
            if not line.strip().startswith("|"):
                continue
            parts = [p.strip() for p in line.strip().split("|")[1:-1]]

            if "피해 유형" in col_map and col_map["피해 유형"] < len(parts):
                val = parts[col_map["피해 유형"]].replace("*", "").strip()
                if not val:
                    val = "해당 없음"  # Treat empty as default
                damage_counts[val] += 1

            if "상태 이상 유형" in col_map and col_map["상태 이상 유형"] < len(parts):
                val = parts[col_map["상태 이상 유형"]].replace("*", "").strip()
                if not val:
                    val = "해당 없음"
                status_counts[val] += 1

    out.write("\n**[피해 유형 (Damage Type) Stats]**\n")
    for val, count in damage_counts.most_common():
        status = "✅" if val in ALLOWED_VALUES["피해 유형"] else "❌ (Invalid)"
        out.write(f"- {val}: {count} {status}\n")

    out.write("\n**[상태 이상 유형 (Status Effect) Stats]**\n")
    for val, count in status_counts.most_common():
        status = "✅" if val in ALLOWED_VALUES["상태 이상 유형"] else "❌ (Invalid)"
        out.write(f"- {val}: {count} {status}\n")
    out.write("-" * 40 + "\n")


with open("validation_report.md", "w", encoding="utf-8") as out:
    out.write("# Damage Type and Status Effect Statistics\n")
    for f in FILES:
        analyze_file(f, out)
