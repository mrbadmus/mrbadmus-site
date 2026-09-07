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
]
