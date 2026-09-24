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
    "bgm-sound-rhythm", "ending-payoff", "prompt-compiler",
    "perception-reaction-gate", "four-layer-shot-gate",
    "aigc-native-visual-event"))]
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
owner05 = (ROOT / "references/04-performance-voice-lipsync.md").read_text(encoding="utf-8") if (ROOT / "references/04-performance-voice-lipsync.md").exists() else ""
compiler = (ROOT / "references/07-prompt-compiler.md").read_text(encoding="utf-8") if (ROOT / "references/07-prompt-compiler.md").exists() else ""
for label, contents in (("core", core), ("G-05 owner", owner05), ("master", skill), ("compiler", compiler), ("cross-style QA", matrix)):
    check("12" in contents and ("对白" in contents or "台词" in contents), f"{label} missing 12+ purposeful dialogue rule")
check("情绪" in owner05 and "时间" in owner05, "G-05 must require emotional progression and timed speech")
owner09 = (ROOT / "references/08-perception-reaction-gate.md").read_text(encoding="utf-8") if (ROOT / "references/08-perception-reaction-gate.md").exists() else ""
check("G-09" in core and "G-09" in skill and "G-09" in matrix and "G-09" in compiler, "G-09 must appear in core, master, regression and final compiler")
check(all(term in owner09 for term in ("触发", "感知", "反射", "识别", "视线", "摄影")), "G-09 owner must define trigger, awareness, visible reflex and camera proof")
for style in STYLES:
    check("G-01～G-11" in style.read_text(encoding="utf-8"), f"Style missing G-11 inheritance declaration: {style.name}")
    row = next((line for line in matrix.splitlines() if line.startswith("| `"+style.name+"`")), "")
    check(row.count("|") == 13 and row.count("必测") == 11, f"Cross-style matrix missing 11 separate gates: {style.name}")
owner10 = (ROOT / "references/09-four-layer-shot-gate.md").read_text(encoding="utf-8") if (ROOT / "references/09-four-layer-shot-gate.md").exists() else ""
check("G-10" in core and "G-10" in skill and "G-10" in matrix and "G-10" in compiler, "G-10 must appear in core, master, matrix and compiler")
check(all(term in owner10 for term in ("画面层", "位置层", "构图层", "光影层", "运动", "地标")), "G-10 must specify four-layer review and movement owner")
check((ROOT / "evaluation/HALLOWEEN_STATE_FIXTURE.md").is_file(), "Missing Halloween spatial regression fixture")
check("Case 17" in (ROOT / "evaluation/REGRESSION_CASES.md").read_text(encoding="utf-8"), "Missing reset-to-origin regression case")
check("Case 18" in (ROOT / "evaluation/REGRESSION_CASES.md").read_text(encoding="utf-8"), "Missing companion-follow regression case")
check("Case 20" in (ROOT / "evaluation/REGRESSION_CASES.md").read_text(encoding="utf-8"), "Missing performance-after-spatial-lock regression case")
owner11 = (ROOT / "references/10-aigc-native-visual-event.md").read_text(encoding="utf-8") if (ROOT / "references/10-aigc-native-visual-event.md").exists() else ""
check("G-11" in core and "G-11" in skill and "G-11" in matrix and "G-11" in compiler, "G-11 must appear in core, master, matrix and compiler")
check(all(term in owner11 for term in ("现实底盘", "触发", "传播", "中间态", "Camera", "Sound")), "G-11 must define reality base, trigger, propagation, intermediate state, camera and sound coupling")
check("Case 21" in (ROOT / "evaluation/REGRESSION_CASES.md").read_text(encoding="utf-8"), "Missing connected-dialogue regression case")
check("Case 22" in (ROOT / "evaluation/REGRESSION_CASES.md").read_text(encoding="utf-8"), "Missing AIGC-native visual regression case")
owner07 = (ROOT / "references/06-ending-payoff.md").read_text(encoding="utf-8") if (ROOT / "references/06-ending-payoff.md").exists() else ""
check("空间锁只锁风险段" in owner10, "G-10 must release camera freedom after risky movement")
check("空间稳定不等于站桩" in owner05, "G-05 must preserve performance density after spatial stabilization")
check("关系回合" in owner07, "G-07 must close the final relationship beat before the hold")
if errors:
    for item in errors:
        print("FAIL:", item)
    sys.exit(1)
print(f"PASS: core registry, 11 owner modules, {len(STYLES)} style inheritance declarations, G-09/G-10/G-11 routing and cross-style regression coverage")
print("NOTE: structural lint only; cinematic and generated-video validation are separate gates")
