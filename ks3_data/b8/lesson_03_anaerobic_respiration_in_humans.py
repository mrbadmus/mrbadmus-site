"""B8 L3 — Anaerobic respiration in humans (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b8/b8-03-anaerobic-respiration-in-humans.dc.html` (582 lines), her
author's notes `docs/ks3/design-reference/b8/NOTES-B8.md`, and the B8 payload schema
`docs/ks3/b8-inventory/PAYLOAD-SCHEMA.md` §4, §7, §8, §9 and §10, under the
MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the items under "What could not be lifted" and the three rung-2
distractors repaired under MRB-177, both itemised below. The four paces, the
four bars, the five phase notes, the three fact cards, the four hook options,
both marked rungs and both self-marked rungs came out of
`node tools/extract_design_payload.js`, not off a keyboard.

── ⚠️ THE ONE BEHAVIOUR THE WHOLE LESSON RESTS ON ───────────────────────

**The breathing bar is driven by LACTATE, not by pace, and it must stay high
AFTER the runner stops.** Measured off page line 438, which carries Design's
own comment saying exactly that:

    breathing = min(100, round(20 + supply × 0.6 + lactate × 0.5))

`pace` does not appear in it. Neither does `demand`. The consequence, traced
press by press from the opening flat-out sprint:

    press            supply  lactate  demand shown   breathing
    (opening state)      25        0            25         35%
    Run 10 s             43       59           150         75%
    Run 10 s             61      100           150        100%
    **Stop 30 s**        51       78            25         90%
    Stop 30 s            41       56            25         73%
    Stop 30 s            31       34            25         56%
    Stop 30 s            25       12            25         41%
    Stop 30 s            25        0            25         35%  ← `ever_recovered`

The bold row IS the lesson. The demand bar collapses from 150 to 25 the instant
the runner stops and the breathing bar stays at 90%, which is the page's own
big question — *"The running has finished. Something else has not."* — drawn as
two bars. `notes["debt"]` names it in words: *"The muscles are not asking for
this oxygen — the lactic acid is."*

A breathing bar that fell when the runner stopped would teach the opposite of
what this lesson exists for. Three parts of the model defend that behaviour and
all three are authored below:

  * `supply_decay: 10` — recovery lowers supply too (`max(25, supply − 10)`
    while lactate remains). Without it, breathing would fall on the supply half
    as well and the effect would be muddied; with it, the only thing holding
    breathing up after two presses is the lactate term.
  * `recover_clear: 22` per 30 s against `lactate_max: 100` — a sprint takes
    five recovery presses to clear. Not padding: a student who presses once and
    leaves has seen breathing fall from 100% to 90%, which is the wrong story.
    The rail stop only ticks when lactate reaches zero.
  * `supply_step: 18` regardless of pace — at walking pace the gap never opens
    and no lactate is made, so the bench can show the AEROBIC case too, which is
    what `notes["within"]` is for. Without it the contrast is untestable.

⚠️ **`model["bar_divisor"]` applies to the two ` units` bars ONLY.** Measured
off page lines 496–502: `demand` and `aerobic` fill at `min(100, value / 1.6)`;
`lactate` fills at `min(100, lactate)` — its own value, because it is already on
a 0–100 scale — and `breathing` fills at `breathing`, because it is already a
percentage. Schema §4 carries one `bar_divisor` on the model and gives the bars
no per-bar scale key, so this cannot be said in the record. It is said here, and
in the report, because an engine that divides all four by 1.6 renders a full
lactate bar at 62% and a maxed breathing bar at 62%, which quietly costs the
lesson its punchline. See "Needed from the engine" at the foot of this
docstring.

── `covers` is a CLAUSE, not the whole bullet ───────────────────────────

`KS3.B.RESP.03` reads, in full:

    the process of anaerobic respiration in humans and micro-organisms,
    including fermentation, and a word summary for anaerobic respiration

`ks3_data/substatements.py` splits it, and the split is the right one: clause
(a) is a body that has run out of oxygen and must pay it back, clause (b) is a
process we deliberately RUN, in a brewery and a yoghurt maker, with no debt to
repay at all. This lesson owns **(a) only**:

    KS3.B.RESP.03a  Anaerobic respiration in humans: what a muscle does when
                    the oxygen supply cannot keep up, and a word summary for it.

Both halves of (a) are discharged and neither is left to another lesson: the
bench is the oxygen supply failing to keep up, and `#s-equation` is the word
summary — *glucose gives lactic acid* — which is also what rung 1 marks. The
substatement file's own note records that the word summary named at the end of
the bullet is not a third clause; it is the product of the process, and it
lands with (a), where the equation is first written. It does.

`KS3.B.RESP.03b` is `fermentation`'s and is deliberately NOT claimed here, even
though rung 1's third option names yeast and alcohol. That option is a
distractor whose correction points the student at the other lesson by name — a
reference, not a restatement.

── ⚑ FOR MIDE'S SCIENCE GATE — the four NOTES-B8 flags that land here ───

  * flag 11  **"Delayed-onset muscle soreness is NOT lactic acid."**
             CHECKED AND AUTHORED PLAINLY, IN THE BODY, WITH NO HEDGE — which
             is Design's own drawing and is what MRB-225 requires. This is the
             canonical-story case in B8: the version that is famous (lactic acid
             causes the ache two days later) is taught in a great many gyms and
             PE departments, and it is false. Blood lactate returns to resting
             levels within about an hour of stopping — usually much sooner —
             while DOMS peaks 24 to 72 hours later, and it is caused by
             microscopic damage to muscle fibres and the inflammatory response
             that repairs it. That is why it follows unfamiliar and eccentric
             (downhill, lowering) work most strongly and why it fades with
             habituation, both of which the page states. Well supported, and the
             page's own last sentence — that the myth sells stretching and
             massage as a way of flushing out something already gone — is the
             reason it matters rather than a swipe.

             ⚖️ **Nothing later in the lesson takes this back**, which is the
             MRB-225 test. The claim is stated at its true size in the first
             place: lactic acid IS real, it IS responsible for the burning
             *during* the effort, and its job ends when you stop. Three claims,
             all true, none retracted. Design shrank it before we got here.
             It is Mide's to confirm — flag 11 is the one Design says
             "generates a staffroom conversation" — but nothing was softened.

  * flag 12  **The oxygen-debt model, and "oxygen debt" over EPOC.**
             CHECKED AND LEFT, AND THE LEGAL LINE DOES DECLARE IT. Verified
             clause by clause against `convention_note` below: arbitrary units
             ✓, a fixed aerobic ceiling ✓, lactate as a single accumulating
             quantity ✓, several real fuel systems and continuous production and
             clearance named as what the model omits ✓, large differences
             between individuals ✓, and the ten-second steps declared as a
             reading device rather than a measured timescale ✓. Six declarations
             for six simplifications; nothing in the model is undeclared.

             The **EPOC** half is not in the legal line and is not added. Design
             judged "excess post-exercise oxygen consumption" wrong for KS3 and
             the judgement is sound: EPOC is the modern term precisely because
             it drops the debt metaphor, and the debt metaphor is what this
             lesson teaches with — *"a loan rather than a loss"*, *"borrowing",
             "the debt is called in"*, and the key fact's own naming of the
             oxygen debt. Naming EPOC here would introduce a term in order to
             disown the one the page is built on. Reported, unchanged; the
             GCSE endmatter already says the debt gets quantified later.

  * flag 13  **The liver's two options for lactate.** CHECKED AND LEFT.
             Oxidise it completely — using some of the oxygen you are gasping
             for — or spend energy converting it back to glucose and returning
             it to the muscle. Both are real and both are correctly described,
             including the cost of the second. The **Cori cycle is deliberately
             not named**, and that is the right call at KS3: the name adds no
             explanatory work the sentence has not already done, and the GCSE
             endmatter carries the destination ("the liver's conversion of
             lactate back into glucose"). Left exactly as drawn.

  * flag 14  **"one of the best single predictors of endurance performance
             there is."** JUDGED CAREFULLY UNDER MRB-225, AND LEFT — the claim
             does not need to shrink, because Design already wrote it at its
             true size. The strong form ("the best predictor") would be an
             overstatement; **the hedged form Design actually wrote is what the
             exercise-physiology literature supports.** In trained and
             homogeneous groups, the pace or power at the lactate threshold
             routinely out-predicts VO₂max for endurance performance, which is
             why threshold testing exists as a commercial service at all. Two
             further checks on the same paragraph, both clean: "Training moves
             that threshold" is true and is the reason the test is repeated over
             a season, and the treadmill pinprick is how it is actually done.

             ⚠️ Recorded so a later reader does not "tighten" it into
             falsehood in either direction: *one of the best* is load-bearing.
             Shrinking it further ("a useful predictor") would understate a
             genuinely strong result, and MRB-225 shrinks a claim until it is
             true, not until it is timid. Growing it ("the best") would be the
             overstatement the rule exists to stop. It stays byte-identical.

  * flag 21  **No diagrams in the unit.** See `figures` below — measured.

── What could not be lifted byte-identical, and why ─────────────────────

1. **Two build-internal lesson codes in student prose, resolved to titles.**
   Design prints `b8-05` and `b8-04` into teaching copy. A student cannot
   resolve a slot code — it is meaningless to them and is exactly the platform
   leakage §8.10 exists to stop — so each is replaced by what it stands for,
   using the string Design herself uses for the same destination in her own
   endmatter. b7-04 resolved the identical case the identical way.

       Design:  The full comparison is b8-05’s job.
       Built:   The full comparison is the job of Aerobic vs anaerobic.

       Design:  That is what yeast does, and it is b8-04’s subject.
       Built:   That is what yeast does, and it is the subject of Fermentation
                and what we use it for.

   Every science word is unchanged and neither destination is lost: both are
   `references` edges, which is where the engine puts cross-lesson navigation,
   and Design draws both in "Connects to" as well.

2. **The fact cards' `kind` becomes `role`.** Design's card is a mono accent tag
   (*What is missing*), a display name and a body; `_rule_card` reads that shape
   under the names `role` / `name` / `body`, which is b7-01's mapping. Three
   strings, three slots, nothing joined and nothing lost.

3. **The key fact stays nested, on the CARD ground.** Design nests it inside
   `#s-equation` (page lines 173–176) with `background: var(--ks3-card)` and
   `box-shadow: 5px 5px 0 var(--ks3-accent)` — the shipped stylesheet's own
   values, so contract R3 does not arise. `r_rule` takes a nested `key_fact`, so
   unlike b7-04 this one does not have to be lifted to a top-level block.
   `card` rather than `band` because the section is already `--ks3-band` and
   band on band is invisible.

4. **The instrument's section heading loses its `<h2>` level.** Design draws
   "Run it, then stop and watch" as an `<h2>` inside `#s-bench` beside the mono
   clock. It is authored as the instrument's `heading` and the renderer decides
   the tag. No word changes.

5. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that a rail
stop came off, "the defect six units have found". Design draws FOUR stops and
`#s-equation` ticks on `s.everRecovered` (page line 386) — the BENCH's
predicate, character for character, one section to the left (page line 385).
The argument turned on a real measurement of the BUILT page: `doneByDom()` in
`shared/ks3.js` read only the DOM inside the stop's own section, and `r_rule`
emits a `<section class="ks3-rule">` with no rungs, no options, no reveal and
no `data-stage-done`, so `ks3_parity.check_rail_reachable` would fail the stop
and it could never tick however `done_when` were spelled. With MRB-208 confining
the rail to sections that require the student to do something, and inventing a
demand Design did not draw closed by MRB-205, THREE stops shipped.

The measurement of the engine was correct. The conclusion drawn about the page
was not.

MRB-205 was cited for one half of itself. Design draws, we render; page wins
over engine. It closes off inventing a control, and closes off dropping a stop
just as firmly. An engine that cannot express what Design drew is the thing
that gives way — and it has: `wireRail`'s `paint()` now resolves the tick at
RAIL level, where Design computes it, rather than looking inside the section.

And what page line 386 does is state the tick condition. The word summary is
the payoff of the bench beside it, and it carries no signals of its own because
`#s-bench` already took the student's commitment. That is a MIRROR, not an
alias.

So the fourth stop is declared: anchor `s-equation`, `mirrors: "s-bench"`,
`done_when: "debt_repaid"` — with Design's `SUMMARY` / *Word summary* pair
restored to it — and `ks3_parity.check_rail_matches_design` gates the built
rail against `docs/ks3/rail-manifest.md`. b7-01's `#s-summary`, b7-04's
`#s-jobs`, b4-05's `#s-stomata`, b5-06's `#s-designs`, b4-01's `#s-parts`,
b4-03's `#s-built`, c1-02's `#s-matrix`, c1-05's `#s-scale`, b3-01's
`#s-nutrients`, b3-02's `#s-limits`, b3-04's `#s-three` and b3-07's `#s-four`
are restored the same way. **The section keeps its anchor**, as it always did.

⚠️ Payload schema §7 recorded the three-stop count as its resolution for all
five B8 pages. That resolution is superseded; §7's own text has not been
re-cut, so read its count as historical.

── ⊕ MRB-177 LENGTH PARITY — RUNG 2 FAILED; RUNG 1 IS CLEAN ─────────────

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one):

    AS DESIGN DREW IT                        AFTER THE REPAIR
    rung 1  correct  4w vs 6 / 6 / 6   ✓     untouched
    rung 2  correct 23w vs 11 / 10 / 11 ✗    correct 23w vs 20 / 22 / 22   ✓

Rung 2 tripped both arms at once — strictly longest, clearing the field by 12
words and by a ratio of 2.1. A student could have scored it without reading it.

The construct is the one MRB-177 named: Design's correct option states a RULE
(what is happening, what it is for, and the name of it — *"the oxygen debt"*)
while all three distractors stated a one-clause wrong REASON, so the correct
answer was longer BY CONSTRUCTION. Each distractor is rewritten as a WRONG RULE
in the same three-part shape, keeping the belief it already carried and gaining
the consequence that belief licenses:

    r2 A  breathing has mechanical momentum
          + "so the breathing runs on under its own momentum"
    r2 C  the muscles are still consuming oxygen after you stop
          + "so they go on needing oxygen at the same rate as during the sprint"
    r2 D  breathing out is how heat leaves
          + "so the rate stays up until you have cooled"

**The correct option is unchanged, `answer: 1` is unchanged, Design's option
ORDER is unchanged, and all three of her corrections are byte-identical.** Each
still answers exactly the belief its rewritten distractor states, and two of the
three now land HARDER than before, which is the sign the repair was to the
construct and not to the science:

  * A now ends on *momentum*, and the correction's first clause is
    "Breathing rate is controlled by what is in your blood, **not by momentum**";
    its second, "Something is still being demanded", answers the new option's
    implied claim that nothing is.
  * C now says the muscles are still working **after you stop** and at the same
    rate, which is what "You are standing still. The muscles are not
    contracting" contradicts head-on.

⚠️ **Rung 1 is left alone, and its shape is the inverse of a tell**: the correct
answer, *"glucose gives lactic acid"*, is the SHORTEST of the four at 4 words
against 6 / 6 / 6, because a summary with one reactant and one product is
shorter than three summaries that wrongly carry a second. `length_tell` does not
fire — it only flags a correct answer that is strictly the longest — and
lengthening the correct option would mean changing the word summary itself,
which is the science the rung exists to mark. Recorded, not touched.

⛔ **No misconception id was minted for any rung-2 distractor.** RESP-13 is this
lesson's named spare and stays PERMANENTLY UNUSED — the same discipline as
`DRUG-07`, `PLANT-09`..`PLANT-12` and `REPRO-17`/`20`/`21`/`23`. Do not
re-point it. The three beliefs above are Design's own distractor beliefs, held
by real students, and they are recorded here rather than in the register because
a distractor belief is not a lesson-level misconception; the two the lesson
actually confronts are RESP-05 and RESP-06 below.

── ⛔ NO RUNTIME STATE IS AUTHORED ──────────────────────────────────────

Payload schema §0 rule 3. NOTES-B8 §2.3's payload sketch and Design's own
`state` block carry `supply`, `lactate`, `seconds`, `phase` and
`everRecovered`; every one of those is a value the RUNTIME owns, and under
contract R5 a key with no read site fails `ks3_key_audit.py`. The renderer
initialises its own state from `model` and `start`.

⚠️ **Design's `runDisabled: false` and `runStyle: ''` are NOT authored** (page
lines 506–507). They are constants read for nothing — the run button is never
disabled — and porting them would ship two dead keys. `stopDisabled` and
`stopStyle` ARE real, and are computed from `phase`, so they are the renderer's
and not the record's.

── Needed from the engine, and NOT done here (contract §0) ──────────────

One item, and it is the flagged behaviour rather than a new key:

    the per-bar fill scale. `model["bar_divisor"] = 1.6` is schema §4's single
    key and it is correct for `demand` and `aerobic` only. `lactate` fills at
    its own value and `breathing` at its own percentage — page lines 500 and
    502. No per-bar key is authored, because the engine pass is building
    `oxygen-debt` against schema §4 right now and a key it does not know about
    is a dead key under R5. It is in the report instead.
"""

# ── the four paces (page lines 322–327) ─────────────────────────────────
#
# ⚖️ `demand` is what the runner is ASKING FOR, in the bench's arbitrary units,
# and the aerobic ceiling is 80. So walking and jogging sit under the ceiling
# and can never open a gap; a hard run opens a small one; a flat-out sprint asks
# for nearly twice what the body can ever deliver. That spread is the bench: two
# paces that stay aerobic and two that do not, which is what makes
# `notes["within"]` reachable and the contrast testable. Do not compress it.
PACES = [
    {"id": "walk",   "label": "Walking",         "demand": 20},
    {"id": "jog",    "label": "Jogging",         "demand": 50},
    {"id": "run",    "label": "Hard run",        "demand": 85},
    {"id": "sprint", "label": "Flat-out sprint", "demand": 150},
]

# ── the model (page lines 329–331, 438, 509–525) ────────────────────────
#
# Every number here was read off Design's own arithmetic, not inferred. The
# three that carry the lesson — `supply_decay`, `recover_clear` and
# `supply_step` — are argued in the docstring and each defends the breathing
# bar's behaviour after the runner stops.
MODEL = {
    "supply_rest":  25,    # `SUPPLY_REST` — where supply starts and returns to
    # ⊕ MRB-257 (5.15) — THE RESTING DEMAND, AND IT IS NOT THE RESTING SUPPLY.
    # `read()` reused `supply_rest` as the demand for the ready phase, so
    # "Standing on the line" asked for 25 units while Walking asks for 20: the
    # bench said standing still costs MORE than walking. Supply comfortably
    # exceeding demand is the whole meaning of "at rest", and 15 against a
    # supply of 25 says it — every pace on the list is now more expensive than
    # standing, which is the only ordering that is true.
    "demand_rest":  15,    # what standing on the line actually asks for
    "supply_max":   80,    # `SUPPLY_MAX` — "the aerobic ceiling: everything
                           #  above this is borrowed" is Design's own comment
    "supply_step":  18,    # per 10 s run, regardless of pace
    "supply_decay": 10,    # per 30 s recovery, while lactate remains
    "recover_demand": 25,  # `RECOVER_DEMAND` — the demand bar once stopped
    "recover_clear":  22,  # lactate cleared per 30 s
    "lactate_factor": 0.55,  # of the demand−supply gap, per 10 s run
    "lactate_max":  100,
    # ⚠️ THE FORMULA THE LESSON RESTS ON. No `pace` term, no `demand` term.
    "breathing": {"base": 20, "per_supply": 0.6, "per_lactate": 0.5,
                  "max": 100},
    "run_seconds":     10,
    "recover_seconds": 30,
    # ⚠️ The two ` units` bars only — see the docstring and the report.
    "bar_divisor": 1.6,
}

# ── the four bars (page lines 494–503) ──────────────────────────────────
#
# ⚖️ ORDER IS THE ARGUMENT and it is Design's: demand, then what oxygen actually
# delivered, then what the gap between them made, then what the body is doing
# about it. Read top to bottom it is the whole lesson in four rows, and the
# fourth is the one that refuses to fall.
#
# `tone` is Design's own colour per bar and it is legible rather than decorative:
# `alert` is amber and belongs to the lactic acid, which is the accumulating
# problem; `ok` is the oxygen actually being delivered; `muted` is the two that
# are neither.
BARS = [
    {"id": "demand",    "name": "Energy demand",
     "suffix": " units",           "tone": "muted"},
    {"id": "aerobic",   "name": "Oxygen delivered (aerobic)",
     "suffix": " units",           "tone": "ok"},
    {"id": "lactate",   "name": "Lactic acid in the muscle",
     "suffix": " units",           "tone": "alert"},
    {"id": "breathing", "name": "Breathing rate",
     "suffix": "% of maximum",     "tone": "muted"},
]

# ── the five phase notes (page lines 448–452) ───────────────────────────
#
# The branch order on the page is: ready → recovering-with-lactate →
# recovering-cleared → shortfall → within. `{n}` in `shortfall` is the gap in
# units (`demand − supply`), Design's own `' + shortfall + '` substitution.
#
# ⚖️ `debt` is the payoff string of the whole bench, and it is the only one that
# says out loud what the bars are showing: the runner has stopped and the
# breathing has not. `cleared` is what stops the episode reading as damage —
# "a loan rather than a loss" is the same idea the Going further layer closes on.
NOTES = {
    "rest": "At rest. Oxygen delivery comfortably covers the demand, so "
            "everything is aerobic and no lactic acid is being made.",
    "within": "Demand is inside what the oxygen supply can cover, so this is "
              "entirely aerobic. You could hold this for a long time; nothing "
              "is building up.",
    "shortfall": "Demand is above the ceiling. Aerobic respiration is running "
                 "flat out and the gap — {n} units — is being covered "
                 "anaerobically, so lactic acid is accumulating. The burning "
                 "in your legs is that acid, and it is what will make you slow "
                 "down.",
    "debt": "You have stopped moving, and you are still breathing hard. The "
            "muscles are not asking for this oxygen — the lactic acid is. This "
            "is the oxygen debt being repaid, and until it is, your breathing "
            "rate is not your own to control.",
    "cleared": "Lactic acid cleared and breathing settling back. The debt is "
               "paid, and the whole episode cost you nothing but time — "
               "nothing was wasted, it was borrowed.",
    # ⊕ MRB-257 (5.13) — A DEBT HAS TO BE INCURRED BEFORE IT CAN BE REPAID.
    # `cleared` fired on `lactate <= 1`, which is also true of a runner who
    # never made any: Walking → Run 10 s → Recover 30 s read "Lactic acid
    # cleared… The debt is paid" with the acid bar at 0 units the whole way
    # through. The engine now tracks the PEAK lactate since the last reset and
    # branches here when it never rose.
    "nothing_to_repay": "Nothing to repay. This pace never went above what "
                        "the oxygen supply could cover, so no lactic acid was "
                        "made and there is no debt — your breathing settles "
                        "as soon as you stop, because it was never borrowing.",
    # ⊕ MRB-257 (5.14) — TWO DIFFERENT FACTS, AND THEY NEED TWO SENTENCES.
    # Once supply has climbed to meet demand, nothing FURTHER is being made —
    # but `within` says "nothing is building up" over an acid bar still reading
    # 4 units, indefinitely. What has stopped is the accumulating; what has not
    # happened yet is the clearing, and that only starts when the runner does.
    "within_with_lactate": "Demand is now inside what the oxygen supply can "
                           "cover, so nothing further is being made and this "
                           "is aerobic from here. The lactic acid already in "
                           "your muscles is still there, though — it clears "
                           "when you stop, not while you keep going.",
}

# ── the three fact cards (page lines 333–337) ───────────────────────────
#
# `role` is Design's `kind` under the name `_rule_card` reads — "What could not
# be lifted" 2. The three tags are science, not decoration: they sort the word
# summary into what is absent, what it costs and what is left over, which is
# the reading rung 1 marks and the whole of what makes this an UNFINISHED job
# rather than a different one.
FACT_CARDS = [
    {"role": "What is missing", "name": "No oxygen",
     "body": "The glucose is only partly broken down, which is why there is no "
             "carbon dioxide and no water on the right-hand side."},
    # ⚠️ "b8-05’s job" resolved to the lesson TITLE — "What could not be
    # lifted" 1. The destination survives as a `references` edge.
    #
    # ⚖️ "a small fraction" is deliberately unquantified HERE. NOTES-B8 flag 19
    # puts the "about twenty times" figure on b8-05 and §1 of the notes records
    # that b8-03 states only "far less energy" and points forward so the
    # CONTRAST lesson has something left to do. Do not import the number.
    {"role": "What it costs", "name": "Far less energy",
     "body": "The same glucose molecule gives a small fraction of what aerobic "
             "respiration gets from it. The full comparison is the job of "
             "Aerobic vs anaerobic."},
    {"role": "What is left", "name": "Lactic acid",
     "body": "It accumulates in the muscle, causes the burning, and has to be "
             "dealt with afterwards. Nothing is discarded — it is a debt, not "
             "a waste."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 148 character for character.
    "slug":        "anaerobic-respiration-in-humans",
    "title":       "Anaerobic respiration in humans",
    "discipline":  "biology",
    "unit":        "respiration",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # ONE CLAUSE, not the whole bullet. `KS3.B.RESP.03` is split in
    # `ks3_data/substatements.py`; (a) is the human process plus its word
    # summary and is this lesson's, (b) is fermentation and is b8-04's. Full
    # argument, including why the word summary lands with (a), in the docstring.
    "covers":      ["KS3.B.RESP.03a"],
    # Named, used, and owned elsewhere. RESP.01 is aerobic respiration, which
    # this page assumes on every screen and never restates — the hook reveal's
    # "Aerobic respiration has not stopped", the bench's `aerobic` bar, and the
    # second confrontation all lean on b8-01 and b8-02 having happened. RESP.03b
    # is fermentation, named once in rung 1's third correction and pointed at by
    # title. RESP.04 is the full aerobic/anaerobic comparison and is b8-05's;
    # this page states only "far less energy" and hands the number forward.
    "touches":     ["KS3.B.RESP.01", "KS3.B.RESP.03b", "KS3.B.RESP.04"],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 2},
                    {"id": "cells-and-systems", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. `aerobic-respiration` is
    # this unit's L1; `exercise-asthma-and-smoking` is B4's and is live. Both
    # are plain slugs because `requires` takes a slug and resolves it against
    # the registry.
    "requires":    ["aerobic-respiration", "exercise-asthma-and-smoking"],
    "assumes":     [],
    # Design's "Connects to" card, in her order — and the two destinations the
    # resolved lesson codes point at ("What could not be lifted" 1), which are
    # the same two. Both are same-unit slugs.
    "references":  ["fermentation", "aerobic-vs-anaerobic"],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Oxygen debt quantified, ATP yields compared, and the "
                   "liver's conversion of lactate back into glucose.",

    # ── framing ─────────────────────────────────────────────────────────────
    # ⚖️ This sentence is the bench's specification. "The running has finished.
    # Something else has not" is exactly what the demand bar collapsing while
    # the breathing bar holds at 90% shows, and the page asks it before the
    # student can see it answered.
    "big_question": "You finish the sprint, you stop dead, and you go on "
                    "gasping for another two minutes. The running has "
                    "finished. Something else has not.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-equation` is the third: no control
    # of its own, so it mirrors `s-bench` and ticks on the bench's predicate —
    # see the docstring, which supersedes payload schema §7's count. `short`
    # and `label` are Design's own `RAIL_SHORT` and `RAIL` strings (page lines
    # 314–320), `SUMMARY` / "Word summary" included.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "Ten seconds",
         "done_when": "committed"},
        # Design's own threshold, kept: `s.everRecovered` (page line 385), set
        # the first time a recovery step brings lactate to exactly zero.
        # ⚖️ Deliberately NOT "a run has been done" — a student who runs and
        # walks away has seen the borrowing and not the repayment, which is the
        # half of the lesson the title is about. From a flat-out sprint it takes
        # five presses of "Stop and recover 30 s" to get there.
        {"anchor": "s-bench", "short": "BENCH", "label": "Run and stop",
         "done_when": "debt_repaid"},
        {"anchor": "s-equation", "short": "SUMMARY", "label": "Word summary",
         "mirrors": "s-bench", "done_when": "debt_repaid"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key. Option B is the
    # correct one and the reveal says so at once; the hook is not a trick, it is
    # a claim the rest of the page has to earn.
    #
    # ⚖️ The reveal's LAST sentence is what makes this hook elicit RESP-06
    # rather than only answer the question: "Aerobic respiration has not
    # stopped; this is running on top of it." A student who picked B and
    # believed the body had switched over has just been told it did not, and
    # `#s-think` is where that is taken apart properly.
    "phenomenon": {
        "kind": "narrative",
        "title": "A 100 m sprinter barely breathes during the race.",
        "prompt": "Ten seconds, a handful of breaths, and a demand for energy "
                  "perhaps twenty times what sitting in a chair costs. There "
                  "is nowhere near enough oxygen arriving to pay for that, and "
                  "no store of oxygen to draw on. The muscles keep working "
                  "anyway.",
        "commit": "So where is the energy coming from?",
        "options": [
            "Oxygen stored in the muscles beforehand",
            "Breaking glucose down without using oxygen",
            "Burning fat, which needs no oxygen",
            "The heart pumping harder, which supplies the energy",
        ],
        "reveal": "From breaking glucose down without using oxygen at all. It "
                  "is a worse deal — far less energy from each glucose "
                  "molecule, and it leaves lactic acid behind instead of "
                  "finishing the job — but it can be done at speed and without "
                  "waiting for a delivery. Aerobic respiration has not "
                  "stopped; this is running on top of it.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Two, pre-allocated by the commander: RESP-05 and RESP-06, in NOTES-B8
    # §5's own order. Both statements are Design's own quoted beliefs from
    # `#s-think`, which is the best possible register text — they are what the
    # page confronts, in the words it confronts them in.
    #
    # RESP-13 is this lesson's named spare and is PERMANENTLY UNUSED. It is not
    # needed: the two beliefs above are the two the page confronts, and the
    # rung-2 distractor beliefs are distractor beliefs rather than lesson-level
    # misconceptions. Do not re-point it and do not renumber down into it.
    #
    # ⚠️ Both `confronted_by` values name the CONFRONTATION ACTIVITY's id rather
    # than the section anchor. That satisfies both gates at once: the MRB-244
    # check resolves it against `data-activity="two-wrong-ideas"` on the built
    # page, and §10.2's Law 3 check requires at least one `confronted_by` to be
    # an activity id. `s-think` would pass the first and fail the second.
    "misconceptions": [
        # ⚑ NOTES-B8 flag 11 — the DOMS belief. NO `elicited_by`, and the
        # absence is honest rather than an omission (MRB-248 makes absence
        # legal). Nothing on this page asks the student to state this belief:
        # the hook is about where the energy comes from, the bench models
        # supply and lactate and has no timescale beyond 30-second steps, and
        # no rung goes near it. A student arrives holding it from a changing
        # room, and `#s-think` is the first and only place it is named.
        # Inventing an elicit site would be inventing a name.
        {"id": "RESP-05",
         "statement": "Lactic acid is why your legs ache two days after a hard "
                      "session.",
         "confronted_by": "two-wrong-ideas"},
        # ⚖️ ELICITED BY THE HOOK, genuinely. The hook's premise — barely
        # breathing, no oxygen arriving, the muscles working anyway — is exactly
        # where a student forms "so it switched over to the other kind", and
        # Design answers it in the reveal's last sentence before taking it apart
        # in `#s-think`. `s-hook` is emitted as `id="s-hook"` on the built page.
        {"id": "RESP-06",
         "statement": "When you sprint, you switch from aerobic to anaerobic "
                      "respiration.",
         "elicited_by": "s-hook",
         "confronted_by": "two-wrong-ideas"},
    ],

    # Design draws no keyword block anywhere in B8, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its
    # exclusion list. Every definition below is authored, not lifted.
    #
    # ⚖️ `aerobic respiration` is deliberately NOT re-declared — b8-01 owns it
    # and this page cites it rather than restating it, which is the register's
    # standing rule. `lactate` IS declared, because the Going further layer uses
    # it four times ("blood lactate", "the lactate concentration") beside "lactic
    # acid" in the body, and a student who does not know they name the same
    # thing reads that paragraph as being about something new.
    "vocabulary": [
        {"term": "anaerobic respiration",
         "definition": "Breaking glucose down to release energy without using "
                       "oxygen.",
         "note": "In human muscle the only product is lactic acid — no carbon "
                 "dioxide and no water."},
        {"term": "lactic acid",
         "definition": "What is left when glucose is broken down without "
                       "oxygen. It builds up in a working muscle.",
         "note": "It causes the burning during the effort, not the ache two "
                 "days later."},
        {"term": "oxygen debt",
         "definition": "The oxygen a body still owes after the exercise has "
                       "stopped, needed to deal with the lactic acid that "
                       "built up.",
         "note": "It is why you go on breathing hard while standing still."},
        {"term": "lactate",
         "definition": "The form lactic acid takes in the blood, and the word "
                       "used when it is measured.",
         "note": None},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED, NOT ASSUMED. Grepped on this page: `<img>`,
    # `<figure>` and `<picture>` each appear ZERO times. The only SVG on it is
    # UI furniture — the nav chevron, the rail tick, the drawn equation arrow,
    # the endmatter link arrows and the ladder tick and cross marks — and the
    # page leaves no placeholder, no empty frame and no caption with nothing
    # under it. §4.10 allows an empty `figures` for a lesson carried by its
    # interactives. NOTES-B8 flag 21 names a mitochondrion and a labelled
    # leaf-and-lung gas-flow figure as the unit's obvious candidates and records
    # that neither is in `docs/ks3/diagram-manifest.md`. That flag is NOT
    # dropped by this pass — it is Mide's to rule on — and inventing a slot here
    # to fill the gap would be a component nobody drew (MRB-205).
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b8/__init__.py::_normalise, which leaves the `practical`
        # shell behind it.
        #
        # ⚠️ SHELL MEASURED, NOT GUESSED: page line 105 is
        # `ks3-block ks3-dark ks3-practical`, so `segment` is `practical` —
        # the ink-dark ground. Contract §4 records that B1 got two of six wrong
        # by inferring the shell from the kind name.
        #
        # ⚠️ THIS INSTRUMENT IS ON INK. `.ks3-dark p` is (0,1,1) and beats a
        # bare instrument class at (0,1,0). Gated since MRB-245 by
        # `ks3_parity.check_dark_text_specificity()`, and recorded here because
        # this payload is what feeds it.
        #
        # ⛔ NO RUNTIME STATE. See the docstring: `supply`, `lactate`,
        # `seconds`, `phase` and `ever_recovered` are the runtime's.
        {"type": "oxygen-debt", "id": "run-it-then-stop",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · supply against demand",
         "heading": "Run it, then stop and watch",
         "prompt": "The interesting part is not the running — it is what "
                   "the breathing bar does after you stop.",

         "options_label": "Pace",
         "paces": PACES,
         # Design's `startPace` default, and it is NOT `paces[0]` — the bench
         # opens on the flat-out sprint, which is the only pace that makes the
         # gap open on the first press. A renderer that opened on the first tab
         # would open on walking, where nothing happens.
         "start": "sprint",

         "model": MODEL,
         "bars": BARS,

         # The mono clock beside the heading (page line 486) and the two
         # non-running phase labels (page line 491). The RUNNING phase label is
         # the current pace's own `label`, so there is no key for it.
         "clock":  {"zero": "on the start line", "suffix": " s",
                    "recovering": " · recovering"},
         "phases": {"ready": "Standing on the line",
                    "recovering": "Stopped — recovering"},
         # The amber line at the top right of the panel (page line 492). `{n}`
         # is the gap in units. ⚖️ "borrowed" and "repaying" are the debt
         # metaphor doing the work the whole lesson is built on; they are not
         # interchangeable with "shortfall" and "recovering".
         "shortfall": {"aerobic": "fully aerobic", "repaying": "repaying",
                       "borrowed": "{n} units borrowed per 10 s"},

         "notes": NOTES,

         "run_label": "Run for 10 s", "running_label": "Keep going, 10 s",
         "stop_label": "Stop and recover 30 s",
         "recovering_label": "Recover another 30 s",
         "reset_label": "Back to the start line"},

        # #s-equation — the word summary. Shell MEASURED as `rule`: page line
        # 152 is a bare `<section>` with `background: var(--ks3-band)` and
        # `border: 3px solid var(--ks3-ink)`, which is `.ks3-rule` and not
        # `.ks3-block`. Payload schema §0 rule 2's table says the same.
        # Rail stop 3, mirroring `s-bench` — see the docstring.
        {"type": "rule", "anchor": "s-equation",
         "eyebrow": "The word summary",
         "statement": "One reactant. One product. An unfinished job.",

         # ⚠️ THE ARROW IS NOT A CHARACTER. `arrow` holds the WORD the drawn
         # arrow means and is the component's accessible name; `r_equation`
         # raises on a typed U+2192, because the design system's fonts have no
         # glyph for it and a typed one drops to a system font mid-line. Design
         # draws it as an SVG on this page too (line 158), with the same
         # geometry b7-01 measured.
         #
         # ⚖️ "gives" is the word the page itself uses everywhere the summary is
         # spoken — the key fact ("glucose giving lactic acid"), the key note
         # ("glucose gives lactic acid") and all four options of rung 1. One
         # authored word, four places.
         #
         # `condition` is Design's full-width mono line beneath the row (page
         # line 160). It is doing real teaching: it is the only place that says
         # what is ABSENT from the right-hand side, which is what makes this an
         # unfinished job rather than a different reaction.
         "equation": {
             "reactants": "glucose",
             "arrow":     "gives",
             "products":  "lactic acid",
             "condition": "no oxygen used · far less energy transferred · no "
                          "carbon dioxide, no water",
         },

         "cards": FACT_CARDS,

         # Design nests the key fact inside this section (page lines 173–176) on
         # the CARD ground with the shipped stylesheet's own 5px 5px accent
         # shadow. `r_rule` takes a nested key fact, so it stays where she drew
         # it — "What could not be lifted" 3.
         "key_fact": {"ref": "the-debt-is-why-you-keep-breathing",
                      "ground": "card"}},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "RESP-05"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # `card`, because it is nested inside a band panel and band on band is
    # invisible. Never amber (MRB-208). Byte-identical to page line 175 and to
    # payload schema §9's b8-03 entry.
    "key_facts": [
        {"id": "the-debt-is-why-you-keep-breathing",
         "text": "In humans, anaerobic respiration is glucose giving lactic "
                 "acid, with no oxygen used and far less energy transferred. "
                 "The lactic acid builds up, and the oxygen needed to deal "
                 "with it afterwards is the oxygen debt — which is why you "
                 "keep breathing hard after you stop.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider (page line 187, `border-top: 2px solid
        # var(--ks3-alert-border)`) — `r_confrontation` renders exactly that
        # from `statements[]`.
        #
        # MEASURED AS STATIC, so this is a `confrontation` and NOT a `predict`:
        # `#s-think` is `ks3-block ks3-misconception` and contains a quote, a
        # paragraph, a rule, a second quote and a second paragraph. No options
        # list, no reveal, no button, no state. Contract R1's `predict` branch
        # applies where `#s-think` asks for a commitment and then reveals; this
        # page does not, so it stays a confrontation — the same rule meeting a
        # different block, as in B1, B4, B5 and B7. It is not a rail stop on any
        # B8 page, so emitting no `data-stage-done` costs nothing.
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "RESP-05",
         "statements": [
             # ⚑ NOTES-B8 flag 11 — THE ONE DESIGN SAYS GENERATES A STAFFROOM
             # CONVERSATION, and it is correct. Authored plainly, in the body,
             # with no hedge and nothing later that walks it back. Full
             # reasoning in the docstring under flag 11.
             #
             # ⚠️ Two typographic details are Design's own and are preserved:
             # `<em>during</em>` (inside `rich()`'s allowance) and the ASCII
             # double quotes around "flushing lactic acid out", which are what
             # her markup carries.
             {"quote": "“Lactic acid is why your legs ache two days after a "
                       "hard session.”",
              "body": ["This one is repeated by coaches, in gyms and in a good "
                       "many textbooks, and it does not survive a measurement. "
                       "Blood lactate is back to its resting level within "
                       "about an hour of stopping — usually much less — and "
                       "the ache people are describing peaks a day or two "
                       "later, when there is no lactate left to blame. That "
                       "delayed soreness comes from microscopic damage to the "
                       "muscle fibres and the inflammation that repairs it, "
                       "which is why it follows unfamiliar or downhill work "
                       "most strongly, and why it fades as you get used to the "
                       "exercise. Lactic acid is real, it is genuinely "
                       "responsible for the burning you feel <em>during</em> "
                       "the effort and for making you slow down, and its job "
                       "ends when you stop. Keeping the two apart matters, "
                       "because the myth sells a lot of stretching and massage "
                       "as a way of \"flushing lactic acid out\" of muscles "
                       "that cleared it before you got home."]},
             # RESP-06. ⚖️ This paragraph CITES THE BENCH BY WHAT IT DOES —
             # "the oxygen delivery bar does not drop when the demand bar
             # rises" — which is only true because `supply_step` is 18
             # regardless of pace. The confrontation and the instrument are one
             # argument; changing the model here breaks a sentence there.
             {"quote": "“When you sprint, you switch from aerobic to anaerobic "
                       "respiration.”",
              "body": ["Nothing switches. Aerobic respiration carries on at "
                       "the highest rate the oxygen supply allows, all the way "
                       "through the sprint, and anaerobic respiration makes up "
                       "the shortfall on top of it. Watch the bench above: the "
                       "oxygen delivery bar does not drop when the demand bar "
                       "rises — it climbs as fast as your heart and lungs can "
                       "push it, and the gap between the two is the part being "
                       "paid for anaerobically. This is why the same activity "
                       "can be aerobic for a trained runner and anaerobic for "
                       "an untrained one: the demand is the same and the "
                       "supply is not. It also explains pacing. A runner who "
                       "chooses a speed just below the point where the gap "
                       "opens can hold it for an hour; one who goes above it "
                       "is borrowing, and the debt is called in whether they "
                       "like it or not."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RULED 17 Aug 2026. Rung 1 is CLEAN and untouched
    # (the correct answer is the SHORTEST, 4w against 6 / 6 / 6, which is the
    # inverse of a tell and is not gated). Rung 2 failed on both arms — 23w
    # against 11, clearing the field by 12 words and by a ratio of 2.1 — and its
    # three distractors are rewritten as WRONG RULES in the correct answer's own
    # shape. Correct option, `answer: 1`, option order and all three corrections
    # are unchanged and byte-identical. 23w against 20 / 22 / 22 after. Full
    # working in the docstring.
    "ladder": {
        # ⚖️ THE RUNG THE STATUTORY CLAUSE TURNS ON. `KS3.B.RESP.03a` names "a
        # word summary for it" and this is where the student produces it. All
        # three distractors are the three summaries a student writes when they
        # have half the idea: one that keeps the oxygen, one that borrows
        # b8-04's products, and one that finishes the job aerobically. Nothing
        # in this rung was touched.
        "recall": {
            "title": "Rung 1 · The summary",
            "q": "What is the word summary for anaerobic respiration in "
                 "humans?",
            "options": [
                "glucose gives lactic acid",
                "glucose + oxygen gives lactic acid",
                "glucose gives carbon dioxide + alcohol",
                "glucose gives carbon dioxide + water",
            ],
            "answer": 0,
            "feedback": {
                1: "Anaerobic means without oxygen. If oxygen were available "
                   "the cell would use it — it gets far more energy that way.",
                # ⚠️ "b8-04’s subject" resolved to the lesson TITLE — "What
                # could not be lifted" 1. Every science word is unchanged and
                # the destination is a `references` edge.
                2: "That is what yeast does, and it is the subject of "
                   "Fermentation and what we use it for. Human muscle produces "
                   "lactic acid, not alcohol.",
                3: "Those are the products of the complete, aerobic breakdown. "
                   "Without oxygen the job is left half done.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "You finish a sprint and stand still, yet you go on breathing "
                 "hard for two minutes. Why?",
            # ⊕ MRB-177, 17 Aug 2026. Options 0, 2 and 3 rewritten as wrong
            # RULES in the correct answer's shape — what is happening, and what
            # follows from it. Option 1 and `answer` are Design's, unchanged.
            "options": [
                # 20w — mechanical momentum, given its consequence. Was "Your
                # lungs take time to slow down after being worked hard" (11w).
                # Design's clause is kept verbatim at the front.
                "Your lungs take time to slow down after being worked hard, so "
                "the breathing runs on under its own momentum",
                # 23w — Design's, unchanged.
                "You are taking in the oxygen you could not get during the "
                "sprint, to deal with the lactic acid — the oxygen debt",
                # 22w — the muscles-still-consuming belief, now stated as a
                # rule that survives the stopping. Was "Your muscles are still
                # working, so they still need oxygen" (10w).
                "Your muscles are still working after you stop, so they go on "
                "needing oxygen at the same rate as during the sprint",
                # 22w — breathing as thermoregulation. Was "You are cooling
                # down, and breathing out is how heat leaves" (11w).
                "You are cooling down, and breathing out is how the extra heat "
                "leaves, so the rate stays up until you have cooled",
            ],
            "answer": 1,
            # All three unchanged from Design, and each still answers exactly
            # the belief its rewritten distractor states — which is the test of
            # whether the rewrite changed what the question measures. Two of the
            # three now land harder; see the docstring.
            "feedback": {
                0: "Breathing rate is controlled by what is in your blood, not "
                   "by momentum. Something is still being demanded.",
                2: "You are standing still. The muscles are not contracting, "
                   "and the breathing is not for them.",
                3: "A little heat does leave that way, but it is not what sets "
                   "your breathing rate. The trigger is chemical.",
            }},
        # ⚖️ Criterion 4 is RESP-06 written as a marking point, and it is the
        # one a student most often leaves out: the two happen TOGETHER. Without
        # it the answer describes a switch, which is the belief `#s-think`
        # spends a paragraph killing.
        "explain": {
            "title": "Rung 3 · Explain the debt",
            "q": "Explain, from the moment a sprint starts to two minutes "
                 "after it finishes, why anaerobic respiration happens and "
                 "what the oxygen debt is.",
            "field_label": "Your explanation",
            "placeholder": "When the sprint starts, the muscles…",
            "success": [
                "Says the muscles suddenly need energy much faster than "
                "before.",
                "Says the heart and lungs cannot deliver oxygen fast enough to "
                "supply all of it aerobically.",
                "Says the shortfall is made up by anaerobic respiration, which "
                "produces lactic acid.",
                "Says aerobic respiration continues throughout at the highest "
                "rate the oxygen supply allows — the two happen together.",
                "Says the deep breathing afterwards supplies the oxygen needed "
                "to deal with the lactic acid, and names this the oxygen debt.",
            ]},
        # The bench's own contrast — "the same activity can be aerobic for a
        # trained runner and anaerobic for an untrained one" — turned into a
        # measurement problem. Criteria 3 to 5 are the fair-test half and are
        # why `ws` carries the experimental-skills strand.
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "Two students run the same distance at the same speed. One "
                 "is back to normal breathing in 40 seconds, the other "
                 "takes three minutes. Explain what that difference shows, "
                 "and design a fair test to compare one person’s recovery "
                 "before and after six weeks of training.",
            "field_label": "Your answer",
            "placeholder": "The student who recovers faster…",
            "success": [
                "Says the fitter student delivered more oxygen during the run, "
                "so less of the energy came from anaerobic respiration.",
                "Says that student therefore built up less lactic acid and has "
                "a smaller oxygen debt to repay.",
                "Designs a test where everyone does the same exercise for the "
                "same time or distance.",
                "Says recovery time is measured the same way for everyone — "
                "for example, time for pulse rate to return to its resting "
                "value.",
                "Identifies something that must be controlled or accounted "
                "for, such as measuring each person’s resting rate first, or "
                "the fact that people start at different fitness levels.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # ⚠️ Speaks the arrow as the word "gives", which is the same word the drawn
    # equation carries as its accessible name.
    "key_note": "When muscles need energy faster than oxygen can be delivered, "
                "they also respire anaerobically: glucose gives lactic acid, "
                "releasing far less energy and using no oxygen. Lactic acid "
                "builds up and causes the burning that forces you to slow "
                "down. Afterwards you keep breathing hard to repay the oxygen "
                "debt, and the liver deals with the lactic acid.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B8 flags 13 and 14 both live in this paragraph and both are
    # CHECKED AND LEFT — the liver's two routes (the Cori cycle, deliberately
    # unnamed) and the lactate-threshold claim. Full reasoning in the docstring.
    #
    # ⚖️ MRB-225 holds across the whole layer: it adds the "how do we know?"
    # story — a pinprick, a treadmill, a threshold that moves with training —
    # and retracts nothing said above it. The body says the liver deals with the
    # lactic acid; this says how, and what happens to it. Nothing is taken back.
    "stretch": [
        {"type": "explainer", "id": "what-the-liver-does-with-it",
         "text": "The lactic acid does not stay in the muscle. It is carried "
                 "away in the blood to the liver, and the liver has two "
                 "options: oxidise it completely, using some of the oxygen you "
                 "are gasping for, or spend energy converting it back into "
                 "glucose and returning it to the muscles. Nothing is thrown "
                 "away, which is why the whole episode is a loan rather than a "
                 "loss. Sports scientists take this seriously enough to "
                 "measure it directly — a pinprick of blood during a treadmill "
                 "test gives the lactate concentration, and the pace at which "
                 "it starts to climb is one of the best single predictors of "
                 "endurance performance there is. Training moves that "
                 "threshold: the same runner, six months later, can hold a "
                 "faster pace before the gap between demand and supply opens "
                 "at all."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own flagship, which is a real destination
    # on the page it is printed on (§4.8.1 C) — and the right one: pacing is
    # what the bench lets a student try, by running the same ten seconds at four
    # different demands and watching which of them opens a gap.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to work out why pacing beats sprinting from the "
                      "gun?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph and nothing in it is a safety instruction — it
    # declares how far the bench's model can be trusted. Routing it through
    # `safety_note` would print it in the treatment reserved for "never light a
    # candle without an adult", which devalues the safety line. b3-05, b3-07,
    # b4-01, b5-06, b7-01 and b7-04 resolve the identical foot line the
    # identical way.
    #
    # ⚑ NOTES-B8 flag 12, CHECKED: six declarations for six simplifications —
    # arbitrary units, a fixed ceiling, lactate as one accumulating quantity,
    # several real fuel systems, continuous production and clearance, and
    # individual variation — plus the ten-second step declared as a reading
    # device rather than a measured timescale. Nothing in the model is
    # undeclared. The EPOC half of flag 12 is not in this line and is not added;
    # see the docstring.
    "convention_note": "The bench is a teaching model in arbitrary units. "
                       "Oxygen delivery is shown rising towards a fixed "
                       "ceiling and lactic acid as a single accumulating "
                       "quantity; real physiology involves several fuel "
                       "systems, a lactate level that is produced and cleared "
                       "continuously, and large differences between "
                       "individuals. The ten-second steps are for reading the "
                       "bars, not a measured timescale.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # Rung 4 asks for a fair test with a controlled exercise, an identically
    # measured recovery and a named confounder, which is the skills strand. The
    # bench is a model whose four readouts have to be read against each other —
    # and the `#s-think` DOMS paragraph is a widely repeated claim that does not
    # survive a measurement, which is the attitudes strand rather than the
    # analysis one.
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation",
           "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
