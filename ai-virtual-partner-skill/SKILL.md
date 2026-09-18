---
name: ai-virtual-partner-skill
description: Standalone AI virtual partner production skill for adult users. It can independently lock an uploaded user identity, resolve a suitable multi-orientation partner from curated libraries, route a compatible relationship combination with an explicit visual-intimacy level, write model-specific image prompts, and after image approval write a 10-second MiniMax H3 flirtatious interaction video prompt while preserving both identities.
---

# AI 虚拟伴侣｜AI Virtual Partner

## Product Goal

Turn one adult user's uploaded real photo into a believable fantasy relationship experience:

> preserve the real user → find a suitable attractive virtual partner → create a captured sweet / intimate / sensual relationship moment → after user approval, animate that approved image into a short flirtatious couple video.

The product is **not** a benchmark demo and not a formal couple-portrait generator.

The desired first impression is:

> “This looks like the best partner I somehow have not met yet.”

---

# Standalone Operating Contract｜独立运行总则

This Skill must work independently in a fresh session.

It must not depend on temporary chat memory, unstated benchmark context, or phrases such as `same as before`.

Read:

- `references/standalone-prompt-routing.md`

The Skill must independently support three modes.

### MODE A — IMAGE PROMPT ONLY

When the user asks only for a still-image prompt:

- lock the real user identity when a real photo is supplied;
- resolve / match a partner when needed;
- run `references/relationship-combination-router.md` to select a compatible Moment / Action / Expression-Gaze / Scene / Color-Wardrobe + Sensuality combination;
- choose the current image model route;
- output one self-contained, directly copyable final image prompt.

Do not require video planning in this mode.

### MODE B — VIDEO PROMPT ONLY

When the user asks only for a video prompt:

- prefer an approved couple image as first-frame visual truth;
- inherit USER and PARTNER identity references separately;
- inherit the approved relationship-combination state, scene, wardrobe and color state;
- compile a time-based interaction rather than rewriting a still-image prompt;
- output one self-contained, directly copyable MiniMax H3 prompt by current production default.

If identity continuity matters and no stable first frame exists, route first to image / first-frame creation.

### MODE C — END-TO-END

```text
USER PHOTO
→ USER IDENTITY LOCK
→ PARTNER RESOLVE / MATCH
→ PARTNER LOCK WHEN NEEDED
→ RELATIONSHIP COMBINATION ROUTER
→ FINAL IMAGE PROMPT / IMAGE
→ USER APPROVAL
→ APPROVED_COUPLE_IMAGE = VIDEO VISUAL TRUTH
→ FINAL 10s MINIMAX H3 VIDEO PROMPT / VIDEO
```

## Prompt Self-Containment

Every final image or video prompt must restate all production information the target model needs.

Image prompts should include, when relevant:

- visible subject assignments;
- identity preservation;
- partner identity / appearance route;
- relationship Moment;
- concrete Action / contact geometry;
- Expression / Gaze;
- Scene;
- physical Color / Wardrobe sources;
- visible sensuality / wardrobe-exposure / body-distance controls when relevant;
- camera / framing when useful;
- realism controls;
- model-specific compensation.

Video prompts should include, when relevant:

- first-frame / visual-truth authority;
- USER / PARTNER identity isolation;
- duration;
- Moment progression;
- Action progression;
- Expression / Gaze change triggered by each beat;
- shot size;
- camera position and movement for each explicit shot;
- cut logic;
- contact continuity;
- scene / wardrobe / color continuity;
- ending / closing hold;
- model-specific controls.

## Direct Prompt Request Rule

If the user explicitly asks for a prompt rather than media generation, output the final copyable prompt directly. Internal libraries make the decision; the final user-facing output stays simple.

---

# 1. Production Runtime Flow｜正式编排

```text
USER UPLOAD
↓
① USER IDENTITY LOCK
↓
USER_IDENTITY_CARD / USER_REFERENCE_PACKAGE
↓
USER PREFERENCE ROUTE
+
VISUAL_INTIMACY_LEVEL
↓
② PARTNER LIBRARY LOOKUP + MATCHING
↓
APPROVED PARTNER IDENTITY / PARTNER_REFERENCE_PACKAGE
↓
RELATIONSHIP COMBINATION ROUTER
↓
RELATIONSHIP_COMBINATION_CARD
↓
③ COUPLE IMAGE GENERATION / IMAGE PROMPT OUTPUT
↓
USER REVIEW
├─ NOT SATISFIED → minimum reroute: partner OR Moment/Action/Expression-Gaze OR Scene/Color
└─ APPROVED → freeze APPROVED_COUPLE_IMAGE
↓
④ VIDEO GENERATION / VIDEO PROMPT OUTPUT
APPROVED_COUPLE_IMAGE = FIRST FRAME
+ USER_REFERENCE_PACKAGE
+ PARTNER_REFERENCE_PACKAGE
+ APPROVED COMBINATION STATE / H3 CONTINUATION SEED
↓
MINIMAX H3
↓
10-SECOND FLIRTATIOUS / INTIMATE INTERACTION VIDEO
↓
IDENTITY + BODY CONTACT + EXPRESSION / GAZE + REALISM + MOTION QC
```

The user-approved couple image is the visual truth for video. Do not rebuild the couple from text after approval.

All people generated or transformed by this Skill are adults.

---

# 2. Stage ① — User Identity Lock

Read:

- `references/portrait-identity-lock.md`
- `references/identity-failure-recovery.md` only when identity failure is detected

Build:

- `USER_IDENTITY_CARD`
- `USER_REFERENCE_PACKAGE` when identity risk / downstream video complexity justifies it

Preserve hard identity anchors. Beautification, partner matching, pose, scene, color and video motion may not overwrite the user's face identity.

---

# 3. Stage ② — Partner Resolve from Libraries

Read only what is needed:

- `references/partner-archetype-library.md`
- `references/matching-engine.md`
- `references/partner-identity-lock.md`

Partner resolution must support at minimum:

- Woman × Man
- Man × Woman
- Woman × Woman
- Man × Man

User explicit choices override system priors, including partner gender, heritage appearance, adult visual-age direction, body-build preference, masculinity / femininity direction, attraction archetype and relationship temperature.

Keep:

`HERITAGE_APPEARANCE ≠ ARCHETYPE_ID`

Do not rank ethnic / racial groups by attractiveness. Do not output fake compatibility percentages.

After a partner is selected, freeze that partner into a reusable identity package when needed. Once approved, that specific person outranks the abstract Archetype.

---

# 4. Relationship Combination Router｜关系导演组合

Read:

- `references/relationship-combination-router.md`

The Router orchestrates existing assets; it does not replace their SSOT files.

Source libraries remain:

- `references/couple-moment-dna.md`
- `references/moment-type-library.md`
- `references/relation-action-library.md`
- `references/expression-gaze-library.md`
- `references/scene-tension-library.md`
- `references/color-wardrobe-library.md`
- `references/sensuality-intensity-layer.md`
- `references/editorial-intimacy-dna.md`

Responsibility boundaries:

```text
MOMENT = WHEN / RELATIONSHIP STATE
ACTION = BODY GEOMETRY / CONTACT
EXPRESSION / GAZE = VISIBLE FACE + EYE RESPONSE
SCENE = WHERE / PHYSICAL SPACE
COLOR / WARDROBE = PHYSICAL COLOR ASSIGNMENT
SENSUALITY = VISIBLE INTIMACY SCALE / SKIN EXPOSURE / BODY DISTANCE / CONTACT INTENSITY
EDITORIAL TREATMENT = COMPOSITION / MATERIAL / CAMERA PROXIMITY / LIGHT DIRECTION / NARRATIVE RESIDUE
ROUTER = WHICH COMPATIBLE SET TO USE TOGETHER
```

Default route:

```text
RELATIONSHIP TEMPERATURE + VISUAL_INTIMACY_LEVEL + VISUAL_TREATMENT_PROFILE
→ RELATIONSHIP COMBINATION ROUTER
→ MOMENT + ACTION + EXPRESSION/GAZE + SCENE + COLOR/WARDROBE + SENSUALITY PAYLOAD + EDITORIAL TREATMENT + CAMERA INTENT
→ COMPATIBILITY / RISK GATES
→ RELATIONSHIP_COMBINATION_CARD
```

Rules:

- explicit user choice wins unless physically / socially / identity / model incompatible;
- preserve `MICRO-EXPRESSION > EXAGGERATED PERFORMANCE`;
- preserve `COORDINATED ≠ IDENTICAL`;
- preserve `MORE TENSION ≠ MORE CONTACT`;
- preserve `RELATIONSHIP TEMPERATURE ≠ VISUAL INTIMACY LEVEL`;
- when the user wants a bolder result, translate it into wardrobe exposure + body distance + contact zone + gaze + framing instead of adding the word `sexy`;
- when the user wants a better-looking / more editorial result, route through `editorial-intimacy-dna.md`; do not solve it by adding `premium / cinematic / high-end`;
- default final fantasy couple images to `VT3 FRAGRANCE-CAMPAIGN TENSION + V3 BOLD SENSUAL` unless the user explicitly chooses a lower-intensity / cozy / UGC / conservative lifestyle route;
- both USER and PARTNER must show reciprocal emotion; one-sided chemistry is a QC failure;
- do not default every couple to one pose / room / palette;
- if a combination is high identity/anatomy risk, reduce the smallest risk variable instead of rebuilding identities.

---

# 5. Stage ③ — Couple Image Generation / Image Prompt Writer

Compile from:

```text
USER_IDENTITY_CARD
+
PARTNER_IDENTITY / PARTNER_APPEARANCE_CARD
+
RELATIONSHIP_COMBINATION_CARD
+
SENSUALITY PAYLOAD WHEN REQUESTED
+
EDITORIAL TREATMENT PAYLOAD
+
CAMERA REALISM
+
IMAGE MODEL ADAPTER
```

The card supplies the selected Moment, Action, Expression/Gaze, Scene, Color/Wardrobe, sensuality level/payload, contact geometry and camera framing intent.

Apply `VISIBLE SUBJECT FILTER` before final delivery. Never include `why_this_combination_internal` or internal matching rationale in the visible prompt.

Read:

- `references/relationship-combination-router.md`
- source relationship libraries only as needed to resolve explicit overrides / compatibility
- `references/model-routing-rules.md`
- `references/model-adaptation.md`
- `references/camera-realism-layer.md`
- `references/standalone-prompt-routing.md`

## Current Delivery Image Route

Default real-photo couple generation route:

`Banana2 Pro`

Use for believable candid photography, real skin / material feel and captured intimacy.

Current compact compensation may include:

- high-attractiveness adult couple;
- visible real skin pores / fine skin microtexture;
- slight natural imperfections;
- realistic candid photography;
- non-posed relationship moment;
- not overexposed;
- avoid milky / foggy white veil when observed;
- clear rendering.

Color and lighting remain subordinate to people + relationship action + scene.

## image 2.5 Role

Use image 2.5 especially for attractive partner exploration, archetype differentiation and canonical partner identity-sheet construction. Do not mechanically copy image 2.5 compensation into Banana2 Pro.

---

# 6. User Review Gate

After the couple image is generated, stop and let the user decide.

If dissatisfied, apply the smallest relevant reroute:

- change Partner → Matching Engine;
- `Try a Different Moment` → keep identities / partner lock; reroute Moment + Action + Expression/Gaze first; keep Scene/Color if compatible;
- change Scene → keep identities + compatible Moment/Action; reroute Scene + Color;
- adjust vibe → reroute Relationship Temperature + relationship assets, not Partner by default;
- too conservative / not sexy enough → increase `VISUAL_INTIMACY_LEVEL` and reroute wardrobe exposure + body distance + contact zone + gaze first; keep identities;
- high-end / luxury / hormonal / ambiguous / large-scale non-explicit request → route to the high-desire route in `editorial-intimacy-dna.md`: VT3 + V3 by default, V4 only when explicitly requested;
- too bold / too sexualized → reduce `VISUAL_INTIMACY_LEVEL` first; keep identities;
- identity changed → `identity-failure-recovery.md`.

Only rebuild an identity when identity itself failed.

If approved, freeze:

`APPROVED_COUPLE_IMAGE`

and preserve the approved `RELATIONSHIP_COMBINATION_CARD` as the starting relationship state for video.

---

# 7. Stage ④ — 10-Second MiniMax H3 Video / Video Prompt Writer

Read:

- `references/relationship-combination-router.md`
- `references/moment-type-library.md`
- `references/relation-action-library.md`
- `references/expression-gaze-library.md`
- `references/minimax-h3-couple-video.md`
- `references/model-adaptation.md`
- `references/standalone-prompt-routing.md`

Default target duration: `10 seconds`.

Inputs:

```text
APPROVED_COUPLE_IMAGE = FIRST FRAME
+
USER_REFERENCE_PACKAGE
+
PARTNER_REFERENCE_PACKAGE
+
APPROVED RELATIONSHIP_COMBINATION_CARD
```

Use the card's current state + `h3_continuation_seed` as planning input, but the approved couple image remains immediate visual truth.

Every explicit Beat combines:

`MOMENT STATE + ACTION CHANGE + EXPRESSION / GAZE CHANGE`.

Current production grammar:

`BEAT 1: ESTABLISH / INITIATE`
→ `CUT / SHOT CHANGE`
→ `BEAT 2: ESCALATE / REACT`
→ `CUT / SHOT CHANGE`
→ `BEAT 3: PAYOFF / HOLD / CLOSE`

A 10-second video normally contains at least three readable relationship beats and approximately two purposeful shot / framing changes unless the concept genuinely benefits from one continuous shot.

Preserve both identities, approved wardrobe / color direction, scene, body-contact continuity and a readable ending hold.

Do not use the historical Seedance single-shot slow-approach route as production default.

---

# 8. Identity Isolation

Always maintain:

`PERSON_A = USER`

`PERSON_B = PARTNER`

No face swap, facial fusion, skin/hair contamination, identity convergence, or rebuilding identities from text after reliable references exist.

If identity failure occurs, route to `references/identity-failure-recovery.md` rather than restarting Matching / director routing.

---

# 9. QC Gate

## Image QC

Check:

- user identity stability;
- partner identity stability;
- partner attractiveness;
- couple-likeness;
- sweetness / chemistry;
- requested sensuality / visual-intimacy level is visibly achieved without relying on abstract adjectives;
- readable Moment state;
- reciprocal Expression / Gaze on both USER and PARTNER; blank / cold USER with affectionate Partner = fail;
- editorial treatment quality: asymmetry, body line, material contrast, directional light, and non-stock-photo staging when the route calls for it;
- Concept-image DNA acceptance gate for V3/VT3+: at least 5/7 of visible body line, close body distance, meaningful waist/hip/back/collar contact, reciprocal expression, asymmetric intimate framing, refined private scene, directional physical light;
- natural body-contact geometry;
- scene/action physical compatibility;
- photographic realism;
- wardrobe / background separation;
- stable identity skin tone under selected palette;
- shareability / fantasy value.

## Video QC

Also check:

- first-frame continuity;
- no identity drift / face fusion;
- no hand / limb penetration;
- continuous contact geometry;
- physically plausible motion;
- facial changes have visible causes;
- wardrobe and scene color continuity;
- three readable relationship beats by default;
- motivated shot / framing variation;
- ending does not switch people / scene / wardrobe.

---

# 10. Asset Libraries vs Product Runtime

Benchmarking is not a product step. Tests exist only to improve reusable libraries and routing decisions.

Read:

- `references/asset-library-governance.md`

Do not expose benchmark complexity to normal users.

---

# 11. Knowledge Modules

Current modular knowledge base:

- `references/portrait-identity-lock.md`
- `references/identity-failure-recovery.md`
- `references/partner-archetype-library.md`
- `references/matching-engine.md`
- `references/partner-identity-lock.md`
- `references/couple-moment-dna.md`
- `references/moment-type-library.md`
- `references/relation-action-library.md`
- `references/expression-gaze-library.md`
- `references/scene-tension-library.md`
- `references/color-wardrobe-library.md`
- `references/sensuality-intensity-layer.md`
- `references/relationship-combination-router.md`
- `references/model-routing-rules.md`
- `references/model-adaptation.md`
- `references/camera-realism-layer.md`
- `references/minimax-h3-couple-video.md`
- `references/standalone-prompt-routing.md`
- `references/seedance-couple-video-start.md` — historical evidence only
- `references/asset-library-governance.md`

Future libraries should stay modular. `SKILL.md` remains orchestration only.

---

# 12. Expansion Rule

Use:

`Research / Reference → Distill into Asset → Small Representative Validation → Record Reusable Failure / Compensation → Add to Library`

Do not repeatedly isolate-test tiny variables once practical evidence is sufficient.

Only run additional A/B tests when the result would change a concrete routing or library decision.

---

# 13. Fresh-Session Requirement｜新会话可独立工作

A fresh-session invocation must be sufficient to perform the production workflow.

`CURRENT USER INPUT + CURRENT SKILL KNOWLEDGE BASE = COMPLETE PROMPT OUTPUT`

When asked only for a prompt, stop at prompt delivery. When asked for end-to-end work, continue through approval and compile video from the approved couple image.