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
    {
        "id": "c8-01-e09",
        "band": "easier",
        "text": "What does it mean to say a metal is ductile?",
        "options": [
            {"text": "It can be drawn out into a long thin wire",
             "correct": True},
            {"text": "It rings with a clear note when it is struck",
             "correct": False,
             "why": "That is sonorous. Ductile is about being pulled out into "
                    "a wire."},
            {"text": "It shatters into pieces when it is hammered",
             "correct": False,
             "why": "That is brittle, and it describes non-metal solids "
                    "rather than metals."},
            {"text": "It lets heat pass through it very quickly",
             "correct": False,
             "why": "That describes a good conductor of heat. Ductility is "
                    "about shape, not temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e10",
        "band": "easier",
        "text": "A material is described as brittle. What does that tell "
                "you about how it behaves?",
        "options": [
            {"text": "It can be hammered into a new shape without breaking "
                     "apart or cracking",
             "correct": False,
             "why": "That is malleable, and it is one of the metal "
                    "properties."},
            {"text": "It carries heat away quickly from whatever touches it",
             "correct": False,
             "why": "That describes a good conductor of heat. Brittleness is "
                    "about how a solid breaks."},
            {"text": "It shatters or cracks when it is hit, instead of "
                     "changing shape",
             "correct": True},
            {"text": "It floats on water instead of sinking to the bottom",
             "correct": False,
             "why": "Floating is about density. A dense material can still "
                    "be brittle."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e11",
        "band": "easier",
        "text": "What is an insulator?",
        "options": [
            {"text": "A material that lets electricity pass through it easily",
             "correct": False,
             "why": "That is a conductor. An insulator is the opposite."},
            {"text": "A material that does not let electricity pass through it",
             "correct": True},
            {"text": "A material that is shiny when it is freshly polished",
             "correct": False,
             "why": "Shine is about how a surface looks. An insulator is "
                    "defined by what it does to a current."},
            {"text": "A material that melts at a very high temperature",
             "correct": False,
             "why": "Melting point says nothing about whether a current can "
                    "pass through."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e12",
        "band": "easier",
        "text": "An element is described as lustrous. What does that mean?",
        "options": [
            {"text": "It can be bent into a new shape without breaking",
             "correct": False,
             "why": "That is malleable. Lustrous is only about how the "
                    "surface looks."},
            {"text": "It shatters into small pieces when it is dropped",
             "correct": False,
             "why": "That is brittle, and lustrous says nothing about how a "
                    "material breaks."},
            {"text": "It feels cold when you first pick it up",
             "correct": False,
             "why": "That is a sign of good heat conduction, not of lustre."},
            {"text": "It has a bright, shiny surface",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e13",
        "band": "easier",
        "text": "What does the density of a material tell you?",
        "options": [
            {"text": "How much mass is packed into a given volume",
             "correct": True},
            {"text": "How hot it has to get before it melts",
             "correct": False,
             "why": "That is its melting point, which is a separate "
                    "measurement."},
            {"text": "How well it carries an electric current",
             "correct": False,
             "why": "That is conductivity. Density is about mass and volume "
                    "only."},
            {"text": "How hard the surface is to scratch with a steel point",
             "correct": False,
             "why": "That is hardness. Lead is very dense and scratches "
                    "with a fingernail."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e14",
        "band": "easier",
        "text": "What is an alloy?",
        "options": [
            {"text": "An element that sits on the line between metals and "
                     "non-metals",
             "correct": False,
             "why": "That is a metalloid. An alloy is a mixture rather than "
                    "a single element."},
            {"text": "A metal mixed with one or more other elements",
             "correct": True},
            {"text": "A metal that has been heated until it melts",
             "correct": False,
             "why": "Melting a metal does not change what it is made of. An "
                    "alloy has something added."},
            {"text": "A non-metal that conducts electricity",
             "correct": False,
             "why": "Graphite fits that description exactly and it is not an "
                    "alloy."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e15",
        "band": "easier",
        "text": "What is a metalloid?",
        "options": [
            {"text": "A metal that has been mixed with a non-metal to harden "
                     "it",
             "correct": False,
             "why": "That is an alloy. A metalloid is a single element, not "
                    "a mixture."},
            {"text": "A metal that is liquid at room temperature",
             "correct": False,
             "why": "That describes mercury, which is an ordinary metal in "
                    "every other way."},
            {"text": "An element with some metal and some non-metal "
                     "properties",
             "correct": True},
            {"text": "A non-metal that has a high melting point",
             "correct": False,
             "why": "Carbon has a very high melting point and is simply a "
                    "non-metal."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e16",
        "band": "easier",
        "text": "What is a semiconductor?",
        "options": [
            {"text": "A material that conducts only once it has been melted",
             "correct": False,
             "why": "Melting is not what the word means. Silicon chips work "
                    "as cold solids."},
            {"text": "A material that conducts heat but never electricity",
             "correct": False,
             "why": "That describes diamond. A semiconductor is named for "
                    "its electrical behaviour."},
            {"text": "A material that conducts electricity better than copper "
                     "does at every temperature",
             "correct": False,
             "why": "Nothing beats the best metals. A semiconductor conducts "
                    "far less well than copper."},
            {"text": "A material that conducts electricity a little, and only "
                     "under some conditions",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e17",
        "band": "easier",
        "text": "Apart from hydrogen, whereabouts in the periodic table are "
                "the non-metals found?",
        "options": [
            {"text": "Together on the right-hand side",
             "correct": True},
            {"text": "Together on the left-hand side and in the middle block",
             "correct": False,
             "why": "That side of the table is the metals' side, and it holds "
                    "no non-metals at all."},
            {"text": "In a single column at the far left of the table",
             "correct": False,
             "why": "The far-left column is group 1, and every element in it "
                    "is a soft, reactive metal."},
            {"text": "Scattered evenly through every group in the table",
             "correct": False,
             "why": "They are not scattered about. The non-metals sit "
                    "together in one corner of the table."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e18",
        "band": "easier",
        "text": "The filament in an old-style light bulb glows at about "
                "2500 °C. Which property of tungsten makes it the right "
                "metal for that job?",
        "options": [
            {"text": "It is the least dense metal, so the filament cannot sag",
             "correct": False,
             "why": "Tungsten is one of the densest metals there is. Density "
                    "is not the reason."},
            {"text": "It melts at 3422 °C, so it stays solid at that "
                     "temperature",
             "correct": True},
            {"text": "It is the only metal that conducts while it is hot",
             "correct": False,
             "why": "Every metal conducts electricity when it is hot. "
                    "Tungsten is not special there."},
            {"text": "It is brittle, so the thin filament keeps its shape",
             "correct": False,
             "why": "Tungsten is a metal and is not brittle the way a "
                    "non-metal solid is."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e19",
        "band": "easier",
        "text": "Why is copper used for the wires inside a plug?",
        "options": [
            {"text": "It is the densest metal there is and holds the wire in "
                     "place",
             "correct": False,
             "why": "A wire is not chosen for its weight, and copper is "
                    "nowhere near the densest metal."},
            {"text": "It is brittle and snaps cleanly if the wire is "
                     "overloaded",
             "correct": False,
             "why": "Copper is not brittle, and a wire that snapped easily "
                    "would be useless."},
            {"text": "It conducts electricity very well and draws into wire",
             "correct": True},
            {"text": "It does not conduct and keeps the plug safe to hold",
             "correct": False,
             "why": "Copper conducts extremely well. The plastic around it "
                    "is what makes a plug safe."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e20",
        "band": "easier",
        "text": "Drinks cans and aircraft bodies are both made from "
                "aluminium. Which property is the main reason?",
        "options": [
            {"text": "It has the highest melting point of any metal",
             "correct": False,
             "why": "Tungsten melts far higher, and a drinks can never gets "
                    "anywhere near melting."},
            {"text": "It is brittle, so a can crumples instead of bending "
                     "out of shape",
             "correct": False,
             "why": "Aluminium is malleable, which is why a can can be "
                    "pressed into shape at all."},
            {"text": "It does not conduct electricity at all",
             "correct": False,
             "why": "Aluminium conducts well enough to be used in overhead "
                    "power cables."},
            {"text": "It has a low density for a metal, so it is light for "
                     "its size",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e21",
        "band": "easier",
        "text": "An element is a gas at room temperature. What can you say "
                "about it?",
        "options": [
            {"text": "It is a non-metal, because no metal is a gas at room "
                     "temperature",
             "correct": True},
            {"text": "It is a metal, because a gas is always made of "
                     "unusually light atoms",
             "correct": False,
             "why": "How heavy the atoms are does not decide the class, and "
                    "every gas here is a non-metal."},
            {"text": "Nothing at all, because a gas cannot be classified",
             "correct": False,
             "why": "Gases are classified like anything else. Nitrogen and "
                    "oxygen are both non-metals."},
            {"text": "It is a metalloid, because metalloids are in between",
             "correct": False,
             "why": "Metalloids are solids. Being in between is about "
                    "properties, not about state."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e22",
        "band": "easier",
        "text": "A gold ring taken from a 3000-year-old grave is still "
                "bright and shiny. Which metal property is that?",
        "options": [
            {"text": "It is ductile, so it can be pulled into a thin wire",
             "correct": False,
             "why": "Ductility is about drawing wire, not about a surface "
                    "staying bright."},
            {"text": "It is lustrous, so the surface stays shiny",
             "correct": True},
            {"text": "It is sonorous, so it rings when it is struck",
             "correct": False,
             "why": "Sonorous describes the sound a metal makes, not how it "
                    "looks."},
            {"text": "It is dense, so it feels heavy for its size",
             "correct": False,
             "why": "Density is about mass and volume, and says nothing "
                    "about shine."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e23",
        "band": "easier",
        "text": "Iodine is a grey-black solid that crumbles to powder under "
                "a light tap. Which non-metal property does the crumbling "
                "show?",
        "options": [
            {"text": "That it is a poor conductor of electricity and heat",
             "correct": False,
             "why": "Conduction is tested with a circuit or a hot plate, not "
                    "with a tap from a hammer."},
            {"text": "That it has a low density compared with a metal",
             "correct": False,
             "why": "Density is found by weighing a known volume, not by "
                    "breaking a sample."},
            {"text": "That it is brittle, as non-metal solids are",
             "correct": True},
            {"text": "That it melts at a fairly low temperature",
             "correct": False,
             "why": "Melting point is measured by heating, and crumbling "
                    "tells you nothing about it."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e24",
        "band": "easier",
        "text": "A block of zinc is hit hard with a hammer. What would you "
                "expect to happen?",
        "options": [
            {"text": "It gives off a gas and slowly disappears",
             "correct": False,
             "why": "Hitting a metal does not make it react. Nothing is "
                    "given off."},
            {"text": "It shatters into small sharp pieces",
             "correct": False,
             "why": "That is what a non-metal solid does under a hammer. "
                    "Zinc is a metal."},
            {"text": "It stops conducting electricity afterwards",
             "correct": False,
             "why": "Changing the shape of a metal does not change whether "
                    "it conducts."},
            {"text": "It changes shape and stays in one piece",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e25",
        "band": "easier",
        "text": "Which of these non-metals is a solid at room temperature?",
        "options": [
            {"text": "Sulfur", "correct": True},
            {"text": "Oxygen", "correct": False,
             "why": "Oxygen is a gas and makes up about a fifth of the air "
                    "in the room."},
            {"text": "Helium", "correct": False,
             "why": "Helium is a gas, which is why a balloon filled with it "
                    "rises."},
            {"text": "Chlorine", "correct": False,
             "why": "Chlorine is a green gas at room temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e26",
        "band": "easier",
        "text": "Silicon is used to make computer chips. How is silicon "
                "classified?",
        "options": [
            {"text": "As a metal, because it is shiny",
             "correct": False,
             "why": "Shine alone never settles it, and silicon is brittle "
                    "and conducts only weakly."},
            {"text": "As a metalloid, with properties of both metals and "
                     "non-metals",
             "correct": True},
            {"text": "As a non-metal, because it has none of the metal "
                     "properties at all",
             "correct": False,
             "why": "Silicon is shiny and does conduct a little, so it is "
                    "not purely non-metallic."},
            {"text": "As an alloy of a metal and a non-metal",
             "correct": False,
             "why": "Silicon is an element. An alloy is a mixture of more "
                    "than one element."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e27",
        "band": "easier",
        "text": "Iron melts at 1538 °C and oxygen boils at −183 °C. Which of "
                "the two has the melting point you would expect of a metal?",
        "options": [
            {"text": "Oxygen, because metals are always gases",
             "correct": False,
             "why": "No metal is a gas at room temperature. Oxygen is a "
                    "non-metal."},
            {"text": "Neither, because every element melts at the same "
                     "temperature",
             "correct": False,
             "why": "Melting points differ enormously from one element to "
                    "the next."},
            {"text": "Iron, because metals usually have high melting points",
             "correct": True},
            {"text": "Both, because 1538 °C and −183 °C are both high "
                     "figures",
             "correct": False,
             "why": "−183 °C is far below room temperature. The two figures "
                    "are nothing alike."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e28",
        "band": "easier",
        "text": "Four blocks of the same size are stood on a hot plate. "
                "Which one will carry the heat through fastest?",
        "options": [
            {"text": "The wooden block", "correct": False,
             "why": "Wood insulates, which is why spoons and pan handles are "
                    "made of it."},
            {"text": "The plastic block", "correct": False,
             "why": "Plastic is an insulator. It is wrapped round wires to "
                    "keep heat and current in."},
            {"text": "The rubber block", "correct": False,
             "why": "Rubber is chosen as an insulator, never as a way of "
                    "moving heat."},
            {"text": "The copper block", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e29",
        "band": "easier",
        "text": "What is a conductor?",
        "options": [
            {"text": "A material that lets heat or electricity pass through "
                     "it easily",
             "correct": True},
            {"text": "A material that is always a shiny silver colour",
             "correct": False,
             "why": "Graphite is dull and black and conducts electricity "
                    "perfectly well."},
            {"text": "A material that never melts, whatever the temperature",
             "correct": False,
             "why": "Every conductor melts if it gets hot enough. Copper "
                    "melts at 1085 °C."},
            {"text": "A material that has to be a pure element rather than "
                     "any kind of mixture",
             "correct": False,
             "why": "Steel and brass are both mixtures and both conduct "
                    "extremely well."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e30",
        "band": "easier",
        "text": "Lead has a density of 11.3 g/cm³ and aluminium 2.7 g/cm³. "
                "A block of each is cut to exactly the same size. What "
                "follows?",
        "options": [
            {"text": "The aluminium block has the greater mass",
             "correct": False,
             "why": "Aluminium has the smaller density, so the same volume "
                    "of it has less mass."},
            {"text": "The lead block has the greater mass",
             "correct": True},
            {"text": "The two blocks have exactly the same mass",
             "correct": False,
             "why": "Equal volumes only have equal masses when the densities "
                    "match, and these do not."},
            {"text": "The masses cannot be compared without melting both",
             "correct": False,
             "why": "Density and volume are enough on their own. Melting "
                    "would not help at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e31",
        "band": "easier",
        "text": "Which of these lists contains only non-metals?",
        "options": [
            {"text": "Copper, sulfur, oxygen", "correct": False,
             "why": "Copper is a metal, and it is the one used for "
                    "electrical wiring."},
            {"text": "Carbon, iron, helium", "correct": False,
             "why": "Iron is a metal. It rings when struck and bends before "
                    "it breaks."},
            {"text": "Carbon, sulfur, oxygen", "correct": True},
            {"text": "Zinc, oxygen, carbon", "correct": False,
             "why": "Zinc is a metal, used to coat steel and to make "
                    "brass."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-e32",
        "band": "easier",
        "text": "Mercury melts at −39 °C. Is mercury solid or liquid in a "
                "room at 20 °C?",
        "options": [
            {"text": "Solid, because −39 °C is above room temperature",
             "correct": False,
             "why": "−39 °C is well below 20 °C. The minus sign means colder "
                    "than freezing water."},
            {"text": "Solid, because every metal is solid at room "
                     "temperature",
             "correct": False,
             "why": "Mercury is the one metal that is not, and its melting "
                    "point is the reason."},
            {"text": "It depends on how much mercury is in the room",
             "correct": False,
             "why": "Melting point does not depend on the amount. A drop and "
                    "a bottle melt together."},
            {"text": "Liquid, because the room is well above its melting "
                     "point",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s09",
        "band": "standard",
        "text": "Gold never corrodes and conducts electricity well, yet the "
                "wiring in a house is copper. Why?",
        "options": [
            {"text": "Copper is far cheaper and plentiful, and conducts "
                     "almost as well",
             "correct": True},
            {"text": "Copper is the only metal that can be drawn into a wire",
             "correct": False,
             "why": "Gold is the most ductile metal of all and draws into "
                    "finer wire than copper does."},
            {"text": "Gold is a non-metal, so it cannot be used in a circuit",
             "correct": False,
             "why": "Gold is a metal — shiny, malleable and conducting. It "
                    "is simply expensive."},
            {"text": "Gold stops conducting once it has been bent to shape",
             "correct": False,
             "why": "Bending a metal does not stop it conducting. Gold wire "
                    "works perfectly well."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s10",
        "band": "standard",
        "text": "A door handle of pure copper dents easily, so brass — "
                "copper mixed with zinc — is used instead. What does mixing "
                "the two metals do?",
        "options": [
            {"text": "It removes the copper's colour, so a brass handle no "
                     "longer looks metallic",
             "correct": False,
             "why": "Brass is bright yellow and looks thoroughly metallic. "
                    "Colour is not the reason."},
            {"text": "It makes the metal harder, because the added atoms "
                     "stop the layers sliding",
             "correct": True},
            {"text": "It turns the copper into a non-metal, which is why "
                     "brass does not conduct",
             "correct": False,
             "why": "Brass conducts heat and electricity perfectly well and "
                    "is still a metal."},
            {"text": "It lowers the melting point so far that brass would "
                     "melt in hot water",
             "correct": False,
             "why": "Brass melts at about 930 °C. Nothing a door handle ever "
                    "meets comes close."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s11",
        "band": "standard",
        "text": "A saucepan base is often a sandwich of aluminium between "
                "two layers of stainless steel. Aluminium carries heat much "
                "better than steel, and steel is harder. What is the design "
                "achieving?",
        "options": [
            {"text": "It makes the pan lighter than one made of either metal "
                     "on its own",
             "correct": False,
             "why": "A sandwich of both is thicker and heavier than a plain "
                    "steel base, not lighter."},
            {"text": "It spreads the heat evenly and keeps a tough surface "
                     "for the food",
             "correct": True},
            {"text": "It stops the pan conducting heat, so the base stays "
                     "cool on the hob",
             "correct": False,
             "why": "A base that did not carry heat would cook nothing. "
                    "Carrying heat is the whole job."},
            {"text": "It turns the steel into an alloy of aluminium and iron "
                     "as it heats up",
             "correct": False,
             "why": "Layers stacked together are not an alloy. Nothing is "
                    "mixed at the level of the atoms."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s12",
        "band": "standard",
        "text": "A strip of copper bends when it is hit and a stick of "
                "sulfur snaps in two. Explain the difference.",
        "options": [
            {"text": "Copper atoms are much smaller, so they fit round the "
                     "bend",
             "correct": False,
             "why": "Atom size does not decide it, and sulfur atoms are not "
                    "unusually large."},
            {"text": "Sulfur is colder inside than copper, and cold things "
                     "always snap",
             "correct": False,
             "why": "Both sit at room temperature, and temperature is not "
                    "what makes a solid brittle."},
            {"text": "The copper was melted and reset at the factory and the "
                     "sulfur was not",
             "correct": False,
             "why": "How a sample was made does not change whether the "
                    "element is malleable."},
            {"text": "In copper the layers of atoms slide and stay bonded; "
                     "in sulfur they cannot",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s13",
        "band": "standard",
        "text": "An element melts at −219 °C and boils at −183 °C. What do "
                "those two figures suggest about its class?",
        "options": [
            {"text": "A non-metal, because those are far below anything a "
                     "metal melts at",
             "correct": True},
            {"text": "A metal, because those are the sort of melting points "
                     "metals have",
             "correct": False,
             "why": "Metals melt high. Iron melts at 1538 °C and tungsten "
                    "higher still."},
            {"text": "A metal, because only a metal can be measured that "
                     "precisely",
             "correct": False,
             "why": "Any element's melting point can be measured. The "
                    "thermometer does not care what it is in."},
            {"text": "Nothing at all, because melting point never helps a "
                     "classification",
             "correct": False,
             "why": "Melting point is one of the six properties, and here it "
                    "separates the classes cleanly."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s14",
        "band": "standard",
        "text": "Aluminium has a density of 2.7 g/cm³ and lead 11.3 g/cm³. "
                "A racing bicycle frame is aluminium and a diver's weight "
                "belt is lead. Explain both choices.",
        "options": [
            {"text": "Aluminium conducts heat and lead does not, so the "
                     "frame stays cool",
             "correct": False,
             "why": "Both conduct heat. Neither choice has anything to do "
                    "with temperature."},
            {"text": "The frame has to be light and the belt has to be heavy "
                     "for its size",
             "correct": True},
            {"text": "Lead is the only metal dense enough to sink, and "
                     "aluminium floats",
             "correct": False,
             "why": "Aluminium is nearly three times as dense as water and "
                    "sinks in it easily."},
            {"text": "Aluminium is brittle and lead is malleable, which "
                     "suits each of the jobs",
             "correct": False,
             "why": "Aluminium is malleable, which is why it can be drawn "
                    "into tubing for a frame."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s15",
        "band": "standard",
        "text": "Steel is iron with a little carbon in it, and carbon is a "
                "non-metal. Steel still conducts electricity and can be bent "
                "and welded. What does that show?",
        "options": [
            {"text": "That adding carbon turns the iron into a non-metal, "
                     "but only slowly",
             "correct": False,
             "why": "Steel behaves as a metal in every test. Nothing about "
                    "it has become non-metallic."},
            {"text": "That steel must contain no carbon at all, since it "
                     "still conducts",
             "correct": False,
             "why": "Steel does contain carbon, usually well under one per "
                    "cent, and still conducts."},
            {"text": "That an alloy keeps the metal properties of the metal "
                     "it is mostly made of",
             "correct": True},
            {"text": "That carbon must really be a metal, since it is in "
                     "steel",
             "correct": False,
             "why": "Carbon is a non-metal. Being mixed into a metal does "
                    "not change what it is."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s16",
        "band": "standard",
        "text": "A student says: “Wood is brittle and does not conduct "
                "electricity, so wood is a non-metal.” What is wrong with "
                "that?",
        "options": [
            {"text": "Wood does conduct electricity, so the first fact is "
                     "the wrong way round",
             "correct": False,
             "why": "Dry wood is a good insulator. The properties given are "
                    "right; the reasoning is not."},
            {"text": "Brittleness is a metal property, so the first fact "
                     "points the wrong way",
             "correct": False,
             "why": "Brittle and insulating are both non-metal properties, so "
                    "the properties named are right. The fault is in what is "
                    "being classified."},
            {"text": "Nothing is wrong at all, because wood passes the "
                     "non-metal test twice over",
             "correct": False,
             "why": "The tests sort ELEMENTS. Wood is not an element and "
                    "belongs to neither class."},
            {"text": "Metal and non-metal are labels for elements, and wood "
                     "is not an element",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s17",
        "band": "standard",
        "text": "A light-bulb filament runs at about 2500 °C. Copper melts "
                "at 1085 °C. Why is copper the wrong metal for a filament?",
        "options": [
            {"text": "Because copper would melt long before 2500 °C was "
                     "reached",
             "correct": True},
            {"text": "Because copper stops conducting electricity once it is "
                     "glowing hot",
             "correct": False,
             "why": "Copper conducts when it is hot. It would simply have "
                    "melted first."},
            {"text": "Because copper is too expensive to use in a filament "
                     "that thin",
             "correct": False,
             "why": "A filament uses a scrap of metal. Cost is not what "
                    "rules copper out."},
            {"text": "Because copper is a non-metal and cannot carry a "
                     "current at all",
             "correct": False,
             "why": "Copper is a metal and the best everyday conductor there "
                    "is."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s18",
        "band": "standard",
        "text": "Gold leaf can be beaten to 0.0001 mm thick, and gold can be "
                "drawn into wire thinner than a human hair. Which two metal "
                "properties are being used?",
        "options": [
            {"text": "Sonorous and lustrous", "correct": False,
             "why": "Those describe the sound and the shine, not what "
                    "happens when gold is worked."},
            {"text": "Malleable and ductile", "correct": True},
            {"text": "Brittle and dense", "correct": False,
             "why": "Brittle would mean it shattered under the hammer, and "
                    "gold does not."},
            {"text": "Conducting and insulating", "correct": False,
             "why": "No material is both, and neither has anything to do "
                    "with shaping gold."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s19",
        "band": "standard",
        "text": "Boron and arsenic sit on the same staircase line of the "
                "periodic table as silicon. What would you expect of them?",
        "options": [
            {"text": "That both behave exactly like sodium does, since they "
                     "are all metals",
             "correct": False,
             "why": "Sodium sits well inside the metal side. Being on the "
                    "line is the whole point."},
            {"text": "That both are gases, since the line runs near the "
                     "right-hand edge",
             "correct": False,
             "why": "All three of these elements are solids at room "
                    "temperature."},
            {"text": "That both show some metal and some non-metal "
                     "properties",
             "correct": True},
            {"text": "That both conduct electricity better than copper does "
                     "at any temperature",
             "correct": False,
             "why": "Copper is one of the best conductors there is. Nothing "
                    "on that line beats it."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s20",
        "band": "standard",
        "text": "Most of the elements in the periodic table are metals, yet "
                "almost all of a human body is built from non-metals. Is "
                "that a contradiction?",
        "options": [
            {"text": "Yes, because most elements are metals so most matter "
                     "has to be metal",
             "correct": False,
             "why": "How many KINDS there are says nothing about how much of "
                    "each one exists."},
            {"text": "Yes, because a body would have to be built from the "
                     "commonest elements",
             "correct": False,
             "why": "Commonness in the table and commonness in a body are "
                    "two different counts."},
            {"text": "No, because every metal is poisonous and could not be "
                     "in a living body",
             "correct": False,
             "why": "Iron and calcium are metals and a body needs both of "
                    "them to work."},
            {"text": "No, because counting kinds of element is not the same "
                     "as counting mass",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s21",
        "band": "standard",
        "text": "A student says: “Aluminium is light and helium is light, so "
                "helium must be a metal.” What is wrong with that?",
        "options": [
            {"text": "Being light is not a metal property, and helium fails "
                     "every other metal test",
             "correct": True},
            {"text": "Nothing is wrong, because an element that is light for "
                     "its size is always a metal",
             "correct": False,
             "why": "Hydrogen and helium are the lightest elements there "
                    "are, and both are non-metals."},
            {"text": "Aluminium is not light, so the comparison fails before "
                     "it starts",
             "correct": False,
             "why": "Aluminium is genuinely light for a metal, at "
                    "2.7 g/cm³. The fault lies elsewhere."},
            {"text": "Helium is a metal, but only once it has been cooled "
                     "into a liquid",
             "correct": False,
             "why": "Cooling an element does not change its class. Liquid "
                    "helium is still a non-metal."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s22",
        "band": "standard",
        "text": "A metal spoon and a wooden spoon have been in the same "
                "drawer all night. The metal one feels colder. Why?",
        "options": [
            {"text": "The metal really is colder and wood holds its warmth "
                     "overnight",
             "correct": False,
             "why": "Both have been in the same drawer all night and are at "
                    "the same temperature."},
            {"text": "Metal carries heat out of your hand quickly and wood "
                     "does not",
             "correct": True},
            {"text": "Metal is denser, and a denser object always sits at a "
                     "lower temperature",
             "correct": False,
             "why": "Density has no effect on temperature. A dense object in "
                    "a warm room is warm."},
            {"text": "The wood gives out heat of its own, which is why it "
                     "feels warm",
             "correct": False,
             "why": "Wood makes no heat. It simply does not carry your "
                    "hand's heat away."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s23",
        "band": "standard",
        "text": "A mains cable is copper wire inside a plastic sleeve. "
                "Explain the choice of each of the two materials.",
        "options": [
            {"text": "Copper is cheap and plastic is expensive, and that is "
                     "the whole reason",
             "correct": False,
             "why": "Cost is not the point. A cheap conductor with no sleeve "
                    "would still be lethal."},
            {"text": "The plastic carries the current and the copper keeps "
                     "the heat in",
             "correct": False,
             "why": "It is the other way round entirely. Plastic is an "
                    "insulator."},
            {"text": "Copper carries the current and plastic stops it "
                     "escaping",
             "correct": True},
            {"text": "Both of them conduct, and two conductors carry more "
                     "current than one",
             "correct": False,
             "why": "Plastic does not conduct at all, which is exactly why "
                    "it is on the outside."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s24",
        "band": "standard",
        "text": "Graphite is soft enough to mark paper and is also used as "
                "an electrode to carry a current. What do those two uses "
                "show?",
        "options": [
            {"text": "That graphite is a metal, since only a metal can "
                     "carry a current at all",
             "correct": False,
             "why": "Graphite is carbon, a non-metal. It is the exception "
                    "that breaks that rule."},
            {"text": "That graphite has been mixed with a metal to make it "
                     "conduct at all",
             "correct": False,
             "why": "Pencil graphite is carbon and conducts on its own, with "
                    "nothing added."},
            {"text": "That a soft material can never be an electrical "
                     "conductor",
             "correct": False,
             "why": "The question itself gives the counter-example. Softness "
                    "and conduction are separate."},
            {"text": "That a non-metal can conduct electricity and still be "
                     "a non-metal",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s25",
        "band": "standard",
        "text": "A bar of iron gives a long musical note when it is hit "
                "with a hammer; a lump of sulfur gives a dull thud and "
                "cracks. Which property is that, and which sample shows it?",
        "options": [
            {"text": "Sonorous — the iron shows it and the sulfur does not",
             "correct": True},
            {"text": "Ductile — the iron shows it, and ringing is what "
                     "ductile means",
             "correct": False,
             "why": "Ductile means it can be drawn into a wire. It has "
                    "nothing to do with sound."},
            {"text": "Sonorous — the sulfur shows it and the iron does not",
             "correct": False,
             "why": "It is the iron that rings. The sulfur thuds and cracks, "
                    "as a non-metal solid does."},
            {"text": "Malleable — the sulfur shows it, which is why it "
                     "cracks",
             "correct": False,
             "why": "Cracking is brittleness, which is the opposite of "
                    "malleable."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s26",
        "band": "standard",
        "text": "An unknown element has a density of 19.3 g/cm³, melts at "
                "1064 °C, conducts electricity and can be beaten into thin "
                "sheets. Metal or non-metal?",
        "options": [
            {"text": "Non-metal, because only a non-metal can be beaten into "
                     "thin sheets",
             "correct": False,
             "why": "Non-metal solids shatter under a hammer. Beating into "
                    "sheets is a metal property."},
            {"text": "Metal, because all four measurements point the same "
                     "way",
             "correct": True},
            {"text": "Impossible to say, because four properties are never "
                     "enough to decide",
             "correct": False,
             "why": "Four agreeing properties is exactly what a confident "
                    "identification looks like."},
            {"text": "Non-metal, because 1064 °C is too low a melting point "
                     "for any metal",
             "correct": False,
             "why": "Tin melts at 232 °C and is a metal. 1064 °C is a high "
                    "melting point, not a low one."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s27",
        "band": "standard",
        "text": "Tin melts at 232 °C, which is far lower than the melting "
                "point of carbon, a non-metal. Does that stop tin being a "
                "metal?",
        "options": [
            {"text": "Yes, because a metal has to melt higher than every "
                     "single non-metal does",
             "correct": False,
             "why": "Carbon melts far higher than tin and is a non-metal. The "
                    "two ranges overlap."},
            {"text": "Yes, because every metal melts somewhere above "
                     "1000 °C",
             "correct": False,
             "why": "Sodium melts at 98 °C and mercury at −39 °C, and both "
                    "of them are metals."},
            {"text": "No, because tin is shiny, malleable and conducting, so "
                     "the pattern says metal",
             "correct": True},
            {"text": "No, because melting point is not a property of an "
                     "element at all",
             "correct": False,
             "why": "Melting point is a property of every element, and it is "
                    "one of the six tested here."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s28",
        "band": "standard",
        "text": "A student is told only that an element sits near the middle "
                "of the right-hand edge of the periodic table. What can they "
                "predict about it?",
        "options": [
            {"text": "That it is probably a metal — shiny, malleable and "
                     "conducting",
             "correct": False,
             "why": "The metals are on the left and in the middle. The "
                    "right-hand edge is non-metals."},
            {"text": "That it is probably a liquid — one of the two that sit "
                     "at the table's edges",
             "correct": False,
             "why": "Position does not set the state, and only two elements "
                    "are liquid at room temperature."},
            {"text": "Nothing at all — a position on the table predicts "
                     "nothing",
             "correct": False,
             "why": "Position is precisely what predicts the class. That is "
                    "why the table is arranged as it is."},
            {"text": "That it is probably a non-metal — dull, brittle if "
                     "solid, and insulating",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s29",
        "band": "standard",
        "text": "A copper roof that was bright when it was new is now dull "
                "green. A student says it has stopped being a metal. Are "
                "they right?",
        "options": [
            {"text": "No, because the dullness is only the surface and the "
                     "other properties are unchanged",
             "correct": True},
            {"text": "Yes, because staying bright and shiny for ever is "
                     "the one property that every metal must have",
             "correct": False,
             "why": "Shine is the least reliable of the tests. A tarnished "
                    "metal is still a metal."},
            {"text": "Yes, because an element that changes colour has become "
                     "a non-metal",
             "correct": False,
             "why": "A colour change does not move an element between "
                    "classes. It is still copper."},
            {"text": "No, because copper cannot change colour at all",
             "correct": False,
             "why": "It plainly does — old copper roofs are green. The "
                    "colour is a surface layer."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s30",
        "band": "standard",
        "text": "Zinc melts at 420 °C with a density of 7.1 g/cm³; sulfur "
                "melts at 115 °C with a density of 2.1 g/cm³. Which set of "
                "figures points to a metal?",
        "options": [
            {"text": "Sulfur's — a low density is what a metal usually shows",
             "correct": False,
             "why": "Metals are usually dense. 2.1 g/cm³ is low and points "
                    "to a non-metal."},
            {"text": "Zinc's — the higher melting point and the higher "
                     "density both fit a metal",
             "correct": True},
            {"text": "Neither set — melting point and density are the same for "
                     "every solid",
             "correct": False,
             "why": "They differ hugely between elements, which is why they "
                    "are worth measuring."},
            {"text": "Both sets equally — 420 °C and 115 °C are both above "
                     "room temperature",
             "correct": False,
             "why": "That only means both are solids in the room. It does "
                    "not sort one from the other."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s31",
        "band": "standard",
        "text": "A furnace lining must stay solid at 1200 °C. Iron melts at "
                "1538 °C, aluminium at 660 °C, tin at 232 °C and lead at "
                "327 °C. Which of the four could it be made from?",
        "options": [
            {"text": "Aluminium, because 660 °C is a comfortable working "
                     "temperature",
             "correct": False,
             "why": "660 °C is well below 1200 °C, so the aluminium would "
                    "have melted already."},
            {"text": "Tin, because a low melting point makes a lining easier "
                     "to cast in place",
             "correct": False,
             "why": "Tin melts at 232 °C, which is not even a fifth of the "
                    "working temperature."},
            {"text": "Iron, because its melting point is above the working "
                     "temperature",
             "correct": True},
            {"text": "Lead, because lead is by far the densest of the four "
                     "metals listed",
             "correct": False,
             "why": "Lead melts at 327 °C. Being dense does not keep a "
                    "lining solid."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-s32",
        "band": "standard",
        "text": "Mercury is a liquid and it still conducts electricity. How "
                "can a liquid conduct, if conducting is a metal property?",
        "options": [
            {"text": "It cannot; the conduction must come from a metal "
                     "powder stirred into the mercury",
             "correct": False,
             "why": "Pure mercury conducts on its own, with nothing stirred "
                    "into it at all."},
            {"text": "Because any liquid conducts electricity, whatever it "
                     "is made of",
             "correct": False,
             "why": "Pure water and cooking oil are both liquids and both "
                    "conduct very poorly."},
            {"text": "Because mercury has been magnetised, and a magnet "
                     "carries a current",
             "correct": False,
             "why": "Magnetism and electrical conduction are different "
                    "things, and mercury is not magnetic."},
            {"text": "Because mercury is a metal, and its free electrons "
                     "move whether it is solid or liquid",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h09",
        "band": "harder",
        "text": "Diamond carries heat better than copper does, yet it does "
                "not conduct electricity at all. What does that pair of "
                "facts show?",
        "options": [
            {"text": "That conducting heat and conducting electricity are "
                     "separate properties",
             "correct": True},
            {"text": "That diamond must really be a metal, since it beats "
                     "copper at something",
             "correct": False,
             "why": "Beating a metal at one property does not make an "
                    "element a metal. Diamond is brittle and insulating."},
            {"text": "That copper has been wrongly classed, since a "
                     "non-metal outperforms it",
             "correct": False,
             "why": "Copper passes every metal test. One property going the "
                    "other way changes nothing."},
            {"text": "That every non-metal carries heat better than every "
                     "metal does, without exception",
             "correct": False,
             "why": "Wood and sulfur are non-metals and both are poor "
                    "conductors of heat. Diamond is the odd one out."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h10",
        "band": "harder",
        "text": "One idea — that a metal's outer electrons move freely "
                "through the whole structure — accounts for its conduction, "
                "its malleability and its shine. Why do scientists prefer "
                "that to a list of five separate facts?",
        "options": [
            {"text": "Because a list is harder to remember than a single "
                     "sentence is",
             "correct": False,
             "why": "Being easy to remember is a convenience, not a reason "
                    "to believe an explanation."},
            {"text": "Because one cause that explains several facts can also "
                     "predict new ones",
             "correct": True},
            {"text": "Because the five separate facts have each turned out "
                     "to be false",
             "correct": False,
             "why": "Every one of them is true and measurable. The idea "
                    "explains them rather than replacing them."},
            {"text": "Because scientists always prefer the shortest possible "
                     "description of anything, whatever it explains",
             "correct": False,
             "why": "Shortness settles nothing on its own. A one-word wrong "
                    "answer is shorter than a right one."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h11",
        "band": "harder",
        "text": "Gallium is shiny, conducts electricity and can be beaten "
                "flat — and it melts at 30 °C, so a lump of it melts in a "
                "warm hand. A student says it cannot be a metal. Evaluate "
                "that.",
        "options": [
            {"text": "They are right: a metal has to survive being held",
             "correct": False,
             "why": "Being held is not one of the tests. The other three "
                    "properties all say metal."},
            {"text": "They are right: 30 °C is below room temperature "
                     "everywhere",
             "correct": False,
             "why": "30 °C is above a normal room. Gallium is a solid on the "
                    "bench and a liquid in a hand."},
            {"text": "They are wrong: three properties say metal and only "
                     "the melting point is unusual",
             "correct": True},
            {"text": "They are wrong: melting point has never been used to "
                     "classify an element",
             "correct": False,
             "why": "Melting point is one of the six properties, and it is "
                    "usually high for a metal."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h12",
        "band": "harder",
        "text": "A new element is made four atoms at a time and each atom "
                "lasts a fraction of a second. Nobody can hammer it, wire it "
                "up or weigh out a lump of it. How can chemists still say "
                "whether it is a metal?",
        "options": [
            {"text": "They cannot, so the element is neither a metal nor a "
                     "non-metal",
             "correct": False,
             "why": "Every element falls on one side or the other. Being "
                    "hard to test does not put it outside."},
            {"text": "They weigh a single atom and call anything heavy a "
                     "metal",
             "correct": False,
             "why": "Atomic mass does not decide the class. Iodine atoms are "
                    "heavier than iron atoms."},
            {"text": "They assume it is a metal, because new elements always "
                     "turn out to be",
             "correct": False,
             "why": "An assumption is not a classification, and a label like "
                    "that would carry no information."},
            {"text": "They use its position in the periodic table, which "
                     "sits well inside the metal side",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h13",
        "band": "harder",
        "text": "Two single tests are offered on an unknown solid element: "
                "whether it conducts electricity, and whether it flattens "
                "under a hammer. Which is the stronger evidence that it is a "
                "metal?",
        "options": [
            {"text": "The hammer, because graphite is a non-metal that "
                     "conducts",
             "correct": True},
            {"text": "The circuit, because conduction is the one property "
                     "that never has an exception",
             "correct": False,
             "why": "Graphite is exactly that exception, which is why the "
                    "circuit is the weaker of the two."},
            {"text": "Neither, because a single test can never give any "
                     "evidence at all",
             "correct": False,
             "why": "A single test gives a clue. The point is that a clue is "
                    "not yet an identification."},
            {"text": "The circuit, because a hammer changes the sample and "
                     "so spoils the evidence",
             "correct": False,
             "why": "Flattening a sample does not change which element it "
                    "is. The result still counts."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h14",
        "band": "harder",
        "text": "Sodium has a density of 0.97 g/cm³ and melts at 98 °C, and "
                "lead is soft enough to scratch with a coin. Both are "
                "metals. What does the pair show about the metal property "
                "list?",
        "options": [
            {"text": "That the list is wrong and should be thrown away",
             "correct": False,
             "why": "The list works for almost every metal. Two awkward "
                    "cases do not overturn it."},
            {"text": "That the list gives what is typical, not a rule every "
                     "metal must obey",
             "correct": True},
            {"text": "That sodium and lead have been wrongly classified for "
                     "years",
             "correct": False,
             "why": "Both are shiny, conducting and malleable. They are "
                    "metals on the pattern."},
            {"text": "That density and hardness should be struck off the "
                     "list, since they mislead so often",
             "correct": False,
             "why": "Both are useful for most metals. A property with "
                    "exceptions is still worth measuring."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h15",
        "band": "harder",
        "text": "A student proposes one machine test for every element: "
                "squeeze a sample, and call it a metal if it flattens. On "
                "which elements would that test give no answer at all?",
        "options": [
            {"text": "On none of them, because every element can be squeezed "
                     "in some form",
             "correct": False,
             "why": "A gas cannot be squeezed flat and neither can a liquid. "
                    "Both simply move aside."},
            {"text": "On the metals, because a metal is too hard for any "
                     "machine to flatten",
             "correct": False,
             "why": "Flattening metals is what a rolling mill does all day. "
                    "Metals are the easy case."},
            {"text": "On anything that is a gas or a liquid, such as oxygen "
                     "or mercury",
             "correct": True},
            {"text": "On the metalloids, because they sit on the line and so "
                     "cannot be squeezed at all",
             "correct": False,
             "why": "Silicon is a brittle solid and shatters under pressure, "
                    "which is a perfectly clear result."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h16",
        "band": "harder",
        "text": "Graphite is soft, dull and conducts electricity. Diamond is "
                "the hardest substance known, clear, and insulates. Both are "
                "pure carbon. Does that break the metal and non-metal "
                "classification?",
        "options": [
            {"text": "Yes, because one element cannot belong to two classes "
                     "at once",
             "correct": False,
             "why": "It does not belong to two. Both forms are non-metals, "
                    "however differently they behave."},
            {"text": "Yes, because diamond must really be a metal and "
                     "graphite a non-metal, since they behave nothing "
                     "alike",
             "correct": False,
             "why": "Diamond is clear, brittle and insulating. Nothing about "
                    "it is metallic."},
            {"text": "No, because graphite and diamond are two different "
                     "elements entirely",
             "correct": False,
             "why": "Both are carbon. Only the arrangement of the atoms is "
                    "different."},
            {"text": "No, because both are carbon and both are non-metals; "
                     "only the arrangement of the atoms differs",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h17",
        "band": "harder",
        "text": "Lead is a metal and melts at 327 °C; mercury is a metal and "
                "melts at −39 °C; iodine is a non-metal and melts at 114 °C, "
                "in between the two. What does that show about melting point "
                "as a test?",
        "options": [
            {"text": "That the metal and non-metal ranges overlap, so "
                     "melting point cannot decide alone",
             "correct": True},
            {"text": "That iodine has been misclassified and is really a "
                     "metal",
             "correct": False,
             "why": "Iodine is brittle, dull-breaking and insulating. Its "
                    "melting point is the only metal-looking thing about "
                    "it."},
            {"text": "That mercury has been misclassified and is really a "
                     "non-metal",
             "correct": False,
             "why": "Mercury is mirror-bright and conducts. Only its melting "
                    "point is unusual."},
            {"text": "That melting point is not worth measuring on an "
                     "unknown element at all",
             "correct": False,
             "why": "It is one of the six properties and it is useful — it "
                    "is simply not decisive alone."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h18",
        "band": "harder",
        "text": "A company advertises a kettle with no metal anywhere in it, "
                "and the heating element still carries a current. A customer "
                "says that is impossible. Evaluate the complaint.",
        "options": [
            {"text": "The customer is right: only a metal can carry a current",
             "correct": False,
             "why": "Graphite is a non-metal and carries a current well "
                    "enough to be used as an electrode."},
            {"text": "The customer is wrong: a non-metal such as graphite "
                     "conducts",
             "correct": True},
            {"text": "The customer is right: a kettle has to boil water, and "
                     "only metals get hot",
             "correct": False,
             "why": "Anything carrying a current warms up. Getting hot is "
                    "not a metal privilege."},
            {"text": "The customer is wrong: plastic carries a current just as "
                     "copper does",
             "correct": False,
             "why": "Plastic is an insulator, and it is wrapped round wires "
                    "precisely to stop a current."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h19",
        "band": "harder",
        "text": "Mercury filled thermometers for three hundred years and has "
                "been replaced by coloured alcohol. Using only properties "
                "from this lesson, what did mercury offer and what limited "
                "it?",
        "options": [
            {"text": "It had a high melting point and was easy to read; being "
                     "a non-metal limited it",
             "correct": False,
             "why": "Mercury has the lowest melting point of any metal, and "
                    "mercury is a metal."},
            {"text": "It had a low density and was cheap to make; being too "
                     "light to see limited it",
             "correct": False,
             "why": "Mercury is one of the densest liquids there is, and a "
                    "silver thread is easy to see."},
            {"text": "It stayed liquid over a wide range and carried heat "
                     "well; below −39 °C it freezes",
             "correct": True},
            {"text": "It was brittle and gave a sharp reading; shattering in "
                     "the glass tube limited it",
             "correct": False,
             "why": "A liquid metal cannot be brittle. Brittleness belongs "
                    "to non-metal solids."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h20",
        "band": "harder",
        "text": "Sample A conducts electricity and flattens under a hammer. "
                "Sample B conducts electricity and shatters. Sample C "
                "insulates and shatters. Which is the metal, and which "
                "sample is the reason one test is not enough?",
        "options": [
            {"text": "A is the metal, and C is the reason, because C "
                     "insulates",
             "correct": False,
             "why": "C behaves like an ordinary non-metal on both tests. It "
                    "surprises nobody."},
            {"text": "B is the metal, and A is the reason, because A is too "
                     "easy to classify",
             "correct": False,
             "why": "B shatters, which is a non-metal property. A agrees "
                    "with itself on both tests."},
            {"text": "C is the metal, and B is the reason, because B "
                     "disagrees with itself",
             "correct": False,
             "why": "C insulates and shatters, which is the non-metal "
                    "pattern the whole way through."},
            {"text": "A is the metal, and B is the reason, because B "
                     "conducts and yet shatters",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h21",
        "band": "harder",
        "text": "Metals far outnumber non-metals in the periodic table. A "
                "student says they will simply answer “metal” every time "
                "and be right most often. Evaluate that as a method.",
        "options": [
            {"text": "It is not a method: a guess gives no reason and gets "
                     "the interesting cases wrong",
             "correct": True},
            {"text": "It is a good method: being right most of the time is "
                     "what science wants",
             "correct": False,
             "why": "Science wants reasons that hold for each case, not a "
                    "score that works on average."},
            {"text": "It is a bad method: fewer than half the elements are "
                     "really metals",
             "correct": False,
             "why": "Metals are the clear majority, which is the one part "
                    "of the student's thinking that is right."},
            {"text": "It is a good method: the non-metals are never the ones "
                     "asked about",
             "correct": False,
             "why": "The non-metals include oxygen, carbon and nitrogen, "
                    "which are asked about constantly."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h22",
        "band": "harder",
        "text": "Copper's electrical conductivity is about 59 000 000 "
                "siemens per metre; pure silicon's is about 0.001, and "
                "sulfur's is smaller still. Why is a measurement like that "
                "more useful than the label “conducts”?",
        "options": [
            {"text": "Because a number can be looked up and a label cannot",
             "correct": False,
             "why": "Labels are looked up constantly. What the number adds "
                    "is how much, not where to find it."},
            {"text": "Because it shows conduction is a scale, not a "
                     "yes-or-no answer",
             "correct": True},
            {"text": "Because it proves silicon is really a metal after all",
             "correct": False,
             "why": "Being thousands of millions of times worse than copper "
                    "is exactly why silicon is not simply a metal."},
            {"text": "Because a number always makes a conclusion more "
                     "certain than any words can",
             "correct": False,
             "why": "A badly measured number is worse than a careful "
                    "description. Precision is not accuracy."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h23",
        "band": "harder",
        "text": "A student writes: “Metals are heavy and non-metals are "
                "light.” Sodium is a metal with a density of 0.97 g/cm³; "
                "iodine is a non-metal with a density of 4.9 g/cm³. Test the "
                "claim.",
        "options": [
            {"text": "The claim holds: sodium is much denser than iodine",
             "correct": False,
             "why": "It is the other way round. Iodine's figure is five "
                    "times sodium's."},
            {"text": "The claim holds: density is not what the word heavy "
                     "means",
             "correct": False,
             "why": "Density is exactly what heavy-for-its-size means, and "
                    "it is the figure given."},
            {"text": "The claim fails both ways: the metal is the lighter "
                     "and the non-metal the denser",
             "correct": True},
            {"text": "The claim cannot be tested: density is measured "
                     "differently for each class",
             "correct": False,
             "why": "Density is mass divided by volume for everything. The "
                    "method does not change."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h24",
        "band": "harder",
        "text": "A properties table says metals conduct electricity — all "
                "of them — but hedges the melting-point row with the word "
                "“usually”. Why are the two rows worded differently?",
        "options": [
            {"text": "Because melting points are harder to measure than "
                     "conduction is",
             "correct": False,
             "why": "Both are routine measurements. The wording is about "
                    "exceptions, not about difficulty."},
            {"text": "Because conduction was discovered first and so has "
                     "been checked more often",
             "correct": False,
             "why": "How long a property has been known does not decide how "
                    "reliable it is."},
            {"text": "Because melting point is not really a property of a "
                     "metal at all",
             "correct": False,
             "why": "It is one of the six properties and it is high for the "
                    "great majority of metals."},
            {"text": "Because no metal fails the conduction test, while "
                     "mercury and sodium melt low",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h25",
        "band": "harder",
        "text": "Brass conducts electricity less well than pure copper but "
                "is much harder. Door handles are brass and wires are "
                "copper. What general rule about alloys does that pair show?",
        "options": [
            {"text": "Alloying trades some of a metal's conduction for "
                     "hardness",
             "correct": True},
            {"text": "Alloying always improves every property of the metal "
                     "it starts from",
             "correct": False,
             "why": "If it improved everything, wires would be brass too. "
                    "The conduction is worse."},
            {"text": "Alloying turns a metal into a non-metal, which is why "
                     "brass is harder",
             "correct": False,
             "why": "Brass is a metal — shiny, malleable and conducting. It "
                    "is simply a harder one."},
            {"text": "Alloying makes no measurable difference and is done "
                     "for the colour alone",
             "correct": False,
             "why": "Brass is measurably harder than copper, which is the "
                    "whole reason a handle is brass."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h26",
        "band": "harder",
        "text": "A museum has a 2500-year-old bronze sword that is still "
                "solid and an iron sword of the same age that has crumbled "
                "to rust. Both are metals. What does that tell you about the "
                "property lists?",
        "options": [
            {"text": "That iron was never a metal, since a real metal would "
                     "have survived",
             "correct": False,
             "why": "Iron passes every property test. Surviving burial is "
                    "not one of them."},
            {"text": "That the lists describe properties, and say nothing "
                     "about how an element reacts",
             "correct": True},
            {"text": "That bronze must be a non-metal, since only non-metals "
                     "last",
             "correct": False,
             "why": "Bronze is an alloy of copper and tin, and it conducts "
                    "and bends like a metal."},
            {"text": "That the property lists are useless for anything that "
                     "has been buried underground for centuries",
             "correct": False,
             "why": "The lists classify an element wherever it has been. "
                    "Where a sword lay changes nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h27",
        "band": "harder",
        "text": "A laptop needs a heat sink. Copper carries heat better than "
                "aluminium; aluminium has a density of 2.7 g/cm³ against "
                "copper's 8.9 g/cm³. The brief says the machine must be as "
                "light as possible. Which metal?",
        "options": [
            {"text": "Copper, because carrying heat is the only thing that "
                     "matters here",
             "correct": False,
             "why": "The brief names weight as well, and copper is over "
                    "three times as dense."},
            {"text": "Copper, because aluminium does not conduct heat at all",
             "correct": False,
             "why": "Aluminium conducts heat well. It is simply not quite as "
                    "good as copper."},
            {"text": "Aluminium, because it conducts well enough and the "
                     "brief puts weight first",
             "correct": True},
            {"text": "Aluminium, because a less dense metal always carries "
                     "heat better than a dense one",
             "correct": False,
             "why": "Copper is the denser of the two and carries heat "
                    "better. The two do not track each other."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h28",
        "band": "harder",
        "text": "A technician is given an element as a fine powder that "
                "looks dull whatever it is made of. It cannot be hammered "
                "flat and it will not ring when struck. Which tests still "
                "work on it?",
        "options": [
            {"text": "None of them, because every one of the tests needs a "
                     "solid lump",
             "correct": False,
             "why": "Two of them do not. A powder can be heated, and it can "
                    "be pressed between two electrodes."},
            {"text": "Only the hammer test, once the powder has been pressed "
                     "back together",
             "correct": False,
             "why": "Pressed powder is not the same sample, and the result "
                    "would say nothing about the element."},
            {"text": "Only the sound test, since a powder makes a "
                     "distinctive noise of its own",
             "correct": False,
             "why": "Ringing needs a solid body to vibrate. A powder is the "
                    "one form that cannot."},
            {"text": "Melting point and electrical conduction, since neither "
                     "needs a lump",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h29",
        "band": "harder",
        "text": "In the 1850s aluminium cost more than gold, and Napoleon "
                "III kept aluminium plates for his most honoured guests. "
                "Today it is kitchen foil. The metal itself did not change. "
                "What did?",
        "options": [
            {"text": "How cheaply it could be separated from its ore",
             "correct": True},
            {"text": "How dense it was compared with other metals",
             "correct": False,
             "why": "Density is fixed for an element and did not fall as "
                    "better aluminium was made. It was 2.7 g/cm³ then and is "
                    "2.7 g/cm³ now."},
            {"text": "How well it conducted a current",
             "correct": False,
             "why": "An element's conductivity does not rise because people "
                    "have started using it for wiring."},
            {"text": "How it was classed among the elements",
             "correct": False,
             "why": "Nothing reclassified it. Aluminium was shiny, malleable "
                    "and conducting in 1855 too."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h30",
        "band": "harder",
        "text": "Two sentences: “Every metal conducts electricity” and "
                "“Everything that conducts electricity is a metal”. One is "
                "true and one is false. Explain which is which.",
        "options": [
            {"text": "Both are true, because they say exactly the same thing",
             "correct": False,
             "why": "Swapping the two halves of a sentence like that changes "
                    "what it claims. Only one survives."},
            {"text": "The first is true; the second is false, because "
                     "graphite conducts",
             "correct": True},
            {"text": "Both are false, because plenty of metals do not "
                     "conduct electricity at all",
             "correct": False,
             "why": "Every metal conducts. That half of the pair is the one "
                    "that holds."},
            {"text": "The second is true; the first is false, because "
                     "mercury does not conduct",
             "correct": False,
             "why": "Mercury conducts perfectly well. It is the melting "
                    "point that makes mercury unusual."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h31",
        "band": "harder",
        "text": "Element P: density 0.53 g/cm³, melts at 181 °C, conducts "
                "electricity, cuts with a knife. Element Q: density "
                "2.07 g/cm³, melts at 115 °C, does not conduct, crumbles. "
                "Classify both and name the test that decided it.",
        "options": [
            {"text": "Both are metals, and density was what decided it",
             "correct": False,
             "why": "Q does not conduct and it crumbles. Those are non-metal "
                    "properties whatever its density."},
            {"text": "P is a non-metal and Q a metal, and melting point "
                     "decided it",
             "correct": False,
             "why": "The classes are the other way round, and the two "
                    "melting points are only 66 °C apart."},
            {"text": "P is a metal and Q a non-metal, and conduction decided "
                     "it",
             "correct": True},
            {"text": "Neither can be classified, because their melting "
                     "points are far too close together",
             "correct": False,
             "why": "Melting point was never going to settle these two. The "
                    "conduction test does it cleanly."},
        ],
        "figure": None,
    },
    {
        "id": "c8-01-h32",
        "band": "harder",
        "text": "One phone contains copper wire, silicon chips and a plastic "
                "case. Describe what each of the three contributes, in terms "
                "of how well it lets a current pass.",
        "options": [
            {"text": "All three insulate, and the current is carried by the "
                     "battery alone",
             "correct": False,
             "why": "A battery pushes a current; something still has to "
                    "carry it, and the copper does."},
            {"text": "All three conduct, which is why a phone works at all",
             "correct": False,
             "why": "Plastic is an insulator, chosen precisely so the "
                    "current cannot reach a hand."},
            {"text": "Copper conducts, silicon conducts under some "
                     "conditions, and plastic insulates",
             "correct": True},
            {"text": "Copper insulates, silicon conducts perfectly and "
                     "plastic conducts a little",
             "correct": False,
             "why": "All three are the wrong way round. Copper is the "
                    "conductor of the three."},
        ],
        "figure": None,
    },
]
