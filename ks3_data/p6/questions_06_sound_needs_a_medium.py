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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p6-06-e05",
        "band": "easier",
        "text": "The speed of sound in water is about…",
        "options": [
            {"text": "340 m/s", "correct": False,
             "why": "That is the figure for air; water's particles are far "
                    "closer, so sound goes much faster."},
            {"text": "1500 m/s", "correct": True},
            {"text": "5000 m/s", "correct": False,
             "why": "That is the figure for steel, where the particles are "
                    "linked most strongly of the three."},
            {"text": "30 m/s", "correct": False,
             "why": "That is slower than sound in air, and water carries "
                    "sound better than air does."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e06",
        "band": "easier",
        "text": "Sound can travel through…",
        "options": [
            {"text": "air only", "correct": False,
             "why": "It travels through water and through steel too, and "
                    "faster in both."},
            {"text": "gases and liquids, but not solids", "correct": False,
             "why": "A tap on one end of a metal fence is heard at the other, "
                    "so solids carry it well."},
            {"text": "gases, liquids and solids", "correct": True},
            {"text": "anything, including a vacuum", "correct": False,
             "why": "A vacuum has no particles to pass the disturbance on, so "
                    "sound cannot cross it at all."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p6-06-s05",
        "band": "standard",
        "text": "A sound takes 2.0 s to cross 3000 m of sea water. What is "
                "its speed?",
        "options": [
            {"text": "6000 m/s", "correct": False,
             "why": "That is 3000 × 2.0. Speed is distance DIVIDED by time."},
            {"text": "1500 m/s", "correct": True},
            {"text": "0.00067 m/s", "correct": False,
             "why": "That is 2.0 ÷ 3000, the division upside down."},
            {"text": "2998 m/s", "correct": False,
             "why": "That subtracts, and a time cannot be taken from a "
                    "distance."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s06",
        "band": "standard",
        "text": "Why does a diver hear a boat's engine so clearly under "
                "water?",
        "options": [            {"text": "Because sound travels more slowly under water, so it "
                     "lasts longer",
             "correct": False,
             "why": "It travels much faster in water — about 1500 m/s against "
                    "340 m/s."},
            {"text": "Because sound is louder under water than in air",
             "correct": False,
             "why": "Loudness depends on the source; what changes is how well "
                    "the material carries the disturbance."},
            {"text": "Because water has no particles to get in the way",
             "correct": False,
             "why": "It is full of particles, and that is exactly why sound "
                    "travels through it so well."},
            {"text": "Because water carries sound well, its particles being "
                     "close together",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p6-06-h05",
        "band": "harder",
        "text": "A sound covers 680 m of air in 2.0 s, and the same 680 m of "
                "steel in 0.136 s. What are the two speeds?",
        "options": [
            {"text": "340 m/s in air and 5000 m/s in steel", "correct": True},
            {"text": "340 m/s in air and 340 m/s in steel", "correct": False,
             "why": "The steel journey took a fifteenth of the time, so its "
                    "speed cannot be the same."},
            {"text": "1360 m/s in air and 92 m/s in steel", "correct": False,
             "why": "Both come from multiplying rather than dividing, and "
                    "they put the faster one in the wrong material."},
            {"text": "0.003 m/s in air and 0.0002 m/s in steel",
             "correct": False,
             "why": "Both are the division upside down — time over distance "
                    "rather than distance over time."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h06",
        "band": "harder",
        "text": "Why does sound travel faster where the particles are closer "
                "together and more strongly linked?",
        "options": [
            {"text": "Because the particles themselves travel further with "
                     "each push",
             "correct": False,
             "why": "The particles barely move at all; it is the disturbance "
                    "that travels."},
            {"text": "Because each particle passes the disturbance on to its "
                     "neighbour sooner",
             "correct": True},
            {"text": "Because a denser material has more energy to give the "
                     "wave",
             "correct": False,
             "why": "The material adds no energy; all of it comes from the "
                    "source."},
            {"text": "Because there is less friction between close particles",
             "correct": False,
             "why": "Friction is not what limits the speed; how quickly one "
                    "particle affects the next is."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p6-06-e07",
        "band": "easier",
        "text": "Sound cannot travel through empty space because "
                "there is no…",
        "options": [
            {"text": "material there to pass the disturbance from one "
            "particle to the next", "correct": True},
            {"text": "gravity there to pull the sound along", "correct": False,
             "why": "Sound is not pulled along by gravity; it is passed on "
             "from particle to particle."},
            {"text": "light there for the sound to travel alongside on its "
            "journey across the gap", "correct": False,
             "why": "Sound does not need light to travel with it; it travels "
             "through matter on its own."},
            {"text": "energy available to make the sound louder", "correct": False,
             "why": "The missing thing is particles to carry a disturbance, "
             "not energy for loudness."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e08",
        "band": "easier",
        "text": "Sound travels through solid oak wood at about…",
        "options": [
            {"text": "340 m/s", "correct": False,
             "why": "That is roughly the speed in air, much slower than in "
             "solid oak."},
            {"text": "3800 m/s", "correct": True},
            {"text": "1500 m/s", "correct": False,
             "why": "That is roughly the speed in water, slower than in "
             "solid oak."},
            {"text": "5000 m/s", "correct": False,
             "why": "That is roughly the speed in steel, faster than in oak."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e09",
        "band": "easier",
        "text": "In which of these could a struck bell actually be "
                "heard?",
        "options": [
            {"text": "Inside a jar with all the air pumped out", "correct": False,
             "why": "With the air removed there are no particles left inside "
             "the jar to carry the sound."},
            {"text": "Floating in the vacuum of outer space", "correct": False,
             "why": "A vacuum has no particles at all, so no sound can cross "
             "it."},
            {"text": "Hanging inside a solid steel casing", "correct": True},
            {"text": "In the evacuated gap between the two walls of a vacuum "
            "flask", "correct": False,
             "why": "The gap between a vacuum flask's two walls has had its "
             "particles pumped out, so there is nothing there to carry a "
             "sound wave."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e10",
        "band": "easier",
        "text": "A siren's noise reaches a farmhouse 1020 m away "
                "through still air, where sound travels at 340 m/s. How long "
                "is the noise delayed by the journey?",
        "options": [
            {"text": "346 800 s", "correct": False,
             "why": "That multiplies the distance by the speed. To find a "
             "time you divide."},
            {"text": "0.33 s", "correct": False,
             "why": "That divides the speed by the distance — the "
             "calculation upside down."},
            {"text": "3.0 m", "correct": False,
             "why": "The arithmetic is right and the unit is wrong. Metres "
             "divided by metres per second leaves seconds."},
            {"text": "3.0 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e11",
        "band": "easier",
        "text": "Sound travels fastest through which of these four "
                "materials?",
        "options": [
            {"text": "Steel", "correct": True},
            {"text": "Air", "correct": False,
             "why": "Air is the slowest of the four; its particles are "
             "furthest apart."},
            {"text": "Water", "correct": False,
             "why": "Water is faster than air but slower than oak and steel."},
            {"text": "Oak", "correct": False,
             "why": "Oak is fast, but not as fast as steel."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e12",
        "band": "easier",
        "text": "A sound wave in a true vacuum would have to travel "
                "through…",
        "options": [
            {"text": "very spread-out particles moving slowly", "correct": False,
             "why": "A true vacuum has no particles left in it, spread out "
             "or otherwise."},
            {"text": "nothing, because a vacuum has no particles at all", "correct": True},
            {"text": "particles moving extremely fast", "correct": False,
             "why": "There are no particles present in a vacuum for anything "
             "to move."},
            {"text": "light particles only, with no matter", "correct": False,
             "why": "Light can cross a vacuum, but sound needs particles of "
             "matter, which a vacuum lacks."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e13",
        "band": "easier",
        "text": "The speed of sound is measured in units of…",
        "options": [
            {"text": "hertz", "correct": False,
             "why": "Hertz is the unit of frequency, a different quantity "
             "from speed."},
            {"text": "seconds", "correct": False,
             "why": "Seconds measure time on their own, not a speed."},
            {"text": "metres per second", "correct": True},
            {"text": "metres", "correct": False,
             "why": "Metres measure distance on their own, not a speed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e14",
        "band": "easier",
        "text": "A sound wave crosses a gap filled with water "
                "instead of air, with nothing else changed. Compared with "
                "air, the sound…",
        "options": [
            {"text": "travels slower", "correct": False,
             "why": "Water carries sound faster than air does, not slower."},
            {"text": "travels at exactly the same speed", "correct": False,
             "why": "The speed of sound depends on the material, and water "
             "and air are different materials."},
            {"text": "cannot cross water at all", "correct": False,
             "why": "Water carries sound extremely well; it is not a barrier "
             "to it."},
            {"text": "travels faster", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e15",
        "band": "easier",
        "text": "A whale's call can be heard by other whales many "
                "kilometres away. This is possible because…",
        "options": [
            {"text": "sound travels very well, and quite fast, through water", "correct": True},
            {"text": "whales actually use light rather than sound to "
            "communicate", "correct": False,
             "why": "Whale calls are genuine sound waves, not light signals."},
            {"text": "sound is louder underwater than in air for every "
            "source", "correct": False,
             "why": "Loudness depends on the source, not automatically on "
             "being underwater."},
            {"text": "water blocks every other sound, so the call stands out", "correct": False,
             "why": "Water carries many sounds well; it does not selectively "
             "block other sounds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e16",
        "band": "easier",
        "text": "Sound needs a medium to travel through. Which of "
                "these counts as a medium?",
        "options": [
            {"text": "A vacuum", "correct": False,
             "why": "A vacuum has no particles, so it cannot act as a "
             "medium."},
            {"text": "A solid, a liquid or a gas", "correct": True},
            {"text": "Empty space with nothing in it", "correct": False,
             "why": "Empty space with nothing in it has no particles to "
             "carry a sound wave."},
            {"text": "Darkness", "correct": False,
             "why": "Darkness is simply an absence of light, not a material "
             "of any kind."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e17",
        "band": "easier",
        "text": "A tap made at one end of a 2500 m steel pipeline is "
                "detected by a sensor at the far end, with the sound moving "
                "through the metal at 5000 m/s. How long does the tap's "
                "sound take to reach the sensor?",
        "options": [
            {"text": "12 500 000 s", "correct": False,
             "why": "That multiplies the distance by the speed. To find a "
             "time you divide."},
            {"text": "2.0 s", "correct": False,
             "why": "That divides the speed by the distance — the "
             "calculation upside down."},
            {"text": "0.5 s", "correct": True},
            {"text": "0.5 m", "correct": False,
             "why": "The arithmetic is right and the unit is wrong. Metres "
             "divided by metres per second leaves seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e18",
        "band": "easier",
        "text": "Compared with a gas, the particles in a solid are…",
        "options": [
            {"text": "further apart and more loosely linked", "correct": False,
             "why": "That describes a gas compared with a solid, the "
             "opposite way round."},
            {"text": "exactly the same distance apart", "correct": False,
             "why": "A solid's particles are packed much closer than a "
             "gas's."},
            {"text": "not linked to each other at all", "correct": False,
             "why": "A solid's particles are strongly linked; that linking "
             "is part of what makes it a solid."},
            {"text": "closer together and more strongly linked", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e19",
        "band": "easier",
        "text": "Because a solid's particles are close together and "
                "strongly linked, sound in a solid travels…",
        "options": [
            {"text": "faster than in a gas", "correct": True},
            {"text": "slower than in a gas", "correct": False,
             "why": "Closer, more strongly linked particles pass a "
             "disturbance on sooner, giving a faster speed, not a slower "
             "one."},
            {"text": "at exactly the same speed as in a gas", "correct": False,
             "why": "The closer spacing and stronger linking of a solid's "
             "particles genuinely change the speed."},
            {"text": "not at all, since solids block sound completely", "correct": False,
             "why": "Solids carry sound very well, often better than gases "
             "do."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e20",
        "band": "easier",
        "text": "Two tin cans joined by a tight string carry a "
                "whisper from one to the other. Along the middle of that "
                "journey, what is acting as the medium?",
        "options": [
            {"text": "The air inside the two cans, the whole way along", "correct": False,
             "why": "The air inside each can only takes the sound the last "
             "short step; the middle of the journey runs along the string."},
            {"text": "The tight string joining the two cans", "correct": True},
            {"text": "Nothing — the sound simply jumps the gap", "correct": False,
             "why": "There is no jump. The string's own particles pass the "
             "disturbance along, one to the next."},
            {"text": "The light travelling along the tight string", "correct": False,
             "why": "Light is not what carries a sound. The string's "
             "particles are the medium here."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e21",
        "band": "easier",
        "text": "A gap between a striker and a microphone is filled "
                "with steel instead of air, with nothing else changed. What "
                "happens to the time the sound takes to arrive?",
        "options": [
            {"text": "It increases, since sound travels slower through steel", "correct": False,
             "why": "Sound is faster in steel than in air, so the travel "
             "time gets shorter, not longer."},
            {"text": "It stays exactly the same", "correct": False,
             "why": "Changing the material changes the speed of sound, which "
             "changes the travel time too."},
            {"text": "It decreases, since sound travels faster through steel", "correct": True},
            {"text": "The sound cannot arrive at all through a solid", "correct": False,
             "why": "Solids carry sound very well, often faster than air "
             "does."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e22",
        "band": "easier",
        "text": "Sound is slowest in which of these three states of "
                "matter?",
        "options": [
            {"text": "A liquid", "correct": False,
             "why": "A liquid carries sound faster than a gas does."},
            {"text": "A solid", "correct": False,
             "why": "A solid carries sound faster than a gas does."},
            {"text": "Sound travels at the same speed in all three", "correct": False,
             "why": "The three states give three different speeds, from "
             "slowest in a gas to fastest in a solid."},
            {"text": "A gas", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e23",
        "band": "easier",
        "text": "A vacuum is best described as…",
        "options": [
            {"text": "a space containing no particles at all", "correct": True},
            {"text": "a space containing only light", "correct": False,
             "why": "A vacuum has no particles of matter, though light can "
             "still cross it; that is not what defines it."},
            {"text": "a very thin gas", "correct": False,
             "why": "A thin gas still has some particles in it; a vacuum has "
             "none."},
            {"text": "a very cold gas", "correct": False,
             "why": "Temperature is not what defines a vacuum; the absence "
             "of particles is."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e24",
        "band": "easier",
        "text": "A diver sets off an underwater signal 3000 m from a "
                "boat, and the sound moves through the sea water at 1500 "
                "m/s. How long before the signal reaches the boat?",
        "options": [
            {"text": "4 500 000 s", "correct": False,
             "why": "That multiplies the distance by the speed. To find a "
             "time you divide."},
            {"text": "2.0 s", "correct": True},
            {"text": "0.5 s", "correct": False,
             "why": "That divides the speed by the distance — the "
             "calculation upside down."},
            {"text": "2.0 m", "correct": False,
             "why": "The arithmetic is right and the unit is wrong. Metres "
             "divided by metres per second leaves seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e25",
        "band": "easier",
        "text": "Which of these correctly lists the three states of "
                "matter sound can travel through?",
        "options": [
            {"text": "Solid, liquid, vacuum", "correct": False,
             "why": "A vacuum has no particles, so it is not one of the "
             "three."},
            {"text": "Gas, vacuum, light", "correct": False,
             "why": "Neither a vacuum nor light is a state of matter sound "
             "needs a medium to cross."},
            {"text": "Solid, liquid, gas", "correct": True},
            {"text": "Liquid, light, vacuum", "correct": False,
             "why": "Neither light nor a vacuum is a state of matter that "
             "carries sound."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e26",
        "band": "easier",
        "text": "A struck bell is placed inside a sealed jar. As the "
                "air is slowly pumped out, what happens to the sound heard?",
        "options": [
            {"text": "It gets louder", "correct": False,
             "why": "Removing the particles that carry the sound makes it "
             "fade, not grow louder."},
            {"text": "It becomes higher-pitched", "correct": False,
             "why": "Pumping out the air removes the medium; it does not "
             "change how often the bell vibrates."},
            {"text": "It is completely unaffected", "correct": False,
             "why": "Removing the air removes the particles carrying the "
             "sound to the listener, so the sound does change."},
            {"text": "It fades away to nothing", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e27",
        "band": "easier",
        "text": "Sound travelling through solid oak wood is…",
        "options": [
            {"text": "longitudinal, exactly as it is in air", "correct": True},
            {"text": "transverse, unlike in air", "correct": False,
             "why": "Sound is longitudinal in every material it travels "
             "through, oak included."},
            {"text": "a mixture of both transverse and longitudinal at once", "correct": False,
             "why": "Sound stays purely longitudinal, whatever material "
             "carries it."},
            {"text": "not a wave at all, just a vibration of the wood", "correct": False,
             "why": "The vibration travelling away from its source through "
             "the wood is exactly what makes it a wave."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e28",
        "band": "easier",
        "text": "Sound can travel through a solid, a liquid or a "
                "gas, but not through…",
        "options": [
            {"text": "cold air", "correct": False,
             "why": "Cold air still has particles in it and carries sound, "
             "just at a slightly different speed."},
            {"text": "a vacuum", "correct": True},
            {"text": "deep water", "correct": False,
             "why": "Deep water is full of particles and carries sound very "
             "well."},
            {"text": "thick steel", "correct": False,
             "why": "Steel carries sound extremely well, faster than any of "
             "the other studied materials."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e29",
        "band": "easier",
        "text": "A sound wave crosses a 1000 m gap filled with air, "
                "taking about 2.94 s. Which speed does this match most "
                "closely?",
        "options": [
            {"text": "about 1500 m/s", "correct": False,
             "why": "That is roughly the speed of sound in water, far faster "
             "than this journey shows."},
            {"text": "about 5000 m/s", "correct": False,
             "why": "That is roughly the speed of sound in steel, far faster "
             "than this journey shows."},
            {"text": "about 340 m/s", "correct": True},
            {"text": "about 3800 m/s", "correct": False,
             "why": "That is roughly the speed of sound in oak, far faster "
             "than this journey shows."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-e30",
        "band": "easier",
        "text": "Increasing how strongly a solid's particles are "
                "linked to each other tends to make the speed of sound in "
                "it…",
        "options": [
            {"text": "slower", "correct": False,
             "why": "Stronger linking lets each particle pass a disturbance "
             "on sooner, which speeds sound up, not down."},
            {"text": "completely unaffected", "correct": False,
             "why": "How strongly particles are linked is exactly what "
             "changes the speed between different materials."},
            {"text": "impossible to predict in any material", "correct": False,
             "why": "The pattern across the materials studied is consistent: "
             "stronger linking gives a faster speed."},
            {"text": "faster", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p6-06-s07",
        "band": "standard",
        "text": "A blacksmith's hammer blow is heard through a 4.5 "
                "km length of railway track made of steel, which carries "
                "sound at 5000 m/s. How long does the sound take to travel "
                "the length of the track?",
        "options": [
            {"text": "0.9 s", "correct": True},
            {"text": "0.9", "correct": False,
             "why": "The arithmetic is right and the unit is missing: this "
             "needs to be given in seconds."},
            {"text": "22 500 000 s", "correct": False,
             "why": "That multiplies the distance by the speed rather than "
             "dividing one by the other."},
            {"text": "9 s", "correct": False,
             "why": "That divides by 500 rather than by the full 5000 m/s "
             "given."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s08",
        "band": "standard",
        "text": "A worker strikes one end of a 900 m steel rail, and "
                "a colleague timing the sound through the metal records 0.18 "
                "s before hearing it at the far end. What speed does this "
                "give for sound in the rail?",
        "options": [
            {"text": "162 m/s", "correct": False,
             "why": "That multiplies the distance by the time rather than "
             "dividing one by the other."},
            {"text": "5000 m/s", "correct": True},
            {"text": "0.0002 m/s", "correct": False,
             "why": "That divides the time by the distance — the calculation "
             "upside down."},
            {"text": "4500 m/s", "correct": False,
             "why": "That divides by 0.2 rather than by the 0.18 s actually "
             "given."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s09",
        "band": "standard",
        "text": "A sound wave crosses the same 500 m gap through air "
                "(340 m/s) and through water (1500 m/s). Roughly how many "
                "times faster does it arrive through water?",
        "options": [
            {"text": "About 0.23 times as fast", "correct": False,
             "why": "That inverts the comparison; water is the FASTER one "
             "here, by a factor bigger than one."},
            {"text": "About 2 times as fast", "correct": False,
             "why": "1500 m/s is more than four times 340 m/s, not roughly "
             "two times."},
            {"text": "About 4.4 times", "correct": True},
            {"text": "It cannot be compared without knowing the distance", "correct": False,
             "why": "The 500 m gap is the same for both journeys, and it "
             "cancels out of a speed ratio in any case."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s10",
        "band": "standard",
        "text": "Why does a sound wave in water reach a diver faster "
                "than the same sound would reach someone standing the same "
                "distance away in air?",
        "options": [
            {"text": "Because water pushes the sound wave along with its own "
            "currents", "correct": False,
             "why": "The wave travels through still water just as well; no "
             "current is needed to carry it."},
            {"text": "Because water is heavier, and heavier materials carry "
            "sound faster", "correct": False,
             "why": "It is the closeness and linking of the particles that "
             "matters, not simply how heavy the material is."},
            {"text": "Because sound becomes a completely different and "
            "faster type of wave the moment it is made underwater rather "
            "than in air", "correct": False,
             "why": "Sound stays the same type of wave, longitudinal, in "
             "every material; only its speed changes."},
            {"text": "Because water's particles are already touching, "
            "passing the disturbance on almost immediately", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s11",
        "band": "standard",
        "text": "A steel rail carries sound at 5000 m/s and an oak "
                "beam carries it at 3800 m/s, both over the same 1900 m "
                "length. Which arrives first, and by roughly how much?",
        "options": [
            {"text": "The steel one, by about 0.12 s", "correct": True},
            {"text": "The oak one, by about 0.12 s", "correct": False,
             "why": "Steel is the faster material here, so the steel journey "
             "finishes first, not the oak one."},
            {"text": "The steel one, by about 0.5 s", "correct": False,
             "why": "0.5 s is roughly the oak journey's own time on its own, "
             "not the gap between the two."},
            {"text": "They arrive together, since both are solids", "correct": False,
             "why": "Being a solid does not fix one single speed; steel and "
             "oak have different speeds from each other."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s12",
        "band": "standard",
        "text": "A sound wave crosses a gap filled first with air, "
                "then the SAME gap is emptied to a vacuum. Compare the two "
                "journeys.",
        "options": [
            {"text": "Through air it arrives instantly, and through the "
            "vacuum it arrives after a short delay", "correct": False,
             "why": "Sound takes a real, measurable time to cross air, and "
             "it never crosses a vacuum at all."},
            {"text": "Through air it arrives after a measurable delay; "
            "through the vacuum it never arrives at all", "correct": True},
            {"text": "It arrives at the same time either way, since the "
            "distance is unchanged", "correct": False,
             "why": "The distance being the same does not help; a vacuum has "
             "no particles to carry the sound across it."},
            {"text": "Through the vacuum it still arrives, but extremely "
            "faintly", "correct": False,
             "why": "There is no faint version; a vacuum carries no sound "
             "whatsoever."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s13",
        "band": "standard",
        "text": "A clap is made 850 cm from a wall-mounted sensor in "
                "still air, where sound moves at 340 m/s. How long does the "
                "clap's sound take to reach the sensor?",
        "options": [
            {"text": "2.5 s", "correct": False,
             "why": "That treats 850 cm as if it were 850 m rather than "
             "converting it into 8.5 m first."},
            {"text": "289 000 s", "correct": False,
             "why": "That multiplies the distance by the speed rather than "
             "dividing one by the other."},
            {"text": "0.025 s", "correct": True},
            {"text": "0.025 m", "correct": False,
             "why": "The arithmetic is right and the unit is wrong: this "
             "needs to be given in seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s14",
        "band": "standard",
        "text": "A sound wave takes 10.0 s to cross a 3400 m gap. "
                "What is the speed of sound in the material filling the gap, "
                "and which studied material does this match?",
        "options": [
            {"text": "1500 m/s, matching water", "correct": False,
             "why": "3400 m over 10.0 s gives 340 m/s, which matches air, "
             "not water."},
            {"text": "5000 m/s, matching steel", "correct": False,
             "why": "3400 m over 10.0 s gives 340 m/s, which matches air, "
             "not steel."},
            {"text": "34 000 m/s, matching no studied material", "correct": False,
             "why": "That multiplies the distance by 10 rather than dividing "
             "the distance by the time."},
            {"text": "340 m/s, matching air", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s15",
        "band": "standard",
        "text": "A sound wave crosses the same distance through oak "
                "(3800 m/s) and through steel (5000 m/s). Which statement is "
                "correct?",
        "options": [
            {"text": "The steel journey takes less time, since sound travels "
            "faster through steel", "correct": True},
            {"text": "The oak journey takes less time, since wood is lighter "
            "than steel", "correct": False,
             "why": "How heavy the material is does not decide this; steel's "
             "closer, more strongly linked particles make it the faster one."},
            {"text": "Both journeys take exactly the same time, since both "
            "are solids", "correct": False,
             "why": "Being a solid does not fix one single speed; oak and "
             "steel have different speeds from each other."},
            {"text": "The steel journey takes less time, but only because "
            "steel is magnetic", "correct": False,
             "why": "Steel being magnetic has nothing to do with how it "
             "carries sound; its particle spacing and bonding are what "
             "matter."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s16",
        "band": "standard",
        "text": "A ship's sonar sends a pulse through 2400 m of sea "
                "water and back again, 4800 m total, at 1500 m/s. How long "
                "does the round trip take?",
        "options": [
            {"text": "1.6 s", "correct": False,
             "why": "That uses only the 2400 m one-way distance, forgetting "
             "the return trip."},
            {"text": "3.2 s", "correct": True},
            {"text": "7 200 000 s", "correct": False,
             "why": "That multiplies the distance by the speed rather than "
             "dividing one by the other."},
            {"text": "3.2 m", "correct": False,
             "why": "The arithmetic is right and the unit is wrong: this "
             "needs to be given in seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s17",
        "band": "standard",
        "text": "Which of these correctly orders sound's speed, from "
                "slowest to fastest?",
        "options": [
            {"text": "Steel, oak, water, air", "correct": False,
             "why": "This is the order reversed, from fastest to slowest "
             "rather than slowest to fastest."},
            {"text": "Water, air, steel, oak", "correct": False,
             "why": "Air is the slowest of the four, not water, so air "
             "should come first."},
            {"text": "Air, water, oak, steel", "correct": True},
            {"text": "Air, oak, water, steel", "correct": False,
             "why": "Water is faster than oak, so water should come before "
             "oak in this order."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s18",
        "band": "standard",
        "text": "Explain why an explosion on the Moon's surface "
                "cannot be heard by someone standing nearby without a radio "
                "link, even though the light from it is clearly seen.",
        "options": [
            {"text": "Sound is much quieter on the Moon because of its lower "
            "gravity", "correct": False,
             "why": "Gravity is not what carries sound; the missing medium "
             "is the reason nothing is heard."},
            {"text": "The Moon's dust absorbs all sound before it can travel "
            "any distance", "correct": False,
             "why": "There is essentially no atmosphere for the sound to be "
             "produced in and travel through in the first place."},
            {"text": "Light travels so much faster than sound that by the "
            "time the sound would arrive it has been left impossibly far "
            "behind to ever be heard", "correct": False,
             "why": "Speed difference explains a delay, not total silence; "
             "the real reason is the missing medium."},
            {"text": "The Moon has essentially no atmosphere, so there are "
            "no particles there to carry a sound wave, while light needs no "
            "medium and crosses freely", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s19",
        "band": "standard",
        "text": "A sound wave crosses a 600 m gap filled with steel "
                "in 0.12 s. What is the speed of sound in the rail?",
        "options": [
            {"text": "5000 m/s", "correct": True},
            {"text": "72 m/s", "correct": False,
             "why": "That multiplies the distance by the time rather than "
             "dividing one by the other."},
            {"text": "0.0002 m/s", "correct": False,
             "why": "That divides the time by the distance — the calculation "
             "upside down."},
            {"text": "50 000 m/s", "correct": False,
             "why": "That has the decimal point in the wrong place; 600 "
             "divided by 0.12 is 5000, not 50 000."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s20",
        "band": "standard",
        "text": "A recording engineer wants sound to travel between "
                "two microphones as fast as possible. Which material should "
                "fill the gap between them?",
        "options": [
            {"text": "Air, since it is the lightest of the materials studied", "correct": False,
             "why": "Being light does not make a material fast for sound; "
             "air is in fact the slowest of the materials studied."},
            {"text": "Steel, since sound travels fastest through it of the "
            "materials studied", "correct": True},
            {"text": "A vacuum, since there is nothing in the way to slow "
            "the sound down", "correct": False,
             "why": "A vacuum carries no sound at all; having nothing in the "
             "way removes the medium sound needs."},
            {"text": "Water, since liquids carry sound faster than solids do", "correct": False,
             "why": "The pattern found here is the opposite: solids like "
             "steel carry sound faster than liquids like water."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s21",
        "band": "standard",
        "text": "A sound signal takes 1.5 minutes to cross a 135 km "
                "stretch of deep ocean water. What is the speed of sound in "
                "that water?",
        "options": [
            {"text": "90 m/s", "correct": False,
             "why": "That forgets to convert the 135 km into 135 000 m "
             "before dividing by the time."},
            {"text": "135 000 m/s", "correct": False,
             "why": "That forgets to divide by the time at all, giving only "
             "the distance in metres."},
            {"text": "1500 m/s", "correct": True},
            {"text": "15 m/s", "correct": False,
             "why": "That divides by 9000 rather than by the 90 seconds "
             "actually in 1.5 minutes."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s22",
        "band": "standard",
        "text": "A construction site uses a large hammer to signal "
                "along a buried steel pipe instead of shouting through the "
                "air alongside it, for a message that needs to travel a long "
                "way quickly. Why might this work better?",
        "options": [
            {"text": "Because shouting cannot be heard at all over long "
            "distances, whatever the material", "correct": False,
             "why": "Shouting can be heard over real distances through air; "
             "the pipe is simply faster, not the only option that works."},
            {"text": "Because the pipe amplifies the sound the way a musical "
            "instrument does", "correct": False,
             "why": "Amplification is a separate effect from speed, and is "
             "not why the pipe gets a signal there sooner."},
            {"text": "Because sound cannot travel through open air at all "
            "over long distances", "correct": False,
             "why": "Sound does travel through open air over real distances; "
             "it is simply slower than through the steel."},
            {"text": "Sound travels faster through the steel pipe than "
            "through the air alongside it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s23",
        "band": "standard",
        "text": "A sound wave's speed in a given material is best "
                "described as a property of…",
        "options": [
            {"text": "the material itself, not of the note being played", "correct": True},
            {"text": "the loudness of the source making the sound", "correct": False,
             "why": "Loudness comes from the amplitude of the source, not "
             "from the material the sound then travels through."},
            {"text": "the pitch of the note being played", "correct": False,
             "why": "Every pitch of sound travels at the same speed through "
             "a given material."},
            {"text": "the listener's distance from the source", "correct": False,
             "why": "Distance changes how long the journey takes, not the "
             "speed the sound travels at."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s24",
        "band": "standard",
        "text": "A class wants to compare how long a sound takes to "
                "cross air, water and steel. Which variable must they keep "
                "the same for the comparison to be fair?",
        "options": [
            {"text": "The material being tested, since that is the point of "
            "the comparison", "correct": False,
             "why": "The material is the one thing that has to change; it is "
             "the variable being tested, not a control."},
            {"text": "The distance the sound travels through each material", "correct": True},
            {"text": "The loudness of the sound, since a louder sound would "
            "arrive sooner", "correct": False,
             "why": "Loudness does not change the speed of sound, so keeping "
             "it fixed is not what makes this comparison fair."},
            {"text": "The time each journey takes, since equal times would "
            "make it a fair test", "correct": False,
             "why": "The time is the measurement being taken; forcing it to "
             "be equal would remove the very difference being looked for."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s25",
        "band": "standard",
        "text": "A sound wave crosses a 4600 m gap of sea water in "
                "about 3.07 s. Which speed does this most closely match?",
        "options": [
            {"text": "roughly 340 m/s", "correct": False,
             "why": "That is roughly the speed of sound in air, far slower "
             "than this journey shows."},
            {"text": "roughly 3800 m/s", "correct": False,
             "why": "That is roughly the speed of sound in oak, faster than "
             "this journey shows."},
            {"text": "roughly 1500 m/s", "correct": True},
            {"text": "roughly 5000 m/s", "correct": False,
             "why": "That is roughly the speed of sound in steel, faster "
             "than this journey shows."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s26",
        "band": "standard",
        "text": "A signal is sent through 1000 m of air and through "
                "1000 m of oak at the same time. Roughly how many seconds "
                "apart do the two signals arrive?",
        "options": [
            {"text": "About 0.26 s", "correct": False,
             "why": "That gives only the oak journey's own time, not the gap "
             "between the two arrivals."},
            {"text": "About 2.94 s", "correct": False,
             "why": "That gives only the air journey's own time, not the gap "
             "between the two arrivals."},
            {"text": "About 5.6 s", "correct": False,
             "why": "That adds the two travel times together instead of "
             "finding the difference between them."},
            {"text": "About 2.7 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s27",
        "band": "standard",
        "text": "A designer wants a warning system where two workers "
                "clearly hear a signal through two different materials at "
                "two noticeably different moments. Which pairing of the "
                "studied materials would give the biggest gap in arrival "
                "time over the same distance?",
        "options": [
            {"text": "Air and steel", "correct": True},
            {"text": "Water and oak", "correct": False,
             "why": "1500 m/s and 3800 m/s are closer to each other than "
             "air's 340 m/s and steel's 5000 m/s are."},
            {"text": "Oak and steel", "correct": False,
             "why": "3800 m/s and 5000 m/s are closer to each other than "
             "air's 340 m/s and steel's 5000 m/s are."},
            {"text": "Air and water", "correct": False,
             "why": "340 m/s and 1500 m/s give a smaller gap than air's 340 "
             "m/s and steel's 5000 m/s do."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s28",
        "band": "standard",
        "text": "A sound wave's speed through a given block of steel "
                "is measured today and again next week, with nothing about "
                "the steel changed in between. What would you expect?",
        "options": [
            {"text": "A different value each time, since sound speed varies "
            "randomly from day to day", "correct": False,
             "why": "The speed of sound in a given, unchanged material stays "
             "consistent; it is not a random value."},
            {"text": "Both measurements to come out the same, since speed is "
            "a property of the material", "correct": True},
            {"text": "A slower speed the second time, since the steel "
            "'tires' after carrying sound once", "correct": False,
             "why": "Carrying a sound wave once does not change the steel's "
             "own properties or slow it down afterwards."},
            {"text": "A faster speed the second time, since the steel has "
            "been 'warmed up' by the first measurement", "correct": False,
             "why": "A single measurement does not meaningfully warm a large "
             "block of steel or change its speed of sound."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s29",
        "band": "standard",
        "text": "A sound wave crosses a 4.5 m gap of air in about "
                "0.0132 s. Which value does this suggest for the speed of "
                "sound in air?",
        "options": [
            {"text": "About 34 m/s", "correct": False,
             "why": "That is ten times too small for the distance and time "
             "given here."},
            {"text": "About 3400 m/s", "correct": False,
             "why": "That is ten times too large for the distance and time "
             "given here."},
            {"text": "About 340 m/s", "correct": True},
            {"text": "About 1500 m/s", "correct": False,
             "why": "That matches water rather than air, and is far larger "
             "than this journey shows."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-s30",
        "band": "standard",
        "text": "Why is it more useful to know the speed of sound in "
                "a material than simply knowing that 'sound travels through "
                "it'?",
        "options": [
            {"text": "Because 'sound travels through it' is not actually "
            "true for any real material", "correct": False,
             "why": "Sound genuinely does travel through solids, liquids and "
             "gases; the statement itself is true."},
            {"text": "Because the speed tells you how loud the sound will be "
            "once it arrives", "correct": False,
             "why": "Loudness comes from the amplitude of the source, not "
             "from the speed the material carries sound at."},
            {"text": "Because the exact numerical value of the speed is what "
            "decides whether a given material counts as a proper medium for "
            "sound", "correct": False,
             "why": "Any material with particles counts as a medium, "
             "whatever its particular speed of sound turns out to be."},
            {"text": "Because the speed lets you calculate exactly how long "
            "a sound will take to cross a known distance", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p6-06-h07",
        "band": "harder",
        "text": "A student claims: 'Since steel is much denser than "
                "air, sound must travel slower through it, because denser "
                "things are harder to push through.' Evaluate.",
        "options": [
            {"text": "Wrong — sound is faster in steel because its particles "
            "are close together and strongly linked, letting each one pass "
            "the disturbance on sooner; density alone does not decide the "
            "speed", "correct": True},
            {"text": "Correct — greater density slows a sound wave down", "correct": False,
             "why": "The materials studied show the opposite pattern: the "
             "denser solids carry sound faster, not slower."},
            {"text": "Correct, though this idea is generally said to hold "
            "mainly for gases rather than for solids such as steel, where "
            "the pattern found by testing is said to run rather differently", "correct": False,
             "why": "The claim is wrong for solids too; steel's density goes "
             "with a faster speed, not a slower one."},
            {"text": "It cannot properly be evaluated unless the exact "
            "temperature of the block of steel being tested is first "
            "measured and stated", "correct": False,
             "why": "Temperature makes a small difference to the exact "
             "value, but it does not change the basic wrongness of linking "
             "density alone to a slower speed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h08",
        "band": "harder",
        "text": "A sound wave crosses a 7.5 km gap of steel. How "
                "long does the journey take?",
        "options": [
            {"text": "37 500 s", "correct": False,
             "why": "That treats 7.5 km as 7.5 m and then multiplies by the "
             "speed rather than dividing."},
            {"text": "1.5 s", "correct": True},
            {"text": "0.0002 s", "correct": False,
             "why": "That divides the speed by the distance — the "
             "calculation upside down."},
            {"text": "15 s", "correct": False,
             "why": "That has the decimal point in the wrong place; 7500 "
             "divided by 5000 is 1.5, not 15."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h09",
        "band": "harder",
        "text": "A student says: 'A vacuum has a very low, but "
                "non-zero, speed of sound, something like 1 m/s, because a "
                "little bit of sound always leaks through no matter what.' "
                "Evaluate.",
        "options": [
            {"text": "Correct — a very faint signal can leak through empty "
            "space", "correct": False,
             "why": "There are no particles in a vacuum to carry even a very "
             "faint signal; nothing crosses it."},
            {"text": "Correct, though this mainly shows up across very short "
            "vacuum gaps rather than longer ones like the gap in outer space", "correct": False,
             "why": "The length of the gap makes no difference; a vacuum "
             "carries no sound at any distance."},
            {"text": "Wrong — a vacuum has no particles at all, so it has no "
            "speed of sound whatsoever; sound simply does not cross it, at "
            "any speed", "correct": True},
            {"text": "It cannot be evaluated without knowing how loud the "
            "original sound was", "correct": False,
             "why": "Loudness plays no part here; a vacuum carries no sound "
             "whatever the original loudness."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h10",
        "band": "harder",
        "text": "A signal travels through 1000 m of water, then 500 "
                "m of steel, one length after the other. How long does the "
                "whole journey take?",
        "options": [
            {"text": "About 0.1 s", "correct": False,
             "why": "That gives only the steel part of the journey, "
             "forgetting the water section entirely."},
            {"text": "About 0.67 s", "correct": False,
             "why": "That gives only the water part of the journey, "
             "forgetting the steel section entirely."},
            {"text": "About 0.57 s", "correct": False,
             "why": "That subtracts the steel section's time from the water "
             "section's instead of adding the two together."},
            {"text": "About 0.77 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h11",
        "band": "harder",
        "text": "A student argues: 'Since the speed of sound in "
                "steel, 5000 m/s, is about fifteen times the speed in air, "
                "340 m/s, a sound must also be about fifteen times louder in "
                "steel.' Evaluate.",
        "options": [
            {"text": "Wrong — speed and loudness are unrelated; speed is a "
            "property of the material, while loudness depends on the "
            "amplitude of the source", "correct": True},
            {"text": "Correct — a faster-travelling sound wave naturally "
            "carries more energy with it as it moves through the material, "
            "the way a faster-moving object generally does", "correct": False,
             "why": "Speed is set by the material a wave travels through, "
             "not by how much energy or how loud the source is."},
            {"text": "Correct, but the loudness increase is smaller than "
            "fifteen times", "correct": False,
             "why": "There is no loudness increase from speed at all; the "
             "two are separate measurements entirely."},
            {"text": "It cannot be evaluated without knowing the frequency "
            "of the sound", "correct": False,
             "why": "Frequency sets the pitch, not the loudness, and is not "
             "needed to see that speed and loudness are unrelated."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h12",
        "band": "harder",
        "text": "A sound wave travels through steel for exactly 0.34 "
                "s. How far does it travel in that time?",
        "options": [
            {"text": "14 705 m", "correct": False,
             "why": "That divides the time into the speed rather than "
             "multiplying the speed by the time."},
            {"text": "1700 m", "correct": True},
            {"text": "1700 m/s", "correct": False,
             "why": "The arithmetic is right and the unit is wrong: this is "
             "a distance, not a speed."},
            {"text": "5000.34 m", "correct": False,
             "why": "That adds the time onto the speed rather than "
             "multiplying the two together."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h13",
        "band": "harder",
        "text": "A student says: 'Because oak is a solid, sound must "
                "travel faster through oak than through water, since water "
                "is only a liquid.' Given oak is about 3800 m/s and water "
                "about 1500 m/s, evaluate the STUDENT'S REASONING (not just "
                "the final answer).",
        "options": [
            {"text": "Wrong — oak is actually slower than water", "correct": False,
             "why": "3800 m/s is faster than 1500 m/s, so oak is genuinely "
             "the faster one here."},
            {"text": "It cannot be judged, since solids and liquids can "
            "never be compared with each other", "correct": False,
             "why": "The two speeds given can be compared directly, and one "
             "is simply bigger than the other."},
            {"text": "The conclusion happens to be right here, but the "
            "reasoning is flawed: it is particle spacing and bonding, not "
            "simply being a solid rather than a liquid, that decides speed, "
            "and this need not hold for every solid-versus-liquid comparison", "correct": True},
            {"text": "Correct, and any solid you could ever choose is faster "
            "than any liquid you could ever choose, purely because being a "
            "solid rather than a liquid is what decides the speed of sound "
            "in it, whatever the two particular materials happen to be in "
            "any given comparison", "correct": False,
             "why": "It is the particles' spacing and bonding that decide "
             "speed, not the solid-versus-liquid label by itself."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h14",
        "band": "harder",
        "text": "Sound in material X travels exactly 2.5 times as "
                "fast as in air, 340 m/s. Roughly what speed does this give "
                "for material X, and does it match any of the studied "
                "materials?",
        "options": [
            {"text": "1500 m/s, so material X must be water, since that is "
            "the nearest of the studied speeds to this value", "correct": False,
             "why": "2.5 times 340 m/s is about 850 m/s, not 1500 m/s, so "
             "this does not match water."},
            {"text": "3800 m/s, so material X must be oak", "correct": False,
             "why": "2.5 times 340 m/s is about 850 m/s, nowhere near oak's "
             "3800 m/s."},
            {"text": "136 m/s, so material X is slower than air", "correct": False,
             "why": "The question states X is 2.5 times FASTER than air, so "
             "its speed must be bigger than 340 m/s, not smaller."},
            {"text": "About 850 m/s, which does not match air, water, oak or "
            "steel, so X must be something else", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h15",
        "band": "harder",
        "text": "The speed of sound in air rises by about 0.6 m/s "
                "for every extra degree Celsius. Air at 0°C carries sound at "
                "about 331 m/s. Roughly what speed would you expect at 20°C?",
        "options": [
            {"text": "About 343 m/s", "correct": True},
            {"text": "About 331 m/s, since temperature has no real effect", "correct": False,
             "why": "The question states directly that temperature does "
             "change the speed, by about 0.6 m/s per degree."},
            {"text": "About 337 m/s", "correct": False,
             "why": "That only adds half the expected rise, as if the "
             "temperature had gone up by 10 degrees rather than 20."},
            {"text": "About 355 m/s", "correct": False,
             "why": "That roughly doubles the expected rise, as if the rate "
             "were about 1.2 m/s per degree rather than 0.6."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h16",
        "band": "harder",
        "text": "A student says: 'A vacuum flask that is very well "
                "insulated should carry sound between its walls better than "
                "an ordinary jar, since good insulation keeps things quiet.' "
                "What is wrong with this reasoning?",
        "options": [
            {"text": "Nothing is wrong — better insulation does help carry "
            "sound further between the two walls of the flask, in exactly "
            "the same way it helps keep a hot drink hot for a good deal "
            "longer than an ordinary uninsulated cup would", "correct": False,
             "why": "Insulating a gap does not add particles to it; an "
             "evacuated gap still has none to carry sound."},
            {"text": "It confuses being well-insulated, which keeps heat in "
            "or out, with having a medium to carry sound; the evacuated gap "
            "between a flask's walls has no particles in it either, whatever "
            "the insulation", "correct": True},
            {"text": "It is wrong mainly because vacuum flasks are built for "
            "hot drinks, not for sound experiments", "correct": False,
             "why": "What a flask is normally used for is not the issue; the "
             "evacuated gap between its walls simply has no particles in it."},
            {"text": "It cannot be judged without knowing how thick the "
            "flask's walls are", "correct": False,
             "why": "Wall thickness does not change whether the evacuated "
             "gap between them has particles in it or not."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h17",
        "band": "harder",
        "text": "A signal takes one fifteenth as long to cross a "
                "certain length of steel as it takes to cross the same "
                "length of air. The air journey takes 3.0 s. How long does "
                "the steel journey take, and does this match the studied "
                "speeds?",
        "options": [
            {"text": "45 s, and checking this against the studied speeds "
            "shows it does not match any of the materials studied on this "
            "bench", "correct": False,
             "why": "One fifteenth of 3.0 s is 0.2 s, not 45 s; that comes "
             "from multiplying by fifteen instead of dividing."},
            {"text": "0.2 s, but this does not match the studied speeds", "correct": False,
             "why": "0.2 s is exactly what a fifteen-times-faster material "
             "should give, matching steel's speed against air's closely."},
            {"text": "0.2 s, and this matches steel being about fifteen "
            "times faster than air, roughly 5000 m/s against 340 m/s", "correct": True},
            {"text": "15 s, and this matches the studied speeds", "correct": False,
             "why": "One fifteenth of 3.0 s is 0.2 s, not 15 s, and 15 s "
             "would not match a fifteen-times-faster material in any case."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h18",
        "band": "harder",
        "text": "A student says: 'Sound can only really travel "
                "properly through air; when it travels through other "
                "materials like brick or glass, that's a kind of special "
                "exception.' Evaluate.",
        "options": [
            {"text": "Correct — air is the one true medium for sound, and "
            "other materials merely pass on a weaker echo of the original "
            "sound that started out travelling through the surrounding air", "correct": False,
             "why": "Other materials carry a genuine sound wave of their "
             "own, not a weakened echo of the one in air."},
            {"text": "Correct, though this seems to hold for materials that "
            "are transparent, like glass", "correct": False,
             "why": "Being transparent has nothing to do with carrying "
             "sound; opaque solids like brick or steel carry it just as "
             "genuinely."},
            {"text": "It cannot be evaluated without knowing the exact "
            "thickness of the brick or glass", "correct": False,
             "why": "Thickness affects how long the journey takes, not "
             "whether the material can carry sound at all."},
            {"text": "Wrong — sound travels through any material with "
            "particles in it, and air is not special; it is simply the "
            "medium we happen to be surrounded by most of the time", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h19",
        "band": "harder",
        "text": "A very loud foghorn and a very quiet whistle are "
                "each sounded once, one straight after the other, from the "
                "same spot 1360 m across still air. Roughly how long after "
                "each sound is it heard?",
        "options": [
            {"text": "Both about 4.0 s later, since loudness does not affect "
            "the speed of sound", "correct": True},
            {"text": "The foghorn much sooner, since louder sounds travel "
            "faster", "correct": False,
             "why": "Loudness comes from amplitude, which does not change "
             "the speed of sound through a given material."},
            {"text": "The whistle much sooner, since quieter, higher sounds "
            "travel faster", "correct": False,
             "why": "Neither loudness nor pitch changes the speed of sound; "
             "both signals travel at the same 340 m/s here."},
            {"text": "It cannot be found without knowing each source's "
            "frequency", "correct": False,
             "why": "Frequency does not affect the speed of sound either; "
             "both signals take the same time regardless of pitch."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h20",
        "band": "harder",
        "text": "A signal crosses 1000 m of water in the same time "
                "as it crosses some length of steel. Roughly how long is "
                "that steel length?",
        "options": [
            {"text": "About 1000 m", "correct": False,
             "why": "That assumes the two lengths must match, ignoring that "
             "steel carries sound faster than water."},
            {"text": "About 3300 m", "correct": True},
            {"text": "About 300 m", "correct": False,
             "why": "That inverts the ratio of the two speeds rather than "
             "applying it the right way round."},
            {"text": "About 5000 m", "correct": False,
             "why": "That treats steel's speed value itself as if it were a "
             "length, rather than using it to scale the water's time."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h21",
        "band": "harder",
        "text": "The speed of sound in oak is usually quoted as about "
                "3800 m/s, 'measured along the grain'. What does this "
                "qualifying phrase tell you?",
        "options": [
            {"text": "That 3800 m/s is a rounded figure with no real "
            "directional dependence at all", "correct": False,
             "why": "The phrase specifically flags a direction, along the "
             "grain, and a measurement taken across the grain gives a "
             "different, slower speed."},
            {"text": "That the grain has to be physically removed from the "
            "wood before any valid measurement of its speed can properly be "
            "taken", "correct": False,
             "why": "The grain is part of what is being measured; removing "
             "it would not be part of a genuine measurement."},
            {"text": "That the speed of sound in oak depends on which "
            "direction it is measured in, not only on the fact that oak is a "
            "solid", "correct": True},
            {"text": "That oak is the only material studied whose speed "
            "could ever depend on direction", "correct": False,
             "why": "The phrase tells you only about oak; it makes no claim "
             "that other materials cannot depend on direction too."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h22",
        "band": "harder",
        "text": "A signal is sent through 200 m of air, then 200 m "
                "of water, then 200 m of oak, one length after another. "
                "Roughly how long does the whole 600 m journey take?",
        "options": [
            {"text": "About 0.6 s", "correct": False,
             "why": "That is close to only the air section's own time, "
             "ignoring the water and oak sections."},
            {"text": "About 1.76 s", "correct": False,
             "why": "That treats the whole 600 m as if it were entirely "
             "through air, ignoring the faster water and oak sections."},
            {"text": "About 0.19 s", "correct": False,
             "why": "That adds only the water and oak sections together, "
             "leaving out the air section entirely."},
            {"text": "About 0.77 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h23",
        "band": "harder",
        "text": "A student says: 'A material with particles held "
                "together even more strongly than steel's would carry sound "
                "slower, not faster, because the particles would resist "
                "moving at all.' Evaluate.",
        "options": [
            {"text": "Wrong — the pattern found across these materials is "
            "that stronger bonding and closer spacing let each particle pass "
            "the disturbance on sooner, giving a faster speed, not a slower "
            "one", "correct": True},
            {"text": "Correct — beyond steel, stronger bonding reverses the "
            "established trend", "correct": False,
             "why": "Nothing in the pattern found here suggests a reversal; "
             "stronger bonding keeps making the speed faster."},
            {"text": "Correct, though this idea is said to hold specifically "
            "for metals whose bonding is even stronger than that of ordinary "
            "steel, rather than for steel itself or for any of the other "
            "materials studied here", "correct": False,
             "why": "There is no such special case; stronger bonding fits "
             "the same faster-speed pattern for any material."},
            {"text": "It cannot be evaluated without testing every possible "
            "material", "correct": False,
             "why": "The established pattern across gases, liquids and the "
             "solids studied is already enough to judge the claim."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h24",
        "band": "harder",
        "text": "A geologist sets off a small explosion and detects "
                "the returning echo through solid rock, acting like a single "
                "material at about 4000 m/s, after 0.85 s for the round "
                "trip. How far away is the reflecting rock layer?",
        "options": [
            {"text": "3400 m", "correct": False,
             "why": "That is the full round-trip distance; the reflecting "
             "layer itself is only half that far away."},
            {"text": "1700 m", "correct": True},
            {"text": "850 m", "correct": False,
             "why": "That halves the distance one time too many: 3400 m is "
             "the round trip, and 1700 m is already the one-way distance."},
            {"text": "1700 m/s", "correct": False,
             "why": "The arithmetic is right and the unit is wrong: this is "
             "a distance, not a speed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h25",
        "band": "harder",
        "text": "A technician times an echo bounced off the far end "
                "of a very long steel cable to find its length. The echo "
                "takes 2.4 s to return. How long is the cable?",
        "options": [
            {"text": "12 000 m", "correct": False,
             "why": "That is the full round-trip distance; the cable itself "
             "is only half that long."},
            {"text": "2083 m", "correct": False,
             "why": "That divides the speed by the time rather than "
             "multiplying the speed by the time and then halving it."},
            {"text": "6000 m", "correct": True},
            {"text": "6000 m/s", "correct": False,
             "why": "The arithmetic is right and the unit is wrong: this is "
             "a distance, not a speed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h26",
        "band": "harder",
        "text": "A student says: 'Since sound is much louder in air "
                "close to a jet engine than it is deep in the ocean near a "
                "whale, sound must actually travel faster in air than in "
                "water.' Evaluate.",
        "options": [
            {"text": "Correct — louder sources produce faster-travelling "
            "sound waves", "correct": False,
             "why": "Loudness comes from the amplitude of the source; it "
             "does not change the speed the wave then travels at."},
            {"text": "Correct, though this seems to hold specifically for "
            "the particular comparison between a jet engine and a whale "
            "given here, rather than as a general rule for every pair of "
            "sources", "correct": False,
             "why": "There is no such special case; the speed of sound in a "
             "material does not depend on which particular source is being "
             "compared."},
            {"text": "It cannot be evaluated without knowing the exact "
            "loudness of each source in decibels", "correct": False,
             "why": "The exact loudness is not needed; speed and loudness "
             "are separate measurements regardless of the numbers involved."},
            {"text": "Wrong — how loud a sound is at its source has nothing "
            "to do with how fast the resulting wave travels; water in fact "
            "carries sound faster than air, about 1500 m/s against 340 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h27",
        "band": "harder",
        "text": "A sound wave travels through a 6200 m gap of steel. "
                "Roughly how long does the journey take, to two significant "
                "figures?",
        "options": [
            {"text": "1.2 s", "correct": True},
            {"text": "1.24 s", "correct": False,
             "why": "That keeps three significant figures rather than "
             "rounding to the two the question asks for."},
            {"text": "12.4 s", "correct": False,
             "why": "That has the decimal point in the wrong place; 6200 "
             "divided by 5000 is 1.24, not 12.4."},
            {"text": "0.81 s", "correct": False,
             "why": "That divides the speed by the distance — the "
             "calculation upside down."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h28",
        "band": "harder",
        "text": "A student argues that because a vacuum has no speed "
                "of sound, it must have an INFINITE speed of sound, since "
                "nothing at all is in the way to slow it down. Evaluate.",
        "options": [
            {"text": "Correct — with nothing in the way to resist it, a "
            "disturbance would be free to cross a vacuum in exactly zero "
            "time", "correct": False,
             "why": "There is no disturbance being carried at all in a "
             "vacuum, so there is nothing to arrive in zero time or any "
             "other time."},
            {"text": "Wrong — having nothing in the way does not create an "
            "unlimited speed; it removes the mechanism sound needs entirely, "
            "so there is no wave at all, not one travelling infinitely fast", "correct": True},
            {"text": "Correct, though this idea seems to apply over very "
            "short vacuum gaps", "correct": False,
             "why": "The length of the gap makes no difference; a vacuum "
             "carries no sound at any distance, short or long."},
            {"text": "It cannot properly be evaluated, since the whole idea "
            "of an infinite speed is one that ordinary physics never "
            "discusses, defines or makes any practical use of in any other "
            "situation", "correct": False,
             "why": "The claim can be judged directly: a vacuum carries no "
             "sound wave at all, infinite or otherwise."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h29",
        "band": "harder",
        "text": "A hiker shouts across a valley and hears the echo "
                "3.0 s later from a cliff face. Using the speed of sound in "
                "air, roughly how far away is the cliff?",
        "options": [
            {"text": "1020 m", "correct": False,
             "why": "That is the full round-trip distance the sound covers; "
             "the cliff itself is only half that far away."},
            {"text": "113 m", "correct": False,
             "why": "That divides the speed by the time rather than "
             "multiplying the speed by the time and then halving it."},
            {"text": "510 m", "correct": True},
            {"text": "510 m/s", "correct": False,
             "why": "The arithmetic is right and the unit is wrong: this is "
             "a distance, not a speed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-06-h30",
        "band": "harder",
        "text": "A student writes this summary: 'Sound needs "
                "SOME material to travel through, but which material it is "
                "doesn't actually matter, since all materials carry sound at "
                "exactly the same speed.' Give the best correction.",
        "options": [
            {"text": "The whole summary is correct, and the differing values "
            "quoted for different materials are only rounding errors", "correct": False,
             "why": "The gap between 340 m/s and 5000 m/s is far too large "
             "to be explained away as rounding."},
            {"text": "The whole summary is wrong — some single material is "
            "uniquely required for sound to travel at all", "correct": False,
             "why": "No single material is uniquely required; sound travels "
             "through any solid, liquid or gas with particles in it."},
            {"text": "The first half is wrong and the second half is right — "
            "sound needs exactly one specific material to exist as a wave at "
            "all, and this second material's own speed of sound never varies "
            "under any circumstance whatsoever, no matter what changes "
            "around it", "correct": False,
             "why": "Sound needs some material, not one specific one, and "
             "even a single material's speed can vary slightly, for instance "
             "with temperature."},
            {"text": "The first half is right, sound needs some material and "
            "none is uniquely special, but the second half is wrong: speed "
            "genuinely differs between materials, from about 340 m/s in air "
            "up to about 5000 m/s in steel, depending on particle spacing "
            "and bonding", "correct": True},
        ],
        "figure": None,
    },
]
