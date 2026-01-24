---
description: 특정 프로세스를 시뮬레이션하고 파일 경로를 확인하여 검증합니다.
---
# 특정 프로세스 검증 (Verify Specific Process)

이 워크플로우를 사용하여 특정 프로세스(Step 0-10)를 시뮬레이션하고, 파일 참조를 확인하며 보고서를 생성합니다.

## Arguments
- `process_id`: 검증할 프로세스 ID (예: "0", "4", "10").

## 1.5. 프로세스별 관련 스킬 (Mapping)

검증할 `process_id`에 해당하는 핵심 스킬을 식별합니다.

| Process ID | Process Name | Relevant Skills (Check Target) |
| :---: | :--- | :--- |
| **0** | 아이디어 발상 | `brainstorm_ideas`, `extract_concepts` |
| **1** | 집필 스타일 | `analyze_project` |
| **2** | 핵심 키워드 | `brainstorm_ideas` |
| **3** | 로그라인 | `update_synopsis`, `improve_writing` |
| **4** | 시놉시스 | `update_synopsis`, `create_plot` |
| **5** | 세계관 디테일 | `create_race`, `create_character`, `create_region`, `create_nation`, `create_organization`, `create_item`, `create_system`, `create_magic`, `create_religion`, `create_history`, `create_lore`, `create_ability` |
| **6** | 에피소드 플롯 | `create_plot`, `analyze_relations` |
| **7** | 챕터 계획 | `create_plot` |
| **8** | 본문 작성 | `write_scene`, `improve_writing` |
| **9** | 리뷰 및 분석 | `review_world`, `analyze_project` |
| **10** | 퇴고 및 수정 | `improve_writing` |

## Steps

1.  **대상 매뉴얼 식별**
    - 주어진 `process_id`에 해당하는 매뉴얼 파일을 찾습니다 (예: `manuals/04_synopsis.md`).

2.  **매뉴얼 내용 분석**
    - 매뉴얼 파일을 읽습니다.
    - **CRITICAL:** 참조된 **모든** 파일 경로를 추출합니다.
        - **요약하지 마십시오** (예: `prompt/04_writing/*.md`와 같이 쓰지 말 것).
        - **각 파일을 개별적으로 나열합니다** (파일이 많더라도 전부 나열).
    - 포함 대상:
        - 템플릿 (`templates/Sheets/...` 또는 `_templates/Sheets/...`)
        - 프롬프트 (`prompt/...`)
        - 데이터 (`data/...`)
        - 다른 매뉴얼 (`manuals/...`)

3.  **관련 스킬 상태 확인 (New)**
    - 위 **Mapping** 테이블을 참조하여 현재 `process_id`에 해당하는 스킬 목록을 확인합니다.
    - 각 스킬에 대해 다음을 점검합니다:
        - **SKILL.md 존재 여부:** `.agent/skills/[Skill_Name]/SKILL.md`
        - **템플릿 폴더 확인:** `.agent/skills/[Skill_Name]/templates/` (존재할 경우)

4.  **파일 존재 여부 확인**
    - 추출된 각 파일 경로가 시스템에 실제로 존재하는지 확인합니다.
    - 각 항목의 상태(유효/누락)를 기록합니다.

5.  **보고서 생성**
    - 키 `_templates/verification_report_template.md`를 사용합니다.
    - 새 보고서 파일 `report/{{date}}_프로세스{{process_id}}_모의점검_보고서.md`를 생성합니다.
    - 템플릿에 검증 결과(파일 경로 및 **스킬 점검 결과**)를 채웁니다.
    - 템플릿에 명시된 표 형식을 사용합니다.

6.  **사용자 알림**
    - 검증이 완료되었음을 알리고 보고서 경로를 제공합니다.
