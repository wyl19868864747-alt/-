---
name: ai-virtual-partner-skill
description: AI virtual partner image and video generation skill. Current verified scope covers user portrait identity locking, partner archetype resolution, matching modes, partner identity locking, sweet-couple moment routing, validated relation actions / scenes, camera realism controls, model-specific image routing, and a validated Seedance 2.5 short couple-video start strategy.
---

# AI 虚拟伴侣｜AI Virtual Partner

Create a believable adult virtual-partner experience from the user's uploaded portrait. The result should feel like a captured sweet relationship moment with a highly attractive, plausible partner—not a formal couple portrait.

## Current Verified Flow

```text
USER UPLOAD
↓
PORTRAIT IDENTITY LOCK
↓
USER_IDENTITY_CARD / USER REFERENCE SHEET
↓
PARTNER ARCHETYPE RESOLVE
↓
MATCHING ENGINE
↓
APPROVED PARTNER CANDIDATE
↓
PARTNER IDENTITY LOCK / PARTNER REFERENCE PACKAGE
↓
COUPLE MOMENT ROUTER
↓
RELATION ACTION / SCENE ROUTER
↓
MODEL ROUTER
↓
MODEL-SPECIFIC IMAGE PROMPT
↓
APPROVED COUPLE FRAME
↓
SEEDANCE COUPLE-VIDEO START ROUTER
↓
IDENTITY + CHEMISTRY + REALISM + MOTION QC
```

## Required Knowledge Modules

Read only the modules needed by the current stage:

- `references/portrait-identity-lock.md` — lock uploaded user identity, four-view logic, drift prevention.
- `references/partner-archetype-library.md` — adult partner appearance archetypes.
- `references/matching-engine.md` — Harmony / Preference / Complementary Contrast routing.
- `references/partner-identity-lock.md` — freeze an approved partner into a reusable identity / reference package.
- `references/couple-moment-dna.md` — sweet, intimate, non-formal couple-image DNA.
- `references/moment-type-library.md` — validated sweet-moment types and their use cases.
- `references/relation-action-library.md` — physical couple-action grammar and validated contact patterns.
- `references/scene-tension-library.md` — validated window / sofa / bedroom scene behavior and tension routing.
- `references/model-routing-rules.md` — choose image 2.5 vs Banana2 Pro by product target.
- `references/model-adaptation.md` — compile different prompts for image 2.5 / Banana2 Pro / Seedance 2.5.
- `references/camera-realism-layer.md` — real skin / exposure / camera texture controls.
- `references/seedance-couple-video-start.md` — validated Seedance 2.5 first-frame and 3–5s approach logic.

Do not copy entire knowledge files into the final model prompt. Resolve the structured decision first, then compile only the minimum effective instructions for the chosen model.

---

## 1. User Identity Gate

Before any partner generation:

1. inspect user portrait evidence;
2. build `USER_IDENTITY_CARD`;
3. separate identity traits from photo conditions;
4. build / infer the identity reference sheet when needed;
5. lock hard identity anchors;
6. reject identity drift.

Core rule:

`IDENTITY FIRST`

If beautification conflicts with the user's identity, preserve identity.

---

## 2. Partner Resolve

Read `partner-archetype-library.md`.

Keep:

`HERITAGE_APPEARANCE` independent from `ARCHETYPE_ID`.

Do not use heritage ranking, skin-tone ranking, golden-ratio formulas, or one universal beauty face.

Create a distinct `PARTNER_APPEARANCE_CARD` before generating the partner.

---

## 3. Matching Engine

Read `matching-engine.md`.

Supported validated modes:

- `HARMONY_MATCH` — strongest natural couple-likeness.
- `PREFERENCE_MATCH` — explicit user attraction preference first.
- `COMPLEMENTARY_CONTRAST` — controlled visual / aura contrast with social-role risk checks.

User explicit preference overrides system priors.

Do not output fake compatibility percentages.

Matching logic is internal. Use a `VISIBLE SUBJECT FILTER` before prompt compilation so solo partner prompts do not accidentally render the user.

---

## 4. Partner Identity Lock

After the user approves a partner candidate, read `partner-identity-lock.md`.

Create:

`PARTNER_IDENTITY_CARD`
+
`PARTNER_REFERENCE_PACKAGE`

The current validated P1 workflow prefers image 2.5 for canonical partner reference-sheet construction because it preserved cross-angle identity better than Banana2 Pro in the tested front / 45° / profile / close-up set.

Banana2 Pro remains a realism-support route, not the current default partner canonicalizer.

Do not mix structurally conflicting identity views from different models into one partner reference package.

Partner reference authority:

`ORIGINAL_APPROVED_PARTNER > PARTNER_IDENTITY_CARD > APPROVED_REFERENCE_PACKAGE > APPROVED_COUPLE_FRAME > TEXT`

---

## 5. Couple Moment + Relation Action Router

Read `couple-moment-dna.md`, `moment-type-library.md`, and `relation-action-library.md`.

Default product goal:

> The first impression should be sweet, intimate and slightly heart-fluttering—“this is what my unknown best partner looks like.”

Validated moment / action findings:

- `SOFT_ALMOST_KISS` — strongest static Hero moment.
- `CLOSE_EYE_CONTACT` — default realistic sweet moment.
- `SHOULDER_LEAN` — safe long-term sweetness.
- `FACE-TO-FACE WAIST HOLD + BREATH-CLOSE` — strongest current physical chemistry route.
- `PROTECTIVE SIDE EMBRACE` — safe protective sweetness.
- `BACK HUG` — clear affection / safety but currently more conservative.

Core rule:

`MORE TENSION ≠ MORE CONTACT`

Prefer controlled approach, gaze and unresolved distance over immediately completing contact.

Avoid stiff, front-facing formal couple portraits.

---

## 6. Scene Router

Read `scene-tension-library.md`.

Current validated scene behavior:

- `WINDOW-SIDE` — strongest current romantic-tension environment and best current Seedance start base.
- `SOFA CORNER` — strongest realistic everyday-couple environment.
- `BEDROOM EDGE` — private-space signal only; does not automatically create stronger chemistry.

Do not use a private location as a substitute for relationship direction.

Color-rich scene families remain under test; do not lock one neutral palette as the product default.

---

## 7. Model Router

Read `model-routing-rules.md` and `model-adaptation.md`.

### Default Hero / Canonical Asset Route

`image 2.5`

Use for:

- highest partner attractiveness
- hero / cover result
- strongest best-partner fantasy
- Soft Almost-Kiss / heart-flutter moments
- current preferred partner canonical reference-sheet construction

Apply validated compensation for noise / grey / dark rendering and anti-redesign controls during identity completion.

### Real / Candid Image Route

`Banana2 Pro`

Use for:

- stronger real-photo feel
- candid couple photography
- low generation noise
- natural heritage appearance
- photographic realism support
- current real-couple first-frame exploration

Current Banana prompt compensation may include real pores / microtexture, `not overexposed`, and avoidance of a white hazy veil when observed. Do not over-stack tonal-control phrases if they flatten the image.

Never mechanically reuse one prompt across models.

---

## 8. Camera Realism

Read `camera-realism-layer.md`.

Distinguish:

`GENERATION NOISE` from `PHOTOGRAPHIC TEXTURE`.

Realism should come from:

- real skin microtexture
- natural tonal irregularity
- believable exposure
- restrained optical softness
- real materials / hair / fabric

not from dirty noise or decorative grain.

---

## 9. Seedance 2.5 Couple Video Start

Read `seedance-couple-video-start.md` before compiling short relationship-motion prompts.

Current validated start:

`LEAN-IN MOMENT → SLOW APPROACH → MICRO-PAUSE → PRE-KISS PAUSE`

Use `LEAN-IN MOMENT` as the default first frame because it preserves motion room and lowers face-collision risk.

Use `PRE-KISS PAUSE` as a later tension beat / second keyframe rather than automatically starting at minimum face distance.

A current 5-second A/B generation showed that stronger romantic tension came from unresolved distance, pause and dimensional side/back light—not from using more aggressive “more intimate” wording or completing contact faster.

Do not complete a kiss unless that beat is explicitly requested.

---

## 10. Couple Identity Isolation

Always maintain:

`PERSON_A = USER_REFERENCE_PACKAGE`

`PERSON_B = PARTNER_REFERENCE_PACKAGE`

No face swap, feature fusion, hair / skin contamination, or identity convergence.

For multiple partner candidates, enforce candidate identity separation; do not reuse the same idealized attractive face with only styling / body changes.

---

## 11. QC Gate

A final image / short video must pass the relevant checks:

- user identity stability
- partner identity stability
- sweetness
- couple-likeness
- romantic chemistry
- partner attractiveness
- photorealism
- fantasy / shareability value
- natural contact geometry
- motion continuity when video is used
- no face fusion / hand-body penetration

Use:

- `validation/portrait-identity-lock-cases.md`
- `validation/archetype-benchmark.md`
- `validation/matching-moment-model-benchmark.md`
- `validation/partner-identity-lock-benchmark.md`
- `validation/seedance-couple-start-benchmark.md`

Only behavior supported by real generation evidence may be labeled runtime-validated.

---

## 12. Not Yet Verified / Future Modules

Do not invent production rules for these until separately researched and tested:

- large relation-action / pose library beyond the current validated core
- color-rich scene / wardrobe palette library
- stronger sensuality escalation system
- longer multi-shot Seedance 2.5 continuity
- automatic-cut relationship video grammar
- long multi-session partner identity persistence across many generations

---

## 13. Expansion Rule

Every new module follows:

`Research → Evidence / Reference Set → Distillation → Benchmark → Failure Analysis → Prompt Compensation → Validation → Add to Knowledge Module → Route from SKILL.md`

Do not over-test one module once practical evidence is sufficient. Advance when the current asset passes operational QC.

Keep `SKILL.md` as orchestration. Store heavy rules, libraries, model behavior and domain knowledge in modular `references/` files.