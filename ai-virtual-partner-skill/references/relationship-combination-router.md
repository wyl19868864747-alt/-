# Relationship Combination Router｜情侣导演组合路由器

## Purpose

Choose a **compatible set of existing relationship assets** for one adult couple image and its possible MiniMax H3 continuation.

This file is orchestration only.

`ROUTER = ORCHESTRATION / COMPATIBILITY`

`LIBRARIES = ASSET SOURCE / SSOT`

Do not redefine Moment, Action, Expression/Gaze, Scene, Color/Wardrobe or Partner Archetypes here. Always read current IDs, status, compatibility and risk from their source libraries.

Runtime:

```text
USER + SELECTED / APPROVED PARTNER
+
RELATIONSHIP TEMPERATURE
+
VISUAL_INTIMACY_LEVEL
+
VISUAL_TREATMENT_PROFILE
+
EXPLICIT USER CHOICES
+
CURRENT BODY GEOMETRY
+
TARGET MODEL
+
RECENT COMBINATION HISTORY
↓
COMBINATION ROUTER
↓
MOMENT + ACTION + EXPRESSION/GAZE + SCENE + COLOR/WARDROBE + SENSUALITY PAYLOAD + EDITORIAL TREATMENT + CAMERA INTENT
↓
COMPATIBILITY / RISK GATES
↓
RELATIONSHIP_COMBINATION_CARD
↓
IMAGE PROMPT WRITER
↓
APPROVED FIRST FRAME
↓
MINIMAX H3 CONTINUATION
```

All people are adults. Role assignment is gender-neutral.

---

# 1. Inputs

The router may read:

- `USER_IDENTITY_CARD`
- `PARTNER_IDENTITY_CARD` or `MATCH_CANDIDATE_CARD`
- `RELATIONSHIP_TEMPERATURE`
- `VISUAL_INTIMACY_LEVEL`
- `VISUAL_TREATMENT_PROFILE`
- `USER_EXPLICIT_MOMENT_PREFERENCE`
- `USER_EXPLICIT_ACTION_PREFERENCE`
- `USER_EXPLICIT_SCENE_PREFERENCE`
- `USER_EXPLICIT_COLOR_PREFERENCE`
- `CURRENT_BODY_GEOMETRY`
- `TARGET_MODEL`
- `PREVIOUS_APPROVED_ASSETS`
- `RECENT_COMBINATION_HISTORY`
- `EXCLUDED_RECENT_COMBINATIONS`

If the user has made an explicit valid choice, preserve it unless it fails physical, social-role, identity or model-stability checks.

---

# 2. Decision Priority

Fixed priority:

```text
EXPLICIT USER CHOICE
>
IDENTITY STABILITY
>
PHYSICAL / SOCIAL COMPATIBILITY
>
VALIDATED CORE ASSET
>
RELATIONSHIP TEMPERATURE FIT
>
VIDEO CONTINUATION VALUE
>
VISUAL DIVERSITY / ROTATION
>
SYSTEM DEFAULT
```

When a conflict appears, replace the **smallest failed variable**.

Example:

`Moment valid + Action valid + Scene cannot support the action → keep Moment/Action, reroute Scene (+ Color only if Scene changes).`

Do not erase a valid Partner identity to fix a director-level combination problem.

---

# 3. RELATIONSHIP_COMBINATION_CARD

```text
RELATIONSHIP_COMBINATION_CARD

combination_id
status

partner_ref
relationship_temperature
visual_intimacy_level
wardrobe_exposure_level
body_distance_level
contact_intensity_summary
sensuality_payload
visual_treatment_profile
editorial_treatment_payload

moment_id
action_id
tension_modifier_when_used

person_a_expression_id
person_a_gaze_id
person_b_expression_id
person_b_gaze_id

scene_id
color_wardrobe_id

camera_framing_intent
body_geometry_summary
contact_geometry_summary

image_model_route
video_continuation_value

compatibility_flags
identity_risk_level
identity_risk_flags
anatomy_risk_level
anatomy_risk_flags
social_misread_flags
model_risk_flags

why_this_combination_internal
image_prompt_payload
h3_continuation_seed
fallback_combination
```

`why_this_combination_internal` is internal only and must never be copied into the visible image prompt.

`image_prompt_payload` contains only renderable production facts.

---

# 4. Compatibility Gate Order

Check in this order:

1. `MOMENT ↔ ACTION`
2. `ACTION ↔ SCENE`
3. `ACTION ↔ CURRENT BODY GEOMETRY`
4. `ACTION ↔ EXPRESSION / GAZE`
5. `SCENE ↔ COLOR / WARDROBE`
6. `VISUAL INTIMACY ↔ ACTION / WARDROBE / SCENE / IDENTITY RISK`
7. `SCENE ↔ CAMERA`
8. `ACTION ↔ CAMERA READABILITY`
9. `COMBINATION ↔ IDENTITY RISK`
10. `COMBINATION ↔ ANATOMY RISK`
11. `COMBINATION ↔ SOCIAL READ`
12. `COMBINATION ↔ TARGET MODEL`
13. `COMBINATION ↔ EDITORIAL TREATMENT`
14. `COMBINATION ↔ H3 CONTINUATION`

Only combinations that pass the gates may become production defaults.

---

# 5. Moment → Action Gate

Moment is `BEFORE → NOW → NEXT`; Action must physically express `NOW`.

Examples:

- `M02 FIRST LEAN-IN` → choose an action that can visibly reduce distance, such as A01 / A05 / A06 / A10 / A11.
- `M11 POST-CONTACT PULLBACK` → keep a plausible remaining waist / shoulder / upper-back connection; do not pair with a distant walking state.
- `M12 UNRESOLVED CLOSE` → preserve unfinished distance; do not force complete contact.
- `M14 WALKING → LOOK BACK` → use movement-capable actions such as A09 / A10 / A12 / A13.

Keep:

`MORE TENSION ≠ MORE CONTACT`.

---

# 6. Action → Scene Spatial Gate

Read `scene-tension-library.md` compatibility before selecting a space.

Hard spatial checks:

- A09 / A10 / A11 / A12 / A13 need open movement or turn space.
- A14 / A19 require an actual readable seat / bench / bed edge / booth.
- A18 requires a real wall / window edge / column / doorframe with an open exit side.
- walking actions may not be placed in cramped sofa corners / narrow bedside gaps.
- seated actions may not float without seat support.
- furniture / table / railing may not hide the contact point that makes the relationship readable.

If the user's requested Action and Scene conflict, preserve the higher-priority explicit choice when possible and reroute the smallest support variable. If both are explicit and physically incompatible, explain the conflict briefly and choose the smallest safe adaptation.

---

# 7. Action → Expression / Gaze Gate

Facial behavior must have a visible cause.

Useful mappings already supported by the source libraries:

- waist pull / approach → reaction smile or short gaze break → gaze return;
- whisper → reaction look;
- playful pull-in → surprise-softening / small laugh → reconnect;
- protective side embrace → quiet warmth / soft partner gaze;
- almost-contact / unresolved close → focused attraction / anticipation, with restrained eye behavior.

Default:

`PERSON_A EXPRESSION ≠ PERSON_B EXPRESSION`.

One adult initiates; the other visibly responds. Do not make both people perform identical smiles / gaze changes at the same instant.

---

# 8. Scene → Color Gate

Read both source files:

- `scene-tension-library.md` = where color can physically exist;
- `color-wardrobe-library.md` = how color is assigned to Person A / Person B / environment / light.

Rules:

- every major color must have a real physical source;
- preserve face / skin readability;
- `COORDINATED ≠ IDENTICAL`;
- do not dress both adults in the dominant background hue;
- if Scene changes, reroute Color only when the existing palette no longer has physical support.

---

# 9. Visual Intimacy Router

Read `sensuality-intensity-layer.md` before finalizing the combination.

Core rule:

`RELATIONSHIP TEMPERATURE ≠ VISUAL_INTIMACY_LEVEL`.

If the user explicitly selects a visual-intimacy level, preserve it unless identity / anatomy / mutual-agency constraints require the smallest safe reduction.

If missing, use the Sensuality Layer defaults; for the current fantasy AI-partner product, default to `V3 BOLD SENSUAL` rather than silently collapsing to a conservative lifestyle result.

The Router must compile sensuality into visible facts:

- wardrobe coverage / cut;
- body distance;
- contact zone;
- gaze / expression intensity;
- framing proximity.

Do not solve `不够性感 / 太保守` by changing Partner identity first.

Upgrade order:

`VISUAL_INTIMACY_LEVEL → WARDROBE EXPOSURE → BODY DISTANCE → CONTACT ZONE → GAZE → FRAMING → ACTION/SCENE only if still needed`.

Keep the output non-explicit and preserve reciprocal adult agency.

---

# 10. Editorial Treatment Router

Read `editorial-intimacy-dna.md` before finalizing the visual treatment.

If the user does not specify a visual style, the product default is:

`VT3 FRAGRANCE-CAMPAIGN TENSION + V3 BOLD SENSUAL`

unless the user explicitly asks for cozy / UGC / everyday / conservative lifestyle.

The Router should prefer:
- asymmetrical close two-shot / 3/4 framing;
- one dominant relationship gesture + one response signal;
- visible body line;
- material contrast;
- directional light with a physical source;
- narrative residue / unfinished moment;
- reciprocal emotion on both adults.

Reject the editorial default when the result collapses into:
- bright beige apartment selfie;
- cream-on-cream styling;
- both smiling at camera;
- centered stock-photo hug;
- flat front lighting;
- generic home décor carrying more visual weight than the couple.

Do not fix “不高级 / 太像普通情侣照” by changing Partner identity first.

Concept-image acceptance gate for VT3/V3 or stronger:
- visible body line beyond ordinary covered casualwear;
- close body distance;
- meaningful waist / hip / back / collar contact;
- reciprocal expression on both adults;
- asymmetric intimate framing;
- refined private scene with controlled material depth;
- directional physical light.

Require at least 5/7 before approval. Otherwise classify as `TOO CONSERVATIVE / TOO GENERIC` and reroute the smallest failed visual variable.

Correction order:
`EXPRESSION RECIPROCITY → COMPOSITION ASYMMETRY → BODY LINE / CONTACT → WARDROBE SILHOUETTE / MATERIAL → LIGHT DIRECTION → SCENE IF NEEDED`.

---

# 11. Relationship Temperature Router

Relationship temperature is a direction, not a fixed pose.

## SWEET

Rotate among directions such as:

- quiet comfort / side or shoulder closeness in home / window / garden spaces;
- reaction smile / laugh-settling in kitchen / café / home lifestyle;
- hand-hold or gentle walking intimacy outdoors.

Prefer simple contact, reciprocal warmth and low anatomy risk.

## ROMANTIC

Rotate among:

- private eye contact + face-to-face waist hold;
- forehead / temple proximity;
- seated lean-in;
- shared view → turn to partner.

Use an immediately readable couple unit and preserve continuation space.

## FLIRTY

Rotate among:

- first lean-in / unresolved close;
- playful pull-in / half-turn;
- turn-back look with maintained connection;
- waist hold + brief gaze break / reaction smile.

Flirty does not require completed contact.

## PASSIONATE

Rotate among:

- A01 + T03 Breath-Close;
- face-side touch when anatomy is stable;
- mutual attraction hold / soft almost-contact;
- controlled environment-supported close only when reciprocity and exit geometry are clear.

Reduce identity / anatomy risk before increasing contact.

## PLAYFUL

Rotate among:

- walking → look back;
- playful pull-in;
- laugh into embrace;
- café / kitchen reaction routes.

Require a visible response so the result does not read as friends.

## PROTECTIVE

Rotate among:

- protective side embrace;
- shoulder / upper-body lean;
- quiet shared-view turn;
- calm home / window / garden closeness.

Both adults must retain agency; protective must not read as bodyguard/client or parent/child.

---

# 12. Combination Diversity Guard

Maintain `RECENT_COMBINATION_HISTORY` for the same locked USER + PARTNER pair.

For a new result, prefer changing at least one core dimension:

- Moment; or
- Action; or
- Scene.

Changing only background color, wardrobe color or tiny expression details does not count as a meaningfully new combination.

Do not repeatedly route every couple to A01 + S05 merely because it is reliable.

When `Try a Different Moment` is requested, exclude the immediately previous Moment + Action pair unless the user explicitly asks to keep it.

---

# 13. Combined Identity Risk Gate

Combination identity risk is ordinal only:

- `LOW`
- `MEDIUM`
- `HIGH`

No fake percentages.

Risk can accumulate from multiple individually acceptable choices, for example:

`night low light + almost-contact + face-side hand + tight close-up + large head rotation`.

Typical risk contributors:

- S05 / S10 / S11 / S12 low / mixed night light;
- A05 / A06 / A07 / A18 close-face geometry;
- extreme close framing;
- large head rotation;
- reflective glass;
- hand occluding face landmarks;
- multiple simultaneous overlaps.

If `HIGH`, reduce **one risk variable first**:

- medium-close instead of extreme close-up;
- keep a small unresolved face gap;
- replace face-side hand with waist / upper-back contact;
- reduce head rotation;
- improve face exposure;
- remove strong reflection.

The Router only prevents risk. If an actual face swap / fusion / drift has already occurred, route to `identity-failure-recovery.md`.

---

# 14. Anatomy Risk Accumulation

Use ordinal `LOW / MEDIUM / HIGH`.

Do not stack too many of these in one still:

- complex fingers;
- linked / crossing arms;
- seated overlapping legs;
- furniture occlusion;
- face-side hand;
- near-contact faces;
- wall support;
- strong body rotation.

Default production preference:

`ONE STRONG RELATIONSHIP ACTION + 1–2 CLEAR SUPPORT SIGNALS > MULTIPLE COMPLEX ACTIONS`.

A19 remains non-default and should not be promoted simply to increase intensity.

---

# 15. Social Misread Gate

Read matching, action and expression social-read guards.

Check at least:

- `FRIENDS`
- `SIBLINGS`
- `BODYGUARD_CLIENT`
- `TRAINER_CLIENT`
- `BOSS_EMPLOYEE`
- `FASHION_CASTING_PAIR`
- `FORMAL_PORTRAIT`
- `UNRELATED_MODELS`

First correction order:

`GAZE / RESPONSE → BODY DISTANCE → ACTION CONTACT → MOMENT STATE → SUPPORTING SCENE`

Do not change the Partner face / identity to fix a social-read problem when casting is already valid.

---

# 16. Still Image Readability Gate

One still image should immediately communicate:

`WHO + RELATIONSHIP + CURRENT MOMENT`.

Minimum readable ingredients:

- both adult identities readable;
- one clear relationship Action;
- one partner-directed gaze / response signal;
- physical scene logic that supports the action.

Do not require the viewer to imagine unseen earlier video beats before the image reads as a couple.

---

# 17. Camera / Framing Intent

This Router sets only the **relationship framing intention**. Camera realism details remain in `camera-realism-layer.md`.

Default intents:

- standing closeness / waist hold → medium two-shot or medium-close 3/4;
- seated lean → diagonal medium two-shot / medium-close;
- walking / turn-back → medium / medium-wide with clear movement direction;
- near-contact → medium-close / close two-shot only while both faces remain separate;
- environmental date / terrace → medium relationship shot, with wider establish only when it does not reduce couple readability.

Avoid extreme close-up when identity + hand + face proximity risks stack.

---

# 18. Model-Aware Combination

## Banana2 Pro｜Current Final Couple Default

Prefer:

- clear identity separation;
- one readable relationship action;
- real candid-photo geometry;
- compact color / camera instructions;
- physically grounded scene.

Do not overload the prompt with director metadata.

## image 2.5

Current role remains partner exploration / canonical identity assets by default. Use as couple model only when explicitly requested or a real routing need exists.

## MiniMax H3

A good approved first frame should have **continuation potential**.

Prefer a state with a plausible next action rather than a completely exhausted endpoint.

The Router outputs only `H3_CONTINUATION_SEED`; the full video prompt remains owned by `minimax-h3-couple-video.md`.

---

# 19. H3_CONTINUATION_SEED

Every selected combination should expose:

```text
H3_CONTINUATION_SEED

current_state
next_natural_beat
second_possible_beat
payoff_direction
```

Example:

```text
current_state: M12 Unresolved Close + A01 Waist Hold + direct partner gaze
next_natural_beat: receiver gives short reaction smile / brief gaze break while maintaining waist contact
second_possible_beat: one partner shifts hand to upper back and both lean slightly closer
payoff_direction: small pullback + soft partner gaze / restrained smile, or forehead proximity if identity remains stable
```

This is not a full video prompt.

---

# 20. High-Value Core Director Routes

These are routing recipes built only from current source-library assets. They are **not a second asset SSOT**; if any source asset changes, the Router must resolve against the latest source file.

## CR01 — GOLDEN TERRACE ROMANTIC HERO｜VALIDATED CORE

- temperature: Romantic / Flirty
- Moment: `M12 UNRESOLVED CLOSE` or `M03 SOFT ALMOST-CONTACT`
- Action: `A01 FACE-TO-FACE WAIST HOLD + T03 BREATH-CLOSE`
- Expression/Gaze: `G01 DIRECT MUTUAL GAZE + E09 ANTICIPATION`; receiver may briefly use E01 restrained smile
- Scene: `S04 GOLDEN TERRACE`
- Color: `CW01 GOLDEN TERRACE`
- camera intent: medium-close 3/4 two-shot
- why physically valid: open standing geometry + readable waist contact + clear face separation + movement space
- best use: Still HERO / H3 first frame
- main risk: sunset haze + faces closing too far
- H3 next: reaction smile / gaze break → upper-back touch → slight pullback or forehead-close payoff

## CR02 — NIGHT CITY WINDOW TENSION｜VALIDATED CORE / PROJECT-PROVEN

- temperature: Romantic / Flirty / Passionate
- Moment: `M03 SOFT ALMOST-CONTACT` or `M12 UNRESOLVED CLOSE`
- Action: `A01 + T03 BREATH-CLOSE`
- Expression/Gaze: `G01 + E05 FOCUSED ATTRACTION` or `E09 ANTICIPATION`
- Scene: `S05 NIGHT CITY WINDOW`
- Color: `CW02 NIGHT CITY WINDOW`
- camera intent: medium / medium-close 3/4 with warm face light and cool city depth
- why physically valid: stable standing window geometry + strong face separation + proven H3 continuity
- best use: Still HERO / Video Start / Payoff seed
- main risk: low-light drift + face fusion at payoff
- H3 next: waist/upper-back contact change → reaction look → tighter but still separated payoff → soft release

## CR03 — SAGE HOME QUIET COMFORT｜PRODUCTION-READY / EVIDENCE-INFORMED

- temperature: Sweet / Protective / Romantic
- Moment: `M08 QUIET COMFORT`
- Action: `A04 SHOULDER / SIDE LEAN` or `A02 PROTECTIVE SIDE EMBRACE`
- Expression/Gaze: `G02 SOFT PARTNER GAZE + E03 QUIET WARMTH`
- Scene: `S06 SAGE & TERRACOTTA HOME`
- Color: `CW03 SAGE & TERRACOTTA HOME`
- camera intent: diagonal medium two-shot / medium-close
- best use: Still / gentle H3 start
- main risk: friends / siblings if gaze and waist/upper-back connection are weak
- H3 next: receiving partner looks up → reaction smile → turn inward / forehead proximity

## CR04 — CLEAN MORNING REACTION｜EVIDENCE-INFORMED

- temperature: Sweet / Playful
- Moment: `M04 REACTION SMILE` or `M05 AFTER-LAUGH RECONNECT`
- Action: `A17 LAUGH INTO EMBRACE`
- Expression/Gaze: `G07 LAUGH → RECONNECT + E02 REACTION SMILE / E07 POST-LAUGH SOFTENING`
- Scene: `S07 KITCHEN MORNING`
- Color: `CW05 CLEAN MORNING`
- camera intent: medium two-shot with one reaction close cut available later
- best use: Still candid / Video Middle seed
- main risk: generic lifestyle-ad smile or prop clutter
- H3 next: small laugh settles → direct gaze → simple side embrace / lean-in

## CR05 — GOLDEN WALK INVITATION｜EVIDENCE-INFORMED

- temperature: Playful / Flirty / Romantic
- Moment: `M14 WALKING → LOOK BACK`
- Action: `A09 HAND-HOLD WALK` or `A10 PLAYFUL PULL-IN`
- Expression/Gaze: `G04 LOOK AWAY → LOOK BACK + E04 PLAYFUL HALF-SMILE`
- Scene: `S14 GOLDEN-HOUR WALK`
- Color: `CW06 GOLDEN OUTDOOR`
- camera intent: medium / medium-wide with clear movement direction
- best use: Video Start / dynamic still
- main risk: travel/friend read if hand connection and response are weak
- H3 next: stop → pull-in → half-turn → close eye contact / embrace

## CR06 — URBAN PLAYFUL PULL｜EVIDENCE-INFORMED

- temperature: Playful / Flirty
- Moment: `M07 PLAYFUL CHALLENGE`
- Action: `A10 HAND-HOLD PULL / PLAYFUL PULL-IN`
- Expression/Gaze: `G04 + E10 SLIGHTLY FLUSTERED RESPONSE` or E04
- Scene: `S18 URBAN WALK / NEIGHBORHOOD DATE`
- Color: `CW07 URBAN CASUAL`
- camera intent: medium-wide start → medium stop point
- best use: Video Start / Middle
- main risk: friend read / limb stretch
- H3 next: receiver follows → A11 half-turn → reaction smile → waist/upper-back close

## CR07 — SOFA ROMANTIC LEAN｜EVIDENCE-INFORMED

- temperature: Romantic / Sweet / Flirty
- Moment: `M01 PRIVATE EYE CONTACT`
- Action: `A14 SOFA / SEATED LEAN-IN`
- Expression/Gaze: `G01 + E01 RESTRAINED SMILE` or E05
- Scene: `S02 SOFA CORNER`
- Color: `CW03 SAGE & TERRACOTTA HOME` when decor supports it; otherwise scene-compatible family from Color Library
- camera intent: diagonal medium two-shot / medium-close
- best use: Still / H3 Start
- main risk: interview / roommate read; hand/knee occlusion
- H3 next: whisper/reaction → closer lean → forehead/temple proximity or soft release

## CR08 — HOTEL REFINED ATTRACTION｜EVIDENCE-INFORMED / CONDITIONAL

- temperature: Romantic / Flirty / Passionate
- Moment: `M10 MUTUAL ATTRACTION HOLD`
- Action: `A07 FACE-SIDE TOUCH` only when hand geometry is stable; fallback A01
- Expression/Gaze: `G03 EYE → LIP → EYE + E09 ANTICIPATION`
- Scene: `S13 HOTEL WINDOW / HOTEL LIFESTYLE`
- Color: `CW08 REFINED HOTEL`
- camera intent: medium-close 3/4; avoid extreme close-up
- best use: Still / H3 Middle or payoff seed
- main risk: hand-face fusion + low-light / close-face identity risk
- H3 next: hand returns to shoulder/upper back → lean closer → slight pullback / soft relief

## CR09 — GARDEN PROTECTIVE CALM｜EVIDENCE-INFORMED

- temperature: Protective / Sweet
- Moment: `M09 PROTECTIVE CALM`
- Action: `A02 PROTECTIVE SIDE EMBRACE`
- Expression/Gaze: `G02 + E08 PROTECTIVE CALM`; receiver returns gaze / touch
- Scene: `S15 PARK / GARDEN`
- Color: `CW09 GARDEN / NATURE`
- camera intent: medium 3/4 two-shot
- best use: Still / gentle Video Start
- main risk: bodyguard/client if only one adult acts
- H3 next: receiver turns inward / touches forearm → private eye contact → relaxed close hold

## CR10 — CAFÉ AFTER-LAUGH｜EVIDENCE-INFORMED

- temperature: Playful / Sweet / Romantic
- Moment: `M05 AFTER-LAUGH RECONNECT`
- Action: `A17 LAUGH INTO EMBRACE` or seated A14 when space is tight
- Expression/Gaze: `G07 + E07 POST-LAUGH SOFTENING`
- Scene: `S17 OUTDOOR CAFÉ`
- Color: `CW10 PLAYFUL CAFÉ`
- camera intent: adjacent-seat medium two-shot / reaction close-up
- best use: Still / H3 Middle
- main risk: table/prop clutter + friend read
- H3 next: laughter settles → partner gaze → shoulder/upper-back contact → leave table / walking beat if desired

## CR11 — WINDOW SHARED-VIEW PROTECTIVE｜EVIDENCE-INFORMED

- temperature: Protective / Romantic / Sweet
- Moment: `M13 SHARED VIEW → TURN TO PARTNER`
- Action: `A02 PROTECTIVE SIDE EMBRACE`
- Expression/Gaze: `G05 SHARED VIEW → PARTNER + E03 QUIET WARMTH`
- Scene: `S01 WINDOW-SIDE`
- Color: `CW11 ELEVATED NEUTRAL` when the scene supports it; otherwise a compatible physical palette
- camera intent: medium two-shot with side-window depth
- best use: Video Start / Still
- main risk: backlight haze / social hug read
- H3 next: turn to partner → private eye contact → waist/upper-back contact or forehead proximity

## CR12 — PASSIONATE WINDOW HOLD｜VALIDATED CORE / HIGH-CONTROL

- temperature: Passionate / Flirty
- Moment: `M10 MUTUAL ATTRACTION HOLD` or `M12 UNRESOLVED CLOSE`
- Action: `A01 + T03 BREATH-CLOSE`
- Expression/Gaze: `G01 + E05 / E09`; G03 only as a brief modifier
- Scene: `S05 NIGHT CITY WINDOW` or `S01 WINDOW-SIDE` according to requested lighting
- Color: `CW02` for S05; scene-compatible family for S01
- camera intent: medium-close two-shot; both faces remain separately readable
- best use: HERO still / H3 payoff seed
- main risk: combined close-distance + night-light + tight framing
- H3 next: one short gaze break / reaction → upper-back contact → unresolved near-contact → slight release

---

# 21. Core Route Status Rule

Use:

- `VALIDATED CORE`
- `EVIDENCE-INFORMED`
- `CANDIDATE`
- `HIGH-RISK / CONDITIONAL`

A combination must not be promoted far above the evidence of its important components.

Existing project-proven Scene / Color / H3 evidence may support a core route without demanding a new synthetic combination benchmark.

---

# 22. User Feedback Minimal Reroute

## “动作不喜欢”

Keep USER/PARTNER identities and compatible Scene. Reroute Action + the Expression/Gaze caused by that Action.

## “场景不好看”

Keep identities + Moment + Action when physically possible. Reroute Scene + Color/Wardrobe.

## “太暧昧了 / 太大胆了”

Lower `VISUAL_INTIMACY_LEVEL` first; if the user also wants a different emotional tone, then lower `RELATIONSHIP_TEMPERATURE`. Preserve identities.

## “太保守 / 不够性感 / 尺度不够”

Keep identities and Partner. Increase `VISUAL_INTIMACY_LEVEL` first, then compile stronger wardrobe exposure + closer body distance + waist/lower-waist/upper-hip contact + stronger partner-directed gaze + slightly tighter framing. Only reroute Action / Scene if the current geometry cannot support the requested level.

## “想要高级、奢华、性感、荷尔蒙、暧昧、大尺度”

Keep USER + Partner identity. Route directly to:
`VT3 FRAGRANCE-CAMPAIGN TENSION + V3 BOLD SENSUAL`.

Compile:
`BODY LINE + FITTED/OPEN WARDROBE + CLOSE DISTANCE + MEANINGFUL CONTACT + RECIPROCAL GAZE + ASYMMETRIC FRAMING + DIRECTIONAL LIGHT`.

If user explicitly asks for the strongest non-explicit result, raise to V4 while preserving adult agency, coverage, anatomy and identity.

## “不高级 / 太普通 / 太像生活照”

Keep USER + Partner identity. Keep valid Moment / Action where possible.

Reroute first:
`VISUAL_TREATMENT_PROFILE → COMPOSITION ASYMMETRY → BODY LINE → WARDROBE MATERIAL / SILHOUETTE → LIGHT DIRECTION`.

Prefer VT2 / VT3 rather than replacing Partner or merely adding abstract words.

## “不够有感觉”

First adjust:

`MOMENT → GAZE / RESPONSE → BODY DISTANCE → ACTION TENSION LAYER`.

Do not immediately change Partner.

## “想换伴侣”

Return to `matching-engine.md`.

## “不是我了 / 伴侣变脸”

Return to `identity-failure-recovery.md`.

---

# 23. TRY A DIFFERENT MOMENT

When the user selects `Try a Different Moment`:

KEEP:

- USER identity;
- PARTNER identity;
- hard partner preferences;
- approved Partner lock.

REROUTE FIRST:

- Moment;
- Action;
- Expression / Gaze.

KEEP Scene / Color when they remain physically compatible.

Only reroute Scene when the new Action cannot occur naturally in the current space. Reroute Color only if the new Scene or wardrobe logic requires it.

Do not reopen Matching.

---

# 24. TRY A DIFFERENT VIBE｜Backend Capability

If requested:

KEEP Partner identity.

Reroute primarily:

- Relationship Temperature;
- Moment;
- Expression / Gaze;
- Action where needed;
- Color direction only when the requested vibe benefits from a different physically supported palette.

Frontend exposure is decided later.

---

# 25. Multi-Orientation Neutrality

The same router applies to:

- Woman × Man
- Man × Woman
- Woman × Woman
- Man × Man

Do not assign initiator, dominant, protective, shy or receiving roles from gender pairing.

Choose roles from:

`CURRENT GEOMETRY + MOMENT + ACTION + PERSON A/B AURA`.

---

# 26. Rule-Level Acceptance Cases

No new generation is required unless a future case cannot be resolved from routing logic.

- **A Sweet:** low-risk, non-formal, reciprocal combination available → PASS.
- **B Romantic Hero:** M03/M12 + readable romantic action + scene/color support → PASS.
- **C Flirty:** tension preserved without requiring completed contact → PASS.
- **D Playful:** movement + reciprocal reaction + romantic follow-through, not friends → PASS.
- **E Protective:** equal adult agency; no bodyguard/client read → PASS.
- **F Passionate:** intimacy increases while combined identity/anatomy risk is controlled → PASS.
- **G Man × Man:** same routing logic; no heteronormative role assignment → PASS.
- **H Woman × Woman:** same routing logic; no fixed role assignment → PASS.
- **I Try a Different Moment:** identity / Partner lock preserved; Moment/Action/Expression rerouted first → PASS.
- **J Explicit Scene + Action conflict:** preserve user intent where possible; replace smallest incompatible support variable or explain minimal adaptation → PASS.

Do not enumerate the full combinatorial space.

---

# 27. Final Runtime Rules

1. Source libraries remain SSOT for asset definitions and IDs.
2. Explicit user choice wins unless physically / socially / identity / model incompatible.
3. Preserve locked identities while rerouting director variables.
4. Use the smallest compatible set of relationship signals.
5. Avoid stacked identity + anatomy risks.
6. Prefer first frames with a clear H3 next beat.
7. Do not let one reliable recipe become the default for every user.
8. Social-read corrections should modify relationship signals before changing Partner identity.
9. Actual identity failure belongs to `identity-failure-recovery.md`, not this Router.
10. Sensuality is a separate axis from relationship temperature; compile it through visible geometry / wardrobe / gaze / framing.
11. Never brute-force all Partner × Moment × Action × Expression × Scene × Color permutations.
