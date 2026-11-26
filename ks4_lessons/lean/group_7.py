# -*- coding: utf-8 -*-
"""Group 7, the halogens, in the lean shape. Spec table: ks4-group-7.md (AQA 8464 5.1.2.6 / 8462
4.1.2.6, word for word the same; no Chemistry-only lines). The ionic equation for a displacement
uses 5.1.1.1's HT-only line (ionic equations), so that card is on the Higher routes only.

LEGACY (batch 11). The ladder (Ks4Practice, 2·2·2·1) and the practice set (the page's own BANK,
the same five items on every route) stay from the Design page; their fixes are logic_edits below.
Every practice stem is kept byte for byte, so every practice id is kept. The batch-11 header writes
"AQA Chemistry 5.1.2.6 · Combined and Triple"; lean_ks4 rebuilds it per route from
batch_lean.CHEM_EYEBROW (needs the 5.1 eyebrow patch).

logic_edits: the five practice items, one edit each (the whole BANK line, stem unchanged). The
rungs were checked and need no edit.
"""

LOGIC_EDITS = [
    # Practice Q1 (chlorine water + potassium bromide): the credited label was the longest, and the replies shouted. Credited label now 'The solution turns orange' (bromine solution is orange).
    ('      V("Chlorine water is added to a solution of potassium bromide. What is observed?", [["The solution turns orange/brown — chlorine displaces bromide ions, releasing bromine", true], ["No change — chlorine cannot react with bromide ions", false], ["The solution turns pale green — chlorine is absorbed by the solution", false], ["A white precipitate forms — chlorine reacts with potassium ions", false]], { "1": "Chlorine IS more reactive than bromine and CAN displace bromide — so a reaction does occur.", "2": "Chlorine water has a yellow-green colour but when it reacts with bromide, the BROWN colour of bromine is what appears in the solution.", "3": "Chlorine does not react with potassium ions — it displaces bromide ions. No precipitate forms." }),',
     '      V("Chlorine water is added to a solution of potassium bromide. What is observed?", [["The solution turns orange — Chlorine displaces bromine from the bromide", true], ["No change — chlorine cannot react with bromide ions", false], ["The solution turns pale green — chlorine is absorbed by the solution", false], ["A white precipitate forms — chlorine reacts with potassium ions", false]], { "1": "Chlorine is more reactive than bromine, so it does displace it.", "2": "Bromine forms in the solution, and bromine solution is orange.", "3": "Chlorine does not react with the potassium ions. No precipitate forms." }),'),
    # Practice Q2 (why fluorine is more reactive): replies used capitals; one said 'the closeness wins over the fewer-proton effect'. Replies rewritten; options kept.
    ('      V("Why is fluorine more reactive than chlorine?", [["Fluorine is a smaller atom — its outer shell is closer to the nucleus, so it attracts an incoming electron more strongly", true], ["Fluorine has fewer electrons, making it less stable and more reactive", false], ["Fluorine has more protons, making its positive charge stronger", false], ["Fluorine is a gas, making it react more easily than other states of matter", false]], { "1": "Fluorine and chlorine both have 7 outer electrons. Fewer electrons in total is not the reason — fluorine\'s outer shell is closer to the nucleus, so it attracts an incoming electron more strongly.", "2": "Fluorine does have fewer protons (9) than chlorine (17) — but its outer shell is MUCH closer to those protons. The closeness wins over the fewer-proton effect.", "3": "Chlorine is also a gas — being a gas is not the reason fluorine is more reactive." }),',
     '      V("Why is fluorine more reactive than chlorine?", [["Its outer shell is closer to the nucleus — So it attracts an incoming electron more strongly", true], ["It has fewer electrons, so it is less stable", false], ["It has more protons in its nucleus", false], ["It is a gas, so it reacts more easily", false]], { "1": "Fluorine and chlorine both have 7 outer electrons. The difference is how close the outer shell is to the nucleus.", "2": "Fluorine has fewer protons than chlorine, 9 against 17. Its outer shell is much closer to the nucleus, so the pull is still stronger.", "3": "Chlorine is a gas too, so being a gas is not the reason." }),'),
    # Practice Q3 (iodine + sodium chloride): one reply was about bleaching and starch, beyond this spec point. Replies rewritten; options kept.
    ('      V("Iodine solution is added to sodium chloride solution. What happens?", [["No reaction — iodine is less reactive than chlorine and cannot displace it", true], ["Chlorine gas is released — iodine displaces chloride ions", false], ["A brown precipitate forms — iodine reacts with sodium ions", false], ["The solution turns pale yellow — iodine bleaches the solution", false]], { "1": "A more reactive halogen displaces a less reactive one. Iodine is LESS reactive than chlorine — so iodine cannot displace chloride ions.", "2": "Iodine does not react with sodium ions — and even if it tried to displace chloride, it couldn\'t because iodine is less reactive than chlorine.", "3": "Iodine actually turns starch blue-black — it doesn\'t bleach. Chlorine is the halogen with bleaching properties." }),',
     '      V("Iodine solution is added to sodium chloride solution. What happens?", [["No reaction — Iodine is less reactive than chlorine and cannot displace it", true], ["Chlorine gas is released — iodine displaces chloride ions", false], ["A brown precipitate forms — iodine reacts with sodium ions", false], ["The solution turns orange — bromine forms", false]], { "1": "Iodine is less reactive than chlorine, so it cannot displace chlorine.", "2": "Iodine does not react with sodium ions, and it is too unreactive to displace chlorine.", "3": "Orange would mean bromine had formed. There is no bromide here, and iodine cannot displace chlorine." }),'),
    # Practice Q4 (boiling point trend): the credited option was 101 characters against 23 to 39. Now 50 against 52, 51 and 47, same science (bigger molecules, stronger forces between them).
    ("      Q('Why does the boiling point of the halogens increase down the group?', 'The molecules get larger, so the intermolecular forces increase and more energy is needed to overcome them', [['The covalent bonds get stronger', 'Boiling does not break the covalent bonds; it overcomes the forces between molecules.'], ['The atoms get more reactive', 'Reactivity falls down the group, and it is not what sets the boiling point.'], ['The molecules have more outer electrons', 'Every halogen has seven outer electrons.']]),",
     "      Q('Why does the boiling point of the halogens increase down the group?', 'Bigger molecules have stronger forces between them', [['The covalent bonds inside each molecule get stronger', 'Boiling does not break the covalent bonds. It overcomes the forces between molecules.'], ['The atoms become more reactive going down the group', 'Reactivity decreases down the group, and it does not set the boiling point.'], ['Each atom has more electrons in its outer shell', 'Every halogen atom has seven outer electrons.']]),"),
    # Practice Q5 (hydrogen chloride): the credited option was the longest, and 'A metal' was not a real misconception. Now 37 characters against 39, 28 and 34; 'A mixture' replaces 'A metal'.
    ("      Q('Chlorine reacts with hydrogen to form hydrogen chloride. What type of compound is hydrogen chloride?', 'A covalent molecular compound: a halogen with a non-metal', [['An ionic compound containing chloride ions', 'Halide ions form when halogens react with metals.'], ['A metal', 'Hydrogen chloride is a gas made of molecules.'], ['A salt', 'Salts are the ionic compounds halogens form with metals, such as sodium chloride.']])",
     "      Q('Chlorine reacts with hydrogen to form hydrogen chloride. What type of compound is hydrogen chloride?', 'A covalent compound made of molecules', [['An ionic compound made of chloride ions', 'Halide ions form when halogens react with metals. Hydrogen is a non-metal.'], ['A salt, like sodium chloride', 'Salts such as sodium chloride are the ionic compounds halogens form with metals.'], ['A mixture of hydrogen and chlorine', 'The hydrogen and chlorine are chemically combined, so it is a compound.']]),"),
    # Blind flag B2 (26 Nov): bromine water is already orange-brown, so "turns brown" could be argued true.
    ("['The solution turns brown', 'Brown would be iodine forming. There is no iodide here, and bromine cannot displace chlorine.']",
     "['The solution turns colourless', 'The bromine water keeps its colour. Nothing reacts, because bromine cannot displace chlorine.']"),
]

LESSON = {
    "slug": "group-7",
    "start": {
        "setup": "Fluorine is at the top of Group 7 and iodine is near the bottom.",
        "question": "If you had to guess, which one is more reactive?",
        "options": [
            ("Fluorine",
             "Fluorine. In Group 7, reactivity decreases going down the group, the opposite of "
             "Group 1."),
            ("Iodine",
             "Fluorine. In Group 7, reactivity decreases going down the group, the opposite of "
             "Group 1."),
        ],
        "answer": 0,
    },
    "words": ["halogen", "halide ion", "displacement", "reactivity"],
    "knowledge": [
        {"kind": "card", "title": "The halogens",
         "body": ["The elements in Group 7 are known as the halogens. They have similar reactions "
                  "because they all have seven electrons in their outer shell.",
                  "The halogens are non-metals. They consist of molecules made of pairs of atoms: "
                  "F₂, Cl₂, Br₂ and I₂."]},
        {"kind": "card", "title": "Compounds with metals and non-metals",
         "body": [{"points": [
             "With a metal, a halogen forms an ionic compound. The halide ion has a charge of −1. "
             "Sodium chloride contains Na⁺ and Cl⁻ ions: 2Na + Cl₂ → 2NaCl.",
             "With a non-metal, a halogen forms a covalent compound made of molecules. Hydrogen and "
             "chlorine make hydrogen chloride: H₂ + Cl₂ → 2HCl.",
             "In a compound, the name ends in -ide: chloride, bromide, iodide.",
         ]}]},
        {"kind": "card", "title": "Trends down the group",
         "body": ["The further down the group an element is, the higher its relative molecular "
                  "mass, melting point and boiling point.",
                  {"slot": "fig:halogen-boiling-points"}]},
        {"kind": "reveal", "title": "The halogens down the group",
         "cols": ["Relative molecular mass", "At room temperature"],
         "rows": [
             ("Fluorine, F₂", "38", "Pale yellow gas"),
             ("Chlorine, Cl₂", "71", "Yellow-green gas"),
             ("Bromine, Br₂", "160", "Red-brown liquid"),
             ("Iodine, I₂", "254", "Grey-black solid"),
         ]},
        {"kind": "card", "title": "Reactivity decreases down the group",
         "body": [{"slot": "fig:halogen-pull"},
                  "A halogen atom reacts by gaining one electron to fill its outer shell.",
                  "Going down the group, the outer shell is further from the nucleus. The "
                  "attraction for an incoming electron is weaker, so the electron is gained less "
                  "easily.",
                  "So the reactivity of the elements decreases going down the group."]},
        {"kind": "card", "title": "Displacement reactions",
         "body": ["A more reactive halogen can displace a less reactive halogen from an aqueous "
                  "solution of its salt.",
                  {"points": [
                      "Cl₂ + 2KBr → 2KCl + Br₂. The solution turns orange as bromine forms.",
                      "Cl₂ + 2KI → 2KCl + I₂. The solution turns brown as iodine forms.",
                      "Br₂ + 2KI → 2KBr + I₂. The solution turns brown as iodine forms.",
                  ]},
                  "A less reactive halogen cannot displace a more reactive one, so iodine added to "
                  "potassium chloride gives no reaction."]},
        {"kind": "reveal", "title": "Halogen added to a potassium halide solution",
         "cols": ["Potas\u00adsium chloride", "Potas\u00adsium bromide", "Potas\u00adsium iodide"],
         "rows": [
             ("Chlorine water", "No reaction", "Orange: bromine forms", "Brown: iodine forms"),
             ("Bromine water", "No reaction", "No reaction", "Brown: iodine forms"),
             ("Iodine solution", "No reaction", "No reaction", "No reaction"),
         ]},
        {"kind": "card", "title": "Ionic equations (Higher)", "routes": ["CH", "TH"],
         "body": ["Leave out the metal ions, which do not change:",
                  {"points": ["Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂"]},
                  "Each chlorine molecule gains two electrons to make two chloride ions. Each "
                  "bromide ion loses one electron. The charge is 2− on each side."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Halogens get more reactive down the group, like Group 1.",
              "Halogen reactivity decreases down the group. Gaining an electron gets harder as the "
              "outer shell gets further from the nucleus."),
             ("Chlorine gas is made of Cl atoms.",
              "Chlorine is made of molecules of two atoms, Cl₂."),
             ("Iodine displaces chlorine from sodium chloride.",
              "Iodine is less reactive than chlorine, so nothing happens."),
             ("A halogen with hydrogen makes an ionic compound.",
              "A halogen with a non-metal makes a covalent compound, such as HCl."),
         ]}]},
    ],
    "key_fact": "The halogens have seven electrons in their outer shell and react by gaining one. "
                "Going down Group 7 the outer shell is further from the nucleus, so an electron is "
                "gained less easily and reactivity decreases. A more reactive halogen displaces a "
                "less reactive halogen from an aqueous solution of its salt.",
    "deeper": [
        {"kind": "card", "title": "Predicting astatine",
         "body": ["Astatine is below iodine. From the trends, it should be a dark solid with a higher "
                  "boiling point than iodine, and the least reactive of these halogens."]},
        {"kind": "card", "title": "Why the boiling points rise",
         "body": ["Bigger molecules have stronger forces between the molecules, so more energy is "
                  "needed to separate them."]},
        {"kind": "card", "title": "Oxidation and reduction (Higher)", "routes": ["CH", "TH"],
         "body": ["In Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂, chlorine gains electrons, so it is reduced. The "
                  "bromide ions lose electrons, so they are oxidised."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Predict</strong>: whether a displacement happens, or a property from a trend.",
             "<strong>Explain</strong>: why reactivity falls down the group, using the outer shell "
             "and the nucleus.",
             "<strong>Describe</strong>: the compounds halogens form with metals and with "
             "non-metals.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-11", "logic_edits": LOGIC_EDITS},
}
