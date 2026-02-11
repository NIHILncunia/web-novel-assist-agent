---
name: pdca
description: bkit PDCA(Plan-Design-Do-Check-Act) 사이클 통합 관리 워크플로우. 계획 수립부터 설계, 구현, 검증, 보고까지의 전 과정을 자동화하고 표준 가이드를 제공합니다.
---

# bkit PDCA Workflow Guide

> **Core Logic**: 루프 중심의 PDCA 사이클을 프로젝트 루트의 `docs/` 폴더 하위에 철저히 문서화하고 관리합니다.

---

## 🛠️ Commands & Steps

| Command | Action | Path |
|---------|--------|------|
| **`/pdca plan {feature}`** | 요구사항 기반 계획 수립 | `docs/01-plan/` |
| **`/pdca design {feature}`** | 상세 기술 설계 | `docs/02-design/` |
| **`/pdca do {feature}`** | 구현 가이드 및 코딩 | (Codes) |
| **`/pdca analyze {feature}`** | Gap 분석 및 품질 검토 | `docs/03-analysis/` |
| **`/pdca iterate {feature}`** | 자동 개선/수정 반복 | `docs/03-analysis/` |
| **`/pdca report {feature}`** | 완료 보고 및 Act | `docs/04-report/` |

---

## 📌 Rules & Guidelines

### 1. 파일 명명 규칙 (Strict)
- **Format**: `{YYYY-MM-DD}-{feature}-{Type}.md`
- **Example**: `2026-02-11-auth-PLAN.md`

### 2. 저장 위치 (Parallel Structure)
- 모든 PDCA 산출물은 `docs/` 하위의 지정된 번호 폴더에 저장됩니다. (PRD와 병렬)

### 3. 능동적 다음 단계 가이드
- 각 단계 완료 후 출력되는 리포트의 **Recommended** 섹션에 마스터가 바로 복사하여 사용할 수 있는 다음 단계 명령어를 포함해야 합니다.
- 예: `💡 Recommended: /pdca design {feature}`

### 4. 진행도 관리
- 각 단계는 이전 단계의 산출물이 있어야 진행 가능합니다 (Plan -> Design -> Do -> Analyze -> Report).

---

## 📊 bkit Feature Usage 리포트 출력 규칙

모든 `/pdca` 관련 답변 하단에는 다음 형식을 고정 출력합니다.

```markdown
---
**📊 bkit Feature Usage**
- ✅ **Used**: [사용한 명령어]
- ⏭️ **Not Used**: [미사용 기능 및 사유]
- 💡 **Recommended**: [피처명을 포함한 다음 복사 명령어]
```
