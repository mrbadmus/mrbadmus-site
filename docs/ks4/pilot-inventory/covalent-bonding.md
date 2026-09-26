# L4 · Covalent bonding · PROCESS

Inventory of `ks4-chemistry-5.2.1.4-covalent-bonding.dc.html`, measured in headless Chrome via `docs/ks4/pilot-inventory/measure_design.py` (25 Sep 2026). Method, widths, routes and standing law: see `README.md` in this folder — not restated here. AQA Chemistry 5.2.1.4.

**Console (default route, all 5 widths): clean.** 0 error(s) (favicon 404s filtered). **Overflow: none** at any of 1280/1340/820/390/360 — `document.documentElement.scrollWidth` equalled `innerWidth` at every width, on every route measured.

**Line-up (NOTES-KS4-pilot.md §7):** Hook (H2) → worked water in 3 steps with a bond-count gate → Shared-pair builder → weak-bond misconception sort.

⚠️ **Misconception placement:** the weak-bond misconception here is carried by #s-sort itself (`class="ks3-block ks3-misconception"` on the SORT section, source-verified) rather than by a separate spot-the-flaw block — a different shape from every other lesson in the pilot, where sort and misconception are two blocks.

## 1. Blocks and components in document order (Triple Higher, 1280)

`GEN?` marks against the closed KS3+KS4 vocabulary (14 KS3 types + `required-practical`/`equation`/`extended-response`/`exam-tip`) — every section here is classified to the CLOSEST registered type; the pilot's flagship instruments are NEW SHAPES inside that type (the vocabulary has no separate entry for a bespoke predict-then-reveal instrument, so `check` is the closest fit for most of them — see the per-block note where a different type fits better).

| # | id | block type | eyebrow / heading | words | box (x,y,w,h) |
|---|---|---|---|---|---|
| 1 | `—` | chrome | AQA Chemistry 5.2.1.4 · Process | 44 | 160,107,960,416 |
| 2 | `s-hook` | hook | Start here | 116 | 160,551,960,621 |
| 3 | `—` | — |  | 0 | 160,1172,960,0 |
| 4 | `—` | explainer |  | 83 | 160,1200,736,210 |
| 5 | `s-watch` | worked-example | Worked · water, H₂O | 51 | 160,1438,960,593 |
| 6 | `s-build` | check | Your turn · the shared-pair builder | 56 | 160,2059,960,602 |
| 7 | `—` | explainer |  | 67 | 160,2689,736,210 |
| 8 | `s-sort` | misconception | Think again · strong bond or weak force? | 138 | 160,2927,960,752 |
| 9 | `—` | keyword | Command words in this lesson | 37 | 160,3706,960,243 |
| 10 | `—` | — |  | 33 | 160,3977,960,127 |
| 11 | `—` | explainer |  | 37 | 160,4132,960,164 |
| 12 | `s-ladder` | ladder | Extended response | 306 | 160,4324,960,2178 |
| 13 | `s-keynote` | key-note |  | 103 | 160,6536,960,484 |
| 14 | `—` | question-bank | Practice set · Triple Higher | 235 | 160,7054,960,1398 |
| 15 | `—` | — |  | 87 | 160,8486,960,476 |

**Flagship (§7):** `#s-build` — Shared-pair builder (HCl, Cl2, O2, N2, NH3, CH4, CO2; +/- pairs per bond; per-atom 'n of 8' chips; correct build reveals the dot-and-cross).

## 2. Route matrix

| Route | sections (1280) | ladder rungs | ladder words | key-note lines | overflow 390/360 |
|---|---|---|---|---|---|
| TH | 15 | 4 | 306 | 6 | clean |
| CF | 15 | 4 | 306 | (TH only measured) | not swept (1280 only) |
| CH | 15 | 4 | 306 | (TH only measured) | not swept (1280 only) |
| TF | 15 | 4 | 306 | (TH only measured) | not swept (1280 only) |

**Question bank (Triple Higher, fully expanded via 2 'load more' clicks — see README's pagination note): 12 items.**

## 3. Rail + overflow per width (Triple Higher)

| Width | Rail | Overflow |
|---|---|---|
| 1280 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Two hydrogen atoms') | clean |
| 1340 | side visible (5 nodes) · top hidden (CSS, >=1340) | clean |
| 820 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Two hydrogen atoms') | clean |
| 390 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Two hydrogen atoms') | clean |
| 360 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Two hydrogen atoms') | clean |

Side rail appears only at >=1340 (CSS `@media (min-width:1340px)`, confirmed). **Below 1340, the top bar is NOT width-driven** — `Ks4Chrome`'s `showTop` comes from `state.scrolled = window.scrollY > 140`, set on a scroll listener, so at the top of a narrow page NEITHER rail is visible; scrolling past ~140px reveals the top bar. This is a genuine page behaviour (`Ks4Chrome.dc.html`), not a measurement artefact, and it is the same on every one of the 14 lessons.

**Keyboard (1280):** 65 focusable controls, 0 with `tabindex="-1"` (none found on this lesson) — every control is a real `<button>`/`<select>`/`<textarea>`, matching NOTES §2's 'all controls are real buttons, selects, ranges or inputs: keyboard-complete'.

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
  box: x192 y802 w896 h30 | `"Instrument Sans", system-ui, sans-serif` · 22px · 700 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x192 y802 w896 h30 |
| option_resting | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(251, 243, 230) · 2px solid rgb(221, 207, 182) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y848 w896 h65 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(243, 236, 224) · rgb(22, 18, 14) · 2px solid rgb(79, 68, 58) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y848 w896 h65 |
| misconception_panel | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(255, 243, 212) · 2px solid rgb(34, 30, 27) · radius 28px · pad 30px · shadow rgb(34, 30, 27) 5px 5px 0px 0px  
  box: x160 y2927 w960 h752 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgb(51, 41, 15) · 2px solid rgb(243, 236, 224) · radius 28px · pad 30px · shadow rgb(243, 236, 224) 5px 5px 0px 0px  
  box: x160 y2927 w960 h752 |
| key_fact_card | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(255, 252, 245) · 2px solid rgb(34, 30, 27) · radius 20px · pad 18px 22px · shadow rgb(228, 87, 46) 5px 5px 0px 0px  
  box: x160 y3977 w960 h127 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgb(31, 26, 21) · 2px solid rgb(243, 236, 224) · radius 20px · pad 18px 22px · shadow rgb(240, 122, 78) 5px 5px 0px 0px  
  box: x160 y3977 w960 h127 |
| badge_pill | `"DM Mono", ui-monospace, monospace` · 13px · 500 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 2px solid rgb(34, 30, 27) · radius 99px · pad 4px 11px · shadow none  
  box: x160 y382 w172 h33 | `"DM Mono", ui-monospace, monospace` · 13px · 500 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 2px solid rgb(243, 236, 224) · radius 99px · pad 4px 11px · shadow none  
  box: x160 y382 w172 h33 |
| ladder_rung_header | `"Bricolage Grotesque", system-ui, sans-serif` · 36px · 800 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x195 y4359 w825 h58 | `"Bricolage Grotesque", system-ui, sans-serif` · 36px · 800 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x195 y4359 w825 h58 |
| check_button | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(251, 243, 230) · 2px solid rgb(221, 207, 182) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y848 w896 h65 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(243, 236, 224) · rgb(22, 18, 14) · 2px solid rgb(79, 68, 58) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y848 w896 h65 |
| key_note_card | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x160 y6536 w960 h484 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x160 y6536 w960 h484 |
| end_prev_next | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(169, 52, 17) · rgba(0, 0, 0, 0) · 0px none rgb(169, 52, 17) · radius 0px · pad 0px · shadow none  
  box: x184 y8549 w229 h29 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(255, 158, 120) · rgba(0, 0, 0, 0) · 0px none rgb(255, 158, 120) · radius 0px · pad 0px · shadow none  
  box: x184 y8549 w229 h29 |

| reveal panel (`[data-arrive]`, after hook commit) | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(252, 231, 222) · 2px solid rgb(228, 87, 46) · radius 18px · pad 18px 20px · shadow none  
  box: x192 y778 w896 h143 | *(dark not separately captured for state-dependent nodes — see README limitation)* |
| hook option, chosen (`aria-pressed=true`) | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(252, 231, 222) · 2px solid rgb(228, 87, 46) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y468 w896 h65 | *(as above)* |

## 5. Interactions driven, and observed text

| # | Trigger | Observed |
|---|---|---|
| 1 | Click #s-hook's first option | reveal text: '\n      Locked in. Watch that idea build a real molecule below.\n      The two atoms overlap and share their electrons as a pair. Each atom now counts two electrons in its shell. The pair is attracted to both nuclei, which holds the molecule together.\n    ' |
| 2 | Same commit, reduced-motion proof | `animation-name` normal motion = `ks4-arrive`, reduced motion = `none` → **swaps instantly: True** (matches `@media (prefers-reduced-motion: reduce) { [data-arrive] { animation: none !important; } }` in `Ks4Choice.dc.html`) |
| 3 | Click a button inside the flagship (`#s-watch`) | clicked=True; new text after click: '(no new tail text — state likely changed via attributes/marks rather than appended prose; see screenshot)' |
| 4 | Tap a card then a bin in the sort (`9` buttons found) | interacted=True |
| 5 | Click #s-ladder rung 1's first option | feedback: 'Not this time. That would need 4 hydrogen atoms; water has 2.' (class `ks3-feedback is-wrong`) |
| 6 | Type 12+ words into the Write rung, click a still-enabled ladder button | ⚠️ **not a reliable measurement** — by this point rung 1 is already answered+disabled from step 5, so `#s-ladder button` (the click target) can land on rung 2/3's own controls rather than rung 4's *Check my answer*; ticks/tally seen: False. Script limitation, see README — not evidence either way about the Write rung's min-words unlock. |
| 7 | Click the key note's Cover/Uncover toggle | button label changed: True |

## 6. Findings

- **Page vs architecture (universal, applies here too — see NOTES §10, not repeated per point):** rung 2 is 'deduce or use data', not the architecture brief's 'units required'; the verbatim quiz lives in a Question bank after the key note, not folded into the ladder; the Route selector is a review affordance the generator must drop; comparison tables are card rows, not `<table>`.
- **Misconception placement, this lesson:** the weak-bond misconception here is carried by #s-sort itself (`class="ks3-block ks3-misconception"` on the SORT section, source-verified) rather than by a separate spot-the-flaw block — a different shape from every other lesson in the pilot, where sort and misconception are two blocks.
- **Console:** clean across all 5 widths on the default route (0 errors).
- **Overflow:** none found at 390 or 360, any route swept.
- **Keyboard:** 0 controls with `tabindex="-1"` (none) — no keyboard gap found.
- **Reduced motion:** the shared `[data-arrive]` reveal mechanism swaps instantly (`animation-name: none`) — True.
- **Relevant NOTES §9 science flags for this lesson:** #6, #16, #18 — see `NOTES-KS4-pilot.md` for the AQA-sourced text of each; not restated here since they are the examiners' remit (§4.2 of the run brief), not this inventory's.

Screenshots (Triple Higher, light): `$MRB_SHOTS/design/covalent-bonding-1280.png`, `$MRB_SHOTS/design/covalent-bonding-360.png`.
