---
name: agentic_validator
description: A precision tool for detecting setting collisions, logic contradictions, and genre-consistency issues across all world Bible and planning files.
---

# 기능: 지능형 설정 검증 (`agentic_validator`)

이 스킬은 작품의 모든 설정 파일(`00_bible`)과 기획 문서(`01_planning`)를 교차 검증하여 논리적 모순이나 설정 충돌을 사전에 차단합니다.

## 1. 개요
- **역할:** 철두철미한 설정 감수자 / 논리 검증 에이전트
- **핵심 목표:** "앞뒤가 안 맞는 설정" 및 "장르 규칙 위반" 전수 조사.
- **주요 참조:** `data/common/conflict_patterns.md`, `data/common/cliches.md`, `00_bible` 하위 모든 파일.

## 2. 검증 프로세스 (Contradiction Drill)

### 1단계: 캐릭터 일관성 검증
- **트레잇 vs 행동:** 캐릭터의 트레잇(예: '비겁함')이 챕터 플롯의 행동(예: '용감하게 선봉에 섬')과 모순되지 않는가?
- **어빌리티 vs 숙련도:** 설정된 어빌리티 등급이나 유형이 전투 묘사에서 갑자기 비약하지 않는가?

### 2단계: 세계관 규칙 검증 (Murim/Fantasy/Systems)
- **마력/내공 자원:** 설정된 에너지 체계(내공/마나) 소모 법칙이 지켜지고 있는가?
- **사회적 위계:** 국가/단체(`05_nations`, `04_organizations`) 설정상의 예법이나 위계가 대화문에서 무너지고 있지 않는가?

### 3단계: 갈등 및 상성 분석
- **상성 활용:** `conflict_patterns.md`를 바탕으로, 현재 캐릭터 조합에서 나올 수 있는 최적의 갈등이 활용되고 있는가?
- **관계도 충돌:** `09_relationships.md`에 정의된 적대 관계가 장면에서 느닷없이 우호적으로 묘사되지 않는가? (복선 없는 변절 확인)

### 4단계: 클리셰 및 트로프 점검
- **장르 적합성:** `cliches.md`를 참조하여, 현재 장르에 기대되는 재미 요소가 충분히 배치되었는가?
- **식상함 방지:** 너무 뻔한 클리셰일 경우 '비틀기 아이디어'가 적용되었는지 확인.

## 3. 출력 리포트 (Validator Feedback)
에이전트는 발견된 충돌 사항을 **[위험 등급]**에 따라 분류하여 보고합니다.

- **🔴 CRITICAL:** 스토리 전개를 불가능하게 만드는 치명적 설정 오류 (예: 죽은 인물의 재등장)
- **🟡 WARNING:** 개연성이 떨어지거나 설명이 필요한 지점 (예: 갑작스러운 성격 변화)
- **🔵 SUGGESTION:** 더 나은 재미나 효율을 위한 제안 (예: 갈등 상성 활용 제안)

## 4. 실행 시점
- 신규 캐릭터/장소 추가 시 `00_bible` 업데이트 직후.
- 챕터 설계도(`01_planning/06_chapter_plans/`) 작성 완료 후 집필 직전.
