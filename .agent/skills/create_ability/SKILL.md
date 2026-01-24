---
name: create_ability
description: An interactive skill that guides the user through creating Active (발동) or Passive (지속) abilities. It enforces the Modular Skill Structure `[Domain:Source]-[Lineage]-[Form]` defined in `manuals/99-1_ability_syntax.md` and saves the result to `data/ability/발동.md` or `data/ability/지속.md`.
---

# 기능: 어빌리티 생성 (`create_ability`)

이 어빌리티는 캐릭터나 몬스터를 위한 **어빌리티 (Ability = Skill)**을 생성하는 데 사용됩니다. **발동 어빌리티(Active)**과 **지속 어빌리티(Passive)**을 모두 포함하며, 프로젝트 표준인 **모듈형 어빌리티 구조**를 강제합니다.

## 1. 어빌리티 유형 결정 (Determine Ability Type)

- **발동 (Active):** 의지, 행동, 자원 소모(마나/기력), 쿨타임이 동반되는 기술.
    - **대상 파일:** `data/ability/발동.md`
- **지속 (Passive):** 상시 효과, 자동 반응, 상태, 별도의 소모값이 없는 기술.
    - **대상 파일:** `data/ability/지속.md`

> **[필수] 작명 및 생성 규칙:**
> 모든 어빌리티 생성 시 **`manuals/97_trait_and_naming_rules.md`**를 반드시 준수하십시오.
> *   **모듈화 원칙:** '화염구' (O) vs '강력한 지옥의 화염구' (X - 수식어 지양)
> *   **이중 수식 금지:** 이름에 불필요한 형용사를 붙이지 말고, 설명(Description) 필드에 상세히 서술하십시오.

> **[참고] 트레잇(Trait) vs 어빌리티(Skill/Ability) 구분 기준:**
> *   **트레잇:** 타고난 것, 생물학적 특징, 의지 없이도 존재하는 상태. (예: 야간 시야, 비늘 피부)
> *   **어빌리티:** 후천적으로 습득하거나, 의지/자원을 소모하여 '사용'하는 기술. (예: 정밀 사격, 마나 실드)
> *   *지속 어빌리티(Passive)은 '트레잇'과 헷갈릴 수 있으나, 시스템적 효과나 조건부 발동이 명확한 경우 어빌리티로 분류합니다.*

## 2. 속성 정의 (Define Attributes)

모든 어빌리티는 다음 컬럼을 포함해야 합니다.
**중요 (CRITICAL):** **구조 (Structure)** 컬럼은 반드시 `[권역:원천] - [계통] - [형태]` 문법을 엄격히 따라야 합니다.

| 컬럼 | 설명 |
|:---|:---|
| **이름 (Name)** | 어빌리티의 이름 (영문명 병기 권장). 예: "화염구 (Fireball)" |
| **구조 (Structure)** | **[권역:원천] - [계통] - [형태]** (3번 항목 참조) |
| **대상 (Target)** | 어빌리티의 영향 범위. **4번 항목 참조.** |
| **피해 유형 (Damage Type)** | 피해를 주는 방식. **4번 항목 참조.** |
| **상태 이상 유형 (Status Effect)** | 부여하는 버프/디버프. **4번 항목 참조.** |
| **설명 (Description)** | 어빌리티의 효과에 대한 서사적 묘사. |

## 3. 모듈형 구조 문법 (Modular Structure Syntax)

모든 어빌리티는 **`[권역:원천] - [계통] - [형태]`** 라는 3단계 구조로 정의됩니다.
상세한 정의는 **`resources/99-1_ability_syntax.md`**를 참고하십시오.

> **구조 작성 팁:**
> 1.  **권역(Domain):** 힘의 뿌리는 무엇인가? (마법/물리/정신/특수/생산)
> 2.  **원천(Source):** 구체적인 재료는 무엇인가? (화염, 신체, 시간 등)
> 3.  **계통(Lineage):** 어떻게 작동하는가? (방출, 구현, 제어 등)
> 4.  **형태(Form):** 최종 모양은 무엇인가? (구체, 광선, 무기 등)

**형식 예시:** `[마법:화염] - [방출계] - [구체]`

### 권역별 유효 계통 및 형태

아래 목록에서 원하는 **계통**과 **형태**를 찾아 조합하십시오. 원천(Source)은 예시에 없더라도 자유롭게 지정할 수 있습니다.

### 권역별 유효 계통 및 형태

#### A. 마법 권역 ([마법:...])
- **[방출계 (Emission)]**: 구체(Orb), 광선(Beam), 파동(Wave), 연사(Barrage)
- **[구현계 (Materialization)]**: 무기(Weapon), 장벽(Barrier), 사슬(Chain), 형상화(Figuration)
- **[강화계 (Enhancement)]**: 오라(Aura), 부분 오라(Part-Aura), 동기화(Sync), 부분 동기화(Partial Sync)
- **[제어계 (Control)]**: 지대(Zone), 함정(Trap), 원격 조작(Telekinesis), 영역(Territory)
- **[계약계 (Contract)]**: 가호(Blessing), 대여(Borrow), 현신(Incarnation), 강림(Descent)
- **[치유계 (Restoration)]**: 회복(Heal), 정화(Purify), 소생(Resurrect), 재구축(Reconstruct)

#### B. 물리 권역 ([물리:...])
- **[타격계 (Striking)]**: 일점(Point), 절단(Slash), 파쇄(Crush), 연격(Barrage), 투척(Throw)
- **[신법계 (Maneuver)]**: 돌진(Charge), 도약(Leap), 회피(Evasion), 잠입(Stealth), 보법(Step)
- **[육체계 (Physiology)]**: 경화(Harden), 재생(Regen), 과부하(Overload), 변형(Morph), 호흡(Breath)
- **[기교계 (Technique)]**: 제압(Subdue), 반격(Counter), 무장 해제(Disarm), 간파(Insight)

#### C. 정신 권역 ([정신:...])
- **[감지계 (Sensory)]**: 탐색(Scan), 추적(Track), 통찰(Analyze), 예지(Foresight)
- **[간섭계 (Influence)]**: 주입(Inject), 조작(Manipulate), 소거(Erase), 동조(Sync)
- **[강화계 (Mentality)]**: 고양(Booster), 평정(Calm), 가속(Accel)
- **[구현계 (Manifestation)]**: 위압(Aura), 충격(Blast), 형상(Construct)

#### D. 특수 권역 ([특수:...])
- **[소환계 (Summoning)]**: 호출(Call), 사역(Command), 빙의(Possess), 송환(Banish)
- **[인과계 (Causality)]**: 가속/감속(Time), 정지(Stop), 역행(Rewind), 확정(Fate)
- **[공간계 (Spatial)]**: 이동(Teleport), 절단(Sever), 격리(Isolate), 왜곡(Distort), 영역(Territory)
- **[규칙계 (Rule/Meta)]**: 부여(Grant), 금지(Ban), 강제(Force), 대가(Exchange)
- **[흡수계 (Absorption)]**: 강탈(Steal), 복제(Copy), 포식(Devour), 반사(Reflect)

#### E. 생산 권역 ([생산:...])
- **[가공계 (Crafting)]**: 제련(Smelt), 단조(Forge), 세공(Cut), 조리(Cook)
- **[연금계 (Alchemy)]**: 조제(Brew), 변환(Transmute), 분해(Dismantle), 합성(Synthesize)
- **[부여계 (Enchant)]**: 부여(Imbue), 새김(Inscribe), 각성(Awaken), 승화(Sublimation)

## 4. 허용된 값 목록 (Allowed Values)

- **Target (대상):** `자신`, `단일`, `다수`, `범위`, `탈것`, `해당 없음`
- **Damage Type (피해 유형):** `해당 없음`, `물리`, `참격`, `관통`, `타격`, `화염`, `냉기`, `전기`, `산성`, `독`, `광휘`, `폭풍`, `수류`, `플라즈마`, `정신`, `사령`, `저주`, `어둠`, `폭발`, `방사능`, `역장`, `공허`, `고정`
- **Status Effect (상태 이상):** `해당 없음`, `강화`, `도발`, `넘어짐`, `출혈`, `심층 창상`, `신체 훼손`, `방어구 관통`, `기절`, `골절`, `넉백`, `침묵`, `화상`, `공포`, `부식`, `동상`, `동결`, `둔화`, `마비`, `감전`, `중독`, `실명`, `혼란`, `표적`, `젖음`, `질식`, `수면`, `광분`, `부패`, `허약`, `오염`, `변이`, `속박`, `속박됨`, `소멸`, `처형`

## 5. 실행 단계 (Execution Steps)

1.  **요청 분석:** 사용자가 원하는 것이 발동 어빌리티인지 지속 어빌리티인지 파악합니다.
2.  **구조 결정:** 어빌리티 컨셉에 가장 적합한 권역, 계통, 형태를 선택합니다.
    - 예: "화염구" -> 마법 권역 -> 방출계 -> 구체 형태.
    - 구조 문자열: `[마법:화염] - [방출계] - [구체]`
3.  **데이터 초안 작성:** 스키마에 맞춰 데이터 행을 작성합니다.
4.  **대상 파일 확인:** `data/ability/발동.md` 또는 `data/ability/지속.md`를 읽어 중복을 확인합니다.
5.  **데이터 추가:** 대상 파일의 테이블에 새로운 행을 추가합니다.
6.  **결과 보고:** 생성된 어빌리티를 사용자에게 알립니다.

## 6. 출력 예시 (Example Output)

**입력:** "풀밭에 서 있으면 체력을 회복하는 패시브 어빌리티 만들어줘."

**수행:**
1.  **유형:** 지속 (상태/조건) -> `data/ability/지속.md`
2.  **구조 결정:**
    - 권역: 마법 (자연의 힘)
    - 계통: 계약계 (자연의 가호)
    - 형태: 가호 (Blessing)
    - **구조:** `[마법:자연] - [계약계] - [가호]`
3.  **초안:**
    - 이름: **자연 치유 (Natural Healing)**
    - 대상: `자신`
    - 피해 유형: `해당 없음`
    - 상태 이상: `강화`
    - 설명: 숲이나 풀밭 위에 서 있을 때 자연의 기운을 받아 체력을 지속적으로 회복한다.
4.  **편집:** `| **자연 치유 (Natural Healing)** | [마법:자연] - [계약계] - [가호] | 자신 | 해당 없음 | 강화 | 숲이나 풀밭 위에 서 있을 때 자연의 기운을 받아 체력을 지속적으로 회복한다. |` 추가.
