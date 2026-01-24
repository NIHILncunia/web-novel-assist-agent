---
name: analyze_project
description: Check project health for broken links, missing files, and potential issues using verify_links.py.
---

# 기능: 프로젝트 건강 진단 (`analyze_project`)

프로젝트의 파일 구조, 내부 링크, 리소스 참조의 무결성을 체계적으로 검증합니다. "맥락 부패" 방지 목적.

## 1. 개요 및 사전 준비

- **목적:** 깨진 링크 및 누락된 에셋 확인.
- **도구:** `tools/verify_links.py` (Python)
- **실행 환경:** `generate_shell_command`를 통해 `uv run python tools/verify_links.py` 실행.

## 2. 작업 프로세스

### Step 1: 링크 검증 실행
- 명령: `uv run python scripts/verify_links.py`
- 모든 마크다운 파일 스캔.

### Step 2: 출력 분석
- **오류 분류:**
  1. 리팩토링 잔재 (구 경로 참조)
  2. 자산 누락 (이미지 등)
  3. 인코딩 문제
  4. 논리적 공백 (템플릿 누락)

### Step 3: 리포트 생성
- 위치: `report/YYYY-MM-DD_시스템_건강_진단_리포트.md`
- 내용: 요약, 치명적 문제, 조치 계획.

## 3. 자가 수정 가이드
- `manuals/04-*` -> `manuals/05-*` 매핑 확인 등.
