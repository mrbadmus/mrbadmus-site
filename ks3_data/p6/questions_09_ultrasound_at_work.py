"""P6 lesson 09 — Ultrasound at work: twelve questions (MRB-223).

Written against Design's page. The hidden weld, the three blocks and the
four-panel energy/information split are hers.

The discriminations, in the order the lesson builds them:

  · ultrasound obeys every ordinary rule of sound (`WAVE-33`);
  · the depth is HALF the path, and the speed belongs to the material;
  · a probe sends AND listens with the same face (`WAVE-34`);
  · the gel is there to remove the air, not to lubricate (`WAVE-36`), and
    the useful property is wavelength, not speed (`WAVE-35`) — the harder
    band sits here.

⚠️ POSITION IS AUTHORED — 1,2,3,0 · 2,1,0,3 · 3,0,1,2, three of each.

⚠️ The ladder's own two marked rungs are NOT restated: the 0.060 ms steel
calculation and the travels-through-solids statement do not appear again.
"""

UNIT = "P6"
LESSON = "ultrasound-at-work"
LESSON_NUMBER = 9

QUESTIONS = [
    {
        "id": "p6-09-e01",
        "band": "easier",
        "text": "Ultrasound is sound with a frequency above about…",
        "options": [
            {"text": "20 Hz",
                         "correct": False,
                         "why": "20 Hz is the BOTTOM of the human range. Below it is infrasound."},
            {"text": "20 000 Hz",
                         "correct": True},
            {"text": "2000 Hz",
                         "correct": False,
                         "why": "2000 Hz is comfortably inside the human range — most speech lives around "
                    "there."},
            {"text": "200 000 Hz",
                         "correct": False,
                         "why": "Sound becomes ultrasound long before that. Even a dog whistle at 30 000 Hz "
                    "is already ultrasound to us."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e02",
        "band": "easier",
        "text": "Which of these uses ultrasound for the ENERGY it carries?",
        "options": [
            {"text": "a medical scan",
                         "correct": False,
                         "why": "A scan wants information back and deliberately uses as little power as it "
                    "can."},
            {"text": "a microphone",
                         "correct": False,
                         "why": "A microphone works at ordinary audible frequencies, and it collects "
                    "information."},
            {"text": "an ultrasonic cleaning bath",
                         "correct": True},
            {"text": "an echo sounder on a ship",
                         "correct": False,
                         "why": "An echo sounder times what returns, so it is an information use."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e03",
        "band": "easier",
        "text": "A pulse of ultrasound is sent into a block and reflects off something 40 mm "
                "down. What total distance does it travel before it gets back?",
        "options": [
            {"text": "20 mm",
                         "correct": False,
                         "why": "That halves when it should double. The 40 mm is already the one-way depth."},
            {"text": "40 mm",
                         "correct": False,
                         "why": "That is only the trip down. The pulse has to come back too."},
            {"text": "160 mm",
                         "correct": False,
                         "why": "That is four times the depth. The journey has two legs, not four."},
            {"text": "80 mm",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e04",
        "band": "easier",
        "text": "A gauge is used on an aluminium block but is still set up for steel. What "
                "goes wrong?",
        "options": [
            {"text": "Nothing — the timing is all that matters",
                         "correct": False,
                         "why": "The timing has to be turned into a depth, and the speed of the material does "
                    "that."},
            {"text": "It reports every depth as too shallow",
                         "correct": False,
                         "why": "Aluminium is FASTER than steel, so the pulse covers more than the gauge "
                    "assumes — the error runs the other way."},
            {"text": "It reports every depth as too deep",
                         "correct": True},
            {"text": "It refuses to give a reading at all",
                         "correct": False,
                         "why": "It gives a perfectly confident reading, which is what makes the error easy "
                    "to miss."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s01",
        "band": "standard",
        "text": "The same reflector sits 60 mm down in water (about 1500 m/s) and in steel "
                "(about 5000 m/s). Where do the two pips on the screen sit closest together?",
        "options": [
            {"text": "In steel, because sound travels more than three times faster there, so the "
                     "echo is back much sooner",
                         "correct": True},
            {"text": "In water, because the pulse has a good deal less material to get through on "
                     "the way down and then back up again",
                         "correct": False,
                         "why": "The depth is the same in both. What differs is how fast the pulse gets there "
                    "and back."},
            {"text": "The same in both, because it is the same reflector at the same depth and the "
                     "screen shows depth rather than time",
                         "correct": False,
                         "why": "The screen shows TIME, and the same distance takes very different times in "
                    "the two materials."},
            {"text": "In water, because water reflects a great deal more of the pulse back to the "
                     "probe than steel does",
                         "correct": False,
                         "why": "How much comes back changes the height of the pip, not when it arrives."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s02",
        "band": "standard",
        "text": "Why does an ultrasound scan need a high frequency rather than an audible "
                "one?",
        "options": [
            {"text": "Because high frequencies travel faster and return sooner",
                         "correct": False,
                         "why": "Every frequency travels at the same speed in the same material."},
            {"text": "Because a high frequency has a very short wavelength, and a short wavelength "
                     "reflects off small features",
                         "correct": True},
            {"text": "Because low frequencies cannot get into the body at all, so only ultrasound "
                     "is able to cross the skin",
                         "correct": False,
                         "why": "Low frequencies enter perfectly well. They simply sail past small structures "
                    "without noticing them."},
            {"text": "Because high frequencies are louder",
                         "correct": False,
                         "why": "Loudness is amplitude and has nothing to do with frequency."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s03",
        "band": "standard",
        "text": "A probe on a water tank sends a pulse and the echo returns 0.20 ms later. "
                "Sound travels at about 1500 m/s in water. How deep is the reflector?",
        "options": [
            {"text": "About 150 mm",
                         "correct": True},
            {"text": "About 300 mm",
                         "correct": False,
                         "why": "That is the whole path, down and back. The reflector is halfway along it."},
            {"text": "About 75 mm",
                         "correct": False,
                         "why": "That halves twice. Halve once only."},
            {"text": "About 7500 mm",
                         "correct": False,
                         "why": "The time is 0.20 thousandths of a second, not 0.20 seconds. Check the "
                    "milliseconds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s04",
        "band": "standard",
        "text": "What do a medical scanner and a microphone have in common?",
        "options": [
            {"text": "Both deliver energy into whatever they are pointed at, and both are run at "
                     "as much power as they can manage",
                         "correct": False,
                         "why": "Both are information devices, and both work at as low a power as they can."},
            {"text": "Both work above 20 000 Hz, at frequencies that sit well past the top of "
                     "anything a person can hear",
                         "correct": False,
                         "why": "A microphone works at ordinary audible frequencies, roughly 20 to 20 000 Hz."},
            {"text": "Both need a layer of gel between them and whatever they are working on "
                     "before anything can get through",
                         "correct": False,
                         "why": "A microphone needs no gel; it takes sound straight out of the air."},
            {"text": "Both take information out of a sound wave and turn it into an electrical "
                     "signal",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h01",
        "band": "harder",
        "text": "Why is the gel between the probe and the skin essential rather than merely "
                "comfortable?",
        "options": [
            {"text": "Because it lets the probe slide about on the skin a great deal more easily "
                     "than it otherwise would do",
                         "correct": False,
                         "why": "It does help with that, but a dry probe pressed still against the skin would "
                    "still give no picture."},
            {"text": "Because it warms the skin so the tissue passes sound more readily, and warm "
                     "tissue carries a pulse further than cold tissue does",
                         "correct": False,
                         "why": "The gel is usually cold, and a degree or two would make no difference "
                    "anyway."},
            {"text": "Because it is what makes the ultrasound audible to the machine, which could "
                     "not register a returning pulse at all without it",
                         "correct": False,
                         "why": "The machine listens electronically and does not need anything made audible."},
            {"text": "Because a thin layer of air would reflect almost the whole pulse straight "
                     "back off the surface, so hardly any would get in",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h02",
        "band": "harder",
        "text": "A scanner looking deep into a body uses a lower frequency than one looking "
                "just under the skin. Why?",
        "options": [
            {"text": "Because high frequencies are absorbed faster and do not reach as far, so "
                     "depth is traded against detail",
                         "correct": True},
            {"text": "Because the structures deep inside are larger and move more slowly, and that "
                     "is what settles the choice",
                         "correct": False,
                         "why": "Size varies at every depth, and movement is not what sets the choice of "
                    "frequency."},
            {"text": "Because a low frequency travels faster and so gets down deeper before its "
                     "echo is needed back",
                         "correct": False,
                         "why": "All frequencies travel at the same speed in the same tissue."},
            {"text": "Because a lower frequency is safer for the deep tissue it has to travel "
                     "through on the way",
                         "correct": False,
                         "why": "Safety is managed by keeping the power low, not by the frequency choice."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h03",
        "band": "harder",
        "text": "A bat hunting in the open uses a lower call, then switches to a higher one "
                "as it closes on a moth. What is it trading?",
        "options": [
            {"text": "Loudness for accuracy — the higher call is quieter and more precise, so the "
                     "bat gives up carrying power for care",
                         "correct": False,
                         "why": "The switch is about wavelength, not about how loud the call is."},
            {"text": "Range for detail — the lower call reaches further, the higher one reflects "
                     "off something as small as a moth",
                         "correct": True},
            {"text": "Speed for range — the higher call gets back faster",
                         "correct": False,
                         "why": "Both calls travel at the same speed through the same air."},
            {"text": "Nothing — it is simply excitement",
                         "correct": False,
                         "why": "The switch is consistent and well documented, and it matches exactly the "
                    "trade a scanner makes."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h04",
        "band": "harder",
        "text": "An engineer inspecting a weld sees a second pip appear before the one from "
                "the far face of the block. What does that suggest, and what is needed to "
                "turn it into a depth?",
        "options": [
            {"text": "The block is thinner than expected, and no further information is needed",
                         "correct": False,
                         "why": "The far-face pip is still where it was; something new has appeared in front "
                    "of it."},
            {"text": "The probe is faulty, and it should be replaced before any reading is taken, "
                     "because a second pip is always an instrument fault",
                         "correct": False,
                         "why": "A fault would not produce a pip at a consistent, repeatable time."},
            {"text": "Something inside is reflecting the pulse, and the speed of sound in that "
                     "material is needed to convert its timing into a depth",
                         "correct": True},
            {"text": "The pulse has been absorbed partway through, and the timing gives the depth "
                     "directly",
                         "correct": False,
                         "why": "Absorbed sound sends nothing back. And the raw timing gives the whole path, "
                    "which still has to be halved."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e05",
        "band": "easier",
        "text": "A pulse of ultrasound is reflected at…",
        "options": [
            {"text": "the surface of the probe only",
                         "correct": False,
                         "why": "The probe sends it in; the reflections that matter come from inside the "
                    "material."},
            {"text": "any point where the material gets warmer",
                         "correct": False,
                         "why": "Temperature changes the speed a little, but a reflection needs a boundary."},
            {"text": "the point where its energy runs out",
                         "correct": False,
                         "why": "A pulse fading away leaves nothing to reflect; a boundary is what sends it "
                    "back."},
            {"text": "a boundary between two different materials",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s05",
        "band": "standard",
        "text": "A pulse is sent into a block and reflects off something 90 mm down. What "
                "total distance does it travel?",
        "options": [
            {"text": "90 mm",
                         "correct": False,
                         "why": "That is the journey down only; the echo has to come back to the probe."},
            {"text": "45 mm",
                         "correct": False,
                         "why": "That halves the depth instead of doubling it — the halving comes later, when "
                    "finding the depth."},
            {"text": "180 mm",
                         "correct": True},
            {"text": "8100 mm",
                         "correct": False,
                         "why": "That is 90 × 90. The two journeys are added, not multiplied."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h05",
        "band": "harder",
        "text": "A pulse in steel at about 5000 m/s returns to the probe 0.040 ms after it "
                "left. How deep is the reflector?",
        "options": [
            {"text": "200 mm",
                         "correct": False,
                         "why": "That is the whole path of 0.20 m; the reflector is half of it down."},
            {"text": "100 mm",
                         "correct": True},
            {"text": "0.2 mm",
                         "correct": False,
                         "why": "That reads the milliseconds as seconds, making the answer a thousand times "
                    "too small."},
            {"text": "125 000 mm",
                         "correct": False,
                         "why": "That is 5000 ÷ 0.040, dividing where the calculation multiplies."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e06",
        "band": "easier",
        "text": "A scanning probe is described as working at 5 MHz. How many "
                "hertz is that?",
        "options": [
            {"text": "5 000 000 Hz",
                         "correct": True},
            {"text": "5000 Hz",
                         "correct": False,
                         "why": "5000 Hz is 5 kHz. A megahertz is a thousand times bigger than a kilohertz, "
                    "so 5 MHz is a thousand times more than this."},
            {"text": "500 Hz",
                         "correct": False,
                         "why": "500 Hz is an ordinary audible tone, ten thousand times smaller than the 5 MHz asked about here."},
            {"text": "5 000 000 000 Hz",
                         "correct": False,
                         "why": "That is 5 GHz, a thousand megahertz. A megahertz is a million hertz, not a "
                    "thousand million."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e07",
        "band": "easier",
        "text": "Like any other sound, ultrasound…",
        "options": [
            {"text": "crosses empty space easily, which is how a scanner reaches deep "
                     "inside a body",
                         "correct": False,
                         "why": "No sound crosses empty space. A scanner works because a body is full of "
                    "material for the pulse to travel through."},
            {"text": "needs a material to travel through, and cannot cross empty space",
                         "correct": True},
            {"text": "travels a good deal faster than audible sound through the same "
                     "material",
                         "correct": False,
                         "why": "Every frequency of sound travels at the same speed through the same "
                    "material; ultrasound is not the quicker of the two."},
            {"text": "is stopped completely by any solid material it happens to meet",
                         "correct": False,
                         "why": "Sound travels through solids very well, which is exactly why an engineer "
                    "can send ultrasound into a steel block at all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e08",
        "band": "easier",
        "text": "In a given material, ultrasound travels…",
        "options": [
            {"text": "at the speed of light",
                         "correct": False,
                         "why": "Sound of any frequency travels far slower than light; the two are entirely "
                    "different kinds of wave."},
            {"text": "at a fixed 20 000 m/s in any material",
                         "correct": False,
                         "why": "There is no such fixed speed; the speed of sound depends on the material it "
                    "is travelling through."},
            {"text": "at that material's speed of sound",
                         "correct": True},
            {"text": "faster than audible sound in the same material",
                         "correct": False,
                         "why": "Every frequency of sound travels at the same speed through the same "
                    "material; ultrasound is not faster."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e09",
        "band": "easier",
        "text": "An ultrasound pulse travelling through a material meets a boundary with a "
                "different material. What happens?",
        "options": [
            {"text": "It passes through every boundary without reflecting",
                         "correct": False,
                         "why": "A boundary between two different materials is exactly where some of a pulse "
                    "reflects."},
            {"text": "It is absorbed completely at the first boundary it meets, leaving nothing to come back",
                         "correct": False,
                         "why": "Some of the pulse reflects at the boundary; it is not simply absorbed and "
                    "gone."},
            {"text": "It reflects wherever it meets a boundary between two materials",
                         "correct": True},
            {"text": "It reflects only at a boundary between two solids",
                         "correct": False,
                         "why": "A boundary of any two materials — solid, liquid or gas — reflects some of "
                    "the pulse, not solids alone."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e10",
        "band": "easier",
        "text": "An ultrasonic cleaning bath and a physiotherapy machine are both examples of "
                "what kind of ultrasound use?",
        "options": [
            {"text": "an information use",
                         "correct": False,
                         "why": "An information use is run at as low a power as possible; both of these "
                    "devices rely on delivering a good deal of energy instead."},
            {"text": "an energy use",
                         "correct": True},
            {"text": "a communication use",
                         "correct": False,
                         "why": "Neither device is sending or receiving a message; both are delivering energy "
                    "into an object or the body."},
            {"text": "a measurement use",
                         "correct": False,
                         "why": "Neither device is timing an echo to measure anything; both simply deliver "
                    "energy."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e11",
        "band": "easier",
        "text": "Which of these is an INFORMATION use of ultrasound?",
        "options": [
            {"text": "an ultrasonic cleaning bath",
                         "correct": False,
                         "why": "A cleaning bath uses the energy the wave carries, not the information it can "
                    "bring back."},
            {"text": "a medical scan",
                         "correct": True},
            {"text": "a physiotherapy treatment",
                         "correct": False,
                         "why": "Physiotherapy uses the energy ultrasound carries to warm tissue, not "
                    "information brought back by an echo."},
            {"text": "an industrial cutting tool",
                         "correct": False,
                         "why": "Cutting relies on delivered energy, not on timing an echo for information."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e12",
        "band": "easier",
        "text": "A flaw sits 15 mm beneath the probe face. Once the pulse has gone down to "
                "the flaw and come back again, what total distance has it covered?",
        "options": [
            {"text": "15 mm",
                         "correct": False,
                         "why": "That is only the downward leg; the pulse still has to travel back up to the "
                    "probe."},
            {"text": "30 mm",
                         "correct": True},
            {"text": "60 mm",
                         "correct": False,
                         "why": "That is four times the depth; the journey has two equal legs, not four."},
            {"text": "7.5 mm",
                         "correct": False,
                         "why": "That halves the depth instead of doubling it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e13",
        "band": "easier",
        "text": "In the flaw gauge, a reflector is moved to twice its original depth in the "
                "same block of steel. What happens to the total path the pulse must travel, "
                "down and back?",
        "options": [
            {"text": "It stays the same, since the material has not changed",
                         "correct": False,
                         "why": "The path depends on the depth as well as the material; doubling the depth "
                    "doubles the path."},
            {"text": "It also doubles",
                         "correct": True},
            {"text": "It halves",
                         "correct": False,
                         "why": "A greater depth means a longer path, not a shorter one."},
            {"text": "It becomes four times as long",
                         "correct": False,
                         "why": "The path has two equal legs, down and back; doubling the depth doubles each "
                    "leg, not quadruples the total."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e14",
        "band": "easier",
        "text": "About how fast does ultrasound travel through steel?",
        "options": [
            {"text": "about 5000 m/s",
                         "correct": True},
            {"text": "about 340 m/s",
                         "correct": False,
                         "why": "That is the speed of sound in air, far slower than in a solid like steel."},
            {"text": "about 1500 m/s",
                         "correct": False,
                         "why": "That is closer to the speed of sound in water; steel carries sound a good "
                    "deal faster."},
            {"text": "about 300 000 000 m/s",
                         "correct": False,
                         "why": "That is the speed of light, not of sound in any material."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e15",
        "band": "easier",
        "text": "About how fast does ultrasound travel through water?",
        "options": [
            {"text": "about 5000 m/s",
                         "correct": False,
                         "why": "That is closer to the speed of sound in steel; water is a good deal slower."},
            {"text": "about 6300 m/s",
                         "correct": False,
                         "why": "That is closer to the speed of sound in aluminium, the fastest of the "
                    "materials in this lesson."},
            {"text": "about 1500 m/s",
                         "correct": True},
            {"text": "about 340 m/s",
                         "correct": False,
                         "why": "That is the speed of sound in air; water carries sound a good deal faster "
                    "than that."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e16",
        "band": "easier",
        "text": "A probe sends its ultrasound into a block as a short pulse rather "
                "than as a continuous tone, mainly so that…",
        "options": [
            {"text": "the pulse travels through the block faster than a continuous tone "
                     "would manage",
                         "correct": False,
                         "why": "Speed is set by the material, not by how long the sound lasts; a pulse and "
                    "a tone travel through the same steel at the same speed."},
            {"text": "the probe draws less electricity over a working day in the workshop",
                         "correct": False,
                         "why": "Saving power is not the reason; without a quiet gap after the pulse there "
                    "would be no way to time an echo at all."},
            {"text": "there is a quiet gap afterwards in which the returning echo can be "
                     "picked out on its own",
                         "correct": True},
            {"text": "a pulse reflects at boundaries that a continuous tone would pass "
                     "straight through",
                         "correct": False,
                         "why": "Both reflect at exactly the same boundaries; what a pulse adds is a clear "
                    "start and finish to time the echo from."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e17",
        "band": "easier",
        "text": "After sending a pulse into a block, what listens for the returning echo?",
        "options": [
            {"text": "a second probe held against the far side of the block",
                         "correct": False,
                         "why": "Only one probe is used; it listens with the same face it sent the pulse "
                    "from."},
            {"text": "the probe itself, using the same face it sent the pulse from",
                         "correct": True},
            {"text": "a microphone held some short distance away from the block instead",
                         "correct": False,
                         "why": "No separate microphone is needed; the probe both sends and listens."},
            {"text": "the operator's own ear, placed against the block",
                         "correct": False,
                         "why": "Ultrasound is above the human hearing range, so an ear could not hear it "
                    "even pressed against the block."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e18",
        "band": "easier",
        "text": "How does a flaw gauge work out how deep a reflector is?",
        "options": [
            {"text": "measuring how warm the block becomes as the pulse passes through it",
                         "correct": False,
                         "why": "Warming is not part of how the gauge finds a depth; it uses timing instead."},
            {"text": "timing how long it takes an echo to return",
                         "correct": True},
            {"text": "watching the block gradually change its colour",
                         "correct": False,
                         "why": "Ultrasound testing does not rely on any colour change in the material."},
            {"text": "listening for a change in pitch",
                         "correct": False,
                         "why": "The pulse's frequency does not change on reflection; depth is found from "
                    "timing, not pitch."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e19",
        "band": "easier",
        "text": "Before a scan, gel is put between the probe and the skin. What is the gel "
                "actually for?",
        "options": [
            {"text": "the gel lubricates the probe so it can be pressed harder",
                         "correct": False,
                         "why": "Easier sliding is a side benefit; the real job of the gel is about what "
                    "happens to the pulse, not comfort."},
            {"text": "the gel cools the skin so the scan is more comfortable",
                         "correct": False,
                         "why": "Cooling is not the gel's purpose here; it is there to let the pulse into the "
                    "body at all."},
            {"text": "the gel makes the ultrasound pulse travel faster",
                         "correct": False,
                         "why": "The gel does not speed the pulse up; it removes an air gap that would "
                    "otherwise block it."},
            {"text": "the gel removes the air between the probe and the skin",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e20",
        "band": "easier",
        "text": "An engineer checks a finished steel weld for hidden cracks with an "
                "ultrasound probe, rather than cutting a sample out of it. The "
                "advantage of the ultrasound check is that…",
        "options": [
            {"text": "the probe repairs any crack it finds as it is passed over the weld",
                         "correct": False,
                         "why": "A probe only sends a pulse and times what comes back; repairing a crack is "
                    "a separate job altogether."},
            {"text": "it removes the need to know the speed of sound in that particular "
                     "steel",
                         "correct": False,
                         "why": "The speed in that steel is exactly what turns an echo's timing into a "
                    "depth, so the check cannot be done without it."},
            {"text": "the weld is checked without being damaged, so it can stay in service "
                     "afterwards",
                         "correct": True},
            {"text": "the steel is left a little stronger each time a pulse passes through "
                     "it",
                         "correct": False,
                         "why": "A low-power pulse changes nothing about the metal; it simply reflects at "
                    "the boundaries it meets and comes back."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e21",
        "band": "easier",
        "text": "Compared with an X-ray, what is a genuine advantage of an ultrasound scan?",
        "options": [
            {"text": "a completely silent, motionless picture",
                         "correct": False,
                         "why": "An ultrasound picture is assembled from many moving echoes; silence and stillness are not the advantage here."},
            {"text": "an image that never needs a trained operator",
                         "correct": False,
                         "why": "A trained operator is still needed to hold the probe and interpret the "
                    "picture; this is not a genuine advantage."},
            {"text": "no cutting and no ionising radiation",
                         "correct": True},
            {"text": "a picture that costs nothing to produce",
                         "correct": False,
                         "why": "Scanning equipment and staff time both have a real cost, so cost is not the advantage here."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e22",
        "band": "easier",
        "text": "Physiotherapy uses the energy ultrasound carries to help treat…",
        "options": [
            {"text": "broken bones that need to be reset",
                         "correct": False,
                         "why": "Resetting a broken bone is a job for a doctor, not for ultrasound treatment."},
            {"text": "a patient's blood pressure",
                         "correct": False,
                         "why": "Blood pressure is not treated with ultrasound energy in this lesson's "
                    "description."},
            {"text": "stiff joints and strained muscles",
                         "correct": True},
            {"text": "a wound that needs stitching closed",
                         "correct": False,
                         "why": "Closing a wound is a job for stitches, not for ultrasound treatment."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e23",
        "band": "easier",
        "text": "A microphone turns the pattern in an arriving sound wave into…",
        "options": [
            {"text": "a beam of light with the same pattern in it",
                         "correct": False,
                         "why": "A microphone's output is electrical, not a beam of light."},
            {"text": "a jet of air with the same pattern in it",
                         "correct": False,
                         "why": "A microphone converts the pattern into an electrical signal, not a moving "
                    "jet of air."},
            {"text": "a changing magnetic field carrying the same pattern within it",
                         "correct": False,
                         "why": "The output a microphone produces is a changing voltage, not a magnetic "
                    "field."},
            {"text": "a changing voltage with the same pattern in it",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e24",
        "band": "easier",
        "text": "Pick the true statement out of these four, about how ultrasound actually "
                "behaves.",
        "options": [
            {"text": "it can travel through a total vacuum",
                         "correct": False,
                         "why": "No sound travels through a vacuum; ultrasound is no exception."},
            {"text": "it needs no boundary to reflect from",
                         "correct": False,
                         "why": "Ultrasound reflects exactly where an ordinary sound wave would, at a "
                    "boundary between materials."},
            {"text": "it obeys the same ordinary rules as any other sound",
                         "correct": True},
            {"text": "it travels a good deal faster than ordinary audible sound",
                         "correct": False,
                         "why": "Every frequency travels at the same speed through the same material; "
                    "ultrasound is not faster."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e25",
        "band": "easier",
        "text": "A typical medical scanner operates at roughly…",
        "options": [
            {"text": "about 20 Hz to 20 000 Hz",
                         "correct": False,
                         "why": "That is the ordinary human hearing range; a scanner uses frequencies far "
                    "above it."},
            {"text": "about 200 Hz to 2000 Hz",
                         "correct": False,
                         "why": "That range sits comfortably inside ordinary human hearing, far below a "
                    "scanner's operating frequencies."},
            {"text": "about 2 000 000 Hz to 15 000 000 Hz",
                         "correct": True},
            {"text": "about 20 000 000 000 Hz and above",
                         "correct": False,
                         "why": "That is a thousand times higher than a real scanner's operating frequencies."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e26",
        "band": "easier",
        "text": "A reflector sits 200 mm below the probe. What is the total distance the "
                "pulse travels, down and back?",
        "options": [
            {"text": "100 mm",
                         "correct": False,
                         "why": "That is the one-way depth, halved; the total path includes the return "
                    "journey too."},
            {"text": "200 mm",
                         "correct": False,
                         "why": "That is only the downward leg; the pulse still has to travel back to the "
                    "probe."},
            {"text": "400 mm",
                         "correct": True},
            {"text": "800 mm",
                         "correct": False,
                         "why": "That is four times the depth; the journey has two equal legs, not four."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e27",
        "band": "easier",
        "text": "Of steel, water and aluminium, which carries ultrasound fastest?",
        "options": [
            {"text": "steel, at about 5000 m/s",
                         "correct": False,
                         "why": "Aluminium carries ultrasound faster still, at about 6300 m/s."},
            {"text": "water, at about 1500 m/s",
                         "correct": False,
                         "why": "Water is the slowest of the three materials given in this lesson, not the "
                    "fastest."},
            {"text": "aluminium, at about 6300 m/s",
                         "correct": True},
            {"text": "all three carry it at exactly the same speed",
                         "correct": False,
                         "why": "The three materials carry ultrasound at clearly different speeds, from about "
                    "1500 to about 6300 m/s."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e28",
        "band": "easier",
        "text": "An inspector sets the reflector depth control on a training rig to 30 mm. "
                "How far, in total, will the displayed pulse travel down to the reflector and "
                "back again?",
        "options": [
            {"text": "120 mm",
                         "correct": False,
                         "why": "That is four times the depth; the journey has two equal legs, not four."},
            {"text": "30 mm",
                         "correct": False,
                         "why": "That is only the downward leg; the pulse still has to travel back up."},
            {"text": "240 mm",
                         "correct": False,
                         "why": "That is eight times the depth, far more than the two equal legs the journey "
                    "actually has."},
            {"text": "60 mm",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e29",
        "band": "easier",
        "text": "A gauge is calibrated assuming a slow material, but the block being tested "
                "actually carries ultrasound faster than that. For a reflector at a given "
                "true depth, what happens to the echo's return TIME compared with what the "
                "gauge was calibrated to expect?",
        "options": [
            {"text": "the echo would return later than the gauge itself expects",
                         "correct": False,
                         "why": "A faster actual material moves the pulse there and back more quickly, not "
                    "more slowly, for the same depth."},
            {"text": "the echo would return sooner than the gauge expects",
                         "correct": True},
            {"text": "no echo would ever return to the probe",
                         "correct": False,
                         "why": "A boundary still reflects a pulse whatever the material's speed; an echo "
                    "does return, just sooner than expected."},
            {"text": "the reading would come out exactly correct regardless",
                         "correct": False,
                         "why": "Using the wrong speed to interpret a real echo time is exactly what causes a "
                    "gauge to misread a depth."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-e30",
        "band": "easier",
        "text": "A device produces a wave at 40 000 Hz, well above human hearing. What is "
                "this wave?",
        "options": [
            {"text": "it is a beam of invisible light",
                         "correct": False,
                         "why": "Light is a completely different kind of wave from sound; a 40 000 Hz wave "
                    "here is still a sound wave."},
            {"text": "it is a stream of tiny solid particles thrown out by the device, rather than a genuine wave",
                         "correct": False,
                         "why": "It is a genuine pressure wave passing through a material, not a stream of "
                    "particles."},
            {"text": "it is a kind of electricity passed through the body rather than a wave of any sort",
                         "correct": False,
                         "why": "It is a mechanical sound wave, not an electrical signal."},
            {"text": "it is ordinary sound above the human hearing range, nothing more exotic",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s06",
        "band": "standard",
        "text": "A reflector sits 100 mm down in both a steel block and an aluminium block. "
                "In which block would the two pips on the screen sit closer together, and "
                "why?",
        "options": [
            {"text": "The aluminium block, because sound travels faster there, so the echo returns "
                     "in less time",
                         "correct": True},
            {"text": "The steel block, because steel is the denser of the two metals, and denser "
                     "materials show a shorter gap between pips",
                         "correct": False,
                         "why": "Density on its own does not set the gap; it is aluminium's higher speed of "
                    "sound that brings the pips closer together here."},
            {"text": "Neither — the two blocks would show exactly the same gap, since the "
                     "reflector sits at the same depth in both",
                         "correct": False,
                         "why": "The depth is the same, but the two metals carry sound at different speeds, "
                    "so the TIME between the pips differs even though the depth does not."},
            {"text": "The steel block, because aluminium reflects far more of the pulse back than "
                     "steel does, giving a taller but more widely spaced pair of pips",
                         "correct": False,
                         "why": "How much reflects back changes the height of a pip, not the time gap between "
                    "the two of them."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s07",
        "band": "standard",
        "text": "An inspector tests the same depth of 100 mm first in a water tank, then in a "
                "steel girder. On which test does the sent-and-received pip pair end up "
                "furthest apart, and why?",
        "options": [
            {"text": "The steel block, since steel is a solid and water is only a liquid",
                         "correct": False,
                         "why": "Being a solid is not what decides the gap; water carries sound more slowly "
                    "than steel, which is what matters here."},
            {"text": "The water tank, because sound travels more slowly through water than through "
                     "steel, so the echo takes longer to return",
                         "correct": True},
            {"text": "Neither — the gap between the two pips depends on the depth alone, and the depth is the same 100 mm in both of the tests described",
                         "correct": False,
                         "why": "Depth being equal does not make the TIME equal, because the two materials "
                    "carry sound at different speeds."},
            {"text": "The water tank, because water absorbs almost all of the pulse, leaving only "
                     "a very faint returning pip that appears to sit further away",
                         "correct": False,
                         "why": "How faint a pip looks is about how much comes back, not about when it "
                    "arrives on the timing axis."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s08",
        "band": "standard",
        "text": "The flaw gauge's timing window is fixed at 0.30 ms, rather than "
                "automatically stretching to fit whichever material is chosen. Explain why a "
                "fixed window is useful here.",
        "options": [
            {"text": "It is fixed because a burst of ultrasound lasts exactly 0.30 ms in any material, and no equipment can make one any longer or any shorter",
                         "correct": False,
                         "why": "A pulse's duration is a choice made by the equipment, not a fixed property "
                    "of ultrasound itself."},
            {"text": "It is fixed so that every material on the selector shows exactly the same size of gap between its two pips, whatever speed it carries sound at",
                         "correct": False,
                         "why": "The window's SIZE is fixed, but the GAP between the pips still changes with "
                    "the material's speed — that changing gap is the whole point of the display."},
            {"text": "It lets a slower material's wider pip gap be compared directly against a "
                     "faster material's narrower one, on the very same scale",
                         "correct": True},
            {"text": "It is fixed because a stretching window would damage the screen over "
                     "repeated use",
                         "correct": False,
                         "why": "A stretching or fixed display is a design choice about what is easy to read, "
                    "not a matter of protecting the screen from damage."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s09",
        "band": "standard",
        "text": "An echo returns 0.020 ms after a pulse is sent into aluminium, at about 6300 "
                "m/s. How deep is the reflector?",
        "options": [
            {"text": "About 126 mm",
                         "correct": False,
                         "why": "That is the whole path, down and back; the reflector's depth is half of it."},
            {"text": "About 31.5 mm",
                         "correct": False,
                         "why": "That halves the correct depth a second time."},
            {"text": "About 315 000 mm",
                         "correct": False,
                         "why": "That treats 0.020 ms as if it were 0.020 s — check the units."},
            {"text": "About 63 mm",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s10",
        "band": "standard",
        "text": "An engineer says that because ultrasound reflects at any boundary between "
                "materials, it can find a hairline crack in a steel girder even if the crack "
                "is completely filled with more steel. Evaluate this claim.",
        "options": [
            {"text": "The claim is wrong — a crack filled with the same material is not a boundary "
                     "at all, so there is nothing there for the pulse to reflect off",
                         "correct": True},
            {"text": "The claim is right, since ultrasound reflects off any crack regardless of "
                     "what, if anything, fills it",
                         "correct": False,
                         "why": "A crack only creates a boundary if what fills it differs from the "
                    "surrounding material; steel filled with more steel is no boundary at all."},
            {"text": "The claim is right, because a crack always contains air, and air reflects strongly whatever the surrounding material is",
                         "correct": False,
                         "why": "The crack in this scenario is described as filled with more steel, not air, "
                    "so there is no air boundary to reflect from here."},
            {"text": "The claim cannot be judged without first knowing how long the crack is",
                         "correct": False,
                         "why": "Length is not the deciding factor; whether there is a genuine boundary "
                    "between two DIFFERENT materials is what decides whether anything reflects."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s11",
        "band": "standard",
        "text": "Does turning up the power of a diagnostic ultrasound scanner make its "
                "picture more accurate?",
        "options": [
            {"text": "Yes — a louder pulse brings back more accurate information about whatever it strikes",
                         "correct": False,
                         "why": "Detail in a scan comes mainly from a short wavelength, not from how much "
                    "power the pulse carries."},
            {"text": "Not necessarily — a scan is an information use run at as low a power as will "
                     "still work, so more power is not the same as more detail",
                         "correct": True},
            {"text": "Yes — a scanner is an energy use, so power is exactly what decides how good and how detailed the resulting picture turns out",
                         "correct": False,
                         "why": "A diagnostic scan is an information use, kept at low power on purpose, unlike an energy use such as a cleaning bath."},
            {"text": "No, never — power has no effect whatsoever on how a scanner performs",
                         "correct": False,
                         "why": "Power still matters for whether a usable echo returns at all; the point is "
                    "that MORE power does not automatically mean a MORE accurate picture."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s12",
        "band": "standard",
        "text": "A pulse is sent into a block and the total path recorded is 0.246 m. If the "
                "material is aluminium, at about 6300 m/s, how deep is the reflector, in "
                "millimetres?",
        "options": [
            {"text": "About 246 mm",
                         "correct": False,
                         "why": "That is the whole path in millimetres; the reflector's depth is half of it."},
            {"text": "About 61.5 mm",
                         "correct": False,
                         "why": "That halves the correct depth a second time."},
            {"text": "About 123 mm",
                         "correct": True},
            {"text": "About 24.6 mm",
                         "correct": False,
                         "why": "That treats the path as if it were ten times smaller than 0.246 m actually "
                    "is."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s13",
        "band": "standard",
        "text": "An ultrasonic cleaning bath and a physiotherapy machine both use the energy "
                "ultrasound carries, yet they run at very different powers and are used very "
                "differently. Suggest why a cleaning bath can be far more intense than a "
                "treatment used directly on a patient's body.",
        "options": [
            {"text": "A cleaning bath actually runs at a lower power than a physiotherapy machine, "
                     "not a higher one, contrary to what many people assume",
                         "correct": False,
                         "why": "A cleaning bath's whole job is to shake dirt loose with vigorous bubble "
                    "formation, which needs considerably more intensity than a gentle "
                    "physiotherapy treatment."},
            {"text": "Ultrasound cannot actually damage living tissue at any intensity, so power "
                     "is never a safety concern for a physiotherapy machine either",
                         "correct": False,
                         "why": "Ultrasound at a high enough intensity can heat or otherwise affect living "
                    "tissue, which is exactly why a physiotherapy machine is kept at a gentler "
                    "level than a cleaning bath."},
            {"text": "The two devices are not really using the same kind of wave, despite both "
                     "being called ultrasound",
                         "correct": False,
                         "why": "Both are genuinely ultrasound, ordinary sound above the human range; what "
                    "differs between them is intensity and purpose, not the kind of wave."},
            {"text": "A cleaning bath is treating an object, not living tissue, so intensities "
                     "that would harm a patient are not a safety concern there",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s14",
        "band": "standard",
        "text": "In physiotherapy, ultrasound is absorbed a few centimetres into the tissue "
                "and warms it there. Explain why this can reach a stiff joint more "
                "effectively than simply pressing a warm heat pad on the skin.",
        "options": [
            {"text": "A heat pad mainly warms the surface and relies on that heat spreading "
                     "inward, while ultrasound delivers its energy directly at depth",
                         "correct": True},
            {"text": "A heat pad and ultrasound both warm exactly the same depth of tissue by "
                     "exactly the same amount, so there is no real difference between them",
                         "correct": False,
                         "why": "The whole point of the ultrasound treatment is reaching depth a surface heat "
                    "pad struggles to warm as directly."},
            {"text": "A heat pad cannot warm skin, since heat can only travel through the body "
                     "using ultrasound",
                         "correct": False,
                         "why": "A heat pad plainly does warm the skin; the difference described here is "
                    "about how well the warmth reaches deeper tissue, not whether the skin itself "
                    "gets warm."},
            {"text": "Ultrasound treatment works by cooling the deep tissue rather than warming it, and it is that cooling which relaxes a stiff joint again",
                         "correct": False,
                         "why": "The energy ultrasound delivers is absorbed and turns into warming, not "
                    "cooling, of the tissue it reaches."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s15",
        "band": "standard",
        "text": "Explain why a diagnostic ultrasound scan is considered safe for routine use "
                "on a developing pregnancy, while a high-power industrial cleaning bath is "
                "not something you would want near living tissue.",
        "options": [
            {"text": "A diagnostic scan uses a completely different kind of wave from a cleaning "
                     "bath, even though both are officially given the very same name, ultrasound, "
                     "in every textbook",
                         "correct": False,
                         "why": "Both are genuinely ultrasound, ordinary sound above the human range; the "
                    "real difference between them here is intensity, not the kind of wave."},
            {"text": "A diagnostic scan is deliberately run at a very low power, just enough for a "
                     "usable echo, while a cleaning bath is run at a much higher intensity on "
                     "purpose",
                         "correct": True},
            {"text": "A cleaning bath is actually run just as gently as a diagnostic scan is, so the caution people show around one of them is unnecessary either way",
                         "correct": False,
                         "why": "A cleaning bath is deliberately intense enough to form and collapse bubbles "
                    "that scrub dirt loose, which is a good deal more vigorous than a diagnostic "
                    "scan."},
            {"text": "Living tissue is completely unaffected by ultrasound at any power, so "
                     "neither use ever needs any caution",
                         "correct": False,
                         "why": "Ultrasound at a high enough intensity can affect living tissue, which is "
                    "exactly why diagnostic scanning is deliberately kept at a low power."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s16",
        "band": "standard",
        "text": "A technician applies gel before a scan but leaves a small air bubble trapped "
                "underneath the probe. Predict what this would do to the screen.",
        "options": [
            {"text": "Nothing would change, since a small bubble is far too tiny to reflect any of "
                     "the pulse",
                         "correct": False,
                         "why": "Even a small air bubble is a genuine boundary between two very different "
                    "materials, gel and air, and it would reflect a noticeable part of the pulse."},
            {"text": "The whole screen would go blank, since any air stops the probe working "
                     "completely",
                         "correct": False,
                         "why": "The probe keeps working; the trapped air simply adds an extra boundary the "
                    "pulse meets on its way in, rather than stopping the equipment entirely."},
            {"text": "An extra, unwanted echo would appear, reflected off the boundary at the "
                     "trapped bubble itself",
                         "correct": True},
            {"text": "The bubble would make the picture clearer, since air improves how well a "
                     "probe can see into the body",
                         "correct": False,
                         "why": "Air is exactly what a scan tries to avoid between probe and skin; a trapped "
                    "bubble degrades the picture rather than improving it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s17",
        "band": "standard",
        "text": "A stethoscope and a diagnostic ultrasound scanner are both information uses, "
                "yet one works with ordinary audible sound and the other with ultrasound. "
                "What do they have in common?",
        "options": [
            {"text": "Both deliberately deliver as much energy as possible into the body being "
                     "examined, since more energy means a clearer overall result",
                         "correct": False,
                         "why": "Both are information uses kept at a low power, not energy uses aiming to "
                    "deliver as much power as possible."},
            {"text": "Both work by timing an echo that bounces off an internal boundary",
                         "correct": False,
                         "why": "A stethoscope simply listens to sound already being made inside the body; it "
                    "does not send out its own pulse and time an echo the way a scanner does."},
            {"text": "Both operate at frequencies above the top of the human hearing range, which "
                     "is what makes both of them genuinely ultrasound",
                         "correct": False,
                         "why": "A stethoscope works with ordinary audible sound, well within the human "
                    "range; only the scanner uses ultrasound."},
            {"text": "Both take information carried in a sound wave and turn it into something a "
                     "person can interpret, run at as low a power as still works",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s18",
        "band": "standard",
        "text": "A reflector sits at the same true depth in steel, water and aluminium. Rank "
                "the three materials from the SHORTEST echo return time to the LONGEST.",
        "options": [
            {"text": "Aluminium, then steel, then water",
                         "correct": True},
            {"text": "Water, then steel, then aluminium",
                         "correct": False,
                         "why": "That is the ranking reversed — water is the slowest of the three, so its "
                    "echo takes the longest, not the shortest, to return."},
            {"text": "Steel, then aluminium, and then water",
                         "correct": False,
                         "why": "Aluminium carries ultrasound faster than steel, so aluminium's echo returns "
                    "first, ahead of steel's."},
            {"text": "All three would return in exactly the same time, since the depth is the same "
                     "in every case",
                         "correct": False,
                         "why": "Equal depth does not mean equal time here, because the three materials carry "
                    "ultrasound at three different speeds."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s19",
        "band": "standard",
        "text": "Explain why the probe sends its pulse and listens for the echo using the "
                "same single face, rather than using one face to send and a separate face to "
                "listen.",
        "options": [
            {"text": "A second face is technically impossible to build into any probe",
                         "correct": False,
                         "why": "There is no technical barrier to a second face; the single-face design works "
                    "because the echo simply returns the way it came."},
            {"text": "The echo travels back along the very same path it went out on, so the "
                     "sending face is exactly where the returning pulse arrives",
                         "correct": True},
            {"text": "Using two separate faces would make the pulse travel at a different speed "
                     "through the material, however the two faces happened to be arranged on the "
                     "block",
                         "correct": False,
                         "why": "The speed of the pulse depends on the material it travels through, not on "
                    "how many faces the probe has."},
            {"text": "A second face would be needed only if the block being tested were unusually thick, since a thick block sends its echo back along a different route",
                         "correct": False,
                         "why": "Thickness changes how long the echo takes to return, not whether a second "
                    "face would be needed at all — the echo returns along the same path whatever "
                    "the thickness."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s20",
        "band": "standard",
        "text": "A cleaning bath runs at about 40 000 Hz, while a diagnostic scanner runs at "
                "several million hertz. Suggest why the cleaning bath does not need anywhere "
                "near as high a frequency.",
        "options": [
            {"text": "A higher frequency would be far too weak to shake any dirt at all loose from a surface, however long the cleaning cycle is left running for",
                         "correct": False,
                         "why": "Frequency is not what decides how much energy a wave carries; the cleaning "
                    "bath's job does not depend on using a very high frequency."},
            {"text": "40 000 Hz is actually the highest frequency any ultrasonic device can "
                     "produce",
                         "correct": False,
                         "why": "Diagnostic scanners routinely run at several million hertz, far above 40 000 "
                    "Hz, so it is not a hard upper limit."},
            {"text": "The cleaning bath does not need to pick out fine detail the way a scan does, "
                     "so it can use a much lower, cheaper-to-produce ultrasonic frequency",
                         "correct": True},
            {"text": "A cleaning bath is not really using ultrasound, only an unusually "
                     "low-pitched audible sound that happens to sit just below the human hearing "
                     "range",
                         "correct": False,
                         "why": "40 000 Hz is above the roughly 20 000 Hz top of human hearing, so it "
                    "genuinely is ultrasound."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s21",
        "band": "standard",
        "text": "Would doubling a diagnostic scanner's frequency, on its own, double how much "
                "fine detail its picture can show?",
        "options": [
            {"text": "No, frequency has no connection to how much detail a scan can show",
                         "correct": False,
                         "why": "Frequency sets the wavelength, and a shorter wavelength is exactly what lets "
                    "a scan pick out smaller features."},
            {"text": "No, because doubling the frequency would simply double how loud the picture appears, rather than how detailed it is",
                         "correct": False,
                         "why": "Loudness is a separate property from frequency; raising frequency changes "
                    "wavelength and detail, not loudness."},
            {"text": "Yes, but only because a higher frequency travels faster through the body",
                         "correct": False,
                         "why": "Every frequency travels at the same speed through the same tissue; it is the "
                    "shorter wavelength, not a change in speed, that improves the detail."},
            {"text": "Roughly, yes — a higher frequency gives a shorter wavelength, and a shorter "
                     "wavelength is what lets smaller features reflect and show up",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s22",
        "band": "standard",
        "text": "Published figures for the speed of sound in steel range from about 5000 to "
                "about 5900 m/s, depending on the exact alloy. Explain why a flaw gauge needs "
                "to be calibrated for the SPECIFIC steel being tested, rather than one fixed "
                "steel value.",
        "options": [
            {"text": "Using the wrong value within that range would convert a real echo time into "
                     "a slightly wrong depth, even though the error might be small",
                         "correct": True},
            {"text": "Different steels reflect completely different fractions of the pulse, which "
                     "is the real reason calibration matters",
                         "correct": False,
                         "why": "This lesson's concern with the exact alloy is about the SPEED used to "
                    "convert time into depth, not about how much of the pulse reflects."},
            {"text": "The range given, 5000 to 5900 m/s, is simply a measurement error, and any "
                     "one steel actually has a single exact speed everyone agrees on",
                         "correct": False,
                         "why": "The range reflects a genuine difference between steel alloys, not a "
                    "measurement error to be explained away."},
            {"text": "A gauge only needs recalibrating for a different alloy if the block is "
                     "unusually thick",
                         "correct": False,
                         "why": "The speed used in the calculation matters whatever the thickness; a wrong "
                    "speed shifts every depth reading, not just readings on thick blocks."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s23",
        "band": "standard",
        "text": "A flaw gauge's display is scaled for depths from 0 to 200 mm. What "
                "would you expect to happen, in reality, if a genuine reflector sat "
                "considerably deeper than 200 mm in a real block?",
        "options": [
            {"text": "Ultrasound would be physically unable to reach any reflector beyond 200 mm, "
                     "in any material whatsoever, regardless of the equipment being used",
                         "correct": False,
                         "why": "200 mm is simply the range that display was scaled to; ultrasound itself can reach and return from much greater depths, depending on the equipment and the material."},
            {"text": "A real gauge could still time an echo from it, given enough range; the 0 to 200 mm scale is a limit of that display, not of ultrasound itself",
                         "correct": True},
            {"text": "The reflector would stop being able to create a boundary at that depth",
                         "correct": False,
                         "why": "A boundary between two materials reflects sound whatever its depth; the 200 mm limit belongs to the display, not to the physics."},
            {"text": "The speed of sound in the material would change once the depth passed 200 mm, in exactly the way the display's scale would suggest",
                         "correct": False,
                         "why": "The speed of sound in a given material stays the same throughout it; it does "
                    "not change at some particular depth."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s24",
        "band": "standard",
        "text": "A bat's echolocation call and a hospital's diagnostic scanner are both "
                "information uses of very high-frequency sound. What do they have in common?",
        "options": [
            {"text": "Both use exactly the same frequency, since any genuine echolocation system "
                     "has to operate at one single shared frequency",
                         "correct": False,
                         "why": "A bat's calls and a hospital scanner's pulses operate at quite different "
                    "frequencies; sharing the same PRINCIPLE does not require sharing the same "
                    "number."},
            {"text": "Both deliver as much energy as possible into whatever they are examining",
                         "correct": False,
                         "why": "Both are information uses, and information uses are run at as low a power as "
                    "will still give a usable echo, not as much energy as possible."},
            {"text": "Both send out a pulse and use the timing and pattern of its returning echoes "
                     "to build up information about their surroundings",
                         "correct": True},
            {"text": "Neither one actually reflects off anything; both work by the sound simply "
                     "fading out at the target",
                         "correct": False,
                         "why": "Both rely on genuine reflection at a boundary — a moth for the bat, an "
                    "internal structure for the scanner — timed as an echo."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s25",
        "band": "standard",
        "text": "Someone claims ultrasound \"can pass through anything, which is what makes "
                "scanning possible.\" Evaluate this claim.",
        "options": [
            {"text": "The claim is right, and is exactly why a scanner needs no gel or careful "
                     "positioning of the probe",
                         "correct": False,
                         "why": "Gel and careful positioning matter precisely because ultrasound does NOT "
                    "simply pass through everything — an air gap alone reflects almost the whole "
                    "pulse."},
            {"text": "The claim is right, since a scan works by shining ultrasound all the way through the body and reading what comes out of the far side",
                         "correct": False,
                         "why": "A scan reads reflections that return to the same probe face the pulse left "
                    "from, not whatever reaches the far side of the body."},
            {"text": "The claim cannot be judged without knowing the exact make of scanner being "
                     "used",
                         "correct": False,
                         "why": "The underlying physics — that ultrasound reflects at boundaries rather than "
                    "passing through everything — holds for any scanner, whatever its make."},
            {"text": "The claim is wrong — scanning depends on ultrasound NOT passing through "
                     "everything; it is the reflections at internal boundaries that build the "
                     "picture",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s26",
        "band": "standard",
        "text": "A block has a near face and a far face, and a pulse reflects off both. Which "
                "pip, near or far, would appear on the screen first, and why?",
        "options": [
            {"text": "The near-face pip, since its echo has a shorter path to travel there and "
                     "back than the far face's echo does",
                         "correct": True},
            {"text": "The far-face pip, since the far face is a stronger reflector than the near "
                     "face, following the same reasoning through carefully",
                         "correct": False,
                         "why": "Which pip is stronger changes how tall it looks, not which one arrives first "
                    "— arrival order comes from path length."},
            {"text": "Both pips would arrive at exactly the same moment",
                         "correct": False,
                         "why": "The two echoes travel different total distances, down to the near face and "
                    "back against down to the far face and back, so they arrive at different "
                    "times unless the block has no thickness at all."},
            {"text": "Neither — only one pip can ever appear on the screen at a time",
                         "correct": False,
                         "why": "Both reflections are genuine echoes and both can appear on the screen, "
                    "arriving one after the other."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s27",
        "band": "standard",
        "text": "A pulse takes 0.030 ms to return from a reflector in water, at about 1500 "
                "m/s. How deep is the reflector?",
        "options": [
            {"text": "About 45 mm",
                         "correct": False,
                         "why": "That is the whole path, down and back; the reflector's depth is half of it."},
            {"text": "About 22.5 mm",
                         "correct": True},
            {"text": "About 11.25 mm",
                         "correct": False,
                         "why": "That halves the correct depth a second time."},
            {"text": "About 45 000 mm",
                         "correct": False,
                         "why": "That treats the depth as if it were a thousand times larger than it really "
                    "is — check the units."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s28",
        "band": "standard",
        "text": "A patient asks why the operator moves the probe around on their skin during "
                "a scan instead of holding it still in one place. Suggest a reason, based on "
                "what a single pulse can reveal.",
        "options": [
            {"text": "Moving the probe is needed to keep the gel evenly spread, and has nothing "
                     "whatsoever to do with the picture the machine ends up building up on screen",
                         "correct": False,
                         "why": "Spreading gel is a side benefit; the main reason for moving the probe is to "
                    "build up information from more than one narrow line into the body."},
            {"text": "A still probe would eventually stop producing any pulses after a few seconds",
                         "correct": False,
                         "why": "A probe kept still would carry on producing pulses perfectly well; the issue "
                    "is that it would only ever see one narrow line into the body."},
            {"text": "A single position only sends pulses along one narrow line into the body, so "
                     "moving the probe builds up echoes from many lines to form a wider picture",
                         "correct": True},
            {"text": "Moving the probe changes the speed of sound in the tissue being examined",
                         "correct": False,
                         "why": "The speed of sound in a given tissue is a property of that tissue, not "
                    "something changed by moving the probe over it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s29",
        "band": "standard",
        "text": "Explain why an ultrasonic cleaning bath can reach into narrow gaps and tiny "
                "crevices of an object in a way that scrubbing with a brush cannot.",
        "options": [
            {"text": "Ultrasound is able to pass straight through the solid object and clean it "
                     "thoroughly from the inside out, wherever the dirt happens to be sitting",
                         "correct": False,
                         "why": "The cleaning action happens where the liquid and its bubbles reach the "
                    "object's surface, not by the sound passing through the solid object itself."},
            {"text": "A brush is physically incapable of ever removing dirt from any metal object",
                         "correct": False,
                         "why": "A brush can clean an accessible flat surface perfectly well; its limitation "
                    "is reaching into narrow gaps, not cleaning metal in general."},
            {"text": "The bath heats the object so strongly that dirt simply burns away on its own",
                         "correct": False,
                         "why": "The cleaning action described here comes from tiny bubbles forming and "
                    "collapsing against the surface, not from heating the object."},
            {"text": "The sound wave, and the tiny bubbles it forms, can reach anywhere the liquid "
                     "itself can reach, including gaps far too narrow for bristles",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-s30",
        "band": "standard",
        "text": "A manufacturer claims their new probe design \"needs no gel at all, because "
                "it uses a special kind of ultrasound that passes straight through air.\" "
                "Evaluate this claim.",
        "options": [
            {"text": "Very unlikely — an air gap between a probe and the skin reflects almost the "
                     "whole pulse straight back, whatever kind of ultrasound is being used",
                         "correct": True},
            {"text": "Very likely true, since ultrasound is a special kind of wave able to cross "
                     "an air gap without any difficulty, unlike the ordinary sound used in "
                     "everyday hearing",
                         "correct": False,
                         "why": "Ultrasound behaves like any other sound at a probe-to-air boundary; there is "
                    "no special version of it that ignores this reflection."},
            {"text": "Very likely true, provided the probe is pressed hard enough against the skin",
                         "correct": False,
                         "why": "Pressing harder does not remove the physics of the boundary; a genuine air "
                    "gap still reflects almost the whole pulse, however firmly the probe is "
                    "pressed."},
            {"text": "The claim cannot be evaluated without first testing the exact probe being "
                     "sold",
                         "correct": False,
                         "why": "The relevant physics — that a probe-to-air boundary reflects almost the "
                    "whole pulse — applies to any probe design, not only a particular one."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h06",
        "band": "harder",
        "text": "A probe fires a pulse into an aluminium block and the echo returns 0.040 ms "
                "later. Sound travels at about 6300 m/s in aluminium. How deep is the "
                "reflector, to the nearest millimetre?",
        "options": [
            {"text": "About 126 mm, since the whole down-and-back path works out at about 252 mm "
                     "and the reflector sits halfway along it",
                         "correct": True},
            {"text": "About 252 mm, taking the whole down-and-back path as if it were the depth on "
                     "its own, without halving it",
                         "correct": False,
                         "why": "252 mm is the whole path, out and back; the reflector's actual depth is half "
                    "of that distance."},
            {"text": "About 63 mm, halving the correct answer a second time as though the journey "
                     "had two halvings rather than one overall",
                         "correct": False,
                         "why": "Only one halving is needed, converting the whole path into the one-way "
                    "depth; a second halving goes too far."},
            {"text": "About 6300 mm, treating the given time as though it were measured in whole "
                     "seconds instead of thousandths of a second",
                         "correct": False,
                         "why": "0.040 ms is a small fraction of a second; reading it as seconds inflates the "
                    "answer enormously."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h07",
        "band": "harder",
        "text": "Two reflectors sit only 1 mm apart in a block, and a probe testing at 1 MHz "
                "cannot tell them apart on screen, while a probe at 10 MHz clearly resolves "
                "both. Explain this difference, using how wavelength relates to frequency.",
        "options": [
            {"text": "The 10 MHz probe is simply louder, and a louder pulse resolves finer detail "
                     "than a quieter one at any frequency",
                         "correct": False,
                         "why": "Loudness is a separate property, amplitude, from frequency; the detail "
                    "difference here comes from wavelength, not from how loud either pulse is."},
            {"text": "The 10 MHz probe has a far shorter wavelength, small enough to reflect "
                     "usefully off features as close together as 1 mm, unlike the longer "
                     "wavelength at 1 MHz",
                         "correct": True},
            {"text": "The 10 MHz probe travels faster through the block, so its pulse arrives at the two reflectors at two clearly separated moments rather than at one single moment",
                         "correct": False,
                         "why": "Every frequency of ultrasound travels at the same speed through the same "
                    "material; speed is not what separates the two reflectors here."},
            {"text": "The 1 MHz probe cannot produce two separate pulses, so it detects one reflector at a time",
                         "correct": False,
                         "why": "The 1 MHz probe sends one ordinary pulse, just as the 10 MHz one does; its "
                    "limitation is a longer wavelength, not an inability to produce more than one "
                    "pulse."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h08",
        "band": "harder",
        "text": "A technician says a 1 MHz probe, whose wavelength in soft tissue works out "
                "at about 1.5 mm, should have no trouble showing a feature 1 cm (10 mm) "
                "across. Evaluate this reasoning.",
        "options": [
            {"text": "Unreasonable — a feature has to be SMALLER than the probe's wavelength before it can reflect anything at all, so a 10 mm feature is far too big at 1.5 mm",
                         "correct": False,
                         "why": "The relationship runs the other way: a feature needs to be roughly the wavelength or larger to reflect usefully, not smaller."},
            {"text": "Unreasonable — wavelength has no bearing whatsoever on which features a "
                     "probe can detect",
                         "correct": False,
                         "why": "Wavelength is exactly what sets how much detail a probe can pick out."},
            {"text": "Reasonable — a wave generally reflects usefully off a feature roughly its "
                     "own wavelength or larger, and 10 mm is a good deal larger than 1.5 mm",
                         "correct": True},
            {"text": "Impossible to judge without first knowing exactly how loud the 1 MHz pulse "
                     "is",
                         "correct": False,
                         "why": "The comparison being judged here is between wavelength and feature size; "
                    "loudness does not come into that particular comparison."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h09",
        "band": "harder",
        "text": "A bat closing in on a moth switches from a lower call to a much higher one, "
                "while a hospital scanner looking deep into a body uses a LOWER frequency "
                "than one looking just under the skin. Explain what these two situations have "
                "in common.",
        "options": [
            {"text": "Both simply turn the volume up when more detail is needed, since louder "
                     "pulses show finer detail",
                         "correct": False,
                         "why": "The trade described in both cases is about frequency and wavelength, not "
                    "about turning the volume up or down."},
            {"text": "Neither situation is really about detail — both are simply choosing "
                     "whichever frequency happens to be available at the time",
                         "correct": False,
                         "why": "Both choices are deliberate trade-offs between how far the pulse reaches and "
                    "how much detail it can resolve, not an arbitrary pick."},
            {"text": "Both are using two entirely different kinds of wave, since a bat's call "
                     "cannot be compared with a hospital scanner's pulse",
                         "correct": False,
                         "why": "Both are genuinely the same kind of thing, ultrasound pulses reflecting off "
                    "boundaries, despite being produced by very different sources."},
            {"text": "Both trade range for detail — a lower frequency reaches further but shows "
                     "less, a higher one shows more but does not reach as far",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h10",
        "band": "harder",
        "text": "A parent asks why their child's scan used ultrasound rather than an X-ray, "
                "when an X-ray might show more detail. Explain a genuine reason a doctor "
                "might prefer ultrasound here.",
        "options": [
            {"text": "Ultrasound involves no ionising radiation, which matters especially for "
                     "repeated scans or scans on children and unborn babies",
                         "correct": True},
            {"text": "Ultrasound is more detailed than an X-ray for absolutely every part of the "
                     "body",
                         "correct": False,
                         "why": "Ultrasound does not always beat an X-ray on detail; its real advantage here is avoiding ionising radiation, not better detail in every case."},
            {"text": "X-rays cannot pass through the human body at all, so ultrasound is the only option available",
                         "correct": False,
                         "why": "X-rays plainly do pass through the body, which is exactly how an X-ray image "
                    "is formed; that is not the reason to prefer ultrasound here."},
            {"text": "Ultrasound machines are incapable of producing any picture of an unborn baby",
                         "correct": False,
                         "why": "Ultrasound scanning of an unborn baby is one of its most familiar uses, "
                    "producing a real picture from the returning echoes."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h11",
        "band": "harder",
        "text": "A pulse takes 0.024 ms to return from a reflector in a water tank, at about "
                "1500 m/s. A second pulse takes 0.080 ms to return from a reflector in a "
                "steel block, at about 5000 m/s. Which reflector sits deeper?",
        "options": [
            {"text": "The one in water, since water is the slower material and a slower material "
                     "gives the deeper reading for a given time",
                         "correct": False,
                         "why": "A slower material means a SHORTER distance is covered in a given time, not a "
                    "deeper one; the steel reflector, worked out properly, is the deeper of the "
                    "two here."},
            {"text": "The one in steel, at about 200 mm, compared with about 18 mm for the one in "
                     "water",
                         "correct": True},
            {"text": "They sit at exactly the same depth, since both times were given to two "
                     "significant figures",
                         "correct": False,
                         "why": "Working through both calculations gives clearly different depths, about 18 "
                    "mm and about 200 mm, not the same figure."},
            {"text": "It cannot be worked out without first knowing how wide each block is",
                         "correct": False,
                         "why": "Depth is found from the time and the speed of sound alone; the width of the "
                    "surrounding block does not enter the calculation."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h12",
        "band": "harder",
        "text": "Explain why an ultrasonic cleaning bath does not need anywhere near the "
                "frequency a medical scanner uses, even though both rely on ultrasound.",
        "options": [
            {"text": "A cleaning bath actually needs a far higher frequency than a scanner, not a "
                     "lower one, since more vigorous cleaning demands it",
                         "correct": False,
                         "why": "This lesson gives a cleaning bath's frequency as around 40 000 Hz, well "
                    "below a scanner's several million hertz."},
            {"text": "Frequency has no effect on how well ultrasound cleans or scans anything",
                         "correct": False,
                         "why": "Frequency sets the wavelength, which is directly relevant to a scanner's "
                    "ability to resolve detail, even though the cleaning bath's job does not "
                    "depend on it in the same way."},
            {"text": "A cleaning bath works through the energy in its bubbles, not through picking "
                     "out fine detail, so it has no need for the very short wavelength a scan "
                     "requires",
                         "correct": True},
            {"text": "A cleaning bath is not really ultrasound, only ordinary audible sound turned "
                     "up as loud as it will go, despite what manufacturers often claim to justify "
                     "a higher price",
                         "correct": False,
                         "why": "40 000 Hz sits above the roughly 20 000 Hz top of human hearing, so a "
                    "cleaning bath genuinely does use ultrasound."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h13",
        "band": "harder",
        "text": "A gauge calibrated for water is mistakenly used on an aluminium block. For a "
                "reflector at the SAME true depth, compare the real echo return time in "
                "aluminium with what the water calibration would predict for that depth.",
        "options": [
            {"text": "The real time in aluminium is considerably longer, since aluminium is a "
                     "solid and solids slow ultrasound down compared with a liquid",
                         "correct": False,
                         "why": "Solids do not always carry sound more slowly than liquids; aluminium in "
                    "particular carries ultrasound a good deal faster than water."},
            {"text": "The two times would be identical, since the depth is the same in both cases",
                         "correct": False,
                         "why": "Equal depth does not give equal time here, because aluminium and water carry "
                    "ultrasound at very different speeds."},
            {"text": "It cannot be compared without first knowing the exact temperature of both "
                     "the water and the aluminium block on the day of the test",
                         "correct": False,
                         "why": "The comparison follows directly from the two materials' very different "
                    "speeds of sound; temperature is not the deciding factor here."},
            {"text": "The real time in aluminium is considerably shorter, since aluminium carries "
                     "the pulse a good deal faster than water does",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h14",
        "band": "harder",
        "text": "A block 0.150 m thick is tested from one side. The near face gives an echo, "
                "and so does the far face, in steel, at about 5000 m/s. How long after the "
                "pulse is sent does the far-face echo return?",
        "options": [
            {"text": "0.060 ms, since the far-face echo travels the full thickness there and back, "
                     "0.300 m in total",
                         "correct": True},
            {"text": "0.030 ms, taking only the one-way thickness as the full path the far-face "
                     "echo has to travel along",
                         "correct": False,
                         "why": "The far-face echo travels down to the far face AND back again, twice the "
                    "one-way thickness, not the one-way thickness alone."},
            {"text": "0.120 ms, doubling the correct time as though the echo made the round trip "
                     "twice over",
                         "correct": False,
                         "why": "The far-face echo makes one round trip, down and back once; doubling that "
                    "time counts the journey twice."},
            {"text": "0.600 ms, treating the 0.150 m thickness as if it were measured in "
                     "centimetres rather than metres",
                         "correct": False,
                         "why": "0.150 m is already in metres; reading it as centimetres inflates the "
                    "distance, and so the time, by a factor of ten."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h15",
        "band": "harder",
        "text": "Using the same block as before, 0.150 m thick, the near-face echo (from the "
                "surface right under the probe) returns essentially the instant the pulse is "
                "sent. Explain why the gauge's screen still shows this as a distinct first "
                "pip rather than nothing at all.",
        "options": [
            {"text": "The screen draws a pip at the very start of the window whether or not any "
                     "reflection has actually happened there, purely as a fixed feature of how the "
                     "display is built",
                         "correct": False,
                         "why": "A pip on this screen represents a genuine reflected pulse; the near-face pip "
                    "appears because a real boundary is there, not as a default mark."},
            {"text": "The near face is itself a boundary — probe against block — so some of the "
                     "pulse's energy reflects there straight away, showing as an almost-instant "
                     "first pip",
                         "correct": True},
            {"text": "The near face cannot actually reflect anything, since the probe is pressed "
                     "directly against it with no gap",
                         "correct": False,
                         "why": "The probe-to-block join is still a boundary between two different materials, "
                    "and some reflection happens there regardless of how firmly the probe is "
                    "pressed."},
            {"text": "The pip only appears because of a small delay built into the electronics, "
                     "unrelated to any real reflection",
                         "correct": False,
                         "why": "The near-face pip corresponds to a genuine reflection at the probe-to-block "
                    "boundary, not an artefact of the electronics."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h16",
        "band": "harder",
        "text": "Explain why gel is applied for a medical scan but is not needed for the flaw "
                "gauge used directly on a bare metal block in a workshop.",
        "options": [
            {"text": "Gel matters for living tissue alone, because metal cannot form a boundary with air",
                         "correct": False,
                         "why": "Metal against air is a genuine boundary too; the real difference here is how "
                    "easily a probe can sit flush against a hard, flat surface compared with "
                    "skin."},
            {"text": "Metal blocks are tested using a completely different, gel-free kind of "
                     "ultrasound",
                         "correct": False,
                         "why": "The same kind of ultrasound pulse is used in both cases; what differs is how "
                    "easily each surface makes contact with the probe."},
            {"text": "The workshop probe is pressed straight onto a hard, flat metal surface with "
                     "no soft, uneven skin to leave an air gap, so there is little or no air "
                     "boundary to remove",
                         "correct": True},
            {"text": "A workshop probe does not actually need to touch the block, unlike a medical "
                     "probe on the skin, because metal conducts sound through open air just as "
                     "readily as through itself",
                         "correct": False,
                         "why": "A workshop probe is pressed onto the block just as a medical probe is "
                    "pressed onto the skin; both need good contact for the pulse to get in."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h17",
        "band": "harder",
        "text": "A ship's echo sounder and a hospital's flaw-detection probe both work by "
                "timing a reflected pulse, yet one operates in open sea water and the other "
                "inside a solid metal part. Explain why both can use essentially the same "
                "underlying method.",
        "options": [
            {"text": "Both situations actually use exactly the same speed of sound, since the "
                     "method could not work otherwise",
                         "correct": False,
                         "why": "Sea water and metal carry sound at very different speeds; the method works "
                    "in both because it uses whichever speed applies, not because the speeds are "
                    "the same."},
            {"text": "Neither situation is really timing anything; both simply measure how loud "
                     "the returning pulse is",
                         "correct": False,
                         "why": "Both methods depend on TIMING the returning pulse to work out a distance, "
                    "not on measuring its loudness."},
            {"text": "Water and metal are actually the same material as far as sound is concerned, "
                     "which is why the method transfers so easily between them",
                         "correct": False,
                         "why": "Water and metal are very different materials with very different speeds of "
                    "sound; the shared method works despite this difference, not because of it."},
            {"text": "The method only needs a pulse, a boundary to reflect it, and a known speed "
                     "of sound in whatever material is being used — water and metal both provide "
                     "that",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h18",
        "band": "harder",
        "text": "A total path of 0.372 m is recorded in an aluminium block, at about 6300 "
                "m/s. Roughly how long did the pulse take to make the whole round trip?",
        "options": [
            {"text": "About 0.059 ms",
                         "correct": True},
            {"text": "About 0.118 ms, doubling the correct time as though the round trip were made "
                     "twice over",
                         "correct": False,
                         "why": "The 0.372 m already IS the whole round-trip path; doubling the resulting "
                    "time counts the journey twice."},
            {"text": "About 5.9 ms, treating the answer as though it were a hundred times larger than it really is",
                         "correct": False,
                         "why": "Dividing 0.372 m by 6300 m/s gives an answer in the tens of microseconds, "
                    "not in whole milliseconds at that scale."},
            {"text": "About 0.0295 ms, halving the correct time as though only half the path "
                     "needed converting to a time",
                         "correct": False,
                         "why": "The whole 0.372 m path corresponds to the whole travel time; halving it here "
                    "is not part of finding the time from a given distance and speed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h19",
        "band": "harder",
        "text": "A student argues that because ultrasound and audible sound obey the same "
                "rules, a stethoscope could in principle be redesigned to work with "
                "ultrasound instead. Evaluate this reasoning against what a stethoscope actually does.",
        "options": [
            {"text": "The reasoning is entirely correct, and any stethoscope could be swapped for "
                     "an ultrasonic one with no other changes needed, since the underlying physics "
                     "is supposedly identical either way",
                         "correct": False,
                         "why": "A stethoscope's whole purpose is letting a person hear a sound directly; "
                    "ultrasound is by definition above what a person can hear."},
            {"text": "The reasoning misses the real issue — a stethoscope listens to sound already "
                     "being made inside the body, and switching to ultrasound would not let a "
                     "human ear hear it any better",
                         "correct": True},
            {"text": "The reasoning is wrong because ultrasound and audible sound do not actually "
                     "obey the same rules",
                         "correct": False,
                         "why": "Ultrasound does obey exactly the same rules as any other sound; the flaw in the student's argument lies elsewhere."},
            {"text": "The reasoning cannot be judged without first knowing the exact make of "
                     "stethoscope being discussed",
                         "correct": False,
                         "why": "The issue here is a stethoscope's basic purpose, letting a human ear hear a "
                    "sound directly, which does not depend on any particular make."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h20",
        "band": "harder",
        "text": "Explain why a single ultrasound pulse sent straight down into a body can "
                "only ever build up one narrow line of information, and what a full picture "
                "actually requires as a result.",
        "options": [
            {"text": "A single pulse already reveals the whole body at once, and a picture is "
                     "simply that one pulse displayed differently",
                         "correct": False,
                         "why": "One pulse only carries information about the boundaries it happens to meet "
                    "along its own path, not about the whole body."},
            {"text": "A picture is built from a single pulse, because an ultrasound pulse spreads out sideways as it travels and so covers the whole width of the body from one narrow line into it",
                         "correct": False,
                         "why": "A picture is built by combining many separate pulses sent along many "
                    "different lines, not by relying on one pulse spreading sideways."},
            {"text": "A pulse only reports on whatever lies directly along the path it travelled, "
                     "so a full picture needs many pulses sent along many different paths and "
                     "assembled together",
                         "correct": True},
            {"text": "One pulse cannot reveal anything about the body; a picture instead comes "
                     "from the heat the probe generates",
                         "correct": False,
                         "why": "A single pulse does reveal real information, the timing of its own echoes; "
                    "the picture problem is about combining many such pulses, not about heat."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h21",
        "band": "harder",
        "text": "A manufacturer claims a new probe can detect a crack \"of any size, however "
                "small, at any depth, however great.\" Evaluate this claim using what is known about detail and depth trading against each other.",
        "options": [
            {"text": "Very likely true, since a sufficiently well-built probe faces no trade-off "
                     "between detail and depth",
                         "correct": False,
                         "why": "That trade-off is a real one, and no probe design removes it entirely."},
            {"text": "Very likely true, provided the probe is simply made loud enough to reach any "
                     "depth, regardless of the frequency chosen for it in the first place or the "
                     "size of flaw being searched for",
                         "correct": False,
                         "why": "Loudness affects how far a pulse's energy carries, but the trade-off "
                    "described here is specifically about frequency, wavelength and detail, not "
                    "loudness."},
            {"text": "The claim cannot be evaluated without first testing the probe on a real "
                     "crack",
                         "correct": False,
                         "why": "The claim can be judged against the general physical trade-off between frequency, detail and depth, without needing to test this particular probe."},
            {"text": "Very unlikely — resolving very small features needs a high frequency, and "
                     "high frequencies are absorbed faster and do not reach as far, so the two "
                     "aims work against each other",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h22",
        "band": "harder",
        "text": "A pulse returns from a reflector in steel after 0.048 ms, at about 5000 m/s. "
                "A second pulse returns from a reflector at the same true depth in aluminium. "
                "Predict, without calculating an exact figure, whether the second time is "
                "longer or shorter than 0.048 ms, and why.",
        "options": [
            {"text": "Shorter, since aluminium carries ultrasound faster than steel, so the same "
                     "depth is covered in less time",
                         "correct": True},
            {"text": "Longer, since aluminium is a lighter metal, and lighter materials take "
                     "longer to carry a pulse the same distance",
                         "correct": False,
                         "why": "Being lighter is not what decides the speed of sound in a metal; aluminium "
                    "in particular is FASTER than steel, not slower."},
            {"text": "Exactly the same, 0.048 ms, since the depth is unchanged between the two "
                     "cases",
                         "correct": False,
                         "why": "Equal depth does not give equal time here, since steel and aluminium carry "
                    "ultrasound at different speeds."},
            {"text": "It cannot be predicted without first calculating the exact depth in "
                     "millimetres",
                         "correct": False,
                         "why": "Knowing which material is faster is already enough to predict the DIRECTION "
                    "of the change, shorter or longer, without working out the exact depth first."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h23",
        "band": "harder",
        "text": "Explain why an ultrasound scan builds its picture from many separate echoes "
                "rather than from one continuous tone held on for the whole examination.",
        "options": [
            {"text": "A continuous tone would simply be far too quiet for any boundary inside the body to reflect at all, however powerful the equipment generating it might be and however carefully the probe is aimed",
                         "correct": False,
                         "why": "Loudness is not the reason short pulses are used; the issue is being able to "
                    "time a distinct echo before sending the next pulse."},
            {"text": "A short pulse, followed by silence to listen for its echo, is what lets each "
                     "echo's timing be measured separately; a continuous tone would give "
                     "overlapping echoes with no clear timing at all",
                         "correct": True},
            {"text": "A continuous tone would instantly turn into infrasound once it entered the "
                     "body, because soft tissue lowers a wave's frequency the moment it crosses "
                     "the skin",
                         "correct": False,
                         "why": "A wave's frequency does not change simply by entering the body; the reason "
                    "for short pulses is about timing echoes, not about frequency shifting."},
            {"text": "Short pulses are used only because continuous tones are illegal to use on "
                     "patients",
                         "correct": False,
                         "why": "The reason for using short pulses is a physical one, about being able to "
                    "time separate echoes clearly, not a legal restriction."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h24",
        "band": "harder",
        "text": "A worn probe delivers a pulse with only half its original energy. Predict "
                "what would change on the screen for a reflector at the same true depth, and "
                "what would stay the same.",
        "options": [
            {"text": "The returning pip would arrive later, since a weaker pulse travels more "
                     "slowly through the same material",
                         "correct": False,
                         "why": "The energy of a pulse does not change how fast it travels; a weaker pulse "
                    "still moves at the material's ordinary speed of sound."},
            {"text": "The returning pip would disappear from the screen completely, since a probe running at half its original energy cannot produce a reflection strong enough to register on the trace at all",
                         "correct": False,
                         "why": "Half the original energy is still a real pulse capable of reflecting off a "
                    "boundary; it would likely look fainter, not vanish."},
            {"text": "The returning pip would likely appear fainter, since less energy comes back, "
                     "but it would still arrive at the same time, since the depth and the speed of "
                     "sound are unchanged",
                         "correct": True},
            {"text": "Nothing would change, since the reflector and the material are exactly the "
                     "same as before",
                         "correct": False,
                         "why": "The amount of energy reaching the boundary and reflecting back has changed, "
                    "so the pip's strength on screen would likely change too, even though its "
                    "timing would not."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h25",
        "band": "harder",
        "text": "Explain why the flaw gauge's readout gives the depth of a hidden crack but "
                "says nothing directly about how wide or how serious that crack actually is.",
        "options": [
            {"text": "The gauge is simply badly designed, and a better one could read off width "
                     "and seriousness from the very same single echo",
                         "correct": False,
                         "why": "The limitation here is a matter of what timing an echo can and cannot "
                    "reveal, not a design flaw that a better gauge could straightforwardly "
                    "remove."},
            {"text": "Width and seriousness are not real physical properties a crack can have",
                         "correct": False,
                         "why": "A crack genuinely does have a width and a degree of seriousness; the gauge "
                    "simply is not measuring either of those from a single echo's timing."},
            {"text": "The gauge cannot detect a crack unless its width is already known in "
                     "advance, from some other test done beforehand",
                         "correct": False,
                         "why": "The gauge detects a crack from the reflection at its boundary, which needs "
                    "no prior knowledge of the crack's width."},
            {"text": "Timing an echo only reveals where a boundary sits along the pulse's path, "
                     "not how large the boundary itself is",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h26",
        "band": "harder",
        "text": "A textbook account of flaw detection describes a pulse reflecting cleanly off one single, clear boundary inside a test block. Describe a genuine complication that a REAL "
                "block often adds to this simple picture.",
        "options": [
            {"text": "A real trace usually also shows separate reflections from the block's far "
                     "face and from any edges, plus background noise, alongside the flaw's own "
                     "echo",
                         "correct": True},
            {"text": "A real block never actually produces any echo, unlike the simple account",
                         "correct": False,
                         "why": "Real blocks do produce genuine echoes; the complication is extra reflections "
                    "and noise alongside the flaw's echo, not an absence of any echo."},
            {"text": "A real block changes the speed of sound travelling through it every few seconds, rather than holding to one steady speed throughout the whole of an inspection",
                         "correct": False,
                         "why": "The speed of sound in a given, unchanging material stays steady; it is extra "
                    "reflections and noise that complicate a real trace, not a shifting speed."},
            {"text": "A real block shows a single pip, exactly matching the simple account in every case",
                         "correct": False,
                         "why": "A real trace typically shows more than that single clean pip, including far-face and edge reflections and background noise."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h27",
        "band": "harder",
        "text": "An apprentice suggests that ordinary water, rather than the usual gel, could "
                "remove the air gap between a probe and a patient's skin just as well. "
                "Evaluate this suggestion, using what the gel is actually for.",
        "options": [
            {"text": "It could never work, since the gel sold for scanning is the one substance physically capable of removing an air boundary between a probe and a patient's skin",
                         "correct": False,
                         "why": "The gel's job is simply to fill the gap and remove the air boundary, and more than one substance can do that."},
            {"text": "It could work in principle, since water also fills the gap and removes the "
                     "air boundary, though gel is thicker and stays in place more conveniently",
                         "correct": True},
            {"text": "It could never work, since water evaporates instantly and could never stay "
                     "in place for a whole scan",
                         "correct": False,
                         "why": "Evaporation over a short scan is not the reason gel is preferred; gel is "
                    "mainly more practical to keep in place and control."},
            {"text": "It makes no difference either way, since the probe would work exactly the "
                     "same with or without anything in the gap",
                         "correct": False,
                         "why": "Without gel or water, an air gap would reflect almost the whole pulse "
                    "straight back, which is exactly the problem either substance is there to "
                    "solve."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h28",
        "band": "harder",
        "text": "A short, sharp pulse generally gives better depth resolution — telling two "
                "close-together reflectors apart — than a long, drawn-out pulse at the same "
                "frequency. Suggest why.",
        "options": [
            {"text": "A short pulse carries a good deal more energy than a long one does, and it is that extra energy, rather than the pulse's timing, that gives the sharper detail",
                         "correct": False,
                         "why": "Energy and pulse length are not directly linked this way; the resolution "
                    "advantage here comes from the pulse's short duration in time, not its "
                    "energy."},
            {"text": "A long pulse cannot travel as far into the material as a short one can",
                         "correct": False,
                         "why": "How far a pulse reaches depends mainly on absorption and frequency, not "
                    "simply on how long the pulse lasts."},
            {"text": "A short pulse produces a brief, sharply-timed echo, so two echoes from close "
                     "reflectors are less likely to overlap into one blurred signal",
                         "correct": True},
            {"text": "A short pulse travels faster than a long one through the same material",
                         "correct": False,
                         "why": "Speed through a material depends on the material itself, not on how long or "
                    "short the pulse is."},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h29",
        "band": "harder",
        "text": "An apprentice claims that using twice as much gel would let a probe's pulse "
                "reach twice as deep into the body. Evaluate this claim.",
        "options": [
            {"text": "The claim is right, since gel is what actually carries the pulse's energy "
                     "deeper into the tissue, more gel meaning more energy carried all the way "
                     "through to wherever it is needed",
                         "correct": False,
                         "why": "Gel's role is limited to removing the air boundary at the surface; it is not "
                    "what carries the pulse's energy deeper into the tissue beyond that."},
            {"text": "The claim is right, but only because thicker gel layers slow the pulse down "
                     "enough to let it penetrate further into the body than it otherwise ever "
                     "could",
                         "correct": False,
                         "why": "A slower pulse in a thicker gel layer would not translate into greater "
                    "penetration once the pulse reaches the tissue itself."},
            {"text": "The claim cannot be evaluated without knowing the exact brand of gel used",
                         "correct": False,
                         "why": "The gel's basic role, removing the air gap, does not depend on brand; the "
                    "claim can be judged against that role directly."},
            {"text": "The claim is wrong — gel's job is only to remove the air gap at the surface; "
                     "how deep a pulse reaches depends on its frequency and how much the tissue "
                     "absorbs it, not on gel quantity",
                         "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-09-h30",
        "band": "harder",
        "text": "Explain why an engineer inspecting a weld chooses a probe frequency based on "
                "both the weld's likely flaw size AND how deep into the metal it needs to "
                "see, rather than simply picking the highest frequency available.",
        "options": [
            {"text": "The highest frequency would give the finest detail but would also be "
                     "absorbed fastest, possibly failing to reach a flaw deep inside a thick weld "
                     "at all",
                         "correct": True},
            {"text": "The highest frequency available is both the most detailed and the "
                     "deepest-reaching choice, so there is no real trade-off to make",
                         "correct": False,
                         "why": "The trade-off is a genuine one: higher frequencies are absorbed faster and do not reach as far, so the highest frequency is not always the best choice."},
            {"text": "Frequency only affects how loud the returning echo sounds, not how deep the "
                     "pulse can reach or how much detail it shows",
                         "correct": False,
                         "why": "Frequency sets the wavelength, and that governs both the detail and how far a pulse usefully reaches."},
            {"text": "The choice of frequency is really just a matter of the engineer's personal "
                     "preference, with no physical consequence either way",
                         "correct": False,
                         "why": "The choice has a real physical consequence: detail is traded against reach."},
        ],
        "figure": None,
    },
]
