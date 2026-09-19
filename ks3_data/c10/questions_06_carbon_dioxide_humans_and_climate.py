"""C10 lesson 06 — Carbon dioxide, humans and climate: twelve questions.

MRB-281. The unit's last question file, and the last of C10's seventy-two.

The lesson's argument has two halves and the bank probes both. The first half
is a MECHANISM — sunlight in, infrared out, absorbed on the way out, and a
higher temperature at the balance point — and a student who has learned it can
say what the gases do NOT absorb as readily as what they do. The second half
is an ARGUMENT: four independent lines of evidence, one of which is doing a
different job from the other three.

These twelve probe the angles the mastery ladder leaves alone: which way round
the transparency goes, what would happen with no greenhouse effect at all, what
the ozone layer actually does, why "water vapour does most of it" is not an
argument, what two agreeing graphs are missing, what a cold winter is evidence
of, and why a fingerprint rules a source out.

The distractors are built from the lesson's declared misconceptions.

`EARTH-16` (the planet is warming because of the hole in the ozone layer
letting extra heat in) drives e04, which is the whole question, and the first
option of h02, where the heat is stopped high up by the wrong layer.

`EARTH-17` (the greenhouse effect is the problem — it is what is causing the
planet to warm) drives e02 and s01. `EARTH-17` carries no `elicited_by` on the
page — nothing there asks a student to commit to it — so this bank is where it
is elicited, which is the `EARTH-03/04/09/13/15` pattern.

⚠️ **THREE THINGS THIS BANK TEACHES THAT ARE NOT REGISTER ENTRIES.** s02 is
the water-vapour argument, s03 is correlation without a mechanism, and s04 is
climate against weather. All three are corrected on the page — in an explainer,
in the evidence block's closing panel, and in the vocabulary definition of
"climate" — and none is minted as a misconception id. The register names the
beliefs a page is BUILT to break, and a page with five of them has stopped
having a spine. See the note in `docs/ks3/misconception-register.md`.

⚠️ **NOTHING HERE COMES FROM `c10-07`.** The carbon cycle is drawn by Design
and deliberately not built; the spine records the ruling. Where the yearly
wobble in the Hawaii record is used, it is explained in the words this page
uses for it and not by naming a lesson that does not exist.

⚠️ **NO QUESTION RETRACTS `c10-05`.** Carbon dioxide is four hundredths of one
per cent of the air on both pages, and nothing here calls it a trace.

⚠️ MRB-278 · ANSWER POSITION. C10's bank stood at [14, 16, 16, 14] over sixty
questions. This file takes **four at index 0, two at index 1, two at index 2
and four at index 3**, which brings the unit to a flat [18, 18, 18, 18].

⚠️ BAND VALUES ARE FULL WORDS — `easier`, `standard`, `harder`, never the
letters.
"""

UNIT = "C10"
LESSON = "carbon-dioxide-humans-and-climate"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c10-06-e01",
        "band": "easier",
        "text": "Greenhouse gases let one kind of radiation through and "
                "absorb another. Which way round is it?",
        "options": [
            {"text": "They let visible light through and absorb infrared "
                     "radiation",
             "correct": True},
            {"text": "They let infrared through and absorb visible light from "
                     "the Sun",
             "correct": False,
             "why": "That is the wrong way round. If they absorbed sunlight "
                    "it would never reach the ground to warm it."},
            {"text": "They absorb visible light and infrared radiation "
                     "equally well",
             "correct": False,
             "why": "They absorb almost no visible light at all — that is why "
                    "the sky is not dark."},
            {"text": "They reflect both kinds of radiation straight back down "
                     "again",
             "correct": False,
             "why": "Nothing is reflected. The gas absorbs infrared and "
                    "radiates it again in all directions."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e02",
        "band": "easier",
        "text": "Would the Earth be a better place to live if there were no "
                "greenhouse effect at all?",
        "options": [
            {"text": "No — the surface would average about −18 °C and be "
                     "frozen",
             "correct": True},
            {"text": "Yes — the planet would stop warming and go back to "
                     "normal",
             "correct": False,
             "why": "It would go far past normal. The natural effect is worth "
                    "about 33 °C, and without it the oceans would freeze."},
            {"text": "Yes — the greenhouse effect is what is causing the "
                     "problem",
             "correct": False,
             "why": "The effect itself is natural and necessary. What is "
                    "causing the problem is the increase in it."},
            {"text": "It would make no real difference to the temperature at "
                     "all",
             "correct": False,
             "why": "It accounts for the difference between about −18 °C and "
                    "about 15 °C. The difference is enormous."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e03",
        "band": "easier",
        "text": "Since about 1750, what has happened to the amount of carbon "
                "dioxide in the air?",
        "options": [
            {"text": "It has fallen by about half, from 420 to 280 parts per "
                     "million",
             "correct": False,
             "why": "Those are the right two numbers in the wrong order. It "
                    "has risen, not fallen."},
            {"text": "It has stayed about the same, at around 280 parts per "
                     "million",
             "correct": False,
             "why": "280 was the level before industry. It is over 420 now, "
                    "and it has risen every year since 1958."},
            {"text": "It has doubled, from about 210 to over 420 parts per "
                     "million",
             "correct": False,
             "why": "It has risen by about half, not doubled. The starting "
                    "point was around 280."},
            {"text": "It has risen by about half, from around 280 to over 420 "
                     "parts per million",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e04",
        "band": "easier",
        "text": "The hole in the ozone layer and the greenhouse effect are "
                "often mixed up. What does the ozone layer actually do?",
        "options": [
            {"text": "It absorbs the infrared that the warmed ground radiates "
                     "back out",
             "correct": False,
             "why": "That is the greenhouse effect, lower down and involving "
                    "different gases entirely."},
            {"text": "It reflects some of the Sun's heat away before it can "
                     "reach us",
             "correct": False,
             "why": "It absorbs ultraviolet rather than reflecting heat. "
                    "Reflection is what clouds and ice do."},
            {"text": "It holds warm air close to the surface like the glass "
                     "of a greenhouse",
             "correct": False,
             "why": "Nothing in the atmosphere does that, and neither does "
                    "the greenhouse effect. There is no lid."},
            {"text": "It blocks most of the ultraviolet radiation coming in "
                     "from the Sun",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c10-06-s01",
        "band": "standard",
        "text": "A student writes: “We need to get rid of the greenhouse "
                "effect.” What is wrong with that?",
        "options": [
            {"text": "The natural effect keeps the planet liveable; the "
                     "problem is that we have strengthened it",
             "correct": True},
            {"text": "Nothing — getting rid of it is exactly what scientists "
                     "are trying to do",
             "correct": False,
             "why": "What is being reduced is the extra carbon dioxide, not "
                    "the effect. Removing the effect would freeze the "
                    "planet."},
            {"text": "Nothing is wrong, but it would take far too long to be "
                     "worth trying",
             "correct": False,
             "why": "It is not a question of how long it would take. It is "
                    "not something anybody would want."},
            {"text": "The greenhouse effect only started when people began "
                     "burning fossil fuels",
             "correct": False,
             "why": "It has operated for billions of years. Human activity "
                    "has added to it."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s02",
        "band": "standard",
        "text": "Someone argues that water vapour is a far bigger greenhouse "
                "gas than carbon dioxide, so carbon dioxide cannot be the "
                "cause. Why does that argument fail?",
        "options": [
            {"text": "Water vapour is not a greenhouse gas at all, so the "
                     "amount of it in the air changes nothing",
             "correct": False,
             "why": "It is a greenhouse gas, and a strong one. That is not "
                    "where the argument goes wrong."},
            {"text": "How much water vapour the air holds is set by the "
                     "temperature, so it follows rather than leads",
             "correct": True},
            {"text": "There is far less water vapour in the air than carbon "
                     "dioxide, so it cannot be doing much",
             "correct": False,
             "why": "There is far more of it, not less. The amount is what "
                    "makes people reach for this argument."},
            {"text": "Water vapour is only found near the ground, so it never "
                     "gets high enough to matter",
             "correct": False,
             "why": "Most of it is low down, and that is not why the argument "
                    "fails. It fails because the temperature sets the "
                    "amount."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s03",
        "band": "standard",
        "text": "Two graphs are put side by side: carbon dioxide rising, and "
                "global temperature rising. A student says this proves carbon "
                "dioxide causes the warming. What is missing?",
        "options": [
            {"text": "Nothing is missing — two graphs going the same way is "
                     "proof enough",
             "correct": False,
             "why": "Plenty of unrelated things have risen since 1958. Two "
                    "lines agreeing is a match, not a cause."},
            {"text": "The graphs would need to cover at least a thousand "
                     "years to prove anything",
             "correct": False,
             "why": "A longer record would help with context, and it still "
                    "would not supply a cause."},
            {"text": "A reason why carbon dioxide should warm anything, which "
                     "the laboratory supplies",
             "correct": True},
            {"text": "A third graph showing something else rising at the same "
                     "time as the other two",
             "correct": False,
             "why": "A third matching line adds a third correlation. It does "
                    "not turn two into a cause."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s04",
        "band": "standard",
        "text": "Britain has an unusually cold winter, and a newspaper says "
                "this shows the planet is not warming. What is wrong with "
                "that?",
        "options": [
            {"text": "Nothing — one cold winter is enough to show the trend "
                     "has reversed",
             "correct": False,
             "why": "One winter cannot show a trend in either direction. It "
                    "is a single point."},
            {"text": "Britain is too small a country for its weather to count "
                     "as evidence",
             "correct": False,
             "why": "The size of the country is not the problem. The length "
                    "of time is."},
            {"text": "Winters are colder everywhere now, so the newspaper has "
                     "the trend right",
             "correct": False,
             "why": "They are not. Individual cold winters still happen while "
                    "the average rises."},
            {"text": "One winter is weather, and climate is the pattern of "
                     "weather averaged over decades",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c10-06-h01",
        "band": "harder",
        "text": "Ice cores show carbon dioxide moving between 180 and 300 "
                "parts per million over 800,000 years, always alongside the "
                "ice ages. Why does that not show the present rise is "
                "natural?",
        "options": [
            {"text": "The present level is above the whole of that range and "
                     "arrived in two centuries",
             "correct": True},
            {"text": "Ice cores cannot be trusted that far back, so the range "
                     "is probably wrong",
             "correct": False,
             "why": "The bubbles are direct samples of the air. The record is "
                    "the strongest evidence there is about the past."},
            {"text": "It does show it — the record proves carbon dioxide has "
                     "always gone up and down",
             "correct": False,
             "why": "It has, and that is not the point. The present level is "
                    "outside the whole range the record covers."},
            {"text": "Ice ages were caused by something else, so the ice-core "
                     "record is irrelevant",
             "correct": False,
             "why": "The ice ages were started by changes in the Earth's "
                    "orbit, and carbon dioxide moved with them. The record "
                    "still stands."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h02",
        "band": "harder",
        "text": "Why is it wrong to say that greenhouse gases trap the Sun's "
                "rays?",
        "options": [
            {"text": "Because the ozone layer stops them much higher up, "
                     "before any gas below can reach them",
             "correct": False,
             "why": "The ozone layer blocks ultraviolet, not the sunlight "
                    "that warms the ground — and it is a separate problem "
                    "entirely."},
            {"text": "Because the gases are transparent to sunlight; what "
                     "they absorb is the infrared going back out",
             "correct": True},
            {"text": "Because the gases reflect the Sun's rays back out to "
                     "space instead of absorbing them",
             "correct": False,
             "why": "They do not reflect anything. Sunlight passes straight "
                    "through them."},
            {"text": "Because sunlight is reflected away by clouds before any "
                     "gas has a chance to act",
             "correct": False,
             "why": "Clouds reflect some of it, and plenty gets through — "
                    "which is what warms the ground in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h03",
        "band": "harder",
        "text": "Methane is far stronger than carbon dioxide per molecule, "
                "but it breaks down in about ten years. What does that make "
                "it?",
        "options": [
            {"text": "The gas responsible for most of the warming that has "
                     "already happened",
             "correct": False,
             "why": "Carbon dioxide is responsible for most of it, because "
                    "there is far more of it and it stays for far longer."},
            {"text": "A gas that can safely be ignored, because it does not "
                     "last very long",
             "correct": False,
             "why": "Ten years is short for a gas and long for a decade of "
                    "warming. While it is up there it does a great deal."},
            {"text": "The gas where cutting emissions would show a result the "
                     "soonest, because it clears quickly",
             "correct": True},
            {"text": "A gas that behaves exactly like carbon dioxide once it "
                     "is in the air",
             "correct": False,
             "why": "It absorbs far more strongly per molecule and it does "
                    "not last. Both differences matter."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h04",
        "band": "harder",
        "text": "The extra carbon dioxide in the air is measurably lighter in "
                "its carbon isotopes than carbon released by volcanoes. Why "
                "does that matter?",
        "options": [
            {"text": "It shows how much of the extra carbon dioxide the "
                     "oceans have absorbed",
             "correct": False,
             "why": "The fingerprint says where the carbon came from, not "
                    "where it has gone since."},
            {"text": "It shows the extra carbon dioxide arrived recently "
                     "rather than long ago",
             "correct": False,
             "why": "The Hawaii record and the ice cores establish when. The "
                    "isotopes establish what it came from."},
            {"text": "It shows the extra carbon dioxide is warming the planet "
                     "more than expected",
             "correct": False,
             "why": "A lighter isotope absorbs infrared in the same way. The "
                    "fingerprint says nothing about how much warming there "
                    "is."},
            {"text": "It rules out volcanoes and the oceans, because the "
                     "light carbon was once living material",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-06-e05",
        "band": "easier",
        "text": "What is infrared radiation?",
        "options": [
            {"text": "The radiation that arrives from the Sun and warms the "
                     "ground, which is what makes a sunny day feel hotter "
                     "than a cloudy one",
             "correct": False,
             "why": "The Sun mostly sends VISIBLE light down. Infrared is "
                    "what the warmed ground sends back up"},
            {"text": "A kind of ultraviolet",
             "correct": False,
             "why": "Ultraviolet is at the other end, shorter than violet. "
                    "Infrared is longer than red"},
            {"text": "A gas in the upper atmosphere",
             "correct": False,
             "why": "It is radiation rather than a substance"},
            {"text": "Radiation given off by anything warm — invisible, and a "
                     "longer wavelength than red light",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e06",
        "band": "easier",
        "text": "What does PARTS PER MILLION mean?",
        "options": [
            {"text": "How many of something there are in every million — 420 "
                     "ppm is 420 molecules in a million",
             "correct": True},
            {"text": "How many tonnes of a gas are added to the atmosphere "
                     "each year, counted in millions so that the figure stays "
                     "a manageable size",
             "correct": False,
             "why": "It is a concentration rather than an amount added. It "
                    "says how dilute the gas is"},
            {"text": "A percentage",
             "correct": False,
             "why": "A percentage is parts per hundred. 420 ppm is 0.042 per "
                    "cent"},
            {"text": "The number of millions of molecules in a sample",
             "correct": False,
             "why": "It is a ratio, not a count of a sample"},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e07",
        "band": "easier",
        "text": "What is the difference between WEATHER and CLIMATE?",
        "options": [
            {"text": "Weather is what happens in one country and climate is "
                     "what happens across the whole world, so the two words "
                     "describe the same thing at two different sizes",
             "correct": False,
             "why": "A single place has a climate of its own. The difference "
                    "is time, not area"},
            {"text": "Weather is what it is doing now; climate is the pattern "
                     "averaged over decades",
             "correct": True},
            {"text": "Weather is measured and climate is predicted",
             "correct": False,
             "why": "Both are measured, and both are forecast. The difference "
                    "is the timescale"},
            {"text": "They mean the same thing",
             "correct": False,
             "why": "Confusing them is what lets one cold winter be offered "
                    "as evidence about the climate"},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e08",
        "band": "easier",
        "text": "Which of these is NOT a greenhouse gas?",
        "options": [
            {"text": "Carbon dioxide",
             "correct": False,
             "why": "One of the main ones, and the one human activity has "
                    "changed most"},
            {"text": "Methane",
             "correct": False,
             "why": "A greenhouse gas, and a far stronger one per molecule "
                    "than carbon dioxide"},
            {"text": "Nitrogen",
             "correct": True},
            {"text": "Water vapour, which is present in far larger amounts "
                     "than any of the others and absorbs a great deal of the "
                     "infrared leaving the surface",
             "correct": False,
             "why": "All of that is true, and it makes water vapour one of "
                    "the strongest greenhouse gases there is"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c10-06-s05",
        "band": "standard",
        "text": "Why does adding greenhouse gas make the surface settle at a "
                "HIGHER temperature?",
        "options": [
            {"text": "Because the extra gas absorbs more of the sunlight "
                     "arriving, and that absorbed energy heats the air and "
                     "the ground below it directly",
             "correct": False,
             "why": "Greenhouse gases are transparent to sunlight. They "
                    "absorb the infrared going OUT"},
            {"text": "Because the gas is warm itself",
             "correct": False,
             "why": "The gas is at the temperature of the air around it. What "
                    "matters is what it absorbs"},
            {"text": "Because more gas means a thicker atmosphere, which "
                     "presses harder on the ground",
             "correct": False,
             "why": "The pressure change is negligible. The mechanism is "
                    "radiation"},
            {"text": "Because energy leaves more slowly, so the surface has "
                     "to be warmer before as much goes out as comes in",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s06",
        "band": "standard",
        "text": "Ice cores are described as the best archive on the planet. "
                "What exactly is in one?",
        "options": [
            {"text": "Bubbles of air sealed in as snow was buried, each a "
                     "sample of the atmosphere of its year",
             "correct": True},
            {"text": "Layers of dust and ash blown onto the ice, which record "
                     "what was in the air each year by what settled out of it "
                     "onto the surface",
             "correct": False,
             "why": "Dust layers are studied too, and the carbon dioxide "
                    "record comes from trapped BUBBLES of the air itself"},
            {"text": "Frozen sea water from the year it formed",
             "correct": False,
             "why": "The cores come from snow that fell on land. Nothing in "
                    "them is sea water"},
            {"text": "A chemical record of the temperature only",
             "correct": False,
             "why": "Temperature is recorded, and the bubbles give the actual "
                    "composition of the air as well"},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s07",
        "band": "standard",
        "text": "Someone says the greenhouse effect is what is warming the "
                "planet, so we should reduce it as far as possible. What is "
                "wrong?",
        "options": [
            {"text": "The greenhouse effect has almost no influence on the "
                     "temperature, so reducing it would make very little "
                     "difference either way to how warm the planet is",
             "correct": False,
             "why": "It accounts for about 33 °C. Its influence is enormous, "
                    "which is why adding to it matters"},
            {"text": "Without it the surface would average about −18 °C — the "
                     "problem is that it has been STRENGTHENED",
             "correct": True},
            {"text": "The greenhouse effect only started when people began "
                     "burning fossil fuels",
             "correct": False,
             "why": "It has operated for as long as the atmosphere has "
                    "existed. What changed is its strength"},
            {"text": "Nothing is wrong",
             "correct": False,
             "why": "Removing it entirely would leave a frozen planet"},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s08",
        "band": "standard",
        "text": "Why is methane described as the gas where cutting emissions "
                "shows a result soonest?",
        "options": [
            {"text": "Because it is a far stronger greenhouse gas per "
                     "molecule than carbon dioxide, so removing a tonne of it "
                     "has a much larger effect than removing a tonne of "
                     "carbon dioxide",
             "correct": False,
             "why": "It is stronger per molecule, and that is about SIZE of "
                    "effect. The soonest is about how fast it clears"},
            {"text": "Because there is very little of it in the air",
             "correct": False,
             "why": "The small amount is part of why its total effect is "
                    "smaller. It is the ten-year lifetime that makes it "
                    "quick"},
            {"text": "Because it breaks down in about ten years, so the "
                     "amount in the air falls quickly once emissions stop",
             "correct": True},
            {"text": "Because it comes mostly from livestock",
             "correct": False,
             "why": "Where it comes from is a separate question from how fast "
                    "a cut would show"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-06-h05",
        "band": "harder",
        "text": "Four independent lines of evidence are named for the cause "
                "of the rise. Why does having FOUR matter?",
        "options": [
            {"text": "Because a conclusion based on four measurements is four "
                     "times as reliable as one based on a single measurement "
                     "of the same thing",
             "correct": False,
             "why": "They are not four measurements of one thing. They are "
                    "four different KINDS of evidence"},
            {"text": "Because no single line of evidence is trustworthy",
             "correct": False,
             "why": "Each is trustworthy on its own. Agreement between "
                    "independent lines is stronger still"},
            {"text": "Because four is the number scientists agree on",
             "correct": False,
             "why": "There is no such convention. It happens to be how many "
                    "there are"},
            {"text": "Because each could have disagreed with the others, and "
                     "they do not",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h06",
        "band": "harder",
        "text": "Sea level rises partly because ice on land melts and partly "
                "for another reason. What is the second one?",
        "options": [
            {"text": "Water expands as it warms, and the ocean is deep enough "
                     "for that to matter",
             "correct": True},
            {"text": "Sea ice melts, and ice that turns to water takes up "
                     "more room in the ocean than it did while it was still "
                     "frozen and floating",
             "correct": False,
             "why": "Floating ice displaces its own weight already, so "
                    "melting it changes the level almost not at all. Land ice "
                    "is the one that counts"},
            {"text": "More rain falls into the sea",
             "correct": False,
             "why": "Rain came out of the sea in the first place. It is not a "
                    "net addition"},
            {"text": "Rivers carry more sediment in",
             "correct": False,
             "why": "That happens and is far too small to matter at this "
                    "scale"},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h07",
        "band": "harder",
        "text": "Why is the ISOTOPE evidence particularly hard to argue "
                "with?",
        "options": [
            {"text": "Because isotopes can be measured to far more decimal "
                     "places than any other quantity in the whole "
                     "investigation, so the figure carries less uncertainty "
                     "than the rest",
             "correct": False,
             "why": "Precision is not what makes it strong. It IDENTIFIES the "
                    "source rather than just measuring an amount"},
            {"text": "Because the extra carbon is lighter in its isotopes, "
                     "which points to carbon that was once living material",
             "correct": True},
            {"text": "Because isotopes cannot be measured wrongly",
             "correct": False,
             "why": "Any measurement can go wrong. Its strength is that it "
                    "points at a particular origin"},
            {"text": "Because volcanoes produce no carbon dioxide",
             "correct": False,
             "why": "They produce a great deal, and its isotopes are "
                    "different — which is exactly how they are ruled out"},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h08",
        "band": "harder",
        "text": "Two graphs rise together: carbon dioxide and temperature. "
                "What has to be added before that is an argument?",
        "options": [
            {"text": "A longer record, because two lines that have only been "
                     "measured for a couple of centuries cannot show anything "
                     "reliable about how they are related",
             "correct": False,
             "why": "A longer record helps and is not what is missing. Two "
                    "lines rising together never establish cause by "
                    "themselves"},
            {"text": "Nothing — two graphs rising together is proof",
             "correct": False,
             "why": "Two things can rise together for a third reason, or by "
                    "coincidence. The mechanism is what closes it"},
            {"text": "A mechanism — a reason why one should warm the other, "
                     "which the laboratory supplies",
             "correct": True},
            {"text": "A third graph",
             "correct": False,
             "why": "More correlations do not become a cause. A physical "
                    "reason does"},
        ],
        "figure": None,
    },

    # -- easier --
    {
        "id": "c10-06-e09",
        "band": "easier",
        "text": "Besides burning fossil fuels, what are the two other human "
                "activities named as adding to the rise in carbon dioxide?",
        "options": [
            {"text": "Clearing forests and making cement",
             "correct": True},
            {"text": "Farming rice paddies and rearing cattle",
             "correct": False,
             "why": "Those are named elsewhere as methane sources. The two "
                    "named for carbon dioxide are clearing forests and "
                    "making cement."},
            {"text": "Flying aeroplanes and driving cars",
             "correct": False,
             "why": "Those burn fossil fuels directly, which is the main "
                    "cause already named. The OTHER two are clearing "
                    "forests and making cement."},
            {"text": "Mining coal and drilling for oil",
             "correct": False,
             "why": "Mining and drilling extract fossil fuels; it is "
                    "burning them that releases the carbon dioxide. The "
                    "other two named causes are forests and cement."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e10",
        "band": "easier",
        "text": "Nitrogen and oxygen make up 99% of the air. Do they absorb "
                "infrared radiation the way carbon dioxide does?",
        "options": [
            {"text": "Yes, both of them absorb it just as strongly as "
                     "carbon dioxide does",
             "correct": False,
             "why": "Neither gas absorbs infrared. Absorbing it is what "
                    "makes a gas a greenhouse gas, and nitrogen and oxygen "
                    "are not greenhouse gases."},
            {"text": "No, neither of them absorbs infrared at all",
             "correct": True},
            {"text": "Just nitrogen absorbs it, and oxygen does not",
             "correct": False,
             "why": "Nitrogen absorbs no infrared either. Neither of the "
                    "two majority gases is a greenhouse gas."},
            {"text": "Just oxygen absorbs it; nitrogen does not",
             "correct": False,
             "why": "Oxygen absorbs no infrared either. Neither of the two "
                    "majority gases is a greenhouse gas."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e11",
        "band": "easier",
        "text": "A real greenhouse is warm mainly because its glass stops "
                "warm air escaping. What does the atmosphere have that "
                "plays the same role as the glass?",
        "options": [
            {"text": "The ozone layer, which seals warm air in beneath it "
                     "the way a pane of glass does",
             "correct": False,
             "why": "The ozone layer blocks ultraviolet radiation; it does "
                    "not seal in warm air. Nothing plays the glass's role."},
            {"text": "Clouds, which form a solid barrier overhead",
             "correct": False,
             "why": "Clouds are not a solid barrier and do not stop air "
                    "moving. Nothing in the atmosphere plays that role."},
            {"text": "Nothing — the atmosphere has no lid, and air moves "
                     "freely through it",
             "correct": True},
            {"text": "Greenhouse gases themselves, which form a physical "
                     "layer that traps air underneath",
             "correct": False,
             "why": "Greenhouse gases absorb infrared radiation; they do "
                    "not form a physical layer that traps air."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e12",
        "band": "easier",
        "text": "Who is credited with independently showing, in the 1850s, "
                "that carbon dioxide absorbs heat radiation?",
        "options": [
            {"text": "Charles Darwin and Alfred Russel Wallace",
             "correct": False,
             "why": "Those two are credited with the theory of evolution by "
                    "natural selection, a separate field entirely."},
            {"text": "Dmitri Mendeleev and Marie Curie",
             "correct": False,
             "why": "Mendeleev built the periodic table and Curie studied "
                    "radioactivity — neither measured what carbon dioxide "
                    "absorbs."},
            {"text": "James Watt and Michael Faraday",
             "correct": False,
             "why": "Watt improved the steam engine and Faraday worked on "
                    "electromagnetism, not on gases absorbing radiation."},
            {"text": "Eunice Foote and John Tyndall",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e13",
        "band": "easier",
        "text": "Livestock and leaking gas pipes are two of the three "
                "named sources of methane. What is the third?",
        "options": [
            {"text": "Waste buried in landfill",
             "correct": True},
            {"text": "Gas from erupting volcanoes",
             "correct": False,
             "why": "Volcanic gas is mostly water vapour and carbon "
                    "dioxide. Methane is not a significant part of it."},
            {"text": "Rivers and lakes",
             "correct": False,
             "why": "Neither is named here as a methane source. The third "
                    "named source is waste buried in landfill."},
            {"text": "Coal-fired power stations",
             "correct": False,
             "why": "Burning coal releases carbon dioxide. The third named "
                    "methane source is waste buried in landfill."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e14",
        "band": "easier",
        "text": "Which piece of evidence establishes the TREND — that "
                "carbon dioxide has been rising, measured continuously in "
                "one place?",
        "options": [
            {"text": "The ice cores, going back 800,000 years",
             "correct": False,
             "why": "Ice cores establish the historical context, not the "
                    "recent trend. That is the Hawaii record's role."},
            {"text": "The direct measurements taken in Hawaii since 1958",
             "correct": True},
            {"text": "The chemical isotope fingerprint of the extra carbon",
             "correct": False,
             "why": "The isotopes identify where the carbon came from, not "
                    "whether it is currently rising."},
            {"text": "The laboratory measurement of the gas absorbing "
                     "infrared",
             "correct": False,
             "why": "The laboratory work supplies the mechanism, not the "
                    "trend over time."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e15",
        "band": "easier",
        "text": "Which piece of evidence establishes the CONTEXT — how the "
                "present level compares with the last 800,000 years?",
        "options": [
            {"text": "The Hawaii measurements",
             "correct": False,
             "why": "Hawaii's record runs back to 1958 and establishes the "
                    "trend, not the 800,000-year context."},
            {"text": "The isotope fingerprint",
             "correct": False,
             "why": "The isotopes identify the source of the carbon, not "
                    "how it compares with the deep past."},
            {"text": "The ice cores",
             "correct": True},
            {"text": "The laboratory work on the gas itself",
             "correct": False,
             "why": "The laboratory work supplies the mechanism, not a "
                    "record of the deep past."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e16",
        "band": "easier",
        "text": "Which piece of evidence establishes the SOURCE — where the "
                "extra carbon dioxide actually came from?",
        "options": [
            {"text": "The Hawaii measurements",
             "correct": False,
             "why": "Hawaii's record shows the amount rising; it says "
                    "nothing about where the carbon came from."},
            {"text": "The ice cores, going back 800,000 years",
             "correct": False,
             "why": "Ice cores show the historical range; identifying the "
                    "source is the isotope fingerprint's role."},
            {"text": "The laboratory work on the gas itself",
             "correct": False,
             "why": "The laboratory work shows what the gas does "
                    "chemically, not where the extra amount came from."},
            {"text": "The chemical fingerprint of the carbon's isotopes",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e17",
        "band": "easier",
        "text": "Which piece of evidence establishes the MECHANISM — a "
                "physical reason why the gas should warm anything at all?",
        "options": [
            {"text": "The laboratory measurement of infrared being absorbed",
             "correct": True},
            {"text": "The Hawaii measurements taken since 1958",
             "correct": False,
             "why": "Hawaii's record shows the amount changing over time; "
                    "it supplies no reason WHY that should warm anything."},
            {"text": "The ice cores",
             "correct": False,
             "why": "Ice cores establish the historical range, not a "
                    "physical reason for warming."},
            {"text": "The isotope fingerprint",
             "correct": False,
             "why": "The isotopes identify the source of the carbon, not a "
                    "physical mechanism for warming."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e18",
        "band": "easier",
        "text": "The Hawaii record shows a small yearly wobble on top of "
                "the long-term rise. What causes that wobble?",
        "options": [
            {"text": "The measuring instrument in Hawaii being serviced "
                     "and recalibrated once a year, on a fixed schedule",
             "correct": False,
             "why": "The wobble is a real seasonal pattern in the gas "
                    "itself, not an artefact of servicing equipment."},
            {"text": "Plants taking in carbon dioxide through the summer "
                     "growing season and releasing it again over winter",
             "correct": True},
            {"text": "Ocean currents changing direction with the seasons",
             "correct": False,
             "why": "The wobble is a biological pattern, driven by plant "
                    "growth and dieback, not by ocean currents."},
            {"text": "Volcanic activity varying from season to season",
             "correct": False,
             "why": "Volcanic activity is not seasonal in this way. The "
                    "wobble is driven by the yearly cycle of plant growth."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e19",
        "band": "easier",
        "text": "Sea level is rising for two separate reasons. What are "
                "they?",
        "options": [
            {"text": "Floating sea ice melting, and more rain falling into "
                     "the sea",
             "correct": False,
             "why": "Floating sea ice melting barely changes sea level, and "
                    "rain falling into the sea is not a net addition. The "
                    "two real reasons are land ice and thermal expansion."},
            {"text": "Rivers carrying more sediment, and the seabed rising",
             "correct": False,
             "why": "Neither sediment nor a rising seabed is named as a "
                    "reason. The two real reasons are land ice melting and "
                    "thermal expansion."},
            {"text": "Ice on land melting, and water expanding as it warms",
             "correct": True},
            {"text": "Increased evaporation, and stronger tides",
             "correct": False,
             "why": "Evaporation would lower sea level, not raise it, and "
                    "tides do not change the average level."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e20",
        "band": "easier",
        "text": "Which kind of ice, melting, actually raises sea level: "
                "land ice, or floating sea ice?",
        "options": [
            {"text": "Floating sea ice",
             "correct": False,
             "why": "Floating ice already displaces its own weight in "
                    "water, so melting it changes the level almost not at "
                    "all."},
            {"text": "Both contribute exactly equally",
             "correct": False,
             "why": "Land ice is the one that adds new water to the ocean. "
                    "Floating sea ice barely changes the level."},
            {"text": "Sea level rise comes just from thermal expansion, "
                     "with no other cause",
             "correct": False,
             "why": "Land ice melting is a real and separate contribution, "
                    "alongside thermal expansion."},
            {"text": "Land ice",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e21",
        "band": "easier",
        "text": "Near the top of an ice core, how are the years dated?",
        "options": [
            {"text": "By counting the annual layers, much like counting "
                     "tree rings",
             "correct": True},
            {"text": "By measuring how much dust has settled on the ice "
                     "surface each year",
             "correct": False,
             "why": "Dust is studied for other purposes; the years near the "
                    "top are dated by counting annual layers."},
            {"text": "By comparing the layers of ice against written "
                     "historical records",
             "correct": False,
             "why": "Written records do not go back far enough for most of "
                    "the core. The years are dated by counting layers."},
            {"text": "By measuring the temperature of the ice itself",
             "correct": False,
             "why": "Temperature is not what dates the layers; counting "
                    "them, like tree rings, is."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e22",
        "band": "easier",
        "text": "Deep inside an ice core, the layers are squeezed too thin "
                "to count individually. How is the ice dated there instead?",
        "options": [
            {"text": "By assuming each metre of depth represents exactly "
                     "the same number of years as near the top",
             "correct": False,
             "why": "Layers squeeze thinner with depth, so a fixed "
                    "metres-per-year assumption would not work. Flow models "
                    "are used instead."},
            {"text": "Using models of how the ice has flowed over time",
             "correct": True},
            {"text": "By carbon-dating the ice itself",
             "correct": False,
             "why": "Carbon-dating works on carbon-containing material of a "
                    "certain age range; the deep ice is dated using models "
                    "of ice flow."},
            {"text": "It cannot be dated any deeper than the counted "
                     "layers",
             "correct": False,
             "why": "The deepest ice can still be dated, using models of "
                    "how the ice flows, reaching back 800,000 years."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e23",
        "band": "easier",
        "text": "Roughly how far back do the deepest ice cores reach?",
        "options": [
            {"text": "About 8,000 years",
             "correct": False,
             "why": "That is a hundred times too recent. The deepest cores "
                    "reach back about 800,000 years."},
            {"text": "About 80 million years",
             "correct": False,
             "why": "That is a hundred times too far. The deepest cores "
                    "reach back about 800,000 years."},
            {"text": "About 800,000 years",
             "correct": True},
            {"text": "About 8 million years",
             "correct": False,
             "why": "That is ten times too far. The deepest cores reach "
                    "back about 800,000 years."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e24",
        "band": "easier",
        "text": "By roughly how many parts per million has carbon dioxide "
                "risen since 1750?",
        "options": [
            {"text": "By about 14 parts per million",
             "correct": False,
             "why": "That is ten times too small. Going from about 280 to "
                    "over 420 is a rise of over 140 parts per million."},
            {"text": "By about 1400 parts per million",
             "correct": False,
             "why": "That is ten times too large. Going from about 280 to "
                    "over 420 is a rise of over 140 parts per million."},
            {"text": "It has not risen by any measurable amount",
             "correct": False,
             "why": "It has risen substantially — from about 280 to over "
                    "420 parts per million."},
            {"text": "By over 140 parts per million",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e25",
        "band": "easier",
        "text": "Roughly how long does methane last in the atmosphere "
                "before it breaks down?",
        "options": [
            {"text": "About ten years",
             "correct": True},
            {"text": "About ten days",
             "correct": False,
             "why": "That is far too short. Methane lasts about ten years "
                    "before breaking down."},
            {"text": "About ten centuries",
             "correct": False,
             "why": "That is far too long. Methane lasts about ten years, "
                    "not ten centuries."},
            {"text": "It does not break down",
             "correct": False,
             "why": "Methane does break down, in about ten years. Carbon "
                    "dioxide is the one that lingers far longer."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e26",
        "band": "easier",
        "text": "Compared with methane's roughly ten-year lifetime, how "
                "long does carbon dioxide already in the air tend to stay "
                "there?",
        "options": [
            {"text": "For a much shorter time than methane",
             "correct": False,
             "why": "Carbon dioxide stays for far longer than methane, not "
                    "a shorter time."},
            {"text": "For a very long time — far longer than methane",
             "correct": True},
            {"text": "For exactly the same length of time as methane",
             "correct": False,
             "why": "The two gases persist for very different lengths of "
                    "time — carbon dioxide lingers far longer."},
            {"text": "It leaves the atmosphere within a few days",
             "correct": False,
             "why": "Carbon dioxide persists for a very long time once "
                    "released, not a few days."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e27",
        "band": "easier",
        "text": "The extra carbon dioxide in the air carries a lighter mix "
                "of carbon isotopes. What does that lighter mix point to as "
                "its origin?",
        "options": [
            {"text": "Volcanic rock deep underground",
             "correct": False,
             "why": "Volcanic carbon carries a different isotope signature. "
                    "The lighter mix points to once-living material."},
            {"text": "Carbon dioxide that has dissolved into the deep "
                     "oceans over time",
             "correct": False,
             "why": "Ocean-dissolved carbon dioxide does not carry this "
                    "particular lighter signature. Once-living material "
                    "does."},
            {"text": "Material that was once living, such as coal, oil or "
                     "gas",
             "correct": True},
            {"text": "Dust blown in from outer space",
             "correct": False,
             "why": "Space dust plays no part in this. The lighter isotope "
                    "mix points to once-living material such as fossil "
                    "fuels."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e28",
        "band": "easier",
        "text": "Four independent lines of evidence all agree on the cause "
                "of the rise. Why does independence matter here?",
        "options": [
            {"text": "Because independent evidence is automatically more "
                     "accurate than any other kind",
             "correct": False,
             "why": "Accuracy is not the point being made. What matters is "
                    "that separate lines of evidence agree rather than "
                    "disagreeing."},
            {"text": "Because it means just one scientist needs to check "
                     "each piece of evidence",
             "correct": False,
             "why": "How many scientists check each piece is not the point. "
                    "What matters is that the lines are independent of one "
                    "another and still agree."},
            {"text": "Because independent evidence cannot later turn out to "
                     "be wrong",
             "correct": False,
             "why": "Any evidence could in principle be revised. What "
                    "matters here is that four separate lines currently "
                    "agree."},
            {"text": "Because each one could have pointed a different way, "
                     "and none of them do",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e29",
        "band": "easier",
        "text": "Why does sea-level rise from a warming ocean continue for "
                "a very long time, even after air temperatures stop rising?",
        "options": [
            {"text": "Because the ocean is extremely deep, and it takes a "
                     "very long time for warming to work all the way "
                     "through it",
             "correct": True},
            {"text": "Because sea level rise has nothing to do with ocean "
                     "temperature",
             "correct": False,
             "why": "Ocean temperature is exactly what drives the "
                    "thermal-expansion part of sea-level rise."},
            {"text": "Because the ocean cools down again as soon as the air "
                     "does",
             "correct": False,
             "why": "The ocean's great depth means it responds far more "
                    "slowly than the air does, not immediately."},
            {"text": "Because ice keeps melting even after the air has "
                     "cooled",
             "correct": False,
             "why": "This question is about the OCEAN's slow response, not "
                    "about ice melting."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-e30",
        "band": "easier",
        "text": "Cement-making is named as a source of carbon dioxide. Is "
                "cement-making the same thing as burning a fossil fuel?",
        "options": [
            {"text": "Yes — cement is itself a kind of fossil fuel that "
                     "gets burned for energy",
             "correct": False,
             "why": "Cement is not a fossil fuel. It is named as a separate "
                    "human activity that releases carbon dioxide."},
            {"text": "No — it is a separate human activity that also "
                     "releases carbon dioxide",
             "correct": True},
            {"text": "Yes — cement factories run solely on burning coal, so "
                     "it comes to the same thing",
             "correct": False,
             "why": "Cement-making is named as its own separate source, "
                    "distinct from burning fossil fuels for energy."},
            {"text": "No — cement-making releases no carbon dioxide",
             "correct": False,
             "why": "Cement-making genuinely does release carbon dioxide; "
                    "that is why it is named alongside burning fossil fuels "
                    "and clearing forests."},
        ],
        "figure": None,
    },
    # -- standard --
    {
        "id": "c10-06-s09",
        "band": "standard",
        "text": "If every fossil fuel power station and vehicle stopped "
                "burning fuel tomorrow, but forests kept being cleared and "
                "cement kept being made, would human carbon dioxide "
                "emissions drop to zero?",
        "options": [
            {"text": "No — clearing forests and making cement would still "
                     "add carbon dioxide, just from a smaller share of the "
                     "total",
             "correct": True},
            {"text": "Yes — burning fossil fuels is the sole human source "
                     "of carbon dioxide there is, and everything else "
                     "people do leaves the air untouched",
             "correct": False,
             "why": "Clearing forests and making cement are both named as "
                    "additional sources, so emissions would not fall to "
                    "zero."},
            {"text": "Yes — forests and cement factories emit carbon "
                     "dioxide while fuel is also being burned nearby, and "
                     "not through their own separate release processes",
             "correct": False,
             "why": "Forest clearing and cement-making release carbon "
                    "dioxide through their own separate processes, not only "
                    "alongside burning fuel."},
            {"text": "It cannot be answered, since forests and cement are "
                     "not connected to carbon dioxide",
             "correct": False,
             "why": "Both are explicitly named as sources of the rise, so "
                    "the question can be answered — the answer is no."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s10",
        "band": "standard",
        "text": "Nitrogen and oxygen, 99% of the air, absorb no infrared at "
                "all. What does that imply about which gases actually "
                "control the planet's temperature?",
        "options": [
            {"text": "The temperature must be controlled mainly by nitrogen "
                     "and oxygen, since they make up almost all of the air "
                     "and so carry almost all of the heat in it",
             "correct": False,
             "why": "Neither gas absorbs infrared, so neither controls the "
                    "greenhouse effect, however abundant they are."},
            {"text": "A small minority of gases, rather than whichever gas "
                     "happens to be most abundant, decide the greenhouse "
                     "effect's strength",
             "correct": True},
            {"text": "No gas in the atmosphere can meaningfully affect the "
                     "temperature",
             "correct": False,
             "why": "Greenhouse gases such as carbon dioxide and methane do "
                    "control the temperature, despite being a tiny minority "
                    "of the air."},
            {"text": "The proportion of a gas in the air predicts how much "
                     "it affects temperature",
             "correct": False,
             "why": "The opposite is shown here — the two most abundant "
                    "gases affect temperature not at all."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s11",
        "band": "standard",
        "text": "A real greenhouse traps warmth mainly by stopping "
                "convection — warm air physically cannot escape past the "
                "glass. Since the atmosphere has no lid and air moves "
                "freely, what mechanism is left to explain the planet's "
                "warming?",
        "options": [
            {"text": "The atmosphere has an invisible barrier high above "
                     "us that stops warm air escaping, just as the glass "
                     "of a greenhouse does",
             "correct": False,
             "why": "Air is known to move freely through the atmosphere. "
                    "The real mechanism is radiation absorption, not a "
                    "hidden barrier."},
            {"text": "Sunlight becoming trapped between the ground and the "
                     "clouds, bouncing between the two until the ground "
                     "heats up",
             "correct": False,
             "why": "Sunlight passes straight through and warms the ground; "
                    "it is the infrared going back OUT that gets absorbed."},
            {"text": "Greenhouse gases absorbing outgoing infrared and "
                     "radiating some of it back towards the surface",
             "correct": True},
            {"text": "There is no remaining mechanism, so the warming must "
                     "be coming from inside the Earth rather than from "
                     "the air",
             "correct": False,
             "why": "The planet genuinely is warmed this way — by "
                    "absorption of infrared, not by trapping air."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s12",
        "band": "standard",
        "text": "Carbon dioxide was first measured absorbing heat "
                "radiation in the 1850s, decades before anyone debated "
                "climate change. Why does that timing matter?",
        "options": [
            {"text": "It shows the measurement must have been about "
                     "something other than climate, since climate change "
                     "was not yet known about",
             "correct": False,
             "why": "The measurement — that the gas absorbs heat "
                    "radiation — is exactly the physical basis the climate "
                    "case rests on today."},
            {"text": "It shows that scientists in the 1850s already "
                     "understood everything about modern climate change",
             "correct": False,
             "why": "They established one physical property of the gas. "
                    "Understanding of the full climate picture developed "
                    "much later."},
            {"text": "It shows the measurement has since been proven wrong "
                     "by later scientists",
             "correct": False,
             "why": "The measurement has held up and remains part of the "
                    "evidence used today; it was not overturned."},
            {"text": "It shows the underlying physical property was "
                     "established independently of any climate debate, so "
                     "it cannot be dismissed as evidence invented to fit a "
                     "conclusion",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s13",
        "band": "standard",
        "text": "Methane is short-lived (about ten years) and highly potent "
                "per molecule; carbon dioxide is far less potent per "
                "molecule but persists for a very long time. Why would "
                "cutting carbon dioxide emissions NOT show a quick result, "
                "unlike cutting methane?",
        "options": [
            {"text": "Because carbon dioxide already in the air stays there "
                     "for a very long time regardless of what happens to "
                     "new emissions",
             "correct": True},
            {"text": "Because carbon dioxide is not a greenhouse gas in the "
                     "way methane is",
             "correct": False,
             "why": "Carbon dioxide genuinely is a greenhouse gas — the "
                    "main one responsible for warming so far."},
            {"text": "Because there is far too little carbon dioxide in the "
                     "air for any cut to make a measurable difference to a "
                     "planet of this size",
             "correct": False,
             "why": "The amount is large enough to matter enormously. The "
                    "slow result is about its long LIFETIME, not its "
                    "amount."},
            {"text": "Because cutting carbon dioxide emissions is just as "
                     "fast as cutting methane emissions",
             "correct": False,
             "why": "It is markedly slower, precisely because carbon "
                    "dioxide persists so much longer once released."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s14",
        "band": "standard",
        "text": "The Hawaii curve dips slightly every summer before rising "
                "again. Why doesn't that seasonal dip contradict the claim "
                "that carbon dioxide is rising overall?",
        "options": [
            {"text": "The dip appears in years when the measurement is "
                     "taken incorrectly, and those years should be "
                     "removed from the record",
             "correct": False,
             "why": "The dip is a genuine, repeating seasonal signal from "
                    "plant growth, not a measurement error."},
            {"text": "The dip is a small, regular seasonal wobble riding on "
                     "top of a much larger long-term rise across every "
                     "decade",
             "correct": True},
            {"text": "The dip shows the rise has stopped and reversed every "
                     "year, so the long-term trend cancels itself out "
                     "over time",
             "correct": False,
             "why": "The curve still ends each year higher than it began. A "
                    "yearly dip is not the same as a reversal of the "
                    "overall trend."},
            {"text": "It does contradict the claim, and the rise should be "
                     "treated as uncertain",
             "correct": False,
             "why": "A small predictable seasonal wobble sitting on top of "
                    "a clear multi-decade rise does not undermine the "
                    "trend."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s15",
        "band": "standard",
        "text": "Floating sea ice already displaces its own weight in "
                "water. Using that fact, explain why melting it changes sea "
                "level by only a tiny amount.",
        "options": [
            {"text": "Floating sea ice is far too small in total volume to "
                     "matter, since almost all of the world's ice sits "
                     "on land instead",
             "correct": False,
             "why": "The volume is not the reason. The reason is the "
                    "physics of an object already floating and displacing "
                    "its own weight."},
            {"text": "Floating sea ice melts far more slowly than land ice "
                     "does, so its effect has not shown up yet",
             "correct": False,
             "why": "Speed of melting is not the reason. Even fully melted, "
                    "floating ice changes the level by almost nothing, "
                    "because of what it already displaces."},
            {"text": "The water it turns into occupies almost exactly the "
                     "space the floating ice was already displacing",
             "correct": True},
            {"text": "Melting floating ice lowers sea level rather than "
                     "raising it, because the meltwater soaks away into "
                     "the seabed",
             "correct": False,
             "why": "It does not lower sea level either — the change either "
                    "way is negligible, for the displacement reason given."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s16",
        "band": "standard",
        "text": "Near the top of an ice core, years are counted like tree "
                "rings. Why does that method stop working further down?",
        "options": [
            {"text": "The deeper ice is a completely different substance "
                     "from the ice nearer the top",
             "correct": False,
             "why": "It is the same ice, simply compressed by the weight "
                    "above. The layers become too thin to count, not a "
                    "different substance."},
            {"text": "Scientists are not permitted to drill deep enough to "
                     "reach those layers",
             "correct": False,
             "why": "Deep cores are drilled and studied; the reason "
                    "counting fails is the physical compression of the "
                    "layers, not access."},
            {"text": "The annual layers simply stop forming once the ice "
                     "below is old enough, so there is nothing left down "
                     "there to count",
             "correct": False,
             "why": "Layers continue to form every year; they just become "
                    "too thin to count individually once compressed."},
            {"text": "The weight of ice above compresses the deeper layers "
                     "so thin that individual years can no longer be told "
                     "apart",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s17",
        "band": "standard",
        "text": "The isotope fingerprint rules out volcanoes and the oceans "
                "as the source of the extra carbon dioxide. Why can it do "
                "that, when all three release carbon dioxide?",
        "options": [
            {"text": "Because carbon from once-living material carries a "
                     "measurably different, lighter mix of isotopes than "
                     "carbon from volcanoes or the oceans",
             "correct": True},
            {"text": "Because volcanoes and the oceans have not released "
                     "any carbon dioxide in recent history",
             "correct": False,
             "why": "Both continue to release carbon dioxide. What rules "
                    "them out here is the isotope signature, not an absence "
                    "of release."},
            {"text": "Because the isotope test detects solely carbon "
                     "dioxide that came from burning fuel",
             "correct": False,
             "why": "The test measures isotope ratios in general; it "
                    "distinguishes once-living carbon from other sources by "
                    "their different signatures."},
            {"text": "Because volcanoes and oceans release a different gas "
                     "entirely, not carbon dioxide",
             "correct": False,
             "why": "Both genuinely release carbon dioxide. What differs is "
                    "the isotope ratio within it, not the gas itself."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s18",
        "band": "standard",
        "text": "A critic says the Hawaii graph alone proves humans caused "
                "the rise, since it has climbed every year since 1958. What "
                "is missing from that argument?",
        "options": [
            {"text": "Nothing is missing — a rising trend measured this "
                     "carefully is already a complete proof",
             "correct": False,
             "why": "A trend on its own does not establish either where the "
                    "carbon came from or why it should warm anything."},
            {"text": "Anything establishing the SOURCE of the extra carbon "
                     "or a MECHANISM for why it would warm anything — the "
                     "Hawaii record shows only the trend",
             "correct": True},
            {"text": "A longer time period, since 1958 to today is not "
                     "considered a long enough span to measure a trend",
             "correct": False,
             "why": "The length of the Hawaii record is not the problem — "
                    "what it lacks is evidence of source and mechanism, not "
                    "more years."},
            {"text": "A second measuring station, since one location cannot "
                     "show a genuine trend",
             "correct": False,
             "why": "The record's role is showing the trend, which one "
                    "well-chosen location already does. What is missing is "
                    "source and mechanism evidence."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s19",
        "band": "standard",
        "text": "Hawaii is a single location far from any city. Why does "
                "measuring the trend there, rather than in a busy city "
                "centre, make the trend MORE convincing?",
        "options": [
            {"text": "Because a city centre could not contain any carbon "
                     "dioxide",
             "correct": False,
             "why": "Cities do contain carbon dioxide; the concern with "
                    "measuring there is LOCAL pollution skewing the "
                    "reading, not an absence of the gas."},
            {"text": "Because Hawaii's volcanoes add carbon dioxide, making "
                     "the reading more representative, rather than "
                     "strengthening a background reading of the whole "
                     "atmosphere",
             "correct": False,
             "why": "Local volcanic gas would be exactly the kind of local "
                    "effect that would distort a background reading, not "
                    "strengthen it."},
            {"text": "Because a location far from local pollution sources "
                     "is measuring the background level of the whole "
                     "atmosphere, not a local effect",
             "correct": True},
            {"text": "Because a single location is inherently more accurate "
                     "than measuring in several places at once",
             "correct": False,
             "why": "The advantage is not about having only one location — "
                    "it is about that location being free of local "
                    "pollution sources."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s20",
        "band": "standard",
        "text": "Ice cores show the CONTEXT (the 800,000-year range) and "
                "Hawaii shows the TREND (the recent rise). Why is neither "
                "one, on its own, enough?",
        "options": [
            {"text": "Both pieces of evidence are measuring exactly the "
                     "same thing, because the Hawaii record was calibrated "
                     "against the ice cores in the first place, so whichever "
                     "of the two you have is already enough on its own",
             "correct": False,
             "why": "They measure different things — one the historical "
                    "range, the other the recent change — which is exactly "
                    "why both are needed together."},
            {"text": "Neither piece of evidence is reliable enough to use "
                     "even in combination with the other",
             "correct": False,
             "why": "Both are treated as reliable; the point is that each "
                    "supplies something the other cannot on its own."},
            {"text": "Ice cores and Hawaii's record disagree with each "
                     "other, so at least one of them must be wrong",
             "correct": False,
             "why": "They do not disagree — used together, they reinforce "
                    "rather than contradict one another."},
            {"text": "The context alone cannot show today's level is "
                     "unusual without a recent trend to compare it against, "
                     "and the trend alone cannot show how unusual it is "
                     "without the long-term context",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s21",
        "band": "standard",
        "text": "If the laboratory measurement of carbon dioxide absorbing "
                "infrared had never been made, what would happen to the "
                "strength of the overall case for human-caused warming?",
        "options": [
            {"text": "It would weaken considerably, since the remaining "
                     "evidence would show correlation and source without "
                     "any physical reason connecting them to warming",
             "correct": True},
            {"text": "It would make no difference, since the other three "
                     "lines of evidence already prove causation by "
                     "themselves",
             "correct": False,
             "why": "Trend, context and source do not by themselves supply "
                    "a REASON the gas should warm anything — that is "
                    "exactly the laboratory evidence's job."},
            {"text": "It would strengthen the case, since fewer pieces of "
                     "evidence are easier to check",
             "correct": False,
             "why": "Fewer pieces of evidence make the case weaker, not "
                    "stronger, particularly when the missing piece is the "
                    "one supplying a mechanism."},
            {"text": "It would have no effect on climate itself, so it "
                     "would not matter scientifically either",
             "correct": False,
             "why": "The question is about the STRENGTH OF THE CASE for the "
                    "cause, not about climate itself changing."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s22",
        "band": "standard",
        "text": "Methane comes partly from livestock and partly from "
                "leaking gas pipes. Why might tackling the leaks appeal as "
                "an early target, compared with reducing livestock numbers?",
        "options": [
            {"text": "Gas leaks release far more methane in total than "
                     "livestock do worldwide, so sealing them removes the "
                     "larger of the two sources",
             "correct": False,
             "why": "Nothing here establishes gas leaks as the larger total "
                    "source. The appeal argued for is ease and cost, not "
                    "sheer scale."},
            {"text": "A leak is pure waste with no other purpose, so "
                     "sealing it costs less disruption than reducing an "
                     "entire industry",
             "correct": True},
            {"text": "Livestock do not produce any methane, contrary to "
                     "popular belief",
             "correct": False,
             "why": "Livestock genuinely are a named methane source. The "
                    "comparison is about how easily each source can be "
                    "tackled."},
            {"text": "Gas leaks are the sole source of methane that can be "
                     "measured accurately",
             "correct": False,
             "why": "Measurement accuracy is not the point being made. The "
                    "appeal is that fixing a leak is simpler than reducing "
                    "an entire industry."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s23",
        "band": "standard",
        "text": "Explain, using the ocean's depth, why a rise in sea level "
                "from thermal expansion can keep happening for centuries "
                "after the air above has stopped warming.",
        "options": [
            {"text": "The ocean warms up faster than the air does, so it "
                     "finishes expanding first",
             "correct": False,
             "why": "The ocean's great depth makes it respond MORE slowly "
                    "than the air, not faster."},
            {"text": "Thermal expansion has nothing to do with how deep the "
                     "ocean is",
             "correct": False,
             "why": "Depth is exactly why the process is slow — heat has a "
                    "great volume of water to work through before the whole "
                    "ocean has expanded."},
            {"text": "Heat takes a very long time to spread all the way "
                     "down through such a deep body of water, so the deep "
                     "ocean is still warming and expanding long after the "
                     "surface and air have levelled off",
             "correct": True},
            {"text": "Sea level stops rising the moment air temperature "
                     "stabilises, because water carries heat downwards so "
                     "quickly that the whole depth of the ocean is always at "
                     "the same temperature as the air above it",
             "correct": False,
             "why": "The two are not directly linked in that way — the deep "
                    "ocean continues warming and expanding well after the "
                    "air stabilises."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s24",
        "band": "standard",
        "text": "A student says: 'Nitrogen and oxygen make up almost all "
                "the air, so they must control the temperature.' What is "
                "the flaw in that reasoning?",
        "options": [
            {"text": "The flaw is that nitrogen and oxygen do not make up "
                     "almost all of the air, because water vapour is the "
                     "majority gas",
             "correct": False,
             "why": "They genuinely do make up about 99% of dry air. The "
                    "flaw is in what is inferred from that fact, not the "
                    "fact itself."},
            {"text": "The flaw is that temperature is not affected by any "
                     "gas in the atmosphere, but only by how much "
                     "sunlight arrives at the ground",
             "correct": False,
             "why": "Temperature is affected by greenhouse gases, which is "
                    "exactly what the student's reasoning overlooks."},
            {"text": "There is no flaw — the most abundant gases do control "
                     "the temperature",
             "correct": False,
             "why": "Nitrogen and oxygen absorb no infrared and so play no "
                    "part in the greenhouse effect, despite their "
                    "abundance."},
            {"text": "It assumes abundance decides chemical importance, "
                     "when in fact neither gas absorbs infrared at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s25",
        "band": "standard",
        "text": "Why is the isotope evidence described as identifying the "
                "source, rather than as proving how much warming there will "
                "be?",
        "options": [
            {"text": "Because a fingerprint can say WHERE something came "
                     "from without saying anything about HOW MUCH effect it "
                     "will have",
             "correct": True},
            {"text": "Because the isotope measurement has never been "
                     "carried out on real air samples, only on coal and oil "
                     "in a laboratory",
             "correct": False,
             "why": "The measurement genuinely has been made on real extra "
                    "carbon dioxide in the air, and it does identify a "
                    "source."},
            {"text": "Because isotopes have no connection whatsoever to "
                     "carbon dioxide of any kind",
             "correct": False,
             "why": "Isotopes are a real property of carbon atoms, and the "
                    "fingerprint depends on measuring exactly that "
                    "property."},
            {"text": "Because the amount of warming has already been "
                     "calculated from the isotopes alone",
             "correct": False,
             "why": "The isotopes are not used to calculate an amount of "
                    "warming; they are used to identify where the carbon "
                    "came from."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s26",
        "band": "standard",
        "text": "Why does the lesson treat 'clearing forests' as adding to "
                "carbon dioxide, rather than as simply removing trees?",
        "options": [
            {"text": "Because clearing forests directly burns fossil fuels "
                     "that are commonly found stored underneath them, "
                     "rather than through the mechanism described here",
             "correct": False,
             "why": "There are no fossil fuels being burned in this "
                    "process. The effect is on trees removing carbon "
                    "dioxide and releasing what they stored."},
            {"text": "Because trees that would otherwise be absorbing "
                     "carbon dioxide are removed, and the carbon stored in "
                     "them is often released as well",
             "correct": True},
            {"text": "Because forests naturally produce more carbon dioxide "
                     "than they ever absorb",
             "correct": False,
             "why": "Growing forests are a net absorber of carbon dioxide; "
                    "clearing them removes that absorption and can release "
                    "stored carbon."},
            {"text": "Because the wood from cleared forests is shipped "
                     "abroad and burned there",
             "correct": False,
             "why": "That is not the mechanism described. The effect is "
                    "losing the trees' ongoing absorption and releasing "
                    "carbon they had stored."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s27",
        "band": "standard",
        "text": "Someone argues methane should be humanity's top priority, "
                "since it is far more potent per molecule than carbon "
                "dioxide. What does that argument leave out?",
        "options": [
            {"text": "That methane is not a greenhouse gas, despite its "
                     "potency per molecule",
             "correct": False,
             "why": "Methane genuinely is a greenhouse gas, and a potent "
                    "one — that much of the argument is correct."},
            {"text": "That livestock do not produce any methane",
             "correct": False,
             "why": "Livestock are a genuine methane source. What the "
                    "argument leaves out is carbon dioxide's much larger "
                    "overall contribution."},
            {"text": "That carbon dioxide is far more abundant and persists "
                     "for far longer, so it is responsible for most of the "
                     "warming that has already happened",
             "correct": True},
            {"text": "That potency per molecule is the only property that "
                     "decides a gas's effect, so how much of it is in the "
                     "air and how long it lasts make no difference at all",
             "correct": False,
             "why": "Potency per molecule is real, but abundance and "
                    "lifetime matter just as much — and those are exactly "
                    "what the argument leaves out."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s28",
        "band": "standard",
        "text": "The isotope fingerprint, the Hawaii trend, the ice-core "
                "context and the laboratory mechanism are each said to "
                "establish something 'alone'. What does adding the word "
                "'alone' to each one signal?",
        "options": [
            {"text": "That each piece of evidence is completely worthless "
                     "without the others, so none of them means anything "
                     "by itself",
             "correct": False,
             "why": "Each piece IS genuine evidence for something on its "
                    "own — the word signals a LIMIT, not worthlessness."},
            {"text": "That just one of the four pieces is trustworthy, and "
                     "the other three are there to make the case look "
                     "stronger than it is",
             "correct": False,
             "why": "All four are treated as genuine and complementary, not "
                    "as one trustworthy piece among three decorative ones."},
            {"text": "That scientists are unsure which of the four pieces "
                     "to believe, and are waiting for one of them to win "
                     "out",
             "correct": False,
             "why": "There is no uncertainty about which to believe — the "
                    "word 'alone' signals what each one, by itself, cannot "
                    "show."},
            {"text": "That each piece is limited on its own, and the full "
                     "case depends on putting all four together",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s29",
        "band": "standard",
        "text": "Explain why a scientist would want the isotope evidence "
                "AND the laboratory evidence, rather than treating either "
                "one as making the other redundant.",
        "options": [
            {"text": "One shows WHERE the extra carbon came from and the "
                     "other shows WHY that carbon should warm anything — "
                     "neither question answers the other",
             "correct": True},
            {"text": "Because the two pieces of evidence measure exactly "
                     "the same underlying fact, so having both of them "
                     "simply doubles the confidence in one single result",
             "correct": False,
             "why": "They measure different things — origin, and a physical "
                    "mechanism — not the same fact twice."},
            {"text": "Because the isotope evidence is now considered "
                     "unreliable and needs the laboratory work to replace "
                     "it",
             "correct": False,
             "why": "The isotope evidence is not treated as unreliable; it "
                    "answers a genuinely different question from the "
                    "laboratory work."},
            {"text": "Because just one of the two can be measured in any "
                     "given decade",
             "correct": False,
             "why": "Both can be and have been measured. The reason both "
                    "matter is that they answer different questions, not a "
                    "scheduling limit."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-s30",
        "band": "standard",
        "text": "Why does describing the ozone layer as 'the problem "
                "humanity actually fixed' matter for how this lesson talks "
                "about carbon dioxide?",
        "options": [
            {"text": "It shows the ozone layer and the greenhouse effect "
                     "are the same problem with two different names",
             "correct": False,
             "why": "They remain two separate problems with different gases "
                    "and mechanisms. The point being made is about what "
                    "successfully fixing a global problem shows."},
            {"text": "It shows a global atmospheric problem CAN be "
                     "identified, understood and acted on successfully, "
                     "which is evidence rather than empty reassurance",
             "correct": True},
            {"text": "It shows carbon dioxide will fix itself over time, "
                     "the same way the ozone layer is recovering",
             "correct": False,
             "why": "The two situations are not claimed to resolve the same "
                    "way. The point is that a fix is POSSIBLE, not "
                    "automatic."},
            {"text": "It shows that scientists were wrong about the ozone "
                     "layer being a serious problem in the first place",
             "correct": False,
             "why": "The ozone layer was a genuine serious problem, which "
                    "is exactly why fixing it is offered as evidence that "
                    "action can work."},
        ],
        "figure": None,
    },
    # -- harder --
    {
        "id": "c10-06-h09",
        "band": "harder",
        "text": "A student argues that since nitrogen and oxygen make up "
                "99% of the air, any change to THEIR proportions would "
                "affect climate far more than a change to carbon dioxide's "
                "tiny 0.04%. Is that argument sound?",
        "options": [
            {"text": "No — proportion of the air is irrelevant to the "
                     "greenhouse effect, since neither nitrogen nor oxygen "
                     "absorbs infrared at all, however much of either there "
                     "is",
             "correct": True},
            {"text": "Yes — a change to 99% of the air must outweigh a "
                     "change to 0.04% of it, whichever gases are involved",
             "correct": False,
             "why": "The greenhouse effect depends on which gases absorb "
                    "infrared, not on sheer proportion. Neither majority "
                    "gas absorbs any."},
            {"text": "Yes — but solely because nitrogen and oxygen are "
                     "chemically identical to carbon dioxide",
             "correct": False,
             "why": "The three gases are chemically very different. Carbon "
                    "dioxide absorbs infrared; nitrogen and oxygen do not, "
                    "whatever their proportions."},
            {"text": "No — but solely because carbon dioxide is, by some "
                     "measure, more abundant overall than nitrogen and "
                     "oxygen are when combined together across the whole "
                     "atmosphere",
             "correct": False,
             "why": "Carbon dioxide is far LESS abundant, at 0.04%. The "
                    "reason the argument fails is about chemistry, not "
                    "about which gas is more common."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h10",
        "band": "harder",
        "text": "The 'greenhouse effect' name survives even though the "
                "mechanism is wrong, because the specification's own "
                "vocabulary uses it and every exam paper and textbook "
                "depends on it. What kind of trade-off does keeping a "
                "misleading name represent?",
        "options": [
            {"text": "No trade-off, since the name is entirely accurate "
                     "once explained",
             "correct": False,
             "why": "The name genuinely does suggest the wrong mechanism "
                    "(trapping air) even after the true one is explained. "
                    "There is a real cost to keeping it."},
            {"text": "Trading a small, correctable inaccuracy in the name "
                     "for a large practical gain: being able to read and "
                     "discuss the same material as everyone else",
             "correct": True},
            {"text": "A trade-off between two equally strong scientific "
                     "explanations, with no clearly correct one",
             "correct": False,
             "why": "There is a single correct mechanism — absorption of "
                    "infrared. The trade-off is about keeping a familiar "
                    "but misleading NAME, not about competing explanations."},
            {"text": "A trade-off that affects merely how the topic is "
                     "marked in an exam, with no effect on understanding",
             "correct": False,
             "why": "It affects understanding too — a name that implies the "
                    "wrong mechanism has to be actively corrected, which is "
                    "exactly why the page adds a closing panel."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h11",
        "band": "harder",
        "text": "Foote and Tyndall's 1850s measurement predates any climate "
                "policy debate by well over a century. Someone argues that "
                "modern climate scientists could have unconsciously "
                "designed their later experiments to confirm what they "
                "already believed. Does that concern apply to the 1850s "
                "measurement itself?",
        "options": [
            {"text": "Yes — Foote and Tyndall were already committed "
                     "campaigners on climate policy, and set out to show "
                     "that burning coal would one day warm the planet",
             "correct": False,
             "why": "There was no climate policy debate for anyone to be "
                    "committed to in the 1850s. The concern could not have "
                    "applied to them."},
            {"text": "Yes — every scientific measurement ever made is "
                     "equally vulnerable to this kind of bias, so the "
                     "date it was taken on makes no difference at all",
             "correct": False,
             "why": "The specific concern raised is about being biased "
                    "TOWARDS AN EXISTING CONCLUSION, which requires the "
                    "conclusion to already exist — it did not, in the "
                    "1850s."},
            {"text": "No — nobody in the 1850s had a climate conclusion to "
                     "be biased towards, since the debate the concern "
                     "describes did not yet exist",
             "correct": True},
            {"text": "It cannot be judged, since a scientist's private "
                     "motives can never be recovered from the measurement "
                     "they published",
             "correct": False,
             "why": "Knowing their private thoughts is not required — the "
                    "debate itself simply had not started yet, which is "
                    "enough to answer the question."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h12",
        "band": "harder",
        "text": "Methane's short lifetime means a cut shows results within "
                "a decade; carbon dioxide's long lifetime means a cut shows "
                "results only over centuries. If the goal were to avoid the "
                "WORST long-term warming rather than to show a quick "
                "result, which gas would matter more?",
        "options": [
            {"text": "Methane, since anything with a quicker visible result "
                     "must also be the more important gas long-term, "
                     "whatever the goal happens to be",
             "correct": False,
             "why": "Speed of visible result and long-term importance are "
                    "different things. Carbon dioxide's persistence makes "
                    "it the one that decides the long-term outcome."},
            {"text": "Neither gas matters more than the other, since both "
                     "are described as greenhouse gases",
             "correct": False,
             "why": "Being a greenhouse gas does not make two gases equally "
                    "important for every purpose — their different "
                    "lifetimes make them suited to different goals."},
            {"text": "Methane, since it is described as more potent per "
                     "molecule than carbon dioxide",
             "correct": False,
             "why": "Potency per molecule matters for methane's SHORT-term "
                    "effect. Long-term accumulation is decided by carbon "
                    "dioxide's persistence, not by potency alone."},
            {"text": "Carbon dioxide, since it is what accumulates and "
                     "determines how much warming is ultimately locked in, "
                     "regardless of how quickly a methane cut shows up",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h13",
        "band": "harder",
        "text": "The Hawaii record's yearly wobble is caused by the "
                "Northern Hemisphere's plants breathing with the seasons. "
                "Would you expect an equivalent station in the Southern "
                "Hemisphere to show its wobble at the SAME point in the "
                "calendar year?",
        "options": [
            {"text": "No — the Southern Hemisphere's growing season is "
                     "roughly six months out of step with the Northern "
                     "Hemisphere's, so its wobble would be shifted by about "
                     "half a year",
             "correct": True},
            {"text": "Yes — the whole planet experiences summer and winter "
                     "at exactly the same time, wherever the measuring "
                     "station happens to be located anywhere on the "
                     "surface of the whole wide globe",
             "correct": False,
             "why": "The two hemispheres have OPPOSITE seasons at any given "
                    "calendar month, which would shift the timing of the "
                    "wobble."},
            {"text": "Yes — the wobble is caused by the measuring "
                     "instrument itself, not by anything occurring in "
                     "either hemisphere over the course of the whole year, "
                     "whichever station happens to be doing the measuring",
             "correct": False,
             "why": "The wobble is caused by a genuine biological process "
                    "(plant growth and dieback), not by the instrument."},
            {"text": "No — but solely because there are no significant "
                     "plants growing anywhere in the Southern Hemisphere",
             "correct": False,
             "why": "The Southern Hemisphere does have significant plant "
                    "life. The real reason for a difference is the opposite "
                    "timing of its seasons."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h14",
        "band": "harder",
        "text": "A skyscraper's glass windows heat its interior partly by "
                "letting sunlight in and partly by trapping warmed air, "
                "since the windows can be sealed shut. Is that closer to "
                "how a garden greenhouse works, or to how the atmosphere "
                "works?",
        "options": [
            {"text": "Closer to the atmosphere — both work purely by "
                     "absorbing infrared radiation, and whether a window "
                     "is sealed makes no difference to how warm a room "
                     "gets",
             "correct": False,
             "why": "A sealed skyscraper's windows physically stop air "
                    "escaping, which is a barrier mechanism — the same kind "
                    "a garden greenhouse uses, not the atmosphere's."},
            {"text": "Closer to a garden greenhouse — both rely on a "
                     "physical barrier stopping warm air escaping, which "
                     "the open atmosphere has no equivalent of",
             "correct": True},
            {"text": "Equally close to both, since all three warm up using "
                     "exactly the same physical process, whatever is or is "
                     "not sealed shut and whatever the walls are made of",
             "correct": False,
             "why": "The atmosphere has no sealed barrier at all; a "
                    "skyscraper and a greenhouse both do. They are not "
                    "equally close to both."},
            {"text": "Closer to neither, since skyscrapers do not get "
                     "warmer than the air outside them",
             "correct": False,
             "why": "Sealed glass buildings are well known to heat up "
                    "considerably inside. The comparison is about WHICH "
                    "mechanism applies, not whether warming happens."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h15",
        "band": "harder",
        "text": "Four lines of evidence establish trend, context, source "
                "and mechanism respectively. If a FIFTH line of evidence "
                "were discovered that also established 'mechanism', what "
                "would that do to the case?",
        "options": [
            {"text": "It would complete the case, since a fifth piece of "
                     "evidence is stronger than four",
             "correct": False,
             "why": "More evidence of a role already covered adds "
                    "confirmation, not a new kind of support. The case was "
                    "already complete across all four roles with the "
                    "original four."},
            {"text": "It would weaken the case, since two pieces agreeing "
                     "on the same role must mean one of them is unreliable, "
                     "rather than completing something that was still "
                     "missing",
             "correct": False,
             "why": "Two independent measurements of the same mechanism "
                    "agreeing strengthens confidence in that finding; it "
                    "does not imply either is unreliable."},
            {"text": "It would add confirmation to the existing mechanism "
                     "evidence, but would not fill any of the three gaps "
                     "the other three roles already cover",
             "correct": True},
            {"text": "It would replace the need for the trend and context "
                     "evidence entirely, since a mechanism proven twice over "
                     "in the laboratory settles the whole case on its own",
             "correct": False,
             "why": "A second mechanism finding says nothing about trend or "
                    "context, which remain necessary and unaffected."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h16",
        "band": "harder",
        "text": "Sea level rises from land ice melting AND from thermal "
                "expansion. If land ice stopped melting entirely today but "
                "the ocean kept warming, would sea level stop rising?",
        "options": [
            {"text": "Yes — without melting land ice, there is no remaining "
                     "process that could raise sea level further, since "
                     "no new water is being added",
             "correct": False,
             "why": "Thermal expansion is a separate, independent process "
                    "from land ice melting and would continue on its own."},
            {"text": "Yes — thermal expansion only happens at the same time "
                     "as land ice is melting, because the meltwater is "
                     "what carries the heat into the sea",
             "correct": False,
             "why": "The two processes are independent of each other. "
                    "Thermal expansion continues whenever the ocean is "
                    "warming, whether or not land ice is melting."},
            {"text": "It cannot be judged, since thermal expansion is far "
                     "too small an effect to separate from ordinary tides "
                     "and waves",
             "correct": False,
             "why": "Thermal expansion is a measured, well-understood "
                    "physical process — water demonstrably takes up more "
                    "volume as it warms."},
            {"text": "No — thermal expansion alone would continue to raise "
                     "sea level for as long as the ocean kept warming",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h17",
        "band": "harder",
        "text": "Ice-core dating relies on counting layers near the surface "
                "and on flow models deeper down. If the flow models used "
                "for the deepest, oldest ice turned out to be slightly "
                "wrong, what part of the climate case would that affect "
                "MOST directly?",
        "options": [
            {"text": "The claim about exactly how far back the 800,000-year "
                     "range extends and its precise dates, rather than the "
                     "fact that the present level is unusually high",
             "correct": True},
            {"text": "The Hawaii measurements, since every other line of "
                     "climate evidence has to be dated against the ice-core "
                     "timescale before it can be compared with anything "
                     "else",
             "correct": False,
             "why": "Hawaii's direct atmospheric measurements do not depend "
                    "on ice-core dating at all — they are an independent, "
                    "separate line of evidence."},
            {"text": "The isotope fingerprint, since isotopes are measured "
                     "using the same flow models as ice cores",
             "correct": False,
             "why": "The isotope fingerprint is measured directly on carbon "
                    "dioxide samples; it does not rely on ice flow models."},
            {"text": "Nothing, since the exact dating of deep ice plays no "
                     "part in the climate case",
             "correct": False,
             "why": "The dating does matter for the ice cores' own "
                    "800,000-year claim, even though other lines of "
                    "evidence do not depend on it."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h18",
        "band": "harder",
        "text": "The isotope fingerprint shows the extra carbon is "
                "'lighter' because plants preferentially take up the "
                "lighter isotope during photosynthesis. Coal, oil and gas "
                "all formed from once-living material. What would you "
                "predict about volcanic carbon dioxide's isotope signature, "
                "given that it never passed through a living thing?",
        "options": [
            {"text": "It should carry an identical isotope mix to "
                     "fossil-fuel carbon, since all carbon dioxide is "
                     "chemically the same, since photosynthesis is what "
                     "shifts the isotope ratio in the first place",
             "correct": False,
             "why": "Being the same chemical compound does not mean "
                    "identical isotope ratios — the biological process of "
                    "photosynthesis is what shifts the ratio."},
            {"text": "It should carry a heavier isotope mix than "
                     "fossil-fuel carbon, since it was never subject to the "
                     "same preferential uptake by living things",
             "correct": True},
            {"text": "It should carry no carbon isotopes of any kind at "
                     "all, since the different isotopes are only created "
                     "inside living cells during photosynthesis",
             "correct": False,
             "why": "Volcanic carbon dioxide still contains carbon atoms "
                    "with the normal mix of isotopes; what differs is the "
                    "ratio, not their presence."},
            {"text": "It is impossible to predict anything about volcanic "
                     "carbon's isotopes without measuring it directly first",
             "correct": False,
             "why": "The reasoning given — that photosynthesis shifts the "
                    "ratio and volcanic carbon never underwent "
                    "photosynthesis — supports a clear prediction."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h19",
        "band": "harder",
        "text": "A politician says: 'Scientists still argue about climate "
                "change, so nothing is really settled.' Using the "
                "distinction between what is established and what is not "
                "yet decided, what is the most accurate reply?",
        "options": [
            {"text": "Nothing about climate change has ever been "
                     "established by any scientist, so the politician is "
                     "entirely correct and the whole topic remains wide "
                     "open",
             "correct": False,
             "why": "Four independent lines of evidence are described as "
                    "agreeing on the cause. That part is settled, even "
                    "though the future amount of warming is not."},
            {"text": "Every detail of climate change, including exactly how "
                     "many degrees warmer it will get by any given year, is "
                     "already fully settled",
             "correct": False,
             "why": "The future amount and rate of warming are explicitly "
                    "described as depending on how much more is burned — "
                    "that part is not settled."},
            {"text": "The CAUSE of the warming so far is well established; "
                     "what remains genuinely open is how much warmer it "
                     "gets and how fast, which depends on future choices",
             "correct": True},
            {"text": "Scientific disagreement about any aspect of a topic "
                     "means the whole topic is unsettled",
             "correct": False,
             "why": "A topic can have some settled parts (the cause) and "
                    "some genuinely open parts (the future amount) at the "
                    "same time."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h20",
        "band": "harder",
        "text": "Clearing a forest both stops it absorbing future carbon "
                "dioxide AND can release carbon it had already stored. "
                "Which of those two effects would you expect to show up in "
                "the atmosphere FIRST?",
        "options": [
            {"text": "The lost future absorption, since carbon locked "
                     "into the wood of a tree cannot be released again once "
                     "the tree has finished growing, while the absorption "
                     "the forest would have done stops the moment it is "
                     "felled",
             "correct": False,
             "why": "Stored carbon genuinely can be released quickly, "
                    "particularly if the cleared trees are burned."},
            {"text": "Both effects happen at exactly the same instant, with "
                     "no difference in timing",
             "correct": False,
             "why": "One is a rapid, one-off release; the other is a "
                    "gradual loss spread over the years the forest would "
                    "otherwise have kept absorbing carbon."},
            {"text": "Neither effect can be detected in the atmosphere at "
                     "any point",
             "correct": False,
             "why": "Both effects genuinely add to atmospheric carbon "
                    "dioxide over time and are part of why forest clearing "
                    "is named as a contributing cause."},
            {"text": "The release of already-stored carbon, which can "
                     "happen quickly if the cleared material is burned or "
                     "left to decay, while lost future absorption only "
                     "shows up gradually over the years that follow",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h21",
        "band": "harder",
        "text": "Someone claims warming stopped in a particular decade "
                "because one especially hot year was followed by a slightly "
                "cooler one. Using the weather-versus-climate distinction, "
                "what is the error?",
        "options": [
            {"text": "Two individual years are weather-scale data points, "
                     "and climate is judged over decades — a single cooler "
                     "year no more ends a warming trend than a single cold "
                     "week ends summer",
             "correct": True},
            {"text": "There is no error — two consecutive years moving in "
                     "opposite directions is already enough to disprove any "
                     "long-term trend, since a genuine trend has to rise in "
                     "every single year to count as one",
             "correct": False,
             "why": "A trend measured over decades is not overturned by two "
                    "individual years, in the same way a single cold week "
                    "does not overturn a season."},
            {"text": "The error is that hot years and cool years cannot be "
                     "compared with each other",
             "correct": False,
             "why": "They can be compared — the error is in treating a "
                    "short-term comparison as evidence about a long-term "
                    "trend."},
            {"text": "The error is that only the hottest year on record is "
                     "ever valid climate evidence",
             "correct": False,
             "why": "No single year, hot or cool, settles a decades-long "
                    "trend on its own — that is the actual error being "
                    "made."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h22",
        "band": "harder",
        "text": "The lesson gives four evidence roles as a CLOSED set: "
                "trend, context, source, mechanism. If a new piece of "
                "evidence were found that fit into a genuinely FIFTH role "
                "no existing entry covers, what would that do to the "
                "framework?",
        "options": [
            {"text": "Nothing — a framework described as a closed set "
                     "cannot be revised by any new finding",
             "correct": False,
             "why": "A framework being useful now does not make it "
                    "permanently unrevisable; a genuine new role would be "
                    "reason to reconsider it."},
            {"text": "It would show the framework's four roles are not "
                     "exhaustive after all, and the set would need to be "
                     "revised rather than treated as fixed",
             "correct": True},
            {"text": "It would automatically get sorted into one of the "
                     "four existing roles, because any piece of evidence "
                     "must do one of those four jobs",
             "correct": False,
             "why": "The scenario specifies the new evidence genuinely does "
                    "not fit an existing role — forcing it into one would "
                    "misrepresent what it shows."},
            {"text": "It would prove the whole case for human-caused "
                     "warming was wrong from the start",
             "correct": False,
             "why": "A framework needing revision is a different matter "
                    "from the underlying evidence itself being wrong."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h23",
        "band": "harder",
        "text": "A greenhouse gas molecule absorbs infrared and re-emits it "
                "'in all directions', including back towards the surface. "
                "Using that, explain why adding MORE greenhouse gas raises "
                "the surface temperature rather than simply absorbing the "
                "same total amount of heat more thoroughly.",
        "options": [
            {"text": "More gas absorbs more incoming sunlight, which "
                     "directly heats the atmosphere regardless of what "
                     "happens to outgoing infrared",
             "correct": False,
             "why": "Greenhouse gases are transparent to sunlight; adding "
                    "more of them does not change how much sunlight is "
                    "absorbed on the way in."},
            {"text": "More gas makes the atmosphere physically thicker, so "
                     "it presses down harder on the surface and warms it "
                     "through pressure, and the extra weight of gas is where "
                     "the 33 degrees actually comes from",
             "correct": False,
             "why": "The pressure change from adding greenhouse gas is "
                    "negligible; the mechanism is about radiation, not "
                    "pressure."},
            {"text": "More gas means more re-emission is directed back "
                     "towards the surface rather than escaping outward, so "
                     "energy leaves more slowly and the balance point "
                     "settles at a higher temperature",
             "correct": True},
            {"text": "More gas has no effect on temperature once the first "
                     "molecule has absorbed the available infrared",
             "correct": False,
             "why": "Additional gas continues to intercept and re-emit "
                    "infrared that earlier molecules missed, which is "
                    "exactly why adding more raises the temperature "
                    "further."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h24",
        "band": "harder",
        "text": "Suppose a fifth, entirely independent line of evidence "
                "were found that DISAGREED with the other four about the "
                "cause of the rise. What would be the scientifically "
                "appropriate response?",
        "options": [
            {"text": "Ignore the new evidence automatically, since four "
                     "independent pieces of evidence agreeing are "
                     "invariably assumed to outrank a fifth one that "
                     "disagrees",
             "correct": False,
             "why": "A disagreement is a genuine finding that needs "
                    "investigating, not something to dismiss purely by "
                    "counting how many pieces are on each side."},
            {"text": "Discard all four of the original pieces of evidence "
                     "immediately, since a newer and better-equipped study "
                     "always replaces any older ones that disagree with "
                     "it",
             "correct": False,
             "why": "Being newer does not make a finding automatically more "
                    "reliable. Both the new and the old evidence would need "
                    "checking."},
            {"text": "Average the disagreeing evidence with the agreeing "
                     "evidence to reach a middle conclusion",
             "correct": False,
             "why": "Averaging conflicting evidence is not how a genuine "
                    "disagreement gets resolved — investigating for an "
                    "error or a real effect is."},
            {"text": "Investigate the disagreement seriously — check the "
                     "new evidence and the existing four for errors — "
                     "rather than simply outvoting it or dismissing it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h25",
        "band": "harder",
        "text": "Sea level rise from thermal expansion continues for "
                "centuries after air temperature stabilises, but a policy "
                "is judged over a few decades. What does that mismatch in "
                "timescale imply for judging whether a climate policy has "
                "'worked'?",
        "options": [
            {"text": "Sea level may keep rising for a long time even after "
                     "a successful policy has stabilised air temperature, "
                     "so sea level alone is a poor short-term test of "
                     "whether the policy worked",
             "correct": True},
            {"text": "A policy is judged a success only if sea level stops "
                     "rising within the same decade it is introduced",
             "correct": False,
             "why": "The ocean's slow response means sea level can keep "
                    "rising for a long time regardless of how well a policy "
                    "has worked on air temperature."},
            {"text": "Sea level and air temperature are completely "
                     "unconnected, so neither can ever be used to judge the "
                     "other",
             "correct": False,
             "why": "They are connected — thermal expansion links ocean "
                    "warming to sea level. The issue is a mismatch in how "
                    "quickly each responds, not a lack of connection."},
            {"text": "Sea level responds almost instantly to any change "
                     "in air temperature, because the sea surface and the "
                     "air above it are always in step, so it is the best "
                     "short-term test of a policy available",
             "correct": False,
             "why": "The ocean's great depth makes its response slow, not "
                    "instant — the opposite of what would make it a good "
                    "short-term test."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h26",
        "band": "harder",
        "text": "The ozone layer was fixed by a treaty banning specific "
                "chemicals with one main use (aerosols and fridges). Carbon "
                "dioxide comes from thousands of different everyday "
                "activities across the whole economy. What does that "
                "difference suggest about comparing the two as problems to "
                "solve?",
        "options": [
            {"text": "Carbon dioxide should be exactly as easy to fix as "
                     "the ozone layer was, since both are gases in the "
                     "atmosphere and one treaty already solved the first "
                     "one",
             "correct": False,
             "why": "Being a gas in the atmosphere is where the similarity "
                    "ends — the number and variety of sources differs "
                    "enormously between the two."},
            {"text": "Carbon dioxide is likely to be harder to address "
                     "through a single measure, since it has far more and "
                     "far more varied sources than the ozone problem did",
             "correct": True},
            {"text": "The ozone layer must have been harder to fix, since "
                     "it involved chemistry rather than everyday activities",
             "correct": False,
             "why": "The ozone fix targeted a small number of chemicals "
                    "with a narrow set of uses, which is exactly why it "
                    "could be addressed by one treaty."},
            {"text": "Neither problem can be meaningfully compared, since "
                     "one is about the atmosphere and the other is not",
             "correct": False,
             "why": "Both are genuinely atmospheric problems; the useful "
                    "comparison is about the NUMBER AND VARIETY of sources "
                    "each one has."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h27",
        "band": "harder",
        "text": "The isotope fingerprint and the laboratory absorption "
                "measurement are both physical-chemistry findings, while "
                "the Hawaii record and the ice cores are both long-run "
                "measurements over time. Does grouping the four this way "
                "change which ones are needed?",
        "options": [
            {"text": "Yes — grouping them into pairs means just one "
                     "measurement per pair is necessary",
             "correct": False,
             "why": "Each of the four still establishes something the other "
                    "three do not, regardless of which two-by-two grouping "
                    "is drawn across them afterwards."},
            {"text": "Yes — the physical-chemistry pair becomes the more "
                     "important of the two, because work done under "
                     "controlled laboratory conditions outranks measurements "
                     "taken outdoors",
             "correct": False,
             "why": "Grouping them differently does not change what each "
                    "one actually establishes on its own; none becomes more "
                    "important than another by being regrouped."},
            {"text": "No — all four still supply a different one of the "
                     "four roles (trend, context, source, mechanism), "
                     "whatever pair-based grouping is drawn across them "
                     "afterwards",
             "correct": True},
            {"text": "It cannot be judged, since the four pieces of "
                     "evidence were not independent of one another in the "
                     "first place, no matter what grouping is drawn across "
                     "them afterwards",
             "correct": False,
             "why": "The four ARE described as independent lines of "
                    "evidence — that independence is exactly what a "
                    "regrouping does not remove."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h28",
        "band": "harder",
        "text": "A model predicts a certain amount of sea-level rise by a "
                "given year assuming CURRENT emissions continue unchanged. "
                "Emissions then fall sharply the following year. Does that "
                "make the original model 'wrong'?",
        "options": [
            {"text": "Yes — any prediction that does not come true exactly "
                     "as stated proves the science behind it was incorrect, "
                     "whatever it happened to assume at the time",
             "correct": False,
             "why": "A conditional prediction ('if emissions continue "
                    "unchanged') is not falsified by the condition itself "
                    "changing — that is a different scenario, not a failed "
                    "prediction."},
            {"text": "Yes — models that mention emissions can never be "
                     "trusted for anything",
             "correct": False,
             "why": "Naming the emissions assumption a model depends on is "
                    "exactly what makes it possible to judge fairly, rather "
                    "than a reason to distrust it."},
            {"text": "No — but because sea-level models cannot be tested "
                     "against what happens",
             "correct": False,
             "why": "Models can and are compared with what actually "
                    "happens; the reason a changed assumption does not make "
                    "one 'wrong' is about conditional predictions, not "
                    "about models being untestable."},
            {"text": "No — the model's prediction was conditional on an "
                     "assumption about future emissions, and that "
                     "assumption changing does not make the underlying "
                     "science wrong",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h29",
        "band": "harder",
        "text": "Explain why 'the cause is established, but the future "
                "amount is not' is a HARDER message to communicate clearly "
                "than either 'it's all settled' or 'nobody really knows'.",
        "options": [
            {"text": "Because it asks a listener to hold two different "
                     "levels of certainty about one topic at once, rather "
                     "than accepting one simple verdict either way",
             "correct": True},
            {"text": "Because it is factually incorrect, unlike the other "
                     "two simpler messages",
             "correct": False,
             "why": "It is the factually accurate message — the difficulty "
                    "described is about communicating it clearly, not about "
                    "whether it is true."},
            {"text": "Because scientists have not yet decided which of the "
                     "three messages to use",
             "correct": False,
             "why": "The accurate message is the nuanced one; the "
                    "difficulty is in explaining it well, not in choosing "
                    "between the three."},
            {"text": "Because it takes longer to say out loud than the "
                     "other two messages, and a message that cannot be said "
                     "in one short sentence is never understood by "
                     "anybody",
             "correct": False,
             "why": "Length of the sentence is not the reason it is harder "
                    "to communicate — holding two different levels of "
                    "certainty at once is."},
        ],
        "figure": None,
    },
    {
        "id": "c10-06-h30",
        "band": "harder",
        "text": "A pupil argues: 'If carbon dioxide is only 0.04% of the "
                "air, doubling it only moves that figure to 0.08%, so "
                "nothing important could have changed.' Using the "
                "greenhouse mechanism, what is wrong with treating the "
                "PERCENTAGE change as the relevant number?",
        "options": [
            {"text": "Nothing is wrong — a change from 0.04% to 0.08% is "
                     "far too small to have any effect on the temperature, "
                     "because a gas only begins to matter for the "
                     "greenhouse effect once it makes up at least one per "
                     "cent of the air",
             "correct": False,
             "why": "Doubling the concentration of a gas that absorbs "
                    "infrared has a real, measurable warming effect, "
                    "however small the change looks as a percentage of the "
                    "whole air."},
            {"text": "The relevant effect is how much MORE infrared the "
                     "extra molecules absorb and re-emit towards the "
                     "surface, which can be large even when the change in "
                     "the overall percentage of the air looks tiny",
             "correct": True},
            {"text": "The pupil's arithmetic is wrong — doubling 0.04% does "
                     "not give 0.08%",
             "correct": False,
             "why": "The arithmetic is correct; doubling 0.04 does give "
                    "0.08. The flaw is in treating that small-looking "
                    "percentage change as the number that decides the "
                    "effect."},
            {"text": "The pupil is right that nothing changed, since "
                     "nitrogen and oxygen still make up 99% of the air "
                     "either way",
             "correct": False,
             "why": "Nitrogen and oxygen's share staying the same is "
                    "irrelevant here — they absorb no infrared, so their "
                    "share was never what mattered for this effect."},
        ],
        "figure": None,
    },
]
