# -*- coding: utf-8 -*-
"""Changes of state, in the lean shape. New record, no legacy page (it replaces the old
generate_site_v5 page). Spec table: ks4-changes-of-state.md (AQA 8464 6.3.1.2 / 8463 4.3.1.2, word
for word the same). No HT-only or physics-only line, no equation, no required practical. Every
route gets the same lesson.

AQA names six changes: melt, freeze, boil, evaporate, condense, sublimate. The old page's
"deposition" (gas straight to solid) is not in the spec and is left out. What the energy does to
the particles during a change of state is taught in internal-energy and specific-latent-heat; this
lesson keeps to the names, the conservation of mass and physical against chemical change.

The practice set reads the route's `quiz` list (K.bank): five per route, the same on every route,
both old stems kept word for word (so their ks4q: ids survive)."""

LESSON = {
    "slug": "changes-of-state",
    "start": {
        "setup": "Water boils in a pan. The steam condenses on a cold window as drops of water.",
        "question": "If you had to guess, is boiling a physical change or a chemical change?",
        "options": [
            ("A physical change",
             "A physical change. The steam is still water. When it condenses, it turns back into "
             "water with all the same properties."),
            ("A chemical change",
             "A physical change. The steam is still water. When it condenses, it turns back into "
             "water with all the same properties."),
        ],
        "answer": 0,
    },
    "words": ["change of state", "physical change", "chemical change", "sublimate"],
    "knowledge": [
        {"kind": "card", "title": "States of matter",
         "body": [{"slot": "fig:particle-states"},
                  "A substance can be a solid, a liquid or a gas.",
                  "In a change of state, the particles stay the same particles. Only how they are "
                  "arranged and how they move changes."]},
        {"kind": "card", "title": "The changes of state",
         "body": [{"slot": "fig:state-changes"},
                  {"points": [
                      "Melting, boiling, evaporating and sublimating happen when energy is "
                      "transferred to the substance.",
                      "Freezing and condensing happen when energy is transferred away from the "
                      "substance.",
                      "Sublimating is a change straight from a solid to a gas. Solid carbon "
                      "dioxide (dry ice) sublimates at room temperature.",
                  ]}]},
        {"kind": "card", "title": "Mass is conserved",
         "body": ["When a substance changes state, mass is conserved.",
                  "No particles are made or destroyed, and each particle keeps its mass. They "
                  "only move closer together or further apart.",
                  {"points": [
                      "100 g of ice melts to give 100 g of water.",
                      "In an open pan, water evaporates and the vapour escapes into the air. The "
                      "water left in the pan has less mass, but the water plus the vapour still "
                      "has the same mass as before.",
                  ]}]},
        {"kind": "card", "title": "Physical, not chemical",
         "body": ["Changes of state are physical changes. They differ from chemical changes "
                  "because the material recovers its original properties if the change is "
                  "reversed.",
                  {"points": [
                      "Melt some wax, then let it cool. You get solid wax again, with the same "
                      "properties.",
                      "Burn paper and you get ash and gases. Cooling them does not give the paper "
                      "back: new substances have formed. That is a chemical change.",
                  ]}]},
        {"kind": "reveal", "title": "Physical or chemical",
         "cols": ["Type of change"],
         "rows": [
             ("Ice melting", "Physical"),
             ("Steam condensing on a window", "Physical"),
             ("Dry ice sublimating", "Physical"),
             ("Wood burning", "Chemical"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Ice has more mass than the water it melts into.",
              "The mass is the same. Ice takes up more volume, so it is less dense."),
             ("The particles get bigger when a solid melts.",
              "The particles stay the same size. They move further apart."),
             ("Boiling water turns it into a new substance.",
              "Steam is still water. A change of state is a physical change."),
         ]}]},
    ],
    "key_fact": "When a substance changes state (melts, freezes, boils, evaporates, condenses or "
                "sublimates), mass is conserved. Changes of state are physical changes: if the "
                "change is reversed, the material recovers its original properties.",
    "deeper": [
        {"kind": "card", "title": "Boiling and evaporating",
         "body": ["Both turn a liquid into a gas. Boiling happens all through the liquid, at its "
                  "boiling point. Evaporating happens only at the surface, and can happen below "
                  "the boiling point."]},
        {"kind": "card", "title": "Links to other lessons",
         "body": [{"points": [
             "Internal energy: what the energy does to the particles during a change of state.",
             "Specific latent heat: how much energy a change of state needs.",
             "Density: the volume changes when the state changes, but the mass does not.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: say what happens to the particles, in order.",
             "<strong>Explain</strong>: give the reason, for example why the mass stays the same "
             "or why the change is physical.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the change of state from a solid straight to a gas.",
             "why": "A solid turning straight into a gas sublimates.",
             "options": [
                 {"text": "Evaporating", "correct": False,
                  "reply": "Evaporating is a liquid turning into a gas."},
                 {"text": "Sublimating", "correct": True},
                 {"text": "Melting", "correct": False,
                  "reply": "Melting is a solid turning into a liquid."},
             ]},
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the change of state from a gas to a liquid.",
             "why": "A gas turning into a liquid condenses.",
             "options": [
                 {"text": "Freezing", "correct": False,
                  "reply": "Freezing is a liquid turning into a solid."},
                 {"text": "Evaporating", "correct": False,
                  "reply": "Evaporating goes the other way: liquid to gas."},
                 {"text": "Condensing", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Use", "marks": 2,
             "prompt": "A 20 g piece of dry ice (solid carbon dioxide) is sealed in a bag. It "
                       "turns straight into a gas. Which statement is correct?",
             "why": "Solid straight to gas is sublimating. Nothing leaves the sealed bag, so the "
                    "mass is conserved.",
             "options": [
                 {"text": "It sublimates, and the mass in the bag stays 20 g", "correct": True},
                 {"text": "It evaporates, and the mass in the bag goes down", "correct": False,
                  "reply": "Evaporating starts from a liquid. Here a solid becomes a gas, and "
                           "the mass stays 20 g."},
                 {"text": "It sublimates, and the mass in the bag drops to 0 g", "correct": False,
                  "reply": "A gas has mass. Nothing leaves the bag, so the mass stays 20 g."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 2,
             "prompt": "Which change gives back the material with its original properties when "
                       "it is reversed?",
             "why": "Condensing is a change of state. Boil the water again and it becomes steam "
                    "again, so it is a physical change.",
             "options": [
                 {"text": "Paper burning to ash", "correct": False,
                  "reply": "New substances form, and cooling them does not give paper back. That "
                           "is a chemical change."},
                 {"text": "Steam condensing to water", "correct": True},
                 {"text": "An egg cooking in a pan", "correct": False,
                  "reply": "A cooked egg does not turn back into a raw one. That is a chemical "
                           "change."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Ice in a sealed bag melts. Explain why the mass of the bag stays the same. "
                       "Put the links in order.",
             "links": ["As the ice melts, the particles leave their fixed positions but stay in "
                       "the bag.",
                       "So the number of particles in the bag does not change, and neither does "
                       "the mass of each one.",
                       "So the total mass stays the same: mass is conserved."],
             "herrings": [{"text": "The water has more mass, because its particles move faster.",
                           "why": "Moving faster does not change the mass of a particle."},
                          {"text": "Some particles are destroyed as the ice melts.",
                           "why": "No particles are made or destroyed in a change of state."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Wax is melted and then left to cool until it is solid again. Explain why "
                       "this is a physical change. Put the links in order.",
             "links": ["The wax melts: the same particles move around each other instead of "
                       "staying in fixed positions.",
                       "As it cools, the same particles go back into fixed positions.",
                       "The solid wax has its original properties back, so this is a physical "
                       "change."],
             "herrings": [{"text": "A new substance forms when the wax melts.",
                           "why": "Melted wax is still wax. No new substance forms."},
                          {"text": "The mass of the wax increases as it becomes solid again.",
                           "why": "Mass is conserved in a change of state."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 4,
             "prompt": "Steam from a kettle condenses on a cold window. Describe what happens to "
                       "the particles, and explain why this is a physical change in which mass "
                       "is conserved.",
             "points": ["The steam changes from a gas to a liquid: it condenses.",
                        "The particles move closer together, but they are the same water "
                        "particles.",
                        "No particles are made or destroyed, so the mass is conserved.",
                        "No new substance forms: the drops on the window are still water.",
                        "Heated again, the water turns back into steam with its original "
                        "properties, so this is a physical change."],
             "reject": ["“The steam turns into a new substance on the glass.” The drops are "
                        "still water.",
                        "“Some mass is lost when the steam condenses.” Mass is conserved."]},
        ],
    },
}
