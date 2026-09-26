# L11 · Metals and alloys · CONTRAST

Inventory of `ks4-chemistry-5.2.2.7-metals-alloys.dc.html`, measured in headless Chrome via `docs/ks4/pilot-inventory/measure_design.py` (25 Sep 2026). Method, widths, routes and standing law: see `README.md` in this folder — not restated here. AQA Chemistry 5.2.2.7.

**Console (default route, all 5 widths): clean.** 0 error(s) (favicon 404s filtered). **Overflow: none** at any of 1280/1340/820/390/360 — `document.documentElement.scrollWidth` equalled `innerWidth` at every width, on every route measured.

**Line-up (NOTES-KS4-pilot.md §7):** Hook (24 vs 18 carat) → Alloy mixer → spot-the-flaw (metals must melt) → Ks4Chain banker No.3 → Triple: engineer's pick (steel, aluminium alloy, bronze or brass).

⚠️ #s-pick ('engineer's pick') is Triple-only (8462 4.10.4.2, chemistry only, NOTES §8) — reference.json shows 15 sections on TH/TF against 14 on CF/CH.

## 1. Blocks and components in document order (Triple Higher, 1280)

`GEN?` marks against the closed KS3+KS4 vocabulary (14 KS3 types + `required-practical`/`equation`/`extended-response`/`exam-tip`) — every section here is classified to the CLOSEST registered type; the pilot's flagship instruments are NEW SHAPES inside that type (the vocabulary has no separate entry for a bespoke predict-then-reveal instrument, so `check` is the closest fit for most of them — see the per-block note where a different type fits better).

| # | id | block type | eyebrow / heading | words | box (x,y,w,h) |
|---|---|---|---|---|---|
| 1 | `—` | chrome | AQA Chemistry 5.2.2.7–5.2.2.8 · Contrast | 66 | 160,107,960,517 |
| 2 | `s-hook` | hook | Start here | 110 | 160,652,960,621 |
| 3 | `—` | — |  | 0 | 160,1273,960,0 |
| 4 | `—` | explainer |  | 77 | 160,1301,736,175 |
| 5 | `s-mixer` | practical | The alloy mixer | 57 | 160,1504,960,491 |
| 6 | `s-think` | misconception | Think again · conducting | 104 | 160,2023,960,549 |
| 7 | `s-chain` | comparison | Build the chain | 146 | 160,2600,960,805 |
| 8 | `s-pick` | check | Alloys as useful materials · AQA 4.10.4.2 (chemistry only) | 111 | 160,3433,960,605 |
| 9 | `—` | keyword | Command words in this lesson | 36 | 160,4066,960,217 |
| 10 | `—` | — |  | 27 | 160,4311,960,127 |
| 11 | `—` | explainer |  | 53 | 160,4467,960,194 |
| 12 | `s-ladder` | ladder | Extended response | 354 | 160,4689,960,2577 |
| 13 | `s-keynote` | key-note |  | 106 | 160,7300,960,574 |
| 14 | `—` | question-bank | Practice set · Triple Higher | 296 | 160,7908,960,1419 |
| 15 | `—` | — |  | 102 | 160,9360,960,464 |

**Flagship (§7):** `#s-mixer` — Alloy mixer (0-4 larger atoms distort the layers; predict, then push: pure slides one place, alloy jams).

## 2. Route matrix

| Route | sections (1280) | ladder rungs | ladder words | key-note lines | overflow 390/360 |
|---|---|---|---|---|---|
| TH | 15 | 4 | 354 | 6 | clean |
| CF | 14 | 4 | 324 | (TH only measured) | not swept (1280 only) |
| CH | 14 | 4 | 354 | (TH only measured) | not swept (1280 only) |
| TF | 15 | 4 | 324 | (TH only measured) | not swept (1280 only) |

**Question bank (Triple Higher, fully expanded via 2 'load more' clicks — see README's pagination note): 12 items.**

## 3. Rail + overflow per width (Triple Higher)

| Width | Rail | Overflow |
|---|---|---|
| 1280 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Gold rings') | clean |
| 1340 | side visible (5 nodes) · top hidden (CSS, >=1340) | clean |
| 820 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Gold rings') | clean |
| 390 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Gold rings') | clean |
| 360 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Gold rings') | clean |

Side rail appears only at >=1340 (CSS `@media (min-width:1340px)`, confirmed). **Below 1340, the top bar is NOT width-driven** — `Ks4Chrome`'s `showTop` comes from `state.scrolled = window.scrollY > 140`, set on a scroll listener, so at the top of a narrow page NEITHER rail is visible; scrolling past ~140px reveals the top bar. This is a genuine page behaviour (`Ks4Chrome.dc.html`), not a measurement artefact, and it is the same on every one of the 14 lessons.

**Keyboard (1280):** 67 focusable controls, 0 with `tabindex="-1"` (none found on this lesson) — every control is a real `<button>`/`<select>`/`<textarea>`, matching NOTES §2's 'all controls are real buttons, selects, ranges or inputs: keyboard-complete'.

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
  box: x192 y903 w896 h30 | `"Instrument Sans", system-ui, sans-serif` · 22px · 700 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x192 y903 w896 h30 |
| option_resting | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(251, 243, 230) · 2px solid rgb(221, 207, 182) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y949 w896 h65 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(243, 236, 224) · rgb(22, 18, 14) · 2px solid rgb(79, 68, 58) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y949 w896 h65 |
| misconception_panel | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(255, 243, 212) · 2px solid rgb(34, 30, 27) · radius 28px · pad 30px · shadow rgb(34, 30, 27) 5px 5px 0px 0px  
  box: x160 y2023 w960 h549 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgb(51, 41, 15) · 2px solid rgb(243, 236, 224) · radius 28px · pad 30px · shadow rgb(243, 236, 224) 5px 5px 0px 0px  
  box: x160 y2023 w960 h549 |
| key_fact_card | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(255, 252, 245) · 2px solid rgb(34, 30, 27) · radius 20px · pad 18px 22px · shadow rgb(228, 87, 46) 5px 5px 0px 0px  
  box: x160 y4311 w960 h127 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgb(31, 26, 21) · 2px solid rgb(243, 236, 224) · radius 20px · pad 18px 22px · shadow rgb(240, 122, 78) 5px 5px 0px 0px  
  box: x160 y4311 w960 h127 |
| badge_pill | `"DM Mono", ui-monospace, monospace` · 13px · 500 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 2px solid rgb(34, 30, 27) · radius 99px · pad 4px 11px · shadow none  
  box: x160 y483 w172 h33 | `"DM Mono", ui-monospace, monospace` · 13px · 500 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 2px solid rgb(243, 236, 224) · radius 99px · pad 4px 11px · shadow none  
  box: x160 y483 w172 h33 |
| ladder_rung_header | `"Bricolage Grotesque", system-ui, sans-serif` · 36px · 800 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x195 y4724 w825 h58 | `"Bricolage Grotesque", system-ui, sans-serif` · 36px · 800 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x195 y4724 w825 h58 |
| check_button | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(251, 243, 230) · 2px solid rgb(221, 207, 182) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y949 w896 h65 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(243, 236, 224) · rgb(22, 18, 14) · 2px solid rgb(79, 68, 58) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y949 w896 h65 |
| key_note_card | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x160 y7300 w960 h574 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x160 y7300 w960 h574 |
| end_prev_next | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(169, 52, 17) · rgba(0, 0, 0, 0) · 0px none rgb(169, 52, 17) · radius 0px · pad 0px · shadow none  
  box: x184 y9421 w261 h58 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(255, 158, 120) · rgba(0, 0, 0, 0) · 0px none rgb(255, 158, 120) · radius 0px · pad 0px · shadow none  
  box: x184 y9421 w261 h58 |

| reveal panel (`[data-arrive]`, after hook commit) | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(252, 231, 222) · 2px solid rgb(228, 87, 46) · radius 18px · pad 18px 20px · shadow none  
  box: x192 y778 w896 h143 | *(dark not separately captured for state-dependent nodes — see README limitation)* |
| hook option, chosen (`aria-pressed=true`) | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(252, 231, 222) · 2px solid rgb(228, 87, 46) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y468 w896 h65 | *(as above)* |

## 5. Interactions driven, and observed text

| # | Trigger | Observed |
|---|---|---|
| 1 | Click #s-hook's first option | reveal text: '\n      Locked in. Push some layers and find out.\n      The other metal atoms are a different size from gold atoms. They distort the neat layers, and distorted layers cannot slide past each other easily.\n    ' |
| 2 | Same commit, reduced-motion proof | `animation-name` normal motion = `ks4-arrive`, reduced motion = `none` → **swaps instantly: True** (matches `@media (prefers-reduced-motion: reduce) { [data-arrive] { animation: none !important; } }` in `Ks4Choice.dc.html`) |
| 3 | Click a button inside the flagship (`#s-mixer`) | clicked=True; new text after click: '(no new tail text — state likely changed via attributes/marks rather than appended prose; see screenshot)' |
| 5 | Click #s-ladder rung 1's first option | feedback: 'Correct. A mixture of a metal with at least one other element, usually another metal.' (class `ks3-feedback is-correct`) |
| 6 | Type 12+ words into the Write rung, click a still-enabled ladder button | ⚠️ **not a reliable measurement** — by this point rung 1 is already answered+disabled from step 5, so `#s-ladder button` (the click target) can land on rung 2/3's own controls rather than rung 4's *Check my answer*; ticks/tally seen: False. Script limitation, see README — not evidence either way about the Write rung's min-words unlock. |
| 7 | Click the key note's Cover/Uncover toggle | button label changed: True |

## 6. Findings

- **Page vs architecture (universal, applies here too — see NOTES §10, not repeated per point):** rung 2 is 'deduce or use data', not the architecture brief's 'units required'; the verbatim quiz lives in a Question bank after the key note, not folded into the ladder; the Route selector is a review affordance the generator must drop; comparison tables are card rows, not `<table>`.
- **Route-tag / build scope, this lesson:** #s-pick ('engineer's pick') is Triple-only (8462 4.10.4.2, chemistry only, NOTES §8) — reference.json shows 15 sections on TH/TF against 14 on CF/CH.
- **Console:** clean across all 5 widths on the default route (0 errors).
- **Overflow:** none found at 390 or 360, any route swept.
- **Keyboard:** 0 controls with `tabindex="-1"` (none) — no keyboard gap found.
- **Reduced motion:** the shared `[data-arrive]` reveal mechanism swaps instantly (`animation-name: none`) — True.
- **Relevant NOTES §9 science flags for this lesson:** #19, #18 — see `NOTES-KS4-pilot.md` for the AQA-sourced text of each; not restated here since they are the examiners' remit (§4.2 of the run brief), not this inventory's.

Screenshots (Triple Higher, light): `$MRB_SHOTS/design/metals-alloys-1280.png`, `$MRB_SHOTS/design/metals-alloys-360.png`.
