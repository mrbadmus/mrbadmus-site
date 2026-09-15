"""P1 lesson 02 — Energy transfers: before and after: twelve questions.

⊕ RUN 1's TWELVE WERE USED AS RAW MATERIAL, NOT ADOPTED (MRB-223).

Run 1 wrote twelve questions for this slot against a lesson it had invented,
believing Design had drawn nothing. She had. Re-read against
`docs/ks3/design-reference/p1/p1-02-energy-transfers-before-and-after.dc.html`
the science in them holds up — run 1's own provenance audit flags L2 as one
of the sets carrying no invented bench data, and that is confirmed here — but
most of them are aimed at the WRONG LESSON.

Her `p1-02` is the before-and-after TALLY: two columns, one total, and the
distinction between useful and wasted. Run 1's set is largely
which-store-is-it identification, which is `p1-01`'s job and is already
covered by `questions_01`. A set can be entirely correct and still leave the
lesson it sits on untested, and that is what these were.

    CHANGED — six of run 1's stems kept, every option set rewritten (6):
        e01  the falling conker, asked as a before-and-after
        e02  the gas hob, now naming the two columns explicitly
        s01  the torch cell, now asking what the TOTAL does
        s04  transferring versus storing — her second misconception quote
        h02  "the energy was used up" — her `ENER-11`, head-on
        h04  the account that balances only with a thermal store in it

    ⚠️ NONE of the six is unchanged, and none is recorded as "survived".
    Every option set was rewritten — to point at her lesson rather than at
    `p1-01`'s, to carry a `why` on every distractor, and to sit at the
    MRB-278 index this set needs. `h04` in particular had its options
    REORDERED after a first draft of this file put the answer at index 1
    while the docstring claimed index 3; the position audit caught it.

    NEW — her content had no question covering it at all (6):
        e03  the bulb's missing 57 J, on her own arithmetic
        e04  efficiency does not change the total
        s02  "wasted" is a judgement about intent — her heater/bulb pair
        s03  the balance from her hook — a flat battery weighs the same
        h01  the LED shopkeeper, her Rung 4 in question form
        h03  her winch, 500 J in for 350 J of gravitational store

    DROPPED — `p1-01` or later-unit material, not this lesson (6):
        run 1's e03 (a stretched spring), e04 (a cyclist pushing off),
        s02 (a runner and a banana), s03 (gravity versus a gravitational
        store), h01 (an astronaut on the Moon) and h03 (a bungee jumper).
        None is wrong; none belongs here.

⚠️ MISCONCEPTION IDS. Run 1 cited `ENER-10`. That id is real and still
correct where the question is about pathways-versus-stores, so `s04` keeps
it. The battery-leak belief this lesson confronts is `ENER-11`, minted here
and continuing C7's numbering — NOT `ENERGY-03`, which is what Design's
`NOTES-P1.md` §1 calls it. No `ENERGY-` id has ever existed and the
register's prefix table forbids opening one.

⚠️ The correct answer's position cycles 0, 1, 2, 3 through the twelve, so the
lesson contributes three of each index and no button beats reading (MRB-278).

⚠️ Every distractor is written to the correct answer's own length (MRB-177).
Where a stem quotes joules, the arithmetic is Design's own: her filament bulb
is 60 J in and about 3 J of light, and her winch is 500 J in for 350 J of
gravitational store.

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P1"
LESSON = "energy-transfers-before-and-after"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-02-e01",
        "band": "easier",
        "text": "A conker falls from a branch and speeds up. Which store is "
                "emptying as it falls?",
        "options": [
            {"text": "The gravitational store",
             "correct": True},
            {"text": "The kinetic store",
             "correct": False,
             "why": "The kinetic store is FILLING — that is what speeding up "
                    "means. Ask which store was full before it moved."},
            {"text": "The chemical store",
             "correct": False,
             "why": "Nothing is reacting. A conker falling is not burning "
                    "fuel or digesting food."},
            {"text": "The elastic store",
             "correct": False,
             "why": "Nothing is stretched or squashed on the way down. That "
                    "store fills when it lands, briefly."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e02",
        "band": "easier",
        "text": "A gas hob heats a pan of water. Which is the correct "
                "before-and-after pair?",
        "options": [
            {"text": "Thermal store of the gas empties, chemical store of "
                     "the water fills",
             "correct": False,
             "why": "The two are the wrong way round. Gas holds a CHEMICAL "
                    "store, and what fills in the water is thermal."},
            {"text": "Chemical store of the gas empties, thermal store of "
                     "the water fills",
             "correct": True},
            {"text": "Chemical store of the gas empties, kinetic store of "
                     "the water fills",
             "correct": False,
             "why": "The water is not being moved anywhere as a whole. What "
                    "rises is its temperature, which is a thermal store."},
            {"text": "Thermal store of the flame empties, thermal store of "
                     "the pan fills",
             "correct": False,
             "why": "This misses where the energy came from. The flame is "
                    "not a supply — the gas's chemical store is."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e03",
        "band": "easier",
        "text": "A filament bulb takes in 60 J each second and gives out "
                "about 3 J as light. What has happened to the other 57 J?",
        "options": [
            {"text": "It was destroyed by the resistance of the filament",
             "correct": False,
             "why": "Nothing destroys energy. Resistance moves it into a "
                    "thermal store; it does not remove it from the total."},
            {"text": "It was used up in making the bulb light up",
             "correct": False,
             "why": "“Making it work” is not a place energy can go. "
                    "Name the store it ended up in."},
            {"text": "It filled a thermal store in the bulb and the room",
             "correct": True},
            {"text": "It is still in the wires, waiting as electrical energy",
             "correct": False,
             "why": "Electrical is a pathway, not a store. Nothing sits in "
                    "the wires holding energy."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e04",
        "band": "easier",
        "text": "Two kettles boil the same water. One is more efficient than "
                "the other. What is true of the TOTAL energy before and "
                "after, for each kettle?",
        "options": [
            {"text": "The efficient kettle ends with more total energy",
             "correct": False,
             "why": "Efficiency changes where the energy ends up, never how "
                    "much of it there is."},
            {"text": "The wasteful kettle ends with less total energy",
             "correct": False,
             "why": "Nothing is missing from the wasteful one. More of its "
                    "energy simply ends up warming the room."},
            {"text": "Both end with less than they started with",
             "correct": False,
             "why": "Neither does. If your columns do not match you have "
                    "missed a store, usually a thermal one."},
            {"text": "Both end with exactly the total they started with",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-02-s01",
        "band": "standard",
        "text": "A torch is switched on and left until the cell goes flat. "
                "What has happened to the total energy over that time?",
        "options": [
            {"text": "It is unchanged — the same total is now in other "
                     "stores",
             "correct": True},
            {"text": "It has fallen to zero, because the cell is flat",
             "correct": False,
             "why": "A flat cell means one store is empty, not that the "
                    "total is. The room is very slightly warmer."},
            {"text": "It has fallen, because the light escaped from the room",
             "correct": False,
             "why": "Light is a pathway. It delivers energy to whatever it "
                    "lands on, which then holds it as a thermal store."},
            {"text": "It has fallen by the amount that was wasted as heat",
             "correct": False,
             "why": "Wasted energy is still in the total. It has moved into "
                    "a thermal store, not left the account."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s02",
        "band": "standard",
        "text": "An electric heater and a filament bulb both end up warming "
                "the room. Why is that wasted for the bulb but not for the "
                "heater?",
        "options": [
            {"text": "The heater makes warmth directly while the bulb "
                     "only makes light",
             "correct": False,
             "why": "The bulb warms the room too. Both end with energy in a "
                    "thermal store there — the physics is identical."},
            {"text": "Because “wasted” describes the job you wanted "
                     "done, not the physics",
             "correct": True},
            {"text": "The heater is more efficient, so a smaller share "
                     "of its energy is wasted",
             "correct": False,
             "why": "Efficiency is not the difference here. The heater's job "
                    "IS the warm room, so none of it is off-target."},
            {"text": "The bulb leaks energy into the room and the heater "
                     "does not leak any",
             "correct": False,
             "why": "Both put the same kind of energy in the same place. "
                    "Only your intention differs."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s03",
        "band": "standard",
        "text": "A power bank is weighed when fully charged and again when "
                "completely flat, on a balance accurate to a milligram. What "
                "does the reading do?",
        "options": [
            {"text": "It falls slightly, by the mass of the energy that left",
             "correct": False,
             "why": "Nothing was poured out to be weighed. The chemicals "
                    "inside were rearranged, and the same atoms are all "
                    "still in there."},
            {"text": "It rises slightly, because the chemicals have "
                     "rearranged",
             "correct": False,
             "why": "Rearranging the chemicals does not add anything. The "
                    "same atoms are present throughout."},
            {"text": "It does not change at all",
             "correct": True},
            {"text": "It falls by a few grams, too little to notice by hand",
             "correct": False,
             "why": "A balance reading to a milligram would find a few "
                    "grams easily. Nothing of that size left the power "
                    "bank."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s04",
        "band": "standard",
        "text": "Which of these is a way of TRANSFERRING energy rather than "
                "a store that holds it?",
        "options": [
            {"text": "The thermal store of a mug of tea",
             "correct": False,
             "why": "That is a store. Leave the mug overnight and it still "
                    "holds energy, just less of it."},
            {"text": "The chemical store of a biscuit",
             "correct": False,
             "why": "That is a store. A biscuit in a tin still holds it a "
                    "year later."},
            {"text": "The elastic store of a drawn bow",
             "correct": False,
             "why": "That is a store. Hold the bow drawn and the energy "
                    "stays exactly where it is."},
            {"text": "An electric current in a wire",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-02-h01",
        "band": "harder",
        "text": "A shop replaces its filament bulbs with LEDs and finds the "
                "winter heating bill rises slightly. What is the best "
                "explanation?",
        "options": [
            {"text": "The old bulbs had been doing part of the heating, "
                     "whether or not anyone intended it",
             "correct": True},
            {"text": "LEDs draw energy away from the heating system, so "
                     "it has less of its own to use",
             "correct": False,
             "why": "They do not interact with the heating at all. They "
                    "simply stop supplying the warmth the bulbs did."},
            {"text": "LEDs are less efficient than the filament bulbs "
                     "were at making the room warm",
             "correct": False,
             "why": "True in a sense, but backwards as an explanation — "
                    "warming the room was never the bulbs' job."},
            {"text": "The shop is using more total energy than it did "
                     "when the filament bulbs were in",
             "correct": False,
             "why": "It is using far less overall. Only the heating system's "
                    "share of it has gone up."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h02",
        "band": "harder",
        "text": "A car brakes from 30 mph to a stop. A student says "
                "“the energy was used up by the brakes”. What is "
                "wrong with that?",
        "options": [
            {"text": "Nothing — braking uses energy up, and that is what "
                     "brakes are for",
             "correct": False,
             "why": "It is the belief this lesson exists to correct. Nothing "
                    "uses energy up, ever."},
            {"text": "Nothing is used up — it filled a thermal store in the "
                     "discs, tyres and air",
             "correct": True},
            {"text": "The energy went into the road surface rather than "
                     "into the brakes",
             "correct": False,
             "why": "Some does, but the error is the phrase “used "
                    "up”, not which object got it."},
            {"text": "The kinetic store was never full, so there was "
                     "nothing there to be used",
             "correct": False,
             "why": "It was full — the car was moving. The question is where "
                    "that went, not whether it existed."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h03",
        "band": "harder",
        "text": "An electric winch uses 500 J to lift a crate, and the crate "
                "gains 350 J in its gravitational store. What is the correct "
                "account of the other 150 J?",
        "options": [
            {"text": "It was lost to inefficiency in the motor",
             "correct": False,
             "why": "“Lost” is the word to avoid. It is somewhere "
                    "specific and a thermometer would find it."},
            {"text": "It never entered the system, because the winch only "
                     "drew 350 J",
             "correct": False,
             "why": "The winch drew all 500 J. The question is where the "
                    "remainder ended up."},
            {"text": "It filled thermal stores in the motor, gearbox, cable "
                     "and air",
             "correct": True},
            {"text": "It was converted into the electrical energy that ran "
                     "the motor",
             "correct": False,
             "why": "Electrical is the pathway that brought the energy in, "
                    "not a store the leftovers sit in."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h04",
        "band": "harder",
        "text": "Why does an energy account for a falling conker only "
                "balance if you include a thermal store?",
        "options": [
            {"text": "Because the gravitational store was never quite full "
                     "at the top",
             "correct": False,
             "why": "It was full. The shortfall appears on the way down, not "
                    "at the start."},
            {"text": "Because some energy is destroyed by the air as the "
                     "conker passes through it",
             "correct": False,
             "why": "Air cannot destroy energy. It receives some, which is "
                    "why the account needs that column."},
            {"text": "Because the kinetic store gains more than the "
                     "gravitational store loses",
             "correct": False,
             "why": "It gains LESS. If it gained more the total would have "
                    "risen, which is equally impossible."},
            {"text": "Because air resistance moves some of it into the air "
                     "and the conker as it falls",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p1-02-e05",
        "band": "easier",
        "text": "What is meant by wasted energy?",
        "options": [
            {"text": "Energy that has been destroyed by the device",
             "correct": False,
             "why": "Nothing destroys energy. Wasted energy is still there, "
                    "just spread out where it is no use."},
            {"text": "Energy that ends up in a store you did not want filled",
             "correct": True},
            {"text": "Energy that was never supplied in the first place",
             "correct": False,
             "why": "It was supplied and it was transferred; it simply "
                    "arrived in the wrong store."},
            {"text": "Energy that leaks out before the device is switched on",
             "correct": False,
             "why": "Waste happens during the transfer, not before anything "
                    "has started."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e06",
        "band": "easier",
        "text": "An electric drill takes in 200 J and 150 J ends up doing the "
                "drilling. How much is wasted?",
        "options": [
            {"text": "350 J", "correct": False,
             "why": "That adds the two. The useful part is included in the "
                    "200 J, not on top of it."},
            {"text": "150 J", "correct": False,
             "why": "That is the useful part. The waste is what is left of "
                    "the 200 J."},
            {"text": "50 J", "correct": True},
            {"text": "0 J, because energy cannot be lost", "correct": False,
             "why": "Energy is not lost, but 50 J of it went somewhere other "
                    "than the drilling."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e07",
        "band": "easier",
        "text": "In an energy account, what is meant by the surroundings?",
        "options": [
            {"text": "Everything around the device — the air, the bench, the "
                     "room",
             "correct": True},
            {"text": "The wires and switches that supply the device",
             "correct": False,
             "why": "Those are part of the device's own circuit, not the "
                    "space around it."},
            {"text": "The place where energy goes when it is destroyed",
             "correct": False,
             "why": "Energy is never destroyed. The surroundings are where "
                    "wasted energy genuinely ends up."},
            {"text": "Any store that has been completely emptied",
             "correct": False,
             "why": "An empty store is a store. The surroundings are the "
                    "things around the device."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p1-02-s05",
        "band": "standard",
        "text": "A hairdryer takes in 1800 J each second. About 1500 J warms "
                "the air and 200 J turns the fan. What has happened to the "
                "other 100 J?",
        "options": [
            {"text": "It has been destroyed inside the motor",
             "correct": False,
             "why": "Nothing destroys energy. Every joule can be found "
                    "somewhere in the account."},
            {"text": "It was never supplied, so the total is really 1700 J",
             "correct": False,
             "why": "The 1800 J was measured going in, so the account has to "
                    "explain all of it."},
            {"text": "It has filled thermal and sound stores in the casing",
             "correct": True},
            {"text": "It is still inside the hairdryer somewhere, waiting to "
                     "be used",
             "correct": False,
             "why": "Nothing in a hairdryer stores energy for later; it "
                    "leaves as fast as it arrives."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s06",
        "band": "standard",
        "text": "A phone charger feels warm while it is charging. What does "
                "that tell you?",
        "options": [
            {"text": "The charger is faulty and should be replaced",
             "correct": False,
             "why": "Every charger warms a little. Some waste is normal, not "
                    "a fault."},
            {"text": "The phone battery is already full, so the extra energy "
                     "has nowhere to go",
             "correct": False,
             "why": "It warms while charging as well, so this is not about "
                    "the battery being full."},
            {"text": "Warmth is being stored in the charger for later use",
             "correct": False,
             "why": "That thermal store simply drains into the room; nothing "
                    "gets it back."},
            {"text": "Some energy is filling thermal stores, not the phone's "
                     "store",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s07",
        "band": "standard",
        "text": "A motor uses 8000 J to raise a lift, and the lift's "
                "gravitational store gains 6000 J. Which account is right?",
        "options": [
            {"text": "6000 J useful, and 2000 J into thermal stores in the "
                     "motor and cable",
             "correct": True},
            {"text": "6000 J useful, and 2000 J destroyed by friction in "
                     "the cable",
             "correct": False,
             "why": "Friction moves energy into thermal stores; it never "
                    "destroys any of it."},
            {"text": "8000 J useful, because all of it went into lifting",
             "correct": False,
             "why": "Only 6000 J reached the lift's gravitational store — the "
                    "measurement says so."},
            {"text": "2000 J useful, and 6000 J wasted in the motor",
             "correct": False,
             "why": "The two figures are the wrong way round: the lift gained "
                    "the 6000 J."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p1-02-h05",
        "band": "harder",
        "text": "A kettle takes in 200 kJ and 180 kJ ends up in the water. "
                "What fraction is wasted, and where has it gone?",
        "options": [
            {"text": "One tenth, into thermal stores in the kettle, worktop "
                     "and air",
             "correct": True},
            {"text": "One tenth, destroyed as the element gets hot",
             "correct": False,
             "why": "The fraction is right but the fate is not: a hot element "
                    "is a thermal store, not a destruction."},
            {"text": "Nine tenths wasted, because only 20 kJ actually did the "
                     "useful job",
             "correct": False,
             "why": "The two figures are swapped: 180 kJ of the 200 kJ "
                    "reached the water."},
            {"text": "None of it, because the water ends up hot either way",
             "correct": False,
             "why": "Only 180 kJ reached the water, so 20 kJ went elsewhere "
                    "and is wasted."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h06",
        "band": "harder",
        "text": "Why can an energy account never be finished with the words "
                "and the rest was lost?",
        "options": [
            {"text": "Because losing energy is only allowed in a closed "
                     "system",
             "correct": False,
             "why": "A closed system is where it is easiest to track. It is "
                    "not a place where loss becomes allowed."},
            {"text": "Because the rest is always somewhere and can be named",
             "correct": True},
            {"text": "Because the totals never quite balance in a real "
                     "experiment anyway",
             "correct": False,
             "why": "They balance every time, once the thermal stores in the "
                    "surroundings are included."},
            {"text": "Because energy is destroyed too slowly to write down",
             "correct": False,
             "why": "Energy is not destroyed at any speed; that is what "
                    "conservation says."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h07",
        "band": "harder",
        "text": "A student writes that a 60 W bulb uses up 60 J each second. "
                "Which rewrite is correct?",
        "options": [
            {"text": "It destroys 60 J each second, which is why the "
                     "electricity bill goes up",
             "correct": False,
             "why": "The bill measures energy supplied, not destroyed. "
                    "Nothing destroys any of it."},
            {"text": "It stores 60 J of light energy each second",
             "correct": False,
             "why": "Light is a pathway, and the bulb holds nothing — the "
                    "energy leaves as fast as it arrives."},
            {"text": "It transfers 60 J each second into light and thermal "
                     "stores",
             "correct": True},
            {"text": "It loses 60 J each second to the wires around it",
             "correct": False,
             "why": "The wires carry energy TO the bulb; the room is where "
                    "almost all of it ends up."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ──────────────────────────────────
    {
        "id": "p1-02-e08",
        "band": "easier",
        "text": "What is meant by useful energy?",
        "options": [
            {"text": "The part that ends up doing the job you wanted done",
             "correct": True},
            {"text": "The part that is left over once the device has finished",
             "correct": False,
             "why": "What is left over is the wasted part, filling stores you "
                    "did not want filled."},
            {"text": "The part the device manages to keep back for next time",
             "correct": False,
             "why": "A device keeps nothing for later. Everything supplied to "
                    "it leaves it again."},
            {"text": "The part you can see or hear while the device works",
             "correct": False,
             "why": "Being noticeable does not make energy useful. The noise "
                    "a drill makes is waste."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e09",
        "band": "easier",
        "text": "To describe a transfer properly, what must you name?",
        "options": [
            {"text": "The device it happened in, the time it took and the "
                     "joules involved",
             "correct": False,
             "why": "Those describe the event, but they never say which "
                    "stores changed."},
            {"text": "The store that empties, the stores that fill, and the "
                     "pathway",
             "correct": True},
            {"text": "The store that empties, and nothing more than that",
             "correct": False,
             "why": "Energy always arrives somewhere. A description that "
                    "stops halfway leaves joules unaccounted for."},
            {"text": "The pathway on its own, since that is what carries it",
             "correct": False,
             "why": "A pathway with no stores named says nothing about where "
                    "the energy started or finished."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e10",
        "band": "easier",
        "text": "A toaster is supplied with 500 J and 380 J of that browns "
                "the bread. State the energy wasted.",
        "options": [
            {"text": "880 J",
             "correct": False,
             "why": "That adds the two figures. The 380 J is part of the "
                    "500 J, not extra to it."},
            {"text": "380 J",
             "correct": False,
             "why": "That is the useful part. The waste is what is left of "
                    "the 500 J."},
            {"text": "120 J",
             "correct": True},
            {"text": "0 J, because energy is never destroyed",
             "correct": False,
             "why": "Nothing is destroyed, but 120 J ended up somewhere other "
                    "than the bread."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e11",
        "band": "easier",
        "text": "A microwave oven is supplied with 1200 J and 900 J of it "
                "warms the food. State the useful energy.",
        "options": [
            {"text": "2100 J",
             "correct": False,
             "why": "That adds the two figures. The useful part is included "
                    "in the 1200 J already."},
            {"text": "1200 J",
             "correct": False,
             "why": "That is everything supplied, rather than the part that "
                    "reached the food."},
            {"text": "300 J",
             "correct": False,
             "why": "That is the wasted part — the share that did not warm "
                    "the food at all."},
            {"text": "900 J",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e12",
        "band": "easier",
        "text": "Where does wasted energy almost always end up?",
        "options": [
            {"text": "In thermal stores in the surroundings",
             "correct": True},
            {"text": "In a chemical store inside the device",
             "correct": False,
             "why": "Nothing in a device refills its own chemical store from "
                    "its waste."},
            {"text": "Nowhere, since it is destroyed as the device runs",
             "correct": False,
             "why": "Nothing destroys energy. Wasted energy is still there, "
                    "spread too thinly to use."},
            {"text": "Back in the supply, ready to be used again later",
             "correct": False,
             "why": "It does not return. A warm room pushes nothing back down "
                    "the cable."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e13",
        "band": "easier",
        "text": "A footballer kicks a stationary ball. Which pair is right?",
        "options": [
            {"text": "Kinetic store of the player empties, elastic store of "
                     "the ball fills",
             "correct": False,
             "why": "The player's supply is chemical, and the ball ends up "
                    "flying rather than squashed."},
            {"text": "Chemical store of the player empties, kinetic store of "
                     "the ball fills",
             "correct": True},
            {"text": "Elastic store of the boot empties, chemical store of "
                     "the ball fills",
             "correct": False,
             "why": "A boot is not a loaded spring, and nothing in the ball "
                    "is being made or rearranged."},
            {"text": "Gravitational store of the ball empties, kinetic store "
                     "of the ball fills",
             "correct": False,
             "why": "The ball starts on the ground, so there is no height for "
                    "it to lose."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e14",
        "band": "easier",
        "text": "A wind turbine turns and supplies a house. Which store is "
                "emptying?",
        "options": [
            {"text": "The chemical store of the turbine",
             "correct": False,
             "why": "Nothing in a turbine reacts or burns. It is the same "
                    "machine before and after."},
            {"text": "The gravitational store of the blades",
             "correct": False,
             "why": "The blades go round rather than down, ending at the "
                    "height they started."},
            {"text": "The kinetic store of the moving air",
             "correct": True},
            {"text": "The thermal store of the air around it",
             "correct": False,
             "why": "The blades do not cool the air. What the turbine takes "
                    "is the movement."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e15",
        "band": "easier",
        "text": "A solar panel on a roof charges a battery all afternoon. "
                "Which store is filling?",
        "options": [
            {"text": "The kinetic store of the battery",
             "correct": False,
             "why": "The battery sits still on a shelf; nothing about it is "
                    "moving anywhere."},
            {"text": "The elastic store of the panel",
             "correct": False,
             "why": "Nothing on the roof is stretched or squashed by "
                    "sunlight."},
            {"text": "The nuclear store of the battery",
             "correct": False,
             "why": "Nothing inside any nucleus in the battery changes as it "
                    "charges."},
            {"text": "The chemical store of the battery",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e16",
        "band": "easier",
        "text": "A car engine burns petrol and the car speeds up. Name the "
                "store that empties and the stores that fill.",
        "options": [
            {"text": "Chemical empties; kinetic and thermal stores fill",
             "correct": True},
            {"text": "Chemical empties; only the kinetic store fills",
             "correct": False,
             "why": "The engine, the exhaust and the brakes all end up warm, "
                    "so thermal stores fill as well."},
            {"text": "Kinetic empties; chemical and thermal stores fill",
             "correct": False,
             "why": "That is backwards. The fuel supplies the energy and the "
                    "movement is the result."},
            {"text": "Thermal empties; kinetic and chemical stores fill",
             "correct": False,
             "why": "The engine gets hotter as it runs, so its thermal store "
                    "fills rather than empties."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e17",
        "band": "easier",
        "text": "A battery-powered clock ticks for a whole year. Which store "
                "has been emptying?",
        "options": [
            {"text": "The elastic store of the hands",
             "correct": False,
             "why": "Nothing in the clock is stretched or squashed; a battery "
                    "clock has no spring."},
            {"text": "The chemical store of the cell",
             "correct": True},
            {"text": "The gravitational store of the hands",
             "correct": False,
             "why": "The hands go round and end each hour where they began, "
                    "so no height is lost."},
            {"text": "The kinetic store of the hands",
             "correct": False,
             "why": "The hands move because energy is supplied to them; their "
                    "movement is not the supply."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e18",
        "band": "easier",
        "text": "A hairdryer is used to dry hair. Is the warm air it makes "
                "useful or wasted?",
        "options": [
            {"text": "Wasted, because warm air is waste in every device",
             "correct": False,
             "why": "Whether warmth is waste depends on the job, and here "
                    "warming the air is the job."},
            {"text": "Wasted, because the hair only needs the air moving",
             "correct": False,
             "why": "The warmth does a large part of the drying; cold air "
                    "dries hair far more slowly."},
            {"text": "Useful, because warming the air is what dries the hair",
             "correct": True},
            {"text": "Neither, because the air is not a store at all",
             "correct": False,
             "why": "The air's thermal store is a real store, and it is what "
                    "the dryer fills."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e19",
        "band": "easier",
        "text": "A kettle's element warms the water around it. Which pathway "
                "carries the energy from the element to the water?",
        "options": [
            {"text": "An electric current, which carries on flowing through "
                     "the water",
             "correct": False,
             "why": "The current runs through the element, not through the "
                    "water around it."},
            {"text": "Light, which the glowing element gives out",
             "correct": False,
             "why": "A kettle element does not glow, and the water warms just "
                    "as well in a solid metal kettle."},
            {"text": "Sound, which the boiling water makes",
             "correct": False,
             "why": "The noise is a side effect. The water is warming long "
                    "before it makes any sound."},
            {"text": "Heating, as the hot element warms the water touching it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e20",
        "band": "easier",
        "text": "In a tally, what do the useful energy and the wasted energy "
                "add up to?",
        "options": [
            {"text": "The total energy supplied to the device",
             "correct": True},
            {"text": "The useful energy, since waste does not count",
             "correct": False,
             "why": "Waste is real energy in a real store, and every joule of "
                    "it belongs in the tally."},
            {"text": "Exactly one hundred joules, whatever the device is",
             "correct": False,
             "why": "The total is whatever was supplied, and different "
                    "devices are supplied with different amounts."},
            {"text": "Less than the total, since some is destroyed on the way",
             "correct": False,
             "why": "Nothing is destroyed, so nothing is ever missing from "
                    "the two columns."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e21",
        "band": "easier",
        "text": "A laptop charger is warm to the touch while it works. Is "
                "that warmth useful or wasted?",
        "options": [
            {"text": "Useful, because a warm charger works faster",
             "correct": False,
             "why": "Warmth does not speed up charging. If anything it makes "
                    "the job harder."},
            {"text": "Wasted, because you were paying to fill the battery",
             "correct": True},
            {"text": "Useful, because the warmth pushes energy into the cell",
             "correct": False,
             "why": "The current carries the energy in. The warmth is what "
                    "escapes on the way."},
            {"text": "Neither, because the warmth is too small to matter",
             "correct": False,
             "why": "Small does not stop it being waste. It is energy in a "
                    "store you did not want filled."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e22",
        "band": "easier",
        "text": "A lift carries people from the ground floor to the fifth. "
                "Which store fills?",
        "options": [
            {"text": "The kinetic store of the passengers",
             "correct": False,
             "why": "They step out at the same standstill they stepped in at, "
                    "so that store is empty at both ends."},
            {"text": "The elastic store of the lift cable",
             "correct": False,
             "why": "The cable stretches a little, but that is not where the "
                    "energy of a raised load goes."},
            {"text": "The gravitational store of the passengers",
             "correct": True},
            {"text": "The chemical store of the passengers",
             "correct": False,
             "why": "Riding in a lift changes nothing about the substances "
                    "inside anybody."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e23",
        "band": "easier",
        "text": "A device is switched on at the wall. Which store did the "
                "energy come from before it reached the device?",
        "options": [
            {"text": "A store inside the wall socket itself",
             "correct": False,
             "why": "A socket holds nothing. It is one end of a route, not a "
                    "container."},
            {"text": "A store inside the cable between the two",
             "correct": False,
             "why": "A cable carries energy along it and holds none of it at "
                    "any point."},
            {"text": "A store inside the switch that was pressed to start it",
             "correct": False,
             "why": "A switch only opens and closes the route; it supplies "
                    "nothing at all."},
            {"text": "A chemical store, usually at a power station",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e24",
        "band": "easier",
        "text": "A transfer has taken place. What does that tell you about "
                "the energy?",
        "options": [
            {"text": "It has moved from one store to another",
             "correct": True},
            {"text": "It has changed into another kind",
             "correct": False,
             "why": "Nothing new is made. The same number simply appears "
                    "against a different store."},
            {"text": "It has been used up doing the job it was supplied for",
             "correct": False,
             "why": "Nothing is used up. Every joule can still be found "
                    "afterwards."},
            {"text": "It has been shared equally between the stores involved",
             "correct": False,
             "why": "There is no rule that the shares are equal; most "
                    "transfers are very uneven indeed."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e25",
        "band": "easier",
        "text": "A garden lamp is supplied with 10 J each second and gives "
                "out 4 J as light. State the energy wasted each second.",
        "options": [
            {"text": "14 J",
             "correct": False,
             "why": "That adds the two. The 4 J of light is part of the 10 J "
                    "supplied, not extra to it."},
            {"text": "6 J",
             "correct": True},
            {"text": "4 J",
             "correct": False,
             "why": "That is the light, which is the useful part rather than "
                    "the waste."},
            {"text": "10 J",
             "correct": False,
             "why": "That is everything supplied, and some of it did the job "
                    "it was meant to do."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e26",
        "band": "easier",
        "text": "A washing machine makes a loud noise while it spins. Is that "
                "noise useful or wasted?",
        "options": [
            {"text": "Useful, because the noise shows the machine is working",
             "correct": False,
             "why": "Showing that it works is not the job it was bought for; "
                    "the job is clean, dry clothes."},
            {"text": "Useful, because the shaking helps water leave the "
                     "clothes",
             "correct": False,
             "why": "The noise is a side effect of the spinning rather than "
                    "part of what removes the water."},
            {"text": "Wasted, because you were paying for clean, dry clothes",
             "correct": True},
            {"text": "Neither, because sound is not really energy at all",
             "correct": False,
             "why": "Sound carries energy, which is why a loud machine warms "
                    "its surroundings very slightly."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e27",
        "band": "easier",
        "text": "A weightlifter raises a heavy barbell above their head. Name "
                "the store that empties and the store that fills.",
        "options": [
            {"text": "The elastic store empties and the gravitational store "
                     "fills",
             "correct": False,
             "why": "Nothing is stretched or squashed. The lifter's supply is "
                    "chemical."},
            {"text": "The gravitational store empties and the kinetic store "
                     "fills",
             "correct": False,
             "why": "The barbell ends up higher than it started, so that "
                    "store fills rather than empties."},
            {"text": "The thermal store empties and the gravitational store "
                     "fills",
             "correct": False,
             "why": "The lifter gets warmer, so their thermal store fills as "
                    "well; it is not the supply."},
            {"text": "The chemical store empties and the gravitational store "
                     "fills",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e28",
        "band": "easier",
        "text": "A blender is run for ten seconds and the jug feels warm "
                "afterwards. What does the warmth show?",
        "options": [
            {"text": "Some of the energy filled a thermal store instead",
             "correct": True},
            {"text": "That the blender has been run for far too long",
             "correct": False,
             "why": "Ten seconds is nothing. Every blender warms a little "
                    "whenever it runs at all."},
            {"text": "That energy in the jug was destroyed by friction",
             "correct": False,
             "why": "Friction fills thermal stores. It never removes energy "
                    "from the account."},
            {"text": "That the motor is faulty and needs to be replaced",
             "correct": False,
             "why": "Some warming is normal in any motor, and it is not a "
                    "sign of a fault."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e29",
        "band": "easier",
        "text": "Which column of a tally does the energy that did the job you "
                "wanted go in?",
        "options": [
            {"text": "The wasted column",
             "correct": False,
             "why": "Devices do waste some energy, but the part that did the "
                    "job you wanted is the useful part."},
            {"text": "The useful column",
             "correct": True},
            {"text": "Neither column",
             "correct": False,
             "why": "Nothing is used up. The energy that did the job is still "
                    "in a store you can name."},
            {"text": "Both columns",
             "correct": False,
             "why": "Counting the same joules twice over would make the after "
                    "column bigger than the before column."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e30",
        "band": "easier",
        "text": "What is meant by the efficiency of a device, in plain words?",
        "options": [
            {"text": "How quickly it does the job it was chosen for",
             "correct": False,
             "why": "That is about speed, and a slow device can still waste "
                    "very little indeed."},
            {"text": "How much energy it uses up over the whole time it is "
                     "working",
             "correct": False,
             "why": "Nothing is used up, and a device supplied with more is "
                    "not automatically worse at its job."},
            {"text": "The share of the energy supplied that does the job",
             "correct": True},
            {"text": "How long it lasts before it has to be replaced",
             "correct": False,
             "why": "That is about how well it is built, not about where its "
                    "energy ends up."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ────────────────────────────────
    {
        "id": "p1-02-s08",
        "band": "standard",
        "text": "A petrol car turns about a quarter of its fuel's chemical "
                "store into movement. Account for the rest.",
        "options": [
            {"text": "It fills thermal stores in the engine, exhaust and air",
             "correct": True},
            {"text": "It is destroyed by the friction inside the engine",
             "correct": False,
             "why": "Friction never destroys energy; it moves it into thermal "
                    "stores you can measure."},
            {"text": "It stays in the tank as fuel that was not needed",
             "correct": False,
             "why": "The tank empties as the car drives, so all of that fuel "
                    "really was spent."},
            {"text": "It never entered the car, since only a quarter was "
                     "supplied",
             "correct": False,
             "why": "The whole tank's chemical store empties, so all of it "
                    "has to be accounted for."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s09",
        "band": "standard",
        "text": "A student says a very efficient device wastes nothing at "
                "all. What is wrong with that?",
        "options": [
            {"text": "Nothing: an efficient device really does waste nothing",
             "correct": False,
             "why": "Every real device fills some thermal store in its "
                    "surroundings, however good it is."},
            {"text": "Every real device always warms its surroundings a "
                     "little",
             "correct": True},
            {"text": "Efficient devices waste more, because they work harder",
             "correct": False,
             "why": "Working harder is not what decides it. An efficient "
                    "device wastes a smaller share."},
            {"text": "Nothing can be efficient, since energy is destroyed",
             "correct": False,
             "why": "Energy is never destroyed, and plenty of devices do "
                    "their job very well."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s10",
        "band": "standard",
        "text": "Why is a kettle one of the best devices there is at doing "
                "its job?",
        "options": [
            {"text": "Because it works faster than almost any other appliance",
             "correct": False,
             "why": "Speed is not the same as waste. A slow kettle can still "
                    "put nearly everything into the water."},
            {"text": "Because such a very small amount of energy is ever "
                     "supplied to it in the first place",
             "correct": False,
             "why": "A kettle is supplied with a great deal. What matters is "
                    "where that energy ends up."},
            {"text": "Because the job wanted is thermal, and what escapes is "
                     "thermal too",
             "correct": True},
            {"text": "Because it is switched off before it can waste anything",
             "correct": False,
             "why": "It wastes while it runs, and switching off only ends the "
                    "transfer."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s11",
        "band": "standard",
        "text": "A fridge motor makes the kitchen slightly warmer while it "
                "runs. Is that warmth useful or wasted?",
        "options": [
            {"text": "Useful, because a warm kitchen helps the food keep",
             "correct": False,
             "why": "Warmth is the opposite of what a fridge was bought to "
                    "do."},
            {"text": "Neither, because the warmth is not really energy",
             "correct": False,
             "why": "A warmer kitchen is a thermal store filling, and that is "
                    "energy."},
            {"text": "Useful, because the warmth is what drives the motor "
                     "round",
             "correct": False,
             "why": "The current drives the motor; the warmth is what escapes "
                    "as it turns."},
            {"text": "Wasted, because you were paying to keep the food cold",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s12",
        "band": "standard",
        "text": "A hand dryer warms the washroom as well as drying hands. "
                "How should that warmth be counted?",
        "options": [
            {"text": "As waste, because the job you wanted was dry hands",
             "correct": True},
            {"text": "As useful, because a warm washroom is pleasant",
             "correct": False,
             "why": "Being pleasant is not the job the dryer was installed to "
                    "do."},
            {"text": "As neither, since the room would have warmed anyway",
             "correct": False,
             "why": "The room is warmer because the dryer ran, so those "
                    "joules belong in the tally."},
            {"text": "As waste, because all energy leaving a device is waste",
             "correct": False,
             "why": "The energy that dried the hands also left the device, "
                    "and that part was useful."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s13",
        "band": "standard",
        "text": "A firework rocket is lit, rises high and then bangs. "
                "Describe the main changes in stores.",
        "options": [
            {"text": "Gravitational empties; kinetic and thermal stores fill "
                     "as it climbs",
             "correct": False,
             "why": "The rocket climbs, so its gravitational store fills "
                    "rather than empties."},
            {"text": "Chemical empties; gravitational, kinetic and thermal "
                     "fill",
             "correct": True},
            {"text": "Kinetic empties; chemical and gravitational stores fill",
             "correct": False,
             "why": "The powder supplies the energy, so the chemical store "
                    "empties rather than fills."},
            {"text": "Thermal empties; chemical and gravitational stores fill",
             "correct": False,
             "why": "The rocket and the air both end up warmer, so thermal "
                    "stores fill."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s14",
        "band": "standard",
        "text": "An electric scooter is supplied with 4000 J and 3000 J ends "
                "up in its kinetic store. What fraction is wasted?",
        "options": [
            {"text": "Three quarters, because only 1000 J did the job",
             "correct": False,
             "why": "The two figures are the wrong way round; 3000 J of the "
                    "4000 J did the job."},
            {"text": "None of it at all, because the scooter really did move "
                     "in the end",
             "correct": False,
             "why": "Moving in the end does not mean every joule helped; "
                    "1000 J went elsewhere."},
            {"text": "A quarter, filling thermal stores in the motor and "
                     "tyres",
             "correct": True},
            {"text": "A quarter, destroyed by friction in the wheel bearings",
             "correct": False,
             "why": "The fraction is right but the fate is not; friction "
                    "fills thermal stores."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s15",
        "band": "standard",
        "text": "A child slides down a playground slide and arrives at the "
                "bottom warm. Give the full account.",
        "options": [
            {"text": "Gravitational empties and kinetic fills, and nothing "
                     "else at all",
             "correct": False,
             "why": "The warmth shows a thermal store filling too, so the "
                    "account is not finished."},
            {"text": "Kinetic empties, and gravitational and thermal stores "
                     "fill",
             "correct": False,
             "why": "The child starts at the top and ends at the bottom, so "
                    "height is what is lost."},
            {"text": "Chemical empties, and kinetic and thermal stores fill",
             "correct": False,
             "why": "The child is not pushing; the slide works just as well "
                    "sitting still at the top."},
            {"text": "Gravitational empties, and kinetic and thermal fill",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s16",
        "band": "standard",
        "text": "A student's tally for a drill shows 300 J supplied and 250 J "
                "accounted for afterwards. What has gone wrong?",
        "options": [
            {"text": "A store has been missed, almost always a thermal one",
             "correct": True},
            {"text": "Fifty joules were destroyed inside the drill",
             "correct": False,
             "why": "Nothing destroys energy, so no tally ever needs a "
                    "destroyed column."},
            {"text": "The drill was only supplied with 250 J after all",
             "correct": False,
             "why": "The 300 J was measured going in, so the account has to "
                    "explain all of it."},
            {"text": "Nothing: a tally rarely balances exactly in practice",
             "correct": False,
             "why": "A tally balances every time once every store has been "
                    "included."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s17",
        "band": "standard",
        "text": "Why do physicists call the warmth from a charger wasted "
                "rather than lost?",
        "options": [
            {"text": "Because such a small amount of waste is not worth a "
                     "stronger word than that",
             "correct": False,
             "why": "Size is not the point; even a large amount is still "
                    "somewhere you can point at."},
            {"text": "Because it is in a store you can point at, just not the "
                     "one you wanted",
             "correct": True},
            {"text": "Because it will find its way back to the charger later",
             "correct": False,
             "why": "It does not come back. A warm room pushes nothing back "
                    "down the cable."},
            {"text": "Because the charger was designed to make warmth as well",
             "correct": False,
             "why": "No charger is designed to warm a room; the warmth is a "
                    "side effect."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s18",
        "band": "standard",
        "text": "An electric heater turns nearly all the energy supplied to "
                "it into a warm room. Explain how that can be.",
        "options": [
            {"text": "Because a heater is supplied with far more energy than "
                     "other devices are",
             "correct": False,
             "why": "How much is supplied does not decide the share that does "
                    "the job."},
            {"text": "Because a heater has no moving parts to waste anything",
             "correct": False,
             "why": "A heater with a fan is nearly as good; the reason is "
                    "where its energy ends up."},
            {"text": "Because the job you wanted is where the waste would "
                     "have gone",
             "correct": True},
            {"text": "Because the room returns the energy to the heater as it "
                     "cools",
             "correct": False,
             "why": "The room sends nothing back; it passes the energy on "
                    "outside instead."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s19",
        "band": "standard",
        "text": "A drill's casing is warm after use. Which column of the "
                "tally does that warmth belong in, and why?",
        "options": [
            {"text": "The useful column, because the warmth helped the "
                     "drilling",
             "correct": False,
             "why": "The warmth did not cut the hole; the turning bit did "
                    "that."},
            {"text": "Neither column, because the warmth has left the drill",
             "correct": False,
             "why": "Leaving the drill does not remove it from the account; "
                    "it fills a store in the room."},
            {"text": "The useful column, because the energy was supplied on "
                     "purpose",
             "correct": False,
             "why": "Energy being supplied on purpose does not mean every "
                    "joule of it did the job."},
            {"text": "The wasted column, because drilling was the job",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s20",
        "band": "standard",
        "text": "A loudspeaker and a washing machine both make sound. Why is "
                "one useful and the other wasted?",
        "options": [
            {"text": "Because sound is the speaker's job and not the "
                     "machine's",
             "correct": True},
            {"text": "Because the speaker's sound is much louder than the "
                     "washing machine's",
             "correct": False,
             "why": "Loudness has nothing to do with it; a quiet speaker is "
                    "still doing its job."},
            {"text": "Because a washing machine's sound carries no energy",
             "correct": False,
             "why": "All sound carries energy, which is why both end up "
                    "warming the room slightly."},
            {"text": "Because only electrical devices make useful sound",
             "correct": False,
             "why": "Both are electrical devices, so that cannot be the "
                    "difference between them."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s21",
        "band": "standard",
        "text": "A student says wasted energy is the part that escapes from a "
                "device. What is the better description?",
        "options": [
            {"text": "It is the part that never really entered the device in "
                     "the first place",
             "correct": False,
             "why": "All of it entered; the tally starts with everything "
                    "supplied."},
            {"text": "It is the part that ended up in a store you did not "
                     "want filled",
             "correct": True},
            {"text": "It is the part the device could not hold on to",
             "correct": False,
             "why": "A device holds nothing. Everything supplied to it leaves "
                    "again, useful or not."},
            {"text": "It is the part that the device has destroyed",
             "correct": False,
             "why": "Nothing is destroyed, which is why the two columns "
                    "always balance."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s22",
        "band": "standard",
        "text": "A box is given an 80 J push and slides across a floor until "
                "it stops. Complete the account.",
        "options": [
            {"text": "80 J fills the kinetic store of the box and then simply "
                     "stays there for good",
             "correct": False,
             "why": "The box has stopped, so nothing is left in its kinetic "
                    "store at the end."},
            {"text": "80 J is used up by the friction of the floor",
             "correct": False,
             "why": "Friction is not a place. Name the store the energy ended "
                    "up in."},
            {"text": "80 J fills the kinetic store, then thermal stores in "
                     "the floor and box",
             "correct": True},
            {"text": "80 J is destroyed as the box slows to a stop",
             "correct": False,
             "why": "Nothing is destroyed; the floor and the box are very "
                    "slightly warmer."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s23",
        "band": "standard",
        "text": "A battery-powered fan is run in a sealed room until the cell "
                "is flat. What has happened to the room?",
        "options": [
            {"text": "It is exactly as it was, since the fan only moved air",
             "correct": False,
             "why": "The air was set moving and slowed again, and that "
                    "movement ended in thermal stores."},
            {"text": "It has lost energy, because the fan used some of it up",
             "correct": False,
             "why": "Nothing is used up, and nothing left a sealed room."},
            {"text": "It is cooler, because moving air always cools a room",
             "correct": False,
             "why": "Moving air feels cooler on skin, but the air itself ends "
                    "up slightly warmer."},
            {"text": "It is very slightly warmer, by the whole of the cell's "
                     "store",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s24",
        "band": "standard",
        "text": "A grill browns toast and also warms the kitchen. Which part "
                "is useful and which is wasted?",
        "options": [
            {"text": "Browning the toast is useful; warming the kitchen is "
                     "wasted",
             "correct": True},
            {"text": "Both are useful, because the kitchen needed warming",
             "correct": False,
             "why": "The job the grill was switched on for was the toast, not "
                    "the room."},
            {"text": "Both are wasted, because a grill is an inefficient "
                     "device",
             "correct": False,
             "why": "The part that browned the toast did exactly the job it "
                    "was chosen for."},
            {"text": "Warming the kitchen is useful; the toast is wasted",
             "correct": False,
             "why": "The two are the wrong way round; nobody switches a grill "
                    "on to heat a room."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s25",
        "band": "standard",
        "text": "An escalator carries shoppers upwards and its motor gets "
                "hot. Name the useful and the wasted stores.",
        "options": [
            {"text": "Kinetic useful; thermal wasted",
             "correct": False,
             "why": "The shoppers step off at a standstill, so their movement "
                    "is not what was bought."},
            {"text": "Gravitational useful; thermal wasted",
             "correct": True},
            {"text": "Thermal useful; the gravitational store wasted",
             "correct": False,
             "why": "The two are the wrong way round; nobody rides an "
                    "escalator to warm a motor."},
            {"text": "Chemical useful; thermal wasted",
             "correct": False,
             "why": "Nothing in the escalator fills a chemical store; its "
                    "supply is at the power station."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s26",
        "band": "standard",
        "text": "A kettle puts 90 J of every 100 J into the water, and a "
                "winch puts 70 J of every 100 J into the load. Which wastes "
                "the larger share, and by how much?",
        "options": [
            {"text": "The kettle, by twenty joules in every hundred",
             "correct": False,
             "why": "The kettle wastes ten in every hundred, which is the "
                    "smaller share of the two."},
            {"text": "Neither, because both waste exactly the same share",
             "correct": False,
             "why": "One wastes ten in every hundred and the other thirty, so "
                    "they are not the same."},
            {"text": "The winch, by twenty joules in every hundred",
             "correct": True},
            {"text": "The winch, by thirty joules in every hundred",
             "correct": False,
             "why": "Thirty is the winch's own waste, not the difference "
                    "between the two devices."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s27",
        "band": "standard",
        "text": "Two lamps run for one hour, one a 60 W filament bulb and one "
                "an 8 W LED. Which fills the room's thermal store more?",
        "options": [
            {"text": "The LED, because it is the more efficient of the two",
             "correct": False,
             "why": "Efficient means a larger share becomes light, and it "
                    "takes far less energy in altogether."},
            {"text": "Both the same, because both end up warming the room",
             "correct": False,
             "why": "Both do warm the room, but the filament bulb is supplied "
                    "with far more energy."},
            {"text": "Neither, because a lamp's energy leaves by the window",
             "correct": False,
             "why": "A closed room keeps it, and light landing on a wall "
                    "fills a thermal store there."},
            {"text": "The filament bulb, because far more is supplied to it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s28",
        "band": "standard",
        "text": "A student's account of a phone charging lists only the "
                "chemical store filling. What must be added?",
        "options": [
            {"text": "Thermal stores in the charger, the phone and the air",
             "correct": True},
            {"text": "An electrical store in the cable between the two",
             "correct": False,
             "why": "A cable holds nothing; a current is a pathway rather "
                    "than a store."},
            {"text": "A note that some of the energy has been destroyed",
             "correct": False,
             "why": "Nothing is destroyed, so no account ever needs that "
                    "line."},
            {"text": "Nothing: the chemical store is the only one that "
                     "changes",
             "correct": False,
             "why": "Both the charger and the phone end up warm, so thermal "
                    "stores change too."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s29",
        "band": "standard",
        "text": "Name the pathway in each of these: a kettle warming water, "
                "and a lamp lighting a wall.",
        "options": [
            {"text": "An electric current for both, since both are plugged in",
             "correct": False,
             "why": "The current gets energy to each device; the question is "
                    "what carries it onwards."},
            {"text": "Heating for the kettle, light for the lamp",
             "correct": True},
            {"text": "Light for the kettle, heating for the lamp",
             "correct": False,
             "why": "The two are the wrong way round; a kettle element does "
                    "not light the water."},
            {"text": "Sound for the kettle, heating for the lamp",
             "correct": False,
             "why": "A kettle is noisy, but the noise is not what warms the "
                    "water."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s30",
        "band": "standard",
        "text": "Why does a sprinter's tally show three quarters of the "
                "chemical store filling a thermal store?",
        "options": [
            {"text": "Because sprinting is so quick that most has no time to "
                     "be used",
             "correct": False,
             "why": "Time is not what decides it; a slow walk wastes a large "
                    "share as well."},
            {"text": "Because the chemical store was only a quarter full to "
                     "start with",
             "correct": False,
             "why": "The tally starts with the whole store that was spent, "
                    "not a part of it."},
            {"text": "Because a human body is a poor machine and a good "
                     "heater",
             "correct": True},
            {"text": "Because the missing three quarters is destroyed in the "
                     "muscles",
             "correct": False,
             "why": "Nothing is destroyed; it is exactly why a sprinter gets "
                    "hot and sweats."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ──────────────────────────────────
    {
        "id": "p1-02-h08",
        "band": "harder",
        "text": "Two torches hold identical cells, one with a filament bulb "
                "and one with an LED. Each is left on until its cell is flat. "
                "Which room ends up warmer?",
        "options": [
            {"text": "Both by the same amount, since the cells held the same "
                     "energy",
             "correct": True},
            {"text": "The filament torch's room, because filament bulbs waste "
                     "more",
             "correct": False,
             "why": "It wastes a bigger share at any instant, but it also "
                    "empties its cell far sooner."},
            {"text": "The LED torch's room, because it stays alight far "
                     "longer",
             "correct": False,
             "why": "Lasting longer adds no energy; both cells hold the same "
                    "amount to start with."},
            {"text": "Neither room warms at all, because the energy left as "
                     "light",
             "correct": False,
             "why": "Light that lands on a wall or a person fills a thermal "
                    "store there."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h09",
        "band": "harder",
        "text": "A tally for a vacuum cleaner balances only when one more "
                "thing is included. What is usually missing?",
        "options": [
            {"text": "The energy the cleaner kept back for the next time",
             "correct": False,
             "why": "A cleaner holds nothing over; everything supplied leaves "
                    "again while it runs."},
            {"text": "The sound it makes, which ends in thermal stores",
             "correct": True},
            {"text": "The energy destroyed in the motor windings",
             "correct": False,
             "why": "Nothing is destroyed, so no tally ever balances by "
                    "adding a destroyed column."},
            {"text": "The dust, which carries some of the energy away",
             "correct": False,
             "why": "The dust is matter being moved, not a store carrying the "
                    "missing joules off."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h10",
        "band": "harder",
        "text": "An electric car is called zero emission because nothing "
                "burns inside it. What does a full energy account show?",
        "options": [
            {"text": "Nothing burns anywhere, so the account starts at the "
                     "battery",
             "correct": False,
             "why": "The battery was filled from the mains, and the account "
                    "has to say what filled it."},
            {"text": "The car creates its own energy as the wheels go round",
             "correct": False,
             "why": "No car creates energy; a car only moves it between "
                    "stores."},
            {"text": "A chemical store often empties at the power station "
                     "instead",
             "correct": True},
            {"text": "No store empties at all, and only pathways are involved",
             "correct": False,
             "why": "A pathway always runs between two stores; an account "
                    "with no store in it is unfinished."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h11",
        "band": "harder",
        "text": "A student tallies a bouncing ball and finds the after column "
                "is smaller than the before column. What was forgotten?",
        "options": [
            {"text": "The gravitational store, which the ball regains on the "
                     "way up",
             "correct": False,
             "why": "That is already in the after column; the shortfall is "
                    "somewhere else entirely."},
            {"text": "The sound of the bounce, which accounts for nearly all "
                     "of it",
             "correct": False,
             "why": "The bounce is quiet; sound is a tiny part and cannot "
                    "explain the whole gap."},
            {"text": "Nothing: a little is lost each bounce",
             "correct": False,
             "why": "It loses height, not energy. Every joule is still "
                    "somewhere you can name."},
            {"text": "The thermal stores of the ball and the floor",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h12",
        "band": "harder",
        "text": "A student writes that a kettle converts electrical energy "
                "into heat energy. Rewrite it properly.",
        "options": [
            {"text": "A chemical store empties and the water's thermal store "
                     "fills",
             "correct": True},
            {"text": "An electrical store empties and a heat store fills in "
                     "the water",
             "correct": False,
             "why": "Neither of those is a store. Electrical is a pathway and "
                    "so is heating."},
            {"text": "A thermal store empties in the element and fills in the "
                     "water",
             "correct": False,
             "why": "The element's own thermal store fills as well, so "
                    "something else must supply both."},
            {"text": "The electrical energy is stored in the water as heat "
                     "energy",
             "correct": False,
             "why": "The water holds a thermal store; there is no such thing "
                    "as a store of heat energy."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h13",
        "band": "harder",
        "text": "A sprinter spends 400 J of chemical store and gains 100 J of "
                "kinetic store. Is it fair to call them inefficient?",
        "options": [
            {"text": "No, because the missing 300 J was destroyed, not "
                     "wasted",
             "correct": False,
             "why": "Nothing is destroyed; the 300 J warms the sprinter and "
                    "the air around them."},
            {"text": "Yes at the job of moving, though the warmth is no "
                     "failure of physics",
             "correct": True},
            {"text": "No, because a person cannot be measured like a machine",
             "correct": False,
             "why": "A person can be tallied exactly like any device, and the "
                    "columns still balance."},
            {"text": "Yes, because the 100 J was created out of nothing",
             "correct": False,
             "why": "No muscle creates energy; it comes from the chemical "
                    "store in food."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h14",
        "band": "harder",
        "text": "Where does the sound from a noisy appliance end up in the "
                "end?",
        "options": [
            {"text": "It keeps travelling outwards for ever, growing quieter",
             "correct": False,
             "why": "It dies away because the energy is absorbed, not because "
                    "it travels for ever."},
            {"text": "It is destroyed once the room becomes quiet again",
             "correct": False,
             "why": "Nothing destroys it; the room going quiet is the energy "
                    "arriving somewhere."},
            {"text": "In thermal stores in the walls, the air and the floor",
             "correct": True},
            {"text": "It returns to the appliance as an echo and is reused",
             "correct": False,
             "why": "Echoes carry energy away from the appliance, and nothing "
                    "collects them."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h15",
        "band": "harder",
        "text": "A crane lifts a load and then lowers it back to the ground. "
                "Over the whole cycle, what has the gravitational store "
                "gained?",
        "options": [
            {"text": "Everything the crane supplied, since the load went up "
                     "first",
             "correct": False,
             "why": "The load came back down, so the store that lifting "
                    "filled has emptied again."},
            {"text": "Half of what the crane supplied, since half the trip "
                     "was up",
             "correct": False,
             "why": "Time spent going up does not decide it; the load's "
                    "height is the same at the end."},
            {"text": "More than the crane supplied, because falling adds "
                     "energy",
             "correct": False,
             "why": "Nothing adds energy; falling only empties the store that "
                    "lifting filled."},
            {"text": "Nothing at all, and it is now in thermal stores",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h16",
        "band": "harder",
        "text": "A student says useful and wasted are properties of the "
                "energy itself. What is wrong with that?",
        "options": [
            {"text": "They only describe the job you wanted, not the joules",
             "correct": True},
            {"text": "Nothing: wasted energy really is a different kind of "
                     "energy",
             "correct": False,
             "why": "There is one kind of energy; the same joules are useful "
                    "in a heater and wasted in a bulb."},
            {"text": "They describe how much energy there is, not what kind",
             "correct": False,
             "why": "Neither word is about how much; both are about what the "
                    "energy ended up doing."},
            {"text": "They describe which pathway it travelled along",
             "correct": False,
             "why": "The same pathway delivers useful energy in one device "
                    "and waste in another."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h17",
        "band": "harder",
        "text": "A 60 W bulb is left on in a small sealed room with very "
                "thick insulation. What happens to the room?",
        "options": [
            {"text": "It stays at the same temperature, because light is not "
                     "warmth",
             "correct": False,
             "why": "Light landing on the walls fills their thermal store, "
                    "and that warms the room."},
            {"text": "It warms by the whole 60 J each second, light included",
             "correct": True},
            {"text": "It warms by 57 J each second and the light escapes",
             "correct": False,
             "why": "The room is sealed, so the light lands inside it and its "
                    "energy stays in the room."},
            {"text": "It cools slowly, because the bulb draws energy from the "
                     "air",
             "correct": False,
             "why": "A bulb supplies energy to the room and takes none out of "
                    "it at all."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h18",
        "band": "harder",
        "text": "A lift's motor is wired to act as a generator while the lift "
                "descends, sending energy back to the supply. Evaluate the "
                "claim that this makes the lift free to run.",
        "options": [
            {"text": "True, because the trip down returns all of the trip up",
             "correct": False,
             "why": "Some fills thermal stores in the motor and cable each "
                    "way, so not all of it returns."},
            {"text": "True, because a generator creates new energy as it "
                     "turns",
             "correct": False,
             "why": "No generator creates energy; it only moves it from one "
                    "store to another."},
            {"text": "False, because thermal stores are filled both ways",
             "correct": True},
            {"text": "False, because energy sent back to the supply is "
                     "destroyed",
             "correct": False,
             "why": "Nothing is destroyed; the returned energy is genuinely "
                    "available to be used again."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h19",
        "band": "harder",
        "text": "Why can a heater be described as wasting almost nothing "
                "while a filament bulb wastes most of what it takes?",
        "options": [
            {"text": "Because a heater is supplied with far less energy than "
                     "a bulb is",
             "correct": False,
             "why": "A heater is supplied with far more, and it still wastes "
                    "almost nothing."},
            {"text": "Because a bulb's energy leaves the room and a heater's "
                     "does not",
             "correct": False,
             "why": "Both end up in the room; the light lands on the walls "
                    "and warms them."},
            {"text": "Because a heater has no moving parts and a bulb has a "
                     "filament",
             "correct": False,
             "why": "Moving parts are not the difference; what matters is the "
                    "job each was chosen for."},
            {"text": "Because the same warm room is one's job and the other's "
                     "waste",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h20",
        "band": "harder",
        "text": "A rechargeable battery is charged and then run flat again. "
                "Compare what went in with what came out.",
        "options": [
            {"text": "Less always comes out than went in, and the difference "
                     "warmed it",
             "correct": True},
            {"text": "Exactly the same comes out as went in, in every cycle",
             "correct": False,
             "why": "Charging and discharging both warm the battery, so some "
                    "never comes back out."},
            {"text": "More comes out than went in, because the battery adds "
                     "its own",
             "correct": False,
             "why": "No battery adds energy; it only gives back what was put "
                    "into it."},
            {"text": "Nothing comes out, because the energy was used up",
             "correct": False,
             "why": "Plenty comes out, which is why the phone works at all."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h21",
        "band": "harder",
        "text": "A village hall is kept warm in winter by the computers left "
                "running in it. Explain that using a tally.",
        "options": [
            {"text": "The computers create warmth as well as doing their work",
             "correct": False,
             "why": "Nothing creates energy; the warmth is the energy "
                    "supplied, arriving where you can feel it."},
            {"text": "Everything supplied to them ends up in the hall's "
                     "thermal store",
             "correct": True},
            {"text": "Only the energy the computers waste reaches the hall",
             "correct": False,
             "why": "The useful part ends up warming the hall too, once the "
                    "work has been done."},
            {"text": "The computers return energy to the supply as they warm "
                     "the hall",
             "correct": False,
             "why": "Nothing goes back down the cable; the hall keeps every "
                    "joule of it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h22",
        "band": "harder",
        "text": "Why must an energy account for any device include the "
                "surroundings?",
        "options": [
            {"text": "Because the surroundings supply part of the energy it "
                     "uses",
             "correct": False,
             "why": "The surroundings receive energy; they do not supply the "
                    "device."},
            {"text": "Because the surroundings are where energy is destroyed",
             "correct": False,
             "why": "Nothing is destroyed anywhere, including in the "
                    "surroundings."},
            {"text": "Because the wasted energy always ends up there and is "
                     "counted",
             "correct": True},
            {"text": "Because no device works unless the room is warm enough",
             "correct": False,
             "why": "Devices work in cold rooms; the account is not about "
                    "what makes them run."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h23",
        "band": "harder",
        "text": "A student claims no device can ever put every joule into the "
                "job it was chosen for. Evaluate that.",
        "options": [
            {"text": "They are right, because every device loses a little "
                     "energy",
             "correct": False,
             "why": "No device loses any; the only question is where the "
                    "joules end up."},
            {"text": "They are right, because a perfect device would break "
                     "conservation",
             "correct": False,
             "why": "A perfect device breaks nothing; the totals balance "
                    "either way."},
            {"text": "They are right, because every device makes some noise",
             "correct": False,
             "why": "A silent device would still warm its surroundings, so "
                    "noise is not the reason."},
            {"text": "They are wrong: an electric heater's waste is its job",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h24",
        "band": "harder",
        "text": "An electric shower takes in 9000 J each second and 8500 J "
                "warms the water. Where is the rest, and why does the pipe "
                "feel warm?",
        "options": [
            {"text": "500 J fills thermal stores in the element and pipes",
             "correct": True},
            {"text": "500 J is destroyed by the resistance of the element",
             "correct": False,
             "why": "Resistance fills thermal stores; it removes nothing from "
                    "the account."},
            {"text": "500 J never arrived, so the shower draws only 8500 J",
             "correct": False,
             "why": "The 9000 J was measured going in, so all of it has to be "
                    "explained."},
            {"text": "500 J is stored in the pipe and returns to the water",
             "correct": False,
             "why": "A warm pipe passes its energy on to the room, not back "
                    "into the water."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h25",
        "band": "harder",
        "text": "A solar panel warms up in the sun as well as charging a "
                "battery. How should the warming be counted?",
        "options": [
            {"text": "As useful, because a warm panel charges faster than a "
                     "cold one",
             "correct": False,
             "why": "A hot panel actually charges slightly less well, and "
                    "warming was not the job."},
            {"text": "As waste, because the job wanted was the battery's "
                     "store",
             "correct": True},
            {"text": "As neither, because the Sun supplied it and not the "
                     "panel",
             "correct": False,
             "why": "Where the energy came from does not change which column "
                    "it lands in."},
            {"text": "As waste, because a panel that warms up must be faulty",
             "correct": False,
             "why": "Every panel warms in sunlight; it is normal rather than "
                    "a fault."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h26",
        "band": "harder",
        "text": "A student tallies a kettle and finds the after column is "
                "bigger than the before column. What must have happened?",
        "options": [
            {"text": "The kettle created some energy while it was boiling",
             "correct": False,
             "why": "No device creates energy, so that can never be the "
                    "explanation."},
            {"text": "The kettle drew extra energy from the warm kitchen air",
             "correct": False,
             "why": "The kitchen is cooler than the kettle, and the flow runs "
                    "the other way."},
            {"text": "Some energy has been counted twice in the after column",
             "correct": True},
            {"text": "Nothing: an after column is expected to be a bit bigger",
             "correct": False,
             "why": "The two columns match exactly once everything has been "
                    "counted once."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h27",
        "band": "harder",
        "text": "Four accounts of a phone charging are offered. Which one is "
                "complete?",
        "options": [
            {"text": "The phone's chemical store fills, and nothing else "
                     "changes",
             "correct": False,
             "why": "The charger and the phone both end up warm, and that has "
                    "to appear in the account."},
            {"text": "An electrical store empties in the mains and fills in "
                     "the phone",
             "correct": False,
             "why": "Electrical is a pathway, so neither end of that sentence "
                    "names a real store."},
            {"text": "A chemical store empties at the power station and is "
                     "destroyed",
             "correct": False,
             "why": "Nothing is destroyed; every joule can be named at the "
                    "end of the account."},
            {"text": "A chemical store empties, the phone's fills, and "
                     "thermal stores fill",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h28",
        "band": "harder",
        "text": "A hoist raises a load at a perfectly steady speed. Which "
                "stores change and which does not?",
        "options": [
            {"text": "Gravitational and thermal fill; kinetic does not change",
             "correct": True},
            {"text": "Kinetic and gravitational both fill, and nothing else "
                     "changes",
             "correct": False,
             "why": "The speed is steady, so the kinetic store is the same "
                    "throughout the lift."},
            {"text": "Only the gravitational store fills, since the speed is "
                     "steady",
             "correct": False,
             "why": "The motor and the cable end up warm, so thermal stores "
                    "fill as well."},
            {"text": "Gravitational fills and kinetic empties as it rises",
             "correct": False,
             "why": "The load is moving at the start as well as the end, at "
                    "the very same speed."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h29",
        "band": "harder",
        "text": "A pupil's tally for a slide shows the gravitational store "
                "emptying and the kinetic store filling by exactly the same "
                "amount. Why must that be wrong for a real slide?",
        "options": [
            {"text": "Because a real slide always takes more energy from a "
                     "child than it gives back",
             "correct": False,
             "why": "A slide gives nothing and takes nothing; it passes "
                    "energy between stores."},
            {"text": "Because rubbing fills thermal stores, so less arrives "
                     "as movement",
             "correct": True},
            {"text": "Because the child's own muscles add energy on the way "
                     "down",
             "correct": False,
             "why": "A child can slide down doing nothing at all and still "
                    "arrive moving."},
            {"text": "Because the two columns are never meant to match",
             "correct": False,
             "why": "The columns always match once every store is included; "
                    "that is the whole method."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h30",
        "band": "harder",
        "text": "Which change would make a device's wasted column smaller "
                "without changing the job it does?",
        "options": [
            {"text": "Running the device for a shorter time each day",
             "correct": False,
             "why": "That lowers both columns together and leaves the shares "
                    "exactly as they were."},
            {"text": "Supplying the device with more energy each second",
             "correct": False,
             "why": "More going in means more of both, and the wasted share "
                    "does not fall at all."},
            {"text": "Fitting better bearings so less of it warms the motor",
             "correct": True},
            {"text": "Switching the device off before it finishes the job",
             "correct": False,
             "why": "The job is then not done, which is exactly what the "
                    "question rules out."},
        ],
        "figure": None,
    },
]
