# -*- coding: utf-8 -*-
"""Percentage yield, in the lean shape. Spec table: ks4-percentage-yield.md.

LEGACY (batch 2, Ks4Ladder). Routes TF and TH only (8462 4.3.3.1, chemistry only; the
theoretical-mass bullet is HT only). The ladder stays from the Design page; its Rung 2 is
already route-aware (a percentage-yield calculation on TF, a theoretical-mass calculation on TH),
so Foundation never sees HT content. The practice set reads the route's `quiz` list
(`K.bank(slug, R.route)`), so its five questions per route are in quiz-percentage-yield.json.

The `cfifa` slot shows the legacy page's own cfExamples and cfQuestions. The legacy page also
had a Higher-only Ks4Cfifa (htExamples / htQuestions) in a section the lean page drops. The
logic_edits below append those two Higher worked examples (copied, with one note corrected) and
question py-h2 (id kept) to the `cfifa` slot on TH only, so TH keeps worked examples of the HT
statement. TF is unchanged.
"""

_HT_DEFS = """const htEx = [
      { tab: 'Higher · from a reactant mass', head: 'Calcium carbonate decomposes: CaCO₃ → CaO + CO₂. A student heats 12.0 g of CaCO₃ and obtains 5.6 g of CaO. Calculate the percentage yield. (Mr: CaCO₃ = 100, CaO = 56)', next: 'Now one in kilograms.', steps: steps5([
        'Nothing to convert: both masses are in g.',
        'n = m ÷ Mr, then the mole ratio, then m = n × Mr; % yield = (actual ÷ theoretical) × 100',
        'n(CaCO₃) = 12.0 ÷ 100 = 0.120 mol',
        '1 : 1 ratio, so n(CaO) = 0.120 mol; theoretical mass = 0.120 × 56 = 6.72 g; % yield = (5.6 ÷ 6.72) × 100',
        'Percentage yield = 83.3% (83%)']) },
      { tab: 'Higher · convert first', head: 'A kiln heats 1.00 kg of CaCO₃ and collects 476 g of CaO. Calculate the percentage yield. (Mr: CaCO₃ = 100, CaO = 56)', next: 'Now yours, below.', steps: [
        { letter: 'C', label: 'Convert', line: '1.00 kg × 1000 = 1000 g', note: 'The mass of one mole in grams equals Mr, so the mass must be in grams.' },
        { letter: 'F', label: 'Formula', line: 'n = m ÷ Mr, then the mole ratio, then m = n × Mr; % yield = (actual ÷ theoretical) × 100', note: '' },
        { letter: 'I', label: 'Insert', line: 'n(CaCO₃) = 1000 ÷ 100 = 10.0 mol', note: '' },
        { letter: 'F', label: 'Fine-tune', line: '1 : 1 ratio, so n(CaO) = 10.0 mol; theoretical mass = 10.0 × 56 = 560 g; % yield = (476 ÷ 560) × 100', note: '' },
        { letter: 'A', label: 'Answer', line: 'Percentage yield = 85%', note: 'Unconverted, the theoretical mass comes out as 0.56 g and the yield as 85 000%.' } ] }
    ];
    const htQ = [
      { tab: 'Question 3', id: 'py-h2', head: 'Fe₂O₃ + 3CO → 2Fe + 3CO₂. 16 kg of iron(III) oxide produces 9.8 kg of iron. Calculate the percentage yield. (Mr Fe₂O₃ = 160, Ar Fe = 56)', close: 'Miss the 1 : 2 ratio and you get 175%: an impossible yield that tells you to check.',
        steps: q5(['16 kg × 1000 = 16 000 g; 9.8 kg × 1000 = 9800 g', 'n = m ÷ Mr, then the mole ratio, then m = n × Ar; % yield = (actual ÷ theoretical) × 100', 'n(Fe₂O₃) = 16 000 ÷ 160 = 100 mol', '1 : 2 ratio, so n(Fe) = 200 mol; theoretical mass = 200 × 56 = 11 200 g; % yield = (9800 ÷ 11 200) × 100', 'Percentage yield = 87.5%'], phHT) }
    ];
    const keyBase = ["""

LOGIC_EDITS = [
    # Rung 1 (percentage-yield#r1): the credited option was visibly the longest (65 against 60).
    # Trimmed to 58, the spec's own idea ("lost when it is separated"). Position and index kept.
    ("{ text: 'Some product is left behind when it is separated from the mixture', correct: true",
     "{ text: 'Some product is lost when it is separated from the mixture', correct: true"),
    # Higher worked examples into the cfifa slot on TH (see the docstring).
    ("const keyBase = [", _HT_DEFS),
    ("      ] : [],\n      cfQuestions: R.isHigher ? cfQH : [",
     "      ].concat(R.isHigher ? htEx : []) : [],\n      cfQuestions: R.isHigher ? cfQH.concat(htQ) : ["),
    # The last standard example said "Your turn below"; on TH two more examples now follow it.
    ("next: 'Convert first, then the same four lines. Your turn below.'",
     "next: R.isHigher ? 'Now the theoretical mass from a reactant.' : 'Convert first, then the same four lines. Your turn below.'"),
    # Examiner SHOULD FIX (13 Nov), exactly as in EXAMINER.md / _exam/proposed.py. Foundation rung 2 unit chips: no 'mol'.
    ("unit: '%', units: ['%', 'g', 'kg', 'mol'],",
     "unit: '%', units: ['%', 'g', 'kg', 'no unit'],"),
]

LESSON = {
    "slug": "percentage-yield",
    "start": {
        "setup": "From the balanced equation, a student's reactants can make 8.0 g of copper "
                 "sulfate at most. The student collects 6.2 g.",
        "question": "If you had to guess, was the missing 1.8 g destroyed in the reaction, or lost "
                    "along the way?",
        "options": [
            ("Destroyed in the reaction",
             "Lost along the way. No atoms are destroyed in a reaction. Some copper sulfate stayed "
             "on the filter paper, on the glassware and in the solution."),
            ("Lost along the way",
             "Lost along the way. No atoms are destroyed in a reaction. Some copper sulfate stayed "
             "on the filter paper, on the glassware and in the solution."),
        ],
        "answer": 1,
    },
    "words": ["yield", "percentage yield", "maximum theoretical mass", "reversible reaction"],
    "knowledge": [
        {"kind": "card", "title": "Why you get less than you calculated",
         "body": ["Even though no atoms are gained or lost in a chemical reaction, it is not "
                  "always possible to obtain the calculated amount of a product because:",
                  {"points": ["the reaction may not go to completion because it is reversible",
                              "some of the product may be lost when it is separated from the "
                              "reaction mixture",
                              "some of the reactants may react in ways different to the expected "
                              "reaction."]}]},
        {"kind": "card", "title": "Yield and percentage yield",
         "body": ["The amount of a product obtained is known as the yield.",
                  "When compared with the maximum theoretical amount as a percentage, it is called "
                  "the percentage yield."]},
        {"kind": "card", "title": "The equation",
         "body": ["% yield = (mass of product actually made ÷ maximum theoretical mass of "
                  "product) × 100",
                  {"points": ["Put both masses in the same unit before you divide.",
                              "The mass actually made goes on top.",
                              "The answer is a percentage."]},
                  "You need to remember this equation."]},
        {"kind": "card", "title": "Theoretical mass from a reactant", "routes": ["TH"],
         "body": ["On the Higher paper you may have to calculate the maximum theoretical mass of "
                  "product from a given mass of reactant and the balanced equation.",
                  {"points": ["Step 1: moles of reactant: n = m ÷ M<sub>r</sub>.",
                              "Step 2: use the balancing numbers to find the moles of product.",
                              "Step 3: maximum theoretical mass of product: m = n × M<sub>r</sub>.",
                              "Then use the percentage yield equation."]},
                  "If one reactant is in excess, start from the limiting reactant."]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "A yield over 100%",
         "body": ["A pure, dry product can never have more mass than the maximum theoretical mass.",
                  "A yield over 100% means something else was weighed with the product, such as "
                  "water in crystals that were not fully dried, or impurities."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("% yield = maximum theoretical mass ÷ mass actually made × 100",
              "The mass actually made goes on top."),
             ("The yield is low because some atoms were destroyed.",
              "No atoms are gained or lost. Product is lost, the reaction is reversible, or "
              "reactants react in other ways."),
             ("A catalyst gives a higher yield.",
              "A catalyst speeds up a reaction. It does not change the maximum mass of product."),
             ("2.5 kg and 1900 g go straight into the equation.",
              "Convert first: 2.5 kg = 2500 g."),
         ]}]},
    ],
    "key_fact": "% yield = (mass of product actually made ÷ maximum theoretical mass of product) × "
                "100. It is less than 100% because the reaction may be reversible, some product is "
                "lost when it is separated from the reaction mixture, or some reactants react in "
                "different ways.",
    "deeper": [
        {"kind": "card", "title": "Why a high yield matters",
         "body": ["A low yield wastes raw materials, so the product costs more to make.",
                  "Less waste is better for the environment and makes raw materials last longer."]},
        {"kind": "card", "title": "Choosing a reaction pathway", "routes": ["TH"],
         "body": ["Chemists choose how to make a product using the yield together with the atom "
                  "economy, the rate, the equilibrium position and how useful any by-products are.",
                  "There is more on this in Atom economy."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: convert, write the formula, insert, work it out, and "
             "give the answer with the % sign.",
             "<strong>Give</strong>: a reason in a few words.",
             "<strong>Suggest</strong>: apply what you know to the practical in the question.",
             "<strong>Explain</strong>: link a cause to its effect on the mass collected.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
}
