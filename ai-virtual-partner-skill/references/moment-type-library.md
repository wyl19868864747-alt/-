# Moment Type Library｜情侣关系时刻库

## Purpose

Define **what relationship state exists at this exact moment in time**.

This file does not own body pose, scene, or facial-expression mechanics.

Keep the layers separate:

- `MOMENT` = what just happened → what is happening now → what may happen next
- `ACTION` = body orientation / contact / weight / hands, owned by `relation-action-library.md`
- `EXPRESSION / GAZE` = visible facial and eye response, owned by `expression-gaze-library.md`
- `SCENE` = physical space, owned by `scene-tension-library.md`

Runtime:

`RELATIONSHIP TEMPERATURE → SELECT MOMENT STATE → SELECT ACTION + EXPRESSION / GAZE → SCENE + COLOR → IMAGE PROMPT / VIDEO PROMPT`

All people are adults. Moment routing is gender-neutral.

---

# 1. Status Labels

- `VALIDATED CORE` — direct project generation evidence supports default use.
- `VALIDATED VIDEO` — demonstrated inside the current MiniMax H3 production route.
- `EVIDENCE-INFORMED` — strongly supported by real couple / lifestyle interaction logic and compatible with current generation grammar.
- `CANDIDATE` — useful but not a default.
- `HIGH-RISK` — easy to misread socially or push identity / anatomy too hard.

Do not benchmark every Moment. Promote through real runtime when useful.

---

# 2. Time-State Rule｜BEFORE → NOW → NEXT

Every Moment must answer:

`WHAT JUST HAPPENED → CURRENT RELATIONSHIP STATE → NEXT NATURAL BEAT`

A Moment is useful when the viewer can feel that the image is a frame taken from an ongoing relationship event rather than a static pose.

For still images, `NOW` must be instantly readable.

For video, the `NEXT NATURAL BEAT` should provide a clean continuation into the next MiniMax H3 beat.

---

# 3. Core Moment Families

## M01 — PRIVATE EYE CONTACT｜VALIDATED CORE

**Relationship temperature:** Sweet / Romantic / Flirty

**What just happened:** conversation / movement / previous touch has paused.

**Current state:** both adults give their attention to each other; the surrounding scene temporarily feels secondary.

**Viewer should read:** mutual interest, private bubble, couple chemistry.

**Compatible actions:** A01, A02, A04, A06, A14

**Expression / gaze patterns:** G01 Direct Mutual Gaze, G02 Soft Partner Gaze, E01 Restrained Smile, E03 Quiet Warmth, E05 Focused Attraction

**Still image value:** VERY HIGH

**Video start:** HIGH | **middle:** HIGH | **payoff:** HIGH

**Next natural beat:** slight lean-in / reaction smile / face-side touch / brief release.

**Failure risk:** if both bodies are upright and both faces perform toward camera, it becomes a posed portrait.

---

## M02 — FIRST LEAN-IN｜EVIDENCE-INFORMED

**Temperature:** Romantic / Flirty / Passionate

**Just happened:** eye contact / side embrace / playful approach.

**Current state:** one partner has started closing personal distance; the other visibly accepts or responds.

**Viewer reads:** something is about to happen.

**Compatible actions:** A01, A05, A06, A07, A10, A11

**Expression / gaze:** G01, G03 Eye→Lip→Eye, G04 Look Away→Look Back, E05 Focused Attraction, E09 Anticipation

**Still:** HIGH | **video start:** VERY HIGH | **middle:** HIGH | **payoff:** MEDIUM

**Next:** unresolved close / almost-contact / reaction smile.

**Risk:** if receiver does not respond, it can read as one-sided or uncomfortable.

---

## M03 — SOFT ALMOST-CONTACT｜VALIDATED CORE

Former `Soft Almost-Kiss`, redefined as a relationship state rather than a fixed pose.

**Temperature:** Romantic / Flirty / Passionate

**Just happened:** both partners have already moved into close personal space.

**Current state:** faces remain very close with a small unresolved gap; contact is not required.

**Viewer reads:** strong mutual attraction and anticipation.

**Compatible actions:** A01 + T03 Breath-Close, A05, A06, A07, A18 when geometry is safe

**Expression / gaze:** G01, G03, G10 Half-Closed Intimate Pause, E05, E09

**Still:** VERY HIGH / HERO | **video start:** MEDIUM | **middle:** HIGH | **payoff:** VERY HIGH

**Next:** brief affectionate contact if allowed, forehead close, slight pullback + smile.

**Risk:** faces too close can fuse; completing contact immediately can remove tension.

Core rule: `MORE TENSION ≠ MORE CONTACT`.

---

## M04 — REACTION SMILE｜VALIDATED VIDEO

**Temperature:** Sweet / Romantic / Flirty / Playful

**Just happened:** one partner initiates a small touch, whisper, pull-in, or gaze cue.

**Current state:** the receiving partner shows a short, restrained smile before returning attention.

**Viewer reads:** the interaction is reciprocal, not staged.

**Compatible actions:** A01, A08, A10, A11, A14, A17

**Expression / gaze:** G06 Whisper→Reaction Look, G07 Laugh→Reconnect, E02 Reaction Smile, E10 Slightly Flustered Response

**Still:** HIGH | **video start:** MEDIUM | **middle:** VERY HIGH | **payoff:** MEDIUM

**Next:** look back / lean closer / settle into embrace.

**Risk:** exaggerated grin becomes commercial acting rather than intimacy.

---

## M05 — AFTER-LAUGH RECONNECT｜EVIDENCE-INFORMED

**Temperature:** Sweet / Playful / Romantic

**Just happened:** both laughed or one reacted to a joke / playful gesture.

**Current state:** laughter settles; eyes return to the partner; body distance closes again.

**Viewer reads:** real familiarity and ease.

**Compatible actions:** A10, A11, A17, A14

**Expression / gaze:** G07 Laugh→Reconnect, E07 Post-Laugh Softening, E01 Restrained Smile

**Still:** HIGH | **video start:** MEDIUM | **middle:** VERY HIGH | **payoff:** HIGH

**Next:** quiet eye contact / forehead close / side embrace.

**Risk:** if laughter remains broad and open-mouth, it reads as generic lifestyle advertising.

---

## M06 — WHISPER REACTION｜EVIDENCE-INFORMED

**Temperature:** Sweet / Flirty / Playful / Romantic

**Just happened:** one partner moves near ear / temple and says something privately.

**Current state:** receiver reacts before turning back.

**Viewer reads:** private shared information and couple-specific closeness.

**Compatible actions:** A02, A06, A14, A17

**Expression / gaze:** G06 Whisper→Reaction Look, E02, E10

**Still:** HIGH | **video start:** MEDIUM | **middle:** VERY HIGH | **payoff:** MEDIUM

**Next:** smile → direct gaze → renewed approach.

**Risk:** mouth placed too close to ear / hair can create fusion; without reaction it looks like staged whispering.

---

## M07 — PLAYFUL CHALLENGE｜EVIDENCE-INFORMED

**Temperature:** Playful / Flirty

**Just happened:** one partner has pulled away half a step, looked back, or teased the other.

**Current state:** small separation exists, but gaze / hand connection clearly invites pursuit.

**Viewer reads:** teasing attraction, not rejection.

**Compatible actions:** A09, A10, A11, A13

**Expression / gaze:** G04, G05 Shared View→Partner, E04 Playful Half-Smile, E10

**Still:** HIGH | **video start:** VERY HIGH | **middle:** HIGH | **payoff:** LOW

**Next:** pull-in / half-turn into embrace / laugh reconnect.

**Risk:** without connection it can look like two friends or a fashion pose.

---

## M08 — QUIET COMFORT｜EVIDENCE-INFORMED

**Temperature:** Sweet / Protective / Romantic

**Just happened:** movement / conversation has settled.

**Current state:** one person rests into the other's space; neither performs strongly.

**Viewer reads:** safety, trust, long-term closeness.

**Compatible actions:** A02, A03, A04, A15

**Expression / gaze:** G02, G08 Downward Soft Gaze, E03 Quiet Warmth, E08 Protective Calm

**Still:** HIGH | **video start:** MEDIUM | **middle:** MEDIUM | **payoff:** HIGH

**Next:** look up / side gaze / soft smile / forehead close.

**Risk:** can read parent-child or caregiver if age / body / agency are imbalanced.

---

## M09 — PROTECTIVE CALM｜EVIDENCE-INFORMED

**Temperature:** Protective / Sweet / Romantic

**Just happened:** one partner has moved closer or wrapped / supported the other.

**Current state:** receiving partner relaxes without losing adult agency.

**Viewer reads:** secure partnership, not control.

**Compatible actions:** A02, A03, A15

**Expression / gaze:** G02, G08, E03, E08

**Still:** HIGH | **video start:** HIGH | **middle:** MEDIUM | **payoff:** HIGH

**Next:** receiving partner turns inward / returns gaze / touches forearm or shoulder.

**Risk:** bodyguard/client or parent-child if only one person acts.

---

## M10 — MUTUAL ATTRACTION HOLD｜EVIDENCE-INFORMED

**Temperature:** Romantic / Flirty / Passionate

**Just happened:** an approach or touch change has completed.

**Current state:** both pause in a close, mutually active position before the next action.

**Viewer reads:** both are choosing to stay close.

**Compatible actions:** A01, A05, A06, A07

**Expression / gaze:** G01, G03, E05, E09

**Still:** VERY HIGH | **video start:** MEDIUM | **middle:** HIGH | **payoff:** HIGH

**Next:** almost-contact / slight pullback / reaction smile.

**Risk:** frozen expressions make it look like fashion posing.

---

## M11 — POST-CONTACT PULLBACK｜VALIDATED VIDEO

**Temperature:** Romantic / Flirty / Passionate

**Just happened:** brief affectionate contact or very close approach.

**Current state:** both separate only slightly while keeping waist / shoulder / upper-back connection.

**Viewer reads:** intimacy just occurred; attraction remains active.

**Compatible actions:** A01, A05, A06

**Expression / gaze:** G01, G02, E01, E06 Soft Relief

**Still:** HIGH | **video start:** LOW | **middle:** MEDIUM | **payoff:** VERY HIGH

**Next:** stable smile / eye-contact close.

**Risk:** if separation is too large, chemistry disappears; if both smile identically, it feels staged.

---

## M12 — UNRESOLVED CLOSE｜VALIDATED CORE

**Temperature:** Romantic / Flirty / Passionate

**Just happened:** distance has narrowed and both adults have stopped before a clear payoff.

**Current state:** small face gap + stable body contact + focused partner attention.

**Viewer reads:** tension from what has not happened yet.

**Compatible actions:** A01 + T03, A05, A06, A18

**Expression / gaze:** G01, G03, G10, E05, E09

**Still:** VERY HIGH | **video start:** MEDIUM | **middle:** HIGH | **payoff:** VERY HIGH

**Next:** contact / pullback / smile / forehead close.

**Risk:** holding this state too long in video becomes visually repetitive.

---

## M13 — SHARED VIEW → TURN TO PARTNER｜EVIDENCE-INFORMED

**Temperature:** Sweet / Romantic / Protective

**Just happened:** both were looking at the same view / environment.

**Current state:** one partner turns attention from the environment to the other; the second notices and responds.

**Viewer reads:** private attention emerging inside a shared experience.

**Compatible actions:** A02, A04, A12, A13

**Expression / gaze:** G05, G02, E01, E03

**Still:** HIGH | **video start:** VERY HIGH | **middle:** HIGH | **payoff:** MEDIUM

**Next:** side embrace / close eye contact / turn-in.

**Risk:** if second partner never responds, it can look observational rather than romantic.

---

## M14 — WALKING → LOOK BACK｜EVIDENCE-INFORMED

**Temperature:** Playful / Flirty / Romantic

**Just happened:** one partner leads / moves half a step ahead.

**Current state:** lead partner looks back while maintaining a hand / waist connection or clear shared path.

**Viewer reads:** invitation and movement toward the next interaction.

**Compatible actions:** A09, A10, A12, A13

**Expression / gaze:** G04, E04, E01

**Still:** HIGH | **video start:** VERY HIGH | **middle:** HIGH | **payoff:** LOW

**Next:** stop / pull-in / half-turn / embrace.

**Risk:** can become solo fashion pose if the second partner's response is not visible.

---

## M15 — REUNION / ARRIVAL BEAT｜CANDIDATE

**Temperature:** Sweet / Romantic / Playful

**Just happened:** one partner has just arrived / stepped into shared space.

**Current state:** attention locks quickly; body distance begins to close.

**Viewer reads:** recognition, anticipation, familiarity.

**Compatible actions:** A09, A10, A11, A17

**Expression / gaze:** G01, G04, E02, E04

**Still:** MEDIUM | **video start:** VERY HIGH | **middle:** MEDIUM | **payoff:** LOW

**Next:** pull-in / laugh / embrace.

**Risk:** without a clear relationship cue, it can read as generic greeting.

---

# 4. Relationship Temperature Routing

## Sweet
Prefer M01, M04, M05, M08, M09, M13.

## Romantic
Prefer M01, M02, M03, M08, M10, M11, M12, M13.

## Flirty
Prefer M02, M03, M04, M06, M07, M10, M12, M14.

## Passionate
Prefer M02, M03, M10, M11, M12.

Do not equate Passionate with immediate completed contact.

## Playful
Prefer M04, M05, M06, M07, M14, M15.

## Protective
Prefer M08, M09, M13.

---

# 5. Still vs Video Rule

## Still Image

Choose a Moment whose `NOW` state reads immediately:

- M01 Private Eye Contact
- M03 Soft Almost-Contact
- M04 Reaction Smile
- M08 Quiet Comfort
- M10 Mutual Attraction Hold
- M12 Unresolved Close

Do not encode an entire multi-step sequence into one still.

## Video

Moment must evolve:

`STATE A → RESPONSE → STATE B`

Useful 10-second chains include:

- M13 Shared View→Partner → M01 Private Eye Contact → M03 / M12 Unresolved Close
- M07 Playful Challenge → M04 Reaction Smile → M05 After-Laugh Reconnect
- M06 Whisper Reaction → M01 Private Eye Contact → M11 Post-Contact Pullback
- M02 First Lean-In → M10 Mutual Attraction Hold → M03 Soft Almost-Contact

Do not hold M03 / M12 unchanged for the full clip.

---

# 6. Social Misread Guard

- `friends / siblings`: require partner-directed gaze + closer shared space + reciprocal response.
- `coworkers`: avoid neutral conversational eye contact with no body / reaction progression.
- `bodyguard / client`: receiving partner must return gaze / touch / weight.
- `parent / child`: preserve adult age coherence and equal agency.
- `trainer / client`: attention should return from task to partner.
- `fashion-model posing`: include a readable BEFORE/NOW/NEXT relationship event rather than frozen stare.

---

# 7. Migrated Legacy Items

The following former “moments” are no longer stored here as Moment types:

- `Shoulder Lean` → Action A04
- `Back Hug` → Action A03
- `Window-Side Embrace` → Scene + Action combination
- `Mirror Couple` → Scene / composition concept, not a core Moment
- `Sweet Selfie` → Action A16 + appropriate Moment
- `Playful Outdoor Couple` → Scene + Action + Moment combination
- `Neck / Shoulder Close Proximity` → Action / proximity geometry, not Moment

Retained and reclassified:

- `Close Eye Contact` → M01 Private Eye Contact
- `Soft Almost-Kiss` → M03 Soft Almost-Contact / M12 Unresolved Close

---

# 8. Current Defaults

- realistic sweet default → `M01 PRIVATE EYE CONTACT`
- romantic Hero → `M03 SOFT ALMOST-CONTACT` or `M12 UNRESOLVED CLOSE`
- playful candid → `M04 REACTION SMILE` or `M05 AFTER-LAUGH RECONNECT`
- protective / stable → `M08 QUIET COMFORT`
- H3 closing beat → `M11 POST-CONTACT PULLBACK` or M01 with restrained smile

Moment selects **when** the relationship is caught. Action selects **what the bodies are doing**. Expression / Gaze selects **what the faces visibly communicate**.