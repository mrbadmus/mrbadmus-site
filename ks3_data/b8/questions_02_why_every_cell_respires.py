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
                     "living cell; breathing only supplies the oxygen for it.",
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
             "why": "Nothing in the body sets oxygen aside in reserve — "
                    "there is only what the blood is carrying at that "
                    "moment, a few minutes' worth. That is exactly why a "
                    "heart cut off from oxygen is permanently damaged "
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
             "why": "No cell sets oxygen aside — the only supply is what the "
                    "blood is carrying, which is why four minutes without "
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
             "why": "There is no oxygen store anywhere in you — only what the "
                    "blood is carrying at that moment, which is why brain "
                    "cells begin to die within about four minutes without "
                    "it."},
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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b8-02-e05",
        "band": "easier",
        "text": "The energy from respiration pays for four jobs in a cell. "
                "Which of them is the only one you can see from outside?",
        "options": [
            {"text": "Building large molecules out of small ones, as in "
                     "growth.",
             "correct": False,
             "why": "Growth and repair are this job, and they are invisible "
                    "while they happen. You see the result weeks later, not "
                    "the work itself."},
            {"text": "Active transport of substances into the cell.",
             "correct": False,
             "why": "Nothing about active transport can be watched. It is "
                    "individual particles being moved across a membrane "
                    "against the gradient."},
            {"text": "Movement, such as a muscle contracting or a cell "
                     "crawling.",
             "correct": True},
            {"text": "Holding the body warmer than its surroundings.",
             "correct": False,
             "why": "You can feel warmth, but you cannot see it — and a "
                    "reptile pays no such bill at all while its cells still "
                    "pay the other three."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-e06",
        "band": "easier",
        "text": "Keeping the body warmer than its surroundings is one of the "
                "jobs respiration pays for. Which animals pay that bill?",
        "options": [
            {"text": "Mammals and birds, which hold a set body temperature.",
             "correct": True},
            {"text": "All animals, because every animal is warm to the touch.",
             "correct": False,
             "why": "A lizard is the temperature of the rock it is lying on. "
                    "Only mammals and birds hold themselves above their "
                    "surroundings."},
            {"text": "Only animals that live in cold parts of the world.",
             "correct": False,
             "why": "A mammal in a hot country pays it too. The bill is for "
                    "holding a set temperature, not for resisting cold "
                    "weather."},
            {"text": "Every living organism, plants and bacteria included.",
             "correct": False,
             "why": "A plant is whatever temperature the air around it is. It "
                    "respires continuously, but not for this."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-e07",
        "band": "easier",
        "text": "What does active transport mean?",
        "options": [
            {"text": "Moving a substance from where there is more of it to "
                     "where there is less.",
             "correct": False,
             "why": "That is diffusion, and it happens on its own with no "
                    "energy supply at all. Active transport goes the other "
                    "way."},
            {"text": "Moving a substance from where there is less of it to "
                     "where there is more.",
             "correct": True},
            {"text": "Moving a substance quickly, because the cell is working "
                     "hard at the time.",
             "correct": False,
             "why": "Speed is not what the word means. It names the "
                    "direction — against the gradient — and that is why it "
                    "has to be paid for."},
            {"text": "Moving water into a cell, which takes energy from "
                     "respiration.",
             "correct": False,
             "why": "Water moves in on its own, down its own gradient, and "
                    "costs nothing. Active transport is about substances "
                    "being pulled the wrong way."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-e08",
        "band": "easier",
        "text": "Roughly how long can brain cells last without oxygen before "
                "they begin to die?",
        "options": [
            {"text": "About four seconds.", "correct": False,
             "why": "Far too short — you can hold your breath for much longer "
                    "than that. The limit is minutes, which is still short "
                    "enough to be dangerous."},
            {"text": "About four hours.", "correct": False,
             "why": "Far too long. There is no store of oxygen to live on, so "
                    "the deadline is measured in minutes."},
            {"text": "About four minutes.", "correct": True},
            {"text": "About four days.", "correct": False,
             "why": "Nothing in the body could last that long. Cells depend "
                    "on a continuous supply, and brain cells fail fastest of "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-e09",
        "band": "easier",
        "text": "A root hair cell spends about three quarters of its energy "
                "on one job. Which job is it?",
        "options": [
            {"text": "Growing the hair itself further out into the soil.",
             "correct": False,
             "why": "That is on its list, but it is a much smaller share. The "
                    "big bill is pulling mineral ions in against the "
                    "gradient."},
            {"text": "Active transport of mineral ions in from the soil.",
             "correct": True},
            {"text": "Taking in the water it draws from the soil around it.",
             "correct": False,
             "why": "Water moves in on its own and costs nothing, which is "
                    "why a plant short of energy goes short of minerals long "
                    "before it goes short of water."},
            {"text": "Making food, since it is a cell belonging to a plant.",
             "correct": False,
             "why": "A root hair cell is underground and has no chloroplasts. "
                    "Its sugar arrives from the leaves; it makes none "
                    "itself."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-e10",
        "band": "easier",
        "text": "How much oxygen does your body hold in store, ready for an "
                "emergency?",
        "options": [
            {"text": "None — only what the blood is carrying now.",
             "correct": True},
            {"text": "Enough for a few hours, held in a reserve inside the "
                     "muscles.",
             "correct": False,
             "why": "There is no such store. That is precisely why a few "
                    "minutes without a supply does permanent damage."},
            {"text": "Enough for a few minutes, held inside the lungs.",
             "correct": False,
             "why": "The lungs hold one breath, not a reserve. The air in "
                    "them is exchanged constantly and nothing is set aside."},
            {"text": "Enough for a whole day, held inside the liver.",
             "correct": False,
             "why": "The liver stores glucose, not oxygen. A store of fuel is "
                    "possible; a store of oxygen is not."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-e11",
        "band": "easier",
        "text": "Growth and repair mean joining small molecules into large "
                "ones. Which job that respiration pays for is that?",
        "options": [
            {"text": "Movement.", "correct": False,
             "why": "Movement is a muscle contracting, a cell crawling or a "
                    "tail beating. Building something is a separate bill."},
            {"text": "Active transport.", "correct": False,
             "why": "Active transport moves a substance across a membrane "
                    "against the gradient. It joins nothing together."},
            {"text": "Keeping warm.", "correct": False,
             "why": "That job holds a body above the temperature around it. "
                    "Building a protein is work of a different kind."},
            {"text": "Building large molecules.", "correct": True},
        ],
        "figure": None,
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b8-02-s05",
        "band": "standard",
        "text": "A heart muscle cell spends about 70% of its energy "
                "contracting and never gets a rest day. What happens to it "
                "within seconds of its oxygen supply being cut off?",
        "options": [
            {"text": "It carries on for a while on the oxygen it had put "
                     "aside.",
             "correct": False,
             "why": "There is nothing put aside. All it ever has is what the "
                    "blood is delivering, which is why a blocked artery does "
                    "damage so quickly."},
            {"text": "It goes on contracting, but builds fewer molecules to "
                     "save energy.",
             "correct": False,
             "why": "A cell cannot choose which bill to pay. Without oxygen "
                    "the aerobic supply fails, and contraction is the first "
                    "thing to go."},
            {"text": "Nothing changes until the next heartbeat is due to "
                     "happen.",
             "correct": False,
             "why": "The cell is spending energy continuously, not only at "
                    "the moment it contracts. The failure starts as soon as "
                    "the supply does."},
            {"text": "Contraction stops, and a few minutes of it does "
                     "permanent damage.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-s06",
        "band": "standard",
        "text": "A mouse and a lizard of the same mass are both resting, and "
                "the mouse has to eat several times as much. Which job that "
                "respiration pays for accounts for most of it?",
        "options": [
            {"text": "Keeping warm — the mouse holds itself above the "
                     "temperature of the room.",
             "correct": True},
            {"text": "Movement — a mouse moves about far more than a lizard "
                     "does.",
             "correct": False,
             "why": "Both are resting in this comparison, so movement is not "
                    "what separates them. The mouse is paying for a "
                    "temperature the lizard never holds."},
            {"text": "Active transport — a mammal's cells pull in far more "
                     "minerals.",
             "correct": False,
             "why": "Both sets of cells do active transport, at broadly "
                    "similar cost. The bill the lizard escapes is the warmth "
                    "one."},
            {"text": "Building molecules — the mouse is growing and the "
                     "lizard has stopped.",
             "correct": False,
             "why": "Both grow and both repair themselves throughout life. "
                    "What the lizard does not pay for is holding its "
                    "temperature above its surroundings."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-s07",
        "band": "standard",
        "text": "A broken bone is knitting together and new tissue is being "
                "built. Which job is being paid for, and what pays for it?",
        "options": [
            {"text": "Active transport, paid for by the food in the diet "
                     "directly.",
             "correct": False,
             "why": "Food is not energy a cell can spend until it has been "
                    "respired. And building tissue is not transport — it is "
                    "joining small molecules into large ones."},
            {"text": "Movement, paid for by respiration in the muscles "
                     "pulling the bone together.",
             "correct": False,
             "why": "The muscles are not what is building the bone. New "
                    "tissue is assembled molecule by molecule, and that is a "
                    "job in its own right."},
            {"text": "Building large molecules, paid for by respiration.",
             "correct": True},
            {"text": "Keeping warm, because a healing injury feels warm to "
                     "the touch.",
             "correct": False,
             "why": "It does feel warm, but the warmth is a side effect. What "
                    "is being paid for is the building of new material."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-s08",
        "band": "standard",
        "text": "A mushroom has no chlorophyll, makes no food of its own and "
                "does not move. Does it respire?",
        "options": [
            {"text": "No — respiration is what animals do, and a fungus is "
                     "not an animal.",
             "correct": False,
             "why": "Respiration is not an animal speciality. Every living "
                    "cell of every organism respires, fungi and bacteria "
                    "included."},
            {"text": "Yes — every living cell of every organism respires, "
                     "continuously.",
             "correct": True},
            {"text": "No — it does not move, so it has nothing to spend "
                     "energy on.",
             "correct": False,
             "why": "Movement is only one of the things respiration pays "
                    "for, and the least of them here. The mushroom is still "
                    "building molecules, "
                    "transporting substances and repairing itself."},
            {"text": "Only while it is growing; a fully grown one stops "
                     "again.",
             "correct": False,
             "why": "A cell that stopped respiring would die. Growth changes "
                    "the rate; it does not switch the reaction on and off."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-s09",
        "band": "standard",
        "text": "During an operation a patient's breathing stops, and a "
                "machine takes over within a minute. Why does that one minute "
                "matter so much?",
        "options": [
            {"text": "Because the blood stops moving the moment breathing "
                     "stops.",
             "correct": False,
             "why": "The heart goes on beating. What stops arriving is fresh "
                    "oxygen, so the blood is soon carrying none to deliver."},
            {"text": "Because the lungs collapse if they are left empty for "
                     "longer.",
             "correct": False,
             "why": "That is not the danger being managed here. The urgency "
                    "is that cells cannot pause, and brain cells fail "
                    "fastest."},
            {"text": "Because carbon dioxide builds up and dissolves the "
                     "cells.",
             "correct": False,
             "why": "Carbon dioxide does build up and that matters, but it "
                    "dissolves nothing. The immediate threat is respiration "
                    "having nothing left to run on."},
            {"text": "Because cells cannot pause, and nothing stores oxygen "
                     "for them.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-s10",
        "band": "standard",
        "text": "A cell is sitting still: not dividing, not growing and not "
                "moving. Why does it still have an energy bill to pay?",
        "options": [
            {"text": "It does not — a cell with nothing to do spends "
                     "nothing.",
             "correct": False,
             "why": "There is no such state in a living cell. Stop paying the "
                    "bill and it is dead within minutes."},
            {"text": "It pumps ions across its membrane and repairs itself.",
             "correct": True},
            {"text": "It is storing the energy it releases so that it is "
                     "ready when work arrives.",
             "correct": False,
             "why": "Energy is not stored once released — it is spent as it "
                    "is transferred. A cell cannot save any for later."},
            {"text": "It is keeping itself warm, the only bill a resting cell "
                     "has.",
             "correct": False,
             "why": "In a mammal that is one of the bills, but never the only "
                    "one — and a plant cell pays no warmth bill at all and "
                    "still cannot rest."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-s11",
        "band": "standard",
        "text": "Heart muscle, nerve, root hair, sperm and white blood cells "
                "spend their energy on quite different jobs, yet all five "
                "fail within minutes of losing oxygen. What does that show?",
        "options": [
            {"text": "That all five are really doing the same job in "
                     "disguise.",
             "correct": False,
             "why": "Their jobs are genuinely different — contracting, "
                    "signalling, pulling in minerals, swimming, engulfing "
                    "bacteria. What they share is the reaction that pays for "
                    "them."},
            {"text": "That the cells holding most mitochondria are the ones "
                     "that fail.",
             "correct": False,
             "why": "All five fail, whatever their mitochondria count. The "
                    "nerve cell is quickest because its bill is largest, not "
                    "because the others are exempt."},
            {"text": "That one reaction pays for every job, and no cell "
                     "stores oxygen.",
             "correct": True},
            {"text": "That oxygen itself is what does the work inside each of "
                     "the five.",
             "correct": False,
             "why": "Oxygen is a reactant, not a worker. It allows the "
                    "glucose to be broken down completely, and the energy "
                    "released is what pays for the job."},
        ],
        "figure": None,
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b8-02-h05",
        "band": "harder",
        "text": "A person at rest transfers about 7000 kJ of energy a day. "
                "The brain is roughly a fiftieth of body mass but takes about "
                "a fifth of that energy. How many kilojoules is that?",
        "options": [
            {"text": "140 kJ", "correct": False,
             "why": "That is a fiftieth of 7000 — the brain's share of the "
                    "MASS, not of the energy. Its share of the energy is a "
                    "fifth, and the gap between the two figures is the whole "
                    "point."},
            {"text": "1400 kJ", "correct": True},
            {"text": "3500 kJ", "correct": False,
             "why": "That is half of 7000. A fifth means dividing by five, "
                    "which gives 1400 kJ."},
            {"text": "35 000 kJ", "correct": False,
             "why": "That is 7000 × 5, multiplying where you should divide. A "
                    "fifth of a number is smaller than the number, not "
                    "larger."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-h06",
        "band": "harder",
        "text": "A root hair cell transfers about 240 kJ of energy in a day "
                "and spends 75% of it on active transport. How much energy is "
                "that?",
        "options": [
            {"text": "60 kJ", "correct": False,
             "why": "That is 25% — the share left for everything else the "
                    "cell does. Active transport takes three quarters, not "
                    "one."},
            {"text": "18 kJ", "correct": False,
             "why": "That is 7.5% of 240. The figure in the question is 75%, "
                    "which is three quarters of the total."},
            {"text": "320 kJ", "correct": False,
             "why": "That is 240 ÷ 0.75, dividing where you should multiply. "
                    "A percentage of a number can never come out larger than "
                    "the number."},
            {"text": "180 kJ", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-h07",
        "band": "harder",
        "text": "Cells lining the airways beat tiny hairs constantly, "
                "sweeping mucus up and out of the lungs. What would you "
                "expect those cells to hold plenty of, and why?",
        "options": [
            {"text": "Chloroplasts, because a cell working this hard must "
                     "make its own food.",
             "correct": False,
             "why": "Chloroplasts need light, and there is none inside an "
                    "airway. These cells are supplied with glucose by the "
                    "blood, like every other animal cell."},
            {"text": "Very little of anything, because hairs that small "
                     "cost nothing to move.",
             "correct": False,
             "why": "Small does not mean free. The beating never stops, and "
                    "every movement in biology has to be paid for."},
            {"text": "Mitochondria, because movement that never stops has to "
                     "be paid for.",
             "correct": True},
            {"text": "Stored oxygen, so the beating carries on if the supply "
                     "is interrupted.",
             "correct": False,
             "why": "No cell holds a store of oxygen. The beating stops when "
                    "the supply does, which is one reason smoke damage to the "
                    "airways is so serious."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-h08",
        "band": "harder",
        "text": "Some fish live in water so poor in oxygen that they gulp air "
                "at the surface. A student asks why they cannot simply "
                "respire less until conditions improve. What is the best "
                "answer?",
        "options": [
            {"text": "Their cells have bills that never stop, and there is "
                     "nothing to draw on meanwhile.",
             "correct": True},
            {"text": "They could, but gulping air happens to be easier than "
                     "slowing down would be.",
             "correct": False,
             "why": "There is no slowing-down option to choose. Respiration "
                    "can run more slowly, but never at nothing, and the bills "
                    "go on arriving."},
            {"text": "Respiration is under their control, so they save it for "
                     "when they swim.",
             "correct": False,
             "why": "This is the you-respire-when-you-exercise idea, wearing "
                    "fins. A resting fish is still pumping ions, building "
                    "molecules and repairing itself."},
            {"text": "They keep oxygen in the swim bladder and live off it "
                     "until the water improves.",
             "correct": False,
             "why": "The swim bladder controls buoyancy; it supplies no cell "
                    "with anything. No animal holds a store of oxygen worth "
                    "the name."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-h09",
        "band": "harder",
        "text": "A donated kidney is packed in ice for the journey to the "
                "hospital. Explain, using respiration, why cooling it helps "
                "it survive with no blood supply.",
        "options": [
            {"text": "Cooling stops respiration completely, so the cells need "
                     "nothing at all.",
             "correct": False,
             "why": "Cells whose respiration stopped would be dead on "
                    "arrival, which is the opposite of what is wanted. "
                    "Cooling slows the reaction; it does not switch it off."},
            {"text": "Cooling lets the cells store oxygen until the blood "
                     "supply is restored.",
             "correct": False,
             "why": "Cells hold no store, however cold they are. What cooling "
                    "changes is how fast they use what little is left."},
            {"text": "Cooling slows respiration, so demand falls and the "
                     "oxygen left lasts longer.",
             "correct": True},
            {"text": "Cooling removes the need for energy, since energy is "
                     "only needed for warmth.",
             "correct": False,
             "why": "Warmth is only one of the things respiration pays for, "
                    "and a kidney cell's other bills do not stop. Cooling "
                    "lowers the rate rather than removing the need."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-h10",
        "band": "harder",
        "text": "Some deep-sea animals live where food is very scarce. They "
                "move slowly and their bodies stay at the temperature of the "
                "water. How does that help them survive on so little food?",
        "options": [
            {"text": "They have stopped respiring altogether, which is how "
                     "they manage on so little food.",
             "correct": False,
             "why": "No cell can stop. What is small here is the rate, and it "
                    "is small because two of the four bills come to almost "
                    "nothing."},
            {"text": "Warmth and movement cost them almost nothing, so the "
                     "bill is tiny.",
             "correct": True},
            {"text": "They respire the water around them, which costs them "
                     "nothing at all.",
             "correct": False,
             "why": "Water is not a fuel — there is no store of energy in it "
                    "to release. Food is scarce down there, which is exactly "
                    "why a low bill matters."},
            {"text": "They make their own food in the dark, so they need none "
                     "from outside.",
             "correct": False,
             "why": "Making food needs light, and there is none at that "
                    "depth. These animals eat what drifts down, and survive "
                    "on very little of it."},
        ],
        "figure": None,
    },
    {
        "id": "b8-02-h11",
        "band": "harder",
        "text": "A student argues that because a plant cell makes its own "
                "glucose, it needs mitochondria less than an animal cell "
                "does. Where does that argument break down?",
        "options": [
            {"text": "Plant cells have no mitochondria at all, so there is "
                     "nothing to compare.",
             "correct": False,
             "why": "Every living plant cell has them, and a root hair cell "
                    "has more than most, because active transport is "
                    "expensive."},
            {"text": "It is right — a plant cell takes its energy from light "
                     "directly.",
             "correct": False,
             "why": "Light is not energy a cell can spend. It is used to "
                    "build glucose, and the glucose has to be respired before "
                    "anything can be paid for."},
            {"text": "It is right for leaf cells, and wrong only for the "
                     "cells in the roots.",
             "correct": False,
             "why": "A leaf cell respires too, at the same moment as it "
                    "photosynthesises. Making the fuel is not the same as "
                    "releasing energy from it."},
            {"text": "Making glucose is not releasing energy; every plant "
                     "cell has to respire it.",
             "correct": True},
        ],
        "figure": None,
    },
]

_MRB338_NEW_QUESTIONS = [
    {
        "id": 'b8-02-e12',
        "band": 'easier',
        "text": 'Which sentence correctly describes what respiration means in science?',
        "options": [
            {"text": 'A chemical reaction inside cells that releases energy from glucose.', "correct": True},
            {"text": 'Breathing air in and out of the lungs.', "correct": False,
             "why": 'That is breathing. Respiration is the chemical reaction that releases energy, and breathing is just the muscular job that supplies it with oxygen.'},
            {"text": 'The exchange of gases between blood and the air in the lungs.', "correct": False,
             "why": 'That is gas exchange, which happens in the lungs. Respiration itself happens inside cells, not in the lungs.'},
            {"text": 'The process of taking food into the body and breaking it into small molecules.', "correct": False,
             "why": 'That is digestion. Digestion supplies the glucose that cells then respire.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e13',
        "band": 'easier',
        "text": 'Which statement about respiration in living cells is correct?',
        "options": [
            {"text": 'Only cells that are moving or growing need to respire.', "correct": False,
             "why": 'Even a cell doing neither still spends energy on ion pumping and repair, so it still respires.'},
            {"text": 'Every living cell in every living organism respires continuously.', "correct": True},
            {"text": 'Cells respire only when the organism is awake or active.', "correct": False,
             "why": 'Respiration continues at the lowest rate even during sleep or rest — it never switches off.'},
            {"text": 'Only animal cells respire; plant cells make their own energy by photosynthesis instead.', "correct": False,
             "why": 'Photosynthesis makes glucose; respiring it for energy is a separate reaction every plant cell still carries out.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e14',
        "band": 'easier',
        "text": 'Which of these is an example of the ‘movement’ job that respiration pays for?',
        "options": [
            {"text": 'A root hair cell pulling in mineral ions.', "correct": False,
             "why": 'That is active transport, a different job from movement.'},
            {"text": 'A cell joining amino acids together to build a protein.', "correct": False,
             "why": 'That is building large molecules, a different job from movement.'},
            {"text": 'A white blood cell crawling towards a bacterium.', "correct": True},
            {"text": 'A mammal keeping its body warmer than the air around it.', "correct": False,
             "why": 'That is keeping warm, a different job from movement.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e15',
        "band": 'easier',
        "text": 'The lining of your small intestine pulls glucose in from the gut even when the lining cells already hold more glucose than the gut does. Which of the four jobs is that?',
        "options": [
            {"text": 'Movement.', "correct": False,
             "why": 'Nothing here is contracting, crawling or beating a tail. A lining cell carrying a glucose molecule across its membrane is a different bill.'},
            {"text": 'Keeping warm.', "correct": False,
             "why": 'That job holds a body above the temperature around it. This cell is shifting a substance, not producing heat.'},
            {"text": 'Active transport.', "correct": True},
            {"text": 'Building new proteins.', "correct": False,
             "why": 'The glucose crosses the membrane unchanged. Nothing is being joined onto it to make a larger molecule.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e16',
        "band": 'easier',
        "text": 'Which of these describes active transport?',
        "options": [
            {"text": 'Moving a substance from where there is less of it to where there is more, using energy.', "correct": True},
            {"text": 'Moving a substance from where there is more of it to where there is less, using no energy.', "correct": False,
             "why": 'That is diffusion, moving the opposite way and needing no energy supply.'},
            {"text": 'Building a large molecule out of many small ones.', "correct": False,
             "why": 'That is the ‘building large molecules’ job, not active transport.'},
            {"text": 'Holding the body at a temperature above the surroundings.', "correct": False,
             "why": 'That is ‘keeping warm’, not active transport.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e17',
        "band": 'easier',
        "text": 'Which group of animals pays the ‘keeping warm’ energy bill?',
        "options": [
            {"text": 'Reptiles and fish.', "correct": False,
             "why": 'These do not hold a set body temperature above their surroundings, so they do not pay this bill.'},
            {"text": 'Mammals and birds.', "correct": True},
            {"text": 'Only animals that live in cold climates.', "correct": False,
             "why": 'Mammals and birds pay this bill wherever they live, not only in the cold.'},
            {"text": 'Every animal, because every animal is warm to the touch.', "correct": False,
             "why": 'An animal can feel warm simply because the air around it is warm; only mammals and birds generate their own steady body heat this way.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e18',
        "band": 'easier',
        "text": 'A heart muscle cell contracts about once a second, non-stop, for a lifetime. What does it spend most of its respired energy on?',
        "options": [
            {"text": 'Building new proteins.', "correct": False,
             "why": 'Repair is a real cost for this cell, but a much smaller share than contracting.'},
            {"text": 'Pumping ions across its membrane.', "correct": False,
             "why": "That is the nerve cell's biggest single cost, not the heart muscle cell's."},
            {"text": 'Contracting.', "correct": True},
            {"text": 'Active transport of minerals.', "correct": False,
             "why": "That is the root hair cell's main job, not a muscle cell's."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e19',
        "band": 'easier',
        "text": 'What is the single biggest energy cost for a nerve cell that is firing signals?',
        "options": [
            {"text": 'Contracting hard, over and over, in the way a muscle cell does.', "correct": False,
             "why": 'A nerve cell carries signals; it does not contract.'},
            {"text": 'Making the chemicals it uses to signal the next cell.', "correct": False,
             "why": 'That is a real cost, but a much smaller one than resetting the ion balance after each signal.'},
            {"text": 'Active transport of minerals from the soil.', "correct": False,
             "why": "That is a root hair cell's job; a nerve cell is not taking anything from soil."},
            {"text": 'Pumping ions back across its membrane after each signal.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e20',
        "band": 'easier',
        "text": 'Why does a root hair cell need so many mitochondria?',
        "options": [
            {"text": 'Pulling mineral ions in against the concentration gradient uses a great deal of energy.', "correct": True},
            {"text": 'It uses them to store the water it absorbs, keeping a reserve ready for a dry spell.', "correct": False,
             "why": 'Mitochondria are not water stores; they are where aerobic respiration happens.'},
            {"text": 'It photosynthesises in the dark soil, and that needs mitochondria.', "correct": False,
             "why": 'Root hair cells have no chloroplasts and no light reaches them, so they cannot photosynthesise.'},
            {"text": 'It needs the extra oxygen mitochondria hold in reserve.', "correct": False,
             "why": 'Mitochondria are not an oxygen store; they are where oxygen is used up in respiration.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e21',
        "band": 'easier',
        "text": 'What does a sperm cell spend almost all of its respired energy on?',
        "options": [
            {"text": 'Building new proteins as it grows.', "correct": False,
             "why": 'A sperm cell is not growing; almost everything not needed for the swim has been stripped out of it.'},
            {"text": 'Beating its tail to swim.', "correct": True},
            {"text": 'Keeping itself warmer than its surroundings.', "correct": False,
             "why": 'Keeping warm is paid for by mammals and birds as whole organisms, not by a single sperm cell.'},
            {"text": 'Active transport of substances into itself.', "correct": False,
             "why": "A sperm cell's job is swimming, not moving substances against a gradient."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e22',
        "band": 'easier',
        "text": 'A white blood cell that has just met bacteria doubles the number of mitochondria it contains within a few hours. What does that tell you about the work it is about to do?',
        "options": [
            {"text": 'Mitochondria are where a cell stores oxygen for later, ready to be released the moment it is needed.', "correct": False,
             "why": 'Mitochondria are not an oxygen store; they are where oxygen is used up during respiration.'},
            {"text": 'The extra mitochondria attack the bacteria directly, breaking them apart piece by piece.', "correct": False,
             "why": 'Mitochondria release energy; they do not attack anything themselves.'},
            {"text": 'It is about to work much harder, chasing and engulfing bacteria, and that costs far more energy.', "correct": True},
            {"text": 'It is preparing to divide, and dividing cells always need more mitochondria.', "correct": False,
             "why": 'The extra mitochondria here pay for crawling and engulfing, not for cell division.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e23',
        "band": 'easier',
        "text": 'Active transport always needs a supply of energy. Why?',
        "options": [
            {"text": 'Because it only happens inside mitochondria, the one part of the cell every process depends on.', "correct": False,
             "why": 'Active transport happens across cell membranes; it is not confined to mitochondria.'},
            {"text": 'Because it always involves building a large molecule.', "correct": False,
             "why": 'Building large molecules is a separate job from active transport, not the reason it costs energy.'},
            {"text": 'Because it only happens in plant cells.', "correct": False,
             "why": 'Active transport happens in plant and animal cells alike — the gut lining is one animal example.'},
            {"text": 'Because it moves a substance against its concentration gradient, from low to high concentration.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e24',
        "band": 'easier',
        "text": 'What is a concentration gradient?',
        "options": [
            {"text": 'The difference between a place with more of a substance and a place with less of it.', "correct": True},
            {"text": 'The rate at which a substance is steadily used up by a respiring cell over time.', "correct": False,
             "why": 'That describes a rate of use, not a difference in concentration between two places.'},
            {"text": "The energy released when a substance is respired inside a cell's mitochondria.", "correct": False,
             "why": 'That describes energy released by respiration, not a difference in concentration.'},
            {"text": 'The temperature difference between the inside and the outside of a working cell.', "correct": False,
             "why": 'A concentration gradient is about the amount of a substance, not about temperature.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e25',
        "band": 'easier',
        "text": 'Which part of a cell is the site of aerobic respiration?',
        "options": [
            {"text": 'The nucleus.', "correct": False,
             "why": "The nucleus stores the cell's genetic information; aerobic respiration happens in the mitochondria."},
            {"text": 'The mitochondria.', "correct": True},
            {"text": 'The cell membrane.', "correct": False,
             "why": 'The cell membrane controls what enters and leaves; respiration itself happens in the mitochondria.'},
            {"text": 'The cytoplasm alone, with no particular part involved.', "correct": False,
             "why": 'Aerobic respiration happens in a specific part of the cell, the mitochondria, not spread evenly through the cytoplasm.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e26',
        "band": 'easier',
        "text": 'A cell transfers 150 kJ of energy in a day and spends 60% of it on building large molecules. How much energy is that?',
        "options": [
            {"text": '60 kJ', "correct": False,
             "why": 'This reads the percentage figure itself as the answer instead of finding 60% of 150.'},
            {"text": '210 kJ', "correct": False,
             "why": 'This adds 60 to 150 instead of finding 60% of it.'},
            {"text": '45 kJ', "correct": False,
             "why": 'This finds 30% of 150, halving the share the question gives.'},
            {"text": '90 kJ', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e27',
        "band": 'easier',
        "text": "A mouse and a lizard of the same mass are resting at the same air temperature. Which of the mouse's extra energy jobs explains why it uses far more energy than the lizard?",
        "options": [
            {"text": 'Keeping warm — the mouse holds its body above the surrounding temperature; the lizard does not.', "correct": True},
            {"text": 'Movement — a resting mouse still moves about far more than a resting lizard ever does.', "correct": False,
             "why": 'Both animals are resting and moving very little; movement is not what separates them here.'},
            {"text": "Active transport — a mouse's cells move far more substances than a lizard's.", "correct": False,
             "why": 'Nothing in the situation compares active transport between the two animals; the stated difference is body temperature.'},
            {"text": 'Building large molecules — the mouse is growing and the lizard is not.', "correct": False,
             "why": 'Nothing says the mouse is growing; both animals are simply resting.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e28',
        "band": 'easier',
        "text": 'A cell is not dividing, not growing and not moving. Is it still respiring?',
        "options": [
            {"text": 'No — a cell with genuinely nothing to do spends no energy on anything at all.', "correct": False,
             "why": 'Even a cell doing none of those three things still pays running costs, such as pumping ions and repairing itself.'},
            {"text": 'Yes — it is still pumping ions and repairing itself, which both cost energy.', "correct": True},
            {"text": 'No — only cells that are actively growing respire.', "correct": False,
             "why": 'Every living cell respires continuously, whether or not it is growing at that moment.'},
            {"text": 'Only if it is about to divide very soon.', "correct": False,
             "why": 'Respiration does not switch on only in preparation for division; it runs continuously in every living cell.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e29',
        "band": 'easier',
        "text": 'Does a single bacterium living in pond water respire?',
        "options": [
            {"text": 'No — respiration needs a whole organism made of many cells.', "correct": False,
             "why": 'A single-celled organism is a complete living cell on its own, and it respires just as any living cell does.'},
            {"text": 'Only if it is moving through the water.', "correct": False,
             "why": 'Respiration pays for far more than movement alone, and it continues even when the cell is not moving.'},
            {"text": 'No — bacteria get their energy directly from the water around them.', "correct": False,
             "why": 'Water itself supplies no energy; the bacterium still has to respire glucose or another fuel to release energy.'},
            {"text": 'Yes — it is a living cell, and every living cell respires.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-e30',
        "band": 'easier',
        "text": 'A leaf cell is photosynthesising in bright sunlight. Is it also respiring at the same time?',
        "options": [
            {"text": 'Yes — every living plant cell respires continuously, in daylight as well as in the dark.', "correct": True},
            {"text": 'No — photosynthesis switches respiration off completely while there is enough light to work with.', "correct": False,
             "why": 'The two reactions run independently; a plant cell does not switch respiration off just because it is also photosynthesising.'},
            {"text": 'Only at night, once photosynthesis has stopped.', "correct": False,
             "why": 'Respiration in a plant cell never stops, in daylight or darkness.'},
            {"text": 'No — a leaf cell gets its energy directly from sunlight instead of respiring.', "correct": False,
             "why": 'Sunlight is used to make glucose in photosynthesis; releasing energy from that glucose still requires the separate reaction of respiration.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s12',
        "band": 'standard',
        "text": 'A student swims 50 lengths, holding their breath underwater on every length. Are their muscle cells respiring during that swim?',
        "options": [
            {"text": 'Yes — respiration is a chemical reaction inside the cells, and it keeps running on the oxygen and glucose already in the blood while breathing is paused.', "correct": True},
            {"text": 'No — respiration needs breathing happening at the same instant.', "correct": False,
             "why": 'Breathing supplies new oxygen to the blood; the oxygen already there keeps respiration running for a short pause.'},
            {"text": 'No — swimming uses stored energy that bypasses respiration entirely.', "correct": False,
             "why": 'Every muscle contraction, in swimming or anywhere else, is paid for by respiration; there is no separate store that bypasses it.'},
            {"text": 'Only the lungs keep respiring without help from the rest of the body.', "correct": False,
             "why": 'Respiration happens inside every cell of the body, not specially in the lungs.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s13',
        "band": 'standard',
        "text": "A gardener says her tomato plant ‘switches off’ overnight because it stops making food in the dark. Which of her plant's cells are still respiring overnight?",
        "options": [
            {"text": 'Only the root cells respire overnight, because the stem and leaf cells store enough energy during the day to coast through until morning.', "correct": False,
             "why": 'Every living cell in the plant respires continuously, not only the roots — none of them ‘coasts’ on a stored supply overnight.'},
            {"text": 'Every living cell in the plant respires continuously — roots, stem and leaves alike, whatever time of day it is.', "correct": True},
            {"text": 'None of the plant respires at night, since respiration only runs alongside photosynthesis.', "correct": False,
             "why": 'Respiration in a plant runs continuously, day and night, whether or not photosynthesis is also happening.'},
            {"text": 'Only the cells nearest the soil keep respiring once it gets dark.', "correct": False,
             "why": 'Light does not switch respiration on or off in any cell; every living plant cell respires all the time, wherever it sits.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s14',
        "band": 'standard',
        "text": 'A sperm cell swimming and a white blood cell crawling both spend most of their energy on the same job. Which job is that, and what is different between the two cells?',
        "options": [
            {"text": 'Active transport — both cells are pulling in far more dissolved minerals than a typical resting cell would ever need.', "correct": False,
             "why": 'Neither cell is described as pulling in minerals against a gradient; both are described moving themselves through a fluid.'},
            {"text": 'Keeping warm — both cells individually hold their own temperature above the fluid around them.', "correct": False,
             "why": 'Keeping warm is paid for by mammals and birds as whole organisms, not by individual cells holding their own temperature.'},
            {"text": 'Movement — but the white blood cell also spends real energy on antibodies and enzymes.', "correct": True},
            {"text": 'Building large molecules — both cells are simply growing larger.', "correct": False,
             "why": 'Neither cell is described as growing; both are described using energy to move.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s15',
        "band": 'standard',
        "text": 'A broken bone is knitting together, with new bone tissue being laid down. Which of the four energy jobs is paying for that, and why?',
        "options": [
            {"text": 'Movement — cells specialised for repair crawl through the bone to the site of the break, using energy the same way a white blood cell does.', "correct": False,
             "why": 'The process described is new tissue being laid down, which is molecules being joined together, not a cell moving from place to place.'},
            {"text": 'Active transport — minerals are pumped into the healing bone against their concentration gradient the whole time it heals.', "correct": False,
             "why": 'The process described is building the tissue itself, not moving a substance against a concentration gradient.'},
            {"text": 'Keeping warm — the injury feels noticeably warm because healing raises the local temperature for weeks.', "correct": False,
             "why": 'A healing injury can feel warm because of increased blood flow, but that is not what is paying for the new tissue being built.'},
            {"text": 'Building large molecules.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s16',
        "band": 'standard',
        "text": 'Cells lining the small intestine pull glucose out of the gut and into the blood, even once there is already more glucose in the blood than in the gut. What must be happening, and why does the cell need many mitochondria?',
        "options": [
            {"text": 'Active transport — moving glucose against its own concentration gradient needs a continuous supply of energy from respiration.', "correct": True},
            {"text": 'Diffusion — glucose simply moves down its own gradient into the blood.', "correct": False,
             "why": 'Once there is already more glucose in the blood than in the gut, diffusion would move it the wrong way; getting it in anyway needs active transport.'},
            {"text": 'Osmosis — water dragging the glucose along with it into the blood.', "correct": False,
             "why": 'Osmosis moves water, not glucose, and would not explain glucose moving against its own gradient.'},
            {"text": 'Filtration — the gut wall lets glucose through under pressure alone.', "correct": False,
             "why": 'Filtration relies on a pressure difference, not on a cell actively spending energy to move a substance against a gradient.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s17',
        "band": 'standard',
        "text": 'A pet snake and a pet hamster are kept in rooms at the same, fairly cool, temperature. The hamster eats far more food for its size than the snake. Which of the four energy jobs best explains this difference?',
        "options": [
            {"text": 'Movement — hamsters are constantly restless in their cage, far more active than a snake ever is at any temperature.', "correct": False,
             "why": 'Even a hamster sitting still all day uses far more energy than a snake of the same mass at the same temperature, so movement is not the main explanation.'},
            {"text": 'Keeping warm — the hamster holds its body above room temperature; the snake does not.', "correct": True},
            {"text": 'Building large molecules — hamsters never stop growing.', "correct": False,
             "why": 'An adult hamster that has stopped growing still needs far more food than a snake of the same mass, so growth is not the main explanation.'},
            {"text": 'Active transport — hamster cells move more substances.', "correct": False,
             "why": 'Nothing here compares active transport between the two animals; the situation is about food needed simply to stay warm.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s18',
        "band": 'standard',
        "text": "A donor heart is packed on ice for the journey to hospital, which slows its cells' respiration right down. Why does this matter for the heart muscle cells specifically?",
        "options": [
            {"text": 'Cooling stops the heart cells needing any energy at all, however long the journey to hospital takes.', "correct": False,
             "why": 'Cooling slows respiration, but it does not stop it completely — the cells still need some energy, just less of it.'},
            {"text": 'Cooling lets the cells store extra oxygen in reserve until they are warmed up again later.', "correct": False,
             "why": 'Cells have no meaningful store of oxygen at any temperature; cooling works by lowering demand, not by creating a reserve.'},
            {"text": 'Heart muscle cells cannot be replaced, so slowing their energy demand keeps them alive.', "correct": True},
            {"text": 'Cooling removes the need for glucose entirely.', "correct": False,
             "why": "Ice supplies no energy of any kind; it only slows the rate at which respiration uses up the cells' limited reserves."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s19',
        "band": 'standard',
        "text": "A local anaesthetic blocks a nerve cell's ability to fire signals, but does not damage the cell. What happens to that nerve cell's energy demand while the anaesthetic is working, and why?",
        "options": [
            {"text": 'It rises sharply, because the nerve cell has to work much harder overall to overcome the effect of the anaesthetic on its membrane.', "correct": False,
             "why": "Blocking signals removes the nerve cell's biggest single cost rather than adding to it, so demand falls rather than rises."},
            {"text": "It stays exactly the same, because a nerve cell's energy demand has nothing at all to do with signalling in the first place.", "correct": False,
             "why": 'Signalling — resetting the ion balance afterwards — is the single biggest energy cost for a firing nerve cell, so blocking it changes demand a great deal.'},
            {"text": 'It falls to zero, because a nerve cell that cannot fire no longer respires in any way whatsoever.', "correct": False,
             "why": 'The cell is still alive and still has running costs such as repair, so its respiration continues at a reduced rate rather than stopping completely.'},
            {"text": 'It falls sharply, because the ion-pumping bill stops the moment no signals are fired.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s20',
        "band": 'standard',
        "text": 'A student says a plant could save energy by absorbing its minerals by diffusion instead of active transport, the same way water enters the root. Explain why this would not work.',
        "options": [
            {"text": 'Minerals are usually more concentrated inside the root hair cell than in the soil, so only active transport can move them in against that gradient.', "correct": True},
            {"text": 'Diffusion is simply too slow a process to rely on.', "correct": False,
             "why": 'Speed is not the reason active transport is needed here — the direction the minerals need to move, against their own gradient, is.'},
            {"text": 'Root hair cells have no membrane for diffusion to cross.', "correct": False,
             "why": 'Root hair cells, like all cells, have a cell membrane; the issue is the direction minerals need to move.'},
            {"text": 'Minerals cannot diffuse through water at all.', "correct": False,
             "why": 'Minerals dissolved in soil water can and do diffuse; the problem is that diffusion alone would move them the wrong way for the plant.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s21',
        "band": 'standard',
        "text": 'A sperm cell that has been swimming for some time suddenly runs out of oxygen. What happens to it, and why can it not simply wait until oxygen returns?',
        "options": [
            {"text": 'It switches over to using its stored glucose instead, and carries on swimming exactly as before without any real interruption.', "correct": False,
             "why": "Even with a store of glucose, releasing energy from it still needs oxygen for the sperm cell's normal route; without oxygen the swim cannot continue as before."},
            {"text": 'It stops swimming almost at once and cannot start again, having no store to fall back on.', "correct": True},
            {"text": 'It slows down only gradually, over several hours, before finally coming to a stop.', "correct": False,
             "why": 'With essentially nothing to fall back on, the stop happens quickly rather than over hours.'},
            {"text": 'Nothing changes at all, because a sperm cell carries its own oxygen supply inside its head.', "correct": False,
             "why": 'No cell carries an oxygen store of its own; a sperm cell depends entirely on the oxygen reaching it from outside.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s22',
        "band": 'standard',
        "text": "During a bad infection, a person's white blood cells are chasing and engulfing far more bacteria than usual, and are also dividing rapidly to increase their numbers. Which of these correctly ranks their extra energy demands, from largest to smallest?",
        "options": [
            {"text": 'Dividing takes by far the largest share, ahead of crawling and engulfing, with antibodies and enzymes using the least of all.', "correct": False,
             "why": 'Dividing is described as the smallest of the three shares, not the largest.'},
            {"text": 'Making antibodies and enzymes comes first, ahead of dividing, with crawling and engulfing using the smallest share.', "correct": False,
             "why": 'Crawling and engulfing is described as the largest single share, not the smallest.'},
            {"text": 'Crawling and engulfing, then making antibodies and enzymes, then dividing.', "correct": True},
            {"text": 'All three jobs take an exactly equal share of the extra energy.', "correct": False,
             "why": 'The three jobs are described as taking different-sized shares, with crawling and engulfing the largest.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s23',
        "band": 'standard',
        "text": 'A student says active transport and diffusion are really the same thing, just moving in opposite directions. Explain what is actually different between them, besides direction.',
        "options": [
            {"text": 'Active transport happens only inside plant cells, while diffusion is something that only ever happens inside animal cells.', "correct": False,
             "why": 'Both processes happen in plant and animal cells; the real difference is that one needs energy and the other does not.'},
            {"text": 'Active transport always moves water, while diffusion only ever moves substances that are dissolved in it.', "correct": False,
             "why": 'Both processes can move dissolved substances; water itself usually moves by osmosis, a special case of diffusion, not by active transport.'},
            {"text": 'Active transport is simply a faster version of diffusion in every single case it occurs in.', "correct": False,
             "why": 'The key difference the lesson draws is about energy, not about which process is faster.'},
            {"text": 'Active transport needs energy; diffusion needs none.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s24',
        "band": 'standard',
        "text": 'Two rooms are connected by an open door. Room A has a strong smell of coffee and Room B has none. Which statement about the concentration gradient of coffee particles is correct?',
        "options": [
            {"text": 'There is a concentration gradient from Room A to Room B, and the coffee particles will diffuse down it entirely on their own.', "correct": True},
            {"text": 'There is no gradient until someone actively moves the smell between the rooms.', "correct": False,
             "why": 'A concentration gradient exists simply because there is more coffee smell in one room than the other; nothing needs to move it for the gradient to exist.'},
            {"text": 'The gradient runs the other way, from Room B towards Room A.', "correct": False,
             "why": 'A gradient runs from where there is more of a substance to where there is less, which here is from Room A towards Room B.'},
            {"text": 'There is a gradient, but it needs energy supplied before it can shift at all.', "correct": False,
             "why": 'Nothing here moves against its gradient, so it needs no energy supply; the particles simply diffuse down the gradient that already exists.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s25',
        "band": 'standard',
        "text": 'A student compares a liver cell, which is very active, with a fat storage cell, which does very little. Which statement about their mitochondria is best supported by what you know about respiration?',
        "options": [
            {"text": 'Both cells should contain exactly the same number of mitochondria, since every cell in the body is the same size as every other.', "correct": False,
             "why": "Cells are not all the same size, and a cell's number of mitochondria tends to match its energy demand rather than a fixed count."},
            {"text": 'The liver cell should contain far more mitochondria, given its much larger energy demand.', "correct": True},
            {"text": 'Neither cell needs any mitochondria, since both store their own fuel.', "correct": False,
             "why": 'A store of fuel is not itself a source of usable energy; a cell still has to respire that fuel in its mitochondria to release energy from it.'},
            {"text": 'The fat storage cell needs more mitochondria to make fat.', "correct": False,
             "why": 'A cell doing very little generally has a lower energy demand and correspondingly fewer mitochondria than a very active cell.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s26',
        "band": 'standard',
        "text": "A free-diver holds their breath and swims underwater for two minutes. Explain, in terms of the body's oxygen store, why this becomes impossible to sustain for much longer.",
        "options": [
            {"text": 'The body has a fixed oxygen store lasting about two minutes, built specifically for diving, which then has to slowly refill overnight.', "correct": False,
             "why": 'The body has no such purpose-built store for diving; it simply has whatever oxygen was already in the blood when the breath was held.'},
            {"text": 'Muscles stop needing oxygen after the first minute underwater, which is why the dive can continue for so much longer.', "correct": False,
             "why": 'Muscles continue needing oxygen throughout the dive; nothing about diving removes that need.'},
            {"text": 'The body holds almost no oxygen reserve, only whatever the blood was carrying when the breath was held.', "correct": True},
            {"text": 'The lungs act as a large oxygen tank that slowly empties over many minutes.', "correct": False,
             "why": 'The lungs hold a breath of air, not a multi-minute reserve; what runs out quickly is the oxygen already in the blood.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s27',
        "band": 'standard',
        "text": 'A root hair cell transfers 320 kJ of energy in a day, and 75% of it pays for active transport of minerals. How much energy does that leave for everything else the cell does?',
        "options": [
            {"text": '240 kJ', "correct": False,
             "why": 'That is the 75% spent on active transport, not the 25% left over for everything else.'},
            {"text": '300 kJ', "correct": False,
             "why": 'That comes from subtracting 20 kJ instead of working out 75% of the total correctly.'},
            {"text": '40 kJ', "correct": False,
             "why": 'That treats the remaining share as 12.5% instead of 25% of the total.'},
            {"text": '80 kJ', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s28',
        "band": 'standard',
        "text": "A mouse and a lizard of equal mass are both moved from a warm room into a cold one. The mouse's food intake rises sharply within a day; the lizard's does not change at all. Explain this difference in terms of the energy jobs respiration pays for.",
        "options": [
            {"text": 'The mouse must spend far more energy holding its body temperature above the colder room; the lizard holds no such temperature and so pays nothing extra.', "correct": True},
            {"text": 'The mouse simply moves around more in the cold to keep itself warm.', "correct": False,
             "why": 'The difference described is specifically about keeping a body temperature above the surroundings, not about extra movement.'},
            {"text": "The lizard's cells stop respiring completely once the room turns cold.", "correct": False,
             "why": "The lizard's cells continue respiring in the cold; they simply are not paying the ‘keeping warm’ bill the mouse's cells are."},
            {"text": 'The mouse needs extra active transport in the cold to absorb nutrients faster.', "correct": False,
             "why": 'Nothing here is about absorbing nutrients faster; the change described is in the ‘keeping warm’ job specifically.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s29',
        "band": 'standard',
        "text": "A doctor says a patient's cells ‘switch off’ during a deep, dreamless sleep to save energy. Using what this lesson teaches about respiration, explain what is wrong with that claim.",
        "options": [
            {"text": 'It is correct — respiration genuinely pauses completely during deep sleep and restarts the moment the sleeper wakes up again.', "correct": False,
             "why": 'Respiration in a living cell does not pause completely at any point; it continues, even if some jobs run at a lower rate than while awake.'},
            {"text": 'No cell switches off completely; even asleep, every cell keeps pumping ions and repairing itself.', "correct": True},
            {"text": 'It is only wrong for muscle cells, which keep contracting slightly even during sleep.', "correct": False,
             "why": 'The claim is wrong for every living cell, not only muscle cells — nerve cells, for instance, keep paying their large ion-pumping bill throughout sleep too.'},
            {"text": 'It is correct for plant cells but not at all for animal cells.', "correct": False,
             "why": 'The claim about switching off respiration completely is wrong for every living cell, plant or animal.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s30',
        "band": 'standard',
        "text": 'A student argues that because a plant cell makes its own glucose by photosynthesis, it does not need to respire the way an animal cell does. Explain what is wrong with this argument.',
        "options": [
            {"text": 'It is correct — a plant cell gets its energy directly from sunlight and never actually needs to respire at all.', "correct": False,
             "why": 'Sunlight is used to make glucose during photosynthesis, but releasing usable energy from that glucose still requires respiration.'},
            {"text": 'It is only wrong for root cells, since leaf cells really can skip respiration entirely.', "correct": False,
             "why": 'Every plant cell, leaf cells included, still has to respire — photosynthesis supplies the fuel, it does not replace the need to release energy from it.'},
            {"text": 'Making glucose is not releasing energy; a plant cell still has to respire it.', "correct": True},
            {"text": 'It is correct during the day, but wrong again once night falls.', "correct": False,
             "why": 'A plant cell respires continuously, day and night, regardless of whether photosynthesis is also happening at that moment.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s31',
        "band": 'standard',
        "text": 'A student says fungi cannot respire because they have no muscles to move and nothing to keep warm. Explain what is wrong with this reasoning.',
        "options": [
            {"text": 'Fungi genuinely do not respire at all, since they have neither muscles nor a set body temperature to maintain.', "correct": False,
             "why": 'Every living cell, fungal cells included, respires continuously to pay for jobs such as building molecules and active transport.'},
            {"text": 'The reasoning is correct for fungi specifically, but would be entirely wrong if applied to bacteria instead.', "correct": False,
             "why": 'The same flaw — assuming movement and keeping warm are the only reasons to respire — applies equally to any living cell, bacteria included.'},
            {"text": 'The reasoning is only wrong because fungi actually do have muscles, just extremely small and hidden ones.', "correct": False,
             "why": 'Fungi do not have muscles at all; the flaw is assuming movement and keeping warm are the only jobs respiration pays for.'},
            {"text": 'Movement and warmth are only two of several jobs respiration pays for.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-s32',
        "band": 'standard',
        "text": 'A single-celled organism in pond water needs no blood or transport system, while a mouse of a similar total cell mass needs an extensive one. Explain why.',
        "options": [
            {"text": 'Every cell in the mouse needs its own supply of glucose and oxygen, and most cells are too far from the outside to get these by diffusion alone; the single cell can exchange directly with the water around it.', "correct": True},
            {"text": 'The single-celled organism does not respire, so it has nothing worth transporting.', "correct": False,
             "why": 'The single-celled organism does respire, just as every living cell does; what it does not need is a transport system, because it can exchange directly with its surroundings.'},
            {"text": "The mouse's cells rely on active transport for everything; the single cell uses none at all.", "correct": False,
             "why": 'Both kinds of cell can use active transport where they need to; the real difference is about distance from the surroundings.'},
            {"text": 'The single cell stores enough oxygen inside itself to avoid ever needing transport.', "correct": False,
             "why": 'No cell holds a meaningful oxygen store; the single-celled organism manages without transport because it can exchange gases directly with the water around it.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h12',
        "band": 'harder',
        "text": "A patient under general anaesthetic has their breathing fully controlled by a ventilator during a delicate operation. A trainee doctor argues that, since a machine is doing the breathing, the patient's cells are not really respiring during the operation. Evaluate this argument.",
        "options": [
            {"text": 'The argument confuses breathing with respiration itself.', "correct": True},
            {"text": 'The argument is correct, because respiration absolutely cannot continue unless the patient is breathing for themselves at that exact moment.', "correct": False,
             "why": 'Respiration inside a cell depends on the oxygen and glucose already reaching it, not on who or what is moving air in and out of the lungs.'},
            {"text": "The argument is correct, because a ventilator supplies oxygen directly to the body's cells instead of them ever needing to respire it themselves.", "correct": False,
             "why": 'A ventilator moves air in and out of the lungs; the cells themselves still have to respire the oxygen that reaches them via the blood.'},
            {"text": 'The argument is wrong only for muscle cells, which can store more than enough energy to keep working without any external system for hours.', "correct": False,
             "why": 'Muscle cells hold no significant store that lets them keep working indefinitely; the flaw in the argument is more general.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h13',
        "band": 'harder',
        "text": "A biologist finds a species of deep-sea worm living beside a hydrothermal vent, in permanent darkness with no plants or algae for hundreds of kilometres. A student argues this worm's cells cannot be respiring aerobically, since nothing there could be producing oxygen. Evaluate this reasoning.",
        "options": [
            {"text": 'Respiration always needs a local, freshly produced source of oxygen right where it is used.', "correct": False,
             "why": 'Oxygen dissolved in water does not need to be produced on the spot; it can be carried a very long way by ocean currents before a deep-sea organism uses it.'},
            {"text": 'The reasoning wrongly assumes oxygen has to be made locally.', "correct": True},
            {"text": 'Deep-sea worms actually respire anaerobically instead, using no oxygen of any kind.', "correct": False,
             "why": 'Many deep-sea animals, worms included, respire aerobically using dissolved oxygen carried from elsewhere; the flaw is in assuming local production is required.'},
            {"text": 'The reasoning is wrong, but the worm makes its own oxygen.', "correct": False,
             "why": 'The worm does not manufacture its own oxygen; it uses dissolved oxygen that was carried a long way by ocean currents.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h14',
        "band": 'harder',
        "text": "A sprinter's leg muscle cell and a marathon runner's leg muscle cell are both contracting hard. The sprinter's cell is also making far more lactic acid than the marathon runner's, relative to how hard each is working. Is ‘movement’ the only thing costing the sprinter's cell more energy than usual?",
        "options": [
            {"text": 'Yes — movement is the only job that ever changes at all when a muscle contracts noticeably harder than usual.', "correct": False,
             "why": 'Harder, faster contraction also increases the repair cost afterwards, because it causes more microscopic damage to the muscle fibres.'},
            {"text": 'No — the extra energy goes mainly on active transport of lactic acid out through the membrane.', "correct": False,
             "why": 'Lactic acid does leave the muscle, but that is not one of the four energy jobs respiration itself is paying for inside the cell.'},
            {"text": "No — the sprinter's cell also spends extra energy on repair, dealing with greater microscopic damage.", "correct": True},
            {"text": 'No — the extra energy goes mainly on keeping the whole body warmer than a gentle jog would.', "correct": False,
             "why": "Keeping warm is the job of holding the whole body above the surrounding temperature; it is not why a sprinting muscle cell's demand rises."},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h15',
        "band": 'harder',
        "text": "An athlete recovering from a broken bone gains 2 kg of new bone and muscle tissue over eight weeks of rehabilitation, while eating almost exactly the number of kilojoules a doctor calculates they need just to stay the same weight. A friend says this is impossible, since building new tissue needs extra energy on top of just staying the same weight. Evaluate the friend's claim.",
        "options": [
            {"text": 'Building large molecules costs no extra energy beyond normal maintenance.', "correct": False,
             "why": 'Building large molecules — joining small molecules together to grow new tissue — is one of the four jobs respiration has to pay for, and it does add an extra cost.'},
            {"text": 'New tissue is built entirely from food, with no respiration involved.', "correct": False,
             "why": 'Building large molecules such as new bone and muscle protein still needs energy supplied by respiration; the raw materials come from food, but joining them together is not free.'},
            {"text": 'Gaining tissue this way is genuinely impossible.', "correct": False,
             "why": "It is not strictly impossible, because other factors — reduced activity elsewhere, or the doctor's estimate already allowing for it — could account for the extra energy needed."},
            {"text": "The friend has a fair point — building tissue is a real extra cost — but it can still balance out if the athlete is correspondingly less active elsewhere, or if the doctor's figure already allowed for it.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h16',
        "band": 'harder',
        "text": "A scientist blocks the mitochondria of a root hair cell with a poison that stops aerobic respiration completely, but leaves the rest of the cell undamaged. Predict what happens to the cell's uptake of water and of mineral ions over the next hour, and explain the difference.",
        "options": [
            {"text": 'Mineral uptake stops almost at once; water uptake continues for a while, needing no energy.', "correct": True},
            {"text": 'Both water uptake and mineral uptake stop completely and immediately, since both processes always need a steady supply of energy from respiration.', "correct": False,
             "why": 'Water moving into the root cell does so on its own, down its own gradient, and needs no energy supply, so it is not affected the moment respiration stops.'},
            {"text": 'Neither uptake process is affected at all, since both water and minerals move entirely independently of anything happening inside the mitochondria.', "correct": False,
             "why": 'Mineral uptake by active transport depends directly on a continuous supply of energy from respiration, so blocking the mitochondria does affect it.'},
            {"text": 'Mineral uptake carries on completely as normal, but water uptake stops immediately instead, the two swapped the wrong way round.', "correct": False,
             "why": 'It is mineral uptake that needs active transport and stops when respiration is blocked, while water uptake needs no energy supply and continues.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h17',
        "band": 'harder',
        "text": 'Two identical hamsters are kept for a month: one at a room temperature just below its comfortable range, and one well above it, hot enough that it pants to lose heat. Both eat noticeably more food than a third hamster kept at a comfortable, middle temperature. Explain why food intake rises in BOTH the cold and the hot room.',
        "options": [
            {"text": 'Both rises happen because keeping warm only ever means generating extra heat, so the hot hamster must be generating heat too.', "correct": False,
             "why": 'In the hot room the extra cost comes from cooling behaviour such as panting, not from generating additional heat, which would worsen overheating.'},
            {"text": 'In the cold, extra energy heats the body; in the heat, extra energy pays for cooling behaviour such as panting.', "correct": True},
            {"text": 'Neither rise is really about temperature at all; both are explained entirely by extra movement in an uncomfortable room.', "correct": False,
             "why": 'The ‘keeping warm’ job specifically accounts for the energy cost of holding body temperature away from the surrounding temperature, on both sides.'},
            {"text": 'Food intake only rises in the cold room; the hot-room rise is measurement error.', "correct": False,
             "why": 'Panting and other active cooling behaviour genuinely cost extra energy, so a real rise in the hot room is expected and is not simply an error.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h18',
        "band": 'harder',
        "text": 'A drug is found to block the recycling and repair of proteins inside cells, without affecting contraction directly. Predict which of the five cells on the bench would be affected soonest and most severely, and explain why.',
        "options": [
            {"text": 'The sperm cell, because almost all of its energy is spent on repair rather than on beating its tail at all.', "correct": False,
             "why": 'The sperm cell is described as spending nearly all of its energy on beating its tail, with very little left for anything else, including repair.'},
            {"text": 'The white blood cell, because repair is easily its single biggest energy cost of all.', "correct": False,
             "why": "The white blood cell's single biggest energy cost is described as crawling and engulfing bacteria, not repair."},
            {"text": 'The heart muscle cell, since it never rests and relies heavily on constant repair to keep working.', "correct": True},
            {"text": 'All five cells would be affected equally and to the same degree.', "correct": False,
             "why": 'The cells are described as having very different energy budgets and different reliance on ongoing repair.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h19',
        "band": 'harder',
        "text": "A stroke cuts off blood flow, and with it oxygen and glucose, to one small region of a person's brain. Doctors say the affected nerve cells begin to die within a few minutes if blood flow is not restored, far faster than most other cells in the body would in the same situation. Explain why brain cells are especially vulnerable to this kind of interruption.",
        "options": [
            {"text": 'Nerve cells are especially vulnerable because they are the only cells in the body that need oxygen at all.', "correct": False,
             "why": 'Every living cell needs a supply of oxygen for aerobic respiration, not only nerve cells; what makes them vulnerable is their very high, continuous demand.'},
            {"text": 'Nerve cells are especially vulnerable because they contain almost no mitochondria of their own.', "correct": False,
             "why": 'Nerve cells are described as having plenty of mitochondria, concentrated where signals are passed on.'},
            {"text": 'Nerve cells are especially vulnerable simply because they sit physically furthest from the heart.', "correct": False,
             "why": 'Distance from the heart is not the reason given; it is their unusually high and continuous energy demand with no reserve to draw on.'},
            {"text": 'Nerve cells run a large, continuous ion-pumping bill and the brain keeps essentially no reserve of oxygen or glucose, so cutting the supply removes what keeps that bill paid almost immediately.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h20',
        "band": 'harder',
        "text": "A gardener floods one plant pot for several days and keeps an identical plant well-watered but never waterlogged, with the same fertiliser in both. After a week, the flooded plant shows signs of mineral deficiency even though its soil actually contains more dissolved minerals than the well-watered pot's soil, because the fertiliser has not been washed away. Explain this apparent contradiction.",
        "options": [
            {"text": 'Waterlogging cuts off oxygen to the roots, so they cannot respire and cannot power active transport of minerals.', "correct": True},
            {"text": 'The flooding must have washed the minerals out of reach of the roots, even though the soil test shows more of them are dissolved there than in the other pot.', "correct": False,
             "why": "The minerals are still present and dissolved in the flooded pot's soil; the problem is the root cells' ability to take them up, not availability."},
            {"text": 'Waterlogged roots simply cannot absorb any dissolved substance at all through their cell membranes, mineral or otherwise, once flooded.', "correct": False,
             "why": 'Root hair cells can still absorb water even when waterlogged, since water moves in on its own and needs no energy; what stops is mineral uptake.'},
            {"text": 'The extra water has diluted the minerals so much that there is effectively none at all left for the plant to use.', "correct": False,
             "why": 'The flooded soil actually contains more dissolved minerals than the well-watered soil, so dilution cannot explain the deficiency.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h21',
        "band": 'harder',
        "text": 'Fertility research finds that sperm cells kept in a fluid rich in glucose but with no dissolved oxygen swim normally for only a very short time before stopping, while sperm kept in a fluid with both glucose and dissolved oxygen swim for far longer. Explain this difference, given that a sperm cell has stripped out almost everything not needed for swimming.',
        "options": [
            {"text": 'Glucose alone should be enough on its own, since it is the actual fuel respiration uses, and oxygen makes no real difference to how long swimming continues.', "correct": False,
             "why": "Releasing the full amount of energy from glucose by the sperm cell's normal route needs oxygen as well as glucose."},
            {"text": 'Without oxygen the sperm cell has no meaningful energy route left and no store to fall back on.', "correct": True},
            {"text": 'Dissolved oxygen makes the fluid noticeably less dense, letting the cells swim for longer with less effort.', "correct": False,
             "why": 'The difference is about how long the cells can keep respiring enough energy to swim, not about the density of the fluid.'},
            {"text": 'The sperm cells without oxygen are simply using up stored oxygen faster.', "correct": False,
             "why": 'A sperm cell holds no meaningful store of oxygen to use up in the first place; the fluid with no dissolved oxygen simply gives it none.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h22',
        "band": 'harder',
        "text": "A drug used in some cancer treatments deliberately damages the mitochondria of the fastest-dividing cells in the body. A doctor warns that patients on this drug are especially vulnerable to infections during treatment. Explain the connection between the drug's target and the doctor's warning, using what this lesson teaches about white blood cells.",
        "options": [
            {"text": "White blood cells do not actually use mitochondria at all, so the drug should not affect the patient's ability to fight off any infection whatsoever.", "correct": False,
             "why": 'White blood cells are described as building far more mitochondria once an infection begins, precisely because their extra activity needs the extra energy.'},
            {"text": 'The connection is coincidental, since white blood cells are not among the fastest-dividing cells the drug is targeting.', "correct": False,
             "why": 'White blood cells are specifically described as dividing rapidly during an infection, which is exactly the kind of fast division the drug targets.'},
            {"text": 'White blood cells divide rapidly and build more mitochondria to power the extra work of an infection, and the drug hits exactly those cells.', "correct": True},
            {"text": 'The drug only really affects red blood cells, which is why patients become anaemic rather than more vulnerable to infection.', "correct": False,
             "why": 'The warning is specifically about vulnerability to infection, which points to an effect on white blood cells rather than red ones.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h23',
        "band": 'harder',
        "text": 'A student proposes that a cell could save energy by using active transport instead of diffusion whenever it needs a substance to enter faster. Evaluate this proposal, given what determines whether a process needs energy.',
        "options": [
            {"text": 'Active transport always works faster than diffusion everywhere.', "correct": False,
             "why": 'The situation described is one where diffusion down the gradient would already move the substance in, so active transport adds cost without adding anything.'},
            {"text": 'Active transport costs no energy once a cell is already respiring anyway.', "correct": False,
             "why": 'Active transport requires a continuous supply of energy from respiration whenever it is used, regardless of what else the cell is doing.'},
            {"text": 'The proposal only really fails for water, which always has to move by diffusion alone.', "correct": False,
             "why": 'The flaw in the proposal is general, and applies to any substance already moving down its own gradient, not specifically to water.'},
            {"text": 'The proposal misunderstands what sets the energy cost — it is the direction relative to the gradient that matters, not speed, so this only adds cost for no gain.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h24',
        "band": 'harder',
        "text": 'A student says that if a substance is spread completely evenly between two connected spaces, with no concentration gradient left at all, diffusion has ‘stopped working’. Evaluate this claim.',
        "options": [
            {"text": 'Particles still move randomly both ways; there is simply no net movement left to drive once the gradient is gone.', "correct": True},
            {"text": 'Once a substance is spread evenly, absolutely all movement of its particles stops completely and permanently.', "correct": False,
             "why": 'Particles keep moving randomly even once concentration is equal on both sides; what stops is the net movement in one direction.'},
            {"text": 'Energy has to be supplied to keep diffusion running, and that energy has now run out entirely.', "correct": False,
             "why": 'Diffusion needs no energy supply at any point, gradient present or not; it simply has nothing left to drive net movement once concentrations are equal.'},
            {"text": 'Diffusion would now actually reverse and start pushing the substance back the other way instead.', "correct": False,
             "why": 'With no concentration gradient in either direction, there is no net movement either way, forwards or in reverse.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h25',
        "band": 'harder',
        "text": 'A biologist compares the mitochondria in a slice of resting skeletal muscle with the same muscle taken from the same person immediately after a marathon. Predict and explain what is most likely to differ between the two samples over time, given what determines how many mitochondria a cell builds.',
        "options": [
            {"text": 'The two samples should be completely identical immediately, since mitochondria are built the very instant a cell needs more energy and vanish the instant it does not.', "correct": False,
             "why": 'Mitochondria numbers change over a longer timescale in response to sustained demand, not instantly during or immediately after a single bout of exercise.'},
            {"text": 'Trained muscle tends to build more mitochondria over weeks, matching its higher regular energy demand.', "correct": True},
            {"text": 'Untrained resting muscle should actually contain more mitochondria, since a cell doing very little conserves them carefully for when they are needed.', "correct": False,
             "why": 'Cells with a lower regular energy demand tend to maintain fewer mitochondria, not more, than cells with a consistently higher demand.'},
            {"text": 'Neither sample should differ, since every cell holds an identical fixed number.', "correct": False,
             "why": 'Cells across a body vary a great deal in how many mitochondria they contain, generally matching how much energy each type of cell regularly needs.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h26',
        "band": 'harder',
        "text": 'A submarine crew is trapped for several hours with a failing air supply. Engineers can either pump in more oxygen or scrub carbon dioxide out of the air, but not both at once, and must choose which matters more urgently, given how little the body stores of each gas.',
        "options": [
            {"text": 'Scrubbing carbon dioxide is more urgent, because the body has absolutely no store of carbon dioxide and it must be removed instantly.', "correct": False,
             "why": 'It is oxygen that the body holds essentially no reserve of; carbon dioxide can be tolerated at raised levels for a period.'},
            {"text": 'Neither choice is more urgent, since both gases change at the same rate.', "correct": False,
             "why": "The body's ability to tolerate a shortage of one gas versus a build-up of the other is very different, which is exactly why one choice is more urgent."},
            {"text": 'Restoring oxygen is more urgent, since the body holds no real reserve of it, unlike carbon dioxide.', "correct": True},
            {"text": 'Oxygen can wait longer, since the body stores hours of it in the muscles.', "correct": False,
             "why": 'The body holds no meaningful store of oxygen in the muscles or anywhere else; this is why an interrupted supply becomes dangerous within minutes.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h27',
        "band": 'harder',
        "text": "A hospital patient's daily energy transfer of 6000 kJ is split so that 25% pays for keeping warm, 15% pays for active transport, and the remainder is split evenly between movement and building large molecules. How much energy, in kJ, is spent on movement alone?",
        "options": [
            {"text": '3000 kJ', "correct": False,
             "why": 'That is 50% of the total, as if the remaining 60% were not split between two jobs.'},
            {"text": '900 kJ', "correct": False,
             "why": 'That halves the correct share again, taking 15% of the total instead of 30%.'},
            {"text": '2400 kJ', "correct": False,
             "why": 'That is 40%, the share spent on keeping warm and active transport combined, not the share left for movement.'},
            {"text": '1800 kJ', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h28',
        "band": 'harder',
        "text": "A biologist studies two lizard species, one living in a cold mountain habitat and one in a warm lowland habitat, and finds their resting energy use per gram of body mass is almost identical. A colleague expected the mountain lizard to use noticeably more energy at rest, reasoning by comparison with a mouse living at altitude. Explain why the colleague's reasoning does not carry over to lizards.",
        "options": [
            {"text": 'Lizards do not hold a set body temperature the way mammals do, so a colder surrounding adds no extra ‘keeping warm’ cost.', "correct": True},
            {"text": "The reasoning is right, and the finding must be a measurement error, since a colder environment should always raise any resting animal's energy use regardless of species.", "correct": False,
             "why": "The finding does not have to be an error — the ‘keeping warm’ cost that raises a mouse's energy use in the cold specifically depends on holding a set body temperature."},
            {"text": "Lizards do not respire at all once the surrounding temperature drops, which is why the mountain lizard's energy use stays the same.", "correct": False,
             "why": 'Lizards continue respiring in cold environments; what differs from a mammal is that they are not paying an extra ‘keeping warm’ bill.'},
            {"text": 'The mountain lizard must simply be moving around noticeably less than the lowland one, which cancels out any extra cost from the cold.', "correct": False,
             "why": 'The explanation does not rely on an assumption about how much either lizard moves; it rests on lizards not paying the mammal-style ‘keeping warm’ bill.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h29',
        "band": 'harder',
        "text": "A researcher claims that during hibernation an animal's cells briefly stop respiring altogether to save energy, then restart when the animal wakes. Evaluate this claim against what you know about respiration in living cells.",
        "options": [
            {"text": 'This is exactly what makes hibernation possible — cells pause completely and use no energy until the animal wakes up again.', "correct": False,
             "why": 'A cell with no energy supply at all would die rather than pause; what actually happens in hibernation is respiration slowing to a very low rate, not stopping.'},
            {"text": 'Respiration slows to a tiny fraction of normal; a cell with none at all would have no energy to stay alive.', "correct": True},
            {"text": "The claim is correct only for the animal's muscle cells, which really do stop completely while every other cell keeps respiring as normal.", "correct": False,
             "why": "The slowdown of respiration during hibernation applies broadly across the hibernating animal's cells, not to muscle cells alone."},
            {"text": 'The claim is wrong only because hibernating animals never actually lower their body temperature at all.', "correct": False,
             "why": 'Hibernating animals do lower their body temperature substantially, which goes with a much lower, but never zero, rate of respiration.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h30',
        "band": 'harder',
        "text": 'A student measures the oxygen concentration inside a sealed, transparent box containing a single potted plant, once in constant bright light and once in constant darkness, over 24 hours each time. In the light the oxygen level rises; in the dark it falls. The student concludes that the plant only respires in the dark. Evaluate this conclusion.',
        "options": [
            {"text": "A net rise in the box's oxygen level could only ever happen once respiration itself had completely stopped altogether.", "correct": False,
             "why": 'A net rise can happen even while respiration continues, if photosynthesis is releasing oxygen faster than respiration is using it up.'},
            {"text": 'The sealed box gave a false reading in both conditions tested.', "correct": False,
             "why": 'Sealing the box is what makes the measurement possible at all; the flaw is in interpreting a net change as showing respiration has stopped.'},
            {"text": 'The plant respires in both conditions; in the light, photosynthesis simply releases oxygen faster than respiration uses it.', "correct": True},
            {"text": 'The conclusion is correct for this plant, but would be wrong for one kept permanently in darkness.', "correct": False,
             "why": 'The flaw in the conclusion is the same regardless of lighting — a net oxygen measurement does not by itself show whether respiration is happening.'},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h31',
        "band": 'harder',
        "text": 'A student argues that because fungi decompose dead material rather than hunting or photosynthesising, they must get their energy directly from the dead material without needing to respire it. Evaluate this argument.',
        "options": [
            {"text": 'The argument is correct, since decomposition itself is a form of energy release that needs no respiration.', "correct": False,
             "why": 'Decomposition describes the breakdown of dead material into simpler molecules the fungus can absorb; releasing usable energy from them still needs respiration.'},
            {"text": 'The argument is correct only for fungi that decompose wood, since wood already contains released energy.', "correct": False,
             "why": "Wood, like any other organic material, is a source of fuel that still has to be respired by the fungus's own cells."},
            {"text": 'The argument is wrong, but only because fungi actually photosynthesise as well as decompose.', "correct": False,
             "why": 'Fungi have no chlorophyll and do not photosynthesise; the flaw is about how energy is released from fuel, not about an extra energy source.'},
            {"text": 'The argument confuses obtaining fuel with releasing energy from it — a fungus still has to respire the fuel it absorbs, just as an animal respires its food.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b8-02-h32',
        "band": 'harder',
        "text": 'A single-celled amoeba and a human liver cell are compared. Both respire glucose and both need a supply of oxygen. A student argues that since both processes are ‘the same reaction’, the amoeba should be just as vulnerable to a sudden local drop in oxygen as an isolated human liver cell would be. Evaluate this claim, considering how each cell obtains its oxygen.',
        "options": [
            {"text": 'The amoeba exchanges oxygen directly with the water around it, while an isolated liver cell depends entirely on a blood supply reaching it.', "correct": True},
            {"text": 'The claim is wrong only because the amoeba does not need any oxygen at all to respire, unlike the liver cell, which absolutely requires a constant supply.', "correct": False,
             "why": 'Both cells are described as needing a supply of oxygen; the real difference is in how reliably that supply reaches each cell.'},
            {"text": 'The claim is wrong only because a human liver cell keeps a substantial store of oxygen inside itself that the amoeba entirely and completely lacks.', "correct": False,
             "why": 'Neither kind of cell holds a meaningful oxygen store; the real difference is in how each obtains its ongoing supply.'},
            {"text": 'Two identical chemical reactions must always be equally vulnerable to any interruption whatsoever, wherever they occur.', "correct": False,
             "why": "The chemical reaction being identical does not make the two cells equally vulnerable, because how reliably each cell's oxygen supply is delivered differs greatly."},
        ],
        "figure": None,
    },
]

QUESTIONS.extend(_MRB338_NEW_QUESTIONS)
