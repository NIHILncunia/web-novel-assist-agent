# PRD: Novel Assist Agent (Web Novel Creation Assistant)

## 1. Project Overview
*   **Goal**: 웹소설 창작의 전 과정(아이디어 발상 ~ 퇴고)을 체계적으로 보조하는 **AI 에이전트 기반 프레임워크**를 구축한다. 작가의 고유 문체를 학습하고, 설정 오류를 방지하며, 창작의 효율성을 극대화한다.
*   **Target User**:
    *   **Primary**: 웹소설 작가 (프로/아마추어) - 체계적인 설정 관리와 집필 보조를 필요로 함.
    *   **Secondary**: 세계관 기획자 - 방대한 설정 데이터(트레잇, 아이템 등)를 관리해야 함.
*   **Key Value**:
    *   **Process-Driven (체계성)**: 11단계 워크플로우를 통해 창작의 방향성 상실 방지.
    *   **Consistency (일관성)**: 'Single Source of Truth' 원칙에 따른 설정 관리로 오류 제로화.
    *   **Modularity (재사용성)**: 세계관, 인물, 설정을 모듈화하여 타 작품에서도 재사용 가능.

## 2. Tech Stack & Environment
*   **Core Logic**: Python 3.10+ (Managed by `uv`)
*   **Data Format**: Markdown (CommonMark) - Human-readable & AI-parseable.
*   **AI Models**: LLM Agnostic (Gemini, Claude, GPT-4 등 지원).
*   **Version Control**: Git / GitHub.
*   **Editor**: Cursor, VS Code (Recommended Extensions: Markdown All in One).

## 3. System Architecture & Features

### 3.1. 11-Step Creative Workflow (Manuals)
*   **Step 0~1 (Preparation)**: 아이디어 발상 및 스타일(문체) 설정.
*   **Step 2~4 (Planning)**: 세계관 선택, 로그라인, 시놉시스 작성 및 프로젝트 승격.
*   **Step 5 (World Building)**: 상세 설정(캐릭터, 단체, 아이템 등) 확정.
*   **Step 6~7 (Structure)**: 플롯 아웃라인 및 챕터별 설계.
*   **Step 8 (Review)**: 집필 전 최종 점검 (QA).
*   **Step 9~10 (Writing)**: 본문 집필 및 퇴고.
*   **Storage Strategy**:
    *   `incubator/`: 기획 단계 (가제)
    *   `projects/`: 확정 단계 (정식 연재)

### 3.2. Core Features (Detailed)
*   **Feature A: Trait Database (트레잇 DB 정규화)**
    *   **Goal**: 캐릭터/몬스터 생성의 기본 재료인 '트레잇' 데이터의 표준화.
    *   **Logic**: 모호한 분류(정신 vs 관계 등)를 명확히 하고, 테이블 포맷을 통일하여 검색 효율성 증대.
    *   **Files**: `data/traits/NN_Category.md` 형식을 엄격히 준수.
*   **Feature B: Skill System (에이전트 스킬)**
    *   **Goal**: 특정 작업을 수행하기 위한 에이전트 전용 도구 모음.
    *   **Implementation**: `.agent/skills/` 내에 `SKILL.md`와 `templates/`를 패키징하여 관리.
    *   **Examples**: `create_core_rules`, `create_item`, `create_character` 등.

## 4. Data Structure (Schema)

### 4.1. Project Structure
```
novel-assist-agent/
├── manuals/            # 11단계 가이드
├── data/               # 공용 데이터 (Traits, Word List)
├── library/            # 재사용 가능한 에셋 (Shared World)
├── incubator/          # 기획 중인 프로젝트
└── projects/           # 정식 연재 프로젝트
```

### 4.2. Trait Data Schema (Markdown Table)
```markdown
# XX. 카테고리명
> **설명:** 카테고리 정의.
| 트레잇 이름 | 하위 분류 | 트레잇 설명 |
| :--- | :---: | :--- |
| **키워드** | 태그 | 효과 및 묘사 |
```

## 5. Non-Functional Requirements & Risks
*   **Scalability**: 프로젝트 수가 늘어나도 폴더 구조가 복잡해지지 않도록 `incubator`와 `projects`를 엄격히 분리한다.
*   **Data Integrity**: 수동 편집 시 포맷이 깨질 위험이 있으므로, `verify_traits.py` 등 검증 스크립트를 통해 주기적으로 무결성을 확인한다.
*   **User Experience**: 작가가 기술적인 설정보다 '창작'에 집중할 수 있도록, 복잡한 설정 파일은 템플릿을 통해 쉽게 작성하도록 유도한다.
