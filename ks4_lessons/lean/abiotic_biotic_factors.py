# -*- coding: utf-8 -*-
"""Abiotic and biotic factors, in the lean shape. Spec table: ks4-abiotic-biotic-factors.md.

LEGACY (batch 10). The ladder and the practice set stay from the Design page. The practice set is
the page's own BANK (all routes), so its fixes are logic_edits. No practice-set stem is edited; rung prompts reworded in place keep their position, so their ids survive.
"""

LOGIC_EDITS = [
    # Rung 1 Q2: "matters most for aquatic animals" is arguable (temperature matters too). Same
    # rung position, same credited option.
    ("'Name the abiotic factor that matters most for aquatic animals.'",
     "'Name the abiotic factor in water that fish need for respiration.'"),
    ("['Carbon dioxide levels', 'That is the factor named for plants.']",
     "['Carbon dioxide levels', 'Respiration uses oxygen. Carbon dioxide levels are listed for plants.']"),
    # Practice set Q1 (polluted river), stem kept: the stored tail "bacteria cause the oxygen to
    # fall" is true of sewage pollution, so the option text no longer says it.
    ('["Disease — bacteria cause the oxygen to fall", false]',
     '["Disease", false]'),
    # Practice set Q2 (grey squirrels), stem kept: the two "Biotic" options turned on the words
    # intraspecific and interspecific, which this lesson does not need. Plain words instead.
    ('["Biotic — interspecific competition between two different species for food and habitat", true]',
     '["Biotic: competition between two different species", true]'),
    ('["Abiotic — grey squirrels changed the temperature of the habitat", false]',
     '["Abiotic: the grey squirrels changed the temperature", false]'),
    ('["Biotic — intraspecific competition between individuals of the same species", false]',
     '["Biotic: competition within one species", false]'),
    ('["Abiotic — grey squirrels are larger so they change the physical environment", false]',
     '["Abiotic: the grey squirrels changed the soil", false]'),
    ('"Grey squirrels don\'t change temperature — their effect is through direct competition for food and habitat, which is a biotic factor."',
     '"The grey squirrels did not change the temperature. They compete with red squirrels for food and nesting sites, which is a biotic factor."'),
    ('"INTRASPECIFIC competition = same species. Red vs grey = TWO DIFFERENT SPECIES = INTERSPECIFIC competition."',
     '"Red and grey squirrels are two different species, so this is competition between species."'),
    ('"Grey squirrels being larger is a physical trait — their impact on red squirrels is through competition for resources (a biotic factor)."',
     '"The grey squirrels did not change the soil. They outcompete the red squirrels for food and nesting sites."'),
    # Practice set Q4 (trees on a cliff), stem kept: "trees have no predators" is untrue.
    ("'That is biotic, and trees have no predators of that kind.'",
     "'A predator is biotic, and it would not make trees lean one way.'"),
    # Practice set Q3 (warm pond), stem kept, and Rung 2 Q1 (dry summer): the credited option was
    # visibly the longest. Distractors lengthened; replies kept.
    ("['The fish warmed the water', 'Fish do not heat a pond; the temperature is the abiotic change.']",
     "['The fish made heat that warmed the pond water', 'Fish do not heat a pond; the temperature is the abiotic change.']"),
    ("['The fish is the abiotic factor', 'Fish are living: biotic.']",
     "['The fish are the abiotic factor that changed', 'Fish are living: biotic.']"),
    ("['A new predator ate the plants', 'Nothing in the data says so; moisture is the measured change.']",
     "['A new predator arrived and ate most of the meadow plants', 'Nothing in the data says so; moisture is the measured change.']"),
    ("['The plant species are the abiotic factor', 'Plants are living: biotic.']",
     "['The plant species are the abiotic factor that fell', 'Plants are living: biotic.']"),
    # Examiner MUST FIX r2.0 (dry summer): the credited option was still visibly the longest.
    ("['Moisture levels fell, so plants needing more water could not survive', [",
     "['The soil was drier, so fewer plant species survived', ["),
    # Examiner MUST FIX practice Q3 (pond warms): the credited option was visibly the longest.
    ("'Warmer water held less oxygen, so fewer fish could survive', [",
     "'Warm water held less oxygen, so fish died', ["),
    # Examiner MUST FIX practice Q4 (trees lean away from the sea): the credited option was the
    # only one in AQA's full phrasing. Every option now uses AQA's phrasing; replies unchanged.
    ("[['Soil pH', 'pH would not make trees lean one way.'], ['A new predator', 'A predator is biotic, and it would not make trees lean one way.'], ['Oxygen levels', 'Oxygen levels matter for aquatic animals.']]",
     "[['Soil pH and mineral content', 'Soil pH and minerals would not make trees lean one way.'], ['New predators arriving', 'A predator is biotic, and it would not make trees lean one way.'], ['Oxygen levels for aquatic animals', 'Oxygen levels in water matter for aquatic animals. They would not make trees lean.']]"),
    # Examiner SHOULD FIX practice Q1 (polluted river): explanations shouted "BIOTIC" and used
    # "=" shorthand. Options unchanged.
    ('"Fish population = a BIOTIC factor — it is a living component. The O₂ level is the abiotic factor that changed."',
     '"Fish are living, so the fish population is a biotic factor. The oxygen level is the abiotic factor that changed."'),
    ('"Disease is a BIOTIC factor — caused by living pathogens. O₂ concentration is abiotic (a chemical feature of the water)."',
     '"Disease is caused by living pathogens, so it is a biotic factor. The oxygen level is abiotic."'),
    ('"Competition is a BIOTIC factor between living organisms. The O₂ level itself is the abiotic factor."',
     '"Competition is between living organisms, so it is a biotic factor. The oxygen level is the abiotic factor."'),
]

LESSON = {
    "slug": "abiotic-biotic-factors",
    "start": {
        "setup": "Grasses and poppies fill an open field. Under the thick trees beside it, only "
                 "ivy and moss grow.",
        "question": "If you had to guess, is it the light or the animals that makes the "
                    "difference?",
        "options": [
            ("The animals",
             "The light. Little light gets through the thick leaves, so only plants that cope "
             "with shade grow there."),
            ("The light",
             "The light. Little light gets through the thick leaves, so only plants that cope "
             "with shade grow there."),
        ],
        "answer": 1,
    },
    "words": ["abiotic factor", "biotic factor", "community", "pathogen"],
    "knowledge": [
        {"kind": "card", "title": "Abiotic factors",
         "body": ["Abiotic factors are the non-living parts of the environment.",
                  "These abiotic factors can affect a community:",
                  {"points": [
                      "light intensity",
                      "temperature",
                      "moisture levels",
                      "soil pH and mineral content",
                      "wind intensity and direction",
                      "carbon dioxide levels for plants",
                      "oxygen levels for aquatic animals",
                  ]}]},
        {"kind": "reveal", "title": "How each abiotic factor affects organisms",
         "cols": ["Why it matters"],
         "rows": [
             ("Light intensity", "Plants need light for photosynthesis. Deep shade supports only "
              "plants that cope with shade."),
             ("Temperature", "Each species survives only within a range of temperatures."),
             ("Moisture levels", "All organisms need water. Few plants grow in very dry soil."),
             ("Soil pH and mineral content", "Some plants, such as heather, grow on acidic soil. "
              "Soil with few mineral ions supports fewer plant species."),
             ("Wind intensity and direction", "Strong wind dries plants out. Trees on an exposed "
              "cliff grow bent away from the wind."),
             ("Carbon dioxide levels for plants", "Plants use carbon dioxide in photosynthesis, "
              "so its level affects how well they grow."),
             ("Oxygen levels for aquatic animals", "Fish and other water animals need dissolved "
              "oxygen for respiration. Warm water holds less oxygen."),
         ]},
        {"kind": "card", "title": "Biotic factors",
         "body": ["Biotic factors are the living parts of the environment.",
                  "These biotic factors can affect a community:",
                  {"points": [
                      "availability of food",
                      "new predators arriving",
                      "new pathogens",
                      "one species outcompeting another so the numbers are no longer sufficient "
                      "to breed",
                  ]}]},
        {"kind": "reveal", "title": "How each biotic factor affects a community",
         "cols": ["What happens"],
         "rows": [
             ("Availability of food", "If food becomes scarce, fewer of the animals that eat it "
              "survive and breed."),
             ("New predators arriving", "The new predator eats prey, so the prey population "
              "falls."),
             ("New pathogens", "A pathogen is a microorganism that causes disease. A new disease "
              "can kill many of a population quickly."),
             ("One species outcompeting another", "Grey squirrels outcompete red squirrels for "
              "food and nesting sites. In many areas too few red squirrels are left to breed."),
         ]},
        {"kind": "card", "title": "Explain a change from data",
         "body": ["Name the factor. Say which way it changed, using the numbers. Then say what "
                  "happened to the organisms and why.",
                  "Information (made up): light was measured at four points from a hedge into a "
                  "field.",
                  {"points": [
                      "0 m: 200 lux, 2 plant species",
                      "2 m: 900 lux, 5 plant species",
                      "4 m: 2500 lux, 9 plant species",
                      "6 m: 4000 lux, 11 plant species",
                  ]},
                  "A full answer: as light intensity rose from 200 to 4000 lux, the number of "
                  "plant species rose from 2 to 11. More light means more photosynthesis, so "
                  "more kinds of plant can grow."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The fish that died are the abiotic factor.",
              "The fish are living, so they are biotic. The oxygen level that fell is the abiotic "
              "factor."),
             ("A new disease is abiotic because germs are tiny.",
              "A pathogen is living, so a new pathogen is a biotic factor."),
             ("Carbon dioxide levels are the factor for aquatic animals.",
              "Carbon dioxide levels are listed for plants. Oxygen levels are listed for aquatic "
              "animals."),
         ]}]},
    ],
    "key_fact": "Abiotic factors are non-living: light intensity, temperature, moisture levels, "
                "soil pH and mineral content, wind intensity and direction, carbon dioxide levels "
                "for plants and oxygen levels for aquatic animals. Biotic factors are living: "
                "availability of food, new predators arriving, new pathogens, and one species "
                "outcompeting another so the numbers are no longer sufficient to breed.",
    "deeper": [
        {"kind": "card", "title": "Measuring abiotic factors",
         "body": [{"points": [
             "Light intensity: a light meter.",
             "Temperature: a thermometer.",
             "Soil pH: a pH probe, or universal indicator with a soil sample.",
         ]},
                  "Measuring a factor at points along a line is taught in Sampling techniques."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Identify</strong>: say whether a factor is abiotic or biotic.",
             "<strong>Explain</strong>: say how a change in a factor affects a community, using "
             "the data.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-10", "logic_edits": LOGIC_EDITS},
}
