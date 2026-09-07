"""B5 lesson 02 — Gametes and fertilisation: twelve questions (MRB-269).

These probe the two things this lesson exists to separate: the events of the
process from each other, and the genetic contribution of the two gametes from
the material contribution. The distractors are built from the lesson's three
declared misconceptions — REPRO-03 (fertilisation is when the sperm reaches
the egg), REPRO-04 (identical twins happen when two eggs are fertilised) and
REPRO-18 (the egg is bigger because it carries more genetic material) — and
from the errors those three drag along with them: that fertilisation happens
in the uterus, that pregnancy begins at fertilisation, that the egg is moved by
gravity or pushed by sperm, that several sperm enter one egg, and that half a
set plus half a set makes half a set. The `harder` band takes the lesson
somewhere new each time: from bar width to volume, from a boy-and-girl twin
pair back to its cause, along three generations of mitochondrial DNA, and into
the one arithmetic the outer layer exists to prevent.
"""

UNIT = "B5"
LESSON = "gametes-and-fertilisation"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-02-e01",
        "band": "easier",
        "text": "Fertilisation happens in one place and one place only. "
                "Where?",
        "options": [
            {"text": "In the uterus, where the lining is thick and ready.",
             "correct": False,
             "why": "That is where implantation happens, several days later. "
                    "By the time a ball of cells reaches the uterus, "
                    "fertilisation is long over."},
            {"text": "In the oviduct, the tube between an ovary and the "
                     "uterus.",
             "correct": True},
            {"text": "In an ovary, as soon as the egg cell is released.",
             "correct": False,
             "why": "The ovary is where release happens, and release happens "
                    "whether or not any sperm are anywhere near."},
            {"text": "In the vagina, where the semen is transferred.",
             "correct": False,
             "why": "Semen is transferred there, but the sperm still have to "
                    "swim through the cervix and the uterus to reach the egg."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e02",
        "band": "easier",
        "text": "An egg cell has no tail and cannot swim. So how does it "
                "travel along the oviduct?",
        "options": [
            {"text": "Cilia and muscle in the wall of the oviduct move it "
                     "along.",
             "correct": True},
            {"text": "It drifts downwards under gravity, from the ovary "
                     "towards the uterus.",
             "correct": False,
             "why": "Nothing in your body is moved by falling. The oviduct "
                    "moves the egg along whichever way up you are standing."},
            {"text": "Sperm push it ahead of them as they swim up the tube.",
             "correct": False,
             "why": "The sperm swim towards the egg, not behind it — and the "
                    "egg is already on the move before any sperm arrive."},
            {"text": "It grows a short tail of its own once it leaves the "
                     "ovary.",
             "correct": False,
             "why": "Only one of the two gametes needs its own propulsion, and "
                    "it is the cheap one. The egg is moved for it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e03",
        "band": "easier",
        "text": "One sperm nucleus fuses with one egg nucleus. How many "
                "chromosomes does the single new cell carry, and where did "
                "they come from?",
        "options": [
            {"text": "23 — the two half sets merge together into one half "
                     "set.",
             "correct": False,
             "why": "Fusing adds the two sets, it does not blend them into "
                    "one. 23 plus 23 makes 46, which is a full set."},
            {"text": "92 — 46 from the sperm and 46 from the egg cell.",
             "correct": False,
             "why": "A gamete carries half a set, not a full one: 23 each. "
                    "46 is what the cell ends up with, not what it starts "
                    "with."},
            {"text": "46 — all of them from the egg, which supplies the "
                     "material.",
             "correct": False,
             "why": "The egg supplies nearly all the material, but not nearly "
                    "all the chromosomes. Each gamete gives exactly 23."},
            {"text": "46 — 23 from the sperm and 23 from the egg.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e04",
        "band": "easier",
        "text": "A sperm cell carries almost no food store, yet it swims a "
                "journey of about 15 cm. Where does the energy come from?",
        "options": [
            {"text": "From the egg cell, which supplies the sperm as soon as "
                     "it arrives.",
             "correct": False,
             "why": "The egg's store is loaded for what happens after fusion, "
                    "not for the journey. A sperm that has arrived has already "
                    "done its swimming."},
            {"text": "From a food store in the head, packed in behind the "
                     "nucleus.",
             "correct": False,
             "why": "The head carries the nucleus, not a store. A store would "
                    "make the sperm heavier, and travelling is easier the "
                    "smaller you are."},
            {"text": "From sugar in the fluid around it, released by its "
                     "mitochondria.",
             "correct": True},
            {"text": "It needs none — it is carried along by cilia and muscle "
                     "in the wall.",
             "correct": False,
             "why": "That is how the egg cell travels. The sperm swims itself, "
                    "and swimming 15 cm costs energy."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-02-s01",
        "band": "standard",
        "text": "Hundreds of millions of sperm are released at a time, but an "
                "ovary releases one egg at a time, about 400 in a lifetime. "
                "What best explains that difference?",
        "options": [
            {"text": "Most sperm are faulty, so huge numbers are needed to "
                     "get a few good ones.",
             "correct": False,
             "why": "Numbers are not about faults. A perfectly good sperm is "
                    "still mostly wasted — of hundreds of millions, only a few "
                    "hundred arrive."},
            {"text": "A sperm is cheap to make and mostly wasted; an egg is "
                     "expensive to make.",
             "correct": True},
            {"text": "Each egg is fertilised by several sperm, so many are "
                     "needed for each one.",
             "correct": False,
             "why": "Only one sperm enters. The moment its nucleus fuses, the "
                    "egg's outer layer changes so that no other sperm can get "
                    "in."},
            {"text": "An egg cell is large, and there is only room in the "
                     "body for a few of them.",
             "correct": False,
             "why": "Space is not the limit — cost is. Cytoplasm, "
                    "mitochondria and a food store all have to be built before "
                    "the egg is released."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s02",
        "band": "standard",
        "text": "A student writes: “The sperm reaches the egg in the "
                "uterus, and that is when pregnancy begins.” Which "
                "rewrite corrects everything that is wrong?",
        "options": [
            {"text": "The sperm reaches the egg in the oviduct, and that is "
                     "when pregnancy begins.",
             "correct": False,
             "why": "The place is right now, but two things are still wrong: "
                    "reaching is not fertilising, and pregnancy begins at "
                    "implantation, days later."},
            {"text": "The sperm's nucleus fuses with the egg's in the uterus, "
                     "and pregnancy begins right there and then.",
             "correct": False,
             "why": "Fusing is the right word for the event, but it happens in "
                    "the oviduct and nowhere else, and pregnancy begins at "
                    "implantation."},
            {"text": "The sperm reaches the egg in the oviduct, and pregnancy "
                     "begins at implantation.",
             "correct": False,
             "why": "The place and the timing are right now, but many sperm "
                    "reach the egg. Reaching describes a crowd arriving; only "
                    "one sperm fuses, and fusing is the event."},
            {"text": "The sperm's nucleus fuses with the egg's in the oviduct, "
                     "and pregnancy begins at implantation.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s03",
        "band": "standard",
        "text": "An egg cell is released on the Tuesday. Sperm reach the "
                "oviduct on the Friday. Predict what happens.",
        "options": [
            {"text": "Nothing — an egg stays able to be fertilised for only "
                     "about a day after release.",
             "correct": True},
            {"text": "Fertilisation happens as normal — the egg waits in the "
                     "oviduct until sperm arrive.",
             "correct": False,
             "why": "The egg does not wait for anything. It is travelling from "
                    "the moment it is released, and it stays able to be "
                    "fertilised for roughly a day."},
            {"text": "Fertilisation happens, but in the uterus, because the "
                     "egg has moved on by then.",
             "correct": False,
             "why": "Fertilisation happens in the oviduct and nowhere else. An "
                    "egg past its day-long window is not fertilised anywhere."},
            {"text": "Nothing — sperm cannot survive that journey and die "
                     "before they ever arrive.",
             "correct": False,
             "why": "Sperm do arrive: a few hundred of the hundreds of "
                    "millions make it. It is the egg's window that has closed, "
                    "not the sperm that failed."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s04",
        "band": "standard",
        "text": "For about five days after fertilisation the cell divides "
                "into two, then four, then eight, all while still travelling. "
                "What is it living on in that time?",
        "options": [
            {"text": "Sugar in the fluid around it, the same supply a sperm "
                     "uses.",
             "correct": False,
             "why": "That supply is enough for one cell's short swim, not for "
                    "five days of a whole ball of cells dividing."},
            {"text": "Food passed to it through the thickened lining of the "
                     "uterus.",
             "correct": False,
             "why": "It cannot be supplied until it has embedded in that "
                    "lining — and that is implantation, the step after these "
                    "five days."},
            {"text": "The food store the egg loaded into its cytoplasm before "
                     "fertilisation.",
             "correct": True},
            {"text": "Food carried in by the sperm at the moment the two "
                     "nuclei fuse.",
             "correct": False,
             "why": "A sperm carries almost no food store at all. Everything "
                    "spent in these five days was loaded before fertilisation, "
                    "by the egg."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-02-h01",
        "band": "harder",
        "text": "The lesson draws the egg's bar twenty times as long as the "
                "sperm head's. A student concludes the egg is twenty times as "
                "much cell. Where does that go wrong?",
        "options": [
            {"text": "It does not go wrong — a bar twenty times as long does "
                     "mean twenty times as much cell.",
             "correct": False,
             "why": "The bars are diameters, not amounts. Widening something "
                    "twenty times in every direction multiplies what fits "
                    "inside it far more than twenty times."},
            {"text": "Two cells can only be compared by bars if they are "
                     "exactly the same shape as each other.",
             "correct": False,
             "why": "The comparison itself is honest — both bars are drawn to "
                    "scale. It is the step from a width to an amount that has "
                    "to be taken carefully."},
            {"text": "Those bars are diameters, and volume goes as the "
                     "diameter cubed — eight thousand times.",
             "correct": True},
            {"text": "It is backwards — the egg is twenty times as wide but "
                     "only about five times the volume.",
             "correct": False,
             "why": "Volume grows faster than width, never slower. Twenty "
                    "times the width is about eight thousand times the volume, "
                    "not five."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h02",
        "band": "harder",
        "text": "A pair of twins is born, one a boy and one a girl. What does "
                "that on its own tell you about how they began?",
        "options": [
            {"text": "They are non-identical: two eggs released, two sperm, "
                     "two separate fertilisations.",
             "correct": True},
            {"text": "They are identical, and the ball of cells split early "
                     "enough for the halves to differ.",
             "correct": False,
             "why": "A split cannot change chromosomes. Both halves carry the "
                    "same set as each other, so identical twins are always the "
                    "same sex."},
            {"text": "Nothing on its own — either kind of twin can be a boy "
                     "and a girl.",
             "correct": False,
             "why": "Each twin's chromosomes were fixed at fertilisation. "
                    "Identical twins share one set between them, so they "
                    "cannot differ in sex."},
            {"text": "They are identical, because they shared one pregnancy "
                     "and were born together.",
             "correct": False,
             "why": "Sharing a pregnancy is what every pair of twins does. "
                    "Non-identical twins are two ordinary siblings who happen "
                    "to share one."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h03",
        "band": "harder",
        "text": "Mitochondrial DNA is compared across three people: a "
                "grandmother, her son, and her daughter's daughter. Whose "
                "matches the grandmother's?",
        "options": [
            {"text": "Only the daughter's daughter — a son inherits none of "
                     "his mother's mitochondria.",
             "correct": False,
             "why": "He inherits all of them: every mitochondrion in a body "
                    "came from the egg it grew from. What a son cannot do is "
                    "pass them on."},
            {"text": "Only the son — mitochondria are passed to sons and "
                     "rebuilt fresh in daughters.",
             "correct": False,
             "why": "Nothing is rebuilt fresh. Both children got all their "
                    "mitochondria from the same egg cells their mother "
                    "supplied."},
            {"text": "None exactly, because mitochondrial DNA is shuffled "
                     "with the father's each generation.",
             "correct": False,
             "why": "Mitochondrial DNA is the part that is not shuffled with "
                    "anything, which is exactly why it works as a clock: it "
                    "changes only by slow mutation."},
            {"text": "All three — everyone's mitochondria came from the egg "
                     "they grew from.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h04",
        "band": "harder",
        "text": "Very rarely the outer layer fails to change in time and a "
                "second sperm's nucleus fuses too. Using this lesson's "
                "numbers, what would that cell carry?",
        "options": [
            {"text": "46, because an egg takes in only 23 chromosomes from "
                     "outside however many sperm fuse.",
             "correct": False,
             "why": "Nothing in the egg counts chromosomes. The only block is "
                    "the outer layer changing, and here it has failed — so a "
                    "second 23 is added."},
            {"text": "69 — the egg's 23, plus 23 from each of the two sperm "
                     "cells.",
             "correct": True},
            {"text": "46, because the second sperm's 23 chromosomes replace "
                     "the first sperm's 23.",
             "correct": False,
             "why": "Fusing adds a half set to what is there; it does not swap "
                    "one out. The first sperm's chromosomes are already part "
                    "of the cell."},
            {"text": "92, because a second fertilisation doubles the 46 the "
                     "cell already had.",
             "correct": False,
             "why": "A sperm brings 23, not 46. Adding one more half set to a "
                    "full set of 46 gives 69."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-02-e05",
        "band": "easier",
        "text": "Several days after fertilisation the ball of cells embeds "
                "itself in the thickened lining of the uterus. What is that "
                "event called?",
        "options": [
            {"text": "Fertilisation", "correct": False,
             "why": "Fertilisation happened days earlier, in the oviduct, "
                    "when the two nuclei fused. This is a separate event, in "
                    "a different organ."},
            {"text": "Implantation", "correct": True},
            {"text": "Release", "correct": False,
             "why": "Release is the egg cell leaving the ovary, before any of "
                    "this. It happens whether or not any sperm are present."},
            {"text": "Dividing", "correct": False,
             "why": "Dividing is what the cell has been doing all the way "
                    "down the oviduct. Embedding is what it does once it "
                    "arrives."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e06",
        "band": "easier",
        "text": "How many chromosomes does a single human gamete carry?",
        "options": [
            {"text": "46 — a full set", "correct": False,
             "why": "46 is the number in the single cell formed when two "
                    "gametes fuse. One gamete brings half of that."},
            {"text": "23 in a sperm cell and 46 in an egg cell",
             "correct": False,
             "why": "The two gametes are unequal in almost every way, and "
                    "this is the one measurement on which they match exactly: "
                    "23 each."},
            {"text": "None — a gamete has no chromosomes until fertilisation",
             "correct": False,
             "why": "A gamete has a nucleus with chromosomes inside it. "
                    "Fertilisation adds a second set to the first; it does "
                    "not create the first."},
            {"text": "23 — half a set", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e07",
        "band": "easier",
        "text": "Which of these does a sperm cell have and an egg cell does "
                "not?",
        "options": [
            {"text": "A tail", "correct": True},
            {"text": "A nucleus", "correct": False,
             "why": "Both have one, and the fusing of those two nuclei is the "
                    "whole of fertilisation."},
            {"text": "Twenty-three chromosomes", "correct": False,
             "why": "Both carry twenty-three. It is the one measurement on "
                    "which the two gametes are identical."},
            {"text": "A large food store", "correct": False,
             "why": "That belongs to the egg, not the sperm. A sperm carries "
                    "almost no store and lives on sugar in the fluid around "
                    "it."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-02-s05",
        "band": "standard",
        "text": "A sperm cell has a few dozen mitochondria packed behind its "
                "head; an egg cell has hundreds of thousands. What is each "
                "set of mitochondria for?",
        "options": [
            {"text": "Both sets release energy for swimming; the egg simply "
                     "carries spares", "correct": False,
             "why": "The egg does not swim at all — it is moved along by "
                    "cilia and by muscle. Its mitochondria are not there for "
                    "propulsion."},
            {"text": "The egg’s release the energy that the sperm uses on its "
                     "journey", "correct": False,
             "why": "The sperm powers itself, using its own mitochondria and "
                    "sugar from the fluid around it. It arrives with its "
                    "energy already spent."},
            {"text": "The sperm’s power its journey; the egg’s are the ones "
                     "the new organism inherits", "correct": True},
            {"text": "The sperm’s are the ones inherited, which is why "
                     "mitochondria come from the father", "correct": False,
             "why": "It is the other way round. Every mitochondrion in your "
                    "body came from the egg, and the sperm’s are destroyed "
                    "after fusion."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s06",
        "band": "standard",
        "text": "A gamete cannot grow into a new organism on its own. What is "
                "the reason for that?",
        "options": [
            {"text": "It has no cytoplasm and no food store of its own to "
                     "grow with", "correct": False,
             "why": "An egg cell has both, in quantity, and still cannot do "
                    "it alone. What is missing is not material."},
            {"text": "It carries half a set of chromosomes, and needs the "
                     "other half added to it", "correct": True},
            {"text": "It is far too small to divide into a new organism",
             "correct": False,
             "why": "The egg is the largest cell in the body, and the "
                    "fertilised cell begins dividing straight away. Size is "
                    "not what stops it."},
            {"text": "It breaks down within about a day unless it is "
                     "fertilised", "correct": False,
             "why": "A released egg does break down within about a day, but "
                    "that is a deadline rather than a reason. Even a fresh "
                    "one could not manage on its own."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s07",
        "band": "standard",
        "text": "One sperm’s nucleus has fused with the egg’s nucleus, and "
                "the egg’s outer layer changes immediately afterwards. What "
                "is that change for?",
        "options": [
            {"text": "It stops any other sperm cell from entering the egg",
             "correct": True},
            {"text": "It seals the food store in, so the cell can live on it",
             "correct": False,
             "why": "The food store is already inside the cytoplasm and is "
                    "not going anywhere. There is nothing to seal in."},
            {"text": "It makes the cell sticky, so it can embed in the "
                     "uterus lining", "correct": False,
             "why": "Embedding is implantation, about five days later and in "
                    "a different organ. This change happens within moments of "
                    "fusion."},
            {"text": "It signals the cell to start dividing", "correct": False,
             "why": "The cell does begin dividing, but keeping the other "
                    "sperm out is what the outer layer is doing. Two things "
                    "happening at once are not the same thing."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-02-h05",
        "band": "harder",
        "text": "Three days after fertilisation, one cell is taken from the "
                "ball of cells travelling down the oviduct. How many "
                "chromosomes does it carry, and why?",
        "options": [
            {"text": "23, because the ball is still made of gametes",
             "correct": False,
             "why": "The two gametes stopped existing at fusion. From that "
                    "moment there is one cell with a full set, and everything "
                    "after it is a copy of that cell."},
            {"text": "92, because the cell has divided twice since "
                     "fertilisation", "correct": False,
             "why": "Dividing makes more cells; it does not make more "
                    "chromosomes in each one. Every division hands on a full "
                    "set of 46."},
            {"text": "46 in some cells and 23 in others, depending which "
                     "gamete each came from", "correct": False,
             "why": "The two sets were combined in one nucleus at fusion and "
                    "never separated again. Every cell in the ball carries "
                    "both halves."},
            {"text": "46, because every cell came by division from the single "
                     "fertilised cell", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h06",
        "band": "harder",
        "text": "A biologist studying an unfamiliar animal finds two kinds of "
                "gamete: one large and immobile with a food store, one tiny "
                "with a tail. Which conclusion is safest?",
        "options": [
            {"text": "The large one is the egg and the tiny one the sperm, "
                     "because each is built for its own job", "correct": True},
            {"text": "The large one must carry more chromosomes than the "
                     "tiny one, since it holds so much more material",
             "correct": False,
             "why": "In humans the two carry exactly the same number, and all "
                    "the size difference is packing material. Size says "
                    "nothing about the chromosome count."},
            {"text": "They must come from two different species, since one "
                     "animal’s gametes would be alike", "correct": False,
             "why": "The two gametes of a single species are normally as "
                    "different as this. Being unalike is the whole point of "
                    "having two kinds."},
            {"text": "The tiny one must be a young gamete that has not yet "
                     "finished growing to its full size", "correct": False,
             "why": "A sperm is small because travelling is easier the "
                    "smaller you are, and it never grows any larger. It is "
                    "finished as it is."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h07",
        "band": "harder",
        "text": "Suppose 300 million sperm cells set out and about 300 of "
                "them reach the oviduct. Roughly what fraction arrives?",
        "options": [
            {"text": "About one in a thousand", "correct": False,
             "why": "One in a thousand of 300 million is 300 000 arriving. "
                    "The real number is a thousand times smaller than that."},
            {"text": "About one in a hundred thousand", "correct": False,
             "why": "Closer, and still a hundredfold too generous: one in a "
                    "hundred thousand of 300 million is 3000."},
            {"text": "About one in a million", "correct": True},
            {"text": "About one in ten million", "correct": False,
             "why": "That would leave only 30 arriving. Dividing 300 million "
                    "by 300 gives one in a million exactly."},
        ],
        "figure": None,
    },
]
