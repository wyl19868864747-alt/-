---
name: ai-virtual-partner-skill
description: AI virtual partner image and video generation skill. Current verified scope covers user portrait identity locking plus a validated partner archetype library and model-specific prompt adaptation rules. Partner matching, persistent partner identity, intimacy pose/scene routing, realism, and image-to-video continuity are added only after separate research and validation.
---

# AI 虚拟伴侣｜AI Virtual Partner

Build a persistent virtual-partner visual experience around the user's uploaded adult portrait. The system must lock the user's identity before any partner matching, couple composition, styling, or video work.

## Current Verified Scope

Active modules:

`User Upload → Portrait Identity Lock → Identity QC → Approved User Reference`

`Partner Archetype Resolve → Model Adaptation → Partner Appearance Prompt`

Read:

- `references/portrait-identity-lock.md` for user identity preservation;
- `references/partner-archetype-library.md` for validated and candidate adult partner appearance archetypes;
- `references/model-adaptation.md` before compiling prompts for image 2.5, Banana2 Pro, or Seedance 2.5.

Do not invent or activate unfinished modules merely because the future product may need them. The following remain **NOT YET VERIFIED**:

- partner matching / couple resemblance logic
- persistent partner identity
- intimacy pose grammar
- intimate scene library
- dedicated realism engine
- image-to-video continuity engine

Each module must be researched, distilled, tested, and then added separately.

## 1. User Portrait Identity Lock

Before generating any couple image, establish a stable user identity representation.

The portrait-lock module must:

1. inspect the uploaded portrait(s) for usable identity evidence;
2. separate stable identity traits from transient photo conditions;
3. build `USER_IDENTITY_CARD`;
4. build `CANONICAL_IDENTITY`;
5. classify traits into hard locks, strong locks, soft locks, and free variables;
6. optionally build a four-view identity reference representation when downstream complexity requires it;
7. run Identity QC after every generation that may become a new reference;
8. reject identity drift and fall back to the original approved identity anchors;
9. promote only high-confidence, identity-stable outputs into the reference pool.

Core rule:

`IDENTITY FIRST > STYLING > SCENE > POSE > BEAUTIFICATION`

If “more attractive” conflicts with “more like the uploaded person,” preserve the uploaded person's identity.

## 2. Partner Archetype Resolve

Read `references/partner-archetype-library.md`.

Keep `HERITAGE_APPEARANCE` independent from `ARCHETYPE_ID`.

The library provides adult attraction archetypes, not ethnic beauty rankings or universal beauty formulas. Use only validated archetypes as default production choices; candidate archetypes may be used for explicit testing but must remain labeled as unverified.

Do not use `golden ratio`, skin-tone ranking, or one fixed face template as a beauty engine.

A partner appearance profile should resolve from structured fields before prompt compilation, for example:

`ADULT AGE BAND + GENDER PRESENTATION + HERITAGE_APPEARANCE + ARCHETYPE_ID + FACE/BODY PARAMETERS + STYLE AURA`

## 3. Model Adaptation

Read `references/model-adaptation.md` before generating.

Do not mechanically reuse one prompt across models.

Compile as:

`STRUCTURED INTENT → MODEL ADAPTER → MODEL-SPECIFIC PROMPT`

Current empirical profiles exist for:

- image 2.5
- Banana2 Pro
- Seedance 2.5

Model behavior must be updated from reusable real-case feedback, not from one-off speculation.

## 4. Reference Priority

User identity authority order is fixed:

`ORIGINAL_USER_IMAGE > USER_IDENTITY_CARD > CANONICAL_IDENTITY > CORE_REFERENCE_SHEET > APPROVED_REFERENCE > TEXT DESCRIPTION`

AI-derived references may strengthen identity coverage but may never overwrite the original user's identity.

## 5. Downstream Isolation

When a virtual partner is added later, the user and partner must occupy separate identity slots:

`PERSON_A = USER`

`PERSON_B = PARTNER`

No downstream module may merge, swap, or cross-contaminate their facial identity features.

## 6. Validation Gate

Use:

- `validation/portrait-identity-lock-cases.md` for identity-lock changes;
- `validation/archetype-benchmark.md` for archetype or model-adaptation changes.

A document edit alone does not prove runtime stability. Only behavior directly supported by real generation evidence may be labeled runtime-validated.

## 7. Expansion Rule

New capabilities are added one module at a time.

For every new module:

`Research → Evidence Cards → Common Mechanism → Distilled Rule → Failure Cases → Validation → Add to Skill`

Do not place large research notes directly into this file. Put heavy domain knowledge in `references/` and keep this file as the orchestration and hard-constraint layer.
