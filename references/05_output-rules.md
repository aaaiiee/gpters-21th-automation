---
title: "05 Output Rules"
summary: "중급 산출물 저장과 출력 방식의 단순 규칙"
---

# Output Rules

## 저장 위치

권장 위치:

```text
C:\501_aiworks\10_working\120autoproject\<120x_single_pipeline_name>\
  source\
  output\
```

저장 원칙:

- 결과물은 반드시 `C:\501_aiworks\10_working\120autoproject` 하위에 저장합니다.
- 자동화 업무별로 `단일 파이프라인 폴더`를 하나씩 생성합니다.
- 인터뷰 메모부터 실행 결과까지 모두 같은 업무 폴더 안에서 관리합니다.
- 한 폴더에 여러 자동화 업무를 섞지 않습니다.
- 폴더명은 가능한 한 `120x_업무주제_automation` 형식으로 통일합니다.

예시:

```text
C:\501_aiworks\10_working\120autoproject\1201_single_pipeline_name\
  source\
  output\
```

스킬 내부의 `bundled_study_docs`는 참고 사본으로 사용하고, 사용자 산출물은 별도 프로젝트 폴더에 두는 것을 우선합니다.

## 출력 방식

- 산출물 1개씩 작성
- 인터뷰 메모와 워크시트를 가장 중요한 산출물로 취급
- 복잡한 상태 폴더를 만들지 않음
- 인터뷰와 워크시트의 핵심 항목은 빈칸으로 두지 않음
- 충분히 질문했지만 사용자가 현재 답할 수 없는 항목은 `[보류: 이유]`
- 비핵심 검증 항목이나 추후 확인 사항만 `[확인 필요]`
- 앞 단계 정보를 최대한 재사용
- 없는 기능은 `그레이 영역`으로 남기고 새 스킬 후보를 적음
- 후속 단계에서 핵심 공백이 보이면 문서를 억지로 완성하지 말고 인터뷰 또는 워크시트로 되돌아감

## 필수 저장 대상

- 인터뷰 메모
- 워크시트 (필수)
- 자동화 설계 초안 (필수)
- 도구 연결표 (필수)
- 실행/결과 확인 메모 또는 실행 보류 메모 (필수)
- Agent 정의 파일 (필수, Step 6 완료 시)

## 권장 파일 예시

- `output\interview_notes.md`
- `output\worksheet.md`
- `output\automation_design.md`
- `output\tool_connection.md`
- `output\orchestration_run.md`
- `output\run_result.md` 또는 실행 보류 메모 파일
- `.claude\agents\{orchestrator-name}.md` (orchestrator agent)
- `.claude\agents\{sub-agent-name}.md` (sub-agent, 필요 시 복수)

## 관련 문서

- [02_doc-classification.md](./02_doc-classification.md)
