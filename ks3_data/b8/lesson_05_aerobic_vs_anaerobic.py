"""B8 L5 — Aerobic vs anaerobic (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b8/b8-05-aerobic-vs-anaerobic.dc.html` (569 lines), her author's
notes `docs/ks3/design-reference/b8/NOTES-B8.md`, and the B8 payload schema
`docs/ks3/b8-inventory/PAYLOAD-SCHEMA.md` §6, §7, §8, §9 and §10, under the
MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted", the six ladder
distractors repaired under MRB-177, and the one science correction marked ⚑
below. The five cases, three routes, six comparison rows, four hook options,
both marked rungs and both self-marked rungs came out of
`node tools/extract_design_payload.js`, not off a keyboard.

── `covers` — one statement, and the lesson is its three clauses ─────────

`KS3.B.RESP.04` reads, in full:

    the differences between aerobic and anaerobic respiration in terms of the
    reactants, the products formed and the implications for the organism

`ks3_data/substatements.py` splits `KS3.B.RESP.03` and does NOT split this one,
so the lesson owns it whole and must discharge all three clauses. The comparison
panel is where that happens, one clause per row-group, which is why `#s-table`
is not decoration:

    reactants                  rows *Oxygen* and *Glucose*
    the products formed        row *Products*
    implications for the       rows *Energy per glucose*, *Where in the cell*,
    organism                   *What it is for* — and the whole bench

── THE INSTRUMENT: the marathon case IS the lesson ──────────────────────

`#s-bench` is `route-decider` on `ks3-block ks3-dark ks3-practical` (page line
105), so `practical` is MEASURED from Design's own markup rather than inherited
from the hook above it — payload schema §0 rule 2.

⚖️ **`marathon` is not a fifth scenario, it is the instrument.** Its answer is
`aerobic`, and almost every student picks anaerobic because the runner is
working hard. Its `why` is the only string on the page that says out loud what
the whole bench is for: *"Hard is not the question — whether the oxygen supply
keeps up is."* Two of the five (`marathon`, `sprint`) exist to separate *working
hard* from *is the supply keeping up*, `yeast` is the only case with no aerobic
respiration in it at all, and `root` is the case b8-02's root hair cell was
built to make available.

**Do not reorder the tabs.** `sitting` first is what makes the marathon feel
like a second easy one; a student who has just been told that almost all the
respiration they will ever do is the quiet aerobic kind walks straight into the
trap, which is the only way the trap teaches anything.

⚠️ **House rule, read precisely** (payload schema §6). No green and no red
reaches the option buttons — measured, the only per-option treatment is an amber
outline on the student's own pick and a fade to 50% opacity on the two they did
not choose. The verdict panel **does** say whether they were right, in words:
`verdicts.right` = *"That is the one"*, `verdicts.wrong` = *"Not this time"*,
above the answer stated as a sentence and then the `why`. Nothing is scored and
nothing is tallied as a mark, so §0.6 holds — but this is the closest B8 comes
to the line. **Do not add colour, and do not remove the words.**

── ⚑ MRB-196 R10 — the CONTRAST self-check, authored ────────────────────

R10 gives CLASSIFY's sort and CONTRAST's settles-it a lightweight self-check:
the student is asked whether they had it and answers for themselves. **No green,
no red, nothing on the option button.** This bench is B8's settles-it — Design's
own vocabulary for it is *settled* (`ran_label`, `tally.all`, `progress`) — so
`self_check` is authored on it, in b1-06's `{question, options, note}` shape so
the two cannot ship as two shapes.

It carries **no truth value**: no `answer`, no `correct`, no `settles` key
exists anywhere inside it, so the renderer is given nothing it could grade with.
It gates nothing — the rail's BENCH stop stays `five_cases_settled`, so an
unanswered self-check can never block a student. Its question names the marathon
rather than asking about the five in general, because a look-back that does not
name the trap lets a student who fell into it report that they were fine.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to be headed "Three
rail stops, not Design's four". Design draws FOUR (`RAIL`, page lines 310–315)
and `#s-table` ticks on `opened >= CASES.length` (page line 399) — the
INSTRUMENT's predicate, character for character, one line above the bench's own
(page line 398). `#s-table` is an eyebrow, a display statement, a six-row
comparison and a key fact: no control, no commitment, no field.

The argument rested on a measurement of the built page: `doneByDom()` in
`shared/ks3.js` read only the DOM inside the stop's own section, and
`r_comparison` emits no `data-stage-done`, no `.ks3-rung`, no `[data-reveal]`,
no `.ks3-reveal-btn` and no `.ks3-option`, so
`ks3_parity.check_rail_reachable()` would fail the stop — with MRB-208's
completion rule read as forbidding a tick for something done in a different
section. So THREE stops shipped.

The measurement was right about the engine and wrong about the page.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine. When the engine cannot express the
page, the engine moves — and it has: `wireRail`'s `paint()` resolves the tick
at RAIL level, where Design computes it.

And page line 399 is a declaration, not an alias. The side-by-side table is the
payoff of the five cases the student just settled; `#s-table` carries no signals
of its own because the bench already took the commitment. That is a MIRROR.

So the fourth stop is declared: anchor `s-table`, `mirrors: "s-bench"`,
`done_when: "five_cases_settled"` — with Design's `TABLE` / *Side by side* pair
restored to it — and `check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`. b7-04's `#s-jobs`, b7-01's `#s-summary`, b5-06's
`#s-designs`, b4-05's `#s-stomata` and the rest are restored the same way.
**`#s-table` keeps its anchor**, as it always did.

The count is uniform across B8 again, at four: payload schema §7's 3, 3, 3, 3,
3 is superseded and its text has not been re-cut, so read it as historical.

── What could not be lifted byte-identical, and why ─────────────────────

1. **The comparison's label-column caption, "Compared on".** `r_comparison`
   takes exactly two columns and emits an empty `<span class="ks3-compare-name">`
   in its header row, so the third caption has nowhere to render. Below 820px
   each cell prints its own column caption and every stacked sentence stays
   attributed, which is the discrimination the block exists for; the label
   column's own heading is what is given up. No science word is lost — every row
   still carries its `name`. The fix, if the caption is to win, is a
   `name_caption` key on `comparison`, an engine change this pass does not own.

2. **The inline link in the second confrontation.** Design writes *"made
   possible by `<a href="b7-04-…">photosynthesis</a>` filling the atmosphere"*.
   `rich()` allows `<em>` and `<strong>` and nothing else, so the tag cannot
   survive. The link TEXT is the plain word *photosynthesis*, not a lesson code,
   so dropping the tag costs no word and leaks nothing — b4-05's precedent
   applies cleanly here where it did not for b7-04. The destination survives as
   a `references` edge, which Design also draws in "Connects to".

3. **The inline link in *Going further*.** Same mechanism: *"part of the
   community you met in `<a href="b3-08-…">Bacteria in the gut</a>`"*. The link
   text is a lesson TITLE, so the words stay and the tag goes, and
   `bacteria-in-the-gut` is carried as a `references` edge.

4. ⚠️ **`b8-03` IS RESOLVED TO A LESSON TITLE IN THE `sprint` CASE, AND THIS ONE
   IS NOT COSMETIC.** Design's `why` reads *"the runner pays it back afterwards
   — the oxygen debt from b8-03."* A build-internal slot code cannot be resolved
   by a student, and printing one is exactly the platform leakage §8.10 exists
   to stop. Replaced by what it stands for, using Design's own endmatter string
   for the same destination:

       Design:  the oxygen debt from b8-03.
       Built:   the oxygen debt from Anaerobic respiration in humans.

   Every science word is unchanged, and the destination is already a `requires`
   edge, so the link Design meant is not lost.

5. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

6. **The bench's section heading loses its `<h2>` level.** Design draws "Which
   route is running here?" as an `<h2>` inside `#s-bench` beside a mono counter.
   It is authored as the instrument's `heading` and the renderer decides the
   tag. No word changes.

── ⊕ MRB-177 LENGTH PARITY — BOTH MARKED RUNGS FAILED AS DRAWN ──────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one):

    AS DESIGN DREW THEM                      AFTER THE REPAIR
    rung 1  correct 16w vs 3 / 5 / 4   ✗     correct 16w vs 16 / 15 / 13   ✓
    rung 2  correct 14w vs 9 / 11 / 12 ✗     correct 14w vs 16 / 16 / 17   ✓

Rung 1 was the worst tell in the unit: the correct answer was sixteen words and
the longest distractor was five. A student could have scored it without reading
a word of the science.

The construct, per Mide's 17 Aug 2026 ruling: on a rule-stating rung the correct
answer states a RULE — subject, condition, consequence — while the distractors
stated one-clause wrong REASONS, so the correct answer was longer BY
CONSTRUCTION. A distractor must state a WRONG RULE instead, in the same shape,
with the misconception as the consequence.

**The correct option of each rung is unchanged, both `answer` indices are
unchanged, Design's option ORDER is unchanged, and all six of Design's
corrections are byte-identical.** Six distractors were rewritten, each keeping
the belief it already carried and gaining the consequence that belief licenses:

    r1 B  energy release marks it out  + "so a cell that needs energy has to use
                                          this route"                  RESP-09
    r1 C  location inverted            + "so a cell with few mitochondria cannot
                                          use this route"              authored
    r1 D  human anaerobic makes CO₂    + "which is why you breathe harder after
                                          a sprint"                    authored
    r2 B  both halves inverted         + mirrors the correct option's own two
                                          clauses, swapped              RESP-09
    r2 C  anaerobic yields more        + "so a sprinter uses it to get more out"
                                                                        RESP-09
    r2 D  equal yields, nasty waste    + "anaerobic differs only by leaving a
                                          harmful waste product"       authored

⚖️ **All six corrections still answer their rewritten option better than they
answered the original**, which is the sign the repair was to the construct and
not to the science. r2 A is the clearest: the rewritten option now states the
correct answer's own two clauses with the labels swapped, and Design's
correction is already *"Both halves are the wrong way round."*

── ⚑ FOR MIDE'S SCIENCE GATE — the NOTES-B8 flags landing on this lesson ─

  * flag 19   **"About twenty times more energy", used throughout.**
              CHECKED, LEFT IN THE BODY, AND ONE SITE CORRECTED — see the ⚑
              below. The figure comes from the usual 2 vs 38 ATP comparison, so
              about nineteen, and "about twenty" is a defensible rounding of it
              in the safe direction only because of the hedge. The legal line at
              the foot of Design's page does say what the schema says it says,
              verbatim: *"'About twenty times more energy' is the usual teaching
              comparison and comes from the ATP yields met at GCSE; the exact
              ratio depends on how the accounting is done."* It is authored here
              as `convention_note`.

              It survives MRB-225 as written **because the hedge is in the body,
              not in the foot note.** The word *about* is in the hook heading,
              in `#s-think`, in the comparison row, in rung 2's fourth
              correction and in rung 3's fourth criterion. The foot note
              EXPLAINS the hedge; it does not introduce one, and no sentence on
              the page takes back a claim an earlier sentence made. That is the
              MRB-225 test and it passes.

              ⚠️ If Mide moves the figure it moves in **nine** places on this
              page. Counted in this record, not taken from the schema:

                  1  `phenomenon.title`      "about twenty times more"
                  2  `phenomenon.prompt`     "a twentyfold waste of food"
                  3  `#s-think` statement 1  "about twenty times more"
                  4  comparison row *Energy per glucose*
                                             "About twenty times more."
                  5  rung 2 `feedback[3]`    "about twentyfold apart"
                  6  rung 3 criterion 4      "about twenty times more energy"
                  7  `stretch` closing       "about twenty times more energy"
                  8  `convention_note`       "About twenty times more energy"
                  9  `marathon` case `why`   "at twenty times the fuel cost"

              Eight of the nine are hedged. The ninth is deliberately not — see
              the ⚑ immediately below.

  * ⚑ ONE UNHEDGED RESTATEMENT, CORRECTED. One word: "about".

    *Going further* closed: *"and using it turned out to release twenty times
    more energy, which is most of the reason anything larger than a bacterium
    exists."* Every other statement of the ratio on the page is hedged; this one
    is not, and it is not a back-reference — it is a fresh assertion of the
    number carrying the lesson's largest claim. Under MRB-225 the claim shrinks
    until it is true, and the true figure is about nineteen on the traditional
    accounting and lower on a modern one. Written as **"about twenty times more
    energy"**, which is the page's own form everywhere else. The teaching point
    — that the yield is why anything big exists — survives untouched.

    The `marathon` case's *"at twenty times the fuel cost"* is deliberately
    LEFT as drawn. It is a back-reference to a figure the hook and `#s-think`
    have already hedged twice before the student reaches the bench, it is inside
    the one verdict the whole lesson turns on, and hedging it there would blunt
    the sentence the instrument exists to deliver. Recorded rather than quietly
    changed.

  * flag 20   **The Great Oxygenation Event, and the overlap with b7-04.**
              CHECKED AND LEFT AS DRAWN. **It BUILDS on b7-04; it does not
              repeat it.** b7-04 is LIVE and was read against this page
              (`ks3_data/b7/lesson_04_why_almost_all_life_depends_on_it.py`,
              its second confrontation). The two tell the same two billion years
              from opposite ends, and neither contains the other:

                  b7-04  the PRODUCER's end. Where the oxygen came from, that
                         it is a waste product, that it was poisonous at the
                         time, and that breathing animals arrived afterwards
                         into an atmosphere already there. Its job is to kill
                         "plants make oxygen for us".
                  b8-05  the RESPIRER's end. That every living thing respired
                         anaerobically first, that the survivors of the
                         poisoning are alive and locatable — a compost heap, a
                         rumen, your own large intestine — and that using the
                         poison is what made large bodies affordable.

              Three things are here that are in no other lesson: obligate
              anaerobes as present-day evidence rather than history, the
              extinction itself, and the causal link from the twentyfold yield
              to body size. That last one is what makes this the CONTRAST
              lesson's closing layer rather than a second telling of B7's.
              The reference is carried as a `references` edge, which is Design's
              own "Connects to" card, and `#s-think`'s stripped inline link
              points at the same lesson.

              What is Mide's, and is not settled by any of the above: whether
              "arguably the largest mass extinction in Earth's history" is a
              claim to put in front of a student your age at all. It is well
              supported and it is hedged with *arguably*. Left as drawn.

  * flag 21   **No diagrams in the unit, and I MEASURED it.**
              `grep -c "<img\\|<figure\\|<picture"` over
              `docs/ks3/design-reference/b8/b8-05-aerobic-vs-anaerobic.dc.html` returns **0**.
              The only SVG on the page is UI furniture: the nav chevron, the
              rail tick, the endmatter link arrows and the ladder tick/cross
              marks. No placeholder, no empty frame, no caption with nothing
              under it. §4.10 allows an empty `figures` for a lesson carried by
              its interactives, so `figures` is `[]`. A mitochondrion and a
              labelled gas-flow figure are the obvious candidates and neither is
              in `docs/ks3/diagram-manifest.md`. The flag is NOT dropped — it is
              Mide's to rule on.

── ⛔ BLOCKER FOR THE COMMANDER: the `RESP` register rows do not exist ───

NOTES-B8 §5 states `RESP-01`..`RESP-10` are *"written into
`docs/ks3/misconception-register.md` with a new prefix row"*. **They are not.**
Grepped at authoring time: the register carries fourteen prefixes — `ATOM BODY
BREATH CELL DIET DRUG ECO GENE LIFE NOS PART PLANT REACT REPRO` — and no `RESP`
row of any kind. `docs/ks3/*` is the commander's file and the brief bars this
pass from touching it, so the rows are REPORTED, not opened. The identical claim
was made by NOTES-B5 about `REPRO` and by NOTES-B7 about `PLANT`; third
occurrence.

`RESP-09` and `RESP-10` below are this lesson's pre-allocated pair and their
statements are Design's own `#s-think` quotes, which is the form the register
wants — the wrong belief as a student holds it. `RESP-15` is this lesson's named
spare. It is **not needed and stays permanently unused**, like `DRUG-07`,
`REPRO-17`/`20`/`21`/`23` and `PLANT-09`..`12`. Do not re-point it.

⚖️ NOTES-B8 §5 asks whether `RESP-06` (*they switch*) and `RESP-09` (*rate
confused with yield*) should merge. They should not, and this page is the
evidence: `RESP-09` is elicited by a student picking **anaerobic for the
marathon** — a judgement about which route is supplying energy under a load —
while `RESP-06` is about the two routes being alternatives that take turns.
Design's `sprint` verdict kills the second in its own last sentence (*"aerobic
respiration never stopped; nothing switched off"*) while leaving the first
standing, which two ids can express and one cannot.

── Keys this pass authors that the ENGINE pass must wire (contract R5) ───

R5 says no key is authored without a read site in the same pass. The renderer
for `route-decider` belongs to the engine pass, so its read sites are named
here explicitly rather than left to be discovered. Everything below follows
payload schema §6 except the last, which the schema does not anticipate:

    cases_label   str                          page line 116
    options_label str                          page line 127
    routes        [{id, text}]                 page line 318 (`ROUTES`)
    cases         [{id, label, text, answer, why}]  page line 324 (`CASES`)
    progress      "{n} of {total} settled"     page line 486 (`benchProgress`)
    tally         {remaining, all}             page line 509 (`tallyLabel`)
    run_label / ran_label                      page line 508 (`checkLabel`)
    verdicts      {right, wrong}               page line 512 (`verdictWord`)
    done_after    5                            page line 399
    self_check    {question, options, note}    ⚑ MRB-196 R10 — NOT on Design's
                                               page, and not in schema §6

⚠️ `answer` must not leak into a tab, an `aria-label` or a `title`: the verdict
panel is the only place a case's route is named, and the whole bench depends on
the student committing before they can see it.

⚠️ **`ks3_data/b8/__init__.py` must map `"route-decider": "practical"` in its
`_INSTRUMENT_SEGMENTS` dict** or this block ships as an unlifted bare list past
a green kinds gate. That file is owned by another pass and is not touched here;
checked at authoring time and the entry is present.

⚠️ **THIS INSTRUMENT IS ON INK.** `.ks3-dark p` is (0,1,1) and beats a bare
instrument class at (0,1,0). As of MRB-245 that is gated by
`ks3_parity.check_dark_text_specificity()`, so forgetting it is a red build
rather than a shipped 1.21:1 label.

⚠️ **No runtime state is authored** (payload schema §0 rule 3). `caseId`,
`picks` and `opened` are values the runtime owns. Design's `startCase` is
`sitting`, which is `cases[0]`, so a renderer that opens on the first case
reproduces it without a key.
"""

# ── the three routes (page line 318, via extract_design_payload.js) ──────
#
# ORDER IS DESIGN'S AND IS LOAD-BEARING: aerobic, both, anaerobic runs from
# "all of one" through "a mixture" to "all of the other". A student reading down
# the list meets the mixture in the middle, which is where it belongs — it is
# the answer to two of the five and the one nobody reaches for first.
ROUTES = [
    {"id": "aerobic",   "text": "Almost entirely aerobic"},
    {"id": "both",      "text": "Aerobic, with anaerobic making up a shortfall"},
    {"id": "anaerobic", "text": "Almost entirely anaerobic — very little "
                                "oxygen is available"},
]

# ── the five situations (page line 324, via extract_design_payload.js) ───
#
# ⚖️ DO NOT REORDER. `sitting` first is what makes `marathon` feel like a second
# easy one, and `marathon` is the instrument — see the docstring. Two of the
# five separate *working hard* from *is the supply keeping up*; `yeast` is the
# only one with no aerobic respiration in it at all; `root` is the case b8-02's
# root hair cell exists to make available.
CASES = [
    {"id": "sitting", "label": "Sitting in class", "answer": "aerobic",
     "text": "You are sitting still, reading this page.",
     "why": "Demand is low and the oxygen supply covers it easily, so the "
            "glucose is broken down completely and effectively no lactic "
            "acid accumulates. "
            "Almost all the respiration you do in a lifetime is this, which is "
            "worth remembering when the topic makes it sound like an emergency "
            "measure."},

    # ⚖️ THE CASE THE LESSON IS BUILT ROUND. Answer `aerobic`, and almost
    # everyone picks anaerobic because the runner is working hard. Its `why` is
    # the only string on the page that states the bench's own criterion out
    # loud, and `self_check` below names this case rather than the five in
    # general so a student who fell in cannot report that they were fine.
    #
    # ⚑ "at twenty times the fuel cost" is UNHEDGED and is left as drawn — a
    # back-reference to a figure hedged twice already. See the docstring.
    {"id": "marathon", "label": "Marathon runner", "answer": "aerobic",
     "text": "A marathon runner, two hours into a race, holding a steady pace.",
     "why": "This is the answer people get wrong because the runner is working "
            "hard. Hard is not the question — whether the oxygen supply keeps "
            "up is. A marathon is run deliberately just below the pace at which "
            "the anaerobic route would take over, because at twenty times the "
            "fuel cost nobody could sustain it for two hours."},

    # ⚠️ "b8-03" RESOLVED TO THE LESSON TITLE. A slot code cannot be resolved by
    # a student and printing one is §8.10 leakage. See "What could not be
    # lifted" 4 — the destination is already a `requires` edge.
    #
    # The last sentence is also what keeps `RESP-06` (*they switch*) separable
    # from `RESP-09` (*rate confused with yield*): it kills the first and leaves
    # the second standing. NOTES-B8 §5 asks whether the two should merge; this
    # is the evidence that they should not.
    {"id": "sprint", "label": "100 m sprinter", "answer": "both",
     "text": "A sprinter in the last three seconds of a 100 m race.",
     "why": "Aerobic respiration is running flat out and is nowhere near "
            "enough. The shortfall is covered anaerobically, lactic acid "
            "accumulates, and the runner pays it back afterwards — the oxygen "
            "debt from Anaerobic respiration in humans. Note that aerobic "
            "respiration never stopped; nothing switched off."},

    {"id": "yeast", "label": "Yeast in dough", "answer": "anaerobic",
     "text": "Yeast in a sealed ball of bread dough, rising on a warm shelf.",
     "why": "No oxygen reaches most of the dough, so the yeast ferments: "
            "glucose to ethanol and carbon dioxide. The gas is what raises "
            "the loaf. This is one of the two cases on the bench where "
            "fermentation supplies nearly all the energy — and it is not an "
            "emergency for the yeast, it is a living."},

    {"id": "root", "label": "Roots in flooded soil", "answer": "anaerobic",
     "text": "The root cells of a houseplant standing in waterlogged soil.",
     "why": "Water has filled the air spaces in the soil, so no oxygen reaches "
            "the roots. The cells respire anaerobically, which gives them "
            "nowhere near enough energy for active transport, and they begin to "
            "die — which is why an overwatered plant shows the symptoms of a "
            "plant with no water at all."},
]

# ── the six comparison rows (page line 342, via extract_design_payload.js) ──
#
# Read ACROSS a row: `name` is what the two routes are being compared on, and
# the two cells are aerobic then anaerobic, in Design's column order.
#
# The last row is the one the panel's own statement points at — "Six
# differences, and the last one is the one that matters" — because *what it is
# for* is the only row that is about the ORGANISM rather than about the
# chemistry, and it is the row `KS3.B.RESP.04`'s third clause is discharged by.
ROWS = [
    {"name": "Oxygen",
     "cells": ["Required.",
               "Not used at all."]},
    {"name": "Glucose",
     "cells": ["Broken down completely.",
               "Broken down only partly — there is energy left in the "
               "product."]},
    {"name": "Products",
     "cells": ["Carbon dioxide and water.",
               "Lactic acid in humans; ethanol and carbon dioxide in yeast."]},
    # ⚑ NOTES-B8 flag 19, site 4 of nine. The docstring lists all nine,
    # because if Mide moves the figure it moves in all of them.
    {"name": "Energy per glucose",
     "cells": ["About twenty times more.",
               "A small fraction of the aerobic yield."]},
    {"name": "Where in the cell",
     "cells": ["In the mitochondria.",
               "Outside them, which is why cells with few mitochondria can "
               "still do it."]},
    {"name": "What it is for",
     "cells": ["Everything, all the time — the default.",
               "Energy needed faster than oxygen arrives, or no oxygen "
               "available at all."]},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 150 character for character.
    "slug":        "aerobic-vs-anaerobic",
    "title":       "Aerobic vs anaerobic",
    "discipline":  "biology",
    "unit":        "respiration",
    "family":      "CONTRAST",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.RESP.04` owned WHOLE — reactants, products, implications, no split
    # in `ks3_data/substatements.py`. See the docstring's mapping.
    "covers":      ["KS3.B.RESP.04"],
    # Named, used, and owned elsewhere. RESP.01 is b8-01 and b8-02's — the
    # reaction and the "enabling every other process" clause, both assumed
    # throughout and neither restated. RESP.03 is b8-03 and b8-04's: lactic
    # acid, fermentation, ethanol, the oxygen debt. PHOT.02 is b7-04's, and it
    # is the oxygen history that `#s-think` and *Going further* both lean on.
    "touches":     ["KS3.B.RESP.01", "KS3.B.RESP.03", "KS3.B.PHOT.02"],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 3},
                    {"id": "cells-and-systems", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's endmatter: "Before this lesson → Anaerobic respiration in humans,
    # Fermentation and what we use it for"; "Connects to → Why almost all life
    # depends on it, Bacteria in the gut". Both prerequisites are B8's own and
    # are authored in this run, so `requires` resolves; both references cross a
    # unit boundary and take the dict form §4.6 requires.
    "requires":    ["anaerobic-respiration-in-humans", "fermentation"],
    "assumes":     [],
    # `why-almost-all-life-depends-on-it` also carries the stripped inline link
    # out of `#s-think` — "What could not be lifted" 2 — and is the lesson that
    # owns the oxygen history this page builds on rather than restates (flag 20,
    # docstring). `bacteria-in-the-gut` carries the one out of *Going further*.
    "references":  [{"unit": "B7",
                     "lesson": "why-almost-all-life-depends-on-it"},
                    {"unit": "B3", "lesson": "bacteria-in-the-gut"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "ATP yields compared numerically, metabolism as a whole, and "
                   "the biotechnology built on anaerobic organisms.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Two ways to get energy out of the same sugar molecule. One "
                    "releases far more of it. The other releases it far faster. "
                    "Almost everything alive uses both, and knowing which is "
                    "running when is the whole point of this unit.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-table` is the third: no control of
    # its own, so it mirrors `s-bench` and ticks on the bench's predicate — see
    # the docstring, which supersedes payload schema §7's count. `short` and
    # `label` are Design's own `RAIL_SHORT` and `RAIL` strings (page lines
    # 310–316), `TABLE` / *Side by side* included.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Twenty times",
         "done_when": "committed"},
        # Design's own threshold, kept: `opened >= CASES.length` (page line
        # 398). All five settled, not one — a student who settles the two easy
        # ones and leaves has not met the marathon.
        {"anchor": "s-bench", "short": "BENCH", "label": "Which route",
         "done_when": "five_cases_settled"},
        {"anchor": "s-table", "short": "TABLE", "label": "Side by side",
         "mirrors": "s-bench", "done_when": "five_cases_settled"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key. Option B is the one
    # the reveal endorses, and the reveal says so immediately: the hook is not a
    # trick, it is the claim the rest of the page has to earn. Its last sentence
    # is the lesson's thesis in one line — two different questions, and
    # confusing them is where the trouble comes from.
    "phenomenon": {
        "kind": "narrative",
        # ⚑ NOTES-B8 flag 19, site 1 of nine (site 2 is the prompt below).
        # Hedged, and the hedge is what makes it true — see the docstring.
        "title": "One route gets about twenty times more out of the same "
                 "glucose.",
        "prompt": "If that were the only thing that mattered, the other route "
                  "would have disappeared long ago — a twentyfold waste of food "
                  "is not a small disadvantage. It has not disappeared. Every "
                  "organism in this unit, from a sprinter to a yeast cell, "
                  "keeps it available.",
        "commit": "So why does anaerobic respiration exist at all?",
        "options": [
            "It only exists in yeast and bacteria, not in humans",
            "It releases energy faster, and without waiting for oxygen",
            "It releases more energy in total",
            "It is the only way a cell can break down glucose",
        ],
        "reveal": "Because it is faster, and it does not have to wait for a "
                  "delivery. Aerobic respiration wins on how much energy it "
                  "gets from each glucose molecule; anaerobic respiration wins "
                  "on how quickly it can supply energy, and it works when there "
                  "is no oxygen to be had. Those are two different questions, "
                  "and confusing them is where most of the trouble in this "
                  "topic comes from.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # `RESP-09` and `RESP-10` are the commander's pre-allocation and both
    # statements are Design's own `#s-think` quotes, which is the register's own
    # form — the wrong belief as a student holds it. The named spare `RESP-15`
    # is NOT used and stays permanently unused. See the docstring; the `RESP`
    # rows do not yet exist in the register and that is reported, not fixed
    # here.
    #
    # Both `elicited_by` and `confronted_by` resolve against the BUILT page
    # (MRB-244 / MRB-248): `s-hook`, `s-bench` and `s-think` are all emitted as
    # `id="…"`. `s-think` is not a rail stop and does not need to be — the gate
    # wants an emitted element, not a completion signal.
    "misconceptions": [
        # Elicited at the bench, and by one case in particular: a student who
        # holds "fast means anaerobic" picks anaerobic for the marathon runner,
        # commits it, and then reads the verdict. That is the belief stated by
        # the student in their own hand, which is what Law 4 asks for and what
        # `#s-think`'s first paragraph then takes apart — two meanings of fast,
        # yield against rate.
        {"id": "RESP-09",
         "statement": "Aerobic respiration is the fast one, because that is the "
                      "one athletes train for.",
         "elicited_by": "s-bench",
         "confronted_by": "s-think"},
        # Elicited in the hook. "So why does anaerobic respiration exist at
        # all?" is precisely the question a student answers to themselves with
        # "because sometimes something goes wrong", and option A is that belief
        # in its other costume — that it is not something humans do. The second
        # confrontation is where it dies: yeast in a vat is not in trouble, and
        # for an obligate anaerobe air is the emergency.
        {"id": "RESP-10",
         "statement": "Anaerobic respiration is the emergency backup — "
                      "something has gone wrong when it happens.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B8, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ The pair is declared HERE as a pair even though b8-01 and b8-03 each
    # own one of them, because a CONTRAST lesson's vocabulary is the
    # DISTINCTION, and a chip list that carried only one of the two would be
    # the lesson's own point stated wrongly. The definitions are written against
    # each other for the same reason.
    "vocabulary": [
        {"term": "aerobic respiration",
         "definition": "Releasing energy from glucose using oxygen, breaking "
                       "the glucose down completely to carbon dioxide and "
                       "water.",
         "note": "The default. Almost all the respiration you will ever do."},
        {"term": "anaerobic respiration",
         "definition": "Releasing energy from glucose without using oxygen, "
                       "breaking it down only partly.",
         "note": "Less energy from each glucose, and it arrives faster."},
        {"term": "lactic acid",
         "definition": "The product of anaerobic respiration in human muscle — "
                       "a substance that still holds energy.",
         "note": "Not a waste product: the liver recovers what is left in it."},
        {"term": "fermentation",
         "definition": "Anaerobic respiration in a micro-organism — in yeast, "
                       "glucose giving ethanol and carbon dioxide.",
         "note": "What we call the food is the organism's waste."},
        {"term": "obligate anaerobe",
         "definition": "An organism for which oxygen is poisonous, and which "
                       "can live only where there is none.",
         "note": "In mud, in a compost heap, in a rumen, and in your own "
                 "large intestine."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED, NOT ASSUMED. `<img>`, `<figure>` and `<picture>`
    # each appear ZERO times in the approved page — counted, not eyeballed. The
    # only SVG on it is UI furniture (nav chevron, rail tick, endmatter arrows,
    # ladder tick and cross). Nothing is declared, because declaring a slot
    # would invent a sourcing task in `docs/ks3/diagram-manifest.md` and a
    # caption would pre-empt the ruling NOTES-B8 flag 21 asks for. The flag is
    # not dropped — it is Mide's.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline in `core` where its position
        # in the document is obvious, and lifted into `activities[]` by
        # ks3_data/b8/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED, not inherited.
        #
        # Payload keys follow docs/ks3/b8-inventory/PAYLOAD-SCHEMA.md §6, plus
        # `self_check`, which the schema does not anticipate and MRB-196 R10
        # requires of a CONTRAST lesson. Read sites for all of them are named in
        # the docstring under "Keys this pass authors".
        {"type": "route-decider", "id": "which-route-is-running",
         "anchor": "s-bench", "demand": "decide",
         "eyebrow": "At the bench · five situations",
         "heading": "Which route is running here?",
         "prompt": "Commit to an answer before you check it. Three of the "
                   "five are not the answer most people give first, and in "
                   "two of them fermentation is supplying nearly all the "
                   "energy.",

         "cases_label":   "The situation",
         "options_label": "Which route is supplying the energy?",
         "routes": ROUTES,
         "cases":  CASES,

         "progress": "{n} of {total} settled",
         "tally":    {"remaining": "{n} still to settle",
                      "all": "all five settled"},
         "run_label": "Check it",
         "ran_label": "Settled",
         # ⚠️ Words, not colour. The verdict panel names the answer in a
         # sentence and says whether the student had it; nothing green and
         # nothing red reaches an option button. Do not add colour, and do not
         # remove the words. Payload schema §6, and the docstring.
         "verdicts": {"right": "That is the one", "wrong": "Not this time"},
         "done_after": 5,

         # ⚑ MRB-196 R10, for CONTRAST. Shown once all five are settled, on the
         # block's own ground. It carries NO truth value — no `answer`, no
         # `correct` — so the renderer is given nothing it could grade with, and
         # it gates nothing: the BENCH stop stays `five_cases_settled`. It names
         # the marathon rather than the five in general, because a look-back
         # that does not name the trap lets a student who fell into it report
         # that they were fine. Shape is b1-06's `{question, options, note}`.
         "self_check": {
             "question": "Now look back at the five. Did you have the marathon "
                         "runner?",
             "options": [
                 "Yes — aerobic, and because the oxygen supply was keeping up.",
                 "Aerobic, but because two hours sounds gentle rather than "
                 "because the supply keeps up.",
                 "No — I went for anaerobic, because the runner is working "
                 "hard.",
             ],
             "note": "Nobody marks this but you. Working hard and running short "
                     "of oxygen are two different questions, and all five turn "
                     "on the second one.",
         }},

        # #s-table — the band panel. Rail stop 3, mirroring `s-bench`; see the
        # docstring. Its anchor also carries every hash link into it.
        # `comparison` is the component: six rows, two captioned columns and the
        # key fact Design nests inside the panel (page lines 169–172).
        {"type": "comparison", "anchor": "s-table",
         "eyebrow": "Side by side",
         "eyebrow_tone": "accent-text",
         "statement": "Six differences, and the last one is the one that "
                      "matters.",
         "ground": "band",
         "columns": [{"caption": "Aerobic"}, {"caption": "Anaerobic"}],
         # Design paints both cells at the same weight — neither route is the
         # quiet one, which is the whole argument of a CONTRAST panel.
         "row_tones": ["ink", "ink"],
         "rows": ROWS,
         "key_fact": {"ref": "two-routes-one-sugar", "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "RESP-09"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # One per lesson, nested in the comparison above, on the card ground —
    # Design's own `box-shadow: 5px 5px 0 var(--ks3-accent)`, which is the
    # shipped stylesheet's value, so contract R3 does not arise here.
    # Never amber (MRB-208).
    #
    # It carries the "about twenty times" claim only by implication — "far more
    # energy per molecule" — which is deliberate: the box is the summary a
    # student photographs, and a hedged number in a photographed box is a number
    # that will be quoted without its hedge.
    "key_facts": [
        {"id": "two-routes-one-sugar",
         "text": "Aerobic respiration uses oxygen, breaks glucose down "
                 "completely to carbon dioxide and water, and releases far more "
                 "energy per molecule. Anaerobic respiration uses no oxygen, "
                 "breaks glucose down only partly, releases much less energy "
                 "per molecule — and can do it faster, and without waiting.",
         "placement": "nested",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment, on Design's page and
        # here: it is a quoted belief, a paragraph, a 2px `--ks3-alert-border`
        # rule, a second quoted belief and a second paragraph, with no options
        # list, no reveal, no button and no state. So under contract §2 R1 it is
        # a `confrontation`, not a `predict` — R1's `predict` branch applies
        # where `#s-think` gates a reveal behind a commitment, and B8 never
        # does. Measured on all five B8 pages (payload schema §8). It is not a
        # rail stop on any of them and Design's `RAIL` never lists it, so
        # emitting no `data-stage-done` costs nothing.
        #
        # ⚠️ `quote` carries NO quotation marks: `_quoted()` adds Design's curly
        # pair in the renderer, and authoring them here would double them.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "RESP-09",
         "statements": [
             # `RESP-09`. The two `<em>`s are Design's and are load-bearing
             # typography rather than decoration — they are what visually
             # separates *per glucose molecule* from *per second*, which is the
             # entire distinction the paragraph exists to make. `rich()` passes
             # `<em>` and would strip anything else.
             #
             # ⚑ NOTES-B8 flag 19, site 3 of nine. Hedged.
             {"quote": "Aerobic respiration is the fast one, because that is "
                       "the one athletes train for.",
              "body": ["Two different meanings of fast are being run together, "
                       "and separating them settles most of this topic. "
                       "Aerobic respiration releases more energy <em>per "
                       "glucose molecule</em> — about twenty times more — which "
                       "is a statement about yield. Anaerobic respiration "
                       "releases energy <em>per second</em> at a higher rate, "
                       "because it involves fewer steps and does not depend on "
                       "oxygen arriving from outside the cell. A sprinter needs "
                       "power now and does not care what it costs in sugar; a "
                       "marathon runner needs to keep going for two hours and "
                       "cannot afford waste, so the whole race is run just "
                       "below the pace where the anaerobic route would take "
                       "over. Both athletes have the same two systems. What "
                       "differs is which constraint their event puts them "
                       "under, and their training moves the line between the "
                       "two."]},
             # `RESP-10`. The last sentence is the b7-04 citation: the anchor is
             # stripped and the plain word *photosynthesis* stays, so nothing is
             # lost and no build code reaches a student — "What could not be
             # lifted" 2. This paragraph is a CITATION of B7's oxygen history,
             # not a restatement of it; what it adds is the consequence for
             # respiration, which is B8's business and not B7's. See flag 20 in
             # the docstring.
             {"quote": "Anaerobic respiration is the emergency backup — "
                       "something has gone wrong when it happens.",
              "body": ["It is a strategy, not a failure. Yeast in a sealed vat "
                       "is not in trouble: it is doing the only thing available "
                       "and doing it deliberately, and we built an industry on "
                       "the result. Bacteria in a cow's rumen, in a bog, in a "
                       "sealed jar of sauerkraut and in your own gut live "
                       "anaerobically as a matter of routine, and some of them "
                       "are killed by oxygen — for them, air is the emergency. "
                       "Even in your muscles the anaerobic route is not a "
                       "fault: it is what lets you sprint for a bus, and the "
                       "burning that stops you is a control mechanism "
                       "protecting the muscle, not a breakdown. There is also a "
                       "historical point worth knowing. Anaerobic respiration "
                       "is the older process by a long way, because for the "
                       "first two billion years of life on Earth there was "
                       "almost no oxygen to respire with — the aerobic route is "
                       "the newcomer, made possible by photosynthesis filling "
                       "the atmosphere with a gas that was, at the time, a "
                       "poison."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY. BOTH marked rungs failed as Design drew them —
    # rung 1 by eleven words, which is the worst tell in the unit — and both are
    # repaired by rewriting distractors into wrong RULES of the same shape.
    # Correct options, `answer` indices, option order and all six corrections
    # are unchanged. Full working, with before-and-after counts and the belief
    # each rewritten distractor names, is in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Tell them apart",
            "q": "Which statement is true of anaerobic respiration in humans "
                 "but not of aerobic respiration?",
            "options": [
                # 16w — Design's, unchanged.
                "It releases energy from glucose, so a cell that needs energy "
                "has to use this route",
                # 16w — `RESP-09` wearing a rule: energy release is what marks
                # this route out. Was "It releases energy" (3w).
                "It happens in the mitochondria, so a cell with few "
                "mitochondria cannot use this route",
                # 15w — the inverted location, given its consequence. Was "It
                # happens in the mitochondria" (5w). The consequence is the
                # exact claim the comparison's *Where in the cell* row denies,
                # which is where a student can go and check it.
                "The glucose is only partly broken down, so a product is left "
                "that still holds energy",
                # 13w — human anaerobic respiration makes carbon dioxide. Was
                # "It produces carbon dioxide" (4w). The new clause supplies the
                # reason a student actually has for believing it — you do breathe
                # harder after a sprint — which is what makes the correction
                # land instead of merely contradict.
                "It produces carbon dioxide, which is why you breathe harder "
                "after a sprint",
            ],
            "answer": 2,
            "feedback": {
                0: "Both do — that is the point of respiring. What differs is "
                   "how much, and how fast.",
                1: "The other way round. Aerobic respiration is the one that "
                   "happens in the mitochondria.",
                3: "In humans it produces lactic acid and no carbon dioxide. In "
                   "yeast it does produce carbon dioxide, which is a good "
                   "reason to name the organism when you answer.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Which describes the difference correctly?",
            "options": [
                # 14w — Design's, unchanged.
                "Aerobic supplies energy at a faster rate; anaerobic is slower "
                "but gets more from each glucose",
                # 16w — `RESP-09`, and the cleanest instance of the MRB-177
                # construct in the key stage: the correct answer's own two
                # clauses with the labels swapped. Was "Aerobic is faster;
                # anaerobic is slower but more efficient" (9w), and Design's
                # correction already reads "Both halves are the wrong way
                # round", which is now literally true of the option.
                "Anaerobic releases more energy from each glucose, so a "
                "sprinter uses it to get more out",
                # 16w — `RESP-09` again, from the yield side. Was "Anaerobic
                # releases more energy overall, which is why sprinters use it"
                # (11w). The sprinter stays in the option because the
                # correction answers the sprinter.
                "They release the same energy per glucose, and anaerobic "
                "differs only by leaving a harmful waste product",
                # 17w — was "They release the same energy, but anaerobic makes a
                # harmful waste product" (12w). The rewritten clause makes the
                # claim a RULE about what the difference IS, which is what the
                # rung asks, and it names the second belief the correction
                # kills: that lactic acid is waste.
                "Aerobic gets more energy from each glucose; anaerobic supplies "
                "energy at a faster rate",
            ],
            "answer": 3,
            "feedback": {
                0: "Both halves are the wrong way round. Aerobic is the "
                   "efficient one; anaerobic is the quick one.",
                1: "It releases much less per glucose. Sprinters use it because "
                   "it arrives quickly, not because there is more of it.",
                # ⚑ NOTES-B8 flag 19, site 5 of nine.
                2: "The yields are about twentyfold apart. And the lactic acid "
                   "is not waste — the liver deals with it and recovers the "
                   "energy left in it.",
            }},
        "explain": {
            "title": "Rung 3 · Two athletes",
            "q": "A 100 m sprinter and a marathon runner have the same two "
                 "respiration systems. Explain why their events depend on them "
                 "so differently, and why the marathon runner paces the race "
                 "instead of running as fast as possible.",
            "field_label": "Your explanation",
            "placeholder": "The sprinter needs energy…",
            "success": [
                "Says the sprinter needs energy far faster than oxygen can be "
                "delivered, so a large part comes anaerobically.",
                "Says this produces lactic acid, which builds up and forces "
                "them to slow down — tolerable over ten seconds.",
                "Says the marathon runner cannot do this, because lactic acid "
                "would accumulate long before the finish.",
                # ⚑ NOTES-B8 flag 19, site 6 of nine.
                "Says aerobic respiration gets about twenty times more energy "
                "from each glucose, so it is the only affordable route over two "
                "hours.",
                "Concludes that pacing means holding a speed at which the "
                "oxygen supply still covers the demand.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "Some bacteria are killed by oxygen and live only where there "
                 "is none — in mud, in a compost heap, in the gut. Explain how "
                 "an organism can live entirely without oxygen, what it gives "
                 "up by doing so, and what their existence suggests about the "
                 "order in which the two kinds of respiration appeared on "
                 "Earth.",
            "field_label": "Your answer",
            "placeholder": "They respire anaerobically, which means…",
            "success": [
                "Says they respire anaerobically, breaking glucose down partly "
                "without oxygen.",
                "Says they get far less energy from each glucose molecule than "
                "an aerobic organism would.",
                "Says they must therefore use much more food for the same "
                "amount of work, or live at a low rate of activity.",
                "Says anaerobic respiration must be the older process, because "
                "for a long period early in Earth’s history there was almost no "
                "oxygen in the atmosphere.",
                "Links the appearance of oxygen to photosynthesis — the oxygen "
                "these organisms avoid was put there by other living things.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Aerobic respiration: uses oxygen, glucose broken down "
                "completely, products carbon dioxide and water, far more energy "
                "per glucose. Anaerobic respiration: no oxygen, glucose broken "
                "down partly, lactic acid in humans or ethanol and carbon "
                "dioxide in yeast, much less energy per glucose but supplied "
                "faster. Organisms use both, and which one dominates depends on "
                "how fast energy is needed and whether oxygen can reach the "
                "cell.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B8 flag 20. CHECKED AND LEFT: this BUILDS on b7-04 rather than
    # repeating it — b7-04 tells the oxygen story from the producer's end, this
    # from the respirer's, and three things here appear in no other lesson
    # (obligate anaerobes as living evidence, the extinction itself, and the
    # link from yield to body size). Full reasoning in the docstring.
    #
    # ⚠️ The anchor around "Bacteria in the gut" is stripped and the words stay —
    # "What could not be lifted" 3. The destination is a `references` edge.
    #
    # ⚑ ONE WORD CHANGED: "about". Design's closing clause read "release twenty
    # times more energy" — the one unhedged statement of the figure on a page
    # that hedges it everywhere else, and a fresh assertion rather than a
    # back-reference. Under MRB-225 the claim shrinks until it is true; the
    # traditional 2-vs-38 ATP comparison gives about nineteen. The teaching
    # point — the yield is why anything large exists — is untouched.
    #
    # ⚖️ MRB-225 holds across the layer: it adds a case, retracts nothing above
    # it, and every claim in the body survives it intact.
    "stretch": [
        {"type": "explainer", "id": "the-world-that-came-first",
         "text": "Some organisms have never made the switch. Obligate anaerobes "
                 "are bacteria for which oxygen is toxic, and they are not rare "
                 "curiosities — they live in the mud of a pond, in the deep "
                 "layers of a compost heap, in a cow's rumen and in the "
                 "oxygen-free depths of your own large intestine, where they "
                 "are part of the community you met in Bacteria in the gut. "
                 "Their existence is a fossil of the world they evolved in. For "
                 "roughly the first two billion years of life there was no "
                 "oxygen worth speaking of, so every living thing respired "
                 "anaerobically; when photosynthetic bacteria began filling the "
                 "atmosphere with oxygen, they caused what is arguably the "
                 "largest mass extinction in Earth's history by poisoning "
                 "almost everything alive. The survivors either retreated to "
                 "places the oxygen could not reach, where their descendants "
                 "still are, or found a way to use the poison — and using it "
                 "turned out to release about twenty times more energy, which "
                 "is most of the reason anything larger than a bacterium "
                 "exists."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to test a situation that is not one of the five?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph and nothing in it is a safety instruction — it is a
    # note about how far one figure and five simplified situations can be
    # trusted. Routing it through `safety_note` would print it in the treatment
    # reserved for "never light a candle without an adult". Same resolution as
    # b3-05, b3-07, b4-01, b5-06 and b7-04.
    #
    # ⚑ NOTES-B8 flag 19, site 8 of nine, and it is the honest half: the
    # page telling the student that "about twenty" is a teaching comparison
    # rather than a measurement. Its second sentence is load-bearing in a
    # different way — it is what stops the five cases being read as five pure
    # states, which they are not, and it is the only place the page says that
    # both routes run in every living example.
    "convention_note": "\"About twenty times more energy\" is the usual "
                       "teaching comparison and comes from the ATP yields met "
                       "at GCSE; the exact ratio depends on how the accounting "
                       "is done. The five situations are simplified: in every "
                       "living example both routes are running at once, and the "
                       "labels describe which one is supplying most of the "
                       "energy.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is one criterion applied to five cases and defended in words,
    # and both self-marked rungs ask for a causal chain to be built from
    # evidence — the marathon and the obligate anaerobes are both "what does
    # this observation let you conclude?".
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
