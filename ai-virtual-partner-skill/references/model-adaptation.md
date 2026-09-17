# Model Adaptation｜模型适配规则

## Purpose

Do not mechanically reuse one prompt across image and video models. The AI Virtual Partner Skill must compile model-specific prompts from the same structured intent.

Only record behaviors supported by actual user runs or repeated project feedback. Treat this file as an empirical operating profile, not a vendor-spec sheet.

---

# image 2.5

## Current observed strengths

- Produces higher-attractiveness faces more readily than Banana2 Pro in current archetype and couple tests.
- Strong at idealized partner exploration and readable fantasy archetypes.
- Strong at romantic hero moments, especially `Soft Almost-Kiss` and `Close Eye Contact`.
- Often gives a stronger “unknown best partner / heart-flutter” first impression.
- Successfully separated Soft Refined / Clean Masculine / Power Masculine / Mature Dominant male types.
- Successfully separated Soft Feminine / Elegant Feminine / Dominant Beauty female types.
- In the P1 four-view identity test, preserved the selected partner more consistently than Banana2 Pro across front / 45-degree / profile / close-up after prompt compensation.

## Current observed risks

- More visible image noise / micro-grain / dirty texture than Banana2 Pro baseline.
- Can render dark, grey, muddy or "cement-like" tonal character.
- Real-camera skin microtexture may be weaker even when the image is attractive.
- Tends toward a shared beauty-template aesthetic, especially across attractive female portraits and multiple attractive male candidates.
- Can over-beautify, reducing structural identity diversity.
- Identity close-ups can drift younger / softer unless the prompt explicitly states `identity completion, not redesign`.
- `F08 Glamorous Bombshell` repeatedly failed to generate in the current platform/runtime; compatibility remains unverified. Do not generalize this as a permanent model limitation.

## Validated prompt compensation

The following improved current couple and identity-reference outputs:

- `high definition`
- `low noise`
- `clean image`
- brighter / airy natural window light
- `not dark`
- `not grey / muddy`
- avoid gloomy dark grading
- real skin texture / pores
- medium-telephoto close portrait photography
- `identity completion, not redesign`
- preserve original age / face width / eye / nose / jaw structure
- explicit anti-template / anti-rebeautification language

Observed result:

- noise improved materially;
- exposure / brightness improved;
- high-attractiveness hero quality remained strong;
- P1 close-up identity stability improved substantially;
- residual grey / cement-like rendering remained and is treated as partly model-driven.

## Prompt strategy

Use image 2.5 primarily for:

- attraction exploration
- archetype differentiation
- aspirational partner generation
- hero / first-impression couple image
- high romantic tension with restrained intimacy
- current preferred canonical partner reference-sheet generation

Protect:

- natural skin texture
- natural asymmetry
- non-template facial identity
- candidate identity separation
- realistic age appearance
- original partner facial geometry when building reference assets

Do not rely on generic `beautiful / handsome / glamorous` alone; they can collapse outputs toward a shared idealized template.

---

# Banana2 Pro

## Current observed strengths

- Very low visible generation noise in baseline outputs.
- Strong photorealistic portrait / couple feel.
- Strong heritage-appearance naturalness.
- Less likely than image 2.5 to push every subject toward one idealized beauty template.
- Strong believable candid composition.
- Mature / sensual / glamorous realism performed particularly well in validated tests.

## Current observed risks

- Conservative beauty prior: often produces believable ordinary people rather than aspirational partner-level attractiveness.
- Abstract style words such as `elegant`, `high-end`, `dominant`, or `romantic` may under-express unless translated into visible structure, posture, gaze and relationship action.
- Elegant Feminine repeatedly drifted toward understated / plain / everyday realism.
- Dominant Beauty can be readable but less visually striking than image 2.5.
- Skin can become overly smooth / beauty-retouched in couple close-ups.
- A recent realism-compensation run showed excessive brightness / higher contrast / overexposed-looking skin highlights.
- Some current outputs show a pale / white hazy veil over the image surface; this is treated as a current model tendency to suppress when it appears.
- In the P1 four-view identity test, front / 45-degree / profile retained useful realism but close-up substantially reinterpreted facial identity; therefore stronger photographic realism did not equal stronger identity canonicalization.

## Prompt strategy

Use Banana2 Pro primarily for:

- photorealism validation
- candid couple photography
- heritage-appearance validation
- low-noise realistic portrait direction
- realistic mature / sensual archetypes
- photographic-realism support after identity has already been established elsewhere
- current realistic couple first-frame generation

Do **not** waste prompt space repeatedly asking for `low noise`; baseline outputs already show this as a model strength.

Do **not** mix structurally conflicting Banana-derived views into an image 2.5 canonical partner reference package.

To raise attractiveness / chemistry, specify visible causes:

- facial structure tendency
- grooming
- body state
- posture
- gaze relationship
- physical proximity
- affectionate / flirtatious relationship action

Current practical compensation should stay minimal and evidence-driven. Useful additions when needed include:

- real visible pores / fine skin microtexture;
- minor natural imperfections;
- `not overexposed`;
- `avoid a pale white hazy veil / white foggy filter`; 
- `clear transparent image surface`.

Do not automatically stack a long group of contrast / white-balance / HDR / highlight-control instructions. In current testing, over-controlling tone made results flatter or overly bright. Add only the smallest correction needed for the current failure.

Do not rely on heavy `film grain / sensor texture` wording as the primary realism mechanism.

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

## Validated couple-start behavior

A real 5-second A/B couple-start test produced a reusable finding:

- the `standard` version felt more romantic / ambiguous than the version explicitly prompted as `more intimate`;
- the stronger result used a slow lean-in, preserved a small unresolved face distance and held the moment rather than resolving contact quickly;
- dimensional side/back window light gave faces more separation and atmosphere than a flatter high-key white backlight result in the tested setup;
- stronger wording alone did not create stronger tension.

Current motion principle:

`APPROACH → MICRO-PAUSE → HOLD UNRESOLVED DISTANCE`

For current couple starts:

`LEAN-IN MOMENT` is the preferred first frame and `PRE-KISS PAUSE` is a later tension beat / second keyframe.

Do not begin at minimum face distance unless the shot is intentionally very short.

## Prompt strategy

Seedance 2.5 prompts should prioritize explicit executable film language:

`scene → subject → blocking/action → shot size → camera position → camera move → spatial continuity → lighting → rhythm/cut logic`

Use concrete descriptions for:

- who is where
- who moves first
- what the camera sees
- shot-size changes
- camera direction and movement
- light source and continuity
- hand-contact stability
- face-distance progression
- when the action pauses and why
- when cuts happen and why

For romantic tension, translate abstract intent into:

- approach speed;
- gaze hold;
- hand placement;
- body distance;
- unresolved final distance;
- micro-pause duration / beat.

Avoid replacing this information with abstract judgments such as `cinematic`, `high-energy`, `more intimate`, or `strong tension`.

For identity-critical couple video, assign USER and PARTNER references explicitly and inherit the approved couple frame rather than rebuilding identities from text.

Current detailed first-frame / motion-start rules live in `seedance-couple-video-start.md`.

---

# Shared Rule

One structured creative decision may compile differently per model.

Therefore:

`STRUCTURED INTENT → MODEL ADAPTER → MODEL-SPECIFIC PROMPT`

Never assume:

`ONE PROMPT = ALL MODELS`

Current product-level routing is defined in `model-routing-rules.md`.

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