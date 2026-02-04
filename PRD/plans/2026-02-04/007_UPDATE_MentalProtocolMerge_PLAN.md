# PLAN: 정신 권역 명사 -> 어빌리티 태그 프로토콜 병합
> **Date:** 2026-02-04
> **Task ID:** 007_UPDATE_MentalProtocolMerge
> **Language:** Korean (Required)

## 1. Objective
정신 권역 분석 리포트에서 도출된 핵심 키워드를 `report/ability_tag_protocol.md`에 병합하여 v0.4로 업데이트합니다.

## 2. Context Analysis
- **Source:** `report/정신권역_명사_분류_리포트.md`
- **Target:** `report/ability_tag_protocol.md` (v0.3)
- **Criterion:** 마법 권역 분석 때와 마찬가지로, 중복을 피하고 정신적 간섭 및 인지 능력을 대표하는 키워드 선정.

## 3. Merge Strategy (Candidate Mapping)

### 3.1. [상태] 카테고리 보강 (감정 및 인지 상태)
- **후보:** `위압`, `매료`, `동조`, `악몽`, `트라우마`, `죄책감`, `무기력`, `광화` (기존 '광분'과 차별화), `본능`

### 3.2. [기동] 및 [은밀] 보강
- **후보:** `직감` (위험 회피), `간파` (패턴 인식)

### 3.3. [특수] 및 [마법] 보강
- **후보:** `언령` (말을 통한 강제), `천리안` (원거리 인지), `예지` (미래 예지), `최면`, `암시`

### 3.4. [정신] 전용 섹션 검토
- 기존 4번 카테고리(상태이상 및 속성)가 너무 비대하므로, 정신적 메커니즘을 9번으로 분리할지 고민하였으나, 우선 4번과 8번에 적절히 배분하여 통합성을 유지함.

## 4. Impact Analysis
- **Affected Files:** 
    - `report/ability_tag_protocol.md` (v0.4 Update)
- **Note:** `망각`, `유혹`은 이미 v0.3에 추가되었으므로 중복 주의.

## 5. Task List
- [ ] `ability_tag_protocol.md` 업데이트 (v0.3 -> v0.4)
- [ ] 정신 권역 특화 태그 삽입

## 6. Verification Plan
- `위압`, `언령`, `천리안`, `예지` 등의 태그가 적절한 카테고리에 포함되었는지 확인.
