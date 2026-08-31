"""C3 L7 — Proving something is pure (INVESTIGATION).

Authored against Design's approved page,
`docs/ks3/design-reference/c3/c3-07-proving-something-is-pure.dc.html`
(704 lines), and Design's unit notes, `docs/ks3/design-reference/c3/NOTES-C3.md`
§2, §3.4, §4 flags 14–15, §5 and §6.

Every student-facing string is byte-identical to the approved page except the
four repairs listed under "Where the prose and the bench disagreed" below.
`RAIL`, `CRITIQUES`, `SAMPLES`, `RUNGS` and `SELF_RUNGS` were taken from the
extracted constants dump rather than retyped; the dial labels, the run-button
labels, the four data notes, the three verdicts, the table headings, the think
options and both reveal paragraphs live inside `lessonVals(s)` on the page and
were lifted from lines 425–600, which is where roughly half this lesson's words
are and where a constants-only lift loses them.

── The lesson turns the unit's toolkit back on itself ───────────────────

NOTES §2: L1–L6 build a separation toolkit; L7 asks what would make a claim of
purity stand up, and the answer is a measurement with a known expected value.
That is why the flagship is not another separation but a melting point, and why
`MIX-02` — *if it looks the same all the way through, it is pure* — is
confronted here for the THIRD time in the unit (the gold ring in c3-01, the
clear filtrate in c3-03, the melting range here). Repeating a misconception
across lessons is deliberate; it is the unit's spine, not duplication.

── Critique before construct (NOTES §6) ────────────────────────────────

Somebody else's four-step plan is ruled on BEFORE the student meets any data.
None of the four steps can settle it, and the closing panel names why: they are
observations, and not one of them is a measurement with an expected value to
compare against. The student then builds the thing the plan was missing.

⚠️ R3 holds on `#s-critique`. Each step opens the SAME verdict whichever
button was pressed — the two buttons record a commitment and mark nothing.

── The heating-rate dial is what makes the bench an instrument ─────────

NOTES §3.4: `melting-point-bench` is the kind to reuse for any "repeats and
anomalies" lesson, and "the heating-rate dial is what turns it from a data
table into a Working Scientifically instrument". Both dials are load-bearing
and neither may be defaulted away:

  * heat FAST and the thermometer lags the sample. Design models it as 55% of
    the true range collapsed and +1.5 °C on the end point (`fast_model` below),
    so every reading reads high and every batch drifts towards the same
    middling range — the impure batch stops standing out.
  * run ONCE and batch 3's anomaly is invisible: a single reading cannot be
    checked against anything, which is exactly `MIX-13`.

⚠️ THE ANOMALY IS REPORTED, NOT DELETED. Batch 3's second run disagrees with
its other two. Rung 3 and the think-again reveal both say it is reported,
explained and set aside — never silently dropped and never averaged in. That is
the Working Scientifically point of the whole lesson and it must not be softened
into "ignore the odd one".

── Where the prose and the bench disagreed (brief §6) ──────────────────

The bench is the measurement and the prose changes. Four repairs, all reported,
none of them a change to a number the instrument computes:

1. The fast/one-run note said "every range came out narrower than it really is".
   It does not: `0.45R + 1.5` INFLATES a sharp melt (batch 1's 0.5 °C becomes
   1.7 °C) and compresses a wide one (batch 2's 7 °C becomes 4.65 °C). The note
   now says what the bench does — every start reads high, and the ranges are
   dragged towards each other until the gap that gives batch 2 away is about
   three degrees instead of six and a half.
2. The same clause in the fast/three-run note ("the ranges are all squashed")
   was repaired the same way, and its first and last sentences are untouched.
3. The think-again reveal said a single fast run "can produce exactly the answer
   you were hoping for". On this bench it does not — fast, batch 2 still melts
   over 4.65 °C, starting more than four degrees low. Shrunk to the claim the
   bench supports: a fast run flatters an impure sample and closes much of the
   gap. (Prose bar §7: overstated claims shrink.)
4. Rung 3 quoted batch 3 as "two runs gave 52–53 °C". The two runs that agree
   are 52.0–53.0 °C and 52.5–53.5 °C, so the second is now quoted as well. The
   criteria are unchanged, and the anomalous run is quoted exactly as the bench
   computes it.

⚑ For Mide's science gate, from Design's NOTES §4:
  * flag 14 — the sample is NAMELESS. Design's page never names it at all (not
    even "compound P"), and it is kept that way: a named substance invites a
    student to look up its melting point and skip the reasoning, and the
    evidence here is the RANGE, not the identity. The numbers are internally
    consistent in both directions everywhere they appear — pure melts sharply
    (batch 1, within a degree, at the expected 53 °C), impure melts LOWER and
    OVER A RANGE (batch 2, six or seven degrees, starting around 45 °C).
  * flag 15 — fast heating reading high and compressing a wide range is real
    (thermometer lag) and is kept as modelled. The four data notes now agree
    with what `fast_model` actually computes; see repairs 1–3 above.
  * Rung 2 — a SHARP melt at 61 °C when 53 °C was expected is a pure substance
    that is not the one you ordered. That is the lesson's hardest idea and the
    one an examiner should look at first.
"""

# ── #s-critique · somebody else's plan, four steps ──────────────────────
#
# Page lines 376–389, byte-identical. `answer` is the ruling and `why` is the
# reasoning behind it; neither is keyed to which button the student pressed.
# Step 3 is the honest one — "Useful, and not enough" — and it is why the
# closing panel says none of the four is useless.
CRITIQUES = [
    {"id": "q1",
     "step": '"Look at the powder under a hand lens and check the crystals '
             'all look the same."',
     "answer": "Tells you nothing about purity.",
     "why": "Two white powders ground together look like one white powder, "
            "and a single substance can crystallise in more than one shape. "
            "Uniform appearance is exactly the evidence that has failed in "
            "every lesson of this unit."},
    {"id": "q2",
     "step": '"Taste a little of it and see if it tastes of anything else."',
     "answer": "Never done, and it would not settle it anyway.",
     # The safety sentences are Mide's, approved 28 Aug 2026, and reproduced
     # VERBATIM. Do not reword them. The final clause is kept from the
     # original because it is the SCIENCE half of the answer — the step's own
     # verdict is "Never done, and it would not settle it anyway", and
     # without it the second half of that verdict is unsupported.
     "why": "Never taste anything in a laboratory. Not a drop, not a "
            "crystal, not even something you are sure you recognise — an "
            "unknown white powder is exactly the thing that can poison you. "
            "In a kitchen, tasting is how you check your food. In here, it "
            "is how you get hurt. Even if it were safe, most impurities are "
            "tasteless at a few per cent."},
    {"id": "q3",
     "step": '"Stir some into water and check that it all dissolves."',
     "answer": "Useful, and not enough.",
     "why": "It would catch an impurity that does not dissolve — sand mixed "
            "into salt would leave a residue. It catches nothing that "
            "dissolves, and most things that get mixed into a powder do "
            "dissolve."},
    {"id": "q4",
     "step": '"Weigh 10 g of it and check that it weighs 10 g."',
     "answer": "Measures the balance, not the powder.",
     "why": "Mass tells you how much you have, never what it is. A mixture "
            "weighs whatever a mixture weighs. There is no expected value to "
            "compare it against, which is what makes it useless here."},
]

# ── #s-bench · the three batches, measured slowly ───────────────────────
#
# Page lines 391–398, byte-identical. These are the TRUE ranges — what a
# thermometer that keeps up would record. `fast_model` on the block derives the
# fast readings from them; nothing here is a fast reading.
#
# ⚖️ The three batches are constructed to be read, not measured off a real
# substance (NOTES flag 14), and they point the same way everywhere:
#   batch 1  0.5–1.0 °C, ending at the expected 53 °C     → pure
#   batch 2  6.5–7.0 °C, starting eight degrees low       → impure
#   batch 3  two runs like batch 1, one that agrees with  → pure, with one
#            neither                                        anomalous run
SAMPLES = [
    {"id": "b1", "name": "Batch 1",
     "runs": [{"start": 52.5, "end": 53.0},
              {"start": 52.5, "end": 53.5},
              {"start": 53.0, "end": 53.5}]},
    {"id": "b2", "name": "Batch 2",
     "runs": [{"start": 45.0, "end": 52.0},
              {"start": 44.0, "end": 51.0},
              {"start": 46.0, "end": 52.5}]},
    {"id": "b3", "name": "Batch 3",
     "runs": [{"start": 52.0, "end": 53.0},
              {"start": 47.5, "end": 52.0},
              {"start": 52.5, "end": 53.5}]},
]

# The bench's own reading of its data, one note per setting. Read by
# `melting-point-bench` after a run; the pair (`rate`, `repeats`) selects one.
#
# ⚠️ Every number in these four notes is one the BENCH computes. See the module
# docstring, repairs 1 and 2: the two fast notes used to claim the ranges came
# out narrower, which is true of batch 2 and false of batches 1 and 3.
BENCH_NOTES = [
    {"rate": "slow", "repeats": 3,
     "text": "Three runs each, heated slowly. Batch 1 melts within a degree, "
             "every time. Batch 2 melts over six or seven degrees and starts "
             "around 45 °C, well below the expected 53 °C. Batch 3 agrees "
             "with batch 1 twice and disagrees with itself once — which is "
             "what an anomalous result looks like when you have bothered to "
             "repeat."},
    {"rate": "slow", "repeats": 1,
     "text": "One run each, heated slowly. Batch 2 stands out — a range of "
             "seven degrees, starting eight degrees low. But with one reading "
             "each you cannot tell a real difference from a bad run, and "
             "batch 3 looks fine on a single measurement that you have no way "
             "of checking."},
    {"rate": "fast", "repeats": 3,
     "text": "Three runs each, heated fast. The repeats agree with each "
             "other, which is reassuring and misleading: they agree because "
             "the same error happened three times. Batch 2 is still visibly "
             "worse than the others, but every start has been dragged up and "
             "every range has been dragged towards the same middling value — "
             "batch 2's seven degrees down to under five, batch 1's half a "
             "degree up to nearly two. Slow the block down and run it again."},
    {"rate": "fast", "repeats": 1,
     "text": "One run each, heated fast. The thermometer cannot keep up with "
             "a fast block, so every start reads high, batch 2's "
             "seven-degree range collapses to under five, and a sharp melt "
             "smears out to nearly two. The gap that gives an impure batch "
             "away has shrunk to about three degrees, on one reading you have "
             "no way of checking. This table cannot answer the question, and "
             "nothing about looking at it harder will fix that."},
]

# The verdict panel, page lines 579–589. `text` is the whole reply for batches
# 1 and 3; batch 2's reply is `text` followed by ONE of `text_trusted` /
# `text_untrusted`, because whether the accusation can be made at all depends
# on how the data was collected — slow, and more than once.
#
# ⚠️ Not a marking. The panel opens on whichever batch was chosen and says what
# that batch's data shows; the ladder is the only place correctness is marked.
BENCH_VERDICTS = [
    {"id": "b1",
     "title": "Batch 1 is the clean one — look at its range.",
     "text": "Batch 1 melts within a degree on every run. That is the "
             "signature of a pure substance, and it is your reference for "
             "what the other two should look like. Batch 2 is the one that "
             "melts over six or seven degrees."},
    {"id": "b2",
     "title": "Batch 2. A range of six or seven degrees, starting eight "
              "degrees low.",
     "text": "Something else is dissolved in it, interrupting the "
             "arrangement, so it starts giving way early and finishes late.",
     "text_trusted": "Your data can carry that claim: three slow runs, "
                     "agreeing with each other, on all three batches.",
     "text_untrusted": "Your data points the right way but cannot carry the "
                       "claim — heated fast, or run once, the ranges are not "
                       "trustworthy. Run it slowly, three times, before you "
                       "accuse a supplier of anything."},
    {"id": "b3",
     "title": "Batch 3 is pure. Its odd run is an anomaly, not evidence.",
     "text": "Two of batch 3's runs melt within a degree, at the expected "
             "temperature. The third disagrees with both — one anomalous run, "
             "most likely a loosely packed tube. Set it aside with a reason "
             "written down and batch 3 is pure. The impure batch is batch 2."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 204 character for character.
    "slug":        "proving-something-is-pure",
    "title":       "Proving something is pure",
    "discipline":  "chemistry",
    "unit":        "mixtures-and-separation",
    "family":      "INVESTIGATION",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚖️ `covers` is SUBJECT content here, not a WS statement, which is the
    # opposite of c1-06's resolution and is right for the opposite reason.
    # §5.7.1 puts an INVESTIGATION lesson on a WS statement when it teaches no
    # new subject content; this one owns `KS3.C.PIS.05` — *the identification
    # of pure substances* — and NOTES §1 gives it no other owner in the unit.
    # Moving it to WS would leave the fifth PIS statement uncovered.
    "covers":      ["KS3.C.PIS.05"],
    "touches":     ["KS3.C.PIS.01", "KS3.WS.ATT.01", "KS3.WS.EXP.05",
                    "KS3.WS.ANA.05"],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 2},
                    {"id": "particles", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's endmatter draws ONE prerequisite (page line 339) and ONE forward
    # link (line 345), and both are kept as drawn.
    "requires":    ["chromatography"],
    "assumes":     [],
    # ⚠️ The forward link LEAVES the unit — c3-07 is the last lesson in C3 and
    # c4-01 is the first in C4 — and Design's card is nonetheless headed "Next
    # in this unit" (page line 343). c1-06 met the same case and resolved it
    # the other way, with "Next unit". Design's string is kept here because it
    # is the delivered page and the heading is student-facing; the unit-wide
    # choice between the two is the commander's, not this lesson's. Flagged in
    # the build report.
    "references":  [{"unit": "C4", "lesson": "chemical-vs-physical-change"}],
    "connects_heading": "Next in this unit",
    # ⊖ Empty so `ks4_becomes` can render Design's authored prose (page line
    # 350). §4.8.1 D makes the two mutually exclusive.
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Someone hands you a white powder and tells you it is "
                    "pure. Believing them is not chemistry — so what "
                    "measurement would make them prove it?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops (NOTES §6), and the predicates are Design's own `DONE()`
    # (page lines 444–451).
    "rail": [
        {"anchor": "s-hook",     "short": "HOOK",     "label": "Three bags",
         "done_when": "committed"},
        {"anchor": "s-critique", "short": "CRITIQUE",
         "label": "Judge the plan", "done_when": "all_steps_ruled"},
        {"anchor": "s-bench",    "short": "DATA",
         "label": "Melting points", "done_when": "verdict_given"},
        {"anchor": "s-think",    "short": "THINK",    "label": "One reading",
         "done_when": "committed"},
        {"anchor": "s-ladder",   "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Ink-dark `.ks3-block.ks3-dark.ks3-hook` (page line 81). `kind` is
    # authored on every KS3 lesson and dispatched on by nothing; Design draws
    # no media here, so there is none.
    "phenomenon": {
        "kind": "narrative",
        "title": "Three bags of white powder. All three labelled pure. One of "
                 "them is not.",
        "prompt": "A supplier has sent three batches of the same white solid, "
                  "all sold as pure. Somewhere in the delivery, one batch has "
                  "something else mixed into it. Every bag looks identical, "
                  "and the label is not evidence.",
        "commit": "You can make one measurement on each. Which measurement "
                  "would settle it?",
        "options": [
            "Weigh a spoonful of each",
            "Check whether each one dissolves in water",
            "Measure the temperature at which each one melts",
            "Look at all three under a microscope",
        ],
        "reveal": "The melting point. A pure substance melts at one "
                  "temperature — sharply, within a degree. A mixture melts "
                  "over a <strong>range</strong>, and it starts melting "
                  "<strong>lower</strong> than the pure substance would. That "
                  "difference is measurable with a thermometer, and it does "
                  "not care what the bag says.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # NOTES §5. MIX-02 is the unit's spine and this is its THIRD and last
    # confrontation — by the melting RANGE, after the gold ring in c3-01 and
    # the clear filtrate in c3-03. Authoring it again here is deliberate.
    "misconceptions": [
        {"id": "MIX-02",
         "statement": "If it looks the same all the way through, it is pure.",
         "elicited_by": "student-plan",
         "confronted_by": "melting-points"},
        {"id": "MIX-13",
         "statement": "One measurement is enough if it is the right answer.",
         "elicited_by": "think-commit-one-run",
         "confronted_by": "melting-points"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # ── #s-critique · critique before construct (NOTES §6) ─────────────
        # Light `.ks3-block` (page line 105) → the `check` shell.
        #
        # ⚠️ A DISTINCT KIND FROM B1's `critique-steps`, and not a rename of
        # it. B1's is a checkbox set — "find all the faults", any number of
        # steps picked, one reveal for the lot. This one takes a two-way
        # ruling on EACH step, locks that step, and opens that step's own
        # verdict. `ks3_art.load()` raises on a family registered in two unit
        # modules, so reusing the name would also collide with `ks3_art/b1.py`.
        {"type": "plan-critique", "id": "student-plan", "anchor": "s-critique",
         "demand": "evaluate",
         "targets": "MIX-02",
         "eyebrow": "Before you plan · judge someone else's method",
         "heading": "A student has written a plan. Four steps. Rule on each "
                    "one.",
         "prompt": "For each step, decide whether it could settle whether the "
                   "powder is pure — before you read what it is actually "
                   "worth.",
         # ⚖️ R3: the SAME verdict opens whichever button was pressed. The
         # buttons record a commitment; nothing here marks it, and the two
         # labels are deliberately not "right" and "wrong".
         "options": [{"id": "settles", "label": "Could settle it"},
                     {"id": "nothing", "label": "Cannot settle it"}],
         "steps": CRITIQUES,
         # Shown once all four are ruled on. This is the sentence the whole
         # section exists for, and it is what the bench then builds.
         "closing": "Four steps, none of them useless, and not one of them "
                    "able to answer the question. The plan is not lazy — it "
                    "is a plan built out of observations rather than out of a "
                    "<strong>measurement with a known expected value</strong>. "
                    "That is the difference you are about to build."},

        # ── #s-bench · the melting point bench (NOTES §3.4) ────────────────
        # Light `.ks3-block` (page line 136) → the `check` shell. DOM only;
        # there is no canvas anywhere in C3.
        #
        # ⚠️ NO GATE, and that is not an omission: the two dials ARE the
        # commitment. The student decides how to measure before there is
        # anything to see, which is the whole difference between this and a
        # data table.
        #
        # ⚖️ `fast_model` IS THE SCIENCE and it is authored here rather than
        # hard-coded in the drawer, because it is the number Mide's gate is
        # ruling on (NOTES flag 15). Fast heating means the thermometer trails
        # the sample: the start reads late by `collapse` of the true range and
        # the end reads late by `end_shift`, so the measured range becomes
        # `0.45 × range + 1.5`. A sharp melt smears out, a wide one compresses,
        # and every batch drifts towards the same middling number — which is
        # how a fast run hides an impure batch.
        {"type": "melting-point-bench", "id": "melting-points",
         "anchor": "s-bench",
         "demand": "investigate",
         "targets": "MIX-13",
         "eyebrow": "Your turn · the melting point bench",
         "heading": "The pure substance should melt at 53 °C. Go and find out "
                    "what you have.",
         "prompt": "A little of each sample in a tube, in a heated block, "
                   "with a thermometer. You record the temperature when "
                   "melting <em>starts</em> and when it <em>finishes</em>. "
                   "Two decisions are yours.",
         "dials": [
             {"id": "rate", "label": "How fast you heat the block",
              "default": "slow",
              "options": [{"id": "slow", "label": "Slowly, about 1 °C a minute"},
                          {"id": "fast", "label": "Quickly, to save time"}]},
             {"id": "repeats", "label": "How many times you run each sample",
              "default": 3,
              "options": [{"id": 1, "label": "Once"},
                          {"id": 3, "label": "Three times"}]},
         ],
         "run_label": "Run the samples",
         "rerun_label": "Run it again with these settings",
         "columns": ["Run", "Melting started", "Melting finished", "Range"],
         "unit": "°C",
         "decimals": 1,
         # A measured range wider than this is the reading that matters, and
         # the table says so in the accent — the one place a number is picked
         # out. Design's threshold, page line 507.
         "wide_above": 2,
         "fast_model": {"collapse": 0.55, "end_shift": 1.5},
         "samples": SAMPLES,
         "notes": BENCH_NOTES,
         "verdict_prompt": "Which batch is the impure one?",
         "verdict_buttons": [{"id": "b1", "label": "Batch 1"},
                             {"id": "b2", "label": "Batch 2"},
                             {"id": "b3", "label": "Batch 3"}],
         # `trusted` is slow AND repeated — the only setting whose data can
         # carry an accusation. It selects batch 2's second paragraph.
         "trusted_when": {"rate": "slow", "repeats_above": 1},
         "verdicts": BENCH_VERDICTS},

        {"type": "key-fact", "ref": "melts-sharply"},

        # ⊕ #s-words. Design drew no words section on this page — c3-01,
        # c3-02 and c3-05 have one because she drew those, and each of those
        # carries a rail stop for it. This one gets the cards and NOT a stop:
        # `check_rail_matches_design` compares the built rail against
        # `docs/ks3/rail-manifest.md`, so an added stop fails the build.
        # `terms` matches `vocabulary[].term` byte for byte.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each "
                 "card over. If you cannot say it, you do not "
                 "know it yet.",
         "terms": ["Melting point", "Melting range", "Expected value",
                   "Anomalous result", "Impurity"]},

        # ── Evaluate · the three limits of the method ──────────────────────
        # Light `.ks3-block` (page line 211), a headed list of three. Authored
        # as a `rule` panel: §5.1.1's vocabulary is closed, `explainer` carries
        # prose and no heading, and these three are the lesson's statement of
        # what its own method cannot do.
        #
        # ⚖️ Limit 1 is the idea rung 2 tests and it is the hardest thing on
        # the page: a sharp melt at the WRONG temperature is a pure substance
        # that is not the one you ordered.
        {"type": "rule", "anchor": "s-limits",
         "eyebrow": "Evaluate · what this method cannot do",
         "statement": "Three honest limits",
         "cards": [
             {"gloss": "A sharp melting point at the expected temperature "
                       "says the sample is pure. A sharp melting point at the "
                       "<strong>wrong</strong> temperature says it is a pure "
                       "substance that is not the one you ordered."},
             {"gloss": "Without an expected value the measurement means "
                       "nothing. You have to know what 53 °C was supposed to "
                       "be."},
             {"gloss": "It says <em>that</em> something else is present, "
                       "never <em>what</em>. Identifying the impurity is a "
                       "different job — and chromatography is where you would "
                       "start."},
         ]},

        {"type": "misconception", "id": "think-commit-one-run",
         "anchor": "s-think", "targets": "MIX-13"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Page lines 205–209: cream card, ink outline, accent shadow. Never amber.
    "key_facts": [
        {"id": "melts-sharply",
         "text": "A pure substance melts sharply, at one temperature. A "
                 "mixture melts over a range, and it starts lower than the "
                 "pure substance would. Purity is proved by a measurement "
                 "with a known expected value — never by looking.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── vocabulary (Law 7) ──────────────────────────────────────────────────
    # ⚖️ Three of these five are the WORKING-SCIENTIFICALLY words the lesson
    # is really about — expected value, melting range, anomalous result — and
    # the page uses all three without stopping for any of them. `Impurity`
    # keeps c3-01's definition unchanged and takes this lesson's note.
    "vocabulary": [
        {"term": "Melting point",
         "definition": "The temperature at which a solid turns to liquid.",
         "note": "A pure substance has one, and it is the same every time "
                 "you measure it."},
        {"term": "Melting range",
         "definition": "The spread between the temperature melting starts "
                       "at and the temperature it finishes at.",
         "note": "Within a degree for a pure substance. Several degrees for "
                 "a mixture, starting lower."},
        {"term": "Expected value",
         "definition": "The result you already know a pure sample should "
                       "give.",
         "note": "Without one, the measurement means nothing. You have to "
                 "know that 53 °C was what it was supposed to be."},
        {"term": "Anomalous result",
         "definition": "A reading that disagrees with the others taken the "
                       "same way.",
         "note": "Reported and set aside with a reason written down. Never "
                 "deleted, and never averaged in."},
        {"term": "Impurity",
         "definition": "Anything present that is not the substance you "
                       "wanted.",
         "note": "The melting range tells you THAT one is there. It never "
                 "tells you what it is."},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # The two instruments are authored inline in `core` above and lifted here
    # by `ks3_data/c3/__init__.py`. This list holds the one activity that is
    # not an instrument.
    "activities": [
        # ══ #s-think · the confrontation (contract R1) ═════════════════════
        #
        # `#s-think` asks for a commitment and then reveals, so it is a
        # `predict` and it DOES tick its rail stop.
        #
        # `statements` carries Design's own wording of the wrong idea (page
        # line 226), which is sharper than the register's MIX-13 line because
        # it names the trap: the reading was RIGHT. An authored statement wins
        # over the register.
        {"id": "think-commit-one-run",
         "kind": "predict",
         "demand": "explain",
         "targets": "MIX-13",
         "statements": [
             "I measured it once and got 53 °C, which is the right answer. "
             "That proves it is pure.",
         ],
         "prompt": "The reading was right and the sample really might be "
                   "pure. Commit before you read on.",
         "options": [
             "Right — the reading was correct, so the job is done",
             "Wrong — one reading cannot tell you whether it was a good "
             "reading",
             "Right, as long as the thermometer was accurate",
             "Wrong — melting point cannot show purity at all",
         ],
         "reveal": [
             # ⚠️ Repair 3 (see the module docstring). This sentence used to
             # end "can produce exactly the answer you were hoping for", which
             # the bench contradicts: fast and once, batch 2 still melts over
             # 4.65 °C and starts nearly four degrees low. The claim is shrunk
             # to what the instrument actually does.
             "One reading cannot tell you whether it was a good reading. Heat "
             "the block too fast and the thermometer lags behind the sample, "
             "so a wide range reads narrow and a low start reads high — a "
             "single fast run flatters an impure sample, closing much of the "
             "gap that would have given it away. Repeat it and the readings "
             "that agree with each other are the ones you can defend.",
             "And note what the batch 3 data did. Two runs agreed, one did "
             "not. The anomalous run is not deleted and it is not averaged in "
             "— it is <strong>reported, explained and set aside</strong>, and "
             "the reason is written down: the tube was packed loosely, or the "
             "block was still warming. That sentence is the difference "
             "between data and a result.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # Design's RUNGS map to the two page-marked rungs and SELF_RUNGS to the two
    # self-marked ones. Rungs 1 and 2 carry no `title`: Design's "Recall" and
    # "The one that catches people" are byte-identical to `LADDER_RUNGS`'
    # defaults, and a second copy is a copy free to drift. Rungs 3 and 4 do
    # carry one, because "Evaluate" and "Design it yourself" are not the
    # defaults ("Explain", "Take it somewhere new").
    "ladder": {
        "recall": {
            "q": "How does the melting behaviour of a pure substance differ "
                 "from that of a mixture?",
            "options": [
                "A pure substance melts over a range, starting lower; a "
                     "mixture melts sharply at one temperature",
                "A pure substance melts higher than a mixture does, but "
                "both of them melt sharply",
                "A pure substance melts sharply at one temperature; a mixture "
                "melts over a range, starting lower",
                "They melt in exactly the same way, so a melting point cannot "
                     "show purity",
            ],
            "answer": 2,
            "feedback": {
                0: "The other way round. The regular arrangement in a pure "
                   "solid gives way all at once.",
                1: "Half right. The pure substance does melt higher — but the "
                   "mixture melts over a range, and that range is the more "
                   "useful clue.",
                3: "Melting point is the standard test for purity, in schools "
                   "and in the pharmaceutical industry.",
            }},
        "apply": {
            "q": "A sample melts sharply, within half a degree — but at "
                 "61 °C, when the pure substance should melt at 53 °C. What "
                 "can you conclude?",
            "options": [
                "It is impure, because the temperature is wrong",
                "The thermometer must be broken",
                "It is pure, but it is not the substance you were expecting",
                "Nothing — a melting point cannot identify a substance",
            ],
            "answer": 2,
            "feedback": {
                0: "An impurity would give a range and a lower start. A sharp "
                   "melt is the signature of purity — this is a pure "
                   "something else.",
                1: "Possible, and checkable — but the reading is sharp and "
                   "repeatable, which is not how a broken thermometer usually "
                   "behaves. Read the data before blaming the kit.",
                3: "It cannot identify it on its own, but a sharp melt at the "
                   "wrong value is strong evidence about what you do and do "
                   "not have.",
            }},
        "explain": {
            "title": "Evaluate",
            # ⚠️ Repair 4 (see the module docstring). Design quoted the two
            # agreeing runs as "52–53 °C"; the bench computes 52.0–53.0 °C and
            # 52.5–53.5 °C, so both are quoted. The anomalous run is quoted
            # exactly as the bench computes it, and no criterion moved.
            "q": "In batch 3, two runs gave 52–53 °C and 52.5–53.5 °C, and "
                 "one gave 47.5–52 °C. Explain what you should do with the "
                 "odd run, what you must write down, and what your conclusion "
                 "about batch 3 should be.",
            "field_label": "Your evaluation",
            "placeholder": "The odd run is an anomaly, so…",
            "success": [
                "Identifies the middle run as an anomalous result.",
                "Says it should be reported and set aside, not silently "
                "deleted and not averaged in.",
                "Gives a plausible cause — sample packed loosely, block "
                "heated too fast, tube not in contact with the block.",
                "Says the anomaly should be repeated to check it.",
                "Concludes that the evidence points to batch 3 being pure, "
                "and says the conclusion rests on the two runs that agree.",
            ]},
        "produce": {
            "title": "Design it yourself",
            "q": "A shop suspects a supplier is bulking out bags of pure "
                 "sugar with something cheaper. You have a melting point "
                 "apparatus, a balance, filter equipment, chromatography "
                 "paper and a known pure sample of the sugar. Design an "
                 "investigation that would show whether the bags have been "
                 "tampered with, and say what result would prove it.",
            "field_label": "Your plan",
            "placeholder": "I would first measure the melting point of the "
                           "known pure sample…",
            "success": [
                "Measures the known pure sample first, to establish the "
                "expected value.",
                "Measures the suspect sample the same way, with repeats.",
                "States the incriminating result: a melting range wider than "
                "the pure sample, starting lower.",
                "Controls something that would otherwise spoil the comparison "
                "— same apparatus, same heating rate, same amount in the tube.",
                "Adds a step to find out what the impurity is, or says that "
                "this method cannot identify it.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "A pure substance melts sharply at one fixed temperature; a "
                "mixture melts over a range and starts lower. That makes "
                "melting point the test for purity — but only against a known "
                "expected value, only with repeats, and only if the sample is "
                "heated slowly enough for the thermometer to keep up. An "
                "anomalous run is reported and explained, never quietly "
                "deleted.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Page lines 330–331. The first paragraph is the PARTICLE explanation of
    # everything the bench measured; the second is the same physics run
    # deliberately, on a road and in a pharmacy.
    "stretch": [
        {"type": "explainer", "id": "why-a-mixture-melts-low",
         "text": "The reason a mixture melts low is worth knowing, because it "
                 "is used on every road in the country. In a pure solid, "
                 "every particle sits in the same regular arrangement, and "
                 "the whole thing gives way at one temperature. Mix something "
                 "else in and the arrangement is interrupted — the particles "
                 "no longer fit together as neatly, so less energy is needed "
                 "to break them apart, and different regions give way at "
                 "different temperatures. That is a lower melting point and a "
                 "range, from the same cause."},
        {"type": "explainer", "id": "grit-and-aspirin",
         "text": "Salt on an icy road is that effect run deliberately: salt "
                 "water freezes several degrees below 0 °C, so the ice melts "
                 "at a temperature at which pure water would stay solid. A "
                 "pharmacist checking a batch of aspirin uses the same "
                 "physics in the opposite direction — a melting range wider "
                 "than a degree means something is in there that should not "
                 "be, and the batch does not ship. Same measurement, same "
                 "reasoning, and one of them is on a gritter and the other is "
                 "in a laboratory."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The CTA points at `#s-bench`, which is where the anomalous run the card
    # names actually is (page line 354).
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure what to do with the anomalous run in "
                      "batch 3?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    "ks4_becomes": "Melting point as evidence of purity, and the distinction "
                   "between a pure substance and a formulation.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The three the lesson actually delivers: a method judged and then built,
    # readings taken with repeats, and an anomaly evaluated rather than tidied.
    "ws": ["experimental-skills-and-investigations", "measurement",
           "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
