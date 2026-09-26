# L9 · Polymers · CLASSIFY

Inventory of `ks4-chemistry-5.2.2.5-polymers.dc.html`, measured in headless Chrome via `docs/ks4/pilot-inventory/measure_design.py` (25 Sep 2026). Method, widths, routes and standing law: see `README.md` in this folder — not restated here. AQA Chemistry 5.2.2.5.

**Console (default route, all 5 widths): clean.** 0 error(s) (favicon 404s filtered). **Overflow: none** at any of 1280/1340/820/390/360 — `document.documentElement.scrollWidth` equalled `innerWidth` at every width, on every route measured.

**Line-up (NOTES-KS4-pilot.md §7):** Hook (ethene vs bag) → Structure decider → spot-the-flaw (polymer != giant covalent) → Triple: addition-polymerisation chain builder (predict atoms lost; verbatim equation; thermosoftening and thermosetting).

⚠️ #s-addition is Triple-only (8462 4.7.3.1/4.10.4.3, chemistry only, NOTES §8) — reference.json shows 14 sections on TH/TF against 13 on CF/CH.

## 1. Blocks and components in document order (Triple Higher, 1280)

`GEN?` marks against the closed KS3+KS4 vocabulary (14 KS3 types + `required-practical`/`equation`/`extended-response`/`exam-tip`) — every section here is classified to the CLOSEST registered type; the pilot's flagship instruments are NEW SHAPES inside that type (the vocabulary has no separate entry for a bespoke predict-then-reveal instrument, so `check` is the closest fit for most of them — see the per-block note where a different type fits better).

| # | id | block type | eyebrow / heading | words | box (x,y,w,h) |
|---|---|---|---|---|---|
| 1 | `—` | chrome | AQA Chemistry 5.2.2.5 · Classify | 60 | 160,107,960,483 |
| 2 | `s-hook` | hook | Start here | 120 | 160,619,960,651 |
| 3 | `—` | — |  | 0 | 160,1270,960,0 |
| 4 | `—` | explainer |  | 72 | 160,1298,736,210 |
| 5 | `s-classify` | check | Structure decider · round 1 | 21 | 160,1536,960,547 |
| 6 | `s-think` | misconception | Think again | 78 | 160,2110,960,579 |
| 7 | `s-addition` | worked-example | Addition polymerisation · AQA 4.7.3.1 (chemistry only) | 91 | 160,2717,960,420 |
| 8 | `—` | keyword | Command words in this lesson | 46 | 160,3165,960,243 |
| 9 | `—` | — |  | 30 | 160,3436,960,157 |
| 10 | `—` | explainer |  | 53 | 160,3621,960,164 |
| 11 | `s-ladder` | ladder | Extended response | 326 | 160,3813,960,2638 |
| 12 | `s-keynote` | key-note |  | 101 | 160,6484,960,544 |
| 13 | `—` | question-bank | Practice set · Triple Higher | 273 | 160,7062,960,1447 |
| 14 | `—` | — |  | 98 | 160,8543,960,464 |

**Flagship (§7):** `#s-classify` — Structure decider (8 drawn diagrams in two rounds; wrong 'giant covalent' on a polymer gets a targeted trap reply).

## 2. Route matrix

| Route | sections (1280) | ladder rungs | ladder words | key-note lines | overflow 390/360 |
|---|---|---|---|---|---|
| TH | 14 | 4 | 326 | 6 | clean |
| CF | 13 | 4 | 326 | (TH only measured) | not swept (1280 only) |
| CH | 13 | 4 | 326 | (TH only measured) | not swept (1280 only) |
| TF | 14 | 4 | 326 | (TH only measured) | not swept (1280 only) |

**Question bank (Triple Higher, fully expanded via 2 'load more' clicks — see README's pagination note): 12 items.**

## 3. Rail + overflow per width (Triple Higher)

| Width | Rail | Overflow |
|---|---|---|
| 1280 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 4 done Gas or carrier bag') | clean |
| 1340 | side visible (4 nodes) · top hidden (CSS, >=1340) | clean |
| 820 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 4 done Gas or carrier bag') | clean |
| 390 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 4 done Gas or carrier bag') | clean |
| 360 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 4 done Gas or carrier bag') | clean |

Side rail appears only at >=1340 (CSS `@media (min-width:1340px)`, confirmed). **Below 1340, the top bar is NOT width-driven** — `Ks4Chrome`'s `showTop` comes from `state.scrolled = window.scrollY > 140`, set on a scroll listener, so at the top of a narrow page NEITHER rail is visible; scrolling past ~140px reveals the top bar. This is a genuine page behaviour (`Ks4Chrome.dc.html`), not a measurement artefact, and it is the same on every one of the 14 lessons.

**Keyboard (1280):** 63 focusable controls, 0 with `tabindex="-1"` (none found on this lesson) — every control is a real `<button>`/`<select>`/`<textarea>`, matching NOTES §2's 'all controls are real buttons, selects, ranges or inputs: keyboard-complete'.

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
  box: x192 y900 w896 h30 | `"Instrument Sans", system-ui, sans-serif` · 22px · 700 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x192 y900 w896 h30 |
| option_resting | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(251, 243, 230) · 2px solid rgb(221, 207, 182) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y946 w896 h65 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(243, 236, 224) · rgb(22, 18, 14) · 2px solid rgb(79, 68, 58) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y946 w896 h65 |
| misconception_panel | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(255, 243, 212) · 2px solid rgb(34, 30, 27) · radius 28px · pad 30px · shadow rgb(34, 30, 27) 5px 5px 0px 0px  
  box: x160 y2110 w960 h579 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgb(51, 41, 15) · 2px solid rgb(243, 236, 224) · radius 28px · pad 30px · shadow rgb(243, 236, 224) 5px 5px 0px 0px  
  box: x160 y2110 w960 h579 |
| key_fact_card | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(255, 252, 245) · 2px solid rgb(34, 30, 27) · radius 20px · pad 18px 22px · shadow rgb(228, 87, 46) 5px 5px 0px 0px  
  box: x160 y3436 w960 h157 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgb(31, 26, 21) · 2px solid rgb(243, 236, 224) · radius 20px · pad 18px 22px · shadow rgb(240, 122, 78) 5px 5px 0px 0px  
  box: x160 y3436 w960 h157 |
| badge_pill | `"DM Mono", ui-monospace, monospace` · 13px · 500 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 2px solid rgb(34, 30, 27) · radius 99px · pad 4px 11px · shadow none  
  box: x160 y450 w172 h33 | `"DM Mono", ui-monospace, monospace` · 13px · 500 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 2px solid rgb(243, 236, 224) · radius 99px · pad 4px 11px · shadow none  
  box: x160 y450 w172 h33 |
| ladder_rung_header | `"Bricolage Grotesque", system-ui, sans-serif` · 36px · 800 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x195 y3848 w825 h58 | `"Bricolage Grotesque", system-ui, sans-serif` · 36px · 800 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x195 y3848 w825 h58 |
| check_button | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(251, 243, 230) · 2px solid rgb(221, 207, 182) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y946 w896 h65 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(243, 236, 224) · rgb(22, 18, 14) · 2px solid rgb(79, 68, 58) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y946 w896 h65 |
| key_note_card | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x160 y6484 w960 h544 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x160 y6484 w960 h544 |
| end_prev_next | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(169, 52, 17) · rgba(0, 0, 0, 0) · 0px none rgb(169, 52, 17) · radius 0px · pad 0px · shadow none  
  box: x184 y8604 w261 h58 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(255, 158, 120) · rgba(0, 0, 0, 0) · 0px none rgb(255, 158, 120) · radius 0px · pad 0px · shadow none  
  box: x184 y8604 w261 h58 |

| reveal panel (`[data-arrive]`, after hook commit) | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(252, 231, 222) · 2px solid rgb(228, 87, 46) · radius 18px · pad 18px 20px · shadow none  
  box: x192 y778 w896 h174 | *(dark not separately captured for state-dependent nodes — see README limitation)* |
| hook option, chosen (`aria-pressed=true`) | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(252, 231, 222) · 2px solid rgb(228, 87, 46) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y468 w896 h65 | *(as above)* |

## 5. Interactions driven, and observed text

| # | Trigger | Observed |
|---|---|---|
| 1 | Click #s-hook's first option | reveal text: '\n      Locked in. Keep that idea; the next paragraph makes it precise.\n      Both are molecules. A poly(ethene) molecule is thousands of times larger than an ethene molecule, so the forces between neighbouring chains are much stronger, strong enough to keep the chains in place at room temperature.\n    ' |
| 2 | Same commit, reduced-motion proof | `animation-name` normal motion = `ks4-arrive`, reduced motion = `none` → **swaps instantly: True** (matches `@media (prefers-reduced-motion: reduce) { [data-arrive] { animation: none !important; } }` in `Ks4Choice.dc.html`) |
| 3 | Click a button inside the flagship (`#s-classify`) | clicked=True; new text after click: '(no new tail text — state likely changed via attributes/marks rather than appended prose; see screenshot)' |
| 5 | Click #s-ladder rung 1's first option | feedback: 'Correct. A small molecule that joins with many others to make a polymer.' (class `ks3-feedback is-correct`) |
| 6 | Type 12+ words into the Write rung, click a still-enabled ladder button | ⚠️ **not a reliable measurement** — by this point rung 1 is already answered+disabled from step 5, so `#s-ladder button` (the click target) can land on rung 2/3's own controls rather than rung 4's *Check my answer*; ticks/tally seen: False. Script limitation, see README — not evidence either way about the Write rung's min-words unlock. |
| 7 | Click the key note's Cover/Uncover toggle | button label changed: True |

## 6. Findings

- **Page vs architecture (universal, applies here too — see NOTES §10, not repeated per point):** rung 2 is 'deduce or use data', not the architecture brief's 'units required'; the verbatim quiz lives in a Question bank after the key note, not folded into the ladder; the Route selector is a review affordance the generator must drop; comparison tables are card rows, not `<table>`.
- **Route-tag / build scope, this lesson:** #s-addition is Triple-only (8462 4.7.3.1/4.10.4.3, chemistry only, NOTES §8) — reference.json shows 14 sections on TH/TF against 13 on CF/CH.
- **Console:** clean across all 5 widths on the default route (0 errors).
- **Overflow:** none found at 390 or 360, any route swept.
- **Keyboard:** 0 controls with `tabindex="-1"` (none) — no keyboard gap found.
- **Reduced motion:** the shared `[data-arrive]` reveal mechanism swaps instantly (`animation-name: none`) — True.
- **Relevant NOTES §9 science flags for this lesson:** #7, #18 — see `NOTES-KS4-pilot.md` for the AQA-sourced text of each; not restated here since they are the examiners' remit (§4.2 of the run brief), not this inventory's.

Screenshots (Triple Higher, light): `$MRB_SHOTS/design/polymers-1280.png`, `$MRB_SHOTS/design/polymers-360.png`.
