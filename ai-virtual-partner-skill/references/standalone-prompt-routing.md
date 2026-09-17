# Standalone Prompt Routing｜独立提示词输出路由

## Purpose

Make the AI Virtual Partner Skill independently usable in a fresh session without relying on temporary chat memory, this week's benchmark context, or unstated prior work.

The Skill must be able to independently produce:

1. a final image-generation prompt;
2. a final video-generation prompt;
3. the full user-photo → partner → couple image → approved first frame → 10-second video workflow.

Every final prompt must be executable on its own.

---

# 1. Operating Modes

## MODE A — IMAGE PROMPT ONLY

Use when the user asks only for a still-image prompt.

Possible inputs:

- user photo / user identity reference;
- partner gender / orientation preference;
- partner appearance preference;
- relationship temperature;
- action preference;
- scene preference;
- target image model.

Runtime:

```text
USER INPUT
→ USER IDENTITY LOCK when a real user photo exists
→ PARTNER RESOLVE / MATCHING when a partner is needed
→ MOMENT + ACTION + SCENE + COLOR + EXPRESSION ROUTE
→ MODEL ROUTE
→ MODEL ADAPTER
→ FINAL IMAGE PROMPT
```

Do not require video planning in image-only mode.

If the user does not provide a real photo, do not pretend identity lock exists. Either generate a generic demo route or explicitly state that the prompt uses a generic subject instead of a locked real identity.

---

## MODE B — VIDEO PROMPT ONLY

Use when the user asks only for a video prompt.

Preferred input authority:

`APPROVED_COUPLE_IMAGE = VISUAL TRUTH / FIRST FRAME`

plus, when available:

`USER_REFERENCE_PACKAGE + PARTNER_REFERENCE_PACKAGE`

Runtime:

```text
APPROVED COUPLE IMAGE
→ INHERIT USER + PARTNER IDENTITIES
→ READ CURRENT RELATIONSHIP STATE / HAND POSITIONS / BODY GEOMETRY
→ MINIMAX H3 VIDEO ROUTE
→ MODEL ADAPTER
→ FINAL 10s VIDEO PROMPT
```

If no approved image / stable first frame exists and identity continuity matters, do not force a weak video prompt. Route first to image-prompt / first-frame creation.

---

## MODE C — END-TO-END

Use when the user wants the full production flow.

```text
USER PHOTO
→ LOCK USER IDENTITY
→ RESOLVE OR CONFIRM PARTNER PREFERENCES
→ PARTNER LIBRARY + MATCHING
→ LOCK PARTNER IDENTITY WHEN NEEDED
→ ROUTE MOMENT / ACTION / SCENE / COLOR / EXPRESSION
→ FINAL IMAGE PROMPT
→ USER APPROVAL
→ FREEZE APPROVED_COUPLE_IMAGE
→ FINAL 10s MINIMAX H3 VIDEO PROMPT
```

---

# 2. Prompt Self-Containment Rule

Every final image or video prompt must be self-contained.

Do not rely on phrases such as:

- `same as before`;
- `continue the previous route`;
- `use the benchmark result`;
- `same character as last time` without an explicit reference assignment;
- unstated temporary chat context.

The final prompt must restate the production facts needed by the target model.

## Image prompt must include, when relevant

- visible subject assignments;
- user identity preservation instructions;
- partner identity / partner appearance route;
- moment / relationship state;
- exact body action / hand placement;
- scene;
- wardrobe / physical color sources;
- expression / gaze;
- camera / framing when it materially affects the result;
- realism controls;
- model-specific compensation.

## Video prompt must include, when relevant

- visual-truth / first-frame authority;
- user / partner identity isolation;
- duration;
- relationship Beat progression;
- body-action progression;
- shot size / camera position / camera move for every explicit shot;
- cut logic;
- hand / body-contact continuity;
- scene / wardrobe / color continuity;
- ending beat / closing hold;
- model-specific controls.

---

# 3. Dual Prompt Writer

The Skill contains two independent prompt writers.

## IMAGE PROMPT WRITER

Goal:

`STRUCTURED COUPLE DECISION → FINAL STILL-IMAGE PROMPT`

Compile from:

```text
USER_IDENTITY_CARD
+
PARTNER_IDENTITY / PARTNER_APPEARANCE_CARD
+
MOMENT_TYPE
+
RELATION_ACTION
+
SCENE
+
COLOR / WARDROBE
+
EXPRESSION / GAZE
+
CAMERA REALISM
+
IMAGE MODEL ADAPTER
```

Current default final-couple image route:

`Banana2 Pro`

Current partner exploration / canonical identity route:

`image 2.5`

The image prompt writer must not include internal matching rationale that should not be visible in the image.

Apply the `VISIBLE SUBJECT FILTER` before the final prompt.

---

## VIDEO PROMPT WRITER

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
CURRENT BODY / HAND GEOMETRY
+
RELATIONSHIP TEMPERATURE
+
MINIMAX H3 10s GRAMMAR
+
VIDEO MODEL ADAPTER
```

Current default production video route:

`MiniMax H3`

Default 10-second structure:

```text
BEAT 1 — INITIATE
→ CUT / FRAMING CHANGE
→ BEAT 2 — ESCALATE / REACT
→ CUT / FRAMING CHANGE
→ BEAT 3 — PAYOFF / HOLD / CLOSE
```

Do not stretch one micro-action across the full 10 seconds unless a specific concept genuinely requires a one-shot hold.

---

# 4. Library Invocation Logic

The Skill is an orchestrator. It should retrieve only the modules needed for the current request.

## Image path

```text
portrait-identity-lock
→ partner-archetype-library
→ matching-engine
→ partner-identity-lock when needed
→ couple-moment-dna
→ moment-type-library
→ relation-action-library
→ scene-tension-library
→ camera-realism-layer
→ model-routing-rules
→ model-adaptation
→ FINAL IMAGE PROMPT
```

## Video path

```text
APPROVED_COUPLE_IMAGE
→ inherit user / partner identity locks
→ minimax-h3-couple-video
→ model-adaptation
→ FINAL VIDEO PROMPT
```

Do not load unrelated benchmark or historical modules unless they are needed to solve a current failure.

---

# 5. Missing-Information Handling

The Skill must remain operational when information is incomplete.

## Real user photo provided

Run identity lock first.

Do not beautify before identity is stabilized.

## No real user photo

Do not fabricate a locked identity.

Use a generic demo subject or ask for the missing photo if real-user continuity is essential.

## Partner preference missing

Use the matching engine's production defaults to propose a suitable adult partner candidate.

Explicit user preference always overrides the default.

## Action / scene missing

Select from validated / production-ready libraries based on the requested relationship temperature.

Do not default every user to the same action or neutral room.

## Video requested but no approved image exists

If identity continuity matters:

1. output / generate the couple-image prompt first;
2. obtain the approved first frame;
3. then compile the video prompt.

---

# 6. Output Contract

## When user asks for an image prompt

Default output:

```text
MODE
MODEL
SELECTED PARTNER / MOMENT / ACTION / SCENE SUMMARY
FINAL IMAGE PROMPT
```

Keep the rationale short unless the user asks for analysis.

The final prompt should be directly copyable.

## When user asks for a video prompt

Default output:

```text
MODE
MODEL
FIRST-FRAME / VISUAL-TRUTH ASSIGNMENT
SHORT BEAT STRUCTURE
FINAL VIDEO PROMPT
```

The final prompt should be directly copyable.

## When user asks for the full workflow

Output / execute in this order:

```text
1. USER IDENTITY RESULT
2. PARTNER ROUTE
3. MOMENT / ACTION / SCENE DECISION
4. FINAL IMAGE PROMPT
5. USER APPROVAL GATE
6. FINAL VIDEO PROMPT
```

Do not output the video prompt before the approval gate unless the user explicitly asks to preview it.

---

# 7. Reference Assignment Rule

When actual image references are available, assign them explicitly.

Use conceptually:

```text
PERSON_A = USER_REFERENCE
PERSON_B = PARTNER_REFERENCE
FIRST_FRAME = APPROVED_COUPLE_IMAGE
```

Text descriptions support the references; they do not replace them.

Reference authority remains:

`ORIGINAL REAL IMAGE > IDENTITY CARD > APPROVED REFERENCE PACKAGE > APPROVED COUPLE IMAGE > TEXT DESCRIPTION`

except that for video composition / clothing / scene state, the approved couple image is the immediate visual truth for the first frame while original references remain the identity authority.

---

# 8. Prohibited Behaviors

The standalone Skill must not:

- depend on temporary benchmark memory in order to function;
- output `same as previous` instead of a self-contained prompt;
- collapse image and video generation into one vague universal prompt;
- mechanically reuse one prompt across different models;
- skip identity lock when a real user photo is provided and identity continuity matters;
- invent unseen body identity details as hard facts;
- expose internal matching rationale as visible subjects;
- rebuild two people from text after reliable references exist;
- generate a video prompt with unclear first-frame authority when identity continuity is critical.

---

# 9. Default Production Route

When the user gives no special model preference, use the current production routing:

```text
PARTNER EXPLORATION / CANONICAL IDENTITY
→ image 2.5

FINAL USER-FACING COUPLE IMAGE
→ Banana2 Pro

USER-APPROVED COUPLE IMAGE → 10s VIDEO
→ MiniMax H3
```

Always allow explicit user model choice to override this routing when compatible with the task.

---

# 10. Fresh-Session Requirement

A fresh-session invocation of this Skill must be sufficient to perform the workflow.

The Skill may use its own files and the user's current inputs, but must not require knowledge of how the libraries were created, which tests were run this week, or what temporary discussion produced the rules.

Runtime principle:

`CURRENT USER INPUT + CURRENT SKILL KNOWLEDGE BASE = COMPLETE PROMPT OUTPUT`
