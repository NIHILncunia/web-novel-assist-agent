import os
import re

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def clean_name(name):
    """
    '~수 있는', '~하는' 등의 서술어를 제거하고 명사형으로 정제합니다.
    """
    name = name.strip()
    patterns = [
        r'을 수 있는$', r'를 수 있는$', r'할 수 있는$', r'될 수 있는$',
        r'하는$', r'되는$', r'시키는$', r'만드는$', r'부리는$',
        r'가진$', r'있는$', r'쓰는$', r'넣는$', r'않는$', r'바꾸는$'
    ]
    for p in patterns:
        name = re.sub(p, '', name)
    return name.strip()

def get_mapping(keyword, desc):
    k = keyword.replace(" ", "")
    d = desc.replace(" ", "")
    
    # [G. 경계 권역]
    if any(x in k for x in ['미디어', '거울', '그림', '화면', '디지털']): return '경계', '매체계', '경계침투', '매체'
    if '실체화' in k and '그림' in k: return '경계', '매체계', '투영', '그림'
    if any(x in k for x in ['분열', '분리', '조각화']): return '경계', '분리계', '분열', '자아'
    if any(x in k for x in ['합체', '융합', '합성']): return '경계', '분리계', '융합', '육체'
    if any(x in k for x in ['가상현실', '꿈속', '꿈과']): return '경계', '가상계', '가상환경', '꿈'

    # [H. 초상 권역]
    if any(x in k for x in ['고체화', '고형화', '굳히']): return '초상', '위상계', '고형화', '물질'
    if any(x in k for x in ['투과', '통과', '비물질']): return '초상', '위상계', '투과', '신체'
    if any(x in k for x in ['언령', '발음', '단어', '말하는대']): return '초상', '정의계', '언령', '언어'
    if any(x in k for x in ['진실', '거짓말']): return '초상', '정의계', '진실', '진실'
    if any(x in k for x in ['인연', '운명']): return '초상', '인연계', '인연조작', '운명'
    if any(x in k for x in ['행운', '불운']): return '초상', '인연계', '확률개변', '운'

    # [D. 특수 권역]
    if any(x in k for x in ['시간', '과거', '미래', '회귀', '정지', '가속', '지연']): return '특수', '인과계', '시간', '시간'
    if any(x in k for x in ['공간', '이동', '문', '텔레포트', '점멸', '차원']): return '특수', '공간계', '이동', '공간'
    if any(x in k for x in ['규칙', '법칙', '무시']): return '특수', '규칙계', '규칙', '법칙'
    if any(x in k for x in ['소환', '불러']): return '특수', '소환계', '호출', '마력'
    if any(x in k for x in ['봉인', '가두']): return '특수', '봉인계', '매체봉인', '봉인'
    if any(x in k for x in ['흡수', '강탈', '빼앗']): return '특수', '흡수계', '강탈', '에너지'
    if any(x in k for x in ['복사', '따라할']): return '특수', '흡수계', '복제', '기술'

    # [C. 정신 권역]
    if any(x in k for x in ['기억', '세뇌', '지배', '조종', '최면']): return '정신', '간섭계', '조작', '정신'
    if any(x in k for x in ['텔레파시', '독심', '마음', '속마음']): return '정신', '감지계', '독심', '생각'
    if any(x in k for x in ['염력', '염동력', '손을대지않고']): return '정신', '구현계', '원격조작', '정신력'
    if any(x in k for x in ['예지', '예견', '미리알']): return '정신', '감지계', '예지', '미래'
    if any(x in k for x in ['영혼', '귀신']): return '정신', '영혼계', '소통', '영혼'

    # [I. 생명 권역]
    if any(x in k for x in ['호르몬', '아드레날린']): return '생명', '조절계', '분비조절', '호르몬'
    if any(x in k for x in ['뼈', '피부', '외골격']): return '생명', '변이계', '조직강화', '신체'
    if any(x in k for x in ['피', '혈액']): return '생명', '조절계', '생체가속', '혈액'
    if any(x in k for x in ['키메라', '합성']): return '생명', '합성계', '생물융합', '유전자'

    # [B. 물리 권역]
    if '신체' in k and ('변형' in k or '강화' in k or '바꾸'): return '물리', '육체계', '변형', '신체'
    if any(x in k for x in ['재생', '회복', '치유', '낫는']): return '물리', '육체계', '재생', '생명력'
    if any(x in k for x in ['빠르게', '비행', '날수', '신속']): return '물리', '신법계', '도약', '신체'
    if any(x in k for x in ['단단한', '금강불괴']): return '물리', '육체계', '경화', '신체'
    if any(x in k for x in ['무기', '검', '창']): return '물리', '기교계', '숙련', '무기'

    # [A. 마법 권역] - 원소
    if any(x in k for x in ['불', '화염', '열기', '태우']): return '마법', '방출계', '파동', '화염'
    if any(x in k for x in ['물', '홍수', '비', '수분', '액체']): return '마법', '조작계', '제어', '물'
    if any(x in k for x in ['얼음', '빙하', '냉기', '서리', '눈', '동결']): return '마법', '생성계', '구현', '얼음'
    if any(x in k for x in ['바람', '공기', '태풍', '폭풍', '기류']): return '마법', '조작계', '제어', '바람'
    if any(x in k for x in ['전기', '번개', '낙뢰', '전류']): return '마법', '방출계', '광선', '전기'
    if any(x in k for x in ['땅', '흙', '바위', '암석', '모래']): return '마법', '생성계', '지형', '대지'
    if any(x in k for x in ['빛', '레이저', '광선']): return '마법', '방출계', '광선', '빛'
    if any(x in k for x in ['어둠', '그림자']): return '마법', '조작계', '제어', '어둠'
    if any(x in k for x in ['독', '산성', '가스']): return '마법', '방출계', '파동', '독'
    
    # [A. 마법 권역] - 기타
    if any(x in k for x in ['마법', '주문', '영창']): return '마법', '방출계', '연사', '마나'

    return '기타', '미분류', '기타', '미상'

def main():
    source_path = 'data/word_list/character/초능력.md'
    base_output_dir = 'data/ability/detailed_lists'
    
    if not os.path.exists(source_path):
        print(f"Error: {source_path} not found.")
        return

    with open(source_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    count = 0
    skipped = 0
    
    for line in lines:
        if not line.strip().startswith('|') or '---' in line or '키워드' in line:
            continue
            
        parts = [p.strip() for p in line.split('|')]
        if len(parts) < 4:
            continue
            
        keyword = parts[2]
        desc = parts[3]
        example = parts[4] if len(parts) > 4 else ""
        
        domain, lineage, form, source = get_mapping(keyword, desc)
        
        if domain == '기타':
            skipped += 1
            continue
            
        # 폴더명 매핑
        domain_folder_map = {
            '마법': '1.마법권역',
            '물리': '2.물리권역',
            '정신': '3.정신권역',
            '특수': '4.특수권역',
            '전술': '5.전술권역',
            '생산': '6.생산권역',
            '경계': '7.경계권역',
            '초상': '8.초상권역',
            '생명': '9.생명권역'
        }
        
        domain_folder = domain_folder_map.get(domain, '99.기타권역')
        filename = f"{domain}_{lineage}_{form}.md"
        file_path = os.path.join(base_output_dir, domain_folder, filename)
        
        ensure_dir(file_path)
        
        # 헤더 생성
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# {domain} - {lineage} - {form}\n\n")
                f.write(f"> **설명:** {domain} 권역의 {lineage}에 속하며, {form}의 형태로 발현되는 어빌리티 목록입니다.\n")
                f.write("---\n\n")
                f.write("| 어빌리티명 | 원천 | 설명 | 예시 |\n")
                f.write("| :--- | :---: | :--- | :--- |\n")
        
        ability_name = clean_name(keyword)
        
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f"| **{ability_name}** | {source} | {desc} | {example} |\n")
            
        count += 1

    print(f"Migration Complete: {count} abilities processed, {skipped} skipped.")

if __name__ == "__main__":
    main()