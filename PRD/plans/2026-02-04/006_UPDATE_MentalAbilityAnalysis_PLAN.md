# PLAN: 정신 권역 어빌리티 분석 및 태그화
> **Date:** 2026-02-04
> **Task ID:** 006_UPDATE_MentalAbilityAnalysis
> **Language:** Korean (Required)

## 1. Objective
정신 권역 어빌리티의 설명을 전수 조사하여 핵심 어절 및 명사를 추출하고, 이를 분류하여 `ability_tag_protocol.md`에 반영합니다. 정신적 간섭, 감지, 강화 등의 특성을 추출하는 것이 핵심입니다.

## 2. Context Analysis
- **Target Files:** `data/ability/detailed_lists/3.정신권역/*.md`
- **Current Issue:** 현재 프로토콜은 물리/마법 위주이며, 정신 권역의 독특한 메커니즘(기억, 감정, 인지, 최면 등)에 대한 태그가 부족할 수 있음.

## 3. Strategy
1. **데이터 추출**: 정신 권역 15개 파일에서 이름과 설명을 추출하여 리포트 생성.
2. **어절/명사 분석**: 
    - 공백 기준 전수 어절 빈도 분석.
    - 조사 제거를 통한 핵심 명사 추출.
3. **카테고리 분류**: 정신 권역 특성에 맞는 새로운 체계(인지, 감정, 기억, 의지 등)로 분류.
4. **프로토콜 업데이트**: 유의미한 키워드를 `ability_tag_protocol.md` v0.4로 업데이트.

## 4. Impact Analysis
- **Affected Files:** 
    - `report/정신권역_어빌리티_설명_목록.md`
    - `report/정신권역_어빌리티_어절_빈도_분석.md`
    - `report/정신권역_어빌리티_명사_분석.md`
    - `report/정신권역_명사_분류_리포트.md`
    - `report/ability_tag_protocol.md` (Update to v0.4)
- **Side Effects:** 기존 마법 권역과 겹치는 '정신' 카테고리를 더 세분화하거나 통합하는 정리가 필요함.

## 5. Task List
- [ ] 정신 권역 설명 추출 및 목록 생성
- [ ] 어절 빈도 및 명사 추출 분석 실행
- [ ] 정신 권역 명사 분류 및 리포트 작성
- [ ] 프로토콜 병합 및 업데이트

## 6. Verification Plan
- 정신 권역 특유의 키워드(동조, 매료, 예지, 위압 등)가 정확히 추출되었는지 확인.
- 분류 체계가 정신 권역의 계통(간섭, 감지, 강화, 구현)을 잘 반영하는지 검토.
