import re
from collections import Counter

def load_existing_tags(filepath):
    tags = set()
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        # **태그, 태그** 형태 추출
        matches = re.findall(r'\*\*(.*?)\*\*', content)
        for match in matches:
            for tag in match.split(','):
                tags.add(tag.strip())
    return tags

def analyze_descriptions(filepath, existing_tags):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 설명 부분만 추출 (테이블의 두 번째 컬럼)
    descriptions = []
    lines = content.split('\n')
    for line in lines:
        if line.startswith('|') and '어빌리티명' not in line and '---' not in line:
            cols = line.split('|')
            if len(cols) >= 3:
                descriptions.append(cols[2].strip())
                
    # 단어 빈도 분석 (간단한 공백 분리 및 특수문자 제거)
    words = []
    for desc in descriptions:
        # 한글, 영어만 남기고 제거
        clean_desc = re.sub(r'[^\w\s가-힣]', ' ', desc)
        for word in clean_desc.split():
            if len(word) > 1: # 1글자 제외
                words.append(word)
                
    counter = Counter(words)
    
    # 기존 태그에 없는 상위 빈도 단어 추출
    new_candidates = []
    for word, count in counter.most_common(200):
        if word not in existing_tags:
            new_candidates.append((word, count))
            
    return new_candidates, counter

def generate_analysis_report(candidates, counter, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 마법 권역 어빌리티 태그 분석\n\n")
        f.write("> **분석 대상:** `report/마법권역_어빌리티_설명_목록.md`\n")
        f.write("> **목적:** 마법 권역 특화 태그 도출\n\n")
        
        f.write("## 1. 신규 태그 후보 (빈도수 상위 200)\n")
        f.write("기존 물리 권역 태그에 포함되지 않은 단어들입니다.\n\n")
        f.write("| 순위 | 단어 | 빈도 | 비고 |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        
        for i, (word, count) in enumerate(candidates):
            f.write(f"| {i+1} | {word} | {count} | |\n")
            
        f.write("\n## 2. 주요 키워드 제안\n")
        f.write("분석 결과를 바탕으로 한 카테고리별 제안입니다. (자동 생성됨, 검토 필요)\n\n")
        
        # 간단한 키워드 매칭 규칙으로 제안
        magic_keywords = ['마력', '원소', '주문', '캐스팅', '소환', '결계', '아티팩트']
        f.write("### [마법 운용]\n")
        f.write(f"- 추천 키워드: {', '.join([w for w in magic_keywords if counter[w] > 0])}\n")

if __name__ == "__main__":
    protocol_path = "report/ability_tag_protocol.md"
    desc_path = "report/마법권역_어빌리티_설명_목록.md"
    output_path = "report/마법권역_어빌리티_태그_분석.md"
    
    print("Loading existing tags...")
    existing_tags = load_existing_tags(protocol_path)
    
    print("Analyzing descriptions...")
    candidates, counter = analyze_descriptions(desc_path, existing_tags)
    
    print(f"Generating report at {output_path}...")
    generate_analysis_report(candidates, counter, output_path)
    print("Done.")