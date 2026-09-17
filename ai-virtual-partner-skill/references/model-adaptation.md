# Model Adaptation｜模型适配规则

## Purpose

Do not mechanically reuse one prompt across image and video models. Compile model-specific prompts from the same structured intent.

Only record behaviors supported by actual user runs or repeated project feedback. Treat this file as an empirical operating profile, not a vendor-spec sheet.

---

# image 2.5

## Current observed strengths

- Produces higher-attractiveness faces readily in current partner / archetype tests.
- Strong at idealized partner exploration and readable attraction archetypes.
- Strong at romantic Hero moments such as Soft Almost-Kiss / Close Eye Contact.
- In the P1 four-view identity test, preserved selected-partner identity more consistently than Banana2 Pro across front / 45° / profile / close-up after compensation.

## Current observed risks

- More visible generation noise / micro-dirty texture than Banana2 Pro baseline.
- Can render dark, grey, muddy or cement-like tonal character.
- Can collapse multiple attractive candidates toward a shared beauty template.
- Identity close-ups may drift younger / softer unless explicitly framed as identity completion rather than redesign.

## Validated compensation

Useful current corrections include:

- high definition;
- low noise;
- clean image;
- brighter / airy natural exposure;
- not dark / not grey-muddy;
- real skin texture / pores;
- identity completion, not redesign;
- preserve original age / face width / eye / nose / jaw structure;
- explicit anti-template / anti-rebeautification language.

## Current production role

Use image 2.5 primarily for:

- attractive partner exploration;
- archetype differentiation;
- aspirational partner alternatives;
- canonical partner reference-sheet construction;
- recovery route when Banana2 Pro becomes too ordinary.

Do not rely on generic `beautiful / handsome / glamorous` alone.

---

# Banana2 Pro

## Current observed strengths

- Very low visible generation noise in baseline outputs.
- Strong photorealistic couple / candid-photo feel.
- Strong heritage-appearance naturalness.
- Strong believable relationship composition.
- Current preferred user-facing couple-image route.

## Current observed risks

- Conservative beauty prior can produce believable but ordinary-looking people.
- Abstract style words under-express unless translated into face, body, posture, gaze and relationship action.
- Skin may become too smooth / beauty-retouched.
- Some outputs become too bright or show a pale / milky white hazy veil.
- In the P1 four-view test, close-up identity reinterpretation was stronger than image 2.5, so Banana2 Pro is not the current canonical identity-sheet model.

## Current practical compensation

Keep compensation minimal and evidence-driven:

- high-attractiveness adult couple;
- real visible pores / fine skin microtexture;
- slight natural imperfections;
- realistic candid photography;
- not overexposed;
- avoid a pale white hazy veil / white foggy filter;
- clear transparent image surface.

Do not waste tokens repeatedly asking for low noise.

Do not stack long HDR / contrast / white-balance / highlight restrictions unless a real failure requires them; over-control flattened prior outputs.

## Current production role

Use Banana2 Pro primarily for:

- final user-facing couple image;
- realistic candid relationship moments;
- natural multi-heritage appearance;
- approved first frame for MiniMax H3 video.

---

# MiniMax H3｜CURRENT VALIDATED VIDEO ROUTE

## Current status

MiniMax H3 is the current production video model for the AI Virtual Partner Skill.

Status: `VALIDATED — FIRST PRODUCTION ROUTE`

A real 10-second Man × Man Night City Window generation was reviewed as basically usable and established the current operating grammar:

- multiple visible relationship beats can occur within 10 seconds;
- shot / framing changes are operationally usable;
- identities, wardrobe and scene can remain sufficiently stable across the clip;
- the result is more engaging than the prior single-shot slow-approach Seedance route.

This is enough to stop broad benchmarking. Continue per-output QC during real use.

## Prompt strategy

Use:

`APPROVED COUPLE IMAGE = VISUAL TRUTH`

Input priority:

`APPROVED_COUPLE_IMAGE + USER_REFERENCE_PACKAGE + PARTNER_REFERENCE_PACKAGE`

Compile the 10-second scene as:

`BEAT 1 — INITIATE`
→ `CUT / SHOT CHANGE`
→ `BEAT 2 — ESCALATE / REACT`
→ `CUT / SHOT CHANGE`
→ `BEAT 3 — PAYOFF / HOLD / CLOSE`

Current default target:

- about 3 readable relationship beats;
- about 2 purposeful cuts / framing changes;
- visible body-contact / posture / gaze progression;
- reciprocal reactions from both partners;
- final 0.8–1.2s readable closing hold.

Use concrete instructions for:

- who initiates;
- body orientation;
- hand trajectory;
- gaze / micro-expression;
- shot size;
- camera position / movement;
- cut timing;
- scene / wardrobe / color continuity;
- identity continuity;
- final state.

Do not spend 10 seconds repeating only `slowly lean closer`.

Translate `more flirtatious / more sensual / more exciting` into visible interaction such as:

- waist pull / side turn;
- hand moving from chest to shoulder / upper back;
- playful half-turn into embrace;
- face / hair-side touch when anatomically safe;
- cheek / temple / side-neck proximity within platform limits;
- gaze → reaction smile → renewed approach;
- brief affectionate contact when the platform / model permits;
- medium two-shot → side medium-close → tighter reaction / payoff shot.

All people are adults. Keep interaction mutual / reciprocal and within the connected platform / model's permitted adult-content range.

---

# Seedance 2.5｜HISTORICAL EVIDENCE ONLY

Seedance 2.5 is not the current production video route for this Skill.

Useful retained findings:

- unresolved distance + micro-pause can create stronger romantic tension than rushing to contact;
- dimensional side / back window light can improve face separation and atmosphere;
- stronger wording alone did not create stronger intimacy.

Historical timing principle:

`APPROACH → MICRO-PAUSE → HOLD UNRESOLVED DISTANCE`

10-second failure finding in the user's current runtime:

- the clip stayed in essentially one composition / one relationship action for too long;
- motion felt too conservative and repetitive;
- meaningful shot progression was not achieved;
- the higher-tension B route failed to generate.

Therefore:

`DO NOT USE SINGLE-SHOT SLOW APPROACH AS THE DEFAULT 10-SECOND PRODUCT TEMPLATE.`

Keep Seedance only as historical evidence unless the production model changes again.

---

# Shared Rule

`STRUCTURED INTENT → MODEL ADAPTER → MODEL-SPECIFIC PROMPT`

Never assume:

`ONE PROMPT = ALL MODELS`

---

# Evidence Update Rule

Only update a model rule when a real result yields a reusable behavior.

Record:

- model / version;
- task;
- successful behavior;
- failure behavior;
- confidence;
- resulting production rule.

Do not turn one isolated failure into a universal vendor claim.