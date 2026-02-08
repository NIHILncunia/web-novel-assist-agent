# Coding Rules & Guidelines (Novel Assist Agent)

본 문서는 `novel-assist-agent` 프로젝트 전체의 일관성 유지와 효율적인 확장을 위한 개발 및 운영 규칙을 정의합니다.

## 1. Architectural Principles
*   **Single Source of Truth (SSOT)**: 모든 설정과 데이터는 '원본' 위치에 유일하게 존재해야 하며, 복제본은 최소화한다.
    *   **Manuals**: 11단계 워크플로우의 기준.
    *   **Bible (`00_bible/`)**: 작품 설정의 기준.
    *   **Data (`data/`)**: 공용 자산의 기준.
*   **Modularity (모듈성)**: 스킬(Skill), 워크플로우(Workflow), 데이터(Trait/Ability) 등 모든 기능 단위는 독립적으로 동작 가능하도록 설계한다.
*   **Progressive Enhancement (점진적 구체화)**: 초기 기획(`incubator`)부터 정식 연재(`projects`)까지, 단계별로 문서의 구체성을 높여가는 방식을 지향한다.

## 2. Directory & File Structure
```
novel-assist-agent/
├── manuals/                # (Step 0~10) 창작 프로세스 가이드
├── .agent/
│   ├── skills/             # [Skill] 에이전트 기능 모듈 (SKILL.md + templates/)
│   └── workflows/          # [Workflow] 자동화 커맨드 정의
├── _templates/             # [Template] 공용 문서 양식
├── data/                   # [Data] 트레잇(traits), 어빌리티(ability) 등 중앙 데이터
├── library/                # [Library] 재사용 가능한 세계관 에셋
├── incubator/              # [Incubator] 작품명 미정 프로젝트 (샌드박스)
└── projects/               # [Project] 정식 연재 프로젝트 (프로덕션)
```

## 3. Naming Conventions (Strict)

### 3.1. General Rules
*   **File Names**: `snake_case` 권장 (단, 폴더명 앞의 숫자는 정렬 용도).
    *   Ex: `00_bible`, `01_planning`, `create_item`.
*   **Variables (Python)**: `snake_case`.
*   **Classes (Python)**: `PascalCase`.

### 3.2. Trait Data Files (`data/traits/`)
*   Format: `NN_CategoryName.md`
*   `NN`: 00~99 숫자 (카테고리 ID).
*   `CategoryName`: 한글 사용 (띄어쓰기는 `_`).

### 3.3. Skill Directory (`.agent/skills/`)
*   Format: `skill_name/` (소문자, snake_case).
*   Structure:
    *   `SKILL.md`: 메인 설명 파일 (필수).
    *   `templates/`: 스킬 전용 템플릿 폴더.
    *   `scripts/`: 스킬 전용 파이썬 스크립트.

## 4. Operational Standards (운영 기준)

### 4.1. Incubator vs Projects
*   **Incubator**: 제목이 정해지지 않은 아이디어 단계. 폴더명은 `[가제_컨셉명]` 사용.
*   **Projects**: 시놉시스(Step 4) 완성 후 제목이 확정된 단계. `incubator` 폴더를 `projects`로 이동(Rename)하여 승격.

### 4.2. Data Management (Trait/Ability)
*   **Traits**: 태생적 성질. `data/traits/`에 저장.
*   **Abilities**: 후천적 능력. `data/ability/`에 저장.
*   **Consistency**: `verify_traits.py` 등의 스크립트를 통해 주기적으로 포맷 및 중복 검사를 수행한다.

### 4.3. Documentation Style
*   **Tone**: 명확하고 간결하게.
*   **Template**: `_templates/` 또는 스킬별 `templates/`에 정의된 양식을 우선 사용.
*   **Language**: 한글 작성을 원칙으로 한다.

## 5. Quality Assurance
*   **Linting**: Python `uv` 환경에서 `black` 또는 `flake8` 사용 (스크립트 개발 시).
*   **Manual Review**: 새로운 스킬이나 데이터 추가 시, 기존 체계와 충돌하지 않는지 `manuals/`를 참조하여 점검.
