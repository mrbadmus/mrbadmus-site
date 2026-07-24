# Bonding Port — Progress Log (MRB-113 Phase B, gates B2–B5 + MRB-124 + exemplar retrofit)

Autonomous batch run. Resume point for a fresh session. **No commits in this run.**
HEAD at run start: `ba4db059e` (clean tree).

---

## PHASE A — RECON (complete)

### Git/env guard
HEAD = `ba4db059e`, tree clean. Generator green + deterministic (tree stays clean after regen).

### What's already built (pilots B0/B1, on disk)
- `shared/heroes/two-state-compare.js` — RENDERERS: `tetrahedral`, `hexLayers` only. Config: emoji/title/subtitle/strap + 2 states {key,label,emoji,tone,effectTitle,caption,legend,props[],visual}. Callout tinted by state `tone`. No force support yet.
- `shared/heroes/categorise-bins.js` — generic bins, browser-shuffled per load, graded by card→bin map. Reuse as-is.
- `shared/heroes/theory-blocks.js` — interactive blocks `mistakeCheck` + `compareReveal`. Config-driven.
- `shared/heroes/bonding-configs.js` — configs for exemplar (two-state + bins) + 2 pilot bins (chemical-bonds, properties-small-molecules).
- `bonding_redesign.py` — theory-block library: STATIC renderers (lead, feature-cards, compare-cards, step-sequence, example-callout, aside-callout, examiner-tip) + INTERACTIVE host emit (mistake-check, compare-reveal). `BONDING_REDESIGN` has 2 pilot entries (chemical-bonds, properties-small-molecules). `render_examiner_tip`, `interactive_init_js` helpers.
- Generator (`generate_site_v5.py`): two `.rd` branches inside `make_new_subtopic_page` —
  (1) `st_id == "giant-covalent-structures"` (exemplar: two-state hero + bins + reveal-quiz, theory still `.theory-line` prose);
  (2) `st_id in BONDING_REDESIGN` (block page: theory→blocks, bins activity, mistake-check replaces static box). Both null `matching_js`, use `PILOT_QUIZ_JS` reveal-quiz, load `bonding-configs.js`.

### Hero `.dc.html` specs (all four present + fully specified — NO blockers)
- **Hero 3 Two-State Compare** — new renderers `metalLayers` (alloy bool + optional force→slide; pure shears, alloy locked) and `delocalised`/electron-sea (`free` bool: drift vs pinned). Optional `force` demo w/ per-state `forced` overrides.
- **Hero 2 Dot-and-Cross Stepper** — atoms as shells; ordered steps (phase neutral/focus/moved); mode transfer|share; layout di|tri. Back/Next/dots nav. Config: left/right {sym,cfgBefore,cfgAfter,charge,outer,r}, steps[], result.
- **Hero 1 State Toggle Lab** — ion lattice; arrangements lattice|jiggle|dissolved|sheared; verdict bulb {glow,title,sub}; optional force→shatter (state not in toggle). Config: ions{pos,neg glyph}, grid{cols,rows}, states[], force.
- **Hero 6 FIFA Step Reveal** — worked (reveal step-by-step) + practice (per-step choice/input marking). FIFA spine (F,I,F,A) structural. Config: problem, given[], steps[4]{title,worked,note,practice{prompt,kind,options/blanks,feedback}}, success, hint.

### PER-VARIANT THEORY CHECK (recon item 5 — RESOLVED CLEAN)
Diffed all 8 protected fields across the 4 data files (CF/CH/TF/TH) for all 12 bonding pages:
- **`theory`, `common_mistake`, `key_note`, `matching` are BYTE-IDENTICAL across all variants** on every page → single decomposition per page is valid. No per-variant block handling needed.
- **`quiz` differs per variant** (expected; `make_new_quiz` reads `st["quiz"]` per variant — automatic).
- **`higher` box** present only on Higher-tier variants: covalent-bonding (CH/TH), nanoparticles (TH), giant-covalent-structures (CH/TH). Generator renders `higher_html` only where present — automatic.
- **`triple_only` FIELD: absent on every bonding page** (nanoparticles is triple-only by *page presence*, not by field). No triple furniture to render from a field.
- **nanoparticles `fifas` DIFFER TF vs TH** → FIFA hero reads the frozen per-variant `st["fifas"]` for the worked spine; practice scaffolding authored per tier. Keeps freeze; right set per tier automatic.

### EXAMINER TIP (recon item 7 — CONFIRMED)
Every page carries `examiner_tip` in every variant it exists in (nanoparticles only TF/TH, as expected). Renders via `render_examiner_tip` amber block on `.rd` pages. Do not author/edit — verify-only.

### ACTIVITY MECHANICS (recon item 6 — RESOLVED)
`make_matching_widget` shuffles the RIGHT column (definitions) with a **seeded build-time shuffle** (`random.Random("match:<st_id>:<n>")`); the LEFT column (terms/drop-slots) renders in source order, graded by `data-group` (category group), independent of position. For a true 1:1 match the defs are already scrambled relative to terms, so there is **no live top-to-bottom positional give-away**. The only residual weakness is that the shuffle is build-time-seeded (fixed per page) rather than a per-load browser shuffle, so a returning student could memorise an arrangement — a site-wide mechanics refinement that belongs to **MRB-121 Phase 2**, NOT this port. Decision: the 8 Match pages reuse the existing `make_matching_widget` + standard `matching_js` under `.rd`. Not bundling MRB-121.

### AUDIT BASELINE (bonding only)
- **0 critical**, **2 major** (`2-practice-absent` on nanoparticles TF+TH — my clear target), **319 minor** (`1-length-parity` = MRB-122 scope, remain), **4 info** (`4-menu` on polymers = has equation, no FIFA, deliberate).
- Audit reads DATA (`fifas`) not HTML, and flags `2-practice-absent` unconditionally when `fifas` present ("systemic: static steps only"). Clearing nanoparticles requires teaching the audit that redesigned FIFA pages (FIFA hero) now render real practice.

### DESIGN DECISIONS locked from recon
1. Generalise the `st_id in BONDING_REDESIGN` generator branch to be data-driven over `rcfg`: `hero` (None | {module,ns,config_key}), `activity` ({type:"bins",config_key} | {type:"match"}), `theory_blocks`.
2. Suppress the static Common-Mistake box **iff** the theory_blocks contain a `mistake-check` (data-driven). Hero pages + compare-reveal pages keep the static box; mistake-check pages replace it.
3. Match pages reuse default `matching_html`/`matching_js`; bins pages use categorise-bins.
4. FIFA hero reads frozen `st["fifas"]` (worked spine, per-variant) zipped with tier-keyed authored practice.
5. Fold the exemplar into `BONDING_REDESIGN` at D2 so there is one branch.

---

## PHASE B — MRB-124 MOBILE FIX  ✅ DONE
**Cause (measured, not assumed):** `.rd .rd-blk-feature { grid-template-columns: repeat(auto-fit,minmax(210px,1fr)); }` placed 2 tracks (2×210+12=432px) on a ~382px content box (viewport−48 padding), so the 2nd track overflowed and dragged the whole page into horizontal scroll — lead text + compare rows clipped at the right at both 390px and 430px.
**Fix:** appended `@media (max-width:560px){ .rd .rd-blk-feature { grid-template-columns:1fr; } }` to `BLOCK_CSS` in `bonding_redesign.py` — same breakpoint the compare-cards already use; later source order beats the base rule (no `!important` needed since feature-cards carry no inline grid-template).
**Verified (headless-Chrome iframe geometry probe @430px):**
- Before: feature-cards 2-col, page horizontally overflowed.
- After: `.content-area` 430 pad 24/24; `.rd-blk-lead` w=382 sw=382 (no overflow); `.rd-blk-feature` single-col w=382 sw=382; **DOC scrollWidth=430=clientWidth → no page overflow** at 390px and 430px.
**Footprint:** `bonding_redesign.py` + the 2 pilot pages ×4 variants ×(root+mirror)=16 HTML. No other page touched (BLOCK_CSS is inlined only on `.rd` bonding pages).
**Observed, out of scope (noted for review):** `.mrb-bins__grid` (3-bin categorise) sw=358 vs box 332 at 382px — the 3-column bins grid is cramped on narrow phones; content stays on-page (overflow visible, right=381<430), no page clip. Pre-existing on the shipped pilots + exemplar, a categorise-bins mobile refinement, NOT MRB-124.

## PHASE C — HEROES  ✅ DONE (all 5 proven, render + interact, 2 configs each)
All modules syntax-clean (`node --check`), no JS console errors on the harness, all interactions driven & screenshot-verified. Reduced-motion guards on every looping animation; all controls real `<button>`s; state paired with label/icon/shape, never colour alone.

1. **Two-State Compare** (extended `two-state-compare.js`) — added `electronSea`/`delocalised` + `metalLayers` renderers + optional `force` support (per-state `forced` override swaps callout/legend/props; force button; `forced=false` on state switch). Backward-compatible: exemplar (no `force`) unchanged.
   - Proof A: metallic-bonding electron-sea on/off — drifting sea, green conducts chips. ✓
   - Proof B: metals-alloys metalLayers + force — clicking Apply force sheared the pure-metal layers into a parallelogram, callout swapped to green "Layers slide → bends", button → "Release force". ✓
2. **Dot-and-Cross Stepper** (new `dot-cross-stepper.js`) — atoms as shells, transfer/share, di/tri layouts, phase neutral/focus/moved, Back/Next/dots nav, optional molecule picker. Focus pulse reduced-motion-guarded.
   - Proof A: ionic transfer NaCl/MgO/MgCl₂ — Na(2.8.1)•/Cl(2.8.7)×; Next×3 → moved: Na⁺(2.8) badge, transferred dot on Cl⁻(2.8.8), green result bar. ✓
   - Proof B: covalent share H₂/Cl₂/HCl — dots + crosses, shared-pair overlap. ✓
3. **State Toggle Lab** (new `state-toggle-lab.js`) — ion lattice; lattice/jiggle/dissolved/sheared arrangements; verdict bulb; optional force→shatter. Jiggle + bulb-glow reduced-motion-guarded.
   - Proof A: ionic-compounds NaCl — 4 states + force → "⚡ repel!" shatter, verdict flips. ✓
   - Proof B: MgO (2 states, ion symbols Mg²⁺/O²⁻, no force) — verdict "No conduction ✕". ✓
4. **FIFA Step Reveal** (new `fifa-step-reveal.js`) — worked (step reveal) + practice (per-step choice/input marking) + example picker. Options read `.correct` (aligned with mistake-check). ≥3 examples via picker.
   - Proof A: nanoparticles Foundation (3 cube examples) — practice mode: picked correct formula → step F solved (green ✓), advanced to step I (active inputs), F/A locked. **This is the interactive practice that clears the nanoparticles FIFA-practice major.** ✓
   - Proof B: nanoparticles Higher (3 nm examples). ✓
   - FIFA content: WORKED spine = frozen `st["fifas"]` per variant (read, never edited); PRACTICE authored per tier in `NANO_FIFA` + zipped by `build_fifa_config(fifas, tier)`. Verified assembly for both tiers, worked lines byte-match frozen. ⚠ Practice accept-values are SCIENCE-SENSITIVE — flagged for Mide's full review.
5. **Categorise Bins** — reused as-is; new config `properties-ionic-compounds-bins` (Ionic/Metal/Both) authored from frozen `matching`. Rendered clean.

Hero configs authored in `bonding-configs.js` (metallic-bonding, metals-alloys, ionic-bonding, covalent-bonding, ionic-compounds, properties-ionic-compounds-bins) — all from frozen prose, colour=meaning via tone. FIFA config assembled in `bonding_redesign.py`.

## PHASE D — PAGE PORTS  ✅ DONE (9 pages)
**Generator infra:** the `st_id in BONDING_REDESIGN` branch is now fully data-driven over `rcfg` (hero None|config-key|FIFA-build; activity bins|match; theory_blocks). Static Common-Mistake box suppressed **iff** a `mistake-check` block is present. FIFA config assembled inline via `build_fifa_config(st["fifas"], tier)`. Import extended with `build_fifa_config`.

**Wiring matrix (generated HTML, verified):**
| page | static mistake | mistake-check | compare-reveal | bins | match | hero |
|---|---|---|---|---|---|---|
| metallic-bonding | ✓ | — | — | — | ✓ | ✓ |
| metals-alloys | ✓ | — | — | — | ✓ | ✓ |
| ionic-bonding | ✓ | — | — | — | ✓ | ✓ |
| covalent-bonding | ✓ | — | — | — | ✓ | ✓ |
| ionic-compounds | ✓ | — | — | — | ✓ | ✓ |
| nanoparticles | ✓ | — | — | — | ✓ | ✓ (FIFA) |
| states-of-matter | — | ✓ | — | — | ✓ | — |
| properties-ionic-compounds | ✓ | — | ✓ | ✓ | — | — |
| polymers | — | ✓ | — | — | ✓ | — |

Hero pages keep the static Common Mistake (exemplar pattern); mistake-check pages suppress it; the compare-reveal page keeps it. No two adjacent pages share a block lineup.

**Screenshot-verified on real generated pages:** metallic-bonding (electron-sea hero, step-sequence, colour=meaning feature-cards, example-callout, static mistake, examiner-tip amber block, drag-match); nanoparticles (FIFA hero, worked line = frozen text); properties-ionic-compounds (compare-cards w/ highlighted payoff, compare-reveal, static mistake kept, bins). Heroes' full interactions proven in Phase C.

**Per-variant correctness:** nanoparticles FIFA — Foundation shows the cube examples (side 1/2/3), Higher shows the nm examples (10nm / 1000nm / work-backwards); Foundation carries none of the Higher examples. Tier furniture: covalent-bonding + nanoparticles Higher box render only on Higher variants; polymers Key Equations present.

**Deliberate calls honoured:** properties-ionic-compounds hero-less (compare-reveal, avoids duplicating page-4 lab); metallic-bonding owns conduction (electron-sea), metals-alloys owns structure→property (metalLayers+force); covalent Dot-and-Cross diatomic-only (H₂/Cl₂/HCl), polyatomics as static feature-cards; ionic Dot-and-Cross gains MgO/MgCl₂ via the molecule picker (uses the tri layout). Match pages reuse `make_matching_widget` (MRB-121 build-time-shuffle noted, not bundled).

## PHASE D2 — EXEMPLAR RETROFIT  ✅ DONE
`giant-covalent-structures` folded into `BONDING_REDESIGN` (Two-State hero + bins + block theory); its dedicated generator `if`-branch deleted, now flows through the single data-driven branch. Theory moved prose → blocks (lead, colour=meaning feature-cards, Diamond|Graphite compare-cards w/ highlighted "Conducts?" payoff + verdict, Uses callout). Hero, bins, quiz, examiner-tip and the static Common Mistake unchanged. Bins kicker made configurable to preserve "sort the properties". Screenshot-verified. (One dead `.rd .theory-line` CSS rule remains in redesign_css — harmless, noted in PORTING.md.)

## PHASE E — VERIFY  ✅ ALL PASS
| # | check | result |
|---|---|---|
| 1 | `generate_site_v5.py` | green, all pages |
| 2 | determinism (twice) | byte-identical (`47f2c190…`) |
| 2b | reshuffle | **zero non-bonding HTML changed** vs HEAD (tokens.css untouched → not even a cache-bust) |
| 3 | content freeze | 4 data files **byte-identical to HEAD** → all 8 protected fields frozen; FIFA worked lines byte-match frozen `fifas` |
| 4 | contrast | every introduced text colour ≥4.5:1 on its real bg (locked-step fixed #B0A695→#6B635A; smallest mono labels ≥13px@render weight 700) |
| 5 | audit | bonding **0 critical / 0 major**; nanoparticles FIFA-practice major **CLEARED** (audit taught to recognise the FIFA hero); 319 length-parity minors remain (MRB-122); 4 `4-menu` info (polymers) |
| 6 | examiner tips | all 46 bonding page-variants render the amber block; none render the flat callout (no double-render) |
| 7 | screenshots | 12 desktop + 2×390px mobile; DOC scrollWidth=clientWidth=390 on both (hero diagram scrolls inside its own overflow-x:auto container). Long hero titles shortened + header wrap safety-net. |

**All 5 hero archetypes verified on real generated pages:** hero+static-mistake (metallic-bonding, ionic-compounds), FIFA (nanoparticles, per-tier examples), compare-reveal+bins+static-mistake (properties-ionic-compounds), mistake-check suppresses static box (states-of-matter), exemplar retrofit (giant-covalent-structures).

**RUN COMPLETE — awaiting Mide review. No commits made.**

## PHASE D — PAGE PORTS
(pending)

## PHASE D2 — EXEMPLAR RETROFIT
(pending)

## PHASE E — VERIFY
(pending)
