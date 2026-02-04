# PLAN: 마법 권역 어빌리티 분석 및 태그화
> **Date:** 2026-02-04
> **Task ID:** 001_UPDATE_MagicAbilityAnalysis
> **Language:** Korean (Required)

## 1. Objective
마법 권역 어빌리티의 설명을 전수 조사하여 핵심 키워드(태그)를 추출하고, 이를 `report/ability_tag_protocol.md`에 반영하여 데이터베이스 정규화의 기초를 마련합니다.

## 2. Context Analysis
- **Target Files:** `data/ability/detailed_lists/1.마법권역/*.md`
- **Current Issue:** 현재 `report/ability_tag_protocol.md`는 물리 권역 위주로 작성되어 있어 마법적 특성을 충분히 반영하지 못하고 있음. 마법 권역의 메커니즘을 분석하여 표준 태그를 보강해야 함.

## 3. Strategy
1. **데이터 추출**: `1.마법권역` 폴더 내 30여 개 파일에서 어빌리티 이름과 설명을 추출하여 리포트 생성.
2. **태그 분석**: 추출된 설명문에서 마법적 메커니즘(방출, 구현, 제어 등), 속성(원소), 영향력을 나타내는 키워드 도출.
3. **프로토콜 업데이트**: 기존 7개 카테고리를 확장하거나 마법 특화 카테고리를 추가하여 `ability_tag_protocol.md` 갱신.

## 4. Impact Analysis
- **Affected Files:** 
    - `report/ability_tag_protocol.md` (업데이트)
    - `report/마법권역_어빌리티_설명_목록.md` (신규 생성)
    - `report/마법권역_어빌리티_태그_분석.md` (신규 생성)
- **Side Effects:** 기존 물리 권역 태그와의 정렬성 유지가 필요함.

## 5. Task List
- [ ] 마법 권역 어빌리티 설명 추출 및 목록 리포트 생성
- [ ] 추출된 설명을 기반으로 태그 분석 리포트 작성
- [ ] `report/ability_tag_protocol.md`에 분석 결과 통합 및 업데이트

## 6. Verification Plan
- `report/마법권역_어빌리티_설명_목록.md`에 모든 마법 권역 파일의 데이터가 포함되었는지 확인.
- 도출된 태그가 마법 권역 어빌리티의 특성을 대표하는지 검토.
- `ability_tag_protocol.md`의 형식이 기존과 일관성을 유지하는지 확인.
