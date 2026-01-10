import json
import os

# Paths
base_dir = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\word_list"
json_path = r"c:\Users\nihil\coding\novel\novel-assist-agent\other.json"
common_dir = os.path.join(base_dir, "common")
fantasy_dir = os.path.join(base_dir, "fantasy")

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

ensure_dir(common_dir)
ensure_dir(fantasy_dir)

def write_md_table(filename, category_name, items):
    filepath = os.path.join(common_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {category_name}\n\n")
        f.write(f"> **작성일:** 2026-01-06\n")
        f.write(f"> **수정일:** 2026-01-06\n\n")
        f.write("| 분류 | 키워드 | 설명 | 예문 |\n")
        f.write("|:---:|:---:|---|---|\n")
        
        for item in items:
            # item looks like "날씨/강수/비"
            parts = item.split("/")
            if len(parts) >= 2:
                # category = "날씨/강수", keyword = "비"
                # But sometimes it might be deeper. Let's take the last part as keyword.
                keyword = parts[-1]
                # classification = "/".join(parts[:-1]) 
                # Let's clean up classification. 
                # If it starts with "날씨/", maybe remove it or keep it?
                # Existing format: "출신지/장소/가상"
                classification = "/".join(parts[:-1])
                f.write(f"| {classification} | {keyword} | | |\n")

def process_other_json():
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Process '날씨'
    if '날씨' in data:
        print(f"Processing Weather: {len(data['날씨'])} items")
        write_md_table("날씨.md", "날씨 (Common)", data['날씨'])
    
    # Process '도구'
    if '도구' in data:
        print(f"Processing Tools: {len(data['도구'])} items")
        # Most tools are common. 
        # We could try to filter fantasy tools if any, but looking at the list from `view_file` earlier,
        # they seem to be "사무용품", "공구", "식기" etc. mostly modern/common.
        # So we write all to common for now.
        write_md_table("도구.md", "도구 (Common)", data['도구'])

if __name__ == "__main__":
    process_other_json()
