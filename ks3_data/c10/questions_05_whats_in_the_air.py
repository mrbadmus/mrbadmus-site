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
]
