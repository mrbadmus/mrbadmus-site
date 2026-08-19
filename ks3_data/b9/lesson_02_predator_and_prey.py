"""B9 L2 — Predator and prey (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b9/b9-02-predator-and-prey.dc.html` (547 lines), her author's notes
`docs/ks3/design-reference/b9/NOTES-B9.md`, and the B9 payload schema
`docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md` §0, §1, §2, §3, §4, §6, §11, §12, §13
and §14, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted", each of which is
either a slot code a student cannot resolve or an MRB-177 distractor repair.
The rail strings, the four cycle cards, both marked rungs, both self-marked
rungs and all six bench notes came out of the page's own `RAIL`, `RAIL_SHORT`,
`CYCLE_CARDS`, `RUNGS`, `SELF_RUNGS` and `renderVals()`, not off a keyboard.

── This lesson is a MODEL, and the model is the argument ────────────────

`#s-bench` is `cycle-runner`, on `ks3-block ks3-dark ks3-practical` (page line
105), so `practical` is MEASURED from Design's own markup rather than inferred
from the kind name — payload schema §0 rule 2, and contract §4 records that B1
got two of six wrong by inferring it.

Two difference equations and nothing else:

    nextPrey = prey + R·prey·(1 − prey/K) − A·prey·pred
    nextPred = pred + B·A·prey·pred − M·pred

R 0.6, K 2000, A 0.0015, B 0.35, M 0.35, opening at 800 rabbits and 120 foxes,
twenty-six years of history. Nothing in those two lines says "cycle" and nothing
says "lag"; both fall out, and that is the whole reason the lesson is built on
an instrument rather than on a graph a student is told to read.

⚖️ **K = 2000 IS THE GRASS SUPPLY AND IT IS NOT A TUNING CONSTANT.** It is the
only reason *Remove every fox* teaches a carrying-capacity result — the rabbits
climb, then stop, crowded and hungry — instead of drawing an exponential curve
that would teach the misconception `#s-think` exists to break. Design says so in
a comment on her own page (lines 304–306) and `r_cycle_runner` refuses a model
whose prey cannot reach the ceiling. Measured in a browser: after a cull the
rabbits settle at 2,000 and stay there. `ECO-04` is confronted by that number.

⚖️ **THE TWO SERIES ARE SCALED INDEPENDENTLY**, `maxPrey = max(600, …)` against
`maxPred = max(150, …)`, and `chart_caption` says so in words. On one scale the
fox series flattens into the axis and the LAG — which is the entire lesson, and
the thing rung 1 and rung 2 both test — becomes unreadable. Merging them is not
a tidy-up, it is deleting the content. Do not "fix" it.

⚠️ *Remove every fox* IS NOT A RESET. It toggles the predator count between zero
and its starting value, pushes ONE history point and advances the year by one,
so the intervention is recorded on the chart as a year like any other and the
student watches the rabbits respond to it over the years that follow.

── ⊖ `notes[].when` IS NOT AUTHORED, and the `id` carries the branch ────

Payload schema §6 sketches each note branch as `{id, when, text}`. `when` is a
predicate held as a string, and a predicate held as a string needs an evaluator
— shipping one would be an eval, and a key whose only reader is a comment is
precisely the dead key contract R5 forbids. The engine pass therefore dropped it
and implemented the six predicates once, in `wireCycleRunner`, keyed by `id`.

So **the six ids are a closed, ORDERED set and the order is asserted** by
`r_cycle_runner`. First match wins, and `no_pred_at_ceiling` must be tested
before `no_pred` or the ceiling note never fires and *Remove every fox* stops
teaching carrying capacity. The six below are in Design's own evaluation order
(page lines 425–431). Recorded as a schema deviation in the report.

⛔ **NO RUNTIME STATE IS AUTHORED** (payload schema §0 rule 3): no `year`, no
`culled`, no `history`. ⚑ `culled` is dead in DESIGN'S OWN CODE — `onCull` sets
it, `onReset` clears it, `renderVals()` never reads it — and is not carried
across.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ─────────────────

Design draws four (page lines 296–302) and her `isDone()` gives `s-cycle` the
BENCH's predicate, character for character, one section to the left:

    if (id === 's-bench') return s.year >= 10;
    if (id === 's-cycle') return s.year >= 10;      // page line 366

`#s-cycle` is an eyebrow, a display statement, four static cards and a key
fact: no control, no commitment, no field, no reveal. MRB-205 binds and is not
re-argued — Design draws, we render, and dropping a stop Design drew is not
rendering what Design drew. The second line above is not an alias; it is Design,
in a rail-level function, saying what completes the stop. The band is the PAYOFF
of the instrument beside it and carries no control precisely because the
instrument already took the student's commitment.

So the third stop is declared with `mirrors: "s-bench"`, `wireRail`'s `paint()`
resolves it at rail level, and `ks3_parity.check_rail_matches_design` gates the
built rail against `docs/ks3/rail-manifest.md` row 99 —
`s-hook s-bench s-cycle s-ladder`, `s-cycle=s-bench`. A three-stop rail fails
the build.

⚠️ Payload schema §4 pre-ruled THREE stops for all six B9 pages and its own
header now records that verdict as reversed. Read §4's count as historical; its
MEASUREMENT of what Design drew is correct and is what is built.

── What could not be lifted byte-identical, and why ─────────────────────

**1. `b9-03` in rung 1's third correction — a slot code (§8.10).** Design
writes *"In a real web there are other routes, which is b9-03's subject, but the
population still tracks its main prey."* A student cannot resolve a slot code,
and printing one is exactly the platform leakage §8.10 exists to stop. Resolved
to the lesson TITLE, which is how b8-01 and b7-04 resolved the identical shape:

    Design:  which is b9-03’s subject
    Built:   which is the subject of Disturbing a food web

The destination is not lost — `disturbing-a-food-web` is carried as a real
`references` edge, which is Design's own *Connects to* card anyway.

**2. `the next lesson` in `#s-think`'s second body — a positional reference
behind a stripped link.** Design writes *"it is the beginning of
`<a href="b9-03-…">the next lesson</a>`, where the consequences spread
outwards"*. `rich()` allows `<em>` and `<strong>` and nothing else, so no
hyperlink survives anywhere on the page. That costs nothing where the link TEXT
is already a lesson title; here the text is a POSITION, so dropping the tag
would leave a student reading "the beginning of the next lesson" with nothing to
follow and an ordering claim a school's own scheme may not honour:

    Design:  the beginning of <a …>the next lesson</a>, where the consequences
    Built:   the beginning of Disturbing a food web, where the consequences

Same edge, already carried. Nothing quantitative and no science word moves.

**3. Rung 1's three distractors — MRB-177, and they are the reason the rung
had to be repaired rather than lifted.** Worked below.

── ⊕ MRB-177 LENGTH PARITY — MEASURED. RUNG 1 REPAIRED, RUNG 2 CLEAN ────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags a
correct option that is strictly the longest AND clears the longest distractor by
≥4 words or by ≥1.4×.

**Rung 1 as Design drew it FAILS the gate**, and it is the textbook instance of
the construct MRB-177 was ruled against: the correct answer states a RULE
(subject · condition · consequence — *the fox population* · *there is not enough
prey* · *falls*) while all three distractors state a short wrong REASON in one
clause.

    correct  14w  "Fall, because there is not enough prey to support the
                   current number of foxes"
    A        8w   "Keep rising, because foxes are still eating rabbits"
    B        9w   "Stay the same, since foxes eat other things too"
    C        10w  "Rise, then fall, then rise again within the same year"

    strictly longest, gap 4 → TELL. A student who has read nothing can pick it.

The ruling fixes the CONSTRUCT and not the threshold, so **the correct option is
untouched** and each distractor is rebuilt to state a WRONG RULE in the same
three-part shape, with the misconception as the consequence. Each keeps the
belief Design chose, because Design's correction for it is what marks it and
every correction is unchanged:

    A  belief: predator numbers track prey numbers with no delay
       Design:  Keep rising, because foxes are still eating rabbits            8w
       Built:   Keep rising, because foxes go on breeding while there are
                still rabbits to catch                                        14w
       Design's correction — "They rise for a while after the rabbits turn —
       that is the lag — but they cannot keep rising once the food runs
       short." — answers the rebuilt option exactly as it answered the first.

    B  belief: an alternative food source decouples the two populations
       Design:  Stay the same, since foxes eat other things too                 9w
       Built:   Stay the same, since foxes eat other prey when rabbits
                become scarce                                                  12w

    C  belief: a population responds to its conditions immediately
       Design:  Rise, then fall, then rise again within the same year          10w
       Built:   Rise, then fall, then rise again within the same year,
                because numbers respond at once                                15w
       Design's clause survives whole; the `because` clause is the wrong rule
       the correction ("A cycle takes several years, because it is limited by
       how fast animals can breed.") was already written to break.

    repaired: correct 14w against 14 / 12 / 15 — not strictly longest  ✓ clean

⚖️ **No belief is from the register**, and that is measured rather than
assumed: this lesson's two register entries are `ECO-03` (the two peaks
coincide) and `ECO-04` (remove the predators and the prey do brilliantly), and
neither is what rung 1 tests — rung 1 tests the DIRECTION the fox population
moves two years into a prey decline. The three beliefs above are written here,
from Design's own distractors, and are reported as authored rather than lifted.

**Rung 2 is clean and nothing on it is touched.** Correct 8w against 10 / 8 / 5
— not strictly longest, because Design built it correctly: all four options
state a RELATIONSHIP between two peaks, so the student cannot pick by shape.

⚖️ **Rung 2's fourth option is five words long and is still not a length tell.**
"There is no consistent pattern" is short because the belief is short — it is
the shrug a student reaches for when a noisy graph defeats them — and padding it
into a rule would make it sound more considered than their own version of it.
The gate measures the correct option against the LONGEST distractor (10w), not
the shortest, and it passes with room. Recorded so a later pass does not "fix" a
clean rung. Same argument, and the same answer, as b8-01's three-word option D.

Every option ORDER, every `answer` index, all six corrections, both self-rung
questions and all ten criteria are Design's, byte-identical.

── ⚖️ THE CANONICAL STORY — `Going further`, and it is not "lynx control hares" ─

NOTES-B9 flag 6 was RESOLVED on 16 Aug and payload schema §13 VERIFIED the
ruling present in the delivered bytes. The paragraph below is lifted whole and
must stay whole. Three things in it are load-bearing and a later pass must not
simplify any of them into a one-cause story:

  1. **The linked cycle is what the data show**, and it is stated positively —
     two wavy lines, roughly ten years, the lynx peak trailing the hare peak.
  2. **Lynx move WITHIN the cycle as much as they drive it.** Hare numbers rise
     and fall for reasons reaching well past lynx: the shoots and twigs are
     stripped after a peak and take years to grow back, and hares under heavy
     pressure raise fewer young. The single-cause reading is refused out loud.
  3. **The ledgers count PELTS BROUGHT IN BY TRAPPERS, not hares alive in the
     forest**, so fur prices and trapper numbers are in the line too. That is
     evidence handling, not a hedge on the model, and it closes on *"A ten-year
     rhythm that survives all of that is a real rhythm. It is still not a
     census."*

⚑ For Mide's science gate — every NOTES-B9 flag landing on THIS lesson, and what
  was checked against it. Two flags, two checked, **neither corrected**:

  * flag 5   **The model's parameters, and damped rather than neutral.**
             CHECKED AND LEFT. The parameters are invented for teaching and the
             page's own legal line says so in its first clause. The choice of a
             damped model over a neutral Lotka–Volterra one is Design's and is
             the right one at KS3: a neutral model cycles for ever at whatever
             amplitude it started with, which looks like perpetual motion and
             is also structurally unstable — any change to the model at all
             destroys the cycle. The damped logistic version carries a real
             carrying capacity, which is what `#s-think`'s second belief and
             rung 4 both need, and it converges to a coexistence point rather
             than to extinction. What a student sees in the first twenty-six
             years is a decaying oscillation with the predator peak trailing,
             which is the claim the lesson makes. ⚑ The one consequence worth
             Mide's eye: run far enough and the cycle damps out to two steady
             numbers, and a student who presses *Ten years* four times will see
             that. ⊕ RULED, MRB-255 S5 (19 Aug 2026): the maths stays and the
             copy shrinks. `steady` and the legal line did NOT cover it — they
             describe a swing, and by then there is none — so a `settled`
             branch was added, and every string promising a cycle that
             continues undiminished ("a repeating cycle", "goes round again")
             was re-authored. The legal line's "cycle less tidily, and
             sometimes do not cycle at all" is load-bearing and stays.

  * flag 6   **Hudson's Bay lynx and hare.** CHECKED AND LEFT — already
             resolved 16 Aug and verified in the bytes; see the ⚖️ block above.
             Both halves are correct as written: the Hudson's Bay Company's fur
             records do run for around two centuries, the recovered cycle is
             about ten years, and the lynx peak does trail the hare peak.
             The refusal of the single-cause reading and the catch-not-census
             point are the two sentences that make this a *how do we know*
             story rather than a graph with a caption. Neither may be trimmed.

  * §15     **No figures, and it is MEASURED.** `<img>`, `<figure>` and
             `<picture>` each appear ZERO times on this page — grepped, not
             assumed — and every `<svg>` is the nav chevron or a `ks3-mark`
             glyph. §4.10 allows an empty `figures` for a lesson carried by its
             interactives. NOTES-B9 flag 17's diagram request is not dropped by
             this; it names b9-01 and b9-03 and is Mide's to rule on.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes six times — *the predator peak comes after the
prey peak, because breeding takes time*. The hook reveal, the `steady` bench
note, cycle card 2, `#s-think`'s first body, the key fact, the key note and rung
3's fifth criterion all state it at the same size. Nothing above is walked back
below. `Going further` adds the ledger evidence and the reasons hares cycle
beyond lynx, and retracts none of it: "a real rhythm" is a confirmation, and
"still not a census" is about the RECORD rather than about the model.

── Misconception ids: ECO-03 and ECO-04 ─────────────────────────────────

⚠️ **The `ECO` prefix row does not yet exist in
`docs/ks3/misconception-register.md`** — grepped: no `ECO-*` row is open, and
the only `ECO` string in the file is the permanent reservation *"`ECO-12` — is
`NOS-04`"*. NOTES-B9 §4 asserts twelve entries were "written into the register
with a new prefix row"; they were not — the identical claim NOTES-B5, NOTES-B7
and NOTES-B8 each made about `REPRO`, `PLANT` and `RESP`, fourth occurrence.
**That file is not this pass's to edit** (contract §0), so the two statements
below are authored here in register voice, byte-identical to Design's own quoted
beliefs (page lines 167 and 171, minus the typographic quotation marks the
engine draws itself), and are reported for whoever opens the row.

No gate resolves an id against the register file — `verify_ks3.py`,
`ks3_parity.py` and `build_ks3.py` do not read it — so the lesson builds either
way; what is at risk is the register's completeness, not this page.

Both values resolve against the BUILT page (MRB-244/MRB-248), which is the whole
universe of `id="…"` and `data-activity="…"` a browser can reach:

    confronted_by  `s-think`   — the confrontation block's emitted anchor, and
                                 the section that takes both beliefs apart.
    elicited_by    `s-ladder`  — the ladder's emitted anchor. Both beliefs are
                                 offered there as something to commit to:
                                 rung 2's FIRST option is `ECO-03` word for
                                 word, and rung 4 asks the student to predict
                                 in their own writing what happens to the
                                 rabbits when every fox is removed, which is
                                 `ECO-04` stated by whoever holds it. Neither
                                 is elicited earlier — the hook asks a
                                 different question and `#s-bench` shows the
                                 answer rather than asking for one.

── Keys this pass authors, and where each is READ (contract R5) ─────────

R5 says no key is authored without a read site in the same pass. The renderer
belongs to the engine pass, so the read sites are named rather than left to be
discovered. Every one is measured off Design's own `renderVals()` and against
`r_cycle_runner` / `wireCycleRunner`:

    progress.prefix   `_KIND_HEAD_FROM["cycle-runner"]` → head counter
                      `{"format": "year {n}", "start": 0}`; runtime `setCount()`
    model.*           all ten in `advance()`'s recurrence or a clamp on it —
                      `r_cycle_runner` raises on any one missing
    series.*.name     the two live readouts; `.colour_token` the bar fill
    chart_caption     the mono line under the chart, and the two colours it
                      reads out by name
    year/ten/reset    the three unconditional buttons
    cull_label        the cull button at rest; `restore_label` its other state,
                      swapped by `wireCycleRunner` on `data-cull-label` /
                      `data-restore-label`
    notes[].id/.text  `noteId()`'s six branches, in this order, first match wins

⚠️ **THIS INSTRUMENT IS ON INK.** `.ks3-dark p` is (0,1,1) and beats a bare
instrument class at (0,1,0). That is the engine pass's problem rather than this
module's, and it is recorded here because this payload feeds it; as of MRB-245
`ks3_parity.check_dark_text_specificity()` gates it.
"""

# ── the four cycle cards (page lines 308–313) ────────────────────────────
#
# Design draws the number in a 38px accent chip; `_rule_card()` reads `role` for
# the mono accent tag, which is the one slot that exists for it, so the STRING
# is byte-identical and the treatment is the shipped one (contract R3). The
# numbers are load-bearing rather than ornamental: card 4's body ends "Which
# returns you to step 1, some years later", and without the numerals that
# sentence points at nothing.
CYCLE_CARDS = [
    {"role": "1", "name": "Plenty of prey",
     "body": "Rabbits are numerous, so foxes are well fed. More cubs survive "
             "their first winter, and the fox population starts to climb."},
    {"role": "2", "name": "Predators rise",
     "body": "More foxes hunting means more rabbits eaten than are born. The "
             "rabbit population turns and begins to fall — while the fox "
             "population is still rising."},
    {"role": "3", "name": "Prey becomes scarce",
     "body": "Now there are many foxes and few rabbits. Foxes go hungry, fewer "
             "cubs survive, and the fox population falls in its turn."},
    {"role": "4", "name": "Predators rise no longer",
     "body": "With few foxes left, the surviving rabbits breed almost "
             "unchecked and the population recovers. Which returns you to step "
             "1, some years later."},
]

# ── the six bench notes (page lines 425–431) ─────────────────────────────
#
# ⚖️ ORDER IS THE MEANING. First match wins in `noteId()`, and
# `no_pred_at_ceiling` is tested BEFORE `no_pred` — reverse them and the ceiling
# note never fires, which turns *Remove every fox* from the lesson's proof of
# carrying capacity into a button that says "climbing fast" for ever.
# `r_cycle_runner` asserts this exact sequence and raises if it drifts.
#
# ⊖ No `when` key: the predicate lives in `wireCycleRunner`, keyed by `id`. See
# the docstring.
NOTES = [
    {"id": "year_zero",
     "text": "Nothing has happened yet. Look at the shape before you read "
             "anything else."},
    # ⚖️ `ECO-04`'s answer, and the reason K exists. The rabbits are at the
    # ceiling with nothing hunting them and the note refuses to call it
    # thriving.
    {"id": "no_pred_at_ceiling",
     "text": "No foxes, and the rabbits have stopped climbing anyway — they "
             "have hit the limit the grass sets. This is what a population at "
             "its ceiling looks like: not thriving, just full. Predators were "
             "never the only thing holding them back."},
    {"id": "no_pred",
     "text": "No foxes left. The rabbits are climbing fast, and they will keep "
             "climbing until the grass runs short — run another ten years to "
             "find the ceiling."},
    # ⊕ MRB-257 (5.11) / MRB-255 S5 — THE STATE THE MODEL ACTUALLY ARRIVES AT.
    # Four presses of "Ten years" takes the prey spread from 30.8–100% to
    # 99.9–100.0%: the oscillation has stopped, and every other note on this
    # list describes one. MRB-255 rules the maths stays and the copy shrinks,
    # so this is the note that makes the arrival legible instead of a chart
    # that has quietly gone flat under a sentence about peaks.
    {"id": "settled",
     "text": "The swings have stopped. Rabbits and foxes have arrived at a "
             "pair of numbers that hold each other in place — neither can "
             "grow, and neither dies out. Nothing is managing it; this is "
             "where the arithmetic comes to rest when nothing disturbs it."},
    {"id": "prey_high_pred_low",
     "text": "Rabbits high and foxes still low. This is the easy part of the "
             "cycle for the foxes, and their numbers will follow — next year, "
             "not this one."},
    {"id": "prey_low",
     "text": "Rabbits scarce. The foxes are now the ones in trouble, and their "
             "numbers will fall until the pressure comes off the rabbits."},
    # ⚖️ MRB-257 (5.12) — "a year or two" was measured and it is FIVE. On the
    # shipped model the prey peak sits at column 15 and the predator peak at
    # column 20, and the page's own GOING FURTHER already says "several years".
    # The "every time" is a claim about the ORDER of the peaks, which is true
    # at any amplitude, and MRB-255 S5 keeps it. What the closing clause adds
    # is the thing the chart is doing that no note admitted to.
    {"id": "steady",
     "text": "Both populations moving. Watch the chart rather than the "
             "numbers: the green bars peak about five years after the amber "
             "ones, every time. The swings are getting smaller as it goes."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 155 character for character.
    "slug":        "predator-and-prey",
    "title":       "Predator and prey",
    "discipline":  "biology",
    "unit":        "ecosystems-and-interdependence",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.ECO.01b` — "Interdependence between a predator and its prey: two
    # populations that each change the other" — owned whole. That clause was
    # minted for exactly this lesson (`ks3_data/substatements.py`, whose own
    # comment names the seam between (b) and (c) as the difference between two
    # populations changing each other and a species being taken OUT).
    #
    # ⚠️ NOTES-B9 §0 says b9-02 "carries no statement of its own". That predates
    # the four-way split of `KS3.B.ECO.01` and is superseded by it; reported.
    # ⚠️ The PARENT `KS3.B.ECO.01` must be owned by nobody — `build_ks3.validate`
    # fails on "PARENT AND CLAUSE BOTH OWNED". All four clauses are claimed one
    # each by b9-01 (a), this lesson (b), b9-03 (c) and b9-04 (d).
    "covers":      ["KS3.B.ECO.01b"],
    # Named, used, and owned elsewhere. ECO.01a is b9-01's — this page assumes a
    # student can read "fox eats rabbit" as a feeding relationship and never
    # re-teaches it. ECO.01c is b9-03's, and `#s-think`'s second belief hands
    # straight to it without doing its work.
    "touches":     ["KS3.B.ECO.01a", "KS3.B.ECO.01c"],
    "beyond_statutory": False,
    # One thread, and it is the unit's own. Nothing else fits: this lesson has
    # no cells in it, no substances and no forces — it is two numbers.
    "threads":     [{"id": "interdependence", "level": 2}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card (page line 265).
    "requires":    ["food-chains-and-food-webs"],
    "assumes":     [],
    # Design's "Connects to" card (page lines 271–272), in her order.
    # `disturbing-a-food-web` carries two stripped inline links as well —
    # rung 1's third correction and `#s-think`'s second body — and it is the
    # same edge, not a repeat. `testing-the-model` is C1 L6: this page IS a
    # model with a legal line about what it leaves out, which is that lesson's
    # whole subject.
    "references":  ["disturbing-a-food-web",
                    {"unit": "C1", "lesson": "testing-the-model"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Population dynamics, carrying capacity, and interpreting "
                   "real predator–prey data with its irregularities.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A fox eating rabbits is bad news for the rabbits. A fox "
                    "population eating a rabbit population is something "
                    "stranger: two numbers chasing each other round in a "
                    "circle, neither able to win.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them, and `short`/`label` are her own
    # `RAIL_SHORT` and `RAIL` strings (page lines 296–302). `s-cycle` is the
    # third: no control of its own, so it mirrors `s-bench` and ticks on the
    # bench's predicate — see the docstring, which also supersedes payload
    # schema §4's three-stop count. Gated against
    # `docs/ks3/rail-manifest.md` row 99: `s-cycle=s-bench`.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Still rabbits",
         "done_when": "committed"},
        # Design's own threshold, kept: `s.year >= 10` (page line 364). Ten
        # years is one full turn of the cycle, which is the shortest run that
        # can show a lag at all.
        {"anchor": "s-bench", "short": "BENCH", "label": "Run the years",
         "done_when": "ten_years_run"},
        {"anchor": "s-cycle", "short": "CYCLE", "label": "The cycle",
         "mirrors": "s-bench", "done_when": "ten_years_run"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key. C is the one the
    # reveal endorses, and the reveal says so at once; the hook is not a trick,
    # it is the claim the bench then has to earn in two equations.
    #
    # ⚖️ None of the four is `ECO-03` or `ECO-04` — measured, not assumed. The
    # hook asks WHY the prey survive, and both register beliefs are about what
    # the graph looks like and what happens when the predator is removed. That
    # is why `elicited_by` names `s-ladder` and not `s-hook`.
    "phenomenon": {
        "kind": "narrative",
        "title": "Foxes have eaten rabbits for thousands of years. There are "
                 "still rabbits.",
        "prompt": "Every predator is better at hunting than its prey is at "
                  "escaping, at least sometimes, or it would starve. Run that "
                  "forward for a few thousand generations and you might expect "
                  "the prey to be gone and the predator with it. Instead both "
                  "are still here.",
        "commit": "Why do predators not wipe out their prey?",
        "options": [
            "Predators only take the old and the sick",
            "Prey breed faster than predators can eat them",
            "When prey become scarce the predators starve, so their numbers "
            "fall too",
            "Predators deliberately leave enough prey to breed",
        ],
        "reveal": "Because the prey running out is the predator's problem "
                  "too. As rabbits become scarce the foxes go hungry, fewer "
                  "cubs survive, and the fox population falls — which takes "
                  "the pressure off the rabbits, who recover, and the "
                  "pattern repeats — each swing smaller than the last. "
                  "Nobody is managing this. It falls out of the arithmetic, "
                  "and the bench below runs it.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # The commander's pre-allocation (payload schema §14). Both statements are
    # Design's own quoted beliefs, byte-identical from page lines 167 and 171.
    #
    # ⚠️ The `ECO` prefix row is NOT yet open in
    # `docs/ks3/misconception-register.md` — see the docstring. That file is not
    # this pass's to edit; the statements below are what belongs in it.
    # ⛔ `ECO-12` must never be minted: the register permanently reserves it as
    # `NOS-04`. Nothing here touches it.
    "misconceptions": [
        # Elicited in the ladder: rung 2's FIRST option is this belief word for
        # word, and the student commits to it or declines to. Confronted in
        # `#s-think`, whose first body sends them back to the chart — the green
        # peak sits to the right of the amber one every single time.
        {"id": "ECO-03",
         "statement": "The two peaks happen at the same time — more rabbits, "
                      "more foxes.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        # Elicited in the ladder: rung 4 asks the student to predict, in their
        # own writing, what happens to the rabbits when every fox is removed,
        # and criterion 2 is what marks this belief. Confronted in `#s-think`,
        # whose second body sends them to the cull button — where K stops the
        # rabbits dead and the `no_pred_at_ceiling` note refuses to call it
        # thriving.
        {"id": "ECO-04",
         "statement": "Remove the predators and the prey will do brilliantly.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B9, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ "carrying capacity" is glossed here even though the page never uses the
    # phrase — it uses "ceiling" and "the limit the grass sets", which is the
    # right register for KS3 — because the idea is half of this lesson and the
    # words are what a student will meet next. `ks4_becomes` names it.
    "vocabulary": [
        {"term": "predator",
         "definition": "An animal that hunts and eats other animals.",
         "note": "Its numbers depend on how much prey there is to catch."},
        {"term": "prey",
         "definition": "An animal that is hunted and eaten by another animal.",
         "note": "The same animal can be prey to one species and a predator "
                 "to another."},
        {"term": "population",
         "definition": "All the individuals of one species living in the same "
                       "place.",
         "note": "This lesson is about numbers of animals, not about any one "
                 "animal."},
        {"term": "carrying capacity",
         "definition": "The largest population an environment can support, set "
                       "by food, water, space and disease.",
         "note": "The page calls it the ceiling. Reaching it is not the same "
                 "as thriving."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # zero times on this page — grepped — and every `<svg>` is the nav chevron
    # or a `ks3-mark` glyph. The chart is drawn by the instrument from the
    # model's own history, so there is nothing to source.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b9/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b9-inventory/PAYLOAD-SCHEMA.md §6. The
        # read sites the engine wires are listed in the docstring.
        {"type": "cycle-runner", "id": "run-the-years",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · one field, two populations",
         "heading": "Run the years and watch the lag",
         "prompt": "Two rules, and nothing else. Rabbits breed and are "
                   "eaten; foxes eat and die. Look at when each peak "
                   "happens — not how high, when.",
         # Design's mono line beside the heading (page line 111): "year 0" to
         # "year 26". One number, no denominator anywhere on the page.
         "progress": {"prefix": "year "},

         # ⚖️ K = 2000 IS THE GRASS SUPPLY. Dropping it, raising it out of
         # reach, or replacing the logistic term with plain growth deletes the
         # lesson — *Remove every fox* would draw the exponential curve that
         # `#s-think`'s second belief exists to break. `prey_cap_mult` and
         # `pred_floor` are the two clamps that stop a DISCRETE model
         # overshooting or oscillating negative; both are required, and
         # `pred_floor` is an extinction floor rather than a rounding artefact
         # — below one animal there is no breeding pair.
         "model": {"r": 0.6, "k": 2000, "a": 0.0015, "b": 0.35, "m": 0.35,
                   "start_prey": 800, "start_pred": 120, "history": 26,
                   "prey_cap_mult": 1.1, "pred_floor": 1},

         # ⚖️ SCALED INDEPENDENTLY, and `chart_caption` says so in words. On
         # one scale the fox series flattens into the axis and the lag — the
         # entire lesson — becomes unreadable. Do not merge them.
         "series": {"prey": {"name": "Rabbits",
                             "colour_token": "--ks3-alert"},
                    "pred": {"name": "Foxes",
                             "colour_token": "--ks3-ok"}},
         "chart_caption": "amber = rabbits · green = foxes · each pair is one "
                          "year, oldest on the left · the two are scaled "
                          "separately",

         "year_label": "One year",
         "ten_label": "Ten years",
         # The one button with two states. `wireCycleRunner` swaps them on the
         # rendered predator count, so the label always says what pressing it
         # will do next.
         "cull_label": "Remove every fox",
         "restore_label": "Let foxes back in",
         "reset_label": "Reset the field",

         "notes": NOTES},

        # #s-cycle — the band panel, and the mirror stop. Design draws it with
        # no class at all, on `--ks3-band` with a 3px ink border (page line
        # 142), which is the `rule` type: eyebrow, display statement, four
        # numbered cards, key fact nested.
        {"type": "rule", "anchor": "s-cycle",
         "eyebrow": "The cycle, in four steps",
         "statement": "It has no beginning, so start anywhere.",
         "cards": CYCLE_CARDS,
         # Design nests the key fact inside this section (page lines 156–159)
         # on the CARD ground with the 5px accent offset shadow. `card`,
         # because the section itself is `band` and band on band is invisible.
         # Never amber: measured — card + 2px ink outline + accent shadow.
         "key_fact": {"ref": "the-predator-peak-comes-second",
                      "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "ECO-03"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-cycle on the card ground — Design's own arrangement.
    # Lifted byte-identical from page line 158 and identical to payload schema
    # §12's b9-02 entry.
    "key_facts": [
        {"id": "the-predator-peak-comes-second",
         "text": "Predator and prey numbers rise and fall together, and the "
                 "predator peak always comes after the prey peak. Each "
                 "population limits the other, so neither wipes the other "
                 "out and neither grows without limit.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: `ks3-mis-head`, two quotes, two bodies, a border-top rule,
        # and no options, no reveal, no button, no state — payload schema §3),
        # so it is a `confrontation` and not a `predict`, and it is not a rail
        # stop on Design's own page either. Contract R1's `predict` branch
        # applies where `#s-think` gates a reveal behind a commitment; no B9
        # page does.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "ECO-03",
         "statements": [
             # `ECO-03`. The paragraph's own evidence is the chart the student
             # has already run, which is why the bench is upstream of it in the
             # document. The shower analogy is the transfer move — delayed
             # feedback producing oscillation is not a biology fact — and it is
             # Design's, kept whole.
             {"quote": "The two peaks happen at the same time — more rabbits, "
                       "more foxes.",
              "body": ["More rabbits does eventually mean more foxes, and "
                       "<em>eventually</em> is the entire content of this "
                       "lesson. A fox that finds plenty of food this spring "
                       "cannot turn that into extra foxes until its cubs "
                       "are born and survive, so the fox numbers respond to "
                       "last year's rabbits, not this year's. Look at the "
                       "chart on the bench: the green peak sits to the "
                       "right of the amber one every single time. That "
                       "delay is what makes the pattern a cycle rather than "
                       "two lines moving together. Without a lag the "
                       "populations would simply settle at a steady value "
                       "and stay there; with one, each overshoots the level "
                       "it could sustain, corrects, overshoots the other "
                       "way, and swings again — a little less far each "
                       "time. Delayed feedback producing oscillation is not "
                       "just biology — it is why a shower runs hot then "
                       "cold when the tap is slow to respond."]},
             # `ECO-04`, and the paragraph that makes K load-bearing: "Press
             # remove every fox on the bench and watch what actually happens"
             # is a real instruction to a real control, and the ceiling note is
             # the evidence waiting at the other end of it.
             #
             # ⚠️ `the next lesson` resolved to its lesson title — "What could
             # not be lifted" 2. The destination is already in `references`.
             {"quote": "Remove the predators and the prey will do brilliantly.",
              "body": ["Press <em>remove every fox</em> on the bench and watch "
                       "what actually happens. The rabbits climb steeply, "
                       "exactly as expected, and then they stop — not because "
                       "anything is eating them, but because there is only so "
                       "much grass. Every environment has a ceiling set by "
                       "food, water, space and disease, and a population that "
                       "reaches it stays there in a state that is nothing like "
                       "doing brilliantly: crowded, hungry and vulnerable to "
                       "any disease that gets in. Predators are one limit "
                       "among several, and often not the tightest one. This is "
                       "why removing a predator to help a prey species so "
                       "rarely works as intended, and it is the beginning of "
                       "Disturbing a food web, where the consequences spread "
                       "outwards to species nobody was thinking about."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RUNG 1 REPAIRED, RUNG 2 CLEAN AND UNTOUCHED.
    # Design's rung 1 fails `length_tell()` (correct 14w, strictly longest, gap
    # 4) because its correct answer states a RULE and its three distractors
    # each state a one-clause wrong REASON. The correct option is unchanged and
    # each distractor is rebuilt to state a WRONG RULE in the same
    # subject-condition-consequence shape, keeping Design's belief so that
    # every correction still answers it word for word. Repaired: 14w against
    # 14 / 12 / 15 — not strictly longest. Full working, including the three
    # beliefs and why none comes from the register, is in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Read the cycle",
            "q": "Rabbit numbers in a field have been falling for two years. "
                 "What is the fox population most likely to do next?",
            # All four state a rule about what the fox population does and why.
            # ⚑ Option A is Design's belief with its rule made explicit; B is
            # the alternative-food belief; C is the immediate-response belief,
            # which is `ECO-03`'s cousin one step further out. None is a
            # register entry — see the docstring.
            "options": [
                "Fall, because there is not enough prey to support the current "
                "number of foxes",
                "Keep rising, because foxes go on breeding while there are "
                "still rabbits to catch",
                "Stay the same, since foxes eat other prey when rabbits become "
                "scarce",
                "Rise, then fall, then rise again within the same year, "
                "because numbers respond at once",
            ],
            "answer": 0,
            # All three corrections are Design's, byte-identical, except the
            # slot code in the second — "What could not be lifted" 1.
            "feedback": {
                1: "They rise for a while after the rabbits turn — that is the "
                   "lag — but they cannot keep rising once the food runs "
                   "short.",
                2: "In this model rabbits are the only food. In a real web "
                   "there are other routes, which is the subject of Disturbing "
                   "a food web, but the population still tracks its main prey.",
                3: "A cycle takes several years, because it is limited by how "
                   "fast animals can breed.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "On a predator–prey graph, how do the two peaks line up?",
            # ⚑ Option A is `ECO-03` word for word, which is why that
            # misconception names `s-ladder` as its `elicited_by`. The student
            # who picks A has stated the belief and can be shown the chart.
            #
            # ⚖️ Option D is five words and is still not a length tell: the
            # gate measures against the LONGEST distractor (10w), the belief is
            # short because students hold it short, and padding it would make
            # it sound more considered than their own version. Do not "fix" it.
            "options": [
                "They coincide — both populations peak in the same year",
                "The predator peak comes shortly after the prey peak",
                "The prey peak comes shortly after the predator peak",
                "There is no consistent pattern",
            ],
            "answer": 1,
            "feedback": {
                0: "Then the graph would show two lines moving together and no "
                   "cycle. Look at the bench: the green peak is always to the "
                   "right.",
                2: "That has the cause and the effect the wrong way round. "
                   "Predators can only increase after there has been plenty to "
                   "eat.",
                3: "There is, and it comes from one fact: breeding takes time, "
                   "so a population responds to conditions some months or "
                   "years earlier.",
            }},
        "explain": {
            "title": "Rung 3 · Explain one full cycle",
            "q": "Describe one complete predator–prey cycle in a field of "
                 "rabbits and foxes, starting from a year when rabbits are "
                 "plentiful. Explain what causes each change rather than just "
                 "describing it.",
            "field_label": "Your explanation",
            "placeholder": "When rabbits are plentiful…",
            # The fifth criterion is the lesson's whole claim marked as a
            # criterion rather than as prose, which is what lets `#s-think`
            # stay static and still be assessed. It is also the criterion that
            # separates a description of the cycle from an explanation of it.
            "success": [
                "Says plentiful prey means more food for predators, so more of "
                "their young survive and predator numbers rise.",
                "Says more predators eat more prey than are born, so prey "
                "numbers fall.",
                "Says the falling prey population leaves predators short of "
                "food, so predator numbers fall in turn.",
                "Says fewer predators allow the prey population to recover, "
                "returning to the start.",
                "States explicitly that the predator peak comes after the prey "
                "peak, and gives the reason — breeding takes time.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A farmer plans to remove every fox from her land to protect "
                 "her chickens. Using the model, predict what will happen to "
                 "the rabbit population over the next few years, what else on "
                 "the farm might be affected, and name one thing the model "
                 "does not account for.",
            "field_label": "Your answer",
            "placeholder": "With no foxes, the rabbits…",
            # ⚑ Criterion 2 is what marks `ECO-04`, which is why that
            # misconception names `s-ladder` as its `elicited_by`: this rung
            # asks the student to write the prediction out in their own words
            # before anything marks it.
            #
            # Criterion 5 is the `analysis-and-evaluation` half of `ws` — name
            # a limitation of the model — and it is what stops the bench being
            # mistaken for a field.
            "success": [
                "Predicts the rabbit population rising quickly at first, with "
                "nothing hunting it.",
                "Says the rise will level off, because food and space set a "
                "limit even with no predators.",
                "Identifies a knock-on effect — more rabbits grazing means "
                "less grass or crop, or damage to the land.",
                "Notes that a crowded population at its limit is more "
                "vulnerable to disease or starvation.",
                "Names a genuine limitation of the model — for example that "
                "foxes eat more than rabbits, that other predators exist, that "
                "foxes will move in from neighbouring land, or that weather "
                "and disease are ignored.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Predator and prey populations cycle. Plenty of prey lets "
                "predator numbers rise; rising predator numbers push prey "
                "numbers down; scarce prey starves the predators; falling "
                "predator numbers let the prey recover. The predator peak "
                "always follows the prey peak, because breeding takes time. "
                "Prey numbers are also limited by food and space, so removing "
                "the predators does not let them rise for ever.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚖️ THE CANONICAL STORY, VERIFIED IN THE DELIVERED BYTES (payload schema
    # §13) AND LIFTED WHOLE. Three things in it are load-bearing and a later
    # pass must not simplify any of them into "lynx control hares": the linked
    # cycle stated positively; "Lynx move within that cycle as much as they
    # drive it", with the food supply and the reduced breeding that are the
    # reasons why; and the ledgers counting PELTS BROUGHT IN BY TRAPPERS rather
    # than hares alive in the forest, closing on "It is still not a census."
    #
    # ⚖️ MRB-225 holds: the layer adds the evidence and retracts nothing above
    # it. "A real rhythm" confirms the model's claim; "not a census" is about
    # the RECORD, not about the model.
    "stretch": [
        {"type": "explainer", "id": "the-ledgers-that-found-the-cycle",
         "text": "The best-known data on this were not collected by "
                 "scientists. The Hudson's Bay Company bought furs in Canada "
                 "for two centuries and kept careful records of how many lynx "
                 "and snowshoe hare pelts came in each year, and when "
                 "ecologists later plotted those ledgers they found two wavy "
                 "lines rising and falling on a cycle of roughly ten years, "
                 "with the lynx peak trailing the hare peak. A linked cycle in "
                 "two species, recovered from a company's account books: that "
                 "is what the data show, and it is the thing worth learning "
                 "from them. What they do not show is one animal governing the "
                 "other. Hare numbers rise and fall for reasons that reach "
                 "well past lynx — the shoots and twigs they feed on are "
                 "stripped after a peak and take years to grow back, and hares "
                 "living under heavy pressure raise fewer young. Lynx move "
                 "within that cycle as much as they drive it. The record "
                 "itself also needs reading with care: those ledgers count "
                 "pelts brought in by trappers, not hares alive in the forest, "
                 "so the price of fur and the number of people out trapping "
                 "are in the line too. A ten-year rhythm that survives all of "
                 "that is a real rhythm. It is still not a census."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to predict what your own change to the field would "
                      "do?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 286) and nothing in it is a safety
    # instruction — it is a note about how far the model can be trusted.
    # Routing it through `safety_note` would print it in the treatment reserved
    # for "never light a candle without an adult", which devalues the safety
    # line.
    #
    # ⚑ Its last clause is load-bearing and answers NOTES-B9 flag 5: the model
    # is here to show why a lag produces a cycle, not to predict a real field.
    # It is also what covers the honest consequence of a damped model — run far
    # enough and the cycle settles.
    "convention_note": "The bench runs a two-species model with a fixed grass "
                       "supply and no weather, disease, migration or "
                       "alternative prey. Real populations are affected by all "
                       "of those, cycle less tidily, and sometimes do not "
                       "cycle at all. The model is here to show why a lag "
                       "produces a cycle, not to predict a real field.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is a quantitative model whose output the student reads a
    # pattern out of, and rung 4 asks for a prediction FROM the model plus a
    # named limitation OF it. That is analysis and evaluation end to end.
    # No apparatus, no measurement, no variables to control: nothing here is
    # `experimental-skills` and tagging it would be a tag that is not true.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
