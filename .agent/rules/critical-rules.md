---
trigger: always_on
---

# bkit Core Rules (Novel Assist Agent)

> 이 규칙은 bkit 및 PDCA 방법론의 효율적인 운영을 위해 글로벌 `bkit-rules`를 기반으로 정의되었습니다.

## Rule 1: PDCA & Planning First
- 모든 기능 개발 또는 0.5레벨 이상의 변경 상황에서는 **PDCA 사이클**을 준수합니다.
- 작업을 시작하기 전 `implementation_plan.md`를 작성하여 마스터의 승인을 얻는 것이 원칙입니다.
- 진행 상황은 `task.md`를 통해 추적하며, 위상 변화 시 `task_boundary`를 호출합니다.

## Rule 2: Project Level & Task Classification
- 프로젝트의 복잡성과 코드 변경량에 따라 레벨을 감지하고 대응합니다.
- **[Trivial]** < 30 lines: 즉시 실행 가능
- **[Minor]** 100-500 lines: `Light PDCA` (간소화된 계획)
- **[Feature]** 500+ lines: `Standard PDCA` (정식 계획 및 검증)

## Rule 3: Mandatory Feature Usage Report (CRITICAL)
모든 답변 하단에는 반드시 다음 형식을 포함합니다 (인용구 스타일 및 아이콘 준수):

---
> 📊 **bkit Feature Usage**
> - ✅ **Used**: [이번 응답에서 사용한 기능/명령어]
> - ⏭️ **Not Used**: [주요 미사용 기능 및 사유]
> - 💡 **Recommended**: [다음 단계에 권장되는 bkit 명령어/스킬]

## Rule 4: PDCA Guide & Next Steps
- 리포트 하단에는 현재 작업의 문맥에 맞는 `/pdca` 명령어 가이드를 제공합니다.
- 예: `[Check] 단계라면: /pdca check [작업명]`
- 작업을 새로 시작하는 경우 시작점 명령어를 구체적으로 안내합니다.

---
> [!NOTE]
> 본 규칙은 글로벌 `~/.gemini/antigravity/skills/bkit-rules/SKILL.md`를 프로젝트에 최적화한 버전입니다. 상세 가이드는 `~/.gemini/README.md`를 참조하십시오.