# -*- coding: utf-8 -*-
"""Simple machines (and work done), in the lean shape. Spec table: docs/lessons/wave1/ks3-simple-machines.md."""

LESSON = {
    "slug": "simple-machines",
    "start": {
        "setup": "A crowbar lets a small push lift a heavy paving slab.",
        "question": "If you had to guess, does your hand move further than the slab rises?",
        "options": [
            ("Much further", "Much further. A smaller force has to move through a bigger distance."),
            ("Not as far", "Much further. A smaller force has to move through a bigger distance."),
        ],
        "answer": 0,
    },
    "words": ["work done", "simple machine", "lever", "fulcrum"],
    "word_defs": {
        "work done": "The energy transferred when a force moves an object. It is measured in joules.",
        "simple machine": "A device, such as a lever or a ramp, that changes the force needed.",
        "lever": "A rigid bar that turns about a fixed point.",
        "fulcrum": "The fixed point a lever turns about. It is also called the pivot.",
    },
    "knowledge": [
        {"kind": "card", "title": "Work done",
         "body": ["When a force moves an object, energy is transferred.",
                  "This energy is called the work done.",
                  "Work done depends on two things: the force, and the distance moved.",
                  "The distance is measured in the direction of the force."]},
        {"kind": "card", "title": "The equation",
         "body": [{"figure": "p1-triangle-wfd"},
                  "work done = force × distance, or W = F × d",
                  {"points": ["W is the work done, in joules (J).",
                              "F is the force, in newtons (N).",
                              "d is the distance moved, in metres (m)."]},
                  "To find the force: F = W ÷ d.",
                  "To find the distance: d = W ÷ F.",
                  "A bigger force or a bigger distance means more work done."]},
        {"kind": "card", "title": "Worked example: work done",
         "body": ["A force of 80 N pushes a crate 250 cm along the floor. Find the work done.",
                  {"points": ["C, convert: 250 cm ÷ 100 = 2.5 m",
                              "F, formula: W = F × d",
                              "I, insert: W = 80 N × 2.5 m",
                              "F, fine-tune: 80 × 2.5 = 200",
                              "A, answer: W = 200 J"]},
                  "Forget to convert and you get 20 000 J. That is 100 times too big."]},
        {"kind": "card", "title": "How a lever helps",
         "body": [{"figure": "p1-lever-trade"},
                  "A lever lets a small force lift a heavy load.",
                  "This example is an ideal lever, with no friction.",
                  "You push down with 100 N. Your end moves 0.6 m.",
                  "Work done by you = 100 N × 0.6 m = 60 J.",
                  "The 600 N load rises 0.1 m.",
                  "Work done on the load = 600 N × 0.1 m = 60 J.",
                  "The force is 6 times smaller, so your end moves 6 times further."]},
        {"kind": "card", "title": "Ramps, pulleys and gears",
         "body": ["A ramp lets you raise a load with less force. You push it further.",
                  "With no friction, push × ramp length = weight × height.",
                  "A pulley system lets you lift with less force. You pull more rope.",
                  "Gears can increase the turning force. The output then turns more slowly.",
                  "Some levers work the other way round.",
                  "A big force moving a short way makes the far end move a long way.",
                  "A fishing rod and your forearm work like this.",
                  "No simple machine gives out more energy than you put in."]},
        {"kind": "card", "title": "Friction in machines",
         "body": ["Real machines have friction at the pivot, the axle or the ramp.",
                  "So you put in more energy than the load gains.",
                  "The extra energy is dissipated by heating.",
                  "So a real machine is less than 100% efficient."]},
        {"kind": "card", "title": "Stretching a spring",
         "body": ["Stretching a spring needs a force to move through a distance.",
                  "So work is done on the spring.",
                  "This work fills the spring's elastic potential store."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A lever gives you extra energy.",
              "A lever never gives out more energy than you put in. It changes the force and the distance."),
             ("Put 250 cm straight into W = F × d.",
              "Convert centimetres to metres first. Divide by 100."),
             ("A longer lever needs less energy.",
              "It needs less force. Your end moves further, so the energy is the same."),
         ]}]},
    ],
    "key_fact": "Work done is the energy transferred when a force moves an object. Work done = force "
                "× distance, in joules. A simple machine trades force for distance. A smaller force "
                "must move further, and a bigger force moves less far. It never reduces the energy needed.",
    "deeper": [
        {"kind": "card", "title": "Your arm is a lever",
         "body": ["Your elbow is the fulcrum. Your biceps pulls on your forearm, close to the elbow.",
                  "So the muscle needs a big force to lift a small load.",
                  "In return, your hand moves much further than the muscle shortens."]},
        {"kind": "card", "title": "Work done against friction",
         "body": ["Pushing a box across a floor at a steady speed still does work.",
                  "This work heats the box and the floor."]},
    ],
    "try": None,
    "ks4_becomes": "Moments, and work done as force × distance along the line of the force.",
    "figures": [
        {"id": "p1-triangle-wfd", "kind": "diagram", "status": "drawn", "art": "formula-triangle",
         "title": "The formula triangle for work done",
         "desc": "A triangle split by a horizontal line. W is in the top part. "
                 "F and d sit side by side in the bottom part. "
                 "A multiply sign sits between them.",
         "caption": "Cover the one you want to find.",
         "data": {"top": {"s": "W", "name": "work done", "unit": "J"},
                  "bottom": [{"s": "F", "name": "force", "unit": "N"},
                             {"s": "d", "name": "distance", "unit": "m"}]}},
        {"id": "p1-lever-trade", "kind": "diagram", "status": "drawn", "art": "lever-trade",
         "title": "A lever lifting a load",
         "desc": "A bar on a triangular fulcrum. "
                 "A 600 N load sits 0.2 m from the fulcrum and rises 0.1 m. "
                 "On the other side, 1.2 m from the fulcrum, a 100 N push moves down 0.6 m. "
                 "Dashed lines show the bar's starting position.",
         "caption": "Small force, big distance. Big force, small distance.",
         "data": {"effort": {"N": 100, "arm_m": 1.2, "moves_m": 0.6},
                  "load": {"N": 600, "arm_m": 0.2, "moves_m": 0.1}}},
    ],
    "ladder_stem": {
        "apply": "A barrel weighs 900 N. You push it up a ramp to a platform at a steady speed. "
                 "Your push along the ramp is 300 N. Ignore friction. What must be true?",
        "explain": "A lever lets you lift a 600 N load with a 100 N push. Explain why it cannot give you "
                   "energy for free. Explain why a real lever needs slightly more energy in than comes out.",
        "produce": "Advert A says a gear set doubles a drill's turning force. Advert B says the gears give "
                   "out twice the energy that goes into them. Explain which advert could be true. Say what "
                   "you would measure to check.",
    },
    "ladder_ticks": [
        ["Says force multiplied by distance at the effort end equals force multiplied by distance at the load end.",
         "Says that, with no friction, force × distance is the same at both ends."],
        ["Says a smaller force is always paid for with a larger distance.",
         "Says the smaller force moves further, such as 6 times as far."],
        ["Says the energy is the product, and the product does not change when the fulcrum moves.",
         "Says force × distance is the energy. An ideal lever gives out all of it."],
        ["Says force is not a conserved quantity, so multiplying it breaks no law.",
         "Says force can be made bigger, but energy cannot be created."],
        ["Says the measured input exceeded the output because friction at the fulcrum fills a thermal store "
         "— and that it was never smaller.",
         "Says friction at the fulcrum dissipates some energy by heating."],
        ["Says the faster-turning side must then turn more slowly, or through fewer turns.",
         "Says the drill bit then turns more slowly, making fewer turns each second."],
        ["Identifies “power” as energy per second, so “doubling the power for free” is the "
         "claim that is wrong.",
         "Says advert B is wrong, because gears cannot create energy."],
        ["Names a measurement: compare energy in and energy out over the same time, and check whether "
         "anything gets warm.",
         "Says to measure energy in and out over the same time, and check for warming."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Convert first: 40 cm is 0.40 m. So 150 × 0.40 = 60 J.",
            1: "That is 150 ÷ 0.40. Work done is force multiplied by distance.",
            2: "That is 150 + 40. Multiply the force by the distance in metres.",
        },
        "apply": {
            0: "The energy is the same as lifting it straight up. Only the force is smaller.",
            2: "A ramp has no energy supply. You push the barrel further instead.",
            3: "Its weight is still 900 N. You push less hard, but further.",
        },
    },
}
