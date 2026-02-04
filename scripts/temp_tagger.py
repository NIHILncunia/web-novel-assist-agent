import os
import sys

# Ensure UTF-8 encoding for stdout/stderr
sys.stdout.reconfigure(encoding='utf-8')

def find_file(directory, pattern_start):
    for f in os.listdir(directory):
        if f.startswith(pattern_start) and f.endswith('.md'):
            return os.path.join(directory, f)
    return None

def run_tagging():
    # Find input file safely
    input_path = find_file('report', '물리권역_어빌리티_설명_목록')
    output_path = 'report/physical_ability_tags.md'

    if not input_path:
        print("Error: Input file starting with '물리권역_어빌리티_설명_목록' not found in report/")
        return

    # 태그 규칙 (마스터의 의도 반영)
    tag_rules = {
        '참격': ['베다', '베기', '참격', '벤다', '검', '도', '칼날', '난도질', '베어'],
        '타격': ['타격', '주먹', '둔기', '충격', '발차기', '펀치', '망치', '스윙', '가격', '내려치다', '강타', '부딪쳐', '밟아'],
        '관통': ['찌르다', '찌르기', '꿰뚫다', '관통', '창', '화살', '뚫어', '송곳니', '박아', '침'],
        '사격': ['발사', '사격', '쏘다', '쏘아', '저격', '활', '총', '탄', '볼트', '화살비'],
        '투척': ['투척', '던져', '던지다', '던짐', '부메랑'],
        '절단': ['절단', '참수', '단두대', '자르다', '끊어버린다', '인대 절단'],
        '파괴': ['파괴', '부수다', '으스러뜨리', '붕괴', '손상', '부러뜨린', '무너뜨려'],
        '파쇄/분쇄': ['파쇄', '분쇄', '으스러', '짓누른다', '압살', '으깨'],
        '증폭': ['증폭', '강화', '과부하', '한계', '배가', '상승', '고조', '폭발적', '부스트'],
        '기교': ['기교', '묘기', '변칙', '우아하게', '춤', '궤적', '스냅', '형식이 없는', '곡예', '서커스'],
        '도구': ['도구', '아이템', '연막', '폭발', '장치', '와이어', '탄두', '그물', '사슬'],
        '마력': ['마력', '마법', '마력 회로', '영창', '투기'],
        '흡혈': ['흡혈', '피를 빤다', '생명력을 빼앗아', '갈증'],
        '방어': ['막아', '방어', '방벽', '보호', '막는', '흘려', '쳐내', '튕겨', '방패', '가드', '엄폐'],
        '회피': ['피하다', '회피', '빗나가게', '잔상', '스텝'],
        '반격': ['반격', '카운터', '받아치다', '리포스트', '후속타', '요격'],
        '무력화': ['제압', '무력화', '구속', '포박', '봉쇄', '꺾다', '잡기', '메다꽂다', '넘어뜨리', '마비', '경직', '차단'],
        '기동성': ['이동', '도약', '돌진', '쇄도', '달리다', '뛰다', '날다', '비행', '순보', '기동', '낙하', '착지', '기습적으로'],
        '은신': ['은신', '숨기', '위장', '기척', '잠입', '그림자', '매복', '사각', '인식하지 못한'],
        '상태이상': ['출혈', '피', '기절', '의식', '뇌진탕', '혼란', '어지러움', '독', '맹독', '중독', '부식', '산성', '오물', '공포'],
        '즉사': ['즉사', '치명상', '숨통', '처형', '암살', '심장', '급소', '숨을 끊는다'],
        '범위': ['범위', '광역', '주변', '다수', '사방', '퍼붓다', '확산', '폭발', '일제히', '모든', '공간', '넓게', '흩뿌려', '휩쓴다'],
        '특수': ['시체', '뼈', '마술', '음식', '음료', '술', '짐승', '포효', '하울링', '포자', '음파']
    }

    def analyze_tags(text):
        tags = set()
        for tag, keywords in tag_rules.items():
            for keyword in keywords:
                if keyword in text:
                    tags.add(tag)
                    break 
        return sorted(list(tags))

    results = []
    total_processed = 0

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('- **'):
                parts = line.split('**:', 1)
                if len(parts) < 2:
                    parts = line.split('** :', 1)
                
                if len(parts) == 2:
                    name_part = parts[0].replace('- **', '').strip()
                    desc = parts[1].strip()
                    full_text = f'{name_part} {desc}'
                    tags = analyze_tags(full_text)
                    results.append(f'| **{name_part}** | {desc} | {", ".join([f"[{t}]" for t in tags])} |')
                    total_processed += 1

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# 물리 권역 어빌리티 태그 분석 결과\n\n')
        f.write(f'총 분석된 어빌리티: {total_processed}개\n\n')
        f.write('| 어빌리티명 | 설명 | 추출된 태그 |\n')
        f.write('| :--- | :--- | :--- |\n')
        f.write('\n'.join(results))

    print(f'Successfully created {output_path} with {total_processed} items.')

if __name__ == "__main__":
    run_tagging()