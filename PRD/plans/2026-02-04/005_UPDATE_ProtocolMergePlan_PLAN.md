# PLAN: 마법 권역 명사 -> 어빌리티 태그 프로토콜 병합 계획
> **Date:** 2026-02-04
> **Task ID:** 005_UPDATE_ProtocolMergePlan
> **Language:** Korean (Required)

## 1. Objective
마법 권역 명사 분류 리포트에서 도출된 핵심 키워드를 선별하여 `report/ability_tag_protocol.md` (v0.2)에 병합합니다. 이를 통해 v0.3으로 업데이트하며, 마법적 디테일을 보강합니다.

## 2. Context Analysis
- **Source:** `report/마법권역_명사_분류_리포트.md` (700+ 명사 데이터)
- **Target:** `report/ability_tag_protocol.md` (v0.2)
- **Criterion:** 기존 태그와 중복되지 않아야 하며, 어빌리티 분류에 실질적인 도움이 되는 '속성', '행위', '효과' 위주로 선정.

## 3. Merge Strategy (Candidate Mapping)

분석된 명사를 기존 8개 카테고리에 맞춰 배정합니다.

### 3.1. [공격] 메커니즘 보강
- **후보:** `압축` (마법적 힘을 압축하여 타격)

### 3.2. [방식] 투사 방식 보강
- **후보:** `추적` (유도 기능), `광선` (레이저 형태)

### 3.3. [영향] 파괴 및 영향 보강
- **후보:** `초토화` (광범위 파괴), `용해` (녹임)

### 3.4. [상태] 속성 및 상태이상 보강
- **후보:** 
    - 속성: `진흙`, `모래`, `산성비`, `마기`
    - 상태: `망각` (기억 소거), `유혹` (정신 계열)

### 3.5. [특수] 특수 능력 보강
- **후보:** `수복` (생명체가 아닌 물체/결계 수리), `봉인` (기능 정지), `변형` (구조 변경)

### 3.6. [마법] 마법 및 초자연 보강 (대거 추가)
- **후보:** 
    - `분신` (Clone/Illusion)
    - `주술` (Shamanism/Hex)
    - `지맥` (Leyline manipulation)
    - `연금` (제조/변환 - '제조' 키워드 대체)
    - `부여` (Enchant)
    - `활성화` (Activation)

## 4. Impact Analysis
- **Affected Files:** 
    - `report/ability_tag_protocol.md` (v0.3 Update)
- **Note:** 이미 v0.2에 `흡수`, `복제`, `투명화`, `반사`, `조작` 등이 포함되어 있으므로 중복 제외에 유의함.

## 5. Task List
- [ ] `ability_tag_protocol.md` 업데이트 (v0.2 -> v0.3)
- [ ] 각 카테고리별 신규 태그 삽입

## 6. Verification Plan
- 업데이트 후 `압축`, `추적`, `망각`, `지맥` 등의 키워드가 올바른 카테고리에 들어갔는지 확인.
