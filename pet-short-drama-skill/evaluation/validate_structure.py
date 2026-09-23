#!/usr/bin/env python3
"""Structural lint only; cannot verify video generation or cinematic continuity."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "references/CORE_RULES.md"
SKILL = ROOT / "SKILL.md"
MATRIX = ROOT / "evaluation/CROSS_STYLE_REGRESSION.md"
STYLES = sorted((ROOT / "references/styles").glob("*.md"))
OWNERS = [f"references/{i:02d}-{name}.md" for i, name in enumerate((
    "project-defaults", "spatial-state-chain", "physical-previsualization",
    "cinematography-composition", "performance-voice-lipsync",
    "bgm-sound-rhythm", "ending-payoff", "prompt-compiler"))]
errors = []

def check(ok, message):
    if not ok:
        errors.append(message)

check(SKILL.is_file() and "references/CORE_RULES.md" in SKILL.read_text(encoding="utf-8"), "SKILL.md must route to CORE_RULES.md")
check(CORE.is_file(), "Missing core registry")
check(MATRIX.is_file(), "Missing cross-style matrix")
check((ROOT / "references/PROJECT_CONTRACT.md").is_file(), "Missing project contract")
check(len(STYLES) >= 4, "Expected all four original styles")
core = CORE.read_text(encoding="utf-8") if CORE.exists() else ""
matrix = MATRIX.read_text(encoding="utf-8") if MATRIX.exists() else ""
skill = SKILL.read_text(encoding="utf-8") if SKILL.exists() else ""
for number, owner in enumerate(OWNERS, 1):
    check((ROOT / owner).is_file(), f"Missing rule-owner file: {owner}")
    check(re.search(rf"\bG-{number:02d}\b", core) is not None, f"Missing G-{number:02d} in core registry")
    check(owner in core, f"Registry must name owner: {owner}")
for style in STYLES:
    body = style.read_text(encoding="utf-8")
    check("全局继承" in body and "CORE_RULES.md" in body, f"Style missing core inheritance header: {style.name}")
    check(style.name in skill, f"Style not routed by SKILL.md: {style.name}")
    check(style.name in matrix, f"Style not covered in regression matrix: {style.name}")
check("逐镜循环" in skill, "SKILL.md must require per-shot iterative previsualization")
check("只修改公共模块" in skill, "SKILL.md must state single-owner core updates")
if errors:
    for item in errors:
        print("FAIL:", item)
    sys.exit(1)
print(f"PASS: core registry, 8 owner modules, {len(STYLES)} style inheritance declarations, routing and regression coverage")
print("NOTE: structural lint only; cinematic and generated-video validation are separate gates")
