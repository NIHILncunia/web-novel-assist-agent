import os
import sys

def extract_descriptions(directory):
    results = {}
    if not os.path.exists(directory):
        return results
    for filename in os.listdir(directory):
        if not filename.endswith(".md"): continue
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        lines = content.splitlines()
        table_started, headers, file_data = False, [], []
        for line in lines:
            line = line.strip()
            if not line.startswith('|'): continue
            if '---' in line:
                table_started = True
                continue
            if not table_started and not headers:
                headers = [h.strip() for h in line.strip('|').split('|')]
                continue
            if table_started:
                cols = [c.strip() for c in line.strip('|').split('|')]
                if len(cols) < 2: continue
                name_idx, desc_idx = 0, -1
                if headers:
                    for i, h in enumerate(headers):
                        if '이름' in h: name_idx = i
                        if '설명' in h: desc_idx = i
                name = cols[name_idx].replace('**', '')
                desc = cols[desc_idx]
                if name and desc:
                    file_data.append({'name': name, 'desc': desc})
        if file_data: results[filename] = file_data
    return results

def generate_report(data, output_file, title):
    with open(output_file, 'w', encoding='utf-8') as f:
        header = f"# {title}\n\n"
        header += f"> **생성일:** 2026-02-04\n"
        header += f"> **대상 파일 수:** {len(data)}개\n\n"
        f.write(header)
        for filename, abilities in sorted(data.items()):
            f.write(f"## 📂 {filename}\n")
            f.write("| 어빌리티명 | 설명 |\n")
            f.write("| :--- | :--- |\n")
            for ab in abilities:
                f.write(f"| {ab['name']} | {ab['desc']} |\n")
            f.write("\n")

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        data = extract_descriptions(sys.argv[1])
        generate_report(data, sys.argv[2], sys.argv[3])