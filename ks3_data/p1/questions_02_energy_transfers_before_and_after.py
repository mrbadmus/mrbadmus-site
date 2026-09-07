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
            {"text": "It has filled thermal and sound stores in the casing "
                     "and the room",
             "correct": True},
            {"text": "It is still inside the hairdryer, waiting to be used",
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
            {"text": "The phone is full and the extra energy has nowhere to "
                     "go",
             "correct": False,
             "why": "It warms while charging as well, so this is not about "
                    "the battery being full."},
            {"text": "Warmth is being stored in the charger for later use",
             "correct": False,
             "why": "That thermal store simply drains into the room; nothing "
                    "gets it back."},
            {"text": "Some of the energy is filling thermal stores instead of "
                     "the phone's chemical store",
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
            {"text": "One tenth, into thermal stores in the kettle body, the "
                     "worktop and the air",
             "correct": True},
            {"text": "One tenth, destroyed as the element gets hot",
             "correct": False,
             "why": "The fraction is right but the fate is not: a hot element "
                    "is a thermal store, not a destruction."},
            {"text": "Nine tenths, because only 20 kJ did the useful job",
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
            {"text": "Because the rest is always somewhere, and naming it "
                     "finishes the account",
             "correct": True},
            {"text": "Because the totals never balance in a real experiment "
                     "anyway",
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
            {"text": "It destroys 60 J each second, which is why the bill "
                     "goes up",
             "correct": False,
             "why": "The bill measures energy supplied, not destroyed. "
                    "Nothing destroys any of it."},
            {"text": "It stores 60 J of light energy each second",
             "correct": False,
             "why": "Light is a pathway, and the bulb holds nothing — the "
                    "energy leaves as fast as it arrives."},
            {"text": "It transfers 60 J each second into light and thermal "
                     "stores in the room",
             "correct": True},
            {"text": "It loses 60 J each second to the wires around it",
             "correct": False,
             "why": "The wires carry energy TO the bulb; the room is where "
                    "almost all of it ends up."},
        ],
        "figure": None,
    },
]
