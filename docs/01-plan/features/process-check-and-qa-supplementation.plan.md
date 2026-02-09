# Plan: 현재 프로세스 점검 및 QA 보완

## 1. 배경 및 목적
- **배경**: Phase 2(데이터 정규화)와 Phase 3(스킬 고도화)이 진행됨에 따라 기존 데이터와 메뉴얼 간의 불일치 가능성 증대.
- **목적**: 11단계 창작 프로세스의 안정성을 확보하고, 에이전트 스킬이 생성하는 결과물의 품질을 보증하기 위한 체계 점검.

## 2. 주요 과업 (Key Tasks)

### 2.1. 데이터 무결성 감사 (Data Integrity Audit)
- **대상**: `data/traits/`, `data/ability/`
- **내용**: 
    - `Coding Rules`에 정의된 Markdown Table 포맷 준수 여부 확인.
    - 중복 데이터 및 모호한 분류(정신 vs 관계 등) 재점검.
    - `scripts/check_traits.py` 등 기존 스크립트를 활용한 자동 검사 실행 및 결과 분석.

### 2.2. 에이전트 스킬 검증 (Skill Verification)
- **대상**: `.agent/skills/` 내 주요 스킬 (`create_core_rules`, `create_item` 등)
- **내용**: 
    - 각 스킬의 `SKILL.md` 지침과 실제 동작(출력물)의 일치성 확인.
    - 스킬별 `templates/`가 최신 `Coding Rules`를 반영하고 있는지 점검.
    - 테스트 케이스를 통한 출력물 품질 QA.

### 2.3. 메뉴얼 및 템플릿 동기화 (Manual & Template Sync)
- **대상**: `manuals/`, `_templates/`
- **내용**: 
    - 11단계 메뉴얼의 단계별 설명이 현재 에이전트 기능과 일치하는지 확인.
    - 공용 템플릿(`note_template.md` 등)의 최신화.
    - `PRD`와 `Manuals` 간의 용어 정의 통일성 점검.

### 2.4. QA 자동화 기반 마련 (QA Automation Foundation)
- **대상**: 프로젝트 전반
- **내용**: 
    - Phase 4의 `Auto-Review` 시스템 구축을 위한 오류 패턴 정리.
    - 주기적인 QA를 위한 체크리스트 문서화.

## 3. 일정 및 우선순위
1. **우선순위 High**: 데이터 무결성 감사 (데이터가 깨지면 모든 스킬이 오작동함)
2. **우선순위 Medium**: 스킬 검증 및 메뉴얼 동기화
3. **우선순위 Low**: QA 자동화 기반 마련

## 4. 기대 효과
- 에이전트가 생성하는 데이터의 신뢰도 100% 확보.
- 작가가 메뉴얼을 따라 작업할 때 혼선 방지.
- 향후 자동화(Phase 4)를 위한 견고한 기반 마련.
