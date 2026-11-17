# -*- coding: utf-8 -*-
"""Mass changes when a reactant or product is a gas, in the lean shape. Spec table:
ks4-mass-changes-reactions.md.

LEGACY (batch 11). The ladder (Ks4Practice, 2·2·2·1) and the practice set stay from the Design page.
The practice set is the page's own hard-coded bank (baseBank on Foundation routes, htBank on Higher
routes, `(F.H ? htBank : baseBank).map((q) => K.item(q))`); it does not read the subtopic `quiz`
list, so its fixes are logic_edits below and there is no quiz JSON. The open/sealed figure (bFig),
the CFIFA examples and questions, and the two Higher Step widgets are the page's own.

Builder seams (for the lead): this logic writes `const done = F.H ? [...] : [...];`, which
lean_ks4's `const done = \\[...\\];` pattern does not match, and its spec eyebrow is the literal
"AQA Chemistry 5.3.1.3 · Combined and Triple" (the 8464 number on the Triple routes too). Neither
can be fixed by a logic_edit (logic_edits run after the done[] swap; the eyebrow is template).
"""

LOGIC_EDITS = [
    # Practice set Q2 (both banks). Fault: rust is not iron oxide alone, rusting needs water as
    # well as oxygen, so the distractor "Water ... adding extra mass" was arguably right, and
    # 4Fe + 3O₂ → 2Fe₂O₃ is not the rusting reaction. Rusting is not in this spec point.
    # Rewritten on the spec's own example, a metal reacting with oxygen. NEW ID (stem changed).
    ('V("Why does the mass of iron increase when it rusts in air?", [["Oxygen from the air '
     'combines with the iron — the oxygen adds to the mass of the solid product (iron oxide)", '
     'true], ["Water from humidity condenses on the rust — adding extra mass", false], ["The iron '
     'becomes denser as it rusts — same volume but more mass", false], ["Iron oxide has more atoms '
     'per formula unit than iron", false]], { "1": "Humidity can contribute, but the primary '
     'reason is oxygen being ABSORBED from the air. The reaction is 4Fe + 3O₂ → 2Fe₂O₃ — the '
     'oxygen becomes part of the solid.", "2": "Density changes do not increase total mass — '
     'mass = density × volume. If both change proportionally, mass stays the same. More mass '
     'comes from more matter (oxygen absorbed).", "3": "Atom count per formula unit is '
     'irrelevant — it is the MASS of oxygen absorbed from air that increases the total mass." }),',
     "Q('Why does the mass of magnesium ribbon increase when it burns in air?', 'Oxygen from "
     "the air joins the magnesium', [['Heat is added, and heat has mass', 'Heat is energy, not "
     "matter. Oxygen joins the solid, so the mass goes up.'], ['Hot atoms are heavier than cold "
     "atoms', 'Heating does not change the mass of an atom. Oxygen joins the solid.'], ['The "
     "magnesium gives off a gas', 'A gas given off would make the mass go down.']]),"),
    # Practice set Q4 (sealed flask), stem kept. The credited option was visibly the longest.
    # KEY CHANGE (options reworded).
    ("'It stays the same: the gas is made but cannot leave', [['It falls, because gas is made', "
     "'Gas is made, but it is trapped and still weighed.'], ['It rises, because gas is made', "
     "'Making a gas inside a sealed flask adds nothing from outside.'], ['It falls, then rises', "
     "'Nothing enters or leaves a sealed flask.']]",
     "'It stays the same: no gas can leave', [['It falls, because a gas is made', 'Gas is made, "
     "but it is trapped and still weighed.'], ['It rises, because a gas is made', 'Making a gas "
     "inside a sealed flask adds nothing from outside.'], ['It falls at first, then rises again', "
     "'Nothing enters or leaves a sealed flask.']]"),
    # Practice set Q5 (copper heated in air, Foundation bank), stem kept. The credited option was
    # visibly the longest (95 characters against 28 to 40). KEY CHANGE.
    ("'Oxygen particles from the air bond to the copper atoms and become part of the solid copper "
     "oxide'",
     "'Oxygen particles bond to the copper atoms'"),
    # Rung 2 (both calcs): the unit chips offered "mol" and one Convert choice was "g to mol" on
    # every route. Moles are Higher only (8464 5.3.2.1 / 8462 4.3.2.1). Same answers, same
    # correct choices and units.
    ("0, 2.2, 'g', ['g', 'kg', 'mol']", "0, 2.2, 'g', ['g', 'kg', 'cm³']"),
    ("1, 2, 'g', ['g', 'kg', 'mol']", "1, 2, 'g', ['g', 'kg', 'cm³']"),
    ("'Convert g to mol'", "'Convert kg to g'"),
    # Examiner SHOULD FIX (13 Nov), exactly as in EXAMINER.md / _exam/proposed.py. Practice Q1 feedback (both banks): dashes, capitals, 'combusting'. Stem and options kept.
    ('{ "1": "Oxygen is not absorbed here — CaCO₃ is decomposing, not combusting. A gas (CO₂) is PRODUCED and escapes.", "2": "Conservation of mass applies to the TOTAL system. In an open container, the mass of the CONTAINER contents decreases because CO₂ leaves. Conservation is still upheld if you include the escaped CO₂.", "3": "There is no initial increase phase — CO₂ is produced and escapes from the start of heating." }',
     '{ "1": "Nothing joins the solid here. Calcium carbonate breaks down and carbon dioxide gas escapes.", "2": "Mass is conserved, but the crucible is open. The carbon dioxide escapes and is no longer weighed.", "3": "The mass never rises. Carbon dioxide escapes from the start of heating." }'),
    # Examiner SHOULD FIX (13 Nov), exactly as in EXAMINER.md / _exam/proposed.py. Kilogram readings to 3 s.f. (rung 2 calc 2, CFIFA example 2, CFIFA Q2). Answers unchanged.
    ('has a mass of 0.3 kg before and 298 g after.',
     'has a mass of 0.300 kg before and 298 g after.'),
    ('has a mass of 0.5 kg at the start and 487 g at the end',
     'has a mass of 0.500 kg at the start and 487 g at the end'),
    ('has a mass of 0.2 kg before and 196 g after',
     'has a mass of 0.200 kg before and 196 g after'),
    # Blind fix (b): practice Q4 leaned on Q3 ('The same reaction'). Reaction named. Both banks. NEW ID.
    ("Q('The same reaction is run in a sealed flask. What happens to the balance reading?'",
     "Q('Marble chips react with acid in a sealed flask. What happens to the balance reading?'"),
    # Lead (13 Nov), after blind round 2: every kilogram reading on these three lines to 3 s.f. (the chips,
    # feedback and worked lines too), and 'open flask' in the two mass-loss stems (the sealed-flask practice
    # question gives the opposite answer). Whole-line pairs, so each old text is unique.
    ("CALC('A flask of marble chips and acid has a mass of 0.300 kg before and 298 g after. Calculate the mass of carbon dioxide lost.', ['Nothing to convert', 'Convert 0.3 kg to 300 g', 'Convert 0.3 kg to 30 g'], 1, 2, 'g', ['g', 'kg', 'cm³'], '0.3 kg = 300 g; 300 − 298 = 2 g.', 'Match the units first: 0.3 kg is 300 g.', ['C · 0.3 kg = 300 g', 'F · mass of gas = before − after', 'I · mass of gas = 300 − 298', 'F · mass of gas = 2', 'A · 2 g'])",
     "CALC('An open flask of marble chips and acid has a mass of 0.300 kg before and 298 g after. Calculate the mass of carbon dioxide lost.', ['Nothing to convert', 'Convert 0.300 kg to 300 g', 'Convert 0.300 kg to 30 g'], 1, 2, 'g', ['g', 'kg', 'cm³'], '0.300 kg = 300 g; 300 − 298 = 2 g.', 'Match the units first: 0.300 kg is 300 g.', ['C · 0.300 kg = 300 g', 'F · mass of gas = before − after', 'I · mass of gas = 300 − 298', 'F · mass of gas = 2', 'A · 2 g'])"),
    ("{ tab: 'Convert kg to g', next: 'Now one where the reading rises.', head: 'A beaker of acid and marble chips has a mass of 0.500 kg at the start and 487 g at the end. Calculate the mass of carbon dioxide lost.', steps: CFL('0.5 kg = 500 g', 'mass of gas = mass before − mass after', 'mass of gas = 500 − 487', 'mass of gas = 13', '13 g of carbon dioxide', 'Both readings must be in the same unit before subtracting.') },",
     "{ tab: 'Convert kg to g', next: 'Now one where the reading rises.', head: 'A beaker of acid and marble chips has a mass of 0.500 kg at the start and 487 g at the end. Calculate the mass of carbon dioxide lost.', steps: CFL('0.500 kg = 500 g', 'mass of gas = mass before − mass after', 'mass of gas = 500 − 487', 'mass of gas = 13', '13 g of carbon dioxide', 'Both readings must be in the same unit before subtracting.') },"),
    ("{ tab: 'Question 2', id: 'mc-q2', head: 'A flask of marble chips and acid has a mass of 0.200 kg before and 196 g after. Calculate the mass of carbon dioxide lost.', close: '0.2 − 196 is meaningless: 0.2 kg is 200 g.', steps: CFQ('0.2 kg = 200 g', 'mass of gas = mass before − mass after', 'mass of gas = 200 − 196', 'mass of gas = 4', '4 g', 'kg to g?') }",
     "{ tab: 'Question 2', id: 'mc-q2', head: 'An open flask of marble chips and acid has a mass of 0.200 kg before and 196 g after. Calculate the mass of carbon dioxide lost.', close: '0.200 − 196 is meaningless: 0.200 kg is 200 g.', steps: CFQ('0.200 kg = 200 g', 'mass of gas = mass before − mass after', 'mass of gas = 200 − 196', 'mass of gas = 4', '4 g', 'kg to g?') }"),
]

LESSON = {
    "slug": "mass-changes-reactions",
    "start": {
        "setup": "Marble chips react with hydrochloric acid in an open flask on a balance. The "
                 "mixture fizzes.",
        "question": "If you had to guess, does the reading go down or stay the same?",
        "options": [
            ("It goes down",
             "It goes down. The fizz is carbon dioxide gas, and it escapes from the open flask."),
            ("It stays the same",
             "It goes down. The fizz is carbon dioxide gas, and it escapes from the open flask."),
        ],
        "answer": 0,
    },
    "words": ["non-enclosed system", "thermal decomposition", "particle model"],
    "knowledge": [
        {"kind": "card", "title": "Mass is still conserved",
         "body": ["Some reactions may appear to involve a change in mass but this can usually be "
                  "explained because a reactant or product is a gas and its mass has not been "
                  "taken into account.",
                  "No atoms are lost or made. A gas has left the container, or joined the "
                  "product, without being weighed."]},
        {"kind": "card", "title": "When the reading falls",
         "body": ["A product is a gas, and it escapes from an open container.",
                  "In the thermal decomposition of a metal carbonate, carbon dioxide is produced "
                  "and escapes into the atmosphere. The metal oxide is the only solid product.",
                  "CaCO₃(s) → CaO(s) + CO₂(g)",
                  "Marble chips and acid in an open flask lose mass the same way:",
                  "CaCO₃(s) + 2HCl(aq) → CaCl₂(aq) + H₂O(l) + CO₂(g)",
                  {"slot": "fig:open-sealed-flasks"}]},
        {"kind": "card", "title": "When the reading rises",
         "body": ["A metal reacts with oxygen from the air.",
                  "The mass of the oxide produced is greater than the mass of the metal, because "
                  "it now includes the oxygen.",
                  "2Mg(s) + O₂(g) → 2MgO(s)"]},
        {"kind": "card", "title": "When the reading stays the same",
         "body": ["In a sealed flask, no gas can get in or out.",
                  "Everything that was weighed at the start is still weighed at the end, so the "
                  "reading does not change."]},
        {"kind": "reveal", "title": "Falls, rises or stays the same",
         "cols": ["Reading", "Why"],
         "rows": [
             ("Marble chips and acid in an open flask", "Falls", "Carbon dioxide escapes"),
             ("Zinc and dilute sulfuric acid in an open tube", "Falls", "Hydrogen escapes"),
             ("Magnesium heated in an open crucible", "Rises",
              "Oxygen from the air joins the solid"),
             ("Calcium carbonate heated in a sealed tube", "Stays the same",
              "The carbon dioxide cannot escape"),
         ]},
        {"kind": "card", "title": "Explaining it with particles",
         "body": [{"points": [
             "Reading falls: gas particles move about randomly and spread out of the open "
             "container. They take their mass with them, so the balance no longer weighs them.",
             "Reading rises: oxygen particles from the air bond to the metal atoms and become part "
             "of the solid oxide. Mass that was not on the balance now is.",
         ]}]},
        {"kind": "card", "title": "Use the balanced equation",
         "body": ["The state symbols tell you which substances are gases.",
                  "CuCO₃(s) → CuO(s) + CO₂(g)",
                  "The carbon dioxide is a gas. Heated in an open tube, it escapes, so the mass "
                  "of solid goes down.",
                  "In 2Mg(s) + O₂(g) → 2MgO(s) the gas is a reactant. The oxygen comes from the "
                  "air, so it was not weighed at the start. It joins the solid product, so the "
                  "mass of solid goes up."]},
        {"kind": "card", "title": "The mass of gas",
         "body": ["mass of gas lost = mass before − mass after",
                  "mass of gas gained = mass after − mass before",
                  "Both readings must be in the same unit before you subtract.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Burning destroys some of the magnesium, so the ash weighs less.",
              "Oxygen joins the magnesium, so the magnesium oxide weighs more."),
             ("The reading falls because mass is lost in the reaction.",
              "No atoms are lost. A gas escaped and is no longer being weighed."),
             ("A sealed flask loses mass when a gas is made.",
              "The gas cannot leave a sealed flask, so the reading stays the same."),
         ]}]},
    ],
    "key_fact": "Some reactions may appear to involve a change in mass because a reactant or "
                "product is a gas and its mass has not been taken into account. A gas that "
                "escapes from an open container lowers the reading, and oxygen from the air that "
                "joins a metal raises it.",
    "deeper": [
        {"kind": "card", "title": "Predicting the mass gained", "routes": ["CH", "TH"],
         "body": ["On Higher you can work out the mass a metal gains from the balanced equation, "
                  "using moles. Step 1 finds the moles of metal. Step 2 uses the ratio in the "
                  "equation. Step 3 turns moles of oxygen back into a mass.",
                  {"slot": "steps-worked"},
                  {"slot": "steps-attempt"}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Predict</strong>: say whether the reading rises, falls or stays the same.",
             "<strong>Explain</strong>: name the gas, say whether it left or joined, and use "
             "particles.",
             "<strong>Calculate</strong>: subtract the readings, in the same unit, and give the "
             "unit.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-11", "logic_edits": LOGIC_EDITS},
}
