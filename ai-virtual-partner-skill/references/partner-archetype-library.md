# Partner Archetype Library｜虚拟伴侣原型运行库

## Purpose

Define **what kind of adult partner this person is before matching, couple staging, or identity locking**.

This is a runtime asset library, not a beauty-ranking document.

Runtime:

`USER PREFERENCE + PARTNER GENDER + AGE VIBE + BODY PREFERENCE + MASCULINITY / FEMININITY + STYLE / ENERGY + HERITAGE APPEARANCE → SELECT ARCHETYPE → BUILD PARTNER_APPEARANCE_CARD → GENERATE DISTINCT PARTNER CANDIDATE`

This file owns:

`ADULT AGE BAND + GENDER PRESENTATION + ARCHETYPE + HERITAGE APPEARANCE + FACE ARCHITECTURE + BODY ARCHITECTURE + MASCULINITY / FEMININITY + HAIR / GROOMING + SKIN STATE + STYLE AURA + DISTINCTIVE FEATURES`

It does **not** own:

- whether the person is the best match for a user → `matching-engine.md`;
- relationship action → `relation-action-library.md`;
- relationship time-state → `moment-type-library.md`;
- expression / gaze → `expression-gaze-library.md`;
- scene / color → scene and color libraries;
- preservation of an approved specific partner → `partner-identity-lock.md`.

Core separation:

`ARCHETYPE = PERSON DESIGN`

`MATCHING = WHO TO CHOOSE`

`PARTNER IDENTITY LOCK = KEEP THE CHOSEN PERSON THE SAME`

All generated partners are adults.

---

# 1. Evidence / Safety Rules

Use:

- `VALIDATED CORE` — direct project generation evidence supports production-default use.
- `EVIDENCE-INFORMED` — supported by attraction / casting / lifestyle / dating-visual evidence and structured enough for production use.
- `CANDIDATE` — promising but not a default.
- `MODEL-SENSITIVE / CONDITIONAL` — valid archetype, but current model behavior needs special handling.

Research is distilled only into generation-relevant controls.

Do not encode:

- a universal golden-ratio face;
- perfect symmetry as a hard beauty rule;
- lighter / darker skin as more attractive;
- one heritage group as more attractive than another;
- one heritage group as one fixed face;
- more masculinity as automatically more attractive;
- more femininity as automatically more attractive;
- thinner / more muscular / more curvy as universally better;
- personality, dominance, body type, relationship role, or sexual orientation from heritage appearance.

Useful broad priors remain flexible rather than absolute:

- coherent / prototypical facial structure can support perceived attractiveness;
- healthy-looking natural skin contributes to visual appeal;
- natural asymmetry is allowed;
- femininity / masculinity can be controlled as visual parameters, but preferences vary;
- grooming, body presentation, distinctiveness and social `vibe` materially change how a partner candidate reads;
- age-consistent vitality is preferable to automatic youthification.

`ATTRACTIVE + DISTINCTIVE + STILL NATURAL`

---

# 2. Adult Age Band System

Use adult visual-age bands as generation controls, not as identity guesses.

- `YOUNG_ADULT` — approximately 21–29 visual age.
- `ADULT` — approximately 30–39 visual age.
- `MATURE_ADULT` — approximately 40–55 visual age.
- `AGE_FLEX` — current archetype may move into an adjacent adult band without changing its core identity logic.

Rules:

1. Never generate a juvenile-looking partner.
2. Do not automatically youngify a mature archetype.
3. Mature adults retain age-natural skin, facial volume, hairline and facial structure rather than becoming a young face with a `mature` label.
4. User-selected age preference overrides archetype default when structurally compatible.
5. Age is independent of dominance, softness, beauty, heritage and relationship role.

---

# 3. Shared Parameter Vocabulary

## 3.1 Body Build

Use only visually meaningful non-extreme categories:

- `LEAN`
- `LEAN_ATHLETIC`
- `ATHLETIC`
- `SOLID_ATHLETIC`
- `MUSCULAR_ATHLETIC`
- `SOFT_NATURAL`
- `CURVY_NATURAL`
- `FULLER_NATURAL`

Body build is independent of gender presentation. Do not default men to muscular or women to curvy.

## 3.2 Masculinity / Femininity

Use:

- `LOW`
- `MODERATE`
- `MODERATE_HIGH`
- `HIGH`
- `FLEXIBLE`

Keep:

`MASCULINITY ≠ DOMINANCE`

`FEMININITY ≠ SOFTNESS`

`DOMINANCE ≠ ANGER`

`ANDROGYNOUS ≠ JUVENILE`

## 3.3 Grooming / Hair Vocabulary

Use as flexible visual controls when compatible with the selected identity / heritage direction:

- clean groomed;
- natural textured;
- short refined;
- longer refined;
- clean shave;
- natural stubble;
- short beard;
- polished / structured hair;
- loose natural hair;
- sleek hair;
- curls / waves / straight texture;
- visible natural hairline.

Do not bind one hairstyle to one heritage appearance.

---

# 4. Heritage Appearance｜Independent Axis

`HERITAGE_APPEARANCE ≠ ARCHETYPE_ID`

Current user-selectable / diversity-routing appearance directions may include:

- European appearance;
- African / African-diaspora appearance;
- Latino / mixed-heritage appearance;
- East Asian appearance;
- Southeast Asian appearance;
- South Asian appearance;
- Middle Eastern / Mediterranean appearance;
- multi-ethnic appearance.

Rules:

1. Never infer the user's real ethnicity / nationality from the user's photo.
2. Heritage appearance comes from explicit user choice, `No Preference / Surprise Me`, or a product diversity route.
3. The same archetype must remain recognizable across heritage directions.
4. Do not implement heritage as `same face template + changed skin color`.
5. Natural morphology may vary with the selected visual direction, but heritage may not automatically determine personality, dominance, attractiveness, body build or relationship role.
6. Never infer sexual orientation from appearance.

---

# 5. Matching Interface Tags

Every archetype exposes tags for `matching-engine.md`. These are candidate descriptors, not final match decisions.

## AURA

`soft | warm | clean | confident | dominant | rugged | cold | playful | glamorous | refined | natural | sensual | artistic | energetic | composed`

## BODY_SIGNAL

`lean | lean-athletic | athletic | strong | solid | soft-natural | curvy | fuller-natural`

## PRESENTATION

`soft | balanced | masculine | feminine | androgynous | powerful | polished | natural`

## AGE_SIGNAL

`young-adult | adult | mature | age-flex`

## ENERGY

`calm | open | energetic | restrained | assertive | playful | sensual | protective-looking | social | editorial`

## GROOMING

`clean | refined | natural-textured | rugged | polished | glamorous | minimal`

## CONTRAST_POTENTIAL

`low | medium | high`

`matching-engine.md` decides whether a tag is useful for the current user. This library does not decide who the user should choose.

---

# 6. Male-Presentation Archetypes

## M01 — Soft Refined｜VALIDATED CORE

**Frontend alias:** `Soft & Refined`

- adult age band: `YOUNG_ADULT / ADULT`;
- gender presentation: adult male-presenting;
- core attraction signal: refinement + softness + adult poise;
- face structure: balanced oval / slightly elongated, soft cheek-to-jaw transition;
- softness / angularity: soft-moderate;
- eye / brow: clear eyes, moderate brow density, slightly more open eye area;
- nose: balanced / refined, not over-sculpted;
- lips: moderate definition;
- jaw / chin: clean, moderate width, non-square;
- facial contrast: moderate;
- masculinity: `LOW–MODERATE`;
- femininity: `LOW–MODERATE` visual softness only;
- hair / grooming: clean shave, refined short or medium-short hair, visible natural hairline;
- skin state: healthy natural texture, not airbrushed;
- body build: `LEAN / LEAN_ATHLETIC`;
- strength signal: low-moderate;
- shoulder signal: moderate / refined silhouette;
- style aura: gentle / polished / composed;
- distinctive feature 01: slightly longer facial proportion or narrower lower face;
- distinctive feature 02: softer brow-eye transition than M02 / M04;
- anti-template rule: do not give broad square jaw, heavy brow or bodybuilder neck;
- age variants: can shift into early `ADULT` while preserving softness;
- model notes: image 2.5 reads this archetype clearly; Banana2 Pro may need explicit refined facial structure so it does not collapse into generic male;
- matching tags: `aura: soft, refined, composed | body: lean | presentation: soft/balanced | age: young-adult/adult | grooming: refined | contrast: medium`.

---

## M02 — Clean Masculine｜VALIDATED CORE

**Frontend alias:** `Clean & Masculine`

- adult age band: `YOUNG_ADULT / ADULT`;
- core attraction signal: balanced masculinity + modern grooming;
- face structure: balanced rectangular-oval;
- softness / angularity: moderate;
- eye / brow: straight / clean brow, calm eyes, medium eye depth;
- nose: straight / balanced;
- lips: moderate, controlled definition;
- jaw / chin: clearly defined but non-extreme;
- facial contrast: moderate;
- masculinity: `MODERATE`;
- femininity: `LOW`;
- hair / grooming: clean-groomed short hair, clean shave or minimal stubble;
- skin: healthy, even but natural;
- body: `LEAN_ATHLETIC / ATHLETIC`;
- strength signal: moderate;
- shoulders: moderate-broad, not power-body emphasis;
- style aura: clean / stable / contemporary;
- distinctive 01: clearer jaw-angle than M01;
- distinctive 02: medium brow-eye depth without M04 heaviness;
- anti-template: preserve moderate structure; do not inflate jaw / shoulders into Power Masculine;
- age variants: `YOUNG_ADULT → ADULT`;
- model notes: stable baseline in both image models;
- tags: `aura: clean, confident | body: lean-athletic | presentation: balanced/masculine | age: young-adult/adult | grooming: clean | contrast: low-medium`.

---

## M03 — Athletic Sunlit｜EVIDENCE-INFORMED

**Frontend alias:** `Athletic & Open`

- adult age band: `YOUNG_ADULT / ADULT`;
- core signal: healthy physical vitality + open social energy;
- face structure: balanced with slightly stronger cheek / jaw definition than M02;
- angularity: moderate;
- eye / brow: open, direct, energetic eye area; natural brow;
- nose / lips: flexible, natural rather than editorially sculpted;
- jaw / chin: athletic but not massive;
- facial contrast: moderate;
- masculinity: `MODERATE`;
- femininity: `LOW`;
- hair / grooming: natural textured short hair; clean shave / light stubble;
- skin: healthy natural texture, slight real-world outdoor variation allowed;
- body: `ATHLETIC`;
- strength: moderate-high;
- shoulders: athletic proportion, not oversized;
- style aura: open / energetic / warm;
- distinctive 01: slightly more prominent cheek / jaw transition;
- distinctive 02: natural textured hair / less polished grooming than M02;
- anti-template: avoid turning athletic into bodybuilding or generic fitness influencer;
- age variants: young-adult / adult;
- model notes: Banana2 Pro useful for realistic lifestyle read; image 2.5 may over-idealize athletic face unless distinctive structure is retained;
- tags: `aura: warm, energetic, open | body: athletic | presentation: balanced | age: young-adult/adult | grooming: natural-textured | contrast: medium`.

---

## M04 — Power Masculine｜VALIDATED CORE

**Frontend alias:** `Strong & Powerful`

- adult age band: `ADULT / AGE_FLEX`;
- core signal: visible physical power + controlled masculinity;
- face structure: broader, more angular, stronger lower third;
- angularity: high but natural;
- eye / brow: deeper-set eye area, stronger brow architecture;
- nose: medium-strong structure;
- lips: moderate / slightly restrained;
- jaw / chin: broad and clearly defined;
- facial contrast: moderate-high;
- masculinity: `HIGH`;
- femininity: `LOW`;
- grooming: clean short hair / short textured hair; clean shave or controlled stubble;
- skin: healthy natural texture;
- body: `MUSCULAR_ATHLETIC`;
- strength: high;
- shoulders: broad;
- style aura: forceful / sensual / controlled;
- distinctive 01: visibly broader jaw / lower face;
- distinctive 02: broader shoulder-to-neck silhouette;
- anti-template: do not exaggerate into bodybuilder proportions, angry expression or comic-book jaw;
- age variants: adult; can move slightly younger / older while retaining power structure;
- model notes: clear in both tested image models;
- tags: `aura: confident, dominant, controlled | body: strong | presentation: powerful/masculine | age: adult/age-flex | grooming: clean | contrast: high`.

---

## M05 — Mature Dominant｜VALIDATED CORE

**Frontend alias:** `Mature & Confident`

- adult age band: `MATURE_ADULT / ADULT`;
- core signal: adult maturity + authority + restraint;
- face structure: mature balanced / slightly long, defined lower face without M04 bulk;
- angularity: moderate-high;
- eye / brow: calm deep-set eyes, stable brow line, lower reactivity;
- nose: defined adult structure;
- lips: moderate / restrained;
- jaw / chin: defined, not necessarily broad;
- facial contrast: moderate;
- masculinity: `MODERATE_HIGH`;
- femininity: `LOW`;
- hair / grooming: refined short hair, age-natural hairline; clean shave, stubble or short beard when identity direction supports it;
- skin: age-natural healthy texture; fine lines allowed;
- body: `SOLID_ATHLETIC / ATHLETIC`;
- strength: moderate-high;
- shoulders: solid rather than maximal;
- style aura: composed / authoritative / restrained;
- distinctive 01: mature eye / brow depth and age-natural facial volume;
- distinctive 02: defined chin / jaw without M04 power-body proportions;
- anti-template: do not create a 25-year-old beauty face with grey hair; maturity must be structural and skin-age consistent;
- age variants: adult → mature adult;
- model notes: validated across multiple heritage appearance routes; Banana2 Pro showed strong heritage naturalness; image 2.5 useful for canonical identity with anti-rebeautification;
- tags: `aura: confident, dominant, composed | body: solid/athletic | presentation: masculine/polished | age: mature | grooming: refined | contrast: high`.

---

## M06 — Rugged Masculine｜EVIDENCE-INFORMED

**Frontend alias:** `Rugged & Grounded`

- adult age band: `ADULT / MATURE_ADULT`;
- core signal: natural texture + physical groundedness;
- face structure: angular / slightly broader mid-lower face;
- angularity: high but irregular / natural;
- eye / brow: heavier natural brow, direct eye area;
- nose: may be slightly broader / more characterful rather than refined-template;
- lips: natural / moderate;
- jaw / chin: strong but less polished than M04;
- facial contrast: moderate;
- masculinity: `HIGH`;
- femininity: `LOW`;
- grooming: natural stubble / short beard; textured hair; visible hairline;
- skin: visibly natural, small texture / minor imperfections allowed;
- body: `SOLID_ATHLETIC / ATHLETIC`;
- strength: moderate-high;
- shoulders: solid;
- aura: rugged / grounded / raw but controlled;
- distinctive 01: natural stubble / beard texture;
- distinctive 02: more characterful nose / brow / skin texture than M04 / M05;
- anti-template: do not polish into luxury-editorial male or exaggerate into unkempt / older appearance;
- age variants: adult / mature adult;
- model notes: image 2.5 can over-clean the face; retain natural skin / grooming cues; Banana2 Pro suits realism;
- tags: `aura: rugged, grounded, confident | body: solid | presentation: masculine/natural | age: adult/mature | grooming: rugged | contrast: medium-high`.

---

## M07 — Cold Elegant｜EVIDENCE-INFORMED

**Frontend alias:** `Cold & Elegant`

- adult age band: `YOUNG_ADULT / ADULT`;
- core signal: lean refinement + restrained editorial presence;
- face structure: elongated / refined, cleaner cheekbone line;
- angularity: moderate-high but narrow;
- eye / brow: narrower / deeper eye read, precise brow shape;
- nose: refined / clean bridge;
- lips: controlled definition;
- jaw / chin: narrower defined jaw, cleaner chin;
- facial contrast: moderate-high;
- masculinity: `MODERATE`;
- femininity: `LOW–MODERATE` visual refinement;
- grooming: sleek / structured short or medium-short hair; clean shave;
- skin: clean, natural, not glossy-plastic;
- body: `LEAN / LEAN_ATHLETIC`;
- strength: low-moderate;
- shoulders: lean / tailored silhouette;
- aura: restrained / elegant / distant / editorial;
- distinctive 01: elongated face + sharper cheekbone-to-jaw transition;
- distinctive 02: sleek structured hairstyle silhouette;
- anti-template: do not turn into M08 soft-androgynous face or M02 generic clean male;
- age variants: young adult / adult;
- model notes: image 2.5 strong for editorial clarity but may converge with idealized fashion face; preserve face length + eye depth;
- tags: `aura: cold, refined, composed, editorial | body: lean | presentation: polished/balanced | age: young-adult/adult | grooming: polished | contrast: medium-high`.

---

## M08 — Androgynous Beauty｜EVIDENCE-INFORMED / CONDITIONAL

**Frontend alias:** `Androgynous & Refined`

- adult age band: `YOUNG_ADULT / ADULT`;
- core signal: adult androgynous facial softness + refined styling;
- face structure: balanced oval / slightly narrow;
- angularity: low-moderate;
- eye / brow: open / elegant eye area, controlled brows;
- nose: refined / moderate;
- lips: moderate definition, slightly fuller allowed;
- jaw / chin: smooth / clean, still adult;
- facial contrast: moderate;
- masculinity: `LOW`;
- femininity: `MODERATE` visual softness;
- grooming: clean shave; refined medium-short / medium hair depending concept;
- skin: healthy natural texture;
- body: `LEAN`;
- strength: low-moderate;
- shoulders: adult lean frame;
- aura: delicate / artistic / refined;
- distinctive 01: softer jaw / cheek transition than M07;
- distinctive 02: slightly fuller lip / softer eye-brow architecture;
- anti-template: must remain clearly adult; do not enlarge eyes, shrink jaw or smooth skin into adolescent appearance;
- age variants: young adult / adult only when clearly adult;
- model notes: image models may over-youngify; include explicit adult age band + mature skin / bone cues;
- tags: `aura: artistic, refined, soft | body: lean | presentation: androgynous | age: young-adult/adult | grooming: refined | contrast: medium`.

---

## M09 — Warm Natural｜EVIDENCE-INFORMED

**Frontend alias:** `Warm & Natural`

- adult age band: `YOUNG_ADULT / ADULT`;
- core signal: approachable warmth + natural adult attractiveness;
- face structure: balanced / slightly shorter or fuller mid-face than M01;
- angularity: low-moderate;
- eye / brow: warm direct eye area, natural brow density;
- nose: natural / characterful rather than idealized;
- lips: relaxed, moderate;
- jaw / chin: moderate, less sculpted than M02;
- facial contrast: low-moderate;
- masculinity: `MODERATE`;
- femininity: `LOW`;
- grooming: natural textured hair; clean shave / light stubble;
- skin: visible natural texture / minor real-world variation;
- body: `LEAN_ATHLETIC / SOFT_NATURAL`;
- strength: moderate;
- shoulders: natural adult proportion;
- aura: warm / approachable / authentic / intimate;
- distinctive 01: natural brow / eye warmth with less polished facial contrast;
- distinctive 02: slightly fuller mid-face or softer jaw than M02;
- anti-template: do not polish into M01 refined beauty or turn into M03 fitness type;
- age variants: young adult / adult;
- model notes: Banana2 Pro particularly suitable; image 2.5 may overbeautify unless anti-template language keeps natural distinctiveness;
- tags: `aura: warm, natural, social | body: lean-athletic/soft-natural | presentation: balanced/natural | age: young-adult/adult | grooming: natural-textured | contrast: medium`.

---

# 7. Female-Presentation Archetypes

## F01 — Soft Feminine｜VALIDATED CORE

**Frontend alias:** `Soft & Feminine`

- adult age band: `YOUNG_ADULT / ADULT`;
- core signal: warmth + high femininity + soft facial structure;
- face structure: balanced oval / soft cheek-jaw transition;
- angularity: low;
- eye / brow: open eye area, softly shaped brows;
- nose: refined / balanced;
- lips: moderate-full, natural;
- jaw / chin: soft but adult-defined;
- facial contrast: moderate;
- femininity: `HIGH`;
- masculinity: `LOW`;
- hair / grooming: soft / natural or polished feminine hair; no fixed heritage-specific style;
- skin: healthy natural texture;
- body: `SOFT_NATURAL / LEAN`;
- strength: low-moderate;
- waist / curve: natural, flexible;
- aura: gentle / warm / romantic;
- distinctive 01: softer lower face + open eye area;
- distinctive 02: lower angularity than F02 / F05;
- anti-template: do not enlarge eyes / lips or shrink jaw into doll-like proportions;
- age variants: young adult / adult;
- model notes: clear in image 2.5; Banana2 Pro may under-express attractiveness unless face structure / skin / grooming are explicit;
- tags: `aura: soft, warm, romantic | body: soft-natural/lean | presentation: feminine/soft | age: young-adult/adult | grooming: refined/natural | contrast: medium`.

---

## F02 — Elegant Feminine｜VALIDATED CORE

**Frontend alias:** `Elegant & Refined`

- adult age band: `ADULT / YOUNG_ADULT`;
- core signal: refinement + composure + feminine structure;
- face structure: refined oval / slightly elongated;
- angularity: moderate;
- eye / brow: controlled eye shape, clean brow architecture;
- nose: defined / refined;
- lips: moderate definition;
- jaw / chin: clean, narrower and more structured than F01;
- facial contrast: moderate;
- femininity: `MODERATE_HIGH`;
- masculinity: `LOW`;
- grooming: polished hair / structured waves / sleek options depending identity;
- skin: healthy natural texture;
- body: `LEAN / LEAN_ATHLETIC`;
- strength: low-moderate;
- waist / curve: subtle / natural;
- aura: elegant / composed / sophisticated;
- distinctive 01: slightly elongated face + cleaner cheekbone line;
- distinctive 02: polished grooming silhouette;
- anti-template: do not collapse into F01 soft romantic or F06 cold editorial; warmth remains restrained but present;
- age variants: young adult / adult;
- model notes: image 2.5 strong; Banana2 Pro may make this ordinary unless face / grooming / aura are concrete;
- tags: `aura: refined, composed, elegant | body: lean | presentation: feminine/polished | age: adult/young-adult | grooming: polished | contrast: medium`.

---

## F03 — Athletic Beauty｜EVIDENCE-INFORMED

**Frontend alias:** `Athletic & Confident`

- adult age band: `YOUNG_ADULT / ADULT`;
- core signal: physical vitality + feminine confidence;
- face structure: balanced with slightly stronger cheek / jaw clarity;
- angularity: moderate;
- eye / brow: open / direct; natural defined brow;
- nose / lips: natural, not over-sculpted;
- jaw / chin: clear but not masculine-coded;
- facial contrast: moderate;
- femininity: `MODERATE_HIGH`;
- masculinity: `LOW–MODERATE` physical strength signal only;
- grooming: natural ponytail / waves / curls / structured hair only when visually compatible; no fixed sports hairstyle;
- skin: healthy natural texture;
- body: `ATHLETIC / LEAN_ATHLETIC`;
- strength: moderate;
- shoulder / waist / curve: athletic proportions, non-extreme;
- aura: healthy / active / confident;
- distinctive 01: stronger shoulder / torso athletic signal than F01 / F02;
- distinctive 02: slightly more defined cheek / jaw contour;
- anti-template: do not turn into fitness-body exaggeration or reduce femininity to makeup;
- age variants: young adult / adult;
- model notes: Banana2 Pro strong for real lifestyle; image 2.5 may over-sculpt body / face unless realism anchors remain;
- tags: `aura: confident, energetic | body: athletic | presentation: feminine/balanced | age: young-adult/adult | grooming: natural/clean | contrast: medium`.

---

## F04 — Mature Seductive｜EVIDENCE-INFORMED

**Frontend alias:** `Mature & Alluring`

- adult age band: `MATURE_ADULT / ADULT`;
- core signal: age-consistent maturity + feminine sensual confidence;
- face structure: mature balanced / slightly elongated;
- angularity: moderate;
- eye / brow: composed eye area with age-natural depth; defined brow;
- nose: mature / defined;
- lips: moderate-full but natural;
- jaw / chin: clean adult structure;
- facial contrast: moderate-high;
- femininity: `HIGH`;
- masculinity: `LOW`;
- grooming: polished / soft glamorous, age-appropriate;
- skin: age-natural healthy texture; fine lines / natural facial volume allowed;
- body: `CURVY_NATURAL / SOFT_NATURAL / LEAN` flexible;
- strength: low-moderate;
- waist / curve: visible but natural;
- aura: mature / sensual / composed;
- distinctive 01: age-natural eye / cheek / facial-volume cues;
- distinctive 02: controlled high-femininity grooming without F08 maximal glamour;
- anti-template: do not youthify or add exaggerated glamour makeup;
- age variants: adult → mature adult;
- model notes: image 2.5 can youngify; use adult age and anti-rebeautification; Banana2 Pro preferred for natural mature skin;
- tags: `aura: sensual, composed, mature | body: soft-natural/curvy/lean | presentation: feminine | age: mature | grooming: polished | contrast: high`.

---

## F05 — Dominant Beauty｜VALIDATED CORE

**Frontend alias:** `Confident & Powerful`

- adult age band: `ADULT / AGE_FLEX`;
- core signal: feminine beauty + assertive presence + structural control;
- face structure: slightly more angular / sculpted than F02;
- angularity: moderate-high;
- eye / brow: direct eye area, stronger brow architecture;
- nose: defined / clean;
- lips: moderate definition;
- jaw / chin: clear, slightly stronger lower face;
- facial contrast: moderate-high;
- femininity: `MODERATE_HIGH`;
- masculinity: `LOW–MODERATE` structure only;
- grooming: sleek / controlled / polished;
- skin: healthy natural;
- body: `LEAN_ATHLETIC / ATHLETIC`;
- strength: moderate;
- shoulder / waist / curve: balanced athletic feminine silhouette;
- aura: assertive / controlled / powerful;
- distinctive 01: stronger brow-eye + jaw control than F02;
- distinctive 02: athletic / upright silhouette rather than soft-natural presentation;
- anti-template: dominance comes from structure / posture / aura, not anger, scowl or masculinization;
- age variants: adult / age-flex;
- model notes: readable in both tested image models;
- tags: `aura: confident, dominant, controlled | body: lean-athletic/athletic | presentation: feminine/powerful | age: adult | grooming: polished | contrast: high`.

---

## F06 — Cold Beauty｜EVIDENCE-INFORMED

**Frontend alias:** `Cold & Striking`

- adult age band: `YOUNG_ADULT / ADULT`;
- core signal: refined facial structure + editorial restraint;
- face structure: elongated / sculpted / refined;
- angularity: moderate-high;
- eye / brow: precise / slightly narrow eye read, defined brow;
- nose: refined / clean;
- lips: controlled / moderate;
- jaw / chin: narrow-defined;
- facial contrast: moderate-high;
- femininity: `HIGH`;
- masculinity: `LOW`;
- grooming: sleek / structured / editorial;
- skin: clean natural texture, not waxy;
- body: `LEAN`;
- strength: low-moderate;
- waist / curve: subtle;
- aura: distant / controlled / editorial;
- distinctive 01: higher cheekbone / elongated-face signal;
- distinctive 02: sleek grooming + low smile baseline;
- anti-template: do not turn into angry / hostile expression or duplicate F05 dominance;
- age variants: young adult / adult;
- model notes: image 2.5 may create generic fashion face; preserve face length / cheekbone / eye-brow structure;
- tags: `aura: cold, refined, editorial | body: lean | presentation: feminine/polished | age: young-adult/adult | grooming: polished | contrast: medium-high`.

---

## F07 — Warm Natural｜EVIDENCE-INFORMED

**Frontend alias:** `Warm & Natural`

- adult age band: `YOUNG_ADULT / ADULT`;
- core signal: authentic warmth + low-performative grooming + healthy natural features;
- face structure: balanced / slightly softer or fuller mid-face;
- angularity: low-moderate;
- eye / brow: natural brow, warm direct eye area;
- nose: natural / characterful;
- lips: relaxed / moderate;
- jaw / chin: natural / moderate;
- facial contrast: low-moderate;
- femininity: `MODERATE_HIGH`;
- masculinity: `LOW`;
- grooming: loose natural hair / curls / waves / simple polished-natural depending identity;
- skin: visible natural skin texture / minor variation;
- body: `SOFT_NATURAL / LEAN / CURVY_NATURAL`;
- strength: low-moderate;
- waist / curve: flexible / non-extreme;
- aura: approachable / authentic / intimate;
- distinctive 01: lower facial contrast + natural brow / skin detail;
- distinctive 02: softer mid-face / jaw than F02;
- anti-template: do not glamorize into F08 or polish into F02;
- age variants: young adult / adult;
- model notes: Banana2 Pro well suited; image 2.5 needs anti-template / natural-skin anchors;
- tags: `aura: warm, natural, intimate | body: soft-natural/lean/curvy | presentation: feminine/natural | age: young-adult/adult | grooming: natural | contrast: medium`.

---

## F08 — Glamorous Bombshell｜VALIDATED CORE / MODEL-SENSITIVE

**Frontend alias:** `Glamorous & Bold`

- adult age band: `ADULT / MATURE_ADULT`;
- core signal: mature high-femininity glamour + overt confidence;
- face structure: balanced / sculpted with visible cheekbone / lip contrast;
- angularity: moderate;
- eye / brow: higher facial contrast, polished eye / brow frame;
- nose: defined / balanced;
- lips: fuller / strongly defined but realistic;
- jaw / chin: clean adult structure;
- facial contrast: high;
- femininity: `HIGH`;
- masculinity: `LOW`;
- grooming: glamorous / polished hair and makeup without identity redesign;
- skin: real skin texture under polished styling;
- body: `CURVY_NATURAL / FULLER_NATURAL / LEAN` depending user preference;
- strength: low-moderate;
- waist / curve: visibly feminine but non-extreme;
- aura: glamorous / confident / sensual;
- distinctive 01: stronger facial contrast + lip / cheekbone read;
- distinctive 02: fuller natural body option / higher visual glamour level;
- anti-template: keep adult realism and identity-specific structure; do not use generic hypersexual influencer face;
- age variants: adult / mature adult;
- model notes: validated in Banana2 Pro; repeated image 2.5 generation failure occurred in current runtime, so image 2.5 compatibility remains unverified rather than archetype-invalid;
- tags: `aura: glamorous, confident, sensual | body: curvy/fuller-natural/lean | presentation: feminine/glamorous | age: adult/mature | grooming: glamorous | contrast: high`.

---

## F09 — Playful Charmer｜EVIDENCE-INFORMED

**Frontend alias:** `Playful & Charming`

- adult age band: `YOUNG_ADULT / ADULT`;
- core signal: lively social presence + adult feminine charm;
- face structure: balanced / slightly shorter visual rhythm than F02 / F06;
- angularity: low-moderate;
- eye / brow: expressive eye area, slightly more animated brow shape;
- nose: natural / balanced;
- lips: relaxed / moderate-full;
- jaw / chin: soft-moderate adult structure;
- facial contrast: moderate;
- femininity: `MODERATE_HIGH`;
- masculinity: `LOW`;
- grooming: polished-natural / loose textured hair;
- skin: healthy natural;
- body: `LEAN / SOFT_NATURAL / ATHLETIC` flexible;
- strength: low-moderate;
- waist / curve: flexible;
- aura: playful / social / warm / confident;
- distinctive 01: expressive brow-eye relationship;
- distinctive 02: subtle natural asymmetry / dimple / freckle option when generated consistently;
- anti-template: playful does not mean childish; keep clearly adult face / body and restrained expression baseline;
- age variants: young adult / adult;
- model notes: model may over-express smile; archetype design should remain neutral enough for later Expression / Gaze routing;
- tags: `aura: playful, warm, social | body: flexible | presentation: feminine/balanced | age: young-adult/adult | grooming: polished-natural | contrast: medium`.

---

# 8. Archetype Differentiation Matrix

Use this before generation when two archetypes could collapse together.

## Male

### M01 vs M02

- M01: softer / slightly longer face, lower masculinity, leaner silhouette, refined-gentle aura.
- M02: clearer jaw angle, more balanced masculinity, lean-athletic body, clean-modern aura.

### M04 vs M05

- M04: power comes from broad jaw + muscular-athletic shoulders + high masculinity.
- M05: authority comes from mature facial depth + solid body + restrained adult composure; not maximal size.

### M05 vs M06

- M05: polished maturity, controlled grooming, refined authority.
- M06: textured skin / stubble / more characterful nose-brow structure, rugged groundedness.

### M07 vs M08

- M07: elongated / sharper / colder / more editorial masculine refinement.
- M08: softer jaw / softer eye-brow architecture / more androgynous adult beauty.

### M01 vs M09

- M01: polished refinement and cleaner facial architecture.
- M09: more natural facial variation, warmer eye-brow read, less polished grooming.

## Female

### F01 vs F02

- F01: softer lower face, warmer / more romantic, soft-natural body option.
- F02: slightly elongated / cleaner face, polished grooming, restrained elegance.

### F04 vs F08

- F04: maturity is primary; sensuality is composed and age-natural.
- F08: glamour / facial contrast / bolder styling is primary; can be adult or mature.

### F05 vs F06

- F05: assertive power + stronger brow / lower-face structure + athletic signal.
- F06: lean editorial refinement + elongated face + cooler restraint; not dominance.

### F02 vs F07

- F02: polished / structured / sophisticated.
- F07: natural skin / hair / lower facial contrast / warmer authenticity.

### F07 vs F09

- F07: calm, authentic, intimate warmth.
- F09: more expressive brow-eye / social-playful energy and stronger reaction potential.

---

# 9. Anti-Template System

## 9.1 Minimum Identity-Differentiating Payload

Never generate a partner from only:

`handsome man`

`beautiful woman`

`attractive model`

For every partner candidate, compile at least:

`ADULT AGE BAND + HERITAGE APPEARANCE + FACE ARCHITECTURE + BODY SIGNAL + HAIR / GROOMING + STYLE AURA + DISTINCTIVE FEATURE 01 + DISTINCTIVE FEATURE 02`

Attraction adjectives are optional support words, never the identity definition.

## 9.2 Candidate Separation Rule

When generating multiple candidates, deliberately vary at least **three structural axes**, not only styling:

- face length / width tendency;
- eye / brow character;
- nose character;
- jaw / chin structure;
- hair silhouette / grooming;
- body build / shoulder or curve signal;
- adult age band;
- style aura.

Do not create `same face + different hairstyle` candidate sets.

## 9.3 Natural Distinctiveness

Distinctive features should be subtle enough to remain attractive and plausible:

- slightly wider / narrower jaw;
- slightly longer / shorter face;
- deeper / more open eye area;
- brow-eye spacing;
- cheekbone prominence;
- nose bridge / tip character;
- lip proportion;
- hairline / texture;
- light stubble / short beard;
- freckles / small stable marks;
- adult natural skin texture;
- body shoulder / torso proportion.

Avoid exaggerated deformity or novelty features.

---

# 10. PARTNER_APPEARANCE_CARD｜Runtime Interface

Build this before partner generation. Unknown / irrelevant fields may be `FLEXIBLE`, `NEUTRAL`, or `NOT REQUIRED`.

```text
PARTNER_APPEARANCE_CARD

adult_age_band
gender_presentation
heritage_appearance
archetype_id
frontend_alias
status

core_attraction_signal
face_prototypicality
face_shape
face_length_width_tendency
face_softness_angularity
facial_adiposity
cheekbone_character

eye_shape
eye_size
eye_spacing
eye_depth
brow_shape
brow_density
brow_eye_spacing

nose_structure
nose_bridge_character
nose_tip_character
lip_structure
lip_fullness
jaw_structure
chin_structure
facial_contrast

masculinity_level
femininity_level

hair_color
hair_texture
hair_length
hair_silhouette
hairline_character
facial_hair
grooming_level

skin_tone
skin_undertone
skin_health
skin_texture

body_build
body_strength_signal
shoulder_width
waist_definition
hip_fullness
body_fullness

style_aura
distinctive_feature_01
distinctive_feature_02
anti_template_rule

matching_tags
model_notes
```

Do not send the full card to the image model automatically.

---

# 11. Prompt Compile Rule｜Minimum Useful Fields

Runtime selects:

`IDENTITY-RELEVANT FIELDS + ARCHETYPE-DIFFERENTIATING FIELDS + CURRENT-TASK FIELDS`

For a solo partner candidate, a compact prompt payload is usually:

`adult + gender presentation + heritage appearance + archetype face structure + body build + hair/grooming + 1–2 distinctive features + style aura + real skin`

Then apply the model adapter.

Do not include:

- the user's appearance;
- the matching rationale;
- why the partner is compatible with the user;
- couple action / scene unless the task actually requires a couple image.

`MATCHING RATIONALE → INTERNAL ONLY`

Apply `VISIBLE SUBJECT FILTER` before prompt delivery.

---

# 12. Model Adaptation

## image 2.5｜Partner Exploration / Canonical Identity

Strengths:

- high-attraction partner exploration;
- archetype differentiation;
- canonical partner identity assets.

Risks:

- beauty-template convergence;
- grey / muddy / cement-like rendering;
- rebeautification / age softening.

Minimum archetype compensation:

- keep the selected face architecture explicit;
- keep 1–2 distinctive features explicit;
- preserve adult age / face width / jaw / nose structure;
- natural real skin texture;
- clean / bright enough to avoid muddy rendering when observed;
- `distinct person, not generic beauty template` when convergence appears.

## Banana2 Pro｜Final Couple / Realism Route

Strengths:

- realistic skin / materials;
- natural heritage appearance;
- believable commercial candid photography.

Risks:

- partner can become too ordinary;
- generic `handsome / beautiful` under-expresses archetype.

Minimum archetype compensation:

- translate attraction into face / body / grooming / aura;
- preserve 1–2 distinctive features;
- use natural skin texture;
- keep prompt concise so color / camera language does not drown person design.

### Current model-sensitive archetypes

- `F08 Glamorous Bombshell`: Banana2 Pro validated; image 2.5 compatibility remains unverified in current runtime.
- `M08 Androgynous Beauty`: watch for over-youngification in either image model.
- `F04 Mature Seductive` / `M05 Mature Dominant`: watch for auto-youngification; maturity must stay structural.

Do not treat model sensitivity as evidence that the archetype itself is invalid.

---

# 13. Partner Candidate → Identity Lock Interface

Archetype output is a **design candidate**, not yet a locked specific person.

Flow:

`PARTNER_APPEARANCE_CARD → GENERATE PARTNER CANDIDATE → USER / RUNTIME APPROVES CANDIDATE → EXTRACT PARTNER_IDENTITY_CARD → PARTNER_REFERENCE_PACKAGE WHEN NEEDED`

When a candidate is approved, `partner-identity-lock.md` should preserve the **actual generated person's identity**, including the distinctive features that survived generation.

Do not keep regenerating from the abstract archetype after a specific partner is approved.

`ARCHETYPE = DESIGN SOURCE`

`APPROVED PARTNER IMAGE = SPECIFIC PERSON SOURCE`

---

# 14. Runtime Default Rules

If user gives an explicit partner type:

`USER PREFERENCE → nearest compatible ARCHETYPE_ID`

If user gives body / age / masculinity / femininity / energy preferences but no archetype:

`FILTER ARCHETYPE TAGS → matching-engine.md selects candidate route`

If user chooses `Surprise Me / No Preference`:

- do not infer ethnicity / orientation from the user photo;
- allow matching engine to propose a diverse, visually coherent candidate from the archetype set;
- avoid repeating the same archetype for every user.

If multiple candidates are generated:

- each candidate must be a distinct identity;
- each should differ on meaningful structural axes;
- do not present minor styling variants as different people.

---

# 15. Current Library Status

## Male presentation

9 archetypes:

- M01 Soft Refined — `VALIDATED CORE`
- M02 Clean Masculine — `VALIDATED CORE`
- M03 Athletic Sunlit — `EVIDENCE-INFORMED`
- M04 Power Masculine — `VALIDATED CORE`
- M05 Mature Dominant — `VALIDATED CORE`
- M06 Rugged Masculine — `EVIDENCE-INFORMED`
- M07 Cold Elegant — `EVIDENCE-INFORMED`
- M08 Androgynous Beauty — `EVIDENCE-INFORMED / CONDITIONAL`
- M09 Warm Natural — `EVIDENCE-INFORMED`

## Female presentation

9 archetypes:

- F01 Soft Feminine — `VALIDATED CORE`
- F02 Elegant Feminine — `VALIDATED CORE`
- F03 Athletic Beauty — `EVIDENCE-INFORMED`
- F04 Mature Seductive — `EVIDENCE-INFORMED`
- F05 Dominant Beauty — `VALIDATED CORE`
- F06 Cold Beauty — `EVIDENCE-INFORMED`
- F07 Warm Natural — `EVIDENCE-INFORMED`
- F08 Glamorous Bombshell — `VALIDATED CORE / MODEL-SENSITIVE`
- F09 Playful Charmer — `EVIDENCE-INFORMED`

Do not expand archetype count again unless real usage shows a meaningful attraction / casting gap that cannot be represented by current archetype + body + age + heritage + grooming parameters.
