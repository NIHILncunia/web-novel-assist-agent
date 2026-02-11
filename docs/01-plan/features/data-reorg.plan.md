# Data Reorganization Plan Document

> Version: 1.1.0 | Created: 2026-02-11 | Status: Proposed

## 1. Executive Summary
현재 `data/word_list`에 산재된 데이터 파일들을 `data/keyword` (단순 키워드/참고자료)와 `data/traits` (시스템 트레잇)으로 명확히 분류하여 시스템의 데이터 구조를 체계화합니다.

## 2. Goals and Objectives
- **Goal 1**: `data/word_list` 폴더의 모호한 역할을 제거하고, 모든 데이터를 목적에 맞는 폴더로 이관합니다.
- **Goal 2**: `data/traits` 시스템(00~18번 파일)을 강화하여 에이전트가 캐릭터/몬스터 생성 시 더 풍부한 데이터를 활용하도록 합니다.
- **Goal 3**: `data/keyword`를 확장하여 작가가 브레인스토밍 시 참고할 수 있는 사전류 데이터를 중앙화합니다.

## 3. Scope
### In Scope
- `data/word_list` 내 모든 파일 및 하위 폴더 분석
- `data/traits`의 기존 파일(00~18)과의 병합 전략 수립
- `data/keyword`의 새로운 폴더 구조 설계
- 파일 이동 및 병합 실행 (Do Phase)

### Out of Scope
- `.agent/skills` 코드 수정 (단, 데이터 경로 변경으로 인한 설정 파일 수정은 포함될 수 있음)

## 4. Success Criteria
| Criterion | Metric | Target |
|-----------|--------|--------|
| **File Cleanup** | `data/word_list` 내 잔여 파일 수 | 0 (All moved/archived) |
| **Data Integrity** | 이동 후 데이터 손실 여부 | 0% Loss |
| **Structure Clarity** | 모든 데이터 파일이 `keyword` 또는 `traits`에 속함 | 100% |

## 5. Analysis & Mapping Strategy

### 5.1. Classification Rules
1.  **System Traits (`data/traits`)**: 캐릭터, 몬스터, 사물 등에 "속성"으로 부여되어 시스템적으로 활용되는 데이터. 에이전트가 캐릭터 생성 시 직접 참조하여 JSON/Markdown 프로필을 구성하는 데 사용됩니다.
2.  **Reference Keywords (`data/keyword`)**: 작가가 묘사나 아이데이션을 위해 참고하는 "사전" 데이터. 에이전트가 브레인스토밍이나 문장 생성 시 어휘를 확장하는 용도로 사용합니다.

### 5.2. Detailed File Mapping
`data/word_list`의 모든 파일은 아래 계획에 따라 이동 또는 병합됩니다.

#### A. Traits (Merge to `data/traits`)
| Source File (in `word_list/`) | Destination (in `traits/`) | Action | Rationale |
| :--- | :--- | :--- | :--- |
| `character/캐릭터유형.md` | `00_유형.md` | **Merge** | 아키타입 정의 |
| `character/종족.md` | `02_기원.md` | **Merge** | 종족 목록 |
| `race/종족_*.md` | `02_기원.md` | **Merge (Append)** | 종족별 상세 스펙 |
| `creature/몬스터_*.md` | `02_기원.md` | **Merge (Append)** | 몬스터 종족 데이터 (별도 섹션 구분) |
| `character/젠더.md` | `03_신체.md` | **Merge** | 생물학적/사회적 성별 |
| `character/특징.md` | `03_신체.md` | **Merge** | 외모 및 신체적 특징 (양이 많으므로 선별 병합 필요 할 수 있음) |
| `character/상태이상.md` | `08_약점.md` | **Merge** | 페널티/상태이상 |
| `character/성격.md` | `10_정신.md` | **Merge** | 성격, 기질 |
| `character/감정.md` | `10_정신.md` | **Merge** | 감정 키워드 |
| `character/성향가치관.md` | `10_정신.md` | **Merge** | 가치관 (D&D Alignment 등) |
| `character/속성.md` | `15_속성.md` | **Merge** | 원소/마법 속성 |
| `character/무기.md` | `16_전투.md` | **Merge** | 무기 숙련 및 종류 |
| `character/초능력.md` | `16_전투.md` | **Merge** | 이능력/기술 (전투와 밀접) |
| `character/캐릭터역할.md` | `17_관계.md` | **Merge** | 파티/스토리 내 역할 |
| `character/신분.md` | `18_직업.md` | **Merge** | 사회적 신분 및 직업 |

#### B. Keywords (Move to `data/keyword`)
| Source Path (in `word_list/`) | Destination Path (New Structure) | Description |
| :--- | :--- | :--- |
| `Thesaurus/*.md` | `keyword/writing_aids/thesaurus/` | 유의어 사전 (기존 Thesaurus 유지) |
| `expression/*.md` | `keyword/writing_aids/expression/` | 묘사, 수식어, 문장 표현 |
| `fantasy/*.md` | `keyword/fantasy/` | 판타지 전용 용어 및 설정 |
| `creature_dnd/*.md` | `keyword/fantasy/dnd_bestiary/` | D&D 몬스터 데이터 (참고용) |
| `common/*.md` | `keyword/common/` | 일반 명사 (날씨, 보석, 음식 등) |
| `history.md` | `keyword/common/history_ref.md` | 역사적 사건 참고 자료 |
| `dnd_terminology.md` | `keyword/fantasy/dnd_terms.md` | D&D 용어집 |

## 6. Risks & Mitigation
- **Risk**: `03_신체.md`나 `10_정신.md` 등 타겟 파일이 비대해질 수 있음.
    - **Mitigation**: 병합 시 `##` 헤더를 명확히 구분하여 가독성 확보. 필요 시 하위 문서 분리(`03_신체_세부.md` 등) 고려.
- **Risk**: 기존 코드(Skills)에서 `data/word_list` 경로를 하드코딩으로 참조하고 있을 가능성.
    - **Mitigation**: `grep -r "data/word_list" .` 명령어로 참조 코드 전수 조사 후 패치.

## 7. Migration Steps (Do Phase)
1.  **Preparation**:
    -   `data` 폴더 전체 백업 (e.g., `data_backup_20260211`).
    -   `data/keyword` 및 하위 폴더 트리 생성.
2.  **Execution (Scripted)**:
    -   파이썬 스크립트 작성 (`scripts/migrate_data.py`).
    -   **Move Phase**: 단순 이동 파일들(`keyword` 타겟)을 먼저 처리.
    -   **Merge Phase**: `traits` 타겟 파일들을 읽어서 기존 `traits` 파일의 하단에 `## [Imported] {Filename}` 섹션을 추가하여 Append.
3.  **Refactoring**:
    -   `data/traits` 파일들을 열어 병합된 내용을 수동으로 정리 (중복 헤더 제거, 포맷 통일).
4.  **Code Updates (Crucial)**:
    -   **`GEMINI.md`**: `data/word_list` 참조(약 2곳)를 확인하고 `data/keyword` 등으로 수정.
    -   **`.agent/skills` & `workflows`**: `word_list` 경로를 사용하는 모든 파일 업데이트.
        -   `write_scene/SKILL.md` (Ctx List)
        -   `process_external_data/SKILL.md`
        -   `extract_creature_tags/SKILL.md`
        -   `create_organization/SKILL.md`
        -   `create_nation/SKILL.md`
        -   `create_history/SKILL.md`
        -   `create_character/SKILL.md`
        -   `start-extract_dnd_*.md` (Workflows)
    -   **Tools**: `tools/verify_links.py` 유효성 검사 로직 업데이트.
5.  **Verification**:
    -   `ls -R data/word_list` -> 결과가 없어야 함 (폴더 삭제).
    -   `grep`으로 확인: `grep -r "word_list" .` (Should return 0 matches in active code, except maybe archive/logs).
    -   **Functional Test**: `create_character` 스킬 등 주요 스킬을 실행하여 에러 없이 데이터를 불러오는지 확인.
