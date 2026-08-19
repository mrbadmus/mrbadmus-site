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
]
