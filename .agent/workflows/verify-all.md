---
description: 모든 프로세스 (0-10) 순차 검증
---
# 모든 프로세스 검증 (Verify All Processes)

이 워크플로우를 사용하여 Step 0부터 Step 10까지의 모든 프로세스를 체계적으로 검증합니다.

## Steps

1.  **프로세스 0 검증 (아이디어 발상)**
    - `/verify-process` 로직을 `process_id=0`으로 실행합니다.

2.  **프로세스 1 검증 (스타일 설정)**
    - `/verify-process` 로직을 `process_id=1`로 실행합니다.

3.  **프로세스 2 검증 (캐릭터)**
    - `/verify-process` 로직을 `process_id=2`로 실행합니다.

4.  **프로세스 3 검증 (로그라인)**
    - `/verify-process` 로직을 `process_id=3`로 실행합니다.

5.  **프로세스 4 검증 (시놉시스)**
    - `/verify-process` 로직을 `process_id=4`로 실행합니다.

6.  **프로세스 5 검증 (세계관)**
    - `/verify-process` 로직을 `process_id=5`로 실행합니다.

7.  **프로세스 6 검증 (스토리 아크)**
    - `/verify-process` 로직을 `process_id=6`로 실행합니다.

8.  **프로세스 7 검증 (챕터 계획)**
    - `/verify-process` 로직을 `process_id=7`로 실행합니다.

9.  **프로세스 8 검증 (최종 검토)**
    - `/verify-process` 로직을 `process_id=8`로 실행합니다.

10. **프로세스 9 검증 (집필)**
    - `/verify-process` 로직을 `process_id=9`로 실행합니다.

11. **프로세스 10 검증 (퇴고)**
    - `/verify-process` 로직을 `process_id=10`로 실행합니다.

12. **최종 요약**
    - 모든 프로세스 검증 완료를 사용자에게 알립니다.
    - 각 단계에서 발견된 모든 실패 사항을 요약하여 제공합니다.
