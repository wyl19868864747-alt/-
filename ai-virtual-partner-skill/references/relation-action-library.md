# Relation Action Library｜情侣关系动作语法

## Purpose

Translate romantic chemistry into executable body relationships instead of generic pose labels. The output should look like a captured relationship moment, not a formal couple pose.

Use the grammar:

`INITIATOR + BODY ORIENTATION + CONTACT POINT + WEIGHT TRANSFER + HEAD RELATION + GAZE + HAND PLACEMENT + INTIMACY LEVEL`

Do not prompt only with labels such as `back hug` or `romantic pose` when body geometry matters.

---

## VALIDATED ACTIONS

### 1. FACE-TO-FACE WAIST HOLD — STRONGEST CURRENT ACTION

Observed result:

- strongest romantic / hormonal tension among the tested action set;
- relationship intention reads immediately;
- works well with eye contact and almost-kiss states;
- suitable base for Seedance lean-in motion.

Grammar:

- initiator: partner slightly more active;
- orientation: face-to-face, bodies close, slight forward lean;
- contact: one hand at waist / rear waist, the other person may touch chest / upper arm / shoulder;
- weight: both move slightly toward each other;
- head: one head slightly lowered, the other slightly raised;
- gaze: at each other, not camera;
- intimacy: Romantic Tension.

Risks:

- waist hand can distort / penetrate fabric;
- if faces start too close, generation can jump directly to a kiss or merge facial geometry;
- if bodies are perfectly square and static, it can read as posed.

---

### 2. PROTECTIVE SIDE EMBRACE — VALIDATED SAFE

Observed result:

- strong sweetness / protective feeling;
- believable couple relationship;
- lower hormonal tension than face-to-face waist hold.

Grammar:

- initiator: partner;
- orientation: side-by-side with partner slightly turned inward;
- contact: shoulder / upper arm / side torso;
- weight: user may softly lean into partner;
- head: head / temple / shoulder proximity;
- gaze: camera or partner depending moment;
- intimacy: Warm Intimacy.

Risk:

- may become conservative or read as a standard posed couple portrait if the bodies remain too upright and symmetrical.

---

### 3. BACK HUG — VALIDATED SWEET, CURRENTLY CONSERVATIVE

Observed result:

- clear affection and safety;
- strong `being held` feeling;
- current tested result remained sweeter than sensual.

Grammar:

- initiator: partner from behind / rear-side;
- orientation: same general direction;
- contact: chest / shoulder to back + arms around waist area;
- weight: user relaxes slightly backward;
- head: partner near temple / side face / hair;
- gaze: user may look camera / down / sideways; partner may look user;
- intimacy: Warm Intimacy → Romantic Tension.

Risks:

- arm / hand collision;
- can look restrictive rather than affectionate;
- AI may misplace arms around abdomen / waist.

---

## TENSION LAYER｜VALIDATED

For the current window-side / face-to-face setup:

### SOFT ROMANTIC

- warm and gentle;
- safe sweetness;
- lower tension.

### TENSION LOOK

- restrained expression;
- focused gaze;
- stronger attraction signal;
- risk of becoming confrontational if smiles / softness are removed too aggressively.

### BREATH-CLOSE — CURRENT STRONGEST

- close body distance;
- clear waist / chest contact;
- very small remaining face distance;
- no completed kiss;
- strongest current balance of sweetness + chemistry + hormonal tension.

Key principle:

`MORE TENSION ≠ MORE CONTACT`

The strongest result preserves a small unresolved distance and lets gaze / breath / hand contact imply what may happen next.

---

## Prompt Compile Rule

For relationship images and video first frames, compile physical facts rather than abstract words:

Bad:

`very romantic, sexy, high chemistry`

Better:

`partner keeps one hand at the user's waist; user rests a hand on the partner's chest; both lean toward each other; faces remain just apart; both look only at each other; no completed kiss.`

---

## Current Default

For a strong romantic Hero direction:

`FACE-TO-FACE WAIST HOLD + BREATH-CLOSE`

For safer sweetness:

`PROTECTIVE SIDE EMBRACE`

For a secure / held feeling:

`BACK HUG`

Do not expand this file with large pose counts until new pose families are actually tested.