"""C5 L3 — Oxidation (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c5/c5-03-oxidation.dc.html` (624 lines), and her
author's notes `docs/ks3/design-reference/c5/NOTES-C5.md` §1, §2, §3, §4
flags 11-15, §5 (`REACT-14`, `REACT-15`) and §6.

Every student-facing string is byte-identical to the approved page. `RAIL`,
`TUBES`, `METHODS`, `RUNGS` and `SELF_RUNGS` came out of the node extractor;
the hook title, prompt, options and reveal, both explainer paragraphs, the
`#s-rust` heading and lede, the four-tube summary and its equation row, the
key fact, the `#s-stop` heading and lede, both sets of segment labels, the
`#s-think` options and its two reveal paragraphs, the key note and both
"Going further" paragraphs were lifted from `lessonVals(s)` and from the
markup, which is where most of this lesson's words live and where a lift of
the top-level constants alone loses them.

── THE SHAPE: a four-tube CONTROLLED INVESTIGATION, not a stepper ───────

NOTES-C5 §2 on this page: "a four-tube controlled investigation. Not a
stepper at all: the four results only mean something read together, and tubes
2 and 3 are the controls doing the work."

That is why `control-tubes` is one instrument holding four cards and ONE
summary, rather than four independent cards. A student may open the tubes in
any order and each opens on its own commitment, but the panel that states the
conclusion is gated on all four being decided — because the conclusion is not
available from any three of them. The rail stop ticks at the same moment, and
it is the same moment Design's `DONE('s-rust')` uses.

⚖️ THE CONTROL ARGUMENT IS ASSERTED IN THE RENDERER, NOT ONLY WRITTEN DOWN.
`ks3_art/c5.py`'s `r_control_tubes` derives which factors are REQUIRED from
the chips and the results — a factor is required if some tube removes it and
no tube that removes it rusts — and then checks every tube's `rust` against
that derived rule, and checks that each required factor has a tube isolating
it. So the summary paragraph below cannot outlive an edit that breaks the
evidence for it: flip a chip or a result and the build fails rather than
shipping a conclusion the four tubes no longer support (§5A).

`control-tubes` payload, per NOTES §3 — kept so that any later "what does
this experiment control?" lesson can take the same shape:

    {"tubes": [{"id", "name", "setup",
                "chips": [{"label", "on"}],
                "rust", "result", "why"}],
     "chip_labels": {"on": …, "off": …},
     "predict_options": [{"id", "label"}],
     "summary": {"title", "text", "equation": {"left", "right"}}}

`chips` is what makes the controlled variables visible at a glance, and it is
the array the assertion above reasons over. `preds: {}` is Design's runtime
state and belongs to the wiring, not to the record.

⚑ For Mide's science gate, from Design's NOTES §4 — ALL FIVE ALREADY RULED:
  * flag 11 — rust as "hydrated iron oxide", avoiding both iron(III) and a
    formula. CONFIRMED as the KS3 form and KEPT, in the summary's equation
    row and nowhere else. It is the other side of C4 flag 10: `c4-03` carries
    no rusting word equation at all, because the honest one needs water as a
    reactant, and this page is where the honest one is drawn — three
    reactants, and a product named rather than formulated. Nothing here
    asserts "iron + oxygen makes iron oxide", and no formula and no oxidation
    number appears anywhere in this lesson.

    ⚖️ RULED EXPLICITLY (MRB-246), because the instruction that produced this
    page could be read two ways and the author was right to ask. "Do not add
    an equation for rust" meant DO NOT INVENT ONE BEYOND DESIGN'S — it did not
    mean cut the one she drew. THE ROW STAYS.

    The two lessons are not in tension, they are a division of labour:
    `word-equations` leaves rust alone because a three-reactant equation is a
    complication a NOTATION lesson does not need and cannot afford, and THIS
    is the lesson where rust is the subject and the honest version belongs. A
    later pass that cuts this row citing c4-03 would be deleting the only
    correct statement of the reaction in the course, on the authority of a
    lesson that deliberately says nothing about it.
  * flag 12 — tube 3's "faintest trace where the oil did not quite seal".
    CONFIRMED and KEPT WHOLE, with Design's own gloss that "the faint trace is
    honest data, not a failure". A student shown only clean negatives learns
    that a real result is a failed one.
  * flag 13 — aluminium as MORE reactive than iron and protected by its own
    oxide. CORRECT and kept. Anodising stays out: it is a process, not a
    reason, and the reason is what `#s-think` is for.
  * flag 14 — sacrificial protection via "gives up its electrons first".
    ⚖️ RULED OUT, and re-authored below rather than deleted. See the note on
    `stretch` for the replacement sentence and the argument.
  * flag 15 — respiration as an oxidation. CORRECT, kept in the first "Going
    further" paragraph, and the cross-link is authored in `references` as a
    LESSON — it renders as "Aerobic respiration", which is that lesson's own
    title. No unit code reaches the page (§14).

── Where the misconception joins land (MRB-244 / MRB-248) ──────────────

Both joins resolve against markup this page really emits, and BOTH WERE
CHECKED AGAINST THE EMITTED MARKUP rather than against NOTES' proposal:

  REACT-14  elicited_by  `s-think`  → the section's own anchor id.
            confronted_by `think-reveal-oxide-layer` → `data-activity=…`, the
            commit-and-reveal activity in that section.

            ⚖️ ONE RENAME, AND IT IS REPORTED. NOTES §5 proposes
            `think-commit-aluminium` / `think-reveal-oxide-layer`.
            `build_ks3.py` emits a confrontation's reveal as
            `<div class="ks3-reveal ks3-reveal-panel" hidden data-reveal>`
            with NO id, so a `think-reveal-*` name cannot be made to resolve
            from inside a content lane — the register says so under `REACT`,
            in as many words. The mandatory key therefore keeps its register
            name and points at the ACTIVITY that owns BOTH the commitment and
            the reveal; the optional one names the section it happens in.
            That is exactly what `REACT-05` did in `c4-03`, and `MIX-06` in
            `c3-03` before it.

  REACT-15  elicited_by  `tube-predictions` → `data-activity="tube-predictions"`,
            the four-tube instrument. Committing "will rust" on tube 2 or
            tube 3 IS the belief, stated.
            confronted_by `four-tube-summary` → `id="four-tube-summary"`, the
            panel `r_control_tubes` emits on the summary itself. A figure or
            panel anchor is a legal target (§6), and the summary is honestly
            where this one is taken apart: it is the only place on the page
            that reads tubes 2 and 3 together.

Law 3 is satisfied by `REACT-14`, whose `confronted_by` is a real activity id.
"""

# ── the four tubes (Design's `TUBES`) ───────────────────────────────────
#
# ONE object, read by the instrument for every card, every chip and every
# result panel. `chips` is the controlled-variables row and it is DATA the
# renderer reasons over, not decoration: see the module docstring.
#
# ⚠️ `rust` REACHES NO MARKUP AND IS NOT DEAD. Design's own `lessonVals`
# never reads it either — the result sentence says what happened — but it is
# the ground truth the renderer's control assertion is checked against, and
# without it a chip could be flipped and the summary would keep claiming a
# conclusion the tubes no longer support.
#
# ⚑ Flag 12 lives in tube 3, whole: "No rust, or the faintest trace where the
# oil did not quite seal." Real controlled data is imperfect and the control
# argument is stronger for saying so.
_TUBES = [
    {"id": "t1",
     "name": "Air and water",
     "setup": "An iron nail half in tap water, tube open to the air.",
     "chips": [{"label": "Oxygen", "on": True},
               {"label": "Water", "on": True}],
     "rust": True,
     "result": "Rusted — orange and flaking at the water line.",
     "why": "Both requirements present. The worst of it is at the surface, "
            "where the nail meets air and water at once."},
    {"id": "t2",
     "name": "Dry air, no water",
     "setup": "A nail in a bunged tube with a drying agent to take all "
              "moisture out of the air.",
     "chips": [{"label": "Oxygen", "on": True},
               {"label": "Water", "on": False}],
     "rust": False,
     "result": "No rust. The nail is as shiny as the day it went in.",
     "why": "Oxygen on its own is not enough. This tube is the control that "
            "rules out air being the whole story."},
    {"id": "t3",
     "name": "Water, no air",
     "setup": "A nail in water that was boiled to drive out dissolved air, "
              "with a layer of oil on top to keep more out.",
     "chips": [{"label": "Oxygen", "on": False},
               {"label": "Water", "on": True}],
     "rust": False,
     "result": "No rust, or the faintest trace where the oil did not quite "
               "seal.",
     "why": "Water on its own is not enough either. Together with tube 2, "
            "this proves both are needed — and the faint trace is honest "
            "data, not a failure."},
    {"id": "t4",
     "name": "Salt water and air",
     "setup": "A nail half in salt water, tube open to the air.",
     "chips": [{"label": "Oxygen", "on": True},
               {"label": "Water", "on": True},
               {"label": "Salt", "on": True}],
     "rust": True,
     "result": "Rusted heavily — much worse than tube 1 in the same four "
               "weeks.",
     "why": "Salt is not a requirement; it is an accelerator. It is why cars "
            "rust faster near the coast and after a gritted winter."},
]

# ── the five ways to stop it (Design's `METHODS`) ───────────────────────
#
# ⚠️ `barrier` REACHES NO MARKUP EITHER, and it is Design's own flag. It
# marks the two methods for which "a barrier" is NOT the whole answer — the
# zinc blocks, which cover nothing at all, and the galvanised gate, whose
# answer opens "Both". The block's heading counts by what a method DOES, so
# the galvanised gate is one of the four that keeps oxygen and water out AND
# the second of the two doing something cleverer. Nothing on the page marks a
# button either way: the panel that opens is a panel of words, and only the
# ladder marks.
#
# ⚑ Flag 14's replacement wording is Design's own, and it is already here in
# `m5`: "corrodes in preference to the iron". The stretch paragraph was
# re-authored to say the same thing, so the lesson now has ONE account of
# sacrificial protection instead of two.
_METHODS = [
    {"id": "m1",
     "name": "Painting a bridge",
     "what": "A continuous film of paint over every exposed surface.",
     "barrier": True,
     "answer": "A barrier. It works only while it is unbroken — a chip in "
               "the paint is where the rust starts, and it then spreads "
               "underneath."},
    {"id": "m2",
     "name": "Oiling a bicycle chain",
     "what": "A thin film of oil, renewed regularly.",
     "barrier": True,
     "answer": "A barrier, and a deliberately temporary one. It has to be "
               "renewed because it wears off, which is why chains need "
               "oiling rather than painting."},
    {"id": "m3",
     "name": "Stainless steel cutlery",
     "what": "Iron mixed with chromium and nickel.",
     "barrier": True,
     "answer": "A barrier, made by the alloy itself: the chromium oxidises "
               "into a tough invisible layer that seals the surface. Not "
               "paint, and the same trick aluminium performs."},
    {"id": "m4",
     "name": "Zinc blocks bolted to a ship",
     "what": "Lumps of zinc attached below the waterline and replaced every "
             "few years.",
     "barrier": False,
     "answer": "Not a barrier — the blocks do not cover anything. Zinc is "
               "more reactive than iron, so it corrodes instead of the hull. "
               "It is called sacrificial protection, and the blocks being "
               "eaten away is the method working."},
    {"id": "m5",
     "name": "A galvanised gate",
     "what": "Steel dipped in molten zinc, leaving a zinc coat.",
     "barrier": False,
     "answer": "Both, and the second one is why it is worth the money. The "
               "zinc is a barrier — and when the barrier is scratched the "
               "exposed zinc still corrodes in preference to the iron, so a "
               "scratch in galvanising does not start rusting."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 218 character for character.
    "slug":        "oxidation",
    "title":       "Oxidation",
    "discipline":  "chemistry",
    "unit":        "types-of-reaction",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # NOTES §1: one statutory bullet, five lessons. `KS3.C.CR.03` names four
    # reaction types in a single bullet and clause `c` is the oxidation one,
    # already minted in `ks3_data/substatements.py` with its reasoning — it is
    # not re-minted and not edited here. `beyond_statutory` is False.
    "covers":      ["KS3.C.CR.03c"],
    "touches":     [],
    "beyond_statutory": False,
    # `structure-function` at 1 is not padding: the whole of `#s-think` turns
    # on how the oxide is BUILT — one clings and seals, the other flakes and
    # exposes — explaining what each metal then does. Same level and reasoning
    # as c2-03 and c3-04 carry it at.
    "threads":     [{"id": "substances-and-reactions", "level": 3},
                    {"id": "structure-function", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # ⚠️ `requires` IS THE DEPENDENCY GRAPH, NOT THE SLOT ORDER, and the two
    # differ here. Design's "Before this lesson" card names Thermal
    # decomposition, which is the PREVIOUS SLOT; the thing this lesson
    # actually cannot be read without is combustion — the hook, the second
    # explainer and the key note all argue from "every combustion is an
    # oxidation". Thermal decomposition is used once, as rung 1's third
    # option, and a distractor is not a dependency. The engine's own
    # "Where to next" card still carries the previous lesson, so nothing a
    # student can follow is lost.
    "requires":    ["combustion"],
    "assumes":     [],
    # ⚑ Flag 15's cross-link. The dict form is required the moment a reference
    # crosses a unit boundary, and the card prints the TARGET'S OWN TITLE —
    # "Aerobic respiration" — so no unit code reaches student-facing text.
    "references":  [{"unit": "B8", "lesson": "aerobic-respiration",
                     "why": "The reaction that keeps you alive is an "
                            "oxidation, run slowly enough to be useful."}],
    "connects_heading": "Connects to",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "A flash of burning magnesium and twenty years of a "
                    "rusting gate are the same reaction. What is it, and "
                    "what does it need?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL` in her order with her ids and her shorts.
    # `done_when` restates her own `DONE()` (page line 411): the hook on a
    # commitment, `#s-rust` when every tube has been predicted, `#s-stop` when
    # every method has been decided, `#s-think` on a commitment, the ladder
    # when both marked rungs are answered and both self-marked rungs checked.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Fast and slow", "done_when": "committed"},
        {"anchor": "s-rust",   "short": "TUBES",
         "label": "Four tubes", "done_when": "all_tubes_predicted"},
        {"anchor": "s-stop",   "short": "STOP",
         "label": "Stopping it", "done_when": "all_methods_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Aluminium", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚑ MRB-177, measured rather than eyeballed: the four options are
    # 4 / 6 / 3 / 5 words. The correct one (B) is strictly longest by ONE word
    # at 1.20×, which clears both thresholds, so nothing was touched. Every
    # distractor is a wrong RULE in B's own shape — a property both events are
    # claimed to share — and each is a real answer: light is what a student
    # can see, water is what rusting needs and burning does not, and "destroys
    # the metal" is the belief that an oxide is nothing rather than something
    # heavier.
    "phenomenon": {
        "kind": "narrative",
        "title": "Magnesium burns in two seconds. A gate rusts over twenty "
                 "years. It is the same reaction.",
        "prompt": "One is a flash of white light and a puff of powder. The "
                  "other is so slow that nobody has ever watched it happen. "
                  "Both take a metal and turn it into a metal oxide, and both "
                  "end up heavier than they started.",
        "commit": "What do the two have in common?",
        "options": [
            "Both give out light",
            "Both are a metal gaining oxygen",
            "Both need water",
            "Both destroy the metal completely",
        ],
        "reveal": "Both are <strong>oxidation</strong>: a substance gaining "
                  "oxygen. Speed is the only difference, and speed is not "
                  "what a reaction is named after. Combustion is oxidation "
                  "fast enough to produce a flame; rusting is oxidation slow "
                  "enough to be somebody else's problem in ten years' time.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ `REACT-14`'s `statement` is the PAGE's quoted line, not NOTES §5's
    # shorter register handle ("Aluminium and stainless steel do not
    # oxidise"). `r_confrontation` prints `statement` as the `#s-think` quote
    # and Design's line is the one that must render — the same reconciliation
    # `c4-03` made for `REACT-05` and `c3-03` for `MIX-06`. `REACT-15` is not
    # quoted anywhere on the page, so it keeps the register's wording.
    #
    # Both joins, and the one rename, are set out in the module docstring.
    "misconceptions": [
        {"id": "REACT-14",
         "statement": "Aluminium does not corrode — that is why drinks cans "
                      "and window frames are made of it.",
         "elicited_by": "s-think",
         "confronted_by": "think-reveal-oxide-layer"},
        {"id": "REACT-15",
         "statement": "Rusting needs water only, or air only.",
         "elicited_by": "tube-predictions",
         "confronted_by": "four-tube-summary"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page lines 106-107. Two paragraphs, two blocks: `explainer` carries
        # one `text`, and running them together would put the breadth claim
        # inside the definition.
        {"type": "explainer",
         "text": "<strong>Oxidation</strong> is a reaction in which a "
                 "substance gains oxygen. Metal plus oxygen makes a metal "
                 "oxide, and the product always weighs more than the metal "
                 "did, because the oxygen atoms are now part of it."},
        {"type": "explainer",
         "text": "That makes oxidation the widest of the four reaction types "
                 "in this unit. Every combustion is an oxidation. So is "
                 "rusting, so is the browning of a cut apple, and so — "
                 "inside every cell in your body, at a temperature you can "
                 "survive — is respiration."},

        # #s-rust — the flagship. Light `ks3-block` → `check`.
        # ⚠️ The activity id is `tube-predictions` and NOT the anchor: it is
        # REACT-15's `elicited_by`, and committing "will rust" on tube 2 or
        # tube 3 is where a student states the belief out loud.
        {"type": "control-tubes", "id": "tube-predictions", "anchor": "s-rust",
         "eyebrow": "Your turn · four tubes, four weeks",
         "heading": "An identical nail in each. Only what surrounds it is "
                    "different.",
         "demand": "investigate",
         "prompt": "Predict every tube before you open any of them. The tubes "
                   "are designed so that the four results together answer the "
                   "question no single tube could.",
         "tubes": _TUBES,
         # Design composes the card's kicker as `'Tube ' + (i + 1)`. The
         # NUMBER is the instrument's to compute — the summary, rung 2 and
         # rung 3 all quote "tube 2" and "tube 3" and must agree with what the
         # cards are labelled — but the WORD is student-facing, so it lives
         # here and not inside the renderer.
         "num_format": "Tube {n}",
         # The chip suffix is a student-facing word, so it lives in the record
         # rather than inside the renderer. "Oxygen present" / "Water removed"
         # — the STATE IS A WORD (R2), not a background colour on its own.
         "chip_labels": {"on": "present", "off": "removed"},
         # Deliberately NOT called `options`: `build_ks3.py` draws a generic
         # lettered list for any activity carrying `options` that its renderer
         # does not consume, and these are a two-button segmented control
         # inside each card.
         "predict_options": [{"id": "rust", "label": "Will rust"},
                             {"id": "no", "label": "Will not rust"}],
         # The confrontation panel, gated on all four commitments — because
         # the conclusion is not available from any three of them. `id` is
         # REACT-15's `confronted_by`.
         "summary": {
             "id": "four-tube-summary",
             "title": "Read the four together.",
             "text": "Tube 1 had air and water and rusted. Tube 2 had air and "
                     "no water: no rust. Tube 3 had water and no air: no "
                     "rust. So <strong>both</strong> are needed, and neither "
                     "on its own will do it — which is a conclusion no single "
                     "tube could have supported. Tube 4 had both plus salt "
                     "and rusted fastest, so salt is not needed but it speeds "
                     "the reaction up. Tubes 2 and 3 are the controls, and "
                     "they are doing the actual work.",
             # ⚑ Flag 11. The one equation on this page, and the honest one:
             # three reactants, and a product NAMED rather than formulated.
             # The arrow between them is drawn as SVG by the renderer — the
             # shipped font subsets carry no U+2192, and this is Design's C4
             # convention, which C5 inherits.
             "equation": {"left": "iron + oxygen + water",
                          "right": "hydrated iron oxide (rust)"}}},

        {"type": "key-fact", "ref": "gaining-oxygen"},

        # #s-stop — five methods, one decision each. Light `ks3-block` →
        # `check`. The rail stop ticks when all five are decided, which is
        # Design's `DONE('s-stop')`.
        {"type": "rust-stop", "id": "rust-methods", "anchor": "s-stop",
         "eyebrow": "Five ways to stop it",
         "heading": "Four keep the oxygen and water out. One does something "
                    "cleverer.",
         "demand": "classify",
         "prompt": "Decide which kind each method is before you read it. If "
                   "you know the rule, one of the five should feel wrong "
                   "under it — that is the one worth understanding.",
         "methods": _METHODS,
         "verdict_options": [
             {"id": "barrier", "label": "Keeps oxygen and water out"},
             {"id": "other", "label": "Works some other way"}]},

        {"type": "misconception", "id": "think-reveal-oxide-layer",
         "anchor": "s-think", "targets": "REACT-14"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. Design draws no diagram on this page and NOTES §6 declares none:
    # the picture is four tubes of words with their controlled variables
    # chipped along the bottom, which is what a controlled investigation draws
    # instead of a diagram. Present and empty, never absent.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "gaining-oxygen",
         "text": "Oxidation is a substance gaining oxygen, and the product is "
                 "always heavier than what you started with. Rusting needs "
                 "oxygen and water together; salt only makes it faster.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two instrument blocks are lifted out of `core` into
    # this list by `_normalise()` and are never authored here.
    #
    # ⚑ MRB-177: the four options measure 7 / 10 / 8 / 13 words. The correct
    # one (B) is not the longest, so there is no tell and nothing was touched.
    # Both "Right" options are real: A is the belief stated flatly and C is
    # the same belief given a reason, which is the version a student who has
    # met the reactivity series actually offers. D is the trap for someone who
    # over-corrects — it gets "corrodes faster than iron" right and draws the
    # wrong conclusion from it.
    "activities": [
        {"id": "think-reveal-oxide-layer",
         "kind": "predict",
         "demand": "explain",
         "targets": "REACT-14",
         "prompt": "Aluminium really does last outdoors for decades without "
                   "going orange and flaking. Commit before you read on.",
         "options": [
             "Right — aluminium does not react with oxygen",
             "Wrong — it oxidises immediately, and the oxide layer protects "
             "it",
             "Right, because aluminium is a very unreactive metal",
             "Wrong — aluminium corrodes faster than iron and cans are lined "
             "to stop it",
         ],
         "reveal": [
             "Aluminium oxidises the moment it meets air, and faster than "
             "iron does — it is one of the more reactive metals you will "
             "meet. Every piece of aluminium you have ever touched was "
             "already covered in a layer of aluminium oxide before you got "
             "to it.",
             "The difference is what the oxide does next. Aluminium oxide is "
             "tough, invisible and <strong>sticks tightly to the metal "
             "underneath</strong>, so it seals the surface and the reaction "
             "stops. Rust is crumbly and flakes off, exposing fresh iron, so "
             "the reaction never stops — a nail left long enough rusts all "
             "the way through. <strong>Both metals corrode; only one of them "
             "is protected by the result.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce. Her four
    # headings are the engine's own defaults character for character, so no
    # rung authors a `title`. `feedback` is keyed by the INT index of each
    # wrong option, which is what `_rung_marked` reads.
    "ladder": {
        # ⚑ MRB-177, measured: 3 / 3 / 6 / 4 words. The correct option is the
        # JOINT SHORTEST, so there is no length tell and nothing moved. Each
        # distractor is another reaction type's rule wearing oxidation's
        # sentence — reduction, thermal decomposition, and the confusion of a
        # requirement with the definition.
        "recall": {
            "q": "What happens to a substance during oxidation?",
            "options": [
                "It gains oxygen",
                "It loses oxygen",
                "It is broken down by heat",
                "It reacts with water",
            ],
            "answer": 0,
            "feedback": {
                1: "That is reduction, which you will meet at GCSE. "
                   "Oxidation is the gain.",
                2: "That is thermal decomposition, and it needs no oxygen at "
                   "all.",
                3: "Rusting does need water as well — but the reaction is "
                   "named for the oxygen the iron gains.",
            }},
        # ⚠️ THE THREE DISTRACTORS BELOW ARE THE ONLY STRINGS IN THIS FILE
        # THAT ARE NOT DESIGN'S, and they are a §13 fix made AT THE
        # DISTRACTOR. Her four options measure 16 / 7 / 4 / 4 words, so the
        # correct one is strictly longest by NINE words at 2.29× — a length
        # tell so loud that a student can take this rung without reading the
        # stem, on the rung whose whole point is that reading carefully is the
        # skill. Rewritten to 16 / 14 / 14 / 13, each still a wrong rule in
        # the correct option's own shape: a claim about what this one tube
        # proves, plus the conclusion drawn from it. The correct option is
        # untouched, the answer is in the same place, and each correction was
        # extended only where the new clause needed answering.
        "apply": {
            "q": "A nail in boiled water under a layer of oil does not rust. "
                 "What does that tube on its own prove?",
            "options": [
                "Only that water alone is not enough — you need the other "
                "tubes to conclude anything more",
                "That water is not involved in rusting, so the other tubes "
                "are not needed",
                "That oil is what prevents rusting — you can conclude that "
                "from this tube alone",
                "That rusting needs salt as well, because this tube had none "
                "in it",
            ],
            "answer": 0,
            "feedback": {
                1: "Tube 1 rusted and had water in it. This tube shows water "
                   "is not sufficient, not that it is unnecessary — and that "
                   "is exactly why the other tubes are needed.",
                2: "The oil is there to keep air out. Concluding that oil is "
                   "the active ingredient confuses the method with the "
                   "variable.",
                3: "Tube 1 had no salt and rusted anyway. Salt changes the "
                   "speed, not the requirements.",
            }},
        "explain": {
            "q": "Explain why the four-tube experiment needs tubes 2 and 3, "
                 "when tube 1 already shows that a nail rusts. Then state the "
                 "conclusion the whole set supports, and what tube 4 adds.",
            "field_label": "Your explanation",
            "placeholder": "Tube 1 on its own shows that…",
            "success": [
                "Says tube 1 alone shows rusting happens but not what is "
                "needed for it.",
                "Says tube 2 removes water while keeping air, and tube 3 "
                "removes air while keeping water.",
                "Says each of those tubes rules out one factor being "
                "sufficient on its own.",
                "States the conclusion: both oxygen and water are needed for "
                "rusting.",
                "Says tube 4 shows salt speeds it up without being a "
                "requirement.",
            ]},
        # ⚑ Flag 14 again, and this is the rung that made the ruling matter.
        # Criterion 2 is Design's own and it says "corrodes in preference to
        # the iron" — no electrons. The stretch paragraph used to answer this
        # rung with a different model from the one the rung credits.
        "produce": {
            "q": "A boat owner is told that bolting blocks of a more reactive "
                 "metal to the hull will protect it, and replies that adding "
                 "more reactive metal to a corroding boat sounds like the "
                 "worst possible idea. Explain why the method works, what "
                 "happens to the blocks, and why they have to be checked.",
            "field_label": "Your answer",
            "placeholder": "The blocks are more reactive than iron, so…",
            "success": [
                "Says the blocks are made of a metal more reactive than iron, "
                "such as zinc.",
                "Says the more reactive metal corrodes in preference to the "
                "iron.",
                "Says the hull is therefore protected while the blocks last.",
                "Says the blocks are gradually eaten away, which is the "
                "method working rather than failing.",
                "Says they must be inspected and replaced, or the protection "
                "ends and the hull starts to corrode.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Oxidation is a substance gaining oxygen, and the product "
                "weighs more than the starting material. Combustion is "
                "oxidation fast enough to burn; rusting is oxidation slow "
                "enough to take years, and it needs oxygen and water together "
                "— salt only speeds it up. Rust flakes off and exposes fresh "
                "iron, which is why iron keeps rusting while aluminium, whose "
                "oxide clings, does not.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Design's two "Going further" paragraphs. The first is byte-identical and
    # is where flag 15 lands: respiration named as an oxidation, with the same
    # products as burning, run slowly enough to be useful.
    #
    # ⚖️ THE SECOND CARRIES THE ONE RULED CUT (flag 14), RE-AUTHORED AS A
    # SENTENCE rather than raw-deleted. Design wrote "because zinc is more
    # reactive, so it gives up its electrons first". The reason for cutting it
    # is not that electrons are hard: it is that this lesson and `c5-01`
    # define oxidation THROUGHOUT as a substance GAINING OXYGEN, and that
    # clause introduces a second, unreconciled definition of both oxidation
    # and reactivity in nine words of a stretch box. A student who notices has
    # been handed a contradiction with no way to settle it; one who does not
    # has learned a phrase. §7 / MRB-225: nothing in a lesson may be undercut
    # by another part of the same lesson.
    #
    # The replacement is Design's own wording from `m5` and from rung 4's
    # second criterion — "the more reactive metal corrodes in preference to
    # the other" — so the page now gives ONE account of sacrificial protection
    # in all three places it appears. The electron model arrives at KS4 with
    # the apparatus to support it, and `ks4_becomes` says so.
    "stretch": [
        {"type": "explainer", "id": "oxidation-without-a-flame",
         "text": "Oxidation does not need a flame, a bench or a metal. Cut an "
                 "apple and the surface browns within minutes as substances "
                 "in the flesh oxidise in air; lemon juice slows it because "
                 "vitamin C is oxidised first, which is what \"antioxidant\" "
                 "means on a label. And the reaction that keeps you alive is "
                 "an oxidation: glucose plus oxygen makes carbon dioxide and "
                 "water, exactly the products of burning it, released slowly "
                 "enough at 37 °C that your cells can use the energy instead "
                 "of catching fire."},
        {"type": "explainer", "id": "the-sacrificial-block",
         "text": "The cleverest anti-rusting trick is worth knowing in full. "
                 "Bolt blocks of zinc to a steel ship's hull and the zinc "
                 "corrodes instead of the steel — not by covering it, but "
                 "because zinc is the more reactive of the two, and the more "
                 "reactive metal corrodes in preference to the other. The "
                 "blocks are inspected and replaced every few years, which is "
                 "why they are called sacrificial. Galvanising is the same "
                 "idea in a thin layer: a scratch in a galvanised gate does "
                 "not start rusting, because the zinc around the scratch is "
                 "still doing the corroding for it."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # ⚠️ The key is `definition`, not `gloss`: `build_ks3.py:939` hard-indexes
    # `v["definition"]` and would raise the moment a `keyword` block was
    # placed.
    #
    # `control` earns its place ahead of every chemistry term here. It is what
    # tubes 2 and 3 ARE, it is the word rung 2 and rung 3 both turn on, and it
    # is the one term on this page a student is likely to have heard used to
    # mean something else entirely.
    "vocabulary": [
        {"term": "oxidation",
         "definition": "A reaction in which a substance gains oxygen. The "
                       "product always weighs more than the substance you "
                       "started with."},
        {"term": "metal oxide",
         "definition": "What a metal becomes when it gains oxygen — "
                       "magnesium oxide, iron oxide, aluminium oxide."},
        {"term": "rust",
         "definition": "Hydrated iron oxide: what iron becomes when it has "
                       "oxygen and water together. It is crumbly and flakes "
                       "off, which is why the iron underneath keeps rusting.",
         "note": "Only iron and steel rust. Other metals corrode, which is "
                 "the general word."},
        {"term": "corrosion",
         "definition": "A metal being eaten away by reacting with its "
                       "surroundings. Rusting is corrosion; so is the "
                       "oxidising of aluminium and of zinc."},
        {"term": "control",
         "definition": "A tube set up to remove exactly one thing, so that "
                       "what happens in it tells you whether that one thing "
                       "was needed."},
        {"term": "sacrificial protection",
         "definition": "Attaching a more reactive metal so that it corrodes "
                       "in preference to the iron you want to keep. The "
                       "blocks are eaten away on purpose and are replaced."},
    ],

    # ── safety (§16) ────────────────────────────────────────────────────────
    # ⚖️ NO `safety_note`, DELIBERATELY, and the decision is reported rather
    # than left silent. Nothing on this page asks a student to do anything:
    # the four tubes were set up four weeks ago by somebody else and are read,
    # not built, and the five stopping methods are a bridge, a bicycle, a
    # drawer of cutlery, a ship and a gate. `c3-03` earned one because it ends
    # with a camping filter and a twelve-year-old might drink what they
    # filtered; there is no equivalent act here. A blanket lab line added
    # anyway would be a callout with nothing to call out, and would train
    # students to skip the ones that mean something.
    #
    # §16 safeguarding is separately NOT earned. Respiration is named as a
    # chemical process happening in cells, not as a fact about the reader's
    # own body needing a route to help.

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why tubes 2 and 3 are the important "
                      "ones?",
              "cta": "Ask about this lesson",
              "anchor": "s-rust"},

    "ks4_becomes": "Oxidation and reduction as electron transfer, corrosion "
                   "and its prevention, and the reactivity series explained.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # Both, and neither is decorative: `experimental-skills` is what tubes 2
    # and 3 are for (controlling one variable at a time), and
    # `analysis-and-evaluation` is the summary's whole move — a conclusion
    # drawn from four results together that none of them supports alone.
    "ws": ["experimental-skills", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
