# L2 · Ionic bonding · PROCESS

Inventory of `ks4-chemistry-5.2.1.2-ionic-bonding.dc.html`, measured in headless Chrome via `docs/ks4/pilot-inventory/measure_design.py` (25 Sep 2026). Method, widths, routes and standing law: see `README.md` in this folder — not restated here. AQA Chemistry 5.2.1.2.

**Console (default route, all 5 widths): clean.** 0 error(s) (favicon 404s filtered). **Overflow: none** at any of 1280/1340/820/390/360 — `document.documentElement.scrollWidth` equalled `innerWidth` at every width, on every route measured.

**Line-up (NOTES-KS4-pilot.md §7):** Hook (Na in Cl2) → Call-each-step stepper → Draw it yourself dot-and-cross builder (Li+F, K+Cl, Ca+O, Mg+S) → Formula forge (Al2O3 worked, then Li2S and Ca3N2; live charge meter; simplest-ratio check).

⚠️ **Misconception placement:** the confront ('the bond is the transfer') opens INSIDE the stepper at gate 3, not as a separate #s-think block — no section on this page carries the ks3-misconception class. Matches NOTES §10.5 ('Where the error is born inside an instrument … the confrontation is an amber panel inside the flagship, not a separate block'), named there for 'L2 gate 3' specifically.

## 1. Blocks and components in document order (Triple Higher, 1280)

`GEN?` marks against the closed KS3+KS4 vocabulary (14 KS3 types + `required-practical`/`equation`/`extended-response`/`exam-tip`) — every section here is classified to the CLOSEST registered type; the pilot's flagship instruments are NEW SHAPES inside that type (the vocabulary has no separate entry for a bespoke predict-then-reveal instrument, so `check` is the closest fit for most of them — see the per-block note where a different type fits better).

| # | id | block type | eyebrow / heading | words | box (x,y,w,h) |
|---|---|---|---|---|---|
| 1 | `—` | chrome | AQA Chemistry 5.2.1.2 · Process | 49 | 160,107,960,450 |
| 2 | `s-hook` | hook | Start here | 100 | 160,585,960,621 |
| 3 | `—` | — |  | 0 | 160,1206,960,0 |
| 4 | `—` | explainer |  | 89 | 160,1234,736,210 |
| 5 | `s-watch` | worked-example | Worked · call each step | 45 | 160,1472,960,758 |
| 6 | `—` | explainer |  | 62 | 160,2258,736,175 |
| 7 | `s-draw` | check | Your turn · draw the dot-and-cross diagram | 90 | 160,2461,960,886 |
| 8 | `s-forge` | check | Formula forge | 94 | 160,3375,960,577 |
| 9 | `—` | keyword | Command words in this lesson | 47 | 160,3980,960,268 |
| 10 | `—` | — |  | 27 | 160,4277,960,127 |
| 11 | `—` | explainer |  | 40 | 160,4432,960,164 |
| 12 | `s-ladder` | ladder | Extended response | 338 | 160,4624,960,2355 |
| 13 | `s-keynote` | key-note |  | 105 | 160,7013,960,484 |
| 14 | `—` | question-bank | Practice set · Triple Higher | 298 | 160,7531,960,1476 |
| 15 | `—` | — |  | 108 | 160,9040,960,458 |

**Flagship (§7):** `#s-watch` — Call-each-step stepper (Na+Cl then Mg+O; three gates — who loses, what charge, what holds them — with the 'the bond is the transfer' confront opening at gate 3).

## 2. Route matrix

| Route | sections (1280) | ladder rungs | ladder words | key-note lines | overflow 390/360 |
|---|---|---|---|---|---|
| TH | 15 | 4 | 338 | 6 | clean |
| CF | 15 | 4 | 338 | (TH only measured) | not swept (1280 only) |
| CH | 15 | 4 | 338 | (TH only measured) | not swept (1280 only) |
| TF | 15 | 4 | 338 | (TH only measured) | not swept (1280 only) |

**Question bank (Triple Higher, fully expanded via 2 'load more' clicks — see README's pagination note): 12 items.**

## 3. Rail + overflow per width (Triple Higher)

| Width | Rail | Overflow |
|---|---|---|
| 1280 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Sodium in chlorine') | clean |
| 1340 | side visible (5 nodes) · top hidden (CSS, >=1340) | clean |
| 820 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Sodium in chlorine') | clean |
| 390 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Sodium in chlorine') | clean |
| 360 | side hidden · top hidden (scrollY=0), **visible after scroll** ('0 of 5 done Sodium in chlorine') | clean |

Side rail appears only at >=1340 (CSS `@media (min-width:1340px)`, confirmed). **Below 1340, the top bar is NOT width-driven** — `Ks4Chrome`'s `showTop` comes from `state.scrolled = window.scrollY > 140`, set on a scroll listener, so at the top of a narrow page NEITHER rail is visible; scrolling past ~140px reveals the top bar. This is a genuine page behaviour (`Ks4Chrome.dc.html`), not a measurement artefact, and it is the same on every one of the 14 lessons.

**Keyboard (1280):** 57 focusable controls, 0 with `tabindex="-1"` (none found on this lesson) — every control is a real `<button>`/`<select>`/`<textarea>`, matching NOTES §2's 'all controls are real buttons, selects, ranges or inputs: keyboard-complete'.

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
  box: x192 y836 w896 h30 | `"Instrument Sans", system-ui, sans-serif` · 22px · 700 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x192 y836 w896 h30 |
| option_resting | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(251, 243, 230) · 2px solid rgb(221, 207, 182) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y881 w896 h65 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(243, 236, 224) · rgb(22, 18, 14) · 2px solid rgb(79, 68, 58) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y881 w896 h65 |
| misconception_panel | *(state-dependent; not present on a fresh mount — see Interactions)* | *(state-dependent; not present on a fresh mount — see Interactions)* |
| key_fact_card | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(255, 252, 245) · 2px solid rgb(34, 30, 27) · radius 20px · pad 18px 22px · shadow rgb(228, 87, 46) 5px 5px 0px 0px  
  box: x160 y4277 w960 h127 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgb(31, 26, 21) · 2px solid rgb(243, 236, 224) · radius 20px · pad 18px 22px · shadow rgb(240, 122, 78) 5px 5px 0px 0px  
  box: x160 y4277 w960 h127 |
| badge_pill | `"DM Mono", ui-monospace, monospace` · 13px · 500 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 2px solid rgb(34, 30, 27) · radius 99px · pad 4px 11px · shadow none  
  box: x160 y416 w172 h33 | `"DM Mono", ui-monospace, monospace` · 13px · 500 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 2px solid rgb(243, 236, 224) · radius 99px · pad 4px 11px · shadow none  
  box: x160 y416 w172 h33 |
| ladder_rung_header | `"Bricolage Grotesque", system-ui, sans-serif` · 36px · 800 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x195 y4659 w825 h58 | `"Bricolage Grotesque", system-ui, sans-serif` · 36px · 800 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x195 y4659 w825 h58 |
| check_button | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(251, 243, 230) · 2px solid rgb(221, 207, 182) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y881 w896 h65 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(243, 236, 224) · rgb(22, 18, 14) · 2px solid rgb(79, 68, 58) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y881 w896 h65 |
| key_note_card | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgba(0, 0, 0, 0) · 0px none rgb(34, 30, 27) · radius 0px · pad 0px · shadow none  
  box: x160 y7013 w960 h484 | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(243, 236, 224) · rgba(0, 0, 0, 0) · 0px none rgb(243, 236, 224) · radius 0px · pad 0px · shadow none  
  box: x160 y7013 w960 h484 |
| end_prev_next | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(169, 52, 17) · rgba(0, 0, 0, 0) · 0px none rgb(169, 52, 17) · radius 0px · pad 0px · shadow none  
  box: x184 y9104 w220 h29 | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(255, 158, 120) · rgba(0, 0, 0, 0) · 0px none rgb(255, 158, 120) · radius 0px · pad 0px · shadow none  
  box: x184 y9104 w220 h29 |

| reveal panel (`[data-arrive]`, after hook commit) | `"Instrument Sans", system-ui, sans-serif` · 19px · 400 · rgb(34, 30, 27) · rgb(252, 231, 222) · 2px solid rgb(228, 87, 46) · radius 18px · pad 18px 20px · shadow none  
  box: x192 y778 w896 h174 | *(dark not separately captured for state-dependent nodes — see README limitation)* |
| hook option, chosen (`aria-pressed=true`) | `"Instrument Sans", system-ui, sans-serif` · 18px · 600 · rgb(34, 30, 27) · rgb(252, 231, 222) · 2px solid rgb(228, 87, 46) · radius 16px · pad 16px 18px · shadow none  
  box: x192 y467 w896 h65 | *(as above)* |

## 5. Interactions driven, and observed text

| # | Trigger | Observed |
|---|---|---|
| 1 | Click #s-hook's first option | reveal text: '\n      Locked in. Hold that thought and test it below.\n      The electron moves from sodium to chlorine. Sodium is left with a full shell and one more proton than electrons; chlorine has a full shell and one extra electron. The white crystals are made of these charged particles, not of atoms.\n    ' |
| 2 | Same commit, reduced-motion proof | `animation-name` normal motion = `ks4-arrive`, reduced motion = `none` → **swaps instantly: True** (matches `@media (prefers-reduced-motion: reduce) { [data-arrive] { animation: none !important; } }` in `Ks4Choice.dc.html`) |
| 3 | Click a button inside the flagship (`#s-watch`) | clicked=True; new text after click: '(no new tail text — state likely changed via attributes/marks rather than appended prose; see screenshot)' |
| 5 | Click #s-ladder rung 1's first option | feedback: 'Not this time. Electrons are transferred, not destroyed — charge is conserved. The compound is neutral because the ion charges balance.' (class `ks3-feedback is-wrong`) |
| 6 | Type 12+ words into the Write rung, click a still-enabled ladder button | ⚠️ **not a reliable measurement** — by this point rung 1 is already answered+disabled from step 5, so `#s-ladder button` (the click target) can land on rung 2/3's own controls rather than rung 4's *Check my answer*; ticks/tally seen: False. Script limitation, see README — not evidence either way about the Write rung's min-words unlock. |
| 7 | Click the key note's Cover/Uncover toggle | button label changed: True |

## 6. Findings

- **Page vs architecture (universal, applies here too — see NOTES §10, not repeated per point):** rung 2 is 'deduce or use data', not the architecture brief's 'units required'; the verbatim quiz lives in a Question bank after the key note, not folded into the ladder; the Route selector is a review affordance the generator must drop; comparison tables are card rows, not `<table>`.
- **Misconception placement, this lesson:** the confront ('the bond is the transfer') opens INSIDE the stepper at gate 3, not as a separate #s-think block — no section on this page carries the ks3-misconception class. Matches NOTES §10.5 ('Where the error is born inside an instrument … the confrontation is an amber panel inside the flagship, not a separate block'), named there for 'L2 gate 3' specifically.
- **Console:** clean across all 5 widths on the default route (0 errors).
- **Overflow:** none found at 390 or 360, any route swept.
- **Keyboard:** 0 controls with `tabindex="-1"` (none) — no keyboard gap found.
- **Reduced motion:** the shared `[data-arrive]` reveal mechanism swaps instantly (`animation-name: none`) — True.
- **Relevant NOTES §9 science flags for this lesson:** #16, #18 — see `NOTES-KS4-pilot.md` for the AQA-sourced text of each; not restated here since they are the examiners' remit (§4.2 of the run brief), not this inventory's.

Screenshots (Triple Higher, light): `$MRB_SHOTS/design/ionic-bonding-1280.png`, `$MRB_SHOTS/design/ionic-bonding-360.png`.
