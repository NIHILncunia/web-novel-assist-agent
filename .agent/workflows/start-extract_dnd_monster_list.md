---
description: D&D 몬스터 목록 추출 (List Only)
---

# D&D 몬스터 목록 추출 명령 절차 (List Only)

이 명령은 D&D 룰북에서 상세 정보를 제외한 **몬스터와 NPC의 목록(이름)**만을 빠르게 추출하여 뼈대 파일을 생성하는 작업을 자동화합니다.

- **CRITICAL** 아래의 모든 작업은 한글(필요시 영문)로만 진행합니다.

## 작업 순서

### Step 1: 현황 확인
1. `library/references/dnd_index.md` 파일을 읽어 현재 작업 현황을 확인합니다.
2. Status 컬럼에서 "In Progress" 또는 진행 중인 항목을 찾습니다.
3. 가장 마지막(아래쪽)에 있는 진행 중인 항목을 다음 작업 대상으로 선정합니다.
   - 만약 진행 중인 항목이 없다면, Status가 비어있거나 가장 위에 있는 미완료 항목을 선택합니다.

### Step 2: 대상 파일 확인
1. Step 1에서 선정한 항목의 Abbreviation과 Filename을 확인합니다.
2. 해당 파일(PDF 또는 Markdown)이 `library/references/D&D/` 디렉토리에 존재하는지 확인합니다.
3. 약칭(Abbreviation)을 기록합니다.

### Step 3: 추출 작업 수행
**⚠️ 중요: `prompt/extract_dnd_monster_list.md` 파일의 내용을 숙지하고, 해당 문서의 지침을 엄격히 준수하여 작업을 수행합니다.**

1.  **지침서 확인:** `prompt/extract_dnd_monster_list.md` 파일을 엽니다.
2.  **목록 추출:** 지침서의 **'2. 작업 절차'** 섹션을 따라 몬스터/NPC 이름을 식별하고 추출합니다.
    - 상세 스탯이나 설명은 추출하지 않습니다.
    - 목차나 Appendix 리스트를 우선적으로 참고합니다.

### Step 4: 결과물 저장
- 지침서(`prompt/extract_dnd_monster_list.md`)의 **'Step 2: 파일 생성'** 섹션에 정의된 규칙을 따릅니다.
  - **경로:** `data/word_list/creature_dnd/[Abbreviation].md`
  - **양식:** 상단 목차(링크) + 하단 상세 헤더(내용은 *TBD*)

### Step 5: 현황 업데이트
1. 작업이 완료되면 `library/references/dnd_index.md` 파일을 다시 읽습니다.
2. 완료한 항목의 Status를 "**목록 추출됨**"으로 업데이트합니다.
3. 다음 작업 대상이 있다면 해당 항목의 Status를 "**진행 중**"으로 변경합니다.
