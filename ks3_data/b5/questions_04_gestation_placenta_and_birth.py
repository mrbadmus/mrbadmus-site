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

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-04-e05",
        "band": "easier",
        "text": "What happens to the placenta at the end of a pregnancy?",
        "options": [
            {"text": "It stays in the uterus and is slowly absorbed",
             "correct": False,
             "why": "It is delivered, not absorbed. Once the cord is cut it "
                    "has nothing left to connect and no job to do."},
            {"text": "It is delivered after the baby, because it is no longer "
                     "needed", "correct": True},
            {"text": "It becomes part of the baby once the cord is cut",
             "correct": False,
             "why": "It grew from the same ball of cells as the embryo, but "
                    "it is never part of the baby’s body. It is the one organ "
                    "a person builds, uses and then discards."},
            {"text": "It stays attached to the wall of the uterus, ready for "
                     "a later pregnancy", "correct": False,
             "why": "A new placenta is built for every pregnancy, over the "
                    "first twelve weeks. Nothing is kept."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e06",
        "band": "easier",
        "text": "Which structure carries the foetus’s own blood out to the "
                "placenta and back again?",
        "options": [
            {"text": "The amniotic fluid", "correct": False,
             "why": "That fluid surrounds the foetus and cushions it. Nothing "
                    "is carried through it in vessels."},
            {"text": "The oviduct", "correct": False,
             "why": "The oviduct is where fertilisation happened, weeks "
                    "earlier. It has no part in supplying a foetus."},
            {"text": "The umbilical cord", "correct": True},
            {"text": "The cervix", "correct": False,
             "why": "The cervix is the lower opening of the uterus, held "
                    "closed for the whole pregnancy. It carries nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e07",
        "band": "easier",
        "text": "During which weeks of a pregnancy are the organs laid down?",
        "options": [
            {"text": "Weeks 9 to 40", "correct": False,
             "why": "By week nine the organs already exist. Those weeks are "
                    "spent growing them and finishing them off."},
            {"text": "The last three weeks before birth", "correct": False,
             "why": "Nothing new is built that late. The lungs are still "
                    "getting ready, but they were laid down long before."},
            {"text": "Weeks 1 and 2", "correct": False,
             "why": "In the first fortnight the ball of cells is implanting "
                    "and beginning to build the placenta. There are no organs "
                    "yet."},
            {"text": "Weeks 3 to 8", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-04-s05",
        "band": "standard",
        "text": "As it grows into the wall of the uterus, the placenta folds "
                "into thousands of finger-like projections. Which feature of "
                "a good exchange surface does that folding give it?",
        "options": [
            {"text": "A very large surface area to exchange across",
             "correct": True},
            {"text": "A very thin barrier between the two blood supplies",
             "correct": False,
             "why": "Thinness depends on how few cells lie between the two "
                    "supplies, and folding does not change that. Folding buys "
                    "area, not closeness."},
            {"text": "A good blood supply on both sides of it",
             "correct": False,
             "why": "The blood supply comes from the vessels growing into "
                    "each side. What the folding does is give those vessels "
                    "far more surface to work across."},
            {"text": "A seal that keeps the two blood supplies from mixing",
             "correct": False,
             "why": "The two are kept apart by the barrier between them, "
                    "which folding leaves exactly as it was."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s06",
        "band": "standard",
        "text": "Glucose crosses the placenta into the foetus’s blood. Where "
                "did that glucose come from?",
        "options": [
            {"text": "The placenta makes it from a store built up earlier in "
                     "the pregnancy", "correct": False,
             "why": "The placenta is an exchange surface, not a factory. "
                    "Everything that crosses it arrived in one of the two "
                    "blood supplies first."},
            {"text": "The mother’s digestion — her small intestine absorbed "
                     "it into her blood", "correct": True},
            {"text": "The amniotic fluid, which the foetus swallows",
             "correct": False,
             "why": "The foetus does swallow that fluid, but its glucose does "
                    "not come from there. It arrives dissolved in blood, at "
                    "the placenta."},
            {"text": "The foetus makes it itself, by respiring",
             "correct": False,
             "why": "Respiration uses glucose up and releases energy from it. "
                    "Nothing in the body makes glucose by respiring."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s07",
        "band": "standard",
        "text": "Put the events of birth into the order in which they happen.",
        "options": [
            {"text": "The placenta is delivered, then the cervix opens, then "
                     "the baby is delivered", "correct": False,
             "why": "The placenta is the last thing to leave, not the first. "
                    "Until the baby is born it is still supplying it."},
            {"text": "The baby is delivered, then the cervix opens, then the "
                     "placenta is delivered", "correct": False,
             "why": "The cervix has to open before anything can pass through "
                    "it. It is the closed lower end of the uterus."},
            {"text": "The uterus contracts and the cervix opens, the baby is "
                     "delivered, then the placenta follows", "correct": True},
            {"text": "The cord is cut, then the cervix opens, then the baby "
                     "is delivered", "correct": False,
             "why": "The cord is cut once the baby has been born, so nothing "
                    "about it can come first."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-04-h05",
        "band": "harder",
        "text": "A pregnancy is dated from the first day of the last period, "
                "about two weeks before fertilisation. If a pregnancy is "
                "described as 32 weeks, for roughly how long has the foetus "
                "itself existed?",
        "options": [
            {"text": "About 34 weeks", "correct": False,
             "why": "This adds the fortnight where it should be taken off. "
                    "The foetus is younger than the dated pregnancy, not "
                    "older."},
            {"text": "About 32 weeks", "correct": False,
             "why": "That is the dated length of the pregnancy. Because the "
                    "dating begins a fortnight before fertilisation, the "
                    "foetus has existed for less time than that."},
            {"text": "About 6 weeks", "correct": False,
             "why": "Six weeks is roughly what is left before a 38-week "
                    "gestation is complete. The question asks how long the "
                    "foetus has already existed."},
            {"text": "About 30 weeks", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h06",
        "band": "harder",
        "text": "A pregnant person is given oxygen through a mask, and the "
                "amount of oxygen in her blood rises. Predict what happens at "
                "the placenta, and say why.",
        "options": [
            {"text": "More oxygen crosses to the foetus, because the "
                     "difference between the two bloods is now larger",
             "correct": True},
            {"text": "Nothing changes, because the two blood supplies never "
                     "mix", "correct": False,
             "why": "They never mix and oxygen still crosses, by diffusing "
                    "between them. Not mixing is not the same as not "
                    "exchanging."},
            {"text": "Nothing changes, because the placenta passes across "
                     "only what the foetus asks for", "correct": False,
             "why": "The placenta works nothing out. Substances move down "
                    "whatever difference exists, so a larger difference means "
                    "a faster crossing."},
            {"text": "The foetus receives too much oxygen, because it is "
                     "pumped across under pressure", "correct": False,
             "why": "Nothing is pumped across. Diffusion has no pressure "
                    "behind it, and it slows as the difference between the "
                    "two sides closes."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h07",
        "band": "harder",
        "text": "The foetus’s carbon dioxide leaves the body through the "
                "mother’s lungs, and its urea through her kidneys. Which "
                "statement about that is right?",
        "options": [
            {"text": "The foetus has no kidneys and no lungs of its own until "
                     "it is born", "correct": False,
             "why": "It has both. The kidneys even make urine, which passes "
                    "into the amniotic fluid, and the lungs are formed but "
                    "full of fluid."},
            {"text": "Its waste crosses the placenta into her blood, and her "
                     "organs do the removing", "correct": True},
            {"text": "The placenta removes the carbon dioxide and urea "
                     "itself, so the foetus needs neither organ",
             "correct": False,
             "why": "The placenta is a surface things cross, and nothing "
                    "leaves the body there. Whatever crosses is still inside "
                    "her, and her organs have to deal with it."},
            {"text": "Its own kidneys and lungs do the work, through the "
                     "umbilical cord", "correct": False,
             "why": "The cord carries the foetus’s blood to the placenta and "
                    "back, not to any organ of hers. Its lungs are not used "
                    "at all before birth."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-04-e08",
        "band": "easier",
        "text": "About five days after fertilisation, where does the ball of "
                "cells embed?",
        "options": [
            {"text": "In the wall of the oviduct, where fertilisation happened",
             "correct": False,
             "why": "Fertilisation happens there, but the ball of cells travels "
                    "on before it settles anywhere."},
            {"text": "In the cervix, at the lower end of the uterus",
             "correct": False,
             "why": "The cervix is the opening at the base of the uterus, and "
                    "it stays closed for the whole pregnancy."},
            {"text": "In the thickened lining of the uterus, where it then stays",
             "correct": True},
            {"text": "In the fluid around it, attached to nothing at all",
             "correct": False,
             "why": "Implanting means attaching. A ball of cells fixed to "
                    "nothing would have no supply at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e09",
        "band": "easier",
        "text": "What does the word gestation describe?",
        "options": [
            {"text": "The time a developing organism spends in the uterus",
             "correct": True},
            {"text": "The time from the last period until the birth",
             "correct": False,
             "why": "That is the span a pregnancy is dated over, and it is "
                    "about a fortnight longer than the gestation."},
            {"text": "The stage in which all the organs are laid down",
             "correct": False,
             "why": "That stage is weeks three to eight. Gestation covers the "
                    "whole time, not one stretch of it."},
            {"text": "The delivery of the baby and then the placenta",
             "correct": False,
             "why": "That is birth, which ends the gestation rather than being "
                    "the whole of it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e10",
        "band": "easier",
        "text": "What is the amniotic fluid?",
        "options": [
            {"text": "The blood the placenta holds ready for the foetus",
             "correct": False,
             "why": "No blood is held in store anywhere. The foetus has its "
                    "own blood, moving in its own vessels."},
            {"text": "The liquid that surrounds and cushions the foetus",
             "correct": True},
            {"text": "The liquid the umbilical cord carries to the foetus",
             "correct": False,
             "why": "The cord carries the foetus's own blood out to the "
                    "placenta and back, and carries nothing else."},
            {"text": "The mother's blood, filling the uterus",
             "correct": False,
             "why": "Her blood stays inside her own vessels throughout. It is "
                    "never loose in the uterus."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e11",
        "band": "easier",
        "text": "Why are a foetus's lungs not used before it is born?",
        "options": [
            {"text": "They have not been built yet at any point before birth",
             "correct": False,
             "why": "They are built in the first eight weeks with every other "
                    "organ, and then spend the rest of the time maturing."},
            {"text": "They are full of fluid, and no gas exchange happens in "
                     "them", "correct": True},
            {"text": "They are kept shut by the pressure of the fluid outside",
             "correct": False,
             "why": "Nothing is being held shut. There is simply no air in the "
                    "uterus for a lung to work with."},
            {"text": "They are used, but only for the last few weeks of it",
             "correct": False,
             "why": "The first breath at birth is genuinely the first. Until "
                    "then every scrap of oxygen arrives dissolved in blood."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e12",
        "band": "easier",
        "text": "Antibodies cross the placenta into the foetus. What do they "
                "give it?",
        "options": [
            {"text": "A store of protein it can break down for energy",
             "correct": False,
             "why": "Antibodies are not a food store, and nothing takes them "
                    "apart. They arrive whole and go to work whole."},
            {"text": "A way of carrying more oxygen in its blood",
             "correct": False,
             "why": "Oxygen is carried by haemoglobin inside red blood cells. "
                    "Antibodies have nothing to do with it."},
            {"text": "Protection against infections in its early life",
             "correct": True},
            {"text": "A set of the mother's chromosomes to build with",
             "correct": False,
             "why": "Chromosomes came from the two gametes at fertilisation. "
                    "Nothing else crossing the placenta carries any."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e13",
        "band": "easier",
        "text": "How thick is the tissue separating the two blood supplies in "
                "the placenta?",
        "options": [
            {"text": "A fraction of a millimetre", "correct": True},
            {"text": "A centimetre of muscle", "correct": False,
             "why": "There is no muscle in it at all, and a barrier that thick "
                    "would be far too slow to diffuse across."},
            {"text": "About the thickness of skin", "correct": False,
             "why": "Skin is many cells deep and is built to keep things out. "
                    "This surface is built to let things through."},
            {"text": "Nothing — they touch directly", "correct": False,
             "why": "If they touched, the two bloods would mix, and the whole "
                    "arrangement exists to stop that happening."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e14",
        "band": "easier",
        "text": "Over which weeks does the placenta grow into the wall of the "
                "uterus?",
        "options": [
            {"text": "Weeks 9 to 40", "correct": False,
             "why": "By week nine the supply line is largely in place. Those "
                    "weeks are spent growing the foetus, not building it."},
            {"text": "Weeks 1 to 12", "correct": True},
            {"text": "The final month before the birth", "correct": False,
             "why": "Everything the foetus received in the eight months before "
                    "that had to cross a placenta, so it existed long before."},
            {"text": "The five days before implantation", "correct": False,
             "why": "Nothing is attached to the uterus in those days. Building "
                    "begins once the ball of cells has embedded."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e15",
        "band": "easier",
        "text": "What pushes the baby out during a birth?",
        "options": [
            {"text": "The pressure of the amniotic fluid behind it",
             "correct": False,
             "why": "That fluid has cushioned the foetus all along and pushes "
                    "nothing anywhere."},
            {"text": "Contractions of the muscular wall of the uterus",
             "correct": True},
            {"text": "Contractions of the placenta against the uterus wall",
             "correct": False,
             "why": "The placenta has no muscle in it. It is an exchange "
                    "surface, and it is delivered afterwards."},
            {"text": "The baby pushing against the opening of the cervix",
             "correct": False,
             "why": "The work is the mother's. The muscle of the uterus wall "
                    "is what does it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e16",
        "band": "easier",
        "text": "Where does the carbon dioxide in a foetus's blood come from?",
        "options": [
            {"text": "Respiration in its own cells, which goes on all the time",
             "correct": True},
            {"text": "Its lungs, which make it before birth", "correct": False,
             "why": "Lungs remove carbon dioxide rather than making it, and "
                    "the foetus's are not being used anyway."},
            {"text": "The mother's blood, crossing into it", "correct": False,
             "why": "It travels the other way. There is more of it in foetal "
                    "blood, so it crosses out to her."},
            {"text": "The amniotic fluid it swallows", "correct": False,
             "why": "Nothing dissolved in that fluid is a source of it. Every "
                    "cell that respires produces it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e17",
        "band": "easier",
        "text": "A foetus produces urea. What is it made from?",
        "options": [
            {"text": "Carbon dioxide left over from its own respiration",
             "correct": False,
             "why": "Carbon dioxide is a separate waste, and it leaves by the "
                    "same route without ever becoming urea."},
            {"text": "Surplus amino acids being broken down", "correct": True},
            {"text": "The mother's urea, crossing into it",
             "correct": False,
             "why": "Urea travels out of the foetus, not into it. It is made "
                    "on the foetal side and leaves across the placenta."},
            {"text": "Glucose it cannot store",
             "correct": False,
             "why": "Surplus glucose is respired or stored, not turned into "
                    "urea. Urea comes from protein, not from sugar."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e18",
        "band": "easier",
        "text": "What is an exchange surface?",
        "options": [
            {"text": "A surface that sorts useful substances from harmful ones",
             "correct": False,
             "why": "No surface in the body sorts anything. Substances move "
                    "wherever there is more of them than elsewhere."},
            {"text": "A surface that pumps substances from one side to the "
                     "other", "correct": False,
             "why": "Pumping needs muscle and an exchange surface has none. "
                    "Almost everything crossing one is diffusing."},
            {"text": "A surface built to move substances by diffusion",
             "correct": True},
            {"text": "A surface that keeps two bloods apart",
             "correct": False,
             "why": "Keeping them apart is a condition it works under, not the "
                    "job it does. The job is moving substances across."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e19",
        "band": "easier",
        "text": "In which direction does a substance diffuse?",
        "options": [
            {"text": "From where there is more of it to where there is less",
             "correct": True},
            {"text": "From where there is less of it to where there is more",
             "correct": False,
             "why": "That is diffusion backwards, and it does not happen on "
                    "its own. Going that way costs energy."},
            {"text": "From the mother's blood into the foetus's blood",
             "correct": False,
             "why": "Four of the six substances go that way and two go the "
                    "other, so direction cannot be the rule."},
            {"text": "Towards whichever side has the greater need of it",
             "correct": False,
             "why": "Need has no effect on a molecule. Only the difference in "
                    "concentration decides which way it moves."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e20",
        "band": "easier",
        "text": "A foetus cannot eat. In what form does the material for "
                "building its body arrive?",
        "options": [
            {"text": "As tiny pieces of food passed along the cord",
             "correct": False,
             "why": "Nothing that could be called food goes down the cord. It "
                    "carries blood, and only blood."},
            {"text": "As small molecules already dissolved in blood",
             "correct": True},
            {"text": "As a store the placenta built up in the first weeks",
             "correct": False,
             "why": "The placenta stores nothing. Everything crossing it "
                    "arrived in one of the two blood supplies first."},
            {"text": "As amniotic fluid, which the foetus swallows",
             "correct": False,
             "why": "It does swallow that fluid, but its building material "
                    "arrives dissolved in blood, at the placenta."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e21",
        "band": "easier",
        "text": "What shape does the placenta take as it grows into the wall of "
                "the uterus?",
        "options": [
            {"text": "It folds into thousands of finger-like projections",
             "correct": True},
            {"text": "It rolls into a long tube running to the foetus",
             "correct": False,
             "why": "The tube running to the foetus is the umbilical cord, "
                    "which is a separate structure from the placenta."},
            {"text": "It forms a smooth flat sheet against the wall",
             "correct": False,
             "why": "A flat sheet would waste most of the area available. The "
                    "folding is what makes the surface enormous."},
            {"text": "It builds a thick pad of muscle around the foetus",
             "correct": False,
             "why": "The muscle around the foetus is the wall of the uterus. "
                    "There is no muscle in the placenta at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e22",
        "band": "easier",
        "text": "What does a foetus do with the glucose that reaches it?",
        "options": [
            {"text": "Passes it back out again once it has been counted",
             "correct": False,
             "why": "Nothing counts anything. Glucose that arrives is used, "
                    "which is why the foetal concentration stays low."},
            {"text": "Turns it into urea to be removed by the mother",
             "correct": False,
             "why": "Urea comes from breaking down surplus amino acids. "
                    "Glucose is not made into it."},
            {"text": "Stores it in the amniotic fluid until it is needed",
             "correct": False,
             "why": "That fluid is not a store cupboard. Glucose arrives "
                    "dissolved in blood and is used from there."},
            {"text": "Respires it, and builds new tissue with it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e23",
        "band": "easier",
        "text": "What is the placenta attached to on the mother's side?",
        "options": [
            {"text": "The wall of the uterus", "correct": True},
            {"text": "The wall of the oviduct", "correct": False,
             "why": "The oviduct is where fertilisation happened, and the "
                    "pregnancy moved on from it within days."},
            {"text": "The inside of the cervix", "correct": False,
             "why": "The cervix is the closed opening at the base of the "
                    "uterus, and nothing is built onto it."},
            {"text": "One of her own lungs", "correct": False,
             "why": "Her lungs do remove the foetus's carbon dioxide, but they "
                    "do it through her blood, from a long way off."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e24",
        "band": "easier",
        "text": "How does a foetal heart compare with an adult heart in how "
                "hard it pushes blood?",
        "options": [
            {"text": "It pushes far harder, to reach the placenta",
             "correct": False,
             "why": "It is a much smaller heart moving a much smaller volume. "
                    "The pressure it produces is lower, not higher."},
            {"text": "It pushes blood far less hard", "correct": True},
            {"text": "It pushes exactly as hard as an adult heart",
             "correct": False,
             "why": "If the two pressures matched, mixing the circulations "
                    "would be harmless, and it is not."},
            {"text": "It does not push at all before birth", "correct": False,
             "why": "The foetal heart beats from very early on. Its blood has "
                    "to travel out to the placenta and back."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e25",
        "band": "easier",
        "text": "What is unusual about the placenta compared with every other "
                "organ a person has?",
        "options": [
            {"text": "It is the only organ with no blood supply of its own",
             "correct": False,
             "why": "It has blood on both sides of it, which is exactly what "
                    "keeps the concentration difference up."},
            {"text": "It is not made of cells",
             "correct": False,
             "why": "It is built of cells like any other tissue, and its cells "
                    "carry the embryo's chromosomes."},
            {"text": "It is built inside another organ",
             "correct": False,
             "why": "It grows into the wall of the uterus rather than inside "
                    "it, and that is not what makes it unusual."},
            {"text": "It is built, used, and then discarded", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e26",
        "band": "easier",
        "text": "What has happened to the lining of the uterus before a ball "
                "of cells implants in it?",
        "options": [
            {"text": "It has thickened", "correct": True},
            {"text": "It has been shed", "correct": False,
             "why": "Shedding the lining is what happens when no pregnancy "
                    "begins. Here it stays and is built up."},
            {"text": "It has hardened into muscle", "correct": False,
             "why": "The muscle is the wall of the uterus, outside the lining. "
                    "The lining itself stays soft."},
            {"text": "It has thinned to let cells through", "correct": False,
             "why": "Nothing passes through the lining. The ball of cells "
                    "embeds in it and stays there."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e27",
        "band": "easier",
        "text": "The growth and maturing stage runs from week 9 to week 40. "
                "How many weeks is that?",
        "options": [
            {"text": "About 40 weeks", "correct": False,
             "why": "Forty weeks is the whole dated pregnancy. This stage "
                    "starts nine weeks into it."},
            {"text": "About 49 weeks", "correct": False,
             "why": "The two numbers are added here instead of subtracted, "
                    "which gives a span longer than the pregnancy."},
            {"text": "About 31 weeks", "correct": True},
            {"text": "About 9 weeks", "correct": False,
             "why": "Nine weeks is where the stage begins, not how long it "
                    "lasts. It runs from there to the birth."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e28",
        "band": "easier",
        "text": "Which of these puts the stages of a pregnancy in order?",
        "options": [
            {"text": "Organs laid down, implantation, the exchange surface "
                     "built, growth, birth", "correct": False,
             "why": "Nothing can be laid down before the ball of cells has "
                    "embedded. Implantation comes first of all."},
            {"text": "Implantation, the exchange surface built, organs laid "
                     "down, growth, birth", "correct": True},
            {"text": "Implantation, organs laid down, growth, the exchange "
                     "surface built, birth", "correct": False,
             "why": "The supply line cannot be built last. Everything the "
                    "organs are made from crosses it first."},
            {"text": "The exchange surface built, implantation, organs laid "
                     "down, growth, birth", "correct": False,
             "why": "There is nothing to build a placenta onto until the ball "
                    "of cells has embedded in the lining."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e29",
        "band": "easier",
        "text": "Why is a baby born at 30 weeks usually lighter than one born "
                "at 40 weeks?",
        "options": [
            {"text": "It has had ten fewer weeks of growth", "correct": True},
            {"text": "Its organs never formed",
             "correct": False,
             "why": "Organs are laid down in the first eight weeks, so they "
                    "were all in place long before 30 weeks."},
            {"text": "Its placenta never finished",
             "correct": False,
             "why": "The placenta is built across weeks one to twelve and is "
                    "long finished by then."},
            {"text": "It stopped growing as soon as its lungs were ready",
             "correct": False,
             "why": "Nothing stops when the lungs mature. Growth carries on "
                    "right up to the birth."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-e30",
        "band": "easier",
        "text": "What is the developing organism called during the first eight "
                "weeks?",
        "options": [
            {"text": "A gamete", "correct": False,
             "why": "A gamete is a sex cell, and two of them fused to start "
                    "this off. What they made is not a gamete."},
            {"text": "A foetus", "correct": False,
             "why": "That word is used from about week nine, once the organs "
                    "exist and are growing rather than forming."},
            {"text": "An embryo", "correct": True},
            {"text": "A placenta", "correct": False,
             "why": "The placenta is the exchange surface being built beside "
                    "it, not the developing organism itself."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-04-s08",
        "band": "standard",
        "text": "Why does the barrier between the two blood supplies have to "
                "be so thin?",
        "options": [
            {"text": "So that the two bloods can be kept safely apart",
             "correct": False,
             "why": "A thicker barrier would keep them apart just as well. "
                    "Thinness is bought for speed, not for safety."},
            {"text": "So that the placenta weighs as little as it possibly can",
             "correct": False,
             "why": "Nothing about the placenta is built to save weight. It "
                    "grows to an enormous folded area quite deliberately."},
            {"text": "So that substances diffuse across fast enough to keep up",
             "correct": True},
            {"text": "So that the mother's blood can push through it more "
                     "easily", "correct": False,
             "why": "Her blood never goes through it. Only dissolved "
                    "substances cross, and they cross by diffusing."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s09",
        "band": "standard",
        "text": "A good exchange surface has a blood supply on both sides. "
                "What does that supply do?",
        "options": [
            {"text": "It pushes substances through the barrier, using the "
                     "pressure the heart puts behind it",
             "correct": False,
             "why": "Nothing is pushed across. Blood pressure moves blood "
                    "along a vessel, not molecules through a wall."},
            {"text": "It warms both sides, so that diffusion happens faster",
             "correct": False,
             "why": "Both sides are at body temperature anyway, and nothing on "
                    "this page turns on warming anything."},
            {"text": "It holds the two circulations a fixed distance apart",
             "correct": False,
             "why": "The tissue of the placenta does that. Flowing blood "
                    "cannot set the width of anything."},
            {"text": "It keeps bringing fresh blood, so the concentration "
                     "difference stays large", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s10",
        "band": "standard",
        "text": "A foetus at 30 weeks needs far more oxygen each minute than "
                "an embryo at 6 weeks. How does the placenta keep up?",
        "options": [
            {"text": "It has grown as well, so its surface area is far larger "
                     "by then", "correct": True},
            {"text": "It begins actively pumping oxygen once demand rises",
             "correct": False,
             "why": "There is no pump anywhere in it. Oxygen crosses by "
                    "diffusion at every stage of the pregnancy."},
            {"text": "Its barrier thins steadily as the pregnancy goes on",
             "correct": False,
             "why": "The barrier is thin from the start, which is what makes "
                    "it an exchange surface in the first place."},
            {"text": "The foetus starts using its own lungs to make up the "
                     "difference itself", "correct": False,
             "why": "The lungs are full of fluid until birth. Every scrap of "
                    "oxygen still crosses the placenta."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s11",
        "band": "standard",
        "text": "The placenta starts being built before any organ is laid "
                "down. Why does that order make sense?",
        "options": [
            {"text": "Because the placenta is the first organ a body makes",
             "correct": False,
             "why": "It is not the embryo's organ in that sense, and being "
                    "first in a list is not a reason for anything."},
            {"text": "Because the uterus lining would otherwise be shed",
             "correct": False,
             "why": "The lining is kept once implantation has happened, and "
                    "that is settled before any building starts."},
            {"text": "Because organs are built from what the supply line "
                     "delivers", "correct": True},
            {"text": "Because the embryo cannot survive without a heartbeat to "
                     "push its blood",
             "correct": False,
             "why": "The heart is one of the organs laid down later. It is not "
                    "what the placenta is waiting for."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s12",
        "band": "standard",
        "text": "A newborn's own immune system has met nothing and takes "
                "months to become useful. How is that gap covered?",
        "options": [
            {"text": "Its own immune system works fully from the moment it is "
                     "born",
             "correct": False,
             "why": "It does not. An immune system has to meet something "
                    "before it can respond to it quickly."},
            {"text": "The placenta goes on protecting it for the first few "
                     "months of life",
             "correct": False,
             "why": "The placenta is delivered minutes after the baby and does "
                    "nothing at all after that."},
            {"text": "Its mother's antibodies are destroyed and rebuilt by it",
             "correct": False,
             "why": "Nothing rebuilds them. They cross the placenta whole, and "
                    "they work as they are."},
            {"text": "It was stocked with its mother's antibodies before birth",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s13",
        "band": "standard",
        "text": "Why is the placenta delivered after the baby rather than "
                "before it?",
        "options": [
            {"text": "It is much heavier than the baby, so it always moves more "
                     "slowly",
             "correct": False,
             "why": "It is far lighter, and nothing about birth is a race "
                    "between two objects."},
            {"text": "Until the baby is born the placenta is still supplying "
                     "it", "correct": True},
            {"text": "It has to be delivered last so the cord can be cut",
             "correct": False,
             "why": "The cord is cut once the baby is out, while the placenta "
                    "is still attached inside."},
            {"text": "The cervix is not wide enough for it until afterwards",
             "correct": False,
             "why": "The cervix opens wide enough for a baby, so width is not "
                    "what settles the order."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s14",
        "band": "standard",
        "text": "A pregnancy is dated at 6 weeks. Which stage of development "
                "has it reached?",
        "options": [
            {"text": "Growth and maturing of organs that already exist",
             "correct": False,
             "why": "That stage begins at about week nine. At six weeks the "
                    "organs are still being formed."},
            {"text": "Implantation of the ball of cells in the lining",
             "correct": False,
             "why": "Implantation happens about five days after "
                    "fertilisation, which is weeks earlier than this."},
            {"text": "Organs are being laid down", "correct": True},
            {"text": "Birth, at the end of the forty weeks", "correct": False,
             "why": "Birth is around week forty. Six weeks in, the embryo is "
                    "smaller than a thumb."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s15",
        "band": "standard",
        "text": "A pregnancy is dated at 14 weeks. What is happening to the "
                "developing organism?",
        "options": [
            {"text": "Its heart, brain, spine and limbs are being formed",
             "correct": False,
             "why": "Those are laid down in weeks three to eight, and that "
                    "work is largely over by week nine."},
            {"text": "Its ball of cells is embedding in the uterus lining",
             "correct": False,
             "why": "Implantation is five days in. By fourteen weeks the "
                    "placenta is complete and the organs exist."},
            {"text": "Its placenta is only just beginning to be built",
             "correct": False,
             "why": "The placenta grows across weeks one to twelve, so it is "
                    "finished rather than starting."},
            {"text": "The organs it has are growing and maturing",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s16",
        "band": "standard",
        "text": "One stage of pregnancy runs weeks 1 to 12 and another runs "
                "weeks 3 to 8. Why do they overlap?",
        "options": [
            {"text": "The placenta is still growing while the organs are being "
                     "laid down", "correct": True},
            {"text": "One set of weeks is counted from fertilisation and the "
                     "other from the last period", "correct": False,
             "why": "Both stages are given on the same forty-week dating. The "
                    "overlap is real, not an artefact of counting."},
            {"text": "The stages are estimates, so their edges are not exact",
             "correct": False,
             "why": "Typical values do vary, but that is not why these two "
                    "sit inside one another. They genuinely run together."},
            {"text": "The organs are laid down twice, once in each stage",
             "correct": False,
             "why": "Nothing is built twice. Each organ is laid down once and "
                    "then grows for the rest of the pregnancy."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s17",
        "band": "standard",
        "text": "A foetus's lungs are full of fluid for the whole pregnancy. "
                "Why is that not a problem before birth?",
        "options": [
            {"text": "Because the amniotic fluid around it contains plenty of "
                     "dissolved oxygen",
             "correct": False,
             "why": "That fluid is not a source of oxygen, and a lung full of "
                    "liquid could not take any from it."},
            {"text": "Because the foetus needs no oxygen until it is born",
             "correct": False,
             "why": "It respires continuously, like any other organism, and "
                    "its demand only rises as it grows."},
            {"text": "Because its oxygen arrives dissolved in blood, from the "
                     "placenta", "correct": True},
            {"text": "Because the mother breathes down the umbilical cord on "
                     "its behalf instead", "correct": False,
             "why": "No air goes down the cord. It carries the foetus's own "
                    "blood out and back, and nothing else."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s18",
        "band": "standard",
        "text": "One reason the two circulations must stay separate is about "
                "pressure. What is it?",
        "options": [
            {"text": "Foetal blood is under such pressure that it would burst "
                     "her vessels", "correct": False,
             "why": "The pressure runs the other way. A foetal heart pushes "
                    "blood far less hard than an adult one."},
            {"text": "The pressure difference would stop anything crossing at "
                     "all", "correct": False,
             "why": "Crossing depends on the concentration difference, not on "
                    "pressure. Pressure would wreck the vessels instead."},
            {"text": "Blood at two different pressures cannot mix",
             "correct": False,
             "why": "It would mix perfectly well, and that is exactly the "
                    "danger. What is at stake is the damage done."},
            {"text": "An adult heart pushes far harder, and would destroy the "
                     "placenta's delicate vessels", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s19",
        "band": "standard",
        "text": "In some pregnancies the placenta grows smaller than usual. "
                "Predict the effect on the foetus, and say why.",
        "options": [
            {"text": "No effect, because substances cross at a fixed rate "
                     "whatever the area", "correct": False,
             "why": "The rate is not fixed. A smaller surface means less "
                    "crossing each minute."},
            {"text": "It grows more slowly, because less crosses each minute",
             "correct": True},
            {"text": "Its organs fail to form, because the supply line is "
                     "incomplete", "correct": False,
             "why": "Organs are laid down in the first eight weeks and need "
                    "very little. What suffers later is growth."},
            {"text": "It receives the same amount but takes longer to use it",
             "correct": False,
             "why": "Nothing arrives that has not crossed. A smaller surface "
                    "delivers less, not the same amount late."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s20",
        "band": "standard",
        "text": "A foetus respires, exactly like any other organism. What does "
                "that tell you it must receive and produce?",
        "options": [
            {"text": "It receives carbon dioxide and produces oxygen from it, "
                     "as a plant does",
             "correct": False,
             "why": "That is photosynthesis, and no animal does it. "
                    "Respiration runs the other way round."},
            {"text": "It receives urea and produces glucose", "correct": False,
             "why": "Urea is a waste it makes itself, and nothing in the body "
                    "produces glucose by respiring."},
            {"text": "It receives glucose and oxygen, and produces carbon "
                     "dioxide", "correct": True},
            {"text": "It receives oxygen and produces antibodies",
             "correct": False,
             "why": "Antibodies arrive from the mother across the placenta. "
                    "Respiration does not make them."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s21",
        "band": "standard",
        "text": "Blood keeps flowing through the umbilical cord all day and "
                "all night. Why does that flow matter at the placenta?",
        "options": [
            {"text": "It stirs the mother's blood on the other side of the "
                     "barrier, mixing the two", "correct": False,
             "why": "The two are never in contact, so one cannot stir the "
                    "other. Each side is kept moving by its own heart."},
            {"text": "It presses the two separate circulations closer together "
                     "against the wall",
             "correct": False,
             "why": "The distance between them is set by the tissue of the "
                    "placenta, not by how fast blood moves."},
            {"text": "It carries the placenta's own oxygen supply away",
             "correct": False,
             "why": "That would be a loss, not a benefit. What the flow "
                    "actually does is keep a difference in place."},
            {"text": "It keeps taking away what has crossed, so the difference "
                     "is not used up", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s22",
        "band": "standard",
        "text": "Why does the placenta have to grow into the wall of the "
                "uterus rather than sit loose inside it?",
        "options": [
            {"text": "That is where the mother's blood supply reaches it",
             "correct": True},
            {"text": "Otherwise the contractions of birth would begin early",
             "correct": False,
             "why": "Contractions are what deliver it at the end. They are not "
                    "held off by where it sits."},
            {"text": "Otherwise the foetus would have nothing to hold on to",
             "correct": False,
             "why": "The foetus floats in fluid and holds on to nothing. It is "
                    "joined to the placenta by the cord."},
            {"text": "Because the uterus wall supplies the muscle it uses",
             "correct": False,
             "why": "The placenta uses no muscle. Almost everything crossing "
                    "it is diffusing down a difference."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s23",
        "band": "standard",
        "text": "A foetus plainly needs oxygen. Explain why saying it breathes "
                "inside the uterus is still wrong.",
        "options": [
            {"text": "It needs far too little oxygen for breathing to be worth "
                     "it", "correct": False,
             "why": "Its demand is real and rises as it grows. The question is "
                    "not how much but by what route."},
            {"text": "Breathing would use up oxygen the mother needs herself",
             "correct": False,
             "why": "She supplies its oxygen either way. What rules breathing "
                    "out is that there is nowhere for it to happen."},
            {"text": "There is no air in the uterus, and its lungs are full of "
                     "fluid", "correct": True},
            {"text": "Breathing only begins once the umbilical cord is cut at "
                     "birth", "correct": False,
             "why": "That is true of the first breath, but it is the "
                    "consequence rather than the reason."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s24",
        "band": "standard",
        "text": "A mother and her baby often have different blood groups, and "
                "the pregnancy is safe. What makes that possible?",
        "options": [
            {"text": "Blood groups do not settle down until some months after a "
                     "baby is born", "correct": False,
             "why": "A baby's blood group is set at fertilisation, by the "
                    "chromosomes it received."},
            {"text": "The placenta converts her blood into the baby's own group "
                     "as it crosses",
             "correct": False,
             "why": "It converts nothing. It is a surface across which "
                    "dissolved substances diffuse."},
            {"text": "Incompatible blood only clots outside the body",
             "correct": False,
             "why": "It clots inside the body too, which is why a transfusion "
                    "of the wrong group is dangerous."},
            {"text": "The two bloods never meet — only dissolved substances "
                     "cross", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s25",
        "band": "standard",
        "text": "Why does urea have to be got out of a foetus at all?",
        "options": [
            {"text": "Because it would be used up by the placenta otherwise",
             "correct": False,
             "why": "The placenta uses none of it. Urea crosses and is carried "
                    "away in the mother's blood."},
            {"text": "Because it is toxic if it builds up", "correct": True},
            {"text": "Because the mother's kidneys would otherwise stop",
             "correct": False,
             "why": "Her kidneys work throughout, and they are what removes "
                    "the urea once it has crossed."},
            {"text": "Because it would make the amniotic fluid too thick",
             "correct": False,
             "why": "Thickness is not the danger. Urea has to leave the system "
                    "because of what it does at high concentration."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s26",
        "band": "standard",
        "text": "Why is a supply of antibodies worth the energy the placenta "
                "spends carrying them across?",
        "options": [
            {"text": "They break down waste the foetus cannot remove itself",
             "correct": False,
             "why": "Waste leaves by crossing the placenta. Antibodies act "
                    "against infection and do nothing to urea."},
            {"text": "They carry oxygen far more efficiently than adult "
                     "haemoglobin manages to", "correct": False,
             "why": "That is foetal haemoglobin, which is a different molecule "
                    "doing an entirely different job."},
            {"text": "A newborn meets infections long before it can make any "
                     "of its own", "correct": True},
            {"text": "They are needed as raw material to build the newborn's "
                     "own immune system",
             "correct": False,
             "why": "The baby builds its own by meeting infections. Borrowed "
                    "antibodies cover the months before that works."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s27",
        "band": "standard",
        "text": "Why is the placenta of no further use once a baby has been "
                "born?",
        "options": [
            {"text": "It has been used up by the substances crossing it",
             "correct": False,
             "why": "Nothing wears it out. It is discarded because there is no "
                    "longer anything for it to do."},
            {"text": "It stops working as soon as the cervix opens",
             "correct": False,
             "why": "It supplies the baby right up to the birth. The cervix "
                    "opening is not what ends its job."},
            {"text": "It is rejected by the mother's immune system at birth",
             "correct": False,
             "why": "It is normally not attacked at all, which is one of the "
                    "stranger unsolved problems in biology."},
            {"text": "The baby's own lungs, gut and kidneys now do the work",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s28",
        "band": "standard",
        "text": "Why does the lining of the uterus thicken before a ball of "
                "cells arrives?",
        "options": [
            {"text": "So there is something for it to embed in", "correct": True},
            {"text": "So the uterus can contract harder at the birth",
             "correct": False,
             "why": "Contractions come from the muscular wall outside the "
                    "lining, and they are forty weeks away."},
            {"text": "So the cervix is held closed for the whole pregnancy",
             "correct": False,
             "why": "The cervix is a separate structure at the base of the "
                    "uterus and is not part of the lining."},
            {"text": "So the amniotic fluid has somewhere to collect",
             "correct": False,
             "why": "That fluid gathers around the foetus once it is "
                    "developing, and not in the lining."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s29",
        "band": "standard",
        "text": "A student says the umbilical cord carries oxygen to the "
                "foetus as a gas. What is wrong with that?",
        "options": [
            {"text": "The cord carries no oxygen of any kind", "correct": False,
             "why": "It does carry oxygen. What is wrong is the form the "
                    "oxygen is imagined to be in."},
            {"text": "Oxygen reaches the foetus through the amniotic fluid "
                     "instead", "correct": False,
             "why": "Nothing useful crosses from that fluid. The route is the "
                    "placenta and then the cord."},
            {"text": "Oxygen travels dissolved in blood, carried by "
                     "haemoglobin", "correct": True},
            {"text": "Oxygen is made by the foetus rather than delivered to it",
             "correct": False,
             "why": "No animal makes oxygen. It is used up by respiration and "
                    "has to arrive from outside."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-s30",
        "band": "standard",
        "text": "A foetus never eats any protein, yet it produces urea. How "
                "can that be?",
        "options": [
            {"text": "Its urea is made by the placenta and passed across the "
                     "barrier into it",
             "correct": False,
             "why": "The placenta makes nothing. Urea is produced in the "
                    "foetus and crosses out from there."},
            {"text": "Urea is another name for the waste its lungs produce",
             "correct": False,
             "why": "The lungs deal with carbon dioxide, and they are not "
                    "being used. Urea is a different waste altogether."},
            {"text": "Its mother's urea crosses into it and is stored there "
                     "until the birth",
             "correct": False,
             "why": "Nothing is stored, and the traffic is the other way: "
                    "foetal urea crosses out into her blood."},
            {"text": "Amino acids cross the placenta, and the surplus is "
                     "broken down", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-04-h08",
        "band": "harder",
        "text": "Antibodies are large proteins and still reach the foetus, "
                "while most large molecules do not. What does that tell you "
                "about the placenta?",
        "options": [
            {"text": "That large molecules diffuse across it slowly rather "
                     "than not at all", "correct": False,
             "why": "Diffusion across a surface built for small molecules is "
                    "not merely slow for a large one. Time does not get a "
                    "protein across."},
            {"text": "That anything the foetus needs badly enough will find a "
                     "way across it", "correct": False,
             "why": "Need moves nothing. A molecule crosses because it can, "
                    "and antibodies can only because they are carried."},
            {"text": "That its barrier is thinner in some places than in "
                     "others", "correct": False,
             "why": "There is no thin patch for large molecules to use. What "
                    "gets antibodies across is a mechanism, not a gap."},
            {"text": "That crossing as a large molecule needs a mechanism, and "
                     "few have one", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h09",
        "band": "harder",
        "text": "A scan shows a foetus that has existed for about 18 weeks. "
                "Roughly how would the pregnancy be dated?",
        "options": [
            {"text": "About 20 weeks", "correct": True},
            {"text": "About 16 weeks", "correct": False,
             "why": "This takes the fortnight off when it should be added. "
                    "Dating starts before fertilisation, so the dated figure "
                    "is the larger of the two."},
            {"text": "About 18 weeks", "correct": False,
             "why": "That is the time since fertilisation. The dated pregnancy "
                    "is counted from about a fortnight earlier."},
            {"text": "About 22 weeks", "correct": False,
             "why": "Four weeks is twice the gap. Dating begins about two "
                    "weeks before fertilisation, not four."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h10",
        "band": "harder",
        "text": "Imagine a placenta whose barrier was twice as thick, with "
                "everything else unchanged. Predict the effect, and say why.",
        "options": [
            {"text": "No change, because the same substances would still be "
                     "able to cross it", "correct": False,
             "why": "Which substances can cross is not the only thing that "
                    "matters. How fast they cross is what a foetus lives on."},
            {"text": "Less would cross each minute, because diffusion across a "
                     "thicker barrier is slower", "correct": True},
            {"text": "More would cross, because there would be more tissue for "
                     "substances to move through", "correct": False,
             "why": "Extra tissue is extra distance, not extra route. It slows "
                    "diffusion rather than helping it."},
            {"text": "Nothing would cross at all, because diffusion needs a "
                     "barrier one cell thick", "correct": False,
             "why": "Thickness changes the rate, not whether it happens. "
                    "Diffusion does not switch off at some thickness."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h11",
        "band": "harder",
        "text": "In some mammals the two blood supplies run past each other in "
                "opposite directions at the placenta. Suggest why that gets "
                "more oxygen across.",
        "options": [
            {"text": "Because blood running the other way is under less "
                     "pressure, so it is easier to cross into", "correct": False,
             "why": "Pressure does not drive a substance across an exchange "
                    "surface. The concentration difference does."},
            {"text": "Because the two bloods touch briefly at the point where "
                     "they pass", "correct": False,
             "why": "They never touch, whichever way they run. Everything "
                    "crosses the tissue between them."},
            {"text": "Because the foetal blood is moving faster than the "
                     "mother's, so it collects more", "correct": False,
             "why": "Speed on its own collects nothing. What matters is "
                    "whether there is still a difference to diffuse down."},
            {"text": "Because a difference is kept up along the whole length "
                     "of the surface", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h12",
        "band": "harder",
        "text": "Two mechanisms are known that help the mother's immune system "
                "tolerate the placenta, and biologists still call the question "
                "open. What does that mean?",
        "options": [
            {"text": "That the two known mechanisms have both been shown to be "
                     "wrong", "correct": False,
             "why": "Both are real: unusual surface proteins on the outer "
                    "layer, and a locally quieter immune response in the "
                    "uterus."},
            {"text": "That no mechanism has ever been found and the whole "
                     "thing is guesswork", "correct": False,
             "why": "Two are known. What is unexplained is not whether "
                    "anything is happening but how far it goes."},
            {"text": "That how the known mechanisms add up to nine months of "
                     "tolerance is still unexplained", "correct": True},
            {"text": "That the placenta is attacked after all, and only "
                     "survives because it is replaced", "correct": False,
             "why": "It is normally not attacked, and nothing replaces it. "
                    "That is precisely what needs explaining."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h13",
        "band": "harder",
        "text": "A baby whose placenta was unusually small from week 12 is "
                "born light but with every organ present. Explain both halves "
                "of that.",
        "options": [
            {"text": "The organs were laid down before demand was high; growth "
                     "later needed a supply that was not there", "correct": True},
            {"text": "The organs were built from a store the embryo carried, "
                     "and the store was used up by week 12", "correct": False,
             "why": "There is no store. Everything an embryo is built from "
                    "crossed the placenta, week by week."},
            {"text": "The organs matter less than growth, so the body builds "
                     "them with whatever is left over", "correct": False,
             "why": "Nothing chooses an order of priority. The organs were "
                    "simply built at a stage when very little was needed."},
            {"text": "A small placenta affects only the last weeks, so the "
                     "whole loss happened after week 36", "correct": False,
             "why": "A supply that is short is short throughout. Growth across "
                    "the whole second half is what falls behind."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h14",
        "band": "harder",
        "text": "A foetus eats nothing, yet it needs glucose and amino acids "
                "continuously. Explain how both statements can be true.",
        "options": [
            {"text": "It swallows amniotic fluid, which is where its glucose "
                     "and amino acids come from", "correct": False,
             "why": "It does swallow that fluid, but its supply arrives "
                    "dissolved in blood, at the placenta."},
            {"text": "It receives them already dissolved in blood, at the end "
                     "of its mother's digestion", "correct": True},
            {"text": "It makes both of them itself, from the oxygen that "
                     "crosses the placenta", "correct": False,
             "why": "Oxygen is used in respiration and is not raw material for "
                    "sugars or proteins. Nothing is manufactured from it."},
            {"text": "It stores enough of both at implantation to last the "
                     "whole pregnancy", "correct": False,
             "why": "A ball of cells could not hold nine months of supply, and "
                    "nothing in the body works that way."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h15",
        "band": "harder",
        "text": "Compare two damaged placentas: one has half the surface area, "
                "the other a barrier twice as thick. What do they have in "
                "common?",
        "options": [
            {"text": "Both stop substances crossing altogether, so neither "
                     "pregnancy could continue at all", "correct": False,
             "why": "Neither stops crossing. Both reduce how much crosses in a "
                    "given time."},
            {"text": "Both change which substances can cross, so the foetus "
                     "receives a different set", "correct": False,
             "why": "The set does not change. Whatever is small and dissolved "
                    "still crosses, only more slowly."},
            {"text": "Both reduce the amount crossing each minute",
             "correct": True},
            {"text": "Both leave the rate unchanged, because diffusion depends "
                     "only on the difference", "correct": False,
             "why": "The difference is one factor of three. Area and thickness "
                    "are the other two, and both have moved."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h16",
        "band": "harder",
        "text": "Why does a baby's first breath have to work within moments of "
                "the cord being cut?",
        "options": [
            {"text": "Because the amniotic fluid has to be replaced by air at "
                     "once", "correct": False,
             "why": "Clearing the lungs is part of it, but the urgency is "
                    "about supply, not about the fluid itself."},
            {"text": "Because the placenta is delivered at the same moment as "
                     "the cord is cut", "correct": False,
             "why": "It follows a little later, and it is supplying nothing by "
                    "then anyway."},
            {"text": "Because a newborn's demand for oxygen is far higher than "
                     "a foetus's was", "correct": False,
             "why": "Demand rises, but the reason for the urgency is simpler: "
                    "there is suddenly no other route in."},
            {"text": "Because the only supply of oxygen it had has just been "
                     "removed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h17",
        "band": "harder",
        "text": "At the end of a birth the placenta is delivered and the "
                "uterus is not. What explains the difference?",
        "options": [
            {"text": "The uterus is far too large to be delivered through the "
                     "cervix", "correct": False,
             "why": "Size is not the point. The uterus is her own organ and is "
                    "not part of the pregnancy at all."},
            {"text": "The placenta grew with the pregnancy and is discarded "
                     "with it", "correct": True},
            {"text": "The uterus is rebuilt after every pregnancy, so it stays "
                     "in place", "correct": False,
             "why": "It shrinks back rather than being rebuilt, and it was "
                    "hers before the pregnancy began."},
            {"text": "The placenta is the mother's tissue, so her body can "
                     "afford to lose it", "correct": False,
             "why": "It is not her tissue. It grew from the same ball of cells "
                    "as the embryo and carries its chromosomes."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h18",
        "band": "harder",
        "text": "At 8 weeks a student says the organs are finished. How far is "
                "that right?",
        "options": [
            {"text": "Completely right: nothing changes in an organ after the "
                     "eighth week", "correct": False,
             "why": "A great deal changes. The lungs in particular are not "
                    "ready for many months after this."},
            {"text": "Completely wrong: no organ exists until about week "
                     "twelve", "correct": False,
             "why": "The heart, brain, spine and limbs are all laid down "
                    "within the first eight weeks."},
            {"text": "Right that they are laid down, wrong that they are "
                     "finished — they mature for 30 more weeks", "correct": True},
            {"text": "Right about the organs, wrong about the placenta, which "
                     "is finished at 8 weeks too", "correct": False,
             "why": "The placenta is built across weeks one to twelve, so at "
                    "eight weeks it is still growing."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h19",
        "band": "harder",
        "text": "Suppose the mother's blood stopped flowing past the placenta "
                "while everything else stayed as it was. Predict what would "
                "happen to the oxygen crossing.",
        "options": [
            {"text": "It would carry on unchanged, because diffusion needs no "
                     "blood flow", "correct": True},
            {"text": "It would slow and then stop, because the two "
                     "concentrations would come into balance", "correct": False,
             "why": "This is the outcome, and it is what the flow on each side "
                    "exists to prevent — but it is not what happens with the "
                    "flow intact."},
            {"text": "It would speed up, because still blood spends longer at "
                     "the surface", "correct": False,
             "why": "Longer at the surface only means the difference is used "
                    "up sooner. Time does not make more oxygen."},
            {"text": "It would reverse, and oxygen would cross back into her "
                     "blood", "correct": False,
             "why": "Reversal needs more on the foetal side, which never "
                    "happens for oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h20",
        "band": "harder",
        "text": "A baby born at 30 weeks is put on a machine that helps it "
                "breathe. Which stage was interrupted, and what is the machine "
                "standing in for?",
        "options": [
            {"text": "Implantation; the machine stands in for the uterus "
                     "lining", "correct": False,
             "why": "Implantation happened in the first week and has nothing "
                    "to do with breathing."},
            {"text": "The building of the exchange surface; the machine stands "
                     "in for the placenta", "correct": False,
             "why": "The placenta was complete by week twelve, and a "
                    "ventilator does not replace it — the baby's own lungs do."},
            {"text": "Growth and maturing; the machine does the work lungs "
                     "that are not finished cannot", "correct": True},
            {"text": "Organs being laid down; the machine replaces lungs that "
                     "were never formed", "correct": False,
             "why": "The lungs were laid down in the first eight weeks with "
                    "everything else. They were built but not yet ready."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h21",
        "band": "harder",
        "text": "Organs are laid down over weeks 3 to 8 of a 40-week dated "
                "pregnancy. What fraction of the pregnancy is that?",
        "options": [
            {"text": "About one fifth", "correct": False,
             "why": "One fifth of forty is eight weeks. The stage is six weeks "
                    "long, because it starts at week three, not week zero."},
            {"text": "About one seventh", "correct": True},
            {"text": "About one third", "correct": False,
             "why": "A third of forty weeks is over thirteen. Nothing like "
                    "that long is spent laying organs down."},
            {"text": "About one tenth", "correct": False,
             "why": "A tenth of forty weeks is four, which is the length of "
                    "the stage if it ran from week three to week seven, not "
                    "week eight. The stage is six weeks long, not four."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h22",
        "band": "harder",
        "text": "Keeping the two circulations separate protects both. Suggest "
                "one way it also costs the foetus something.",
        "options": [
            {"text": "It means the foetus has to build its own blood, which "
                     "uses material it could grow with", "correct": False,
             "why": "It would need its own blood whatever the arrangement. "
                    "Every organism circulates its own."},
            {"text": "It means everything has to cross a barrier, so nothing "
                     "arrives as fast as it could", "correct": True},
            {"text": "It means the foetus receives no antibodies, because "
                     "large molecules cannot cross", "correct": False,
             "why": "Antibodies do arrive — carried across deliberately, at a "
                    "cost in energy to the placenta."},
            {"text": "It means the two hearts have to beat at the same rate as "
                     "each other", "correct": False,
             "why": "They beat at quite different rates, and nothing about the "
                    "arrangement requires otherwise."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h23",
        "band": "harder",
        "text": "A student argues: the placenta carries antibodies across "
                "using energy, so it must carry oxygen across too. Where does "
                "that reasoning fail?",
        "options": [
            {"text": "Antibodies are not carried either — they diffuse like "
                     "everything else", "correct": False,
             "why": "They really are carried, at a cost in energy. That half "
                    "of the argument is sound."},
            {"text": "Oxygen is small enough to diffuse, so nothing has to "
                     "carry it", "correct": True},
            {"text": "Oxygen crosses in the opposite direction, so it cannot "
                     "use the same route", "correct": False,
             "why": "Oxygen crosses into the foetus, the same way antibodies "
                    "do. Direction is not where the argument breaks."},
            {"text": "The placenta has no energy to spend on two jobs at once",
             "correct": False,
             "why": "It has plenty of blood on both sides of it. The reason it "
                    "does not carry oxygen is that it need not."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h24",
        "band": "harder",
        "text": "An infection damages the placenta without ever reaching the "
                "foetus. Explain how the foetus could still be harmed.",
        "options": [
            {"text": "The damage would be repaired using material taken from "
                     "the foetus itself", "correct": False,
             "why": "Nothing is taken back across. The traffic in that "
                    "direction is carbon dioxide and urea."},
            {"text": "The foetus would catch the infection later, through the "
                     "amniotic fluid", "correct": False,
             "why": "The question sets aside anything reaching the foetus. "
                    "What is left is damage to the surface."},
            {"text": "A damaged exchange surface passes less of everything, so "
                     "supply falls", "correct": True},
            {"text": "Damaged tissue would begin to mix the two blood supplies "
                     "deliberately", "correct": False,
             "why": "Nothing does anything deliberately here, and mixing is "
                    "not what damage to a surface means."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h25",
        "band": "harder",
        "text": "A book says the placenta feeds the baby. Give the most "
                "accurate correction.",
        "options": [
            {"text": "Nothing is fed and nothing is chosen: dissolved "
                     "molecules diffuse across a surface", "correct": True},
            {"text": "It is the umbilical cord that feeds the baby, and the "
                     "placenta only holds it in place", "correct": False,
             "why": "The cord carries the foetus's own blood out and back. "
                    "Neither structure feeds anybody."},
            {"text": "It is the mother who feeds the baby, by sending her own "
                     "blood down the cord", "correct": False,
             "why": "Her blood never enters the foetus. The two circulations "
                    "are separate for the whole pregnancy."},
            {"text": "The placenta does feed the baby, but only until its own "
                     "gut starts working", "correct": False,
             "why": "The gut is not used before birth either. Everything "
                    "arrives dissolved in blood until then."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h26",
        "band": "harder",
        "text": "In a twin pregnancy two foetuses develop at once. Suggest one "
                "extra demand this places on the mother.",
        "options": [
            {"text": "Her heart has to beat at twice its usual rate to supply "
                     "them both", "correct": False,
             "why": "The rate does not double. What rises is the total demand "
                    "her body is meeting."},
            {"text": "Her lungs and kidneys are clearing the waste of three "
                     "individuals", "correct": True},
            {"text": "She has to produce two separate sets of antibodies, one "
                     "for each of them", "correct": False,
             "why": "The antibodies are the same ones. Each placenta carries "
                    "across a copy of what she already has."},
            {"text": "Her blood has to be divided between the two, so each "
                     "receives half of it", "correct": False,
             "why": "Her blood is not divided up, and none of it enters "
                    "either foetus. Only substances cross."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h27",
        "band": "harder",
        "text": "A student suggests a foetus could simply store its carbon "
                "dioxide until birth instead of passing it across. Evaluate "
                "that.",
        "options": [
            {"text": "It would work, because carbon dioxide is harmless until "
                     "it is breathed out", "correct": False,
             "why": "It is not harmless. It is a waste that the body removes "
                    "continuously for good reason."},
            {"text": "It would work, because the amniotic fluid could hold all "
                     "of it safely", "correct": False,
             "why": "That fluid is inside the system. Anything held there is "
                    "still inside the mother."},
            {"text": "It would fail, because respiration makes it continuously "
                     "and it would build up", "correct": True},
            {"text": "It would fail, because the foetus makes no carbon "
                     "dioxide before birth", "correct": False,
             "why": "It respires throughout, so it produces carbon dioxide "
                    "throughout. That is the whole problem."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h28",
        "band": "harder",
        "text": "Engineers building an artificial womb have to replace what "
                "the placenta does. Which pair of jobs is essential?",
        "options": [
            {"text": "Cushioning the foetus, and holding it in position",
             "correct": False,
             "why": "That is the amniotic fluid's part, and it keeps nothing "
                    "supplied."},
            {"text": "Supplying oxygen and glucose, and removing carbon "
                     "dioxide and urea", "correct": True},
            {"text": "Producing the contractions of birth, and opening the "
                     "cervix at the end", "correct": False,
             "why": "Those belong to the uterus at the very end. A foetus "
                    "would not survive nine months without a supply."},
            {"text": "Filtering out harmful substances, and choosing what the "
                     "foetus needs", "correct": False,
             "why": "The placenta does neither. It has no way of telling one "
                    "small dissolved molecule from another."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h29",
        "band": "harder",
        "text": "A baby's borrowed immunity fades after a few months. Suggest "
                "why it does not last longer.",
        "options": [
            {"text": "It was a stock of antibodies, and the baby cannot make "
                     "any more of them", "correct": True},
            {"text": "The antibodies are rejected once the baby's own immune "
                     "system starts up", "correct": False,
             "why": "Nothing rejects them. They are simply used up and not "
                    "replaced."},
            {"text": "They were destroyed by the first infection the baby met "
                     "after being born", "correct": False,
             "why": "Meeting an infection is what they are for. They fade "
                    "whether or not anything is met."},
            {"text": "They cross back into the mother once the cord has been "
                     "cut at the birth", "correct": False,
             "why": "Nothing crosses anywhere after the cord is cut. The two "
                    "are separated completely."},
        ],
        "figure": None,
    },
    {
        "id": "b5-04-h30",
        "band": "harder",
        "text": "A student writes: a mother and her foetus are one organism, "
                "because they share a blood supply. Give the two corrections "
                "needed.",
        "options": [
            {"text": "They are one organism until the birth, and they share a "
                     "circulation until the cord is cut", "correct": False,
             "why": "Neither half is right. They are two individuals, and "
                    "their circulations were never joined."},
            {"text": "They are two individuals, and they share a circulation "
                     "only at the placenta", "correct": False,
             "why": "The first half is right and the second is not. The two "
                    "circulations are separate at the placenta as well."},
            {"text": "They are two individuals, and nothing is shared — only "
                     "substances cross between them", "correct": True},
            {"text": "They are one organism, but the blood supply belongs to "
                     "the foetus rather than to her", "correct": False,
             "why": "There are two blood supplies, one each, and two "
                    "individuals. Both halves of this are wrong."},
        ],
        "figure": None,
    },
]
