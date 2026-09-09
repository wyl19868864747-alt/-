# Product Truth Lock

Purpose: create a reliable product source-of-truth before commercial creativity begins.

The lock does **not** mean “the model knows every fact.” It means every usable fact has evidence and uncertainty is never silently converted into certainty.

## Evidence States

- `CONFIRMED`: explicitly supplied in reliable user/product information or unambiguous source text.
- `VISIBLE`: clearly observable in the supplied reference asset.
- `SUPPORTED_INFERENCE`: reasonable for creative planning, but not safe to state as a product fact or claim.
- `UNKNOWN`: not established by current evidence.

Never promote `SUPPORTED_INFERENCE` or `UNKNOWN` into `CONFIRMED`.

## Lock Dimensions

### 1. Identity
- product / brand name when established
- SKU / variant / size / set
- package form and included items

### 2. Visual Identity
- silhouette and geometry
- relative proportions and scale cues
- visible color / finish
- visible material cues
- logo, label, typography, readable packaging text
- component layout and accessories

### 3. Mechanical / Physical State
- open / closed / sealed / assembled / disassembled state
- ports, buttons, lids, pumps, hinges, interfaces, moving parts
- contact surfaces and real operation path
- what must change state before use

### 4. Commercial Truth
- price and offer
- subscription / service terms
- included or excluded services
- verified selling points
- verified use conditions / audience restrictions
- real CTA destination or next action

### 5. Claim Boundaries
Treat the following as `UNKNOWN` unless explicitly supported:
- certification / approval
- medical or health outcomes
- exact performance numbers
- long-term durability
- precise sensory results
- sales volume / ratings / reviews
- comparative superiority

## Source Discipline

For every high-impact fact, retain its source role: `user_text`, `reference_asset`, `verified_product_info`, or `unknown`.

If two sources conflict, mark `CONFLICT` and do not silently merge them. Resolve only when the conflicting fact is required for the ad; otherwise omit it.

A product image alone can lock visible appearance and state. It cannot guarantee hidden specifications, exact dimensions, internal material, price, certification, or performance.

## Truth Card — internal minimum

```text
PRODUCT ID:
SKU / VARIANT:
REFERENCE ASSETS:
CONFIRMED FACTS:
VISIBLE FACTS:
SUPPORTED INFERENCES:
UNKNOWN / CANNOT CLAIM:
PHYSICAL STATE:
COMMERCIAL FACTS:
CTA FACT:
CONFLICTS:
```

## Hard Rules

`UNCERTAINTY MUST STAY UNCERTAIN`
`VISIBLE ≠ VERIFIED SPECIFICATION`
`CATEGORY KNOWLEDGE ≠ SKU FACT`
`REACTION ≠ OBJECTIVE PROOF`
`CREATIVE STYLE MUST NOT ALTER PRODUCT IDENTITY`

The goal is not to claim perfect omniscience. The goal is to prevent unsupported facts from entering Story, Hook, Proof, CTA, or Prompt.