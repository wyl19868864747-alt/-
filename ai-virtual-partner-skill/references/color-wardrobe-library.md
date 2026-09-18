# Color + Wardrobe Library｜情侣色彩与服装运行库

## Purpose

Convert scene + relationship intent into **physically assignable wardrobe and environment colors** without letting color styling overpower identity, action or scene logic.

This is a runtime asset library, not a color-theory article.

Runtime:

`SCENE FAMILY + RELATIONSHIP TEMPERATURE + TWO PERSON IDENTITIES → SELECT COLOR FAMILY → ASSIGN PERSON A / PERSON B / ENVIRONMENT / LIGHT → CHECK FACE + SKIN READABILITY → CHECK SCENE COMPATIBILITY → COMPILE IMAGE / VIDEO PROMPT`

Priority:

`PEOPLE / ACTION / SCENE > COLOR > LIGHTING DECORATION`

Color is an enhancement layer. The final prompt should use the **fewest executable color facts** that materially improve the image.

---

# 1. Core Separation Rule

Keep these separate:

- `COLOR FAMILY` = reusable color relationship / palette logic
- `WARDROBE ITEM` = the actual garment carrying a color
- `LIGHT COLOR` = color from daylight / practical lamp / city light / sunset
- `ENVIRONMENT COLOR` = color from wall / sofa / plants / sky / water / wood / stone / vehicle / architecture

Bad:

`romantic cinematic colorful palette`

Better:

`Person A wears a blush knit top; Person B wears deep navy; plant green and pale blue sky remain in the background; warm late-afternoon light falls naturally on both faces.`

Every important color should have a physical source.

---

# 2. Couple Wardrobe Assignment Logic

## 2.1 COORDINATED ≠ IDENTICAL

Default couple styling should look related, not uniform.

Avoid by default:

- same hue + same value + same garment type on both people;
- all black;
- all white;
- all grey;
- both people wearing the dominant background color;
- forced matching-couple uniforms unless explicitly requested.

Prefer:

- one dominant wardrobe color + one support color;
- related saturation / refinement level without literal matching;
- enough value or hue separation that both bodies remain readable;
- material variation such as knit vs jacket, linen vs denim, soft fabric vs structured outerwear;
- wardrobe that makes sense for the scene and intended movement.

Practical photography guidance also favors coordinated rather than identical outfits and wardrobe that matches the location / intended mood.

## 2.2 Person A / Person B Role Assignment

Do not assign color roles by gender.

Assign by visual need:

- `SOFTER / LIGHTER ROLE` — blush, cream, sage, soft blue, muted sand, pale olive;
- `ANCHOR / DEEPER ROLE` — navy, deep teal, burgundy, espresso, warm charcoal, dark olive;
- `ACCENT ROLE` — terracotta, rust, wine, muted coral, cobalt accent, olive, denim;
- `NEUTRAL BUFFER` — cream, camel, stone, warm grey, soft black used selectively.

Either person may carry any role.

## 2.3 Value Separation

If both people have similar hair / wardrobe darkness, separate them through one of:

- lighter garment value on one person;
- different hue family;
- different material reflectance;
- directional light edge;
- background separation.

Do not solve separation by changing identity skin tone.

## 2.4 Background Competition Rule

If the background already carries a strong hue, do not place both people in the same competing hue.

Examples:

- cool-blue city background → avoid two blue outfits; use burgundy / deep green / warm neutral on at least one person;
- green garden → avoid both people in foliage-matching green; introduce cream / navy / rust / soft blue;
- terracotta interior → avoid both people in orange / rust; use sage / cream / navy / denim support.

---

# 3. Skin / Face Readability Guard

User and partner stable skin tone remain identity attributes. Color styling may not redefine them.

Do not infer ethnicity / nationality from appearance and do not encode race-based color rules.

Protect face readability by avoiding:

- strong green light covering the full face;
- strong blue light shifting stable skin tone;
- orange sunset light turning all skin uniformly orange;
- red / magenta neon crossing eyes / nose / mouth as a default;
- blown white backlight creating milky haze over faces;
- wardrobe color spill strong enough to contaminate facial identity.

Mixed light is allowed when the face still reads naturally. Real photography practice treats unwanted green / blue / yellow casts as a color-balance problem rather than a desirable skin transformation.

Default:

- keep face / skin under neutral, warm-neutral or believable mixed ambient light;
- let stronger color live mainly in background, wardrobe, practical lamps and environmental accents;
- keep eye / nose / mouth structure readable before increasing palette drama.

---

# 4. Status Labels

- `VALIDATED CORE` — direct project output / production evidence supports default use.
- `EVIDENCE-INFORMED` — established commercial / lifestyle photography logic and low enough risk for production.
- `CANDIDATE` — useful but not yet a default.
- `HIGH-CONTROL / CONDITIONAL` — palette can work but requires careful skin / model / scene control.

Do not run synthetic color benchmarks unless a real routing decision depends on them.

---

# 5. Color Families

## CW01 — GOLDEN TERRACE｜VALIDATED CORE

**Best relationship temperature:** Romantic / Flirty / Sweet / Playful

**Best scenes:** S04 Golden Terrace; also S14 Golden-Hour Walk, S19 Resort / Coastal Terrace when environment supports it.

**Person A color role:** peach / blush / muted coral / warm cream.

**Person B color role:** deep navy / dark teal / warm charcoal / espresso.

**Environment color sources:** plant green, pale blue sky, warm stone / wood / railing surfaces.

**Light color:** warm golden natural late-afternoon light; keep face exposure natural rather than orange.

**Contrast logic:** soft warm subject color + deep anchor subject color + green / blue environment creates readable separation without literal matching.

**Skin readability:** keep warm light directional / soft; avoid placing low sun directly behind both faces.

**Hair / wardrobe separation:** dark hair benefits from blush / cream / medium-value fabric or warm rim separation; deep navy should not merge into a dark background.

**Image model risk:** Banana2 Pro may go overly bright / hazy if golden light is over-described; keep compensation short. image 2.5 can turn warm tones muddy if overall exposure is too dark.

**MiniMax H3 continuity value:** VERY HIGH — wardrobe / sky / plant colors are simple and stable across cuts.

**Project evidence:** directly approved for strong realism, couple feel and flirtatious intimacy.

---

## CW02 — NIGHT CITY WINDOW｜VALIDATED CORE

**Best relationship temperature:** Romantic / Flirty / Passionate / Protective

**Best scenes:** S05 Night City Window; also S10 Rooftop Evening, S11 Street Night, S12 Bar / Lounge, S13 Hotel Window when lighting geometry matches.

**Person A color role:** burgundy / wine / warm neutral / muted plum.

**Person B color role:** forest green / deep teal / warm charcoal / espresso.

**Environment color sources:** cool-blue city background, dark window, warm amber floor / table lamp, dark wood / metal.

**Light color:** warm amber practical on faces + cool blue city ambient in background; do not reverse this by putting hard blue over facial landmarks.

**Contrast logic:** warm/deep wardrobe against cool city depth; one person can carry wine while the other carries teal / charcoal for clear body separation.

**Skin readability:** faces remain warm-neutral enough to preserve stable skin tone; blue / magenta stays mostly background / edge light.

**Hair / wardrobe separation:** dark hair + dark clothing requires amber edge / background contrast; avoid two dark-blue outfits against blue city background.

**Image model risk:** low-light Banana2 Pro can become too smooth / hazy; image 2.5 can become grey / muddy. Avoid excessive neon terms.

**MiniMax H3 continuity value:** VERY HIGH — directly production-proven in Man × Man H3 clip; keep wardrobe colors and warm/cool direction unchanged across cuts.

---

## CW03 — SAGE & TERRACOTTA HOME｜VALIDATED CORE

**Best relationship temperature:** Sweet / Romantic / Protective / Playful

**Best scenes:** S06 Sage & Terracotta Home; also S02 Sofa Corner, S07 Kitchen Morning, S08 Dining / Counter when decor supports it.

**Person A color role:** sage / muted olive / cream.

**Person B color role:** terracotta / rust / warm camel / deep navy support.

**Environment color sources:** cream wall, natural wood, sage textile / plant tones, terracotta ceramics / cushions.

**Light color:** soft window daylight + subtle warm practical.

**Contrast logic:** low-to-medium saturation earth colors with one cooler green family and one warmer clay family.

**Skin readability:** keep green in wardrobe / decor, not as face light; practical light should stay warm-neutral rather than orange.

**Hair / wardrobe separation:** dark hair reads well against cream / sage; light hair needs enough value separation from cream walls through terracotta / olive / navy wardrobe.

**Image model risk:** overusing muted earth tones can become flat / beige; keep one clear green or terracotta anchor.

**MiniMax H3 continuity value:** HIGH — simple home palette is stable across interior cuts.

---

## CW04 — WARM COASTAL｜EVIDENCE-INFORMED

**Best relationship temperature:** Sweet / Romantic / Protective

**Best scenes:** S16 Beach / Waterfront, S19 Resort / Coastal Terrace, S20 Scenic Overlook.

**Person A color role:** soft sand / cream / pale blue / muted coral.

**Person B color role:** navy / olive / camel / denim blue.

**Environment color sources:** sky, water, sand / stone, coastal greenery, pale architecture.

**Light color:** sunrise / golden-hour / open-shade daylight.

**Contrast logic:** soft warm neutral + restrained blue / navy + natural coastal background.

**Skin readability:** keep reflective water / sky from washing faces blue; use side / front-side daylight.

**Hair / wardrobe separation:** avoid pale-on-pale when both hair and architecture are light; introduce navy / olive / medium-value garment.

**Image model risk:** blown sky / water highlights can create haze; keep exposure natural.

**MiniMax H3 continuity value:** HIGH if wind is mild and wardrobe remains simple.

---

## CW05 — CLEAN MORNING｜EVIDENCE-INFORMED

**Best relationship temperature:** Sweet / Playful / Romantic

**Best scenes:** S07 Kitchen Morning, S02 Sofa Corner, S17 Outdoor Café.

**Person A color role:** cream / pale blue / soft sage / light denim.

**Person B color role:** camel / navy / olive / muted rust accent.

**Environment color sources:** daylight, white / cream wall, wood counter, ceramic mugs, plants.

**Light color:** clean morning daylight with minimal warm practical support.

**Contrast logic:** light airy environment + one medium/deep wardrobe anchor.

**Skin readability:** do not let white walls / windows overexpose faces; preserve natural skin texture.

**Hair / wardrobe separation:** dark hair against white wall is readable; light hair may need navy / olive garment or wood background.

**Image model risk:** Banana2 Pro can become too white / milky; explicitly avoid white haze only if observed.

**MiniMax H3 continuity value:** HIGH.

---

## CW06 — GOLDEN OUTDOOR｜EVIDENCE-INFORMED

**Best relationship temperature:** Romantic / Sweet / Playful / Flirty

**Best scenes:** S14 Golden-Hour Walk, S15 Park / Garden, S18 Urban Walk, S20 Scenic Overlook.

**Person A color role:** rust / muted coral / cream / olive.

**Person B color role:** navy / denim / camel / deep green.

**Environment color sources:** foliage, path, stone, sky, architecture.

**Light color:** low-angle warm daylight.

**Contrast logic:** one warm wardrobe accent + one darker cooler / neutral anchor against natural greens / sky.

**Skin readability:** avoid orange saturation across the entire face; keep warmth in light edge / environment rather than skin recoloring.

**Hair / wardrobe separation:** do not put dark-haired subject in black against dark trees without light edge.

**Image model risk:** excessive `golden` wording can flatten everything into orange.

**MiniMax H3 continuity value:** VERY HIGH for walking / turn / pull-in sequences.

---

## CW07 — URBAN CASUAL｜EVIDENCE-INFORMED

**Best relationship temperature:** Playful / Flirty / Sweet / Romantic

**Best scenes:** S11 Street Night, S18 Urban Walk / Neighborhood Date, S21 Car-Side / Arrival.

**Person A color role:** denim / cream / muted green / burgundy accent.

**Person B color role:** dark navy / brown / warm charcoal / camel.

**Environment color sources:** brick, concrete, storefront materials, street furniture, vehicle paint when present.

**Light color:** daylight / early-evening practicals.

**Contrast logic:** casual materials with one richer accent; avoid both people in grey-on-grey city camouflage.

**Skin readability:** keep colored signage off the central facial plane.

**Hair / wardrobe separation:** use garment value separation from brick / concrete background.

**Image model risk:** too many storefront colors / logos create noise; keep background secondary.

**MiniMax H3 continuity value:** HIGH.

---

## CW08 — REFINED HOTEL｜EVIDENCE-INFORMED

**Best relationship temperature:** Romantic / Flirty / Passionate

**Best scenes:** S13 Hotel Window / Hotel Lifestyle; S12 Bar / Lounge when simplified.

**Person A color role:** burgundy / cream / soft black / deep plum.

**Person B color role:** navy / espresso / dark olive / camel.

**Environment color sources:** cream / taupe upholstery, wood, brass, stone, curtain, city / landscape window.

**Light color:** warm-neutral practical + window / dusk ambient.

**Contrast logic:** deep refined wardrobe + restrained warm interior, with one lighter garment / surface preserving separation.

**Skin readability:** practical light must not become strong yellow / orange cast.

**Hair / wardrobe separation:** dark wardrobe against dark hair requires lighter wall / curtain / edge light.

**Image model risk:** can drift into overly dark luxury / muddy brown; keep faces brighter than background.

**MiniMax H3 continuity value:** HIGH.

---

## CW09 — GARDEN / NATURE｜EVIDENCE-INFORMED

**Best relationship temperature:** Sweet / Romantic / Protective / Playful

**Best scenes:** S15 Park / Garden, S14 Golden-Hour Walk, S19 Resort / Coastal Terrace with greenery.

**Person A color role:** cream / pale blue / blush / muted lavender / rust accent.

**Person B color role:** navy / camel / olive used only if it does not merge with foliage / soft charcoal.

**Environment color sources:** green foliage, flowers, stone / wood path, sky.

**Light color:** open shade / late-afternoon natural light.

**Contrast logic:** keep at least one wardrobe color outside the dominant foliage green family.

**Skin readability:** avoid green reflected light dominating jaw / lower face.

**Hair / wardrobe separation:** dark hair + dark green wardrobe against foliage is discouraged unless cream / sky separation is strong.

**Image model risk:** image 2.5 may muddy greens; Banana2 Pro may make foliage too bright if heavily described.

**MiniMax H3 continuity value:** HIGH.

---

## CW10 — PLAYFUL CAFÉ｜EVIDENCE-INFORMED

**Best relationship temperature:** Playful / Sweet / Romantic

**Best scenes:** S17 Outdoor Café, S08 Dining / Counter, S07 Kitchen Morning.

**Person A color role:** soft blue / muted coral / cream / sage.

**Person B color role:** denim / navy / camel / olive.

**Environment color sources:** awning, wood / metal furniture, cups, pastry, plants, street background.

**Light color:** open shade / storefront ambient / warm pendant indoors.

**Contrast logic:** approachable mid-saturation palette; one person carries a soft accent while the other carries a stable neutral / deep tone.

**Skin readability:** prevent colorful awning / signage from casting saturated stripes across faces.

**Hair / wardrobe separation:** keep table / chair colors below the main body silhouette.

**Image model risk:** prop and color clutter can distract from the couple.

**MiniMax H3 continuity value:** MEDIUM–HIGH.

---

## CW11 — ELEVATED NEUTRAL｜EVIDENCE-INFORMED / CONDITIONAL

**Best relationship temperature:** Protective / Romantic / Refined Sweet

**Best scenes:** S01 Window-Side, S02 Sofa Corner, S13 Hotel Lifestyle, S20 Scenic Overlook.

**Person A color role:** cream / stone / camel / taupe.

**Person B color role:** warm charcoal / espresso / navy / soft black.

**Environment color sources:** natural wood, stone, linen, off-white wall, sky / window.

**Light color:** neutral / warm-neutral natural light.

**Contrast logic:** use value / material contrast because hue contrast is restrained.

**Skin readability:** protect against all-beige washout; skin must remain distinct from wall / clothing.

**Hair / wardrobe separation:** dark hair with charcoal needs lighter environment; light hair with cream needs darker garment / background anchor.

**Image model risk:** HIGHER risk of flat / generic / overly conservative output, especially given project history with neutral overuse.

**MiniMax H3 continuity value:** HIGH but visual distinctiveness is lower.

**Guard:** do not default-route every couple here.

---

## CW12 — RICH EDITORIAL｜CANDIDATE / HIGH-CONTROL

**Best relationship temperature:** Flirty / Passionate / Fashion-forward Romantic

**Best scenes:** S05 Night City Window, S10 Rooftop Evening, S12 Bar / Lounge, S13 Hotel Lifestyle.

**Person A color role:** wine / plum / deep cobalt accent / rich cream.

**Person B color role:** dark teal / forest / espresso / controlled black.

**Environment color sources:** practical lamps, city lights, upholstery, metal / glass, architectural surfaces.

**Light color:** controlled warm practical + restrained cool / colored background accents.

**Contrast logic:** richer saturation lives in wardrobe / background accents while faces stay natural.

**Skin readability:** mandatory guard — no saturated magenta / blue / green wash over central facial landmarks.

**Hair / wardrobe separation:** use edge / background value separation when both wardrobe and hair are dark.

**Image model risk:** higher; image 2.5 may turn saturated dark colors muddy, Banana2 Pro may over-brighten practicals or create haze.

**MiniMax H3 continuity value:** MEDIUM — only use when the approved first frame already established the palette successfully.

---

# 6. Relationship Temperature → Color Routing

Do not use simplistic mappings such as `Passionate = red` or `Sweet = pink`.

Route by relationship temperature **plus scene**.

## Sweet

Prefer:

- CW03 Sage & Terracotta Home
- CW05 Clean Morning
- CW09 Garden / Nature
- CW10 Playful Café
- CW04 Warm Coastal

## Romantic

Prefer:

- CW01 Golden Terrace
- CW03 Sage & Terracotta Home
- CW04 Warm Coastal
- CW06 Golden Outdoor
- CW08 Refined Hotel
- CW11 Elevated Neutral when the user wants restraint

## Flirty

Prefer:

- CW01 Golden Terrace
- CW02 Night City Window
- CW06 Golden Outdoor
- CW07 Urban Casual
- CW08 Refined Hotel
- CW12 Rich Editorial only when skin / model stability is strong

## Passionate

Prefer palettes with clear subject separation and deeper wardrobe values, not automatic red:

- CW02 Night City Window
- CW08 Refined Hotel
- CW12 Rich Editorial under controlled lighting
- CW01 Golden Terrace can also support passion through action rather than darker color

## Playful

Prefer:

- CW05 Clean Morning
- CW06 Golden Outdoor
- CW07 Urban Casual
- CW09 Garden / Nature
- CW10 Playful Café

## Protective

Prefer:

- CW03 Sage & Terracotta Home
- CW04 Warm Coastal
- CW09 Garden / Nature
- CW11 Elevated Neutral
- CW02 Night City Window when a quiet night mood is desired

---

# 7. Scene → Color Compatibility Matrix

Use Scene ID first; then choose among compatible color families.

- **S01 Window-Side** → CW01, CW05, CW08, CW11
- **S02 Sofa Corner** → CW03, CW05, CW11
- **S03 Bedroom Edge** → CW03, CW08, CW11; avoid heavy editorial color by default
- **S04 Golden Terrace** → CW01 primary; CW06 secondary
- **S05 Night City Window** → CW02 primary; CW08 / CW12 secondary
- **S06 Sage & Terracotta Home** → CW03 primary
- **S07 Kitchen Morning** → CW05 primary; CW03 / CW10 secondary
- **S08 Dining / Counter** → CW10 / CW03 / CW08 depending venue
- **S09 Hallway / Doorway** → CW07 / CW08 / CW11 depending architecture
- **S10 Rooftop Evening** → CW02 / CW07 / CW12 / CW06 at earlier dusk
- **S11 Street Night** → CW07 primary; CW02 / CW12 secondary
- **S12 Bar / Lounge Corner** → CW08 / CW02 / CW12
- **S13 Hotel Window / Lifestyle** → CW08 primary; CW11 / CW02 secondary
- **S14 Golden-Hour Walk** → CW06 primary; CW01 / CW09 secondary
- **S15 Park / Garden** → CW09 primary; CW06 / CW04 secondary
- **S16 Beach / Waterfront** → CW04 primary; CW06 secondary
- **S17 Outdoor Café** → CW10 primary; CW07 / CW05 secondary
- **S18 Urban Walk / Neighborhood Date** → CW07 primary; CW06 / CW10 secondary
- **S19 Resort / Coastal Terrace** → CW04 primary; CW01 / CW08 secondary
- **S20 Scenic Overlook** → CW04 / CW06 / CW11
- **S21 Car-Side / Arrival** → CW07 primary; CW02 at night; vehicle paint must not dominate both people

Reject a palette if its physical sources do not exist in the selected scene.

---

# 8. Model Adaptation

## Banana2 Pro

Use minimum effective color language.

Priorities:

- preserve subject / relationship description first;
- assign 1 color role to each person + 2–3 environment sources at most;
- avoid overexposure / pale white haze;
- do not stack long contrast / white-balance instructions that flatten the image;
- use real skin texture and believable color rather than heavy color grading language.

## image 2.5

Guard against:

- grey / muddy / cement-like rendering;
- gloomy dark grading;
- dirty low-saturation color mixtures.

Prefer:

- one clear anchor hue;
- brighter / cleaner exposure;
- readable skin and wardrobe separation;
- concise color assignment.

## MiniMax H3

The approved first frame owns color continuity.

Across cuts:

- wardrobe color does not change;
- garment type does not change;
- scene dominant colors remain stable;
- warm/cool direction does not flip;
- practical lamp / city / sky color source remains in the same spatial direction;
- do not recolor skin to create mood.

Video color instruction should usually be continuity language, not a new palette design.

---

# 9. Prompt Compile Rule

Final prompt order:

`IDENTITY / SUBJECT → RELATION ACTION → SCENE → MINIMAL COLOR ASSIGNMENT → REALISM / MODEL COMPENSATION`

Good compact compile:

`Person A wears a muted blush knit top; Person B wears deep navy. Plant green and pale blue sky remain behind them under warm late-afternoon natural light. Keep both faces naturally exposed and preserve their original skin tones.`

Do not expand this into a long color essay if the same result can be achieved in one or two sentences.

---

# 10. Current Production Defaults

If no explicit color preference exists:

- S04 Golden Terrace → CW01
- S05 Night City Window → CW02
- S06 Sage & Terracotta Home → CW03
- S14 Golden-Hour Walk → CW06
- S17 Outdoor Café → CW10
- S18 Urban Walk → CW07
- S19 Resort / Coastal Terrace → CW04
- S13 Hotel Lifestyle → CW08

If scene and wardrobe are both unspecified, scene selection happens first. Color never chooses an incompatible scene.

---

# Editorial Wardrobe / Material Guard

When `editorial-intimacy-dna.md` selects VT2 / VT3 / VT4, wardrobe should not default to conservative lifestyle styling.

For V2+ sensual editorial routes, avoid using both adults in:
- bulky cream knitwear;
- loose beige overshirts;
- fully covered high necklines;
- identical soft textures;
- cream-on-cream bodies against a cream room.

Prefer at least one visible body-line or material cue:
- open neck / collarbone;
- fitted waist;
- shoulder / upper-back line;
- low-back / open-back silhouette;
- leg line / slit when scene-compatible;
- fitted fine-gauge knit;
- silk / satin / body-skimming jersey;
- crisp open-collar shirt;
- tailored dark layer;
- soft leather accent;
- structured contrast between Person A and Person B.

High-value editorial color logic:

`SKIN + ONE DARK ANCHOR + ONE SOFT SUPPORT + ONE PHYSICAL LIGHT SOURCE`

This does not replace the existing palette families; it changes how wardrobe and material are assigned inside them.

Do not equate “high-end” with all-black, all-white, or more colors.
