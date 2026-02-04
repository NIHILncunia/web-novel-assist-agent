import os
import re

def extract_descriptions(directory):
    results = {}
    
    # 디렉토리 내 모든 md 파일 순회
    for filename in os.listdir(directory):
        if not filename.endswith(".md"):
            continue
            
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 테이블 행 추출 (헤더와 구분선 제외)
        lines = content.split('\n')
        table_started = False
        headers = []
        
        file_data = []
        
        for line in lines:
            line = line.strip()
            if not line.startswith('|'):
                continue
                
            # 구분선 건너뛰기
            if '---' in line:
                table_started = True
                continue
                
            # 헤더 파싱 (아직 테이블 시작 전이고, |로 시작하는 첫 줄이면 헤더로 간주)
            if not table_started and not headers:
                headers = [h.strip() for h in line.strip('|').split('|')]
                continue
                
            # 데이터 행 파싱
            if table_started:
                cols = [c.strip() for c in line.strip('|').split('|')]
                if len(cols) < 2: continue
                
                # 인덱스 찾기 (이름, 설명 등)
                try:
                    name_idx = 0 # 보통 첫번째가 이름
                    desc_idx = -1 # 보통 마지막이 설명
                    
                    # 헤더가 있다면 더 정확히 찾기 시도
                    if headers:
                        for i, h in enumerate(headers):
                            if '이름' in h: name_idx = i
                            if '설명' in h: desc_idx = i
                            
                    name = cols[name_idx].replace('**', '') # 볼드 제거
                    desc = cols[desc_idx]
                    
                    if name and desc:
                        file_data.append({'name': name, 'desc': desc})
                except IndexError:
                    continue

        if file_data:
            results[filename] = file_data
            
    return results

def generate_report(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 마법 권역 어빌리티 설명 목록\n\n")
        f.write(f"> **생성일:** 2026-02-04\n")
        f.write(f"> **대상 파일 수:** {len(data)}개\n\n")
        
        for filename, abilities in sorted(data.items()):
            f.write(f"## 📂 {filename}\n")
            f.write("| 어빌리티명 | 설명 |\n")
            f.write("| :--- | :--- |\n")
            for ab in abilities:
                f.write(f"| {ab['name']} | {ab['desc']} |\n")
            f.write("\n")

if __name__ == "__main__":
    target_dir = "data/ability/detailed_lists/1.마법권역"
    output_path = "report/마법권역_어빌리티_설명_목록.md"
    
    print(f"Extracting from {target_dir}...")
    data = extract_descriptions(target_dir)
    
    print(f"Generating report at {output_path}...")
    generate_report(data, output_path)
    print("Done.")