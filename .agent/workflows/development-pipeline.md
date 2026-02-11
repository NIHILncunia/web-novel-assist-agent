---
name: development-pipeline
description: 9-phase Development Pipeline complete knowledge. 통합된 bkit PDCA 체계와 연동하여 개발의 전 과정을 9단계로 관리합니다.
---

# bkit 9-Phase Development Pipeline

> **Purpose**: 프로젝트 초기 사양 정의부터 배포까지의 모든 과정을 9단계로 표준화하여 일관된 품질을 보장합니다.

---

## 1. 파이프라인과 PDCA 연동

모든 페이즈는 bkit PDCA 사이클의 특정 단계에 속하며, `docs/` 하위의 지정된 폴더에 결과물을 저장합니다.

| Phase | 명칭 | PDCA 단계 | 저장 경로 |
|-------|------|----------|-----------|
| **Phase 1** | Schema (용어/데이터) | Plan | `docs/01-plan/` |
| **Phase 2** | Convention (규칙) | Plan | `docs/01-plan/` |
| **Phase 3** | Mockup (UI/UX) | Design | `docs/02-design/` |
| **Phase 4** | API Spec | Design/Do | `docs/02-design/` |
| **Phase 5** | Design System | Do | `docs/02-design/` |
| **Phase 6** | UI Integration | Do | (Codes) |
| **Phase 7** | SEO/Security | Do | (Codes) |
| **Phase 8** | Code Review | Check | `docs/03-analysis/` |
| **Phase 9** | Deployment | Act | `docs/04-report/` |

---

## 2. 프로젝트 수준별 페이즈 적용

| Level | 필수 페이즈 | 비고 |
|-------|-----------|------|
| **Starter** | 1, 2, 3, 6, 9 | 최소 기능 구현 중심 |
| **Dynamic** | 1, 2, 3, 4, 6, 9 | API 및 데이터 연동 필수 |
| **Enterprise** | 1 ~ 9 전체 | 안정성 및 확장성 중심 |

---

## 3. 명령어 활용

- `/development-pipeline status`: 파이프라인의 현재 진행 상태 확인.
- `/development-pipeline start`: 파이프라인의 첫 단계(Phase 1) 시작.
- `/development-pipeline next`: 다음 페이즈로 이동 및 가이드 제공.

---

**📊 bkit Feature Usage**
- ✅ **Used**: `/development-pipeline`
- ⏭️ **Not Used**: `None`
- 💡 **Recommended**: `/development-pipeline next`
