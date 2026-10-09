"""ks4_lessons.start_here — the "Start here" two-option guess for every live
KS4 lesson that was not built on it (Mide's rule 1, 2 Oct 2026,
docs/ks4/architecture.md): the 14 pilot lessons and the 29 batch 2–3 lessons.
Batches 4+ were authored by Design on `Ks4Guess` already and are not here.

One record per lesson slug. Each becomes Design's `Ks4Guess` block
(docs/ks4/design-reference/batch-4/lessons/Ks4Guess.dc.html):

  title, scene  — the opener's heading and one short paragraph
  question      — what follows "If you had to guess, " (lower-case start,
                  asks exactly what the two options answer)
  options       — exactly two (text, correct, reply); one is correct
  bridge        — shown under whichever reply; leads into the first teaching
  figure        — None, or the name of the lesson's existing logic key that
                  holds the opener's SVG string (passed as `figure-svg`)
  figure_alt    — optional `figure-alt` for that SVG
  logic_swaps   — optional exact (old, new) edits to the lesson's logic that
                  the swap needs (only ever the opener's own figure binding)

Batch 2–3 lessons are Code-authored, so tools/ks4_start_here.py writes these
records straight into their `.dc.html` sources. Pilot lessons are Design's
files and are never edited: ks4_rulings.apply_r18_start_here() swaps the
opener at build time, AFTER ks4_science_rulings, so every science correction
that touched an old opener is carried in the new text below instead.

Report: docs/ks4/START-HERE-REWRITE.md.
"""

PILOT = "pilot"
B2 = "batch-2"
B3 = "batch-3"


def O(text, correct, reply):
    return {"text": text, "correct": correct, "reply": reply}


def G(batch, title, scene, question, options, bridge, figure=None,
      figure_alt=None, logic_swaps=()):
    assert len(options) == 2 and sum(o["correct"] for o in options) == 1
    assert question[:1].islower() and question.endswith("?")
    return {"batch": batch, "title": title, "scene": scene, "question": question,
            "options": options, "bridge": bridge, "figure": figure,
            "figure_alt": figure_alt, "logic_swaps": list(logic_swaps)}


START_HERE = {
    # ─── batch 2 ─────────────────────────────────────────────────────────
    "atoms-elements-compounds": G(
        B2, "A metal that burns, a gas that poisons, a crystal you eat.",
        "Sodium is a soft metal that reacts violently with water. Chlorine is a "
        "toxic yellow-green gas. Bring the two together and you get sodium "
        "chloride: table salt, safe to sprinkle on food.",
        "are the sodium and chlorine in salt just mixed together, or joined up "
        "into something new?",
        [O("Just mixed together", False,
           "If they were only mixed, each would still behave as it did before, "
           "and salt would fizz in water. They have joined up into a new "
           "substance."),
         O("Joined up into something new", True,
           "They have chemically combined, and the new substance has "
           "properties of its own.")],
        "A substance made of two or more elements chemically combined is a "
        "compound. Next: atoms, elements, compounds and mixtures."),
    "carbon-cycle": G(
        B2, "A fallen leaf rots away. Its carbon does not.",
        "A leaf that drops in autumn has mostly vanished a year later. Yet the "
        "amount of carbon on Earth never changes: carbon atoms are not made or "
        "destroyed, only moved.",
        "did most of the leaf’s carbon go up into the air, or down into the "
        "soil?",
        [O("Up into the air", True,
           "Bacteria and fungi in the soil feed on the leaf and respire, "
           "releasing its carbon as carbon dioxide."),
         O("Down into the soil", False,
           "Some stays in the soil for a while, but bacteria and fungi keep "
           "feeding on it. As they respire, they release most of it into the "
           "air as carbon dioxide.")],
        "From the air, a plant can take that carbon in again. Next: follow one "
        "carbon atom round the cycle."),
    "carbonates-halides-sulfates": G(
        B2, "Five salts. Five tubes. Every one said chloride.",
        "A student tested five different white salts for halide ions. She "
        "acidified each solution with dilute hydrochloric acid, then added "
        "silver nitrate solution. Every tube gave a white precipitate, so she "
        "wrote “chloride” five times.",
        "did the chloride in every tube come from the salts, or from something "
        "she added?",
        [O("From the salts", False,
           "Five different salts giving one identical result is the clue. The "
           "hydrochloric acid she added brought chloride ions of its own."),
         O("From something she added", True,
           "Hydrochloric acid contains chloride ions, so every tube made white "
           "silver chloride, whatever the salt was.")],
        "The halide test is acidified with dilute nitric acid, which adds no "
        "halide ions. Next: the three tests, and the acid that goes with each.",
        figure="hookFig"),
    "changes-in-energy": G(
        B2, "Twice as fast. How much harder to stop?",
        "To stop a car, its brakes must transfer away all of its kinetic "
        "energy, and the brakes get hot. Now the same car is driven at twice "
        "the speed.",
        "do the brakes now have to transfer twice as much energy, or more than "
        "twice as much?",
        [O("Twice as much", False,
           "Twice the speed, twice the energy sounds right, and most people say "
           "it. In fact it is four times as much."),
         O("More than twice as much", True, "It is four times as much.")],
        "Kinetic energy depends on the speed squared: Ek = ½ m v². Next: kinetic "
        "energy and two other energy stores."),
    "chromosomes-mitosis": G(
        B2, "One fertilised egg. Trillions of cells.",
        "Every cell in your skin, muscles and gut came from one fertilised egg "
        "dividing again and again, and nearly every body cell still carries "
        "the same 46 chromosomes. Here is a model cell with just 4 chromosomes. It "
        "is about to divide into two cells, and each new cell needs all 4.",
        "does the cell copy its chromosomes before it divides, or share out the "
        "4 it has?",
        [O("Copy them first", True,
           "Every chromosome is copied, then one copy of each goes into each "
           "new cell."),
         O("Share out the 4 it has", False,
           "Then each new cell would get only 2, half a set. The cell copies "
           "every chromosome first, so each new cell gets all 4.")],
        "That is how a body cell with 46 chromosomes makes two cells with 46 "
        "each. Next: chromosomes and genes, then run the cell cycle.",
        figure="hookFig", figure_alt="{{ hookFigAlt }}",
        logic_swaps=[(
            "hookFig: ready ? K.fig(cellFig(D, 0).svg, cellFig(D, 0).alt) : null,",
            "hookFig: ready ? cellFig(D, 0).svg : '', hookFigAlt: ready ? cellFig(D, 0).alt : '',")]),
    "concentration-of-solutions": G(
        B2, "60 g of sugar in every litre.",
        "A sports drink label reads: carbohydrate 60 g/dm³. That number is a "
        "concentration: the mass of sugar dissolved in each dm³ of drink. One "
        "dm³ is one litre, or 1000 cm³. You pour yourself a 250 cm³ glass.",
        "is there about 15 g of sugar in your glass, or about 240 g?",
        [O("About 15 g", True,
           "250 cm³ is a quarter of a litre, so the glass holds a quarter of "
           "60 g."),
         O("About 240 g", False,
           "That is 60 × 4. A glass smaller than a litre must hold less than "
           "60 g: a quarter of it, 15 g.")],
        "Mass, volume and concentration are linked by one equation. Next: how "
        "to calculate a concentration."),
    "decomposition": G(
        B2, "A compost heap steams on a frosty morning.",
        "The air is below 0 °C, but a thermometer pushed into the middle of the "
        "heap of garden waste reads over 50 °C. Nothing is on fire, and there "
        "is no heater.",
        "is the heat coming from sunshine soaked up in the day, or from living "
        "things inside the heap?",
        [O("Sunshine soaked up in the day", False,
           "Winter sun is weak, and the heap is hottest in the middle, where no "
           "light reaches. The warmth comes from living things inside it."),
         O("Living things inside the heap", True,
           "Bacteria and fungi are feeding on the waste. As they feed, they "
           "respire, and respiration releases energy.")],
        "Some of the energy they release warms the heap. Next: what happens to "
        "a fallen leaf as it decays."),
    "enzymes": G(
        B2, "Chew a plain cracker for a minute. It starts to taste sweet.",
        "A cracker is mostly starch, and starch does not taste sweet. Keep a "
        "piece in your mouth without swallowing, and after a minute or so it "
        "tastes sugary.",
        "is the sugar made by the chewing, or by something in your saliva?",
        [O("By the chewing", False,
           "Chewing breaks the cracker into smaller pieces, but the pieces are "
           "still starch. Something in saliva is turning the starch into "
           "sugar."),
         O("By something in your saliva", True,
           "Saliva contains amylase, an enzyme that breaks starch down into "
           "sugars.")],
        "Without an enzyme, that reaction would be far too slow to notice at "
        "body temperature. Next: what enzymes are, and why each one works on "
        "only one kind of substance."),
    "eukaryotes-prokaryotes": G(
        B2, "A liver cell and a bacterium, drawn to the same scale.",
        "Both are living cells, and both need DNA to make their proteins. The "
        "liver cell keeps its DNA inside a nucleus.",
        "is the bacterium’s DNA inside a nucleus too, or loose in the cell?",
        [O("Inside a nucleus too", False,
           "Most people expect that, because it is where our cells keep theirs. "
           "A bacterium has no nucleus: its DNA is loose in the cytoplasm."),
         O("Loose in the cell", True,
           "A bacterium has no nucleus. Its DNA is a single loop, loose in the "
           "cytoplasm.")],
        "Cells with a nucleus are eukaryotic; bacteria are prokaryotic. Next: "
        "build the two cells and see what else differs.",
        figure="hookFig",
        figure_alt="A liver cell and a bacterium drawn to the same scale",
        logic_swaps=[(
            "hookFig: ready ? K.fig(hookFig(D), 'A liver cell and a bacterium drawn to the same scale') : null,",
            "hookFig: ready ? hookFig(D) : '',")]),
    "internal-energy": G(
        B2, "Turn the gas up under boiling water.",
        "A pan of water is boiling on a hob. A thermometer in the water reads "
        "100 °C. You turn the flame up to full and keep it there.",
        "while the water keeps boiling, does the thermometer reading go up, or "
        "stay at 100 °C?",
        [O("It goes up", False,
           "More energy is going in, so a rise makes sense. But while the water "
           "boils, it stays at 100 °C and boils away faster."),
         O("It stays at 100 °C", True,
           "The water just boils away faster.")],
        "The extra energy is still going into the water, but it changes the "
        "water’s state instead of its temperature. Next: the two ways "
        "particles store energy."),
    "lenses": G(
        B2, "One magnifying glass, a page and a window.",
        "Hold a magnifying glass just above a page and the words look bigger "
        "and the right way up. Now hold the same lens at arm’s length and look "
        "through it at a window across the room.",
        "do you see the window the right way up, or upside down?",
        [O("The right way up", False,
           "That is what the lens does to a page held close. With the window "
           "far away, the picture is small and upside down."),
         O("Upside down", True,
           "And smaller too. The same lens has made a different kind of "
           "image.")],
        "Where the object is, compared with the lens’s focal length, decides "
        "the image. Next: how a lens bends light, and how to find the image "
        "with two rays."),
    "metal-hydroxides": G(
        B2, "Blue solution in. Blue solid out.",
        "Copper(II) sulfate solution is clear and blue. Add a few drops of "
        "colourless sodium hydroxide solution and a pale blue solid appears, "
        "swirls, and slowly sinks to the bottom of the tube.",
        "is the blue solid a new substance, or copper sulfate coming back out "
        "of the solution?",
        [O("A new substance", True,
           "It is copper(II) hydroxide: copper ions from one solution met "
           "hydroxide ions from the other."),
         O("Copper sulfate coming back out", False,
           "Copper sulfate dissolves easily, and adding sodium hydroxide does not "
           "change that. The copper ions have joined hydroxide ions to make a "
           "new compound, copper(II) hydroxide.")],
        "Copper(II) hydroxide is insoluble, so it comes out as a solid: a "
        "precipitate. Next: how sodium hydroxide tests for metal ions.",
        figure="hookFig"),
    "percentage-yield": G(
        B2, "8.0 g on paper. 6.2 g in the dish.",
        "A student makes copper sulfate crystals from copper oxide and "
        "sulfuric acid. From the balanced equation, the reactants they used "
        "can make 8.0 g at most. After filtering, crystallising and drying, "
        "the balance reads 6.2 g.",
        "was the missing 1.8 g destroyed in the reaction, or left behind along "
        "the way?",
        [O("Destroyed in the reaction", False,
           "Atoms are never destroyed in a reaction. The 1.8 g is still "
           "somewhere, just not in the dish."),
         O("Left behind along the way", True,
           "Some copper sulfate stayed in the filter paper, on the glassware "
           "and in the solution.")],
        "The 8.0 g is the theoretical yield and the 6.2 g is the actual yield. "
        "Next: follow the copper sulfate through the practical."),
    "relative-formula-mass": G(
        B2, "Three atoms against two.",
        "A water molecule, H₂O, has three atoms. An oxygen molecule, O₂, has "
        "two. Atoms of different elements have different masses: on the "
        "periodic table, hydrogen is 1 and oxygen is 16.",
        "which molecule has the greater mass: the water, or the oxygen?",
        [O("The water", False,
           "More atoms does not always mean more mass: two of water’s three "
           "atoms are hydrogen, the lightest of all. H₂O is 1 + 1 + 16 = 18; "
           "O₂ is 16 + 16 = 32."),
         O("The oxygen", True,
           "Add up the masses: H₂O is 1 + 1 + 16 = 18, and O₂ is 16 + 16 = "
           "32.")],
        "Adding up the masses of the atoms in a formula gives its relative "
        "formula mass. Next: how to count the atoms in any formula."),
    "titrations": G(
        B2, "One drop turns the whole flask.",
        "A conical flask holds 25.00 cm³ of sodium hydroxide solution and a "
        "few drops of phenolphthalein, so it is pink. Acid runs in from a "
        "burette. Near the end, each splash makes a colourless patch that "
        "vanishes when the flask is swirled. Then, after one more drop, the "
        "pink is gone for good.",
        "has the indicator been used up, or has the alkali been neutralised?",
        [O("The indicator has been used up", False,
           "The indicator is still there. It changes colour because the "
           "solution is no longer alkaline."),
         O("The alkali has been neutralised", True,
           "The acid has exactly neutralised the alkali. This is the end "
           "point.")],
        "The volume of acid needed to reach the end point is the titre. Next: "
        "the AQA method, step by step."),
    "using-moles-calculations": G(
        B2, "The fizzing stops. Something ran out.",
        "Magnesium fizzes in hydrochloric acid, giving off hydrogen gas: Mg + "
        "2HCl → MgCl₂ + H₂. A student mixes 2.4 g of magnesium with 3.65 g of "
        "hydrogen chloride dissolved in water. After a while the fizzing "
        "stops.",
        "which ran out: the magnesium, or the hydrogen chloride?",
        [O("The magnesium", False,
           "There is less magnesium by mass, but reactions go by numbers of "
           "particles, not by mass. Each Mg needs two HCl, so the hydrogen "
           "chloride runs out and some magnesium is left over."),
         O("The hydrogen chloride", True,
           "There is 0.1 mol of each, but each Mg needs two HCl. The hydrogen "
           "chloride runs out, and magnesium is left over.")],
        "Next: the limiting reactant, and how to find it from the masses."),

    # ─── batch 3 ─────────────────────────────────────────────────────────
    "atom-economy": G(
        B3, "Two factories. One product.",
        "Both factories make ethanol, C₂H₅OH. Factory A ferments sugar: "
        "C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂. Factory B adds steam to ethene: C₂H₄ + H₂O "
        "→ C₂H₅OH. Both run perfectly: every molecule of starting material "
        "reacts.",
        "which factory turns the bigger share of its starting materials’ mass "
        "into ethanol: A or B?",
        [O("Factory A", False,
           "Each sugar molecule does make two ethanol molecules, but two carbon "
           "dioxide molecules leave with them, carrying off almost half the "
           "mass."),
         O("Factory B", True,
           "Ethanol is the only product, so every atom of the ethene and steam "
           "ends up in it.")],
        "Factory A does not want its carbon dioxide, so not all of its starting "
        "mass becomes useful product. Next: put a number on the share that "
        "does."),
    "conservation-of-mass": G(
        B3, "A spark in a sealed flask.",
        "A thick glass flask holds methane and oxygen. The stopper is clamped "
        "shut, and the flask sits on a balance reading 312.48 g. A spark sets "
        "the methane burning. A flash, and then droplets of water run down the "
        "inside of the glass.",
        "once the flask has cooled, does the balance read less than 312.48 g, "
        "or exactly the same?",
        [O("Less than 312.48 g", False,
           "The methane and oxygen were used up, but every one of their atoms "
           "is still in the flask, now in carbon dioxide and water."),
         O("Exactly 312.48 g", True,
           "Nothing entered or left the sealed flask, so the mass stays the "
           "same.")],
        "A flash, new substances, and still the same reading. Next: the law "
        "behind it."),
    "early-atmosphere": G(
        B3, "Venus and Mars may still have the kind of air Earth started with.",
        "Scientists think Earth’s air, about 4 billion years ago, was mainly "
        "carbon dioxide, like theirs. Compare it with Earth’s air today.",
        "is most of the carbon from all that carbon dioxide now locked "
        "underground, or inside living things?",
        [O("Locked underground", True,
           "Most of it is in sedimentary rocks such as limestone, and in fossil "
           "fuels."),
         O("Inside living things", False,
           "Living things hold some of it, but only a small share. Far more is "
           "locked underground, in rocks such as limestone and in fossil "
           "fuels.")],
        "Getting it there took about 4 billion years. Next: run the clock on "
        "how Earth’s air changed.",
        figure="hookFig"),
    "greenhouse-gases": G(
        B3, "Take away three gases and Earth would average about −18 °C.",
        "Today the Earth’s surface averages about 15 °C. Same Sun, same "
        "distance, same ground. The difference is made by water vapour, carbon "
        "dioxide and methane in the air.",
        "do those gases keep the surface warm by reflecting sunlight back down, "
        "or by soaking up heat given off by the ground?",
        [O("Reflecting sunlight back down", False,
           "That is what most people think. In fact the gases absorb the heat "
           "the warm ground gives off, and send some of it back down."),
         O("Soaking up heat from the ground", True,
           "The warm ground gives off heat, and the gases absorb some of it and "
           "send some back down.")],
        "Sunlight passes through those gases, but the heat from the ground does "
        "not get through so easily. Next: why the two are different."),
    "microscopy": G(
        B3, "Your cells are full of ribosomes. For nearly 300 years, nobody saw "
        "one.",
        "Robert Hooke looked at cork through a microscope in 1665 and named the "
        "tiny boxes he saw cells. Better and better light microscopes followed. "
        "Ribosomes were there all along, and none of those microscopes ever "
        "showed one.",
        "to see a ribosome, what would you need most: a microscope that makes "
        "things even bigger, or one that shows finer detail?",
        [O("One that makes things even bigger", False,
           "You need a big image too, but enlarging a blur only gives a bigger "
           "blur. The microscope has to show two very close points as "
           "separate."),
         O("One that shows finer detail", True,
           "Ribosomes are only about 20 nm across. The microscope has to show "
           "two points that close together as separate.")],
        "Ribosomes were first seen in the 1950s, with an electron microscope. "
        "Next: magnification, resolution, and the two kinds of microscope."),
    "mixtures": G(
        B3, "A spoonful of sugar in hot water.",
        "The crystals vanish. The water looks exactly as clear as before, but "
        "it now tastes sweet.",
        "is it still sugar, or has it turned into something new?",
        [O("Still sugar", True,
           "It is spread through the water, mixed but not chemically "
           "combined."),
         O("Something new", False,
           "A reaction would make a new substance, but this still tastes of "
           "sugar.")],
        "Let the water evaporate and the sugar comes back, unchanged. Next: "
        "mixtures, and five ways to separate them."),
    "particle-motion-pressure": G(
        B3, "“Do not burn, even after use.”",
        "Every aerosol can carries that warning. An “empty” can is not empty: "
        "once the spray runs out, it is still sealed and still full of gas.",
        "when the can heats up on a fire, does it burst because the leftover gas "
        "catches fire inside it, or because the hot gas pushes harder on the "
        "walls?",
        [O("The gas catches fire inside", False,
           "Even a can holding only air, which cannot burn, would burst. As the "
           "gas heats up, it pushes harder and harder on the walls."),
         O("The hot gas pushes harder", True,
           "The can is sealed, so the hot gas cannot escape, and its push on "
           "the walls keeps growing until the metal splits.")],
        "What the gas particles do to push harder is yours to work out on the "
        "bench. Next: what that push is."),
    "power": G(
        B3, "Two kettles, one cup of tea.",
        "A 3000 W kettle and a 1500 W kettle each heat 0.5 kg of water from "
        "20 °C to 100 °C. The 3000 W kettle finishes first.",
        "does the 3000 W kettle transfer more energy to the water, or the same "
        "energy, faster?",
        [O("More energy", False,
           "More watts means faster, not more. Both warm the same water through "
           "the same temperature rise, so both transfer the same energy."),
         O("The same energy, faster", True,
           "The same water through the same temperature rise takes the same "
           "energy. The 3000 W kettle transfers it faster.")],
        "What the 3000 W kettle has more of is power. Next: what a watt means."),
    "sound-waves-hearing": G(
        B3, "A whistle that only the dog can hear.",
        "A trainer blows a dog whistle. Across the park, the dog’s head snaps "
        "round. The trainer, with the whistle at her lips, hears nothing at "
        "all.",
        "does she hear nothing because the whistle is too quiet, or because "
        "its note is too high?",
        [O("It is too quiet", False,
           "She has it right at her lips, where it is loudest, and still hears "
           "nothing. Its note is too high for a human ear."),
         O("Its note is too high", True,
           "Its frequency is too high for a human ear, but not for a dog’s.")],
        "A human ear only hears sounds within a certain range of frequencies. "
        "Next: what a sound wave is, and how your ear turns it into something "
        "you hear."),
    "specific-latent-heat": G(
        B3, "Same temperature, worse burn.",
        "A splash of boiling water on your hand hurts. A puff of steam from a "
        "kettle spout, at the same 100 °C, can leave a much worse burn.",
        "is the steam worse because it spreads over more skin, or because it "
        "gives the skin more energy?",
        [O("It spreads over more skin", False,
           "Even the same mass on the same patch of skin burns worse. Steam has "
           "to turn back into water first, and that gives out a lot of "
           "energy."),
         O("It gives the skin more energy", True,
           "Steam condenses into water on your skin, and condensing gives out a "
           "lot of energy with no change in temperature.")],
        "Then that water cools, just as the boiling water does. Next: the "
        "energy needed to change state."),
    "temperature-changes-shc": G(
        B3, "Sand and sea, same sunshine.",
        "On a sunny afternoon at the beach, the dry sand and the sea next to it "
        "get the same sunshine all day.",
        "if 1 kg of dry sand and 1 kg of seawater get exactly the same energy, "
        "which warms up more?",
        [O("The sand", True,
           "Dry sand needs only about a fifth of the energy per degree that "
           "water does."),
         O("The seawater", False,
           "Water needs far more energy for each degree than sand does, so the "
           "same energy warms it much less.")],
        "That is why dry sand can get too hot to walk on while the sea stays "
        "cool. Next: the three things that decide a temperature rise."),
    "types-of-em-waves": G(
        B3, "Your phone is sending a wave to the nearest mast right now.",
        "The phone signal, the warmth you feel from a fire, the light from this "
        "screen, the ultraviolet that tans skin and the X-rays that photograph "
        "a broken bone are one family of waves: electromagnetic waves.",
        "can your eyes detect most of that family, or only a small part of "
        "it?",
        [O("Most of it", False,
           "The rest are all around you: phone signals, radio, and the Sun’s "
           "infrared and ultraviolet. Your eyes just do not respond to them."),
         O("Only a small part", True,
           "Your eyes only respond to visible light, from red to violet.")],
        "Visible light is one group of seven. The other six are just as real: "
        "an aerial, a camera sensor or your skin can detect them. Next: what "
        "all seven have in common."),
    "waves-detection-exploration": G(
        B3, "Nobody has ever seen the Earth’s core.",
        "It lies thousands of kilometres beneath your feet, and no drill has "
        "come anywhere near it. Yet geologists can tell you how big the core "
        "is, and that part of it is liquid.",
        "does their evidence come from lava, or from earthquake waves?",
        [O("Lava", False,
           "Lava comes from far nearer the surface than the core, so it carries "
           "no sample of it. The evidence is earthquake waves."),
         O("Earthquake waves", True,
           "Earthquakes send waves right through the Earth, and instruments all "
           "over the world record them.")],
        "The way those waves pass through the Earth, or fail to, is the "
        "evidence. Next: the two kinds of earthquake wave."),

    # ─── the pilot (Design's files; swapped at build by ks4_rulings R18) ──
    "chemical-bonds": G(
        PILOT, "Same chlorine. Two partners. Two different worlds.",
        "Sodium is a soft metal that fizzes on water. Chlorine is a poisonous "
        "green gas. Together they make table salt: a white crystal that stays "
        "solid until 801 °C. Swap sodium for hydrogen and chlorine makes "
        "hydrogen chloride, which stays a gas until it is cooled below "
        "−85 °C.",
        "what makes the difference: whether chlorine’s partner is a metal, or "
        "how heavy the partner’s atoms are?",
        [O("Whether its partner is a metal", True,
           "Sodium is a metal; hydrogen is not, even though, like sodium, it "
           "has one outer electron."),
         O("How heavy its partner’s atoms are", False,
           "Mass does not decide which type of bond forms. Sodium is a metal "
           "and hydrogen is not, and that changes how each bonds with "
           "chlorine.")],
        "A metal gives electrons to chlorine and they form ions; hydrogen "
        "shares electrons with chlorine and makes small molecules. Next: the "
        "three ways atoms bond."),
    "ionic-bonding": G(
        PILOT, "Hot sodium, a jar of chlorine, a flash of yellow light.",
        "Drop hot sodium into chlorine gas and it burns with a bright yellow "
        "flame. When the smoke clears, the jar is coated in white crystals of "
        "sodium chloride. A sodium atom has one electron in its outer shell. "
        "A chlorine atom has seven.",
        "does sodium’s outer electron move across to the chlorine, or do the "
        "two atoms share it?",
        [O("It moves across to the chlorine", True,
           "Sodium loses its outer electron and chlorine gains it, so both end "
           "up with a full outer shell."),
         O("The two atoms share it", False,
           "Sharing does happen, between two non-metals. Sodium is a metal: "
           "its outer electron moves across to the chlorine.")],
        "Each atom becomes a charged particle, an ion, and the white crystals "
        "are made of these. Next: watch the transfer one step at a time."),
    "ionic-compounds": G(
        PILOT, "Crush a salt crystal. You get smaller cubes.",
        "Look at table salt through a hand lens and every grain is a tiny cube "
        "with flat faces and square corners. Crush one and the fragments break "
        "along flat faces into smaller cubes. Grow salt slowly from a solution "
        "and you get cubes the size of dice.",
        "is that because each salt particle is a tiny cube, or because the "
        "particles stack in a pattern that repeats?",
        [O("Each particle is a tiny cube", False,
           "A neat idea, but the shape comes from how the particles are "
           "arranged. They stack in one pattern that repeats, and the pattern "
           "is a cube."),
         O("They stack in a pattern that repeats", True,
           "One regular pattern repeats all the way through the crystal.")],
        "Salt’s repeat is a cube of alternating sodium and chloride ions, so it "
        "grows, and breaks, along square faces. Next: the giant ionic "
        "lattice."),
    "covalent-bonding": G(
        PILOT, "Two hydrogen atoms. One electron each. Both need two.",
        "Hydrogen gas is not made of single atoms. It is made of H₂ molecules, "
        "and pulling one apart takes a lot of energy. Yet each hydrogen atom "
        "has only one electron, and a full first shell needs two.",
        "can both atoms have a full shell at the same time, or only one of "
        "them?",
        [O("Both at the same time", True,
           "They share their two electrons as a pair, and the pair counts for "
           "both atoms."),
         O("Only one of them", False,
           "If one atom gave its electron away, it would have none left. "
           "Instead they share the pair, and it counts for both.")],
        "Sharing is how two non-metal atoms bond. Next: what holds the shared "
        "pair in place, and how many bonds each atom forms."),
    "metallic-bonding": G(
        PILOT, "A grain of gold, hammered into a sheet the size of a tablecloth.",
        "Gold-beaters hammer one gram of gold into a sheet close to a square "
        "metre in area, only a few hundred atoms thick. It never cracks. Hit a "
        "grain of salt, another giant structure of charged particles, and it "
        "shatters at the first blow.",
        "does gold bend because its particles are softer, or because they can "
        "slide past each other?",
        [O("Its particles are softer", False,
           "It is not the particles themselves that are soft. Layers of them "
           "slide past each other, and the bonding holds them together as they "
           "move."),
         O("They can slide past each other", True,
           "Layers of particles slide over one another, and the whole "
           "structure stays bonded. Salt has no way to do that.")],
        "The difference lies in what holds each structure together. Next: the "
        "bond inside a metal."),
    "states-of-matter": G(
        PILOT, "A tube of white wax in a hot-water bath.",
        "A student puts a boiling tube of solid stearic acid, a waxy "
        "substance, into a beaker of water at 90 °C. She stirs the wax with "
        "the thermometer and reads the temperature every 30 seconds for ten "
        "minutes. The water bath never stops heating the tube.",
        "while the wax is melting, does the thermometer reading keep rising, "
        "or stay about the same?",
        [O("It keeps rising", False,
           "Energy keeps going in, so rising makes sense. But while the wax "
           "melts, the reading stays almost flat."),
         O("It stays about the same", True,
           "The reading stays almost flat until all the wax has melted.")],
        "The water bath is still supplying energy, but the energy goes into "
        "overcoming the forces between the particles, not into making them "
        "move faster. Next: solids, liquids and gases."),
    "properties-ionic-compounds": G(
        PILOT, "Two probes, one bulb, a pile of salt crystals.",
        "Push two carbon probes into a heap of dry salt crystals and connect "
        "them to a battery and a bulb. The bulb stays dark. Every crystal is "
        "packed with Na⁺ and Cl⁻ ions: billions of charged particles, right "
        "between the probes.",
        "is the bulb dark because the charges cancel out, or because the ions "
        "cannot move?",
        [O("The charges cancel out", False,
           "They do balance overall, but they balance in molten salt too, and "
           "molten salt conducts. In the solid, the ions cannot move."),
         O("The ions cannot move", True,
           "The ions are locked in place. They have charge, but they cannot "
           "move, so no charge can flow.")],
        "Next: set the ions free and see what the bulb does."),
    "properties-small-molecules": G(
        PILOT, "A kettle of water. A bubble of steam.",
        "Water boils at 100 °C. Splitting water into hydrogen and oxygen needs "
        "an electric current running through it for minutes, or a temperature "
        "of thousands of degrees. Both processes start with the same H₂O "
        "molecules.",
        "is a bubble of steam full of water molecules, or of hydrogen and "
        "oxygen?",
        [O("Water molecules", True,
           "Whole H₂O molecules, far apart and moving fast."),
         O("Hydrogen and oxygen", False,
           "Then boiling would split water, and splitting water takes far more "
           "than a kettle. Steam is whole H₂O molecules, far apart.")],
        "Boiling pulls whole molecules away from each other. The bonds inside "
        "each molecule are untouched. Next: the two kinds of attraction in a "
        "small-molecule substance."),
    "polymers": G(
        PILOT, "Same atoms. One is a gas, one is a carrier bag.",
        "An ethene molecule, C₂H₄, has six atoms. It boils at −104 °C. A single "
        "molecule of poly(ethene) in a carrier bag is a chain of many thousands "
        "of carbon atoms, each with two hydrogens. The bag stays solid until it "
        "softens at over 100 °C.",
        "is poly(ethene) solid because the bonds inside its molecules are "
        "stronger, or because its molecules are much bigger?",
        [O("The bonds inside are stronger", False,
           "Both are held together inside by the same kind of strong covalent "
           "bonds. The difference is size: poly(ethene) molecules are "
           "thousands of times bigger."),
         O("Its molecules are much bigger", True,
           "Much bigger molecules mean much stronger forces between them, "
           "strong enough to hold the chains in place at room temperature.")],
        "Both substances are made of molecules; what changes is their size. "
        "Next: what a polymer is."),
    "giant-covalent-structures": G(
        PILOT, "A drill bit and a pencil. Both carbon.",
        "Diamond-tipped drills cut through granite. Graphite, the grey “lead” "
        "in a pencil, is so soft it rubs off onto paper and is used to "
        "lubricate locks, yet it carries a current well enough to be used as "
        "electrodes. Neither melts until it is hotter than 3500 °C.",
        "is graphite soft because it has something else mixed in, or because "
        "its carbon atoms are joined differently?",
        [O("It has something else mixed in", False,
           "Pencil lead does have clay in it, but pure graphite is just as "
           "soft. What differs is how the carbon atoms are joined."),
         O("Its atoms are joined differently", True,
           "The atoms are the same; the bonding is not.")],
        "How many bonds each carbon atom forms decides whether you get a rigid "
        "network or stacked layers. Next: giant covalent structures."),
    "metals-alloys": G(
        PILOT, "24-carat gold scratches. 18-carat gold lasts a lifetime.",
        "Pure, 24-carat gold is so soft that a ring made from it dents and "
        "scratches in weeks. Many wedding rings are 18-carat: three parts gold "
        "mixed with one part of other metals such as copper and silver. They "
        "keep their shape for decades.",
        "does mixing in other metals make gold harder by reacting with it, or "
        "by getting in the way of its layers?",
        [O("By reacting with it", False,
           "An alloy is a mixture: no new compound forms. Copper atoms are a "
           "different size from gold atoms, so they distort the gold’s "
           "layers."),
         O("By getting in the way of its layers", True,
           "Copper atoms are a different size from gold atoms, so they distort "
           "the neat layers.")],
        "Distorted layers cannot slide past each other easily, so the alloy "
        "keeps its shape. Next: why pure metals bend in the first place."),
    "nanoparticles": G(
        PILOT, "A red glass window, coloured with gold.",
        "Medieval glassmakers turned windows ruby-red by stirring in a trace of "
        "gold. The gold spreads through the glass as particles around 25 nm "
        "across, too small to see. A lump of gold looks gold; these tiny specks "
        "make the glass red.",
        "does gold behave differently at this size because its atoms change, or "
        "because a far bigger share of them sit at the surface?",
        [O("Its atoms change", False,
           "A gold atom is the same in a ring or in glass. What changes is "
           "where the atoms are: in a tiny particle, a far bigger share of them "
           "sit at the surface."),
         O("A far bigger share sit at the surface", True,
           "In a 25 nm particle, a far larger fraction of the atoms sit on the "
           "surface, where they meet light and other chemicals.")],
        "That is where the new properties come from. Next: how small "
        "nanoparticles are."),
    "resistors": G(
        PILOT, "A bulb takes a big gulp of current, then settles.",
        "Switch on an old filament bulb and, for the first fraction of a "
        "second, it draws several times more current than it does once it is "
        "glowing. Filament bulbs usually blow at the moment they are switched "
        "on, not while they are lit.",
        "does the cold filament have a lower resistance than the hot one, or a "
        "higher one?",
        [O("Lower", True,
           "A cold filament has a much lower resistance, so the first rush of "
           "current is large."),
         O("Higher", False,
           "Then it would draw less current at first, not more. A cold "
           "filament has a lower resistance.")],
        "As the filament heats up, its resistance rises and the current falls. "
        "That is what makes a lamp’s I–V graph a curve. Next: the required "
        "practical."),
    "series-parallel-circuits": G(
        PILOT, "A 4 Ω resistor and an 8 Ω resistor, one 12 V battery.",
        "The two resistors are in series with the battery.",
        "which resistor gets the bigger share of the battery’s 12 V: the 4 Ω, "
        "or the 8 Ω?",
        [O("The 4 Ω resistor", False,
           "Tempting, because it lets current through more easily. But in "
           "series both carry the same current, so the bigger resistance takes "
           "the bigger share."),
         O("The 8 Ω resistor", True,
           "Both carry the same current, so the bigger resistance takes the "
           "bigger share.")],
        "4 V across the 4 Ω and 8 V across the 8 Ω add up to the battery’s "
        "12 V. Next: the rules for series and parallel circuits.",
        figure="hookFig",
        logic_swaps=[(
            "hookFig: ready ? K.fig(this.fig(CFG[0], false), '') : null,",
            "hookFig: ready ? this.fig(CFG[0], false) : '',")]),
}


def for_batch(batch):
    return {slug: rec for slug, rec in START_HERE.items() if rec["batch"] == batch}


# ─── rendering (used by tools/ks4_start_here.py) ─────────────────────────
import re as _re


def _attr(v):
    return v.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def _attr_keep_binding(v):
    """Escape, but leave a `{{ … }}` binding untouched."""
    parts = _re.split(r"(\{\{.*?\}\})", v)
    return "".join(p if p.startswith("{{") else _attr(p) for p in parts)


def _js(v):
    return v.replace("\\", "\\\\").replace("'", "\\'")


def render_section(slug):
    r = START_HERE[slug]
    a = ['title="%s"' % _attr(r["title"]), 'scene="%s"' % _attr(r["scene"]),
         'question="%s"' % _attr(r["question"])]
    if r["figure"]:
        a.append('figure-svg="{{ %s }}"' % r["figure"])
        if r["figure_alt"]:
            a.append('figure-alt="%s"' % _attr_keep_binding(r["figure_alt"]))
    a += ['options="{{ hookOptions }}"', 'bridge="%s"' % _attr(r["bridge"]),
          'on-commit="{{ onHook }}"', 'hint-size="100%,420px"']
    return ('<section id="s-hook" class="ks3-block ks3-hook" style="scroll-margin-top: 92px;">\n'
            '        <dc-import name="Ks4Guess" %s></dc-import>\n'
            '      </section>' % " ".join(a))


def render_options_js(slug):
    rows = ["        { text: '%s', correct: %s, reply: '%s' }"
            % (_js(o["text"]), "true" if o["correct"] else "false", _js(o["reply"]))
            for o in START_HERE[slug]["options"]]
    return "hookOptions: [\n%s\n      ],\n      " % ",\n".join(rows)
