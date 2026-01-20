---
description: D&D 몬스터 정보 추출
---

# D&D 몬스터 정보 추출 명령 절차

이 명령은 D&D 룰북에서 몬스터 정보를 추출하는 작업을 자동화합니다.

- **CRITICAL** 아래의 모든 작업은 한글(필요시 영문)로만 진행합니다.

## 작업 순서

### Step 1: 현황 확인
1. `library/references/D&D/index.md` 파일을 읽어 현재 작업 현황을 확인합니다.
2. Status 컬럼에서 "In Progress" 또는 진행 중인 항목을 찾습니다.
3. 가장 마지막(아래쪽)에 있는 진행 중인 항목을 다음 작업 대상으로 선정합니다.
   - 만약 진행 중인 항목이 없다면, Status가 비어있거나 가장 위에 있는 미완료 항목을 선택합니다.

### Step 2: 대상 파일 확인
1. Step 1에서 선정한 항목의 Abbreviation과 Filename을 확인합니다.
2. 해당 PDF 파일이 `library/references/D&D/` 디렉토리에 존재하는지 확인합니다.
3. 약칭(Abbreviation)을 기록합니다.

### Step 3: 추출 작업 수행
**⚠️ 중요: `prompt/extract_dnd_monsters.md` 파일의 내용을 숙지하고, 해당 문서의 지침을 엄격히 준수하여 작업을 수행합니다.**

1.  **지침서 확인:** `prompt/extract_dnd_monsters.md` 파일을 엽니다.
2.  **목차 확인 및 텍스트 추출:** 지침서의 **'3. 작업 절차'** 섹션을 따릅니다.
3.  **정보 추출 및 변환:** 지침서의 **'2. 추출 대상 정보'** 섹션 및 `data/word_list/dnd_terminology.md`를 따릅니다.

### Step 4: 결과물 저장
- 지침서(`prompt/extract_dnd_monsters.md`)의 **'4. 결과물 저장'** 섹션에 정의된 규칙(경로, 파일명, 형식)을 따릅니다.

### Step 5: 예외 처리
- 지침서의 **'5. 예외 처리'** 항목을 따릅니다.

### Step 6: 현황 업데이트
1. 작업이 완료되면 `library/references/D&D/index.md` 파일을 다시 읽습니다.
2. 완료한 항목의 Status를 "완료"로 업데이트합니다.
3. 다음 작업 대상이 있다면 해당 항목의 Status를 "진행 중"으로 변경합니다.
   - 진행 단계를 표시하려면 괄호 안에 알파벳을 추가할 수 있습니다 (예: "진행 중 (D)")
