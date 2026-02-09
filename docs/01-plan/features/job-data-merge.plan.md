# Plan: 직업 데이터 통합 및 정규화 (job-data-merge)

## 1. 배경 및 목적
- **배경**: 현재 직업 관련 키워드가 `data/word_list/common/직업.md`(현실)와 `data/word_list/fantasy/직업.md`(판타지)로 나뉘어 있어 관리가 불편하고, 트레잇 시스템과의 연동이 부족함.
- **목적**: 모든 직업 키워드를 `data/traits/18_직업.md`로 통합하여 'Single Source of Truth'를 구축하고, 포맷을 트레잇 표준으로 정규화함.

## 2. 주요 과업 (Key Tasks)

### 2.1. 직업 데이터 병합 및 정규화
- **대상**: 
    - `data/word_list/common/직업.md`
    - `data/word_list/fantasy/직업.md`
    - `data/traits/18_직업.md` (기존)
- **내용**: 
    - 중복 키워드 제거.
    - 포맷 변경: `| 키워드 | 분류 | 설명 |` (기존 예문은 설명에 통합하거나 삭제).
    - 카테고리 재분류: 현대 전문직, 가상 전투직, 마법직 등으로 체계화.

### 2.2. 파일 구조 정리
- 병합 완료 후 `word_list` 내의 원본 직업 파일들을 성격에 따라 `traits` 또는 `keyword` 폴더로 이동하거나 정리.
- 불필요한 구버전 파일 삭제.

## 3. 성공 기준 (Success Criteria)
- `data/traits/18_직업.md` 파일 하나로 모든 직업 정보를 조회 가능함.
- `check_traits.py` 실행 시 무결성 검사를 통과함.
- 모든 데이터가 `Coding Rules`의 테이블 포맷을 준수함.

## 4. 일정 및 우선순위
1. **우선순위 High**: `18_직업.md` 통합 및 정규화 (실제 데이터 병합).
2. **우선순위 Medium**: 폴더 구조 정리 및 파일 이동.
