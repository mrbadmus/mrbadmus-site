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

    # -- easier --
    {
        "id": "c10-05-e09",
        "band": "easier",
        "text": "Roughly how long has the atmosphere's composition been "
                "remarkably steady, according to the lesson?",
        "options": [
            {"text": "About 200 million years",
             "correct": True},
            {"text": "About 2000 years, since the start of recorded human "
                     "history",
             "correct": False,
             "why": "That is far too short. The stability described goes "
                    "back tens of millions of times longer than that."},
            {"text": "About 4.6 billion years, the whole age of the Earth",
             "correct": False,
             "why": "The composition changed dramatically for most of that "
                    "time. It has only been steady for a much smaller, more "
                    "recent slice of it."},
            {"text": "About 20 million years",
             "correct": False,
             "why": "That understates it by a factor of ten. The figure "
                    "given is closer to 200 million years."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e10",
        "band": "easier",
        "text": "Nitrogen is essential to every protein in your body. Why "
                "can't you meet that need simply by breathing more air?",
        "options": [
            {"text": "There is not enough nitrogen in the air for breathing "
                     "to ever supply a useful amount of it",
             "correct": False,
             "why": "There is plenty — nitrogen is nearly four fifths of "
                    "the air. The problem is that the gas form cannot be "
                    "used directly."},
            {"text": "Nitrogen gas is far too unreactive for your body to "
                     "absorb and use directly, so it has to come from food "
                     "instead",
             "correct": True},
            {"text": "Breathing only delivers oxygen to the body, never any "
                     "other gas from the air at all",
             "correct": False,
             "why": "Other gases are inhaled too, nitrogen included. The "
                    "issue is that the body cannot make use of nitrogen in "
                    "that unreactive gas form."},
            {"text": "The lungs are only able to absorb gases that are "
                     "denser than nitrogen is",
             "correct": False,
             "why": "Density is not what decides it. The gas is simply too "
                    "chemically unreactive to be taken up and used."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e11",
        "band": "easier",
        "text": "Nitrogen, oxygen, argon and carbon dioxide add up to about "
                "99.94% of dry air. What does the remaining 0.06% consist "
                "of?",
        "options": [
            {"text": "Water vapour, which has simply been left off the bar "
                     "by mistake",
             "correct": False,
             "why": "Water vapour is left out on purpose because it varies, "
                    "and it is far more than that over a warm sea."},
            {"text": "Measurement error, since no instrument can ever be "
                     "perfectly accurate",
             "correct": False,
             "why": "The remainder is real gas, not a mistake in measuring "
                    "the other four."},
            {"text": "Other gases, present in the air in much smaller "
                     "amounts than any of the four shown",
             "correct": True},
            {"text": "Pollution released by human activity in modern times",
             "correct": False,
             "why": "The remaining gases are a natural part of the air, not "
                    "a product of pollution."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e12",
        "band": "easier",
        "text": "According to the lesson's own carbon dioxide note, why is "
                "the 0.04% figure changing today?",
        "options": [
            {"text": "It is falling because plants are absorbing it faster "
                     "than ever before",
             "correct": False,
             "why": "The figure is rising, not falling. Burning adds carbon "
                    "dioxide faster than plants remove it."},
            {"text": "It stays fixed at exactly 0.04% and never changes at "
                     "all",
             "correct": False,
             "why": "The note says this fraction is rising now. It is not a "
                    "fixed, unchanging figure."},
            {"text": "It changes only with the seasons and always returns "
                     "to the same yearly average",
             "correct": False,
             "why": "A seasonal wobble is a separate matter from the rise "
                    "the note actually describes."},
            {"text": "It is rising because of what people burn",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e13",
        "band": "easier",
        "text": "Roughly how much water vapour can the air hold over a warm "
                "sea, compared with almost none over a desert?",
        "options": [
            {"text": "About four parts in a hundred",
             "correct": True},
            {"text": "About four parts in a million",
             "correct": False,
             "why": "That is far too small. Over a warm sea the figure "
                    "given is close to four per cent, not four in a "
                    "million."},
            {"text": "About forty parts in a hundred",
             "correct": False,
             "why": "That would make water vapour nearly half the air, "
                    "which is far higher than the figure given."},
            {"text": "About the same as the argon in dry air, roughly one "
                     "part in a hundred",
             "correct": False,
             "why": "The figure given for a warm sea is over four times "
                    "argon's share, not roughly the same as it."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e14",
        "band": "easier",
        "text": "Argon was not included in Mendeleev's original periodic "
                "table. What is the reason given for that?",
        "options": [
            {"text": "Mendeleev deliberately left unreactive gases out of "
                     "his table on purpose",
             "correct": False,
             "why": "Nothing suggests he excluded it deliberately. The gas "
                    "simply had not been discovered yet."},
            {"text": "Argon had not yet been discovered when Mendeleev drew "
                     "up his table",
             "correct": True},
            {"text": "Argon does not actually belong anywhere on a periodic "
                     "table of elements",
             "correct": False,
             "why": "Argon is a genuine element and does have its own place "
                    "on a modern periodic table."},
            {"text": "Mendeleev's table only included metals, and argon is "
                     "not a metal",
             "correct": False,
             "why": "The table included non-metals too. Argon's absence was "
                    "about timing of discovery, not about being a "
                    "non-metal."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e15",
        "band": "easier",
        "text": "You only actually absorb about a quarter of the oxygen you "
                "breathe in. What happens to the rest of it?",
        "options": [
            {"text": "It is converted into carbon dioxide before it leaves "
                     "your lungs",
             "correct": False,
             "why": "Conversion of oxygen into carbon dioxide happens "
                    "elsewhere in the body's chemistry, not simply by "
                    "sitting unused in the lungs."},
            {"text": "It is stored inside the lungs for later use",
             "correct": False,
             "why": "The lungs do not store unused oxygen. What is not "
                    "absorbed is exhaled straight away."},
            {"text": "It is breathed straight back out again, still present "
                     "in the air you exhale",
             "correct": True},
            {"text": "It reacts with the nitrogen already present in the "
                     "lungs",
             "correct": False,
             "why": "Nitrogen is far too unreactive to react with anything "
                    "in the lungs at body temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e16",
        "band": "easier",
        "text": "Which stage of the atmosphere's history happened FIRST, "
                "about 4600 million years ago?",
        "options": [
            {"text": "Photosynthetic bacteria appearing and releasing "
                     "oxygen",
             "correct": False,
             "why": "That happened far later, around 2700 million years "
                    "ago, not at the very start."},
            {"text": "Carbon becoming buried in rock as coal, oil and gas",
             "correct": False,
             "why": "That is the most recent of the five stages, around 400 "
                    "million years ago."},
            {"text": "The water vapour condensing to form the oceans",
             "correct": False,
             "why": "That came slightly later, once the surface had cooled "
                    "a little further."},
            {"text": "Volcanoes releasing enormous quantities of gas",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e17",
        "band": "easier",
        "text": "Around 400 million years ago, carbon began being locked "
                "away underground in solid form. Which of these is NOT "
                "one of the forms it took?",
        "options": [
            {"text": "Limestone",
             "correct": False,
             "why": "Limestone is one of the forms named. Shells and "
                    "skeletons had been building it up since the oceans "
                    "first appeared."},
            {"text": "Natural gas",
             "correct": False,
             "why": "Natural gas is one of the forms named, from buried "
                    "marine organisms."},
            {"text": "Liquid nitrogen",
             "correct": True},
            {"text": "Coal",
             "correct": False,
             "why": "Coal is one of the forms named, from the buried "
                    "remains of vast swamp forests."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e18",
        "band": "easier",
        "text": "What happens to nitrogen in your lungs when you breathe?",
        "options": [
            {"text": "It is absorbed and used for respiration, exactly as "
                     "oxygen is",
             "correct": False,
             "why": "Oxygen is the gas absorbed for respiration. Nitrogen "
                    "passes through without being used."},
            {"text": "It passes straight through unchanged and is breathed "
                     "back out",
             "correct": True},
            {"text": "It is added to by your body and breathed out in "
                     "greater amounts than it arrived",
             "correct": False,
             "why": "That describes carbon dioxide, not nitrogen. Nitrogen "
                    "simply passes through unchanged."},
            {"text": "It reacts with the walls of the lungs and forms a new "
                     "compound",
             "correct": False,
             "why": "Nitrogen is far too unreactive to form a new compound "
                    "inside the lungs."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e19",
        "band": "easier",
        "text": "Most of the air you breathe in comes straight back out "
                "again. What is different about carbon dioxide's journey "
                "through your lungs?",
        "options": [
            {"text": "It passes straight through unchanged, exactly as "
                     "nitrogen does",
             "correct": False,
             "why": "Carbon dioxide is added to by the body. Nitrogen is "
                    "the gas that passes through unchanged."},
            {"text": "It is absorbed and used for respiration, exactly as "
                     "oxygen is",
             "correct": False,
             "why": "Oxygen is what is absorbed for respiration. Carbon "
                    "dioxide is a waste product that is added, not "
                    "absorbed."},
            {"text": "Your body adds to it, so more leaves in the air you "
                     "breathe out than arrived in the air you breathed in",
             "correct": True},
            {"text": "It is broken down into oxygen before it leaves the "
                     "lungs",
             "correct": False,
             "why": "Nothing breaks carbon dioxide down inside the lungs. "
                    "It is simply added to and breathed out."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e20",
        "band": "easier",
        "text": "Coal took hundreds of millions of years to form by burial. "
                "Roughly how long does burning it take to put that same "
                "carbon back into the air?",
        "options": [
            {"text": "A couple of million years",
             "correct": False,
             "why": "That is far slower than burning actually is. Burning "
                    "releases the carbon within a few hundred years at "
                    "most."},
            {"text": "A couple of decades",
             "correct": False,
             "why": "That understates how long widespread burning has "
                    "taken. The figure given is closer to a couple of "
                    "centuries."},
            {"text": "Exactly as many years as it took to form",
             "correct": False,
             "why": "The two timescales are wildly different, which is "
                    "precisely the point being made."},
            {"text": "A couple of centuries",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e21",
        "band": "easier",
        "text": "Which two gases cannot be drawn to their true width on the "
                "composition bar, because their true share would be too "
                "thin to see or tap?",
        "options": [
            {"text": "Argon and carbon dioxide",
             "correct": True},
            {"text": "Nitrogen and oxygen, because a wide slice is harder "
                     "to draw accurately",
             "correct": False,
             "why": "Those two make up the vast majority of the bar and are "
                    "easily wide enough to draw and tap accurately."},
            {"text": "Nitrogen and argon",
             "correct": False,
             "why": "Nitrogen is easily wide enough to draw accurately. The "
                    "two thin gases are argon and carbon dioxide."},
            {"text": "Oxygen and carbon dioxide",
             "correct": False,
             "why": "Oxygen is a fifth of the air and easily wide enough to "
                    "draw. The other thin gas is argon, not oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e22",
        "band": "easier",
        "text": "Has the atmosphere's composition been the same since the "
                "Earth first formed, or has it changed?",
        "options": [
            {"text": "It has been exactly the same throughout the whole 4.6 "
                     "billion years of Earth's history",
             "correct": False,
             "why": "The composition changed dramatically for most of that "
                    "time. Steadiness is a comparatively recent state."},
            {"text": "It has changed dramatically, and only settled into "
                     "something steady much more recently",
             "correct": True},
            {"text": "It has changed constantly and randomly, with no "
                     "period of it ever being steady at all",
             "correct": False,
             "why": "It has been remarkably steady for roughly the last 200 "
                    "million years, so it is not constantly changing even "
                    "now."},
            {"text": "Nobody knows whether it has changed, since there is "
                     "no way to find out",
             "correct": False,
             "why": "Evidence such as ancient rocks and volcanic gases does "
                    "let scientists work out how it has changed."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e23",
        "band": "easier",
        "text": "Does argon play any biological role in your body, in the "
                "way oxygen and carbon dioxide do?",
        "options": [
            {"text": "Yes — argon is needed for building proteins, exactly "
                     "as nitrogen is",
             "correct": False,
             "why": "Nitrogen has that role, once it comes from food. Argon "
                    "has no biological role of any kind."},
            {"text": "Yes — argon is absorbed for respiration, exactly as "
                     "oxygen is",
             "correct": False,
             "why": "Oxygen is what is absorbed for respiration. Argon "
                    "passes through the body doing nothing at all."},
            {"text": "No — argon has no biological role in your body at all",
             "correct": True},
            {"text": "Yes — argon is released as a waste product, exactly "
                     "as carbon dioxide is",
             "correct": False,
             "why": "Nothing in the body produces argon as a waste product. "
                    "It simply has no biological role."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e24",
        "band": "easier",
        "text": "About how many years passed between volcanoes forming the "
                "earliest atmosphere (4600 million years ago) and the water "
                "vapour condensing to form the oceans (4400 million years "
                "ago)?",
        "options": [
            {"text": "About 2 million years",
             "correct": False,
             "why": "That is a hundred times too small. The gap between the "
                    "two dates given is 200 million years."},
            {"text": "About 2000 million years",
             "correct": False,
             "why": "That is ten times too large. Subtracting the two dates "
                    "given leaves 200 million years, not 2000."},
            {"text": "About 20 million years",
             "correct": False,
             "why": "That is ten times too small. The gap between the two "
                    "dates given is 200 million years."},
            {"text": "About 200 million years",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e25",
        "band": "easier",
        "text": "About how many years passed between the oceans forming "
                "(4400 million years ago) and carbon dioxide dissolving "
                "into them (4000 million years ago)?",
        "options": [
            {"text": "About 400 million years",
             "correct": True},
            {"text": "About 40 million years",
             "correct": False,
             "why": "That is ten times too small. Subtracting the two dates "
                    "given leaves 400 million years."},
            {"text": "About 4000 million years",
             "correct": False,
             "why": "That is ten times too large. The gap between the two "
                    "dates given is 400 million years, not 4000."},
            {"text": "About 800 million years",
             "correct": False,
             "why": "That is double the true gap. Subtracting the two dates "
                    "given leaves 400 million years."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e26",
        "band": "easier",
        "text": "Roughly when did photosynthetic bacteria first appear and "
                "start releasing oxygen, according to the timeline?",
        "options": [
            {"text": "About 270 million years ago",
             "correct": False,
             "why": "That is ten times too recent. The timeline gives 2700 "
                    "million years ago, not 270."},
            {"text": "About 2700 million years ago",
             "correct": True},
            {"text": "About 27,000 million years ago",
             "correct": False,
             "why": "That is far older than the Earth itself, which formed "
                    "about 4600 million years ago."},
            {"text": "About 4600 million years ago, at the very start",
             "correct": False,
             "why": "That is the date volcanoes formed the earliest "
                    "atmosphere. Photosynthesis appeared much later."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e27",
        "band": "easier",
        "text": "What does the water vapour figure being left out of the "
                "usual 78/21/0.9/0.04 composition tell you about those four "
                "numbers?",
        "options": [
            {"text": "They are only rough estimates, since nobody has ever "
                     "measured the air precisely",
             "correct": False,
             "why": "The four figures are precisely measured for dry air. "
                    "What varies is the water vapour, which is separate "
                    "from them."},
            {"text": "They only apply to air found high up in the "
                     "atmosphere, far above the ground",
             "correct": False,
             "why": "They describe ordinary air generally. What sets them "
                    "apart is that the water vapour has been left out, not "
                    "the altitude."},
            {"text": "They are the composition of DRY air, with the "
                     "variable water vapour taken out",
             "correct": True},
            {"text": "They are wrong, because water vapour should always be "
                     "included in any composition figure",
             "correct": False,
             "why": "Leaving water vapour out is a deliberate, sensible "
                    "choice, since its amount varies so much from place to "
                    "place."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e28",
        "band": "easier",
        "text": "Roughly how old is the Earth itself, according to the "
                "timeline's very first stage?",
        "options": [
            {"text": "About 460 million years old",
             "correct": False,
             "why": "That is ten times too young. The timeline's first "
                    "stage is dated to about 4600 million years ago."},
            {"text": "About 46,000 million years old",
             "correct": False,
             "why": "That is far older than the age given for the universe "
                    "itself, let alone the Earth."},
            {"text": "About 400 million years old",
             "correct": False,
             "why": "That is the date of the timeline's LAST stage, when "
                    "carbon became buried in rock, not the Earth's age."},
            {"text": "About 4600 million years old",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e29",
        "band": "easier",
        "text": "The lesson describes the early atmosphere as 'the leading "
                "idea' rather than as a directly measured fact. Why?",
        "options": [
            {"text": "Because nobody has a sample of air from 4.6 billion "
                     "years ago to measure directly",
             "correct": True},
            {"text": "Because scientists have not yet agreed on any part "
                     "of what the early atmosphere contained",
             "correct": False,
             "why": "There is real agreement on the broad picture, "
                    "particularly that there was no oxygen worth measuring. "
                    "It is a lack of a direct sample, not a lack of "
                    "agreement."},
            {"text": "Because volcanoes today release completely different "
                     "gases from the ones they released long ago",
             "correct": False,
             "why": "Studying today's volcanoes is part of how the model is "
                    "built, on the assumption that the chemistry has not "
                    "changed."},
            {"text": "Because the early atmosphere is thought not to have "
                     "existed",
             "correct": False,
             "why": "The early atmosphere certainly existed. What is "
                    "uncertain is its exact detailed composition, not "
                    "whether it was there."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-e30",
        "band": "easier",
        "text": "Roughly when did carbon dioxide dissolve into the new "
                "oceans, according to the timeline?",
        "options": [
            {"text": "About 400 million years ago",
             "correct": False,
             "why": "That is the date of the timeline's LAST stage, when "
                    "carbon became buried in rock, not when it dissolved "
                    "into the oceans."},
            {"text": "About 4000 million years ago",
             "correct": True},
            {"text": "About 40 million years ago",
             "correct": False,
             "why": "That is far too recent. The timeline gives 4000 "
                    "million years ago for this stage."},
            {"text": "About 2700 million years ago",
             "correct": False,
             "why": "That is when photosynthetic bacteria appeared, a later "
                    "and separate stage on the timeline."},
        ],
        "figure": None,
    },
    # -- standard --
    {
        "id": "c10-05-s09",
        "band": "standard",
        "text": "Nitrogen is essential to every protein in your body, and "
                "you breathe it in constantly as part of the air. What must "
                "your body actually be doing instead, to get the nitrogen "
                "it needs?",
        "options": [
            {"text": "Getting it from food, where nitrogen is already "
                     "combined into a chemical form the body can use",
             "correct": True},
            {"text": "Slowly converting the nitrogen gas that reaches the "
                     "lungs into protein over the course of many years",
             "correct": False,
             "why": "The lungs cannot convert nitrogen gas into anything at "
                    "all. The body relies on food instead."},
            {"text": "Absorbing a very small fraction of the nitrogen gas "
                     "breathed in, too small to notice on a bar chart",
             "correct": False,
             "why": "None of the nitrogen gas breathed in is absorbed, "
                    "however small a fraction. It is all breathed back out "
                    "again."},
            {"text": "Storing nitrogen gas in body fat until it is needed "
                     "to build a protein",
             "correct": False,
             "why": "Nitrogen gas is not stored anywhere in the body for "
                    "this purpose. It has to arrive already combined, "
                    "through food."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s10",
        "band": "standard",
        "text": "You only absorb about a quarter of the oxygen you breathe "
                "in, so the breath you exhale still carries roughly three "
                "quarters of the oxygen it arrived with. Why does that fact "
                "make resuscitation, breathing into someone else, work?",
        "options": [
            {"text": "Because breathing out adds fresh oxygen to the air "
                     "that was not there before",
             "correct": False,
             "why": "Nothing adds new oxygen. The exhaled breath simply "
                    "still contains most of the oxygen it started with."},
            {"text": "Because the rescuer's exhaled breath still carries "
                     "far more oxygen than the person receiving it "
                     "currently has coming in on their own",
             "correct": True},
            {"text": "Because carbon dioxide in the exhaled breath is what "
                     "actually restarts the other person's breathing",
             "correct": False,
             "why": "It is the oxygen still present in the exhaled breath "
                    "that helps, not the carbon dioxide."},
            {"text": "Because all of the oxygen breathed in is used up, so "
                     "none of it is wasted by exhaling any of it",
             "correct": False,
             "why": "Only about a quarter is used. The other three quarters "
                    "is exactly what is exhaled and can still help another "
                    "person."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s11",
        "band": "standard",
        "text": "A composition bar for dry air has to draw its two "
                "smallest gases wider than their true share, because at "
                "their real width they would be a hairline nobody could "
                "tap. Why does the page choose to ADMIT this distortion "
                "rather than simply leave it unremarked?",
        "options": [
            {"text": "Because admitting it makes the bar chart look more "
                     "impressive and scientific to whoever is reading it, "
                     "and a chart that lists its own limits is always "
                     "trusted more",
             "correct": False,
             "why": "Appearing impressive is not the reason given. The "
                    "reason is about not misleading the reader."},
            {"text": "Because the two gases are far more common than the "
                     "bar shows, once the distortion is admitted",
             "correct": False,
             "why": "Admitting the distortion does not change how much of "
                    "each gas there really is. It only makes the chart's "
                    "own limits honest."},
            {"text": "Because a distortion that is openly admitted teaches "
                     "something true about scale, while the same distortion "
                     "left unremarked teaches a false impression instead",
             "correct": True},
            {"text": "Because every bar chart legally has to state exactly "
                     "how accurate it is",
             "correct": False,
             "why": "There is no such legal requirement. The choice is "
                    "about honest teaching, not about following a rule."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s12",
        "band": "standard",
        "text": "Photosynthetic bacteria appeared around 2700 million years "
                "ago, and carbon started being buried in rock in large "
                "quantities around 400 million years ago. Roughly how many "
                "years separate those two stages?",
        "options": [
            {"text": "About 3100 million years",
             "correct": False,
             "why": "That would be the result of adding the two dates "
                    "together rather than finding the gap between them."},
            {"text": "About 230 million years, a tenth of the true gap",
             "correct": False,
             "why": "That is ten times too small. Subtracting 400 from 2700 "
                    "leaves 2300 million years, not 230."},
            {"text": "About 400 million years",
             "correct": False,
             "why": "That is only the later of the two dates on its own, "
                    "not the gap between the two stages."},
            {"text": "About 2300 million years",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s13",
        "band": "standard",
        "text": "Argon is unreactive and has no biological role at all; "
                "carbon dioxide is chemically central to every living "
                "thing. Why does the FRACTION of each gas in the air not "
                "reflect how important it is?",
        "options": [
            {"text": "Because how much of a gas there is and how much it "
                     "matters chemically are two entirely separate "
                     "questions",
             "correct": True},
            {"text": "Because argon's fraction is a mistake and should "
                     "really be much smaller than it is measured to be",
             "correct": False,
             "why": "Argon's fraction is measured accurately. There is no "
                    "error to correct here."},
            {"text": "Because carbon dioxide's fraction is a mistake and "
                     "should really be much larger than it is currently "
                     "measured to be",
             "correct": False,
             "why": "Carbon dioxide's fraction is measured accurately. It "
                    "genuinely is a tiny share of the air."},
            {"text": "Because importance to living things is always "
                     "directly proportional to how common a gas is",
             "correct": False,
             "why": "That is exactly the assumption this comparison shows "
                    "to be false — a tiny fraction can matter enormously."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s14",
        "band": "standard",
        "text": "Which came first, the oceans forming or photosynthetic "
                "bacteria appearing, and roughly how many years apart were "
                "the two events?",
        "options": [
            {"text": "Photosynthetic bacteria, by roughly 1700 million "
                     "years",
             "correct": False,
             "why": "The oceans formed around 4400 million years ago, well "
                    "before photosynthesis appeared around 2700 million "
                    "years ago — not the other way round."},
            {"text": "The oceans, by roughly 1700 million years",
             "correct": True},
            {"text": "The oceans, by roughly 200 million years",
             "correct": False,
             "why": "The order is right and the gap is far too small. "
                    "Subtracting the two dates leaves about 1700 million "
                    "years, not 200."},
            {"text": "Both at roughly the same time, within a few million "
                     "years of each other",
             "correct": False,
             "why": "The two dates are well over a billion years apart, "
                    "nowhere close to roughly the same time."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s15",
        "band": "standard",
        "text": "The lesson calls the early atmosphere's composition 'the "
                "leading idea' rather than a plain fact. What kind of "
                "evidence does it say that idea is actually built from?",
        "options": [
            {"text": "A guess made without reference to any evidence, "
                     "simply because nobody can know for certain",
             "correct": False,
             "why": "It is built from real evidence, not from an "
                    "unsupported guess. Volcanic gases and ancient rocks "
                    "supply the evidence."},
            {"text": "Direct chemical analysis of trapped air bubbles "
                     "sealed inside 4.6-billion-year-old ice",
             "correct": False,
             "why": "No ice or air sample from that far back exists. The "
                    "evidence instead comes from modern volcanoes and "
                    "ancient rocks."},
            {"text": "What volcanoes release today, together with what the "
                     "oldest surviving rocks record",
             "correct": True},
            {"text": "Computer simulations of other planets that are "
                     "assumed to resemble the early Earth",
             "correct": False,
             "why": "The evidence named is volcanic gases and ancient "
                    "rocks, not simulations of other planets."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s16",
        "band": "standard",
        "text": "The gap between volcanoes forming the earliest atmosphere "
                "and the oceans appearing is only 200 million years, "
                "against a full 4.6-billion-year history. Is it fair to "
                "call the oceans forming 'quick' on that scale?",
        "options": [
            {"text": "No — 200 million years is an enormous span of time by "
                     "any measure, so it cannot fairly be called quick",
             "correct": False,
             "why": "It is enormous in absolute terms, and the question is "
                    "about the scale being used — against 4.6 billion "
                    "years, it is a small fraction."},
            {"text": "No — the two events happened at exactly the same "
                     "time, so there is no gap to call quick",
             "correct": False,
             "why": "There is a real 200-million-year gap between the two "
                    "dates given. They did not happen simultaneously."},
            {"text": "Yes — but only because 200 million years is the "
                     "shortest gap anywhere on the whole timeline",
             "correct": False,
             "why": "Whether it is the shortest gap is not what makes it "
                    "fair to call quick here — being a small fraction of "
                    "the whole span is."},
            {"text": "Yes — 200 million years is a small fraction of 4.6 "
                     "billion years, so on that scale it counts as quick",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s17",
        "band": "standard",
        "text": "Carbon began being buried in rock in large quantities "
                "about 400 million years ago. Is the time since then "
                "roughly a tenth, roughly a half, or roughly all of the "
                "Earth's 4.6-billion-year history?",
        "options": [
            {"text": "Roughly a tenth of Earth's history",
             "correct": True},
            {"text": "Roughly a half of Earth's history",
             "correct": False,
             "why": "Half of 4.6 billion years is about 2.3 billion "
                    "years, nearly six times longer than the 400 million "
                    "years given here."},
            {"text": "Roughly all of Earth's history, with almost nothing "
                     "left over",
             "correct": False,
             "why": "400 million years is under a tenth of 4.6 billion "
                    "years, leaving the great bulk of it outside that "
                    "period."},
            {"text": "It cannot be judged as any particular fraction "
                     "without knowing the exact day Earth formed",
             "correct": False,
             "why": "The approximate ages given are more than enough to "
                    "judge the fraction roughly, without needing an exact "
                    "day."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s18",
        "band": "standard",
        "text": "Water vapour can be close to four per cent of the air over "
                "a warm sea and almost nothing over a desert. Why would "
                "printing a single fixed percentage for it on a composition "
                "chart be misleading?",
        "options": [
            {"text": "Because water vapour cannot be measured accurately by "
                     "any scientific instrument that currently exists",
             "correct": False,
             "why": "Water vapour can be measured accurately. The problem "
                    "is that the true value keeps changing, not that it "
                    "cannot be measured."},
            {"text": "Because that single number would only ever be true in "
                     "one place at one time, while the real figure varies "
                     "enormously from place to place",
             "correct": True},
            {"text": "Because water vapour is not really a gas, so it "
                     "should not appear on a gas composition chart",
             "correct": False,
             "why": "Water vapour genuinely is a gas. The issue is its "
                    "variability, not whether it counts as one."},
            {"text": "Because a fixed percentage would always have to be "
                     "shown as exactly zero, which nobody would believe",
             "correct": False,
             "why": "A fixed figure would not have to be zero. The real "
                    "problem is that any single fixed figure would be wrong "
                    "most of the time."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s19",
        "band": "standard",
        "text": "The atmosphere changed dramatically for most of Earth's "
                "history, and has only been steady for roughly the last 200 "
                "million years. What do these two facts together show about "
                "the atmosphere's past?",
        "options": [
            {"text": "It has been equally stable throughout the whole of "
                     "Earth's history, without exception",
             "correct": False,
             "why": "The composition changed dramatically for most of that "
                    "history. Stability is the more recent and shorter "
                    "regime."},
            {"text": "It has been equally chaotic throughout the whole of "
                     "Earth's history, right up to today",
             "correct": False,
             "why": "The last 200 million years are described as remarkably "
                    "steady, not as chaotic."},
            {"text": "It has passed through two very different regimes: a "
                     "long period of upheaval, followed by a much shorter "
                     "period of stability",
             "correct": True},
            {"text": "The two facts contradict each other, so one of them "
                     "must be a mistake",
             "correct": False,
             "why": "They describe two different periods of Earth's history "
                    "and are entirely consistent with each other."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s20",
        "band": "standard",
        "text": "Nitrogen and argon are both extremely unreactive as gases, "
                "yet nitrogen ends up essential to every protein in your "
                "body while argon has no biological role at all. What does "
                "that pair show?",
        "options": [
            {"text": "One of the two facts must be wrong, since both gases "
                     "behave identically in every other respect",
             "correct": False,
             "why": "Both facts are correct. They are not identical in "
                    "every respect — only in how unreactive each is as a "
                    "free gas."},
            {"text": "Argon must have some hidden biological role that has "
                     "not yet been discovered",
             "correct": False,
             "why": "Argon genuinely has no biological role. The pair shows "
                    "something about unreactivity, not a hidden role "
                    "waiting to be found."},
            {"text": "Nitrogen must be reactive as a gas after all, since "
                     "it plays a biological role",
             "correct": False,
             "why": "Nitrogen gas is genuinely unreactive. It plays its "
                    "biological role only once combined into a different "
                    "chemical form, via food."},
            {"text": "Being unreactive as a free gas does not by itself "
                     "decide whether an element has a biological role in "
                     "some other chemical form",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s21",
        "band": "standard",
        "text": "Carbon dioxide is described as both 'a sliver' of the air, "
                "at 0.04%, and as 'the fraction that is rising now because "
                "of what people burn'. Why doesn't being a sliver make the "
                "second point trivial?",
        "options": [
            {"text": "Because the lesson's whole point is that a very small "
                     "fraction can still matter enormously, and changing it "
                     "still has real consequences",
             "correct": True},
            {"text": "Because 0.04% is not a small number once it is "
                     "measured correctly",
             "correct": False,
             "why": "0.04% genuinely is a very small fraction of the air. "
                    "The point is that small does not mean unimportant, not "
                    "that the figure is wrong."},
            {"text": "Because the rise being described is far too small to "
                     "ever be measured",
             "correct": False,
             "why": "The rise has been measured. Being a sliver of the air "
                    "is a separate matter from whether the change in it can "
                    "be detected."},
            {"text": "Because the 0.04% figure is a share of dry air only, "
                     "and once the water vapour is counted back in the real "
                     "share turns out to be many times larger",
             "correct": False,
             "why": "Counting water vapour back in makes every other gas's "
                    "share slightly smaller, not larger. What makes the "
                    "point matter is the chemistry and biology built from "
                    "that tiny fraction."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s22",
        "band": "standard",
        "text": "Roughly what fraction of Earth's 4.6-billion-year history "
                "does the last 200 million years of atmospheric stability "
                "represent?",
        "options": [
            {"text": "Roughly one half",
             "correct": False,
             "why": "That would need about 2300 million years, well over "
                    "ten times as long as the 200 million years given."},
            {"text": "Roughly one twentieth",
             "correct": True},
            {"text": "Roughly nine tenths of the whole span",
             "correct": False,
             "why": "That would need over 4000 million years, vastly longer "
                    "than the 200 million years given."},
            {"text": "Roughly one thousandth",
             "correct": False,
             "why": "That would need only about 4.6 million years, far "
                    "shorter than the 200 million years given."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s23",
        "band": "standard",
        "text": "Oxygen makes up about a fifth of the air, and every animal "
                "needs it for respiration. What does the lesson say ALL of "
                "that oxygen was originally put there by?",
        "options": [
            {"text": "Volcanoes, releasing it alongside the carbon dioxide "
                     "and water vapour they also gave off",
             "correct": False,
             "why": "Volcanoes release almost no oxygen at all. Every atom "
                    "of it came from photosynthesis instead."},
            {"text": "Sunlight, splitting water vapour apart high in the "
                     "atmosphere",
             "correct": False,
             "why": "That happens in only tiny amounts and accounts for "
                    "almost none of the oxygen present today."},
            {"text": "Photosynthesis, carried out by living things over "
                     "billions of years",
             "correct": True},
            {"text": "The original cloud of gas and dust that the Earth "
                     "itself first formed out of",
             "correct": False,
             "why": "The earliest atmosphere had essentially no oxygen in "
                    "it. All of today's oxygen arrived much later."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s24",
        "band": "standard",
        "text": "Argon is produced by radioactive decay in the rocks and "
                "takes part in no chemical reaction at all. Why can a gas "
                "like that build up in the air over time, in a way a "
                "reactive one cannot?",
        "options": [
            {"text": "Unreactive gases are made in much larger quantities "
                     "than reactive ones ever are",
             "correct": False,
             "why": "How much is produced is a separate matter from whether "
                    "anything removes it afterwards, which is the point "
                    "being made here."},
            {"text": "Reactive gases evaporate out of the atmosphere "
                     "entirely once they are made",
             "correct": False,
             "why": "Reactive gases do not evaporate away. They get used up "
                    "or changed into something else by reacting."},
            {"text": "Unreactive gases are lighter than reactive ones, so "
                     "they float upward and collect at the top",
             "correct": False,
             "why": "Weight and floating are not the reason. It is having "
                    "no chemical route out of the air that lets an "
                    "unreactive gas accumulate."},
            {"text": "Because nothing chemical takes it back out of the "
                     "air, so each amount released adds to what is there",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s25",
        "band": "standard",
        "text": "Nitrogen and oxygen are 78% and 21% of dry air, adding to "
                "99% between them. Given that argon and carbon dioxide add "
                "a further 0.94% on top of that, roughly what does the full "
                "total come to?",
        "options": [
            {"text": "Almost exactly 100%, with only a tiny sliver left "
                     "over for anything else",
             "correct": True},
            {"text": "Only about 90%, leaving a full 10% completely "
                     "unaccounted for",
             "correct": False,
             "why": "Adding 78, 21, 0.9 and 0.04 comes to 99.94%, not 90%. "
                    "There is only a tiny sliver left over."},
            {"text": "Well over 100%, showing that one of the four figures "
                     "must be measured wrongly",
             "correct": False,
             "why": "Adding all four figures gives 99.94%, safely under "
                    "100%. None of them needs to be wrong."},
            {"text": "Exactly 100%, with nothing left over for any other "
                     "gas at all",
             "correct": False,
             "why": "Adding the four figures gives 99.94%, which leaves a "
                    "tiny sliver — about 0.06% — for other gases."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s26",
        "band": "standard",
        "text": "A student says water vapour should simply be added as a "
                "fifth slice on the composition bar, alongside the other "
                "four gases. What is the problem with doing that?",
        "options": [
            {"text": "There is no problem, and it should simply be added as "
                     "a fifth slice",
             "correct": False,
             "why": "It is left out deliberately, because its amount varies "
                    "too much for one fixed slice to represent it."},
            {"text": "Its share changes so much from place to place and day "
                     "to day that a single slice could never represent it "
                     "accurately",
             "correct": True},
            {"text": "Water vapour is chemically identical to carbon "
                     "dioxide, so adding it would simply duplicate a slice "
                     "already on the bar",
             "correct": False,
             "why": "Water vapour and carbon dioxide are chemically "
                    "completely different substances. That is not the "
                    "reason it is left out."},
            {"text": "A bar chart can show only four slices at most, "
                     "whatever the subject being drawn",
             "correct": False,
             "why": "There is no such limit on a bar chart. The reason "
                    "water vapour is excluded is that its amount varies."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s27",
        "band": "standard",
        "text": "Carbon started being buried in large quantities in rock "
                "around 400 million years ago, and burning fossil fuels is "
                "now returning that carbon to the air. What does comparing "
                "the two timescales highlight?",
        "options": [
            {"text": "Both timescales are roughly the same length, once "
                     "measured carefully",
             "correct": False,
             "why": "One is hundreds of millions of years and the other a "
                    "couple of centuries — they are wildly different, not "
                    "roughly the same."},
            {"text": "Burial and burning must have started happening at the "
                     "same time as each other",
             "correct": False,
             "why": "Burial began around 400 million years ago, and the "
                    "burning being compared is a very recent, modern "
                    "activity."},
            {"text": "Carbon that took an immensely long time to lock away "
                     "can be released again far, far more quickly",
             "correct": True},
            {"text": "Nothing useful can be learned from comparing two "
                     "timescales that differ so enormously from one "
                     "another in size",
             "correct": False,
             "why": "The comparison is exactly what highlights how quickly "
                    "stored carbon can be returned to the air."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s28",
        "band": "standard",
        "text": "Mars has an atmosphere that is mostly carbon dioxide. "
                "Using what this lesson says removed most of Earth's early "
                "carbon dioxide, suggest what Mars is missing that Earth "
                "has.",
        "options": [
            {"text": "Volcanoes capable of releasing carbon dioxide into "
                     "its atmosphere in the first place",
             "correct": False,
             "why": "Mars does have volcanic activity in its past. What it "
                    "lacks is a process for taking carbon dioxide back out "
                    "of the air."},
            {"text": "Any atmosphere whatsoever, of any composition at all",
             "correct": False,
             "why": "Mars does have a thin atmosphere, it is simply mostly "
                    "carbon dioxide rather than nitrogen and oxygen."},
            {"text": "Enough gravity to hold on to any gases released by "
                     "its volcanoes",
             "correct": False,
             "why": "Mars clearly does hold some atmosphere, since it has "
                    "one. The missing piece is a removal process for carbon "
                    "dioxide, not weak gravity."},
            {"text": "Oceans capable of dissolving carbon dioxide out of "
                     "the air and locking it into rock",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s29",
        "band": "standard",
        "text": "The lesson states that argon is made by radioactive decay "
                "in the rocks, rather than by any living process. What does "
                "that tell you about where argon's supply eventually comes "
                "from?",
        "options": [
            {"text": "From inside the solid Earth, released slowly over an "
                     "extremely long time",
             "correct": True},
            {"text": "From the oceans, released as water evaporates into "
                     "the air",
             "correct": False,
             "why": "Argon does not come from the oceans. It is produced by "
                    "radioactive decay inside the solid rock of the Earth."},
            {"text": "From living things, released as a waste product just "
                     "as carbon dioxide is",
             "correct": False,
             "why": "Nothing alive makes argon. Its source is decay inside "
                    "the rocks, not any living process."},
            {"text": "From the Sun, arriving as part of the same stream of "
                     "particles that also strips gas away from planets",
             "correct": False,
             "why": "The Sun's stream of particles removes gas from a "
                    "planet rather than delivering argon to it. The source "
                    "given is decay inside the rocks."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-s30",
        "band": "standard",
        "text": "The chart shows the percentages of the two main gases in dry "
                "air. What percentage of dry air is made up of all the other "
                "gases together?",
        "options": [
            {"text": "About 21%",
             "correct": False,
             "why": "That is the oxygen bar on its own. The other gases are "
                    "what is left after nitrogen AND oxygen are taken from "
                    "100%."},
            {"text": "About 1%",
             "correct": True},
            {"text": "About 99%",
             "correct": False,
             "why": "That is nitrogen and oxygen added together. The other "
                    "gases are what is left over: 100 − 99."},
            {"text": "About 0.04%",
             "correct": False,
             "why": "That is carbon dioxide alone, which is only one of the "
                    "other gases. Argon on its own is nearly 1%."},
        ],
        "figure": "c10-air-two-gases",
    },
    # -- harder --
    {
        "id": "c10-05-h09",
        "band": "harder",
        "text": "Using the timeline's own dates, roughly how many million "
                "years separate the very first stage (volcanoes, 4600 "
                "million years ago) from the very last stage (carbon buried "
                "in rock, 400 million years ago)?",
        "options": [
            {"text": "About 4200 million years",
             "correct": True},
            {"text": "About 5000 million years, adding the two dates "
                     "together",
             "correct": False,
             "why": "That would come from adding the two dates rather than "
                    "finding the gap between them."},
            {"text": "About 4600 million years, the age of the Earth",
             "correct": False,
             "why": "That is only the age of the very first stage on its "
                    "own, not the gap to the last stage."},
            {"text": "About 400 million years",
             "correct": False,
             "why": "That is only the age of the very last stage on its "
                    "own, not the gap between the first and the last."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h10",
        "band": "harder",
        "text": "The atmosphere has been steady for roughly 200 million "
                "years, out of Earth's full 4.6-billion-year history. "
                "Roughly what fraction of that whole history does 200 "
                "million years represent?",
        "options": [
            {"text": "About one half, or roughly 50%",
             "correct": False,
             "why": "That would need about 2300 million years, well over "
                    "ten times as long as 200 million years."},
            {"text": "About one twenty-third, or roughly 4%",
             "correct": True},
            {"text": "About nine tenths of it, or roughly 90%",
             "correct": False,
             "why": "That would need over 4000 million years, vastly longer "
                    "than 200 million years."},
            {"text": "About one two-hundredth, or roughly 0.5%",
             "correct": False,
             "why": "That would need Earth's history to be 40,000 million "
                    "years, far longer than the 4.6 billion years it "
                    "actually is."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h11",
        "band": "harder",
        "text": "A textbook claims argon 'has no importance' because it "
                "plays no biological role. Using this lesson's own logic "
                "about carbon dioxide's tiny but decisive share, is that "
                "claim about argon flawed in the same way?",
        "options": [
            {"text": "Yes — a small fraction is never allowed to be "
                     "unimportant, whatever gas is being discussed",
             "correct": False,
             "why": "Carbon dioxide's small fraction matters because of "
                    "what it chemically does. Argon genuinely does nothing "
                    "chemically that living things rely on."},
            {"text": "Yes — since argon and carbon dioxide have almost "
                     "identical shares of the air, whatever is true of one "
                     "must be true of the other",
             "correct": False,
             "why": "Their shares are not close at all — argon is over "
                    "twenty times carbon dioxide's share — and their "
                    "chemical roles are entirely different in any case."},
            {"text": "Not really — for argon, no biological role really "
                     "does mean no chemical importance to life, unlike "
                     "carbon dioxide, whose tiny share still matters "
                     "enormously",
             "correct": True},
            {"text": "Not really — but only because argon's fraction is "
                     "smaller than carbon dioxide's, not because of its own "
                     "chemistry",
             "correct": False,
             "why": "Argon's fraction is actually larger than carbon "
                    "dioxide's. What decides the flaw is chemistry, not the "
                    "size of the fraction."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h12",
        "band": "harder",
        "text": "Photosynthetic bacteria began releasing oxygen around 2700 "
                "million years ago, and oxygen did not begin building up in "
                "the air until roughly 300 million years later. In which of "
                "these windows did oxygen first become a measurable part of "
                "the atmosphere?",
        "options": [
            {"text": "Around 3000 million years ago",
             "correct": False,
             "why": "Adding 300 million years to 2700 million years ago "
                    "moves further into the past, not closer to today, "
                    "which is the wrong direction here."},
            {"text": "Around 2700 million years ago, immediately",
             "correct": False,
             "why": "The oxygen was being made from that point onward, and "
                    "the lesson gives a roughly 300-million-year delay "
                    "before it built up in the AIR."},
            {"text": "Around 400 million years ago",
             "correct": False,
             "why": "That is the much later date carbon began being buried "
                    "in rock, a separate and far more recent stage."},
            {"text": "Around 2400 million years ago",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h13",
        "band": "harder",
        "text": "Someone says the atmosphere has 'always basically been the "
                "air we breathe today' because it has been steady for 200 "
                "million years. Using the full timeline, what is wrong with "
                "that claim?",
        "options": [
            {"text": "200 million years is a small slice of Earth's "
                     "4.6-billion-year history, and before it the "
                     "atmosphere went through dramatic, unrecognisable "
                     "changes",
             "correct": True},
            {"text": "Nothing is wrong with it, since 200 million years is "
                     "in fact the whole of Earth's history",
             "correct": False,
             "why": "Earth's full history is about 4.6 billion years, over "
                    "twenty times longer than the 200-million-year steady "
                    "period."},
            {"text": "The claim is wrong because the atmosphere has not "
                     "been steady at any single point across its "
                     "whole history, including right up to the "
                     "present day",
             "correct": False,
             "why": "The lesson does describe the last 200 million years as "
                    "remarkably steady. The problem is extending that claim "
                    "back over the WHOLE history."},
            {"text": "The claim is wrong because the composition today is "
                     "entirely different from what it was 200 million "
                     "years ago, and from every point in between then and "
                     "now",
             "correct": False,
             "why": "The point of describing it as steady is that it has "
                    "NOT changed much over that particular period."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h14",
        "band": "harder",
        "text": "Argon is 0.9% of dry air and carbon dioxide is 0.04%. By "
                "roughly what factor does argon's share exceed carbon "
                "dioxide's?",
        "options": [
            {"text": "By roughly 2 to 3 times",
             "correct": False,
             "why": "Dividing 0.9 by 0.04 gives a much larger factor than 2 "
                    "or 3 — closer to 22."},
            {"text": "By roughly 22 to 23 times",
             "correct": True},
            {"text": "By roughly 900 times",
             "correct": False,
             "why": "That greatly overstates the true ratio. Dividing 0.9 "
                    "by 0.04 gives about 22, not 900."},
            {"text": "There is no such factor, since both shares are far "
                     "too small to be compared with one another",
             "correct": False,
             "why": "Both are real measured percentages, however small, so "
                    "one divides into the other perfectly well."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h15",
        "band": "harder",
        "text": "Argon was absent from Mendeleev's original periodic table. "
                "Does that mean Mendeleev's table was wrong?",
        "options": [
            {"text": "Yes — any periodic table missing an entire element "
                     "must be considered simply wrong",
             "correct": False,
             "why": "A table can only include elements already discovered. "
                    "Missing an undiscovered one is incompleteness, not an "
                    "error in what it did include."},
            {"text": "No — because Mendeleev knew about argon in advance "
                     "but chose to leave it out",
             "correct": False,
             "why": "Nothing suggests he knew about argon in advance. It "
                    "simply had not been discovered when he built his "
                    "table."},
            {"text": "No — the table was built from the elements known at "
                     "the time, and a later discovery does not make earlier "
                     "work incorrect, only incomplete",
             "correct": True},
            {"text": "Yes — because a correct periodic table must predict "
                     "every element that will ever be discovered, and a "
                     "table that leaves a space unfilled has failed at its "
                     "main job",
             "correct": False,
             "why": "No table could predict every future discovery. Being "
                    "useful and broadly correct does not require that."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h16",
        "band": "harder",
        "text": "Coal formed over hundreds of millions of years of burial, "
                "and a comparable amount of stored carbon has been released "
                "by burning since the start of the industrial era, a period "
                "of under 300 years. As an order of magnitude, is the "
                "release roughly a thousand times faster, a million times "
                "faster, or is the comparison meaningless?",
        "options": [
            {"text": "Roughly a thousand times faster",
             "correct": False,
             "why": "Dividing hundreds of millions of years by under 300 "
                    "years gives a ratio far larger than a thousand — "
                    "closer to a million."},
            {"text": "The comparison is meaningless, since burial and "
                     "burning cannot be measured on the same scale",
             "correct": False,
             "why": "Both are measured in years, so a ratio between the two "
                    "timescales is a meaningful, if rough, comparison."},
            {"text": "Roughly the same speed, since both processes involve "
                     "the same carbon",
             "correct": False,
             "why": "Involving the same carbon does not make the two "
                    "timescales similar in length — one is vastly longer "
                    "than the other."},
            {"text": "Roughly a million times faster",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h17",
        "band": "harder",
        "text": "If nitrogen, oxygen, argon and carbon dioxide together "
                "make up 99% of dry air, does that mean scientists have "
                "accounted for everything the atmosphere might do "
                "chemically?",
        "options": [
            {"text": "No — accounting for 99% by amount says nothing about "
                     "chemical importance, since carbon dioxide alone shows "
                     "a tiny fraction can be decisive",
             "correct": True},
            {"text": "Yes — once 99% of the mass is identified, nothing "
                     "chemically significant can remain in the last 1%",
             "correct": False,
             "why": "Chemical importance does not scale with how much of "
                    "the air a gas makes up, as carbon dioxide's own tiny "
                    "share already demonstrates."},
            {"text": "Yes — because the missing 1% must be entirely "
                     "unreactive gases with no chemical role",
             "correct": False,
             "why": "Nothing here establishes what the missing 1% actually "
                    "consists of, let alone that all of it must be "
                    "unreactive."},
            {"text": "No — but only because 99% is too low a figure to "
                     "count as 'accounted for' in the first place",
             "correct": False,
             "why": "The issue is not whether 99% counts as high enough — "
                    "it is that proportion by amount does not measure "
                    "chemical importance at all."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h18",
        "band": "harder",
        "text": "Two students disagree: one says photosynthesis caused the "
                "oceans to form, the other says the oceans existed long "
                "before photosynthesis. Using the timeline's own dates, who "
                "is right?",
        "options": [
            {"text": "The first student — photosynthesis released the water "
                     "vapour that later condensed to form the oceans",
             "correct": False,
             "why": "Water vapour came from volcanoes, and the oceans "
                    "formed long before photosynthesis existed to release "
                    "anything at all."},
            {"text": "The second student — the oceans formed around 4400 "
                     "million years ago, roughly 1700 million years before "
                     "photosynthesis appeared",
             "correct": True},
            {"text": "Neither — the two events happened within a few "
                     "million years of each other, too close to say which "
                     "of the two came first with any confidence",
             "correct": False,
             "why": "The two dates given are roughly 1700 million years "
                    "apart, far too large a gap to call them roughly "
                    "simultaneous."},
            {"text": "Both are right in different ways, since the oceans "
                     "formed twice, once before and once after "
                     "photosynthesis appeared",
             "correct": False,
             "why": "The timeline gives one date for the oceans forming, "
                    "not two separate events."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h19",
        "band": "harder",
        "text": "Order these three gaps from LONGEST to SHORTEST: (a) "
                "volcanoes to oceans forming, (b) oceans forming to carbon "
                "dioxide dissolving, (c) carbon dioxide dissolving to "
                "photosynthesis appearing.",
        "options": [
            {"text": "a, then b, then c",
             "correct": False,
             "why": "That is the gaps in the wrong order — (a) is the "
                    "shortest of the three, at only 200 million years, not "
                    "the longest."},
            {"text": "b, then a, then c",
             "correct": False,
             "why": "(c), from 4000 to 2700 million years ago, is the "
                    "longest gap of the three at 1300 million years, not "
                    "the shortest."},
            {"text": "c, then b, then a",
             "correct": True},
            {"text": "All three gaps are the same length as each other",
             "correct": False,
             "why": "The three gaps are 200, 400 and 1300 million years "
                    "respectively — clearly different lengths, not the "
                    "same."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h20",
        "band": "harder",
        "text": "Because nobody has a direct sample of 4.6-billion-year-old "
                "air, the early atmosphere's makeup is called a model "
                "rather than a measured fact. Does that mean scientists are "
                "simply guessing?",
        "options": [
            {"text": "Yes — without a direct sample of the actual ancient "
                     "air itself, there is no genuine evidence of "
                     "any kind available to build a working model "
                     "on",
             "correct": False,
             "why": "Evidence does not have to be a direct sample of the "
                    "air itself. Modern volcanic gases and ancient rocks "
                    "supply real evidence instead."},
            {"text": "Yes — a model is, by definition, simply a polite word "
                     "that scientists use whenever they are making an "
                     "educated guess about something in the distant past",
             "correct": False,
             "why": "A model built from and constrained by real evidence is "
                    "different from an unsupported guess, even though both "
                    "fall short of a direct measurement."},
            {"text": "No — but because the early atmosphere has now been "
                     "measured directly after all",
             "correct": False,
             "why": "No direct sample of that ancient air has been found. "
                    "The model still rests on indirect evidence."},
            {"text": "No — the model is built from real evidence, such as "
                     "gases released by volcanoes today and what the oldest "
                     "surviving rocks record",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h21",
        "band": "harder",
        "text": "Every version of the early-atmosphere model agrees only "
                "that there was 'no oxygen worth measuring'. If a rock were "
                "later found showing a tiny trace of oxygen had existed "
                "after all, would that overturn the account?",
        "options": [
            {"text": "No — a carefully qualified claim like 'no oxygen "
                     "worth measuring' would simply be refined by such a "
                     "find, not overturned by it",
             "correct": True},
            {"text": "Yes — any oxygen found would completely destroy the "
                     "whole account of the early atmosphere",
             "correct": False,
             "why": "The claim was already qualified to allow for amounts "
                    "too small to matter. A tiny trace would fit within "
                    "that qualification, not contradict it."},
            {"text": "No — but only because no rock old enough to test this "
                     "particular claim could possibly still exist anywhere "
                     "in the world to be studied today",
             "correct": False,
             "why": "Very old rocks do survive and are studied. The reason "
                    "a trace would not overturn the account is the careful "
                    "wording of the original claim."},
            {"text": "Yes — because the account claims there was absolutely "
                     "zero oxygen present at any point, with no exceptions "
                     "permitted anywhere in it at all",
             "correct": False,
             "why": "The account says 'no oxygen worth measuring', which "
                    "already allows for an amount too small to matter, not "
                    "a claim of exactly zero."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h22",
        "band": "harder",
        "text": "Nitrogen and oxygen alone make up 99% of dry air, and "
                "carbon dioxide is only 0.04%. Which piece of reasoning "
                "best supports oxygen, rather than nitrogen, as the gas "
                "that has changed life on Earth most dramatically over its "
                "history?",
        "options": [
            {"text": "Oxygen makes up a smaller share of the air than "
                     "nitrogen does, so any change in it matters more",
             "correct": False,
             "why": "Having a smaller share does not by itself make a gas "
                    "more important — carbon dioxide is smaller still. The "
                    "reasoning here rests on oxygen's history, not its "
                    "size."},
            {"text": "Oxygen was essentially absent before life produced "
                     "it, and its arrival was a global chemical event that "
                     "reshaped which organisms could survive",
             "correct": True},
            {"text": "Nitrogen has been present in roughly the same amount "
                     "throughout the whole of Earth's history, so nothing "
                     "about it could ever have changed life on this "
                     "planet dramatically",
             "correct": False,
             "why": "Being unchanged does rule nitrogen out here, and it is "
                    "not the strongest reasoning FOR oxygen, which rests on "
                    "oxygen's own dramatic arrival."},
            {"text": "Nitrogen is used to build proteins, so it must have "
                     "changed life more dramatically than oxygen ever did",
             "correct": False,
             "why": "Being useful to life is not the same as having caused "
                    "a dramatic global change. Oxygen's sudden arrival is "
                    "the stronger case for dramatic change."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h23",
        "band": "harder",
        "text": "Nitrogen makes up nearly four fifths of the air and is "
                "essential to every protein, yet none of it is absorbed by "
                "breathing. What does that combination show about the "
                "relationship between how MUCH of a gas there is and how it "
                "actually reaches the body?",
        "options": [
            {"text": "It shows nitrogen must be absorbed by breathing after "
                     "all, since the body could not otherwise build any "
                     "protein at all",
             "correct": False,
             "why": "The lesson is clear that none of the nitrogen breathed "
                    "in is absorbed. It passes through completely "
                    "unchanged."},
            {"text": "It shows that being abundant in the air is what makes "
                     "a gas essential to life in the first place",
             "correct": False,
             "why": "Argon is even less reactive and also abundant, yet has "
                    "no biological role at all — abundance does not by "
                    "itself make a gas essential."},
            {"text": "A gas can be abundant and essential to life without "
                     "breathing being the route by which the body actually "
                     "obtains it",
             "correct": True},
            {"text": "It shows that essential gases are always absorbed by "
                     "breathing, with nitrogen being the sole exception to "
                     "that general rule",
             "correct": False,
             "why": "Oxygen is absorbed by breathing and is essential; "
                    "nitrogen is essential but is not absorbed that way — "
                    "there is no single rule connecting the two."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h24",
        "band": "harder",
        "text": "Photosynthesis released oxygen into the oceans first, "
                "which reacted with dissolved iron for roughly 300 million "
                "years before any oxygen reached the air. What does that "
                "delay show about how much oxygen the early oceans could "
                "initially absorb?",
        "options": [
            {"text": "The oceans could not absorb any oxygen, so all of it "
                     "must have reached the air immediately",
             "correct": False,
             "why": "If none had been absorbed, oxygen would have reached "
                    "the air straight away rather than 300 million years "
                    "later."},
            {"text": "Photosynthesis stopped working for 300 million years "
                     "while the oceans were being studied",
             "correct": False,
             "why": "Photosynthesis continued the whole time. What delayed "
                    "the air's oxygen was the oceans absorbing the surplus, "
                    "not a pause in photosynthesis."},
            {"text": "The delay shows nothing useful, since oceans and air "
                     "are chemically unconnected to one another in any way "
                     "that matters here",
             "correct": False,
             "why": "The oceans and the air are connected — oxygen made in "
                    "the water only reached the air once the ocean's "
                    "capacity to absorb it had been used up."},
            {"text": "The oceans could absorb an enormous quantity of "
                     "oxygen before becoming saturated enough for any "
                     "surplus to reach the air",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h25",
        "band": "harder",
        "text": "Dinosaurs went extinct around 66 million years ago, and "
                "the atmosphere has been remarkably steady for roughly the "
                "last 200 million years. Using those two facts, would "
                "dinosaurs have been breathing air of roughly the same "
                "composition we breathe today?",
        "options": [
            {"text": "Yes — 66 million years ago falls within the last "
                     "200-million-year period the lesson describes as "
                     "remarkably steady",
             "correct": True},
            {"text": "No — 66 million years ago falls well outside the last "
                     "200-million-year steady period described",
             "correct": False,
             "why": "66 is smaller than 200, so that date falls INSIDE the "
                    "steady period, not outside it."},
            {"text": "It cannot be judged, since the two figures given have "
                     "nothing to do with one another",
             "correct": False,
             "why": "Both figures describe spans of time measured back from "
                    "today, so comparing them directly is exactly how the "
                    "question can be judged."},
            {"text": "No — the atmosphere changes completely every few "
                     "million years, so no two eras ever share even a "
                     "roughly similar composition",
             "correct": False,
             "why": "The lesson describes the last 200 million years as "
                    "remarkably steady, which is the opposite of constant "
                    "dramatic change."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h26",
        "band": "harder",
        "text": "Volcanoes released nitrogen as part of the earliest "
                "atmosphere, and nitrogen has stayed largely unreactive "
                "ever since. Using that, explain why nitrogen's share of "
                "the air has been able to keep climbing over time, while "
                "carbon dioxide's share has fallen dramatically.",
        "options": [
            {"text": "Volcanoes release far more nitrogen than carbon "
                     "dioxide each time they erupt, so the air simply "
                     "inherited the proportions the eruptions delivered and "
                     "has kept them ever since, with nothing else having to "
                     "happen at all",
             "correct": False,
             "why": "Volcanoes actually release more carbon dioxide than "
                    "nitrogen. The difference in outcome comes from what "
                    "happens to each gas AFTERWARDS, not from how much is "
                    "released."},
            {"text": "With nothing removing the nitrogen once it is "
                     "released, each new volcanic release simply adds to "
                     "what is already there, while carbon dioxide is "
                     "steadily removed by dissolving and by living things",
             "correct": True},
            {"text": "Carbon dioxide reacts with nitrogen in the air, "
                     "converting one into the other over time",
             "correct": False,
             "why": "Nitrogen and carbon dioxide do not react with each "
                    "other in the air. Carbon dioxide is instead removed by "
                    "dissolving into oceans and by living things."},
            {"text": "Nitrogen is being continuously created inside living "
                     "organisms and released back into the air",
             "correct": False,
             "why": "Nothing alive manufactures nitrogen gas. Its supply "
                    "traces back to volcanic release from the early Earth, "
                    "not to any ongoing living process."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h27",
        "band": "harder",
        "text": "The lesson gives the early atmosphere's carbon dioxide and "
                "water vapour a common origin (volcanoes) but two very "
                "different fates: the water condensed into oceans within a "
                "relatively short time, while the carbon dioxide dissolved "
                "away more slowly. What do the timeline's own dates suggest "
                "about the relative speed of those two changes?",
        "options": [
            {"text": "Both changes happened at exactly the same speed, over "
                     "precisely 200 million years each, since the volcanoes "
                     "that supplied them both stopped at the same moment",
             "correct": False,
             "why": "The timeline gives 200 million years for the water "
                    "vapour and a further 400 million years on top of that "
                    "for the carbon dioxide stage — different lengths, not "
                    "the same."},
            {"text": "The carbon dioxide was removed first, and the water "
                     "vapour condensed afterwards",
             "correct": False,
             "why": "The timeline puts the oceans forming (4400 million "
                    "years ago) before the carbon dioxide dissolving (4000 "
                    "million years ago), the other way round."},
            {"text": "The water vapour condensed within about 200 million "
                     "years, while the carbon dioxide took roughly 600 "
                     "million years in total to be largely removed",
             "correct": True},
            {"text": "Neither change can be timed using the figures given "
                     "in the timeline",
             "correct": False,
             "why": "The timeline gives explicit dates for both stages, "
                    "which is enough to work out roughly how long each one "
                    "took."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h28",
        "band": "harder",
        "text": "Someone argues that because the four listed gases total "
                "99.94% of dry air, the remaining 0.06% is too small to be "
                "worth studying. Using this lesson's own argument about "
                "carbon dioxide, is that a safe conclusion?",
        "options": [
            {"text": "Yes — 0.06% is smaller than carbon dioxide's own "
                     "0.04%, so it must be even less important by the same "
                     "logic",
             "correct": False,
             "why": "The lesson's logic is the opposite: a fraction being "
                    "small does not decide its importance, so a smaller "
                    "fraction cannot be assumed less important either."},
            {"text": "Yes — anything under 1% of the air can safely be "
                     "ignored by scientists as a general rule",
             "correct": False,
             "why": "No such general rule is given, and carbon dioxide "
                    "itself, at 0.04%, is the lesson's own example of why "
                    "such a rule would be unsafe."},
            {"text": "No — but because the 0.06% figure has certainly been "
                     "measured wrongly",
             "correct": False,
             "why": "Nothing suggests the figure is measured wrongly. The "
                    "reason the conclusion is unsafe is about importance, "
                    "not about measurement error."},
            {"text": "No — the lesson's whole point about carbon dioxide is "
                     "that a tiny fraction can still matter enormously, so "
                     "size alone cannot settle the question",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h29",
        "band": "harder",
        "text": "The oldest rocks used as evidence for the early atmosphere "
                "are described as recording 'no oxygen worth measuring'. If "
                "those same rocks instead showed clear evidence of abundant "
                "oxygen from the very start, what would that do to the "
                "account of photosynthesis making the oxygen later?",
        "options": [
            {"text": "It would seriously undermine that account, since the "
                     "timing of when oxygen built up is central evidence "
                     "for photosynthesis having made it",
             "correct": True},
            {"text": "It would make no difference, since the rocks are not "
                     "real evidence for anything about the atmosphere",
             "correct": False,
             "why": "The rocks are described as genuine evidence in the "
                    "lesson. Their content — no early oxygen — directly "
                    "supports the account given."},
            {"text": "It would strengthen the account, since more oxygen "
                     "earlier would support life appearing sooner",
             "correct": False,
             "why": "Finding oxygen from the very start would contradict "
                    "the claim that photosynthesis was the SOURCE of the "
                    "oxygen that built up later, not support it."},
            {"text": "It would affect only the dates involved, without "
                     "changing anything about which process is credited "
                     "with making the oxygen in the first place",
             "correct": False,
             "why": "Early abundant oxygen with no life yet present would "
                    "remove the reason for crediting photosynthesis as the "
                    "source at all."},
        ],
        "figure": None,
    },
    {
        "id": "c10-05-h30",
        "band": "harder",
        "text": "Volcanoes supplied nitrogen, carbon dioxide and water "
                "vapour to the earliest atmosphere, but almost no oxygen at "
                "all. Using that fact together with the timeline, explain "
                "why the appearance of oxygen around 2700 million years ago "
                "is treated as evidence of a biological event rather than a "
                "further volcanic one.",
        "options": [
            {"text": "Because volcanoes had stopped erupting by 2700 "
                     "million years ago, so no gas appearing after that date "
                     "could have come from them and something else entirely "
                     "had to be responsible",
             "correct": False,
             "why": "Nothing in the lesson says volcanic activity stopped. "
                    "The reasoning rests on volcanoes never releasing "
                    "oxygen, not on volcanoes falling silent."},
            {"text": "Since volcanoes are not a source of oxygen, a gas "
                     "that had not appeared in volcanic releases before "
                     "requires a different kind of explanation, and "
                     "photosynthesis supplies one",
             "correct": True},
            {"text": "Because oxygen and carbon dioxide are the same gas "
                     "measured in two different ways",
             "correct": False,
             "why": "Oxygen and carbon dioxide are entirely different "
                    "substances, not two measurements of one gas."},
            {"text": "Because the timeline states outright that volcanoes "
                     "are biological in origin",
             "correct": False,
             "why": "Volcanoes are a geological process, not a biological "
                    "one. The reasoning is about what gas they do and do "
                    "not release, not about their own origin."},
        ],
        "figure": None,
    },
]
