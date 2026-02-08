---
name: create_ability
description: Interactive skill to create Active/Passive abilities. Generates 5 base abilities + 10 brainstorming variations. Enforces strict `[Domain:Source]-[Lineage]-[Form]` syntax (manuals/99-1) and saves to `detailed_lists`.
---

# 기능: 어빌리티 생성 (`create_ability`)

이 스킬은 캐릭터나 몬스터를 위한 **어빌리티(Ability)**를 생성하고 데이터를 확장하는 **대규모 창작 도구**입니다.
사용자의 요청을 받아 **기본 5종**을 생성하고, 이를 분석하여 **추가 10종**을 브레인스토밍한 뒤, **엄격한 규칙 검증**을 거쳐 저장합니다.

## 1. 핵심 규칙 (Core Rules)

1.  **모듈형 구조 준수 (Critical):** 모든 어빌리티는 반드시 `[권역:원천] - [계통] - [형태]` 구조를 따라야 합니다.
    *   참조: `manuals/99-1_ability_syntax.md` (새로운 형태 창조 금지, 정의된 형태만 사용)
    *   참조: `manuals/99-2_ability_tags.md` (태그 프로토콜 준수, 태그 필드 필수)
2.  **선-리포트 후-저장 (Report First):** 생성된 어빌리티를 즉시 `data/` 폴더에 저장하지 않습니다.
    *   반드시 **리포트(`report/ability/`)를 우선 생성**하고, 사용자의 검토 승인을 거쳐야 합니다.
    *   승인 후 저장되는 경로: `data/ability/detailed_lists/[권역]권역/[권역]_[계통]계_[형태].md`
3.  **대량 생성 프로토콜:** 1회 실행 시 **총 15개** (기본 5 + 확장 10)의 데이터를 다룹니다.

## 2. 실행 프로세스 (Execution Process)

### 단계 1: 어빌리티 생성 및 브레인스토밍 (Generation & Brainstorming)
*   사용자의 요청(컨셉, 키워드)을 분석하여 **기본 5종**을 제안합니다.
*   분석 결과를 바탕으로 **10개의 추가 어빌리티**를 심화 브레인스토밍합니다. (변주, 상반, 연계 등)
*   총 **15개**의 어빌리티 목록을 확보합니다.

### 단계 2: 자가 점검 및 검증 (Self-Verification)
*   생성된 어빌리티가 **유효한 계통/형태**인지 검증합니다.
    *   `manuals/99-1`에 정의된 형태 준수 여부
    *   권역과 계통의 일치 여부
    *   데이터 스키마 준수 여부

### 단계 3: 리포트 생성 (Report Generation) - **CRITICAL**
*   **절대 data 폴더에 바로 저장하지 마십시오.**
*   검증된 어빌리티 목록을 `report/ability/` 폴더 내에 마크다운 파일로 생성합니다.
    *   파일명 예시: `report/ability/[YYYYMMDD]_[요청주제]_생성리포트.md`
*   리포트에는 다음 내용이 포함되어야 합니다:
    *   생성된 어빌리티 목록 (테이블 형식)
    *   적용 대상 파일 경로 (`data/ability/detailed_lists/...`)
    *   특이 사항 및 검토 요청

### 단계 4: 사용자 검토 및 반영 (Review & Apply)
*   사용자에게 리포트 경로를 알리고 검토를 요청합니다.
*   **사용자의 승인이 떨어진 후**, `/apply-report-data` 커맨드나 수동 작업을 통해 `data` 폴더의 실질적인 파일에 내용을 반영합니다.

## 3. 권역별 유효 계통 및 형태 (Valid Lineages & Forms)

아래의 목록에 정의된 **형태(Form)**만을 사용하십시오. 새로운 형태를 임의로 창조해서는 안 됩니다.

#### A. 마법 권역 ([마법:...])
*   **[방출계]**: 구체(Orb), 광선(Beam), 파동(Wave), 연사(Barrage)
*   **[구현계]**: 무기(Weapon), 장벽(Barrier), 사슬(Chain), 형상화(Figuration)
*   **[강화계]**: 오라(Aura), 부분 오라(Part-Aura), 동기화(Sync), 부분 동기화(Partial Sync)
*   **[제어계]**: 지대(Zone), 함정(Trap), 원격 조작(Telekinesis), 영역(Territory), 토템(Totem)
*   **[계약계]**: 가호(Blessing), 대여(Borrow), 현신(Incarnation), 강림(Descent)
*   **[치유계]**: 회복(Heal), 정화(Purify), 소생(Resurrect), 재구축(Reconstruct)

#### B. 물리 권역 ([물리:...])
*   **[타격계]**: 일점(Point), 절단(Slash), 파쇄(Crush), 연격(Barrage)
*   **[사격계]**: 조준(Aim), 곡사(Arc), 관통(Pierce), 산탄(Scatter)
*   **[신법계]**: 돌진(Charge), 도약(Leap), 회피(Evasion), 잠입(Stealth), 보법(Step)
*   **[육체계]**: 경화(Harden), 재생(Regen), 과부하(Overload), 변형(Morph), 호흡(Breath)
*   **[기교계]**: 제압(Subdue), 반격(Counter), 무장 해제(Disarm), 간파(Insight), 공연(Performance)

#### C. 정신 권역 ([정신:...])
*   **[감지계]**: 탐색(Scan), 추적(Track), 통찰(Analyze), 예지(Foresight)
*   **[간섭계]**: 주입(Inject), 조작(Manipulate), 소거(Erase), 동조(Sync), 매료(Charm)
*   **[강화계]**: 고양(Booster), 평정(Calm), 가속(Accel)
*   **[구현계]**: 위압(Aura), 충격(Blast), 형상(Construct)

#### D. 특수 권역 ([특수:...])
*   **[소환계]**: 호출(Call), 사역(Command), 빙의(Possess), 송환(Banish)
*   **[약화계]**: 중독(Poison), 쇠약(Weaken), 불운(Jinx), 낙인(Brand)
*   **[인과계]**: 가속/감속(Time), 정지(Stop), 역행(Rewind), 확정(Fate)
*   **[공간계]**: 이동(Teleport), 절단(Sever), 격리(Isolate), 왜곡(Distort)
*   **[규칙계]**: 부여(Grant), 금지(Ban), 강제(Force), 대가(Exchange)
*   **[흡수계]**: 강탈(Steal), 복제(Copy), 포식(Devour), 반사(Reflect)

#### E. 전술 권역 ([전술:...])
*   **[지휘계]**: 호령(Shout), 지정(Mark), 진형(Formation)
*   **[교섭계]**: 설득(Persuasion), 기만(Deception), 선동(Agitation), 위압(Intimidate)

#### F. 생산 권역 ([생산:...])
*   **[채집계]**: 식별(Identification), 추출(Extraction), 수확(Harvesting)
*   **[가공계]**: 정제(Refining), 변환(Transmutation), 분해(Dismantling)
*   **[제작계]**: 조형(Forging), 합성(Synthesis), 결합(Assembly)
*   **[조성계]**: 구축(Construction), 배치(Placement), 양육(Husbandry)

## 4. 허용된 값 목록 (Allowed Values)

어빌리티 생성 시, `manuals/99-2_ability_tags.md`에 정의된 **태그 프로토콜**을 따르십시오.
새로운 개념이 필요하다면 **오픈 태깅 규칙**에 따라 자유롭게 태그를 확장할 수 있습니다.

*   **참조 파일:** `manuals/99-2_ability_tags.md` (무기, 속성, 상태이상, 일반 태그 전체 목록)

## 5. 데이터 스키마 (Data Schema)

### A. [Draft/Report] 보고 및 제안용 스키마
사용자와 대화하거나 리포트를 생성할 때에는 **전체 구조**를 명확히 보여주기 위해 아래 형식을 사용합니다.

```markdown
| 이름 (Name) | 구조 (Structure) | 대상 (Target) | 피해 (Dmg.Type) | 상태이상 (Effect) | 태그 (Tags) | 설명 (Description) |
|:---|:---|:---|:---|:---|:---|:---|
| (예시) 파이어볼 | [마법:화염] - [방출] - [구체] | 범위 | 화염 | 화상 | #화염 #폭발 #1서클 | 지정한 위치에 화염 구체를 던져 폭발시킨다. |
```

### B. [File Storage] 데이터 파일 저장용 스키마
`data/ability/detailed_lists/` 내의 파일에 저장할 때에는 **이미 파일명과 폴더구조가 권역/계통/형태를 설명하므로**, 구조(Structure) 컬럼 대신 **원천(Source)** 컬럼을 사용해야 합니다.

*   **변환 규칙:** `[권역:원천] - [계통] - [형태]`  ->  `원천`만 추출하여 기록
*   **예시:** `[마법:화염] - [방출] - [구체]` -> `화염` (파일명이 `마법_방출계_구체.md` 이므로)

```markdown
| 이름 (Name) | 원천 (Source) | 대상 (Target) | 피해 (Dmg.Type) | 상태이상 (Effect) | 태그 (Tags) | 설명 (Description) |
|:---|:---:|:---:|:---:|:---:|:---|:---|
| 파이어볼 | 화염 | 범위 | 화염 | 화상 | #화염 #폭발 #1서클 | 지정한 위치에 화염 구체를 던져 폭발시킨다. |
```