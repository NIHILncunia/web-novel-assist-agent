---
name: bkit-rules
description: bkit 플러그인의 핵심 규칙. PDCA 방법론, 레벨 감지, 대리인 자동 트리거, 코드 품질 표준 등을 정의합니다.
---

# bkit Core Rules Skill

## Instructions

이 스킬은 Anti-Gravity 에이전트가 bkit 표준에 따라 행동하도록 강제하는 핵심 규칙셋입니다.

### 🛡️ 핵심 규칙 (Core Rules)

1. **PDCA 최우선 (PDCA First)**: 모든 기능 개발은 `docs/01-plan/`, `docs/02-design/` 등의 문서를 먼저 생성하고 승인받는 것을 원칙으로 합니다.
2. **레벨 감지 (Level Detection)**: 프로젝트 구조를 분석하여 **Starter**, **Dynamic**, **Enterprise** 수준을 자동으로 판단합니다.
3. **병렬 폴더 구조**: `PRD/`(설계)와 `docs/`(기록) 폴더를 병렬로 엄격히 분리하여 관리합니다.
4. **리포트 템플릿 고정**: 모든 답변 하단에 **bkit Feature Usage** 리포트를 고정 템플릿으로 출력합니다.
5. **능동적 가이드**: 리포트의 `Recommended` 섹션에 현재 피처명을 포함한 다음 실행 명령어(복사 가능 형식)를 항상 노출합니다.

### 📌 에이전트 행동 강령
- **Gap 분석**: 구현 완료 후 반드시 `/pdca analyze`를 통해 일치도를 확인합니다 (90% 미만 시 iterate).
- **파일명**: 모든 산출물 파일명에는 오늘 날짜(`YYYY-MM-DD`)를 포함합니다.
- **언어**: 마스터와의 대화 및 모든 문서 작성은 **한글**을 사용합니다.
