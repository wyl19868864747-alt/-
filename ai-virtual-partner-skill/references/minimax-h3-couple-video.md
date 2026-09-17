# MiniMax H3 Couple Video｜10秒暧昧互动视频资产

## Purpose

Turn the user-approved couple image into a short, visually evolving 10-second adult romantic interaction while preserving both identities.

This file is the current production video route for the AI Virtual Partner Skill.

Current status: `VALIDATED — FIRST PRODUCTION ROUTE`

Validation scope:

- one real 10-second MiniMax H3 generation using an approved Man × Man Night City Window couple image;
- identity, wardrobe and scene remained operationally stable across the clip;
- the clip executed visible action progression and shot / framing changes;
- the result was judged usable for production by the user;
- therefore the grammar is promoted for current production use without expanding into a new large benchmark campaign.

---

## Input Authority

Use:

`APPROVED_COUPLE_IMAGE = FIRST FRAME / VISUAL TRUTH`

plus, when available:

`USER_REFERENCE_PACKAGE`
+
`PARTNER_REFERENCE_PACKAGE`
+
`APPROVED_RELATIONSHIP_COMBINATION_CARD`

Do not rebuild either identity from text.

If a `RELATIONSHIP_COMBINATION_CARD` exists, read only its approved current-state fields and `h3_continuation_seed` as planning input. The card does not override the visible first frame.

Priority:

`APPROVED_COUPLE_IMAGE for composition / body state / wardrobe / scene`

`USER + PARTNER REFERENCE PACKAGES for identity`

`H3_CONTINUATION_SEED for next-beat planning`

Read when compiling relationship behavior:

- `references/relationship-combination-router.md`
- `references/moment-type-library.md`
- `references/relation-action-library.md`
- `references/expression-gaze-library.md`

Read when a video identity failure is detected:

- `references/identity-failure-recovery.md`

---

## Combination Card → H3 Interface

When available, map:

```text
RELATIONSHIP_COMBINATION_CARD
.current state
.body_geometry_summary
.contact_geometry_summary
.camera_framing_intent
.h3_continuation_seed.current_state
.h3_continuation_seed.next_natural_beat
.h3_continuation_seed.second_possible_beat
.h3_continuation_seed.payoff_direction
```

into the validated 3-beat grammar.

Do not mechanically copy all card metadata into the prompt. Use only visible, executable facts.

If the approved image visibly differs from the pre-image card, the approved image wins for actual first-frame geometry.

---

## Validated 10s Grammar

Avoid a ten-second single action.

Use:

`BEAT 1 — INITIATE`
→ `CUT / FRAMING CHANGE`
→ `BEAT 2 — ESCALATE / REACT`
→ `CUT / FRAMING CHANGE`
→ `BEAT 3 — PAYOFF / HOLD / CLOSE`

Current production target:

- 3 distinct relationship beats;
- approximately 2 purposeful cuts / shot changes;
- changing body relationship, not only changing camera;
- reciprocal reaction from both partners;
- final 0.8–1.2s readable closing hold.

The first H3 production run showed that this structure can produce a more engaging 10-second interaction than the earlier single-shot Seedance slow-approach route.

Identity recovery must not replace this grammar. It only adjusts identity inheritance, face separation, rotation stress and where cuts are placed around risky transformations.

---

## Moment + Expression / Gaze Compile Rule

Each beat should define a relationship-state change, not only a body move.

Compile from:

`MOMENT STATE + ACTION CHANGE + GAZE / EXPRESSION CHANGE`

For every explicit shot, state only the minimum visible facial logic needed:

`CURRENT GAZE + CURRENT EXPRESSION + TRIGGER + CHANGE`

Example:

`direct mutual gaze + restrained smile → waist pull triggers a brief look-away / reaction smile → gaze returns as both lean closer.`

Useful production chain:

`PRIVATE EYE CONTACT`
→ action initiation
→ `REACTION SMILE / LOOK BACK`
→ renewed approach
→ `UNRESOLVED CLOSE / SOFT ALMOST-CONTACT`
→ slight release
→ `POST-CONTACT PULLBACK / SOFT PARTNER GAZE`

Do not keep one fixed “sexy stare” for the whole clip. Eye / expression change should follow a visible cause.

---

## Recommended Interaction Palette

Select only 2–3 actions per 10-second clip.

### Initiation actions

- waist pull closer
- side step / half turn toward partner
- hand from chest to upper arm / shoulder
- direct gaze → small reaction smile
- protective side wrap

### Escalation actions

- closer waist / back contact
- playful turn into side embrace
- hand moves to upper back / shoulder blade
- one partner gently tucks hair / touches side of face when anatomically stable
- cheek / temple / side-neck proximity within platform limits
- mutual lean-in with reciprocal response

### Payoff actions

- unresolved pre-kiss hold
- forehead / temple closeness
- brief affectionate contact if platform / model permits
- pull apart slightly and smile at each other
- close embrace + eye contact

Do not stack every action into one clip.

---

## Shot Design

Every explicit shot should state the visible relationship purpose and how the camera follows it.

### Shot 1｜0–3s｜Medium Two-Shot

- show both identities clearly;
- establish the approved first-frame relationship;
- one partner initiates a visible action;
- establish a readable gaze / expression state;
- subtle lateral slide / short push-in may follow the movement.

### Shot 2｜3–6.5s｜Side Medium-Close / Reaction

- cut on movement;
- show hand contact / gaze / reaction from a new angle;
- execute one stronger intimate action;
- show one visible reciprocal expression / gaze change caused by that action;
- camera follows the face / upper-body relation rather than orbiting randomly.

### Shot 3｜6.5–10s｜Tighter Two-Shot / Close Hold

- cut to a tighter or 3/4 angle;
- execute payoff / near-contact / affectionate beat;
- preserve both identities at close distance;
- expression settles rather than escalating endlessly;
- hold the final relationship state for about 1 second before ending.

The camera change must support a relationship beat. Do not add cuts only for visual decoration.

---

## Identity + Anatomy Guards

Throughout all shots:

- USER identity unchanged;
- PARTNER identity unchanged;
- stable hairline / age / face geometry;
- hands stay attached to correct arms;
- contact points remain physically plausible;
- no hand penetrating waist / chest / neck;
- no face fusion at close distance;
- no sudden wardrobe / scene / body-shape changes.

Use cuts to reduce transition stress when one continuous transformation would risk anatomy failure.

For every new shot after a cut, conceptually rebind:

`PERSON_A = USER_REFERENCE_PACKAGE`

`PERSON_B = PARTNER_REFERENCE_PACKAGE`

while preserving:

`APPROVED_COUPLE_IMAGE = FIRST-FRAME VISUAL TRUTH`.

---

## Video Identity Failure Recovery

If a generated clip shows identity drift, face fusion, USER / PARTNER switch after a cut, sudden age change, hairline change or body-build change, route to `references/identity-failure-recovery.md`.

Recovery priority:

1. keep the approved first frame;
2. keep original USER / PARTNER identity packages as authority;
3. reject drifted frames as identity references;
4. shorten long continuous morphs;
5. cut before the highest-risk transformation;
6. reduce extreme head rotation;
7. preserve visible separation between faces;
8. shorten high-risk face-to-face convergence;
9. explicitly rebind A/B identity references after each cut.

For close proximity:

`IDENTITY STABILITY > CONTACT COMPLETION`

A small unresolved face gap is preferred over a fused payoff.

Do not reopen Matching because a video frame drifted. Do not regenerate an approved partner from the abstract Archetype.

---

## Chemistry Rule

Build chemistry from:

`INITIATION + RECIPROCAL REACTION + TOUCH CHANGE + GAZE + DISTANCE CHANGE + PAUSE`

Both people should actively respond. Avoid holding one almost-kiss pose for most of the clip.

---

## Color / Scene Continuity

Preserve the approved first frame's scene / color identity unless the product explicitly requests a second location.

Use physically grounded wardrobe / sky / city / plant / wood / practical-light colors. Avoid one grey / black / white palette across every couple.

The validated H3 run preserved the Night City Window warm-amber / cool-blue relationship well enough for production use.

---

## Current Production Default

Compile from the approved image rather than a fixed gender-specific script.

Default pattern:

`0–3s visible initiation + readable starting gaze`
→ cut / angle change
→ `3–6.5s reciprocal reaction + stronger body-contact change + expression / gaze change`
→ cut / tighter framing
→ `6.5–9s near-contact / affectionate payoff within platform allowance`
→ `9–10s slight release + soft partner gaze / restrained smile / stable close`

Adapt exact action, Moment, gaze, expression and payoff to approved image, orientation, scene, hand availability and body geometry.

Do not reopen broad H3 benchmarking unless a real production failure exposes a routing decision.