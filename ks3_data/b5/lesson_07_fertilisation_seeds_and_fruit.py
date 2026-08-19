"""B5 L7 — Fertilisation, seeds and fruit (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b5/b5-07-fertilisation-seeds-and-fruit.dc.html` (536 lines), under
the MRB-220 build contract, with the instrument authored against
`r_what_it_becomes` in `build_ks3.py` — see "The instrument" below for which of
the two sources was used and why.

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted", none of which is a
sentence of science. The six before/after rows, the five process steps and all
four ladder rungs came out of `node tools/extract_design_payload.js`, not off a
keyboard.

── `covers` is the SUB-ID, and it is already minted ─────────────────────

`KS3.B.REP.02b` is *"Fertilisation in plants, and seed and fruit formation."*
(`ks3_data/substatements.py`). `a` is `flowers-and-pollination` and `c` is
`seed-dispersal`; §5.7's exactly-once rule would fail the build on any overlap,
and this page is careful about the boundary in both directions — step 01 names
pollination and hands it back to the previous lesson, step 05 names dispersal
and hands it forward to the next one.

── The flagship: the reveal is GATED, and the whole row is the button ────

`#s-becomes` is `what-it-becomes`, on `ks3-block ks3-dark ks3-practical` (page
line 113), so `practical` is MEASURED from Design's own markup rather than
inherited. Six rows, `open: {}` starts EMPTY, and each row's `why` is behind
`<sc-if value="{{ row.open }}">` (page line 144) — so on load a student sees
twelve before/after cells and not one explanation. MRB-208's "nothing is ticked
on load" is satisfied by the same fact: `isDone('s-becomes')` needs six opens.

⚖️ THE ROW IS ONE FULL-WIDTH BUTTON AND THERE IS NO CHEVRON. Page line 131 wraps
the entire three-cell grid in a single `<button>` at `width: 100%`; NOTES-B5
§2.5 says so in terms — *"the whole row is the button, as in `gamete-compare`.
No separate chevron control."* An added chevron would be a second control for
one action and a second tab stop for no gain.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that
`#s-steps` came off the rail. Design draws FOUR stops and `#s-steps` ticks on
`Object.keys(s.open).length >= 6` (page line 394) — the BECOMES predicate,
character for character, one section to the left — and because `#s-steps` is an
eyebrow, a display statement, five static step cards and a key fact, with no
control, no commitment and no field, the reading was that MRB-208's completion
rule ruled it out, that `ks3_parity.check_rail_reachable` would fail a `rule`
section for carrying none of the signals `doneByDom()` reads, and that
inventing a demand Design did not draw is closed to this build. So the lesson
shipped THREE stops.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine. Dropping a stop Design drew is not
rendering what Design drew.

And Design's `isDone()` states the tick condition. It is a rail-level function
and returns the identical expression for `#s-becomes` and then for `#s-steps`.
The five steps are the payoff of the six rows the student just opened; the
section holds no control because `#s-becomes` — whose reveal is gated, above —
already took the commitment. That is a MIRROR, resolved at rail level in
`wireRail`'s `paint()`.

So the fourth stop is declared: anchor `s-steps`, `mirrors: "s-becomes"`,
`done_when: "all_six_rows_opened"` — the BECOMES predicate, named as borrowed,
and gated by `check_rail_matches_design` against `docs/ks3/rail-manifest.md`.
b4-01's `#s-parts`, c1-02's `#s-matrix`, c1-05's `#s-scale`, b3-01's
`#s-nutrients` and b3-02's `#s-limits` are restored the same way. The section
keeps its anchor, as it always did, so the tutor card's `#s-steps` link and
every hash link into it still work.

── What could not be lifted, and why ────────────────────────────────────

1. **The step cards' NUMBER CHIPS, and step 03's promotion.** Design draws
   `#s-steps` as an `<ol>` of five cards, each with an ink `01`–`05` chip, and
   draws card `03` differently from the other four — `--ks3-inset` ground, a 3px
   border instead of 2px, and an ACCENT chip instead of an ink one (page lines
   478–481), because 03 is the only one that is fertilisation. `r_rule` emits a
   `<ul>` on a `repeat(auto-fit, minmax(220px, 1fr))` grid with no slot for a
   numeral and no per-card modifier. Document order is preserved, so the five
   steps still read in order and step 03 still says *"That fusion, and only that
   fusion, is fertilisation"* in its own words; the chips and the promotion are
   DROPPED rather than smuggled into the card text, which is b4-01's ruling on
   the identical component. Reported. This is the larger of the two losses on
   this page, because the section's own statement — *"Five steps, and only one
   of them is fertilisation"* — is what the promotion draws.

2. **The `where` tag is FOLDED into the card term, not dropped.** Design sets it
   in mono accent type on the same baseline as the step's name (`Fertilisation`
   / `Inside an ovule — and nowhere else`), and `r_rule`'s card is two parts. All
   five are DIFFERENT strings and every one of them is science — *"On the stigma
   — this is pollination"* and *"Inside an ovule — and nowhere else"* are the
   whole argument of the section — so dropping them would lose content. They are
   joined to the name with " · ", which is b4-01's and b3-05's precedent and
   Design's own separator elsewhere on the page. Both strings survive
   byte-identical.

3. **The key fact leaves Design's nested panel.** She nests it inside `#s-steps`
   (page lines 171–174); `r_rule` has no nested key-fact slot (only
   `r_comparison` does), so it renders as its own top-level block directly under
   the panel, on the band ground every other top-level key fact in the key stage
   takes. The words are unchanged and the order is unchanged.

4. **The inline link inside `#s-think` is STRIPPED and every word is kept.**
   Design writes *"It is the same distinction you drew in
   <a href="b5-02-gametes-and-fertilisation.html">Gametes and fertilisation</a>
   between a sperm reaching an egg and a sperm fusing with one."* `rich()` allows
   `<em>` and `<strong>` and nothing else, so an authored `<a>` would be escaped
   and a student would read the raw markup. The sentence is lifted whole without
   the anchor, and `b5-02` is carried in `references` so the destination is a
   real link in the end matter rather than a dead one in prose. Same resolution
   as b3-07, b3-08, b4-02, b4-03 and b4-05.

5. **Design draws TWO endmatter link cards; the engine emits one.** Her "Next in
   this unit" (`seed-dispersal`) and "Connects to" (`flowers-and-pollination`,
   `gametes-and-fertilisation`) are one card in `r_endmatter`, headed by
   `connects_heading`. All three links live in it, the forward one first, under
   "Connects to" — b3-01 and b4-01 resolved the identical layout the identical
   way. The heading "Next in this unit" is what is given up; no link is.

6. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

── ⚠️ NOTES-B5 flag 44 BINDS, AND THIS PAGE BREAKS IT SEVEN TIMES ───────

Flag 44 rules teleology out at KS3: b5-08's first Think again attacks *so that*,
*wants* and *tries*, and its rung 3 marks a student down for using them. This
page — same unit, same delivery — is written in purposive language throughout.
Nothing authored here reintroduces it; every instance below is Design's own copy,
lifted byte-identical under MRB-205, and every one is REPORTED rather than
silently repaired:

  1. step 05 — *"depends on how that species **intends** to move its seeds"*.
     The bare verb flag 44 names.
  2. `petals.why` — *"has nothing to gain from further insect visits, **so** the
     petals … are abandoned"*, and the sentence before it, *"The advertising
     budget is cut the moment the sale is made."*
  3. `stamens.why` — *"it is other flowers **they have to reach**"*.
  4. `ovary.why` — *"All of them are ovaries **doing the same job** — protecting
     the seeds and getting them moved."*
  5. the hook prompt — *"the plant **has to** get one of them to the other"*.
  6. the stretch layer — *"a plant that built one for every ovule **would waste**
     most of them"*, and *"a plant's packed lunch for a seedling"*.
  7. rung 2's carrot correction — *"a food store the plant **built for
     itself**"*, and the key note's *"have **done their jobs** and wither"*.

Two of these are the strongest writing on the page (the advertising-budget line
and the packed-lunch line) and one of them, step 05, is a single word away from
compliance. This is Mide's call, not an authoring pass's: the choice is between
flag 44 as ruled and Design's register as drawn, and it has to be the same answer
in b5-07 and b5-08 or the unit teaches a rule it breaks on the facing page.

⚑ For Mide's science gate — NOTES-B5 §3 flags landing on THIS lesson:
  * flag 35 — double fertilisation and endosperm in the stretch layer.
  * flag 36 — *"White flour is very nearly pure endosperm."*
  * flag 37 — pollen tube timing, *"hours in some plants, months in some trees"*.
    Stated three times: hook reveal, first confrontation, and the legal line.
  * flag 38 — the fruit/vegetable confrontation, carrot / potato / celery, and
    the wheat grain as a fruit. Design's own note says the wheat grain is the one
    most likely to be challenged, since the fruit wall is fused to the seed coat.
  * flag 13 — `b5-pollen-tube` is named in Design's legal line and is not in
    `docs/ks3/diagram-manifest.md`. Declared here at `status: "needed"` (§4.10,
    not a build blocker) so it is a tracked sourcing task rather than a dangling
    reference. Nothing is invented to fill it.

⚑ Three design flags of my own, and the page WINS on all three:

  a. **The hook heading gives away the hook's own answer.** The `<h2>` reads *"A
     pollen grain solves the problem by growing a tunnel."*, the rail's label for
     the stop is *"A tunnel"*, and then the commit asks *"So how does the male
     gamete reach the ovule?"* with option B *"The grain grows a tube down
     through the style…"*. A student who has read the heading is not making a
     wager. Law 1 says the hook ends in a commitment and R3 says the wager is
     never marked, so nothing here is a correctness fault — but it is a hook that
     answers itself, and moving one sentence would fix it.

  b. **⊕ RESOLVED — MRB-177 RULED 17 Aug 2026, and rung 1 is repaired.**
     Measured before: the correct option was 11 words against distractors of
     6 / 7 / 7 — nearly twice the longest wrong answer, and the only one naming
     both nuclei.

     Mide ruled the CONSTRUCT rather than the instance: on a recall or apply
     rung the correct answer states a RULE — subject, condition, consequence —
     while the distractors stated one-clause wrong REASONS, so the correct
     answer was longer by construction and a student could score the rung
     without reading it. His three replacement distractors are applied verbatim.
     **The correct option is unchanged, `answer: 1` is unchanged, and the gate's
     threshold is unchanged.** Measured after: 11 against 10 / 9 / 9 — gap 1,
     ratio 1.10, inside both limbs. All three corrections in `feedback` already
     answered the new wording and are byte-identical.

     ⛔ Superseded, kept as history: this flag used to read *"not repairable by
     lift … No distractor was rewritten, because rewriting one means authoring
     science-bearing copy Design did not write, which this build is closed to."*
     That was right — and the copy that repairs it is Mide's, not an author's,
     so the build's closure was never breached. The
     `("fertilisation-seeds-and-fruit", "ladder recall")` entry in
     `verify_ks3.py`'s `KNOWN_TELLS` is now stale; the commander deletes it.

     Rung 2 is untouched and still passes (2 / 2 / 2 / 4, correct is 2).

  c. **`becomeProgress` counts opens, and an open row can be shut again.** Page
     line 468 reads `Object.keys(s.open).length + ' of 6 opened'` while
     `row.open` is a TOGGLE (line 473) — a key stays in `s.open` after the row is
     closed, so a student who opens six and shuts them all still reads "6 of 6
     opened" over six collapsed rows, and the stop stays ticked. That is the
     kinder behaviour of the two and it matches MRB-208 (completion, not current
     state), so it is left exactly as drawn. Recorded because it will look like a
     bug to whoever reads the counter next.

── The instrument: which source was used ────────────────────────────────

⚠️ `docs/ks3/b5-inventory/PAYLOAD-SCHEMA.md` DID NOT EXIST when this module was
written, and neither did `r_what_it_becomes` — `grep` found the kind registered
in `ks3_data/b5/__init__.py::_INSTRUMENT_SEGMENTS` and nowhere else in
`build_ks3.py`, `shared/ks3.js` or `shared/ks3.css`. So the payload below is
authored against **NOTES-B5 §2.5's declared payload** — `{rows: [{id, name,
before, after, why}], open: {}}` — widened with the shell keys `r_activity`
already reads (`eyebrow`, `heading`, `head_counter`, `prompt`) and a `table`
map for the three column headings, on the exact precedent of `r_gas_compare`,
where `table` supplies both the header row and the per-cell captions that
replace it below the stack breakpoint. Design needs that map here for the same
reason: `[data-cmp-head]` hides under 880px and `[data-cmp-cap]` appears in its
place (page lines 24–28), so an uncaptioned "A seed" would be a cell with
nothing saying which column it came from.

If the engine pass's schema names these keys differently, this is the one place
in the module to change and the strings themselves do not move.
"""

# ── the six before/after rows (page lines 320–333, via extract_design_payload.js)
#
# Document order is Design's and it is not alphabetical or structural: the three
# parts that BECOME something come first (ovule → seed, ovary → fruit, fused
# nuclei → embryo), then the two that go, then the one that stays. The argument
# of the section is in that order.
BECOMES = [
    {"id": "ovule", "name": "Ovule",
     "before": "A tiny structure inside the ovary, holding one female gamete "
               "nucleus",
     "after": "A seed",
     "why": "One ovule becomes one seed, which is why counting the seeds in a "
            "fruit counts the ovules that were fertilised. The seed contains "
            "an embryo plant, a food store, and a tough coat around both."},
    {"id": "ovary", "name": "Ovary",
     "before": "A chamber at the base of the carpel containing the ovules",
     "after": "The fruit",
     "why": "It swells, and what it swells into depends on the species: fleshy "
            "in a tomato or a plum, dry and papery in a pea pod, hard in a "
            "hazelnut. All of them are ovaries doing the same job — protecting "
            "the seeds and getting them moved."},
    {"id": "zygote", "name": "The fused nuclei",
     "before": "One nucleus from the pollen, one from the ovule",
     "after": "The embryo plant",
     "why": "This is the fertilised cell, and it divides to become a miniature "
            "plant with the beginnings of a root and a shoot, folded up inside "
            "the seed and waiting. It is the only part of all this that is "
            "genuinely new."},
    {"id": "petals", "name": "Petals",
     "before": "Coloured, scented, advertising for visitors",
     "after": "Wither and fall",
     "why": "The advertising budget is cut the moment the sale is made. A "
            "flower whose ovules are fertilised has nothing to gain from "
            "further insect visits, so the petals — which were expensive to "
            "build — are abandoned."},
    {"id": "stamens", "name": "Stamens",
     "before": "Anthers making and releasing pollen",
     "after": "Wither and fall",
     "why": "Same reasoning. The male parts of this flower have already sent "
            "their pollen out into the world, and it is other flowers they "
            "have to reach, not this one."},
    {"id": "sepals", "name": "Sepals",
     "before": "Green flaps enclosing the bud",
     "after": "Often stay, sometimes hardly change",
     "why": "Look at the top of a strawberry or a tomato: that little green "
            "star is the sepals, still there long after everything else has "
            "gone. They protected the bud and in many species they go on "
            "protecting the fruit."},
]

# ── the five steps of the process (page lines 335–346) ───────────────────
#
# Design's `where` is joined to `name` with " · " — see "What could not be
# lifted" 2. The `what` prose is untouched. The `num` chips and step 03's
# accent promotion are dropped — see "What could not be lifted" 1.
STEPS = [
    ("Pollen lands", "On the stigma — this is pollination",
     "A grain arrives, carried by an insect or the wind. If it is the wrong "
     "species the stigma usually does not respond at all; if it is the right "
     "one, the grain begins to grow."),
    ("The pollen tube grows", "Down through the style",
     "The grain extends a single tube down through the tissue of the style "
     "towards the ovary, digesting its way through as it goes. The male gamete "
     "nucleus travels down inside it."),
    ("Fertilisation", "Inside an ovule — and nowhere else",
     "The tube reaches an ovule and the male gamete nucleus fuses with the "
     "female gamete nucleus. That fusion, and only that fusion, is "
     "fertilisation. Every ovule that is going to become a seed needs its own "
     "pollen tube."),
    ("Seeds form", "From the fertilised ovules",
     "Each fertilised ovule becomes a seed: an embryo plant, a store of food "
     "to start it off, and a tough coat around both. The seed can survive "
     "conditions that would kill the parent plant."),
    ("The fruit forms", "From the ovary around them",
     "The ovary wall swells and becomes the fruit, and the rest of the flower "
     "withers away. Whether it ends up fleshy, dry, hooked or winged depends "
     "on how that species intends to move its seeds — which is the next "
     "lesson."),
]

STEP_CARDS = [{"term": "%s · %s" % (name, where), "gloss": what}
              for name, where, what in STEPS]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 128 character for character.
    "slug":        "fertilisation-seeds-and-fruit",
    "title":       "Fertilisation, seeds and fruit",
    "discipline":  "biology",
    "unit":        "reproduction",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # The `b` clause of the split bullet — fertilisation in plants, and seed and
    # fruit formation. `a` is flowers-and-pollination; `c` is seed-dispersal.
    "covers":      ["KS3.B.REP.02b"],
    # Named but not taught: step 01 hands pollination back to REP.02a, step 05
    # hands dispersal forward to REP.02c, and the first confrontation settles
    # itself by appeal to the animal case (REP.01b).
    "touches":     ["KS3.B.REP.02a", "KS3.B.REP.02c", "KS3.B.REP.01b"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 1},
                    {"id": "structure-function", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 50,

    # ── progression edges ───────────────────────────────────────────────────
    # No `requires`: Design draws no "Before this lesson" card, and the engine
    # omits an empty one rather than printing a promise the lesson did not make.
    # All three of her forward and sideways links live in the middle card — see
    # "What could not be lifted" 5. `gametes-and-fertilisation` is also the
    # destination of the stripped inline link in `#s-think` (item 4).
    "requires":    [],
    "assumes":     [],
    "references":  ["seed-dispersal",
                    "flowers-and-pollination",
                    "gametes-and-fertilisation"],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Seed structure and germination, plant hormones, and the "
                   "genetics of self- and cross-fertilisation.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Pollen has landed. The two gametes are still several "
                    "centimetres apart, and neither of them can move.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-steps` is the third: no control of
    # its own, so it mirrors `s-becomes` and ticks on that section's predicate
    # — see the docstring. `short` and `label` are Design's own `RAIL_SHORT`
    # and `RAIL` strings (page lines 312–318).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "A tunnel",
         "done_when": "committed"},
        # Design's own threshold, kept: the stage ticks when all six rows have
        # been opened, not on the first one. A stop that ticked on one open
        # would call a six-row instrument finished at a sixth of it.
        {"anchor": "s-becomes", "short": "BECOMES", "label": "What it becomes",
         "done_when": "all_six_rows_opened"},
        {"anchor": "s-steps", "short": "STEPS", "label": "Five steps",
         "mirrors": "s-becomes", "done_when": "all_six_rows_opened"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3). Option D is
    # REPRO-14 offered as one of the four, which is what makes the hook elicit
    # it. See design flag (a) in the docstring: the heading above these options
    # already names the tunnel.
    "phenomenon": {
        "kind": "narrative",
        "title": "A pollen grain solves the problem by growing a tunnel.",
        "prompt": "There is no sperm here, nothing swims, and nothing is "
                  "carried. The gametes are at opposite ends of a solid stalk "
                  "of plant tissue, and the plant has to get one of them to "
                  "the other.",
        "commit": "So how does the male gamete reach the ovule?",
        "options": [
            "The stigma absorbs it and passes it down to the ovary",
            "The grain grows a tube down through the style, and the nucleus "
            "travels along it",
            "Rain washes it down the inside of the style",
            "It does not need to — fertilisation happens on the stigma",
        ],
        "reveal": "The grain grows. Once it lands on a stigma of the right "
                  "species it puts out a pollen tube — a single cell extending "
                  "down through the tissue of the style, digesting its way "
                  "towards an ovary it cannot see — and the male gamete "
                  "nucleus travels down inside it. The journey takes hours in "
                  "some plants and months in others. Only when the tube "
                  "reaches an ovule does anything fuse, and that is the moment "
                  "this lesson is about.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ The `REPRO` family is NOT yet in `docs/ks3/misconception-register.md` —
    # NOTES-B5 §5 mints seventeen for this unit and the commander maintains the
    # register centrally. IDs here are the ones PRE-ALLOCATED to this lesson by
    # the commander (MRB-244), because five parallel authors collided on B4's
    # family and B5 has eight.
    #
    # ⚠️ THE NUMBERING RUNS AGAINST PAGE ORDER, DELIBERATELY. Design draws
    # "Pollination and fertilisation are the same thing" FIRST and "A tomato is
    # a vegetable" second, but NOTES-B5 §5 pins the first of those to REPRO-14
    # by name — *"Pollination and fertilisation are the same thing → REPRO-14,
    # owned by fertilisation-seeds-and-fruit"* — so the tomato takes REPRO-13.
    # Renumbering to match reading order would break the one entry Design's own
    # notes name. Register order is not page order and never was.
    #
    # ⚠️ THERE IS NO THIRD BELIEF ON THIS PAGE, so REPRO-23 IS NOT USED. The
    # commander pre-allocated it against a third; `#s-think` carries exactly two
    # `ks3-mis-quote` lines (page lines 182 and 186) and nothing elsewhere on the
    # page states a belief in the student's voice. REPRO-23 is returned unspent
    # and is free for whoever needs it.
    #
    # `elicited_by` is honest per entry. REPRO-14 really is surfaced before it is
    # killed: hook option D *is* the belief, and the student commits to one of
    # the four before the reveal opens. `s-hook` is the anchor rather than an
    # activity id because the hook HAS no activity id — it is a `core` block with
    # a `ref`, and the anchor is the only stable name it has, which is the same
    # argument `_normalise()` makes for an inline instrument. REPRO-13 is not
    # asked for anywhere before the block that kills it, so the block is named
    # for both; b3-04's `think-balanced` and b4-01 are the same pattern.
    "misconceptions": [
        {"id": "REPRO-14",
         "statement": "Pollination and fertilisation are the same thing.",
         "elicited_by": "s-hook",
         "confronted_by": "two-wrong-ideas"},
        {"id": "REPRO-13",
         "statement": "A tomato is a vegetable.",
         "elicited_by": "two-wrong-ideas",
         "confronted_by": "two-wrong-ideas"},
    ],

    # Design draws no keyword block anywhere in B5, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list — which matters here,
    # because "stigma", "style", "ovule", "carpel" and "endosperm" would
    # otherwise all count against the page.
    #
    # ⚠️ Every definition below is AUTHORED, not lifted, and every one is written
    # against NOTES-B5 flag 44: a structure has consequences, not intentions.
    # There is no "so that", no "in order to", and no verb of wanting or trying
    # anywhere in this list. Design's own copy does not hold that line — see the
    # flag 44 section of the docstring — but nothing added by this pass loosens
    # it further.
    "vocabulary": [
        {"term": "pollination",
         "definition": "The transfer of pollen from an anther to a stigma.",
         "note": "Delivery only. Nothing has fused at this point."},
        {"term": "fertilisation",
         "definition": "The fusion of a male gamete nucleus with a female "
                       "gamete nucleus.",
         "note": "In a flowering plant it happens inside an ovule."},
        {"term": "pollen tube",
         "definition": "A single cell that the pollen grain extends down "
                       "through the style, with the male gamete nucleus "
                       "inside it.",
         "note": "One tube per ovule fertilised."},
        {"term": "style",
         "definition": "The stalk of tissue between the stigma and the ovary.",
         "note": None},
        {"term": "ovule",
         "definition": "A structure inside the ovary containing one female "
                       "gamete nucleus.",
         "note": "One fertilised ovule becomes one seed."},
        {"term": "ovary",
         "definition": "The chamber at the base of the carpel that contains "
                       "the ovules.",
         "note": "After fertilisation it becomes the fruit."},
        {"term": "seed",
         "definition": "An embryo plant and a food store, inside a tough coat.",
         "note": None},
        {"term": "fruit",
         "definition": "The structure that develops from the ovary of a "
                       "flower, containing the seeds.",
         "note": "A biological definition. It says nothing about sweetness."},
        {"term": "endosperm",
         "definition": "The food store tissue inside the seed of a flowering "
                       "plant.",
         "note": "Most of a grain of wheat, and nearly all of white flour."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # Design's legal line names ONE slot on this page and no artwork exists for
    # it, so it is DECLARED at `needed` rather than dropped: the manifest is
    # generated from this field, which turns a dangling reference into a tracked
    # sourcing task. `needed` is not a build blocker. No `figure` block is added
    # to `core` — Design draws no figure slot on the page, and one here would be
    # a component nobody drew. The caption is authored and describes only what
    # this lesson teaches, in the order the five steps take.
    "figures": [
        {"id": "b5-pollen-tube",
         "kind": "diagram",
         "caption": "A pollen grain on the stigma, the pollen tube extending "
                    "down through the style, and the male gamete nucleus "
                    "reaching an ovule inside the ovary.",
         "status": "needed"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-becomes — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b5/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 113), so the segment is measured and not inherited.
        {"type": "what-it-becomes", "id": "what-each-part-turns-into",
         "anchor": "s-becomes",
         "demand": "investigate",
         "eyebrow": "Before and after · six parts",
         "heading": "What each part turns into",
         "head_counter": {"format": "{n} of 6 opened", "total": 6},
         "prompt": "A fertilised flower does not build a fruit from nothing — "
                   "it converts the parts it already has. Tap a row to see why.",

         "rows": BECOMES,

         # ⚖️ THE REVEAL IS GATED AND NOTHING IS OPEN ON LOAD. `open: {}` starts
         # empty on Design's page and each `why` sits behind `row.open`; the row
         # itself is the only control, at full width, with no chevron beside it.
         # See the docstring.
         "table": {"name": "Part of the flower",
                   "before": "Before",
                   "after": "After fertilisation"}},

        # #s-steps — the band panel. Rail stop 3, mirroring `s-becomes`; see
        # the docstring. `rule` is the component: band ground, 3px ink border, an accent-text
        # eyebrow and a display statement, then a card list — Design's markup
        # (page lines 152–169) minus the number chips and step 03's promotion.
        {"type": "rule", "anchor": "s-steps",
         "eyebrow": "The process, in order",
         "statement": "Five steps, and only one of them is fertilisation.",
         "cards": STEP_CARDS},

        # Design nests this inside `#s-steps`; `r_rule` has no nested slot, so it
        # renders directly under the panel in document order. See "What could not
        # be lifted" 3.
        {"type": "key-fact", "ref": "delivery-then-fusion"},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "REPRO-14"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "delivery-then-fusion",
         "text": "Pollination is delivery to the stigma. Fertilisation is "
                 "fusion at the ovule, later, at the bottom of a tube the "
                 "pollen grain had to grow. A fertilised ovule becomes a seed "
                 "and the ovary around it becomes the fruit.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`, and an authored statement wins over the register. The
        # block asks for no commitment, on Design's page and here, so it is not a
        # rail stop and emits no completion contract.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "REPRO-14",
         "statements": [
             {"quote": "Pollination and fertilisation are the same thing.",
              # ⚠️ Design's inline link to `Gametes and fertilisation` is dropped
              # and every word is kept; see "What could not be lifted" 4.
              "body": ["They are separated by a distance, a delay and a "
                       "definition — and this is the single most common error "
                       "in the whole of plant reproduction. Pollination is "
                       "transport: a grain of pollen arrives on a stigma. "
                       "Nothing has joined, nothing is fertilised, and the "
                       "plant may still end up with no seeds at all. "
                       "Fertilisation is the fusion of the pollen's gamete "
                       "nucleus with the ovule's, which happens somewhere else "
                       "entirely — down inside the ovary — after the grain has "
                       "grown a tube the whole length of the style to get "
                       "there. Hours later in some species; in an oak, months. "
                       "It is the same distinction you drew in Gametes and "
                       "fertilisation between a sperm reaching an egg and a "
                       "sperm fusing with one. Arriving is not fusing, in an "
                       "animal or in a plant."]},
             {"quote": "A tomato is a vegetable.",
              "body": ["In a kitchen, certainly. In biology the word "
                       "<em>fruit</em> has a definition and it has nothing "
                       "to do with sweetness: a fruit is the structure that "
                       "develops from the ovary of a flower, and it "
                       "contains the seeds. Cut anything open and the seeds "
                       "settle it. Tomatoes, cucumbers, peppers, "
                       "courgettes, pea pods, aubergines and — the one that "
                       "surprises everybody — the tough case around a grain "
                       "of wheat are all fruits. Carrots are roots, "
                       "potatoes are underground stems, celery is a leaf "
                       "stalk, and none of those has ever been near an "
                       "ovary. <em>Vegetable</em> is a culinary word "
                       "covering any plant part we happen to eat savoury; "
                       "it draws no biological line at all. This is worth "
                       "having straight for a reason beyond winning an "
                       "argument: once you know a fruit is a converted "
                       "ovary, you can look at any one and read backwards "
                       "to the flower it used to be."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026, AND RUNG 1 IS REPAIRED.
    #   rung 1: correct 11w against distractors of 10 / 9 / 9. The three
    #           distractors are Mide's own replacement copy, applied verbatim;
    #           the correct option, `answer: 1` and the gate's threshold are all
    #           unchanged. See design flag (b) in the docstring for the ruling.
    #   rung 2: correct 2w against distractors of 2 / 2 / 4 — passes, untouched.
    #
    # ⛔ Superseded, kept: this block used to read "MEASURED, AND RUNG 1 FAILS …
    # NOT repaired: rewriting a distractor means authoring science-bearing copy
    # Design did not write. Flagged for Mide." It was flagged; he ruled, and the
    # copy is his.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Define it precisely",
            "q": "In a flowering plant, which of these is fertilisation?",
            "options": [
                "A pollen grain landing on the stigma of the flower",
                "A pollen nucleus fusing with an ovule nucleus inside the "
                "ovary",
                "The ovary swelling and ripening to become a fruit",
                "A seed being carried away and starting to grow",
            ],
            "answer": 1,
            "feedback": {
                0: "That is pollination — delivery to the front door. The "
                   "gametes are still centimetres apart.",
                2: "That happens because fertilisation has already occurred. "
                   "Effect, not event.",
                3: "That is dispersal and germination, both much later, and "
                   "both possible only because fertilisation happened first.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Which of these is a fruit, biologically?",
            "options": [
                "A carrot",
                "A tomato",
                "A potato",
                "A stick of celery",
            ],
            "answer": 1,
            "feedback": {
                0: "A root. It is a food store the plant built for itself, and "
                   "it has never been part of a flower.",
                2: "An underground stem — a tuber. The eyes on it are buds, "
                   "which is why a potato can sprout.",
                3: "A leaf stalk. Follow it up and you find the leaf still "
                   "attached at the top.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the sequence",
            "q": "Describe what happens from a pollen grain landing on a "
                 "stigma to a fruit forming. Make clear which single step is "
                 "fertilisation, and say what the ovule and the ovary each "
                 "become.",
            "field_label": "Your explanation",
            "placeholder": "The pollen grain lands on the stigma and…",
            "success": [
                "Says the pollen grain grows a pollen tube down through the "
                "style.",
                "Says the male gamete nucleus travels down the tube to an "
                "ovule.",
                "Identifies fertilisation as the fusion of the two nuclei, "
                "inside the ovule.",
                "Says the fertilised ovule becomes a seed containing an embryo "
                "and a food store.",
                "Says the ovary becomes the fruit, and that the petals and "
                "stamens wither.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A gardener pinches off every flower on a tomato plant as "
                 "soon as it opens, to keep the plant tidy. Explain why they "
                 "will get no tomatoes, using the words pollination, "
                 "fertilisation, ovule and ovary.",
            "field_label": "Your answer",
            "placeholder": "Removing the flower removes…",
            "success": [
                "Says removing the flower removes the ovary, and the fruit can "
                "only develop from an ovary.",
                "Says pollen never reaches the stigma, so pollination cannot "
                "happen.",
                "Says without fertilisation the ovules do not become seeds.",
                "Concludes that a tomato is a converted ovary, so no flower "
                "means no tomato.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "After pollination, the pollen grain grows a pollen tube down "
                "through the style to an ovule. The male gamete nucleus "
                "travels down the tube and fuses with the female gamete "
                "nucleus inside the ovule: that fusion is fertilisation. The "
                "fertilised ovule becomes a seed containing an embryo plant "
                "and a food store, inside a tough coat. The ovary around it "
                "becomes the fruit. Petals, stamens and stigma have done their "
                "jobs and wither.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # NOTES-B5 flags 35 and 36 land here: double fertilisation, endosperm, and
    # white flour. Lifted whole.
    "stretch": [
        {"type": "explainer", "id": "fertilised-twice",
         "text": "Flowering plants fertilise twice, with the same pollen tube. "
                 "Two nuclei travel down it: one fuses with the egg nucleus "
                 "and becomes the embryo, and the second fuses with other "
                 "nuclei in the ovule to make a tissue called endosperm — the "
                 "seed's food store. Nothing else on Earth does this, and it "
                 "solves an accounting problem elegantly. A food store is "
                 "expensive, so a plant that built one for every ovule would "
                 "waste most of them; here the store is only started once "
                 "fertilisation has actually happened, and an unfertilised "
                 "ovule costs almost nothing. Then consider what that tissue "
                 "is. A grain of wheat, rice, maize, barley or oats is mostly "
                 "endosperm; white flour is very nearly pure endosperm with "
                 "the embryo and the coat milled away. Most of the calories "
                 "eaten by most people who have ever lived have been a plant's "
                 "packed lunch for a seedling, redirected — and none of it "
                 "would have been made at all if a pollen tube had not "
                 "arrived."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check the difference between pollination and "
                      "fertilisation?",
              "cta": "Ask about this lesson",
              "anchor": "s-steps"},

    # ⊕ MRB-228's `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph here and nothing in it is a safety instruction — it
    # is a note about how variable the timings on this page are, and a
    # declaration about a figure that has not been drawn yet. Routing it through
    # `safety_note` would print it in the treatment reserved for "never light a
    # candle without an adult", which devalues the safety line. b3-05, b3-07 and
    # b4-01 resolve the identical foot line the identical way.
    #
    # ⚠️ The figure id keeps its plain text; Design sets it in mono inside the
    # sentence and a foot line is escaped, so the id renders in body copy and the
    # words are unchanged.
    # ⊕ MRB-257 · C4 / audit 4.6 — the "… is declared in the lesson record
    # as `b5-…`, awaiting illustration" sentence was our own build metadata,
    # printed to a student on eleven pages (§8.10). Cut. The measurement
    # caveat before it is the part that was doing work and it stays.
    "convention_note": "Timings vary enormously between species: a pollen "
                       "tube may reach the ovule in a few hours or, in some "
                       "trees, after several months.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # A judgement, and the weaker of the record's calls: nothing on this page is
    # measured, so `measurement` and `experimental-skills` are both out, and the
    # instrument reveals rather than investigates. What the lesson actually
    # trains is reasoning backwards from a structure to its origin — "you can
    # look at any one and read backwards to the flower it used to be" — and rungs
    # 3 and 4 are both reasoned explanations applied to a case the page has not
    # answered. That is `analysis-and-evaluation`.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
