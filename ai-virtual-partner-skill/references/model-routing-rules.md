# Model Routing Rules｜模型路由规则

## Purpose

Choose the model by the production asset being created. Model testing serves three purposes in order:

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
- approved first frame for later MiniMax H3 video

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

## Route C — Approved Couple 10s Video｜CURRENT VIDEO DEFAULT

**Model:** MiniMax H3

Use after the user approves the couple image.

Input priority:

`APPROVED_COUPLE_IMAGE + USER_REFERENCE_PACKAGE + PARTNER_REFERENCE_PACKAGE`

Current production requirement:

- 10-second interaction;
- at least 3 readable relationship beats by default;
- purposeful shot / framing variation instead of stretching one micro-action;
- normally ~2 natural cuts / angle changes when supported;
- preserve first-frame scene / wardrobe / color continuity;
- maintain both identities through close interaction.

Current H3 route is newly selected and awaits one representative production validation. Do not launch a large H3 benchmark series.

Seedance 2.5 is no longer the current production route; retain its prior results only as historical timing / tension evidence.

---

# Runtime Routing Logic

```text
IF creating / exploring the partner identity
→ image 2.5 when high-attraction archetype clarity / canonical identity coverage is needed

IF creating the final user-facing romantic couple image
→ Banana2 Pro by current production default

IF user approves couple image and requests video
→ MiniMax H3, 10 seconds, approved image as first-frame visual truth

IF user explicitly requests a specific model
→ honor the user model choice + apply that model adapter
```

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
8. suitability as video first frame
9. 10-second identity / anatomy stability
10. shot / cut controllability

Stop model comparison once the production routing is operationally clear.
