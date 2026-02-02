# PLAN: Trait DB Normalization & Refactoring
> **Date:** 2026-02-02
> **Task ID:** 001_UPDATE_TraitRefactoring
> **Language:** Korean

## 1. Objective
트레잇 데이터베이스의 무결성을 검증하는 자동화 스크립트를 도입하고, 비대해진 `10_정신.md` 파일에서 '관계' 관련 항목을 분리하여 데이터 구조를 명확히 한다. 이를 통해 향후 데이터 확장성을 확보하고 관리 효율을 높인다.

## 2. Context Analysis
- **Target Files:**
  - `data/traits/*.md` (전체 트레잇 파일)
  - `data/traits/10_정신.md`
  - `scripts/check_traits.py` (신규 생성)
- **Current Issue:**
  - `data/traits` 내 파일들이 수동 관리되어 중복이나 포맷 오류가 발생하기 쉬움.
  - `10_정신.md` 파일이 너무 비대하며(430라인+), 성격이 다른 '사회적 관계' 데이터가 혼재되어 데이터 분류 체계가 모호함.

## 3. Strategy
1. **검증 스크립트 먼저 작성 (TDD)**: 데이터를 건드리기 전에 현재 상태를 검증할 수 있는 `check_traits.py`를 먼저 작성하여 현재의 오류(중복, 포맷 깨짐)를 리포팅한다.
2. **관계 데이터 분리**: `10_정신.md`에서 '관계', '상호작용' 등의 키워드를 가진 항목을 추출하여 신규 파일 `17_관계.md`로 이동한다.
3. **데이터 표준화**: 새 파일 생성 시 기존 마크다운 테이블 포맷을 엄격히 준수한다.

## 4. Impact Analysis
- **Affected Files:**
  - `data/traits/10_정신.md`: 라인 수 감소, 내용 변경.
  - `data/traits/17_관계.md`: 신규 생성.
- **Side Effects:**
  - 기존에 `10_정신.md`의 라인 번호나 절대 경로를 하드코딩해서 참조하던 외부 문서가 있다면 링크가 깨질 수 있음(현재 프로젝트 내에서는 없는 것으로 파악됨).
  - 트레잇 데이터를 로드하는 다른 스크립트(`check_missing_mcls.py` 등)에 영향이 없는지 확인 필요.

## 5. Task List
- [ ] **Python Setup**: `scripts/check_traits.py` (중복/포맷 검사) 작성
- [ ] **Data Refactoring**:
  - `17_관계.md` 파일 생성 (헤더 포함)
  - `10_정신.md`에서 관계 관련 항목 이동
  - `10_정신.md` 정리 (빈 줄 등)
- [ ] **Verification**: 스크립트 실행 및 결과 확인

## 6. Verification Plan
- **Pre-check**: 스크립트 작성 직후 기존 데이터에 대해 실행하여 오류 리포트 확인.
- **Post-check**: 데이터 분리 후 스크립트 재실행하여 `Clean` 상태(오류 0건) 확인.
- **Manual**: `17_관계.md` 파일이 정상적으로 렌더링되는지 육안 확인.
