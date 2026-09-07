"""Chemistry · Chemical changes — reactivity, acids, salts and electrolysis.

Thirteen subtopics of AQA 8462 §5.4, twelve questions each. The distractors are
built from the misconceptions the lesson pages themselves declare: the
displacement rule run backwards (copper "displacing" iron), carbon reduction
applied to metals above carbon, the agent that does the opposite of its name
(an oxidising agent is itself reduced), the missing water or missing carbon
dioxide from an acid + carbonate, pH 2 confused with pH 12, the cathode
believed to be positive, the metal predicted at the anode, the impure copper
put on the wrong electrode, sodium predicted from an aqueous solution, and
"strong" read as "concentrated".

Two subtopics sit outside the base set and their flags come from the
curriculum, not from here: `titrations` is chemistry-only (triple_only=True)
and `strong-weak-acids` and `half-equations` are Higher tier. Every
foundation-tier question in this file is kept clear of half equations and of
strong/weak ionisation reasoning.

Equations are written flat throughout — formulae (H2SO4, Al2O3, CO2) AND ionic
charges (Cu2+, O2-, 2e-, 4OH-). ⊕ The charges were superscripted (Cu²⁺, 2e⁻)
until the cold review of 6 Sep 2026; `analysis.py` and the rest of the chemistry
pool had always written them flat, so a student met both forms in one week's
homework. Flat is now the single form across all nine chemistry files — do not
reintroduce the superscripts here. Every equation has been checked for atom and
charge balance, and every product is one the reaction actually gives.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── reactivity-series ─────────────────────────────────────────────
    {
        "id": "ks4-reactivity-series-e01",
        "subtopic_slug": "reactivity-series",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Four metals are listed: zinc, copper, potassium, magnesium. "
                "State which one is the most reactive.",
        "options": [
            "Zinc",
            "Copper",
            "Potassium",
            "Magnesium",
        ],
        "correct_index": 2,
        "why": "Potassium sits at the very top of the reactivity series, "
               "above sodium, lithium, calcium and magnesium.",
    },
    {
        "id": "ks4-reactivity-series-e02",
        "subtopic_slug": "reactivity-series",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what is observed when a small piece of calcium is "
                "added to cold water.",
        "options": [
            "Steady bubbling, and the solution slowly turns cloudy",
            "No change at all, even after several minutes",
            "It melts into a ball and burns with a lilac flame",
            "A dense red-brown gas is given off from the surface",
        ],
        "correct_index": 0,
        "why": "Calcium reacts steadily with cold water to give hydrogen and "
               "calcium hydroxide, which is only slightly soluble and clouds "
               "the water.",
    },
    {
        "id": "ks4-reactivity-series-e03",
        "subtopic_slug": "reactivity-series",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two non-metals are placed in the reactivity series. State "
                "which two, and why they are included.",
        "options": [
            "Oxygen and chlorine — they are the gases metals react with",
            "Hydrogen and oxygen — they are the two products made when a "
            "reactive metal is dropped into cold water",
            "Carbon and chlorine — they both attack metals when hot",
            "Carbon and hydrogen — they are reference points for extraction "
            "and for reactions with acid",
        ],
        "correct_index": 3,
        "why": "Carbon marks the line between metals extracted by smelting "
               "and by electrolysis, and hydrogen marks which metals react "
               "with dilute acid.",
    },
    {
        "id": "ks4-reactivity-series-e04",
        "subtopic_slug": "reactivity-series",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the metal that bubbles steadily in dilute "
                "hydrochloric acid but shows no reaction with cold water.",
        "options": [
            "Sodium",
            "Zinc",
            "Copper",
            "Gold",
        ],
        "correct_index": 1,
        "why": "Zinc is above hydrogen so it releases hydrogen from acid, but "
               "it is too low in the series to attack cold water.",
    },
    {
        "id": "ks4-reactivity-series-s01",
        "subtopic_slug": "reactivity-series",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium ribbon is placed in colourless zinc sulfate "
                "solution. Predict what happens.",
        "options": [
            "No reaction — zinc is the more reactive of the two metals, so it "
            "stays in the solution as its ions",
            "Magnesium displaces zinc: grey zinc appears and magnesium "
            "sulfate forms",
            "Zinc displaces magnesium: magnesium metal is deposited",
            "The solution turns bright blue as zinc ions are released",
        ],
        "correct_index": 1,
        "why": "Magnesium is above zinc, so Mg + ZnSO4 → MgSO4 + Zn and the "
               "displaced zinc appears as a grey deposit.",
    },
    {
        "id": "ks4-reactivity-series-s02",
        "subtopic_slug": "reactivity-series",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why silver is found in the ground as the pure metal, "
                "while magnesium is only ever found in compounds.",
        "options": [
            "Silver atoms are much heavier than magnesium atoms, so over time "
            "they sink through the rock and gather as the pure metal",
            "Magnesium compounds are made by living organisms in the soil",
            "Silver melts at a much lower temperature and separates out",
            "Silver is very unreactive, so it does not readily combine, while "
            "magnesium reacts easily",
        ],
        "correct_index": 3,
        "why": "A metal is found native only if it is unreactive enough to "
               "resist combining with oxygen and sulfur.",
    },
    {
        "id": "ks4-reactivity-series-s03",
        "subtopic_slug": "reactivity-series",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student places clean copper turnings into iron(II) sulfate "
                "solution and records no change after ten minutes. Explain "
                "this result.",
        "options": [
            "Copper is below iron in the series, so it cannot displace iron",
            "Copper is above iron, so the reaction finishes too fast to see",
            "Iron sulfate is insoluble, so no iron ions are available",
            "Copper displaces metals from oxides only, never from solutions",
        ],
        "correct_index": 0,
        "why": "Displacement only runs one way: the more reactive metal takes "
               "the place of the less reactive one, and copper is the less "
               "reactive here.",
    },
    {
        "id": "ks4-reactivity-series-s04",
        "subtopic_slug": "reactivity-series",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Four metal strips are each dropped into dilute hydrochloric "
                "acid. W fizzes vigorously, X fizzes very slowly, Y gives no "
                "bubbles and Z fizzes steadily. Determine the order from most "
                "to least reactive.",
        "options": [
            "Y, X, Z, W",
            "W, X, Z, Y",
            "W, Z, X, Y",
            "Z, W, Y, X",
        ],
        "correct_index": 2,
        "why": "The more reactive the metal, the faster it releases hydrogen "
               "from the acid, so vigorous beats steady beats slow beats "
               "none.",
    },
    {
        "id": "ks4-reactivity-series-h01",
        "subtopic_slug": "reactivity-series",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Copper displaces iron from iron(II) "
                "sulfate, because copper is lower in the reactivity series "
                "and lower metals are the ones that displace.' Identify the "
                "error.",
        "options": [
            "The rule is the wrong way round — the more reactive metal "
            "displaces the less reactive one, so iron displaces copper",
            "There is no error — the reasoning and the conclusion both hold",
            "Only the salt is wrong — copper displaces iron from iron "
            "chloride solution, but sulfate ions hold on to the iron too "
            "tightly",
            "Displacement needs a molten compound, so no reaction can happen "
            "in a solution",
        ],
        "correct_index": 0,
        "why": "The more reactive metal holds the non-metal more strongly, so "
               "it is the one that takes the compound over.",
    },
    {
        "id": "ks4-reactivity-series-h02",
        "subtopic_slug": "reactivity-series",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Metal Q displaces copper from copper sulfate solution but "
                "does not react with cold water. Metal R fizzes steadily in "
                "cold water. Deduce a possible identity for Q and for R.",
        "options": [
            "Q = calcium, R = iron",
            "Q = copper, R = zinc",
            "Q = zinc, R = lithium",
            "Q = sodium, R = magnesium",
        ],
        "correct_index": 2,
        "why": "Zinc is above copper but below the metals that attack cold "
               "water, while lithium is one of the metals that fizzes "
               "steadily in it.",
    },
    {
        "id": "ks4-reactivity-series-h03",
        "subtopic_slug": "reactivity-series",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what the reactivity of a metal tells you about how "
                "hard its oxide is to break down.",
        "options": [
            "Reactive metals form oxides that are only weakly held together, "
            "so gentle heating alone decomposes them back to the metal",
            "A more reactive metal holds its oxygen more strongly, so its "
            "oxide is harder to reduce and needs more energy",
            "Oxide stability depends on the mass of the metal, not on its "
            "reactivity at all",
            "Reactive metals form oxides that carbon reduces most easily",
        ],
        "correct_index": 1,
        "why": "The more readily a metal gives its electrons away to oxygen, "
               "the more energy it takes to get them back.",
    },
    {
        "id": "ks4-reactivity-series-h04",
        "subtopic_slug": "reactivity-series",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student suggests that because iron reacts with steam, it "
                "must react just as readily with cold water. Evaluate this "
                "suggestion.",
        "options": [
            "Correct — a metal that reacts with steam must react at exactly "
            "the same rate with cold water, since it is the same substance "
            "either way",
            "Correct — an iron gate left in the rain goes rusty, which shows "
            "the same reaction running at the same rate in cold water",
            "Incorrect — iron reacts with neither steam nor cold water",
            "Incorrect — steam is far hotter, and iron reacts only very "
            "slowly with it and not noticeably with cold water",
        ],
        "correct_index": 3,
        "why": "Iron sits low enough in the series that only the extra energy "
               "of steam gets a visible reaction going.",
    },
    # ── extraction-of-metals ──────────────────────────────────────────
    {
        "id": "ks4-extraction-of-metals-e01",
        "subtopic_slug": "extraction-of-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the method used to extract zinc from zinc oxide.",
        "options": [
            "Electrolysis of the molten oxide",
            "Heating the oxide with carbon",
            "Displacement using aluminium powder in solution",
            "Heating the ore in air on its own",
        ],
        "correct_index": 1,
        "why": "Zinc is below carbon in the reactivity series, so carbon can "
               "take the oxygen away from it: ZnO + C → Zn + CO.",
    },
    {
        "id": "ks4-extraction-of-metals-e02",
        "subtopic_slug": "extraction-of-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the main ore of iron that is fed into a blast furnace.",
        "options": [
            "Bauxite",
            "Cryolite",
            "Malachite",
            "Haematite",
        ],
        "correct_index": 3,
        "why": "Haematite is mostly iron(III) oxide, Fe2O3, which is what the "
               "carbon monoxide reduces in the furnace.",
    },
    {
        "id": "ks4-extraction-of-metals-e03",
        "subtopic_slug": "extraction-of-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the pair of metals that are found in the Earth as "
                "the uncombined element.",
        "options": [
            "Iron and zinc",
            "Aluminium and magnesium",
            "Gold and platinum",
            "Sodium and potassium",
        ],
        "correct_index": 2,
        "why": "Gold and platinum are so unreactive that they never combined "
               "with oxygen or sulfur in the first place.",
    },
    {
        "id": "ks4-extraction-of-metals-e04",
        "subtopic_slug": "extraction-of-metals",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the metal that must be extracted by electrolysis "
                "rather than by heating with carbon.",
        "options": [
            "Sodium",
            "Iron",
            "Lead",
            "Copper",
        ],
        "correct_index": 0,
        "why": "Sodium is above carbon in the reactivity series, so carbon "
               "cannot take the non-metal away from it.",
    },
    {
        "id": "ks4-extraction-of-metals-s01",
        "subtopic_slug": "extraction-of-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Inside the blast furnace, carbon dioxide reacts with more "
                "hot coke. Identify the balanced equation for this step.",
        "options": [
            "CO2 + C → 2CO",
            "CO2 + 2C → 2CO2",
            "C + O2 → CO2",
            "2CO + O2 → 2CO2",
        ],
        "correct_index": 0,
        "why": "One carbon dioxide shares its two oxygen atoms with one more "
               "carbon atom, giving two molecules of carbon monoxide.",
    },
    {
        "id": "ks4-extraction-of-metals-s02",
        "subtopic_slug": "extraction-of-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Coke is loaded into the blast furnace along with the iron "
                "ore. Describe the two jobs the coke does.",
        "options": [
            "It keeps the furnace cool and it filters out impurities",
            "It supplies the electric current for the reduction, and it "
            "lowers the melting point of the iron so that it can be tapped "
            "off",
            "It burns to heat the furnace, and it is the source of the carbon "
            "monoxide that removes the oxygen",
            "It dissolves the ore and it coats the iron to stop it rusting",
        ],
        "correct_index": 2,
        "why": "Burning coke provides the heat, and reacting it further gives "
               "the carbon monoxide that reduces the iron oxide.",
    },
    {
        "id": "ks4-extraction-of-metals-s03",
        "subtopic_slug": "extraction-of-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why aluminium was once a rarer and more expensive "
                "metal than gold, even though it is very common in the "
                "Earth's crust.",
        "options": [
            "Aluminium ore was extremely rare until large new deposits of "
            "bauxite were discovered",
            "Aluminium could only be imported from one country at the time",
            "Aluminium is far denser, so much more ore had to be dug up",
            "Extracting it needs electrolysis, and cheap electricity did not "
            "yet exist",
        ],
        "correct_index": 3,
        "why": "Abundance is not the same as availability — aluminium is "
               "locked in a compound that only electricity can break open.",
    },
    {
        "id": "ks4-extraction-of-metals-s04",
        "subtopic_slug": "extraction-of-metals",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Copper oxide is heated strongly with carbon and carbon "
                "dioxide is given off. Identify the balanced equation.",
        "options": [
            "CuO + C → Cu + CO2",
            "2CuO + C → 2Cu + CO2",
            "CuO + 2C → 2Cu + CO2",
            "2CuO + 2C → Cu + 2CO2",
        ],
        "correct_index": 1,
        "why": "One carbon atom needs two oxygen atoms to become CO2, and "
               "those come from two units of CuO, leaving 2Cu.",
    },
    {
        "id": "ks4-extraction-of-metals-h01",
        "subtopic_slug": "extraction-of-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Zinc oxide is heated with carbon in one experiment and with "
                "aluminium powder in another. Predict whether each mixture "
                "produces zinc.",
        "options": [
            "Neither — zinc is too reactive to be displaced from its oxide",
            "Only the aluminium works, because carbon cannot reduce any oxide",
            "Only the carbon works, because aluminium is below zinc",
            "Both work — carbon and aluminium are each more reactive than "
            "zinc",
        ],
        "correct_index": 3,
        "why": "Zinc sits below both carbon and aluminium, so either of them "
               "can take its oxygen away.",
    },
    {
        "id": "ks4-extraction-of-metals-h02",
        "subtopic_slug": "extraction-of-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the same reactivity series that predicts "
                "displacement in solution also predicts a metal's extraction "
                "method.",
        "options": [
            "Because every extraction method uses a solution of the ore",
            "Because extraction is displacement in reverse — the more "
            "reactive the metal, the more tightly it holds its non-metal",
            "Because the series is really an order of melting points, and "
            "that is what sets the temperature the furnace must be able to "
            "reach",
            "Because only a metal that has already been in solution can be "
            "reduced back to the element",
        ],
        "correct_index": 1,
        "why": "Both jobs come down to the same question: which element wants "
               "the non-metal more.",
    },
    {
        "id": "ks4-extraction-of-metals-h03",
        "subtopic_slug": "extraction-of-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two ores are available: tin oxide and calcium oxide. "
                "Determine which of them carbon can reduce, and justify the "
                "choice.",
        "options": [
            "Tin oxide only — tin lies below carbon in the reactivity series",
            "Calcium oxide only — calcium is more reactive, so it reacts more "
            "readily",
            "Both — carbon reduces any metal oxide if it is hot enough",
            "Neither — carbon reduces sulfide ores but never oxides",
        ],
        "correct_index": 0,
        "why": "Carbon can only take oxygen from metals below it in the "
               "series, and calcium is well above it.",
    },
    {
        "id": "ks4-extraction-of-metals-h04",
        "subtopic_slug": "extraction-of-metals",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the blast furnace, Fe2O3 + 3CO → 2Fe + 3CO2. Determine "
                "how many molecules of carbon monoxide are needed to reduce "
                "2 units of Fe2O3.",
        "options": [
            "2 molecules",
            "3 molecules",
            "6 molecules",
            "12 molecules",
        ],
        "correct_index": 2,
        "why": "The equation needs 3 CO for every 1 Fe2O3, so 2 units of the "
               "oxide need 2 × 3 = 6 molecules of CO.",
    },
    # ── oxidation-reduction ───────────────────────────────────────────
    {
        "id": "ks4-oxidation-reduction-e01",
        "subtopic_slug": "oxidation-reduction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to a substance that is oxidised, in terms "
                "of oxygen.",
        "options": [
            "It loses oxygen",
            "It passes its oxygen on to a metal",
            "It is broken apart by an electric current",
            "It gains oxygen",
        ],
        "correct_index": 3,
        "why": "In the oxygen definition, oxidation is gain of oxygen and "
               "reduction is loss of oxygen.",
    },
    {
        "id": "ks4-oxidation-reduction-e02",
        "subtopic_slug": "oxidation-reduction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the reaction 2Mg + O2 → 2MgO, state which substance is "
                "oxidised.",
        "options": [
            "Oxygen — it is used up during the reaction",
            "Magnesium — it gains oxygen to form the oxide",
            "Magnesium oxide — it is the product of the reaction",
            "Neither — burning is not a redox reaction",
        ],
        "correct_index": 1,
        "why": "The magnesium ends up combined with oxygen it did not have "
               "before, which is the definition of being oxidised.",
    },
    {
        "id": "ks4-oxidation-reduction-e03",
        "subtopic_slug": "oxidation-reduction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a reducing agent does to another substance.",
        "options": [
            "It takes oxygen away from it, or gives electrons to it",
            "It adds oxygen to it, or takes electrons from it",
            "It speeds the reaction up without being changed itself",
            "It dissolves it so that it forms a solution",
        ],
        "correct_index": 0,
        "why": "A reducing agent is the substance that causes reduction in "
               "something else, by handing over electrons or taking oxygen.",
    },
    {
        "id": "ks4-oxidation-reduction-e04",
        "subtopic_slug": "oxidation-reduction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the everyday process in which iron is oxidised.",
        "options": [
            "Melting iron in a furnace",
            "Hammering iron into a flat sheet",
            "Rusting of an iron gate left outdoors",
            "Cooling red-hot iron in a bucket of oil",
        ],
        "correct_index": 2,
        "why": "Rusting is iron combining with oxygen and water — a gain of "
               "oxygen, so oxidation.",
    },
    {
        "id": "ks4-oxidation-reduction-s01",
        "subtopic_slug": "oxidation-reduction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium burns in chlorine: 2Na + Cl2 → 2NaCl. State what "
                "happens to the chlorine, in terms of electrons.",
        "options": [
            "It is oxidised — each atom loses one electron",
            "It acts as the reducing agent, and is therefore oxidised",
            "It is reduced — each atom gains one electron",
            "It is unchanged — it takes no part in the electron transfer",
        ],
        "correct_index": 2,
        "why": "Each chlorine atom picks up an electron to become a chloride "
               "ion, and gain of electrons is reduction (RIG).",
    },
    {
        "id": "ks4-oxidation-reduction-s02",
        "subtopic_slug": "oxidation-reduction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Zinc is added to copper sulfate solution and copper is "
                "deposited. Identify the oxidising agent.",
        "options": [
            "The copper ions — they take electrons and are reduced",
            "The zinc — it gives away electrons and is reduced",
            "The sulfate ions — they carry the charge through the solution",
            "The water — it supplies the electrons for the transfer",
        ],
        "correct_index": 0,
        "why": "The copper ions are what cause the zinc to be oxidised, and "
               "they do so by accepting its electrons.",
    },
    {
        "id": "ks4-oxidation-reduction-s03",
        "subtopic_slug": "oxidation-reduction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says 'an oxidising agent must itself be oxidised'. "
                "Explain why this is wrong.",
        "options": [
            "It is right — the name tells you what happens to it",
            "An oxidising agent takes electrons from something else, so it is "
            "itself reduced",
            "An oxidising agent is completely unchanged by the reaction, so "
            "it is neither oxidised nor reduced itself",
            "An oxidising agent gives electrons away, so it is oxidised twice "
            "over",
        ],
        "correct_index": 1,
        "why": "The name describes what the substance does to its partner, "
               "not what happens to it — agents end up doing the opposite.",
    },
    {
        "id": "ks4-oxidation-reduction-s04",
        "subtopic_slug": "oxidation-reduction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hydrogen is passed over hot lead(II) oxide: PbO + H2 → Pb + "
                "H2O. Explain why this is described as a redox reaction.",
        "options": [
            "Because a metal and a non-metal both take part, and any reaction "
            "between those two types of element is called redox",
            "Because heat is needed before anything happens",
            "Because water is one of the products",
            "Because oxidation and reduction happen together — hydrogen gains "
            "oxygen while lead oxide loses it",
        ],
        "correct_index": 3,
        "why": "Oxygen has to go somewhere, so one substance is always "
               "oxidised in the same step that another is reduced.",
    },
    {
        "id": "ks4-oxidation-reduction-h01",
        "subtopic_slug": "oxidation-reduction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the reaction 2Na + Cl2 → 2NaCl, deduce how many electrons "
                "are transferred for each chlorine molecule that reacts.",
        "options": [
            "One electron in total",
            "Two electrons — one to each chlorine atom",
            "Four electrons — two to each chlorine atom",
            "None — the electrons are shared, not transferred",
        ],
        "correct_index": 1,
        "why": "A Cl2 molecule holds two atoms, and each becomes a Cl- ion by "
               "gaining a single electron from a sodium atom.",
    },
    {
        "id": "ks4-oxidation-reduction-h02",
        "subtopic_slug": "oxidation-reduction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the role of carbon in the blast furnace with the "
                "role of oxygen in rusting.",
        "options": [
            "Both are acting as reducing agents",
            "Both are acting as oxidising agents",
            "Carbon is the oxidising agent and oxygen is the reducing agent",
            "Carbon is the reducing agent and oxygen is the oxidising agent",
        ],
        "correct_index": 3,
        "why": "Carbon takes oxygen away from iron oxide, while oxygen adds "
               "itself to iron — opposite roles in the same redox picture.",
    },
    {
        "id": "ks4-oxidation-reduction-h03",
        "subtopic_slug": "oxidation-reduction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes 'a reducing agent gains electrons'. "
                "Identify the error and correct it.",
        "options": [
            "There is no error — reducing agents do gain electrons",
            "The only error is the word 'agent' — it should say 'reducing "
            "substance'",
            "A reducing agent loses electrons: it gives them away, and is "
            "itself oxidised",
            "A reducing agent neither gains nor loses electrons — it only "
            "moves oxygen about",
        ],
        "correct_index": 2,
        "why": "To reduce something else you must supply the electrons it "
               "gains, which means losing them yourself.",
    },
    {
        "id": "ks4-oxidation-reduction-h04",
        "subtopic_slug": "oxidation-reduction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the reaction Cl2 + 2KBr → 2KCl + Br2, predict which "
                "species is oxidised and justify the answer.",
        "options": [
            "The bromide ions — they lose electrons to become bromine",
            "The chlorine — it gains electrons to become chloride",
            "The potassium — it changes from an atom into an ion",
            "Nothing — this is a simple displacement, not a redox reaction",
        ],
        "correct_index": 0,
        "why": "Each Br- gives up an electron to a chlorine atom, and losing "
               "electrons is oxidation (OIL).",
    },
    # ── reactions-of-acids ────────────────────────────────────────────
    {
        "id": "ks4-reactions-of-acids-e01",
        "subtopic_slug": "reactions-of-acids",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the products formed when an acid reacts with a metal "
                "oxide.",
        "options": [
            "A salt and water",
            "A salt and hydrogen",
            "A salt, water and carbon dioxide",
            "A salt and oxygen",
        ],
        "correct_index": 0,
        "why": "A metal oxide is a base, so it neutralises the acid to give a "
               "salt and water and nothing else.",
    },
    {
        "id": "ks4-reactions-of-acids-e02",
        "subtopic_slug": "reactions-of-acids",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gas that gives a squeaky pop when a lit splint is "
                "held to it.",
        "options": [
            "Carbon dioxide",
            "Oxygen",
            "Chlorine",
            "Hydrogen",
        ],
        "correct_index": 3,
        "why": "The pop is a tiny explosion as hydrogen burns in the air to "
               "form water.",
    },
    {
        "id": "ks4-reactions-of-acids-e03",
        "subtopic_slug": "reactions-of-acids",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the salt produced when nitric acid reacts with "
                "potassium hydroxide.",
        "options": [
            "Potassium chloride",
            "Potassium nitrate",
            "Potassium sulfate",
            "Potassium oxide",
        ],
        "correct_index": 1,
        "why": "The salt takes the metal from the alkali and the negative ion "
               "from the acid, and nitric acid always gives nitrates.",
    },
    {
        "id": "ks4-reactions-of-acids-e04",
        "subtopic_slug": "reactions-of-acids",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the laboratory test for carbon dioxide.",
        "options": [
            "It relights a glowing splint",
            "It bleaches damp litmus paper",
            "It turns limewater milky",
            "It gives a squeaky pop with a lit splint",
        ],
        "correct_index": 2,
        "why": "Carbon dioxide reacts with the calcium hydroxide in limewater "
               "to make a cloudy suspension of calcium carbonate.",
    },
    {
        "id": "ks4-reactions-of-acids-s01",
        "subtopic_slug": "reactions-of-acids",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Black copper(II) oxide powder is stirred into warm dilute "
                "sulfuric acid. Describe what is observed.",
        "options": [
            "Vigorous fizzing as hydrogen gas is released",
            "The powder floats and the liquid stays colourless",
            "The powder dissolves and the solution turns blue",
            "A thick white precipitate forms straight away",
        ],
        "correct_index": 2,
        "why": "The copper oxide is neutralised to copper sulfate, which is "
               "blue in solution, and no gas is made by an oxide and an acid.",
    },
    {
        "id": "ks4-reactions-of-acids-s02",
        "subtopic_slug": "reactions-of-acids",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the correctly balanced equation for calcium "
                "carbonate reacting with hydrochloric acid.",
        "options": [
            "CaCO3 + HCl → CaCl2 + H2O + CO2",
            "CaCO3 + 2HCl → CaCl2 + H2O + CO2",
            "CaCO3 + 2HCl → CaCl + H2O + CO2",
            "CaCO3 + 2HCl → CaCl2 + H2 + CO2",
        ],
        "correct_index": 1,
        "why": "Calcium forms a 2+ ion so it needs two chlorides, which means "
               "two molecules of HCl.",
    },
    {
        "id": "ks4-reactions-of-acids-s03",
        "subtopic_slug": "reactions-of-acids",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium carbonate solution is added to dilute nitric acid "
                "until the fizzing stops. Name the salt formed.",
        "options": [
            "Sodium nitrite",
            "Sodium carbonate",
            "Sodium chloride",
            "Sodium nitrate",
        ],
        "correct_index": 3,
        "why": "The sodium comes from the carbonate and the nitrate from the "
               "acid, giving Na2CO3 + 2HNO3 → 2NaNO3 + H2O + CO2.",
    },
    {
        "id": "ks4-reactions-of-acids-s04",
        "subtopic_slug": "reactions-of-acids",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A technician needs to make iron(II) sulfate. Choose the "
                "correct pair of starting materials.",
        "options": [
            "Iron and dilute sulfuric acid",
            "Iron and dilute hydrochloric acid",
            "Iron oxide and dilute nitric acid",
            "Sulfur and dilute sulfuric acid",
        ],
        "correct_index": 0,
        "why": "The metal supplies the iron and sulfuric acid supplies the "
               "sulfate: Fe + H2SO4 → FeSO4 + H2.",
    },
    {
        "id": "ks4-reactions-of-acids-h01",
        "subtopic_slug": "reactions-of-acids",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student adds dilute nitric acid to magnesium carbonate and "
                "reports that the only products are magnesium nitrate and "
                "hydrogen. Identify what is wrong with the report.",
        "options": [
            "Nothing is wrong — carbonates release hydrogen with acids",
            "The gas is carbon dioxide, not hydrogen, and water is also "
            "formed",
            "The salt should be magnesium nitrite rather than the nitrate",
            "No reaction happens at all, because carbonates are unreactive",
        ],
        "correct_index": 1,
        "why": "An acid and a carbonate always give three products — salt, "
               "water and carbon dioxide — and hydrogen is not one of them.",
    },
    {
        "id": "ks4-reactions-of-acids-h02",
        "subtopic_slug": "reactions-of-acids",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the formula of the salt formed when aluminium "
                "oxide reacts with dilute hydrochloric acid.",
        "options": [
            "AlCl3",
            "AlCl2",
            "Al2Cl3",
            "AlCl",
        ],
        "correct_index": 0,
        "why": "Aluminium forms a 3+ ion and chloride is 1-, so three "
               "chlorides balance one aluminium: Al2O3 + 6HCl → 2AlCl3 + "
               "3H2O.",
    },
    {
        "id": "ks4-reactions-of-acids-h03",
        "subtopic_slug": "reactions-of-acids",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what is observed when dilute hydrochloric acid is "
                "added to magnesium ribbon and to magnesium carbonate powder.",
        "options": [
            "Both fizz, and the gas from each of them gives the same squeaky "
            "pop when a lit splint is held to it",
            "Neither fizzes; both solids simply dissolve away",
            "Both fizz, but only the ribbon gives hydrogen — the carbonate "
            "gives carbon dioxide",
            "Only the ribbon fizzes; the carbonate dissolves with no gas",
        ],
        "correct_index": 2,
        "why": "The same acid gives different gases with a metal and with a "
               "carbonate, so the gas test is what tells them apart.",
    },
    {
        "id": "ks4-reactions-of-acids-h04",
        "subtopic_slug": "reactions-of-acids",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Dilute hydrochloric acid is poured onto excess zinc oxide "
                "powder. Explain why no bubbles are seen, even though the "
                "powder dissolves.",
        "options": [
            "Zinc oxide is insoluble, so nothing actually reacts",
            "Zinc lies below hydrogen in the reactivity series, so it cannot "
            "release any hydrogen from the acid",
            "The acid is too dilute to react with any metal oxide",
            "An acid and a metal oxide give only a salt and water — there is "
            "no gaseous product",
        ],
        "correct_index": 3,
        "why": "The oxygen in the oxide ends up in the water, so nothing is "
               "left over to leave as a gas.",
    },
    # ── salts-neutralisation ──────────────────────────────────────────
    {
        "id": "ks4-salts-neutralisation-e01",
        "subtopic_slug": "salts-neutralisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the first step in making copper sulfate crystals from "
                "copper oxide and dilute sulfuric acid.",
        "options": [
            "Filter the sulfuric acid to remove any impurities",
            "Evaporate the acid first, so that it becomes concentrated enough "
            "to react",
            "Warm the acid and stir in copper oxide until no more dissolves",
            "Add a few drops of indicator to the acid",
        ],
        "correct_index": 2,
        "why": "Adding solid until no more will dissolve is how you know all "
               "the acid has been used up.",
    },
    {
        "id": "ks4-salts-neutralisation-e02",
        "subtopic_slug": "salts-neutralisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the apparatus used to separate the unreacted solid from "
                "the salt solution.",
        "options": [
            "A burette and stand",
            "A filter funnel and filter paper",
            "A pipette and safety filler",
            "A measuring cylinder",
        ],
        "correct_index": 1,
        "why": "Filtration holds back the undissolved solid while the "
               "dissolved salt passes through with the liquid.",
    },
    {
        "id": "ks4-salts-neutralisation-e03",
        "subtopic_slug": "salts-neutralisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how an insoluble salt is made in the laboratory.",
        "options": [
            "By mixing two solutions so that the salt precipitates out",
            "By evaporating a solution of the salt to dryness",
            "By adding excess metal to an acid and then filtering",
            "By electrolysing the molten compound",
        ],
        "correct_index": 0,
        "why": "An insoluble salt will never crystallise from solution, so it "
               "has to be thrown out of solution as a precipitate instead.",
    },
    {
        "id": "ks4-salts-neutralisation-e04",
        "subtopic_slug": "salts-neutralisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these substances is an alkali.",
        "options": [
            "Copper oxide",
            "Calcium carbonate",
            "Iron(III) oxide",
            "Sodium hydroxide",
        ],
        "correct_index": 3,
        "why": "An alkali is a base that dissolves in water, and sodium "
               "hydroxide dissolves to release hydroxide ions.",
    },
    {
        "id": "ks4-salts-neutralisation-s01",
        "subtopic_slug": "salts-neutralisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the copper sulfate preparation, explain why the filtrate "
                "is kept and the residue thrown away.",
        "options": [
            "The residue left on the paper is the salt, and the filtrate that "
            "runs through is only the leftover waste acid",
            "Both contain the salt, so either one can be used",
            "The residue holds the water that has to be evaporated off",
            "The salt is dissolved, so it passes through the paper with the "
            "liquid while unreacted solid is held back",
        ],
        "correct_index": 3,
        "why": "Filtration separates by whether something is dissolved, and "
               "the salt you want is in solution.",
    },
    {
        "id": "ks4-salts-neutralisation-s02",
        "subtopic_slug": "salts-neutralisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how good crystals of copper sulfate are obtained "
                "from copper sulfate solution.",
        "options": [
            "Evaporate some of the water, then leave the solution to "
            "crystallise slowly",
            "Boil the solution to complete dryness as quickly as possible "
            "over a strong flame",
            "Add more sulfuric acid until crystals appear",
            "Filter the solution a second time to collect the crystals",
        ],
        "correct_index": 0,
        "why": "Slow crystallisation lets the ions arrange into large regular "
               "crystals, while boiling dry just leaves a powder.",
    },
    {
        "id": "ks4-salts-neutralisation-s03",
        "subtopic_slug": "salts-neutralisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name two solutions that can be mixed to precipitate barium "
                "sulfate.",
        "options": [
            "Barium sulfate solution and sodium chloride solution",
            "Barium nitrate solution and sodium carbonate solution",
            "Barium chloride solution and sodium sulfate solution",
            "Barium hydroxide solution and sodium chloride solution",
        ],
        "correct_index": 2,
        "why": "One solution must supply barium ions and the other sulfate "
               "ions: BaCl2 + Na2SO4 → BaSO4 + 2NaCl.",
    },
    {
        "id": "ks4-salts-neutralisation-s04",
        "subtopic_slug": "salts-neutralisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a precipitate is washed with distilled water "
                "before it is dried.",
        "options": [
            "To dissolve away any of the precipitate that is impure",
            "To rinse off the soluble salt left behind from the mixture",
            "To cool it so that it does not decompose in the oven",
            "To turn it into its hydrated form before weighing",
        ],
        "correct_index": 1,
        "why": "The other product stays dissolved in the liquid clinging to "
               "the solid, and washing removes it without dissolving the "
               "insoluble salt.",
    },
    {
        "id": "ks4-salts-neutralisation-h01",
        "subtopic_slug": "salts-neutralisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the excess-solid method cannot be used to make "
                "sodium chloride from sodium hydroxide and hydrochloric acid.",
        "options": [
            "Both reactants are soluble, so any excess cannot be filtered off",
            "Sodium chloride is insoluble, so it would never crystallise",
            "Sodium hydroxide is not a base, so it cannot neutralise the acid",
            "The reaction is far too slow for the method to work",
        ],
        "correct_index": 0,
        "why": "The method depends on being able to see and remove the "
               "leftover solid, which is impossible if it dissolves.",
    },
    {
        "id": "ks4-salts-neutralisation-h02",
        "subtopic_slug": "salts-neutralisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student prepares zinc sulfate by adding excess zinc powder "
                "to dilute sulfuric acid and then evaporating the mixture. "
                "The dried product is white crystals mixed with grey powder. "
                "Suggest what went wrong.",
        "options": [
            "The solution was evaporated far too slowly",
            "Too much sulfuric acid was used at the start",
            "The crystals were washed with distilled water, which dissolved "
            "part of the product away",
            "The mixture was not filtered, so unreacted zinc was left in it",
        ],
        "correct_index": 3,
        "why": "Excess solid must be filtered off before evaporating, or it "
               "simply dries out alongside the crystals.",
    },
    {
        "id": "ks4-salts-neutralisation-h03",
        "subtopic_slug": "salts-neutralisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the same ionic equation describes both nitric "
                "acid neutralised by potassium hydroxide and sulfuric acid "
                "neutralised by sodium hydroxide.",
        "options": [
            "Because both of the salts formed are soluble in water",
            "Because in every case it is hydrogen ions joining hydroxide ions "
            "to make water",
            "Because both of the acids contain exactly the same number of "
            "hydrogen atoms in each molecule",
            "Because the two metals involved form ions of the same charge",
        ],
        "correct_index": 1,
        "why": "Neutralisation is always H+ + OH- → H2O; only the ions that "
               "are left dissolved change from one pair to the next.",
    },
    {
        "id": "ks4-salts-neutralisation-h04",
        "subtopic_slug": "salts-neutralisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Silver nitrate solution is added to sodium chloride "
                "solution. Predict the colour of the precipitate and name the "
                "substance left in solution.",
        "options": [
            "A yellow precipitate, leaving silver metal in solution",
            "A blue precipitate of silver hydroxide, leaving sodium hydroxide "
            "dissolved in the solution",
            "A white precipitate of silver chloride, leaving sodium nitrate "
            "in solution",
            "A black precipitate, leaving nitric acid in solution",
        ],
        "correct_index": 2,
        "why": "Silver chloride is insoluble and white, so it drops out while "
               "the sodium and nitrate ions stay dissolved.",
    },
    # ── ph-scale ──────────────────────────────────────────────────────
    {
        "id": "ks4-ph-scale-e01",
        "subtopic_slug": "ph-scale",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the pH of a neutral solution.",
        "options": [
            "0",
            "7",
            "14",
            "1",
        ],
        "correct_index": 1,
        "why": "At pH 7 the numbers of hydrogen ions and hydroxide ions are "
               "equal, which is what neutral means.",
    },
    {
        "id": "ks4-ph-scale-e02",
        "subtopic_slug": "ph-scale",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the colour universal indicator turns in a strongly "
                "alkaline solution.",
        "options": [
            "Red",
            "Green",
            "Purple",
            "Orange",
        ],
        "correct_index": 2,
        "why": "Universal indicator runs red through green to purple as pH "
               "rises, so the top of the scale is purple.",
    },
    {
        "id": "ks4-ph-scale-e03",
        "subtopic_slug": "ph-scale",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the colour of phenolphthalein in an acidic solution.",
        "options": [
            "Pink",
            "Yellow",
            "Blue",
            "Colourless",
        ],
        "correct_index": 3,
        "why": "Phenolphthalein is colourless in acid and pink in alkali, "
               "which is why the end point is so easy to see.",
    },
    {
        "id": "ks4-ph-scale-e04",
        "subtopic_slug": "ph-scale",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the method that gives the most precise numerical "
                "value for pH.",
        "options": [
            "A pH probe connected to a meter",
            "Universal indicator paper",
            "Red litmus paper",
            "A thermometer placed in the solution",
        ],
        "correct_index": 0,
        "why": "A meter reads a number directly, while an indicator only "
               "matches a colour to a range.",
    },
    {
        "id": "ks4-ph-scale-s01",
        "subtopic_slug": "ph-scale",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A solution turns red litmus paper blue. Deduce a likely pH "
                "for it.",
        "options": [
            "pH 11",
            "pH 7",
            "pH 4",
            "pH 1",
        ],
        "correct_index": 0,
        "why": "Red litmus only turns blue in an alkali, so the pH must be "
               "above 7.",
    },
    {
        "id": "ks4-ph-scale-s02",
        "subtopic_slug": "ph-scale",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what a pH value actually measures.",
        "options": [
            "The total number of ions of every kind in the solution",
            "How strongly the bonds inside the acid are held together",
            "The mass of acid dissolved in each cubic decimetre",
            "The concentration of hydrogen ions in the solution",
        ],
        "correct_index": 3,
        "why": "pH is a scale of hydrogen ion concentration, which is why a "
               "low pH always means a lot of H+ ions.",
    },
    {
        "id": "ks4-ph-scale-s03",
        "subtopic_slug": "ph-scale",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the pH changes as sodium hydroxide solution is "
                "slowly added to dilute hydrochloric acid.",
        "options": [
            "It stays at 7 the whole time",
            "It falls steadily from 7 down to 1",
            "It rises slowly at first, changes sharply near the end point, "
            "then rises slowly again",
            "It rises smoothly and evenly from 1 up to 14, in equal steps for "
            "every drop of alkali added",
        ],
        "correct_index": 2,
        "why": "Almost all of the change happens in the last drops, when "
               "there is very little acid left to soak up the added "
               "hydroxide.",
    },
    {
        "id": "ks4-ph-scale-s04",
        "subtopic_slug": "ph-scale",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Universal indicator turns orange in a solution. Identify "
                "which of these it is most likely to be.",
        "options": [
            "Sodium hydroxide solution",
            "Vinegar",
            "Pure water",
            "Limewater",
        ],
        "correct_index": 1,
        "why": "Orange sits at the acidic end of the indicator's range, and "
               "vinegar is a dilute acid at about pH 3.",
    },
    {
        "id": "ks4-ph-scale-h01",
        "subtopic_slug": "ph-scale",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The hydrogen ion concentration of an acid is reduced to one "
                "hundredth of its original value. Determine the change in pH.",
        "options": [
            "It falls by 2 units",
            "It falls by 100 units",
            "It rises by 100 units",
            "It rises by 2 units",
        ],
        "correct_index": 3,
        "why": "Each pH unit is a factor of ten in H+ concentration, so "
               "dividing by 100 raises the pH by 2.",
    },
    {
        "id": "ks4-ph-scale-h02",
        "subtopic_slug": "ph-scale",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why adding water to an alkali makes its pH fall "
                "towards 7.",
        "options": [
            "Water is very slightly acidic, so adding it neutralises some of "
            "the alkali present",
            "The hydroxide ions are spread through more water, so their "
            "concentration falls",
            "Water reacts with the alkali to form a salt and hydrogen",
            "The alkali decomposes as soon as it is diluted",
        ],
        "correct_index": 1,
        "why": "Dilution does not destroy the ions, it just spreads the same "
               "number of them through a larger volume.",
    },
    {
        "id": "ks4-ph-scale-h03",
        "subtopic_slug": "ph-scale",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student states that 'any solution with pH 7 must be pure "
                "water'. Evaluate this statement.",
        "options": [
            "Wrong — a sodium chloride solution is also neutral at pH 7",
            "Correct — only pure water can ever be exactly neutral",
            "Wrong — pure water is actually pH 6, not pH 7",
            "Correct — every other solution is either an acid or an alkali",
        ],
        "correct_index": 0,
        "why": "pH 7 only means the H+ and OH- concentrations are equal, and "
               "plenty of salt solutions meet that condition.",
    },
    {
        "id": "ks4-ph-scale-h04",
        "subtopic_slug": "ph-scale",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the pH changes so sharply just before the end "
                "point when acid is added to an alkali.",
        "options": [
            "The indicator itself starts to react with the acid",
            "The temperature rises suddenly, which changes the pH",
            "Almost no hydroxide ions are left, so each further drop of acid "
            "makes a large change to the H+ concentration",
            "The salt that has just been formed begins to behave as an acid "
            "of its own, which pushes the pH down very suddenly",
        ],
        "correct_index": 2,
        "why": "While there is plenty of hydroxide left it mops up the added "
               "H+; once it runs out, the H+ concentration climbs quickly.",
    },
    # ── titrations (TRIPLE ONLY) ──────────────────────────────────────
    {
        "id": "ks4-titrations-e01",
        "subtopic_slug": "titrations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the apparatus used to transfer an exact 25.00 cm3 "
                "volume of alkali into the conical flask.",
        "options": [
            "A burette",
            "A measuring cylinder",
            "A beaker",
            "A pipette",
        ],
        "correct_index": 3,
        "why": "A pipette is made to deliver one fixed volume very "
               "accurately, which is why the alkali is measured with it.",
    },
    {
        "id": "ks4-titrations-e02",
        "subtopic_slug": "titrations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the colour of methyl orange in an alkaline solution.",
        "options": [
            "Red",
            "Colourless",
            "Yellow",
            "Purple",
        ],
        "correct_index": 2,
        "why": "Methyl orange is yellow in alkali and red in acid, so the end "
               "point is a clear yellow-to-red change.",
    },
    {
        "id": "ks4-titrations-e03",
        "subtopic_slug": "titrations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why a white tile is placed under the conical flask.",
        "options": [
            "To stop the conical flask sliding across the bench while it is "
            "being swirled",
            "To make the indicator's colour change easier to see",
            "To insulate the flask from the cold bench",
            "To catch any acid that is spilled",
        ],
        "correct_index": 1,
        "why": "A plain white background makes the first permanent tinge of "
               "colour obvious, so the end point is not overshot.",
    },
    {
        "id": "ks4-titrations-e04",
        "subtopic_slug": "titrations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how the titre is worked out from the burette readings.",
        "options": [
            "Final reading minus initial reading",
            "Initial reading minus final reading",
            "Final reading plus initial reading",
            "The volume of alkali placed in the flask",
        ],
        "correct_index": 0,
        "why": "The burette scale runs downwards as liquid leaves it, so the "
               "volume delivered is the increase in the reading.",
    },
    {
        "id": "ks4-titrations-s01",
        "subtopic_slug": "titrations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A burette reads 1.20 cm3 at the start of a titration and "
                "26.75 cm3 at the end. Calculate the titre.",
        "options": [
            "27.95 cm3",
            "25.55 cm3",
            "26.75 cm3",
            "24.55 cm3",
        ],
        "correct_index": 1,
        "why": "The titre is the difference between the two readings: 26.75 − "
               "1.20 = 25.55 cm3.",
    },
    {
        "id": "ks4-titrations-s02",
        "subtopic_slug": "titrations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the burette is rinsed with the acid before it is "
                "filled with acid.",
        "options": [
            "Any water left inside would dilute the acid, making the titre "
            "too large",
            "Rinsing with the acid is the only reliable way to clear air "
            "bubbles out of the burette tap",
            "Rinsing warms the glass so the acid runs out evenly",
            "Water would react with the acid and give out heat",
        ],
        "correct_index": 0,
        "why": "Diluted acid contains less acid per cm3, so more of it is "
               "needed to reach the end point and the titre reads high.",
    },
    {
        "id": "ks4-titrations-s03",
        "subtopic_slug": "titrations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what is meant by the end point of an acid-alkali "
                "titration.",
        "options": [
            "The moment the solution first shows any trace of colour change",
            "The point at which the burette has been completely emptied",
            "The point at which the indicator has faded away entirely",
            "The point at which one further drop causes a permanent colour "
            "change",
        ],
        "correct_index": 3,
        "why": "A colour that swirls away has not reached the end point; only "
               "a change that stays shows the reaction is complete.",
    },
    {
        "id": "ks4-titrations-s04",
        "subtopic_slug": "titrations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a rough titration is carried out before the "
                "accurate runs.",
        "options": [
            "It is the only way to rinse the burette with acid",
            "It brings the acid and the alkali to exactly the same "
            "temperature before the accurate runs begin",
            "It finds the approximate titre, so later runs can be slowed to "
            "dropwise near that volume",
            "It checks that the indicator has not gone off",
        ],
        "correct_index": 2,
        "why": "Knowing roughly where the end point falls means the acid can "
               "be run in quickly at first and dropwise only where it "
               "matters.",
    },
    {
        "id": "ks4-titrations-h01",
        "subtopic_slug": "titrations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student's four titres are 23.10, 23.85, 23.15 and 23.05 "
                "cm3. Calculate the mean titre that should be reported.",
        "options": [
            "23.29 cm3",
            "23.15 cm3",
            "23.10 cm3",
            "23.85 cm3",
        ],
        "correct_index": 2,
        "why": "Only the three concordant values are averaged: (23.10 + 23.15 "
               "+ 23.05) ÷ 3 = 23.10 cm3.",
    },
    {
        "id": "ks4-titrations-h02",
        "subtopic_slug": "titrations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student rinses the pipette with distilled water and does "
                "not dry it before measuring out the alkali. Predict the "
                "effect on the titre.",
        "options": [
            "No effect, because water is neutral",
            "The titre is too large, because the water left behind has made "
            "the alkali more concentrated",
            "The titre is unchanged, but the result is less precise",
            "The titre is too small, because the alkali has been diluted so "
            "less acid is needed",
        ],
        "correct_index": 3,
        "why": "The pipette delivers the same volume of liquid but less "
               "alkali in it, so less acid is needed to neutralise it.",
    },
    {
        "id": "ks4-titrations-h03",
        "subtopic_slug": "titrations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "During a titration the conical flask is never swirled. "
                "Explain why this makes the end point unreliable.",
        "options": [
            "The acid and alkali do not mix, so the indicator changes colour "
            "locally before the whole flask has reacted",
            "Swirling is only needed to keep the solution warm enough",
            "Without swirling, the indicator sinks and settles at the bottom "
            "of the flask, where its colour change cannot be seen",
            "The reaction stops completely unless the solution is moving",
        ],
        "correct_index": 0,
        "why": "A patch of colour where the acid lands is not the end point — "
               "only a fully mixed flask tells you the alkali is used up.",
    },
    {
        "id": "ks4-titrations-h04",
        "subtopic_slug": "titrations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two students obtain mean titres of 24.50 cm3 and 24.55 cm3 "
                "for the same pair of solutions. Evaluate whether their "
                "results agree.",
        "options": [
            "No — any difference at all means one of them is wrong",
            "Yes — they differ by 0.05 cm3, which is inside the 0.10 cm3 used "
            "to judge concordance",
            "No — two mean titres have to match to the nearest 0.01 cm3 "
            "before they can be said to agree",
            "Yes — but only because both values happen to be above 24 cm3",
        ],
        "correct_index": 1,
        "why": "A burette can only be read to about ±0.05 cm3, so a gap this "
               "small is within the uncertainty of the measurement.",
    },
    # ── electrolysis-principles ───────────────────────────────────────
    {
        "id": "ks4-electrolysis-principles-e01",
        "subtopic_slug": "electrolysis-principles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by an electrolyte.",
        "options": [
            "An ionic compound that is molten or dissolved, so its ions can "
            "move",
            "Any liquid that will conduct heat well",
            "The metal wire that joins the electrodes to the supply",
            "A solid whose lattice carries electrons from one electrode to "
            "the other",
        ],
        "correct_index": 0,
        "why": "Electrolysis needs charged particles that can travel to the "
               "electrodes, and only molten or dissolved ionic compounds have "
               "them.",
    },
    {
        "id": "ks4-electrolysis-principles-e02",
        "subtopic_slug": "electrolysis-principles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the electrode that is connected to the negative "
                "terminal of the power supply.",
        "options": [
            "The anode",
            "The cathode",
            "The electrolyte",
            "The anion",
        ],
        "correct_index": 1,
        "why": "The cathode is the negative electrode, which is why positive "
               "ions are drawn to it.",
    },
    {
        "id": "ks4-electrolysis-principles-e03",
        "subtopic_slug": "electrolysis-principles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the pair of materials commonly used as inert "
                "electrodes.",
        "options": [
            "Copper and zinc",
            "Iron and lead",
            "Sodium and calcium",
            "Graphite and platinum",
        ],
        "correct_index": 3,
        "why": "Graphite and platinum conduct well but do not react, so the "
               "products come only from the electrolyte.",
    },
    {
        "id": "ks4-electrolysis-principles-e04",
        "subtopic_slug": "electrolysis-principles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which type of ion travels towards the anode.",
        "options": [
            "Positive ions, which are called cations",
            "Both positive and negative ions equally",
            "Negative ions, which are called anions",
            "Neither — only electrons move through the electrolyte",
        ],
        "correct_index": 2,
        "why": "The anode is positive, so it attracts the negatively charged "
               "ions.",
    },
    {
        "id": "ks4-electrolysis-principles-s01",
        "subtopic_slug": "electrolysis-principles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a direct current supply, rather than an "
                "alternating one, is used for electrolysis.",
        "options": [
            "Alternating current would heat the electrolyte far too much and "
            "boil it away before anything was made",
            "Alternating current cannot pass through a solution at all",
            "Direct current is the only kind that can create ions",
            "Each electrode must keep a fixed charge, so that every ion "
            "always travels to the same electrode",
        ],
        "correct_index": 3,
        "why": "If the charges swapped over many times a second the products "
               "would form and be undone at each electrode in turn.",
    },
    {
        "id": "ks4-electrolysis-principles-s02",
        "subtopic_slug": "electrolysis-principles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to positive ions when they reach the "
                "cathode.",
        "options": [
            "They lose electrons and are oxidised",
            "They lose electrons and are reduced",
            "They gain electrons and are reduced",
            "They gain electrons and are oxidised",
        ],
        "correct_index": 2,
        "why": "The cathode supplies electrons, and gaining electrons is "
               "reduction — RED CAT.",
    },
    {
        "id": "ks4-electrolysis-principles-s03",
        "subtopic_slug": "electrolysis-principles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why inert electrodes are chosen for most "
                "electrolysis experiments.",
        "options": [
            "They take no part, so the products come only from the "
            "electrolyte",
            "They conduct electricity better than any reactive metal does",
            "They dissolve slowly and so replace the ions that are used up",
            "They stop the electrolyte from becoming hot",
        ],
        "correct_index": 0,
        "why": "A reactive electrode would join in and change what is made, "
               "so an inert one keeps the result predictable.",
    },
    {
        "id": "ks4-electrolysis-principles-s04",
        "subtopic_slug": "electrolysis-principles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A copper anode is used instead of a graphite one in copper "
                "sulfate solution. Describe what happens to that anode.",
        "options": [
            "It stays exactly the same throughout",
            "It gradually dissolves as copper enters the solution",
            "It becomes coated with a fresh layer of copper",
            "It turns into copper oxide, which flakes away",
        ],
        "correct_index": 1,
        "why": "A reactive anode is itself oxidised, so its own atoms lose "
               "electrons and go into solution as copper ions.",
    },
    {
        "id": "ks4-electrolysis-principles-h01",
        "subtopic_slug": "electrolysis-principles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict whether molten sugar could be electrolysed, and "
                "justify the prediction.",
        "options": [
            "Yes — any substance that has been melted will conduct, because "
            "melting always frees its particles",
            "No — sugar is a covalent substance, so it has no ions to carry "
            "the charge",
            "Yes — but only if graphite electrodes are used",
            "No — sugar melts at too low a temperature for the current",
        ],
        "correct_index": 1,
        "why": "Electrolysis needs mobile ions, and a molecular covalent "
               "substance has none however hot it is.",
    },
    {
        "id": "ks4-electrolysis-principles-h02",
        "subtopic_slug": "electrolysis-principles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the cathode must be positive, because "
                "positive ions are attracted to it. Identify the error.",
        "options": [
            "The cathode is negative — that is exactly why positive ions are "
            "attracted to it",
            "The cathode is positive, and it attracts the negative ions",
            "There is no error — the cathode is the positive electrode",
            "The cathode carries no charge at all, so the ions simply drift "
            "about the solution at random",
        ],
        "correct_index": 0,
        "why": "Opposite charges attract, so it is the cathode's negative "
               "charge that pulls the positive ions in.",
    },
    {
        "id": "ks4-electrolysis-principles-h03",
        "subtopic_slug": "electrolysis-principles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a graphite anode keeps its mass during "
                "electrolysis while a copper anode loses mass.",
        "options": [
            "Graphite is much denser, so any loss is too small to measure",
            "Graphite is not truly part of the circuit, and so no reaction "
            "can take place at its surface, however long the current is left "
            "running",
            "Graphite does not react — ions from the electrolyte discharge on "
            "its surface, while copper atoms themselves go into solution",
            "Copper conducts better, so a larger current passes and wears it "
            "away",
        ],
        "correct_index": 2,
        "why": "An inert electrode only lends its surface; a reactive one is "
               "part of the reaction.",
    },
    {
        "id": "ks4-electrolysis-principles-h04",
        "subtopic_slug": "electrolysis-principles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A steel spoon is silver-plated using a silver anode in "
                "silver nitrate solution. Explain why the concentration of "
                "silver ions in the solution stays roughly constant.",
        "options": [
            "The power supply itself creates fresh silver ions in the "
            "solution at exactly the rate they are used up",
            "The solution is topped up automatically as it is used",
            "Silver nitrate does not ionise, so its concentration cannot "
            "change",
            "As fast as silver ions are deposited on the spoon, the silver "
            "anode dissolves to replace them",
        ],
        "correct_index": 3,
        "why": "The reactive anode puts ions back into the solution at the "
               "same rate the cathode takes them out.",
    },
    # ── electrolysis-molten ───────────────────────────────────────────
    {
        "id": "ks4-electrolysis-molten-e01",
        "subtopic_slug": "electrolysis-molten",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is always produced at the cathode when a molten "
                "ionic compound is electrolysed.",
        "options": [
            "A non-metal gas",
            "Oxygen",
            "The metal",
            "The compound, completely unchanged",
        ],
        "correct_index": 2,
        "why": "The metal ions are the positive ones, so they are the ones "
               "drawn to the negative cathode and discharged there.",
    },
    {
        "id": "ks4-electrolysis-molten-e02",
        "subtopic_slug": "electrolysis-molten",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the product formed at the anode when molten lead(II) "
                "bromide is electrolysed.",
        "options": [
            "Lead",
            "Hydrogen",
            "Oxygen",
            "Bromine",
        ],
        "correct_index": 3,
        "why": "Bromide ions are the only negative ions present, so bromine "
               "is released at the positive anode.",
    },
    {
        "id": "ks4-electrolysis-molten-e03",
        "subtopic_slug": "electrolysis-molten",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the colour of the vapour seen at the anode during the "
                "electrolysis of molten lead(II) bromide.",
        "options": [
            "Yellow-green",
            "Red-brown",
            "Colourless",
            "Lilac",
        ],
        "correct_index": 1,
        "why": "Bromine is a red-brown liquid whose vapour has the same "
               "colour; yellow-green would be chlorine.",
    },
    {
        "id": "ks4-electrolysis-molten-e04",
        "subtopic_slug": "electrolysis-molten",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why the electrolysis of molten lead(II) bromide is "
                "carried out in a fume cupboard.",
        "options": [
            "The bromine vapour produced is toxic",
            "The lead produced is radioactive",
            "The hydrogen produced is explosive",
            "The apparatus becomes uncomfortably hot",
        ],
        "correct_index": 0,
        "why": "Bromine vapour is harmful to breathe, so it must be drawn "
               "away from the room.",
    },
    {
        "id": "ks4-electrolysis-molten-s01",
        "subtopic_slug": "electrolysis-molten",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the products of electrolysing molten potassium "
                "iodide.",
        "options": [
            "Potassium at the cathode and iodine at the anode",
            "Iodine at the cathode and potassium at the anode",
            "Hydrogen at the cathode and oxygen at the anode",
            "Nothing — potassium iodide cannot be decomposed",
        ],
        "correct_index": 0,
        "why": "The only ions present are K+ and I-, so the metal goes to the "
               "negative cathode and the non-metal to the positive anode.",
    },
    {
        "id": "ks4-electrolysis-molten-s02",
        "subtopic_slug": "electrolysis-molten",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why hydrogen is never one of the products when a "
                "molten ionic compound is electrolysed.",
        "options": [
            "Hydrogen ions are too small to be discharged at an electrode",
            "There is no water present, so there are no hydrogen ions",
            "Hydrogen is a gas and cannot form in a very hot melt",
            "Hydrogen is produced, but it escapes before it can be collected",
        ],
        "correct_index": 1,
        "why": "Only the ions of the compound itself are present in a melt, "
               "and none of them is a hydrogen ion.",
    },
    {
        "id": "ks4-electrolysis-molten-s03",
        "subtopic_slug": "electrolysis-molten",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Molten magnesium chloride is electrolysed. Determine the "
                "ratio of magnesium atoms to chlorine molecules produced.",
        "options": [
            "2 : 1",
            "1 : 2",
            "1 : 1",
            "2 : 3",
        ],
        "correct_index": 2,
        "why": "MgCl2 supplies one Mg2+ and two Cl- ions, and two chloride "
               "ions make a single Cl2 molecule.",
    },
    {
        "id": "ks4-electrolysis-molten-s04",
        "subtopic_slug": "electrolysis-molten",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the mass of the electrolyte during the "
                "electrolysis of molten lead(II) bromide, and explain why.",
        "options": [
            "It increases, because the bromine dissolves back into the melt",
            "It stays the same, because nothing leaves the container",
            "It increases, because the electrodes add material to the melt",
            "It decreases, because lead is deposited and bromine leaves as "
            "vapour",
        ],
        "correct_index": 3,
        "why": "Both elements are removed from the melt — one as a metal on "
               "the electrode and one as a gas.",
    },
    {
        "id": "ks4-electrolysis-molten-h01",
        "subtopic_slug": "electrolysis-molten",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Molten sodium chloride and molten magnesium chloride are "
                "electrolysed separately, and the same total charge is passed "
                "through each. Compare the number of metal atoms produced at "
                "the two cathodes.",
        "options": [
            "The same number, because each of the two compounds holds just "
            "one metal ion in every formula unit",
            "More magnesium, because each magnesium ion carries two charges",
            "No magnesium at all, because magnesium is too reactive to be "
            "deposited",
            "More sodium, because each sodium ion needs only one electron "
            "while each magnesium ion needs two",
        ],
        "correct_index": 3,
        "why": "A 2+ ion must be given twice as much charge as a 1+ ion to "
               "become an atom, so the same charge makes half as many atoms.",
    },
    {
        "id": "ks4-electrolysis-molten-h02",
        "subtopic_slug": "electrolysis-molten",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student predicts that electrolysing molten zinc chloride "
                "gives zinc at the anode. Identify the error and give the "
                "correct products.",
        "options": [
            "There is no error — the zinc does appear at the anode",
            "Zinc forms at the anode and chlorine forms at the cathode, "
            "because each ion goes to the electrode of the same sign",
            "Zinc ions are positive, so zinc forms at the negative cathode, "
            "and chlorine forms at the anode",
            "Neither element forms — zinc chloride is too stable to decompose",
        ],
        "correct_index": 2,
        "why": "An ion always travels to the oppositely charged electrode, so "
               "a positive metal ion can only be discharged at the cathode.",
    },
    {
        "id": "ks4-electrolysis-molten-h03",
        "subtopic_slug": "electrolysis-molten",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why sodium is made by electrolysing molten sodium "
                "chloride rather than a solution of it.",
        "options": [
            "In a solution, hydrogen from the water is produced at the "
            "cathode instead of the sodium",
            "In a solution the ions are held still and cannot move",
            "A solution of sodium chloride does not conduct electricity",
            "The solution would boil away long before enough current could "
            "flow through it to make any sodium",
        ],
        "correct_index": 0,
        "why": "Water brings hydrogen ions with it, and sodium is so far "
               "above hydrogen that the hydrogen is discharged first.",
    },
    {
        "id": "ks4-electrolysis-molten-h04",
        "subtopic_slug": "electrolysis-molten",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The electrolysis of molten lead(II) bromide is left running "
                "for a long time. Suggest what is observed as the last of the "
                "compound is used up.",
        "options": [
            "The lead that has already formed redissolves back into the melt, "
            "and so the current begins to rise again",
            "The current falls to zero, because there are no ions left to "
            "carry charge and be discharged",
            "Bromine starts to be given off at both electrodes",
            "Lead begins to be deposited at the anode instead",
        ],
        "correct_index": 1,
        "why": "Once every ion has been discharged there is nothing left to "
               "move through the melt, so the circuit stops conducting.",
    },
    # ── electrolysis-extraction ───────────────────────────────────────
    {
        "id": "ks4-electrolysis-extraction-e01",
        "subtopic_slug": "electrolysis-extraction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the substance that aluminium oxide is dissolved in "
                "during aluminium extraction.",
        "options": [
            "Molten sodium chloride",
            "Molten cryolite",
            "Concentrated sulfuric acid",
            "Hot water",
        ],
        "correct_index": 1,
        "why": "Cryolite acts purely as a solvent for the aluminium oxide, "
               "and is recovered rather than used up.",
    },
    {
        "id": "ks4-electrolysis-extraction-e02",
        "subtopic_slug": "electrolysis-extraction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the main reason cryolite is used in aluminium "
                "extraction.",
        "options": [
            "It lowers the working temperature from about 2050 °C to about "
            "950 °C",
            "It reacts with the oxide and releases the aluminium",
            "It stops the molten aluminium reacting with the oxygen in the "
            "air above the tank",
            "It makes the aluminium oxide dissolve in water",
        ],
        "correct_index": 0,
        "why": "Aluminium oxide on its own melts at a temperature that would "
               "be far too costly to maintain.",
    },
    {
        "id": "ks4-electrolysis-extraction-e03",
        "subtopic_slug": "electrolysis-extraction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the electrolyte used when impure copper is purified by "
                "electrolysis.",
        "options": [
            "Dilute sulfuric acid",
            "Molten copper oxide",
            "Copper sulfate solution",
            "Sodium chloride solution",
        ],
        "correct_index": 2,
        "why": "The solution must already contain copper ions so that copper "
               "can be carried from one electrode to the other.",
    },
    {
        "id": "ks4-electrolysis-extraction-e04",
        "subtopic_slug": "electrolysis-extraction",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which electrode an object being electroplated is "
                "connected as, and why.",
        "options": [
            "The anode, because it must lose electrons to the circuit",
            "Neither — it simply hangs in the middle of the solution",
            "The anode, because that is where metal is always deposited",
            "The cathode, because metal ions are deposited there",
        ],
        "correct_index": 3,
        "why": "The coating forms where positive metal ions gain electrons, "
               "which is the negative cathode.",
    },
    {
        "id": "ks4-electrolysis-extraction-s01",
        "subtopic_slug": "electrolysis-extraction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what the anode sludge contains in copper "
                "purification, and why it is worth collecting.",
        "options": [
            "Copper oxide, which can be sold on as a pigment",
            "Discharged sulfate ions, which are recycled into fresh acid",
            "Gold, silver and platinum, which are too unreactive to dissolve "
            "and drop to the bottom",
            "Impure copper that has broken away from the cathode and dropped "
            "to the bottom of the cell",
        ],
        "correct_index": 2,
        "why": "The impurities below copper in the reactivity series will not "
               "go into solution, so they fall as a valuable sludge.",
    },
    {
        "id": "ks4-electrolysis-extraction-s02",
        "subtopic_slug": "electrolysis-extraction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why crude copper straight from smelting is not good "
                "enough for electrical wiring.",
        "options": [
            "It is far too soft to be drawn out into a wire",
            "It becomes brittle as soon as it cools after smelting",
            "It contains sulfur, which makes it magnetic",
            "The impurities in it lower its electrical conductivity",
        ],
        "correct_index": 3,
        "why": "Wiring needs the very high conductivity that only copper of "
               "about 99.99% purity gives.",
    },
    {
        "id": "ks4-electrolysis-extraction-s03",
        "subtopic_slug": "electrolysis-extraction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the masses of the two electrodes change during "
                "copper purification.",
        "options": [
            "Both gain mass, because copper is added to each of them",
            "The anode loses mass and the cathode gains mass",
            "Both lose mass, because copper is lost into the solution",
            "The anode gains mass and the cathode loses mass",
        ],
        "correct_index": 1,
        "why": "Copper leaves the impure anode as ions and arrives at the "
               "pure cathode as metal.",
    },
    {
        "id": "ks4-electrolysis-extraction-s04",
        "subtopic_slug": "electrolysis-extraction",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why extracting aluminium by electrolysis is so "
                "expensive.",
        "options": [
            "Huge amounts of electrical energy are needed, and the anodes "
            "must be replaced regularly",
            "Aluminium ore is extremely rare and must be mined very deep",
            "The cryolite is used up during the reaction and has to be bought "
            "again for every single batch",
            "The metal must be shipped while still molten in special vessels",
        ],
        "correct_index": 0,
        "why": "The process runs continuously at high temperature on a large "
               "current, and the carbon anodes are consumed as it does.",
    },
    {
        "id": "ks4-electrolysis-extraction-h01",
        "subtopic_slug": "electrolysis-extraction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "During silver plating, the silver anode loses 0.48 g. "
                "Determine the mass gained by the object at the cathode.",
        "options": [
            "0.48 g",
            "0.24 g",
            "0.96 g",
            "It gains no mass at all",
        ],
        "correct_index": 0,
        "why": "Every silver atom that leaves the anode as an ion is "
               "deposited on the cathode, so the two mass changes match "
               "exactly.",
    },
    {
        "id": "ks4-electrolysis-extraction-h02",
        "subtopic_slug": "electrolysis-extraction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the aluminium cell is a steel tank lined with "
                "graphite, rather than a metal rod dipped into the melt.",
        "options": [
            "Graphite is the only substance that conducts at 950 °C",
            "The lining conducts, does not react with the melt, and holds the "
            "molten aluminium that collects at the bottom",
            "Graphite is magnetic, so it attracts the aluminium ions towards "
            "it",
            "The graphite lining lowers the melting point of the mixture "
            "still further, below the 950 °C the cryolite gives",
        ],
        "correct_index": 1,
        "why": "The cathode has to be a container as well as a conductor, "
               "because the aluminium forms as a liquid and sinks.",
    },
    {
        "id": "ks4-electrolysis-extraction-h03",
        "subtopic_slug": "electrolysis-extraction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen if the anode in copper "
                "purification were made of graphite instead of impure copper.",
        "options": [
            "Copper would still be deposited at the cathode, and the whole "
            "process would run exactly as it does with a copper anode",
            "No copper at all would be deposited at the cathode",
            "The graphite would dissolve and replace the copper ions",
            "The copper ions would be used up without being replaced, so the "
            "solution would fade and deposition would slow",
        ],
        "correct_index": 3,
        "why": "An inert anode releases oxygen instead of dissolving, so "
               "nothing puts copper ions back into the solution.",
    },
    {
        "id": "ks4-electrolysis-extraction-h04",
        "subtopic_slug": "electrolysis-extraction",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare aluminium extraction with copper purification in "
                "terms of what happens at the anode.",
        "options": [
            "In both, the anode dissolves into the electrolyte",
            "In both, the anode is inert and takes no part in the reaction",
            "Aluminium extraction releases oxygen at an inert graphite anode, "
            "while copper purification uses a copper anode that dissolves",
            "Aluminium extraction dissolves its anode into the melt, while "
            "copper purification releases oxygen at an inert graphite anode "
            "instead",
        ],
        "correct_index": 2,
        "why": "The aluminium anode only supplies a surface for oxide ions to "
               "discharge on, whereas the copper anode is itself the source "
               "of the copper.",
    },
    # ── electrolysis-aqueous ──────────────────────────────────────────
    {
        "id": "ks4-electrolysis-aqueous-e01",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two extra ions that the water itself contributes to "
                "any aqueous solution.",
        "options": [
            "Sodium ions and chloride ions",
            "Sulfate ions and nitrate ions",
            "Oxide ions and metal ions",
            "Hydrogen ions and hydroxide ions",
        ],
        "correct_index": 3,
        "why": "Water ionises very slightly to give H+ and OH-, and those are "
               "what compete with the salt's own ions.",
    },
    {
        "id": "ks4-electrolysis-aqueous-e02",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the laboratory test for oxygen gas.",
        "options": [
            "It relights a glowing splint",
            "It gives a squeaky pop with a lit splint",
            "It turns limewater milky",
            "It bleaches damp litmus paper",
        ],
        "correct_index": 0,
        "why": "Oxygen supports combustion, so a splint that is only glowing "
               "bursts back into flame in it.",
    },
    {
        "id": "ks4-electrolysis-aqueous-e03",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the laboratory test for chlorine gas.",
        "options": [
            "It relights a glowing splint",
            "It bleaches damp litmus paper",
            "It turns limewater milky",
            "It gives a squeaky pop with a lit splint",
        ],
        "correct_index": 1,
        "why": "Chlorine bleaches the dye in the litmus, turning the damp "
               "paper white.",
    },
    {
        "id": "ks4-electrolysis-aqueous-e04",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which gas is collected at the cathode when dilute "
                "sulfuric acid is electrolysed.",
        "options": [
            "Oxygen",
            "Sulfur dioxide",
            "Hydrogen",
            "Chlorine",
        ],
        "correct_index": 2,
        "why": "The only positive ions present are hydrogen ions, so hydrogen "
               "gas is what is discharged at the negative electrode.",
    },
    {
        "id": "ks4-electrolysis-aqueous-s01",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the product formed at the cathode when sodium "
                "sulfate solution is electrolysed.",
        "options": [
            "Sodium metal",
            "Hydrogen gas",
            "Oxygen gas",
            "Sulfur",
        ],
        "correct_index": 1,
        "why": "Sodium is far above hydrogen in the reactivity series, so the "
               "hydrogen ions from the water are discharged instead.",
    },
    {
        "id": "ks4-electrolysis-aqueous-s02",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the product formed at the anode when copper sulfate "
                "solution is electrolysed with inert electrodes.",
        "options": [
            "Copper",
            "Sulfur dioxide",
            "Oxygen",
            "Hydrogen",
        ],
        "correct_index": 2,
        "why": "There are no halide ions present, so the hydroxide ions from "
               "the water are discharged and oxygen is released.",
    },
    {
        "id": "ks4-electrolysis-aqueous-s03",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why hydrogen, and not sodium, is produced at the "
                "cathode when brine is electrolysed.",
        "options": [
            "Sodium is far more reactive than hydrogen, so the hydrogen ions "
            "are discharged in preference",
            "Sodium ions are attracted to the anode rather than the cathode",
            "There are far more sodium ions than hydrogen ions present, so "
            "the sodium ions are discharged first",
            "Sodium metal is produced, but it reacts instantly with the "
            "chlorine",
        ],
        "correct_index": 0,
        "why": "Where two positive ions compete, the less reactive element is "
               "the one that takes the electrons.",
    },
    {
        "id": "ks4-electrolysis-aqueous-s04",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the third useful product that is left dissolved in the "
                "solution after concentrated brine has been electrolysed.",
        "options": [
            "Sodium chlorate",
            "Hydrochloric acid",
            "Sodium carbonate",
            "Sodium hydroxide",
        ],
        "correct_index": 3,
        "why": "The hydrogen ions and chloride ions are removed as gases, "
               "leaving sodium ions and hydroxide ions behind in solution.",
    },
    {
        "id": "ks4-electrolysis-aqueous-h01",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Dilute sulfuric acid is electrolysed and both gases are "
                "collected. Determine the ratio of the volume of gas at the "
                "cathode to the volume at the anode.",
        "options": [
            "1 : 1",
            "1 : 2",
            "2 : 1",
            "4 : 1",
        ],
        "correct_index": 2,
        "why": "The water is split into hydrogen and oxygen in the ratio it "
               "is built from, so twice as much hydrogen is made as oxygen.",
    },
    {
        "id": "ks4-electrolysis-aqueous-h02",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the sulfate ions are not discharged at the anode "
                "when copper sulfate solution is electrolysed.",
        "options": [
            "Sulfate ions are far too large to reach the surface of the "
            "electrode and be discharged there",
            "They are attracted to the cathode rather than the anode",
            "They were already discharged in the solid before it dissolved",
            "Hydroxide ions from the water are discharged in preference, so "
            "oxygen is released instead",
        ],
        "correct_index": 3,
        "why": "Sulfate ions are very stable, so the competing hydroxide ions "
               "always give up their electrons first.",
    },
    {
        "id": "ks4-electrolysis-aqueous-h03",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the products of electrolysing very dilute sodium "
                "chloride solution, and explain how they differ from those "
                "given by concentrated brine.",
        "options": [
            "Sodium and chlorine, exactly as concentrated brine gives",
            "Hydrogen at the cathode and mostly oxygen at the anode, because "
            "the chloride ions are now too dilute to be favoured",
            "Hydrogen at both of the electrodes, because with so little salt "
            "present it is the water that completely dominates the process",
            "Chlorine at the cathode and hydrogen at the anode",
        ],
        "correct_index": 1,
        "why": "Chloride ions only win at the anode when they are "
               "concentrated; dilute them and the hydroxide ions take over.",
    },
    {
        "id": "ks4-electrolysis-aqueous-h04",
        "subtopic_slug": "electrolysis-aqueous",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student electrolyses silver nitrate solution with inert "
                "electrodes and predicts hydrogen at the cathode. Evaluate "
                "this prediction.",
        "options": [
            "Wrong — silver is below hydrogen in the series, so silver metal "
            "is deposited instead",
            "Correct — hydrogen is always the cathode product from an aqueous "
            "solution",
            "Wrong — nitrogen is produced at the cathode from the nitrate "
            "ions",
            "Correct — the silver ions go to the anode, so hydrogen must form "
            "at the cathode",
        ],
        "correct_index": 0,
        "why": "The cathode rule turns on reactivity: a metal below hydrogen "
               "is discharged in preference to it.",
    },
    # ── strong-weak-acids (HIGHER TIER) ───────────────────────────────
    {
        "id": "ks4-strong-weak-acids-e01",
        "subtopic_slug": "strong-weak-acids",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what is meant by a strong acid.",
        "options": [
            "An acid that is completely ionised in water",
            "An acid with a large number of moles per dm3",
            "An acid that will react with every metal",
            "An acid that cannot be diluted with water",
        ],
        "correct_index": 0,
        "why": "Strength describes how completely the acid splits into ions, "
               "not how much of it there is.",
    },
    {
        "id": "ks4-strong-weak-acids-e02",
        "subtopic_slug": "strong-weak-acids",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Identify which of these is a weak acid.",
        "options": [
            "Hydrochloric acid",
            "Nitric acid",
            "Ethanoic acid",
            "Sulfuric acid",
        ],
        "correct_index": 2,
        "why": "Ethanoic acid only partially ionises — roughly one molecule "
               "in a hundred releases its hydrogen ion.",
    },
    {
        "id": "ks4-strong-weak-acids-e03",
        "subtopic_slug": "strong-weak-acids",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what the ⇌ symbol shows in the equation CH3COOH ⇌ "
                "CH3COO- + H+.",
        "options": [
            "That the reaction happens extremely quickly",
            "That the acid solution is concentrated",
            "That the acid ionises completely, so every molecule releases its "
            "hydrogen ion",
            "That the ionisation is reversible, so only some molecules split "
            "up",
        ],
        "correct_index": 3,
        "why": "The double arrow means the ions recombine as fast as they "
               "form, so most of the acid stays as whole molecules.",
    },
    {
        "id": "ks4-strong-weak-acids-e04",
        "subtopic_slug": "strong-weak-acids",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what happens to the molecules of a strong acid when it "
                "dissolves in water.",
        "options": [
            "About one in a hundred of them releases a hydrogen ion",
            "Every one of them releases its hydrogen ion",
            "They stay whole and release no ions at all",
            "They join together into larger molecules",
        ],
        "correct_index": 1,
        "why": "Full dissociation is exactly what makes an acid strong: HCl → "
               "H+ + Cl- goes to completion.",
    },
    {
        "id": "ks4-strong-weak-acids-s01",
        "subtopic_slug": "strong-weak-acids",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Compare the electrical conductivity of 0.1 mol/dm3 "
                "hydrochloric acid with that of 0.1 mol/dm3 ethanoic acid.",
        "options": [
            "They conduct equally well, because the concentrations match",
            "Ethanoic acid conducts better, because its molecules are larger",
            "Neither conducts, because both are covalent substances",
            "Hydrochloric acid conducts better, because it contains far more "
            "ions",
        ],
        "correct_index": 3,
        "why": "Conductivity depends on how many free ions there are, and "
               "only the fully ionised acid supplies the full number.",
    },
    {
        "id": "ks4-strong-weak-acids-s02",
        "subtopic_slug": "strong-weak-acids",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why magnesium fizzes far more vigorously in 1 "
                "mol/dm3 hydrochloric acid than in 1 mol/dm3 ethanoic acid.",
        "options": [
            "The ethanoic acid forms a coating that blocks the magnesium",
            "The hydrochloric acid has a much higher hydrogen ion "
            "concentration",
            "The ethanoic acid is the more concentrated of the two",
            "The hydrochloric acid is supplied at a higher temperature",
        ],
        "correct_index": 1,
        "why": "Rate depends on the concentration of H+ ions, and full "
               "ionisation gives about a hundred times more of them.",
    },
    {
        "id": "ks4-strong-weak-acids-s03",
        "subtopic_slug": "strong-weak-acids",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Excess magnesium is added to equal volumes of 1 mol/dm3 "
                "hydrochloric acid and 1 mol/dm3 ethanoic acid. Predict the "
                "total volume of hydrogen each produces.",
        "options": [
            "More from the hydrochloric acid, because it is the stronger acid",
            "More from the ethanoic acid, because it keeps some of its "
            "hydrogen in reserve as whole molecules",
            "The same from both, because each contains the same total number "
            "of acid molecules",
            "None from the ethanoic acid, because it is too weak to react",
        ],
        "correct_index": 2,
        "why": "Strength changes the rate, not the amount — as the weak acid "
               "reacts, more of it ionises until every molecule has been "
               "used.",
    },
    {
        "id": "ks4-strong-weak-acids-s04",
        "subtopic_slug": "strong-weak-acids",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "About 1% of the molecules in 0.1 mol/dm3 ethanoic acid are "
                "ionised. Deduce its approximate pH.",
        "options": [
            "pH 3",
            "pH 1",
            "pH 7",
            "pH 5",
        ],
        "correct_index": 0,
        "why": "1% of 0.1 mol/dm3 gives about 0.001 mol/dm3 of H+, and 0.001 "
               "is 10 to the power −3, so the pH is about 3.",
    },
    {
        "id": "ks4-strong-weak-acids-h01",
        "subtopic_slug": "strong-weak-acids",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Solution P is 0.001 mol/dm3 hydrochloric acid and solution Q "
                "is 1.0 mol/dm3 ethanoic acid. Deduce which has the lower pH.",
        "options": [
            "P, because a strong acid always has the lower pH",
            "Q, because although it is weak, it is a thousand times more "
            "concentrated and so releases more hydrogen ions",
            "P, because dilute solutions always sit at the low end of the "
            "scale",
            "They have the same pH, because being a thousand times weaker and "
            "a thousand times more concentrated cancel out exactly",
        ],
        "correct_index": 1,
        "why": "Only the H+ concentration sets the pH: even at 1% ionisation, "
               "1.0 mol/dm3 gives more H+ than fully ionised 0.001 mol/dm3.",
    },
    {
        "id": "ks4-strong-weak-acids-h02",
        "subtopic_slug": "strong-weak-acids",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Explain why a weak acid becomes proportionally more ionised "
                "when it is diluted with water.",
        "options": [
            "Dilution shifts the ionisation equilibrium to the right, so a "
            "greater fraction of the molecules split into ions",
            "Dilution adds extra hydrogen ions that come from the water",
            "Dilution converts the weak acid into a strong acid",
            "Dilution washes the negative ions away from the solution, so no "
            "further ionisation of the acid molecules is possible",
        ],
        "correct_index": 0,
        "why": "The ions are further apart in the larger volume, so they "
               "recombine less often and the balance sits further towards "
               "ionisation.",
    },
    {
        "id": "ks4-strong-weak-acids-h03",
        "subtopic_slug": "strong-weak-acids",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A strong acid and a weak acid are found to have the same pH. "
                "Compare their concentrations.",
        "options": [
            "They must be at exactly the same concentration, since the pH of "
            "a solution depends only on its concentration",
            "The strong acid must be the more concentrated of the two",
            "They cannot possibly have the same pH, whatever their "
            "concentrations",
            "The weak acid must be the more concentrated, because only a "
            "small fraction of it is ionised",
        ],
        "correct_index": 3,
        "why": "To supply the same number of H+ ions from only a small "
               "fraction of its molecules, the weak acid needs far more "
               "molecules present.",
    },
    {
        "id": "ks4-strong-weak-acids-h04",
        "subtopic_slug": "strong-weak-acids",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A student writes: 'concentrated ethanoic acid must be a "
                "strong acid, because it burns the skin.' Evaluate this "
                "statement.",
        "options": [
            "Correct — anything corrosive enough to burn is a strong acid",
            "Correct — 'concentrated' and 'strong' are simply two different "
            "words for describing the very same property of an acid",
            "Wrong — it is a concentrated weak acid; strength describes the "
            "degree of ionisation, not the harm caused",
            "Wrong — ethanoic acid is not really an acid at all",
        ],
        "correct_index": 2,
        "why": "Strength and concentration are independent: ethanoic acid "
               "stays only partly ionised however concentrated it is.",
    },
    # ── half-equations (HIGHER TIER) ──────────────────────────────────
    {
        "id": "ks4-half-equations-e01",
        "subtopic_slug": "half-equations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State on which side of a cathode half equation the electrons "
                "are written.",
        "options": [
            "On the right, because the electrons are given away",
            "On neither side — cathode equations do not include electrons",
            "On the left, because the ions gain the electrons",
            "On both sides, so that the charges cancel out",
        ],
        "correct_index": 2,
        "why": "Reduction is gain of electrons, so at the cathode the "
               "electrons are among the reactants.",
    },
    {
        "id": "ks4-half-equations-e02",
        "subtopic_slug": "half-equations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Identify the correct half equation for the production of "
                "hydrogen at the cathode.",
        "options": [
            "H+ + e- → H2",
            "2H+ + 2e- → H2",
            "H2 → 2H+ + 2e-",
            "2H+ → H2 + 2e-",
        ],
        "correct_index": 1,
        "why": "A hydrogen molecule needs two ions and therefore two "
               "electrons, which balances both the atoms and the charge.",
    },
    {
        "id": "ks4-half-equations-e03",
        "subtopic_slug": "half-equations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "Identify the half equation that shows oxidation.",
        "options": [
            "2Br- → Br2 + 2e-",
            "Pb2+ + 2e- → Pb",
            "Al3+ + 3e- → Al",
            "2H+ + 2e- → H2",
        ],
        "correct_index": 0,
        "why": "Oxidation is loss of electrons, so the electrons appear on "
               "the product side — which happens at the anode.",
    },
    {
        "id": "ks4-half-equations-e04",
        "subtopic_slug": "half-equations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what must be balanced in a half equation, as well as "
                "the atoms.",
        "options": [
            "The mass in grams on each side",
            "The number of molecules on each side",
            "The temperature of each side",
            "The total electrical charge on each side",
        ],
        "correct_index": 3,
        "why": "The electrons are added precisely so that the total charge is "
               "the same on both sides.",
    },
    {
        "id": "ks4-half-equations-s01",
        "subtopic_slug": "half-equations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Identify the half equation for the deposition of aluminium "
                "at the cathode.",
        "options": [
            "Al3+ + 3e- → Al",
            "Al3+ → Al + 3e-",
            "Al + 3e- → Al3+",
            "Al3+ + 2e- → Al",
        ],
        "correct_index": 0,
        "why": "An Al3+ ion carries three positive charges, so it needs "
               "exactly three electrons to become a neutral atom.",
    },
    {
        "id": "ks4-half-equations-s02",
        "subtopic_slug": "half-equations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Identify the correctly balanced anode half equation for the "
                "discharge of oxide ions during aluminium extraction.",
        "options": [
            "O2- → O2 + 2e-",
            "2O2- → O2 + 2e-",
            "O2- + 2e- → O2",
            "2O2- → O2 + 4e-",
        ],
        "correct_index": 3,
        "why": "Two oxide ions make one O2 molecule and carry 4− between "
               "them, so four electrons must be released.",
    },
    {
        "id": "ks4-half-equations-s03",
        "subtopic_slug": "half-equations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Identify the correct half equation for the formation of "
                "oxygen from hydroxide ions at the anode.",
        "options": [
            "4OH- → O2 + 2H2O + 2e-",
            "4OH- → O2 + 2H2O + 4e-",
            "2OH- → O2 + H2O + 2e-",
            "4OH- + 4e- → O2 + 2H2O",
        ],
        "correct_index": 1,
        "why": "Four hydroxide ions supply 4 O and 4 H, which become one O2 "
               "and two H2O, and their 4− charge is released as 4 electrons.",
    },
    {
        "id": "ks4-half-equations-s04",
        "subtopic_slug": "half-equations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Molten sodium chloride is electrolysed and sodium is "
                "deposited. Identify the cathode half equation.",
        "options": [
            "Na → Na+ + e-",
            "2Na+ + 2e- → Na2",
            "Na+ + e- → Na",
            "Na+ → Na + e-",
        ],
        "correct_index": 2,
        "why": "A sodium ion carries a single positive charge, so one "
               "electron turns it into a sodium atom.",
    },
    {
        "id": "ks4-half-equations-h01",
        "subtopic_slug": "half-equations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Combine 2H+ + 2e- → H2 with 4OH- → O2 + 2H2O + 4e- to "
                "determine the overall equation for the electrolysis of "
                "dilute sulfuric acid.",
        "options": [
            "2H2O → H2 + O2",
            "H2O → H2 + O2",
            "2H2O → 2H2 + 2O2",
            "2H2O → 2H2 + O2",
        ],
        "correct_index": 3,
        "why": "The cathode equation must be doubled so that four electrons "
               "match at each electrode, and the result is water split 2 : 1.",
    },
    {
        "id": "ks4-half-equations-h02",
        "subtopic_slug": "half-equations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Determine the factor by which Al3+ + 3e- → Al must be "
                "multiplied before it can be combined with 2O2- → O2 + 4e- "
                "multiplied by three.",
        "options": [
            "2",
            "3",
            "4",
            "6",
        ],
        "correct_index": 2,
        "why": "Three anode equations release 12 electrons, and 12 ÷ 3 = 4, "
               "so four aluminium ions are reduced for every three O2 "
               "molecules.",
    },
    {
        "id": "ks4-half-equations-h03",
        "subtopic_slug": "half-equations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Copper sulfate solution is electrolysed using copper "
                "electrodes, so that both half equations involve copper. "
                "Explain what the overall equation shows.",
        "options": [
            "That the copper sulfate is decomposed, giving copper metal at "
            "one electrode and solid sulfur at the other",
            "That there is no net chemical change — copper is simply "
            "transferred from the anode to the cathode",
            "That copper is oxidised at both of the electrodes",
            "That the copper reacts with the sulfate to form copper oxide",
        ],
        "correct_index": 1,
        "why": "Cu → Cu2+ + 2e- at the anode and Cu2+ + 2e- → Cu at the "
               "cathode cancel, leaving only a move from one electrode to the "
               "other.",
    },
    {
        "id": "ks4-half-equations-h04",
        "subtopic_slug": "half-equations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A student writes the anode half equation for bromine as Br- "
                "→ Br2 + e-. Identify both of the errors.",
        "options": [
            "The bromine atoms and the charge are both unbalanced — it should "
            "read 2Br- → Br2 + 2e-",
            "Only the charge is unbalanced — the bromine atoms are fine, so "
            "it should read Br- → Br2 + 2e-",
            "The electrons belong on the left — it should read Br- + e- → Br2",
            "There are no errors; the equation is correct as it stands",
        ],
        "correct_index": 0,
        "why": "One bromide ion cannot make a two-atom molecule, and a single "
               "1− charge cannot be balanced by a single electron on the far "
               "side.",
    },
]
