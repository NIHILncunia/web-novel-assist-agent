---
name: extract_creature_tags
description: Analyze a monster description to extract standardized Traits (Origin, Physical, Intellect, etc.) and Skills (Active, Passive). Updates `data/traits/` and `data/ability/`.
---

# 기능: 몬스터 태그 추출 (`extract_creature_tags`)

이 **skills extract_creature_tags**는 입력된 몬스터(생물) 정보를 분석하여 **생물 유형, 핵심 트레잇, 2대 생물 어빌리티(발동/지속)**을 추출하고, 이를 기반으로 데이터베이스를 확장합니다.

## 1. 개요 및 저장 위치

- **목적:** 몬스터 데이터를 '공용 레고 블록'화하여 DB에 저장.
- **저장 위치:** `data/traits/` (키워드 누적), `data/ability/` (어빌리티 상세)

## 2. 작업 지침

### 2-1. 명명 규칙 (규칙 준수)
- 명사형 종결 ("화염 방사" O, "불을 뿜는다" X).
- D&D 용어는 소설에 맞게 변환.
- **범용성:** 인물도 사용할 수 있는 형태로 정의.

### 2-2. 분석 축 (Classification Axes)

1. **생물 유형/크기:** `data/traits/00_유형.md`, `01_크기.md` 참조.
2. **핵심 트레잇 키워드:**
   - 기원 (Origin): 출생, 배경.
   - 신체 (Physical): 재질, 형태, 내성.
   - 지성 (Intellect): 지능, 성격, 소통 (`04_지식_지혜.md` 참조).
   - 군집 (Social): 사회성, 서열.
   - 약점 (Weakness): 치명적 결함.
   - 이동 (Mobility): 이동 방식 (비행 등).
   - 감각 (Senses): 인지 어빌리티 (야간 시야 등).
3. **생물 어빌리티 (Abilities):**
   - **발동 (Active):** 행동 소모 기술.
   - **상시 (Passive):** 상시 적용 효과.
   - **전설 (Legendary):** 전설적 행동/트레잇.

### 2-3. 확장 (Brainstorming)
- 주된 유형 외에 파생/반대/심화 키워드를 5개 이상 추가 연상.

## 3. 데이터 저장 지침

1. **트레잇 키워드:** `data/traits/[분류].md`에 누적 저장.
2. **어빌리티:** `data/ability/detailed_lists/[권역]권역/[권역]_[계통]계_[형태].md`에 테이블 형식으로 추가.
   - 구조: `[권역:원천]-[계통]-[형태]` 준수.
