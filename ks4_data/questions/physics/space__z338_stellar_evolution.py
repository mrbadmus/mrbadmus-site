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

    # ── standard, continued: named real objects (Betelgeuse, Sirius B, the
    # Crab Nebula), the fusion/supernova element-origin split, a fresh
    # lifetime calculation, density in numbers, and the pressure/gravity
    # balance stated plainly ───────────────────────────────────────────────
    {
        "id": "ks4-stellar-evolution-s19",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Betelgeuse, a red supergiant in the constellation Orion, "
                "is roughly twenty times the mass of the Sun. Explain "
                "why astronomers expect it to end its life very "
                "differently from how the Sun will end its life.",
        "options": [
            "Its far greater mass means it will collapse and explode "
            "as a supernova, rather than shedding its outer layers "
            "quietly to leave a white dwarf",
            "Its greater size alone guarantees it will burn out faster, "
            "whatever its mass turns out to be once it is measured "
            "more accurately",
            "Being a supergiant rather than a giant means it has "
            "already finished its main sequence stage and cannot fuse "
            "any further elements at all",
            "Stars in the constellation Orion are known to follow a "
            "different life cycle from stars found in every other "
            "part of the sky",
        ],
        "correct_index": 0,
        "why": "Above roughly eight solar masses, a star's core cannot "
               "settle as a white dwarf and instead collapses "
               "catastrophically, driving a supernova.",
    },
    {
        "id": "ks4-stellar-evolution-s20",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Sirius B is a white dwarf with roughly the mass of the "
                "Sun packed into a volume no larger than the Earth's. "
                "Explain what this tells you about the material inside "
                "it.",
        "options": [
            "The material must still be undergoing fusion of some "
            "kind, since only active fusion could ever support that "
            "much mass squeezed into so small a volume",
            "The material is compressed to an extremely high density, "
            "far beyond anything achievable inside an ordinary star or "
            "on Earth",
            "The material must be lighter than the material that makes "
            "up the Sun, since it takes up so little space for its "
            "mass",
            "The volume given must be a measurement error, since no "
            "known material could ever be compressed that far",
        ],
        "correct_index": 1,
        "why": "Packing about a solar mass into an Earth-sized sphere "
               "means matter crushed to a density enormously greater "
               "than anything found in ordinary stars or on Earth.",
    },
    {
        "id": "ks4-stellar-evolution-s21",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Crab Nebula is the visible remains of a supernova "
                "recorded by astronomers in the year 1054, and it is "
                "still expanding today. Explain what this remnant "
                "shows about what happens to the material a dying star "
                "throws out.",
        "options": [
            "It shows that supernova debris cools instantly and stops "
            "expanding within a few years of the explosion itself",
            "It shows that supernova material always collapses back "
            "together into a single brand-new star within only a few "
            "centuries of the original explosion taking place",
            "It shows that the material keeps expanding outward for "
            "many centuries, spreading across space where it can later "
            "become part of new stars and planets",
            "It shows that a supernova remnant becomes completely "
            "invisible to telescopes within a hundred years of the "
            "explosion",
        ],
        "correct_index": 2,
        "why": "Nearly a thousand years on, the Crab Nebula's material "
               "is still spreading outward, exactly the kind of "
               "long-lived cloud from which later stars and planets "
               "can form.",
    },
    {
        "id": "ks4-stellar-evolution-s22",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain the difference between how an element such as "
                "carbon is made inside a star and how an element such "
                "as gold is made.",
        "options": [
            "Carbon and gold are both made by ordinary fusion inside a "
            "star's core during its main sequence stage, with no "
            "difference between them",
            "Carbon is made only in the Big Bang, while gold is made "
            "entirely by fusion inside an ordinary star like the Sun",
            "Carbon and gold are both made only during a supernova "
            "explosion itself, with neither one forming at any earlier "
            "stage of a star's life, whatever that star's mass turns "
            "out to be",
            "Carbon forms by ordinary nuclear fusion during a star's "
            "life, while an element as heavy as gold is built during "
            "the extreme conditions of a supernova explosion itself",
        ],
        "correct_index": 3,
        "why": "Fusion inside a star builds elements up to iron; "
               "heavier elements such as gold need the far more "
               "extreme, brief conditions of a supernova to form.",
    },
    {
        "id": "ks4-stellar-evolution-s23",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An astronomer estimates that a particular star has "
                "already used up two thirds of its time on the main "
                "sequence, with 3 billion years remaining before it "
                "moves on to become a giant. Work out the total length "
                "of its main-sequence stage.",
        "options": [
            "9 billion years",
            "4.5 billion years",
            "6 billion years",
            "12 billion years",
        ],
        "correct_index": 0,
        "why": "If 3 billion years is the remaining third, the whole "
               "lifetime is 3 × 3 = 9 billion years.",
    },
    {
        "id": "ks4-stellar-evolution-s24",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A teaspoon of white dwarf material has a mass of "
                "roughly a tonne, while a teaspoon of neutron star "
                "material has a mass of roughly a billion tonnes. "
                "Compare the two and explain what the difference tells "
                "you.",
        "options": [
            "It tells you the two remnants must be made of completely "
            "different chemical elements from one another, and that "
            "difference alone is the only real reason for the mass "
            "difference",
            "It tells you that a neutron star is compressed to a far "
            "greater density than a white dwarf, consistent with it "
            "forming from the collapse of a much more massive core",
            "It tells you the measurement of one of the two must be "
            "wrong, since no stellar remnant could differ from another "
            "by that much",
            "It tells you that a neutron star is much larger in size "
            "than a white dwarf, which is why it holds so much more "
            "mass",
        ],
        "correct_index": 1,
        "why": "A billion-fold jump in density between the two remnants "
               "matches the far more violent collapse that produces a "
               "neutron star from a far more massive star's core.",
    },
    {
        "id": "ks4-stellar-evolution-s25",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain what keeps a main sequence star at a stable, "
                "unchanging size for most of its life.",
        "options": [
            "Its own magnetic field holds every layer of the star in "
            "place against the pull of gravity",
            "The star has permanently stopped changing in any way at "
            "all once fusion first begins, and nothing further can "
            "ever then affect its size again",
            "The outward pressure produced by fusion in the core "
            "balances the inward pull of gravity, so neither one wins "
            "out over the other",
            "The star's rotation flings its outer layers outward with "
            "exactly enough force to cancel gravity completely",
        ],
        "correct_index": 2,
        "why": "A main sequence star sits in balance: fusion pushes "
               "outward and gravity pulls inward, and while the two "
               "match, the star's size stays steady.",
    },
    {
        "id": "ks4-stellar-evolution-s26",
        "subtopic_slug": "stellar-evolution",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the material a dying Sun-like star sheds as "
                "a planetary nebula contains carbon and oxygen, but no "
                "iron or anything heavier.",
        "options": [
            "The Sun's core reaches a high enough temperature to fuse "
            "hydrogen into helium and then helium into carbon and "
            "oxygen, but never hot enough to fuse beyond that",
            "Iron is present in the shed material too, but it is "
            "invisible to telescopes because it does not glow the way "
            "carbon and oxygen do",
            "The Sun in fact fuses every single element up to iron "
            "during its lifetime, but that iron sinks down to the "
            "white dwarf's centre and is never released into the "
            "shed material",
            "Carbon and oxygen were present in the nebula the Sun "
            "formed from, and the Sun has done no fusion of its own at "
            "any point in its life",
        ],
        "correct_index": 0,
        "why": "A star of the Sun's mass reaches temperatures high "
               "enough to fuse hydrogen and then helium into carbon "
               "and oxygen, but its core never gets hot enough to fuse "
               "iron or anything heavier.",
    },

    # ── harder, continued: Betelgeuse's timescale, a Crab Nebula
    # expansion-speed calculation, Sirius B's frozen composition, why
    # SN 1054 was visible in daylight, gold's real origin, two remnants
    # compared, the red-giant/supernova claim tested, and a compound
    # deduction from a short main-sequence lifetime ─────────────────────
    {
        "id": "ks4-stellar-evolution-h19",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Betelgeuse could explode as a supernova at any time "
                "within the next 100 000 years, which astronomers "
                "describe as 'astronomically soon'. Evaluate why this "
                "description makes sense despite the huge span of time "
                "involved.",
        "options": [
            "100 000 years is a tiny fraction of a star's lifetime of "
            "millions or billions of years, even though it is far "
            "longer than any human lifetime",
            "100 000 years is soon because it is shorter than the time "
            "light itself actually takes to travel all the way from "
            "Betelgeuse to reach the Earth",
            "100 000 years is soon only because Betelgeuse is "
            "unusually close to the Earth compared with most other "
            "stars in the sky",
            "The description is a mistake: 100 000 years is a long "
            "time by any reasonable standard, on any timescale that "
            "matters",
        ],
        "correct_index": 0,
        "why": "Judged against stellar lifetimes measured in millions "
               "to billions of years, a window of 100 000 years is a "
               "very narrow, imminent one — 'soon' is relative to the "
               "timescale being discussed.",
    },
    {
        "id": "ks4-stellar-evolution-h20",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Crab Nebula has expanded to a radius of about "
                "5.5 light-years since the supernova was observed in "
                "the year 1054. Taking the nebula's age as about "
                "970 years, estimate its average expansion speed in "
                "light-years per year.",
        "options": [
            "About 5.5 light-years per year",
            "About 970 light-years per year",
            "About 0.0057 light-years per year",
            "About 0.057 light-years per year",
        ],
        "correct_index": 2,
        "why": "Dividing distance by time: 5.5 ÷ 970 ≈ 0.0057 "
               "light-years per year — a huge speed in everyday terms, "
               "but tiny next to the light-year scale of the nebula "
               "itself.",
    },
    {
        "id": "ks4-stellar-evolution-h21",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student argues that because white dwarfs never "
                "undergo fusion, their composition is fixed forever "
                "from the moment they form. Evaluate this claim about "
                "a white dwarf such as Sirius B.",
        "options": [
            "The claim is unsound, because a white dwarf continues "
            "fusing helium slowly and steadily for billions of years "
            "after it first forms, gradually changing its composition "
            "the whole time",
            "The claim is unsound, because a white dwarf's composition "
            "changes completely once it cools into a black dwarf",
            "The claim is broadly sound: with no fusion taking place, "
            "nothing inside a white dwarf converts one element into "
            "another, so its composition stays essentially unchanged "
            "as it simply cools",
            "The claim is unsound, because gravity continues to fuse "
            "new elements inside a white dwarf even without any "
            "nuclear reactions taking place",
        ],
        "correct_index": 2,
        "why": "Fusion is what changes a star's composition, and a "
               "white dwarf has none; what happens to it afterwards is "
               "cooling, not any further chemical change.",
    },
    {
        "id": "ks4-stellar-evolution-h22",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The supernova that created the Crab Nebula was bright "
                "enough to be seen with the naked eye in daylight for "
                "over three weeks in the year 1054, despite the star "
                "itself being thousands of light-years away. Explain "
                "how this was possible.",
        "options": [
            "The star was actually far closer to Earth than thousands "
            "of light-years, and the distance usually quoted for it "
            "is a later error",
            "Ancient observers were simply mistaken, and no object "
            "that far away could ever have been visible in daylight "
            "at all",
            "The star had already been growing steadily brighter for "
            "several centuries leading up to 1054, and the explosion "
            "itself was only the final, barely noticeable step at the "
            "very end of that long process",
            "A supernova releases an enormous amount of energy in a "
            "very short time, briefly outshining anything else in its "
            "part of the sky even across a distance of thousands of "
            "light-years",
        ],
        "correct_index": 3,
        "why": "The sudden release of a supernova's energy makes it "
               "briefly among the brightest objects in the sky, "
               "bright enough to be seen even across a distance of "
               "thousands of light-years.",
    },
    {
        "id": "ks4-stellar-evolution-h23",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student claims that the gold found on Earth must "
                "have been made inside the Sun's core, since the Sun "
                "is the source of every other kind of atom in the "
                "Solar System. Evaluate this claim.",
        "options": [
            "The claim is unsound: the Sun's core never reaches the "
            "extreme conditions needed to build an element as heavy "
            "as gold, so it must have come from an earlier supernova "
            "instead",
            "The claim is sound, because every single element found "
            "anywhere in the Solar System, however heavy it happens "
            "to be, was made inside the Sun's own core before any of "
            "the planets had even formed",
            "The claim is sound, because gold is chemically similar "
            "enough to iron that the Sun's core can fuse it just as "
            "easily",
            "The claim is unsound, because the Sun contains no gold "
            "anywhere within it, which is why none is found on any of "
            "the planets",
        ],
        "correct_index": 0,
        "why": "Elements as heavy as gold need the extreme conditions "
               "of a supernova to form; the Sun's core never reaches "
               "that far, so the gold predates the Solar System's own "
               "formation.",
    },
    {
        "id": "ks4-stellar-evolution-h24",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The Crab Nebula, from a supernova in 1054, is about "
                "11 light-years across. The Veil Nebula, from a "
                "supernova roughly 8000 years ago, is about "
                "110 light-years across. Compare the two and suggest "
                "what mainly accounts for the difference in size.",
        "options": [
            "The Veil Nebula's star must have been about ten times "
            "more massive than the Crab Nebula's star, and more "
            "massive stars produce larger remnants",
            "The Veil Nebula has simply had far longer to expand — "
            "roughly eight times the Crab Nebula's age — so its "
            "debris has spread proportionally further",
            "The Crab Nebula is still contracting after its "
            "explosion, while the Veil Nebula has always been "
            "expanding since the moment its star exploded",
            "The two figures cannot be compared at all, because a "
            "nebula's visible size depends only on the telescope used "
            "to measure it, not on the nebula itself",
        ],
        "correct_index": 1,
        "why": "Both remnants are expanding outward from their "
               "explosions; the Veil Nebula has simply had thousands "
               "of years longer to do so, which is enough on its own "
               "to explain most of the size difference.",
    },
    {
        "id": "ks4-stellar-evolution-h25",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that any star which becomes a red "
                "giant is now destined to end its life as a supernova.",
        "options": [
            "The claim is sound, because becoming a red giant is "
            "itself proof that a star has enough mass to end its life "
            "that way",
            "The claim is sound, because every single star without "
            "exception passes through a red giant stage somewhere on "
            "its way towards an eventual supernova explosion",
            "The claim is unsound: a Sun-mass star also passes through "
            "a red giant stage, yet ends quietly as a white dwarf "
            "rather than as a supernova",
            "The claim is unsound, because no star that becomes a red "
            "giant has ever gone on to explode as a supernova",
        ],
        "correct_index": 2,
        "why": "Becoming a giant is about running out of core hydrogen, "
               "which happens to stars of many masses; only the much "
               "more massive ones go on to end in a supernova.",
    },
    {
        "id": "ks4-stellar-evolution-h26",
        "subtopic_slug": "stellar-evolution",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A star has been on the main sequence for a relatively "
                "short time and is expected to leave it after only "
                "about 10 million years in total. Deduce its most "
                "likely eventual fate.",
        "options": [
            "It will most likely end its days quietly as a white "
            "dwarf, since a short main-sequence lifetime like this "
            "one is typical of an ordinary star around the Sun's own "
            "mass",
            "Nothing about its eventual fate can be deduced from its "
            "main-sequence lifetime alone, whatever that lifetime "
            "turns out to be",
            "It will most likely fade directly into a cold black "
            "dwarf without delay, skipping every one of the other "
            "stages a star of any mass would usually pass through "
            "first",
            "It will most likely end its life as a supernova, since "
            "only a star far more massive than the Sun burns through "
            "its core hydrogen quickly enough to have such a short "
            "main-sequence lifetime",
        ],
        "correct_index": 3,
        "why": "A short main-sequence lifetime implies a large mass, "
               "and it is exactly the most massive stars whose lives "
               "end in a supernova.",
    },
]
