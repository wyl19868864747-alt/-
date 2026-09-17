# Matching Engine｜伴侣匹配引擎

## Purpose

Choose **which adult partner route to generate** from the Partner Archetype Library using explicit user preference first, then safe visual-coherence rules.

The engine does **not** predict a soulmate, psychological compatibility, or real-world romantic outcome.

Core output:

`WHO TO GENERATE`

Not:

`HOW THE COUPLE SHOULD POSE`

Responsibility boundaries:

- partner design → `partner-archetype-library.md`
- matching / candidate selection → this file
- approved partner preservation → `partner-identity-lock.md`
- relationship action → `relation-action-library.md`
- relationship moment → `moment-type-library.md`
- expression / gaze → `expression-gaze-library.md`
- scene / color → downstream scene / color libraries

All generated partners are adults.

---

# 1. Runtime Architecture

```text
USER PHOTO
↓
USER IDENTITY LOCK
↓
USER_PREFERENCE_CARD
+
SAFE USER VISUAL FEATURES
+
PARTNER ARCHETYPE TAGS
↓
HARD CONSTRAINT GATE
↓
ARCHETYPE SHORTLIST
↓
MATCH MODE ROUTER
↓
COUPLE COHERENCE GATE
↓
CONTRAST / SOCIAL-ROLE RISK GUARD
↓
SELECT PARTNER ROUTE
↓
MATCH_CANDIDATE_CARD
↓
VISIBLE SUBJECT FILTER
↓
PARTNER_APPEARANCE_CARD
↓
GENERATE PARTNER CANDIDATE
↓
USER APPROVAL
↓
PARTNER IDENTITY LOCK
```

Once the partner is approved, **matching stops**. The approved generated person becomes the specific identity source.

---

# 2. USER_PREFERENCE_CARD

Most product-facing inputs should come from choice controls rather than mandatory free text.

```text
USER_PREFERENCE_CARD

partner_gender_preference:
  MEN | WOMEN | OPEN_TO_EITHER | SURPRISE_ME

archetype_preference:
  FRONTEND_ALIAS | NO_PREFERENCE | SURPRISE_ME

relationship_temperature:
  SWEET | ROMANTIC | FLIRTY | PASSIONATE | PLAYFUL | SURPRISE_ME

heritage_appearance_preference:
  EXPLICIT_SELECTION | NO_PREFERENCE | SURPRISE_ME

age_vibe:
  SIMILAR | YOUNGER_ADULT | MORE_MATURE | NO_PREFERENCE

body_preference:
  LEAN | ATHLETIC | STRONG | SOFT_NATURAL | CURVY | FULLER_NATURAL | NO_PREFERENCE

energy_preference:
  GENTLE | CALM | PLAYFUL | CONFIDENT | DOMINANT | REFINED | NATURAL | NO_PREFERENCE
```

The final frontend wording is owned by the later UI layer. This file defines the backend routing contract.

---

# 3. Preference Priority

Fixed priority:

```text
EXPLICIT USER HARD CHOICE
>
EXPLICIT USER SOFT PREFERENCE
>
SAFE COUPLE COHERENCE
>
MATCH MODE PRIOR
>
DIVERSITY / ROTATION PRIOR
>
SYSTEM DEFAULT
```

Explicit user hard choices include, when supplied:

- partner gender presentation;
- heritage appearance direction;
- adult age direction;
- body preference;
- explicit archetype preference.

Do not silently override these preferences merely because another candidate looks more visually harmonious.

Only reject / reroute a hard preference when the requested combination is unavailable, contradictory, or fails a hard adult / product / model constraint.

---

# 4. Safe User Visual Features

The Matching Engine may read only appearance information already supported by `USER_IDENTITY_CARD` and useful for visual couple coherence.

Allowed soft inputs:

- `VISUAL_AGE_RANGE`;
- face softness / angularity;
- grooming / refinement level when visible;
- body build only when actually visible and sufficiently supported;
- shoulder / body scale only when sufficiently supported;
- current visual presentation;
- broad polish / casualness of the current image.

Do **not** infer from the user's image:

- ethnicity / nationality;
- sexual orientation;
- religion;
- personality;
- socioeconomic status;
- hidden dating preference;
- who the user "should" be attracted to.

User appearance is used only for:

`SAFE COUPLE VISUAL COHERENCE`

It does not replace explicit user preference.

---

# 5. Unknown / Low-Confidence Handling

Never promote weak identity evidence into a hard matching rule.

- body not visible → do not use body build / shoulder scale as a hard match variable;
- age uncertain → use broad adult-age compatibility rather than inventing a narrow band;
- grooming uncertain → treat as unknown / soft;
- headshot only → do not invent height, torso scale, waist / hip proportions or full-body build.

`UNKNOWN ≠ DEFAULT MODEL BODY`

---

# 6. Partner Archetype Interface

Read STEP 5 tags directly from `partner-archetype-library.md`:

- `AURA`
- `BODY_SIGNAL`
- `PRESENTATION`
- `AGE_SIGNAL`
- `ENERGY`
- `GROOMING`
- `CONTRAST_POTENTIAL`
- `FRONTEND_ALIAS`

Backend route:

```text
USER PREFERENCE
↓
FRONTEND_ALIAS / TAG FILTER
↓
ARCHETYPE SHORTLIST
↓
MATCH MODE + COHERENCE + RISK CHECK
```

Examples of direct alias mapping:

- `Soft & Refined` → `M01`
- `Mature & Confident` → `M05`
- `Confident & Powerful` → `F05`
- `Glamorous & Bold` → `F08`
- `Playful & Charming` → `F09`

The current archetype file is the source of truth for aliases and tags. Do not reconstruct a parallel archetype taxonomy here.

---

# 7. Hard Constraint Gate

Resolve explicit constraints before visual-coherence ranking.

Check:

1. `PARTNER_GENDER`
2. `ADULT_ONLY`
3. `EXPLICIT_HERITAGE_DIRECTION` when supplied
4. `EXPLICIT_ARCHETYPE`
5. `EXPLICIT_AGE_DIRECTION`
6. `EXPLICIT_BODY_DIRECTION`
7. any explicit masculinity / femininity / presentation request

If a hard choice maps to more than one valid archetype, keep all valid candidates for the next stage.

If `OPEN_TO_EITHER`, allow both male-presentation and female-presentation archetypes into the shortlist.

If `SURPRISE_ME`, never infer the answer from the user's apparent ethnicity or presumed sexual orientation.

---

# 8. Match Mode Router

Current validated modes remain:

- `H1 — HARMONY MATCH`
- `P1 — PREFERENCE MATCH`
- `C1 — COMPLEMENTARY CONTRAST`

## Router

### Use P1 when

The user explicitly selects a meaningful attraction variable such as:

- archetype;
- body signal;
- energy / aura;
- age direction;
- heritage appearance;
- strong presentation direction.

Rule:

`USER PREFERENCE > DEFAULT COHERENCE PRIOR`

### Use H1 when

The user provides no strong partner-type preference or chooses `NO_PREFERENCE` and wants the system to choose a naturally coherent candidate.

### Use C1 when

- the user explicitly requests contrast; or
- `SURPRISE_ME` produces a high-value contrast route;

and the route passes the Social-Role / Contrast Risk Guard.

C1 is not selected merely because contrast is visually dramatic.

---

# 9. H1 — Harmony Match｜VALIDATED

Goal:

`NATURAL COUPLE-LIKENESS WITHOUT FACE CLONING`

Softly prioritize:

- visual-age coherence;
- grooming / refinement coherence;
- presentation-level coherence;
- aura compatibility;
- body-scale plausibility when evidence exists;
- moderate face-rhythm compatibility;
- attractiveness / polish parity.

## Face Harmony Rule

`FACIAL HARMONY ≠ COPY USER FACE`

Do not copy the user's:

- eye shape;
- nose;
- lips;
- jaw;
- chin;
- exact facial proportions.

Harmony means the two adults can plausibly occupy the same visual / social world, not that they look genetically related.

Validated finding retained:

- natural couple read does not require high geometric facial similarity;
- excessive similarity can reduce candidate distinctiveness.

---

# 10. P1 — Preference Match｜VALIDATED

Goal:

`RESPECT THE USER'S STATED ATTRACTION TYPE`

Example retained from project evidence:

`softer refined user + M05 Mature Dominant`

can remain a valid partner route even if H1 would select a softer candidate.

Do not silently replace an explicit `Mature & Confident`, `Strong & Powerful`, `Glamorous & Bold`, or other user-selected type with a more harmonious archetype unless the requested route fails a hard risk constraint.

P1 may still use Couple Coherence to make **small supporting choices** such as:

- age band within the requested archetype's allowed range;
- grooming variant;
- body variant within user preference;
- presentation intensity.

It may not erase the chosen attraction direction.

---

# 11. C1 — Complementary Contrast｜VALIDATED WITH LIMITS

Goal:

Create attraction fantasy through **controlled contrast**, while preserving adult couple plausibility.

Useful contrast axes include:

- soft ↔ powerful;
- lean ↔ strong;
- warm ↔ cold-refined;
- natural ↔ polished;
- playful ↔ composed;
- young-adult ↔ somewhat more mature adult, while remaining age-plausible.

Default rule:

`1–2 MAJOR CONTRAST DIMENSIONS ONLY`

Do not simultaneously maximize contrast in:

- age;
- body scale;
- grooming;
- social presentation;
- visual authority;
- aura.

Too many contrast axes make the pair read as another social relationship rather than a couple.

---

# 12. Couple Coherence Gate

After hard preferences are respected, check:

- `AGE_COHERENCE`
- `GROOMING_COHERENCE`
- `BODY_SCALE_PLAUSIBILITY`
- `PRESENTATION_LEVEL`
- `AURA_COMPATIBILITY`
- `SOCIAL_ROLE_READ`
- `ATTRACTIVENESS / POLISH PARITY`

## Attractiveness Parity Rule

Do **not** reduce partner attractiveness to force a matching level with the user.

The product may still generate a high-attraction fantasy partner.

The coherence layer only prevents obvious casting discontinuity where the two people look as though they belong to unrelated visual worlds.

---

# 13. Relationship Temperature as a Soft Signal

Relationship temperature may influence tie-breaking, but may not override explicit archetype preference.

Possible soft tendencies:

- `SWEET` → warm / soft / natural / refined routes may receive a tie-break advantage;
- `ROMANTIC` → refined / warm / composed / confident routes can work broadly;
- `FLIRTY` → confident / playful / glamorous / cold-refined routes may receive a tie-break advantage;
- `PASSIONATE` → powerful / confident / sensual routes may receive a tie-break advantage;
- `PLAYFUL` → warm / open / playful / energetic routes may receive a tie-break advantage.

Never encode:

`SWEET = SOFT PARTNER`

or

`PASSIONATE = DOMINANT PARTNER`

The user's explicit type remains primary.

---

# 14. Multi-Orientation / Gender-Neutral Routing

Support at minimum:

- Woman × Man
- Man × Woman
- Woman × Woman
- Man × Man

Matching may not assume:

- who is dominant;
- who is feminine;
- who is protective;
- who initiates;
- who is more physically assertive.

Those roles come later from:

`PARTNER ARCHETYPE + MOMENT + ACTION + CURRENT GEOMETRY`

not from the gender combination itself.

## OPEN_TO_EITHER

When the user selects `OPEN_TO_EITHER`:

- male-presentation and female-presentation archetypes may both enter the shortlist;
- use the user's other explicit preferences, archetype compatibility, coherence, and diversity rotation;
- do not infer orientation from the uploaded photo.

---

# 15. Surprise Me / No Preference

Correct route:

```text
EXPLICIT PARTNER-GENDER SETTING OR OPEN_TO_EITHER
+
NO_PREFERENCE / SURPRISE_ME
↓
SAFE VISUAL COHERENCE
+
ARCHETYPE DIVERSITY
+
NON-REPETITIVE ROTATION
↓
ADULT PARTNER CANDIDATE
```

Do not:

- infer user's ethnicity and return the same heritage automatically;
- infer sexual orientation;
- repeatedly return the same archetype;
- default every user to M02 / F02 merely because they are broad baselines.

If heritage preference is absent, heritage appearance may vary through a diversity route. It is not chosen by guessing the user's real ethnicity.

---

# 16. Contrast / Social-Role Risk Guard

Use risk flags before finalizing H1 / P1 / C1.

A risk flag does not always require replacing the whole partner. Prefer the **smallest variable correction**.

## BODYGUARD_CLIENT

**Common trigger:** very large strength / size contrast + rigid powerful partner + passive user presentation.

**Minimal correction:** soften body-scale difference, reduce rigid / protective aura, or choose a more reciprocal presentation variant while retaining the archetype.

## TRAINER_CLIENT

**Trigger:** athletic / strong partner + highly athletic styling disparity + task-oriented presentation.

**Correction:** preserve the requested athletic archetype but align grooming / social presentation; downstream romantic Action/Gaze must not look instructional.

## PARENT_CHILD_AGE_GAP

**Trigger:** large visual-age gap, especially when one candidate is young-adult-looking and the other reads substantially older.

**Correction:** move one age band closer while preserving the requested archetype when possible.

## CAREGIVER_DEPENDENT

**Trigger:** large age / body / presentation asymmetry + one partner reading frail / dependent.

**Correction:** preserve adult age and archetype but reduce dependent visual coding; align body/presentation parity.

## BOSS_EMPLOYEE

**Trigger:** extreme polished-authoritative vs subordinate-casual contrast plus age / grooming hierarchy.

**Correction:** narrow grooming / presentation gap or choose a less hierarchical variant of the same archetype.

## OVERPOWERED_USER

**Trigger:** power, size and dominance all strongly favor the partner with no balancing visual agency.

**Correction:** reduce one contrast axis only—usually body scale, dominance intensity, or age gap.

## SIBLING_READ

**Trigger:** excessive facial similarity, same grooming, same age signal, same styling.

**Correction:** increase identity distinction through face architecture / hair silhouette / aura while preserving compatibility.

## FRIEND_READ

**Trigger:** candidate route lacks romantic differentiation and both people read as same-energy casual peers.

**Correction:** keep identities; downstream Moment / Action / Expression should carry romantic signaling. Do not overcorrect the partner archetype if the casting itself is valid.

## FASHION_CASTING_PAIR

**Trigger:** both are highly editorial / distant / model-like with no relationship warmth.

**Correction:** keep one editorial archetype if desired; soften the other's aura / grooming or rely on downstream Moment/Gaze to create reciprocity.

## UNRELATED_MODELS

**Trigger:** extreme mismatch in polish, visual age, body presentation, or social-world styling without intentional contrast logic.

**Correction:** align one support variable—usually grooming, age band, or presentation level—without erasing the user's preference.

---

# 17. Internal Fit Labels

Do not use fake compatibility percentages.

Allowed internal ordinal labels:

- `HARD PASS`
- `HARD FAIL`
- `STRONG FIT`
- `GOOD FIT`
- `CONTRAST FIT`
- `RISK FLAG`

Do not output:

- `98% compatible`
- `97% soulmate`
- `perfect match score`

These labels are routing aids, not scientific claims.

---

# 18. MATCH_CANDIDATE_CARD

Matching output should use:

```text
MATCH_CANDIDATE_CARD

partner_gender
selected_archetype_id
frontend_alias
match_mode

resolved_hard_preferences
resolved_soft_preferences

selected_age_band
selected_body_signal
selected_presentation
selected_aura
selected_energy
selected_grooming
selected_heritage_appearance

coherence_notes
contrast_dimensions
risk_flags
fit_label

partner_appearance_card_ref
generation_model_route

internal_selection_reason
visible_prompt_payload
```

## Field Rules

`internal_selection_reason`

- internal only;
- may mention user preference / coherence rationale / contrast reasoning;
- must never be copied into the visible image prompt.

`visible_prompt_payload`

- contains only renderable partner traits;
- derived from the chosen `PARTNER_APPEARANCE_CARD`;
- follows the Archetype Anti-Template rule;
- contains no hidden relationship-selection logic.

---

# 19. VISIBLE SUBJECT FILTER｜VALIDATED

Pipeline:

```text
USER + PREFERENCE
↓
MATCHING ENGINE
↓
MATCH_CANDIDATE_CARD
↓
VISIBLE SUBJECT FILTER
↓
PARTNER_APPEARANCE_CARD / VISIBLE PROMPT PAYLOAD
↓
IMAGE MODEL
```

For `PARTNER SOLO CANDIDATE`, the final prompt must not say:

- compatible with the user;
- stronger than the user;
- creates contrast with the uploaded person;
- selected because the user likes this type;
- visually balances the user's face.

Real project testing showed that relationship rationale can accidentally cause a solo-partner model prompt to render both people.

---

# 20. Default Candidate Policy

Normal commercial runtime generates:

`1 PRIMARY PARTNER MATCH`

Do not display a wall of 10–20 candidates by default.

The candidate should be distinct, high-attraction, and consistent with the resolved preferences.

---

# 21. Try Another Match｜Minimal Reroute

When the user chooses:

`Try Another Match / 换一个`

Keep:

- `USER_IDENTITY`
- `USER_HARD_PREFERENCES`
- `USER_SELECTED_RELATIONSHIP_TEMPERATURE`

Reroute:

- partner candidate only.

Always add:

`EXCLUDE_PREVIOUS_PARTNER_IDENTITY`

## If archetype preference is explicit

Keep the archetype unless the user says the type itself is wrong.

Generate a **new concrete identity** inside the same archetype using the Anti-Template / Candidate Diversity rules.

## If Surprise Me / No Preference

Prefer a different valid archetype or materially different identity route before returning another near-duplicate.

---

# 22. Candidate Diversity Guard

Do not reroll as:

`SAME FACE + DIFFERENT HAIR`

Across repeated candidates, vary multiple real structural axes while respecting hard preferences.

Use at least several of:

- face shape / length-width tendency;
- eye / brow character;
- nose structure;
- jaw / chin;
- hair silhouette / grooming;
- body signal;
- age band when user preference permits;
- aura.

If the archetype is fixed, keep its core design logic while generating a distinct person inside that archetype.

---

# 23. Minimal Reroute Logic for Negative Feedback

When the user says the partner is wrong, change only the failed variable.

### A. "I don't like this face / this person"

`KEEP ARCHETYPE → NEW IDENTITY`

### B. "I don't like this type"

`NEW ARCHETYPE`

### C. "Too young / too old"

`KEEP ARCHETYPE WHERE COMPATIBLE → CHANGE AGE BAND`

### D. "Wrong body type"

`KEEP FACE / ARCHETYPE DIRECTION → CHANGE BODY SIGNAL`

### E. "Wrong vibe / energy"

`KEEP STRUCTURAL IDENTITY DIRECTION → REROUTE AURA / GROOMING OR ARCHETYPE IF NECESSARY`

Do not clear the full user preference state unless the user explicitly requests a reset.

---

# 24. Partner Approval Stop Rule

Once the user approves the generated partner candidate:

```text
MATCHING STOP
↓
ORIGINAL_APPROVED_PARTNER
↓
PARTNER IDENTITY LOCK
```

The Matching Engine may no longer silently change:

- face;
- visual age;
- heritage appearance;
- body identity;
- stable distinctive features.

Only an explicit `CHANGE PARTNER` request reopens matching.

The downstream identity module uses:

`APPROVED VISIBLE IDENTITY > ABSTRACT ARCHETYPE PLAN`

---

# 25. Generation Model Route

Matching chooses **who**, not the final model behavior.

Current partner-candidate route normally references:

- `image 2.5` for high-attraction partner exploration / archetype differentiation / canonical identity support;
- Banana2 Pro when realism / natural heritage appearance is the immediate priority or when current model sensitivity requires it.

Apply `model-routing-rules.md` and `model-adaptation.md` after candidate selection.

Example:

- `F08 Glamorous Bombshell` → Banana2 Pro currently has project validation; image 2.5 remains model-sensitive / unverified.

---

# 26. Rule-Level Acceptance Cases

These are routing checks, not a new image benchmark program.

## CASE A — No strong preference

Input:

- partner gender set;
- archetype / body / energy = no preference.

Expected:

`H1 Harmony Match`

Use safe coherence + diversity rotation.

## CASE B — Explicit Mature & Confident

Input:

- frontend alias `Mature & Confident`.

Expected:

`P1 → M05 Mature Dominant`

User preference overrides a softer H1 alternative.

## CASE C — Soft user + explicit Strong & Powerful

Input:

- user visual presentation = soft / refined;
- explicit `Strong & Powerful`.

Expected:

`P1 with intentional contrast`, or `C1` when the contrast itself is explicitly requested.

Risk-check:

- BODYGUARD_CLIENT;
- OVERPOWERED_USER;
- age / grooming coherence.

Do not silently replace M04 with M01.

## CASE D — Woman × Woman

Expected:

- female-presentation archetypes enter shortlist according to explicit preference;
- no automatic dominant / feminine role assignment;
- H1 / P1 / C1 work identically.

## CASE E — Man × Man

Expected:

- male-presentation archetypes enter shortlist according to explicit preference;
- no heteronormative role assignment;
- visual contrast allowed only through normal archetype / tag logic.

## CASE F — OPEN_TO_EITHER + SURPRISE_ME

Expected:

- both male- and female-presentation archetypes are eligible;
- no orientation inference from the user image;
- select through safe coherence + diversity rotation + valid risk state.

## CASE G — Repeated Try Another Match

Expected:

- keep user identity and hard preferences;
- exclude previous partner identity;
- fixed explicit archetype → new identity inside same archetype;
- Surprise Me → prefer a different valid archetype / structural route;
- no repeated template face.

These cases are sufficient for rule-level acceptance. Do not generate images unless a future real case reveals a decision that cannot be resolved from the routing logic alone.

---

# 27. Current Validated Findings Retained

Keep previous project findings:

- H1 Harmony Match can produce natural couple coherence without face cloning;
- P1 Preference Match successfully preserved a requested `Mature Dominant` direction against a softer user presentation;
- C1 Complementary Contrast can work when the contrast is limited and social-role misread is controlled;
- solo-partner prompts must isolate internal matching rationale;
- different candidates must be separate identities, especially with image 2.5 template-convergence risk.

---

# 28. Final Hard Rules

1. `EXPLICIT USER PREFERENCE > SYSTEM MATCH PRIOR`.
2. User appearance supports visual coherence only; it does not reveal hidden attraction preference.
3. Never infer ethnicity, nationality, orientation, religion, personality or socioeconomic status from the user photo.
4. Never output fake soulmate / compatibility percentages.
5. H1 harmony does not mean facial cloning.
6. C1 contrast should usually vary only 1–2 major dimensions.
7. Same-sex / multi-orientation routes use the same neutral matching logic.
8. Candidate rerolls must create distinct identities, not styling variants.
9. Matching rationale is internal and must pass the `VISIBLE SUBJECT FILTER`.
10. Once a partner is approved, Matching stops and Partner Identity Lock takes authority.
11. Do not reopen broad partner benchmarking unless a real runtime failure exposes a concrete routing problem.
