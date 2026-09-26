# KS4 pilot — final live audit (26 Sep 2026)

Audited: the 54 pilot URLs on **https://mrbadmus.com**, live from main `08ae75e22` (the byte-identity of live
and the committed build was re-confirmed for `triple/higher/physics/electricity/resistors.html`: live bytes ==
`mrbadmus_site/` bytes). Read-only audit; nothing committed.

**Method.** Headless Chrome via `ks3_browser.py` (fresh browser per page, viewport set before navigating,
`prefers-color-scheme: light` forced with `measure_design.set_media` — headless Chrome's own default is dark).
Every page was walked at **360 and 1280** (108 walks) plus **one dark pass per lesson at 1280, Triple Higher**
(14 walks) — 122 full walks, ~83 min of browser time. Each walk: load → page checks → hook → flagship
instrument → CFIFA (where present) → ladder (4 rungs + retry) → key note → question bank → end-matter links →
page checks again → tutor → console. A separate 54-page pass (`innerText`-based) produced the route table,
and a separate pass the science spot-checks. All prev/next/connects links (62 distinct URLs) were fetched with
`curl -L`. Scripts and raw JSON are in the session scratchpad, not in the repo.

Screenshots (full page): `/Users/midebadmus/tmp/ks4-pilot-shots/live/<slug>-TH-360-light.png`,
`<slug>-TH-1280-light.png`, `<slug>-TH-1280-dark.png` — 42 files, 14 lessons × 3.

---

## 1. Defects (severity-ordered)

| ID | Severity | Where | What | Evidence / root cause |
|---|---|---|---|---|
| **D1** | **Degrades** (high) — a pupil cannot reach the AI tutor from any of the 54 pages | all 54 pages, both widths, light and dark | The "Ask Mr Badmus AI → **Ask about this lesson**" control does **not** open the tutor panel. It is an `<a href="#s-ladder">` that just jumps to the ladder; `#chatOverlay` stays `inert`, never gets `.open`. There is **no other** `[data-open-chat]` control on the page (count 0), so the tutor overlay, although loaded and `MrBadmus.init(…)`-ed, is unreachable. | Design's `Ks4End.dc.html` line 35 draws the CTA as `<a class="ks3-tutor-cta" href="#s-ladder">`; the port kept it verbatim. `mrbadmus.v2.js` only opens the panel from `[data-open-chat]` (KS3 lessons use `<button class="ks3-tutor-cta" data-open-chat>`; the pre-pilot KS4 pages also had a `data-open-chat` control). Regression versus the old KS4 pages. 122/122 walks: `open:false, inert:true`. |
| **D2** | **Degrades** | L10 giant-covalent-structures, **Combined Foundation + Combined Higher** | "Connects to → **Nanoparticles (Triple)**" is shown on Combined routes and links to `/triple/foundation/…/nanoparticles.html` (CF) and `/triple/higher/…/nanoparticles.html` (CH). The link resolves (200), but it sends a Combined pupil out of their route into chemistry-only content — the brief's rule is that Combined routes must not link to nanoparticles. | Only offender: every other Combined page has no nanoparticles link (L11 metals-alloys' *Next* on Combined correctly skips it). The `connects` list for L10 is not route-filtered. |
| **D3** | Cosmetic | all 54 pages | Console error on every load: `Failed to load resource: 404 … /favicon.ico`. The pilot pages ship **no `<link rel="icon">`**; the pre-pilot KS4 pages and KS3 pages carry the inline-SVG icon (`build_ks3.py` ~l.314), so the browser falls back to `/favicon.ico`, which does not exist. Pupils see no favicon in the tab. | Present in 122/122 walks; it is the **only** console line on any page. The `api/health` keep-alive line did not appear at all. |
| **D4** | Cosmetic (latent — only visible once D1 is fixed) | all 54 pages | The tutor overlay header reads **"KS3 Science Tutor"** (signed-out subtitle). Pre-pilot KS4 pages say "GCSE Science Tutor". | `build_ks4.tutor_block()` reuses `build_ks3.KS3_CHAT_OVERLAY` verbatim. |

No defect found that **blocks a pupil**. Nothing failed in the lesson itself: every hook, flagship, CFIFA, ladder
rung, key note and question bank worked on all 54 pages at both widths, in light and in dark.

### Observations for Mide (not scored as defects)

- **Coverage chips on every route.** The lesson header always carries `COMBINED · TRIPLE` and `FOUNDATION · HIGHER`
  (Design's "this lesson is on these pathways" chips; the examination rated them OK). So a Combined Foundation pupil
  does see the words "Triple" and "Higher" in the header. No Triple-only or Higher-only *content* leaks (see §3) —
  if the brief's "no Triple badge" rule is meant to cover these coverage chips too, that is a ruling for Mide.
- **Thin practice banks on physics.** L13 and L14 banks hold **2 items** on every route (no load-more); L9 polymers
  holds **4** on Combined routes. Matches the inventory; works, but thin.
- **"Draft — not yet science-reviewed."** is present as a string inside each page's compiled template (JSON in a
  `<script>`), but is **never rendered** (`.ks3-review-flag` elements: 0; not in visible text on any page).
- **L13/L14 RP strings** (series-parallel-circuits-C5, resistors-C13) are shipped in the page's data
  (`window.KS4SRC[slug].rp`, from `shared/ks4-source.js`) but the lesson pages do not render the `rp` field anywhere
  visible; L14's visible practical is the badge "Required practical · I–V characteristics". Old strings absent everywhere.
- **L6 heating curve** ran from 1:30 (42.6 °C) through the plateau (~68–69 °C) to 10:00 on every route; the
  anomaly and melting-point checks both answered.

---

## 2. The 54 pages

`walk ✓` = hook, flagship, CFIFA (where present), all four ladder rungs + "Retry my misses", key note and question
bank all responded as a pupil would expect. Page-level checks on **every** row, both widths, before and after the
walk: no visible "Draft" text; no Route `<select>`; zero occurrences of `unpkg`, `React`, `Babel`, `support.js` in
`outerHTML`; no "undefined"/"NaN"/"[object Object]" in rendered text; `scrollWidth == 360` at 360 (no horizontal
scroll). `tutor ✗` = D1. Console column = everything logged after the full walk; the only line is D3.

| # | Lesson | Route | 360 | 1280 | Console (both widths, after full walk) | Notes |
|---|---|---|---|---|---|---|
| 1 | L1 chemical-bonds | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 2 | L1 chemical-bonds | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 3 | L1 chemical-bonds | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 4 | L1 chemical-bonds | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 5 | L2 ionic-bonding | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 6 | L2 ionic-bonding | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 7 | L2 ionic-bonding | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 8 | L2 ionic-bonding | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 9 | L3 ionic-compounds | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 10 | L3 ionic-compounds | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 11 | L3 ionic-compounds | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 12 | L3 ionic-compounds | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 13 | L4 covalent-bonding | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 14 | L4 covalent-bonding | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 15 | L4 covalent-bonding | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 16 | L4 covalent-bonding | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 17 | L5 metallic-bonding | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 18 | L5 metallic-bonding | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 19 | L5 metallic-bonding | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 20 | L5 metallic-bonding | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 21 | L6 states-of-matter | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | heating ran 0:00→10:00, anomaly+MP checks answered |
| 22 | L6 states-of-matter | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | heating ran 0:00→10:00, anomaly+MP checks answered |
| 23 | L6 states-of-matter | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | heating ran 0:00→10:00, anomaly+MP checks answered |
| 24 | L6 states-of-matter | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | heating ran 0:00→10:00, anomaly+MP checks answered |
| 25 | L7 properties-ionic-compounds | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 26 | L7 properties-ionic-compounds | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 27 | L7 properties-ionic-compounds | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 28 | L7 properties-ionic-compounds | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 29 | L8 properties-small-molecules | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 30 | L8 properties-small-molecules | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 31 | L8 properties-small-molecules | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 32 | L8 properties-small-molecules | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 33 | L9 polymers | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | bank Combined Foundation: 4 items, no load-more |
| 34 | L9 polymers | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | bank Combined Higher: 4 items, no load-more |
| 35 | L9 polymers | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 36 | L9 polymers | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 37 | L10 giant-covalent-structures | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | **Connects-to links to /triple/…/nanoparticles** (D2) |
| 38 | L10 giant-covalent-structures | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | **Connects-to links to /triple/…/nanoparticles** (D2) |
| 39 | L10 giant-covalent-structures | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 40 | L10 giant-covalent-structures | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 41 | L11 metals-alloys | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 42 | L11 metals-alloys | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 43 | L11 metals-alloys | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 44 | L11 metals-alloys | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 |  |
| 45 | L12 nanoparticles | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | CFIFA 5/5 steps |
| 46 | L12 nanoparticles | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | CFIFA 5/5 steps |
| 47 | L13 series-parallel-circuits | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | bank Combined Foundation: 2 items, no load-more; switch closed → change 1 of 4 done; R_total chip present |
| 48 | L13 series-parallel-circuits | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | bank Combined Higher: 2 items, no load-more; switch closed → change 1 of 4 done; R_total chip present |
| 49 | L13 series-parallel-circuits | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | bank Triple Foundation: 2 items, no load-more; switch closed → change 1 of 4 done; R_total chip present |
| 50 | L13 series-parallel-circuits | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | bank Triple Higher: 2 items, no load-more; switch closed → change 1 of 4 done; R_total chip present |
| 51 | L14 resistors | CF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | bank Combined Foundation: 2 items, no load-more; 7 readings (5+, 2−) collected |
| 52 | L14 resistors | CH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | bank Combined Higher: 2 items, no load-more; 7 readings (5+, 2−) collected |
| 53 | L14 resistors | TF | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | bank Triple Foundation: 2 items, no load-more; 7 readings (5+, 2−) collected |
| 54 | L14 resistors | TH | walk ✓ · sw 360≤360 · tutor ✗ | walk ✓ · tutor ✗ | favicon.ico 404 | bank Triple Higher: 2 items, no load-more; 7 readings (5+, 2−) collected |

**Dark pass (1280, Triple Higher, all 14 lessons):** 14/14 walked clean; `.rd` ground `rgb(22, 18, 14)` with
`prefers-color-scheme: dark` matching; same single favicon line; same tutor result.

**Links:** all 62 distinct prev/next/connects URLs return 200 after redirects. Nanoparticles is linked from Combined
routes only in D2.

---

## 3. Walk-through findings per lesson (Triple Higher 1280 shown; the other routes and 360 behaved identically)

| Lesson | Hook | Flagship — what was done | Other | Ladder (r2 / r3 / r4) |
|---|---|---|---|---|
| L1 chemical-bonds | reveal appeared (+388 chars) | Bond decider: H+Li → called Ionic, "Try another pair", C+N → Covalent; chamber drew each and agreed/disagreed. Ca+C and H+Cl also driven for §5. | exam tip present | r2 checked · chain checked ("One card needs to move") · mark scheme opened at 20 words, self-marked |
| L2 ionic-bonding | ✓ | Stepper: Na+Cl (who loses → 1+ → the transfer…) then Mg+O; the "bond is the attraction, not the transfer" confront opened | | ✓ / ✓ / ✓ |
| L3 ionic-compounds | ✓ | Lattice lens: predicted 2 → one layer → neighbours in layer → +layers above/below = 6, with the "you said 2" reply | | ✓ / ✓ / ✓ |
| L4 covalent-bonding | ✓ | Shared-pair builder: cycled all 7 molecules, −/+ pairs, Check → "Not full yet" feedback with per-atom n-of-8 chips | | ✓ / ✓ / ✓ |
| L5 metallic-bonding | ✓ | Workbench: battery, heat, hammer; prediction answered; "layer slides one place" reveal | | ✓ / ✓ / ✓ |
| L6 states-of-matter | ✓ | **Start heating** ran the curve 0:00→10:00 (plateau ≈ 68–69 °C); anomaly select + MP entry → Check gave feedback | HT-only "Limits of the model" only on CH/TH | ✓ / ✓ / 6-mark level picked (4 of 6) |
| L7 properties-ionic-compounds | ✓ | Beakers: molten / solution predicted, "bulb lights" → ion-drift reveal | Be-the-examiner answered (see §5) | ✓ / ✓ / ✓ (6-mark) |
| L8 properties-small-molecules | ✓ | Two-forces model: slider to max → gated bp call answered → H₂O done → other molecules | | ✓ / ✓ / ✓ |
| L9 polymers | ✓ | Structure decider round 1 complete → round 2 (5 of 8 decided) | chem-only addition polymerisation only on Triple | ✓ / ✓ / ✓ |
| L10 giant-covalent-structures | ✓ | Diamond/graphite: bonds per atom, conductivity, hardness, m.p. — comparison table filled | **D2** on Combined | ✓ / ✓ / ✓ (6-mark) |
| L11 metals-alloys | ✓ | Alloy mixer: slider to 4 atoms, predicted, pushed → "alloy jams" reveal; pure-metal push | chem-only "Engineer's pick" only on Triple | ✓ / ✓ / ✓ |
| L12 nanoparticles (TF, TH) | ✓ | Cube splitter: predicted ×10, stepped 1000→100→10→1 nm | CFIFA 5/5 steps + Q1 checked | ✓ / ✓ / ✓ |
| L13 series-parallel-circuits | ✓ | Circuit bench: both meters predicted → **Close the switch** → reveal → "Next change" (1 of 4 changes) | CFIFA 5/5 + Q1; **no exam tip**; R_total chip ✓ | ✓ / ✓ / ✓ (6-mark) |
| L14 resistors | ✓ | Run the practical: component + graph call committed; **7 readings collected (5 positive, 2 negative)** after reversing connections on the filament lamp | CFIFA 5/5 + Q1; **no exam tip** | ✓ / ✓ / ✓ (6-mark) |

On every page: key note "Cover and recall" hid the lines, the button became "Uncover all", pressing it restored
them; question bank answered one item (status "1 of N answered"), "Show 4 more" took 4 → 8 items where present;
"Retry my misses" was enabled once all four rungs were tried and reset only the missed rungs.

---

## 4. Route correctness

| Check | Result |
|---|---|
| Combined routes: no Triple-only section | ✓ — L9 "Addition polymerisation (chemistry only)" and L11 "Alloys as useful materials (chemistry only)" appear on TF/TH only, with a "Contains Triple" chip there; on CF/CH only the explanatory footnote ("…show only on Triple routes") remains. Coverage chips: see Observations. |
| Foundation routes: no Higher-only section | ✓ — L6 "Limits of the model (HT only)" + "Contains Higher" chip on CH/TH only; absent on CF/TF. |
| Practice-set label matches the route | ✓ 54/54 ("Practice set · Combined Foundation", etc.) |
| Nanoparticles only on Triple | ✓ pages: `/combined/foundation/…/nanoparticles.html` and `/combined/higher/…/nanoparticles.html` return **404** ("Page not found \| MrBadmusAI") — not the old page. TF/TH return 200 with the new lesson. ✗ one inbound link: **D2**. |
| L13/L14 have no exam-tip block | ✓ 8/8 pages: `section[data-block=exam-tip]` count 0 and no "Examiner tip" text. The 12 chemistry lessons carry theirs. |
| L13 R_total card carries "Not on the sheet · learn it" | ✓ 4/4 routes: "NOT ON THE SHEET · LEARN IT — Rtotal = R₁ + R₂ for resistors in series only…" (V = I R card carries "Equation sheet"). |
| No Route `<select>` | ✓ 54/54 |

---

## 5. Science spot-checks (live, from `docs/ks4/examination/*.md` §2)

Each checked on Triple Higher **and** Combined Foundation (nanoparticles: TH + TF). "Visible" = in rendered page
text after the interaction that shows it; "old" checked absent from rendered text **and** from the full page HTML.

| # | Change | Trigger | New visible | Old absent |
|---|---|---|---|---|
| 1 | chemical-bonds-C4 key note: "Hydrogen is a non-metal, even though it has one outer electron like Group 1." | load | ✓ ✓ | ✓ ✓ |
| 2 | chemical-bonds-C1/C2: hook reveal "…even though, like sodium, it has one outer electron." and decider verdict "Hydrogen has one outer electron, like Group 1, but it is a non-metal." | hook click; decider H+Cl called Ionic or Metallic | ✓ ✓ (shows only on a wrong call, correctly) | ✓ ✓ |
| 3 | chemical-bonds-C10/C12 superscript/"undefined" fix | decider **Ca + C** → "Ionic: calcium carbide … the GCSE rule calls this ionic. Carbon rarely forms simple ions, so no formula is given…" | ✓ ✓ | ✓ no "undefined", no Ca₂C/C⁴⁻. **And no "undefined"/"NaN" in rendered text on any of the 54 pages, before or after the walk.** |
| 4 | ionic-bonding-C1 "For Groups 1, 2, 6 and 7, both end up with the electron arrangement of a noble gas." | load | ✓ ✓ | ✓ ✓ |
| 5 | covalent-bonding-C1 "like diamond and silicon dioxide (sand), where" | load | ✓ ✓ | ✓ ✓ |
| 6 | properties-ionic-compounds-C1 Be-the-examiner: 0 marks is correct | clicked "0 marks" → "Agreed. Zero. Having charged particles is not a marking point without free to move…" | ✓ ✓ | ✓ ✓ |
| 7 | metals-alloys-C8 "The table shows model data for the hardness of iron…" | load | ✓ ✓ | ✓ ✓ |
| 8 | nanoparticles-C2 "an atom has a radius of about 0.1 nm" (the brief quoted "about 0.2 nm across"; that phrase is the examiner's reasoning, the shipped `new` string is the radius wording) | load | ✓ ✓ | ✓ "about 0.1 nm across" gone |
| 9 | series-parallel-circuits-C5 "RP15 (Combined Science) / RP3 (Physics)" | page data | shipped in `KS4SRC` ✓ ✓; not rendered as visible text (the page has no `rp` slot) | ✓ "RP15 (Physics)" gone |
| 10 | resistors-C13 "RP16 (Combined Science) / RP4 (Physics)" + resistors-C1 method step 3 "…so that the resistor stays at a constant temperature." | page data; load | C13 in `KS4SRC` ✓ ✓ (not rendered); C1 visible ✓ ✓ | ✓ ✓ |

10/10 correct live. No science error observed during the walks (L6 plateau, L13 1 A / 4 V "before" circuit, L14 I–V
graph shapes all consistent with the spec).

---

## 6. Screenshots examined

- **chemical-bonds TH 1280 light** (top 1800 px): Design's double-chevron nav + breadcrumb; eyebrow "AQA CHEMISTRY
  5.2.1.1 · CLASSIFY", 74 px "Chemical bonds", rust big-question, the two coverage chips, hook card with orange offset
  shadow and four A–D options; explainer with bold key terms; bond-decider card with the group tray. Clean.
- **chemical-bonds TH 1280 dark**: same layout on the `#16120E` ground, cream type, salmon accents; option borders
  readable; no light-mode remnants.
- **chemical-bonds TH 360 light**: breadcrumb wraps to three lines under the brand; title, chips (stacked), hook card
  and options all fit the 360 column with the 16 px gutter; no clipping.
- **metals-alloys TH 360 light** (mid-page): alloy mixer lattice figure fits the card, slider and two prediction
  buttons full-width; amber "Think again · conducting" misconception card; "Build the chain" card. Clean.
- **series-parallel-circuits TH 1280 light** (mid-page): circuit bench with before/after circuits (A, V, R₁ 4 Ω, R₂
  8 Ω → 20 Ω, open switch drawn with hollow contacts), prediction chips, disabled "Close the switch" until both are
  predicted; "Sort the rules" card with Rₜₒₜₐₗ subscript rendering correctly.
- **resistors TH 360 light** (mid-page): RP card with the AQA circuit (battery, ammeter, resistor with voltmeter in
  parallel, variable resistor), the five-step method including the corrected step 3, risks; "Run the practical" with
  component chips and graph options A/B stacked. Clean.

---

## 7. Verdict

The 14 rebuilt lessons are live and work, end to end, on all 54 URLs at phone and desktop width, in light and dark:
every hook, flagship instrument (including the L6 heating curve, the L13 switch and the L14 practical with readings),
worked example, all four ladder rungs with retry, key note and practice bank behaved as a pupil would expect; no
page scrolls sideways at 360, no Design runtime or "Draft" text ships visibly, route gating is right (nanoparticles
404s on Combined, HT-only and chemistry-only sections appear only where they should, no exam tips on L13/L14, the
R_total chip is present), and all ten science spot-checks read correctly live. Nothing blocks a pupil. The one
material gap is **D1: the "Ask about this lesson" tutor button does nothing on all 54 pages** — the AI tutor is
loaded but unreachable — followed by **D2** (Combined L10 links out to the Triple nanoparticles page) and two
cosmetic items (missing favicon → the only console error; "KS3 Science Tutor" label). D1 and D2 are small generator
fixes (`data-open-chat` on the CTA as KS3 does; route-filter L10's `connects`), and should land before the other 250
pages are built from this template.
