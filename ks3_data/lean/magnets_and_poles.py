# -*- coding: utf-8 -*-
"""Magnets and poles, in the lean shape. Spec table: docs/lessons/wave2/ks3-magnets-and-poles.md."""

LESSON = {
    "slug": "magnets-and-poles",
    "start": {
        "setup": "Two bar magnets snap together. You turn one round, and now they push apart.",
        "question": "If you had to guess, what changed when one magnet was turned round?",
        "options": [
            ("How strong it is",
             "Its strength is the same. A different end now faces the other magnet."),
            ("Which end faces the other",
             "Yes. Each end is a pole, and the two ends of a magnet behave oppositely."),
        ],
        "answer": 1,
    },
    "words": ["pole", "repel", "attract", "magnetic material"],
    "word_defs": {
        "pole": "One end of a magnet, where its force is strongest. Every magnet has a north and a south pole.",
        "repel": "To push apart. Like poles repel.",
        "attract": "To pull together. Unlike poles attract.",
        "magnetic material": "A material a magnet attracts: iron, steel, nickel or cobalt.",
    },
    "knowledge": [
        {"kind": "card", "title": "North and south poles",
         "body": ["Every magnet has two poles, one at each end.",
                  "Hang a magnet up and one end turns to point north.",
                  "That end is the north-seeking pole, written N.",
                  "The other end is the south-seeking pole, written S.",
                  "Poles always come in pairs.",
                  "Cut a magnet in half and each piece has an N and an S."]},
        {"kind": "card", "title": "How magnets interact",
         "body": [{"figure": "p10-pole-pairs-three"},
                  "Like poles repel. N and N push apart. S and S push apart.",
                  "Unlike poles attract. N and S pull together.",
                  "The forces on the two magnets are equal in size and opposite in direction.",
                  "Magnets push and pull without touching, so this is a non-contact force."]},
        {"kind": "card", "title": "Closer means much stronger",
         "body": ["The force between two magnets gets weaker quickly as the gap grows.",
                  "Halve the gap, and the force grows to far more than double.",
                  "That is why two magnets snap together over the last centimetre."]},
        {"kind": "card", "title": "Magnetic materials",
         "body": ["A magnet only attracts a few materials.",
                  "Iron, steel, nickel and cobalt are magnetic materials.",
                  "Most metals are not magnetic. Aluminium, copper, brass and gold are not.",
                  "Wood, plastic and glass are not magnetic either.",
                  "A magnet attracts a magnetic material, whichever pole you use."]},
        {"kind": "card", "title": "The test for a magnet",
         "body": [{"figure": "p10-steel-test-three"},
                  "Near a magnet, a piece of steel becomes a magnet for a while.",
                  "The end of the steel nearest the magnet becomes the opposite pole.",
                  "So the steel is pulled in, whichever pole of the magnet you use.",
                  "Attraction cannot tell a magnet from plain steel.",
                  "Repulsion is the only proof. Only a magnet can be pushed away by a magnet."]},
        {"kind": "reveal", "title": "What a magnet does",
         "cols": ["N pole near it", "S pole near it"],
         "rows": [
             ("Another magnet's N pole", "Repel", "Attract"),
             ("Another magnet's S pole", "Attract", "Repel"),
             ("A steel nail", "Attract", "Attract"),
             ("An aluminium can", "Nothing", "Nothing"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("All metals are magnetic.",
              "Iron, steel, nickel and cobalt are. Aluminium and copper are not.", "MAG-01"),
             ("It stuck to the magnet, so it must be a magnet.",
              "Plain steel sticks too. Only repulsion proves it is a magnet.", "MAG-02"),
             ("Turning a magnet round makes it stronger or weaker.",
              "It changes which pole faces the other magnet. Its strength stays the same.", "MAG-03"),
             ("A magnet does nothing to plain steel.",
              "A magnet attracts plain steel, whichever pole you use.", "MAG-04"),
             ("Cut a magnet in half to get a north piece and a south piece.",
              "Each piece is a new magnet with its own N and S."),
         ]}]},
    ],
    "key_fact": "Every magnet has a north pole and a south pole. "
                "Like poles repel and unlike poles attract. "
                "A magnet also attracts iron, steel, nickel and cobalt. "
                "So only repulsion proves an object is a magnet.",
    "deeper": [
        {"kind": "card", "title": "Sorting cans",
         "body": ["Recycling plants use magnets to sort cans.",
                  "Steel cans are lifted out, because steel is a magnetic material.",
                  "Aluminium cans are left behind, because aluminium is not.",
                  "To check a can left behind, hold a magnet near it both ways round.",
                  "Any pull at all means it is a magnetic material."]},
        {"kind": "card", "title": "Iron and steel",
         "body": ["Near a magnet, iron and steel both become magnets.",
                  "Take the magnet away, and soft iron loses its magnetism straight away.",
                  "Steel can keep some, and become a magnet of its own."]},
    ],
    "try": None,
    "tutor_body": "Not sure whether a test proves something is a magnet?",
    "connects_heading": None,
    "safeguarding_note": {
        "eyebrow": "If a magnet has been swallowed, or you are worried about someone",
        "body": "Swallowing a strong magnet is treated urgently, even when the person seems fine. "
                "Tell an adult straight away rather than waiting to see. "
                "A pharmacist, your GP or 111 will tell you what to do next. "
                "At school, the school nurse or any member of staff can start that. "
                "If you would rather talk to somebody outside all of that, "
                "<strong>Childline is free on 0800 1111</strong>, at any hour, and you do not have to give your name.",
    },
    "ks4_becomes": "Permanent and induced magnetism, and magnetic field patterns.",
    "figures": [
        {"id": "p10-pole-pairs-three", "kind": "diagram", "status": "drawn", "art": "p10-pole-pairs",
         "title": "Three pairs of bar magnets and the forces on them",
         "desc": "Three rows, each with two bar magnets end to end. In the first row two N poles face "
                 "each other and arrows point away from the gap: N and N repel. In the second row two S "
                 "poles face each other and the arrows point away: S and S repel. In the third row an N "
                 "pole faces an S pole and the arrows point towards the gap: N and S attract.",
         "caption": "The arrows show which way each magnet is pushed or pulled.",
         "data": {}},
        {"id": "p10-steel-test-three", "kind": "diagram", "status": "drawn", "art": "p10-steel-test",
         "title": "A magnet tested against plain steel, then against a magnet",
         "desc": "Three rows. In the first, the N pole of a magnet faces a plain steel bar. The steel's "
                 "near end is marked S in small letters and an arrow shows it pulled in. In the second, "
                 "the magnet is turned round so its S pole faces the steel. The steel's near end is now "
                 "marked N, and it is pulled in again. In the third, the N pole faces the N pole of a "
                 "second magnet, and an arrow shows that magnet pushed away.",
         "caption": "The small letters show the poles the magnet makes in the steel.",
         "data": {}},
    ],
    "ladder_stem": {
        "produce": "A scrapyard sorts crushed drinks cans. Steel and aluminium cans pass on the same belt. "
                   "A magnet lifts one kind out. Say which kind is lifted. "
                   "Explain how you would check that a can left behind is really aluminium.",
    },
    "ladder_feedback": {
        "recall": {
            0: "Plain steel is attracted both ways too. Attraction never proves it is a magnet.",
            2: "Two magnets do attract when unlike poles face. That reason is wrong.",
            3: "It moved towards the magnet, so it is a magnetic material.",
        },
        "apply": {
            0: "The force does not just follow the gap. Halving it gives far more than double.",
            1: "The magnets are the same, but the force depends on the gap too.",
            3: "Pushing them closer is harder because the force is getting bigger.",
        },
    },
}
