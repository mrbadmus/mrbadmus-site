"""C3 L3 — Filtration (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c3/c3-03-filtration.dc.html` (686 lines), and her
author's notes `docs/ks3/design-reference/c3/NOTES-C3.md` §1, §2, §3.3, §4
flags 6 and 7, §5 (`MIX-06`, `MIX-07`) and §6.

Every student-facing string is byte-identical to the approved page. `RAIL`,
`STEPS`, `RUNGS`, `SELF_RUNGS` and `SHUFFLED` came out of the node extractor;
the hook options and reveal, the residue/filtrate explainer, the pour-gate
options, the all-steps summary, both report templates, the two particle panels,
the key fact, the `#s-think` options and its two reveal paragraphs, the key
note and both "Going further" paragraphs were lifted from `lessonVals(s)` and
from the markup, which is where roughly 900 of this lesson's words live and
where a lift of the top-level constants alone loses them.

── The five steps are ONE payload, used twice ──────────────────────────

Design draws the same five steps in two sections: `#s-steps` watches them one
at a time with a reason for each, and `#s-build` shuffles the same five and
asks for them back in order. That is one instrument kind (NOTES §3.3,
`sequence-rebuild`) in two phases, and `_STEPS` below is one Python object
referenced by both blocks — so the two can never drift apart, and no step
string is typed twice.

⚠️ WRONG ORDERS ARE ANSWERED WITH CONSEQUENCES, NEVER WITH MARKS. The
`tooSoon` string per step is the whole mechanism (NOTES §3.3), and the report
templates below quote it. Nothing green and nothing red may reach a step
button: only the mastery ladder marks correctness.

── The particle panels are the load-bearing figure of the unit ─────────

NOTES §2: the particle-scale panel "is why no filter can hold back salt".
Design draws it in markup — two DOM panels of circles either side of a
dashed filter-paper rule — and NOTES §6 declares no figure for this lesson,
so it is authored here as a `drawn` figure whose whole content is in `data`:
the panel labels, every dot's colour and diameter in the order Design places
them, and the sentence under each. The commander registers the drawer
`particle-panels` in `ks3_art/c3.py`; the `desc` below is Design's own
`role="img"` label, byte-identical.

The page's closing paragraph sits directly under those panels and describes
exactly what they show, so it is the figure's caption rather than a separate
explainer — that keeps it attached to the drawing it explains.

⚑ For Mide's science gate, from Design's NOTES §4:
  * flag 6 — filter paper as a FIBRE TANGLE rather than a sieve, retaining
    particles smaller than its widest gap, and slow filtration being cleaner
    filtration. KEPT, in `stretch` and byte-identical. It is the honest
    version and it is what makes "pouring too fast pushes them through"
    true rather than a rule about patience.
  * flag 7 — reverse osmosis desalination at 3-4 kWh per cubic metre. The
    approved page states RO, the enormous pressure and the expense and quotes
    NO figure at all, so there is no number in these two files to keep or
    change. Nothing was added: a number Design did not write would be new
    science-bearing prose in a lifted paragraph. Flagged to the commander.
  * MIX-06's lab-safety line is authored as `safety_note` — small, at the
    foot, alongside the standing legal line, and NOT a callout.
"""

# ── the five steps (NOTES §3.3) ─────────────────────────────────────────
#
# One object, referenced by BOTH `sequence-rebuild` blocks below. `short` is
# the shuffled bank button and the word the wrong-order report quotes; `title`
# is the step line in the worked stepper and in the order the student builds;
# `detail` and `why` are the two paragraphs a revealed step opens; `tooSoon`
# is the consequence on the bench, and it is written to read after the step's
# own name in the report template — "you did X too early: <tooSoon>".
_STEPS = [
    {"id": "fold",
     "short": "Fold the paper",
     "title": "Fold the circle of filter paper into a cone.",
     "detail": "In half, in half again, then open one side out so it makes a "
               "cone with three thicknesses on one side and one on the other.",
     "why": "A cone fits the funnel. A flat disc laid in the funnel leaves "
            "gaps at the edge, and the mixture runs round it.",
     "tooSoon": "nothing goes wrong — but you fold the paper before "
                "doing anything else, so this is where it belongs."},
    {"id": "seat",
     "short": "Seat and wet it",
     "title": "Sit the cone in the funnel and wet it with a little distilled "
              "water.",
     "detail": "A few drops, then press the paper gently against the glass.",
     "why": "Wet paper clings to the funnel. Dry paper lifts as the mixture "
            "arrives, and the mixture runs down the gap unfiltered.",
     "tooSoon": "you wet the paper before it was in the funnel, so it tore as "
                "you tried to seat it and you started again with a new one."},
    {"id": "stand",
     "short": "Stand the funnel in the flask",
     "title": "Stand the funnel in a conical flask, with its tip touching the "
              "inside wall.",
     "detail": "The stem should reach inside the flask, not hover above it.",
     "why": "Touching the wall stops the filtrate splashing back up into the "
            "paper, and stops drops running down the outside of the flask.",
     "tooSoon": "the funnel was standing in the flask with no paper in it, so "
                "the mixture went straight through and you had to pour it "
                "back and start again."},
    {"id": "pour",
     "short": "Pour down a rod",
     "title": "Pour the mixture down a stirring rod, keeping the level below "
              "the rim of the paper.",
     "detail": "The rod touches the paper on the three-thickness side. Fill "
               "to about two thirds of the paper, no higher.",
     "why": "Poured straight from the beaker it splashes over the rim, and "
            "anything that goes over the rim has not been filtered.",
     "tooSoon": "you poured before the paper and funnel were ready, so the "
                "sand went into the flask with the water and the whole thing "
                "had to be done again."},
    {"id": "rinse",
     "short": "Wait, then rinse",
     "title": "Let it drip through, then rinse the residue with a little "
              "distilled water.",
     "detail": "Do not squeeze or poke the paper. Rinsing washes the last of "
               "the filtrate out of the sand.",
     "why": "Squeezing tears the paper and lets the residue through. Rinsing "
            "matters when you want a clean residue — otherwise it dries "
            "with dissolved substances in it.",
     "tooSoon": "you rinsed before there was anything in the paper, which "
                "just wet the paper again and told you nothing."},
]

# ── the particle section's head ─────────────────────────────────────────
#
# Design's own eyebrow and headline for the panels section. Held as constants
# because they are needed in TWO places and must never come apart: the `rule`
# block that renders the head, and the figure's `data`, so that the commander
# can fold the head into the drawer instead and delete the rule block without
# re-reading the page. One string either way.
_PANEL_EYEBROW = "Why it works · and why it cannot work on salt"
_PANEL_HEADING = "The holes in the paper are the whole story"

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 200 character for character.
    "slug":        "filtration",
    "title":       "Filtration",
    "discipline":  "chemistry",
    "unit":        "mixtures-and-separation",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # NOTES §1 gives this lesson `KS3.C.PIS.04`, and so do c3-04, c3-05 and
    # c3-06 — the bullet names four techniques and the unit gives each one a
    # lesson. `validate()` rule 4 owns a statement exactly once, so the parent
    # was authored here first and the four clauses were minted mid-run in
    # `ks3_data/substatements.py` (MRB-272, the commander's file). This is
    # clause `a`, filtration: separating an insoluble solid from a liquid.
    "covers":      ["KS3.C.PIS.04a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 3},
                    {"id": "substances-and-reactions", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # The page's "Before this lesson" card links to c3-02; the whole size
    # argument needs "dissolved" to already mean something.
    "requires":    ["dissolving-and-solutions"],
    "assumes":     [],
    "references":  ["pure-or-mixture"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Getting sand out of water takes one piece of paper. "
                    "Getting salt out of water cannot be done with any paper "
                    "at all — and the reason is a matter of size.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops (NOTES §6). `done_when` restates the page's own DONE(): the
    # hook on a commitment, the stepper when all five are open, the rebuild
    # when five have been placed, `#s-think` on a commitment, the ladder when
    # every rung is answered and both self-marked rungs checked.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",  "label": "Sand and salt",
         "done_when": "committed"},
        {"anchor": "s-steps",  "short": "STEPS", "label": "Watched first",
         "done_when": "all_steps_opened"},
        {"anchor": "s-build",  "short": "BUILD", "label": "Your sequence",
         "done_when": "order_complete"},
        {"anchor": "s-think",  "short": "THINK", "label": "Clear water",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # `kind` is unread by the generator (it dispatches on which media key is
    # present) and is authored for consistency with C1 and C2.
    "phenomenon": {
        "kind": "narrative",
        "title": "Two beakers of water. One has sand in it, one has salt. The "
                 "same filter paper is about to meet both.",
        "prompt": "Stir a spoon of sand into the first: it goes cloudy and "
                  "the grains settle. Stir a spoon of salt into the second: "
                  "it goes clear and stays clear. Pour each through a filter "
                  "paper.",
        "commit": "What is left in the two filter papers afterwards?",
        "options": [
            "Sand in one paper, salt in the other",
            "Sand in one paper, nothing in the other",
            "Nothing in either — both pass through",
            "Sand in one, and the other paper turns salty but stays empty",
        ],
        "reveal": "Sand in the first paper. Nothing at all in the second "
                  "— the salt went straight through with the water and "
                  "is still in the liquid underneath, exactly as it was. "
                  "<strong>Filtration separates an insoluble solid from a "
                  "liquid, and never separates anything dissolved.</strong> "
                  "That one sentence is the whole lesson; the rest is how to "
                  "do it without ruining it.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ MIX-06's `statement` is the page's quoted line, not NOTES §5's
    # register wording ("Filtered water is clean water."). `r_confrontation`
    # prints `statement` as the `#s-think` quote, and Design's line is the one
    # that must render — the same reconciliation c2-03 made for ATOM-07, and
    # for the same reason. The register wording is the shorter handle; the
    # page's is what a student says out loud.
    "misconceptions": [
        {"id": "MIX-06",
         "statement": "I filtered the pond water and it came out clear, so it "
                      "is clean water now.",
         "elicited_by": "think-commit-pond",
         "confronted_by": "think-commit-pond"},
        {"id": "MIX-07",
         "statement": "A fine enough filter would separate salt from water.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-particles"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page line 105 — the two words the rest of the lesson uses.
        {"type": "explainer",
         "text": "The solid caught in the paper is the "
                 "<strong>residue</strong>. The liquid that comes through is "
                 "the <strong>filtrate</strong>. Both are worth keeping "
                 "— which one you actually want depends on what you are "
                 "doing."},

        # #s-steps — phase one of the flagship. Light `ks3-block` → `check`.
        {"type": "sequence-rebuild", "id": "filter-steps", "anchor": "s-steps",
         "phase": "watch",
         "eyebrow": "Watched first · five steps",
         "heading": "Filtering sand out of water",
         "demand": "investigate",
         "prompt": "Each step has a reason. Reveal them one at a time — "
                   "and there is a prediction to make before you pour.",
         "steps": _STEPS,
         "reveal_label": "Show step {n}",
         # Design's `requirePourPrediction` prop, default true (page line 405).
         # The gate blocks the step whose id is named, and nothing else: it is
         # a commitment about where the SALT goes, made before the pour makes
         # it observable.
         "require_prediction": True,
         "gate": {"after": "pour",
                  "prompt": "Before you pour: where does the salt beaker's "
                            "salt end up?",
                  "options": [
                      "In the paper, with the sand",
                      "Through the paper, in the flask",
                      "Half in the paper, half through",
                  ]},
         # ⚠️ The paper has just had salt water poured through it, so it is
         # WET, and when it dries it carries a faint salt residue — which is
         # exactly what a real class observes (C3-08, chem audit 25 Aug
         # 2026). "Clean, dry, empty" was false in the moment and the honest
         # core of the sentence never needed it.
         "summary": "Sand in the paper, water in the flask — and in the "
                    "other beaker, salt water in the flask and a filter "
                    "paper with nothing caught in it at all. Nothing was "
                    "removed from the salt water at all."},

        # #s-build — phase two, the same five steps. Light `ks3-block` → `check`.
        {"type": "sequence-rebuild", "id": "filter-rebuild", "anchor": "s-build",
         "phase": "rebuild",
         "eyebrow": "Your turn · build the same sequence",
         "heading": "Same five steps, shuffled. Put them in order.",
         "demand": "construct",
         "prompt": "Tap them in the order you would do them. Nobody is "
                   "marking this — you will simply be told what happened "
                   "on the bench as a result.",
         "steps": _STEPS,
         # Design's fixed bank order (page line 456): indices into `steps`.
         # Fixed rather than randomised so the lesson is the same lesson in
         # every room, and so a teacher can talk about "the third button".
         "shuffled": [3, 0, 4, 2, 1],
         "clear_label": "Clear and start again",
         # ⚠️ TEMPLATES, NOT SENTENCES. The step number, the step's own `short`
         # and its `tooSoon` are all computed by the instrument from the order
         # the student built; §6 forbids hard-coding any of them here. `{when}`
         # resolves to `when.early` or `when.late` — the report says which
         # direction the step moved, because "step 3 is wrong" teaches nothing
         # and "you stood the funnel in the flask too early" teaches the
         # dependency.
         "report": {
             "right_title": "That is the order, and here is what came out.",
             "right_text": "Paper folded, seated and wet, funnel standing in "
                           "the flask, mixture poured down the rod below the "
                           "rim, then rinsed. Clean sand in the paper, clear "
                           "filtrate in the flask, nothing spilled. Every "
                           "step you did was protecting the step after it.",
             "wrong_title": "It ran, but look at what happened at step {n}.",
             "wrong_text": "You did \"{short}\" {when}: {too_soon} The order "
                           "that works is the one you were shown — fold, "
                           "seat and wet, stand in the flask, pour down the "
                           "rod, rinse.",
             "when": {"early": "too early", "late": "too late"},
         }},

        # The particle section's head. Design draws a plain `ks3-block` with an
        # eyebrow and an h2; the closed block vocabulary has no light block
        # that carries a headline and nothing else, and `rule` is the one that
        # carries an eyebrow above a statement. If the commander would rather
        # the drawer emitted the head, both strings are already in the figure's
        # `data` and this block can go.
        {"type": "rule",
         "eyebrow": _PANEL_EYEBROW,
         "statement": _PANEL_HEADING},

        # The anchor is what lets MIX-07 name the thing that actually
        # confronts it (MRB-244). Design draws no id here; an id is
        # invisible to a student and the page is silent on it.
        {"type": "figure", "ref": "particle-panels",
         "anchor": "s-particles"},

        {"type": "key-fact", "ref": "no-filter-for-dissolved"},

        # ⊕ #s-words. c3-01, c3-02 and c3-05 carry a words section BECAUSE
        # DESIGN DREW ONE and put a stop on the rail for it. She drew none
        # here, so the block goes in and the RAIL IS NOT TOUCHED — five stops
        # in, five stops out. `terms` matches `vocabulary[].term` byte for
        # byte; `r_keyword` drops a term it cannot resolve, silently.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each "
                 "card over. If you cannot say it, you do not "
                 "know it yet.",
         "terms": ["Filtration", "Residue", "Filtrate", "Insoluble",
                   "Dissolved"]},

        {"type": "misconception", "id": "think-commit-pond", "anchor": "s-think",
         "targets": "MIX-06"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the figure (§5.4) ───────────────────────────────────────────────────
    # NOTES §2: THE load-bearing figure of the unit. DOM circles, not canvas
    # (NOTES §6). `dots` is (colour, diameter in px) in Design's own order —
    # one grain drawn as three big sand-coloured lumps, dissolved salt as eight
    # small particles alternating sodium-blue and chloride-orange, in the
    # 10/7/10/10/7/10/10/7 sequence she places them in. The dashed rule between
    # the dots and the text is the paper: `--ks3-rule-strong` dashes 9px on,
    # 6px off, ink 2px top and bottom.
    "figures": [
        {"id": "particle-panels",
         "kind": "diagram",
         "status": "drawn",
         "art": "particle-panels",
         "title": _PANEL_HEADING,
         # ⊕ MRB-272 — THE DRAWER COMPOSES THE REAL `desc`, AND THIS ONE WAS
         # DESCRIBING A DIFFERENT DRAWING. It said "two particle diagrams
         # either side of a filter paper", sand above and salt below; Design
         # draws TWO SIDE-BY-SIDE PANELS, each with its own paper. MRB-254 is
         # explicit that a `<desc>` describes what is ACTUALLY DRAWN, and that
         # shipping a knowingly false one because it is the designer's is the
         # wrong reading of MRB-205 — three of the twelve biology figures did
         # exactly that.
         #
         # `r_particle_panels` walks the plate in reading order and builds a
         # ~1,600-character description from the REAL counts, diameters and
         # gap, then passes `dict(fig, desc=…)` to `_svg_open`. So this key is
         # overridden on every build and cannot reach a student. It is kept,
         # short and true, only as the fallback any future non-drawing path
         # would take.
         "desc": "Two panels side by side, each showing particles above a "
                 "filter paper drawn as a dashed line. On the left, sand: "
                 "clumps far wider than the gaps, all held above the paper. "
                 "On the right, dissolved salt: single particles smaller "
                 "than the gaps, three of them drawn below the paper having "
                 "passed straight through.",
         "caption": "A grain of sand is a lump of many millions of particles "
                    "stuck together, thousands of times wider than the gaps "
                    "between the paper's fibres. A dissolved salt particle is "
                    "on its own, and it is smaller than the gap by more than "
                    "the gap is smaller than the grain. There is no filter "
                    "paper that stops one and passes the other.",
         "data": {
             "eyebrow": _PANEL_EYEBROW,
             "heading": _PANEL_HEADING,
             "colours": {"sand": "#9C8F62", "blue": "#2F5D8A",
                         "orange": "#E4572E"},
             "panels": [
                 {"label": "A grain of sand",
                  "dots": [("sand", 26), ("sand", 22), ("sand", 30)],
                  "text": "Millions of particles stuck together in one lump, "
                          "thousands of times wider than the gaps. It cannot "
                          "get through, and it does not."},
                 {"label": "Dissolved salt",
                  "dots": [("blue", 10), ("orange", 7), ("blue", 10),
                           ("blue", 10), ("orange", 7), ("blue", 10),
                           ("blue", 10), ("orange", 7)],
                  "text": "Single particles, mixed among the water particles "
                          "and far smaller than the gaps. They go wherever "
                          "the water goes."},
             ],
         }},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "no-filter-for-dissolved",
         "text": "Filtration separates an insoluble solid from a liquid. The "
                 "solid left in the paper is the residue; the liquid through "
                 "it is the filtrate. Anything dissolved goes straight "
                 "through.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── vocabulary (Law 7) ──────────────────────────────────────────────────
    # `Insoluble` takes c3-02's definition unchanged — one definition, two
    # lessons, no second copy free to drift — and only the note is this
    # lesson's. `Dissolved` is the word the whole size argument turns on and
    # the page never stops for it.
    "vocabulary": [
        {"term": "Filtration",
         "definition": "Separating an insoluble solid from a liquid by "
                       "pouring the mixture through filter paper.",
         "note": "It never separates anything dissolved, however fine the "
                 "paper is."},
        {"term": "Residue",
         "definition": "The solid left behind in the filter paper.",
         "note": "In sand and water, that is the sand."},
        {"term": "Filtrate",
         "definition": "The liquid that passes through the filter paper.",
         "note": "Clear is not the same as pure. Everything dissolved is "
                 "still in it."},
        {"term": "Insoluble",
         "definition": "Will not dissolve in that solvent.",
         "note": "An insoluble solid stays in lumps, and lumps are what a "
                 "filter can catch."},
        {"term": "Dissolved",
         "definition": "Broken up into single particles, spread evenly "
                       "through the liquid.",
         "note": "Far smaller than any gap in the paper, so it goes wherever "
                 "the water goes."},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two `sequence-rebuild` blocks are lifted out of
    # `core` into this list by `_normalise()` and are never authored here.
    "activities": [
        {"id": "think-commit-pond",
         "kind": "predict",
         "demand": "explain",
         "targets": "MIX-06",
         "prompt": "It went in murky and came out clear. Commit before you "
                   "read on.",
         "options": [
             "Right — once water is clear, whatever was harmful in it "
             "has been removed",
             "Wrong — everything dissolved is still in it, including "
             "things that could harm you",
             "Right, if you filter it twice, because a second pass "
             "catches what the first missed",
             "Wrong — the paper sheds fibres as the water passes, so "
             "it comes out dirtier",
         ],
         "reveal": [
             "Clear means the bits you could see are gone. Everything "
             "dissolved is still there — and so is almost everything "
             "dangerous. Bacteria are far smaller than the mud you removed "
             "and most of them pass through filter paper without noticing it. "
             "Dissolved lead, nitrate and pesticide are single particles and "
             "pass straight through.",
             "A water treatment works does filter — and then it settles, "
             "adds chemicals to clump the fine particles, filters again "
             "through sand, and finally kills what is left with chlorine or "
             "ultraviolet light. <strong>Filtration is one step of several, "
             "and it is the step that deals with the least dangerous thing in "
             "the water.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce. Her rung
    # labels are the engine's own defaults character for character ("Recall",
    # "The one that catches people", "Explain", "Take it somewhere new"), so no
    # rung authors a `title`. `feedback` is keyed by the INT index of each
    # wrong option, which is what `_rung_marked` reads.
    "ladder": {
        "recall": {
            "q": "A sand and water mixture is filtered. What are the sand and "
                 "the water now called?",
            "options": [
                "The sand is the residue, the water is the filtrate",
                "The sand is the filtrate, the water is the residue",
                "Both are called the filtrate",
                "The sand is the solute, the water is the solvent",
            ],
            "answer": 0,
            "feedback": {
                1: "The other way round. The filtrate is what filters "
                   "through; the residue is what is left behind.",
                2: "Only the liquid that passes through the paper is the "
                   "filtrate.",
                3: "Those words are for dissolving. Sand does not dissolve "
                   "— that is why it can be filtered.",
            }},
        # ⚑ This is `rung-2-filter`: NOTES §5's elicitation site for MIX-07.
        "apply": {
            "q": "A student cannot separate salt from water with a filter and "
                 "asks for finer filter paper. What should you tell them?",
            "options": [
                "No paper will do it — the dissolved salt particles are "
                "smaller than any gap in any paper",
                "A fine enough paper stops anything, so filtering out salt is "
                "a matter of the right grade",
                "Filtering twice removes what one pass missed, so a second "
                "pour would take the salt out",
                "Hot water passes through more easily, so heating it first "
                "would leave the salt behind",
            ],
            "answer": 0,
            "feedback": {
                1: "Fineness is not the problem. Dissolved particles are "
                   "single particles, thousands of times smaller than the "
                   "fibres — there is no paper fine enough.",
                2: "The salt passes through every time, because it is "
                   "dissolved. Pouring it through again changes nothing.",
                3: "Heating dissolves the salt more thoroughly, if anything. "
                   "It does not make the salt filterable.",
            }},
        "explain": {
            "q": "Sand and salt are both stirred into the same beaker of "
                 "water and the mixture is filtered. Explain exactly what is "
                 "in the filter paper and what is in the flask afterwards, "
                 "and how you know.",
            "field_label": "Your explanation",
            "placeholder": "In the paper there is…",
            "success": [
                "Says the sand is in the paper because it is insoluble, so it "
                "stays as visible lumps.",
                "Says the salt is in the flask, dissolved in the water.",
                "Explains it by size: the sand grains are far bigger than the "
                "gaps, the dissolved salt particles are far smaller.",
                "Says the liquid in the flask is a salt solution, not pure "
                "water.",
                "Gives a way to show the salt is there — taste, boil it "
                "dry, or weigh what is left.",
            ]},
        "produce": {
            "q": "A camping filter bottle claims to make river water safe to "
                 "drink. Using what you know about filtration, explain what "
                 "such a bottle can and cannot do, and what you would want to "
                 "know before trusting it.",
            "field_label": "Your answer",
            "placeholder": "A filter can remove…",
            "success": [
                "Says a filter removes insoluble solids — mud, grit, "
                "silt — and makes the water look clear.",
                "Says anything dissolved passes through, so clear does not "
                "mean safe.",
                "Names something dangerous a paper filter would not stop "
                "— bacteria, or a dissolved chemical.",
                "Says a real bottle must do something more, such as a "
                "membrane fine enough to hold back microbes or a chemical "
                "treatment.",
                "Asks a sensible question of the manufacturer — what "
                "size of particle it stops, or what it is tested against.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Filtration separates an insoluble solid from a liquid. The "
                "solid caught in the paper is the residue; the liquid that "
                "passes through is the filtrate. It works because the solid "
                "is in lumps far larger than the gaps in the paper — so "
                "anything dissolved, being single particles far smaller than "
                "those gaps, goes straight through. Clear is not the same as "
                "pure.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ Science flag 6 is the first paragraph and it is KEPT WHOLE. The fibre
    # tangle is what makes "a paper stops particles smaller than the widest gap
    # through it" true, and it is what makes the last sentence a mechanism
    # rather than a rule about patience. Shrinking it to "the holes are too
    # small" would be the famous version, not the true one.
    "stretch": [
        {"type": "explainer", "id": "fibre-tangle",
         "text": "A filter paper is not a sieve with holes in it. It is a "
                 "tangle of cellulose fibres, and a particle can be caught by "
                 "hitting a fibre, by sticking to one, or by being trapped in "
                 "a bend well below the surface — which is why a paper "
                 "stops particles smaller than the widest gap through it, and "
                 "why pouring too fast pushes them through anyway. Slow "
                 "filtration is cleaner filtration, and that is not a rule "
                 "about patience."},
        # ⚑ Science flag 7 lives here. Design quotes NO energy figure — RO,
        # enormous pressure, and expense. Nothing added; see the docstring.
        {"type": "explainer", "id": "reverse-osmosis",
         "text": "Nothing on this bench will take the salt out of sea water, "
                 "because the salt is dissolved and dissolved things go where "
                 "the water goes. The way round it is to move the water and "
                 "leave the salt behind — which is the next lesson but "
                 "one. Industry does have filters fine enough to hold back "
                 "dissolved particles: reverse osmosis membranes desalinate "
                 "sea water by forcing it through under enormous pressure. "
                 "They are not filter paper, and the pressure is the reason "
                 "they are expensive."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── safety (§1.5) — not a callout, and not a safeguarding block ─────────
    # ⚠️ NEW PROSE, and the only new prose in this file. The approved page
    # carries no foot line, and MIX-06 is a lesson about pond water that ends
    # with a camping bottle: the one thing a twelve-year-old might actually do
    # after reading it is drink something they have filtered. It renders as
    # `ks3-legal ks3-safety` — small, at the bottom edge, beside the standing
    # legal line. NOT a callout, and NOT a safeguarding block: this lesson is
    # about water, not about a student's own body or health.
    #
    # Scoped to pond and river water on purpose. A blanket "never taste
    # anything" would retract rung 3's own criterion, which credits tasting as
    # a way of showing dissolved salt is present, and §7 forbids a lesson
    # retracting itself later on the same page.
    "safety_note": "Filtered pond or river water is not drinking water. The "
                   "filter takes out what you could see and leaves everything "
                   "that could make you ill, so it is never tasted or drunk.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why no filter can hold back dissolved "
                      "salt?",
              "cta": "Ask about this lesson",
              "anchor": "s-build"},

    "ks4_becomes": "Choosing and justifying a separation method for a given "
                   "mixture, and required practicals where the technique "
                   "itself is assessed.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
