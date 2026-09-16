# Partner Archetype Visual Benchmark

## Status

`DOCUMENTED FROM REAL USER GENERATIONS`

This benchmark validates whether attraction archetypes remain visibly distinct under controlled portrait conditions and whether `HERITAGE_APPEARANCE` can vary independently from `ARCHETYPE_ID`.

The benchmark does not prove universal attractiveness. It tests generation readability, realism, and controllability in the current production workflow.

---

## Controlled Test Design

Fixed variables included:

- adult subjects
- similar visual age bands
- chest-up / half-body portrait framing
- eye-level camera
- neutral background
- simple clothing
- natural window-like light
- realistic portrait perspective

Primary variables:

1. same heritage appearance, different archetypes;
2. same archetype, different heritage appearances;
3. soft vs strong / dominant extremes.

Primary evaluation criteria:

- archetype readability
- attractiveness
- photorealism
- heritage naturalness
- non-template identity
- structural expression beyond clothing / styling

---

# Male Results

## CORE VALIDATED

### M01 Soft Refined

Result: readable and distinct.

Observed:

- image 2.5 produced stronger idealized attractiveness;
- Banana2 Pro produced stronger realism but more conservative attractiveness.

### M02 Clean Masculine

Result: readable and usable as control archetype.

Observed:

- visibly separated from M01 but remains intentionally closer than Power Masculine;
- image 2.5 pushes more strongly toward aspirational attractiveness.

### M04 Power Masculine

Result: strong pass.

Observed:

- body strength and broader masculine structure were readable;
- Banana2 Pro preserved realism particularly well;
- image 2.5 produced stronger idealized attractiveness.

### M05 Mature Dominant

Result: strong pass.

Observed:

- mature / controlled / authoritative read remained stable;
- archetype survived heritage-appearance changes.

---

# Heritage Independence Test

Fixed archetype: `M05 Mature Dominant`.

Tested appearance directions:

- East Asian
- European
- African / African-diaspora
- South Asian

Result: pass.

Key observation:

- Banana2 Pro showed especially strong naturalness and avoided obvious `same face + changed skin color` behavior.
- image 2.5 maintained high attractiveness but showed more shared idealized facial aesthetics across outputs.

Validation rule:

`HERITAGE_APPEARANCE` and `ARCHETYPE_ID` must remain independent controls.

---

# Female Results

## F01 Soft Feminine

Result: pass.

- image 2.5 produced a high-attractiveness warm / approachable result.
- Banana2 Pro remained realistic but more conservative.

## F02 Elegant Feminine

Result: partial model-dependent pass.

- image 2.5: clear refined / elegant differentiation and high attractiveness.
- Banana2 Pro: realism remained strong, but repeated outputs under-expressed aspirational elegance and leaned too plain / everyday.

Adaptation implication:

Banana2 Pro needs concrete visible elegance cues rather than abstract `elegant / high-end` wording alone.

## F05 Dominant Beauty

Result: pass.

- image 2.5 produced strong visual presence and high attractiveness.
- Banana2 Pro produced readable dominance with stronger realism but lower aspirational attractiveness.

Important:

Dominance must be expressed through structure, posture, controlled expression, and presence—not anger or masculinization.

## F08 Glamorous Bombshell

Result: model-dependent.

- Banana2 Pro: pass; mature sensuality, glamour, curves, and realism were readable.
- image 2.5: repeated generation failures in the current runtime/platform. Mark `IMAGE_2_5_COMPATIBILITY_UNVERIFIED`.

Do not infer from this failure that the archetype itself is invalid.

---

# Candidate Archetypes Not Yet Sufficiently Tested

Male:

- M03 Athletic Sunlit
- M06 Rugged Masculine
- M07 Cold Elegant
- M08 Androgynous Beauty

Female:

- F03 Athletic Beauty
- F04 Mature Seductive
- F06 Cold Beauty
- F07 Warm Natural

These remain useful structural candidates but must not be presented as runtime-validated until direct benchmark evidence exists.

---

# Model Behavior Learned From This Benchmark

## image 2.5

Observed strengths:

- stronger attractiveness prior
- stronger fantasy / aspirational partner feel
- strong archetype readability

Observed risks:

- more visible noise / micro-grain than Banana2 Pro
- template-beauty convergence, especially across female outputs
- over-beautification can reduce structural diversity

## Banana2 Pro

Observed strengths:

- low visible noise
- strong photorealism
- natural heritage-appearance variation
- realistic skin and portrait cleanliness

Observed risks:

- conservative attractiveness prior
- abstract elegance / dominance language may be under-expressed
- may generate believable ordinary people instead of aspirational partner targets unless visible attractiveness cues are specified

---

# Current Validation Decision

Promote to `CORE VALIDATED`:

Male:

- M01 Soft Refined
- M02 Clean Masculine
- M04 Power Masculine
- M05 Mature Dominant

Female:

- F01 Soft Feminine
- F02 Elegant Feminine — with model adaptation note
- F05 Dominant Beauty
- F08 Glamorous Bombshell — Banana2 Pro validated; image 2.5 compatibility unverified

Keep all other archetypes as `CANDIDATE`.

---

# Regression Requirements

Any future change to archetype definitions or model adaptation should re-test at least:

1. M01 vs M04 — soft vs power masculine;
2. F01 vs F05 — soft vs dominant feminine;
3. M05 across at least two heritage appearance settings;
4. F02 on Banana2 Pro;
5. one anti-template test on image 2.5.

Record the model/version and runtime because generation behavior may change over time.
