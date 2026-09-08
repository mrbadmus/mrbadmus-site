"""C8 lesson 01 — Metals and non-metals: twelve questions (MRB-281).

The lesson's argument is one shape: metals and non-metals differ on a SET of
properties, every one of those properties has an exception somewhere, and so a
classification is made on the pattern rather than on a single test. The page
teaches it by handing the student six unlabelled samples, three of which break
a rule and are still what they are.

These twelve probe the angles the mastery ladder leaves alone: what a single
property does and does not license, which of the exceptions is which, and what
happens when the properties are put to work choosing a material.

The distractors are built from the lesson's two declared misconceptions.

`PTAB-01` (if it conducts electricity it must be a metal) drives the wrong
options in e02, s01, s04 and h01. Each treats one property as a decision.
s04 is the one that matters: it gives the student a sample that conducts AND
shatters, so the belief has to be weighed against a second observation rather
than merely asserted.

`PTAB-02` (a liquid element cannot be a metal) drives e04, s02 and h03, where
state of matter is read as though it settled the question. h03 puts it the
other way round — a solid that is not a metal — because the belief is really
about state deciding class, and it runs in both directions.

A third strand, on the page and in neither register entry, is that "shiny"
survives being a bad test: e03 and h04 are built on it, because a freshly cut
sodium surface is a mirror for four seconds and a polished non-metal can look
like a metal for as long as you like.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS. `easier`, `standard`, `harder` — never the
letters. Five banks shipped with the short form and forty questions were
silently unreachable from any assignment, because `questions_for()` filters on
equality with the full word and a bank of `"s"` matches nothing.

Every question here is new prose, and the bar is §13's: each distractor is a
WRONG RULE in the correct answer's own shape, at the correct answer's own
length, and each is a mistake a real student actually makes.
"""

UNIT = "C8"
LESSON = "metals-and-non-metals"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c8-01-e01",
        "band": "easier",
        "text": "Which list gives four properties that are typical of "
                "metals?",
        "options": [
            {"text": "Shiny, malleable, good conductor, high melting point",
             "correct": True},
            {"text": "Dull, brittle, poor conductor, low melting point",
             "correct": False,
             "why": "That is the non-metal list — every item is the opposite "
                    "of the metal one."},
            {"text": "Shiny, brittle, poor conductor, high melting point",
             "correct": False,
             "why": "Brittle and insulating are non-metal properties. A list "
                    "that mixes the two describes nothing."},
            {"text": "Dull, malleable, good conductor, low melting point",
             "correct": False,
             "why": "Metals are shiny on a fresh surface. Sodium looks dull "
                    "only because it has already reacted with the air."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e02",
        "band": "easier",
        "text": "A solid element is dull, shatters when hit, and does not "
                "conduct electricity. What is it?",
        "options": [
            {"text": "A metal, because all solid elements are metals",
             "correct": False,
             "why": "Sulfur, carbon and phosphorus are all solid non-metals. "
                    "Being solid settles nothing."},
            {"text": "A non-metal, because all three properties point the "
                     "same way",
             "correct": True},
            {"text": "A metal, because only metals are ever tested this way",
             "correct": False,
             "why": "The same three tests are used on any element. The tests "
                    "do not know what they are testing."},
            {"text": "Impossible to say, because no test can classify an "
                     "element",
             "correct": False,
             "why": "One property is a clue; three agreeing properties is an "
                    "identification. That is the whole method."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e03",
        "band": "easier",
        "text": "Why is a saucepan made of metal and its handle made of "
                "plastic or wood?",
        "options": [
            {"text": "Metal is cheaper than plastic, and the handle is the "
                     "expensive part",
             "correct": False,
             "why": "Cost is not the reason. A metal handle would be cheap "
                    "and unusable."},
            {"text": "Metal is heavier, which stops the pan sliding on the "
                     "hob",
             "correct": False,
             "why": "Weight has nothing to do with it. The pan has to pass "
                    "heat to the food."},
            {"text": "Metal conducts heat well and the non-metal handle does "
                     "not",
             "correct": True},
            {"text": "Metal is shinier, which reflects the heat back into the "
                     "food",
             "correct": False,
             "why": "The pan does not reflect the heat, it conducts it. A "
                    "shiny plastic pan would still melt."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e04",
        "band": "easier",
        "text": "Mercury is a liquid at room temperature. What does that tell "
                "you about whether it is a metal?",
        "options": [
            {"text": "It cannot be a metal, because every metal is a solid",
             "correct": False,
             "why": "Mercury IS a metal — shiny, conducting, and freezing at "
                    "−39 °C. It is the exception the rule needs."},
            {"text": "It cannot be an element, because elements are solids or "
                     "gases",
             "correct": False,
             "why": "Mercury and bromine are both elements and both are "
                    "liquid at room temperature."},
            {"text": "It must be a metal, because only a metal could be that "
                     "shiny",
             "correct": False,
             "why": "It is a metal, but shine did not prove it. A polished "
                    "non-metal can look like a mirror too."},
            {"text": "Nothing on its own — its other properties have to be "
                     "checked",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c8-01-s01",
        "band": "standard",
        "text": "A student says “graphite conducts electricity, so carbon "
                "must be a metal.” What is wrong with the argument?",
        "options": [
            {"text": "Conducting is one property, and carbon fails every "
                     "other metal test",
             "correct": True},
            {"text": "Graphite does not really conduct — the meter was faulty",
             "correct": False,
             "why": "Graphite genuinely conducts, about as well as some "
                    "metals. That is what makes it the awkward case."},
            {"text": "Graphite is a compound, so it is not carbon at all",
             "correct": False,
             "why": "Graphite is a form of the element carbon. There is "
                    "nothing else in it."},
            {"text": "Carbon is a metal, so the argument is actually correct",
             "correct": False,
             "why": "Carbon is one of the most thoroughly non-metallic "
                    "elements there is: dull, brittle, and its oxide is "
                    "acidic."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s02",
        "band": "standard",
        "text": "An unknown element is a dark red liquid that does not "
                "conduct electricity. What is the best conclusion?",
        "options": [
            {"text": "It is a metal, because liquids flow and metals are "
                     "flexible",
             "correct": False,
             "why": "Flowing is not malleability, and a metal that did not "
                    "conduct would be the first one ever found."},
            {"text": "It is a non-metal, because it does not conduct and is "
                     "not shiny",
             "correct": True},
            {"text": "It is a metal, because mercury is a liquid metal too",
             "correct": False,
             "why": "Mercury is silvery and conducts. This sample matches it "
                    "on neither count — it is bromine."},
            {"text": "It cannot be classified, because there is no liquid "
                     "category",
             "correct": False,
             "why": "There is no liquid category, which is exactly why you "
                    "judge on the other properties instead."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s03",
        "band": "standard",
        "text": "Sodium can be cut with a knife and floats on water. Why does "
                "that not stop it being a metal?",
        "options": [
            {"text": "Because softness and floating are not on the list of "
                     "metal properties",
             "correct": False,
             "why": "Hardness and density are typical of metals. Sodium is a "
                    "genuine exception to both, not a case the list ignores."},
            {"text": "Because sodium is only a metal once it has reacted with "
                     "water",
             "correct": False,
             "why": "It is a metal before, during and after. Reacting does "
                    "not change what an element is."},
            {"text": "Because it is shiny when cut, conducts, and its other "
                     "properties are metallic",
             "correct": True},
            {"text": "Because every metal floats if the piece is small enough",
             "correct": False,
             "why": "Iron does not float at any size. Sodium floats because "
                    "it is genuinely less dense than water."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s04",
        "band": "standard",
        "text": "A sample conducts electricity and shatters into flakes when "
                "it is hit. Which single further test would settle it fastest?",
        "options": [
            {"text": "Weigh it, because metals are always denser than "
                     "non-metals",
             "correct": False,
             "why": "Sodium and lithium both float on water. Density does not "
                    "sort the two classes cleanly."},
            {"text": "Test it again for conduction, because the first result "
                     "may be wrong",
             "correct": False,
             "why": "Repeating a test you already trust adds nothing. You "
                    "need a DIFFERENT property."},
            {"text": "Warm it gently, because every non-metal melts below "
                     "100 °C",
             "correct": False,
             "why": "Carbon does not melt below 3000 °C. Low melting point is "
                    "typical of non-metals, not universal."},
            {"text": "Look at a freshly broken surface for metallic shine",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c8-01-h01",
        "band": "harder",
        "text": "Silicon is shiny, brittle, and conducts electricity a little "
                "under some conditions. Why is it not simply classed as a "
                "metal?",
        "options": [
            {"text": "Because it sits on the staircase and matches neither "
                     "list fully",
             "correct": True},
            {"text": "Because a metal must conduct at every temperature "
                     "without exception",
             "correct": False,
             "why": "That is not the rule, and inventing it would exclude "
                    "several genuine metals at low temperature."},
            {"text": "Because it is a compound rather than an element",
             "correct": False,
             "why": "Silicon is an element. Sand is the compound."},
            {"text": "Because shine is the only property that ever counts",
             "correct": False,
             "why": "Shine is the least reliable of the properties, which is "
                    "why the lesson never lets it decide anything alone."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h02",
        "band": "harder",
        "text": "Overhead power cables are aluminium wound around a steel "
                "core. What does each material contribute?",
        "options": [
            {"text": "The aluminium insulates the cable and the steel carries "
                     "the current",
             "correct": False,
             "why": "Aluminium is a conductor, not an insulator. Both metals "
                    "conduct; the roles are the other way round."},
            {"text": "The aluminium carries the current and the steel carries "
                     "the weight",
             "correct": True},
            {"text": "The steel makes the cable shiny and the aluminium makes "
                     "it heavy",
             "correct": False,
             "why": "Neither appearance nor weight is wanted. Aluminium was "
                    "chosen because it is LIGHT."},
            {"text": "The aluminium melts at high current and protects the "
                     "steel",
             "correct": False,
             "why": "A cable that melts in normal use is a failed cable. "
                    "Aluminium's melting point of 660 °C is never reached."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h03",
        "band": "harder",
        "text": "A student writes: “Iodine is a solid at room temperature, so "
                "it must be a metal.” Explain the flaw in the same terms the "
                "student used.",
        "options": [
            {"text": "Iodine is a liquid, so the premise is wrong before the "
                     "reasoning starts",
             "correct": False,
             "why": "Iodine really is a grey-black solid. The premise is "
                    "right; it is the inference that fails."},
            {"text": "Solids are all non-metals, so the conclusion is exactly "
                     "backwards",
             "correct": False,
             "why": "Most metals are solids. Solidity points weakly towards "
                    "metal, which is why the argument is tempting."},
            {"text": "Being a solid is a property most metals share and some "
                     "non-metals share too",
             "correct": True},
            {"text": "Iodine is a compound, so it cannot be classified as "
                     "either",
             "correct": False,
             "why": "Iodine is an element. It is a solid non-metal, which is "
                    "the case the student's rule cannot accommodate."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h04",
        "band": "harder",
        "text": "Why is “is it shiny?” the least reliable of the tests in "
                "this lesson?",
        "options": [
            {"text": "Because shine cannot be measured with any instrument at "
                     "all",
             "correct": False,
             "why": "Reflectivity is measurable. The problem is not "
                    "measurement, it is what the measurement means."},
            {"text": "Because only freshly cut metals are shiny and "
                     "non-metals never are",
             "correct": False,
             "why": "If that were true it would be a perfect test. Polished "
                    "graphite and iodine crystals both shine."},
            {"text": "Because shine has nothing to do with conducting "
                     "electricity",
             "correct": False,
             "why": "True but irrelevant — none of the tests measures the "
                    "same thing as another. That is why several are used."},
            {"text": "Because a metal dulls in air within seconds and some "
                     "non-metals shine",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-01-e05",
        "band": "easier",
        "text": "What does malleable mean?",
        "options": [
            {"text": "Able to be hammered or bent into a new shape without "
                     "breaking",
             "correct": True},
            {"text": "Able to be melted at a low enough temperature that an "
                     "ordinary Bunsen burner will pour it out of a crucible",
             "correct": False,
             "why": "That is about melting point. Malleable is about "
                    "reshaping a solid"},
            {"text": "Able to be pulled out into a long thin wire without it "
                     "snapping part way along",
             "correct": False,
             "why": "Very close, and that word is ductile. Malleable is about "
                    "hammering rather than drawing"},
            {"text": "Able to carry an electric current from one end of the "
                     "sample right through to the other",
             "correct": False,
             "why": "That is conducting, and it is a separate property"},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e06",
        "band": "easier",
        "text": "What does sonorous mean, and why does it matter for a bell?",
        "options": [
            {"text": "It bends without snapping, so a bell survives being "
                     "struck over and over again for a hundred years without "
                     "cracking",
             "correct": False,
             "why": "That is malleable. Sonorous is about the note, not the "
                    "survival"},
            {"text": "It rings with a clear note when struck",
             "correct": True},
            {"text": "It conducts sound faster than air does",
             "correct": False,
             "why": "Most solids do that. Sonorous is about the ringing "
                    "itself"},
            {"text": "It is heavy enough to swing",
             "correct": False,
             "why": "Mass is not the property. A wooden bell of the same "
                    "weight still thuds"},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e07",
        "band": "easier",
        "text": "Roughly what share of the elements are metals?",
        "options": [
            {"text": "About a quarter",
             "correct": False,
             "why": "That is nearer the share of NON-metals — about twenty of "
                    "them out of a hundred"},
            {"text": "About half",
             "correct": False,
             "why": "Metals are the clear majority. The non-metals are a "
                    "short list"},
            {"text": "About three-quarters",
             "correct": True},
            {"text": "Nearly all of them, with only three or four non-metals "
                     "on the whole of the table",
             "correct": False,
             "why": "There are about twenty non-metals, and life is built out "
                    "of them"},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e08",
        "band": "easier",
        "text": "Which of these is a non-metal?",
        "options": [
            {"text": "Mercury, which is unusual enough to be liquid at room "
                     "temperature and so cannot be a metal at all",
             "correct": False,
             "why": "Mercury is a metal, and a liquid one. Being liquid rules "
                    "nothing out"},
            {"text": "Sodium",
             "correct": False,
             "why": "Soft and light, and still a metal — shiny when cut, and "
                    "it conducts"},
            {"text": "Zinc",
             "correct": False,
             "why": "A hard grey metal, and one of the transition block"},
            {"text": "Sulfur",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c8-01-s05",
        "band": "standard",
        "text": "Mercury and bromine are both liquids at room temperature and "
                "one is a metal. Which single test separates them?",
        "options": [
            {"text": "See whether it conducts electricity",
             "correct": True},
            {"text": "Weigh equal volumes of each — the metal is always the "
                     "denser of any two liquids you are asked to compare",
             "correct": False,
             "why": "Mercury is denser here, and density is not a reliable "
                    "divider. Several non-metals beat several metals"},
            {"text": "See which one evaporates first",
             "correct": False,
             "why": "Bromine does evaporate readily, and boiling point is not "
                    "one of the deciding properties"},
            {"text": "Look at the colour",
             "correct": False,
             "why": "Bromine is dark red and mercury silver, and colour is "
                    "the least reliable test in this lesson"},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s06",
        "band": "standard",
        "text": "Non-metals are described as brittle WHEN SOLID. Why is that "
                "qualification there?",
        "options": [
            {"text": "Because a non-metal that has been cooled far enough "
                     "stops being brittle and starts to bend like a metal "
                     "instead",
             "correct": False,
             "why": "Cooling makes things more brittle rather than less. The "
                    "qualification is about state"},
            {"text": "Because many non-metals are gases or liquids at room "
                     "temperature, and brittleness only applies to solids",
             "correct": True},
            {"text": "Because a non-metal is only brittle if it is pure",
             "correct": False,
             "why": "Purity does not change it. Sulfur shatters whether it is "
                    "pure or not"},
            {"text": "Because some non-metals are malleable",
             "correct": False,
             "why": "Solid non-metals shatter — that is the point of the "
                    "test. The qualification is about the ones that are not "
                    "solid"},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s07",
        "band": "standard",
        "text": "Which of these would you NOT expect of a typical non-metal?",
        "options": [
            {"text": "A dull surface",
             "correct": False,
             "why": "Dullness is on the non-metal list, so this is expected"},
            {"text": "Shattering when it is hit",
             "correct": False,
             "why": "Brittle is on the list. This is exactly what a solid "
                    "non-metal does"},
            {"text": "A high melting point",
             "correct": True},
            {"text": "Failing to carry a current in a simple circuit made up "
                     "of a battery, a bulb and two crocodile clips",
             "correct": False,
             "why": "Poor conduction is on the list, and graphite is the one "
                    "well-known exception to it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s08",
        "band": "standard",
        "text": "Why does this lesson insist that an element is judged on the "
                "whole set of properties rather than on one test?",
        "options": [
            {"text": "Because a single test can be carried out wrongly, and "
                     "running several of them is a way of checking that no "
                     "mistake has been made",
             "correct": False,
             "why": "Careful work is good and it is not the reason. Even a "
                    "perfectly performed single test can point the wrong "
                    "way"},
            {"text": "Because the tests take very little time each",
             "correct": False,
             "why": "Convenience is not a reason for a rule. The reason is "
                    "that one result can mislead"},
            {"text": "Because the periodic table has to be consulted as well",
             "correct": False,
             "why": "The table would settle it at once. The point is about "
                    "judging from properties"},
            {"text": "Because every single property has exceptions",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-01-h05",
        "band": "harder",
        "text": "In a metal the outer electrons move freely through the whole "
                "structure rather than staying with one atom. Which pair of "
                "properties does that ONE idea explain?",
        "options": [
            {"text": "Conducting electricity, and bending instead of "
                     "shattering",
             "correct": True},
            {"text": "Being shiny, and having a high density, since a "
                     "structure with electrons running through it has to be "
                     "packed more tightly than one without",
             "correct": False,
             "why": "Density comes from how the atoms pack rather than from "
                    "the electrons. Two of the five properties are cleaner "
                    "than that"},
            {"text": "Being solid at room temperature, and being heavy for the "
                     "size of it",
             "correct": False,
             "why": "Mercury is neither, and it is a metal. Neither follows "
                    "from free electrons"},
            {"text": "Being unreactive, and resisting attack by acids at room "
                     "temperature",
             "correct": False,
             "why": "Sodium is a metal and does neither. Reactivity comes "
                    "from a different part of the story"},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h06",
        "band": "harder",
        "text": "Silicon conducts, but only a little and only under some "
                "conditions. Why is that halfway behaviour so useful?",
        "options": [
            {"text": "Because it conducts just enough to carry a signal "
                     "without ever getting hot, which is the problem that "
                     "stops metals being used inside a chip",
             "correct": False,
             "why": "Chips do get hot, and heat is a major engineering "
                    "problem. What matters is the switching"},
            {"text": "Because it can be persuaded to conduct or not, which is "
                     "what a computer needs",
             "correct": True},
            {"text": "Because it is cheaper than copper",
             "correct": False,
             "why": "Cost helps and it is not the reason. A cheap conductor "
                    "would just be a conductor"},
            {"text": "Because it is brittle, so it can be cut into the very "
                     "thin wafers that a chip is built on",
             "correct": False,
             "why": "Wafers are cut, and brittleness is not what makes "
                    "silicon special. The switching is"},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h07",
        "band": "harder",
        "text": "Diamond is a non-metal and conducts HEAT better than any "
                "metal does. What should a student do with that fact?",
        "options": [
            {"text": "Reclassify diamond as a metal, since conducting heat "
                     "well is one of the properties on the metal list and "
                     "diamond does it better than anything else",
             "correct": False,
             "why": "One property never decides it. Diamond fails every other "
                    "metal test"},
            {"text": "Conclude that the metal and non-metal lists are useless "
                     "and ought to be abandoned",
             "correct": False,
             "why": "The lists work for almost everything. Exceptions are why "
                    "the pattern is judged as a whole"},
            {"text": "Treat it as one more exception, and judge diamond on "
                     "the whole pattern",
             "correct": True},
            {"text": "Conclude that diamond is not really carbon",
             "correct": False,
             "why": "It is carbon, and so is graphite — which conducts "
                    "electricity. Both are exceptions worth knowing"},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h08",
        "band": "harder",
        "text": "Copper conducts electricity better than aluminium, and "
                "overhead power lines are aluminium. What is the trade-off?",
        "options": [
            {"text": "Aluminium conducts better once it is cold, and a cable "
                     "strung high in the open air is cold for most of the "
                     "year in this country",
             "correct": False,
             "why": "Copper is the better conductor at any temperature. The "
                    "reason is weight and cost"},
            {"text": "Copper is a transition metal and so cannot be drawn out "
                     "into a wire long enough to span two pylons",
             "correct": False,
             "why": "Copper wire is the most familiar wire there is. It draws "
                    "beautifully"},
            {"text": "Aluminium is stronger, so it needs no steel core",
             "correct": False,
             "why": "It is weaker, which is exactly why the cable is wound "
                    "around a steel core"},
            {"text": "Aluminium is far lighter, so a span can be longer and "
                     "the pylons can be further apart",
             "correct": True},
        ],
        "figure": None,
    },
]
