# -*- coding: utf-8 -*-
"""Poles of a magnet, in the lean shape. New record, no legacy page.
Spec table: ks4-poles-of-a-magnet.md (AQA 8464 6.7.1.1 / 8463 4.7.1.1)."""

LESSON = {
    "slug": "poles-of-a-magnet",
    "start": {
        "setup": "A magnet picks up an iron nail. You pull the nail off the magnet.",
        "question": "If you had to guess, what happens to the nail's magnetism?",
        "options": [
            ("It stays a strong magnet",
             "It loses most of its magnetism quickly. The nail was an induced magnet, made by the "
             "magnet's field."),
            ("It loses most of its magnetism",
             "It loses most of its magnetism quickly. The nail was an induced magnet, made by the "
             "magnet's field."),
        ],
        "answer": 1,
    },
    "words": ["pole", "non-contact force", "permanent magnet", "induced magnet"],
    "knowledge": [
        {"kind": "card", "title": "The poles",
         "body": ["Every magnet has a north pole and a south pole.",
                  "The poles of a magnet are the places where the magnetic forces are strongest."]},
        {"kind": "card", "title": "Like and unlike poles",
         "body": ["When two magnets are brought close together they exert a force on each other.",
                  {"points": ["Two like poles repel each other: north and north, or south and south.",
                              "Two unlike poles attract each other: north and south."]},
                  "Look at which poles face each other.",
                  {"slot": "fig:two-magnets"}]},
        {"kind": "card", "title": "A non-contact force",
         "body": ["Attraction and repulsion between two magnetic poles are examples of "
                  "non-contact force.",
                  "The magnets do not have to touch for the force to act."]},
        {"kind": "card", "title": "Permanent magnets",
         "body": ["A permanent magnet produces its own magnetic field.",
                  "It can attract or repel another magnet, depending on which poles face each other.",
                  "A bar magnet is a permanent magnet."]},
        {"kind": "card", "title": "Induced magnets",
         "body": ["An induced magnet is a material that becomes a magnet when it is placed in a "
                  "magnetic field.",
                  "Iron, steel, cobalt and nickel are magnetic materials. They can become induced "
                  "magnets.",
                  "Induced magnetism always causes a force of attraction.",
                  "When removed from the magnetic field, an induced magnet loses most or all of its "
                  "magnetism quickly."]},
        {"kind": "reveal", "title": "Permanent and induced magnets",
         "cols": ["Permanent magnet", "Induced magnet"],
         "rows": [
             ("Where its magnetism comes from",
              "It produces its own magnetic field.",
              "It becomes a magnet when it is placed in a magnetic field."),
             ("Force on another magnet",
              "Attraction or repulsion.",
              "Always attraction."),
             ("Taken out of the field",
              "It stays a magnet.",
              "It loses most or all of its magnetism quickly."),
             ("Example",
              "A bar magnet.",
              "An iron nail held near a bar magnet."),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("An induced magnet can repel a magnet.",
              "Induced magnetism always causes a force of attraction."),
             ("If a bar is attracted to a magnet, it must be a permanent magnet.",
              "A magnetic material is attracted too. Only repulsion shows both are permanent magnets."),
             ("An induced magnet keeps its magnetism.",
              "It loses most or all of its magnetism quickly when removed from the field."),
         ]}]},
    ],
    "key_fact": "Like poles repel and unlike poles attract, and these are non-contact forces. A "
                "permanent magnet produces its own magnetic field, but an induced magnet only "
                "becomes a magnet in a magnetic field, always attracts, and loses most or all of its "
                "magnetism quickly when removed from the field.",
    "deeper": [
        {"kind": "card", "title": "Why an induced magnet always attracts",
         "body": ["The end of the induced magnet nearest the magnet becomes the opposite pole.",
                  "Hold a north pole near an iron nail: the near end of the nail becomes a south pole.",
                  "Unlike poles attract, so the nail is pulled towards the magnet whichever pole you use."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: say what happens, for example which poles attract and "
             "which repel.",
             "<strong>Describe the difference</strong>: say something about both kinds of magnet "
             "each time.",
             "<strong>Explain</strong>: say what happens and why.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State where the magnetic forces of a magnet are strongest.",
             "why": "The poles of a magnet are the places where the magnetic forces are strongest.",
             "options": [
                 {"text": "In the middle of the magnet", "correct": False,
                  "reply": "The forces are weakest in the middle."},
                 {"text": "At the poles", "correct": True},
                 {"text": "Equally all along the magnet", "correct": False,
                  "reply": "The forces are strongest at the poles."},
             ]},
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "Two bar magnets are held with their south poles facing. State what happens.",
             "why": "Two like poles repel each other.",
             "options": [
                 {"text": "They attract", "correct": False,
                  "reply": "Unlike poles attract. These are like poles."},
                 {"text": "Nothing happens", "correct": False,
                  "reply": "Two magnets close together always exert a force on each other."},
                 {"text": "They repel", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "Describe the difference between a permanent magnet and an induced magnet.",
             "why": "A permanent magnet produces its own field. An induced magnet needs to be in a "
                    "magnetic field.",
             "options": [
                 {"text": "An induced magnet produces its own magnetic field. A permanent magnet "
                          "only works near another magnet.", "correct": False,
                  "reply": "This is the wrong way round."},
                 {"text": "A permanent magnet produces its own magnetic field. An induced magnet "
                          "becomes a magnet in a magnetic field.", "correct": True},
                 {"text": "A permanent magnet can only attract. An induced magnet can attract or "
                          "repel.", "correct": False,
                  "reply": "Induced magnetism always causes attraction. A permanent magnet can do both."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "A student holds each end of a metal bar near the north pole of a magnet. "
                       "Both ends are attracted. Explain what this tells you about the bar.",
             "why": "A permanent magnet would repel at one end. Both ends attract, so the bar is a "
                    "magnetic material acting as an induced magnet.",
             "options": [
                 {"text": "It is a permanent magnet, because it is attracted", "correct": False,
                  "reply": "A magnetic material is attracted too. A permanent magnet would repel at one end."},
                 {"text": "It is a magnetic material, not a permanent magnet", "correct": True},
                 {"text": "It is not a magnetic material, because both ends behave the same",
                  "correct": False,
                  "reply": "It is attracted, so it must be a magnetic material."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "A bar magnet picks up an iron nail. A second iron nail then hangs from the "
                       "first nail. Explain why. Put the links in order.",
             "links": ["The first nail is in the magnetic field of the magnet, so it becomes an "
                       "induced magnet.",
                       "The second nail is in the magnetic field of the first nail, so it becomes "
                       "an induced magnet too.",
                       "Induced magnetism always causes a force of attraction, so the second nail "
                       "hangs from the first."],
             "herrings": [{"text": "The second nail repels the first nail.",
                           "why": "Induced magnetism always causes a force of attraction."},
                          {"text": "Both nails become permanent magnets.",
                           "why": "They are only magnets while they are in a magnetic field."}]},
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "A bar magnet is held above an iron nail. The nail jumps up to the magnet. "
                       "Then the nail is pulled off. Describe what happens to the nail. Put the "
                       "links in order.",
             "links": ["The nail is placed in the magnetic field of the magnet.",
                       "The nail becomes an induced magnet, so it is attracted to the magnet.",
                       "When the nail is removed from the field, it loses most or all of its "
                       "magnetism quickly."],
             "herrings": [{"text": "The nail is repelled by one pole of the magnet.",
                           "why": "Induced magnetism always causes a force of attraction."},
                          {"text": "The nail stays a strong magnet after it is pulled off.",
                           "why": "An induced magnet loses most or all of its magnetism quickly."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "Describe the differences between a permanent magnet and an induced magnet.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "Compares the two kinds of magnet on two or "
                  "more points: where the field comes from, the forces each can cause, or what "
                  "happens out of the field.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "Gives one correct fact about either kind of "
                  "magnet.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["A permanent magnet produces its own magnetic field.",
                        "An induced magnet is a material that becomes a magnet when it is placed "
                        "in a magnetic field.",
                        "A permanent magnet can attract or repel another magnet: like poles "
                        "repel, unlike poles attract.",
                        "Induced magnetism always causes a force of attraction.",
                        "When removed from the magnetic field, an induced magnet loses most or "
                        "all of its magnetism quickly."],
             "reject": ["“An induced magnet can repel a magnet.”",
                        "“An induced magnet keeps its magnetism for ever.”"]},
        ],
    },
}
