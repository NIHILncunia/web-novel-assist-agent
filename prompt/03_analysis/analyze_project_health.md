---
description: 프로젝트의 건강 상태를 종합적으로 분석하여 깨진 링크, 누락된 파일, 잠재적 문제를 확인합니다.
---

# 프로젝트 건강 진단 프롬프트 (Project Health Check Prompt)

> **목적:** 프로젝트의 파일 구조, 내부 링크, 리소스 참조의 무결성을 체계적으로 검증합니다. 이는 리팩토링 과정에서 문서 간의 연결이 끊어지는 "맥락 부패(Context Rot)" 현상을 방지하기 위함입니다.

## 1. 사전 준비 (Pre-requisites)
- `tools/verify_links.py` 스크립트가 존재해야 합니다.
- Python 실행 환경(uv)이 준비되어 있어야 합니다.

## 2. 실행 단계 (Execution Steps)

### Step 1: 링크 검증 실행 (Run Link Verification)
다음 명령어를 실행하여 모든 마크다운 파일(`manuals/`, `prompt/`, `_templates/`) 내의 깨진 상대 경로 및 절대 경로를 스캔하십시오.

```bash
uv run python tools/verify_links.py
```

### Step 2: 출력 분석 (Analyze Output)
스크립트는 `[SourceFile] -> 'TargetPath' (Reason)` 형식으로 깨진 링크 목록을 출력합니다.
다음 카테고리를 기준으로 오류를 분석하십시오:
1.  **리팩토링 잔재:** 이전 경로를 참조하는 경우 (예: 파일이 `manuals/05-00...`으로 이동했으나 여전히 `manuals/04-00...`을 참조).
2.  **자산 누락 (Missing Assets):** 생성되지 않은 이미지나 파일을 참조하는 경우.
3.  **인코딩 문제:** 경로에 깨진 문자가 포함된 경우 (예: `data/ų.md`).
4.  **논리적 공백:** 존재해야 하지만 실제로는 없는 파일 참조 (예: 특정 템플릿 파일).

### Step 3: 리포트 생성 (Report Generation)
`report/` 폴더에 `YYYY-MM-DD_시스템_건강_진단_리포트.md`와 같은 이름으로 새 리포트를 생성(또는 업데이트)하십시오.
리포트에는 다음 내용이 포함되어야 합니다:
- **요약:** 발견된 깨진 링크의 총 개수.
- **치명적 문제:** 핵심 워크플로우를 차단하는 오류 (예: 존재하지 않는 매뉴얼을 가리키는 프롬프트).
- **조치 계획:** 링크를 수정하기 위해 구체적으로 수정해야 할 파일 목록.

## 3. 자가 수정 가이드 (Self-Correction Guide)
- `data/word_list/` 내에서 `fantasy.md`에 대한 참조가 발견되면, 이것이 `fantasy/판타지_용어.md` 등을 가리켜야 하는지 확인하십시오.
- `manuals/04-*` 패턴의 참조가 보이면, 이는 현재 구조인 `manuals/05-*`로 매핑되어야 합니다.
