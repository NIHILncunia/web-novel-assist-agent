---
name: enhance_entity
description: Analyze an entity (character, monster, etc.) and suggest existing Traits/Skills from the database to enrich its setting.
---

# 기능: 내 엔티티 강화 (`enhance_entity`)

이 **skills enhance_entity**는 마스터의 프로젝트 내 특정 엔티티(캐릭터, 몬스터 등)를 분석하고, 현재 구축된 DB(`data/traits/`, `data/ability/`)에서 적합한 태그 및 어빌리티를 제안합니다.

## 1. 핵심 철학
- **LEGO Block:** 모든 트레잇/어빌리티는 출처 불문 자유롭게 조립 가능한 '공용 레고 블록'입니다.
- **재해석:** 몬스터의 트레잇을 인물에게, 혹은 그 반대로 재해석하여 적용합니다.

## 2. 작업 프로세스

### 1단계: 엔티티 분석
- 대상의 이름과 설정 파일 위치 입력.
- 핵심 테마 키워드 3~5개 추출.

### 2단계: DB 검색 및 매칭
- 각 키워드에 대해 `data/traits/` 및 `data/ability/` 검색.
- 연관되거나 시너지가 있는 기존 항목 식별.

### 3단계: 제안 목록 구성
- **직관적 매칭 (3+):** 키워드와 정확히 일치.
- **창의적 비틀기 (2+):** 의외의 조합, 서사적 시너지.
- **비전투 확장:** 경영, 생활, 정신 등 비전투 분야 적극 제안.

## 3. 적용 가이드
- 선택된 항목을 엔티티 파일의 `15. 트레잇 및 어빌리티` 섹션에 추가.
- DB에는 이미 존재하므로 중복 추가 불필요.
