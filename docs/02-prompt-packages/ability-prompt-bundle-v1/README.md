# 어빌리티 프롬프트 번들 v1

> 목적: 보편 어빌리티 문법 v2를 다른 프로젝트나 다른 에이전트에 쉽게 이식할 수 있도록, 하나의 거대한 프롬프트가 아니라 역할별 프롬프트 묶음으로 분리한 패키지.

---

## 구성

1. `00_MASTER_PROMPT.md`
   - 어빌리티 포맷, 핵심 원칙, 필수 규칙, 출력 스키마
2. `01_LAYER_OPTIONS.md`
   - 층위 선택지
3. `02_EXPRESSION_DOMAIN_OPTIONS.md`
   - 표현 권역 선택지
4. `03_SOURCE_OPTIONS.md`
   - 원천 대분류 및 세부 원천 후보
5. `04_LINEAGE_OPTIONS.md`
   - 계통 선택지
6. `05_FORM_OPTIONS.md`
   - 형태 선택지
7. `06_EFFECT_OPTIONS.md`
   - 효과 선택지
8. `07_ACTIVATION_OPTIONS.md`
   - 발동 방식 선택지
9. `08_DURATION_OPTIONS.md`
   - 지속 방식 선택지
10. `09_COST_OPTIONS.md`
   - 비용 선택지
11. `10_RISK_OPTIONS.md`
   - 리스크 선택지
12. `11_TAG_OPTIONS.md`
   - 태그 규칙 및 태그 후보
13. `12_OUTPUT_TEMPLATE.md`
   - 최종 출력 템플릿
14. `13_PROMPT_ASSEMBLY_GUIDE.md`
   - 어떤 상황에 어떤 프롬프트를 붙일지에 대한 조립 가이드

---

## 최소 사용법

가장 단순한 사용은 아래 3개만 붙이면 된다.

1. `00_MASTER_PROMPT.md`
2. 필요한 선택지 파일 2~5개
3. `12_OUTPUT_TEMPLATE.md`

예:

- 신체 재생 능력 생성:
  - `00_MASTER_PROMPT.md`
  - `01_LAYER_OPTIONS.md`
  - `03_SOURCE_OPTIONS.md`
  - `04_LINEAGE_OPTIONS.md`
  - `05_FORM_OPTIONS.md`
  - `06_EFFECT_OPTIONS.md`
  - `12_OUTPUT_TEMPLATE.md`

- 태그까지 엄격히 붙이는 생성:
  - 위 파일들
  - `11_TAG_OPTIONS.md`

- 밸런싱까지 보는 생성:
  - 위 파일들
  - `07_ACTIVATION_OPTIONS.md`
  - `08_DURATION_OPTIONS.md`
  - `09_COST_OPTIONS.md`
  - `10_RISK_OPTIONS.md`

---

## 권장 원칙

1. 마스터 프롬프트는 항상 포함한다.
2. 선택지 프롬프트는 필요한 것만 붙인다.
3. 태그 프롬프트는 검색/분류가 중요할 때만 붙인다.
4. 비용과 리스크 프롬프트는 밸런싱 검토가 필요할 때 우선 붙인다.
5. 최종 응답 형식이 중요하면 반드시 `12_OUTPUT_TEMPLATE.md`를 함께 붙인다.
