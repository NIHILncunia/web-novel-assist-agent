import os
import re

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_mapping(keyword):
    """
    초능력 키워드를 분석하여 [권역, 계통, 형태]를 매핑합니다.
    """
    k = keyword.replace(" ", "")
    
    # [G. 경계 권역]
    if '미디어' in k or '거울' in k or '그림' in k and '가둘' in k: return '경계', '매체계', '경계침투'
    if '그림' in k and '실체화' in k: return '경계', '매체계', '투영'
    if '분열' in k or '분리' in k: return '경계', '분리계', '분열'
    if '합체' in k or '합성' in k: return '경계', '분리계', '융합'

    # [H. 초상 권역]
    if '고체화' in k or '고형화' in k: return '초상', '위상계', '고형화'
    if '투과' in k or '통과' in k: return '초상', '위상계', '투과'
    if '언령' in k or '발음' in k or '단어' in k: return '초상', '정의계', '언령'
    if '진실' in k or '거짓말' in k: return '초상', '정의계', '진실'

    # [D. 특수 권역] - 기존 확장
    if '시간' in k or '과거' in k or '미래' in k: return '특수', '인과계', '시간'
    if '공간' in k or '이동' in k or '문' in k: return '특수', '공간계', '이동'
    if '운명' in k or '인연' in k: return '특수', '인과계', '운명'
    if '행운' in k or '불운' in k: return '특수', '인과계', '확률'
    if '규칙' in k or '법칙' in k: return '특수', '규칙계', '법칙'

    # [C. 정신 권역]
    if '기억' in k or '세뇌' in k or '조종' in k and ('사람' in k or '타인' in k): return '정신', '간섭계', '조작'
    if '텔레파시' in k or '독심' in k or '마음' in k: return '정신', '감지계', '독심'
    if '염동력' in k or '물건' in k and '조종' in k: return '정신', '구현계', '염동력'

    # [B. 물리 권역]
    if '신체' in k and ('변형' in k or '강화' in k): return '물리', '육체계', '변형'
    if '재생' in k or '회복' in k: return '물리', '육체계', '재생'
    if '빠르게' in k or '비행' in k or '날' in k: return '물리', '신법계', '기동'

    # [A. 마법 권역] - 원소
    if any(x in k for x in ['불', '화염', '물', '얼음', '바람', '번개', '땅', '바위']): return '마법', '방출계', '원소'

    return '기타', '미분류', '기타'

def main():
    source_path = 'data/word_list/character/초능력.md'
    base_output_dir = 'data/ability/detailed_lists'
    
    if not os.path.exists(source_path):
        print(f"Error: {source_path} not found.")
        return

    with open(source_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    count = 0
    
    for line in lines:
        if not line.strip().startswith('|') or '---' in line or '키워드' in line:
            continue
            
        parts = [p.strip() for p in line.split('|')]
        if len(parts) < 4: continue
            
        keyword = parts[2]
        desc = parts[3]
        example = parts[4] if len(parts) > 4 else ""
        
        domain, lineage, form = get_mapping(keyword)
        
        if domain == '기타': continue

        # 폴더 매핑
        domain_map = {
            '마법': '1.마법권역', '물리': '2.물리권역', '정신': '3.정신권역',
            '특수': '4.특수권역', '전술': '5.전술권역', '생산': '6.생산권역',
            '경계': '7.경계권역', '초상': '8.초상권역'
        }
        
        folder = domain_map.get(domain, '99.기타')
        filename = f"{domain}_{lineage}_{form}.md"
        file_path = os.path.join(base_output_dir, folder, filename)
        
        ensure_dir(file_path)
        
        # 헤더 생성
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# {domain} - {lineage} - {form}

")
                f.write(f"| 어빌리티명 | 설명 | 예시 |
")
                f.write("| :--- | :--- | :--- |
")
        
        # 내용 추가
        with open(file_path, 'a', encoding='utf-8') as f:
            clean_name = keyword.replace("수 있는", "").replace("하는", "").strip()
            f.write(f"| **{clean_name}** | {desc} | {example} |
")
            
        count += 1

    print(f"Migration Complete: {count} abilities processed.")

if __name__ == "__main__":
    main()
