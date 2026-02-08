#!/usr/bin/env python3
"""
중복 검사 스크립트: 리포트에서 추출된 특성/어빌리티를 기존 데이터와 대조

사용법:
    python tools/check_duplicates.py <리포트_파일_경로>

예시:
    python tools/check_duplicates.py report/concept_analyze/character/fate_stay_night_saber.md
"""

import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Set

# 프로젝트 루트 경로
PROJECT_ROOT = Path(__file__).parent.parent
DATA_TRAITS_DIR = PROJECT_ROOT / "data" / "traits"
DATA_ABILITY_DIR = PROJECT_ROOT / "data" / "ability"


def _force_utf8_stdio() -> None:
    """
    Cursor/CI 등에서 stdout을 UTF-8로 기대하는 경우가 많아,
    Windows 기본 코드페이지(cp949 등)로 인한 깨짐/예외를 방지합니다.
    """
    for name in ("stdout", "stderr"):
        stream = getattr(sys, name, None)
        if stream is None:
            continue
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            # Python < 3.7 or non-text streams
            pass


def normalize_name(name: str) -> str:
    """
    중복 비교용 이름 정규화.
    - 영문 표기 등을 위한 괄호 구간 제거: "악몽 구현 (Nightmare Manifestation)" -> "악몽 구현"
    - 공백 정리
    """
    # 일반 괄호/전각 괄호 모두 제거
    name = re.sub(r"\s*\([^)]*\)\s*", " ", name)
    name = re.sub(r"\s*（[^）]*）\s*", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name


def extract_name_from_markdown_table(content: str) -> Set[str]:
    """마크다운 테이블에서 특성/어빌리티 이름 추출"""
    names = set()

    # 마크다운 테이블 형식: | **이름** | 설명 |
    pattern = r"\|\s*\*\*([^*]+)\*\*\s*\|"
    matches = re.findall(pattern, content)

    for match in matches:
        name = normalize_name(match.strip())
        if name:
            names.add(name)

    return names


def load_existing_data() -> Dict[str, Set[str]]:
    """기존 데이터 파일에서 모든 특성/어빌리티 이름 로드"""
    existing = defaultdict(set)

    # Traits 파일들 읽기
    if DATA_TRAITS_DIR.exists():
        for trait_file in DATA_TRAITS_DIR.glob("*.md"):
            content = trait_file.read_text(encoding="utf-8")
            names = extract_name_from_markdown_table(content)
            existing[f"traits/{trait_file.name}"] = names

    # Ability 파일들 읽기 (하위 폴더 포함)
    if DATA_ABILITY_DIR.exists():
        for ability_file in DATA_ABILITY_DIR.rglob("*.md"):
            content = ability_file.read_text(encoding="utf-8")
            names = extract_name_from_markdown_table(content)
            # 상대 경로를 키로 사용 (예: ability/detailed_lists/1.마법권역/마법_방출계_구체.md)
            rel_path = ability_file.relative_to(DATA_ABILITY_DIR.parent)
            existing[str(rel_path).replace("\\", "/")] = names

    return existing


def parse_report(report_path: Path) -> Dict[str, List[Dict[str, Any]]]:
    """리포트 파일에서 특성/어빌리티 추출"""
    content = report_path.read_text(encoding="utf-8")

    extracted: Dict[str, List[Dict[str, Any]]] = {"traits": [], "ability": []}

    # 리포트 형식 파싱
    # 예: **[트레잇] 이름**, **[특성] 이름**, **[발동] 이름**, **[지속] 이름**, **[어빌리티] 이름**
    trait_pattern = r"\*\*\[(?:특성|트레잇)\]\s+([^*]+)\*\*"
    active_pattern = r"\*\*\[(?:발동|어빌리티)\]\s+([^*]+)\*\*"
    passive_pattern = r"\*\*\[지속\]\s+([^*]+)\*\*"

    # 분류 정보도 함께 추출
    # 예: **분류:** `data/traits/10_정신.md`
    # 예: **구조:** [마법:원소] - [제어계] - [영역]
    classification_pattern = r"\*\*분류:\*\*\s*(?:`([^`]+)`|([^\n]+))"
    structure_pattern = (
        r"\*\*구조:\*\*\s*\[([^\]]+)\]\s*-\s*\[([^\]]+)\]\s*-\s*\[([^\]]+)\]"
    )

    # 각 항목 블록 찾기
    blocks = re.split(
        r"\n\s*\d+\.\s+", content
    )  # 번호 매겨진 리스트 항목(1. 2. 등)으로 분할

    for block in blocks:
        # 중복 표기 확인
        is_already_exists = "(이미 존재)" in block

        # 특성/트레잇 추출
        trait_match = re.search(trait_pattern, block)
        if trait_match:
            full_name = trait_match.group(1).strip()
            name = normalize_name(full_name)
            class_match = re.search(classification_pattern, block)
            classification = ""
            if class_match:
                classification = (class_match.group(1) or class_match.group(2)).strip()
                # '02_기원' 처럼 파일명만 온 경우 경로 보정
                if not classification.startswith(
                    "data/"
                ) and not classification.startswith("traits/"):
                    classification = f"traits/{classification}"
                if not classification.endswith(".md"):
                    classification += ".md"

            extracted["traits"].append(
                {
                    "name": name,
                    "classification": classification,
                    "is_already_exists": is_already_exists,
                    "block": block[:200],
                }
            )

        # 발동/어빌리티 추출 (이제 일반 어빌리티로 취급)
        active_match = re.search(active_pattern, block)
        if active_match:
            full_name = active_match.group(1).strip()
            name = normalize_name(full_name)

            # 구조 정보 추출 시도
            struct_match = re.search(structure_pattern, block)
            classification = ""
            if struct_match:
                domain_raw, lineage, form = struct_match.groups()
                # '정신:소리' 에서 '정신'만 추출
                domain = domain_raw.split(":")[0].strip()

                # 권역 번호 매칭 시도 (기존 어빌리티 폴더 구조 활용)
                domain_map = {
                    "마법": "1.마법권역",
                    "물리": "2.물리권역",
                    "정신": "3.정신권역",
                    "특수": "4.특수권역",
                    "전술": "5.전술권역",
                    "생산": "6.생산권역",
                }
                domain_folder = domain_map.get(domain, "unknown")
                if domain_folder != "unknown":
                    classification = f"ability/detailed_lists/{domain_folder}/{domain}_{lineage}_{form}.md"

            # 분류 정보가 직접 명시된 경우 우선함
            class_match = re.search(classification_pattern, block)
            if class_match:
                classification = (class_match.group(1) or class_match.group(2)).strip()

            extracted["ability"].append(
                {
                    "name": name,
                    "classification": classification,
                    "is_already_exists": is_already_exists,
                    "block": block[:200],
                }
            )

        # 지속 어빌리티 추출 (이제 트레잇으로 취급)
        passive_match = re.search(passive_pattern, block)
        if passive_match:
            full_name = passive_match.group(1).strip()
            name = normalize_name(full_name)
            class_match = re.search(classification_pattern, block)
            classification = ""
            if class_match:
                classification = (class_match.group(1) or class_match.group(2)).strip()
                if not classification.startswith(
                    "data/"
                ) and not classification.startswith("traits/"):
                    classification = f"traits/{classification}"
                if not classification.endswith(".md"):
                    classification += ".md"

            extracted["traits"].append(
                {
                    "name": name,
                    "classification": classification,
                    "is_already_exists": is_already_exists,
                    "block": block[:200],
                }
            )

    return extracted


def check_duplicates(
    extracted: Dict[str, List[Dict[str, Any]]], existing: Dict[str, Set[str]]
) -> Dict[str, List[Dict[str, Any]]]:
    """중복 검사 수행"""
    results: Dict[str, List[Dict[str, Any]]] = {
        "duplicates": [],
        "new_items": [],
        "similar_names": [],
    }

    # 추출된 항목들을 분류별로 확인
    for category, items in extracted.items():
        for item in items:
            name = item["name"]
            classification = item["classification"]
            is_already_exists = item.get("is_already_exists", False)

            # 분류에서 파일명 추출
            target_file = classification.replace("data/", "").replace("`", "").strip()

            # 리포트 자체에 '이미 존재' 표기가 있으면 중복으로 처리
            if is_already_exists:
                results["duplicates"].append(
                    {
                        "name": name,
                        "category": category,
                        "file": target_file,
                        "note": "리포트에서 '이미 존재'로 표시됨",
                    }
                )
                continue

            # 해당 파일에서 중복 확인
            if target_file in existing:
                if name in existing[target_file]:
                    results["duplicates"].append(
                        {
                            "name": name,
                            "category": category,
                            "file": target_file,
                            "classification": classification,
                        }
                    )
                else:
                    # 다른 파일에서 중복 확인
                    found_in_other = []
                    for file_path, names in existing.items():
                        if file_path != target_file and name in names:
                            found_in_other.append(file_path)

                    if found_in_other:
                        results["duplicates"].append(
                            {
                                "name": name,
                                "category": category,
                                "file": target_file,
                                "found_in": found_in_other,
                                "classification": classification,
                            }
                        )
                    else:
                        results["new_items"].append(
                            {
                                "name": name,
                                "category": category,
                                "file": target_file,
                                "classification": classification,
                            }
                        )
            else:
                # 분류 파일이 없거나 경로가 불완전하면 새 항목으로 처리하되 경고 표시
                results["new_items"].append(
                    {
                        "name": name,
                        "category": category,
                        "file": target_file,
                        "classification": classification,
                        "note": "분류 파일이 존재하지 않거나 경로가 불명확함"
                        if not target_file.endswith(".md")
                        else "신규 파일 대상",
                    }
                )

    return results


def print_results(results: Dict, report_path: Path):
    """결과 출력"""
    print(f"\n{'=' * 60}")
    print(f"중복 검사 결과: {report_path.name}")
    print(f"{'=' * 60}\n")

    # 중복 항목
    if results["duplicates"]:
        print(f"[WARN] 중복 발견: {len(results['duplicates'])}개\n")
        for dup in results["duplicates"]:
            print(f"  - {dup['name']} ({dup['category']})")
            if "found_in" in dup:
                print(f"    -> 예상 위치: {dup['file']}")
                print(f"    -> 실제 위치: {', '.join(dup['found_in'])}")
            else:
                print(f"    -> 위치: {dup['file']}")
        print()
    else:
        print("[OK] 중복 없음\n")

    # 새 항목
    if results["new_items"]:
        print(f"[신규] 새 항목: {len(results['new_items'])}개\n")
        for item in results["new_items"]:
            print(f"  - {item['name']} ({item['category']})")
            print(f"    -> 추가 위치: {item['file']}")
            if "note" in item:
                print(f"    [주의] {item['note']}")
        print()

    # 요약
    print(f"{'=' * 60}")
    print("요약:")
    print(f"  중복: {len(results['duplicates'])}개")
    print(f"  신규: {len(results['new_items'])}개")
    print(f"{'=' * 60}\n")


def main():
    _force_utf8_stdio()
    if len(sys.argv) < 2:
        print("사용법: python tools/check_duplicates.py <리포트_파일_경로>")
        sys.exit(1)

    report_path = Path(sys.argv[1])
    if not report_path.exists():
        print(f"[ERR] 파일을 찾을 수 없습니다: {report_path}")
        sys.exit(1)

    # 기존 데이터 로드
    print("기존 데이터 로드 중...")
    existing = load_existing_data()
    print(
        f"  - Traits 파일: {len([f for f in existing.keys() if f.startswith('traits/')])}개"
    )
    print(
        f"  - 어빌리티 파일: {len([f for f in existing.keys() if f.startswith('ability/')])}개"
    )

    # 리포트 파싱
    print(f"\n리포트 파싱 중: {report_path.name}")
    extracted = parse_report(report_path)
    print(f"  - 트레잇 (지속 포함): {len(extracted['traits'])}개")
    print(f"  - 어빌리티 (발동): {len(extracted['ability'])}개")

    # 중복 검사
    print("\n중복 검사 수행 중...")
    results = check_duplicates(extracted, existing)

    # 결과 출력
    print_results(results, report_path)

    # 중복이 있으면 종료 코드 1 반환
    if results["duplicates"]:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
