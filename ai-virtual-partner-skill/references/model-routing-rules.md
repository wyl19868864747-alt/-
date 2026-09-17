# Model Routing Rules｜模型路由规则

## Purpose

Choose the image model by the production asset being created. Model testing serves three purposes in order:

1. select the model best suited to the Skill's actual production target;
2. test whether prompt compensation can reduce that model's weaknesses;
3. accumulate reusable model experience for future tasks.

Do not treat model benchmarking as an end in itself.

---

# Current Production Routing

## Route A — User-Facing Couple Image｜CURRENT DELIVERY DEFAULT

**Model:** Banana2 Pro

Use for the final user-facing couple image when priority is:

- believable real-photo feel
- candid relationship moment
- visible real skin / material texture
- natural heritage appearance
- sweet / flirtatious captured intimacy
- approved first frame for later Seedance 2.5 video

Current compensation may include:

- high-attractiveness adult couple
- visible real skin pores
- fine skin microtexture
- slight natural imperfections
- realistic photography
- non-posed relationship moment
- image not overexposed
- avoid a milky / foggy white veil when observed
- clear, transparent rendering

Do not over-stack tonal controls when they flatten the image.

Known risks:

- can be visually conservative unless attraction / relationship action is made concrete;
- can over-smooth skin;
- some outputs can become too bright or acquire a white hazy veil;
- close-up identity canonicalization was weaker than image 2.5 in the current P1 test.

Current decision:

`DEFAULT USER-FACING COUPLE IMAGE MODEL = Banana2 Pro`

---

## Route B — Partner Exploration / Canonical Identity Asset

**Model:** image 2.5

Use when priority is:

- high-attraction partner exploration
- archetype differentiation
- aspirational partner / Hero alternatives
- canonical partner reference-sheet construction
- recovering stronger partner beauty when Banana2 Pro becomes too ordinary

Validated compensation:

- high definition
- low noise
- clean image
- brighter / airy natural exposure
- avoid dark / grey / muddy grading
- preserve real skin texture
- explicit anti-template / anti-rebeautification language
- identity completion, not redesign

Known residual limitation:

- some outputs retain grey / cement-like tonal character;
- real-camera skin microtexture can remain weaker than Banana2 Pro;
- attractive candidates may collapse toward a shared idealized template unless identity separation is explicit.

Current decision:

`DEFAULT PARTNER CANONICAL-ASSET MODEL = image 2.5`

---

# Runtime Routing Logic

```text
IF creating / exploring the partner identity
→ image 2.5 when high-attraction archetype clarity / canonical identity coverage is needed

IF creating the final user-facing romantic couple image
→ Banana2 Pro by current production default

IF user explicitly requests a specific model
→ honor the user model choice + apply that model adapter
```

The user-facing approved couple image may be generated with another model when product evidence later changes this routing decision.

Never compile the same prompt unchanged across models.

---

# Model Evaluation Dimensions

When a genuinely new routing decision is needed, evaluate only what can change that decision:

1. partner attractiveness
2. identity preservation
3. couple sweetness / chemistry
4. skin / camera realism
5. tonal quality / exposure
6. action / scene controllability
7. prompt-compensation effectiveness
8. suitability as Seedance first frame

Stop model comparison once the production routing is operationally clear.
