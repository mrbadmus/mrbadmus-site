"""C3 L4 — Evaporation and crystallisation (PROCESS).

Authored against Design's approved page,
`docs/ks3/design-reference/c3/c3-04-evaporation-and-crystallisation.dc.html`
(681 lines), and her unit notes `docs/ks3/design-reference/c3/NOTES-C3.md`
(§2, §3.4, §4 flags 8 and 9, §5, §6).

Every student-facing string is byte-identical to the approved page. `RAIL`,
`SOLUTES`, `METHODS`, `JOBS`, `RUNGS` and `SELF_RUNGS` came out of the node
extractor; the dial labels, the predict-gate, the three readout labels, the
dish caption, the run-button format, the alt-text template, the all-three
summary line, both explainer paragraphs, the key fact, the key note, the two
"Going further" paragraphs and the whole of `#s-think` were lifted from
`lessonVals()` and the markup, which is where they live and where a lift of
the top-level constants alone silently loses them.

── The bench is a PARAMETER BENCH, and that is a decision ───────────────

NOTES §2 and §6: `c3-03` already used a stepper, and an identical block lineup
two lessons running must never be the default. So this one is three solutes
crossed with three methods — nine runs, freely chosen, no fixed order.

⚖️ THE MASS RECOVERED IS THE SAME IN ALL NINE RUNS AND ONLY THE CRYSTALS
CHANGE. `recovered_mass` is ONE string on the instrument, not a field on
`solutes[]` and not a field on `methods[]`, because that is the teaching point
expressed as structure: there is nowhere in this record for a method to carry
a yield, so no edit can accidentally make a faster method pay better. The
summary line, the `apply` rung and four of the twelve questions all rest on
it. If a later change gives `methods[]` its own mass, the lesson is gone.

`time`, `size`, `count` and `quality` DO vary by method; `colour`, `shape`,
`product`, `hard` and `slow` vary by solute. Nothing varies by both except
the composed hazard line, and that is composition, not data.

── What the renderer must compute, and must not be handed ───────────────

The dish drawing is derived from `size`, `count`, `colour` and `shape`; the
alt text is derived from `count`, `product` and `size`. Neither is authored as
a finished string, because §6 of the brief binds: a figure quoted in prose has
to be what the instrument computed, and a hand-written "14 tiny crystals"
would be a second copy free to drift. `size_words` carries the thresholds
Design's own ternary uses, so the wording is authored and the choice is not.

⚑ For Mide's science gate, from Design's NOTES §4:
  * flag 8 — copper sulfate turning WHITE when a dry dish is over-heated, and
    the water of crystallisation named as the reason. KEPT, in the stretch
    layer, as drawn. It is true, it is the honest explanation of an
    observation this bench actually produces (`SOLUTES.copper.hard` is the
    warning the bench prints on a boil run), and nothing later in the lesson
    walks it back. The stretch paragraph and the bench agree word for word:
    stop heating while there is still liquid in the dish.
  * flag 9 — the Naica gypsum crystals, "metres long", grown over hundreds of
    thousands of years at a steady 58 °C. KEPT and deliberately not
    numbered: the largest beams are about 11–12 m, so "metres long" is true,
    conservative, and cannot be overtaken by a better survey.
  * MIX-08 is PART-05 in a third costume (NOTES §5). The cross-reference is
    student-facing, in the second reveal paragraph of `#s-think` — "the same
    wrong idea as 'the puddle dried up and the water was destroyed', met in
    the particle model and met again here". It is authored there rather than
    as a register key because the register has no cross-reference key with a
    read site, and R5 binds: a key nothing renders is not authored.
"""

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 201 character for character.
    "slug":        "evaporation-and-crystallisation",
    "title":       "Evaporation and crystallisation",
    "discipline":  "chemistry",
    "unit":        "mixtures-and-separation",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # NOTES §1: PIS.04 names four techniques and gets four lessons, one each.
    # This is one of the four, and claiming the statement is correct — §5 of
    # the brief: a statutory statement may be claimed by more than one lesson.
    "covers":      ["KS3.C.PIS.04b"],
    "touches":     ["KS3.C.PIS.02"],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 2},
                    {"id": "structure-function", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # `requires` draws the "Before this lesson" card, `references` the
    # "Next in this unit" card — both measured from Design's end matter.
    "requires":    ["filtration"],
    "assumes":     [],
    "references":  ["distillation"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "The salt is dissolved and invisible. Getting it back is "
                    "easy — getting it back as crystals you can hold is a "
                    "question of how much of a hurry you are in.",

    # ── the progress rail ───────────────────────────────────────────────────
    # Five stops (NOTES §6). `done_when` is documentation — the rail's real
    # test is `doneByDom` in shared/ks3.js — so each one records Design's own
    # `DONE()` expression in words.
    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",  "label": "Two dishes",
         "done_when": "committed"},
        {"anchor": "s-bench", "short": "BENCH", "label": "The bench",
         "done_when": "all_three_methods_run"},
        {"anchor": "s-jobs",  "short": "JOBS",  "label": "Three jobs",
         "done_when": "all_jobs_decided"},
        {"anchor": "s-think", "short": "THINK",
         "label": "Where the water went", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # `kind` is unread by the engine and reported as such in build_ks3.py; it
    # stays because it is how the record names what sort of hook this is.
    "phenomenon": {
        "kind": "demo",
        "title": "Same solution, same salt, two dishes. One took four "
                 "minutes and one took a week.",
        "prompt": "Both dishes started with 20 cm³ of the same salt "
                  "solution. One was boiled over a Bunsen until it was dry. "
                  "The other sat on a windowsill until the water had gone. "
                  "Both ended up with exactly the same mass of salt.",
        "commit": "Which dish has the bigger crystals in it, and why would "
                  "anyone care?",
        "options": [
            "The boiled dish — heat makes crystals grow",
            "The windowsill dish — slow growth gives bigger crystals",
            "Both the same — same salt, same mass",
            "Neither — you only get a powder either way",
        ],
        "reveal": "The windowsill. Boiling gives a white crust of crystals "
                  "too small to see individually; a week of slow evaporation "
                  "gives cubes you can pick up with tweezers. Same salt, same "
                  "mass, same substance — and the difference matters, "
                  "because a big clean crystal is the evidence that you have "
                  "one substance and not a dried-out puddle of whatever was "
                  "in the dish.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # IDs from NOTES §5. The STATEMENT is the page's own drawn quote where the
    # page draws one, because `_misconception_quote()` prints it verbatim as
    # the `ks3-mis-quote` — same convention as c2-03's ATOM-07.
    #
    # ⚑ MIX-08 IS PART-05 IN A THIRD COSTUME. "The puddle dried up", "the mass
    # went down when it burned" (that one minted as ATOM-11), and now "the
    # water evaporated so it is gone". Design minted it separately because the
    # confrontation is different — a cold surface, not a sealed bag — and it
    # carries the cross-reference rather than pretending to be new. The
    # cross-reference is IN THE STUDENT-FACING REVEAL, second paragraph of
    # `think-commit-water`, where it renders; see the module docstring.
    #
    # Design's register names an elicit half and a confront half
    # (`think-commit-water` / `think-reveal-water`, `bench-boil-run` /
    # `bench-summary`). Each pair is two beats of ONE activity — the gated
    # commitment and its reveal — and an activity has one id, so both fields
    # name the activity. The finer names are recorded here and nowhere else.
    "misconceptions": [
        {"id": "MIX-08",
         "statement": "The water has gone. It evaporated, so it is not "
                      "anywhere any more.",
         "elicited_by": "think-commit-water",
         "confronted_by": "think-commit-water"},
        {"id": "MIX-09",
         "statement": "Faster evaporation gives more product.",
         "elicited_by": "crystallising-bench",
         "confronted_by": "crystallising-bench"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # ⊖ Design draws ONE `.ks3-explainer` section carrying TWO paragraphs.
        # `r_explainer()` emits exactly one `<p>`, so this is authored as two
        # consecutive explainer blocks — same words, same order, same reading
        # measure, one extra section boundary. Reported to the commander: if
        # `r_explainer` grows a `paragraphs[]` key these collapse back to one.
        {"type": "explainer",
         "text": "<strong>Evaporation</strong> removes the solvent: it leaves "
                 "the solution as a gas and the solute stays behind. "
                 "<strong>Crystallisation</strong> is what the solute does as "
                 "it goes — once the solution is saturated, solute "
                 "particles start joining a growing, regular arrangement, and "
                 "that arrangement is a <strong>crystal</strong>."},
        {"type": "explainer",
         "text": "So the two words are not alternatives. Evaporation is the "
                 "thing you do; crystallisation is the thing the solute does "
                 "while you do it. How fast you do it decides what you get."},

        # #s-bench — the flagship. `class="ks3-block"` alone: LIGHT, so the
        # shell behind it is `check`, not `practical`. There is no ink-dark
        # practical block anywhere in C3.
        {"type": "crystal-bench", "id": "crystallising-bench",
         "anchor": "s-bench",
         "eyebrow": "Your turn · the crystallising bench",
         "heading": "Pick a solution and a way of removing the water. "
                    "Predict, then run it.",
         "demand": "investigate",
         "targets": "MIX-09",

         # Design's two dial labels, verbatim. No prose above them: §5 of the
         # brief forbids narrating controls, and the page narrates none.
         "dial_labels": {"solute": "The solution in the dish",
                         "method": "How you remove the water"},

         # The predict-gate. Nothing runs until a commitment is on record.
         "gate": {"prompt": "Before you run it: what will be left in the dish?",
                  "options": [
                      "A crust of crystals too small to pick up",
                      "A few crystals big enough to hold",
                      "Nothing — it will all go into the air",
                  ]},

         # `hard` is the warning printed on a BOIL run; `slow` is the crystal
         # description printed on a WINDOWSILL run. A water-bath run prints
         # neither and takes the method's hazard alone. Composition rule:
         #   boil -> solute.hard + " " + method.hazard
         #   sill -> solute.slow + " " + method.hazard
         #   bath -> method.hazard
         "solutes": [
             {"id": "salt", "name": "Salt solution", "colour": "#F3EDE1",
              "shape": "cube", "product": "sodium chloride cubes",
              "hard": "Some spitting as the last of the water boils off.",
              "slow": "Cubes with square faces and sharp edges."},
             # ⚑ Science flag 8 lives here, on the bench, and again in the
             # stretch layer. The two say the same thing and neither retracts
             # the other: stop heating a dish that has gone dry.
             {"id": "copper", "name": "Copper sulfate solution",
              "colour": "#2F5D8A", "shape": "diamond",
              "product": "blue copper sulfate crystals",
              "hard": "Over-heating turns the blue crystals into a white "
                      "powder. Keep the heat off the dry dish.",
              "slow": "Deep blue, angular, some over a centimetre across."},
             {"id": "alum", "name": "Alum solution", "colour": "#E6E2D8",
              "shape": "diamond", "product": "colourless alum crystals",
              "hard": "A fine crust rather than crystals, and it is hard to "
                      "lift out of the dish.",
              "slow": "Clear eight-sided crystals — the classic school "
                      "crystal-growing result."},
         ],

         # `size` is the drawn crystal's edge in px and `count` is how many are
         # drawn. They are the instrument's two variables and the only place
         # crystal size is stated as a quantity — the prose never quotes them.
         "methods": [
             {"id": "boil", "label": "Boil hard over a Bunsen",
              "time": "4 minutes", "size": 3, "count": 14,
              "quality": "A fine crust of tiny crystals",
              "note": "Every particle came out of solution at once, in a "
                      "hurry, wherever it happened to be. Thousands of "
                      "crystals started growing at the same moment and none "
                      "of them got big.",
              "hazard": "Hot solution spits as it dries. Safety glasses, and "
                        "never lean over the dish."},
             {"id": "bath", "label": "Warm gently over a water bath",
              "time": "35 minutes", "size": 9, "count": 7,
              "quality": "Small, clear, well-formed crystals",
              "note": "Slow enough for the solute to join a growing "
                      "arrangement in order, fast enough to finish in a "
                      "lesson. This is the compromise a school practical is "
                      "built around.",
              "hazard": "A water bath cannot go above 100 °C, so nothing "
                        "spits and nothing scorches."},
             {"id": "sill", "label": "Leave on a windowsill",
              "time": "6 days", "size": 26, "count": 3,
              "quality": "Large, regular crystals",
              "note": "A few crystals started, and every particle that came "
                      "out of solution afterwards joined one of them. Nothing "
                      "was hurried, so nothing was disordered.",
              "hazard": "No hazard, and no way to finish it inside a lesson."},
         ],

         # Where the bench opens. Copper sulfate over a water bath is the run
         # a school actually does, so the resting state is a real practical.
         "start_solute": "copper",
         "start_method": "bath",

         "readout_labels": {"time": "Time taken",
                            "quality": "What is in the dish",
                            "mass": "Mass of solute recovered"},

         # ⚖️ ONE STRING, FOR ALL NINE RUNS. See the module docstring. This is
         # the lesson, expressed as structure rather than as a sentence.
         "recovered_mass": "5.0 g",

         # Design's declared prop `showTimings` (NOTES §6), default on. With it
         # off, the time readout reads `timings_hidden` instead of the method's
         # time — the front-of-class setting for asking a class to estimate.
         "show_timings": True,
         "timings_hidden": "not shown",

         "dish_caption": "In the evaporating dish",

         # The alt text is COMPOSED, never authored finished: `{count}` and
         # `{product}` come from the current run and `{size_words}` from the
         # first threshold the method's `size` clears, strictly greater than.
         "dish_alt": {
             "template": "An evaporating dish holding {count} {product}, "
                         "drawn {size_words}.",
             "size_words": [[20, "large and regular"],
                            [6, "small and even"],
                            [0, "as a fine crust of very small crystals"]]},

         # `{method}` is the method's label, lower-cased.
         "run_label": "Run it · {method}",

         # Shown once all three METHODS have been run, on any solutes. This is
         # the confrontation half of MIX-09 and it names the trade directly.
         "summary": "All three methods, and the mass of solute recovered was "
                    "the same every time. Only the crystals changed. "
                    "<strong>Speed does not buy you more product — it "
                    "costs you the quality of it.</strong>"},

        {"type": "key-fact", "ref": "slow-grows-large"},

        # ⊕ #s-words. Design drew no words section on this page — c3-01,
        # c3-02 and c3-05 have one because she drew those — so the block goes
        # in and the RAIL IS NOT TOUCHED. `terms` matches `vocabulary[].term`
        # byte for byte; a term that does not resolve is dropped silently.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each "
                 "card over. If you cannot say it, you do not "
                 "know it yet.",
         "terms": ["Evaporation", "Crystallisation", "Crystal", "Solute",
                   "Solvent"]},

        # #s-jobs — `class="ks3-block"` alone: LIGHT, shell `check`.
        # Three decisions, each revealed on commitment. NOTHING IS MARKED
        # here — §5 of the brief: only the mastery ladder marks correctness.
        # Design's `JOBS` carries a `correct` field which her own page reads
        # NOWHERE, and it is deliberately not authored: R5 forbids a key with
        # no read site, and a renderer that read it would be marking an option
        # button. The method is named in `answer`, in prose, which is where a
        # student needs it.
        {"type": "method-choice", "id": "three-jobs", "anchor": "s-jobs",
         "eyebrow": "Three jobs · pick the method",
         "heading": "Same equipment, three different things wanted",
         "demand": "classify",
         "prompt": "Commit to a method for each, then read what actually "
                   "happens. One of the three cannot be done this way at all.",
         "options": [
             {"id": "boil", "label": "Boil it dry"},
             {"id": "sill", "label": "Slow evaporation"},
             {"id": "none", "label": "Evaporation is wrong for this"},
         ],
         "items": [
             {"id": "j1",
              "task": "A geologist has rock salt dissolved and filtered, and "
                      "needs the salt back today to weigh it.",
              "answer": "Warm it gently — or boil it, if all you need is "
                        "the mass.",
              "why": "Nobody is looking at these crystals; the answer is a "
                     "number on a balance. Speed is free here, and a crust "
                     "weighs the same as a cube."},
             {"id": "j2",
              "task": "A student wants one large, sharp copper sulfate "
                      "crystal to keep.",
              "answer": "Leave it to evaporate slowly. Days, not minutes.",
              "why": "Big crystals are made of time. Boiling gives a powder, "
                     "and heating a dry dish of copper sulfate turns it white "
                     "and ruins it."},
             # j3 is the one that cannot be done this way, and it is the hinge
             # into the next lesson rather than a trick.
             {"id": "j3",
              "task": "A village needs the fresh water out of a barrel of sea "
                      "water. The salt can be thrown away.",
              "answer": "Not this method at all. Evaporation keeps the solid "
                        "and loses the liquid.",
              "why": "Here it is the water that is wanted, and evaporation "
                     "sends the water into the air. You need to catch it as "
                     "it comes off — which is distillation, in the next "
                     "lesson."},
         ]},

        {"type": "misconception", "id": "think-commit-water",
         "anchor": "s-think", "targets": "MIX-08"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box ────────────────────────────────────────────────────
    "key_facts": [
        {"id": "slow-grows-large",
         "text": "Evaporating the solvent leaves the solute behind. The "
                 "slower the solvent goes, the larger and more regular the "
                 "crystals — and the solvent itself is lost to the air, "
                 "so this method keeps the solid and throws the liquid away.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── vocabulary (Law 7) ──────────────────────────────────────────────────
    # `Solute` and `Solvent` keep c3-02's definitions unchanged and take this
    # lesson's notes: one definition per word across the unit, and the note is
    # where the lesson does its own work. The pair is on the list because this
    # lesson's whole point is which of the two you keep.
    "vocabulary": [
        {"term": "Evaporation",
         "definition": "Removing the solvent by letting it leave as a gas, "
                       "so the solute is left behind.",
         "note": "It keeps the solid and loses the liquid."},
        {"term": "Crystallisation",
         "definition": "Solute particles joining a growing, regular "
                       "arrangement as the solution loses its solvent.",
         "note": "Evaporation is what you do; crystallisation is what the "
                 "solute does while you do it."},
        {"term": "Crystal",
         "definition": "A solid whose particles sit in a regular repeating "
                       "arrangement, giving it flat faces and sharp edges.",
         "note": "The slower it grows, the larger and more regular it is."},
        {"term": "Solute",
         "definition": "The substance that dissolves.",
         "note": "This is the one evaporation keeps, and you get all of it "
                 "back however fast you work."},
        {"term": "Solvent",
         "definition": "The liquid the solute dissolves in.",
         "note": "This is the one evaporation throws away — into the air, "
                 "with no way of getting it back."},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # Hand-authored predicts only. `_normalise()` lifts the two instruments out
    # of `core` and appends them to this list.
    "activities": [
        {"id": "think-commit-water",
         "kind": "predict",
         "demand": "explain",
         "targets": "MIX-08",
         # The drawn quote, so the block leads with the wrong idea in a
         # student's own words rather than the register's summary of it.
         "statements": [
             {"quote": "The water has gone. It evaporated, so it is not "
                       "anywhere any more."},
         ],
         "prompt": "The dish is dry and you can see it is dry. Commit before "
                   "you read on.",
         "options": [
             "Right — evaporating uses the water up, so it is not "
             "anywhere any more",
             "Wrong — it is in the air as a gas, and could be collected",
             "Wrong — heating turns the water into salt, so the "
             "crystals are the water itself",
             "Right, unless a lid traps it, because only water kept "
             "in the dish still exists",
         ],
         "reveal": [
             "The water is in the room. Its particles left the surface one at "
             "a time and joined the air, and they are still water — the "
             "same particles, the same mass, spread out where you cannot see "
             "them. Hold something cold above a warm dish and they come back "
             "as liquid on it, which is the whole of the next lesson.",
             # ⚑ THE CROSS-REFERENCE TO PART-05, student-facing and rendered.
             "This is the same wrong idea as \"the puddle dried up and the "
             "water was destroyed\", met in the particle model and met again "
             "here. Evaporation is a <strong>change of state</strong> and a "
             "change of place. It destroys nothing. The only reason it feels "
             "like a loss is that this method deliberately throws the solvent "
             "away.",
         ]},
    ],

    # ── the mastery ladder (Law 8) ──────────────────────────────────────────
    # Rungs 1 and 2 from Design's RUNGS, 3 and 4 from SELF_RUNGS. All four take
    # the engine's default titles — Recall, The one that catches people,
    # Explain, Take it somewhere new — which is what her page prints, so no
    # `title` override is authored.
    "ladder": {
        "recall": {
            "q": "A salt solution is left in an open dish until the dish is "
                 "dry. What is left, and what happened to the rest?",
            "options": [
                "The salt is left; the water was destroyed",
                "The water is left; the salt evaporated",
                "The salt is left; the water evaporated into the air",
                "Nothing is left; both go into the air",
            ],
            "answer": 2,
            "feedback": {
                0: "Nothing is destroyed by evaporation. The water is in the "
                   "air as a gas, and could be collected on a cold surface.",
                1: "The solute stays. Salt does not evaporate at anything "
                   "like these temperatures.",
                3: "Only the solvent leaves. Weigh the dish afterwards and "
                   "the salt is there to the gram.",
            }},
        "apply": {
            "q": "Two students crystallise identical solutions. One boils "
                 "hers dry in four minutes; the other leaves his for a week. "
                 "What is the difference in what they get?",
            "options": [
                "A smaller mass of solid for her, because boiling drives some "
                     "of it off with the steam",
                "The same mass of solid, but hers is a crust of tiny crystals "
                "and his is a few large ones",
                "A larger mass of solid for him, because evaporating "
                "slowly wastes less of it than boiling does",
                "The same mass of solid, and the same crystals too, "
                "because the method changes only the waiting",
            ],
            "answer": 1,
            "feedback": {
                0: "The mass is the same. The solute cannot leave the dish "
                   "and cannot be destroyed by a Bunsen.",
                2: "Efficiency is not the variable. Every gram of solute "
                   "stays in the dish either way; only the crystal size "
                   "changes.",
                3: "The mass is the same and the crystals are not. Rate of "
                   "crystallisation sets crystal size.",
            }},
        "explain": {
            "q": "Explain, in terms of particles, why slow evaporation "
                 "produces larger crystals than fast boiling — and why "
                 "the mass of solid recovered is the same either way.",
            "field_label": "Your explanation",
            "placeholder": "When the solution becomes saturated…",
            "success": [
                "Says crystals form when the solution becomes saturated and "
                "solute comes out of solution.",
                "Says fast boiling starts a very large number of crystals at "
                "once, so each one stays tiny.",
                "Says slow evaporation starts only a few, and later particles "
                "join those, so they grow large.",
                "Says the particles have time to settle into a regular "
                "arrangement when it is slow.",
                "Says the mass is unchanged because all the solute stays in "
                "the dish however fast the solvent leaves.",
            ]},
        "produce": {
            "q": "A coastal village can boil sea water over a wood fire but "
                 "has no other equipment. They need drinking water. Explain "
                 "why evaporating the sea water in an open pan is exactly the "
                 "wrong thing to do, and what the smallest change to their "
                 "method would be.",
            "field_label": "Your answer",
            "placeholder": "Evaporation keeps the…",
            "success": [
                "Says evaporation keeps the solute and loses the solvent "
                "— here the solvent is what they want.",
                "Says an open pan sends the fresh water into the air and "
                "leaves salt in the pan.",
                "Says the water is not destroyed and could be caught as it "
                "comes off.",
                "Proposes catching the steam on a cold surface and collecting "
                "the drops — a lid, a sheet, a cold plate.",
                "Names the method, or describes it: condensing the vapour "
                "back to a liquid, which is distillation.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Evaporation removes the solvent as a gas and leaves the "
                "solute behind; crystallisation is the solute coming out of a "
                "saturated solution into a regular arrangement. Fast boiling "
                "starts thousands of crystals at once and gives a fine crust; "
                "slow evaporation starts a few and grows them large. The mass "
                "recovered is the same either way — and the solvent is "
                "lost, so this method is only for keeping the solid.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Design draws ONE `.ks3-layer` with two paragraphs; `r_layer` renders a
    # list of blocks, so this is two explainers inside one "Going further".
    "stretch": [
        # ⚑ Science flag 9. "Metres long" is kept unnumbered on purpose: the
        # largest Naica beams are about 11–12 m, so the claim is true and
        # conservative, and it does not have to be revised if a longer one is
        # measured. Cave temperature 58 °C, hundreds of thousands of years.
        {"type": "explainer", "id": "salt-pans-and-naica",
         "text": "Slow crystallisation has been running for far longer than "
                 "anyone's windowsill. Salt pans around the Mediterranean "
                 "flood a shallow bed with sea water, let the sun take the "
                 "water over weeks, and rake up crystals — the same "
                 "process, at the scale of a field. Under Naica in Mexico, a "
                 "cave of gypsum crystals grew in mineral-rich water at a "
                 "steady 58 °C for hundreds of thousands of years; the "
                 "largest beams are metres long. Nothing exotic happened. It "
                 "was simply slow for a very long time."},
        # ⚑ Science flag 8, and the ruling is KEEP. Water of crystallisation
        # is named a year early, in the stretch layer, because it is the
        # honest explanation of the white powder the bench prints a warning
        # about — and an unexplained warning teaches nothing. The claim that
        # cooling cannot undo it is correct at this level: the water has left
        # the dish, and re-hydrating needs water added back, not cooling.
        {"type": "explainer", "id": "copper-sulfate-goes-white",
         "text": "One warning about heating crystals you have just grown. "
                 "Copper sulfate crystals are blue because water is built "
                 "into the crystal itself, and heating them hard drives it "
                 "out and leaves a white powder. The substance is still "
                 "there, but the crystals are gone and cannot be undone by "
                 "cooling. It is a good reason to stop heating a dish while "
                 "there is still liquid in it and let the last of it go on "
                 "its own."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # Design prints the per-run hazard on the bench rather than a page-foot
    # callout, so this is the one line the bench cannot carry: the general
    # rule, not the run-specific warning.
    "safety_note": "Evaporating to dryness over a naked flame spits hot "
                   "solution. Safety glasses, a gentle flame, and take the "
                   "heat away while there is still liquid in the dish rather "
                   "than baking it dry.",

    # ── end matter ──────────────────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why slow evaporation gives bigger "
                      "crystals?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    "ks4_becomes": "Crystallisation as a required practical step in making a "
                   "soluble salt, and hydrated versus anhydrous compounds.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
