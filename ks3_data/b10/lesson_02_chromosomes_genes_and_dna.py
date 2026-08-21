"""B10 L2 — Chromosomes, genes and DNA (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b10/b10-02-chromosomes-genes-and-dna.dc.html` (556 lines), her
author's notes `docs/ks3/design-reference/b10/NOTES-B10.md`, and the B10 payload schema
`docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md` §0, §1, §3, §7, §8, §9, §10, §11, §12, §13,
§14, §15 and §16, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page except the
three listed under "What could not be lifted" and the three rung-2 distractors rewritten
under MRB-177, each of which is recorded below with its before and after. The six zoom
levels, the four say-it-back questions, the four model cards, both marked rungs and both
self-marked rungs came out of the page's own `LEVELS`, `QUIZ`, `MODEL_CARDS`, `RUNGS` and
`SELF_RUNGS` arrays via `tools/extract_design_payload.js`, not off a keyboard.

── `covers` is one clause, and the unit's other lesson owns the other ──

`KS3.B.INH.02` reads, in full: *a simple model of chromosomes, genes and DNA in heredity,
including the part played by Watson, Crick, Wilkins and Franklin in the development of the
DNA model*. `ks3_data/substatements.py` splits it at the comma that separates the model
from the people: `02a` is *a simple model of chromosomes, genes and DNA in heredity, and
how the four nest inside one another*, and that is this page whole — the bench nests them,
`#s-model` names them, and rung 1 marks the ordering. `02b` — the part played by the four
scientists — is b10-03's and is not touched here. `build_ks3.validate()` enforces
exactly-once ownership, so a second claim would fail the build rather than quietly double
up.

── THE INSTRUMENT: SIX LEVELS, AND THE SCALE COLUMN IS THE ARGUMENT ────

`#s-bench` is `zoom-bench`, on `ks3-block ks3-dark ks3-practical` (page line 106), so
`practical` is MEASURED from Design's own class attribute rather than inferred from the
kind name — payload schema §0 rule 2, and contract §4 records that B1 got two of six wrong
by inferring it.

⚖️ **THE SIX LEVELS ARE THE PAGE'S, NOT THE NOTES'.** Schema §3.1 quotes the scale column
verbatim precisely because a retyped zero in row 6 would be invisible and wrong, and the
six `name`/`scale` pairs below are that table character for character:

    1  A person       1.6 m
    2  A cell         0.02 mm
    3  The nucleus    0.006 mm
    4  A chromosome   0.002 mm long
    5  A gene         a section of the strand
    6  The bases      0.0000003 mm apart

⚠️ **ROW 5 PRINTS NO NUMBER AND ROW 5 IS NOT `DNA`.** Both are measured, and both are
things a careful author will want to "fix":

  * **Row 5 has no figure** because a gene has no characteristic length, and Design says so
    in words instead. Do not complete the column.
  * **Level 5 is `A gene` and level 6 is `The bases`.** `NOTES-B10 §1.2` and the dispatch
    brief both describe the ladder as ending at *DNA* and *a base pair*; schema §10 item 1
    records that the NOTES line is the one that is wrong. The page is internally consistent
    with its own choice — its own bottom-out paragraph reads *"the last four are all the
    same molecule seen at different magnifications"*, which is true of chromosome, gene and
    bases and would be false of a list that put DNA beside them as a fifth separate thing.
    The page wins on measurement. `A gene` and `The bases` are what ship.

── ⚑ THE THOUSANDFOLD CLAIM, CARRIED AND NOT RESOLVED (schema §10 item 2) ──

The bench lead says the scale *"drops by roughly a factor of a thousand at every step"*.
Worked from the figures the same block prints, four steps are measurable and not one of
them is a thousandfold:

    1.6 m      → 0.02 mm       ×80,000        (~10⁵)
    0.02 mm    → 0.006 mm      ×3.3
    0.006 mm   → 0.002 mm      ×3
    0.002 mm   → (a gene)      no figure printed
    (a gene)   → 0.0000003 mm  ×~7,000

**Both the sentence and the figures are lifted byte-identical and neither is touched.**
The sentence is Mide's to rule on: NOTES flag 5 asks him to confirm the figures but says
nothing about the claim made over them, so the contradiction has never been put in front of
him. Raised in the report. ⚑ It lands in exactly ONE string — the bench `prompt` — and
nothing else in the lesson depends on it: the key fact, the key note, the close and all
four rungs argue from NESTING, never from a ratio. Whichever way he rules, one line moves.

⚠️ **THE EYEBROW SAYS FIVE AND THE PANEL HAS SIX, AND THAT IS CORRECT.** *"At the bench ·
zoom in five times"* over six levels is consistent arithmetic — six levels, five presses of
the button, and the progress line reads *"all six levels"* — but the two numbers sit four
lines apart and read as a contradiction. Schema §10 item 4 exists so that a later pass does
not "correct" the five into an error. Lifted as drawn.

⛔ **NO RUNTIME STATE IS AUTHORED** (schema §0 rule 3). Design's state bag holds `shown`
and `quiz`; both are the runtime's, and under R5 a key with no read site fails
`ks3_key_audit.py`. The single exception is `opens_on`, and it is authored for the reason
§3.2 gives and no other: `state.quiz` opens on `'contains'`, which is `questions[1]` and
not the first. That is a teaching choice — *"What contains what?"* is the question that
states the whole nesting, so the panel opens already saying the thing the bench is for —
and omitting the key would silently open the page on *"Which is the longest?"* instead.

⊖ **The say-it-back panel is NOT a second activity.** Measured: it is inside
`<section id="s-bench">` (page lines 141–152), not a block of its own, so it is part of
this payload. It gates nothing and marks nothing — the answer for the selected question is
always visible — which is why it authors no `answer` index and no feedback.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ────────────────

Design draws four (page lines 307–312) and her `isDone()` gives `s-model` the BENCH's
predicate, character for character, one section to the left:

    if (id === 's-bench') return s.shown >= LEVELS.length;
    if (id === 's-model') return s.shown >= LEVELS.length;      // page line 508

`#s-model` is an eyebrow, a display statement, four static cards and a key fact: no
control, no commitment, no field, no reveal. It is the PAYOFF of the bench beside it, and
it carries no control precisely because the bench has already taken the student's
commitment. That relationship is a MIRROR, `wireRail`'s `paint()` resolves it at rail
level — which is the level Design computes it at — and
`ks3_parity.check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`, where this page's row reads
`s-hook s-bench s-model s-ladder | s-model=s-bench`.

⚠️ Payload schema §8's tables are correct as MEASUREMENT and its instruction to *author
three stops and drop the band* is REVERSED at the head of the same section, and the struck
paragraph below that reversal is explicitly NOT what to build. Four is what Design drew and
four is what ships. Shipping three fails the build.

`#s-think` and `#s-keynote` are on no rail, and that is Design's too: `#s-keynote` asks
nothing, and `#s-think` here is static markup — two quotes, two bodies, no options, no
reveal, no button — so it is a `confrontation` and not contract R1's `predict`. Schema §9,
measured on all five B10 pages.

── What could not be lifted byte-identical, and why ────────────────────

All three are build-internal slot codes. **No science word moves in any of them**, and
every one of the three destinations survives on the page.

1. **`b1-05` in `#s-think`'s first body.** Design writes *"the levels-of-organisation
   ladder from b1-05 is the right way to hold it"*, with `b1-05` as the anchor TEXT. A
   student cannot resolve a slot code, and printing one is exactly the platform leakage
   §8.10 exists to stop. `rich()` allows `<em>` and `<strong>` and nothing else, so the
   anchor tag goes in any case.

   b9-01 resolved the identical shape to the target's TITLE — *"the photosynthesis you met
   in b7-04"* → *"… in Why almost all life depends on it"* — and that worked because the
   title and the surrounding noun phrase were different words. **Here they are the same
   words**: the target's title is *Levels of organisation* and the sentence already says
   *the levels-of-organisation ladder*, so resolving produces *"the levels-of-organisation
   ladder from Levels of organisation"*, which reads as a defect on a live page. So the
   POINTER is cut and every teaching word kept:

       Design:  the levels-of-organisation ladder from b1-05 is the right way to hold it
       Built:   the levels-of-organisation ladder is the right way to hold it

   The destination is not lost — `levels-of-organisation` is Design's own second *Before
   this lesson* card and is carried in `requires`, so the link a student would have
   followed is on the same page, one section down.

2. **`b1-04` in `#s-think`'s second body**, and the same stutter for the same reason: the
   target's title is *Specialised cells* and the clause already says *the specialised
   cells*. Pointer cut, teaching kept:

       Design:  which is the mechanism behind the specialised cells you met in b1-04.
       Built:   which is the mechanism behind the specialised cells.

   `specialised-cells` is Design's own second *Connects to* card and is carried in
   `references`, so this destination is on the page too.

3. **`b10-01` in the legal line.** Design writes *"as b10-01's height curve already
   implied"*. This one is NOT cut, because b10-01 is the one of the three destinations that
   is neither a *Before this lesson* card nor a *Connects to* card — cutting the pointer
   would lose it entirely, and Design drew exactly two cards per list so a third cannot be
   added (MRB-205). Resolved to the title, recast from possessive to prepositional so that
   a title carrying a colon reads:

       Design:  as b10-01's height curve already implied
       Built:   as the height curve in Variation: continuous and discontinuous already
                implied

   Every word of the science claim in front of it is untouched.

⚠️ No sequence leak to repair on this page: `year`, `Year` and `half-term` appear zero
times in Design's bytes, checked rather than assumed.

── ⊕ MRB-177 LENGTH PARITY — RUNG 1 CLEAN, RUNG 2 REPAIRED ─────────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags a correct
option that is strictly the longest AND clears the longest distractor by ≥4 words or by
≥1.4×.

    rung 1  correct  4w vs  4 /  4 /  4  — not strictly longest      ✓ as drawn
    rung 2  correct 21w vs 12 /  6 / 10  — gap 9, ratio 1.75         ✗ TRIPPED
    rung 2  correct 21w vs 22 / 21 / 21  — not strictly longest      ✓ repaired

**Rung 1 is Design's, untouched, and it could not have needed touching.** All four options
are the same four nouns in four different orders — four words each, by construction — so
the rung is length-blind and a student has nothing but the nesting to go on. That is the
construct MRB-177 asks for, arrived at by the question's own shape.

**Rung 2 tripped both arms at once** and it is the construct MRB-177 named, exactly:
Design's correct option states a RULE with two branches (every cell with a nucleus has the
complete set; only some genes are switched on in each) while all three distractors stated a
one-clause wrong LOCATION — *"Only if you have brown eyes"* is six words. The correct
answer was therefore longer BY CONSTRUCTION, and a student could have scored the rung
without reading it.

Each distractor is rewritten as a WRONG RULE in the correct answer's own shape — where the
genes are, and what follows from their being there — keeping Design's clause verbatim at
the front and gaining the consequence the belief licenses:

    r2 A  No — that gene is only in the cells of the eye
          + ", so each cell carries only the genes its organ uses"     12w → 22w
    r2 C  Only if you have brown eyes
          + ", because a gene for a characteristic is only present in
             the people who show it"                                    6w → 21w
    r2 D  No — genes move to the organs that need them
          + ", so a gene ends up in whichever cells are using it"      10w → 21w

**The correct option is unchanged, `answer: 1` is unchanged, Design's option ORDER is
unchanged, and all three of her corrections are byte-identical.** Each still answers exactly
the belief its rewritten distractor states, and two of the three now land harder:

  * A now ends on *each cell carries only the genes its organ uses*, and the correction's
    second sentence is *"Nothing sorts them out by destination"* — which is that rule
    denied, in the same words.
  * D now says a gene ENDS UP where it is needed, as a rule, and the correction's "Genes
    cannot move. They are sections of the chromosomes, which stay in the nucleus of their
    own cell" contradicts precisely that.

⚖️ **The four options now run 22 / 21 / 21 / 21, so the correct answer is joint-shortest
and there is no tell in either direction.** That was deliberate: padding the distractors
well past the correct answer would trade one tell for its mirror image, which a class works
out just as fast.

⚑ For Mide's science gate — every NOTES-B10 flag landing on THIS lesson, and what was
  checked against it. Three flags, three checked, **none corrected**:

  * flag 5   **"Two metres of DNA per cell", nucleus ~0.006 mm.** CHECKED AND LEFT. The two
             metres is printed three times on the page and all three agree (hook heading,
             hook prompt, say-it-back answer `longest`); the nucleus figure is printed
             twice, in two notations, and they agree (hook prompt *"around six thousandths
             of a millimetre across"*, level 3 `scale` `0.006 mm`). Both are the standard
             rounded teaching figures — ~2 m of DNA per diploid human cell and a nucleus of
             roughly 5–10 µm — and the legal line already says the scale figures are
             rounded to the nearest order of magnitude. ⚑ **What this flag does NOT cover is
             the thousandfold sentence written over those figures.** See the section above;
             that is the finding, and it is new to Mide.

  * flag 6   **"Around twenty thousand genes"**, the Human Genome Project surprise, and the
             chromosome-count comparisons (chimp 48, potato 48, dog 78, a fern over a
             thousand). CHECKED AND LEFT. Current human protein-coding gene estimates sit
             at roughly 19,000–20,000, and pre-project estimates in the tens of thousands
             up to ~100,000 are well documented. Chimpanzee 48 and dog 78 are right; potato
             is 48 (tetraploid, 4n = 48) and Design says *"a potato 48"* without claiming
             it is a diploid count, which is the honest form of it; *Ophioglossum* ferns
             exceed a thousand chromosomes. *"A water flea has more genes than you do"* is
             right — *Daphnia pulex* runs to about 31,000. The paragraph's argument is that
             the COUNT is the wrong thing to look at, and every figure in it serves that.

  * flag 7   **"One gene, one characteristic" as the working model.** CHECKED AND LEFT, AND
             THE HEDGE IS LOAD-BEARING. The page states the simplification in three places
             — level 5's *"the instruction for one characteristic"*, `#s-model`'s statement
             *"A gene is an instruction for one job."* and the `Gene` card's *"codes for
             one characteristic"* — and then retracts none of it while the legal line names
             it as a deliberate simplification and gives both directions of the real
             picture (many genes per characteristic, many characteristics per gene). That
             is MRB-225 performed in the drawing: the claim is stated at the size KS3 can
             use, and the honest correction sits where a student can find it rather than
             being smuggled into the body. **The one thing that must not happen is a later
             pass "tidying" the legal line** — it is the only place the simplification is
             admitted.

  * flag 19  **No diagrams anywhere in B10, and a chromosome-to-DNA nesting figure is one
             of the two obvious candidates.** MEASURED on this page rather than assumed:
             `<img>`, `<figure>` and `<picture>` each appear ZERO times, and every `<svg>`
             is the nav chevron, the rail tick, a ladder tick/cross or an endmatter arrow.
             `figures` is therefore empty per schema §11, which also records why: **this
             lesson's `zoom-bench` IS the nesting figure**, built out of DOM — six levels,
             each inside the last, with the scale on every one. Declaring a figure slot the
             page never references would invent a sourcing task in
             `docs/ks3/diagram-manifest.md` for a drawing the bench already is. The flag is
             not dropped by this and it is Mide's to rule on; the other candidate, Photo
             51, is b10-03's and carries a rights question that is his and not this build's.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes seven times: *these are not four things, they are one
thing at four magnifications*. The hook's reveal ("A chromosome is not a different
substance from DNA. It is DNA, packed."), level 5's body ("Not a separate object attached
to the chromosome — a part of it"), the bench's close ("the last four are all the same
molecule seen at different magnifications"), `#s-think`'s first body ("one thing described
at three magnifications"), the key fact, rung 3's fourth criterion and the key note all say
the same thing at the same size. The stretch layer adds the chromosome-count and gene-count
argument and retracts nothing above it.

── Misconception ids: GENE-03 and GENE-04, and the spare is untouched ──

Schema §12 pre-allocates `GENE-03` and `GENE-04` to this lesson before any author starts,
with `GENE-12` as the named spare, for a concurrency reason and not a generosity one: five
authors work five files at once and none can see the others, so "mint the next free id"
mints the same id five times. **Exactly two beliefs are confronted on this page** — the two
`.ks3-mis-quote` runs in `#s-think`, and there is no third anywhere — so `GENE-12` is
claimed by nothing here and stays permanently unused, in the same class as `DRUG-07`.

⚠️ **The `GENE` prefix row does not yet exist in `docs/ks3/misconception-register.md`.**
`NOTES-B10 §4` states its ten entries were "written into" the register with a new prefix
row; schema §12's standing note records that four deliveries have now said that and none of
them did it, and that a §4 is to be read as an allocation PROPOSAL. **That file is not this
pass's to edit** (contract §0 — it is another agent's this run), so the two statements are
authored here in register voice, byte-identical to Design's own quoted beliefs, and are
reported for whoever opens the row. No gate resolves an id against the register file, so
the lesson builds either way; what is at risk is the register's completeness.

Both values in each row resolve against the BUILT page (MRB-244, gated): `s-think` is the
confrontation block's emitted anchor and `s-ladder` is the ladder's. `s-ladder` is the
honest `elicited_by` for both — rung 1's options C and D are `GENE-03` stated in the
student's own words (a gene ordered outside the chromosome that contains it), and rung 2's
option A is `GENE-04` stated in the student's own words. The ladder is the only place on
this page where either belief is offered as something to COMMIT to: the hook's four options
are about how two metres fits into a nucleus and carry neither belief, and the bench shows
the nesting and asks for no verdict.

── Keys this pass authors that the RENDERER reads (contract R5) ────────

Named explicitly rather than left to be discovered. Every one is schema §3's shape:

    levels        six ordered outermost → innermost; name, scale, body
    in_label      / in_done_label → the zoom button's two states
    reset_label   the reset button
    close         the bottom-out paragraph, rendered only at `shown === 6`
    progress      {"all", "step_prefix", "step_join"} → the mono head readout
    say_it_back   options_label + opens_on + four questions

⚠️ **`progress` IS AUTHORED IN SCHEMA §3's KEY ORDER AND THAT MAY MATTER.**
`_progress_readout()` prints the FIRST authored state at rest, and this bench's resting
state is `shown = 1` — *"level 1 of 6"*, not *"all six levels"*. `zoom-bench` belongs in
`_KIND_FN_OWNS_PROGRESS` for exactly that reason: the head row is composed by the
instrument's own renderer from a prefix, a count and a join, and the three keys are
fragments rather than named states. Authored in the schema's order because the schema wins
on naming and shape; reported to the engine pass so the resting value is composed and not
taken off the first key.

⚠️ **THIS INSTRUMENT IS ON INK.** `.ks3-dark p` is (0,1,1) and beats a bare component class
at (0,1,0); every colour rule for it must be written at (0,2,0) under `.ks3-dark …` and
`ks3_parity.check_dark_text_specificity()` resolves it on the real cascade. Recorded here
because this payload is what feeds it, and the scale column is `--ks3-alert` on ink.

── One place Design's page and the ENGINE disagree, and it is reported ─

Design's `#s-model` runs: eyebrow, display statement, four cards, THEN the key fact box,
and there is no closing paragraph after it. `r_rule()` emits the nested key fact before
`close`, which is the same order — so this page, unlike b9-01, has no ordering divergence
to report. It is recorded as checked rather than left silent, because the b9-01 defect was
found only by looking.

⚠️ Recorded and not fixed: `ks3_data/b10/__init__.py`'s docstring says *"Design's page
titles it `How we worked out DNA`"* for b10-03. Design's page titles it **How we worked out
DNA's structure**, identical to `structure.py`, so the "known title divergence" that note
records does not exist. That file is not this pass's to edit; the consequence for THIS
lesson is handled in `references` — see the comment there.
"""


# ── the six zoom levels (page lines 313–326) ─────────────────────────────
#
# ORDERED outermost → innermost, and the order is the whole instrument: each level is
# inside the one above it, and `shown` walks down the list one press at a time.
#
# ⚠️ THE `scale` COLUMN IS QUOTED, NOT COMPOSED. Schema §3.1 prints all six figures
# verbatim for one reason — a retyped zero in row 6 is invisible and wrong — and these are
# that table. `0.0000003 mm apart` carries seven decimal places and `0.002 mm long` carries
# the word `long`, which the other five do not.
#
# ⚠️ ROW 5 PRINTS NO NUMBER, DELIBERATELY. A gene has no characteristic length and Design
# says so in words. Do not complete the column.
#
# ⚠️ ROW 5 IS `A gene` AND ROW 6 IS `The bases`. NOTES §1.2 and the dispatch brief both say
# DNA and a base pair; schema §10 item 1 records that they are the ones that are wrong. The
# page's own close — "the last three are all the same molecule seen at different
# magnifications" — is only true of the list as drawn.
LEVELS = [
    {"name": "A person", "scale": "1.6 m",
     "body": "Around thirty trillion cells, almost every one of them carrying "
             "an identical copy of the same instructions."},
    {"name": "A cell", "scale": "0.02 mm",
     "body": "Any body cell will do — a cheek cell, a liver cell, a root hair "
             "cell in a plant. All of them keep their instructions in the same "
             "place."},
    {"name": "The nucleus", "scale": "0.006 mm",
     "body": "The control centre of the cell, and where the DNA is kept. Red "
             "blood cells are the famous exception: they throw theirs away to "
             "make room for haemoglobin."},
    {"name": "A chromosome", "scale": "0.002 mm long",
     "body": "DNA wound around proteins and coiled tightly. A human body cell "
             "has 46 of them, in 23 pairs — one of each pair from each parent. "
             "They are only visible under a microscope when a cell is about to "
             "divide."},
    {"name": "A gene", "scale": "a section of the strand",
     "body": "A length of the DNA in that chromosome, carrying the instruction "
             "for one characteristic. Not a separate object attached to the "
             "chromosome — a part of it, like a chapter in a book."},
    {"name": "The bases", "scale": "0.0000003 mm apart",
     "body": "The instruction is written in a sequence of four bases, known by "
             "their initials A, T, C and G. The order of those letters along "
             "the gene is the information."},
]

# ── the four say-it-back questions (page lines 328–333) ──────────────────
#
# Inside `<section id="s-bench">`, not a block of its own — so they are part of this
# payload rather than a second activity. The answer for the selected question is always
# visible: the panel gates nothing and marks nothing, which is why no `answer` INDEX and no
# feedback exist anywhere in it.
#
# ⚖️ `contains` IS SECOND AND IS WHAT THE PANEL OPENS ON. That is the one authored opening
# selection on this page (`opens_on`, schema §3.2) and the reason is teaching, not runtime:
# "What contains what?" states the whole nesting in one answer, so the panel opens already
# saying the thing the bench exists to show. Design's order is otherwise kept.
QUIZ = [
    {"id": "longest", "label": "Which is the longest?",
     "answer": "All the DNA in one cell — about two metres if you uncoiled "
               "it all. It is divided between 46 chromosomes, each packed "
               "down to a few thousandths of a millimetre."},
    {"id": "contains", "label": "What contains what?",
     "answer": "The nucleus contains the chromosomes; each chromosome is one "
               "coiled DNA molecule; each gene is a section of that DNA; the "
               "bases are the units the section is written in. Five levels, "
               "each inside the last."},
    {"id": "howmany", "label": "How many, in a human?",
     "answer": "46 chromosomes in 23 pairs in a body cell, 23 single "
               "chromosomes in a sperm or egg cell, and around twenty thousand "
               "genes altogether."},
    {"id": "same", "label": "Do all your cells match?",
     "answer": "Yes — every cell with a nucleus carries the same complete set. "
               "What differs is which genes are switched on, and that is what "
               "makes a nerve cell different from a skin cell."},
]

# ── the four model cards (page lines 340–346) ────────────────────────────
#
# Design's `kind` is the mono accent tag and maps to `role`, which is the slot
# `_rule_card()` actually reads for it (`role` or `label`, then `term`/`name`/`title`, then
# `gloss`/`body`/`close`). Authoring `kind` would be a dead key under R5 and would render
# nothing — the failure mode MRB-245 repaired, where ten cards shipped as empty boxes on a
# laid-out grid behind a green build. All three strings per card survive unchanged.
#
# ⚖️ The cards are ordered molecule → package → instruction → alphabet, which is NOT the
# bench's order and is not a slip: the bench walks outside-in, and these four name the same
# four things by the JOB each does. Reading them in the bench's order would make the fourth
# card look like a fifth level.
MODEL_CARDS = [
    {"role": "The molecule", "name": "DNA",
     "body": "A long, thin molecule made of two strands twisted round each "
             "other. It carries information in the order of its four bases, "
             "and it can be copied exactly."},
    {"role": "The package", "name": "Chromosome",
     "body": "One DNA molecule, coiled with proteins so it can be stored and "
             "moved without tangling. 46 in a human body cell, in 23 matched "
             "pairs."},
    {"role": "The instruction", "name": "Gene",
     "body": "A section of DNA that codes for one characteristic. Different "
             "versions of the same gene are why people differ — the gene for "
             "eye colour is in everybody."},
    {"role": "The alphabet", "name": "Bases",
     "body": "Four of them, A, T, C and G, in a sequence. Everything a cell "
             "can be told is written with those four letters and nothing "
             "else."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 164 character for character.
    "slug":        "chromosomes-genes-and-dna",
    "title":       "Chromosomes, genes and DNA",
    "discipline":  "biology",
    "unit":        "inheritance-and-dna",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.INH.02a` — the simple model, and how the four nest inside one
    # another — owned whole. `#s-bench` builds the nesting and `#s-model` names
    # it. `02b`, the part played by Watson, Crick, Wilkins and Franklin, is
    # b10-03's and is not touched here.
    "covers":      ["KS3.B.INH.02a"],
    # Named, used, and owned elsewhere. CELLS.02 is b1-03's — the nucleus is
    # where this whole lesson starts and the page does not re-teach what a
    # nucleus is for. CELLS.06 is b1-05's, and `#s-think` leans on it by name:
    # cell → tissue → organ → organ system was one nesting and this is another,
    # which is the sentence that makes the ladder feel familiar rather than new.
    "touches":     ["KS3.B.CELLS.02", "KS3.B.CELLS.06"],
    "beyond_statutory": False,
    # `genes-and-evolution` is at `develop`: b5-02 opened it at `encounter`
    # with gametes carrying half a set, and this is the lesson that says what is
    # actually IN the set. `cells-and-systems` is at `secure` — the student has
    # the nucleus from B1 and the organisation ladder from b1-05, and this is
    # where both are used together on something one level smaller than a cell.
    "threads":     [{"id": "genes-and-evolution", "level": 2},
                    {"id": "cells-and-systems", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" cards, in her order. `levels-of-organisation`
    # is also the destination of the first pointer this page loses to §8.10 —
    # see "What could not be lifted" 1 — so the edge is carried whether or not
    # the pointer survives in the prose.
    "requires":    ["animal-and-plant-cells",
                    "levels-of-organisation"],
    "assumes":     [],
    # Design's "Connects to" cards, in her order.
    #
    # ⚠️ `specialised-cells` MUST carry its unit. A bare slug in `references` is
    # resolved against the CURRENT unit — unlike `requires`, which resolves
    # across the key stage — so the bare form would build a link to
    # `/ks3/biology/inheritance-and-dna/specialised-cells.html`, which is not a
    # page. It is also the destination of the second lost pointer.
    #
    # ⚠️ `label` IS AUTHORED ON THE B10-03 EDGE, DELIBERATELY (MRB-228). The
    # card prints the TARGET's own title by default, and b10-03 is being
    # authored right now in a file this pass cannot see. Design's card here
    # reads "How we worked out DNA's structure" — which is also `structure.py`'s
    # title and also that page's own `<h1>` — but `ks3_data/b10/__init__.py`
    # records a "known title divergence" claiming Design titles it "How we
    # worked out DNA", so a sibling author following that note would silently
    # change the bytes of THIS page's endmatter. The label is the property of
    # the EDGE — how this lesson names that one — and pinning it makes Design's
    # card byte-identical whichever title b10-03 lands on.
    "references":  [{"unit": "B10", "lesson": "how-we-worked-out-dna",
                     "label": "How we worked out DNA's structure"},
                    {"unit": "B1", "lesson": "specialised-cells"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Alleles, genotype and phenotype, protein synthesis, and "
                   "the genome as a whole.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Four words that people use as though they meant the same "
                    "thing — nucleus, chromosome, gene, DNA — and they are "
                    "four different levels of one structure, nested inside "
                    "each other like the levels of organisation you already "
                    "know.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them (page lines 307–312). `s-model` is the
    # third: no control of its own, so it mirrors `s-bench` and ticks on the
    # bench's predicate — Design's own `isDone()`, page line 508. `short` and
    # `label` are her `RAIL_SHORT` and `RAIL` strings, "Two metres" included.
    # Shipping three fails `check_rail_matches_design`; see the docstring.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Two metres",
         "done_when": "committed"},
        # Design's own threshold, kept: `s.shown >= LEVELS.length` (page line
        # 507). Six levels means five presses of the zoom button, which is what
        # the eyebrow counts.
        {"anchor": "s-bench", "short": "ZOOM", "label": "Zoom in",
         "done_when": "all_levels_shown"},
        {"anchor": "s-model", "short": "MODEL", "label": "The model",
         "mirrors": "s-bench", "done_when": "all_levels_shown"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key, and Design's own
    # reveal is gated on `hookChoice !== null` rather than on a right answer
    # (schema §7: any choice reveals the same paragraph). B is the true one and
    # the reveal says so at once; the hook is not a trick, it is the claim the
    # bench then has to earn one magnification at a time.
    #
    # ⚖️ None of the four is `GENE-03` or `GENE-04`, which is why neither
    # misconception names `s-hook` as its `elicited_by`. All four are answers to
    # "how does two metres fit", and the three wrong ones are the three a class
    # actually offers: it is shared out, it is partly elsewhere, or the number
    # is a figure of speech.
    "phenomenon": {
        "kind": "narrative",
        "title": "Two metres of DNA, in a nucleus you cannot see.",
        "prompt": "Unwind the DNA from a single one of your cells and lay it "
                  "end to end and it measures about two metres. The nucleus "
                  "holding it is around six thousandths of a millimetre "
                  "across. Every cell in your body is doing this, right now.",
        "commit": "How does two metres of anything fit into that?",
        "options": [
            "It is cut into pieces and stored in different cells",
            "It is coiled and packed, and it is extraordinarily thin",
            "Only a small part of it is in the nucleus at any time",
            "The two metres is a figure of speech, not a real length",
        ],
        # ⚑ NOTES-B10 flag 5's first two sites — two metres, and the nucleus
        # figure. Both checked and left; the working is in the docstring.
        # ⚖️ The last two sentences are the lesson's thesis and the reason the
        # bench can run at all: a chromosome is not a different SUBSTANCE.
        "reveal": "It is unimaginably thin, and it is coiled — wound around "
                  "proteins, then coiled, then coiled again, into 46 packages "
                  "called chromosomes. A chromosome is not a different "
                  "substance from DNA. It is DNA, packed. That is the single "
                  "most useful sentence in this lesson.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Schema §12's pre-allocation, and the two beliefs Design's `#s-think`
    # quotes. Both statements are her own bytes, page lines 258 and 262, in
    # register voice.
    #
    # ⚠️ The `GENE` prefix row is NOT yet open in
    # `docs/ks3/misconception-register.md` — see the docstring. That file is
    # another agent's this run; the two rows that belong in it are reported.
    #
    # ⛔ `GENE-12` IS THIS LESSON'S NAMED SPARE AND IS NOT CLAIMED. Exactly two
    # beliefs are confronted on this page and there is no third, so the spare
    # stays permanently unused — the same class as `DRUG-07`. It must never be
    # re-pointed at a different belief in a later pass.
    #
    # Both `confronted_by` values resolve against the BUILT page (MRB-244):
    # `s-think` is the confrontation block's emitted anchor. Both `elicited_by`
    # values are `s-ladder`, which is where each belief is offered as something
    # to commit to — rung 1's options C and D, and rung 2's option A.
    "misconceptions": [
        {"id": "GENE-03",
         "statement": "Chromosomes, genes and DNA are three different things "
                      "in the nucleus.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "GENE-04",
         "statement": "Only the cells that need a gene contain it.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B10 (schema §7's chassis table),
    # so these never reach the lesson body. The TERMS reach a student as the
    # browse page's "Words this unit gives you" chips, and the reading-age gate
    # reads them as its exclusion list. Every definition below is authored, not
    # lifted.
    #
    # ⚖️ `base` is glossed as a UNIT OF WRITING and not as a chemical, because
    # that is the only sense the page uses and the chemistry of it is GCSE's.
    # The KS3 word "base" in an acids lesson is a different word entirely; the
    # note is what keeps a browse-page chip from colliding with C5's.
    "vocabulary": [
        {"term": "DNA",
         "definition": "The long molecule that carries the instructions for "
                       "building and running an organism.",
         "note": "One molecule, seen at four magnifications in this lesson."},
        {"term": "chromosome",
         "definition": "One DNA molecule coiled tightly with proteins so it "
                       "can be stored and moved without tangling.",
         "note": "Not a different substance from DNA. It is DNA, packed."},
        {"term": "gene",
         "definition": "A section of the DNA in a chromosome, carrying the "
                       "instruction for one characteristic.",
         "note": "A part of the chromosome, not an object attached to it."},
        {"term": "base",
         "definition": "One of the four units — A, T, C and G — whose order "
                       "along a gene is the instruction.",
         "note": "The alphabet. Nothing to do with the bases in acid "
                 "chemistry."},
        {"term": "nucleus",
         "definition": "The part of a cell that holds the chromosomes.",
         "note": "Met in Animal and plant cells; this lesson looks inside it."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⊕ MRB-254 — NO LONGER EMPTY, AND THE REASONING THAT KEPT IT EMPTY IS
    # THE REASONING THE AUDIT OVERTURNED.
    #
    # The note here used to say that `zoom-bench` "is already the
    # chromosome-to-DNA nesting figure NOTES flag 19 asks for, built out of
    # DOM", so declaring a slot would invent a sourcing task for a drawing that
    # already ships. The KS3 Biology audit of 18 Aug 2026 drove that bench and
    # found the opposite, measured: at level 6 it renders **six equally-sized
    # sibling cards stacked vertically**. Nothing is drawn inside anything.
    #
    # This lesson's named misconception is *"three different things in the
    # nucleus"* → *"one thing at three magnifications"*, and a stack of equal
    # siblings is a picture of three things side by side. **The bench's own
    # layout is the misconception the lesson is trying to kill.** It remains a
    # good instrument for everything else it does; what it cannot do is nest,
    # and nesting is the claim.
    "figures": [
        {"id": "b10-nested-scale",
         "kind": "diagram",
         "status": "drawn",
         "art": "nested-scale",
         "title": "Chromosomes, genes and DNA: one strand at five "
                  "magnifications",
         "desc": "Five framed drawings in a column, each a magnified callout "
                 "of the one above it, joined by tapering wedges. Panel 01, a "
                 "cell 0.02 mm across, with a nucleus at its centre; a single "
                 "orange fleck inside the nucleus is the strand the figure "
                 "follows. Panel 02, that nucleus enlarged to 0.006 mm, "
                 "holding 46 chromosomes in 23 pairs drawn in grey, with one "
                 "of them picked out in orange. Panel 03, that one "
                 "chromosome, 0.002 mm long, drawn as an orange strand coiled "
                 "around grey proteins and unwinding at its lower end. Panel "
                 "04, the unwound strand as two orange backbones with rungs "
                 "between them, running the width of the frame; a bracket "
                 "marks one length of it as a gene. Panel 05, four rungs of "
                 "that same length, each a pair of lettered boxes: A with T, "
                 "C with G, T with A, G with C, the letters 0.0000003 mm "
                 "apart. Orange is DNA in every panel. Grey and dark ink are "
                 "everything that is not DNA.",
         "caption": "One molecule, five magnifications. Each frame is a "
                    "callout of the frame above it, and the orange strand you "
                    "can trace from the top of the column to the bottom never "
                    "stops being the same strand. Orange is DNA wherever it "
                    "appears; ink and grey are everything that is not DNA. "
                    "The gene in panel 04 is a marked length of the strand "
                    "that was coiled in panel 03 — a section of it, not a "
                    "separate object sitting on it. Nothing is swapped for "
                    "anything else on the way down: a chromosome, a gene and "
                    "DNA are not three things sitting side by side in the "
                    "nucleus, they are one thing at three magnifications. "
                    "Count the marks in panel 02 — there are 46, in 23 pairs "
                    "— and the orange one is the member of one pair that the "
                    "rest of the column follows."},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b10/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 106), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md §3. The
        # read sites are listed in the docstring; `shown` and `quiz` are the
        # runtime's and are deliberately absent, and `opens_on` is the ONE
        # authored opening selection, for the reason §3.2 gives.
        {"type": "zoom-bench", "id": "from-a-whole-person-to-four-letters",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         # ⚠️ FIVE, OVER A SIX-LEVEL PANEL, AND IT IS CORRECT. Six levels means
         # five presses of the zoom button. Schema §10 item 4 exists so that a
         # later pass does not "correct" this into an error. Lifted as drawn.
         "eyebrow": "At the bench · zoom in five times",
         "heading": "From a whole person to four letters",
         # ⚑⚑ THE THOUSANDFOLD CLAIM. This sentence and the six `scale` figures
         # above disagree: the four measurable steps are ~10⁵, ~3×, ~3× and
         # ~7000×, and not one is a thousandfold. BOTH are lifted byte-identical
         # and NEITHER is touched — schema §10 item 2 makes this Mide's copy
         # ruling, and NOTES flag 5 asks him about the figures but not about the
         # claim made over them. It lands in this one string and nothing else in
         # the lesson depends on a ratio. Raised in the report.
         "prompt": "Each step down is inside the one above it, and nothing "
                   "new is added — you are looking at the same material, "
                   "closer.",
         # Design's mono line beside the heading (page line 473):
         # `bottomed ? 'all six levels' : 'level ' + shown + ' of ' + total`.
         # Three fragments, one computed count and one computed total — the
         # denominator is `len(levels)` and is never authored, so a seventh
         # level would need no new prose and could not disagree with the panel
         # beside it.
         #
         # ⚠️ THE TWO FRAGMENTS CARRY THEIR OWN SPACES AND MUST KEEP THEM.
         # `_b10_zoom_progress` composes `step_prefix + n + step_join + total`
         # by raw concatenation — its own docstring warns that a missing join
         # reads "level 36" — so `"level"` and `"of"` would ship "level1of6".
         # Measured against the built page, not assumed. Design's expression is
         # `'level ' + shown + ' of ' + total`, and these are her two literals.
         "progress": {"all": "all six levels",
                      "step_prefix": "level ",
                      "step_join": " of "},

         "levels": LEVELS,

         "in_label": "Zoom in",
         "in_done_label": "As far in as it goes",
         "reset_label": "Back out",
         # Rendered only at `shown === 6` (page line 135). This is the sentence
         # that makes the six-level list one claim rather than six facts, and it
         # is why level 5 is `A gene` rather than `DNA`: "the last four are all
         # the same molecule" is true of chromosome, gene and bases and would be
         # false of a list carrying DNA beside them as a separate thing.
         "close": "Six levels, and the last three are all the same molecule "
                  "seen at different magnifications. A chromosome is coiled "
                  "DNA; a gene is a section of that DNA; the bases are the "
                  "units the section is written in. Nothing was swapped for "
                  "anything else on the way down.",

         "say_it_back": {
             "options_label": "Say it back — which one is which?",
             # ⚖️ THE ONE AUTHORED OPENING SELECTION ON THIS PAGE, and only
             # because it is not first in its list (schema §0 rule 3, §3.2).
             # Omitting it would open the panel on `longest` and quietly change
             # what the bench says first.
             "opens_on": "contains",
             "questions": QUIZ}},

        # #s-model — the band panel, and the section that names the four things
        # the bench has just nested. Rail stop 3, mirroring `s-bench`.
        #
        # ⊖ Checked, not assumed: Design draws eyebrow → statement → cards →
        # key fact and no closing paragraph, and `r_rule()` emits the nested key
        # fact in exactly that position. Unlike b9-01 there is no ordering
        # divergence here to report.
        {"type": "rule", "anchor": "s-model",
         "eyebrow": "The model in four sentences",
         # ⚑ NOTES-B10 flag 7's second site — "one gene, one job" as the working
         # model. Checked and left; the legal line carries the hedge and it is
         # load-bearing. See the docstring.
         "statement": "A gene is an instruction for one job.",

         "cards": MODEL_CARDS,

         # Design nests the key fact inside this section (page lines 348–351) on
         # the CARD ground with the 5px accent offset shadow. `card`, because
         # the section itself is `--ks3-band` and band on band is invisible —
         # the same arrangement and the same reason as b7-01's and b9-01's.
         "key_fact": {"ref": "the-four-levels", "ground": "card"}},

        # ⊕ MRB-254 — NESTED, WHERE THE BENCH IS STACKED.

        # `zoom-bench` at level 6 renders six equally-sized sibling cards in a

        # vertical column — six things side by side, which is this lesson's named

        # misconception drawn as a layout. The figure puts every panel inside a

        # callout of the one before it, so the nesting is physical, and carries one

        # orange strand the whole way down so the reader can see it is one thing.

        {"type": "figure", "ref": "b10-nested-scale", "anchor": "s-nested"},


        {"type": "misconception", "id": "three-things-and-the-cells-that-need-them",
         "anchor": "s-think", "targets": "GENE-03"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-model on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 350
    # and identical to payload schema §13's b10-02 entry.
    "key_facts": [
        {"id": "the-four-levels",
         "text": "DNA is a long molecule found in the nucleus. It is coiled "
                 "into chromosomes — 46 in a human body cell, in 23 pairs. A "
                 "gene is a section of DNA carrying the instruction for one "
                 "characteristic, and the instruction is written in a sequence "
                 "of four bases.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, schema
        # §9), so it is a `confrontation` and not a `predict`, it is not a rail
        # stop, and it emits no completion contract. Contract R1's `predict`
        # branch applies where `#s-think` gates a reveal behind a commitment; no
        # B10 page does, and none of the five rails lists `s-think`.
        {"id": "three-things-and-the-cells-that-need-them",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "GENE-03",
         "statements": [
             # GENE-03. The `<em>` run on "or" is kept — `rich()` renders it —
             # because the library-and-paper sentence turns entirely on that one
             # italicised word.
             #
             # ⚠️ "from b1-05" cut — "What could not be lifted" 1. The
             # destination survives in `requires`.
             {"quote": "Chromosomes, genes and DNA are three different things "
                       "in the nucleus.",
              "body": ["They are one thing described at three magnifications, "
                       "and the levels-of-organisation ladder is the right way "
                       "to hold it: cell, tissue, organ, organ system was one "
                       "nesting, and DNA, gene, chromosome, nucleus is "
                       "another. DNA is the molecule. A gene is a length of "
                       "that molecule — a section, not a separate object "
                       "sitting on it. A chromosome is the whole molecule "
                       "coiled up tightly with proteins so that it can be "
                       "moved around without tangling. Asking whether a "
                       "nucleus contains chromosomes <em>or</em> DNA is like "
                       "asking whether a library contains books or paper. The "
                       "one place the analogy is worth pushing further: a "
                       "chromosome is a single, extremely long DNA molecule, "
                       "so a gene is not attached to a chromosome — it is part "
                       "of it, the way a chapter is part of a book rather than "
                       "a bookmark in one."]},
             # GENE-04, and the reason the bench is upstream of it in the
             # document: the student has already seen the whole set sitting in
             # one nucleus, six levels down.
             #
             # ⚖️ "If cells only carried the genes they were using, none of that
             # would be possible" is the sentence the whole misconception turns
             # on: it makes the belief answerable by consequence rather than by
             # assertion, and rung 2 marks exactly that move.
             #
             # ⚠️ "you met in b1-04" cut — "What could not be lifted" 2. The
             # destination survives in `references`.
             {"quote": "Only the cells that need a gene contain it.",
              "body": ["Every cell with a nucleus carries the whole set: all "
                       "46 chromosomes, all of your genes, the complete "
                       "instructions. A cell in your eye contains the genes "
                       "for making liver enzymes and for growing hair, and a "
                       "cell in your liver contains the genes for eye colour. "
                       "What differs between cells is which genes are "
                       "<em>switched on</em>, and that is what makes a nerve "
                       "cell different from a skin cell despite the two "
                       "carrying identical information — which is the "
                       "mechanism behind the specialised cells. It is also the "
                       "reason a single cell left at a crime scene identifies "
                       "a person, and the reason a whole sheep could be built "
                       "from one udder cell. If cells only carried the genes "
                       "they were using, none of that would be possible."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RUNG 1 CLEAN AS DRAWN, RUNG 2 REPAIRED. rung 1
    # correct 4w against 4 / 4 / 4 (four nouns in four orders, so the rung is
    # length-blind by construction); rung 2 correct 21w against 12 / 6 / 10 as
    # delivered, which tripped BOTH arms of the gate, and 22 / 21 / 21 after
    # each distractor is rewritten as a wrong RULE in the correct answer's own
    # shape. The correct option, `answer`, Design's option ORDER and every one
    # of her six corrections are byte-identical. Full working, with the before
    # and after of all three, in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Put them in order",
            "q": "Order these from largest to smallest: gene, nucleus, "
                 "chromosome, base.",
            # Design's four, untouched, and they could not have needed
            # touching: every option is the same four nouns permuted, so all
            # four are four words and there is nothing to pick by except the
            # nesting. Three of the four are `GENE-03` in three different
            # student wordings.
            #
            #   A  correct
            #   B  authored belief: the chromosome is the container, not the
            #      nucleus
            #   C  GENE-03 — a gene as something beside the chromosome rather
            #      than inside it
            #   D  the ladder read upside down
            "options": [
                "Chromosome, nucleus, gene, base",
                "Nucleus, chromosome, gene, base",
                "Nucleus, gene, chromosome, base",
                "Gene, chromosome, nucleus, base",
            ],
            "answer": 1,
            "feedback": {
                0: "The nucleus is the container — all 46 chromosomes sit "
                   "inside it.",
                2: "A gene is a section of a chromosome, so it must be smaller "
                   "than the whole chromosome.",
                3: "That is almost exactly backwards. The base is the smallest "
                   "unit, not the largest.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Does a cell in your foot contain the gene for eye colour?",
            # ⊕ MRB-177, 18 Aug 2026. Options 0, 2 and 3 rewritten as wrong
            # RULES in the correct answer's shape — where the genes are, and
            # what follows from their being there. Option 1 and `answer` are
            # Design's, unchanged. Each rewrite keeps Design's own clause
            # verbatim at the front.
            #
            #   A  GENE-04 — the set is sorted by destination
            #   B  correct, Design's, unchanged
            #   C  authored belief: a gene is only present in the people who
            #      show the characteristic
            #   D  authored belief: genes travel to where they are needed
            "options": [
                # 22w. Was "No — that gene is only in the cells of the eye"
                # (12w). The added clause is the sorting-by-destination rule
                # head-on, which is what the correction's second sentence
                # denies in the same words.
                "Yes — every cell with a nucleus has the complete set, but "
                "only some genes are switched on in each cell",
                # 21w — Design's, unchanged.
                "No — that gene is only in the cells of the eye, so each cell "
                "carries only the genes its organ uses",
                # 21w. Was "Only if you have brown eyes" (6w). Now states the
                # presence-follows-appearance reading as a rule, which "the
                # gene is present in everyone" contradicts precisely.
                "Only if you have brown eyes, because a gene for a "
                "characteristic is only present in the people who show it",
                # 21w. Was "No — genes move to the organs that need them"
                # (10w). The consequence the belief licenses: a gene with a
                # destination.
                "No — genes move to the organs that need them, so a gene ends "
                "up in whichever cells are using it",
            ],
            "answer": 0,
            # All three unchanged from Design, and each still answers exactly
            # the belief its rewritten distractor states — which is the test of
            # whether the rewrite changed what the question measures.
            "feedback": {
                1: "Every cell with a nucleus carries the complete set of "
                   "instructions. Nothing sorts them out by destination.",
                2: "The gene is present in everyone; what differs between "
                   "people is the version of it they carry.",
                3: "Genes cannot move. They are sections of the chromosomes, "
                   "which stay in the nucleus of their own cell.",
            }},
        # ⚖️ Criterion 4 is the rung's whole point and it is why the question
        # hands the student a sentence to REPAIR rather than a definition to
        # recite: "not three separate contents of the nucleus but one structure
        # at three levels" is `GENE-03` refused in the student's own writing.
        "explain": {
            "title": "Rung 3 · Explain the nesting",
            "q": "A student says \"the nucleus contains chromosomes and DNA "
                 "and genes\". Rewrite the sentence so it is correct, and "
                 "explain how the four things are related.",
            "field_label": "Your explanation",
            "placeholder": "The nucleus contains chromosomes, which are…",
            "success": [
                "Says the nucleus contains chromosomes.",
                "Says each chromosome is a long DNA molecule, coiled up — not "
                "a separate thing from DNA.",
                "Says a gene is a section of the DNA in a chromosome.",
                "Makes clear the three are not three separate contents of the "
                "nucleus but one structure at three levels.",
                "Uses a comparison or an ordering that shows the nesting "
                "clearly — for example largest to smallest, or a book, chapter "
                "and letters.",
            ]},
        # ⚖️ Criterion 5 is what keeps this from being a forensics anecdote: it
        # marks a student for naming a limitation, and it offers three real ones
        # rather than one. The red-blood-cell branch is the strongest, because
        # it is the page's own level-3 body — the famous exception — used
        # against the page's own claim.
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A single cheek cell left on a glass at a crime scene is "
                 "enough to identify a person. Explain what makes that "
                 "possible, using what you know about where genetic "
                 "information is stored and which cells carry it.",
            "field_label": "Your answer",
            "placeholder": "Every cell with a nucleus…",
            "success": [
                "Says every cell with a nucleus carries the person’s complete "
                "set of chromosomes.",
                "Says the DNA in any one cell is therefore the same as in any "
                "other cell of that person.",
                "Says the sequence of bases differs between people, so it can "
                "be used to tell them apart.",
                "Says a single cell is enough because the whole instruction "
                "set is present in it, not just part of it.",
                "Identifies a limitation — identical twins share their DNA, or "
                "the sample may be contaminated or degraded, or a red blood "
                "cell would not work because it has no nucleus.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "DNA is a long molecule, coiled with proteins into chromosomes "
                "and stored in the nucleus. A human body cell has 46 "
                "chromosomes in 23 pairs, one of each pair from each parent. A "
                "gene is a section of DNA that carries the instruction for a "
                "characteristic, and the instruction is written as a sequence "
                "of four bases. Every cell with a nucleus carries the whole "
                "set; cells differ in which genes are switched on.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B10 flag 6 lives here in full and is checked and left; the working
    # is in the docstring. ⚖️ MRB-225 holds: the layer applies the lesson's own
    # claim — that a count is not the thing to look at — to two counts the
    # lesson never gave, and retracts nothing above it. Design's own hedge, that
    # "the interesting differences … are as much about when and where genes are
    # switched on", is load-bearing: it is what stops the one-per-cent figure
    # reading as a claim that humans and chimpanzees are ninety-nine per cent
    # the same thing.
    "stretch": [
        {"type": "explainer", "id": "what-the-counts-do-not-tell-you",
         "text": "The number of chromosomes tells you almost nothing about an "
                 "organism. A human has 46, a chimpanzee 48, a potato 48, a "
                 "dog 78 and a particular fern over a thousand. Complexity "
                 "does not track the count, and neither does the number of "
                 "genes: humans have around twenty thousand, which came as an "
                 "unwelcome surprise in 2003 when the Human Genome Project "
                 "finished and the pre-project bets had run to a hundred "
                 "thousand. A water flea has more genes than you do. What the "
                 "count misses is that a gene can be read in several ways, "
                 "that most of the genome is regulatory rather than "
                 "instructional, and that the interesting differences between "
                 "species are as much about when and where genes are switched "
                 "on as about which genes exist. Chimpanzee and human DNA "
                 "differ by something like one per cent of the letters, and "
                 "that one per cent includes a great deal of switching."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to get the four words straight in your own "
                      "wording?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 297) and nothing in it is a safety
    # instruction — it is a note about how far the scale figures can be trusted
    # and about the size of the model's central claim. Routing it through
    # `safety_note` would print it in the treatment reserved for "never light a
    # candle without an adult".
    #
    # ⚑ NOTES-B10 flag 7's fourth and last site, and the one that does the real
    # work: it is the only place the "one gene, one characteristic" model is
    # admitted to be a simplification, and it gives BOTH directions of the real
    # picture. It must not be trimmed.
    #
    # ⚠️ `b10-01` resolved to its lesson title, recast from possessive to
    # prepositional so the colon in the title reads — "What could not be
    # lifted" 3. Unlike the two `#s-think` pointers, this destination is on
    # neither endmatter list, so cutting it would lose it entirely.
    "convention_note": "The scale figures are rounded to the nearest order of "
                       "magnitude to make the nesting readable. \"One gene, "
                       "one characteristic\" is a deliberate simplification "
                       "kept for KS3: most characteristics involve many genes "
                       "and many genes affect more than one characteristic, as "
                       "the height curve in Variation: continuous and "
                       "discontinuous already implied.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is a scale model whose figures the legal line explicitly tells
    # the student are rounded, and rung 4 asks for an explanation AND an honest
    # limitation of it — which is the analysis-and-evaluation strand rather than
    # an experimental one. Nothing on this page is measured by the student, so
    # `experimental-skills` and `measurement` are not claimed.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
