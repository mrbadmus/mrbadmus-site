# -*- coding: utf-8 -*-
"""Echoes, reflection and absorption, in the lean shape.
Spec table: docs/lessons/wave2/ks3-echoes-reflection-and-absorption.md."""

LESSON = {
    "slug": "echoes-reflection-and-absorption",
    "start": {
        "setup": "You hear an echo only when the reflection comes back a little after your shout.",
        "question": "If you had to guess, would a hard brick wall a few steps in front of you give a "
                    "clear echo?",
        "options": [
            ("Yes, a clear echo",
             "The wall does reflect most of the sound. But it comes back too fast to hear on its own."),
            ("No, not a separate one",
             "Right. The reflection comes back too fast. Your ear blends it with your shout."),
        ],
        "answer": 1,
    },
    "words": ["reflected", "absorbed", "transmitted", "echo"],
    "word_defs": {
        "reflected": "Bounced back off a surface.",
        "absorbed": "Taken in by a material. The sound's energy warms the material very slightly.",
        "transmitted": "Passed on through a material and out the other side.",
        "echo": "A reflected sound that you hear as a separate sound.",
    },
    "knowledge": [
        {"kind": "card", "title": "When sound meets a surface",
         "body": [{"figure": "p6-echo-boundary"},
                  "When sound meets a surface, three things can happen.",
                  "Some of the sound is reflected. It bounces back off the surface.",
                  "Some is absorbed. The material takes in its energy.",
                  "Some is transmitted. It passes on through the material.",
                  "Usually all three happen at once."]},
        {"kind": "reveal", "title": "Hard and soft surfaces",
         "cols": ["Most of the sound is", "Examples"],
         "rows": [
             ("A hard, smooth surface", "Reflected", "A brick wall, a cliff, tiles"),
             ("A soft surface full of holes", "Absorbed", "Curtains, carpet, foam"),
         ]},
        {"kind": "card", "title": "What an echo needs",
         "body": ["An echo is a reflected sound that you hear as a separate sound.",
                  "It needs a hard surface that reflects most of the sound.",
                  "It also needs the surface to be far enough away.",
                  "A reflection back within about 0.1 s blends with your shout.",
                  "In air, the surface must be about 17 m away or more."]},
        {"kind": "card", "title": "There and back",
         "body": ["The sound travels to the surface, then back to you.",
                  "So it travels twice the distance to the surface.",
                  "distance travelled (m) = speed (m/s) × time (s)",
                  "distance to the surface = distance travelled ÷ 2"]},
        {"kind": "card", "title": "Worked example: how far is the cliff",
         "body": [{"figure": "p6-echo-cliff"},
                  "You shout at a cliff. The echo comes back 2.0 s later.",
                  "Sound travels at 340 m/s in air. Find how far away the cliff is.",
                  {"points": ["Convert: nothing. The speed is in m/s and the time is in s.",
                              "Formula: distance travelled = speed × time",
                              "Insert: distance travelled = 340 m/s × 2.0 s",
                              "Fine-tune: 340 × 2.0 = 680 m there and back. 680 ÷ 2 = 340",
                              "Answer: the cliff is 340 m away."]},
                  "Forget to halve, and your answer is twice the real distance."]},
        {"kind": "card", "title": "Worked example: depth of the sea",
         "body": ["A ship sends a pulse of sound down to the sea bed. The echo returns after 1.2 s.",
                  "Sound travels at 1500 m/s in sea water. Find the depth of the sea.",
                  {"points": ["Convert: nothing. The speed is in m/s and the time is in s.",
                              "Formula: distance travelled = speed × time",
                              "Insert: distance travelled = 1500 m/s × 1.2 s",
                              "Fine-tune: 1500 × 1.2 = 1800 m down and back. 1800 ÷ 2 = 900",
                              "Answer: the sea is 900 m deep."]},
                  "Use the speed of sound in water here, not in air."]},
        {"kind": "card", "title": "Too many echoes",
         "body": ["A sports hall or a swimming pool has hard walls and floors.",
                  "They reflect most of the sound, so voices echo and blur together.",
                  "Soft panels, curtains and carpets absorb sound, so less is reflected.",
                  "Recording studios have foam on the walls for the same reason."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("An echo is a new sound made by the wall.",
              "An echo is your own sound, reflected back off the wall.", "WAVE-25"),
             ("Soft materials stop sound travelling.",
              "Soft materials absorb much of the sound that hits them, so less is reflected.", "WAVE-26"),
             ("The distance to the cliff is speed × time.",
              "Speed × time is the distance there and back. Halve it.", "WAVE-27"),
             ("A small room has no echo because there is no room for the sound.",
              "The walls are too close. The reflection comes back too soon to hear separately.",
              "WAVE-28"),
             ("Halve the time, then halve the distance too.",
              "Halve only once: either the time or the total distance."),
         ]}]},
    ],
    "key_fact": "An echo is a reflected sound heard separately from the original. "
                "It needs a hard surface about 17 m away or more in air. "
                "The sound goes there and back. "
                "So the distance to the surface is (speed × time) ÷ 2.",
    "deeper": [
        {"kind": "card", "title": "Designing a hall for music",
         "body": ["A concert hall needs some reflections, or the music sounds dull.",
                  "Too many, and each note runs into the next.",
                  "Designers choose how much of each surface is hard and how much is soft."]},
        {"kind": "card", "title": "Blocking sound is different",
         "body": ["A thin foam panel absorbs echoes well.",
                  "It does little to stop noise reaching the next room.",
                  "A heavy brick wall is much better at that."]},
    ],
    "try": None,
    "tutor_body": "Want to check an echo calculation?",
    "connects_heading": None,
    "ks4_becomes": None,      # reflection at a boundary and echo sounding are GCSE Physics only, not every route
    "figures": [
        {"id": "p6-echo-boundary", "kind": "diagram", "status": "drawn", "art": "p6-echo-boundary",
         "title": "Sound meeting a wall",
         "desc": "An arrow labelled sound in travels from the left to a wall. One arrow goes back to the "
                 "left, labelled reflected. A dashed arrow carries on through the wall to the right, "
                 "labelled transmitted. Inside the wall a wavy line gets smaller and stops, labelled "
                 "absorbed.",
         "caption": "Reflected, absorbed and transmitted: usually some of each.",
         "data": {"labels": {"in": "sound in", "reflected": "reflected", "absorbed": "absorbed",
                             "transmitted": "transmitted", "wall": "wall"}}},
        {"id": "p6-echo-cliff", "kind": "diagram", "status": "drawn", "art": "p6-echo-cliff",
         "title": "A shout and its echo",
         "desc": "A person on the left shouts at a cliff on the right. At the top: echo back after 2.0 s, "
                 "sound in air 340 m/s. An arrow labelled there goes from the person to the cliff, and an "
                 "arrow labelled back returns to the person. A measuring line on the ground from the "
                 "person to the cliff is labelled distance equals question mark.",
         "caption": "The shout travels to the cliff and back again.",
         "data": {"given": ["Echo back after 2.0 s", "Sound in air: 340 m/s"],
                  "there": "there", "back": "back", "distance": "distance = ?"}},
    ],
    "figure_caption": {"p6-echo-cliff": None},     # the card text already says it
    "ladder_stem": {
        "produce": "A ship measures the depth of the sea. It sends a pulse of sound straight down and times "
                   "the echo. The pulse returns after 0.40 s. Sound travels at about 1500 m/s in sea water. "
                   "Work out the depth. Say why the answer would be wrong if you forgot that the pulse "
                   "makes two journeys.",
    },
    "ladder_ticks": [
        ["Names a soft, open-textured material to add — curtains, carpet, acoustic panels or similar.",
         "Names a soft material to add, such as curtains, carpet or acoustic panels."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Distance travelled is speed × time, not speed ÷ time.",
            1: "That halves twice. Halve the time, or halve the total distance, but not both.",
            2: "1020 m is there and back. The cliff is half of that, 510 m.",
        },
        "apply": {
            1: "Sound crosses the room easily. The soft things absorb it, so little comes back.",
            2: "Warm air does not absorb the sound. The carpet, curtains and bed do.",
            3: "Soft surfaces reflect much less than hard walls do. They absorb most of it.",
        },
    },
}
