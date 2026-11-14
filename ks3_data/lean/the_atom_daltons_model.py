# -*- coding: utf-8 -*-
"""The atom: Dalton's model, in the lean shape. Spec table: docs/lessons/wave1/ks3-the-atom-daltons-model.md."""

LESSON = {
    "slug": "the-atom-daltons-model",
    "start": {
        "setup": "For centuries, alchemists tried to turn lead into gold.",
        "question": "If you had to guess, could modern furnaces, acids and mixing turn lead into gold?",
        "options": [
            ("Yes, with modern kit", "No, however good the kit. Chemical reactions only rearrange atoms. They cannot turn lead atoms into gold atoms."),
            ("No, however good the kit", "No, however good the kit. Chemical reactions only rearrange atoms. They cannot turn lead atoms into gold atoms."),
        ],
        "answer": 1,
    },
    "words": ["atom", "element", "model", "chemical reaction"],
    "word_defs": {
        "atom": "The smallest particle of an element.",
        "element": "A substance made of only one kind of atom.",
        "model": "A simple picture of how something works. Scientists use it to explain and predict.",
        "chemical reaction": "A change that rearranges atoms to make new substances.",
    },
    "knowledge": [
        {"kind": "card", "title": "What an atom is",
         "body": ["Everything is made of tiny particles called atoms.",
                  "An atom is the smallest particle of an element.",
                  "Each element has its own kind of atom.",
                  {"figure": "c2-lead-gold-atoms"},
                  "Atoms are far too small to see, even with a light microscope."]},
        {"kind": "card", "title": "Dalton's model",
         "body": ["John Dalton put forward his model of the atom over 200 years ago.",
                  "His model says:",
                  {"points": ["Everything is made of atoms.",
                              "All atoms of one element are the same. They differ from the atoms of other elements.",
                              "Atoms cannot be split, made or destroyed.",
                              "Atoms join in simple whole-number ratios to make compounds.",
                              "A chemical reaction rearranges atoms. It never changes one kind into another."]}]},
        {"kind": "card", "title": "What the model explains",
         "body": [{"points": ["Why mass stays the same in a reaction. The atoms are only rearranged.",
                              "Why a compound always has the same make-up. Pure water always has the same ratio "
                              "of hydrogen to oxygen.",
                              "Why lead never turned into gold."]},
                  "Alchemists worked with furnaces and acids.",
                  "They tried for centuries and always failed. That is evidence for the model.",
                  "If anyone made gold from lead by a chemical reaction, the model would be wrong."]},
        {"kind": "card", "title": "Where the model was wrong",
         "body": ["Later scientists found that two of Dalton's claims were wrong:",
                  {"points": ["Atoms can be split. They contain even smaller particles, such as electrons.",
                              "Atoms of one element can have different masses."]},
                  "Radioactive atoms can change into atoms of another element. That is not a chemical reaction.",
                  "No chemical reaction changes one kind of atom into another."]},
        {"kind": "card", "title": "Why a wrong model is still used",
         "body": ["A model is judged by what it explains.",
                  "Dalton's model still explains reactions, conservation of mass and fixed ratios.",
                  "It cannot explain electrons, radioactivity, or atoms of one element with different masses.",
                  "So the model is kept, with a known limit."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A copper atom is orange, shiny and conducts electricity.",
              "Those properties come from many atoms together. One atom does not have them."),
             ("A model with one wrong part should be thrown away.",
              "A model is kept while it explains what it is used for."),
             ("Heating or mixing can turn one element into another.",
              "Chemical reactions only rearrange atoms. The kinds of atom stay the same."),
         ]}]},
    ],
    "key_fact": "An atom is the smallest particle of an element. Each element has its own kind of atom. "
                "Chemical reactions rearrange atoms, but never change one kind into another.",
    "deeper": [
        {"kind": "card", "title": "How small is an atom",
         "body": ["An atom has a radius of about 0.1 nanometres.",
                  "A nanometre is one billionth of a metre."]},
        {"kind": "card", "title": "Inside the atom",
         "body": ["At GCSE you meet a newer model of the atom.",
                  "It has a tiny nucleus in the middle, with electrons around it."]},
    ],
    "try": None,
    "ladder_stem": {
        "recall": "Which is the best definition of an atom?",
        "apply": "Two of Dalton's claims are now known to be wrong. Chemists still use his model to "
                 "explain what happens to atoms in ordinary chemical reactions. Which is the best reason?",
        "explain": "Alchemists never turned lead into gold by heating, burning or mixing. Explain why this "
                   "is evidence for Dalton's model. Say what alchemists would have needed to do to prove "
                   "it wrong.",
        "produce": "A student says, \"Dalton was wrong that atoms cannot be split. So throw his model "
                   "away.\" Reply to the student. Give one thing the model still explains, and one thing "
                   "it cannot.",
    },
    "ladder_ticks": [
        ["Says that fifteen hundred years of careful failure is evidence, not just an absence of success.",
         "Says centuries of careful failure count as evidence for the model."],
        ["Names something Dalton’s model still explains — fixed proportions, conservation of mass, or "
         "why alchemy failed.",
         "Names one thing the model explains: fixed ratios, conservation of mass, or alchemy failing."],
        ["Names something it cannot explain — electricity from atoms, radioactivity, or atoms of one "
         "element with different masses.",
         "Names one thing it cannot explain: electrons, radioactivity, or one element's atoms having different masses."],
    ],
    "figures": [
        {"id": "c2-lead-gold-atoms", "kind": "diagram", "status": "drawn",
         "art": "particle-boxes",
         "title": "Lead atoms and gold atoms",
         "desc": "Two boxes side by side. The left box, labelled Lead, is filled with identical grey "
                 "circles marked Pb, packed in touching rows. The right box, labelled Gold, is filled "
                 "with identical yellow circles marked Au, slightly smaller, packed in touching rows.",
         "caption": "Lead is only lead atoms. Gold is only gold atoms.",
         "data": {"boxes": [
             {"label": "Lead", "layout": "grid", "rows": 4, "cols": 5, "atom": "Pb"},
             {"label": "Gold", "layout": "grid", "rows": 4, "cols": 5, "atom": "Au"},
         ]}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "A water particle is more than one atom. An atom is the smallest particle of an element.",
            1: "Liquids and gases are made of atoms too. Being small does not make it an atom.",
            2: "A virus is too small for a light microscope, and it is not an atom.",
        },
        "apply": {
            0: "Chemists still use it. It gives the right answers for reactions.",
            2: "It has been replaced for some questions. For reactions, it still works.",
            3: "That is not why. The model is kept because it still works for reactions.",
        },
    },
}
