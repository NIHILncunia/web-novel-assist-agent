---
description: bkit 자산(스킬, 템플릿)을 Antigravity, Cursor 및 전체 글로벌 워크스페이스로 통합 동기화
---

이 워크플로우는 `extensions/bkit`의 최신 자산을 전체 개발 환경(Antigravity 글로벌, Cursor, 로컬 임시 환경 등)으로 강력하게 전파하고 동기화합니다. 특히 스킬들을 글로벌 워크플로우로 승격시켜 어디서나 즉시 슬래시 커맨드로 사용할 수 있게 합니다.

// turbo
1. 글로벌 통합 동기화 및 스킬 전파 실행 (Windows PowerShell)
```bash
# 변수 설정
powershell -Command "$srcDir = 'c:\Users\nihil\.gemini\extensions\bkit'; $globalWorkflowsDir = 'c:\Users\nihil\.gemini\antigravity\global_workflows'; $globalSkillsDir = 'c:\Users\nihil\.gemini\antigravity\skills'; $globalTemplatesDir = 'c:\Users\nihil\.gemini\antigravity\templates'; $cursorSkillsDir = 'c:\Users\nihil\.cursor\skills'; if (-not (Test-Path $globalWorkflowsDir)) { New-Item -ItemType Directory -Path $globalWorkflowsDir -Force }; if (-not (Test-Path $globalSkillsDir)) { New-Item -ItemType Directory -Path $globalSkillsDir -Force }; if (-not (Test-Path $globalTemplatesDir)) { New-Item -ItemType Directory -Path $globalTemplatesDir -Force }; if (-not (Test-Path $cursorSkillsDir)) { New-Item -ItemType Directory -Path $cursorSkillsDir -Force }"

# 1. 스킬을 글로벌 워크플로우로 배포 (슬래시 커맨드화)
powershell -Command "Get-ChildItem -Path 'c:\Users\nihil\.gemini\extensions\bkit\skills' -Directory | ForEach-Object { $skillName = $_.Name; $skillMd = Join-Path $_.FullName 'SKILL.md'; if (Test-Path $skillMd) { $destFile = Join-Path 'c:\Users\nihil\.gemini\antigravity\global_workflows' ($skillName + '.md'); Copy-Item -Path $skillMd -Destination $destFile -Force; Write-Host \"Registered Global Workflow: $skillName\" } }"

# 2. 글로벌 스킬 및 템플릿 원본 최신화 (Antigravity용)
powershell -Command "Copy-Item -Path 'c:\Users\nihil\.gemini\extensions\bkit\skills\*' -Destination 'c:\Users\nihil\.gemini\antigravity\skills' -Recurse -Force; Copy-Item -Path 'c:\Users\nihil\.gemini\extensions\bkit\templates\*' -Destination 'c:\Users\nihil\.gemini\antigravity\templates' -Recurse -Force; Write-Host 'Global Technical Assets Updated.'"

# 3. Cursor 자산 동기화
powershell -Command "Copy-Item -Path 'c:\Users\nihil\.gemini\extensions\bkit\skills\*' -Destination 'c:\Users\nihil\.cursor\skills' -Recurse -Force; Write-Host 'Cursor Skills Updated.'"
```

2. 동기화 및 등록 확인
```bash
# 글로벌 워크플로우 등록 현황 확인
ls c:\Users\nihil\.gemini\antigravity\global_workflows
```

3. 완료 메시지
통합 동기화 및 글로벌 등록이 완료되었습니다!
- **커맨드화**: 이제 어디서든 `/pdca`, `/code-review` 등을 즉시 사용 가능합니다.
- **Cursor**: bkit 스킬셋이 Cursor 에이전트에도 동기화되었습니다.
- **최신화**: 모든 템플릿과 스킬 원본이 글로벌 표준으로 정렬되었습니다.

- **📊 bkit Feature Usage**
    - ✅ **Used**: bkit-sync, Global Workflow Promotion, PowerShell Automation
    - ⏭️ **Not Used**: /bkit-init (전역 설정이 완료되었으므로 로컬 초기화 없이 즉시 사용 가능)
    - 💡 **Recommended**: 이제 어떤 프로젝트에서든 슬래시 커맨드를 바로 입력해 보세요!
