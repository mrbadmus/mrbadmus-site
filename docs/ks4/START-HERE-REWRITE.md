# KS4 "Start here" rewrite — every live lesson onto the two-option guess

**Run:** 8–9 Oct 2026, unattended. Branch `feat/ks4-start-here`.
**Rule:** Mide's rule 1 (2 Oct 2026, `docs/ks4/architecture.md`): "Start here" is a
two-option guess — "If you had to guess, …?" — in everyday wording any pupil on any
route can answer, not patronising for Triple Higher, not giving the answer away in
the title or scene, with a friendly reply to each option that leads into the
teaching.

## What changed

43 live KS4 lessons opened on a 3–4-option `Ks4Choice` test ("Commit first"):
the 14 pilot lessons and the 29 lessons of batches 2 and 3 (confirmed from the
code: every other live lesson, batches 4 and 5, already mounts `Ks4Guess`). Each
now opens on Design's own `Ks4Guess` block — the one batches 4–5 use — with a new
two-option guess written from that lesson's own science.

**Only the opener changed.** On every page the `#s-hook` section and its
`hookOptions`/`hookReveal` constants are replaced; nothing else in the lesson
moved. No quiz item, frozen content, flashcard, class page or B2C file was
touched (`frozen_window_guard` green). Batches 4–6 untouched. Pages of lessons
not in the 43 are byte-identical to main.

| Where | What |
|---|---|
| `ks4_lessons/start_here.py` | All 43 openers as data: title, scene, question, two options (each with its reply), bridge. The single source of the new text. |
| `tools/ks4_start_here.py` | `--apply` / `--refresh` / `--check`: writes a record into a batch 2–3 source (exact anchors, fails loud), and checks every applied lesson still matches the data. |
| `ks4_rulings.py` R18 | The pilot is Design's files, never edited: R18 swaps the opener at build time, **after** `ks4_science_rulings`, so every science correction that touched an old pilot opener still fires, and its correction is carried in the new text. |
| `build_ks4.py` | Compiles Design's `Ks4Guess` (batch-4 copy) for the pilot and batches 2–3 and registers it **only on a page whose lesson uses it**. No CSS change anywhere: `Ks4Guess`'s only `<style>` is already in `shared/ks4-lesson.css`. |
| `ks4_parity.py` | The pilot's Design-fidelity gate now **proves** each pilot opener (every rendered piece present, in order, old hook gone) instead of comparing it with Design's old hook — the same pattern as R13's approved exam tips. |

## How the science was checked

Each opener was written from its lesson's own taught content (the section after
the hook, the old reveal, the pack's checked science source) and read against
Design's 13 batch-4 openers. Three fresh Opus reviewers then read every opener
against its whole lesson, its `ks4_science_rulings` rows and its examination
notes — one per group (pilot, batch 2, batch 3). All 43 correct options were
confirmed correct by AQA; 30 openers had wording changes, all applied. The ones
that mattered for the science:

- **nanoparticles** — "far more atoms at the surface" is wrong in absolute
  terms (a ring has more surface atoms than one particle); now "a far bigger
  share". The draft scene also gave the answer away.
- **polymers** — "the same C–C and C–H bonds in both" is untrue for ethene
  (C=C), which the same page teaches; reworded.
- **metals-alloys** — replies name copper, not "the added atoms": silver is the
  same size as gold (`metals-alloys-C3`).
- **chemical-bonds** — keeps `chemical-bonds-C1` (hydrogen is *not* "above
  sodium" in the table) and `-C9`.
- **particle-motion-pressure** — the first draft (bigger vs faster particles)
  answered the lesson's own gas-bench predictions in advance; now fire vs push.
- **microscopy** — "a microscope that makes things bigger" could be argued
  right (the electron microscope also magnifies more); now asks what you need
  *most*.
- **carbonates-halides-sulfates** — the question now asks where the *chloride*
  came from (the silver always comes from the silver nitrate).
- **temperature-changes-shc**, **lenses**, **atoms-elements-compounds** — the
  title or scene stated the result; reworded.

Each reply reads after the block's own "Good guess." / "Fair guess."; bridges
were cut where they repeated the next paragraph (Mide's no-redundant-text rule).

## The 43 openers

Routes: CF/CH = Combined Foundation/Higher, TF/TH = Triple Foundation/Higher. "Old opener" is the question and options the page carried on main before this run. The "why" is the reply a pupil sees for the correct option.

### Pilot (Design's files, swapped by ruling R18)

| Lesson | Route(s) | Old opener | New question and two options | Correct option, and why |
|---|---|---|---|---|
| chemical-bonds | CF CH TF TH | What decides whether chlorine ends up in a high-melting crystal or in a gas?<br>4 options: Whether its partner is a metal or a non-metal / How heavy its partner’s atoms are / How reactive its partner is / How many chlorine atoms join on | If you had to guess, what makes the difference: whether chlorine’s partner is a metal, or how heavy the partner’s atoms are?<br>**This:** Whether its partner is a metal<br>**Or this:** How heavy its partner’s atoms are | **Whether its partner is a metal.** Sodium is a metal; hydrogen is not, even though, like sodium, it has one outer electron. |
| ionic-bonding | CF CH TF TH | Where does sodium's single outer electron end up?<br>4 options: It moves across to the chlorine atom / The two atoms share it between them / It stays on sodium; the atoms just stick / It is given off as the yellow light | If you had to guess, does sodium’s outer electron move across to the chlorine, or do the two atoms share it?<br>**This:** It moves across to the chlorine<br>**Or this:** The two atoms share it | **It moves across to the chlorine.** Sodium loses its outer electron and chlorine gains it, so both end up with a full outer shell. |
| ionic-compounds | CF CH TF TH | Why does salt come out as cubes at every size?<br>4 options: The particles inside stack in one regular pattern that repeats / Salt molecules are shaped like tiny cubes / Factories cut salt into cubes / Water shapes the grains as it evaporates | If you had to guess, is that because each salt particle is a tiny cube, or because the particles stack in a pattern that repeats?<br>**This:** Each particle is a tiny cube<br>**Or this:** They stack in a pattern that repeats | **They stack in a pattern that repeats.** One regular pattern repeats all the way through the crystal. |
| covalent-bonding | CF CH TF TH | How can both hydrogen atoms have a full shell at the same time?<br>4 options: They share their two electrons, and both count the pair as their own / One gives its electron to the other, making ions / They borrow electrons from the air around them / They cannot: H₂ has half-empty shells | If you had to guess, can both atoms have a full shell at the same time, or only one of them?<br>**This:** Both at the same time<br>**Or this:** Only one of them | **Both at the same time.** They share their two electrons as a pair, and the pair counts for both atoms. |
| metallic-bonding | CF CH TF TH | What must be true inside gold for it to bend instead of break?<br>4 options: Its particles can shift past each other without the bonding breaking / Gold atoms are softer than sodium and chloride ions / Gold has no charged particles, so nothing repels / The hammering melts the gold a little at a time | If you had to guess, does gold bend because its particles are softer, or because they can slide past each other?<br>**This:** Its particles are softer<br>**Or this:** They can slide past each other | **They can slide past each other.** Layers of particles slide over one another, and the whole structure stays bonded. Salt has no way to do that. |
| states-of-matter | CF CH TF TH | While the wax is melting, what does the thermometer do?<br>4 options: It keeps rising steadily, because heat keeps going in / It stays at about the same temperature until all the wax has melted / It falls, because melting takes heat away / It rises faster, because liquids heat up more easily | If you had to guess, while the wax is melting, does the thermometer reading keep rising, or stay about the same?<br>**This:** It keeps rising<br>**Or this:** It stays about the same | **It stays about the same.** The reading stays almost flat until all the wax has melted. |
| properties-ionic-compounds | CF CH TF TH | Why does no current flow through the crystals?<br>4 options: The ions are held in fixed positions and cannot move / The positive and negative charges cancel out / Salt has no charged particles in it / The crystals are not touching the probes properly | If you had to guess, is the bulb dark because the charges cancel out, or because the ions cannot move?<br>**This:** The charges cancel out<br>**Or this:** The ions cannot move | **The ions cannot move.** The ions are locked in place. They have charge, but they cannot move, so no charge can flow. |
| properties-small-molecules | CF CH TF TH | What is inside a bubble of steam?<br>4 options: Whole water molecules, spread far apart / Hydrogen and oxygen gases / Hot air that was dissolved in the water / Nothing: a steam bubble is empty | If you had to guess, is a bubble of steam full of water molecules, or of hydrogen and oxygen?<br>**This:** Water molecules<br>**Or this:** Hydrogen and oxygen | **Water molecules.** Whole H₂O molecules, far apart and moving fast. |
| polymers | CF CH TF TH | Why is poly(ethene) a solid at room temperature when ethene is a gas?<br>4 options: Its molecules are so large that the forces between them are much stronger / Joining up the molecules made the covalent bonds stronger / Poly(ethene) is a giant covalent structure / Poly(ethene) has ions in it | If you had to guess, is poly(ethene) solid because the bonds inside its molecules are stronger, or because its molecules are much bigger?<br>**This:** The bonds inside are stronger<br>**Or this:** Its molecules are much bigger | **Its molecules are much bigger.** Much bigger molecules mean much stronger forces between them, strong enough to hold the chains in place at room temperature. |
| giant-covalent-structures | CF CH TF TH | Same element, same very high melting point. What differs?<br>4 options: How the carbon atoms are bonded to each other / Graphite has impurities that make it soft / Diamond is carbon under pressure, so its atoms are smaller / Graphite is a metal and diamond is not | If you had to guess, is graphite soft because it has something else mixed in, or because its carbon atoms are joined differently?<br>**This:** It has something else mixed in<br>**Or this:** Its atoms are joined differently | **Its atoms are joined differently.** The atoms are the same; the bonding is not. |
| metals-alloys | CF CH TF TH | Why would mixing in other metal atoms make gold harder?<br>4 options: The different-sized atoms get in the way of the layers moving / The copper and gold react to make a hard compound / Copper atoms are harder than gold atoms / The extra metal fills gaps, so there is less space to bend into | If you had to guess, does mixing in other metals make gold harder by reacting with it, or by getting in the way of its layers?<br>**This:** By reacting with it<br>**Or this:** By getting in the way of its layers | **By getting in the way of its layers.** Copper atoms are a different size from gold atoms, so they distort the neat layers. |
| nanoparticles | TF TH | Why does gold behave so differently at this size?<br>4 options: A far bigger share of its atoms are at the surface / The gold has reacted with the glass to form a new compound / The atoms themselves become smaller / Heat from the furnace changes gold into another element | If you had to guess, does gold behave differently at this size because its atoms change, or because a far bigger share of them sit at the surface?<br>**This:** Its atoms change<br>**Or this:** A far bigger share sit at the surface | **A far bigger share sit at the surface.** In a 25 nm particle, a far larger fraction of the atoms sit on the surface, where they meet light and other chemicals. |
| resistors | CF CH TF TH | What must be different about the cold filament?<br>4 options: A cold filament has a lower resistance than a hot one / A cold filament has a higher resistance / The battery pushes harder at first / The glass has to warm up before light gets out | If you had to guess, does the cold filament have a lower resistance than the hot one, or a higher one?<br>**This:** Lower<br>**Or this:** Higher | **Lower.** A cold filament has a much lower resistance, so the first rush of current is large. |
| series-parallel-circuits | CF CH TF TH | The two resistors are in series. Which one has the bigger potential difference across it?<br>4 options: The 8 Ω resistor / The 4 Ω resistor / They share it equally, 6 V each / Each has the full 12 V | If you had to guess, which resistor gets the bigger share of the battery’s 12 V: the 4 Ω, or the 8 Ω?<br>**This:** The 4 Ω resistor<br>**Or this:** The 8 Ω resistor | **The 8 Ω resistor.** Both carry the same current, so the bigger resistance takes the bigger share. |

### Batch 2

| Lesson | Route(s) | Old opener | New question and two options | Correct option, and why |
|---|---|---|---|---|
| atoms-elements-compounds | CF CH TF TH | Why is salt safe to eat when sodium and chlorine are not?<br>4 options: Salt holds only a tiny amount of sodium and chlorine, too little to harm you. / The sodium and chlorine are still there, but water in the salt keeps them apart. / The elements have chemically combined into a new substance with new properties. / Cooking and processing remove the dangerous parts of each element. | If you had to guess, are the sodium and chlorine in salt just mixed together, or joined up into something new?<br>**This:** Just mixed together<br>**Or this:** Joined up into something new | **Joined up into something new.** They have chemically combined, and the new substance has properties of its own. |
| carbon-cycle | CF CH TF TH | So where did the leaf's carbon go?<br>4 options: Microorganisms respired it out as carbon dioxide / It soaked into the soil and stays there for ever / Rotting destroyed the carbon atoms completely / It turned into coal within a few months | If you had to guess, did most of the leaf’s carbon go up into the air, or down into the soil?<br>**This:** Up into the air<br>**Or this:** Down into the soil | **Up into the air.** Bacteria and fungi in the soil feed on the leaf and respire, releasing its carbon as carbon dioxide. |
| carbonates-halides-sulfates | TF TH | What went wrong?<br>4 options: The hydrochloric acid added chloride ions to every tube / Silver nitrate makes a white precipitate with any salt / All five salts really were chlorides after all / The solutions needed warming before the silver nitrate | If you had to guess, did the chloride in every tube come from the salts, or from something she added?<br>**This:** From the salts<br>**Or this:** From something she added | **From something she added.** Hydrochloric acid contains chloride ions, so every tube made white silver chloride, whatever the salt was. |
| changes-in-energy | CF CH TF TH | How much energy do the brakes now have to transfer?<br>4 options: The same amount / Twice as much / Four times as much / Eight times as much | If you had to guess, do the brakes now have to transfer twice as much energy, or more than twice as much?<br>**This:** Twice as much<br>**Or this:** More than twice as much | **More than twice as much.** It is four times as much. |
| chromosomes-mitosis | CF CH TF TH | This cell will divide into two cells, and each must end up with all 4 chromosomes. How?<br>4 options: It copies every chromosome first, then shares out the copies / It gives two of its four chromosomes to each new cell / It splits first, then each new cell builds its own four / One new cell keeps the nucleus; the other grows a new one | If you had to guess, does the cell copy its chromosomes before it divides, or share out the 4 it has?<br>**This:** Copy them first<br>**Or this:** Share out the 4 it has | **Copy them first.** Every chromosome is copied, then one copy of each goes into each new cell. |
| concentration-of-solutions | CF CH TF TH | How much sugar is in your glass?<br>4 options: 15 g / 60 g / 240 g / 15 000 g | If you had to guess, is there about 15 g of sugar in your glass, or about 240 g?<br>**This:** About 15 g<br>**Or this:** About 240 g | **About 15 g.** 250 cm³ is a quarter of a litre, so the glass holds a quarter of 60 g. |
| decomposition | CF CH TF TH | Where does the heat come from?<br>4 options: Sunlight absorbed by the heap during the day / Living things in the heap, releasing energy as they feed / The waste slowly burning without any flames / Warmth rising from the ground under the heap | If you had to guess, is the heat coming from sunshine soaked up in the day, or from living things inside the heap?<br>**This:** Sunshine soaked up in the day<br>**Or this:** Living things inside the heap | **Living things inside the heap.** Bacteria and fungi are feeding on the waste. As they feed, they respire, and respiration releases energy. |
| enzymes | CF CH TF TH | Where has the sugar come from?<br>4 options: Something in saliva breaks the starch down into sugar / The starch dissolves in saliva and becomes sugar / Chewing releases sugar hidden inside the cracker / Warmth in the mouth cooks the starch into sugar | If you had to guess, is the sugar made by the chewing, or by something in your saliva?<br>**This:** By the chewing<br>**Or this:** By something in your saliva | **By something in your saliva.** Saliva contains amylase, an enzyme that breaks starch down into sugars. |
| eukaryotes-prokaryotes | CF CH TF TH | Where is the bacterium's DNA?<br>4 options: Inside a nucleus, like the liver cell, only smaller / Loose in the cytoplasm, as one loop, with no nucleus / It has none: a bacterium is too small to need DNA / Only in its plasmids, which act as its nucleus | If you had to guess, is the bacterium’s DNA inside a nucleus too, or loose in the cell?<br>**This:** Inside a nucleus too<br>**Or this:** Loose in the cell | **Loose in the cell.** A bacterium has no nucleus. Its DNA is a single loop, loose in the cytoplasm. |
| internal-energy | CF CH TF TH | What does the thermometer do while the water keeps boiling?<br>4 options: It climbs above 100 °C, because more energy is going in / It stays at 100 °C, and the water boils away faster / It falls, because boiling takes energy out of the water / It creeps up slowly, then settles at a new higher value | If you had to guess, while the water keeps boiling, does the thermometer reading go up, or stay at 100 °C?<br>**This:** It goes up<br>**Or this:** It stays at 100 °C | **It stays at 100 °C.** The water just boils away faster. |
| lenses | TF TH | What do you see through the lens?<br>4 options: The window, upside down and smaller / The window, the right way up and bigger / The window, the right way up and smaller / Only a blur: a lens works close up | If you had to guess, do you see the window the right way up, or upside down?<br>**This:** The right way up<br>**Or this:** Upside down | **Upside down.** And smaller too. The same lens has made a different kind of image. |
| metal-hydroxides | TF TH | What is the blue solid?<br>4 options: A new insoluble compound containing the copper / Copper sulfate coming back out of the solution / The sodium hydroxide, turned blue by the solution / Copper metal, pushed out of its compound | If you had to guess, is the blue solid a new substance, or copper sulfate coming back out of the solution?<br>**This:** A new substance<br>**Or this:** Copper sulfate coming back out | **A new substance.** It is copper(II) hydroxide: copper ions from one solution met hydroxide ions from the other. |
| percentage-yield | TF TH | Where did the missing 1.8 g go?<br>4 options: It was destroyed when the copper oxide and the acid reacted together / It stayed behind in the filter paper, the glassware and the solution / It escaped as steam while the solution was being heated / Nothing is missing: 8.0 g was only an estimate of the mass | If you had to guess, was the missing 1.8 g destroyed in the reaction, or left behind along the way?<br>**This:** Destroyed in the reaction<br>**Or this:** Left behind along the way | **Left behind along the way.** Some copper sulfate stayed in the filter paper, on the glassware and in the solution. |
| relative-formula-mass | CF CH TF TH | Which molecule has the greater mass?<br>4 options: The water molecule, because it has more atoms / They are the same, because both contain oxygen / The oxygen molecule, even though it has fewer atoms / You cannot compare molecules of two different substances | If you had to guess, which molecule has the greater mass: the water, or the oxygen?<br>**This:** The water<br>**Or this:** The oxygen | **The oxygen.** Add up the masses: H₂O is 1 + 1 + 16 = 18, and O₂ is 16 + 16 = 32. |
| titrations | TF TH | The flask has just turned colourless for good. What has happened?<br>4 options: The indicator has all been used up by the acid / The acid has exactly neutralised the alkali: the end point / The flask is now strongly acidic / Some of the alkali has evaporated from the flask | If you had to guess, has the indicator been used up, or has the alkali been neutralised?<br>**This:** The indicator has been used up<br>**Or this:** The alkali has been neutralised | **The alkali has been neutralised.** The acid has exactly neutralised the alkali. This is the end point. |
| using-moles-calculations | CH TH | Which reactant runs out first?<br>4 options: Magnesium, because there is a smaller mass of it / Hydrogen chloride, because each Mg needs two HCl / Both together, because there are equal moles of each / Neither: the fizzing stops once the gas escapes | If you had to guess, which ran out: the magnesium, or the hydrogen chloride?<br>**This:** The magnesium<br>**Or this:** The hydrogen chloride | **The hydrogen chloride.** There is 0.1 mol of each, but each Mg needs two HCl. The hydrogen chloride runs out, and magnesium is left over. |

### Batch 3

| Lesson | Route(s) | Old opener | New question and two options | Correct option, and why |
|---|---|---|---|---|
| atom-economy | TF TH | Which factory turns the bigger share of its starting materials’ mass into ethanol?<br>4 options: Factory A, because each sugar molecule makes two ethanol molecules / Factory B, because ethanol is the only substance it makes / Neither: every molecule reacts in both, so both use all of it / Factory A, because sugar is a renewable raw material | If you had to guess, which factory turns the bigger share of its starting materials’ mass into ethanol: A or B?<br>**This:** Factory A<br>**Or this:** Factory B | **Factory B.** Ethanol is the only product, so every atom of the ethene and steam ends up in it. |
| conservation-of-mass | CF CH TF TH | What does the balance read once the flask has cooled?<br>4 options: More than 312.48 g, because new substances have been made / Less than 312.48 g, because some mass burned away as energy / Exactly 312.48 g, because nothing entered or left the flask / Less than 312.48 g, because the methane and oxygen were used up | If you had to guess, once the flask has cooled, does the balance read less than 312.48 g, or exactly the same?<br>**This:** Less than 312.48 g<br>**Or this:** Exactly 312.48 g | **Exactly 312.48 g.** Nothing entered or left the sealed flask, so the mass stays the same. |
| early-atmosphere | CF CH TF TH | So where is most of Earth's carbon now?<br>4 options: Locked in rocks and fossil fuels underground / Turned into the oxygen that we breathe today / Inside the plants and animals alive today / Still in the air, just spread more thinly | If you had to guess, is most of the carbon from all that carbon dioxide now locked underground, or inside living things?<br>**This:** Locked underground<br>**Or this:** Inside living things | **Locked underground.** Most of it is in sedimentary rocks such as limestone, and in fossil fuels. |
| greenhouse-gases | CF CH TF TH | How do those gases keep the surface warmer?<br>4 options: They absorb heat given off by the ground and send some back / They reflect the sunlight back down onto the ground / They block the Sun’s ultraviolet rays like a shield / They soak up sunlight on its way in, warming the air | If you had to guess, do those gases keep the surface warm by reflecting sunlight back down, or by soaking up heat given off by the ground?<br>**This:** Reflecting sunlight back down<br>**Or this:** Soaking up heat from the ground | **Soaking up heat from the ground.** The warm ground gives off heat, and the gases absorb some of it and send some back down. |
| microscopy | CF CH TF TH | What would it take to see a ribosome?<br>4 options: A lens that magnifies far more, say ×20 000 / A better stain, so the ribosomes stand out / A microscope that can separate much closer points / A living cell, so the ribosomes are moving | If you had to guess, to see a ribosome, what would you need most: a microscope that makes things even bigger, or one that shows finer detail?<br>**This:** One that makes things even bigger<br>**Or this:** One that shows finer detail | **One that shows finer detail.** Ribosomes are only about 20 nm across. The microscope has to show two points that close together as separate. |
| mixtures | CF CH TF TH | What has happened to the sugar?<br>4 options: It has reacted with the water to make a new substance / It is still sugar, spread out through the water / It has turned into water, so it cannot come back / It has been broken down by the heat and is gone | If you had to guess, is it still sugar, or has it turned into something new?<br>**This:** Still sugar<br>**Or this:** Something new | **Still sugar.** It is spread through the water, mixed but not chemically combined. |
| particle-motion-pressure | CF CH TF TH | Why must an empty aerosol can never go on a fire?<br>4 options: Heating makes the gas particles swell until they split the can open / Heating makes the gas inside push harder on the walls, until the can bursts / The leftover gas catches fire inside the can and burns through it / Heating softens the metal, so the normal push of the gas splits it | If you had to guess, when the can heats up on a fire, does it burst because the leftover gas catches fire inside it, or because the hot gas pushes harder on the walls?<br>**This:** The gas catches fire inside<br>**Or this:** The hot gas pushes harder | **The hot gas pushes harder.** The can is sealed, so the hot gas cannot escape, and its push on the walls keeps growing until the metal splits. |
| power | CF CH TF TH | Which kettle transfers more energy to the water?<br>4 options: The 3000 W kettle: a bigger number means more energy / The 1500 W kettle: it runs for longer, so works harder / The same: the 3000 W kettle just transfers it faster / You cannot tell without knowing how long each one takes | If you had to guess, does the 3000 W kettle transfer more energy to the water, or the same energy, faster?<br>**This:** More energy<br>**Or this:** The same energy, faster | **The same energy, faster.** The same water through the same temperature rise takes the same energy. The 3000 W kettle transfers it faster. |
| sound-waves-hearing | TH | Why does the trainer hear nothing?<br>4 options: It is too quiet to hear from so close by / Its pitch is too high for a human ear / Its sound cannot travel through the air to her / It is not a sound wave, so ears cannot detect it | If you had to guess, does she hear nothing because the whistle is too quiet, or because its note is too high?<br>**This:** It is too quiet<br>**Or this:** Its note is too high | **Its note is too high.** Its frequency is too high for a human ear, but not for a dog’s. |
| specific-latent-heat | CF CH TF TH | Why is the steam worse?<br>4 options: Steam releases extra energy as it condenses on the skin / Steam is hotter than boiling water, even at 100 °C / Steam particles move faster, so they hit the skin harder / Steam is a gas, so it spreads over more of the skin | If you had to guess, is the steam worse because it spreads over more skin, or because it gives the skin more energy?<br>**This:** It spreads over more skin<br>**Or this:** It gives the skin more energy | **It gives the skin more energy.** Steam condenses into water on your skin, and condensing gives out a lot of energy with no change in temperature. |
| temperature-changes-shc | CF CH TF TH | Give 1 kg of dry sand and 1 kg of seawater exactly the same energy. Which warms up more?<br>4 options: The sand: it needs less energy for each degree it warms / The seawater: liquids always warm up faster than solids / Neither: the same energy gives the same temperature rise / The sand: it is darker, so more of the energy reaches it | If you had to guess, if 1 kg of dry sand and 1 kg of seawater get exactly the same energy, which warms up more?<br>**This:** The sand<br>**Or this:** The seawater | **The sand.** Dry sand needs only about a fifth of the energy per degree that water does. |
| types-of-em-waves | CF CH TF TH | How much of the whole electromagnetic spectrum can your eyes detect?<br>4 options: A narrow band in the middle of it / Most of it: the other groups are rare and weak / All of it: the others are not really light / Exactly half: the other half is invisible | If you had to guess, can your eyes detect most of that family, or only a small part of it?<br>**This:** Most of it<br>**Or this:** Only a small part | **Only a small part.** Your eyes only respond to visible light, from red to violet. |
| waves-detection-exploration | TH | What evidence could they possibly have?<br>3 options: Rock samples brought up from the core by drilling / Records of earthquake waves from all over the world / Lava from volcanoes, which flows up from the core | If you had to guess, does their evidence come from lava, or from earthquake waves?<br>**This:** Lava<br>**Or this:** Earthquake waves | **Earthquake waves.** Earthquakes send waves right through the Earth, and instruments all over the world record them. |

## For Mide

### 1. The big question above "Start here" gives the answer away on several pages

Each lesson's header carries a big question (`ks3-bigq`) that renders *above*
"Start here". On these lessons it states the opener's answer before the pupil
guesses — it did the same with the old openers, so this is not new. It is lesson
text outside the opener, so this run left it alone (hard line). Suggested
wording, for your ruling:

| Lesson | Now | Suggested |
|---|---|---|
| enzymes | Amylase in your saliva turns starch into sugar in a minute. Heat it, or change the pH, and it slows or stops. Why, and how do you measure it the way AQA expects? | Chew a cracker long enough and it turns sweet. Heat it, or change the pH, and that slows or stops. What is doing it, and how do you measure it the way AQA expects? |
| internal-energy | Heat boiling water harder and the thermometer does not move. Where does the energy go, and why is energy not the same thing as temperature? | Heat boiling water harder. Where does the extra energy go, and why is energy not the same thing as temperature? |
| states-of-matter (pilot) | You keep heating a solid, but the thermometer stops rising. Where is the energy going, and how do you find a melting point from messy readings? | You keep heating a solid until it melts. Where does the energy go, and how do you find a melting point from messy readings? |
| lenses | The same lens can make a page look bigger and a window look small and upside down. What decides which image you get… | The same lens can show a page one way and a window another. What decides which image you get, and can you call it before the rays are drawn? |
| mixtures | Sugar stirred into water is still sugar. So how do you get each substance back out… | Stir sugar into water and it seems to vanish. How do you get each substance back out of a mixture, and how do you choose the right method? |
| conservation-of-mass | …Why does the balance underneath not move, and how does a balanced equation prove it? | Bonds break, new substances form, a flame flashes inside a sealed flask. What happens to the mass, and how does a balanced equation prove it? |
| specific-latent-heat | …Where is the extra energy, and how do you calculate it? | Steam and boiling water are both at 100 °C, yet steam does far more damage. What makes the difference, and how do you put a number on it? |
| particle-motion-pressure | …How does a gas push on its walls, and why does heating it make it push harder? | An aerosol can is thin metal holding a gas. How does a gas push on the walls of its container, and what changes when you heat it? |
| waves-detection-exploration | …How can waves reveal a structure that is hidden from view? | Doctors watch a baby before it is born, and geologists map a core that no one will ever reach. How can anyone see a structure that is hidden from view? |
| nanoparticles (pilot) | …it turns red and becomes a catalyst. Same atoms. What changed, and can you calculate it? | Drop "Same atoms." |
| covalent-bonding (pilot) | When two atoms both want electrons, neither will give any away. How do they still end up with full shells? | What holds two non-metal atoms together, and how many bonds does each one form? |

Milder leans, optional: power ("If they transfer the same energy…"),
greenhouse-gases ("How do they hold on to heat"), eukaryotes-prokaryotes ("What
does the bacterium not have"), ionic-compounds ("little NaCl molecules, or
something else"), changes-in-energy ("which does far more").

### 2. Things I was not sure about

- **using-moles-calculations** — the ladder's rung-1 reply says "In the hook,
  magnesium had the smaller mass and was left over." Still true of the new
  opener, but pupils never see the word "hook". Outside the opener, so left;
  suggested: "At the start of the lesson, magnesium had the smaller mass and was
  left over."
- **carbon-cycle** — "most of the leaf's carbon goes up into the air" matches
  AQA 4.7.2.2 and the long run; over a single year some becomes humus or is
  dragged into the soil by worms. Kept; an examiner could argue the timescale.
- **carbonates-halides-sulfates** — the scene works because the five salts
  are unnamed; with a bromide or iodide among them the precipitate would not be
  white.
- **chemical-bonds** — the wrong option "how heavy the partner's atoms are" is
  partly defensible to a Triple Higher pupil (bigger molecules boil higher),
  though it never decides the bond type, which the reply says.
- **series-parallel-circuits** — the least everyday of the 43 (a circuit, not a
  scene from life). It needs only KS3 series knowledge to guess, so kept.
- **The pilot scenes** are Design's own and denser with numbers (801 °C,
  −104 °C, 25 nm) than batch 4's. They pass the four tests as guesses; a later
  pass could make them plainer.
- **microscopy** — "about 20 nm" is the lesson's own figure; eukaryotic
  ribosomes are nearer 25–30 nm. Fine for the argument.

## Gates

Four units, one commit each, on `feat/ks4-start-here` (rebased onto KS4 batch 5):
batch 2 part 1 (8 lessons + engine), batch 2 part 2 (8), batch 3 (13), pilot (14).

- Fast: `ks4_pilot_check` 54 pages clean; `ks4_batch_check` batches 2–5 clean;
  `ks4_science_rulings_check` 101 OK, 0 MISS; `frozen_window_guard` green;
  `tools/ks4_start_here.py --check` exit 0; the rest of the fast set green.
- Slow: `ks4_chrome_drive` PASS; `ks4_parity` PASS (full pilot sweep, final
  tree); `ks4_parity --batch batch-2` 728/728 and `--batch batch-3` 616/616.
- `curriculum_tree_mirror` is red on origin/main itself (the held B2C index
  ruling); this branch does not touch `consumer/curriculum-index.json`.
- This machine hit random headless-Chrome timeouts on the night (several
  sessions running Chrome gates at once). Every one was a CDP navigation
  timeout at a different point; every re-run passed.

## Rulings applied, 9 Oct

Mide ruled on every item in "For Mide" above. Applied exactly as ruled; nothing
else in any lesson changed, batches 4–6 and the opener blocks are untouched.

**The 11 big questions — the suggested wording, word for word.** Batch 2–3 lessons
are edited in their authored sources (`ks4_lessons/authored/batch-N/*.dc.html`);
the three pilot lessons are Design's files, so they take the new ruling **R19**
(`ks4_rulings.R19_BIGQ`, applied after R18), and `ks4_parity` proves each pilot
header carries the ruled text, from the same table.

| Lesson | Big question now |
|---|---|
| enzymes | Chew a cracker long enough and it turns sweet. Heat it, or change the pH, and that slows or stops. What is doing it, and how do you measure it the way AQA expects? |
| internal-energy | Heat boiling water harder. Where does the extra energy go, and why is energy not the same thing as temperature? |
| states-of-matter (pilot, R19) | You keep heating a solid until it melts. Where does the energy go, and how do you find a melting point from messy readings? |
| lenses | The same lens can show a page one way and a window another. What decides which image you get, and can you call it before the rays are drawn? |
| mixtures | Stir sugar into water and it seems to vanish. How do you get each substance back out of a mixture, and how do you choose the right method? |
| conservation-of-mass | Bonds break, new substances form, a flame flashes inside a sealed flask. What happens to the mass, and how does a balanced equation prove it? |
| specific-latent-heat | Steam and boiling water are both at 100 °C, yet steam does far more damage. What makes the difference, and how do you put a number on it? |
| particle-motion-pressure | An aerosol can is thin metal holding a gas. How does a gas push on the walls of its container, and what changes when you heat it? |
| waves-detection-exploration | Doctors watch a baby before it is born, and geologists map a core that no one will ever reach. How can anyone see a structure that is hidden from view? |
| nanoparticles (pilot, R19) | "Same atoms." dropped: …it turns red and becomes a catalyst. What changed, and can you calculate it? |
| covalent-bonding (pilot, R19) | What holds two non-metal atoms together, and how many bonds does each one form? |

**using-moles-calculations** — the ladder's rung-1 reply now reads "At the start of
the lesson, magnesium had the smaller mass and was left over."

**Left as they are, as ruled:** the milder leans (power, greenhouse-gases,
eukaryotes-prokaryotes, ionic-compounds, changes-in-energy); carbon-cycle,
carbonates-halides-sulfates, chemical-bonds, series-parallel-circuits and
microscopy; the pilot's number-heavy scenes.

**Noticed, not changed (not in the ruling):** *power*'s legal footnote also says
"In the hook, each kettle is treated as transferring all of its energy to the
water" — the same word "hook" pupils never see.

**Re-freeze.** The twelve changed lessons were examiner-frozen, so their freeze
hashes were re-recorded (`build_ks4.py --freeze`, `--batch batch-2 --freeze`,
`--batch batch-3 --freeze`) after the change was read against each lesson; the
wording itself is Mide's ruling. `ks4_science_rulings_check` and
`frozen_window_guard` stay green.
