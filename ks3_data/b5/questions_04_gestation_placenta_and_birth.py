"""B5 lesson 04 — Gestation, the placenta and birth: twelve questions (MRB-269).

The lesson has one argument — the placenta is an exchange surface, so every
crossing is a concentration difference and nothing is ever chosen, pumped or
mixed — and the bank is built to catch a student who has kept the placenta as a
kind of pipe or a kind of filter. The easier band holds the four facts the
argument rests on: where the missing fortnight between 38 and 40 weeks comes
from, the three features of a good exchange surface, the eight-week seam
between embryo and foetus, and which pair of substances travels which way. The
standard band works the six substances the student committed to at the bench —
the antibody crossing that is not diffusion, nicotine crossing for exactly the
same reason oxygen does, urea leaving although the foetus makes urine, and the
stage of the pregnancy that explains why a baby born at 30 weeks needs help
breathing. The harder band joins two ideas or moves them somewhere new: foetal
haemoglobin read as a statement about the concentration difference, the same
molecule crossing at week 5 and at week 30, the placenta as an organ carrying
somebody else's chromosomes, and a transfusion set beside the two consequences
of the bloods mixing.

The distractors are the lesson's two declared misconceptions plus the one it
deliberately hands forward. REPRO-08 ("the baby's blood mixes with the mother's
blood in the placenta") supplies the mixing option in e04's neighbours, the
her-blood-enters-the-foetus option in s01 and the whole of h04's wrong set.
REPRO-07 ("the baby breathes and eats inside the uterus") supplies the
lungs-start-at-birth option in s04 and the foetus-deals-with-its-own-waste
option in s03. REPRO-09 — the placenta as a filter, which b5-05 owns and this
lesson only sets up — supplies s02's blocked option and h02's
antibodies-protect option, and both `why` lines correct it without claiming
b5-05's confrontation. Two further errors the lesson corrects in passing supply
the rest: something being pulled or pumped across rather than diffusing (h01,
e02), and the amniotic fluid read as somewhere outside the system (s03, h02).

`figure` is None throughout. The lesson declares one figure, `b5-placenta-
exchange`, at `status: "needed"` — no artwork exists for it, and a question
that leant on a diagram nobody has drawn would be unanswerable on the built
page.
"""

UNIT = "B5"
LESSON = "gestation-placenta-and-birth"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-04-e01",
        "band": "easier",
        "text": "Gestation in humans is about 38 weeks, but a pregnancy is "
                "almost always described as 40 weeks long. Where does the "
                "extra fortnight come from?",
        "options": [
            {"text": "Babies are usually born about two weeks late, so the "
                     "figure was rounded up to match.",
             "correct": False,
             "why": "The 40 weeks is not an average of how late babies "
                    "arrive. It is the same pregnancy measured from an "
                    "earlier starting point, so both numbers describe the "
                    "same event."},
            {"text": "Pregnancy is dated from the first day of the last "
                     "period, about two weeks before fertilisation.",
             "correct": True},
            {"text": "The last two weeks are the birth itself, which is "
                     "counted separately from the gestation.",
             "correct": False,
             "why": "Birth is one stage at around 40 weeks, not a fortnight "
                    "bolted on at the end. The extra two weeks sit at the "
                    "start, in how the counting begins."},
            {"text": "The ball of cells spends two weeks travelling before it "
                     "implants in the uterus lining.",
             "correct": False,
             "why": "Implantation is about five days after fertilisation, not "
                    "two weeks — and those five days are already inside the "
                    "38 weeks of gestation."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e02",
        "band": "easier",
        "text": "A student lists what makes the placenta a good exchange "
                "surface: a very large surface area, a very thin barrier, and "
                "a thick muscular wall to pump substances across. Which part "
                "is wrong?",
        "options": [
            {"text": "The third. It should be a good blood supply on both "
                     "sides, keeping the concentration difference up.",
             "correct": True},
            {"text": "The first. The placenta is small, and it is the "
                     "thinness of the barrier that does all the work.",
             "correct": False,
             "why": "The surface is enormous — the placenta folds into "
                    "thousands of finger-like projections to get the area up. "
                    "Thinness matters too, and both belong on the list."},
            {"text": "The second. A thick barrier is needed to hold the two "
                     "blood supplies safely apart.",
             "correct": False,
             "why": "The barrier is thin, a fraction of a millimetre, and "
                    "that is what makes diffusion fast enough. The two bloods "
                    "stay separate because they are in separate vessels."},
            {"text": "None of them. All three are genuine features of an "
                     "exchange surface anywhere in the body.",
             "correct": False,
             "why": "Nothing is pumped across the placenta. Almost everything "
                    "crosses by diffusion, down a concentration difference, "
                    "with no muscle involved at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e03",
        "band": "easier",
        "text": "At what point does the word “embryo” give way to the word "
                "“foetus”, and what has changed by then?",
        "options": [
            {"text": "At implantation, five days in, once the ball of cells "
                     "has embedded in the uterus lining.",
             "correct": False,
             "why": "Implantation is where gestation is counted from, but the "
                    "developing organism is called an embryo for the whole of "
                    "the first eight weeks — far longer than five days."},
            {"text": "At around week twelve, once the placenta has finished "
                     "growing into the wall of the uterus.",
             "correct": False,
             "why": "The exchange surface is built across weeks 1–12, but the "
                    "name changes at about week nine, and it changes with the "
                    "organs rather than with the placenta."},
            {"text": "At about week nine, once the organs exist and are "
                     "growing and maturing rather than being formed.",
             "correct": True},
            {"text": "At birth, when the lungs are used for the first time "
                     "and the umbilical cord is cut.",
             "correct": False,
             "why": "After birth it is a baby. Foetus is the word for the "
                    "whole stretch from about week nine until birth, which is "
                    "most of the pregnancy."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e04",
        "band": "easier",
        "text": "Which pair of substances crosses the placenta out of the "
                "foetus's blood and into the mother's?",
        "options": [
            {"text": "Oxygen and glucose.",
             "correct": False,
             "why": "Both cross the other way, into the foetus. It cannot "
                    "breathe and cannot eat, so both have to arrive from the "
                    "mother's blood."},
            {"text": "Glucose and carbon dioxide.",
             "correct": False,
             "why": "Carbon dioxide does leave, but glucose arrives. Check "
                    "each substance separately — the rule is the same for all "
                    "of them, but the direction is not."},
            {"text": "Urea and antibodies.",
             "correct": False,
             "why": "Urea does leave. Antibodies go the other way, into the "
                    "foetus, stocking it with a copy of the mother's immunity "
                    "for its first few months."},
            {"text": "Carbon dioxide and urea.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-04-s01",
        "band": "standard",
        "text": "Antibodies are far larger than anything else on the list of "
                "substances that cross the placenta, and they still reach the "
                "foetus. How do they get across?",
        "options": [
            {"text": "They diffuse across like everything else, only more "
                     "slowly because they are so large.",
             "correct": False,
             "why": "They are far too big to slip across a barrier built for "
                    "small molecules, and no amount of time changes that. "
                    "Something else has to move them."},
            {"text": "They are broken into small pieces, cross the barrier, "
                     "and are rebuilt in the foetus's blood.",
             "correct": False,
             "why": "Nothing takes them apart. An antibody broken up would no "
                    "longer work as an antibody, and the whole protein is "
                    "what arrives on the other side."},
            {"text": "The placenta carries them across deliberately, using "
                     "energy — the one crossing that is not diffusion.",
             "correct": True},
            {"text": "They travel in the mother's blood, which enters the "
                     "foetus along the umbilical cord.",
             "correct": False,
             "why": "Her blood never enters the foetus; the two circulations "
                    "stay separate for the whole pregnancy. The antibodies "
                    "cross the barrier without her blood crossing it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s02",
        "band": "standard",
        "text": "Nicotine molecules are small and dissolved in the blood, "
                "exactly like oxygen and glucose. Predict what the placenta "
                "does with them.",
        "options": [
            {"text": "They cross into the foetus, because the placenta cannot "
                     "tell a useful small molecule from a harmful one.",
             "correct": True},
            {"text": "They are blocked, because the placenta filters out "
                     "anything that could harm the developing foetus.",
             "correct": False,
             "why": "The placenta is an exchange surface, not a filter. It "
                    "has no mechanism at all for judging what a molecule will "
                    "do once it arrives."},
            {"text": "They cross only if the mother has a large enough amount "
                     "of it in her blood at any one time.",
             "correct": False,
             "why": "There is no threshold to pass. Crossing depends on being "
                    "small and dissolved, and on the concentration "
                    "difference, so any amount begins crossing."},
            {"text": "They are broken down inside the barrier before they can "
                     "reach the foetal blood at all.",
             "correct": False,
             "why": "Nothing on the list is destroyed on the way across. A "
                    "small dissolved molecule diffuses down its concentration "
                    "difference the same way oxygen does."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s03",
        "band": "standard",
        "text": "A foetus has kidneys, and they do make urine, which passes "
                "into the fluid around it. So why does its urea still have to "
                "cross the placenta?",
        "options": [
            {"text": "It does not — its own kidneys deal with all of it, and "
                     "the fluid around it is replaced regularly.",
             "correct": False,
             "why": "The kidneys cannot finish the job, because everything "
                    "they make stays inside the system. Something still has "
                    "to take the urea out of it altogether."},
            {"text": "The foetal kidneys do not start working until the last "
                     "few weeks before the birth.",
             "correct": False,
             "why": "They work, and they make urine. The problem is not that "
                    "the kidneys fail; it is that there is nowhere inside for "
                    "the urea they produce to go."},
            {"text": "The mother's kidneys make the urea, and it crosses into "
                     "the foetus to be stored until birth.",
             "correct": False,
             "why": "That is the direction reversed. The foetus makes the "
                    "urea itself, from breaking down surplus amino acids, and "
                    "it crosses out into her blood."},
            {"text": "Urine into that fluid keeps the urea inside the system; "
                     "only the placenta takes it out altogether.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s04",
        "band": "standard",
        "text": "A baby born at 30 weeks often needs help with breathing, "
                "while one born at 40 weeks usually does not. Which stage of "
                "the pregnancy explains that?",
        "options": [
            {"text": "Organs are laid down, weeks 3–8 — a baby born early "
                     "never formed lungs in the first place.",
             "correct": False,
             "why": "The lungs are laid down in the first eight weeks like "
                    "every other organ. What is missing at 30 weeks is the "
                    "finishing, not the building."},
            {"text": "Growth and maturing, weeks 9–40 — the lungs are among "
                     "the last organs to be ready.",
             "correct": True},
            {"text": "The exchange surface is built, weeks 1–12 — a small "
                     "placenta leaves the lungs short of oxygen.",
             "correct": False,
             "why": "That stage builds the supply line, and it is long "
                    "finished by 30 weeks. The breathing problem is about how "
                    "far the lungs themselves have matured."},
            {"text": "Birth, around 40 weeks — the lungs only begin growing "
                     "once the umbilical cord has been cut.",
             "correct": False,
             "why": "Nothing starts growing at birth. The first breath is the "
                    "first time the lungs are used, but they were built and "
                    "matured across the whole pregnancy."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-04-h01",
        "band": "harder",
        "text": "Foetal haemoglobin holds on to oxygen more tightly than the "
                "adult kind. Explain how that helps oxygen keep crossing the "
                "placenta.",
        "options": [
            {"text": "It lets the foetal blood pull oxygen out of the "
                     "mother's blood and across the thin barrier.",
             "correct": False,
             "why": "Nothing pulls anything across the placenta. The tighter "
                    "grip works by keeping the foetal side low, and oxygen "
                    "then diffuses down that difference by itself."},
            {"text": "It means the foetus needs less oxygen overall, so a "
                     "smaller amount has to cross each minute.",
             "correct": False,
             "why": "The foetus respires like any other organism and its "
                    "demand does not fall. What the tighter grip changes is "
                    "the concentration difference, not the requirement."},
            {"text": "It makes the barrier between the two circulations "
                     "thinner as the pregnancy goes on.",
             "correct": False,
             "why": "Haemoglobin sits inside red blood cells and cannot "
                    "change the barrier. It acts on the third feature of the "
                    "exchange surface: the difference across it."},
            {"text": "It keeps free oxygen in the foetal blood low, so the "
                     "difference across the barrier stays large.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h02",
        "band": "harder",
        "text": "The same small harmful molecule crosses the placenta at week "
                "5 and again at week 30. Why is the earlier crossing likely "
                "to matter more?",
        "options": [
            {"text": "Weeks 3–8 is when the organs are being laid down, so "
                     "anything crossing then affects how they form.",
             "correct": True},
            {"text": "The barrier is thinner in the early weeks, so far more "
                     "of the molecule gets across at week 5.",
             "correct": False,
             "why": "The barrier is thin throughout — that is what makes it "
                    "an exchange surface. What differs is what the developing "
                    "organism is doing at the time."},
            {"text": "By week 30 the antibodies carried across the placenta "
                     "protect the foetus from harmful molecules.",
             "correct": False,
             "why": "Antibodies act against infection, not against dissolved "
                    "chemicals — and the placenta never gains any way of "
                    "telling a harmful small molecule from a useful one."},
            {"text": "By week 30 the foetus is big enough to pass the "
                     "molecule out into the fluid around it.",
             "correct": False,
             "why": "That fluid is not outside the system. Urea passed into "
                    "it still has to leave across the placenta, and anything "
                    "else the foetus produces is in the same position."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h03",
        "band": "harder",
        "text": "A transplanted kidney is attacked unless drugs prevent it. "
                "The placenta carries foreign proteins too, and is not "
                "attacked. What makes its proteins foreign?",
        "options": [
            {"text": "The mother's immune system has never met it before, "
                     "because it forms so quickly after implantation.",
             "correct": False,
             "why": "Novelty is not about speed. The proteins count as "
                    "foreign because of which chromosomes coded them, not "
                    "because of how fast the organ appeared."},
            {"text": "The uterus builds it out of the mother's own tissue, "
                     "and she then discards it at the birth.",
             "correct": False,
             "why": "It is not built from her tissue. It grows from the same "
                    "ball of cells as the embryo, which is exactly why "
                    "foreign proteins are on it at all."},
            {"text": "It grows from the same ball of cells as the embryo, so "
                     "its cells carry the embryo's chromosomes.",
             "correct": True},
            {"text": "The foetal blood flowing through it belongs to a "
                     "different individual from the mother.",
             "correct": False,
             "why": "That blood is indeed not hers, but the puzzle is about "
                    "the organ's own cells. It is the placenta's tissue that "
                    "carries a foreign set of chromosomes."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h04",
        "band": "harder",
        "text": "A hospital will never transfuse blood of the wrong group "
                "into a patient. Use that to give one reason the two "
                "circulations must stay separate.",
        "options": [
            {"text": "The foetus would receive too much oxygen at once, and "
                     "its growing tissues would be damaged by it.",
             "correct": False,
             "why": "Oxygen is not the danger. Two things go wrong if the "
                    "bloods mix: incompatible blood groups clot, and adult "
                    "blood pressure destroys the placenta's vessels."},
            {"text": "A mother and her baby often have different blood "
                     "groups, and mixing incompatible blood makes it clot.",
             "correct": True},
            {"text": "The foetus's blood would be diluted by hers, so it "
                     "could no longer carry enough oxygen around.",
             "correct": False,
             "why": "Nothing is diluted. The two reasons the page gives are "
                    "blood groups clotting and the pressure of an adult heart "
                    "wrecking the delicate placental vessels."},
            {"text": "Her immune system would attack the placenta the moment "
                     "the two blood supplies met.",
             "correct": False,
             "why": "The placenta already carries foreign proteins and is "
                    "normally not attacked — that is the unsolved question in "
                    "Going further, not the reason the bloods stay apart."},
        ],
        "figure": None,
    },
]
