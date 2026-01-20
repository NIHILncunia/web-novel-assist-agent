#!/usr/bin/env python3
"""
중복 검사 스크립트: 리포트에서 추출된 특성/능력을 기존 데이터와 대조

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
DATA_SKILL_DIR = PROJECT_ROOT / "data" / "skill"


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
    """마크다운 테이블에서 특성/능력 이름 추출"""
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
    """기존 데이터 파일에서 모든 특성/능력 이름 로드"""
    existing = defaultdict(set)

    # Traits 파일들 읽기
    if DATA_TRAITS_DIR.exists():
        for trait_file in DATA_TRAITS_DIR.glob("*.md"):
            content = trait_file.read_text(encoding="utf-8")
            names = extract_name_from_markdown_table(content)
            existing[f"traits/{trait_file.name}"] = names

    # Skill 파일들 읽기
    if DATA_SKILL_DIR.exists():
        for skill_file in DATA_SKILL_DIR.glob("*.md"):
            content = skill_file.read_text(encoding="utf-8")
            names = extract_name_from_markdown_table(content)
            existing[f"skill/{skill_file.name}"] = names

    return existing


def parse_report(report_path: Path) -> Dict[str, List[Dict[str, Any]]]:
    """리포트 파일에서 특성/능력 추출"""
    content = report_path.read_text(encoding="utf-8")

    extracted: Dict[str, List[Dict[str, Any]]] = {"traits": [], "발동": [], "지속": []}

    # 리포트 형식 파싱
    # 예: **[특성] 이름** 또는 **[발동] 이름** 또는 **[지속] 이름**
    trait_pattern = r"\*\*\[특성\]\s+([^*]+)\*\*"
    active_pattern = r"\*\*\[발동\]\s+([^*]+)\*\*"
    passive_pattern = r"\*\*\[지속\]\s+([^*]+)\*\*"

    # 분류 정보도 함께 추출
    # 예: **분류:** `data/traits/10_정신.md`
    classification_pattern = r"\*\*분류:\*\*\s*`([^`]+)`"

    # 각 항목 블록 찾기
    blocks = re.split(r"\n\n+", content)

    for block in blocks:
        # 특성 추출
        trait_match = re.search(trait_pattern, block)
        if trait_match:
            name = normalize_name(trait_match.group(1).strip())
            class_match = re.search(classification_pattern, block)
            classification = class_match.group(1) if class_match else "unknown"
            extracted["traits"].append(
                {
                    "name": name,
                    "classification": classification,
                    "block": block[:200],  # 컨텍스트 일부
                }
            )

        # 발동 능력 추출
        active_match = re.search(active_pattern, block)
        if active_match:
            name = normalize_name(active_match.group(1).strip())
            class_match = re.search(classification_pattern, block)
            classification = class_match.group(1) if class_match else "unknown"
            extracted["발동"].append(
                {"name": name, "classification": classification, "block": block[:200]}
            )

        # 지속 능력 추출
        passive_match = re.search(passive_pattern, block)
        if passive_match:
            name = normalize_name(passive_match.group(1).strip())
            class_match = re.search(classification_pattern, block)
            classification = class_match.group(1) if class_match else "unknown"
            extracted["지속"].append(
                {"name": name, "classification": classification, "block": block[:200]}
            )

    return extracted


def check_duplicates(
    extracted: Dict[str, List[Dict[str, Any]]], existing: Dict[str, Set[str]]
) -> Dict[str, List[Dict[str, Any]]]:
    """중복 검사 수행"""
    results: Dict[str, List[Dict[str, Any]]] = {
        "duplicates": [],
        "new_items": [],
        "similar_names": [],  # 유사한 이름 (나중에 확장 가능)
    }

    # 추출된 항목들을 분류별로 확인
    for category, items in extracted.items():
        for item in items:
            name = item["name"]
            classification = item["classification"]

            # 분류에서 파일명 추출
            # 예: `data/traits/10_정신.md` -> `traits/10_정신.md`
            target_file = classification.replace("data/", "").replace("`", "").strip()

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
                # 분류 파일이 없으면 새 항목으로 처리
                results["new_items"].append(
                    {
                        "name": name,
                        "category": category,
                        "file": target_file,
                        "classification": classification,
                        "note": "분류 파일이 존재하지 않음",
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
        f"  - Skill 파일: {len([f for f in existing.keys() if f.startswith('skill/')])}개"
    )

    # 리포트 파싱
    print(f"\n리포트 파싱 중: {report_path.name}")
    extracted = parse_report(report_path)
    print(f"  - 특성: {len(extracted['traits'])}개")
    print(f"  - 발동 능력: {len(extracted['발동'])}개")
    print(f"  - 지속 능력: {len(extracted['지속'])}개")

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
