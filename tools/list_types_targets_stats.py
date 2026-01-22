import collections

FILES = ["data/skill/발동.md", "data/skill/지속.md"]

ALLOWED_VALUES = {
    "계통": ["물리", "원소", "정신", "소환", "치유", "생산", "특수"],
    "대상": ["자신", "단일", "다수", "범위", "탈것", "해당 없음"],
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

    type_counts = collections.Counter()
    target_counts = collections.Counter()

    for i, line in enumerate(lines):
        if line.strip().startswith("|") and "이름" in line:
            header_idx = i
            headers = [h.strip() for h in line.strip().split("|")[1:-1]]
            try:
                col_map["계통"] = headers.index("계통")
                col_map["대상"] = headers.index("대상")
            except ValueError:
                pass
            continue

        if header_idx != -1 and i > header_idx + 1:
            if not line.strip().startswith("|"):
                continue
            parts = [p.strip() for p in line.strip().split("|")[1:-1]]

            if "계통" in col_map and col_map["계통"] < len(parts):
                val = parts[col_map["계통"]].replace("*", "").strip()
                type_counts[val] += 1

            if "대상" in col_map and col_map["대상"] < len(parts):
                val = parts[col_map["대상"]].replace("*", "").strip()
                target_counts[val] += 1

    out.write("\n**[계통 (Type) Stats]**\n")
    for val, count in type_counts.most_common():
        status = "✅" if val in ALLOWED_VALUES["계통"] else "❌ (Invalid)"
        out.write(f"- {val}: {count} {status}\n")

    out.write("\n**[대상 (Target) Stats]**\n")
    for val, count in target_counts.most_common():
        status = "✅" if val in ALLOWED_VALUES["대상"] else "❌ (Invalid)"
        out.write(f"- {val}: {count} {status}\n")
    out.write("-" * 40 + "\n")


with open("stats_report.md", "w", encoding="utf-8") as out:
    out.write("# Skill Types and Targets Statistics\n")
    for f in FILES:
        analyze_file(f, out)
