# Asset Library Governance｜资产库治理与测试原则

## Purpose

The AI Virtual Partner Skill is a production orchestration system supported by reusable asset libraries.

Benchmarks exist only to improve those libraries. They are not user-facing workflow steps and should not become endless isolated experiments.

---

## 1. What the Asset Libraries Must Answer

The libraries must let runtime answer four practical questions quickly:

1. `WHO IS THE USER?`
   - lock the uploaded real person's identity;
   - preserve it through image and video generation.

2. `WHO IS A SUITABLE PARTNER?`
   - search partner archetype / matching libraries;
   - support multiple adult orientation routes;
   - respect explicit user preference first;
   - return an attractive, plausible partner identity.

3. `WHAT SHOULD THEY BE DOING / WHERE?`
   - select relationship action, moment, scene, color / wardrobe palette, expression and relationship temperature;
   - avoid repeating one pose / one neutral room / one palette for every user.

4. `HOW SHOULD THE APPROVED IMAGE MOVE?`
   - use the approved couple image as the video first frame / visual truth;
   - preserve both identities;
   - use the validated 10-second MiniMax H3 multi-beat / multi-shot interaction grammar.

---

## 2. Library Families

### Identity Libraries

- user portrait identity lock;
- partner identity lock.

### Partner Libraries

- partner archetypes;
- heritage appearance routes;
- body / age / masculinity / femininity variants;
- multi-orientation partner candidates;
- matching priors and user-preference routing.

### Relationship Image Libraries

- Couple Moment DNA;
- relation-action grammar;
- gaze / expression patterns;
- scene families;
- color / wardrobe palettes;
- relationship temperature.

### Model Libraries

- Banana2 Pro image adapter;
- image 2.5 partner / canonical-identity adapter;
- MiniMax H3 validated 10-second video adapter;
- historical Seedance 2.5 evidence;
- camera-realism controls.

### Video Libraries

- approved first-frame authority;
- 10-second flirt / intimacy interaction patterns;
- 3-beat / 2-cut shot grammar;
- safe hand / body-contact trajectories;
- identity-preserving motion patterns;
- ending beats.

---

## 3. Validation Status

Every runtime asset should carry one of these statuses:

- `VALIDATED CORE` — direct project generation evidence supports production-default use.
- `EVIDENCE-INFORMED` — supported by established photography / interaction practice or strong adjacent evidence and simple enough for production use, but not yet a project default.
- `CANDIDATE` — promising and structurally useful, but should not become a default until real runtime evidence supports it.
- `HIGH-RISK` / `REJECTED / RISKY` — anatomy, identity, social-role, model-compatibility, or product-value risk is high enough that runtime should not default-route to it.

An asset may carry a compound label such as `EVIDENCE-INFORMED / ANATOMY-SENSITIVE` or `CANDIDATE / HIGH-RISK` when that gives runtime a useful routing warning.

Do not keep testing a VALIDATED item unless a new model / market / real production failure changes the decision.

Do not require a synthetic benchmark before every EVIDENCE-INFORMED asset can be used. Prefer real runtime evidence when geometry is simple and the risk is low.

---

## 4. Testing Doctrine｜少测但测对

Core rule:

`TEST ONLY WHEN THE RESULT CAN CHANGE A PRODUCT / LIBRARY DECISION`

Good reasons to test:

- verify a real-user identity-lock technique;
- validate a genuinely new partner archetype family;
- check whether a new action reads romantic rather than friendly;
- validate a new scene / color family when it fills a real asset gap;
- investigate a concrete MiniMax H3 identity / anatomy / cut failure seen in runtime.

Weak reasons to test:

- prove a tiny wording difference with no routing consequence;
- repeatedly A/B the same validated asset;
- isolate every color / pose / expression separately when a combined runtime test can answer the practical question;
- create benchmark pages that never become runtime assets.

---

## 5. Combined Representative Tests

When variables can be interpreted together, prefer one representative combined test:

`PARTNER TYPE + ACTION + SCENE + COLOR + EXPRESSION + RELATIONSHIP STATE`

If the output is operationally good, record the useful components and move on.

Do not automatically split one production question into many isolated benchmark pages.

---

## 6. Minimum Useful Sample Principle

Use the smallest sample that can reveal a real decision.

Typical guidance:

- new action family: 1–3 representative outputs only when risk / product read is unclear;
- new scene / color family: 1–3 representative outputs;
- new partner archetype family: small contrast set rather than every permutation;
- model route comparison: stop once strengths / weaknesses and routing are clear;
- video grammar: one representative production clip is enough when it proves the chosen route operationally usable.

These are operating guidelines, not mandatory numeric quotas.

---

## 7. Current Status｜Benchmark Phase Closed

Current production routing is sufficiently established for the next phase:

- `image 2.5` → partner exploration / canonical partner identity assets;
- `Banana2 Pro` → current default user-facing couple image;
- `MiniMax H3` → current validated 10-second video route;
- Seedance 2.5 → historical evidence only.

The first H3 10-second multi-beat / multi-shot run has been judged usable. Do not continue broad video benchmarking.

Asset-library expansion should now happen mainly from research distillation + real runtime cases rather than synthetic benchmark pages.

---

## 8. Next Priority｜ONE End-to-End Acceptance Test

The only planned validation still worth doing is one complete runtime acceptance test using a real uploaded adult user image:

```text
UPLOAD REAL USER PHOTO
→ LOCK USER IDENTITY
→ READ / CONFIRM PARTNER PREFERENCE + ORIENTATION
→ PARTNER LIBRARY LOOKUP + MATCHING
→ LOCK PARTNER IDENTITY IF NEEDED
→ ACTION / MOMENT / SCENE / COLOR LOOKUP
→ BANANA2 PRO COUPLE IMAGE
→ USER APPROVES / MINIMAL REROUTE
→ FREEZE APPROVED_COUPLE_IMAGE
→ MINIMAX H3 10s VIDEO
→ FINAL IDENTITY / ANATOMY / REALISM QC
```

If this one end-to-end flow is operationally successful, treat the Skill as ready for product packaging / iMA integration. Do not start a new benchmark cycle unless the end-to-end run reveals a concrete blocker.

---

## 9. Runtime Is Not a Benchmark UI

Normal user experience should stay simple:

```text
UPLOAD PHOTO
→ CHOOSE / CONFIRM PARTNER PREFERENCES
→ GENERATE COUPLE IMAGE
→ USER APPROVES OR CHANGES PARTNER / MOMENT
→ GENERATE 10s VIDEO
```

Internal library IDs, benchmark labels and validation history remain invisible unless needed for debugging or expert controls.
