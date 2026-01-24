---
name: brainstorm_ideas
description: A keyword brainstorming engine that expands a single keyword into related Traits, Contrasting Traits, Passive Skills, and Active Skills. Updates `data/traits/` and `data/ability/`.
---

# 기능: 키워드 확장 엔진 (`brainstorm_ideas`)

이 스킬은 단일 '핵심 키워드'를 입력받아, 세계관 구축에 필요한 '특성'과 '능력'으로 확장하는 범용 브레인스토밍 지침입니다.

## 1. 개요 및 저장 위치

- **목적:** 데이터베이스 풍부화.
- **저장 위치:** `data/traits/` 및 `data/ability/`

## 2. 작업 프로세스

### 0단계: 기존 데이터베이스 분석 (Pre-check)
- 입력된 키워드가 이미 DB에 있는지 검색.
- 발견 시 "기존 연관 항목"으로 분류하여 제시.

### 1단계: 신규 아이디어 확장
다음 4가지 방향으로 **새로운** 아이디어를 생성합니다.

1. **연관 특성 (Related Traits):**
   - 질문: "이 키워드와 직접적으로 연관되거나 본질적인 특성은?"
   - 목표: 2~3개 (`data/traits/`용)

2. **반전 특성 (Contrasting Traits):**
   - 질문: "정반대 개념이거나, 왜곡/극복 시 나타나는 특성은?"
   - 목표: 2~3개 (`data/traits/`용)

3. **연관 지속 능력 (Related Passives):**
   - 질문: "파생되는 상시 발현 능력은?"
   - 목표: 1~2개 (`data/ability/지속.md`용)

4. **연관 발동 능력 (Related Actives):**
   - 질문: "의지를 갖고 사용하는 능력은?"
   - 목표: 1~2개 (`data/ability/발동.md`용)

## 3. 데이터 저장 지침

1. 사용자 선택 항목을 `data/traits/` 또는 `data/ability/`의 적절한 파일에 추가.
2. 중복 방지 필수.
