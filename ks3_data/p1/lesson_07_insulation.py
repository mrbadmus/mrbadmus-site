"""p1-07 — *Insulation*.

Ported from Claude Design's `p1-07-insulation.dc.html`.

── WHAT THIS LESSON OWNS ───────────────────────────────────────────────

`KS3.P.ECT.02d` — "use of insulators", the last quarter of the compound
heating bullet.

── ⚖️ THE FAMILY IS `INVESTIGATION`, AND DESIGN SAYS SO ───────────────

Her science flag 19: *"the plan-the-trial section marks variable control
before any data exists. INVESTIGATION-family requirement."* `#s-plan` comes
BEFORE `#s-trial` on her page and the rail, so a student decides what may
vary before seeing a single reading. That ordering is the family's whole
point and is not rearranged.

── ⚠️ FIVE SECTIONS, FOUR RAIL STOPS ──────────────────────────────────

Her `RAIL` const is `[s-hook, s-plan, s-trial, s-ladder]`. `#s-ice` AND
`#s-think` are sections with ids and no stops — this lesson is one of the
two that drop a second one, which her `PHYSICS-AUDIT` §3 records as
*"p1-07 drops ICE and THINK"*. Counted off her const, not off the prose.

── ⚖️ THE ICE TRIAL IS THE ONLY DECISIVE EVIDENCE, AND IT IS NOT CUT ───

Design's flag 18, quoted because it is an instruction: *"the ice trial is
the only decisive evidence in the lesson. Hot-water cooling curves alone are
consistent with 'insulation adds warmth'; only the ice result rules it out.
Do not cut it for length."*

That is exactly right and it is worth stating why. Every hot-water curve in
`#s-trial` shows a wrapped beaker staying hotter, which is equally well
explained by the wool being a source of warmth. The ice is the control that
separates the two accounts: if wool added warmth, wrapped ice would melt
FASTER. It melts about four times slower. Only "insulation slows a flow,
whichever way the flow is going" survives both trials.

── ⚖️ MRB-278 · WHERE THE CORRECT ANSWER SITS ─────────────────────────

This lesson takes **2 and 0**.

── ⚑ MISCONCEPTION · `ENER-18` ────────────────────────────────────────

Design's `NOTES-P1.md` §2 calls it `ENERGY-10`; the prefix is `ENER` and the
numbering continues from `ENER-17`.
"""

LESSON = {
    "slug":  "insulation",
    "title": "Insulation",
    "discipline": "physics",
    "unit": "Energy transfers",
    "family": "INVESTIGATION",

    "covers": ["KS3.P.ECT.02d"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 7}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["radiation"],
    "assumes": [],
    "references": [],
    "ks4_links": [],

    "meta_description": "Wrap an ice cube in a thick woolly blanket and it "
                        "lasts four times longer. Plan the trial, run the "
                        "cooling curves, and find the one result that rules "
                        "out insulation being a source of warmth.",

    "big_question": "Two identical ice cubes. One in the open air, one "
                    "wrapped in a thick woollen blanket — the sort you would "
                    "call warm. Which melts first?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Ice in a blanket", "done_when": "committed"},
        {"anchor": "s-plan",   "short": "PLAN",
         "label": "Plan the trial",   "done_when": "all_five_decided"},
        {"anchor": "s-trial",  "short": "TRIAL",
         "label": "Cooling curves",   "done_when": "run_to_28_minutes"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",   "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "An ice cube in a blanket.",
        "prompt": "Two identical ice cubes on the same bench in the same "
                  "room. One sits in the open air. The other is wrapped in a "
                  "thick woollen blanket — the sort you would call warm.",
        "commit": "Commit before the trial runs.",
        "options": [
            "Faster — the blanket is warm, so it heats the ice",
            "Slower — the blanket slows the flow of energy into the ice",
            "At the same rate — insulation only works on hot things",
            "It will not melt at all while wrapped",
        ],
        "reveal": "The wrapped one lasts far longer. If a blanket were a "
                  "source of warmth, wrapping ice in it would be the fastest "
                  "way to melt it — and it is the slowest. <strong>A blanket "
                  "does not make warmth. It slows a flow.</strong> That is "
                  "the whole lesson, and the trial below lets you prove it "
                  "with numbers.",
    },

    "misconceptions": [
        {"id": "ENER-18",
         "statement": "A blanket, a woolly hat or a coat is a source of "
                      "warmth — insulation adds heat to what it wraps.",
         "elicited_by": "s-hook",
         "confronted_by": "ice-trial"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "An insulator is a material that lets energy through only "
                 "slowly. Nothing about that definition mentions warmth, and "
                 "nothing in it says which way the energy is going — which "
                 "is why the same foam box carries hot chips home and keeps "
                 "ice cream frozen. This lesson plans a trial, runs it, and "
                 "then runs the one version of it that can tell two "
                 "explanations apart."},

        # ── #s-plan — bare `ks3-block` → `check`.
        # ⚖️ Flag 19 — variable control is marked BEFORE any data exists.
        # This is the INVESTIGATION family's requirement and the reason this
        # section precedes the trial on her rail.
        {"type": "plan-the-trial", "id": "plan-the-trial",
         "anchor": "s-plan",
         "demand": "evaluate",
         "eyebrow": "Plan the trial · what you change and what you must not",
         "heading": "One variable at a time",
         "prompt": "Before running anything, decide which of these you are "
                   "allowed to vary between the beakers. Get this wrong and "
                   "the results mean nothing.",
         "choices": ["Change it", "Keep it the same"],
         "sort_items": [
             {"id": "v1", "text": "The wrapping around the beaker",
              "answer": "Change it",
              "right": "Change it — this is the independent variable, the "
                       "one thing the trial is about.",
              "wrong": "This is the whole point of the trial. If every "
                       "beaker has the same wrapping you learn nothing."},
             {"id": "v2", "text": "The volume of water in each beaker",
              "answer": "Keep it the same",
              "right": "Keep it the same. More water cools more slowly "
                       "whatever the wrapping, so this would confound the "
                       "result.",
              "wrong": "Vary this and you cannot tell whether a slow cooler "
                       "was well insulated or just fuller."},
             {"id": "v3", "text": "The starting temperature",
              "answer": "Keep it the same",
              "right": "Keep it the same. A hotter start means a faster "
                       "initial drop, which would look like poor "
                       "insulation.",
              "wrong": "Different starting temperatures give different "
                       "cooling rates on their own. That difference would "
                       "swamp the one you are looking for."},
             {"id": "v4", "text": "The room the beakers stand in",
              "answer": "Keep it the same",
              "right": "Keep it the same. Cooling depends on the difference "
                       "between the water and the room.",
              "wrong": "Put one beaker by a window and one by a radiator and "
                       "the wrapping becomes irrelevant."},
             {"id": "v5", "text": "The times at which you read each "
                                  "thermometer",
              "answer": "Keep it the same",
              "right": "Keep it the same. Readings have to be simultaneous "
                       "to be comparable.",
              "wrong": "Reading one beaker at 5 minutes and another at 12 "
                       "gives you two unrelated numbers, not a comparison."},
         ],
         "close": "One thing changes and everything else is held. That is "
                  "not a rule about tidiness — it is the only arrangement in "
                  "which a difference at the end can be blamed on the "
                  "wrapping rather than on something else."},

        # ── #s-trial — bare `ks3-block` → `check`.
        {"type": "insulation-trial", "id": "insulation-trial",
         "anchor": "s-trial",
         "demand": "investigate",
         "eyebrow": "The insulation trial · run it and record",
         "heading": "Cooling curves, side by side.",
         "prompt": "Four beakers, each with 200 ml of water at 80 °C, in a "
                   "20 °C room. Different wrappings. Run the clock and watch "
                   "them separate.",
         "start_temp": 80,
         "room_temp": 20,
         "jump_to": 30,
         "done_at": 28,
         "beakers": [
             {"id": "bare", "label": "Nothing (control)", "k": 1.0,
              "blocks": "None — this is the comparison"},
             {"id": "foil", "label": "Shiny foil", "k": 0.74,
              "blocks": "Radiation, reflected back"},
             {"id": "wool", "label": "Wool, 1 layer", "k": 0.5,
              "blocks": "Conduction and convection — trapped air"},
             {"id": "wool3", "label": "Wool, 3 layers + lid", "k": 0.26,
              "blocks": "All three — more trapped air, lid stops convection"},
         ],
         # ⚠️ THE CURVES ALONE DO NOT DECIDE ANYTHING, AND THE NOTE SAYS SO.
         # Every one of them is equally consistent with the wool being a
         # source of warmth. That is what makes the ice trial necessary
         # rather than decorative.
         "close": "Every wrapped beaker stayed hotter than the control, and "
                  "the best one stayed hottest. Notice what this does NOT "
                  "prove: a blanket that ADDED warmth would give exactly "
                  "these curves too. Both explanations fit every number on "
                  "this table, which is why the trial below exists."},

        # ── #s-ice — `ks3-block ks3-dark ks3-practical` → `practical`.
        # ⚠️ A SECTION, NOT A RAIL STOP.
        {"type": "ice-trial", "id": "ice-trial",
         "anchor": "s-ice",
         "demand": "evaluate",
         "targets": "ENER-18",
         "eyebrow": "The decisive trial · run it the other way round",
         "heading": "Now insulate something cold",
         "prompt": "Everything so far kept hot water hot, which is "
                   "consistent with a blanket being a source of warmth. This "
                   "trial is not. Same wrappings, ice instead of hot water.",
         "bare_minutes": 14,
         "wrapped_minutes": 54,
         "notes": {
             "rest":    "Two identical cubes, one wrapped. If the wool were "
                        "a source of warmth, the wrapped one would be gone "
                        "first. Run it.",
             "early":   "Watch which one shrinks faster. The blanket is "
                        "doing the opposite of what its name suggests.",
             "decided": "The unwrapped cube has gone and the wrapped one is "
                        "still mostly ice. This is the observation that "
                        "decides it.",
             "done":    "Both melted — but the unwrapped cube was gone in "
                        "about fourteen minutes and the wrapped one took "
                        "nearly four times as long. Wrapping ice in a "
                        "“warm” blanket keeps it frozen. There is "
                        "no version of “insulation adds heat” "
                        "that survives this result.",
         }},

        # ── #s-think — `ks3-block ks3-misconception` → `misconception`.
        # ⚠️ A SECTION, NOT A RAIL STOP. This lesson drops two.
        {"type": "misconception", "id": "think-hat-warms",
         "anchor": "s-think", "targets": "ENER-18"},

        {"type": "key-fact", "id": "insulation-slows-a-flow",
         "ground": "card",
         "text": "An insulator slows the transfer of energy. It does not add "
                 "warmth and it does not care which way the energy is going "
                 "— which is why the same box keeps chips hot and ice "
                 "cream frozen."},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "activities": [
        {"id": "think-hat-warms",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-18",
         "statements": [
             {"targets": "ENER-18",
              "quote": "A woolly hat warms your head.",
              "body": [
                  "A hat has no energy supply. It cannot warm anything. What "
                  "warms your head is your own body, running at about 100 W "
                  "from your chemical store, and the hat simply slows the "
                  "rate at which that energy escapes. Take the hat off a "
                  "dead thermos flask and nothing happens — because there "
                  "was never any warmth in the hat to begin with.",
                  "The ice trial is the proof, and it is worth being precise "
                  "about why. If insulation warmed things, wrapped ice would "
                  "melt faster. It melts slower. The only description that "
                  "fits both trials is that insulation slows the flow, "
                  "whichever way the flow happens to be going — hot water "
                  "stays hot longer and ice stays frozen longer, from the "
                  "same property. That is why the same foam box carries "
                  "chips home and carries a transplant organ to hospital.",
              ]},
         ]},
    ],

    "figures": [],
    "key_facts": [],

    "ladder": {
        "recall": {
            "q": "What makes wool a good insulator?",
            # MRB-278: correct at index 2.
            "options": [
                "Wool produces warmth of its own",
                "Wool is a good conductor, so it spreads the heat evenly",
                "It traps pockets of air, and air conducts very badly",
                "It reflects radiation like a mirror",
            ],
            "answer": 2,
            "feedback": {
                0: "No material produces warmth without an energy supply. "
                   "Wool has none.",
                1: "A good conductor would be a bad insulator — that is the "
                   "opposite of what is wanted.",
                3: "Shiny foil does that. Wool works by trapping air.",
            }},
        "apply": {
            "q": "An ice cube wrapped in a thick blanket is compared with an "
                 "identical one left in the open. What happens?",
            # MRB-278: correct at index 0.
            "options": [
                "The wrapped one melts more slowly",
                "The wrapped one melts faster, because blankets are warm",
                "They melt at the same rate — insulation only works on hot "
                "things",
                "The wrapped one never melts at all",
            ],
            "answer": 0,
            "feedback": {
                1: "This is exactly the misconception. A blanket has no "
                   "warmth of its own to give.",
                2: "Insulation slows flow in either direction. Nothing about "
                   "it prefers hot to cold.",
                3: "It is slowed, not stopped. Given long enough it reaches "
                   "room temperature like everything else.",
            }},
        "explain": {
            "q": "A vacuum flask keeps tea hot for hours. Explain how it "
                 "blocks all three methods of energy transfer.",
            "field_label": "Your explanation",
            "placeholder": "The gap between the walls has no air…",
            "success": [
                "Says the gap between the two walls is a vacuum with no "
                "particles.",
                "Says this stops conduction across the gap, because there is "
                "nothing to pass energy along.",
                "Says this stops convection, because there is no fluid that "
                "could move.",
                "Says the silvered surfaces reflect radiation back instead "
                "of absorbing it.",
                "Says the stopper or lid blocks the convection route out of "
                "the top.",
            ]},
        "produce": {
            "q": "A takeaway uses the same foam boxes for hot chips and for "
                 "ice cream, and a customer says one of those must be a "
                 "mistake. Explain why both work, using your ice trial as "
                 "evidence.",
            "field_label": "Your answer",
            "placeholder": "Insulation slows the transfer of energy…",
            "success": [
                "Says insulation slows the transfer of energy rather than "
                "adding or removing it.",
                "Says with hot chips the flow is outwards, and the box slows "
                "it.",
                "Says with ice cream the flow is inwards, from the warmer "
                "room, and the box slows that too.",
                "Says the same property does both jobs — nothing about the "
                "box has to change.",
                "Uses the ice trial as the evidence: wrapped ice lasted "
                "longer, which rules out the box being a source of warmth.",
            ]},
    },

    "key_note": "An insulator slows a flow of energy; it never adds warmth. "
                "The proof is the ice: if insulation warmed things, wrapped "
                "ice would melt faster, and it lasts about four times "
                "longer.",

    "stretch": [
        {"type": "explainer", "id": "why-a-house-loses-most-through-the-roof",
         "text": "Every route in this unit shows up in one place: the energy "
                 "bill for a house. Warm air rises, so convection carries "
                 "energy to the ceiling and out through the roof, which is "
                 "why loft insulation is the cheapest saving available and "
                 "why it works by trapping air rather than by blocking "
                 "anything. Conduction leaves through solid walls, which is "
                 "why cavity walls exist and why the cavity is filled with "
                 "foam rather than left as a gap — a gap would simply "
                 "convect. Radiation leaves through glass, which is why "
                 "double glazing is coated with a thin metal film you cannot "
                 "see. Three routes, three different fixes, and a builder "
                 "who confuses them wastes the money on the wrong wall."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "insulator",
         "definition": "A material that lets energy through only slowly. It "
                       "slows a transfer in either direction and never adds "
                       "warmth of its own."},
        {"term": "independent variable",
         "definition": "The one thing you deliberately change in a trial. "
                       "Here, the wrapping on the beaker."},
        {"term": "control variable",
         "definition": "Something you deliberately keep the same, so that a "
                       "difference in the results can be blamed on the "
                       "independent variable."},
        {"term": "cooling curve",
         "definition": "A graph of temperature against time as something "
                       "cools. Steeper at the start, because the "
                       "temperature difference is greatest then."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why a blanket cannot warm anything?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Rate of cooling and thermal conductivity treated "
                   "quantitatively, and the design of a building's whole "
                   "thermal envelope.",

    "ws": ["experimental-skills-and-investigations",
           "analysis-and-evaluation"],
}
