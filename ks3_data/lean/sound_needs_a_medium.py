# -*- coding: utf-8 -*-
"""Sound needs a medium, in the lean shape. Spec table: docs/lessons/wave2/ks3-sound-needs-a-medium.md."""

LESSON = {
    "slug": "sound-needs-a-medium",
    "start": {
        "setup": "A small buzzer hangs on a thread inside a thick glass jar, ringing away. "
                 "A pump starts pulling the air out of the jar.",
        "question": "If you had to guess, once the air is out, does the little hammer keep beating "
                    "against the bell?",
        "options": [
            ("Yes, it keeps beating",
             "Yes. The buzzer runs on electricity, so it keeps beating. But the sound fades to nothing."),
            ("No, it stops beating",
             "It keeps beating, because the buzzer runs on electricity. What stops is the sound."),
        ],
        "answer": 0,
    },
    "words": ["medium", "vacuum", "speed of sound"],
    "word_defs": {
        "medium": "The material a wave travels through. Sound needs a solid, a liquid or a gas.",
        "vacuum": "A space with no particles in it at all. Sound cannot travel through it.",
        "speed of sound": "How fast sound travels through a material. It is different in each material.",
    },
    "knowledge": [
        {"kind": "card", "title": "Sound needs particles",
         "body": ["Sound is a vibration passed from particle to particle.",
                  "Each particle pushes the next one along, so the vibration travels.",
                  "The material sound travels through is called the medium.",
                  "Sound can travel through solids, liquids and gases.",
                  "A vacuum has no particles, so sound cannot travel through it."]},
        {"kind": "card", "title": "The bell jar experiment",
         "body": [{"figure": "p6-medium-bell-jar"},
                  "A ringing buzzer hangs inside a glass jar.",
                  "A vacuum pump slowly takes the air out of the jar.",
                  "The sound gets quieter and quieter, until you hear nothing.",
                  "You can still see the hammer beating against the bell.",
                  "Light can travel through a vacuum, so you still see it.",
                  "Let the air back in, and you hear the sound again.",
                  "So the buzzer never stopped. Sound needs particles to travel."]},
        {"kind": "reveal", "title": "Sound in different materials",
         "cols": ["The particles", "Speed of sound"],
         "rows": [
             ("A vacuum", "None at all", "No sound"),
             ("Air, a gas", "Far apart", "About 340 m/s"),
             ("Water, a liquid", "Close together", "About 1500 m/s"),
             ("Steel, a solid", "Close and held tightly", "About 5000 m/s"),
         ]},
        {"kind": "card", "title": "Why sound is fastest in solids",
         "body": ["Sound travels fastest in solids, slower in liquids and slowest in gases.",
                  "In a solid, the particles are close together and strongly held.",
                  "Each one passes the vibration to the next very quickly.",
                  "In a gas, the particles are far apart.",
                  "The vibration takes longer to pass from one particle to the next.",
                  "Sound travels about 15 times faster in steel than in air."]},
        {"kind": "card", "title": "The speed equation",
         "body": [{"figure": "p6-medium-speed-triangle"},
                  "distance (m) = speed (m/s) × time (s)",
                  "speed = distance ÷ time",
                  "time = distance ÷ speed",
                  "Use the speed of sound for the material the sound travels through."]},
        {"kind": "card", "title": "Worked example: through a rail",
         "body": [{"figure": "p6-medium-rail"},
                  "A hammer hits one end of a steel rail 1000 m long.",
                  "Find the time the sound takes to travel along the steel.",
                  {"points": ["Convert: nothing. The distance is in m and the speed is in m/s.",
                              "Formula: time = distance ÷ speed",
                              "Insert: time = 1000 m ÷ 5000 m/s",
                              "Fine-tune: 1000 ÷ 5000 = 0.2",
                              "Answer: time = 0.2 s"]},
                  "Through the air, the same sound takes 1000 ÷ 340 = 2.9 s.",
                  "So the listener hears the blow through the rail first."]},
        {"kind": "card", "title": "Worked example: finding a speed",
         "body": ["A tap travels 2.4 km along a steel pipe in 0.48 s. Find the speed of sound in the pipe.",
                  {"points": ["Convert: 2.4 km × 1000 = 2400 m",
                              "Formula: speed = distance ÷ time",
                              "Insert: speed = 2400 m ÷ 0.48 s",
                              "Fine-tune: 2400 ÷ 0.48 = 5000",
                              "Answer: speed = 5000 m/s"]},
                  "Put in 2.4 instead of 2400, and the answer is a thousand times too small."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Sound can cross a vacuum, just very faintly.",
              "Sound cannot cross a vacuum at all. There are no particles to carry it.", "WAVE-21"),
             ("Sound is fastest in air, because air is easy to move through.",
              "Sound is slowest in gases like air. It is fastest in solids.", "WAVE-22"),
             ("The buzzer cannot vibrate in a vacuum, because there is no air to push against.",
              "It vibrates just the same. There are no particles to carry the vibration away.", "WAVE-23"),
             ("Sound can only travel through air.",
              "Sound travels through any solid, liquid or gas.", "WAVE-24"),
             ("Put 2.4 km straight into the equation.",
              "Change kilometres to metres first. 2.4 km is 2400 m."),
         ]}]},
    ],
    "key_fact": "Sound is a vibration passed from particle to particle, so it needs a medium. "
                "It cannot travel through a vacuum. "
                "It is fastest in solids and slowest in gases. "
                "Speeds: about 340 m/s in air, 1500 m/s in water, 5000 m/s in steel.",
    "deeper": [
        {"kind": "card", "title": "Listening through metal",
         "body": ["Put your ear to a long metal fence while someone taps the far end.",
                  "You hear the tap through the metal first.",
                  "A moment later, you hear it again through the air."]},
        {"kind": "card", "title": "Warm air and cold air",
         "body": ["Sound travels a little faster in warm air than in cold air.",
                  "The speed goes up by about 0.6 m/s for each degree Celsius.",
                  "So 340 m/s is a typical value for air, not an exact one."]},
        {"kind": "card", "title": "Talking in space",
         "body": ["Space is a vacuum, so astronauts cannot talk to each other through it.",
                  "They use radios instead.",
                  "Radio waves, like light, can travel through a vacuum."]},
    ],
    "try": None,
    "tutor_body": "Want to check a speed of sound calculation?",
    "ks4_becomes": "Measuring the speed of sound, and the wave equation: wave speed = frequency × wavelength.",
    "figures": [
        {"id": "p6-medium-bell-jar", "kind": "diagram", "status": "drawn", "art": "p6-medium-bell-jar",
         "title": "The bell jar experiment",
         "desc": "Two glass jars side by side, each on a base plate with a pipe to a vacuum pump. "
                 "In each jar an electric buzzer hangs from a wire, its hammer beating against its bell. "
                 "The left jar is full of air, drawn as dots, and curved lines show sound leaving it. "
                 "It is labelled: air in the jar, you hear the bell. The right jar has no dots and no "
                 "sound lines. It is labelled: air pumped out, you hear nothing.",
         "caption": "The hammer beats in both jars. Only the jar with air in it lets the sound out.",
         "data": {"pump": "to the vacuum pump",
                  "panels": [{"title": "Air in the jar", "result": "You hear the bell", "air": True},
                             {"title": "Air pumped out", "result": "You hear nothing", "air": False}]}},
        {"id": "p6-medium-speed-triangle", "kind": "diagram", "status": "drawn", "art": "formula-triangle",
         "title": "The formula triangle for distance, speed and time",
         "desc": "A triangle split by a horizontal line. Distance, s, in metres, sits in the top part. "
                 "Speed, v, in metres per second, and time, t, in seconds, sit side by side in the bottom "
                 "part, with a multiplication sign between them.",
         "caption": "Cover the one you want. Side by side means multiply. One over the other means divide.",
         "data": {"top": {"s": "s", "name": "distance", "unit": "m", "caption": "distance in metres"},
                  "bottom": [{"s": "v", "name": "speed", "unit": "m/s", "caption": "speed in m/s"},
                             {"s": "t", "name": "time", "unit": "s", "caption": "time in seconds"}]}},
        {"id": "p6-medium-rail", "kind": "diagram", "status": "drawn", "art": "p6-medium-rail",
         "title": "One blow, two paths",
         "desc": "A hammer strikes the left end of a steel rail. A listener stands at the right end. "
                 "A measuring line under the rail is labelled 1000 m. A solid arrow along the rail is "
                 "labelled: through the steel, 5000 m/s. A dashed arrow through the air above it is "
                 "labelled: through the air, 340 m/s.",
         "caption": "The same blow reaches the listener through the steel and through the air.",
         "data": {"length": "1000 m",
                  "steel": "Through the steel: 5000 m/s",
                  "air": "Through the air: 340 m/s"}},
    ],
    "figure_caption": {"p6-medium-rail": None},     # the card text already says it
    "ladder_stem": {
        "produce": "You stand beside a long steel railway rail. You hear a hammer blow from far down the "
                   "track twice: once through the rail and once through the air. The blow is 1700 m away "
                   "along the rail. "
                   "Work out both arrival times and the gap between them. Say which arrives first and why.",
    },
    "ladder_feedback": {
        "recall": {
            0: "That divides the wrong way round. Time = distance ÷ speed, so 680 ÷ 340.",
            1: "The number is right but the unit is wrong. A time is in seconds.",
            3: "Multiplying gives a distance. To find a time, divide the distance by the speed.",
        },
        "apply": {
            0: "Sound cannot cross a vacuum at all, faintly or slowly. There are no particles.",
            2: "With nothing in the way, there is also nothing to carry the sound.",
            3: "Sound easily travels 100 m through air. Here it is the vacuum that stops it.",
        },
    },
}
