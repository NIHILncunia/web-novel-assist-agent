# GEMINI.md: NOVEL AI 에이전트 내부 작동 지침서

**이 문서는 NOVEL 프로젝트의 AI 에이전트(저, Gemini)를 위한 핵심 지침입니다.** 여기에는 프로젝트의 전체 폴더 구조, 파일 관리 규칙, 상호작용 워크플로우 등 제가 작업을 수행하는 데 필요한 모든 기술적 명세가 포함되어 있습니다.

---

## 1. AI 상호작용 기본 원칙

*   **한국어 응답:** 마스터와의 모든 상호작용은 반드시 한국어로 진행합니다.
*   **매뉴얼 준수:** 모든 작업은 `manuals/` 폴더에 명시된 11단계 워크플로우와 각 단계별 가이드를 엄격히 준수합니다.
*   **템플릿 활용:** 모든 기획 문서와 설정 파일은 `_templates/` 폴더의 해당 템플릿을 기반으로 생성합니다.
*   **선-제안, 후-생성:** 파일을 생성하기 전에 반드시 제안서를 먼저 제시하고 마스터의 동의를 얻습니다.
*   **대화 기록:** 모든 상호작용은 `00_conversation_log.md`에 `manuals/99_common_logger.md` 지침에 따라 기록합니다.

---

## 2. 전체 폴더 구조 (Master Directory Structure)

제가 참조하고 관리해야 할 전체 폴더 구조는 다음과 같습니다.

```
novel-assist-agent/
│
├── 📂 manuals/                     # 11단계 창작 프로세스 가이드 (AI 행동의 근거)
│   ├── 00_idea_generation.md       # [Step 0] 아이디어 발상
│   ├── 01_style_config.md          # [Step 1] 집필 스타일 설정
│   ├── ... (이하 11단계 가이드)
│   └── 10_revision.md              # [Step 10] 퇴고 및 수정
│
├── 📂 .agent/                      # AI 에이전트 자원
│   ├── skills/                     # 특화 작업 단위 (Skills) 및 템플릿
│   └── workflows/                  # 자동화 워크플로우
│
├── 📂 _templates/                  # [공용 양식]
│   └── note_template.md            # 메모 템플릿
│
├── 📂 library/                     # 공용 자산 라이브러리
│   └── shared_world/               # 재사용 가능한 공용 세계관
│
├── 📂 data/                        # [중앙 데이터] 프로젝트 공통 데이터
│   ├── word_list/                  # 장르별 키워드 사전
│   ├── traits/                     # [트레잇] 총 13종
│   ├── ability/                    # [어빌리티] 발동형/지속형 기술
│   └── 아이템.md                   # 아이템 요약 테이블
│
├── 📂 incubator/                   # 아이디어 인큐베이터 (제목 미정 기획물)
│   └── [Idea_Concept_A]/           # 아이디어별 폴더로 관리
│       ├── 00_conversation_log.md  # 통합 대화 로그
│       ├── 00_bible/               # 작품 전용 설정집 (초안)
│       └── 01_planning/            # 기획 문서 (초안)
│
└── 📂 projects/                    # 정식 프로젝트 (제목 확정 후)
    └── [Project_Title]/
        ├── 00_conversation_log.md  # 통합 대화 로그
        ├── 00_bible/               # 작품 전용 설정집 (확정)
        ├── 01_planning/            # 기획 문서 (확정)
        └── 02_drafts/              # 실제 원고
```

---

## 3. 핵심 워크플로우 및 파일 관리 규칙

### 3.1. 대화 기록 (Conversation Logging)

**규칙:** 모든 마스터의 요청과 저의 응답은 해당 프로젝트의 `00_conversation_log.md` 파일에 **즉시, 자동으로 기록**되어야 합니다.

1.  **파일 위치:**
    *   **인큐베이터 단계:** `incubator/[가제_컨셉명]/00_conversation_log.md`
    *   **프로젝트 단계:** `projects/[작품명]/00_conversation_log.md`
2.  **기록 형식:** `manuals/99_common_logger.md` 파일에 명시된 마크다운 블록 형식을 엄격히 준수합니다.

### 3.2. Step별 결과 파일 저장

- **목표:** 프로젝트 내에서 혼용되는 '스킬(Skill)' 용어를 문맥에 따라 '어빌리티(Ability)' 또는 **skills <이름>**으로 표준화하여 혼란을 방지합니다.
- **작업 규칙:**
    - 작품 내 캐릭터/몬스터의 능력, 시스템 등을 지칭할 때: **스킬 -> 어빌리티**
    - 에이전트의 도구/기능을 지칭할 때: **스킬 -> **skills <이름>** **
**규칙:** 각 Step의 최종 결과물은 대화 로그와 **별도로** 지정된 폴더에 확정된 내용만 저장합니다.

*   **저장 위치:**
    *   **작품명 미정 시:** `incubator/[가제_컨셉명]/` 하위 폴더
    *   **작품명 확정 후:** `projects/[작품명]/` 하위 폴더
*   **파일 경로:**
    *   `style_profile.md` → `.../00_bible/style_profile.md`
    *   `concept_note.md` → `.../01_planning/01_concept_note.md`
    *   `logline.md` → `.../01_planning/02_logline.md`
    *   `synopsis.md` → `.../01_planning/03_synopsis.md`
    *   **세계관 설정 파일들** → `.../00_bible/` 하위의 각 타입별 폴더
    *   `world_detail_check.md` → `.../01_planning/04_world_detail_check.md`
    *   `plot_outline.md` → `.../01_planning/05_plot_outline.md`
    *   **챕터 계획 파일들** → `.../01_planning/06_chapter_plans/`
    *   `review_reports` → `.../01_planning/07_review_reports/`
    *   **원고 파일들** → `.../02_drafts/`

### 3.3. 프로젝트 승격: `incubator` → `projects`

**규칙:** `manuals/04_synopsis.md`에 따라, **Step 4 (시놉시스) 완료 후** 마스터에게 작품명을 확정할지 반드시 질문해야 합니다.

1.  **질문:** "마스터, 시놉시스가 완성되었습니다. 이제 이 작품의 정식 제목을 정하시겠습니까?"
2.  **마스터가 제목 확정 시:**
    *   `incubator/[가제_컨셉명]/` 폴더 전체를 `projects/[새 작품명]/`으로 **이동(move)**합니다.
    *   이동 후, 기존 `incubator` 폴더는 삭제됩니다.
    *   이후의 모든 작업은 새로운 `projects/[새 작품명]/` 폴더를 기준으로 수행합니다.
3.  **마스터가 제목 보류 시:**
    *   계속 `incubator/[가제_컨셉명]/` 폴더에서 다음 Step을 진행합니다.
    *   이후 Step 진행 중 언제든 마스터가 제목을 정하면, 그 시점에서 프로젝트 승격 절차를 수행합니다.

---

## 4. 고급 기능 활용 지침

*   **키워드 브레인스토밍, 설정 추출 등:** `manuals/98_ai_prompt_guide.md`에 기술된 고급 기능을 수행할 수 있습니다. 각 기능은 대응하는 **skills**을 호출하여 수행합니다.
*   **시소러스 활용:** 캐릭터, 배경, 플롯 등을 구체화할 때 `data/word_list/Thesaurus/`의 데이터를 적극적으로 활용하여 깊이 있는 제안을 합니다.
- **공용 레고 블록 (Universal Lego Block):** `data/traits`와 `data/ability`의 데이터를 활용합니다. 인물, 단체, 아이템, 국가 생성 시 이 트레잇과 어빌리티를 자유롭게 가져와 조립하여 '새로운 해석'을 적용해야 합니다. 선입견 없이 데이터를 섞으십시오.

---
**[AI 에이전트 지침서 최종 업데이트: 2026-01-15]**
이 문서는 제 행동의 기준이므로, 항상 최신 상태를 유지해야 합니다.