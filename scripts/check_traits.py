import glob
import os
import sys

# 프로젝트 루트 기준 경로 설정
# 이 스크립트는 scripts 폴더 안에 위치하므로 부모의 data/traits를 참조
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRAITS_DIR = os.path.join(BASE_DIR, "data", "traits")


def check_traits():
    md_files = glob.glob(os.path.join(TRAITS_DIR, "*.md"))
    all_keywords = {}
    errors = []

    print(f"Scanning {len(md_files)} files in {TRAITS_DIR}...")
    print("-" * 50)

    for file_path in md_files:
        filename = os.path.basename(file_path)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            line_stripped = line.strip()

            # 테이블 행이 아니면 스킵
            if not line_stripped.startswith("|"):
                continue

            # 헤더 구분선 스킵 (| :--- | 등)
            if "---" in line_stripped:
                continue

            parts = [p.strip() for p in line_stripped.split("|")]

            # 빈 파트 제외 (| A | B | -> ['', 'A', 'B', ''] -> len 4)
            # 내용은 최소 3개 컬럼(키워드, 분류, 설명)이어야 함
            # parts는 최소 5개여야 함 (양쪽 끝 빈 문자열 포함)
            if len(parts) < 5:
                # 테이블 포맷 경고 (주석 처리 등은 제외)
                # errors.append(f"[FORMAT] {filename}:{i+1} - Broken table format or missing columns")
                continue

            # 키워드 추출 (1번째 인덱스)
            raw_keyword = parts[1]
            keyword = raw_keyword.replace("*", "").strip()

            # 헤더 행 스킵
            if keyword == "키워드" or not keyword:
                continue

            # 중복 검사
            if keyword in all_keywords:
                prev_file, prev_line = all_keywords[keyword]
                errors.append(
                    f"[DUPLICATE] '{keyword}' in {filename}:{i + 1} (Previously in {prev_file}:{prev_line})"
                )
            else:
                all_keywords[keyword] = (filename, i + 1)

    print("-" * 50)
    if errors:
        print(f"FAILED: Found {len(errors)} errors.")
        for err in errors:
            print(err)
        sys.exit(1)
    else:
        print("SUCCESS: No duplicates found.")
        sys.exit(0)


if __name__ == "__main__":
    if not os.path.exists(TRAITS_DIR):
        print(f"Error: Directory not found: {TRAITS_DIR}")
        sys.exit(1)
    check_traits()
