# Standalone Prompt Routing｜独立提示词输出路由

## Purpose

Make the AI Virtual Partner Skill independently usable in a fresh session without relying on temporary chat memory, benchmark context, or unstated prior work.

Runtime principle:

`CURRENT USER INPUT + CURRENT SKILL KNOWLEDGE BASE = COMPLETE PROMPT OUTPUT`

The Skill must independently support:

1. `MODE A — IMAGE PROMPT ONLY`
2. `MODE B — VIDEO PROMPT ONLY`
3. `MODE C — END-TO-END`
4. `IDENTITY FAILURE RECOVERY`

Every final prompt must be self-contained, model-specific, directly copyable, and compiled only from current trusted inputs / references / library state.

CURRENT PRODUCT DEFAULT:
`VT3 FRAGRANCE-CAMPAIGN TENSION + V3 BOLD SENSUAL`
unless the user explicitly chooses a lower-intensity / cozy / UGC / conservative route.

All generated or transformed partners are adults.

---

# 1. Direct Prompt Request Rule

If the user asks for a prompt rather than media generation, output the final copyable prompt directly after the required internal routing.

The user does not need to know:

- internal library IDs;
- Match Mode;
- benchmark status;
- risk labels;
- why a combination was selected.

Internal structure may be detailed. User-facing prompt output should remain compact and executable.

---

# 2. MODE A — IMAGE PROMPT ONLY

Use when the user asks only for a still-image prompt.

Possible current inputs:

- user photo / identity reference;
- partner gender / appearance preference;
- relationship temperature;
- visual intimacy level / desired boldness;
- visual treatment preference when supplied; otherwise use the product default from `editorial-intimacy-dna.md`;
- optional Moment / Action / Scene / Color preference;
- target image model.

Runtime:

```text
USER INPUT
→ USER IDENTITY LOCK when a real user photo exists
→ USER_PREFERENCE_CARD
→ PARTNER ARCHETYPE / MATCHING when needed
→ PARTNER CANDIDATE ROUTE
→ APPROVED PARTNER LOCK when a specific partner has already been approved
→ RELATIONSHIP COMBINATION ROUTER
→ RELATIONSHIP_COMBINATION_CARD
→ MODEL ROUTE
→ IMAGE PROMPT COMPILE
→ FINAL COPYABLE IMAGE PROMPT
```

Rules:

- If a real user photo exists, identity lock comes first.
- If no real user photo exists, never pretend a locked real identity exists.
- The user does not need to manually select Action / Scene / internal asset IDs.
- If a partner candidate is shown as a separate product step, stop at `APPROVE / TRY ANOTHER` before partner lock.
- If the product mode auto-continues directly to a couple image, the chosen concrete partner candidate must still be internally frozen as the current Partner identity source before compiling the couple prompt.
- Do not independently improvise Moment / Action / Expression / Scene / Color in a fresh session; let `relationship-combination-router.md` resolve compatibility.

---

# 3. MODE B — VIDEO PROMPT ONLY

Use when the user asks for a 10-second couple-video prompt.

Preferred authority:

`APPROVED_COUPLE_IMAGE = FIRST-FRAME VISUAL TRUTH`

plus, when available:

`USER_REFERENCE_PACKAGE + PARTNER_REFERENCE_PACKAGE + APPROVED_RELATIONSHIP_COMBINATION_CARD`

Runtime:

```text
APPROVED COUPLE IMAGE
→ BIND PERSON_A / PERSON_B IDENTITIES
→ READ CURRENT BODY / HAND / CONTACT GEOMETRY
→ READ CURRENT MOMENT / EXPRESSION / SCENE / COLOR STATE
→ READ H3_CONTINUATION_SEED when available
→ MINIMAX H3 ROUTE
→ VIDEO PROMPT COMPILE
→ FINAL COPYABLE 10s VIDEO PROMPT
```

Authority split:

```text
USER / PARTNER REFERENCE PACKAGES = IDENTITY AUTHORITY
APPROVED_COUPLE_IMAGE = FIRST-FRAME COMPOSITION / BODY / WARDROBE / SCENE TRUTH
H3_CONTINUATION_SEED = NEXT-BEAT PLANNING INPUT
```

The approved first frame may not redefine the user's or partner's higher-authority facial identity.

If no approved / stable first frame exists and identity continuity matters, route first to couple-image / first-frame creation. Do not pretend a high-consistency video route already exists.

---

# 4. MODE C — END-TO-END

Fresh-session production flow:

```text
USER PHOTO
→ USER IDENTITY LOCK
→ CHOICE-BASED PARTNER PREFERENCES
→ MATCHING ENGINE
→ PARTNER CANDIDATE
→ USER APPROVES / TRY ANOTHER
→ PARTNER IDENTITY LOCK
→ RELATIONSHIP COMBINATION ROUTER
→ FINAL COUPLE IMAGE PROMPT / IMAGE
→ USER REVIEW
→ APPROVED_COUPLE_IMAGE
→ FINAL MINIMAX H3 VIDEO PROMPT / VIDEO
```

## Partner Candidate Approval Gate

Normal visible product flow:

```text
PARTNER CANDIDATE
→ USER APPROVES / TRY ANOTHER
→ PARTNER IDENTITY LOCK
→ COUPLE GENERATION
```

Do not jump from an unapproved abstract partner route straight into downstream identity-critical video.

If a product mode intentionally skips a visible partner-selection page, the system must still mark one concrete generated candidate as the current Partner identity source before couple generation.

## Couple Image Approval Gate

Normal route:

```text
COUPLE IMAGE
→ USER APPROVAL
→ APPROVED_COUPLE_IMAGE
→ VIDEO PROMPT
```

Do not treat an unapproved image prompt / unapproved generated image as frozen video visual truth.

Exception: if the user explicitly asks to preview the video prompt before approval, output a preview and state internally that the first frame is not yet frozen.

---

# 5. IMAGE_PROMPT_COMPILE_PACKET

Do not dump complete internal cards into the image model.

Build an internal compile packet:

```text
IMAGE_PROMPT_COMPILE_PACKET

PERSON_A_REFERENCE_ASSIGNMENT
PERSON_B_REFERENCE_ASSIGNMENT

USER_IDENTITY_LOCK_PAYLOAD
PARTNER_IDENTITY_OR_APPEARANCE_PAYLOAD

RELATIONSHIP_COMBINATION_VISIBLE_FIELDS
- moment state
- action / body geometry
- hand / contact geometry
- expression / gaze
- scene
- wardrobe / physical color sources
- visual-intimacy payload: wardrobe exposure / body distance / contact zone / framing intensity
- editorial treatment payload / composition intent
- concept-image DNA acceptance: body line / close distance / meaningful contact / reciprocal expression / asymmetric framing / refined private scene / directional light
- camera framing intent

MODEL_ROUTE
MODEL_ADAPTER_MINIMUM
CAMERA_REALISM_MINIMUM
```

Then compile:

```text
INTERNAL STRUCTURED STATE
→ VISIBLE SUBJECT FILTER
→ MINIMUM USEFUL FIELD SELECTION
→ INFORMATION PRIORITY
→ MERGE DUPLICATE CONTROLS
→ REMOVE INTERNAL LABELS
→ MODEL-SPECIFIC FINAL PROMPT
```

`why_this_combination_internal`, `internal_selection_reason`, Match Mode, fit labels and risk labels never enter the visible prompt.

---

# 6. Image Prompt Information Priority

Use this order:

```text
1. WHO THE PEOPLE ARE
2. IDENTITY PRESERVATION / REFERENCE ASSIGNMENT
3. WHAT THEY ARE DOING
4. BODY / HAND / CONTACT GEOMETRY
5. CURRENT MOMENT
6. EXPRESSION / GAZE
7. SCENE
8. VISUAL INTIMACY / WARDROBE EXPOSURE / CONTACT INTENSITY
9. WARDROBE / PHYSICAL COLOR SOURCES
10. EDITORIAL TREATMENT: ASYMMETRY / BODY LINE / MATERIAL / LIGHT DIRECTION
11. CAMERA REALISM
12. MODEL COMPENSATION
```

Global rule:

`PEOPLE / ACTION / SCENE > COLOR > LIGHTING DECORATION`

Do not let camera, color or lighting language become longer or more important than the people and relationship event.

---

# 7. Abstract-Word Translation Guard

Final model prompts may not rely on abstract judgement words as the main instruction.

Do not use these as substitutes for visual design:

- high chemistry
- cinematic
- premium
- high-end
- visual impact
- romantic tension
- sexy vibe
- luxury feeling
- strong hook

If a small style label remains, the prompt must already specify the visible cause through:

`PEOPLE + ACTION + HANDS + DISTANCE + GAZE + SCENE + PHYSICAL COLOR SOURCES + CAMERA`.

Relationship temperature, visual intimacy, and visual treatment are internal routing directions; the final prompt should express them through visible behavior. For editorial / high-end requests, compile asymmetry + body line + material contrast + directional light + narrative residue rather than adding `premium / cinematic / high-end`.

---

# 8. Prompt Compression Rule

Final prompts must be:

- minimal;
- precise;
- semantically complete;
- directly executable by the target model.

Internal cards may be detailed. Final prompts should not read like technical documentation.

Compression pipeline:

```text
SELECT ONLY VISIBLE / EXECUTABLE FIELDS
→ DROP NON-RENDERABLE RATIONALE
→ MERGE DUPLICATE IDENTITY CONTROLS
→ MERGE DUPLICATE REALISM CONTROLS
→ KEEP ONLY MODEL-RELEVANT COMPENSATION
→ FINAL PROMPT
```

Examples of duplicate cleanup:

Instead of stacking:

`same person + preserve identity + do not change face + identity unchanged`

use one compact identity-control statement with concrete anchors / reference assignment.

Instead of stacking:

`realistic skin + natural pores + real texture + fine skin texture + no plastic skin`

keep only the 2–3 controls materially useful for the selected model.

---

# 9. Prompt Pollution Guard

Never put these into the final visible model prompt unless a target system explicitly requires a technical identifier:

- benchmark status;
- `VALIDATED CORE`;
- `EVIDENCE-INFORMED`;
- internal risk level;
- Match Mode;
- fit label;
- compatibility explanation;
- `internal_selection_reason`;
- `why_this_combination_internal`;
- library IDs;
- analysis of user preferences;
- research notes;
- fallback logic that is not meant to render.

The model sees only the production facts required to make the requested image / video.

---

# 10. Reference Assignment Guard

Conceptual assignment:

```text
PERSON_A = USER_REFERENCE
PERSON_B = PARTNER_REFERENCE
FIRST_FRAME = APPROVED_COUPLE_IMAGE
```

If the target platform uses tokens such as `{{Mixed 1}}`, `{{Mixed 2}}`, or another reference syntax:

- state once which token is USER;
- state once which token is PARTNER;
- state once which token / image is FIRST FRAME;
- do not repeatedly @ / cite the same reference throughout the prompt unless the target system requires it.

Text supports reliable references; it does not replace them.

For identity:

`USER / PARTNER AUTHORITY SOURCES > APPROVED COUPLE FRAME > TEXT DESCRIPTION`.

For the exact recovery hierarchy, read `identity-failure-recovery.md`.

---

# 11. VIDEO_PROMPT_COMPILE_PACKET

Build internally:

```text
VIDEO_PROMPT_COMPILE_PACKET

FIRST_FRAME_VISUAL_TRUTH
PERSON_A_IDENTITY_REFERENCE
PERSON_B_IDENTITY_REFERENCE

CURRENT_STATE
CURRENT_HAND_GEOMETRY
CURRENT_CONTACT_GEOMETRY
CURRENT_EXPRESSION_GAZE

H3_CONTINUATION_SEED

SCENE_CONTINUITY
WARDROBE_CONTINUITY
COLOR_CONTINUITY

MINIMAX_H3_GRAMMAR
MODEL_ADAPTER_MINIMUM
```

Do not spend the video prompt re-describing the entire first frame. State only enough first-frame information to anchor continuity, then describe what happens next.

---

# 12. Video Prompt Compile Rule

Current default:

`MiniMax H3`

Default grammar remains:

```text
BEAT 1 — INITIATE
→ CUT / FRAMING CHANGE
→ BEAT 2 — ESCALATE / REACT
→ CUT / FRAMING CHANGE
→ BEAT 3 — PAYOFF / HOLD / CLOSE
```

Target:

- 3 readable relationship beats;
- approximately 2 purposeful cuts / framing changes;
- final readable hold;
- identity / wardrobe / scene continuity.

The grammar is a structure, not a fixed script.

Each actual beat must come from:

`APPROVED FIRST FRAME + COMBINATION CARD + CURRENT GEOMETRY`.

Every explicit shot should contain concise executable camera behavior integrated with the relationship action, for example:

- slow push-in following the approach;
- short lateral follow as one partner turns inward;
- side medium-close tracking the reaction;
- cut to tighter 3/4 as the body relationship changes;
- small backward follow during a playful pull.

Do not write `camera moves cinematically`.

Do not create decorative camera movement unrelated to the relationship beat.

---

# 13. Video Identity Control

Use one global slot assignment:

`PERSON_A = USER`

`PERSON_B = PARTNER`

After each cut, the conceptual slot assignment remains unchanged.

Do not repeat `preserve identity` in every sentence. Use one strong global identity rule plus necessary shot inheritance.

If identity actually fails, leave Prompt Compilation and route to `identity-failure-recovery.md`.

---

# 14. Still vs Video Responsibility

## IMAGE PROMPT

Creates one complete, immediately readable adult-couple relationship moment.

A still should not contain an entire 10-second timeline.

## VIDEO PROMPT

Continues from the approved first frame and creates new relationship events over time.

A video prompt should not rebuild / redesign the first frame from scratch.

---

# 15. Library Invocation Logic

## Image path

```text
portrait-identity-lock
→ partner-archetype-library
→ matching-engine
→ partner-identity-lock when needed
→ relationship-combination-router
   ↳ source Moment / Action / Expression-Gaze / Scene / Color + Sensuality + Editorial Intimacy libraries as SSOT
→ camera-realism-layer
→ model-routing-rules
→ model-adaptation
→ IMAGE PROMPT COMPILE
→ FINAL IMAGE PROMPT
```

## Video path

```text
APPROVED_COUPLE_IMAGE
→ USER / PARTNER identity packages
→ APPROVED RELATIONSHIP_COMBINATION_CARD when available
→ minimax-h3-couple-video
→ model-adaptation
→ VIDEO PROMPT COMPILE
→ FINAL VIDEO PROMPT
```

## Identity-recovery path

```text
USER FEEDBACK OR QC FAILURE
→ identity authority check
→ identity-failure-recovery
→ invalidate bad reference when needed
→ minimum recovery
→ RECOVERED AUTHORITY SOURCE + UNCHANGED DIRECTOR STATE
→ recompile only failed target state
→ identity QC
```

Do not reload unrelated benchmark / historical modules for normal runtime.

---

# 16. Missing Information Handling

## Real user photo provided

Run identity lock first. Do not beautify before identity is stabilized.

## No real user photo

Do not fabricate a locked identity. Use a generic demo route or request the missing image only when real-user identity continuity is essential.

## Partner preference missing

Use Matching Engine defaults. Explicit user preference wins.

## Relationship creative inputs missing

Use:

`RELATIONSHIP TEMPERATURE + CURRENT GEOMETRY + USER EXPLICIT CHOICES → RELATIONSHIP COMBINATION ROUTER`.

Do not ask the user to manually solve internal creative routing unless the product intentionally exposes those controls.

## Video requested without approved first frame

If high identity continuity matters:

1. create / output couple-image route;
2. obtain approved first frame;
3. compile H3 video.

---

# 17. User Feedback Routing

Use the smallest reroute.

## “换一个伴侣 / Try Another Match”

→ Matching Engine.

Keep USER identity and hard preferences. Exclude / replace the previous concrete Partner candidate according to Matching rules.

## “这个脸我不喜欢，但类型对”

→ keep Archetype / hard type preference; generate a new concrete Partner identity.

Do not change USER identity or director state unnecessarily.

## “换个动作”

→ Combination Router: reroute Action + caused Expression/Gaze; keep identities and compatible Scene.

## “换个 Moment / Try a Different Moment”

Keep USER + Partner identity / Partner lock. Reroute Moment + Action + Expression/Gaze first. Keep Scene/Color when still compatible.

## “换个场景”

Keep identities + compatible Moment/Action. Reroute Scene + Color/Wardrobe.

## “太暧昧 / 太大胆了”

Lower `VISUAL_INTIMACY_LEVEL` first. Change Relationship Temperature only if the user also wants a different emotional tone.

## “高级 / 奢华 / 性感 / 荷尔蒙 / 暧昧 / 大尺度”

Keep USER + Partner identity.

Default:
`VT3 FRAGRANCE-CAMPAIGN TENSION + V3 BOLD SENSUAL`.

Compile visible causes only:
- fitted / open / low-back / body-skimming wardrobe;
- close body distance;
- waist / lower-waist / upper-hip / upper-back / collar contact;
- reciprocal gaze / expression on both adults;
- asymmetric medium-close / close 3/4 framing;
- refined private scene;
- directional physically sourced light.

Do not output the abstract words as the main rendering instruction.

If the user explicitly wants the strongest non-explicit route, use V4.

## “太保守 / 不够性感 / 尺度不够”

Keep USER + Partner identity. Increase `VISUAL_INTIMACY_LEVEL`; reroute wardrobe exposure + body distance + contact zone + gaze + framing first. Only change Action / Scene when the current combination cannot physically support the requested level.

## “不高级 / 太普通 / 太像生活照”

Keep USER + Partner identity. Switch or strengthen `VISUAL_TREATMENT_PROFILE` first. Prefer `VT2 REFINED EDITORIAL` or `VT3 FRAGRANCE-CAMPAIGN TENSION`; then adjust composition asymmetry, body line, wardrobe material / silhouette and light direction. Do not merely add `高级 / premium / cinematic`.

## “不够有感觉”

Adjust first:

`MOMENT → GAZE / RESPONSE → BODY DISTANCE → ACTION TENSION LAYER`.

Do not immediately replace Partner.

## “不是我了 / 伴侣变脸 / 第二镜换人”

→ Identity Failure Recovery.

## “手穿模 / 手指错了”

→ Anatomy / Action correction. Do not rebuild identities if the people are still the same.

## “颜色不好看”

→ Color / Wardrobe reroute. Preserve identities / valid geometry.

## “伴侣不够帅/美，但还是同一个人”

→ Model / presentation / styling refinement.

This is not Identity Recovery unless the person's actual identity changed.

---

# 18. Identity Failure Fresh-Session Route

If a fresh-session user provides a failed result plus trusted identity references and says something like `第二镜不是我`, do not require Matching again.

Route:

```text
FAILED OUTPUT + TRUSTED USER/PARTNER REFERENCES
→ DETECT IDENTITY FAILURE
→ identity-failure-recovery
→ KEEP APPROVED FIRST FRAME / DIRECTOR STATE when valid
→ RESTORE CORRECT IDENTITY AUTHORITY
→ REWRITE / REGENERATE ONLY FAILED VIDEO STATE
```

Examples that route here:

- `不是我了 / 这不是我`;
- `脸变了`;
- `怎么年轻了 / 变老了`;
- `这个伴侣不是刚才那个`;
- `两个人脸混了 / 换脸了`;
- `第二个镜头换人了`;
- `越改越不像`.

Distinguish identity failure from Anatomy / Action / Scene / Color / Matching / Model-Presentation failures.

---

# 19. Default Model Routing

Current production defaults:

```text
PARTNER EXPLORATION / CANONICAL IDENTITY
→ image 2.5

FINAL USER-FACING COUPLE IMAGE
→ Banana2 Pro

APPROVED COUPLE IMAGE → 10s VIDEO
→ MiniMax H3
```

Seedance is historical evidence only, not the production default.

A compatible explicit user model choice may override these defaults.

Never compile one unchanged prompt for all models.

---

# 20. Output Contract

## Image prompt

```text
MODE
MODEL
SHORT PARTNER + RELATIONSHIP COMBINATION SUMMARY
FINAL IMAGE PROMPT
```

## Video prompt

```text
MODE
MODEL
FIRST-FRAME / IDENTITY ASSIGNMENT
SHORT 3-BEAT PROGRESSION
FINAL VIDEO PROMPT
```

## Full workflow

```text
1. USER IDENTITY RESULT
2. PARTNER CANDIDATE / APPROVAL STATE
3. PARTNER LOCK WHEN APPROVED
4. RELATIONSHIP COMBINATION SUMMARY
5. FINAL IMAGE PROMPT / IMAGE
6. COUPLE IMAGE APPROVAL GATE
7. FINAL VIDEO PROMPT / VIDEO
```

## Identity recovery

```text
1. DETECT WHO DRIFTED
2. CLASSIFY MINIMUM FAILURE
3. RETURN TO CORRECT IDENTITY AUTHORITY
4. DISCARD BAD REFERENCE IF NEEDED
5. KEEP UNFAILED DIRECTOR ASSETS
6. RECOMPILE / REGENERATE FAILED STATE ONLY
7. QC
```

---

# 21. Prohibited Behaviors

The standalone Skill must not:

- depend on temporary benchmark memory;
- output `same as before` instead of a self-contained prompt;
- collapse image and video into one universal prompt;
- mechanically reuse one prompt across models;
- skip identity lock when a real uploaded user photo exists and continuity matters;
- invent unseen body identity facts;
- expose internal matching / combination rationale as visible subjects;
- copy full internal cards into a model prompt;
- rebuild people from text after reliable references exist;
- generate high-consistency video with unclear first-frame authority;
- let color / lighting / camera language overpower people / action / scene;
- treat `sexy / sensual / bold` as sufficient visible instructions without compiling the physical causes;
- rely on abstract judgement words instead of visible instructions;
- use fixed gender roles;
- make both adults use identical smile / gaze behavior by default;
- allow one-sided chemistry where the AI Partner is affectionate but the USER remains blank / cold;
- default final fantasy couple imagery to beige lifestyle / stock-photo staging when editorial treatment is not explicitly requested;
- approve a VT3/V3 still with fewer than 5 of 7 concept-image DNA signals;
- repair drift from a drifted output;
- reopen Matching because an approved partner drifted downstream;
- treat hand / scene / palette / attractiveness problems as identity failure when identity is stable;
- brute-force Partner × Moment × Action × Expression × Scene × Color permutations;
- bypass `relationship-combination-router.md` when the creative combination is not explicitly fixed by the user;
- leak benchmark status / internal IDs / risk labels / selection rationale into final prompts.

---

# 22. Interface Continuity Audit

Required pipeline interfaces:

```text
MATCH_CANDIDATE_CARD
→ PARTNER_APPEARANCE_CARD / visible_prompt_payload
→ GENERATED PARTNER CANDIDATE
→ APPROVAL
→ PARTNER_IDENTITY_CARD
```

Then:

```text
PARTNER_IDENTITY / APPEARANCE
+ USER_IDENTITY
→ RELATIONSHIP_COMBINATION_CARD
→ IMAGE_PROMPT_COMPILE_PACKET
→ FINAL IMAGE PROMPT
```

And after image approval:

```text
APPROVED_RELATIONSHIP_COMBINATION_CARD
+ APPROVED_COUPLE_IMAGE
+ USER/PARTNER REFERENCES
→ VIDEO_PROMPT_COMPILE_PACKET
→ MINIMAX H3 PROMPT
```

Recovery interface:

```text
RECOVERED AUTHORITY SOURCE
+ UNCHANGED DIRECTOR STATE
→ PROMPT RECOMPILE
```

Do not regenerate Moment / Scene / Color merely because identity recovery occurred.

---

# 23. Standalone Static Acceptance Cases｜STEP 9

No real generation is required for these checks.

## CASE A — Real user + Men + Mature & Confident + Flirty

Expected route:

`Identity Lock → USER_PREFERENCE_CARD → Matching/P1 → concrete Partner Candidate → Partner approval/lock → Combination Router → IMAGE_PROMPT_COMPILE_PACKET → Banana2 Pro Prompt`

Expected output: complete Partner / Couple image prompt flow without internal IDs exposed.

Status: `PASS`.

## CASE B — Real user + Women + Surprise Me + Sweet

Expected route:

`Identity Lock → Matching Surprise route → adult female-presentation candidate → Router Sweet rotation → Image Compile`.

No ethnicity / orientation inference from photo.

Status: `PASS`.

## CASE C — Man × Man + Romantic

Same Match / Router / Prompt grammar; no heterosexual role inheritance.

Status: `PASS`.

## CASE D — Woman × Woman + Playful

Same role-neutral Action / Expression routing; reciprocal response carries relationship read.

Status: `PASS`.

## CASE E — “帮我换一个 Moment”

Keep USER / PARTNER identity; call `Try a Different Moment`; reroute Moment + Action + Expression/Gaze first.

Status: `PASS`.

## CASE F — Approved Couple Image → “写10秒视频提示词”

Enter MODE B; first frame = visual truth; identities = USER/PARTNER references; use Combination state / H3 seed when available.

Status: `PASS`.

## CASE G — High-consistency video but no approved first frame

Route first to couple-image / first-frame creation.

Status: `PASS`.

## CASE H — “第二镜不是我”

Identity Recovery; preserve approved director state; do not reopen Matching.

Status: `PASS`.

## CASE I — “伴侣不够帅/美，但还是同一个人”

Model / presentation refinement, not identity recovery.

Status: `PASS`.

## CASE J — Completely fresh session

Uses current input + Skill files only; no benchmark memory required.

Status: `PASS`.

---

# 24. Fresh-Session Requirement

A fresh-session invocation must be sufficient to:

- lock a real uploaded user identity when present;
- resolve a Partner from choice-based preferences;
- preserve or resolve a user-selected visual-intimacy level;
- establish a concrete Partner identity source;
- call the Relationship Combination Router;
- compile a self-contained still prompt;
- preserve the approved couple state;
- compile a self-contained MiniMax H3 video prompt;
- enter identity recovery directly when the failure type warrants it.

The Skill must never require knowledge of how the libraries were built, what tests happened previously, or what temporary chat produced the rules.
