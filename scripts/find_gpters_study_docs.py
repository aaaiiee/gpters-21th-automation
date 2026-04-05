from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[1] / "references" / "bundled_study_docs"

# 번들 문서 역할 매핑
RULES = {
    "flow_reference": ("업무자동화", "전체-플로우-도식화"),
    "hub": ("인터뷰및자동화룰", "생성방법"),
    "interview": ("업무정의-자동화-위임설계서-인터뷰",),
    "worksheet": ("업무정의-자동화-위임설계서-인터뷰-워크시트",),
    "workflow_rules_template": ("workflow_rules", "작성"),
    "workflow_rules_sample": ("workflow_rules", "sample"),
    "student_guide": ("학생용-사용법-및-실행-설명서",),
}

STAGE_RULES = {
    "intent": (
        ("flow_reference", "primary"),
        ("hub", "supporting"),
        ("student_guide", "supporting"),
    ),
    "interview": (
        ("interview", "primary"),
        ("hub", "supporting"),
        ("flow_reference", "supporting"),
        ("student_guide", "supporting"),
    ),
    "worksheet": (
        ("worksheet", "primary"),
        ("interview", "supporting"),
        ("hub", "supporting"),
        ("student_guide", "supporting"),
    ),
    "automation_design": (
        ("workflow_rules_template", "primary"),
        ("workflow_rules_sample", "supporting"),
        ("worksheet", "supporting"),
        ("interview", "supporting"),
        ("flow_reference", "supporting"),
    ),
    "tool_connection": (
        ("workflow_rules_template", "supporting"),
        ("workflow_rules_sample", "supporting"),
        ("student_guide", "supporting"),
        ("flow_reference", "supporting"),
    ),
    "orchestration_execution": (
        ("student_guide", "primary"),
        ("workflow_rules_sample", "supporting"),
        ("flow_reference", "supporting"),
        ("hub", "supporting"),
    ),
    "agent_conversion": (
        ("student_guide", "supporting"),
        ("workflow_rules_template", "supporting"),
        ("workflow_rules_sample", "supporting"),
        ("flow_reference", "supporting"),
    ),
}


def normalize(text: str) -> str:
    return text.casefold().replace("_", "-")


def matches(name: str, terms: tuple[str, ...]) -> bool:
    normalized = normalize(name)
    return all(normalize(term) in normalized for term in terms)


def list_markdown_files(root: Path) -> list[Path]:
    return sorted(
        (
            item
            for item in root.iterdir()
            if item.is_file()
            and item.suffix.lower() == ".md"
            and not item.name.casefold().endswith(".security.md")
        ),
        key=lambda item: item.name.casefold(),
    )


def build_map(root: Path) -> dict[str, dict[str, str] | None]:
    files = list_markdown_files(root)
    result: dict[str, dict[str, str] | None] = {}
    for role, terms in RULES.items():
        match = next((item for item in files if matches(item.name, terms)), None)
        if match is None:
            result[role] = None
            continue
        result[role] = {"name": match.name, "path": str(match)}
    return result


def render_markdown(root: Path, mapping: dict[str, dict[str, str] | None]) -> str:
    lines = [f"# 중급 자동화 문서 매핑", "", f"- root: `{root}`", "", "| role | file |", "|---|---|"]
    for role, payload in mapping.items():
        if payload is None:
            lines.append(f"| {role} | NOT FOUND |")
        else:
            lines.append(f"| {role} | {payload['name']} |")
    return "\n".join(lines)


def build_stage_payload(
    mapping: dict[str, dict[str, str] | None], stage: str
) -> list[dict[str, str | None]]:
    payload: list[dict[str, str | None]] = []
    for role, priority in STAGE_RULES[stage]:
        entry = mapping.get(role)
        payload.append(
            {
                "priority": priority,
                "role": role,
                "name": None if entry is None else entry["name"],
                "path": None if entry is None else entry["path"],
            }
        )
    return payload


def render_stage_markdown(
    root: Path, stage: str, stage_docs: list[dict[str, str | None]]
) -> str:
    lines = [
        "# 중급 자동화 문서 매핑",
        "",
        f"- root: `{root}`",
        f"- stage: `{stage}`",
        "- primary: 현재 단계의 사실상 정본",
        "- supporting: 보조 참조 문서",
        "",
        "| priority | role | file |",
        "|---|---|---|",
    ]
    for entry in stage_docs:
        file_name = entry["name"] if entry["name"] is not None else "NOT FOUND"
        lines.append(f"| {entry['priority']} | {entry['role']} | {file_name} |")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="중급 자동화 스킬의 번들 참고 문서를 현재 파일명 기준으로 역할별 매핑합니다.")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="문서 루트 경로. 기본값은 스킬 내부 bundled_study_docs")
    parser.add_argument(
        "--stage",
        choices=tuple(STAGE_RULES),
        help="특정 단계에서 우선 참고할 문서만 출력",
    )
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="출력 형식")
    parser.add_argument("--list-stages", action="store_true", help="지원하는 단계 이름 목록 출력")
    parser.add_argument("--save", help="결과 저장 경로")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.list_stages:
        print("\n".join(STAGE_RULES))
        return

    root = Path(args.root).expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"문서 폴더를 찾지 못했습니다: {root}")

    mapping = build_map(root)
    if args.stage:
        stage_docs = build_stage_payload(mapping, args.stage)
        if args.format == "json":
            output = json.dumps({"stage": args.stage, "docs": stage_docs}, ensure_ascii=False, indent=2)
        else:
            output = render_stage_markdown(root, args.stage, stage_docs)
    elif args.format == "json":
        output = json.dumps(mapping, ensure_ascii=False, indent=2)
    else:
        output = render_markdown(root, mapping)

    if args.save:
        save_path = Path(args.save).expanduser().resolve()
        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_path.write_text(output, encoding="utf-8")

    print(output)


if __name__ == "__main__":
    main()
