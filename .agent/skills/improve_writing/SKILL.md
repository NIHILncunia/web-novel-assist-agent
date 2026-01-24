---
name: improve_writing
description: Analyze and improve specific aspects of the writing such as Consistency, Pacing, and Dialogue.
---

# 기능: 집필 개선 (`improve_writing`)

이 **skills improve_writing**은 작성된 원고의 품질을 높이기 위해 **일관성 검토, 전개 속도 조절, 대사 개선** 등 특정 영역을 집중적으로 분석하고 수정을 제안합니다.

## 1. 개요
- **입력:** 수정할 원고, 관련 설정(캐릭터 시트 등).
- **출력:** 수정 제안, 전후 비교, 비평 리포트.

## 2. 작업 모드 (Modes)

### Mode 1: 일관성 검토 (Consistency)
- **목적:** 캐릭터, 세계관, 이전 줄거리와의 모순 발견.
- **기준:** [Bible 설정] 및 [이전 회차 요약(`templates/episode_sheet.md`)] 대조.
- **출력:** 오류 위치, 문제점 번호, 참고 설정, 수정 제안.

### Mode 2: 전개 속도 조절 (Pacing)
- **목적:** 몰입도 조절 (Speed Up / Slow Down).
- **기준:** 행동 중심 vs 감정/묘사 중심 서술 제어.
- **출력:** 수정된 원고 구간, 변경점 요약.

### Mode 3: 대사 개선 (Dialogue)
- **목적:** 캐릭터 개성 강화 (Show, Don't Tell).
- **기준:** 캐릭터 시트(말투, 성격) 반영.
- **출력:** 수정 전/후 대사 비교, 의도 설명.

## 3. 실행 프로세스
1. **모드 선택:** 사용자의 요청에 따라 모드(일관성/속도/대사)를 결정합니다.
2. **컨텍스트 로드:** 관련 Bible 파일 및 원고를 읽습니다. (필요 시 `view_file` 활용)
3. **분석 및 제안:** 각 모드의 가이드라인에 따라 분석하고 수정안을 제시합니다.
