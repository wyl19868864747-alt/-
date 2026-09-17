# Partner Identity Lock Benchmark

## Status

`DOCUMENTED FROM REAL USER GENERATIONS`

Test subject: approved P1 Mature Dominant adult East Asian male partner.

Models compared:

- image 2.5
- Banana2 Pro

Views generated:

- front
- 45-degree
- side profile
- face close-up

---

## image 2.5 Results

### Front
PASS.

- strong resemblance to original P1
- stable age / jaw / brow / hairline

### 45-degree
PASS.

- identity remained recognizable
- geometry remained consistent

### Side profile
PASS.

- profile nose / chin / jaw logic corresponded to the source identity

### Close-up V1
CONDITIONAL.

- still recognizable as P1
- slight younger / softer drift
- face became a little narrower / more beautified

### Close-up V2
PASS.

Prompt compensation explicitly required:

- identity completion, not redesign
- preserve original age / facial geometry
- no younger / slimmer / template-beauty reinterpretation
- bright neutral natural window light
- high definition / low noise / clean image
- no dark / grey / muddy rendering

Observed result:

- stronger identity match
- better light / tonal quality
- reduced grey / dull appearance
- usable real skin texture

Decision:

`PREFERRED PARTNER IDENTITY-ASSET MODEL = image 2.5`

for the current P1 workflow.

---

## Banana2 Pro Results

### Front
PARTIAL PASS.

- plausible same type / broadly recognizable
- face became somewhat longer / harder

### 45-degree
PARTIAL PASS.

- usable realism
- facial interpretation already began to drift from original P1

### Side profile
PARTIAL PASS.

- useful photographic quality
- nose / jaw volume became heavier than original reference

### Close-up
FAIL for canonical identity use.

Observed drift:

- changed eye character
- wider / heavier nose interpretation
- older / rougher age impression
- overall face read as same archetype rather than clearly the same individual

Decision:

Banana2 Pro is not the current default model for constructing canonical partner identity reference sheets.

It remains useful for photographic-realism validation.

---

## Key Distillation

1. `SAME ARCHETYPE` is not enough; partner reference views must read as `SAME PERSON`.
2. Identity reference packages should be internally coherent; do not mix structurally conflicting outputs from different models.
3. image 2.5's tendency to beautify / grey-render can be partially compensated by explicit anti-redesign + bright / clean instructions.
4. Banana2 Pro's stronger photographic realism does not automatically mean stronger identity canonicalization.
5. Do not spend repeated test cycles proving a small A/B gain when the practical identity asset already passes QC. Advance to the next module once the reference package is usable.

---

## Current Approved P1 Reference Package

`ORIGINAL P1`
+
`image 2.5 FRONT`
+
`image 2.5 45-DEGREE`
+
`image 2.5 PROFILE`
+
`image 2.5 CLOSE-UP V2`

Status:

`APPROVED FOR NEXT-STAGE TESTING`

---

## Not Yet Validated

- long-session persistence
- exact improvement percentage from using four-view vs single-view reference
- Seedance 2.5 video continuity
- all partner archetypes / heritage appearances

Do not overgeneralize this benchmark beyond the tested workflow without further evidence.