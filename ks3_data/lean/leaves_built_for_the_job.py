# -*- coding: utf-8 -*-
"""Leaves built for the job, in the lean shape. Spec table: docs/lessons/wave1/ks3-leaves-built-for-the-job.md."""

LESSON = {
    "slug": "leaves-built-for-the-job",
    "start": {
        "setup": "A leaf has tiny holes that let gases in and out.",
        "question": "If you had to guess, are most of these holes on top, or underneath?",
        "options": [
            ("On the top surface", "On the underside. It is shaded and cooler there, so less water evaporates."),
            ("On the underside", "On the underside. It is shaded and cooler there, so less water evaporates."),
        ],
        "answer": 1,
    },
    "words": ["adaptation", "palisade cells", "stomata", "cuticle"],
    "word_defs": {
        "adaptation": "A feature that helps an organism survive where it lives.",
        "palisade cells": "Tall cells packed with chloroplasts, just under the top surface of a leaf.",
        "stomata": "Tiny holes in a leaf that let gases in and out. One is a stoma.",
        "cuticle": "The waxy layer on the outside of a leaf. It reduces water loss.",
    },
    "knowledge": [
        {"kind": "card", "title": "Inside a leaf",
         "body": [{"figure": "b7-leaf-section"},
                  "Carbon dioxide enters through a stoma on the underside.",
                  "It diffuses through the air spaces to the palisade cells.",
                  "Water arrives through the veins."]},
        {"kind": "reveal", "title": "Each part of a leaf and its job",
         "cols": ["Where it is", "Its job"],
         "rows": [
             ("Broad, flat shape", "The whole leaf", "Gives a large surface area to absorb light"),
             ("Waxy cuticle", "The outer surface, thickest on top", "Reduces water loss"),
             ("Upper epidermis", "Top layer of cells, under the cuticle", "See-through, so light reaches the palisade cells"),
             ("Palisade cells", "Just under the upper epidermis", "Do most of the photo­synthesis. Packed with chloro­plasts, near the light."),
             ("Spongy layer", "Below the palisade cells", "Air spaces let carbon dioxide reach the cells and oxygen get out"),
             ("Stomata", "Mostly on the underside", "Let carbon dioxide in, and oxygen and water vapour out"),
             ("Guard cells", "Around each stoma", "Open and close the stoma"),
             ("Veins", "All through the leaf", "Bring water in and carry sugars away"),
         ]},
        {"kind": "card", "title": "Why a leaf is thin",
         "body": ["Carbon dioxide diffuses from the stomata to every cell.",
                  "In a thin leaf, this distance is short, so it arrives quickly.",
                  "Light also gets dimmer as it passes down through the leaf.",
                  "So extra cells deep in a thick leaf would get little light.",
                  "Adding more cells does not add much photosynthesis."]},
        {"kind": "card", "title": "Why stomata are underneath",
         "body": ["Stomata let carbon dioxide in. But water vapour escapes through them too.",
                  "The underside is shaded and cooler, so less water evaporates there.",
                  "Guard cells open the stomata in the light. They close them at night.",
                  "They also close them when the plant is short of water."]},
        {"kind": "card", "title": "Light against water",
         "body": ["Features that help photosynthesis can also make a leaf lose more water.",
                  "So the best leaf depends on where the plant lives.",
                  {"points": ["Dark forest floor: large, thin, dark green leaves catch more light. "
                              "Water is plentiful, so losing water matters less.",
                              "Hot, dry places: small leaves, a thick cuticle and few stomata.",
                              "A cactus has spines instead of leaves. Its green stem photosynthesises."]},
                  "Leaves that save water photosynthesise more slowly. So these plants grow slowly."]},
        {"kind": "card", "title": "Why leaves look green",
         "body": ["Chlorophyll absorbs mostly red and blue light.",
                  "It reflects much of the green light, so leaves look green.",
                  "So under green light alone, a plant photosynthesises slowly."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Stomata only let oxygen out.",
              "They let carbon dioxide in, and oxygen and water vapour out."),
             ("Bigger leaves are always better.",
              "Big leaves lose more water. The best leaf depends on the habitat."),
             ("Carbon dioxide gets in through the cuticle.",
              "It gets in through the stomata. The waxy cuticle lets very little gas through."),
         ]}]},
    ],
    "key_fact": "A leaf is adapted for photosynthesis. It is broad to absorb light and thin so gases "
                "diffuse quickly. Palisade cells full of chloroplasts sit near the top surface. Stomata "
                "on the underside let carbon dioxide in.",
    "deeper": [
        {"kind": "card", "title": "Why leaves change colour in autumn",
         "body": ["In autumn, many trees break down their chlorophyll.",
                  "Yellow and orange pigments were in the leaf all summer.",
                  "Without the green, these pigments now show."]},
        {"kind": "card", "title": "Why pine trees keep their needles",
         "body": ["Pine needles are small, tough and waxy.",
                  "They lose very little water, even in winter.",
                  "So a pine tree can keep its leaves all year."]},
    ],
    "try": None,
    "tutor_body": "Want to check which leaf features suit a habitat?",
    "figure_caption": {"b7-leaf-section": "Most leaves are less than half a millimetre thick."},
    "ladder_stem": {
        "apply": "Pondweed is put under a green filter, then a red filter. Both let through the same "
                 "amount of light energy. It gives off far fewer bubbles under green. Which is the best "
                 "explanation?",
        "explain": "A leaf is usually less than half a millimetre thick. Explain why being thin helps. "
                   "Then explain why a leaf twice as thick would not photosynthesise twice as fast.",
        "produce": "Design a leaf for a plant on a dark rainforest floor, where water is plentiful. Then "
                   "design one for a plant on a hot, dry hillside. Give three features of each. Explain "
                   "each one using light and water loss. Say what each leaf gives up.",
    },
    "ladder_ticks": [
        ["Says a short diffusion distance means the gas arrives quickly, so no cell is starved of it.",
         "Says a short distance means carbon dioxide reaches every cell quickly."],
        ["Says light is absorbed as it passes through the leaf, so cells deeper down receive less of it.",
         "Says light is absorbed on the way down, so deeper cells get less."],
        ["Concludes that extra chloroplasts low in a thick leaf would sit in dim light and receive carbon dioxide "
         "slowly, so they would add little.",
         "Says chloroplasts deep in a thick leaf get dim light and carbon dioxide slowly."],
        ["Notes that a thicker leaf also costs more tissue to build and to keep alive — or gives another cost, "
         "such as weight or shading.",
         "Says more cells do not help if light and carbon dioxide cannot reach them."],
        ["Forest floor: broad or very large surface area, justified by the scarcity of light.",
         "Forest floor: three light-catching features, such as large, thin, dark green leaves."],
        ["Forest floor: accepts the high water loss, because water is plentiful there.",
         "Forest floor: says losing more water does not matter, because water is plentiful there."],
        ["Dry hillside: small surface area, few stomata, or a thick waxy cuticle — at least two of these.",
         "Dry hillside: three water-saving features, such as small leaves, few stomata, thick cuticle."],
        ["Dry hillside: says the cost of those features is a lower rate of photosynthesis, and that the plant "
         "therefore grows slowly.",
         "Dry hillside: says these features slow photosynthesis, so the plant grows slowly."],
        ["States explicitly that neither leaf is better in general — each is the compromise that suits its habitat.",
         "Forest floor: says this leaf would lose too much water in a dry place."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Palisade cells are not for support. They are packed with chloroplasts.",
            2: "Most stomata are on the underside, not the top.",
            3: "Water comes in through the veins. Palisade cells are on top for the light.",
        },
        "apply": {
            0: "Both filters let through the same light energy. Chlorophyll absorbs less green light.",
            2: "A filter only changes the light. Carbon dioxide still reaches the pondweed.",
            3: "Leaves look green because they reflect green light. They do not store it.",
        },
    },
}
