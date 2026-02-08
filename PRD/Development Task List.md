# Development Task List (Novel Assist Agent)

본 문서는 `novel-assist-agent` 프로젝트의 전체적인 개발 로드맵과 세부 과업을 정의합니다.

## Phase 1: Foundation (기반 구축) - [Completed]
> 에이전트 핵심 구조와 11단계 창작 프로세스 메뉴얼 완비.
- [x] **Core Directory**: `manuals/`, `_templates/`, `data/`, `incubator/`, `projects/` 구조 확립.
- [x] **Base Manuals**: Step 0 ~ Step 10 창작 가이드 문서 작성 (`manuals/*.md`).
- [x] **Agent Config**: `.agent/` 폴더 내 기본 설정 및 워크플로우 정의.
- [ ] **Initial PRD**: 프로젝트 성격 정의 및 문서화 (본 문서 포함 PRD 3종).

## Phase 2: Data Standardization (데이터 정규화) - [In Progress]
> 트레잇, 어빌리티 등 창작 재료(Data)의 일관성 확보.
- [x] **Trait Cleanup**: `10_정신` 분리 (`17_관계`), 모호한 트레잇 재배치.
- [x] **Format Unification**: Markdown Table 포맷 표준화 (`Coding Rules` 참조).
- [x] **Expansion**: `15_속성`, `19_직업` 등 신규 카테고리 추가.
- [ ] **Validation Script**: `verify_traits.py` (중복 검사, 포맷 검사 자동화 스크립트) 개발.

## Phase 3: Skill Expansion (기능 고도화) - [Active]
> 에이전트가 수행할 수 있는 '스킬'들을 개발하고 고도화.
- [x] **Core Rules**: `create_core_rules` 스킬 개발 및 템플릿 개선 (주요 설정 명칭 변경 등).
- [x] **Item Creation**: `create_item` 스킬 및 `아이템.md` 연동.
- [ ] **Character Design**: `create_character` (또는 `create_npc`) 스킬 고도화.
- [ ] **World Building**: `create_nation`, `create_organization` 등 세계관 구축 스킬 정교화.

## Phase 4: Automation & Optimization (자동화 및 최적화)
> 반복 작업을 줄이고 에이전트의 자율성을 높이는 단계.
- [ ] **Auto-Review**: `review_world` 스킬을 활용한 설정 오류 자동 리포팅 시스템.
- [ ] **Sync Script**: `incubator` -> `projects` 승격 시 파일 이동 및 링크 자동 수정 스크립트.
- [ ] **Backup System**: `archive/` 폴더로의 자동 백업 워크플로우 구축.

## Phase 5: Documentation & Maintainance
- [ ] **User Guide**: 작가를 위한 `README.md` 개선 및 `START_HERE.md` 튜토리얼 보강.
- [ ] **Legacy Archive**: 구버전 데이터 및 문서 아카이빙 전략 수립.
