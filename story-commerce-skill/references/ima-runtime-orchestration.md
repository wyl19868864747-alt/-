# iMA Runtime Orchestration — Story Product Ad

Purpose: define the user-facing iMA interaction flow for this Skill. This file controls **when to ask, what the user sees, and when generation may begin**. It does not replace the creative DNA in `SKILL.md`, Product Truth, Styles, Hooks, Story, CTA, or Prompt modules.

Do not add platform-bug workarounds or generic continuation patches here.

## User Experience Voice

The flow should feel like a capable creative partner guiding one decision at a time — not a form, checklist, or system log.

Use plain, natural American English for all user-facing copy.

Rules:
- Acknowledge the user’s last choice briefly, then move directly to the next useful decision.
- Ask only one decision at a time.
- Do not expose internal terms such as `Product Truth Lock`, `Hook DNA`, `state`, `router`, `prompt compile`, or tool names.
- Do not narrate internal processing with filler such as “analyzing deeply,” “running the workflow,” or “processing step 4.”
- Keep card labels easy to scan. Put explanation in the description, not in long labels.
- When presenting creative recommendations, explain them in commercial language the user can judge quickly.
- Before generation, make it clear that nothing has started yet and that the user will review the final generation settings first.
- Do not show the final video prompt unless the user explicitly asks to inspect it.

## Runtime Principle

The user should only need to invoke this Skill and upload a product image at entry. All other choices are collected progressively through native iMA choice cards.

Core flow:

`Product Image → Style Choice → Duration Choice → Deep Product Analysis → 3 Selling Directions → Direction Choice → Hook / Story / CTA Design → Story Outline Review → Hidden Prompt Compile → Video Generation Confirmation → Generate → Deliver`

## State Map

`INPUT_PENDING → STYLE_PENDING → DURATION_PENDING → DIRECTION_PENDING → OUTLINE_REVIEW_PENDING → PROMPT_COMPILE_HIDDEN → GENERATION_REVIEW_PENDING → GENERATING → DELIVERED`

Only move forward when the current state has the required user choice.

---

## 1. Entry — Product Image Only

### User-visible welcome copy

**Upload a product image and we’ll build the ad from there.**

Optional shorter variant when the UI already makes the task obvious:

**Upload your product image to get started.**

At entry, do not ask for Style, duration, selling point, Hook, CTA, model, resolution, or prompt.

### Required input

- At least one usable product image.

### Runtime action

- Confirm that the uploaded asset can be used as the product reference.
- Perform only enough initial recognition to identify the task as a product ad and avoid irrelevant questions.
- Do **not** perform the full product lock yet; deep product analysis happens after Style and duration are confirmed.

### Transition copy

Use one short line before the Style card:

**Got it — I’ll build around this product. First, choose the visual style you want.**

Next state: `STYLE_PENDING`.

---

## 2. Style Choice Card

Show one native choice card immediately after the product image is accepted.

```yaml
question: What visual style do you want for this ad?
options:
  - id: ST01
    label: Native U.S. Social
    description: Natural phone-camera realism, real-life lighting, light handheld movement, native social-feed feel.
  - id: ST02
    label: Quiet Luxury
    description: Restrained, refined, spacious, material-focused premium advertising.
  - id: ST03
    label: High-Fashion Editorial
    description: Strong styling, sculpted light, bold framing, fashion-campaign energy.
  - id: ST04
    label: Hollywood Action
    description: Strong motion, spatial depth, directional light, high-energy action-film grammar.
  - id: ST05
    label: Surreal Creative
    description: A real photographic world disrupted by one clear impossible visual event.
  - id: ST06
    label: Futuristic Tech
    description: Precise, geometric, cool, advanced, structured technology aesthetics.
  - id: ST07
    label: 1970s Americana Film
    description: Warm film texture, period color, grain, glow, and authentic retro imaging.
  - id: ST08
    label: Y2K Pop
    description: Early-2000s digital-pop energy, hard flash, reflective materials, playful framing.
  - id: ST09
    label: Airy Japanese Lifestyle
    description: Clean, bright, quiet, natural lifestyle imagery with soft light and generous breathing room.
  - id: ST10
    label: Mediterranean Holiday
    description: Bright sun, relaxed openness, blue-white warmth, breezy lifestyle-ad atmosphere.
  - id: ST11
    label: American Western
    description: Rugged materials, strong sunlight, grounded weight, and open-space visual language.
  - id: ST12
    label: Film Noir
    description: High-contrast shadow, silhouette, reflection, mystery, and controlled dramatic tension.
  - id: STYLE_AUTO
    label: Choose for me
    description: Let the Skill pick the best-fit style for this product and ad goal.
selection_mode: single
allow_freeform: false
```

The 12 actual Styles remain ST01–ST12. `STYLE_AUTO` is a utility choice, not a thirteenth Style.

If the user chooses a Style, record that exact `style_id` and load only that Style DNA.

If the user chooses `STYLE_AUTO`, defer final Style selection until deep product analysis, then choose one Primary Style using product truth, likely audience, strongest Proof opportunity, desired perception, and generation stability.

### Transition copy after a Style is selected

**Style set. Now choose how much story you want to give it.**

If `STYLE_AUTO` is selected:

**I’ll choose the best-fit style for the product. Now choose the video length.**

Next state: `DURATION_PENDING`.

---

## 3. Duration Choice Card

Show one native choice card after Style preference is confirmed.

```yaml
question: How long should the ad be?
options:
  - id: D15
    label: 15 seconds
    description: Faster and tighter — one Hook, one main selling point, one clear Proof, one CTA.
  - id: D30
    label: 30 seconds
    description: More room for story, product persuasion, objection handling, and a stronger payoff.
selection_mode: single
allow_freeform: false
```

Record `duration = 15s` or `30s` exactly as selected.

Do not ask for aspect ratio, resolution, audio, model, or quantity here.

### Transition copy

**Got it. I’ll use the product, style, and timing to find the strongest way to sell it.**

Next state: `DIRECTION_PENDING`.

---

## 4. Deep Product Analysis + Three Selling Directions

After Style preference and duration are confirmed, perform the full Product Truth Lock using `references/product-truth-lock.md`.

Deep-lock the product from available evidence, including:

- product identity / SKU / variant when established
- silhouette, geometry, scale cues, proportions
- color, finish, gloss level, reflectivity
- visible material and texture cues
- transparent / translucent / matte / metallic / soft-touch behavior when visible
- logo, label, readable text, typography, packaging layout
- components, accessories, ports, pumps, lids, hinges, seams, buttons, interfaces
- open / closed / sealed / assembled / active physical state
- real contact and operation surfaces
- price / offer / service / claim facts only when supported
- visual elements that must remain unchanged during generation

Keep `CONFIRMED`, `VISIBLE`, `SUPPORTED_INFERENCE`, and `UNKNOWN` separate. Never turn a visual guess into a commercial fact.

If `STYLE_AUTO` was selected, resolve one Primary Style now before creating the three directions.

Then combine:

`Product Truth + resolved Style DNA + duration + likely audience/job + strongest available Proof`

and propose exactly **three clearly different selling directions**.

### User-visible intro

Use:

**Here are three directions I’d recommend for this product. Each one sells it from a different angle:**

### User-visible direction format

Keep each direction concise, concrete, and easy to compare. Do not output the final video prompt.

**A — [Short Direction Name]**  
**Lead with:** [the product value or selling point]  
**Why it works:** [why this direction fits this product + Style]  
**Show it by:** [one concise visual / Proof approach]

**B — [Short Direction Name]**  
**Lead with:** [...]  
**Why it works:** [...]  
**Show it by:** [...]

**C — [Short Direction Name]**  
**Lead with:** [...]  
**Why it works:** [...]  
**Show it by:** [...]

Avoid generic phrases such as “highlight quality,” “show premium feeling,” or “focus on the product.” Each direction must make a visibly different commercial choice.

Immediately after the text, show one native choice card.

The card labels should mirror the generated direction names when possible so the user does not have to remember what A/B/C meant.

```yaml
question: Which direction should we build the ad around?
options:
  - id: direction_a
    label: A — [generated direction name]
    description: Build the ad around Direction A shown above.
  - id: direction_b
    label: B — [generated direction name]
    description: Build the ad around Direction B shown above.
  - id: direction_c
    label: C — [generated direction name]
    description: Build the ad around Direction C shown above.
  - id: direction_manual
    label: I have my own angle
    description: Tell me the selling point or direction you want to emphasize instead.
selection_mode: single
allow_freeform: true
```

If the user provides their own selling point or direction, treat that text as the active direction and continue with it. Do not force A/B/C afterward.

### Transition copy after direction selection

For A/B/C:

**Good choice — I’ll build the story around this direction.**

For manual input:

**Got it — I’ll use your angle as the core of the ad.**

Next state: `OUTLINE_REVIEW_PENDING` after the chosen direction has been compiled into the story plan.

---

## 5. Hook + Story + Selling-Point Expression

Use the confirmed inputs:

- product image and deep Product Truth Lock
- resolved Style DNA
- selected duration
- selected/manual selling direction

Then resolve internally:

- Commercial Core
- one primary Hook DNA
- product-entry mechanism
- Proof / selling-point expression
- Story Architecture
- reversal only when useful
- one CTA DNA
- location, cast, performance, staging, camera, light, and sound direction

Do not expose this internal module selection to the user unless asked.

### 30-second default commercial arc

For `30s`, preserve this persuasion sequence unless product truth or Style makes a specific beat invalid:

`High-salience incident Hook → product enters as the causal solution → product value build → skepticism / challenge → answer through Proof → belief shift → purchase intent → CTA`

The opening incident should be calibrated to the resolved Style. A strange or absurd event should still feel native to that Style rather than forcing every ad into slapstick comedy.

### 15-second default commercial arc

For `15s`, keep only the highest-value chain:

`Immediate Hook → product causal entry → one selling-point Proof → reaction / decision shift → CTA`

Do not compress a 30-second script by simply speaking faster. Remove secondary objections, side stories, extra claims, and unnecessary beats.

---

## 6. Story Outline + Approval Loop

After the creative plan is complete, show the user a concise story outline in normal text.

### User-visible intro

Use:

**Here’s the story plan before I generate anything:**

### Required outline format

**Title:** [short ad / segment name]  
**Duration:** [15s / 30s]  
**Style:** [resolved Style name]  
**Mood:** [one concise sentence]  
**Visual Keywords:** [3–6 concrete keywords]  
**Cast:** [who appears and their role]  
**Setting:** [specific story location]  
**What happens:** [fast, readable summary from opening to ending]  
**Hook:** [what happens first and why it earns attention]  
**Product Moment:** [how the product enters and changes the situation]  
**Selling Point / Proof:** [what the audience understands and how it is demonstrated]  
**CTA:** [the final viewer action]

The outline must be short enough to scan and detailed enough that the user can picture the whole ad. Avoid production jargon that does not help the user judge the idea.

Then show one native choice card:

```yaml
question: Does this story direction work for you?
options:
  - id: outline_approve
    label: Looks good — continue
    description: Keep this story and prepare the final video-generation settings.
  - id: outline_revise
    label: I want to change something
    description: Change the story, Hook, selling point, characters, setting, tone, or CTA before generation.
selection_mode: single
allow_freeform: false
```

### Revision branch

If `outline_revise` is selected, show a freeform-enabled native question card:

```yaml
question: What would you like to change? You can give a specific edit or describe a different direction.
options:
  - id: submit_revision
    label: Submit my changes
    description: Apply what I write and rebuild the story outline.
selection_mode: single
allow_freeform: true
```

After revision text is received:

`Re-analyze → rebuild the complete outline → show the revised outline → show the same approval card again`

Do not show only the changed lines; show the full revised outline so the user can judge the complete film again.

Repeat until `outline_approve` is selected.

---

## 7. Hidden Prompt Compile + Video Generation Confirmation

After outline approval, use one short transition line:

**The story is set. I’ll prepare the final video settings for you to review before anything is generated.**

Then:

1. Compile the final video-generation prompt using the Skill’s Prompt Compiler and the confirmed Product / Style / Hook / Story / CTA modules.
2. Keep the prompt body hidden from the normal user-facing conversation unless the user explicitly asks to inspect it.
3. Query the currently available video models and use the platform-default or recommended **compatible** model that supports the confirmed reference-image input, duration, aspect ratio, resolution preference, and audio requirements. Do not invent a model id.
4. Submit one video-generation request with:
   - the uploaded product image included as a real source asset
   - the current runtime’s supported reference-image-to-video category
   - `duration`: previously confirmed `15s` or `30s`
   - `aspect_ratio`: `9:16`
   - `resolution`: prefer `720p` when supported by the compatible model
   - `audio`: ON
   - `count`: `1`
   - `prompt`: hidden final compiled prompt
5. Submission should trigger the native iMA video-generation confirmation card.
6. Stop the current round and let the user review/edit the generation card and click **Generate**.
7. Do not claim generation has started before the user confirms that card.

If the platform-default model cannot satisfy the confirmed duration or reference-image requirement, choose the current compatible recommended/default model without reopening the creative flow.

If no compatible model supports `720p`, use the compatible model’s supported default resolution and expose that real value on the confirmation card rather than inventing support.

If no compatible model exists for the confirmed duration + product reference, report the platform capability blocker instead of silently changing the duration or dropping the product reference.

Next state after confirmation: `GENERATING`.

---

## 8. Generate, Deliver, End

After the user confirms the native video-generation card:

- Generate the video with the confirmed card parameters.
- Preserve the product reference and all confirmed commercial facts.
- Deliver the generated video result to the user.
- Do not reopen creative parameter questions after successful delivery.

### User-visible delivery copy

Keep the delivery simple:

**Your video is ready.**

The generated video itself is the primary result; do not bury it under a long recap.

Final state: `DELIVERED`.

The runtime task ends only after the generated result is presented to the user.
