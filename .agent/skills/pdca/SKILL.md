---
name: pdca
description: bkit PDCA(Plan-Design-Do-Check-Act) 사이클 통합 관리 스킬. 계획 수립부터 설계, 구현, 검증, 보고까지의 전 과정을 자동화하고 표준 가이드를 제공합니다.
---

# pdca Skill (bkit Standard)

## Instructions

이 스킬은 프로젝트 개발 전 과정을 bkit PDCA 사이클에 맞춰 체계적으로 관리하기 위한 통합 지침입니다.

### 🛠️ PDCA 5단계 지침

#### 1. Plan (계획)
- **명령어**: `/pdca plan {feature}`
- **수행**: `docs/01-plan/` 하위에 요구사항과 성공 지표를 정의한 계획서를 생성합니다.
- **파일명**: `{YYYY-MM-DD}-{feature}-PLAN.md`

#### 2. Design (설계)
- **명령어**: `/pdca design {feature}`
- **수행**: `docs/02-design/` 하위에 데이터 모델, API 사양, 클린 아키텍처 레이어를 설계합니다.
- **파일명**: `{YYYY-MM-DD}-{feature}-DESIGN.md`

#### 3. Do (구현)
- **명령어**: `/pdca do {feature}`
- **수행**: 설계를 준수하여 실제 코드를 개발합니다. `Coding-Rules.md`를 엄격히 따릅니다.

#### 4. Check (검증)
- **명령어**: `/pdca analyze {feature}`
- **수행**: `docs/03-analysis/` 하위에 설계와 구현의 일치도(Gap Analysis)를 정량화하여 보고합니다.

#### 5. Act (보고/개선)
- **명령어**: `/pdca report {feature}`
- **수행**: `docs/04-report/` 하위에 최종 결과를 보고하고 프로젝트 사이클을 종료합니다.

---

### 📌 공통 규칙
- **저장 위치**: 모든 산출물은 `docs/` 폴더 하위에 저장합니다 (PRD와 병렬).
- **명명 규칙**: 파일명에 반드시 오늘 날짜(`YYYY-MM-DD`)를 포함합니다.
- **리포트**: 모든 답변 하단에 **bkit Feature Usage** 리포트를 포함하며, `Recommended` 섹션에 다음 명령어를 제안합니다.
