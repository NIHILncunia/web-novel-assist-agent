# PLAN: 지속 어빌리티의 특성(Trait) 이관을 위한 매핑 및 분류 계획
> **Date:** 2026-02-02
> **Task ID:** 002_PLAN_PassiveAbilityMigrationMapping
> **Language:** Korean

## 1. Objective
`data/ability` 폴더 내에 잔류하고 있는 '지속(Passive)' 계열 어빌리티들을 전수 조사하여, 성격상 '특성(Trait)'에 부합하는 항목들을 선별한다. 실제 데이터를 이동하기 전, 별도의 매핑 파일을 생성하여 분류의 적절성을 마스터와 검토하고 데이터베이스 정규화를 달성한다.

## 2. Context Analysis
- **Target Files:**
  - `data/ability/지속_물리.md`
  - `data/ability/지속_마법.md`
  - `data/ability/지속_생산.md`
  - `data/ability/지속_정신.md`
  - `data/traits/*.md` (이관 대상 카테고리)
- **Current Issue:**
  - '지속 어빌리티'로 분류되어 있으나, 실제로는 '선천적 체질', '환경 적응력', '지식' 등 상시 적용되는 '특성'에 가까운 항목들이 혼재되어 있음.
  - 이로 인해 설정 조형 시 어빌리티와 특성 사이의 경계가 모호해지는 현상 발생.

## 3. Strategy
1. **분류 기준 수립**: 상시성(Permanence), 능동적 태세 필요 여부(Stance), 발원지(Innate vs Learned)를 기준으로 특성 이관 대상을 정의한다.
2. **별도 매핑 파일 생성**: `report/passive_ability_mapping.md` 파일을 생성하여 각 어빌리티별 타겟 트레잇 카테고리 및 근거를 명시한다.
3. **카테고리 매칭**: 기존 00~17번 트레잇 카테고리와 신규 생성될 카테고리(예: 19_직업 등)를 고려하여 최적의 위치를 할당한다.
4. **마스터 승인 후 이관**: 매핑 결과에 대해 마스터의 최종 승인을 득한 후, 실제 파일 수정을 진행한다.

## 4. Impact Analysis
- **Affected Files:**
  - `data/ability/지속_*.md`: 항목 삭제 및 분류 재정비.
  - `data/traits/*.md`: 새로운 항목 추가 및 데이터 확충.
- **Side Effects:**
  - 어빌리티 데이터베이스와 트레잇 데이터베이스 간의 참조 관계가 변동될 수 있음.
  - 기존에 어빌리티로 등록되어 있던 항목이 특성으로 바뀌면서 캐릭터 시트 작성 가이드라인의 수정이 필요할 수 있음.

## 5. Task List
- [ ] **Data Analysis**: 지속 어빌리티 파일 4종 전수 조사 및 이관 후보 선별
- [ ] **Drafting Mapping File**: `report/passive_ability_mapping.md` 작성 (이름, 현재 위치, 타겟 위치, 사유 포함)
- [ ] **Refining Categories**: 매핑 중 기존 트레잇 카테고리에 적합한 곳이 없을 경우 신규 카테고리 제안
- [ ] **Verification**: 매핑 완료 후 마스터에게 검토 요청

## 6. Verification Plan
- **Mapping Consistency**: 모든 이관 대상이 `PRD/PRD.md`에 정의된 트레잇 포맷(이름, 분류, 설명)을 준수할 수 있는지 확인.
- **Redundancy Check**: 기존 트레잇 데이터와 중복되는 항목이 없는지 `scripts/check_traits.py`를 활용해 검토 (스크립트 완료 시).
- **Manual Review**: 마스터의 피드백을 반영하여 최종 매핑 테이블 확정.
