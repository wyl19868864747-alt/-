---
name: ai-virtual-partner-skill
description: AI virtual partner generation workflow for adult users. The production flow locks the uploaded user identity, resolves a suitable multi-orientation partner from curated partner libraries, selects relationship actions/scenes/colors from validated asset libraries, generates a sweet intimate couple image, then converts the user-approved image into a 10-second MiniMax H3 flirtatious interaction video while preserving both identities.
---

# AI 虚拟伴侣｜AI Virtual Partner

## Product Goal

Turn one adult user's uploaded real photo into a believable fantasy relationship experience:

> preserve the real user → find a suitable attractive virtual partner → create a captured sweet / intimate relationship moment → after user approval, animate that approved image into a short flirtatious couple video.

The product is **not** a benchmark demo and not a formal couple-portrait generator.

The desired first impression is:

> “This looks like the best partner I somehow have not met yet.”

---

# 1. Production Runtime Flow｜正式编排

```text
USER UPLOAD
↓
① USER IDENTITY LOCK
↓
USER_IDENTITY_CARD / USER_REFERENCE_PACKAGE
↓
USER PREFERENCE ROUTE (optional / explicit user choice wins)
↓
② PARTNER LIBRARY LOOKUP + MATCHING
↓
APPROVED PARTNER IDENTITY / PARTNER_REFERENCE_PACKAGE
↓
ACTION + MOMENT + SCENE + COLOR LIBRARY LOOKUP
↓
③ COUPLE IMAGE GENERATION
↓
USER REVIEW
├─ NOT SATISFIED → reroute partner / action / scene / relationship temperature with minimum necessary change
└─ APPROVED → freeze APPROVED_COUPLE_IMAGE
↓
④ VIDEO GENERATION
APPROVED_COUPLE_IMAGE = FIRST FRAME
+ USER_REFERENCE_PACKAGE
+ PARTNER_REFERENCE_PACKAGE
↓
MINIMAX H3
↓
10-SECOND FLIRTATIOUS / INTIMATE INTERACTION VIDEO
↓
IDENTITY + BODY CONTACT + REALISM + MOTION QC
```

The user-approved couple image is the visual truth for the video. Do not rebuild the couple from text after approval.

All people generated or transformed by this Skill are adults.

---

# 2. Stage ① — User Identity Lock

Read:

- `references/portrait-identity-lock.md`

Goal:

`LOCK WHO THE USER IS BEFORE ANY FANTASY GENERATION`

Build:

- `USER_IDENTITY_CARD`
- `USER_REFERENCE_PACKAGE` when identity risk / downstream video complexity justifies it

Preserve hard identity anchors. Beautification, partner matching, pose, scene, color and video motion may not overwrite the user's face identity.

The four-view logic is an identity-support asset, not a mandatory visible product step. It may be inferred / generated internally only when useful.

---

# 3. Stage ② — Partner Resolve from Libraries

Read only what is needed:

- `references/partner-archetype-library.md`
- `references/matching-engine.md`
- `references/partner-identity-lock.md`

Partner resolution must support multiple adult orientation routes, including at minimum:

- Woman × Man
- Man × Woman
- Woman × Woman
- Man × Man

User explicit choices override system priors, including:

- partner gender
- heritage appearance
- visual age range
- body-build preference
- masculinity / femininity direction
- attraction archetype
- relationship temperature

Keep:

`HERITAGE_APPEARANCE ≠ ARCHETYPE_ID`

Do not rank ethnic / racial groups by attractiveness. Do not output fake compatibility percentages.

The matching engine exists to choose plausible, attractive candidates and avoid obvious visual mismatch—not to claim scientific destiny.

After a partner is selected, freeze that partner into a reusable identity package when needed for complex image / video generation.

---

# 4. Asset Library Lookup｜动作 / 场景 / 色彩不是临场乱写

The production image should be assembled from validated asset libraries.

Read as needed:

- `references/couple-moment-dna.md`
- `references/moment-type-library.md`
- `references/relation-action-library.md`
- `references/scene-tension-library.md`
- future `references/color-scene-library.md`

Resolve the relationship image from:

```text
COUPLE MOMENT
+
RELATION ACTION
+
SCENE
+
COLOR / WARDROBE PALETTE
+
EXPRESSION / GAZE
+
RELATIONSHIP TEMPERATURE
```

Do not default every couple to one pose, one neutral room or one black / white / grey wardrobe.

The current visual direction favors captured relationship moments:

- direct / meaningful eye contact
- natural body contact
- weight transfer / leaning
- clear romantic partner geometry
- unresolved near-contact when tension is desired
- non-formal, non-passport, non-wedding-photo posing

Current validated action families include:

- `FACE-TO-FACE WAIST HOLD + BREATH-CLOSE`
- `PROTECTIVE SIDE EMBRACE`
- `BACK HUG`
- `SHOULDER / SIDE LEAN`

These are library assets, not the complete future pose inventory.

---

# 5. Stage ③ — Couple Image Generation

## Current Delivery Image Route

Default current real-photo couple generation route:

`Banana2 Pro`

Use it for the user-facing couple image when the target is believable candid photography, real skin / material feel and captured intimacy.

Read:

- `references/model-routing-rules.md`
- `references/model-adaptation.md`
- `references/camera-realism-layer.md`

Current Banana2 Pro compensation may include:

- high-attractiveness adult couple
- visible real skin pores / fine skin texture
- slight natural imperfections
- realistic photography
- non-posed relationship moment
- image not overexposed
- avoid milky / foggy white veil when observed
- clear, transparent image rendering

Do not over-stack tonal restrictions when they make the image flat.

## image 2.5 Role

Use image 2.5 when its strengths are specifically needed, especially:

- attractive partner exploration
- archetype differentiation
- canonical partner identity-sheet construction
- high-attraction fantasy / hero alternatives

Current image 2.5 compensation remains model-specific and should not be copied mechanically into Banana2 Pro.

---

# 6. User Review Gate

After the couple image is generated, stop and let the user decide whether it is acceptable.

If the user is not satisfied, do **not** restart the whole pipeline automatically.

Apply the smallest relevant reroute, for example:

- keep user identity, change partner
- keep both identities, change action
- keep identities + action, change scene / color
- keep composition, adjust relationship temperature / gaze / expression

Only rebuild an identity when identity itself failed.

If the user approves the image, freeze it as:

`APPROVED_COUPLE_IMAGE`

That approved image becomes the first-frame anchor for video.

---

# 7. Stage ④ — 10-Second MiniMax H3 Video

Read:

- `references/minimax-h3-couple-video.md`
- `references/model-adaptation.md`

Default target duration:

`10 seconds`

Inputs:

```text
APPROVED_COUPLE_IMAGE = FIRST FRAME
+
USER_REFERENCE_PACKAGE
+
PARTNER_REFERENCE_PACKAGE
```

Video goal:

- preserve both faces / hairlines / ages / body identities
- continue the relationship already visible in the approved image
- create a visibly evolving flirtatious / intimate interaction rather than stretching one micro-action across ten seconds
- increase chemistry through motion, gaze, touch, posture change, proximity and reaction
- use shot-size / angle variation and natural cuts when the model can execute them
- allow stronger sensuality only within the platform / model's permitted adult-content range
- do not turn the video into a generic montage unrelated to the approved first frame

Current production grammar:

`BEAT 1: ESTABLISH / INITIATE`
→ `CUT / SHOT CHANGE`
→ `BEAT 2: ESCALATE PHYSICAL / EMOTIONAL CONTACT`
→ `CUT / SHOT CHANGE`
→ `BEAT 3: PAYOFF / HOLD / CLOSE`

A 10-second video should normally contain at least **three readable relationship beats** and approximately **two purposeful shot / framing changes** unless a specific concept genuinely benefits from one continuous shot.

Do not use the previous Seedance single-shot slow-approach template as the production default. Real testing showed it was too conservative and visually repetitive for a full 10-second delivery; an attempted higher-tension Seedance variant also failed in the current runtime. Seedance findings remain historical evidence only.

---

# 8. Identity Isolation

Always maintain:

`PERSON_A = USER`

`PERSON_B = PARTNER`

No:

- face swap
- facial feature fusion
- skin / hair contamination
- candidate identity convergence
- rebuilding identities from text after an approved image exists

---

# 9. QC Gate

## Image QC

Check:

- user identity stability
- partner identity stability
- partner attractiveness
- couple-likeness
- sweetness / romantic chemistry
- natural body-contact geometry
- photographic realism
- shareability / fantasy value

## Video QC

Also check:

- first-frame continuity
- no identity drift during motion
- no face fusion at close distance
- no hand / limb penetration
- continuous contact geometry
- physically plausible motion
- at least three readable relationship beats for the default 10-second route
- shot / framing variation feels motivated rather than random
- ending does not accidentally switch people / scene / wardrobe

---

# 10. Asset Libraries vs Product Runtime

**Benchmarking is not a product step.**

All current research / generation tests exist only to improve the reusable asset libraries:

- what attractive partner archetypes work
- whether uploaded real users can be identity-locked
- which partner matches plausibly with which user / preference
- which actions create sweetness / tension
- which scenes / colors increase visual appeal
- which model best executes each asset type
- which video interaction grammars preserve identity while remaining engaging

Read:

- `references/asset-library-governance.md`

Do not expose internal benchmark complexity to normal product users.

---

# 11. Knowledge Modules

Current modular knowledge base:

- `references/portrait-identity-lock.md`
- `references/partner-archetype-library.md`
- `references/matching-engine.md`
- `references/partner-identity-lock.md`
- `references/couple-moment-dna.md`
- `references/moment-type-library.md`
- `references/relation-action-library.md`
- `references/scene-tension-library.md`
- `references/model-routing-rules.md`
- `references/model-adaptation.md`
- `references/camera-realism-layer.md`
- `references/minimax-h3-couple-video.md`
- `references/seedance-couple-video-start.md` — historical Seedance test evidence only; not current production runtime.
- `references/asset-library-governance.md`

Future libraries should stay modular. `SKILL.md` remains the orchestration layer.

---

# 12. Expansion Rule

Use:

`Research / Reference → Distill into Asset → Small Representative Validation → Record Reusable Failure / Compensation → Add to Library`

Do **not** repeatedly isolate-test tiny variables once practical evidence is sufficient.

When safe and interpretable, combine multiple creative variables in one representative test, such as:

`partner type + action + scene + color + expression + relationship state`

Only run additional A/B tests when the result would change a concrete routing or library decision.

The goal is a strong production library, not an endless benchmark set.
