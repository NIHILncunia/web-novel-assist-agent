import re
import sys
from collections import Counter

def extract_nouns(input_file, output_file, title):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.splitlines()
    word_counts = []
    for line in lines:
        if line.startswith('|') and '순위' not in line and '---' not in line:
            cols = line.split('|')
            if len(cols) >= 4:
                phrase = cols[2].strip()
                try:
                    count = int(cols[3].strip())
                    word_counts.append((phrase, count))
                except ValueError: continue
    predicates = ['함으로써', '시킨다', '시킴으로써', '하여서', '하거나', '하도록', '하므로', '하여', '하며', '하고', '한다', '하게', '한', '할', '함', '기', '시킨', '시킬']
    particles = ['로부터', '에서', '에게', '으로', '부터', '까지', '보다', '조차', '마저', '은', '는', '이', '가', '을', '를', '의', '에', '와', '과', '로', '도', '만']
    noun_counter = Counter()
    for phrase, count in word_counts:
        phrase = re.sub(r'[\(\)]', '', phrase)
        for p in predicates:
            if phrase.endswith(p) and len(phrase) > len(p):
                phrase = phrase[:-len(p)]; break
        for p in particles:
            if phrase.endswith(p) and len(phrase) > len(p):
                phrase = phrase[:-len(p)]; break
        stop_words = ['자신', '것', '수', '등', '적', '전', '후', '내', '외', '시', '중', '그', '이', '저', '개']
        if len(phrase) >= 2 and phrase not in stop_words:
            noun_counter[phrase] += count
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# " + title + "\n\n")
        f.write("> **분석 대상:** " + input_file + "\n")
        f.write("> **추출 방식:** 어절 끝의 조사 및 서술어 어미 제거를 통한 명사형 추출\n\n")
        f.write("## 💎 핵심 명사 목록 (빈도순)\n\n")
        f.write("| 순위 | 명사 | 빈도 | 비고 |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for i, (noun, count) in enumerate(noun_counter.most_common()):
            f.write("| " + str(i+1) + " | " + noun + " | " + str(count) + " | |\n")

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        extract_nouns(sys.argv[1], sys.argv[2], sys.argv[3])