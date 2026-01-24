# TODO: NOVEL 프로젝트 개선 작업 목록 (2026.01)

## ✍️ 콘텐츠 및 데이터베이스 확장

### 1. 특성 및 능력 데이터베이스 대규모 확장 (Fate Series)
- **목표:** Fate 시리즈의 개성 강한 캐릭터(서번트)들을 분석하여, 범용적으로 사용할 수 있는 고품질의 특성(Trait)과 능력(Skill) 데이터를 대량 확보합니다.
- **작업 내용:**
    - [ ] **Fate/Zero 캐릭터 분석:** 7명의 서번트(세이버, 아처, 랜서, 라이더, 캐스터, 어쌔신, 버서커) 핵심 컨셉 추출
    - [ ] **Fate/Stay Night 캐릭터 분석:** 5차 성배전쟁의 주요 서번트 및 마스터 분석
    - [ ] **브레인스토밍:** 추출된 키워드에서 파생되는 연관/반전 특성 및 능력 생성 (`prompt/02_refinement/brainstorm_from_keyword.md` 활용)
    - [ ] **데이터화:** `data/traits/` 및 `data/ability/`에 정제된 데이터 입력

- **진행 현황 (2026-01-21 기준 / `archive/report/concept_analyze/character` Fate만)**
    - **완료 (데이터 적용/아카이브됨)**
        - **Fate/Zero**
            - 서번트: 라이더(이스칸달/정복왕) (`fate_zero_iskandar.md`)
        - **Fate/Stay Night**
            - 서번트: 세이버(알트리아 펜드래곤) (`fate_stay_night_saber.md`)
            - 서번트: 아처(에미야) (`fate_stay_night_archer.md`)
            - 서번트: 버서커(헤라클레스) (`fate_stay_night_berserker.md`)
            - 서번트: 라이더(메두사) (`fate_stay_night_rider_medusa.md`)
            - 마스터: 에미야 시로 (`fate_stay_night_emiya_shirou.md`)
            - 마스터: 토오사카 린 (`fate_stay_night_tohsaka_rin.md`)
            - 마스터: 마토 사쿠라 (`fate_stay_night_matou_sakura.md`)
            - 마스터: 이리야스필 폰 아인츠베른 (`fate_stay_night_illyasviel_von_einzbern.md`)

    - **앞으로 분석할 대상 (체크리스트)**
        - **Fate/Stay Night (마스터 8인 / 서번트 9인)**
            - *(왜 8/9인가?)* 5차 성배전쟁은 비정규로 **바젯(원래 마스터)** + **키레이(탈취 마스터)**가 함께 카운트되고, 서번트는 **정규 7기 + 어쌔신 2기(사사키/진 어쌔신) + 길가메시(4차 잔존)**까지 포함해 9기로 집계되는 경우가 있음.
            - **마스터 8인**
                - [x] 에미야 시로 (Saber 마스터)
                - [x] 토오사카 린 (Archer 마스터)
                - [x] 마토 사쿠라 (Rider의 진 마스터)
                - [x] 마토 신지 (Rider의 명목/대리 마스터)
                - [x] 이리야스필 폰 아인츠베른 (Berserker 마스터)
                - [x] 쿠즈키 소이치로 (Caster 마스터)
                - [x] 마토 조켄 (진 어쌔신 마스터 / Heaven's Feel)
                - [x] 바젯 프라가 맥레미츠 (Lancer의 원래 마스터)
                - [x] 코토미네 키레이 (Lancer 탈취 / 길가메시 잔존 계약)
            - **서번트 9인**
                - [x] 세이버: 알트리아 펜드래곤 (Artoria Pendragon)
                - [x] 아처: 에미야 (EMIYA)
                - [x] 랜서: 쿠 훌린 (Cú Chulainn)
                - [x] 라이더: 메두사 (Medusa)
                - [x] 캐스터: 메데이아 (Medea)
                - [x] 어쌔신(가짜): 사사키 코지로 (Sasaki Kojirou)
                - [x] 어쌔신(진): 저주의 팔의 하산 (Hassan of the Cursed Arm)
                - [x] 버서커: 헤라클레스 (Heracles)
                - [x] 길가메시 (Gilgamesh) *(4차 잔존/개입)*

        - **Fate/Zero (마스터 7인 / 서번트 7인)**
            - **마스터 7인**
                - [ ] 에미야 키리츠구 (Saber 마스터)
                - [ ] 토오사카 토키오미 (Archer 마스터)
                - [ ] 케이네스 엘멜로이 아치볼드 (Lancer 마스터)
                - [ ] 웨이버 벨벳 (Rider 마스터)
                - [ ] 마토 카리야 (Berserker 마스터)
                - [ ] 우류 류노스케 (Caster 마스터)
                - [ ] 코토미네 키레이 (Assassin 마스터)
            - **서번트 7인**
                - [ ] 세이버: 알트리아 펜드래곤 (Artoria Pendragon)
                - [ ] 아처: 길가메시 (Gilgamesh)
                - [ ] 랜서: 디어뮈드 우아 두브네 (Diarmuid Ua Duibhne)
                - [x] 라이더: 이스칸달 (Iskandar)
                - [ ] 캐스터: 질 드 레 (Gilles de Rais)
                - [ ] 어쌔신: 하산(백인의 하산) (Hassan of the Hundred Faces)
                - [ ] 버서커: 랜슬롯 (Lancelot)

### 2. 어휘 및 표현력 데이터 채우기 (New)
- **목표:** 구조만 잡혀있는 표현력 DB(`data/word_list/expression/`)에 실제 데이터를 채워 넣습니다.
- **작업 내용:**
    - [ ] `01_관용구.md` 데이터 추가
    - [ ] `02_동사.md` ~ `06_어미.md` 데이터 추가
    - [ ] `07_상황_묘사_수식어.md` 지속적 보강 (현재 120KB 확보)

---

## ⚙️ 시스템 및 워크플로우 개선

### 3. 데이터 관리 시스템 고도화
- **목표:** 데이터 관리의 효율성과 안정성을 높이고, 장기적인 확장성을 확보합니다.
- **작업 내용:**
    - [ ] **데이터 관리 시스템 변경:** `data/아이템.md`, `data/스킬.md` 등의 마크다운 테이블을 CSV 또는 SQLite DB로 전환하여 데이터 추가/수정/삭제 작업을 안정화합니다.
    - [ ] **로그 시스템 변경:** `00_conversation_log.md` 파일을 데이터베이스 테이블로 전환하여, 장기 프로젝트의 컨텍스트 관리 효율성을 높이고 성능 저하를 방지합니다.

### 4. 집필 프로세스 자동화
- **목표:** `07_chapter_plan.md`를 동적인 집필 현황판으로 활용하여 챕터별 진행 상태를 시각적으로 관리합니다.
- **작업 내용:**
    - [ ] AI 에이전트가 특정 챕터의 집필 시작/완료 명령을 인식하고, 챕터 상태(`계획`, `집필 중`, `완료`)를 자동으로 업데이트하는 로직 구현.

### 5. 데이터 정제 및 표준화 (New)
- **목표:** 기존 데이터의 일관성을 확보하고 허용되지 않은 값을 정제합니다.
- **작업 내용:**
    - [ ] **어빌리티 데이터 대폭 수정 (`data/ability/`):** 2026-01-23 업데이트된 허용 값 목록(물리, 폭발, 어둠, 저주, 강화, 도발, 넘어짐, 속박됨 등)을 기준으로 기존의 부적절한 피해 유형 및 상태 이상 값을 전수 조사하여 수정.

### 6. 용어 표준화 작업 (스킬 -> 어빌리티) (진행 중)
- **목표:** 프로젝트 내에서 혼용되는 '스킬(Skill)' 용어를 문맥에 따라 '어빌리티(Ability)' 또는 '**skills <이름>**'으로 표준화하여 혼란을 방지합니다.
- **작업 규칙:**
    - 작품 내 캐릭터/몬스터의 능력, 시스템 등을 지칭할 때: **스킬 -> 어빌리티**
    - 에이전트의 도구/기능을 지칭할 때: **스킬 -> **skills <이름>****
- **진행 현황 (2026-01-24):**
    - [x] **manuals/ 폴더 완료:** 모든 매뉴얼 내 용어 치환 완료 (에이전트 도구 제외)
    - [ ] **.agent/skills/ 폴더 진행 중:**
        - 완료된 파일:
            - `write_scene/SKILL.md`
            - `improve_writing/SKILL.md`
            - `improve_writing/templates/10_revision_sheet.md`
            - `extract_creature_tags/SKILL.md`
            - `create_trait/SKILL.md`
            - `enhance_entity/SKILL.md`
            - `create_religion/SKILL.md`
            - `create_system/SKILL.md`
        - 대기 중인 파일:
            - `extract_concepts/SKILL.md`
            - `create_race/SKILL.md`
            - `create_plot/SKILL.md`
            - `create_magic/SKILL.md`
            - `create_lore/SKILL.md`
            - `create_history/SKILL.md`
            - 그 외 `.agent/skills/` 하위 모든 `.md` 파일들
    - [ ] **_templates/ 폴더 대기 중**
    - [ ] **data/ 폴더 대기 중**

---

## ✅ 완료된 작업

### 세계관 설정 시스템 고도화 (2026.01.20 완료)
- [x] **특성 데이터 확장:** `11_지역환경.md`, `12_외교.md` 추가 및 `00_유형.md` 개념 정립 (총 13종 시스템 구축)
- [x] **템플릿 전면 개편:** `_templates/world_detail/` 10종 템플릿에 `data/traits` 연동 테이블 포맷 적용
- [x] **예시 라이브러리 구축:** `_templates/world_detail/examples/` 폴더 신설 및 고품질 예시 파일 10종 생성
- [x] **매뉴얼/프롬프트 동기화:** 가이드 문서 링크 연결 및 생성 프롬프트(`create_*.md`) 로직 업데이트

### 템플릿 및 가이드 보강 (2026.01 완료)
- [x] **템플릿 예시 추가:** `_templates/world_detail/` 4종(아이템, 지역, 단체, 국가)에 상세 작성 예시 추가 완료.


### 8. 플롯 템플릿 확장 (2026.01 완료)
- [x] **20가지 마스터 플롯 가이드 완료**
    - `01_master_plots_part1.md` (1~10번: 추구, 모험, 추적, 구출, 탈출, 복수, 수수께끼, 라이벌, 희생자, 유혹)
    - `02_master_plots_part2.md` (11~20번: 변신, 변모, 성숙, 사랑, 금지된 사랑, 희생, 발견, 지독한 행위, 상승, 하강)
- [x] **서사 구조 및 트로프 정리 완료**
    - `03_narrative_structures.md` (3막, 스토리 서클, 세이브 더 캣, 피히테 곡선, 기승전결)
    - `04_webnovel_tropes.md` (회귀, 빙의, 환생, 헌터물)

### 문서 및 일관성 (2026.01 완료)
- [x] **문서 역할 분리:** `README.md`(사용자용)와 `GEMINI.md`(에이전트용)의 역할 정의 및 중복 최소화 완료.
- [x] **표현력 DB 구조 잡기:** `data/word_list/expression/` 폴더 및 기본 파일 생성 완료.

### 이전 완료 내역
- [x] **매뉴얼 일치:** 워크플로우 11단계로 통합.
- [x] **데이터 확장:** 무협(`murim`) 키워드 DB 구축.
- [x] **승격 자동화:** `/promote` 워크플로우 생성.
- [x] **핵심 워크플로우 개선:** 아크 설계(Step 6), 세계관 상세(Step 5) 가이드 보강.
- [x] **시소러스 시스템 연동:** 에이전트가 시소러스 데이터를 활용하도록 프로세스 내재화.

---
**마지막 업데이트:** 2026년 1월 24일 토요일