# D&D 몬스터 목록 추출 (List Only)

이 프롬프트는 D&D 룰북(PDF 또는 Markdown 파일)에서 몬스터와 NPC의 목록만을 빠르게 추출하여 작업의 기초 뼈대를 만드는 것을 목적으로 합니다.

## 1. 개요
- **목표:** 룰북 텍스트에서 몬스터/NPC 이름을 식별하고, 이를 바탕으로 상세 정보 작업을 위한 뼈대 파일(`[Abbreviation].md`)을 생성합니다.
- **대상:** `library/references/D&D/` 경로에 있는 PDF 또는 Markdown 파일.

## 2. 작업 절차

### Step 1: 소스 파일 분석
1. 대상 파일을 읽어 **Appendix** 섹션이나 **Stat Blocks**, **Monsters**, **NPCs** 관련 섹션을 찾습니다.
2. 해당 섹션에 나열된 몬스터 및 주요 NPC의 이름을 추출합니다.

### Step 2: 파일 생성
1. **경로:** `data/word_list/creature_dnd/[Abbreviation].md` (예: `HotDQ.md`)
2. **파일명:** 룰북의 약칭(Abbreviation)을 사용합니다.
3. **내용 양식:**
   - **Frontmatter/Header:**
     ```markdown
     # [Rulebook Name] Monster List

     > **Source:** [Relative Path to Source File]
     > **Status:** In Progress (List Extracted)
     ```
   - **List Section:**
     - `Checklist` 형태가 아닌, 목차(TOC) 스타일의 링크 리스트로 상단에 배치합니다.
     - 형식: `- **[[한글 이름] ([English Name])](#anchor-link)**`
     - 한글 이름은 통용되는 번역을 따르거나, 적절히 음차합니다.
   - **Detail Section:**
     - 각 몬스터별로 `## [English Name] ([한글 이름])` 헤더를 생성합니다.
     - 내용은 `*TBD*` (To Be Determined)로 채웁니다.

### Step 3: 인덱스 업데이트
1. `library/references/dnd_index.md` 파일을 엽니다.
2. 해당 룰북 항목의 **Status** 컬럼을 `List Extracted`로 업데이트합니다.

## 3. 주의사항
- **상세 정보 생략:** 이 단계에서는 스탯 블록(Stat block)이나 상세 설명을 추출하지 않습니다. 오직 이름만 추출하여 리스트를 확보하는 데 집중합니다.
- **번역:** 몬스터 이름의 한글 표기는 기존 `dnd_terminology.md`나 일반적인 D&D 번역 관례를 따릅니다.
- **누락 방지:** 텍스트 내에 숨어있는 몬스터보다는, 명시적으로 리스트업된(Appendix 등) 대상을 우선합니다.
