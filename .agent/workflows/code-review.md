---
name: code-review
description: Code review skill for analyzing code quality, detecting bugs, and ensuring best practices.
---

# Code Review Guide

> **Context**: bkit PDCA 'Check' 단계의 핵심 활동입니다.

---

## 🛠️ Action Items

### 1. 정적 분석
- 컨벤션 준수, 명명 규칙, 중복 코드, 복잡도를 점검합니다.

### 2. 로직 및 버그 탐지
- 잠재적 런타임 에러, 엣지 케이스 처리, 보안 취약점을 점검합니다.

### 3. 대리인 활용
- `code-analyzer`를 호출하여 심층 분석 리포트를 생성합니다.

---

**📊 bkit Feature Usage**
- ✅ **Used**: `/code-review`
- 💡 **Recommended**: `/pdca analyze {feature}`
