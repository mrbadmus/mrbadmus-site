"""Physics · Magnetism — the MRB-335 extension.

The thinnest topic in the whole KS4 pool for a Combined class, and the only
one where FOUNDATION was short (36 on the 7 Sep table, against a floor of
50). Seven of the ten subtopics are Higher, five of those Triple as well, so
Combined Foundation sees exactly three: `poles-of-a-magnet`,
`magnetic-fields` and `electromagnetism`. Every row in this file is in one
of those three, and each gets eight — four `easier`, two `standard`, two
`harder`, which is the split that lifts Foundation to 60 and Higher to 60
together.

⚠️ `docs/ks4/pool-authoring.md` §2 names `poles-of-a-magnet` as one of the
subtopics where the lesson page's matching block prints the whole examinable
core. That is still true, and the eight rows here work around it rather than
through it: what a magnet is made of and how domains behave are the printed
pairs, so these ask instead about DROPPING a magnet, about the induced chain
of paperclips, about what repulsion proves that attraction does not, and
about why hard and soft materials are chosen for different jobs.

No question needs a figure. Every field pattern is described in words.
"""

TOPIC = "magnetism"
SUBJECT = "physics"

QUESTIONS = [
    # ── poles-of-a-magnet ─────────────────────── BASE (6.7.1.1) ── +8 ──
    {
        "id": "ks4-poles-of-a-magnet-e05",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the two poles that every magnet has.",
        "options": [
            "Two north poles",
            "A north-seeking pole and a south-seeking pole",
            "A positive pole and a negative pole",
            "A magnetic pole and a neutral pole",
        ],
        "correct_index": 1,
        "why": "Magnetic poles always come in pairs — a north and a south — "
               "and no magnet has ever been found with only one.",
    },
    {
        "id": "ks4-poles-of-a-magnet-e06",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by an induced magnet.",
        "options": [
            "A magnet that keeps its magnetism permanently once made",
            "A magnet produced by heating a metal strongly",
            "A material that becomes a magnet only while it sits in a "
            "magnetic field",
            "A material that pushes all other magnets away from it",
        ],
        "correct_index": 2,
        "why": "Induced magnetism is borrowed: the material is magnetic "
               "while the field is there and stops being magnetic when it is "
               "removed.",
    },
    {
        "id": "ks4-poles-of-a-magnet-e07",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the force between two magnets as they "
                "are moved further apart.",
        "options": [
            "It gets weaker",
            "It gets stronger",
            "It stays exactly the same",
            "It changes from attraction to repulsion",
        ],
        "correct_index": 0,
        "why": "A magnetic field gets weaker with distance, so the "
               "non-contact force between two magnets falls as the gap "
               "grows.",
    },
    {
        "id": "ks4-poles-of-a-magnet-e08",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the observation that on its own proves a metal bar is "
                "a magnet.",
        "options": [
            "It attracts one end of a known magnet",
            "It repels one end of a known magnet",
            "It is attracted by a switched-on electromagnet",
            "It is made of steel rather than aluminium",
        ],
        "correct_index": 1,
        "why": "An unmagnetised magnetic material is always attracted, so "
               "only repulsion shows the bar has poles of its own.",
    },
    {
        "id": "ks4-poles-of-a-magnet-s05",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bar magnet is dropped onto a hard floor several times and "
                "becomes noticeably weaker. Explain why.",
        "options": [
            "The impacts knock the domains out of alignment, so they no "
            "longer point the same way",
            "The impacts heat the magnet past its Curie temperature very "
            "briefly",
            "The impacts knock iron atoms off the surface of the magnet",
            "The impacts reverse the poles, so the two ends cancel out",
        ],
        "correct_index": 0,
        "why": "The magnetism comes from domains pointing the same way, and "
               "a sharp shock jolts some of them back into random "
               "directions.",
    },
    {
        "id": "ks4-poles-of-a-magnet-s06",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A steel paperclip hangs from a magnet, and a second "
                "paperclip hangs from the first. Explain how the first clip "
                "is able to hold the second.",
        "options": [
            "The first clip becomes an induced magnet in the field, with "
            "poles of its own",
            "The magnet's field reaches straight through the first clip to "
            "the second one",
            "Steel paperclips are permanently magnetic because of the metal "
            "they are made from",
            "Static electricity builds up and holds the second clip in place",
        ],
        "correct_index": 0,
        "why": "The field magnetises the first clip, which then has its own "
               "north and south poles and can attract the next clip in "
               "turn.",
    },
    {
        "id": "ks4-poles-of-a-magnet-h05",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two bars, P and Q, attract each other whichever ends are "
                "brought together. Deduce what P and Q must be.",
        "options": [
            "Both are magnets",
            "Both are unmagnetised magnetic materials",
            "One is a magnet and the other is an unmagnetised magnetic "
            "material",
            "One is a magnet and the other is a non-magnetic material",
        ],
        "correct_index": 2,
        "why": "Two magnets would repel in one of the orientations, and two "
               "unmagnetised bars would do nothing, so exactly one of them "
               "is a magnet.",
    },
    {
        "id": "ks4-poles-of-a-magnet-h06",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a permanent magnet is made from a HARD magnetic "
                "material while an electromagnet's core is made from a SOFT "
                "one.",
        "options": [
            "A hard material is physically stronger, so it can lift a "
            "heavier load",
            "A soft material cannot be magnetised at all, which is what "
            "makes it safe to use inside a coil",
            "A hard material heats up less when a current flows through the "
            "coil",
            "A hard material keeps its alignment; a soft one loses it as "
            "soon as the field goes, so the magnet switches off",
        ],
        "correct_index": 3,
        "why": "The whole point of an electromagnet is that it can be turned "
               "off, and only a core that gives up its magnetism instantly "
               "will do that.",
    },

    # ── magnetic-fields ───────────────────────── BASE (6.7.1.2) ── +8 ──
    {
        "id": "ks4-magnetic-fields-e05",
        "subtopic_slug": "magnetic-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the direction in which magnetic field lines are drawn "
                "outside a bar magnet.",
        "options": [
            "From the south pole to the north pole",
            "From both poles inwards towards the middle",
            "From the north pole to the south pole",
            "From the middle outwards towards both poles",
        ],
        "correct_index": 2,
        "why": "By convention a field line points the way a compass north "
               "end would, which outside the magnet runs from its north pole "
               "to its south pole.",
    },
    {
        "id": "ks4-magnetic-fields-e06",
        "subtopic_slug": "magnetic-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what closely spaced field lines show about a magnetic "
                "field.",
        "options": [
            "The field is strong in that region",
            "The field is weak in that region",
            "The field points downwards in that region",
            "The field is zero in that region",
        ],
        "correct_index": 0,
        "why": "The spacing of the lines is how the model records strength: "
               "crowded lines mean a strong field.",
    },
    {
        "id": "ks4-magnetic-fields-e07",
        "subtopic_slug": "magnetic-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where the magnetic field of a bar magnet is "
                "strongest.",
        "options": [
            "Halfway along the length of the magnet",
            "At the two poles",
            "Everywhere around it, equally",
            "Just outside the middle of one long side",
        ],
        "correct_index": 1,
        "why": "The field lines are packed most closely at the poles, which "
               "is where the field is strongest.",
    },
    {
        "id": "ks4-magnetic-fields-e08",
        "subtopic_slug": "magnetic-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a plotting compass needle lines up with.",
        "options": [
            "The nearest north pole, wherever it is",
            "The Earth's geographic north pole, always",
            "The direction of the magnetic field at the point where it sits",
            "The heaviest concentration of iron filings nearby",
        ],
        "correct_index": 2,
        "why": "A compass responds to the total field where it is, which is "
               "why it is the tool that shows a field's direction rather "
               "than only its shape.",
    },
    {
        "id": "ks4-magnetic-fields-s05",
        "subtopic_slug": "magnetic-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a ship's compass must be kept away from the "
                "steel hull and from electrical cables.",
        "options": [
            "Steel becomes an induced magnet and a current makes its own "
            "field, and either can turn the needle",
            "Steel and copper both absorb the Earth's magnetic field, "
            "leaving nothing for the compass to detect",
            "The compass needle would rust in contact with steel and stop "
            "turning",
            "Electrical cables heat the needle and destroy its magnetism",
        ],
        "correct_index": 0,
        "why": "The compass shows the TOTAL field where it sits, so any "
               "nearby field adds to the Earth's and gives a false "
               "direction.",
    },
    {
        "id": "ks4-magnetic-fields-s06",
        "subtopic_slug": "magnetic-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the Earth behaves as though it has a bar magnet "
                "inside it, and state the evidence for this.",
        "options": [
            "Its rocks hold enough iron to act as one huge magnet, and iron "
            "filings stick to them everywhere",
            "Its liquid iron core produces the field, and the evidence is a "
            "compass settling the same way everywhere",
            "Its atmosphere carries an electric current, and the evidence "
            "is the aurora",
            "It does not — a compass points north only because it is "
            "attracted to the North Star",
        ],
        "correct_index": 1,
        "why": "The field comes from movement in the molten iron core, and a "
               "compass settling the same way everywhere is what shows a "
               "planet-wide field exists.",
    },
    {
        "id": "ks4-magnetic-fields-h05",
        "subtopic_slug": "magnetic-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student plotting a bar magnet's field marks two dots from "
                "two different field lines at exactly the same place. "
                "Explain why this must be a mistake.",
        "options": [
            "Field lines never cross, because the field has one direction "
            "only at any given point",
            "Field lines can cross, but only at a neutral point",
            "The two dots must belong to the same field line, so there is "
            "nothing wrong",
            "The compass was simply held too close to the magnet",
        ],
        "correct_index": 0,
        "why": "A compass at that point can only settle one way, so only one "
               "field line can pass through it.",
    },
    {
        "id": "ks4-magnetic-fields-h06",
        "subtopic_slug": "magnetic-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe a method using a plotting compass to compare the "
                "strengths of two bar magnets, and state the variable that "
                "must be controlled.",
        "options": [
            "Count the iron filings each magnet attracts, keeping the paper "
            "the same",
            "Time how long each magnet takes to turn the needle, keeping "
            "the temperature of the room the same",
            "Measure the mass each magnet can lift, keeping the compass "
            "nearby throughout",
            "Measure the distance at which each magnet just deflects the "
            "needle, keeping the needle's starting direction the same",
        ],
        "correct_index": 3,
        "why": "The stronger magnet reaches further before its field beats "
               "the Earth's, so the deflection distance is a fair comparison "
               "provided the starting conditions match.",
    },

    # ── electromagnetism ──────────────────────── BASE (6.7.2.1) ── +8 ──
    {
        "id": "ks4-electromagnetism-e05",
        "subtopic_slug": "electromagnetism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the magnetic field of a solenoid when "
                "the direction of the current is reversed.",
        "options": [
            "The field disappears completely for a moment",
            "The field becomes twice as strong",
            "The field reverses, so the north and south ends swap over",
            "The field is completely unchanged in every way",
        ],
        "correct_index": 2,
        "why": "The field direction is set by the current direction, so "
               "reversing one reverses the other and the poles change ends.",
    },
    {
        "id": "ks4-electromagnetism-e06",
        "subtopic_slug": "electromagnetism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one way to make an electromagnet stronger.",
        "options": [
            "Increase the current flowing through the coil",
            "Use a plastic core in place of the iron one",
            "Reduce the number of turns on the coil",
            "Use a longer wire wound as a single large turn",
        ],
        "correct_index": 0,
        "why": "A bigger current gives a stronger field around every turn, "
               "and the turns' fields add together inside the coil.",
    },
    {
        "id": "ks4-electromagnetism-e07",
        "subtopic_slug": "electromagnetism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the material used for the core of an electromagnet, "
                "and give the reason.",
        "options": [
            "Steel, because it is hard and keeps its magnetism",
            "Copper, because it conducts electricity extremely well",
            "Aluminium, because it is light enough to move quickly",
            "Iron, because it is soft and loses its magnetism when the "
            "current stops",
        ],
        "correct_index": 3,
        "why": "Iron magnetises strongly while the current flows and lets go "
               "the instant it stops, which is exactly what a switchable "
               "magnet needs.",
    },
    {
        "id": "ks4-electromagnetism-e08",
        "subtopic_slug": "electromagnetism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the magnetic field around a wire when "
                "the current is switched off.",
        "options": [
            "It disappears",
            "It stays exactly as it was",
            "It reverses direction",
            "It becomes stronger for a moment and then fades",
        ],
        "correct_index": 0,
        "why": "The field is produced by the moving charge, so with no "
               "current there is no field at all.",
    },
    {
        "id": "ks4-electromagnetism-s05",
        "subtopic_slug": "electromagnetism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scrapyard crane lifts steel with an electromagnet. "
                "Explain how the load is released.",
        "options": [
            "The current is switched off, the iron core loses its magnetism "
            "and the steel falls",
            "The current is reversed, which repels the steel away from the "
            "core",
            "The crane is lowered until the steel touches the ground and "
            "sticks there instead",
            "The core is heated until it loses all of its magnetism",
        ],
        "correct_index": 0,
        "why": "A soft iron core keeps no magnetism of its own, so cutting "
               "the current is enough to drop the load exactly where it is "
               "wanted.",
    },
    {
        "id": "ks4-electromagnetism-s06",
        "subtopic_slug": "electromagnetism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wire carrying a current passes vertically through a "
                "horizontal card, and iron filings are sprinkled on the "
                "card. Describe the pattern and state what it shows.",
        "options": [
            "Straight lines radiating outwards from the wire, showing the "
            "field points away from it everywhere",
            "Concentric circles centred on the wire, closest near it, so "
            "the field is circular and strongest there",
            "A completely even covering across the card, showing the field "
            "is the same everywhere",
            "No pattern at all, because a current in a straight wire "
            "produces no field",
        ],
        "correct_index": 1,
        "why": "The field around a straight wire is circular and gets weaker "
               "with distance, so the filings ring the wire and thin out "
               "further away.",
    },
    {
        "id": "ks4-electromagnetism-h05",
        "subtopic_slug": "electromagnetism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two solenoids carry the same current. Solenoid A has 200 "
                "turns spread over 10 cm; solenoid B has 200 turns spread "
                "over 40 cm. Predict which has the stronger field inside it, "
                "and explain.",
        "options": [
            "B, because its field is spread out over a much greater length "
            "of coil",
            "They are equal, because both have exactly 200 turns",
            "A, because its turns are packed more closely, so their fields "
            "add over a shorter length",
            "B, because a longer solenoid gives the field more room to "
            "build up",
        ],
        "correct_index": 2,
        "why": "What matters is turns per unit length, not turns alone: "
               "packing the same 200 turns into a quarter of the length "
               "concentrates the field.",
    },
    {
        "id": "ks4-electromagnetism-h06",
        "subtopic_slug": "electromagnetism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electromagnet is wound from INSULATED copper wire. "
                "Explain why the insulation is necessary.",
        "options": [
            "Without it the current would short across touching turns "
            "instead of going round every turn",
            "Without it the copper itself would become an induced magnet "
            "and cancel the field",
            "Without it the coil would overheat and melt the iron core",
            "Without it the magnetic field would point the wrong way along "
            "the coil",
        ],
        "correct_index": 0,
        "why": "The field depends on the current going round the coil many "
               "times, and bare touching turns would let it jump straight "
               "along instead.",
    },
]
