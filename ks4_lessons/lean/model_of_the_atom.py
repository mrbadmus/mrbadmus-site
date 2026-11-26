# -*- coding: utf-8 -*-
"""Development of the model of the atom, in the lean shape. Spec table: ks4-model-of-the-atom.md
(AQA 8464 5.1.1.3 / 8462 4.1.1.3, word for word the same, common content with physics; no HT-only
or Chemistry-only lines).

LEGACY (batch 11). The ladder (Ks4Practice, 2·2·2·1) and the practice set (the page's own BANK,
the same five items on every route) stay from the Design page; their fixes are logic_edits below.
Every practice stem is kept byte for byte, so every practice id is kept. The batch-11 header writes
"AQA Chemistry 5.1.1.3 · Combined and Triple"; lean_ks4 rebuilds it per route from
batch_lean.CHEM_EYEBROW (needs the 5.1 eyebrow patch).

logic_edits: the five practice items (one edit each, the whole BANK line, stem unchanged), then:
  6. Rung 2a (what most alpha particles did): the credited option was the longest; the two
     distractors are lengthened, same misconceptions.
  7. Rung 2b (plum pudding against nuclear): the credited option was 126 characters against 53 and
     36. The distractors are now the same two models swapped round (the same length) and "plum
     pudding has no electrons" written at the same length.
"""

LOGIC_EDITS = [
    # Practice Q1 (most passed straight through): replies shouted in capitals and one said the particles missed atoms. Options kept in meaning; replies rewritten.
    ('      V("In Rutherford\'s gold foil experiment, most alpha particles passed straight through the foil. What does this tell us?", [["Atoms are mostly empty space — most particles found no matter to deflect them", true], ["Gold atoms are very large — the particles passed through the gaps between atoms", false], ["Alpha particles are too fast to be deflected", false], ["The plum pudding model was correct — the positive charge is spread out", false]], { "1": "Atomic SIZE explains why particles might miss atoms, not why they pass THROUGH them. The key conclusion is that the atom is mostly empty space internally.", "2": "Alpha particles can be deflected — some WERE deflected at large angles, showing the nucleus exists.", "3": "The plum pudding model predicted only SMALL deflections. The large angle deflections and back-scattering DISPROVED the plum pudding model." }),',
     '      V("In Rutherford\'s gold foil experiment, most alpha particles passed straight through the foil. What does this tell us?", [["Atoms are mostly empty space — Most alpha particles met nothing that could deflect them", true], ["Gold atoms are very large — the particles passed through gaps between the atoms", false], ["Alpha particles move too fast to be deflected by anything", false], ["The plum pudding model was correct — the positive charge is spread out", false]], { "1": "The atoms in gold foil are packed together. The alpha particles passed through the atoms themselves, because an atom is mostly empty space.", "2": "Some alpha particles were deflected, so they can be deflected.", "3": "Plum pudding could not explain the few that bounced back. The nuclear model replaced it." }),'),
    # Practice Q2 (why the nuclear model was accepted): the credited option was the longest by far (93 characters to its label). Shortened to 60; replies rewritten without capitals.
    ('      V("Why did the scientific community accept Rutherford\'s nuclear model over Thomson\'s plum pudding model?", [["The gold foil experiment produced results that could not be explained by the plum pudding model — the new model fitted the evidence", true], ["Rutherford was more famous than Thomson, so his model was believed", false], ["The plum pudding model was proposed before electrons were discovered", false], ["Both models are still equally accepted today", false]], { "1": "Scientific acceptance is based on EVIDENCE, not reputation — the gold foil results clearly contradicted the plum pudding model.", "2": "Thomson\'s plum pudding model was specifically based on and designed to explain the discovery of electrons.", "3": "Rutherford\'s nuclear model replaced the plum pudding model — it is not still equally accepted, though both are discussed historically." }),',
     '      V("Why did the scientific community accept Rutherford\'s nuclear model over Thomson\'s plum pudding model?", [["The scattering results could not be explained by plum pudding — The nuclear model fitted the new evidence", true], ["Rutherford was more famous than Thomson, so his model was believed", false], ["The plum pudding model was proposed before electrons were discovered", false], ["Both models are still equally accepted by scientists today", false]], { "1": "Scientists accept a model because of the evidence, not because of who suggested it.", "2": "The plum pudding model was suggested after the electron was discovered, to include it.", "3": "The nuclear model replaced the plum pudding model, because it explained the scattering results." }),'),
    # Practice Q3 (describe plum pudding): the credited option was the longest. Two distractors now longer, same misconceptions (nuclear model, Bohr).
    ("      Q('Describe the plum pudding model of the atom.', 'A ball of positive charge with negative electrons embedded in it', [['A tiny sphere that cannot be divided', 'That is the model before the electron was discovered.'], ['A small positive nucleus with electrons around it', 'That is the nuclear model, which replaced plum pudding.'], ['Electrons orbiting at specific distances from the nucleus', 'That is Bohr’s adaptation of the nuclear model.']]),",
     "      Q('Describe the plum pudding model of the atom.', 'A ball of positive charge with negative electrons embedded in it', [['A tiny sphere that cannot be divided', 'That is the model before the electron was discovered.'], ['A tiny positive nucleus with the negative electrons moving around it', 'That is the nuclear model, which replaced plum pudding.'], ['Negative electrons orbiting a nucleus at specific distances from it', 'That is Bohr’s adaptation of the nuclear model.']]),"),
    # Practice Q4 (Chadwick): the credited option was the longest (80). Shortened to 55; distractors lengthened to 52 to 62.
    ("      Q('What did the experimental work of James Chadwick provide evidence for, and roughly when?', 'Neutrons in the nucleus, about 20 years after the nucleus became an accepted idea', [['The electron, before the plum pudding model', 'The electron came first, in 1897; Chadwick’s work was later.'], ['The nucleus, from alpha scattering', 'That was the scattering experiment of 1911.'], ['Protons, at the same time as the nucleus', 'Protons came from later experiments on the nuclear charge; neutrons came about 20 years after the nucleus.']]),",
     "      Q('What did the experimental work of James Chadwick provide evidence for, and roughly when?', 'Neutrons, about 20 years after the nucleus was accepted', [['The electron, just before the plum pudding model was suggested', 'The electron came first, in 1897. Chadwick’s work was much later.'], ['The nucleus, from the alpha particle scattering experiment', 'That was the scattering experiment of 1911.'], ['Protons, at the same time as the nucleus was accepted', 'Protons came from later experiments on the charge of the nucleus. Neutrons came about 20 years after the nucleus.']]),"),
    # Practice Q5 (Bohr): the credited option was more than twice the length of any other. Now 51 characters against 48, 56 and 59; a Chadwick distractor replaces 'He removed the nucleus'.
    ("      Q('How did Bohr change the nuclear model?', 'Electrons orbit the nucleus at specific distances; his calculations agreed with experimental observations', [['He removed the nucleus', 'The nucleus stayed; Bohr placed the electrons.'], ['He put electrons inside the nucleus', 'Electrons orbit outside the nucleus.'], ['He spread the positive charge through the atom', 'That is plum pudding, which the scattering experiment had already replaced.']])",
     "      Q('How did Bohr change the nuclear model?', 'He put the electrons in orbits at specific distances', [['He showed that there are neutrons in the nucleus', 'That was Chadwick, about 20 years after the nucleus was accepted.'], ['He put the electrons inside the nucleus with the protons', 'Electrons orbit outside the nucleus.'], ['He spread the positive charge evenly through the whole atom', 'That is plum pudding, which the scattering experiment had already replaced.']]),"),
    ("['They passed straight through the foil', ['They bounced straight back', 'Only a very few did.'], "
     "['They were absorbed by the gold', 'The foil was thin; most went through.']]",
     "['They passed straight through the foil', ['They bounced straight back off the gold foil', "
     "'Only a very few did.'], ['They were absorbed by the gold atoms', 'The foil was thin, and most "
     "went straight through.']]"),
    ("['Plum pudding has no electrons; the nuclear model does', 'Both have electrons.'], "
     "['The nuclear model has no empty space', 'The nuclear model is mostly empty space.']]",
     "['Plum pudding concentrates the mass in a tiny charged nucleus; the nuclear model spreads the "
     "positive charge through the atom', 'That is the wrong way round. Plum pudding has no nucleus.'], "
     "['Plum pudding has no electrons; the nuclear model has electrons around a tiny charged nucleus', "
     "'Both models have electrons. In plum pudding they are embedded in the positive charge.']]"),
    # Parent's fix round (26 Nov): Rung 1 item 2, "The electron" was the longest option. "The neutron"
    # becomes "The alpha particle", a real mix-up (alpha particles were used later, to test the model).
    # Key and index unchanged.
    ("['The neutron', 'Neutrons came last, with Chadwick.']",
     "['The alpha particle', 'Alpha particles were used later, to test the plum pudding model.']"),
]

LESSON = {
    "slug": "model-of-the-atom",
    "start": {
        "setup": "Scientists fired tiny positive particles, called alpha particles, at very thin gold "
                 "foil.",
        "question": "If you had to guess, did most of them bounce back, or go straight through?",
        "options": [
            ("Bounce back",
             "Most went straight through, because most of an atom is empty space. Only a very few "
             "bounced back."),
            ("Go straight through",
             "Most went straight through, because most of an atom is empty space. Only a very few "
             "bounced back."),
        ],
        "answer": 1,
    },
    "words": ["plum pudding model", "nuclear model", "alpha particle", "nucleus"],
    "knowledge": [
        {"kind": "card", "title": "Models change with evidence",
         "body": ["New experimental evidence may lead to a scientific model being changed or "
                  "replaced. The model of the atom changed several times in this way."]},
        {"kind": "card", "title": "Before the electron, and plum pudding",
         "body": ["Before the discovery of the electron, atoms were thought to be tiny spheres that "
                  "could not be divided.",
                  "The discovery of the electron led to the plum pudding model. It suggested that "
                  "the atom is a ball of positive charge with negative electrons embedded in it.",
                  {"slot": "fig:plum-pudding-nuclear"}]},
        {"kind": "card", "title": "The alpha particle scattering experiment",
         "body": ["Positive alpha particles were fired at very thin gold foil.",
                  {"slot": "fig:alpha-scattering"},
                  {"points": [
                      "Most passed straight through, so most of the atom is empty space.",
                      "Some were deflected, so the centre of the atom is charged. Positive alpha "
                      "particles are repelled by it.",
                      "A very few bounced back, so most of the mass is concentrated in a tiny "
                      "space at the centre.",
                  ]}]},
        {"kind": "card", "title": "Why the model changed",
         "body": ["The plum pudding model could not explain these results. Positive charge spread "
                  "through the whole atom could only deflect alpha particles a tiny amount.",
                  "So scientists concluded that the mass of an atom is concentrated at the centre "
                  "(the nucleus) and that the nucleus is charged. This nuclear model replaced the "
                  "plum pudding model."]},
        {"kind": "reveal", "title": "Plum pudding and nuclear model compared",
         "cols": ["Plum pudding", "Nuclear model"],
         "rows": [
             ("Positive charge", "Spread through the whole atom", "In a tiny nucleus at the centre"),
             ("Mass", "Spread through the whole atom", "Concentrated in the nucleus"),
             ("Electrons", "Embedded in the positive charge", "Around the nucleus"),
             ("Empty space", "None", "Most of the atom"),
         ]},
        {"kind": "card", "title": "Bohr, protons and neutrons",
         "body": [{"slot": "fig:bohr-atom"},
                  {"points": [
                      "Niels Bohr adapted the nuclear model by suggesting that electrons orbit the "
                      "nucleus at specific distances. His theoretical calculations agreed with "
                      "experimental observations.",
                      "Later experiments showed that the positive charge of any nucleus could be "
                      "subdivided into a whole number of smaller particles, each with the same "
                      "amount of positive charge. These particles were named protons.",
                      "The experimental work of James Chadwick provided the evidence for neutrons in "
                      "the nucleus. This was about 20 years after the nucleus became an accepted "
                      "scientific idea.",
                  ]}]},
        {"kind": "card", "title": "The models in order",
         "body": [{"points": [
             "1. Tiny spheres that could not be divided.",
             "2. Plum pudding, after the electron was discovered.",
             "3. The nuclear model, after the alpha particle scattering experiment.",
             "4. Bohr's model: electrons orbit at specific distances.",
             "5. Protons in the nucleus.",
             "6. Neutrons in the nucleus, from Chadwick's work.",
         ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Most alpha particles bounced back.",
              "Most went straight through. Only a very few bounced back."),
             ("The plum pudding model has a nucleus.",
              "In plum pudding the positive charge is spread through the whole atom. There is no "
              "nucleus."),
             ("The alpha particles bounced back off electrons.",
              "Electrons have very little mass. The alpha particles were repelled by the small, "
              "positive nucleus."),
             ("The model changed because a famous scientist said so.",
              "It changed because the new evidence could not be explained by the old model."),
         ]}]},
    ],
    "key_fact": "New experimental evidence may lead to a scientific model being changed or replaced. "
                "The alpha particle scattering experiment showed that the mass of an atom is "
                "concentrated in a tiny, charged nucleus, so the nuclear model replaced the plum "
                "pudding model.",
    "deeper": [
        {"kind": "card", "title": "Names and dates",
         "body": [{"points": [
             "1803: John Dalton describes atoms as tiny spheres that cannot be divided.",
             "1897: J. J. Thomson discovers the electron. His plum pudding model follows in 1904.",
             "1909 to 1911: Geiger and Marsden fire alpha particles at gold foil, and Rutherford "
             "explains the results with the nuclear model.",
             "1913: Bohr places the electrons at specific distances.",
             "1932: Chadwick finds the neutron.",
         ]},
                  "You do not need the details of the experiments behind Bohr's model or "
                  "Chadwick's work."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: each model, and the difference between plum pudding and "
             "the nuclear model.",
             "<strong>Explain</strong>: why the model changed. Give the evidence and what the old "
             "model could not explain.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-11", "logic_edits": LOGIC_EDITS},
}
