---
name: extract_creature_tags
description: Analyze a monster description to extract standardized Traits (Origin, Physical, Intellect, etc.) and Skills (Active, Passive). Updates `data/traits/` and `data/ability/`.
---

# 기능: 몬스터 태그 추출 (`extract_creature_tags`)

이 **skills extract_creature_tags**는 입력된 몬스터(생물) 정보를 분석하여 **생물 유형, 핵심 트레잇, 2대 생물 어빌리티(발동/지속)**을 추출하고, 이를 기반으로 데이터베이스를 확장합니다.

## 1. 개요 및 저장 위치

- **목적:** 몬스터 데이터를 '공용 레고 블록'화하여 DB에 저장.
- **저장 위치:** 
    - **트레잇:** `data/traits/` (키워드 누적)
    - **어빌리티:** `report/ability/` (검토 후 `detailed_lists` 이동)

## 2. 작업 지침

### 2-1. 명명 규칙 (규칙 준수)
- 명사형 종결 ("화염 방사" O, "불을 뿜는다" X).
- D&D 용어는 소설에 맞게 변환.
- **범용성:** 인물도 사용할 수 있는 형태로 정의.
- **저작권 회피 (Critical):** 특정 작품의 고유 명사(기술명, 종족명 등)는 피하고, **기능을 설명하는 범용적 명칭**을 사용합니다.
    - `아바다 케다브라` (X) -> `즉사 주문` (O)
    - `포스 라이트닝` (X) -> `전격 방출` (O)

### 2-2. 분석 축 (Classification Axes)

1. **생물 유형/크기:** `data/traits/00_유형.md`, `01_크기.md` 참조.
2. **핵심 트레잇 키워드:**
   - **분류 기준:** `skills create_trait` 및 `data/traits/`의 19종 분류(00~18)를 엄격히 준수합니다.
   - 예: `03_신체`, `04_지성`, `08_약점`, `10_정신` 등.
3. **생물 어빌리티 (Abilities):**
   - **구조:** `manuals/99-1_ability_syntax.md` 준수 (`[권역:원천]-[계통]-[형태]`).
   - **태그:** `manuals/99-2_ability_tags.md` 준수 (태그 필드 필수).
   - **검증:** 사용된 태그가 `manuals/99-2`에 있는지 확인하고, 없으면 신규 태그로 분류.

### 2-3. 확장 (Brainstorming)
- 주된 유형 외에 파생/반대/심화 키워드를 5개 이상 추가 연상.

## 3. 리포트 생성 지침 (Report Generation)

**CRITICAL:** 데이터를 즉시 `data/` 폴더에 저장하지 말고, 리포트(`report/ability/`)를 생성하여 사용자 검토를 받으십시오.

### 출력 양식 (Output Format)

어빌리티와 트레잇은 반드시 다음 **리스트 형식**을 사용해야 합니다 (테이블 형식 금지).

#### [브레인스토밍 (Expansion)]
1. **[트레잇] 이름 (English Name)** (유사: 유사개념)
   - **분류:** 분류코드_분류명
   - **설명:** 트레잇에 대한 상세 설명.
2. **[어빌리티] 이름 (English Name)**
   - **구조:** [도메인:계열] - [라인] - [형태]
   - **태그:** #태그1 #태그2
   - **설명:** 어빌리티에 대한 상세 설명.
   - **대상:** 대상 / **피해:** 피해량 / **상태이상:** 효과

**[신규 태그 보고]**
만약 `manuals/99-2`에 없는 태그(예: `#마그마`)가 사용되었다면, 리포트 하단에 별도 섹션을 만들어 기재하십시오.

```markdown
## 신규 발견 태그 (New Tags Detected)
*   **#마그마**: 화염보다 상위의 열기를 표현하기 위해 사용. `manuals/99-2` 추가 제안.
```
