import os

# Refined list
refined_weapons = sorted(list(set([
    "장검", "대검", "직검", "곡검", "대곡검", "세검", "레이피어", "단검", "대거", "비수", "쌍검", 
    "도", "쌍도", "환도", "환두대도", "일본도", "카타나", "협도", 
    "창", "단창", "장창", "삼지창", "투창", "할버드", "랜스", 
    "봉", "곤", "지팡이", "스태프", "완드", 
    "망치", "해머", "워해머", "철퇴", "메이스", "모닝스타", "곤봉", 
    "너클", "건틀릿", "클로", "갈퀴", 
    "도끼", "양날도끼", "전투도끼", "토마호크", 
    "활", "대궁", "석궁", "쇠뇌", "슬링", "투석구", 
    "표창", "수리검", "부메랑", 
    "권총", "리볼버", "소총", "저격총", "산탄총", "기관총", "기관단총", 
    "포", "박격포", "미사일", "로켓포", 
    "수류탄", "지뢰", "폭탄", "C4", "화염병", 
    "레이저건", "레일건", "가우스건", "플라즈마건", 
    "광선검", "단분자커터", "전기톱", 
    "채찍", "낫", "사슬낫", "올가미", 
    "방패", "보호막"
])))

file_path = 'report/ability_tag_protocol.md'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
weapon_set = set(refined_weapons)

for line in lines:
    if line.startswith('## 1. 무기류 [Weapon]'):
        new_lines.append(line)
        new_lines.append("- **" + ", ".join(refined_weapons) + "**
")
        skip = True
    elif skip and line.startswith('- **'):
        continue
    elif skip and not line.strip():
        new_lines.append(line)
        skip = False
    elif line.startswith('### [') and not skip:
        new_lines.append(line)
    elif line.startswith('- **') and not skip:
        # Clean General Tags
        tags = line.strip()[4:-2].split(", ")
        filtered = [t for t in tags if t not in weapon_set]
        if filtered:
            new_lines.append("- **" + ", ".join(filtered) + "**
")
    else:
        new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print("Done")
