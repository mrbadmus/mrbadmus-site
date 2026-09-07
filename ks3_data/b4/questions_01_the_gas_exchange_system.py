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
]
