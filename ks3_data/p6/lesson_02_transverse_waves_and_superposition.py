"""P6 L2 — Transverse waves, reflection and superposition (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p6/p6-02-transverse-waves-and-superposition.dc.html`.

Her page wins outright. The two stones, the three-lane channel, the
part–whole bar, both worked examples and all four rungs are hers.

── ⚖️ MRB-204 · A PART–WHOLE BAR, AND IT KEEPS ITS COVER BUTTONS ─────

`R = a + b` is a SUM. A triangle here would teach a product that does not
exist, so the figure is a part–whole bar — and unlike P5's stack and
balance it KEEPS its buttons, because covering a part asks a real
question: *what is left?* That is the split Design's flag 0a draws, and it
is why `p6-02` and `p6-07` take the engine's own `r_cover_bar` while
`p5-02`, `p5-03` and `p5-04` do not.

The out-of-step case, `R = a − b`, is the one permitted extra display
line.

── ⚖️ RULED · ZERO DRAWS A FLAT TRACE, NOT AN ABSENT LANE ────────────

A wave of 0 mm amplitude is a real state — one paddle switched off — and
it is different from cancelling. Design's note for it says so in terms:
*"this is not cancelling — cancelling needs two waves, and there are
none."* `WAVE-06` is *if the water is flat the energy has gone*, and that
branch is where it is met.

── ⚖️ RULED · THE EXACT CANCEL IS ITS OWN BRANCH ─────────────────────

Both waves are still there, and both leave the overlap unchanged at their
original height. That is `WAVE-05` — *when two waves cancel they destroy
each other* — and it needs its own sentence rather than being the small
end of the partly-cancelling one.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-meet · s-bar · s-ladder

⚠️ **MRB-208** — the `s-bar` id goes on the attempt panel, which is what
Design's `s.buildOpen` is set by.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    WAVE-05  when two waves cancel they destroy each other
    WAVE-06  if the water is flat the energy has gone
    WAVE-07  two waves meeting average out
    WAVE-08  the stronger wave wins and the weaker one disappears

`WAVE-06` has no `elicited_by`, which §5.3 allows. `WAVE-08` is not in
Design's table — it arrived with the hook's third option, and it is
separate from `WAVE-07`: averaging is an arithmetic error, and winning is
a claim that one wave stops existing.
"""

LESSON = {
    "slug":  "transverse-waves-and-superposition",
    "title": "Transverse waves, reflection and superposition",
    "discipline": "physics",
    "unit": "Waves and sound",
    "family": "MODEL",

    "covers": ["KS3.P.OBW.01b", "KS3.P.OBW.01c"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["waves-on-water"],
    "assumes": [],
    "references": ["waves-on-water", "echoes-reflection-and-absorption"],
    "ks4_links": [],

    "meta_description": "Two stones into one pond, and some patches of the "
                        "crossing pattern heave twice as far while others "
                        "never move. The surface obeys both waves at once, "
                        "and the arithmetic for that is the whole lesson.",

    "big_question": "Two waves arrive at the same patch of water and each "
                    "one wants the surface somewhere different. The surface "
                    "obeys both at once, and the arithmetic for that is the "
                    "whole lesson.",

    "rail": [
        {"anchor": "s-hook",   "short": "STONES",
         "label": "Two stones, one pond",   "done_when": "committed"},
        {"anchor": "s-meet",   "short": "MEET",
         "label": "Where two waves meet",   "done_when": "gate_and_a_control"},
        {"anchor": "s-bar",    "short": "CFIFA",
         "label": "The bar and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Two stones, one pond, and patches of water that never "
                 "move.",
        "prompt": "Drop two stones into still water at the same moment, a "
                  "metre apart. Two sets of rings spread out and run into "
                  "each other. Where they cross, some patches of the surface "
                  "heave twice as far as either ring on its own. Others sit "
                  "almost dead flat while rings pour through them from both "
                  "sides.",
        "commit": "At a spot where the two sets of ripples are crossing, "
                  "what is the water doing?",
        "options": [
            "The two waves bounce off each other where they meet, and neither "
            "carries on past it",
            "The two join into one new wave and the original two are gone, "
            "because one place holds one wave",
            "At every point the two displacements add: up with up makes a "
            "bigger up, up with down cancels",
            "The stronger set of ripples wins where they meet, and the weaker "
            "set disappears for good",
        ],
        "answer": 2,
        "reveal": "The surface cannot be in two places, so it does the only "
                  "thing left: it goes to the sum of what each wave was "
                  "asking for. A 6 mm lift and a 6 mm lift make a 12 mm "
                  "lift. A 6 mm lift and a 6 mm drop make no movement at "
                  "all. Adding the two displacements at every point is "
                  "called <strong>superposition</strong>, and it is the "
                  "whole of what happens where waves meet.",
    },

    "misconceptions": [
        {"id": "WAVE-05",
         "statement": "When two waves cancel they destroy each other.",
         "elicited_by": "meet",
         "confronted_by": "meet"},
        {"id": "WAVE-06",
         "statement": "If the water is flat the energy has gone.",
         "confronted_by": "meet"},
        {"id": "WAVE-07",
         "statement": "Two waves meeting average out.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
        {"id": "WAVE-08",
         "statement": "The stronger wave wins and the weaker one "
                      "disappears.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A wave on water is <strong>transverse</strong>: the "
                 "surface moves up and down, at right angles to the "
                 "direction the wave is travelling. That up-or-down amount "
                 "at a point is its <strong>displacement</strong>, and it is "
                 "a displacement rather than a distance because it has a "
                 "direction — up counts as positive, down as negative."},
        {"type": "explainer",
         "text": "Waves on water also <strong>reflect</strong>. Put a "
                 "barrier across a tank and a wave train bounces back off it "
                 "and travels the other way, still a wave, still the same "
                 "wavelength. And when two waves are in the same water at "
                 "the same time, the surface takes the sum of both "
                 "displacements at every point. Two crests arriving together "
                 "give a bigger crest — the waves <strong>add</strong>. A "
                 "crest arriving with a trough of the same size gives flat "
                 "water — the waves <strong>cancel</strong>. Both are "
                 "superposition; nothing else is happening."},

        # ── #s-meet · two wave trains sent along one channel ───────────
        {"type": "superposition-lanes",
         "id": "meet",
         "anchor": "s-meet",
         "eyebrow": "At the bench · two wave trains sent along one channel",
         "heading": "Set two waves going. Read the third.",
         "progress": "Move a control to begin",
         "lead": "Two paddles at the same end of a narrow channel, both "
                 "laying crests 500 mm apart. Set the height of each, and "
                 "set whether the second one starts crest-with-crest or "
                 "crest-with-trough.",
         "px_per_mm": 2.5,
         "start_in_step": True,
         "label_a": "WAVE A",
         "label_b": "WAVE B",
         "label_r": "WHERE THEY MEET",
         "phase_label": "How B arrives",
         "gate": {
             "prompt": "Commit first. Two waves of exactly the same height "
                       "meet crest on trough. What is the water doing where "
                       "they overlap?",
             "options": [
                 "It heaves twice as far, because two waves are arriving "
                 "instead of one",
                 "It lies flat while they overlap, and both waves carry on "
                 "out the far side",
                 "Both waves stop dead at the overlap and nothing travels "
                 "on",
                 "The wave that got there first keeps going and the other "
                 "one is blocked",
             ],
             "answer": 1,
         },
         "lanes": [
             {"id": "a", "label": "Wave A", "min": 0, "max": 20, "step": 2,
              "start": 8, "value": "8 mm"},
             {"id": "b", "label": "Wave B", "min": 0, "max": 20, "step": 2,
              "start": 6, "value": "6 mm"},
         ],
         "phases": [
             {"in_step": True, "label": "Crest on crest"},
             {"in_step": False, "label": "Crest on trough"},
         ],
         "branches": {
             "none": "Neither paddle is moving, so there is nothing to add: "
                     "the channel reads 0 mm all the way along. This is not "
                     "cancelling — cancelling needs two waves, and there are "
                     "none.",
             "one_only": "Only wave {only} is running, at {r} mm, so the "
                         "bottom trace is a copy of it. With nothing to add "
                         "to and nothing to cancel against, crest-on-crest "
                         "and crest-on-trough give the same {r} mm.",
             "adding": "Crest on crest: {a} mm and {b} mm both lift the "
                       "surface at the same moment, so the water goes to "
                       "{a} + {b} = {r} mm. Send the same two waves crest on "
                       "trough and the same water reads {diff} mm instead. "
                       "Nothing about either paddle has changed — only when "
                       "the second one starts.",
             "cancels_exactly": "Crest on trough, and both waves are {a} mm: "
                                "one lifts the surface by exactly as much as "
                                "the other drops it, so the water reads 0 mm "
                                "and lies flat. Both waves are still there, "
                                "and both leave the overlap at {a} mm.",
             "partly": "Crest on trough: the {small} mm wave cancels {small} "
                       "mm of the {big} mm one, leaving {big} − {small} = "
                       "{r} mm. Only an exact match cancels to nothing, and "
                       "these two are {gap} mm apart.",
         },
         "readouts": [
             {"id": "a", "label": "Wave A alone"},
             {"id": "b", "label": "Wave B alone"},
             {"id": "r", "label": "Where they meet"},
             {"id": "verdict", "label": "What the two are doing"},
         ]},

        {"type": "formula",
         "id": "superposition-rule",
         "eyebrow": "The relationship · a bar, not a triangle",
         "statement": "Where two waves meet, the surface takes the sum of "
                      "both displacements.",
         "support": [
             "Crest on crest: R = a + b",
             "Crest on trough: R = a − b",
             "Every height is measured from the still level, in millimetres.",
         ],
         # ⚖️ A PART–WHOLE BAR KEEPS ITS COVER BUTTONS. Covering a part
         # asks a real question here — unlike P5's stack, where covering a
         # layer of water asks nothing.
         # ⚖️ MRB-204 · A SUM TAKES A BAR, and Design drew one. The weights
         # ARE the arithmetic — 8 and 6 make the 14 the whole bar is — so
         # the two parts fill the whole to the pixel rather than being laid
         # out to look as though they do.
         "cover": {
             "shape": "bar",
             "eyebrow": "The bar",
             "heading": "Cover the one you want",
             "aria_label": "A bar model. One long bar is the displacement "
                           "where the two waves meet. Underneath, the same "
                           "length is split into two: wave A alone and wave "
                           "B alone. Covering one leaves the way to work it "
                           "out.",
             "whole": {"id": "R", "label": "R — where they meet",
                       "button": "Cover R"},
             "parts": [
                 {"id": "a", "label": "a", "button": "Cover a", "weight": 8},
                 {"id": "b", "label": "b", "button": "Cover b", "weight": 6},
             ],
             "covered": "R",
             "results": {
                 "R": {"result": "R = a + b",
                       "sentence": "Cover the whole bar and the two parts "
                                   "are left side by side — add them."},
                 "a": {"result": "a = R − b",
                       "sentence": "Cover wave A and the whole bar and wave "
                                   "B are left — take B away from the "
                                   "whole."},
                 "b": {"result": "b = R − a",
                       "sentence": "Cover wave B and the whole bar and wave "
                                   "A are left — take A away from the "
                                   "whole."},
             },
             "close": "Two parts side by side make the whole. Cover the part "
                      "you want and take the other one away from the whole. "
                      "Crest on trough is the same bar with one part "
                      "pointing the other way, so the parts subtract "
                      "instead.",
         }},

        {"type": "worked-example", "id": "cfifa-super-plain"},
        {"type": "worked-example", "id": "cfifa-super-convert"},
        {"type": "check", "id": "your-turn-super", "anchor": "s-bar"},

        {"type": "key-fact", "ref": "the-surface-takes-the-sum"},

        {"type": "misconception", "id": "think-waves-destroy",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-super-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "Two ripples meet crest on crest. One is 8 mm high, the "
                    "other is 5 mm. How high is the water where they meet?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "8 mm stays 8 mm · 5 mm stays 5 mm",
              "note": "Both heights are already in millimetres, so there is "
                      "nothing to convert."},
             {"letter": "F", "label": "Formula", "line": "R = a + b",
              "note": "Crest on crest, so the two displacements are both "
                      "upwards and they add."},
             {"letter": "I", "label": "Insert", "line": "R = 8 mm + 5 mm",
              "note": "Both heights are measured from the still level."},
             {"letter": "F", "label": "Fine-tune", "line": "8 + 5 = 13",
              "note": "Millimetres added to millimetres leave millimetres."},
             {"letter": "A", "label": "Answer", "line": "R = 13 mm",
              "note": "Thirteen millimetres above the still level, and only "
                      "while the two are overlapping."},
         ]},

        {"id": "cfifa-super-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A crest 1.2 cm high meets a crest 7 mm high. How high "
                    "is the water where they meet?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, on your own channel."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "1.2 cm × 10 = 12 mm",
              "note": "Two heights cannot be added until they are in the "
                      "same unit, and a centimetre is ten millimetres."},
             {"letter": "F", "label": "Formula", "line": "R = a + b",
              "note": "Crest on crest, so both displacements are upwards and "
                      "they add."},
             {"letter": "I", "label": "Insert", "line": "R = 12 mm + 7 mm",
              "note": "The converted height goes in. The 1.2 never does."},
             {"letter": "F", "label": "Fine-tune", "line": "12 + 7 = 19",
              "note": "Millimetres added to millimetres leave millimetres."},
             {"letter": "A", "label": "Answer", "line": "R = 19 mm",
              "note": "Add 1.2 to 7 and you get 8.2 of nothing at all — the "
                      "units were never the same."},
         ]},

        {"id": "your-turn-super",
         "kind": "p6-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "rest": {"inA": 8, "inB": 6, "sign": "+", "r": 14, "arrive": "crest on crest",
                  "formnote": "Crest on crest, so both displacements are upwards and they add.",
                  "answernote": "14 millimetres from the still level, and only while the two are overlapping."},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              # ⊕ PHASE 3, 25 Aug 2026 — HER question, her lines and
              # her notes, with this engine's token names in place of
              # her state expressions.
              "head": "Your two waves: {inA} mm and {inB} mm, arriving "
                      "{arrive}.",
              "lead": "Write all five lines before you check. Both heights "
                      "are the ones your own channel is showing.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{inA} mm stays {inA} mm · {inB} mm stays {inB} "
                           "mm",
                   "note": "Both sliders read in millimetres, so there is "
                           "nothing to convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "R = a {sign} b",
                   "note": "{formnote}"},
                  {"letter": "I", "label": "Insert",
                   "line": "R = {inA} mm {sign} {inB} mm",
                   "note": "Both heights come from the sliders above, "
                           "measured from the still level."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{inA} {sign} {inB} = {r}",
                   "note": "Millimetres and millimetres leave millimetres."},
                  {"letter": "A", "label": "Answer",
                   "line": "R = {r} mm",
                   "note": "{answernote}"},
              ],
              "close": "The five lines above give {r} mm where the two "
                       "meet."},
             {"id": "q2", "tab": "Question 2",
              # ⊕ PHASE 3, 25 Aug 2026 — HER question, not one of
              # ours. The port had written a different second
              # question here with different numbers; hers is the
              # one a student is meant to meet.
              "head": "A crest 0.9 cm high meets a crest 4 mm high, crest "
                      "on crest.",
              "lead": "This one needs the Convert line to do some "
                      "work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "0.9 cm × 10 = 9 mm",
                   "note": "Two heights cannot be added until they share a "
                           "unit, and a centimetre is ten millimetres."},
                  {"letter": "F", "label": "Formula",
                   "line": "R = a + b",
                   "note": "Crest on crest, so both are upwards and they "
                           "add."},
                  {"letter": "I", "label": "Insert",
                   "line": "R = 9 mm + 4 mm",
                   "note": "The converted height goes in. The 0.9 never "
                           "does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "9 + 4 = 13",
                   "note": "Millimetres added to millimetres leave "
                           "millimetres."},
                  {"letter": "A", "label": "Answer",
                   "line": "R = 13 mm",
                   "note": "Add 0.9 to 4 and you get 4.9 of nothing at all."},
              ],
              "close": "The five lines give 13 mm. The whole question "
                       "turned on the first one."},
         ]},

        {"id": "think-waves-destroy",
         "kind": "predict",
         "demand": "explain",
         "targets": "WAVE-05",
         "statements": [
             {"quote": "When two waves cancel, they destroy each other.",
              "targets": "WAVE-05",
              "body": [
                  "Cancelling is something that happens to a "
                  "<em>place</em>, not to the waves. While the two are on "
                  "top of one another the surface there is flat, because "
                  "one wave is asking it to rise by as much as the other is "
                  "asking it to drop. Keep watching and both waves come out "
                  "the far side with their original heights, wavelengths "
                  "and directions, as though nothing had happened. Two "
                  "ripples crossing a pond do not knock lumps out of each "
                  "other; they pass straight through.",
              ]},
             {"quote": "If the water is flat, the energy has gone.",
              "targets": "WAVE-08",
              "body": [
                  "Energy is not stored point by point in the surface, and "
                  "cancelling does not remove any. Wherever two waves "
                  "cancel there are other places, half a wavelength away, "
                  "where the same two waves add — the energy is moved about "
                  "the pattern, not deleted. That is why the crossing rings "
                  "from two stones show still patches and violent patches "
                  "side by side: the total is unchanged, and it has simply "
                  "been dealt out unevenly.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "the-surface-takes-the-sum",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Where two waves overlap, the surface takes the sum of the "
                 "two displacements at every point. Crest on crest adds and "
                 "gives a bigger wave; crest on trough of the same size "
                 "cancels and gives flat water. Both waves then carry on past "
                 "the overlap exactly as they were."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3.
    "ladder": {
        "recall": {
            "q": "Two waves meet crest on crest. One has an amplitude of 6 "
                 "mm, the other 4 mm. What is the amplitude of the water "
                 "where they overlap?",
            "options": [
                "5 mm — take the average, because the surface can only be "
                "in one place at a time",
                "10 mm — add the two, because both waves lift the surface "
                "at the same moment",
                "24 mm — multiply the two amplitudes, because both waves "
                "are acting at once",
                "2 mm — take the smaller from the bigger, because one wave "
                "always cancels part of the other",
            ],
            "answer": 1,
            "feedback": {
                0: "The surface being in one place is exactly why you add: "
                   "it goes to the total of what both waves ask for, not to "
                   "a compromise between them.",
                2: "Two things acting at once are added, not multiplied. "
                   "Multiplying millimetres by millimetres would give "
                   "square millimetres, which is an area, not a height.",
                3: "Subtracting is the crest-on-trough case. Crest on crest "
                   "means both are lifting the surface at once, so the two "
                   "displacements add.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "Two wave trains of amplitude 7 mm meet exactly crest on "
                 "trough. A student says the two waves have destroyed each "
                 "other. Which statement is right?",
            "options": [
                "The two waves have destroyed each other, so nothing "
                "carries on past the overlap.",
                "The whole tank goes flat, because the two waves cancel "
                "everywhere they are present.",
                "The surface is flat where they overlap, and both waves "
                "carry on past unchanged — the cancelling lasts only while "
                "they are on top of each other.",
                "The bigger wave absorbs the smaller one, so a single 7 mm "
                "wave carries on — a wave that meets a larger one is always "
                "swallowed by it, and only the larger one comes out the far "
                "side",
            ],
            "answer": 2,
            "feedback": {
                0: "Waves are not objects that can be broken. Each one is "
                   "still travelling through, and both come out the far "
                   "side at 7 mm.",
                1: "The verdict is right in one place and wrong everywhere "
                   "else. Cancelling happens where a crest lands on a "
                   "trough; half a wavelength along, the same two waves are "
                   "adding.",
                3: "Neither is bigger here, and absorption is not what "
                   "superposition does. Both waves carry on, and the flat "
                   "patch exists only where they overlap.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Two stones are dropped into a pond a metre apart at the "
                 "same moment. Explain why some patches of the crossing "
                 "pattern heave twice as far as either ripple on its own "
                 "while other patches stay almost flat.",
            "field_label": "Your explanation",
            "placeholder": "Where the two sets of ripples overlap…",
            "success": [
                "Says the two sets of ripples overlap and the surface takes "
                "the sum of both displacements.",
                "Says a crest arriving with a crest gives a bigger crest, "
                "so those patches heave further.",
                "Says a crest arriving with a trough of the same size gives "
                "no movement, so those patches stay flat.",
                "Says which patch is which depends on how far each ripple "
                "has had to travel to get there.",
                "Says both sets of ripples carry on past the crossing "
                "unchanged.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A harbour wall has two gaps in it. Inside the harbour, "
                 "boats moored at some spots rock hard on a swell while "
                 "boats a few metres away barely move, and the pattern is "
                 "the same every time that swell runs. Explain what is "
                 "going on, then say what would change if one gap were "
                 "blocked up.",
            "field_label": "Your answer",
            "placeholder": "Each gap lets a set of waves into the harbour, "
                           "so…",
            "success": [
                "Says each gap lets its own set of waves spread into the "
                "harbour.",
                "Says the two sets overlap inside and superpose.",
                "Says the hard-rocking spots are where crests arrive "
                "together and add.",
                "Says the calm spots are where a crest from one gap arrives "
                "with a trough from the other and they cancel.",
                "Says blocking one gap leaves a single set of waves, so the "
                "pattern of calm and rough spots disappears and every boat "
                "rocks about the same amount.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Waves on water are transverse: the surface is displaced at "
                "right angles to the direction of travel, upwards or "
                "downwards. Waves reflect off a barrier and travel back. "
                "Where two waves overlap, the surface takes the sum of the "
                "two displacements at every point: crest on crest adds to a "
                "bigger wave, and crest on trough of equal size cancels to "
                "flat water. That is superposition, and both waves leave the "
                "overlap unchanged.",

    "stretch": [
        # ⊕ PHASE 3 REVERT, 25 Aug 2026 — Design's *Going further*,
        # verbatim, both paragraphs. What had been here was different
        # content of this lane's own: good physics, and not hers, and
        # "a different example" is not a defect anyone can name.
        {"id": "reflection-and-superposition-together",
         "type": "explainer",
         "text": "Reflection and superposition together make something "
                 "worth seeing. Send a wave train down a channel with a "
                 "barrier at the far end and the reflected train runs back "
                 "through the train still coming in. Where the two "
                 "superpose, some points end up permanently still and some "
                 "heave hard, and — because both trains have the same "
                 "wavelength — the still points sit half a wavelength apart "
                 "and never move along. The pattern stops looking like a "
                 "travelling wave at all and starts looking like water "
                 "rocking on the spot, which is what a bath sloshing end to "
                 "end is doing."},
        {"id": "the-same-rule-works",
         "type": "explainer",
         "text": "The same rule works for waves that are not on water. Two "
                 "loudspeakers wired to the same note give quiet patches "
                 "you can walk through, and noise-cancelling headphones "
                 "work by generating a wave that arrives crest on trough "
                 "with the sound they want gone. Different material, "
                 "identical arithmetic — which is the reason superposition "
                 "is taught on water first, where you can see it."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "superposition",
         "definition": "Adding the displacements of two waves at every "
                       "point. The whole of what happens where waves meet."},
        {"term": "displacement",
         "definition": "How far the surface is from the still level, and "
                       "which way. Up counts as positive, down as negative."},
        {"term": "reflection",
         "definition": "A wave bouncing back off a barrier, still a wave and "
                       "still the same wavelength."},
    ],

    "tutor": {
        "anchor": "s-meet",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a crossing pattern you cannot account for?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Path difference and phase, constructive and destructive "
                   "interference, standing waves, and the two-source "
                   "interference experiment.",

    "convention_note": "The bench is a teaching model. It shows the two waves "
                       "as though they travel along the same line with the "
                       "same wavelength of 500 mm, which is the simplest case "
                       "and the only one where a single number describes the "
                       "overlap; ripples spreading from two stones cross at "
                       "an angle, and the result then changes from place to "
                       "place across the pattern. All three traces are drawn "
                       "to one scale of 2.5 pixels per millimetre. The traces "
                       "are snapshots rather than animations, and a real "
                       "overlap is moving. Heights are displacements from the "
                       "still level, so a crest counts as up and a trough as "
                       "down.",

    "ws": [],
}
