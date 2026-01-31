import csv
import os

csv_dir = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\csv"
output_file = os.path.join(csv_dir, "missing_mcls_records.csv")
encoding = "utf-8"


def extract_missing_mcls():
    files = [
        f
        for f in os.listdir(csv_dir)
        if f.endswith(".csv") and f != "missing_mcls_records.csv"
    ]
    files.sort()

    missing_records = []
    fieldnames = [
        "source_file",
        "line_no",
        "trait_no",
        "trait_nm",
        "trait_expln",
        "trait_lcls",
        "trait_mcls",
        "aply_trgt",
        "cnfl_trait_no",
    ]

    print(f"Scanning {len(files)} files...")

    for filename in files:
        filepath = os.path.join(csv_dir, filename)

        try:
            with open(filepath, "r", encoding=encoding) as f:
                reader = csv.DictReader(f)

                if "trait_mcls" not in reader.fieldnames:
                    print(f"Skipping {filename}: 'trait_mcls' column missing")
                    continue

                for row_num, row in enumerate(reader, start=2):
                    mcls = row.get("trait_mcls", "").strip()
                    if not mcls:
                        # Add source metadata
                        record = {
                            "source_file": filename,
                            "line_no": row_num,
                            **{
                                k: row.get(k, "")
                                for k in fieldnames
                                if k not in ["source_file", "line_no"]
                            },
                        }
                        missing_records.append(record)

        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue

    if missing_records:
        with open(output_file, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(missing_records)

        print(f"\nSuccessfully extracted {len(missing_records)} records to:")
        print(f"{output_file}")
    else:
        print("\nNo missing trait_mcls records found.")


if __name__ == "__main__":
    extract_missing_mcls()
