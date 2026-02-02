# Coding Rules & Guidelines (Trait DB)

본 문서는 `novel-assist-agent`의 트레잇 데이터베이스를 관리하고 확장하기 위한 규칙을 정의합니다.

## 1. Architectural Principles
*   **Single Source of Truth (SSOT)**: 모든 트레잇은 `data/traits` 디렉토리 내에 유일하게 존재해야 하며, 파일 간 중복된 키워드를 허용하지 않는다.
*   **Modular Expansion (모듈식 확장)**: 카테고리는 독립적인 모듈로 취급하며, 새로운 개념(장르 등)이 추가될 때 기존 파일을 수정하기보다 새로운 번호의 파일을 생성하는 것을 원칙으로 한다.
*   **Human-Centric Design**: 데이터는 기계가 읽기 쉬워야 하지만, 최종 소비자인 '작가'가 영감을 얻을 수 있도록 문학적이고 풍부한 설명을 포함해야 한다.

## 2. Directory & File Structure
트레잇 데이터는 `data/traits/` 디렉토리에 평면적(Flat) 구조로 저장하되, 파일명 앞의 숫자로 정렬 순서를 제어한다.

```
data/traits/
├── 00_유형.md            # Entity Type (종족, 기원) - *변경 최소화*
├── 01_크기.md            # Size Class - *변경 최소화*
├── 02_기원.md            # Origin & Background
├── 03_신체.md            # Physical Traits
├── 04_지식_지혜.md       # Knowledge & Intellect
├── ...
├── 10_정신.md            # Mind & Personality
├── 11_지역환경.md        # Environment & World
├── 15_속성.md            # Elemental Attributes - *변경 최소화*
├── 16_전투.md            # Combat Style & Tactics
└── 99_미분류.md          # Uncategorized (임시 저장소)
```

## 3. Naming Conventions (Strict)

### 3.1. File Naming
*   Format: `NN_CategoryName.md`
*   `NN`: 2자리 숫자 (00~99). 논리적 흐름(기원 -> 신체 -> 정신 -> 사회) 순으로 배정한다.
*   `CategoryName`: 한글 사용을 원칙으로 하며, 띄어쓰기 대신 언더바(`_`)를 사용한다.

### 3.2. Trait Keyword Naming
*   **트레잇 이름(Key)**: `**한글 키워드**` 형식을 기본으로 한다.
*   **영문 병기**: 국제적 통용어구나 뉘앙스 차이가 큰 경우 `(English)`를 병기한다. (예: `**광전사 (Berserker)**`)
*   **중복 불가**: 전체 파일을 통틀어 동일한 키워드는 단 하나만 존재해야 한다.

### 3.3. Description Style
*   **Tone**: 객관적이면서도 작가에게 영감을 줄 수 있는 묘사적 어조.
*   **Ending**: 반드시 완결된 문장으로 끝맺는다. (`~함.`, `~다.`)
*   **Length**: 1문장 이상, 3문장 이하를 권장한다.

## 4. Classification Standards (분류 기준)

가장 혼동하기 쉬운 카테고리 간의 경계를 명확히 정의한다.

### 4.1. 정신(10) vs 관계(XX)
*   **정신(Mind)**:
    *   주체: **나(Self)**
    *   기준: 혼자 무인도에 있어도 성립하는 성향.
    *   예시: 우울증, 낙천주의, 강박증, 다중인격.
*   **관계(Relationships)** (현 10_정신 내 포함됨 -> 분리 권장):
    *   주체: **나와 너(Interaction)**
    *   기준: 타인이 없으면 성립하지 않는 태도나 상호작용.
    *   예시: 짝사랑, 가스라이팅, 계약 연애, 라이벌.

> **Rule:** 모호하면 **'발원지'**를 확인하라. 내면에서 솟아나면 정신, 외부 자극에 대한 반응이면 관계다.

### 4.2. 신체(03) vs 전투(16)
*   **신체(Physical)**:
    *   기준: **상시(Passive)** 존재하는 생물학적 특징.
    *   예시: 4개의 팔, 야간 시야, 강철 피부, 독 주머니.
*   **전투(Combat)**:
    *   기준: 실전 상황에서 발휘되는 **전술적(Tactical)** 기질이나 습관.
    *   예시: 저격 본능, 광폭화, 무기 교체, 킬러 본능.

### 4.3. 트레잇(Trait) vs 어빌리티(Ability)
*   **트레잇**: 태생적이거나 고정된 성질. 코스트(MP)가 들지 않는다. "그 존재 자체".
*   **어빌리티**: 획득하거나 마스터해야 하는 기술. 코스트가 들거나 쿨타임이 있다. "그 존재가 하는 것".

## 5. Quality Assurance
*   **Linting**: 정기적으로 스크립트를 돌려 깨진 테이블이나 중복 키워드를 검출한다.
*   **Review**: 모호한 트레잇은 `99_미분류.md`에 우선 저장하고, 마스터의 리뷰를 거쳐 적절한 곳으로 이동한다.
