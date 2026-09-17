# Standalone Prompt Routing｜独立提示词输出路由

## Purpose

Make the AI Virtual Partner Skill independently usable in a fresh session without relying on temporary chat memory, benchmark context, or unstated prior work.

The Skill must independently support:

1. final still-image prompt;
2. final MiniMax H3 video prompt;
3. full user-photo → partner → couple image → approval → 10-second video workflow;
4. minimum identity-recovery route when a person changes, fuses, swaps or drifts.

Every final prompt must be executable on its own.

---

# 1. Operating Modes

## MODE A — IMAGE PROMPT ONLY

Possible inputs:

- user photo / identity reference;
- partner gender / appearance preference;
- relationship temperature;
- optional Moment / Action / Scene / Color preference;
- target image model.

Runtime:

```text
USER INPUT
→ USER IDENTITY LOCK when a real photo exists
→ PARTNER RESOLVE / MATCHING when needed
→ PARTNER LOCK when a specific approved partner exists
→ RELATIONSHIP COMBINATION ROUTER
→ RELATIONSHIP_COMBINATION_CARD
→ MODEL ROUTE
→ MODEL ADAPTER
→ FINAL IMAGE PROMPT
```

Do not independently improvise five separate creative libraries in a fresh session. Let `relationship-combination-router.md` orchestrate their compatibility.

If there is no real user photo, do not pretend identity lock exists. Use a generic demo route or ask for the missing photo only when real-user continuity is essential.

---

## MODE B — VIDEO PROMPT ONLY

Preferred authority:

`APPROVED_COUPLE_IMAGE = VISUAL TRUTH / FIRST FRAME`

plus, when available:

`USER_REFERENCE_PACKAGE + PARTNER_REFERENCE_PACKAGE + APPROVED_RELATIONSHIP_COMBINATION_CARD`

Runtime:

```text
APPROVED COUPLE IMAGE
→ INHERIT USER + PARTNER IDENTITIES
→ READ CURRENT BODY / HAND / MOMENT / EXPRESSION / SCENE / COLOR STATE
→ READ COMBINATION CARD current state + H3_CONTINUATION_SEED when available
→ MINIMAX H3 VIDEO ROUTE
→ MODEL ADAPTER
→ FINAL 10s VIDEO PROMPT
```

The seed is planning input only. The approved couple image remains immediate first-frame visual truth.

If no approved stable first frame exists and identity continuity matters, route first to couple-image creation.

---

## MODE C — END-TO-END

```text
USER PHOTO
→ LOCK USER IDENTITY
→ RESOLVE / CONFIRM PARTNER PREFERENCES
→ PARTNER LIBRARY + MATCHING
→ LOCK APPROVED PARTNER WHEN NEEDED
→ RELATIONSHIP COMBINATION ROUTER
→ FINAL IMAGE PROMPT
→ USER APPROVAL
→ FREEZE APPROVED_COUPLE_IMAGE + APPROVED COMBINATION STATE
→ FINAL 10s MINIMAX H3 VIDEO PROMPT
```

---

# 2. Prompt Self-Containment

Never rely on:

- `same as before`;
- `continue previous route`;
- `use the benchmark result`;
- unstated chat history.

## Image prompt includes, when relevant

- visible subject assignments;
- user identity preservation;
- partner identity / appearance route;
- current Moment;
- Action / hand / contact geometry;
- Expression / Gaze;
- Scene;
- Wardrobe / physical color sources;
- camera / framing when material;
- realism controls;
- model compensation.

## Video prompt includes, when relevant

- first-frame authority;
- USER / PARTNER identity isolation;
- duration;
- Moment progression;
- Action progression;
- Expression / Gaze change caused by each beat;
- shot size / camera position / camera move per explicit shot;
- cut logic;
- body-contact continuity;
- scene / wardrobe / color continuity;
- ending hold;
- model controls.

---

# 3. Image Prompt Writer

Goal:

`STRUCTURED COUPLE DECISION → FINAL STILL-IMAGE PROMPT`

Compile from:

```text
USER_IDENTITY_CARD
+
PARTNER_IDENTITY / PARTNER_APPEARANCE_CARD
+
RELATIONSHIP_COMBINATION_CARD
+
CAMERA REALISM
+
IMAGE MODEL ADAPTER
```

The Router resolves:

`MOMENT + ACTION + EXPRESSION/GAZE + SCENE + COLOR/WARDROBE + CAMERA INTENT`.

Source libraries remain their own SSOT; the Router only chooses a compatible set.

Read:

- `references/relationship-combination-router.md`
- `references/couple-moment-dna.md`
- source Moment / Action / Expression / Scene / Color files only when resolving compatibility or explicit overrides;
- `references/camera-realism-layer.md`;
- `references/model-routing-rules.md`;
- `references/model-adaptation.md`.

Current defaults:

- final user-facing couple image → `Banana2 Pro`;
- partner exploration / canonical identity → `image 2.5`.

Never copy `why_this_combination_internal` or internal matching rationale into the visible prompt.

Apply `VISIBLE SUBJECT FILTER`.

---

# 4. Video Prompt Writer

Goal:

`APPROVED COUPLE IMAGE → TIME-BASED RELATIONSHIP INTERACTION`

Compile from:

```text
APPROVED_COUPLE_IMAGE
+
USER_REFERENCE_PACKAGE
+
PARTNER_REFERENCE_PACKAGE
+
APPROVED_RELATIONSHIP_COMBINATION_CARD when available
+
CURRENT BODY / HAND GEOMETRY
+
CURRENT EXPRESSION / GAZE / SCENE / COLOR STATE
+
H3_CONTINUATION_SEED when available
+
MINIMAX H3 10s GRAMMAR
+
VIDEO MODEL ADAPTER
```

Current default route: `MiniMax H3`.

Default grammar:

```text
BEAT 1 — INITIATE
→ CUT / FRAMING CHANGE
→ BEAT 2 — ESCALATE / REACT
→ CUT / FRAMING CHANGE
→ BEAT 3 — PAYOFF / HOLD / CLOSE
```

Each Beat should compile:

`MOMENT STATE + ACTION CHANGE + GAZE / EXPRESSION CHANGE`.

Do not stretch one micro-action or fixed facial expression across 10 seconds.

Color is continuity data in video, not a new palette-design task.

---

# 5. Library Invocation Logic

## Image path

```text
portrait-identity-lock
→ partner-archetype-library
→ matching-engine
→ partner-identity-lock when needed
→ relationship-combination-router
   ↳ consult moment / action / expression-gaze / scene / color libraries as asset SSOT
→ camera-realism-layer
→ model-routing-rules
→ model-adaptation
→ FINAL IMAGE PROMPT
```

## Video path

```text
APPROVED_COUPLE_IMAGE
→ inherit USER / PARTNER identity locks
→ inherit APPROVED RELATIONSHIP_COMBINATION_CARD current state
→ minimax-h3-couple-video
→ model-adaptation
→ FINAL VIDEO PROMPT
```

## Identity-recovery path

Use only when the person themselves changed / fused / swapped / drifted:

```text
USER FEEDBACK OR QC FAILURE
→ identity authority check
→ identity-failure-recovery
→ invalidate bad reference when needed
→ minimum recovery
→ regenerate failed state
→ identity QC
```

Do not load benchmark / historical modules unless a real current failure requires them.

---

# 6. Missing Information

## Real user photo provided

Run identity lock first. Do not beautify before identity is stable.

## No real user photo

Do not fabricate a locked identity.

## Partner preference missing

Use Matching Engine defaults. Explicit user preference always wins.

## Relationship creative inputs missing

Do not select Moment / Action / Expression / Scene / Color independently in ad hoc order.

Use:

`RELATIONSHIP TEMPERATURE + CURRENT GEOMETRY + USER EXPLICIT CHOICES → RELATIONSHIP COMBINATION ROUTER`.

The Router checks source-library compatibility and recent-combination diversity.

## Video requested with no approved image

If identity continuity matters:

1. create / output the couple-image prompt;
2. obtain approved first frame;
3. compile video from that image.

---

# 7. Output Contract

## Image prompt

```text
MODE
MODEL
SELECTED PARTNER + RELATIONSHIP COMBINATION SUMMARY
FINAL IMAGE PROMPT
```

Keep reasoning short unless requested.

## Video prompt

```text
MODE
MODEL
FIRST-FRAME / VISUAL-TRUTH ASSIGNMENT
SHORT 3-BEAT RELATIONSHIP PROGRESSION
FINAL VIDEO PROMPT
```

## Full workflow

```text
1. USER IDENTITY RESULT
2. PARTNER ROUTE
3. RELATIONSHIP COMBINATION CARD / USER-FACING SUMMARY
4. FINAL IMAGE PROMPT
5. USER APPROVAL GATE
6. FINAL VIDEO PROMPT
```

Do not output video before approval unless explicitly requested as preview.

## Identity failure

```text
1. DETECT WHO DRIFTED
2. CLASSIFY MINIMUM FAILURE
3. RETURN TO CORRECT IDENTITY AUTHORITY
4. DISCARD BAD REFERENCE IF NEEDED
5. KEEP NON-FAILED DIRECTOR ASSETS
6. REGENERATE FAILED STATE
7. QC
```

---

# 8. Reference Assignment

Use conceptually:

```text
PERSON_A = USER_REFERENCE
PERSON_B = PARTNER_REFERENCE
FIRST_FRAME = APPROVED_COUPLE_IMAGE
```

References outrank text for identity.

For video composition / clothing / scene, approved couple image is immediate first-frame truth while original USER / PARTNER references remain identity authority.

For exact recovery authority, read `references/identity-failure-recovery.md`.

---

# 9. User Feedback Routing

## Try Another Match

Return to Matching Engine. Keep user identity and hard preferences. Do not reroute director assets until a new Partner is selected.

## Try a Different Moment

Keep:

- USER identity;
- PARTNER identity / lock;
- hard partner preferences.

Reroute first:

- Moment;
- Action;
- Expression / Gaze.

Keep Scene / Color when compatible. Change Scene only if the new Action cannot physically work there; then reroute Color only as needed.

Do not reopen Matching.

## Try a Different Vibe

Keep Partner. Reroute Relationship Temperature + Moment + Expression/Gaze + Action as needed; change Color only when physically supported and useful.

## “动作不喜欢”

Keep identities / compatible Scene; reroute Action + caused Expression/Gaze.

## “场景不好看”

Keep identities + compatible Moment/Action; reroute Scene + Color.

## “不够有感觉”

Adjust first:

`Moment → Gaze / Response → Body Distance → Action Tension Layer`.

Do not immediately replace Partner.

## “不是我了 / 伴侣变脸 / 第二镜换人”

Route to Identity Failure Recovery.

---

# 10. Prohibited Behaviors

The standalone Skill must not:

- depend on temporary benchmark memory;
- output shorthand instead of a self-contained prompt;
- collapse image and video into one universal prompt;
- reuse one model prompt mechanically across models;
- skip identity lock for a real uploaded user when continuity matters;
- invent unseen body identity facts;
- expose internal matching or combination rationale as visible subjects;
- rebuild two people from text after reliable references exist;
- generate video with unclear first-frame authority;
- let color instructions overpower people / action / scene;
- use fixed gender roles;
- make both people use identical smile / gaze behavior by default;
- repair drift from a drifted output;
- reopen Matching because an approved partner drifted downstream;
- treat hand / scene / palette / attractiveness problems as identity failure;
- brute-force Partner × Moment × Action × Expression × Scene × Color permutations;
- allow fresh-session prompt writing to bypass `relationship-combination-router.md` when the creative combination is not explicitly fixed by the user.

---

# 11. Default Production Route

```text
PARTNER EXPLORATION / CANONICAL IDENTITY
→ image 2.5

FINAL USER-FACING COUPLE IMAGE
→ Banana2 Pro

USER-APPROVED COUPLE IMAGE → 10s VIDEO
→ MiniMax H3
```

Explicit compatible user model choice may override defaults.

---

# 12. Fresh-Session Requirement

`CURRENT USER INPUT + CURRENT SKILL KNOWLEDGE BASE = COMPLETE PROMPT OUTPUT`

The user does not need to know internal asset IDs.

A fresh session must be able to resolve Partner, call the Combination Router, generate a complete still prompt, preserve the approved state, and compile the video without knowing how the libraries were originally benchmarked.

---

# 13. Fresh-Session Identity Failure Router

If the user says:

- `不是我了 / 这不是我`;
- `脸变了`;
- `怎么年轻了 / 变老了`;
- `这个伴侣不是刚才那个`;
- `两个人脸混了 / 换脸了`;
- `第二个镜头换人了`;
- `越改越不像`;

route first to `references/identity-failure-recovery.md`.

Distinguish:

`IDENTITY FAILURE`

from:

`ANATOMY / ACTION / SCENE / COLOR / MATCHING / MODEL-PRESENTATION FAILURE`.

Recover from the correct authority source and preserve all unaffected approved variables.