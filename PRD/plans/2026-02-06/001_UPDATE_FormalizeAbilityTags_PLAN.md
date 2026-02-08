# PLAN: 어빌리티 태그 프로토콜 공식화 및 시스템 통합
> **Date:** 2026-02-06
> **Task ID:** 001_UPDATE_FormalizeAbilityTags
> **Language:** Korean

## 1. Objective
임시로 작성된 `report/ability_tag_protocol.md`의 내용을 정식 매뉴얼(`manuals/99-2_ability_tags.md`)로 승격시키고, 이를 시스템(`create_ability` 스킬)에 통합하여 어빌리티 생성 시 태그가 필수적으로 포함되도록 한다. 또한 태그 목록의 확장성을 보장한다.

## 2. Context Analysis
- **Target Files:** `report/ability_tag_protocol.md`, `.agent/skills/create_ability/SKILL.md`, `manuals/99-2_ability_tags.md` (NEW)
- **Current Issue:** 현재 태그 프로토콜은 단순 리포트 형태이며 시스템적으로 강제되지 않음. 어빌리티 생성 시 검색 및 분류를 위한 메타데이터(태그)가 누락될 수 있음.

## 3. Strategy
1.  **매뉴얼화 (Migration):** 리포트의 내용을 `manuals/99-2_ability_tags.md`로 이동. 핵심 규칙(필수 필드, 오픈 태깅)을 명시.
2.  **스킬 통합 (Integration):** `create_ability` 스킬이 출력하는 데이터 스키마에 `Tag` 컬럼을 추가하고, 새 매뉴얼을 참조하도록 지침 수정.
3.  **정리 (Cleanup):** 구 리포트 파일 삭제.

## 4. Impact Analysis
- **Affected Files:** `create_ability` 스킬 정의, 매뉴얼 폴더.
- **Side Effects:** 이후 생성되는 모든 어빌리티 데이터에 태그 필드가 추가됨. 기존 데이터에는 영향 없음.

## 5. Task List
- [ ] `manuals/99-2_ability_tags.md` 생성 (리포트 내용 이관)
- [ ] `.agent/skills/create_ability/SKILL.md` 수정 (태그 필드 추가, 매뉴얼 참조)
- [ ] `report/ability_tag_protocol.md` 삭제
- [ ] 변경 사항 검증

## 6. Verification Plan
- 생성된 매뉴얼 파일(`manuals/99-2_ability_tags.md`)의 규칙 및 목록 확인.
- 스킬 파일(`SKILL.md`)의 데이터 스키마 내 `Tags` 컬럼 존재 여부 확인.
