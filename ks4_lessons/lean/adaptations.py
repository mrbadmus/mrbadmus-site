# -*- coding: utf-8 -*-
"""Adaptations, in the lean shape. Spec table: ks4-adaptations.md.

LEGACY (batch 10). The ladder and the practice set stay from the Design page. The practice set is
the page's own BANK (all routes), so its fixes are logic_edits. No practice-set stem is edited; rung prompts reworded in place keep their position, so their ids survive.
"""

LOGIC_EDITS = [
    # Rung 1 Q2: the credited option was visibly the longest, and one reply said "in the spec's
    # sense". Distractors lengthened, reply plain.
    ("['A polar bear', 'The Arctic is cold, but a bear is not an extremophile in the spec’s sense.']",
     "['A polar bear living on Arctic ice', 'A polar bear is adapted to the cold, but it is not an extremophile.']"),
    ("['A rabbit', 'Rabbits live in ordinary conditions.']",
     "['A rabbit living in a grassy field', 'Rabbits live in ordinary conditions.']"),
    # Rung 2 Q2: the credited option was visibly the longest.
    ("['It has a large surface area compared with its volume', 'That would lose more heat.']",
     "['It has a large surface area compared with its volume, so more heat is kept', 'A large surface area compared with volume loses more heat.']"),
    ("['Small ears hear better in the cold', 'Ear size here is about heat loss, not hearing.']",
     "['Small ears hold more blood, so they store more heat', 'Ear size here is about heat loss through the surface.']"),
    # Practice set Q2 (fennec fox ears), stem kept: "hear predators from further away" was
    # arguable (its own feedback said hearing is enhanced too).
    ('"Large ears help the animal hear predators from further away in the flat desert"',
     '"Large ears reduce the surface area for heat loss"'),
    ('"Hearing is enhanced too — but the PRIMARY ecological reason for the fennec fox\'s extraordinarily large ears relative to body size is thermoregulation (heat loss). Other desert animals with large ears (jackrabbits) also use them for cooling."',
     '"Large ears give a large surface area, so more heat is lost, not less."'),
    # Practice set Q4 (Antarctic fish), stem kept: the credited option was visibly the longest.
    ("['It swims faster; a behavioural adaptation', 'The information is about its blood, not its swimming.']",
     "['It swims faster to keep warm; a behavioural adaptation', 'The information is about its blood, not its swimming.']"),
    ("['It is camouflaged; a structural adaptation', 'The proteins are inside the body and stop freezing.']",
     "['It is hidden against the ice; a structural adaptation', 'The proteins are inside the body and stop freezing.']"),
    ("['It stays warm; a structural adaptation', 'The proteins stop ice forming; they are a process in the blood: functional.']",
     "['Its blood stays warmer than the water; a structural adaptation', 'The proteins stop ice forming; they are a process in the blood: functional.']"),
    # Examiner MUST FIX r2.0 (jerboa): the credited option was visibly the longest.
    ("['Making very concentrated urine', [",
     "['Concentrated urine', ["),
    # Examiner SHOULD FIX r3.1 (cactus): roots, stem and spines were three separate adaptations,
    # so the order was forced only by wording. Same position (id kept); now one causal chain with
    # one forced order. The writer's "spines take up water from the air" herring is replaced:
    # some cactus spines do collect fog droplets, so it was not definitely wrong.
    ("'Information: a cactus has a thick waxy stem, spines instead of leaves and wide shallow roots. Explain how it is adapted to the desert. Put the links in order.',\n            ['Wide shallow roots take up rain quickly before it drains away.', 'The thick waxy stem stores that water and stops it escaping.', 'Spines instead of leaves give a small surface, so little of the stored water is lost.'],\n            [['The spines make their own food.', 'The green stem photosynthesises; the spines reduce water loss.'], ['The roots store water for the leaves.', 'A cactus has no leaves; the stem stores the water.']]",
     "'Information: a cactus has spines instead of leaves. Explain how this helps it survive in the desert. Put the links in order.',\n            ['Spines have a much smaller surface area than leaves.', 'So less water is lost from the plant.', 'So the cactus keeps enough water to survive the long dry periods.'],\n            [['The spines make their own food.', 'The green stem photosynthesises; the spines reduce water loss.'], ['The spines store water for the dry season.', 'The thick stem stores the water; the spines reduce water loss.']]"),
    # Examiner NOTE practice Q1 (polar bear): explanations shouted ("DOES", "STRUCTURAL", "OF")
    # and used dash asides. Options unchanged.
    ('"Behavioural adaptations are things the organism DOES — e.g. hibernating or huddling. Fur and blubber are physical STRUCTURAL features."',
     '"Behavioural adaptations are things the organism does, such as huddling. Fur and blubber are body parts, so they are structural."'),
    ('"Functional (physiological) adaptations are internal chemical processes — e.g. antifreeze proteins, concentrated urine production. Fur and blubber are physical structures."',
     '"Functional adaptations are processes inside the body, such as making concentrated urine. Fur and blubber are body parts."'),
    ('"The environment selects for adaptations through natural selection — but adaptations are features OF the organism, not caused directly by the environment."',
     '"Adaptations are features of the organism. Fur and blubber are body parts, so they are structural."'),
    # Examiner NOTE practice Q4 (Antarctic fish): credited option 8 characters longer than the
    # longest distractor; trimmed.
    ("'Its blood does not freeze in water below 0 °C; a functional adaptation'",
     "'Its blood does not freeze below 0 °C; a functional adaptation'"),
]

LESSON = {
    "slug": "adaptations",
    "start": {
        "setup": "A polar bear is moved to a hot desert.",
        "question": "If you had to guess, would it be comfortable, or would it overheat?",
        "options": [
            ("It would be comfortable",
             "It would overheat. Its thick fur and layer of fat keep heat in. They suit the "
             "Arctic, not a desert."),
            ("It would overheat",
             "It would overheat. Its thick fur and layer of fat keep heat in. They suit the "
             "Arctic, not a desert."),
        ],
        "answer": 1,
    },
    "words": ["adaptation", "behavioural", "functional", "extremophile"],
    "knowledge": [
        {"kind": "card", "title": "What an adaptation is",
         "body": ["Organisms have features (adaptations) that enable them to survive in the "
                  "conditions in which they normally live.",
                  "These adaptations may be structural, behavioural or functional."]},
        {"kind": "reveal", "title": "Three types of adaptation",
         "cols": ["What it is", "Examples"],
         "rows": [
             ("Structural", "A body part or body shape",
              "Thick fur, a layer of blubber, cactus spines"),
             ("Behavioural", "Something the organism does",
              "Hunting at night, migrating, living in a herd"),
             ("Functional", "A process inside the body",
              "Antifreeze proteins in the blood, very concentrated urine"),
         ]},
        {"kind": "card", "title": "Keeping warm and keeping cool",
         "body": ["Heat is lost through the surface of the body.",
                  {"points": [
                      "A large animal with small ears and short legs has a small surface area "
                      "compared with its volume. It loses less heat, so it suits a cold place.",
                      "An animal with very large ears has a large surface area compared with its "
                      "volume. It loses more heat, so it suits a hot place.",
                  ]},
                  "The Arctic fox has small ears. The fennec fox, which lives in the desert, has "
                  "very large ears."]},
        {"kind": "card", "title": "Plants in the desert",
         "body": ["A cactus is adapted to keep the little water it gets.",
                  {"points": [
                      "Spines instead of leaves give a small surface, so less water is lost.",
                      "A thick, waxy stem stores water and stops it escaping.",
                      "Wide, shallow roots take up rain quickly before it drains away.",
                  ]}]},
        {"kind": "card", "title": "Extremophiles",
         "body": ["Some organisms live in environments that are very extreme, such as at high "
                  "temperature, pressure, or salt concentration. These organisms are called "
                  "extremophiles.",
                  "Bacteria living in deep sea vents are extremophiles."]},
        {"kind": "card", "title": "Explain an adaptation from information",
         "body": ["For each feature, name the type, say what it does, and say how that helps the "
                  "organism survive where it lives.",
                  "Information: the sand cat lives in deserts. Fur covers the soles of its feet. "
                  "It hunts at night and shelters in a burrow by day. Its kidneys make very "
                  "concentrated urine.",
                  {"points": [
                      "Fur on its feet (structural) protects them from the hot sand.",
                      "Hunting at night and sheltering by day (behavioural) avoids the daytime "
                      "heat.",
                      "Very concentrated urine (functional) means less water is lost.",
                  ]}]},
        {"kind": "card", "title": "Where adaptations come from",
         "body": ["Individuals in a population vary.",
                  "Those with a feature that suits the environment are more likely to survive and "
                  "breed, and pass the feature on to their offspring.",
                  "Over many generations the feature becomes common. This is natural selection."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The fennec fox grew big ears because it was hot.",
              "Foxes with bigger ears survived and bred more, so over many generations big ears "
              "became common."),
             ("Hunting at night is a structural adaptation.",
              "It is something the animal does, so it is behavioural."),
             ("A camel's hump stores water.",
              "The hump stores fat."),
         ]}]},
    ],
    "key_fact": "Adaptations are features that enable organisms to survive in the conditions in "
                "which they normally live, and they may be structural, behavioural or functional. "
                "Extremophiles live in very extreme environments, such as bacteria living in deep "
                "sea vents.",
    "deeper": [
        {"kind": "card", "title": "More extremophiles",
         "body": ["Other extremophiles live in hot springs or in very salty lakes."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong>: say how each feature helps the organism survive where it "
             "lives.",
             "<strong>Suggest</strong>: use the information to say how an organism you have not "
             "met before is adapted.",
             "<strong>Classify</strong>: say whether an adaptation is structural, behavioural or "
             "functional.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-10", "logic_edits": LOGIC_EDITS},
}
