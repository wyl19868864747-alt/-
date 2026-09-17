# Matching / Moment / Model Benchmark

## Status

`DOCUMENTED FROM REAL USER GENERATIONS`

This benchmark validates three things:

1. matching modes produce different believable partner directions;
2. moment type changes sweetness / intimacy / romantic tension;
3. image 2.5 and Banana2 Pro require different prompt compensation and serve different product goals.

---

# Matching Results

## Harmony Match

Result: PASS.

Observed:

- strongest natural couple-likeness;
- stable / comfortable relationship feeling;
- did not require copying facial features;
- lower fantasy tension than stronger modes.

## Preference Match

Result: PASS.

Observed:

- mature dominant partner preference remained readable;
- high compatibility with the softer refined test user;
- became the selected couple for later moment-type testing.

## Complementary Contrast

Result: PASS WITH LIMITS.

Observed:

- stronger body / masculinity contrast was readable;
- risk of reading as bodyguard / trainer increases when physical contrast is pushed too far;
- partner identity separation is required, especially in image 2.5.

---

# Prompt Compile Failure Learned

During partner-solo testing, prompts that explained how a male candidate should match a female user sometimes caused the model to render both people.

Validated fix:

`MATCHING LOGIC` must remain internal.

For solo generation:

`MATCH_CANDIDATE_CARD → VISIBLE SUBJECT FILTER → MODEL PROMPT`

Only visible subjects belong in the final prompt.

---

# Moment Type Results

## Shoulder Lean

Result: PASS.

Strength:

- natural
- safe
- long-term sweetness

Weakness:

- lower romantic tension / fantasy value

Decision:

`SECONDARY SAFE MOMENT`

## Close Eye Contact

Result: STRONG PASS.

Strength:

- sweetness
- believable intimacy
- eye-line chemistry
- suitable for both models

Decision:

`DEFAULT REALISTIC SWEET MOMENT`

## Soft Almost-Kiss

Result: STRONGEST HERO PASS.

Strength:

- highest heart-flutter potential
- romantic tension
- fantasy / best-partner feeling

Decision:

`DEFAULT HERO MOMENT`

---

# image 2.5 Results

Observed strengths:

- highest partner attractiveness
- strongest aspirational / fantasy feeling
- strong Soft Almost-Kiss result
- strong Close Eye Contact result

Observed weaknesses:

- darker / greyer / more cement-like tonal character in some outputs
- weaker real-camera skin microtexture
- visible generation noise stronger than Banana2 Pro baseline

Prompt compensation tested:

- high definition
- low noise
- clean image
- brighter natural window light
- do not render dark / grey / gloomy
- real skin texture
- medium-telephoto real-photo framing

Result:

- noise improved materially;
- brightness improved;
- hero quality remained strong;
- residual grey / cement-like rendering remains partially model-driven.

Decision:

`DEFAULT HERO / FIRST-IMPRESSION MODEL = image 2.5`

---

# Banana2 Pro Results

Observed strengths:

- strong photographic cleanliness
- low visible generation noise
- believable couple-photo feel
- strong real-world composition

Observed weaknesses:

- more conservative attractiveness
- can under-express romantic sweetness without explicit relationship action
- skin can become overly smooth / beauty-retouched
- latest realism compensation run showed stronger contrast / overexposure and brighter clipped-looking skin highlights

Interpretation:

Real-world camera texture should not be approximated by simply adding more grain / sensor language. Use skin microtexture + exposure / tonal controls instead.

Decision:

`SECONDARY REALISM / CANDID MODEL = Banana2 Pro`

Future Banana regression should test:

- natural visible pores
- fine irregular skin texture
- protected highlights
- gentle highlight roll-off
- soft low-contrast tone
- no HDR / clipped highlights

---

# Current Product Route

Default couple image route:

```text
LOCK USER
↓
RESOLVE PARTNER
↓
MATCH MODE
↓
MOMENT TYPE
↓
MODEL ROUTER
↓
MODEL-SPECIFIC PROMPT
↓
IDENTITY / CHEMISTRY / REALISM QC
```

Default first-impression route:

`Preference or Harmony partner → Soft Almost-Kiss → image 2.5`

Default realism route:

`Preference or Harmony partner → Close Eye Contact → Banana2 Pro`

---

# Not Yet Validated

- Back Hug
- Sweet Selfie
- Playful Outdoor Couple
- dedicated intimate scene library
- stronger sensual pose library
- image-to-video continuity

Do not promote these to default production behavior until tested.
