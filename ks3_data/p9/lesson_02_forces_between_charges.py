"""P9 L2 — Forces between charges (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p9/p9-02-forces-between-charges.dc.html`.

Her page wins outright. The two balloons, the two spheres on their stands,
the nine-case table and all four rungs are hers.

── ⚖️ RULED 21 Aug 2026 (Mide) · INDUCTION IN RELATIVE WORDS ONLY ────

Her FLAG 9 asks for a ruling on the induced-attraction coefficient: the
distance dependence is right in KIND — it falls faster than the force
between two charges — and the coefficient is chosen so the effect is
readable on the same scale rather than measured.

**The coefficient is ACCEPTED, and induced attraction is reported in
relative words only. No absolute force in newtons appears anywhere on
this page — not in a tile, a note, the legal line or a rung.**

Her page already holds that line, exactly: the strength tile's sub-line
for a neutral pair reads *"a small fraction of the charged pair at this
gap"* and prints no figure at all, and the like/unlike cases carry her
RELATIVE scale, on which 100 is the closest fully charged pair and which
the legal line declares as a scale rather than a measurement. Nothing
moved. `r_charge_pair` walks the whole payload and refuses one that names
a newton anywhere in it, so the ruling cannot be lost to a later edit.

── ⚖️ THE STRENGTH WORD IS COMPUTED, AND THE EQUAL AND ZERO STATES ARE
   REAL ────────────────────────────────────────────────────────────────

Design's seven bands run from *no force at all* through *far too weak to
see* to *very strong*, and the word is derived from the value rather than
authored per control (5A.1). Two states are worth driving on purpose:

  * **both neutral** — strength 0, no arrows at all, and the note says
    this is the ONE case in the whole table that gives nothing;
  * **one neutral at the widest gap** — the induced term is
    `8 × (4 ÷ 20)⁴ = 0.0128`, which lands on *far too weak to see*, and
    the tile still refuses to print a figure.

── ⚖️ ATTRACTION PROVES NOTHING; REPULSION IS THE PROOF ──────────────

That is the closing line of the nine-case table and the whole of rung 1.
It is the reason the table exists rather than the two-rule summary: four
of its nine cells are the third outcome.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's two marked rungs both put the correct answer at index 0, as do
all six across P9. **Her option TEXT and every correction are verbatim;
only the ORDER moves.** This lesson takes indices **1 and 3**. Engine
policy, not a register row.

── ⚠️ NO SAFEGUARDING BLOCK. NO DRAFT MARKINGS. ──────────────────────
"""

LESSON = {
    "slug": "forces-between-charges",
    "title": "Forces between charges",
    "discipline": "physics",
    "unit": "Static electricity",
    "family": "MODEL",

    "covers": ["KS3.P.STAT.01b"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "electricity", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 60,

    # ⚠️ NO LESSON HERE ASSUMES ITS PREDECESSOR. Design's §4 records that
    # `p9-02` restates in one clause that rubbing separates charge, so a
    # school running P9 in another order strands nobody. The edge is still
    # declared, because it is the honest reading order.
    "requires": ["charging-by-rubbing"],
    "assumes": [],
    "references": [{"unit": "P8", "lesson": "conductors-and-insulators"},
                   {"unit": "P8", "lesson": "current-and-circuits"}],
    "ks4_links": [],

    "meta_description": "Like charges push apart and unlike charges pull "
                        "together — and a charged object also pulls on "
                        "something with no charge at all.",

    "big_question": "Like charges push apart, unlike charges pull together — "
                    "and a charged object also pulls on something with no "
                    "charge at all, which is the case people forget.",

    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "Two balloons",           "done_when": "committed"},
        {"anchor": "s-spheres", "short": "BENCH",
         "label": "Charge them, move them", "done_when": "gate_and_a_control"},
        # ⚠️ Design's `DONE` gives this stop the GATE alone, before the bench
        # beside it is finished. The bench marks it through `band_anchor` /
        # `band_at`; `mirrors` would tick it late and would also fail
        # `check_rail_matches_design`, which derives the mirror map from her
        # `isDone()` and finds two different expressions here.
        {"anchor": "s-matrix",  "short": "TABLE",
         "label": "Every combination",      "done_when": "gate_committed"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Two balloons, one jumper, two opposite results.",
        "prompt": "Rub two balloons on the same jumper and hang them side by "
                  "side on threads: they swing away from each other and "
                  "refuse to touch. Take either one and hold it near the "
                  "wall and it sticks there.",
        "commit": "How can the same balloon push one thing away and pull "
                  "another thing in?",
        "options": [
            "Both balloons got the same charge, so they repel; the wall has "
            "no charge, and a charged object attracts an uncharged one",
            "The wall is oppositely charged because the room is positively "
            "charged overall",
            # ⚠️ MRB-177 — Design's distractor, FINISHED. Her hook's correct
            # option is 22 words against a longest distractor of 15, which is
            # a tell at the ≥4-word threshold — and a tell on a HOOK does the
            # most damage of all, because a student who spots the answer
            # never commits and a belief nobody commits to cannot be
            # confronted. Remedied at the distractor, and the added clause
            # states the wrong rule completely rather than padding it.
            "The balloon that sticks has lost its charge, so it is held to "
            "the wall by ordinary friction and nothing electrical",
            "Balloons repel other balloons and attract everything else, as a "
            "property of rubber",
        ],
        "answer": 0,
        "reveal": "Rubbed on the same jumper, both balloons end up with the "
                  "same charge, and like charges repel — so they swing "
                  "apart. The wall was never charged, and it still is not. "
                  "What the balloon does is push the wall's own charges "
                  "aside, so the surface nearest the balloon becomes "
                  "slightly opposite to it, and the balloon is pulled in. "
                  "Attraction to an uncharged object is a real effect with "
                  "its own name: <strong>induction.</strong>",
    },

    "misconceptions": [
        {"id": "CHRG-05",
         "statement": "The rod picks up the paper, so the paper must be "
                      "charged.",
         "elicited_by": "spheres",
         "confronted_by": "s-think"},
        {"id": "CHRG-06",
         "statement": "They have to touch, or the air has to carry it.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "CHRG-07",
         "statement": "The force between two charges falls in step with the "
                      "distance, so doubling the gap halves it.",
         "elicited_by": "s-ladder",
         "confronted_by": "spheres"},
        {"id": "CHRG-08",
         "statement": "A charged object does nothing at all to an uncharged "
                      "one, because there is no charge for it to act on.",
         "elicited_by": "spheres",
         "confronted_by": "matrix"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Two charged objects push or pull on each other without "
                 "touching, and the rule is short: <strong>like charges "
                 "repel, unlike charges attract</strong>. Two positives push "
                 "apart. Two negatives push apart. A positive and a negative "
                 "pull together. The two forces are always equal in size and "
                 "opposite in direction — whichever object is smaller or "
                 "more lightly charged, it feels exactly the same pull as "
                 "the other one."},
        {"type": "explainer",
         "text": "The force gets rapidly weaker as they move apart. Doubling "
                 "the separation does not halve it: it cuts it to about a "
                 "quarter. That is why static effects are dramatic at a "
                 "centimetre and undetectable across a room."},
        {"type": "explainer",
         "text": "Then the case that surprises people. A charged object also "
                 "attracts a completely <strong>uncharged</strong> one. "
                 "Bring a negative rod near a scrap of paper and the rod's "
                 "charge pushes the paper's own electrons to the far side, "
                 "leaving the near side slightly positive. The paper is "
                 "still neutral overall — nothing has been added or removed "
                 "— but its near side is now oppositely charged and closer, "
                 "so the pull wins over the push. This is "
                 "<strong>induction</strong>, and it is the whole reason a "
                 "rubbed rod picks things up."},

        # ── #s-spheres · two light spheres on insulating stands ────────
        {"type": "charge-pair",
         "id": "spheres",
         "anchor": "s-spheres",
         "eyebrow": "At the bench · two light spheres on insulating stands",
         "heading": "Charge them. Move them.",
         # ⚠️ A MAP OF NAMED STATES, NOT A STRING — see `p9-01`'s note and the
         # long one where `_head` is NOT, in `ks3_art/p9.py`.
         "progress": {"idle": "Change a control to begin",
                      "live": "Three controls live"},
         "lead": "Each sphere can be left neutral or given a positive or a "
                 "negative charge of the same size. The arrows show the "
                 "force on each one and how strong it is.",
         # ⚖️ HER MODEL, EXACTLY. Two charged spheres fall as the inverse
         # square — the real relationship — with 100 set at the closest gap.
         # The induced case falls as the fourth power, which is right in
         # KIND, on a coefficient chosen to be readable. Ruled acceptable
         # 21 Aug 2026, on the condition that it is never reported as a
         # force in newtons.
         "k": 100,
         "ind_k": 8,
         "ref_d": 4,
         "band_anchor": "s-matrix",
         "band_at": 1,
         "start_a": 2,
         "start_b": 1,
         "a_label": "Left sphere",
         "b_label": "Right sphere",
         "bench_label": "INSULATING STANDS ON A BENCH",
         # ⚖️ THE INDUCED CASE'S STRENGTH SUB-LINE. A COMPARISON, WITH NO
         # FIGURE IN IT — the ruling, in the one place it would otherwise
         # have been tempting to print one.
         "induced_sub": "a small fraction of the charged pair at this gap",
         "gate": {
             "prompt": "Commit first. One sphere is charged negative. The "
                       "other is left completely neutral. What happens?",
             "options": [
                 "Nothing — a neutral object has no charge, so there is "
                 "nothing to push or pull on",
                 "They repel, because the neutral one has as many negatives "
                 "as the charged one",
                 "They attract weakly, because the charged one pushes the "
                 "neutral one's charges aside",
                 "They attract strongly, exactly as two opposite charges "
                 "would",
             ],
             "answer": 2,
         },
         "sep": {"label": "How far apart", "min": 4, "max": 20, "step": 1,
                 "start": 8, "value": "8 cm"},
         "states": [
             {"id": "pos", "label": "Positive", "q": 1,
              "word": "positively charged"},
             {"id": "neu", "label": "Neutral", "q": 0, "word": "neutral"},
             {"id": "neg", "label": "Negative", "q": -1,
              "word": "negatively charged"},
         ],
         # ⚠️ SEVEN WORDS, AND THE WORD IS THE ONLY CHANNEL THE READING HAS
         # in the induced case, where no figure is printed at all. Read
         # highest-first by the wiring.
         "strength_bands": [
             {"at_least": 70, "word": "very strong"},
             {"at_least": 30, "word": "strong"},
             {"at_least": 10, "word": "moderate"},
             {"at_least": 3, "word": "weak"},
             {"at_least": 0.5, "word": "very weak"},
             {"at_least": 0, "word": "far too weak to see"},
         ],
         "readouts": [
             {"id": "verdict", "label": "What happens", "sub": "—"},
             {"id": "strength", "label": "How strong", "sub": "—"},
             {"id": "sep", "label": "Separation", "sub": "centre to centre"},
             {"id": "pair", "label": "Force on each sphere"},
         ],
         # ⚠️ `{d}` is the separation in cm, `{strength}` the relative
         # figure to one decimal, `{sign}` the shared sign word, `{cside}` /
         # `{nside}` which side is charged and which neutral, `{csign}` the
         # charged sphere's sign and `{nearsign}` / `{farsign}` the induced
         # signs on the neutral sphere's two faces. `verdict` and `sub` are
         # the two readout words the tile shows beside the note.
         "branches": {
             "none": {
                 "verdict": "nothing happens",
                 "sub": "both spheres neutral",
                 "note": "Neither sphere carries a charge, so there is "
                         "nothing to push or pull with, and the arrows are "
                         "gone. Move them as close as you like and nothing "
                         "changes. This is the one case in the whole table "
                         "that gives no force — which is worth noticing, "
                         "because “neutral” is not the same as "
                         "“nothing to do with electricity”."},
             "repel": {
                 "verdict": "they repel",
                 "sub": "both positive",
                 "sub_alt": "both negative",
                 "note": "Both spheres are {sign} — like charges — so each "
                         "is pushed away from the other, with equal and "
                         "opposite forces. At {d} cm the strength is "
                         "{strength} on this scale. Halve the separation and "
                         "it goes up about four times; double it and it "
                         "drops to about a quarter. Repulsion is the only "
                         "result that proves both objects are charged."},
             "attract": {
                 "verdict": "they attract",
                 "sub": "one positive, one negative",
                 "note": "One sphere is positive and one negative — unlike "
                         "charges — so each is pulled towards the other, "
                         "with equal and opposite forces. At {d} cm the "
                         "strength is {strength} on this scale, the same "
                         "size as the repulsion between two like charges at "
                         "the same distance. Only the direction changed."},
             "induced": {
                 "verdict": "they attract, weakly",
                 "sub": "induction on the neutral sphere",
                 "note": "The {cside} sphere is {csign} and the {nside} one "
                         "has no charge at all — and they still attract. The "
                         "charged sphere pushes the neutral one's own "
                         "charges along, so its near face turns slightly "
                         "{nearsign} and its far face slightly {farsign}. "
                         "Both faces feel a force, but the near one is "
                         "closer and closeness matters enormously, so the "
                         "pull wins. It is much weaker than the pull two "
                         "oppositely charged spheres would give across the "
                         "same gap, and it dies away faster still as you "
                         "separate them. The neutral sphere's total charge "
                         "is unchanged throughout."},
         },
         # ⚖️ `scale_sub` IS THE ONLY PLACE A FIGURE IS PRINTED, AND IT SAYS
         # WHAT THE FIGURE IS. Never a newton; a position on a declared
         # scale. The induced case does not reach it at all — it takes
         # `induced_sub`, which carries no number.
         "words": {
             "zero_word": "no force at all",
             "zero_sub": "zero on this scale",
             "scale_sub": "{strength} where 100 is the strongest shown",
             "pair": "equal and opposite",
             "pair_none": "none on either",
         }},

        # ── #s-matrix · every combination there is ─────────────────────
        {"type": "charge-band",
         "id": "matrix",
         "anchor": "s-matrix",
         "eyebrow": "The figure",
         "heading": "Every combination there is",
         "lead": "Two objects, three states each, nine cases. Only one of "
                 "the nine produces nothing at all — which is worth "
                 "noticing, because the usual summary of this topic mentions "
                 "two.",
         "matrix": {
             "corner": "Left / right",
             "columns": ["Positive", "Neutral", "Negative"],
             "rows": [
                 {"head": "Positive", "cells": [
                     {"text": "<strong>Repel</strong> — like charges",
                      "strong": True},
                     {"text": "Attract weakly — induction"},
                     {"text": "<strong>Attract</strong> — unlike charges",
                      "strong": True},
                 ]},
                 {"head": "Neutral", "cells": [
                     {"text": "Attract weakly — induction"},
                     {"text": "Nothing"},
                     {"text": "Attract weakly — induction"},
                 ]},
                 {"head": "Negative", "cells": [
                     {"text": "<strong>Attract</strong> — unlike charges",
                      "strong": True},
                     {"text": "Attract weakly — induction"},
                     {"text": "<strong>Repel</strong> — like charges",
                      "strong": True},
                 ]},
             ],
         },
         "close": "This gives you a test worth remembering. <strong>"
                  "Attraction proves nothing</strong> — an object that is "
                  "pulled towards a charged rod might be oppositely charged, "
                  "or might have no charge at all. Only <strong>repulsion"
                  "</strong> is proof, because nothing but a like charge can "
                  "push."},

        {"type": "key-fact", "ref": "repulsion-is-the-proof"},

        {"type": "misconception", "id": "think-attraction-proves-nothing",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        # ⚠️ PLAIN `predict`, as everywhere else in the key stage. `#s-think`
        # is NOT a rail stop on this page — Design's third stop is the table
        # — so the section needs no completion contract of its own.
        {"id": "think-attraction-proves-nothing",
         "kind": "predict",
         "demand": "explain",
         "targets": "CHRG-05",
         "statements": [
             {"quote": "The rod picks up the paper, so the paper must be "
                       "charged.",
              "targets": "CHRG-05",
              "body": [
                  "The paper came out of a drawer and nobody rubbed it. It "
                  "is neutral, and it stays neutral the whole time — its "
                  "total charge never changes. What the rod does is push the "
                  "paper's own electrons to the far side of it, so the near "
                  "face becomes slightly opposite to the rod and the far "
                  "face slightly the same. Both faces feel a force, but the "
                  "near one is closer, and the force weakens so fast with "
                  "distance that the near face wins. The paper is pulled in "
                  "as a whole. Attraction is never proof of charge; only "
                  "repulsion is.",
              ]},
             {"quote": "They have to be touching, or there has to be air in "
                       "between to carry it.",
              "targets": "CHRG-06",
              "body": [
                  "Neither. The spheres never touch, and the force is "
                  "undiminished in a vacuum — two charged objects in an "
                  "evacuated jar push and pull on each other exactly as they "
                  "did in air. There is nothing in the gap doing the "
                  "carrying. That is such a strange claim that physics gives "
                  "it its own name and its own lesson: the charged object "
                  "fills the space around it with an <em>electric field</em>, "
                  "and the field is what the other object responds to.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "repulsion-is-the-proof",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Like charges repel and unlike charges attract, with equal "
                 "and opposite forces that weaken quickly with distance. A "
                 "charged object also attracts a neutral one, by pushing "
                 "that object's own charges to one side. So repulsion proves "
                 "an object is charged; attraction does not."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 1 and 3.
    # Design put both at 0; her option TEXT and every correction are verbatim
    # and only the ORDER moves.
    "ladder": {
        "recall": {
            "q": "A negatively charged rod is held near a hanging "
                 "metal-coated ball on a thread. The ball swings towards the "
                 "rod. What can you conclude about the ball?",
            "options": [
                "It must be positively charged, because unlike charges "
                "attract",
                "Nothing certain — it could be positively charged, or it "
                "could be neutral",
                "It must be neutral, because a charged ball would have been "
                "pushed away",
                "It must be negatively charged, because the rod is negative",
            ],
            "answer": 1,
            "feedback": {
                0: "A positive ball would be attracted, but so would a "
                   "neutral one — by induction. Attraction cannot tell the "
                   "two apart; only repulsion is proof.",
                2: "A ball with a like charge would be pushed away. A ball "
                   "with the opposite charge would be pulled in just as a "
                   "neutral one is.",
                3: "Two negatives repel, so a negative ball is the one thing "
                   "this observation rules out.",
            },
            "title": "Rung 1 · Predict"},
        "apply": {
            "q": "Two identical spheres carrying the same charge repel with "
                 "a certain force at 5 cm. They are moved to 10 cm apart. "
                 "What happens to the force?",
            "options": [
                "It falls to about half, because the distance doubled",
                "It stays the same, because neither charge has changed",
                "It falls to about a quarter on the nearer sphere and stays "
                "the same on the further one",
                "It falls to about a quarter of what it was",
            ],
            "answer": 3,
            "feedback": {
                0: "The force does not simply track the distance. Doubling "
                   "the separation cuts it to about a quarter, which is why "
                   "static effects vanish so quickly.",
                1: "The charges have not changed, but the force between "
                   "charges depends on how far apart they are as well as how "
                   "big they are.",
                2: "The quarter is right, but it applies to both. The two "
                   "forces are always equal in size and opposite in "
                   "direction, however different the spheres are.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A balloon rubbed on a jumper sticks to a wall that nobody "
                 "has charged. Explain how a charged object can be attracted "
                 "to an uncharged one.",
            "field_label": "Your explanation",
            "placeholder": "The balloon is charged and the wall is not, so…",
            "success": [
                "Says the balloon is charged and the wall is neutral, and "
                "stays neutral throughout.",
                "Says the balloon’s charge pushes the wall’s own charges to "
                "one side.",
                "Says the near surface of the wall ends up with the opposite "
                "charge to the balloon.",
                "Says the far side ends up with the same charge as the "
                "balloon, so it is pushed away.",
                "Says the near side wins because the force weakens quickly "
                "with distance, so the balloon is pulled in overall.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "You are given two identical hanging balls, one of which "
                 "you know is charged, and no other apparatus. Describe how "
                 "you would find out whether the second ball is charged too, "
                 "and explain why one possible result would tell you "
                 "nothing.",
            "field_label": "Your answer",
            "placeholder": "Bring the two balls near each other and watch…",
            "success": [
                "Describes bringing the two balls close and watching whether "
                "they move apart or together.",
                "Says that repulsion shows the second ball is charged, with "
                "the same sign as the first.",
                "Says that attraction is the ambiguous result.",
                "Explains why: an oppositely charged ball and a neutral ball "
                "both get attracted.",
                "Concludes that only a repulsion answers the question, so a "
                "single attraction is not a result you can report.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Charged objects push and pull on each other without "
                "touching. Like charges repel, unlike charges attract, and "
                "the two forces are always equal in size and opposite in "
                "direction. The force weakens quickly as the separation "
                "grows — doubling the distance cuts it to about a quarter. A "
                "charged object also attracts a neutral one, because it "
                "pushes that object's own charges to one side and the "
                "closer, opposite face wins. So repulsion is proof that an "
                "object is charged, and attraction is not.",

    "stretch": [
        {"id": "stronger-than-gravity",
         "type": "explainer",
         "text": "The electric force is staggeringly strong compared with "
                 "gravity. Between two protons it beats their gravitational "
                 "attraction by a factor of about ten thousand million "
                 "million million million million million. You never notice, "
                 "because matter is so precisely balanced: every object you "
                 "have ever picked up has its positive and negative charges "
                 "matched to an extraordinary accuracy, and the tiny "
                 "imbalance a duster can produce is enough to lift paper "
                 "against the pull of the whole Earth."},
        {"id": "induction-at-work",
         "type": "explainer",
         "text": "Induction is quietly useful. Electrostatic paint spraying "
                 "gives the paint droplets a charge and the car body the "
                 "opposite one, so the paint is pulled onto the metal and "
                 "wraps round edges instead of drifting past; a "
                 "power-station precipitator charges the smoke particles and "
                 "collects them on plates, taking out most of the ash before "
                 "it reaches the chimney. Both work on the case in the "
                 "middle of the table — charge one thing, and something "
                 "uncharged comes to you."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "repel",
         "definition": "To push apart. Two charges of the same sign always "
                       "repel, and repulsion is the only proof that both "
                       "objects are charged."},
        {"term": "attract",
         "definition": "To pull together. Two opposite charges attract — and "
                       "so do a charged object and a neutral one, which is "
                       "why attraction proves nothing on its own."},
        {"term": "induction",
         "definition": "A charged object pushing a neutral object's own "
                       "charges to one side, so the near face becomes "
                       "opposite and the whole object is pulled in. The "
                       "neutral object's total charge never changes."},
    ],

    "tutor": {
        "anchor": "s-spheres",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got two objects and want to know whether they attract, "
                "repel or do nothing?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Electric field lines and their direction, and the "
                   "inverse-square dependence stated properly.",

    "convention_note": "The bench is a teaching model. Both charges are "
                       "treated as equal in size and as sitting at the "
                       "centre of each sphere, and the strength is reported "
                       "as a relative figure with the closest fully charged "
                       "case set to 100 — no force in newtons is given "
                       "anywhere on the bench, because the equation for it "
                       "is beyond this stage and any number in newtons here "
                       "would be invented rather than measured. Induced "
                       "attraction on a neutral sphere is reported in "
                       "relative words only, never as a figure, because the "
                       "size of that effect is a chosen coefficient rather "
                       "than a measurement. The relative figure falls as the "
                       "square of the separation for two charged spheres, "
                       "which is the real relationship; the much weaker "
                       "attraction to a neutral sphere is modelled as "
                       "falling faster still, which is the right behaviour "
                       "but the coefficient is chosen to be readable rather "
                       "than measured. Real spheres are not points, so at "
                       "the closest separations the true force is somewhat "
                       "larger than the model gives. The induced charges "
                       "drawn on a neutral sphere are indicative, and the "
                       "sphere's total charge stays zero throughout.",

    "ws": ["measurement"],
}
