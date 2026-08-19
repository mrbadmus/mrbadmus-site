"""B10 L4 — Passing it on: heredity (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b10/b10-04-passing-it-on-heredity.dc.html` (585 lines), her
author's notes `docs/ks3/design-reference/b10/NOTES-B10.md` §2 flags 13 and 14, and
the B10 payload schema `docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md` §0, §1, §5
(including §5.1 and §5.2), §7, §8, §9, §10, §11, §12, §13, §14, §15 and §16,
under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the one listed under "What could not be lifted". The three genotype
labels, the four step cards, both marked rungs, both self-marked rungs and all
four bench notes came out of the page's own `GENOTYPES`, `STEP_CARDS`, `RUNGS`,
`SELF_RUNGS` and `renderVals()` via `tools/extract_design_payload.js`, not off a
keyboard.

── `covers` is one statutory clause, owned whole ────────────────────────

`KS3.B.INH.01` reads, in full: *heredity as the process by which genetic
information is transmitted from one generation to the next*
(`docs/ks3/statutory-register.md` line 181). No sub-statements are minted for it —
`ks3_data/substatements.py` splits `INH.02` and `INH.05` and leaves `INH.01`
whole, because the clause is one process and this page teaches it as one
process: `#s-steps` gives the four steps of the transmission and `#s-bench`
makes the student run it often enough to see that the outcome is a *proportion*
and not a rule about any one seed.

`INH.02a` and `b` belong to b10-02 and b10-03, `INH.04` to b10-01 and `INH.03`
to b10-05. `build_ks3.validate()` enforces exactly-once ownership, so a second
claim would fail the build rather than quietly double up. b5-02
`gametes-and-fertilisation` already `touches` `INH.01`; a `touches` is not a
claim and the two do not collide.

── ⛔ THE BENCH IS UNSEEDED AND MUST STAY UNSEEDED ──────────────────────

Schema §5.1, and it is ruled. Design's `grow()` calls `Math.random()` **once per
gamete, per parent, per seed** — two calls per seed, the only `Math.random()` in
B10 — and there is no PRNG, no seed, and no seed key anywhere on any of the five
pages.

**There is no `seed` key in this payload and there must not be one.** This is
not an oversight to be tidied by a later pass and it is not a testing
inconvenience to be routed around. The claim the lesson makes is that 3:1 is a
*sampling* result, not a property of any one litter, and the only way a student
can find that out is by getting a different answer from the person next to them.
A class of thirty pressing "Grow one seed" gets thirty different seeds; a class
of thirty pressing "Grow a hundred" gets thirty tallies that are all *near* 3:1
and none of them exactly it. That difference IS the lesson, and the page says so
in three places that would all become false against a seeded bench: the legal
line ("a real 3:1 ratio only emerges over large numbers — which is why the
hundred-seed button exists"), rung 4 criterion 3 ("she cannot predict any
individual puppy — which version each gamete carries is chance") and rung 4
criterion 4 ("a small litter may not show the ratio at all, so the prediction is
about large numbers").

⚠️ **A later pass adding a seed would be a REGRESSION, not a hardening.** A
seeded bench delivers 75/25 on cue, and 75/25 on cue is the exact misconception
rung 4 criterion 4 is written to break — it teaches that the ratio is a rule the
offspring obey rather than a shape that only large numbers show. The cost of
keeping it real is real and is accepted:

  * **This bench is not screenshot-reproducible.** Any parity or render gate
    must compare the chassis and the controls — the six genotype buttons, the
    three action buttons, the cross line, the two tally rows, the note panel —
    and never the tally numbers, the percentages, the ratio line or the
    most-recent-seed card.
  * A drive that wants a deterministic assertion has one available that costs
    nothing: set both parents to `PP` and every seed is purple, or both to `pp`
    and every seed is white. Those two settings are deterministic *by the
    science*, which is a very different thing from a seed.

⊖ **`showDraft` is the only tweak prop on this page** (schema §15, measured from
the `data-props` attribute). NOTES §3 names preset parent genotypes as the
natural second tweak. **It is not drawn and it is not added.** If it ever were,
it would collide with `start` below, and `start` wins — `start` is CONTENT, not
a preview dial, and the reason is in the comment on the key itself.

── ⚠️ THE FOUR `notes` ARE ORDERED AND THE ORDER IS LOAD-BEARING ────────

Schema §5.2. Design evaluates them as an if/else chain and the first match wins,
so the dict below is authored in evaluation order and the renderer must test in
that order. It is **not alphabetical, not arbitrary, and not to be tidied** — a
later pass that sorts these keys, or that "groups the pure cases together", or
that lets a formatter reorder them, breaks the instrument silently:

    1  one_pure_dominant    neither parent can give two p AND at least one is PP
    2  both_pure_recessive  both parents pp
    3  both_carriers        both parents Pp  ← Mendel's 3:1, the headline case
    4  mixed                everything else (a pp homozygote × a Pp heterozygote)

Reversing 1 and 2 would be harmless because their conditions are disjoint.
Moving 3 below 4 would not be: `mixed` is the fall-through, so `Pp × Pp` would
match it and the one cross the whole lesson is about would print the generic
line instead of the 3:1 one. The order is the guard.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ────────────────

Design draws four (page lines 320–326: `s-hook`, `s-bench`, `s-steps`,
`s-ladder`) and her `isDone()` gives `s-steps` the BENCH's predicate, character
for character, one section down (page lines 394–395):

    if (id === 's-bench') return s.tally.purple + s.tally.white >= 20;
    if (id === 's-steps') return s.tally.purple + s.tally.white >= 20;

`#s-steps` is an eyebrow, a display statement, four numbered cards and the KEY
FACT: no control, no commitment, no field, no reveal. It is the PAYOFF of the
bench beside it and it carries no control precisely because the bench has
already taken the student's commitment. So it is authored as a mirror,
`wireRail`'s `paint()` resolves it at rail level — which is the level Design
computes it at — and `ks3_parity.check_rail_matches_design` gates the built rail
against `docs/ks3/rail-manifest.md`, whose row for this lesson reads
`s-hook s-bench s-steps s-ladder | s-steps=s-bench`.

⚠️ Payload schema §8's tables are correct as MEASUREMENT and the instruction to
*author three stops and drop the band* is REVERSED in the ⊕ block at the head of
the same section, with the struck paragraph kept below it. **The struck
paragraph is not what to build.** Four is what Design drew and four is what
ships; shipping three fails the build.

⚖️ **TWENTY SEEDS, AND NOT ONE SEED.** Design's threshold is `>= 20`, not
`> 0`, and it is a teaching claim rather than a wiring detail: one seed is the
"chance decides each one" story and twenty is the first point at which a student
has something a proportion can be read off. `done_when` is `twenty_seeds_grown`
on the bench and on its mirror. Note that "Grow a hundred" clears it in one
press and "Grow one seed" needs twenty presses — which is itself the argument
the two buttons exist to make.

`#s-think` and `#s-keynote` are on no rail, and that is Design's own: none of
the five B10 rails lists `s-think`, and `#s-think` here is static markup — two
quotes, two bodies, no options, no reveal, no button, no `sc-if` — so it is a
`confrontation` and not contract R1's `predict`. Schema §9, measured on all five
pages.

── What could not be lifted byte-identical, and why ────────────────────

One, and no science word moves in it.

1. **`b10-01's` in `#s-think`'s first body.** Design writes *"Height in people
   looks like blending because hundreds of genes are involved, which is
   `<a href="b10-01-…">b10-01's</a>` smooth curve"*. Two problems in one clause,
   and they have the same fix. A student cannot resolve a slot code, and
   printing one is exactly the platform leakage §8.10 exists to stop; and
   `rich()` allows `<em>` and `<strong>` and nothing else, so the anchor does
   not survive anywhere on the page in any case and the link TEXT is all that
   would reach a student. Resolved to the lesson TITLE, the way b9-01 resolved
   the identical shape:

       Design:  which is b10-01's smooth curve
       Built:   which is the smooth curve in Variation: continuous and
                discontinuous

   The possessive is what forces the small reordering — *"b10-01's smooth
   curve"* becomes *"Variation: continuous and discontinuous's smooth curve"* on
   a straight substitution, which is not English. Every other word of the
   sentence is Design's, "smooth curve" included.

   ⚖️ **The destination is NOT then added to `references`,** which is where this
   departs from b9-01: its two stripped links pointed at cards Design had
   already drawn, and b10-01 is on neither of this page's endmatter cards, so
   carrying it would put a third link in a "Connects to" card drawn with two.
   The full working is on the `references` key. What the student gains is a
   lesson TITLE where a slot code used to be, which is the better pointer of the
   two.

⚠️ No sequence leak to repair. Grepped the delivered file: `half-term` appears
zero times, and the only match for `year` is *"cited a handful of times in
thirty-four years"* in the stretch layer, which is Mendel's history and is
content. No school year is named anywhere on the page.

── ⊕ MRB-177 LENGTH PARITY — BOTH RUNGS CLEAN AS DRAWN, NOTHING TOUCHED ─

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags a
correct option that is strictly the longest AND clears the longest distractor by
≥4 words or by ≥1.4×.

    rung 1  correct 13w vs 11 / 13 /  7   — TIED longest, not strictly   ✓ clean
    rung 2  correct 10w vs 10 /  8 /  8   — TIED longest, not strictly   ✓ clean

**No option was touched on either rung, so there is no before/after to show: the
before and the after are the same four strings, and the counts above are both.**
Recorded at this length anyway, because a clean rung is exactly what a later
pass "improves" by padding a short distractor, and the reason these two are
clean is worth keeping.

**Rung 1 is clean because every option is a NUMBER plus its reason.** The
correct answer gives 23 and says why (one from each pair, so fertilisation
restores 46); distractor B gives 46 and says why (every cell has the same
number); C gives the right number for a wrong reason (half are lost); D gives 92
and says why (they double first). Four numbers, four reasons, same shape — and
C, the near miss, is exactly as long as the correct answer, which is the one
option a student is most likely to pick by shape if the shapes differ.

**Rung 2 is clean because all four options are one-clause CLAIMS ABOUT A
CAUSE.** Carried without showing · appeared by mutation · blended and separated ·
something in the soil. None of them states a rule with branches, which is the
construct MRB-177 named and the reason twenty rungs across five units tripped
the gate; here the correct answer is not longer by construction because the
construction does not favour it.

⚖️ **Option C at 8w is not a tell either.** `length_tell()` measures the correct
option against the LONGEST distractor, not the shortest, and padding a short
belief makes it read as more considered than the student's own version of it.
Recorded so a later pass does not "fix" a clean rung.

⚑ For Mide's science gate — the NOTES-B10 §2 flags landing on THIS lesson, and
  what was checked against each. Two flags, both already ruled in schema §16:

  * flag 13  **Hold "dominant" and "recessive" back to GCSE.** RULED AND
             CONFIRMED (schema §16), and it constrains the whole record. The
             lesson says *"overrides"* and *"hidden"* and names neither term,
             and nothing authored here introduces either as a synonym "for
             later" — not in the vocabulary chips, not in `support` (which is
             empty; Design draws no `ks3-support` layer on this page), and not
             in a comment.

             ⚖️ The test is not that the words are absent but that nothing here
             becomes WRONG at GCSE, and it is worth stating what that forbids,
             because it is the tempting rewrite: **the hidden version is never
             described as weaker, lost or used up.** That is precisely the
             belief `GENE-08` confronts (*"it skipped a generation, so the gene
             must have disappeared and come back"*), so the lesson already
             argues against its own worst failure mode — and every one of rung
             3's five criteria is written to mark the same distinction, the
             fifth explicitly ("the version was never lost or recreated — it was
             carried the whole time"). P/p, clean dominance and a 3:1
             expectation are standard and correct for Mendel's peas at this
             level.

             ⚑ TWO SITES WHERE A FORM OF THE WORD DOES APPEAR, both shipped as
             drawn, both reported rather than edited:

               1. `convention_note` — *"a clean dominance rule"*, twice.
                  Design's own bytes. It is the noun used to describe the
                  MODEL's scope, not a label a student is asked to learn or is
                  marked on, and it appears in the legal line rather than in
                  teaching copy. MRB-205 says the page wins. Reported because
                  the ruling's sentence is "names neither term" and this is not
                  literally term-free.
               2. `ks4_becomes` — *"Alleles, dominant and recessive, …"*.
                  Design's *At GCSE this becomes* card, which is the one place
                  on the page whose entire job is to name what arrives later. A
                  destination list is not an introduction, and removing the
                  words from it would leave the card unable to say what the
                  lesson turns into.

  * flag 14  **Mendel: ~28,000 plants, 1856–1863, published 1866, rediscovered
             1900, died 1884** (stretch layer). CHECKED AND LEFT, and schema
             §16's closing paragraph rules the same way. Mendel worked at Brno
             from 1856 to 1863; the commonly cited total is around 28,000
             plants; *Versuche über Pflanzen-Hybriden* was read in 1865 and
             published in the society's proceedings in 1866; he died in 1884;
             the rediscovery by de Vries, Correns and Tschermak is 1900.
             Design's own hedge *"something like 28,000"* is load-bearing and
             must not be trimmed to a bare figure — the count is an estimate
             from his own account, not a tally anybody has audited. ⚑ Mendel is
             a *historical* set of dates and is not a school-year leak; the
             no-year rule is about sequencing the curriculum.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes seven times: *the instruction was there the
whole time, unchanged*. The hook's reveal ("carried, complete and unaltered"),
`#s-steps` card 2 ("Which one it gets is decided by chance"), the key fact
("one may be hidden for generations and still be passed on unchanged"),
`#s-think`'s second body ("The white version was in both parents, in every one
of their cells, doing nothing visible"), rung 2's correction to option C ("The
white version was passed on unchanged"), rung 3 criterion 5 and the key note all
say the same thing at the same size. The stretch layer adds Mendel's history and
retracts nothing above it, and the legal line narrows the MODEL rather than the
claim — which is MRB-225 done correctly: the hedge shrinks what the bench is
evidence for, not what the lesson taught.

── Misconception ids: GENE-07 and GENE-08, and GENE-14 IS NOT CLAIMED ──

Schema §12's pre-allocation, fixed before five parallel authors were dispatched
precisely so that nobody mints "the next free id" and collides with everybody
else. This lesson's two are `GENE-07` and `GENE-08` and its spare is `GENE-14`.

⛔ **`GENE-14` IS NOT CLAIMED AND STAYS PERMANENTLY UNUSED.** Both of Design's
`#s-think` quotes map cleanly onto the two allocated ids and nothing on the page
is a third belief in search of a number. An unclaimed spare is worth exactly
what `DRUG-07` is worth: nothing, and much less than the collision it prevents.
Never re-point it.

⚠️ **The `GENE` prefix row does not yet exist in
`docs/ks3/misconception-register.md`** — schema §12's standing note says
`NOTES-B10 §4`'s claim to have written it is one of four occurrences of the same
slip across B5, B7, B10 and B11, and that a delivery's §4 is an allocation
PROPOSAL to be checked rather than a record. That file belongs to another pass
in flight and is not this module's to edit (contract §0), so the two statements
below are authored in register voice, byte-identical to Design's own quoted
beliefs minus their typographic quote marks, and are reported for whoever opens
the row. No gate resolves an id against the register file, so the lesson builds
either way; what is at risk is the register's completeness.

Both values resolve against the BUILT page (MRB-244), and both are drawn from
the six anchors schema §12 lists for this lesson (`s-hook`, `s-bench`,
`s-think`, `s-ladder`, `s-keynote`, `s-steps`):

  * `GENE-07` is elicited at **`s-hook`**, not at the ladder, and this is where
    b10-04 differs from b9-01. The hook's whole premise is the blending belief
    being set up to fail — *"Not medium plants. Tall ones, every time."* — and
    option C, *"The tall and short blended, then separated again"*, is `GENE-07`
    in a student's own words offered as something to press. It is elicited again
    at rung 2 option C, which is where it is MARKED; the hook is where it is
    first committed to, and the hook is ungated, so a student can hold it
    without penalty for exactly as long as it takes to read the reveal.
  * `GENE-08` is elicited at **`s-ladder`**. Rung 2 option B — *"A new white
    version appeared by mutation in the offspring"* — is the disappeared-and-
    came-back belief in its commonest classroom form, and rung 3 asks for the
    skipped generation to be explained and marks criterion 5 on refusing "lost
    or recreated". The hook's option B is the same belief, but the ladder is
    where it is offered as something to commit to AND adjudicated, which is the
    stronger reading of `elicited_by`.
  * Both are confronted at **`s-think`**, in Design's own page order: the first
    quote is `GENE-07` and the second is `GENE-08`.

── ⚠️ ONE PLACE DESIGN'S PAGE AND THE ENGINE DISAGREE, AND IT IS REPORTED ─

**`#s-steps`' cards carry a NUMBER BADGE and `_rule_card()` has no slot for
one.** Schema §7 records this lesson's card shape as `{num, name, body}` — an
ordered list with a 38px accent square holding "1".."4" (page lines 174–180).
`_rule_card()` in `build_ks3.py` reads `role`/`label`, `term`/`name`/`title`,
`chips`, `gloss`/`body`/`close` and `examples`, and `r_rule()` emits a `<ul>`.
There is no `num`, and no numbered badge.

`build_ks3.py` belongs to the engine pass and is not this module's to edit
(contract §0), and under contract R5 authoring a `num` the renderer never reads
would be a dead key that `ks3_key_audit.py` should fail on. So the digit is
authored into `role`, which is the slot the accent tag renders from, and it
reaches the student as the mono accent tag "1".."4" above each card name rather
than as a badge beside it. **Nothing is joined, dropped or invented — the same
four digits and the same eight strings ship, in the same order, one slot over.**

⚑ Reported for the engine pass: if `_rule_card()` gains a `num` → numbered-badge
slot, this record's four `role` values move to `num` unchanged and the treatment
matches Design's drawing exactly. b10-03's band has the same shape with an
initials badge (`{initials, name, role, body}`) and will have hit the same wall.

── Keys this pass authors that the RENDERER reads (contract R5) ────────

Named explicitly rather than left to be discovered. Every one is measured off
Design's `renderVals()` and is listed in schema §5's shape:

    genotypes      the three parent buttons, their labels and their alleles
    parents        two, both drawing the same genotype set
    start          Pp × Pp — the OPENING CROSS, and content; see the key
    phenotypes     dominant → "purple", recessive → "white"
    one_label / many_label / many_n / reset_label   the three buttons
    cross_join     between the two genotype ids in the panel headline
    last_label / last_template                      the single-seed card
    tally_rows     two rows, each a name + a value + a bar
    ratio_template / no_recessive_template          the mono alert line
    notes          FOUR, ORDERED — see above
    progress       the mono seed counter in the bench header

⛔ **NO RUNTIME STATE IS AUTHORED** (schema §0.3). `tally`, `last`, `picks`,
`hookChoice`, `answers`, `text`, `checked`, `ticks` and `active` are all the
runtime's; the renderer initialises its own. `start` is the single exception the
schema names and it is authored for the reason on the key.

⚠️ **`pea-cross` is not yet registered in `ACTIVITY_KIND_RENDERERS`.** Grepped
`build_ks3.py`, `shared/ks3.js` and `ks3_parity.py`: zero matches. That is
EXPECTED — the engine pass is mid-flight — and no renderer is added here.
Reported rather than worked around.

⚑ **One consequence of that is worth naming, because it looks like an authoring
defect and is not one.** With no `r_pea_cross`, `pea-cross` is not in
`_KIND_FN_OWNS_PROGRESS` (which `build_ks3.py` DERIVES by asking which renderers
read `progress`), so the authored `progress` map falls through to
`_progress_readout`, whose `_PROGRESS_NAME` is `^[a-z][a-z0-9-]*$` and rejects
the underscore in `suffix_one`. The build therefore says:

    progress state 'suffix_one' is not a usable name

**The key names are the schema's (§5) and they are correct as authored, and they
must not be hyphenated to make the message go away.** b10-02 is the proof: it
ships `step_prefix` and `step_join` — same underscores, same head-row slot — and
builds green, because `r_zoom_bench` reads its `progress` and the derived
`_KIND_HEAD_FROM["zoom-bench"]` composes the row. `pea-cross` needs the same two
things and then this message goes with it. Renaming the keys here instead would
put this record out of step with the schema every other B10 author and the
engine pass are working from.

Proved in a scratch harness rather than asserted: with a throwaway in-memory
`pea-cross` renderer standing in (no file written), this record renders to a
23.7 KB page and `check_rail_matches_design`, `check_rail_reachable` and
`check_rail_anchors` are all clean on it — the rail matches
`docs/ks3/rail-manifest.md`'s row for this page stop for stop, including the
mirror. `ks3_key_audit.py B10` reports this lesson's seventeen `pea-cross`
payload keys as unread, which is the same fact stated a second way and clears
with the renderer.
"""


# ── the three parent genotypes (page lines 328–332) ──────────────────────
#
# Design's own array, lifted whole. The order is `PP`, `Pp`, `pp` and it is the
# order the three buttons are drawn in under each parent; `start` names the
# SECOND of them for both parents, which is why the opening selection needs a
# key at all (schema §0.3).
#
# ⚖️ The labels carry the colour word, not the term. `PP · purple` and
# `pp · white` are as far as the vocabulary goes on this page — NOTES flag 13,
# ruled in schema §16, and the whole reason there is no `dominant_term` key in
# the payload shape. The LETTERS carry the relationship: capital P is the one
# that shows, and the bench lead says so in words ("P gives purple and beats p")
# without ever naming what that relationship is called.
GENOTYPES = [
    {"id": "PP", "label": "PP · purple", "alleles": ["P", "P"]},
    {"id": "Pp", "label": "Pp · purple", "alleles": ["P", "p"]},
    {"id": "pp", "label": "pp · white",  "alleles": ["p", "p"]},
]

# ── the four step cards (page lines 174–180) ─────────────────────────────
#
# The band section's ordered list, and the four steps the statutory clause calls
# "the process by which genetic information is transmitted". Read as a sequence:
# two of each → one of each → two again → copied into everything.
#
# ⚠️ `role` HOLDS DESIGN'S NUMBER BADGE. Her shape is `{num, name, body}` and
# `_rule_card()` has no `num` slot, so the digit renders as the mono accent tag
# instead of as a badge. Full working in the docstring's "one place Design's
# page and the engine disagree"; if the engine gains a `num` slot these four
# values move across unchanged.
#
# ⚖️ Card 2 is the one that does the real work and it is why `#s-steps` mirrors
# the bench rather than standing alone: "Which one it gets is decided by chance"
# is the sentence the unseeded instrument next to it demonstrates. Card 4 is the
# one a scheme of work usually leaves out — the new combination is fixed once,
# at fertilisation, and every cell afterwards is a copy of it, which is what
# makes "carried without being shown" a claim about every cell of the organism
# rather than about its gametes.
STEP_CARDS = [
    {"num": "1", "name": "Every body cell has two of each",
     "body": "Chromosomes come in pairs — 23 pairs in a human — so every gene "
             "is present twice, once on each chromosome of the pair. The two "
             "copies may be the same version or different ones."},
    {"num": "2", "name": "Gametes get one of each",
     "body": "When sex cells are made, each gamete receives one chromosome "
             "from every pair, so it carries a single version of each gene. "
             "Which one it gets is decided by chance, which is why siblings "
             "differ."},
    {"num": "3", "name": "Fertilisation restores the pair",
     "body": "One gamete from each parent fuses and the full number is back — "
             "46 in humans, half from each parent. This is the moment the new "
             "combination is fixed."},
    {"num": "4", "name": "Every cell is a copy",
     "body": "The fertilised egg divides again and again, copying its DNA "
             "exactly each time, so every cell of the new organism carries the "
             "same instructions it started with."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 166 character for character.
    "slug":        "passing-it-on-heredity",
    "title":       "Passing it on: heredity",
    "discipline":  "biology",
    "unit":        "inheritance-and-dna",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.INH.01` — heredity as the process by which genetic information is
    # transmitted from one generation to the next — owned whole and unsplit.
    # See the docstring; INH.02a/b, INH.03 and INH.04 belong to the other four
    # lessons of this unit.
    "covers":      ["KS3.B.INH.01"],
    # Named, used, and owned elsewhere. INH.02a is b10-02's and is what every
    # mention of a chromosome, a gene and a version on this page rests on — the
    # step cards use all three and re-teach none of them. INH.04 is b10-01's and
    # is what `#s-think`'s first body points at when it explains why height
    # LOOKS like blending.
    "touches":     ["KS3.B.INH.02", "KS3.B.INH.04"],
    "beyond_statutory": False,
    # `genes-and-evolution` reaches `secure` here: b5-02 opened it at
    # `encounter` with gametes, b10-01 and b10-02 developed it, and this is the
    # lesson where the thread's central mechanism is used to predict something.
    # `cells-and-systems` is at `secure` too — the four step cards are cells,
    # chromosome pairs, gametes and division, all of them met before and none of
    # them explained again here.
    "threads":     [{"id": "genes-and-evolution", "level": 3},
                    {"id": "cells-and-systems", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. `requires` resolves
    # across the whole key stage, so `gametes-and-fertilisation` needs no unit
    # qualifier even though it lives in B5.
    "requires":    ["chromosomes-genes-and-dna",
                    "gametes-and-fertilisation"],
    "assumes":     [],
    # Design's "Connects to" card, in her order, and ONLY her two.
    #
    # ⚖️ `variation-continuous-and-discontinuous` is deliberately NOT added
    # here, and this is where this record departs from b9-01's handling of a
    # stripped link. b9-01's two lost destinations were both already on
    # Design's "Before this lesson" card, so carrying them cost nothing;
    # b10-01 is on NEITHER of this page's endmatter cards, so adding it would
    # put a third link in a "Connects to" card Design drew with two — a
    # student-visible change to drawn endmatter, made to serve a data edge.
    # MRB-205 says the page wins. The destination is not actually lost: the
    # resolved sentence in `#s-think` now names the lesson by its full title
    # where Design printed a slot code, which is a better pointer than the
    # anchor was, b10-01 is one click away on this unit's own index, and the
    # relationship is recorded in `touches` as `KS3.B.INH.04`.
    #
    # ⚠️ `natural-selection` MUST carry its unit. A bare slug in `references` is
    # resolved against the CURRENT unit — unlike `requires`, which resolves
    # across the key stage — so the bare form would build a link to
    # `/ks3/biology/inheritance-and-dna/natural-selection.html`, which is not a
    # page. `check_internal_links` catches it; the dict form is what b9-01 uses
    # for the same reason.
    "references":  ["what-makes-a-species",
                    {"unit": "B11", "lesson": "natural-selection"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    # ⚑ Design's own *At GCSE this becomes* card, lifted byte-identical. It
    # names "dominant and recessive", which the LESSON deliberately does not —
    # and that is the point of the card rather than a leak of the ruling. See
    # the flag 13 note in the docstring; reported, not edited.
    "ks4_becomes": "Alleles, dominant and recessive, homozygous and "
                   "heterozygous, Punnett squares and probability, and "
                   "inherited disorders.",

    # ── framing ─────────────────────────────────────────────────────────────
    # Authored, not lifted — Design's deliveries are lesson pages and draw no
    # unit card. One job: say what the lesson decides, without naming a year and
    # without explaining the platform.
    "big_question": "A characteristic can vanish for a whole generation and "
                    "come back unchanged. Whatever carries it cannot be a "
                    "fluid that mixes — and working out what it is instead is "
                    "the beginning of genetics.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them (page lines 320–326). `s-steps` is the
    # third: no control of its own, so it mirrors `s-bench` and ticks on the
    # bench's predicate — Design's own `isDone()`, page lines 394–395. `short`
    # and `label` are her `RAIL_SHORT` and `RAIL` strings.
    # Shipping three fails `check_rail_matches_design`; see the docstring.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "It came back",
         "done_when": "committed"},
        # Design's own threshold, kept: twenty seeds, not one
        # (`s.tally.purple + s.tally.white >= 20`). One seed is the "chance
        # decides each one" story; twenty is the first point a proportion can be
        # read off. "Grow a hundred" clears it in a single press.
        {"anchor": "s-bench", "short": "BENCH", "label": "Grow seeds",
         "done_when": "twenty_seeds_grown"},
        {"anchor": "s-steps", "short": "STEPS", "label": "The journey",
         "mirrors": "s-bench", "done_when": "twenty_seeds_grown"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key, and Design's own
    # reveal is gated on `hookChoice !== null` rather than on a right answer
    # (schema §7: "No option is correct — any choice reveals the same
    # paragraph"). A is the one the reveal goes on to support, and it says so at
    # once; the hook is not a trick, it is the claim the bench then has to earn
    # in seeds.
    #
    # ⚖️ Option C IS `GENE-07` in a student's own words, which is why `GENE-07`
    # names `s-hook` as its `elicited_by` — and it is deliberately offered here,
    # ungated and unmarked, because it was the accepted scientific view for most
    # of the nineteenth century. A student who holds it is in Darwin's company,
    # and `#s-think` says so.
    "phenomenon": {
        "kind": "narrative",
        "title": "Cross a tall pea plant with a short one and you get tall "
                 "plants.",
        "prompt": "Not medium plants. Tall ones, every time. Then breed those "
                  "tall plants together and the short ones come back, in about "
                  "a quarter of the offspring — from parents that were all "
                  "tall, carrying something that had not shown itself for a "
                  "generation.",
        "commit": "What does the reappearance tell you?",
        "options": [
            "The short instruction was carried, hidden, by the tall plants",
            "A new short version appeared by chance",
            "The tall and short blended, then separated again",
            "The soil made some of them grow shorter",
        ],
        "reveal": "The instruction for short was still there the whole time — "
                  "carried, complete and unaltered, by plants that were tall. "
                  "Inherited information comes in separate units that keep "
                  "their identity from one generation to the next. Nothing "
                  "blended, and nothing was diluted. That single observation "
                  "is the foundation of genetics.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Schema §12's pre-allocation, and the two beliefs Design's `#s-think`
    # quotes. Both statements are her own bytes, page lines 191 and 195, in
    # register voice.
    #
    # ⚠️ The `GENE` prefix row is NOT yet open in
    # `docs/ks3/misconception-register.md` — see the docstring. That file
    # belongs to another pass in flight and is not this module's to edit; the
    # two rows that belong in it are reported.
    #
    # ⛔ `GENE-14` is this lesson's pre-allocated SPARE and is NOT claimed. Two
    # beliefs, two ids. A spare is never re-pointed and an unclaimed one stays
    # permanently unused.
    #
    # Both `confronted_by` values resolve against the BUILT page (MRB-244):
    # `s-think` is the confrontation block's emitted anchor, and Design's page
    # order puts GENE-07's quote first. The two `elicited_by` values differ on
    # purpose and the working is in the docstring.
    "misconceptions": [
        {"id": "GENE-07",
         "statement": "Characteristics blend — a tall parent and a short "
                      "parent give a medium child.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "GENE-08",
         "statement": "It skipped a generation, so the gene must have "
                      "disappeared and come back.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B10, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⛔ **NO `allele`, NO `dominant`, NO `recessive`.** NOTES flag 13, ruled in
    # schema §16. A chip is exactly the shape the ruling forbids — a term with
    # no machinery attached, offered to be memorised — and "version of a gene"
    # is the page's own word for the same thing, used consistently in every
    # string on the page and in all ten ladder criteria. b9-01 glossed "trophic
    # level" as a forward chip and that was right there, because the KS3 word
    # and the GCSE word name the same object and nothing about the KS3 treatment
    # becomes wrong. This is the opposite case: "dominant" arrives at GCSE
    # attached to genotypes, gametes and Punnett squares this lesson
    # deliberately does not have.
    "vocabulary": [
        {"term": "heredity",
         "definition": "The passing of genetic information from parents to "
                       "their offspring.",
         "note": "The process, not the information. What is passed on is "
                 "genes."},
        {"term": "gamete",
         "definition": "A sex cell — a sperm, an egg or a pollen grain — "
                       "carrying one chromosome from every pair instead of "
                       "two.",
         "note": "Half a set, so that two of them make a full one."},
        {"term": "fertilisation",
         "definition": "Two gametes fusing, so the offspring has a full set of "
                       "chromosomes again, half from each parent.",
         "note": "The moment the new combination is fixed."},
        {"term": "version of a gene",
         "definition": "One of the alternative forms a gene comes in, such as "
                       "the one for purple flowers and the one for white.",
         "note": "An organism carries two and may show only one of them."},
        {"term": "offspring",
         "definition": "The new organisms produced by a cross or by a pair of "
                       "parents.",
         "note": "A proportion of them, not any single one, is what a "
                 "prediction is about."},
        {"term": "pure-breeding",
         "definition": "Carrying two identical versions of a gene, so every "
                       "offspring receives the same one.",
         "note": "Mendel started every experiment with lines like these."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED, on all five B10 pages (schema §11). `<img>`,
    # `<figure>` and `<picture>` each appear zero times here — grepped — and
    # every `<svg>` on the page is chassis: the brand chevron, the rail tick,
    # the ladder tick and cross marks, the endmatter arrows. Not one is content.
    #
    # NOTES flag 19's two candidates are a chromosome-to-DNA nesting figure,
    # which b10-02's `zoom-bench` arguably already is, and Photo 51, which is a
    # specific photograph with rights attached and Mide's licensing decision
    # rather than this build's. Neither lands on this lesson.
    #
    # ⚑ If a figure were ever wanted HERE the obvious one is a two-by-two grid
    # of the four gamete combinations from Pp × Pp — but that is a Punnett
    # square with the name taken off, and Punnett squares are exactly what flag
    # 13 holds back to GCSE. The bench IS this lesson's picture of the cross,
    # drawn out of DOM and run rather than looked at, and the argument it makes
    # (a proportion over many seeds) is one a static grid of four boxes cannot
    # make. Reported, not built.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b10/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 102), so the segment is MEASURED and not inherited from the
        # kind name.
        #
        # Payload keys follow docs/ks3/b10-inventory/PAYLOAD-SCHEMA.md §5. The
        # read sites are listed in the docstring; every runtime value is
        # deliberately absent and §0.3 is the reason.
        {"type": "pea-cross", "id": "grow-seeds-and-count-them",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · two parents, one gene",
         "heading": "Grow seeds and count them",
         # `<strong>` survives `rich()`; `<em>` and `<strong>` are the only two
         # tags that do. The two bold letters are the whole rule of the bench
         # stated once in words, and they are why no term is needed.
         "prompt": "Flower colour in pea plants. Each parent carries two "
                   "copies of the gene and passes one of them, chosen at "
                   "random, into each seed. <strong>P</strong> gives purple "
                   "and beats <strong>p</strong>; a plant is white only if it "
                   "has p from both parents.",
         # Design's mono line in the bench header. Three states, because the
         # count is a real English sentence: none, one, many.
         "progress": {"none": "no seeds grown",
                      "suffix_one": "seed grown",
                      "suffix_many": "seeds grown"},

         "genotypes": GENOTYPES,
         "parents": [
             {"id": "parent1", "name": "Parent plant 1"},
             {"id": "parent2", "name": "Parent plant 2"},
         ],
         # ⚖️ `start` IS CONTENT AND IT IS THE SECOND ENTRY, NOT THE FIRST.
         # Schema §0.3's single exception to "author no runtime state": an
         # opening selection that is not `genotypes[0]` is a teaching choice and
         # gets a key. The bench opens on the ONLY cross that produces the 3:1,
         # so the headline result is one button-press away and a student has to
         # change something to discover the other three cases.
         #
         # ⛔ Schema §15: NOTES names preset parent genotypes as a natural tweak
         # prop. It is NOT drawn — `data-props` carries `$preview` and
         # `showDraft` and nothing else — and it must not be added. If it ever
         # were it would collide with this key, and this key wins: `start` is
         # content, a tweak prop is an author's preview dial.
         "start": {"parent1": "Pp", "parent2": "Pp"},

         # As far as the vocabulary goes: two outcomes, two colour words, no
         # term. NOTES flag 13, ruled in schema §16.
         "phenotypes": {"dominant": "purple", "recessive": "white"},

         "one_label": "Grow one seed",
         "many_label": "Grow a hundred",
         "many_n": 100,
         "reset_label": "Clear the plot",

         "cross_join": "crossed with",

         # ⚠️ THE SINGLE-SEED CARD AND THE HUNDRED-SEED RUN ARE NEVER ON SCREEN
         # TOGETHER, and that is measured (`last: n === 1 ? last : null`).
         # Growing a hundred CLEARS this card. They are two different stories —
         # "chance decides each one" and "only the totals show the pattern" —
         # and showing them at once would let a student read the second off the
         # first.
         "last_label": "Most recent seed",
         # ⚠️ `parent 1` and `parent 2` here are LOWERCASE LITERALS, not the
         # parent names. Schema §5 offers `{p1}` and `{p2}` slots; Design's
         # expression does not use the names ("Parent plant 1") in this sentence
         # and prints the lowercase form instead, so the slots are unused and
         # the words are part of the template. The page wins on measurement.
         # Reported.
         #
         # ⚖️ `{genotype}` IS NORMALISED TO DOMINANT-FIRST BY THE RENDERER: a
         # seed that received p then P prints `Pp`, never `pP`. Measured
         # (`s.last.g1 + s.last.g2 === 'pP' ? 'Pp' : …`), and it is not
         # cosmetic — `pP` on the card would read as a fourth genotype that is
         # on none of the six buttons.
         "last_template": "This seed received {g1} from parent 1 and {g2} from "
                          "parent 2, so it is {genotype} — a "
                          "{phenotype}-flowered plant.",

         "tally_rows": [
             {"id": "dominant", "name": "Purple flowers"},
             {"id": "recessive", "name": "White flowers"},
         ],
         # `{ratio}` is printed to two decimal places, which is deliberate and
         # is the unseeded bench made visible: a hundred seeds from Pp × Pp
         # gives 2.85 : 1 or 3.35 : 1 and essentially never 3.00 : 1. A student
         # who runs it twice sees two different numbers either side of three,
         # which is the argument the legal line makes in words.
         "ratio_template": "Ratio purple to white — {ratio} : 1",
         # The branch for a tally with no white at all, which is the honest
         # thing to print rather than a ratio with zero underneath it. It is
         # also the correct output for PP × anything, where "no white in 100
         # seeds" IS the result.
         "no_recessive_template": "No white plants at all in {total} seeds",
         # ⊕ MRB-257 (5.44) — the singular. One seed is a state this bench
         # reaches on its first press, on purpose, and "in 1 seeds" undercuts
         # the sentence beside it.
         "no_recessive_template_one": "No white plant — {total} seed grown",
         # ⊕ MRB-257 (5.45) — THE MISSING BRANCH. `pp × pp` grows a hundred
         # white plants and printed "Ratio purple to white — 0.00 : 1"; so did
         # any single seed that came up white. A ratio needs both phenotypes,
         # and with no purple plants there is no ratio to state — the honest
         # line says what there is. The mirror case had had its own line
         # since Design drew it; this is the other half of the same rule.
         "no_dominant_template": "No purple plants at all in {total} seeds",
         "no_dominant_template_one": "No purple plant — {total} seed grown",

         # ⚠️⚠️ **ORDERED. FIRST MATCH WINS. NOT ALPHABETICAL, NOT ARBITRARY,
         # AND NOT TO BE TIDIED.** Schema §5.2, and the renderer must test in
         # this order. `mixed` is the fall-through, so moving `both_carriers`
         # below it would send Pp × Pp — the one cross this whole lesson is
         # about — to the generic line. Full working in the docstring.
         "notes": {
             # ⊕ MRB-257 / MRB-255 (5.38) — 1a and 1b ARE NEW AND ARE TESTED
             # FIRST. `one_pure_dominant` covered three crosses and its closing
             # promise — "some of them are quietly carrying p, which will show
             # up in the generation after" — is true of exactly one of them.
             # With both parents PP no offspring can carry p at all, and the
             # page was promising a hidden recessive that cannot exist: the
             # misconception this lesson is built to remove, printed by the
             # lesson. With PP × pp the opposite is true — every single seed
             # carries it — and "some of them" undersells the fact that makes
             # the F2 generation surprising.
             #
             # 1a. Both parents PP.
             "both_pure_dominant":
                 "Both parents carry two P versions, so there is no p anywhere "
                 "in this cross to pass on. Every seed is purple, and none of "
                 "them is carrying anything hidden — grow a thousand and the "
                 "generation after will be purple too.",
             # 1b. PP × pp — the classic F1, and every seed is a carrier.
             "pure_dominant_x_pure_recessive":
                 "One parent has only P and the other only p, so every seed "
                 "receives one of each and every seed is Pp. All purple — "
                 "and every single one of them is carrying p. Cross two of "
                 "these and the white flowers come back.",
             # 1. PP × Pp — what is left, and the sentence written for it.
             "one_pure_dominant":
                 "One parent carries two P versions, so every seed receives at "
                 "least one P. Every offspring is purple however many you "
                 "grow — and some of them are quietly carrying p, which will "
                 "show up in the generation after.",
             # 2. Both parents pp.
             "both_pure_recessive":
                 "Both parents carry only p, so every seed gets p from both "
                 "sides. All white, every time. A hidden version stops being "
                 "hidden when there is nothing left to override it.",
             # 3. Both parents Pp — Mendel's 3:1, and the case the bench opens
             #    on. THIS ONE MUST BE TESTED BEFORE `mixed`.
             "both_carriers":
                 "Both parents are purple and both carry p. Each seed has a "
                 "one-in-four chance of receiving p from both — so about a "
                 "quarter come out white, from two purple parents. This is "
                 "Mendel’s 3:1, and it is the result that made him think in "
                 "particles.",
             # 4. Everything else — a pp homozygote crossed with a Pp
             #    heterozygote. The fall-through, and it must stay last.
             "mixed":
                 "One parent carries two of the same version and the other "
                 "carries one of each. Watch the proportion rather than any "
                 "individual seed — chance decides each one, and only the "
                 "totals show the pattern.",
         }},

        # #s-steps — the band panel, and the section that gives the statutory
        # clause its four steps. Rail stop 3, mirroring `s-bench`.
        #
        # ⚠️ The card `role` values are Design's NUMBER BADGE digits; there is
        # no `num` slot in `_rule_card()`. See the docstring.
        {"type": "rule", "anchor": "s-steps",
         "eyebrow": "How the information travels",
         "statement": "Halved, combined, then copied into everything.",

         "cards": STEP_CARDS,

         # Design nests the key fact inside this section (page lines 182–185) on
         # the CARD ground with the 5px accent offset shadow. `card`, because
         # the section itself is `--ks3-band` and band on band is invisible —
         # the same arrangement and the same reason as b9-01's.
         "key_fact": {"ref": "heredity-halved-combined-copied",
                      "ground": "card"}},

        {"type": "misconception", "id": "blending-and-the-skipped-generation",
         "anchor": "s-think", "targets": "GENE-07"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-steps on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 185
    # and identical to payload schema §13's b10-04 entry.
    #
    # ⚖️ Its last clause is the flag 13 ruling performed rather than stated:
    # "one may be hidden for generations and still be passed on unchanged"
    # names no term, and it forecloses `GENE-08` — hidden, not weakened; passed
    # on unchanged, not lost and recreated.
    "key_facts": [
        {"id": "heredity-halved-combined-copied",
         "text": "Heredity is the transfer of genetic information from parents "
                 "to offspring. Each parent passes half their chromosomes in a "
                 "gamete, so offspring carry two versions of every gene, one "
                 "from each parent. Versions are not blended: one may be "
                 "hidden for generations and still be passed on unchanged.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, no
        # `sc-if`, schema §9), so it is a `confrontation` and not a `predict`,
        # it is not a rail stop, and it emits no completion contract.
        {"id": "blending-and-the-skipped-generation",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "GENE-07",
         "statements": [
             # GENE-07. ⚠️ `b10-01's` resolved to its lesson title — "What could
             # not be lifted" 1, and the possessive is what forces the
             # reordering. Every other word is Design's.
             #
             # ⚖️ The paragraph's first move is to say the belief was the
             # ACCEPTED VIEW and that Darwin worried about it. That is not
             # softening — it is the only honest framing, and it is what makes
             # the refutation an argument rather than a correction. Amber is a
             # wrong idea, never the student.
             {"quote": "Characteristics blend — a tall parent and a short "
                       "parent give a medium child.",
              "body": ["This was the accepted view for most of the nineteenth "
                       "century, and it has a fatal problem that Darwin "
                       "himself worried about: if characteristics blended, "
                       "then variation would halve with every generation and "
                       "after a few dozen generations every individual in a "
                       "species would be identical. Look around a classroom; "
                       "that has not happened. Mendel's peas showed why. Cross "
                       "a tall variety with a short one and the offspring are "
                       "all tall, not medium — and the shortness reappears, "
                       "undiluted, in the generation after. Information is "
                       "carried in discrete units that keep their identity, "
                       "and what you see is the result of which versions a "
                       "plant happens to be carrying. Height in people looks "
                       "like blending because hundreds of genes are involved, "
                       "which is the smooth curve in Variation: continuous and "
                       "discontinuous; underneath, each of those hundreds of "
                       "genes is being passed on whole."]},
             # GENE-08, and the reason the bench is upstream of it in the
             # document: "Set both parents on the bench to Pp" is a real
             # instruction about an instrument the student has already run, and
             # the six buttons it names are on the page above.
             #
             # ⚖️ The three `<em>` runs are kept — `rich()` renders them — and
             # each is load-bearing. `<em>Pp</em>` is the bench setting quoted
             # as a setting; the last two mark the distinction the whole
             # paragraph exists to draw, and italics are how the contrast is
             # made.
             #
             # ⚖️ NOT ONE WORD HERE CALLS THE HIDDEN VERSION WEAK, LOST OR USED
             # UP. "Doing nothing visible" is the strongest thing said about it,
             # and that is the flag 13 test passed in the one paragraph where it
             # would have been easiest to fail.
             {"quote": "It skipped a generation, so the gene must have "
                       "disappeared and come back.",
              "body": ["Nothing disappeared. A characteristic that is hidden "
                       "in one generation was being carried the whole time by "
                       "parents who did not show it, because they also carried "
                       "a version that overrides it. Set both parents on the "
                       "bench to <em>Pp</em> — both purple — and roughly a "
                       "quarter of the seeds come out white. The white version "
                       "was in both parents, in every one of their cells, "
                       "doing nothing visible. This matters far beyond peas: "
                       "it is why two people with no family history of a "
                       "condition can have a child who inherits it, and why "
                       "breeders and doctors distinguish between what an "
                       "organism shows and what it carries. The two questions "
                       "<em>what does it look like</em> and <em>what is it "
                       "carrying</em> have different answers, and only the "
                       "second one predicts the next generation."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — BOTH RUNGS CLEAN AS DRAWN. rung 1 correct 13w
    # against 11 / 13 / 7 and rung 2 correct 10w against 10 / 8 / 8; in both the
    # correct option TIES the longest distractor rather than exceeding it, so
    # `length_tell()` returns None and neither arm of the gate is reached.
    # **No option, no `answer` and no correction was touched on either rung**,
    # so there is no before/after to show — the counts above are both. The
    # reason each rung is clean, and the warning against a later pass "fixing"
    # them, is in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · The numbers",
            "q": "A human body cell has 46 chromosomes. How many are in a "
                 "sperm cell, and why?",
            # Design's four, untouched. Every one is a NUMBER plus the reason
            # for it, which is why the parity falls out of the construct rather
            # than being imposed on it.
            #
            #   A  correct
            #   B  authored belief: every cell in the body has the same number,
            #      gametes included
            #   C  the right number for the wrong reason — halving read as LOSS,
            #      which is the arithmetic form of GENE-08 and the reason this
            #      distractor is the dangerous one
            #   D  authored belief: the doubling happens before fertilisation
            #      rather than the halving happening before it
            "options": [
                "23 — one from each pair, so the fertilised egg has 46 again",
                "46 — every cell in the body has the same number",
                "23 — because half the chromosomes are lost when the sperm is "
                "made",
                "92 — the chromosomes double before fertilisation",
            ],
            "answer": 0,
            # Design's three, byte-identical. B's is the strongest correction on
            # the page because it runs the belief forward two generations and
            # lets the arithmetic refute it — 92, then 184 — rather than simply
            # naming it wrong.
            "feedback": {
                1: "Then fertilisation would give 92, and 184 in the "
                   "generation after that. Gametes must carry half.",
                2: "Right number, wrong reason. Nothing is lost — the "
                   "chromosomes are shared out between four gametes, each "
                   "getting a complete single set.",
                3: "The opposite. The number is halved to make a gamete, so "
                   "that fusing two of them restores it.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Two purple-flowered pea plants are crossed and about a "
                 "quarter of the offspring are white. What does that show?",
            # Design's four, untouched. All four are one-clause claims about a
            # CAUSE, which is why the correct answer is not longer by
            # construction.
            #
            #   A  correct
            #   B  GENE-08 in its commonest classroom form — the version was not
            #      there and then it was. This is why GENE-08 names `s-ladder`
            #      as its `elicited_by`.
            #   C  GENE-07 — blending, restated as blending-then-separating,
            #      which is the version that survives meeting the 3:1
            #   D  authored belief: an environmental cause for a proportion that
            #      is far too clean to be environmental
            "options": [
                "Both parents were carrying the white version without showing "
                "it",
                "A new white version appeared by mutation in the offspring",
                "The white parents’ characteristics blended and separated "
                "again",
                "Something in the soil turned those flowers white",
            ],
            "answer": 0,
            # Design's three, byte-identical. Each answers the belief its option
            # states rather than restating the correct answer: B is refuted on
            # FREQUENCY (a quarter is far too many for mutation), C on the
            # version being passed on unchanged, and D on the proportion being
            # the giveaway — the ratio itself is the evidence that this is
            # inheritance, which is the bench's whole argument.
            "feedback": {
                1: "A quarter of the offspring is far too many for that. "
                   "Mutation is rare; this ratio is what "
                   "carrying-without-showing predicts.",
                2: "Nothing blended. The white version was passed on "
                   "unchanged — that is exactly the point Mendel established.",
                3: "Flower colour here is set by the versions of the gene the "
                   "plant received. The proportion — close to a quarter — is "
                   "the giveaway that this is inheritance and not "
                   "environment.",
            }},
        # ⚖️ Criterion 5 is the rung's whole point and it is the flag 13 ruling
        # made assessable: "never lost or recreated — it was carried the whole
        # time" is `GENE-08` marked rather than merely contradicted. A student
        # can satisfy the first four criteria and still be holding the belief;
        # the fifth is the one that catches it.
        "explain": {
            "title": "Rung 3 · Explain the skipped generation",
            "q": "A characteristic appears in a grandparent, is absent in the "
                 "parents, and appears again in a grandchild. Explain how, "
                 "using what you know about versions of genes and how gametes "
                 "are made.",
            "field_label": "Your explanation",
            "placeholder": "The grandparent had two copies of…",
            "success": [
                "Says each individual carries two versions of the gene, one "
                "from each parent.",
                "Says one version can override the other, so an individual can "
                "carry a version without showing it.",
                "Says the parents each carried the hidden version and passed "
                "it on unchanged.",
                "Says the grandchild received that version from both parents, "
                "so there was nothing to override it.",
                "Makes clear the version was never lost or recreated — it was "
                "carried the whole time.",
            ]},
        # ⚑ Criteria 3 and 4 are where the UNSEEDED bench is marked. Criterion 3
        # marks a student for saying no individual puppy can be predicted, and
        # criterion 4 for saying a small litter may not show the ratio at all.
        # Against a seeded bench that always returned 75/25 both would be marks
        # for a claim the instrument on the same page contradicts — which is the
        # concrete cost of adding a seed, stated as a mark scheme.
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A dog breeder wants white-coated puppies, and white is the "
                 "hidden version of the coat-colour gene. She has two "
                 "coloured-coated dogs that have each produced a white puppy "
                 "in an earlier litter. Explain what she can predict, what she "
                 "cannot, and why breeding for a hidden characteristic is "
                 "easier than breeding one out.",
            "field_label": "Your answer",
            "placeholder": "Both dogs must be carrying…",
            "success": [
                "Says both dogs must be carrying the white version, because "
                "they have produced white puppies.",
                "Says roughly a quarter of the puppies in a litter would be "
                "expected to be white.",
                "Says she cannot predict any individual puppy — which version "
                "each gamete carries is chance.",
                "Says a small litter may not show the ratio at all, so the "
                "prediction is about large numbers.",
                "Explains that a white dog must carry two white versions and "
                "so breeds true, while a coloured dog may or may not be "
                "carrying white and cannot be identified by looking.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Heredity is the passing of genetic information from one "
                "generation to the next. Gametes carry half the chromosomes — "
                "23 in humans — so a fertilised egg has a full set of 46, half "
                "from each parent, and every cell of the new organism is a "
                "copy of that. Genes come in versions; an organism carries two "
                "of each and shows one, so a version can be carried without "
                "being shown and can reappear generations later.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B10 flag 14 lives entirely in this paragraph and is checked and
    # left; the working is in the docstring. ⚖️ MRB-225 holds: the layer adds
    # the history of how the claim was established and retracts nothing above
    # it. Design's hedge — "something like 28,000" — is load-bearing and must
    # not be trimmed to a bare figure.
    #
    # ⚖️ The paragraph's real argument is not biographical. "Other people had
    # crossed plants before and described the results; Mendel counted them" is
    # the working-scientifically claim of the whole lesson, and it is the reason
    # the bench has a hundred-seed button rather than a diagram: the ratio is
    # only visible to someone who counts.
    "stretch": [
        {"type": "explainer", "id": "the-man-who-counted-the-peas",
         "text": "Gregor Mendel was a monk running a garden in what is now the "
                 "Czech Republic, and between 1856 and 1863 he grew something "
                 "like 28,000 pea plants, counting the offspring of every "
                 "cross. Peas were an inspired choice: they self-pollinate, so "
                 "he could establish pure-breeding lines; they have several "
                 "characteristics that come in two clean forms; and they grow "
                 "fast. Counting was the real innovation. Other people had "
                 "crossed plants before and described the results; Mendel "
                 "counted them, found ratios close to 3:1, and realised the "
                 "ratio implied particles rather than fluids. He published in "
                 "1866 and was almost entirely ignored — his paper was cited a "
                 "handful of times in thirty-four years — and he died in 1884 "
                 "without knowing. Three separate botanists rediscovered the "
                 "same rules in 1900 and found his paper already there. It is "
                 "the clearest case in science of a correct answer arriving "
                 "before anyone had a use for it."},
    ],

    # ⚠️ EMPTY, AND MEASURED. Design draws NO `ks3-support` layer on this page —
    # grepped, zero occurrences — unlike b10-03, whose support layer carries the
    # Photo 51 credit note. Nothing is invented to fill the slot, and in
    # particular nothing is written here that would introduce "dominant" or
    # "recessive" as a scaffold, which schema §16 forbids by name.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C) — and the question it asks is one the
    # bench can actually answer, since predicting a cross before running it is
    # exactly what the six genotype buttons are for.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to work out what a cross would produce before you "
                      "run it?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 293) and nothing in it is a safety
    # instruction — it is a note about how far the bench's model can be trusted.
    # Routing it through `safety_note` would print it in the treatment reserved
    # for "never light a candle without an adult".
    #
    # ⚖️ ITS LAST CLAUSE IS THE UNSEEDED BENCH ARGUED IN WORDS: "a real 3:1
    # ratio only emerges over large numbers — which is why the hundred-seed
    # button exists". That sentence is false against a seeded bench, and it is
    # the first thing that would have to be edited by a pass that added a seed.
    # It stays.
    #
    # ⚑ Reported, not edited: this is the one place on the page where a form of
    # the held-back vocabulary appears — "a clean dominance rule", twice. It
    # describes the MODEL's scope rather than labelling anything a student is
    # taught or marked on, and MRB-205 says the page wins. See the docstring.
    "convention_note": "The bench uses one gene with two versions and a clean "
                       "dominance rule, which is the simplest case and the one "
                       "Mendel chose deliberately. Most characteristics "
                       "involve several genes, several versions and no clean "
                       "dominance, and a real 3:1 ratio only emerges over "
                       "large numbers — which is why the hundred-seed button "
                       "exists.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench produces a tally the student has to interpret as a proportion,
    # and rung 4 marks explicitly for distinguishing what can be predicted from
    # what cannot and for knowing that a small sample may not show the pattern.
    # That is the analysis-and-evaluation strand. Nothing on this page is
    # measured with an instrument, so `measurement` is not claimed, and the
    # student designs no procedure, so `experimental-skills-and-investigations`
    # is not either.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
