# Matching Engine｜伴侣匹配规则

## Purpose

Recommend visually convincing adult partner candidates for the locked user identity without pretending to predict a soulmate.

The engine optimizes **couple coherence + user preference + attraction fantasy**, not a fake compatibility percentage.

---

## Evidence Classes

- `[E] Evidence-backed`: supported by relationship / attraction research.
- `[EI] Evidence-informed`: useful research signal, but context-dependent.
- `[C] Creative Heuristic`: product rule validated through generation testing rather than universal science.

---

## Hard Rules

1. `USER_HARD_PREFERENCE` overrides system preference priors.
2. Do not output fake precision such as `98% soulmate`.
3. Do not clone the user's facial features into the partner.
4. Do not treat actual geometric facial similarity as a linear attractiveness score.
5. Do not lower partner attractiveness just to force a "matching level" with the user.
6. Preserve age coherence and presentation parity unless the user explicitly requests contrast.
7. Same-sex matching must not inherit heterosexual gender-role assumptions.

---

## Matching Architecture

```text
USER_IDENTITY_CARD
+
USER_PREFERENCE_CARD
+
PARTNER_ARCHETYPE_LIBRARY
↓
HARD CONSTRAINT GATE
↓
COUPLE COHERENCE LAYER
↓
MATCH MODE ROUTER
↓
PARTNER CANDIDATES
```

### Hard Constraint Gate

Resolve explicit user choices first:

- partner gender presentation
- heritage appearance direction
- adult visual-age range
- body preference
- masculinity / femininity preference
- archetype preference

### Couple Coherence Layer

Use only as soft controls:

- `VISUAL_AGE_COHERENCE`
- `AURA_COHERENCE`
- `PRESENTATION_PARITY`
- `MODERATE_FACIAL_HARMONY`
- `ATTRACTIVENESS / GROOMING PARITY`

`MODERATE_FACIAL_HARMONY` means compatible overall facial rhythm, softness/sharpness and refinement level. It does **not** mean copying eyes, nose, lips or chin.

---

# Validated Match Modes

## H1 — Harmony Match｜VALIDATED

Goal: strongest natural couple-likeness.

Prioritize:

- similar visual-age band
- similar grooming / refinement level
- compatible warmth and social aura
- moderate facial rhythm harmony
- controlled masculine / feminine differentiation

Generation benchmark result:

- repeatedly read as the most natural / stable couple mode;
- did not require facial cloning;
- excessive facial similarity is unnecessary and should be avoided.

Use when the user has no strong explicit archetype preference.

---

## P1 — Preference Match｜VALIDATED

Goal: satisfy the user's stated attraction preference while keeping the couple visually coherent.

Prioritize:

`USER PREFERENCE > COUPLE COHERENCE PRIOR`

The validated test used a `Mature Dominant` partner against a softer refined user identity and produced a convincing couple while preserving the requested attraction type.

Use when the user explicitly selects partner type / body / aura / appearance direction.

---

## C1 — Complementary Contrast｜VALIDATED WITH LIMITS

Goal: increase fantasy and chemistry by intentionally contrasting selected dimensions.

Validated example:

`Soft / refined user × Power Masculine partner`

Keep stable:

- visual-age plausibility
- grooming level
- social-world coherence
- overall attractiveness / presentation level

Allow contrast in:

- body strength
- visual masculinity / femininity
- softness vs physical power
- restrained dominance vs warmth

Risk flags:

- `BODYGUARD_CLIENT`
- `TRAINER_CLIENT`
- `PARENT_CHILD_AGE_GAP`
- `OVERPOWERED_USER`

Contrast must stop before the relationship reads as a different social role.

---

## Prompt Isolation Rule｜VALIDATED

Matching rationale is **internal logic**, not visible-scene content.

Pipeline:

```text
MATCHING ENGINE
↓
MATCH_CANDIDATE_CARD
↓
VISIBLE SUBJECT FILTER
↓
MODEL ADAPTER
↓
FINAL PROMPT
```

If the task is `PARTNER_SOLO_PORTRAIT`, do not include the user's appearance or couple rationale in the final image prompt. Real tests showed that mentioning the intended partner relationship can cause the image model to render both people.

---

## Candidate Identity Separation｜VALIDATED

Different candidates must be distinct identities, not one idealized face with different body / styling.

For each candidate, lock at least:

- face shape tendency
- eye / brow character
- nose structure tendency
- jaw structure
- hair structure
- body build
- social aura

This is especially important for image 2.5, which showed convergence toward a shared idealized attractive male face across multiple candidate types.

---

## Status

`Harmony Match`, `Preference Match`, and `Complementary Contrast` are generation-validated routing modes in the current benchmark.

They are **not** scientific claims that one mode is objectively best for every person.
