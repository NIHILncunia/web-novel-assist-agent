# [Step 5] 세계관 디테일 확정 (World Detailing)

> **작성일:** 2026-01-04
> **수정일:** 2026-06-19

## 1. 개요
이 단계는 시놉시스와 플롯 아웃라인에 등장한 고유명사를 실제로 집필 가능한 설정 파일로 분해하고, 누락 여부를 점검하는 단계입니다.

**핵심 원칙**
- 먼저 목표를 정한 뒤 작업합니다.
- 파일은 제안서 승인 후 생성합니다.
- 생성 뒤에는 반드시 점검 파일을 갱신합니다.

---

## 2. 작업 프로세스

### Step 0. 목표 설정 및 점검 파일 준비
1. `01_planning/04_synopsis_sheet.md`를 읽어 인물, 지역, 국가, 종족, 단체, 아이템 등 고유명사를 추출합니다.
2. 추출 항목을 '필수 설정'으로 간주하고 작업 목록을 만듭니다.
3. `01_planning/05_world_detail_check.md` 파일을 생성하거나 갱신합니다.
   - 작품명 미정 시: `incubator/[가제_컨셉명]/01_planning/05_world_detail_check.md`
   - 작품명 확정 후: `projects/[작품명]/01_planning/05_world_detail_check.md`
4. `00_bible/` 하위의 기존 설정 파일을 확인해 이미 존재하는 항목은 체크합니다.
5. 작업 시작 시 아래 형식으로 브리핑합니다.

```markdown
마스터, 지금부터 **Step 5: 세계관 디테일 확정** 단계를 시작하겠습니다.

1. `04_synopsis_sheet.md`를 분석하여 필수 설정 목록을 추출했습니다.
2. `05_world_detail_check.md`를 생성 또는 업데이트하여 작업 목표를 정리했습니다.

가장 먼저 어떤 설정부터 구체화하시겠습니까?
```

### Step 1. 입력 분석
- 요청이 어떤 설정 타입인지 분류합니다.
  - 코어 규칙
  - 종족
  - 인물
  - 지역
  - 단체
  - 국가
  - 아이템
  - 역사
  - 전설
  - 관계
- 기존 설정과 충돌하는지 확인합니다.
- 부족한 연관 설정이 있으면 함께 제안합니다.

### Step 2. 제안서 작성
파일을 바로 만들지 않고 아래 항목을 포함한 제안서를 먼저 보여줍니다.

1. 설정 타입
2. 핵심 컨셉 요약
3. 연관 설정 제안
4. 예상 파일명 및 저장 위치

### Step 3. 승인 후 생성
마스터가 승인하면 그때 파일을 생성합니다.

### Step 4. 템플릿 기반 작성
실제 존재하는 `.agent/skills/.../templates/` 템플릿과 각 가이드를 기준으로 작성합니다.

- 코어 규칙: `.agent/skills/create_core_rules/templates/core_rules_template.md`
- 종족: `.agent/skills/create_race/templates/01_races_template.md`
- 인물: `.agent/skills/create_character/templates/02-1_character_template.md`, `02-2_sub_character_template.md`
- 지역: `.agent/skills/create_region/templates/03_regions_template.md`
- 단체: `.agent/skills/create_organization/templates/04_organizations_template.md`
- 국가: `.agent/skills/create_nation/templates/05_nations_template.md`
- 아이템: `.agent/skills/create_item/templates/06_items_template.md`
- 역사: `.agent/skills/create_history/templates/07_history_template.md`
- 전설: `.agent/skills/create_lore/templates/08_stories_template.md`
- 관계: `.agent/skills/analyze_relations/templates/09_relationships_template.md`

추가 규칙:
- YAML Frontmatter를 포함합니다.
- 판타지 용어는 `data/word_list/fantasy/판타지_용어.md`를 우선 참조합니다.
- 무협 용어는 `data/keyword/murim/` 하위 문서를 참조합니다.
- 인물과 몬스터 능력은 `data/ability/`와 `data/traits/`를 함께 참조합니다.
- 아이템은 먼저 `data/아이템.md`에서 재사용 가능성을 확인합니다.

### Step 5. 자가점검
설정 생성 후에는 반드시 `01_planning/05_world_detail_check.md`를 갱신합니다.

**점검 기준**
- 시놉시스에 언급된 핵심 고유명사에 대응하는 설정 파일이 존재하는가?

**점검 결과 예시**
```markdown
## 점검 결과

### 완료된 설정
- [x] 주인공: 카엘 -> `00_bible/02_characters/protagonists/주연_카엘.md`
- [x] 지역: 은빛숲 -> `00_bible/03_regions/지역_은빛숲.md`

### 누락된 설정
- [ ] 적대자: 마탑주 아르칸 마이어
- [ ] 지역: 마탑 아르카나
```

---

## 3. 참조 가이드

| 타입 | 참조 문서 |
| :--- | :--- |
| 코어 규칙 | `manuals/05-00_core_rules_guide.md` |
| 종족 | `manuals/05-01_races_guide.md` |
| 인물 | `manuals/05-02_character_guide.md` |
| 지역 | `manuals/05-03_regions_guide.md` |
| 단체 | `manuals/05-04_organizations_guide.md` |
| 국가 | `manuals/05-05_nations_guide.md` |
| 아이템 | `manuals/05-06_items_guide.md` |
| 역사 | `manuals/05-07_history_guide.md` |
| 전설 | `manuals/05-08_stories_guide.md` |
| 관계 | `manuals/05-09_relationships_guide.md` |

---

## 4. 표준 저장 구조

```text
[프로젝트]/00_bible/
├── 00_core_rules/
├── 01_races/
├── 02_characters/
│   ├── protagonists/
│   ├── supporting/
│   └── minor/
├── 03_regions/
├── 04_organizations/
├── 05_nations/
├── 06_items/
├── 07_history/
└── 08_stories/
```

점검 파일은 `01_planning/05_world_detail_check.md`에 둡니다.

---

## 5. 주의사항
- 제안 없이 바로 생성하지 않습니다.
- 기존 설정과 충돌하면 새 파일 생성보다 통합 또는 수정안을 먼저 제시합니다.
- Step 6 이후에도 부족한 설정이 발견되면 언제든 Step 5로 돌아올 수 있습니다.
