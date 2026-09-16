# Portrait Identity Lock Validation Cases

Status target for this module after documentation-only creation:

`UPDATED — RUNTIME UNVERIFIED`

These cases define the minimum regression set for future image-generation testing.

## Case 1 — Original Failure: Beautification changes identity

### Input
One clear adult portrait with stable front-facing facial features.

### Stress
Request a more glamorous, sexy, high-end result.

### Expected
- same face shape
- same eye spacing and eye shape
- same nose structure
- same lip structure
- same jaw/chin structure
- same visual age range
- same stable skin tone
- styling may improve lighting, makeup, wardrobe, and camera treatment only

### Fail if
The result is prettier but clearly becomes a different person.

---

## Case 2 — Neighbor Case: Scene and wardrobe change

### Input
One approved user identity.

### Stress
Change from casual indoor clothing to evening wardrobe and a different environment.

### Expected
Only wardrobe, scene, lighting, camera, and pose change.

### Fail if
The face, age, stable skin tone, hairline, or body baseline changes materially.

---

## Case 3 — Counterexample: Unknown body evidence

### Input
Headshot only.

### Stress
Generate a full-body scene.

### Expected
Body fields unsupported by the source remain `UNKNOWN` internally and must not be presented as known identity facts.

### Fail if
The system claims a specific body type was inferred with confidence from the headshot.

---

## Case 4 — Multi-image conflict

### Input
Three photos of the same adult:
- one unfiltered normal-perspective image
- one beauty-filter image
- one wide-angle selfie

### Expected
Stable facial structure is anchored primarily from the unfiltered normal-perspective evidence. Filter and lens distortion are treated as photo conditions.

### Fail if
The canonical face inherits enlarged eyes, narrowed jaw, altered nose, or other filter/lens artifacts.

---

## Case 5 — Four-view consistency

### Input
One approved user identity.

### Stress
Build front, three-quarter, profile, and close-up identity views.

### Expected
All views remain recognizably the same person with coherent 3D facial geometry, stable age, stable skin tone, stable hairline, and preserved distinctive marks where visible.

### Fail if
Any view looks like a different person or introduces a redesigned nose, jaw, lips, eyes, or age.

---

## Case 6 — Drift propagation block

### Input
One original portrait, one approved reference, and one newly generated image with visible identity drift.

### Expected
The drifted image is marked `IDENTITY_DRIFT` and excluded from the reference pool. Regeneration falls back to the original/canonical/approved identity anchors.

### Fail if
The drifted image becomes the next generation's identity source.

---

## Case 7 — Two-person identity isolation

### Input
Approved user reference plus a separate future partner reference.

### Stress
Generate a close couple composition.

### Expected
- user remains the user
- partner remains the partner
- no facial fusion
- no face swap
- no skin-tone or hairstyle cross-contamination

### Fail if
The two identities merge, swap, or converge into sibling-like copied faces because of reference contamination.

---

## Case 8 — Text prompt cannot override identity

### Input
Approved user identity.

### Stress
Prompt contains words such as `beautiful`, `handsome`, `glamorous`, `model-like`, or `sexy`.

### Expected
Those terms affect presentation only.

### Fail if
They trigger automatic eye enlargement, face slimming, nose redesign, lip enlargement, jaw redesign, age reduction, or stable skin-tone change.

---

## Runtime Evaluation Requirement

When a real image-generation runtime is available, execute at least:

1. original failure case;
2. one normal neighbor case;
3. one counterexample;
4. one four-view case;
5. one drift-recovery case.

Record:

- input reference set
- generated result
- Identity QC score
- whether the result was promoted or rejected
- observed failure mode
- rule change if any

Documentation presence alone is not runtime proof.
