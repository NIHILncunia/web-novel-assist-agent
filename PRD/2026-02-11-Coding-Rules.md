# Coding Rules & Guidelines

## 1. bkit Standard Architecture (Agentic)
* **Design Pattern**: **Skill-based Modular Architecture**
    * **Core**: `manuals/` (Logic Definition)
    * **Tools**: `.agent/skills/` (Functional Units)
    * **Data**: `data/` (Static Resources), `library/` (Shared Assets)
* **Directory Structure**:
    ```
    novel-assist-agent/
    ├── manuals/          # Business Logic (Workflow)
    ├── .agent/           
    │   ├── skills/       # Executable Capabilities
    │   └── workflows/    # Orchestration Flows
    ├── projects/         # User Data (Runtime)
    ├── incubator/        # User Data (Staging)
    └── data/             # System Data
    ```

## 2. Naming Conventions (Strict)
* **Files (System)**: `kebab-case` or `snake_case` (consistent within folders).
    * Manuals: `00_topic.md` (Numbered prefixes for ordering).
* **Files (User Content)**: 
    * Convention: `00_bible`, `01_planning` (Numbered folders).
* **Skills**: `snake_case` (e.g., `create_character`, `brainstorm_ideas`).
* **Workflows**: `kebab-case` (e.g., `create-prd`, `bkit-init`).
* **PDCA Documents**:
    * Location: `docs/01-plan/`, `docs/02-design/`, `docs/03-analysis/`, `docs/04-report/`.
    * Naming: `YYYY-MM-DD-feature_STAGE.md` (e.g., `2026-02-11-bkit_update_PLAN.md`).
    * Format: 반드시 글로벌 템플릿(`.agent/templates/*.template.md`)을 기반으로 작성.

## 3. Coding Standards (Python / Markdown)
* **Markdown**:
    * Headers: Use `#` for Hierarchy. Step headers are specific.
    * Links: Use relative paths `./` for portability.
    * Frontmatter: Use YAML for metadata if needed.
* **Python (Scripts/Skills)**:
    * **Type Hinting**: 모든 함수 인자와 반환값에 타입 힌트 필수.
    * **Docstrings**: Google Style Docstrings 권장.
    * **Error Handling**: 파일 입출력 시 `try-except` 필수.
* **Interactive Rules (LLM)**:
    * **System Prompt Compliance**: `GEMINI.md` 및 `manuals/`의 지침을 최우선으로 준수.
    * **Language**: Always answer in **Korean** (User rule).
    * **Validation**: 파일 생성 전 반드시 사용자 승인(Review) 절차 거침.
* **bkit Commands**: 
    * `/pdca plan [feature]`: 기획 시작.
    * `/pdca report [feature]`: 최종 보고서 작성.
    * 모든 답변 하단에 **bkit Feature Usage 리포트** 필수 포함.
