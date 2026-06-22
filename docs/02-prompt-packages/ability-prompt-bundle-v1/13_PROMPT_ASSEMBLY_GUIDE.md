# 프롬프트 조립 가이드

이 패키지는 상황에 따라 필요한 프롬프트만 붙여 쓰도록 설계한다.

## 1. 최소 조립

가벼운 브레인스토밍용:

1. `00_MASTER_PROMPT.md`
2. `01_LAYER_OPTIONS.md`
3. `04_LINEAGE_OPTIONS.md`
4. `05_FORM_OPTIONS.md`
5. `06_EFFECT_OPTIONS.md`
6. `12_OUTPUT_TEMPLATE.md`

## 2. 세계관 맞춤 조립

연출 어조와 원천이 중요한 경우:

1. `00_MASTER_PROMPT.md`
2. `02_EXPRESSION_DOMAIN_OPTIONS.md`
3. `03_SOURCE_OPTIONS.md`
4. `04_LINEAGE_OPTIONS.md`
5. `05_FORM_OPTIONS.md`
6. `06_EFFECT_OPTIONS.md`
7. `12_OUTPUT_TEMPLATE.md`

## 3. 밸런싱 조립

실제 시스템 설계나 게임 룰 반영용:

1. `00_MASTER_PROMPT.md`
2. `01_LAYER_OPTIONS.md`
3. `02_EXPRESSION_DOMAIN_OPTIONS.md`
4. `03_SOURCE_OPTIONS.md`
5. `04_LINEAGE_OPTIONS.md`
6. `05_FORM_OPTIONS.md`
7. `06_EFFECT_OPTIONS.md`
8. `07_ACTIVATION_OPTIONS.md`
9. `08_DURATION_OPTIONS.md`
10. `09_COST_OPTIONS.md`
11. `10_RISK_OPTIONS.md`
12. `11_TAG_OPTIONS.md`
13. `12_OUTPUT_TEMPLATE.md`

## 4. 추천 운용 방식

1. 처음에는 마스터 프롬프트와 핵심 선택지 몇 개만 붙여서 넓게 브레인스토밍한다.
2. 마음에 드는 구조가 나오면 비용, 리스크, 태그 프롬프트를 추가해 정제한다.
3. 최종적으로는 출력 템플릿을 붙여 결과물을 일정한 포맷으로 고정한다.

## 5. 이식 팁

1. 다른 프로젝트에서는 이 폴더 전체를 복사해도 된다.
2. 세계관 전용 어휘가 필요하면 `03_SOURCE_OPTIONS.md`, `11_TAG_OPTIONS.md`만 별도 확장하면 된다.
3. 장르 전용 룰이 생기면 마스터 프롬프트를 바꾸기보다 추가 프롬프트를 한 장 더 만드는 편이 안전하다.
