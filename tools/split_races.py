import os
import re

# Paths
base_dir = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\word_list"
source_file = os.path.join(base_dir, "character", "종족.md")
target_dir = os.path.join(base_dir, "race")

def process_races():
    if not os.path.exists(source_file):
        print(f"Source file not found: {source_file}")
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Extract header lines (Title + Metadata + Table Header)
    header_lines = []
    content_lines = []
    
    table_header_found = False
    
    for line in lines:
        if line.strip().startswith("| 분류 |"):
            table_header_found = True
            header_lines.append(line)
            continue
        if table_header_found and line.strip().startswith("|:--"):
            header_lines.append(line)
            continue
        
        if table_header_found and line.strip().startswith("|"):
            content_lines.append(line)
        # Skip title and metadata from original file to create fresh ones, 
        # or we could keep them. Let's create fresh headers for each file.

    # Group by category
    # Keyword format: "마법/종족/카테고리/..." or "종족/카테고리/..."
    # The file we viewed shows col 2: "종족/거인", "종족/드래곤/..."
    
    lines_by_category = {}
    
    for line in content_lines:
        parts = line.split("|")
        if len(parts) < 3:
            continue
        
        keyword_col = parts[2].strip() # Index 2 because split creates empty str at start for |
        
        # Parse category: "종족/Something" -> Something
        # If it just "종족", handle gracefully
        
        match = re.search(r"종족/([^/]+)", keyword_col)
        if match:
            category = match.group(1)
        else:
            category = "기타"
            
        if category not in lines_by_category:
            lines_by_category[category] = []
        
        lines_by_category[category].append(line)

    # Write files
    for category, cat_lines in lines_by_category.items():
        filename = f"종족_{category}.md"
        filepath = os.path.join(target_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# 종족 ({category})\n\n")
            f.write(f"> **작성일:** 2026-01-04\n")
            f.write(f"> **수정일:** 2026-01-06 (Split from original)\n\n")
            f.writelines(header_lines)
            f.writelines(cat_lines)
            
        print(f"Created {filename} with {len(cat_lines)} entries.")

if __name__ == "__main__":
    process_races()
