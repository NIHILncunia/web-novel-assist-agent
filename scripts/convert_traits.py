import glob
import os
import re

import pandas as pd

# Configuration
INPUT_DIR = "data/traits"
OUTPUT_DIR = "data/csv"

# Column Mapping
# Target Column: [Possible Source Columns in Markdown]
COLUMN_MAPPING_RULES = {
    "trait_nm": ["트레잇 이름", "키워드", "이름", "Trait Name", "트레잇명"],
    "trait_mcls": ["분류", "Category", "하위 분류"],
    "trait_expln": ["트레잇 설명", "설명", "Description", "효과/설명"],
}

# Final DataFrame Columns
FINAL_COLUMNS = [
    "trait_no",  # 1) 특성 번호 (PK) - Optional[int]
    "trait_nm",  # 2) 특성 명 - str
    "trait_expln",  # 3) 특성 설명 (TEXT) - Optional[str]
    "trait_lcls",  # 4) 특성 대분류 - str
    "trait_mcls",  # 5) 특성 중분류 - str
    "aply_trgt",  # 6) 적용 대상 - str
    "cnfl_trait_no",  # 7) 상충 특성 번호 (FK) - Optional[int]
]


def extract_lcls_from_filename(filename):
    # Removes numbered prefix (e.g., "00_", "01_") and extension
    basename = os.path.splitext(os.path.basename(filename))[0]
    # Remove leading digits and underscore if present
    match = re.match(r"^\d+_(.+)$", basename)
    if match:
        return match.group(1)
    return basename


def parse_markdown_table(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the table. Assuming standard Markdown table format.
    # Look for the header line which must contain at least "분류" or "설명" or "이름"
    lines = content.split("\n")
    table_lines = []
    in_table = False

    header_pattern = re.compile(r"\|.*\|.*\|")
    separator_pattern = re.compile(r"\|[-\s:]+\|[-\s:]+\|")

    headers = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if header_pattern.match(line) and not separator_pattern.match(line):
            # Potential header
            # Check if it contains keywords we expect
            temp_headers = [h.strip() for h in line.strip("|").split("|")]
            if any(
                k in temp_headers
                for k in ["트레잇 이름", "키워드", "이름", "분류", "설명"]
            ):
                headers = temp_headers
                in_table = True
                continue

        if in_table:
            if separator_pattern.match(line):
                continue
            if header_pattern.match(line):
                # Data row
                row_values = [v.strip() for v in line.strip("|").split("|")]
                # Handle cases where row might have different number of columns (though unlikely in strict markdown)
                # Pad or truncate to match headers
                if len(row_values) < len(headers):
                    row_values += [""] * (len(headers) - len(row_values))
                elif len(row_values) > len(headers):
                    row_values = row_values[: len(headers)]

                row_dict = dict(zip(headers, row_values))
                table_lines.append(row_dict)
            else:
                # End of table or malformed line
                pass

    return table_lines


def normalize_row(row_dict, lcls):
    new_row = {
        "trait_no": None,
        "trait_nm": "",
        "trait_expln": "",
        "trait_lcls": lcls,
        "trait_mcls": "",
        "aply_trgt": "",
        "cnfl_trait_no": None,
    }

    # Map 'trait_nm'
    for source in COLUMN_MAPPING_RULES["trait_nm"]:
        if source in row_dict:
            # Clean up bold markdown (**text**)
            text = row_dict[source]
            text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
            new_row["trait_nm"] = text
            break

    # Map 'trait_mcls'
    for source in COLUMN_MAPPING_RULES["trait_mcls"]:
        if source in row_dict:
            new_row["trait_mcls"] = row_dict[source]
            break

    # Map 'trait_expln'
    for source in COLUMN_MAPPING_RULES["trait_expln"]:
        if source in row_dict:
            new_row["trait_expln"] = row_dict[source]
            break

    return new_row


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    files = glob.glob(os.path.join(INPUT_DIR, "*.md"))
    print(f"Found {len(files)} markdown files in {INPUT_DIR}")

    for file_path in files:
        filename = os.path.basename(file_path)
        lcls = extract_lcls_from_filename(filename)
        print(f"Processing {filename} -> Category: {lcls}")

        raw_rows = parse_markdown_table(file_path)
        if not raw_rows:
            print(f"  No table found or empty in {filename}")
            continue

        normalized_data = [normalize_row(row, lcls) for row in raw_rows]

        df = pd.DataFrame(normalized_data, columns=FINAL_COLUMNS)

        # Save to CSV
        output_filename = os.path.splitext(filename)[0] + ".csv"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        df.to_csv(
            output_path, index=False, encoding="utf-8-sig"
        )  # utf-8-sig for Excel compatibility if needed
        print(f"  Saved {len(df)} rows to {output_path}")


if __name__ == "__main__":
    main()
