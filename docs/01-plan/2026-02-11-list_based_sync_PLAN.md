# [PLAN] 2026-02-11 - 사용자 정의 소스 리스트 기반 자산 동기화 (v3)

## 1. 개요
마스터가 직접 제공한 `2026-02-11-bkit_skills_source_list.md` 소스 리스트를 최종 기준으로 삼아, 프로젝트의 bkit 환경을 정밀 동기화합니다.

## 2. 동기화 대상 분석
- **Skills (22종)**: `bkit-rules`부터 `zero-script-qa`까지 마스터가 지정한 스킬 폴더 전체를 `.agent/skills/`로 동기화.
- **Workflows (27종)**: `bkit-init.md`부터 `phase-9-deployment.md`까지 워크플로우 파일들을 `.agent/workflows/`로 동기화.
- **Rules (3종)**: `plan-and-result-protocol.md` 등 글로벌 규칙들을 프로젝트 규정에 맞게 확인 및 적용.

## 3. 작업 상세
### 3.1. 스킬 동기화 (Source -> Target)
- 각 스킬의 `SKILL.md`가 포함된 상위 폴더를 `.agent/skills/` 하위로 개별 복사합니다.
- 예: `.../antigravity/skills/pdca/` -> `.agent/skills/pdca/`

### 3.2. 워크플로우 동기화 (Source -> Target)
- 지정된 `.md` 파일들을 `.agent/workflows/` 하위로 개별 복사합니다.
- 기존 파일이 있을 경우 덮어쓰기(Overwrite)하여 최신 버전을 유지합니다.

### 3.3. 예외 처리
- 로컬 전용 Novel AI 스킬(`write_scene` 등)은 리스트에 없으므로 **절대 삭제하거나 수정하지 않고 그대로 보존**합니다.

## 4. 검증 계획
- 소스 리스트상의 파일 수와 로컬에 복사된 파일 수가 일치하는지 전수 조사.
- 핵심 워크플로우(`bkit-init`, `pdca`)의 동작 여부 샘플 테스트.
