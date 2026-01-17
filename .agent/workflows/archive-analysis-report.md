---
description: 분석 리포트 완료 처리 및 아카이빙
---

1. 사용자로부터 완료 처리할 리포트 파일의 경로를 확보합니다. (예: `report/concept_analyze/character/Fate_Zero_Rider.md`)
2. `view_file` 도구를 사용하여 해당 리포트의 내용을 읽습니다.
3. 리포트 내용 상단의 메타데이터 블록을 수정합니다.
   - `> **상태:** [작성 중 등]` 부분을 `> **상태:** 완료 (Archived)` 로 변경합니다.
4. 아카이브 이동 경로를 생성합니다.
   - 규칙: 원본 경로의 루트 앞에 `archive/`를 추가하여 구조를 유지합니다.
   - 예: `report/concept_analyze/character/Fate_Zero_Rider.md` -> `archive/report/concept_analyze/character/Fate_Zero_Rider.md`
5. `write_to_file` 도구를 사용하여 **아카이브 경로(4번에서 생성한 경로)**에 수정된 내용을 저장합니다.
   - `IsArtifact`: false
   - `Overwrite`: false (이미 존재한다면 확인 필요하지만, 보통 새로 생성)
6. 파일이 안전하게 아카이브 경로에 생성되었는지 확인 후, `run_command`를 사용해 원본 파일을 삭제합니다.
   - 명령어: `rm "[원본 파일 절대 경로]"` 
7. 사용자에게 원본 파일이 삭제되고 아카이브 경로로 이동되었음을 `notify_user`로 알립니다.
