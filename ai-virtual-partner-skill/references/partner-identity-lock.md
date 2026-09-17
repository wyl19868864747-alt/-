# Partner Identity Lock｜虚拟伴侣身份锁定

## Purpose

Turn an approved generated partner candidate into a reusable **specific visual identity** for later couple images and video.

This module preserves the chosen partner; it must not redesign or re-cast the partner.

Core separation:

`PARTNER ARCHETYPE = PERSON DESIGN SOURCE`

`APPROVED PARTNER CANDIDATE = SPECIFIC PERSON SOURCE`

`PARTNER IDENTITY LOCK = KEEP THAT PERSON THE SAME`

---

# 1. Upstream Interface

Start from:

`PARTNER_APPEARANCE_CARD`
→ partner candidate generation
→ candidate review / approval
→ `ORIGINAL_APPROVED_PARTNER`

The abstract `PARTNER_APPEARANCE_CARD` helps create the candidate, but once a specific candidate is approved, the **actual approved image becomes the identity source**.

Do not repeatedly regenerate from the archetype and call the results the same person.

When the approved candidate visibly preserves archetype-distinguishing features, carry those features into the identity lock.

Examples:

- face length / width tendency;
- brow-eye spacing / eye depth;
- nose structure;
- jaw / chin shape;
- hairline / hair silhouette;
- stable freckles / marks;
- facial-hair pattern;
- adult visual age;
- body-build / shoulder-width category.

Do not force a planned archetype feature into the identity card if the final approved image does not actually show it.

`APPROVED VISIBLE IDENTITY > ABSTRACT ARCHETYPE PLAN`

---

# 2. PARTNER_IDENTITY_CARD

Create from the approved partner reference:

```text
PARTNER_IDENTITY_CARD

source_archetype_id
source_partner_appearance_card
approved_partner_reference
adult_age_band
heritage_appearance

face_shape
head_proportions
face_length_width_tendency
cheekbone_character
brow_structure
brow_eye_spacing
eye_shape
eye_spacing
eye_depth
nose_structure
lip_structure
jaw_structure
chin_structure

hairline
hair_color
hair_texture
base_hairstyle
facial_hair

skin_tone
skin_state
stable_marks

body_build
shoulder_width
stable_body_signal

stable_distinctive_feature_01
stable_distinctive_feature_02
stable_aura_signal
```

Fields unsupported by the approved image should remain `UNKNOWN` / `LOW CONFIDENCE` instead of being invented.

Do not infer new identity traits simply to make the partner more attractive.

---

# 3. Lock Levels

## HARD IDENTITY ANCHORS

Do not change:

- face shape / head proportions;
- eye shape / spacing;
- nose structure;
- lip proportions;
- jaw / chin structure;
- visual age;
- core hairline;
- core facial identity;
- stable distinctive features that materially identify the person.

## STRONG LOCKS

Keep highly stable:

- stable skin tone;
- brow structure;
- hair color / base cut;
- body-build category;
- shoulder-width category;
- overall mature / soft / dominant / refined identity signal.

## SOFT LOCKS

May change slightly:

- expression;
- minor hair styling;
- grooming state within identity-safe bounds;
- small skin-state changes;
- subtle posture.

## FREE VARIABLES

May change:

- clothing;
- environment;
- action / pose;
- camera;
- lighting;
- Moment;
- Expression / Gaze;
- scene / color styling.

Free variables must not trigger identity rebuilding.

---

# 4. Partner Reference Package

For identity-critical downstream work, build only when complexity justifies it:

`ORIGINAL_APPROVED_PARTNER`
+
`FRONT VIEW`
+
`45-DEGREE VIEW`
+
`SIDE PROFILE`
+
`FACE CLOSE-UP`

The purpose is identity coverage across viewing angles, not a character-design sheet.

All views must preserve:

- same person;
- same adult visual age;
- same hairline;
- same facial geometry;
- same stable skin tone / selected heritage appearance;
- same base hairstyle;
- same stable distinctive features.

Do not use the four-view process to beautify, sharpen, feminize / masculinize, age-shift or redesign the partner.

---

# 5. Reference Priority

Partner authority order:

`ORIGINAL_APPROVED_PARTNER > PARTNER_IDENTITY_CARD > APPROVED_REFERENCE_PACKAGE > APPROVED_COUPLE_FRAME > TEXT DESCRIPTION > ABSTRACT ARCHETYPE DESCRIPTION`

The archetype is a design source, not a higher authority than the chosen person's real generated face.

AI-generated views strengthen angle coverage but may not overwrite the original approved identity.

---

# 6. Reference Sheet QC

Check every generated view for:

- `SAME PERSON`;
- `FACIAL GEOMETRY`;
- `VISUAL AGE`;
- `HAIRLINE`;
- `SKIN / HERITAGE APPEARANCE`;
- `DISTINCTIVE FEATURES`;
- `BODY-BUILD CATEGORY` when visible.

Reject a view if it looks like a different attractive person of the same archetype.

Common failure cases:

- younger / older face drift;
- narrower / broader face redesign;
- different nose or jaw;
- changed hairline;
- distinctive feature disappears / changes;
- template-beauty replacement;
- profile that cannot geometrically correspond to the front view.

Rejected views must not enter the partner reference pool.

---

# 7. Validated Model Choice for Reference Assets

## image 2.5 — CURRENT PREFERRED IDENTITY-ASSET MODEL

Real tests on the selected P1 partner showed stronger cross-angle identity consistency than Banana2 Pro for front / 45-degree / profile / close-up identity completion.

Use image 2.5 for partner canonical reference assets when identity stability is the priority.

Validated compensation:

- high definition;
- low noise;
- clean image;
- bright / neutral natural window light;
- avoid dark / grey / muddy rendering;
- preserve original face structure;
- preserve approved distinctive features;
- explicit anti-template / anti-rebeautification language;
- identity completion, not redesign.

A close-up retry improved both identity and tonal quality when the prompt explicitly framed the task as identity completion rather than beautification.

## Banana2 Pro — REALISM SUPPORT, NOT DEFAULT CANONICALIZER

Current P1 tests showed strong photographic skin / material realism but weaker cross-angle identity preservation, especially in close-up where the face was reinterpreted.

Do not mix Banana2 Pro-derived identity views into an image 2.5 canonical reference package when they disagree structurally.

Banana2 Pro remains useful as a realism / photographic-quality route, not the current default identity canonicalization route.

---

# 8. Reference Package Rule

Do not create a hybrid identity package from conflicting models.

Bad:

`image FRONT + Banana PROFILE + Banana CLOSE-UP`

Preferred:

one internally coherent, QC-passed package from the model that preserved the approved partner best.

For the current validated P1 case:

`image 2.5 package = preferred`

---

# 9. Downstream Couple / Video Use

When generating a couple image or video later:

`PERSON_A = USER_REFERENCE_PACKAGE`

`PERSON_B = PARTNER_REFERENCE_PACKAGE`

The two packages remain isolated.

Do not merge facial traits, swap features, or let the partner reference package overwrite the user identity.

Once a partner identity is locked, downstream prompts should reference the locked identity rather than recompile a new person from the archetype card.

---

# 10. Validation Scope

Validated in the current P1 case:

- an approved partner can be expanded into four identity views;
- image 2.5 preserved the selected partner more consistently than Banana2 Pro across the tested views;
- image 2.5 close-up quality improved with explicit anti-redesign + bright / clean compensation;
- conflicting model interpretations should not be mixed into one reference package.

Not yet claimed as universally validated:

- exact quantitative gain from four-view references in every downstream couple generation;
- long-session identity persistence;
- every archetype's four-view behavior.

Do not require expensive A/B testing for every partner. Use four-view reference construction when downstream complexity or identity risk justifies it, then validate by practical output quality.
