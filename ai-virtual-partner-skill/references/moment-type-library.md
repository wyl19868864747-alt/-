# Moment Type Library｜甜蜜瞬间类型库

## Purpose

Provide reusable adult-couple moment patterns. Moment type changes the relationship feeling while identity, partner selection and model routing remain fixed.

---

## VALIDATED CORE MOMENTS

### MMT-01 — Close Eye Contact

Use for:

- sweetness
- emotional intimacy
- believable romantic chemistry
- safer default than stronger sensual moments

Visual grammar:

- bodies close
- both orient naturally toward each other
- user gaze soft / warm
- partner gaze focused and affectionate
- neither person performs directly for the camera
- camera feels like it caught a private moment

Validated result:

- consistently produced clear couple chemistry in image 2.5 and Banana2 Pro;
- image 2.5 generated stronger fantasy / beauty;
- Banana2 Pro generated stronger photographic realism but required more explicit emotional cues.

Recommended use:

`DEFAULT REALISTIC SWEET MOMENT`

---

### MMT-02 — Soft Almost-Kiss

Use for:

- highest romantic tension
- hero / cover image
- stronger fantasy value
- subtle sensuality without direct explicitness

Visual grammar:

- faces very close
- retain a small unresolved gap
- user slightly raises face / gaze
- partner approaches with restrained attention
- body proximity is obvious
- sweetness remains stronger than explicit sexuality

Validated result:

- strongest hero potential in current tests;
- image 2.5 repeatedly produced the highest-impact result;
- Banana2 Pro remained realistic but required more relationship / tension cues.

Recommended use:

`DEFAULT HERO MOMENT`

---

### MMT-03 — Shoulder Lean

Use for:

- stable couple feeling
- warmth
- safety
- long-term relationship mood

Visual grammar:

- user naturally leans into partner shoulder
- partner subtly leans back / toward user
- bodies close without tension performance
- relaxed expression

Validated result:

- natural and sweet;
- lower romantic tension than Close Eye Contact or Soft Almost-Kiss;
- useful as secondary / everyday content, not the strongest default hero.

Recommended use:

`SAFE / LONG-TERM SWEETNESS`

---

## CANDIDATE MOMENTS

Not yet sufficiently benchmarked for production default:

- Sweet Selfie
- Back Hug
- Playful Outdoor Couple
- Mirror Couple
- Window-Side Embrace
- Neck / Shoulder Close Proximity

Keep candidate until tested with locked identities and at least two models where appropriate.

---

## Moment Selection Logic

If user asks for:

- `sweet / real / everyday` → prefer `Close Eye Contact` or `Shoulder Lean`
- `heart-flutter / romantic / best partner` → prefer `Soft Almost-Kiss`
- `safe / gentle / stable relationship` → prefer `Shoulder Lean`
- `strong chemistry` → prefer `Close Eye Contact` then `Soft Almost-Kiss`

Do not select a stronger intimate moment merely because it is visually more dramatic. Match the user's requested intimacy level.
