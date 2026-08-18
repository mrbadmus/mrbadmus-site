"""B11 L2 — Natural selection (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b11/b11-02-natural-selection.dc.html` (562 lines), her author's
notes `docs/ks3/design-reference/b11/NOTES-B11.md` §2 flags 4, 5 and 6, and the B11 payload
schema `docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md` §0, §1, §3, §6, §7, §8, §9, §10,
§11, §12, §13 and §14, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the six listed under "What could not be lifted". The three barks, the
five step cards, both marked rungs and both self-marked rungs came out of the
page's own `BARKS`, `STEP_CARDS`, `RUNGS` and `SELF_RUNGS` arrays via
`tools/extract_design_payload.js`; the hook options, the five bench notes, the
key fact, the key note, both *Going further* paragraphs, both `#s-think` bodies
and the legal line came out of the delivered markup and the delivered
`renderVals()`. No survival rate, criterion or correction was retyped.

── `covers`: the SECOND half of INH.05, and b11-01 owns the first ──────

`KS3.B.INH.05` is sub-split in `ks3_data/substatements.py` into exactly two
clauses, and the split was made for this unit: `05a` is *variation between and
within species meaning some organisms compete more successfully — and that which
variation helps depends on where the organism is*, which is b11-01's
`advantage-bench`; `05b` is *how that difference in competitive success,
repeated over generations, drives natural selection*, which is this page. The
substatement file's own comment says why they are not taught in one sitting:
teaching them together is what produces the belief that an individual adapts
during its own life, which is `EVOL-03` and is the most expensive misconception
in the unit. `build_ks3.validate()` enforces exactly-once ownership.

── ⚖️ THE TEACHING POINT IS THAT NOTHING CHANGES EXCEPT THE PROPORTION ──

From the KEY FACT, which is schema §9 verbatim: **individuals do not change —
populations do.** That single claim is made seven times over and every one of
them is Design's:

  * the big question opens *Not one animal in the population changes*;
  * the hook's reveal ends *No individual giraffe ever grew a longer neck. The
    average moved because of who had calves and who did not.*;
  * the bench intro says *watch the population change while no individual moth
    changes at all*, and `notes.dark_high` says it again with the run finished —
    *not one moth ever changed colour*;
  * step card 1 puts the variation BEFORE the change and step card 5 puts the
    shift AFTER many generations, so the arrow of the process is drawn twice;
  * `EVOL-03` is the claim that an individual changes itself, `EVOL-04` is the
    claim that a population does it on purpose, and `#s-think` takes both apart;
  * rung 1's three distractors are three ways of saying an individual changed,
    and rung 3's fifth criterion is *does not say that any moth changed colour*.

⛔ **No authored comment, bench note or ladder correction in this file lets an
individual change.** The `selection-runner` carries a fraction and nothing else —
no individuals are modelled at all, which is why the model cannot express the
wrong idea even by accident.

── The instrument: a closed-form recurrence, and the control is EXACT ───

`#s-bench` is `selection-runner`, on `ks3-block ks3-dark ks3-practical`
(page line 105), so `practical` is MEASURED from Design's own class attribute
rather than inferred from the kind name — schema §0 rule 3, and contract §4
records that B1 got two of six wrong by inferring it.

⚖️ **THERE IS NO RANDOMNESS AND THAT IS LOAD-BEARING** (schema §0 rule 2).
Each generation, with the current pale fraction `p`:

    survivors_pale = p · pale_surv
    survivors_dark = (1 − p) · dark_surv
    p′             = survivors_pale / (survivors_pale + survivors_dark)

Equivalently the odds `p/(1−p)` are multiplied by `pale_surv / dark_surv`, a
fixed constant per bark, every generation. Population size is not modelled — only
the fraction is carried, which is why the legal line says the population is held
constant. `grep -icE "math\\.random|<canvas|requestAnimationFrame"` returns 0 on
the delivered page. B11 teaches a process people wrongly imagine to be directed;
a stochastic bench would let a student watch a run go "the wrong way" and
conclude the model is broken, or watch a lucky run and conclude selection is a
lottery. **Never add a jitter, a shuffle or a "more realistic" sampling step.**

⚖️ **`mixed` IS THE CONTROL AND ITS TWO RATES MUST STAY BIT-FOR-BIT EQUAL.**
`0.70 == 0.70` makes `p′ === p` exactly, so the bars do not creep by a rounding
pixel over fifty generations. Any pass that "varies it slightly for realism"
destroys the one panel that shows selection *not* happening — which is the panel
that proves the other two are showing selection rather than an animation. Design
says it herself in the bark note: *Neither colour has an advantage, which makes
this the control.*

⛔ **NO RUNTIME STATE IS AUTHORED** (schema §0 rule 4). Design's state bag holds
`bark`, `pale`, `gen` and `history`; all four are the runtime's. `start_pale`,
`reset_pale` and `history_len` ARE authored because they are constants of the
MODEL that the recurrence reads, and schema §3 lists all three as keys.

⚠️ **AND THE OPENING BARK IS DELIBERATELY NOT A KEY.** Design opens on `sooty`,
which is `barks[1]` and not first. Schema §0 rule 4 rules that the opening values
are recorded as PROSE in §3 rather than as keys, and §3's key block has no
`start_bark`; §11 records that NOTES named a starting bark as a natural tweak and
that it does not exist in the delivered bytes. So the renderer opens on `sooty`
because §3 tells it to, not because this record does. **Reported to the commander
rather than resolved here**, because authoring the key would be authoring a key
the schema forbids and inventing one the other three authors will not have.

── ⚠️ THE RESET DEFECT, AND THE SIXTH `notes` ENTRY THIS PASS AUTHORS ──

Schema §11 item 3. `notes.start` is shown when `gen === 0` and reads *"Nine moths
in ten are pale, which is where the British population started."* `onReset` sets
`pale: 0.5, gen: 0` — so pressing **Start again at fifty-fifty** displays a
fifty-fifty population under a sentence saying nine in ten are pale. Design's
defect, in the delivered bytes, and not mentioned in NOTES.

The fix is schema §3's: gate `notes.start` on `gen === 0 && pale === start_pale`,
and carry a separate note for `gen === 0 && pale === reset_pale`. **This pass
authors that entry as `notes.reset`** — the only string in this record that is
not Design's, written to do exactly the job `notes.start` does one branch over:
state the proportion the student is looking at, then say what to do next.

⚠️ Schema §3 calls it *"a fifth entry"* and it is the SIXTH — the delivered
`renderVals()` already has five branches (`start`, `control`, `dark_high`,
`pale_high`, `moving`) and §3's own key block lists all five. An off-by-one in
the schema's prose, not in its instruction. **Reported.**

── FOUR rail stops, and the third is a MIRROR (MRB-249) ────────────────

Design draws four (page lines 342–347 in `RAIL`) and her `isDone()` gives
`s-steps` the BENCH's predicate, character for character, one line down:

    if (id === 's-bench') return s.gen >= 10;
    if (id === 's-steps') return s.gen >= 10;      // page lines 381–382

`#s-steps` is an eyebrow, a display statement, five numbered cards and a key
fact: no control, no commitment, no field, no reveal. It is the PAYOFF of the
bench beside it and carries no control precisely because the bench has already
taken the student's commitment. That relationship is a MIRROR, `wireRail`'s
`paint()` resolves it at rail level — which is the level Design computes it at —
and `ks3_parity.check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`, whose row for this page already reads
`s-hook s-bench s-steps s-ladder | s-steps=s-bench`.

⚠️ Schema §8's struck reasoning — *author three stops and drop the band* — is
REVERSED at the head of the same section and again at its foot, and the unit's
`__init__.py` records the call as made. Four is what Design drew and four is what
ships. Shipping three fails the build naming this page.

⚖️ **TEN GENERATIONS IS DESIGN'S OWN THRESHOLD AND IT IS READ TWICE**, once for
the bench and once for the mirror. It is also exactly one press of *Ten
generations*, so the stop is reachable in one action and the mirror ticks with
it — and on sooty bark ten generations from 90% pale reach about 99% dark, which
is the point at which `notes.dark_high` is the note on screen.

`#s-think` and `#s-keynote` are on no rail, and that is Design's too:
`#s-keynote` asks nothing, and `#s-think` here is static markup — two quotes, two
bodies, no options, no reveal, no button — so it is a `confrontation` and not
contract R1's `predict`. Schema §7, measured on all four B11 pages.

── What could not be lifted byte-identical, and why ────────────────────

Six. **No science word moves in any of them**; four are platform slot codes or a
delivered-bytes defect, and two are the MRB-177 distractor repair, which has its
own section below.

1. **`b11-01` in step card 2 — a slot code (§8.10).** Design writes *"This is
   where b11-01's competition comes in."* A student cannot resolve a slot code,
   and printing one is exactly the platform leakage §8.10 exists to stop.
   Resolved to the lesson TITLE, the way b9-02, b10-01 and b10-04 resolved the
   identical shape:

       Design:  This is where b11-01’s competition comes in.
       Built:   This is where the competition you met in Variation and
                competitive success comes in.

   The destination is not lost — `variation-and-competitive-success` is Design's
   own first *Before this lesson* card and is carried in `requires`.

2. **`b10-04` in step card 4 — the same defect.** Design writes *"This is
   b10-04's heredity doing the work."* The lesson title is *Passing it on:
   heredity*, which contains the word `heredity`, so the possessive cannot be
   substituted without saying the word twice in five words. Recast so that the
   science word is stated once and the title is a destination:

       Design:  This is b10-04’s heredity doing the work.
       Built:   This is heredity doing the work, and you met it in Passing it
                on: heredity.

   `passing-it-on-heredity` is Design's own second *Before this lesson* card and
   is carried in `requires`.

3. **TWO `\\u00b7` ESCAPES THAT LEAKED INTO THE MARKUP.** Page line 128 prints
   the axis note as `pale on top, dark below \\u00b7 one column per generation
   \\u00b7 oldest on the left` — two literal backslash-u-0-0-b-7 runs in the HTML
   body, not in the script block. Every other middot in this page's markup is the
   character itself (the head eyebrow, the bench eyebrow, the breadcrumb), and
   every `\\u00b7` and `\\u2014` inside the `<script>` is an ordinary JS escape
   that resolves. These two resolve to nothing: a browser would print twelve
   literal characters. Authored as the middots Design meant, which is also the
   value schema §3 records. **Reported as a defect in the delivered page rather
   than fixed silently** — it is b10-01's `\\u2014` leak again, one unit on.

4. **The bench notes are keyed, not branched.** Design's `renderVals()` computes
   the note with an if/else chain over `gen`, `bark` and `darkPct`. Schema §1
   names the key `notes` and §3 names the five branches, so the five strings are
   carried under `start`, `control`, `dark_high`, `pale_high` and `moving`
   byte-identical and the branching is the renderer's. No string changes.

5. **`notes.reset` is authored, not lifted** — it does not exist in the delivered
   bytes. See the reset-defect section above.

6. **Six ladder distractors rebuilt** — MRB-177, below. No correct option was
   shortened, no answer index moved, no correction edited.

── ⊕ MRB-177 LENGTH PARITY — BOTH MARKED RUNGS FAIL AS DRAWN, BOTH REPAIRED ─

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one word). The gate flags
a correct option that is strictly the longest AND clears the longest distractor
by ≥4 words or by ≥1.4×.

**Both rungs as Design drew them FAIL**, and both are the textbook instance of
the construct MRB-177 was ruled against: the correct answer states a RULE
(subject · condition · consequence) while each distractor states a short wrong
REASON in one clause. The ruling fixes the CONSTRUCT and not the threshold, so
**both correct options are untouched** and each distractor is rebuilt to state a
WRONG RULE in the same three-part shape, keeping the belief Design chose so that
every one of her corrections still answers it word for word.

    RUNG 1 — as drawn
    correct  19w  The proportions in the population — more of the moths born
                  were dark, because dark parents survived to breed
    A         8w  The moths gradually darkened to match the bark
    B         6w  The soot stained the moths dark
    C         7w  The pale moths learned to hide better
    strictly longest, gap 11, ratio 2.375 → TELL. A student who has read
    nothing can pick it by length alone.

    RUNG 1 — built
    A  belief: an individual changes to match its surroundings  (this is EVOL-03)
       Design:  The moths gradually darkened to match the bark                  8w
       Built:   The moths themselves gradually darkened, because an individual
                living on sooty bark changes colour to match it               17w
       Design's correction — "No moth changed colour at any point. A moth is
       the colour it hatched, and it stays that colour." — answers the rebuilt
       option exactly as it answered the first.
    B  belief: colour is APPLIED by the environment rather than inherited
       Design:  The soot stained the moths dark                                 6w
       Built:   The soot stained the moths dark, because anything resting on
                a blackened trunk is blackened too                            16w
       Design's clause survives whole; the `because` clause is the wrong rule
       her correction ("Then washing one would turn it pale…") already breaks.
    C  belief: learned behaviour is inherited
       Design:  The pale moths learned to hide better                           7w
       Built:   The pale moths learned to hide better, and passed what they
                had learned on to their offspring                             17w
       Her correction opens "Learning is not inherited", which is now the
       answer to the option's second clause rather than to something the
       option never claimed.
    correct 19w against 17 / 16 / 17 → still strictly longest, gap 2 (<4),
    ratio 1.118 (<1.4). CLEAN.

    RUNG 2 — as drawn
    correct  16w  Because changes made during an animal’s life do not alter
                  the genetic information it passes on
    A         8w  Because giraffes cannot stretch their necks at all
    C         8w  Because giraffes do not eat from tall trees
    D         6w  Because necks got shorter, not longer
    strictly longest, gap 8, ratio 2.000 → TELL.

    RUNG 2 — built
    A  belief: the story fails on the FACT rather than on the mechanism
       Design:  Because giraffes cannot stretch their necks at all              8w
       Built:   Because giraffes cannot stretch their necks at all, so there
                is nothing to pass on                                         15w
       Her correction — "They can stretch, and it makes no difference —
       stretching does not change the DNA in the gametes." — answers both
       clauses, and the second half of it is now doing visible work.
    C  same shape, the feeding denied instead of the stretching
       Design:  Because giraffes do not eat from tall trees                     8w
       Built:   Because giraffes do not eat from tall trees, so no stretching
                ever happened                                                 13w
    D  belief: the story fails on the DIRECTION of the change
       Design:  Because necks got shorter, not longer                           6w
       Built:   Because necks got shorter, not longer, so the direction in
                the story is wrong                                            14w
       Her correction ("They got longer. The question is how — by animals
       changing, or by which animals bred.") answers the first clause and
       then names the real question, unchanged.
    correct 16w against 15 / 13 / 14 → strictly longest, gap 1 (<4),
    ratio 1.067 (<1.4). CLEAN.

⛔ **NO CORRECT OPTION WAS SHORTENED, NO `answer` INDEX MOVED, AND NO CORRECTION
WAS EDITED.** All six of Design's corrections are byte-identical. The two correct
options are byte-identical, including the curly apostrophe in *animal’s*. Six
distractors changed and nothing else, which is the repair MRB-177 asked for.

⚠️ Rung 2's stem quotes the wrong story with STRAIGHT double quotes — *Why is
"giraffes stretched their necks…" wrong?* — where the `#s-think` quotes use
curly ones. That is Design's, it is inside a JS single-quoted string rather than
in markup, and it is left exactly as delivered.

── Misconception ids: EVOL-03 and EVOL-04, and EVOL-10 is UNUSED ───────

Schema §12's pre-allocation for b11-02, and the two beliefs Design's `#s-think`
quotes, in her page order. Both statements are her own bytes (page lines 176 and
180), in register voice with the curly quotes stripped — the renderer draws
those.

**Two beliefs were found and two ids were used. `EVOL-10`, this lesson's named
spare, is UNCLAIMED and stays permanently unused**, exactly like `DRUG-07` and
`GENE-11`. It is never re-pointed at a different belief in a later pass. No
second spare was needed, so nothing escalates.

⊕ **THE `EVOL` PREFIX ROW IS OPEN, AND IT AGREES WITH THIS FILE.** It was not
there when the schema was written — §11 item 5 records that NOTES-B11 §4 claims
these eight were "written into" the register and that `grep -n "EVOL"` returned
nothing — so it was checked rather than assumed. It has since been opened, and
its `EVOL-03` and `EVOL-04` rows match the two authored here on statement, on
`elicited_by` and on `confronted_by`, arrived at independently. Nothing to
reconcile. That file is in flight this session and is not this pass's to edit.

Both `elicited_by` values are `s-hook` and both `confronted_by` values are
`s-think`, and the doubling is measured rather than lazy. The register states it:
*the giraffe hook offers stretching-and-inheriting as option A and
needed-so-it-developed as option C, which is Design putting both costumes of one
wrong idea in front of the student before the lesson starts.* They carry separate
ids because the confrontations differ — `EVOL-03` fails on the mechanism of
inheritance, `EVOL-04` on a population having no way to want anything. The ladder
cannot be `EVOL-04`'s elicitation: no rung on this page offers a purpose-driven
option at all, and rung 2's stem hands the student the Lamarckian claim already
labelled as wrong.

The register also carries a `reappears_in` edge from `EVOL-01` (b11-01,
*survival of the fittest means the strongest survive*) to this lesson. That is a
register-side field; nothing in this record declares it, and nothing here
re-teaches `EVOL-01`.

── Keys this pass authors that the RENDERER reads (contract R5) ────────

Named explicitly rather than left to be discovered, all measured off schema §3
and Design's `renderVals()`:

    eyebrow / title / intro    the practical shell's head row and lead
    tabs_label                 the mono label over the three bark tabs
    gen_label /                the mono readout top-right; `gen_zero_label`
    gen_zero_label             exists because Design prints "generation 0"
                               rather than composing it
    barks                      tabs + note + the two survival rates that ARE
                               the model
    start_pale / reset_pale    the two opening fractions; `reset_pale` is also
                               the discriminator that gates `notes.reset`
    history_len                columns kept before the oldest shifts off left
    pale_label / dark_label    composed as "Pale 62%" / "Dark 38%"
    axis_note                  the mono caption under the columns
    one_label / ten_label /    the three buttons
    reset_label
    notes                      six states, one line each

⚠️ **THIS INSTRUMENT IS ON INK.** `.ks3-dark p` is (0,1,1) and beats a bare
component class at (0,1,0), so every colour rule for it has to be written at
(0,2,0) under `.ks3-dark …`, and `ks3_parity.check_dark_text_specificity()`
resolves it on the real cascade. Recorded here because this payload feeds it.

⚑ Schema §11 also records that `--ks3-alert` (amber) is used as the DARK-MOTH
data colour on this bench, which is the same ink the brand reserves for a wrong
idea being confronted. Nothing on the bench marks the student and no verdict is
authored at all, so §0.7 is not breached — but it is one ink doing two jobs on
one page, and it is a design-pass question rather than a payload key. Left as
drawn, flagged.

── figures: the moth pair, and what this pass could actually author ────

⭐ Schema §14 flag 16 RULES THE PEPPERED MOTH PAIR DRAWN, and it is the right
call: camouflage is the one idea in B11 that is genuinely and irreducibly visual,
and `selection-runner` shows the proportion changing over generations, which is
the CONSEQUENCE — it never shows the thing the consequence follows from.

**`figures: []` here is a REPORT, not a judgement.** `SVG_ART` in `build_ks3.py`
held exactly `food-web` and `base-pairs` when this pass ran; there is no
`moth-pair` drawer, and `r_figure` RAISES on a `status: "drawn"` figure whose
`art` it cannot draw — deliberately, so that a drawn figure with no drawer can
never ship as an empty `<figure>`. Authoring the record before the drawer exists
would therefore red the build for the other three authors as well as for this
one, and `build_ks3.py` is the engine pass's file, not this one's. So the slot is
left empty and the commander wires it. What the record needs, when it can be
written, is in the report.

Note that schema §13 predates the flag-16 ruling and still says `figures: []` on
all four "and that is deliberate". §14 is dated later and is the standing
authority; §13's MEASUREMENT (zero `<img>`, `<figure>`, `<picture>` and
`background-image` on the delivered page, ten `<svg>` elements all UI furniture)
is correct and is why the drawing has to be code rather than an asset.

── ⚑ For Mide's science gate — every NOTES-B11 flag landing on THIS lesson ─

Three flags, all three already RULED in schema §14 under this run's standing
authority, and none is re-opened here.

  * flag 4   **Lamarck treated with respect** rather than dismissed — a serious
             theory, right that species change, wrong on mechanism. RULED SHIP AS
             DRAWN, and §14 gives the reason: it is both better history and
             better teaching, and the respect makes the correction land harder.
             Design's body carries the three classic disproofs (the blacksmith's
             children, the mouse's tail, generations of haircuts) and then the
             general rule they share — *what an organism does during its life
             does not rewrite the DNA in its gametes*. Left exactly as drawn.
             ⛔ Do not let a later pass "tighten" this into mockery.
  * flag 5   **The two-paragraph *Going further*.** RULED KEEP BOTH. Design
             offers to move or cut the antibiotic-resistance paragraph because
             this layer now runs to two where no other lesson's does. §14: *Going
             further* is a layer the STUDENT chose, a student who opened it is
             not harmed by a second paragraph, and length uniformity across
             lessons is a habit, not a rule. The two do different jobs — the
             moth-method story is a *how do we know?* about the organism the
             lesson just taught, and antibiotic resistance is natural selection
             happening now in the only context where a student may one day act on
             it. Moving antibiotic resistance would strand it on a page whose
             bench is not about selection. **BOTH SHIP.**
  * flag 6   **"as prescribed".** RULED KEEP IT EXACTLY. The finish-the-course
             advice has been questioned in the research literature; *as
             prescribed* is deliberately the wording that survives that argument,
             because it defers to the prescriber rather than asserting that
             longer is always better. ⛔ Do not "modernise" it and do not expand
             it into the argument itself — this is a KS3 selection lesson, and
             the sentence's job is that every use of an antibiotic is a selection
             pressure.

── ⛔ THE PEPPERED MOTH IS TAUGHT PLAINLY. NO HEDGE, ANYWHERE IN THE BODY ─

Ruled 16 Aug and VERIFIED IN THE DELIVERED BYTES by schema §10, which checked it
sentence by sentence rather than in the abstract. Re-checked here on the built
record: no "some scientists", no "it is thought", no "the classic story", no "has
been questioned" appears in the bench intro, in any bark note, in any bench note,
in any step card, in either `#s-think` body, in any rung, in the key fact, in the
key note or in the legal line. The legal line covers the BENCH MODEL only —
*survival differences are fixed percentages, the population size is held
constant, and there is no mutation, migration or chance beyond the survival rates
themselves* — and says nothing about the science.

The method criticism lives in *Going further*, in full: Kettlewell's 1950s
release-recapture in Birmingham and Dorset, the three fair criticisms (released
by day, at unnatural densities, often onto exposed trunks when the moths mostly
rest higher up beneath branches), the period when the conclusion was wrongly
reported as having fallen with the method, and Majerus re-running it in the 2000s
in natural resting positions at natural densities with birds watched taking them,
same result more strongly, published in 2012 after his death.

⛔ **DO NOT ADD A QUALIFIER BACK — not to a body sentence, not to the legal line,
and not to a comment in this file that a later pass could lift into copy.** The
conclusion is sound. The reason the method story is in *Going further* is that it
is the strongest *how do we know?* story in the biology build, not that the
science needs a disclaimer.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes: *the population changes because of who
reproduced; no individual changes.* The hook's reveal, all three bark notes, all
six bench notes, all five step cards, both `#s-think` bodies, the key fact, rung
1's correct option, rung 3's fifth criterion and the key note all say it at the
same size. *Going further* retracts nothing: paragraph 1 strengthens the moth
case rather than weakening it, and paragraph 2 applies the identical claim to
bacteria — *they were there before the drug was ever used*.

── One phrase a later pass might read as a sequence leak, and should not ─

`Year 7`, `Year 8`, `Year 9`, `Year 10`, `Year 11` and `half-term` appear ZERO
times in this record — checked rather than assumed, and now gated in
`verify_ks3.py`. Every date in the lesson is HISTORICAL and is content: 1809
(Lamarck), the nineteenth century (industrial soot), the 1950s (Kettlewell), the
2000s and 2012 (Majerus). `typical_year` is metadata and reaches no page byte.
"generation" is a unit of the model, never a school year.
"""


# ── the three barks (page lines 350–357) ─────────────────────────────────
#
# Design's order, and the ORDER IS THE ARGUMENT: `clean` is the world before the
# factories, `sooty` is the world the page opens in, and `mixed` is the CONTROL
# that comes last because it only means something once the student has seen the
# other two move. The tabs do NOT reset the population, which is what lets a
# student run it sooty and then switch to clean and watch it come back —
# `notes.pale_high` is written for exactly that moment.
#
# ⛔ `pale_surv` AND `dark_surv` ARE THE WHOLE MODEL. They are the only numbers
# in it. `clean` multiplies the pale odds by 0.85/0.45 = ×1.889 every generation,
# `sooty` by 0.45/0.85 = ×0.529, and `mixed` by exactly 1. A third bark, a fourth
# rate, or a nudge to any of the six would change what the bench teaches while
# still drawing a perfectly plausible graph.
#
# ⚖️ `mixed` MUST STAY 0.70 AND 0.70. Equal to the bit, so `p′ === p` and the
# columns do not creep. See the docstring.
BARKS = [
    {"id": "clean", "label": "Clean, lichen-covered",
     "pale_surv": 0.85, "dark_surv": 0.45,
     "note": "Pale, mottled lichen on the trunks — the state of most woodland "
             "before industry, and again in many places today."},
    # The bark the page opens on — `barks[1]`, deliberately not first, and NOT
    # authored as a key. See the docstring: schema §3 records the opening
    # selection as prose and §0 rule 4 forbids the key.
    {"id": "sooty", "label": "Blackened by soot",
     "pale_surv": 0.45, "dark_surv": 0.85,
     "note": "Soot from coal-burning factories has killed the lichen and "
             "darkened the bark, as it did across industrial Britain in the "
             "nineteenth century."},
    # ⚑ THE CONTROL. Nothing moves, exactly, for ever.
    {"id": "mixed", "label": "Patchy, partly recovered",
     "pale_surv": 0.70, "dark_surv": 0.70,
     "note": "Some lichen returning, some bark still dark. Neither colour has "
             "an advantage, which makes this the control."},
]

# ── the five step cards in the band section (page lines 360–366) ─────────
#
# `num` + `name` + `body` is the badged card `_rule_card` reads — the accent
# square to the left of a two-row card, spanning both rows, which is the same
# component b10-04's `#s-steps` ships and is measured identically here. The digit
# is CONTENT: it is the card's position in a numbered process, and a renderer
# that computed it would be guessing at a list Design might have ordered
# differently.
#
# ⚖️ THE FIVE ARE A CHAIN AND THE ORDER IS THE MECHANISM. 1 puts the variation
# BEFORE the change, which is the whole of `EVOL-03`'s refutation; 3 says
# "Nothing is choosing", which is the whole of `EVOL-04`'s; and 5 is the one that
# stops a student expecting to see evolution happen in a single generation.
# Rung 3 asks for all five by name.
#
# ⚠️ Cards 2 and 4 carry the two slot codes resolved to lesson titles —
# "What could not be lifted" 1 and 2. No science word moves in either.
STEP_CARDS = [
    {"num": "1", "name": "Variation already exists",
     "body": "Individuals in the population differ, and the differences are "
             "there before anything changes. In the moths, pale and dark forms "
             "both existed long before the factories were built — dark ones "
             "were simply rare."},
    {"num": "2", "name": "More are born than survive",
     "body": "Every population produces far more offspring than the food, "
             "space and shelter can support, so most of them will not live to "
             "breed. This is where the competition you met in Variation and "
             "competitive success comes in."},
    {"num": "3", "name": "Some survive better than others",
     "body": "Whichever variations happen to suit the current conditions make "
             "survival more likely. Nothing is choosing; the environment "
             "simply kills a higher proportion of one kind."},
    {"num": "4", "name": "Survivors reproduce and pass it on",
     "body": "The survivors are the ones that breed, and they pass on the "
             "versions of the genes they carry — which are, on average, the "
             "ones that helped them survive. This is heredity doing the work, "
             "and you met it in Passing it on: heredity."},
    {"num": "5", "name": "Repeat, and the population shifts",
     "body": "A small change each generation, accumulated over many "
             "generations. Nothing dramatic happens in any single generation, "
             "and after fifty the population looks different."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 172 character for character.
    "slug":        "natural-selection",
    "title":       "Natural selection",
    "discipline":  "biology",
    "unit":        "evolution-extinction-and-biodiversity",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.INH.05b` — how a difference in competitive success, repeated over
    # generations, drives natural selection. `05a` is b11-01's; the split is in
    # `substatements.py` and was made for this unit. See the docstring.
    "covers":      ["KS3.B.INH.05b"],
    # Named, used, and owned elsewhere. INH.01 is b10-04's and every mention of
    # passing something on rests on it — step card 4 uses heredity and re-teaches
    # none of it. INH.02a is b10-02's: this page says "the versions of the genes
    # they carry" and "the DNA in its gametes" and explains neither. INH.04 is
    # b10-01's, and it is what makes "variation already exists" a sentence the
    # student can already picture.
    "touches":     ["KS3.B.INH.01", "KS3.B.INH.02a", "KS3.B.INH.04"],
    "beyond_statutory": False,
    # `genes-and-evolution` at `secure`: b5-02 opened it with gametes, B10
    # developed it through variation, DNA and heredity, and this is the lesson
    # where all of that is USED at once on something none of it was about — a
    # population over generations. `evidence-and-explanation` at `secure` too,
    # and it is earned rather than decorative: `#s-think` takes a serious theory
    # apart on its mechanism rather than on its conclusion, and *Going further*
    # is a method being attacked and a conclusion surviving a better test.
    "threads":     [{"id": "genes-and-evolution", "level": 3},
                    {"id": "evidence-and-explanation", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. Both are bare slugs —
    # `requires` resolves across the whole key stage, so the B10 edge needs no
    # unit — and both are the destinations of the two resolved slot codes in the
    # step cards, which is what makes those edges real rather than decorative.
    "requires":    ["variation-and-competitive-success", "passing-it-on-heredity"],
    "assumes":     [],
    # Design's "Connects to" card, in her order.
    #
    # ⚠️ `what-makes-a-species` MUST carry its unit. A bare slug in `references`
    # is resolved against the CURRENT unit — unlike `requires` — so the bare form
    # would build a link to a B11 page that does not exist and
    # `check_internal_links` would catch it. `when-the-environment-changes-
    # extinction` is b11-03, this unit's own, so a bare slug is correct there.
    "references":  ["when-the-environment-changes-extinction",
                    {"unit": "B10", "lesson": "what-makes-a-species"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Darwin and Wallace, the evidence for evolution, speciation, "
                   "mutation as the source of new variation, and selective "
                   "breeding as the contrast case.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Not one animal in the population changes. The population "
                    "changes, because of which animals had offspring — and "
                    "that is a completely different mechanism from the one "
                    "most people imagine.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-steps` is the third: no control of its
    # own, so it mirrors `s-bench` and ticks on the bench's predicate — Design's
    # own `isDone()`, page lines 381–382. `short` and `label` are her
    # `RAIL_SHORT` and `RAIL` strings. `docs/ks3/rail-manifest.md` already carries
    # the row `s-hook s-bench s-steps s-ladder | s-steps=s-bench`, so shipping
    # three fails `check_rail_matches_design` naming this page.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "The giraffe",
         "done_when": "committed"},
        # Design's own threshold, kept: `gen >= 10`, which is exactly one press
        # of "Ten generations". Sticky by her design and monotonic by ours — the
        # reset returns `gen` to 0 but `doneByDom` reads the emitted
        # `data-stage-done`, and MRB-208 has the instrument emit 0 on load so
        # nothing ticks before the student acts.
        {"anchor": "s-bench", "short": "BENCH", "label": "Run generations",
         "done_when": "ten_generations_run"},
        # The MIRROR. Design gives it the bench's predicate character for
        # character one line further down, so the stop ticks the moment the
        # bench does and nothing ticks on load.
        {"anchor": "s-steps", "short": "STEPS", "label": "Five steps",
         "mirrors": "s-bench",
         "done_when": "ten_generations_run"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key, and Design's own
    # reveal is gated on `hookChoice !== null` rather than on a right answer
    # (schema §6: all four hooks are four-option single-choice with the reveal
    # behind a commitment). B is the one the reveal endorses and it says so at
    # once; the hook is not a trick, it is the mechanism the bench then runs.
    #
    # ⚖️ OPTION A IS `EVOL-03` AND OPTION C IS `EVOL-04`, both word for word,
    # and that is why BOTH name this section as `elicited_by`. Design puts the
    # two costumes of one wrong idea in front of the student before the lesson
    # starts — an individual changing itself, and a population wanting something.
    # D is the third escape route students take, and it is the only one the
    # reveal does not need to argue with, because it does not explain the necks.
    "phenomenon": {
        "kind": "narrative",
        "title": "Giraffes have long necks. How did that happen?",
        "prompt": "The obvious story is that giraffes stretched for high "
                  "leaves, their necks lengthened a little, and they passed "
                  "the extra length on. It is a clear, sensible explanation, "
                  "it was the mainstream scientific view for fifty years, and "
                  "it is wrong in a way worth understanding precisely.",
        "commit": "What actually happened over those generations?",
        "options": [
            # A: EVOL-03, word for word, and this is its `elicited_by`
            "Giraffes stretched, and their calves inherited the extra length",
            # B: the one the reveal endorses
            "Neck length already varied, and longer-necked animals survived "
            "and bred more",
            # C: EVOL-04, word for word, and this is its `elicited_by`
            "The species needed longer necks, so they developed",
            # D: the migration escape — not a misconception about mechanism,
            # just a different story, and the reveal leaves it alone
            "Short-necked giraffes moved somewhere else",
        ],
        "reveal": "Neck length already varied. In hard times the longer-necked "
                  "animals reached food the others could not, survived better, "
                  "and had more offspring — who inherited the versions of the "
                  "genes that made necks long. No individual giraffe ever grew "
                  "a longer neck. The average moved because of who had calves "
                  "and who did not.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Schema §12's pre-allocation for b11-02, and the two beliefs Design's
    # `#s-think` quotes, in her page order. Both statements are her own bytes,
    # page lines 176 and 180, in register voice with the curly quotes stripped.
    #
    # ⊕ `docs/ks3/misconception-register.md`'s `EVOL` rows for these two ids
    # agree with these on statement, on `elicited_by` and on `confronted_by`.
    # That file is in flight this session and is not this pass's to edit.
    #
    # ⛔ `EVOL-10` is this lesson's named SPARE and is NOT claimed: two beliefs
    # were found and two ids were used. It stays permanently unused rather than
    # being re-pointed at anything later (schema §12).
    #
    # Both `elicited_by` values are `s-hook` — hook options A and C — and the
    # doubling is measured, not lazy. Both `confronted_by` values are `s-think`,
    # the confrontation block's emitted anchor, and all four resolve against the
    # BUILT page (MRB-244). Reasoning in the docstring.
    "misconceptions": [
        {"id": "EVOL-03",
         "statement": "Animals change themselves to suit their environment, "
                      "and pass the change on.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "EVOL-04",
         "statement": "The population needed to change, so it did.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B11, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its exclusion
    # list. Every definition below is authored, not lifted.
    #
    # ⚖️ Three of the six are glossed defensively, because the word itself is
    # what carries the misconception. `adaptation` is defined as a FEATURE and
    # the note says outright that it is not something an individual does —
    # a student who reads "adapt" as a verb has `EVOL-03` in one word.
    # `selection pressure` is glossed with "nothing is choosing", because the
    # word *selection* is the other half of the same problem. `generation` is
    # here because the whole mechanism only exists across them.
    "vocabulary": [
        {"term": "natural selection",
         "definition": "The process by which individuals whose variations suit "
                       "the conditions survive and reproduce more, so those "
                       "variations become more common over generations.",
         "note": "It acts on a population. It cannot act on an individual."},
        {"term": "adaptation",
         "definition": "A feature that makes an organism well suited to where "
                       "it lives.",
         "note": "A feature, not an action — no individual adapts during its "
                 "own life."},
        {"term": "selection pressure",
         "definition": "Anything in the environment that makes some variations "
                       "survive better than others.",
         "note": "A bird that eats what it can see. Nothing is choosing."},
        {"term": "variation",
         "definition": "The differences between individuals of the same "
                       "species.",
         "note": "It has to be there before the conditions change, or there is "
                 "nothing to select from."},
        {"term": "generation",
         "definition": "One complete round of a population being born, "
                       "surviving and reproducing.",
         "note": "Almost nothing happens in one. Everything happens in fifty."},
        {"term": "inherited",
         "definition": "Passed from parents to offspring through their genes.",
         "note": "What an organism does during its life is not inherited."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⭐ EMPTY, AND IT IS A REPORT RATHER THAN A JUDGEMENT. Schema §14 flag 16
    # RULES the peppered-moth pair drawn, and it is the right call. But `SVG_ART`
    # in `build_ks3.py` held only `food-web` and `base-pairs` when this pass ran,
    # `r_figure` RAISES on a `status: "drawn"` figure whose `art` it cannot draw,
    # and `build_ks3.py` is the engine pass's file. Authoring the record before
    # the drawer exists would red the build for four authors at once. The
    # commander wires it; the shape it needs is in the report and in the
    # docstring.
    # ⊕ DRAWN, 18 Aug 2026 — Mide's diagram ruling, and schema §14 rules THIS
    # figure specifically. It is the only diagram in B11 and the only one the
    # unit needs.
    #
    # Camouflage is the one idea here that is irreducibly visual. The whole
    # claim is whether a bird can pick a moth out against a background, and
    # `selection-runner` beside it shows the CONSEQUENCE — the proportion moving
    # over generations — not the thing the consequence follows from. A student
    # can run ten generations, watch the dark moths take over, and never once
    # have seen why.
    #
    # ⚠️ The two barks differ by PATTERN as well as tone (lichen mottle against
    # vertical soot streaks), and every moth carries a label and a note. That is
    # the never-colour-alone rule, and on this figure it is not a formality: a
    # reader who cannot separate the two tones is exactly the reader for whom a
    # picture of two greys is worth nothing, and they are the one person who
    # most needs the words.
    #
    # NOTES flag 16 asked for this and recorded that it was not in the diagram
    # manifest. It is now.
    "figures": [
        {"id": "b11-moth-pair",
         "kind": "diagram",
         "status": "drawn",
         "art": "moth-pair",
         "title": "The same two moths on two kinds of bark",
         # The `<desc>` does the whole job for a reader who cannot see it: what
         # is on each bark, and which moth is hard to find on which. Never a
         # copy of the caption — the caption addresses someone who can already
         # see the drawing.
         "desc": "Two panels side by side, each showing the same pair of "
                 "moths on a different bark. On the left, clean bark mottled "
                 "with lichen: the pale moth is almost invisible against it "
                 "and the dark moth stands out sharply. On the right, bark "
                 "blackened by soot and marked with vertical streaks: the "
                 "same pale moth now stands out sharply and the same dark "
                 "moth is almost invisible. Neither moth has changed. Only "
                 "the bark has.",
         "caption": "Neither moth changed. The bark did. A bird hunting on "
                    "the left panel finds the dark moth first; on the right "
                    "it finds the pale one — and being found is the whole of "
                    "the disadvantage.",
         "data": {
             "key": "Being hard to see is not a property of the moth. It is a "
                    "property of the moth and the background together.",
             "panels": [
                 {"bark": "lichen",
                  "label": "Clean, lichen-covered bark",
                  "moths": [
                      {"tone": "pale", "label": "Pale moth",
                       "note": "hard to see"},
                      {"tone": "dark", "label": "Dark moth",
                       "note": "easy to see"}]},
                 {"bark": "soot",
                  "label": "Bark blackened by soot",
                  "moths": [
                      {"tone": "pale", "label": "Pale moth",
                       "note": "easy to see"},
                      {"tone": "dark", "label": "Dark moth",
                       "note": "hard to see"}]}]}},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b11/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md §3. The read
        # sites are listed in the docstring; an opening bark and every one of
        # `bark`, `pale`, `gen` and `history` are deliberately absent, and each
        # has its own reason there.
        {"type": "selection-runner", "id": "run-the-generations",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · a hundred moths on a tree trunk",
         "title": "Run the generations",
         "intro": "Pale and dark moths resting on tree bark, hunted by birds "
                  "that find whatever they can see. Choose the bark, run the "
                  "generations, and watch the population change while no "
                  "individual moth changes at all.",

         # ⚑ The eyebrow says "a hundred moths" and nothing in the model is a
         # count of a hundred individuals — it is a proportion throughout.
         # Schema §3: lift it and leave it, because it is a reading aid and the
         # legal line already says the population is held constant. Recorded so
         # that nobody later "adds" a population of 100 to make it literal.

         "tabs_label": "The tree bark",
         "barks": BARKS,

         # ⚠️ `gen_label` CARRIES A TRAILING SPACE, which is schema §3's recorded
         # value and is how Design composes it: `'generation ' + s.gen`. The zero
         # case is a whole string of its own rather than a composition, which is
         # also hers. Both are authored as measured; if the renderer composes
         # with its own separator the space would double, and that is a
         # coordination point rather than a science one.
         "gen_label": "generation ",
         "gen_zero_label": "generation 0",

         # The two opening fractions. `start_pale` is the real historical
         # starting point and `notes.start` names it in words; `reset_pale` is
         # what "Start again at fifty-fifty" sets AND the discriminator that
         # tells `notes.reset` apart from `notes.start`, which is the whole of
         # the §11 item 3 fix.
         "start_pale": 0.9,
         "reset_pale": 0.5,
         # Columns kept before the oldest shifts off the left. Design's
         # `HISTORY`. Ten generations is one press, so 24 holds two full runs
         # and a bark switch without the student losing where they started.
         "history_len": 24,

         "pale_label": "Pale",
         "dark_label": "Dark",
         "axis_note": "pale on top, dark below · one column per generation · "
                      "oldest on the left",

         "one_label": "One generation",
         "ten_label": "Ten generations",
         "reset_label": "Start again at fifty-fifty",

         # ⚖️ SIX STATES, ONE LINE EACH, and the line under the readout is the
         # only place the bench SAYS anything. Nothing here marks the student and
         # no verdict is authored at all (schema §0.7) — these are descriptions
         # of a population, not judgements of a prediction.
         "notes": {
             # `gen === 0 && pale === start_pale`. The gate on the second half
             # is the §11 item 3 fix; without it this sentence is printed over a
             # fifty-fifty population after a reset.
             "start": "Nine moths in ten are pale, which is where the British "
                      "population started. Choose a bark and run some "
                      "generations.",
             # ⚠️ AUTHORED, NOT LIFTED — it does not exist in the delivered
             # bytes. `gen === 0 && pale === reset_pale`. Written to do exactly
             # what `notes.start` does one branch over: state the proportion on
             # screen, then say what to do next. It is honest about why
             # fifty-fifty is offered at all — it is not history, it is the
             # cleanest place to watch a change from.
             "reset": "Half the moths are pale and half are dark — not where "
                      "the British population started, but the clearest place "
                      "to watch a change from. Choose a bark and run some "
                      "generations.",
             # `bark === 'mixed'`. THE CONTROL, and the note says so in the
             # words that matter: without a difference in survival there is no
             # selection.
             "control": "Neither colour has an advantage on patchy bark, so "
                        "the proportions barely move however long you run it. "
                        "This is the control: without a difference in survival "
                        "there is no selection, only a population sitting "
                        "where it already was.",
             # `darkPct > 85`. The payoff of the sooty run, and the sentence
             # the whole lesson exists for.
             "dark_high": "The population is now overwhelmingly dark, and not "
                          "one moth ever changed colour. Every moth that has "
                          "ever lived in this simulation was born its colour "
                          "and died its colour. What moved was the proportion, "
                          "generation by generation, decided entirely by who "
                          "was eaten.",
             # `palePct > 85 && bark === 'clean'`. Written for the student who
             # ran it sooty and then switched — which the tabs allow on purpose,
             # because they do not reset the population.
             "pale_high": "On clean lichen the pale form is nearly invisible "
                          "and the dark form stands out, so the population "
                          "stays pale — or returns to pale, if you have "
                          "switched back after running it sooty. Selection has "
                          "no memory and no direction.",
             # Everything else. The line that stops a student expecting to see
             # evolution happen in one generation.
             "moving": "The proportions are shifting. Notice how little "
                       "changes in any single generation and how much has "
                       "changed after ten — that is the whole reason evolution "
                       "is hard to see happening."}},

        # #s-steps — the band panel, rail stop 3, mirroring `s-bench`. Design
        # draws eyebrow, statement, five badged cards, key fact — and NO closing
        # paragraph, so `close` is absent.
        {"type": "rule", "anchor": "s-steps",
         "eyebrow": "The process, in five steps",
         "statement": "Every step is something you have already met.",

         "cards": STEP_CARDS,

         # Design nests the key fact inside this section (page lines 369–372) on
         # the CARD ground with the 5px accent offset shadow. `card`, because the
         # section itself is `--ks3-band` and band on band is invisible — the
         # same arrangement and the same reason as b9-01's and b10-04's.
         "key_fact": {"ref": "natural-selection-in-four-moves",
                      "ground": "card"}},

        # Placed after `#s-steps`, the band that states the four steps of
        # natural selection — so the drawing lands on the step the student has
        # just read ("those whose variations suit the conditions survive and
        # reproduce more") and shows what "suit the conditions" looks like.
        {"type": "figure", "ref": "b11-moth-pair", "anchor": "s-moths"},

        {"type": "misconception", "id": "nothing-is-trying",
         "anchor": "s-think", "targets": "EVOL-03"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-steps on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 372
    # and identical to payload schema §9's b11-02 entry.
    #
    # ⚖️ ITS LAST SENTENCE IS THE LESSON. Four clauses of mechanism and then the
    # thing the mechanism means: individuals do not change, populations do. No
    # later pass may drop it as a summary of what came before — it is the claim
    # `EVOL-03` and `EVOL-04` both deny, and it is what rung 3's fifth criterion
    # marks.
    "key_facts": [
        {"id": "natural-selection-in-four-moves",
         "text": "Natural selection: individuals vary; those whose variations "
                 "suit the conditions survive and reproduce more; they pass "
                 "those variations to their offspring; over many generations "
                 "the population changes. Individuals do not change — "
                 "populations do.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, no `sc-if`,
        # schema §7), so it is a `confrontation` and not a `predict`, it is not a
        # rail stop, and it emits no completion contract. The commitment for this
        # lesson already lives in the hook, and a second one here would
        # double-count it.
        {"id": "nothing-is-trying",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "EVOL-03",
         "statements": [
             # EVOL-03. ⚑ NOTES-B11 flag 4, RULED SHIP AS DRAWN: Lamarck is
             # treated with respect rather than dismissed. The `<em>` run is kept
             # — `rich()` renders it — because "already there" is the load-bearing
             # phrase of the whole unit: the variation arrives BEFORE the
             # environment changes, not in response to it.
             #
             # ⛔ The last sentence is the peppered moth stated FLATLY, and it is
             # one of the sentences schema §10 checked. No hedge goes back in.
             {"quote": "Animals change themselves to suit their environment, "
                       "and pass the change on.",
              "body": ["This is Lamarck's idea, and it deserves respect rather "
                       "than mockery: it was a serious scientific theory, it "
                       "explained the observations available in 1809, and "
                       "Lamarck was right about the big thing — that species "
                       "change over time — when most people still thought they "
                       "did not. It fails on the mechanism. A blacksmith's "
                       "children are not born with thick arms; a mouse that "
                       "loses its tail has ordinary tailed offspring; and "
                       "generations of people cutting their hair has produced "
                       "nobody born bald. What an organism does during its "
                       "life does not rewrite the DNA in its gametes, so it "
                       "cannot be inherited. What natural selection needs "
                       "instead is variation that is <em>already there</em>, "
                       "arriving before the environment changes rather than in "
                       "response to it. The moths on the bench above were not "
                       "turned dark by soot; some were already dark and the "
                       "soot changed which ones got eaten."]},
             # EVOL-04. The two `<em>` runs are the TEST, and they are the reason
             # this body cannot be flattened: "developed" and "in order to" are
             # named as the two phrases that smuggle a purpose in, and a student
             # cannot watch for a phrase that has not been shown to them. The
             # paragraph then does what no assertion could — it names the COST of
             # getting it wrong (a population does not conjure up a variation it
             # lacks, it dies) and hands the reader the antibiotic case that
             # *Going further* picks up.
             {"quote": "The population needed to change, so it did.",
              "body": ["Nothing in this process is aiming at anything. There "
                       "is no need, no goal, no trying — natural selection is "
                       "the accumulated arithmetic of who happened to leave "
                       "more offspring, and it cannot look ahead. The language "
                       "makes this hard: it is almost impossible to describe "
                       "evolution without saying a species <em>developed</em> "
                       "a feature <em>in order to</em> do something, and every "
                       "one of those phrases smuggles in a purpose that is not "
                       "there. Watch the wording in the mastery ladder and in "
                       "your own answers. The consequences of getting it right "
                       "are real: a population facing a change it has no "
                       "existing variation for does not conjure one up, it "
                       "dies, and that is why extinction is common rather than "
                       "rare. And it is why antibiotic resistance appears "
                       "within years of a new drug — the resistant bacteria "
                       "were already in the population before the drug "
                       "arrived."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — BOTH MARKED RUNGS FAILED AS DRAWN AND BOTH ARE
    # REPAIRED AT THE DISTRACTOR. rung 1 correct 19w, strictly longest, gap 11,
    # ratio 2.375; rung 2 correct 16w, strictly longest, gap 8, ratio 2.000. Both
    # are the construct MRB-177 was ruled against — a correct answer stating a
    # RULE against three one-clause wrong REASONS — so both correct options are
    # UNCHANGED and each of the six distractors is rebuilt to state a WRONG RULE
    # in the same subject-condition-consequence shape, keeping Design's belief so
    # that every correction still answers it word for word. Repaired: rung 1
    # 19w against 17 / 16 / 17 (gap 2, ratio 1.118); rung 2 16w against
    # 15 / 13 / 14 (gap 1, ratio 1.067). No correct option shortened, no `answer`
    # index moved, no correction edited, no distractor padded with filler. Full
    # working, option by option, is in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · What changes",
            "q": "After fifty generations on sooty bark, most of the moths are "
                 "dark. What changed?",
            # All four now state a rule about WHAT changed and why. ⚑ Option B
            # is `EVOL-03` in the student's own words with its rule made
            # explicit; C is the colour-is-applied belief; D is the
            # learning-is-inherited belief, which is `EVOL-03`'s cousin one step
            # further out. None is a register entry in its own right — the hook
            # is where both registered beliefs are elicited.
            #
            #   A  correct — the proportion moved, and the reason is who bred
            #   B  the individual changed to match the bark
            #   C  the environment applied the colour
            #   D  the individual learned, and taught its offspring
            "options": [
                "The proportions in the population — more of the moths born "
                "were dark, because dark parents survived to breed",
                "The moths themselves gradually darkened, because an "
                "individual living on sooty bark changes colour to match it",
                "The soot stained the moths dark, because anything resting on "
                "a blackened trunk is blackened too",
                "The pale moths learned to hide better, and passed what they "
                "had learned on to their offspring",
            ],
            "answer": 0,
            # All three corrections are Design's, byte-identical. Each answers
            # exactly the belief its own option states, and each still lands on
            # the rebuilt option — which is the test the repair had to pass.
            "feedback": {
                1: "No moth changed colour at any point. A moth is the colour "
                   "it hatched, and it stays that colour.",
                2: "Then washing one would turn it pale, and its offspring "
                   "would be pale anyway. The colour is inherited, not "
                   "applied.",
                3: "Learning is not inherited, and it is not what the graph "
                   "shows — the pale ones did not survive better, there were "
                   "simply fewer of them being born.",
            }},
        "apply": {
            # ⚖️ THE RUNG THAT MARKS LAMARCK. The stem hands the student the
            # wrong story already labelled wrong and asks WHY it is wrong, so
            # every option is a candidate reason and only one is about the
            # mechanism of inheritance. Three of the four attack a FACT in the
            # story — the stretching, the feeding, the direction — and are the
            # three ways a student avoids the mechanism without noticing.
            "title": "Rung 2 · The one that catches people",
            "q": "Why is \"giraffes stretched their necks and passed the extra "
                 "length to their calves\" wrong?",
            # ⚠️ Design's straight double quotes in the stem are hers and are
            # left as delivered; the curly quotes on this page are all in
            # `#s-think`.
            #
            #   A  denies the stretching
            #   B  correct: the mechanism of inheritance is what fails
            #   C  denies the feeding
            #   D  denies the direction of the change
            "options": [
                "Because giraffes cannot stretch their necks at all, so there "
                "is nothing to pass on",
                "Because changes made during an animal’s life do not "
                "alter the genetic information it passes on",
                "Because giraffes do not eat from tall trees, so no stretching "
                "ever happened",
                "Because necks got shorter, not longer, so the direction in "
                "the story is wrong",
            ],
            "answer": 1,
            # All three corrections are Design's, byte-identical. D's is the one
            # that does the lesson's real work: it concedes the observation and
            # then re-asks the only question that matters — by animals changing,
            # or by which animals bred.
            "feedback": {
                0: "They can stretch, and it makes no difference — stretching "
                   "does not change the DNA in the gametes.",
                2: "They do. The feeding is real; the mechanism of inheritance "
                   "in the story is what fails.",
                3: "They got longer. The question is how — by animals "
                   "changing, or by which animals bred.",
            }},
        "explain": {
            # ⚖️ THE RUNG THE FIVE STEP CARDS ARE WRITTEN FOR, and the fifth
            # criterion is the one that cannot be met by accident: it marks the
            # ABSENCE of the wrong idea. A student can hit the first four with a
            # narrative that still has the moths darkening.
            "title": "Rung 3 · Explain it properly",
            "q": "Explain how a population of mainly pale moths became a "
                 "population of mainly dark moths after the bark was blackened "
                 "by soot. Use all five steps, and be careful not to say the "
                 "moths changed.",
            "field_label": "Your explanation",
            "placeholder": "Both pale and dark moths already existed…",
            "success": [
                "Says both pale and dark moths already existed before the bark "
                "darkened.",
                "Says birds could see the pale moths more easily against the "
                "dark bark, so more of them were eaten.",
                "Says more dark moths therefore survived to reproduce.",
                "Says the surviving dark moths passed on the genes for dark "
                "colour to their offspring.",
                "Says the proportion of dark moths increased over many "
                "generations — and does not say that any moth changed colour.",
            ]},
        "produce": {
            # ⚑ The transfer rung, and the reason *Going further*'s second
            # paragraph belongs on THIS page (§14 flag 5): the student has just
            # run the same mechanism on an insect population, so the antibiotic
            # paragraph is a third instance of a pattern rather than a fourth
            # unrelated fact. The fifth criterion asks for the pattern by name.
            "title": "Rung 4 · Take it somewhere new",
            "q": "A farmer sprays a pesticide that kills 99% of the insect "
                 "pests. Within three years it barely works at all. Explain "
                 "what has happened, why spraying more of it makes the problem "
                 "worse, and what this shares with the moth bench.",
            "field_label": "Your answer",
            "placeholder": "A few insects in the original population…",
            "success": [
                "Says a few insects in the original population happened to be "
                "resistant, before the pesticide was used.",
                "Says the pesticide killed the others, leaving the resistant "
                "ones with little competition.",
                "Says those survivors bred and passed resistance on, so the "
                "proportion of resistant insects rose each generation.",
                "Says spraying more applies the same selection pressure harder "
                "and speeds the process up.",
                "Identifies the shared mechanism: existing variation plus a "
                "change in what survives, with no individual insect becoming "
                "resistant during its life.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Natural selection needs four things: variation that already "
                "exists in the population, competition because more are born "
                "than can survive, a difference in who survives and "
                "reproduces, and inheritance so the surviving variations are "
                "passed on. Repeat over many generations and the population "
                "changes. No individual adapts during its own life, and the "
                "process has no goal.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚠️ TWO PARAGRAPHS, AND BOTH SHIP. Schema §14 flag 5 RULES IT: Design offers
    # to move or cut the second because this layer runs to two where no other
    # lesson's does, and the answer is keep both. *Going further* is a layer the
    # STUDENT chose; the two do different jobs — a *how do we know?* about the
    # organism the lesson just taught, and natural selection happening now in the
    # only context where a student may one day act on it — and moving antibiotic
    # resistance would strand it on a page whose bench is not about selection.
    # Length uniformity across lessons is a habit, not a rule.
    #
    # ⛔ THIS IS WHERE THE METHOD CRITICISM LIVES, AND IT IS THE ONLY PLACE ON
    # THE PAGE THAT QUALIFIES ANYTHING. The lesson body states the moth science
    # flatly (§10, verified in the delivered bytes). Paragraph 1 is not a
    # disclaimer — it strengthens the conclusion, and its last two sentences are
    # the transferable point about how science actually works. ⚑ NOTES-B11 flag 5.
    "stretch": [
        {"type": "explainer", "id": "how-do-we-know-about-the-moths",
         "text": "Ask <em>how do we know?</em> about the moths and you get the "
                 "best answer in this book. Bernard Kettlewell tested the idea "
                 "directly in the 1950s: he released marked pale and dark "
                 "moths into a polluted wood near Birmingham and an unpolluted "
                 "one in Dorset, recaptured what he could, and in each wood "
                 "the better-hidden form came back in greater numbers. It was "
                 "in every textbook within a decade — and then the method was "
                 "taken apart. He had released moths by day, at densities no "
                 "real wood would hold, and often onto exposed trunks, when "
                 "peppered moths mostly rest higher up beneath branches. Those "
                 "criticisms were fair, and for a while they were reported as "
                 "though the conclusion had fallen with the method. It had "
                 "not. Michael Majerus spent the 2000s running the experiment "
                 "the way the critics said it should be run — moths in natural "
                 "resting positions, at natural densities, with birds watched "
                 "taking them — and got the same result, more strongly; the "
                 "findings were published in 2012, after his death. That "
                 "sequence is not an embarrassment for science, it is the "
                 "whole of science in one example. A conclusion is only ever "
                 "as good as the method behind it, so someone attacks the "
                 "method, and a conclusion that survives a better test than "
                 "the one that first produced it is standing on firmer ground "
                 "than before."},
        # ⚑ NOTES-B11 flag 6, RULED KEEP EXACTLY: "as prescribed" is deliberately
        # the wording that survives the current research argument about finishing
        # a course, because it defers to the prescriber rather than asserting
        # that longer is always better. ⛔ Do not "modernise" it, and do not
        # expand it into the argument — the sentence's job here is that every use
        # of an antibiotic is a selection pressure.
        {"type": "explainer", "id": "antibiotic-resistance-is-this-happening-now",
         "text": "Antibiotic resistance is natural selection happening fast "
                 "enough to be a public health emergency. In any large "
                 "population of bacteria a few individuals happen to carry a "
                 "version of a gene that lets them survive a particular "
                 "antibiotic — they were there before the drug was ever used, "
                 "produced by ordinary random mutation. Give the antibiotic "
                 "and it kills the rest, which leaves the resistant few with "
                 "no competition and an empty patient to reproduce into. "
                 "Bacteria divide every twenty minutes, so a population that "
                 "is almost entirely susceptible in the morning can be almost "
                 "entirely resistant within days. This is exactly the moth "
                 "bench with the generation time reduced from a year to twenty "
                 "minutes, and it is why finishing a course as prescribed, and "
                 "not demanding antibiotics for a virus, are not fussiness. "
                 "Every use of an antibiotic is a selection pressure applied "
                 "to every bacterium in the person taking it."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C), and the ask is the sharpest one in
    # the unit — it invites the student to bring their own sentence back and have
    # the purpose hunted out of it, which is `EVOL-04` turned into an offer.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check whether your explanation smuggles in a "
                      "purpose?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 311) and nothing in it is a safety
    # instruction — it is a statement of what the simulation does and does not
    # model. Routing it through `safety_note` would print it in the treatment
    # reserved for "never light a candle without an adult".
    #
    # ⛔ ⚑ NOTES-B11 flag 5 / schema §10(b). THIS LINE COVERS THE BENCH MODEL
    # ONLY. The caveat sentence about the science was CUT under the 16 Aug
    # ruling, and it does not come back. Every clause here is about the
    # simulation: fixed percentages, constant population size, and no mutation,
    # migration or chance. It is also the line that keeps the "hundred moths"
    # eyebrow honest.
    "convention_note": "The moth bench is a teaching model: survival "
                       "differences are fixed percentages, the population size "
                       "is held constant, and there is no mutation, migration "
                       "or chance beyond the survival rates themselves.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is `interpret observations and data` performed rather than
    # described — the student reads a changing proportion off a column chart and
    # the notes say what it means — and rung 3 asks for that reading in prose.
    # `scientific-attitudes` is earned twice over: `#s-think` evaluates a serious
    # historical theory on its mechanism, and *Going further* is a method being
    # attacked and a conclusion surviving a better test. Nothing here is measured
    # by the student and nothing is planned, so neither `measurement` nor the
    # experimental strand is claimed.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
