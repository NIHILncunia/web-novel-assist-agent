# bkit 명령어 총정리 (Cheat Sheet)

## 1. 모든 명령어 목록 (All Commands)

### PDCA (개발 사이클)
| 명령어 | 설명 |
| :--- | :--- |
| `/pdca plan [기능명]` | **계획 문서** 생성 (01-plan). 여기서부터 시작하세요. |
| `/pdca design [기능명]` | **설계 문서** 생성 (02-design). 구체적인 구현 방법을 정의합니다. |
| `/pdca do [기능명]` | **구현 실행**. 설계대로 코드를 작성합니다. |
| `/pdca analyze [기능명]` | **검증 (Check)**. 설계 vs 구현 차이를 분석합니다. |
| `/pdca iterate [기능명]` | **반복 개선**. 검증 점수가 낮으면 자동으로 수정합니다. |
| `/pdca report [기능명]` | **완료 보고**. 작업을 마무리하고 보고서를 씁니다. |
| `/pdca archive [기능명]` | 문서 정리. 완료된 문서를 아카이브로 옮깁니다. |
| `/pdca status` | 현재 진행 상황 확인. |
| `/pdca next` | 다음 단계 추천. |

### 프로젝트 초기화 (Init)
| 명령어 | 설명 |
| :--- | :--- |
| `/starter init [이름]` | 정적 웹 (HTML/CSS/JS) 프로젝트 생성. |
| `/dynamic init [이름]` | 풀스택 (Next.js + Supabase) 프로젝트 생성. |
| `/enterprise init [이름]` | 마이크로서비스 (MSA) 엔터프라이즈 프로젝트 생성. |

### 개발 파이프라인 (Phase 1~9)
| 명령어 | 설명 |
| :--- | :--- |
| `/development-pipeline` | 전체 9단계 파이프라인 가이드 보기. |
| `/phase-1-schema` | 데이터 모델링 및 스키마 설계. |
| `/phase-2-convention` | 코딩 컨벤션 및 룰 설정. |
| `/phase-3-mockup` | UI/UX 목업 및 와이어프레임. |
| `/phase-4-api` | 백엔드 API 설계. |
| `/phase-5-design-system` | 디자인 시스템 및 컴포넌트 구축. |
| `/phase-6-ui-integration` | UI 구현 및 API 연동. |
| `/phase-7-seo-security` | SEO 최적화 및 보안 점검. |
| `/phase-8-review` | 코드 리뷰 및 아키텍처 점검. |
| `/phase-9-deployment` | 배포 및 CI/CD 설정. |

### 플랫폼 특화
| 명령어 | 설명 |
| :--- | :--- |
| `/mobile-app` | 모바일 앱 (React Native, Flutter) 가이드. |
| `/desktop-app` | 데스크탑 앱 (Electron, Tauri) 가이드. |

### 유틸리티 & 품질
| 명령어 | 설명 |
| :--- | :--- |
| `/code-review [경로]` | 지정한 코드에 대한 심층 리뷰. |
| `/zero-script-qa` | 테스트 스크립트 없는 로그 기반 QA. |
| `/qa` | QA 모니터링 실행. |
| `/skill-creator` | 새로운 커스텀 스킬 만들기. |
| `/learn` | Gemini CLI 학습 가이드. |
| `/learn setup` | 프로젝트 설정 최적화. |
| `/bkit` | bkit 전체 도움말 표시. |

---

## 2. 작업 순서 (Workflow)

가장 효율적인 작업 흐름입니다.

1.  **시작:** `/pdca plan [기능명]`
    *   *목표를 먼저 정합니다.*
2.  **설계:** `/pdca design [기능명]`
    *   *어떻게 만들지 그립니다.* (필요시 `/phase-1`~`/phase-9` 명령어 참조)
3.  **구현:** `/pdca do [기능명]`
    *   *실제 코드를 짭니다.*
4.  **검증:** `/pdca analyze [기능명]`
    *   *제대로 됐는지 확인합니다.*
5.  **보완:** `/pdca iterate [기능명]` (필요시)
    *   *부족하면 고칩니다.*
6.  **종료:** `/pdca report [기능명]`
    *   *끝내고 보고합니다.*

---

## 3. 마스터를 위한 팁 (Tips)

- **순서가 헷갈리면?** 무조건 `/pdca status`를 치세요. 현재 위치를 알려줍니다.
- **막혔을 때?** `/pdca next`를 치세요. 에이전트가 갈 길을 알려줍니다.
- **새 프로젝트?** `/starter`, `/dynamic`, `/enterprise` 중 하나로 시작하면 기본 뼈대를 다 잡아줍니다.
- **데이터가 중요해?** `/phase-1-schema`를 적극 활용하세요. 데이터 구조가 튼튼해야 나중에 고생 안 합니다.
