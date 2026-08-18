"""B5 L4 — Gestation, the placenta and birth (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b5/b5-04-gestation-placenta-and-birth.dc.html` (579 lines), its
author's notes `docs/ks3/design-reference/b5/NOTES-B5.md` (§2.2, §3 flags 20–25, §4 read
whole rather than by flag), and the MRB-220 build contract
(`docs/ks3/mrb-220-build-contract.md`).

⊕ **This is the record MRB-244 records as never written.** The other seven B5
lessons survived the 16 Aug session limit; this one did not exist, which is why
`ks3_data/_parked_biology_b5_reproduction.py` names it first in its list of what
is missing. It is written last and against the same page the other seven were
written against, so it is authored to match them rather than to improve on them.

Every student-facing string is lifted byte-identical from the approved page.
The six substances, the five stages, both marked rungs and both self-marked
rungs came out of `node tools/extract_design_payload.js`; the static prose came
out of the page's own markup. Nothing on this page was retyped. The exceptions
are listed under "What could not be lifted", and none of them is a word of copy.

⚠️ Design's static markup uses STRAIGHT apostrophes (`the mother's blood`) and
her script constants use CURLY ones (`the mother’s blood`). Both are reproduced
exactly as delivered rather than normalised — the same deliberate split
`lesson_03` and `lesson_05` carry, and for the same reason: normalising either
half would break byte-identity against the half it changed.

── ⚠️ TONE IS A GATE ON THIS UNIT, AND THIS IS THE BIRTH LESSON ──────────

Read `ks3_data/b5/__init__.py` first; its tone section binds here. What it means
on THIS page:

- **Third person, function-first, clinical.** "The foetus", "the mother's
  blood", "a mother and her baby". Nothing addresses the reader as pregnant, as
  a future parent, or as anybody's child. Nothing here adds a second person.
- **Birth is ONE card, and it is anatomy.** Stage 05 says the uterus wall
  contracts, the cervix opens, the baby is delivered through the vagina, the
  cord is cut and the placenta follows. No pain, no choice, no intervention, no
  caesarean, and nothing about what can go wrong. That is Design's deliberate
  scope decision (NOTES flag 25, and she flags it herself as reviewable because
  *"a Year 8 class will ask"*). It is carried exactly as delivered — an
  authoring pass neither widens it nor hedges it.
- **No normative language about family structure anywhere**, and none is added.
- **The legal line is carried whole**, small, at the bottom edge, never a
  callout (§8.10). See `convention_note` at the foot of this record.

── ⚖️ THE INSTRUMENT IS THE LESSON, AND IT IS b5-05's SHAPE FIRST ────────

`#s-cross` is `crossing-bench`, on `ks3-block ks3-dark ks3-practical` (page
line 104), so `practical` is MEASURED from Design's own markup and not
inherited. Six substances, a two-way direction commit, then a verdict, the
direction in a sentence, and a *why* that always names the concentration
difference.

NOTES §1 and §6 both say b5-05's `crosses-panel` deliberately repeats THIS
instrument's shape, *"because the lesson's whole argument is that the crossing
rule from the previous lesson does not change when the substance is a harmful
one"*, and asks that the two not be refactored apart. So this record is
authored with `lesson_05`'s key set wherever the two instruments do the same
job — `eyebrow`, `heading`, `head_counter`, `prompt`, `subs`, `choices`,
`commit_label`, `check_label`, `hint`, `verdict` — and differs only where
Design's pages differ: this one commits to a DIRECTION rather than to yes/no,
and carries no week bar. The repetition is the argument.

⚠️ **`dir` is an INDEX INTO `choices`, and 0 is `into the foetus`.** Design's
`SUBS[].dir` is a bare integer matched against the index of the pressed
direction button (`pick === sub.dir`, page line 515), where `dirOptions` is
`[IN, OUT]`. NOTES §2.2 declares the field as `dir`, so it is authored as `dir`
and `choices` is authored in Design's order so the index still means what she
made it mean. Four of the six are `0`; carbon dioxide and urea are `1`.

⚠️ **The two direction labels are Design's `IN` and `OUT` CONSTANTS** (page
lines 323–324), not markup, and they are the only place the two directions are
written in words. They are authored as `choices[].label` because a renderer
hard-coding them would be a renderer holding science copy. NOTES §2.2's payload
line does not list them; the page does. Reported.

── FOUR rail stops — Design's fourth restored (MRB-249) ──────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that the rail
lost a stop, "the defect five units have now found". Design draws FOUR stops,
and `#s-stages` ticks on `Object.keys(s.opened).length >= 6` (page line 412) —
the BENCH's predicate, verbatim, one section to the left — and because
`#s-stages` is an eyebrow, a display statement, five static stage cards and a
key fact with no control, no commitment and no field, the reading was that
`ks3_parity.check_rail_reachable` would fail a stop carrying none of the
signals `doneByDom()` reads, and that inventing a demand Design did not draw is
closed to this build. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 was cited for one half of itself. Design draws, we render: it forbids
inventing a control, and just as plainly forbids dropping a stop Design drew.
Page wins over engine.

And Design's `isDone()` states the tick condition. It is a rail-level function
and returns the identical expression for `#s-cross` and then for `#s-stages`.
The forty weeks are the payoff of the six crossings the student just settled;
the section carries no control because the bench already took the commitment.
That is a MIRROR, resolved at rail level in `wireRail`'s `paint()`.

So the fourth stop is declared: anchor `s-stages`, `mirrors: "s-cross"`,
`done_when: "all_six_checked"` — the bench's own predicate, named as borrowed,
and gated by `check_rail_matches_design` against `docs/ks3/rail-manifest.md`.
b5-03's `#s-events`, b5-05's `#s-windows`, b4-01's `#s-parts`, b3-06's
`#s-three`, c1-02's `#s-matrix` and c1-05's `#s-scale` are restored the same
way. **The section keeps its `#s-stages` anchor**, as it always did.

The stop is Design's `{id: 's-stages', label: 'Forty weeks'}`, short `STAGES` —
her label, now carried rather than merely recorded.

── Misconceptions: this lesson owns REPRO-07 and REPRO-08 ───────────────

⚠️ IDs are PRE-ALLOCATED by the commander (MRB-244) and are not re-derived
here. NOTES-B5 §5 pins one of the two by name: *"The baby's blood mixes with
the mother's blood in the placenta"* → **`REPRO-08`**, owned by this lesson. The
remaining allocated id, `REPRO-07`, therefore belongs to the page's second
belief.

    REPRO-08  "The baby's blood mixes with the mother's blood in the placenta."
    REPRO-07  "The baby breathes and eats inside the uterus."

⚑ **They are listed in PAGE ORDER, not in id order**, which is the one place
this record reads differently from its siblings. Design draws the mixing belief
first and the breathing/eating belief second, behind the amber divider; NOTES §5
fixes the mixing belief to the higher of the two numbers. Both cannot be
satisfied at once, and page order is the one a reader can check against the
page. Reported so it is not read as a slip.

⚑ **NO THIRD BELIEF IS MINTED, and the spare range `REPRO-17+` is untouched.**
Two candidates were considered and both are declined:

  1. *"The placenta chooses what the foetus needs and sends it"* — rung 1
     distractor C. It is close to `REPRO-09` (*"The placenta filters out
     anything harmful"*), which **b5-05 already owns**, and it is answered only
     in a rung correction which partly CONCEDES it (*"The placenta does
     actively carry a few things, such as antibodies"*). b5-03's runner-up
     precedent declines exactly this shape. **CITED, not re-declared:** the
     `drugs` substance in the bench says *"The placenta is not a filter and has
     no way of telling a useful small molecule from a harmful one"*, which is
     `REPRO-09` in Design's own words — and its last sentence hands the belief
     forward on purpose (*"What follows from that is the whole of the next
     lesson"*). This page sets the belief up; b5-05 takes it apart. A
     `misconceptions` row here would claim the confrontation.
  2. *The umbilical cord carries the mother's blood into the baby* — rung 2's
     whole question. It is not a distinct belief: it is `REPRO-08` applied to
     the cord, and the confrontation paragraph closes on it in as many words
     (*"The cord is not a pipe carrying the mother's blood"*). It is what gives
     `REPRO-08` a second, marked confrontation on this page.

`elicited_by` is honest per entry and both point at the HOOK, because the hook's
four options are the two beliefs written out: option A is the mixing belief and
option D is the breathing belief, and the student commits to one before anything
is explained. `r_hook` emits `data-activity="hook"`, so both values resolve on
the built page.

── What could not be lifted, and why ────────────────────────────────────

1. **TWO inline `<a>`s in the hook's reveal.** Design links *alveoli* to
   `b4-03` and *small intestine* to `b3-07` inside the reveal sentence.
   `rich()` (build_ks3.py:247) allows `<em>` and `<strong>` and nothing else, by
   an explicit ruling — *"a third needs a ruling rather than a regex"*. So both
   anchors are dropped and **both link texts stay in the sentence unchanged**:
   *"the same process you met in the alveoli and the small intestine"*. Not one
   word is lost. Neither DESTINATION is lost either — Design draws both in her
   own "Connects to" card and they are in `references[]` already, so the edges
   survive without needing b5-05's rescue manoeuvre.

2. **The stages' NUMBER CHIPS.** Design draws `#s-stages` as an `<ol>` of five
   cards, each with a `01`–`05` chip. `r_rule` emits a `<ul>` of term/gloss
   cards and has no slot for a numeral. Document order is preserved, so the five
   stages still read in order; the chips are DROPPED rather than smuggled into
   the card text. Identical finding to b5-03 and b4-01, and the fix — if the
   chips are to win — is an `index` flag on `rule`, not a new block type.

3. **⚑ The PROMOTION of stage 02 is dropped, and it is a real loss.** Design
   paints *The exchange surface is built* on `--ks3-inset` with a 3px border and
   an accent number chip while the other four are `--ks3-card` at 2px (page
   lines 521–524), and NOTES §1 names that promotion as the shape of the lesson:
   *"five stages of the pregnancy with `the exchange surface is built` promoted
   rather than birth, because the supply line is what everything else depends
   on."* `r_rule`'s cards carry no emphasis flag and inventing one is an engine
   change this pass does not make (build contract §0). Every word of the card
   survives; only its weight is lost. **Reported, not worked around.** Design's
   own display statement directly above the cards says the same thing in prose —
   *"Building the supply line comes first. Everything else depends on it."* — so
   the argument still reaches the student, just not in the type. b5-03 and b5-05
   meet this identically; it is one flag on `rule`, once.

4. **The `when` line is FOLDED into the card term, not dropped.** Design sets it
   in mono accent type on the same baseline as the stage's name (`Implantation`
   / `About five days after fertilisation`). All five are different strings and
   every one is science — *"Weeks 3–8 · the embryo"* is the claim `b5-05`'s
   whole timing table rests on — so they are joined to the name with " · ",
   which is b5-03's and b4-01's precedent and Design's own separator elsewhere
   on this page. Both strings survive byte-identical.

5. **The key fact leaves Design's band panel.** She nests it inside `#s-stages`;
   `r_rule` has no nested key-fact slot (only `r_comparison` does), so it renders
   as its own top-level block directly under the panel, on the band ground every
   other top-level key fact in the key stage takes. The words and the order are
   unchanged. Note that Design draws it on `--ks3-card` with the accent offset
   shadow INSIDE a band section; rendered top-level on band it takes the shipped
   `.ks3-keyfact` treatment, which is the same identity (band ground, 2px ink
   outline, hard accent shadow, mono label, display statement) at MRB-208's
   ruled numbers rather than hers. That is R3, and R3 says the stylesheet wins.

6. **Design draws TWO endmatter link cards; the engine emits one.** Her "Next in
   this unit" (`lifestyle-and-the-developing-foetus`) and "Connects to"
   (`gametes-and-fertilisation`, `alveoli-built-for-exchange`,
   `absorption-and-the-small-intestine`) are one card in `r_endmatter`, headed by
   `connects_heading`. All four links live in it, the forward one first, under
   "Connects to" — b5-03, b5-05, b4-01 and b3-01 resolve the identical layout
   identically. The heading "Next in this unit" is what is given up; no link is.

   `requires` stays EMPTY for the same reason: Design draws no "Before this
   lesson" card, and a `requires` edge would render one she did not draw.

7. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

8. **The mono `<span>` around the figure id in the legal line.** A foot line is
   escaped, so `b5-placenta-exchange` renders in body copy rather than in mono.
   The words are unchanged. b5-03, b5-05 and b4-01 resolved this the same way.

9. **`phenomenon.kind` is NOT authored.** build_ks3.py:539 records it as read by
   nothing and dispatching on which key is present instead, and R5 says a key
   with no read site is not authored. b5-03 authors it; b5-05 does not. The
   omission follows b5-05 and R5, and the divergence between the two siblings is
   reported rather than propagated.

10. **`key_facts[].placement` is NOT authored.** `r_key_fact` reads `ref`,
    `ground`, `eyebrow` and `text`, and positions the box by document order —
    its own docstring says so in as many words. b5-03 authors
    `placement: "top-level"`; nothing reads it. Same call as 9.

11. **`vocabulary` definitions are AUTHORED, not lifted.** Design draws no
    keyword block anywhere in B5, so these never reach the lesson body: the
    TERMS become the unit page's chips and the reading-age gate's exclusion
    list, which matters here because "placenta", "gestation", "umbilical",
    "embryo" and "foetus" would otherwise count against the page.
    `verify_ks3.py` requires the list to be non-empty. Every definition is
    assembled from the page's OWN sentences and adds no claim the page does not
    make. "uterus" and "cervix" are deliberately absent: `b5-01` owns both, and
    a term defined twice in one unit is a term that can drift.

── ⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026, BOTH RUNGS REPAIRED ─────

The unit-wide pattern this section used to report has been ruled on as a
pattern. Mide's ruling: on a recall or apply rung the correct answer states a
RULE — subject, condition, consequence — while the distractors stated one-clause
wrong REASONS, so the correct answer was longer BY CONSTRUCTION and a student
could score the rung without reading it. A distractor must state a WRONG RULE
instead: the same shape as the correct answer, with the misconception as the
consequence. Length parity then follows from the construct; nothing was trimmed.

Six distractors across the two marked rungs are Mide's own replacement copy,
applied verbatim. **Neither correct option was touched, neither `answer` index
moved, and `verify_ks3.py`'s threshold is unchanged.** Measured after:

    ladder recall (rung 1): correct 16w against 14 / 14 / 16 — no longer
                            STRICTLY the longest
    ladder apply  (rung 2): correct 13w against 16 / 14 / 13 — no longer the
                            longest option at all

All six corrections in `feedback` already answered the new wording and are
byte-identical.

⛔ SUPERSEDED, KEPT AS HISTORY. This section used to record rung 1 at 15w
against 9w and rung 2 at 12w against 8w, and closed: *"Both are Design's option
sets exactly as drawn. **Nothing here is rewritten.** Rewriting a distractor
changes what a marked question measures, which is Mide's gate and not an
authoring pass's."* It was his gate. The two `gestation-placenta-and-birth`
entries in `KNOWN_TELLS` are now stale; the commander deletes them, and
`verify_ks3.py` remains the engine pass's file under build contract §0 and is
not touched here.

⚠️ One typographic note, reported rather than corrected. Mide's replacement
copy uses STRAIGHT apostrophes ("the mother's blood", "the baby's lungs") while
this rung's surviving strings use Design's CURLY ones ("the foetus’s own
blood"), so one option set now carries both forms. His instruction was to apply
the copy exactly as given and not to adjust it, so it is applied exactly. It is
a one-character fix in either direction whenever he rules which convention this
rung takes.

── Figures are declared and NOT drawn (§4.10) ───────────────────────────

Design's legal line names ONE slot on this page, `b5-placenta-exchange`, and no
artwork exists for it. It is declared at `status: "needed"` so the manifest
counts it as a sourcing task rather than losing it. Nothing is invented to fill
it, and no `figure` block is added to `core` — Design draws no figure slot, and
one here would be a component nobody drew. NOTES-B5 flag 13 asks Mide to confirm
what he wants illustrated across the unit, and the human slots specifically,
before anything is commissioned; the caption below is a proposal, not a
commission.

⚑ For Mide's science gate — NOTES-B5 flags landing on THIS lesson:
  * flag 20 — **antibodies actively carried across, using energy**, in contrast
    with everything else on the list. In `anti`'s `kind`, `answer` and `why`,
    and again in rung 1's correction C. Confirm the depth.
  * flag 21 — *"Foetal haemoglobin also holds oxygen more tightly than the adult
    kind, which keeps the difference up."* One sentence, in `o2`'s `why`.
    Design's own note: it is really GCSE material, and it is what keeps the
    gradient up on a page about gradients.
  * flag 22 — **urea leaves via the placenta although the foetus does make urine
    into the amniotic fluid.** Both stated, in `urea`'s `why`. Confirm the
    simplification.
  * flag 23 — *"Pregnancy is dated in weeks from the first day of the last
    period rather than from fertilisation, so the familiar forty weeks is about
    two weeks longer than the time the foetus has existed."* In the legal line,
    and it is the kind of detail that confuses if half-stated.
  * flag 24 — **the Going further ends on an open research question** (immune
    tolerance of the foetus). Confirm you are happy to end a lesson unresolved.
  * flag 25 — **birth is one card**: contractions, cervix opening, delivery,
    cord cut, placenta delivered. No pain, no intervention, no caesarean,
    nothing about what can go wrong. Design's deliberate scope decision, and she
    marks it reviewable herself. Carried as delivered.
  * flag 7, carried from b5-02 and load-bearing here — **implantation at about
    five days**, which is stage 01 and the point `gestation` is defined from.
  * flag 13 — `b5-placenta-exchange` is named in the legal line and is in no
    manifest. Declared here at `needed`.

⚑ Two page-internal notes, both reported rather than silently ruled (MRB-205):
  1. **`#s-stages` and `#s-cross` share a completion predicate**, verbatim. See
     the rail section above: since MRB-249 that is read as Design declaring a
     MIRROR, so both stops ship and `#s-stages` names `#s-cross` as the section
     it borrows from.
  2. **The stage windows overlap, and it is not an error.** Stage 02 is
     *Weeks 1–12* and stage 03 is *Weeks 3–8*, which sit inside each other on
     purpose: the placenta is still growing while the organs are being laid
     down. Noted only because the numbers are read side by side and a reviewer
     will check them against stage 04's *Weeks 9–40*.
"""

# ── the six substances (page lines 326–351, via extract_design_payload.js) ─
#
# ⚠️ Order is Design's and is load-bearing: the two things the foetus needs come
# first, the two wastes next so that the direction reverses while the rule does
# not, antibodies fifth as the single crossing that is NOT diffusion, and the
# drugs row last because its closing sentence hands the whole idea forward to
# b5-05 (*"What follows from that is the whole of the next lesson."*).
#
# ⚠️ `dir` is an INDEX INTO `choices`: 0 is "Mother’s blood → foetus" and 1 is
# "Foetus → mother’s blood". Design matches it against the pressed button's
# index (`pick === sub.dir`). Four are 0; carbon dioxide and urea are 1.
#
# ⚠️ Curly apostrophes throughout — these are script constants, and the page
# body's straight ones are elsewhere in this file. Both are as delivered.
SUBS = [
    {"id": "o2",
     "label": "Oxygen",
     "name": "Oxygen",
     "kind": "Small molecule · diffusion",
     "dir": 0,
     "context": "The foetus respires like any other organism and cannot use "
                "its own lungs — they are full of fluid.",
     "answer": "Into the foetus, from the mother’s blood.",
     # ⚑ NOTES flag 21 lives in the last sentence: foetal haemoglobin holding
     # oxygen more tightly than the adult kind. Lifted whole.
     "why": "The mother’s blood arrives at the placenta freshly oxygenated "
            "from her lungs; the foetal blood arrives having just delivered "
            "its oxygen to foetal tissue. More on one side, less on the other, "
            "so oxygen diffuses across. Foetal haemoglobin also holds oxygen "
            "more tightly than the adult kind, which keeps the difference up."},

    {"id": "glucose",
     "label": "Glucose",
     "name": "Glucose",
     "kind": "Small molecule · carried across",
     "dir": 0,
     "context": "The foetus needs glucose for respiration and raw material for "
                "building, and does not eat.",
     "answer": "Into the foetus, from the mother’s blood.",
     "why": "This is the far end of the mother’s digestion: her small "
            "intestine absorbed the glucose hours earlier and her blood is "
            "carrying it. The placenta moves it across into foetal blood, "
            "where the concentration is lower because the foetus is "
            "continually using it up."},

    {"id": "co2",
     "label": "Carbon dioxide",
     "name": "Carbon dioxide",
     "kind": "Small molecule · diffusion",
     "dir": 1,
     "context": "Respiration in the foetus produces it continuously, and the "
                "foetus cannot breathe it out.",
     "answer": "Out to the mother’s blood — and she breathes it out.",
     "why": "Carbon dioxide builds up in foetal blood, so there is more of it "
            "there than in the mother’s blood arriving at the placenta. It "
            "diffuses across the other way and leaves her body at her alveoli. "
            "Two organisms, one set of lungs."},

    {"id": "urea",
     "label": "Urea",
     "name": "Urea",
     "kind": "Waste · diffusion",
     "dir": 1,
     "context": "Breaking down surplus amino acids produces urea, which is "
                "toxic if it accumulates.",
     "answer": "Out to the mother’s blood — and her kidneys remove it.",
     # ⚑ NOTES flag 22: the foetus DOES make urine into the amniotic fluid, and
     # the urea still leaves across the placenta. Both stated, in Design's
     # order, and the simplification is hers.
     "why": "The foetus has kidneys, and they do make urine, which passes into "
            "the amniotic fluid. But the urea itself has to leave the system "
            "altogether, and the only route out is across the placenta into "
            "the mother’s blood. Her kidneys are doing the work for both."},

    {"id": "anti",
     "label": "Antibodies",
     "name": "Antibodies",
     # ⚑ NOTES flag 20. The ONLY row on the list that is not diffusion, and the
     # `kind` line says so before the student commits. That contrast is the
     # reason the row is in the set.
     "kind": "Large protein · actively carried",
     "dir": 0,
     "context": "A newborn’s immune system has never met anything, and takes "
                "months to become useful.",
     "answer": "Into the foetus — but not by diffusion.",
     "why": "Antibodies are large proteins, far too big to slip across an "
            "exchange surface built for small molecules. The placenta carries "
            "them across deliberately, using energy, and stocks the foetus "
            "with a copy of the mother’s immunity that lasts for the first few "
            "months of life. It is the one crossing on this list that the "
            "placenta chooses to make."},

    {"id": "drugs",
     "label": "Nicotine and alcohol",
     "name": "Nicotine, alcohol and many drugs",
     "kind": "Small molecules · diffusion",
     "dir": 0,
     "context": "These are small molecules dissolved in the blood, exactly "
                "like oxygen and glucose.",
     "answer": "Into the foetus — for the same reason oxygen crosses.",
     # ⚑ THE HAND-OFF ROW. "The placenta is not a filter and has no way of
     # telling a useful small molecule from a harmful one" is REPRO-09 in
     # Design's own words — and REPRO-09 belongs to b5-05, which confronts it.
     # This page SETS IT UP and says so in the last sentence. Cited in the
     # docstring, deliberately not declared in `misconceptions`.
     #
     # ⚠️ TONE. The row names two substances and passes no judgement on anyone
     # who uses them: the whole sentence is about what a molecule's size lets
     # it do. That neutrality is what makes b5-05's anti-blame paragraph
     # answerable, and it is not to be sharpened here.
     "why": "The placenta is not a filter and has no way of telling a useful "
            "small molecule from a harmful one. Anything small enough and "
            "dissolved in the mother’s blood crosses down its concentration "
            "difference, and within minutes the foetus has it too. What "
            "follows from that is the whole of the next lesson."},
]


# ── the five stages (page lines 353–364, via extract_design_payload.js) ───
#
# `when` is joined to `name` with " · " — see "What could not be lifted" 4. The
# `what` prose is untouched, and the `01`–`05` chips and the promotion of stage
# 02 are lost with `r_rule`'s card shape — see 2 and 3.
#
# ⚠️ Stage 05 is BIRTH and it is one card. Anatomy only, by Design's ruling
# (NOTES flag 25). It is not expanded, not softened and not annotated.
STAGES = [
    ("Implantation", "About five days after fertilisation",
     "The ball of cells embeds in the thickened lining of the uterus. Part of "
     "it will become the embryo; another part immediately begins building the "
     "structure that will supply it."),

    # ⚑ THE PROMOTED CARD on Design's page, and the promotion is what `r_rule`
    # cannot carry. The words are all here; only the weight is lost.
    ("The exchange surface is built", "Weeks 1–12",
     "The placenta grows into the uterus wall, folding into thousands of "
     "finger-like projections until its surface area is enormous, and the "
     "umbilical cord connects it to the embryo. Two circulations are brought "
     "within a fraction of a millimetre of each other. Nothing that follows is "
     "possible without this."),

    ("Organs are laid down", "Weeks 3–8 · the embryo",
     "Heart, brain, spine, limbs and every other organ are formed while the "
     "embryo is smaller than your thumb. This is the shortest stage and the "
     "one where anything crossing the placenta has the largest effect."),

    ("Growth and maturing", "Weeks 9–40 · the foetus",
     "The organs that exist get bigger and finish developing. The lungs are "
     "among the last to be ready, which is why being born early is mostly a "
     "breathing problem."),

    ("Birth", "Around 40 weeks",
     "The muscular wall of the uterus begins contracting and the cervix opens. "
     "The contractions push the baby out through the vagina, the umbilical "
     "cord is cut, and the placenta — no longer needed — is delivered "
     "afterwards."),
]

STAGE_CARDS = [{"term": "%s · %s" % (name, when), "gloss": what}
               for name, when, what in STAGES]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 125 character for character. Slugs are
    # permanent (§8.4) and are the join for every `requires` edge and every
    # progress record — b5-02, b5-03 and b5-05 all point at this string.
    #
    # ⚠️ NOTES-B5 §0 records the one filename correction in this unit: the
    # previous notes called this lesson `gestation-the-placenta-and-birth`,
    # WITH the article. `structure.py` has no article and the generator wins.
    "slug":        "gestation-placenta-and-birth",
    "title":       "Gestation, the placenta and birth",
    "discipline":  "biology",
    "unit":        "reproduction",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # The `d` clause of the split bullet — gestation and birth. Minted in
    # ks3_data/substatements.py for this unit; §5.7's exactly-once rule means
    # this lesson claims `d` and nothing wider.
    "covers":      ["KS3.B.REP.01d"],
    # ⚠️ Both are genuinely OUTSIDE this lesson's own bullet, and rung 4 reaches
    # into both by name: it asks the student to compare the alveoli, the villi
    # and the placenta as three solutions to one problem. `GAS.01b` is b4-03's
    # (adaptations of the gas exchange surface) and `NUT.04c` is b3-07's
    # (adaptations of the digestive system). Named and leant on, not taught —
    # which is what `touches` is for.
    "touches":     ["KS3.B.GAS.01b", "KS3.B.NUT.04c"],
    "beyond_statutory": False,
    # `structure-function` at 3 because the whole page is one exchange surface's
    # specification and rung 4 generalises it across three organs — the same
    # level b3-07 and b4-03 take for the same idea. `cells-and-systems` at 2 is
    # the unit's thread, carried by b5-03 and b5-05.
    "threads":     [{"id": "structure-function", "level": 3},
                    {"id": "cells-and-systems", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # No `requires` and no `before_this`: Design draws no "Before this lesson"
    # card and the engine would emit one from either. All four of her links live
    # in the middle card, the forward one first — see "What could not be
    # lifted" 6. The two cross-unit links are also the two destinations the
    # hook's dropped anchors pointed at, so nothing is lost with the markup.
    "requires":    [],
    "assumes":     [],
    "references":  ["lifestyle-and-the-developing-foetus",
                    "gametes-and-fertilisation",
                    {"unit": "B4", "lesson": "alveoli-built-for-exchange"},
                    {"unit": "B3",
                     "lesson": "absorption-and-the-small-intestine"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Exchange surfaces compared quantitatively, the hormones of "
                   "pregnancy and birth, and the ethics of antenatal "
                   "screening.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "For nine months one organism lives inside another and "
                    "takes everything it needs from it — without their blood "
                    "ever meeting.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-stages` is the third: no control of
    # its own, so it mirrors `s-cross` and ticks on the bench's predicate — see
    # the docstring. `short` and `label` are Design's own `RAIL_SHORT` and
    # `RAIL` strings (page lines 315–321), all four of them.
    "rail": [
        # `isDone('s-hook')` is `s.hookChoice !== null` (page line 410): the
        # stop ticks on the commitment, which is the only thing the hook asks
        # for. Nothing is ticked on load (MRB-208) — `hookChoice` opens null.
        {"anchor": "s-hook", "short": "HOOK", "label": "Never mix",
         "done_when": "committed"},
        # Design's own threshold, kept: `Object.keys(s.opened).length >= 6`
        # (page line 411). ALL SIX checked, not one — a stop that ticked on the
        # first substance would call the bench finished at a sixth of it, and
        # the lesson's claim is about the SET: the same rule, in both
        # directions, with one crossing that is not diffusion at all.
        {"anchor": "s-cross", "short": "CROSS", "label": "Which way?",
         "done_when": "all_six_checked"},
        # `isDone('s-ladder')` is both marked rungs answered AND both
        # self-marked rungs checked (page line 413).
        {"anchor": "s-stages", "short": "STAGES", "label": "Forty weeks",
         "mirrors": "s-cross", "done_when": "all_six_checked"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3), and no length
    # tell is possible in an unmarked set.
    #
    # ⚠️ The four options are the lesson's two misconceptions written out:
    # A is REPRO-08 (the bloods mix) and D is REPRO-07 (the foetus uses its
    # lungs). Both are elicited HERE, before anything is explained, which is
    # what `misconceptions[].elicited_by` records.
    #
    # ⚠️ The reveal's two inline links are gone and their words are not — see
    # "What could not be lifted" 1. Both destinations survive in `references`.
    "phenomenon": {
        "title": "The mother's blood and the foetus's blood never mix.",
        "prompt": "They are two separate circulations, kept separate for the "
                  "whole of the pregnancy. And yet the foetus does not "
                  "breathe, does not eat, and does not use its kidneys — "
                  "everything it needs arrives, and everything it produces "
                  "leaves.",
        "commit": "So how does oxygen get from one to the other?",
        "options": [
            "The two bloods mix in the placenta and share it",
            "It diffuses across from one blood supply to the other",
            "The mother breathes it down the umbilical cord",
            "The foetus takes it from the fluid around it, using its lungs",
        ],
        "reveal": "It diffuses. In the placenta the two blood supplies are "
                  "brought within a fraction of a millimetre of each other "
                  "across an enormous surface, and substances move between "
                  "them from where there is more to where there is less. No "
                  "pumping, no mixing, no decision — the same process you met "
                  "in the alveoli and the small intestine, solving a third "
                  "version of the same problem.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ IDs are PRE-ALLOCATED by the commander (MRB-244). This lesson owns
    # `REPRO-07` and `REPRO-08` and nothing else, and NOTES-B5 §5 pins the
    # mixing belief to `REPRO-08` by name. No id is minted here, the spare range
    # `REPRO-17+` is untouched, and `docs/ks3/misconception-register.md` is the
    # commander's file — the two statements are reported for writing into it.
    #
    # ⚑ Listed in PAGE order, so `REPRO-08` comes first. See the docstring: id
    # order and page order cannot both be honoured and page order is the one a
    # reader can check.
    #
    # `elicited_by` is honest for both: the hook's option A is the mixing belief
    # and option D is the breathing belief, and the student commits to one of
    # the four before a word of explanation. `r_hook` emits
    # `data-activity="hook"`, so both values resolve on the built page.
    #
    # `confronted_by` is the confrontation activity for both, and `REPRO-08` is
    # confronted a second time in ladder rung 2 — which is the whole of that
    # rung's question.
    "misconceptions": [
        {"id": "REPRO-08",
         "statement": "The baby's blood mixes with the mother's blood in the "
                      "placenta.",
         "elicited_by": "hook",
         "confronted_by": "two-wrong-ideas"},
        {"id": "REPRO-07",
         "statement": "The baby breathes and eats inside the uterus.",
         "elicited_by": "hook",
         "confronted_by": "two-wrong-ideas"},
    ],

    # ── vocabulary ──────────────────────────────────────────────────────────
    # Design draws no keyword block in B5, so these never reach the lesson body:
    # the TERMS become the unit page's chips and the reading-age gate's
    # exclusion list. Definitions are AUTHORED, assembled from the page's own
    # sentences — see "What could not be lifted" 11. Third person, function-
    # first, no euphemism, and no claim the page does not make.
    #
    # "uterus" and "cervix" are deliberately absent: `b5-01` defines both, and a
    # term defined twice in one unit is a term that can drift. "embryo" and
    # "foetus" ARE repeated from `b5-05`, in the same words, because this page
    # is where the eight-week seam between them is actually taught.
    "vocabulary": [
        {"term": "gestation",
         "definition": "The time a developing organism spends in the uterus, "
                       "from implantation to birth — about 40 weeks in "
                       "humans.",
         "note": "Pregnancy is dated from the first day of the last period, so "
                 "the familiar forty weeks is about two weeks longer than the "
                 "time the foetus has existed."},
        {"term": "placenta",
         "definition": "The exchange surface between two separate "
                       "circulations, where dissolved substances move between "
                       "the mother's blood and the foetus's blood.",
         "note": "The two blood supplies come close enough to diffuse across, "
                 "and never mix."},
        {"term": "umbilical cord",
         "definition": "The cord that carries the foetus's own blood out to "
                       "the placenta and back.",
         "note": "It does not carry the mother's blood, and nothing in it is "
                 "food."},
        {"term": "exchange surface",
         "definition": "A surface built to move substances between two places "
                       "by diffusion: a very large surface area, a very thin "
                       "barrier, and a good blood supply to keep the "
                       "concentration difference up.",
         "note": "The alveoli, the villi and the placenta are three of them, "
                 "in three different systems."},
        {"term": "embryo",
         "definition": "The developing organism in the first eight weeks, "
                       "while the organs are being laid down.",
         "note": None},
        {"term": "foetus",
         "definition": "The developing organism from about week nine, once the "
                       "organs exist and are growing and maturing.",
         "note": None},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # Design's legal line names this slot and no artwork exists for it, so it is
    # DECLARED at `needed` rather than dropped: the manifest is generated from
    # this field, which turns a dangling reference into a tracked sourcing task.
    # `needed` is not a build blocker.
    #
    # ⚠️ The caption describes only what this lesson teaches, and it is drawn to
    # the tone: an exchange surface with two separate circulations and labelled
    # directions of movement. No body outline, no figure, nobody depicted.
    # NOTES flag 13 asks Mide to confirm what the human pages illustrate and at
    # what level of detail BEFORE anything is commissioned, and this is a
    # proposal, not a commission.
    "figures": [
        {"id": "b5-placenta-exchange",
         "kind": "diagram",
         "caption": "The placenta drawn as an exchange surface: the mother's "
                    "blood on one side, the foetus's blood on the other in "
                    "the folded finger-like projections, the two brought "
                    "within a fraction of a millimetre and never joined, with "
                    "the umbilical cord carrying the foetus's own blood to and "
                    "from it. Arrows labelled for direction — oxygen and "
                    "glucose crossing in, carbon dioxide and urea crossing "
                    "out.",
         "status": "needed"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-cross — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b5/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 104), so the segment is MEASURED, not inherited — and it is
        # on INK, so every text rule in the instrument's CSS must be scoped to
        # at least (0,2,0) to beat `.ks3-dark p`. That is the engine pass's
        # business and is recorded in `ks3_data/b5/__init__.py`.
        {"type": "crossing-bench", "id": "which-way-does-it-cross",
         "anchor": "s-cross",
         "demand": "investigate",
         "eyebrow": "At the exchange surface · six substances",
         "heading": "Which way does it cross?",
         "head_counter": {"format": "{n} of 6 checked", "total": 6},
         "prompt": "Pick a substance, commit to a direction, then check it. "
                   "Every answer comes from the same rule: things move from "
                   "where there is more of them to where there is less.",

         "subs": SUBS,

         # ⚖️ THE TWO DIRECTIONS, and they are Design's `IN` and `OUT`
         # constants (page lines 323–324) rather than markup. Order is
         # load-bearing: `subs[].dir` is an INDEX into this list, so index 0 is
         # into the foetus and index 1 is out to the mother. Reordering these
         # two entries silently inverts four of the six answers.
         "choices": [{"id": "in", "label": "Mother’s blood → foetus"},
                     {"id": "out", "label": "Foetus → mother’s blood"}],
         "commit_label": "Which way does it cross the placenta?",

         # ⚖️ The check is LOCKED until the student has committed
         # (`checkLocked: !hasPick || opened`, page line 511), and locked again
         # once opened so a substance cannot be re-answered after the reveal. A
         # student who could read the verdict first and then say what they
         # expected has predicted nothing — and this page is a page about a
         # rule that becomes predictable.
         "check_label": "Check it",
         "hint": {"idle": "Choose a direction first.",
                  "ready": "Ready.",
                  "done": "Now try another substance."},
         # ⚠️ "Other way round" rather than "Wrong" — Design's own string, and
         # it names what the student got instead of judging them. MRB-202: only
         # the ladder marks correctness.
         "verdict": {"right": "Correct", "wrong": "Other way round"}},

        # #s-stages — the band panel. Rail stop 3, mirroring `s-cross`; see
        # the docstring. `rule` is the component: band ground, 3px ink border, an accent-text
        # eyebrow and a display statement, then a card grid — Design's markup
        # (page lines 154–171) minus the number chips and minus stage 02's
        # promotion. `.ks3-rule` ships exactly her section's ground, border and
        # padding, which is why this is `rule` and not `comparison`.
        {"type": "rule", "anchor": "s-stages",
         "eyebrow": "Forty weeks, in five stages",
         # The promotion `r_rule` cannot draw, said in prose instead — and it is
         # Design's own sentence, directly above her own promoted card.
         "statement": "Building the supply line comes first. Everything else "
                      "depends on it.",
         "cards": STAGE_CARDS},

        # Design nests this inside `#s-stages`; `r_rule` has no nested slot, so
        # it renders directly under the panel in document order. See "What could
        # not be lifted" 5.
        {"type": "key-fact", "ref": "built-to-spec"},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "REPRO-08"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # The one line that must survive the lesson, and it is deliberately the
    # GENERAL one: the placenta is built to the same specification as two
    # surfaces the student has already met. That is what rung 4 then asks them
    # to do something with.
    "key_facts": [
        {"id": "built-to-spec",
         "text": "The placenta is an exchange surface, built to the same "
                 "specification as the alveoli and the villi: a very large "
                 "surface area, a very thin barrier, and a blood supply on "
                 "both sides to keep the concentration difference up. The two "
                 "blood supplies come close enough for substances to diffuse "
                 "across, and never mix.",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`, and an authored statement wins over the register.
        # The block asks for no commitment, on Design's page and here, so it is
        # not a rail stop and emits no completion contract (this is B1's
        # `confrontation` case, not the MRB-220 R1 `predict` case).
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "REPRO-08",
         "statements": [
             # ── REPRO-08 ────────────────────────────────────────────────
             # Quotes are bare: `_quoted()` strips and re-wraps in “ ” exactly
             # once, which is what Design draws.
             #
             # ⚠️ The two consequences are given in Design's order — blood
             # groups first, pressure second — and both are physical
             # consequences of mixing, not warnings. The paragraph closes on
             # the cord, which is what ladder rung 2 then marks.
             {"quote": "The baby's blood mixes with the mother's blood in the "
                       "placenta.",
              "body": ["Two circulations, side by side, never joined. If they "
                       "did mix, two things would go wrong immediately. The "
                       "first is blood groups: a mother and her baby often "
                       "have different ones, and mixing incompatible blood "
                       "makes it clot. The second is pressure — an adult heart "
                       "pushes blood far harder than a foetal one, and the "
                       "delicate vessels of the placenta would simply be "
                       "destroyed. What the placenta does instead is bring the "
                       "two supplies within a fraction of a millimetre of each "
                       "other over an enormous folded surface, so that "
                       "dissolved substances can diffuse across the gap. "
                       "Everything the foetus receives arrives that way, one "
                       "molecule at a time, down a concentration difference. "
                       "The cord is not a pipe carrying the mother's blood; it "
                       "carries the foetus's own blood out to the exchange "
                       "surface and back."]},

             # ── REPRO-07 ────────────────────────────────────────────────
             # ⚠️ One belief, two organs, and the paragraph answers both halves
             # with the same argument — there is nowhere for either to happen.
             # It is lifted whole. The lungs half is also what makes stage 04's
             # "being born early is mostly a breathing problem" mean something.
             {"quote": "The baby breathes and eats inside the uterus.",
              "body": ["It does neither, and the reason is the same both "
                       "times: there is nowhere for either to happen. The "
                       "lungs are full of fluid for the whole pregnancy and no "
                       "gas exchange takes place in them — the first breath at "
                       "birth is genuinely the first time they are used, which "
                       "is why the lungs are among the last organs to be ready "
                       "and why babies born very early often need help with "
                       "breathing. Food is the same story in a different "
                       "organ. Nothing that could be called a meal goes down "
                       "the umbilical cord: what crosses the placenta is "
                       "glucose, amino acids and other small molecules already "
                       "dissolved in blood, which is what the mother's "
                       "digestive system has spent hours turning food into. "
                       "The foetus is supplied at the end of somebody else's "
                       "digestion."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026, AND BOTH RUNGS ARE FIXED.
    # Six distractors are Mide's own replacement copy, applied verbatim; each
    # now states a WRONG RULE in the same shape as the correct answer, which is
    # where the parity comes from. Both correct options, both `answer` indices
    # and the gate's threshold are untouched. See the docstring for the ruling,
    # the measurements, and the straight/curly apostrophe note.
    #
    # ⛔ Superseded, kept: this block used to read "MEASURED, AND BOTH MARKED
    # RUNGS FAIL. Neither option set is rewritten … the repair is not this
    # pass's to make." The repair was Mide's, and he has made it.
    #
    # Rungs 3 and 4 are Design's `SELF_RUNGS`: the student marks themselves
    # against her criteria, and only the ladder scores. Her rung titles are kept
    # verbatim — the engine's slot names are internal and the student reads the
    # title.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Read the surface",
            "q": "Why does oxygen move from the mother’s blood into the "
                 "foetus’s blood at the placenta?",
            "options": [
                "The mother's heart pumps blood hard enough to push oxygen "
                "across into the foetus",
                "There is more oxygen in her blood than in the foetal blood, "
                "so it diffuses across",
                "The placenta works out what the foetus needs and sends "
                "exactly that across to it",
                "The two blood supplies mix in the placenta, so whatever she "
                "has the foetus has too",
            ],
            "answer": 1,
            "feedback": {
                0: "Nothing is pumped across. The two circulations are "
                   "separate, and her heart moves her blood only.",
                # ⚑ This correction is the one that comes closest to REPRO-09,
                # which b5-05 owns. It CONCEDES the active-transport half
                # ("does actively carry a few things") rather than refuting the
                # belief, which is exactly why no third id is minted here. See
                # the docstring.
                2: "The placenta does actively carry a few things, such as "
                   "antibodies. Oxygen is not one of them — it simply "
                   "diffuses.",
                3: "They never mix. If they did, differing blood groups and "
                   "adult blood pressure would both cause serious harm.",
            }},
        "apply": {
            # ⚑ REPRO-08's SECOND confrontation, and the only one the page
            # marks. The whole question is the belief.
            "title": "Rung 2 · The one that catches people",
            "q": "A student says the umbilical cord carries the mother’s blood "
                 "into the baby. What is wrong with that?",
            "options": [
                "The cord carries the mother’s blood into the baby, which is "
                "exactly what it is for",
                "The cord carries the foetus’s own blood out to the placenta "
                "and back",
                "The cord carries food rather than blood, because the baby is "
                "being fed through it",
                "The cord carries air to the baby’s lungs, because it has to "
                "breathe somehow",
            ],
            "answer": 1,
            "feedback": {
                0: "Then a mother and baby with different blood groups could "
                   "not survive a pregnancy together, and they routinely do.",
                2: "It carries blood. What it does not carry is anybody else’s "
                   "blood, and nothing in it is food in any recognisable "
                   "sense.",
                3: "The foetal lungs are full of fluid and are not used. "
                   "Oxygen arrives dissolved in blood, from the placenta.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the surface",
            "q": "Explain how the placenta supplies a foetus with oxygen and "
                 "glucose and removes its carbon dioxide and urea, without the "
                 "two bloods mixing. Name the three features that make it a "
                 "good exchange surface.",
            "field_label": "Your explanation",
            "placeholder": "The two circulations are brought close together…",
            "success": [
                "Says the two blood supplies are brought very close together "
                "but stay separate.",
                "Says substances move by diffusion, from where there is more "
                "to where there is less.",
                "Gets both directions right: oxygen and glucose in, carbon "
                "dioxide and urea out.",
                "Names a large surface area, a thin barrier and a good blood "
                "supply on both sides.",
                "Says the umbilical cord carries the foetus’s own blood to and "
                "from the placenta.",
            ]},
        "produce": {
            # ⚑ The rung the key fact exists to make possible, and the reason
            # `touches` names `KS3.B.GAS.01b` and `KS3.B.NUT.04c`: it asks for
            # one idea to be carried across three organs in three systems, and
            # then for the one way this organ's problem is harder.
            "title": "Rung 4 · Take it somewhere new",
            "q": "Alveoli, villi and the placenta are three different organs "
                 "in three different systems. Explain what problem all three "
                 "are solving, what design features they share, and one way "
                 "the placenta’s problem is harder than the other two.",
            "field_label": "Your answer",
            "placeholder": "All three have to move substances…",
            "success": [
                "Says all three move substances between two places by "
                "diffusion, and need a big enough rate.",
                "Names the shared features: large surface area, thin barrier, "
                "good blood supply maintaining the difference.",
                "Gives a correct example of what crosses at each of the "
                "three.",
                "Says what is harder at the placenta — the two supplies belong "
                "to two different individuals and must not mix.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # ⚠️ Birth is the last clause and it is anatomy: the uterus muscle
    # contracts, the cervix opens, the baby is delivered, the placenta follows.
    # Design's scope decision (NOTES flag 25), carried into the summary exactly
    # as she carried it into stage 05.
    "key_note": "Gestation is the time from implantation to birth, about 40 "
                "weeks in humans. The placenta is the exchange surface between "
                "two separate circulations: oxygen, glucose and other small "
                "molecules diffuse in from the mother's blood, carbon dioxide "
                "and urea diffuse out into it, and the two never mix. The "
                "umbilical cord carries the foetus's own blood to and from the "
                "placenta. Organs are laid down in the first eight weeks; the "
                "rest is growth. At birth the uterus muscle contracts, the "
                "cervix opens, the baby is delivered, and the placenta "
                "follows.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES flag 24: it ENDS ON AN OPEN QUESTION, deliberately, and Design
    # asks for that to be confirmed rather than assumed. The layer is also the
    # only place on the page that mentions the father, and it does so as a
    # statement about chromosomes in an organ — which is the tone treatment
    # holding at the one point where it would be easiest to drop it.
    #
    # This is the lesson's ONLY `explainer`, so it is the whole of the §5.2
    # prose budget: ~215 words against ~450.
    "stretch": [
        {"type": "explainer", "id": "an-organ-that-is-not-rejected",
         "text": "The placenta is not the mother's organ. It grows from the "
                 "same ball of cells as the embryo, so its cells carry the "
                 "embryo's chromosomes — half of them from the father — and it "
                 "is the only organ a human being ever builds, uses and then "
                 "discards. That raises a question nobody has fully answered. "
                 "An immune system attacks tissue whose cells it does not "
                 "recognise; that is why transplanted organs are rejected "
                 "without drugs to prevent it. Yet here is an organ, and an "
                 "entire foetus, carrying a set of foreign proteins, growing "
                 "inside another person's body for nine months, pressed right "
                 "up against her blood supply, and normally not attacked at "
                 "all. Several mechanisms are known — the outer layer of the "
                 "placenta displays unusual surface proteins, and the immune "
                 "response in the uterus is locally dialled down — but how "
                 "they add up to nine months of tolerance is still an active "
                 "research question. The most ordinary event in biology is "
                 "also one of its stranger unsolved problems."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check why the two bloods must stay apart?",
              "cta": "Ask about this lesson",
              "anchor": "s-cross"},

    # ⊕ MRB-228's `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph and nothing in it is a safety instruction: it is a
    # note about how the numbers on this page were taken, a correction about how
    # pregnancy is dated, a signpost, and a declaration about a figure not yet
    # drawn. Routing it through `safety_note` would print it in the treatment
    # reserved for "never light a candle without an adult", which devalues the
    # safety line — and §8.10 puts a legal note small, at the bottom edge, never
    # as a callout. b5-03, b5-05, b4-01, b3-05 and b3-07 resolve the identical
    # foot line the identical way.
    #
    # ⚠️ Lifted whole. The signpost sentence — school nurse, doctor or midwife,
    # and RSE and PSHE for relationships and consent — is part of it and is not
    # trimmed, rewritten or promoted into the body of the lesson. Every human
    # lesson in this unit closes with the same two signposts (NOTES §4).
    #
    # ⚠️ Design sets the figure id in mono inside the sentence; a foot line is
    # escaped, so `b5-placenta-exchange` renders in body copy. The words are
    # unchanged.
    "convention_note": "Times are typical values. Pregnancy is dated in weeks "
                       "from the first day of the last period rather than from "
                       "fertilisation, so the familiar forty weeks is about "
                       "two weeks longer than the time the foetus has existed. "
                       "This lesson covers the biology; anything personal "
                       "belongs with your school nurse, doctor or midwife, and "
                       "relationships and consent are covered in RSE and PSHE. "
                       "The labelled placenta diagram is declared in the "
                       "lesson record as b5-placenta-exchange, awaiting "
                       "illustration.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # `analysis-and-evaluation`: the bench is commit-then-check across six
    # cases with one rule to predict from, and the student is asked to apply it
    # in both directions before the page states it.
    # `scientific-attitudes`: the lesson ends on a question that is open — the
    # Going further says in terms that how immune tolerance adds up is still
    # being researched, which is a claim about the state of knowledge rather
    # than about placentas.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
