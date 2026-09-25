#!/usr/bin/env python3
"""Audit direct module discoverability for linfeng-video-prompt."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
CAPTURE_BASELINE = ROOT / "references" / "camera-light-quality-baseline.md"


def local_links(text: str) -> set[str]:
    return set(
        re.findall(r"`((?:references|evaluation-cases)/[^`]+\.md)`", text)
    )


def main() -> int:
    errors: list[str] = []
    skill_text = SKILL.read_text(encoding="utf-8")
    capture_text = CAPTURE_BASELINE.read_text(encoding="utf-8")

    actual_references = {
        str(path.relative_to(ROOT)) for path in (ROOT / "references").glob("*.md")
    }
    linked_references = {
        link for link in local_links(skill_text) if link.startswith("references/")
    }

    for path in sorted(linked_references - actual_references):
        errors.append(f"missing reference: {path}")
    for path in sorted(actual_references - linked_references):
        errors.append(f"orphaned reference without direct SKILL.md route: {path}")

    for markdown in [SKILL, *ROOT.glob("references/*.md"), *ROOT.glob("evaluation-cases/*.md")]:
        text = markdown.read_text(encoding="utf-8")
        for link in sorted(local_links(text)):
            if not (ROOT / link).is_file():
                errors.append(f"broken local link in {markdown.relative_to(ROOT)}: {link}")

    required_core = [
        "references/camera-light-quality-baseline.md",
        "references/prompt-compilation-and-consistency.md",
        "references/spatial-handoff-lock.md",
        "references/output-contract-and-validation.md",
    ]
    for path in required_core:
        if skill_text.count(path) < 2:
            errors.append(f"required writing entry points is not declared in both workflow and routing table: {path}")

    if "并列勾选项" not in skill_text or "不得命中第一项后停止" not in skill_text:
        errors.append("parallel additive routing invariant is missing from SKILL.md")

    mandatory_prompt_line = next(
        (line for line in skill_text.splitlines() if "写/重写Prompt必读" in line),
        "",
    )
    if "references/camera-light-quality-baseline.md" not in mandatory_prompt_line:
        errors.append(
            "capture baseline is not in the mandatory write/rewrite Prompt read chain"
        )

    if "摄影机与成像基线是常驻能力" not in skill_text:
        errors.append("always-on capture baseline invariant is missing from SKILL.md")

    if "先保护 Hero Idea，再修执行" not in skill_text:
        errors.append("creative preservation invariant is missing from SKILL.md")

    if "Creative Pass" not in skill_text or "Execution Gate" not in skill_text:
        errors.append("creative-pass-before-execution-gate workflow is missing from SKILL.md")

    if "Always-on Capture Baseline" not in capture_text or "每次必过" not in capture_text:
        errors.append(
            "camera-light-quality-baseline.md no longer declares the always-on capture layer"
        )

    if errors:
        print("Routing audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Routing audit passed: "
        f"{len(actual_references)} references are directly routed; "
        "all local links resolve; mandatory capture baseline, creative preservation, required writing entry points, and additive routing are present."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
