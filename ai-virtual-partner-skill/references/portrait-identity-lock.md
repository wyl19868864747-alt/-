# Portrait Identity Lock｜用户人像锁定规则

## Purpose

Lock the uploaded user's visual identity before any styling, partner generation, couple pose, scene change, or image-to-video step.

The goal is not to beautify the person. The goal is to preserve the same identity across angle, lighting, wardrobe, pose, scene, and motion changes.

Core rule:

`IDENTITY FIRST`

If a styling choice conflicts with identity fidelity, identity wins.

---

## 1. Input Quality Gate

Prefer, in order:

`clear front view > clear 45-degree view > clear profile > full body > other references`

Useful identity evidence should have:

- visible facial features
- limited occlusion
- limited beauty-filter distortion
- normal perspective
- sufficient face resolution
- no extreme expression when avoidable

If multiple images are provided, do not average all images blindly. Extract the repeated stable structure and down-weight transient photo conditions.

### Multi-image conflict priority

`unfiltered > heavily filtered`

`normal perspective > wide-angle selfie distortion`

`neutral expression > extreme expression`

`unoccluded > occluded`

`clear > blurry`

---

## 2. Identity vs Photo Condition

Always separate:

`IDENTITY_TRAIT`

from:

`PHOTO_CONDITION`

### Identity traits

Stable features such as:

- face shape
- eye shape and spacing
- brow-eye relationship
- nose structure
- lip structure
- cheekbone structure
- jaw and chin structure
- hairline
- stable skin tone range
- stable body proportions when visible
- persistent distinctive marks

### Photo conditions

Do not encode as permanent identity:

- temporary expression
- makeup level
- lighting direction
- exposure
- wide-angle distortion
- beauty filter
- head tilt
- temporary hairstyle styling
- occlusion

Do not infer race, ethnicity, nationality, or cultural identity from appearance. If such a category is needed by a later module, use explicit user selection rather than automatic identity inference.

---

## 3. USER_IDENTITY_CARD

Create one structured identity card and reuse it downstream. Do not let each module independently reinterpret the person.

### Basic visual state

Record when supported:

- `VISUAL_AGE_RANGE`
- `SKIN_TONE_RANGE`
- `BODY_BUILD`
- `SHOULDER_WIDTH`
- `HEAD_BODY_RATIO`

If evidence is insufficient, use `UNKNOWN` rather than inventing a value.

### Face geometry

Record:

- `FACE_SHAPE`
- `FACE_LENGTH_WIDTH_RATIO`
- `FOREHEAD_WIDTH`
- `CHEEKBONE_WIDTH`
- `CHEEKBONE_PROMINENCE`
- `JAW_WIDTH`
- `JAW_ANGLE`
- `CHIN_SHAPE`
- `NATURAL_ASYMMETRY`

### Eyes and brows

Record:

- `EYE_SHAPE`
- `EYE_SIZE`
- `EYE_SPACING`
- `EYE_TILT`
- `EYELID_TYPE`
- `BROW_SHAPE`
- `BROW_THICKNESS`
- `BROW_EYE_DISTANCE`

### Nose

Record:

- `NOSE_LENGTH`
- `NOSE_BRIDGE_HEIGHT`
- `NOSE_BRIDGE_WIDTH`
- `NOSE_TIP_SHAPE`
- `NOSE_TIP_PROJECTION`
- `ALA_WIDTH`

### Mouth

Record:

- `MOUTH_WIDTH`
- `UPPER_LIP_SHAPE`
- `LOWER_LIP_SHAPE`
- `UPPER_LOWER_LIP_RATIO`
- `CUPID_BOW`
- `MOUTH_CORNER_DIRECTION`
- `PHILTRUM_LENGTH`

### Skin and distinctive marks

Record:

- `BASE_SKIN_TONE`
- `SKIN_UNDERTONE` when visually supportable
- `SKIN_TEXTURE`
- `FRECKLES`
- `MOLES`
- `SCARS`
- `BIRTHMARKS`
- `OTHER_DISTINCTIVE_MARKS`

### Hair

Record:

- `HAIRLINE_SHAPE`
- `HAIRLINE_HEIGHT`
- `HAIR_COLOR`
- `HAIR_TEXTURE`
- `HAIR_DENSITY`
- `BASE_HAIRSTYLE`
- `FACIAL_HAIR` when relevant

### Body identity

Only when supported by the source image(s), record:

- `BODY_BUILD`
- `SHOULDER_WIDTH`
- `NECK_PROPORTION`
- `TORSO_PROPORTION`
- `WAIST_PROPORTION`
- `HIP_PROPORTION`
- `ARM_BUILD`
- `LEG_BUILD`
- `HEAD_BODY_RATIO`

Never silently replace an unknown body with an idealized model body.

---

## 4. Confidence Tags

Every uncertain field may carry:

`HIGH / MEDIUM / LOW`

Examples:

- clear front-facing eye shape: `HIGH`
- nose profile inferred from front view only: `LOW`
- body build from a headshot: `LOW` or `UNKNOWN`

Low-confidence fields must not be treated as hard facts.

---

## 5. Lock Levels

Use four levels.

### L3 — ABSOLUTE LOCK

Identity-defining structure. Do not redesign:

- face shape
- eye spacing
- eye shape
- nose structure
- lip structure
- cheekbones
- jaw
- chin
- visual age range
- stable skin tone
- strong distinctive marks

### L2 — STRONG LOCK

Preserve strongly:

- hairline
- base hair color
- body proportions
- shoulder width
- head-body ratio
- hair texture

### L1 — SOFT LOCK

May vary within identity-safe bounds:

- hairstyle arrangement
- makeup
- beard length
- facial expression
- temporary skin sheen
- loose hair strands

### L0 — FREE VARIABLE

May change without redefining identity:

- wardrobe
- accessories
- environment
- pose
- camera
- lighting
- scene styling

L0 changes must never trigger L3/L2 reconstruction.

---

## 6. CANONICAL_IDENTITY

Build a neutral internal identity baseline from the available evidence.

Canonical state should represent:

- neutral or relaxed expression
- normal head pose
- normal perspective
- no extreme beauty filter
- no exaggerated makeup reinterpretation
- natural skin texture
- stable visual age
- stable facial proportions

Downstream modules must reuse this identity baseline rather than reconstructing the user's face from scratch each time.

---

## 7. Four-View Identity Reference

For complex downstream work, build either an internal virtual four-view model or a rendered reference sheet.

Recommended views:

1. `FRONT`
2. `THREE_QUARTER_45`
3. `PROFILE`
4. `CLOSE_UP`

### Purpose by view

`FRONT` locks overall proportions, eye spacing, face width, nose width, mouth width, and jaw width.

`THREE_QUARTER_45` locks cheekbone volume, nose projection, eye depth, jaw turn, and facial depth.

`PROFILE` locks forehead curve, nose root/bridge/tip, lips, chin, and jaw profile.

`CLOSE_UP` locks skin texture, brows, eye details, lip details, hairline, and distinctive marks.

### Shared invariants

All four views must represent:

- same person
- same age
- same stable skin tone
- same hairline
- same base hairstyle
- same bone structure
- same distinctive marks where geometrically visible

Only view angle should materially change.

### Virtual vs rendered sheet

`VIRTUAL_REFERENCE_SHEET` may be used for lower-complexity single-image tasks.

`RENDERED_REFERENCE_SHEET` is preferred for:

- repeated multi-scene generation
- large angle changes
- couple images
- close physical interaction
- image-to-video generation
- camera orbit / turn-head motion

A rendered reference sheet is AI-derived and therefore never outranks the original user image.

---

## 8. Reference Authority

Fixed order:

`ORIGINAL_USER_IMAGE > USER_IDENTITY_CARD > CANONICAL_IDENTITY > CORE_REFERENCE_SHEET > APPROVED_REFERENCE > TEXT_DESCRIPTION`

Rules:

- text cannot override image identity;
- an AI-generated reference cannot redefine the original user;
- “beautiful”, “handsome”, “sexy”, “glamorous”, “model-like”, or similar styling words may change presentation, not anatomy;
- do not auto-slim the face, enlarge eyes, redesign nose, enlarge lips, alter jaw, alter stable skin tone, or auto-youngen the person.

Optimize photography, not identity.

---

## 9. Reference Pool

Keep a small, high-quality reference pool.

Recommended:

- original user reference
- canonical identity
- one core four-view sheet when needed
- up to 1–3 high-quality approved generated references

Do not accumulate large numbers of inconsistent generations.

A new generated image can enter the pool only if:

1. identity is stable;
2. it contributes a useful new angle or body view;
3. it passes Identity QC;
4. it does not conflict with the original image.

---

## 10. Identity QC

Every generated image that may become a reference must be checked before reuse.

### Weighted score

- `Face Identity`: 30
- `Facial Geometry`: 20
- `Age Consistency`: 10
- `Skin Identity`: 10
- `Hair / Hairline`: 10
- `Body Identity`: 10
- `Distinctive Features`: 10

Total: `100`

### PASS

`TOTAL >= 85`

and

`Face Identity >= 22`

and

`Facial Geometry >= 15`

May become `APPROVED_REFERENCE`.

### CONDITIONAL

`TOTAL 75–84`

May be displayed if otherwise useful, but must not become a core identity reference.

### FAIL

`TOTAL < 75`

or either critical subscore falls below threshold.

Mark as:

`IDENTITY_DRIFT`

and do not propagate it.

### Critical failure regardless of score

Reject immediately if there is:

- obvious face replacement
- major face-shape reconstruction
- strong nose/lip/jaw redesign
- major age shift
- major stable skin-tone shift
- head/body identity mismatch
- user/partner face swap
- facial fusion between two people

---

## 11. Drift Recovery

Never continue generating from a drifted reference.

Use:

`IDENTITY_DRIFT → DISCARD_DRIFTED_REFERENCE → RETURN_TO_ORIGINAL → LOAD_CANONICAL_IDENTITY → LOAD_BEST_APPROVED_REFERENCE_IF_NEEDED → REGENERATE → QC`

Do not recursively repair a wrong identity through repeated edits. That compounds drift.

For classified failures, two-person contamination, reference-pool contamination, or video/cut identity failures, read:

- `references/identity-failure-recovery.md`

The recovery library owns failure classification and the smallest safe repair route. This file remains the authority for USER identity definition and lock levels.

---

## 12. Double-Person Isolation

When the partner module is added, identity slots must be separate:

`PERSON_A = USER`

`PERSON_B = PARTNER`

The user may inherit only user identity anchors. The partner may inherit only partner identity anchors.

Shared styling, scene, mood, lighting, or photographic chemistry may coordinate the pair, but face identity may never be blended.

If slot contamination, face swap, or face fusion is detected, do not improvise a blended repair. Route to `identity-failure-recovery.md` and rebind the two authority sources separately.

---

## 13. Image-to-Video Carryover

When video is added later, the user's video identity must inherit from:

`USER_IDENTITY_CARD + CANONICAL_IDENTITY + CORE_REFERENCE_SHEET + FINAL_APPROVED_IMAGE`

Video may vary:

- expression
- gaze
- breathing
- small head/body motion
- hair motion
- clothing motion
- environment
- camera motion

Video must not redesign:

- face shape
- eyes
- nose
- mouth
- age
- stable skin tone
- hairline
- body identity

Higher motion and larger head rotation increase drift risk and therefore require stronger reference coverage.

If video identity drifts, preserve the approved first-frame state and route recovery through `references/identity-failure-recovery.md` rather than promoting later drifted frames as new identity evidence.

---

## 14. Final Hard Rules

1. `IDENTITY FIRST`.
2. Image identity evidence outranks text styling.
3. Stable anatomy must be separated from transient photo conditions.
4. Scene, outfit, pose, camera, and light changes cannot rebuild identity.
5. AI-derived references can support but never overwrite the original identity.
6. Two-person identities must remain isolated.
7. Drifted outputs cannot be reused as references.
8. Only QC-passed outputs can be promoted.
9. Four-view references exist to complete identity geometry, not to beautify or redesign the user.
10. If evidence is missing, mark it unknown; do not invent identity details.
11. Classified identity failures route to `identity-failure-recovery.md`; recover only the failed identity variable whenever possible.
