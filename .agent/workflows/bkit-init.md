---
description: 글로벌 bkit 자산(템플릿)을 현재 워크스페이스로 가져와 초기화합니다.
---

이 워크플로우는 글로벌에 설정된 bkit 환경을 개별 프로젝트와 연결합니다. 이제 스킬들이 글로벌 워크플로우로 존재하므로, 로컬 프로젝트에서는 문서 템플릿 구성 위주로 가볍게 초기화합니다.

// turbo
1. 워크스페이스 초기화 및 템플릿 배포 (Windows PowerShell)
```bash
# 워크스페이스 내 필수 구조 생성
powershell -Command "$targetDir = '.agent\templates'; if (-not (Test-Path $targetDir)) { New-Item -ItemType Directory -Path $targetDir -Force }"

# 글로벌 템플릿 로컬 프로젝트로 배포
powershell -Command "$globalTemplatesDir = 'c:\Users\nihil\.gemini\antigravity\templates'; $targetDir = '.agent\templates'; if (Test-Path $globalTemplatesDir) { Copy-Item -Path ($globalTemplatesDir + '\*') -Destination $targetDir -Recurse -Force; Write-Host 'Local Templates Ready.' }"
```

2. 설치 완료
이제 로컬 프로젝트에서도 bkit의 표준 템플릿을 활용할 준비가 되었습니다!
또한 글로벌 워크플로우 덕분에 아래 커맨드를 즉시 사용하실 수 있습니다.

- `/pdca plan [기능명]`: 신규 기능 개발 시작
- `/bkit-start`: bkit 시작 가이드 확인

- **📊 bkit Feature Usage**
    - ✅ **Used**: bkit-init, Global Workflow Linkage
    - ⏭️ **Not Used**: /bkit-sync (프로젝트 로컬 최적화만 수행)
    - 💡 **Recommended**: `/pdca plan`으로 첫 기획을 시작해 보세요.
