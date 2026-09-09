"""B4 lesson 01 — The gas exchange system: twelve questions (MRB-269).

The lesson makes two arguments and the bank probes both. The first is the
route: six parts, five of them airway, and exchange happening at exactly one
of them. The second is the two bags — exhaled air is still mostly the air that
went in, and every figure on the page is there to stop a student saying
otherwise. The easier band holds the four facts the route rests on (why the
trachea is ringed with cartilage, where oxygen actually crosses, what the nose
does that the mouth does not, what cilia do with trapped dust). The standard
band works situations the lesson itself raises — the ventilator, the asthma
attack, the hundredfold carbon dioxide rise, and breath visible on a cold
morning. The harder band takes the ideas somewhere new or joins two of them:
the floating piece of lung read as evidence about surface area, the fetus whose
lungs never held air, the nitrogen stretch layer set against "unchanged means
unused", and a tracheostomy that bypasses the conditioning step.

The distractors are the lesson's three declared misconceptions plus the two
errors the route exists to correct. BREATH-01 ("you breathe in oxygen and
breathe out carbon dioxide") supplies the mostly-carbon-dioxide and
oxygen-removed options in s03 and the invisible-oxygen mist in s04. BREATH-02
("breathing and respiration are the same thing") is the whole of s01. BREATH-03
("your lungs are hollow bags that fill up like balloons") supplies the hollow
cavity and the muscle-packed lung in h01. Two more run through the bank: that
gas exchange happens a little all the way down the airway (e02, e03, h04), and
that the nose or the airway adds oxygen to the air rather than conditioning it
(e03, h04). The cartilage rings are used three times as a test of whether a
student knows stiff-and-holding-open from muscular-and-narrowing (e01, s02,
h04).

`figure` is None throughout. The lesson declares one figure,
`b4-gas-exchange-labelled`, at `status: "needed"` — no artwork exists for it
yet, so a question that leaned on it would be unanswerable.
"""

UNIT = "B4"
LESSON = "the-gas-exchange-system"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b4-01-e01",
        "band": "easier",
        "text": "The trachea is held open by C-shaped rings of cartilage. "
                "What would go wrong without them?",
        "options": [
            {"text": "It would fill with mucus, because the cilia need "
                     "cartilage to push against.",
             "correct": False,
             "why": "Mucus and cilia clean the air, and they do that whether "
                    "the tube around them is stiff or not. The rings do a "
                    "mechanical job instead: they stop the tube closing."},
            {"text": "It could collapse inwards when the pressure inside it "
                     "drops on a breath in.",
             "correct": True},
            {"text": "It could not narrow in an asthma attack, so attacks "
                     "would do no harm.",
             "correct": False,
             "why": "The narrowing in an asthma attack happens in the "
                    "bronchioles, which have muscle in their walls instead of "
                    "cartilage. The trachea's rings exist for the opposite "
                    "reason — to keep it open."},
            {"text": "No gas exchange could happen along it, so less oxygen "
                     "would reach the blood.",
             "correct": False,
             "why": "No gas exchange happens in the trachea at any time, rings "
                    "or no rings. It is a transport tube, and the only "
                    "exchange surface in your body is the alveoli."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e02",
        "band": "easier",
        "text": "Oxygen crosses into your blood in one place and nowhere "
                "else. Which part of the route is it?",
        "options": [
            {"text": "The trachea, where the air is closest to the front of "
                     "the neck.",
             "correct": False,
             "why": "The trachea is plumbing. It is lined with mucus and cilia "
                    "to clean the air on its way past, and nothing crosses "
                    "into the blood there."},
            {"text": "The bronchi, where the air first arrives inside a lung.",
             "correct": False,
             "why": "The bronchi are still wide and still ringed with "
                    "cartilage, and the lesson is blunt about them: no "
                    "exchange happens here."},
            {"text": "A little at every stage of the route, from the nose "
                     "downwards.",
             "correct": False,
             "why": "This is the commonest version of the mistake. Every part "
                    "before the alveoli either moves the air or conditions it "
                    "— not one molecule of oxygen crosses into the blood until "
                    "the air reaches an alveolus."},
            {"text": "The alveoli, some 500 million air sacs wrapped in "
                     "capillaries.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e03",
        "band": "easier",
        "text": "Cold dry air taken in through an open mouth irritates the "
                "airways. What is your nose doing that your mouth does far "
                "less well?",
        "options": [
            {"text": "Warming, moistening and filtering the air with hairs "
                     "and mucus.",
             "correct": True},
            {"text": "Adding oxygen to the air before it travels down to the "
                     "lungs.",
             "correct": False,
             "why": "Nothing in your body adds oxygen to the air you breathe "
                    "in — it arrives at 21% oxygen and the alveoli take some "
                    "of it out. The nose changes the air's temperature, "
                    "wetness and cleanliness, not what it is made of."},
            {"text": "Starting gas exchange early, so less is left for the "
                     "alveoli to do.",
             "correct": False,
             "why": "Gas exchange happens in the alveoli and nowhere else. "
                    "Everything above them prepares the air; none of it swaps "
                    "any gas with the blood."},
            {"text": "Slowing the air down so that more of it fits inside the "
                     "lungs.",
             "correct": False,
             "why": "How much air fits in your chest is set by the muscles "
                    "that change the chest's volume, not by how fast the air "
                    "moves through your nose. The nose's job is conditioning."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e04",
        "band": "easier",
        "text": "You breathe in a speck of dust and it sticks in the mucus "
                "lining your trachea. What happens to it next?",
        "options": [
            {"text": "It carries on down to an alveolus and passes into the "
                     "blood with the oxygen.",
             "correct": False,
             "why": "An alveolus wall is one cell thick and lets gases across, "
                    "not specks of dust. Trapping the dust long before it gets "
                    "that far is exactly what the mucus is for."},
            {"text": "It stays stuck there for good, because nothing in the "
                     "airway can shift it.",
             "correct": False,
             "why": "The airway is not passive. Cilia — tiny hairs lining it — "
                    "beat constantly and move the mucus along, so trapped dust "
                    "does not stay where it lands."},
            {"text": "Cilia sweep it, still in the mucus, back up the airway "
                     "away from the lungs.",
             "correct": True},
            {"text": "It is broken down by the cartilage rings as the trachea "
                     "flexes around it.",
             "correct": False,
             "why": "Cartilage is stiff supporting tissue that holds the tube "
                    "open. It breaks nothing down, and nothing in the airway "
                    "digests dust."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b4-01-s01",
        "band": "standard",
        "text": "A patient on a ventilator is described as “not respiring — "
                "the machine is doing it for them”. Why is that description "
                "wrong?",
        "options": [
            {"text": "The machine is doing their gas exchange for them, so it "
                     "is gas exchange that stopped.",
             "correct": False,
             "why": "Gas exchange still happens in the patient's own alveoli — "
                    "the machine only delivers air to them. No machine swaps "
                    "gases with your blood."},
            {"text": "The machine is breathing for them; respiration carries "
                     "on in every cell.",
             "correct": True},
            {"text": "Respiration only stops when the heart stops, so the "
                     "sentence would be right later.",
             "correct": False,
             "why": "That swaps one failure for another. Respiration is "
                    "happening in the patient's cells the whole time the "
                    "machine works — the word simply does not mean what the "
                    "sentence assumes."},
            {"text": "Nothing is wrong with it — a ventilator does a "
                     "patient's respiring for them.",
             "correct": False,
             "why": "This is the mistake the sentence contains. Respiration is "
                    "a chemical reaction inside cells, releasing energy from "
                    "glucose. A machine pushing air into an airway is doing "
                    "the breathing."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s02",
        "band": "standard",
        "text": "In an asthma attack the airways narrow. Which part narrows, "
                "and what makes that possible?",
        "options": [
            {"text": "The bronchioles, which have muscle in their walls "
                     "instead of cartilage.",
             "correct": True},
            {"text": "The trachea, because its C-shaped cartilage rings "
                     "tighten around it.",
             "correct": False,
             "why": "Cartilage rings are stiff and hold the trachea open — "
                    "that is their whole purpose. They cannot tighten, and the "
                    "trachea is not what narrows."},
            {"text": "The bronchi, because they are the widest tubes and so "
                     "carry the most muscle.",
             "correct": False,
             "why": "The bronchi are wide, but they are still ringed with "
                    "cartilage, like the trachea. The muscle appears further "
                    "down the branching, where the cartilage runs out."},
            {"text": "The alveoli, because their walls are one cell thick and "
                     "collapse easily.",
             "correct": False,
             "why": "A wall one cell thick is what makes an alveolus good at "
                    "exchange, not what makes it narrow. The narrowing is in "
                    "the tubes leading to them."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s03",
        "band": "standard",
        "text": "Carbon dioxide goes from 0.04% of the air in to 4% of the "
                "air out — a hundredfold rise. A student writes that this "
                "proves exhaled air is mostly carbon dioxide. Pick the best "
                "correction.",
        "options": [
            {"text": "A hundredfold rise means there is now a hundred times "
                     "more carbon dioxide than oxygen.",
             "correct": False,
             "why": "A hundredfold says how much the carbon dioxide changed, "
                    "not how it compares with anything else. Exhaled air is "
                    "about 16% oxygen and 4% carbon dioxide — four times more "
                    "oxygen, not less."},
            {"text": "The 4% figure has to be wrong, because exhaled air has "
                     "had all its oxygen taken out.",
             "correct": False,
             "why": "Only about a quarter of the oxygen is taken out: 21% goes "
                    "in and 16% comes out. Neither figure is wrong, and "
                    "neither gas comes close to being most of the bag."},
            {"text": "Percentages of different gases cannot be compared, so "
                     "nothing can be said about which is biggest.",
             "correct": False,
             "why": "They can, and the whole bench activity depends on it — "
                    "both bags are measured the same way. Compare them "
                    "straight off: 78, then 16, then 4."},
            {"text": "4% is a twenty-fifth of the bag — a huge rise from a "
                     "tiny start still stays small.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s04",
        "band": "standard",
        "text": "On a cold morning you can see your breath; indoors in "
                "summer you cannot. What is becoming visible, and why only "
                "in the cold?",
        "options": [
            {"text": "The carbon dioxide you breathed out, which only shows "
                     "up at low temperatures.",
             "correct": False,
             "why": "Carbon dioxide is a colourless gas at every temperature, "
                    "and it is only 4% of the bag. What you can see is liquid "
                    "water in tiny droplets."},
            {"text": "Your body only adds water to the air when it is cold, "
                     "to warm that air up.",
             "correct": False,
             "why": "Exhaled air is saturated with water vapour whatever the "
                    "weather. What the cold changes is not how much water "
                    "leaves you but whether it condenses where you can see "
                    "it."},
            {"text": "Water vapour: exhaled air is saturated, and the cold "
                     "condenses it.",
             "correct": True},
            {"text": "Oxygen you did not use, turning into mist as it cools "
                     "in the outside air.",
             "correct": False,
             "why": "Oxygen stays a gas far below any weather on Earth, and "
                    "the oxygen you did not use is invisible — it is 16% of "
                    "every breath out."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b4-01-h01",
        "band": "harder",
        "text": "A piece of fresh lung feels like a solid sponge, and it "
                "floats when you drop it in water. What does that texture "
                "tell you about how a lung is built?",
        "options": [
            {"text": "It is one hollow cavity full of air, which is what "
                     "makes it light enough to float.",
             "correct": False,
             "why": "That is the balloon picture, and the sponge texture is "
                    "the evidence against it. A single open cavity would feel "
                    "like an empty bag, not like solid tissue."},
            {"text": "It is packed with muscle, which feels solid and "
                     "squeezes the air back out again.",
             "correct": False,
             "why": "There is no muscle anywhere in a lung — it cannot move "
                    "itself, which is why the diaphragm and ribs exist. The "
                    "branching is what makes the tissue feel solid."},
            {"text": "It is divided again and again into some 500 million "
                     "alveoli — all surface area.",
             "correct": True},
            {"text": "The sponge slows the air down so the oxygen has longer "
                     "to cross into the blood.",
             "correct": False,
             "why": "The structure is not about slowing air down. Gas exchange "
                    "is limited by surface area, and every one of those "
                    "twenty-three divisions exists to turn a bag into a "
                    "surface."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h02",
        "band": "harder",
        "text": "Before you were born your lungs had never held air, yet "
                "your blood carried oxygen the whole time. Which statement "
                "fits this lesson?",
        "options": [
            {"text": "The placenta did the gas exchange; after birth the "
                     "alveoli are the only place.",
             "correct": True},
            {"text": "A fetus takes oxygen in through its skin, and switches "
                     "over to its lungs at birth.",
             "correct": False,
             "why": "Nothing in this lesson gives skin an exchange role, and "
                    "the lesson names the placenta directly: before you were "
                    "born, the placenta did all of it."},
            {"text": "The fetal alveoli exchange gases with the fluid around "
                     "the baby instead of with air.",
             "correct": False,
             "why": "Fluid-filled alveoli are doing no exchanging. The oxygen "
                    "arrives already dissolved in the blood, from the "
                    "placenta, and the alveoli only start work at the first "
                    "breath."},
            {"text": "Gas exchange can happen anywhere in the body whenever "
                     "the lungs are not available.",
             "correct": False,
             "why": "“The only place” means exactly that, once you are "
                    "breathing air. Before birth the swap happened at the "
                    "placenta — not at some spare site inside the fetus."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h03",
        "band": "harder",
        "text": "Nitrogen goes in at 78% and comes out at 78%. A student "
                "concludes that your body has no use for nitrogen at all. "
                "Where does that reasoning break down?",
        "options": [
            {"text": "It does not — nitrogen is unchanged, so your body "
                     "genuinely never uses any of it.",
             "correct": False,
             "why": "The gas being unchanged is right; the conclusion is not. "
                    "You are full of nitrogen — it is in every protein and "
                    "every strand of DNA in you. The leap from “not taken from "
                    "the air” to “not used” is what fails."},
            {"text": "You are built from nitrogen, but all of it comes from "
                     "food, not from the air.",
             "correct": True},
            {"text": "The figures are rounded, so a small amount really is "
                     "absorbed on every breath.",
             "correct": False,
             "why": "Rounding is not hiding an absorption. Your body cannot "
                    "break the triple bond in N₂ at all — certain bacteria "
                    "can, and no animal can."},
            {"text": "Your body does use it, but only in exercise, when your "
                     "breathing is much deeper.",
             "correct": False,
             "why": "Breathing harder moves more air of the same composition. "
                    "Nitrogen goes in and comes out unchanged at every "
                    "breathing rate."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h04",
        "band": "harder",
        "text": "A patient has a tube fitted straight into the trachea "
                "through the front of the neck, so air no longer passes "
                "through the nose or mouth. Predict one problem this "
                "creates.",
        "options": [
            {"text": "No gas exchange can happen, because air has to pass "
                     "the nose to be exchanged.",
             "correct": False,
             "why": "Gas exchange happens in the alveoli and nowhere else, and "
                    "the tube still delivers air to them. The nose adds "
                    "nothing to the swap itself."},
            {"text": "Less oxygen reaches the alveoli, because the nose is "
                     "where oxygen enters the air.",
             "correct": False,
             "why": "The nose adds no oxygen. Air is already 21% oxygen before "
                    "it reaches you, and the nose changes its temperature, "
                    "wetness and cleanliness, not what it is made of."},
            {"text": "The trachea will collapse, because its rings hold it "
                     "open only when air comes from above.",
             "correct": False,
             "why": "The C-shaped cartilage rings are stiff all the time. They "
                    "hold the tube open whatever route the air took to get "
                    "there."},
            {"text": "The air arrives cold, dry and unfiltered, because the "
                     "conditioning step is skipped.",
             "correct": True},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b4-01-e05",
        "band": "easier",
        "text": "Put these parts of the airway in the order air travels "
                "through them on the way in.",
        "options": [
            {"text": "Nose and mouth, bronchi, trachea, bronchioles, alveoli.",
             "correct": False,
             "why": "The trachea and the bronchi are the wrong way round. The "
                    "trachea is a single tube, and it divides into the two "
                    "bronchi — so the single tube has to come first."},
            {"text": "Nose and mouth, trachea, bronchi, bronchioles, alveoli.",
             "correct": True},
            {"text": "Nose and mouth, trachea, bronchioles, bronchi, alveoli.",
             "correct": False,
             "why": "The bronchioles are the narrowest branches, so they come "
                    "after the bronchi and not before them. The airway gets "
                    "narrower the further in you go, never wider."},
            {"text": "Nose and mouth, trachea, alveoli, bronchi, bronchioles.",
             "correct": False,
             "why": "The alveoli are the end of the airway, not the middle of "
                    "it. Air reaches them last, after about twenty-three "
                    "divisions of branching."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e06",
        "band": "easier",
        "text": "What do the words gas exchange mean?",
        "options": [
            {"text": "Moving air in and out of the lungs using muscles.",
             "correct": False,
             "why": "That is breathing. Gas exchange is the swap that happens "
                    "at the end of the airway, after the air has arrived."},
            {"text": "A chemical reaction that releases energy from glucose "
                     "inside every living cell.",
             "correct": False,
             "why": "That is respiration, and it happens in every cell in "
                    "your body. Gas exchange happens in one place only."},
            {"text": "Oxygen and carbon dioxide swapping between the "
                     "alveoli and the blood.",
             "correct": True},
            {"text": "Warming, moistening and filtering the air in the nose "
                     "and throat before it reaches the lungs.",
             "correct": False,
             "why": "That is conditioning, and the nose does most of it. "
                    "Nothing is swapped with the blood while it happens."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e07",
        "band": "easier",
        "text": "Roughly how many alveoli does a pair of human lungs hold, "
                "and what is wrapped around each one?",
        "options": [
            {"text": "About 500 million, each wrapped in capillaries.",
             "correct": True},
            {"text": "About 500, each wrapped in a ring of cartilage.",
             "correct": False,
             "why": "Cartilage rings belong to the trachea and the bronchi, "
                    "where they hold wide tubes open. There are hundreds of "
                    "millions of alveoli, not hundreds."},
            {"text": "About two, one large sac filling each lung.",
             "correct": False,
             "why": "That is the hollow-bag picture. A lung is a solid-feeling "
                    "sponge, divided again and again into hundreds of millions "
                    "of sacs."},
            {"text": "About 500 million, each wrapped in a layer of muscle.",
             "correct": False,
             "why": "The number is right and the wrapping is not. There is no "
                    "muscle anywhere in a lung — what covers every alveolus is "
                    "a dense net of capillaries carrying blood."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e08",
        "band": "easier",
        "text": "Inhaled air is about 21% oxygen. About how much oxygen is in "
                "the air you breathe out?",
        "options": [
            {"text": "About 0%, because your body takes all of it.",
             "correct": False,
             "why": "You keep only about a quarter of the oxygen you take in. "
                    "If exhaled air held none, mouth-to-mouth resuscitation "
                    "could not work."},
            {"text": "About 4%, the same as the carbon dioxide figure.",
             "correct": False,
             "why": "4% is the carbon dioxide figure, not the oxygen one. "
                    "Exhaled air holds four times more oxygen than carbon "
                    "dioxide."},
            {"text": "About 21%, because breathing does not change it.",
             "correct": False,
             "why": "Nitrogen is the gas that comes out unchanged. Oxygen does "
                    "fall, from 21% to about 16%, and that fall is what your "
                    "blood took."},
            {"text": "About 16%, so roughly a quarter of it has been taken.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e09",
        "band": "easier",
        "text": "Apart from the gases, what else is different about exhaled "
                "air compared with the air that went in?",
        "options": [
            {"text": "It is colder and drier, because the lungs take heat and "
                     "water out of it.",
             "correct": False,
             "why": "Both the wrong way round. Air is warmed to body "
                    "temperature and moistened on the way in, and it leaves "
                    "carrying that heat and water with it."},
            {"text": "It is warmer, and it is saturated with the water vapour it "
                     "picked up.",
             "correct": True},
            {"text": "It is warmer, but it holds exactly as much water as it "
                     "did going in.",
             "correct": False,
             "why": "The airway moistens the air as well as warming it, which "
                    "is why exhaled air comes out saturated. That water is the "
                    "mist you can see on a cold morning."},
            {"text": "It is heavier, because carbon dioxide has replaced most "
                     "of the oxygen.",
             "correct": False,
             "why": "Carbon dioxide has replaced almost none of it — the air "
                    "out is 4% carbon dioxide and still 16% oxygen. What has "
                    "changed besides the gases is the temperature and the "
                    "water."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e10",
        "band": "easier",
        "text": "The ribs, the intercostal muscles and the diaphragm are all "
                "involved in getting air into you. How are they different "
                "from the trachea, the bronchi and the alveoli?",
        "options": [
            {"text": "They are the parts where the air is warmed and "
                     "filtered.",
             "correct": False,
             "why": "Conditioning is done by the nose and the lining of the "
                    "airway. The ribs, the muscles between them and the "
                    "diaphragm never touch the air at all."},
            {"text": "They are the widest parts of the airway, so the most "
                     "air passes through them.",
             "correct": False,
             "why": "No air passes through any of them. They sit outside the "
                    "lungs, and the airway runs from the nose to the alveoli "
                    "without going near them."},
            {"text": "They are not part of the airway — they are the "
                     "machinery that moves the air.",
             "correct": True},
            {"text": "They are where a small amount of gas exchange happens "
                     "before the alveoli.",
             "correct": False,
             "why": "Gas exchange happens in the alveoli and nowhere else, and "
                    "these three are not even part of the airway. They "
                    "change the volume of the chest."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e11",
        "band": "easier",
        "text": "At its lower end the trachea divides into two tubes. What "
                "are they called and where does each one go?",
        "options": [
            {"text": "The bronchi, one running into each lung.",
             "correct": True},
            {"text": "The bronchioles, one running into each lung.",
             "correct": False,
             "why": "The bronchioles come much further along. They are the "
                    "narrowest branches, produced after the bronchi have "
                    "divided again and again inside the lungs."},
            {"text": "The alveoli, one filling each lung.",
             "correct": False,
             "why": "The alveoli are the tiny sacs at the very end of the "
                    "airway, and there are hundreds of millions of them, "
                    "not two. The first split gives the two bronchi."},
            {"text": "The bronchi, one running to a lung and one to the "
                     "stomach.",
             "correct": False,
             "why": "Nothing in the airway leads to the stomach. Both bronchi "
                    "carry air, one into the left lung and one into the "
                    "right."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b4-01-s05",
        "band": "standard",
        "text": "A firefighter breathes smoky air for several minutes without "
                "a mask and coughs for hours afterwards. What is the lining "
                "of their airway doing?",
        "options": [
            {"text": "Absorbing the smoke particles into the blood so they "
                     "can be carried away.",
             "correct": False,
             "why": "Nothing but dissolved gas crosses into the blood, and "
                    "only at the alveoli. Soot particles are trapped long "
                    "before they get that far."},
            {"text": "Narrowing the trachea by tightening its cartilage rings "
                     "to keep the smoke out.",
             "correct": False,
             "why": "Cartilage rings are stiff and hold the trachea open; they "
                    "cannot tighten. The airway's defence against particles is "
                    "mucus and cilia, not a change of width."},
            {"text": "Producing extra mucus to trap the particles, which the "
                     "cilia then sweep back up.",
             "correct": True},
            {"text": "Sending the particles down to the alveoli, where they "
                     "are broken down.",
             "correct": False,
             "why": "The alveoli are the last place you would want a particle "
                    "to reach, and nothing there breaks anything down. The "
                    "whole point of the mucus is to stop that happening."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s06",
        "band": "standard",
        "text": "Each bronchus divides again and again — about twenty-three "
                "generations of branching — before the airway ends. What "
                "does all that dividing achieve?",
        "options": [
            {"text": "It ends in hundreds of millions of sacs, which is an "
                     "enormous surface for exchange.",
             "correct": True},
            {"text": "It slows the air down, so each molecule of oxygen has "
                     "longer to cross.",
             "correct": False,
             "why": "The branching is not about timing. Gas exchange is "
                    "limited by how much surface the air and the blood can "
                    "meet across, and dividing is how a bag is turned into a "
                    "surface."},
            {"text": "It lets the lungs hold far more air than a single "
                     "cavity of the same size would.",
             "correct": False,
             "why": "Branching does not add volume — a sponge and a bag of the "
                    "same size hold about the same air. What branching adds is "
                    "surface."},
            {"text": "It filters the air a little more at every branch, so "
                     "the deepest air is the cleanest.",
             "correct": False,
             "why": "Filtering is done by the hairs, mucus and cilia higher "
                    "up, and it is not what the branching is for. The reason "
                    "for dividing is surface area."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s07",
        "band": "standard",
        "text": "You hold your breath for thirty seconds. Which of the three "
                "processes has stopped, and which are still going?",
        "options": [
            {"text": "All three have stopped, because nothing can happen "
                     "without fresh air.",
             "correct": False,
             "why": "Only the movement of air has stopped. There is still air "
                    "in your alveoli and still oxygen in your blood, so the "
                    "other two carry on."},
            {"text": "Respiration has stopped; breathing and gas exchange "
                     "carry on.",
             "correct": False,
             "why": "Respiration is the one that cannot stop — it is running "
                    "in every cell, and it is what makes holding your breath "
                    "uncomfortable. Breathing is the one you have paused."},
            {"text": "Breathing has stopped; gas exchange and respiration "
                     "carry on.",
             "correct": True},
            {"text": "Gas exchange has stopped; breathing and respiration "
                     "carry on.",
             "correct": False,
             "why": "You cannot be breathing while holding your breath. And "
                    "oxygen keeps crossing into the blood from the air already "
                    "sitting in your alveoli."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s08",
        "band": "standard",
        "text": "A student calls exhaled air “used air”. Inhaled air is 78% "
                "nitrogen and 21% oxygen; exhaled air is 78% nitrogen and "
                "about 16% oxygen. Why is “used air” a poor description?",
        "options": [
            {"text": "It is a fair description, because every gas in the bag "
                     "has been altered by the body.",
             "correct": False,
             "why": "Nitrogen is 78% of the bag going in and 78% coming out — "
                    "the largest part of exhaled air has not been touched at "
                    "all."},
            {"text": "Most of it is untouched: nitrogen is unchanged and most "
                     "of the oxygen is still there.",
             "correct": True},
            {"text": "It is wrong because exhaled air is mostly carbon "
                     "dioxide, which is a new gas rather than a used one.",
             "correct": False,
             "why": "Exhaled air is not mostly carbon dioxide — it is 4%. That "
                    "is behind the nitrogen and behind the oxygen, whatever "
                    "you call it."},
            {"text": "It is wrong because the body puts the oxygen back "
                     "before the air leaves.",
             "correct": False,
             "why": "Nothing is put back. The 16% of oxygen in exhaled air is "
                    "simply the oxygen that was never taken out on the way "
                    "through."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s09",
        "band": "standard",
        "text": "A student says that taking a deep breath brings in air with "
                "more oxygen in it than a shallow breath does. What is the "
                "best correction?",
        "options": [
            {"text": "A deep breath does bring in richer air, because it "
                     "reaches further down the airway than a shallow one.",
             "correct": False,
             "why": "The air is the same air wherever it reaches. How far down "
                    "it gets does not change what it is made of."},
            {"text": "A deep breath brings in poorer air, because the extra "
                     "air drawn in is already partly used.",
             "correct": False,
             "why": "There is no partly used air waiting outside you. Every "
                    "breath, deep or shallow, starts with room air at about "
                    "21% oxygen."},
            {"text": "It is right, but only outdoors, where the air is "
                     "richer in oxygen.",
             "correct": False,
             "why": "Ordinary indoor and outdoor air are both about 21% "
                    "oxygen. Neither the depth of the breath nor the room "
                    "changes the composition."},
            {"text": "The air is about 21% oxygen either way — a deep "
                     "breath brings in more of it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s10",
        "band": "standard",
        "text": "A student writes: “Gas exchange happens in the lungs and "
                "respiration happens in the alveoli.” Both halves need "
                "correcting. What should it say?",
        "options": [
            {"text": "Gas exchange happens in the alveoli, and respiration "
                     "happens in every cell of the body.",
             "correct": True},
            {"text": "Gas exchange happens in the alveoli, and respiration "
                     "happens in the blood as it passes them.",
             "correct": False,
             "why": "The first half is now right. The second still puts "
                    "respiration outside the cells — it is a reaction inside "
                    "cells, including the ones in your toes."},
            {"text": "Gas exchange happens all along the airway, and "
                     "respiration happens in the alveoli.",
             "correct": False,
             "why": "This makes the first half worse rather than better. No "
                    "exchange happens anywhere before the alveoli, and "
                    "respiration is not in the lungs at all."},
            {"text": "Nothing needs correcting, because the alveoli are in "
                     "the lungs anyway.",
             "correct": False,
             "why": "They are, which is what makes the sentence sound "
                    "reasonable. But it has put respiration in the lungs, and "
                    "respiration happens in every cell in your body."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s11",
        "band": "standard",
        "text": "Asked where the air is cleaned, a student answers “in the "
                "alveoli”. Where does the cleaning actually happen, and why "
                "does it matter that it happens there?",
        "options": [
            {"text": "In the bronchioles, because their muscle squeezes "
                     "particles out of the air.",
             "correct": False,
             "why": "Muscle in a bronchiole wall narrows the tube; it does not "
                    "filter anything. Cleaning is done by hairs, mucus and "
                    "cilia, and most of it happens much higher up."},
            {"text": "In the nose and the airway lining, before the air "
                     "reaches the exchange surface.",
             "correct": True},
            {"text": "In the alveoli, because that is where the air finally "
                     "stops moving.",
             "correct": False,
             "why": "An alveolus wall is one cell thick and has no way of "
                    "trapping anything. If cleaning waited until there, the "
                    "dirt would already be at the exchange surface."},
            {"text": "Nowhere — the air is not cleaned, only warmed and "
                     "moistened.",
             "correct": False,
             "why": "Filtering is one of the three things the nose and airway "
                    "do. Hairs and mucus trap particles, and cilia sweep the "
                    "mucus back up and away from the lungs."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b4-01-h05",
        "band": "harder",
        "text": "A baby is born and takes its first breath. Which of the "
                "three processes is starting at that moment, and which were "
                "already running?",
        "options": [
            {"text": "All three start at the first breath — none can happen "
                     "before birth.",
             "correct": False,
             "why": "Respiration cannot pause for nine months — the baby's "
                    "cells have been releasing energy from glucose the whole "
                    "time. Something must also have been supplying them with "
                    "oxygen."},
            {"text": "Breathing starts and gas exchange moves to the "
                     "alveoli; respiration was already running.",
             "correct": True},
            {"text": "Breathing and respiration both start at birth, while "
                     "gas exchange had been happening at the placenta.",
             "correct": False,
             "why": "Half right. The placenta was doing the gas exchange, but "
                    "respiration was running in every one of the baby's cells "
                    "long before the first breath."},
            {"text": "Gas exchange starts for the first time; breathing and "
                     "respiration had both been running since well before "
                     "birth.",
             "correct": False,
             "why": "Gas exchange was happening at the placenta before birth, "
                    "so it does not start — it moves. And you cannot breathe "
                    "before you have taken a breath."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h06",
        "band": "harder",
        "text": "In cystic fibrosis the mucus in the airways is unusually "
                "thick and sticky. Predict the problem this causes, given "
                "what normally happens to airway mucus.",
        "options": [
            {"text": "Dust would no longer be trapped, so particles would "
                     "reach the alveoli freely.",
             "correct": False,
             "why": "Thicker mucus traps particles at least as well as thin "
                    "mucus does. The trouble is not with the trapping — it is "
                    "with what happens next."},
            {"text": "No gas exchange could take place, because the mucus "
                     "would coat the alveoli.",
             "correct": False,
             "why": "The mucus lines the airway, not the exchange surface. The "
                    "problem it causes is one of clearing, which then makes "
                    "infections much more likely."},
            {"text": "The cilia could no longer sweep it away, so trapped "
                     "dust and bacteria would build up.",
             "correct": True},
            {"text": "The cartilage rings would soften, so the trachea would "
                     "collapse on every breath in.",
             "correct": False,
             "why": "Mucus has nothing to do with the cartilage. The rings "
                    "stay stiff, and the airway stays open — what fails is the "
                    "sweeping system that keeps it clean."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h07",
        "band": "harder",
        "text": "Someone takes 15 breaths a minute, each of 500 ml. Inhaled "
                "air is 21% oxygen and exhaled air is 16% oxygen. How much "
                "oxygen do they absorb per minute?",
        "options": [
            {"text": "375 ml", "correct": True},
            {"text": "1575 ml", "correct": False,
             "why": "That is 21% of all the air breathed in — the oxygen that "
                    "arrived, not the oxygen absorbed. You have to take off "
                    "the 16% that comes straight back out."},
            {"text": "1200 ml", "correct": False,
             "why": "That is 16% of the air moved, which is the oxygen leaving "
                    "in the exhaled breath. What the body took is the "
                    "difference between the two figures, not either one of "
                    "them."},
            {"text": "25 ml", "correct": False,
             "why": "That is one breath's worth: 5% of 500 ml. The question "
                    "asks for a minute, so it has to be multiplied by the 15 "
                    "breaths taken in that minute."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h08",
        "band": "harder",
        "text": "A submarine recycles its air. An engineer proposes removing "
                "the carbon dioxide the crew breathe out and pumping the same "
                "air round again. Why will that not be enough?",
        "options": [
            {"text": "It would work — taking the carbon dioxide back out "
                     "restores the recycled air to exactly what it was.",
             "correct": False,
             "why": "It restores one of the two changes. Every pass through a "
                    "crew member also takes about a quarter of the oxygen "
                    "away, and nothing puts that back."},
            {"text": "The nitrogen would run out first, because the crew "
                     "use up nitrogen as well as oxygen.",
             "correct": False,
             "why": "Nitrogen is 78% going in and 78% coming out. It is the "
                    "one gas the crew make no difference to at all."},
            {"text": "Each pass also drops oxygen from about 21% to 16%, so "
                     "oxygen must be added.",
             "correct": True},
            {"text": "Water vapour would build up until the air became "
                     "unbreathable.",
             "correct": False,
             "why": "Damp air is uncomfortable rather than unbreathable, and a "
                    "submarine dries its air anyway. The change that would "
                    "actually kill the crew is the falling oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h09",
        "band": "harder",
        "text": "Exhaled air is described as saturated with water vapour "
                "rather than being given a percentage. What does saturated "
                "mean here?",
        "options": [
            {"text": "That all of the water in the body has been given up "
                     "to the air that you breathe out each time.",
             "correct": False,
             "why": "You would not survive a single breath if that were true. "
                    "Saturated describes the air, not the body — and it is a "
                    "small amount of water each time."},
            {"text": "That the air holds as much water vapour as it can at "
                     "that temperature.",
             "correct": True},
            {"text": "That the water vapour has already turned into liquid "
                     "droplets inside the airways.",
             "correct": False,
             "why": "The water leaves as a vapour, which is why you cannot "
                    "usually see it. It only turns to liquid outside you, when "
                    "cold air cools it — that is visible breath."},
            {"text": "That water vapour is a fixed 6% of every breath out.",
             "correct": False,
             "why": "There is no fixed figure, and that is the reason for "
                    "using the word instead of a number. Warm air can hold "
                    "much more water vapour than cold air can."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h10",
        "band": "harder",
        "text": "Several people are shut in a small sealed room. Comparing "
                "each gas with the amount that was there to begin with, which "
                "changes by far the greater factor, and why?",
        "options": [
            {"text": "The nitrogen, because it is by far the biggest part "
                     "of the air.",
             "correct": False,
             "why": "Being the largest part is not the same as changing the "
                    "most. Nitrogen goes in at 78% and comes out at 78% — of "
                    "the three, it is the one that does not change at all."},
            {"text": "The oxygen, because it is the only one of the three "
                     "gases the body actually removes.",
             "correct": False,
             "why": "Oxygen is taken out, but only about a quarter of it each "
                    "pass — 21% down to 16%. That is a much smaller factor "
                    "than the carbon dioxide's change."},
            {"text": "Neither: both change by the same amount, because each "
                     "oxygen used is replaced by a carbon dioxide.",
             "correct": False,
             "why": "The oxygen falls by about 5 parts in a hundred and the "
                    "carbon dioxide rises by about 4, so the amounts are "
                    "similar — but the question asks about the factor, and the "
                    "carbon dioxide started at almost nothing."},
            {"text": "The carbon dioxide, which rises a hundredfold as "
                     "oxygen falls a quarter.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h11",
        "band": "harder",
        "text": "Nitrogen makes up 78% of the air and passes through you "
                "completely unchanged. Explain why an air supply made only of "
                "nitrogen would keep nobody alive.",
        "options": [
            {"text": "Nothing crosses into the blood from it, so no oxygen "
                     "would reach any cell.",
             "correct": True},
            {"text": "Nitrogen would fill the alveoli, so no gas could cross "
                     "them ever again.",
             "correct": False,
             "why": "Nitrogen already fills most of every alveolus, on every "
                    "breath you take, and oxygen crosses perfectly well "
                    "alongside it. The problem is that there would be no "
                    "oxygen there to cross."},
            {"text": "Nitrogen is poisonous in large amounts, which is why "
                     "the body refuses to absorb it.",
             "correct": False,
             "why": "It is not poisonous, and the body does not refuse it — it "
                    "simply has no way of using it. Nearly four fifths of "
                    "every breath you have ever taken was nitrogen."},
            {"text": "The lungs would not inflate, because nitrogen is too "
                     "heavy to move down the airway.",
             "correct": False,
             "why": "The lungs would inflate exactly as usual — air is mostly "
                    "nitrogen already. What would be missing is the one gas "
                    "that crosses into the blood."},
        ],
        "figure": None,
    },
    # ── easier ────────────────────────────────────────────────────────
    {
        "id": "b4-01-e12",
        "band": "easier",
        "text": "One part of the airway has muscle in its walls where the "
                "tubes above it have cartilage. Which part is it?",
        "options": [
            {"text": "The trachea, whose C-shaped rings are made of muscle "
                     "rather than cartilage.",
             "correct": False,
             "why": "The trachea's rings are cartilage — stiff, and "
                    "holding the tube permanently open. Muscle would let "
                    "it change width, which is the last thing the single "
                    "main airway needs to do."},
            {"text": "The bronchioles, the narrowest branches at the end "
                     "of the airway.",
             "correct": True},
            {"text": "The alveoli, whose walls squeeze to push the air "
                     "back out again.",
             "correct": False,
             "why": "An alveolus wall is one cell thick and contains no "
                    "muscle at all. Nothing about an alveolus squeezes; "
                    "the air is moved by machinery well outside the lungs."},
            {"text": "The bronchi, which are the widest tubes inside a "
                     "lung and so need the most support.",
             "correct": False,
             "why": "The bronchi are still ringed with cartilage, like the "
                    "trachea above them. The switch from cartilage to "
                    "muscle happens further down, at the bronchioles."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e13",
        "band": "easier",
        "text": "Where does the trachea run, and how many tubes is it?",
        "options": [
            {"text": "One tube, running down the front of the neck from "
                     "the throat towards the lungs.",
             "correct": True},
            {"text": "Two tubes, one running down each side of the neck "
                     "and into a lung of its own.",
             "correct": False,
             "why": "That describes the bronchi, which are what the "
                    "trachea divides into at its lower end. Above that "
                    "division there is only ever one tube."},
            {"text": "One tube, running down the back of the throat and on "
                     "towards the stomach.",
             "correct": False,
             "why": "The tube that carries food down to the stomach is the "
                    "oesophagus, and it sits behind the trachea. Air and "
                    "food take separate routes."},
            {"text": "A network of narrow branching tubes spread all "
                     "through both lungs.",
             "correct": False,
             "why": "That is the bronchioles, right at the far end of the "
                    "route. The trachea is the single wide tube the whole "
                    "network starts from."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e14",
        "band": "easier",
        "text": "Rings of cartilage hold parts of the airway open. Which "
                "parts carry them?",
        "options": [
            {"text": "The bronchioles and the alveoli, the two narrowest "
                     "parts of the route.",
             "correct": False,
             "why": "The bronchioles have muscle in their walls instead of "
                    "cartilage, and an alveolus has neither — its wall is "
                    "a single cell thick."},
            {"text": "Every part of the airway, from the nose all the way "
                     "down to the alveoli.",
             "correct": False,
             "why": "Cartilage stops well before the end. If it ran all "
                    "the way down, the alveolus wall could never be the "
                    "single cell that gas has to cross."},
            {"text": "The alveoli only, because they are the part where a "
                     "collapse would matter most.",
             "correct": False,
             "why": "Nothing in an alveolus is stiffened. The rings are on "
                    "the wide tubes higher up, where a collapse would shut "
                    "off the whole route."},
            {"text": "The trachea and the bronchi, the two widest tubes of "
                     "the route.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e15",
        "band": "easier",
        "text": "What are cilia, and which way do they sweep?",
        "options": [
            {"text": "Tiny hairs lining the airway, sweeping the mucus up "
                     "towards the throat.",
             "correct": True},
            {"text": "Tiny hairs lining the airway, sweeping mucus down "
                     "towards the alveoli.",
             "correct": False,
             "why": "Sweeping downwards would carry every trapped speck of "
                    "dust to the one surface in the body that has to stay "
                    "clear. Cilia beat the other way, away from the lungs."},
            {"text": "Rings of stiff cartilage that hold the trachea open "
                     "as air rushes down it.",
             "correct": False,
             "why": "That is the cartilage, and it does not move at all. "
                    "Cilia are hairs, and their whole job is movement."},
            {"text": "Tiny blood vessels that carry trapped dust away from "
                     "the airway in the blood.",
             "correct": False,
             "why": "Dust is never taken into the blood. It is trapped in "
                    "mucus on the surface of the airway and moved back out "
                    "along that surface."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e16",
        "band": "easier",
        "text": "The inside of the airway is lined with sticky mucus. What "
                "is the mucus there for?",
        "options": [
            {"text": "To dissolve oxygen out of the air so that the blood "
                     "can pick it up more easily.",
             "correct": False,
             "why": "Oxygen crosses into the blood at the alveoli, and the "
                    "mucus higher up plays no part in it. Mucus is there "
                    "to catch things, not to pass anything on."},
            {"text": "To make the tubes slippery so that air can travel "
                     "down them faster.",
             "correct": False,
             "why": "The airway is not trying to speed air up. Mucus is "
                    "sticky for a reason: anything that lands in it stops "
                    "there."},
            {"text": "To trap dust and bacteria in the airway before they "
                     "reach the alveoli.",
             "correct": True},
            {"text": "To keep the rings of cartilage soft enough to bend "
                     "as you turn your head.",
             "correct": False,
             "why": "Cartilage is already flexible on its own, and the "
                    "mucus lies on the inner surface of the tube rather "
                    "than in its wall."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e17",
        "band": "easier",
        "text": "How thick is the wall between the air inside an alveolus "
                "and the blood outside it?",
        "options": [
            {"text": "About a millimetre, thick enough to feel between "
                     "your fingers.",
             "correct": False,
             "why": "That is thousands of times too thick. A wall like "
                    "that would slow the crossing so much that the lungs "
                    "could not keep up with the body."},
            {"text": "One cell thick.",
             "correct": True},
            {"text": "Several layers of muscle thick, so that the sac can "
                     "squeeze the air out.",
             "correct": False,
             "why": "There is no muscle anywhere in an alveolus, and "
                    "nothing there squeezes. The thinness is the point: it "
                    "is what the gases have to cross."},
            {"text": "Thick enough to see with the naked eye, like the "
                     "skin on the back of your hand.",
             "correct": False,
             "why": "A single alveolus is far too small to see without a "
                    "microscope, let alone its wall. Thin is exactly what "
                    "it has to be."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e18",
        "band": "easier",
        "text": "Roughly what share of the air you breathe in is nitrogen?",
        "options": [
            {"text": "About 21%, the same share as the oxygen beside it.",
             "correct": False,
             "why": "21% is the oxygen figure. Nitrogen is nearly four "
                    "times that, and it is the largest thing in every "
                    "breath you have ever taken."},
            {"text": "About 4%, a little more than the carbon dioxide.",
             "correct": False,
             "why": "4% is the carbon dioxide figure for exhaled air. "
                    "Nitrogen is far and away the biggest share of the "
                    "bag, going in and coming out."},
            {"text": "Almost none of it, because air is very nearly all "
                     "oxygen.",
             "correct": False,
             "why": "Air is not mostly oxygen — oxygen is only about a "
                    "fifth of it. Most of what you take in and pass back "
                    "out is nitrogen."},
            {"text": "About 78%.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e19",
        "band": "easier",
        "text": "Which gas is the largest part of the air a person "
                "breathes out?",
        "options": [
            {"text": "Nitrogen, at about 78%, which is the same share it "
                     "had going in.",
             "correct": True},
            {"text": "Carbon dioxide, because that is the gas the body "
                     "makes and gets rid of.",
             "correct": False,
             "why": "Carbon dioxide is only about 4% of exhaled air — the "
                    "smallest of the four things listed here. It is the "
                    "gas that changes most, not the gas there is most of."},
            {"text": "Oxygen, because most of what goes in comes straight "
                     "back out again.",
             "correct": False,
             "why": "Most of the oxygen really does come back out, and 16% "
                    "makes it the second largest figure in the bag. "
                    "Nitrogen, at 78%, is far larger still."},
            {"text": "Water vapour, because exhaled air is saturated with "
                     "it.",
             "correct": False,
             "why": "Exhaled air is saturated, but saturated air still "
                    "holds only a few per cent water vapour. Nitrogen is "
                    "the bulk of the breath."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e20",
        "band": "easier",
        "text": "At an alveolus, which gas moves into the blood and which "
                "moves out of it?",
        "options": [
            {"text": "Carbon dioxide moves in, and oxygen moves out into "
                     "the air in the sac.",
             "correct": False,
             "why": "That is the right pair of gases going the wrong way. "
                    "Blood arriving at the lungs is short of oxygen and "
                    "loaded with carbon dioxide, and both are put right."},
            {"text": "Nitrogen moves in, and carbon dioxide moves out into "
                     "the air in the sac.",
             "correct": False,
             "why": "Nitrogen crosses nowhere: it goes in at 78% and comes "
                    "out at 78%. The gas moving into the blood is oxygen."},
            {"text": "Oxygen moves into the blood, and carbon dioxide "
                     "moves out of it.",
             "correct": True},
            {"text": "Both gases move into the blood, and the lungs get "
                     "rid of them together later on.",
             "correct": False,
             "why": "Carbon dioxide is already in the blood when it "
                    "arrives — it was made by the body's cells. The "
                    "alveolus is where it leaves, not where it is "
                    "collected."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e21",
        "band": "easier",
        "text": "Breathing is called a mechanical process rather than a "
                "chemical one. What does breathing itself involve?",
        "options": [
            {"text": "Releasing energy from glucose inside every cell of "
                     "the body.",
             "correct": False,
             "why": "That is respiration, and it is a chemical reaction. "
                    "It happens in cells in your toes as much as in your "
                    "chest."},
            {"text": "Moving air in and out of the lungs, using muscles "
                     "outside them.",
             "correct": True},
            {"text": "Swapping oxygen and carbon dioxide between the "
                     "alveoli and the blood.",
             "correct": False,
             "why": "That is gas exchange, which happens only at the "
                    "alveoli. Breathing is what delivers the air to them."},
            {"text": "Warming, moistening and filtering the air on its way "
                     "down the airway.",
             "correct": False,
             "why": "That is conditioning, done by the nose and the airway "
                    "lining. It changes the state of the air, not where "
                    "the air is."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e22",
        "band": "easier",
        "text": "Cilia sweep mucus up the airway until it reaches the top "
                "of the throat. What happens to it there?",
        "options": [
            {"text": "It passes into the blood, which carries the trapped "
                     "dust away to be broken down.",
             "correct": False,
             "why": "Nothing trapped in mucus enters the blood. Keeping it "
                    "out of the blood is the whole point of catching it on "
                    "a surface."},
            {"text": "It drips back down into the lungs as soon as the "
                     "cilia stop beating.",
             "correct": False,
             "why": "Cilia beat continuously, and the mucus travels one "
                    "way. It is a conveyor belt running steadily away from "
                    "the lungs."},
            {"text": "It stays at the top of the airway permanently, which "
                     "is why the throat feels rough.",
             "correct": False,
             "why": "Mucus is made and cleared all the time. If it "
                    "collected at the throat and stayed there, the belt "
                    "would jam within a day."},
            {"text": "It is swallowed.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e23",
        "band": "easier",
        "text": "A breath of air has just travelled through the "
                "bronchioles. Which part does it reach next?",
        "options": [
            {"text": "The bronchi, which the bronchioles feed back into.",
             "correct": False,
             "why": "Air reaches the bronchi before the bronchioles, not "
                    "after. The route only ever gets narrower on the way "
                    "in."},
            {"text": "The trachea, on its way back up towards the throat.",
             "correct": False,
             "why": "The trachea is passed near the start of the journey "
                    "in. The question follows the air inwards, and the "
                    "bronchioles are almost at the end of that route."},
            {"text": "The alveoli.",
             "correct": True},
            {"text": "The capillaries, which the air flows straight into "
                     "from the bronchioles.",
             "correct": False,
             "why": "Air never flows into a blood vessel. It stops in the "
                    "air sacs, and only the gases cross the wall between "
                    "the sac and the blood."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e24",
        "band": "easier",
        "text": "What is an alveolus?",
        "options": [
            {"text": "A tiny air sac at the end of the airway, wrapped in "
                     "capillaries.",
             "correct": True},
            {"text": "A narrow tube with muscle in its wall, deep inside "
                     "the lung.",
             "correct": False,
             "why": "That is a bronchiole. It carries air towards the sacs "
                    "but nothing crosses into the blood along it."},
            {"text": "One of the two large air spaces that a lung is made "
                     "up of.",
             "correct": False,
             "why": "A lung is not made of two large spaces — it holds "
                    "around 500 million alveoli, which is why it feels "
                    "like a sponge rather than a bag."},
            {"text": "A ring of cartilage that holds the smallest airways "
                     "open.",
             "correct": False,
             "why": "The cartilage rings are on the trachea and bronchi, "
                    "and they are not sacs at all. An alveolus is a space "
                    "with a wall one cell thick."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e25",
        "band": "easier",
        "text": "Inhaled air is about 0.04% carbon dioxide. About what is "
                "the figure for exhaled air?",
        "options": [
            {"text": "About 0.04% — unchanged, in the same way the "
                     "nitrogen figure is unchanged.",
             "correct": False,
             "why": "Nitrogen is the gas that comes back unchanged. Carbon "
                    "dioxide is the one that changes most of all, rising a "
                    "hundredfold."},
            {"text": "About 4%.",
             "correct": True},
            {"text": "About 40%, a thousand times what went in.",
             "correct": False,
             "why": "The rise is a hundredfold, not a thousandfold, and "
                    "40% would leave almost no room for the nitrogen that "
                    "actually fills most of the bag."},
            {"text": "About 96%, with the last few per cent being leftover "
                     "oxygen.",
             "correct": False,
             "why": "This is the bagful-of-carbon-dioxide picture, and the "
                    "figures kill it: exhaled air is still 78% nitrogen "
                    "and 16% oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e26",
        "band": "easier",
        "text": "Mouth-to-mouth resuscitation keeps a casualty alive on "
                "air that has already been through the rescuer's lungs. "
                "Which fact about exhaled air explains why it works?",
        "options": [
            {"text": "The rescuer's lungs add fresh oxygen before the air "
                     "is breathed out.",
             "correct": False,
             "why": "Nothing in the body adds oxygen to air. The rescuer's "
                    "lungs take some out — the point is how much is left."},
            {"text": "It carries no oxygen, but its carbon dioxide can be "
                     "used in an emergency.",
             "correct": False,
             "why": "Carbon dioxide is a waste gas and no cell can use it. "
                    "What keeps the casualty alive is the oxygen still in "
                    "the bag."},
            {"text": "Exhaled air is warm, and warmth is what a casualty "
                     "needs most.",
             "correct": False,
             "why": "The air is warmer, but warmth is not what is being "
                    "delivered. The casualty needs oxygen, and exhaled air "
                    "still has plenty."},
            {"text": "It still contains about 16% oxygen, which is most of "
                     "the 21% that went in.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e27",
        "band": "easier",
        "text": "Put these three tubes in order of width, widest first: "
                "bronchiole, bronchus, trachea.",
        "options": [
            {"text": "Bronchiole, bronchus, trachea.",
             "correct": False,
             "why": "These are the right three tubes in the wrong "
                    "direction. The trachea is the single widest tube and "
                    "the bronchioles are the narrowest branches at the far "
                    "end."},
            {"text": "Bronchus, trachea, bronchiole.",
             "correct": False,
             "why": "The bronchi are what the trachea divides into, so "
                    "they must be narrower than it, never wider."},
            {"text": "Trachea, bronchus, bronchiole.",
             "correct": True},
            {"text": "Trachea, bronchiole, bronchus.",
             "correct": False,
             "why": "The trachea is right in first place, but the last two "
                    "are swapped: a bronchus divides many times over "
                    "before the tubes become bronchioles."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e28",
        "band": "easier",
        "text": "Two things inside the nose filter the air on its way in. "
                "What are they?",
        "options": [
            {"text": "Hairs, and a coating of sticky mucus.",
             "correct": True},
            {"text": "Cilia and rings of cartilage.",
             "correct": False,
             "why": "Cilia do move trapped dust, but they are lower down "
                    "and they move what the mucus has already caught. "
                    "Cartilage holds tubes open and traps nothing."},
            {"text": "A network of capillaries and a layer of muscle.",
             "correct": False,
             "why": "Capillaries in the nose help warm the air rather than "
                    "clean it, and there is no filtering muscle anywhere "
                    "in the airway."},
            {"text": "The bones of the skull and a lining of thin dry "
                     "skin.",
             "correct": False,
             "why": "The lining of the nose is wet, not dry — that is what "
                    "lets it hold on to dust. Bone gives the nose its "
                    "shape and does no filtering."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e29",
        "band": "easier",
        "text": "Of the two main gases in the air you breathe in, which "
                "does your body take and use, and which passes straight "
                "through?",
        "options": [
            {"text": "Nitrogen is taken and used; oxygen passes straight "
                     "through.",
             "correct": False,
             "why": "This has the two gases the wrong way round. The "
                    "nitrogen figure is 78% in and 78% out, which is what "
                    "passing straight through looks like."},
            {"text": "Oxygen is taken and used; nitrogen passes straight "
                     "through.",
             "correct": True},
            {"text": "Both are taken and used, which is why both of their "
                     "figures fall between the two bags.",
             "correct": False,
             "why": "Only one figure falls. Oxygen drops from 21% to 16%, "
                    "while nitrogen is 78% in both bags."},
            {"text": "Neither is used: the body only ever adds carbon "
                     "dioxide to the air passing through.",
             "correct": False,
             "why": "Carbon dioxide is added, but oxygen is genuinely "
                    "taken as well — about a quarter of what goes in stays "
                    "behind."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e30",
        "band": "easier",
        "text": "Oxygen goes in at 21% and comes out at 16%. Roughly how "
                "much of the oxygen you breathe in do you keep?",
        "options": [
            {"text": "About three quarters of it, leaving only a little to "
                     "come back out.",
             "correct": False,
             "why": "That is the wrong way round: about three quarters "
                    "comes back out, and it is the quarter you keep that "
                    "does the work."},
            {"text": "All of it, which is why exhaled air contains no "
                     "oxygen.",
             "correct": False,
             "why": "Exhaled air is 16% oxygen — most of what went in. If "
                    "none came back out, mouth-to-mouth resuscitation "
                    "could not work."},
            {"text": "About a twentieth of it, which is where the 4% "
                     "carbon dioxide comes from.",
             "correct": False,
             "why": "The oxygen figure falls by 5 percentage points out of "
                    "21, which is about a quarter of it, not a twentieth."},
            {"text": "About a quarter of it, with the rest coming straight "
                     "back out.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e31",
        "band": "easier",
        "text": "Breathing, gas exchange and respiration are three "
                "different things. Which of them happens inside every cell "
                "of the body?",
        "options": [
            {"text": "Gas exchange, which is the reason the lungs are "
                     "needed at all.",
             "correct": False,
             "why": "Gas exchange happens in one place only — the alveoli. "
                    "It is what supplies the cells rather than what "
                    "happens inside them."},
            {"text": "Breathing, because every cell in the body needs air "
                     "brought to it.",
             "correct": False,
             "why": "Breathing is muscles moving air in and out of the "
                    "lungs. Air never reaches a cell; dissolved oxygen "
                    "does, carried in the blood."},
            {"text": "Respiration.",
             "correct": True},
            {"text": "Gas exchange and respiration together, since both of "
                     "them involve oxygen.",
             "correct": False,
             "why": "Both involve oxygen, but only one of them is inside a "
                    "cell. Gas exchange stays at the alveoli."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-e32",
        "band": "easier",
        "text": "Sort the airway into the tubes that transport air and the "
                "surface where gas is exchanged. Which grouping is right?",
        "options": [
            {"text": "Trachea, bronchi and bronchioles transport; the "
                     "alveoli exchange.",
             "correct": True},
            {"text": "Trachea and bronchi transport; the bronchioles and "
                     "alveoli both exchange.",
             "correct": False,
             "why": "The bronchioles are transport tubes like the ones "
                    "above them — narrower, and walled with muscle, but "
                    "still carrying air rather than exchanging it."},
            {"text": "The nose transports, and every part below it "
                     "exchanges a little.",
             "correct": False,
             "why": "This is the commonest version of the mistake. "
                    "Exchange happens at one place only, and every tube "
                    "before it is moving or conditioning the air."},
            {"text": "The alveoli transport air on to the bronchioles, "
                     "which are where it is exchanged.",
             "correct": False,
             "why": "This reverses the route as well as the jobs. The "
                    "alveoli are the end of the road, not a stage on the "
                    "way to one."},
        ],
        "figure": None,
    },
    # ── standard ──────────────────────────────────────────────────────
    {
        "id": "b4-01-s12",
        "band": "standard",
        "text": "A sample of air taken from inside the trachea during a "
                "breath in has the same composition as the air in the "
                "room. Explain why.",
        "options": [
            {"text": "The trachea replaces any oxygen that has already "
                     "been taken, so the sample looks untouched.",
             "correct": False,
             "why": "Nothing in the body puts oxygen back into air. The "
                    "sample is unchanged because nothing has been removed "
                    "from it yet."},
            {"text": "Some exchange has happened, but far too little of it "
                     "to show up on the equipment used.",
             "correct": False,
             "why": "It is not a matter of the amount being small. No "
                    "oxygen at all crosses into the blood anywhere above "
                    "the alveoli."},
            {"text": "No gas has crossed into the blood yet: the trachea "
                     "is a transport tube, not an exchange surface.",
             "correct": True},
            {"text": "The air has already been to the alveoli and back, "
                     "arriving at the trachea at 21% oxygen again.",
             "correct": False,
             "why": "Air that has been to the alveoli comes back at 16% "
                    "oxygen, not 21%. On a breath in, this air has not "
                    "been anywhere yet."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s13",
        "band": "standard",
        "text": "Air enters the nose at room temperature and leaves the "
                "mouth at body temperature. Explain what has warmed it.",
        "options": [
            {"text": "Respiration in the alveoli, which releases its heat "
                     "straight into the air in the sacs.",
             "correct": False,
             "why": "Respiration happens inside cells all over the body, "
                    "not in the air. The air is warmed by touching a warm "
                    "surface, not by a reaction happening in it."},
            {"text": "Friction, as the air rushes down the narrow tubes of "
                     "the airway.",
             "correct": False,
             "why": "Quiet breathing moves air slowly and gently. The "
                    "warming happens just as much on a slow breath as on a "
                    "fast one, which rules friction out."},
            {"text": "The carbon dioxide added to it on the way, which is "
                     "a warmer gas than the oxygen it replaces.",
             "correct": False,
             "why": "A gas does not carry a temperature of its own into a "
                    "mixture, and the carbon dioxide added is only about "
                    "4% of the breath in any case."},
            {"text": "The warm, wet lining of the nose and airway, which "
                     "the air is touching the whole way down.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s14",
        "band": "standard",
        "text": "Oxygen from a hospital cylinder is completely dry, and it "
                "is bubbled through water before a patient breathes it. "
                "Suggest why.",
        "options": [
            {"text": "It does the moistening the nose would normally do, "
                     "so the airway lining does not dry out.",
             "correct": True},
            {"text": "Water is needed before oxygen will dissolve into the "
                     "blood at the alveoli.",
             "correct": False,
             "why": "The alveoli have their own moist lining and supply "
                    "that themselves. The water is added for the tubes the "
                    "gas travels through, not for the crossing at the end."},
            {"text": "Bubbling it through water puts back the carbon "
                     "dioxide the patient still needs to breathe in.",
             "correct": False,
             "why": "Water does not add carbon dioxide, and a patient "
                    "needs none breathed in — carbon dioxide is a waste "
                    "gas made by their own cells."},
            {"text": "Wet air carries more oxygen than dry air, so each "
                     "breath delivers a larger dose.",
             "correct": False,
             "why": "Adding water vapour to a gas does not increase its "
                    "oxygen. If anything the water takes up room the "
                    "oxygen would otherwise fill."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s15",
        "band": "standard",
        "text": "Two joiners work all day in the same dusty workshop. One "
                "breathes through the nose and the other through the "
                "mouth. Predict the difference, and give the reason.",
        "options": [
            {"text": "The nose breather takes in more, because dust "
                     "settles in the nose and is drawn down later.",
             "correct": False,
             "why": "Dust caught in the nose is held in mucus and moved "
                    "back out, not released later. Catching it there is "
                    "what keeps it out of the lungs."},
            {"text": "The mouth breather takes in more dust, because the "
                     "nose's hairs and mucus filter it out.",
             "correct": True},
            {"text": "There is no difference, because the trachea does all "
                     "the filtering below both routes anyway.",
             "correct": False,
             "why": "The trachea does trap dust in its mucus, but it is "
                    "the second line rather than the first. Air through "
                    "the mouth arrives at it dirtier."},
            {"text": "The mouth breather takes in less, because the mouth "
                     "is a wider opening and dust falls out of slow air.",
             "correct": False,
             "why": "A wider opening filters less, not more. Nothing about "
                    "the mouth traps particles the way nose hairs and "
                    "mucus do."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s16",
        "band": "standard",
        "text": "A student writes that nitrogen goes into your lungs and "
                "stays inside your body. Use the two nitrogen figures to "
                "correct them.",
        "options": [
            {"text": "It goes in at 78% and comes out at 16%, so most of "
                     "it really does stay behind.",
             "correct": False,
             "why": "16% is the oxygen figure for exhaled air. Nitrogen "
                    "reads 78% in both bags."},
            {"text": "The figures cannot settle it, because a percentage "
                     "says nothing about how much gas there is.",
             "correct": False,
             "why": "Both bags hold the same volume of air, so the same "
                    "percentage means the same amount. That is exactly why "
                    "the comparison works."},
            {"text": "It goes in at 78% and comes out at 78%, so "
                     "essentially all of it comes straight back out.",
             "correct": True},
            {"text": "The student is right, and the figure is rounded to "
                     "78% because the amount absorbed is small.",
             "correct": False,
             "why": "There is no slow absorption hiding in the rounding. "
                    "Your body has no way of taking nitrogen out of air at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s17",
        "band": "standard",
        "text": "The trachea is ringed with cartilage while the "
                "bronchioles have muscle instead. Explain why the two need "
                "different walls.",
        "options": [
            {"text": "Cartilage is simply stronger than muscle, and only a "
                     "tube as wide as the trachea is able to carry rings "
                     "of it.",
             "correct": False,
             "why": "Width is not the reason — the bronchi are narrower "
                    "than the trachea and are ringed too. The question is "
                    "whether a tube needs to change width or never to "
                    "close."},
            {"text": "The bronchioles are where gas exchange happens, and "
                     "rings of cartilage would get in its way.",
             "correct": False,
             "why": "No exchange happens in a bronchiole; it is a "
                    "transport tube like the ones above it. Exchange "
                    "begins only at the alveoli."},
            {"text": "Cartilage wears out in narrow tubes, so the body "
                     "switches to muscle wherever a tube is small.",
             "correct": False,
             "why": "Cartilage does not wear out with use, and the switch "
                    "is not about durability. It is about what each tube "
                    "has to be able to do."},
            {"text": "The trachea is the one route for all the air and "
                     "must never close, while muscle lets bronchioles "
                     "change width.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s18",
        "band": "standard",
        "text": "A student says the alveoli squeeze oxygen across into the "
                "blood. What is wrong with that picture?",
        "options": [
            {"text": "Nothing in an alveolus moves: the gases cross a wall "
                     "one cell thick on their own.",
             "correct": True},
            {"text": "It is the capillaries that squeeze, pushing the "
                     "oxygen out of the air and into the blood.",
             "correct": False,
             "why": "A capillary wall is one cell thick as well, and it "
                    "does no pushing. The gases move without anything "
                    "driving them across."},
            {"text": "The alveoli do squeeze, but only during exercise, "
                     "when much more oxygen is needed each minute.",
             "correct": False,
             "why": "Exercise changes how fast air is moved in and out, "
                    "not what an alveolus does. An alveolus has no muscle "
                    "to squeeze with at any time."},
            {"text": "The squeezing happens in the bronchioles, and the "
                     "alveoli only store the air until it is needed.",
             "correct": False,
             "why": "Bronchiole muscle changes the width of a tube; it "
                    "never drives gas across a wall. And the alveoli are "
                    "the exchange surface, not a store."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s19",
        "band": "standard",
        "text": "A breath in is 500 ml of air, and inhaled air is 21% "
                "oxygen. Calculate the volume of oxygen taken in with that "
                "breath.",
        "options": [
            {"text": "21 ml",
             "correct": False,
             "why": "This treats the 21 as a volume rather than as a "
                    "percentage. The percentage has to be taken of the 500 "
                    "ml: 500 × 0.21 = 105 ml."},
            {"text": "105 ml",
             "correct": True},
            {"text": "1050 ml",
             "correct": False,
             "why": "This is ten times too large, and larger than the "
                    "breath itself. A power of ten has slipped: 500 × 0.21 "
                    "= 105 ml."},
            {"text": "395 ml",
             "correct": False,
             "why": "This is 500 − 105, the volume of everything that is "
                    "not oxygen. The question asks for the oxygen itself."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s20",
        "band": "standard",
        "text": "Exhaled air is about 4% carbon dioxide, and a breath out "
                "is 500 ml. Calculate the volume of carbon dioxide in it.",
        "options": [
            {"text": "4 ml",
             "correct": False,
             "why": "This reads the 4 as a volume instead of a percentage. "
                    "Four per cent of 500 ml is 500 × 0.04 = 20 ml."},
            {"text": "125 ml",
             "correct": False,
             "why": "This divides 500 by 4 rather than taking 4% of it. "
                    "Dividing by 4 would be finding a quarter, which is "
                    "25%, not 4%."},
            {"text": "20 ml",
             "correct": True},
            {"text": "200 ml",
             "correct": False,
             "why": "This is 40% of the breath, not 4%. The decimal point "
                    "has moved one place."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s21",
        "band": "standard",
        "text": "A student believes the air inside an alveolus is pure "
                "oxygen by the time it gets there. Explain what is "
                "actually in it.",
        "options": [
            {"text": "Pure oxygen, because the airway strips out the other "
                     "gases on the way down.",
             "correct": False,
             "why": "The airway removes nothing from the air except dust. "
                    "Air arrives at the alveoli with the same gases it "
                    "started with."},
            {"text": "Pure carbon dioxide, because the blood has already "
                     "unloaded its carbon dioxide there.",
             "correct": False,
             "why": "Carbon dioxide does arrive from the blood, but it "
                    "only ever reaches about 4% of the air in the sac."},
            {"text": "Nothing at all until the blood arrives, because an "
                     "alveolus is empty between breaths.",
             "correct": False,
             "why": "An alveolus never empties. Air stays in it between "
                    "breaths, which is why fresh air mixes with air "
                    "already there."},
            {"text": "Mostly nitrogen, as every breath is, with some "
                     "oxygen and a little carbon dioxide.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s22",
        "band": "standard",
        "text": "You breathe out about a hundred times more carbon dioxide "
                "than you breathe in. Where in the body was it made, and "
                "how did it reach the alveoli?",
        "options": [
            {"text": "In respiring cells all over the body; the blood "
                     "carried it to the alveoli.",
             "correct": True},
            {"text": "In the alveoli, where oxygen is turned into carbon "
                     "dioxide as it crosses the wall.",
             "correct": False,
             "why": "Nothing is turned into anything at an alveolus. "
                    "Oxygen crosses one way and carbon dioxide crosses the "
                    "other, unchanged."},
            {"text": "In the lungs, which manufacture it from the air that "
                     "arrives there each breath.",
             "correct": False,
             "why": "Lungs make no gases. They are the place where a gas "
                    "made elsewhere in the body finally leaves it."},
            {"text": "In the stomach, from food, and it travels up the "
                     "oesophagus into the airway.",
             "correct": False,
             "why": "Food and air take separate tubes, and the carbon "
                    "dioxide you breathe out has come through the blood "
                    "rather than up the gullet."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s23",
        "band": "standard",
        "text": "A patient has one whole lung removed. Predict the effect "
                "on their total gas exchange surface, and whether they can "
                "still exchange gases.",
        "options": [
            {"text": "Gas exchange stops altogether, because both lungs "
                     "are needed for the two gases to cross over.",
             "correct": False,
             "why": "Each alveolus does the whole job on its own — oxygen "
                    "in, carbon dioxide out. Half as many of them is "
                    "fewer, not incapable."},
            {"text": "The surface is roughly halved, but exchange carries "
                     "on: one lung still holds millions of alveoli.",
             "correct": True},
            {"text": "The surface is unchanged, because the trachea and "
                     "the bronchi are both left exactly as they were.",
             "correct": False,
             "why": "The exchange surface is the alveoli, not the tubes "
                    "that lead to them. Taking a lung away takes about "
                    "half of those sacs with it."},
            {"text": "The remaining lung at once grows enough new alveoli "
                     "to replace every single one that was lost.",
             "correct": False,
             "why": "A lung cannot rebuild half an exchange surface on "
                    "demand. The patient manages because one lung's "
                    "surface is still very large."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s24",
        "band": "standard",
        "text": "Sample A is 78% nitrogen, 21% oxygen and 0.04% carbon "
                "dioxide. Sample B is 78% nitrogen, 16% oxygen and 4% "
                "carbon dioxide. Which sample was breathed out, and which "
                "figures decide it?",
        "options": [
            {"text": "Sample A, because its carbon dioxide figure is the "
                     "lower of the two.",
             "correct": False,
             "why": "A low carbon dioxide reading is the mark of air that "
                    "has not been in anyone. Breathing out raises that "
                    "figure a hundredfold."},
            {"text": "Sample B, because its nitrogen has changed while "
                     "sample A's nitrogen has not.",
             "correct": False,
             "why": "Both samples read 78% nitrogen — that gas is the one "
                    "thing breathing leaves alone. It is the oxygen and "
                    "carbon dioxide that give the answer."},
            {"text": "Sample B: its oxygen has fallen and its carbon "
                     "dioxide has risen.",
             "correct": True},
            {"text": "It cannot be decided, because the two samples share "
                     "the same nitrogen figure.",
             "correct": False,
             "why": "The shared figure is the uninformative one. Two of "
                    "the three gases differ, and both differ in the "
                    "direction that breathing predicts."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s25",
        "band": "standard",
        "text": "A student says the nose cleans the air completely, so "
                "nothing dirty ever gets past it. Evaluate that claim.",
        "options": [
            {"text": "It is correct, and it is why the alveoli need no "
                     "cleaning system of their own.",
             "correct": False,
             "why": "The alveoli have no cleaning system, which is true, "
                    "but that is a weakness rather than a sign that "
                    "everything upstream has been caught."},
            {"text": "It is far too weak: the nose removes nothing, and "
                     "all the cleaning is done lower down the airway.",
             "correct": False,
             "why": "The nose's hairs and mucus do a great deal, which is "
                    "why mouth breathing in a dusty place is worse for "
                    "you."},
            {"text": "It cannot be judged either way, because there is no "
                     "means of telling how clean the air is.",
             "correct": False,
             "why": "The evidence is in the airway itself: mucus and cilia "
                    "lining the trachea and bronchi are there because "
                    "particles get past the nose."},
            {"text": "It is too strong: the nose removes a lot, which is "
                     "why the trachea and bronchi still carry mucus and "
                     "cilia.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s26",
        "band": "standard",
        "text": "Exhaled air is saturated with water vapour even when the "
                "air breathed in was dry. Where has that water come from?",
        "options": [
            {"text": "From the moist lining of the airway and alveoli, "
                     "from which water evaporates into the passing air.",
             "correct": True},
            {"text": "From the blood, which releases liquid water directly "
                     "into each alveolus.",
             "correct": False,
             "why": "Blood does not empty water into the air sacs — they "
                    "would fill up. The lining is already wet, and water "
                    "leaves it as vapour."},
            {"text": "From respiration, which happens inside the alveoli "
                     "and is the only place water is ever made.",
             "correct": False,
             "why": "Respiration does make water, but it happens in cells "
                    "all over the body rather than in the alveoli."},
            {"text": "From the oxygen taken out of the air, which turns "
                     "into water as it crosses the wall.",
             "correct": False,
             "why": "Oxygen crosses the wall unchanged and is still oxygen "
                    "on the other side. Nothing is converted at the "
                    "exchange surface."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s27",
        "band": "standard",
        "text": "Trace one molecule of oxygen from the air outside to the "
                "blood. Which list of parts does it pass through?",
        "options": [
            {"text": "Nose, trachea, bronchiole, bronchus, alveolus, then "
                     "across into a capillary.",
             "correct": False,
             "why": "The two branching tubes are the wrong way round. A "
                    "bronchus divides into bronchioles, so the wide one "
                    "comes first."},
            {"text": "Nose, trachea, bronchus, bronchiole, alveolus, then "
                     "across into a capillary.",
             "correct": True},
            {"text": "Nose, trachea, bronchus, bronchiole, then straight "
                     "into a capillary in the bronchiole wall.",
             "correct": False,
             "why": "This stops one stage short. Nothing crosses into the "
                    "blood from a bronchiole; the molecule has to reach an "
                    "alveolus first."},
            {"text": "Mouth, oesophagus, stomach, then across into the "
                     "blood along with the food.",
             "correct": False,
             "why": "That is the route food takes. Oxygen is not absorbed "
                    "from the gut, and the oesophagus carries no air to "
                    "the lungs."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s28",
        "band": "standard",
        "text": "A pupil's notes say the air is cleaned in the trachea and "
                "warmed in the alveoli. Which two corrections does that "
                "need?",
        "options": [
            {"text": "Cleaning happens only in the alveoli, and warming "
                     "happens only in the trachea.",
             "correct": False,
             "why": "This swaps the two claims round rather than "
                    "correcting them. The alveoli neither clean nor warm — "
                    "both jobs are finished before the air arrives."},
            {"text": "The cleaning claim is right, and warming happens in "
                     "the blood once the oxygen has crossed.",
             "correct": False,
             "why": "Cleaning starts in the nose, above the trachea. And "
                    "the air is warmed by the airway lining rather than by "
                    "anything happening in the blood."},
            {"text": "Cleaning starts in the nose and continues along the "
                     "airway, and warming happens before the alveoli "
                     "rather than at them.",
             "correct": True},
            {"text": "The warming claim is right, and cleaning happens in "
                     "the bronchioles, where the muscle squeezes particles "
                     "out.",
             "correct": False,
             "why": "Bronchiole muscle changes the width of a tube and "
                    "traps nothing, and the alveoli are not where air is "
                    "warmed."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s29",
        "band": "standard",
        "text": "Compare what happens to a dust particle that lands in the "
                "trachea with one that reaches an alveolus.",
        "options": [
            {"text": "Both are caught in mucus and swept back up, because "
                     "the whole airway is lined the same way.",
             "correct": False,
             "why": "The lining changes at the end of the route. Alveoli "
                    "have no cilia and no mucus belt — they are a bare "
                    "exchange surface."},
            {"text": "The one in the trachea passes into the blood, and "
                     "the one in an alveolus is coughed back out.",
             "correct": False,
             "why": "This has both fates backwards. Nothing crosses into "
                    "the blood from the trachea, and a particle in an "
                    "alveolus is past the reach of a cough."},
            {"text": "Neither can settle for long, because the moving air "
                     "blows both of them straight back out again on the "
                     "very next breath.",
             "correct": False,
             "why": "Mucus is sticky precisely so that particles do "
                    "settle. If air movement cleared the airway, there "
                    "would be no need for cilia."},
            {"text": "The one in the trachea is trapped in mucus and swept "
                     "back up, while the one in an alveolus has no cilia "
                     "to move it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s30",
        "band": "standard",
        "text": "A patient breathes pure oxygen through a sealed mask for "
                "several minutes. Predict what happens to the nitrogen "
                "figure in the air they breathe out.",
        "options": [
            {"text": "It falls towards zero, because no nitrogen is going "
                     "in for them to breathe back out.",
             "correct": True},
            {"text": "It stays at 78%, because the body always gives back "
                     "the nitrogen it is holding.",
             "correct": False,
             "why": "The body holds no store of nitrogen gas to give back. "
                    "The 78% in an ordinary breath out is simply the 78% "
                    "that went in."},
            {"text": "It rises above 78%, because taking the oxygen out "
                     "leaves the nitrogen more concentrated.",
             "correct": False,
             "why": "That effect is real when air is breathed, but it is "
                    "tiny, and here there is no nitrogen going in to "
                    "become concentrated."},
            {"text": "It stays at 78%, because nitrogen is produced in the "
                     "lungs as a waste gas.",
             "correct": False,
             "why": "The lungs make no gases at all. The only waste gas "
                    "leaving at the alveoli is carbon dioxide, made by "
                    "respiring cells."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s31",
        "band": "standard",
        "text": "Two students argue about whether the lungs and the gas "
                "exchange system mean the same thing. Who is right, and "
                "why?",
        "options": [
            {"text": "They are the same, because everything to do with "
                     "breathing happens inside the lungs.",
             "correct": False,
             "why": "The nose, the trachea and the bronchi all sit outside "
                    "the lungs, and every breath passes through them "
                    "first."},
            {"text": "They differ: the lungs are organs, and the system "
                     "also takes in the airway above them.",
             "correct": True},
            {"text": "They differ: the gas exchange system is only the "
                     "alveoli, and the lungs are everything else.",
             "correct": False,
             "why": "The alveoli are the exchange surface, but a system is "
                    "the organs working together — the tubes that deliver "
                    "the air belong to it too."},
            {"text": "They differ: the lungs are a tissue, and the gas "
                     "exchange system is the single organ built from it.",
             "correct": False,
             "why": "This has the levels of organisation inverted. A lung "
                    "is an organ, built from tissues, and several organs "
                    "together make the system."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-s32",
        "band": "standard",
        "text": "A pupil draws the trachea leading straight into one large "
                "air sac in each lung. Name the two things the drawing "
                "leaves out.",
        "options": [
            {"text": "The rings of cartilage, and the muscle that squeezes "
                     "each large sac empty again.",
             "correct": False,
             "why": "The rings are worth drawing, but a lung holds no "
                    "muscle of its own to squeeze with — so the second "
                    "half puts in something that is not there."},
            {"text": "The nose above the trachea, and the mucus that lines "
                     "the inside of the large sac.",
             "correct": False,
             "why": "The nose is a fair addition, but an exchange surface "
                    "lined with mucus would be a contradiction: mucus is "
                    "for the tubes, not the sacs."},
            {"text": "The branching into bronchi and bronchioles, and the "
                     "alveoli they end in.",
             "correct": True},
            {"text": "The capillaries wrapped around the sac, and the ribs "
                     "that would be drawn outside it.",
             "correct": False,
             "why": "Both are real, but neither is the structural point. "
                    "The drawing's mistake is the single hollow bag where "
                    "there should be branching ending in millions of sacs."},
        ],
        "figure": None,
    },
    # ── harder ────────────────────────────────────────────────────────
    {
        "id": "b4-01-h12",
        "band": "harder",
        "text": "The trachea and bronchi are lined with a moist membrane, "
                "just as the alveoli are. A student argues that gas "
                "exchange must therefore happen there too, only more "
                "slowly. Give the two reasons it does not.",
        "options": [
            {"text": "Their lining is moist but never warm enough, and the "
                     "air moves past it far too quickly to exchange "
                     "anything.",
             "correct": False,
             "why": "Air in the trachea is already close to body "
                    "temperature, and speed is not the obstacle. The "
                    "obstacles are the thickness of the wall and the "
                    "absence of capillaries against it."},
            {"text": "Their mucus seals the surface, and the rings of "
                     "cartilage around them block any gas from crossing.",
             "correct": False,
             "why": "Gases pass through mucus perfectly well, and the "
                    "rings are open C shapes with gaps between them. "
                    "Neither is what stops exchange."},
            {"text": "The air there is still 21% oxygen, and gas will only "
                     "cross once that figure has begun to fall.",
             "correct": False,
             "why": "This gets the direction backwards. A high oxygen "
                    "figure beside oxygen-poor blood is the best possible "
                    "condition for crossing — what is missing is somewhere "
                    "to cross to."},
            {"text": "Their walls are many cells thick, and no dense "
                     "network of capillaries is pressed against the "
                     "lining.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h13",
        "band": "harder",
        "text": "A student says gas exchange would work just as well if "
                "the blood beside the alveoli stood still, since the wall "
                "is thin either way. Evaluate that claim.",
        "options": [
            {"text": "It would soon stop: moving blood carries the oxygen "
                     "away, which is what keeps the difference across the "
                     "wall large.",
             "correct": True},
            {"text": "It would work just as well, because a thin wall is "
                     "the only thing oxygen needs in order to cross it.",
             "correct": False,
             "why": "A thin wall is necessary but not sufficient. Once the "
                    "standing blood filled up with oxygen, there would be "
                    "no difference left across the wall and crossing would "
                    "stop."},
            {"text": "It would work better than before, because standing "
                     "blood has longer beside the air to pick oxygen up.",
             "correct": False,
             "why": "Longer contact does not help once the blood is full. "
                    "What matters is that fresh, oxygen-poor blood keeps "
                    "arriving."},
            {"text": "It would stop at once, because it is the movement of "
                     "the blood that physically drags oxygen through the "
                     "wall.",
             "correct": False,
             "why": "Nothing drags the oxygen across — it moves on its "
                    "own. The flow matters because of what it takes away, "
                    "not because of any pull it exerts."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h14",
        "band": "harder",
        "text": "One person's alveoli give a total exchange surface of "
                "about 70 m², while their skin covers about 2 m². "
                "Determine how many times greater the alveolar surface is, "
                "and say why the body needs it.",
        "options": [
            {"text": "About 35 times greater, because the lungs must hold "
                     "35 times more air than the body has skin.",
             "correct": False,
             "why": "The arithmetic is right and the reason is not. "
                    "Surface area is not a volume of air: the point is how "
                    "much gas can cross at once."},
            {"text": "About 35 times greater, because how much gas can "
                     "cross depends on the area available.",
             "correct": True},
            {"text": "About 68 times greater, since the two areas are "
                     "subtracted to compare them.",
             "correct": False,
             "why": "Comparing how many times bigger means dividing, not "
                    "subtracting. 70 ÷ 2 = 35."},
            {"text": "About 140 times greater, because each of the two "
                     "lungs has a surface of 70 m² of its own.",
             "correct": False,
             "why": "The 70 m² figure is already the total for both lungs "
                    "together, so it must not be doubled."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h15",
        "band": "harder",
        "text": "An insect has no lungs. Air enters holes along its sides "
                "and travels down fine tubes that reach its tissues "
                "directly. Compare that with the human arrangement.",
        "options": [
            {"text": "The insect exchanges gases through its skin, while a "
                     "human exchanges them in the alveoli.",
             "correct": False,
             "why": "The insect's gases still cross at the end of a tube, "
                    "not through its outer surface. The real difference is "
                    "what the tubes deliver to."},
            {"text": "The insect's tubes are its alveoli, so both animals "
                     "exchange gases at the end of an airway.",
             "correct": False,
             "why": "The tubes end at the tissues themselves rather than "
                    "at a sac beside a blood vessel, which is the whole "
                    "point of the comparison."},
            {"text": "The insect's tubes take air to the cells themselves, "
                     "so no blood need carry it; a human exchanges at one "
                     "surface.",
             "correct": True},
            {"text": "Neither system relies on the gases moving on their "
                     "own: the insect pumps its air and the human pumps "
                     "its blood.",
             "correct": False,
             "why": "The gases move on their own in both animals. Pumping "
                    "brings the air or the blood close; the crossing "
                    "itself is never pumped."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h16",
        "band": "harder",
        "text": "A diver breathes a mixture that is 40% oxygen. If their "
                "body removes about a quarter of the oxygen in each "
                "breath, predict the oxygen percentage of the air they "
                "breathe out.",
        "options": [
            {"text": "About 10%, since a quarter of what went in is what "
                     "is left.",
             "correct": False,
             "why": "A quarter is removed, so three quarters remain. This "
                    "keeps the quarter and throws away the rest."},
            {"text": "About 16%, the same figure as for ordinary air.",
             "correct": False,
             "why": "16% is what is left of 21%. Start from 40% and three "
                    "quarters of it is 30%."},
            {"text": "About 35%, because the fall is always the 5 "
                     "percentage points seen with ordinary air.",
             "correct": False,
             "why": "The 5-point fall is a quarter of 21, not a fixed "
                    "amount. Take a quarter of 40 and the fall is 10 "
                    "points."},
            {"text": "About 30%.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h17",
        "band": "harder",
        "text": "Someone absorbs 300 ml of oxygen a minute. Each breath is "
                "500 ml, and 5% of a breath's volume is absorbed as "
                "oxygen. Determine how many breaths they take in a minute.",
        "options": [
            {"text": "12 breaths a minute",
             "correct": True},
            {"text": "25 breaths a minute",
             "correct": False,
             "why": "25 ml is the oxygen absorbed from one breath (500 × "
                    "0.05), not the number of breaths. Divide 300 by that "
                    "to get 12."},
            {"text": "60 breaths a minute",
             "correct": False,
             "why": "This divides 300 by 5, using the percentage as though "
                    "it were the volume per breath. The volume per breath "
                    "is 25 ml."},
            {"text": "6 breaths a minute",
             "correct": False,
             "why": "This divides 300 by 50, which is ten times the oxygen "
                    "each breath actually supplies."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h18",
        "band": "harder",
        "text": "A newborn baby has about 50 million alveoli and an adult "
                "about 500 million, while an adult's body mass is roughly "
                "twenty times a newborn's. Compare the two changes.",
        "options": [
            {"text": "The alveoli increase about twentyfold, exactly "
                     "keeping pace with the rise in body mass.",
             "correct": False,
             "why": "500 million is ten times 50 million, not twenty. The "
                    "two figures deliberately do not match."},
            {"text": "The alveoli increase about tenfold, so they do not "
                     "keep pace with body mass.",
             "correct": True},
            {"text": "The alveoli increase about 450 million times, "
                     "because the two numbers are subtracted.",
             "correct": False,
             "why": "Subtracting gives the extra number of alveoli, not "
                    "how many times more there are. For that, divide: 500 "
                    "÷ 50 = 10."},
            {"text": "The alveoli do not increase at all, because a baby "
                     "is born with every alveolus it will ever have and "
                     "each one simply grows larger.",
             "correct": False,
             "why": "The two figures in the question rule this out on "
                    "their own — 50 million becomes 500 million, so new "
                    "sacs are made after birth as well as bigger ones."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h19",
        "band": "harder",
        "text": "Of every 600 ml breath, about 150 ml stays in the airway "
                "and never reaches an alveolus. At 15 breaths a minute, "
                "calculate the volume of air that does reach the alveoli "
                "each minute.",
        "options": [
            {"text": "9000 ml",
             "correct": False,
             "why": "This is 600 × 15, the whole volume moved. It ignores "
                    "the 150 ml of each breath that stops in the tubes."},
            {"text": "2250 ml",
             "correct": False,
             "why": "This is 150 × 15, the air left behind in the airway "
                    "rather than the air that gets past it."},
            {"text": "6750 ml",
             "correct": True},
            {"text": "450 ml",
             "correct": False,
             "why": "This is the useful volume of a single breath (600 − "
                    "150). It still has to be multiplied by the 15 "
                    "breaths."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h20",
        "band": "harder",
        "text": "Two people each move 6 litres of air a minute. One takes "
                "12 breaths of 500 ml; the other takes 24 shallow breaths "
                "of 250 ml. About 150 ml of every breath stays in the "
                "airway for both. Determine which gets more air to their "
                "alveoli.",
        "options": [
            {"text": "The 250 ml breather, because more breaths a minute "
                     "means more chances for fresh air to arrive.",
             "correct": False,
             "why": "Each shallow breath wastes the same 150 ml, so taking "
                    "more of them multiplies the waste. Working it through "
                    "gives 2400 ml against 4200 ml."},
            {"text": "Neither: both reach 6000 ml, because the total "
                     "volume of air moved is the same for the two of them.",
             "correct": False,
             "why": "The totals moved are equal, which is exactly what "
                    "makes this worth asking. The 150 ml of dead space is "
                    "subtracted from every breath, so the number of "
                    "breaths decides it."},
            {"text": "The 250 ml breather, because only the extra 100 ml "
                     "of each of their breaths is wasted.",
             "correct": False,
             "why": "The waste is 150 ml of each breath, not 100 ml, and "
                    "it is the useful part that is left over: 250 − 150 = "
                    "100 ml per breath, which is the smaller share."},
            {"text": "The 500 ml breather, at 4200 ml a minute against "
                     "2400 ml.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h21",
        "band": "harder",
        "text": "Rescue breaths deliver air that is only 16% oxygen, while "
                "ordinary air is 21%. Explain how a casualty's blood can "
                "still gain oxygen from it.",
        "options": [
            {"text": "Their blood arrives at the alveoli with less oxygen "
                     "than that, so oxygen still crosses into the blood.",
             "correct": True},
            {"text": "The 16% figure climbs back to 21% inside the "
                     "casualty's airway before the air arrives at the "
                     "alveoli.",
             "correct": False,
             "why": "No part of the airway puts oxygen back into air. What "
                    "is in the breath when it goes in is what reaches the "
                    "sacs."},
            {"text": "The casualty's lungs work harder than usual to make "
                     "up the difference between 16% and 21%.",
             "correct": False,
             "why": "A casualty being given rescue breaths is not "
                    "breathing at all, and a lung cannot work harder in "
                    "any case — it contains no muscle."},
            {"text": "Oxygen always moves into blood whatever the amounts "
                     "on each side, because blood pulls it across the "
                     "wall.",
             "correct": False,
             "why": "Blood pulls nothing across. Oxygen moves from where "
                    "there is more of it to where there is less, and it "
                    "would not move at all if the blood already held more."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h22",
        "band": "harder",
        "text": "Carbon dioxide rises from 0.04% of inhaled air to 4% of "
                "exhaled air. State that rise as a ratio, and state what "
                "percentage of exhaled air is still something else.",
        "options": [
            {"text": "A rise of just 4 to 1, and 96% of the exhaled air is "
                     "something else.",
             "correct": False,
             "why": "The second figure is right but the ratio is not. 4 "
                    "divided by 0.04 is 100, not 4."},
            {"text": "A rise of 100 to 1, and 96% of the exhaled air is "
                     "something else.",
             "correct": True},
            {"text": "A rise of 100 to 1, and 4% of the exhaled air is "
                     "something else.",
             "correct": False,
             "why": "The ratio is right, but the last figure is the carbon "
                    "dioxide itself. Everything else is 100 − 4 = 96%."},
            {"text": "A rise of 400 to 1, and 60% of the exhaled air is "
                     "something else.",
             "correct": False,
             "why": "Neither number works. 4 ÷ 0.04 = 100, and what is "
                    "left of the bag is 96%, most of it nitrogen."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h23",
        "band": "harder",
        "text": "Air sampled at the mouth during a breath in is 21% "
                "oxygen, but air sampled from inside an alveolus is only "
                "about 14%. Suggest why the alveolar figure is lower.",
        "options": [
            {"text": "The airway takes the oxygen out of the air on the "
                     "way down, so the figure has already fallen before "
                     "the air arrives.",
             "correct": False,
             "why": "No oxygen crosses anywhere above the alveoli. Air "
                    "reaches them at the same 21% it started at."},
            {"text": "The measurement must be wrong, because alveolar air "
                     "stays at 21% until the blood takes some.",
             "correct": False,
             "why": "The blood is taking oxygen continuously, all day, so "
                    "there is no moment at which alveolar air sits "
                    "untouched at 21%."},
            {"text": "Fresh air does not replace alveolar air completely: "
                     "it mixes with air already there, which has been "
                     "giving up oxygen.",
             "correct": True},
            {"text": "The blood adds nitrogen to the alveoli, which "
                     "dilutes the oxygen down from 21%.",
             "correct": False,
             "why": "Nitrogen crosses in neither direction — it is the one "
                    "gas that is 78% in both bags."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h24",
        "band": "harder",
        "text": "A frog can exchange gases through its moist skin as well "
                "as through its lungs. Suggest why a human cannot rely on "
                "skin in the same way.",
        "options": [
            {"text": "Human skin has no blood supply, so there would be "
                     "nothing on the far side for the gases to cross into.",
             "correct": False,
             "why": "Skin is well supplied with blood — that is why it "
                    "flushes and why a cut bleeds. Its problem is that it "
                    "is dry, thick and small by comparison."},
            {"text": "Humans use far less oxygen than frogs do, so the "
                     "skin route was lost as it was never needed.",
             "correct": False,
             "why": "A human uses far more oxygen than a frog, being much "
                    "larger and much warmer. That is the reason a "
                    "dedicated exchange surface is needed."},
            {"text": "Gas can only ever cross a surface inside the body, "
                     "so no animal exchanges gases at its skin.",
             "correct": False,
             "why": "The frog in the question is doing exactly that, and "
                    "so do earthworms. Inside or outside is not what "
                    "decides it."},
            {"text": "Human skin is dry, thick, and tiny in area beside "
                     "the alveoli, so almost no gas can cross it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h25",
        "band": "harder",
        "text": "Air at the top of a high mountain is still 21% oxygen, "
                "yet climbers there are short of oxygen. Explain how both "
                "of those can be true.",
        "options": [
            {"text": "The air is thinner, so a breath of the same volume "
                     "holds fewer molecules of every gas in it.",
             "correct": True},
            {"text": "Percentages are measured differently at altitude, so "
                     "21% up there is not the same as 21% at sea level.",
             "correct": False,
             "why": "A percentage means the same thing everywhere. What "
                    "changes is how much gas there is in total for that "
                    "percentage to be a share of."},
            {"text": "The cold makes the alveoli work more slowly, so less "
                     "of the oxygen present is taken up.",
             "correct": False,
             "why": "Alveoli do no work and have no rate to slow down, and "
                    "the incoming air is warmed to body temperature before "
                    "it gets there."},
            {"text": "The oxygen at altitude is too spread out to travel "
                     "the length of the airway to the alveoli.",
             "correct": False,
             "why": "The air travels down as a whole and reaches the "
                    "alveoli perfectly well. There is simply less in it "
                    "when it arrives."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h26",
        "band": "harder",
        "text": "Put the stages of one carbon dioxide molecule's journey "
                "into order, from the muscle cell that made it to the air "
                "outside.",
        "options": [
            {"text": "Cell, alveolus, blood, bronchiole, bronchus, "
                     "trachea.",
             "correct": False,
             "why": "The blood is what carries the molecule from the cell "
                    "to the alveolus, so it cannot come after it."},
            {"text": "Cell, blood, alveolus, bronchiole, bronchus, "
                     "trachea.",
             "correct": True},
            {"text": "Cell, blood, trachea, bronchus, bronchiole, "
                     "alveolus.",
             "correct": False,
             "why": "This is the route in, run backwards. On the way out "
                    "the tubes widen: bronchiole, then bronchus, then "
                    "trachea."},
            {"text": "Cell, blood, alveolus, bronchus, bronchiole, "
                     "trachea.",
             "correct": False,
             "why": "The two branching tubes are swapped. An alveolus "
                    "opens into a bronchiole, and many bronchioles join to "
                    "make a bronchus."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h27",
        "band": "harder",
        "text": "Room air is bubbled through one tube of limewater and "
                "exhaled air through another, using the same volume of air "
                "in each. Predict the result and explain it.",
        "options": [
            {"text": "Only the exhaled tube changes, because ordinary room "
                     "air contains no carbon dioxide at all.",
             "correct": False,
             "why": "Room air is about 0.04% carbon dioxide, which is "
                    "small but not nothing. The difference between the "
                    "tubes is a matter of how much, not of all or none."},
            {"text": "Only the room air tube changes, because exhaled air "
                     "is mostly nitrogen and oxygen.",
             "correct": False,
             "why": "Exhaled air is mostly nitrogen and oxygen, but it "
                    "also holds a hundred times more carbon dioxide than "
                    "room air, so it is the tube that turns milky."},
            {"text": "The exhaled tube turns milky; the room tube hardly "
                     "changes, holding a hundred times less.",
             "correct": True},
            {"text": "Neither tube changes, because 4% is far too small a "
                     "share of the bag to be detected.",
             "correct": False,
             "why": "Limewater is a sensitive test and 4% is easily "
                    "enough. Being a small share of the bag does not make "
                    "a gas hard to detect."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h28",
        "band": "harder",
        "text": "In that limewater comparison, one variable has to be kept "
                "the same for the result to mean anything. Which, and why?",
        "options": [
            {"text": "The temperature of the limewater, because carbon "
                     "dioxide only turns it milky when it is warm.",
             "correct": False,
             "why": "Limewater goes milky at room temperature perfectly "
                    "well. Temperature is worth keeping steady, but it is "
                    "not what would wreck this comparison."},
            {"text": "The person doing the breathing, because different "
                     "people breathe out different gases.",
             "correct": False,
             "why": "Everyone breathes out the same gases, at close to the "
                    "same percentages. Who breathes is not the variable "
                    "that decides the result."},
            {"text": "The colour of the limewater at the start, because it "
                     "must be clear before any air is added.",
             "correct": False,
             "why": "Both tubes starting clear is a condition of the test "
                    "rather than a variable to be matched. What must match "
                    "is how much air goes through each."},
            {"text": "The volume of air through each tube, because more "
                     "air carries more carbon dioxide whatever its share.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h29",
        "band": "harder",
        "text": "A pupil tests exhaled air with dry cobalt chloride paper "
                "and it turns pink. Held in the room instead, the paper "
                "also turns pink, only far more slowly. Explain what that "
                "means for their conclusion.",
        "options": [
            {"text": "Room air already holds water vapour, so the claim "
                     "must be that exhaled air holds more, not that it "
                     "alone does.",
             "correct": True},
            {"text": "The paper is faulty, because it should only respond "
                     "to air that has been inside a person.",
             "correct": False,
             "why": "The paper is doing its job. It responds to water "
                    "vapour wherever the water vapour comes from, which is "
                    "what makes the room result meaningful."},
            {"text": "The room air must have come out of someone else's "
                     "lungs earlier in the day, so the two samples are "
                     "really the same.",
             "correct": False,
             "why": "Outdoor air holds water vapour too, on a day nobody "
                    "has breathed near it. Air does not need to have been "
                    "exhaled to be damp."},
            {"text": "It means nothing at all, because cobalt chloride "
                     "paper turns pink over time in any air whatever.",
             "correct": False,
             "why": "Speed is the whole of the evidence here. The paper "
                    "turns much faster in exhaled air, and that difference "
                    "is the result."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h30",
        "band": "harder",
        "text": "Air collected at the very start of a breath out is 21% "
                "oxygen, while air collected at the end of the same breath "
                "out is 16%. Suggest why the two differ.",
        "options": [
            {"text": "The equipment drifts during a measurement, so the "
                     "two figures are really one reading taken twice.",
             "correct": False,
             "why": "The difference is repeatable and has a cause. Two "
                    "readings 5 percentage points apart are not instrument "
                    "drift."},
            {"text": "The first air out is airway air that never reached "
                     "an alveolus, while the last has come from them.",
             "correct": True},
            {"text": "The first air out is alveolar air, and the last air "
                     "out is room air that followed the breath in.",
             "correct": False,
             "why": "This has the order reversed. The air nearest the "
                    "mouth leaves first, and that is the air that never "
                    "got as far as a sac."},
            {"text": "Oxygen is added to the air as the breath out goes "
                     "on, which is why the early figure is the higher one.",
             "correct": False,
             "why": "Nothing adds oxygen to air inside the body, and here "
                    "the early figure is high because that air was never "
                    "used, not because anything was put into it."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h31",
        "band": "harder",
        "text": "Evaluate this claim: because nitrogen passes through the "
                "body unchanged, a supply of 21% oxygen and 79% helium "
                "would keep a person alive just as well as ordinary air.",
        "options": [
            {"text": "The claim fails, because the body needs nitrogen "
                     "from the air in order to build its proteins.",
             "correct": False,
             "why": "You are built from nitrogen, but every atom of it "
                    "comes from food. The nitrogen you breathe in comes "
                    "straight back out."},
            {"text": "The claim fails, because helium is much lighter than "
                     "nitrogen and so cannot travel down to the alveoli.",
             "correct": False,
             "why": "A gas mixture travels down the airway as a whole and "
                    "does not separate out by weight on the way."},
            {"text": "The claim holds: the body uses neither gas, so what "
                     "matters is that the oxygen share is unchanged.",
             "correct": True},
            {"text": "The claim fails, because without nitrogen the "
                     "alveoli would have nothing to hold them open between "
                     "breaths.",
             "correct": False,
             "why": "Helium fills the space just as nitrogen did. Swapping "
                    "one unused gas for another leaves the sacs exactly as "
                    "full as before."},
        ],
        "figure": None,
    },
    {
        "id": "b4-01-h32",
        "band": "harder",
        "text": "A pupil says the job of the gas exchange system is to get "
                "oxygen to every cell in the body. Evaluate how much of "
                "that job the system actually does.",
        "options": [
            {"text": "It does the whole job, because the airway branches "
                     "so finely that it reaches every part of the body.",
             "correct": False,
             "why": "The branching is all inside the lungs. No tube of the "
                    "airway goes anywhere near a muscle cell in your leg."},
            {"text": "It does none of it, because the blood collects the "
                     "oxygen it needs from food in the gut.",
             "correct": False,
             "why": "No oxygen is absorbed from food. All of it crosses at "
                    "the alveoli, which is the part of the job this system "
                    "does."},
            {"text": "It does the whole job as far as the cell wall, where "
                     "respiration takes the oxygen the rest of the way in.",
             "correct": False,
             "why": "The system hands over long before the cell. Oxygen "
                    "crosses into the blood at the alveoli and is carried "
                    "the rest of the way."},
            {"text": "It gets oxygen only as far as the blood; the "
                     "circulatory system carries it to the cells.",
             "correct": True},
        ],
        "figure": None,
    },
]
