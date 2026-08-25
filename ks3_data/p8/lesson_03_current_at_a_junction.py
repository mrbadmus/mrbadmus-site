"""P8 L3 — Current at a junction (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p8/p8-03-current-at-a-junction.dc.html`.

Her page wins outright. The river round the island, the two-branch bench,
the part–whole bar, both worked examples, both attempts and all four rungs
are hers.

── ⚖️ MRB-204 · A PART–WHOLE BAR, AND IT KEEPS ITS COVER BUTTONS ─────

`I = a + b` is a SUM. A triangle here would teach a product that does not
exist, so the figure is a part–whole bar — and it keeps its buttons,
because covering a part asks a real question: *what is left?*

⚖️ **THE PARTS ARE UNEQUAL, AND THE WEIGHTS ARE MEASURED OFF HER SVG.**
337 against 213 of a 560-wide whole. That is not decoration: `CIRC-09` is
*at a junction the current halves*, and a bar drawn in two equal parts
would be the misconception in the figure that is supposed to kill it.

`I = a + b + c` is the one permitted extra display line.

── ⚖️ RULED · THE EQUAL STATE IS REAL AND HAS ITS OWN BRANCH ─────────

Two lamps, or two resistors, or two buzzers, genuinely split the main
current in half — and the note for that state says in terms that halving
works ONLY because the branches happen to match. A bench that could never
reach the equal state would leave a student unable to see that it is a
special case rather than a rule.

── ⚖️ RULED · THE ZERO STATE AND THE ONE-BRANCH-OPEN STATE ARE BOTH
   REAL, AND NEITHER IS A DEGENERATE CASE ───────────────────────────

Both branches empty reads 0.00 A at all three meters with the junction
still sitting there. One branch empty is the state that shows the
surviving branch reading exactly what it would read on its own, which is
`CIRC-10` met head-on.

── ⚠️ FOUR RAIL STOPS ───────────────────────────────────────────────

    s-hook · s-junction · s-bar · s-ladder

⚠️ **MRB-208** — the `s-bar` id goes on the ATTEMPT PANEL, because
Design's own `DONE` reads `s.q[0].open && s.q[1].open`.

── ⚖️ FOUR MISCONCEPTIONS ───────────────────────────────────────────

    CIRC-09  at a junction the current halves            (hers, §7)
    CIRC-10  a second branch means less for the first    (hers, §7)
    CIRC-11  add every reading you can see               (from rung 1 B)
    CIRC-12  some current is left behind in the harder branch (from the hook)

── ⚠️ POSITION IS AUTHORED. This lesson takes indices 0 and 2.
"""

LESSON = {
    "slug":  "current-at-a-junction",
    "title": "Current at a junction",
    "discipline": "physics",
    "unit": "Electric circuits",
    "family": "SYSTEM",

    "covers": ["KS3.P.CUR.01c"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "electricity", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["series-and-parallel"],
    "assumes": [],
    "references": ["current-and-circuits", "resistance"],
    "ks4_links": [],

    "meta_description": "Three ammeters round one split in the wire. Two of "
                        "the readings always add up to the third — whatever "
                        "you put in the branches, and however lopsided the "
                        "split.",

    "big_question": "Three ammeters round one split in the wire. Two of the "
                    "readings always add up to the third — whatever you put "
                    "in the branches, and however lopsided the split.",

    "rail": [
        {"anchor": "s-hook",     "short": "RIVER",
         "label": "A river splits",       "done_when": "committed"},
        {"anchor": "s-junction", "short": "BENCH",
         "label": "Change the branches",  "done_when": "gate_and_a_control"},
        {"anchor": "s-bar",      "short": "CFIFA",
         "label": "The bar and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder",   "short": "LADDER",
         "label": "Mastery ladder",       "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "A river splits round an island.",
        "prompt": "A river meets an island and divides. One channel is wide "
                  "and deep, the other narrow and shallow, so far more water "
                  "goes one way than the other. Below the island the two "
                  "channels rejoin.",
        "commit": "How much water flows below the island, compared with above "
                  "it?",
        "options": [
            "The same amount — the two channels add back to what arrived",
            "Less, because some water is left behind in the shallow channel",
            "Half as much, because the flow was divided in two",
            "More, because two channels can carry more than one",
        ],
        "answer": 0,
        "reveal": "The same amount, because the island neither swallows water "
                  "nor makes any. The split is lopsided — far more goes down "
                  "the easy channel — but the two add back to exactly what "
                  "arrived. A junction in a wire behaves the same way, and "
                  "for the same reason: nothing is stored at a point.",
    },

    "misconceptions": [
        {"id": "CIRC-09",
         "statement": "At a junction the current halves, because it has two "
                      "ways to go.",
         "elicited_by": "junction",
         "confronted_by": "junction"},
        {"id": "CIRC-10",
         "statement": "Adding a second branch means less current for the "
                      "first one.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "CIRC-11",
         "statement": "To find the total at a junction you add every reading "
                      "you can see, including the main wire's.",
         "elicited_by": "s-ladder",
         "confronted_by": "junction"},
        {"id": "CIRC-12",
         "statement": "Some of the current is left behind in the branch that "
                      "resists more.",
         "elicited_by": "s-hook",
         "confronted_by": "s-hook"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A <strong>junction</strong> is any point where a wire "
                 "divides, or where two wires meet. Nothing is stored there "
                 "and nothing is made there: the charge arriving has nowhere "
                 "to go except out along the branches. So the current going "
                 "in equals the total of the currents coming out."},
        {"type": "explainer",
         "text": "That is not the same as saying the branches get equal "
                 "shares. Each branch draws whatever it draws — a lamp takes "
                 "more than a buzzer, an empty branch takes nothing — and the "
                 "main wire simply carries the sum. Which is why the split is "
                 "usually lopsided, and why you cannot guess a branch reading "
                 "by halving the main one."},
        {"type": "explainer",
         "text": "The rule works both ways round a parallel section. Where "
                 "the branches divide, the main current shares out; where "
                 "they rejoin, the branch currents add back together. The two "
                 "junctions of one parallel section always carry the same "
                 "total."},

        # ── #s-junction · two branches, three ammeters ─────────────────
        {"type": "junction-bench",
         "id": "junction",
         "anchor": "s-junction",
         "eyebrow": "At the bench · one 3.0 V battery, two branches, three "
                    "ammeters",
         "heading": "Change what is in the branches.",
         # A MAP, NOT A STRING. `progress` authored as a string is
         # read as a COUNT FORMAT (MRB-248's widening), and these
         # are two named states rather than a tally.
         "progress": {"idle": "Change a control to begin",
                      "live": "Both controls live"},
         "lead": "The two branches can each hold a lamp, a resistor, a "
                 "buzzer, or nothing at all. Every arrangement gives three "
                 "readings, and they are always related the same way.",
         "start_a": 0,
         "start_b": 2,
         "battery_label": "3.0 V",
         "junction_label": "JUNCTION",
         "main_label": "MAIN WIRE",
         "a_label": "In branch A",
         "b_label": "In branch B",
         "gate": {
             "prompt": "Commit first. A lamp draws 0.30 A and a buzzer draws "
                       "0.10 A. You put the lamp in one branch and the buzzer "
                       "in the other. What does the ammeter in the main wire "
                       "read?",
             "options": [
                 "0.40 A — the two branch currents added together",
                 "0.20 A — the average of the two branches",
                 "0.30 A — whichever branch draws the most",
                 "0.20 A — the main current halves at the junction",
             ],
             "answer": 0,
         },
         "parts": [
             {"id": "lamp", "label": "Lamp", "name": "LAMP", "amps": 0.30,
              "sub": "a lamp, 10 ohms", "shape": "lamp"},
             {"id": "res", "label": "Resistor", "name": "RESISTOR",
              "amps": 0.20, "sub": "a resistor, 15 ohms", "shape": "res"},
             {"id": "buz", "label": "Buzzer", "name": "BUZZER", "amps": 0.10,
              "sub": "a buzzer, 30 ohms", "shape": "buz"},
             {"id": "none", "label": "Nothing", "name": "BRANCH OPEN",
              "amps": 0, "sub": "the branch is open", "shape": "none"},
         ],
         "readouts": [
             {"id": "a", "label": "Branch A carries", "sub": "—"},
             {"id": "b", "label": "Branch B carries", "sub": "—"},
             {"id": "main", "label": "The main wire carries", "sub": "—"},
             {"id": "split", "label": "How it splits", "word": True},
         ],
         "branches": {
             "none":
                 "Both branches are open, so there is no path from one end of "
                 "the battery to the other and all three meters read 0.00 A. "
                 "The junction is still there; it simply has nothing arriving "
                 "and nothing to send anywhere.",
             "one_open":
                 "Branch {dead} is open and carries 0.00 A, so everything "
                 "goes through branch {live}: {total} there and the same "
                 "{total} in the main wire. The sum still holds — one of the "
                 "parts is simply zero. Notice that branch {live} reads "
                 "exactly what it would read on its own, because opening the "
                 "other branch took nothing from it.",
             "equal":
                 "The two branches hold the same component, so they resist "
                 "the same and take the same current: {a} each, adding to "
                 "{total} in the main wire. This is the one case where "
                 "halving the main reading gives you a branch reading — and "
                 "it works only because the branches happen to match.",
             "uneven":
                 "Branch A carries {a} and branch B carries {b}, which add to "
                 "{total} in the main wire. Branch {bigger} takes the larger "
                 "share because the component in it resists less, not because "
                 "the junction favoured it. Halving the main reading would "
                 "give {half}, which is neither branch.",
         }},

        # ── #s-bar · the relationship, the two examples, the attempt ───
        {"type": "formula",
         "id": "junction-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "The current arriving at a junction is the current "
                      "leaving it",
         "support": ["Three branches: I = a + b + c",
                     "I · current in the main wire · A",
                     "a · current in the first branch · A",
                     "b · current in the second branch · A"],
         # ⚖️ A PART–WHOLE BAR KEEPS ITS COVER BUTTONS, and the weights ARE
         # the arithmetic: 337 and 213 measured off Design's own 560-wide
         # bar, so the two parts fill the whole to the pixel and the split
         # is visibly lopsided.
         "cover": {
             "shape": "bar",
             "eyebrow": "The bar",
             "heading": "Cover the one you want",
             "aria_label": "A part-whole bar. One long bar labelled I sits "
                           "above two unequal bars, a and b, which together "
                           "fill exactly the length of I.",
             "whole": {"id": "I", "label": "I", "button": "Cover I"},
             "parts": [
                 {"id": "a", "label": "a", "button": "Cover a", "weight": 337},
                 {"id": "b", "label": "b", "button": "Cover b", "weight": 213},
             ],
             "covered": "I",
             "results": {
                 "I": {"result": "I = a + b",
                       "sentence": "Cover the main wire and the two branches "
                                   "are left side by side — add them."},
                 "a": {"result": "a = I − b",
                       "sentence": "Cover the first branch and the main wire "
                                   "and the second branch are left — take the "
                                   "second branch away from the whole."},
                 "b": {"result": "b = I − a",
                       "sentence": "Cover the second branch and the main wire "
                                   "and the first branch are left — take the "
                                   "first branch away from the whole."},
             },
             "close": "Two parts side by side make the whole. Cover the part "
                      "you want and take the other one away from the whole.",
         }},

        {"type": "worked-example", "id": "cfifa-junction-plain"},
        {"type": "worked-example", "id": "cfifa-junction-convert"},
        {"type": "check", "id": "your-turn-junction", "anchor": "s-bar"},

        {"type": "key-fact", "ref": "currents-add-at-a-junction"},

        {"type": "misconception", "id": "think-junction-halves",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-junction-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "The main wire into a junction reads 0.45 A. One branch "
                    "reads 0.15 A. What does the other branch carry?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "0.45 A stays 0.45 A · 0.15 A stays 0.15 A",
              "note": "Both meters already read in amps, so there is nothing "
                      "to convert."},
             {"letter": "F", "label": "Formula", "line": "b = I − a",
              "note": "Cover b on the bar: the whole with the other part "
                      "taken away."},
             {"letter": "I", "label": "Insert",
              "line": "b = 0.45 A − 0.15 A",
              "note": "The whole is the main wire, 0.45 A. The part you know "
                      "is the first branch, 0.15 A."},
             {"letter": "F", "label": "Fine-tune",
              "line": "0.45 − 0.15 = 0.30",
              "note": "Amps take away amps leaves amps."},
             {"letter": "A", "label": "Answer", "line": "b = 0.30 A",
              "note": "Check it: 0.15 A and 0.30 A add to the 0.45 A in the "
                      "main wire."},
         ]},

        {"id": "cfifa-junction-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "The main wire into a junction reads 1.20 A. One branch "
                    "reads 250 mA. What does the other branch carry?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "250 mA ÷ 1000 = 0.250 A",
              "note": "There are 1000 milliamps in an amp, so divide before "
                      "you take anything away."},
             {"letter": "F", "label": "Formula", "line": "b = I − a",
              "note": "Cover b on the bar: the whole with the other part "
                      "taken away."},
             {"letter": "I", "label": "Insert",
              "line": "b = 1.20 A − 0.250 A",
              "note": "The converted branch reading goes in. The milliamp "
                      "reading never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "1.20 − 0.250 = 0.950",
              "note": "Amps take away amps leaves amps."},
             {"letter": "A", "label": "Answer", "line": "b = 0.950 A",
              "note": "Take 250 from 1.20 instead and you get a negative "
                      "current, which no ammeter ever reads."},
         ]},

        {"id": "your-turn-junction",
         "kind": "p8-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         # The bench's opening state: a lamp in branch A and a buzzer in
         # branch B, so 0.30 A and 0.10 A adding to 0.40 A. `totalnum` and
         # its siblings are the BARE numbers the Fine-tune line divides out
         # to; the unit-carrying tokens are separate because the two lines
         # want different things.
         "rest": {"total": "0.40 A", "a": "0.30 A", "b": "0.10 A",
                  "totalnum": "0.40", "anum": "0.30", "bnum": "0.10"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your junction: the main wire reads {total} and branch "
                      "A reads {a}.",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{total} stays {total} · {a} stays {a}",
                   "note": "Both meters already read in amps, so nothing "
                           "changes."},
                  {"letter": "F", "label": "Formula", "line": "b = I − a",
                   "note": "Cover b on the bar: the whole with the other part "
                           "taken away."},
                  {"letter": "I", "label": "Insert",
                   "line": "b = {total} − {a}",
                   "note": "The whole is the main wire; the part you know is "
                           "branch A."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{totalnum} − {anum} = {bnum}",
                   "note": "Amps take away amps leaves amps."},
                  {"letter": "A", "label": "Answer",
                   "placeholder": "remember the unit",
                   "line": "b = {b}",
                   "note": "Check it against the meter in branch B, which "
                           "reads {b}."},
              ],
              "close": "The five lines give {b} for branch B, and {a} + {b} "
                       "is the {total} in the main wire."},
             {"id": "q2", "tab": "Question 2",
              "head": "A junction where the main wire reads 0.80 A and branch "
                      "A reads 320 mA.",
              "lead": "This one needs the Convert line to do some work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "320 mA ÷ 1000 = 0.320 A",
                   "note": "There are 1000 milliamps in an amp, so divide "
                           "before you take anything away."},
                  {"letter": "F", "label": "Formula", "line": "b = I − a",
                   "note": "Cover b on the bar: the whole with the other part "
                           "taken away."},
                  {"letter": "I", "label": "Insert",
                   "line": "b = 0.80 A − 0.320 A",
                   "note": "The converted branch reading goes in. The "
                           "milliamp reading never does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "0.80 − 0.320 = 0.480",
                   "note": "Amps take away amps leaves amps."},
                  {"letter": "A", "label": "Answer",
                   "placeholder": "remember the unit",
                   "line": "b = 0.480 A",
                   "note": "Take 320 from 0.80 instead and you get a negative "
                           "current, which no ammeter ever reads."},
              ],
              "close": "The five lines give 0.480 A in branch B, and 0.320 A "
                       "+ 0.480 A is the 0.80 A in the main wire."},
         ]},

        {"id": "think-junction-halves",
         "kind": "predict",
         "demand": "explain",
         "targets": "CIRC-09",
         "statements": [
             {"quote": "At a junction the current halves, because it has two "
                       "ways to go.",
              "targets": "CIRC-09",
              "body": [
                  "Only if the two branches happen to be identical. Put a "
                  "lamp in one branch and a buzzer in the other and the split "
                  "is 0.30 A against 0.10 A — three quarters of the charge "
                  "takes the easier route. The junction does not divide "
                  "anything up; it simply lets each branch take what it "
                  "takes, and the main wire carries whatever that adds to. "
                  "Halving is a special case, not the rule.",
              ]},
             {"quote": "Adding a second branch means less current for the "
                       "first one.",
              "targets": "CIRC-10",
              "body": [
                  "The first branch does not notice. It has the same battery "
                  "across it as before, so it draws the same current as "
                  "before, and the meter in it does not move when you add or "
                  "remove the other branch. What changes is the main wire, "
                  "which now has to carry both branch currents — so the "
                  "battery works harder and goes flat sooner. It is the "
                  "supply that pays, not the neighbouring branch.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "currents-add-at-a-junction",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Charge is neither made nor stored at a junction, so the "
                 "currents leaving add up to the current arriving: I = a + b. "
                 "The branches do not get equal shares — each draws what it "
                 "draws — and the same total passes both junctions of a "
                 "parallel section."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 2.
    "ladder": {
        "recall": {
            "q": "A junction splits into three branches. The main wire "
                 "carries 0.85 A, the first branch 0.30 A and the second "
                 "0.40 A. What does the third branch carry?",
            "options": [
                "0.15 A",
                "1.55 A — add all three readings together",
                "0.28 A — share the main current equally between the three "
                "branches",
                "0.10 A — take the smaller branch away from the larger one",
            ],
            "answer": 0,
            "feedback": {
                1: "You have added the parts to the whole. The whole is "
                   "already given as 0.85 A; the third part is what is left "
                   "of it after the other two.",
                2: "Branches are not given equal shares. Two of them are "
                   "already measured at 0.30 A and 0.40 A, which are not "
                   "equal, so the third is 0.85 − 0.30 − 0.40.",
                3: "That compares two branches with each other. The missing "
                   "branch is fixed by the total: 0.85 A must be shared out "
                   "among all three.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "Two lamps are in parallel on a battery, each drawing "
                 "0.30 A. A student unscrews one and predicts the other will "
                 "now draw 0.60 A, because it gets all the current to itself. "
                 "What is right?",
            "options": [
                "The student is right — the total from the battery is fixed "
                "at 0.60 A, so the remaining lamp must take all of it.",
                "It draws 0.15 A, because removing a branch makes the circuit "
                "harder to get round.",
                "It still draws 0.30 A. Its branch has the same battery "
                "across it as before, and the main wire now carries 0.30 A "
                "instead of 0.60 A.",
                "It still draws 0.30 A, because a battery always gives out "
                "the same current whatever is connected to it.",
            ],
            "answer": 2,
            "feedback": {
                0: "The total is not fixed. The battery supplies whatever the "
                   "branches ask for, and one lamp asks for 0.30 A.",
                1: "Removing a parallel branch does make the circuit harder "
                   "to get round overall, but the surviving branch is "
                   "unchanged — it has the same battery across it and the "
                   "same resistance, so the same current.",
                3: "The verdict is right and the reason is not. A battery "
                   "does not give a fixed current — the total here drops from "
                   "0.60 A to 0.30 A. What is fixed is the push across each "
                   "branch.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A lamp and a buzzer are in parallel on the same battery. "
                 "The lamp branch carries 0.30 A and the buzzer branch "
                 "0.10 A. Explain what the ammeter in the main wire reads, "
                 "and why the split is not even.",
            "field_label": "Your explanation",
            "placeholder": "The main wire carries…",
            "success": [
                "Gives the main reading as 0.40 A, with the unit.",
                "Says the branch currents add because charge is not made or "
                "stored at a junction.",
                "Says each branch draws its own current rather than being "
                "given a share.",
                "Says the buzzer resists more, so less current goes that way.",
                "Says the same 0.40 A passes the junction where they divide "
                "and the junction where they rejoin.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "An extension lead is marked \"maximum 13 A\". Someone plugs "
                 "in a heater drawing 9 A, a kettle drawing 11 A and a lamp "
                 "drawing 0.3 A, and points out that no single appliance is "
                 "over 13 A. Explain, using the junction rule, why this is "
                 "dangerous and what will happen.",
            "field_label": "Your answer",
            "placeholder": "The sockets are in parallel, so…",
            "success": [
                "Says the sockets are branches in parallel off one main "
                "cable.",
                "Adds the branch currents to get about 20.3 A in the lead.",
                "Says that total, not the largest single appliance, is what "
                "the lead has to carry.",
                "Says 20.3 A is well over the 13 A rating, so the lead itself "
                "overheats.",
                "Says the fuse or breaker is chosen for the total and should "
                "cut off first — and that the risk is a fire in the cable or "
                "the reel, not a fault in any one appliance.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "A junction is a point where a wire divides or two wires "
                "meet. Charge is not made or stored there, so the currents "
                "leaving add up to the current arriving: I = a + b. The "
                "branches are not given equal shares — each draws its own "
                "current, so an easier branch takes more — and the same total "
                "passes the junction where they divide and the junction where "
                "they rejoin. Adding a branch does not steal current from the "
                "others; it makes the main wire and the battery carry more.",

    "stretch": [
        {"id": "kirchhoffs-first-law",
         "type": "explainer",
         "text": "This rule has a name at A level: Kirchhoff's first law, "
                 "published by Gustav Kirchhoff in 1845 when he was "
                 "twenty-one. It is not really a law about electricity at all "
                 "— it is the conservation of charge, applied to a point. "
                 "Charge cannot be created or destroyed, and a junction has "
                 "no room to keep any, so the books must balance every "
                 "instant."},
        {"id": "engineers-use-the-sum-backwards",
         "type": "explainer",
         "text": "Engineers use the sum in the direction you might not "
                 "expect: backwards, to size a cable. A ring main feeding a "
                 "kitchen has to carry the kettle, the toaster, the fridge "
                 "and the lights added together, even though each appliance "
                 "only knows about itself. Underrate that main cable and it "
                 "is the wire that overheats, not the appliance — which is "
                 "why the fuse or breaker protecting a circuit is chosen for "
                 "the total, and why adding one more heater to a loaded "
                 "extension lead is the moment it becomes dangerous."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "junction",
         "definition": "A point where a wire divides, or where two wires "
                       "meet. Nothing is stored there and nothing is made "
                       "there."},
        {"term": "main wire",
         "definition": "The single wire on either side of a parallel "
                       "section, carrying the branch currents added "
                       "together."},
        {"term": "milliamp",
         "definition": "A thousandth of an amp, written mA. Divide by 1000 "
                       "before using it in any sum that wants amps."},
    ],

    "tutor": {
        "anchor": "s-junction",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got two of the three readings and want to find the missing "
                "one?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Kirchhoff's current law, used with the potential "
                   "difference rules to solve circuits with several loops.",

    "convention_note": "The bench is a teaching model. Each component is "
                       "treated as having a fixed resistance on a 3.0 V "
                       "supply — lamp 10 ohms, resistor 15 ohms, buzzer 30 "
                       "ohms — giving 0.30 A, 0.20 A and 0.10 A; a real "
                       "filament lamp and a real buzzer both change as they "
                       "run. The battery and the connecting wires are treated "
                       "as having no resistance, which is why the branch "
                       "readings do not sag when the other branch is added. "
                       "Readings are rounded to two decimal places. "
                       "Conventional current is drawn from + to − by "
                       "long-standing convention; the electrons in a metal "
                       "drift the other way.",

    "ws": ["measurement", "analysis"],
}
