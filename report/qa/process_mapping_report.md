# QA Report: 창작 프로세스 - 스킬 - 템플릿 매핑

## 1. 매핑 테이블

| 단계 (Step) | 관련 메뉴얼 | 대응 스킬 (Skill) | 결과물 템플릿 (Template) | 저장 위치 |
| :--- | :--- | :--- | :--- | :--- |
| **Step 00** | `00_idea_generation.md` | `brainstorm_ideas` | - | `01_planning/00_ideas.md` |
| **Step 01** | `01_style_config.md` | `improve_writing` | `note_template.md` | `00_bible/style_profile.md` |
| **Step 02** | `02_world_concept.md` | `create_core_rules` | `core_rules_template.md` | `00_bible/00_core_rules/` |
| **Step 03** | `03_logline.md` | - | `note_template.md` | `01_planning/02_logline.md` |
| **Step 04** | `04_synopsis.md` | `update_synopsis` | `note_template.md` | `01_planning/03_synopsis.md` |
| **Step 05-01** | `05-01_races_guide.md` | `create_race` | `race_template.md` | `00_bible/01_races/` |
| **Step 05-02** | `05-02_character_guide.md` | `create_character` | `protagonist_template.md` | `00_bible/02_characters/` |
| **Step 05-03** | `05-03_regions_guide.md` | `create_region` | `region_template.md` | `00_bible/03_regions/` |
| **Step 05-04** | `05-04_organizations_guide.md`| `create_organization`| `org_template.md` | `00_bible/04_organizations/` |
| **Step 05-05** | `05-05_nations_guide.md` | `create_nation` | `nation_template.md` | `00_bible/05_nations/` |
| **Step 05-06** | `05-06_items_guide.md` | `create_item` | `item_template.md` | `00_bible/06_items/` |
| **Step 05-07** | `05-07_history_guide.md` | `create_history` | `history_template.md` | `00_bible/07_history/` |
| **Step 06** | `06_story_arc.md` | `create_plot` | `plot_template.md` | `01_planning/05_plot_outline.md` |
| **Step 07** | `07_chapter_plan.md` | - | `note_template.md` | `01_planning/06_chapter_plans/` |
| **Step 08** | `08_final_review.md` | `review_world` | `verification_report.md` | `01_planning/07_review_reports/` |
| **Step 09** | `09_drafting.md` | `write_scene` | - | `02_drafts/` |
| **Step 10** | `10_revision.md` | `improve_writing` | - | `02_drafts/` |

## 2. 발견된 문제점 및 개선 사항

1.  **스킬 부재**: `Step 03 (로그라인)`과 `Step 07 (챕터 계획)`은 현재 전용 스킬 없이 범용 템플릿만 사용 중입니다. 이 과정에서 작가가 어떤 질문에 답해야 하는지 가이드해주는 인터뷰 스킬이 보강되면 좋습니다.
2.  **용어 불일치**: 일부 메뉴얼에서는 '능력'을 '스킬'로 혼용하고 있습니다. 에이전트 도구는 `skills`, 캐릭터 능력은 `ability`로 용어를 전수 통일해야 합니다.
3.  **저장 위치 명확화**: `create_item` 스킬은 `data/아이템.md`와 `00_bible/` 두 곳에 데이터를 저장하므로, 무결성 유지를 위해 `verify_links.py` 같은 검증 도구가 더 자주 활용되어야 합니다.

## 3. 결론
데이터 정규화 이후 템플릿 포맷은 통일되었으나, 각 단계별 스킬의 **인터뷰 질문(Prompt)**이 최신 정규화된 데이터(`traits`, `ability`)를 참조하도록 고도화하는 작업이 추가로 필요합니다.
