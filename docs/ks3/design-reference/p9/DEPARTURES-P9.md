# DEPARTURES — P9 *Static electricity*

Design's page is the default and it stays unless the change can be defended
to an examiner. ⊕ **Widened by Mide, 25 Aug 2026:** a deliberate, registered
improvement is allowed where the lane genuinely judges that its version
teaches better — *"if code genuinely think it's clearer his way, let him
effect the changes, it's fine"* — so the old "name the defect in hers"
column becomes a RATIONALE column. What did not widen: her STRUCTURE is
untouched, MRB-205 stands, and the register is expected to be SHORT. A row
that would not be defended to Mide is not written.

**This one has SIX changed rows and SIX considered-not-changed rows.** Two
are contrast repairs, two are length tells at her own threshold, one is a
narrow-viewport repair and one is a lower-case sentence. Nothing in her
physics moved, and nothing in her structure did.

There are also **two findings at the end that are not departures from
anything of hers**: a duplicated head row on every P4/P5/P6 bench, which is
on live pages; and a flaky gate, which fails at random on pages that are
correct.

---

## Changed — 6 rows

### 1. Every fixed SVG caption moves from `#8C8177` to `--ks3-on-dark-muted`

| | |
|---|---|
| **Where** | All three benches. `ELECTRONS`, `LEFT HAND`, `RIGHT HAND`, `PROTONS DO NOT MOVE` (`p9-01`); `INSULATING STANDS ON A BENCH` (`p9-02`); `EVERY ARROW POINTS THE WAY A SMALL POSITIVE CHARGE WOULD BE PUSHED` (`p9-03`). |
| **What she drew** | `fill: #8C8177` at 14–15px, on `--ks3-dark-panel` (`#3E3730`). |
| **What is built** | `fill: var(--ks3-on-dark-muted)` (`#C6B9A7`). Same size, same face, same words. |
| **Rationale** | **Measured: `#8C8177` on `#3E3730` is 3.08:1.** At 14–15px that is body-size text and the bar is 4.5:1, so it fails AA — and `shared/tokens.css` warns about this exact composite beside `--ks3-on-dark-muted`. The token is 6.09:1 on the same ground and is what the token law already names for a caption on an ink-dark block. This is the call P6 made for the same strings and the same reason; making it again is consistency, not preference. |

### 2. `p9-03`'s field grid moves from `#6E655D` to `#8C8177`

| | |
|---|---|
| **Where** | `p9-03` `#s-field` — the ninety-one grid arrows, which ARE the instrument's picture |
| **What she drew** | `stroke: #6E655D` at 3px, on `--ks3-dark-panel`. |
| **What is built** | `stroke: #8C8177` at 3px — a colour already on her own drawing, one step brighter. |
| **Rationale** | **Measured: `#6E655D` on `#3E3730` is 2.05:1**, below the 3:1 bar for a meaningful graphic — and this graphic is not decoration, it is the thing the whole lesson asks the student to read. `#8C8177` is 3.08:1 and clears it. It is deliberately NOT lifted to `--ks3-on-dark-muted`: the hierarchy she drew puts the grid a step below the charges and the test point, and flattening that would make the map harder to read rather than easier. Her own palette supplied the replacement. |

### 3. One distractor is finished on `p9-01`'s rung 2

| | |
|---|---|
| **Where** | `p9-01` mastery ladder, rung 2, her option D |
| **What she wrote** | *"Charge was created, but an equal amount of positive charge was created on the jumper at the same time, so it balances."* — 22 words, against a 27-word correct answer. |
| **What is built** | The same wrong rule, finished: *"…so the two new charges balance and the total stays zero."* — 30 words. **Her correct answer is untouched to the character and her correction for this option is untouched.** The option's INDEX also moves, for an unrelated reason that is engine policy rather than a departure — see the note below this table. |
| **Rationale** | **`verify_ks3`'s own threshold: correct is strictly the longest and clears the longest distractor by ≥4 words.** 27 against 22 is 5, so a student can score this rung by choosing the longest option without reading it. The remedy is always at the distractor — never shorten a correct answer, never move an index to fix a tell — and the added clause states the belief completely rather than padding it. |

⚠️ **MRB-278 · THE ORDER OF EVERY MARKED RUNG'S OPTIONS MOVES, AND IT IS NOT
A ROW HERE.** All six marked rungs in P9 put the correct answer at index 0,
which is the exact defect the position gate fails a unit for — a student
scores the whole unit by pressing the first button. Measured across the six
sets before: `[6, 0, 0, 0]`. After: `[1, 2, 2, 1]`, with every index used and
none over half. **Every option's text and every correction is verbatim; only
the ORDER changes, and the `answer` index follows the correct option.** That
is engine policy, recorded in each lesson's own docstring, and it is
explicitly not the length-tell remedy — which never moves an index.

### 4. Two hooks get a finished distractor, for the same reason and a sharper one

| | |
|---|---|
| **Where** | `p9-02`'s hook (her option C) and `p9-03`'s hook (her option D) |
| **What she wrote** | `p9-02` C: *"…so it is held by ordinary friction"* — 15 words against a 22-word correct option. `p9-03` D: *"…and the two attract directly"* — 13 words against 17. |
| **What is built** | `p9-02` C: *"…so it is held to the wall by ordinary friction and nothing electrical"* — 21 words. `p9-03` D: *"…and two opposite charges pull on each other directly across the gap"* — 20 words. Both correct options untouched. |
| **Rationale** | The same measured tell as row 3 — and on a HOOK it does more damage than anywhere else. A hook exists to make a student COMMIT to a wrong idea so that the reveal underneath can take it apart; a student who spots the answer by its length never commits, and a belief nobody commits to cannot be confronted. `p9-03` D's added clause is also the better distractor on its own terms: it now names the belief `CHRG-05` is about rather than gesturing at it. |

### 5. `p9-01`'s branch note starts with a capital letter

| | |
|---|---|
| **Where** | `p9-01` `#s-rub`, the note panel, both transfer directions |
| **What she wrote** | `note = A.name.toLowerCase() + ' sits above ' + …` — so the panel renders *"polythene rod sits below wool duster on the list, so it holds its electrons more tightly…"*, a paragraph beginning in lower case. |
| **What is built** | The identical sentence with its first letter capitalised. Every word is hers; nothing else about the note moves, and the two branches that already begin with a capital are untouched. |
| **Rationale** | It is a paragraph in a panel of its own, not a clause continuing something above it. Starting it in lower case reads as a typesetting fault rather than as a choice, and a student reading the bench's only prose meets it first. Applied in the wiring, once, so it cannot drift per branch. |

### 6. The triboelectric ladder's rows wrap on a phone

| | |
|---|---|
| **Where** | `p9-01`'s ladder figure — the seven material rows |
| **What she drew** | One non-wrapping flex row per material: badge, name, and the tell (*"most likely to end up positive"*) at `flex: 0 0 auto`. |
| **What is built** | The same row with `flex-wrap: wrap`, so the tell drops to its own line when it will not fit beside the name. Identical at 820px and above. |
| **Rationale** | **Measured at 360 and 390: the row runs to 464px and the DOCUMENT scrolls sideways.** A page body that scrolls horizontally on a phone is the one responsive failure the build treats as unconditional, and below 1340px the narrow rail is the only rail a student sees — this is a phone-first page. Nothing is lost: the tell is still on the row, one line down. |

---

## Considered, not changed — 6 rows

**⚖️ THE CHARGE CEILING (her FLAG 8) — SATISFIED BY HER OWN PAGE.** Mide
ruled on 21 Aug 2026 that `p9-01`'s model must have one, because a model
that climbs for ever teaches *rub harder, get more, without limit*. Her
NOTES say the model has none; **her page has `STROKE_CEIL = 26.3` and
`STROKE_TAU = 14`**, so the stroke term is `26.3 × (1 − e^(−r/14))`, and her
legal line says the term levels off *"because a real charge leaks away and
because the air eventually breaks down"*. The drawing was measured and
ported exactly. `r_transfer_pair` now REFUSES a payload with no ceiling, so
the ruling is structural rather than a note. **This is a notes-versus-
drawing contradiction, not a change** — see the section below.

**⚖️ THE INDUCED-ATTRACTION COEFFICIENT (her FLAG 9) — ACCEPTED, AND HER
PAGE ALREADY HOLDS THE LINE.** Mide accepted the chosen coefficient on
condition that induced attraction is reported in relative words only, with
no absolute force in newtons anywhere on the page. Her page prints no figure
at all for the induced case — the strength tile's sub-line is *"a small
fraction of the charged pair at this gap"* — and the like/unlike cases carry
her declared relative scale with 100 at the closest fully charged pair.
Nothing moved. `r_charge_pair` walks the whole payload and refuses one that
names a newton, so a later edit cannot lose it.

**⚖️ `p9-01` CARRIES NO FORMULA BLOCK AND KEEPS BOTH READOUTS (her FLAG 4).**
`Q = n × e` is a genuine product and would take a triangle cleanly. Ruled:
no block, because the coulomb and the elementary charge are both GCSE and
`STAT.01` names neither; and BOTH readouts stay, because the count of
electrons alone would weaken the equal-and-opposite point that is the
lesson. Her page is built as drawn.

**⚖️ NO SAFEGUARDING BLOCK ON `p9-03` (her §6).** Its *Going further*
explains why a car is safe in a thunderstorm and rung 4 asks for it. That is
safety information a student is being GIVEN, not a risk they are being asked
to disclose, and adding the block would dilute a block that means something
where it is used. Ruled the same way by Mide and by Design, independently.

**⊖ `p9-03`'s TEST POINT STAYS AMBER, AND `--ks3-data` IS THE WRONG TOKEN
HERE.** 5A.2 sends a selection mark to `--ks3-data`, and Design's own token
law says the token *"applies from P10 onward"* with P8/P9 using the
substitution in her §9 — which records amber on this marker as one of four
declared uses. The measured reason it stays: **`--ks3-data` is `#8FB7FF`,
which is the colour of the ninety-one field arrows the test point has to be
distinguishable from.** The substitution would erase the distinction rather
than improve it, the reading is carried in words in two tiles as well, and
amber on `--ks3-dark-panel` is 7.43:1. Flagged rather than applied.

**⊖ `p9-01`'s FOURTH TILE IS A CONSTANT AND IT STAYS A TILE.** `0.0 nC ·
nothing was created` never changes however hard a student rubs, and a
constant in a row of live readouts is the shape 5A.1 usually calls a defect.
Kept, because here the CONSTANCY is the lesson — it is the one reading on
the bench that answers the page's own big question — and it is written on
every repaint rather than left in the shipped bytes, so it is a live claim
about the state and not a caption beside it.

---

## Notes versus drawing — 1 contradiction, and the drawing won

⚠️ **HER FLAG 8 SAYS `p9-01`'s CHARGE MODEL HAS NO CEILING. HER `p9-01` PAGE
HAS ONE.**

`NOTES-P8-P9.md` §9 item 4: *"FLAG 8 — `p9-01`'s charge model has no
ceiling. Twenty strokes of hair against PVC gives about 38 nC … the model
would keep climbing if the slider went further. A real charge stops rising
because it leaks and because the air eventually breaks down. **The legal
line says so; the model does not implement it.**"*

`p9-01-charging-by-rubbing.dc.html`, lines 438–443 (and line 647):

```js
const PER = 2.0e9;
// Charge approaches a ceiling: it leaks away and the air eventually breaks down.
// STROKE_CEIL and STROKE_TAU are set so 20 strokes still lands where the linear
// model landed, and the curve is visibly flattening by then.
const STROKE_TAU = 14;
const STROKE_CEIL = 26.3;
```

and `strokeFactor = STROKE_CEIL * (1 - Math.exp(-s.rubs / STROKE_TAU))`.

**Measured on her own constants:** at 20 strokes `strokeFactor` = 20.00,
which is exactly where the straight line `strokeFactor = rubs` would have
put it; at 10 strokes it is 13.43 against a straight line's 10.00; the gain
from the nineteenth stroke to the twentieth is 0.467 against the first
stroke's 1.813 — a quarter of it. The curve is real and it is bending. Her
branch note carries a `nearCeiling` sentence that fires above `0.55 ×
STROKE_CEIL`, from twelve strokes on, and says the charge *"is levelling off
towards a ceiling, because it leaks away into the air as fast as more of it
is separated"*.

Her flag's own figure confirms the port: hair against PVC at twenty strokes
is six rungs apart, and `26.3 × (1 − e^(−20/14)) × 2.0e9 × 6 × 1.602e−10` is
**38.4 nC** — *"about 38 nC"*, exactly as she writes it.

The note is stale and the page is right, so the page is what is built. The
ruling that was made against the note is satisfied by the drawing, and it is
recorded as satisfied rather than as a change.

**No other contradiction was found.** Her §5 state-space table, her §10
family list and her §8 hedge list all match the three pages as delivered.

---

## Hedges carried through verbatim

Design's §8 names them load-bearing and they are not tidied anywhere:

* **"about"** on every triboelectric prediction (`p9-01`'s legal line, the
  ladder's `most likely to end up positive` / `negative`) and on every
  relative strength in `p9-02`.
* **"likely outcome, not a certainty"** on the transfer direction, in
  `p9-01`'s legal line.
* **"middling — poor at either job"** on cotton, which is the one row of the
  ladder that tells a student not to use it.
* **"almost"** on the field inside a conductor being zero — `p9-03`'s
  *Going further* and its rung 4 criteria both say *very nearly zero*.
* **"typical of a rubbed rod"** on the nanocoulomb figures, and **"are not
  measurements"** on the same line.

## What is not ported

Her `ks3-review-flag` (*"Draft — not yet science-reviewed."*) and the
`showDraft` prop, on all three pages. Engine policy, no register row: no
draft marking appears anywhere a student can see, and `verify_ks3` asserts
it. The concept was swept as well as the string — nothing on the three built
pages says *draft*, *review*, *not yet checked* or *provisional*.

---

## A finding about FOUR OTHER UNITS, on live pages

⚠️ **EVERY P4, P5 AND P6 BENCH THAT AUTHORS A `progress` SHIPS ITS EYEBROW,
ITS HEADING AND ITS READOUT TWICE.** This is not a departure from anything of
Design's — her pages are correct — and it is not P9's to fix. It is reported
because it was found here and because it is in front of students.

`ks3/physics/waves-and-sound/sound-needs-a-medium.html` renders

```html
<h2>Same bang. Change what is in the way.</h2>
…
<h2>Same bang. Change what is in the way.</h2>
```

one line under the other, with the eyebrow and the "Change a control to
begin" readout doubled with it.

**The mechanism.** `r_activity`'s shell draws the block's head row from
`eyebrow` / `heading` / `progress`. P4, P5 and P6 each define a private
`_head(hook, a)` that draws the same three from the same keys, and every
bench calls it. Both draw.

`_kinds_consuming` exists precisely to stop this: it decides whether the
SHELL should draw the readout by searching the drawer's own source for
`a.get("progress")`. In P4/P5/P6 that string is inside `_head` — a different
function — so the search finds nothing and the shell draws one too. The
mechanism is sound; a helper hid the read from it.

**Why no gate saw it.** Every gate in the build counts elements, asserts they
respond to their controls, or compares against the rail manifest. Two correct
head rows are two correct head rows. It is visible only by looking at the
page, which is how it was found here — on P9's first bench screenshot.

**P9 has no `_head`.** The shell owns the head row, `progress` is authored as
a map of named states so it routes to `_progress_readout`, and the wiring
drives it through the engine's own `setCountState`. That is the fix; applying
it to P4, P5 and P6 is four units' worth of built pages and belongs to
whoever owns them.

Measured: 2 `ks3-blockhead` on each P9 page against 6 on `p6-06`, and zero
duplicated `<h2>` on all three P9 pages.

⊕ **Fixed 25 Aug 2026 (MRB-223), on P4, P5 and P6 themselves** — see the
`⊕ Fixed` section at the end of each of `DEPARTURES-P4.md`, `-P5.md` and
`-P6.md`. Measured after: zero duplicated `<h2>` on all 22 pages.

---

## A finding about A GATE — `ks3_figure_sweep` is flaky, and here is exactly why

⚠️ **`verify_ks3.py`'s figure sweep FAILS AT RANDOM, on pages that are
correct, because it treats the engine's own live backend ping as a defect.**
Not P9's, not any unit's, and worth a ticket rather than a shrug — a gate
that fails at random is how people learn to ignore gates.

**Measured on this run.** Two consecutive `verify_ks3.py` runs, on a tree
that did not change between them:

| run | exit | result |
|---|---|---|
| 1 | **1** | `❌ 1 FAILED: ⊕ MRB-254 · every drawn figure reads at 390, 768 and 1440` — 4 problems, all on `b3 the-digestive-system` and `b7 leaves-built-for-the-job`, all of them CORS / `net::ERR_FAILED` on `mrbadmus-backend.onrender.com/api/health` |
| 2 | **0** | `✅ all automated gates pass · 3 items remain MANUAL` — 187 checks, 0 failures |

**The mechanism, in full.** `shared/mrbadmus.v2.js` is on every KS3 page and
carries a Render warm-up ping:

```js
// Also ping immediately on page load to warm up Render
setTimeout(function () {
  fetch('https://mrbadmus-backend.onrender.com/api/health').catch(function(){});
}, 2000);
```

`.catch()` swallows the promise rejection but **cannot** suppress Chrome's own
console entries for a CORS violation or a failed resource — those are
browser-level logs. `ks3_figure_sweep.py` reads console errors right after its
probe and appends EVERY one as a problem, unfiltered:

```python
logs = [m for m in (page.console_errors() if hasattr(page, "console_errors") else [])]
…
for m in logs:
    problems.append("FIGURE SWEEP: /%s at %dpx logged a console error: %s" % (rel, w, m))
```

Note the list comprehension: it is shaped like a filter and filters nothing.

So the gate fails whenever a page load takes longer than the 2-second timer
plus the round trip — which on a 156-page × 3-width sweep on a busy machine
happens occasionally and nowhere in particular. **Run 1 caught it twice in
468 loads (0.4%).**

**Independently confirmed.** The two pages the gate named were reloaded at
the three sweep widths, three times each, plus two P9 pages and a P6 control
— **45 loads, zero console errors on any of them.** The pages are innocent;
the timing is the variable.

**Not fixed here, deliberately.** `ks3_figure_sweep.py` is a shared gate file,
and narrowing what it accepts is weakening a gate — which this run is not
permitted to do and should not want to. The fix is somebody's ticket, and it
is small: ignore console entries whose URL is the backend origin, or stub the
host in the sweep's own server. Either keeps the gate's real power — a figure
that throws is still a failure — while removing a live-network dependency
from a build gate.

---

## ⊖ Commander's Phase 3 — two reverts, 25 Aug 2026

The built pages were compared against her JavaScript constants and her HTML
prose, string by string, after the executor's own pass. Two of hers were not
on the page. Both are REVERTS: her version is restored, because in neither
case had anyone decided anything.

| # | Where | What had been done | Now |
|---|---|---|---|
| R1 | `p9-03` key note | Paraphrased — *"A charged object fills the space around it with an electric field, and anything charged that arrives…"*. Good physics, not hers, and no row claimed it. | Hers, verbatim: *"An electric field is what a charged object does to the space around it: at every point there is a size and a direction…"* (P6 R2 precedent: every key note is hers) |
| R2 | `p9-02` rung 3, criterion 4 | A straight apostrophe where hers is typographic (*balloon’s*, *wall’s*) | Hers |

Everything else the comparator returned is accounted for above: rows 3 and 4
(the finished distractors), her aria descriptions of her own SVGs, the
safeguard eyebrow no P9 page has, and her `showDraft` chrome.

## ⚠️ Two collisions caught only at integration, 25 Aug 2026

P8 and P9 were built in parallel worktrees and each passed every gate alone.
Merged into one lane, `ks3_art.load()` refused the build: P8's `circ-band`
and P9's `charge-band` had both registered the shell class `ks3-cband-block`
(MRB-279's assertion, doing exactly what it was written for). Then the
liveness gate refused the push: P8's `circ-think` and P9's `charge-think`
both emitted the marker attribute `data-cthink`, which the registry does
not check — the liveness gate found P8's page carrying P9's marker. P9's
stems are now `chband` and `chthink`, renamed inside `ks3_art/p9.py` and
P9's own BEGIN/END blocks in `shared/ks3.js` and `shared/ks3.css` and
nowhere else. Nothing a student sees changed. ⚑ The registry could usefully
assert marker-attribute uniqueness as it asserts class uniqueness; the two
are the same defect by a different route.
