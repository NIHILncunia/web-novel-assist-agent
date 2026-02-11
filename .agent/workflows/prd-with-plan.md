---
description: prd-with-plan — PRD 준수 + 플랜 필수 (Anti-Gravity)
---

# prd-with-plan : PRD 준수 + PDCA 사이클 (bkit 표준)

이 **워크플로(커맨드)**는 사용자 요청을 처리할 때 **bkit 글로벌 표준(PDCA)**을 엄격히 준수하며, **날짜 기반 파일명**을 사용하여 모든 산출물을 관리합니다.

**참조 규칙:** `~/.gemini/rules/plan-and-result-protocol.md`, `~/.gemini/antigravity/global_workflows/bkit-rules.md`

## 필수 동작 흐름 (PDCA Cycle)

### 0. PRD 확인 및 생성 (Preparation)
1. **PRD 점검**: 프로젝트 루트 `PRD/` 폴더에 오늘 날짜 또는 최신 PRD가 있는지 확인합니다.
2. **없을 경우**:
    - `~/.gemini/antigravity/global_workflows/create-prd.md` 워크플로를 먼저 실행하여 `YYYY-MM-DD-PRD.md` 등 3종 문서를 생성합니다.
    - 사용자에게 "PRD 생성을 완료했습니다."라고 보고 후 진행합니다.

### 1. Plan (계획 수립)
- **파일 생성**: `PRD/plans/YYYY-MM-DD/` 폴더에 계획 문서를 생성합니다.
- **파일명 규칙**: `YYYY-MM-DD-{Seq}_PLAN_{Feature}.md`
    - 예: `2024-05-20-001_PLAN_Login.md`
- **내용**: `bkit` 표준 템플릿을 사용하여 구현 목표, 변경 대상 파일, 검증 계획을 수립합니다.
- **승인**: "마스터, `[파일명]` 계획을 수립했습니다. 진행하겠습니까?" 승인 요청.

### 2. Design (상세 설계) - *권장*
- **파일 생성**: `PRD/plans/YYYY-MM-DD/` 폴더에 설계 문서를 생성합니다.
- **파일명 규칙**: `YYYY-MM-DD-{Seq}_DESIGN_{Feature}.md`
- **내용**: 인터페이스 정의, 데이터 흐름, 컴포넌트 구조 등 상세 설계.

### /prd-with-plan: PRD 준수 및 능동적 계획 수립

> **Purpose**: PRD의 사양을 엄격히 준수하면서도 현재 작업에 가장 적합한 bkit PDCA 계획을 수립합니다.

---

## 🛠️ Step-by-Step

### 1. 사양 및 규칙 확인 (Check PRD)
- `PRD/PRD.md`를 열람하여 기능의 최초 설계 사양을 확인합니다.
- `PRD/Coding-Rules.md`를 열람하여 준수해야 할 기술적 제약을 확인합니다.

### 2. 9단계 파이프라인 상태 점검
- `/development-pipeline status`를 통해 현재 기능이 어느 페이즈에 있는지 확인합니다.

### 3. bkit PDCA 계획 수립 (Plan)
- `docs/01-plan/` 폴더 하위에 `{YYYY-MM-DD}-{feature}-PLAN.md` 문서를 생성합니다.
- **주의**: 단순 결과물 나열이 아닌, 구현 전략(Strategy)과 리스크 분석을 포함한 꼼꼼한 계획이어야 합니다.

### 4. 마스터 승인 및 가이드
- 수립된 계획을 마스터에게 보고하고 승인을 요청합니다.
- 리포트의 **Recommended** 섹션에 `/pdca design {feature}`를 명시하여 다음 단계를 안내합니다.

---

## 🏷️ 파일 명명 및 저장 규칙
- **저장 경로**: `docs/01-plan/`
- **파일명**: `{YYYY-MM-DD}-{feature}-PLAN.md`

---

**📊 bkit Feature Usage**
- ✅ **Used**: `/prd-with-plan`
- ⏭️ **Not Used**: `None`
- 💡 **Recommended**: `/pdca plan {feature}`

## 경로 및 네이밍 요약 (Strict)

- **PRD 폴더**: `PRD/`
    - `YYYY-MM-DD-PRD.md`
    - `YYYY-MM-DD-Coding-Rules.md`
    - `YYYY-MM-DD-Task-List.md`
- **PDCA 아티팩트**: `PRD/plans/YYYY-MM-DD/`
    - `YYYY-MM-DD-{Seq}_PLAN_{Feature}.md`
    - `YYYY-MM-DD-{Seq}_DESIGN_{Feature}.md`
    - `YYYY-MM-DD-{Seq}_CHECK_{Feature}.md`
    - `YYYY-MM-DD-{Seq}_RESULT_{Feature}.md`

## 사용 예시

- "로그인 기능 만들어줘 **@prd-with-plan**"
- "이 API 수정해줘, **prd-with-plan** 절차대로"

이 워크플로는 **작업의 크기와 상관없이** 항상 위 PDCA 절차와 파일명 규칙을 따릅니다.
