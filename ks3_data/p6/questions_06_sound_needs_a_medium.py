"""P6 lesson 06 — Sound needs a medium: twelve questions (MRB-223).

Written against Design's page. The buzzer in the jar, the striker and
microphone and both worked examples are hers.

The discriminations, in the order the lesson builds them:

  · a vacuum carries NO sound, at any distance, for any time (`WAVE-21`);
  · sound is FASTEST in solids, not in air (`WAVE-22`);
  · what is missing in a vacuum is something to be pushed, not something
    to push against (`WAVE-23`);
  · any material will do — air is not special (`WAVE-24`) — the harder
    band sits here.

⚠️ POSITION IS AUTHORED — 2,3,0,1 · 0,1,3,2 · 1,0,2,3, three of each.

⚠️ The ladder's own two marked rungs are NOT restated, nor are the worked
examples' figures (1000 m in 0.20 s, 2.4 km in 0.48 s).
"""

UNIT = "P6"
LESSON = "sound-needs-a-medium"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p6-06-e01",
        "band": "easier",
        "text": "Sound cannot travel through a vacuum because…",
        "options": [
            {"text": "a vacuum is far too cold for any disturbance to be "
                     "passed along from place to place", "correct": False,
             "why": "Temperature changes the speed a little. It is not why "
                    "there is no sound at all."},
            {"text": "a vacuum is far too dark for any disturbance to be "
                     "able to find its way across", "correct": False,
             "why": "Light and sound are different things, and darkness has "
                    "nothing to do with it."},
            {"text": "there are no particles at all there to pass the "
                     "disturbance from one to the next", "correct": True},
            {"text": "sound is absorbed by empty space, which soaks up any "
                     "disturbance that tries to cross it", "correct": False,
             "why": "Absorbing needs a material to do the absorbing, and "
                    "there is none. Nothing sets off in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e02",
        "band": "easier",
        "text": "Sound travels fastest through…",
        "options": [
            {"text": "a gas", "correct": False,
             "why": "In a gas the particles are furthest apart, so it is the "
                    "slowest of the three."},
            {"text": "a liquid", "correct": False,
             "why": "A liquid is faster than a gas and slower than a solid."},
            {"text": "a vacuum", "correct": False,
             "why": "A vacuum has no speed of sound at all, because no sound "
                    "crosses it."},
            {"text": "a solid", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e03",
        "band": "easier",
        "text": "The speed of sound in air is about…",
        "options": [
            {"text": "340 m/s", "correct": True},
            {"text": "1500 m/s", "correct": False,
             "why": "That is roughly the speed in water."},
            {"text": "5000 m/s", "correct": False,
             "why": "That is roughly the speed in steel."},
            {"text": "300 000 000 m/s", "correct": False,
             "why": "That is the speed of light, about a million times "
                    "faster."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e04",
        "band": "easier",
        "text": "A bang travels 1700 m through air at about 340 m/s. How "
                "long does it take?",
        "options": [
            {"text": "About 578 000 s", "correct": False,
             "why": "That multiplies the distance by the speed. To find a "
                    "time you divide."},
            {"text": "5.0 s", "correct": True},
            {"text": "0.20 s", "correct": False,
             "why": "That divides the speed by the distance — the "
                    "calculation upside down."},
            {"text": "5.0 m", "correct": False,
             "why": "The arithmetic is right and the unit is wrong. Metres "
                    "divided by metres per second leaves seconds."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p6-06-s01",
        "band": "standard",
        "text": "A buzzer rings inside a jar. As the air is pumped out the "
                "sound fades to nothing, and the hammer can still be seen "
                "beating. What does that show?",
        "options": [
            {"text": "The buzzer goes on working, and what has been removed "
                     "is the material that was carrying the sound",
             "correct": True},
            {"text": "The pump has switched the buzzer off", "correct": False,
             "why": "The hammer is visibly still beating, so the buzzer is "
                    "still working."},
            {"text": "The glass has become thicker as the pressure dropped",
             "correct": False,
             "why": "The glass is unchanged, and letting the air back in "
                    "restores the sound instantly."},
            {"text": "The sound is now too high for a person to hear, "
                     "because thinner air makes a buzzer ring faster",
             "correct": False,
             "why": "The hammer beats at the same rate throughout, so the "
                    "frequency has not changed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s02",
        "band": "standard",
        "text": "Why does sound travel faster in steel than in air?",
        "options": [
            {"text": "Because steel is a great deal heavier than air, and "
                     "heavy things always move faster through a room than "
                     "lighter ones do", "correct": False,
             "why": "Nothing is moving through the steel. The disturbance is "
                    "handed on from particle to particle."},
            {"text": "Because steel's particles are close together and "
                     "strongly linked, so each one passes the shove on "
                     "sooner", "correct": True},
            {"text": "Because steel is harder for sound to get into, so it "
                     "hurries through, and the more a material resists the "
                     "faster the sound crosses it", "correct": False,
             "why": "Difficulty getting in is not a mechanism, and it would "
                    "predict slowness rather than speed."},
            {"text": "Because steel does not absorb any of the sound at "
                     "all, so the whole of it arrives at the far end "
                     "rather than only a part of what set off",
             "correct": False,
             "why": "Steel does absorb some. Absorbing changes how much "
                    "arrives, not how fast it gets there."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s03",
        "band": "standard",
        "text": "A blow travels the length of a 3000 m steel pipe in 0.60 s. "
                "What is the speed of sound in the pipe?",
        "options": [
            {"text": "1800 m/s", "correct": False,
             "why": "That multiplies rather than divides, and gives a "
                    "distance rather than a speed."},
            {"text": "0.0002 m/s", "correct": False,
             "why": "That divides the time by the distance — upside down."},
            {"text": "500 m/s", "correct": False,
             "why": "That divides by 6 rather than by 0.60. Check where the "
                    "decimal point goes."},
            {"text": "5000 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s04",
        "band": "standard",
        "text": "A whale call carries for tens of kilometres through the "
                "sea. Which comparison with air is right?",
        "options": [
            {"text": "Sound in water is slower than it is in air, so the "
                     "call lasts longer and therefore carries further",
             "correct": False,
             "why": "It is faster in water, about 1500 m/s against 340."},
            {"text": "Sound in water and in air travel at exactly the same "
                     "speed, because it is the same sound either way",
             "correct": False,
             "why": "The speed belongs to the material, not to the sound, "
                    "and water and air are very different materials."},
            {"text": "Sound in water is more than four times faster than in "
                     "air, because the particles are already touching",
             "correct": True},
            {"text": "Sound cannot travel in water at all, which is why "
                     "whales have to signal to each other with light "
                     "instead", "correct": False,
             "why": "Water carries sound extremely well; it is light that "
                    "struggles to get far through the sea."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p6-06-h01",
        "band": "harder",
        "text": "A student says a vacuum stops sound because the buzzer has "
                "nothing to push against. Why is that reasoning a problem, "
                "even though the conclusion is right?",
        "options": [
            {"text": "Because the buzzer really does need something to push "
                     "against, and the student has the wrong material in "
                     "mind — it is the glass of the jar, not the air", "correct": False,
             "why": "It needs nothing to push against at all — that is the "
                    "point being missed."},
            {"text": "Because what is missing is something to BE pushed — a "
                     "chain of particles — not something to push against, "
                     "and the same error gets rockets in space wrong",
             "correct": True},
            {"text": "Because the buzzer stops vibrating in a vacuum, so "
                     "there is nothing to explain", "correct": False,
             "why": "The buzzer visibly goes on vibrating throughout."},
            {"text": "Because sound does cross a vacuum, just very slowly",
             "correct": False,
             "why": "It does not cross at all, at any speed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h02",
        "band": "harder",
        "text": "You put your ear to one end of a 200 m metal fence and "
                "someone taps the far end once. You hear two taps. Roughly "
                "how far apart are they?",
        "options": [
            {"text": "About half a second", "correct": True},
            {"text": "About a tenth of a second", "correct": False,
             "why": "Through the air alone the trip takes about 0.59 s, so "
                    "the gap cannot be that small."},
            {"text": "About five seconds", "correct": False,
             "why": "Even the slower path, through the air, takes well under "
                    "a second over 200 m."},
            {"text": "They arrive together, because it is one tap",
             "correct": False,
             "why": "One tap, but two paths at very different speeds — which "
                    "is exactly why two arrivals are heard."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h03",
        "band": "harder",
        "text": "Why is the value 340 m/s always quoted with a temperature "
                "attached?",
        "options": [
            {"text": "Because cold air is denser than warm air, and denser "
                     "air blocks the sound on its way", "correct": False,
             "why": "Density is not the mechanism here, and warm air is "
                    "faster, not slower."},
            {"text": "Because sound is only made within a certain range of "
                     "temperatures, and not outside it", "correct": False,
             "why": "Sound is made at any temperature. The clause is about "
                    "the speed, not about whether sound exists."},
            {"text": "Because warmer particles are already moving faster, so "
                     "they reach their neighbours sooner", "correct": True},
            {"text": "Because a thermometer is the instrument that has to "
                     "be used when measuring sound", "correct": False,
             "why": "Sound is timed rather than measured with a thermometer. "
                    "The temperature is a condition, not an instrument."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h04",
        "band": "harder",
        "text": "An astronaut on a spacewalk hears their own breathing and "
                "the radio, but nothing from outside. Why?",
        "options": [
            {"text": "Because the helmet blocks the outside sound in the "
                     "way that a pair of earplugs blocks the noise of a "
                     "busy room", "correct": False,
             "why": "Even with the visor open there would be nothing to "
                    "hear, because there is nothing outside to carry it."},
            {"text": "Because sound outside is at frequencies too high for "
                     "a human ear, since a thin medium can only carry the "
                     "fastest vibrations", "correct": False,
             "why": "There is no sound outside at any frequency, because "
                    "there are no particles to make one."},
            {"text": "Because the radio is louder than anything outside "
                     "could ever be, and it simply drowns out the rest of "
                     "what arrives at the helmet", "correct": False,
             "why": "Loudness is not the issue. Outside there is no sound "
                    "at all to be quieter."},
            {"text": "Because the suit holds a pocket of air that carries "
                     "sound, while outside it there are no particles at all",
             "correct": True},
        ],
        "figure": None,
    },
]
