---
name: create_trait
description: Extracts and classifies new Traits (트레잇) for characters, monsters, or objects. It analyzes the request to select one of the 14 standard categories (e.g., Physical, Mind, Origin) and appends the data to the corresponding `data/traits` file.
---

# 기능: 트레잇 생성 (`create_trait`)

이 **skills create_trait**는 캐릭터, 몬스터, 사물을 위한 **트레잇 (Trait)**을 생성하는 데 사용됩니다. '트레잇'이란 '무엇을 하는가(Ability)'가 아니라 '무엇인가(Identity)'를 정의하는 선천적 자질, 생리적 특징, 배경 요소를 의미합니다.

## 1. 분류 기준 (Classification Criteria)

데이터가 트레잇인지 어빌리티인지 먼저 판단하십시오:
- **트레잇 (Trait):** 선천적, 생리적, 불변(대체로), 배경 설정. 예: '날개', '강철 피부', '용의 혈통'.
- **어빌리티 (Skill):** 후천적, 기술적, 행동 가능, 소모성. 예: '비행 숙련', '철갑화 기술', '화염구'.

**만약 어빌리티(Ability)라면 **skills create_ability**를 대신 사용하십시오.**

## 2. 카테고리 선정 (14 Categories)

새로운 트레잇에 가장 적합한 **단 하나의 카테고리**를 선택하십시오. 이것이 저장될 파일(`data/traits/XX_Category.md`)을 결정합니다.

| ID | 카테고리 | 정의 | 파일 |
|:---|:---|:---|:---|
| **00** | **유형 (Type)** | 생물학적 종족, 본질적 분류. (예: 언데드, 정령) | `data/traits/00_유형.md` |
| **01** | **크기 (Size)** | 물리적인 체급과 부피. | `data/traits/01_크기.md` |
| **02** | **기원 (Origin)** | 태생적 배경, 출처, 서사적 근원. | `data/traits/02_기원.md` |
| **03** | **신체 (Physical)** | 신체 부위, 구조, 외형. (가장 흔함) | `data/traits/03_신체.md` |
| **04** | **지성 (Intellect)** | 지능 수준, 연산 어빌리티, 통신 수단. | `data/traits/04_지성.md` |
| **05** | **군집 (Social)** | 사회적 구조, 계급, 무리 행동. | `data/traits/05_군집.md` |
| **06** | **이동 (Mobility)** | 선천적 이동 방식 (기술 아님). | `data/traits/06_이동.md` |
| **07** | **감각 (Senses)** | 감각 어빌리티, 인지 체계. | `data/traits/07_감각.md` |
| **08** | **약점 (Weakness)** | 치명적인 결함, 취약점, 공포증. | `data/traits/08_약점.md` |
| **09** | **생활 (Life)** | 일상 습관, 역할, 비전투 활동. | `data/traits/09_생활.md` |
| **10** | **정신 (Mind)** | 성격, 의지, 신념, 트라우마. | `data/traits/10_정신.md` |
| **11** | **지역환경 (Environment)** | 지형, 기후, 시설 특징. | `data/traits/11_지역환경.md` |
| **12** | **외교 (Diplomacy)** | 정치적 입장, 대외 관계 성향. | `data/traits/12_외교.md` |
| **13** | **경영 (Management)** | 행정, 경제, 인프라 운영 어빌리티. | `data/traits/13_경영.md` |

## 3. 실행 단계 (Execution Steps)

1.  **요청 분석:** 사용자가 요청한 트레잇의 핵심 컨셉을 파악합니다.
2.  **카테고리 선택:** 위 표에서 가장 적절한 ID를 선택합니다.
3.  **대상 파일 확인:** 해당 `data/traits/XX_Category.md` 파일을 읽어 포맷과 중복 여부를 확인합니다.
4.  **데이터 포맷팅:** 다음 형식으로 새로운 행을 작성합니다:
    ```markdown
    | **트레잇명 (영문명)** | 분류 | 설명 |
    ```
    - **트레잇명:** 한글 이름.
    - **영문명:** 괄호 안에 영문 번역.
    - **분류:** 더 구체적인 하위 타입 (예: '자연적', '인공적', '저주').
    - **설명:** 트레잇의 효과나 서사적 의미에 대한 간결한 설명.
5.  **데이터 추가:** `multi_replace_file_content` (혹은 `replace_file_content`)를 사용하여 대상 파일의 테이블에 행을 추가합니다.
6.  **결과 보고:** 생성된 트레잇과 저장 위치를 사용자에게 알립니다.

## 4. 출력 예시 (Example Output)

**입력:** "용암으로 만들어진 몬스터 트레잇 만들어줘."

**수행:**
1.  **분석:** '용암으로 만들어짐' -> 신체 구성 -> **03. 신체**.
2.  **대상:** `data/traits/03_신체.md`.
3.  **데이터:**
    - 이름: **용암 신체 (Lava Body)**
    - 분류: 신체
    - 설명: 전신이 끓어오르는 용암으로 이루어져 있어 닿는 것을 불태우며 물리 공격을 무효화함.
4.  **편집:** `| **용암 신체 (Lava Body)** | 신체 | 전신이 끓어오르는 용암으로 이루어져 있어 닿는 것을 불태우며 물리 공격을 무효화함. |` 추가.
