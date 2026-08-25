"""P8 lesson 02 — Series and parallel: twelve questions (MRB-223).

Written against Design's page. The blown kitchen bulb, the two rewireable
bulbs and the five-way comparison table are hers.

The discriminations, in the order the lesson builds them:

  · counting PATHS is what tells the two apart, not the shape of the
    drawing;
  · in series one break stops everything, and both bulbs are equally dim
    (`CIRC-06`);
  · in parallel each branch has the whole push, so nothing is shared out
    (`CIRC-05`) — the harder band sits here;
  · what parallel costs is the BATTERY, not the neighbouring branch.

⚠️ POSITION IS AUTHORED AND MEASURED —
1,3,0,2 · 2,0,3,2 · 1,1,2,3;
the twelve fall 2/3/4/3 across the four indices.

⚠️ The ladder's own two marked rungs are NOT restated: neither the three
parallel lamps on 6 V with the middle one unscrewed, nor the second
identical bulb added in series.
"""

UNIT = "P8"
LESSON = "series-and-parallel"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p8-02-e01",
        "band": "easier",
        "text": "Two components are in SERIES when…",
        "options": [
            {"text": "they are drawn next to each other on the page",
             "correct": False,
             "why": "How they are drawn does not decide it. Count the paths "
                    "from one end of the battery to the other."},
            {"text": "the charge has to go through one and then the other",
             "correct": True},
            {"text": "each one has its own path back to the battery",
             "correct": False,
             "why": "That is parallel. In series there is only one path."},
            {"text": "they are the same kind of component", "correct": False,
             "why": "A lamp and a buzzer can be in series. It is about the "
                    "wiring, not the parts."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-e02",
        "band": "easier",
        "text": "How do you tell a series circuit from a parallel one?",
        "options": [
            {"text": "Count the components", "correct": False,
             "why": "Two components can be wired either way. The count says "
                    "nothing about the arrangement."},
            {"text": "Look at whether the drawing is a rectangle or a ladder",
             "correct": False,
             "why": "The same circuit can be drawn either shape. Follow the "
                    "path instead of trusting the picture."},
            {"text": "Check whether the battery has a switch", "correct": False,
             "why": "A switch can be in either arrangement, and usually is "
                    "in series with the whole thing."},
            {"text": "Count the paths from one end of the battery to the "
                     "other", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-e03",
        "band": "easier",
        "text": "One lamp in a string of ten wired in series fails. What "
                "happens to the other nine?",
        "options": [
            {"text": "They all go out", "correct": True},
            {"text": "They all get brighter, because there is one fewer to "
                     "share with", "correct": False,
             "why": "Nothing is shared, and nothing is left to be brighter: "
                    "the only path is broken."},
            {"text": "Only the ones after the failed lamp go out",
             "correct": False,
             "why": "There is no after in a loop. The break stops the "
                    "current everywhere at the same instant."},
            {"text": "Nothing happens, because the other nine each have "
                     "their own path", "correct": False,
             "why": "In series they do not. One path, shared by all ten."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-e04",
        "band": "easier",
        "text": "Where in a house are the lights and sockets wired?",
        "options": [
            {"text": "In series, so one switch controls the lot",
             "correct": False,
             "why": "Wired that way, one blown bulb would darken the whole "
                    "house and every lamp would be dim."},
            {"text": "In series for the lights and parallel for the sockets",
             "correct": False,
             "why": "Both are parallel. Every light has its own branch, "
                    "which is why one failing changes nothing."},
            {"text": "In parallel, so each one gets the full supply and works "
                     "on its own", "correct": True},
            {"text": "Neither — house wiring uses a different kind of "
                     "circuit altogether", "correct": False,
             "why": "There are only two ways to add a component. A house is "
                    "parallel from the meter outwards."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p8-02-s01",
        "band": "standard",
        "text": "A 3 V battery drives two identical lamps in parallel. Each "
                "lamp on its own would draw 0.25 A. What leaves the battery?",
        "options": [
            {"text": "0.125 A", "correct": False,
             "why": "That halves a single lamp's current. Adding a branch "
                    "makes the battery supply more, not less."},
            {"text": "0.25 A", "correct": False,
             "why": "That is one branch. The two branch currents add at the "
                    "battery."},
            {"text": "0.50 A", "correct": True},
            {"text": "0.0 A, because the two branches cancel", "correct": False,
             "why": "Branches do not cancel. They both draw from the same "
                    "battery in the same direction."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-s02",
        "band": "standard",
        "text": "Why is a switch put in series with the thing it controls "
                "rather than in parallel with it?",
        "options": [
            {"text": "Because a switch in series can break the only path, "
                     "which is what turning something off means",
             "correct": True},
            {"text": "Because a switch in parallel would be too far from the "
                     "component to work", "correct": False,
             "why": "Distance is irrelevant in a circuit. What matters is "
                    "which path the switch is in."},
            {"text": "Because a switch has to be nearer the battery than "
                     "anything else", "correct": False,
             "why": "Position round a single loop makes no difference. A "
                    "switch works anywhere in the loop it is breaking."},
            {"text": "Because a switch in parallel would use more current "
                     "when it is open", "correct": False,
             "why": "An open switch carries nothing wherever it is. The "
                    "problem with parallel is what happens when it CLOSES."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-s03",
        "band": "standard",
        "text": "Two identical lamps are wired in series. A student swaps "
                "them over. What changes?",
        "options": [
            {"text": "The lamp that is now first becomes brighter",
             "correct": False,
             "why": "There is no first. One loop carries one current at "
                    "every point at the same instant."},
            {"text": "The total current from the battery falls",
             "correct": False,
             "why": "Nothing about the loop has changed — the same two lamps "
                    "are still in the same single path."},
            {"text": "The one nearer the battery gets more of the p.d.",
             "correct": False,
             "why": "Identical lamps take identical shares wherever they "
                    "sit. Position does not decide a share; resistance does."},
            {"text": "Nothing at all", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-s04",
        "band": "standard",
        "text": "Adding a THIRD lamp in parallel to two that are already "
                "there does what to the first lamp?",
        "options": [
            {"text": "It dims, because the current is now shared three ways",
             "correct": False,
             "why": "Nothing is shared out. Each branch draws what it draws, "
                    "and the battery supplies the total."},
            {"text": "It brightens, because more branches make it easier for "
                     "charge to get round", "correct": False,
             "why": "The whole circuit does get easier, but the first lamp's "
                    "own branch is unchanged, so it draws exactly what it "
                    "drew before."},
            {"text": "Nothing changes for the lamp, but the battery now "
                     "supplies more current and goes flat sooner",
             "correct": True},
            {"text": "It goes out, because one battery cannot drive three "
                     "branches at once", "correct": False,
             "why": "A battery supplies whatever the branches ask for until "
                    "it is exhausted. Three lamps run; the battery just "
                    "flattens sooner."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p8-02-h01",
        "band": "harder",
        "text": "A cheap decoration string is wired in series. Why do "
                "manufacturers do that, when they know one failure kills the "
                "whole string?",
        "options": [
            {"text": "Because a series string draws less current from the "
                     "mains, and a maker has to keep the current down to "
                     "stay within the rating of the plug it is sold with",
             "correct": False,
             "why": "It does draw less, and that is not the reason: the "
                    "saving is in the bulbs, which can be tiny low-voltage "
                    "ones."},
            {"text": "Because in series each bulb only needs a small share "
                     "of the supply voltage, so it can be a cheap "
                     "low-voltage bulb", "correct": True},
            {"text": "Because parallel wiring is not allowed at mains "
                     "voltage", "correct": False,
             "why": "Every light and socket in a house is parallel at mains "
                    "voltage. It is allowed and it is normal."},
            {"text": "Because a series string is easier to fault-find",
             "correct": False,
             "why": "It is the opposite: every bulb goes out at once, so the "
                    "fault gives no clue where it is."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-h02",
        "band": "harder",
        "text": "A car has two headlamps in parallel. One bulb fails on a "
                "dark road. What does the driver see, and why?",
        "options": [
            {"text": "Both go out, because the two lamps share one loop",
             "correct": False,
             "why": "They do not share one loop. In parallel each lamp has "
                    "its own branch off the battery."},
            {"text": "The other lamp stays exactly as bright, because its "
                     "branch is untouched", "correct": True},
            {"text": "The other lamp brightens, because it now gets all the "
                     "current", "correct": False,
             "why": "There is no fixed total to inherit. The surviving lamp "
                    "draws what it always drew; the battery simply supplies "
                    "less."},
            {"text": "The other lamp dims, because the battery is now "
                     "unbalanced", "correct": False,
             "why": "A battery is not balanced between branches. Each branch "
                    "has the whole p.d. across it either way."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-h03",
        "band": "harder",
        "text": "A student wires a spare piece of wire in parallel with a "
                "lamp, expecting it to make no difference. What actually "
                "happens?",
        "options": [
            {"text": "The lamp gets brighter, because the extra branch adds "
                     "current to it", "correct": False,
             "why": "A branch beside the lamp does not feed the lamp. It "
                    "offers the charge a way past it."},
            {"text": "Nothing, because a plain wire has no component in it",
             "correct": False,
             "why": "A plain wire has almost no resistance, which is exactly "
                    "what makes it the easy route."},
            {"text": "The lamp goes out, because the wire is a route with "
                     "almost no resistance and the charge takes it",
             "correct": True},
            {"text": "The battery stops working, because a second path "
                     "back to it cancels the push of the first one and "
                     "leaves nothing driving the loop", "correct": False,
             "why": "Nothing cancels. The battery pushes harder than ever — "
                    "which is the danger, because almost nothing is limiting "
                    "the current."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-h04",
        "band": "harder",
        "text": "You are given a battery, two lamps and one switch, and told "
                "the switch must be able to turn BOTH lamps off while each "
                "lamp still runs at full brightness. How do you wire it?",
        "options": [
            {"text": "Both lamps in series with each other and the switch in "
                     "parallel with one of them", "correct": False,
             "why": "Series would leave both lamps dim, and a switch in "
                    "parallel with a lamp shorts it out rather than "
                    "switching it off."},
            {"text": "Both lamps in parallel and the switch in parallel with "
                     "them too", "correct": False,
             "why": "A switch in parallel with the lamps does not cut them "
                    "off — closing it short-circuits the battery."},
            {"text": "Everything in series, with the switch between the two "
                     "lamps", "correct": False,
             "why": "The switch would work, but both lamps would be dim: in "
                    "series the battery's push is shared between them."},
            {"text": "The two lamps in parallel with each other, and the "
                     "switch in series with the pair", "correct": True},
        ],
        "figure": None,
    },
]
