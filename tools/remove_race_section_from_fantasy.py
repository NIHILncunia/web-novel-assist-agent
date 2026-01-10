import os

def remove_race_section():
    file_path = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\word_list\fantasy.md"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    skip = False
    race_section_found = False
    
    for line in lines:
        # Start of Race Section
        if line.strip().startswith("## 1. 종족 (Race)"):
            skip = True
            race_section_found = True
            continue
        
        # End of Race Section (Start of next section)
        if skip and line.strip().startswith("## 2. 직업"):
            skip = False
            # We keep this line (the next section header)
            
        if not skip:
            new_lines.append(line)
            
    if not race_section_found:
        print("Race section not found or already removed.")
        return

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Successfully processed {file_path}")

if __name__ == "__main__":
    remove_race_section()
