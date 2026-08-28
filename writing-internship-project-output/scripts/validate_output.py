#!/usr/bin/env python3
"""Validate writing-internship-project-output artifacts.

The validator is intentionally structural: it checks that an output covers every
workflow slot required by SKILL.md, instead of judging prose quality.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Check:
    key: str
    label: str
    description: str
    required_any: tuple[str, ...] = ()
    required_all: tuple[str, ...] = ()
    strict_only: bool = False


WORKFLOW_CHECKS: tuple[Check, ...] = (
    Check(
        key="evidence",
        label="先收集证据",
        description="需要交代内容基于代码、文档、任务记录、已有产出或用户描述。",
        required_any=("证据", "源码依据", "基于项目代码", "基于 `", "README", "设计文档", "任务记录", "已有产出"),
    ),
    Check(
        key="story",
        label="识别项目故事",
        description="需要包含项目定位、需求背景、业务问题、旧方案痛点或风险。",
        required_any=("项目定位", "需求背景", "业务背景", "问题背景", "旧方案", "痛点", "风险"),
    ),
    Check(
        key="highlights",
        label="核心亮点",
        description="需要有技术亮点，且亮点具备“问题背景 -> 技术方案 -> 收益”链路。",
        required_any=("核心亮点", "技术亮点", "亮点 1", "亮点1"),
        required_all=("问题背景", "技术方案", "收益"),
    ),
    Check(
        key="complete_output_structure",
        label="完整产出结构",
        description="完整项目产出应覆盖项目定位、亮点、技术深度、简历、待补充、面试话术、项目意义。",
        required_all=("项目定位", "核心亮点", "技术深度", "简历段落", "待补充信息", "面试话术", "项目意义"),
        strict_only=True,
    ),
    Check(
        key="style",
        label="匹配表达风格",
        description="需要体现技术复盘式表达，围绕业务问题、技术机制、工程收益组织。",
        required_all=("问题背景", "技术方案", "收益"),
    ),
    Check(
        key="resume_interview",
        label="生成简历和面试材料",
        description="需要同时包含简历段落/bullet 和面试话术/深挖问题。",
        required_all=("简历", "面试"),
    ),
    Check(
        key="real_pitfalls",
        label="补充真实场景坑点",
        description="需要覆盖开发/联调/真实问题/配置验证/测试样例/AI 方案纠偏等复盘内容。",
        required_any=("真实场景坑点", "开发复盘", "联调", "真实问题", "配置验证", "测试样例", "AI 生成方案", "vibe coding"),
        strict_only=True,
    ),
    Check(
        key="evidence_check",
        label="证据自检",
        description="需要有证据自检或待补充信息，避免无证据指标和敏感信息。",
        required_any=("证据自检", "待补充信息", "无法证明", "无证据", "不要写", "未证实"),
    ),
)


RISK_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"(?<!不要说[“\"])(?<!不要写[“\"])独立负责", "避免无证据个人贡献: 独立负责"),
    (r"(?<!不要说[“\"])(?<!不要写[“\"])独立完成", "避免无证据个人贡献: 独立完成"),
    (r"(?<!不要说[“\"])(?<!不要写[“\"])主导上线", "避免无证据上线表述: 主导上线"),
    (r"(?<!不要说[“\"])(?<!不要写[“\"])已上线", "避免无证据上线状态: 已上线"),
    (r"提升\s*\d+(\.\d+)?\s*%", "避免无证据性能百分比"),
    (r"日均\s*\d+", "避免无证据业务量级"),
    (r"\bQPS\b\s*[:：]?\s*\d+", "避免无证据 QPS"),
    (r"\bDAU\b\s*[:：]?\s*\d+", "避免无证据 DAU"),
    (r"https?://[^\s)）]+", "避免输出非公开或敏感 URL"),
)


def contains_any(text: str, needles: Iterable[str]) -> bool:
    return any(needle in text for needle in needles)


def missing_checks(text: str, strict: bool) -> list[dict[str, str]]:
    failures: list[dict[str, str]] = []
    for check in WORKFLOW_CHECKS:
        if check.strict_only and not strict:
            continue
        missing_parts: list[str] = []
        if check.required_any and not contains_any(text, check.required_any):
            missing_parts.append("至少包含其一: " + " / ".join(check.required_any))
        for needle in check.required_all:
            if needle not in text:
                missing_parts.append(f"缺少: {needle}")
        if missing_parts:
            failures.append(
                {
                    "key": check.key,
                    "label": check.label,
                    "description": check.description,
                    "missing": "; ".join(missing_parts),
                }
            )
    return failures


def risk_hits(text: str) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for pattern, message in RISK_PATTERNS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            line_no = text.count("\n", 0, match.start()) + 1
            line = text.splitlines()[line_no - 1].strip()
            hits.append({"line": str(line_no), "message": message, "text": line})
    return hits


def print_human_report(failures: list[dict[str, str]], risks: list[dict[str, str]]) -> None:
    if not failures and not risks:
        print("PASS: 输出覆盖 SKILL.md 工作流要求，且未发现高风险表述。")
        return
    print("FAIL: 输出未通过验收。")
    if failures:
        print("\n缺失工作流项:")
        for failure in failures:
            print(f"- {failure['label']}: {failure['description']}")
            print(f"  {failure['missing']}")
    if risks:
        print("\n风险表述:")
        for risk in risks:
            print(f"- line {risk['line']}: {risk['message']}")
            print(f"  {risk['text']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate an output against writing-internship-project-output workflow requirements."
    )
    parser.add_argument("output", help="Path to generated Markdown/text output.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Require every SKILL.md workflow slot, including full output structure and real-scenario pitfalls.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON report.",
    )
    args = parser.parse_args(argv)

    output_path = Path(args.output)
    if not output_path.exists():
        print(f"FAIL: output file not found: {output_path}")
        return 2
    text = output_path.read_text(encoding="utf-8")

    failures = missing_checks(text, strict=args.strict)
    risks = risk_hits(text)
    if args.json:
        print(json.dumps({"failures": failures, "risks": risks}, ensure_ascii=False, indent=2))
    else:
        print_human_report(failures, risks)
    return 1 if failures or risks else 0


if __name__ == "__main__":
    raise SystemExit(main())
