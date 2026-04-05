---
title: "01 Stage Map"
summary: "중급 사용자 흐름: 인터뷰 -> 워크시트 -> 자동화 설계 -> 도구 연결 -> 오케스트레이션 실행 및 결과 확인 -> Agent 변환. 각 단계 진입 전 문서 매핑기를 다시 확인하고, 인터뷰와 워크시트는 다음 단계로 넘어가기 전 품질 게이트로 취급합니다."
---

# Stage Map

## 중급 흐름

0. 의도 확인 (반드시 먼저 실행)
1. 인터뷰
2. 워크시트
3. 자동화 설계
4. 도구 연결
5. 오케스트레이션 실행 및 결과 확인
6. Agent 변환 (자율 실행 Agent 정의 파일 생성)

## 단계 시작 전 공통 준비

- 각 단계에 들어가기 전에 `find_gpters_study_docs.py --stage <stage>`로 현재 번들 문서 매핑을 다시 확인합니다.
- `<stage>`에는 `intent`, `interview`, `worksheet`, `automation_design`, `tool_connection`, `orchestration_execution`, `agent_conversion` 중 하나를 넣습니다.
- `NOT FOUND`가 나온 정본 역할은 누락 상태를 먼저 보고하고, 번호를 추정해서 진행하지 않습니다.
- 정본 역할이 없어도 현재까지 확보한 산출물과 supporting 문서를 기준으로 단계 진행과 파일 생성은 계속합니다.

| 단계 | 명령 | 현재 단계 정본 역할 |
|---|---|---|
| 의도 확인 | `python ...\find_gpters_study_docs.py --stage intent` | `flow_reference` |
| 인터뷰 | `python ...\find_gpters_study_docs.py --stage interview` | `interview` |
| 워크시트 | `python ...\find_gpters_study_docs.py --stage worksheet` | `worksheet` |
| 자동화 설계 | `python ...\find_gpters_study_docs.py --stage automation_design` | `workflow_rules_template` |
| 도구 연결 | `python ...\find_gpters_study_docs.py --stage tool_connection` | 정본 없음, supporting만 사용 |
| 실행/결과 확인 | `python ...\find_gpters_study_docs.py --stage orchestration_execution` | `student_guide` |
| Agent 변환 | `python ...\find_gpters_study_docs.py --stage agent_conversion` | 정본 없음, supporting만 사용 |

## 단계 게이트

- `의도 확인 -> 인터뷰`: 사용자가 자동화할 업무와 방향(새 업무 / 기존 이어가기 / 복수 묶기)을 명시해야 합니다. 기존 프로젝트가 있어도 자동으로 이어가지 않고 반드시 질문합니다.
- `인터뷰 -> 워크시트`: 필수 인터뷰 항목이 채워졌거나 `[보류: 이유]`가 명시되어야 합니다.
- `워크시트 -> 자동화 설계`: 핵심 섹션이 채워졌고, 제3자가 읽어도 이해 가능한 상태여야 합니다.
- `자동화 설계 -> 도구 연결`: 자동화 단계와 입출력이 분명해야 합니다.
- `도구 연결 -> 실행`: 실제 입력 자료 또는 실행 전제조건이 확인되어야 합니다.
- `실행 -> Agent 변환`: orchestration_run.md가 완성되고 최소 1회 드라이런 결과가 있어야 합니다.
- 후속 단계에서 핵심 공백이 발견되면 이전 단계로 되돌아갑니다.

## 단계별 핵심 산출물

| 단계 | 핵심 산출물 | 다음 단계로 넘기는 조건 |
|---|---|---|
| 의도 확인 | 사용자 의도 확인 결과 | 자동화할 업무와 방향(새 업무/기존 이어가기/복수 묶기)이 명시됨 |
| 인터뷰 | 답변 메모 | 인터뷰 필수 항목이 채워졌거나 `[보류: 이유]`가 명시됨 |
| 워크시트 | 구조화된 초안 | 핵심 섹션이 채워지고 큰 모호점이 정리됨 |
| 자동화 설계 | 자동화 설계 초안 | 자동화 단계, 입출력, 예외가 분명함 |
| 도구 연결 | 도구 연결표 | 실제 도구 연결과 그레이 영역이 구분됨 |
| 실행/결과 확인 | 실행 메모와 결과 요약 또는 실행 보류 메모 | 입력 자료 준비 여부와 실행 가능 범위가 설명됨 |
| Agent 변환 | `.claude/agents/{name}.md` (orchestrator + sub-agent) | Agent 파일이 생성되고 실제 호출 테스트가 1회 이상 완료됨 |

## 관련 문서

- [02_doc-classification.md](./02_doc-classification.md)
- [03_interaction-protocol.md](./03_interaction-protocol.md)
