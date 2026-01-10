import os

# Paths
base_dir = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\word_list"
backstory_dir = os.path.join(base_dir, "backstory")
common_dir = os.path.join(base_dir, "common")
fantasy_dir = os.path.join(base_dir, "fantasy")

source_file = os.path.join(backstory_dir, "04_출신지가상_장소.md")
common_file = os.path.join(common_dir, "장소.md")
fantasy_file = os.path.join(fantasy_dir, "장소.md")

# Simple keyword sets for classification
fantasy_keywords = [
    "던전", "마탑", "드래곤", "신전", "마계", "천계", "이계", "유적", "미궁", "결계", 
    "성소", "제단", "마법", "정령", "저주", "포탈", "세계수", "요정", "신들", 
    "고대유적", "수정동굴", "용의", "마나", "심연", "나락", "지옥", "천국", "에덴", 
    "신수", "영묘", "마수", "몬스터", "차원", "영원", "불사", "영생", "천상"
]

def classify_line(line):
    # Check fantasy
    for kw in fantasy_keywords:
        if kw in line:
            return "fantasy"
    return "common" # Default to common

def process_places():
    if not os.path.exists(source_file):
        print(f"Source file not found: {source_file}")
        return

    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    common_lines = []
    fantasy_lines = []
    
    # Identify header end
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
            fantasy_lines.append(line.replace("| 출신지/장소/가상 |", "| 판타지/장소 |"))
        else:
             common_lines.append(line.replace("| 출신지/장소/가상 |", "| 장소 |"))
        
    # Write Common
    with open(common_file, 'w', encoding='utf-8') as f:
        f.write("# 장소 (Common)\n\n")
        f.write(f"> **작성일:** 2026-01-06\n\n")
        f.writelines(header_lines)
        f.writelines(common_lines)
        
    # Write Fantasy
    with open(fantasy_file, 'w', encoding='utf-8') as f:
        f.write("# 장소 (Fantasy)\n\n")
        f.write(f"> **작성일:** 2026-01-06\n\n")
        f.writelines(header_lines)
        f.writelines(fantasy_lines)

    print(f"Processed Places: {len(common_lines)} Common, {len(fantasy_lines)} Fantasy")

if __name__ == "__main__":
    process_places()
