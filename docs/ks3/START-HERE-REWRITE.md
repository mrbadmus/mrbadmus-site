# KS3 "Start here" rewrite — every live lesson onto the two-option guess

**Run:** 9–10 Oct 2026, unattended. Branch `feat/ks3-start-here`, worktree
`mrbadmus-worktrees/ks3-start-here`, cut from `origin/main` at `b9a9f5488`.
**Rule:** Mide's rule of 2 Oct 2026, written for KS4 and applied here unchanged:
"Start here" is "If you had to guess, …?" with exactly two options, in simple
everyday wording any Year 7 pupil can answer, not patronising for a strong Year 9,
the answer not given away in the title, the scene or the big question above it, and
a friendly reply to each option that leads into the teaching.

## How KS3 openers work (step 1, from the code)

| What | Where |
|---|---|
| The opener's data | each lesson's `phenomenon` dict in `ks3_data/<unit>/lesson_NN_*.py`: `title`, `prompt` (the scene), `commit` (the question), `options`, `reveal`, plus `art`/`tiles`/`figures` for the media column and, on 70 lessons, an `answer` index. The big question is the lesson's `big_question`, shown in the header above the hook and on the year index cards. |
| How it renders | `r_hook()` in `build_ks3.py` (the `"hook"` block renderer): `#s-hook`, ink-dark, `data-activity="hook"`. Options come from `r_activity_options()` (`ks3_art/kit.py`) as lettered `.ks3-option` buttons, and one shared `.ks3-reveal` opens on any pick (`wirePredictions` in `shared/ks3.js`). No unit module overrides the hook. |
| Which build | `build_ks3.py` (step 2 of `build_all.py`), mirrored to `ks3/` and `mrbadmus_site/ks3/`. |
| Which gates watch it | `verify_ks3` (a hook exists, `#s-hook` resolves, the rail), `ks3_parity` (style rows on the hook, and the c1-06 keyed-commit rows), `answer_lengths` (hook options when an `answer` index exists), `ks3_rail_manifest`. |
| Frozen content? | **No.** `frozen_window_guard` reads only the KS4 question bank's frozen window; no KS3 opener text is frozen. It stayed green. |
| Lessons | **185** live (authored) KS3 lessons: 184 opened on four options, 1 (`life-processes`) on three. **None** had a two-option guess, so none was left alone. |

### The route taken

KS3 had no two-option block, so per the ruling the KS4 `Ks4Guess` behaviour is
ported into KS3's own system. It needed **no new component at all**: KS3 already
has `keyed-commit` (c1-03 `#s-bubble`, c1-06 `#s-verdict`), a set of `.ks3-option`
buttons whose panel shows the reply for the option pressed, then closing paragraphs
everyone reads. `shared/ks3.js`'s `wireKeyedCommit` drives it and `shared/ks3.css`
already paints it for ink-dark blocks. So the guess is the hook with that markup:

- `#s-hook` gains `data-keyedblock`; its commit line is the "If you had to guess,
  …?" question; two lettered `.ks3-option` buttons (KS3's house look, not KS4's
  "This / Or this"); one `.ks3-keyed-reply` per option, opening with **Good
  guess.** or **Fair guess.** as `Ks4Guess` does; then the bridge as a
  `.ks3-keyed-static` paragraph.
- Under KS3's R3 the options are never marked and stay re-choosable (`Ks4Guess`
  disables after one pick). A pupil can press the other option and read its reply.
- **No shared code changed.** `shared/ks3.js`, `shared/ks3.css` and every other
  shared asset are byte-identical to main, so no other page's cache-bust stamp
  moved: KS4, the class pages, the student work list and B2C are untouched, and
  every KS3 page whose opener did not change is byte-identical to main.

| File | Change |
|---|---|
| `ks3_data/start_here.py` | **New.** Every opener as data: question, two (option, reply) pairs, the correct index, the bridge, and a new title / scene / big question only where the old one gave the answer away. `validate()` refuses a malformed entry. |
| `ks3_data/__init__.py` | `build_units()` merges each entry over its lesson's `phenomenon` (and `big_question`), so the generator and every gate see the same opener; refuses an entry for a lesson that is not authored. The lesson modules themselves, Design's transcriptions, are untouched. |
| `build_ks3.py` | `r_hook()` renders a guess with the keyed-commit markup (`_hook_guess`). A hook with no entry renders exactly as before. |
| `ks3_parity.py` | The c1-06 keyed-commit rows and their drive are scoped to `#s-verdict`. With the hook keyed too, a bare `[data-keyed]` would have silently started measuring the hook instead, which sits above it. A tightening, not a weakening. |

### How each opener was written and checked

Sonnet writers drafted each batch from the whole lesson file (its explainer, key
facts, activities, ladder and misconceptions), against the KS4 batch 4–6 openers
as the model. A fresh Opus reviewer per two batches then read every lesson in full
and checked each opener against the four tests, the science, the title / scene /
big question for give-aways, any later text on the page that refers back to the
hook (rail labels, "at the top of this lesson"), and any later prediction it might
answer in advance, fixing what failed. A mechanical lint refused any entry whose
correct option was visibly longer, any em dash in new text, and any reply carrying
its own "Good guess". Each batch was then built, every changed page was driven in
headless Chrome (two options, the right reply per pick, the bridge, the rail stop
ticks, no console errors), every other KS3 page was compared with main byte for
byte, and the fast gates were run before the commit.

## The openers (60 of 185 lessons)

| Year | Lesson | Old opener | New question and two options | Correct option, and why | Pushed / waiting |
|---|---|---|---|---|---|
| 7 | life-processes (B1) | Is a candle flame alive?<br>3 options: Yes — it does everything a living thing does / No — but I could not say what is missing / No — and I know what is missing | If you had to guess, is a candle flame alive?<br>**A:** Yes, it is alive<br>**B:** No, it is not alive<br>*also changed: big question* | **No, it is not alive.** A flame moves, grows, feeds and makes waste, and it is still not alive. What it is missing is cells. | batch 1: committed, not pushed |
| 7 | using-a-microscope (B1) | Which objective would you turn in first to find the cells?<br>4 options: The ×4 — the widest view / The ×10 / The ×40 — the most detail / It makes no difference which | If you had to guess, which lens should you start with to find the cells?<br>**A:** The weakest lens<br>**B:** The strongest lens<br>*also changed: big question* | **The weakest lens.** That is the right start. Find the cells on the weakest lens first, then move up to a stronger one. | batch 1: committed, not pushed |
| 7 | animal-and-plant-cells (B1) | Which one is in an animal cell but not in a plant cell?<br>4 options: The nucleus / The mitochondria / The cytoplasm / None of them | If you had to guess, does the cheek cell have any of these seven parts that the oak leaf cell lacks?<br>**A:** Yes, at least one<br>**B:** No, not one<br>*also changed: title, scene, big question* | **No, not one.** Every part in your cheek cell is in the leaf cell too. The leaf cell just has some extra parts of its own. | batch 1: committed, not pushed |
| 7 | specialised-cells (B1) | Something must be worth all that. What does losing the nucleus buy the cell?<br>4 options: It can fit through narrower vessels / Room — space for the cargo it carries / It saves energy by not using the nucleus / Nothing. It is a mistake in the process | If you had to guess, what does the red blood cell gain by throwing its nucleus away?<br>**A:** More room inside<br>**B:** A faster trip | **More room inside.** Room is the gain. The space the nucleus leaves is packed with haemoglobin, the red stuff that carries oxygen. | batch 1: committed, not pushed |
| 7 | levels-of-organisation (B1) | Nothing is missing from the dish. So what has the stomach got?<br>4 options: More cells / The cells arranged into layers that work together / Different kinds of cell / Nothing — the dish just needs more time | If you had to guess, what lets a real stomach do what the dish of cells cannot?<br>**A:** Many more cells<br>**B:** Cells arranged in layers<br>*also changed: title, scene* | **Cells arranged in layers.** Layers, each with its own job: muscle to churn the food, a lining to make acid and enzymes. They only work as a team. | batch 1: committed, not pushed |
| 7 | unicellular-organisms (B1) | One is an organism. One is part of one. What settles it?<br>4 options: It can move on its own / It has more structures inside it / It carries out all seven life processes by itself / It lives in water instead of inside a body | If you had to guess, what makes the Paramecium a whole living thing and not just a piece of one?<br>**A:** It does every job itself<br>**B:** It can swim about | **It does every job itself.** A Paramecium has nobody to feed it or clean up after it. It has to feed, grow, move and reproduce all on its own. | batch 1: committed, not pushed |
| 7 | what-the-skeleton-does (B2) | What actually decides how serious a broken bone is?<br>4 options: How big the bone is / How much it hurts / What job that bone was doing, and what depended on it / How long it takes to heal | If you had to guess, what matters most for how bad a broken bone is?<br>**A:** What relies on the bone<br>**B:** How big the bone is<br>*also changed: big question* | **What relies on the bone.** A finger bone has little relying on it. A femur holds up your whole body, so far more fails when it breaks. | batch 1: committed, not pushed |
| 7 | joints (B2) | Why is the shoulder the one that gives way?<br>4 options: Shoulder muscles are weaker than elbow muscles / It moves in far more directions, so far more directions can push it out / People use their shoulders more / The bones there are softer | If you had to guess, why does the shoulder come out of place so much more than the elbow?<br>**A:** It moves in more directions<br>**B:** Its muscles are weaker<br>*also changed: title, big question* | **It moves in more directions.** Every direction a joint can move in is a direction it cannot hold against. The shoulder swings almost anywhere, so almost anything can push it out. | batch 1: committed, not pushed |
| 7 | antagonistic-muscle-pairs (B2) | You push a door open, straightening your arm. What straightens it?<br>4 options: The biceps pushes the forearm out / The biceps gets longer on its own / A different muscle, behind the arm, pulls / Nothing does — the arm falls straight | If you had to guess, when you push a door open, where is the muscle that straightens your arm?<br>**A:** On the front of your upper arm<br>**B:** On the back of your upper arm | **On the back of your upper arm.** A muscle on the back of the upper arm, the triceps, pulls on the bone behind your elbow and swings the forearm straight. | batch 1: committed, not pushed |
| 7 | biomechanics-forces-in-the-body (B2) | Something about that arrangement is doing the damage. What?<br>4 options: Muscles are simply weak for their size / The two distances from the elbow are very different / The bag is heavier than it looks / The forearm bones get in the way of the pull | If you had to guess, why does your biceps have to pull so much harder than the bag weighs?<br>**A:** Some of its pull is wasted<br>**B:** It is attached near the elbow<br>*also changed: title, scene* | **It is attached near the elbow.** The bag sits far out along your forearm, but the muscle pulls close to the elbow. A pull that close in has to be much bigger to hold the bag up. | batch 1: committed, not pushed |
| 7 | a-balanced-diet (B3) | One orange. What is it doing?<br>4 options: Supplying energy the rest of the plate is missing / Supplying about 50 mg of one substance the body cannot make / Making the meal easier to digest / Adding water, which the rest of the plate lacks | If you had to guess, what in the orange saves the person on Plate B?<br>**A:** A tiny vital substance<br>**B:** A bit more energy<br>*also changed: scene, big question* | **A tiny vital substance.** Just 50 mg of vitamin C, a tiny fraction of the meal. Without it the body cannot build the protein that holds your body together. | batch 2: committed, not pushed |
| 7 | food-tests (B3) | What can you conclude from tube 2 on its own?<br>4 options: That milk contains no sugar / That milk contains less sugar than tube 1 suggested / Nothing about the milk at all / That the Benedict’s solution had gone off | If you had to guess, what does tube 2 on its own tell you about the milk?<br>**A:** It has no sugar in it<br>**B:** Nothing either way<br>*also changed: scene* | **Nothing either way.** On its own, a blue tube only says the test did not find sugar this time. That is a fact about the test, not about the milk. | batch 2: committed, not pushed |
| 7 | energy-in-food-and-what-you-need (B3) | Same food in. Why the different outcome?<br>4 options: The cyclist digests food more efficiently / They transfer very different amounts of energy in a day / The older person’s body stores food instead of using it / 11 000 kJ is the wrong amount for both of them | If you had to guess, what explains the different outcome?<br>**A:** How much energy each body needs<br>**B:** How well each body digests food<br>*also changed: scene, big question* | **How much energy each body needs.** Bodies need very different amounts of energy in a day. The same food is more than enough for one and not enough for the other. | batch 2: committed, not pushed |
| 7 | when-diet-goes-wrong (B3) | How can both be true at once?<br>4 options: The intake figure must have been measured wrongly / Malnutrition is about balance, not quantity / Their body is failing to digest any of the food / 13 000 kJ is not actually very much | If you had to guess, could this patient be malnourished?<br>**A:** Yes, they could be<br>**B:** No, not on that much<br>*also changed: title, scene, big question* | **Yes, they could be.** Malnourished means badly nourished, not underfed. A big diet can still be missing something the body needs, such as iron or a vitamin. | batch 2: committed, not pushed |
| 7 | the-digestive-system (B3) | Could that liquid pass straight into your blood?<br>4 options: Yes — it is a liquid with no lumps in it / Yes, but only the parts that dissolved / No — the molecules in it are still far too large / No — it has not been mixed with stomach acid | If you had to guess, could that smooth liquid go straight into your blood?<br>**A:** Yes, it is smooth enough<br>**B:** No, the bits are too big | **No, the bits are too big.** Smooth is not the same as small enough. The starch in the liquid is still in long chains, far too big to cross into your blood. | batch 2: committed, not pushed |
| 7 | enzymes-in-digestion (B3) | So what is an enzyme doing?<br>4 options: Being broken down along with the starch / Speeding the reaction up without being changed by it / Turning itself into glucose / Supplying the energy the reaction needs | If you had to guess, is the amylase still there once the starch has gone?<br>**A:** Yes, all of it<br>**B:** No, it gets used up<br>*also changed: title, scene, big question* | **Yes, all of it.** All of it is still there. An enzyme is a catalyst: it speeds a reaction up without being used up, so a teaspoon goes a very long way. | batch 2: committed, not pushed |
| 7 | absorption-and-the-small-intestine (B3) | Same length, same width, sixty times the surface. How?<br>4 options: The intestine is coiled up, which adds surface / Its wall is folded at three different scales / It stretches when food is inside it / Its wall is much thicker than a hose’s | If you had to guess, how does the intestine get sixty times the surface of a hose?<br>**A:** It is coiled up<br>**B:** Its wall is folded<br>*also changed: big question* | **Its wall is folded.** Folded, and then folded again. Folds with bumps on them, and tinier bumps on those, give far more surface than a plain tube of the same size. | batch 2: committed, not pushed |
| 7 | bacteria-in-the-gut (B3) | Removing every bacterium made the mouse worse. Why?<br>4 options: The sterile food was less nutritious / Its gut bacteria had been doing jobs it cannot do itself / Living in a bubble is stressful / It could not digest anything at all without bacteria | If you had to guess, does a mouse with no bacteria need more food than a normal mouse, or less?<br>**A:** More food<br>**B:** Less food<br>*also changed: scene, big question* | **More food.** About 30% more. Gut bacteria release energy from parts of the food the mouse cannot digest itself, so without them that energy is lost. | batch 2: committed, not pushed |
| 7 | particle-model (C1) | Three millilitres of liquid are missing. Commit to a reason.<br>4 options: Some of it evaporated while you were pouring / The two liquids reacted and made something smaller / Particles of one liquid settled into gaps between particles of the other / The measuring cylinder is not accurate enough | If you had to guess, where did the missing 3 ml go?<br>**A:** It evaporated away<br>**B:** It squeezed into gaps<br>*also changed: big question* | **It squeezed into gaps.** Nothing is lost. Every drop is still in the cylinder. Liquids are not solid all the way through, so the small bits of one settle into gaps between the big bits of the other. | batch 2: committed, not pushed |
| 7 | solids-liquids-and-gases (C1) | So what got bigger?<br>4 options: Each iron particle expanded in the heat / The gaps between the particles got bigger / The steel absorbed moisture from the summer air / Extra particles were added by the heat | If you had to guess, when steel expands in the heat, what gets bigger?<br>**A:** Each particle swells up<br>**B:** The gaps between them<br>*also changed: big question* | **The gaps between them.** Heat makes the particles jiggle harder, so each needs more room and the gaps grow. The particles themselves stay exactly the same size. | batch 2: committed, not pushed |
| 7 | changes-of-state (C1) | What does the balance read the second time?<br>4 options: Less than 50 g — some of the ice is gone / Exactly 50 g / More than 50 g — water is denser than ice / It depends how long you leave it | If you had to guess, once the ice has melted, will the balance read less than 50 g, or exactly 50 g?<br>**A:** A bit less<br>**B:** Exactly 50 g<br>*also changed: title, scene* | **Exactly 50 g.** Melting moves the particles around but never removes any, and nothing can leave a sealed bag. The balance has nothing to report. | batch 3: committed, not pushed |
| 7 | gas-pressure (C1) | Commit to what bursts it.<br>4 options: Leftover propellant liquid that boils / The gas already inside, hitting the walls harder as it heats / The metal expanding until it tears / Nothing — an empty can is safe | If you had to guess, is that can really empty inside?<br>**A:** No, there is gas inside<br>**B:** Yes, it is empty<br>*also changed: title, big question* | **No, there is gas inside.** The can is full of gas. There is no such thing as a sealed can with nothing in it, even when it has stopped spraying. | batch 3: committed, not pushed |
| 7 | diffusion (C1) | Commit to what moved it.<br>4 options: A draught too small to see / The perfume particles moved there themselves, bouncing off air particles / Warm air rising carried it across / The particles were attracted towards the empty part of the room | If you had to guess, with no draught to carry it, will the smell of the perfume ever reach you?<br>**A:** Yes, in the end<br>**B:** No, it needs a draught<br>*also changed: title, scene, big question* | **Yes, in the end.** The perfume particles spread out by themselves, bouncing off the air particles on the way. It is slow, but no draught is needed. | batch 3: committed, not pushed |
| 7 | testing-the-model (C1) | The model has just made a wrong prediction. Commit to what that means.<br>4 options: The model is wrong and should be abandoned / Water is a special case and can be ignored / The model has found a limit, and the limit is worth knowing / Someone measured it wrong | If you had to guess, will the lump float on the melted wax, or sink in it?<br>**A:** It floats<br>**B:** It sinks<br>*also changed: title, scene* | **It sinks.** Almost every solid sinks in its own liquid. Its particles are packed more tightly, so a lump of it is heavier than the same amount of liquid. | batch 3: committed, not pushed |
| 7 | the-atom-daltons-model (C2) | What would explain a failure that complete?<br>4 options: They were not skilled enough, and modern equipment would manage it / Lead and gold are made of different kinds of particle, and no reaction changes one kind into another / Gold is heavier, so more material would be needed / They were kept secret whenever it worked | If you had to guess, could modern furnaces, acids and mixing finally turn lead into gold?<br>**A:** Yes, with modern kit<br>**B:** No, however good the kit<br>*also changed: title, big question* | **No, however good the kit.** Lead atoms and gold atoms are different kinds. Heating, burning and mixing only rearrange atoms, and no reaction changes one kind into the other. | batch 3: committed, not pushed |
| 7 | elements (C2) | If you had a sample of something, how would you find out whether it was on that list?<br>4 options: See whether it looks like a metal / Test whether it conducts electricity / Try to break it down into anything simpler / Weigh it and measure its melting point | If you had to guess, how would you tell whether a sample is on that list: try to break it down, or look at it closely?<br>**A:** Try to break it down<br>**B:** Look at it closely | **Try to break it down.** If anything simpler comes out, it was never on the list. An element is made of one kind of atom, so there is nothing simpler inside it. | batch 3: committed, not pushed |
| 7 | compounds (C2) | Where has the iron gone?<br>4 options: It melted and ran to the bottom of the dish / It joined with the sulfur to make a different substance / The sulfur has coated each piece of iron / It burnt away and left the sulfur behind | If you had to guess, has the iron burnt away, or joined up with the sulfur?<br>**A:** It burnt away<br>**B:** It joined the sulfur<br>*also changed: big question* | **It joined the sulfur.** Every bit of the iron is still in the dish, now joined to the sulfur in a new substance. | batch 3: committed, not pushed |
| 7 | chemical-symbols (C2) | Why do chemists write in symbols instead of names?<br>4 options: To save time writing / So that one written symbol means one element, in every language / To make chemistry look more scientific / Because some element names are very long | If you had to guess, when the book gives the formula for water, will it be H2O, or written in Japanese?<br>**A:** H2O, as here<br>**B:** Written in Japanese<br>*also changed: title, scene, big question* | **H2O, as here.** The words around it are all Japanese, but the formula is H2O, exactly as you would write it. | batch 3: committed, not pushed |
| 7 | formulae (C2) | What is actually different about them?<br>4 options: One is more concentrated than the other / Each particle of one has an extra oxygen atom / One has something dissolved in it / They are the same substance at different temperatures | If you had to guess, would bubbling oxygen gas through water turn it into the dangerous liquid?<br>**A:** Yes, it would<br>**B:** No, it would not | **No, it would not.** The oxygen just mixes in with the water. To make the other liquid, an extra oxygen atom has to be joined into every single particle. | batch 3: committed, not pushed |
| 7 | conservation-of-mass (C2) | So where did sixty grams of wax go?<br>4 options: It was destroyed / It turned into heat and light / It left as invisible gases / It soaked into the plate | If you had to guess, where did the wax go?<br>**A:** Into gas in the air<br>**B:** Into heat and light<br>*also changed: big question* | **Into gas in the air.** The wax joined with oxygen from the air and drifted off as invisible gases. It is still somewhere in the room. | batch 3: committed, not pushed |
| 7 | pure-or-mixture (C3) | Which one is pure, and what is the word doing in the other?<br>4 options: The juice — it says 100% pure on the carton / The water — it is one substance and the juice is many / Both — neither has anything added to it / Neither — nothing is ever completely pure | If you had to guess, which of these would a chemist call pure?<br>**A:** The orange juice<br>**B:** The distilled water<br>*also changed: title, scene, big question* | **The distilled water.** Distilled water is one substance and nothing else. Juice is water, sugars, acids, pulp and more all together. | batch 4: committed, not pushed |
| 7 | dissolving-and-solutions (C3) | What does the balance read now?<br>4 options: 100 g — the sugar has gone / Somewhere between 100 g and 110 g / 110 g — everything that went in is still there / More than 110 g — the sugar takes up water | If you had to guess, will the balance still read 110 g now, or less?<br>**A:** Still 110 g<br>**B:** Less than 110 g<br>*also changed: big question* | **Still 110 g.** The sugar has not gone. It has broken up into particles too small to see and spread through the water, and the balance counts every gram. | batch 4: committed, not pushed |
| 7 | filtration (C3) | What is left in the two filter papers afterwards?<br>4 options: Sand in one paper, salt in the other / Sand in one paper, nothing in the other / Nothing in either — both pass through / Sand in one, and the other paper turns salty but stays empty | If you had to guess, will the filter papers catch sand and salt, or just the sand?<br>**A:** Just the sand<br>**B:** Sand and salt<br>*also changed: big question* | **Just the sand.** The sand grains are far too big to fit through the paper. The dissolved salt goes straight through with the water. | batch 4: committed, not pushed |
| 7 | evaporation-and-crystallisation (C3) | Which dish has the bigger crystals in it, and why would anyone care?<br>4 options: The boiled dish — heat makes crystals grow / The windowsill dish — slow growth gives bigger crystals / Both the same — same salt, same mass / Neither — you only get a powder either way | If you had to guess, which dish has the bigger crystals in it?<br>**A:** The boiled dish<br>**B:** The windowsill dish<br>*also changed: big question* | **The windowsill dish.** Slow evaporation lets the salt particles join up in an orderly way. A few crystals start, and they grow big. | batch 4: committed, not pushed |
| 7 | distillation (C3) | What do you do with the pan, the plastic and the cup?<br>4 options: Filter the sea water through the plastic sheet / Boil it and let it all go into the air / Boil it and catch what comes off on the cold plastic / Leave it in the sun until the salt sinks | If you had to guess, how do you get fresh water out of the sea water?<br>**A:** Boil it, catch the steam<br>**B:** Wait for the salt to sink<br>*also changed: big question* | **Boil it, catch the steam.** Only the water boils off. The salt stays behind, and the steam turns back into fresh water when it meets a cold surface. | batch 4: committed, not pushed |
| 7 | chromatography (C3) | Draw a dot of each ink near the bottom of a strip of paper and let water creep up through it. What happens?<br>4 options: The dots wash away and the paper stays blank / Each dot climbs and splits into separate coloured spots / The dots stay where they are and go paler / All four inks give exactly the same pattern | If you had to guess, as the water creeps up, will the black dot stay black, or split into other colours?<br>**A:** It stays black<br>**B:** It splits into colours<br>*also changed: title, scene, big question* | **It splits into colours.** The black is really a mix of dyes. The water carries each dye up the paper a different distance, so they separate. | batch 4: committed, not pushed |
| 7 | proving-something-is-pure (C3) | You can make one measurement on each. Which measurement would settle it?<br>4 options: Weigh a spoonful of each / Check whether each one dissolves in water / Measure the temperature at which each one melts / Look at all three under a microscope | If you had to guess, will the powder with something mixed in start melting at a lower temperature, or a higher one?<br>**A:** A lower temperature<br>**B:** A higher temperature<br>*also changed: title, scene* | **A lower temperature.** Something mixed in breaks up the neat pattern of the particles, so it starts to give way sooner. Salt on an icy road works in the same way. | batch 4: committed, not pushed |
| 7 | speed (P3) | So what would you have to know to say which is faster?<br>4 options: Which of them crossed your view the fastest / How far each one travelled, and how long it took / Which of the two of them is the bigger object / How far away each of them is from your eye | If you had to guess, which one is really going faster?<br>**A:** The fly<br>**B:** The plane<br>*also changed: title, scene, big question* | **The plane.** Because it is so far away, it looks slow. It really covers about 250 metres every second. | batch 4: committed, not pushed |
| 7 | distance-time-graphs (P3) | So what is the height of the line telling you?<br>4 options: How high above the ground the walker is / How far the walker is from the start / How fast the walker is going / How long the walker has been walking | If you had to guess, while the walker waits at the door, does the line go flat, or drop to the bottom?<br>**A:** It goes flat<br>**B:** It drops to the bottom<br>*also changed: scene, big question* | **It goes flat.** The walker stays 6 m from the start the whole time they wait, so the line stays at that height. | batch 4: committed, not pushed |
| 7 | relative-motion (P3) | Commit. How fast is that train going?<br>4 options: 100 km/h — that is what the driver was told / 0 km/h — it is not moving, you can see that / 200 km/h / The question cannot be answered as it stands | If you had to guess, with the blinds pulled down, could you tell that your own train was moving at all?<br>**A:** Yes, you would feel it<br>**B:** No, you could not tell<br>*also changed: scene* | **No, you could not tell.** At a steady speed on a smooth track, everything inside the train behaves just as it would standing still. Only looking out tells you. | batch 4: committed, not pushed |
| 7 | what-a-force-is (P4) | So what is a force?<br>4 options: Something an object has inside it, which gets used up / A push or a pull, always between two objects / How fast something is going, in metres per second / The energy stored in something that is moving | If you had to guess, as you roll away, are you still carrying the wall's push with you?<br>**A:** Yes, until it runs out<br>**B:** No, it has already stopped | **No, it has already stopped.** The wall's push lasts only while your hands are on it. You keep rolling because you are already moving, not because you are carrying a push. | batch 5: committed, not pushed |
| 7 | drawing-and-adding-forces (P4) | A sledge is pulled right with 40 N and left with 25 N. What single force would have exactly the same effect?<br>4 options: 65 N to the right / 15 N to the right / 15 N to the left / 40 N to the right | If you had to guess, how hard is the sledge pulled overall?<br>**A:** 15 N to the right<br>**B:** 40 N to the right<br>*also changed: title, scene* | **15 N to the right.** The 25 N pull cancels 25 N of the 40 N pull. The 15 N left over is the only pull the sledge responds to. | batch 5: committed, not pushed |
| 7 | balanced-and-unbalanced (P4) | So what is different about the forces on the book on the table?<br>4 options: The falling book has more weight than the same book resting on a table / A second force pushes up on the resting book, exactly matching its weight / The resting book has no forces acting on it at all while it stays still / Gravity switches off as soon as something rests on a solid surface | If you had to guess, is anything pushing up on the book that rests on the table?<br>**A:** Yes, something is<br>**B:** No, nothing is<br>*also changed: title, scene, big question* | **Yes, something is.** The table is squashed a tiny bit, too little to see, and it pushes up on the book. It pushes exactly as hard as gravity pulls the book down. | batch 5: committed, not pushed |
| 7 | what-forces-do-to-motion (P4) | So why does it keep moving?<br>4 options: Force from the push is still stored inside it, and it is only slowly running out / Nothing needs to push it — with almost nothing left over, almost nothing changes / The ice underneath is pushing the stone forwards the whole way down / It keeps going because it is heavy, and heavy things carry themselves along | If you had to guess, does the stone need something pushing it forwards to keep going?<br>**A:** No, it keeps going alone<br>**B:** Yes, something must push it<br>*also changed: title, scene, big question* | **No, it keeps going alone.** Moving does not need a push. Smooth ice holds the stone back so little that it carries on at nearly the same speed. | batch 5: committed, not pushed |
| 7 | friction (P4) | Why is starting it harder than keeping it going?<br>4 options: The crate gets lighter once it is moving, so less push is needed to keep it going / Friction is largest just before sliding starts, and drops once the surfaces are sliding / Your push gets stronger as you lean into it, so the crate moves once you push hard enough / The floor stops pushing back once the crate is moving, so nothing resists it | If you had to guess, once the crate is sliding, is keeping it going easier than starting it, or just as hard?<br>**A:** A little easier<br>**B:** Just as hard<br>*also changed: scene, big question* | **A little easier.** The floor grips the crate hardest just before it moves. Once it is sliding, the two surfaces never get the chance to settle into each other, so the grip drops. | batch 5: committed, not pushed |
| 7 | air-and-water-resistance (P4) | Why does the falling stop getting faster?<br>4 options: Gravity gets weaker as you fall, so the pull on you drops until you stop speeding up / There is a fastest speed anything can fall at, and every object reaches the same one / Air resistance grows with speed until it matches the weight, leaving 0 N over / The air is holding the skydiver up completely, so gravity has stopped acting | If you had to guess, what happens to the skydiver's speed over the minute?<br>**A:** Stops getting faster<br>**B:** Keeps getting faster<br>*also changed: title, scene, big question* | **Stops getting faster.** After about ten seconds the speed levels off at around 55 metres per second, even with nothing underneath them. The air pushes back harder the faster they fall. | batch 5: committed, not pushed |
| 7 | moments (P4) | Why is the same force so much less use near the hinge?<br>4 options: You push harder at the handle without noticing, because leaning is easier there / The turning effect depends on the distance from the pivot as well as the force / The door is heavier near the hinge, so there is more of it to shift there / The hinge takes the force away, so a push near it never reaches the door | If you had to guess, does the door swing open just as easily this time?<br>**A:** Yes, just as easily<br>**B:** No, it hardly moves<br>*also changed: scene, big question* | **No, it hardly moves.** The push is just as hard, but this close to the hinge it barely turns the door. Where you push matters as well as how hard. | batch 5: committed, not pushed |
| 7 | springs-and-hookes-law (P4) | What will the extension be at 10 N?<br>4 options: 200 mm — every newton adds another 20 mm, all the way / More than 200 mm — the pattern stops holding at some load / Less than 200 mm — a spring gets harder to stretch as it goes / Nothing — it will have snapped long before 10 N | If you had to guess, will this spring keep adding 20 mm for every extra newton, all the way to 10 N?<br>**A:** Yes, all the way<br>**B:** No, the pattern stops<br>*also changed: title, scene, big question* | **No, the pattern stops.** For the first few newtons the pattern holds exactly. But every spring has a load where it stops, and a small lab spring reaches it before 10 N. | batch 5: committed, not pushed |
| 7 | non-contact-forces (P4) | What is pulling the hair?<br>4 options: The air in between is pushing the hair upwards / The balloon touches the hair too quickly for you to see / Some forces act across a gap, with nothing in between / Static is a stickiness rather than a force | If you had to guess, does the balloon have to touch the hair to make it move?<br>**A:** Yes, it has to touch<br>**B:** No, it works across a gap<br>*also changed: title, scene, big question* | **No, it works across a gap.** The hair lifts while there is still a clear centimetre of air in between. The balloon pulls on it across the gap, with nothing touching. | batch 5: committed, not pushed |
| 7 | density (P11) | Which one is heavier?<br>4 options: The iron, because a metal always weighs more than wood / The oak, because there is so much more of it on the pan / They weigh the same, because the balance is level / It depends on the shape of each of the two blocks | If you had to guess, which is heavier?<br>**A:** The lump of iron<br>**B:** Neither: they balance<br>*also changed: title, scene, big question* | **Neither: they balance.** The beam stays level, so they weigh the same. It takes about twelve times as much oak to match one lump of iron. | batch 5: committed, not pushed |
| 7 | brownian-motion (P11) | What is moving them?<br>4 options: Tiny air currents are blowing them about / Something alive inside them is swimming / Invisible particles are hitting them from every side / The microscope lamp is heating one side of each speck | If you had to guess, what is moving the specks about?<br>**A:** Unseen bits of air hitting them<br>**B:** Draughts of air blowing them<br>*also changed: big question* | **Unseen bits of air hitting them.** The air is made of particles far too small to see, and billions of them strike each speck every second. The strikes almost cancel, and the small leftover shoves the speck about. | batch 6: committed, not pushed |
| 7 | temperature-and-internal-energy (P11) | Which one holds more energy?<br>4 options: The spark, because it is far hotter / The bath, because there is far more of it / Neither — they are both the same kind of energy / The spark, because sparks are made of metal | If you had to guess, which one holds more energy?<br>**A:** The spark<br>**B:** The bath<br>*also changed: scene, big question* | **The bath.** The bath holds something like a hundred million times more. The spark is far hotter, but there is almost nothing of it. | batch 6: committed, not pushed |
| 7 | why-ice-floats (P11) | Why does the ice float on the water it came from?<br>4 options: Ice is lighter than water, because it is frozen / Ice is less dense than the water it came from / The ice is held up by bubbles trapped in it / Cold things always float on warm things | If you had to guess, why does ice float on the water it came from?<br>**A:** Freezing makes it take more room<br>**B:** Freezing makes it weigh less<br>*also changed: big question* | **Freezing makes it take more room.** Water gets about 9% bigger when it freezes, but it weighs the same. The same mass in more room makes ice less dense than water, so it floats. | batch 6: committed, not pushed |
| 8 | the-gas-exchange-system (B4) | What does that tell you about the air you breathe out?<br>4 options: It has no oxygen left — something else must be keeping them alive / It still contains most of the oxygen that went in / It is mostly carbon dioxide, which the body can use in an emergency / It works only because the rescuer breathes very deeply first | If you had to guess, how much of the oxygen in a breath is still there when you breathe it out?<br>**A:** Most of it<br>**B:** Hardly any of it<br>*also changed: title, scene, big question* | **Most of it.** You keep only about a quarter of the oxygen in each breath and pass the rest straight back out. That is why a first-aider's breath can help someone else. | batch 6: committed, not pushed |
| 8 | how-breathing-works (B4) | Nothing is blocking it. Why can it not fill?<br>4 options: The wound is letting air escape faster than it can go in / The lung needs the pressure around it to be lower than the air inside it / The lung muscles have been cut / Blood has filled the alveoli | If you had to guess, how does a healthy lung normally fill with air?<br>**A:** The chest stretches it open<br>**B:** It stretches itself open<br>*also changed: title, scene, big question* | **The chest stretches it open.** A lung has no muscle and cannot open itself. As the chest gets bigger, the lung is stretched open with it. Once air gets in around the lung, that stops working. | batch 6: committed, not pushed |
| 8 | alveoli-built-for-exchange (B4) | How long would you survive?<br>4 options: Normally — the same air is still in there / A few hours, breathing much faster / Minutes — almost all the exchange surface has gone / Indefinitely, as long as you kept the airway clear | If you had to guess, could you stay alive with the bag instead?<br>**A:** Yes, just as well<br>**B:** No, not for long<br>*also changed: title, scene* | **No, not for long.** A smooth bag has hardly any surface for oxygen to pass through, so you would last only minutes. What matters is surface, not the amount of air. | batch 6: committed, not pushed |
| 8 | exercise-asthma-and-smoking (B4) | If the air is fine, what has gone wrong?<br>4 options: The oxygen in the air around them has dropped / Their alveoli have stopped working / The tubes carrying air to the alveoli have narrowed / Their diaphragm has stopped contracting | If you had to guess, does the puff from the inhaler contain extra oxygen?<br>**A:** Yes, extra oxygen<br>**B:** No oxygen at all<br>*also changed: title, scene* | **No oxygen at all.** There is no oxygen in it. The air around them already has plenty; the medicine relaxes muscle in the walls of the air tubes, so they widen and air gets through. | batch 6: committed, not pushed |
| 8 | stomata-and-gas-exchange-in-plants (B4) | What is the plant doing during those steady minutes?<br>4 options: Nothing — it is between processes / Only photosynthesis, at a very low rate / Respiring and photosynthesising at exactly equal rates / It has closed its stomata so no gas can move | If you had to guess, during those steady minutes, is the plant making or using any carbon dioxide at all?<br>**A:** No, it is doing neither<br>**B:** Yes, it is doing both<br>*also changed: big question* | **Yes, it is doing both.** It is respiring, which makes carbon dioxide, and photosynthesising, which uses it up. At that light level the two run at the same rate, so the reading stays flat. | batch 6: committed, not pushed |
| 8 | human-reproductive-systems (B5) | Two systems with the same purpose. Why such different strategies?<br>4 options: One system is more efficient than the other / The two gametes have very different jobs, so they cost very different amounts to make / Egg cells last longer, so fewer are needed / It is a coincidence with no biological reason | If you had to guess, are egg cells made all the time too?<br>**A:** Yes, all the time<br>**B:** No, only before birth<br>*also changed: title, scene, big question* | **No, only before birth.** The ovaries of a newborn already hold every immature egg cell there will ever be, about a million, and no new ones are made. Only about four hundred are ever released. | batch 6: committed, not pushed |
| 8 | gametes-and-fertilisation (B5) | Equal instructions, wildly unequal size. Where has all the extra gone?<br>4 options: The egg carries more copies of the chromosomes / The egg carries cytoplasm, mitochondria and a food store / The sperm loses most of itself on the journey / The egg is bigger because it is older | If you had to guess, is most of the egg's extra size more genetic instructions, or food and supplies?<br>**A:** Food and supplies<br>**B:** More genetic instructions<br>*also changed: title, scene, big question* | **Food and supplies.** The egg is packed with food and the machinery to build a body, which the new cell needs for its first days. Both cells bring the same instructions: 23 chromosomes each. | batch 6: committed, not pushed |

## Arguable calls

The full per-lesson review notes (what each reviewer changed and why) are kept
with the run's scratch files; these are the calls worth Mide's eye.

**How the rule was applied**

- **"Good guess." / "Fair guess."** open every reply, as in KS4's `Ks4Guess`.
  KS3's R3 says activities never mark, and the options are never visually
  marked, but those two words do tell a pupil which option was right. That is
  what the rule's "friendly reply to each option" asks for, and what KS4 does.
  If Mide wants KS3 strictly unmarked, the two words are one line in
  `_hook_guess()` (`build_ks3.py`).
- **Options stay re-choosable** (R3); `Ks4Guess` locks after one pick. A pupil
  can press the other option and read its reply too.
- **The railbar and the H1 count as "above it".** On load, the railbar shows the
  hook's rail label directly above the H1, and neither may be changed. Where
  either answered the natural guess, the guess changed angle instead (e.g. *seasons-and-the-tilt*'s label reads "Closer in January";
  *how-far-is-a-light-year*'s H1 is the question itself; *the-earth-is-a-magnet*,
  *electromagnets*, *sound-needs-a-medium*, *atmospheric-pressure*,
  *conservation-of-energy*). Each new angle is still that lesson's own science.
- **Later text that points back at the hook was kept true.** Where a rail
  label, ladder feedback or vocabulary note refers to the hook's situation
  ("the door-hinge test at the top of this lesson", "the bag of sugar at the
  top of this lesson", "This is the dawn reading from the hook", "This is the
  hook, with a bigger ball"), the opener kept that situation. *moments*, *the-
  gas-exchange-system*, *stomata-and-gas-exchange-in-plants*, *non-contact-
  forces* and *drawing-and-adding-forces* went back to their old scenes for
  this reason.
- **A guess may repeat a question the page asks later** only where the old hook
  already asked it (the brief's allowance): *acid-plus-metal*, *whats-in-the-
  air*, *filtration*, *distillation*, *hearing-and-auditory-range*,
  *gestation-placenta-and-birth*, *aerobic-respiration*. Where a draft
  answered a *different* later prediction, it was changed (*displacement*,
  *chemical-vs-physical-change*, *word-equations*, *symbol-equations-and-
  balancing*, *transverse-waves-and-superposition*, *mass-in-a-reaction*).
- **Some hooks no longer offer the misconception the register says they
  elicit** (*toxic-build-up* ECO-09, *echoes* WAVE-25/27, *light-year*
  SPACE-19, *disturbing-a-food-web* ECO-05, *relative-motion* FORCE-09). In
  each case the H1 or rail label already ruled that belief out, so it could not
  be drawn out honestly. The register is metadata; no gate reads it beyond the
  `#s-hook` anchor.

**Science judgement calls (Mide's gate)**

- *testing-the-model*: solid candle wax sinks in its own melt (paraffin about
  0.90 g/cm³ solid against 0.78 liquid; it is why a candle sinks round the
  wick). Matches the lesson's "almost every other solid sinks in its own liquid".
- *springs-and-hookes-law*: "the pattern stops before 10 N" holds for the
  lesson's model spring (limit 6 N) and a small school-lab spring; a very stiff
  spring would survive 10 N.
- *gravity-and-weight*: the scale reads "a little less" on Everest (about 0.3%,
  the lesson's own figure). True of the reading, though smaller than a bathroom
  scale's error.
- *ceramics-polymers-and-composites*: rests on the lesson's claim that a china
  plate laid flat on a hard floor would hold a person standing on it.
- *what-drugs-do-to-the-body*: "caffeine is a drug" rests on the lesson's
  definition, "any substance that changes the way the body works".
- *chemical-vs-physical-change*: colour change is the wrong option, following
  the lesson's ruling that colour is a clue and not the test; some KS3 courses
  call it a "sign of reaction". The reply concedes it is a clue.
- *human-reproductive-systems*: "about a million" immature eggs at birth is the
  lesson's figure; sources give 1–2 million.
- *seasons-and-the-tilt*: the correct reply states the Earth is nearest the Sun
  in early January.
- *the-atom-daltons-model*: "furnaces, acids and mixing" deliberately rules out
  nuclear transmutation.

## Lesson-text issues found, not fixed (outside the opener rule)

The rule forbade touching any other lesson text, so these are reported, not
changed. The first group are science errors on live pages.

**Science errors**

1. **groups-and-periods** — potassium is *one* period below sodium (periods 3
   and 4), not two. Still wrong in the hook's rail label "Next door and two rows
   down" (shown above the H1 on load) and in the think reveal ("two rows down the
   same column"). The opener no longer says it.
2. **group-1-the-alkali-metals** — the explainer says every group 1 metal is
   "light enough to float on water", and the ladder's *produce* success
   criterion credits "caesium would float". Rubidium (≈1.5 g/cm³) and caesium
   (≈1.9 g/cm³) sink.
3. **charging-by-rubbing** — the think block (CHRG-01) says "Every electron
   that ends up on the duster was on the rod a moment earlier". In this lesson
   the polythene rod ends up negative, so the electrons went from the duster to
   the rod: backwards. (The hook's own old reveal had it right.)
4. **energy-and-changes-of-state** — the think reveal says melting takes
   "several times more energy than warming the same water by a single degree"
   (it is about 80 times: 334 kJ/kg against 4.2 kJ/kg per °C), and that ice at
   the plateau "is absorbing heat faster than at any other point". With a steady
   flame the *rate* is the same throughout; it is the *total* that is large.
5. **heating-and-thermal-equilibrium** — the hook scene still says a 40 °C bath
   "can genuinely injure a small child"; the file's own MRB-297 note says 40 °C
   is a normal bath (the meta description was corrected, the scene was not).
6. **unicellular-organisms** — the big question calls a Paramecium "a whole
   animal"; it is a single-celled protist ("a whole organism").
7. **chromosomes-genes-and-dna** — the hook scene says "Every cell in your body
   is doing this" (copying DNA in the nucleus); red blood cells have no nucleus,
   as the lesson's own bench card says.
8. **acids-and-alkalis** — the big question says one liquid "is safe to drink";
   the scene says both are dangerous, and neither is safe.
9. **atmospheric-pressure** — the old title "Nothing touched the can." and big
   question "nothing goes anywhere near it" are false (the air presses on it).
   The opener replaces the title; the meta description still says it.
10. **the-gas-exchange-system** — "Six parts, and only the last one exchanges
    anything": the sixth card is the ribs and muscles; the exchanger is the
    fifth (already flagged in the lesson's docstring).
11. **refraction** — "slows down when it enters a denser transparent material":
    a pupil will read "denser" as mass density, and perspex is less dense than
    water yet slows light more.

**Wording and references**

- *word-equations*: the rail label "Twenty-two words" — the quoted sentence has 25.
- *gravity-and-weight*: the hook's rail label is "The falling lift", but the hook
  (old and new) is Everest.
- *human-reproductive-systems*: the oviduct note says "the structure the reveal
  warned you about"; no reveal mentions the oviduct.
- *group-0-and-why-groups-exist*: a vocabulary note shows a raw anchor id to
  pupils ("that is the whole of #s-uses").
- *chromatography*: Pen D's lane is a single blue spot, but the scene says all
  four inks look identical on paper.
- *which-reaction-is-this* calls acid + carbonate "neutralisation"; the C6
  carbonates lesson never does.
- *compounds*: the safety note says hydrogen sulfide is given off; the explainer
  says every atom "is still in the dish".
- *P6 misconception ids*: on five P6 pages (how-sound-is-made, transverse-waves,
  frequency-pitch-and-loudness, sound-needs-a-medium, hearing-and-auditory-range)
  the "Think again" quotes carry ids one or two off the register's.
- *energy-stores*, *atmospheric-pressure*, *echoes*: the meta description (search
  snippet) still states the hook's answer.
- **Rail labels and H1s that state their lesson's answer before the hook**
  (handled by moving the guess, listed so Mide can decide whether to change the
  labels): *formulae* "One atom apart", *relative-motion* "Relative to what",
  *gestation-placenta-and-birth* "Never mix", *lifestyle-and-the-developing-
  foetus* "Not a filter", *leaves-built-for-the-job* "Every hole leaks",
  *seasons-and-the-tilt* "Closer in January", *the-sun-stars-and-galaxies* "A
  star you can see in daylight", *how-far-is-a-light-year* (H1 and "A year that
  is a distance"), *antagonistic-muscle-pairs* "Only ever a pull",
  *biomechanics* "Eight times harder", *thermal-decomposition* "One in, two
  out", *what-a-force-is* "The wall pushed you", *gravity-earth-moon-and-sun*
  "Why the Moon does not fall" (the lesson's point is that it *is* falling).
