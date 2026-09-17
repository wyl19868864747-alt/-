---
name: ai-virtual-partner-skill
description: AI virtual partner image and video generation skill. Current verified scope covers user portrait identity locking, partner archetype resolution, matching modes, partner identity locking, sweet-couple moment routing, camera realism controls, and model-specific image routing. Full pose/scene libraries and image-to-video continuity remain separate future modules.
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
MODEL ROUTER
↓
MODEL-SPECIFIC PROMPT
↓
IDENTITY + CHEMISTRY + REALISM QC
```

## Required Knowledge Modules

Read only the modules needed by the current stage:

- `references/portrait-identity-lock.md` — lock uploaded user identity, four-view logic, drift prevention.
- `references/partner-archetype-library.md` — adult partner appearance archetypes.
- `references/matching-engine.md` — Harmony / Preference / Complementary Contrast routing.
- `references/partner-identity-lock.md` — freeze an approved partner into a reusable identity / reference package.
- `references/couple-moment-dna.md` — sweet, intimate, non-formal couple-image DNA.
- `references/moment-type-library.md` — validated sweet-moment types and their use cases.
- `references/model-routing-rules.md` — choose image 2.5 vs Banana2 Pro by product target.
- `references/model-adaptation.md` — compile different prompts for image 2.5 / Banana2 Pro / Seedance 2.5.
- `references/camera-realism-layer.md` — real skin / exposure / camera texture controls.

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

## 5. Couple Moment Router

Read `couple-moment-dna.md` and `moment-type-library.md`.

Default product goal:

> The first impression should be sweet, intimate and slightly heart-fluttering—“this is what my unknown best partner looks like.”

Validated moments:

- `SOFT_ALMOST_KISS` — default Hero / strongest romantic-tension moment.
- `CLOSE_EYE_CONTACT` — default realistic sweet moment.
- `SHOULDER_LEAN` — safe long-term sweetness / secondary moment.

Avoid defaulting to stiff, front-facing formal couple portraits.

---

## 6. Model Router

Read `model-routing-rules.md` and `model-adaptation.md`.

### Default Hero Route

`image 2.5`

Use for:

- highest partner attractiveness
- hero / cover result
- strongest best-partner fantasy
- Soft Almost-Kiss / heart-flutter moments
- current preferred partner canonical reference-sheet construction

Apply validated compensation for noise / grey / dark rendering and anti-redesign controls during identity completion.

### Real / Candid Route

`Banana2 Pro`

Use for:

- stronger real-photo feel
- candid couple photography
- low generation noise
- natural heritage appearance
- photographic realism support

Apply skin-microtexture + exposure / highlight controls. Do not overuse film-grain / sensor-texture wording.

Never mechanically reuse one prompt across models.

---

## 7. Camera Realism

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

## 8. Couple Identity Isolation

Always maintain:

`PERSON_A = USER_REFERENCE_PACKAGE`

`PERSON_B = PARTNER_REFERENCE_PACKAGE`

No face swap, feature fusion, hair / skin contamination, or identity convergence.

For multiple partner candidates, enforce candidate identity separation; do not reuse the same idealized attractive face with only styling / body changes.

---

## 9. QC Gate

A final couple image must pass:

- user identity stability
- partner identity stability
- sweetness
- couple-likeness
- romantic chemistry
- partner attractiveness
- photorealism
- fantasy / shareability value

Use:

- `validation/portrait-identity-lock-cases.md`
- `validation/archetype-benchmark.md`
- `validation/matching-moment-model-benchmark.md`
- `validation/partner-identity-lock-benchmark.md`

Only behavior supported by real generation evidence may be labeled runtime-validated.

---

## 10. Not Yet Verified / Future Modules

Do not invent production rules for these until separately researched and tested:

- full relation-action / pose library
- full intimate scene library
- stronger sensuality escalation system
- image-to-video continuity engine
- Seedance 2.5 couple-video benchmark
- long multi-session partner identity persistence across many generations

---

## 11. Expansion Rule

Every new module follows:

`Research → Evidence / Reference Set → Distillation → Benchmark → Failure Analysis → Prompt Compensation → Validation → Add to Knowledge Module → Route from SKILL.md`

Do not over-test one module once practical evidence is sufficient. Advance when the current asset passes operational QC.

Keep `SKILL.md` as orchestration. Store heavy rules, libraries, model behavior and domain knowledge in modular `references/` files.