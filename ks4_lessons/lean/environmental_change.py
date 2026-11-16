# -*- coding: utf-8 -*-
"""The impact of environmental change, in the lean shape. LEGACY: the live batch-10 Design page.
Spec table: ks4-environmental-change.md (AQA 8461 4.7.2.4, biology only, HT only; the page
exists on TH only).

The ladder (rungs) and the practice set (BANK, written in the logic, five items) stay from the
legacy page, so their ids survive. The practice set does NOT read the subtopic `quiz` list, so its
fixes are logic_edits. Every edit keeps the item in its place, and every practice-set edit keeps
its question text, so every id survives."""

LESSON = {
    "slug": "environmental-change",
    "start": {
        "setup": None,
        "question": "If you had to guess, as the UK has warmed, have many species been found "
                    "further north or further south than before?",
        "options": [
            ("Further north",
             "Further north. Places further north have become warm enough for them, so their "
             "distribution has moved."),
            ("Further south",
             "Further north. Places further north have become warm enough for them, so their "
             "distribution has moved."),
        ],
        "answer": 0,
    },
    "words": ["distribution", "environmental change", "seasonal", "geographic"],
    "knowledge": [
        {"kind": "card", "title": "Three environmental changes",
         "body": ["Environmental changes affect the distribution of species in an ecosystem. "
                  "Distribution means where a species is found.",
                  "These changes include:",
                  {"points": ["temperature",
                              "availability of water",
                              "composition of atmospheric gases."]}]},
        {"kind": "reveal", "title": "Three kinds of cause",
         "cols": ["What it means", "Example"],
         "rows": [("Seasonal", "The change happens at the same time every year.",
                   "A pond shrinks every summer."),
                  ("Geographic", "Conditions are different from place to place.",
                   "It is colder higher up a mountain."),
                  ("Human interaction", "People cause the change.",
                   "A town takes water from a river, so the flow falls.")]},
        {"kind": "card", "title": "How a species can respond",
         "body": [{"points": [
             "It spreads into places that have become suitable.",
             "It disappears from places that are no longer suitable.",
             "It changes the timing of events, such as when it breeds.",
             "Its numbers fall.",
         ]},
             "Spreading into new places is moving, not evolving."]},
        {"kind": "card", "title": "An example of each change",
         "body": [{"points": [
             "<strong>Temperature</strong>: as the climate warms, some species are now found "
             "further north, or higher up mountains, than before.",
             "<strong>Availability of water</strong>: when less water flows in a river, fish "
             "that need fast, shallow water to breed can decline.",
             "<strong>Atmospheric gases</strong>: some lichens cannot grow where there is a lot "
             "of sulfur dioxide in the air. They return when the sulfur dioxide falls.",
         ]}]},
        {"kind": "card", "title": "Evaluating given information",
         "body": ["The exam gives you the information. Use the facts it gives, such as what a "
                  "species needs.",
                  {"points": [
                      "1. Describe the change in the data, using the numbers.",
                      "2. Link it to the environmental change.",
                      "3. Say what else could explain it.",
                      "4. Say what further data would make the conclusion stronger.",
                      "5. Give a judgement.",
                  ]},
                  "Two things changing at the same time suggests a link. It does not prove that "
                  "one caused the other."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The data prove that warming caused the change.",
              "The data can show a link. Other factors could also explain it."),
             ("Geographic means a change through the year.",
              "Geographic means a difference from place to place. Seasonal is through the year."),
             ("A species that has spread north has evolved.",
              "It has moved into places that became suitable."),
         ]}]},
    ],
    "key_fact": "Changes in temperature, availability of water and the composition of "
                "atmospheric gases affect the distribution of species in an ecosystem. The "
                "changes may be seasonal, geographic or caused by human interaction.",
    "deeper": [
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Evaluate</strong>: use the information to give points for and against, "
             "then a judgement.",
             "<strong>Describe</strong>: say how the distribution changed, using the data.",
             "<strong>Suggest</strong>: give another factor that could explain the change.",
         ]}]},
        {"kind": "card", "title": "Links",
         "body": ["Global warming is one human cause of a change in temperature. Abiotic and "
                  "biotic factors covers what else affects a community."]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-10",
        "logic_edits": [
            # Rung 1 Q1: "Light, soil pH, wind" are abiotic factors that can also change a
            # distribution, so that distractor was arguable; the credited option was the longest.
            # Blind doubt r1-1 (HIGH): "Seasonal changes, geographic changes and human
            # interaction" uses the spec's own words, so a pupil can defend it; replaced with a
            # definitely wrong set. Examiner MUST FIX: credited option shortened so it is not the
            # longest (the why line keeps the full spec wording).
            ("['Temperature, availability of water, composition of atmospheric gases', "
             "['Food, mates, territory', 'Those are things animals compete for.'], "
             "['Light, soil pH, wind', 'Abiotic factors, but not the three named changes.']]",
             "['Temperature, availability of water and atmospheric gases', "
             "['Photosynthesis, respiration and decay by microorganisms', 'Those are processes "
             "in the carbon cycle, not changes in the environment.'], ['Producers, primary "
             "consumers and secondary consumers', 'Those are trophic levels.']]"),
            # Rung 1 Q2: "Natural, artificial, random" is arguable (human interaction is
            # artificial). Swap for the changes, which pupils mix up with the causes.
            ("['Seasonal, geographic, human interaction', ['Structural, behavioural, "
             "functional', 'Those are types of adaptation.'], ['Natural, artificial, random', "
             "'Not the spec’s terms.']]",
             "['Seasonal, geographic, human interaction', ['Structural, behavioural, "
             "functional', 'Those are types of adaptation.'], ['Temperature, water, atmospheric "
             "gases', 'Those are the changes, not the causes.']]"),
            # Rung 2 Q1: the credited option was visibly the longest.
            ("['Its range extended northwards and the number of squares rose from 11 to 21', "
             "['It moved south', 'The new squares are to the north.'], ['It became rarer', "
             "'It was recorded in more squares.']]",
             "['Its range extended northwards and the number of squares rose from 11 to 21', "
             "['Its range moved southwards and the number of squares fell from 21 to 11', "
             "'The new squares are to the north, and there are more of them.'], ['Its range "
             "stayed the same and the number of squares fell', 'It was recorded in more "
             "squares, further north.']]"),
            # Rung 2 Q2: the credited option was the longest; even up the lengths.
            ("['Less sulfur dioxide in the air', ['Warmer winters', 'The information points at "
             "the factory gas.'], ['More rain', 'Nothing in the information is about water.']]",
             "['Less sulfur dioxide in the air', ['Warmer winters in the city', 'The "
             "information points at the factory gas.'], ['More rain falling on the trees', "
             "'Nothing in the information is about water.']]"),
            # Rung 3 Q1: "using the given chain" pointed at an information box the lean page no
            # longer has. The links carry the chain.
            # Examiner MUST FIX: the chain tested eutrophication, which the lean page does not
            # teach and which is not in 4.7.2.4 (blind doubt r3-1 too). Same position (id kept);
            # now a temperature change and a distribution change, with one forced order.
            ("'Fertiliser washes into a lake and fish die. Explain, using the given chain. Put "
             "the links in order.'",
             "'As the climate warms, a butterfly is now found further north than before. "
             "Explain why. Put the links in order.'"),
            # Practice Q1 (question text kept, id kept): the credited option was the longest by
            # far with a dash tail, and the "evolved" distractor is arguable.
            ('''[["Climate change — rising spring temperatures trigger earlier breeding, as birds respond to warmer conditions", true], ["Selective breeding by conservationists to match earlier insect emergence", false], ["Reduced daylight in summer due to increased cloud cover", false], ["Birds have evolved to breed earlier because earlier chicks survive better", false]], { "1": "Conservationists don't selectively breed wild bird populations — the change is a response to environmental conditions.", "2": "Daylight hours have not significantly changed — it is TEMPERATURE that is changing with climate change. Day length is a key breeding trigger, but the earlier TIMING of temperature warming is causing earlier breeding.", "3": "While natural selection could eventually select for earlier breeding, the change has occurred too rapidly (within 50 years) to be explained by evolutionary change — it is a direct behavioural response to environmental change." }''',
             '''[["Rising spring temperatures", true], ["Selective breeding by conservationists", false], ["Shorter days in spring", false], ["Colder winters", false]], { "1": "People do not breed wild birds to change when they nest. The birds are responding to warmer springs.", "2": "Day length in spring has not changed. Spring temperatures have risen.", "3": "UK winters and springs have become warmer, not colder." }'''),
            # Practice Q2 (question text kept): the credited option was the longest by far.
            ("'The oxygen level below the pipe is probably too low for them; the data do not "
             "show what caused the low oxygen', [['The farm is definitely poisoning the river', "
             "'The information links the larvae to oxygen, not to a poison; the cause of low "
             "oxygen is not given.'], ['Mayflies have evolved to avoid farms', 'They need "
             "oxygen; where there is less, they cannot survive.'], ['Nothing can be concluded', "
             "'The given fact lets you conclude that oxygen is probably low below the pipe.']]",
             "'Low oxygen below the pipe could explain it, but is not proven', [['The farm is "
             "definitely poisoning the river with toxic chemicals', 'The data do not show the "
             "cause, so you cannot say definitely.'], ['Mayflies have evolved to "
             "avoid water near farms', 'Something below the pipe stops them surviving. That is "
             "not evolution.'], ['Nothing at all can be concluded from this information', "
             "'Something below the pipe stops them surviving, and low oxygen is one possible "
             "reason.']]"),
            # Practice Q3 (question text kept): the credited option was the longest by far.
            ("'The plant’s range moved about 200 m uphill as temperatures rose', [['The plant "
             "has disappeared', 'It is still found over a 500 m band, just higher.'], ['The "
             "plant spread downhill', 'Both limits moved up, from 1500 to 1700 m and 2000 to "
             "2200 m.'], ['The temperature had no effect', 'The shift matches warming, though "
             "the data alone cannot prove the cause.']]",
             "'Its range moved about 200 m uphill', [['It has disappeared from "
             "the whole mountain', 'It is still found over a 500 m band, just higher.'], ['Its "
             "range moved about 200 m downhill', 'Both limits moved up, from 1500 to 1700 m and "
             "2000 to 2200 m.'], ['Its range stayed the same as it got warmer', 'Both limits "
             "moved up by 200 m.']]"),
            # Practice Q4 (question text kept): the credited option was the longest by far.
            ("'Fewer caterpillars when the chicks hatch, so fewer chicks survive: a timing "
             "mismatch', [['More chicks survive because the leaves come earlier', 'The chicks "
             "miss the caterpillar peak.'], ['The birds evolve within a year', 'Evolution takes "
             "many generations.'], ['No effect: the birds eat leaves', 'The information says "
             "they feed chicks on caterpillars.']]",
             "'Fewer chicks survive, as the caterpillars peak too early', [['More chicks "
             "survive, because the leaves come out earlier', 'The chicks hatch after the "
             "caterpillar peak, so there is less food.'], ['The birds evolve to nest earlier "
             "within a year', 'Evolution takes many generations.'], ['No effect, because the "
             "birds feed on the leaves', 'The information says they feed their chicks on "
             "caterpillars.']]"),
            # Practice Q5 (question text kept): the credited option was the longest by far.
            ("'Sulfur dioxide from burning fuels making the air more polluted', [['A river "
             "drying up in summer', 'That is water availability, seasonal.'], ['Hotter "
             "summers', 'That is temperature.']",
             "'More sulfur dioxide in the air', [['A river drying up in summer', 'That is "
             "water availability, seasonal.'], ['Hotter summers each year', 'That is "
             "temperature.']"),
            # Examiner MUST FIX r3.0, continued: the links and herrings of the new butterfly chain.
            ("['Algae multiply and cover the surface, blocking light to the water plants below.', 'The water plants die and bacteria decompose them, using oxygen in respiration.', 'The oxygen level falls, so the fish die.']",
             "['The climate warms, so temperatures rise.', 'Places further north become warm enough for the butterfly to live in.', 'The butterfly spreads into these places, so its distribution extends north.']"),
            ("[['The algae use up all the oxygen directly.', 'Bacteria decomposing dead plants use the oxygen.'], ['The fertiliser is poisonous to fish.', 'The chain runs through algae, light, decomposition and oxygen.']]",
             "[['The butterfly evolves to live in the cold.', 'It moves into places that have become suitable. It does not evolve.'], ['Places further south become colder.', 'Warming makes places warmer, not colder.']]"),
            # Blind doubt r3-2 (MED): data-then-interpretation and claim-then-evidence were both defensible
            # orders. Each link now refers back to the one before ("This suggests", "those other
            # factors"), so only one order is right. Position kept (id kept).
            ("['The data show the range moved north over the same years that spring temperatures rose.', 'Warming may have made northern areas suitable, but other factors, such as habitat change or more recording, could contribute.', 'To be more certain, check that recording effort was equal and look at data on other factors.']",
             "['The data show the range moved north over the same years that spring temperatures rose.', 'This suggests warming made northern areas suitable, but other factors, such as habitat change or more recording, could also explain it.', 'To test those other factors, check that recording effort was equal and look at data on habitat change.']"),
        ],
    },
}
