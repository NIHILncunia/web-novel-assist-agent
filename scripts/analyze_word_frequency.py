import re
import sys
from collections import Counter

def analyze_word_frequency(input_file, output_file, title):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    descriptions = []
    lines = content.splitlines()
    for line in lines:
        if line.startswith('|') and '어빌리티명' not in line and '---' not in line:
            cols = line.split('|')
            if len(cols) >= 3:
                descriptions.append(cols[2].strip())
    all_phrases = []
    for desc in descriptions:
        clean_desc = re.sub(r'[\.\?\!\,]', '', desc)
        phrases = clean_desc.split()
        all_phrases.extend(phrases)
    counter = Counter(all_phrases)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"> **분석 대상:** {input_file}\n")
        f.write(f"> **분석 방법:** 공백(' ') 단위 분절 및 빈도 계산\n")
        f.write(f"> **전체 어절 수:** {len(all_phrases)}개\n")
        f.write(f"> **고유 어절 수:** {len(counter)}개\n\n")
        f.write("## 📊 전체 어절 빈도 목록\n\n")
        f.write("| 순위 | 어절 | 빈도 | 비고 |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for i, (phrase, count) in enumerate(counter.most_common()):
            f.write(f"| {i+1} | {phrase} | {count} | |\n")

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        analyze_word_frequency(sys.argv[1], sys.argv[2], sys.argv[3])