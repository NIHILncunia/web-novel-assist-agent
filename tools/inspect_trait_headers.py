import os

TRAIT_DIR = "data/traits"


def get_table_header(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header_line = None
    for line in lines:
        if line.strip().startswith("|") and "---" not in line:
            header_line = line.strip()
            break
    return header_line


def inspect_files():
    files = sorted([f for f in os.listdir(TRAIT_DIR) if f.endswith(".md")])
    print(f"{'Filename':<20} | {'Header'}")
    print("-" * 80)
    for f in files:
        header = get_table_header(os.path.join(TRAIT_DIR, f))
        print(f"{f:<20} | {header}")


if __name__ == "__main__":
    inspect_files()
