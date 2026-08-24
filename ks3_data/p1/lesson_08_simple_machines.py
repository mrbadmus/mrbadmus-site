"""p1-08 — *Simple machines* (QUANTITATIVE).

Ported from Claude Design's `p1-08-simple-machines.dc.html`.

── WHAT THIS LESSON OWNS ───────────────────────────────────────────────

`KS3.P.ECT.01`. It is the unit's QUANTITATIVE lesson and the only one
carrying a worked example.

── ⚖️ MRB-204 · A BEAM *AND* TRIANGLES, AND THAT IS NOT A CONTRADICTION ─

This is the page where the ruling earns its keep, and Design gets it exactly
right in her own words: *"Each side is a multiplication, so each pan carries
a triangle. The equals sign between them is a balance, which no triangle can
show."*

    E = F × d              a genuine product  → TRIANGLE, legitimately
    F₁ × d₁ = F₂ × d₂      a balance of two   → BEAM, with a triangle on
                           products             each pan

Her `COVERS` map says the same thing about the fourth option: *"there are
four quantities and an equals sign, not three quantities and a bar. Read it
off the beam instead."* Nothing here needed correcting.

⚠️ **SUBSCRIPTS.** `<sub>1</sub>` in markup, plain digits inside payload
values. Design's page uses U+2081/U+2082 directly; those are converted on the
way in rather than carried through, because a payload value is not markup and
a screen reader reads a Unicode subscript as an ordinary digit anyway.

⚠️ Arrows inside the formula block are SVG. Typed arrows stay in prose.

── ⚠️ SIX SECTIONS, FOUR RAIL STOPS ───────────────────────────────────

Her `RAIL` is `[s-hook, s-bench, s-worked, s-ladder]`. `#s-balance` AND
`#s-think` are sections with ids and no stops — the second of the two
lessons that drop two, recorded in her audit as *"p1-08 drops BALANCE and
THINK"*. Counted off her const.

── ⚖️ CFIFA, NOT FIFA ─────────────────────────────────────────────────

Design's `PHYSICS-AUDIT-2026-08-23.md` §1 records the rule: Convert ·
Formula · Insert · Fine-tune · Answer, with the C step ALWAYS present, and
`p1-08` was rebuilt from four-step FIFA onto it. Two worked examples —
*Nothing to convert* and *Convert first* — and two student attempts.

`build_ks3`'s `r_fifa` reads a list of `{letter, label, line, note}` and its
docstring says in as many words that a worked example may name its own steps
("Fine-tune", not "Fix") because MRB-204 step 3 needs it. So the five steps
are authored directly and no engine change is required.

⚠️ `fifa` is one of the four RESERVED payload keys (`cards`, `sim`, `fifa`,
`scorecards`) that `r_activity` renders itself with no opt-out. That is
exactly what is wanted here — this block IS a fifa block — but it is the
reason nothing else in P1 may carry the name.

── ⚖️ HER SCIENCE FLAG 20 IS LOAD-BEARING ─────────────────────────────

*"Force meter readings scatter ~+0.5 to +3.5%, always upward. Friction costs
energy, so measured input exceeds the ideal — never below. Rung 3 criterion 5
depends on it."*

The scatter is one-sided ON PURPOSE. A bench that scattered both ways would
show students an input smaller than the output — a machine giving energy for
free — several times per session, and the lesson's whole claim is that this
never happens. `input_bias` carries it and the renderer refuses a symmetric
one.

── ⚖️ MRB-278 · WHERE THE CORRECT ANSWER SITS ─────────────────────────

This lesson takes **3 and 1**, completing the unit's 4/4/4/4.

── ⚑ MISCONCEPTION · `ENER-19` ────────────────────────────────────────

Design's `NOTES-P1.md` §2 calls it `ENERGY-11`. It is due to resurface at P4
`moments` and P5 `hydraulics`, per her §7.
"""

LESSON = {
    "slug":  "simple-machines",
    "title": "Simple machines",
    "discipline": "physics",
    "unit": "Energy transfers",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.ECT.01"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 8}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["insulation"],
    "assumes": [],
    "references": ["conservation-of-energy"],
    "ks4_links": [],

    "meta_description": "A crowbar lifts a 600 N slab with a 100 N push and "
                        "has no motor, no battery and no moving parts. Six "
                        "times the force — so where did it come from? "
                        "Measure both ends and multiply.",

    "big_question": "A paving slab weighing 600 N will not budge. Slide a "
                    "crowbar underneath and a push of 100 N lifts it. The "
                    "bar has no motor and no battery. Where did the extra "
                    "500 N come from?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The crowbar",    "done_when": "committed"},
        {"anchor": "s-bench",  "short": "LEVER",
         "label": "Lever bench",    "done_when": "three_runs_recorded"},
        {"anchor": "s-worked", "short": "CFIFA",
         "label": "CFIFA",          "done_when": "both_attempts_opened"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Six times the force. No extra effort.",
        "prompt": "A paving slab weighing 600 N will not budge when you pull "
                  "on it. Slide a crowbar underneath, and a push of 100 N "
                  "lifts it easily. The bar has no motor, no battery and no "
                  "moving parts.",
        "commit": "Commit. Where did the extra 500 N come from?",
        "options": [
            "The bar stores energy and releases it",
            "Nowhere — you move your end much further, so the energy matches",
            "The ground pushes up with the extra force",
            "The slab weighs less once it is on the bar",
        ],
        "reveal": "Nowhere. <strong>Force is not conserved and there is "
                  "nothing strange about multiplying it</strong> — you get "
                  "six times the force and you move your end six times as "
                  "far. Multiply force by distance on each side and the two "
                  "products match. The energy is what cannot be multiplied, "
                  "and that is what the bench below measures.",
    },

    "misconceptions": [
        {"id": "ENER-19",
         "statement": "A machine that multiplies force gives you energy for "
                      "free.",
         "elicited_by": "s-hook",
         "confronted_by": "lever-bench"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "A simple machine is any device that trades force against "
                 "distance: levers, ramps, pulleys, gears, screws. None of "
                 "them creates energy, none of them reduces the energy "
                 "needed for a job, and every one of them makes a job "
                 "possible that your muscles could not do directly. "
                 "<strong>This lesson measures the trade rather than "
                 "asserting it.</strong>"},

        # ── #s-bench — bare `ks3-block` → `check`.
        {"type": "lever-bench", "id": "lever-bench",
         "anchor": "s-bench",
         "demand": "investigate",
         "targets": "ENER-19",
         "eyebrow": "The lever bench · move the fulcrum and measure",
         "heading": "Read both ends, then multiply.",
         "prompt": "A 600 N load on a 2.4 m bar. Slide the fulcrum, lift the "
                   "load by 5 cm, and record what the force meter and the "
                   "two rulers say.",
         "load": 600,
         "load_rise": 0.05,
         "bar": 2.4,
         "runs_to_record": 3,
         "gate": {
             "prompt": "Commit first. A lever lets you lift a load with a "
                       "quarter of the force. What happens to the energy you "
                       "have to supply?",
             "options": [
                 "It is a quarter as much",
                 "It is the same, and you move your end four times as far",
                 "It is four times as much",
                 "It depends on how long the lever is",
             ],
         },
         # ⚖️ Flag 20 — the scatter is ONE-SIDED and must stay so. Friction
         # costs energy, so measured input EXCEEDS the ideal, never falls
         # below it. A symmetric scatter would show a machine giving energy
         # away for free several times a session.
         "input_bias": {"min_pct": 0.5, "max_pct": 3.5},
         "columns": [
             {"id": "effort",   "label": "Your force"},
             {"id": "edist",    "label": "Your distance"},
             {"id": "ein",      "label": "Energy in"},
             {"id": "eout",     "label": "Energy out"},
         ],
         "close": "Every row has the same number in the last two columns, "
                  "whatever you did with the fulcrum — and the input column "
                  "is always a little the larger, never the smaller. That is "
                  "friction at the fulcrum taking its cut into a thermal "
                  "store. A machine changes the shape of a job; it never "
                  "changes the size of it, and it never does it for less."},

        # ── #s-balance — bare `ks3-block` → `check`. THE FORMULA BLOCK.
        # ⚠️ A SECTION, NOT A RAIL STOP.
        {"type": "formula", "id": "the-lever-rule",
         "anchor": "s-balance",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "force on one side × distance on that side = force on "
                      "the other side × distance on that side",
         "support": ["force is measured in newtons (N)",
                     "distance is measured in metres (m)",
                     "their product, the energy, is in joules (J)"],
         # ⚖️ MRB-204. The BEAM is the relationship: two products either side
         # of an equals sign, which no triangle can hold.
         "figure": {
             "shape": "balance",
             "aria_label": "A balance beam, level. On the left pan: your "
                           "force multiplied by your distance. On the right "
                           "pan: the load's force multiplied by the load's "
                           "distance. The two products are equal.",
             "pans": {"left": "your force × your distance",
                      "right": "load force × load distance"},
             "caption": "two products, balanced"},
         # ⚖️ MRB-204. The TRIANGLE is legitimate HERE, because solving for
         # one factor inside ONE side is a genuine product relationship.
         # Design's own `COVERS` map carries these three results verbatim,
         # and her fourth entry says explicitly that the whole relationship
         # cannot go on a triangle — which is why the BEAM above is the
         # figure and this is only ever one side of it.
         #
         # ⚠️ `triangle`, NOT `cover`. `r_formula` reads three separate keys:
         # `figure` draws the relationship's own shape, `triangle` is the
         # MRB-204 formula triangle (top/left/right), and `cover` is a
         # part-whole BAR. A triangle authored under `cover` renders as a bar
         # — which for `c2-06` is right, because conservation of mass is a
         # sum, and for a product here would be wrong.
         "triangle": {
             "eyebrow": "One side at a time",
             "heading": "Which quantity are you solving for?",
             "aria_label": "Formula triangle: energy transferred on top, "
                           "force and distance side by side below",
             "top": {
                 "label": "E",
                 "button": "Cover E",
                 "text": "Energy is alone at the top. Cover it and the other "
                         "two sit side by side — multiply."},
             "left": {
                 "label": "F",
                 "button": "Cover F",
                 "text": "Force sits underneath with energy above it. Cover "
                         "F and you are left with E over d — divide."},
             "right": {
                 "label": "d",
                 "button": "Cover d",
                 "text": "Distance sits underneath with energy above it. "
                         "Cover d and you are left with E over F — divide."},
             "close": "Two things side by side means multiply. One thing "
                      "over another means divide. This triangle is for ONE "
                      "side of the lever rule: the rule itself has four "
                      "quantities and an equals sign, not three quantities "
                      "and a bar, so read that off the beam above."}},

        # ── #s-worked — bare `ks3-block` → `check`. CFIFA.
        # ⚠️ TWO worked examples, because Design draws two: her Cfifa
        # component has a `Nothing to convert` tab and a `Convert first`
        # tab. The engine's `worked-example` renders ONE `fifa` list, so the
        # two tabs become two blocks in document order. Only the first
        # carries the anchor — `#s-worked` is one rail stop, not two.
        {"type": "worked-example", "id": "cfifa-lever-plain",
         "anchor": "s-worked"},
        {"type": "worked-example", "id": "cfifa-lever-convert"},

        # ── #s-think — `ks3-block ks3-misconception` → `misconception`.
        # ⚠️ A SECTION, NOT A RAIL STOP.
        {"type": "misconception", "id": "think-free-energy",
         "anchor": "s-think", "targets": "ENER-19"},

        {"type": "key-fact", "id": "never-both-never-energy",
         "ground": "card",
         "text": "A machine can multiply force or multiply distance, but "
                 "never both, and never energy. The energy you put in at "
                 "your end is always at least the energy that comes out at "
                 "the load end — the rest goes to friction."},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "activities": [
        # ⊕ CFIFA · five steps, the C always present. Her audit §1 records the
        # rebuild from four-step FIFA onto this shape across nineteen lessons.
        {"id": "cfifa-lever-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Five lines, every time · CFIFA",
         "heading": "You push a lever with 250 N and your end moves 0.12 m. "
                    "How much energy do you transfer?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "staged": True,
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Now the same five steps where the units "
                                  "do need converting."},
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "250 N stays 250 N · 0.12 m stays 0.12 m",
              "note": "The force is already in newtons and the distance "
                      "already in metres, so there is nothing to convert. "
                      "The step still gets written down — that is how you "
                      "notice the times there IS something."},
             {"letter": "F", "label": "Formula",
              "line": "E = F × d",
              "note": "Cover E on the triangle: F sits beside d, so you "
                      "multiply."},
             {"letter": "I", "label": "Insert",
              "line": "E = 250 N × 0.12 m",
              "note": "The distance is how far YOUR end moved, not how far "
                      "the load rose. Those are different numbers and this "
                      "is where they get swapped."},
             {"letter": "F", "label": "Fine-tune",
              "line": "250 × 0.12 = 30",
              "note": "Newtons times metres gives joules."},
             {"letter": "A", "label": "Answer",
              "line": "E = 30 J",
              "note": "Thirty joules in at your end — and the load end can "
                      "never get more than that."},
         ]},

        {"id": "cfifa-lever-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "The same five lines · when the units do not match",
         "heading": "You push a crate up a ramp with 80 N and it moves "
                    "250 cm along the slope.",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "staged": True,
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "The C step is why the answer is 200 J "
                                  "and not 20 000."},
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "250 cm ÷ 100 = 2.50 m",
              "note": "A joule is a newton times a metre, and a centimetre "
                      "is a hundredth of one, so divide by 100."},
             {"letter": "F", "label": "Formula",
              "line": "E = F × d",
              "note": "Cover E on the triangle: F sits beside d, so you "
                      "multiply."},
             {"letter": "I", "label": "Insert",
              "line": "E = 80 N × 2.50 m",
              "note": "The converted distance goes in. The 250 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "80 × 2.50 = 200",
              "note": "Newtons times metres gives joules."},
             {"letter": "A", "label": "Answer",
              "line": "E = 200 J",
              "note": "Insert 250 instead of 2.50 and the answer comes out "
                      "20 000 J — a hundred times too big."},
         ]},

        {"id": "think-free-energy",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-19",
         "statements": [
             {"targets": "ENER-19",
              "quote": "A machine that multiplies force gives you energy for "
                       "free.",
              "body": [
                  "Force and energy are different quantities, and only one "
                  "of them is conserved. Nothing forbids multiplying a force "
                  "— a lever does it, a ramp does it, your own forearm does "
                  "it in reverse every time you lift something. What is "
                  "forbidden is getting more energy out than you put in, and "
                  "no arrangement of levers has ever managed it.",
                  "Your own runs are the argument. Every row of the table "
                  "has the same number in the last two columns, whatever you "
                  "did with the fulcrum. Six times the force, one sixth of "
                  "the distance, identical product. A machine changes the "
                  "shape of a job so your muscles can do it; it never "
                  "changes the size of the job.",
                  "And in reality the last column is always slightly the "
                  "larger of the two, because friction at the fulcrum takes "
                  "its cut into a thermal store. Real machines need a little "
                  "more energy in than the job strictly requires — never "
                  "less.",
              ]},
             {"quote": "A longer lever gets the job done with less energy.",
              "body": [
                  "It gets it done with less FORCE, and you pay for that in "
                  "distance. Double the length of your side and you halve "
                  "the force needed, but your end has to travel twice as far "
                  "— and force × distance, which is the energy, comes out "
                  "the same. Every simple machine trades one for the other "
                  "along a line of fixed energy, and friction means the "
                  "trade is always slightly in the machine’s favour, "
                  "never in yours.",
              ]},
         ]},
    ],

    "figures": [],
    "key_facts": [],

    "ladder": {
        "recall": {
            "q": "You push down with 150 N and your end of the lever moves "
                 "40 cm. How much energy did you transfer?",
            # MRB-278: correct at index 3.
            "options": ["6000 J", "375 J", "190 J", "60 J"],
            "answer": 3,
            "feedback": {
                0: "Watch the units — 40 cm is 0.40 m, not 40 m. "
                   "150 × 0.40 = 60.",
                1: "That is 150 ÷ 0.40. Energy is force multiplied by "
                   "distance, not divided.",
                2: "That is 150 + 40. The two quantities are multiplied, and "
                   "they are not even in the same units.",
            }},
        "apply": {
            "q": "A ramp lets you push a 900 N barrel up to a platform using "
                 "only 300 N. What must be true?",
            # MRB-278: correct at index 1.
            "options": [
                "You transfer a third of the energy you would lifting it "
                "straight up",
                "You push it three times as far along the ramp as the "
                "platform is high",
                "The ramp supplies the other 600 N from somewhere",
                "The barrel weighs less on the ramp",
            ],
            "answer": 1,
            "feedback": {
                0: "The energy is the same — that is the point. Only the "
                   "force is a third.",
                2: "A ramp has no energy supply. It changes the direction "
                   "and the distance, nothing else.",
                3: "Its weight has not changed. What changed is how much of "
                   "that weight you have to work against at once.",
            }},
        "explain": {
            "q": "Using your own results from the lever bench, explain why a "
                 "lever cannot give you energy for free — and explain why "
                 "your measured input was always slightly larger than the "
                 "output.",
            "field_label": "Your explanation",
            "placeholder": "In every run, force times distance at my end…",
            "success": [
                "Says force multiplied by distance at the effort end equals "
                "force multiplied by distance at the load end.",
                "Says a smaller force is always paid for with a larger "
                "distance.",
                "Says the energy is the product, and the product does not "
                "change when the fulcrum moves.",
                "Says force is not a conserved quantity, so multiplying it "
                "breaks no law.",
                "Says the measured input exceeded the output because "
                "friction at the fulcrum fills a thermal store — and that it "
                "was never smaller.",
            ]},
        "produce": {
            "q": "A gear system is advertised as “doubling the "
                 "power of your drill for free”. Explain what it can "
                 "and cannot do, and say what you would measure to check the "
                 "claim.",
            "field_label": "Your answer",
            "placeholder": "Gears can multiply turning force…",
            "success": [
                "Says gears can multiply turning force, which is allowed.",
                "Says the faster-turning side must then turn more slowly, or "
                "through fewer turns.",
                "Says the energy transferred per second cannot be increased "
                "by the gears.",
                "Identifies “power” as energy per second, so "
                "“doubling the power for free” is the claim "
                "that is wrong.",
                "Names a measurement: compare energy in and energy out over "
                "the same time, and check whether anything gets warm.",
            ]},
    },

    "key_note": "A simple machine trades force against distance and the "
                "product of the two — the energy — is what stays fixed. "
                "Multiply the force and you divide the distance by the same "
                "amount. Friction means you always put in a little more than "
                "comes out, and never less.",

    "stretch": [
        # ⚖️ Design's flag 21 asks for the 1911 date to be checked. It matches
        # the standard citation for the USPTO's practice of requiring a
        # working model for perpetual-motion applications; left as drawn and
        # flagged to Mide as a historical rather than a scientific claim.
        {"type": "explainer", "id": "the-patent-office-rule",
         "text": "People have been trying to build a machine that gives out "
                 "more than it takes in for at least eight hundred years, "
                 "and the applications never stopped arriving — so in 1911 "
                 "the US Patent Office simply refused to consider such "
                 "applications without a working model, which nobody has "
                 "ever produced. What makes the whole class impossible is "
                 "not a flaw in any particular design; it is the sum you "
                 "have been checking all lesson. If force × distance in must "
                 "equal force × distance out, there is nothing left over to "
                 "run the machine with, no matter how the linkages are "
                 "arranged. <strong>Conservation of energy does not need to "
                 "inspect your invention to know it will not work.</strong>"},
    ],

    "support": [],

    "vocabulary": [
        {"term": "simple machine",
         "definition": "A device that trades force against distance — a "
                       "lever, ramp, pulley, gear or screw. It never creates "
                       "energy."},
        {"term": "lever",
         "definition": "A rigid bar that turns about a fulcrum. Force on one "
                       "side times its distance equals force on the other "
                       "side times its distance."},
        {"term": "fulcrum",
         "definition": "The fixed point a lever turns about. Moving it "
                       "changes how the force and distance are traded."},
        {"term": "work done",
         "definition": "Energy transferred by a force moving through a "
                       "distance. Calculated as force × distance, in joules."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why multiplying force is allowed but "
                      "multiplying energy is not?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Moments and the principle of moments, work done as a "
                   "calculated quantity, and efficiency expressed as a "
                   "percentage of the energy supplied.",

    "ws": ["measurement", "analysis-and-evaluation"],
}
