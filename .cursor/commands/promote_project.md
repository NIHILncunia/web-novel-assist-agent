---
description: 인큐베이터의 프로젝트를 정식 프로젝트로 승격(이동)시킵니다.
---

# 프로젝트 승격 (Promote Project)

이 워크플로우는 `incubator/` 폴더에 있는 임시 프로젝트를 `projects/` 폴더로 이동하여 정식 프로젝트로 승격시킵니다.

1. **승격할 프로젝트 확인**
   - 현재 작업 중인 `incubator` 내의 폴더명을 확인합니다.
   - 예: `incubator/무제_판타지_01`

2. **새로운 작품명 입력**
   - 사용자에게 확정된 작품명을 입력받습니다. (이미 입력받았다면 생략)
   - 예: `황금의_기사`

3. **폴더 이동 (Rename/Move)**
   - `incubator/[기존폴더명]`을 `projects/[새작품명]`으로 이동합니다.
   
```bash
# Windows (PowerShell)
Move-Item -Path "incubator/[Old_Name]" -Destination "projects/[New_Name]"
```

4. **완료 메시지**
   - 사용자에게 승격 완료를 알리고, 이후 작업은 `projects/[새작품명]`에서 진행됨을 명시합니다.
