# Model Adaptation｜模型适配规则

## Purpose

Do not mechanically reuse one prompt across image and video models. The AI Virtual Partner Skill must compile model-specific prompts from the same structured intent.

Only record behaviors supported by actual user runs or repeated project feedback. Treat this file as an empirical operating profile, not a vendor-spec sheet.

---

# image 2.5

## Current observed strengths

- Produces higher-attractiveness faces more readily than Banana2 Pro in the current archetype tests.
- Strong at idealized partner exploration and readable fantasy archetypes.
- Successfully separated Soft Refined / Clean Masculine / Power Masculine / Mature Dominant male types.
- Successfully separated Soft Feminine / Elegant Feminine / Dominant Beauty female types.
- Often gives stronger aspirational / high-attractiveness results with relatively little prompting.

## Current observed risks

- More visible image noise / micro-grain / dirty texture than Banana2 Pro in current runs.
- Tends toward a shared beauty-template aesthetic, especially across attractive female portraits.
- Can over-beautify, reducing structural archetype diversity.
- `F08 Glamorous Bombshell` repeatedly failed to generate in the current platform/runtime; compatibility remains unverified. Do not generalize this as a permanent model limitation.

## Prompt strategy

Use image 2.5 primarily for:

- attraction exploration
- archetype differentiation
- aspirational face / fantasy partner exploration

When realism matters, explicitly protect:

- natural skin texture
- natural asymmetry
- non-template facial identity
- structural differences between archetypes
- realistic age appearance

Do not rely on generic `beautiful / handsome / glamorous` alone; they can collapse outputs toward a shared idealized template.

---

# Banana2 Pro

## Current observed strengths

- Very low visible noise in current outputs.
- Strong photorealistic portrait feel.
- Natural skin and photographic cleanliness.
- Strong heritage-appearance naturalness in the current benchmark.
- Less likely than image 2.5 to push every subject toward one idealized beauty template.
- Mature / sensual / glamorous realism performed particularly well in the validated F08 test.

## Current observed risks

- Conservative beauty prior: often produces believable ordinary people rather than aspirational partner-level attractiveness.
- Abstract style words such as `elegant`, `high-end`, or `dominant` may under-express unless translated into visible structure, posture, grooming, and social signal.
- Elegant Feminine repeatedly drifted toward understated / plain / everyday realism rather than strong aspirational elegance.
- Dominant Beauty can be readable but may remain less visually striking than image 2.5.

## Prompt strategy

Use Banana2 Pro primarily for:

- photorealism validation
- heritage-appearance validation
- low-noise final portrait direction
- realistic mature / sensual archetypes

Do **not** waste prompt space repeatedly asking for `low noise`; current runs already show this as a model strength.

To raise attractiveness, specify visible causes rather than abstract praise:

- facial structure tendency
- body state
- grooming
- posture
- social signal
- mature / refined / sensual presentation

Keep the prompt concrete and photographic.

---

# Seedance 2.5

## Current user-validated operating profile

The user's production workflow primarily uses Seedance 2.5 for video.

Observed / provided working characteristics:

- can generate up to roughly 30 seconds in one generation in the user's current workflow;
- can accept a large reference set, up to roughly 50 references in the user's current workflow;
- can automatically cut between shots;
- responds better when camera, lighting, shot content, blocking, and storyboard intent are described explicitly;
- behaves more like a professional film-production model than a casual one-line text-to-video tool.

## Prompt strategy

Seedance 2.5 prompts should prioritize explicit executable film language:

`scene → subject → blocking/action → shot size → camera position → camera move → spatial continuity → lighting → rhythm/cut logic`

Use concrete descriptions for:

- who is where
- who moves first
- what the camera sees
- shot size changes
- camera direction and movement
- light source and continuity
- when cuts happen and why

Avoid replacing this information with abstract judgments such as `cinematic`, `high-energy`, or `strong tension`.

For identity-critical couple video, later modules must compile reference assignments explicitly for USER and PARTNER rather than relying only on text.

---

# Shared Rule

One structured creative decision may compile differently per model.

Example:

`F05 Dominant Beauty`

is one archetype card, but:

- image 2.5 may need stronger anti-template / natural-skin controls;
- Banana2 Pro may need stronger visible attractiveness / presence cues;
- Seedance 2.5 will need explicit performance, camera, spatial, and reference continuity instructions.

Therefore:

`STRUCTURED INTENT → MODEL ADAPTER → MODEL-SPECIFIC PROMPT`

Never assume:

`ONE PROMPT = ALL MODELS`

---

# Evidence Update Rule

Every meaningful user result may update this file only when it yields a reusable model behavior.

Record:

- model name / version
- task type
- prompt pattern
- successful behavior
- failure behavior
- repeatability / confidence
- resulting adaptation rule

One isolated failure should be recorded as `observed in current runtime`, not promoted to a permanent universal limitation without repetition.
