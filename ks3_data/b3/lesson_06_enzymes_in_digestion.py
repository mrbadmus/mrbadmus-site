"""B3 L6 — Enzymes in digestion (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b3/b3-06-enzymes-in-digestion.dc.html` (657 lines), and its
author's notes, `docs/ks3/design-reference/b3/NOTES-B3.md`. Every student-facing string is
lifted byte-identical from the approved page except where this docstring says
otherwise, and every exception is here.

═══════════════════════════════════════════════════════════════════════════
⚠️  ENZYME RATE IS TAUGHT ON THIS PAGE AND IS **NOT** CLAIMED UNDER ANY
    STATUTORY STATEMENT.  MRB-199.  READ THIS BEFORE EDITING `covers`.
═══════════════════════════════════════════════════════════════════════════

`covers` names ONE clause and one only: the **catalyst** clause of
`KS3.B.NUT.04` — "enzymes simply as biological catalysts". That is the whole
of what the statutory document asks for, and the word *simply* is doing real
work in it.

Enzyme RATE — the temperature curve, the pH curve, the optimum, denaturing —
has **no KS3 statutory statement anywhere in the programme of study**. It
belongs to the Year 9 bridge, and MRB-199 removed it from B1 for exactly this
reason: `enzymes-and-what-changes-their-rate` is its natural owner, that lesson
is not yet authored, and a unit with no statement to hold the material must not
grow one to fit.

**Both of the following are true and this module holds both:**

  1. **THE PAGE IS BUILT AS DRAWN.** MRB-205: Design draws, Code renders. The
     bench is not gutted, the six temperature notes are not trimmed, the pH
     dial is not removed and the two rate-bearing ladder rungs are not
     rewritten. Every one of them is below, complete.

  2. **THE RATE MATERIAL IS NOT CLAIMED.** `covers` is `["KS3.B.NUT.04b"]`,
     the catalyst clause. `KS3.B.NUT.04` is NOT stretched to cover rate curves
     and no statement is invented for them. `beyond_statutory` stays False,
     because §7.6 rule 2 makes that flag mean "owns nothing" and this lesson
     owns the catalyst clause; the flag is not the place to record a lesson
     that is partly on-spec and partly ahead of it.

**Exactly which parts are beyond-statutory**, so Mide can rule on each rather
than on a summary. Line numbers are `b3-06-enzymes-in-digestion.dc.html`:

  ON-SPEC (the catalyst clause):
    line 88-104   the hook — a teaspoon of amylase digests a kilogram of
                  starch, and the reveal defines a catalyst.
    line 118      the three counters, and the instruction to watch the third.
    line 197      the key fact's FIRST sentence: "An enzyme is a biological
                  catalyst: it speeds a reaction up and is not used up doing
                  it."
    line 210-211  the second confrontation, "The enzyme gets used up".
    line 287      the key note's first two sentences: catalysts, and the three
                  named enzymes with their substrates and products.
    rung 1        what is left of the amylase afterwards.

  BEYOND-STATUTORY (rate — no KS3 statement owns any of it):
    line 80       "Heat it by fifteen degrees and it never works again."
    line 110-177  the whole bench: a 0–80 °C dial, three pH settings and a
                  live rate as a percentage of maximum.
    line 190      "Best at pH …" on each of the three enzyme cards.
    line 197      the key fact's SECOND sentence: "…and above about 50 °C that
                  shape is destroyed permanently."
    line 207      the first confrontation, "Enzymes are killed by heat" — the
                  whole paragraph, including "Cool it back to 37 °C and
                  nothing recovers".
    line 287      the key note's last two sentences: "Each works fastest at
                  about 37 °C and at the pH of the organ that makes it. Above
                  about 50 °C the enzyme is denatured and the change is
                  permanent."
    line 296      GOING FURTHER: the 40 °C / 60 °C washing-powder trade-off and
                  the fresh-pineapple jelly.
    rung 2        70 °C, cooled to 37 °C, still nothing — the denature latch.
    rung 3        the pH switch, mouth → stomach → small intestine, including
                  "raising the pH to around 8".
    rung 4        predict 20 °C, 40 °C and 90 °C, and design a fair test.
    line 316      the endmatter says so itself: "At GCSE this becomes …
                  rate-against-temperature and rate-against-pH curves."

That last line is worth Mide's eye on its own: the page names the two curves
as what this becomes at GCSE while teaching both of them here.

⚑ **THIS IS A FLAGGED FINDING, NOT A SILENT DECISION.** What is wanted is a
  ruling: either the rate material stays here and the Year 9 bridge lesson
  re-confronts rather than restates (NOTES-B3 §5 already proposes that, and
  says the bridge "should probably open by naming what B3 already did"), or it
  moves and this page loses its bench. Nothing in this module presumes either.

── `KS3.B.NUT.04b` is not yet minted ────────────────────────────────────

Same position as b3-05's `04a`. The unit wrapper
`ks3_data/biology_b3_nutrition.py` names the three-way split and the letters;
what is missing is the `ks3_data/substatements.py` entry, which spans b3-05,
this lesson and b3-07. Nothing in the build depends on it — `check_statutory`
only fires when a sub-ID is registered AND its parent is also owned — so this
ships correct and the minting is one edit across three lessons. Flagged rather
than done from one of three parallel lessons.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that the rail
lost a stop. Design's stage 3 (`#s-three`) ticks on `s.everRan` — the BENCH's
predicate, verbatim (page line 408) — and because `#s-three` is an eyebrow, a
display line, three cards and a key fact with no control, no commit and no
field, MRB-208's completion rule looked to forbid it and
`ks3_parity.check_rail_reachable` looked set to name the defect. THREE stops
shipped, not four.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine.

And `s.everRan` appearing twice is Design stating the tick condition, not
Design forgetting to write one. `isDone()` is a rail-level function and returns
the identical expression for `#s-bench` and then for `#s-three`. Amylase,
protease and lipase are the payoff of the run beside them; the section holds no
control because the bench has already taken the student's commitment. That is a
MIRROR, resolved at rail level in `wireRail`'s `paint()`.

So the fourth stop is declared: anchor `s-three`, `mirrors: "s-bench"`,
`done_when: "reaction_run"` — the bench's own predicate, named as borrowed, and
gated by `check_rail_matches_design` against `docs/ks3/rail-manifest.md`. The
section keeps its anchor, as it always did.

── One addition inside a component Design drew ──────────────────────────

The bench's verdict now shows whenever a run has FINISHED, whatever finished
it. Design shows it on twenty ticks or on denaturing (page line 592), so a run
at a rate of exactly zero that is NOT denatured — stomach protease dropped into
pH 8, which is one press of one button — finished on its first tick and showed
**no verdict at all**. The bench went quiet, and the "slow" verdict that exists
to send the student back to the pH dial never appeared. Design's three verdict
branches are unchanged; only when they are shown moved. The page was silent on
this case, so this is an addition rather than a contradiction.

⊕ RULED AND FIXED — MRB-255 S4 (19 Aug 2026). Stomach protease at pH 8 read 0%
  of maximum, because the bench modelled ONE protease with `opt_ph` 2 and the
  pH term falls linearly over 4.5 units: |8 − 2| = 6 against a span of 4.5, so
  zero. It sat directly beside its own card — "Best at pH 2 in the stomach, 8
  in the small intestine" — and this module flagged it as a science call rather
  than a build one, which was right.

  The gate ruled: **the card is right and the model changes.** Pepsin is ~2 and
  trypsin ~8; it is why the lesson teaches the pancreatic alkali at all, and it
  is what AQA asks. `opt_ph` is now a SET and the rate uses the gap to the
  nearest optimum in it, so protease reads 100% at both pH 2 and pH 8 and the
  bench finally agrees with the card. This was the sharpest instance of the
  prose-over-instrument class in the whole audit: the pairing the lesson most
  wants a student to try was the one the bench denied.

── What could not be lifted byte-identical ─────────────────────────────

* **`#s-three`'s three enzyme cards are compressed.** Design draws each with a
  mono "Made in …" line, a display name, the equation in its own inset mono
  panel, a note and a mono "Best at pH …" line. The §5.1.1 block vocabulary is
  CLOSED; `rule` — whose shell matches Design's section value for value
  (`--ks3-band`, 3px ink, `--ks3-r-block`, 34px 32px, accent eyebrow) — carries
  a `term` and a `gloss`. So the name becomes the term and the other four lines
  become one gloss, with the "Made in …" and "Best at pH …" lines in
  `<strong>` and the system's own middot joining the equation to the note.
  Every authored byte is present, in Design's order; the equation loses its
  inset panel. Reported.

* **The three reaction equations are authored twice** — once on the bench, for
  its live readout, and once inside the `rule` card glosses. Design holds one
  `ENZYMES` array serving both; here the bench is an activity and the band is a
  block, and a block cannot read an activity's data. Reported.

── Ladder length parity (MRB-177) ───────────────────────────────────────

**BOTH MARKED RUNGS FAILED AS DELIVERED, and both are fixed by completing the
distractors — never by shortening the correct answer, and never by changing
which misconception a distractor carries.** Design's own precedent is c1-02.

    rung 1  BEFORE  correct 14, distractors 10 / 6 / 7.
                    +4 words and ×1.40 over the longest — over BOTH thresholds.
            AFTER   correct 14 (unchanged), distractors 13 / 13 / 13.
                    +1 word, ×1.08 — PASS.
            Misconceptions kept exactly: consumed by the reaction; some is
            always lost; the amount needed scales with the substrate.

    rung 2  BEFORE  correct 14, distractors 10 / 9 / 5.
                    +4 words and ×1.40 — over BOTH thresholds.
            AFTER   correct 14 (unchanged), distractors 12 / 12 / 13.
                    +1 word, ×1.08 — PASS.
            Misconceptions kept exactly: it needs re-warming; it was killed;
            the starch denatured instead.

    Every one of Design's per-option `correction` strings still answers its
    completed distractor and is lifted unchanged.

⚑ For Mide's science gate — NOTES-B3's own flags, carried here:
  * flag 15  stomach protease at pH 2 described as "unusual for a protein".
  * flag 16  the rate model is not a real curve: optimum 37 °C, zero at and
             above `denature_c`, linear pH falloff over 4.5 units, threshold
             settled at 50 °C and now stated in four places. The foot line
             says the bench is a simplified model.

⚑ `DIET-13` / `DIET-14` are the two ids NOTES-B3 §5 names for the enzyme pair,
  and they are the only anchored ones in the family — the rest of B3's
  numbering is provisional. `docs/ks3/misconception-register.md` contains no
  `DIET` family row at all, although NOTES says fifteen were written into it.
  Nothing machine-reads the register, so the build is unaffected.

⚑ `--ks3-ok` OUTSIDE THE LADDER. The enzyme counter's bar is green. The
  token's own comment in `tokens.css` reserves green for the ladder marking
  correctness, and this is a bar meaning "unchanged" on a block that marks
  nothing. Design drew it; it is reproduced as drawn and registered in a parity
  row, so the day the palette question is ruled the gate names the value.
"""

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 108 character for character.
    "slug":        "enzymes-in-digestion",
    "title":       "Enzymes in digestion",
    "discipline":  "biology",
    "unit":        "nutrition-and-digestion",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚠️ ONE CLAUSE, AND NOT A WORD MORE. "enzymes simply as biological
    # catalysts". The rate material on this page is beyond-statutory and is
    # deliberately NOT claimed here — see the module docstring, which lists
    # every rate-bearing line by number. Do not widen this to `KS3.B.NUT.04`
    # and do not invent a statement for the curves.
    "covers":      ["KS3.B.NUT.04b"],
    "touches":     [],
    # ⚠️ FALSE, and that is not a contradiction of the note above. §7.6 rule 2
    # makes `beyond_statutory` mean "owns NO statement", and this lesson owns
    # the catalyst clause. The flag has no half-setting; the docstring is where
    # a partly-ahead lesson is recorded.
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "substances-and-reactions", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 40,

    # ── progression edges ───────────────────────────────────────────────────
    "requires":    ["the-digestive-system"],
    "assumes":     [],
    "references":  ["food-tests",
                    {"unit": "P1", "lesson": "heating-and-thermal-equilibrium"}],
    "ks4_links":   [],
    # ⚑ The page's own admission that it is ahead of itself. Lifted unchanged.
    "ks4_becomes": "The lock-and-key model, active sites, and "
                   "rate-against-temperature and rate-against-pH curves.",

    # ── framing ─────────────────────────────────────────────────────────────
    # ⚑ The second sentence is beyond-statutory (denaturing). Lifted.
    "big_question": "One enzyme molecule can cut a thousand others apart and "
                    "still be there at the end. Heat it by fifteen degrees and "
                    "it never works again. Neither of those is what people "
                    "expect.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-three` is the third: no control of
    # its own, so it mirrors `s-bench` and ticks on the bench's predicate — see
    # the docstring. `short` and `label` are Design's own (page lines
    # 337–342).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "A teaspoon",
         "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",  "label": "Run it",
         "done_when": "reaction_run"},
        {"anchor": "s-three", "short": "THREE", "label": "The three",
         "mirrors": "s-bench", "done_when": "reaction_run"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Squarely the catalyst clause: a teaspoon does a kilogram and is all still
    # there. No rate anywhere in it.
    "phenomenon": {
        "kind": "narrative",
        "title": "A teaspoon of amylase digests a kilogram of starch.",
        "prompt": "Weigh the amylase before and after. It has not gone down. "
                  "Filter it out at the end and it works exactly as well on "
                  "the next kilogram, and the one after that. The starch is "
                  "gone; the amylase is all still there.",
        "commit": "So what is an enzyme doing?",
        "options": [
            "Being broken down along with the starch",
            "Speeding the reaction up without being changed by it",
            "Turning itself into glucose",
            "Supplying the energy the reaction needs",
        ],
        "reveal": "It is a catalyst: a molecule that makes a reaction happen "
                  "faster without being changed or used up by it. That is the "
                  "whole definition, and it is why a small amount of enzyme is "
                  "enough for an enormous amount of food.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # The two ids NOTES-B3 §5 names for the enzyme pair, in Design's document
    # order. Each `statement` is Design's own `.ks3-mis-quote` without its
    # quote marks.
    #
    # ⚑ DIET-13 is a RATE misconception. It is confronted here because Design's
    # page confronts it here; it is not claimed under any statement.
    "misconceptions": [
        {"id": "DIET-13",
         "statement": "Enzymes are killed by heat.",
         "elicited_by": "the-bench",
         "confronted_by": "two-wrong-ideas"},
        {"id": "DIET-14",
         "statement": "The enzyme gets used up as the food is digested.",
         "elicited_by": "the-bench",
         "confronted_by": "two-wrong-ideas"},
    ],

    # Design draws no keyword block on this page, so these never reach the
    # lesson body; they reach a student as the unit page's chips and are the
    # reading-age gate's exclusion list.
    #
    # ⚑ `denatured` is beyond-statutory vocabulary — it belongs to the rate
    # material, not to the catalyst clause. It is defined here because the page
    # uses the word eleven times and a chip that is missing for a word the
    # lesson leans on is worse than one that is ahead of the statement.
    "vocabulary": [
        {"term": "enzyme",
         "definition": "A protein that speeds up one particular reaction in a "
                       "living thing.",
         "note": None},
        {"term": "catalyst",
         "definition": "Something that makes a reaction go faster without "
                       "being used up by it.",
         "note": "That is why a teaspoon of enzyme can handle a kilogram of "
                 "food."},
        {"term": "substrate",
         "definition": "The substance an enzyme works on.",
         "note": None},
        {"term": "denatured",
         "definition": "An enzyme whose shape has been destroyed, so it no "
                       "longer fits its substrate.",
         "note": "Not the same as dead. An enzyme is a molecule and was never "
                 "alive."},
    ],

    # Nothing on this page references a figure — the bench is the drawing.
    # Present and empty, never absent.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, on `ks3-block ks3-dark ks3-practical`.
        # Authored inline; `_normalise` lifts it into `activities[]` and leaves
        # a `practical` shell behind it.
        #
        # ⚑ EVERYTHING FROM `temp` DOWN IS BEYOND-STATUTORY, and it is built as
        # drawn. See the module docstring for the ruling this is waiting on.
        {"type": "enzyme-run", "id": "the-bench", "anchor": "s-bench",
         "demand": "investigate",
         "eyebrow": "At the bench · one tube, two dials",
         "heading": "Run the reaction, watch the counts",
         # A two-state readout rather than a count: there is one thing to
         # report and it is a boolean.
         "head_counter": {"off": "not run yet", "on": "reaction run"},
         "prompt": "Watch all three counters, and watch what happens to the "
                   "third one.",
         "group_labels": {"enzyme": "Enzyme",
                          "ph": "pH of the tube",
                          "temp": "Temperature"},

         # The counter names are authored per enzyme rather than built from a
         # substrate word: "Fatty acids and glycerol made" is a sentence, not a
         # capitalisation.
         "enzymes": [
             {"id": "amylase", "label": "Carbohydrase",
              "equation": "starch → glucose", "opt_ph": 7,
              "counter_substrate": "Starch left",
              "counter_product": "Glucose made"},
             # ⚖️ MRB-255 S4 · TWO OPTIMA, AND THE CARD WAS ALWAYS RIGHT.
             # Design modelled one protease at pH 2, so protease + pH 8 read
             # 0% and the verdict said "the conditions are simply wrong for
             # it" — directly under a card reading "Best at pH 2 in the
             # stomach, 8 in the small intestine". Pepsin is ~2 and trypsin
             # ~8; that is why the lesson teaches the pancreatic alkali at
             # all, and it is what AQA asks. Ruled: the card is right and the
             # model moves. `opt_ph` may be a scalar or a set; the rate uses
             # the gap to the NEAREST optimum. `_erun_rate` and `rateFor()`
             # both implement it and must stay in step.
             {"id": "protease", "label": "Protease",
              "equation": "protein → amino acids", "opt_ph": [2, 8],
              "counter_substrate": "Protein left",
              "counter_product": "Amino acids made"},
             {"id": "lipase", "label": "Lipase",
              "equation": "lipid → fatty acids + glycerol", "opt_ph": 8,
              "counter_substrate": "Lipid left",
              "counter_product": "Fatty acids and glycerol made"},
         ],
         "phs": [
             {"value": 2, "label": "pH 2 — stomach"},
             {"value": 7, "label": "pH 7 — mouth"},
             {"value": 8, "label": "pH 8 — small intestine"},
         ],
         # The bench opens at the MOUTH's pH with carbohydrase in the tube, so
         # the resting rate is 100% and the student's first move is away from
         # a working reaction rather than towards one.
         "start_ph": 7,

         "temp": {"min": 0, "max": 80, "step": 1, "start": 37,
                  "format": "{t} °C",
                  "field_label": "Temperature of the tube"},

         # ⚠️ ONE THRESHOLD, AUTHORED ONCE. `denature_c` is quoted in the key
         # fact, in two temperature notes, in the key note, in a ladder
         # correction and in GOING FURTHER — six sentences, one number, and it
         # reaches the runtime from here.
         "model": {"denature_c": 50, "optimum_c": 37,
                   "rise_exponent": 1.6, "fall_divisor": 13,
                   "ph_span": 4.5},
         "temp_bands": {"past_optimum": 45, "optimum": 33, "cold": 12},

         # ⚖️ SIX BRANCHES, AND THE TWO DENATURED ONES SAY DIFFERENT THINGS.
         # "Cool it first, then take a fresh tube" has to be distinguishable
         # from "cooling changes nothing", or the latch teaches nothing.
         "temp_notes": {
             "denatured_hot":
                 "Above about 50 °C the folds holding this enzyme’s shape have "
                 "come apart, and the damage is already done. Cooling the tube "
                 "will not bring it back — cool it first, then take a fresh "
                 "tube.",
             "denatured_cool":
                 "This enzyme was taken above 50 °C and is denatured. It is "
                 "back at a temperature it would work perfectly well at, and "
                 "it will not work at all. Only a fresh tube starts again.",
             "past_optimum":
                 "Past the optimum and falling fast. The molecule is beginning "
                 "to lose its shape, and above 50 °C it will not get it back.",
             "optimum":
                 "Around body temperature — close to the fastest this enzyme "
                 "goes.",
             "cold":
                 "Cold but unharmed. Molecules collide less often, so the rate "
                 "is low; warm it up and it recovers completely.",
             "freezing":
                 "Near freezing. Almost nothing happens, and nothing is "
                 "damaged — this is how a fridge slows food spoiling.",
         },

         "run": {"ticks": 20, "tick_ms": 160, "units_per_tick": 90,
                 "start_substrate": 1000,
                 # Reduced motion SCALES the tick rate and never stops the
                 # counter: every one of the twenty ticks still happens, each
                 # further apart, so the end state is the same one.
                 "reduced_motion_scale": 0.35,
                 "slow_below_pct": 25,
                 "labels": {"start": "Run the reaction",
                            "more": "Run more",
                            "running": "Running…",
                            "reset": "Fresh tube",
                            "clock": "{n} of {total} ticks",
                            "clock_fresh": "fresh tube",
                            "rate": "Rate {pct}% of maximum"}},
         "units_format": "{n} units",

         # ⚖️ THE COUNTER THAT NEVER MOVES. A constant string and a full bar,
         # with no runtime handle at all — see the renderer.
         "enzyme_counter_label": "Enzyme molecules present",
         "enzyme_counter_value": "40 — unchanged",

         "verdicts": {
             "denatured":
                 "Nothing was digested and nothing will be. All forty enzyme "
                 "molecules are still in the tube — they have not been used "
                 "up, they have been ruined. Turn the temperature back down "
                 "and run it again: still nothing. That is the difference "
                 "between denatured and merely cold.",
             # ⊕ MRB-257 (5.7) — THE RUN THAT PRODUCED NOTHING. Protease +
             # pH 7, lipase + pH 2 and carbohydrase + pH 2 all finished on
             # `Rate 0%` and `0 units made` under "A little product, slowly."
             # A little is not none, and the sentence a student reads has to
             # be true of the counters beside it. Tested BEFORE the rate.
             "nothing":
                 "Nothing was digested at all. The enzyme is intact — it has "
                 "not been ruined, and the counter still reads forty — but in "
                 "these conditions it is not working. Move the pH towards one "
                 "this enzyme works at, or the temperature back towards 37 °C, "
                 "and run it again.",
             # ⚖️ 5.51 — THE BLAME MOVED. This branch named pH as the cause in
             # every state, including pH 7 with the temperature slider at 0 °C,
             # where the pH is already the enzyme's own optimum and the cold is
             # the whole of the problem. The rate term is a PRODUCT of a
             # temperature term and a pH term, so a slow run has two possible
             # causes and the sentence may not pick one.
             "slow":
                 "A little product, slowly. The enzyme is intact and these are "
                 "not the conditions it works best in — move the pH towards "
                 "one this enzyme works at, or the temperature towards 37 °C, "
                 "and run it again to see the difference.",
             "worked":
                 "Substrate down, product up, enzyme unchanged. Forty "
                 "molecules converted hundreds of units and are all still "
                 "there, ready to do it again.",
         }},

        # #s-three — Design's classless band section, which IS the `rule`
        # shell. Rail stop 3, mirroring `s-bench`; see the docstring.
        {"type": "rule", "anchor": "s-three",
         "eyebrow": "The three you must know",
         "statement": "One enzyme, one substrate, one place it works best.",
         # ⚠️ COMPRESSED, and the equations are authored a second time here —
         # see the docstring. `t()` DRAWS the arrow rather than typing it.
         "cards": [
             {"term": "Carbohydrase (amylase)",
              "gloss": "<strong>Made in the salivary glands and pancreas</strong> "
                       "starch → glucose · Starts in the mouth, stops in the "
                       "acid of the stomach, and starts again in the small "
                       "intestine when pancreatic alkali has neutralised the "
                       "acid. <strong>Best at pH 7 (neutral)</strong>"},
             {"term": "Protease",
              "gloss": "<strong>Made in the stomach and pancreas</strong> "
                       "protein → amino acids · The stomach version is built "
                       "to work in acid, which is unusual for a protein — most "
                       "would denature at pH 2. It is a genuinely specialised "
                       "molecule. <strong>Best at pH 2 in the stomach, 8 in "
                       "the small intestine</strong>"},
             {"term": "Lipase",
              "gloss": "<strong>Made in the pancreas</strong> "
                       "lipid → fatty acids + glycerol · Works on the surface "
                       "of fat droplets, so bile’s emulsifying job multiplies "
                       "its rate rather than helping it chemically. "
                       "<strong>Best at pH 8 (slightly alkaline)</strong>"},
         ]},

        {"type": "key-fact", "ref": "enzymes-are-catalysts"},

        {"type": "misconception", "id": "two-wrong-ideas",
         "anchor": "s-think", "targets": "DIET-13"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # ⚑ Sentence one is the catalyst clause. Sentence two's tail — "and above
    # about 50 °C that shape is destroyed permanently" — is beyond-statutory.
    # Lifted whole; the docstring records the split.
    "key_facts": [
        {"id": "enzymes-are-catalysts",
         "text": "An enzyme is a biological catalyst: it speeds a reaction up "
                 "and is not used up doing it. Each one has a shape that fits "
                 "one substrate, and above about 50 °C that shape is destroyed "
                 "permanently.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "two-wrong-ideas",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "DIET-13",
         "statements": [
             # ⚑ BEYOND-STATUTORY in full — this is the denaturing paragraph.
             {"quote": "Enzymes are killed by heat.",
              "body": [
                  "An enzyme cannot be killed, because it was never alive. It "
                  "is a single protein molecule — no cell, no membrane, no "
                  "respiration, nothing that could die. What heat does is "
                  "shake the molecule until the folds holding its shape come "
                  "apart, and since the shape is the whole point, a molecule "
                  "with the wrong shape no longer fits its substrate. The word "
                  "is <em>denatured</em>, and examiners take the difference "
                  "seriously. It matters practically too: “killed” suggests "
                  "something that could be replaced by growing more, whereas a "
                  "denatured enzyme is a permanently ruined tool. Cool it back "
                  "to 37 °C and nothing recovers — which is exactly what you "
                  "saw on the bench above, and it is why the change is not "
                  "simply the reverse of warming up."]},
             # On-spec: this one IS the catalyst clause.
             {"quote": "The enzyme gets used up as the food is digested.",
              "body": [
                  "Watch the third counter on the bench. Substrate falls, "
                  "product rises, enzyme does not move. A single amylase "
                  "molecule binds a starch chain, cuts it, releases the pieces "
                  "and is immediately free to bind the next one — thousands of "
                  "times a second in some cases. This is what the word "
                  "catalyst means, and it explains a fact that is otherwise "
                  "baffling: your pancreas makes a few grams of enzyme a day "
                  "and it handles a kilogram of food. If enzymes were consumed "
                  "by the reactions they catalyse, digestion would be limited "
                  "by how fast you could manufacture them, and no animal could "
                  "eat a large meal."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # ⚖️ **BOTH MARKED RUNGS FAILED MRB-177's LENGTH-PARITY CHECK AS DELIVERED
    # AND BOTH ARE FIXED BY COMPLETING THE DISTRACTORS.** Design's correct
    # options are unchanged — they are the science — and every distractor keeps
    # its misconception exactly. The measurement, before and after, is in the
    # module docstring. Precedent: c1-02's rung 2.
    "ladder": {
        "recall": {
            "title": "Rung 1 · What a catalyst is",
            "q": "After digesting a large amount of starch, how much of the "
                 "original amylase is left?",
            # BEFORE: 14 / 10 / 6 / 7 words — the correct option ran +4 words
            # and ×1.40 over the longest distractor, which is over both
            # thresholds, and a class works out early that the long one is
            # usually right. AFTER: 14 / 13 / 13 / 13.
            "options": [
                "All of it — an enzyme is not used up by the reaction it "
                "catalyses",
                # was "None — it is consumed as the starch is broken down"
                "None — it is consumed by the reaction as the starch is "
                "broken down",
                # was "About half — some is always lost"
                "About half — some enzyme is always lost each time it does "
                "its job",
                # was "It depends how much starch there was"
                "It depends how much starch there was — more starch uses up "
                "more enzyme",
            ],
            "answer": 0,
            "feedback": {
                1: "Then a teaspoon could not digest a kilogram. Substrate "
                   "falls and product rises; the enzyme count does not change.",
                2: "None is lost to the reaction. A catalyst finishes each "
                   "cycle in the same state it started.",
                3: "It does not. That is precisely what makes a catalyst "
                   "useful — the amount needed does not scale with the amount "
                   "of substrate.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Amylase at 70 °C digests no starch. It is cooled back to "
                 "37 °C and still digests no starch. Why not?",
            # BEFORE: 10 / 14 / 9 / 5 words — again +4 and ×1.40 over the
            # longest distractor. AFTER: 12 / 14 / 12 / 13.
            "options": [
                # was "It needs to be warmed up again to become active"
                "It needs to be warmed up again before it will become active",
                "Its shape was permanently destroyed by the heat, so it no "
                "longer fits starch",
                # was "The enzyme was killed and dead enzymes cannot work"
                "The enzyme was killed by the heat, and dead enzymes cannot "
                "work",
                # was "The starch was denatured instead"
                "The starch was denatured instead, so amylase has nothing left "
                "to work on",
            ],
            "answer": 1,
            "feedback": {
                0: "It is at 37 °C, which is its optimum. Temperature is no "
                   "longer the problem — something about the molecule has "
                   "changed.",
                2: "The idea is close but the word is wrong, and the wrong "
                   "word carries a wrong picture. An enzyme is a molecule and "
                   "was never alive; it is denatured, not dead.",
                3: "Starch has no folded shape to lose. Heating starch in "
                   "water does not stop amylase digesting it — it usually "
                   "helps.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the pH switch",
            "q": "Amylase from saliva works well in the mouth, stops working "
                 "in the stomach, and then starch digestion resumes in the "
                 "small intestine. Explain all three stages, and say what the "
                 "pancreas contributes besides enzymes.",
            "field_label": "Your explanation",
            "placeholder": "In the mouth… in the stomach… in the small "
                           "intestine…",
            "success": [
                "Says salivary amylase works at about pH 7, which is the pH of "
                "the mouth.",
                "Says the stomach is about pH 2 and that this stops amylase "
                "working.",
                "Says the pancreas supplies fresh amylase into the small "
                "intestine.",
                "Says the pancreas also supplies an alkali that neutralises "
                "the stomach acid, raising the pH to around 8.",
                "Makes clear that the amylase which entered the stomach does "
                "not recover — the resumed digestion uses new enzyme.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A washing powder claims to work at any temperature. Using "
                 "what you know about enzymes, say what you would expect to "
                 "happen at 20 °C, at 40 °C and at 90 °C, and design a fair "
                 "test of the claim.",
            "field_label": "Your answer",
            "placeholder": "At 20 °C I would expect…",
            "success": [
                "Predicts slow action at 20 °C — enzymes work, but the rate is "
                "low.",
                "Predicts the best result near 40 °C, close to the optimum.",
                "Predicts little or no enzyme action at 90 °C because the "
                "enzymes are denatured, while noting hot water alone still "
                "removes some dirt.",
                "Describes a fair test: identical stains, identical fabric, "
                "same mass of powder, same time, only the temperature changed.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # ⚑ Sentences one and two are the catalyst clause. Sentences three and four
    # are beyond-statutory. Lifted whole.
    "key_note": "Enzymes are biological catalysts. Carbohydrase breaks starch "
                "to glucose; protease breaks protein to amino acids; lipase "
                "breaks lipid to fatty acids and glycerol. Each works fastest "
                "at about 37 °C and at the pH of the organ that makes it. "
                "Above about 50 °C the enzyme is denatured and the change is "
                "permanent.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # MRB-225: the trade-off and the model's edges live HERE, and nothing above
    # is retracted by it — the 40 °C advice is not withdrawn, it is given a
    # cost. ⚑ Entirely beyond-statutory.
    "stretch": [
        {"type": "explainer", "id": "washing-and-pineapple",
         "text": "Biological washing powder contains protease and lipase, "
                 "which is why it removes blood and grease and why the box "
                 "tells you to wash at 40 °C rather than 60 °C — a hot wash "
                 "denatures the enzymes you paid for. The awkward consequence "
                 "is that a wash cool enough to keep the enzymes working is "
                 "also cool enough to leave some bacteria alive, so the choice "
                 "between a 40 °C enzyme wash and a 60 °C sterilising wash is "
                 "a genuine trade-off rather than a mistake. Enzymes are also "
                 "why you cannot make jelly with fresh pineapple: it contains "
                 "a protease that cuts the gelatin protein apart faster than "
                 "it can set. Tinned pineapple works perfectly, because "
                 "canning heats it and denatures the enzyme."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to talk through why denaturing cannot be undone?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is an investigation with two independent variables, and rung 4
    # asks for a fair test in as many words.
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ⚠️ THE FOOT LINE, BYTE-IDENTICAL. It is a statement about how the numbers
    # on this page were taken — `convention_note`'s exact purpose (plain
    # `.ks3-legal`, page-specific, before the standing line) rather than
    # `safety_note`, whose treatment is reserved for a safety instruction.
    "convention_note": "The bench is a simplified model: rate is shown against "
                       "temperature and pH only, and one substrate at a time. "
                       "Real digestion runs several enzymes at once on a "
                       "mixture, and the curves are smoother than the numbers "
                       "here suggest.",

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
