# Manuals 폴더 수정 작업 완료 보고

마스터의 요청에 따라 `manuals/` 폴더 내의 모든 매뉴얼 파일에 대한 번호 매기기 및 내부 참조 수정 작업을 완료했습니다.
이제 Step 0부터 Step 10까지 논리적인 흐름이 끊기지 않고 이어집니다.

## ✅ 완료된 작업 목록

### 1. 매뉴얼 제목 및 단계 번호 표준화 (Step X)
모든 매뉴얼의 제목을 `기능 XX`에서 `[Step X]` 형식으로 통일했습니다.
- `03_logline.md`: Function 02 -> **[Step 3]**
- `04_synopsis.md`: Function 03 -> **[Step 4]**
- `05_world_detail.md`: Function 04 -> **[Step 5]**
- `06_story_arc.md`: Function 05 -> **[Step 6]**
- `07_chapter_plan.md`: Function 06 -> **[Step 7]**
- `08_final_review.md`: Function 07 -> **[Step 8]**
- `09_drafting.md`: Function 08 -> **[Step 9]**
- `10_revision.md`: [Step 10] (유지)

### 2. 내부 참조 및 연결 흐름 수정
각 단계에서 이전 단계와 다음 단계를 가리키는 모든 링크와 텍스트를 수정했습니다.
- 예: Step 4(시놉시스) -> **Step 5(세계관 디테일)** -> **Step 6(플롯 아웃라인)**
- 이전 참조(Step -1)와 다음 참조(Step +1)가 모두 정렬되었습니다.

### 3. 산출물 파일 경로 업데이트
매뉴얼 내에서 생성하거나 참조하는 파일의 이름과 경로를 새로운 단계 번호에 맞췄습니다.
- `04_world_detail_check.md` -> **`05_world_detail_check.md`**
- `05_plot_outline.md` -> **`06_plot_outline.md`**
- `06_chapter_plans/` -> **`07_chapter_plans/`**
- `07_review_reports/` -> **`08_review_reports/`**

### 4. 하위 가이드 (Sub-guides) 헤더 수정
Step 5(세계관 디테일)에서 사용하는 하위 가이드 문서들의 헤더를 모두 `05-XX`로 업데이트했습니다.
- `05-00_framework_guide.md` ~ `05-08_stories_guide.md` (총 9개 파일)

---

## 📂 최종 파일 구조 (Manuals)

- `[Step 0]` 00_idea_generation.md
- `[Step 1]` 01_style_config.md
- `[Step 2]` 02_world_concept.md
- **`[Step 3]` 03_logline.md** (Updated)
- **`[Step 4]` 04_synopsis.md** (Updated)
- **`[Step 5]` 05_world_detail.md** (Updated)
    - `05-xx_..._guide.md` (Sub-guides Updated)
- **`[Step 6]` 06_story_arc.md** (Updated)
- **`[Step 7]` 07_chapter_plan.md** (Updated)
- **`[Step 8]` 08_final_review.md** (Updated)
- **`[Step 9]` 09_drafting.md** (Updated)
- `[Step 10]` 10_revision.md

작업이 성공적으로 마무리되었습니다.
