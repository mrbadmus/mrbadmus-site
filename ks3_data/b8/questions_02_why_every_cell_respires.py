"""B8 lesson 02 — Why every cell respires: twelve questions (MRB-269).

The lesson claims the second clause of the respiration bullet — the breakdown of
organic molecules enabling *all the other chemical processes necessary for life*
— and the bank is built to test that clause rather than the reaction itself.
Three things carry it. First, what respiration is and is not: a reaction inside
every living cell, not breathing, with mitochondria as the machinery and no
oxygen store anywhere to fall back on. Second, the four jobs the energy pays
for — movement, building large molecules, active transport, keeping warm — of
which only the first is visible from outside. Third, the bench's five cells,
whose energy budgets are the evidence: a nerve cell spending 65% on pumping ions
after every signal, a white blood cell building mitochondria before it works
harder, a sperm cell with its mitochondria wrapped around the base of the tail.

The easier band checks the four things a student must hold before any of it
works — respiration is not breathing, a mitochondrion is where aerobic
respiration happens, the energy pays for four jobs and not one, and every living
cell of a plant respires. The standard band puts them back on the bench: why the
nerve cell fails fastest, why a person sitting still still cannot hold their
breath, why a white blood cell builds machinery in advance, and why the sperm
cell's mitochondria sit where they do. The harder band takes the ideas somewhere
the page did not go: the brain's share of resting energy, a gut lining cell
pulling glucose uphill, a twenty-four-hour greenhouse, and a bird's flight
muscle beside a lizard's leg.

Both declared misconceptions supply distractors throughout. RESP-03 ("plants
photosynthesise, animals respire") drives the reversed definition in e01, the
chloroplast option in e02, the whole of e04, and the greenhouse student in h03 —
attacked in its light-side form, since the ladder already owns the dark-cupboard
version. RESP-04 ("you respire when you need energy — when you exercise") drives
the resting-cell option in e03, the whole of s02, the "thinking is hard work"
opening of h01, and the bird that builds mitochondria only while flying in h04.
Two further errors the lesson exists to correct supply the rest: that something
somewhere stores oxygen (e02, s03, h01, h02, h04), and that mitochondria do the
work rather than release the energy that pays for it (e02, s03, s04).

`figure` is None throughout, and it has to be — this lesson declares no figures
at all, so no question may depend on a student seeing one.
"""

UNIT = "B8"
LESSON = "why-every-cell-respires"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b8-02-e01",
        "band": "easier",
        "text": "Your friend says: \"Respiration is just another word for "
                "breathing.\" What is wrong with that?",
        "options": [
            {"text": "Respiration releases energy from glucose inside every "
                     "living cell; breathing only supplies the oxygen for "
                     "it.",
             "correct": True},
            {"text": "Nothing is wrong with it — breathing air in and out is "
                     "how your body releases the energy it gets from food.",
             "correct": False,
             "why": "Breathing moves air and releases no energy at all. The "
                    "energy comes out of glucose inside your cells, in "
                    "respiration; breathing is the muscular job that delivers "
                    "the oxygen respiration needs."},
            {"text": "Respiration happens in the lungs, and breathing is the "
                     "movement of the chest muscles that fills them with air.",
             "correct": False,
             "why": "You have breathing right, but respiration does not happen "
                    "in the lungs. It happens inside every living cell you "
                    "own — in your toes, your liver, your bones — and it never "
                    "stops."},
            {"text": "Respiration is what plants do to release energy, and "
                     "breathing is the animal version of exactly the same "
                     "thing.",
             "correct": False,
             "why": "This is the plants-and-animals swap, and it is the wrong "
                    "idea this lesson exists to kill. Plants and animals both "
                    "respire, in every living cell. Plants do not breathe at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-e02",
        "band": "easier",
        "text": "A heart muscle cell contracts about once a second for a whole "
                "lifetime, and by some counts a third of its volume is "
                "mitochondria. What is a mitochondrion?",
        "options": [
            {"text": "The part of a cell that stores oxygen, so the cell can "
                     "keep going for a while if the supply stops.",
             "correct": False,
             "why": "Nothing in the body stores oxygen — a few seconds' worth "
                    "dissolved in the blood is all there is. That is exactly "
                    "why a heart cut off from oxygen is permanently damaged "
                    "within minutes."},
            {"text": "The part of a cell where aerobic respiration happens, "
                     "releasing energy from glucose using oxygen.",
             "correct": True},
            {"text": "The part of a muscle cell that does the contracting, "
                     "which is why muscle carries so many of them.",
             "correct": False,
             "why": "Mitochondria do not contract or move anything themselves. "
                    "They release the energy, and something else in the cell "
                    "spends it — here, on contracting."},
            {"text": "The part of a cell where photosynthesis happens, which "
                     "is why a hard-working cell carries plenty.",
             "correct": False,
             "why": "That is a chloroplast, and only plant cells that get "
                    "light have them. A heart muscle cell has none. "
                    "Mitochondria are where aerobic respiration happens, in "
                    "plant and animal cells alike."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-e03",
        "band": "easier",
        "text": "The energy respiration releases is spent inside the cell. "
                "Which list names what it is spent on?",
        "options": [
            {"text": "Movement only — everything else in a cell happens on its "
                     "own, without needing energy.",
             "correct": False,
             "why": "Movement is the only job on the list you can see from "
                    "outside, which is why it is the one everybody names. "
                    "Building a protein, pumping ions uphill and holding you "
                    "at 37 °C all have to be paid for too."},
            {"text": "Movement and keeping warm — building molecules and "
                     "transport both happen by diffusion instead.",
             "correct": False,
             "why": "Diffusion needs no energy, but it only ever moves things "
                    "down a gradient. Active transport goes the other way, "
                    "against the gradient, and joining small molecules into "
                    "large ones is work as well."},
            {"text": "Whichever job you happen to be doing at the time — a "
                     "cell at rest has no energy bill to pay.",
             "correct": False,
             "why": "This is the you-respire-when-you-exercise idea. A resting "
                    "cell is still pumping ions across its membrane, still "
                    "repairing itself and, if you are a mammal, still holding "
                    "you at 37 °C."},
            {"text": "Movement, building large molecules, active transport, "
                     "and in mammals and birds keeping warm.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-e04",
        "band": "easier",
        "text": "Which cells of an oak tree respire?",
        "options": [
            {"text": "Only the leaf cells, because they are the ones that make "
                     "the glucose in the first place.",
             "correct": False,
             "why": "Every living cell in the tree respires, leaves included "
                    "but not only. A root cell is buried in the dark, has no "
                    "chloroplasts, lives on sugar sent down from the leaves — "
                    "and respires exactly as your cells do."},
            {"text": "Only the root cells, because they are the ones with no "
                     "chloroplasts to photosynthesise with.",
             "correct": False,
             "why": "You have spotted that roots must respire, which is right. "
                    "But respiration is not what a cell does instead of "
                    "photosynthesis — a leaf cell in bright light does both at "
                    "once."},
            {"text": "Every living cell in the tree, continuously, day and "
                     "night.",
             "correct": True},
            {"text": "All of them, but only at night, once photosynthesis has "
                     "stopped for the day.",
             "correct": False,
             "why": "Respiration never pauses. In bright light a leaf "
                    "photosynthesises faster than it respires, so the gases "
                    "going in and out look reversed — but the respiration "
                    "underneath never stopped."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b8-02-s01",
        "band": "standard",
        "text": "Cut the oxygen off and the nerve cell on the bench fails "
                "faster than any of the other four. Which explanation fits?",
        "options": [
            {"text": "Nerve cells are the only cells in the body that need "
                     "oxygen, so they are the ones that feel the loss.",
             "correct": False,
             "why": "Every cell on the bench fails without oxygen — the muscle "
                    "cell, the sperm cell and the root hair cell all do. The "
                    "nerve cell is simply quickest, because its bill is the "
                    "largest and never pauses."},
            {"text": "It runs an enormous non-stop bill pumping ions back "
                     "across its membrane, and no cell stores any oxygen.",
             "correct": True},
            {"text": "It is the cell furthest from the heart, so it is the "
                     "last one to get any oxygen that is still left.",
             "correct": False,
             "why": "Distance is not what decides it. Your toes are much "
                    "further from your heart than your brain is, and they "
                    "survive far longer than four minutes without oxygen."},
            {"text": "It has almost no mitochondria, so it cannot get much "
                     "energy out of the oxygen it does receive.",
             "correct": False,
             "why": "A nerve cell has many mitochondria, concentrated at the "
                    "ends where signals are passed on. A cell with a large "
                    "energy bill carries more of the machinery, not less."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-s02",
        "band": "standard",
        "text": "Sitting completely still in a quiet room, you still cannot "
                "hold your breath for more than a minute or two. What does "
                "that tell you?",
        "options": [
            {"text": "That your lungs are too small to hold enough air for "
                     "longer, whatever your cells happen to be doing.",
             "correct": False,
             "why": "Lung size is not the limit. The limit is that your cells "
                    "cannot stop respiring, and there is no store of oxygen "
                    "anywhere to keep them supplied while you hold your "
                    "breath."},
            {"text": "That your muscles go on respiring at rest, while the "
                     "rest of your cells wait until you move again.",
             "correct": False,
             "why": "Not just the muscles. Sitting still, your heart is "
                    "contracting, your kidneys are filtering, your gut is "
                    "transporting, and every cell you own is pumping ions "
                    "across its membrane."},
            {"text": "That every cell is respiring the whole time, and nothing "
                     "in you stores oxygen for later.",
             "correct": True},
            {"text": "That respiration has stopped, and the discomfort is your "
                     "body demanding that you start it again.",
             "correct": False,
             "why": "Rest is not the state of not respiring — it is the state "
                    "of respiring at your lowest rate. A cell that stops "
                    "respiring is a dead one."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-s03",
        "band": "standard",
        "text": "As soon as an infection begins, a white blood cell starts "
                "building extra mitochondria. Predict why.",
        "options": [
            {"text": "It is about to work much harder, and more mitochondria "
                     "mean more aerobic respiration to pay for it.",
             "correct": True},
            {"text": "Mitochondria attack and digest bacteria, so the cell "
                     "needs more of them to fight off the infection.",
             "correct": False,
             "why": "Mitochondria are where aerobic respiration happens; they "
                    "attack nothing. The cell crawls after the bacterium and "
                    "engulfs it itself — and that is one of the jobs the "
                    "mitochondria pay for."},
            {"text": "Mitochondria are where a cell keeps its oxygen, so extra "
                     "ones let it carry on if the supply drops.",
             "correct": False,
             "why": "No cell stores oxygen — that is why four minutes without "
                    "it does permanent damage. Mitochondria release energy "
                    "from glucose using oxygen; they hold none of it in "
                    "reserve."},
            {"text": "Building them uses up the cell's spare energy, which "
                     "would otherwise go to waste while it waits.",
             "correct": False,
             "why": "Energy is not something a cell has spare and must burn "
                    "off. Building mitochondria costs energy, and the cell "
                    "only does it because a far bigger bill is about to "
                    "arrive."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-s04",
        "band": "standard",
        "text": "A sperm cell spends about 90% of its energy beating its tail, "
                "and its mitochondria sit in a tight spiral around the base of "
                "that tail. Why there?",
        "options": [
            {"text": "Because oxygen enters a sperm cell through the tail, so "
                     "respiration has to happen at that end of it.",
             "correct": False,
             "why": "Oxygen diffuses in across the whole cell surface, not "
                    "through the tail. The mitochondria sit there because that "
                    "is where almost all the energy is spent."},
            {"text": "Because the spiral of mitochondria is the thing that "
                     "whips the tail from side to side as the cell swims.",
             "correct": False,
             "why": "Mitochondria release the energy; they do not do the "
                    "moving. The engine is not the propeller — it is placed "
                    "next to it."},
            {"text": "Because a sperm cell has to store enough energy at the "
                     "start to last the whole of the journey ahead.",
             "correct": False,
             "why": "There is no store to fall back on, and that is the sperm "
                    "cell's whole problem. Cut off its oxygen and it stops "
                    "swimming and cannot start again."},
            {"text": "Because that is where nearly all its energy is spent — "
                     "the machinery is placed right beside the job.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b8-02-h01",
        "band": "harder",
        "text": "The brain is about a fiftieth of your body mass but uses "
                "roughly a fifth of your energy at rest. A student says that "
                "must be because thinking is hard work. What is the better "
                "explanation?",
        "options": [
            {"text": "Most of it pays to pump ions back across nerve cell "
                     "membranes after every signal, day and night.",
             "correct": True},
            {"text": "Thinking is exactly it — the harder you concentrate, the "
                     "more of your energy your brain takes up.",
             "correct": False,
             "why": "Concentrating makes very little difference to the figure. "
                    "The bill is there whether you are solving equations or "
                    "staring out of a window, because it is the cost of "
                    "maintaining nerve cells, not the cost of effort."},
            {"text": "Nerve cells are far larger than other cells, so a fifth "
                     "of your energy is really just their size.",
             "correct": False,
             "why": "Size is not what drives an energy bill. A root hair cell "
                    "is tiny and still spends three quarters of its energy on "
                    "one job. What a cell does decides its bill, not how big "
                    "it is."},
            {"text": "The brain is storing oxygen that the rest of the body "
                     "may need later, and storing it costs energy.",
             "correct": False,
             "why": "There is no oxygen store anywhere in you — a few seconds' "
                    "worth dissolved in the blood is all of it, which is why "
                    "brain cells begin to die within about four minutes "
                    "without it."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-h02",
        "band": "harder",
        "text": "Cells lining the small intestine pull glucose out of the gut "
                "and into the blood, even when there is less glucose in the "
                "gut than there already is inside the cell. What would you "
                "expect these cells to be packed with, and why?",
        "options": [
            {"text": "Chloroplasts, because a cell that handles this much "
                     "sugar needs somewhere of its own to make it.",
             "correct": False,
             "why": "Chloroplasts build glucose using light, and there is no "
                    "light inside a gut. These cells do not make glucose at "
                    "all — they move it uphill, and moving it uphill is what "
                    "has to be paid for."},
            {"text": "Very little of anything, because glucose slides down its "
                     "gradient on its own and needs no energy supply.",
             "correct": False,
             "why": "Read the gradient again. There is less glucose in the gut "
                    "than in the cell, so it is being moved from low to high — "
                    "the opposite direction to diffusion, and impossible "
                    "without energy."},
            {"text": "Stored oxygen, so that the pumping can carry on between "
                     "meals when the blood is busy somewhere else.",
             "correct": False,
             "why": "No cell anywhere holds a store of oxygen. It has to "
                    "arrive continuously, which is why the deadline without it "
                    "is minutes rather than weeks."},
            {"text": "Mitochondria, because moving glucose against the "
                     "gradient is active transport and has to be paid for.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-h03",
        "band": "harder",
        "text": "A grower keeps greenhouse lights on twenty-four hours a day. "
                "A student says those plants never need to respire, because "
                "they never run out of light. Where does that go wrong?",
        "options": [
            {"text": "It is right about the leaves but wrong about the roots, "
                     "which are in the dark and so have to respire instead.",
             "correct": False,
             "why": "The roots do have to respire — but so does every cell in "
                    "the leaves, in full light, at the same moment as they "
                    "photosynthesise. Photosynthesis is an extra process, not "
                    "a replacement for respiration."},
            {"text": "Photosynthesis only builds the glucose; nothing but "
                     "respiration can release the energy a cell actually "
                     "spends.",
             "correct": True},
            {"text": "It is right — a plant in constant light takes its energy "
                     "straight from the light and has no need of glucose.",
             "correct": False,
             "why": "Light is not energy a cell can spend. It is used to build "
                    "glucose, and the glucose then has to be respired before "
                    "the cell can pay for growth, repair or active transport."},
            {"text": "It goes wrong only at night, and there is no night in "
                     "this greenhouse, so here the student is right.",
             "correct": False,
             "why": "Respiration is not a night shift. It runs continuously, "
                    "in every living cell, whatever the light is doing — a "
                    "cell that stops respiring is a dead one."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-h04",
        "band": "harder",
        "text": "A bird's flight muscle cell holds far more mitochondria than "
                "the leg muscle cell of a lizard of the same size. Which "
                "explanation fits this lesson best?",
        "options": [
            {"text": "The lizard's cells do not respire; a reptile takes its "
                     "energy from the warmth of the sun instead.",
             "correct": False,
             "why": "Every living cell respires, reptiles included — a lizard "
                    "basking on a rock is releasing energy from glucose in "
                    "every cell it has. What the sun saves it is the cost of "
                    "heating itself, not the respiring."},
            {"text": "Mitochondria are an oxygen store, and a flying bird "
                     "needs a bigger one than a lizard on a rock.",
             "correct": False,
             "why": "Mitochondria store nothing. No animal has an oxygen store "
                    "worth the name, which is why the supply cannot be "
                    "interrupted for more than a few minutes in a bird or a "
                    "lizard."},
            {"text": "A bird powers flight and holds its body above air "
                     "temperature; a lizard does neither, so its bill is "
                     "smaller.",
             "correct": True},
            {"text": "The bird builds them only while it is flying and loses "
                     "them again once it lands and stops needing them.",
             "correct": False,
             "why": "A perched bird is still respiring, and still paying to "
                    "keep itself warm — the bill never falls to nothing. This "
                    "is the you-respire-when-you-exercise idea, applied to a "
                    "bird."},
        ],
        "figure": None,
    },
]
