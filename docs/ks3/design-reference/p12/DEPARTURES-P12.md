# DEPARTURES-P12 — every difference between Claude Design's delivered P12 pages and the built ones

Written 25 Aug 2026 by the MRB-223 P12 executor, against
`docs/ks3/design-reference/p12/` as delivered on 23 Aug 2026.

**Every difference from her page is either a row here or a revert. There is no
third category.** The rows below are the complete list; anything not here is
her drawing, ported.

Her structure is untouched throughout: her sections, in her order, with her
ids, her four rail stops per page, her two Think-again quotes per page, her one
key-fact block, her key note, her *Going further*, her *Connects to* and her
legal line. Every one of her explainers, reveals, quotes, corrections and
success criteria is lifted verbatim from the delivered HTML.

---

## 1. Changed

| # | Where | What Design drew | What is built | Why |
|---|---|---|---|---|
| 1 | `p12-05` bench · the season verdict | `warm = h > 13 \|\| a > 60`, giving three verdicts: *"That is summer."*, *"That is winter."*, *"That is a season in between."* | Four verdicts. The fourth is selected when the SWING in daylight between the two solstices at that latitude is under one hour, and reads *"That is neither summer nor winter: this close to the equator the day barely changes length all year and the Sun is always high, so there is no seasonal swing to name."* | Her rule prints **"That is summer."** at the equator on **all four of her dates**, because the noon Sun there clears 60° in March, June, September and December alike. That contradicts her own explainer three paragraphs above the bench — *"places on the equator … barely have seasons at all"* — and it is four of her twelve reachable states. The swing is the quantity that actually decides it and it is computed from her own model: 0.0 h at the equator, 4.5 at Sydney, 9.0 at London. 5A.1: a comparative label over per-state values is COMPUTED, and every reachable state has something true to say. Driven: all twelve states now read true. |
| 2 | `p12-02` bench · the closing tail of the note | A ternary with two named cases and a fallback. The fallback reads *"Take it to Jupiter and the weight nearly two-and-a-half times over; take it to the Moon and it drops to about a sixth."* | Three branches keyed on the ratio of the local field strength to Earth's — `same`, `less`, `more` — each a complete sentence with the ratio printed: *"Here the weight is 0.16 times its Earth value, and the object is not one atom smaller."* | Her fallback **has no verb**, and it is the branch shown on Earth AND on Mars — half her slider positions. It is also a comparative authored beside the values rather than derived from them, which is the 5A.1 rule this unit is bound by. Deriving it makes it true in all four positions by construction and would survive a fifth. The EDITOR-CUT LAW: the seam is re-authored to land as a sentence, not patched. |
| 3 | `p12-03` bench · the bar sub-lines | `'a ' + (n * n) + 'th of full strength'`, rendering **"a 4th"**, **"a 9th"**, **"a 16th"** | `a quarter` / `a ninth` / `a sixteenth`, authored on the slider positions | Her own `aria-label` for the same three bars already says *"a quarter, a ninth and a sixteenth"*, so the page contradicts itself and the drawn version is the wrong half. |
| 4 | `p12-03` bench · the note at any moved separation | `'it does not fall to a ' + V + 'th of its value; it falls to a ' + (V*V) + 'th'`, rendering **"it does not fall to a 2th of its value; it falls to a 4th"** | `it does not fall to a half of its value; it falls to a quarter`, from authored words on the slider positions | "a 2th" and "a 3th" are not English. Same defect as row 3, in the sentence rather than the label. |
| 5 | `p12-03` bench · the third readout's sub-line at the resting position | `'divided by ' + (V * V)`, rendering **"divided by 1"** on load | `not divided at all` at the real separation; her template elsewhere | The resting state is the first thing every student meets, and this is a bench about division. Her own bar list already has a word for the undivided case (*"full strength"*), so this is her treatment applied one tile over rather than a new idea. |
| 6 | `p12-04` bench · `fmtKm` under a million kilometres | `(km / 1e6).toFixed(2) + ' million km across'`, rendering Proxima Centauri as **"0.21 million km across"** | `210,000 km across` | 210 000 km is a number a Year 9 can hold; "0.21 million" is the same number made unreadable. Her VALUE is untouched. |
| 7 | `p12-04` bench · `fmtKm` above a million million kilometres | `(km / 9.461e12).toFixed(0) + ' ly across'`, rendering the Milky Way as **"100411 ly across"** and Andromeda as **"211394 ly across"** | `about 100,000 ly across` / `about 210,000 ly across` — two significant figures, grouped, hedged | Eight significant figures on a galaxy width known to about ten per cent. Her own legal line on the same page says *"the Milky Way about 100 000 light years across"*, so the drawn figure contradicts her own stated precision. |
| 8 | `p12-04` bench · the solar-system tab's note | *"Measured out to Neptune. Sunlight takes about four hours to cross it."* | *"Measured out well beyond Neptune, whose orbit alone is 9000 million km across. Light crosses the whole of this in hours rather than years."* | Her note and her own readout disagree: the tab's `ly` value is `0.00126`, which the distance readout renders as **11.0 light hours** — about 80 astronomical units, well beyond Neptune, whose light time from the Sun is 4.2 hours. 5A.1 settles which side moves: *the instrument is the measurement and the prose is what changes.* Her `ly` and her `dia` are both untouched, and the new sentence is true of both. |
| 9 | `p12-06` bench · `fmtD` in the million-kilometre branch | `(m / 1e12).toFixed(2) + ' million km'` — metres divided by 10^12, a **thousand times** too many. Neptune's bar reads **"4.50 million km"** | `4,500 million km` | 4.5 × 10^12 m is four and a half thousand million kilometres. Her own `p12-04` legal line says so in as many words: *"Neptune's orbit about 4.5 billion km from the Sun."* The arithmetic is simply wrong and the page carries the contradiction on its face. |
| 10 | `p12-06` bench · `fmtD` above a million light years | `(m / 9.461e15).toFixed(2) + ' light years'`, rendering Andromeda as **"2501458.99 light years"** | `2.50 million light years` | Eight significant figures and no grouping, on the one figure the lesson's closing argument rests on. |
| 11 | `p12-06` CFIFA · the question head at exponent zero | `T.t.toExponential(2).replace('e+', ' × 10^')`, rendering the Moon — the bench's OPENING tab — as **"1.28 × 10^0 s"** | `1.28` | A power of ten that is not doing anything, in the first sentence of the attempt panel, on the resting state. Every other exponent is untouched. |
| 12 | Every bench · the `aria-label` on the bar panel | An authored sentence naming some of the bars. `p12-01`'s names **four of the five she draws** — the one it omits is deep space at 0.0 N/kg | A template with a `{list}` token, composed at render time from the bars themselves | 5A.4: *a `<desc>` walks the drawing … and it describes what is ACTUALLY DRAWN.* Deep space is the state the whole second half of `p12-01` turns on, and it was the one missing from the label. Derived rather than typed, so a sixth bar cannot arrive without appearing in it. `r_space_bench` refuses a `bars_alt` without `{list}`. |
| 13 | Every bench · the selected bar | `tone: 'var(--ks3-alert)'` — amber fill on the current bar, the other bars `--ks3-blue-light` | Every bar keeps the `--ks3-data` fill; the current bar's TRACK takes a 2px `--ks3-accent` ring and its label goes to 700 | 5A.2 and `shared/tokens.css`: **amber warns — a wrong IDEA being confronted — and never merely labels; category and selection go to `--ks3-data`.** The obvious substitution is impossible here: `--ks3-data` and `--ks3-blue-light` are THE SAME VALUE (`#8FB7FF`, deliberately), so swapping the fill would make the selected bar identical to the four beside it. Accent as a BORDER is not accent text and clears the token's size rule; the readout cards name the current selection in words on every page, so colour is never the only signal. |
| 14 | `p12-02` explainer 2, last clause | *"…so it changes with where the object is, and it disappears entirely nowhere in particular but falls to almost nothing far from any large body."* | *"…so it changes with where the object is, and it never disappears entirely anywhere — but far from any large body it falls to almost nothing."* | Her clause is ambiguous on first reading in exactly the direction the unit fights: *"it disappears entirely nowhere in particular"* parses as *it disappears* before it parses as *it never disappears*. The claim is unchanged; the order of the words is what moved. |
| 15 | `p12-03` explainer 1, last sentence | *"Every pair of objects in the universe is pulling on every other pair, including you and this page."* | *"Every object in the universe is pulling on every other object, including you and this page."* | A pair does not pull on another pair; an object pulls on an object. Her own next paragraph gets it right (*"The Sun pulls the Earth and the Earth pulls the Sun"*), so this is a slip rather than an intention. |
| 16 | All six pages · the draft flag | `<p class="ks3-review-flag">Draft — not yet science-reviewed.</p>` under every `<h1>`, behind her `showDraft` prop | Absent | Engine policy, not a judgement about the content: MRB-221 revoked the review marker for the whole key stage on 16 Aug 2026 and `verify_ks3.py` asserts its ABSENCE. Named here rather than left silent because it is a visible difference from her page. |
| 18 | `p12-01` CFIFA · question 1's Insert note | `'The field strength is the one for ' + T.name + ', not for Earth.'`, rendering **"The field strength is the one for Earth, not for Earth."** on the opening tab | *"The field strength is the one for {name} — the place you are standing, never a default."* | Her clause is right on four of her five places and nonsense on the fifth, and the fifth is the one the bench OPENS on — so it is the first sentence of the attempt panel that every student reads. One clause, true in all five. Nothing is lost from the page: question 2's own notes still carry the explicit *"Use the Martian field strength, not the Earth one"*, and the bench's fourth readout tile makes the Earth comparison live a few centimetres above. Found by driving the page and reading the screenshot, which is the only way this shape is ever found. |
| 19 | `p12-01` CFIFA · question 1's closing line | `'The five lines give ' + W + ' N on ' + T.name + '. The same ' + V + ' kg on Earth would weigh ' + earthW + ' N.'`, rendering **"The five lines give 500 N on Earth. The same 50 kg on Earth would weigh 500 N."** on the opening tab | *"The five lines give {w} N on {name}, for a mass of {v} kg that is the same everywhere."* | Same defect as row 18, in the same panel, in the same resting state: her sentence says the identical thing twice. The replacement makes the unit's own point instead, and is true in every state. |
| 17 | All six pages · rung 2, and `p12-05` rung 1 | Six length tells. Her correct option states a RULE and each distractor states a short wrong REASON — 30 words against 15 on `p12-01`, 23 against 16 on `p12-02`, 24 against 13 on `p12-03`, 28 against 14 on `p12-04`, 34 against 11 and 25 against 12 on `p12-05`, 36 against 12 on `p12-06` | Every distractor on those seven rungs is FINISHED so that it states a complete wrong RULE, in the same three-part shape as the correct answer | MRB-177's ruling, in the construct its own note predicts: *"if a new tell appears, it is almost certainly this construct again and NOT a one-off. Rewrite the distractors as wrong rules."* **No correct answer was shortened, no index was moved for this, and no correction was edited.** Eleven bank questions carried the same construct and were remedied the same way. Measured after: zero tells across every ladder rung, every hook, every bench gate, every predict and all 72 bank questions. |

---

## 2. Considered, and not changed

| Where | What was considered | Why it stands |
|---|---|---|
| `p12-03`'s forces in `10^20` notation | Her NOTES §6 asks whether standard form is too early for KS3, or whether words would do | **Ruled: stands as drawn.** The figures are READOUTS the bench computes, not arithmetic asked of a student; rung 2 asks about EQUALITY rather than a calculation; and standard form is on the KS3 maths curriculum. Powers are typed `10^20` throughout, which is her own §5 convention — U+2070 and U+2074–U+2079 are absent from every shipped font subset and fall back to a system face mid-number. |
| `p12-04`'s star counts | Her NOTES §6 asks whether to quote figures at all rather than an order of magnitude | **Ruled: they stand.** "About 200 billion", "about a trillion" and "around two trillion galaxies" are already hedged in her own words and her legal line records that galaxy star counts are estimates with wide error bars. An order of magnitude with no number attached is harder for a student to hold, not easier. |
| `p12-05`'s astronomical model | Whether the sunrise equation, `90 − \|lat − dec\|` and `sin(altitude)` are more than a KS3 bench needs | **Ruled: the model stands with its legal line.** It is real astronomy and it comes out right — London on 21 June gives 16.5 h and 61°, both asserted in the unit's own content-truth drive. Her legal line names what it leaves out (refraction, the Sun's disc, absorption and scattering). |
| `g = 10 N/kg` | Whether to use 9.81 | **Statutory.** `KS3.P.SPACE.01` names 10 N/kg and it is the figure used throughout. Every relevant legal line records that Earth's true mean value is 9.81 and that it varies by about 0.5% pole to equator. |
| A Childline / safeguarding block | Whether any P12 page warrants one | **No.** Nothing in the unit asks a student to disclose anything about themselves. Her delivery carries none and none is added — the block means something where it is used. |
| The KEY FACT's position on `p12-01`, `p12-02` and `p12-06` | On her pages it sits INSIDE `#s-formula`, after the CFIFA block. The engine renders `key-fact` as its own block | **Stands as the engine renders it.** It is the same block in the same reading position, immediately after the attempt panel and before `#s-think`; the section boundary is the only thing that differs, and it is not visible. Identical to P7's treatment of the same shape. |
| `p12-03`'s third readout duplicating the second at the resting position | Both tiles read `1.98 × 10^20 N` on load | **Hers, and it is the point.** The two tiles coincide only at the real separation and come apart the instant the slider moves, which is the comparison the bench is built to make. Only the sub-line was touched (row 5). |
| The `.ks3-blockhead` progress readout wrapping below the heading at narrow widths | Design's `Bench` keeps it on the heading's row | **Stands.** It is `r_activity`'s shell, shared with P7, P8 and P9, and it holds her layout — eyebrow and heading left, readout right — at every width where the row fits. The unit draws no head row of its own, deliberately: P4, P5 and P6 each define one and ship every bench heading twice on live pages. |
| `p12-04`'s solar-system tab having a "distance from Earth" at all | You are standing inside it | **Hers.** The rung is a scale on a ladder and the readout label is her own; row 8 fixes the one sentence that disagreed with the number. |

---

## 3. Notes versus drawing — where her own documents disagree with her own pages

| What her note says | What her page measures | Which was built |
|---|---|---|
| `NOTES-P11-P12.md` §3: *"p12-03 \| four gravitational pairs × four separations \| inverse-square fall-off"* | Correct, and her bar SUB-LINES and her NOTE render the fractions as "a 4th" and "a 2th" while her `aria-label` for the same bars says "a quarter, a ninth and a sixteenth" | The `aria-label`'s wording, in all three places. Rows 3 and 4. |
| `NOTES-P11-P12.md` §6: *"p12-03 gives gravitational forces in scientific notation (1.98 × 10^20 N). Confirm that is not too early for KS3, or ask for words instead."* | The page gives them as readouts and asks no arithmetic of them | The page. Ruled; see §2. |
| `p12-04`'s solar-system note: *"Measured out to Neptune. Sunlight takes about four hours to cross it."* | The same tab's `ly` renders as 11.0 light hours — about 80 AU, and her `dia` of 9 × 10^9 km is Neptune's orbit DIAMETER | The readouts, with the note rewritten to agree (row 8). |
| `p12-04`'s legal line: *"the Milky Way about 100 000 light years across"* | Her `fmtKm` prints `100411 ly across` for the same galaxy | The legal line's precision (row 7). |
| `p12-06`'s bar for Neptune: `4.50 million km` | Her `p12-04` legal line: *"Neptune's orbit about 4.5 billion km from the Sun"* | The legal line. The formatter's divisor was wrong by 10^3 (row 9). |
| `p12-05`'s explainer: *"places on the equator … barely have seasons at all"* | Her bench prints *"That is summer."* at the equator on all four dates | The explainer (row 1). |
| `README.txt`: *"Draft — not yet science-reviewed. Every page says so on its face until that flag is cleared."* | Every page carries `showDraft` | Neither, and not a judgement about her content: MRB-221 removed the review marker key-stage-wide and `verify_ks3.py` asserts its absence (row 16). |

---

## 4. Engine policy — recorded here, not a register row

**MRB-278 · answer positions are AUTHORED.** All twelve of Design's marked
rungs put the correct answer at index 0. Her option TEXT and every correction
are verbatim; only the ORDER moves, and `answer` follows it. Across the unit:

    p12-01  1, 3      p12-03  3, 1      p12-05  1, 3
    p12-02  2, 0      p12-04  0, 2      p12-06  2, 0

Three uses of each of the four indices. The 72 bank questions are authored
across all four indices independently (17 / 19 / 22 / 14). Index 0 is USED
rather than avoided: a student who learns that the first option is never right
has learned a tell of the opposite sign.

**Her `showDraft` chrome is not ported**, on any page, in any form. Swept by
concept — "draft", "review", "not yet checked", "provisional" — across the six
built pages: zero occurrences.

**No `→`, `✓` or `✕` characters** appear in any payload. Her end-matter arrows
are already inline SVG and stay that way.

**Powers of ten are typed `10^n`** throughout, her own §5 convention, and unit
symbols keep their Latin-1 superscripts. Nothing in this unit needed a `<sub>`.

**Her `aria-label` texts are corrected where the port corrects the drawing**
(row 12), on 5A.4's rule that a description of a figure describes what is
actually drawn.

**Design's `Cfifa.dc.html` in this delivery is byte-identical to the one in
`docs/ks3/design-reference/p7/`** — checked, not assumed — so the attempt panel
is `ks3_art.kit.r_cfifa_attempt` with P12's own family and namespace, and
nothing in the shared kit moved. Her `blockedProgress` string has no slot in
that helper and travels as a span of this unit's own rather than as an edit to
a file five units share.

**One behaviour is repaired rather than reproduced** (R4's rule): P4's attempt
panel disables the Check button when question 1 blocks and never re-enables it,
so a student who visits deep space and comes back finds the button dead until
they happen to touch a field. `paintAttemptP12` repaints it from what is
actually written. Driven both ways.

---

## 5. Unresolved

Nothing. Every flag in `NOTES-P11-P12.md` §6 that touches P12 is ruled above,
every contradiction between her notes and her pages is listed in §3, and every
difference between her drawing and the built pages is a row in §1.

One thing is NOTED and deliberately NOT raised as new: three P12 pages put
`#s-think` on the rail, which parallels the open flag P9 recorded for `p9-01`
(*Think-again as a rail stop*). The predicate differs — hers here is satisfied
by the hook or by ladder rung 1 rather than by the bench's gate — so the
section takes a wire function of its own instead of being marked by the bench.
Recorded in `docs/ks3/misconception-register.md` under `SPACE`; the flag itself
stays where P9 left it.
