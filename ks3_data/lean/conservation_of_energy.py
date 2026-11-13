# -*- coding: utf-8 -*-
"""Conservation of energy, in the lean shape. Spec table: docs/lessons/wave1/ks3-conservation-of-energy.md."""

LESSON = {
    "slug": "conservation-of-energy",
    "start": {
        "setup": "A pendulum swings a little lower each time. After a few hundred swings, it stops.",
        "question": "If you had to guess, is anything in the room now a tiny bit warmer?",
        "options": [
            ("Yes, a tiny bit warmer", "Yes. The air and the pivot are a tiny bit warmer. The swing's energy went there."),
            ("No, nothing has changed", "Yes. The air and the pivot are a tiny bit warmer. The swing's energy went there."),
        ],
        "answer": 0,
    },
    "words": ["conservation of energy", "closed system", "dissipated", "friction"],
    "word_defs": {
        "conservation of energy": "Energy cannot be created or destroyed. The total stays the same.",
        "closed system": "A group of objects that no energy can enter or leave.",
        "dissipated": "Spread out into the surroundings, mostly by heating, so it is hard to use.",
        "friction": "A force that acts against movement between two surfaces. It heats both surfaces.",
    },
    "knowledge": [
        {"kind": "card", "title": "The law",
         "body": ["Energy cannot be created or destroyed.",
                  "It can only be transferred from one store to another.",
                  "So in a closed system, the total energy never changes.",
                  "Only the way it is shared between the stores changes."]},
        {"kind": "card", "title": "A swinging pendulum",
         "body": [{"figure": "p1-pendulum-stores"},
                  "It starts at the top with 120 J in its gravitational potential store.",
                  "At the bottom, most of it is in the kinetic store.",
                  "Each swing, air resistance and friction at the pivot heat the surroundings.",
                  "When it stops, all 120 J is in thermal stores of the surroundings.",
                  "The total is 120 J all the way through."]},
        {"kind": "card", "title": "Stopped does not mean out of energy",
         "body": ["A car that has stopped has an empty kinetic store.",
                  "Its fuel tank may still be full.",
                  "Its brakes are now hot, so their thermal store has filled.",
                  "The energy has moved. None of it has been destroyed."]},
        {"kind": "card", "title": "Efficient and wasteful machines",
         "body": ["Every machine obeys conservation of energy exactly.",
                  "An efficient machine wastes less of the energy put in.",
                  "The wasted energy still exists, in thermal stores of the surroundings."]},
        {"kind": "card", "title": "Machines that run forever",
         "body": ["Some people claim a machine can run forever with no energy supply.",
                  "Friction and air resistance always dissipate some energy by heating.",
                  "So a machine with no energy supply slows down and stops.",
                  "A machine that lights a lamp must be emptying some energy store.",
                  "If no store can keep supplying it, the claim is false.",
                  "Magnets return to the same positions each turn.",
                  "So over each turn, the magnets supply no energy."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A stopped object has run out of energy.",
              "Its kinetic store is empty. The energy is now in other stores."),
             ("Friction destroys energy.",
              "Friction transfers energy to thermal stores."),
             ("Only efficient machines conserve energy.",
              "Every machine conserves energy. Efficient ones waste less of it."),
         ]}]},
    ],
    "key_fact": "Energy cannot be created or destroyed. In a closed system, the total energy stays "
                "the same. When friction or air resistance slows something, energy is dissipated to the "
                "surroundings by heating.",
    "deeper": [
        {"kind": "card", "title": "Why a bouncing ball stops",
         "body": ["Each bounce squashes the ball against the floor.",
                  "Some energy heats the ball and the floor.",
                  "So each bounce is a little lower than the last."]},
        {"kind": "card", "title": "The missing energy that found a particle",
         "body": ["In the 1920s, some energy seemed to vanish in one kind of radioactive decay.",
                  "In 1930, Wolfgang Pauli suggested an unseen particle carried it away.",
                  "This particle, the neutrino, was detected in 1956.",
                  "The total balanced again."]},
    ],
    "try": None,
    "ks4_becomes": "Closed systems, and the efficiency of real devices.",
    "figures": [
        {"id": "p1-pendulum-stores", "kind": "diagram", "status": "drawn", "art": "store-bars",
         "title": "Energy stores of a pendulum and its surroundings at three moments",
         "desc": "Three bar charts, each with a dashed total line at 120 J. "
                 "Just released: gravitational potential 120 J. "
                 "Bottom of the first swing: kinetic 117 J, thermal (surroundings) 3 J. "
                 "Long after it stops: thermal (surroundings) 120 J.",
         "caption": "The bars change. The total stays at 120 J.",
         "data": {"total": 120, "unit": "J",
                  "stores": ["Gravitational potential", "Kinetic", "Thermal (surroundings)"],
                  "panels": [
                      {"label": "Just released", "values": [120, 0, 0]},
                      {"label": "Bottom of the first swing", "values": [0, 117, 3]},
                      {"label": "Long after it stops", "values": [0, 0, 120]},
                  ]}},
    ],
    "ladder_stem": {
        "apply": "A pendulum is released with 120 J in its gravitational potential store. It swings "
                 "until it hangs still. What is true of this 120 J of energy at the end?",
        "explain": "A skateboarder starts at the top of one side of a half-pipe. They roll down, then up "
                   "the other side. They do not quite reach their starting height. Explain what happened "
                   "to the energy. Explain why conservation of energy is not broken.",
        "produce": "An advert shows a machine made of magnets. Once started, it is said to turn forever. "
                   "It also lights a lamp with no fuel. Use conservation of energy to explain why it "
                   "cannot work. Say how you would test it.",
    },
    "ladder_ticks": [
        ["Says the energy starts in the gravitational store, at the highest point.",
         "Says the energy starts in the gravitational potential store, at the top."],
        ["Says it fills the kinetic store on the way down, and the gravitational store again on the way up.",
         "Says the kinetic store fills on the way down. Gravitational potential fills on the way up."],
        ["Names where the thermal stores are — the wheels, the ramp, the air.",
         "Names where the thermal stores are, such as the wheels, ramp and air."],
        ["Says friction and air resistance always move energy into thermal stores, so the machine must run down.",
         "Says friction and air resistance dissipate energy, so the machine must slow down."],
        ["Says the light requires energy to be supplied continuously.",
         "Says a lamp lit forever needs energy supplied forever."],
        ["Identifies that the claim requires a store nobody can name — the giveaway.",
         "Says the magnets return to the same positions, so they supply no energy overall."],
        ["Names a measurement: run it in a sealed insulated box and check whether anything gets warmer, or "
         "simply time how long it runs.",
         "Names a test, such as timing how long it runs with no supply."],
    ],
    "ladder_feedback": {
        "recall": {
            1: "Machines transfer energy. They never use it up.",
            2: "Energy is not lost. It is transferred to thermal stores.",
            3: "Efficiency describes how energy is shared out, not the total.",
        },
        "apply": {
            0: "Friction transfers energy to thermal stores. It cannot destroy energy.",
            1: "Nothing is moving, so the kinetic store is empty. The 120 J is in thermal stores.",
            3: "None of it is destroyed. All 120 J is still there, in thermal stores.",
        },
    },
}
