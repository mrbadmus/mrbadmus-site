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
            {"text": "None — only what the blood is carrying at that moment.",
             "correct": True},
            {"text": "Enough for a few hours, held inside the muscles.",
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
            {"text": "Movement, paid for by respiration in the muscles around "
                     "the bone.",
             "correct": False,
             "why": "The muscles are not what is building the bone. New "
                    "tissue is assembled molecule by molecule, and that is a "
                    "job in its own right."},
            {"text": "Building large molecules, paid for by respiration in "
                     "the cells doing it.",
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
            {"text": "It is pumping ions across its membrane and repairing "
                     "itself constantly.",
             "correct": True},
            {"text": "It is storing energy up so that it is ready when work "
                     "arrives.",
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
            {"text": "They have stopped respiring, which is how they manage "
                     "without food.",
             "correct": False,
             "why": "No cell can stop. What is small here is the rate, and it "
                    "is small because two of the four bills come to almost "
                    "nothing."},
            {"text": "They pay almost nothing for warmth or movement, so the "
                     "cells' bill is small.",
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
