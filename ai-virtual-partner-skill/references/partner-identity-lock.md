# Partner Identity Lock｜虚拟伴侣身份锁定

## Purpose

Turn an approved partner candidate into a reusable visual identity for later couple images and video. This module preserves the chosen partner; it must not redesign or re-cast the partner.

---

## 1. Identity Source

Start from an approved partner reference that has already passed archetype / matching review.

Create:

`PARTNER_IDENTITY_CARD`

with:

- adult age band
- heritage appearance
- face shape / facial proportions
- brow / eye / nose / lip structure
- jaw / chin
- hairline / base hairstyle
- skin tone / skin state
- body build / shoulder width
- stable aura / style signal

Do not infer new identity traits simply to make the partner more attractive.

---

## 2. Lock Levels

### HARD IDENTITY ANCHORS

Do not change:

- face shape / head proportions
- eye shape / spacing
- nose structure
- lip proportions
- jaw / chin structure
- age appearance
- core hairline
- core facial identity

### STRONG LOCKS

Keep highly stable:

- skin tone
- brow structure
- hair color / base cut
- body-build category
- shoulder-width category
- overall mature / soft / dominant visual identity

### SOFT LOCKS

May change slightly:

- expression
- minor hair styling
- grooming state
- small skin-state changes
- subtle posture

### FREE VARIABLES

May change:

- clothing
- environment
- pose
- camera
- lighting
- moment type

Free variables must not trigger identity rebuilding.

---

## 3. Partner Reference Package

For identity-critical downstream work, build a partner reference package:

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

### Four-view rules

All views must preserve:

- same person
- same age
- same hairline
- same facial geometry
- same skin / heritage appearance
- same base hairstyle

Do not use the four-view process to beautify, sharpen, feminize / masculinize, age-shift or redesign the partner.

---

## 4. Reference Priority

Partner authority order:

`ORIGINAL_APPROVED_PARTNER > PARTNER_IDENTITY_CARD > APPROVED_REFERENCE_PACKAGE > APPROVED_COUPLE_FRAME > TEXT DESCRIPTION`

AI-generated views strengthen angle coverage but may not overwrite the original approved identity.

---

## 5. Reference Sheet QC

Check each generated view for:

- `SAME PERSON`
- `FACIAL GEOMETRY`
- `VISUAL AGE`
- `HAIRLINE`
- `SKIN / HERITAGE APPEARANCE`
- `DISTINCTIVE FEATURES`

Reject a view if it looks like a different attractive person of the same type.

Common failure cases:

- younger / older face drift
- narrower / broader face redesign
- different nose or jaw
- changed hairline
- template-beauty replacement
- profile that cannot geometrically correspond to the front view

Rejected views must not enter the partner reference pool.

---

## 6. Validated Model Choice for Reference Assets

### image 2.5 — CURRENT PREFERRED IDENTITY-ASSET MODEL

Real tests on the selected P1 partner showed stronger cross-angle identity consistency than Banana2 Pro for front / 45-degree / profile / close-up identity completion.

Use image 2.5 for partner canonical reference assets when identity stability is the priority.

Validated compensation:

- high definition
- low noise
- clean image
- bright / neutral natural window light
- avoid dark / grey / muddy rendering
- preserve original face structure
- explicit anti-template / anti-rebeautification language

A close-up retry improved both identity and tonal quality when the prompt explicitly said the task was identity completion rather than beautification.

### Banana2 Pro — REALISM SUPPORT, NOT DEFAULT CANONICALIZER

Current P1 tests showed strong photographic skin / material realism but weaker cross-angle identity preservation, especially in close-up where the face was reinterpreted.

Do not mix Banana2 Pro-derived identity views into an image 2.5 canonical reference package when they disagree structurally.

Banana2 Pro remains useful as a realism / photographic-quality reference route, not the current default identity canonicalization route.

---

## 7. Reference Package Rule

Do not create a hybrid identity package from conflicting models.

Bad:

`image FRONT + Banana PROFILE + Banana CLOSE-UP`

Preferred:

one internally coherent, QC-passed package from the model that preserved identity best.

For the current validated P1 case:

`image 2.5 package = preferred`

---

## 8. Downstream Couple / Video Use

When generating a couple image or video later:

`PERSON_A = USER_REFERENCE_PACKAGE`

`PERSON_B = PARTNER_REFERENCE_PACKAGE`

The two packages remain isolated.

Do not merge facial traits, swap features, or let the partner reference package overwrite the user identity.

---

## 9. Validation Scope

Validated in the current P1 case:

- an approved partner can be expanded into four identity views;
- image 2.5 preserved the selected partner more consistently than Banana2 Pro across the tested views;
- image 2.5 close-up quality improved with explicit anti-redesign + bright / clean compensation;
- conflicting model interpretations should not be mixed into one reference package.

Not yet claimed as universally validated:

- exact quantitative gain from four-view references in every downstream couple generation;
- long-session identity persistence;
- Seedance 2.5 video identity continuity.

Do not require expensive A/B testing for every partner. Use four-view reference construction when downstream complexity or identity risk justifies it, then validate by practical output quality.