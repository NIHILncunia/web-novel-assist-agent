# [Report] 프로세스 {{process_id}} ({{process_name}}) 모의 점검 결과

> **작성일:** {{date}}
> **점검 대상:** Step {{process_id}} {{process_name}} 프로세스

## 1. 개요
본 보고서는 `manuals/{{manual_filename}}`를 시작점으로 하는 'Step {{process_id}}: {{process_name}}' 단계의 워크플로우를 모의 주행하며, 참조된 모든 파일과 폴더의 경로가 유효한지 검증한 결과를 담고 있습니다.

## 2. 검증 결과 요약
- **총 점검 항목:** {{total_count}}개 (파일 {{file_count}}개, 폴더 {{folder_count}}개)
- **유효 경로:** {{valid_count}}개 ({{valid_percent}}%)
- **누락/오류:** {{error_count}}개 ({{error_percent}}%)
- **판정:** **{{pass_fail_status}}**

## 3. 상세 점검 내역

### 3.1. 매뉴얼 (Manuals)
| 구분 | 파일 경로 | 상태 | 비고 |
| :--- | :--- | :---: | :--- |
| **메인 매뉴얼** | `manuals/{{manual_filename}}` | ✅ **유효** / ❌ **누락** | 프로세스 진입점 |

### 3.2. 템플릿 (Templates)
| 구분 | 파일 경로 | 상태 | 비고 |
| :--- | :--- | :---: | :--- |
| **{{template_name}}** | `_templates/Sheets/{{template_filename}}` | ✅ **유효** / ❌ **누락** | {{template_description}} |

### 3.3. 프롬프트 및 데이터 (Prompts & Data)
| 구분 | 파일 경로 | 상태 | 비고 |
| :--- | :--- | :---: | :--- |
| **{{resource_name}}** | `{{resource_path}}` | ✅ **유효** / ❌ **누락** | {{resource_description}} |

### 3.4. 에이전트 스킬 (Agent Skills)
| 구분 | 스킬명 (폴더) | SKILL.md 상태 | 템플릿 상태 | 비고 |
| :--- | :--- | :---: | :---: | :--- |
| **{{skill_name}}** | `.agent/skills/{{skill_folder}}` | ✅ **유효** / ❌ **누락** | ✅ **유효** / ❌ **누락** | {{skill_function}} |

### 3.5. 공통 요소 (Common)
| 구분 | 파일 경로 | 상태 | 비고 |
| :--- | :--- | :---: | :--- |
| **로그 시스템** | `manuals/99_common_logger.md` | ✅ **유효** | 대화 기록 지침 |

## 4. 결론
{{conclusion_text}}
