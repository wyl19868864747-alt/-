# Sensuality Intensity Layer｜视觉亲密尺度控制层

## Purpose

Control **how visibly sensual / bold an adult couple image or video feels** without confusing sensuality with relationship temperature, identity, nudity, or explicit sexual activity.

This module exists because:

`RELATIONSHIP TEMPERATURE ≠ VISUAL INTIMACY SCALE`

A scene can be Romantic but visually conservative, or Sweet but physically close. The Skill therefore needs a separate production axis for how much skin, body proximity, contact placement, wardrobe exposure, gaze intensity and framing are visible.

Runtime:

`RELATIONSHIP TEMPERATURE + VISUAL_INTIMACY_LEVEL + MOMENT + ACTION + SCENE + IDENTITIES + TARGET MODEL → SENSUALITY PAYLOAD → RELATIONSHIP COMBINATION ROUTER → IMAGE / VIDEO PROMPT`

All people are adults.

This layer stays **non-explicit**. It may create attractive, flirtatious, sensual, bold adult imagery, but it does not route explicit sexual activity or exposed intimate anatomy.

---

# 1. Responsibility Boundary

This file owns:

- visual intimacy level;
- skin-exposure intensity;
- wardrobe cut / body-reveal level;
- body-distance intensity;
- allowed contact-zone escalation;
- sensual gaze / expression intensity;
- camera proximity appropriate to the intimacy level;
- non-explicit upper boundary;
- risk reduction when sensuality conflicts with identity / anatomy stability.

It does **not** own:

- partner selection → `matching-engine.md`;
- identity → identity lock modules;
- base body action geometry → `relation-action-library.md`;
- relationship time-state → `moment-type-library.md`;
- expression mechanics → `expression-gaze-library.md`;
- scene selection → `scene-tension-library.md`;
- color assignment → `color-wardrobe-library.md`.

Core separation:

`RELATIONSHIP TEMPERATURE = WHAT THEY FEEL`

`VISUAL_INTIMACY_LEVEL = HOW BOLDLY THE IMAGE SHOWS IT`

---

# 2. VISUAL_INTIMACY_LEVEL

Use one of five levels.

## V0 — NATURAL / CONSERVATIVE

Frontend alias: `自然克制`

Use when the user wants believable everyday couple imagery with low sensual emphasis.

Visible cues:

- normal date / lifestyle wardrobe;
- shoulder / hand / upper-back contact;
- comfortable personal distance;
- restrained smile or soft gaze;
- medium two-shot / medium-close;
- no deliberate emphasis on body exposure.

Default compatible actions:

A02 / A03 / A04 / A09 / A14 / A15 / A17.

---

## V1 — FLIRTY

Frontend alias: `暧昧`

Visible cues:

- fitted but everyday clothing;
- open collar / off-shoulder / fitted knit / sleeveless styling when scene-appropriate;
- waist / upper-back contact;
- smaller body gap;
- direct partner gaze, gaze break → return;
- one initiator + one visible response;
- medium-close 3/4 framing.

Default compatible actions:

A01 / A05 / A06 / A10 / A11 / A13 / A14.

---

## V2 — SENSUAL｜DEFAULT RECOMMENDED

Frontend alias: `性感`

This remains a moderate sensual level, but it is no longer the default for the current fantasy AI-partner product.

Visible cues:

- body-skimming / fitted wardrobe;
- visibly open neck / shoulder / upper-back / leg line where physically plausible;
- low-back / backless / slit / fitted silhouettes may be used;
- one partner's hand may rest at waist / rear waist / lower waist / upper hip;
- body contact may extend from upper torso to waist while both identities remain distinct;
- focused attraction, eye→lip→eye used briefly, or short gaze break followed by return;
- slightly parted relaxed lips are allowed when natural;
- medium-close / 3/4 couple framing that keeps both faces readable.

Preferred actions:

A01 + T03 / A05 / A06 / A07 / A10 / A11 / A18 when safe.

Preferred Moments:

M02 / M03 / M10 / M12 / M11.

Rule:

`SENSUALITY COMES FROM VISIBLE GEOMETRY + WARDROBE + GAZE, NOT FROM THE WORD "SEXY".`

---

## V3 — BOLD SENSUAL

Frontend alias: `大胆性感`

Use when the user explicitly wants a stronger adult fantasy look.

Visible cues:

- more deliberate skin reveal while intimate areas remain covered;
- backless or low-back evening wear;
- deep but covered neckline;
- high-slit skirt / fitted dress / fitted bodysuit / open shirt styling;
- swimwear when the physical scene supports it;
- lower waist / upper-hip contact;
- close torso alignment with slight offset rather than flat body collision;
- seated side-perch or environment-supported closeness only when anatomy is stable;
- stronger focused gaze / anticipation / short eye→lip→eye;
- camera may move tighter, but avoid extreme close-up when face proximity is already high.

Preferred actions:

A01 + T03 / A07 / A18 / carefully staged A19 / A14 close seated variant.

Preferred scenes:

S05 / S12 / S13 / S04 / S19 / S16 when wardrobe physically fits the environment.

Guard:

Do not stack low light + extreme close-up + face-side hand + near-contact + complex seated limbs in one shot.

---

## V4 — MAXIMUM NON-EXPLICIT

Frontend alias: `最大非露骨尺度`

This is the upper production ceiling for this Skill.

Goal:

Create the strongest adult sensual read possible **without explicit sex or exposed intimate anatomy**.

Allowed visible direction:

- lingerie-inspired fashion, non-transparent bodysuit, swimwear or similarly revealing but covering wardrobe when contextually plausible;
- exposed shoulders / back / side torso / legs;
- close body-to-body positioning;
- waist / lower-waist / upper-hip / outer-thigh-side contact;
- near-kiss / cheek / temple / neck-side proximity without forcing identity-damaging contact;
- seated / reclining adult couple poses only when anatomy remains clear;
- direct mutual attraction and clearly reciprocal adult agency.

Hard ceiling:

- intimate areas remain covered;
- no explicit sexual activity;
- no genital / breast contact as the relationship action;
- no coercive restraint;
- no juvenile presentation;
- no identity sacrifice for more contact.

If V4 conflicts with identity stability, anatomy or model capability:

`IDENTITY + ANATOMY + MUTUAL AGENCY > INTENSITY`

Reduce only the smallest risky variable while preserving the requested boldness elsewhere.

---

# 3. Default Routing Policy

If the user explicitly selects a level:

`EXPLICIT VISUAL_INTIMACY_LEVEL > SYSTEM DEFAULT`

If the user does not select a level:

- Sweet → V1 by default;
- Romantic → V2 by default;
- Flirty → V2 by default;
- Passionate → V3 by default;
- Playful → V1–V2 depending Action;
- Protective → V0–V1 by default.

Product-level recommendation:

For the AI Virtual Partner experience, the current product default is:

`V3 — 大胆性感`

when the user has not explicitly selected a lower visual-intimacy level. Use V2 only when the user chooses a more restrained sensual route. Use V4 only when the user explicitly requests the strongest non-explicit result.

Do not auto-escalate a user's explicit lower choice.

---

# 4. Sensuality Compile Axes

The Router should compile sensuality from **multiple visible axes**, not one adjective.

## 4.1 Wardrobe Exposure

Ordinal:

- `W0 EVERYDAY`
- `W1 FITTED / OPEN`
- `W2 REVEALING FASHION`
- `W3 BOLD NON-EXPLICIT`

Examples:

W1:
- fitted knit;
- sleeveless top;
- open collar;
- off-shoulder styling.

W2:
- backless / low-back dress;
- high-slit skirt;
- fitted evening dress;
- open shirt over covered torso;
- fitted bodysuit;
- scene-appropriate swimwear.

W3:
- lingerie-inspired fashion with intimate areas fully covered;
- non-transparent fitted bodysuit;
- bold swimwear;
- highly open-back / side-cut fashion that remains non-explicit.

This layer owns **coverage / cut**, not palette. Color still comes from `color-wardrobe-library.md`.

## 4.2 Body Distance

- `D0 COMFORTABLE`
- `D1 CLOSE`
- `D2 BODY-CONTACT`
- `D3 BREATH-CLOSE / UNRESOLVED`

Do not force complete facial contact to increase sensuality.

## 4.3 Contact Zone

Progressive zones:

- shoulder / upper arm;
- upper back / shoulder blade;
- waist / rear waist;
- lower waist / upper hip;
- outer thigh-side above knee when composition is clear.

Avoid escalating into explicit intimate-body contact.

## 4.4 Gaze / Expression

Increase sensuality through:

- sustained partner-directed gaze;
- brief eye→lip→eye;
- look away → return;
- restrained half-smile;
- focused attraction;
- anticipation;
- short post-contact softening.

Do not use:

- exaggerated lip bite as a default;
- cartoon seduction;
- simultaneous identical “sexy face” from both adults.

## 4.5 Camera

Higher intimacy may use:

- medium-close 3/4;
- side close two-shot;
- profile-separated close framing;
- short push-in for video.

Avoid:

- extreme close-up when two faces are already nearly touching;
- framing that crops away the body contact point needed to read the relationship;
- low-angle sexualization that destroys identity / anatomy clarity.

---

# 5. Sensuality Upgrade Rule

When feedback is:

`太保守 / 不够性感 / 尺度不够 / 不够暧昧 / 想更大胆`

Do **not** immediately replace Partner or Scene.

Upgrade in this order:

1. `VISUAL_INTIMACY_LEVEL +1`;
2. increase wardrobe exposure one step where scene-compatible;
3. reduce body distance;
4. move contact from shoulder → waist / lower waist / upper hip;
5. strengthen gaze / anticipation;
6. tighten framing slightly;
7. only then consider changing Action / Scene.

Keep identities unchanged.

This is a **minimum reroute**, not a full restart.

---

# 6. Sensuality Downgrade Rule

When feedback is:

`太性感 / 太暧昧 / 太大胆`

Keep identities and scene when possible.

Reduce:

1. contact zone;
2. body distance;
3. wardrobe exposure;
4. gaze intensity;
5. Action intensity only if needed.

Do not replace Partner by default.

---

# 7. Anatomy / Identity Risk Guard

Sensuality risk accumulates.

High-risk stack example:

`V3/V4 + low-light scene + face-side hand + near-contact + extreme close-up + body overlap`

If risk becomes HIGH, remove **one** risk contributor first.

Preferred reductions:

- extreme close-up → medium-close;
- complete contact → small unresolved gap;
- face-side touch → waist / upper-back;
- full lap stacking → side-perch;
- severe torso twist → simple diagonal alignment;
- deep shadow → readable face light.

Do not simply downgrade the entire image to conservative styling.

---

# 8. Social Read / Mutual Agency

A bold sensual image must still read as a **mutual adult couple**.

Require:

- reciprocal gaze or touch;
- visible acceptance / response;
- neither adult appears trapped;
- open exit geometry in wall / window scenes;
- no bodyguard/client hierarchy;
- no passive mannequin partner.

`BOLD ≠ COERCIVE`

`PASSIONATE ≠ AGGRESSIVE`

---

# 9. Prompt Compile Payload

The final prompt should not output internal labels such as `V3`.

Compile only visible facts.

Example internal state:

`V3 + W2 + D3 + lower-waist contact`

Visible prompt payload:

`Person B keeps one hand low at Person A's waist while Person A rests one hand on B's shoulder; their torsos are close but slightly staggered, faces remain just apart, both hold focused partner-directed gaze. Person A wears a fitted low-back evening dress; Person B wears an open-collar fitted dark shirt. Medium-close 3/4 framing keeps both faces and waist contact clearly visible.`

Do not rely on:

`very sexy, bold, seductive, hot couple`

without the physical causes.

---

# 10. Still Image vs Video

## Still

A sensual still must immediately show:

- body distance;
- contact zone;
- wardrobe exposure;
- reciprocal gaze / reaction;
- both adult identities.

## Video

Sensuality should evolve rather than remain frozen.

Example:

`close waist hold → brief gaze break / reaction → hand shifts to upper back / lower waist → breath-close hold → slight release`

Do not spend 10 seconds maintaining one static “sexy look.”

---

# 11. UI Recommendation

Add a main-screen choice:

## 你希望画面有多大胆？

- `自然克制` → V0
- `暧昧` → V1
- `性感` → V2 — recommended default
- `大胆性感` → V3
- `最大非露骨尺度` → V4

This control should not be hidden inside Advanced settings if the product goal includes sensual fantasy.

---

# 12. Final Hard Rules

1. `RELATIONSHIP TEMPERATURE ≠ VISUAL_INTIMACY_LEVEL`.
2. Sensuality must be translated into visible wardrobe / distance / contact / gaze / framing.
3. Default AI-partner fantasy route should not silently collapse to conservative lifestyle imagery.
4. Explicit user intimacy choice overrides the default.
5. More sensuality does not require more completed facial contact.
6. Identity and anatomy stability outrank forcing stronger contact.
7. Both adults retain reciprocal agency.
8. Do not expose internal V-level codes in final prompts.
9. Color remains owned by `color-wardrobe-library.md`; this layer owns coverage/cut/intimacy.
10. Keep output non-explicit.


---

## Concept-image sensuality lock

For the current product direction, the visual target is not ordinary romantic lifestyle photography.

When user intent includes:
- 高级;
- 奢华;
- 性感;
- 荷尔蒙;
- 暧昧;
- 大尺度;

default to:
`V3 BOLD SENSUAL`

and pair with:
`VT3 FRAGRANCE-CAMPAIGN TENSION`

V3 must visibly compile through:
- at least one fitted / open / low-back / body-skimming wardrobe cue;
- smaller body distance;
- one meaningful waist / lower-waist / upper-hip / upper-back / collar contact;
- reciprocal partner-directed expression from both adults;
- tighter asymmetric framing.

If those visible causes are absent, the result has not actually reached V3 even if the prompt contains words such as `sensual`, `sexy`, or `bold`.
