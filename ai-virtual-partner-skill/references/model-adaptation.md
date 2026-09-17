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

# MiniMax H3｜CURRENT VIDEO ROUTE

## Current status

MiniMax H3 is the current production video model selected by the user for this Skill.

This route replaces Seedance 2.5 for future AI Virtual Partner video generation.

Current H3 couple-video behavior is **not yet fully runtime-validated** in this Skill. Treat the first production clip as a small representative validation, not a new large benchmark campaign.

## Prompt strategy

Compile the 10-second interaction as a short directed scene with multiple relationship beats rather than one stretched micro-action.

Default structure:

`APPROVED FIRST FRAME → BEAT 1 → CUT / SHOT CHANGE → BEAT 2 → CUT / SHOT CHANGE → BEAT 3 / CLOSE`

For the default 10-second route, target:

- roughly 3 readable relationship beats;
- roughly 2 purposeful shot / framing changes;
- one clear escalation in body contact / gaze / posture;
- one distinct reaction or playful / intimate micro-event;
- a readable ending beat instead of an abrupt cutoff.

Use concrete instructions for:

- who initiates;
- body direction;
- hand trajectory;
- gaze / facial reaction;
- shot size;
- camera position / move;
- cut timing;
- scene / wardrobe / color continuity;
- identity continuity;
- ending state.

Do not spend ten seconds repeating only `slowly lean closer`.

Do not use abstract intensity words alone. Translate `more flirtatious / more sensual / more exciting` into visible interaction such as:

- waist pull / side turn;
- hand moving from chest to shoulder / upper back;
- playful half-turn into an embrace;
- hair / face-side touch where anatomically safe;
- cheek / temple / neck-side proximity within platform limits;
- eye contact → reaction smile → renewed approach;
- brief affectionate contact when the model / platform permits it;
- change from medium two-shot to side close-up / tighter reaction shot.

Identity rule:

`APPROVED_COUPLE_IMAGE = visual truth`

Do not reconstruct either person from text after approval.

Input priority:

`APPROVED_COUPLE_IMAGE + USER_REFERENCE_PACKAGE + PARTNER_REFERENCE_PACKAGE`

Current safety / product rule:

- all people are adults;
- increase sensuality only within the connected platform / model's allowed adult-content range;
- preserve mutual / reciprocal body language;
- no coercive or non-consensual framing.

---

# Seedance 2.5｜HISTORICAL TEST EVIDENCE

Seedance 2.5 is no longer the current production video route for this Skill.

## Useful historical findings

A real 5-second A/B couple-start test produced a reusable interaction finding:

- the `standard` version felt more romantic / ambiguous than the version explicitly prompted as `more intimate`;
- the stronger result used a slow lean-in, preserved a small unresolved face distance and held the moment rather than resolving contact quickly;
- dimensional side/back window light gave faces more separation and atmosphere than a flatter high-key white backlight result in the tested setup;
- stronger wording alone did not create stronger tension.

Historical motion principle worth keeping:

`APPROACH → MICRO-PAUSE → HOLD UNRESOLVED DISTANCE`

## 10-second failure finding

The later 10-second Seedance test exposed a product-level problem:

- the generated video stayed in essentially one composition / relationship action for most of the duration;
- motion was too conservative and visually repetitive;
- no meaningful cut / shot progression occurred despite the product needing a more engaging 10-second interaction;
- the higher-tension B route failed in the user's current Seedance runtime.

Therefore:

`DO NOT USE SINGLE-SHOT SLOW APPROACH AS THE DEFAULT 10-SECOND PRODUCT TEMPLATE.`

Keep Seedance notes only as historical evidence for romantic timing / unresolved distance.

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
