# Asset Library Governance｜资产库治理与测试原则

## Purpose

The AI Virtual Partner Skill is a production orchestration system supported by reusable asset libraries.

Benchmarks exist only to improve those libraries. They are not user-facing workflow steps and should not become endless isolated experiments.

---

## 1. What the Asset Libraries Must Answer

The libraries should make the runtime able to answer four practical questions quickly:

1. `WHO IS THE USER?`
   - lock the uploaded real person's identity;
   - preserve that identity through image and video generation.

2. `WHO IS A SUITABLE PARTNER?`
   - search the partner archetype / matching library;
   - support multiple adult orientation routes;
   - respect explicit user preference first;
   - return an attractive, plausible partner identity.

3. `WHAT SHOULD THEY BE DOING / WHERE?`
   - select relationship action, moment, scene, color / wardrobe palette, expression and relationship temperature from reusable libraries;
   - avoid repeating one pose / one neutral room / one palette for every user.

4. `HOW SHOULD THE APPROVED IMAGE MOVE?`
   - use the approved couple image as the video first frame;
   - preserve both identities;
   - select a validated 10-second Seedance 2.5 interaction grammar.

---

## 2. Library Families

### Identity Libraries

- user portrait identity lock
- partner identity lock

### Partner Libraries

- partner archetypes
- heritage appearance routes
- body / age / masculinity / femininity variants
- multi-orientation partner candidates
- matching priors and user-preference routing

### Relationship Image Libraries

- Couple Moment DNA
- relation-action grammar
- gaze / expression patterns
- scene families
- color / wardrobe palettes
- relationship temperature

### Model Libraries

- Banana2 Pro prompt adapter
- image 2.5 prompt adapter
- Seedance 2.5 video adapter
- camera-realism controls

### Video Libraries

- first-frame states
- 10-second flirt / intimacy interaction patterns
- safe hand / body-contact trajectories
- identity-preserving motion patterns
- ending beats

---

## 3. Validation Status

Every library entry should be one of:

- `VALIDATED` — real generation evidence supports production use.
- `CANDIDATE` — promising but not yet sufficiently tested.
- `REJECTED / RISKY` — produced repeatable failure or poor product value.

Do not promote a rule merely because it sounds plausible.

Do not keep testing a VALIDATED item unless a new model / market / failure changes the decision.

---

## 4. Testing Doctrine｜少测但测对

### Core Rule

`TEST ONLY WHEN THE RESULT CAN CHANGE A PRODUCT / LIBRARY DECISION`

Good reasons to test:

- choose between two model routes;
- verify an identity-lock technique;
- validate a new partner archetype family;
- check whether an action is romantic rather than friendly;
- validate a new scene / color family;
- verify a Seedance motion pattern does not drift identity or penetrate bodies.

Weak reasons to test:

- prove a tiny wording difference with no routing consequence;
- repeatedly A/B the same validated asset;
- isolate every color / pose / expression separately when a combined test can answer the practical question;
- create benchmark pages that never become runtime assets.

---

## 5. Combined Representative Tests

When variables can be interpreted together, prefer one representative combined test:

`PARTNER TYPE + ACTION + SCENE + COLOR + EXPRESSION + RELATIONSHIP STATE`

Example:

A Western female-female couple candidate may be tested once using:

- validated attractive partner route
- sofa-corner lean-in
- night-city window
- burgundy + cream wardrobe
- relaxed flirtatious gaze
- breath-close relationship state

If the result is operationally good, record the useful components and move on.

Do not automatically split it into six isolated test pages.

---

## 6. Minimum Useful Sample Principle

Use the smallest sample that can reveal a real decision.

Typical guidance:

- new action family: 1–3 representative outputs;
- new scene / color family: 1–3 representative outputs;
- new partner archetype family: a small contrast set rather than every permutation;
- model route comparison: stop once strengths / weaknesses are clear and compensation has been tried;
- video motion grammar: 1–2 short clips per genuinely different motion structure before expanding.

These are operating guidelines, not mandatory numeric quotas.

---

## 7. Current Production Priorities

Do not spend more time re-proving already sufficient modules unless they fail in real runtime.

Current priority gaps are:

1. broaden the partner library for Western / English-speaking commercial use without stereotyping;
2. expand relation-action / scene / color variety using distilled high-value references;
3. build the Seedance 2.5 **10-second** interaction library from approved first frames;
4. validate the end-to-end runtime once with a real uploaded user image:
   `upload → lock → partner resolve → action/scene lookup → image → approval → 10s video`.

---

## 8. Runtime Is Not a Benchmark UI

Normal user experience should be simple:

```text
UPLOAD PHOTO
→ CHOOSE / CONFIRM PARTNER PREFERENCES
→ GENERATE COUPLE IMAGE
→ USER APPROVES OR CHANGES PARTNER / MOMENT
→ GENERATE 10s VIDEO
```

Internal libraries and benchmark labels should remain invisible unless needed for debugging or expert controls.
