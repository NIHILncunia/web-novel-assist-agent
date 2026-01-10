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
**⚠️ 중요: 반드시 `prompt/extract_dnd_monsters.md`의 지침을 따라야 합니다.**

1. **목차 확인 및 페이지 찾기:**
   - **⚠️ 중요: 몬스터를 찾을 때 이름으로 검색하지 말고, 반드시 PDF의 목차(Index)를 먼저 확인합니다.**
   - 대부분의 D&D 룰북은 PDF 끝부분에 알파벳순으로 정리된 몬스터 목차가 있습니다.
   - 목차를 확인하여 해당 알파벳 섹션의 몬스터 목록과 페이지 번호를 파악합니다.
   - 예: `uv run python tools/extract_pdf_text.py "library/references/D&D/[Filename]" --start_page [목차_페이지] --end_page [목차_페이지+1]`로 목차를 먼저 확인
   - 목차에서 확인한 페이지 번호를 바탕으로 각 몬스터의 정보를 추출합니다.

2. **PDF 텍스트 추출:**
   - 목차에서 확인한 페이지 번호를 사용하여 `tools/extract_pdf_text.py` 스크립트로 몬스터 정보를 추출합니다.
   - 사용법: `uv run python tools/extract_pdf_text.py "library/references/D&D/[Filename]" --start_page [N] --end_page [M]`
   - **주의:** 이름으로 검색(`--search`)하는 방식은 비효율적이며, PDF가 알파벳순으로 정렬되어 있지 않을 수 있으므로 사용하지 않습니다.

3. **용어 번역:**
   - `library/word_list/dnd_terminology.md` 파일을 참조하여 D&D 용어를 소설에 적합한 한국어로 변환합니다.
   - 게임 메카닉 용어(AC, HP, DC, 주사위 굴림 등)는 서사적 묘사로 변환합니다.
   - 수치 정보는 제외하고 능력의 형태와 효과를 묘사하는 텍스트 위주로 작성합니다.

4. **정보 추출:**
   - 각 몬스터에 대해 다음 정보를 추출합니다:
     - 몬스터 이름 (한글/영문 병기)
     - 몬스터 유형
     - 크기
     - 성향 (약어 금지, 전체 단어로 표기)
     - 도전 등급 (CR)
     - 방어 수준 (서사적 묘사)
     - 생명력 (서사적 묘사)
     - 이동 능력
     - 기술 및 저항
     - 감각
     - 몬스터 설명 (2줄 내외)
     - 세부 능력
     - 특징 (Tag)

5. **양식 준수:**
   - `prompt/extract_dnd_monsters.md`의 "작성 양식 예시"를 반드시 따라 작성합니다.
   - 각 몬스터는 `## [몬스터 이름] (영문명)` 형식으로 시작합니다.
   - 모든 항목은 마크다운 리스트 형식으로 작성합니다.

### Step 4: 결과물 저장
1. **저장 위치:** `library/word_list/creature_dnd/` 폴더
2. **파일 구조:**
   - 항목이 적은 경우: `[Abbreviation].md` (예: `LMoP.md`)
   - 항목이 많은 경우: `[Abbreviation]/` 폴더를 생성하고 알파벳순으로 분할 저장
     - 예: `library/word_list/creature_dnd/MM/MM-A.md`, `MM-B.md`
3. **파일명 형식:** `[Abbreviation]-[Alphabet].md` (분할 시)
4. **파일 형식:** Markdown

### Step 5: 예외 처리
- 해당 룰북에서 몬스터 정보를 발견할 수 없는 경우:
  - 해당 약칭의 파일(`[Abbreviation].md`)을 생성하되, 내용은 "몬스터 정보 없음" 또는 "No creatures found in this reference." 등으로 명시합니다.

### Step 6: 현황 업데이트
1. 작업이 완료되면 `library/references/D&D/index.md` 파일을 다시 읽습니다.
2. 완료한 항목의 Status를 "Done"으로 업데이트합니다.
3. 다음 작업 대상이 있다면 해당 항목의 Status를 "In Progress"로 변경합니다.
   - 진행 단계를 표시하려면 괄호 안에 알파벳을 추가할 수 있습니다 (예: "In Progress (D)")

## 주의 사항

- **목차 우선 확인:** 몬스터를 찾을 때 이름으로 검색하지 말고, 반드시 PDF의 목차(Index)를 먼저 확인하여 페이지 번호를 파악한 후 해당 페이지에서 정보를 추출합니다. 이는 PDF가 알파벳순으로 정렬되어 있지 않을 수 있고, 이름 검색이 비효율적이기 때문입니다.
- **게임 메카닉 배제:** 주사위 굴림, 구체적인 데미지 수치, HP, DC 등 게임 메카닉적 요소는 철저히 배제합니다.
- **서사적 묘사:** 서사적 특징, 생태, 전투 스타일 등 설정적인 측면에 집중합니다.
- **용어 변환:** 모든 용어는 `library/word_list/dnd_terminology.md`의 가이드라인을 따라 소설에 적합한 표현으로 변환합니다.
- **양식 준수:** 반드시 `prompt/extract_dnd_monsters.md`에 명시된 양식을 따라야 합니다.