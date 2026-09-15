"""Physics · Space — `stellar-evolution`, the MRB-338 expansion.

⚠️ Read `docs/ks4/pool-authoring.md` §2 before adding to this leaf. It is one
of the two named subtopics whose lesson page prints its whole examinable core
as an already-paired matching block — one life cycle, five stages, each with
its description — and whose two "Test yourself" tasks take the two questions
an author reaches for first: why a main sequence star is stable for billions
of years, and why the elements heavier than iron are rare. All four of those
are off limits, and the twenty rows already here have taken most of what is
left of the bare life-cycle sequence.

So these 34 go sideways rather than round again. The numbers the page states
but nobody has examined: the core temperature fusion needs, the size of a
white dwarf, the mass above which a star ends in a supernova, the order of
the fusion products, the Sun's total main-sequence budget. The reasoning the
page implies but never asks for: why no black dwarf has been seen, why the
oldest stars carry almost no heavy elements, why the Earth's iron cannot have
come from the Sun, what a ten-billion-year main sequence tells you about a
star's mass, what happens to a cloud too small ever to ignite.

10 / 12 / 12: the easier band was already eight deep on naming the stages, so
it takes only the stated quantities it was missing, and the deductions carry
the weight at `standard` and `harder`.
"""

TOPIC = "space"
SUBJECT = "physics"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-stellar-evolution-e09",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the approximate core temperature a collapsing cloud must "
                "reach before nuclear fusion begins.",
        "options": [
            "About 1000 °C",
            "About 100 000 °C",
            "About 10 million °C",
            "About 100 billion °C",
        ],
        "correct_index": 2,
        "why": "Fusion needs roughly 10 million °C at the core; below that the "
               "hydrogen nuclei cannot get close enough to fuse.",
    },
    {
        "id": "ks4-stellar-evolution-e10",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the two objects that a supernova can leave behind.",
        "options": [
            "A neutron star or a black hole",
            "A red giant or a white dwarf",
            "A planetary nebula or a protostar",
            "A red supergiant or a main sequence star",
        ],
        "correct_index": 0,
        "why": "Which one forms depends on the mass left in the collapsed core: "
               "a neutron star if it is moderate, a black hole if it is very "
               "large.",
    },
    {
        "id": "ks4-stellar-evolution-e11",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the stage of a star's life during which it fuses hydrogen "
                "into helium in its core.",
        "options": [
            "The protostar stage",
            "The main sequence",
            "The red giant stage",
            "The planetary nebula stage",
        ],
        "correct_index": 1,
        "why": "Hydrogen fusion in the core is what defines the main sequence, "
               "and it is where a star spends most of its life.",
    },
    {
        "id": "ks4-stellar-evolution-e12",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the approximate size of a white dwarf.",
        "options": [
            "About the size of the Sun",
            "About the size of the Solar System",
            "About the size of a large city",
            "About the size of the Earth",
        ],
        "correct_index": 3,
        "why": "A white dwarf packs a whole stellar core into roughly the volume "
               "of the Earth, which is why it is so dense.",
    },
    {
        "id": "ks4-stellar-evolution-e13",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the stage that a star far more massive than the Sun swells "
                "into once the hydrogen in its core is gone.",
        "options": [
            "A red supergiant",
            "A white dwarf",
            "A protostar",
            "A planetary nebula",
        ],
        "correct_index": 0,
        "why": "Massive stars become red supergiants; only stars of about the "
               "Sun's mass become red giants and then white dwarfs.",
    },
    {
        "id": "ks4-stellar-evolution-e14",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which kind of star ends its life in a supernova.",
        "options": [
            "A star of about the Sun's mass",
            "A star less massive than the Sun",
            "A star much more massive than the Sun",
            "A star of any mass",
        ],
        "correct_index": 2,
        "why": "A star far more massive than the Sun collapses and explodes at "
               "the end of its life; a star like the Sun ends quietly as a "
               "white dwarf instead.",
    },
    {
        "id": "ks4-stellar-evolution-e15",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the gas and dust of a nebula is largely the remains "
                "of.",
        "options": [
            "Planets stripped by the solar wind",
            "Earlier stars",
            "Material from a black hole",
            "Comets that have broken up into dust",
        ],
        "correct_index": 1,
        "why": "Nebulae are built from the material earlier stars shed or threw "
               "off, which is why later stars contain heavier elements.",
    },
    {
        "id": "ks4-stellar-evolution-e16",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the element that a star fuses helium into.",
        "options": [
            "Hydrogen",
            "Iron",
            "Uranium",
            "Carbon",
        ],
        "correct_index": 3,
        "why": "Once helium fusion begins the next product is carbon, and in a "
               "massive star fusion then works on upwards towards iron.",
    },
    {
        "id": "ks4-stellar-evolution-e17",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the surface temperature of a star as it "
                "becomes a red giant.",
        "options": [
            "It falls",
            "It rises",
            "It stays the same",
            "It falls to absolute zero",
        ],
        "correct_index": 0,
        "why": "The outer layers expand enormously, and spreading the same "
               "energy over a far larger surface leaves it cooler — and so "
               "redder.",
    },
    {
        "id": "ks4-stellar-evolution-e18",
        "subtopic_slug": "stellar-evolution",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State whether nuclear fusion takes place inside a white dwarf.",
        "options": [
            "Yes, it still fuses hydrogen",
            "No",
            "Yes, it still fuses iron",
            "Yes, it still fuses helium",
        ],
        "correct_index": 1,
        "why": "A white dwarf is a remnant: no fusion happens in it at all, and "
               "it shines only because it is still hot.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-stellar-evolution-s07",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student describes a star as a huge ball of burning gas. "
                "Explain why the word 'burning' is wrong.",
        "options": [
            "Burning needs a solid fuel, and a star's fuel is a gas rather than "
            "a solid",
            "Burning happens only at the surface, whereas a star gives out "
            "energy from every part of itself equally",
            "A star joins nuclei together rather than reacting chemically, so "
            "it needs no oxygen",
            "Burning gives out light but no heat, and a star gives out a great "
            "deal of heat as well",
        ],
        "correct_index": 2,
        "why": "Burning is a chemical reaction with oxygen; a star releases "
               "energy by nuclear fusion in its core, and there is no oxygen "
               "involved.",
    },
    {
        "id": "ks4-stellar-evolution-s08",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a protostar is not yet counted as a star.",
        "options": [
            "It is smaller than the Sun is",
            "It is not yet held together by gravity",
            "It gives out no light of its own",
            "Fusion has not begun in it",
        ],
        "correct_index": 3,
        "why": "A protostar is still heating up as it collapses; it becomes a "
               "star at the moment its core is hot enough for fusion to start.",
    },
    {
        "id": "ks4-stellar-evolution-s09",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what happens in the core of a massive star once iron "
                "has built up there.",
        "options": [
            "The core collapses suddenly, and the star explodes",
            "The core cools slowly and the star fades away",
            "The iron is fused into gold and uranium",
            "The iron sinks out of the core",
        ],
        "correct_index": 0,
        "why": "Iron cannot be fused to release energy, so the outward pressure "
               "fails, gravity wins, and the sudden collapse drives the "
               "supernova.",
    },
    {
        "id": "ks4-stellar-evolution-s10",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why no black dwarf has ever been observed.",
        "options": [
            "A black dwarf gives out no gravity, so no telescope can pick one "
            "out",
            "Cooling to that state takes longer than the universe has so far "
            "existed",
            "Black dwarfs are so far away that their light has not yet reached "
            "the Earth",
            "Black dwarfs were destroyed by supernovae early in the history of "
            "the universe",
        ],
        "correct_index": 1,
        "why": "A white dwarf takes far more than 13.8 billion years to cool "
               "into a black dwarf, so none has had the time to form yet.",
    },
    {
        "id": "ks4-stellar-evolution-s11",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain where the carbon atoms in your body were made.",
        "options": [
            "In the Big Bang, which produced the heavier elements",
            "Inside the Earth, where heat and pressure built them up from "
            "lighter ones",
            "By fusion inside stars, which then released them into space",
            "In the Sun, and carried to the Earth by the solar wind",
        ],
        "correct_index": 2,
        "why": "The Big Bang made hydrogen and helium; carbon is a fusion "
               "product of stars, scattered when those stars shed their layers "
               "or exploded.",
    },
    {
        "id": "ks4-stellar-evolution-s12",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the length of time a star of twenty solar masses "
                "spends on the main sequence with the time the Sun spends there.",
        "options": [
            "Both spend roughly ten billion years there",
            "The massive star spends far longer there, because it starts out "
            "with more hydrogen to fuse",
            "The massive star spends about twenty times as long there",
            "The massive star spends millions of years there and the Sun "
            "billions",
        ],
        "correct_index": 3,
        "why": "A massive star's core is hotter and fuses far faster, so its "
               "main sequence is measured in millions of years against the "
               "Sun's billions.",
    },
    {
        "id": "ks4-stellar-evolution-s13",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the order in which a red supergiant fuses elements, "
                "beginning with helium.",
        "options": [
            "Helium, then carbon, then oxygen, and onwards to iron",
            "Helium, then iron, then carbon, and onwards to uranium",
            "Helium, then hydrogen, then carbon, and onwards to oxygen",
            "Helium, then oxygen, then carbon, and no further than that",
        ],
        "correct_index": 0,
        "why": "Fusion works upwards through the elements — helium to carbon to "
               "oxygen and beyond — and stops at iron, which cannot be fused to "
               "release energy.",
    },
    {
        "id": "ks4-stellar-evolution-s14",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what becomes of the material that a supernova throws "
                "out into space.",
        "options": [
            "It is pulled back in by the remnant that is left behind at the "
            "centre",
            "It forms new nebulae, from which later stars and planets form",
            "It spreads out and stops existing in the heat",
            "It collects into a ring around the remnant",
        ],
        "correct_index": 1,
        "why": "Supernova debris enriches the clouds that later collapse into "
               "new star systems — which is why the Earth contains heavy "
               "elements at all.",
    },
    {
        "id": "ks4-stellar-evolution-s15",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how astronomers can describe the whole life cycle of a "
                "star when every stage of it takes millions of years.",
        "options": [
            "They record one star for a very long time, passing the work on "
            "from one generation of astronomers to the next",
            "They calculate the whole cycle from theory, observing nothing",
            "They observe many different stars, each caught at a different "
            "stage",
            "They use telescopes powerful enough to speed the stages up",
        ],
        "correct_index": 2,
        "why": "The sky contains nebulae, protostars, main sequence stars, red "
               "giants and remnants all at once, so the sequence can be pieced "
               "together from snapshots.",
    },
    {
        "id": "ks4-stellar-evolution-s16",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the shell of gas around a dying Sun-like star can "
                "be seen glowing.",
        "options": [
            "The gas is still burning and goes on burning",
            "The gas rubs against the gas in space and the friction heats it",
            "The gas reflects the light of the galaxy behind it",
            "It is lit by the very hot remnant core at its centre",
        ],
        "correct_index": 3,
        "why": "The core left behind is extremely hot, and its radiation makes "
               "the expanding shell glow for a while — the planetary nebula "
               "stage.",
    },
    {
        "id": "ks4-stellar-evolution-s17",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the property of a star that decides how its life will "
                "end.",
        "options": [
            "Its mass",
            "Its surface colour",
            "Its distance from other stars",
            "The size of the nebula it formed from",
        ],
        "correct_index": 0,
        "why": "Mass sets the core temperature, the rate of fusion, the "
               "lifetime and the remnant — everything about how a star ends.",
    },
    {
        "id": "ks4-stellar-evolution-s18",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A star has already spent 4.6 billion years on the main "
                "sequence and has 4.6 billion years of it still to come. "
                "Calculate its total main-sequence lifetime and the fraction of "
                "that lifetime it has used.",
        "options": [
            "4.6 billion years in total, all of it used",
            "9.2 billion years in total, half of it used",
            "9.2 billion years in total, a quarter of it used",
            "2.3 billion years in total, half of it used",
        ],
        "correct_index": 1,
        "why": "4.6 + 4.6 = 9.2 billion years, and the 4.6 already spent is "
               "half of that.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-stellar-evolution-h07",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A cloud of gas is contracting, its core is at 5 million °C, "
                "and no fusion is taking place in it. Deduce which stage it has "
                "reached.",
        "options": [
            "A main sequence star",
            "A red giant",
            "A protostar",
            "A white dwarf",
        ],
        "correct_index": 2,
        "why": "Contracting, heating and not yet fusing is exactly the "
               "protostar stage; it becomes a star when the core reaches about "
               "10 million °C.",
    },
    {
        "id": "ks4-stellar-evolution-h08",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a neutron star is far denser than a white dwarf.",
        "options": [
            "It is much younger, and any stellar remnant grows steadily less "
            "dense as the years pass by",
            "It is still fusing material, and fusion packs matter more tightly "
            "together",
            "It is made of iron while a white dwarf is made of helium",
            "It is the core of a far more massive star, so gravity crushes it "
            "very much further",
        ],
        "correct_index": 3,
        "why": "The remnant core of a massive star is squeezed by a far "
               "stronger gravitational collapse, ending up at roughly a billion "
               "tonnes per teaspoon.",
    },
    {
        "id": "ks4-stellar-evolution-h09",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Deduce why the very oldest stars contain almost no elements "
                "heavier than helium.",
        "options": [
            "They formed before any earlier star had made heavier elements and "
            "spread them about",
            "They are so hot that heavier elements are broken apart inside "
            "them",
            "The heavier elements sank to their centres long ago",
            "They are so far away that only hydrogen and helium show up",
        ],
        "correct_index": 0,
        "why": "The Big Bang produced hydrogen and helium only, so the first "
               "generation of stars had nothing heavier to form from.",
    },
    {
        "id": "ks4-stellar-evolution-h10",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A star has been fusing hydrogen in its core for ten billion "
                "years and is still doing so. Deduce how its mass compares with "
                "the mass of the Sun.",
        "options": [
            "It must be far more massive than the Sun",
            "It is about the Sun's mass or less",
            "It must be exactly twice the Sun's mass",
            "Nothing can be deduced from the time alone",
        ],
        "correct_index": 1,
        "why": "A more massive star burns through its hydrogen in millions of "
               "years, so a ten-billion-year main sequence means a star no "
               "heavier than the Sun.",
    },
    {
        "id": "ks4-stellar-evolution-h11",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a supernova is a rare sight in a galaxy that "
                "contains hundreds of billions of stars.",
        "options": [
            "Supernovae are too faint to pick out from the Earth",
            "Supernovae happened in the early universe alone",
            "Only the few most massive stars end that way",
            "Every star produces one, but each lasts a very long time",
        ],
        "correct_index": 2,
        "why": "Stars above about eight solar masses are a small minority, and "
               "each galaxy therefore produces only a supernova or two per "
               "century.",
    },
    {
        "id": "ks4-stellar-evolution-h12",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the core of a red giant contracts at the same time "
                "as its outer layers expand.",
        "options": [
            "The core is pulled inwards by the gravity of the outer layers as "
            "those layers move away from it",
            "The core cools and shrinks while the outer layers are heated by "
            "the light of nearby stars",
            "The core is made of helium, which contracts when it is heated, "
            "while hydrogen expands when it is heated",
            "The core has lost the fusion that held it up, while fusion in a "
            "shell around it pushes the outer layers out",
        ],
        "correct_index": 3,
        "why": "Two things happen at once: with core hydrogen gone gravity "
               "squeezes the core, and the shell fusion that starts around it "
               "drives the envelope outwards.",
    },
    {
        "id": "ks4-stellar-evolution-h13",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Predict what will happen to a white dwarf over the next "
                "hundred billion years.",
        "options": [
            "It will cool and fade into a black dwarf",
            "It will collapse into a black hole as it cools",
            "It will fuse helium and swell into a red giant again",
            "It will explode as a supernova as it cools",
        ],
        "correct_index": 0,
        "why": "There is no fusion left to replace what it radiates away, so a "
               "white dwarf simply cools, dimming until it is a cold black "
               "dwarf.",
    },
    {
        "id": "ks4-stellar-evolution-h14",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the iron in the Earth's core cannot have been made "
                "inside the Sun.",
        "options": [
            "The Sun's core is too hot for iron to survive there",
            "The Sun is not massive enough to fuse elements as far as iron",
            "Iron is magnetic, so the Sun's magnetic field would have kept "
            "hold of it",
            "The Sun formed after the Earth did",
        ],
        "correct_index": 1,
        "why": "Fusion up to iron happens only in the cores of far more massive "
               "stars, so the Earth's iron was made in an earlier star and "
               "scattered before the Solar System formed.",
    },
    {
        "id": "ks4-stellar-evolution-h15",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Deduce what would happen to the Sun if the rate of fusion in "
                "its core suddenly increased.",
        "options": [
            "It would collapse inwards, because faster fusion uses up the fuel "
            "that was holding the core apart from the start",
            "Nothing would change, because a star's size is fixed by its mass",
            "It would expand, because the outward pressure would then be "
            "greater than gravity",
            "It would explode as a supernova, because that is how one starts",
        ],
        "correct_index": 2,
        "why": "The main sequence is a balance between outward pressure from "
               "fusion and inward gravity, so increasing the pressure pushes "
               "the star outwards until the balance is restored.",
    },
    {
        "id": "ks4-stellar-evolution-h16",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a star of twenty solar masses cannot end its life "
                "as a white dwarf.",
        "options": [
            "Its outer layers drift away, leaving no core behind",
            "It ends as a red supergiant, which leaves no remnant",
            "It has used up all of its hydrogen, and a white dwarf must still "
            "hold some unfused hydrogen of its own",
            "The core left behind is far too massive, so it collapses further "
            "still",
        ],
        "correct_index": 3,
        "why": "Above roughly eight solar masses the remnant core cannot "
               "support itself and collapses past the white dwarf state into a "
               "neutron star or a black hole.",
    },
    {
        "id": "ks4-stellar-evolution-h17",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A collapsing cloud of gas and dust is too small for its core "
                "ever to become hot enough for fusion. Predict what happens to "
                "it.",
        "options": [
            "It stays a cool, dark object and never becomes a star",
            "It becomes a white dwarf, the remnant left when fusion fails",
            "It explodes, because nothing holds an unfused cloud together",
            "It becomes a very dim star that fuses helium instead",
        ],
        "correct_index": 0,
        "why": "Fusion is what makes a star; without enough mass to reach the "
               "temperature it needs, the object simply contracts, cools and "
               "stays dark.",
    },
    {
        "id": "ks4-stellar-evolution-h18",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a supernova can briefly shine more brightly than "
                "all the other stars of its galaxy put together.",
        "options": [
            "Its light is focused into a narrow beam by the remnant's gravity",
            "The collapse releases an enormous amount of energy in a few "
            "moments",
            "It sets fire to the gas and dust around it, and the fire spreads",
            "The other stars are hidden by the dust that the explosion throws "
            "out",
        ],
        "correct_index": 1,
        "why": "The core collapse converts a huge amount of gravitational "
               "energy in seconds, so the output for a short time rivals a "
               "whole galaxy's steady output.",
    },
]
