# iMA Runtime Orchestration — Story Product Ad

Purpose: define the user-facing iMA interaction flow for this Skill. This file controls **when to ask, what to show, and when generation may begin**. It does not replace the creative DNA in `SKILL.md`, Styles, Hooks, CTA, Product Truth, Story, or Prompt modules.

Do not add platform-bug workarounds or generic continuation patches here.

## Runtime Principle

The user should only need to invoke this Skill and upload a product image at entry. All other required choices are collected progressively through native iMA choice cards.

Core runtime flow:

`Product Image → Style Choice → Duration Choice → Deep Product Lock → 3 Selling-Point Directions → Direction Choice → Story/Hook Design → Outline Review → Hidden Prompt Compile → Video Generation Confirmation → Generate → Deliver`

## State Map

`INPUT_PENDING → STYLE_PENDING → DURATION_PENDING → DIRECTION_PENDING → OUTLINE_REVIEW_PENDING → PROMPT_COMPILE_HIDDEN → GENERATION_REVIEW_PENDING → GENERATING → DELIVERED`

Only move forward when the current state's required user choice exists.

---

## 1. Entry — Product Image Only

### User-visible welcome copy

**Upload a product image to get started.**

The user should not be asked for Style, duration, selling point, Hook, CTA, model, resolution, or prompt at entry.

### Required input

- At least one usable product image.

### Runtime action

- Confirm that the uploaded asset is usable as a product reference.
- Perform only enough initial recognition to identify the task as a product ad and to avoid asking irrelevant questions.
- Do **not** perform the full Product Truth Lock yet; the deep lock happens after Style and duration are confirmed.

Next state: `STYLE_PENDING`.

---

## 2. Style Choice Card

Immediately after the product image is accepted, show one native choice card.

```yaml
question: Which visual style should this product ad use?
options:
  - id: ST01
    label: Native U.S. Mobile Social Realism
    description: Natural phone-camera realism, real-life light, light handheld movement, native social-feed feel.
  - id: ST02
    label: Quiet-Luxury Premium Advertising
    description: Restrained, refined, spacious, material-focused premium visual language.
  - id: ST03
    label: Western High-Fashion Editorial
    description: Strong styling, sculpted light, bold editorial framing, fashion-campaign energy.
  - id: ST04
    label: Hollywood Action Blockbuster
    description: Strong motion, spatial depth, directional light, high-energy cinematic action grammar.
  - id: ST05
    label: Surreal Creative Advertising
    description: A real photographic world disrupted by one clear impossible visual mechanism.
  - id: ST06
    label: Futuristic Sci-Fi Technology
    description: Precise, geometric, cool, advanced, structured technology aesthetics.
  - id: ST07
    label: 1970s American Film
    description: Warm Americana film texture, period color, grain, glow, authentic retro imaging.
  - id: ST08
    label: Y2K Pop
    description: Early-2000s digital-pop energy, hard flash, reflective materials, playful framing.
  - id: ST09
    label: Japanese Airy Lifestyle
    description: Clean, bright, quiet, natural, soft lifestyle realism with generous air and detail.
  - id: ST10
    label: Mediterranean Sun Holiday
    description: Bright sun, relaxed openness, blue-white warmth, breezy lifestyle-ad atmosphere.
  - id: ST11
    label: American Western Frontier
    description: Rugged materials, strong sunlight, grounded weight, open-space visual language.
  - id: ST12
    label: Film-Noir Dark Cinema
    description: High-contrast shadow, silhouette, reflection, mystery, controlled dramatic tension.
selection_mode: single
allow_freeform: false
```

After selection, record the exact `style_id` and load only that Style DNA.

Next state: `DURATION_PENDING`.

---

## 3. Duration Choice Card

Show one native choice card after Style is confirmed.

```yaml
question: How long should the final product story ad be?
options:
  - id: D15
    label: 15 seconds
    description: One fast Hook, one core selling point, one clear Proof, compact CTA.
  - id: D30
    label: 30 seconds
    description: More complete story escalation, product persuasion, objection handling, and CTA payoff.
selection_mode: single
allow_freeform: false
```

Record `duration = 15s` or `30s` exactly as selected.

Do not ask aspect ratio or resolution here. Default runtime output is `9:16`.

Next state: `DIRECTION_PENDING`.

---

## 4. Deep Product Lock + Three Selling-Point Directions

After Style and duration are confirmed, perform the full Product Truth Lock using `references/product-truth-lock.md`.

Deep-lock the product from the available evidence, including:

- product identity / SKU / variant when established
- silhouette, geometry, scale cues, proportions
- color, finish, gloss level, reflectivity
- visible material and texture cues
- transparent / translucent / matte / metallic / soft-touch behavior when visible
- logo, label, text, typography, packaging layout
- components, accessories, ports, pumps, lids, hinges, seams, buttons, interfaces
- open / closed / sealed / assembled / active physical state
- real contact and operation surfaces
- price / offer / service / claim facts only when supported
- visual elements that must remain unchanged during generation

Keep `CONFIRMED`, `VISIBLE`, `SUPPORTED_INFERENCE`, and `UNKNOWN` separate. Never turn a visual guess into a commercial fact.

Then combine:

`Product Truth + selected Style DNA + duration + likely audience/job + strongest available Proof`

and propose exactly **three differentiated selling-point directions**.

### User-visible direction format

Keep each direction concise and commercial. Do not output a video-generation prompt.

**A — [Direction Name]**  
Focus: [which product value or selling point to emphasize]  
Why it fits: [why this is strong for this product + selected Style]  
How to show it: [one concise visual/proof approach]

**B — [Direction Name]**  
Focus: [...]  
Why it fits: [...]  
How to show it: [...]

**C — [Direction Name]**  
Focus: [...]  
Why it fits: [...]  
How to show it: [...]

Immediately after the text, show one native choice card:

```yaml
question: Which selling-point direction should the ad build around?
options:
  - id: direction_a
    label: Direction A
    description: Use the full A direction shown above.
  - id: direction_b
    label: Direction B
    description: Use the full B direction shown above.
  - id: direction_c
    label: Direction C
    description: Use the full C direction shown above.
  - id: direction_manual
    label: None of these — I’ll provide the selling point
    description: Use my own selling-point direction instead.
selection_mode: single
allow_freeform: true
```

If the user types their own selling point, treat that text as the active selling-point direction and continue with it. Do not force A/B/C afterward.

Next state: `OUTLINE_REVIEW_PENDING` after the selected/manual direction has been compiled into the story plan.

---

## 5. Hook + Story + Selling-Point Expression

Use the confirmed inputs:

- product image and deep Product Truth Lock
- selected Style DNA
- selected duration
- selected/manual selling-point direction

Then resolve:

- Commercial Core
- primary Hook DNA
- product-entry mechanism
- Proof / selling-point expression
- Story Architecture
- reversal only when useful
- CTA DNA
- location, cast, performance, staging, camera, light, and sound direction

### 30-second default commercial arc

For `30s`, preserve this persuasion sequence unless the product truth or Style makes a specific beat invalid:

`Absurd / high-salience incident Hook → product enters as the causal solution → product value build → skepticism / challenge question → answer through Proof → belief shift → “where / how do I get it?” intent → CTA / order guidance`

The opening incident should be calibrated to the selected Style. “Absurd” means a highly readable, unusual commercial event; it does not require slapstick comedy when the selected Style is restrained.

### 15-second default commercial arc

For `15s`, keep only the highest-value chain:

`Immediate Hook → product causal entry → one selling-point Proof → reaction / decision shift → CTA`

Do not compress a 30-second script by simply speaking faster. Reduce story branches, objections, supporting claims, and secondary beats.

---

## 6. User-Visible Story Outline + Approval Loop

After creative analysis is complete, show a concise story outline in normal text. This is the user’s review object. Do **not** show the final video-generation prompt.

### Required outline format

**Title:** [short segment/ad name]  
**Duration:** [15s / 30s]  
**Style:** [selected Style name]  
**Atmosphere:** [one concise sentence]  
**Visual Keywords:** [3–6 concrete keywords]  
**Cast:** [who appears and their role]  
**Location:** [specific story location]  
**Story Flow:** [fast, readable summary of what happens from opening to ending]  
**Hook:** [what the viewer sees/hears first and why it creates attention]  
**Product Entry:** [how the product enters causally]  
**Selling Point / Proof:** [what is demonstrated and how]  
**CTA:** [the final viewer action]

The outline must be accurate, concise, and immediately understandable as a film plan. Avoid production jargon that does not help the user judge the story.

Then show one native choice card:

```yaml
question: Approve this story outline and continue to video generation?
options:
  - id: outline_approve
    label: Approve and continue
    description: Keep this story direction and prepare the final video-generation prompt.
  - id: outline_revise
    label: Revise the outline
    description: I want to change the story, selling-point emphasis, Hook, characters, scene, or CTA.
selection_mode: single
allow_freeform: false
```

### Revision branch

If `outline_revise` is selected, ask for revision input through a native freeform-enabled question card:

```yaml
question: What should be changed? You can describe specific edits or provide a new outline direction.
options:
  - id: submit_revision
    label: Submit revision notes
    description: Apply my written changes and rebuild the outline.
selection_mode: single
allow_freeform: true
```

After revision text is received:

`Re-analyze → rebuild outline → show full revised outline → show the same approval card again`

Repeat until `outline_approve` is selected.

---

## 7. Hidden Prompt Compile + Video Generation Confirmation

After outline approval:

1. Compile the final video-generation prompt using the Skill’s Prompt Compiler and the confirmed Style / Hook / Story / CTA modules.
2. Keep the prompt body hidden from the normal user-facing conversation unless the user explicitly asks to inspect it.
3. Query the currently available video models and use the platform-default or recommended **compatible** model that supports the confirmed reference-image input, duration, aspect ratio, resolution, and audio requirements. Do not invent a model id.
4. Submit one video-generation request with:
   - reference product image included as a real source asset
   - `category`: reference-image-to-video equivalent supported by the current runtime
   - `duration`: previously confirmed `15s` or `30s`
   - `aspect_ratio`: `9:16`
   - `resolution`: `720p`
   - `audio`: ON
   - `count`: `1`
   - `prompt`: hidden final compiled prompt
5. Submission should trigger the native iMA video-generation confirmation card.
6. Stop the current round and wait for the user to click **Generate** on that card.
7. Do not claim generation has started before the user confirms the generation card.

If the current platform default model is incompatible with the confirmed duration or reference input, choose the current compatible default/recommended model without asking another creative question. If no compatible model exists, report that platform capability blocker instead of silently changing the confirmed duration or dropping the product reference.

Next state after confirmation: `GENERATING`.

---

## 8. Generate, Deliver, End

After the user confirms the native video-generation card:

- Generate the video with the confirmed card parameters.
- Preserve the product reference and all confirmed commercial facts.
- Deliver the generated video result to the user.
- Do not reopen creative parameter questions after successful delivery.

Final state: `DELIVERED`.

The runtime task ends only after the generated result is presented to the user.
