# -*- coding: utf-8 -*-
"""Culturing microorganisms, in the lean shape. Spec table: ks4-culturing-microorganisms.md (AQA 8461
4.1.1.6, "(biology only)": Triple routes only, TF and TH; 8464 has no such section). One line is
"(HT only)": expressing the number of bacteria in standard form, so that card is on TH only. The
practical is 8461 Required practical 2 (antiseptics or antibiotics and zones of inhibition).

LEGACY (batch 6). The ladder and the practice set stay from the Design page. The practice set is the
page's own hard-coded bank (four shared items plus a fifth that differs: standard form on TH, taping
the lid on TF), so its fixes are logic_edits. Every stem is kept, so every ks4q: id survives. Rung
prompts keep their positions, so rung ids survive; Rung 3 (i) keeps its position with a new chain.
The doubling steps (cm-w, cm-a) are placed in a card as they were.
This batch's logic is plain ASCII with \\uXXXX escapes; the edits below are written that way
(generated from the post-ruling logic, so each `old` occurs exactly once).
"""

LOGIC_EDITS = \
[
    # Before the library loads, R has no isTriple, so the per-route eyebrow would read the Combined Science wording on this Biology-only page for a moment. The fallback route is Triple Higher, so it says so.
    ("const R = K ? K.route(this) : { route: 'Triple Higher', onRoute: () => {}, isHigher: true };",
     "const R = K ? K.route(this) : { route: 'Triple Higher', onRoute: () => {}, isHigher: true, isTriple: true };"),
    # The props object was a bare `return {`; lean_ks4 binds the per-route eyebrow (and the record's equations) into `Object.assign({}, R, {`. The page's own keys come after R, so route, isHigher and the rest are unchanged.
    ('    return {\n      route, onRoute: R.onRoute,',
     '    return Object.assign({}, R, {\n      route, onRoute: R.onRoute,'),
    ('      endConnects: []\n    };',
     '      endConnects: []\n    });'),
    # Practice Q1 (25 °C), stem kept: credited the longest (+55), dash.
    ("opts: [['Safety \\u2014 bacteria that grow optimally at 37\\u00b0C are more likely to be harmful human pathogens', true], ['Bacteria grow faster at 25\\u00b0C', false], ['37\\u00b0C would melt the agar', false], ['Antibiotics only work at 25\\u00b0C', false]],",
     "opts: [['To reduce the chance of growing human pathogens', true], ['Bacteria grow faster at 25\\u00a0\\u00b0C than at 37\\u00a0\\u00b0C', false], ['The agar jelly would melt at 37\\u00a0\\u00b0C in the incubator', false], ['Antibiotics only work at temperatures up to 25\\u00a0\\u00b0C', false]],"),
    ("wrong_explanations: { 1: 'Bacteria generally grow FASTER at higher temperatures \\u2014 37\\u00b0C would give quicker results, but the safety risk outweighs this.', 2: 'Agar melts at much higher temperatures (around 85\\u00b0C) \\u2014 37\\u00b0C would not melt it.', 3: 'Antibiotic effectiveness is not temperature-dependent in this way \\u2014 the safety concern is the primary reason.' } },",
     "wrong_explanations: { 1: 'Bacteria generally grow faster when it is warmer. 25\\u00a0\\u00b0C is for safety.', 2: 'Agar stays solid well above 37\\u00a0\\u00b0C.', 3: 'The lower temperature is for safety, not for the antibiotics.' } },"),
    # Practice Q2 (large clear zone), stem kept: credited the longest (+50), dash.
    ("opts: [['The antibiotic is highly effective against that bacterium \\u2014 it diffuses outward and kills bacteria in a wide area', true], ['The bacteria are resistant \\u2014 they moved away from the antibiotic', false], ['The disc absorbed the bacteria, leaving a clear area', false], ['The agar failed to set properly in that area', false]],",
     "opts: [['The antibiotic works well against these bacteria', true], ['The bacteria are resistant and moved away from it', false], ['The paper disc soaked up the bacteria around it', false], ['The agar did not set properly around the disc', false]],"),
    ("wrong_explanations: { 1: 'Resistant bacteria show NO inhibition zone \\u2014 they grow right up to the disc.', 2: 'Discs absorb the antibiotic solution \\u2014 they don\\u2019t absorb bacteria.', 3: 'Properly prepared agar sets evenly \\u2014 uneven setting would affect all areas, not just around specific discs.' } },",
     "wrong_explanations: { 1: 'Resistant bacteria grow right up to the disc, so there is no clear zone.', 2: 'The disc holds the antibiotic. It does not soak up bacteria.', 3: 'Agar sets evenly. The clear zone is where the bacteria did not grow.' } },"),
    # Practice Q3 (flaming the loop), stem kept: credited the longest (+60), dash.
    ("opts: [['To sterilise it \\u2014 killing all microorganisms before use (preventing contamination) and after use (preventing spread)', true], ['To warm the loop so bacteria transfer more easily', false], ['To melt the agar so bacteria can be mixed in', false], ['To activate the bacteria before plating', false]],",
     "opts: [['To sterilise it, by killing any microorganisms on it', true], ['To warm the loop so bacteria transfer more easily', false], ['To melt the agar so the bacteria can be mixed in', false], ['To activate the bacteria before they are spread', false]],"),
    ("wrong_explanations: { 1: 'Warming would not sterilise \\u2014 only red-hot temperatures kill all microorganisms.', 2: 'The loop does not touch agar during streaking in a way that needs melting \\u2014 it is used at room temperature to spread bacteria on the surface.', 3: 'Bacteria don\\u2019t need \\u2018activation\\u2019 \\u2014 flaming is purely for sterilisation.' } },",
     "wrong_explanations: { 1: 'Warming is not enough. The flame kills microorganisms on the loop.', 2: 'The loop spreads bacteria over the agar surface. It does not melt it.', 3: 'Bacteria do not need activating. Flaming sterilises the loop.' } },"),
    # Practice Q5 on Triple Foundation (taping the lid), stem kept: credited the longest (+24).
    ("opts: [['So oxygen can get in and harmful anaerobic bacteria don\\u2019t grow', true], ['So the lid can be lifted off easily', false], ['So the agar can dry out', false], ['So more bacteria can get in from the air', false]],",
     "opts: [['So oxygen gets in and anaerobic bacteria do not grow', true], ['So the lid can easily be lifted off to check it', false], ['So the agar can dry out more quickly in the air', false], ['So more bacteria from the air can reach the agar', false]],"),
    # First worked example: the Convert line was wordy, with a dash, and Insert repeated the halving. Same numbers: r = 9 mm, π × 81 = 254.47 mm².
    ("{ letter: 'C', label: 'Convert', line: 'Nothing to convert \\u2014 the diameter is given in millimetres (mm) and the radius and area are calculated in millimetres throughout, so no unit conversion is needed.',",
     "{ letter: 'C', label: 'Convert', line: 'Nothing to convert: the diameter is in mm.',"),
    ("{ letter: 'I', label: 'Insert', line: 'Diameter = 18 mm \\u2192 radius = 9 mm. Area = \\u03c0 \\u00d7 9\\u00b2' }",
     "{ letter: 'I', label: 'Insert', line: 'Area = \\u03c0 \\u00d7 9\\u00b2' }"),
    # Rung 3 (i) chain: its three links were three separate facts (tape, oxygen, upside down) that fit in any order. It is now one chain with one order; the taping reasons are taught in Key knowledge. Prompt reworded; the rung keeps its position, so its id.
    ("prompt: 'Explain why the lid of a Petri dish is taped and the dish stored upside down. Put the links in order.',\n            links: ['A few strips of tape stop the lid coming off, so microorganisms from the air can\\u2019t get in.', 'Not taping all the way round lets oxygen in, so harmful anaerobic bacteria don\\u2019t grow.', 'Storing it upside down stops condensation dripping onto the agar and spreading the colonies.'],\n            herrings: [{ text: 'The tape keeps oxygen out so the bacteria grow faster.', why: 'Oxygen should get in.' }, { text: 'Upside down lets the agar drain.', why: 'The agar is a solid gel; the reason is condensation.' }] },",
     "prompt: 'Explain why a Petri dish is stored upside down. Put the links in order.',\n            links: ['Water from the agar condenses into drops on the inside of the lid.', 'If the lid were on top, these drops would fall onto the agar.', 'Falling drops would spread the colonies, so the dish is stored upside down.'],\n            herrings: [{ text: 'Storing it upside down keeps oxygen away from the bacteria.', why: 'Oxygen should reach the culture. The reason is condensation.' }, { text: 'Upside down lets the agar drain.', why: 'The agar is a solid gel; the reason is condensation.' }] },"),
    # Examiner, 26 Nov 2026: practice Q4 (1 hour, a division every 20 minutes), the reply for "6".
    ("2: 'That adds 2 each time. Bacteria double each division.'",
     "2: '6 is 3 \\u00d7 2. Bacteria double at each division: 1 \\u2192 2 \\u2192 4 \\u2192 8.'"),
    # Blind check, 26 Nov 2026 (CU-07, Rung 2 (ii)): a pupil working in hours (3 divisions an hour,
    # for 2 hours) could defend "Nothing to convert", but the key is hours to minutes. That choice is
    # swapped for a conversion that is wrong; the credited choice and its position are unchanged.
    # ("Convert minutes to hours: divide by 60", the swap first suggested, is a CORRECT conversion
    # that also reaches 6 divisions, so it would have kept the ambiguity.)
    ("convOptions: ['Nothing to convert', 'Convert hours to minutes: multiply by 60', 'Convert minutes to hours: multiply by 60'], convAnswer: 1, answer: 640",
     "convOptions: ['Convert hours to minutes: divide by 60', 'Convert hours to minutes: multiply by 60', 'Convert minutes to hours: multiply by 60'], convAnswer: 1, answer: 640"),
]

# The Design page's two triangles (its EQ_A and EQ_N, unchanged).
EQUATIONS = {
    "EQ_AREA": {"name": "Area of a circle", "written": "A = π r²", "source": "none",
                "top": {"s": "A", "name": "area", "unit": "mm²"},
                "bottom": [{"s": "π", "name": "pi, about 3.14", "unit": "", "fixed": True},
                           {"s": "r²", "root": "r", "name": "radius", "unit": "mm"}]},
    "EQ_DIV": {"name": "Number of divisions", "written": "number of divisions = time ÷ mean division time",
               "source": "none",
               "top": {"s": "t", "name": "time", "unit": "min"},
               "bottom": [{"s": "n", "name": "number of divisions", "unit": "no unit"},
                          {"s": "d", "name": "mean division time", "unit": "min"}]},
}

LESSON = {
    "slug": "culturing-microorganisms",
    "start": {
        "setup": "One slice of bread is kept on a warm kitchen worktop and another in the fridge.",
        "question": "If you had to guess, would mould and bacteria grow faster somewhere warm, or somewhere cold?",
        "options": [
            ("Somewhere warm",
             "Somewhere warm. Bacteria multiply faster when they have a suitable temperature and "
             "enough nutrients."),
            ("Somewhere cold",
             "Somewhere warm. Cold slows bacteria down, which is why food keeps longer in a fridge."),
        ],
        "answer": 0,
    },
    "words": ["binary fission", "aseptic technique", "culture", "zone of inhibition"],
    "knowledge": [
        {"kind": "card", "title": "How bacteria multiply",
         "body": ["Bacteria multiply by simple cell division, called binary fission. This can happen "
                  "as often as once every 20 minutes if they have enough nutrients and a suitable "
                  "temperature. Each division doubles the number of bacteria.",
                  "Bacteria can be grown in a nutrient broth solution, or as colonies on an agar gel "
                  "plate."]},
        {"kind": "card", "title": "Why a culture must be pure",
         "body": ["Uncontaminated cultures of microorganisms are needed to investigate the action of "
                  "disinfectants and antibiotics. Aseptic technique keeps a culture "
                  "uncontaminated."]},
        {"kind": "reveal", "title": "Aseptic technique",
         "cols": ["Why"],
         "rows": [
             ("Sterilise Petri dishes and culture media before use", "To kill any microorganisms "
              "already on them"),
             ("Pass the inoculating loop through a flame", "To sterilise it, killing the "
              "microorganisms on it"),
             ("Secure the lid with a few strips of tape", "So microorganisms from the air cannot get "
              "in. Not sealing it all the way round lets oxygen in, so harmful anaerobic bacteria "
              "do not grow"),
             ("Store the dish upside down", "So drops of condensation fall onto the lid, not onto "
              "the agar"),
             ("Incubate at 25 °C in school", "To reduce the chance of growing pathogens that "
              "could harm humans"),
         ]},
        {"kind": "card", "title": "Required practical 2: antibiotics and antiseptics",
         "body": [{"slot": "fig:agar-plate-zones"},
                  {"points": [
                      "Use aseptic technique to spread bacteria evenly over an agar plate.",
                      "Place paper discs soaked in different antibiotics or antiseptics on the agar, "
                      "and a control disc soaked in sterile water.",
                      "Keep the disc size, the concentration and the incubation time the same. Tape "
                      "the lid, store the dish upside down and incubate at 25 °C.",
                      "Measure the diameter of the clear zone around each disc. This is the zone of "
                      "inhibition, where the bacteria have not grown.",
                  ]},
                  "The bigger the clear zone, the more effective the antibiotic or antiseptic. In the "
                  "drawing, B is the most effective, and C did not stop these bacteria growing."]},
        {"kind": "card", "title": "Area of a clear zone",
         "body": [{"slot": "triangle:EQ_AREA"},
                  "Measure the diameter, then halve it to get the radius r. Keep every length in "
                  "mm, so the area is in mm²: cm × 10 gives mm.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Number of bacteria after a time",
         "body": [{"slot": "triangle:EQ_DIV"},
                  {"points": [
                      "Step 1: number of divisions = time ÷ mean division time. Put both times in "
                      "minutes first.",
                      "Step 2: double the starting number once for each division. This is the same "
                      "as starting number × 2ⁿ, where n is the number of divisions.",
                  ]},
                  "One bacterium dividing every 20 minutes for 3 hours: 180 ÷ 20 = 9 divisions, "
                  "and 1 × 2⁹ = 512 bacteria.",
                  {"slot": "steps-worked"},
                  {"slot": "steps-attempt"}]},
        {"kind": "card", "title": "Higher: standard form", "routes": ["TH"],
         "body": ["Give a large number of bacteria in standard form. Move the decimal point until "
                  "one digit is in front of it, and count the places moved.",
                  {"points": [
                      "512 = 5.12 × 10²",
                      "2 560 000 = 2.56 × 10⁶",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Incubate at 37 °C because bacteria grow best at body temperature.",
              "In school, incubate at 25 °C. This reduces the chance of growing pathogens that "
              "could harm humans."),
             ("Each division adds 2 bacteria.",
              "Each division doubles the number of bacteria."),
             ("Put the diameter of the clear zone into πr².",
              "Halve the diameter first to get the radius."),
         ]}]},
    ],
    "key_fact": "Bacteria multiply by binary fission, as often as once every 20 minutes, so each "
                "division doubles the number. Aseptic technique keeps a culture uncontaminated, and "
                "the bigger the clear zone around a disc, the more effective the antibiotic or "
                "antiseptic.",
    "deeper": [
        {"kind": "card", "title": "Why the control disc matters",
         "body": ["The control disc is the same paper, soaked in sterile water, with only the "
                  "antibiotic left out. If the bacteria grow right up to its edge, the paper and "
                  "the water are ruled out, so a clear zone round another disc is down to the "
                  "antibiotic on it."]},
        {"kind": "card", "title": "Where this goes next",
         "body": ["Antibiotics, and bacteria that are resistant to them, are in Antibiotics and "
                  "painkillers."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain why</strong> for each aseptic step: the step, then what it prevents.",
             "<strong>Calculate</strong> an area: halve, then πr². A number of bacteria: "
             "divide, then double.",
             "<strong>Compare</strong> antibiotics: the sizes of the clear zones, in a fair test, "
             "against the control.",
         ]}]},
    ],
    "equations": EQUATIONS,
    "try": None,
    "legacy": {"batch": "batch-6", "logic_edits": LOGIC_EDITS},
}
