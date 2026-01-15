# TODO: NOVEL 프로젝트 개선 작업 목록 (2025.01)

## ✍️ 콘텐츠 및 데이터베이스 확장

### 1. 템플릿 및 가이드 보강
- **목표:** 사용자가 각 설정 항목을 더 쉽게 작성할 수 있도록 템플릿에 구체적인 예시를 추가하고, 분석 자료를 확대합니다.
- **작업 내용:**
    - [ ] `_templates/world_detail/` 내부의 나머지 템플릿(지역, 아이템 등)에 실제 작성 예시를 추가합니다. (`character_template`은 1차 완료)
    - [ ] `library/style_examples/`에 더 다양한 장르와 작품의 문체 분석(Case Study)을 추가합니다. (현재 3종 보유)

### 2. 문서 통합 및 일관성 확보 (보류)
- **목표:** 프로젝트의 각종 문서와 매뉴얼의 일관성을 높여 사용자와 AI 에이전트가 정확한 정보를 참조하도록 합니다.
- **작업 내용:**
    - [ ] `README.md`와 `GEMINI.md`의 내용 중복을 최소화하고 역할을 명확히 재정의합니다. (README: 외부 사용자용 / GEMINI: 에이전트 프롬프트용)

---

## ⚙️ 시스템 및 워크플로우 개선

### 향후 개선 계획
- **목표:** 데이터 관리의 효율성과 안정성을 높이고, 장기적인 확장성을 확보합니다.
- **작업 내용:**
    - [ ] **데이터 관리 시스템 변경:** `data/아이템.md`, `data/스킬.md` 등의 마크다운 테이블을 CSV 또는 SQLite DB로 전환하여 데이터 추가/수정/삭제 작업을 안정화합니다. (현재 컬럼 확정 대기 중)
    - [ ] **로그 시스템 변경:** `00_conversation_log.md` 파일을 데이터베이스 테이블로 전환하여, 장기 프로젝트의 컨텍스트 관리 효율성을 높이고 성능 저하를 방지합니다.

## ✨ 신규 기능 및 자동화

### 5. 기획과 집필 연동 강화 (챕터 진행 상태 관리)
- **목표:** `07_chapter_plan.md`를 동적인 집필 현황판으로 활용하여 챕터별 진행 상태를 시각적으로 관리합니다.
- **작업 내용:**
    - [ ] AI 에이전트가 특정 챕터의 집필 시작/완료 명령을 인식하고, 해당 프로젝트의 `07_chapter_plan.md` 파일 내 챕터 상태(`계획`, `집필 중`, `완료`)를 자동으로 업데이트하는 로직을 구현합니다.

### 6. 정합성 및 데이터 확장 (완료)
- [x] **.cursorrules 최신화:** 9단계 워크플로우를 11단계로 수정하여 매뉴얼과 일치시킴.
- [x] **데이터 확장:** 무협(`murim/index.md`) 키워드 DB 구축.
- [x] **승격 자동화:** `/promote` 워크플로우 생성.

### 7. 플롯 템플릿 확장 (Future Plan)
> **"인류 보편적 이야기 구조(Master Plots) 적용"**  
> 단순한 기승전결을 넘어, 로널드 B. 토비아스의 **20가지 마스터 플롯** 등을 참고하여 선택 가능한 플롯 템플릿을 늘립니다.

- [ ] **Plot Research & Template Creation**
    1.  **추구 (Quest):** 주인공이 소중한 무언가를 찾아 떠나는 여정. (반지의 제왕)
    2.  **모험 (Adventure):** 목적보다는 여정 자체의 흥미진진함에 초점. (돈키호테)
    3.  **추적 (Pursuit):** 도망치는 자와 쫓는 자의 숨 막히는 대결. (레미제라블)
    4.  **구출 (Rescue):** 악당에게 잡힌 대상을 구하고 돌아옴. (슈퍼마리오)
    5.  **탈출 (Escape):** 억압된 상황에서 자유를 찾아 탈출함. (쇼생크 탈출)
    6.  **복수 (Revenge):** 범죄를 목격하고 정의를 구현(보복)함. (몽테크리스토 백작)
    7.  **수수께끼 (The Riddle):** 감춰진 진실을 파헤침. (추리물, 셜록 홈즈)
    8.  **라이벌 (Rivalry):** 경쟁자와의 대결을 통해 성장. (슬램덩크)
    9.  **희생자/언더독 (Underdog):** 약자가 강자를 이기는 카타르시스. (다윗과 골리앗)
    10. **유혹 (Temptation):** 치명적인 유혹에 빠져 파멸하거나 극복함. (파우스트)
    11. **변신 (Metamorphosis):** 저주에 걸려 육체가 변하고, 이를 풀기 위해 노력. (미녀와 야수)
    12. **변모 (Transformation):** 내면의 변화와 성숙 과정. (성장물 전반)
    13. **성숙 (Maturation):** 아이에서 어른으로, 미숙에서 성숙으로. (빌트 웅스 로만)
    14. **사랑 (Love):** 시련을 극복하고 사랑을 쟁취. (로맨스)
    15. **금지된 사랑 (Forbidden Love):** 사회적 금기를 넘어서는 사랑. (로미오와 줄리엣)
    16. **희생 (Sacrifice):** 더 큰 가치를 위해 자신을 바침. (아마겟돈)
    17. **발견 (Discovery):** 자신이나 세상에 대한 비밀을 깨달음. (오이디푸스)
    18. **지독한 행위 (Wretched Excess):** 심리적 결함으로 인해 파멸해감. (사이코패스물)
    19. **상승 (Ascension):** 밑바닥에서 정상으로 올라감. (성공 신화)
    20. **하강 (Descension):** 정상에서 밑바닥으로 추락. (몰락의 서사)

- [ ] **Modern & Web Novel Specific Plots (Research Findings)**
    *   **댄 하몬의 스토리 서클 (Dan Harmon's Story Circle):**
        *   8단계 순환 구조: **일상(You) -> 욕망(Need) -> 탐험(Go) -> 적응(Search) -> 발견(Find) -> 대가(Take) -> 귀환(Return) -> 변화(Change)**.
        *   캐릭터의 심리적 변화와 성장에 초점. 미드(릭앤모티 등)와 현대 웹소설에 적합.
    *   **세이브 더 캣 (Save the Cat):**
        *   헐리우드 시나리오 작법의 웹소설화.
        *   독자의 이탈을 막는 **'비트 시트(Beat Sheet, 장면 구성표)'**와 페이스 조절에 특화. 특히 **'재미와 놀이(Fun and Games, 흥미 유발 구간)'** 중시.
    *   **기승전결 (Kishōtenketsu):**
        *   동양적 4단 구성. 갈등보다는 '전(Twist)'을 통한 국면 전환 강조.
        *   빌드업 후 터뜨리는 웹소설 호흡과 잘 맞음.
    *   **피히테 곡선 (Fichtean Curve):**
        *   빠른 전개, 위기의 연속. (**초반 훅(Hook)** -> 위기1 -> 위기2 -> 위기3 -> 절정)
        *   지루할 틈 없이 사건이 몰아치는 현대 웹소설/스릴러에 최적화.
    *   **회/빙/환 구조 (Regression/Possession/Transmigration):**
        *   **회귀 (Regression):** 미래의 지식으로 과거의 후회를 바로잡고 사이다 선사. (인생 2회차, 상태창)
        *   **빙의 (Possession):** 소설/게임 속 인물(주로 악역/단역)이 되어 원작 지식 활용 + 생존.
        *   **환생 (Reincarnation):** 새로운 세계에서 다시 태어나 전생의 능력/지식 활용.

### 8. 어휘 및 표현력 확장 (Vocabulary Expansion)
> **"풍부한 한국어 묘사를 위한 데이터베이스 구축"**  
> `data/word_list/Thesaurus`를 보강하여, AI가 더 감각적이고 다채로운 한국어 표현을 사용할 수 있도록 지원합니다.

- [X] **Korean Expression Database Creation (Structure Setup)**
    *   `data/word_list/expression/01_관용구.md` (Idioms)
    *   `data/word_list/expression/02_동사.md` (Verbs)
    *   `data/word_list/expression/03_형용사.md` (Adjectives)
    *   `data/word_list/expression/04_부사.md` (Adverbs)
    *   `data/word_list/expression/05_명사.md` (Nouns)
    *   `data/word_list/expression/06_어미.md` (Endings)
    *   `data/word_list/expression/07_상황_묘사_수식어.md` (Situational Modifiers)

---

## ✅ 완료된 작업

### 핵심 워크플로우 개선 (2025.01 완료)
- **Step 5 → Step 6 연계 강화:**
  - `manuals/06_story_arc.md`에 아크 설계 완료 및 에피소드 검증 절차 명시 완료.
- **Step 4 연관 설정 제안 규칙 명확화:**
  - `manuals/05_world_detail.md`에 필수 설정과 확장 설정 제안 프로세스 정립 완료.
- **문서화:**
  - `incubator`에서 `projects` 폴더로 이동하는 절차를 `README.md` 및 `manuals/04_synopsis.md`에 명시 완료.
- **체크리스트 보완:**
  - `_templates/world_checklist.md` 상세 항목 보강 완료.

### 이전 완료 내역
- **`START_HERE.md` 프로세스 단계 일치:**
  - `START_HERE.md` 파일의 프로세스 안내를 실제 `manuals` 구조와 일치하는 11단계(Step 0-10)로 수정 완료.
- **시소러스 데이터베이스 연동 시스템 리뉴얼 (Phase 1, 2, 3):**
  - AI가 시소러스(`data/word_list/Thesaurus/`) 데이터를 적극적으로 활용하도록 시스템 전반을 갱신 완료.
  - **Phase 1:** 핵심 매뉴얼(`05_world_detail`, `09_drafting`, `10_revision`)에 시소러스 활용 지침 반영.
  - **Phase 2:** 캐릭터 템플릿(`02-1_character_template.md`)에 시소러스 구조(트라우마, 감정 표현) 통합.
  - **Phase 3:** 핵심 프롬프트(`create_character`, `write_scene`)에 시소러스 활용 로직 내재화.

---
**마지막 업데이트:** 2026년 1월 15일 목요일
