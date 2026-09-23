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
        "text": "Look at the diagram. A student concludes that the egg must "
                "be twenty times as much cell as the sperm. Where does that "
                "go wrong?",
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
                     "diameter cubed — about eight thousand times.",
             "correct": True},
            {"text": "It is backwards — the egg is twenty times as wide but "
                     "only about five times the volume.",
             "correct": False,
             "why": "Volume grows faster than width, never slower. Twenty "
                    "times the width is about eight thousand times the volume, "
                    "not five."},
        ],
        "figure": "b5-egg-sperm-scale",
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

    # ── MRB-338 night 3 top-up ──────────────────────────────────────────
    #
    # The two cells and the five steps, and nothing else: what each gamete
    # carries and why, and which event is which. The cycle belongs to lesson 3
    # and the organs to lesson 1, so nothing here asks what an organ is for.
    # Rungs 1 to 4 own the definition of fertilisation, what the egg's extra
    # material is for, the two specialisations compared in writing, and the
    # two kinds of twin, so the bank approaches each of those from a different
    # task or leaves it alone.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-02-e08",
        "band": "easier",
        "text": "Which is the largest cell in the human body?",
        "options": [
            {"text": "The sperm cell", "correct": False,
             "why": "A sperm is one of the smallest: its head is about "
                    "0.005 mm across, a twentieth of a millimetre's twentieth."},
            {"text": "A cell of the uterus lining", "correct": False,
             "why": "The lining is thick because it has many cells in it, not "
                    "because its cells are large."},
            {"text": "The fertilised cell, once the two have fused",
             "correct": False,
             "why": "Fusing adds a sperm's nucleus to an egg. The egg was "
                    "already that size, and it is the size that counts."},
            {"text": "The egg cell", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e09",
        "band": "easier",
        "text": "Roughly how wide is an egg cell?",
        "options": [
            {"text": "About 0.1 mm", "correct": True},
            {"text": "About 0.005 mm", "correct": False,
             "why": "That is the width of a sperm cell's head — twenty times "
                    "smaller."},
            {"text": "About 1 mm", "correct": False,
             "why": "Ten times too wide. At 1 mm an egg would be obvious to "
                    "the naked eye rather than only just visible."},
            {"text": "About 1 cm", "correct": False,
             "why": "A hundred times too wide. No human cell is anywhere near "
                    "a centimetre across."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e10",
        "band": "easier",
        "text": "Roughly how wide is the head of a sperm cell?",
        "options": [
            {"text": "About 0.1 mm", "correct": False,
             "why": "That is the egg cell's width. The sperm's head is twenty "
                    "times narrower than that."},
            {"text": "About 0.05 mm", "correct": False,
             "why": "Ten times too wide. The figure is 0.005 mm, which is half "
                    "of a hundredth of a millimetre."},
            {"text": "About 0.005 mm", "correct": True},
            {"text": "About 0.5 mm", "correct": False,
             "why": "That would make a sperm's head five times wider than the "
                    "largest cell in the body."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e11",
        "band": "easier",
        "text": "For roughly how long does the fertilised cell divide as it "
                "travels, before it arrives anywhere?",
        "options": [
            {"text": "About an hour", "correct": False,
             "why": "Far too quick. In an hour it would have divided once or "
                    "twice and gone almost nowhere."},
            {"text": "About a day", "correct": False,
             "why": "About a day is how long a released egg stays able to be "
                    "fertilised. The journey afterwards is longer."},
            {"text": "About a fortnight", "correct": False,
             "why": "Three times too long. The cell has arrived and embedded "
                    "well before a fortnight is up."},
            {"text": "About five days", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e12",
        "band": "easier",
        "text": "Hundreds of millions of sperm cells set out. Roughly how many "
                "arrive at the oviduct?",
        "options": [
            {"text": "Only one", "correct": False,
             "why": "Only one fuses with the egg, but many more than one get "
                    "there. A few hundred arrive."},
            {"text": "A few million", "correct": False,
             "why": "Thousands of times too many. The journey is about 15 cm "
                    "for a cell 0.005 mm long, and almost none survives it."},
            {"text": "Half of them", "correct": False,
             "why": "Nothing like it. Almost all are lost on the way — only "
                    "about one in a million arrives."},
            {"text": "A few hundred", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e13",
        "band": "easier",
        "text": "Which gamete carries a large food store?",
        "options": [
            {"text": "The sperm cell", "correct": False,
             "why": "A sperm carries almost none. It uses sugar in the fluid "
                    "around it instead, and a store would only weigh it down."},
            {"text": "Both of them, equally", "correct": False,
             "why": "Only one of them does. The store is the reason the egg is "
                    "so much the larger cell."},
            {"text": "The egg cell", "correct": True},
            {"text": "Neither of them — the store is added at fertilisation",
             "correct": False,
             "why": "Nothing is added at fertilisation except a nucleus. "
                    "Everything spent afterwards was loaded before it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e14",
        "band": "easier",
        "text": "Whereabouts in a sperm cell are its mitochondria?",
        "options": [
            {"text": "Packed in behind the head", "correct": True},
            {"text": "Spread along the whole length of the tail",
             "correct": False,
             "why": "The tail is the part that beats. The mitochondria that "
                    "power it are packed together behind the head."},
            {"text": "Inside the nucleus, with the chromosomes",
             "correct": False,
             "why": "The nucleus holds chromosomes and nothing else. "
                    "Mitochondria sit outside it."},
            {"text": "At the very tip of the tail, well clear of the head",
             "correct": False,
             "why": "Nothing is carried at the tip. Weight out there would "
                    "make the tail harder to beat, not easier."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e15",
        "band": "easier",
        "text": "Every mitochondrion in a new organism comes from which "
                "gamete?",
        "options": [
            {"text": "From the sperm cell", "correct": False,
             "why": "The sperm's few dozen power its journey and are destroyed "
                    "after fusion. None of them is passed on."},
            {"text": "From both, about half from each", "correct": False,
             "why": "They are not shared out. The egg supplies all the "
                    "cytoplasm and everything in it."},
            {"text": "From neither — they are built after fertilisation",
             "correct": False,
             "why": "The fertilised cell starts with the egg's mitochondria "
                    "already in place, in their hundreds of thousands."},
            {"text": "From the egg cell", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e16",
        "band": "easier",
        "text": "What happens to a sperm cell's own mitochondria after the two "
                "nuclei have fused?",
        "options": [
            {"text": "They are destroyed", "correct": True},
            {"text": "They join the egg's own", "correct": False,
             "why": "They do not join the collection. The egg's hundreds of "
                    "thousands are the whole of what the new cell keeps."},
            {"text": "They enter the nucleus", "correct": False,
             "why": "Only the nuclei fuse, and mitochondria are not part of a "
                    "nucleus in the first place."},
            {"text": "They keep the fertilised cell supplied for five days",
             "correct": False,
             "why": "The food store the egg loaded does that. The sperm's "
                    "mitochondria are gone by then."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e17",
        "band": "easier",
        "text": "What happens to an egg cell that is not fertilised within "
                "about a day of release?",
        "options": [
            {"text": "It travels on and embeds in the uterus lining anyway",
             "correct": False,
             "why": "Only a fertilised cell embeds. An unfertilised egg never "
                    "gets that far."},
            {"text": "It breaks down where it is", "correct": True},
            {"text": "It returns to the ovary and waits for the next month",
             "correct": False,
             "why": "Nothing in the oviduct travels backwards, and no egg cell "
                    "is ever released twice."},
            {"text": "It divides on its own into a ball of cells",
             "correct": False,
             "why": "Dividing starts only once two nuclei have fused. An "
                    "unfertilised egg divides not at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e18",
        "band": "easier",
        "text": "Which happens first, fertilisation or implantation?",
        "options": [
            {"text": "Implantation, a few hours earlier", "correct": False,
             "why": "Nothing can embed before there is a fertilised cell to "
                    "embed. The order runs the other way."},
            {"text": "Neither — at the same moment", "correct": False,
             "why": "They are days apart and in different organs — one in the "
                    "oviduct, the other in the uterus."},
            {"text": "Fertilisation, about five days earlier", "correct": True},
            {"text": "Whichever the sperm reaches first", "correct": False,
             "why": "The sperm plays no part in implantation. The order of the "
                    "two events never changes."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e19",
        "band": "easier",
        "text": "What does a sperm cell use its tail for?",
        "options": [
            {"text": "Holding on to the egg cell once it arrives",
             "correct": False,
             "why": "Nothing grips with a tail. One sperm passes through the "
                    "outer layer, and the tail has done its work by then."},
            {"text": "Swimming towards the egg cell", "correct": True},
            {"text": "Storing the sugar it uses on the journey",
             "correct": False,
             "why": "A sperm carries almost no store at all. Its sugar comes "
                    "from the fluid around it."},
            {"text": "Carrying its chromosomes", "correct": False,
             "why": "The chromosomes are in the nucleus, inside the head. The "
                    "tail carries nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e20",
        "band": "easier",
        "text": "An egg cell is a tenth of a millimetre across. What does "
                "that mean for seeing one?",
        "options": [
            {"text": "It is just visible without a microscope",
             "correct": True},
            {"text": "It can be seen clearly and its parts made out",
             "correct": False,
             "why": "At a tenth of a millimetre it is a speck at best. Making "
                    "out the parts inside needs a microscope."},
            {"text": "It is far too small to see by any means",
             "correct": False,
             "why": "It is the largest cell in the body, and it is the one "
                    "human cell that does not need a microscope at all."},
            {"text": "It can be seen only once it has been fertilised",
             "correct": False,
             "why": "Fertilisation adds a nucleus, not size. The cell is the "
                    "same width before and after."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e21",
        "band": "easier",
        "text": "Which gamete is expensive to make, and is therefore made in "
                "small numbers?",
        "options": [
            {"text": "The sperm cell, because it has to swim so far",
             "correct": False,
             "why": "Swimming is what a sperm does, not what it costs. Sperm "
                    "are the cheap gamete and are made in vast numbers."},
            {"text": "Both, which is why neither is made in large numbers",
             "correct": False,
             "why": "Hundreds of millions of sperm are released at a time. "
                    "Only one of the two is made sparingly."},
            {"text": "Neither, since a cell costs a body almost nothing",
             "correct": False,
             "why": "An egg carries cytoplasm, mitochondria and a food store, "
                    "and all of it has to be built before release."},
            {"text": "The egg cell, because of everything it carries",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e22",
        "band": "easier",
        "text": "What is the first step of the process called, in which one "
                "egg cell leaves an ovary?",
        "options": [
            {"text": "Fertilisation", "correct": False,
             "why": "Fertilisation is the third step, and it happens only if "
                    "a sperm's nucleus fuses with the egg's."},
            {"text": "Transfer and travel", "correct": False,
             "why": "Transfer and travel is the sperm's journey in, and it "
                    "starts in the vagina rather than in an ovary."},
            {"text": "Implantation", "correct": False,
             "why": "Implantation is the last step, days later, and it happens "
                    "in the uterus rather than the ovary."},
            {"text": "Release", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e23",
        "band": "easier",
        "text": "Roughly how many mitochondria does a sperm cell carry?",
        "options": [
            {"text": "A few dozen", "correct": True},
            {"text": "None at all", "correct": False,
             "why": "It has some, and it needs them: they release the energy "
                    "that drives the tail."},
            {"text": "Hundreds of thousands", "correct": False,
             "why": "That is the egg cell's count, and those are the ones a "
                    "new organism inherits."},
            {"text": "Exactly twenty-three", "correct": False,
             "why": "Twenty-three is the chromosome count. Mitochondria are "
                    "not counted out to match it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e24",
        "band": "easier",
        "text": "In which part of the egg cell is its food store held?",
        "options": [
            {"text": "In the nucleus", "correct": False,
             "why": "The nucleus holds the chromosomes. Nothing is stored in "
                    "it."},
            {"text": "In the outer layer", "correct": False,
             "why": "The outer layer is the surface that changes after one "
                    "sperm has fused. It stores nothing."},
            {"text": "In the cytoplasm", "correct": True},
            {"text": "In the mitochondria", "correct": False,
             "why": "Mitochondria release energy from food; they are not where "
                    "the food is kept."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e25",
        "band": "easier",
        "text": "What are the two things a sperm cell brings to fertilisation?",
        "options": [
            {"text": "Chromosomes, and a food store for the first few days",
             "correct": False,
             "why": "The food store is the egg's. A sperm carries almost "
                    "nothing of the kind."},
            {"text": "Cytoplasm, and the machinery for building a body",
             "correct": False,
             "why": "Both of those come from the egg. The sperm brings far "
                    "less material than that."},
            {"text": "A full set of chromosomes, and a tail", "correct": False,
             "why": "The tail is right; the chromosomes are not. It brings half "
                    "a set — 23 — which is the same number the egg brings."},
            {"text": "Chromosomes, and a means of arriving", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e26",
        "band": "easier",
        "text": "How many egg cells are released at a time?",
        "options": [
            {"text": "One", "correct": True},
            {"text": "About four hundred", "correct": False,
             "why": "Four hundred is roughly how many are released across a "
                    "whole lifetime, one at a time."},
            {"text": "Hundreds of millions", "correct": False,
             "why": "That is a count of sperm cells released at a time. Egg "
                    "cells are never released in numbers like that."},
            {"text": "Two", "correct": False,
             "why": "One egg cell finishes maturing and is released, from one "
                    "ovary. Two at once is not the ordinary case."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e27",
        "band": "easier",
        "text": "Which step of the process takes the sperm from the vagina, "
                "through the uterus, and into the oviduct?",
        "options": [
            {"text": "Release", "correct": False,
             "why": "Release is the egg cell leaving an ovary, and it happens "
                    "at the other end of the system."},
            {"text": "Dividing", "correct": False,
             "why": "Dividing is what the fertilised cell does afterwards, "
                    "travelling the other way down the oviduct."},
            {"text": "Transfer and travel", "correct": True},
            {"text": "Implantation", "correct": False,
             "why": "Implantation is the ball of cells embedding in the uterus "
                    "lining, at the very end of the process."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e28",
        "band": "easier",
        "text": "How many sperm cells fuse with one egg cell?",
        "options": [
            {"text": "A few hundred", "correct": False,
             "why": "A few hundred arrive, and they do not all get in. Exactly "
                    "one fuses."},
            {"text": "Two", "correct": False,
             "why": "One sperm brings a whole 23. A second one would take the "
                    "count past 46, which is why the outer layer changes."},
            {"text": "None", "correct": False,
             "why": "One sperm passes through the outer layer, and its nucleus "
                    "fuses with the egg's. That fusing is fertilisation."},
            {"text": "One", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e29",
        "band": "easier",
        "text": "Which gamete carries almost no food store of its own?",
        "options": [
            {"text": "The egg cell", "correct": False,
             "why": "The egg carries a large store in its cytoplasm, and lives "
                    "on it for five days after fertilisation."},
            {"text": "Neither — both carry enough for five days",
             "correct": False,
             "why": "Five days of dividing is paid for out of the egg's store "
                    "alone. The sperm contributes nothing to it."},
            {"text": "Both of them, before fertilisation", "correct": False,
             "why": "Only one of them travels light. The egg's store is loaded "
                    "before it is ever released."},
            {"text": "The sperm cell", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-e30",
        "band": "easier",
        "text": "After about five days of dividing, what has the single "
                "fertilised cell become?",
        "options": [
            {"text": "A ball of cells", "correct": True},
            {"text": "One larger cell", "correct": False,
             "why": "Dividing makes more cells rather than a bigger one. The "
                    "cell has become many, not larger."},
            {"text": "Two gametes again, ready to fuse", "correct": False,
             "why": "The gametes stopped existing at fusion. Nothing after "
                    "that point is a gamete."},
            {"text": "A fully formed embryo with organs", "correct": False,
             "why": "It is a ball of cells and nothing more when it arrives. "
                    "Organs come much later."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-02-s08",
        "band": "standard",
        "text": "A sperm cell is 0.005 mm long and swims about 15 cm. Roughly "
                "how many of its own lengths is that?",
        "options": [
            {"text": "About 300", "correct": False,
             "why": "This divides 15 by 0.005 and forgets the units. 15 cm is "
                    "150 mm, and that is what has to be divided."},
            {"text": "About 3000", "correct": False,
             "why": "This divides 150 mm by 0.05 mm. The sperm is 0.005 mm, so "
                    "a factor of ten has slipped out."},
            {"text": "About 30 000", "correct": True},
            {"text": "About 300 000", "correct": False,
             "why": "This takes a centimetre as a thousand millimetres. It is "
                    "ten, so 15 cm is 150 mm and the answer is ten times "
                    "smaller."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s09",
        "band": "standard",
        "text": "Only one sperm cell fuses with the egg. Suggest why hundreds "
                "of millions are released.",
        "options": [
            {"text": "Because almost all of them are lost on the journey, and "
                     "only a few hundred arrive", "correct": True},
            {"text": "Because the egg needs many sperm around it before one "
                     "can be let in through the outer layer", "correct": False,
             "why": "Nothing about the egg waits for a crowd. The outer layer "
                    "changes the moment one nucleus has fused."},
            {"text": "Because each sperm carries only a few chromosomes, so "
                     "many are needed to make up a full set", "correct": False,
             "why": "One sperm carries a complete 23, which is exactly half a "
                    "set. No topping up is needed or possible."},
            {"text": "Because the sperm that arrive first are usually the "
                     "faulty ones and are turned away", "correct": False,
             "why": "There is no sorting of that kind. The losses happen "
                    "across a 15 cm journey, not at the door."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s10",
        "band": "standard",
        "text": "A student lists the five steps out of order. Which listing "
                "is right?",
        "options": [
            {"text": "Release, transfer and travel, dividing, fertilisation, "
                     "implantation", "correct": False,
             "why": "Nothing divides before the two nuclei have fused. "
                    "Fertilisation comes before dividing, not after it."},
            {"text": "Transfer and travel, release, fertilisation, dividing, "
                     "implantation", "correct": False,
             "why": "The egg is released and already moving along the oviduct "
                    "before any sperm reach it."},
            {"text": "Release, transfer and travel, fertilisation, dividing, "
                     "implantation", "correct": True},
            {"text": "Release, fertilisation, transfer and travel, "
                     "implantation, dividing", "correct": False,
             "why": "The sperm have to arrive before anything can fuse, and "
                    "the dividing happens on the way to the uterus."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s11",
        "band": "standard",
        "text": "Fertilisation happens in the oviduct and implantation in the "
                "uterus. What makes the journey between them, and how long "
                "does it take?",
        "options": [
            {"text": "The unfertilised egg cell, over about a day",
             "correct": False,
             "why": "An unfertilised egg breaks down where it is. What travels "
                    "on is a cell that has already been fertilised."},
            {"text": "A single fertilised cell, arriving within hours",
             "correct": False,
             "why": "It is not single for long and it is not quick: it divides "
                    "as it goes, and the trip takes about five days."},
            {"text": "A ball of cells, dividing as it goes, over about five "
                     "days", "correct": True},
            {"text": "One sperm cell carrying the egg with it, over about five "
                     "days", "correct": False,
             "why": "The sperm's part ends at fusion. What travels on is one "
                    "cell that came from both of them."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s12",
        "band": "standard",
        "text": "Identical twins begin as one fertilised cell. At what point "
                "do they become two?",
        "options": [
            {"text": "At fertilisation, when two sperm nuclei fuse with the "
                     "one egg nucleus instead of one", "correct": False,
             "why": "That would give a single cell with 69 chromosomes rather "
                    "than two embryos. The outer layer normally prevents it."},
            {"text": "After fertilisation, when the ball of cells splits in "
                     "two", "correct": True},
            {"text": "Before fertilisation, when the egg cell divides in two",
             "correct": False,
             "why": "An egg cell does not divide before it is fertilised. It "
                    "is fertilised or it breaks down."},
            {"text": "At implantation, when the ball of cells embeds",
             "correct": False,
             "why": "By implantation there are already two embryos or one. "
                    "Embedding does not divide anything."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s13",
        "band": "standard",
        "text": "Which one of the five steps happens whether or not any sperm "
                "cells are present?",
        "options": [
            {"text": "Fertilisation", "correct": False,
             "why": "Fertilisation is a sperm nucleus fusing with an egg "
                    "nucleus. Without sperm there is nothing to fuse."},
            {"text": "Dividing", "correct": False,
             "why": "An unfertilised egg does not divide. It breaks down where "
                    "it is, after about a day."},
            {"text": "Transfer and travel", "correct": False,
             "why": "Transfer and travel IS the sperm's journey, so without "
                    "sperm there is nothing to happen."},
            {"text": "Release", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s14",
        "band": "standard",
        "text": "An egg cell is 0.1 mm across and a sperm cell's head is "
                "0.005 mm. How many times wider is the egg?",
        "options": [
            {"text": "About 5 times wider", "correct": False,
             "why": "The five is a digit in the measurement rather than the "
                    "ratio. 0.1 divided by 0.005 is twenty."},
            {"text": "About 8000 times wider", "correct": False,
             "why": "Eight thousand is the difference in VOLUME. In width the "
                    "two differ by twenty times."},
            {"text": "About 200 times wider", "correct": False,
             "why": "100 thousandths divided by 5 thousandths is 20. The "
                    "division has been left half done."},
            {"text": "About 20 times wider", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s15",
        "band": "standard",
        "text": "The lesson insists that fertilisation and implantation are "
                "two different events. Which two differences does it give?",
        "options": [
            {"text": "They happen in different organs, and several days apart",
             "correct": True},
            {"text": "They happen in the same organ, several days apart",
             "correct": False,
             "why": "One is in the oviduct and one in the uterus, so the "
                    "organs are not the same."},
            {"text": "They happen in different organs, at the same moment",
             "correct": False,
             "why": "About five days separate them, which is most of the "
                    "reason for keeping the two words apart."},
            {"text": "They happen in different organs, and only one of them "
                     "involves a cell dividing", "correct": False,
             "why": "Dividing is a step of its own, between the two. Neither "
                    "fertilisation nor implantation is a division."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s16",
        "band": "standard",
        "text": "Suggest why a sperm cell carries almost no food store of its "
                "own.",
        "options": [
            {"text": "Because a store would add weight, and travelling is "
                     "easier the smaller a cell is", "correct": True},
            {"text": "Because a sperm cell does not respire at all, so it "
                     "needs no food of any kind", "correct": False,
             "why": "It respires hard — that is what the mitochondria behind "
                    "its head are for. It takes its sugar from the fluid "
                    "around it."},
            {"text": "Because the egg cell feeds every sperm that reaches it, "
                     "so no store is needed", "correct": False,
             "why": "A sperm that has reached the egg has already done its "
                    "swimming. The store would be needed earlier, not later."},
            {"text": "Because a sperm's journey is far too short for it to "
                     "need any food", "correct": False,
             "why": "About 15 cm, for a cell 0.005 mm long, is an enormous "
                    "journey. It is a swim that has to be paid for."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s17",
        "band": "standard",
        "text": "Mitochondrial DNA changes only by slow mutation. Why does "
                "that make it useful for measuring time?",
        "options": [
            {"text": "Because mitochondria divide far faster than cells do",
             "correct": False,
             "why": "A fast clock is not the same as a steady one. What makes "
                    "this one readable is that nothing shuffles it."},
            {"text": "Because it is not shuffled each generation, so "
                     "differences build up steadily", "correct": True},
            {"text": "Because every generation adds one change to it, so the "
                     "changes can simply be counted off", "correct": False,
             "why": "Mutation is slow and irregular rather than one per "
                    "generation. The steadiness is in the long run."},
            {"text": "Because it is inherited from both parents, so it records "
                     "twice as much history as the chromosomes",
             "correct": False,
             "why": "It comes down one line only, through egg cells. That is "
                    "precisely why it is not shuffled."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s18",
        "band": "standard",
        "text": "A fertilised cell divides into two, then four, then eight. "
                "How many cells are there after five divisions?",
        "options": [
            {"text": "10", "correct": False,
             "why": "This adds two cells each time. Every cell divides, so the "
                    "number doubles rather than growing by two."},
            {"text": "16", "correct": False,
             "why": "This leaves the first division out. All five count: two, "
                    "four, eight, sixteen, thirty-two."},
            {"text": "25", "correct": False,
             "why": "This multiplies five by five. There is one cell to start "
                    "with, and doubling is not multiplying by five."},
            {"text": "32", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s19",
        "band": "standard",
        "text": "Two days after an egg cell was released, a cell taken from "
                "the oviduct is found to carry 46 chromosomes. What must have "
                "happened?",
        "options": [
            {"text": "The egg cell has doubled its own chromosomes ready to "
                     "divide", "correct": False,
             "why": "An unfertilised egg does not double anything. It stays at "
                    "23 until a sperm nucleus fuses with it."},
            {"text": "Two egg cells have fused together, giving 23 and 23 "
                     "between them", "correct": False,
             "why": "Egg cells do not fuse with each other. The 23 that is "
                    "added comes from a sperm."},
            {"text": "The cell has implanted, which is when the count reaches "
                     "46", "correct": False,
             "why": "Implantation happens in the uterus, days later, and it "
                    "changes no chromosome count."},
            {"text": "Fertilisation, because a gamete carries only 23",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s20",
        "band": "standard",
        "text": "Why can the ball of cells not be supplied by the uterus "
                "until it has implanted?",
        "options": [
            {"text": "Because it has to be embedded in the lining before "
                     "anything can reach it from there", "correct": True},
            {"text": "Because the lining has not finished thickening yet",
             "correct": False,
             "why": "The lining is thickened and held ready in advance. It is "
                    "waiting rather than still being built."},
            {"text": "Because the ball of cells has no need of supply until "
                     "it stops dividing", "correct": False,
             "why": "It is dividing hard for those five days, which is exactly "
                    "why it has to carry the egg's store with it."},
            {"text": "Because the uterus can only supply a cell once it has "
                     "reached forty-six chromosomes", "correct": False,
             "why": "It has carried 46 since fertilisation. The chromosome "
                    "count has nothing to do with being supplied."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s21",
        "band": "standard",
        "text": "An egg cell is released on a Monday morning and is fertilised "
                "that evening. Roughly when would it implant?",
        "options": [
            {"text": "On the Tuesday, about a day later", "correct": False,
             "why": "A day is the egg's fertilisable window, not the journey. "
                    "The dividing cell takes about five days after that."},
            {"text": "On the Saturday or Sunday, about five days later",
             "correct": True},
            {"text": "On the Monday evening, straight after fertilisation",
             "correct": False,
             "why": "Fertilisation happens in the oviduct and implantation in "
                    "the uterus, with a five-day journey in between."},
            {"text": "Two weeks later, once the lining is at its thickest",
             "correct": False,
             "why": "The lining is already thick and held ready. Nothing waits "
                    "a fortnight to embed."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s22",
        "band": "standard",
        "text": "Predict what would happen if a fertilised cell reached the "
                "uterus before the lining had thickened.",
        "options": [
            {"text": "It would divide faster, to make up for the supply it "
                     "was not getting from the lining", "correct": False,
             "why": "Dividing does not speed up to order, and the store it is "
                    "living on is fixed in any case."},
            {"text": "It would be fertilised a second time", "correct": False,
             "why": "Fertilisation happened days earlier in the oviduct, and "
                    "the outer layer changed to stop a second sperm."},
            {"text": "It would have nowhere to embed, so it could not be "
                     "supplied", "correct": True},
            {"text": "It would travel back up the oviduct and wait",
             "correct": False,
             "why": "Nothing travels back. The oviduct moves its contents one "
                    "way, towards the uterus."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s23",
        "band": "standard",
        "text": "Predict what would happen to a newly released egg cell if the "
                "cilia in the oviduct stopped beating.",
        "options": [
            {"text": "It would grow a tail of its own and swim towards the "
                     "uterus instead", "correct": False,
             "why": "An egg cell has no tail and never grows one. Only the "
                    "cheap gamete carries its own propulsion."},
            {"text": "It would move down the oviduct more slowly, but muscle "
                     "in the wall would still move it", "correct": True},
            {"text": "It would be carried the other way, back into the ovary "
                     "it came from", "correct": False,
             "why": "Nothing in the oviduct works in reverse. The egg is "
                    "carried towards the uterus or it goes nowhere."},
            {"text": "It would fall towards the uterus under its own weight, "
                     "as it normally does", "correct": False,
             "why": "Nothing inside the body is moved by falling. The egg goes "
                    "the same way whichever way up a person is."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s24",
        "band": "standard",
        "text": "A cell is found to have 23 chromosomes, a tail, and a few "
                "dozen mitochondria behind its head. What is it?",
        "options": [
            {"text": "An egg cell", "correct": False,
             "why": "An egg carries hundreds of thousands of mitochondria and "
                    "has no tail at all."},
            {"text": "A fertilised cell", "correct": False,
             "why": "A fertilised cell carries 46 chromosomes and has no tail. "
                    "Twenty-three means a gamete."},
            {"text": "A sperm cell", "correct": True},
            {"text": "A cell of the uterus lining", "correct": False,
             "why": "An ordinary body cell carries 46 chromosomes. A count of "
                    "23 rules it out at once."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s25",
        "band": "standard",
        "text": "A few hundred sperm cells arrive at the oviduct and one "
                "fuses. Roughly what share of those that arrived is that?",
        "options": [
            {"text": "About half of them, since only some of the arrivals get "
                     "as far as the egg", "correct": False,
             "why": "Exactly one fuses, whatever number arrive. Half of a few "
                    "hundred is over a hundred."},
            {"text": "About one in a few hundred", "correct": True},
            {"text": "About one in a million", "correct": False,
             "why": "One in a million covers all the sperm that set out. Among "
                    "those that arrive the share is far larger."},
            {"text": "All of them, since every sperm that arrives fuses with "
                     "part of the egg", "correct": False,
             "why": "One nucleus fuses with one nucleus. The outer layer then "
                    "changes so that no other sperm can enter."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s26",
        "band": "standard",
        "text": "Which step is the fertilised cell carrying out as it travels "
                "down the oviduct?",
        "options": [
            {"text": "Implantation", "correct": False,
             "why": "Implantation happens in the uterus lining, once the "
                    "travelling is over."},
            {"text": "Fertilisation", "correct": False,
             "why": "Fertilisation is over by then — it is what made the cell "
                    "a fertilised one in the first place."},
            {"text": "Dividing", "correct": True},
            {"text": "Transfer and travel", "correct": False,
             "why": "Transfer and travel is the sperm's journey in, before "
                    "fertilisation, and it runs the other way."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s27",
        "band": "standard",
        "text": "An egg cell can be fertilised for only about a day, and the "
                "sperm's journey takes time. Why does that make timing matter?",
        "options": [
            {"text": "Because the sperm have to be in the oviduct within that "
                     "short window", "correct": True},
            {"text": "Because the egg cell speeds up towards the end of the "
                     "day, and becomes harder to catch", "correct": False,
             "why": "It is moved at the pace the oviduct moves it. Nothing "
                    "about it accelerates."},
            {"text": "Because a sperm that arrives late will fertilise the egg "
                     "in the uterus instead of the oviduct", "correct": False,
             "why": "Fertilisation happens in the oviduct and nowhere else, "
                    "whenever the sperm arrive."},
            {"text": "Because the egg can only be fertilised as it leaves "
                     "the ovary", "correct": False,
             "why": "It has about a day, which is a window rather than a "
                    "moment — just a short one."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s28",
        "band": "standard",
        "text": "Six days after an egg cell was released, a ball of cells is "
                "found embedded in the uterus lining. Which two events must "
                "already have happened, in order?",
        "options": [
            {"text": "Implantation in the oviduct, then fertilisation in the "
                     "uterus", "correct": False,
             "why": "Both places are wrong and so is the order. Fertilisation "
                    "is in the oviduct and implantation in the uterus."},
            {"text": "Fertilisation in the oviduct, then implantation in the "
                     "uterus", "correct": True},
            {"text": "Fertilisation in the uterus, then implantation in the "
                     "lining just above it", "correct": False,
             "why": "Fertilisation happens in the oviduct. Nothing fuses in "
                    "the uterus at any point."},
            {"text": "Dividing in the ovary, then fertilisation on the way "
                     "down the oviduct", "correct": False,
             "why": "Nothing divides in the ovary, and dividing only starts "
                    "once the cell has been fertilised."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s29",
        "band": "standard",
        "text": "A student calls a gamete “half a cell”. What is wrong with "
                "that description?",
        "options": [
            {"text": "It is a whole cell, with half a set of chromosomes "
                     "inside it", "correct": True},
            {"text": "It is half a cell, but only until the two halves fuse "
                     "into a whole one at fertilisation", "correct": False,
             "why": "Two whole cells meet, and one nucleus fuses with another. "
                    "Neither of them was ever half a cell."},
            {"text": "It is two cells rather than one, a head and a tail",
             "correct": False,
             "why": "A sperm is a single cell, tail included, and an egg cell "
                    "has no tail to count."},
            {"text": "It is a whole cell with a whole set of chromosomes",
             "correct": False,
             "why": "The chromosomes really are halved: 23 rather than 46. It "
                    "is the CELL that is whole."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-s30",
        "band": "standard",
        "text": "Take a sperm cell as carrying 50 mitochondria and an egg cell "
                "as carrying 200 000. Roughly how many times more does the egg "
                "carry?",
        "options": [
            {"text": "About 4000 times", "correct": True},
            {"text": "About 400 times", "correct": False,
             "why": "This takes the egg's count as 20 000. A zero has been "
                    "dropped: 200 000 divided by 50 is four thousand."},
            {"text": "About 40 times", "correct": False,
             "why": "This divides 200 by 5. The thousands have been thrown "
                    "away on one side only."},
            {"text": "About 10 000 times", "correct": False,
             "why": "This divides by 20. The sperm's count is 50, and 200 000 "
                    "divided by 50 is four thousand."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-02-h08",
        "band": "harder",
        "text": "Volume goes as the cube of the diameter. If an egg cell were "
                "only ten times the width of a sperm head, how many times the "
                "volume would it be?",
        "options": [
            {"text": "About 30 times", "correct": False,
             "why": "This multiplies by three instead of cubing. Ten cubed is "
                    "ten times ten times ten."},
            {"text": "About 100 times", "correct": False,
             "why": "Ten in two directions gives an area. A volume takes all "
                    "three, so it is ten times larger again."},
            {"text": "About 1000 times", "correct": True},
            {"text": "About 8000 times", "correct": False,
             "why": "Eight thousand comes from twenty cubed, the real width "
                    "ratio. At ten times the width it would be a thousand."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h09",
        "band": "harder",
        "text": "Mitochondrial DNA traces an unbroken line back through the "
                "generations. A student says it therefore traces all of a "
                "person's ancestors. Evaluate that.",
        "options": [
            {"text": "It is right: every ancestor contributed mitochondria",
             "correct": False,
             "why": "Only one line contributed any. A sperm's mitochondria are "
                    "destroyed after fusion, so half the ancestors at each "
                    "step leave nothing."},
            {"text": "It is wrong: it traces one line of egg cells, which is a "
                     "single ancestor at each generation", "correct": True},
            {"text": "It is right for the last few generations, and stops "
                     "being right further back than that", "correct": False,
             "why": "The restriction is the same at every generation. It has "
                    "always been one line and never all of them."},
            {"text": "It is wrong, because mitochondrial DNA is shuffled with "
                     "the chromosomes at every fertilisation", "correct": False,
             "why": "It is never shuffled with anything — that is exactly why "
                    "it can be read as a clock."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h10",
        "band": "harder",
        "text": "Why can mitochondrial DNA be read as a clock, when the DNA in "
                "the chromosomes cannot be read in the same simple way?",
        "options": [
            {"text": "Because the chromosomes are shuffled at every "
                     "generation, and the mitochondria's DNA is not",
             "correct": True},
            {"text": "Because the chromosomes mutate so slowly that no change "
                     "can be measured in them at all", "correct": False,
             "why": "They mutate too. What makes them hard to read is that "
                    "each generation mixes two sets together."},
            {"text": "Because a mitochondrion carries far more DNA than a "
                     "chromosome does, so it records more", "correct": False,
             "why": "It carries a small loop, much less than a chromosome. "
                    "Being unmixed, not being large, is what matters."},
            {"text": "Because only mitochondrial DNA is inherited at all",
             "correct": False,
             "why": "The chromosomes are inherited exactly — 23 from each "
                    "gamete. Nothing is rebuilt from scratch."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h11",
        "band": "harder",
        "text": "Suppose an egg cell's outer layer changed before any sperm "
                "had fused with it. Predict what would follow.",
        "options": [
            {"text": "Two sperm would fuse instead of one", "correct": False,
             "why": "The change is what keeps sperm out. Making it happen "
                    "earlier lets fewer in, not more."},
            {"text": "No sperm could enter, so no fertilisation could happen",
             "correct": True},
            {"text": "Fertilisation would happen as usual, but in the uterus "
                     "rather than in the oviduct", "correct": False,
             "why": "Fertilisation happens in the oviduct and nowhere else, "
                    "and a sealed egg cannot be fertilised anywhere."},
            {"text": "The egg would divide on its own, and implant in the "
                     "lining about five days later", "correct": False,
             "why": "An unfertilised egg does not divide. It breaks down where "
                    "it is, after about a day."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h12",
        "band": "harder",
        "text": "A student writes: “The sperm and the egg both divide, and "
                "that is how the embryo is made.” What is wrong with that?",
        "options": [
            {"text": "Only the sperm divides; the egg supplies the material "
                     "for the new cells that result", "correct": False,
             "why": "Neither gamete divides. The sperm's part is over the "
                    "moment its nucleus has fused."},
            {"text": "The two gametes fuse into one cell, and it is that cell "
                     "which then divides", "correct": True},
            {"text": "Only the egg divides, before any sperm reaches it",
             "correct": False,
             "why": "An egg does not divide unfertilised. Dividing starts only "
                    "after the two nuclei have fused."},
            {"text": "Both divide, and the sperm's halves are then destroyed",
             "correct": False,
             "why": "The mitochondria are destroyed; the sperm never divides "
                    "at all, so there are no halves."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h13",
        "band": "harder",
        "text": "An animal's egg cells are found to carry no food store at "
                "all. What must be true about what happens after "
                "fertilisation?",
        "options": [
            {"text": "Its fertilised cells must divide for far longer",
             "correct": False,
             "why": "Dividing is exactly what costs material. With no store, "
                    "less dividing can be paid for, not more."},
            {"text": "Its fertilised cells must be supplied from somewhere "
                     "else almost at once", "correct": True},
            {"text": "Its eggs must carry more chromosomes instead",
             "correct": False,
             "why": "Chromosomes are instructions rather than supplies, and "
                    "their number is set by the species."},
            {"text": "Its sperm cells must carry the food store instead, and "
                     "hand it over at fertilisation", "correct": False,
             "why": "A sperm is small precisely because it carries nothing. "
                    "Loading it would undo what makes it able to travel."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h14",
        "band": "harder",
        "text": "In humans a gamete carries 23 chromosomes and a body cell "
                "carries 46. In a species whose body cells carry 78, how many "
                "does each gamete carry?",
        "options": [
            {"text": "78", "correct": False,
             "why": "This gives a gamete the species' full set. Two full sets "
                    "fusing would double the number every generation."},
            {"text": "23", "correct": False,
             "why": "Twenty-three is half of the HUMAN number. The rule is "
                    "half the species' own count."},
            {"text": "39", "correct": True},
            {"text": "156", "correct": False,
             "why": "This doubles instead of halving, and 78 is already the "
                    "body cell's count rather than the gamete's."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h15",
        "band": "harder",
        "text": "The lesson dates the start of a pregnancy to implantation "
                "rather than to fertilisation. What has to be true at "
                "implantation that is not true before it?",
        "options": [
            {"text": "The cell has a full set of 46 chromosomes for the first "
                     "time, which it did not have on the journey",
             "correct": False,
             "why": "It has carried 46 since fertilisation, five days "
                    "earlier. Nothing about the count changes on arrival."},
            {"text": "The embryo is embedded where it can be supplied, rather "
                     "than living on what it set out with", "correct": True},
            {"text": "The embryo has finished dividing, and begins growing "
                     "instead once it has arrived", "correct": False,
             "why": "Dividing does not stop at implantation. What changes is "
                    "where the material for it comes from."},
            {"text": "The lining of the uterus begins to thicken, now that "
                     "there is something in it to hold", "correct": False,
             "why": "The lining thickened in advance and was held ready. It "
                    "does not wait to be asked."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h16",
        "band": "harder",
        "text": "A student argues that because the egg supplies all the "
                "mitochondria, it must supply more than half of everything a "
                "new organism inherits. Evaluate that.",
        "options": [
            {"text": "It is right, and it is why an egg is thousands of times "
                     "the volume of a sperm cell", "correct": False,
             "why": "The volume difference is packing material. It says "
                    "nothing about the split of the chromosomes."},
            {"text": "It is wrong, because mitochondria carry no DNA of their "
                     "own for anything to be inherited from", "correct": False,
             "why": "They carry a small loop of their own DNA, and it is "
                    "inherited. That is what makes the clock possible."},
            {"text": "It is right, because the sperm's chromosomes are "
                     "destroyed after fusion along with its mitochondria",
             "correct": False,
             "why": "Only the mitochondria are destroyed. The sperm's 23 "
                    "chromosomes are half of the new cell's set."},
            {"text": "The chromosomes are split exactly 23 and 23, so the "
                     "mitochondria are a small extra rather than a majority",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h17",
        "band": "harder",
        "text": "Put these four events into the order in which they happen: "
                "the outer layer changes; the two nuclei fuse; the ball of "
                "cells embeds; the egg leaves the ovary.",
        "options": [
            {"text": "The egg leaves the ovary; the outer layer changes; the "
                     "two nuclei fuse; the ball of cells embeds",
             "correct": False,
             "why": "The layer changes because a nucleus has fused. Putting it "
                    "first would keep every sperm out."},
            {"text": "The two nuclei fuse; the egg leaves the ovary; the outer "
                     "layer changes; the ball of cells embeds",
             "correct": False,
             "why": "Nothing can fuse before the egg has been released into "
                    "the oviduct, which is the only place fusing happens."},
            {"text": "The egg leaves the ovary; the two nuclei fuse; the outer "
                     "layer changes; the ball of cells embeds", "correct": True},
            {"text": "The egg leaves the ovary; the two nuclei fuse; the ball "
                     "of cells embeds; the outer layer changes",
             "correct": False,
             "why": "The layer changes within moments of fusion, days before "
                    "anything embeds anywhere."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h18",
        "band": "harder",
        "text": "Suggest why the mitochondria are not shuffled between the two "
                "gametes at fertilisation, when the chromosomes are.",
        "options": [
            {"text": "Because a mitochondrion is far too large to pass into a "
                     "nucleus, so it stays outside and is shared out later",
             "correct": False,
             "why": "Nothing is shared out later. The sperm's are destroyed, "
                    "and the egg's are the whole of what the new cell has."},
            {"text": "Because mitochondria carry no DNA, so there is nothing "
                     "in them to shuffle in the first place", "correct": False,
             "why": "They carry a small loop of DNA of their own, which is "
                    "why the question of shuffling arises at all."},
            {"text": "Because the two nuclei fuse while the mitochondria do "
                     "not, and the sperm's are destroyed", "correct": True},
            {"text": "Because the egg's mitochondria are made fresh after "
                     "fertilisation, from the food store in the cytoplasm",
             "correct": False,
             "why": "They were in the egg all along, in their hundreds of "
                    "thousands, and are inherited as they are."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h19",
        "band": "harder",
        "text": "The lesson closes on “equal genetic contribution, radically "
                "unequal material contribution”. Which observation supports "
                "each half?",
        "options": [
            {"text": "The 23 chromosomes each supports the first half; the "
                     "food store and cytoplasm support the second",
             "correct": True},
            {"text": "The 23 chromosomes each supports the second half; the "
                     "difference in numbers released supports the first",
             "correct": False,
             "why": "The chromosome count is the genetic half of the claim, "
                    "and how many are released is about cost rather than "
                    "either half."},
            {"text": "The tail and the mitochondria support the first half; "
                     "the chromosome count supports the second",
             "correct": False,
             "why": "Both of those are material rather than genetic, and the "
                    "chromosome count is the one measurement that is equal."},
            {"text": "Nothing in the lesson supports the first half, because "
                     "the two cells differ in every measurement taken",
             "correct": False,
             "why": "They match exactly on one: 23 chromosomes each. That is "
                    "the observation the first half rests on."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h20",
        "band": "harder",
        "text": "An animal releases about 500 egg cells at a time and a few "
                "thousand sperm. Using the lesson's reasoning about numbers, "
                "what does that suggest?",
        "options": [
            {"text": "That its sperm must be far more expensive to make than a "
                     "human sperm cell is, cell for cell", "correct": False,
             "why": "Nothing here measures a sperm against a human one. What "
                    "the numbers compare is the two gametes of this animal."},
            {"text": "That the two gametes cost that animal much more nearly "
                     "the same as each other", "correct": True},
            {"text": "That its egg cells must carry far more chromosomes than "
                     "its sperm cells carry", "correct": False,
             "why": "The two gametes of a species carry the same number, half "
                    "a set each. Numbers released say nothing about it."},
            {"text": "That fertilisation in that animal must happen inside the "
                     "body, as it does in humans", "correct": False,
             "why": "Where fertilisation happens is a separate question "
                    "entirely, and these numbers do not decide it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h21",
        "band": "harder",
        "text": "One pair of people differ at 6 places in their "
                "mitochondrial DNA; another pair differ at 18. What does that "
                "suggest?",
        "options": [
            {"text": "That the second pair's lines of egg cells separated "
                     "longer ago", "correct": True},
            {"text": "That the second pair are more closely related, since "
                     "they have more in common to compare", "correct": False,
             "why": "Differences count against relatedness, not for it. More "
                    "differences means further apart."},
            {"text": "That the first pair must share a father and the second "
                     "pair a mother", "correct": False,
             "why": "Mitochondrial DNA comes down the line of egg cells only, "
                    "so it says nothing at all about fathers."},
            {"text": "That the second pair's mitochondria mutate three times "
                     "as fast as the first pair's do", "correct": False,
             "why": "The method works because the rate is taken as much the "
                    "same for everybody. It is the TIME that differs."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h22",
        "band": "harder",
        "text": "Identical twins share their mitochondrial DNA, and so do "
                "non-identical twins. Why is that true of both kinds?",
        "options": [
            {"text": "Because twins of either kind share a pregnancy, and the "
                     "mitochondria are pooled between them", "correct": False,
             "why": "Nothing is pooled during a pregnancy. Each embryo keeps "
                    "the mitochondria of the egg it grew from."},
            {"text": "Because the mitochondria in every cell come from the egg "
                     "cell, and both kinds come from the same person's eggs",
             "correct": True},
            {"text": "Because identical twins come from one egg and "
                     "non-identical twins from one sperm cell",
             "correct": False,
             "why": "Non-identical twins come from two eggs and two sperm. "
                    "One sperm is never shared between two embryos."},
            {"text": "Because mitochondrial DNA is the same in everybody, so "
                     "any two people share it", "correct": False,
             "why": "It differs between people, which is what makes it usable "
                    "for tracing a line at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h23",
        "band": "harder",
        "text": "A student writes that a sperm cell “gives half its "
                "chromosomes to the egg”. What is wrong with the wording?",
        "options": [
            {"text": "It gives all 23 that it has, and 23 is already half a "
                     "set", "correct": True},
            {"text": "It gives none of them away at all: the two sets stay "
                     "separate inside the fertilised cell", "correct": False,
             "why": "The two nuclei fuse into one, which is what fertilisation "
                    "is. Nothing stays separate afterwards."},
            {"text": "It gives half of 46, which is why the fertilised cell "
                     "ends up carrying 23", "correct": False,
             "why": "The fertilised cell carries 46. A sperm never held 46 to "
                    "halve in the first place."},
            {"text": "It gives twice what the egg gives, because the egg's "
                     "half set is already inside the cell", "correct": False,
             "why": "The two contributions are exactly equal, at 23 each. That "
                    "is the lesson's whole point about genetic contribution."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h24",
        "band": "harder",
        "text": "One cell in an ovary carries 23 chromosomes and one in an "
                "oviduct carries 46. Which is which, and what separates them?",
        "options": [
            {"text": "The 23 is a fertilised cell and the 46 an egg cell; the "
                     "count halves when a cell is fertilised", "correct": False,
             "why": "Fertilisation adds a half set rather than removing one. "
                    "It takes the count up to 46, not down to 23."},
            {"text": "Both are egg cells, and the count depends on how far "
                     "along the oviduct each one has travelled",
             "correct": False,
             "why": "Travelling changes nothing about a chromosome count. Only "
                    "fusing with a sperm nucleus does."},
            {"text": "The 23 is an egg cell before fusion and the 46 a "
                     "fertilised cell; fertilisation is what separates them",
             "correct": True},
            {"text": "The 23 is an egg cell and the 46 an ordinary body cell "
                     "of the ovary that has been collected by mistake",
             "correct": False,
             "why": "An ordinary body cell does carry 46, but this one is in "
                    "the oviduct and the egg released into it has been "
                    "fertilised."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h25",
        "band": "harder",
        "text": "Comparing mitochondrial DNA across living people traces "
                "everyone back to one maternal ancestor in Africa. What does "
                "that conclusion rest on?",
        "options": [
            {"text": "On mitochondrial DNA passing unshuffled down egg cells "
                     "and changing only by slow mutation", "correct": True},
            {"text": "On mitochondrial DNA being identical in every person "
                     "alive, which points back to a single origin",
             "correct": False,
             "why": "It is not identical — the small differences between "
                    "people are the whole of the evidence."},
            {"text": "On the chromosomes being compared at the same time, "
                     "which is what fixes the place and the date",
             "correct": False,
             "why": "The chromosomes are shuffled every generation, which is "
                    "why this particular line of evidence uses mitochondria "
                    "instead."},
            {"text": "On mitochondria being inherited from both gametes, so "
                     "that every line of ancestry is covered", "correct": False,
             "why": "They come from the egg alone. A single line is exactly "
                    "what the method can follow."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h26",
        "band": "harder",
        "text": "In some animals the gametes are shed into water and meet "
                "there. Which of the five human steps would have no "
                "equivalent?",
        "options": [
            {"text": "Fertilisation and dividing, which need a body",
             "correct": False,
             "why": "Both happen perfectly well in water. It is the steps that "
                    "need another body that go."},
            {"text": "Release and fertilisation, because the water does both "
                     "of those for the animal", "correct": False,
             "why": "The animal still releases its own gametes, and water "
                    "cannot fuse two nuclei."},
            {"text": "Transfer and travel, and implantation", "correct": True},
            {"text": "Dividing and implantation, because a fertilised cell in "
                     "water has nothing to live on", "correct": False,
             "why": "Its egg's own food store is what it lives on, exactly as "
                    "in a human. Dividing still happens."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h27",
        "band": "harder",
        "text": "Suppose an egg cell could be fertilised for only an hour "
                "after release rather than about a day. Predict the effect.",
        "options": [
            {"text": "None, because the sperm arrive within minutes of being "
                     "transferred into the vagina", "correct": False,
             "why": "The journey is about 15 cm for a cell 0.005 mm long. "
                    "Nothing about it is over in minutes."},
            {"text": "Fertilisation would happen in the uterus instead, since "
                     "the egg would still be higher up the oviduct",
             "correct": False,
             "why": "Fertilisation happens in the oviduct and nowhere else. A "
                    "shorter window does not move it."},
            {"text": "Fertilisation would become far less likely, because the "
                     "sperm's journey takes time", "correct": True},
            {"text": "The egg would be moved along the oviduct much faster, to "
                     "make up for the shorter window", "correct": False,
             "why": "The oviduct moves it at the pace it moves it. Nothing "
                    "speeds up to suit the egg."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h28",
        "band": "harder",
        "text": "A student writes: “The egg has 8000 times the volume, so it "
                "has 8000 times the chromosomes.” Identify both errors.",
        "options": [
            {"text": "The 8000 is a width rather than a volume, and "
                     "chromosome number does scale with a cell's size",
             "correct": False,
             "why": "Eight thousand is the volume figure, from a twentyfold "
                    "width. And chromosome number does not scale with size: "
                    "both gametes carry 23."},
            {"text": "The 8000 belongs to the volume, but both cells carry 23 "
                     "chromosomes, so the second half does not follow",
             "correct": True},
            {"text": "The 8000 belongs to the width, and the chromosome count "
                     "is 46 in both gametes rather than a multiple",
             "correct": False,
             "why": "The width ratio is twenty, and a gamete carries 23 rather "
                    "than 46."},
            {"text": "Neither is an error, since a larger cell needs more "
                     "chromosomes to run all of that extra material",
             "correct": False,
             "why": "Volume and chromosome number are unconnected. The two "
                    "gametes match exactly at 23 each, whatever their size."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h29",
        "band": "harder",
        "text": "In which organ does each of the last three steps happen: "
                "fertilisation, dividing, and implantation?",
        "options": [
            {"text": "Oviduct, uterus, uterus", "correct": False,
             "why": "The dividing happens on the way, in the oviduct. The cell "
                    "is a ball of cells by the time it reaches the uterus."},
            {"text": "Uterus, oviduct, uterus", "correct": False,
             "why": "Fertilisation is in the oviduct and nowhere else, which "
                    "is the claim the whole lesson is built around."},
            {"text": "Oviduct, oviduct, uterus", "correct": True},
            {"text": "Oviduct, oviduct, oviduct", "correct": False,
             "why": "Implantation is in the lining of the uterus. Being in a "
                    "different organ is half of what separates it from "
                    "fertilisation."},
        ],
        "figure": None,
    },
    {
        "id": "b5-02-h30",
        "band": "harder",
        "text": "Suppose an egg cell carried no mitochondria of its own, and a "
                "sperm cell's survived fusion instead. What would change about "
                "what a new organism inherits?",
        "options": [
            {"text": "Nothing would change, because mitochondria carry no "
                     "inherited information of their own", "correct": False,
             "why": "They carry a small loop of DNA, and it is inherited. That "
                    "loop is what the maternal line is traced along."},
            {"text": "Its mitochondria, and their DNA, would come down the "
                     "other line instead", "correct": True},
            {"text": "It would inherit no mitochondria at all, and would have "
                     "to build its own after fertilisation", "correct": False,
             "why": "The sperm's would be there, by the terms of the question. "
                    "Where they came from is what has changed."},
            {"text": "Its chromosomes would come from the sperm alone",
             "correct": False,
             "why": "Chromosomes and mitochondria are inherited separately. "
                    "The 23-and-23 split is untouched by any of this."},
        ],
        "figure": None,
    },
]
