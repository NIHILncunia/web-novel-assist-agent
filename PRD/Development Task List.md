# Development Task List (Trait DB Standardization)

본 문서는 트레잇 데이터베이스 정규화 프로젝트의 단계별 작업 목록을 정의합니다.

### Phase 1: Analysis & Foundation (분석 및 기반)
- [x] **Snapshot Analysis**: 현재 `data/traits` 디렉토리의 파일 목록 및 규모 분석 (완료)
- [x] **Rule Definition**: 모호한 분류 기준(정신 vs 관계 등)에 대한 명확한 가이드라인(`Coding Rules & Guidelines.md`) 작성 (완료)
- [ ] **Python Setup**: 데이터 검증을 위한 Python 스크립트 개발 환경 구성 (`scripts/check_traits.py`)

### Phase 2: Refactoring (데이터 재구조화)
- [x] **Category Separation**: `10_정신.md`가 너무 비대하므로(430+), **`17_관계.md`** 파일을 신규 생성하여 관계형 트레잇을 전면 이관한다.
    - [x] `10_정신` 내 '관계', '소셜', '상호작용' 태그 데이터 필터링
    - [x] `17_관계.md` 생성 및 데이터 이동
- [x] **Ambiguity Resolution**: 모호한 트레잇 재배치
    - [x] `03_신체` vs `16_전투` 경계에 있는 트레잇 검토 (예: '재생력'은 신체, '전투 재생'은 전투?)
    - [x] `00_유형` 내의 중복되거나 너무 구체적인 몬스터 이름 정리 (특이사항 없음)
- [x] **Format Normalization**: 모든 `.md` 파일의 테이블 포맷 통일
    - [x] Pipe(`|`) 정렬
    - [x] 분류(Category) 컬럼값 표준화 (예: '정신' -> 'Mind' 등으로 내부 코드화 할지 결정)

### Phase 3: Expansion (확장 및 보강)
- [x] **Attribute Expansion**: `15_속성.md` 데이터 확충 (현재 32개 -> 목표 50개 이상)
    - [x] 복합 속성(예: 빙결+화염) 및 추상적 속성(공허, 혼돈 등) 추가
- [x] **New Category**: 필요 시 새로운 카테고리 신설
    - [-] `18_서사.md` (Narrative): 생성 취소 (사용자 요청)
    - [x] `19_직업.md` (Class/Role): 전사, 마법사 등 직업적 정체성 트레잇

### Phase 4: Verification & Automation (검증 및 자동화)
- [ ] **Lint Script Development**: `verify_traits.py` 제작
    - [ ] **Duplicate Check**: 전체 파일 대상 키워드 중복 검사 기능
    - [ ] **Format Check**: 마크다운 테이블 문법 오류 검사
    - [ ] **Report Generation**: 오류 리포트 자동 생성 (`logs/trait_error_log.txt`)
- [ ] **Final Review**: 마스터와 함께 재구성된 데이터베이스 최종 점검
    - [ ] 분류 적절성 확인
    - [ ] 신규 추가된 트레잇 퀄리티 확인

### Phase 5: Ability Tagging & Analysis (어빌리티 태그화 및 분석)
- [x] **Physical Realm Analysis**: 물리 권역 어빌리티 태그 분석 및 프로토콜 작성 (완료)
- [x] **Magic Realm Extraction**: 마법 권역 어빌리티 설명 추출 (완료)
- [x] **Magic Realm Tagging**: 마법 권역 어빌리티 태그 추출 및 프로토콜 업데이트 (완료)

### Phase 6: Documentation
- [ ] **Update Manual**: `manuals/` 내의 관련 문서 업데이트 (트레잇 데이터 활용법 등)
- [ ] **Archive**: 구버전 데이터 백업 및 아카이빙
