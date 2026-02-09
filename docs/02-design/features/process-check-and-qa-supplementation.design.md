# Design: 현재 프로세스 점검 및 QA 보완

## 1. 데이터 무결성 감사 설계 (Data Integrity Audit)

### 1.1. 자동 검증 스크립트 활용
- **실행 스크립트**: `uv run python scripts/check_traits.py`
- **검증 항목**:
    - 파일명 규칙 (`NN_CategoryName.md`) 준수 여부.
    - 테이블 헤더 및 구분선 포맷 (`| :--- | :---: | :--- |`) 일치 여부.
    - 트레잇 이름 중복 검사.
- **결과 처리**: 발견된 오류를 `report/qa/data_audit_report.md`에 기록.

### 1.2. 수동 분류 점검
- **점검 대상**: `10_정신.md`, `17_관계.md` 등 최근 분리/수정된 파일.
- **기준**: `manuals/97_trait_and_naming_rules.md`의 분류 기준과 일치하는지 샘플링 검사.

## 2. 에이전트 스킬 검증 설계 (Skill Verification)

### 2.1. 스킬-템플릿 정렬 점검
- **대상 스킬**: `create_core_rules`, `create_item`, `create_character`
- **점검 내용**:
    - `SKILL.md` 내의 "출력 예시"가 현재 `templates/` 파일의 내용과 일치하는가?
    - `templates/` 내의 주석 및 가이드가 `Coding Rules & Guidelines.md`를 반영하는가?

### 2.2. 출력물 QA (Test Run)
- **방법**: 각 스킬을 임시 데이터로 실행하여 결과 파일 생성.
- **평가 기준**:
    - 생성된 파일의 Markdown 문법 오류 없음.
    - `PRD` 및 `Manuals`에서 요구하는 필수 섹션 포함 여부.

## 3. 메뉴얼 및 템플릿 동기화 설계 (Manual & Template Sync)

### 3.1. 11단계 프로세스 추적성 검사
- `manuals/` 폴더의 00~10 단계 문서와 대응하는 `.agent/skills/` 및 `_templates/` 매핑 테이블 작성.
- 누락된 템플릿이나 업데이트가 필요한 가이드 식별.

### 3.2. 공용 템플릿 업데이트
- `_templates/note_template.md` 등을 최신 프로젝트 스타일에 맞춰 갱신.

## 4. 구현 과업 (Implementation Tasks)

1.  **[QA-DATA]** `scripts/check_traits.py` 실행 및 결과 분석/수정.
2.  **[QA-SKILL]** 주요 스킬(3종) SKILL.md 및 템플릿 무결성 점검.
3.  **[QA-MANUAL]** 11단계 메뉴얼 - 스킬 - 템플릿 정렬표 작성.
4.  **[QA-REPORT]** 전체 점검 결과 요약 보고서 생성.

## 5. 성공 기준 (Success Criteria)
- `check_traits.py` 실행 시 Error 0건.
- 주요 스킬 3종의 출력물이 설계된 템플릿과 100% 일치.
- 메뉴얼에서 지시하는 모든 문서 양식이 `_templates/` 또는 스킬 내에 구비됨.
