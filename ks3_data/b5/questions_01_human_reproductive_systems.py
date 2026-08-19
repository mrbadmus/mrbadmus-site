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
]
