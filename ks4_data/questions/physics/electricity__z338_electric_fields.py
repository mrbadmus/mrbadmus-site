"""Physics · Electricity — the MRB-338 expansion of `electric-fields` (triple-only).

AQA 8463 §6.2.6, physics only. The twelve baseline rows in `electricity__b.py`
establish the definition of a field, the spacing-means-strength rule, the
never-cross rule, the unit N/C, two of the three rearrangements of E = F ÷ q,
the electron-in-a-field case and the opposite-charge pair. The weight here
falls on the material those rows leave untouched: the four field-line PATTERNS
stated in words (single positive, single negative, two like charges, the
uniform field between parallel plates), the missing rearrangement q = F ÷ E,
and the discharge sequence — ionisation, the spark, lightning and the static
hazards that follow from it.

`easier` stays at eight because the remaining pure recall is small: the four
patterns, the equation itself, the non-contact classification and what a strong
field does to air. `standard` and `harder` carry the rest, because almost
everything left in this subtopic is either a rearranged calculation or a claim
that has to be evaluated against a named charge configuration.
"""

TOPIC = "electricity"
SUBJECT = "physics"

QUESTIONS = [
    # ── easier ───────────────────────────────────────────────────────────
    {
        "id": "ks4-electric-fields-e05",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe the pattern of the electric field lines around a "
                "single positive point charge.",
        "options": [
            "They radiate straight outwards in all directions away from the charge",
            "They point straight inwards towards the charge from every direction",
            "They form closed circles around the charge, as magnetic lines do",
            "They run parallel to one another and are equally spaced apart",
        ],
        "correct_index": 0,
        "why": "Field lines show the direction a positive charge would be "
               "pushed, so around a positive charge they point away from it in "
               "every direction.",
    },
    {
        "id": "ks4-electric-fields-e06",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A single negative point charge sits on its own. State which "
                "way its field lines point.",
        "options": [
            "Inwards, towards the charge from every direction",
            "Outwards, away from the charge in every direction",
            "Sideways, in closed circles drawn around the charge",
            "Nowhere, because only positive charges have field lines",
        ],
        "correct_index": 0,
        "why": "A positive charge placed nearby would be pulled towards a "
               "negative charge, so the lines point inwards.",
    },
    {
        "id": "ks4-electric-fields-e07",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to air that is placed in a very strong "
                "electric field.",
        "options": [
            "It melts under the heat of the field and turns into a thin conducting liquid film",
            "It is ionised, and the ionised air conducts electricity",
            "It is pushed out of the gap, leaving a vacuum behind it",
            "It becomes an even better insulator than it was before",
        ],
        "correct_index": 1,
        "why": "A strong enough field strips electrons from air molecules, and "
               "the ions and free electrons left behind let the air conduct.",
    },
    {
        "id": "ks4-electric-fields-e08",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the family of forces to which the force between two "
                "charged objects belongs.",
        "options": [
            "Non-contact forces, like magnetic and gravitational forces",
            "Contact forces, like friction and air resistance",
            "Balanced forces, which act in equal and opposite pairs",
            "Turning forces, which act about a fixed pivot point",
        ],
        "correct_index": 0,
        "why": "Charged objects push and pull each other through their "
               "electric fields without touching, exactly as magnets and "
               "masses do.",
    },
    {
        "id": "ks4-electric-fields-e09",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "The dome of a Van de Graaff generator produces an electric "
                "field of strength 200 N/C at a nearby point. Determine "
                "the force this exerts on a charge of 0.50 C placed "
                "there.",
        "options": [
            "0.0025 N",
            "400 N",
            "100 N",
            "200 N",
        ],
        "correct_index": 2,
        "why": "E = F ÷ q rearranges to F = E × q = 200 × 0.50 = 100 N.",
    },
    {
        "id": "ks4-electric-fields-e10",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two flat metal plates, one positive and one negative, face "
                "each other. State what the field lines in the gap between "
                "them look like.",
        "options": [
            "Radiating outwards in all directions from a point in the middle of the gap",
            "Parallel and equally spaced, running from the positive plate to the negative plate",
            "Bunched close together near the positive plate and far apart near the negative one",
            "Curved, arcing from the edge of one plate around to the edge of the other one",
        ],
        "correct_index": 1,
        "why": "Parallel charged plates produce a uniform field: the lines are "
               "parallel and evenly spaced, so the field has the same strength "
               "everywhere between them.",
    },
    {
        "id": "ks4-electric-fields-e11",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the equation that links electric field strength E, "
                "force F and charge q.",
        "options": [
            "E = F × q",
            "E = q ÷ F",
            "F = q ÷ E",
            "E = F ÷ q",
        ],
        "correct_index": 3,
        "why": "Electric field strength is the force per unit charge, so the "
               "force is divided by the charge: E = F ÷ q.",
    },
    {
        "id": "ks4-electric-fields-e12",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two positive charges are held a short distance apart. "
                "Describe the field lines in the region between them.",
        "options": [
            "They run straight across the gap from one charge to the other",
            "They form closed loops that circle around both charges together",
            "They curve away from each other instead of meeting in the gap",
            "They are parallel and equally spaced right across the whole gap",
        ],
        "correct_index": 2,
        "why": "Both charges push a positive test charge away, so the lines "
               "bend apart rather than joining one charge to the other.",
    },

    # ── standard ─────────────────────────────────────────────────────────
    {
        "id": "ks4-electric-fields-s05",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Inside a photocopier, a toner particle carrying a charge of "
                "5.0 × 10⁻⁸ C experiences a force of 2.0 × 10⁻⁵ N. Calculate "
                "the electric field strength at that point.",
        "options": [
            "2.5 × 10⁻³ N/C",
            "1.0 × 10⁻¹² N/C",
            "4000 N/C",
            "400 N/C",
        ],
        "correct_index": 3,
        "why": "E = F ÷ q = 2.0 × 10⁻⁵ ÷ 5.0 × 10⁻⁸ = 400 N/C.",
    },
    {
        "id": "ks4-electric-fields-s06",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An ink droplet carrying a charge of 8.0 × 10⁻¹¹ C passes "
                "through a uniform electric field of strength 2.5 × 10⁵ N/C "
                "inside an inkjet printer. Calculate the electric force on "
                "the droplet.",
        "options": [
            "2.0 × 10⁻⁵ N",
            "3.1 × 10¹⁵ N",
            "3.2 × 10⁻¹⁶ N",
            "2.0 × 10⁻⁶ N",
        ],
        "correct_index": 0,
        "why": "F = E × q = 2.5 × 10⁵ × 8.0 × 10⁻¹¹ = 2.0 × 10⁻⁵ N.",
    },
    {
        "id": "ks4-electric-fields-s07",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In an industrial electrostatic precipitator, a charged dust "
                "particle experiences a force of 0.90 N within a field of "
                "strength 250 N/C. Work out the charge carried by the "
                "particle.",
        "options": [
            "0.036 C",
            "0.0036 C",
            "225 C",
            "280 C",
        ],
        "correct_index": 1,
        "why": "E = F ÷ q rearranges to q = F ÷ E = 0.90 ÷ 250 = 0.0036 C.",
    },
    {
        "id": "ks4-electric-fields-s08",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe the two things that a set of electric field lines "
                "tells you about a field.",
        "options": [
            "The size of the charge on the object, and the length of time the field has existed",
            "The exact path that a charge will follow, and the speed it travels along that path",
            "The direction of the force on a positive charge, and the strength of the field from their spacing",
            "The energy stored in the field, and the size of the current that would flow in it",
        ],
        "correct_index": 2,
        "why": "The arrows give the direction a positive charge would be "
               "pushed, and the spacing gives the strength — closer lines mean "
               "a stronger field.",
    },
    {
        "id": "ks4-electric-fields-s09",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A proton and an electron are released from rest at the same "
                "point in a uniform electric field. Compare the directions in "
                "which the two particles move.",
        "options": [
            "They move in the same direction, because the field at that point can only point one way",
            "Only the proton moves, because an electric field pushes positive charges and ignores negative ones",
            "Only the electron moves, because it is far lighter and a field acts on the lighter charge",
            "They move in opposite directions, because the field pushes positive and negative charges opposite ways",
        ],
        "correct_index": 3,
        "why": "A positive charge is pushed along the field lines and a "
               "negative charge is pushed the opposite way, so the proton and "
               "electron separate.",
    },
    {
        "id": "ks4-electric-fields-s10",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A single positive point charge is held on an insulating "
                "stand. Compare the strength of its electric field at a point "
                "2 cm from it with the strength at a point 6 cm from it.",
        "options": [
            "It is stronger at 2 cm, because the field lines are closer together nearer the charge",
            "It is stronger at 6 cm, because the lines have had further to spread and gather there",
            "It is the same at both points, because the charge on the stand has not been altered",
            "It is zero at 6 cm, because the field of a point charge stops a few centimetres out",
        ],
        "correct_index": 0,
        "why": "The lines spread apart as they move outwards, so they are "
               "closest — and the field strongest — near the charge.",
    },
    {
        "id": "ks4-electric-fields-s11",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the field line pattern between two oppositely charged "
                "parallel plates with the pattern around a single positive "
                "point charge.",
        "options": [
            "Both patterns are parallel and equally spaced, because every electric field has one shape",
            "Between the plates the lines are parallel and evenly spaced; around the point charge they radiate outwards",
            "Between the plates the lines radiate outwards; around the point charge they are parallel and evenly spaced",
            "Between the plates the lines form closed loops; around the point charge they run from side to side",
        ],
        "correct_index": 1,
        "why": "Parallel plates give a uniform field of evenly spaced lines, "
               "while a point charge gives a radial field whose lines spread "
               "apart with distance.",
    },
    {
        "id": "ks4-electric-fields-s12",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student draws the electric field between a positive charge "
                "and a negative charge, and labels the lines as running from "
                "north to south. Explain what is wrong with the labels.",
        "options": [
            "Nothing is wrong, because electric field lines follow exactly the same rule as magnetic ones",
            "The labels are the wrong way round, because electric field lines run from south across to north",
            "North and south are magnetic poles; electric field lines run from the positive charge to the negative",
            "The labels should be taken off altogether, because electric field lines have no direction at all",
        ],
        "correct_index": 2,
        "why": "Poles belong to magnets. A charge configuration has positive "
               "and negative ends, and the lines run from the positive charge "
               "to the negative one.",
    },
    {
        "id": "ks4-electric-fields-s13",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A charged plastic rod is held near a small charged ball "
                "without touching it, and the ball is pushed away. Explain how "
                "the rod exerts a force on the ball across the gap.",
        "options": [
            "Air molecules are pushed from the rod across to the ball, carrying the force over the gap",
            "Charge leaks steadily from the rod to the ball through the air, and the flow drives them apart",
            "The rod has to touch the ball for a moment first, so a gap means that no force can act",
            "The rod sets up an electric field around itself, and the ball feels a force wherever it sits in it",
        ],
        "correct_index": 3,
        "why": "The electric force is a non-contact force: the rod's field "
               "fills the space around it, and any charge in that space feels "
               "a force.",
    },
    {
        "id": "ks4-electric-fields-s14",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A metal sphere on an insulating stand is charged more and "
                "more. No spark occurs at first, but one suddenly jumps across "
                "to a nearby earthed object. Explain why the spark happens "
                "only then.",
        "options": [
            "The field has to be strong enough to ionise the air, and only a large enough charge makes it so",
            "The air in the gap has to be heated until it melts, and heating it up takes time to happen",
            "The sphere can only hold a fixed amount of charge, and it overflows once it has been filled",
            "The earthed object has to build up a charge of its own first, and collecting it takes time",
        ],
        "correct_index": 0,
        "why": "More charge means a stronger field in the gap; once the field "
               "is strong enough to ionise the air, the ionised air conducts "
               "and a spark jumps.",
    },
    {
        "id": "ks4-electric-fields-s15",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A person slides across a car seat and feels a small shock "
                "when their hand comes near the metal door handle. Explain why "
                "the shock happens.",
        "options": [
            "The car battery pushes a current through the handle whenever it is touched from inside",
            "Sliding leaves the person charged, and the charge crosses to the earthed metal as a spark",
            "Friction warms the person's hand, and the warm air conducts once it reaches the handle",
            "The seat magnetises the person as they slide, and the magnetism drives charge to their hand",
        ],
        "correct_index": 1,
        "why": "Friction charges the person; bringing that charge near an "
               "earthed conductor makes the field in the gap strong enough for "
               "a discharge.",
    },
    {
        "id": "ks4-electric-fields-s16",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe why the air between a storm cloud and the ground, "
                "which is normally an insulator, suddenly conducts during a "
                "lightning strike.",
        "options": [
            "Falling raindrops join into a continuous wire of water reaching from the cloud to the ground",
            "Charge moving fast enough passes straight through any insulator, and cloud charge moves fast",
            "Charge builds up in the cloud until the field is enormous, and that field ionises the air",
            "Thunder shakes the air molecules apart first, opening a path for the charge to follow down",
        ],
        "correct_index": 2,
        "why": "The huge charge separation makes the field between cloud and "
               "ground so strong that the air breaks down and a conducting "
               "channel forms.",
    },
    {
        "id": "ks4-electric-fields-s17",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A metal rod is fixed to the top of a building but its lower "
                "end is not connected to the ground. Explain why the rod does "
                "not protect the building.",
        "options": [
            "The rod has to be made of iron rather than copper before any charge can travel along it",
            "The rod takes in more charge than it can hold and then releases it into the building again",
            "The rod has no electric field of its own, so no charge can ever be drawn towards it",
            "Charge reaching the rod has no path to the earth, so it cannot flow safely away",
        ],
        "correct_index": 3,
        "why": "The protection comes from a low-resistance route to earth; an "
               "unconnected rod gives the charge nowhere to go.",
    },
    {
        "id": "ks4-electric-fields-s18",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The electric field strength at a point is 250 N/C. State what "
                "this tells you about the force at that point.",
        "options": [
            "A charge of 1 C placed there would experience a force of 250 N",
            "A charge of 250 C placed there would experience a force of 1 N",
            "Any charge placed there experiences a force of 250 N, whatever its size",
            "The field transfers 250 J of energy to each coulomb of charge passing",
        ],
        "correct_index": 0,
        "why": "Field strength is force per unit charge, so 250 N/C means 250 N "
               "of force on every coulomb of charge placed there.",
    },
    {
        "id": "ks4-electric-fields-s19",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says that the electric field between two parallel "
                "charged plates is strongest close to the positive plate. "
                "Explain why this is wrong.",
        "options": [
            "The field is strongest close to the negative plate, because that is where the lines end up",
            "The lines between the plates are equally spaced, so the field has the same strength throughout",
            "The field is strongest exactly halfway across, because the lines from both plates meet there",
            "There is no field between the plates at all, because the two charges cancel one another out",
        ],
        "correct_index": 1,
        "why": "A uniform field has parallel, evenly spaced lines, so its "
               "strength does not vary from one side of the gap to the other.",
    },
    {
        "id": "ks4-electric-fields-s20",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A charged metal object has a sharp spike on one side and a "
                "smooth rounded surface elsewhere. State where the electric "
                "field around the object is strongest.",
        "options": [
            "At the rounded surface, because a curved surface spreads its charge over a greater area",
            "Equally strong everywhere around it, because the object carries a single amount of charge",
            "At the spike, because charge gathers most closely on a sharply curved part of the surface",
            "Midway between the spike and the rounded side, where the fields from the two parts meet",
        ],
        "correct_index": 2,
        "why": "Charge concentrates at sharp points, so the field lines are "
               "packed most closely there and the field is at its strongest.",
    },
    {
        "id": "ks4-electric-fields-s21",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pair of parallel plates is set up with the positive plate "
                "on the left and the negative plate on the right. A small "
                "positive charge is released midway between them. State the "
                "direction in which it begins to move.",
        "options": [
            "Towards the left, because a positive charge is pulled back towards the positive plate",
            "It stays still, because it is exactly the same distance from each of the two plates",
            "Along the gap, parallel to the plates, because the field runs that way between them",
            "Towards the right, because the force on a positive charge acts from positive to negative",
        ],
        "correct_index": 3,
        "why": "The field runs from the positive plate to the negative plate, "
               "and a positive charge is pushed along the field, so it "
               "accelerates to the right.",
    },
    {
        "id": "ks4-electric-fields-s22",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what happens to the electric field around a charged "
                "metal sphere if the charge on the sphere is doubled.",
        "options": [
            "The field becomes stronger everywhere around it, but its shape and direction do not change",
            "The field becomes stronger only at the surface, because the extra charge all stays there",
            "The field reaches twice as far out, but has the same strength at each point it already had",
            "The field keeps the same strength, but each line is drawn twice as long to show the charge",
        ],
        "correct_index": 0,
        "why": "More charge on the sphere means a larger force on any charge "
               "placed nearby, so the field is stronger at every point while "
               "the radial pattern stays the same.",
    },
    {
        "id": "ks4-electric-fields-s23",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In an electrostatic spray gun, a paint droplet carrying a "
                "charge of 40 µC experiences a force of 0.80 N. Calculate the "
                "electric field strength acting on the droplet.",
        "options": [
            "50 N/C",
            "20 000 N/C",
            "0.020 N/C",
            "3.2 × 10⁻⁵ N/C",
        ],
        "correct_index": 1,
        "why": "40 µC = 4.0 × 10⁻⁵ C, so E = F ÷ q = 0.80 ÷ 4.0 × 10⁻⁵ = "
               "20 000 N/C.",
    },
    {
        "id": "ks4-electric-fields-s24",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says that only positively charged objects have an "
                "electric field around them. Explain the error.",
        "options": [
            "Only negatively charged objects have a field, because electrons are the charges that move",
            "Neither has a field on its own; a field exists once two charged objects are brought near",
            "Any charged object has a field; around a negative charge the lines point inwards instead",
            "Both have a field, but the field around a negative object is too weak to act on anything",
        ],
        "correct_index": 2,
        "why": "A field surrounds any charged object. The sign of the charge "
               "changes the direction of the lines, not whether a field exists.",
    },
    {
        "id": "ks4-electric-fields-s25",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe the shape of the electric field lines in the region "
                "between a positive point charge and a nearby negative point "
                "charge.",
        "options": [
            "They form closed loops that circle around each of the two charges in turn",
            "They radiate straight outwards from both charges and never meet in the gap",
            "They arc across the gap from the negative charge towards the positive charge",
            "They arc across the gap from the positive charge towards the negative charge",
        ],
        "correct_index": 3,
        "why": "Field lines start on positive charge and end on negative "
               "charge, so between an opposite pair they curve across from the "
               "positive one to the negative one.",
    },
    {
        "id": "ks4-electric-fields-s26",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student finds the electric field strength at a point by "
                "multiplying the force on a charge by the size of that charge. "
                "Explain the error.",
        "options": [
            "Field strength is force per unit charge, so the force is divided by the charge",
            "Field strength is charge per unit force, so the charge is divided by the force instead",
            "Field strength is the force added to the charge, so the two values are summed together",
            "Field strength is the force on its own, so the charge should not be used in it at all",
        ],
        "correct_index": 0,
        "why": "E = F ÷ q. Multiplying would give a quantity with units of N C, "
               "not newtons per coulomb.",
    },

    # ── harder ───────────────────────────────────────────────────────────
    {
        "id": "ks4-electric-fields-h05",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "During a Millikan-style experiment, an oil droplet's charge "
                "produces an electric force of 3.0 × 10⁻¹³ N when the "
                "droplet sits in a field of strength 5.0 × 10⁴ N/C. "
                "Determine the size of that charge.",
        "options": [
            "1.5 × 10⁻⁸ C",
            "6.0 × 10⁻¹⁸ C",
            "1.7 × 10¹⁷ C",
            "6.0 × 10⁻⁹ C",
        ],
        "correct_index": 1,
        "why": "E = F ÷ q rearranges to q = F ÷ E = 3.0 × 10⁻¹³ ÷ 5.0 × 10⁴ = "
               "6.0 × 10⁻¹⁸ C.",
    },
    {
        "id": "ks4-electric-fields-h06",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A small charged bead carries a charge of 250 nC and "
                "experiences a force of 1.5 mN in an electric field. Determine "
                "the electric field strength.",
        "options": [
            "0.0060 N/C",
            "3.8 × 10⁻¹⁰ N/C",
            "6000 N/C",
            "60 000 N/C",
        ],
        "correct_index": 2,
        "why": "250 nC = 2.5 × 10⁻⁷ C and 1.5 mN = 1.5 × 10⁻³ N, so E = F ÷ q "
               "= 1.5 × 10⁻³ ÷ 2.5 × 10⁻⁷ = 6000 N/C.",
    },
    {
        "id": "ks4-electric-fields-h07",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A charged pollen grain, carrying charge 2.5 × 10⁻⁹ C, is "
                "pushed upwards by a uniform electric field of strength "
                "4.0 × 10³ N/C. Given the grain's weight is 6.0 × 10⁻⁶ N, "
                "determine what happens to it.",
        "options": [
            "It stays where it is, because the upward electric force exactly balances its weight",
            "It falls, because the upward electric force is smaller than the weight of the grain",
            "It rises at first and then stops, because the field weakens as the grain moves up",
            "It rises, because the upward electric force is larger than the weight of the grain",
        ],
        "correct_index": 3,
        "why": "F = E × q = 4.0 × 10³ × 2.5 × 10⁻⁹ = 1.0 × 10⁻⁵ N, which is "
               "larger than the 6.0 × 10⁻⁶ N weight, so there is a resultant "
               "upward force.",
    },
    {
        "id": "ks4-electric-fields-h08",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two equal positive charges are fixed a short distance apart. "
                "State the force on a small positive test charge placed "
                "exactly midway between them.",
        "options": [
            "Zero, because the push from each charge is equal in size and opposite in direction",
            "Twice the push from one charge alone, because the two pushes add together at that point",
            "A push towards one of them, because two like charges drive a test charge to one side",
            "A push at right angles to the line joining them, because both pushes are turned sideways",
        ],
        "correct_index": 0,
        "why": "At the midpoint the two charges push the test charge equally "
               "hard in opposite directions, so the resultant force is zero — "
               "this is the neutral point between like charges.",
    },
    {
        "id": "ks4-electric-fields-h09",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two small metal spheres carry equal but opposite charges and "
                "are clamped 4 cm apart on a bench. A tiny positively charged "
                "bead rests at the halfway point on the line joining the "
                "spheres. State the direction of the electric force acting on "
                "the bead.",
        "options": [
            "Towards the positive sphere, because a charged bead is drawn to the larger of the fields",
            "Towards the negative sphere, because the bead is pushed by one charge and pulled by the other",
            "There is no force, because the pull of one sphere is exactly undone by that of the other",
            "At right angles to the line joining the spheres, because the lines curve round at that point",
        ],
        "correct_index": 1,
        "why": "The positive sphere repels the bead and the negative sphere "
               "attracts it, and both effects act the same way, so the two "
               "forces add and point towards the negative sphere.",
    },
    {
        "id": "ks4-electric-fields-h10",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A builder suggests replacing a building's copper lightning "
                "conductor with a rod of exactly the same shape made of "
                "plastic. Evaluate this suggestion.",
        "options": [
            "It would work as well as copper, because the pointed shape is the only part that matters",
            "It would work better than copper, because an insulator stops lightning entering at all",
            "It would not work, because plastic is an insulator and cannot carry charge down to earth",
            "It would work as well as copper, because the earth connection alone carries the charge",
        ],
        "correct_index": 2,
        "why": "The rod's job is to conduct: charge has to flow along it to "
               "earth, and plastic will not let it.",
    },
    {
        "id": "ks4-electric-fields-h11",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a spark between a charged metal dome and an "
                "earthed sphere lasts only a moment instead of continuing.",
        "options": [
            "The air in the gap is used up by the spark, and no more charge can cross until it renews",
            "The spark heats the gap so much that the air expands away and breaks the path at once",
            "The earthed sphere fills up with charge almost at once and can take no more from the dome",
            "Charge crosses until the dome is discharged, so the field collapses and the air stops conducting",
        ],
        "correct_index": 3,
        "why": "The spark carries charge away from the dome; once the charge "
               "has gone the field is no longer strong enough to keep the air "
               "ionised.",
    },
    {
        "id": "ks4-electric-fields-h12",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the electric field around a charged sphere with the "
                "gravitational field around a planet.",
        "options": [
            "Both act without contact, but a gravitational field only attracts while an electric one can repel",
            "Both act without contact, and both can attract or repel depending on the sign of the mass",
            "Both need a material in between to carry the force, and both act only over short distances",
            "Only the gravitational field acts without contact; an electric force needs the objects to touch",
        ],
        "correct_index": 0,
        "why": "Both are non-contact fields, but mass comes in one kind only, "
               "so gravity always pulls, whereas two like charges repel.",
    },
    {
        "id": "ks4-electric-fields-h13",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare what an electric field and a magnetic field each "
                "exert a force on.",
        "options": [
            "Both push any charged object, because charge and magnetism are two names for one property",
            "An electric field pushes any charged object; a magnetic field pushes magnetic materials",
            "An electric field pushes only metals; a magnetic field pushes any object that is rubbed",
            "An electric field pushes magnetic materials; a magnetic field pushes stationary charges",
        ],
        "correct_index": 1,
        "why": "A stationary charge feels a force in an electric field but not "
               "in a magnetic one; a magnetic field acts on magnetic materials "
               "and on magnets.",
    },
    {
        "id": "ks4-electric-fields-h14",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two students measure the electric field strength at the same "
                "point in a field. One uses a charge of 2 nC and the other "
                "uses a charge of 8 nC. Predict what the two students find.",
        "options": [
            "The second finds a field four times larger, because a larger charge makes a stronger field",
            "The second finds a field four times smaller, because one force is shared over more charge",
            "Both find the same field strength, because the force is four times larger for four times the charge",
            "Neither can find the field, because a field strength cannot be worked out from a force at all",
        ],
        "correct_index": 2,
        "why": "E = F ÷ q, and the force is proportional to the charge used, so "
               "the ratio — the field strength — is the same for both.",
    },
    {
        "id": "ks4-electric-fields-h15",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two parallel plates set up a uniform electric field of "
                "strength 800 N/C. A charge of 3.0 × 10⁻⁷ C is first held "
                "1.0 cm from the positive plate, then moved to a point 3.0 cm "
                "from it, still between the plates. Determine the electric "
                "force on the charge at the second point.",
        "options": [
            "8.0 × 10⁻⁵ N",
            "7.2 × 10⁻⁴ N",
            "2.4 × 10⁻⁶ N",
            "2.4 × 10⁻⁴ N",
        ],
        "correct_index": 3,
        "why": "The field is uniform, so moving the charge does not change it: "
               "F = E × q = 800 × 3.0 × 10⁻⁷ = 2.4 × 10⁻⁴ N.",
    },
    {
        "id": "ks4-electric-fields-h16",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fuel tanker is connected to an earthing cable before any "
                "fuel is pumped. Explain why connecting the cable after "
                "pumping had started would not protect the tanker.",
        "options": [
            "Charge builds up as soon as the fuel begins to flow, so a spark could jump before it is fitted",
            "The cable works while fuel is still in the tank, and the tank empties as soon as pumping begins",
            "The pump earths the tanker by itself once fuel moves, so the cable makes no difference then",
            "Fuel becomes charged while it is standing still, so the danger has already passed by then",
        ],
        "correct_index": 0,
        "why": "Flowing fuel charges the tanker by friction; the earth "
               "connection has to be in place first so the charge drains away "
               "instead of building up to a spark.",
    },
    {
        "id": "ks4-electric-fields-h17",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "At a point in an electric field, a charge of 5.0 nC "
                "experiences a force of 2.0 × 10⁻⁵ N. Determine the force on a "
                "charge of 12 nC placed at the same point.",
        "options": [
            "2.0 × 10⁻⁵ N",
            "4.8 × 10⁻⁵ N",
            "2.4 × 10⁻⁴ N",
            "8.3 × 10⁻⁶ N",
        ],
        "correct_index": 1,
        "why": "E = F ÷ q = 2.0 × 10⁻⁵ ÷ 5.0 × 10⁻⁹ = 4000 N/C, then F = E × q "
               "= 4000 × 12 × 10⁻⁹ = 4.8 × 10⁻⁵ N.",
    },
    {
        "id": "ks4-electric-fields-h18",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "At point A the field lines around a charged object are 2 mm "
                "apart; at point B they are 8 mm apart. Compare the electric "
                "force on the same small charge placed at each of the two "
                "points.",
        "options": [
            "The force is larger at B, because the wider spacing gives the charge more room to be pushed",
            "The force is the same at both points, because the same small charge is placed at each one",
            "The force is larger at A, because closer lines mean a stronger field and so a larger force",
            "The force is four times larger at B, because the spacing there is four times as great",
        ],
        "correct_index": 2,
        "why": "Line spacing shows field strength, and F = E × q, so the same "
               "charge feels a larger force where the lines are closer "
               "together.",
    },
    {
        "id": "ks4-electric-fields-h19",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A small negative charge is placed in the field of a single "
                "positive point charge. State the direction of the force on it "
                "and how that compares with the direction of the field there.",
        "options": [
            "The force is away from the positive charge, which is along the outward direction of the field",
            "The force is towards the positive charge, which is along the outward direction of the field",
            "There is no force on it, because a negative charge is not affected by a positive one's field",
            "The force is towards the positive charge, which is opposite to the outward field direction",
        ],
        "correct_index": 3,
        "why": "The field of a positive charge points outwards, and a negative "
               "charge is pushed the opposite way to the field, so it is "
               "attracted inwards.",
    },
    {
        "id": "ks4-electric-fields-h20",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Dry air breaks down and begins to conduct when the electric "
                "field strength reaches about 3.0 × 10⁶ N/C. Determine the "
                "force on a single electron, of charge 1.6 × 10⁻¹⁹ C, placed "
                "in a field of this strength.",
        "options": [
            "4.8 × 10⁻¹³ N",
            "1.9 × 10²⁵ N",
            "5.3 × 10⁻²⁶ N",
            "4.8 × 10⁻¹² N",
        ],
        "correct_index": 0,
        "why": "F = E × q = 3.0 × 10⁶ × 1.6 × 10⁻¹⁹ = 4.8 × 10⁻¹³ N.",
    },
    {
        "id": "ks4-electric-fields-h21",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The electric field at a point is described only as "
                "'500 N/C'. Explain why this does not fully describe the field "
                "at that point.",
        "options": [
            "The field is a scalar, so the charge that it acts on has to be stated alongside the value",
            "The field is a vector, so its direction at that point is needed as well as its size",
            "The unit is wrong, so the value has to be converted into newtons before it means anything",
            "The value is an average, so the largest and smallest readings have to be given as well",
        ],
        "correct_index": 1,
        "why": "Electric field strength is a vector quantity: a full "
               "description gives both how strong the field is and which way "
               "it acts.",
    },
    {
        "id": "ks4-electric-fields-h22",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A charged dome makes a spark jump to an earthed sphere held "
                "2 cm away. The sphere is then moved to 10 cm away and no "
                "spark jumps. Explain why.",
        "options": [
            "The charge on the dome leaks away completely as soon as the sphere is moved further off",
            "Air conducts within about 2 cm of a charged object, whatever the field strength may be",
            "The field across the wider gap is weaker, so it is no longer strong enough to ionise the air",
            "The sphere stops being earthed once it is moved, so the charge has nowhere left to flow",
        ],
        "correct_index": 2,
        "why": "The same charge spread across a wider gap gives a weaker field "
               "there, and below the breakdown value the air stays an "
               "insulator.",
    },
    {
        "id": "ks4-electric-fields-h23",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two parallel metal plates are connected to a power supply. "
                "Explain the effect on the field between the plates of "
                "increasing the potential difference across them.",
        "options": [
            "The field becomes weaker, because the same charge is spread across a larger potential difference",
            "The field stays exactly the same, because the spacing of the plates has not been altered",
            "The field reverses direction, because raising the potential difference swaps the positive plate",
            "The field becomes stronger, so a given charge between the plates feels a larger force",
        ],
        "correct_index": 3,
        "why": "A larger potential difference drives more charge onto the "
               "plates, strengthening the uniform field and so the force on "
               "any charge in it.",
    },
    {
        "id": "ks4-electric-fields-h24",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An inkjet printer deflects charged ink droplets using two "
                "parallel charged plates rather than a single charged sphere. "
                "Explain why parallel plates are used.",
        "options": [
            "The field between plates is uniform, so every droplet feels the same force wherever it passes",
            "The field between plates grows stronger the further a droplet travels, so the push builds up",
            "A single sphere makes no field at all unless it is touching the droplets as they go past",
            "A single sphere would charge the droplets, and uncharged droplets are the ones that deflect",
        ],
        "correct_index": 0,
        "why": "A uniform field gives a constant, predictable force on each "
               "droplet, so the deflection can be controlled precisely; a "
               "sphere's radial field varies with position.",
    },
    {
        "id": "ks4-electric-fields-h25",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The same small test charge is placed at two points, A and B, "
                "in the field of a single positive charge. At A the force on "
                "it is 0.12 N and at B the force is 0.030 N. Determine how "
                "many times stronger the field is at A than at B.",
        "options": [
            "Sixteen times stronger, because the ratio of the forces has itself to be squared",
            "Four times stronger, because the field is proportional to the force on a given charge",
            "The same at both points, because the same small test charge is used at each of them",
            "One quarter as strong, because a larger force on a charge means a weaker field there",
        ],
        "correct_index": 1,
        "why": "E = F ÷ q with the same q at both points, so the field ratio "
               "equals the force ratio: 0.12 ÷ 0.030 = 4.",
    },
    {
        "id": "ks4-electric-fields-h26",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why lightning is more likely to strike a tall tree "
                "standing in an open field than the flat ground beside it.",
        "options": [
            "Wood conducts far better than soil, so charge in the cloud is drawn towards the tree first",
            "The tree is full of sap, and a wet object is the only kind that can carry a strike to earth",
            "The top of the tree is nearer the cloud and sharply shaped, so the field there is strongest",
            "The tree blocks the field from reaching the ground, so all of the charge must pass through it",
        ],
        "correct_index": 2,
        "why": "The gap to the cloud is shortest at the treetop and charge "
               "concentrates on its pointed shape, so the field there reaches "
               "the breakdown value first.",
    },
]
