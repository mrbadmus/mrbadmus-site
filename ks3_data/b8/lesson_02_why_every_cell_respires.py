"""B8 L2 — Why every cell respires (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b8/b8-02-why-every-cell-respires.dc.html` (559 lines), her author's
notes `docs/ks3/design-reference/b8/NOTES-B8.md`, and the B8 payload schema
`docs/ks3/b8-inventory/PAYLOAD-SCHEMA.md` §3, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the four items under "What could not be lifted" and the one science
correction under `⊕`, all of which are itemised below. The five cells, the four
job cards, the four hook options, both marked rungs and both self-marked rungs
came out of `node tools/extract_design_payload.js`, not off a keyboard.

── `covers` is the SECOND CLAUSE of a two-clause bullet, and that clause is
   the whole lesson ────────────────────────────────────────────────────────

`KS3.B.RESP.01` reads, in full:

    aerobic and anaerobic respiration in living organisms, including the
    breakdown of organic molecules to enable all the other chemical processes
    necessary for life

NOTES-B8 §0 assigns the bullet to *"b8-01 and b8-02 together"*, and says the
second clause — *enabling all the other chemical processes* — *"is the whole of
b8-02 and is the one usually skipped"*. That is right about the teaching and
cannot be said in `covers`: `build_ks3.validate()` gates
*"every subject-content statement owned exactly once"*, and `substatements.py`
carries no `RESP` split. So this lesson claims the bullet WHOLE, on the
commander's dispatch.

⚑ **COORDINATION POINT, REPORTED.** Exactly-once means `b8-01` must NOT also
claim `KS3.B.RESP.01`; its statement is `KS3.B.RESP.02` (the word summary). If
both units' passes claim it the build goes red on that check, and the honest fix
is a lazy `substatements.py` split — `KS3.B.RESP.01a` (aerobic and anaerobic
respiration in living organisms) to b8-01, `KS3.B.RESP.01b` (the breakdown of
organic molecules enabling every other chemical process) to this lesson. That is
a one-line mint in a file this pass does not own, so it is reported rather than
taken.

The clause is discharged one-to-one by Design's `#s-jobs` cards, which is why
that section is not decoration and why its four cards may not be trimmed to
three:

    movement                     Job one
    building large molecules     Job two
    active transport             Job three
    keeping warm                 Job four

"all the OTHER chemical processes" is the load-bearing word. Job one is the only
one a student already believes, and the panel's own display statement — *"Only
one of them is moving."* — is the sentence that turns the clause over.

── The flagship: five cells, and the plant one is why it exists ──────────

`#s-bench` is `cell-demand`, on `ks3-block ks3-dark ks3-practical` (page line
105), so `practical` is MEASURED off Design's own markup rather than inherited
from the hook above it — payload schema §0 rule 2, and contract §4 records that
B1 got two of six wrong that way.

⚖️ **The root hair cell is the load-bearing tab and it is not smoothed into the
shape of the other four.** It is the only plant cell of the five; it is what
makes `RESP-03` unarguable, because it is a cell that does no movement of any
kind and still spends three quarters of its energy budget; and its `fails` line
— mineral uptake stops, water uptake does not, so the plant goes short of
minerals long before it goes short of water — is what sets up rung 4 on
waterlogged soil and b8-05's `root` case. The other four are animal cells whose
energy bill a student can already picture as effort (contracting, signalling,
swimming, crawling). This one cannot be read that way at all, which is the
entire argument of the lesson arriving as a tab rather than as a sentence.

`done_after` is **3**, which is Design's own threshold (`seen >= 3`, page line
403) and not a round number chosen here. Three of five means a student cannot
reach the stop on the two animal cells nearest their prior belief alone.

── FOUR rail stops — Design's fourth restored (MRB-249) ──────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that a rail
stop came off, and called the reason measured rather than stylistic. Design
draws FOUR stops and `#s-jobs` ticks on the BENCH's seen-count (page line 404:
`if (id === 's-jobs') return seen >= 3;` — the identical predicate to `s-bench`
one line above it). `#s-jobs` itself is an eyebrow, a display statement, four
static cards and a key fact: no control, no commitment, no field. The argument
was that `ks3_parity.check_rail_reachable()` fails a stop whose section carries
none of the five DOM signals `doneByDom()` reads, and that ALIASING it to the
bench would tick a stop for something the student did in a different section —
which is what MRB-208's completion rule exists to prevent. So THREE stops
shipped, ruled for the whole unit in `ks3_data/b8/__init__.py` before dispatch.

The measurement was right and the conclusion was wrong.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine. Dropping a stop Design drew is not
rendering what Design drew.

And the two consecutive lines are Design stating how the second stop ticks, in
a rail-level function. That is not an alias. The four jobs are the payoff of
the five cells beside them — the section carries no control precisely because
the bench has already taken the student's commitment. That relationship has a
name now, a MIRROR, and `wireRail`'s `paint()` resolves mirrors at rail level
instead of hunting for a DOM signal inside the section.

So the fourth stop is declared: anchor `s-jobs`, `mirrors: "s-bench"`,
`done_when: "three_cells_cut"` — Design's `JOBS` / "Four jobs", ticking on her
`seen >= 3` — and `check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`. **The section keeps its `anchor`**, as it always
did, so every hash link into it still works and `RESP-04`'s `elicited_by` still
resolves: the MRB-244/248 gate wants an emitted `id`, and that is unrelated to
the rail.

── What could not be lifted byte-identical, and why ─────────────────────

1. **The inline link in the first confrontation.** Design writes *"The
   day-and-night version of this is
   `<a href="b4-05-stomata-and-gas-exchange-in-plants.html">b4-05's</a>`."*
   Two separate problems, and b7-04 hit the identical pair one unit earlier.
   `rich()` allows `<em>` and `<strong>` and nothing else, so the tag cannot
   survive; and left as plain text *"b4-05's"* puts a build-internal slot code
   in front of a student, which they cannot resolve and which §8.10 exists to
   stop. Resolved to what the code stands for:

       Design:  The day-and-night version of this is <a …>b4-05's</a>.
       Built:   The day-and-night version of this is the subject of Stomata
                and gas exchange in plants.

   No science word moves. The destination is carried as a real `references`
   edge, and Design draws it in "Connects to" as well.

2. **`b5-02` in the sperm cell's mitochondria line.** Same rule, same fix,
   inside instrument copy rather than prose: *"You met this cell in b5-02."* →
   *"You met this cell in Gametes and fertilisation."*, with a `references`
   edge to `gametes-and-fertilisation` that Design's endmatter does not draw.
   The edge is added rather than the destination dropped: a named lesson a
   student cannot navigate to is worse than the code was.

3. **`b4-03` in rung 1's third correction.** Same rule again — *"as you
   established in b4-03."* → *"as you established in Alveoli: built for
   exchange."*, with the matching `references` edge. The lesson title carries a
   colon and reads a little stiffly inside the sentence; that is the cost of
   not printing a slot code, and it is the cost b7-03 and b7-04 both paid.

4. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose (*"Metabolism, ATP, active transport across membranes…"*) and
   §4.8.1 D makes the two mutually exclusive.

The `#s-jobs` cards, by contrast, ARE lifted whole and in Design's own four
parts — `role` / `term` / `gloss` map exactly onto her `kind` / `name` / `body`
since MRB-245 widened `_rule_card`. b7-04 had to join tag and name with a middle
dot; this lesson does not, and the key fact stays NESTED on the card ground
where Design draws it (page lines 172–175) because `r_rule` has taken a nested
`key_fact` since the same change.

── ⊕ MRB-225 — ONE OVERSTATEMENT IN THE HOOK, CORRECTED IN THE BODY ──────

**NOTES-B8 flag 6 is the flag Design most wanted answered, and the answer is
that the four-minute figure is already right and the sentence four lines below
it is not.**

Flag 6 asks whether *"three weeks, three days, four minutes"* is framed
correctly, given that the four minutes is the onset of brain damage rather than
death. Checked against what the page actually says, at all four sites:

    big question   "Minutes without oxygen."                      no claim
    hook heading   "Three weeks, three days, four minutes."       no claim
    hook prompt    "…about four minutes before permanent damage
                    begins."                                      CORRECT
    nerve cell     "Brain cells begin to die within about four
                    minutes…"                                     CORRECT

Design never states four minutes as time-to-death. The prompt names the onset of
permanent damage explicitly and the bench names cell death beginning, which is
the same event. Flag 6's premise does not hold against the page: nothing needed
shrinking there, and the heading is an incomplete statement completed by the
next sentence, not a claim retracted by one.

⊕ **The hook REVEAL is the defect, and it is the one flag 6 was reaching for.**
Design wrote:

    Stop the supply and every cell in the body stops respiring at once, which
    means every process in the body stops at once.

Two things wrong with that, and the second is fatal on its own page:

  (i) Cells deprived of oxygen do not stop respiring. They respire
      ANAEROBICALLY — which is `b8-03`, in this unit, three lessons from here,
      and it is half of the very statement this lesson claims (*"aerobic and
      anaerobic respiration in living organisms"*). A student who reads this
      sentence and then meets b8-03 has been told two incompatible things.
 (ii) *"every process in the body stops at once"* contradicts the SAME SECTION,
      three sentences earlier: if everything stopped at once there would be no
      four minutes to have permanent damage begin at the end of. The section
      argues against itself.

Corrected under the standing rule that where an approved page contradicts a
matter of fact the fact wins, and it is the narrowest edit that makes it true:

    Design:  …every cell in the body stops respiring at once, which means every
             process in the body stops at once.
    Built:   …every cell in the body loses its main source of energy at once,
             which is why the deadline is minutes rather than weeks.

The rhetoric survives whole — *"every cell … at once"* is the point, and it is
the point because it is what separates oxygen from food, which is one organ at a
time. The simultaneity is kept, the false instantaneous stop is not, and the new
clause lands back on the three numbers the hook opened with. b8-03 now ADDS the
anaerobic reserve to this instead of taking something back from it.

── ⊕ MRB-245's osmosis ruling, applied — the LABEL goes, the idea stays ──

The page names osmosis twice: in the root hair cell's `fails` line and in rung
1's second option and its correction. `ks3_data/` contains **zero** student-
facing uses of the word — b1-06 describes a contractile vacuole *"again avoiding
osmosis by name"*, b4-05 teaches guard cells going turgid without it, and
b7-03's Going further had the term stripped under MRB-245 with the finding
recorded as a key-stage position: *"If Mide wants osmosis named at KS3 that is a
key-stage ruling, not a b7-03 edit."*

Shipping three fresh uses here would reverse that ruling silently, which is
worse than either answer to it. So the label is removed at both sites and the
idea is kept in full, in words the student already has from b4-03's diffusion:

    root `fails`   "Water still moves in by osmosis, which needs no energy"
                 → "Water still moves in on its own, which needs no energy"
    rung 1 opt B   "Water moving into a root by osmosis"
                 → "Water moving into a root from the soil"
    rung 1 corr B  "Osmosis is diffusion of water down its own gradient and
                    needs no energy supply."
                 → "Water moves into a root by diffusion, down its own
                    gradient, and needs no energy supply."

The second sentence of that correction is untouched, and it is the one carrying
the teaching point (minerals run short before water does). This is the second
Design delivery in two units to reach for the term; if Mide wants it named at
KS3 that is now a live question rather than a hypothetical, and answering it yes
would move `b1-06`, `b4-05`, `b7-03` and these three sites together.

── MRB-177 — MEASURED, AND NEITHER RUNG NEEDED REPAIR ───────────────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one):

    rung 1  correct 9w vs 8 / 8 / 5    ✓ (gap 1; the gate wants ≥4 or ≥1.4×)
    rung 2  correct 11w vs 10 / 14 / 9 ✓ (the correct answer is not the longest)

Rung 1's construct is a LIST OF PROCESSES, not a rule-stating rung: all four
options are noun phrases naming a process, so the shape MRB-177 repairs — a
correct answer that states subject, condition and consequence against
distractors that state one clause — does not arise. Rung 2's correct option is
the third-longest of four. **No distractor was rewritten for length.** The one
distractor edited (rung 1 B) was edited for the osmosis ruling above and its
token count moved 7 → 8, away from the correct answer's 9 rather than toward it.

⚖️ Every correct option, both `answer` indices, Design's option ORDER, and all
six corrections are byte-identical apart from the two label-and-code edits
itemised above.

⚑ For Mide's science gate — NOTES-B8's flags landing on THIS lesson, and what
  was checked against each:

  * flag 6   **"Three weeks, three days, four minutes."** ANSWERED ABOVE. The
             four-minute framing was already correct at every site; the
             overstatement was elsewhere in the same section and is corrected in
             the body under MRB-225. The three-weeks and three-days figures are
             hedged as *"around"* and are conservative against every published
             range, so they are left. The page nowhere claims they are
             measurements.

  * flag 7   **"The brain is about a fiftieth of your body mass and uses roughly
             a fifth of your resting energy."** CHECKED AND LEFT. About 1.4 kg
             of a 70 kg adult is 2%, which is a fiftieth; 20% of resting energy
             expenditure is the standard adult figure. Both are hedged
             (*"about"*, *"roughly"*) and both round in the safe direction.

  * flag 8   **The energy shares are invented illustrative proportions.**
             CHECKED, AND THE LEGAL LINE DOES SAY SO. Verified on the page (line
             303) rather than assumed: *"illustrative proportions chosen to show
             what each cell type is mainly doing, not measured values"*, plus a
             second sentence covering the mitochondria counts. It is carried
             here as `convention_note` — see the note on that field — and it is
             load-bearing, not decoration. Flag 8 offers to replace the
             percentages with ranked words; that remains Mide's to rule on and
             this record does not pre-empt it, since ranked words would still
             need the same order the `pct` values encode.

  * flag 9   **ACTIVE TRANSPORT is used here and is not named in the KS3
             programme of study.** AUTHORED AS DRAWN, AND THE RULING IS
             REPORTED, NOT TAKEN. What was found, since the question turns on
             it: `ks3_data/` contains the phrase exactly **twice**, in
             `b3-07` and `b1-04`, and BOTH are in `ks4_becomes` — the "At GCSE
             this becomes" card. So it has zero uses as taught KS3 vocabulary
             and two as a named GCSE destination, and this page's own
             `ks4_becomes` makes it a third.

             That is a real tension and it is why the call is reported. But the
             osmosis precedent does not transfer, and the difference is not the
             ruling, it is the LOAD:

               · b7-03 used "osmosis" twice, UNGLOSSED, in a Going further
                 aside. Removing the label cost one clause.
               · This page GLOSSES active transport in its own job card
                 (*"Moving a substance from where there is less of it to where
                 there is more — the opposite of diffusion, and impossible
                 without an energy supply"*), which is the correct way to
                 introduce a term, and then builds on it in eight further
                 places: the card title, the root hair cell's spend bar, its
                 mitochondria line, the key fact, the key note, rung 1's correct
                 answer, two of rung 3's five criteria and one of rung 4's.
               · Rung 3 asks the student to NAME it (*"Names active transport as
                 the process that moves substances against the concentration
                 gradient"*). Strip the label and that criterion has nothing
                 left to mark.

             The statutory clause this lesson claims needs an example of a
             chemical process that is NOT movement, and this is the clearest one
             there is. Removing the name would not keep the idea — it would
             replace a handle with a circumlocution the student has to
             re-assemble at nine sites. So it stays, and whether KS3 names it is
             a key-stage ruling exactly as osmosis was, not a b8-02 edit. If
             Mide rules it out, it moves in the nine places listed above and the
             `active transport` vocabulary chip goes with it.

  * flag 10  **Hibernation** (Going further): body temperature to a few degrees
             above ambient, heart rate to a handful of beats a minute, arousal
             taking hours and costing a serious fraction of the reserve.
             CHECKED AND LEFT. All four hold for a small hibernator such as the
             hazel dormouse, and the paragraph's opening arithmetic — a small
             body loses heat quickly relative to its mass — is the surface-area-
             to-volume argument b1-04 already teaches, arriving here as a
             consequence rather than as a new rule.

  * flag 5   **"By some counts a third of the cell's volume is mitochondria"**
             (heart muscle). CHECKED AND LEFT. The figure varies by source and
             species and Design has ALREADY hedged it, in those words, on the
             page. Nothing to soften that she has not softened. Flag 5 is not
             dropped — it is shared with b8-01, which states it too.

  * flag 21  **No figures, and it is measured.** `<img>`, `<figure>` and
             `<picture>` each appear ZERO times on this page — grepped, not
             assumed — and the page leaves no empty frame and no caption with
             nothing under it. §4.10 allows an empty `figures` for a lesson
             carried by its interactives. A mitochondrion is the obvious
             candidate and is not in `docs/ks3/diagram-manifest.md`; nothing is
             declared here, because declaring a slot means writing a caption and
             a caption would pre-empt the ruling flag 21 asks for.

── Keys this pass authors that the ENGINE pass must wire (contract R5) ───

The `cell-demand` renderer belongs to the engine pass. Its read sites are the
payload schema's §3, which was written before dispatch, and every key below
appears in it: `eyebrow`, `heading`, `prompt`, `progress{zero,some}`,
`options_label`, `spend_label`, `mito_label`, `cells[]`, `start`, `run_label`,
`ran_label`, `done_after`. `{n}` and `{total}` in `progress.some` are the cut
count and `len(cells)`.

⚠️ **No runtime state is authored** (payload schema §0 rule 3). NOTES-B8 §2.2
sketches `cut` and `seen`; both are values the runtime owns, and a key with no
read site fails `ks3_key_audit.py`. `start` IS authored, because §3 lists it —
it is Design's `startCell` tweak prop and its default is `muscle`, which is also
`cells[0]`, so a renderer that opens on the first cell reproduces it either way.
"""

# ── the five cells (page lines 321–347, via extract_design_payload.js) ───
#
# Tab order is Design's and is not alphabetical or arbitrary: two animal cells
# whose energy bill reads as obvious effort (a heart contracting, a nerve
# firing), then the plant cell that cannot be read that way at all, then two
# more animal cells that widen "movement" past muscle. The root hair sits third
# because it lands after the student has settled into the obvious reading and
# before the bench has finished — see the docstring.
#
# `pct` values are ILLUSTRATIVE PROPORTIONS and the page's own legal line says
# so; it is carried as `convention_note`. NOTES-B8 flag 8 offers ranked words
# instead and that is Mide's to rule on — the order these encode survives either
# answer.
CELLS = [
    {"id": "muscle", "label": "Muscle cell", "name": "Heart muscle cell",
     "origin": "Animal",
     "job": "Contracts about once a second, every second, for a lifetime, and "
            "never gets a rest day.",
     "spend": [{"name": "Contracting", "pct": 70},
               {"name": "Pumping ions across the membrane", "pct": 20},
               {"name": "Repair and rebuilding", "pct": 10}],
     # ⚑ NOTES-B8 flag 5, and Design has already hedged it herself — "by some
     # counts". Checked and left; shared with b8-01, which states it too.
     "mito": "Enormous numbers — by some counts a third of the cell’s volume. "
             "The hardest-working cell in the body has the most machinery for "
             "the job.",
     "fails": "Contraction stops within seconds. A heart deprived of oxygen "
              "for a few minutes suffers permanent damage, and it is heart "
              "muscle’s inability to be replaced afterwards that makes a heart "
              "attack so serious."},

    {"id": "nerve", "label": "Nerve cell", "name": "Nerve cell",
     "origin": "Animal",
     "job": "Carries signals along a fibre that may be a metre long, hundreds "
            "of times a second.",
     # The 65% row is the quiet half of the lesson: the biggest single energy
     # bill on the bench belongs to a cell that is not moving anything.
     "spend": [{"name": "Pumping ions back across the membrane after each "
                        "signal", "pct": 65},
               {"name": "Making transmitter chemicals", "pct": 20},
               {"name": "Maintenance", "pct": 15}],
     # ⚑ NOTES-B8 flag 7 — a fiftieth of body mass, a fifth of resting energy.
     # Checked against the standard adult figures and left. See the docstring.
     "mito": "Many, and concentrated at the ends where signals are passed on. "
             "The brain is about a fiftieth of your body mass and uses roughly "
             "a fifth of your resting energy.",
     # ⚑ NOTES-B8 flag 6. "Begin to die within about four minutes" is the onset
     # of damage, correctly stated, and it is where the hook's number comes
     # from. Left exactly as drawn; the overstatement flag 6 was reaching for is
     # in the hook reveal and is corrected there. See the docstring.
     "fails": "Fastest failure of any cell here. Brain cells begin to die "
              "within about four minutes, which is where the number at the top "
              "of this page comes from."},

    # ⚖️ THE LOAD-BEARING TAB. The only plant cell of the five, and the only one
    # whose energy bill cannot be read as effort — it makes RESP-03 unarguable
    # and its `fails` line sets up rung 4 and b8-05's `root` case. Not to be
    # smoothed into the shape of the other four, and not the one to cut if a
    # later pass trims the bench. See the docstring and payload schema §3.
    {"id": "root", "label": "Root hair cell", "name": "Root hair cell",
     "origin": "Plant",
     "job": "Absorbs water and mineral ions from the soil, and pulls the "
            "minerals in against the concentration gradient.",
     "spend": [{"name": "Active transport of mineral ions", "pct": 75},
               {"name": "Growth of the hair itself", "pct": 15},
               {"name": "Maintenance", "pct": 10}],
     "mito": "Plenty — more than most plant cells, and the reason is on the "
             "line above. Active transport is expensive and this cell does "
             "almost nothing else.",
     # ⊕ MRB-245's osmosis ruling applied: "by osmosis" → "on its own". Three
     # words, no science lost — the clause already says "which needs no
     # energy", which is the whole of what the label was carrying here. Full
     # working, and the three sites it touches, in the docstring.
     "fails": "Mineral uptake stops immediately, because moving ions from a "
              "low concentration to a high one cannot happen without an energy "
              "supply. Water still moves in on its own, which needs no energy, "
              "so the plant goes short of minerals long before it goes short "
              "of water."},

    {"id": "sperm", "label": "Sperm cell", "name": "Sperm cell",
     "origin": "Animal",
     "job": "Swims, and does nothing else at all. Everything not needed for "
            "the journey has been stripped out.",
     "spend": [{"name": "Beating the tail", "pct": 90},
               {"name": "Everything else", "pct": 10}],
     # ⊕ "You met this cell in b5-02." → the lesson TITLE. A student cannot
     # resolve a slot code (§8.10), and the destination is carried as a real
     # `references` edge. "What could not be lifted" 2.
     "mito": "A tight spiral of them wrapped around the base of the tail — the "
             "engine placed directly next to the propeller. You met this cell "
             "in Gametes and fertilisation.",
     "fails": "It stops swimming and cannot start again. There is no store to "
              "fall back on, which is one reason so few of the hundreds of "
              "millions that set out arrive."},

    {"id": "white", "label": "White blood cell", "name": "White blood cell",
     "origin": "Animal",
     "job": "Crawls out of blood vessels, chases bacteria and engulfs them.",
     "spend": [{"name": "Crawling and engulfing", "pct": 55},
               {"name": "Making antibodies and enzymes", "pct": 30},
               {"name": "Dividing rapidly during an infection", "pct": 15}],
     "mito": "Numerous, and they multiply along with the cell when an "
             "infection begins — a cell that is about to work harder builds "
             "more of the machinery first.",
     "fails": "It stops moving and stops engulfing. Everything on its list — "
              "crawling, swallowing a bacterium, building an antibody molecule "
              "— is work, and work has to be paid for."},
]

# ── the four jobs (page lines 349–354) ──────────────────────────────────
#
# One card per thing the statutory clause's "all the other chemical processes"
# has to be paid for. Dropping any one leaves the clause part-unclaimed while
# the register still reads as covered — and dropping job one would remove the
# only card the student already believes, which is what the panel's display
# statement ("Only one of them is moving.") is counting.
#
# `role` / `term` / `gloss` are Design's `kind` / `name` / `body` unchanged.
# Since MRB-245 widened `_rule_card` all three parts render natively, so unlike
# b7-04 nothing is joined with a middle dot and no string is lost.
#
# ⚑ Job three names ACTIVE TRANSPORT and glosses it in the same card. NOTES-B8
# flag 9 asks whether KS3 should name it at all; authored as drawn and the
# ruling reported, with the full argument and the nine sites it would move in
# the docstring.
JOB_CARDS = [
    {"role": "Job one", "term": "Movement",
     "gloss": "Muscle contraction in animals, but also a white blood cell "
              "crawling and a sperm cell swimming. The only job on this list "
              "that is visible from outside."},
    {"role": "Job two", "term": "Building molecules",
     "gloss": "Joining small molecules into large ones: amino acids into "
              "proteins, glucose into starch or cellulose. Growth and repair "
              "are this job, running for years."},
    {"role": "Job three", "term": "Active transport",
     "gloss": "Moving a substance from where there is less of it to where "
              "there is more — the opposite of diffusion, and impossible "
              "without an energy supply. Root hairs and the gut lining both "
              "live on it."},
    {"role": "Job four", "term": "Keeping warm",
     "gloss": "Mammals and birds hold their body temperature above their "
              "surroundings, and the energy comes from respiration. A reptile "
              "does not pay this bill, and eats far less as a result."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 147 character for character.
    "slug":        "why-every-cell-respires",
    "title":       "Why every cell respires",
    "discipline":  "biology",
    "unit":        "respiration",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.RESP.01` claimed WHOLE, on the commander's dispatch. The bullet has
    # two clauses and this lesson is the second one; `substatements.py` carries
    # no RESP split and `validate()` gates exactly-once ownership, so b8-01 must
    # claim `KS3.B.RESP.02` and not this. Reported, not taken — see the
    # docstring's COORDINATION POINT.
    "covers":      ["KS3.B.RESP.01"],
    # Named and used, owned elsewhere. PHOT.01 is b7-01's reaction, which the
    # first confrontation sets respiration against without restating it.
    # NUT.06 is B7's mineral-and-water-from-the-soil clause, which the root hair
    # cell and rungs 1, 3 and 4 all lean on and none of them re-teaches.
    "touches":     ["KS3.B.PHOT.01", "KS3.B.NUT.06"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "energy", "level": 2},
                    {"id": "structure-function", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's endmatter: "Before this lesson → Aerobic respiration, Specialised
    # cells"; "Connects to → Stomata and gas exchange in plants, Heating and
    # thermal equilibrium".
    "requires":    ["aerobic-respiration", "specialised-cells"],
    "assumes":     [],
    # Design's two, in her document order, then the two destinations added by
    # the code-resolutions in "What could not be lifted" 2 and 3. The dict form
    # is required the moment an edge crosses a unit boundary.
    #
    # `heating-and-thermal-equilibrium` is P1, which is authored and held for
    # MRB-223. It goes in `references` rather than anywhere else precisely
    # because this is the field with the graceful-pending path — `requires`
    # SILENTLY drops a slug it cannot find, so the link Design drew would
    # disappear with no error anywhere. Same resolution b7-04 used for
    # `energy-stores`.
    "references":  [{"unit": "B4",
                     "lesson": "stomata-and-gas-exchange-in-plants"},
                    {"unit": "P1", "lesson": "heating-and-thermal-equilibrium"},
                    {"unit": "B4", "lesson": "alveoli-built-for-exchange"},
                    {"unit": "B5", "lesson": "gametes-and-fertilisation"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Metabolism, ATP, active transport across membranes, and "
                   "calculating metabolic rate from oxygen consumption.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Weeks without food. Days without water. Minutes without "
                    "oxygen. The gap between those three numbers is the whole "
                    "subject of this lesson.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-jobs` is the third: no control of
    # its own, so it mirrors `s-bench` and ticks on the bench's `seen >= 3` —
    # see the docstring, which reverses the unit ruling in
    # ks3_data/b8/__init__.py. `short` and `label` are Design's own
    # `RAIL_SHORT` and `RAIL` strings (page lines 313–319), `JOBS` / "Four
    # jobs" included.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Four minutes",
         "done_when": "committed"},
        # Design's own threshold, kept: `seen >= 3` (page line 403). Three
        # DISTINCT cells cut, not three presses — the cut is per cell and
        # one-way, so a student cannot reach it on the two animal cells nearest
        # their prior belief.
        {"anchor": "s-bench", "short": "CELLS", "label": "Five cells",
         "done_when": "three_cells_cut"},
        {"anchor": "s-jobs", "short": "JOBS", "label": "Four jobs",
         "mirrors": "s-bench", "done_when": "three_cells_cut"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key. B is the true one and
    # the reveal says so at once; the hook is not a trick, it is the claim the
    # rest of the page has to earn.
    #
    # ⊕ THE REVEAL CARRIES THIS LESSON'S ONE SCIENCE CORRECTION. Design's last
    # clause said every cell stops respiring and every process stops, at once.
    # Cells without oxygen respire ANAEROBICALLY — b8-03, in this unit, and half
    # of the statement this lesson claims — and "every process stops at once"
    # contradicts the four-minute figure three sentences above it in the same
    # section. Narrowed to what is true, keeping the simultaneity that is the
    # actual point. Full working in the docstring under MRB-225.
    "phenomenon": {
        "kind": "narrative",
        "title": "Three weeks, three days, four minutes.",
        "prompt": "A person can survive around three weeks without food and "
                  "three days without water. Without oxygen the number "
                  "collapses to about four minutes before permanent damage "
                  "begins. Nothing else the body needs has a deadline anything "
                  "like that short.",
        "commit": "Why is oxygen on such a different timescale?",
        "options": [
            "Because the brain needs oxygen in order to think",
            "Because there is no store of oxygen, and every cell needs it "
            "every second",
            "Because blood is mostly made of oxygen",
            "Because the lungs collapse without air in them",
        ],
        "reveal": "Because there is no store of it and every cell needs it "
                  "every second. Fat is a store of fuel that lasts weeks. "
                  "There is no oxygen tank anywhere in the body — a few "
                  "seconds' worth is dissolved in the blood and that is all. "
                  "Stop the supply and every cell in the body loses its main "
                  "source of energy at once, which is why the deadline is "
                  "minutes rather than weeks.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # `RESP-03` and `RESP-04` are the commander's pre-allocation and are the
    # only two ids this lesson may use. **`RESP-12` is this lesson's named spare
    # and is deliberately left UNUSED** — a permanent gap, like `PLANT-09`..`12`,
    # `DRUG-07` and `REPRO-17`/`20`/`21`/`23`. Do not re-point it.
    #
    # Both `statement`s are Design's own quoted beliefs, lifted byte-identical
    # from `#s-think` (page lines 183 and 187). That is deliberate rather than
    # convenient: `r_confrontation` was ruled in MRB-245 so that an AUTHORED
    # statement wins over the register, after b1-01 shipped a student the
    # register's wording instead of the one Design drew. The `RESP` register
    # rows are the engine pass's to write and these are the strings they take.
    #
    # Both values resolve against the BUILT page (MRB-244/248): `s-think`,
    # `s-bench` and `s-jobs` are all emitted as `id="…"`. Whether `s-jobs` is a
    # rail stop is beside the point here — the gate wants an emitted element,
    # not a completion signal.
    "misconceptions": [
        # Elicited at the bench, by the root hair tab: a plant cell whose energy
        # bill is 75% one process, and whose `fails` line kills it outright when
        # the oxygen goes. That is where a student holding "plants
        # photosynthesise instead of respiring" meets a plant cell that dies of
        # not respiring. `#s-think` is where the belief is named and taken
        # apart.
        {"id": "RESP-03",
         "statement": "Plants photosynthesise, animals respire.",
         "elicited_by": "s-bench",
         "confronted_by": "s-think"},
        # Elicited by the jobs panel: card ONE is Movement, which is the belief
        # in a box, and the student reads it before the three that are not.
        # Design's display statement — "Only one of them is moving." — is the
        # page turning it over, and `#s-think`'s second half is where the
        # "when you exercise" half dies. Same construction as b7-04's PLANT-08
        # on its own `#s-jobs`.
        {"id": "RESP-04",
         "statement": "You respire when you need energy — when you exercise.",
         "elicited_by": "s-jobs",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block on any B8 page, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚑ "active transport" is included and the call is reported — NOTES-B8
    # flag 9. It is the term the statutory clause's "all the OTHER chemical
    # processes" is discharged through, it is glossed in its own job card, and
    # rung 3 asks the student to name it. If Mide rules it out of KS3 this chip
    # goes with it and the term moves in the nine places listed in the
    # docstring. Same handling as b7-04 gave "chemosynthesis".
    "vocabulary": [
        {"term": "respiration",
         "definition": "The reaction every living cell runs continuously to "
                       "release energy from glucose.",
         "note": "Not breathing. Breathing is the muscular job that supplies "
                 "it."},
        {"term": "active transport",
         "definition": "Moving a substance from where there is less of it to "
                       "where there is more, which needs a supply of energy.",
         "note": "The opposite direction to diffusion, which needs none."},
        {"term": "concentration gradient",
         "definition": "The difference between a place where there is more of "
                       "a substance and a place where there is less.",
         "note": "Things drift down one on their own; pushing one up it has to "
                 "be paid for."},
        {"term": "mitochondria",
         "definition": "The parts of a cell where aerobic respiration happens.",
         "note": "A cell with a large energy bill carries more of them."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # ZERO times on this page — grepped, not assumed — and the page leaves no
    # empty frame and no caption with nothing under it. NOTES-B8 flag 21 names a
    # mitochondrion as the obvious candidate and records that it is not in
    # `docs/ks3/diagram-manifest.md`; the flag is not dropped by this, it is
    # Mide's.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b8/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 105), so the segment is MEASURED and not inferred from the
        # kind name.
        #
        # ⚠️ THIS INSTRUMENT IS ON INK. `.ks3-dark p` is (0,1,1) and beats a
        # bare instrument class at (0,1,0). That is the engine pass's problem
        # rather than this module's, and since MRB-245
        # `ks3_parity.check_dark_text_specificity()` fails the build on it — but
        # it is recorded here because this payload is what feeds it.
        #
        # Keys follow docs/ks3/b8-inventory/PAYLOAD-SCHEMA.md §3 exactly. No
        # runtime state is authored (§0 rule 3): `cut` and `seen` belong to the
        # renderer.
        {"type": "cell-demand", "id": "five-cells-one-reaction",
         "anchor": "s-bench", "demand": "compare",
         "eyebrow": "At the bench · five cells, one reaction",
         "heading": "What is the energy actually for?",
         "prompt": "Five very different cells, including one from a plant.",
         # `{n}` is the number of distinct cells cut; `{total}` is len(cells).
         "progress": {"zero": "no cells cut off yet",
                      "some": "{n} of {total} cut off"},

         "options_label": "The cell",
         "spend_label": "Where its energy goes",
         "mito_label": "Mitochondria",
         "cells": CELLS,
         # Design's `startCell` default, which is also cells[0].
         "start": "muscle",

         "run_label": "Cut off the oxygen",
         "ran_label": "Oxygen cut off",
         # Design's own threshold (page line 403), kept. Three DISTINCT cells.
         "done_after": 3},

        # #s-jobs — the band panel, `rule` with a four-card grid. Rail stop 3,
        # mirroring `s-bench`; the anchor also carries hash links and RESP-04's
        # `elicited_by`. One card per thing the statutory clause has to pay
        # for.
        {"type": "rule", "anchor": "s-jobs",
         "eyebrow": "Four things the energy pays for",
         "statement": "Only one of them is moving.",
         "cards": JOB_CARDS,
         # Design NESTS the key fact inside this section (page lines 172–175) on
         # the card ground, with the accent offset shadow. `r_rule` has taken a
         # nested `key_fact` since MRB-245, so unlike b7-04 the box does not
         # have to be lifted to a top-level block: `card`, because the section
         # is already `--ks3-band` and band on band is invisible.
         "key_fact": {"ref": "every-cell-pays-the-bill", "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "RESP-03"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-jobs on the card ground — Design's own arrangement, and
    # measured: `background: var(--ks3-card)`, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`, which is the shipped stylesheet's value, so contract
    # R3's drift question does not arise here. Never amber.
    #
    # This is the sentence the lesson exists to leave behind, and it names all
    # four jobs in the clause's own order.
    "key_facts": [
        {"id": "every-cell-pays-the-bill",
         "text": "Every living cell in every living organism respires "
                 "continuously, because every other chemical process in a cell "
                 "— movement, growth, repair, active transport and keeping "
                 "warm — has to be paid for out of the energy respiration "
                 "releases.",
         # NESTED, inside #s-jobs — there is no `placement` key, because
         # nothing reads one (R5: "it documents intent" is not a read site).
         # Position is decided by the `key_fact` ref on the `rule` block.
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment, on Design's page and
        # here: measured as static markup on all five B8 pages, no options, no
        # reveal, no button, no state. So `confrontation`, not `predict`
        # (contract §2 R1's predict branch wants a commitment then a reveal),
        # and it emits no completion contract — which costs nothing, because
        # Design's RAIL never lists `#s-think` on any B8 page.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "RESP-03",
         "statements": [
             # ⊕ The closing sentence's inline link is stripped and the lesson
             # NAMED instead — `rich()` allows no <a>, and "b4-05's" is a build
             # slot code a student cannot resolve (§8.10). "What could not be
             # lifted" 1. Every science word is unchanged, and the destination
             # is carried as a `references` edge.
             {"quote": "Plants photosynthesise, animals respire.",
              "body": ["A plant is made of living cells, and a living cell "
                       "that does not respire is a dead one. Every root cell, "
                       "every stem cell, every leaf cell respires "
                       "continuously, day and night, using oxygen and "
                       "producing carbon dioxide exactly as yours do. "
                       "Photosynthesis is not an alternative to respiration; "
                       "it is an extra process that a plant can also do, in "
                       "the cells that have chloroplasts, when there is light. "
                       "Put the two together and the arithmetic works out like "
                       "this: in bright light a leaf photosynthesises faster "
                       "than it respires, so the net movement of gases looks "
                       "like the opposite of an animal's, which is where the "
                       "wrong idea comes from. Look at a root instead — "
                       "buried, dark, no chloroplasts, and entirely dependent "
                       "on sugar sent down from the leaves — and the plant "
                       "looks exactly like you. The day-and-night version of "
                       "this is the subject of Stomata and gas exchange in "
                       "plants."]},
             # ⚑ NOTES-B8 flag 6's second site. "The clearest evidence is the
             # four-minute figure at the top of this page" is an ARGUMENT from
             # the number, not a restatement of it, and it makes no claim about
             # death. Checked and left exactly as drawn.
             {"quote": "You respire when you need energy — when you exercise.",
              "body": ["You respire fastest when you exercise. You respire all "
                       "the time, and most of what you use in a day is spent "
                       "while you are doing nothing you would describe as "
                       "activity. Sitting still, your heart is contracting, "
                       "your kidneys are filtering, your gut is transporting, "
                       "your liver is running thousands of reactions, your "
                       "brain is signalling, and every cell you own is pumping "
                       "ions across its membrane to stay alive. That last one "
                       "alone is a large and permanent bill. The clearest "
                       "evidence is the four-minute figure at the top of this "
                       "page: if respiration only mattered during effort, "
                       "someone sitting quietly could hold their breath for an "
                       "hour, and they cannot. Rest is not the state of not "
                       "respiring — it is the state of respiring at your "
                       "lowest rate, and that rate is still enough to keep you "
                       "at 37 °C in a cold room."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 MEASURED AND CLEAN. Rung 1's correct option is 9 words against
    # 8 / 8 / 5 and rung 2's is 11 against 10 / 14 / 9 — the gate wants the
    # correct answer to be strictly the longest AND ahead by ≥4 words or ≥1.4×,
    # and neither is. **No distractor was rewritten for length.** Rung 1's
    # construct is a list of processes rather than a rule-stating rung, so the
    # shape MRB-177 repairs does not arise on it. Full working in the docstring.
    #
    # The two distractor-side edits below are for RULED reasons, not parity:
    # the osmosis label (MRB-245) and a build slot code in student prose
    # (§8.10). Correct options, `answer` indices, option order and every other
    # word of Design's six corrections are byte-identical.
    "ladder": {
        "recall": {
            "title": "Rung 1 · What needs energy",
            "q": "Which of these processes could not happen at all without "
                 "respiration?",
            "options": [
                # 9w — Design's, unchanged. The only one of the four that has to
                # be paid for; the other three are all diffusion wearing
                # different clothes, which is the rung's whole construct.
                "Active transport of minerals into a root hair cell",
                # 8w — was "Water moving into a root by osmosis" (7w). The
                # LABEL goes under MRB-245's ruling; the belief the distractor
                # carries (water uptake must cost energy too) is untouched, and
                # the count moves away from the correct answer, not toward it.
                "Water moving into a root from the soil",
                "Oxygen diffusing from the alveoli into the blood",
                "Carbon dioxide leaving a cell",
            ],
            "answer": 0,
            "feedback": {
                # First sentence loses the label only — "Osmosis is diffusion of
                # water down its own gradient" → "Water moves into a root by
                # diffusion, down its own gradient". The second sentence, which
                # carries the teaching point, is byte-identical.
                1: "Water moves into a root by diffusion, down its own "
                   "gradient, and needs no energy supply. That is exactly why "
                   "a plant short of energy goes short of minerals before it "
                   "goes short of water.",
                # ⊕ "as you established in b4-03" → the lesson TITLE, with the
                # matching `references` edge. "What could not be lifted" 3.
                2: "Diffusion is passive — particles move down a gradient "
                   "without anything pushing them, as you established in "
                   "Alveoli: built for exchange.",
                3: "Also diffusion. There is more carbon dioxide inside the "
                   "cell than outside it, so it leaves without being pushed.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A potted plant is left in a completely dark cupboard. What "
                 "is happening in its cells?",
            # All four are Design's, unchanged, and all four state a rule about
            # what a plant's cells do in the dark — the construct MRB-177 wants,
            # already present. Option C is `RESP-03` in its most persuasive
            # form and is the longest option on the rung.
            "options": [
                "Nothing — without light a plant shuts down until morning",
                "Respiration continues in every cell, using oxygen and "
                "releasing carbon dioxide",
                "The plant respires instead of photosynthesising, which is the "
                "swap plants make at night",
                "Only the root cells respire, because the leaves "
                "photosynthesise",
            ],
            "answer": 1,
            "feedback": {
                0: "A cell that shuts down is dead. Photosynthesis stops in "
                   "the dark; respiration does not, and cannot.",
                2: "Close, and the word instead is the problem. Respiration "
                   "never stopped — it was running all day too, underneath the "
                   "photosynthesis.",
                3: "Every living cell respires, leaves included. A leaf cell "
                   "does both when there is light and just the one when there "
                   "is not.",
            }},
        # ⚑ Criteria 3 and 4 name ACTIVE TRANSPORT and are two of the nine sites
        # NOTES-B8 flag 9 would move. Criterion 3 asks the student to produce
        # the term itself, which is why removing the label would not "keep the
        # idea" here — it would leave the criterion with nothing to mark.
        "explain": {
            "title": "Rung 3 · Explain the root hair",
            "q": "A root hair cell absorbs mineral ions from soil where those "
                 "minerals are far more dilute than they are inside the cell. "
                 "Explain why this needs respiration, and why a root hair cell "
                 "is packed with mitochondria.",
            "field_label": "Your explanation",
            "placeholder": "The minerals are more concentrated inside the cell "
                           "than outside, so…",
            "success": [
                "Says the mineral ions are more concentrated inside the cell "
                "than in the soil water.",
                "Says diffusion moves substances the other way, from high to "
                "low, so it cannot do this job.",
                "Names active transport as the process that moves substances "
                "against the concentration gradient.",
                "Says active transport requires energy, and that the energy "
                "comes from respiration.",
                "Concludes that the cell holds many mitochondria because "
                "active transport is its main and continuous activity.",
            ]},
        # The rung the root hair tab exists to make reachable. Criterion 3 is
        # also the one place in the lesson that a student has to hold "no
        # oxygen" and "aerobically" together, which is the handover to b8-03.
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A houseplant that is watered too often dies, and the leaves "
                 "go yellow and droop as if it were short of water. Gardeners "
                 "say the roots have \"drowned\". Explain what has actually "
                 "happened, using respiration.",
            "field_label": "Your answer",
            "placeholder": "Waterlogged soil has no…",
            "success": [
                "Says soil normally contains air spaces, and that waterlogging "
                "fills them with water.",
                "Says root cells need oxygen because they respire, just as "
                "animal cells do.",
                "Says without oxygen the root cells cannot respire "
                "aerobically, so they have little or no energy available.",
                "Says active transport of minerals stops, and the root cells "
                "begin to die.",
                "Explains the apparent contradiction: dead or dying roots "
                "cannot take up water, so a plant standing in water shows "
                "exactly the symptoms of a plant with none.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # Lifted whole. Its last sentence is the corrected hook reveal's destination
    # and the two now agree: no store, so the supply cannot be interrupted for
    # more than a few minutes. Nothing here is retracted by b8-03 — the
    # anaerobic reserve is what makes it minutes rather than seconds.
    "key_note": "Respiration happens in every living cell of every living "
                "organism, plants included, continuously. The energy it "
                "releases pays for movement, for building large molecules from "
                "small ones during growth and repair, for active transport, "
                "and in mammals and birds for keeping the body warm. There is "
                "no store of oxygen, which is why the supply cannot be "
                "interrupted for more than a few minutes.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B8 flag 10: body temperature to a few degrees above ambient, a
    # handful of heartbeats a minute, arousal costing a serious fraction of the
    # reserve. Checked and left — all four hold for a small hibernator, and the
    # opening arithmetic is b1-04's surface-area-to-volume argument arriving as
    # a consequence rather than as a new rule.
    #
    # ⚖️ MRB-225 holds: the layer adds a case at the far end of the lesson's own
    # scale — respiration turned down almost to nothing, deliberately — and
    # retracts nothing above it. The body says respiration is continuous and
    # cannot stop; this says how far down it can be turned without stopping,
    # which is the same claim under load.
    "stretch": [
        {"type": "explainer", "id": "the-animal-that-turns-it-down",
         "text": "A dormouse in October has a problem an arithmetic teacher "
                 "would recognise. Keeping a small warm body at 37 °C through "
                 "a British winter costs more energy than a winter's food "
                 "supply can provide, because a small animal loses heat "
                 "quickly relative to its mass. Hibernation is the accounting "
                 "solution: it abandons the temperature. Body temperature "
                 "falls to a few degrees above the surroundings, the heart "
                 "slows to a handful of beats a minute, and respiration drops "
                 "to a tiny fraction of its normal rate — slow enough that a "
                 "store of fat laid down in autumn can last until spring. The "
                 "animal is not asleep in any ordinary sense and cannot simply "
                 "wake up; getting back to operating temperature takes hours "
                 "and costs a serious fraction of the reserve, which is why a "
                 "hibernating animal disturbed too often in winter can starve "
                 "before spring."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own flagship, which is a real destination
    # on the page it is printed on (§4.8.1 C) — Design's `href="#s-bench"`.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to work out what a cell spends its energy on?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 303) and nothing in it is a safety
    # instruction — it is a note about how far the bench's numbers can be
    # trusted. Routing it through `safety_note` would print it in the treatment
    # reserved for "never light a candle without an adult", which devalues the
    # safety line. b3-05, b3-07, b4-01, b5-06 and b7-04 resolve the identical
    # foot line the identical way.
    #
    # ⚑ THIS LINE IS LOAD-BEARING, and it is the whole of NOTES-B8 flag 8's
    # answer: it is the page telling the student, in its own words, that the
    # energy shares are illustrative and not measured. It was verified on the
    # page rather than assumed. If the percentages ever become ranked words this
    # sentence changes with them; it may not simply be dropped.
    "convention_note": "The energy shares on the bench are illustrative "
                       "proportions chosen to show what each cell type is "
                       "mainly doing, not measured values — real figures vary "
                       "with the organism, its age and what it is doing at the "
                       "time. Mitochondria counts are given as broad "
                       "comparisons rather than exact numbers.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is five cases compared on three fixed dimensions, and rung 4
    # asks the student to resolve an apparent contradiction — symptoms of
    # drought in a plant standing in water — by reasoning from a mechanism
    # rather than from the appearance. Both are analysis and evaluation.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
