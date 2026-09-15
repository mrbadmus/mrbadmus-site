# -*- coding: utf-8 -*-
"""B5 lesson 01 — Human reproductive systems: twelve questions (MRB-269).

The lesson makes one argument: two systems, one shared purpose, and almost
nothing else in common. Everything here probes some part of that — the eight
structures and the nine functions of the matching instrument, the five-job
table, the egg's route and the sperm's 15 cm, and the temperature argument in
the stretch note.

The distractors are built from the lesson's two declared misconceptions and
from the instrument's own design. REPRO-01 ("the two systems are mirror
images") supplies the options that pair structures that do not pair — uterus
with sperm duct, cervix with glands, penis with vagina — and the h04 option
that says the male structures were simply left off the table. REPRO-02 ("egg
cells are made all the time, like sperm cells") supplies the h03 options that
explain the ovary running out by size, by space or by rate of use rather than
by the stock being complete at birth. The rest follow the flagship's rule that
a wrong option is another structure's real job: the glands carrying, the sperm
duct making, the oviduct named where a male tube belongs. Two more errors the
lesson exists to correct are worked as well — that the egg swims towards the
sperm, and that a testis inside the abdomen would be too cold rather than too
warm.

No question restates a ladder rung. The rungs already own where fertilisation
happens, the correct statement about egg cells, the written explanation of the
asymmetry and the glands' sugar, so the bank works around all four:
fertilisation appears only inside the oviduct's route, the egg-stock idea is
put as "why does the ovary run out" rather than as a statement to pick, the
five jobs are approached through what the three female-only ones have in
common, and the glands are asked about as the source of semen rather than as a
fuel supply.

`figure` is `None` throughout. Both declared figures are at `status: needed` —
no artwork exists yet — so no question leans on one.
"""

UNIT = "B5"
LESSON = "human-reproductive-systems"
LESSON_NUMBER = 1

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-01-e01",
        "band": "easier",
        "text": "Which structure adds the fluid that, together with the "
                "sperm, makes semen?",
        "options": [
            {"text": "The testes", "correct": False,
             "why": "The testes make the sperm cells themselves. The fluid "
                    "they end up travelling in is added further along, by the "
                    "glands."},
            {"text": "The sperm duct", "correct": False,
             "why": "A transport tube and nothing more. It carries sperm "
                    "towards the urethra and adds nothing to them."},
            {"text": "The glands", "correct": True},
            {"text": "The penis", "correct": False,
             "why": "The penis transfers the finished semen into the vagina. "
                    "By the time it does, the fluid is already there."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e02",
        "band": "easier",
        "text": "Which structure stays closed while an embryo is developing, "
                "and opens during birth?",
        "options": [
            {"text": "The cervix", "correct": True},
            {"text": "The oviduct", "correct": False,
             "why": "The oviduct joins the ovary to the top of the uterus and "
                    "the egg travels along it. It is nowhere near the way "
                    "out."},
            {"text": "The uterus", "correct": False,
             "why": "The uterus is the organ being held closed. The cervix is "
                    "its lower end, and that is where the closing happens."},
            {"text": "The vagina", "correct": False,
             "why": "The vagina leads up to the cervix, but it does not close "
                    "the uterus off. A ring of muscle does that, and it is "
                    "the cervix."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e03",
        "band": "easier",
        "text": "Sperm cells are made in the testes. Which structure carries "
                "them from there towards the urethra?",
        "options": [
            {"text": "The glands", "correct": False,
             "why": "The glands add fluid to sperm that are already on their "
                    "way past them. They carry nothing themselves."},
            {"text": "The oviduct", "correct": False,
             "why": "The oviduct is in the female system and carries the egg "
                    "towards the uterus. The similar-looking name is the trap "
                    "in this question."},
            {"text": "The cervix", "correct": False,
             "why": "The cervix is the ring of muscle at the lower end of the "
                    "uterus, in the other system entirely."},
            {"text": "The sperm duct", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e04",
        "band": "easier",
        "text": "The lesson says the two systems genuinely pair up at one "
                "point only. Which pair is it?",
        "options": [
            {"text": "The penis and the vagina", "correct": False,
             "why": "Their jobs are related — one transfers gametes, the "
                    "other receives them — but they are not the same job, and "
                    "only one true pairing is named."},
            {"text": "The testes and the ovaries", "correct": True},
            {"text": "The uterus and the sperm duct", "correct": False,
             "why": "One holds and supplies an embryo for nine months, the "
                    "other is a transport tube. Nothing in the male system "
                    "corresponds to the uterus."},
            {"text": "The cervix and the glands", "correct": False,
             "why": "One is a ring of muscle keeping the uterus shut, the "
                    "other adds fluid to sperm. There is no shared job here "
                    "at all."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-01-s01",
        "band": "standard",
        "text": "An egg cell is released, is fertilised on the way, and then "
                "develops. In which order is it inside these structures?",
        "options": [
            {"text": "Ovary, then oviduct, then uterus", "correct": True},
            {"text": "Ovary, then uterus, then oviduct", "correct": False,
             "why": "The oviduct is the tube between the two, so the egg "
                    "cannot reach the uterus before it. Fertilisation happens "
                    "on the way, in the oviduct."},
            {"text": "Ovary, then cervix, then uterus", "correct": False,
             "why": "The cervix is the lower opening of the uterus. Sperm "
                    "pass through it coming in; the egg arrives from above "
                    "and never goes near it."},
            {"text": "Oviduct, then ovary, then uterus", "correct": False,
             "why": "The immature egg cells sit in the ovary from birth, so "
                    "the ovary is always where the journey starts."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s02",
        "band": "standard",
        "text": "One structure in these two systems has a job outside "
                "reproduction as well. Which structure, and what is that "
                "second job?",
        "options": [
            {"text": "The cervix — it also holds back urine from the bladder",
             "correct": False,
             "why": "The cervix closes the uterus, not the bladder. It has "
                    "one job, and it is a reproductive one."},
            {"text": "The testes — they also control body temperature",
             "correct": False,
             "why": "A muscle does move the testes to keep them cool, but "
                    "that is done for the sake of sperm production. It is "
                    "part of the reproductive job, not outside it."},
            {"text": "The penis — it also passes urine out of the body",
             "correct": True},
            {"text": "The glands — they also add fluid to urine as it passes",
             "correct": False,
             "why": "The urethra is shared, but the fluid the glands make has "
                    "one purpose: it goes into the semen."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s03",
        "band": "standard",
        "text": "A student writes: “The uterus does the same job as the "
                "sperm duct, because both are tubes that gametes pass "
                "through.” What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong — every structure in one system has a "
                     "partner in the other", "correct": False,
             "why": "This is the mirror-image idea the lesson is built to "
                    "break. Testes and ovaries pair up; after that the two "
                    "lists diverge completely."},
            {"text": "The uterus is not a transport tube, and the male system "
                     "has no equivalent of it", "correct": True},
            {"text": "The sperm duct is not a tube — it makes sperm cells as "
                     "well as moving them", "correct": False,
             "why": "The sperm duct really is a transport tube and nothing "
                    "more; sperm are made in the testes. The error in the "
                    "sentence is on the uterus’s side."},
            {"text": "The uterus is a tube, but it carries egg cells rather "
                     "than sperm cells", "correct": False,
             "why": "The oviduct is the tube that carries the egg. The uterus "
                    "is a muscular organ with a thick blood-rich lining — not "
                    "a tube at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s04",
        "band": "standard",
        "text": "The two gametes do not make the same journey. Which "
                "comparison is right?",
        "options": [
            {"text": "The egg swims up the oviduct while the sperm swim down "
                     "it", "correct": False,
             "why": "The egg does not swim — it has no tail. It is moved "
                    "along the oviduct by cilia and by muscle."},
            {"text": "Both travel about the same distance, meeting halfway "
                     "between them", "correct": False,
             "why": "They meet in the oviduct, which is close to the ovary "
                    "and a long way from where the sperm start. The two "
                    "journeys are nothing like equal."},
            {"text": "The egg travels further, because it starts further back "
                     "in the system", "correct": False,
             "why": "The egg is moved only a few centimetres along the "
                    "oviduct. Starting further back is not the same as "
                    "travelling further."},
            {"text": "The sperm travel about 15 cm; the egg only a few "
                     "centimetres", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-01-h01",
        "band": "harder",
        "text": "A baby is born with one testis still inside the abdomen, and "
                "surgeons move it into place during infancy. Why can it not "
                "be left where it is?",
        "options": [
            {"text": "Sperm made inside the body could not reach the sperm "
                     "duct", "correct": False,
             "why": "The plumbing is not the problem — a testis in the "
                    "abdomen is still connected. It is the temperature there "
                    "that stops sperm being made."},
            {"text": "Inside the body the testis would be too cold to make "
                     "sperm", "correct": False,
             "why": "That is the wrong way round. Inside is the warm place, "
                    "about 37 °C; sperm production works best a few "
                    "degrees cooler, around 34 °C."},
            {"text": "Inside the body, at about 37 °C, it would make no "
                     "sperm", "correct": True},
            {"text": "A testis inside the body would make egg cells instead",
             "correct": False,
             "why": "An organ’s job does not change with where it sits. "
                    "The testis stays a testis; at 37 °C it simply fails "
                    "to make sperm."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h02",
        "band": "harder",
        "text": "Whales and elephants keep their testes inside the body and "
                "still produce sperm perfectly well. What does that tell you?",
        "options": [
            {"text": "Cooling matters, but hanging the testes outside is only "
                     "one way to do it", "correct": True},
            {"text": "Sperm production does not really need to be cooler than "
                     "the body after all", "correct": False,
             "why": "It does. These animals cool the testes internally, using "
                    "blood returning from the skin — which is evidence that "
                    "the requirement is the same."},
            {"text": "Their sperm must be made somewhere other than in the "
                     "testes", "correct": False,
             "why": "Sperm are made in the testes in these animals too. What "
                    "differs is where the organ sits and how it is kept "
                    "cool."},
            {"text": "Their whole body must run below 34 °C, unlike "
                     "ours", "correct": False,
             "why": "They are mammals with a warm core, like us. The cooling "
                    "is local, done by blood coming back from the skin."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h03",
        "band": "harder",
        "text": "Biologists call the ovary the organ that runs out, and never "
                "say that about the testes. Why not?",
        "options": [
            {"text": "Egg cells get used up faster than sperm cells do",
             "correct": False,
             "why": "The opposite is true: about four hundred eggs are ever "
                    "released, against hundreds of millions of sperm a day. "
                    "Rate of use is not what runs the ovary down."},
            {"text": "The ovary is smaller, so it cannot store as many cells",
             "correct": False,
             "why": "Size is not the limit. A testis would run out too if it "
                    "could not make new sperm — the difference is that it "
                    "can."},
            {"text": "Egg cells are larger, so fewer of them fit inside the "
                     "ovary", "correct": False,
             "why": "Egg cells are larger, which is why they are expensive to "
                    "make. But the limit is that no new ones are ever made, "
                    "not that the ovary is full."},
            {"text": "The ovary’s stock was complete at birth; the "
                     "testes keep making more", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h04",
        "band": "harder",
        "text": "Three of the five jobs have no male structure at all against "
                "them. What do those three have in common?",
        "options": [
            {"text": "They all happen after fertilisation, so no organ is "
                     "needed for them", "correct": False,
             "why": "They need organs very much — a uterus, a cervix and a "
                    "placenta. And receiving a gamete happens before "
                    "fertilisation, not after."},
            {"text": "Each happens inside the body: receiving, then "
                     "protecting and supplying an embryo",
             "correct": True},
            {"text": "They are shared really, but the matching male "
                     "structures were just left off the table",
             "correct": False,
             "why": "There are no male structures to add. Expecting some is "
                    "the mirror-image idea, and this table exists to break "
                    "it."},
            {"text": "The male system is simply the smaller and simpler of "
                     "the two", "correct": False,
             "why": "Size is not the point. The male system has organs for "
                    "making, transporting, adding fluid and transferring — it "
                    "has no equivalents because nothing develops inside it."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-01-e05",
        "band": "easier",
        "text": "Where are the egg cells held before one of them is "
                "released?",
        "options": [
            {"text": "In the oviducts", "correct": False,
             "why": "The oviduct is the tube a released egg travels along. It "
                    "carries the egg towards the uterus; it never held the "
                    "stock."},
            {"text": "In the lining of the uterus", "correct": False,
             "why": "The lining is built to receive a fertilised egg, not to "
                    "keep unfertilised ones. No egg cell is ever stored "
                    "there."},
            {"text": "In the ovaries", "correct": True},
            {"text": "In the cervix", "correct": False,
             "why": "The cervix is the ring of muscle at the lower end of the "
                    "uterus. It is a doorway, not a store."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e06",
        "band": "easier",
        "text": "Which structure receives the semen when it is transferred "
                "from the male system?",
        "options": [
            {"text": "The vagina", "correct": True},
            {"text": "The uterus", "correct": False,
             "why": "The uterus is further in, beyond the cervix. Sperm pass "
                    "through it afterwards, but it is not where the transfer "
                    "happens."},
            {"text": "The oviduct", "correct": False,
             "why": "The oviduct is where the sperm are heading, about 15 cm "
                    "further on. It is the end of the journey, not the "
                    "start."},
            {"text": "The urethra", "correct": False,
             "why": "The urethra is the tube semen leaves the male system "
                    "through, so it sits on the other side of the transfer "
                    "entirely."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e07",
        "band": "easier",
        "text": "About how many immature egg cells are present in the ovaries "
                "of a newborn baby?",
        "options": [
            {"text": "None — they begin to be made at puberty", "correct": False,
             "why": "That is the sperm pattern applied to eggs. The whole "
                    "stock of immature egg cells is already there before "
                    "birth."},
            {"text": "About four hundred", "correct": False,
             "why": "About four hundred is roughly how many are ever released "
                    "across a lifetime. The stock they are drawn from is far "
                    "larger."},
            {"text": "Hundreds of millions", "correct": False,
             "why": "Hundreds of millions is the number of sperm cells "
                    "released at a time. Egg cells are never made in anything "
                    "like those numbers."},
            {"text": "About a million", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-01-s05",
        "band": "standard",
        "text": "Both oviducts of a person become completely blocked, and "
                "every other structure works normally. Which event can no "
                "longer happen, and why?",
        "options": [
            {"text": "Egg cells can no longer be released, because they have "
                     "nowhere to go", "correct": False,
             "why": "The ovary releases its egg whether the tube beyond it is "
                    "open or not. What is lost is what would have happened "
                    "next."},
            {"text": "Fertilisation, because the sperm and the egg can only "
                     "meet in the oviduct", "correct": True},
            {"text": "The lining of the uterus can no longer be built, "
                     "because nothing reaches it", "correct": False,
             "why": "The lining is built every cycle regardless of what "
                    "arrives. It is prepared in advance, not in response to "
                    "something."},
            {"text": "Sperm can no longer be made, because they have nowhere "
                     "to swim to", "correct": False,
             "why": "Sperm production happens in the testes, in the other "
                    "system entirely, and takes no notice of what is "
                    "happening here."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s06",
        "band": "standard",
        "text": "A student is asked what semen actually is. Which answer is "
                "right?",
        "options": [
            {"text": "Sperm cells together with the fluid added by the glands",
             "correct": True},
            {"text": "The fluid the glands make, before any sperm are added "
                     "to it", "correct": False,
             "why": "That fluid is only half of it. Semen is the fluid and "
                    "the sperm cells together, which is why the name applies "
                    "only after the two have met."},
            {"text": "Sperm cells alone, given a new name once they leave the "
                     "testes", "correct": False,
             "why": "Sperm cells on their own are just sperm cells. The name "
                    "changes because something has been added to them, not "
                    "because they have moved."},
            {"text": "Fluid made in the testes and carried along by the sperm "
                     "duct", "correct": False,
             "why": "The testes make sperm, not the fluid, and the sperm duct "
                    "only transports. The fluid is added further along, by "
                    "the glands."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s07",
        "band": "standard",
        "text": "Semen has been transferred into the vagina. Which two "
                "structures do the sperm pass through next, in order, on the "
                "way to the oviduct?",
        "options": [
            {"text": "The uterus, then the cervix", "correct": False,
             "why": "The right pair in the wrong order. The cervix is the "
                    "lower opening of the uterus, so it has to be passed "
                    "first."},
            {"text": "The urethra, then the uterus", "correct": False,
             "why": "The urethra belongs to the male system and the sperm "
                    "have already left it. Nothing on this journey goes back "
                    "through it."},
            {"text": "The cervix, then the uterus", "correct": True},
            {"text": "The ovary, then the oviduct", "correct": False,
             "why": "Sperm never enter an ovary. The egg comes out of the "
                    "ovary, and it is met in the tube beyond it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-01-h05",
        "band": "harder",
        "text": "Sperm are produced continuously at something like fifteen "
                "hundred a second, while an ovary releases about one egg cell "
                "a month. Which explanation of that difference fits both "
                "systems?",
        "options": [
            {"text": "Egg cells survive far longer than sperm cells do, so "
                     "fewer of them are needed", "correct": False,
             "why": "A released egg can be fertilised for roughly a day, "
                    "which is not long at all. How long a gamete lasts is not "
                    "what sets how many are made."},
            {"text": "An ovary is smaller than a testis, so it has less room "
                     "to work in", "correct": False,
             "why": "Size is not the limit. A testis of any size would still "
                    "be making new cells, and an ovary of any size would "
                    "still be releasing from a stock that is already "
                    "complete."},
            {"text": "The body makes exactly as many gametes as it is going "
                     "to use, and no more", "correct": False,
             "why": "Hundreds of millions of sperm are released for one "
                    "possible fertilisation, so almost all of them are "
                    "wasted. Nothing here is matched to need."},
            {"text": "An egg is expensive to build and a sperm is cheap, so "
                     "the numbers follow the cost", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h06",
        "band": "harder",
        "text": "The sperm duct and the oviduct have similar names. A student "
                "says both carry gametes towards the outside of the body. "
                "What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong — both of them lead out of the body",
             "correct": False,
             "why": "Only one of them does. The oviduct leads further in, "
                    "towards the uterus, which is where a developing embryo "
                    "has to end up."},
            {"text": "The oviduct carries the egg inwards, towards the "
                     "uterus, rather than out of the body", "correct": True},
            {"text": "The sperm duct carries sperm inwards, back towards the "
                     "testes", "correct": False,
             "why": "It runs the other way: from the testes towards the "
                    "urethra. Sperm are made in the testes, so that is where "
                    "the journey begins."},
            {"text": "The oviduct carries sperm rather than eggs, so it is "
                     "not an egg tube at all", "correct": False,
             "why": "Sperm do swim up the oviduct, and the egg is carried "
                    "down it. Its named job is carrying the egg, and it is "
                    "named for that."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h07",
        "band": "harder",
        "text": "Sperm cells are produced at roughly fifteen hundred per "
                "second. Roughly how many is that in one minute?",
        "options": [
            {"text": "About 25 sperm cells", "correct": False,
             "why": "This divides fifteen hundred by sixty. A rate per second "
                    "becomes a larger number per minute, not a smaller one."},
            {"text": "About 1500 sperm cells", "correct": False,
             "why": "That is the number for a single second. A minute is "
                    "sixty of them, so the figure has to be multiplied."},
            {"text": "About 90 000 sperm cells", "correct": True},
            {"text": "About 15 000 sperm cells", "correct": False,
             "why": "This multiplies by ten rather than by sixty. There are "
                    "sixty seconds in a minute, not ten."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ──────────────────────────────────────────
    #
    # Structure and function only: which organ, what it does, what follows
    # from what it does. Fertilisation is left to lesson 2 and the lining and
    # the cycle to lesson 3, so nothing here asks where fertilisation happens
    # (rung 1 owns that) or what the glands' sugar is for (rung 4 owns that).

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-01-e08",
        "band": "easier",
        "text": "Which organ makes the sperm cells?",
        "options": [
            {"text": "The sperm duct", "correct": False,
             "why": "A transport tube. It carries sperm away from where they "
                    "were made and makes none of its own."},
            {"text": "The glands", "correct": False,
             "why": "The glands add fluid to sperm that are already passing "
                    "them. They make no cells at all."},
            {"text": "The testes", "correct": True},
            {"text": "The urethra", "correct": False,
             "why": "The urethra is the tube semen leaves the body by. Nothing "
                    "is made anywhere along it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e09",
        "band": "easier",
        "text": "Which organ holds and supplies a developing embryo for nine "
                "months?",
        "options": [
            {"text": "The uterus", "correct": True},
            {"text": "The oviduct", "correct": False,
             "why": "The oviduct carries the egg towards the uterus. An embryo "
                    "passes along it early on, but it does not stay there."},
            {"text": "The cervix", "correct": False,
             "why": "The cervix is the ring of muscle at the lower end of the "
                    "uterus. It closes an organ; it holds nothing."},
            {"text": "The ovaries", "correct": False,
             "why": "The ovaries contain the egg cells and release one about "
                    "every month. Nothing develops inside them."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e10",
        "band": "easier",
        "text": "The oviduct goes by a second name as well. What is it?",
        "options": [
            {"text": "The sperm duct", "correct": False,
             "why": "That is the male system's transport tube, and it carries "
                    "sperm rather than egg cells."},
            {"text": "The cervix", "correct": False,
             "why": "The cervix is a structure of its own — the ring of muscle "
                    "at the lower end of the uterus."},
            {"text": "The birth canal", "correct": False,
             "why": "The birth canal is the vagina, at the far end of the "
                    "female system from the oviduct."},
            {"text": "The fallopian tube", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e11",
        "band": "easier",
        "text": "Which structure is the canal that a baby passes through at "
                "birth?",
        "options": [
            {"text": "The oviduct", "correct": False,
             "why": "The oviduct sits at the top of the female system, between "
                    "an ovary and the uterus. Nothing leaves the body along "
                    "it."},
            {"text": "The vagina", "correct": True},
            {"text": "The ovary", "correct": False,
             "why": "The ovary is where egg cells are held and released. It is "
                    "not on the route out of the body at all."},
            {"text": "The uterus", "correct": False,
             "why": "The uterus is the organ the baby leaves. The canal it "
                    "passes along comes after it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e12",
        "band": "easier",
        "text": "From what point in life do the testes make sperm cells?",
        "options": [
            {"text": "From before birth, so the whole stock is ready at birth",
             "correct": False,
             "why": "That is the pattern for egg cells, not sperm. The testes "
                    "start later and then keep going."},
            {"text": "From birth onwards, at a steady rate for life",
             "correct": False,
             "why": "Production has not begun at birth. It starts at puberty, "
                    "and from then on it is continuous."},
            {"text": "From puberty onwards, continuously", "correct": True},
            {"text": "From puberty onwards, once each month",
             "correct": False,
             "why": "About once a month is how often an ovary releases an egg "
                    "cell. Sperm production does not work in monthly rounds."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e13",
        "band": "easier",
        "text": "How often does an ovary release an egg cell?",
        "options": [
            {"text": "About once a month", "correct": True},
            {"text": "About once a week", "correct": False,
             "why": "Four times too often. About four hundred egg cells are "
                    "released in a whole lifetime, which is nothing like "
                    "weekly."},
            {"text": "Continuously", "correct": False,
             "why": "Continuous production is the sperm pattern. An ovary "
                    "releases one egg cell at a time, about a month apart."},
            {"text": "About once a year", "correct": False,
             "why": "Twelve times too seldom. That would give about a dozen "
                    "egg cells in a lifetime rather than about four hundred."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e14",
        "band": "easier",
        "text": "What does the word gamete mean?",
        "options": [
            {"text": "A fertilised egg cell, before it starts to divide",
             "correct": False,
             "why": "That is a single cell formed from two gametes. The word "
                    "names the cells that fuse, not what they become."},
            {"text": "Any cell of the reproductive system", "correct": False,
             "why": "Most of the cells in those organs are ordinary body "
                    "cells. Only the sex cells are gametes."},
            {"text": "The fluid the glands add to the sperm cells",
             "correct": False,
             "why": "That fluid, together with sperm, makes semen. A gamete is "
                    "a cell, not a fluid."},
            {"text": "A sex cell: a sperm cell or an egg cell", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e15",
        "band": "easier",
        "text": "The cervix is made of what?",
        "options": [
            {"text": "A ring of cilia", "correct": False,
             "why": "Cilia move the egg along the oviduct. They are far too "
                    "small to hold an organ shut."},
            {"text": "A ring of muscle", "correct": True},
            {"text": "A blood-rich lining", "correct": False,
             "why": "The lining is inside the uterus above it. The cervix is "
                    "the muscular ring at the uterus's lower end."},
            {"text": "A pouch of skin", "correct": False,
             "why": "A pouch of skin holds the testes outside the body cavity, "
                    "in the other system altogether."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e16",
        "band": "easier",
        "text": "Roughly how many egg cells ever finish maturing and are "
                "released across one lifetime?",
        "options": [
            {"text": "About four hundred", "correct": True},
            {"text": "About a million", "correct": False,
             "why": "About a million is the stock of immature egg cells "
                    "present at birth. Only a tiny share of them is ever "
                    "released."},
            {"text": "About four thousand", "correct": False,
             "why": "Ten times too many. At one a month, four thousand would "
                    "take more than three hundred years."},
            {"text": "Hundreds of millions", "correct": False,
             "why": "Hundreds of millions is a count of sperm cells, and of "
                    "sperm released at one time at that."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e17",
        "band": "easier",
        "text": "The urethra carries two different things out of the body. "
                "Which two?",
        "options": [
            {"text": "Semen and blood", "correct": False,
             "why": "Nothing carries blood out of either reproductive system. "
                    "The second thing the urethra carries is urine."},
            {"text": "Urine and egg cells", "correct": False,
             "why": "Egg cells belong to the female system, which has no "
                    "urethra in it at all. Sperm and urine share this tube."},
            {"text": "Semen and urine", "correct": True},
            {"text": "Semen and the fluid the glands make", "correct": False,
             "why": "The glands' fluid is already part of the semen by then, "
                    "so that is one thing rather than two."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e18",
        "band": "easier",
        "text": "Where in the body are the testes held?",
        "options": [
            {"text": "Inside the abdomen, beside the bladder",
             "correct": False,
             "why": "A testis left inside the abdomen makes no sperm, which is "
                    "why an undescended one is moved surgically in infancy."},
            {"text": "Inside the body cavity, high up behind the glands",
             "correct": False,
             "why": "Anywhere inside the body cavity is too warm. The whole "
                    "point of their position is that it runs cooler."},
            {"text": "Inside the body cavity, just below the sperm ducts",
             "correct": False,
             "why": "The sperm ducts run up past the body cavity line from the "
                    "testes, so the testes are below it and outside."},
            {"text": "Outside the body cavity, in a pouch of skin",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e19",
        "band": "easier",
        "text": "Sperm production works best at roughly what temperature?",
        "options": [
            {"text": "Around 20 °C", "correct": False,
             "why": "That is room temperature, well below anything inside a "
                    "human body. The testes run a few degrees under core "
                    "temperature, not twenty."},
            {"text": "Around 34 °C", "correct": True},
            {"text": "Around 37 °C", "correct": False,
             "why": "37 °C is core body temperature, and that is the "
                    "temperature at which sperm production fails."},
            {"text": "Around 40 °C", "correct": False,
             "why": "Warmer than the body core, and the wrong direction "
                    "entirely. Sperm production needs the testes cooler than "
                    "the body, not hotter."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e20",
        "band": "easier",
        "text": "Which one of these structures belongs to the female system?",
        "options": [
            {"text": "The oviduct", "correct": True},
            {"text": "The sperm duct", "correct": False,
             "why": "The sperm duct carries sperm from the testes towards the "
                    "urethra, so it is male. The similar name is the trap."},
            {"text": "The glands", "correct": False,
             "why": "The glands add the fluid that, with sperm, makes semen. "
                    "There is nothing matching them on the female side."},
            {"text": "The penis", "correct": False,
             "why": "The penis transfers semen into the vagina, so it is the "
                    "male half of that one event."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e21",
        "band": "easier",
        "text": "When is the stock of immature egg cells in the ovaries "
                "complete?",
        "options": [
            {"text": "At puberty, when the first one is released",
             "correct": False,
             "why": "Puberty is when releasing starts, not when the stock is "
                    "built. The stock was finished long before that."},
            {"text": "It is never complete, because new ones are added each "
                     "month", "correct": False,
             "why": "None is ever added. The ovaries contain egg cells rather "
                    "than making them, and the count only falls."},
            {"text": "Before birth — no more are made afterwards",
             "correct": True},
            {"text": "At birth, when the ovaries make their first batch",
             "correct": False,
             "why": "They are already there at birth, made earlier still. The "
                    "ovary makes no batch at any point."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e22",
        "band": "easier",
        "text": "How many of the five jobs of reproduction does the female "
                "system do?",
        "options": [
            {"text": "Two of them", "correct": False,
             "why": "Two is how many jobs are SHARED. The female system also "
                    "receives a gamete, protects an embryo and supplies it."},
            {"text": "Three of them", "correct": False,
             "why": "Three is how many jobs the female system does alone, not "
                    "how many it does altogether."},
            {"text": "Four of them", "correct": False,
             "why": "Supplying a developing embryo is on the female side of "
                    "the table as well, so nothing in the list is missing."},
            {"text": "All five of them", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e23",
        "band": "easier",
        "text": "The uterus is a muscular organ. What lines the inside of it?",
        "options": [
            {"text": "A ring of muscle that opens for birth",
             "correct": False,
             "why": "That is the cervix, at the uterus's lower end, and it is "
                    "a structure in its own right rather than a lining."},
            {"text": "A thick lining, rich in blood", "correct": True},
            {"text": "Cilia, which sweep the egg cell along", "correct": False,
             "why": "Cilia line the oviduct and move the egg towards the "
                    "uterus. They are not what the uterus is lined with."},
            {"text": "A layer of stored fluid from the glands",
             "correct": False,
             "why": "The glands' fluid is part of semen and is made in the "
                    "male system. Nothing of it is stored here."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e24",
        "band": "easier",
        "text": "One of the five jobs of reproduction is done by both systems. "
                "Which job is it?",
        "options": [
            {"text": "Making gametes", "correct": True},
            {"text": "Receiving a gamete", "correct": False,
             "why": "Only the female system receives one. The male system has "
                    "no structure for it, because it never receives anything."},
            {"text": "Protecting a developing embryo", "correct": False,
             "why": "The uterus does this, and the male system has no "
                    "equivalent of the uterus at all."},
            {"text": "Supplying a developing embryo", "correct": False,
             "why": "Nothing develops inside the male system, so nothing there "
                    "has to be supplied."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e25",
        "band": "easier",
        "text": "Which structure sits between the vagina and the uterus?",
        "options": [
            {"text": "The oviduct", "correct": False,
             "why": "The oviduct is on the far side of the uterus, joining it "
                    "to an ovary. It is nowhere near the vagina."},
            {"text": "The ovary", "correct": False,
             "why": "The ovaries sit at the outer ends of the oviducts, at the "
                    "top of the system rather than at its base."},
            {"text": "The cervix", "correct": True},
            {"text": "The urethra", "correct": False,
             "why": "The urethra belongs to the male system, and carries urine "
                    "and semen rather than joining two female organs."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e26",
        "band": "easier",
        "text": "What does each of the two gamete-making organs do with "
                "gametes?",
        "options": [
            {"text": "The testes release stored sperm; the ovaries make "
                     "them", "correct": False,
             "why": "Exactly the wrong way round. The testes make sperm, and "
                    "the ovaries release egg cells from a stock they hold."},
            {"text": "Both organs store gametes that were made before birth",
             "correct": False,
             "why": "Only the ovaries hold a stock from before birth. The "
                    "testes make new sperm cells continuously."},
            {"text": "Both organs make new gametes from puberty onwards",
             "correct": False,
             "why": "The testes do. The ovaries make none: they contain the "
                    "egg cells and release them."},
            {"text": "The testes make sperm cells; the ovaries release egg "
                     "cells", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e27",
        "band": "easier",
        "text": "For roughly how long does the cervix keep the uterus closed "
                "while an embryo develops?",
        "options": [
            {"text": "About a month", "correct": False,
             "why": "A month is about the gap between one egg cell being "
                    "released and the next. Development takes nine of them."},
            {"text": "About nine months", "correct": True},
            {"text": "About five days", "correct": False,
             "why": "Five days is roughly how long a fertilised egg takes to "
                    "reach the uterus, before the nine months even begin."},
            {"text": "About a fortnight", "correct": False,
             "why": "Far too short. The uterus holds and supplies a developing "
                    "embryo for nine months, and stays shut throughout."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e28",
        "band": "easier",
        "text": "In cold conditions, what happens to the testes?",
        "options": [
            {"text": "A muscle raises them closer to the body",
             "correct": True},
            {"text": "They are drawn back inside the body cavity",
             "correct": False,
             "why": "They are never taken inside the cavity. Inside is 37 °C, "
                    "and at that temperature they would make no sperm."},
            {"text": "They stop making sperm until it is warmer",
             "correct": False,
             "why": "Production is continuous. Being cool is the condition it "
                    "needs, not something that interrupts it."},
            {"text": "They hang further away from the body", "correct": False,
             "why": "That is what happens in warm conditions, to lose heat. "
                    "Cold calls for the opposite move."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e29",
        "band": "easier",
        "text": "Which one of the five jobs has no male structure listed "
                "against it?",
        "options": [
            {"text": "Making gametes", "correct": False,
             "why": "The testes do this from puberty onwards, and it is the "
                    "one job at which the two systems genuinely pair up."},
            {"text": "Delivering gametes", "correct": False,
             "why": "The sperm duct, the glands and the penis all do this. The "
                    "job is shared, though the two systems do it differently."},
            {"text": "Protecting a developing embryo", "correct": True},
            {"text": "Transferring gametes into the other system",
             "correct": False,
             "why": "That is the penis's job, and it is the male half of the "
                    "transfer. Nothing about it is missing."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-e30",
        "band": "easier",
        "text": "After leaving a testis, which two structures does a sperm "
                "cell pass along, in order?",
        "options": [
            {"text": "The urethra, then the sperm duct", "correct": False,
             "why": "The right pair in the wrong order. The sperm duct leads "
                    "towards the urethra, so it comes first."},
            {"text": "The oviduct, then the urethra", "correct": False,
             "why": "The oviduct is in the female system and carries egg "
                    "cells. No sperm passes along it inside the male system."},
            {"text": "The sperm duct, then the cervix", "correct": False,
             "why": "The cervix is in the female system, and a sperm reaches "
                    "it only after it has left the male system entirely."},
            {"text": "The sperm duct, then the urethra", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-01-s08",
        "band": "standard",
        "text": "The testes already make the sperm cells. So why does the male "
                "system need glands as well?",
        "options": [
            {"text": "Because the glands finish off sperm cells that leave the "
                     "testes only half made, adding the tail to each one",
             "correct": False,
             "why": "A sperm leaves a testis complete, tail and all. Nothing is "
                    "added to the cell itself further along the route."},
            {"text": "Because sperm cannot travel on their own, and the fluid "
                     "gives them something to swim in", "correct": True},
            {"text": "Because the fluid protects the sperm cells from the "
                     "urine that shares the urethra with them",
             "correct": False,
             "why": "The urethra is a shared route, not a shared moment. The "
                    "fluid is there so the sperm can move."},
            {"text": "Because the glands store the sperm cells until they are "
                     "transferred", "correct": False,
             "why": "The glands add fluid to sperm already passing them. They "
                    "hold nothing back and store nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s09",
        "band": "standard",
        "text": "Explain why the testes are held outside the body cavity "
                "rather than inside it.",
        "options": [
            {"text": "There is no room for them inside, once the bladder and "
                     "the glands are in place", "correct": False,
             "why": "Space is not the reason, and other mammals fit theirs "
                    "inside comfortably. Temperature is what decides it."},
            {"text": "Sperm cells have to leave the body quickly, and the "
                     "shortest route is from outside", "correct": False,
             "why": "The sperm duct runs up into the body cavity and back down "
                    "again, so the route is not short at all."},
            {"text": "Outside they are easier for a muscle to move up and "
                     "down as needed", "correct": False,
             "why": "The muscle exists to keep them at the right temperature. "
                    "Being movable is how the reason is served, not the reason."},
            {"text": "Sperm production works best a few degrees below core "
                     "body temperature", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s10",
        "band": "standard",
        "text": "A muscle pulls the testes towards the body in cold weather "
                "and lets them hang further away in hot weather. What is that "
                "muscle doing?",
        "options": [
            {"text": "Holding the testes at a steady temperature a few degrees "
                     "below the body's core", "correct": True},
            {"text": "Protecting the testes from being knocked while a person "
                     "moves about", "correct": False,
             "why": "Protection would not depend on the weather. A response "
                    "that tracks temperature is about temperature."},
            {"text": "Pushing sperm cells along the sperm duct towards the "
                     "urethra", "correct": False,
             "why": "The sperm duct carries sperm along. This muscle moves the "
                    "whole organ rather than anything inside it."},
            {"text": "Warming the testes back up to core body temperature",
             "correct": False,
             "why": "Core temperature, 37 °C, is where production fails. The "
                    "muscle keeps them below it, not at it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s11",
        "band": "standard",
        "text": "The cervix has to do two opposite things across a pregnancy. "
                "What are they?",
        "options": [
            {"text": "It thickens for nine months, then thins out as the baby "
                     "passes", "correct": False,
             "why": "Thickening describes the lining inside the uterus. The "
                    "cervix is a ring of muscle, and its job is opening and "
                    "closing."},
            {"text": "It opens to let sperm in, then closes again the moment "
                     "an embryo implants", "correct": False,
             "why": "Sperm pass through a cervix that is not held open for "
                    "them, and closing is what it does for the whole nine "
                    "months."},
            {"text": "It stays shut for nine months, then opens over hours "
                     "during birth", "correct": True},
            {"text": "It holds the embryo in place, then releases it when the "
                     "uterus contracts", "correct": False,
             "why": "The embryo is held by the uterus, well above the cervix. "
                    "The cervix closes the way out rather than gripping "
                    "anything."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s12",
        "band": "standard",
        "text": "Why does the lesson say that nothing in the male system "
                "corresponds to the uterus?",
        "options": [
            {"text": "Because the male system is smaller, so its organs have "
                     "to do more than one job each", "correct": False,
             "why": "Size decides nothing here. Each male structure has its "
                    "own single job, and none of them is holding an embryo."},
            {"text": "Because no male structure has to hold and supply another "
                     "organism for nine months", "correct": True},
            {"text": "Because the uterus is a muscular organ, and the male "
                     "system contains no muscle at all", "correct": False,
             "why": "The male system has muscle in it — the one that moves the "
                    "testes, for a start. It is the job that has no match, not "
                    "the tissue."},
            {"text": "Because the uterus was left off the list of five jobs "
                     "the two systems share", "correct": False,
             "why": "The uterus is in the list, at jobs 4 and 5. What is "
                    "missing is anything male to write beside it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s13",
        "band": "standard",
        "text": "One structure of the female system has two jobs at opposite "
                "ends of the nine months. Which structure, and what are they?",
        "options": [
            {"text": "The uterus — it receives the semen, and then holds the "
                     "developing embryo", "correct": False,
             "why": "Semen is received lower down, and the uterus is where the "
                    "embryo develops. Only one of the two is its job."},
            {"text": "The cervix — it lets sperm through, and then supplies "
                     "the embryo until birth", "correct": False,
             "why": "The cervix supplies nothing. It closes the lower end of "
                    "the uterus and opens during birth."},
            {"text": "The oviduct — it carries the egg cell, and then carries "
                     "the baby out", "correct": False,
             "why": "Nothing leaves the body along an oviduct. It runs between "
                    "an ovary and the uterus and goes nowhere else."},
            {"text": "The vagina — it receives semen, and it is the canal a "
                     "baby passes through", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s14",
        "band": "standard",
        "text": "Which structure does a sperm cell pass along last, on its way "
                "out of the male system?",
        "options": [
            {"text": "The urethra, which runs out through the penis",
             "correct": True},
            {"text": "The sperm duct, which runs up from a testis",
             "correct": False,
             "why": "The sperm duct comes earlier, carrying sperm from a "
                    "testis towards the urethra."},
            {"text": "The glands, which add fluid on the way past",
             "correct": False,
             "why": "The glands sit part way along the route and add fluid. "
                    "There is a tube to travel along after them."},
            {"text": "The testes, where the sperm cell was made",
             "correct": False,
             "why": "The testes are where the journey starts, not where it "
                    "ends. Sperm are made there and leave from there."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s15",
        "band": "standard",
        "text": "Both systems deliver a gamete, but only one of them delivers "
                "into the other body. Which does, and where is the other "
                "system's gamete delivered to?",
        "options": [
            {"text": "The female system delivers into the male; the sperm are "
                     "carried to the urethra", "correct": False,
             "why": "Nothing passes from the female system into the male one. "
                    "The transfer runs one way."},
            {"text": "Both deliver into the other; the two gametes are "
                     "exchanged between the systems", "correct": False,
             "why": "There is no exchange. Sperm cross into the female system, "
                    "and the egg never leaves it."},
            {"text": "The male system delivers into the female; the egg is "
                     "moved along the oviduct", "correct": True},
            {"text": "The male system delivers into the female; the egg is "
                     "carried down into the cervix", "correct": False,
             "why": "The egg is moved the other way, from the ovary along the "
                    "oviduct. It never travels as far down as the cervix."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s16",
        "band": "standard",
        "text": "A student lists the male structures in the order a sperm cell "
                "meets them: glands, testes, sperm duct, penis. What is wrong "
                "with the list?",
        "options": [
            {"text": "The penis should come before the glands, because the "
                     "fluid is added last", "correct": False,
             "why": "The fluid is added before the transfer, not after it. The "
                    "penis is genuinely last in the list."},
            {"text": "The testes should come first, because sperm cells are "
                     "made there", "correct": True},
            {"text": "The sperm duct should come first, because it collects "
                     "the sperm before they are made", "correct": False,
             "why": "Nothing is collected before it exists. The duct carries "
                    "sperm away from the testes that made them."},
            {"text": "Nothing is wrong: a sperm cell really does pass the "
                     "glands before the testes", "correct": False,
             "why": "It cannot. A sperm cell starts life inside a testis, so "
                    "the testis is where its route begins."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s17",
        "band": "standard",
        "text": "The sperm travel about 15 cm, while the egg cell is moved "
                "only a few centimetres. Why is the egg's journey so much "
                "shorter?",
        "options": [
            {"text": "Because the egg cell is far larger, so it cannot be "
                     "moved as far", "correct": False,
             "why": "Size is not the limit: the egg is moved by cilia and "
                    "muscle, which could carry it the length of the tube."},
            {"text": "Because the egg cell is released only once the sperm "
                     "have arrived nearby", "correct": False,
             "why": "Release happens whether or not any sperm are present. The "
                    "two events are not timed against each other."},
            {"text": "Because the two meet in the oviduct, which is close to "
                     "the ovary the egg started from", "correct": True},
            {"text": "Because the egg cell travels for a few hours and the "
                     "sperm travel for several days", "correct": False,
             "why": "How long each takes is a separate question. The reason "
                    "the distances differ is where in the system they meet."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s18",
        "band": "standard",
        "text": "A student says that because the penis carries urine, urine "
                "must be part of semen. What is wrong with that?",
        "options": [
            {"text": "They share the urethra as a route, but the fluid in "
                     "semen comes from the glands", "correct": True},
            {"text": "Urine is made in the testes alongside the sperm, so it "
                     "is kept well apart from them there", "correct": False,
             "why": "Urine comes from the bladder, which has no reproductive "
                    "job at all. The testes make sperm and nothing else."},
            {"text": "The penis carries urine along a tube of its own, quite "
                     "separate from the urethra", "correct": False,
             "why": "There is one tube, and both things use it. That is "
                    "exactly why the confusion arises."},
            {"text": "Urine is part of semen, but only in very small amounts",
             "correct": False,
             "why": "None of it is. Semen is sperm cells together with the "
                    "fluid the glands add, and nothing else."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s19",
        "band": "standard",
        "text": "Sperm cells are still made normally in the testes, but they "
                "cannot pass along either sperm duct. Which of the five jobs "
                "has failed?",
        "options": [
            {"text": "Making gametes, because sperm that go nowhere are not "
                     "counted as made", "correct": False,
             "why": "They have been made, in the testes, exactly as before. "
                    "What has failed is what happens to them next."},
            {"text": "Protecting a developing embryo, because none can now be "
                     "started", "correct": False,
             "why": "That job belongs to the uterus, in the other system. A "
                    "blocked duct does not change what the uterus does."},
            {"text": "Delivering gametes, because the sperm cannot reach the "
                     "route out", "correct": True},
            {"text": "Receiving a gamete, because nothing arrives to be "
                     "received", "correct": False,
             "why": "Receiving is the female system's job, and it is the male "
                    "system that has the blockage."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s20",
        "band": "standard",
        "text": "An ovary releases about one egg cell a month. Roughly how "
                "many is that over ten years?",
        "options": [
            {"text": "About 10", "correct": False,
             "why": "That is one a year rather than one a month. Ten years at "
                    "twelve a year gives about 120."},
            {"text": "About 120", "correct": True},
            {"text": "About 520", "correct": False,
             "why": "This counts one a week. The rate is monthly, so ten years "
                    "gives about 120."},
            {"text": "About 1200", "correct": False,
             "why": "Ten times too many — a hundred a year rather than twelve. "
                    "Only about four hundred are released in a whole lifetime."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s21",
        "band": "standard",
        "text": "Delivering a gamete takes three structures in the male system "
                "and one in the female system. Which three are the male ones?",
        "options": [
            {"text": "The testes, the sperm duct and the urethra",
             "correct": False,
             "why": "The testes make the gametes rather than deliver them, and "
                    "that is a different job in the list."},
            {"text": "The sperm duct, the urethra and the bladder",
             "correct": False,
             "why": "The bladder has no reproductive job. It stores urine and "
                    "happens to share the tube out."},
            {"text": "The testes, the glands and the penis", "correct": False,
             "why": "Two of the three are right. The testes belong to making "
                    "gametes; the sperm duct is the one that carries them."},
            {"text": "The sperm duct, the glands and the penis",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s22",
        "band": "standard",
        "text": "The cervix is part of the same organ as the uterus. Why is it "
                "counted as a structure of its own?",
        "options": [
            {"text": "Because it has a job of its own: closing the uterus, and "
                     "opening for birth", "correct": True},
            {"text": "Because it is made of muscle, and the rest of the uterus "
                     "is not", "correct": False,
             "why": "The uterus is muscular too. What separates the cervix is "
                    "what it does, not what it is made of."},
            {"text": "Because it belongs to the vagina rather than to the "
                     "uterus", "correct": False,
             "why": "It is the uterus's own lower end. Being named separately "
                    "does not move it into the next structure along."},
            {"text": "Because it is the only part of the female system sperm "
                     "pass through", "correct": False,
             "why": "Sperm pass through the vagina, the cervix, the uterus and "
                    "into an oviduct. The cervix is one of four."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s23",
        "band": "standard",
        "text": "The uterus is described as having muscular walls, a "
                "blood-rich lining and a cervix that stays shut. Which job do "
                "those three features add up to?",
        "options": [
            {"text": "Making a gamete ready to be released", "correct": False,
             "why": "Gametes are made and released in the ovaries. The uterus "
                    "takes no part in it."},
            {"text": "Delivering a gamete towards the place it is needed",
             "correct": False,
             "why": "Delivering is the oviduct's part of the story on this "
                    "side, and the sperm duct's on the other."},
            {"text": "Protecting a developing embryo", "correct": True},
            {"text": "Receiving a gamete from the other system",
             "correct": False,
             "why": "Receiving happens at the vagina, below the cervix. By "
                    "then the sperm are on their way through."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s24",
        "band": "standard",
        "text": "Receiving a gamete is listed as a female-only job. Why does "
                "the male system need no structure for it?",
        "options": [
            {"text": "Because the male system receives one earlier, inside the "
                     "testes", "correct": False,
             "why": "Nothing arrives in a testis from outside. Sperm are made "
                    "there and leave from there."},
            {"text": "Because the male system only ever transfers gametes out, "
                     "and never takes one in", "correct": True},
            {"text": "Because the urethra does the job, taking in gametes as "
                     "well as passing them out", "correct": False,
             "why": "The urethra carries semen and urine out. Nothing travels "
                    "in along it."},
            {"text": "Because receiving a gamete is not really a job, so "
                     "neither system has a structure for it", "correct": False,
             "why": "It is a job, and the vagina and cervix do it. The point "
                    "is that only one system has to."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s25",
        "band": "standard",
        "text": "The lesson says the two systems solve two different halves of "
                "one problem. Which pair of halves is it?",
        "options": [
            {"text": "One half makes both gametes, and the other half stores "
                     "them until needed", "correct": False,
             "why": "Both systems have gametes of their own, and neither "
                    "stores the other's. Making is a shared job, not a half."},
            {"text": "One half deals with the gametes, and the other half "
                     "deals with the embryo", "correct": False,
             "why": "The female system does both: it delivers a gamete and "
                    "then holds the embryo. The split is not there."},
            {"text": "One half has to get a gamete out and across, and the "
                     "other has to take one in and hold the result",
             "correct": True},
            {"text": "One half does the work before fertilisation, and the "
                     "other does the work after it", "correct": False,
             "why": "The female system is busy on both sides of "
                    "fertilisation — moving the egg beforehand, holding the "
                    "embryo afterwards."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s26",
        "band": "standard",
        "text": "Semen has two parts, and they come from two different "
                "structures. Which two?",
        "options": [
            {"text": "Sperm cells from the testes, and fluid from the glands",
             "correct": True},
            {"text": "Sperm cells from the sperm duct, and fluid from the "
                     "testes", "correct": False,
             "why": "The duct carries sperm rather than making them, and the "
                    "testes make no fluid."},
            {"text": "Sperm cells from the testes, and fluid from the bladder",
             "correct": False,
             "why": "The bladder holds urine and has no reproductive job. The "
                    "fluid in semen is made by the glands."},
            {"text": "Sperm cells from the glands, and fluid from the sperm "
                     "duct", "correct": False,
             "why": "Both halves are swapped. The glands make the fluid and "
                    "the duct is a transport tube."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s27",
        "band": "standard",
        "text": "Which of these would stop sperm cells being made, rather than "
                "stop them being delivered?",
        "options": [
            {"text": "A sperm duct that is completely blocked along its "
                     "length", "correct": False,
             "why": "Production carries on in the testis behind the blockage. "
                    "It is the route out that has gone."},
            {"text": "Glands that add no fluid to the sperm cells at all",
             "correct": False,
             "why": "The sperm exist; what they lack is something to swim in. "
                    "That is a delivery problem."},
            {"text": "A testis held inside the body at 37 °C", "correct": True},
            {"text": "A urethra that is blocked where the sperm duct joins it",
             "correct": False,
             "why": "The testes go on making sperm regardless. Again it is the "
                    "way out that has failed."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s28",
        "band": "standard",
        "text": "Which two of the five jobs are shared between the two "
                "systems?",
        "options": [
            {"text": "Making gametes and protecting an embryo",
             "correct": False,
             "why": "Protecting an embryo is female only — the male system has "
                    "no equivalent of the uterus."},
            {"text": "Making gametes and delivering gametes", "correct": True},
            {"text": "Delivering gametes and receiving a gamete",
             "correct": False,
             "why": "Receiving is female only. The male system never takes a "
                    "gamete in."},
            {"text": "Receiving a gamete and supplying an embryo",
             "correct": False,
             "why": "Both of those are female only, so neither of them is "
                    "shared with anything."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s29",
        "band": "standard",
        "text": "A high fever holds someone's whole body several degrees above "
                "its usual temperature for a week. Suggest why sperm "
                "production might fall.",
        "options": [
            {"text": "The sperm cells would be washed out of the testes "
                     "faster than they could be replaced", "correct": False,
             "why": "Nothing about a fever moves sperm along the duct. The "
                    "effect is on where they are made."},
            {"text": "The muscle holding the testes would stop working while "
                     "the body was unwell", "correct": False,
             "why": "The muscle may well go on responding. The trouble is that "
                    "the body it is holding them near is itself too warm."},
            {"text": "The testes would be held above the temperature at which "
                     "production works", "correct": True},
            {"text": "The glands would make less fluid, so fewer sperm cells "
                     "would be made", "correct": False,
             "why": "The fluid is added after the sperm are made, and how much "
                    "there is does not change the number produced."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-s30",
        "band": "standard",
        "text": "Taking the five jobs together, how do the two systems differ "
                "in what they have to do?",
        "options": [
            {"text": "The male system makes and delivers a gamete; the female "
                     "system also receives one and keeps the embryo",
             "correct": True},
            {"text": "The male system makes a gamete; the female system "
                     "delivers it and then keeps the embryo", "correct": False,
             "why": "Delivering is shared. The male system moves its gamete "
                    "out and transfers it across."},
            {"text": "The male system delivers a gamete; the female system "
                     "makes one and then keeps and supplies the embryo for "
                     "nine months", "correct": False,
             "why": "Making is shared as well: the testes make sperm and the "
                    "ovaries hold and release egg cells."},
            {"text": "Both systems make, deliver and receive a gamete, and "
                     "both of them then protect the embryo they have started",
             "correct": False,
             "why": "Receiving is female only, and so is protecting. The male "
                    "system has no structure for either, because nothing is "
                    "received by it and nothing develops inside it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-01-h08",
        "band": "harder",
        "text": "The lesson gives two figures for sperm production: about "
                "fifteen hundred a second, and over a hundred million a day. "
                "Which calculation shows that the two agree?",
        "options": [
            {"text": "1500 × 60 × 24, which comes to a little over 2 million",
             "correct": False,
             "why": "This turns seconds straight into hours. There are sixty "
                    "seconds in a minute and sixty minutes in an hour, so one "
                    "step has been missed."},
            {"text": "1500 × 60 × 60, which comes to about 5 million",
             "correct": False,
             "why": "That is one hour's worth. A day is twenty-four of them, "
                    "and the figure to reach is a daily one."},
            {"text": "1500 × 60 × 60 × 24, which comes to about 130 million",
             "correct": True},
            {"text": "1500 × 24, which comes to about 36 thousand",
             "correct": False,
             "why": "This treats the rate as fifteen hundred an hour. It is "
                    "fifteen hundred a second, which is 3600 times faster."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h09",
        "band": "harder",
        "text": "In some animals the gametes meet outside the body, in water. "
                "Which of the five jobs would such an animal still need?",
        "options": [
            {"text": "Making gametes and delivering them, but not receiving, "
                     "protecting or supplying one inside the body",
             "correct": True},
            {"text": "All five, because every animal that reproduces has to "
                     "do all five somewhere", "correct": False,
             "why": "Three of the five are about what happens inside a body. "
                    "An animal whose young develop outside one does none of "
                    "them."},
            {"text": "Receiving and protecting, but not making or delivering "
                     "gametes", "correct": False,
             "why": "This is upside down. Gametes still have to be made and "
                    "released; it is the inside-the-body jobs that go."},
            {"text": "Making gametes only, because water does the delivering "
                     "for the animal", "correct": False,
             "why": "The gametes still have to be released into the water, and "
                    "releasing them is what delivering means here."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h10",
        "band": "harder",
        "text": "Sperm production fails at 37 °C and works at 34 °C. A student "
                "concludes that all human cells work better a few degrees "
                "cool. Evaluate that conclusion.",
        "options": [
            {"text": "It is right, which is why a fever makes a person feel so "
                     "unwell", "correct": False,
             "why": "A fever has its own causes. It is not evidence that the "
                    "body's ordinary working temperature is too warm for it."},
            {"text": "It is right, and it explains why the testes are the "
                     "organ held furthest from the core", "correct": False,
             "why": "The testes are the exception, not the rule. Nothing "
                    "follows from one organ to all the others."},
            {"text": "It cannot be judged, because no temperature is given for "
                     "any other organ", "correct": False,
             "why": "One temperature for the others is given: 37 °C is the "
                    "core, and that is where the rest of the body works."},
            {"text": "It is wrong: the rest of the body works at 37 °C, and "
                     "sperm production is the exception", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h11",
        "band": "harder",
        "text": "The urethra becomes blocked. Name the two things that can no "
                "longer leave the body, one reproductive and one not.",
        "options": [
            {"text": "Sperm cells and the glands' fluid, which travel out "
                     "along separate tubes", "correct": False,
             "why": "By the urethra they are one thing, semen, and they share "
                    "one tube. Neither of them is the job outside "
                    "reproduction."},
            {"text": "Semen, and urine from the bladder", "correct": True},
            {"text": "Semen, and the fluid the glands add to it",
             "correct": False,
             "why": "The glands' fluid is already part of the semen, so that "
                    "counts two things once. The other is urine."},
            {"text": "Urine from the bladder, and egg cells from the ovary",
             "correct": False,
             "why": "Egg cells are in the other system entirely, and never "
                    "come near a urethra."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h12",
        "band": "harder",
        "text": "A student writes a rule: “Every structure in one system has a "
                "partner in the other, except the uterus.” Why is the rule "
                "still wrong?",
        "options": [
            {"text": "Because the uterus does have a partner — the glands, "
                     "which also supply something", "correct": False,
             "why": "Adding fluid to sperm and supplying an embryo for nine "
                    "months are not the same job in any respect."},
            {"text": "Because the sperm duct has no partner either, so the "
                     "exception belongs on the male side", "correct": False,
             "why": "The sperm duct carries a gamete, and so does the oviduct. "
                    "The structures with no counterpart are all female."},
            {"text": "Because the cervix and the vagina have no partner "
                     "either — only the testes and ovaries pair up",
             "correct": True},
            {"text": "Because the rule is the wrong way round: the uterus is "
                     "the one that pairs up", "correct": False,
             "why": "The uterus is the clearest case of a structure with no "
                    "counterpart. The genuine pairing is testes with ovaries."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h13",
        "band": "harder",
        "text": "Sperm travel about 15 cm and the egg cell a few centimetres. "
                "A student concludes that sperm must be the faster cell. Is "
                "that a safe conclusion?",
        "options": [
            {"text": "No — distance on its own says nothing about speed "
                     "without the time each journey takes", "correct": True},
            {"text": "Yes — a cell that covers more ground has to be moving "
                     "more quickly", "correct": False,
             "why": "Only if the two took the same time, and nothing here says "
                    "they do. A slow journey can still be a long one."},
            {"text": "No — the egg must be the faster of the two, because it "
                     "is carried along rather than having to swim for itself",
             "correct": False,
             "why": "Being carried says nothing about speed either. The "
                    "measurement that decides it has not been taken."},
            {"text": "Yes — the sperm has a tail and the egg has none, so the "
                     "distances settle it between them", "correct": False,
             "why": "The tail explains how the sperm moves, not how fast. The "
                    "conclusion is about speed and the evidence is about "
                    "distance."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h14",
        "band": "harder",
        "text": "About four hundred egg cells are released in a lifetime, "
                "against hundreds of millions of sperm at a time. A student "
                "calls the male system the more efficient one. Which reply is "
                "best?",
        "options": [
            {"text": "Efficiency is the right word, and the female system is "
                     "the wasteful one", "correct": False,
             "why": "The female system wastes almost nothing: about four "
                    "hundred egg cells are released and each is released on "
                    "its own."},
            {"text": "Efficiency is the right word, because more gametes means "
                     "more chances", "correct": False,
             "why": "More chances is not more efficient. It is the opposite: a "
                    "system that spends hundreds of millions for one result."},
            {"text": "Neither system is efficient, because both of them waste "
                     "almost every gamete they make, egg cells included",
             "correct": False,
             "why": "Only one of them does. An ovary releases one egg cell at "
                    "a time, and the waste is nearly all on the other side."},
            {"text": "Efficiency is the wrong measure: nearly every sperm is "
                     "wasted, which is affordable only because each is cheap",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h15",
        "band": "harder",
        "text": "A student writes the female structures in one column and the "
                "male ones in another, then pairs them off down the page. "
                "What does that produce, and how much of it survives?",
        "options": [
            {"text": "It pairs the ovaries with the testes and then every "
                     "other structure correctly in turn, so the whole of the "
                     "list survives", "correct": False,
             "why": "Only the first pair is real. There are five female "
                    "structures and four male ones, and the lists stop "
                    "matching immediately."},
            {"text": "It pairs the oviduct with the sperm duct and the uterus "
                     "with the glands; only the first pair, testes with "
                     "ovaries, is real", "correct": True},
            {"text": "It pairs the uterus with the penis, which is right "
                     "because both handle gametes", "correct": False,
             "why": "One transfers a gamete out and the other holds an embryo "
                    "for nine months. Handling gametes is not one job."},
            {"text": "It produces nothing, because the two columns hold the "
                     "same number of structures", "correct": False,
             "why": "They do not: five female structures against four male "
                    "ones, which is part of why pairing them off fails."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h16",
        "band": "harder",
        "text": "A structure is described as a muscular ring, kept closed for "
                "nine months and opened over hours. Which structure is it, and "
                "which job does that serve?",
        "options": [
            {"text": "The uterus, and it serves supplying a developing "
                     "embryo", "correct": False,
             "why": "The uterus is the organ being kept closed, not the ring "
                    "closing it, and supplying is a separate job again."},
            {"text": "The vagina, and it serves receiving a gamete",
             "correct": False,
             "why": "The vagina is the canal below, and it is not a ring of "
                    "muscle that opens and closes."},
            {"text": "The cervix, and it serves protecting a developing "
                     "embryo", "correct": True},
            {"text": "The cervix, and it serves delivering a gamete",
             "correct": False,
             "why": "Delivering on this side is the oviduct's part, moving the "
                    "egg along. A ring held shut for nine months is doing the "
                    "protecting job."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h17",
        "band": "harder",
        "text": "Nothing in the male system matches the uterus, because no "
                "male structure holds another organism. Use that reasoning to "
                "say why nothing in the female system matches the glands.",
        "options": [
            {"text": "Because the egg cell does not swim, so nothing has to "
                     "make a fluid for it to swim in", "correct": True},
            {"text": "Because the female system contains no fluids of its own "
                     "at all, anywhere along its length", "correct": False,
             "why": "It is not short of fluid. The point is that the egg is "
                    "moved by the oviduct rather than swimming."},
            {"text": "Because the egg cell is far too large for any fluid to "
                     "carry it along", "correct": False,
             "why": "Size is not what decides it. Cilia and muscle move the "
                    "egg, whatever fluid is around it."},
            {"text": "Because the glands' fluid reaches the female system "
                     "anyway, inside the semen the penis transfers",
             "correct": False,
             "why": "That is true and it is not the reason. The question is "
                    "why no female structure has to make any."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h18",
        "band": "harder",
        "text": "In one case a testis sits in the abdomen at 37 °C. In "
                "another, both oviducts are completely blocked. Which job "
                "fails in each case?",
        "options": [
            {"text": "Making gametes in the first; protecting an embryo in the "
                     "second", "correct": False,
             "why": "The uterus is untouched by a blocked oviduct, so "
                    "protecting is not what fails. Nothing reaches the uterus "
                    "to be protected."},
            {"text": "Delivering gametes in the first; making gametes in the "
                     "second", "correct": False,
             "why": "Both halves are wrong. The warm testis makes none, and "
                    "the ovary goes on releasing behind a blockage."},
            {"text": "Receiving a gamete in the first; delivering gametes in "
                     "the second", "correct": False,
             "why": "The male system never receives a gamete, so that job "
                    "cannot fail in it."},
            {"text": "Making gametes in the first; delivering gametes in the "
                     "second", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h19",
        "band": "harder",
        "text": "A student calls the vagina “the female urethra”, because both "
                "are the tube a gamete crosses by. Give the strongest reason "
                "that is not a fair pairing.",
        "options": [
            {"text": "The urethra is a good deal longer than the vagina is, "
                     "so the two journeys cannot fairly be compared",
             "correct": False,
             "why": "Length is not the difference that matters, and it is the "
                    "jobs that are being compared rather than the sizes."},
            {"text": "One passes a gamete out of its system and the other "
                     "takes one in, and only one also carries urine",
             "correct": True},
            {"text": "The vagina carries urine as well, exactly as the urethra "
                     "does", "correct": False,
             "why": "It does not. Carrying urine is the one job outside "
                    "reproduction, and it belongs to the urethra alone."},
            {"text": "No gamete crosses the vagina at all, so there is nothing "
                     "to compare", "correct": False,
             "why": "Sperm cross it on the way in. Receiving them is the "
                    "vagina's own job in the list of five."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h20",
        "band": "harder",
        "text": "An unfamiliar mammal's female tract is found to contain an "
                "ovary, a tube, a chamber with a thick lining and a muscular "
                "ring at the chamber's base. Which human structures do the "
                "last two match?",
        "options": [
            {"text": "The chamber matches the oviduct, and the ring matches "
                     "the vagina", "correct": False,
             "why": "The oviduct is the tube before the chamber, and the "
                    "vagina is a canal rather than a ring of muscle."},
            {"text": "The chamber matches the ovary, and the ring matches the "
                     "cervix", "correct": False,
             "why": "The ovary is already named separately in the description. "
                    "A lined chamber is a uterus."},
            {"text": "The chamber matches the uterus, and the ring matches the "
                     "cervix", "correct": True},
            {"text": "The chamber matches the uterus, and the ring matches the "
                     "oviduct", "correct": False,
             "why": "An oviduct is a tube running to an ovary, not a ring at "
                    "the base of the uterus."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h21",
        "band": "harder",
        "text": "About a million immature egg cells are present at birth and "
                "about four hundred are ever released. Roughly what percentage "
                "of the stock is that?",
        "options": [
            {"text": "About 0.04%", "correct": True},
            {"text": "About 0.4%", "correct": False,
             "why": "Ten times too high. Four hundred in a million is four in "
                    "ten thousand, which is 0.04%."},
            {"text": "About 4%", "correct": False,
             "why": "That would be forty thousand egg cells released. A "
                    "hundred times too many."},
            {"text": "About 40%", "correct": False,
             "why": "Four hundred thousand egg cells, which is most of the "
                    "stock. The real share is tiny."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h22",
        "band": "harder",
        "text": "Two of the nine functions are “transfers gametes into the "
                "other system” and “receives gametes and leads towards the "
                "egg”. Whose are they, and why are they not a matching pair?",
        "options": [
            {"text": "The sperm duct's and the oviduct's; they run in opposite "
                     "directions, so they cancel out", "correct": False,
             "why": "Neither function belongs to those tubes. One is the "
                    "penis's and the other the vagina's."},
            {"text": "The penis's and the uterus's; the uterus holds an embryo "
                     "as well as receiving, so it does the larger share of the "
                     "job", "correct": False,
             "why": "Receiving is the vagina's function, not the uterus's. The "
                    "uterus is further in."},
            {"text": "The penis's and the vagina's; they are the same job seen "
                     "twice, so they do pair up", "correct": False,
             "why": "Transferring and receiving are different jobs. A system "
                    "that only transfers needs no structure for receiving."},
            {"text": "The penis's and the vagina's; one transfers and one "
                     "receives, which are two halves of an event rather than "
                     "one job", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h23",
        "band": "harder",
        "text": "One of these functions belongs to no male structure at all. "
                "Which one?",
        "options": [
            {"text": "Carrying gametes from where they are made",
             "correct": False,
             "why": "That is the sperm duct's function, running from the "
                    "testes towards the urethra."},
            {"text": "Closing an organ, and opening it again later",
             "correct": True},
            {"text": "Adding fluid that gametes can swim in", "correct": False,
             "why": "The glands do this, and it is the male system that has "
                    "the structure for it rather than the female one."},
            {"text": "Transferring gametes into the other system",
             "correct": False,
             "why": "That is the penis's function, and it is the male half of "
                    "the transfer."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h24",
        "band": "harder",
        "text": "A student gives the function “holds and supplies a developing "
                "embryo” to the oviduct. Whose function have they taken, and "
                "what is left unassigned?",
        "options": [
            {"text": "They have taken the ovary's function, and the ovary is "
                     "then left with nothing at all to do", "correct": False,
             "why": "The ovary contains and releases egg cells. Holding an "
                    "embryo was never its function."},
            {"text": "They have taken the vagina's own function, and the "
                     "uterus is then the one left unassigned", "correct": False,
             "why": "The vagina receives gametes and is the birth canal. "
                    "Holding an embryo is the uterus's own function."},
            {"text": "They have taken the uterus's, and the oviduct's own "
                     "function is then left unassigned", "correct": True},
            {"text": "They have taken the cervix's, and the cervix is then "
                     "left unassigned", "correct": False,
             "why": "The cervix closes the lower end of the uterus. It holds "
                    "and supplies nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h25",
        "band": "harder",
        "text": "A student suggests that wrapping the testes warmly would "
                "raise sperm production. Evaluate that suggestion.",
        "options": [
            {"text": "It would lower production, because warming them towards "
                     "37 °C is what stops it", "correct": True},
            {"text": "It would raise production, because warmth speeds up "
                     "everything that a cell does", "correct": False,
             "why": "Not this. Production works around 34 °C and fails at "
                    "37 °C, so warming is the wrong direction."},
            {"text": "It would make no difference, because the muscle would "
                     "hold the temperature steady anyway", "correct": False,
             "why": "The muscle works by moving the testes nearer to or "
                    "further from the body. Wrapping them defeats that."},
            {"text": "It would raise production in cold weather and lower it "
                     "in warm weather", "correct": False,
             "why": "The target temperature is the same in all weathers, and "
                    "it is below the body's core either way."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h26",
        "band": "harder",
        "text": "A testis is measured at 34 °C on a day when the air is 2 °C, "
                "and again at 34 °C on a day when the air is 22 °C. What does "
                "that show?",
        "options": [
            {"text": "That the air temperature has no effect on the body at "
                     "all", "correct": False,
             "why": "It has plenty of effect, which is why the muscle has to "
                    "respond to it. The reading is steady because something is "
                    "holding it steady."},
            {"text": "That the testes are at core body temperature on both "
                     "days", "correct": False,
             "why": "Core temperature is 37 °C. Both readings are three "
                    "degrees below it."},
            {"text": "That sperm production must work at any temperature "
                     "between 2 °C and 22 °C", "correct": False,
             "why": "Those are the air temperatures, not the organ's. The "
                    "organ stayed at 34 °C in both."},
            {"text": "That the temperature of the testes is being held steady, "
                     "whatever the air does", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h27",
        "band": "harder",
        "text": "Suppose an animal's uterus had no muscular ring at its lower "
                "end. Which of the five jobs would be hardest for it?",
        "options": [
            {"text": "Making gametes, because the ovaries would have nothing "
                     "to release into", "correct": False,
             "why": "The ovaries release into the oviducts at the top of the "
                    "system. Nothing at the lower end affects them."},
            {"text": "Protecting a developing embryo, because the uterus could "
                     "not be kept closed", "correct": True},
            {"text": "Delivering a gamete, because the egg cell could not be "
                     "moved along", "correct": False,
             "why": "The egg is moved by cilia and muscle in the oviduct, at "
                    "the other end of the system entirely."},
            {"text": "Receiving a gamete, because sperm could no longer get "
                     "in", "correct": False,
             "why": "Sperm would get in more easily, not less. A ring of "
                    "muscle is a closure rather than a door."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h28",
        "band": "harder",
        "text": "Why does it take three male structures to deliver a gamete, "
                "when the female system manages with one?",
        "options": [
            {"text": "Because sperm are smaller, and smaller cells need more "
                     "structures to handle them", "correct": False,
             "why": "Size does not set the number of structures. What the "
                    "journey demands does."},
            {"text": "Because there are hundreds of millions of sperm and only "
                     "one egg, so more organs are needed to hold them",
             "correct": False,
             "why": "None of the three stores sperm. They carry them, add "
                    "fluid and transfer them."},
            {"text": "Because its gamete must be carried out, given fluid to "
                     "swim in and transferred into another body",
             "correct": True},
            {"text": "Because the female system's single structure does all "
                     "three of those jobs at once", "correct": False,
             "why": "The oviduct does none of them. It moves the egg a few "
                    "centimetres inside one body, which is a much smaller "
                    "task."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h29",
        "band": "harder",
        "text": "Take the sperm's journey as 15 cm and the egg's as about "
                "4 cm. Roughly how many times further do the sperm travel?",
        "options": [
            {"text": "About four times", "correct": True},
            {"text": "About eleven times", "correct": False,
             "why": "Eleven centimetres is the difference between the two "
                    "distances. The question asks how many times, which needs "
                    "a division."},
            {"text": "About sixty times", "correct": False,
             "why": "This multiplies the two figures instead of dividing them. "
                    "15 divided by 4 is close to 4."},
            {"text": "About forty times", "correct": False,
             "why": "A factor of ten has slipped in. 15 cm against 4 cm is "
                    "about four times, not forty."},
        ],
        "figure": None,
    },
    {
        "id": "b5-01-h30",
        "band": "harder",
        "text": "Put the five jobs in the order in which they would be done "
                "for one embryo.",
        "options": [
            {"text": "Deliver a gamete, make a gamete, receive one, supply the "
                     "embryo, protect it", "correct": False,
             "why": "A gamete has to exist before it can be delivered, and "
                    "protecting begins as soon as it is held."},
            {"text": "Make a gamete, receive one, deliver it, protect the "
                     "embryo, supply it", "correct": False,
             "why": "Nothing can be received before it has been delivered. "
                    "Those two are the wrong way round."},
            {"text": "Receive a gamete, make one, deliver it, protect the "
                     "embryo, supply it", "correct": False,
             "why": "Receiving is the third step, not the first. A gamete is "
                    "made and delivered before any system receives it."},
            {"text": "Make a gamete, deliver it, receive one, protect the "
                     "embryo, supply it", "correct": True},
        ],
        "figure": None,
    },
]
