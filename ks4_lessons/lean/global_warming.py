# -*- coding: utf-8 -*-
"""Global warming, in the lean shape. New record, no legacy page.
Spec table: ks4-global-warming.md (AQA 8464 4.7.3.5 / 8461 4.7.3.5, the same words in both)."""

LESSON = {
    "slug": "global-warming",
    "start": {
        "setup": "The place where a species of butterfly lives gets warmer, year after year.",
        "question": "If you had to guess, what could happen to where the butterfly is found?",
        "options": [
            ("It could change",
             "It could change. As temperatures change, some species can live in new places and "
             "others can no longer live where they used to."),
            ("It stays the same",
             "It could change. As temperatures change, some species can live in new places and "
             "others can no longer live where they used to."),
        ],
        "answer": 0,
    },
    "words": ["global warming", "methane", "distribution", "migration"],
    "knowledge": [
        {"kind": "card", "title": "What is changing",
         "body": ["Levels of carbon dioxide and methane in the atmosphere are increasing.",
                  "They contribute to global warming: a rise in the average temperature of the Earth."]},
        {"kind": "reveal", "title": "Biological consequences of global warming",
         "cols": ["What happens to living things"],
         "rows": [
             ("Sea levels rise",
              "Low-lying land is flooded, so habitats are lost."),
             ("Temperature and rainfall change",
              "The distribution of species changes. Some species can live in new areas. Others can "
              "no longer live where they used to."),
             ("The timing of the seasons changes",
              "The migration patterns of animals, such as birds, change."),
             ("Species cannot move or adapt fast enough",
              "They may become extinct, so biodiversity is reduced."),
         ]},
        {"kind": "card", "title": "Distribution means where",
         "body": ["The distribution of a species is where it is found.",
                  "How many there are is the population size. That is a different thing."]},
        {"kind": "card", "title": "The evidence",
         "body": ["The scientific consensus about global warming and climate change is based on "
                  "systematic reviews of thousands of peer-reviewed publications.",
                  "Some evidence is uncertain or incomplete. The climate is complex, many factors act "
                  "at once, and predictions of the future come from models."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Distribution means how many of a species there are.",
              "Distribution means where a species is found."),
             ("Global warming only changes the weather.",
              "It changes where species live, when they migrate, and biodiversity."),
             ("Some uncertainty means scientists do not agree.",
              "The consensus is based on reviews of thousands of peer-reviewed publications."),
         ]}]},
    ],
    "key_fact": "Levels of carbon dioxide and methane in the atmosphere are increasing, and contribute "
                "to global warming. Biological consequences include habitats lost as sea levels rise, "
                "changes in the distribution and migration patterns of species, and reduced "
                "biodiversity.",
    "deeper": [
        {"kind": "card", "title": "Where the extra gases come from",
         "body": [{"points": [
             "<strong>Carbon dioxide</strong>: burning fossil fuels, deforestation, and the decay or "
             "burning of peat.",
             "<strong>Methane</strong>: cattle, rice fields, and rubbish rotting in landfill sites.",
         ]}]},
        {"kind": "card", "title": "How the gases warm the Earth",
         "body": ["You learn this in chemistry.",
                  "Short wavelength radiation from the Sun passes through the atmosphere and warms "
                  "the Earth's surface.",
                  "The Earth gives off long wavelength radiation. Carbon dioxide and methane absorb "
                  "some of it, so the atmosphere warms up.",
                  {"slot": "fig:greenhouse-effect"}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: say what happens, for example one change to living things.",
             "<strong>Explain</strong>: say what happens and why.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the two gases whose increasing levels in the atmosphere contribute to "
                       "global warming.",
             "why": "Levels of carbon dioxide and methane in the atmosphere are increasing.",
             "options": [
                 {"text": "Oxygen and nitrogen gases", "correct": False,
                  "reply": "These are the main gases in air, but they do not contribute to global warming."},
                 {"text": "Carbon dioxide and methane", "correct": True},
                 {"text": "Nitrogen and argon gases", "correct": False,
                  "reply": "The two gases are carbon dioxide and methane."},
             ]},
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State what is meant by the distribution of a species.",
             "why": "Distribution is where a species is found.",
             "options": [
                 {"text": "How many of the species there are", "correct": False,
                  "reply": "That is population size."},
                 {"text": "What the species eats", "correct": False,
                  "reply": "That is its diet. Distribution is where it is found."},
                 {"text": "Where the species is found", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "Describe one biological consequence of rising sea levels.",
             "why": "Low-lying land floods, so the species that live there lose their habitat.",
             "options": [
                 {"text": "Low-lying habitats are flooded and lost", "correct": True},
                 {"text": "Every coastal species gains more space", "correct": False,
                  "reply": "Rising sea levels flood land, so coastal species lose habitat."},
                 {"text": "Sea water turns into fresh water", "correct": False,
                  "reply": "The sea stays salty. Low-lying land is flooded."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why the scientific consensus about global warming can be trusted.",
             "why": "It is based on systematic reviews of thousands of peer-reviewed publications.",
             "options": [
                 {"text": "It is based on the weather in one country for a few years", "correct": False,
                  "reply": "That is far too little evidence."},
                 {"text": "It comes from reviews of thousands of peer-reviewed publications",
                  "correct": True},
                 {"text": "It is based on what most members of the public believe", "correct": False,
                  "reply": "A scientific consensus comes from reviewing scientific evidence."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how rising levels of carbon dioxide and methane can reduce "
                       "biodiversity. Put the links in order.",
             "links": ["Rising levels of carbon dioxide and methane contribute to global warming.",
                       "The temperature changes, so some places are no longer suitable for the "
                       "species that live there.",
                       "Species that cannot move or adapt may become extinct, so biodiversity is "
                       "reduced."],
             "herrings": [{"text": "Methane levels in the atmosphere are falling.",
                           "why": "Levels of carbon dioxide and methane are increasing."},
                          {"text": "Warmer temperatures always increase the number of species.",
                           "why": "Some species can no longer live where they used to."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how global warming can reduce the number of species living on a "
                       "low-lying coast. Put the links in order.",
             "links": ["Global warming makes sea levels rise.",
                       "Low-lying coastal land is flooded.",
                       "Species living there lose their habitat, so fewer species can live there."],
             "herrings": [{"text": "Sea levels fall, so the coast dries out.",
                           "why": "Global warming makes sea levels rise."},
                          {"text": "Flooding gives land animals more space.",
                           "why": "Flooding destroys the habitat of land species."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "Describe some of the biological consequences of global warming.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "Describes two or more consequences for living "
                  "things, each with what happens to the species.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "Names one consequence.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Sea levels rise, so low-lying habitats are flooded and lost.",
                        "The distribution of species changes: some can live in new areas, others can "
                        "no longer live where they used to.",
                        "The migration patterns of animals, such as birds, change.",
                        "Species that cannot move or adapt may become extinct.",
                        "So biodiversity is reduced."],
             "reject": ["“Global warming makes the hole in the ozone layer bigger.”",
                        "“Distribution means the number of a species.”"]},
        ],
    },
}
