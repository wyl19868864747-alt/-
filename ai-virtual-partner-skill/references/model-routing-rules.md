# Model Routing Rules｜模型路由规则

## Purpose

Choose the image model by product goal, then apply model-specific compensation. Model testing serves three purposes in order:

1. select the model best suited to the Skill's target result;
2. test whether prompt compensation can reduce the chosen model's weaknesses;
3. accumulate reusable model experience for future tasks.

Do not treat model benchmarking as an end in itself.

---

# Default Route｜VALIDATED

## Route A — Dream / Hero

**Model:** image 2.5

Use when priority is:

- highest partner attractiveness
- heart-flutter / fantasy value
- hero / cover image
- strong romantic tension
- "unknown best partner" feeling

Recommended default moment:

`Soft Almost-Kiss`

Secondary:

`Close Eye Contact`

Mandatory compensation:

- high definition
- low noise
- clean image
- brighter / airy natural exposure
- avoid dark / grey / muddy grading
- preserve real skin texture
- anti-template identity controls

Known residual limitation:

- even after compensation, some outputs retain a grey / cement-like tonal character and weaker real-camera skin texture.

Current decision:

`DEFAULT IMAGE MODEL = image 2.5`

Reason: the first product impression prioritizes a high-attractiveness, sweet, aspirational best-partner fantasy.

---

## Route B — Real / Candid

**Model:** Banana2 Pro

Use when priority is:

- believable real-photo feel
- candid relationship moment
- low generation noise
- natural heritage appearance
- everyday intimacy

Recommended default moment:

`Close Eye Contact`

Secondary:

`Soft Almost-Kiss`

Mandatory compensation:

- explicitly preserve high partner attractiveness
- relationship action must be visible
- sweetness / affection must be concrete, not abstract
- real skin microtexture, not beauty-filter smoothness
- protected highlights
- low-contrast natural tone
- avoid HDR / overexposed skin

Known limitation:

- can be visually conservative / ordinary;
- can over-smooth skin;
- stronger realism texture prompts may coincide with excessive highlight / contrast response in current runs.

Current decision:

`SECONDARY REALISM MODEL = Banana2 Pro`

---

# Routing Logic

```text
IF first-impression / hero / fantasy priority
→ image 2.5

IF realism / candid-photo priority
→ Banana2 Pro

IF user explicitly requests one model
→ honor user model choice + apply that model adapter
```

Do not compile the same prompt unchanged across the two models.

---

# Model Evaluation Dimensions

When comparing future models, evaluate:

1. partner attractiveness
2. identity preservation
3. couple sweetness
4. romantic chemistry
5. skin / camera realism
6. tonal quality / exposure
7. archetype controllability
8. prompt-compensation effectiveness

Model selection must be based on the product target, not only on technical image cleanliness.
