import os

def classify_nouns(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 명사와 빈도 추출
    nouns = []
    for line in lines:
        if line.startswith('|') and '순위' not in line and '---' not in line:
            cols = line.split('|')
            if len(cols) >= 4:
                noun = cols[2].strip()
                try:
                    count = int(cols[3].strip())
                    nouns.append((noun, count))
                except ValueError:
                    continue

    # 카테고리 정의 및 키워드 매핑
    categories = {
        "원천/에너지 (Source)": ["마력", "마나", "생명력", "영혼", "신성", "저주", "기운", "원천", "마기", "신성력", "활력", "에너지", "마법", "흑마법", "주술", "정전기", "태양", "지맥"],
        "원소/속성 (Element)": ["화염", "번개", "바람", "대지", "빛", "어둠", "얼음", "냉기", "전기", "독", "산성", "용암", "금속", "흙", "바위", "물", "불", "벼락", "전류", "산성비", "불꽃", "진흙", "모래바람", "도깨비불", "광선", "빛"],
        "작동/메커니즘 (Mechanism)": ["주입", "방출", "전개", "계약", "소환", "구현", "제어", "발사", "투사", "가속", "응축", "압축", "변환", "조작", "설치", "부여", "발동", "생성", "사용", "행사", "유인", "기습", "돌진", "비행", "회피", "해제", "분석", "재현", "투사", "공급", "활성화", "감지", "지혈", "이식", "제조"],
        "형태/매체 (Medium)": ["결계", "장벽", "구체", "광선", "룬", "마법진", "아티팩트", "물약", "무기", "사슬", "고리", "구역", "지대", "영역", "도구", "매개체", "솥", "영약", "인형", "골렘", "깃발", "전차", "날개", "분신", "복제품", "장치", "그물", "낙인", "문자", "보석"],
        "영향/결과 (Effect)": ["회복", "재생", "폭발", "파괴", "변이", "환영", "소생", "노화", "탈진", "강화", "약화", "마비", "치유", "손상", "소멸", "정화", "수리", "봉인", "중독", "폭주", "과부하", "상승", "감소", "봉합", "초토화", "망각", "유혹", "환각", "복종", "붕괴", "수복", "동기화", "변형"],
        "대상/범위 (Target)": ["시전자", "아군", "적들", "주변", "공간", "영역", "신체", "심장", "육체", "피부", "장기", "근육", "뼈", "지면", "땅", "반경", "직선", "광범위", "단일", "다수", "범위", "지역", "위치", "전방", "내부", "외부", "자신", "대상", "피해자", "목표"]
    }

    classified_data = {cat: [] for cat in categories}
    others = []

    for noun, count in nouns:
        matched = False
        for cat, keywords in categories.items():
            if any(key in noun for key in keywords):
                classified_data[cat].append((noun, count))
                matched = True
                break
        if not matched:
            others.append((noun, count))

    # 결과 리포트 작성
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 마법 권역 명사 분류 리포트\n\n")
        f.write("> **분석 기반:** `report/마법권역_어빌리티_명사_분석.md`\n")
        f.write("> **목적:** 어빌리티 설계를 위한 구성 요소(레고 블록) 체계화\n\n")

        for cat, items in classified_data.items():
            f.write(f"## 📂 {cat}\n")
            f.write("| 명사 | 빈도 | 비고 |\n")
            f.write("| :--- | :--- | :--- |\n")
            for noun, count in sorted(items, key=lambda x: x[1], reverse=True):
                f.write(f"| {noun} | {count} | |\n")
            f.write("\n")

        f.write("## 📂 기타/미분류 (Others)\n")
        f.write("| 명사 | 빈도 | 비고 |\n")
        f.write("| :--- | :--- | :--- |\n")
        for noun, count in sorted(others, key=lambda x: x[1], reverse=True):
            f.write(f"| {noun} | {count} | |\n")
        f.write("\n")

if __name__ == "__main__":
    classify_nouns("report/마법권역_어빌리티_명사_분석.md", "report/마법권역_명사_분류_리포트.md")