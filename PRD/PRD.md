# PRD: 트레잇 데이터베이스 정규화 및 확장 (Trait DB Standardization)

## 1. Project Overview
*   **Goal**: `novel-assist-agent`의 핵심 자산인 '트레잇(Trait)' 데이터의 분류 기준 모호성을 제거하고, 무한한 확장이 가능한 체계적인 데이터베이스 구조(Schema)와 운영 정책을 수립한다.
*   **Target User**: 
    *   **Primary**: 마스터 (소설 작가) - 일관된 설정으로 캐릭터를 조형하고자 함.
    *   **Secondary**: AI 에이전트 (Gemini) - 모호함 없이 데이터를 검색하고 추천해야 함.
*   **Key Value**:
    *   **Consistency (일관성)**: 중복되거나 모호한 트레잇을 제거하여 설정 충돌 방지.
    *   **Scalability (확장성)**: 새로운 속성이나 개념이 등장해도 기존 체계를 무너뜨리지 않고 추가 가능.
    *   **Usability (사용성)**: 원하는 느낌의 트레잇을 즉시 찾아내거나 조합할 수 있는 검색 효율성.

## 2. Tech Stack & Environment
*   **Data Format**: Markdown Tables (`.md`)
    *   **Reason**: 사람이 읽기 쉽고(Human-readable), AI가 파싱하기에도 용이함.
*   **Validation Tool**: Python Script (Custom Lint)
    *   **Libraries**: `os`, `re` (정규표현식), `pandas` (데이터 분석용, 선택적)
*   **Version Control**: Git (Project Repository 내 포함)

## 3. System Architecture & Features

### 3.1. Data Flow (Workflow)
1.  **Request**: 마스터가 새로운 개념(예: "사이버펑크 임플란트") 추가 요청.
2.  **Analysis**: AI가 해당 개념이 기존 카테고리(00~16)에 속하는지, 새로운 카테고리가 필요한지 분석.
3.  **Validation**: 중복 키워드 존재 여부 확인.
4.  **Insertion**: 정해진 스키마 포맷에 맞춰 데이터 삽입.
5.  **Audit**: 주기적인 스크립트 실행으로 데이터 건전성(무결성) 검사.

### 3.2. Core Features
*   **Feature A: 표준화된 분류 체계 (Categorization Standard)**
    *   **Logic**: 모호한 경계(예: 성격 vs 관계, 신체 vs 전투)를 명확히 정의하는 결정 트리(Decision Tree) 수립.
    *   **Validation**: 하나의 트레잇은 오직 하나의 파일(카테고리)에만 존재해야 한다.
*   **Feature B: 데이터 무결성 검증기 (Consistency Validator)**
    *   **Logic**: 파일명 규칙(`XX_이름.md`), 테이블 컬럼(`이름`, `분류`, `설명`) 준수 여부, 파이프(`|`) 문자 이스케이프 처리 등을 검사.

## 4. Data Structure (Schema)

모든 트레잇 파일은 아래의 Markdown Table 형식을 엄격히 준수한다.

```markdown
# XX. 카테고리명 (English Name)

> **설명:** 이 카테고리에 대한 정의 및 포함 기준.

## 트레잇 목록

| 트레잇 이름 | 하위 분류 | 트레잇 설명 |
| :--- | :---: | :--- |
| **키워드 (영문)** | 세부 태그 | 구체적인 효과 묘사 및 예시 |
```

*   **트레잇 이름**: 한글 표기를 원칙으로 하며, 필요시 `(영문)` 또는 `(한자)`를 병기한다. **굵게(Bold)** 처리한다.
*   **하위 분류**: 해당 카테고리 내에서의 세부 속성 (예: 물리, 마법, 정신 등).
*   **트레잇 설명**: 개조식 문장이 아닌, 서술형 문장으로 마침표(`.`)로 끝맺는다.

## 5. Non-Functional Requirements & Risks
*   **Maintainability**: 파일 용량이 너무 커질 경우(1000라인 이상), 하위 폴더 분리나 파일 분할 규칙을 적용해야 한다.
*   **Ambiguity Risk**: '정신'과 '관계' 처럼 겹칠 수 있는 영역은 **"발원지"**를 기준으로 삼는다. (내면에서 비롯되면 정신, 상호작용이면 관계)
