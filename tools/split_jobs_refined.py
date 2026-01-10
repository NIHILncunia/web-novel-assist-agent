import os
import shutil

# Paths
base_dir = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\word_list"
char_dir = os.path.join(base_dir, "_archive") # Read from archive since we moved it? Or just read from the original source path if I moved it back? 
# Wait, I moved the source files to _archive. I should read from _archive.
source_file = os.path.join(base_dir, "_archive", "가상직업.md")

common_file = os.path.join(base_dir, "common", "직업.md")
fantasy_file = os.path.join(base_dir, "fantasy", "직업.md")

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

ensure_dir(os.path.dirname(common_file))
ensure_dir(os.path.dirname(fantasy_file))

# Keywords for Fantasy (Explicit Magic/Supernatural)
fantasy_keywords = [
    "용사", "용기사", "신성기사", "암흑기사", "마도기사", "마도전사", 
    "백마도사", "흑마도사", "소환사", "연금술사", "마녀", "마도사", "정령사", "환수사", "사령술사", "영매사",
    "음양사", "무녀", "드루이드", "화염술사", "냉기술사", 
    "마법스크롤상인", "요리사(마물)", "팔라딘", "버서커", "점성술사", "예언자", "주술사", "마법공예가", 
    "용조련사", "암흑마도사", "신성마도사", "신성사제", "암흑사제", "바바리안", "야만전사", "바드",
    "소서러", "소서리스", "위자드", "위치", "마왕", "클레릭", "프리스트", "마검사", "궁정마법사", "궁정사제",
    "광명술사", "암흑술사", "바람술사", "대지술사", "마수조련사", "정제사", "정화사", "마적", "괴도", 
    "엘프", "드워프", "오크", "고블린", "마법", "마력", "신성력", "저주", "드래곤", "마수", "정령",
    "닌자", "음양사" # Ninja often implies magic in games/novels
]

# Everything else -> Common
# (Includes: Gunner, Artillery, Engineer, Rogue, Martial Artist, Samurai, King, Queen, etc.)

def classify_line(line):
    # Check fantasy
    for kw in fantasy_keywords:
        if kw in line:
            return "fantasy"
    return "common"

def process_jobs():
    if not os.path.exists(source_file):
        print(f"Source file not found: {source_file}")
        return

    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    common_lines = []
    fantasy_lines = []
    
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
            fantasy_lines.append(line.replace("| 가상직업 |", "| 판타지/직업 |").replace("| 무협/직업 |", "| 판타지/직업 |"))
        else:
             common_lines.append(line.replace("| 가상직업 |", "| 직업 |").replace("| 무협/직업 |", "| 직업 |"))
        
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

    print(f"Processed Jobs: Common={len(common_lines)}, Fantasy={len(fantasy_lines)}")
    
    # Remove old dirs if exist
    ma_dir = os.path.join(base_dir, "martial_arts")
    
    # We should clean up the files we created there.
    # Note: shutil.rmtree might be dangerous if not careful, but path is specific.
    # We'll just print a message to delete them with a command for safety.

if __name__ == "__main__":
    process_jobs()
