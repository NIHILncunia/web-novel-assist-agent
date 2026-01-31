import csv
import os

csv_dir = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\csv"
output_file = r"c:\Users\nihil\coding\novel\novel-assist-agent\missing_mcls_report.txt"
encoding = "utf-8"


def check_missing_mcls():
    files = [f for f in os.listdir(csv_dir) if f.endswith(".csv")]
    files.sort()

    missing_count = 0
    results = []

    for filename in files:
        filepath = os.path.join(csv_dir, filename)
        file_missing = []

        try:
            with open(filepath, "r", encoding=encoding) as f:
                reader = csv.DictReader(f)

                if "trait_mcls" not in reader.fieldnames:
                    results.append(f"[{filename}] 'trait_mcls' column missing!")
                    continue

                for row_num, row in enumerate(reader, start=2):
                    mcls = row.get("trait_mcls", "").strip()
                    nm = row.get("trait_nm", "").strip()
                    if not mcls:
                        file_missing.append((row_num, nm))

        except Exception as e:
            results.append(f"Error reading {filename}: {e}")
            continue

        if file_missing:
            results.append(f"\n[{filename}]")
            for line_no, nm in file_missing:
                results.append(f"  - Line {line_no}: {nm}")
                missing_count += 1

    with open(output_file, "w", encoding="utf-8") as f:
        if missing_count == 0:
            f.write("No missing trait_mcls found in any files.\n")
            print("No missing records found.")
        else:
            f.write(f"Total missing trait_mcls records: {missing_count}\n")
            for line in results:
                f.write(line + "\n")
            print(f"Report generated: {output_file} (Total missing: {missing_count})")


if __name__ == "__main__":
    check_missing_mcls()
