import os

# Paths
base_dir = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\word_list"
char_dir = os.path.join(base_dir, "character")
common_dir = os.path.join(base_dir, "common")
fantasy_dir = os.path.join(base_dir, "fantasy")
martial_arts_dir = os.path.join(base_dir, "martial_arts")

source_file = os.path.join(char_dir, "가상직업.md")
common_file = os.path.join(common_dir, "직업.md")
fantasy_file = os.path.join(fantasy_dir, "직업.md")
martial_arts_file = os.path.join(martial_arts_dir, "직업.md")

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

ensure_dir(common_dir)
ensure_dir(fantasy_dir)
ensure_dir(martial_arts_dir)

# Simple keyword sets for classification
fantasy_keywords = [
    "용사", "용기사", "신성기사", "암흑기사", "마도기사", "마도전사", 
    "백마도사", "흑마도사", "소환사", "연금술사", "마녀", "마도사", "정령사", "환수사", "사령술사", "영매사",
    "음양사", "무녀", "드루이드", "모험가", "트레저헌터", "도적", "레인저", "가디언", "화염술사", "냉기술사", 
    "마법스크롤상인", "요리사(마물)", "팔라딘", "버서커", "점성술사", "예언자", "주술사", "마법공예가", 
    "용조련사", "몽크", "암흑마도사", "신성마도사", "신성사제", "암흑사제", "바바리안", "야만전사", "로그", "바드",
    "소서러", "소서리스", "위자드", "위치", "마왕", "클레릭", "프리스트", "마검사", "궁정마법사", "궁정사제",
    "광명술사", "암흑술사", "바람술사", "대지술사", "마수조련사", "정제사", "정화사", "마적", "괴도", 
    "엘프", "드워프", "오크", "고블린", "마법", "마력", "신성력", "저주", "드래곤", "마수", "정령"
]

martial_arts_keywords = [
    "무투가", "무사", "협객", "낭인", "표사", "녹림", "마교", "무림", "내공", "경공", 
    "사무라이", "닌자", "음양사" # 음양사 can be both, but usually associated with Eastern fantasy
]

def classify_line(line):
    # Check martial arts
    for kw in martial_arts_keywords:
        if kw in line:
            return "martial_arts"
            
    # Check fantasy
    for kw in fantasy_keywords:
        if kw in line:
            return "fantasy"

    return "common" # Default to common

def process_jobs():
    if not os.path.exists(source_file):
        print(f"Source file not found: {source_file}")
        return

    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    common_lines = []
    fantasy_lines = []
    martial_arts_lines = []
    
    table_start_idx = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("| 분류 |"):
            table_start_idx = i
            break
            
    header_lines = lines[table_start_idx:table_start_idx+2]
    content_lines = lines[table_start_idx+2:]
    
    for line in content_lines:
        if not line.strip().startswith("|"):
            continue
            
        category = classify_line(line)
        
        if category == "fantasy":
            fantasy_lines.append(line.replace("| 가상직업 |", "| 판타지/직업 |"))
        elif category == "martial_arts":
            martial_arts_lines.append(line.replace("| 가상직업 |", "| 무협/직업 |"))
        else:
             common_lines.append(line.replace("| 가상직업 |", "| 직업 |"))
        
    # Write Common
    with open(common_file, 'w', encoding='utf-8') as f:
        f.write("# 직업 (Common)\n\n")
        f.write(f"> **작성일:** 2026-01-06\n\n")
        f.writelines(header_lines)
        f.writelines(common_lines)
        
    # Write Fantasy
    with open(fantasy_file, 'w', encoding='utf-8') as f:
        f.write("# 직업 (Fantasy)\n\n")
        f.write(f"> **작성일:** 2026-01-06\n\n")
        f.writelines(header_lines)
        f.writelines(fantasy_lines)

    # Write Martial Arts
    with open(martial_arts_file, 'w', encoding='utf-8') as f:
        f.write("# 직업 (Martial Arts)\n\n")
        f.write(f"> **작성일:** 2026-01-06\n\n")
        f.writelines(header_lines)
        f.writelines(martial_arts_lines)
        
    print(f"Processed Jobs: Common={len(common_lines)}, Fantasy={len(fantasy_lines)}, Martial={len(martial_arts_lines)}")

if __name__ == "__main__":
    process_jobs()
