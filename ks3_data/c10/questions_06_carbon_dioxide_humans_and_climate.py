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
]
