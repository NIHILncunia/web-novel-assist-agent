import os

def get_mapping(keyword, desc):
    k = keyword.replace(" ", "")
    d = desc.replace(" ", "")
    
    # [G. 경계 권역]
    if any(x in k for x in ['미디어', '거울', '그림', '화면', '디지털']): return '경계:매체계:경계침투'
    if '실체화' in k and '그림' in k: return '경계:매체계:투영'
    if any(x in k for x in ['분열', '분리', '조각화']): return '경계:분리계:분열'
    if any(x in k for x in ['합체', '융합', '합성']): return '경계:분리계:융합'

    # [H. 초상 권역]
    if any(x in k for x in ['고체화', '고형화', '굳히']): return '초상:위상계:고형화'
    if any(x in k for x in ['투과', '통과', '비물질']): return '초상:위상계:투과'
    if any(x in k for x in ['언령', '발음', '단어', '말하는대']): return '초상:정의계:언령'
    if any(x in k for x in ['진실', '거짓말']): return '초상:정의계:진실'

    # [D. 특수 권역]
    if any(x in k for x in ['시간', '과거', '미래', '회귀', '정지', '가속', '지연']): return '특수:인과계:시간'
    if any(x in k for x in ['공간', '이동', '문', '텔레포트', '점멸', '차원']): return '특수:공간계:이동'
    if any(x in k for x in ['운명', '인연', '실', '수명']): return '특수:인과계:운명'
    if any(x in k for x in ['행운', '불운', '운']): return '특수:인과계:확률'
    if any(x in k for x in ['규칙', '법칙', '무시']): return '특수:규칙계:법칙'

    # [C. 정신 권역]
    if any(x in k for x in ['기억', '세뇌', '지배', '조종', '최면']): return '정신:간섭계:조작'
    if any(x in k for x in ['텔레파시', '독심', '마음', '속마음']): return '정신:감지계:독심'
    if any(x in k for x in ['염력', '염동력', '손을대지않고']): return '정신:구현계:염동력'
    if any(x in k for x in ['예지', '예견', '미리알']): return '정신:감지계:예지'

    # [B. 물리 권역]
    if '신체' in k and ('변형' in k or '강화' in k or '바꾸'): return '물리:육체계:변형'
    if any(x in k for x in ['재생', '회복', '치유', '낫는']): return '물리:육체계:재생'
    if any(x in k for x in ['빠르게', '비행', '날수', '신속']): return '물리:신법계:기동'
    if any(x in k for x in ['단단한', '금강불괴']): return '물리:육체계:경화'

    # [A. 마법 권역] - 원소
    if any(x in k for x in ['불', '화염', '열기', '태우']): return '마법:방출계:화염'
    if any(x in k for x in ['물', '홍수', '비', '수분', '액체']): return '마법:조작계:물'
    if any(x in k for x in ['얼음', '빙하', '냉기', '서리', '눈', '동결']): return '마법:생성계:얼음'
    if any(x in k for x in ['바람', '공기', '태풍', '폭풍', '기류']): return '마법:조작계:바람'
    if any(x in k for x in ['전기', '번개', '낙뢰', '전류']): return '마법:방출계:전기'
    if any(x in k for x in ['땅', '흙', '바위', '암석', '모래']): return '마법:생성계:대지'
    if any(x in k for x in ['빛', '레이저', '광선']): return '마법:방출계:빛'
    if any(x in k for x in ['어둠', '그림자']): return '마법:조작계:어둠'
    if any(x in k for x in ['독', '산성', '가스']): return '마법:방출계:독'

    return '미분류:미분류:미분류'

def main():
    temp_path = 'data/word_list/character/초능력_mapping_temp.md'
    if not os.path.exists(temp_path): return
    
    with open(temp_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|'):
            if '---' in stripped:
                new_lines.append(stripped + ' :---: |\n')
                continue
            
            parts = [p.strip() for p in line.split('|')]
            if len(parts) > 3:
                if '키워드' in parts[2]:
                    new_lines.append(stripped + ' 매핑 결과 |\n')
                    continue
                
                keyword = parts[2]
                desc = parts[3]
                mapping = get_mapping(keyword, desc)
                new_lines.append(stripped + f' {mapping} |\n')
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(temp_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    main()