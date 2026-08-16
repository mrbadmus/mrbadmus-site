"""B5 L2 — Gametes and fertilisation (PROCESS).

Authored against Design's approved page,
`KS3 B5 lessons/b5-02-gametes-and-fertilisation.dc.html` (561 lines), under the
MRB-220 build contract, with `NOTES-B5.md` and `README.txt` read whole.

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted", none of which is a
sentence of science. The six comparison rows, the five steps, the two scale
rows and all four ladder rungs came out of
`node tools/extract_design_payload.js`, not off a keyboard.

── ⚠️ TONE IS A GATE ON THIS LESSON, AND NOTHING HERE SOFTENS IT ────────

Design's register is the ruled one (confirmed 16 Aug 2026, MRB-244; see
`ks3_data/b5/__init__.py`). This lesson is clinical and function-first
throughout: *sperm cell*, *egg cell*, *oviduct*, *uterus*, *vagina*, *semen*,
*implantation*, each used plainly and each doing a job in the argument. There
is no euphemism, no sexual detail beyond `REP.01b`'s clause, no normative
language about families, and no conflation of sex with gender — the page never
says *man* or *woman* anywhere, and this record has not introduced either. The
copy is third person except in the legal foot line (see below).

Nothing has been softened, sharpened, warned about or annotated on the way in.
Where a judgement was unavoidable it is recorded here for Mide rather than
taken silently in the data.

── `covers` is the SUB-ID, not the whole bullet ─────────────────────────

`KS3.B.REP.01` is the longest bullet in the KS3 biology spine and
`ks3_data/substatements.py` splits it at its own clause list. This lesson owns
**`KS3.B.REP.01b`** — *"Gametes and fertilisation."* It must NOT claim `REP.01`
whole: `human-reproductive-systems` owns `a`, `the-menstrual-cycle` owns `c`,
`gestation-placenta-and-birth` owns `d` and `lifestyle-and-the-developing-
foetus` owns `e`, and §5.7's exactly-once rule would fail the build on the
overlap. The five steps here run to implantation and stop: what the uterus
lining was doing beforehand is lesson 3 and what happens next is lesson 4, and
this page deliberately answers neither.

── The flagship: the reveal is GATED, one row at a time ─────────────────

`#s-compare` is `gamete-compare`, on `ks3-block ks3-dark ks3-practical` (page
line 114), so `practical` is MEASURED from Design's own markup rather than
inherited. Six features of two specialised cells, three columns, and **every
`why` is closed on load** — Design's state is `open: {}` (page line 419) and
each row's explanation renders only inside `<sc-if value="{{ row.open }}">`
(page lines 145–147). The whole row is the button; there is no separate chevron
control. A student who could read all six reasons on arrival would have been
told the argument instead of asked for it, and the section counter — *"0 of 6
opened"* on load — is Design saying so on the page.

⚠️ THE BLOCK IS ON INK. `.ks3-dark p` is (0,1,1) and beats a bare instrument
class at (0,1,0). Every text rule in this instrument's CSS must be scoped to at
least (0,2,0); this has now bitten five builds, and B4 shipped a label at
1.21:1 past a green kinds gate because of it. Flagged for the engine pass, not
fixable from a data module.

── One rail stop comes off, and it is the same defect for the sixth time ─

Design draws FOUR stops. `isDone('s-fert')` is

    if (id === 's-compare') return Object.keys(s.open).length >= 6;
    if (id === 's-fert')    return Object.keys(s.open).length >= 6;

— page lines 410–411, character for character the same predicate, one section
to the left. `#s-fert` is an eyebrow, a display statement, five static cards
and a key fact: no control, no commitment, no field, and nothing a student can
do inside it that the page can observe. MRB-208 ruled the rail is
completion-based and carries only sections that require the student to do
something, and `ks3_parity.check_rail_reachable` would fail it for exactly that
— a `rule` section carries none of the signals `doneByDom()` reads. Inventing a
demand Design did not draw is closed to this build.

So the lesson declares **THREE stops**, the same call and the same reasoning as
c1-02's `#s-matrix`, c1-05's `#s-scale`, b3-01's `#s-nutrients`, b3-02's
`#s-limits` and b4-01's `#s-parts`. **The section keeps its anchor**, so the
tutor card's `#s-fert` link and every hash link into it still resolve.

── What could not be lifted, and why ────────────────────────────────────

1. **The step cards' NUMBER CHIPS, and step 03's promotion.** Design draws
   `#s-fert` as an `<ol>` of five cards, each with a chip `01`–`05`, and
   promotes the third — `--ks3-inset` ground, a 3px border instead of 2px, and
   an accent chip instead of an ink one (page lines 501–504). `r_rule` emits a
   `<ul>` on a `repeat(auto-fit, minmax(220px, 1fr))` grid with no slot for a
   numeral and no per-card ground. Document order is preserved, so the five
   steps still read in order, and the promotion survives **in words** rather
   than in paint: step 3's own card says *"This step, and only this step, is
   fertilisation."*, the panel statement above it says *"Five steps, and only
   one of them is fertilisation."*, and the key fact under it names the same
   event a third time. The chips and the highlight are DROPPED rather than
   smuggled into the card text. Reported. The fix, if the promotion is to win,
   is an `index` + `emphasis` flag on `rule` — not a new block type, because
   §5.1.1's vocabulary is closed and `render_blocks` raises on anything outside
   it. b4-01 gave up the same chips on the same component.

2. **The `where` column is FOLDED into the card term, not dropped.** Design
   sets it in mono accent type on the same baseline as the step name
   (`Fertilisation` / `Oviduct — and nowhere else`), and `r_rule`'s card is two
   parts. All five are DIFFERENT strings and every one of them is science —
   *"Oviduct — and nowhere else"* is the whole argument of the section — so
   they are joined to the name with " · ", which is b3-05's `#s-two` and
   b4-01's `#s-parts` precedent and Design's own separator elsewhere on this
   page ("Reproduction · Process", "Two specialised cells · six features").
   Both strings survive byte-identical.

3. **The key fact leaves Design's band panel.** She nests it inside `#s-fert`;
   `r_rule` has no nested key-fact slot (only `r_comparison` does), so it
   renders as its own top-level block directly under the panel, on the band
   ground every other top-level key fact in the key stage takes. The words are
   unchanged and the order is unchanged.

4. **One inline `<a href>`.** Design links *Specialised cells* (b1-04) inside
   the instrument's lede — *"These are the specialised cells from Specialised
   cells, doing the clearest job in the body."* `rich()` allows `<em>` and
   `<strong>` and nothing else; an anchor renders as visible tag soup. The
   WORDS are unchanged and the hyperlink is dropped. The destination survives
   as a `references` edge, because Design already draws it in her own end
   matter — this is not a third navigation edge invented for the page
   (MRB-205). b4-02, b4-03 and b3-07 resolved the identical case identically.

5. **Design draws TWO endmatter link cards; the engine emits one.** Her "Next
   in this unit" (`the-menstrual-cycle`) and "Connects to"
   (`human-reproductive-systems`, `specialised-cells`) become one card in
   `r_endmatter`, headed by `connects_heading`, the forward link first. b3-01
   and b4-01 resolved the identical layout the identical way. The heading "Next
   in this unit" is what is given up; no link is.

6. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

⚑ For Mide's science gate — NOTES-B5 §3 flags landing on THIS lesson:
  * **flag 3 — CARRIED AS INSTRUCTED, RECORDED APPROVED.** *"An egg cell has
    several thousand times the volume of a sperm cell."* against egg ~0.1 mm
    and sperm head ~0.005 mm. NOTES marks it **RESOLVED, 15 Aug** — the hedge
    "several thousand times" is consistent with the arithmetic the lesson
    itself gives further down the same section (*"a twentyfold difference in
    width is roughly an eight-thousandfold difference in volume"*), and rung 2
    says "thousands of times more material". Authored exactly as delivered in
    all three places. NOTES asks only that you confirm you are happy with the
    hedge; nothing has been rounded, tightened or reconciled here.
  * flag 4 — *"Fertilisation happens in the oviduct."* Named in the key fact,
    in step 3's `where`, and in the key note. `REPRO-03` is its entry.
  * flag 5 — *"It remains able to be fertilised for roughly a day."* (step 1).
    Usually given as 12–24 hours; b5-03 reuses the same claim.
  * flag 6 — *"Hundreds of millions set out; a few hundred arrive."* (step 2).
  * flag 7 — implantation "about five days" and *"it is where pregnancy
    begins"* (step 5, and the first confrontation says it again). A clinical
    rather than a purely biological definition, stated flatly, and b5-04 leans
    on it.
  * flag 8 — the outer layer changing so no second sperm can enter (step 3).
  * flag 9 — maternal mitochondrial inheritance and the molecular clock (the
    Going further layer), including the simplification that the sperm's
    mitochondria are destroyed after fusion — which the `mito` comparison row
    also states.
  * flag 12 — *"Almost none — it uses sugar in the fluid around it"* (the
    `food` row), the depth of which is shared with b5-01 rung 4.
  * flag 13 — `b5-gametes-labelled` is named in Design's legal line and is not
    in `docs/ks3/diagram-manifest.md`. Declared below at `status: "needed"`
    (§4.10, not a build blocker) so it is a tracked sourcing task rather than a
    dangling reference. Nothing is invented to fill it. NOTES asks that the
    human slots be ruled on for *what is illustrated and at what level of
    detail* before anything is commissioned; the caption here describes only
    what this page already teaches in words.

⚑ Findings of my own, all reported rather than repaired:

  A. **MRB-177 LENGTH TELL ON RUNG 1, MEASURED — and NOT rewritten.**
     Rung 1's correct option is 12 words against a longest distractor of 8:
     gap 4 (threshold ≥4) and ratio 1.50 (threshold ≥1.4), so it trips
     `verify_ks3.py`'s `length_tell` on both limbs. Rung 2 measures clean
     (13 against 10 — gap 3, ratio 1.30). Rewriting a distractor changes what a
     marked question measures, which is Mide's gate and not an author's, and
     the copy is lifted byte-identical, so the tell is authored AS DRAWN. It
     needs either Mide's rewrite or a `("gametes-and-fertilisation", "ladder
     recall")` entry in `verify_ks3.py`'s `KNOWN_TELLS` — the tenth, and the
     second found in a unit being built rather than inherited. Both of those
     are decisions above this module; neither file is touched here.

  B. **The page is internally inconsistent about emphasis markup, and is
     lifted as it stands.** The first confrontation writes *"Use *reaches* and
     you have described a crowd; use *fuses* and you have described the
     event."* with literal asterisks, then two clauses later writes
     `<em>implantation</em>` and `<em>pregnancy</em>` as real tags — the same
     device, two notations, one paragraph. The asterisks render as asterisks.
     MRB-205 says the page wins and that a page contradicting ITSELF is
     reported rather than ruled on silently, so all four are carried exactly as
     drawn: four literal asterisks and two `<em>` pairs. Converting the
     asterisks would be an authoring pass sharpening approved copy.

  C. **NOTES-B5 §4 promises two closing signposts; this page draws one.**
     §4 says every lesson in the human half "closes with two signposts: RSE/PSHE
     for relationships and consent, and a trusted adult, school nurse, doctor
     or midwife for anything personal." The legal line on this page carries the
     first and not the second. The page wins (MRB-205) and the line is lifted
     whole; the discrepancy is Design's to close if the second signpost was
     meant to be here.

  D. **The legal line is the one second-person sentence on the page**, and it
     is deliberate: *"relationships and consent are covered in your RSE and
     PSHE lessons"* addresses the reader about their own timetable, not about
     their own body. It is lifted byte-identical and routed to the foot line
     treatment §8.10 requires — small, bottom edge, never a callout. It is NOT
     a `safety_note`: nothing in it is a safety instruction, and printing it in
     the treatment reserved for "never light a candle without an adult" would
     devalue the safety line. b3-05, b3-07 and b4-01 resolve the identical foot
     line identically.
"""

# ── the six comparison rows (page lines 337–350, via extract_design_payload.js)
#
# ⚠️ Order is Design's and is load-bearing: `size` and `motion` set up the
# cheap-to-make argument, `chrom` is the one row where the two cells are
# identical and lands in the middle of the differences, and `number` is the
# consequence that closes it. Sorting these by anything would break the
# reading.
CMP = [
    {"id": "size",
     "name": "Size",
     "sperm": "Head about 0.005 mm",
     "egg": "About 0.1 mm — the largest cell in the body",
     "why": "The egg is large because of what it carries, not because of what "
            "it does. A sperm only has to travel, and travelling is easier the "
            "smaller you are."},
    {"id": "motion",
     "name": "Movement",
     "sperm": "A tail, and it swims",
     "egg": "None — it is moved for it",
     "why": "The egg is carried along the oviduct by cilia and by muscle in "
            "the wall. Only one of the two gametes needs its own propulsion, "
            "and it is the cheap one."},
    {"id": "mito",
     "name": "Mitochondria",
     "sperm": "Many, packed behind the head",
     "egg": "Many — and these are the ones you inherit",
     "why": "The sperm’s mitochondria release energy for swimming and are "
            "destroyed after fusion. Every mitochondrion in your body came "
            "from the egg."},
    {"id": "food",
     "name": "Food store",
     "sperm": "Almost none — it uses sugar in the fluid around it",
     "egg": "A large store in the cytoplasm",
     "why": "The fertilised egg has to survive several days of dividing before "
            "it implants and can be supplied. Everything it spends in that "
            "time was loaded before fertilisation."},
    {"id": "chrom",
     "name": "Chromosomes",
     "sperm": "23 — half a set",
     "egg": "23 — half a set",
     "why": "The one row where the two are identical. Half a set is only "
            "useful if it is going to be added to another half — which is why "
            "a gamete cannot live independently."},
    {"id": "number",
     "name": "Numbers",
     "sperm": "Hundreds of millions at a time",
     "egg": "One at a time, about 400 in a lifetime",
     "why": "A direct consequence of cost. Something cheap to make can be made "
            "in vast numbers and mostly wasted; something expensive cannot."},
]

# ── the scale panel inside the same section (page lines 492–497, 165) ────
#
# ⚠️ `pct` is Design's own bar width, not a derived one: 100% against 5%, which
# IS 0.005/0.1 to scale. There is no clamp and none is wanted — unlike b4-01's
# gas bars, both figures are large enough to draw honestly, and the whole point
# of the panel is that the smaller bar looks as small as it really is. The
# closing note is what stops the bars being read as volumes.
SCALE = {
    "label": "Relative diameter, to scale",
    "rows": [
        {"id": "egg", "name": "Egg cell", "size": "0.1 mm across", "pct": 100},
        {"id": "sperm", "name": "Sperm cell head", "size": "0.005 mm across",
         "pct": 5},
    ],
    "note": "Those bars are diameters. Because volume goes as the cube of the "
            "diameter, a twentyfold difference in width is roughly an "
            "eight-thousandfold difference in volume — and the egg’s cytoplasm "
            "is where nearly all of that sits.",
}

# ── the five steps (page lines 352–363) ─────────────────────────────────
#
# `where` is joined to `name` with " · " — see "What could not be lifted" 2.
# The `what` prose is untouched. The `01`–`05` chips are dropped; the ORDER is
# what carries the sequence, and §8.10's "sequence is data" is honoured by the
# list being a list rather than by a numeral being typed into a sentence.
STEPS = [
    ("Release", "Ovary → oviduct",
     "One mature egg cell leaves an ovary and enters the oviduct, where cilia "
     "and muscle begin moving it along. It remains able to be fertilised for "
     "roughly a day."),
    ("Transfer and travel", "Vagina → uterus → oviduct",
     "Semen is transferred into the vagina. Sperm swim through the cervix and "
     "uterus into the oviduct — a journey of several inches for a cell 0.005 "
     "mm long. Hundreds of millions set out; a few hundred arrive."),
    ("Fertilisation", "Oviduct — and nowhere else",
     "One sperm passes through the egg’s outer layer and its nucleus fuses "
     "with the egg’s nucleus. 23 plus 23 makes 46. The outer layer then "
     "changes so no other sperm can enter. This step, and only this step, is "
     "fertilisation."),
    ("Dividing", "Travelling down the oviduct",
     "The single fertilised cell divides into two, then four, then eight, over "
     "about five days, while still travelling. It is a ball of cells before it "
     "has arrived anywhere."),
    ("Implantation", "Uterus lining",
     "The ball of cells embeds itself in the thickened lining of the uterus, "
     "where it can be supplied. This is a separate event from fertilisation, "
     "several days later and in a different organ — and it is where pregnancy "
     "begins."),
]

STEP_CARDS = [{"term": "%s · %s" % (name, where), "gloss": what}
              for name, where, what in STEPS]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 123 character for character. Slugs are
    # permanent (§8.4).
    "slug":        "gametes-and-fertilisation",
    "title":       "Gametes and fertilisation",
    "discipline":  "biology",
    "unit":        "reproduction",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # The `b` clause of the split bullet. See the docstring; a, c, d and e
    # belong to the other four human lessons.
    "covers":      ["KS3.B.REP.01b"],
    # Named but not taught. The comparison names cytoplasm, mitochondria and
    # the nucleus and says what each is FOR (B1's CELLS.02 owns them), and the
    # chromosome row and the Going further layer both talk about genetic
    # information passing between generations (B10's INH.01 owns that).
    "touches":     ["KS3.B.CELLS.02", "KS3.B.INH.01"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "structure-function", "level": 2},
                    {"id": "genes-and-evolution", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 50,

    # ── progression edges ───────────────────────────────────────────────────
    # No `requires`: Design draws no "Before this lesson" card and the engine
    # omits an empty one. Her forward link and both sideways links live in the
    # middle card — see "What could not be lifted" 5.
    "requires":    [],
    "assumes":     [],
    "references":  ["the-menstrual-cycle",
                    "human-reproductive-systems",
                    {"unit": "B1", "lesson": "specialised-cells"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Meiosis, sexual and asexual reproduction compared, and "
                   "inherited variation.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Two cells fuse and become one. Each brought half a set of "
                    "instructions; neither brought anything like half the "
                    "material.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # THREE stops. Design draws four; `s-fert` is dropped — see the docstring.
    # `short` and `label` are Design's own `RAIL_SHORT` and `RAIL` strings
    # (page lines 329–335).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Unequal sizes",
         "done_when": "committed"},
        # Design's own threshold, kept: the stop ticks when all six rows have
        # been opened (`Object.keys(s.open).length >= 6`, page line 410). A
        # stop that ticked on the first row would call the table finished at a
        # sixth of it.
        {"anchor": "s-compare", "short": "CELLS", "label": "Two cells",
         "done_when": "all_six_rows_opened"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3). Option A is the
    # wrong idea `REPRO-18` names, and it is the reason the hook exists.
    "phenomenon": {
        "kind": "narrative",
        "title": "An egg cell has several thousand times the volume of a sperm "
                 "cell.",
        "prompt": "An egg is around 0.1 mm across — just visible without a "
                  "microscope, the largest cell in the human body. A sperm’s "
                  "head is about 0.005 mm. They contribute exactly the same "
                  "number of chromosomes: twenty-three each.",
        "commit": "Equal instructions, wildly unequal size. Where has all the "
                  "extra gone?",
        "options": [
            "The egg carries more copies of the chromosomes",
            "The egg carries cytoplasm, mitochondria and a food store",
            "The sperm loses most of itself on the journey",
            "The egg is bigger because it is older",
        ],
        "reveal": "Into everything the new organism needs for its first few "
                  "days: cytoplasm, mitochondria, a food store, and all the "
                  "machinery for building a body. The sperm brings chromosomes "
                  "and a means of arriving. Equal genetic contribution, "
                  "radically unequal material contribution — and both of those "
                  "facts matter.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    #
    # ⚠️ The `REPRO` family is NOT yet in `docs/ks3/misconception-register.md`
    # — NOTES-B5 §5 mints seventeen for this unit and the commander maintains
    # the register centrally. THREE ids are used here and their allocation was
    # pinned before authoring, because five parallel authors collided on B4's
    # family: this module owns `REPRO-03` and `REPRO-04` and nothing else, and
    # the third belief it confronts takes `REPRO-18` — the eighteenth entry,
    # one past the seventeen NOTES-B5 §5 declares.
    #
    # ⚑ `REPRO-18` IS NEW AND IS FLAGGED. NOTES-B5 does not list it: the unit's
    # notes count seventeen entries and this lesson's third wrong idea is not
    # among them. It is minted here because the hook is BUILT on it — option A
    # is the belief stated in a student's own words, rung 2's first distractor
    # states it again ("Extra copies of the chromosomes, in case some are
    # damaged"), and the `chrom` comparison row exists to kill it. A belief a
    # page elicits twice and confronts three times is a register entry by the
    # register's own rule, and leaving it unminted would make the hook's whole
    # commitment invisible to the tutor prompt (§5.9).
    #
    # `elicited_by` is honest per entry. `REPRO-18` really is surfaced before
    # it is answered — the student commits to a cause for the size difference
    # before any of it is explained. `REPRO-03` and `REPRO-04` are not asked
    # for anywhere before the block that kills them, so the block is named for
    # both; b3-05, b4-01 and b4-05 use the same pattern.
    "misconceptions": [
        {"id": "REPRO-03",
         "statement": "Fertilisation is when the sperm reaches the egg.",
         "elicited_by": "two-wrong-ideas",
         "confronted_by": "two-wrong-ideas"},
        {"id": "REPRO-04",
         "statement": "Identical twins happen when two eggs are fertilised.",
         "elicited_by": "two-wrong-ideas",
         "confronted_by": "two-wrong-ideas"},
        {"id": "REPRO-18",
         "statement": "The egg is bigger than the sperm because it carries "
                      "more genetic material.",
         "elicited_by": "hook",
         "confronted_by": "two-cells"},
    ],

    # Design draws no keyword block anywhere in B5, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list — which matters here,
    # because "gamete", "fertilisation", "oviduct" and "implantation" would
    # otherwise all count against the page.
    #
    # ⚠️ Every definition is COMPOSED FROM THIS PAGE'S OWN SENTENCES — the key
    # note defines `gamete` and `fertilisation` almost verbatim and steps 1 and
    # 5 define `oviduct` and `implantation` in the course of using them. No
    # anatomical claim has been invented here, which on this unit is a tone
    # decision as much as an accuracy one. `cytoplasm`, `mitochondria` and
    # `chromosome` are deliberately NOT redefined: they are B1's vocabulary and
    # this lesson `touches` CELLS.02 rather than teaching it.
    "vocabulary": [
        {"term": "gamete",
         "definition": "A sex cell with half a set of chromosomes — 23 in "
                       "humans.",
         "note": "Half a set is only useful if it is going to be added to "
                 "another half, which is why a gamete cannot live "
                 "independently."},
        {"term": "fertilisation",
         "definition": "The fusion of the nucleus of a sperm with the nucleus "
                       "of an egg, producing a single cell with 46 "
                       "chromosomes.",
         "note": "It happens in the oviduct, and everything before and after "
                 "it is a different step with a different name."},
        {"term": "oviduct",
         "definition": "The tube an egg cell travels along after leaving an "
                       "ovary, moved by cilia and by muscle in the wall.",
         "note": "Also called the fallopian tube. Fertilisation happens here "
                 "and nowhere else."},
        {"term": "implantation",
         "definition": "The ball of cells embedding itself in the thickened "
                       "lining of the uterus, where it can be supplied.",
         "note": "A separate event from fertilisation, several days later and "
                 "in a different organ."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # Design's legal line names exactly ONE slot on this page and no artwork
    # exists for it, so it is DECLARED at `needed` rather than dropped: the
    # manifest is generated from this field, which turns a dangling reference
    # into a tracked sourcing task. `needed` is not a build blocker. No
    # `figure` block is added to `core` — Design draws no figure slot on the
    # page, and one here would be a component nobody drew. The caption
    # describes only what this lesson already teaches in words, and stops
    # there: NOTES-B5 flag 13 asks that the level of detail in the human slots
    # be ruled on before anything is commissioned.
    "figures": [
        {"id": "b5-gametes-labelled",
         "kind": "diagram",
         "caption": "A sperm cell and an egg cell drawn to the same scale and "
                    "labelled: the sperm’s head, mitochondria and tail, and "
                    "the egg’s nucleus, cytoplasm, food store and outer layer, "
                    "with each cell’s diameter given — about 0.005 mm and "
                    "about 0.1 mm.",
         "status": "needed"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-compare — the flagship, authored inline and lifted into
        # activities[] by ks3_data/b5/__init__.py::_normalise, which leaves the
        # `practical` shell behind it. Design's block is
        # `ks3-block ks3-dark ks3-practical` (page line 114), so the segment is
        # measured and not inherited.
        #
        # ⚖️ GATED, NOT OPEN ON LOAD. `rows_open_on_load` is False and every
        # `why` is behind its own row. See the docstring — Design's `open: {}`
        # and her `<sc-if value="{{ row.open }}">` are what this reproduces,
        # and the counter reading "0 of 6 opened" on arrival is the contract
        # stated on the page.
        {"type": "gamete-compare", "id": "two-cells", "anchor": "s-compare",
         "demand": "investigate",
         "eyebrow": "Two specialised cells · six features",
         "heading": "Every difference has a reason",
         "head_counter": {"format": "{n} of 6 opened", "total": 6},
         # The inline link to b1-04 is dropped and every word kept — see "What
         # could not be lifted" 4.
         "prompt": "These are the specialised cells from Specialised cells, "
                   "doing the clearest job in the body. Tap a row to see why "
                   "each cell has what it has.",

         # The three column headings. They are also the per-cell captions below
         # 880px, where the header row hides (page lines 24–29), so a stacked
         # row still says which cell it came out of.
         "columns": {"feature": "Feature",
                     "sperm": "Sperm cell",
                     "egg": "Egg cell"},

         "rows": CMP,
         "rows_open_on_load": False,
         "why_label": "Why:",

         # The panel below the table, inside the same section.
         "scale": SCALE},

        # #s-fert — the band panel. NOT on the rail; see the docstring.
        # `rule` is the component: band ground, 3px ink border, an accent-text
        # eyebrow and a display statement, then a card grid on the option
        # border — Design's markup (page lines 169–186) minus the number chips
        # and step 3's promotion.
        {"type": "rule", "anchor": "s-fert",
         "eyebrow": "The process, in order",
         "statement": "Five steps, and only one of them is fertilisation.",
         "cards": STEP_CARDS},

        # Design nests this inside `#s-fert`; `r_rule` has no nested slot, so it
        # renders directly under the panel in document order. See "What could
        # not be lifted" 3.
        {"type": "key-fact", "ref": "fertilisation-is-fusion"},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "REPRO-03"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # One per lesson, and amber is reserved for misconceptions (README).
    "key_facts": [
        {"id": "fertilisation-is-fusion",
         "text": "Fertilisation is the moment the nucleus of a sperm fuses "
                 "with the nucleus of an egg, forming a single cell with a "
                 "full set of chromosomes. It happens in the oviduct, and "
                 "everything before and after it is a different step with a "
                 "different name.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`, and an authored statement wins over the register. The
        # block asks for no commitment, on Design's page and here, so it is not
        # a rail stop and emits no completion contract.
        #
        # ⚠️ The literal asterisks around *reaches* and *fuses* are Design's,
        # in a paragraph that also uses real `<em>` tags. Lifted as drawn — see
        # finding B in the docstring.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "REPRO-03",
         "statements": [
             {"quote": "Fertilisation is when the sperm reaches the egg.",
              "body": ["Arriving is not fertilising. Many sperm reach the egg "
                       "and touch its surface; fertilisation is the single "
                       "event in which one sperm’s nucleus fuses with the "
                       "egg’s nucleus, and it happens once. The distinction is "
                       "not fussiness — the moment of fusion is what triggers "
                       "the egg to change its outer layer so that no second "
                       "sperm can enter, and it is what produces the full set "
                       "of forty-six chromosomes. Use *reaches* and you have "
                       "described a crowd; use *fuses* and you have described "
                       "the event. The same care applies to the words either "
                       "side of it: <em>implantation</em> is a different step, "
                       "days later and in a different organ, and "
                       "<em>pregnancy</em> begins there rather than at "
                       "fertilisation."]},
             {"quote": "Identical twins happen when two eggs are fertilised.",
              "body": ["That is the recipe for non-identical twins, and it is "
                       "worth having both straight because the two arise at "
                       "completely different moments. Non-identical twins: two "
                       "eggs released, two sperm, two separate fertilisations "
                       "— two ordinary siblings who happen to share a "
                       "pregnancy, and they can be different sexes. Identical "
                       "twins: <em>one</em> egg, <em>one</em> sperm, one "
                       "fertilisation — and then, within the first fortnight, "
                       "the ball of cells splits in two and each half "
                       "continues as a whole embryo. Same chromosomes in both, "
                       "always the same sex. Notice what that means: identical "
                       "twins are not caused by anything about the gametes at "
                       "all. The cause happens after fertilisation is over."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED, AND RUNG 1 FAILS. See finding A in
    # the docstring.
    #   rung 1 (recall): correct 12w against distractors of 7 / 8 / 7 — gap 4,
    #           ratio 1.50. A TELL on both limbs of the heuristic.
    #   rung 2 (apply):  correct 13w against distractors of 10 / 10 / 9 —
    #           gap 3, ratio 1.30. Clean.
    # No distractor was rewritten. The copy is Design's, the tell is Design's,
    # and repairing it would change what a marked question measures — Mide's
    # gate, not an author's.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Define it precisely",
            "q": "Which of these is fertilisation?",
            "options": [
                "A sperm cell reaching the egg cell",
                "The nucleus of a sperm fusing with the nucleus of an egg",
                "The fertilised egg embedding in the uterus lining",
                "The egg being released from the ovary",
            ],
            "answer": 1,
            "feedback": {
                0: "Many sperm reach the egg. Reaching describes a crowd "
                   "arriving; fertilisation is one specific event.",
                2: "That is implantation, several days later and in a "
                   "different organ. Two different events with two different "
                   "names.",
                3: "That is release, and it happens whether or not any sperm "
                   "are present.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A sperm and an egg each carry 23 chromosomes, but an egg has "
                 "thousands of times more material. What is the extra material "
                 "for?",
            "options": [
                "Extra copies of the chromosomes, in case some are damaged",
                "Cytoplasm, mitochondria and a food store for the first few "
                "days of dividing",
                "It makes the egg easier for the sperm to find",
                "Nothing in particular — egg cells are simply bigger",
            ],
            "answer": 1,
            "feedback": {
                0: "There are no spare copies. Exactly 23 in each, and the "
                   "fertilised cell has exactly 46.",
                2: "Size does help the sperm locate it, but that is a side "
                   "effect. The material is there for what happens after "
                   "fusion, not before.",
                3: "Every feature of both gametes has a reason. That is the "
                   "point of the comparison table.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the two designs",
            "q": "Explain why a sperm cell is small with a tail and many "
                 "mitochondria, while an egg cell is large and immobile with a "
                 "food store. Say what each is specialised for, and name the "
                 "one feature they share.",
            "field_label": "Your explanation",
            "placeholder": "A sperm is specialised for… an egg is specialised "
                           "for…",
            "success": [
                "Says the sperm is specialised for travelling — small, tail, "
                "mitochondria for energy.",
                "Says the egg is specialised for supplying the first days of "
                "development — cytoplasm and food store.",
                "Explains why the egg does not need to move: it is carried by "
                "cilia and muscle.",
                "Names the shared feature: each carries 23 chromosomes, half a "
                "set.",
                "Connects the number of each gamete to how expensive it is to "
                "make.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A student says identical twins must come from two eggs, "
                 "because there are two babies. Say whether they are right, "
                 "explain what actually causes each kind of twin, and give one "
                 "observation that would tell the two kinds apart.",
            "field_label": "Your answer",
            "placeholder": "They are describing…",
            "success": [
                "Says they have described non-identical twins: two eggs, two "
                "sperm, two fertilisations.",
                "Says identical twins come from one egg and one sperm, with "
                "the ball of cells splitting after fertilisation.",
                "Makes clear that the cause of identical twins happens after "
                "fertilisation, not in the gametes.",
                "Gives a usable observation — identical twins always share the "
                "same sex and the same chromosomes; non-identical twins need "
                "not.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A gamete is a sex cell with half a set of chromosomes — 23 in "
                "humans. Sperm are small, mobile and numerous; egg cells are "
                "large, immobile and few, and carry the food store and "
                "cytoplasm. Fertilisation is the fusion of the two nuclei, in "
                "the oviduct, producing a single cell with 46 chromosomes. It "
                "divides as it travels and implants in the uterus lining "
                "several days later.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # NOTES-B5 flag 9. It ends on a claim about human ancestry rather than on a
    # claim about anyone's family, which is the tone rule doing work: the
    # sentence is about mitochondrial DNA, not about mothers.
    "stretch": [
        {"type": "explainer", "id": "a-clock-in-the-packing-material",
         "text": "Every mitochondrion in your body came from your mother. The "
                 "egg supplies all the cytoplasm and everything in it; the "
                 "sperm’s few mitochondria power its journey and are destroyed "
                 "after fusion. Mitochondria carry a small loop of their own "
                 "DNA, so that DNA passes down an unbroken line of mothers — "
                 "and because it is not shuffled with anything each "
                 "generation, it changes only by slow mutation. That makes it "
                 "a clock. Comparing mitochondrial DNA across living humans "
                 "traces every one of us back to a common maternal ancestor in "
                 "Africa, and it is how the deep structure of human migration "
                 "was worked out before anyone could sequence a whole genome. "
                 "A cell’s leftover packing material turned out to be the "
                 "archive."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The tutor card points at `#s-fert`, which is the section that came off
    # the rail and kept its anchor. That link is the reason the anchor stays.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check the difference between reaching and "
                      "fusing?",
              "cta": "Ask about this lesson",
              "anchor": "s-fert"},

    # ⊕ MRB-228's `convention_note`, not `safety_note` — see finding D in the
    # docstring. Design draws ONE plain `.ks3-legal` paragraph at the bottom
    # edge and nothing in it is a safety instruction: it is a note about how
    # the two figures on this page were taken, a scope signpost to RSE and
    # PSHE, and a declaration about a diagram that has not been drawn yet.
    #
    # ⚠️ The figure id keeps its plain text; Design sets it in mono inside the
    # sentence and a foot line is escaped, so the id renders in body copy and
    # the words are unchanged.
    "convention_note": "Cell sizes are typical values: egg about 0.1 mm "
                       "diameter, sperm head about 0.005 mm. This is the "
                       "biology of the cells and the process; relationships "
                       "and consent are covered in your RSE and PSHE lessons. "
                       "The labelled gamete diagram is declared in the lesson "
                       "record as b5-gametes-labelled, awaiting illustration.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The instrument is read-the-evidence-then-reason: six paired observations
    # opened one at a time, each with the reason it takes, closing on a scale
    # argument the student has to carry from diameter to volume.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
