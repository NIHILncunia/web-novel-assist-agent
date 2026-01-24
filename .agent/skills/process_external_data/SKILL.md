---
name: process_external_data
description: Extract information from external sources like PDF rulebooks (D&D) using provided tools and scripts.
---

# 기능: 외부 데이터 처리 (`process_external_data`)

PDF 룰북 등 외부 문서에서 정보를 추출하여 프로젝트 데이터베이스(Word List, Traits, Skills)로 변환합니다.

## 1. 개요
- **목표:** 참고 자료(Reference)의 데이터베이스화.
- **도구:** `tools/extract_pdf_text.py`

## 2. 작업 모드 (Modes)

### Mode 1: D&D 몬스터 추출
- **입력:** D&D PDF 파일 (`library/references/D&D/`).
- **도구 명령:** `uv run python scripts/extract_pdf_text.py "path" ...`
- **출력 위치:** `data/word_list/creature_dnd/[Abbreviation]/`.
- **처리 규칙:**
  - 게임 메카닉(수치) 제거 -> 서사적 묘사로 변환.
  - `data/word_list/dnd_terminology.md` 용어 순화 규칙 적용.
  - **트레잇(Traits)** 및 **어빌리티(Abilities)** 분리 추출.

## 3. 실행 프로세스
1. `library/references/D&D/index.md` 등 인덱스 확인.
2. `extract_pdf_text.py` 스크립트로 텍스트 추출.
3. 추출된 텍스트를 `prompt/05_data_processing/extract_dnd_monsters.md`의 양식에 맞춰 가공.
4. 결과 파일 저장.
