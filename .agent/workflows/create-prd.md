---
description:# /create-prd: 프로젝트 초기화 및 PRD 관리

> **Purpose**: bkit 표준에 따라 새로운 프로젝트를 초기화하거나 기존 PRD를 갱신합니다.

---

## 🛠️ Step-by-Step

### 1. 요구사항 분석 및 정보 수집
- **Context Search**: 프로젝트 루트에 `PRD/` 폴더가 있는지 확인합니다.
- **Goal**: 마스터의 요청을 분석하여 신규 프로젝트인지 기존 프로젝트 갱신인지를 판단합니다.

### 2. 프로젝트 수준(Level) 결정
- 규모에 따라 **Starter**, **Dynamic**, **Enterprise** 수준을 제안하고 마스터의 확답을 받습니다.

### 3. PRD 문서 셋업 (PRD/ 폴더)
`PRD/` 폴더 내에 프로젝트 사양과 규칙을 담은 핵심 3종 문서를 생성/갱신합니다.

1.  **PRD.md**: 프로젝트 개요, 핵심 목표, 상세 사양.
2.  **Coding-Rules.md**: 기술 스택 및 코딩 컨벤션.
3.  **Task-List.md**: 전체 개발 태스크 리스트 및 상태 관리.

### 4. 활동 기록 셋업 (docs/ 폴더)
`docs/` 폴더 하위에 PDCA 사이클별 관리 폴더를 생성합니다.
- `01-plan/`, `02-design/`, `03-analysis/`, `04-report/`

### 5. 로컬 규칙 생성
`.cursorrules` 및 `.agent/rules/` 하위에 프로젝트 로컬 규칙을 생성하여 에이전트 행동을 고정합니다.

---

## 📁 저장 규칙
- **PRD 자산**: 반드시 `PRD/` 폴더 내 저장.
- **날짜 포함**: 신규 문서 생성 시 파일명에 `YYYY-MM-DD` 포함.

---

**📊 bkit Feature Usage**
- ✅ **Used**: `/create-prd`
- ⏭️ **Not Used**: `None`
- 💡 **Recommended**: `/pdca plan {feature}`

# [Templates]

## Document 1: PRD (Product Requirements Document)
**(파일명 예시: `2024-05-20-PRD.md`)**

### 1. Project Overview
* **Project Name**: [프로젝트명]
* **bkit Level**: [Starter / Dynamic / Enterprise]
* **Goal**: [핵심 목표와 비전]
* **Target User**: [구체적 페르소나]
* **Key Value**: [핵심 가치]

### 2. Tech Stack & Environment (Specific Versions)
* **Framework**: [예: Next.js v14+ (App Router)]
* **Language**: TypeScript v5+ (Strict Mode)
* **Start Command**: [예: `npm run dev`]
* **Styling**: [예: TailwindCSS v3.4]
* **State Management**: [예: Zustand v4]
* **Backend/DB**: [Level에 따라 작성. 예: Supabase, Firebase, or None]
* **Infra**: [예: Vercel]

### 3. Core Features & User Flow
#### 3.1. User Flow
* **Flow**: [진입 -> 행동 -> 결과 흐름]

#### 3.2. Detailed Features
* **Feature A**: 
    - **Logic**: [상세 로직]
    - **Validation**: [검증 규칙]

### 4. Data Structure (Schema)
*(JSON 또는 ERD, Dynamic/Enterprise 레벨 필수)*
```json
// Example
{
  "id": "uuid",
  "created_at": "timestamp"
}
```

### 5. Non-Functional Requirements & Risks
* **Performance**: [Lighthouse 점수, 로딩 속도 등]
* **Security**: [보안 정책]
* **Risks**: [잠재 리스크 및 대응]

---

## Document 2: Coding Rules & Guidelines
**(파일명 예시: `2024-05-20-Coding-Rules.md`)**

### 1. bkit Standard Architecture
* **Design Pattern**: [예: FSD(Feature-Sliced Design), MVVM 등]
* **Directory Structure**:
*(프로젝트 레벨에 맞는 상세 트리 구조)*
```
src/
├── app/                  # Routing
├── features/             # Business Logic
├── shared/               # UI Kit, Utils
└── entities/             # Domain Models
```

### 2. Naming Conventions (Strict)
* **Files**: `kebab-case` (예: `user-profile.tsx`)
* **Components**: `PascalCase` (예: `UserProfile`)
* **Functions/Vars**: `camelCase`
* **Constants**: `UPPER_SNAKE_CASE`

### 3. Coding Standards
* **TypeScript**: `strict: true`, `no-explicit-any`
* **Error Handling**: 
    - Global Error Boundary 사용
    - API 에러 표준 포맷 정의
* **Computed/State**: 파생 상태는 `useMemo` 등을 적절히 활용
* **Comments**: 복잡한 로직에만 "Why" 위주 주석 작성

---

## Document 3: Development Task List
**(파일명 예시: `2024-05-20-Task-List.md`)**
*(PDCA 사이클 기반 순차적 작성)*

### Phase 1: Environment & Foundation (Plan)
- [ ] **Init**: 프로젝트 생성 알고리즘 (`/starter` or `/dynamic` etc.) 및 Git 초기화
- [ ] **Config**: 환경변수, Lint, Formatter 설정
- [ ] **Base UI**: 공통 레이아웃, 테마, 글로벌 스타일 설정

### Phase 2: Core Domain & Data (Design)
- [ ] **Schema**: DB 및 데이터 모델 설계
- [ ] **API**: API 인터페이스 및 Mocking 정의

### Phase 3: Feature Implementation (Do)
- [ ] **Feature A**: [기능명]
    - [ ] UI 컴포넌트 구현
    - [ ] 로직 및 상태 연동
- [ ] **Feature B**: [기능명]
    - [ ] ...

### Phase 4: Verification & Polish (Check)
- [ ] **QA**: 기능 테스트 및 버그 수정
- [ ] **Refactor**: 코드 품질 개선 (`/code-review` 활용)

### Phase 5: Deployment (Act)
- [ ] **Build**: 프로덕션 빌드 확인
- [ ] **Deploy**: 배포 및 최종 점검

---

# User Input Data
1. **User Idea**: [사용자가 입력한 아이디어/요구사항]
2. **Context**: [대화 맥락에서 파악된 추가 정보]

# Command
위 **User Input Data**를 바탕으로, **[Templates]** 내용을 완벽하게 구체화하여 작성하시오.
- **필수**: 루트 디렉토리에 `PRD` 폴더와 `docs` 폴더를 생성(없으면)하고, 그 안에 **오늘 날짜가 포함된** 3가지 파일을 저장하십시오.
    1. `docs/YYYY-MM-DD-PRD.md` (예: `docs/2024-05-20-PRD.md`)
    2. `docs/YYYY-MM-DD-Coding-Rules.md` 
    3. `docs/YYYY-MM-DD-Task-List.md`
- 날짜 형식은 **반드시** `YYYY-MM-DD` (예: 2024-05-20)여야 합니다.
- 모든 내용은 **한글**로 작성하십시오.