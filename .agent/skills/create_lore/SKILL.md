---
name: create_lore
description: Create Legends, Myths, Folktales, or Rumors (Lore) that influence the story. Covers Core Story, Transmission, Truth, and Current Impact. Saves to `00_bible/08_stories/`.
---

# 기능: 전설 및 신화 생성 (`create_lore`)

이 어빌리티는 세계관 내에 구전되는 **전설, 신화, 민담, 야사** 등을 설계하는 지침입니다. 단순한 옛날 이야기가 아니라, 현재의 서사에 영향(믿음, 복선, 떡밥)을 주는 요소를 생성합니다. '역사적 사실(History)'이 아닌 **'이야기(Story/Lore)'**를 다룹니다.

## 1. 개요 및 저장 위치

- **저장 위치:** `00_bible/08_stories/`
- **파일명:** `전설_[이름].md` 또는 `신화_[이름].md`
- **템플릿:** `templates/08_stories_template.md`

## 2. 인터뷰 프로세스 (5 Axes)

### Axis 1. 유형 (Type)
- **질문:** "이 이야기는 어떤 형태입니까?"
- **옵션:** 창세 신화, 영웅 전설, 민담, 저주/금기, 예언, 괴담

### Axis 2. 핵심 내용 (Core Story)
- **질문:** "이야기의 줄거리는 무엇입니까?"
- **요소:** 주인공(신/영웅), 주요 사건, 교훈/결말

### Axis 3. 전승 방식 및 왜곡 (Transmission)
- **질문:** "어떻게 전해지며, 얼마나 믿을만 합니까?"
- **수단:** 구전, 경전, 금서
- **신뢰도:** 절대적 진실 vs 헛소문
- **왜곡:** 변질된 부분

### Axis 4. 진실 (The Truth)
- **질문:** "실제 진실은 무엇입니까? (마스터와 에이전트만 아는 비밀)"
- **Pack:** 전설과 정반대이거나 과장됨.

### Axis 5. 현재 영향 (Current Impact)
- **질문:** "이 이야기가 현재 시점의 주인공이나 세상에 어떤 영향을 줍니까?"
- **문화:** 축제, 관습, 속담
- **플롯:** 수수께끼, 유물 위치, 피해야 할 장소

## 3. 데이터 저장 지침

1. **템플릿:** `templates/08_stories_template.md` 사용.
2. **저장:** `00_bible/08_stories/[Lore_Name].md`.
