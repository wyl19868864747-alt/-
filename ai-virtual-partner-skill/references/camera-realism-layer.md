# Camera Realism Layer｜真实摄影质感规则

## Purpose

Create the feel of a real camera capturing real people. This layer is separate from subject cleanliness / generation noise.

Important distinction:

`GENERATION NOISE` ≠ `PHOTOGRAPHIC TEXTURE`

The goal is not dirty pixels or low-quality grain. The goal is subtle real-world image texture: natural skin microdetail, restrained tonal variation, optical softness and a believable camera capture feel.

---

## Reusable Realism DNA

Use selectively:

- visible but natural skin pores
- fine skin microtexture
- small tonal variation in skin
- minor real-world skin imperfections
- soft highlight roll-off
- gentle natural contrast
- slight optical softness rather than over-sharpening
- very subtle camera / film-like texture only when it improves realism
- natural hair flyaways and fabric texture
- physically believable window / ambient light

Avoid:

- plastic skin
- airbrushed beauty-filter skin
- waxy surface
- hyper-sharpened pores
- harsh local contrast
- clipped highlights
- overexposed skin
- HDR-like contrast
- synthetic cinematic grain used as decoration

---

# image 2.5 Compensation｜VALIDATED

Observed issue:

- attractive / romantic results can drift dark, grey, muddy or "cement-like";
- visible generation noise can be stronger than Banana2 Pro;
- skin may lack convincing real photographic microtexture.

Validated prompt compensation improved results:

- `high definition`
- `low noise`
- `clean image`
- `bright / airy natural window light`
- `not dark`
- `not grey / muddy`
- `avoid gloomy dark grading`
- `real skin texture / pores`
- `medium-telephoto close portrait photography`

Result:

- noise improved materially;
- brightness improved;
- residual grey / cement-like rendering remained and is treated as a current model tendency rather than a fully prompt-fixable issue.

Do not overfill prompts with lighting language. Subject identity and relationship moment remain primary.

---

# Banana2 Pro Compensation｜VALIDATED / PARTIAL

Observed baseline strengths:

- clean low-noise output
- strong real-photo feel
- strong skin cleanliness

Observed issue after realism prompting:

- skin can become too smooth / over-retouched;
- adding strong photographic texture language can coincide with higher contrast / overexposure in current runs;
- highlights may become too bright and tonal separation too aggressive.

Therefore do **not** simply add more `film grain`, `sensor texture`, or contrast language.

Prefer:

- `natural visible skin pores`
- `fine irregular skin microtexture`
- `no beauty filter`
- `no airbrushing`
- `soft low-contrast tonal curve`
- `protected skin highlights`
- `gentle highlight roll-off`
- `neutral / warm-neutral white balance`
- `no HDR contrast`
- `no clipped highlights`

Use camera texture sparingly. Realism should come primarily from skin, exposure, optical behavior and natural imperfections—not a heavy grain overlay.

---

## UGC Realism Reuse Rule

This module may reuse validated realism principles from the existing UGC scene/product-image workflow when relevant:

- real material texture
- restrained depth of field
- natural optical behavior
- minor imperfections
- believable exposure
- real-world mixed-light response

But person identity and couple chemistry remain higher priority than texture styling.
