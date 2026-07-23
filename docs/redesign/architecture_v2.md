# Bonding v2 — Canonical Architecture

**Status:** law for all bonding builds from Phase 0 onward. Synthesized from `council_bonding_review.md` §3 (page-structure philosophy), §5 (text strategy), §6 (component library) and §7 (phased plan). Where this document and an older port map disagree, this document wins. Where this document and the council record disagree, the council record wins — flag the conflict, don't improvise.

**Standing constraints (unchanged, restated):** the 8 frozen science fields (`quiz`, `matching`, `common_mistake`, `key_note`, `theory`, `fifas`, `higher`, `triple_only`) are never edited — interactives are built *from* frozen science, and any net-new activity content is flagged ⚑ for Mide's examiner review. Vanilla JS, no build step. Locked design tokens, WCAG AA, full keyboard access, reduced-motion support. Tier/pathway gating as in the generator. Generator determinism (two runs → byte-identical output). AQA accuracy. Approved examiner tips: placement may move, text never.

---

## 1. The eight laws

Every bonding page is judged against these. A page that violates one is a defect, not a style choice.

**Law 1 — Demand-driven structure.**
One design language, variable architecture. Tokens, type ramp, tone-tints (green = conducts/favourable, red = limit/error, amber = examiner/aside), the instrument-panel anatomy (head / tinted callout / viz / dark mono strap) as the only panel shape, quiz mechanics, and the identical end-matter ritual (stars → AI → prev/next) are fixed. Everything else — which instruments are mounted, where, at what scale, in what order — is decided by the topic's dominant cognitive demand, via the architecture families in §2. Two pages with identical block lineups should be a coincidence of need, never a default.

**Law 2 — The 150-word encode–act spine.**
Never more than ~150 words of continuous prose (lead + one block) before the student must commit to something — a prediction, a construction, a classification, or a written answer. A page is a chain of encode→act cycles ending in mixed consolidation, not encode-everything-then-test-everything. Any static block whose content an interactive now teaches is deleted from the composition (replace, don't stack; the frozen text itself is untouched — rendering selection only, listed at the gate).

**Law 3 — Three interactive scales, placed at demand peaks.**
Per page: **one flagship lab** (L, one max), **one–two mid-size activities** (M), and **micro-widgets** woven into the prose ad lib — plus the quiz ladder. Three committed-response interactives above the quiz is the ceiling; a page that is all instruments has no rhythm either. Each instrument sits at the point in the page where its concept's demand peaks, not parked at the top.

**Law 4 — Predict before reveal.**
No interactive shows a verdict the student hasn't wagered on. Every stateful reveal — a toggle, a force button, a heat ramp — is gated by a committed prediction (commit-chip row), and the reveal answers the prediction right/wrong in tone tokens. No passive animation; commitment is what converts watching into learning.

**Law 5 — Watch/do duality.**
A linear worked sequence is legitimate *only* when paired with a do-it-yourself counterpart (FIFA's worked/practice dual mode, generalised). Steppers stay as the worked mode; the practice mode makes the student produce the same artifact. Neither ships alone.

**Law 6 — Production-ending exam ladder.**
Every page ends in the four-rung ladder: ① recall check → ② apply (deduce/calculate) → ③ explain (chain assembly) → ④ extended response (write-then-self-mark), tariff-tagged, with per-question persistence and "retry my misses". Recognition (MCQ) feeds the ladder; production tops it — because AQA pays for production. The misconception-tagged distractor bank is preserved and mined, never gamified away.

**Law 7 — One design language.**
The visual system stays coherent while architecture varies: mono kickers replace emoji section titles; callouts never sit adjacent; max one amber element per screen; dark surfaces max two per page; drawn-atom primitives (shared module) do content labour, not emoji; one mid-page breather moment (verdict strap / display-scale fact / dark surface). Variety in arrangement, unity in material.

**Law 8 — Persistence and return loops.**
Scores persist (`quiz_best_<page>`, `lab_best_<page>` in localStorage), the end screen shows score + delta vs best, and "retry my misses" rebuilds only what was missed. Never punish: no streaks, no guilt copy, timers opt-in only, no page-level leaderboards, no XP. Low scores get diagnosis + a route; stars respond with a route, not congratulations.

---

## 2. The five architecture families

Each of the 12 pages belongs to one family. The family fixes the page's skeletal rhythm; the lab catalogue (council §4) fills in the instruments.

### PROCESS — "a mechanism unfolds in steps"
*Pages: **ionic-bonding**, **covalent-bonding**, **polymers**.*
The topic is a procedure (transfer electrons; share pairs; open the double bond and chain). Skeleton: lead → worked stepper with predict-gates at each step (Law 4 + 5) → do-mode construction of the same artifact (electron drag / shared-pair builder / chain builder) → properties that follow from the mechanism → exam ladder. The static step-sequence block that narrates what the stepper shows is deleted (Law 2). Common Mistake sits at the step where the error is born (e.g. "the transfer IS the bond" at the attraction step).

### MODEL — "one structure explains everything"
*Pages: **states-of-matter**, **ionic-compounds**, **metallic-bonding**.*
The topic is a single physical model (particle motion; the lattice; the electron sea) whose parameters drive all behaviour. Skeleton: lead → flagship parameter-sweep instrument (heating curve / heat-the-lattice / electron-sea workbench) with predict-gates at each regime change → property blocks each anchored back to the model → exam ladder. The model instrument is the page's centre of gravity; prose orbits it.

### CONTRAST — "two things, one discriminating difference"
*Pages: **giant-covalent-structures**, **metals-alloys**, **properties-ionic-compounds**, **properties-small-molecules**.*
The topic is a comparison (diamond vs graphite; pure vs alloy; solid vs molten; within vs between). Skeleton: lead → predict-gated A/B instrument (two-state compare, force test) → parallel compare-cards as the static reference → explanation-chain builders that force the *linked* comparison AQA's 6-markers reward → exam ladder. These four pages own the unit's three 6-mark bankers; their ladders are the heaviest.

### TRIAGE — "decide which category, fast"
*Page: **chemical-bonds**.*
The topic is a decision rule (metal + non-metal → ionic…). Skeleton: lead → decision instrument (bond decider: pick elements, commit a prediction, watch the resolution) → the 3-way compare reference → classification drills (bins, speed sort, mystery substance) at rising stakes → exam ladder. The page is the unit's front door and ends with the visual unit map.

### QUANTITATIVE — "a calculation carries the concept"
*Page: **nanoparticles**.*
The topic is scale arithmetic (SA:V, powers of ten). Skeleton: lead → scale instrument (powers-of-ten zoom) → the concept-calculation pair: cube-splitting sim feeding directly into FIFA worked/practice (Law 5) — FIFA directly after the sim, never after the matching → uses/risks with the evaluate ladder → exam ladder with standard-form production. ⚑ Known spec gaps (PM10/PM2.5, size-range recall, 11-question quiz, spec-pill number) are gated on Mide.

---

## 3. Text strategy (council §5, binding)

1. **150-word rule** as Law 2 — lead stays, first commitment lands immediately after it.
2. **Micro-interactions replace paragraphs that describe actions.** Any steps-block an interactive animates is deleted from the composition; any "draw/deduce/predict X" prose becomes the thing itself.
3. **Callout discipline:** never two callout boxes adjacent — separate with plain prose, a diagram, or a micro-widget; max one amber per screen; dark surfaces max two per page.
4. **Common Mistake** moves to the moment the error is born and becomes spot-the-flaw where possible.
5. **Examiner Tip splits:** exam technique → directly above the quiz; content-specific coaching → the success state of the relevant interactive. Text never changes (approved tips), placement only.
6. **Key Note:** last, static, restyled as a photographable revision card (index-card styling, mono type, inset surface) with an optional cover-and-recall toggle. Frozen text untouched.
7. **Quiz presentation:** exam paper, not cards — one continuous panel, hanging mono numbers (CSS counters), hairline rules, compact lettered options; chunked Warm-up / Exam standard / Stretch (4+4+4) with later sets behind `<details>`; sticky progress chip; per-set check; 2–3 retrieval questions relocated inline as checkpoint micro-quizzes after the theory block they test (same frozen questions).
8. **Tone pass (copy, not science):** diagnostic wrong-answer explanations stay verbatim; one emoji per message max; no exclamation stacking; low-score messages are diagnosis + route naming the actual weak area; stars respond with a route.
9. **Section headers:** mono kicker voice, not emoji titles; emoji survive only where irreplaceable in content.

---

## 4. Component tiers (council §6, build order)

### Tier 0 — fixes and extractions (Phase 0, MRB-132; before anything new)
| Component | Role |
|---|---|
| **TapMatch** (`shared/tap-match.js`) | Matching engine replacement using the bins input model (tap-select, tap-place, real buttons, Enter/Space, browser Fisher–Yates shuffle of both columns, grading by mapping). Retires HTML5 DnD — which is dead on touch — from all bonding output. |
| Bins keyboard fix | Drop-targets become buttons: tabindex, Enter/Space, aria-pressed. |
| Hero aria pass | `role="img"` + per-state generated `aria-label` on every hero viz; every `@keyframes` loop gated on `prefers-reduced-motion` (`mrbEDrift` explicitly); static fallback where missing. |
| **quiz.js extraction** (`shared/quiz.js`) | The inlined quiz engine centralised; generator emits script tags, not blobs. Behaviour-identical (rendered-DOM verified). |
| Score persistence | `quiz_best_<stId>` / `lab_best_<stId>`; delta at quiz end; "retry my misses"; never punish. |

### Tier 1 — retrofit multipliers (Phase 1, MRB-133; all 12 pages)
| Component | Role |
|---|---|
| **PredictWrapper** (`shared/predict-wrapper.js`) | `predict: {question, options[], correctIndex, revealsOn}` commit-chip row gating any stateful hero's first reveal; right/wrong vs prediction in tone tokens. Highest pedagogy-per-line in the plan. |
| mistakeCheck v2 | Reset button + multi-item bank; existing single items migrate unchanged. |
| Key Note revision card | Restyle + cover-and-recall toggle. |
| Mode chooser | Teach me / Labs / Test me anchor links under the hero kicker. |
| Quiz exam-paper restyle | §3 item 7, incl. chunking, sticky progress, per-chunk check, inline checkpoints. |

### Tier 2 — the engines (Phase 2+)
ChainBuilder · WriteThenMark · SliderSim (drives the existing pure renderers) · CircuitBench · TapDragConstruct · RankLadder · SpeedRound · FormulaDeducer · BeTheExaminer · shared drawn-primitive module (`atom()/bond()/honeycomb()` extracted from two-state-compare — retires content emoji).

### Tier 3 — flagships (Phase 3–4)
DotCrossCanvas (ionic + covalent) · Electron-Sea Workbench · ScaleZoom · HeatingCurveLab.

**Upgrade, don't replace:** two-state-compare (renderer registry is the platform), state-toggle-lab (absorbed by SliderSim), categorise-bins, fifa-step-reveal. **Replace:** the matching DnD engine (TapMatch). **Keep as worked-mode:** dot-cross-stepper, paired with a drag practice mode.

---

## 5. Phase map and gates (council §7, summary)

- **Phase 0 — Make it honest (MRB-132):** Tier 0 in full. Gate 0 packet: spec defects (verbatim from council §8) + proposed de-leaked matching texts + everything ⚑.
- **Phase 1 — Sharpen what exists (MRB-133):** Tier 1 on all 12 pages + composition dedup (ionic/covalent duplicated blocks) + callout-spacing pass + tone pass. Gate 1: Mide reviews ionic-bonding + giant-covalent-structures.
- **Phase 2 — Exam engines:** ChainBuilder, WriteThenMark, FormulaDeducer on the four 6-marker pages + ionic-bonding. Gate 2: marking-point decompositions (Mide's examiner skillset).
- **Phase 3 — Labs at scale:** batches A (states-of-matter, ionic-compounds, ionic-bonding), B (covalent, small-molecules, polymers), C (chemical-bonds, metallic, metals-alloys, nanoparticles). Gate per batch.
- **Phase 4 — Flagship polish:** DotCrossCanvas, Be-the-Examiner, command-word ladder, anchored stars, bonding mastery map. Final gate against this document.

Verification at every phase: keyboard walk, touch model, reduced-motion, WCAG contrast on new tints, Foundation/Combined variants correct, determinism double-run, zero non-bonding pages changed.
