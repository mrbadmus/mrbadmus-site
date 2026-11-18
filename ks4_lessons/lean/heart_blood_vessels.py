# -*- coding: utf-8 -*-
"""The heart and blood vessels, in the lean shape. Spec table: ks4-heart-blood-vessels.md (AQA 8464
4.2.2.2 / 8461 4.2.2.2, word for word the same; no HT-only or Biology-only lines). Pacemakers are
here; faulty valves and their replacement are on Coronary heart disease (4.2.2.4).

LEGACY (batch 4). The ladder and the practice set stay from the Design page. The practice set is
the page's own hard-coded `bankSrc` (same five items on every route), so its fixes are
logic_edits. No practice-set stem is edited, so every ks4q: id survives; rung prompts keep their
positions, so rung ids survive. The bank's "Why do veins have valves but arteries do not?" stem
is kept (its id): the credited answer now says why veins need them; see UNSURE.md.
"""


def _js(s):
    """This batch's logic is plain ASCII with \\uXXXX escapes: spell a target the way the file does."""
    # Every non-ASCII character as backslash-u + 4 lower-case hex, the way these logic files spell
    # them (backslashreplace gave \\xNN for U+0080-U+00FF: µ ° ÷ × would never match).
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in s)


_EDITS = [
    # Practice Q1 (left ventricle), stem kept: credited option visibly the longest (+52), dash.
    ("['It pumps blood to the whole body — needs much higher pressure than the right ventricle which only pumps to the nearby lungs', true]",
     "['It pumps blood all round the body, at a higher pressure', true]"),
    ("wrong_explanations: { 1: 'Both ventricles receive the same volume of blood per beat — the difference is in the distance the blood must be pumped, not the volume.', 2: 'Body size has no relationship to heart wall thickness — it’s purely about pumping distance and pressure.', 3: 'Oxygenated and deoxygenated blood have essentially the same density — the thickness difference is purely about pressure requirements.' }",
     "wrong_explanations: { 1: 'Both ventricles pump the same volume of blood. The left pumps it further, at a higher pressure.', 2: 'Body shape is not the reason. The left ventricle pumps blood all round the body.', 3: 'Oxygenated and deoxygenated blood weigh about the same. The reason is the higher pressure needed.' }"),
    # Practice Q2 (pulmonary artery), stem kept: credited option visibly the longest (+30), dash
    # tails, "the most common mistake in this topic!" and capitals in the replies.
    ("opts: [['Deoxygenated blood — it has just returned from the body and needs to be reoxygenated', true], ['Oxygenated blood — all arteries carry oxygenated blood', false], ['A mixture of oxygenated and deoxygenated blood', false], ['Blood with no red blood cells — only plasma', false]],",
     "opts: [['Deoxygenated blood', true], ['Oxygenated blood', false], ['A mixture of oxygenated and deoxygenated blood', false], ['Plasma with no red blood cells', false]],"),
    ("wrong_explanations: { 1: 'This is the most common mistake in this topic! Arteries carry blood AWAY from the heart — but the pulmonary artery specifically carries deoxygenated blood to be oxygenated in the lungs.', 2: 'Blood in the heart is kept completely separate — left side carries oxygenated, right side carries deoxygenated. There is no mixing.', 3: 'All blood contains red blood cells — plasma alone would have no oxygen-carrying capacity.' }",
     "wrong_explanations: { 1: 'Arteries carry blood away from the heart. The pulmonary artery carries deoxygenated blood to the lungs.', 2: 'The two sides of the heart are kept separate, so the blood does not mix.', 3: 'All blood contains red blood cells.' }"),
    # Practice Q3 (valves in veins), stem kept: credited option two sentences (+63), dash; one
    # reply ("Valves in veins do slightly slow flow") muddled the item.
    ("['Blood pressure in veins is low — valves prevent backflow. Arterial pressure is high enough to keep blood flowing in the right direction', true], ['Arteries have thicker walls so they don’t need valves', false], ['Veins carry deoxygenated blood which needs extra support to flow', false], ['Valves in arteries would slow down the high-pressure blood flow too much', false]],",
     "['Blood in veins is at low pressure, so valves stop backflow', true], ['Arteries have thicker walls, so they do not need valves', false], ['Veins carry deoxygenated blood, which needs help to flow', false], ['Valves would slow down the blood in arteries too much', false]],"),
    ("wrong_explanations: { 1: 'Wall thickness helps arteries withstand pressure — but valves are specifically about preventing BACKFLOW, which is a problem in low-pressure veins, not high-pressure arteries.', 2: 'The oxygen content of blood has nothing to do with the need for valves — the PRESSURE is what matters.', 3: 'Valves in veins do slightly slow flow, but that’s acceptable — their role is to prevent dangerous backflow in low-pressure vessels.' }",
     "wrong_explanations: { 1: 'Thick walls let arteries withstand high pressure. Valves are about stopping backflow.', 2: 'It is the low pressure, not the oxygen, that makes backflow a risk in veins.', 3: 'Arteries do not need valves along their length, because the high pressure keeps the blood moving forward.' }"),
    # Practice Q4 (capillaries), stem kept: credited option visibly the longest (+33); the
    # distractor "carry both oxygenated and deoxygenated blood" was not definitely wrong (blood
    # gives up oxygen along a capillary), so it is replaced.
    ("opts: [['Walls are only one cell thick — very short diffusion distance. Dense network = large surface area', true], ['They have the highest blood pressure of all blood vessels', false], ['They carry both oxygenated and deoxygenated blood simultaneously', false], ['They have valves to keep substances moving in one direction', false]],",
     "opts: [['Their walls are one cell thick, and they have a large surface area', true], ['They have the highest blood pressure of all blood vessels', false], ['They have thick muscular walls that push substances out', false], ['They have valves to keep substances moving in one direction', false]],"),
    ("wrong_explanations: { 1: 'Arteries have the highest blood pressure. By the time blood reaches the capillaries the pressure has already dropped a lot.', 2: 'Which blood a capillary carries is not what makes it good at exchange — thin walls and a large surface area are.', 3: 'Capillaries have no valves — substances move by DIFFUSION driven by concentration gradients.' }",
     "wrong_explanations: { 1: 'Arteries have the highest blood pressure.', 2: 'Capillary walls are one cell thick, which keeps the diffusion distance short.', 3: 'Capillaries have no valves. Substances move in and out by diffusion.' }"),
    # Practice Q5 (artificial pacemaker), stem kept: credited option visibly the longest (+23).
    ("[['It is an electrical device that corrects irregularities in the heart rate', true], ['It replaces a faulty heart valve', false],",
     "[['It is an electrical device that corrects an irregular heart rate', true], ['It replaces a faulty heart valve with a mechanical one', false],"),
]

# Examiner pass (EXAMINER.md) and blind pass, 18 Nov 2026. Each old string is the logic AFTER the
# edits above, and occurs exactly once (validate.py checks).
_EDITS += [
    ("links: ['The left ventricle pumps blood all round the body.', 'The right ventricle only pumps blood to the lungs, which are close by.', 'So the left ventricle must pump at a higher pressure, which needs more muscle.'],",
     "links: ['The left ventricle pumps blood all round the body, not just to the lungs.', 'So it must pump at a higher pressure than the right ventricle.', 'A higher pressure needs more muscle, so its wall is thicker.'],"),
    ("links: ['There are millions of alveoli, giving a very large surface area.', 'Their walls are thin, so the diffusion distance is short.', 'A dense capillary network carries oxygen away, keeping the concentration gradient steep.'],",
     "links: ['The walls of the alveoli and the capillaries are very thin.', 'So oxygen only has a short distance to diffuse into the blood.', 'The blood then carries the oxygen away, so the concentration gradient stays steep.'],"),
    ("[['It is an electrical device that corrects an irregular heart rate', true],",
     "[['It corrects irregularities in the heart rate', true],"),
    ("heartFig: ready ? K.fig(this.heart(st), '') : null,",
     "heartFig: ready ? K.fig(this.heart(), '') : null,"),
    ("b += D.T(240, 360, 'valve', 13, { weight: 'normal' });",
     "b += D.T(132, 210, 'valve', 13, { weight: 'normal' }) + D.line(152, 206, 222, 205, 1.5);"),
    ("convOptions: ['Nothing to convert', 'Convert seconds to minutes: divide by 60'",
     "convOptions: ['Nothing to convert: use 15 s as the time', 'Convert seconds to minutes: divide by 60'"),
]

LESSON = {
    "slug": "heart-blood-vessels",
    "start": {
        "question": "If you had to guess, on one full trip round the body, how many times does "
                    "blood pass through the heart?",
        "options": [
            ("Once",
             "Twice. The right side pumps blood to the lungs, and the left side pumps it round the "
             "rest of the body. This is a double circulatory system."),
            ("Twice",
             "Twice. The right side pumps blood to the lungs, and the left side pumps it round the "
             "rest of the body. This is a double circulatory system."),
        ],
        "answer": 1,
    },
    "words": ["double circulatory system", "ventricle", "pacemaker", "alveoli"],
    "knowledge": [
        {"kind": "card", "title": "A double circulatory system",
         "body": ["The heart is an organ that pumps blood around the body in a double circulatory "
                  "system.",
                  {"slot": "legacy-fig:heartFig"},
                  {"points": [
                      "The right ventricle pumps blood to the lungs, where gas exchange takes "
                      "place.",
                      "The left ventricle pumps blood around the rest of the body.",
                      "Blood from the body returns to the right atrium. Blood from the lungs "
                      "returns to the left atrium.",
                  ]},
                  "Valves in the heart stop blood flowing backwards. You do not need their "
                  "names."]},
        {"kind": "reveal", "title": "The blood vessels of the heart",
         "cols": ["Carries blood"],
         "rows": [
             ("Vena cava", "From the body to the right atrium"),
             ("Pulmonary artery", "From the right ventricle to the lungs"),
             ("Pulmonary vein", "From the lungs to the left atrium"),
             ("Aorta", "From the left ventricle to the rest of the body"),
             ("Coronary arteries", "Over the heart, supplying the heart muscle with oxygenated "
                                   "blood"),
         ]},
        {"kind": "card", "title": "The thicker left ventricle",
         "body": ["The left ventricle has a thicker muscle wall than the right ventricle.",
                  "It pumps blood all round the body, so it must pump at a higher pressure. The "
                  "right ventricle only pumps blood to the lungs, which are close by."]},
        {"kind": "card", "title": "The lungs",
         "body": ["Air passes down the trachea, into the bronchi, then into millions of tiny air "
                  "sacs called alveoli. A network of capillaries surrounds the alveoli.",
                  {"slot": "legacy-fig:lungFig"},
                  "Oxygen diffuses from the alveoli into the blood. Carbon dioxide diffuses from "
                  "the blood into the alveoli.",
                  {"points": [
                      "Millions of alveoli give a very large surface area.",
                      "The alveolus wall and the capillary wall are thin, so the diffusion "
                      "distance is short.",
                      "The capillary network carries oxygen away and brings carbon dioxide, so "
                      "the concentration gradients stay steep.",
                  ]}]},
        {"kind": "card", "title": "Pacemakers",
         "body": ["The natural resting heart rate is controlled by a group of cells located in "
                  "the right atrium that act as a pacemaker.",
                  "Artificial pacemakers are electrical devices used to correct irregularities "
                  "in the heart rate."]},
        {"kind": "card", "title": "Arteries, veins and capillaries",
         "body": ["The body contains three different types of blood vessel.",
                  {"slot": "legacy-fig:vesselFig"}]},
        {"kind": "reveal", "title": "How each blood vessel suits its job",
         "cols": ["Structure", "Function"],
         "rows": [
             ("Artery", "Thick muscular wall with elastic fibres",
              "Carries blood away from the heart at high pressure"),
             ("Vein", "Thinner wall, wide lumen, and valves",
              "Carries blood back to the heart at low pressure; the valves stop it flowing "
              "backwards"),
             ("Capillary", "Wall one cell thick, in a dense network",
              "Exchange with the tissues: a short diffusion distance and a large surface area"),
         ]},
        {"kind": "card", "title": "Rate calculations",
         "body": ["A rate is an amount divided by the time.",
                  {"points": [
                      "rate of blood flow = volume of blood ÷ time",
                      "heart rate = number of beats ÷ time",
                  ]},
                  "Convert to the units the question asks for first, such as dm³ and minutes.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("All arteries carry oxygenated blood.",
              "Arteries carry blood away from the heart. The pulmonary artery carries "
              "deoxygenated blood to the lungs."),
             ("The left ventricle pumps more blood than the right.",
              "Both pump the same volume. The left pumps at a higher pressure."),
             ("The lungs pump oxygen into the blood.",
              "Oxygen diffuses from the alveoli into the blood."),
         ]}]},
    ],
    "key_fact": "The heart pumps blood around the body in a double circulatory system: the right "
                "ventricle pumps blood to the lungs, where gas exchange takes place, and the left "
                "ventricle pumps blood around the rest of the body. Arteries carry blood away from "
                "the heart at high pressure, veins carry it back at low pressure, and capillaries "
                "have walls one cell thick for exchange.",
    "deeper": [
        {"kind": "card", "title": "Blood pressure round the body",
         "body": ["The pressure is highest in the arteries, lower in the capillaries, and lowest "
                  "in the veins."]},
        {"kind": "card", "title": "When the heart goes wrong",
         "body": ["Blocked coronary arteries and faulty valves, and how they are treated, are on "
                  "Coronary heart disease."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Name</strong> a blood vessel: aorta, vena cava, pulmonary artery, pulmonary "
             "vein or coronary artery.",
             "<strong>Explain</strong> an adaptation: give the feature, then say what it does, "
             "such as \"thin walls, so a short diffusion distance\".",
             "<strong>Calculate</strong> a rate: convert first, then amount ÷ time.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-4", "logic_edits": [(_js(a), _js(b)) for a, b in _EDITS]},
}
