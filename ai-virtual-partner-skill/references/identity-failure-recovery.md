# Identity Failure & Recovery｜身份失败与恢复运行库

## Purpose

Recover USER / PARTNER identity failures with the **smallest safe correction** instead of rebuilding the whole AI Virtual Partner workflow.

This file owns:

`DETECT FAILURE → CLASSIFY → LOCATE FAILED IDENTITY VARIABLE → RETURN TO CORRECT IDENTITY AUTHORITY → DISCARD BAD REFERENCE WHEN NEEDED → MINIMUM RECOVERY → REGENERATE → QC → PROMOTE ONLY PASSED OUTPUT`

It does **not** own normal identity construction. Normal identity locking remains in:

- `portrait-identity-lock.md`
- `partner-identity-lock.md`

Core separation:

`IDENTITY LOCK = HOW TO KEEP A CORRECT IDENTITY STABLE`

`IDENTITY FAILURE & RECOVERY = WHAT TO DO AFTER IDENTITY HAS ALREADY FAILED`

All people are adults.

---

# 1. Identity Authority｜Never Recover from a Lower-Authority Drift

## USER

`ORIGINAL_USER_IMAGE > USER_IDENTITY_CARD > CANONICAL_IDENTITY > CORE_REFERENCE_SHEET > APPROVED_REFERENCE > TEXT`

## PARTNER

`ORIGINAL_APPROVED_PARTNER > PARTNER_IDENTITY_CARD > APPROVED_REFERENCE_PACKAGE > APPROVED_COUPLE_FRAME > TEXT`

The abstract Partner Archetype is **not** a recovery identity authority after a specific partner has been approved.

Hard rule:

`DO NOT REPAIR DRIFT FROM DRIFT`

Wrong:

`DRIFTED OUTPUT → EDIT → EDIT → EDIT`

Correct:

`DETECT DRIFT → INVALIDATE BAD OUTPUT / REFERENCE → RETURN TO HIGHEST RELIABLE AUTHORITY → LOAD IDENTITY CARD → LOAD BEST QC-PASSED SUPPORT REFERENCE WHEN NEEDED → REGENERATE TARGET STATE → QC`

A prettier later generation never outranks the correct higher-authority identity source.

---

# 2. Severity

- `WARNING` — visible inconsistency that does not yet prove identity replacement; do not promote until checked.
- `RECOVERABLE` — identity drift is localized and can usually be corrected without restarting Matching / Scene / Action.
- `CRITICAL` — current output must immediately fail Identity QC and must never enter an active reference pool.

Critical regardless of aggregate QC score:

- obvious face replacement;
- USER / PARTNER face swap;
- face fusion;
- major age replacement;
- major stable skin-tone replacement;
- major nose / jaw / facial-geometry reconstruction;
- wrong person after a video cut;
- body-slot swap / duplicated identity when two separate people are required;
- a known drifted reference being promoted as identity authority.

---

# 3. Global Minimum-Recovery Rule

Recover only the failed variable.

Examples:

- hairline drift → restore hairline; keep approved scene / action / wardrobe;
- age drift → restore age + identity authority; keep other approved variables where possible;
- scene error → Scene recovery, **not** Identity recovery;
- hand penetration → Anatomy / Action recovery, **not** Identity recovery;
- user dislikes selected partner → Matching reroute, **not** Identity recovery;
- partner is same person but looks less glamorous → Model / presentation issue, **not** Identity recovery.

`IDENTITY FIRST > CONTACT COMPLETION`

For close-proximity romance, preserving two separate identities outranks forcing complete facial contact.

Keep:

`MORE TENSION ≠ MORE CONTACT`

---

# 4. Failure Taxonomy｜33 Runtime Failure Types

## A. Face Identity Failure｜F01–F10

| ID | Failure | Affected | Detection signal | Likely cause | Return authority | Discard | Keep | Minimum recovery | Model note | QC requirement | Severity |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | `FACE_REPLACEMENT` | USER / PARTNER | face reads as another person, not local drift | rebeautification, weak reference binding, recursive edits | USER: original user image; PARTNER: original approved partner | failed output; any derivative reference | scene/action/wardrobe if independently stable | rebind correct identity + L3/HARD anchors; regenerate target state | image 2.5 / Banana / H3 can all fail differently | same-person check + facial geometry | `CRITICAL` |
| F02 | `FACE_SHAPE_DRIFT` | USER / PARTNER | face width/length, cheekbone or lower-face structure changes | angle completion becomes redesign; model beauty prior | highest identity image + identity card | drifting view if used as reference | non-identity styling | restore face shape / width / cheekbone / jaw proportions only | image 2.5 may soften/narrow; Banana close-up may reinterpret | geometry must correspond across views | `RECOVERABLE`; major reconstruction → `CRITICAL` |
| F03 | `EYE_STRUCTURE_DRIFT` | USER / PARTNER | eye shape/spacing/eyelid/brow-eye relation changes | close-up redesign, face fusion, beautification | original + identity card eye anchors | failed close-up if inconsistent | age, nose, jaw, styling | restore eye shape / spacing / brow-eye relation | do not solve by generic “more beautiful eyes” | eye spacing/shape same-person check | `RECOVERABLE` |
| F04 | `NOSE_STRUCTURE_DRIFT` | USER / PARTNER | bridge, width, projection or tip becomes different person | profile completion / beauty-template replacement | original + identity card nose anchors | inconsistent profile / close-up | other correct identity traits | restore approved nose structure; identity completion, not redesign | profile / 3/4 views are sensitive | nose must geometrically correspond to front reference | `RECOVERABLE`; major redesign → `CRITICAL` |
| F05 | `LIP_STRUCTURE_DRIFT` | USER / PARTNER | mouth width / lip ratio / cupid bow changes materially | glamorization, close-contact contamination | original + identity card mouth anchors | failed close-up | correct face geometry and styling | restore mouth width / lip proportion; remove beautification pressure | near-contact can merge lip contours | compare neutral mouth structure | `RECOVERABLE`; major replacement → `CRITICAL` |
| F06 | `JAW_CHIN_DRIFT` | USER / PARTNER | jaw width/angle/chin shape changes | masculinity/femininity styling overwrites identity | original + identity card jaw/chin | drifting output if used as ref | other correct variables | restore jaw/chin only; keep presentation styling separate | partner archetype must not overwrite approved identity | jaw/chin same-person check | `RECOVERABLE`; major reconstruction → `CRITICAL` |
| F07 | `HAIRLINE_DRIFT` | USER / PARTNER | hairline height/shape changes; temple line moves | hairstyle edit, angle completion, model cleanup | original + identity card hairline | only bad hairline reference if promoted | face, age, scene, action | lock core hairline; allow hairstyle arrangement only | image 2.5 / H3 can smooth hairline during motion | hairline consistency at matching angle | `RECOVERABLE` |
| F08 | `AGE_DRIFT` | USER / PARTNER | younger/older face, changed facial volume/skin-age cues | auto-youngification, rebeautification, model cut drift | highest identity source + explicit adult visual-age lock | age-drifted ref | approved non-age styling | restore original visual age + structural age cues; keep other approved state | M05/F04 and androgynous routes need attention | age consistency gate | `RECOVERABLE`; major age replacement → `CRITICAL` |
| F09 | `SKIN_TONE_DRIFT` | USER / PARTNER | stable skin tone materially changes beyond lighting | color cast treated as identity; cross-model reinterpretation | original stable skin-tone evidence | drifted identity ref; not merely a color-graded display output | scene/color if face can be re-rendered correctly | restore stable tone; separate lighting cast from identity | strong blue/green/red light can mimic drift | compare under neutral interpretation | `RECOVERABLE`; major stable-tone replacement → `CRITICAL` |
| F10 | `DISTINCTIVE_FEATURE_LOSS` | USER / PARTNER | stable freckle/mole/scar/facial-hair pattern or defining feature disappears/changes | cleanup, beauty filter, angle completion | original + identity card / approved partner | derivative ref that erases defining feature if identity-critical | other correct identity data | restore only stable visible features; do not invent unseen marks | keep subtle natural distinctiveness | distinctive-feature QC | `RECOVERABLE` |

---

## B. Body Identity Failure｜F11–F15

| ID | Failure | Affected | Detection signal | Likely cause | Return authority | Discard | Keep | Minimum recovery | Model note | QC | Severity |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F11 | `BODY_BUILD_DRIFT` | USER / PARTNER | lean/athletic/curvy/fullness category changes materially | idealized body prior; motion morph | identity card + best approved full/upper-body reference | drifted body reference | face identity, scene/action where possible | restore approved body-build category; no arbitrary slimming/bulking | video may change torso under contact | body-category match | `RECOVERABLE` |
| F12 | `SHOULDER_WIDTH_DRIFT` | USER / PARTNER | shoulder category becomes markedly broader/narrower | power styling, pose correction, two-person overlap | identity card + approved body reference | bad body view | face / wardrobe if valid | restore shoulder category only | strong archetypes must not overwrite approved person | shoulder/body silhouette QC | `RECOVERABLE` |
| F13 | `BODY_PROPORTION_DRIFT` | USER / PARTNER | torso/waist/hip/limb balance changes beyond pose | generation completion from insufficient evidence; motion morph | approved body reference; user original when visible | drifted body ref | correct face + scene | restore only evidenced proportions; unknown stays unknown | never idealize missing body evidence | proportion plausibility + identity | `RECOVERABLE` |
| F14 | `HEAD_BODY_RATIO_DRIFT` | USER / PARTNER | head looks too large/small relative to known body | perspective/model scaling error | original / approved full-body evidence | drifted body frame if promoted | local scene/action | restore stable ratio or reduce perspective stress | wide-angle / video motion can exaggerate | ratio + perspective check | `RECOVERABLE` |
| F15 | `UNKNOWN_BODY_INVENTION` | USER primarily | headshot-only user is assigned a hard specific body identity | unsupported completion treated as fact | USER_IDENTITY_CARD with `UNKNOWN` | invented body as identity reference | face identity | remove invented body lock; keep body generic/flexible until evidence exists | do not treat model default body as user fact | confidence-source check | `WARNING / RECOVERABLE` |

---

## C. Two-Person Contamination｜F16–F22

| ID | Failure | Detection signal | Likely cause | Return authority | Discard | Keep | Minimum recovery | QC | Severity |
|---|---|---|---|---|---|---|---|---|---|
| F16 | `USER_PARTNER_FACE_SWAP` | USER face appears on partner or vice versa | weak slot binding; close interaction/cut transition | A=USER original/package; B=PARTNER approved/package | entire contaminated output as identity ref | scene/action concept if otherwise useful | explicitly rebind A/B references per shot/frame; regenerate | each face must map to correct slot | `CRITICAL` |
| F17 | `FACE_FUSION` | faces share features / merge at close distance | almost-kiss / forehead / cheek proximity too compressed | separate A/B identity authorities | fused output | relationship moment concept | increase face separation; offset heads; simplify transition; rebind both identities | two distinct readable faces | `CRITICAL` |
| F18 | `FEATURE_CONTAMINATION` | eye/nose/lip traits bleed from one person to the other | identity proximity / ambiguous reference assignment | separate A/B cards + references | contaminated reference | correct unaffected traits | isolate slots; reduce occlusion / overlap; regenerate | compare both persons separately | `CRITICAL` when materially identity-changing |
| F19 | `HAIR_CONTAMINATION` | hairline/color/style transfers between people | overlap, similar silhouettes, reference confusion | separate A/B identity sources | contaminated output if promoted | face identity if clean | rebind hair/hairline per person; change framing if silhouettes overlap | hairline + hair color identity | `RECOVERABLE` |
| F20 | `SKIN_CONTAMINATION` | one person's stable skin appearance shifts toward the other's | close light/color mixing or slot confusion | each person's stable skin evidence | contaminated ref | scene color logic if physically valid | restore each identity tone; reduce face-overlap / strong colored spill | separate-person skin identity check | `RECOVERABLE`; major swap → `CRITICAL` |
| F21 | `BODY_SLOT_SWAP` | partner body traits attach to user or vice versa | contact morph, cut reassignment | A/B body identity sources | failed frame/output | action idea | rebind identity+body slots each shot; simplify transition | face + body must belong to same slot | `CRITICAL` |
| F22 | `DUPLICATED_PERSON` | both figures become the same identity | model template convergence / missing slot isolation | A/B separate authorities | duplicated output | scene/action concept | explicit distinct PERSON_A/PERSON_B references; strengthen candidate separation | distinct identities required | `CRITICAL` |

---

## D. Reference Failure｜F23–F27

| ID | Failure | Detection signal | Likely cause | Return authority | Discard | Keep | Minimum recovery | QC | Severity |
|---|---|---|---|---|---|---|---|---|---|
| F23 | `BAD_REFERENCE_PROMOTED` | later generations drift after one low-quality reference entered pool | QC bypass | highest trusted original / approved identity | bad reference + derived authority role | independent valid refs | mark invalid, remove from active pool, regenerate affected identity-critical assets if needed | source lineage + same-person check | `CRITICAL` for reference pool |
| F24 | `CONFLICTING_REFERENCE_PACKAGE` | package contains mutually inconsistent face geometry | mixed generations / failed views | original + one coherent QC-passed package | conflicting views | coherent subset | remove contradictory refs; rebuild only missing angle if needed | package must be geometrically self-consistent | `CRITICAL` for package use |
| F25 | `CROSS_MODEL_IDENTITY_CONFLICT` | image 2.5 and Banana versions depict structurally different person | model reinterpretation | highest original/approved identity + one coherent model package | lower-authority conflicting version as identity ref | model output as display artifact if not reused | choose one coherent identity package; never average faces | nose/jaw/face-shape consistency | `RECOVERABLE`; promoted hybrid → `CRITICAL` |
| F26 | `DRIFTED_REFERENCE_REUSE` | known drifted image continues generating more drift | reference lifecycle failure | original / approved identity | drifted ref and any authority status | unaffected valid refs | remove from active pool; stop descendants from becoming authorities | reference-status audit | `CRITICAL` |
| F27 | `RECURSIVE_EDIT_DRIFT` | identity gradually changes after repeated edits | editing the latest edit rather than authority source | original / approved identity | recursive edit chain as authority | final scene intent / edit target spec | restart target edit from correct authority source | compare against original, not previous edit | `RECOVERABLE`; severe replacement → `CRITICAL` |

Reference contamination protocol:

`MARK INVALID → REMOVE FROM ACTIVE REFERENCE POOL → TRACE DEPENDENT IDENTITY-CRITICAL OUTPUTS WHEN RELEVANT → DO NOT USE AS FUTURE AUTHORITY`

A bad reference may remain as a non-authoritative failure example, but never as an active identity source.

---

## E. Video Identity Failure｜F28–F33

| ID | Failure | Detection signal | Likely cause | Return authority | Discard / keep | Minimum recovery | H3 strategy | QC | Severity |
|---|---|---|---|---|---|---|---|---|---|
| F28 | `MOTION_IDENTITY_DRIFT` | face gradually changes within a shot | long continuous transformation, head turn, contact stress | first-frame visual truth + USER/PARTNER identity packages | keep approved first frame; reject drifted clip | reduce continuous morph load; shorter action; stronger identity inheritance | cut before high-risk transform; rebind next shot | same-person across frames | `RECOVERABLE`; obvious replacement → `CRITICAL` |
| F29 | `CLOSE_DISTANCE_FACE_FUSION` | near-contact causes merged faces | face-to-face distance too small during motion | separate A/B identity refs + first frame | reject fused clip | preserve unresolved gap; offset heads; shorten near-contact transition | use cut into stable close state instead of continuous collision | two distinct faces at payoff | `CRITICAL` |
| F30 | `CUT_IDENTITY_SWITCH` | after cut, USER/PARTNER becomes wrong person or identity | shot reinitialization loses slot mapping | first frame + A/B packages | reject affected clip | explicitly restate A=USER / B=PARTNER identity inheritance for every shot | every shot starts from same identity assignment | slot identity after each cut | `CRITICAL` |
| F31 | `SHOT_TO_SHOT_AGE_DRIFT` | one person becomes younger/older after shot change | shot reinitialization / rebeautification | identity package + visual-age lock | reject affected segment/clip | restate adult visual age and identity anchors per shot; reduce beauty reinterpretation | keep 3-beat grammar; add age continuity only | age consistency across cuts | `RECOVERABLE`; major replacement → `CRITICAL` |
| F32 | `HAIR_WARDROBE_IDENTITY_CONFUSION` | hair/wardrobe swaps or becomes identity cue for wrong person | slot ambiguity after cut | A/B identity packages + approved first-frame wardrobe state | reject when it causes slot confusion | bind each person's hair + wardrobe continuity separately | restate person-specific continuity after each cut | identity + wardrobe slot check | `RECOVERABLE`; if person switch → `CRITICAL` |
| F33 | `BODY_SHAPE_CHANGE_DURING_MOTION` | torso/shoulder/build changes across movement | motion morph / overlap | approved first frame + body identity evidence | reject severe drift clip | simplify body-contact transition; keep body category stable | cut around high-risk overlap; reduce extreme rotation | body identity across shots | `RECOVERABLE` |

MiniMax H3 production grammar remains unchanged:

`BEAT 1 → CUT → BEAT 2 → CUT → BEAT 3`

Recovery modifies **identity inheritance and motion stress**, not the validated 3-beat / ~2-cut structure.

---

# 5. Close-Proximity Identity Guard

High-risk interaction families include:

- Soft Almost-Contact;
- Breath-Close;
- Forehead Close;
- Face-Side Touch;
- cheek / temple proximity;
- near-kiss payoffs.

Default recovery preference:

`KEEP TWO FACES SEPARATE + OFFSET HEADS + PRESERVE SMALL UNRESOLVED GAP > FORCE COMPLETE CONTACT`

If identity becomes unstable:

1. increase face separation slightly;
2. offset head angles / heights;
3. reduce face occlusion by hands / hair;
4. shorten the continuous close-in motion;
5. use a natural cut before the highest-risk geometry;
6. rebind A/B identity references after the cut.

Do not sacrifice identity stability to make the action more explicit.

---

# 6. USER Recovery Route

When feedback / QC indicates USER identity failure:

```text
FAILURE DETECTED
→ ORIGINAL_USER_IMAGE
→ USER_IDENTITY_CARD
→ RELOAD L3 ABSOLUTE LOCK
→ RELOAD L2 STRONG LOCK WHEN RELEVANT
→ BEST QC-PASSED SUPPORT REFERENCE IF NEEDED
→ REGENERATE ONLY FAILED STATE
→ IDENTITY QC
```

Compact prompt intent when needed:

`same adult person; preserve original face geometry, visual age, stable skin tone and hairline; identity completion, not redesign.`

Do not stack dozens of negative constraints unless a concrete failure requires them.

---

# 7. PARTNER Recovery Route

After user approval, the partner is a **specific person**.

Recovery authority:

```text
ORIGINAL_APPROVED_PARTNER
→ PARTNER_IDENTITY_CARD
→ BEST QC-PASSED APPROVED_REFERENCE_PACKAGE
```

Never recover a drifted approved partner by calling the abstract Archetype again.

Wrong:

`Partner X drifted → generate another M05 → call it Partner X`

Correct:

`Partner X drifted → return to Partner X approved image / identity card → regenerate same person`

Only explicit user action such as `CHANGE PARTNER / 换伴侣` may release the partner lock and reopen Matching.

---

# 8. Archetype vs Identity Boundary

Before approval:

`ARCHETYPE → PARTNER DESIGN`

After approval:

`APPROVED PARTNER IMAGE → SPECIFIC IDENTITY`

Therefore, after approval:

- Archetype may describe broad style lineage;
- Archetype may **not** overwrite nose / eyes / jaw / hairline / age / distinctive features;
- Recovery always returns to the approved person, not a new person of the same type.

---

# 9. Cross-Model Conflict Rule

Possible identity assets may pass through:

- image 2.5;
- Banana2 Pro;
- MiniMax H3.

If two models disagree structurally about the same person:

`ONE INTERNALLY COHERENT QC-PASSED PACKAGE > HYBRID CONFLICTING PACKAGE`

Do not average or merge conflicting nose / jaw / face-shape interpretations.

For Partner identity assets, retain the current empirical rule:

- image 2.5 is the preferred canonical identity-asset route when it preserved the approved person best;
- Banana2 Pro can support realism but must not replace a structurally stronger canonical package;
- MiniMax H3 inherits identity; it does not become a new identity authority because a later video frame looks attractive.

---

# 10. Model-Specific Failure Separation

## image 2.5

Known identity risks:

- template convergence;
- age softening / rebeautification;
- face-width / structure drift in identity completion.

Recovery:

`preserve original face structure + adult age unchanged + distinctive features unchanged + identity completion, not redesign`

Known rendering risk:

- grey / muddy / cement-like tonality.

This is a **render-quality problem**, not identity failure unless it also changes identity-relevant skin / facial structure.

## Banana2 Pro

Known risks:

- close-up reinterpretation;
- conservative / ordinary beauty prior;
- skin oversmoothing;
- bright / milky white haze.

Keep separate:

`PARTNER NOT ATTRACTIVE ENOUGH ≠ IDENTITY DRIFT`

If the approved person is still the same person but looks less glamorous, route to Model / presentation / lighting refinement, not identity reconstruction.

## MiniMax H3

Keep:

`APPROVED_COUPLE_IMAGE = FIRST FRAME / VISUAL TRUTH`

Identity authorities remain the USER / PARTNER reference packages.

For identity failure:

- reduce long continuous morphs;
- cut before high-risk head / contact transforms;
- reduce extreme head rotation;
- preserve visible separation between faces;
- shorten face-to-face convergence;
- rebind USER / PARTNER references for every new shot.

Do not replace the validated 3-beat / ~2-cut grammar.

---

# 11. Failure → Recovery Quick Matrix

| Failure | Return to | Minimum recovery |
|---|---|---|
| `FACE_REPLACEMENT` | original user / approved partner | rebind correct person + hard face anchors; regenerate |
| `FACE_SHAPE_DRIFT` | original + identity card | restore L3/HARD geometry only |
| `AGE_DRIFT` | original + visual-age anchor | restore age; preserve approved scene/action/wardrobe |
| `HAIRLINE_DRIFT` | original / identity card | lock hairline only |
| `SKIN_TONE_DRIFT` | stable identity evidence | restore stable tone; separate lighting cast from identity |
| `FACE_FUSION` | A/B identity authorities | rebind both; increase face separation; offset heads; simplify transition |
| `USER_PARTNER_FACE_SWAP` | A=USER, B=PARTNER | explicit slot rebind; regenerate affected output |
| `PARTNER_RECAST` / partner looks like another person | original approved partner | prohibit Archetype regeneration; regenerate same approved person |
| `BAD_REFERENCE_PROMOTED` | higher authority | invalidate + remove reference; stop future reuse |
| `CONFLICTING_REFERENCE_PACKAGE` | original + coherent subset | remove contradictory views; rebuild only missing coverage |
| `RECURSIVE_EDIT_DRIFT` | original / approved source | restart edit from authority, not latest edit |
| `MOTION_IDENTITY_DRIFT` | first frame + identity packages | shorten continuous transform; cut and rebind |
| `CUT_IDENTITY_SWITCH` | first frame + A/B packages | explicit A/B assignment at every shot |
| `CLOSE_DISTANCE_FACE_FUSION` | A/B packages | keep unresolved gap; cut into stable close state |

---

# 12. Natural-Language User Feedback Router

Users do not need to know failure IDs.

| User feedback | Internal classification | Route |
|---|---|---|
| `不是我了 / 这不是我` | F01 FACE_REPLACEMENT or major F02 | USER recovery from original user image |
| `脸变了` | F02–F06 depending visible change | identify changed facial variable; restore only that variable |
| `鼻子变了` | F04 NOSE_STRUCTURE_DRIFT | restore approved nose structure |
| `怎么年轻了 / 变老了` | F08 AGE_DRIFT | restore visual age from identity authority |
| `发际线变了` | F07 HAIRLINE_DRIFT | restore hairline only |
| `肤色不对了` | F09 or lighting issue | first separate light cast vs identity drift, then recover if identity changed |
| `这个人不是刚才那个` | Partner F01 / recast | return to ORIGINAL_APPROVED_PARTNER; do not reopen Archetype |
| `两个人脸混了` | F17 FACE_FUSION / F18 contamination | rebind A/B; increase separation / simplify close geometry |
| `他们换脸了` | F16 USER_PARTNER_FACE_SWAP | rebind PERSON_A / PERSON_B |
| `第二个镜头换人了` | F30 CUT_IDENTITY_SWITCH | rebind identities at every shot / cut |
| `越改越不像` | F27 RECURSIVE_EDIT_DRIFT | stop edit chain; restart from authority source |
| `参考图好像本来就不对` | F23 / F24 / F26 | invalidate bad reference and rebuild from higher authority |

Agent-facing behavior:

- classify internally;
- perform / recommend the smallest recovery route;
- do not expose failure-code jargon unless the user asks for debugging detail.

---

# 13. Not Identity Failure｜Module Boundary

Do **not** call Identity Recovery for:

- hand / finger penetration, extra fingers, limb intersection → `Anatomy / Relation Action`;
- wrong action / pose / contact point → `Relation Action`;
- wrong Moment / emotional timing → `Moment`;
- wrong gaze / smile → `Expression / Gaze`;
- wrong scene / furniture / spatial logic → `Scene`;
- wrong palette / wardrobe color with identity intact → `Color / Wardrobe`;
- selected partner type not liked by user → `Matching Engine`;
- approved partner is same person but not glamorous enough → `Model / Presentation`;
- grey / muddy image with stable identity → `Model Rendering Quality`;
- white haze / overexposure with stable identity → `Model / Camera Realism`.

Only escalate to Identity Recovery when the **person themselves** has changed, fused, swapped, or their stable identity evidence has been corrupted.

---

# 14. Reference-Pool Promotion Gate

Before any generated USER or PARTNER image enters an active reference pool:

1. same-person identity passes;
2. face geometry passes;
3. age passes;
4. stable skin identity passes;
5. hair / hairline passes;
6. body identity passes when visible;
7. distinctive features pass when relevant;
8. no Critical Failure flag exists.

`CRITICAL FAILURE → IMMEDIATE FAIL`, even if an aggregate numerical QC score would otherwise be high.

Only QC-passed outputs may be promoted.

---

# 15. Runtime Recovery Algorithm

```text
USER / QC REPORTS IDENTITY PROBLEM
↓
IS THE PERSON'S STABLE IDENTITY ACTUALLY WRONG?
├─ NO → ROUTE TO ACTION / SCENE / MODEL / MATCHING / COLOR / ANATOMY
└─ YES
    ↓
CLASSIFY FAILURE TYPE
    ↓
IS OUTPUT / REFERENCE CONTAMINATED?
├─ YES → INVALIDATE / REMOVE FROM ACTIVE POOL
└─ NO → KEEP NON-FAILED ASSETS
    ↓
RETURN TO CORRECT USER / PARTNER AUTHORITY
    ↓
RECOVER ONLY FAILED IDENTITY VARIABLE(S)
    ↓
IF TWO-PERSON OR VIDEO: REBIND PERSON_A / PERSON_B
    ↓
IF CLOSE-PROXIMITY: REDUCE TRANSFORMATION STRESS / PRESERVE FACE SEPARATION
    ↓
REGENERATE TARGET STATE
    ↓
IDENTITY QC
    ↓
PASS → MAY PROMOTE
FAIL → DO NOT PROPAGATE; RETURN TO AUTHORITY AGAIN
```

---

# 16. Testing Rule

Do not create a broad identity-failure benchmark suite.

Use current project evidence + future real production failures.

Only run a new generation test when a concrete Recovery Rule cannot be decided without it and the result would change production routing.

Current STEP 7 requires **no new synthetic generation test**.
