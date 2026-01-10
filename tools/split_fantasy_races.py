import os
import re

def split_fantasy_races():
    source_file = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\word_list\fantasy.md"
    target_dir = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\word_list\race"
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find sections. 
    # Sections start with ### and contain specific titles.
    # We'll look for sections starting with "1-" as they seem to be the race sections.
    # Pattern: ### 1-X. [Title]
    
    # Let's define the sections we want to capture based on the file inspection
    # 1-1 to 1-10
    
    # We can split the file by "### "
    parts = re.split(r'^### ', content, flags=re.MULTILINE)
    
    created_files = []

    for part in parts:
        lines = part.strip().split('\n')
        if not lines:
            continue
            
        header = lines[0].strip()
        
        # Check if it is a race section (starts with 1-)
        if not header.startswith("1-"):
            continue
            
        # Extract title for filename
        # Example header: "1-1. 인간형 종족 (통합 리스트)"
        # We want: "종족_인간형.md"
        
        # Remove numbering "1-X. "
        title_part = re.sub(r'^\d+-\d+\.\s*', '', header)
        
        # Remove parenthetical info if deemed extra, but "인공생명/특수종" matches might have parens.
        # Let's simplify: take the main name before any parenthesis or slash if complex, 
        # but user asked for "종족_인간형", "종족_거인형" etc.
        # Let's map explicitly if possible, or use a heuristic.
        
        filename_core = ""
        
        if "인간형" in header: filename_core = "인간형"
        elif "거인형" in header: filename_core = "거인형"
        elif "수인형" in header: filename_core = "수인형"
        elif "용인형" in header: filename_core = "용인형"
        elif "마족" in header or "악마형" in header: filename_core = "마족_악마형"
        elif "언데드" in header: filename_core = "언데드형"
        elif "정령형" in header: filename_core = "정령형"
        elif "신족" in header or "천사형" in header: filename_core = "신족_천사형"
        elif "기타 환상종" in header or "기타 환상종" in header: filename_core = "기타환상종" # whitespace sensitivity
        elif "인공생명" in header or "특수종" in header: filename_core = "인공생명_특수종"
        else:
            # Fallback cleanup
            filename_core = title_part.split('(')[0].strip().replace('/', '_').replace(' ', '')

        filename = f"종족_{filename_core}.md"
        filepath = os.path.join(target_dir, filename)
        
        # Reconstruct content: Header + Body (Table)
        # We might want to remove the "1-X." from the header in the new file, or just keep the table.
        # User usually wants the table. Let's include a title.
        
        file_content = f"# {filename_core}\n\n"
        # Find the table part. usually starts after the header lines.
        # The content already includes everything after the header line found by split.
        
        # Re-join lines except the first (header)
        body = '\n'.join(lines[1:]).strip()
        
        file_content += body
        
        with open(filepath, 'w', encoding='utf-8') as f_out:
            f_out.write(file_content)
            
        created_files.append(filename)
        print(f"Created: {filename}")

if __name__ == "__main__":
    split_fantasy_races()
