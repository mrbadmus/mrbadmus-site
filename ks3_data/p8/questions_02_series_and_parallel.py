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
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "They all go out, because their one shared path "
                     "breaks", "correct": True},
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
            {"text": "Because a switch wired in parallel would be too far "
                     "from the component it controls to work",
             "correct": False,
             "why": "Distance is irrelevant in a circuit. What matters is "
                    "which path the switch is in."},
            {"text": "Because a switch has to sit nearer the battery than "
                     "anything else in the loop", "correct": False,
             "why": "Position round a single loop makes no difference. A "
                    "switch works anywhere in the loop it is breaking."},
            {"text": "Because a switch in parallel would draw more current "
                     "from the supply while it is open", "correct": False,
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
            {"text": "It dims, because the fixed current from the battery is "
                     "now shared three ways",
             "correct": False,
             "why": "Nothing is shared out, and there is no fixed total. Each "
                    "branch draws what it draws, and the battery supplies "
                    "the total."},
            {"text": "It brightens, because more branches make it easier for "
                     "the charge to get round the circuit", "correct": False,
             "why": "The whole circuit does get easier, but the first lamp's "
                    "own branch is unchanged, so it draws exactly what it "
                    "drew before."},
            {"text": "Nothing changes for the lamp, but the battery now "
                     "supplies more current and goes flat sooner",
             "correct": True},
            {"text": "It goes out, because one battery cannot drive as many "
                     "as three branches at once", "correct": False,
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p8-02-e05",
        "band": "easier",
        "text": "Two components are in PARALLEL when…",
        "options": [
            {"text": "they sit on separate branches across the same supply",
             "correct": True},
            {"text": "they sit one after another in the same loop",
             "correct": False,
             "why": "That is series — one path, and one current through both "
                    "of them."},
            {"text": "they are the same distance from the battery",
             "correct": False,
             "why": "Distance decides nothing. What matters is how many paths "
                    "there are."},
            {"text": "they are identical to one another", "correct": False,
             "why": "A lamp and a buzzer can be in parallel; being alike has "
                    "nothing to do with it."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-e06",
        "band": "easier",
        "text": "One branch of a parallel circuit is broken. What happens to "
                "the other branches?",
        "options": [            {"text": "They all stop as well", "correct": False,
             "why": "That is what happens in series. Each parallel branch has "
                    "its own complete path."},
            {"text": "They get brighter, because they take the broken "
                     "branch's current",
             "correct": False,
             "why": "Nothing is handed on: each branch draws its own current, "
                    "which does not change."},
            {"text": "They get dimmer, because the supply is damaged",
             "correct": False,
             "why": "The supply is untouched, and each branch still has the "
                    "whole of its push."},
            {"text": "They carry on working as before", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-e07",
        "band": "easier",
        "text": "Which arrangement lets each lamp be switched off on its own?",
        "options": [            {"text": "Series, with one switch in the loop", "correct": False,
             "why": "One switch in a single loop turns everything off "
                    "together."},
            {"text": "Either, as long as the switches are identical",
             "correct": False,
             "why": "The kind of switch is irrelevant; the wiring is what "
                    "decides."},
            {"text": "Series, with a switch beside each lamp",
             "correct": False,
             "why": "Any open switch in a single loop stops the whole loop, "
                    "wherever it sits."},
            {"text": "Parallel, with a switch in each branch", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-e08",
        "band": "easier",
        "text": "How many paths are there from one end of the battery to the "
                "other in a series circuit?",
        "options": [
            {"text": "One path, whatever it passes through", "correct": True},
            {"text": "Two, one out and one back", "correct": False,
             "why": "Out and back are the two halves of a single path, not "
                    "two paths."},
            {"text": "One for each component in the loop", "correct": False,
             "why": "Components sitting one after another all lie on the same "
                    "single path."},
            {"text": "It depends on how many cells are in the battery",
             "correct": False,
             "why": "Cells in a battery sit in the same loop, so they do not "
                    "add paths."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p8-02-s05",
        "band": "standard",
        "text": "Two identical lamps are wired in series on one battery. How "
                "does each compare with a single lamp on the same battery?",
        "options": [            {"text": "Each is just as bright, because the battery has not "
                     "changed",
             "correct": False,
             "why": "The battery's push is now shared between two lamps, so "
                    "each gets less of it."},
            {"text": "The first is bright and the second is dim",
             "correct": False,
             "why": "The same current passes through both, and they share the "
                    "push equally."},
            {"text": "Each is brighter, because two lamps draw more current",
             "correct": False,
             "why": "Two lamps in series draw LESS current than one, not "
                    "more."},
            {"text": "Each is dimmer than the single lamp", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-s06",
        "band": "standard",
        "text": "A student says two lamps in parallel must each be dimmer, "
                "because the current splits between them. What is right?",
        "options": [
            {"text": "Each branch gets the whole push, so each is as "
                     "bright as one",
             "correct": True},
            {"text": "The student is right: two branches always halve the "
                     "brightness",
             "correct": False,
             "why": "Each branch draws its own current, and neither is "
                    "starved by the other's presence."},
            {"text": "Each lamp is brighter, because the branches help each "
                     "other",
             "correct": False,
             "why": "Branches do not add to one another; each simply behaves "
                    "as if it were alone."},
            {"text": "The brightness cannot be predicted without knowing the "
                     "battery's size",
             "correct": False,
             "why": "Whatever the battery, each branch gets the whole of its "
                    "push."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-s07",
        "band": "standard",
        "text": "A torch has two lamps that must BOTH go out when one switch "
                "is opened. Where does that switch go?",
        "options": [
            {"text": "In one of the two branches", "correct": False,
             "why": "That would leave the other branch lit, which is the "
                    "opposite of what is wanted."},
            {"text": "In the main wire, in series with the battery",
             "correct": True},
            {"text": "In parallel with the battery", "correct": False,
             "why": "A switch across the battery would short it out when "
                    "closed, not control the lamps."},
            {"text": "In parallel with one of the lamps", "correct": False,
             "why": "Closing that switch would short out one lamp, leaving "
                    "the other lit."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-s08",
        "band": "standard",
        "text": "Two identical lamps sit in series. A student says the first "
                "is brighter because it gets the current first. What is "
                "right?",
        "options": [            {"text": "The first is brighter, but only slightly",
             "correct": False,
             "why": "There is no difference at all: the same current passes "
                    "through both."},
            {"text": "The second is brighter, because it gets what is left "
                     "over",
             "correct": False,
             "why": "Nothing is left over. The same current goes through each "
                    "of them."},
            {"text": "It depends which way round the battery is connected",
             "correct": False,
             "why": "Reversing the battery reverses the current and changes "
                    "neither brightness."},
            {"text": "Neither is brighter, because there is nothing to be "
                     "first in a loop",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p8-02-h05",
        "band": "harder",
        "text": "Two identical lamps in parallel are rewired in series on the "
                "same battery. What happens to the current leaving the "
                "battery?",
        "options": [
            {"text": "It stays the same, because the same two lamps are "
                     "connected",
             "correct": False,
             "why": "How they are wired is exactly what changes the current, "
                    "not which lamps they are."},
            {"text": "It falls, because the two lamps now sit in one path",
             "correct": True},
            {"text": "It rises, because a single path lets charge move more "
                     "freely",
             "correct": False,
             "why": "One path with two lamps in it is harder to drive charge "
                    "through, not easier."},
            {"text": "It doubles, because series adds the two lamps together",
             "correct": False,
             "why": "Series adds what OPPOSES the current, so the current "
                    "goes down rather than up."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-h06",
        "band": "harder",
        "text": "A string of lights is advertised as one bulb out, the rest "
                "stay lit. How must it be wired, and what does that cost?",
        "options": [
            {"text": "In series, and it costs a more expensive kind of bulb",
             "correct": False,
             "why": "Series is the arrangement where one failure kills the "
                    "whole string, whatever bulbs are used."},
            {"text": "In parallel, and it costs more wire and more current "
                     "from the supply",
             "correct": True},
            {"text": "In parallel, and it costs nothing extra at all",
             "correct": False,
             "why": "Every branch needs its own wiring, and the supply has to "
                    "deliver all the branch currents."},
            {"text": "In series, and it costs a higher supply voltage",
             "correct": False,
             "why": "Raising the voltage does not make a broken series loop "
                    "carry current."},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-h07",
        "band": "harder",
        "text": "Three identical lamps: two in parallel with each other, and "
                "that pair in series with the third. Which lamp is "
                "brightest?",
        "options": [            {"text": "The two in parallel, because each gets its own branch",
             "correct": False,
             "why": "Each of them carries only part of the current, so each "
                    "is dimmer than the single one."},
            {"text": "All three are equally bright, because they are "
                     "identical",
             "correct": False,
             "why": "Being identical does not make the currents equal; the "
                    "wiring decides that."},
            {"text": "It cannot be told without knowing the battery's "
                     "voltage",
             "correct": False,
             "why": "Whatever the voltage, the single lamp carries what both "
                    "branches carry together."},
            {"text": "The single lamp, because the whole current passes "
                     "through it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p8-02-h08",
        "band": "harder",
        "text": "A fourth identical lamp is added in parallel to three that "
                "are already on a battery. What happens at the battery?",
        "options": [            {"text": "Nothing changes, because each branch looks after "
                     "itself",
             "correct": False,
             "why": "Each branch does look after itself, and the battery has "
                    "to supply one more branch's worth."},
            {"text": "It supplies less current, shared between more branches",
             "correct": False,
             "why": "Nothing is shared out. The branch currents ADD at the "
                    "battery."},
            {"text": "It supplies the same current at a higher voltage",
             "correct": False,
             "why": "A battery's push does not rise because more is asked of "
                    "it; if anything it sags."},
            {"text": "It supplies more current, so it goes flat sooner",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {"id": "p8-02-e09", "band": "easier",
     "text": "A student is told two lamps are wired in series. What does "
             "that tell you about how many paths connect them to the "
             "battery?",
     "options": [
         {"text": "There is exactly one path, passing through both lamps",
          "correct": True},
         {"text": "There are three paths — one for each lamp and one "
                  "shared return path", "correct": False,
          "why": "A series loop has just one path all the way round, not "
                 "an extra shared return on top of it."},
         {"text": "The number of paths cannot be known from the word "
                  "\"series\" alone", "correct": False,
          "why": "Series is defined exactly by there being one path; "
                 "nothing else needs to be known."},
         {"text": "There are two separate paths, one for each lamp",
          "correct": False,
          "why": "Two separate paths is what parallel means. Series is "
                 "one path shared by both."},
     ], "figure": None},
    {"id": "p8-02-e10", "band": "easier",
     "text": "A string of decorative lights is wired in series. You want "
             "to add one more identical lamp without dimming the ones "
             "already there. Where in the string could you insert it to "
             "achieve that?",
     "options": [
         {"text": "Right at the very end of the string, after the last "
                  "lamp, where the charge has already passed through "
                  "every other one", "correct": False,
          "why": "The end of the one shared path is still part of that "
                 "same path — a lamp added there still dims every lamp "
                 "in the string."},
         {"text": "Nowhere — inserting it anywhere adds to the one "
                  "shared path and dims every lamp", "correct": True},
         {"text": "Right at the start, closest to the battery",
          "correct": False,
          "why": "Position in a single shared path makes no difference; "
                 "an extra lamp dims the whole string wherever it is "
                 "inserted."},
         {"text": "Anywhere, as long as the new lamp is identical to the "
                  "others already in the string", "correct": False,
          "why": "Being identical does not stop the new lamp from "
                 "adding resistance to the one shared path, which dims "
                 "every lamp on it."},
     ], "figure": None},
    {"id": "p8-02-e11", "band": "easier",
     "text": "Two lamps are wired in series with each other, and that "
             "pair is then connected to a battery — nothing else is "
             "added. Is there a second branch anywhere in this "
             "arrangement?",
     "options": [
         {"text": "Yes — each lamp counts as its own branch",
          "correct": False,
          "why": "Being in series means the two lamps share the one "
                 "path; neither one has a branch of its own."},
         {"text": "No — there is only the one path through both lamps",
          "correct": True},
         {"text": "Yes — the battery itself always counts as a second "
                  "branch", "correct": False,
          "why": "The battery is the supply, not a branch; a branch is "
                 "one of several separate paths, and there is only one "
                 "path here."},
         {"text": "It depends on which lamp is wired closer to the "
                  "battery", "correct": False,
          "why": "Position within the one shared path makes no "
                 "difference to how many branches exist; there is still "
                 "just the one."},
     ], "figure": None},
    {"id": "p8-02-e12", "band": "easier",
     "text": "Why can every socket in a house be switched on or off "
             "independently of every other socket?",
     "options": [
         {"text": "Because each socket has a slightly different supply "
                  "voltage", "correct": False,
          "why": "Every socket in a house runs at the same supply "
                 "voltage; independence comes from the wiring, not from "
                 "different voltages."},
         {"text": "Because sockets, unlike lights, are never wired "
                  "together at all", "correct": False,
          "why": "Sockets are wired together, on parallel branches off "
                 "the same supply, just like the lights are."},
         {"text": "Because the sockets are wired in series with each "
                  "other", "correct": False,
          "why": "Series wiring would mean one switch affected every "
                 "socket at once, not each independently."},
         {"text": "Because each socket has its own branch off the "
                  "supply", "correct": True},
     ], "figure": None},
    {"id": "p8-02-e13", "band": "easier",
     "text": "Two lamps sit on separate branches, each connected straight "
             "across the same battery. What arrangement is this?",
     "options": [
         {"text": "Parallel", "correct": True},
         {"text": "A short circuit", "correct": False,
          "why": "A short circuit is an unwanted low-resistance path, not "
                 "a description of two lamps on their own branches."},
         {"text": "Neither — a battery can only drive one branch at a "
                  "time", "correct": False,
          "why": "A battery can drive as many parallel branches as are "
                 "connected to it, all at once."},
         {"text": "Series", "correct": False,
          "why": "Series would put both lamps on the one shared path, not "
                 "on separate branches."},
     ], "figure": None},
    {"id": "p8-02-e14", "band": "easier",
     "text": "A single switch is wired into the one shared path of a "
             "series loop holding three lamps. What happens when it is "
             "opened?",
     "options": [
         {"text": "Nothing happens until all three lamps are also "
                  "switched off individually", "correct": False,
          "why": "There is only the one switch in this loop; the lamps "
                 "have no switches of their own to worry about."},
         {"text": "All three lamps go out together", "correct": True},
         {"text": "Only the lamp nearest the switch goes out",
          "correct": False,
          "why": "Opening the one shared path stops the current "
                 "everywhere in the loop, not just near the switch."},
         {"text": "The lamps dim slightly but stay lit", "correct": False,
          "why": "An open switch is a complete gap, not a partial "
                 "obstacle. Nothing flows at all once it is open."},
     ], "figure": None},
    {"id": "p8-02-e15", "band": "easier",
     "text": "How many complete paths does a genuinely parallel "
             "arrangement of three lamps give the charge, from one end of "
             "the battery to the other?",
     "options": [
         {"text": "One, shared between all three lamps", "correct": False,
          "why": "One shared path is series. Parallel gives each lamp its "
                 "own path."},
         {"text": "Two, however many lamps are added", "correct": False,
          "why": "The number of paths grows with the number of branches; "
                 "it is not fixed at two."},
         {"text": "Three, one for each lamp", "correct": True},
         {"text": "It depends on how far apart the lamps are drawn",
          "correct": False,
          "why": "Distance on a diagram has no bearing on how many paths "
                 "there are; that is decided by the wiring."},
     ], "figure": None},
    {"id": "p8-02-e16", "band": "easier",
     "text": "In a series loop with two lamps, is there ever a moment when "
             "one lamp is carrying current and the other is not?",
     "options": [
         {"text": "Yes, if one lamp is much brighter than the other",
          "correct": False,
          "why": "Brightness does not create a gap in time between the "
                 "two lamps; the same current still passes through both "
                 "at once."},
         {"text": "It depends on which lamp is wired closer to the "
                  "battery", "correct": False,
          "why": "Position in a single loop makes no difference — the "
                 "current is identical everywhere in it."},
         {"text": "Yes, briefly, right after the switch closes",
          "correct": False,
          "why": "There is no such delay — the current is the same at "
                 "every point of the loop from the instant it starts."},
         {"text": "No — one loop carries one current through both at "
                  "every instant", "correct": True},
     ], "figure": None},
    {"id": "p8-02-e17", "band": "easier",
     "text": "A branch of a parallel arrangement contains nothing at all — "
             "no lamp, resistor or buzzer, just a break. What can you say "
             "about that branch?",
     "options": [
         {"text": "It carries no current at all, but the other branches "
                  "are unaffected", "correct": True},
         {"text": "It carries no current, and neither do the other "
                  "branches", "correct": False,
          "why": "In parallel, a break in one branch does not stop the "
                 "others — each has its own separate path."},
         {"text": "It carries the same current as the busiest branch",
          "correct": False,
          "why": "A broken branch has no complete path in it at all, so "
                 "it cannot carry any current, however busy other "
                 "branches are."},
         {"text": "It carries a small current, since the battery still "
                  "reaches it", "correct": False,
          "why": "Reaching a break is not enough — a broken branch has no "
                 "complete path, so no current flows through it."},
     ], "figure": None},
    {"id": "p8-02-e18", "band": "easier",
     "text": "What is the very first thing you should check to decide "
             "whether two components in a diagram are wired in series or "
             "in parallel?",
     "options": [
         {"text": "Whether they are drawn the same size", "correct": False,
          "why": "Size in a diagram carries no information about wiring "
                 "at all."},
         {"text": "How many paths there are between them and the "
                  "battery's two ends", "correct": True},
         {"text": "Which one is drawn closer to the cell", "correct": False,
          "why": "Position on the page does not decide the wiring; "
                 "following the paths does."},
         {"text": "Whether the two components are identical to each "
                  "other", "correct": False,
          "why": "Two very different components can be wired either way; "
                 "being alike has nothing to do with it."},
     ], "figure": None},

    {"id": "p8-02-e19", "band": "easier",
     "text": "A fridge and a toaster are plugged into different sockets in "
             "the same kitchen. The toaster is unplugged. Does the fridge "
             "stop working?",
     "options": [
         {"text": "Yes, but only if the toaster was drawing a large "
                  "current", "correct": False,
          "why": "The size of the toaster's current is irrelevant — "
                 "unplugging it simply removes its branch, leaving the "
                 "fridge's own branch completely untouched."},
         {"text": "Yes, because both appliances share one path back to "
                  "the supply", "correct": False,
          "why": "House sockets are wired in parallel, not series, so "
                 "there is no one shared path for both to depend on."},
         {"text": "No — each kitchen socket has its own separate branch "
                  "off the house supply", "correct": True},
         {"text": "It depends which socket was plugged in first",
          "correct": False,
          "why": "Order of plugging in makes no difference to parallel "
                 "branches; each is independent of the others regardless "
                 "of timing."},
     ], "figure": None},
    {"id": "p8-02-e20", "band": "easier",
     "text": "What word describes one of the separate paths in a parallel "
             "arrangement?",
     "options": [
         {"text": "A terminal", "correct": False,
          "why": "A terminal is a connection point on a cell or battery, "
                 "not one of the paths leading away from it."},
         {"text": "A loop", "correct": False,
          "why": "The whole arrangement, or a single-path circuit, is "
                 "usually called a loop; one path within a parallel "
                 "section has its own name."},
         {"text": "A junction", "correct": False,
          "why": "A junction is the point where branches divide or meet, "
                 "not one of the paths itself."},
         {"text": "A branch", "correct": True},
     ], "figure": None},
    {"id": "p8-02-e21", "band": "easier",
     "text": "A buzzer and a lamp are joined one after another, so charge "
             "must pass through the buzzer and then the lamp. What "
             "arrangement is this?",
     "options": [
         {"text": "Series", "correct": True},
         {"text": "Parallel", "correct": False,
          "why": "Parallel would give the buzzer and the lamp separate "
                 "paths, not one shared path passed through in order."},
         {"text": "A short circuit", "correct": False,
          "why": "Nothing here describes an unwanted low-resistance "
                 "path; it is simply two components sharing one loop."},
         {"text": "It cannot be decided without knowing which one is "
                  "drawn first", "correct": False,
          "why": "Order on the page does not decide it — passing through "
                 "one and then the other, whichever way round, is what "
                 "makes it series."},
     ], "figure": None},
    {"id": "p8-02-e22", "band": "easier",
     "text": "Two lamps sit on separate branches of a parallel "
             "arrangement. A switch is wired into just ONE of those "
             "branches. What happens when that switch is opened?",
     "options": [
         {"text": "Both lamps dim, sharing the effect of the open switch",
          "correct": False,
          "why": "Dimming both would need a shared path; here only the "
                 "one branch with the switch is affected, and it goes "
                 "fully dark rather than merely dim."},
         {"text": "Only the lamp on that branch goes out; the other stays "
                  "lit", "correct": True},
         {"text": "Both lamps go out together", "correct": False,
          "why": "A switch in one branch only breaks that branch; the "
                 "other branch has its own separate path, untouched by "
                 "it."},
         {"text": "Neither lamp is affected, since the switch is not in "
                  "the main supply wire", "correct": False,
          "why": "The switch is still part of the branch it sits in, so "
                 "opening it does break that one branch's path."},
     ], "figure": None},
    {"id": "p8-02-e23", "band": "easier",
     "text": "Two lamps sit on separate branches of a parallel "
             "arrangement. A single switch is wired into the SHARED wire "
             "leading back to the battery, before the branches split. "
             "What happens when that switch is opened?",
     "options": [
         {"text": "Only the nearer lamp goes out", "correct": False,
          "why": "The switch sits before either branch splits off, so it "
                 "affects the supply to both of them equally, not just "
                 "the nearer one."},
         {"text": "Neither lamp is affected", "correct": False,
          "why": "The shared wire is part of the path for both branches; "
                 "breaking it before they split stops both."},
         {"text": "Both lamps go out together", "correct": True},
         {"text": "The lamps swap brightness with each other",
          "correct": False,
          "why": "Nothing about opening a switch causes lamps to swap "
                 "brightness; here it simply cuts off both together."},
     ], "figure": None},
    {"id": "p8-02-e24", "band": "easier",
     "text": "Saying two components are \"in parallel\" means they are "
             "connected…",
     "options": [
         {"text": "at opposite ends of the circuit diagram",
          "correct": False,
          "why": "Position on the page does not decide the wiring; being "
                 "drawn far apart does not make two components parallel."},
         {"text": "using two different batteries, one for each of the "
                  "two components", "correct": False,
          "why": "Parallel branches normally share the same single "
                 "battery; using two batteries is a different question "
                 "altogether."},
         {"text": "one after another, along a single shared path, so that "
                  "the charge is forced to visit each of them in turn",
          "correct": False,
          "why": "That describes series. Parallel means separate paths, "
                 "not one shared one."},
         {"text": "directly across the same two points, on their own "
                  "separate branches", "correct": True},
     ], "figure": None},
    {"id": "p8-02-e25", "band": "easier",
     "text": "Two identical resistors are wired end to end in a single "
             "loop with a cell. How many paths does the charge have from "
             "one end of the cell to the other?",
     "options": [
         {"text": "One", "correct": True},
         {"text": "Two, one for each resistor", "correct": False,
          "why": "Two resistors end to end share the one path; giving "
                 "each its own path is what parallel would mean."},
         {"text": "It depends on the value of the resistors",
          "correct": False,
          "why": "The number of paths is decided by the wiring, not by "
                 "the resistors' values."},
         {"text": "Zero, since resistors block all current",
          "correct": False,
          "why": "A resistor makes current harder to push through, not "
                 "impossible; some current still flows round the one "
                 "path."},
     ], "figure": None},
    {"id": "p8-02-e26", "band": "easier",
     "text": "Modern LED string lights are wired in parallel rather than "
             "in series, specifically so that…",
     "options": [
         {"text": "each bulb can be a different colour from the others",
          "correct": False,
          "why": "Colour has nothing to do with series or parallel "
                 "wiring; bulbs of any colour can be wired either way."},
         {"text": "one bulb failing does not take out any of the others",
          "correct": True},
         {"text": "the string uses less wire overall", "correct": False,
          "why": "Parallel wiring generally needs MORE wire than series, "
                 "not less, since every branch needs its own connection."},
         {"text": "the bulbs can be dimmed individually by hand",
          "correct": False,
          "why": "Parallel wiring on its own does not let you dim "
                 "individual bulbs by hand; that needs extra controls, "
                 "not just the wiring arrangement."},
     ], "figure": None},
    {"id": "p8-02-e27", "band": "easier",
     "text": "A heater and a lamp each have their own separate branch "
             "connected straight across the same battery. What "
             "arrangement is this?",
     "options": [
         {"text": "Series", "correct": False,
          "why": "Series would put the heater and the lamp on one shared "
                 "path, not on their own separate branches."},
         {"text": "A short circuit", "correct": False,
          "why": "Having its own branch across the battery is not the "
                 "same as an unwanted low-resistance path."},
         {"text": "Parallel", "correct": True},
         {"text": "It cannot be decided without knowing which one draws "
                  "more current", "correct": False,
          "why": "The current each one draws does not decide the "
                 "arrangement; having separate branches is what makes it "
                 "parallel."},
     ], "figure": None},
    {"id": "p8-02-e28", "band": "easier",
     "text": "Four identical lamps are each given their own separate "
             "branch across the same battery. How many complete paths are "
             "there from one end of the battery to the other?",
     "options": [
         {"text": "It cannot be known without measuring each lamp's "
                  "resistance", "correct": False,
          "why": "Counting paths only needs the wiring, not the "
                 "resistance of what is in each one."},
         {"text": "One, shared between all four", "correct": False,
          "why": "One shared path is series; here each lamp has its own "
                 "branch instead."},
         {"text": "Two", "correct": False,
          "why": "The number of paths matches the number of branches, "
                 "which is four here, not two."},
         {"text": "Four", "correct": True},
     ], "figure": None},
    {"id": "p8-02-e29", "band": "easier",
     "text": "A plug from any lamp fits into any wall socket in a house "
             "and lights the lamp exactly the same way, whatever else is "
             "plugged in elsewhere. What does this tell you about how "
             "sockets are wired?",
     "options": [
         {"text": "They are wired in parallel, so each socket gets the "
                  "whole supply regardless of the others", "correct": True},
         {"text": "They must all be connected to their own separate "
                  "battery", "correct": False,
          "why": "House sockets share one supply; it is the parallel "
                 "wiring, not separate batteries, that makes each "
                 "socket behave the same."},
         {"text": "It tells you nothing reliable about the wiring at "
                  "all", "correct": False,
          "why": "This behaviour is exactly the signature of parallel "
                 "wiring — each branch getting the full supply "
                 "independently of the others."},
         {"text": "They must be wired in series, so every socket gets an "
                  "identical share", "correct": False,
          "why": "Series sharing would mean the lamp's brightness "
                 "depended on how many other things were switched on — "
                 "which is exactly what does not happen here."},
     ], "figure": None},
    {"id": "p8-02-e30", "band": "easier",
     "text": "A vacuum cleaner is plugged into a socket. A lamp in another "
             "room is then switched off. Does the vacuum's performance "
             "change?",
     "options": [
         {"text": "Yes, it runs slightly faster with less competing for "
                  "the supply", "correct": False,
          "why": "Parallel branches do not compete with each other; the "
                 "vacuum's branch is unaffected by what happens on "
                 "another one."},
         {"text": "No — its branch is completely independent of the "
                  "lamp's branch", "correct": True},
         {"text": "Yes, it runs slower, because less current overall is "
                  "now being drawn from the supply", "correct": False,
          "why": "How much current OTHER branches draw does not change "
                 "what the vacuum's own branch draws."},
         {"text": "It depends on which room's socket was wired first",
          "correct": False,
          "why": "The order sockets were wired in makes no difference to "
                 "how independent their branches are from each other."},
     ], "figure": None},
    # ── MRB-338 night 3 top-up · standard ─────────────────────────────
    # ── standard ────────────────────────────────────────────────────────
    {"id": "p8-02-s09", "band": "standard",
     "text": "A single bulb on a 3.0 V battery draws 0.30 A. Two more "
             "identical bulbs are added in parallel with it, on the same "
             "battery. What does the battery now supply?",
     "options": [
         {"text": "0.90 A", "correct": True},
         {"text": "0.60 A, because two extra bulbs double the original "
                  "current", "correct": False,
          "why": "Two extra branches ADD their own 0.30 A each to the "
                 "original, which comes to 0.90 A, not a simple doubling."},
         {"text": "0.10 A, shared out over the three branches",
          "correct": False,
          "why": "Nothing is shared out — each branch draws its own "
                 "0.30 A, and the battery supplies the total of all "
                 "three."},
         {"text": "0.30 A, the same as before", "correct": False,
          "why": "That is what one branch draws. Two more identical "
                 "branches add their own current on top of it."},
     ], "figure": None},
    {"id": "p8-02-s10", "band": "standard",
     "text": "Three identical lamps are wired in series on a battery. A "
             "fourth identical lamp is added into the same single loop. "
             "What happens to the brightness of all four lamps?",
     "options": [
         {"text": "All four become brighter, since there are now more "
                  "lamps to share the battery's push", "correct": False,
          "why": "More lamps in series does not mean more push shared "
                 "out usefully — it means more resistance for the same "
                 "current to get through, so it falls."},
         {"text": "All four are dimmer than the original three were",
          "correct": True},
         {"text": "All four stay exactly as bright as the original three "
                  "were", "correct": False,
          "why": "Adding another lamp to the one shared path makes it "
                 "harder for the charge to get round, so the current — "
                 "and the brightness — falls."},
         {"text": "The new lamp is dim and the original three are "
                  "unaffected", "correct": False,
          "why": "One current passes through all four lamps at once; "
                 "there is no way for three of them to be unaffected by "
                 "the fourth."},
     ], "figure": None},
    {"id": "p8-02-s11", "band": "standard",
     "text": "A parallel arrangement of two identical lamps is rewired so "
             "the same two lamps sit in series instead, on the same "
             "battery. Explain what happens to the total current the "
             "battery supplies.",
     "options": [
         {"text": "It stays the same, because the same two lamps and the "
                  "same battery are involved either way", "correct": False,
          "why": "Which two lamps are involved does not decide the "
                 "current — how they are wired together does."},
         {"text": "It cannot be predicted without knowing the exact "
                  "resistance of each lamp", "correct": False,
          "why": "You do not need the exact resistance to know the "
                 "DIRECTION of the change: fewer paths to a harder "
                 "arrangement always means less current overall."},
         {"text": "It falls, because the two lamps now share one harder "
                  "path instead of drawing on their own separate ones",
          "correct": True},
         {"text": "It rises, because a single path is always easier for "
                  "charge to get round than two separate ones",
          "correct": False,
          "why": "A single path through two lamps is harder to get round "
                 "than either lamp's own separate branch was, not "
                 "easier."},
     ], "figure": None},
    {"id": "p8-02-s12", "band": "standard",
     "text": "A teacher wants ONE switch that turns off every light in a "
             "classroom together, without dimming any of them while they "
             "are on. How should the lights and switch be wired?",
     "options": [
         {"text": "The lights in parallel with each other, and the switch "
                  "in parallel with each light individually",
          "correct": False,
          "why": "A switch in parallel with a light does not turn it off "
                 "— closing it short-circuits that light instead."},
         {"text": "The lights in series with each other, and the switch "
                  "in parallel with one of them", "correct": False,
          "why": "Series lights would still be dim, and a switch in "
                 "parallel with one of them shorts it out rather than "
                 "controlling the group."},
         {"text": "The lights in series with each other, and the switch "
                  "in series with the whole string", "correct": False,
          "why": "Lights in series would all be dim while running, which "
                 "breaks the \"without dimming\" requirement."},
         {"text": "The lights in parallel with each other, and the switch "
                  "in series with the whole set", "correct": True},
     ], "figure": None},
    {"id": "p8-02-s13", "band": "standard",
     "text": "A student says: \"Two lamps in parallel must be dimmer than "
             "one lamp on its own, because now there are two things "
             "sharing the battery.\" Correct this statement.",
     "options": [
         {"text": "Nothing is shared out — each lamp gets the battery's "
                  "full push and is exactly as bright as it would be "
                  "alone", "correct": True},
         {"text": "The lamps are dimmer, but only the second one added, "
                  "not the first", "correct": False,
          "why": "Both branches sit identically across the battery; "
                 "neither is treated differently for having been added "
                 "second."},
         {"text": "The student is completely right, and this is exactly "
                  "why parallel wiring is avoided in ordinary house "
                  "circuits", "correct": False,
          "why": "Parallel wiring is exactly how houses ARE wired, "
                 "specifically because it does not dim anything."},
         {"text": "The student is right about the dimming, but wrong "
                  "about why — it is the resistance of the lamps, not "
                  "there being two of them, that dims each one",
          "correct": False,
          "why": "Neither lamp dims at all in parallel — each has the "
                 "battery's whole push across it, exactly as it would "
                 "alone."},
     ], "figure": None},
    {"id": "p8-02-s14", "band": "standard",
     "text": "A string of ten identical lamps is wired in series. One is "
             "removed from its socket entirely, leaving an empty gap. What "
             "happens to the other nine, and could you tell the difference "
             "between this and one of them simply having a blown "
             "filament?",
     "options": [
         {"text": "The other nine dim slightly for a removed lamp, but go "
                  "fully dark for a blown filament", "correct": False,
          "why": "Both are simply a gap in the one shared path; neither "
                 "produces a partial dimming rather than the other."},
         {"text": "The other nine go dark either way, and both faults "
                  "look electrically identical from outside the string",
          "correct": True},
         {"text": "The other nine stay lit either way, since the string "
                  "has plenty of working lamps left", "correct": False,
          "why": "In series there is only the one shared path; either "
                 "fault breaks it and every lamp goes dark."},
         {"text": "Removing a lamp is different from a blown filament, "
                  "because removing it leaves a visible gap in the "
                  "socket", "correct": False,
          "why": "Visually you could tell them apart by looking, but "
                 "electrically — from the current and brightness alone — "
                 "the two faults behave identically."},
     ], "figure": None},
    {"id": "p8-02-s15", "band": "standard",
     "text": "Explain why adding a lamp in parallel changes the current "
             "leaving the battery, but adding the same lamp in series "
             "changes it in the opposite direction.",
     "options": [
         {"text": "Both arrangements increase the current, just by "
                  "different amounts each time", "correct": False,
          "why": "Series wiring reduces the current, because the shared "
                 "path becomes harder to get round with an extra lamp in "
                 "it."},
         {"text": "Neither arrangement changes the current, because the "
                  "battery always supplies exactly the same amount",
          "correct": False,
          "why": "A battery supplies whatever the circuit around it "
                 "asks for, and that amount clearly changes with how a "
                 "new lamp is wired in."},
         {"text": "In parallel the new branch adds its own current to "
                  "the total; in series the new lamp adds resistance to "
                  "the one shared path and reduces the current",
          "correct": True},
         {"text": "In parallel the new lamp reduces the current by "
                  "sharing the battery; in series it increases the "
                  "current by adding a second push", "correct": False,
          "why": "A lamp does not push at all, in either arrangement, "
                 "and a parallel branch does not share anything with "
                 "the others — it simply draws its own current."},
     ], "figure": None},
    {"id": "p8-02-s16", "band": "standard",
     "text": "A car has two identical rear lamps that must each shine at "
             "full brightness, and a fault in one must not affect the "
             "other. Which arrangement satisfies both requirements?",
     "options": [
         {"text": "Either arrangement works equally well for this "
                  "purpose", "correct": False,
          "why": "Only parallel meets both requirements; series would "
                 "dim both lamps and let one fault kill the other."},
         {"text": "Series, but only if a fuse is added between the two "
                  "lamps", "correct": False,
          "why": "A fuse between them would not stop a fault in one lamp "
                 "from breaking the one shared path that both depend on."},
         {"text": "Series, because one shared path is simpler to wire",
          "correct": False,
          "why": "Series wiring fails both requirements at once — the "
                 "lamps would be dim, and one fault would take out the "
                 "other too."},
         {"text": "Parallel", "correct": True},
     ], "figure": None},

    {"id": "p8-02-s17", "band": "standard",
     "text": "A lamp drawing 0.30 A, a buzzer drawing 0.10 A and a heater "
             "drawing 0.20 A are each on their own branch across the same "
             "battery. What total current does the battery supply?",
     "options": [
         {"text": "0.60 A", "correct": True},
         {"text": "0.20 A, the average of the three", "correct": False,
          "why": "An average is not what a battery supplies to parallel "
                 "branches; it supplies the total of what they each "
                 "draw."},
         {"text": "0.006 A, the three currents multiplied together",
          "correct": False,
          "why": "Branch currents in parallel add together; they are "
                 "never multiplied."},
         {"text": "0.30 A, the largest of the three branch currents",
          "correct": False,
          "why": "The battery supplies the SUM of all three branch "
                 "currents, not just the largest one."},
     ], "figure": None},
    {"id": "p8-02-s18", "band": "standard",
     "text": "Two identical lamps in parallel each draw 0.30 A. The "
             "switch in one branch is opened. What does the battery now "
             "supply?",
     "options": [
         {"text": "0.60 A, unchanged, since one branch's switch does not "
                  "affect the total", "correct": False,
          "why": "Opening a branch's switch removes that branch's "
                 "current from the total, so the total does fall."},
         {"text": "0.30 A", "correct": True},
         {"text": "0.15 A, since the remaining lamp now shares the "
                  "supply with the open branch", "correct": False,
          "why": "An open branch carries nothing to share; the "
                 "surviving branch simply keeps drawing its own 0.30 A."},
         {"text": "0.00 A, because opening any switch in a parallel "
                  "arrangement stops the whole thing", "correct": False,
          "why": "A switch in one branch only breaks that branch; the "
                 "other branch's separate path is unaffected."},
     ], "figure": None},
    {"id": "p8-02-s19", "band": "standard",
     "text": "Three identical lamps in series are compared with two "
             "identical lamps in series, on the same battery. Which set "
             "is dimmer?",
     "options": [
         {"text": "Both sets are equally bright, since all the lamps are "
                  "identical", "correct": False,
          "why": "Identical lamps do not guarantee identical brightness "
                 "— the number of them sharing one path changes how much "
                 "current gets through."},
         {"text": "It cannot be judged without knowing the battery's "
                  "exact size", "correct": False,
          "why": "Whatever the battery, adding another lamp to the one "
                 "shared path always makes the current — and the "
                 "brightness — fall further."},
         {"text": "The three-lamp set", "correct": True},
         {"text": "The two-lamp set, because sharing between fewer lamps "
                  "means each gets less", "correct": False,
          "why": "Fewer lamps in series makes the shared path EASIER to "
                 "get round, giving a larger current and brighter lamps, "
                 "not dimmer ones."},
     ], "figure": None},
    {"id": "p8-02-s20", "band": "standard",
     "text": "A student wires a plain piece of wire in parallel with a "
             "switch, expecting no change since the switch is \"off to "
             "the side\". What actually happens whenever that switch is "
             "left open?",
     "options": [
         {"text": "The circuit becomes safer, since there are now two "
                  "ways for the current to get through", "correct": False,
          "why": "Having an extra always-open path defeats the point of "
                 "the switch rather than making anything safer."},
         {"text": "The wire only matters once the switch is closed, not "
                  "while it is open", "correct": False,
          "why": "The wire provides a path whether the switch is open or "
                 "closed — it is precisely WHILE the switch is open that "
                 "the wire's path matters."},
         {"text": "Nothing changes — a plain wire off to one side cannot "
                  "affect the circuit", "correct": False,
          "why": "The wire offers an alternative path of its own, and an "
                 "alternative path with almost no resistance is never "
                 "\"off to the side\" electrically."},
         {"text": "It carries on working anyway, since the wire "
                  "gives it a path regardless", "correct": True},
     ], "figure": None},
    {"id": "p8-02-s21", "band": "standard",
     "text": "A student wires two lamp branches, but by mistake connects "
             "both of them to the SAME single terminal of the battery, "
             "never reaching the other terminal at all. What happens?",
     "options": [
         {"text": "Neither lamp lights, because there is no complete "
                  "path from one terminal to the other for either of "
                  "them", "correct": True},
         {"text": "Only one lamp lights — whichever of the two branches "
                  "happened to be connected to that terminal first",
          "correct": False,
          "why": "Order of connecting them makes no difference; neither "
                 "branch reaches both terminals, so neither is a "
                 "complete path."},
         {"text": "Both lamps light, but dimmer than usual",
          "correct": False,
          "why": "Dim implies some current is flowing; with no complete "
                 "path to the other terminal, no current flows at all."},
         {"text": "Both lamps light normally, since each has its own "
                  "branch, and a branch needs one firm connection to "
                  "the battery to work", "correct": False,
          "why": "Having separate branches only helps once each one "
                 "actually reaches both terminals of the battery."},
     ], "figure": None},
    {"id": "p8-02-s22", "band": "standard",
     "text": "The shared path of two lamps wired in series carries "
             "0.20 A. What current passes through EACH lamp?",
     "options": [
         {"text": "0.10 A each, since the current is shared between them",
          "correct": False,
          "why": "Series does not share current out between components; "
                 "the same current passes through every one of them."},
         {"text": "0.20 A each", "correct": True},
         {"text": "0.40 A each, since both lamps add to the shared "
                  "reading", "correct": False,
          "why": "Adding is what happens to branch currents in parallel; "
                 "in series the one reading already IS what each lamp "
                 "carries."},
         {"text": "It depends which lamp is nearer the battery",
          "correct": False,
          "why": "Position in a single loop makes no difference — the "
                 "current is identical at every point of it."},
     ], "figure": None},
    {"id": "p8-02-s23", "band": "standard",
     "text": "Two identical buzzers are wired in parallel on a battery, "
             "each drawing 0.15 A on its own. What total current does the "
             "battery supply, and does either buzzer sound differently "
             "because the other is present?",
     "options": [
         {"text": "0.15 A total, shared between the two buzzers",
          "correct": False,
          "why": "Nothing is shared out in parallel — each branch draws "
                 "its own current, and the battery supplies the total of "
                 "both."},
         {"text": "0.15 A total, since two identical buzzers cancel each "
                  "other's demand", "correct": False,
          "why": "Identical branches do not cancel each other; both "
                 "draw current in the same direction, adding at the "
                 "battery."},
         {"text": "0.30 A total, and neither buzzer's own sound is "
                  "affected by the other's presence", "correct": True},
         {"text": "0.30 A total, but both buzzers sound quieter than "
                  "they would alone", "correct": False,
          "why": "Each buzzer's own branch is unaffected by the other "
                 "one; it draws exactly the current it would draw on its "
                 "own, so its sound is unaffected too."},
     ], "figure": None},
    {"id": "p8-02-s24", "band": "standard",
     "text": "Which of these is a genuine real-world example of "
             "components wired in SERIES: two lamps sharing one path "
             "with a single cell, a fridge and a lamp on their own "
             "separate house sockets, or two phone chargers plugged into "
             "different sockets?",
     "options": [
         {"text": "A fridge and a lamp on their own separate house "
                  "sockets", "correct": False,
          "why": "Separate sockets are separate branches off the same "
                 "supply — that is parallel, not series."},
         {"text": "Two phone chargers plugged into different sockets",
          "correct": False,
          "why": "Different sockets again means separate branches, "
                 "which is parallel rather than a single shared path."},
         {"text": "None of these examples is genuinely series or "
                  "parallel", "correct": False,
          "why": "The first example — two lamps sharing one path with "
                 "one cell — is a straightforward, genuine example of "
                 "series wiring."},
         {"text": "Two lamps sharing one path with a single cell",
          "correct": True},
     ], "figure": None},
    {"id": "p8-02-s25", "band": "standard",
     "text": "A car radio and its headlights are on separate branches of "
             "the same 12 V battery. The radio is switched off. What "
             "happens to the headlights' brightness?",
     "options": [
         {"text": "It is unaffected — the two run on independent "
                  "branches of the same battery", "correct": True},
         {"text": "The headlights brighten, since less current overall "
                  "is now being drawn from the battery", "correct": False,
          "why": "A parallel branch's current depends only on its own "
                 "resistance and the battery's push, not on what other "
                 "branches happen to be doing."},
         {"text": "The headlights dim slightly, since the battery is now "
                  "under less total load", "correct": False,
          "why": "Less total load does not dim a healthy branch; each "
                 "branch keeps drawing exactly what it always drew."},
         {"text": "It depends on how loud the radio was before it was "
                  "switched off", "correct": False,
          "why": "The radio's own volume has no bearing on the "
                 "headlights' branch, which is entirely independent of "
                 "it."},
     ], "figure": None},
    {"id": "p8-02-s26", "band": "standard",
     "text": "Two lamps are wired in series with each other, and that "
             "pair is then wired in parallel with a third identical lamp, "
             "across the same battery. Is the third lamp's brightness "
             "affected by what happens to the series pair — for instance, "
             "if one of them fails?",
     "options": [
         {"text": "It cannot be judged without knowing which lamp in the "
                  "series pair fails first", "correct": False,
          "why": "Which lamp fails within the series pair makes no "
                 "difference to the third lamp, since its branch is "
                 "entirely separate from that pair's branch."},
         {"text": "No — the third lamp is on its own separate branch, "
                  "independent of the series pair", "correct": True},
         {"text": "Yes, because all three lamps ultimately share the "
                  "same single battery", "correct": False,
          "why": "Sharing the same battery is not the same as sharing "
                 "the same path; the third lamp's own branch is what "
                 "decides its current, not the series pair's condition."},
         {"text": "Yes, but only once the series pair has completely "
                  "failed rather than just dimmed", "correct": False,
          "why": "Even a complete failure in the series pair's branch "
                 "leaves the third lamp's own separate branch untouched."},
     ], "figure": None},
    {"id": "p8-02-s27", "band": "standard",
     "text": "Compare what a break in the ONE shared path does in a "
             "series loop with what a break in ONE branch does in a "
             "parallel arrangement.",
     "options": [
         {"text": "A series break only affects the component nearest to "
                  "it; a parallel break affects the whole arrangement",
          "correct": False,
          "why": "It is the other way round: a series break stops "
                 "everything in the one shared loop, while a parallel "
                 "break is confined to just that one branch."},
         {"text": "Neither kind of break has any effect unless a fuse is "
                  "also fitted", "correct": False,
          "why": "No fuse is needed for a break to have an effect; a "
                 "gap anywhere in a path always stops the current in "
                 "that path."},
         {"text": "A series break stops every component in the loop; "
                  "a parallel break stops just that one branch",
          "correct": True},
         {"text": "Both kinds of break stop every component in the whole "
                  "circuit, whichever arrangement is used", "correct": False,
          "why": "That is true only for series. A break in one parallel "
                 "branch leaves the other branches working normally."},
     ], "figure": None},
    {"id": "p8-02-s28", "band": "standard",
     "text": "A car's two brake lights and its single reversing light "
             "are all wired in parallel on the same battery. Pressing "
             "the brake pedal lights only the brake lights, never the "
             "reversing light. What does this tell you about the "
             "reversing light's branch?",
     "options": [
         {"text": "It must be wired in series with the brake lights "
                  "rather than in parallel with them", "correct": False,
          "why": "If it were in series with the brake lights, it would "
                 "light up together with them whenever the brakes were "
                 "pressed, which is not what happens."},
         {"text": "It draws far less current than the brake lights, "
                  "which is why the pedal cannot switch it on",
          "correct": False,
          "why": "How much current a branch draws does not decide "
                 "whether a particular switch controls it; only the "
                 "wiring of the switch does."},
         {"text": "It has no switch at all and is permanently lit "
                  "whenever the car is running", "correct": False,
          "why": "A reversing light is not permanently lit while "
                 "driving forward; it needs its own switch, just one "
                 "linked to reverse gear rather than to the brake "
                 "pedal."},
         {"text": "It must have its own separate switch, controlled "
                  "independently of the brake pedal", "correct": True},
     ], "figure": None},
    {"id": "p8-02-s29", "band": "standard",
     "text": "A washing machine and a kettle are plugged into different "
             "sockets on the same house ring and switched on together, "
             "with neither working any differently from when it is used "
             "alone. What property of parallel wiring explains this?",
     "options": [
         {"text": "Each appliance's branch gets the whole of the "
                  "supply's push, regardless of what else is connected",
          "correct": True},
         {"text": "Parallel wiring automatically limits how much current "
                  "any one appliance can draw", "correct": False,
          "why": "Parallel wiring does not limit an appliance's current "
                 "at all — each branch simply draws whatever its own "
                 "resistance and the supply's push give it."},
         {"text": "The two appliances take turns drawing current from "
                  "the supply", "correct": False,
          "why": "Parallel branches all draw current at the same time; "
                 "nothing about the wiring makes them take turns."},
         {"text": "Each appliance is secretly given its own separate "
                  "battery inside the house wiring", "correct": False,
          "why": "All the sockets share the one house supply; it is the "
                 "parallel wiring, not separate batteries, that makes "
                 "each behave independently."},
     ], "figure": None},
    {"id": "p8-02-s30", "band": "standard",
     "text": "A parallel arrangement's total current is measured with a "
             "single ammeter in the main wire, before the branches "
             "split. Does that one reading tell you how the current "
             "splits between the branches?",
     "options": [
         {"text": "No — it only gives the total; a separate reading in "
                  "each branch is needed to know the split",
          "correct": True},
         {"text": "Yes — the main-wire reading always splits equally "
                  "between however many branches there are",
          "correct": False,
          "why": "Branches are not given equal shares; each draws its "
                 "own current depending on its own resistance."},
         {"text": "Yes — the main wire's reading is simply the smaller "
                  "of the two branch readings", "correct": False,
          "why": "The main wire carries the SUM of the branch readings, "
                 "not whichever one happens to be smaller."},
         {"text": "It depends on whether the branches contain identical "
                  "components or not", "correct": False,
          "why": "Whether the components are identical or not, one "
                 "total reading never by itself reveals how it was made "
                 "up between the branches."},
     ], "figure": None},
    # ── MRB-338 night 3 top-up · harder ───────────────────────────────
    # ── harder ──────────────────────────────────────────────────────────
    {"id": "p8-02-h09", "band": "harder",
     "text": "Circuit A has two identical lamps in series on a battery. "
             "Circuit B has the same two lamps in parallel on an "
             "identical battery. Compare the total current each battery "
             "supplies, and the brightness of each lamp.",
     "options": [
         {"text": "Battery A supplies less current than battery B, and "
                  "each lamp in A is dimmer than each lamp in B",
          "correct": True},
         {"text": "Both batteries supply the same current, but the lamps "
                  "in A are dimmer because they are further from the "
                  "battery", "correct": False,
          "why": "Distance from the battery is not what dims a series "
                 "lamp — sharing one harder path with another lamp is."},
         {"text": "Battery A supplies more current than battery B, "
                  "because a single shared path is more efficient",
          "correct": False,
          "why": "A single path through two lamps resists the current "
                 "more, not less, so battery A supplies LESS current, not "
                 "more."},
         {"text": "Both batteries supply the same current and both sets "
                  "of lamps are equally bright, since the components are "
                  "identical", "correct": False,
          "why": "Identical components do not guarantee identical "
                 "outcomes — the wiring between them changes both the "
                 "current and the brightness."},
     ], "figure": None},
    {"id": "p8-02-h10", "band": "harder",
     "text": "A three-lamp parallel arrangement has one lamp unscrewed. A "
             "student argues the remaining two lamps must now be brighter, "
             "\"because there is less competition for the battery's "
             "current.\" What is wrong with this reasoning?",
     "options": [
         {"text": "The competition is real, but becomes noticeable mainly "
                  "once a fourth lamp is added rather than removed",
          "correct": False,
          "why": "There is no competition at any number of parallel "
                 "branches — each branch's current depends only on its "
                 "own resistance and the battery's push."},
         {"text": "There is no competition between branches — each "
                  "draws its own current regardless of the others",
          "correct": True},
         {"text": "The reasoning is correct, and the two lamps really do "
                  "get brighter once the third is removed", "correct": False,
          "why": "The two remaining lamps are completely unaffected — "
                 "each still has the same battery across its own "
                 "unchanged branch."},
         {"text": "The reasoning would be right if the lamps were "
                  "different sizes, but not when they are identical",
          "correct": False,
          "why": "Whether the lamps are identical or not, parallel "
                 "branches simply do not compete with each other for "
                 "current."},
     ], "figure": None},
    {"id": "p8-02-h11", "band": "harder",
     "text": "A designer wants a set of four identical warning lamps that "
             "must ALL be equally bright, and where a single failed lamp "
             "must dim none of the survivors but should be noticeable as "
             "a drop in the total current drawn. Which arrangement, and "
             "why?",
     "options": [
         {"text": "Series — because a series arrangement is what shows a "
                  "change in the total current when a lamp fails",
          "correct": False,
          "why": "A parallel arrangement shows exactly this kind of "
                 "change too — the total current drops by that branch's "
                 "share when one lamp fails."},
         {"text": "Parallel, but the requirement about noticing a drop in "
                  "current cannot be met by any arrangement at all",
          "correct": False,
          "why": "It can be met by parallel wiring — a failed branch "
                 "simply stops contributing its share to the total "
                 "current, which is a visible, measurable drop."},
         {"text": "Parallel — each branch gets the full push, so a "
                  "failure only lowers the total current",
          "correct": True},
         {"text": "Series — equal brightness because one shared current "
                  "passes through all four identically, and a failure "
                  "shows up as a fall in the total current",
          "correct": False,
          "why": "A series failure does not just lower the total "
                 "current — it breaks the one shared path completely, "
                 "taking out every lamp, not just dimming the total."},
     ], "figure": None},
    {"id": "p8-02-h12", "band": "harder",
     "text": "A cheap torch and an expensive one both use two identical "
             "1.5 V cells and an identical bulb, but the cheap one is "
             "noticeably dimmer. A technician suspects one torch wires its "
             "cells differently from the other. What difference in wiring "
             "could explain it, given both torches otherwise work?",
     "options": [
         {"text": "The dim torch's bulb might simply be a different "
                  "shape from the bright torch's bulb", "correct": False,
          "why": "The question is specifically about a wiring difference "
                 "in the cells, and an identical bulb was stated in both "
                 "torches."},
         {"text": "The dim torch's cells are wired in parallel with each "
                  "other instead of in series", "correct": True},
         {"text": "The bulb in the dim torch must be wired in parallel "
                  "with the cells rather than in series with them",
          "correct": False,
          "why": "A bulb wired in parallel with the cells, rather than in "
                 "the one loop with them, would not light at all in a "
                 "normal torch arrangement."},
         {"text": "The dim torch's cells are wired one forward and one "
                  "back, which partly cancels their push", "correct": False,
          "why": "Two IDENTICAL cells facing opposite ways cancel each "
                 "other exactly, not partly, so that torch's bulb would "
                 "not light at all rather than being merely dim."},
     ], "figure": None},
    {"id": "p8-02-h13", "band": "harder",
     "text": "Two identical lamps are wired in series on a battery, giving "
             "each a certain brightness. Without changing the battery or "
             "either lamp, describe ONE single change to the wiring that "
             "would make BOTH lamps reach full brightness simultaneously.",
     "options": [
         {"text": "Rewire the two lamps so each sits on its own branch, "
                  "straight across the battery, instead of sharing one "
                  "path", "correct": True},
         {"text": "Swap the positions of the two lamps within the same "
                  "single loop", "correct": False,
          "why": "Position within one loop makes no difference — the "
                 "same reduced current still passes through both lamps "
                 "either way."},
         {"text": "Add a third identical lamp into the same single loop",
          "correct": False,
          "why": "A third lamp added to the same shared path makes the "
                 "current — and the brightness of all three — fall "
                 "further, not rise to full brightness."},
         {"text": "Reverse the battery's connections without changing "
                  "anything else about the wiring", "correct": False,
          "why": "Reversing the battery changes the direction of the "
                 "current, not its size, so the lamps stay exactly as "
                 "dim as before."},
     ], "figure": None},
    {"id": "p8-02-h14", "band": "harder",
     "text": "A four-branch parallel arrangement has one branch containing "
             "a lamp and the other three left completely open (no "
             "component, no connection at all). Compare this to a single "
             "lamp connected on its own, with no other branches present.",
     "options": [
         {"text": "The two cases cannot be compared without knowing how "
                  "many branches the battery is rated to support",
          "correct": False,
          "why": "A battery is not \"rated\" for a fixed number of "
                 "branches in this sense; it simply supplies whatever "
                 "current the connected branches actually draw."},
         {"text": "The two situations are electrically identical — the "
                  "open branches carry nothing and do not affect the lit "
                  "one", "correct": True},
         {"text": "The single-lamp case draws more current, since it has "
                  "no other branches competing for the battery's push",
          "correct": False,
          "why": "There is no competition between branches to begin "
                 "with, whether they are open or carrying a lamp; the "
                 "lit branch draws exactly the same current in both "
                 "cases."},
         {"text": "The four-branch case draws less current overall, "
                  "since three of its four paths are broken",
          "correct": False,
          "why": "Open branches carry no current and contribute nothing "
                 "either way, so the total current comes only from the "
                 "one lit branch — identical in both cases."},
     ], "figure": None},
    {"id": "p8-02-h15", "band": "harder",
     "text": "A student builds what they believe is a parallel circuit "
             "with two lamps, but by mistake wires a switch into the "
             "single wire connecting the two branches back to the "
             "battery's other terminal — a wire both branches share. "
             "What effect does that switch have?",
     "options": [
         {"text": "It affects whichever of the two lamps happens to be "
                  "wired closer to it along the shared wire, and no "
                  "other", "correct": False,
          "why": "The switch sits on a wire shared by both branches "
                 "before they reach the battery, so it affects both "
                 "equally, not just the nearer one."},
         {"text": "It turns the parallel arrangement into a series one "
                  "automatically", "correct": False,
          "why": "The two lamps still sit on their own separate branches "
                 "further along; only the shared return wire has "
                 "changed, which does not turn them into a single "
                 "series path."},
         {"text": "It behaves like a switch in series with the WHOLE "
                  "parallel pair, cutting off both lamps together when "
                  "opened", "correct": True},
         {"text": "It has no effect, since a switch controls just the "
                  "branch it is physically wired inside, and this one "
                  "sits outside both of them", "correct": False,
          "why": "A shared wire that both branches must use to complete "
                 "their loop is still part of both loops; a break in it "
                 "stops both."},
     ], "figure": None},
    {"id": "p8-02-h16", "band": "harder",
     "text": "Explain why a fuse, which is meant to protect an entire "
             "circuit by breaking if the current gets too large, is "
             "always wired in series with what it protects, never in "
             "parallel with it.",
     "options": [
         {"text": "Because a fuse in parallel would end up doubling the "
                  "total resistance of the whole circuit and wasting "
                  "a lot of energy", "correct": False,
          "why": "A parallel fuse would not double any resistance; the "
                 "real problem is that it would not be in the current's "
                 "path at all, so it could never sense an overload to "
                 "break on."},
         {"text": "Because a parallel fuse would have to be a different "
                  "physical size from a series one to fit the holder",
          "correct": False,
          "why": "Size is not the reason; the reason is about which "
                 "wiring position lets the fuse actually experience the "
                 "current it is meant to be protecting against."},
         {"text": "Because a series fuse can be reset after it blows, "
                  "whereas a parallel one cannot", "correct": False,
          "why": "Resetting has nothing to do with the wiring position; "
                 "the real issue is that a parallel fuse would not carry "
                 "the protected current at all."},
         {"text": "Because only a series fuse sits in the path all the "
                  "current must use, so breaking it stops everything",
          "correct": True},
     ], "figure": None},
    {"id": "p8-02-h17", "band": "harder",
     "text": "Two identical lamps sit in parallel with each other, and that "
             "pair sits in series with a third identical lamp. One of the "
             "two lamps in the parallel pair blows, leaving its branch "
             "broken. What happens to the THIRD lamp?",
     "options": [
         {"text": "It goes out, because a blown lamp breaks the only path "
                  "the current had", "correct": False,
          "why": "The surviving parallel branch still offers a complete "
                 "path, so the loop is not broken and the third lamp "
                 "stays lit."},
         {"text": "It dims, because the one shared path is now harder to "
                  "push charge through", "correct": True},
         {"text": "It brightens, because it takes over the current the "
                  "blown lamp used to carry", "correct": False,
          "why": "No branch hands its current on to anything; losing a "
                 "branch makes the whole loop harder to drive, so less "
                 "current passes the third lamp, not more."},
         {"text": "Nothing changes, because the blown lamp was on its own "
                  "separate branch away from the third lamp",
          "correct": False,
          "why": "Losing one of two parallel branches makes the PAIR "
                 "harder to get through, and the third lamp is in series "
                 "with that pair, so what happens there does reach it."},
     ], "figure": None},
    {"id": "p8-02-h18", "band": "harder",
     "text": "A parallel arrangement of two lamps is working normally. One "
             "branch is then rewired so its lamp sits in series with a "
             "brand-new switch, while the OTHER branch is left completely "
             "unchanged. The new switch is left open. Describe the state "
             "of each lamp, and of the battery's total current.",
     "options": [
         {"text": "The unchanged lamp goes dark instead, because it now "
                  "has to carry the whole of the other branch's current "
                  "as well as its own", "correct": False,
          "why": "A branch does not inherit another branch's current; "
                 "the unchanged lamp simply keeps drawing exactly what it "
                 "always drew."},
         {"text": "The unchanged lamp shines as before; the other is "
                  "dark, since its branch has a gap; the total falls "
                  "to the surviving share", "correct": True},
         {"text": "Both lamps go dark, because opening any switch "
                  "anywhere breaks the whole arrangement, wherever in "
                  "it that switch happens to be wired", "correct": False,
          "why": "A switch inside ONE branch only breaks that branch; "
                 "the other branch's own separate path is completely "
                 "unaffected."},
         {"text": "Both lamps stay lit exactly as before, because "
                  "parallel branches do not affect each other in any way",
          "correct": False,
          "why": "The branch containing the new open switch is itself "
                 "broken, so that lamp specifically goes dark — the "
                 "unaffected part is only the OTHER branch."},
     ], "figure": None},
    {"id": "p8-02-h19", "band": "harder",
     "text": "A parallel pair of identical lamps each draw 0.30 A. A "
             "third identical lamp is added in parallel. Immediately "
             "afterwards, the first lamp is removed entirely. Track the "
             "total battery current through both changes, in order.",
     "options": [
         {"text": "It stays at 0.60 A throughout both changes",
          "correct": False,
          "why": "Adding a third branch genuinely raises the total "
                 "before anything is removed; the total does not stay "
                 "fixed."},
         {"text": "It rises to 0.60 A, then falls to 0.30 A",
          "correct": False,
          "why": "Adding a THIRD lamp to an existing pair gives three "
                 "branches at 0.30 A each, which is 0.90 A, not 0.60 A."},
         {"text": "It rises to 0.90 A, then falls to 0.60 A",
          "correct": True},
         {"text": "It rises to 0.90 A, then falls all the way back to "
                  "0.30 A", "correct": False,
          "why": "Removing only the first lamp still leaves two working "
                 "branches, each drawing 0.30 A, giving 0.60 A — not a "
                 "return to a single branch's current."},
     ], "figure": None},
    {"id": "p8-02-h20", "band": "harder",
     "text": "Two identical lamps in series each glow well below their "
             "normal brightness. A student connects a plain wire directly "
             "across just ONE of the two lamps, in parallel with that "
             "lamp alone. What happens to each lamp?",
     "options": [
         {"text": "Both lamps go dark, since the wire short-circuits the "
                  "whole loop", "correct": False,
          "why": "The wire is only in parallel with ONE lamp, not with "
                 "the whole loop, so only that one lamp is bypassed."},
         {"text": "The bypassed lamp becomes brighter, since it now has "
                  "an extra path helping it", "correct": False,
          "why": "The wire does not help the lamp — it offers an "
                 "alternative, easier route that the current takes "
                 "instead of going through the lamp at all."},
         {"text": "Neither lamp changes, since the wire is simply added "
                  "alongside one of them, not replacing anything",
          "correct": False,
          "why": "A near-zero-resistance path added alongside a lamp "
                 "diverts almost all the current away from that lamp, "
                 "which is a real change, not none at all."},
         {"text": "The bypassed lamp goes dark; the other becomes "
                  "brighter", "correct": True},
     ], "figure": None},
    {"id": "p8-02-h21", "band": "harder",
     "text": "A designer wants four lamps such that ONE master switch "
             "turns off all four together, but a fault in any single "
             "lamp must not affect the other three. Describe the "
             "necessary wiring for both the lamps and the switch.",
     "options": [
         {"text": "The four lamps in parallel with each other, and the "
                  "master switch in series with their shared supply "
                  "wire", "correct": True},
         {"text": "The four lamps in series with each other, with the "
                  "master switch anywhere in the one shared loop",
          "correct": False,
          "why": "Series lamps would already fail the second "
                 "requirement — one lamp's fault would take out the "
                 "other three, master switch or not."},
         {"text": "The four lamps in parallel, with a completely "
                  "separate master switch wired individually into "
                  "each of the four branches", "correct": False,
          "why": "Four separate switches could not be operated as a "
                 "single master switch turning everything off together "
                 "in one action."},
         {"text": "The four lamps in series, with the master switch "
                  "wired in parallel with just one of them",
          "correct": False,
          "why": "A switch in parallel with one lamp would short that "
                 "lamp out when closed rather than controlling the whole "
                 "group when opened."},
     ], "figure": None},
    {"id": "p8-02-h22", "band": "harder",
     "text": "Explain why doubling the number of identical parallel "
             "branches does not double the brightness of any single "
             "lamp, but does roughly double how quickly the battery runs "
             "flat.",
     "options": [
         {"text": "Both effects are caused by the same thing: the "
                  "battery's push falling as more branches are added",
          "correct": False,
          "why": "The battery's push to each branch does not fall in "
                 "this ideal picture; what changes is only the TOTAL "
                 "current it has to supply."},
         {"text": "Each branch draws its own current, unaffected by the "
                  "others; the battery just supplies a bigger total, so "
                  "it drains faster", "correct": True},
         {"text": "Each lamp's brightness depends on how many other "
                  "branches exist, so more branches should really "
                  "double the brightness of each one", "correct": False,
          "why": "A parallel branch's own current does not depend on how "
                 "many other branches there are; brightness stays the "
                 "same, however many are added."},
         {"text": "The battery runs flat at the same rate regardless, "
                  "since its rating fixes how long it lasts", "correct": False,
          "why": "A battery's store is used up faster the more total "
                 "current it has to supply, and doubling the branches "
                 "roughly doubles that total."},
     ], "figure": None},
    {"id": "p8-02-h23", "band": "harder",
     "text": "A single loop contains two lamps in series. A wire is "
             "connected in parallel across BOTH lamps TOGETHER, from one "
             "end of the pair to the other. What happens to the two "
             "lamps?",
     "options": [
         {"text": "Both lamps become brighter, since the wire gives the "
                  "loop an extra path to help the current along",
          "correct": False,
          "why": "The wire does not help the lamps — it gives the "
                 "current an easier route that bypasses them almost "
                 "entirely, so neither lamp lights."},
         {"text": "Neither lamp is affected, since the wire is in "
                  "parallel rather than replacing anything in the "
                  "series loop", "correct": False,
          "why": "An almost resistance-free path added in parallel with "
                 "the whole pair diverts nearly all the current away "
                 "from both lamps."},
         {"text": "Both go dark, since the wire bypasses the whole "
                  "pair with an almost resistance-free path",
          "correct": True},
         {"text": "Just the first lamp goes dark, since the wire reaches "
                  "merely as far as the point between the two lamps",
          "correct": False,
          "why": "The wire is connected across BOTH lamps together, "
                 "from one end of the pair to the other, so it bypasses "
                 "both of them, not just the first."},
     ], "figure": None},
    {"id": "p8-02-h24", "band": "harder",
     "text": "A shop sign has fifty identical bulbs. The owner wants: all "
             "fifty equally bright; losing a few bulbs to barely affect "
             "the rest; and losing bulbs to be noticeable as a drop in "
             "total current. Assess whether one large parallel "
             "arrangement of all fifty meets every requirement.",
     "options": [
         {"text": "It fails the first two requirements entirely, since "
                  "parallel bulbs tend to be unevenly bright",
          "correct": False,
          "why": "Identical bulbs in parallel are equally bright, and "
                 "losing a few genuinely leaves the survivors "
                 "unaffected — those two requirements are met well."},
         {"text": "It meets all three requirements perfectly, with no "
                  "tension between any of them", "correct": False,
          "why": "There is a real practical tension: a tiny fractional "
                 "drop in the total current from losing one or two bulbs "
                 "out of fifty may go unnoticed without careful "
                 "measurement."},
         {"text": "It fails the third requirement completely, since a "
                  "parallel arrangement's total current does not "
                  "change "
                  "when a bulb fails", "correct": False,
          "why": "The total current does drop, by that bulb's own "
                 "share, when it fails — the issue is only how small and "
                 "hard to notice that drop is against the whole."},
         {"text": "It meets the first two well, but losing one or two "
                  "of fifty bulbs is too small a fraction of the total "
                  "current to notice easily", "correct": True},
     ], "figure": None},
    {"id": "p8-02-h25", "band": "harder",
     "text": "Two parallel branches, each rated safe up to 1 A, currently "
             "draw 0.60 A each. A third identical branch is added. Is the "
             "arrangement now safe for the two original branches, and "
             "for the shared main wire feeding all three?",
     "options": [
         {"text": "Each branch stays safely under its own 1 A rating, "
                  "but the shared main wire must now carry all three "
                  "together", "correct": True},
         {"text": "The two original branches are now over their rating, "
                  "since a third branch has been added to share the "
                  "supply with", "correct": False,
          "why": "A parallel branch's own current depends only on its "
                 "own resistance and the battery's push, not on how many "
                 "other branches exist — each stays at 0.60 A."},
         {"text": "Nothing about the main wire needs checking, since "
                  "individual branches are the sole thing that can be "
                  "overloaded",
          "correct": False,
          "why": "The main wire carries the SUM of every branch's "
                 "current, so it is exactly the part of the circuit that "
                 "needs checking when a branch is added."},
         {"text": "The new branch alone is unsafe, because being added "
                  "third makes it carry the other two branches' current "
                  "as well as its own", "correct": False,
          "why": "A new branch does not inherit the other branches' "
                 "current; it simply draws its own 0.60 A, same as the "
                 "others."},
     ], "figure": None},
    {"id": "p8-02-h26", "band": "harder",
     "text": "A teacher says: \"In parallel, adding a branch is free — "
             "nothing about the existing branches changes.\" Assess "
             "whether \"free\" is a fair word, considering the WHOLE "
             "circuit rather than just the individual branches.",
     "options": [
         {"text": "The word becomes fair merely once a fourth or later "
                  "branch is added to the arrangement, rather than "
                  "counting from the very first extra one",
          "correct": False,
          "why": "The same tension applies from the very first extra "
                 "branch onwards — the battery's total load rises with "
                 "every branch added, not just from the fourth."},
         {"text": "Fair for the existing branches, which are unaffected, "
                  "but not for the whole circuit, since the battery "
                  "now supplies more", "correct": True},
         {"text": "Completely fair, since nothing anywhere in the circuit "
                  "is affected in any way by adding one more parallel "
                  "branch", "correct": False,
          "why": "The battery and the shared main wire genuinely do "
                 "have to supply and carry more current once another "
                 "branch is added; something in the circuit does "
                 "change."},
         {"text": "Completely unfair, since adding any branch changes "
                  "the current in every existing branch", "correct": False,
          "why": "The existing branches themselves really are "
                 "unaffected — each still draws exactly what it drew "
                 "before, unchanged."},
     ], "figure": None},
    {"id": "p8-02-h27", "band": "harder",
     "text": "Two identical lamps sit correctly in parallel. The battery "
             "is swapped for one supplying twice the push, and each "
             "lamp's own current rises in direct proportion to the push "
             "across it. Compare the new total current to the original "
             "total current.",
     "options": [
         {"text": "The new total is four times the original, since both "
                  "branches double AND then add together again",
          "correct": False,
          "why": "Doubling each of two branch currents and then adding "
                 "them gives double the original total, not four times "
                 "it."},
         {"text": "The new total cannot be predicted without knowing "
                  "the lamps' exact resistance in ohms", "correct": False,
          "why": "You do not need the exact resistance to predict the "
                 "DIRECTION and rough scale of the change, given that "
                 "each branch's current is stated to rise in proportion "
                 "to the push."},
         {"text": "The new total is roughly double the original, since "
                  "each branch's own current roughly doubles too",
          "correct": True},
         {"text": "The new total stays the same, since parallel branches "
                  "draw a fixed current regardless of the push",
          "correct": False,
          "why": "A branch's current is not fixed — it rises with a "
                 "bigger push, which is exactly why doubling the push "
                 "roughly doubles each branch's current."},
     ], "figure": None},
    {"id": "p8-02-h28", "band": "harder",
     "text": "In a parallel arrangement, branch A draws 0.40 A and branch "
             "B draws 0.20 A, so the battery supplies 0.60 A. Branch A's "
             "own component is then also placed in series with a plain "
             "wire link within branch A itself — nothing else changes. "
             "In this course's convention, does the total battery current "
             "stay at 0.60 A?",
     "options": [
         {"text": "No — adding any extra component to a branch raises "
                  "that branch's own current", "correct": False,
          "why": "A wire link is treated as adding no resistance in "
                 "this course's convention, so it does not raise branch "
                 "A's current at all."},
         {"text": "No — branch A's current now has to be shared between "
                  "its component and the new wire link", "correct": False,
          "why": "Components in series share the SAME current, they do "
                 "not divide it between them; branch A's current stays "
                 "what it was."},
         {"text": "It cannot be judged without knowing the exact length "
                  "of the wire link added", "correct": False,
          "why": "In this course's convention every plain wire link is "
                 "treated as having no resistance regardless of its "
                 "length, so the length does not matter here."},
         {"text": "Yes — a wire link is treated as having no "
                  "resistance, so branch A's current stays unchanged",
          "correct": True},
     ], "figure": None},
    {"id": "p8-02-h29", "band": "harder",
     "text": "A series loop with three identical lamps gives an ammeter "
             "reading of 0.10 A. One lamp is removed and replaced with a "
             "plain wire link, so the loop stays complete but that lamp's "
             "resistance is gone. What happens to the ammeter reading and "
             "to the two remaining lamps?",
     "options": [
         {"text": "The reading rises above 0.10 A, and the two remaining "
                  "lamps become brighter than before", "correct": True},
         {"text": "The reading falls below 0.10 A, and the two remaining "
                  "lamps become dimmer", "correct": False,
          "why": "Removing a resisting lamp makes the one shared path "
                 "EASIER to get round, which raises the current rather "
                 "than lowering it."},
         {"text": "The reading stays at 0.10 A, since the loop is still "
                  "just as complete as before", "correct": False,
          "why": "Being complete is not the only thing that matters — "
                 "removing a lamp's resistance changes how hard the loop "
                 "is to push charge round, which changes the current."},
         {"text": "The reading rises, but the two remaining lamps stay "
                  "exactly as bright as before", "correct": False,
          "why": "A lamp's brightness depends on the current through "
                 "it, so a higher current through the two survivors "
                 "makes them brighter too, not unchanged."},
     ], "figure": None},
    {"id": "p8-02-h30", "band": "harder",
     "text": "Explain, in terms of the number of paths, why a single loop "
             "with no branching can never show two different ammeter "
             "readings at two different points, while a parallel "
             "arrangement can perfectly normally show three different "
             "readings across its three branches.",
     "options": [
         {"text": "Both arrangements show identical readings throughout, "
                  "provided every one of the components is wired "
                  "correctly and matches", "correct": False,
          "why": "That is only true of a single loop. Different branches "
                 "in parallel routinely carry different currents from "
                 "each other, by design."},
         {"text": "A single loop is one path, so the same current "
                  "appears everywhere in it; parallel branches are "
                  "separate, free to differ", "correct": True},
         {"text": "A single loop can show different readings too, but "
                  "just if its components are different from each "
                  "other", "correct": False,
          "why": "Whatever the components, one shared path carries one "
                 "current at every point of it — different components "
                 "change the SIZE of that one current, not create "
                 "several different ones."},
         {"text": "Parallel branches show different readings just when "
                  "they use different battery voltages", "correct": False,
          "why": "All the branches share the very same battery here; "
                 "their currents differ because of their own differing "
                 "resistances, not different voltages."},
     ], "figure": None},
]
