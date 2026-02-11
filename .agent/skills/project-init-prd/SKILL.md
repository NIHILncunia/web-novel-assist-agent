---
name: project-init-prd
description: bkit 표준에 따른 프로젝트 초기화 및 PRD/PDCA 체계 구축 가이드. 프로젝트 시작 시 PRD 폴더와 docs 폴더를 병렬로 구성하고 표준 템플릿을 생성합니다.
---

# Project Init with bkit PDCA Standard

## Instructions

이 스킬은 프로젝트의 기초를 bkit 표준(PDCA 방법론 + 병렬 폴더 구조)에 맞게 **초기화하거나 갱신**하기 위한 가이드입니다.

### 1. 폴더 구조 구축 (Parallel Structure)

프로젝트 루트에서 다음과 같이 목적이 분리된 두 개의 폴더를 생성합니다.

- **PRD/**: 프로젝트 설계도 및 고정 규칙
    - `PRD.md`: 프로젝트 개요 및 상세 사양
    - `Coding-Rules.md`: 프로젝트 전용 코딩 규칙
    - `Task-List.md`: 작업 목록 및 상태 관리
- **docs/**: 활동 기록 및 실시간 계획/결과 (PDCA 사이클)
    - `01-plan/`: 계획 단계 산출물
    - `02-design/`: 설계 단계 산출물
    - `03-analysis/`: 검증/분석 단계 산출물
    - `04-report/`: 결과 보고 단계 산출물

---

### 2. 표준 PRD 3종 템플릿

#### 2-1. `PRD/PRD.md`
```markdown
# Product Requirements Document (PRD)

## 1. 개요
- **목표**: [프로젝트 핵심 목표]
- **주요 가치**: [사용자에게 제공하는 핵심 가치]

## 2. 기술 스택
- **언어/런타임**: [TypeScript v5.0+, Node.js v20+ 등]
- **주요 라이브러리**: [핵심 라이브러리 목록]

## 3. 상세 사양 (Functional Requirements)
- **기능 A**: [상세 로직 및 동작 방식]
- **기능 B**: [...]
```

#### 2-2. `PRD/Coding-Rules.md`
```markdown
# Coding Rules & Guidelines

## 1. 아키텍처 원칙
- **패턴**: [Clean Architecture, DDD 등]
- **레이어 구성**: [Presentation, Application, Domain, Infrastructure 등]

## 2. 코드 규칙 (Convention)
- **네이밍**: [PascalCase, camelCase, kebab-case 등]
- **에러 핸들링**: [에러 처리 전략]
```

#### 2-3. `PRD/Task-List.md`
```markdown
# Development Task List

## [Phase 1] 초기화 및 기반 구축
- [ ] 프로젝트 초기화 및 PRD 셋업
- [ ] 폴더 구조 및 기초 설정

## [Phase 2] 핵심 기능 개발
- [ ] 기능 A 구현
- [ ] 기능 B 구현
```

---

### 3. PDCA 프로세스 적용 규칙

1. **시작**: 모든 작업은 `docs/01-plan/` 내의 계획 파일 생성에서 시작합니다.
2. **명명**: 파일명은 반드시 `{YYYY-MM-DD}-{feature}-{Type}.md` 형식을 준수합니다.
3. **조회**: 진행 상황 문의 시 `docs/`의 활동 기록을 먼저 확인하고, `PRD/Task-List.md`로 전체 맥락을 보완합니다.

---

## Examples

### 새 프로젝트 초기화 (/create-prd 실행 시)
1. 루트에 `PRD/` 폴더가 없음을 확인.
2. `PRD/` 폴더와 `docs/` 하위 4개 폴더를 생성.
3. 위 템플릿을 사용하여 초기 문서 3종 작성.
4. `.cursorrules` 및 `.agent/rules/`에 bkit PDCA 프로토콜을 복사하여 행동 지침 고정.
