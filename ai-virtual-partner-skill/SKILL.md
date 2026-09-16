---
name: ai-virtual-partartner-skill
description: AI virtual partner image and video generation skill. Current verified scope is user portrait identity locking: extract stable identity anchors from uploaded adult portraits, build a canonical identity representation, optionally build a four-view reference sheet, preserve identity across downstream image generation, reject drift, and only promote identity-stable outputs as references. Partner matching, partner archetypes, intimacy pose/scene routing, realism, and image-to-video continuity are added only after separate research and validation.
---

# AI 虚拟伴侣｜AI Virtual Partner

Build a persistent virtual-partner visual experience around the user's uploaded adult portrait. The system must lock the user's identity before any partner matching, couple composition, styling, or video work.

## Current Verified Scope

Only the following module is active in V0:

`User Upload → Portrait Identity Lock → Identity QC → Approved User Reference`

Read `references/portrait-identity-lock.md` before any downstream image or video generation.

Do not invent or activate unfinished modules merely because the future product may need them. The following remain **NOT YET VERIFIED**:

- partner appearance archetypes
- partner matching / couple resemblance logic
- persistent partner identity
- intimacy pose grammar
- intimate scene library
- realism engine
- image-to-video continuity

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

## 2. Reference Priority

Identity authority order is fixed:

`ORIGINAL_USER_IMAGE > USER_IDENTITY_CARD > CANONICAL_IDENTITY > CORE_REFERENCE_SHEET > APPROVED_REFERENCE > TEXT DESCRIPTION`

AI-derived references may strengthen identity coverage but may never overwrite the original user's identity.

## 3. Downstream Isolation

When a virtual partner is added later, the user and partner must occupy separate identity slots:

`PERSON_A = USER`

`PERSON_B = PARTNER`

No downstream module may merge, swap, or cross-contaminate their facial identity features.

## 4. Validation Gate

Use `validation/portrait-identity-lock-cases.md` whenever this module changes.

A document edit alone does not prove runtime stability. Until live image/video regressions pass, status is:

`UPDATED — RUNTIME UNVERIFIED`

## 5. Expansion Rule

New capabilities are added one module at a time.

For every new module:

`Research → Evidence Cards → Common Mechanism → Distilled Rule → Failure Cases → Validation → Add to Skill`

Do not place large research notes directly into this file. Put heavy domain knowledge in `references/` and keep this file as the orchestration and hard-constraint layer.
