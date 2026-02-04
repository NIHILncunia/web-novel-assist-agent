import os

def classify_mental_nouns(input_file, output_file):
    if not os.path.exists(input_file): return
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    nouns = []
    for line in lines:
        if line.startswith('|') and '순위' not in line and '---' not in line:
            cols = line.split('|')
            if len(cols) >= 4:
                noun = cols[2].strip()
                try:
                    nouns.append((noun, int(cols[3].strip())))
                except ValueError: continue
    categories = {
        "정신 영역 (Domain)": ["정신", "인지", "감정", "기억", "의지", "의식", "사고", "마음", "심리", "뇌", "신경"],
        "간섭/조작 (Interference)": ["간섭", "조작", "소거", "주입", "동조", "매료", "지우거나", "바꾸거나", "최면", "암시", "조종"],
        "감지/예지 (Detection)": ["감지", "예지", "추적", "탐색", "통찰", "투시", "관찰", "읽어", "파악"],
        "영향/효과 (Effect)": ["혼란", "공포", "위압", "충격", "가속", "고양", "평정", "매료", "유혹", "공포", "위압", "압박", "분노", "슬픔", "즐거움"],
        "성질/강도 (Attribute)": ["강력", "일시적", "강제", "보이지", "않는", "흐릿", "점진적", "비약적", "동시", "연속"]
    }
    classified_data = {cat: [] for cat in categories}
    others = []
    for noun, count in nouns:
        matched = False
        for cat, keywords in categories.items():
            if any(key in noun for key in keywords):
                classified_data[cat].append((noun, count))
                matched = True; break
        if not matched: others.append((noun, count))
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 정신 권역 명사 분류 리포트\n\n")
        f.write("> **분석 기반:** `report/정신권역_어빌리티_명사_분석.md`\n\n")
        for cat, items in classified_data.items():
            f.write("## 📂 " + cat + "\n")
            f.write("| 명사 | 빈도 | 비고 |\n| :--- | :--- | :--- |\n")
            for noun, count in sorted(items, key=lambda x: x[1], reverse=True):
                f.write("| " + noun + " | " + str(count) + " | |\n")
            f.write("\n")
        f.write("## 📂 기타/미분류 (Others)\n")
        f.write("| 명사 | 빈도 | 비고 |\n| :--- | :--- | :--- |\n")
        for noun, count in sorted(others, key=lambda x: x[1], reverse=True):
            f.write("| " + noun + " | " + str(count) + " | |\n")

if __name__ == "__main__":
    classify_mental_nouns("report/정신권역_어빌리티_명사_분석.md", "report/정신권역_명사_분류_리포트.md")