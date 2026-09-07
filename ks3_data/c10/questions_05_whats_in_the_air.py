"""C10 lesson 05 — What's in the air: twelve questions (MRB-281).

The lesson's argument is one shape: the air is a MIXTURE whose proportions are
not what anybody guesses, and every one of those proportions is the result of
something that happened. The page teaches it with a bar drawn from the four
shares and a five-stage history that runs from the volcanoes to the coal.

These twelve probe the angles the mastery ladder leaves alone: what a mixture
actually claims, why the figures are quoted dry, why nitrogen is the one that
built up, what argon is doing there, why a fraction that small is not a
negligible one, and what the rocks record.

The distractors are built from the lesson's declared misconceptions.

`EARTH-14` (air is mostly oxygen — that is the point of it) drives the wrong
options in e01, s01 and h02. Each treats the gas a body needs as the gas there
must be most of.

`EARTH-15` (the air has always been roughly like this, so the oxygen was there
from the start) drives s02, h01 and h03, where the air is offered as a fixed
backdrop that living things arrived into rather than as something they made.
`EARTH-15` carries no `elicited_by` on the page — nothing there asks a student
to commit to it — so this bank is where it is elicited, which is the
`EARTH-03/04/09/13` pattern.

⚠️ **NOTHING HERE DEPENDS ON `c10-06`.** Carbon dioxide's share and its
importance are both taught on this page and both appear below; the greenhouse
effect, the climate record and what is being done about any of it do not. This
lesson sets the next one up and must not borrow from it.

⚠️ **NO QUESTION QUOTES A PERCENTAGE THE PAGE DOES NOT PRINT.** The four shares
are the ones the bar derives — 78, 21, 0.9 and 0.04 — and where a figure is
used it is one a student has seen on the panel.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles through each
band — 0,1,2,3 · 1,2,3,0 · 2,3,0,1 — so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — `easier`, `standard`, `harder`, never the
letters.
"""

UNIT = "C10"
LESSON = "whats-in-the-air"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c10-05-e01",
        "band": "easier",
        "text": "Which gas makes up the largest part of the air?",
        "options": [
            {"text": "Nitrogen, which is nearly four fifths of every breath "
                     "you take",
             "correct": True},
            {"text": "Oxygen, because it is the gas that living things "
                     "actually need",
             "correct": False,
             "why": "Needing a gas is not the same as there being most of it. "
                    "Oxygen is about a fifth."},
            {"text": "Carbon dioxide, because every plant on Earth is built "
                     "out of it",
             "correct": False,
             "why": "Plants are built out of it, and it is still only 0.04 "
                    "per cent of the air."},
            {"text": "Argon, because nothing at all is able to react with it "
                     "or remove it",
             "correct": False,
             "why": "Argon is unreactive and it is still under one per cent. "
                    "Nitrogen is the majority gas."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e02",
        "band": "easier",
        "text": "Why is air described as a mixture rather than as a compound?",
        "options": [
            {"text": "Because it contains more than one different chemical "
                     "element in it",
             "correct": False,
             "why": "A compound contains more than one element too. What "
                    "matters is whether they are chemically joined."},
            {"text": "Because the gases in it are not chemically joined and "
                     "each keeps its own properties",
             "correct": True},
            {"text": "Because it is a gas, and every gas counts as a mixture "
                     "of some kind",
             "correct": False,
             "why": "Plenty of gases are pure compounds — carbon dioxide is "
                    "one. Being a gas decides nothing."},
            {"text": "Because you cannot see the separate gases when you look "
                     "at the air",
             "correct": False,
             "why": "You cannot see them in a compound either. Not being able "
                    "to see something is not evidence about its bonding."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e03",
        "band": "easier",
        "text": "The composition of air is always given for DRY air. Why?",
        "options": [
            {"text": "Water vapour is not really a gas, so it does not belong "
                     "in the list",
             "correct": False,
             "why": "Water vapour is a gas. It is left out because the amount "
                    "of it changes, not because it is not one."},
            {"text": "Water vapour is a liquid once it is inside the "
                     "atmosphere",
             "correct": False,
             "why": "Vapour means the gas form. It condenses to a liquid only "
                    "when it cools enough."},
            {"text": "How much water vapour there is changes from place to "
                     "place and day to day",
             "correct": True},
            {"text": "There is far too little water vapour in the air for it "
                     "to be worth counting",
             "correct": False,
             "why": "Over a warm sea it can be four parts in a hundred, which "
                    "is more than argon and carbon dioxide together."},
        ],
        "figure": None,
    },
    # ⚠️ NOT "where did the oxygen come from" — that is the apply rung's
    # question word for word, and check 6 of `verify_questions.py` exists to
    # keep the bank additional to the ladder rather than a copy of it. The
    # origin of the oxygen is covered here from the other end: what the air
    # was made of BEFORE anything alive touched it.
    {
        "id": "c10-05-e04",
        "band": "easier",
        "text": "The gases of the Earth's earliest atmosphere came mainly "
                "from one source. What was it?",
        "options": [
            {"text": "The Sun, which drove a steady stream of gas onto the "
                     "surface of the young Earth",
             "correct": False,
             "why": "The stream of particles from the Sun strips gas AWAY "
                    "from a planet. It does not deliver an atmosphere."},
            {"text": "Living things, which released gases as they grew and "
                     "spread across the whole planet",
             "correct": False,
             "why": "Living things changed the atmosphere later, and "
                    "dramatically. They did not make the first one."},
            {"text": "Comets and meteorites, which delivered the entire "
                     "atmosphere from outer space",
             "correct": False,
             "why": "Comets did bring some water and gas. The bulk of the "
                    "early atmosphere came from below, not from above."},
            {"text": "Volcanoes, which released enormous quantities of gas "
                     "as the young Earth cooled",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c10-05-s01",
        "band": "standard",
        "text": "In pure oxygen, a glowing splint bursts back into flame and "
                "steel wool burns fiercely. In ordinary air neither happens. "
                "What does that tell you about the nitrogen?",
        "options": [
            {"text": "The nitrogen reacts with the oxygen and uses some of it "
                     "up",
             "correct": False,
             "why": "Nitrogen is very unreactive as a gas. Nothing has "
                    "reacted — the two are simply mixed."},
            {"text": "It dilutes the oxygen, so burning is possible but not "
                     "automatic",
             "correct": True},
            {"text": "The nitrogen puts fires out in the way a fire "
                     "extinguisher does",
             "correct": False,
             "why": "It does not smother the flame. It is simply that four "
                    "fifths of what arrives is not oxygen."},
            {"text": "The nitrogen makes the air heavier, so less oxygen can "
                     "reach the flame",
             "correct": False,
             "why": "The gases are mixed evenly. What limits the flame is the "
                    "proportion of oxygen, not the weight of the air."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s02",
        "band": "standard",
        "text": "Rocks laid down more than about two and a half billion years "
                "ago contain iron minerals that could not survive in the "
                "presence of oxygen. What does that show?",
        "options": [
            {"text": "The iron in those rocks came from somewhere other than "
                     "the Earth",
             "correct": False,
             "why": "The iron is ordinary. What is unusual is the air it was "
                    "sitting under."},
            {"text": "Those rocks formed deep underground, where no air could "
                     "reach them",
             "correct": False,
             "why": "Many of them formed on the sea floor, in contact with "
                    "water that was in contact with the air."},
            {"text": "The atmosphere at that time contained essentially no "
                     "oxygen",
             "correct": True},
            {"text": "Oxygen only reacts with iron once there is water "
                     "present as well",
             "correct": False,
             "why": "Water speeds rusting up, and the oceans were already "
                    "there. The missing thing was the oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s03",
        "band": "standard",
        "text": "The early atmosphere was mostly carbon dioxide and there is "
                "very little left in the air now. Where did nearly all of it "
                "go?",
        "options": [
            {"text": "It was broken down by sunlight into carbon and oxygen "
                     "high in the atmosphere",
             "correct": False,
             "why": "That happens in tiny amounts and accounts for almost "
                    "none of it. Photosynthesis and the oceans did this."},
            {"text": "It escaped into space as the Earth cooled down and the "
                     "atmosphere thinned",
             "correct": False,
             "why": "Carbon dioxide is a heavy gas and the Earth's gravity "
                    "holds it easily. It went downwards, not outwards."},
            {"text": "It was buried inside the mantle when the crust cracked "
                     "into plates",
             "correct": False,
             "why": "Some carbon does travel down at plate boundaries, but "
                    "the great store is in the crust: rock and fossil fuel."},
            {"text": "It dissolved into the oceans and ended up locked in "
                     "limestone and fossil fuels",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s04",
        "band": "standard",
        "text": "Nitrogen and argon are both very unreactive. How does that "
                "help explain why there is so much of them in the air?",
        "options": [
            {"text": "Unreactive gases are lighter, so they float to the top "
                     "and collect there",
             "correct": False,
             "why": "The gases are mixed evenly, and argon is heavier than "
                    "air. Reactivity is not about weight."},
            {"text": "Once they were released, almost nothing could take them "
                     "back out again",
             "correct": True},
            {"text": "Unreactive gases are produced far faster by volcanoes "
                     "than reactive ones are",
             "correct": False,
             "why": "Volcanoes released far more carbon dioxide than "
                    "nitrogen. The difference is what happened afterwards."},
            {"text": "Unreactive gases cannot dissolve in water at all, so "
                     "the oceans never touched them",
             "correct": False,
             "why": "They dissolve a little. The reason they stayed is that "
                    "nothing reacted them into a solid."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c10-05-h01",
        "band": "harder",
        "text": "Photosynthesis started around 2.7 billion years ago, but "
                "oxygen did not build up in the air for roughly another three "
                "hundred million years. What was happening in between?",
        "options": [
            {"text": "Photosynthesis was too slow at first to make any "
                     "measurable oxygen at all",
             "correct": False,
             "why": "It was making oxygen the whole time. The question is "
                    "where that oxygen was going."},
            {"text": "The oxygen was reacting with iron dissolved in the "
                     "oceans and settling as rust",
             "correct": True},
            {"text": "Volcanoes were still adding carbon dioxide faster than "
                     "the oxygen could arrive",
             "correct": False,
             "why": "Adding one gas does not remove another. Something was "
                    "consuming the oxygen, and the rocks say what."},
            {"text": "The first organisms were using up all the oxygen they "
                     "made by respiring it",
             "correct": False,
             "why": "They were photosynthesising far more than they respired. "
                    "The oceans took the surplus."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h02",
        "band": "harder",
        "text": "Carbon dioxide is 0.04 per cent of the air. Why is it wrong "
                "to call a fraction that small unimportant?",
        "options": [
            {"text": "Because it is rising quickly, and a gas that is rising "
                     "must be an important one",
             "correct": False,
             "why": "Rising is why it is in the news. It mattered enormously "
                    "before it started rising at all."},
            {"text": "Because 0.04 per cent of something as large as the "
                     "atmosphere is still a great mass",
             "correct": False,
             "why": "True, and it is not the argument. Argon is more than "
                    "twenty times the mass and does nothing."},
            {"text": "Because every plant, and so ultimately every animal, is "
                     "built from carbon taken out of it",
             "correct": True},
            {"text": "Because it is the only gas in the air that will "
                     "dissolve into the oceans at all",
             "correct": False,
             "why": "Oxygen and nitrogen dissolve too — fish depend on "
                    "dissolved oxygen. Solubility is not what makes it "
                    "matter."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h03",
        "band": "harder",
        "text": "Mars has a thin atmosphere that is about 96 per cent carbon "
                "dioxide. Using the Earth's history, suggest the best "
                "explanation.",
        "options": [
            {"text": "Mars never had oceans or life, so nothing removed the "
                     "carbon dioxide the volcanoes released",
             "correct": True},
            {"text": "Mars formed from completely different material, so its "
                     "volcanoes gave off different gases",
             "correct": False,
             "why": "The two planets formed from the same kind of material "
                    "and their volcanoes released much the same gases."},
            {"text": "Carbon dioxide is heavier than the other gases, so on a "
                     "small planet it is the one that stays",
             "correct": False,
             "why": "Mars has lost gas of every kind. Weight does not sort an "
                    "atmosphere into layers like that."},
            {"text": "The Sun has broken the other gases on Mars down into "
                     "carbon dioxide over time",
             "correct": False,
             "why": "Sunlight breaks molecules apart, it does not build "
                    "carbon dioxide out of nitrogen."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h04",
        "band": "harder",
        "text": "Argon makes up 0.9 per cent of the air, takes part in no "
                "reaction anywhere on Earth and has no role in any living "
                "thing. So why is there any of it at all?",
        "options": [
            {"text": "Living things release it slowly as a waste product, in "
                     "the way they release carbon dioxide",
             "correct": False,
             "why": "Nothing alive makes argon. It has no biological role at "
                    "either end."},
            {"text": "It was made in the volcanic gases that formed the "
                     "earliest atmosphere",
             "correct": False,
             "why": "Volcanoes do carry it up, but they did not make it — the "
                    "rock beneath them did, and is still doing it."},
            {"text": "It has been produced by radioactive decay in the rocks "
                     "and nothing can take it out again",
             "correct": True},
            {"text": "It is left over from the cloud of gas the Sun and the "
                     "planets first formed from",
             "correct": False,
             "why": "That argon was largely lost. The argon in the air today "
                    "was made inside the Earth."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-05-e05",
        "band": "easier",
        "text": "What is an atmosphere?",
        "options": [
            {"text": "The air inside a room",
             "correct": False,
             "why": "That is the everyday sense. Here it means a planet's "
                    "gases"},
            {"text": "The oxygen a planet holds",
             "correct": False,
             "why": "It is all the gases. Mars has an atmosphere with almost "
                    "no oxygen in it"},
            {"text": "The layer of air immediately above the ground, which "
                     "extends up to about the height that the highest clouds "
                     "and the weather reach",
             "correct": False,
             "why": "The weather does happen low down, and the atmosphere is "
                    "the whole envelope of gas the planet holds"},
            {"text": "The layer of gases held around a planet by its "
                     "gravity",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e06",
        "band": "easier",
        "text": "Roughly what proportion of dry air is oxygen?",
        "options": [
            {"text": "About 21 per cent",
             "correct": True},
            {"text": "About 78 per cent, which is why a fire in an ordinary "
                     "room burns as readily as it does and why the air can "
                     "keep a person alive",
             "correct": False,
             "why": "78 per cent is the NITROGEN. Oxygen is about a fifth"},
            {"text": "About 50 per cent",
             "correct": False,
             "why": "That would make almost anything flammable. The real "
                    "ratio is about one to four"},
            {"text": "About 0.9 per cent",
             "correct": False,
             "why": "That is the argon. Oxygen is more than twenty times "
                    "that"},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e07",
        "band": "easier",
        "text": "What is a fossil fuel?",
        "options": [
            {"text": "A fuel dug out of the ground, as opposed to one grown "
                     "on the surface, which is what makes coal and wood "
                     "different from each other",
             "correct": False,
             "why": "Being dug up is not the definition. What matters is that "
                    "it is made of buried remains"},
            {"text": "A fuel made from the remains of living things buried "
                     "and compressed over millions of years",
             "correct": True},
            {"text": "A fuel that contains fossils",
             "correct": False,
             "why": "Recognisable fossils are occasionally found in coal, and "
                    "the fuel itself is the compressed remains"},
            {"text": "Any fuel that gives off carbon dioxide",
             "correct": False,
             "why": "Wood does that and is not a fossil fuel. The carbon in a "
                    "fossil fuel left the air long ago"},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e08",
        "band": "easier",
        "text": "Where did the oxygen in today's air come from?",
        "options": [
            {"text": "It was there from the moment the Earth formed",
             "correct": False,
             "why": "The rocks record when it arrived, and the early "
                    "atmosphere had essentially none"},
            {"text": "From the volcanoes that supplied the rest of the early "
                     "atmosphere, releasing it alongside the carbon dioxide "
                     "and the water vapour",
             "correct": False,
             "why": "Volcanoes give carbon dioxide, water vapour and "
                    "nitrogen. They release almost no oxygen"},
            {"text": "From photosynthesis, over billions of years",
             "correct": True},
            {"text": "From water splitting in sunlight high in the "
                     "atmosphere",
             "correct": False,
             "why": "That happens in tiny amounts and accounts for almost "
                    "none of it"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c10-05-s05",
        "band": "standard",
        "text": "Why is water vapour left OUT when the composition of air is "
                "quoted?",
        "options": [
            {"text": "Because there is too little of it to matter",
             "correct": False,
             "why": "There can be several per cent of it — more than argon "
                    "and carbon dioxide together"},
            {"text": "Because it is not a greenhouse gas",
             "correct": False,
             "why": "It is one of the strongest. That is a different lesson "
                    "and not the reason here"},
            {"text": "Because water vapour is not really one of the gases of "
                     "the air, being a liquid that happens to have evaporated "
                     "into it rather than a gas in its own right",
             "correct": False,
             "why": "Water vapour IS a gas and is genuinely part of the air. "
                    "It is left out because it varies"},
            {"text": "Because how much of it there is varies from place to "
                     "place and day to day",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s06",
        "band": "standard",
        "text": "The air's proportions can vary, and a compound's cannot. "
                "What does that establish about air?",
        "options": [
            {"text": "That it is a mixture",
             "correct": True},
            {"text": "That it is a compound whose formula is difficult to "
                     "write down, because the proportions of the gases in it "
                     "change with the weather and with height",
             "correct": False,
             "why": "A compound has one fixed formula. Varying proportions "
                    "rule a compound out"},
            {"text": "That it is an element",
             "correct": False,
             "why": "It holds several different kinds of atom, so it cannot "
                    "be an element"},
            {"text": "That its gases are chemically joined",
             "correct": False,
             "why": "They are not joined at all. Each keeps its own "
                    "properties"},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s07",
        "band": "standard",
        "text": "What happened to the water vapour in the early atmosphere?",
        "options": [
            {"text": "It was split apart by sunlight into hydrogen and "
                     "oxygen, and the oxygen it released is what the "
                     "atmosphere is made of now",
             "correct": False,
             "why": "That happens in tiny amounts. The oceans came from the "
                    "vapour, and the oxygen came from life"},
            {"text": "It condensed as the Earth cooled and formed the oceans",
             "correct": True},
            {"text": "It is still there — most of the air is water vapour",
             "correct": False,
             "why": "Water vapour is a small and variable part of the air"},
            {"text": "It reacted with the carbon dioxide",
             "correct": False,
             "why": "Carbon dioxide DISSOLVED in the oceans the water made. "
                    "The vapour itself condensed"},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s08",
        "band": "standard",
        "text": "Which gas in the air has been produced by radioactive decay "
                "in the rocks?",
        "options": [
            {"text": "Nitrogen, which is released from rocks as they weather "
                     "and is the reason it makes up so much more of the air "
                     "than any of the other gases do",
             "correct": False,
             "why": "Nitrogen came from volcanoes. The gas produced by decay "
                    "is argon"},
            {"text": "Oxygen",
             "correct": False,
             "why": "Every atom of it came out of photosynthesis"},
            {"text": "Argon",
             "correct": True},
            {"text": "Carbon dioxide",
             "correct": False,
             "why": "It came from volcanoes, and now from burning and "
                    "respiration"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-05-h05",
        "band": "harder",
        "text": "Banded iron formations were laid down in enormous "
                "quantities from about 2.5 billion years ago and then largely "
                "stopped. What do they record?",
        "options": [
            {"text": "Volcanoes releasing iron",
             "correct": False,
             "why": "Volcanoes release gases. The iron was already dissolved "
                    "in the sea"},
            {"text": "Iron rusting on land and being blown out to sea",
             "correct": False,
             "why": "Rusting on land needs the oxygen that had not built up "
                    "yet. The reaction happened in the water"},
            {"text": "A period when the Earth's crust was unusually rich in "
                     "iron, which was washed into the sea by rivers and "
                     "settled on the floor in bands as the water dried out",
             "correct": False,
             "why": "The crust's iron did not change. What changed was the "
                    "arrival of oxygen to react with the iron in the water"},
            {"text": "Oxygen reacting with iron dissolved in the oceans, "
                     "until the oceans had been swept clear of it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h06",
        "band": "harder",
        "text": "The arrival of oxygen is described as a catastrophe for "
                "almost everything then alive. Why?",
        "options": [
            {"text": "It was a corrosive poison to organisms that had evolved "
                     "without it, and most of them died",
             "correct": True},
            {"text": "It made the atmosphere so much heavier that the "
                     "pressure at the surface crushed the simple organisms "
                     "that had grown up under a thinner sky",
             "correct": False,
             "why": "The pressure change was not what killed them. Oxygen is "
                    "chemically aggressive"},
            {"text": "It cooled the planet into an ice age",
             "correct": False,
             "why": "There were consequences for the climate, and the "
                    "catastrophe named here is chemical"},
            {"text": "It blocked the sunlight photosynthesis needed",
             "correct": False,
             "why": "Oxygen is transparent. The organisms making it went on "
                    "making it"},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h07",
        "band": "harder",
        "text": "Photosynthesis released the oxygen. Where did the CARBON "
                "those organisms took out of the air end up?",
        "options": [
            {"text": "Back in the air, because respiration returns every atom "
                     "of carbon that photosynthesis takes out and the two "
                     "processes balance each other exactly",
             "correct": False,
             "why": "They nearly balance, and the small excess buried over "
                    "billions of years is what removed the carbon dioxide"},
            {"text": "In living material, and eventually locked into "
                     "sedimentary rocks and fossil fuels",
             "correct": True},
            {"text": "It was released as a gas by volcanoes",
             "correct": False,
             "why": "Volcanoes PUT carbon dioxide in. The question is where "
                    "it went afterwards"},
            {"text": "It dissolved in the oceans and stayed dissolved",
             "correct": False,
             "why": "Much of it dissolved on the way, and it did not stay "
                    "there — it ended up in limestone"},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h08",
        "band": "harder",
        "text": "Why is the composition of the air evidence that life has "
                "CHANGED the planet rather than merely lived on it?",
        "options": [
            {"text": "Because the air holds carbon dioxide, which living "
                     "things need",
             "correct": False,
             "why": "Volcanoes supplied that. It shows life depends on the "
                    "air rather than the other way round"},
            {"text": "Because living things breathe the air in and out "
                     "constantly, so every molecule in it has passed through "
                     "something alive at some point in its history",
             "correct": False,
             "why": "Breathing moves gas about without changing what the "
                    "atmosphere is made of. MAKING the oxygen did"},
            {"text": "Because the oxygen in it was produced by organisms, and "
                     "there was essentially none before them",
             "correct": True},
            {"text": "Because the air is a mixture",
             "correct": False,
             "why": "Mars's atmosphere is a mixture too, and nothing has ever "
                    "lived there as far as anyone knows"},
        ],
        "figure": None,
    },
]
