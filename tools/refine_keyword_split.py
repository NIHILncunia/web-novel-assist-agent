import os

# Paths
base_dir = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\word_list"
common_file = os.path.join(base_dir, "common", "직업.md")
fantasy_file = os.path.join(base_dir, "fantasy", "직업.md")

# Strict Common (Modern/Timeless Realism)
# We will iterate through Common file and move items NOT in this list (or matching heuristic) to Fantasy.
# Actually, it's safer to define what to MOVE to Fantasy (Historical/Archaic/RPG Classes).

move_to_fantasy_keywords = [
    "투사", "무투가", "아마조네스", "암살자", "음유시인", "국왕", "공주", "그림자투사", "군사", 
    "근위병", "기병", "궁병", "신관", "수도승", "귀족", "산적", "모험가", "트레저헌터", 
    "한량", "레인저", "사무라이", "유랑예능인", "도구상인", "대장장이", "길드마스터", "점술가", 
    "궁수", "파이터", "검술사", "창술사", "도끼술사", "둔기술사", "폴암술사", "궁술사", "석궁술사", 
    "로그", "군단장", "기사", "황제", "왕", "여제", "여왕", "마부", "약초사", "처형인", "수적", "마적",
    "공적" # Public Enemy usually implies wanted posters in fantasy
]

# Note: "총병"(Gunner), "포병"(Artillery), "보병"(Infantry) are modern military terms too. 
# But "총병" usually means Musketeer in these lists. Let's ask user? 
# User said "Common = Modern". Gunner/Artillery exist. Keep them in Common?
# "장군"(General) - Keep.
# "주교", "사제", "수녀", "승려" - Religious. Keep in Common.
# "집사", "메이드" - Modern rich people / hotels. Keep.
# "정원사" - Keep.
# "해적" - Modern pirates exist. Keep.
# "도적" (Thief), "도둑" (Burglar) - Keep.
# "도박사", "무희", "놀이꾼", "용병" - Keep.
# "숙박업주", "술집주인", "정보수집가", "기계공학자", "학자", "건축기술자", "사냥꾼", "행상인", "현상금사냥꾼", "정보상인", "상인", "무기상인", "광대", "조련사" - Keep.

# Special case handling:
# "의사" should be in Common.

def process_reclassification():
    if not os.path.exists(common_file):
        print("Common file not found.")
        return

    with open(common_file, 'r', encoding='utf-8') as f:
        common_lines_in = f.readlines()
        
    with open(fantasy_file, 'r', encoding='utf-8') as f:
        fantasy_lines_in = f.readlines()

    # Extract headers
    header_lines = []
    content_lines = []
    
    table_start = False
    for line in common_lines_in:
        if line.strip().startswith("| 분류 |"):
            table_start = True
            header_lines.append(line)
            continue
        if table_start and line.strip().startswith("|:--"):
            header_lines.append(line)
            continue
        if table_start and line.strip().startswith("|"):
            content_lines.append(line)
        elif not table_start and line.startswith("#"):
             pass # Skip original header
             
    # Prepare Fantasy existing content (skip header)
    fantasy_content = []
    f_table_start = False
    for line in fantasy_lines_in:
         # We assume header is same, just grab content
        if line.strip().startswith("| 분류 |"):
            f_table_start = True
            continue
        if f_table_start and line.strip().startswith("|:--"):
            continue
        if f_table_start and line.strip().startswith("|"):
            fantasy_content.append(line)

    new_common_content = []
    new_fantasy_content = []
    
    for line in content_lines:
        move = False
        for kw in move_to_fantasy_keywords:
            # Check if keyword is in the 2nd column
            # | 직업 | 키워드 | ...
            parts = line.split("|")
            if len(parts) > 2:
                keyword = parts[2].strip()
                if keyword == kw:
                    move = True
                    break
        
        if move:
            # Change category name to '판타지/직업' just in case, though user didn't specify format strictly, strict separation suggests it.
            # But the existing Fantasy file uses "| 판타지/직업 |".
            # The Common file uses "| 직업 |".
            new_line = line.replace("| 직업 |", "| 판타지/직업 |")
            new_fantasy_content.append(new_line)
        else:
            new_common_content.append(line)

    # Re-write Common
    with open(common_file, 'w', encoding='utf-8') as f:
        f.write("# 직업 (Common)\n\n")
        f.write(f"> **작성일:** 2026-01-06\n")
        f.write(f"> **수정일:** 2026-01-06\n\n")
        f.writelines(header_lines)
        f.writelines(new_common_content)
        
    # Re-write Fantasy
    # Check header of fantasy file to preserve it if needed or just overwrite distinctively
    fantasy_header_lines = []
    with open(fantasy_file, 'r', encoding='utf-8') as f:
         # Just grab top lines until table
         f.seek(0)
         for line in f:
             if line.strip().startswith("|"):
                 break
             fantasy_header_lines.append(line)
    
    with open(fantasy_file, 'w', encoding='utf-8') as f:
        f.write("# 직업 (Fantasy)\n\n")
        f.write(f"> **작성일:** 2026-01-06\n")
        f.write(f"> **수정일:** 2026-01-06\n\n")
        f.writelines(header_lines) # Use same table header
        f.writelines(fantasy_content)
        f.writelines(new_fantasy_content)

    print(f"Reclassified: Moved {len(new_fantasy_content)} items from Common to Fantasy.")
    print(f"Common now has {len(new_common_content)} items.")
    print(f"Fantasy now has {len(fantasy_content) + len(new_fantasy_content)} items.")

if __name__ == "__main__":
    process_reclassification()
