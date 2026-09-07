"""Physics · Magnetism — poles, fields, electromagnetism, the motor effect.

The first five subtopics of AQA 8463 §6.7 (part A of the magnetism topic):
`poles-of-a-magnet`, `magnetic-fields`, `electromagnetism`,
`flemings-left-hand-rule` and `electric-motors`.

Distractors are built from the four misconceptions the lesson pages declare:
induced magnetism mistaken for permanent magnetism (and attraction taken as
proof of a magnet, when only repulsion is); field lines drawn from south to
north outside a magnet, and closer lines read as a weaker field; a hard
(steel) core used where a soft (iron) one is needed; and Fleming's RIGHT hand
— the generator rule — used for the motor effect. In the F = BIl questions the
wrong answers come from the errors rather than from noise: the length of
conductor left out entirely, centimetres not converted to metres, and the
number of turns forgotten.

⚠️ `magnetic-fields` is byte-identical to a KS3 lesson slug. These questions
are deliberately KS4: the required practical's plotting-compass method, the
neutral point between like poles, the uniform field in a horseshoe gap, and
the field-lines-as-a-model idea. None of them would be set at KS3.

⚠️ No question here needs a figure. Every direction in the Fleming's
left-hand-rule questions is given in words — compass points, vertical, along
the bench — never "as shown".
"""

TOPIC = "magnetism"
SUBJECT = "physics"

QUESTIONS = [
    # ── poles-of-a-magnet ───────────────────────────────── BASE (6.7.1.1) ──
    {
        "id": "ks4-poles-of-a-magnet-e01",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which list contains only magnetic (ferromagnetic) materials?",
        "options": [
            "Aluminium, copper and nickel",
            "Iron, aluminium and cobalt",
            "Iron, nickel and cobalt",
            "Copper, steel and brass",
        ],
        "correct_index": 2,
        "why": "Only iron, steel, nickel and cobalt are ferromagnetic — "
               "aluminium, copper and brass feel no force from a magnet at "
               "all.",
    },
    {
        "id": "ks4-poles-of-a-magnet-e02",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens when the north pole of one bar magnet is "
                "brought close to the north pole of another.",
        "options": [
            "They repel each other",
            "They attract each other",
            "They attract only if one magnet is the stronger of the two",
            "There is no force between them, because both ends are north",
        ],
        "correct_index": 0,
        "why": "Like poles always repel — two north poles push apart without "
               "ever touching, because magnetism is a non-contact force.",
    },
    {
        "id": "ks4-poles-of-a-magnet-e03",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement about the force between a magnet and a "
                "magnetic material is correct?",
        "options": [
            "It acts only once the magnet is touching the object",
            "It acts only on objects that carry an electric charge",
            "It acts on every metal, because all metals contain iron",
            "It is a non-contact force, so it acts at a distance",
        ],
        "correct_index": 3,
        "why": "Magnetic force is a non-contact force: the magnet pulls on a "
               "magnetic material across a gap, with nothing in between.",
    },
    {
        "id": "ks4-poles-of-a-magnet-e04",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the material a permanent bar magnet is usually made "
                "from, and give the reason.",
        "options": [
            "Iron, because it is soft and so is easy to magnetise",
            "Steel, because it is hard and so keeps its magnetism",
            "Copper, because it conducts electricity well",
            "Aluminium, because it is light and does not corrode",
        ],
        "correct_index": 1,
        "why": "Steel is a hard magnetic material — harder to magnetise, but "
               "it holds on to its magnetism once it has been magnetised.",
    },
    {
        "id": "ks4-poles-of-a-magnet-s01",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electromagnet lifts an unmagnetised iron nail. The "
                "current is then switched off. Predict what the nail does, "
                "and give the reason.",
        "options": [
            "It stays firmly stuck on, because it is now permanently "
            "magnetised",
            "It falls off, because iron is soft and loses its induced "
            "magnetism",
            "It falls off, because the nail's domains have become "
            "permanently aligned",
            "It is pushed away, because the nail's poles reverse as the "
            "current stops",
        ],
        "correct_index": 1,
        "why": "Iron is magnetically soft — its domains fall back into random "
               "directions the moment the external field is removed, so the "
               "induced magnetism disappears.",
    },
    {
        "id": "ks4-poles-of-a-magnet-s02",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the difference, in terms of domains, between a "
                "magnetised and an unmagnetised piece of steel.",
        "options": [
            "The magnetised piece contains many more domains than the "
            "unmagnetised piece",
            "The magnetised piece has large domains, while the unmagnetised "
            "piece has tiny ones",
            "The domains of the magnetised piece are all north, and those of "
            "the unmagnetised piece all south",
            "The domains of the magnetised piece point the same way, and "
            "those of the unmagnetised piece point randomly",
        ],
        "correct_index": 3,
        "why": "Magnetising does not create domains, it lines them up — "
               "aligned domains add together to give a net field, while "
               "randomly arranged ones cancel out.",
    },
    {
        "id": "ks4-poles-of-a-magnet-s03",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A steel bar magnet is heated strongly in a Bunsen flame and "
                "then left to cool. Explain what has happened to its "
                "magnetism.",
        "options": [
            "It is far weaker, because heating past the Curie temperature "
            "randomises the domains",
            "It is stronger, because the heat gives the domains the energy to "
            "line up better",
            "It is unchanged, because steel is a hard magnetic material that "
            "resists any change",
            "Its two poles have swapped over, because heating reverses every "
            "domain",
        ],
        "correct_index": 0,
        "why": "Above the Curie temperature the domains have enough energy to "
               "jumble out of alignment, so the magnet loses its net field.",
    },
    {
        "id": "ks4-poles-of-a-magnet-s04",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pin is magnetised by stroking it repeatedly in the same "
                "direction with one pole of a bar magnet. Suggest why "
                "stroking it in alternating directions would not work.",
        "options": [
            "Alternating strokes heat the pin past its Curie temperature, so "
            "its alignment is destroyed",
            "Alternating strokes make the pin repel the magnet, so no domains "
            "can move",
            "Each stroke would align the domains the opposite way to the "
            "stroke before it",
            "A pin can only be magnetised by a current in a solenoid, never "
            "by stroking",
        ],
        "correct_index": 2,
        "why": "Magnetising works by pulling the domains into one common "
               "direction, so reversing the stroke each time simply undoes "
               "the alignment made by the stroke before.",
    },
    {
        "id": "ks4-poles-of-a-magnet-h01",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical steel bars, X and Y, are held end to end. X is "
                "a magnet; Y has not been magnetised. A student says: 'They "
                "attract, so both bars must be magnets.' Evaluate this "
                "statement.",
        "options": [
            "Correct — attraction needs two sets of poles, so both bars must "
            "be magnets",
            "Correct — Y must be a magnet already, because steel is always "
            "magnetic",
            "Incorrect — attraction between the bars proves that neither bar "
            "is a magnet",
            "Incorrect — X induces magnetism in Y, so attraction on its own "
            "proves nothing about Y",
        ],
        "correct_index": 3,
        "why": "Only repulsion is a reliable test for a magnet: a magnet "
               "attracts any magnetic material by inducing the opposite pole "
               "in the end nearest to it.",
    },
    {
        "id": "ks4-poles-of-a-magnet-h02",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student magnetises a steel bar by stroking it, then keeps "
                "stroking it for a further five minutes. Explain why the bar "
                "does not keep getting stronger.",
        "options": [
            "The extra strokes heat the bar past its Curie temperature",
            "The extra strokes gradually reverse the direction of the bar's "
            "poles, so it weakens again",
            "Once every domain is aligned there is nothing left to align",
            "The bar starts to lose its magnetism, because steel is a soft "
            "magnetic material",
        ],
        "correct_index": 2,
        "why": "Stroking works by aligning domains, so once they all point "
               "the same way the magnet has reached the strongest it can be.",
    },
    {
        "id": "ks4-poles-of-a-magnet-h03",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Steel food cans and aluminium drinks cans travel together "
                "along a conveyor belt and are separated by a magnet above "
                "the belt. Explain why this works.",
        "options": [
            "Aluminium is repelled by the magnet while steel is attracted, so "
            "the two are pushed apart",
            "Steel is ferromagnetic and is attracted to the magnet, while "
            "aluminium is not magnetic at all",
            "Aluminium conducts better, so the magnet induces a stronger "
            "field in the steel cans",
            "Steel is denser than aluminium, so the magnet is able to lift "
            "only the lighter cans",
        ],
        "correct_index": 1,
        "why": "Only iron, steel, nickel and cobalt are attracted to a "
               "magnet, so the steel cans are lifted off the belt while the "
               "aluminium ones feel no force and stay on it.",
    },
    {
        "id": "ks4-poles-of-a-magnet-h04",
        "subtopic_slug": "poles-of-a-magnet",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'While the current is on, the iron core of "
                "an electromagnet is a permanent magnet, because it produces "
                "its own magnetic field.' Identify the error.",
        "options": [
            "The core is an induced magnet — it is magnetic only while it "
            "sits in the coil's field",
            "The core is not magnetic at all — the whole field comes from the "
            "coil of wire",
            "The core is a permanent magnet, but only when it is made of iron "
            "rather than steel",
            "The core is a permanent magnet whose poles reverse each time the "
            "current is switched on",
        ],
        "correct_index": 0,
        "why": "A permanent magnet keeps its field with no external field "
               "present, whereas the iron core is only magnetic because the "
               "coil's field is inducing magnetism in it.",
    },

    # ── magnetic-fields ─────────────────────────────────── BASE (6.7.1.2) ──
    {
        "id": "ks4-magnetic-fields-e01",
        "subtopic_slug": "magnetic-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a magnetic field.",
        "options": [
            "The region inside a magnet in which the domains are aligned",
            "The region around a magnet in which a magnetic material "
            "experiences a force",
            "The set of lines drawn on paper where iron filings happen to "
            "settle",
            "The region around a magnet in which the air itself becomes "
            "magnetised",
        ],
        "correct_index": 1,
        "why": "A magnetic field is the region of space in which a magnetic "
               "material feels a force; the field lines are only a way of "
               "drawing it.",
    },
    {
        "id": "ks4-magnetic-fields-e02",
        "subtopic_slug": "magnetic-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which piece of equipment shows the direction of a magnetic "
                "field at a point, and not just its shape?",
        "options": [
            "Iron filings scattered onto a sheet of paper",
            "A steel paper clip hung from a thread",
            "A plotting compass",
            "An ammeter connected across the two poles",
        ],
        "correct_index": 2,
        "why": "A plotting compass needle turns until it lines up with the "
               "field, and its north end then points along the field line — "
               "something iron filings cannot show.",
    },
    {
        "id": "ks4-magnetic-fields-e03",
        "subtopic_slug": "magnetic-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is always true about two magnetic field lines.",
        "options": [
            "They never cross one another",
            "They cross at right angles close to the poles",
            "They cross wherever the field is at its strongest",
            "They cross only on the inside of the magnet",
        ],
        "correct_index": 0,
        "why": "The field at any point has one single direction, so two lines "
               "crossing would mean a compass there pointing two ways at "
               "once.",
    },
    {
        "id": "ks4-magnetic-fields-e04",
        "subtopic_slug": "magnetic-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plotting compass placed well away from any magnet always "
                "settles pointing in the same direction. State what this "
                "provides evidence for.",
        "options": [
            "That the compass needle is magnetised afresh by the air around "
            "it each time it is used",
            "That iron in the rocks directly beneath the compass attracts "
            "the needle towards itself",
            "That gravity pulls the heavier end of the needle round towards "
            "the nearest pole",
            "That the Earth has its own magnetic field, produced by its core",
        ],
        "correct_index": 3,
        "why": "A compass lines itself up with whatever field it sits in, so "
               "a consistent direction everywhere shows the Earth itself is "
               "producing a magnetic field.",
    },
    {
        "id": "ks4-magnetic-fields-s01",
        "subtopic_slug": "magnetic-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical bar magnets lie in a line on a bench with "
                "their north poles a few centimetres apart. Describe the "
                "field in the space between them.",
        "options": [
            "The lines run straight across from one magnet to the other, "
            "giving a strong uniform field",
            "The lines cross one another at the midpoint between the two "
            "magnets",
            "The field is at its strongest exactly midway between the two "
            "north poles",
            "The lines curve apart, and midway between them the fields "
            "cancel at a neutral point",
        ],
        "correct_index": 3,
        "why": "Two like poles push their field lines apart, and at the "
               "midpoint the two equal fields act in opposite directions and "
               "cancel, leaving a neutral point.",
    },
    {
        "id": "ks4-magnetic-fields-s02",
        "subtopic_slug": "magnetic-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student is plotting a field line around a bar magnet with "
                "a plotting compass and has marked the first dot. Describe "
                "the correct next step.",
        "options": [
            "Move the compass until its south end sits on the dot, then mark "
            "the new position of its north end",
            "Move the compass until its north end sits on the dot, then mark "
            "the new position of its south end",
            "Turn the compass through 180 degrees without moving it, and mark "
            "where the north end now points",
            "Move the compass 5 cm directly away from the magnet, and mark "
            "the position of both of its ends",
        ],
        "correct_index": 0,
        "why": "Each step has to start where the last one finished, so the "
               "compass is moved forward until its south end is on the "
               "previous dot and its north end marks the next point along.",
    },
    {
        "id": "ks4-magnetic-fields-s03",
        "subtopic_slug": "magnetic-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why iron filings alone cannot tell a student which "
                "end of a bar magnet is its north pole.",
        "options": [
            "Iron filings are attracted only to a south pole, so they always "
            "gather at one end",
            "Iron filings are not magnetic, so they only show where the field "
            "falls to zero",
            "Each filing becomes an induced magnet lying along the field "
            "line, but not which way along it",
            "Iron filings show only the direction of the field, and give no "
            "information at all about its strength",
        ],
        "correct_index": 2,
        "why": "A filing is induced into a tiny magnet that lines up with the "
               "field, so it traces the line's shape but sits along it "
               "equally well either way round.",
    },
    {
        "id": "ks4-magnetic-fields-s04",
        "subtopic_slug": "magnetic-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A horseshoe magnet is a bar magnet bent so that its north "
                "and south poles face each other across a small gap. Describe "
                "the field in that gap.",
        "options": [
            "There is no field in the gap, because the two opposite poles "
            "cancel each other out",
            "The lines run straight across the gap from north to south, "
            "giving a strong, almost uniform field",
            "The lines curve around the outside of the magnet and do not "
            "enter the gap at all",
            "The lines run straight across the gap from south to north, "
            "giving a weak and uneven field",
        ],
        "correct_index": 1,
        "why": "Unlike poles facing each other pull the field lines straight "
               "across the gap, so they are close together and evenly spaced "
               "— a strong, nearly uniform field.",
    },
    {
        "id": "ks4-magnetic-fields-h01",
        "subtopic_slug": "magnetic-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the end of a compass needle that swings towards "
                "the north is called its north pole, even though it is "
                "attracted to what lies in that direction.",
        "options": [
            "It is named for the direction it seeks, and the Earth's magnetic "
            "pole under the geographic north is a south pole, so unlike poles "
            "attract",
            "It is named for the direction it seeks, and the Earth's magnetic "
            "pole under the geographic north is a north pole, so like poles "
            "attract over long distances",
            "It is a north pole because the Earth's field magnetises the "
            "needle afresh every time the compass is used",
            "The name is arbitrary, because a compass needle has no poles of "
            "its own and simply lies along the field",
        ],
        "correct_index": 0,
        "why": "'North pole' means the north-seeking end, and it is pulled "
               "that way because what sits beneath the geographic north is "
               "magnetically a south pole.",
    },
    {
        "id": "ks4-magnetic-fields-h02",
        "subtopic_slug": "magnetic-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that a bar magnet's field exists only in "
                "the flat plane of the paper it is resting on, because that "
                "is where the iron filings lie. Evaluate this claim.",
        "options": [
            "Correct — a magnetic field is a flat pattern that exists only on "
            "a surface",
            "Incorrect — the field fills the space all around the magnet, "
            "and the filings show one slice of it",
            "Incorrect — the field exists only inside the magnet, and the "
            "filings are held on the paper by gravity",
            "Correct — the field of a magnet reaches into three dimensions "
            "only when the magnet is stood on end",
        ],
        "correct_index": 1,
        "why": "Field lines are drawn on paper for convenience, but the field "
               "itself is a region of space surrounding the magnet in every "
               "direction.",
    },
    {
        "id": "ks4-magnetic-fields-h03",
        "subtopic_slug": "magnetic-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the required practical a student plots a bar magnet's "
                "field on a bench next to a large steel radiator, and finds "
                "the pattern is not symmetrical. Suggest the most likely "
                "reason.",
        "options": [
            "The plotting compass is faulty, because its needle has become "
            "demagnetised",
            "Iron filings should have been used, because a compass cannot "
            "plot the field of a bar magnet",
            "The magnet is too strong, so the compass needle is unable to "
            "turn freely on its pivot",
            "The steel radiator has become an induced magnet, and its field "
            "adds to the bar magnet's",
        ],
        "correct_index": 3,
        "why": "A compass lines up with the resultant of every field present, "
               "so nearby magnetic material distorts the pattern being "
               "plotted.",
    },
    {
        "id": "ks4-magnetic-fields-h04",
        "subtopic_slug": "magnetic-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student states: 'Field lines are real lines in space, and "
                "in the gaps between them there is no magnetic field.' "
                "Explain the error in this statement.",
        "options": [
            "There is indeed no field between the lines, though there is one "
            "along them, so the statement is nearly right",
            "The lines are real, but the field in the gaps between them "
            "points the opposite way",
            "Field lines are a model — the field is present everywhere, and "
            "the lines only record it",
            "Field lines are real, and every bar magnet has exactly eight of "
            "them running from pole to pole",
        ],
        "correct_index": 2,
        "why": "The field is continuous throughout the whole region; the "
               "lines are a drawing convention whose spacing represents how "
               "strong that everywhere-present field is.",
    },

    # ── electromagnetism ────────────────────────────────── BASE (6.7.2.1) ──
    {
        "id": "ks4-electromagnetism-e01",
        "subtopic_slug": "electromagnetism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the shape of the magnetic field around a long "
                "straight wire carrying a current.",
        "options": [
            "Straight lines running alongside the wire, in the same direction "
            "as the current",
            "Straight lines pointing outwards from the wire, like the spokes "
            "of a wheel",
            "A single large loop joining the two ends of the wire together",
            "Circles centred on the wire, lying in a plane at right angles to "
            "it",
        ],
        "correct_index": 3,
        "why": "The field of a current-carrying wire is a set of circles "
               "around the wire, in the plane perpendicular to it.",
    },
    {
        "id": "ks4-electromagnetism-e02",
        "subtopic_slug": "electromagnetism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the strength of the magnetic field "
                "around a straight wire as the distance from the wire "
                "increases.",
        "options": [
            "It becomes stronger, because the circles of field are longer",
            "It becomes weaker",
            "It stays exactly the same at every distance",
            "It falls to zero and then rises again beyond 1 cm",
        ],
        "correct_index": 1,
        "why": "The field of a current-carrying wire weakens with distance, "
               "which is why the circles are drawn further apart the further "
               "out you go.",
    },
    {
        "id": "ks4-electromagnetism-e03",
        "subtopic_slug": "electromagnetism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the two parts that together make up an electromagnet.",
        "options": [
            "A solenoid and a permanent bar magnet",
            "A single straight wire and a steel core",
            "A solenoid and an iron core",
            "A coil of copper wire and a copper core",
        ],
        "correct_index": 2,
        "why": "An electromagnet is a solenoid wound around a soft iron core, "
               "which becomes an induced magnet and greatly strengthens the "
               "field.",
    },
    {
        "id": "ks4-electromagnetism-e04",
        "subtopic_slug": "electromagnetism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the magnetic field inside a solenoid carrying a "
                "steady current.",
        "options": [
            "Strong and uniform, with parallel lines along the axis of the "
            "coil",
            "Zero, because the fields of the separate turns cancel inside the "
            "coil",
            "Circular, running round and round the inside of the coil",
            "Strongest at the centre, with lines pointing outwards in every "
            "direction",
        ],
        "correct_index": 0,
        "why": "Every turn adds its own field along the axis, so inside the "
               "solenoid the lines are parallel, evenly spaced and all one "
               "way — a uniform field.",
    },
    {
        "id": "ks4-electromagnetism-s01",
        "subtopic_slug": "electromagnetism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student wants a stronger electromagnet but must keep the "
                "same power supply and the same core. Determine which change "
                "would work.",
        "options": [
            "Wind more turns of wire onto the core",
            "Spread the same number of turns along a longer piece of the core",
            "Replace the copper wire with the same length of plastic-coated "
            "string",
            "Reverse the direction of the current flowing through the coil",
        ],
        "correct_index": 0,
        "why": "A solenoid's field grows with the number of turns, because "
               "each extra turn adds its own field along the same axis.",
    },
    {
        "id": "ks4-electromagnetism-s02",
        "subtopic_slug": "electromagnetism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A compass rests on a bench beside a wire. Explain why the "
                "needle swings round when the current in the wire is switched "
                "on.",
        "options": [
            "The current heats the wire, and the rising warm air pushes the "
            "needle round",
            "The current gives the wire an electric charge, and this charge "
            "then attracts the metal needle",
            "The current produces a magnetic field around the wire, which "
            "the needle lines up with",
            "The current magnetises the compass needle so that it lies along "
            "the wire",
        ],
        "correct_index": 2,
        "why": "This is Oersted's discovery: a current always creates a "
               "magnetic field around the conductor, and a compass lines "
               "itself up with it.",
    },
    {
        "id": "ks4-electromagnetism-s03",
        "subtopic_slug": "electromagnetism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric bell uses an electromagnet to move its striker. "
                "Explain why an electromagnet is used rather than a permanent "
                "magnet.",
        "options": [
            "A permanent magnet would be far too heavy for the striker to "
            "carry",
            "The electromagnet can be switched off and on again and again, "
            "so the striker keeps striking",
            "A permanent magnet would pull the striker in the wrong "
            "direction, away from the bell dome entirely",
            "The electromagnet transfers much less energy overall than a "
            "permanent magnet does",
        ],
        "correct_index": 1,
        "why": "A bell works by breaking and remaking its own circuit, and "
               "only an electromagnet's field switches off when that circuit "
               "breaks.",
    },
    {
        "id": "ks4-electromagnetism-s04",
        "subtopic_slug": "electromagnetism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A solenoid is viewed end-on, and the conventional current is "
                "seen to flow anticlockwise around the coil. State which pole "
                "faces the observer.",
        "options": [
            "A south pole, because an anticlockwise current marks the "
            "negative end of a coil",
            "A south pole, because conventional current always leaves a coil "
            "at its south end",
            "Neither pole, because a solenoid's field lies entirely inside it",
            "A north pole, because an anticlockwise current seen end-on marks "
            "the north end",
        ],
        "correct_index": 3,
        "why": "Viewed end-on, an anticlockwise conventional current gives a "
               "north pole facing you; a clockwise one gives a south pole.",
    },
    {
        "id": "ks4-electromagnetism-h01",
        "subtopic_slug": "electromagnetism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Investigating an electromagnet, a student finds it holds 6 "
                "paper clips with 20 turns and 11 clips with 40 turns, both "
                "at 2.0 A. They then use 60 turns but at 1.0 A, and it holds "
                "7 clips. Explain why this last result cannot be used to "
                "judge the effect of the number of turns.",
        "options": [
            "Because 60 turns lies outside the range over which a solenoid "
            "can be tested",
            "Because paper clips are made of steel, and steel cannot be "
            "picked up by an electromagnet",
            "Because two variables were changed at once, so the fall cannot "
            "be blamed on either one",
            "Because the number of clips held is not related to the strength "
            "of the field",
        ],
        "correct_index": 2,
        "why": "Only one variable may change at a time — with both the turns "
               "and the current altered, the result cannot show what either "
               "of them did.",
    },
    {
        "id": "ks4-electromagnetism-h02",
        "subtopic_slug": "electromagnetism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A relay uses an electromagnet to pull a switch contact "
                "closed. When the coil current is switched off the contact "
                "does not spring open again. Suggest the most likely cause.",
        "options": [
            "The current used was too large, so the coil has kept some of "
            "its charge",
            "The coil has too many turns, so its field is unable to fall to "
            "zero",
            "The contact is made of aluminium, and aluminium stays stuck to "
            "a magnet with no current",
            "The core is a hard material such as steel, so it stayed "
            "magnetised",
        ],
        "correct_index": 3,
        "why": "Only a soft material such as iron loses its induced "
               "magnetism when the field is removed; a hard core keeps its "
               "magnetism and holds the contact closed.",
    },
    {
        "id": "ks4-electromagnetism-h03",
        "subtopic_slug": "electromagnetism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the magnetic field of a single straight wire with "
                "that of the same wire wound into a solenoid, both carrying "
                "the same current.",
        "options": [
            "The solenoid's field is far stronger inside the coil, where the "
            "turns' fields add up",
            "The two fields are equally strong, because the same current "
            "flows in the same length of wire",
            "The straight wire's field is stronger, because coiling the wire "
            "makes the turns' fields cancel",
            "The solenoid's field is stronger only outside the coil, since "
            "inside the coil the field is zero",
        ],
        "correct_index": 0,
        "why": "Winding the wire brings many turns' circular fields into "
               "line, and inside the coil they add together to give a strong, "
               "uniform field.",
    },
    {
        "id": "ks4-electromagnetism-h04",
        "subtopic_slug": "electromagnetism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A circuit breaker contains an electromagnet in series with "
                "the appliance it protects. Explain how it cuts off the "
                "current when the current becomes dangerously large.",
        "options": [
            "The large current heats the coil until the wire inside melts and "
            "the circuit is opened",
            "The large current makes the electromagnet strong enough to pull "
            "the switch open",
            "The large current reverses the polarity of the electromagnet, "
            "which then repels the switch shut",
            "The large current demagnetises the iron core, and a "
            "spring-loaded switch is released",
        ],
        "correct_index": 1,
        "why": "Field strength rises with current, so above a set current the "
               "electromagnet can pull the contacts apart — and breaking the "
               "circuit removes the current that created the field.",
    },

    # ── flemings-left-hand-rule ────────────────── HIGHER TIER (6.7.2.2) ──
    {
        "id": "ks4-flemings-left-hand-rule-e01",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "A current-carrying wire in a magnetic field feels a force. "
                "State what happens to the direction of that force if BOTH "
                "the current and the magnetic field are reversed.",
        "options": [
            "It is unchanged, because reversing both of them reverses the "
            "force twice",
            "It reverses, because reversing the current always reverses the "
            "force",
            "It reverses, because reversing the field always reverses the "
            "force",
            "It falls to zero, because the two reversals cancel the force "
            "out",
        ],
        "correct_index": 0,
        "why": "Reversing either the current or the field on its own "
               "reverses the force, so reversing both puts the force back "
               "the way it started.",
    },
    {
        "id": "ks4-flemings-left-hand-rule-e02",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the unit of magnetic flux density, B, in the equation "
                "F = BIl.",
        "options": [
            "The newton, N",
            "The ampere, A",
            "The newton per ampere squared, N/A²",
            "The tesla, T",
        ],
        "correct_index": 3,
        "why": "Magnetic flux density is measured in tesla (T); the force is "
               "in newtons, the current in amperes and the length in metres.",
    },
    {
        "id": "ks4-flemings-left-hand-rule-e03",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "A wire of length 0.50 m carries a current of 3.0 A at right "
                "angles to a magnetic field of flux density 0.20 T. Calculate "
                "the force on the wire.",
        "options": [
            "0.60 N",
            "0.30 N",
            "1.2 N",
            "3.7 N",
        ],
        "correct_index": 1,
        "why": "F = BIl = 0.20 T x 3.0 A x 0.50 m = 0.30 N.",
    },
    {
        "id": "ks4-flemings-left-hand-rule-e04",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the condition under which the force on a "
                "current-carrying conductor in a magnetic field is at its "
                "greatest.",
        "options": [
            "When the conductor lies parallel to the field lines",
            "When the conductor is made of iron rather than of copper",
            "When the conductor lies at right angles to the field lines",
            "When the conductor lies at 45 degrees to the field lines",
        ],
        "correct_index": 2,
        "why": "The motor-effect force is largest when the current runs "
               "perpendicular to the field, and falls to zero when the wire "
               "lies along it.",
    },
    {
        "id": "ks4-flemings-left-hand-rule-s01",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A straight wire is held vertically and carries a "
                "conventional current vertically downwards. The magnetic "
                "field at the wire is horizontal and points due north. "
                "Determine the direction of the force on the wire.",
        "options": [
            "Vertically upwards, opposite to the current",
            "Horizontally, towards the west",
            "Horizontally, towards the east",
            "Horizontally, towards the north, along the field",
        ],
        "correct_index": 2,
        "why": "First finger north for the field and second finger downwards "
               "for the current leaves the left thumb pointing east, at "
               "right angles to them both.",
    },
    {
        "id": "ks4-flemings-left-hand-rule-s02",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A wire carrying a current of 4.0 A lies at right angles to a "
                "magnetic field of flux density 0.15 T, and the force on it "
                "is 0.36 N. Calculate the length of wire that is in the "
                "field.",
        "options": [
            "2.4 m",
            "0.60 m",
            "0.22 m",
            "0.090 m",
        ],
        "correct_index": 1,
        "why": "Rearranging F = BIl gives l = F / (B x I) = 0.36 N / (0.15 T "
               "x 4.0 A) = 0.60 m.",
    },
    {
        "id": "ks4-flemings-left-hand-rule-s03",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A student uses their right hand to work out the direction of "
                "the force on a current-carrying wire in a motor. Explain "
                "what is wrong with this.",
        "options": [
            "Nothing is wrong, because either hand gives the same answer once "
            "the fingers are at right angles",
            "The right hand is correct here, but only for a wire carrying "
            "alternating current",
            "The right hand is for the motor effect and the left for the "
            "generator effect, so the two are simply named the wrong way "
            "round",
            "The right hand is the generator rule, so using it here gives a "
            "force in exactly the opposite direction to the true one",
        ],
        "correct_index": 3,
        "why": "The left hand is the motor rule — a current in a field giving "
               "a force; the right hand is for induced current in a "
               "generator, and it points the answer the opposite way.",
    },
    {
        "id": "ks4-flemings-left-hand-rule-s04",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A wire carries a conventional current vertically upwards "
                "between the poles of a magnet, whose field points "
                "horizontally towards the west. Determine the direction of "
                "the force on the wire.",
        "options": [
            "Horizontally, towards the south",
            "Horizontally, towards the north",
            "Vertically downwards, opposite to the current",
            "Horizontally, towards the east, opposite to the field",
        ],
        "correct_index": 0,
        "why": "First finger west for the field and second finger upwards for "
               "the current leaves the left thumb pointing south, at right "
               "angles to them both.",
    },
    {
        "id": "ks4-flemings-left-hand-rule-h01",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A wire of length 8.0 cm carries a current of 2.5 A at right "
                "angles to a magnetic field of flux density 0.40 T. Calculate "
                "the force on the wire.",
        "options": [
            "8.0 N",
            "0.080 N",
            "0.80 N",
            "0.0080 N",
        ],
        "correct_index": 1,
        "why": "The length has to be in metres: F = BIl = 0.40 T x 2.5 A x "
               "0.080 m = 0.080 N.",
    },
    {
        "id": "ks4-flemings-left-hand-rule-h02",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Two wires lie at right angles to the same 0.30 T field. Wire "
                "P carries 6.0 A and has 4.0 cm in the field; wire Q carries "
                "3.0 A and has 10 cm in the field. Compare the forces on "
                "them.",
        "options": [
            "The force on Q is the larger, at 0.090 N against 0.072 N on P",
            "The force on P is the larger, because it carries twice the "
            "current that Q carries",
            "The forces are equal, because P has twice the current while Q "
            "has 2.5 times the length",
            "The force on Q is the larger, at 9.0 N against 7.2 N on P",
        ],
        "correct_index": 0,
        "why": "F = BIl for each: P gives 0.30 x 6.0 x 0.040 = 0.072 N and Q "
               "gives 0.30 x 3.0 x 0.100 = 0.090 N, so the longer wire wins "
               "despite its smaller current.",
    },
    {
        "id": "ks4-flemings-left-hand-rule-h03",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A wire carrying a conventional current due north lies in a "
                "magnetic field that also points due north. Predict the force "
                "on the wire and explain your answer.",
        "options": [
            "The force is a maximum, because the current and the field point "
            "the same way and so add together",
            "The force acts vertically upwards, because the left thumb always "
            "points up when field and current agree",
            "There is no force, because the current runs parallel to the "
            "field instead of across it",
            "The force acts due east, at right angles to both the current and "
            "the field",
        ],
        "correct_index": 2,
        "why": "The motor effect needs the current to cut across the field, "
               "so a conductor lying along the field lines feels no force at "
               "all.",
    },
    {
        "id": "ks4-flemings-left-hand-rule-h04",
        "subtopic_slug": "flemings-left-hand-rule",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A student writes: 'If I double the current and halve the "
                "length of wire in the field, the force must double, because "
                "current matters more than length.' Evaluate this statement.",
        "options": [
            "Correct — the force doubles, because F depends on the current "
            "squared but only on the length itself",
            "Incorrect — the force halves, because the length of wire in the "
            "field matters more than the current",
            "Incorrect — the force quadruples, because shortening the wire "
            "and raising the current both increase it",
            "Incorrect — the force is unchanged, because F = BIl depends on "
            "the product I x l, which has not altered",
        ],
        "correct_index": 3,
        "why": "In F = BIl the current and the length are multiplied "
               "together, so doubling one while halving the other leaves the "
               "product, and therefore the force, exactly as it was.",
    },

    # ── electric-motors ────────────────────────── HIGHER TIER (6.7.2.3) ──
    {
        "id": "ks4-electric-motors-e01",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the energy transfer that takes place in an electric "
                "motor while it is running.",
        "options": [
            "From a kinetic store to an electrical store",
            "From a chemical store to a thermal store",
            "From an electrical store to a kinetic store",
            "From a magnetic store to a chemical store",
        ],
        "correct_index": 2,
        "why": "A motor turns electrical working into rotation, so energy is "
               "shifted from an electrical store to the kinetic store of the "
               "spinning coil.",
    },
    {
        "id": "ks4-electric-motors-e02",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the name of the fixed carbon contacts that carry the "
                "current to the rotating coil of a DC motor.",
        "options": [
            "The armature",
            "The split-ring commutator",
            "The solenoid",
            "The brushes",
        ],
        "correct_index": 3,
        "why": "The brushes are stationary contacts pressing on the turning "
               "commutator, so that current can reach a coil which is "
               "spinning.",
    },
    {
        "id": "ks4-electric-motors-e03",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the equation that gives the size of the force on one "
                "side of a motor's coil.",
        "options": [
            "F = B I l",
            "F = B / (I l)",
            "F = I l / B",
            "F = B I l squared",
        ],
        "correct_index": 0,
        "why": "Each side of the coil is a current-carrying conductor sitting "
               "in a magnetic field, so the motor-effect force on it is "
               "F = BIl.",
    },
    {
        "id": "ks4-electric-motors-e04",
        "subtopic_slug": "electric-motors",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what happens to the direction a DC motor's coil turns "
                "if the two connections to the power supply are swapped over.",
        "options": [
            "It keeps turning the same way, because the commutator corrects "
            "the reversal",
            "It turns the other way, because reversing the current reverses "
            "each force",
            "It stops turning, because the current now opposes the magnetic "
            "field",
            "It turns the same way but faster, because the current is now in "
            "its natural direction",
        ],
        "correct_index": 1,
        "why": "Reversing the current reverses the motor-effect force on each "
               "side of the coil, so the turning effect acts the opposite way "
               "round.",
    },
    {
        "id": "ks4-electric-motors-s01",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why the two long sides of a motor's coil experience "
                "forces in opposite directions.",
        "options": [
            "One side sits in the north pole's field and the other in the "
            "south pole's, so the fields oppose",
            "The current runs in opposite directions along the two sides, so "
            "the left-hand rule gives opposite forces",
            "One side is closer to the magnet than the other, so the field "
            "acting on it is stronger",
            "The commutator allows current to flow along only one side of the "
            "coil at a time",
        ],
        "correct_index": 1,
        "why": "Current goes up one side of the loop and back down the other, "
               "and reversing the current in the same field reverses the "
               "direction of the force.",
    },
    {
        "id": "ks4-electric-motors-s02",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Determine which change would make a DC motor turn faster.",
        "options": [
            "Winding more turns of wire onto the coil",
            "Fitting a weaker pair of permanent magnets",
            "Adding extra resistance in series with the coil",
            "Replacing the iron core inside the coil with a plastic one",
        ],
        "correct_index": 0,
        "why": "Every extra turn adds another BIl force at the same distance "
               "from the axle, so the total turning effect, and the speed, "
               "goes up.",
    },
    {
        "id": "ks4-electric-motors-s03",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "A motor is built with a complete ring instead of a split "
                "ring. Predict what its coil does when the current is "
                "switched on.",
        "options": [
            "It turns continuously, but much more slowly than it would with "
            "a proper split ring fitted",
            "It does not move at all, because no current can reach the coil",
            "It turns continuously, but in the opposite direction to normal",
            "It rocks back and forth instead of turning, because the current "
            "in it never reverses",
        ],
        "correct_index": 3,
        "why": "With no split, the current keeps the same direction in the "
               "coil, so past the upright position the force pushes the coil "
               "back again instead of round.",
    },
    {
        "id": "ks4-electric-motors-s04",
        "subtopic_slug": "electric-motors",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why real DC motors use many coils wound at different "
                "angles on an iron armature, rather than one single coil.",
        "options": [
            "It lets the motor run from an alternating supply as well as from "
            "a direct one",
            "It stops the coils overheating, by sharing the current between "
            "them",
            "As one coil reaches its weakest position another is well placed "
            "to push",
            "It removes the need for a commutator, because the coils reverse "
            "each other's current",
        ],
        "correct_index": 2,
        "why": "A single coil gives no turning effect at the upright "
               "position, so several coils set at different angles keep one "
               "of them always well placed to push.",
    },
    {
        "id": "ks4-electric-motors-h01",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A motor's coil has 50 turns. Each turn has a side of length "
                "6.0 cm in a magnetic field of flux density 0.25 T, and the "
                "coil carries a current of 1.2 A. Calculate the total force "
                "on one side of the coil.",
        "options": [
            "0.018 N",
            "90 N",
            "1.8 N",
            "0.90 N",
        ],
        "correct_index": 3,
        "why": "One turn gives BIl = 0.25 x 1.2 x 0.060 = 0.018 N, and the 50 "
               "turns together give 50 x 0.018 = 0.90 N.",
    },
    {
        "id": "ks4-electric-motors-h02",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A student claims that a DC motor's coil is pushed round with "
                "the same turning effect at every point in its rotation. "
                "Evaluate this claim.",
        "options": [
            "Correct — the forces on the two sides are always equal and "
            "opposite, so the turning effect never changes",
            "Correct — the commutator holds the turning effect constant "
            "throughout each rotation",
            "Incorrect — the turning effect falls to zero where the two "
            "forces act along the plane of the coil, and momentum carries the "
            "coil past",
            "Incorrect — the turning effect falls to zero twice a turn "
            "because the commutator cuts the current, and the coil is then "
            "pushed backwards",
        ],
        "correct_index": 2,
        "why": "The two forces stay the same size, but their turning effect "
               "depends on where the coil is and vanishes when they no longer "
               "act to rotate it.",
    },
    {
        "id": "ks4-electric-motors-h03",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "An electric motor is 92% efficient and a petrol engine is "
                "30% efficient. Compare the input energy each needs to "
                "deliver the same useful output.",
        "options": [
            "The engine needs about 0.62 times the input energy the motor "
            "needs",
            "The engine needs about 3 times the input energy the motor needs",
            "The engine needs about 62% more input energy than the motor "
            "needs",
            "Both need the same input energy, and only the energy wasted is "
            "different",
        ],
        "correct_index": 1,
        "why": "Input = useful output / efficiency, so for one unit of useful "
               "output the engine needs 1 / 0.30 = 3.3 units against the "
               "motor's 1 / 0.92 = 1.1 units.",
    },
    {
        "id": "ks4-electric-motors-h04",
        "subtopic_slug": "electric-motors",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A designer can raise a motor's turning effect either by "
                "increasing the current or by adding more turns to the coil. "
                "Suggest one disadvantage of increasing the current.",
        "options": [
            "A larger current heats the coil more, wasting energy and risking "
            "damage to the insulation",
            "A larger current reverses the direction of the force acting on "
            "the coil",
            "A larger current weakens the permanent magnets, so the force "
            "falls again",
            "A larger current prevents the commutator from reversing the "
            "current each half turn",
        ],
        "correct_index": 0,
        "why": "Heating in a resistance rises steeply with current, so a "
               "bigger current wastes more energy as thermal energy in the "
               "coil and runs the motor hotter.",
    },
]
