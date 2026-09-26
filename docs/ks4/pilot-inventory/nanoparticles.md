# L12 · Nanoparticles · QUANTITATIVE

Inventory of `ks4-chemistry-5.2.3.3-nanoparticles.dc.html`, measured in headless Chrome via `docs/ks4/pilot-inventory/measure_design.py` (25 Sep 2026). Method, widths, routes and standing law: see `README.md` in this folder — not restated here. AQA Chemistry 4.2.4 (filename keeps the pilot slug 5.2.3.3, which is actually graphene/fullerenes — NOTES flag 2).

**Console (default route, all 5 widths): clean.** 0 error(s) (favicon 404s filtered). **Overflow: none** at any of 1280/1340/820/390/360 — `document.documentElement.scrollWidth` equalled `innerWidth` at every width, on every route measured.

**Line-up (NOTES-KS4-pilot.md §7):** Hook (ruby glass) → coarse/fine/nano size sort (unit conversion required) → Cube splitter → spot-the-flaw (same substance) → equation → CFIFA → evaluate Ks4Write (sun cream).

⚠️ pilot-build-contract.md §0 pins this lesson's real URLs to TF/TH ONLY (the whole lesson is chemistry-only, 8462 4.2.4). Design's review page still exposes all four Route options for QA — measured identically, 17 sections on every route — which is correct for a REVIEW tool (NOTES §2: 'the generator renders one route per URL and drops the selector'), not a contradiction to port: the generator must build only 2 of the 4 URLs for this slug, not 4.

## 1. Blocks and components in document order (Triple Higher, 1280)

`GEN?` marks against the closed KS3+KS4 vocabulary (14 KS3 types + `required-practical`/`equation`/`extended-response`/`exam-tip`) — every section here is classified to the CLOSEST registered type; the pilot's flagship instruments are NEW SHAPES inside that type (the vocabulary has no separate entry for a bespoke predict-then-reveal instrument, so `check` is the closest fit for most of them — see the per-block note where a different type fits better).

| # | id | block type | eyebrow / heading | words | box (x,y,w,h) |
|---|---|---|---|---|---|
| 1 | `—` | chrome | AQA Chemistry 4.2.4 (chemistry only) · Quantitative | 53 | 160,107,960,483 |
| 2 | `s-hook` | hook | Start here | 103 | 160,619,960,621 |
| 3 | `—` | — |  | 0 | 160,1239,960,0 |
| 4 | `—` | explainer |  | 81 | 160,1267,736,210 |
| 5 | `s-sizes` | check | Sort by size | 90 | 160,1505,960,534 |
| 6 | `s-cube` | worked-example | The cube splitter | 53 | 160,2067,960,260 |
| 7 | `s-think` | misconception | Think again | 75 | 160,2355,960,520 |
| 8 | `s-equation` | equation | Equation | 65 | 160,2903,960,285 |
| 9 | `s-calc` | worked-example | Worked example · CFIFA · one step at a time | 110 | 160,3216,960,1297 |
| 10 | `s-evaluate` | extended-response | Uses and risks · AQA 4.2.4.2 | 103 | 160,4541,960,679 |
| 11 | `—` | keyword | Command words in this lesson | 35 | 160,5248,960,243 |
| 12 | `—` | — |  | 38 | 160,5518,960,157 |
| 13 | `—` | explainer |  | 49 | 160,5703,960,164 |
| 14 | `s-ladder` | ladder | Extended response | 371 | 160,5895,960,2614 |
| 15 | `s-keynote` | key-note |  | 127 | 160,8543,960,544 |
| 16 | `—` | question-bank | Practice set · Triple Higher | 284 | 160,9121,960,1504 |
| 17 | `—` | — |  | 88 | 160,10659,960,458 |

**Flagship (§7):** `#s-cube` — Cube splitter (predict x10; 1000->1 nm; SA, V and ratio tiles).

## 2. Route matrix

| Route | sections (1280) | ladder rungs | ladder words | key-note lines | overflow 390/360 |
|---|---|---|---|---|---|
| TH | 17 | 4 | 371 | 6 | clean |
| CF | 17 | 4 | 371 | (TH only measured) | not swept (1280 only) |
| CH | 17 | 4 | 371 | (TH only measured) | not swept (1280 only) |
| TF | 17 | 4 | 346 | (TH only measured) | not swept (1280 only) |

⚠️ Per `pilot-build-contract.md` §0, this lesson's real URLs are **TF/TH only** — the CF/CH rows above are the review tool's route selector, not routes the generator should build.

**Question bank (Triple Higher, fully expanded via 2 'load more' clicks — see README's pagination note): 11 items.**

## 3. Rail + overflow per width (Triple Higher)

| Width | Rail | Overflow |
|---|---|---|
| 1280 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 6 done Gold in glass') | clean |
| 1340 | side visible (6 nodes) · top hidden (CSS, >=1340) | clean |
| 820 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 6 done Gold in glass') | clean |
| 390 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 6 done Gold in glass') | clean |
| 360 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 6 done Gold in glass') | clean |

Side rail appears only at >=1340 (CSS `@media (min-width:1340px)`, confirmed). **Below 1340, the top bar is NOT width-driven** — `Ks4Chrome`'s `showTop` comes from `state.scrolled = window.scrollY > 140`, set on a scroll listener, so at the top of a narrow page NEITHER rail is visible; scrolling past ~140px reveals the top bar. This is a genuine page behaviour (`Ks4Chrome.dc.html`), not a measurement artefact, and it is the same on every one of the 14 lessons.

**Keyboard (1280):** 71 focusable controls, 0 with `tabindex="-1"` (none found on this lesson) — every control is a real `<button>`/`<select>`/`<textarea>`, matching NOTES §2's 'all controls are real buttons, selects, ranges or inputs: keyboard-complete'.

## 4. Computed styles — light vs dark (1280, Triple Higher)

⚠️ Headless Chrome's own default `prefers-color-scheme` is **dark** (verified: `matchMedia('(prefers-color-scheme: dark)').matches` is `true` and `.rd` background is `rgb(22, 18, 14)` with NO emulation applied at all). Every 'light' row below was measured with `prefers-color-scheme: light` explicitly forced — see README.

| Component | Light | Dark |
|---|---|---|
| h1 | `"Bricolage Grotesque", system-ui, sans-serif` · 74px · 800 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x160 y140 w960 h70 | `"Bricolage Grotesque", system-ui, sans-serif` · 74px · 800 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x160 y140 w960 h70 |
| eyebrow | `"Instrument Sans", system-ui, sans-serif` · 13px · 700 · rgb(95, 86, 79) · rgba(0, 0, 0, 0) · 0px none rgb(95, 86, 79) · radius 0px · pad 0px · shadow none  
  box: x160 y107 w960 h21 | `"Instrument Sans", system-ui, sans-serif` · 13px · 700 · rgb(194, 182, 166) · rgba(0, 0, 0, 0) · 0px none rgb(194, 182, 166) · radius 0px · pad 0px · shadow none  
  box: x160 y107 w960 h21 |
| commit | `"Instrument Sans", system-ui, sans-serif` · 22px · 700 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x192 y869 w896 h30 | `"Instrument Sans", system-ui, sans-serif` · 22px · 700 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x192 y869 w896 h30 |
| option_resting | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(251, 243, 230) · 2px solid rgb(221, 207, 182) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y915 w896 h65 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(243, 236, 224) · rgb(22, 18, 14) · 2px solid rgb(79, 68, 58) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y915 w896 h65 |
| misconception_panel | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(255, 243, 212) · 2px solid rgb(34, 30, 27) · radius 28px · pad 30px · shadow rgb(34, 30, 27) 5px 5px 0px 0px  
  box: x160 y2355 w960 h520 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgb(51, 41, 15) · 2px solid rgb(243, 236, 224) · radius 28px · pad 30px · shadow rgb(243, 236, 224) 5px 5px 0px 0px  
  box: x160 y2355 w960 h520 |
| key_fact_card | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(255, 252, 245) · 2px solid rgb(34, 30, 27) · radius 20px · pad 18px 22px · shadow rgb(228, 87, 46) 5px 5px 0px 0px  
  box: x160 y5518 w960 h157 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgb(31, 26, 21) · 2px solid rgb(243, 236, 224) · radius 20px · pad 18px 22px · shadow rgb(240, 122, 78) 5px 5px 0px 0px  
  box: x160 y5518 w960 h157 |
| badge_pill | `"DM Mono", ui-monospace, monospace` · 13px · 500 · rgb(37, 69, 168) · rgb(225, 232, 254) · 2px solid rgb(47, 92, 224) · radius 99px · pad 4px 11px · shadow none  
  box: x160 y450 w77 h33 | `"DM Mono", ui-monospace, monospace` · 13px · 500 · rgb(168, 192, 255) · rgb(27, 36, 64) · 2px solid rgb(108, 142, 255) · radius 99px · pad 4px 11px · shadow none  
  box: x160 y450 w77 h33 |
| ladder_rung_header | `"Bricolage Grotesque", system-ui, sans-serif` · 36px · 800 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x195 y5930 w825 h58 | `"Bricolage Grotesque", system-ui, sans-serif` · 36px · 800 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x195 y5930 w825 h58 |
| check_button | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(251, 243, 230) · 2px solid rgb(221, 207, 182) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y915 w896 h65 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(243, 236, 224) · rgb(22, 18, 14) · 2px solid rgb(79, 68, 58) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y915 w896 h65 |
| key_note_card | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x160 y8543 w960 h544 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x160 y8543 w960 h544 |
| end_prev_next | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(169, 52, 17) · rgba(0, 0, 0, 0) · 0px none rgb(169, 52, 17) · radius 0px · pad 0px · shadow none  
  box: x184 y10722 w227 h29 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(255, 158, 120) · rgba(0, 0, 0, 0) · 0px none rgb(255, 158, 120) · radius 0px · pad 0px · shadow none  
  box: x184 y10722 w227 h29 |

| reveal panel (`[data-arrive]`, after hook commit) | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(252, 231, 222) · 2px solid rgb(228, 87, 46) · radius 18px · pad 18px 20px · shadow none  
  box: x192 y777 w896 h174 | *(dark not separately captured for state-dependent nodes — see README limitation)* |
| hook option, chosen (`aria-pressed=true`) | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(252, 231, 222) · 2px solid rgb(228, 87, 46) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y467 w896 h65 | *(as above)* |

## 5. Interactions driven, and observed text

| # | Trigger | Observed |
|---|---|---|
| 1 | Click #s-hook's first option | reveal text: '\n      Locked in. Test it with the cube splitter below.\n      In a lump of gold, almost every atom is buried inside. In a 25 nm particle, a large fraction of the atoms sit on the surface, where they interact with light and with other chemicals. That is where the new properties come from.\n    ' |
| 2 | Same commit, reduced-motion proof | `animation-name` normal motion = `ks4-arrive`, reduced motion = `none` → **swaps instantly: True** (matches `@media (prefers-reduced-motion: reduce) { [data-arrive] { animation: none !important; } }` in `Ks4Choice.dc.html`) |
| 3 | Click a button inside the flagship (`#s-sizes`) | clicked=True; new text after click: '(no new tail text — state likely changed via attributes/marks rather than appended prose; see screenshot)' |
| 5 | Click #s-ladder rung 1's first option | feedback: 'Correct. Smaller particle, larger surface area to volume ratio.' (class `ks3-feedback is-correct`) |
| 6 | Type 12+ words into the Write rung, click a still-enabled ladder button | ⚠️ **not a reliable measurement** — by this point rung 1 is already answered+disabled from step 5, so `#s-ladder button` (the click target) can land on rung 2/3's own controls rather than rung 4's *Check my answer*; ticks/tally seen: False. Script limitation, see README — not evidence either way about the Write rung's min-words unlock. |
| 7 | Click the key note's Cover/Uncover toggle | button label changed: True |

## 6. Findings

- **Page vs architecture (universal, applies here too — see NOTES §10, not repeated per point):** rung 2 is 'deduce or use data', not the architecture brief's 'units required'; the verbatim quiz lives in a Question bank after the key note, not folded into the ladder; the Route selector is a review affordance the generator must drop; comparison tables are card rows, not `<table>`.
- **Route-tag / build scope, this lesson:** pilot-build-contract.md §0 pins this lesson's real URLs to TF/TH ONLY (the whole lesson is chemistry-only, 8462 4.2.4). Design's review page still exposes all four Route options for QA — measured identically, 17 sections on every route — which is correct for a REVIEW tool (NOTES §2: 'the generator renders one route per URL and drops the selector'), not a contradiction to port: the generator must build only 2 of the 4 URLs for this slug, not 4.
- **Console:** clean across all 5 widths on the default route (0 errors).
- **Overflow:** none found at 390 or 360, any route swept.
- **Keyboard:** 0 controls with `tabindex="-1"` (none) — no keyboard gap found.
- **Reduced motion:** the shared `[data-arrive]` reveal mechanism swaps instantly (`animation-name: none`) — True.
- **Relevant NOTES §9 science flags for this lesson:** #2, #3, #4, #5, #18 — see `NOTES-KS4-pilot.md` for the AQA-sourced text of each; not restated here since they are the examiners' remit (§4.2 of the run brief), not this inventory's.

Screenshots (Triple Higher, light): `$MRB_SHOTS/design/nanoparticles-1280.png`, `$MRB_SHOTS/design/nanoparticles-360.png`.
