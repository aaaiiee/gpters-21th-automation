---
title: "04 File Discovery"
summary: "번호가 바뀐 번들 참고 문서를 역할과 단계 기준으로 다시 찾는 규칙"
---

# File Discovery

## 원칙

- 숫자보다 파일명 핵심 부분을 우선합니다.
- 먼저 스크립트로 현재 번들 문서 매핑을 확인합니다.
- 기본 명령은 전체 역할 매핑을, `--stage` 명령은 현재 단계에 필요한 정본/보조 문서를 좁혀서 보여줍니다.
- 아래 표의 역할명은 스크립트 내부 식별자이며, 사용자 설명에서는 역할 의미를 우선합니다.
- `.security.md` 같은 스캔 산출물은 문서 정본 후보에서 제외합니다.

```powershell
python .claude\skills\_education_skills_중급\automation-pipeline-design-eduv-중급\scripts\find_gpters_study_docs.py
```

지원 단계 목록이 필요하면:

```powershell
python .claude\skills\_education_skills_중급\automation-pipeline-design-eduv-중급\scripts\find_gpters_study_docs.py --list-stages
```

## 단계별 사용 방법

| 단계 | 명령 | 현재 단계 정본 역할 | 보조 역할 |
|---|---|---|---|
| 의도 확인 | `python ...\find_gpters_study_docs.py --stage intent` | `flow_reference` | `hub`, `student_guide` |
| 인터뷰 | `python ...\find_gpters_study_docs.py --stage interview` | `interview` | `hub`, `flow_reference`, `student_guide` |
| 워크시트 | `python ...\find_gpters_study_docs.py --stage worksheet` | `worksheet` | `interview`, `hub`, `student_guide` |
| 자동화 설계 | `python ...\find_gpters_study_docs.py --stage automation_design` | `workflow_rules_template` | `workflow_rules_sample`, `worksheet`, `interview`, `flow_reference` |
| 도구 연결 | `python ...\find_gpters_study_docs.py --stage tool_connection` | 없음 | `workflow_rules_template`, `workflow_rules_sample`, `student_guide`, `flow_reference` |
| 오케스트레이션 실행 및 결과 확인 | `python ...\find_gpters_study_docs.py --stage orchestration_execution` | `student_guide` | `workflow_rules_sample`, `flow_reference`, `hub` |
| Agent 변환 | `python ...\find_gpters_study_docs.py --stage agent_conversion` | 없음 | `student_guide`, `workflow_rules_template`, `workflow_rules_sample`, `flow_reference` |

정본 역할이 `NOT FOUND`면 누락 상태를 먼저 보고합니다. 번호를 추정하지는 않지만, 현재까지 확보한 산출물과 보조 문서를 기준으로 단계 진행은 계속합니다.

## 중급 검색 키워드

| 문서 역할 | 키워드 |
|---|---|
| 전체 플로우 도식화 | `업무자동화`, `전체-플로우-도식화` |
| 허브 | `인터뷰및자동화룰`, `생성방법` |
| 인터뷰 | `업무정의-자동화-위임설계서-인터뷰` |
| 워크시트 | `업무정의-자동화-위임설계서-인터뷰-워크시트` |
| 자동화 설계 참고 템플릿 | `workflow_rules`, `작성` |
| 자동화 설계 참고 샘플 | `workflow_rules`, `sample` |
| 사용자용 실행 가이드 | `학생용-사용법-및-실행-설명서` |

## 관련 문서

- [01_stage-map.md](./01_stage-map.md)
- [03_interaction-protocol.md](./03_interaction-protocol.md)
