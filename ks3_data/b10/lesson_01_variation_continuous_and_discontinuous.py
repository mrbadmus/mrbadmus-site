"""B10 L1 — Variation: continuous and discontinuous (INVESTIGATION).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b10/b10-01-variation-continuous-and-discontinuous.dc.html`
(590 lines), her author's notes `docs/ks3/design-reference/b10/NOTES-B10.md`, and
the B10 payload schema `docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md` §0, §1, §2, §7,
§8, §9, §10, §11, §12, §13, §14, §15 and §16, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the two listed under "What could not be lifted". The six characteristics,
the four cards, both marked rungs and both self-marked rungs came out of the
page's own `CHARS`, `KIND_CARDS`, `RUNGS` and `SELF_RUNGS` arrays via
`tools/extract_design_payload.js`, not off a keyboard. No option, criterion or
bin figure was retyped.

── `covers` is one clause and this lesson owns the whole of it ─────────

`KS3.B.INH.04` reads, in full: *the variation between individuals within a
species being continuous or discontinuous, to include measurement and graphical
representation of variation*. The clause has three parts and the page has three
answers — `#s-hook` and `#s-two` give the distinction, `#s-bench` gives the
graphical representation by making the student commit to a shape and then draw
it, and the measurement is the sixty-student data set every bin is counted from.
It is not sub-split in `ks3_data/substatements.py`, so it is owned whole and
`build_ks3.validate()` enforces exactly-once ownership: INH.01 is b10-04's,
INH.02a and b are b10-02's and b10-03's, INH.03 is b10-05's.

── ⚖️ THE TEACHING POINT IS THAT THERE ARE TWO QUESTIONS, NOT ONE ──────

From the KEY FACT, which is schema §13 verbatim: **whether variation is
continuous is a question about the DATA; what caused it — genes, environment or
both — is a SEPARATE question with a separate answer.** That split is the whole
lesson and it is drawn six times over:

  * the band section is titled *What shape is it, and what caused it.* and its
    four cards are labelled *Question one · shape* twice and *Question two ·
    cause* twice;
  * every characteristic on the bench carries `shape` AND `cause` as two
    separate authored fields, printed either side of a rule with a bold
    lead-in — `r_variation_plotter` refuses a characteristic missing either,
    and its docstring says a renderer that merged them would delete the lesson;
  * the hook's reveal ends *it says nothing yet about what causes the
    variation*;
  * `GENE-01` IS the conflation of the two, and rung 2 marks it.

⛔ **No authored comment, bench verdict or ladder correction in this file blurs
the two.** The bench verdict tag judges the PREDICTION about shape and says
nothing about cause; the cause line is printed under a rule, unmarked, as
information. Height is the counter-example that holds the whole thing together —
continuous AND strongly inherited — and it is `characteristics[0]`, the tab the
page opens on, deliberately.

── The instrument: a bar gap that is DERIVED and must never be authored ─

`#s-bench` is `variation-plotter`, on `ks3-block ks3-dark ks3-practical` (page
line 105), so `practical` is MEASURED from Design's own class attribute rather
than inferred from the kind name — schema §0 rule 2, and contract §4 records
that B1 got two of six wrong by inferring it.

⚖️ **THE GAP BETWEEN THE BARS IS A PURE FUNCTION OF `data_type`.** Design
computes `gap = kind === 'continuous' ? '0px' : '6px'` once per selected
characteristic and gives every bar `width: calc(100% - gap)` in an equal-width
flex column, so continuous bars TOUCH and discontinuous bars STAND APART. The
histogram/bar-chart convention is therefore taught by the rendering, and schema
§2 is explicit that it must not be overridable: **there is no `gap` key, no
`spacing` key and no `chart_type` key in this record**, because an authored one
would let blood group ship with touching bars. `data_type` is carried once and
decides three things at a stroke — the gap, the display-weight verdict line, and
whether the prediction was right.

⚖️ **THE STUDENT CANNOT SEE THE GRAPH BEFORE COMMITTING TO A SHAPE.** The plot
button ships `disabled` and stays disabled until a prediction exists for the
current characteristic. Six characteristics, one prediction each, no re-run, and
**no reset** — schema §2, measured. `reset_label` is therefore NOT authored: a
key with no read site is a dead key under contract R5, and a reset button would
be a control Design did not draw.

⛔ **NO RUNTIME STATE IS AUTHORED** (schema §0 rule 3). Design's state bag holds
`char`, `predicts` and `plotted`; all three are the runtime's. Nor is an opening
selection authored: schema §0 rule 3's exception is for an opening selection
that is NOT first in its list, and `height` IS `characteristics[0]`, so the
renderer's default of index 0 already ships Design's page. b10-02, b10-03 and
b10-04 each author one because theirs are not first.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ────────────────

Design draws four (page lines 322–327) and her `isDone()` gives `s-two` the
BENCH's predicate, character for character, one section to the left:

    if (id === 's-bench') return n >= 3;
    if (id === 's-two') return n >= 3;          // page lines 417–418

`#s-two` is an eyebrow, a display statement, four static cards and a key fact:
no control, no commitment, no field, no reveal. It is the PAYOFF of the bench
beside it and carries no control precisely because the bench has already taken
the student's commitment. That relationship is a MIRROR, `wireRail`'s `paint()`
resolves it at rail level — which is the level Design computes it at — and
`ks3_parity.check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`, whose row for this page reads
`s-hook s-bench s-two s-ladder | s-two=s-bench`.

⚠️ Schema §8's struck paragraph — *author three stops and drop the band* — is
REVERSED at the head of the same section. Four is what Design drew and four is
what ships. Shipping three fails the build.

⚖️ **THREE PLOTTED IS DESIGN'S OWN THRESHOLD AND IT IS READ TWICE**, once for
the bench and once for the mirror. `build_ks3._B10_VP_THRESHOLD` holds it, and
`r_variation_plotter` refuses a bench with fewer than three characteristics
because that would ship two rail stops no student could ever tick. Three of six
is also the point at which a student has necessarily met both data types.

`#s-think` and `#s-keynote` are on no rail, and that is Design's too:
`#s-keynote` asks nothing, and `#s-think` here is static markup — two quotes,
two bodies, no options, no reveal, no button — so it is a `confrontation` and
not contract R1's `predict`. Schema §9, measured on all five pages.

── What could not be lifted byte-identical, and why ────────────────────

1. **`b9-06` in rung 4's question.** Design writes *"…how you would avoid the
   sampling problem you met in b9-06."* A student cannot resolve a slot code,
   and printing one is exactly the platform leakage §8.10 exists to stop.
   Resolved to the lesson TITLE, the way b9-01 resolved the identical shape:

       Design:  the sampling problem you met in b9-06
       Built:   the sampling problem you met in Sampling an ecosystem

   The destination is not lost — `sampling-an-ecosystem` is Design's own first
   *Before this lesson* card and is carried in `requires`.

2. **A `\\u2014` ESCAPE THAT LEAKED INTO THE MARKUP.** Page line 129 prints the
   predict label as `Before you plot it \\u2014 which shape do you expect?` —
   a literal backslash-u-2014 in the HTML body, not in the script block. Every
   other em dash in this page's markup is the character itself (the key fact,
   the keynote, the stretch layer), and every `\\u2014` inside the `<script>` is
   an ordinary JS escape that resolves. This one resolves to nothing: a browser
   would print the six characters. Authored as the em dash Design meant, which
   is what the two predict BUTTONS beside it already carry. **Reported as a
   defect in the delivered page rather than fixed silently.**

── ⊕ MRB-177 LENGTH PARITY — BOTH MARKED RUNGS CLEAN AS DRAWN ──────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags
a correct option that is strictly the longest AND clears the longest distractor
by ≥4 words or by ≥1.4×.

    rung 1  correct 5w vs 2 / 2 / 7   — not strictly longest      ✓ as drawn
    rung 2  correct 11w vs 11 / 7 / 10  — TIED, not strictly longest ✓ as drawn

**NO OPTION ON THIS PAGE WAS TOUCHED. No correct option was shortened, no answer
index moved, no correction edited, and no distractor padded.** Both rungs pass on
their construct rather than on a repair, and the construct is worth recording
because it is the one MRB-177 asked for:

  * **Rung 1** asks which characteristic is discontinuous, so all four options
    are NAMES of characteristics — two to seven words each. There is no rule
    stated anywhere in the option set, so there is nothing for a rule to be
    longer than, and the longest option on the rung is a DISTRACTOR.
  * **Rung 2** is the rung MRB-177 usually trips, and it does not trip here
    because Design wrote all four options as answers to the same question in the
    same grammar — three of them beginning *That…* and stating a wrong cause,
    the correct one refusing the question. Correct and distractor A are the same
    length to the word, which is the cleanest possible outcome: a student who
    counts words learns nothing in either direction.

── Misconception ids: GENE-01 and GENE-02, and GENE-11 is UNUSED ───────

Schema §12's pre-allocation for b10-01, and the two beliefs Design's `#s-think`
quotes, in her page order. Both statements are her own bytes (page lines 192 and
196), in register voice with the curly quotes stripped — the renderer draws
those.

**Two beliefs were found and two ids were used. `GENE-11`, this lesson's named
spare, is UNCLAIMED and stays permanently unused**, exactly like `DRUG-07`. It
is never re-pointed at a different belief in a later pass.

⊕ **THE `GENE` PREFIX ROW IS OPEN, AND IT AGREES WITH THIS FILE.** It was not
there when this pass started — NOTES-B10 §4 claims its entries were "written
into" the register and schema §12 records that four separate deliveries have
claimed that and none of them did it, so it was checked rather than assumed.
It was opened by the register pass DURING this run, and re-checked at the end
for that reason: that file is in flight this session and is not this pass's to
edit (contract §0). Its `GENE-01` and `GENE-02` rows match the two authored
here on statement, on `elicited_by` and on `confronted_by` — including the
split that puts `GENE-02`'s elicitation at `s-hook` rather than at the ladder —
arrived at independently, with neither pass able to see the other. Nothing to
reconcile. No gate resolves an id against the register, so the lesson would
build either way; what the agreement buys is that the register is now true.

Both `confronted_by` values are `s-think` and both resolve against the BUILT
page (MRB-244). The two `elicited_by` values are deliberately DIFFERENT, because
the two beliefs are offered as commitments in two different places:

  * `GENE-01` → `s-ladder`. Rung 2 option A — *That it is caused by the
    environment rather than by genes* — is the belief in the student's own words,
    it is the answer to a question whose stem hands them the shape and asks for
    the cause, and the ladder is the only place on the page where it is MARKED.
  * `GENE-02` → `s-hook`. Hook option B — *Whether you can measure it with an
    instrument* — is that belief exactly, and the hook is the only place it is
    offered as something to commit to. Rung 1 cannot elicit it: all three of its
    distractors are ruler-measurable AND continuous, so a student holding the
    belief is led to the right answer by it. **A belief that is confronted but
    never elicited is a belief a student never notices they hold**, and this page
    does elicit it — one section earlier than the ladder.

── Keys this pass authors that the RENDERER reads (contract R5) ────────

Named explicitly rather than left to be discovered. Every one is measured off
`r_variation_plotter` and its head-row derivation:

    options_label     the mono label over the six tabs
    characteristics   tabs + one panel each, every panel in the document,
                      each carrying `data_type` (the gap), `axis`, `bins`,
                      `shape` and `cause`
    predict_label     the ask above the two prediction buttons
    predict_options   their ids ARE the two data types and are compared
                      against `data_type` to decide the verdict
    kind_lines        the display-weight line that NAMES the shape
    run_label /       the plot button before and after
    run_done_label
    verdicts          the mono tag, and the only thing on the bench that
                      judges the prediction (schema §0.6)
    progress_suffix   → `_KIND_HEAD_FROM["variation-plotter"]`, composed into
                      `{n} of {total} plotted`; the denominator comes from
                      `_KIND_HEAD_TOTAL`, which counts the characteristics
    eyebrow /         the practical shell's head row
    heading / prompt

⚠️ **THIS INSTRUMENT IS ON INK.** `.ks3-dark p` is (0,1,1) and beats a bare
component class at (0,1,0), so every colour rule for it is written at (0,2,0)
under `.ks3-dark …` and `ks3_parity.check_dark_text_specificity()` resolves it
on the real cascade. Recorded here because this payload is what feeds it.

── The forward reference from b9-06, resolved ─────────────────────────

`ks3_data/b9/lesson_06_sampling_an_ecosystem.py` carries
`{"unit": "B10", "lesson": "variation-continuous-and-discontinuous"}` in
`references` — authored as a reference rather than a `requires` precisely so
that it could ship before this lesson existed, since an unknown `requires`
target fails the build while an unbuilt reference renders as a coming-soon line.
**This record landing resolves it, and nothing in b9-06 changes.** The edge is
reciprocated here as a `requires`, which is Design's own first *Before this
lesson* card, and rung 4 is what makes it real: it asks for a sampling plan.

This lesson makes the same forward bet one unit on. `variation-and-competitive-
success` is b11-01 and B11 is not yet built, so it is carried in `references`
with its unit — `{"unit": "B11", …}` — and renders as coming-soon until B11
lands. A bare slug in `references` resolves against the CURRENT unit and would
have built a link to a B10 page that does not exist; `check_internal_links`
catches that, and the dict form is what b9-01 and b8-01 use for the same reason.

── figures: [] and MEASURED ───────────────────────────────────────────

`<img>`, `<figure>` and `<picture>` each appear ZERO times on this page —
grepped, not assumed — and every `<svg>` is the nav chevron, a rail tick or a
ladder mark. Schema §11 says the same across all five B10 pages and explains
why: b10-02's `zoom-bench` is itself the nesting figure NOTES flag 19 asks for,
and Photo 51 is a licensing decision that is Mide's and not a commissioning one.
Nothing in THIS lesson is spatial or structural — the bench draws six graphs out
of DOM and the argument is the gap between two bars — so declaring a figure slot
would invent a sourcing task in `docs/ks3/diagram-manifest.md` for a drawing
nothing on the page references.

── ⚑ For Mide's science gate — every NOTES-B10 flag landing on THIS lesson ─

Four flags, four checked, **none corrected**. Schema §16 already ruled flags 9,
10 and 13, which are b10-03's and b10-04's, and none of the four below was held
for an answer by `README.txt`.

  * flag 1   **The sixty-student data set is invented.** CHECKED AND LEFT, and
             the page says so itself: the legal line opens *"The sixty-student
             data set is invented for this lesson, shaped to be realistic rather
             than taken from a real survey."* That is MRB-225 performed in the
             drawing — the claim is already stated at the size that is true.
             The shapes are right: all three continuous characteristics peak in
             the middle bin and fall away either side, and the blood group
             column runs O 28, A 25, B 5, AB 2 out of sixty, which is about
             47 / 42 / 8 / 3 per cent against the usual UK figures of roughly
             48 / 38 / 10 / 3. Close enough for a class survey and the legal
             line calls them approximate. ⚑ Mide's if he wants a real set;
             the cost would be six `bins` lists and nothing else.
  * flag 2   **Eye colour as three categories.** CHECKED AND LEFT. It is the
             one characteristic on the bench that could be argued onto the other
             side of the line, and the page argues it ITSELF rather than hiding
             it: the `shape` field says real eyes grade into one another more
             than three columns suggest and that the categories have to be
             agreed before the survey starts, and the legal line says it again.
             A recorded category IS discontinuous — the recording is what makes
             it so — and saying that out loud is a better lesson than dropping
             the case. ⚑ If Mide wants it cut, the cost is one characteristic
             and the `cause` line that says several genes are involved.
  * flag 3   **Tongue rolling called "largely genetic" with the single-gene
             story flagged as too simple.** CHECKED AND LEFT, and this one is
             right where many textbooks are wrong. The clean single-gene account
             traces to Sturtevant in 1940, who withdrew it himself after twin
             studies found discordant identical pairs, and some people do learn
             it. Design's `cause` line says exactly that, and its last sentence —
             *a tidy example is usually a simplified one* — is the transferable
             point. Do not let a later pass "correct" it back to the textbook.
  * flag 4   **Dutch men averaging around 1.84 m, and a twenty-centimetre rise
             since 1860.** CHECKED AND LEFT. Both are the commonly reported
             figures and the argument does not depend on the second decimal:
             what the paragraph needs is that the rise is far too fast for the
             gene pool to have changed, which holds at fifteen centimetres as
             well as at twenty. The stalling and reversal in some countries is
             real and is the honest form of the claim.

── One phrase a later pass might read as a sequence leak, and should not ─

The bench prompt opens *"Data from one year group."* The word `year` appears
there and nowhere else in the lesson; `Year 7`, `Year 8`, `Year 9` and
`half-term` appear zero times, checked rather than assumed. "One year group"
names no year and pins the student to no point in a scheme of work — it says
where sixty students came from, which is what makes the data set one population
rather than a pile of numbers. Left as drawn.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes: *the shape of the graph tells you nothing
about the cause*. The hook's reveal, every one of the six `cause` lines, both
`#s-think` bodies, the key fact, rung 2's correct option, rung 3's fifth
criterion and the key note all say it at the same size. The stretch layer adds
the Dutch-height case and retracts nothing: it is the same claim applied
somewhere new, and it ends on the strongest available evidence that height is
genuinely both.
"""


# ── the six characteristics (page lines 330–361) ─────────────────────────
#
# Three continuous and three discontinuous, in Design's order, and the ORDER IS
# THE ARGUMENT twice over: `height` is `characteristics[0]` and therefore the tab
# the page opens on — the one characteristic that is continuous AND strongly
# inherited, which is `GENE-01` refuted before it is stated — and the switch from
# the third to the fourth tab is where the bars stop touching. `r_variation_
# plotter` refuses a bench that is all of one type for exactly that reason.
#
# ⛔ `data_type` IS NOT A LABEL. It decides the bar gap, the display-weight
# verdict line and whether the prediction was right, so a third spelling would
# make all three wrong at once and still draw a plausible graph. Two values, and
# the renderer closes the set.
#
# `shape` and `cause` are the lesson's TWO QUESTIONS and neither may be folded
# into the other. `axis` is the mono caption that says IN WORDS why the bars
# touch or do not — it is the only place the gap rule is spoken rather than
# drawn, which is what a student reading with a screen reader gets instead.
CHARACTERISTICS = [
    {"id": "height", "label": "Height",
     "name": "Height, in centimetres",
     "data_type": "continuous",
     "axis": "height in cm · 60 students · bars touch because the categories "
             "are ranges",
     "bins": [{"label": "145–150", "n": 3}, {"label": "150–155", "n": 7},
              {"label": "155–160", "n": 13}, {"label": "160–165", "n": 16},
              {"label": "165–170", "n": 12}, {"label": "170–175", "n": 6},
              {"label": "175–180", "n": 3}],
     "shape": "A smooth hump with no gaps. Every value in the range is "
              "possible, and most people are near the middle — which is what "
              "the shape of nearly all continuous data looks like.",
     "cause": "Both. Hundreds of genes each contribute a little, and "
              "childhood nutrition and health move the whole thing up or "
              "down. The clearest example there is of a characteristic with "
              "two causes at once."},
    {"id": "span", "label": "Hand span",
     "name": "Hand span, in centimetres",
     "data_type": "continuous",
     "axis": "hand span in cm · 60 students · bars touch because the "
             "categories are ranges",
     "bins": [{"label": "15–16", "n": 4}, {"label": "16–17", "n": 9},
              {"label": "17–18", "n": 15}, {"label": "18–19", "n": 17},
              {"label": "19–20", "n": 10}, {"label": "20–21", "n": 5}],
     "shape": "The same hump. Any span between the smallest and largest is "
              "possible, so the data has no gaps and the bars have none "
              "either.",
     "cause": "Both, and mostly genetic — hand span is closely related to "
              "height, which is the same argument one step removed."},
    {"id": "mass", "label": "Body mass",
     "name": "Body mass, in kilograms",
     "data_type": "continuous",
     "axis": "mass in kg · 60 students · bars touch because the categories "
             "are ranges",
     "bins": [{"label": "35–40", "n": 5}, {"label": "40–45", "n": 11},
              {"label": "45–50", "n": 16}, {"label": "50–55", "n": 14},
              {"label": "55–60", "n": 9}, {"label": "60–65", "n": 5}],
     "shape": "Continuous, and wider than the height curve. Mass has more "
              "room to vary because it responds much more strongly to how "
              "someone lives.",
     "cause": "Both, and the environmental share is larger than for height — "
              "diet and activity can move an individual a long way, which is "
              "why this curve is the broadest of the three."},
    # ⚖️ THE FIRST DISCONTINUOUS ONE, and the tab where the gap opens. It is also
    # the only characteristic on the bench with a one-word cause — "Genes only." —
    # and the cleanest half of the shape-versus-cause split: four sharp groups AND
    # a single cause, against height's smooth curve AND two causes.
    {"id": "blood", "label": "Blood group",
     "name": "Blood group",
     "data_type": "discontinuous",
     "axis": "blood group · 60 students · bars are separated because the "
             "categories are",
     "bins": [{"label": "O", "n": 28}, {"label": "A", "n": 25},
              {"label": "B", "n": 5}, {"label": "AB", "n": 2}],
     "shape": "Four separate columns and nothing between them. There is no "
              "such thing as being partway between group A and group B, so "
              "the bars are drawn apart.",
     "cause": "Genes only. One gene, three versions of it, and nothing you "
              "eat, do or experience can change your blood group."},
    # ⚑ NOTES-B10 flag 3. "Largely genetic", with the clean single-gene story
    # called too simple. Checked and left — the working is in the docstring, and
    # the last sentence is the transferable point, not a hedge to be trimmed.
    {"id": "tongue", "label": "Tongue rolling",
     "name": "Able to roll the tongue",
     "data_type": "discontinuous",
     "axis": "can or cannot · 60 students · two separate categories",
     "bins": [{"label": "Can roll", "n": 39}, {"label": "Cannot", "n": 21}],
     "shape": "Two columns. You either can or you cannot, with no halfway, "
              "which makes this the simplest discontinuous characteristic to "
              "survey in a classroom.",
     "cause": "Largely genetic, and the textbook version that calls it a "
              "single gene is now known to be too simple — identical twins "
              "sometimes differ, and some people learn it. A good reminder "
              "that a tidy example is usually a simplified one."},
    # ⚑ NOTES-B10 flag 2, and the legal line says it a second time. The `shape`
    # field does the arguing itself: recorded AS categories, so plotted as separate
    # bars, and the categories have to be agreed before the survey starts. Checked
    # and left; see the docstring.
    {"id": "eyes", "label": "Eye colour",
     "name": "Eye colour",
     "data_type": "discontinuous",
     "axis": "recorded colour · 60 students · categories, so the bars are "
             "separated",
     "bins": [{"label": "Brown", "n": 34}, {"label": "Blue", "n": 17},
              {"label": "Green or hazel", "n": 9}],
     "shape": "Recorded as categories, so it is plotted as separate bars — "
              "though real eyes grade into one another more than three "
              "columns suggest, which is why the categories have to be agreed "
              "before the survey starts.",
     "cause": "Genes only, but several genes rather than one. Nothing in the "
              "environment changes it, and the old rule that two blue-eyed "
              "parents cannot have a brown-eyed child is not reliable."},
]

# ── the four cards in the band section (page lines 363–368) ──────────────
#
# TWO PAIRS, AND THE PAIRING IS THE SECTION. Design's `kind` is the mono accent
# tag and it reads "Question one · shape" on the first two and "Question two ·
# cause" on the last two — so the card grid IS the key fact, laid out. `kind`
# maps to `role`, `name` to `name` and `eg` to `examples`, which are the slots
# `_rule_card()` reads for them; the fourth part is the mono example line under
# the body, which is the slot b1-04's four problem cards shipped as empty `<li>`s
# for before MRB-245 repaired it.
#
# ⚖️ The examples are chosen so that the two questions cut ACROSS each other,
# and that is the whole reason both pairs are drawn: blood group and eye colour
# appear under Discontinuous AND under Genes; height and mass appear under
# Continuous AND under Environment, or both. A student who reads shape as cause
# has to explain why the same characteristic is on two different cards.
KIND_CARDS = [
    {"role": "Question one · shape",
     "name": "Continuous",
     "body": "Any value between the extremes is possible. Plotted as a "
             "histogram with the bars touching, because the categories are "
             "ranges that join up.",
     "examples": "Height, mass, hand span, leaf length"},
    {"role": "Question one · shape",
     "name": "Discontinuous",
     "body": "Separate categories with no values in between. Plotted as a bar "
             "chart with gaps, because the categories really are separate.",
     "examples": "Blood group, eye colour, tongue rolling, number of siblings"},
    {"role": "Question two · cause",
     "name": "Genes",
     "body": "Inherited from your parents and fixed at conception. Nothing "
             "you do changes it, and you can pass it on.",
     "examples": "Blood group, eye colour, natural hair colour"},
    {"role": "Question two · cause",
     "name": "Environment, or both",
     "body": "Shaped by food, exercise, illness, sunlight or accident. Most "
             "characteristics are both: genes set a range and the environment "
             "decides where in it you land.",
     "examples": "Height, mass, scars, language spoken"},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 163 character for character.
    "slug":        "variation-continuous-and-discontinuous",
    "title":       "Variation: continuous and discontinuous",
    "discipline":  "biology",
    "unit":        "inheritance-and-dna",
    "family":      "INVESTIGATION",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.INH.04` — continuous or discontinuous variation within a species,
    # including measurement and graphical representation — owned WHOLE. It is
    # not sub-split in `substatements.py`; see the docstring.
    "covers":      ["KS3.B.INH.04"],
    # Named, used, and owned elsewhere. INH.02 is b10-02's and b10-03's: this
    # page says "a single gene with a few versions" and "hundreds of genes, each
    # contributing a small amount" and explains neither — the model of
    # chromosomes, genes and DNA arrives next lesson, and rung 3 marks the
    # ONE-versus-MANY count rather than the machinery. WS.EXP.06 is b9-06's
    # sampling statement, which rung 4 asks the student to apply and this page
    # does not re-teach.
    "touches":     ["KS3.B.INH.02", "KS3.WS.EXP.06"],
    "beyond_statutory": False,
    # `genes-and-evolution` at `develop`: the student met genes as the thing a
    # gamete carries in b5-02 (`encounter`), and this is where the thread is used
    # on something new — a room full of people, and a graph. It is the only
    # thread this lesson genuinely runs; the data-handling spine is Working
    # Scientifically, which architecture §4.7 rules is deliberately NOT a thread
    # and is declared under `ws` instead.
    "threads":     [{"id": "genes-and-evolution", "level": 2}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. `sampling-an-ecosystem`
    # is the b9-06 edge this lesson RESOLVES (see the docstring) and it is also
    # rung 4's destination — the one place the slot code had to be resolved to a
    # title. Both are bare slugs: `requires` resolves across the whole key stage.
    "requires":    ["sampling-an-ecosystem", "life-processes"],
    "assumes":     [],
    # Design's "Connects to" card, in her order.
    #
    # ⚠️ `variation-and-competitive-success` MUST carry its unit. A bare slug in
    # `references` is resolved against the CURRENT unit — unlike `requires` — so
    # the bare form would build a link to a B10 page that does not exist. B11 is
    # not yet built, so this renders as a coming-soon line, which is the same bet
    # b9-06 made on this lesson and it is why this lesson exists to resolve it.
    "references":  ["chromosomes-genes-and-dna",
                    {"unit": "B11",
                     "lesson": "variation-and-competitive-success"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Normal distributions, polygenic inheritance, and "
                   "separating genetic from environmental causes using twin "
                   "and adoption studies.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Line a class up by height and you get a smooth ramp with "
                    "no gaps. Line the same class up by blood group and you "
                    "get four piles and nothing in between. The difference is "
                    "not what you measured with.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them (page lines 322–327). `s-two` is the
    # third: no control of its own, so it mirrors `s-bench` and ticks on the
    # bench's predicate — Design's own `isDone()`, page lines 417–418. `short`
    # and `label` are her `RAIL_SHORT` and `RAIL` strings, "Four piles" included.
    # Shipping three fails `check_rail_matches_design`; see the docstring.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Four piles",
         "done_when": "committed"},
        # Design's own threshold, kept: three of the six plotted (page line
        # 417). Sticky by her design and monotonic by ours — `plotted` is a map
        # that is only ever added to, and there is no reset to untick it.
        {"anchor": "s-bench", "short": "BENCH", "label": "Plot it",
         "done_when": "three_plotted"},
        # The MIRROR. Design gives it the bench's predicate character for
        # character one line further down, so the stop ticks the moment the
        # bench does and nothing ticks on load.
        {"anchor": "s-two", "short": "TWO", "label": "Two questions",
         "mirrors": "s-bench",
         "done_when": "three_plotted"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key, and Design's own
    # reveal is gated on `hookChoice !== null` rather than on a right answer
    # (schema §7: no option is correct, any choice reveals the same paragraph).
    # C is the one the reveal endorses and it says so at once; the hook is not a
    # trick, it is the definition the bench then has to earn six times.
    #
    # ⚖️ OPTION B IS `GENE-02`, WORD FOR WORD, and it is the reason this section
    # is that belief's `elicited_by`. A and D are the shape-versus-cause
    # conflation from the other side — both answer a question about SHAPE with a
    # fact about CAUSE — so the hook offers the whole of the lesson's error space
    # before a single graph is drawn.
    "phenomenon": {
        "kind": "narrative",
        "title": "Nobody is halfway between blood group A and blood group B.",
        "prompt": "Somebody in your class is halfway between the two tallest "
                  "people, and somebody is halfway between them. Keep going "
                  "and you never run out of in-between values. Do the same "
                  "with blood group and you stop immediately: there are four, "
                  "and nothing sits between them.",
        "commit": "What decides which kind of variation a characteristic "
                  "shows?",
        "options": [
            # A: a question about SHAPE answered with a fact about CAUSE
            "Whether it is inherited from your parents",
            # B: GENE-02, word for word, and this is its `elicited_by`
            "Whether you can measure it with an instrument",
            # C: the one the reveal endorses
            "Whether values exist in between",
            # D: the same conflation as A, from the environment side
            "Whether the environment can change it",
        ],
        "reveal": "Whether intermediate values exist. If any value between "
                  "two others is possible, the variation is continuous; if "
                  "the characteristic falls into separate groups with nothing "
                  "between them, it is discontinuous. That is the whole "
                  "definition, and it says nothing yet about what causes the "
                  "variation.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Schema §12's pre-allocation for b10-01, and the two beliefs Design's
    # `#s-think` quotes, in her page order. Both statements are her own bytes,
    # page lines 192 and 199, in register voice.
    #
    # ⊕ The `GENE` prefix row was opened in
    # `docs/ks3/misconception-register.md` by the register pass during this run,
    # and its rows for these two ids agree with these on all three fields. That
    # file is not this pass's to edit (contract §0); re-checked at the end of
    # the run because it was in flight. See the docstring.
    #
    # ⛔ `GENE-11` is this lesson's named SPARE and is NOT claimed: two beliefs
    # were found and two ids were used. It stays permanently unused rather than
    # being re-pointed at anything later (schema §12).
    #
    # The two `elicited_by` values are deliberately different — rung 2 option A
    # for the first, hook option B for the second — and the reasoning is in the
    # docstring. Both `confronted_by` values are `s-think`, the confrontation
    # block's emitted anchor, and all four resolve against the BUILT page
    # (MRB-244).
    "misconceptions": [
        {"id": "GENE-01",
         "statement": "Continuous variation is caused by the environment; "
                      "discontinuous variation is genetic.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "GENE-02",
         "statement": "If you can measure it with a ruler it is continuous.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B10, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its exclusion
    # list. Every definition below is authored, not lifted.
    #
    # ⚖️ The two graph names are glossed as CLAIMS rather than as shapes —
    # "the touching bars are the claim that the values in between exist" — because
    # that is what the bench's derived gap teaches and a chip that said "bars
    # touch" would teach the convention as an arbitrary rule. `gene` is
    # deliberately absent: it is b10-02's chip and this lesson touches INH.02
    # rather than owning it.
    "vocabulary": [
        {"term": "variation",
         "definition": "The differences between individuals of the same "
                       "species.",
         "note": "Every characteristic you can measure or record has some."},
        {"term": "continuous variation",
         "definition": "Variation with values that grade into one another, so "
                       "any value between two others is possible.",
         "note": "Height, mass, hand span. Plotted as a histogram."},
        {"term": "discontinuous variation",
         "definition": "Variation that falls into separate groups with no "
                       "values in between.",
         "note": "Blood group, tongue rolling. Plotted as a bar chart."},
        {"term": "histogram",
         "definition": "A graph whose bars touch, because the categories are "
                       "ranges that join up.",
         "note": "The touching bars are the claim that the values in between "
                 "exist."},
        {"term": "bar chart",
         "definition": "A graph whose bars are drawn apart, because the "
                       "categories really are separate.",
         "note": "The gap is the claim that nothing sits between them."},
        {"term": "characteristic",
         "definition": "A feature of an organism that can be measured or "
                       "recorded.",
         "note": "The thing you choose before you can ask either question "
                 "about it."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # zero times on this page — grepped — and every `<svg>` is chrome. Schema §11
    # says the same of all five B10 pages and gives the reason; nothing in this
    # lesson is spatial or structural, and declaring a slot the page never
    # references would invent a sourcing task in `docs/ks3/diagram-manifest.md`.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b10/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md §2. The
        # read sites are listed in the docstring; `reset_label`, an opening
        # selection, and every one of `char`, `predicts` and `plotted` are
        # deliberately absent and each has its own reason there.
        {"type": "variation-plotter", "id": "predict-the-graph-then-plot-it",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · sixty students, six characteristics",
         "heading": "Predict the graph, then plot it",
         "prompt": "Data from one year group. The cause line underneath is "
                   "a separate question from the shape.",

         # The mono label over the six tabs, and the mono word at the end of the
         # head readout. `_KIND_HEAD_FROM` composes "{n} of {total} plotted" from
         # the suffix and `_KIND_HEAD_TOTAL` counts the characteristics, so the
         # denominator is a fact about the payload rather than a number authored
         # twice — and the resting bytes read "0 of 6 plotted", not "{n} of…".
         "options_label": "Characteristic",
         "progress_suffix": "plotted",

         "characteristics": CHARACTERISTICS,

         # ⚠️ THE ESCAPE LEAK, REPAIRED. Page line 129 prints `\u2014` as six
         # literal characters inside the markup; the em dash is what Design meant
         # and what the two buttons underneath already carry. "What could not be
         # lifted" 2, and it is reported rather than fixed silently.
         "predict_label": "Before you plot it — which shape do you expect?",
         # ⛔ THE IDS ARE THE TWO DATA TYPES. They are compared against each
         # characteristic's `data_type` to decide the verdict, so an id outside
         # the pair would be a prediction that is wrong on all six
         # characteristics while the page looked entirely normal. The renderer
         # closes the set; this is the record that has to match it.
         "predict_options": [
             {"id": "continuous",
              "label": "Smooth range — continuous"},
             {"id": "discontinuous",
              "label": "Separate groups — discontinuous"},
         ],

         # ⚖️ THE DISPLAY-WEIGHT LINE THAT NAMES THE SHAPE, keyed on `data_type`
         # — the same value that set the gap the student is looking at. It is the
         # answer to question one, printed between the verdict tag and the
         # explanation, and without it the panel opens on a tag and then prose
         # with the answer missing from between them.
         "kind_lines": {
             "continuous": "Continuous — a histogram, bars touching",
             "discontinuous": "Discontinuous — a bar chart, bars separated"},

         "run_label": "Plot the data",
         "run_done_label": "Plotted",

         # ⛔ THE ONE THING IN THIS UNIT THAT JUDGES A PREDICTION (schema §0.6,
         # a recorded and deliberate departure from B7 §0.6). Both tags are drawn
         # in the same tone on the same cream panel — accent-TEXT mono, no green,
         # no red, no badge — because what is being judged is the IDEA the
         # student committed to about the shape of some data, not the student.
         # It says nothing whatever about the cause line underneath it.
         "verdicts": {
             "right": "Your prediction was right",
             "wrong": "Not what you predicted"}},

        # #s-two — the band panel, rail stop 3, mirroring `s-bench`. Design draws
        # eyebrow, statement, four cards, key fact — and NO closing paragraph, so
        # `close` is absent and the ordering finding b9-01 reported (`r_rule`
        # emits the nested key fact before `close`) cannot arise on this page.
        {"type": "rule", "anchor": "s-two",
         "eyebrow": "Two questions, asked separately",
         "statement": "What shape is it, and what caused it.",

         "cards": KIND_CARDS,

         # Design nests the key fact inside this section (page lines 181–183) on
         # the CARD ground with the 5px accent offset shadow. `card`, because the
         # section itself is `--ks3-band` and band on band is invisible — the same
         # arrangement and the same reason as b7-01's, b8-01's and b9-01's.
         "key_fact": {"ref": "shape-and-cause-are-two-questions",
                      "ground": "card"}},

        {"type": "misconception", "id": "shape-is-not-cause",
         "anchor": "s-think", "targets": "GENE-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-two on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 183
    # and identical to payload schema §13's b10-01 entry.
    #
    # ⚖️ ITS LAST TWO SENTENCES ARE THE LESSON. Everything else on the page is
    # in service of them, and no later pass may compress them into one: "a
    # question about the data" and "a separate question with a separate answer"
    # are the two halves `GENE-01` collapses.
    "key_facts": [
        {"id": "shape-and-cause-are-two-questions",
         "text": "Continuous variation has intermediate values and is plotted "
                 "as a histogram; discontinuous variation falls into separate "
                 "groups and is plotted as a bar chart. Whether variation is "
                 "continuous is a question about the data. What caused it — "
                 "genes, environment or both — is a separate question with a "
                 "separate answer.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, no `sc-if`,
        # schema §9), so it is a `confrontation` and not a `predict`, it is not a
        # rail stop, and it emits no completion contract. Contract R1's `predict`
        # branch applies where `#s-think` gates a reveal behind a commitment; no
        # B10 page does.
        {"id": "shape-is-not-cause",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "GENE-01",
         "statements": [
             # GENE-01, and the `<em>` run at the end is kept — `rich()` renders
             # it — because "one gene tends to give discontinuous variation; many
             # genes tend to give continuous variation" is the honest summary the
             # whole paragraph is built to earn, and the italics are how Design
             # marks it as the thing to take away. ⚖️ Note what the correction
             # does NOT do: it does not replace one cause with another. It
             # answers a question about CAUSE with a fact about the NUMBER of
             # genes, which is the only answer that leaves both causes standing.
             {"quote": "Continuous variation is caused by the environment; "
                       "discontinuous variation is genetic.",
              "body": ["Height is the counter-example that settles it: it is "
                       "continuous, and it is one of the most strongly "
                       "inherited characteristics there is — tall parents "
                       "have tall children with great reliability — while "
                       "also being affected by childhood nutrition. Both "
                       "causes, one smooth curve. What actually makes a "
                       "characteristic continuous is the number of genes "
                       "involved. Blood group is decided by a single gene "
                       "with a few versions, so you get a few discrete "
                       "groups. Height is influenced by hundreds of genes, "
                       "each contributing a small amount, and hundreds of "
                       "small contributions added together produce a smooth "
                       "range with no gaps in it — then the environment moves "
                       "everyone a little further along. So the honest "
                       "summary is: <em>one gene tends to give discontinuous "
                       "variation; many genes tend to give continuous "
                       "variation</em>; and the environment can adjust "
                       "anything that is not fixed at conception."]},
             # GENE-02. The two `<em>` runs here are the TEST, stated as two
             # rival questions a sentence apart, and they are the reason this
             # body cannot be flattened: "can I put a number on it" against "can
             # a value exist between two neighbouring values" is the whole
             # correction, and it lands as a contrast or not at all.
             {"quote": "If you can measure it with a ruler it is continuous.",
              "body": ["Close enough to be dangerous. Number of brothers and "
                       "sisters is a number, you can count it precisely, and "
                       "it is discontinuous — nobody has 2.4 siblings, and "
                       "the average being 2.4 does not make it a possible "
                       "value for a person. Number of leaves on a plant, "
                       "number of petals, shoe size in the UK system: all "
                       "counted, all discontinuous, because the values step "
                       "rather than flow. The test is not <em>can I put a "
                       "number on it</em> but <em>can a value exist between "
                       "two neighbouring values</em>. Between 172 cm and 173 "
                       "cm there is 172.4 cm and a student who is exactly "
                       "that; between two and three siblings there is nothing "
                       "at all. Get that test right and the graph follows "
                       "automatically: bars that touch for continuous data "
                       "because the categories are ranges that join up, bars "
                       "with gaps for discontinuous data because the "
                       "categories genuinely are separate."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — BOTH MARKED RUNGS CLEAN AS DRAWN, AND NOTHING
    # WAS TOUCHED. rung 1 correct 5w against 2 / 2 / 7 (the longest option on
    # the rung is a DISTRACTOR); rung 2 correct 11w against 11 / 7 / 10 (TIED
    # with distractor A, so not strictly longest). No correct option was
    # shortened, no `answer` index moved, no correction edited and no distractor
    # padded. Full working in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Sort them",
            "q": "Which of these shows discontinuous variation?",
            # Design's four, untouched. All four NAME a characteristic and
            # nothing else, so there is no rule anywhere in the set for a
            # correct answer to be longer than — and the seven-word option is
            # a distractor. Each of the three wrong ones is a different way
            # of being continuous: a length measured in whole units, a mass
            # read off a scale, and a natural object that grades smoothly.
            #
            #   A  correct — counted, steps, no intermediates
            #   B  GENE-02's shape: measured with a ruler, so read as
            #      continuous — and it IS continuous, which is why this rung
            #      cannot ELICIT the belief, only reward it
            #   C  authored belief: a decimal place means continuous
            #   D  authored belief: leaves are countable objects, so counting
            #      them is the same as measuring one
            "options": [
                "Number of brothers and sisters",
                "Arm length",
                "Body mass",
                "Length of the leaves on a tree",
            ],
            "answer": 0,
            "feedback": {
                1: "Any value between the shortest and longest arm is "
                   "possible, so it is continuous — even though it is "
                   "measured in whole centimetres for convenience.",
                2: "Continuous. The scale reads to a decimal place because "
                   "every value in between genuinely exists.",
                3: "Continuous, and a good one to survey — leaf length grades "
                   "smoothly from the smallest to the largest on a single "
                   "branch.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Height is continuous. What does that tell you about its "
                 "cause?",
            # Design's four, untouched, and the construct is why the gate is
            # quiet: three of them begin "That…" and name a wrong CAUSE, and
            # the correct one refuses the question the stem asks. Same
            # subject, same grammar, same kind of consequence.
            #
            #   A  GENE-01 — continuous, therefore environmental
            #   B  correct: shape and cause are separate questions
            #   C  the mirror-image error: continuous, therefore genes alone
            #   D  authored belief: genes can only ever produce categories,
            #      so a smooth range rules genes out altogether
            "options": [
                "That it is caused by the environment rather than by genes",
                "Nothing on its own — shape and cause are separate questions",
                "That it is caused by genes alone",
                "That no genes are involved, since genes give discrete "
                "categories",
            ],
            "answer": 1,
            # All three corrections are Design's, byte-identical. Each answers
            # exactly the belief its own option states, and C's is the one
            # that does the lesson's real work: it concedes the genetics and
            # then refuses the inference.
            "feedback": {
                0: "Height is one of the most strongly inherited "
                   "characteristics there is. Continuous does not mean "
                   "environmental.",
                2: "Also no. Nutrition in childhood affects adult height, "
                   "which is why average height has risen so much in a "
                   "century.",
                3: "One gene tends to give categories. Hundreds of genes each "
                   "adding a little give a smooth range — which is exactly "
                   "what height is.",
            }},
        "explain": {
            # ⚖️ THE RUNG THE KEY FACT IS WRITTEN FOR. It hands the student
            # two characteristics that are BOTH strongly genetic and asks why
            # only one of them is smooth — so the answer cannot be "genes
            # versus environment", and criterion 5 then asks separately what
            # the environment does to each. One gene against many genes is
            # the only account that works, which is `GENE-01` refuted by
            # construction rather than by contradiction.
            "title": "Rung 3 · Explain the smooth curve",
            "q": "Blood group falls into four sharp categories and height "
                 "forms a smooth curve, although both are strongly influenced "
                 "by genes. Explain the difference, and say what part the "
                 "environment plays in each.",
            "field_label": "Your explanation",
            "placeholder": "Blood group is controlled by…",
            "success": [
                "Says blood group is controlled by a single gene with a small "
                "number of versions.",
                "Says a single gene therefore produces a small number of "
                "distinct categories with nothing in between.",
                "Says height is influenced by a large number of genes, each "
                "contributing a small amount.",
                "Says many small contributions added together produce a "
                "smooth range of values.",
                "Says the environment — nutrition and health — affects height "
                "but has no effect at all on blood group.",
            ]},
        "produce": {
            # ⚠️ `b9-06` RESOLVED TO ITS LESSON TITLE — "What could not be
            # lifted" 1. A student cannot resolve a slot code and printing one
            # is the platform leakage §8.10 exists to stop; the destination
            # survives in `requires`, and this is the rung that makes the
            # b9-06 edge real rather than decorative.
            "title": "Rung 4 · Take it somewhere new",
            "q": "Plan an investigation into variation in leaf length on a "
                 "single tree. Say how you would collect the data, how you "
                 "would present it, and how you would avoid the sampling "
                 "problem you met in Sampling an ecosystem.",
            "field_label": "Your plan",
            "placeholder": "I would collect leaves…",
            "success": [
                "Collects a large enough sample — at least fifty leaves — and "
                "says why a small sample is not enough.",
                "Chooses the leaves without bias, rather than picking ones "
                "that look interesting or are easy to reach.",
                "Measures each leaf the same way, from the same points, with "
                "a stated precision.",
                "Groups the measurements into equal ranges and plots a "
                "histogram with touching bars, because the data is continuous.",
                "Predicts a hump-shaped curve, and identifies a factor that "
                "could shift it — shade, height on the tree, or age of the "
                "shoot.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Continuous variation has values that grade into one another "
                "with no gaps, and is shown on a histogram with touching "
                "bars. Discontinuous variation falls into separate categories "
                "with no intermediates, and is shown on a bar chart with "
                "gaps. Characteristics controlled by one gene tend to be "
                "discontinuous; those influenced by many genes tend to be "
                "continuous, and the environment can shift anything that is "
                "not fixed at conception.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B10 flag 4 lives in the first two sentences and is checked and
    # left; the working is in the docstring. ⚖️ MRB-225 holds: the layer applies
    # the lesson's own claim to a population over a century and a half and
    # retracts nothing above it. Its last sentence is the whole argument in one
    # object — a doorway built for people who were shorter because of what they
    # ate, not because of what they carried.
    "stretch": [
        {"type": "explainer", "id": "why-the-dutch-got-taller",
         "text": "Dutch men are now the tallest in the world, averaging "
                 "around 1.84 m, and in 1860 they were among the shorter "
                 "populations in Europe. Twenty centimetres in a century and "
                 "a half is far too fast for the gene pool to have changed "
                 "much — what changed was nutrition, public health and "
                 "childhood disease. The same shift has happened in South "
                 "Korea and Japan within living memory, and it has stalled or "
                 "reversed in a few countries where nutrition got worse. This "
                 "is the clearest evidence there is that height is genuinely "
                 "both: the ranking within a population is largely inherited, "
                 "and the level the whole population sits at is set by the "
                 "environment. It also explains a fact you can check in any "
                 "old building — Tudor doorways and the bunks in Nelson's "
                 "navy were not built for shorter people out of some quirk of "
                 "taste."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to sort a characteristic the bench does not cover?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 312) and nothing in it is a safety
    # instruction — it is a note about where the numbers came from and how far
    # one of the six categories can be trusted. Routing it through `safety_note`
    # would print it in the treatment reserved for "never light a candle without
    # an adult".
    #
    # ⚑ NOTES-B10 flags 1 and 2 both land here, and this line is where the page
    # is honest about them in front of the student. It must keep saying the same
    # thing as the eye-colour `shape` field, which makes the same admission in
    # the middle of the bench.
    "convention_note": "The sixty-student data set is invented for this "
                       "lesson, shaped to be realistic rather than taken from "
                       "a real survey. Blood group frequencies are "
                       "approximate UK values. Eye colour is treated as three "
                       "categories here, which is a simplification: eye "
                       "colour is influenced by several genes and real eyes "
                       "grade into one another more than this bench suggests.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is `present observations and data using appropriate methods`
    # (ANA.02) performed rather than described — the student commits to a shape,
    # draws it, and reads a conclusion off it — and rung 3 is `interpret
    # observations and data` (ANA.03). Rung 4 is a planning task with a sampling
    # constraint, which is the experimental strand rather than the analytical
    # one. Nothing here is measured by the student, so `measurement` is not
    # claimed even though the data set is measured data.
    "ws": ["analysis-and-evaluation",
           "experimental-skills-and-investigations"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
