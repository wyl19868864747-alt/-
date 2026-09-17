---
name: ai-virtual-partner-skill
description: Standalone AI virtual partner production skill for adult users. It can independently lock an uploaded user identity, resolve a suitable multi-orientation partner from curated libraries, route relationship moment/action/expression/scene/color, write model-specific image prompts, and after image approval write a 10-second MiniMax H3 flirtatious interaction video prompt while preserving both identities.
---

# AI 虚拟伴侣｜AI Virtual Partner

## Product Goal

Turn one adult user's uploaded real photo into a believable fantasy relationship experience:

> preserve the real user → find a suitable attractive virtual partner → create a captured sweet / intimate relationship moment → after user approval, animate that approved image into a short flirtatious couple video.

The product is **not** a benchmark demo and not a formal couple-portrait generator.

The desired first impression is:

> “This looks like the best partner I somehow have not met yet.”

---

# Standalone Operating Contract｜独立运行总则

This Skill must work independently in a fresh session.

It must not depend on:

- this week's benchmark context;
- temporary chat memory;
- unstated earlier prompt experiments;
- phrases such as `same as before` or `continue the previous route`.

Read:

- `references/standalone-prompt-routing.md`

The Skill must independently support three modes:

### MODE A — IMAGE PROMPT ONLY

When the user asks only for a still-image prompt:

- lock the real user identity when a real photo is supplied;
- resolve / match a partner when needed;
- route Moment → Action → Expression / Gaze → Scene → Color / Wardrobe;
- choose the current image model route;
- output one self-contained, directly copyable final image prompt.

Do not require video planning in this mode.

### MODE B — VIDEO PROMPT ONLY

When the user asks only for a video prompt:

- prefer an approved couple image as first-frame visual truth;
- inherit USER and PARTNER identity references separately;
- inherit the approved scene / wardrobe / color state;
- read the current Moment / Action / Expression-Gaze state;
- compile a time-based interaction rather than rewriting a still-image prompt;
- output one self-contained, directly copyable MiniMax H3 prompt by current production default.

If identity continuity matters and no stable first frame exists, route first to image / first-frame creation instead of pretending video continuity is already solved.

### MODE C — END-TO-END

When the user wants the full workflow:

```text
USER PHOTO
→ USER IDENTITY LOCK
→ PARTNER RESOLVE / MATCH
→ MOMENT
→ ACTION
→ EXPRESSION / GAZE
→ SCENE
→ COLOR / WARDROBE
→ FINAL IMAGE PROMPT / IMAGE
→ USER APPROVAL
→ APPROVED_COUPLE_IMAGE = VIDEO VISUAL TRUTH
→ FINAL 10s MINIMAX H3 VIDEO PROMPT / VIDEO
```

## Prompt Self-Containment

Every final image or video prompt must restate all production information the target model needs.

Do not rely on hidden project history.

Image prompts should include, when relevant:

- visible subject assignments;
- identity preservation;
- partner identity / appearance route;
- relationship Moment;
- concrete Action / contact geometry;
- Expression / Gaze;
- Scene;
- physical Color / Wardrobe sources;
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
- camera position and camera movement for each explicit shot;
- cut logic;
- contact continuity;
- scene / wardrobe / color continuity;
- ending / closing hold;
- model-specific controls.

## Direct Prompt Request Rule

If the user explicitly asks for a prompt rather than asking the Skill to generate the media itself, output the final copyable prompt directly.

Do not require the user to know internal library names.

The internal libraries make the decision; the final user-facing output should remain simple.

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
MOMENT → ACTION → EXPRESSION / GAZE → SCENE → COLOR / WARDROBE LOOKUP
↓
③ COUPLE IMAGE GENERATION / IMAGE PROMPT OUTPUT
↓
USER REVIEW
├─ NOT SATISFIED → reroute partner / Moment / Action / Expression-Gaze / Scene / Color with minimum necessary change
└─ APPROVED → freeze APPROVED_COUPLE_IMAGE
↓
④ VIDEO GENERATION / VIDEO PROMPT OUTPUT
APPROVED_COUPLE_IMAGE = FIRST FRAME
+ USER_REFERENCE_PACKAGE
+ PARTNER_REFERENCE_PACKAGE
↓
MINIMAX H3
↓
10-SECOND FLIRTATIOUS / INTIMATE INTERACTION VIDEO
↓
IDENTITY + BODY CONTACT + EXPRESSION / GAZE + REALISM + MOTION QC
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

# 4. Asset Library Lookup｜关系状态 / 动作 / 表情 / 场景 / 色彩不是临场乱写

The production image should be assembled from reusable asset libraries.

Read as needed:

- `references/couple-moment-dna.md`
- `references/moment-type-library.md`
- `references/relation-action-library.md`
- `references/expression-gaze-library.md`
- `references/scene-tension-library.md`
- `references/color-wardrobe-library.md`

Keep responsibility boundaries strict:

```text
MOMENT = WHEN / RELATIONSHIP STATE
ACTION = BODY GEOMETRY / CONTACT
EXPRESSION / GAZE = VISIBLE FACE + EYE RESPONSE
SCENE = WHERE / PHYSICAL SPACE
COLOR / WARDROBE = PHYSICAL COLOR ASSIGNMENT
```

Default runtime order:

```text
RELATIONSHIP TEMPERATURE
→ MOMENT STATE
→ ACTION FAMILY
→ EXPRESSION / GAZE PATTERN
→ SCENE FAMILY
→ COLOR / WARDROBE FAMILY
```

Scene selection answers **where colors can physically exist**. `color-wardrobe-library.md` decides **how those colors are assigned to Person A / Person B / environment / light**.

Do not default every couple to one pose, one fixed smile, one neutral room or one black / white / grey wardrobe.

The current visual direction favors captured relationship moments:

- direct / meaningful partner attention;
- natural body contact;
- weight transfer / leaning;
- clear romantic partner geometry;
- reciprocal facial response;
- unresolved near-contact when tension is desired;
- non-formal, non-passport, non-wedding-photo posing.

Current validated action families include:

- `FACE-TO-FACE WAIST HOLD + BREATH-CLOSE`
- `PROTECTIVE SIDE EMBRACE`
- `BACK HUG`
- `SHOULDER / SIDE LEAN`

Current validated / production-ready Moment defaults include:

- `PRIVATE EYE CONTACT`
- `SOFT ALMOST-CONTACT`
- `UNRESOLVED CLOSE`
- `REACTION SMILE`
- `POST-CONTACT PULLBACK`

Expression routing must follow:

`MICRO-EXPRESSION > EXAGGERATED PERFORMANCE`

Do not make both adults perform the same smile / gaze behavior by default. One initiates; the other reacts.

Color routing must follow:

`COORDINATED ≠ IDENTICAL`

Use physical wardrobe / environment / light sources. Color remains subordinate to people, relationship action and scene.

---

# 5. Stage ③ — Couple Image Generation / Image Prompt Writer

## Independent Image Prompt Writer

When the user asks for a still-image prompt, compile independently from:

```text
USER_IDENTITY_CARD
+
PARTNER_IDENTITY / PARTNER_APPEARANCE_CARD
+
MOMENT_STATE
+
RELATION_ACTION
+
EXPRESSION / GAZE
+
SCENE
+
COLOR / WARDROBE
+
CAMERA REALISM
+
IMAGE MODEL ADAPTER
```

Apply the `VISIBLE SUBJECT FILTER` before the final prompt. Internal matching rationale must not accidentally become visible scene content.

The final prompt must be directly copyable and may not rely on prior chat shorthand.

Read:

- `references/moment-type-library.md`
- `references/relation-action-library.md`
- `references/expression-gaze-library.md`
- `references/scene-tension-library.md`
- `references/color-wardrobe-library.md`
- `references/model-routing-rules.md`
- `references/model-adaptation.md`
- `references/camera-realism-layer.md`
- `references/standalone-prompt-routing.md`

## Current Delivery Image Route

Default current real-photo couple generation route:

`Banana2 Pro`

Use it for the user-facing couple image when the target is believable candid photography, real skin / material feel and captured intimacy.

Current Banana2 Pro compensation may include:

- high-attractiveness adult couple;
- visible real skin pores / fine skin texture;
- slight natural imperfections;
- realistic candid photography;
- non-posed relationship moment;
- image not overexposed;
- avoid milky / foggy white veil when observed;
- clear, transparent image rendering.

Color prompts for Banana2 Pro should stay compact. Do not let long palette / lighting constraints flatten the image or overpower identity and relationship action.

Expression / gaze prompts should also stay compact. One immediately readable state is enough for a still image.

## image 2.5 Role

Use image 2.5 when its strengths are specifically needed, especially:

- attractive partner exploration;
- archetype differentiation;
- canonical partner identity-sheet construction;
- high-attraction fantasy / hero alternatives.

Current image 2.5 compensation remains model-specific and should not be copied mechanically into Banana2 Pro.

Color instructions for image 2.5 should protect against grey / muddy / cement-like rendering using concise, physically assigned color anchors rather than a long grading description.

---

# 6. User Review Gate

After the couple image is generated, stop and let the user decide whether it is acceptable.

If the user is not satisfied, do **not** restart the whole pipeline automatically.

Apply the smallest relevant reroute, for example:

- keep user identity, change partner;
- keep both identities, change Action;
- keep Action, change Moment / Expression-Gaze;
- keep identities + Action, change Scene / Color;
- keep composition, adjust relationship temperature / gaze / expression.

Only rebuild an identity when identity itself failed.

If the user approves the image, freeze it as:

`APPROVED_COUPLE_IMAGE`

That approved image becomes the first-frame anchor for video, including its Moment state, hand/body geometry, expression/gaze state, wardrobe and scene color state.

---

# 7. Stage ④ — 10-Second MiniMax H3 Video / Video Prompt Writer

Read:

- `references/moment-type-library.md`
- `references/relation-action-library.md`
- `references/expression-gaze-library.md`
- `references/minimax-h3-couple-video.md`
- `references/model-adaptation.md`
- `references/standalone-prompt-routing.md`

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

## Independent Video Prompt Writer

When the user asks for a video prompt, compile independently from the approved first frame and current identity packages.

Every explicit Beat should combine:

`MOMENT STATE + ACTION CHANGE + EXPRESSION / GAZE CHANGE`

The prompt must explicitly include:

- who each person is / which reference belongs to which person;
- first-frame visual truth;
- current body and hand geometry;
- current Moment / Expression-Gaze state;
- 10-second Beat progression;
- camera / cut progression;
- continuity rules;
- closing beat.

Do not merely append motion words to the still-image prompt.

Video goal:

- preserve both faces / hairlines / ages / body identities;
- preserve approved wardrobe colors and scene warm/cool direction across cuts;
- continue the relationship already visible in the approved image;
- create visibly evolving Moment / Action / Expression changes rather than stretching one micro-action across ten seconds;
- increase chemistry through motion, gaze, touch, posture change, proximity and reaction;
- use shot-size / angle variation and natural cuts when the model can execute them;
- allow stronger sensuality only within the platform / model's permitted adult-content range;
- do not turn the video into a generic montage unrelated to the approved first frame.

Current production grammar:

`BEAT 1: ESTABLISH / INITIATE`
→ `CUT / SHOT CHANGE`
→ `BEAT 2: ESCALATE / REACT`
→ `CUT / SHOT CHANGE`
→ `BEAT 3: PAYOFF / HOLD / CLOSE`

A 10-second video should normally contain at least **three readable relationship beats** and approximately **two purposeful shot / framing changes** unless a specific concept genuinely benefits from one continuous shot.

Expression / gaze should change because of the interaction, not randomly. Avoid holding one fixed “sexy stare” for the full clip.

Do not use the previous Seedance single-shot slow-approach template as the production default. Real testing showed it was too conservative and visually repetitive for a full 10-second delivery; an attempted higher-tension Seedance variant also failed in the current runtime. Seedance findings remain historical evidence only.

---

# 8. Identity Isolation

Always maintain:

`PERSON_A = USER`

`PERSON_B = PARTNER`

No:

- face swap;
- facial feature fusion;
- skin / hair contamination;
- candidate identity convergence;
- rebuilding identities from text after an approved image exists.

---

# 9. QC Gate

## Image QC

Check:

- user identity stability;
- partner identity stability;
- partner attractiveness;
- couple-likeness;
- sweetness / romantic chemistry;
- readable Moment state;
- reciprocal Expression / Gaze rather than duplicated performance;
- natural body-contact geometry;
- photographic realism;
- wardrobe / background separation;
- skin tone remains identity-consistent under the selected palette;
- shareability / fantasy value.

## Video QC

Also check:

- first-frame continuity;
- no identity drift during motion;
- no face fusion at close distance;
- no hand / limb penetration;
- continuous contact geometry;
- physically plausible motion;
- Moment / Expression / Gaze changes have visible causes;
- wardrobe color does not change across cuts;
- scene dominant colors / warm-cool direction remain stable;
- at least three readable relationship beats for the default 10-second route;
- shot / framing variation feels motivated rather than random;
- ending does not accidentally switch people / scene / wardrobe.

---

# 10. Asset Libraries vs Product Runtime

**Benchmarking is not a product step.**

All current research / generation tests exist only to improve the reusable asset libraries:

- what attractive partner archetypes work;
- whether uploaded real users can be identity-locked;
- which partner matches plausibly with which user / preference;
- which Moments / Actions create sweetness / tension;
- which Expression / Gaze patterns make the relationship read correctly;
- which scenes / colors increase visual appeal;
- which model best executes each asset type;
- which video interaction grammars preserve identity while remaining engaging.

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
- `references/expression-gaze-library.md`
- `references/scene-tension-library.md`
- `references/color-wardrobe-library.md`
- `references/model-routing-rules.md`
- `references/model-adaptation.md`
- `references/camera-realism-layer.md`
- `references/minimax-h3-couple-video.md`
- `references/standalone-prompt-routing.md`
- `references/seedance-couple-video-start.md` — historical Seedance test evidence only; not current production runtime.
- `references/asset-library-governance.md`

Future libraries should stay modular. `SKILL.md` remains the orchestration layer.

---

# 12. Expansion Rule

Use:

`Research / Reference → Distill into Asset → Small Representative Validation → Record Reusable Failure / Compensation → Add to Library`

Do **not** repeatedly isolate-test tiny variables once practical evidence is sufficient.

When safe and interpretable, combine multiple creative variables in one representative test, such as:

`partner type + Moment + Action + Expression / Gaze + Scene + Color`

Only run additional A/B tests when the result would change a concrete routing or library decision.

The goal is a strong production library, not an endless benchmark set.

---

# 13. Fresh-Session Requirement｜新会话可独立工作

A fresh-session invocation of this Skill must be sufficient to perform the production workflow.

Runtime requirement:

`CURRENT USER INPUT + CURRENT SKILL KNOWLEDGE BASE = COMPLETE PROMPT OUTPUT`

The Skill may read its own knowledge files and the user's current assets, but it must not require knowledge of how the rules were discovered or what temporary conversation produced them.

When asked only for a prompt, the Skill must be able to stop at the prompt-delivery stage without requiring media generation.

When asked for end-to-end work, it should continue through the approval gate and then compile the video prompt from the approved couple image.