# Repository Agent Instructions

## Mandatory governance

Before creating, editing, distilling, syncing, refactoring, evaluating, or declaring completion of any Skill in this repository, read and follow:

`skill-engineering-governance/SKILL.md`

## SSOT

- GitHub `main` is the only Skill mother-template SSOT.
- Do not overwrite `main` from memory, old chat context, or an older local/account copy.
- External repositories are research inputs only, never SSOT for this repository.

## Change discipline

- Find the earliest owning layer and root cause before editing.
- Prefer the smallest change that fixes the identified failure.
- Do not bundle unrelated cleanup with a targeted fix.
- Important behavior changes must add or update an evaluation / validation case.
- Do not patch platform/runtime context-loss problems by adding recovery text to creative Skills.

## Verification discipline

Before saying a GitHub change is complete:

1. write the change;
2. read the changed file back from the target branch;
3. verify required paths and references exist;
4. report the exact verified state.

Do not claim account-level Skill synchronization unless the account-side Skill was directly read or otherwise verified.

## Output separation

Operator communication rules such as status-first answers, progress visibility, numbered execution steps, or verification labels belong to the interaction/governance layer.

They must never leak into Seedance, image-generation, or other model-facing creative prompts.
