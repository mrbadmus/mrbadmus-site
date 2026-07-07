# Physics — judgement-layer audit (distractor quality, exam register, tier integrity)

Stratified sample ~26 page-tier instances across all 8 physics units, both pathways/tiers, weighted to Higher/Triple calculation pages. Two corpus-wide structural comparisons run to ground the tier-integrity call.

## Corpus-wide structural facts (verified programmatically, not sampled)
- **Every physics page has exactly 2 quiz questions** (Combined: 103 tier-instances, Triple: 146 — all n=2). Rule 1 floor is 5, target 10.
- **Tier differentiation essentially absent.** For every page carrying both Foundation and Higher: `quiz` identical 50/50 (Combined) and 64/64 (Triple); `fifas` identical; `common_mistake` identical; `summary` identical. Only `higher_box` ever differs (13/50 Combined, 27/64 Triple). So on ~60-75% of pages, Foundation and Higher are byte-for-byte the same page with a different badge.

## Defect table (actual problems only)

| page | tier | dimension | severity | evidence |
|---|---|---|---|---|
| ALL physics pages | Higher & Triple | Tier integrity (R5) | major | Higher quiz/FIFA/common-mistake byte-identical to Foundation on 100% of pages. Systemic "same page, harder badge". |
| energy/power | higher | Tier integrity (R5) | major | Higher Q1 verbatim = Foundation Q1 ("A 2000 W heater is on for 3 minutes…") — no rearrangement/conversion escalation. |
| electricity/power-electricity | higher | Tier integrity (R5) | major | Higher = Foundation identical (R = 8 Ω carries 3 A + fuse Q); 2 plug-in Qs shared with Foundation. |
| particle-model/specific-latent-heat | higher | Tier integrity (R5) | major | Identical to Foundation; no mcΔθ+mL two-stage chain the topic supports. |
| particle-model/temperature-changes-shc | higher | Exam register (R1) | minor | Only 2 Qs, no Higher multi-step (g→kg / rearrangement) despite calc-heavy topic. |
| electricity/circuit-symbols | higher | Exam register (R1) | minor | "What does a circle with a cross inside represent?" — pure symbol-lookup, the exact defect Rule 1 names. |
| magnetism/poles-of-a-magnet | higher | Distractor/construct (R1) | major | Stem asks "key difference regarding magnetism" but correct option says *both* are permanent — no coherent answer; filler options. |
| waves/types-of-em-waves | higher | Exam register (R1) | minor | Both Qs lookup-style; distractors diagnostic though. |
| atomic-structure/structure-of-atom | higher | Distractor quality (R1) | minor | Option "0 — electrons are not part of the neutral atom" is filler; both Qs straight recall. |
| forces/contact-noncontact-forces | higher | Exam register (R1) | minor | "Which is a non-contact force?" lookup framing; distractors good. |
| energy/energy-resources | higher | Exam register (R1) | minor | "Which resource is renewable?" lookup-style; thin for Higher. |

## Patterns
1. **Distractor quality is genuinely strong — the corpus's best feature.** Calculation wrong-options are textbook diagnostic (forgot to square v, dropped the ½, minutes not seconds, squared R, V×I vs V÷I). Conceptual distractors mostly encode real misconceptions. Only a handful of true filler.
2. **Exam register good on calc/Triple pages, weaker on recall pages.** Lookup-style stems cluster on low-maths recall pages (circuit-symbols, em-waves, some atomic-structure) — minor, contained.
3. **Dominant defect is tier integrity, structural not per-page.** Higher/Triple inherit Foundation quiz+FIFA+common-mistake verbatim; only lever is an optional `higher_box` on ~⅓ of pages.
4. **Net:** physics doesn't need new distractors or a register rewrite — it needs Higher/Triple variants authored *as* Higher/Triple (rearrangement, conversion, two-formula chains, Triple depth) and the count lifted off 2. That plus count resolves the overwhelming majority of physics defects.
