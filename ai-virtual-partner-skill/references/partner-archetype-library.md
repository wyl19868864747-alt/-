# Partner Archetype Library｜虚拟伴侣外貌原型库

## Purpose

Provide a compact, generation-oriented library of adult partner appearance archetypes for the AI Virtual Partner Skill.

This library does **not** rank ethnic or heritage groups by attractiveness. `HERITAGE_APPEARANCE` and `ARCHETYPE_ID` are independent controls.

A partner profile is composed as:

`ADULT AGE BAND + GENDER PRESENTATION + HERITAGE_APPEARANCE + ARCHETYPE_ID + BODY / FACE PARAMETERS + STYLE AURA + MODEL ADAPTATION`

Never reduce a heritage group to one fixed face template.

---

## Evidence Labels

Use three evidence classes:

- `[E] Evidence-backed`: supported by relatively stable attractiveness research or cross-cultural findings.
- `[EI] Evidence-informed`: supported by some research signal, but context, culture, observer preference, or effect size limits universality.
- `[C] Creative Heuristic`: product / casting / fashion / photographic archetype used to create readable fantasy types; not a scientific claim about who is more attractive.

Hard rules:

- Do not use a universal `golden ratio = beautiful` rule.
- Do not encode `lighter/darker skin = more attractive`.
- Do not encode `one heritage = one beauty standard`.
- Do not encode `more masculine = always more attractive` or `thinner = always more attractive`.
- Prefer healthy natural skin, coherent facial structure, age-consistent vitality, and controlled distinctiveness over synthetic perfection.

---

## Global Base

The following are shared priors, not a single perfect-face formula:

- facial prototypicality / structural coherence: useful baseline `[E]`
- healthy natural skin appearance: useful baseline `[E]`
- natural asymmetry is allowed; perfect symmetry is not required `[E/EI]`
- female facial femininity can be a useful parameter `[E]`
- male facial masculinity is preference- and context-sensitive `[EI]`
- body strength / athleticism can influence male attractiveness, but must remain parameterized `[EI]`
- body fullness / waist definition / curvature may influence female attractiveness, but must remain parameterized and non-numeric `[EI]`
- visual age must be preserved as an intentional parameter; do not auto-youngify adults `[E/C]`

---

# Male Archetypes

## CORE VALIDATED

### M01 — Soft Refined

Purpose: gentle, polished, attractive adult male with lower visual masculinity and high refinement.

Core fields:

- `face_prototypicality: high` `[E]`
- `masculinity_level: low-moderate` `[EI]`
- `face_structure: soft / balanced` `[C]`
- `jaw: clean, moderate definition` `[C]`
- `body_build: lean` `[C]`
- `skin_health: high, natural texture` `[E]`
- `style_aura: refined / gentle / composed` `[C]`

Validation note: visually separated from Clean Masculine and Power Masculine in image 2.5 and Banana2 Pro testing.

### M02 — Clean Masculine

Purpose: balanced, modern, broadly usable high-attractiveness male baseline.

Core fields:

- `face_prototypicality: high` `[E]`
- `masculinity_level: moderate` `[EI]`
- `jaw: clearly defined, non-extreme` `[C]`
- `body_build: lean-athletic` `[EI]`
- `skin_health: high` `[E]`
- `style_aura: clean / stable / modern masculine` `[C]`

Validation note: functions as the control archetype for male comparison.

### M04 — Power Masculine

Purpose: physically powerful, highly masculine adult male without bodybuilder exaggeration.

Core fields:

- `face_prototypicality: medium-high` `[E]`
- `masculinity_level: high` `[EI]`
- `face_structure: broader / more angular` `[C]`
- `jaw: strong, non-cartoonish` `[C]`
- `body_build: muscular-athletic` `[EI]`
- `body_strength_signal: high` `[EI]`
- `shoulder_width: visually broad` `[EI]`
- `style_aura: forceful / sensual / controlled` `[C]`

Validation note: strong archetype readability in both tested image models.

### M05 — Mature Dominant

Purpose: mature, controlled, authoritative adult male.

Core fields:

- `visual_age: mature adult band` `[C]`
- `face_prototypicality: medium-high` `[E]`
- `masculinity_level: moderate-high` `[EI]`
- `jaw: defined` `[C]`
- `body_build: athletic / solid` `[EI]`
- `skin: age-natural and healthy` `[E/C]`
- `style_aura: composed / authoritative / restrained` `[C]`

Validation note: archetype remained readable across East Asian, European, African / African-diaspora, and South Asian appearance tests. Heritage independence was strongest in Banana2 Pro.

## CANDIDATE

### M03 — Athletic Sunlit

- `masculinity_level: moderate` `[EI]`
- `body_build: athletic` `[EI]`
- `body_strength_signal: moderate-high` `[EI]`
- `style_aura: healthy / open / energetic` `[C]`

### M06 — Rugged Masculine

- `masculinity_level: high` `[EI]`
- `face_structure: angular / textured` `[C]`
- `facial_hair: natural stubble or short beard` `[C]`
- `skin_texture: clearly natural` `[E]`
- `body_build: solid / athletic` `[EI]`
- `style_aura: rugged / grounded / raw` `[C]`

### M07 — Cold Elegant

- `masculinity_level: moderate` `[EI]`
- `face_structure: lean / refined` `[C]`
- `body_build: lean` `[C]`
- `style_aura: restrained / elegant / distant` `[C]`

### M08 — Androgynous Beauty

- `face_prototypicality: high` `[E]`
- `masculinity_level: low` `[EI]`
- `facial_softness: high` `[C]`
- `body_build: lean` `[C]`
- `facial_hair: none / minimal` `[C]`
- `style_aura: delicate / artistic / refined` `[C]`

Must remain clearly adult.

---

# Female Archetypes

## CORE VALIDATED

### F01 — Soft Feminine

Purpose: warm, approachable, high-femininity adult woman.

Core fields:

- `face_prototypicality: high` `[E]`
- `femininity_level: high` `[E]`
- `face_structure: soft / balanced` `[C]`
- `facial_contrast: moderate` `[E]`
- `skin_health: high` `[E]`
- `style_aura: gentle / warm / romantic` `[C]`

Validation note: clear and stable in image 2.5; natural but more conservative in Banana2 Pro.

### F02 — Elegant Feminine

Purpose: refined, composed, attractive adult woman with restrained elegance.

Core fields:

- `face_prototypicality: high` `[E]`
- `femininity_level: moderate-high` `[E]`
- `face_structure: refined / balanced` `[C]`
- `facial_contrast: moderate` `[E]`
- `body_build: lean-natural` `[C]`
- `style_aura: elegant / composed / sophisticated` `[C]`

Validation note: strong in image 2.5. Banana2 Pro preserved realism but repeatedly under-expressed high-attractiveness / sophistication, so model adaptation is required.

### F05 — Dominant Beauty

Purpose: clearly feminine adult woman with strong presence, control, and assertiveness.

Core fields:

- `face_prototypicality: medium-high` `[E]`
- `femininity_level: moderate-high` `[E]`
- `face_structure: slightly more angular / controlled` `[C]`
- `body_build: lean / athletic` `[EI]`
- `style_aura: assertive / controlled / powerful` `[C]`

Validation note: archetype became clearly readable in both tested image models. Dominance must come from structure, posture, and social signal rather than anger or masculinization.

### F08 — Glamorous Bombshell

Purpose: mature, glamorous, strongly feminine adult woman with overt sensual confidence.

Core fields:

- `face_prototypicality: medium-high` `[E]`
- `femininity_level: high` `[E]`
- `facial_contrast: high` `[E/C]`
- `body_fullness: moderate` `[EI]`
- `waist_definition: visible, non-numeric` `[EI]`
- `body_curvature: higher, realistic` `[EI]`
- `style_aura: glamorous / confident / sensual` `[C]`

Validation note: validated in Banana2 Pro with strong realism and mature sensuality. Repeated image 2.5 generation failure was observed in the current runtime; treat image 2.5 compatibility for this archetype as unverified, not as evidence that the archetype is invalid.

## CANDIDATE

### F03 — Athletic Beauty

- `femininity_level: moderate-high` `[E]`
- `body_build: athletic feminine` `[EI]`
- `body_strength_signal: moderate` `[EI]`
- `style_aura: healthy / active / confident` `[C]`

### F04 — Mature Seductive

- `visual_age: mature adult band` `[C]`
- `femininity_level: high` `[E]`
- `facial_contrast: moderate-high` `[E/C]`
- `skin: age-natural and healthy` `[E]`
- `style_aura: mature / sensual / composed` `[C]`

### F06 — Cold Beauty

- `face_prototypicality: medium-high` `[E]`
- `femininity_level: high` `[E]`
- `face_structure: refined` `[C]`
- `style_aura: distant / controlled / editorial` `[C]`

### F07 — Warm Natural

- `face_prototypicality: high` `[E]`
- `femininity_level: moderate-high` `[E]`
- `facial_contrast: low-moderate` `[E]`
- `skin_health: natural high` `[E]`
- `style_aura: approachable / authentic / intimate` `[C]`

Use `Warm Natural`, not age-ambiguous labels such as `girl-next-door`, in system-facing fields.

---

# Heritage Appearance

`HERITAGE_APPEARANCE` is an independent user-selected or explicitly requested visual direction. It must not imply attractiveness rank or personality.

Candidate appearance families may include:

- East Asian appearance
- Southeast Asian appearance
- South Asian appearance
- European appearance
- African / African-diaspora appearance
- Middle Eastern / Mediterranean appearance
- Latino / mixed-heritage appearance
- multi-ethnic appearance

Rules:

1. Do not infer a user's real ethnicity or nationality from appearance.
2. For generated partners, use the user's explicit selection or requested visual direction.
3. Preserve natural facial morphology and skin tone diversity; never implement heritage as `same template face + changed skin color`.
4. The same archetype must remain recognizable across multiple heritage appearance settings.

---

# PARTNER_APPEARANCE_CARD

Use the following structure downstream. Not every field must be sent to the image model; many fields are internal control / QC fields.

```text
PARTNER_APPEARANCE_CARD

adult_age_band
gender_presentation
heritage_appearance
skin_tone
skin_undertone
archetype_id

face_prototypicality
face_shape
facial_adiposity
eye_shape
eye_size
eye_spacing
brow_shape
brow_density
nose_structure
lip_structure
jaw_structure
chin_structure
femininity_level
masculinity_level
facial_contrast

hair_color
hair_texture
hair_length
facial_hair

body_build
body_strength_signal
body_fullness
shoulder_width
waist_definition
hip_fullness

visual_age
skin_health
skin_texture

distinctive_feature_01
distinctive_feature_02
style_aura
```

Prompt compile should normally keep only the fields that materially change the target model's output.

---

# Status

`CORE VALIDATED` means the archetype achieved readable separation in the current benchmark evidence. It does not mean universal attractiveness is scientifically proven.

`CANDIDATE` means structurally useful but not yet sufficiently benchmarked in the current runtime.
