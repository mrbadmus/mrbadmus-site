"""Biology · Infection and response — the nine subtopics of AQA 4.3.

Covers communicable disease and the body's defences, the viral, bacterial,
fungal and protist diseases named in the specification, vaccination,
antibiotics and painkillers, drug discovery and testing, and the two
Triple-only subtopics (plant disease detection and defence, monoclonal
antibodies).

The distractors are built from the errors this topic actually produces in a
classroom: antibiotics reached for against a virus, the mosquito named as the
pathogen rather than the vector, the patient (not the bacterium) described as
becoming resistant, a vaccine believed to contain a live full-strength
pathogen, "immune" read as "cannot possibly catch it", painkillers believed
to cure an infection, plants credited with antibodies and lymphocytes, and
monoclonal antibodies confused with a vaccine. Pathogen type is deliberately
tested by identification as well as by explanation, because misfiling one is
the fastest way to lose a mark here.

Seven subtopics are BASE and carry no Higher-tier and no Triple-only content
in their stems or their options — in particular no mRNA vaccines, no herd
immunity thresholds and no peer review, all of which sit in the Higher
extension prose. `plant-disease-detection-defence` is Triple-only at
foundation tier; `monoclonal-antibodies` is Triple-only and Higher.

Nothing here restates a lesson page's own "Test yourself" question or a pair
from its matching block — both are printed with their answers on a page the
child can open at will, and belong to a different pool.
"""

TOPIC = "infection-response"
SUBJECT = "biology"

QUESTIONS = [
    # ── communicable-diseases-defence ────────────────────────────────────
    {
        "id": "ks4-communicable-diseases-defence-e01",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which type of pathogen reproduces by binary fission inside "
                "the body and causes disease mainly by releasing toxins?",
        "options": [
            "Bacteria",
            "Viruses",
            "Fungi",
            "Protists",
        ],
        "correct_index": 0,
        "why": "Bacteria are prokaryotic cells that divide rapidly by binary "
               "fission, and it is the toxins they secrete that produce most "
               "of the symptoms.",
    },
    {
        "id": "ks4-communicable-diseases-defence-e02",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cholera is spread by which route of transmission?",
        "options": [
            "Airborne droplets released by coughing",
            "Sharing contaminated needles",
            "Drinking contaminated water",
            "Direct skin-to-skin contact",
        ],
        "correct_index": 2,
        "why": "Cholera bacteria are swallowed in water contaminated with "
               "sewage, which is why clean water supplies stop outbreaks.",
    },
    {
        "id": "ks4-communicable-diseases-defence-e03",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What name is given to the molecules on the surface of a "
                "pathogen that the immune system recognises as foreign?",
        "options": [
            "Antibodies",
            "Antigens",
            "Antibiotics",
            "Antivirals",
        ],
        "correct_index": 1,
        "why": "Antigens are the surface markers a pathogen carries; "
               "antibodies are the proteins the body makes to fit them.",
    },
    {
        "id": "ks4-communicable-diseases-defence-e04",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The skin produces slightly acidic secretions. Suggest how "
                "this helps to defend the body against disease.",
        "options": [
            "It seals any cuts in the skin so that pathogens cannot enter",
            "It kills every virus that lands on the skin within seconds",
            "It traps pathogens so that cilia can sweep them away",
            "It inhibits the growth of bacteria on the skin surface",
        ],
        "correct_index": 3,
        "why": "Acidic conditions make the skin surface a poor place for "
               "bacteria to grow, adding a chemical defence to the physical "
               "barrier.",
    },
    {
        "id": "ks4-communicable-diseases-defence-s01",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Antibodies are described as specific. Explain what this "
                "means.",
        "options": [
            "They are produced faster than any other protein in the blood",
            "They are able to bind to any pathogen that enters the body",
            "They destroy pathogens by engulfing and then digesting them",
            "Each antibody binds only to one particular antigen shape",
        ],
        "correct_index": 3,
        "why": "An antibody's binding site is complementary to one antigen, "
               "so a lymphocyte making it is useful against one pathogen "
               "only.",
    },
    {
        "id": "ks4-communicable-diseases-defence-s02",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to a pathogen once a phagocyte has "
                "taken it inside the cell.",
        "options": [
            "Enzymes inside the phagocyte digest and destroy it",
            "Antibodies released inside the cell make it burst open",
            "It is carried to the liver, where it is broken down",
            "It is coated in mucus and swept up to the throat",
        ],
        "correct_index": 0,
        "why": "The phagocyte's membrane draws the pathogen in and its own "
               "digestive enzymes break the pathogen down.",
    },
    {
        "id": "ks4-communicable-diseases-defence-s03",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A doctor tells a patient that their illness is not "
                "communicable. Which statement must therefore be true?",
        "options": [
            "The illness will always be less serious than an infection",
            "The illness must have been inherited from their parents",
            "The illness cannot be passed to another person",
            "The illness can be treated with antibiotics but not antivirals",
        ],
        "correct_index": 2,
        "why": "A communicable disease is one that spreads from host to host, "
               "so a non-communicable illness cannot be caught from the "
               "patient.",
    },
    {
        "id": "ks4-communicable-diseases-defence-s04",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chef handles raw chicken and then prepares a salad without "
                "washing their hands. Suggest why customers become ill.",
        "options": [
            "Handling raw meat releases toxins from the chef's own skin",
            "Bacteria are transferred to food that is not cooked again",
            "The bacteria mutate on warm hands into a deadlier strain",
            "The chef's sweat provides the water bacteria need to grow",
        ],
        "correct_index": 1,
        "why": "Cooking would have killed the bacteria, so moving them onto "
               "food that is eaten raw removes the only step that made it "
               "safe.",
    },
    {
        "id": "ks4-communicable-diseases-defence-h01",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bacterial infection and a viral infection both cause a "
                "fever. Compare how the two pathogens damage body tissue.",
        "options": [
            "Both burst body cells open as they reproduce inside them",
            "Bacteria mainly release toxins; viruses destroy the cells "
            "they replicate inside",
            "Bacteria destroy the cells from within; viruses release "
            "toxins into the bloodstream",
            "Neither damages tissue — all the harm is done by the fever",
        ],
        "correct_index": 1,
        "why": "Bacteria stay outside cells and secrete toxins, while a "
               "virus can only copy itself by taking over a host cell, "
               "destroying it in the process.",
    },
    {
        "id": "ks4-communicable-diseases-defence-h02",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "After a country treats its drinking water and separates it "
                "from sewage, cholera cases fall sharply but influenza cases "
                "do not change. Explain why.",
        "options": [
            "Influenza bacteria are resistant to water treatment chemicals",
            "Cholera is a virus and viruses are removed by water filters",
            "Influenza spreads through contaminated food, and food hygiene "
            "rules were unchanged",
            "Influenza spreads in airborne droplets, a route water treatment "
            "does not break",
        ],
        "correct_index": 3,
        "why": "A control measure only works on the transmission route it "
               "targets, and influenza never travels through the water "
               "supply.",
    },
    {
        "id": "ks4-communicable-diseases-defence-h03",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person can catch a cold many times even though "
                "they produce antibodies against it each time.",
        "options": [
            "Different cold viruses carry different antigens, so old "
            "antibodies do not fit them",
            "Antibodies made against a cold are broken down by the stomach "
            "acid a few days after they are made",
            "Cold viruses are bacteria, so antibodies cannot bind to them",
            "The body stops producing antibodies once a person is fully "
            "grown",
        ],
        "correct_index": 0,
        "why": "Antibodies are specific to one antigen shape, and a cold "
               "caught next winter is usually a different virus with "
               "different antigens.",
    },
    {
        "id": "ks4-communicable-diseases-defence-h04",
        "subtopic_slug": "communicable-diseases-defence",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hospital asks all visitors to use alcohol hand gel and "
                "asks anyone with a cough to wear a mask. Explain which "
                "transmission route each measure targets.",
        "options": [
            "Hand gel targets airborne droplets; masks target direct contact",
            "Both of these measures target the contaminated food and water "
            "routes instead",
            "Hand gel targets contact with surfaces; masks target airborne "
            "droplets",
            "Both target vectors, because insects carry pathogens on wards",
        ],
        "correct_index": 2,
        "why": "Pathogens picked up from door handles and rails travel by "
               "direct contact, while a cough releases them as droplets into "
               "the air.",
    },

    # ── viral-diseases ───────────────────────────────────────────────────
    {
        "id": "ks4-viral-diseases-e01",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement describes the structure of a virus?",
        "options": [
            "A single cell with a cell wall, cytoplasm and a plasmid",
            "A cell with a nucleus that holds its genetic material and "
            "ribosomes",
            "Genetic material inside a protein coat, with no cell structure",
            "A single cell with a membrane but no cell wall",
        ],
        "correct_index": 2,
        "why": "A virus is not a cell at all — it is genetic material wrapped "
               "in protein, which is why it needs a host cell to reproduce.",
    },
    {
        "id": "ks4-viral-diseases-e02",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these diseases of plants is caused by a virus?",
        "options": [
            "Tobacco mosaic disease",
            "Rose black spot",
            "Salmonella food poisoning",
            "Malaria",
        ],
        "correct_index": 0,
        "why": "Tobacco mosaic virus is a plant virus; rose black spot is "
               "fungal, Salmonella is bacterial and malaria is caused by a "
               "protist.",
    },
    {
        "id": "ks4-viral-diseases-e03",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which drugs are used to control an HIV infection?",
        "options": [
            "Antibiotics, which kill the virus in the bloodstream",
            "Painkillers, which stop the virus reproducing",
            "Fungicides, which are sprayed to kill the virus",
            "Antiretroviral drugs, which stop the virus replicating",
        ],
        "correct_index": 3,
        "why": "Antiretrovirals block the virus from making copies of itself, "
               "keeping the number of virus particles in the body low.",
    },
    {
        "id": "ks4-viral-diseases-e04",
        "subtopic_slug": "viral-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which serious complication can a measles infection lead to?",
        "options": [
            "Infertility, caused by pelvic inflammatory disease",
            "Pneumonia, a lung infection that can be fatal",
            "Anaemia, caused by destruction of red blood cells",
            "Kidney failure, caused by toxins in the blood",
        ],
        "correct_index": 1,
        "why": "Measles is far more than a rash — pneumonia and inflammation "
               "of the brain are recognised complications and can kill.",
    },
    {
        "id": "ks4-viral-diseases-s01",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "There is no specific antiviral drug for measles. Describe "
                "what actually clears the virus from a patient's body.",
        "options": [
            "The paracetamol kills the virus once the fever falls",
            "The patient's own immune system destroys the virus",
            "Antibiotics taken for the rash also clear the virus",
            "The liver filters the virus out of the blood",
        ],
        "correct_index": 1,
        "why": "Rest and fluids only support the patient; it is the "
               "lymphocytes and phagocytes that remove the virus.",
    },
    {
        "id": "ks4-viral-diseases-s02",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower finds one tomato plant with mosaic-patterned "
                "leaves. Suggest why they should disinfect their pruning "
                "tools before touching other plants.",
        "options": [
            "The tools would otherwise rust and become blunt",
            "Disinfectant acts as a fertiliser for healthy plants",
            "The virus can be carried on the tools to healthy plants",
            "Cleaning removes the fungal spores causing the mosaic",
        ],
        "correct_index": 2,
        "why": "Tobacco mosaic virus spreads by contact, so sap left on a "
               "blade takes the virus straight into the next plant's cut "
               "tissue.",
    },
    {
        "id": "ks4-viral-diseases-s03",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person can be infected with HIV for many "
                "years before becoming seriously ill.",
        "options": [
            "The virus destroys lymphocytes slowly, so the immune system "
            "copes for years",
            "The virus stays outside the body's cells until it is triggered",
            "The virus cannot reproduce until a second infection arrives",
            "Antibiotics keep the number of virus particles low for years",
        ],
        "correct_index": 0,
        "why": "The immune system copes until enough lymphocytes have been "
               "destroyed, and antiretroviral drugs push that point much "
               "further away.",
    },
    {
        "id": "ks4-viral-diseases-s04",
        "subtopic_slug": "viral-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why measles spreads very quickly through a crowded "
                "school.",
        "options": [
            "The virus survives for months on surfaces with no host",
            "Children of school age cannot make antibodies against the "
            "measles virus",
            "Measles bacteria divide rapidly in a warm classroom",
            "It travels in droplets from coughs, and pupils sit close "
            "together",
        ],
        "correct_index": 3,
        "why": "Droplet spread needs people close together, and a school puts "
               "hundreds of unprotected hosts within a metre of each other.",
    },
    {
        "id": "ks4-viral-diseases-h01",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener says the yellow patches on their tomato leaves "
                "must be a lack of magnesium rather than a virus. Suggest "
                "one observation that would support the virus instead.",
        "options": [
            "The plant is taller than the others growing in the same soil",
            "The yellowing appears first on the oldest leaves at the base",
            "Adding fertiliser to the soil makes the patches disappear",
            "Plants handled with the same tools show the same patchy pattern",
        ],
        "correct_index": 3,
        "why": "A mineral deficiency does not travel between plants, so "
               "symptoms following the path of the tools point to an "
               "infection.",
    },
    {
        "id": "ks4-viral-diseases-h02",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a drug that kills viruses is much harder to "
                "develop than one that kills bacteria.",
        "options": [
            "Viruses reproduce too quickly for a drug to reach them in time",
            "Viruses replicate inside host cells, so a drug may damage those "
            "cells too",
            "Viruses are living cells with the same structures as human cells",
            "Viruses are surrounded by thick cell walls that most drugs "
            "cannot pass through",
        ],
        "correct_index": 1,
        "why": "There is little a virus has that a host cell does not, so "
               "attacking the virus usually means attacking the patient's own "
               "cells.",
    },
    {
        "id": "ks4-viral-diseases-h03",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A blood transfusion service screens every donation for HIV "
                "even though donors are asked whether they have the virus. "
                "Explain why the screening is still necessary.",
        "options": [
            "HIV can be caught from the equipment used to take the blood",
            "Antibiotics in donated blood would hide the virus from tests",
            "A donor can carry HIV for years without symptoms and not know",
            "HIV is destroyed by refrigeration, so only fresh blood is risky",
        ],
        "correct_index": 2,
        "why": "An honest donor can still be infectious, because HIV causes "
               "no obvious illness for a long time after infection.",
    },
    {
        "id": "ks4-viral-diseases-h04",
        "subtopic_slug": "viral-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a country with a good antiretroviral programme, deaths "
                "from AIDS fall sharply while the number of people living "
                "with HIV rises. Explain this pattern.",
        "options": [
            "The drugs stop the virus replicating, so infected people live "
            "far longer",
            "The drugs cure HIV, so fewer people carry the virus each year",
            "The drugs make HIV spread more easily between treated people",
            "The drugs turn HIV into a bacterial infection that "
            "antibiotics are able to treat",
        ],
        "correct_index": 0,
        "why": "Antiretrovirals control the infection without removing it, so "
               "patients survive for decades and remain part of the count.",
    },

    # ── bacterial-diseases ───────────────────────────────────────────────
    {
        "id": "ks4-bacterial-diseases-e01",
        "subtopic_slug": "bacterial-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which type of pathogen causes gonorrhoea?",
        "options": [
            "A virus",
            "A bacterium",
            "A fungus",
            "A protist",
        ],
        "correct_index": 1,
        "why": "Gonorrhoea is caused by the bacterium Neisseria gonorrhoeae, "
               "which is why antibiotics can treat it at all.",
    },
    {
        "id": "ks4-bacterial-diseases-e02",
        "subtopic_slug": "bacterial-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "How long after eating contaminated food do the symptoms of "
                "Salmonella food poisoning usually begin?",
        "options": [
            "Within a few minutes",
            "After about three weeks",
            "After about six months",
            "Between 12 and 72 hours",
        ],
        "correct_index": 3,
        "why": "The bacteria need time to reach the intestine and multiply "
               "before enough toxin is produced to cause symptoms.",
    },
    {
        "id": "ks4-bacterial-diseases-e03",
        "subtopic_slug": "bacterial-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the main way in which many bacteria damage the body's "
                "tissues.",
        "options": [
            "They release toxins that damage cells",
            "They inject genetic material into cells",
            "They use up all the oxygen in the blood",
            "They stop the body making any antibodies",
        ],
        "correct_index": 0,
        "why": "Most bacterial symptoms come from the chemicals the bacteria "
               "secrete rather than from the bacteria themselves.",
    },
    {
        "id": "ks4-bacterial-diseases-e04",
        "subtopic_slug": "bacterial-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which method of contraception also reduces the spread of "
                "gonorrhoea?",
        "options": [
            "The contraceptive pill",
            "An intrauterine device",
            "Condoms",
            "A contraceptive implant",
        ],
        "correct_index": 2,
        "why": "Only a barrier method stops the bacteria passing between "
               "people; hormonal methods do nothing to block an infection.",
    },
    {
        "id": "ks4-bacterial-diseases-s01",
        "subtopic_slug": "bacterial-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fridge is set to 4 °C. Explain how this reduces the risk "
                "of Salmonella food poisoning.",
        "options": [
            "It kills all the Salmonella on the food within a few hours",
            "It destroys any toxin the bacteria have already produced",
            "It slows their reproduction, so far fewer build up",
            "It makes the food too acidic for the bacteria to survive",
        ],
        "correct_index": 2,
        "why": "Cold does not kill Salmonella — it only slows the division "
               "that would otherwise take the numbers to a dangerous level.",
    },
    {
        "id": "ks4-bacterial-diseases-s02",
        "subtopic_slug": "bacterial-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why many women with gonorrhoea pass the infection on "
                "without knowing they have it.",
        "options": [
            "The bacteria are only infectious before any symptoms appear",
            "The infection is often symptom-free, so it goes undiagnosed",
            "Antibiotics remove the symptoms but leave a person infectious",
            "The discharge can only be seen through a clinic microscope",
        ],
        "correct_index": 1,
        "why": "Gonorrhoea is frequently asymptomatic in women, so nothing "
               "prompts them to seek the test that would find it.",
    },
    {
        "id": "ks4-bacterial-diseases-s03",
        "subtopic_slug": "bacterial-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Under ideal conditions a bacterium divides every 20 minutes. "
                "Calculate the number of bacteria present after 2 hours, "
                "starting from one bacterium.",
        "options": [
            "6 bacteria",
            "12 bacteria",
            "120 bacteria",
            "64 bacteria",
        ],
        "correct_index": 3,
        "why": "Two hours is six divisions, and the number doubles each time: "
               "2⁶ = 64.",
    },
    {
        "id": "ks4-bacterial-diseases-s04",
        "subtopic_slug": "bacterial-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why penicillin damages bacteria but does not damage "
                "the patient's own cells.",
        "options": [
            "It disrupts cell wall building, and human cells have no wall",
            "Human cells are much larger, so the drug cannot enter them",
            "Human cells have a nucleus that shields them from the drug",
            "Bacteria absorb the drug faster because they have no membrane",
        ],
        "correct_index": 0,
        "why": "Penicillin blocks the building of the bacterial cell wall — "
               "a structure a human cell does not have at all, so there is "
               "nothing in the patient for it to attack.",
    },
    {
        "id": "ks4-bacterial-diseases-h01",
        "subtopic_slug": "bacterial-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient is treated successfully for gonorrhoea but is "
                "infected again a month later. Their partner was never "
                "tested. Explain the most likely reason.",
        "options": [
            "The untreated partner still carries the bacteria and passed it "
            "back",
            "Antibiotic treatment gives only one month of immunity",
            "Memory cells for bacteria are lost about four weeks afterwards",
            "The antibiotic course makes a patient more likely to be "
            "reinfected",
        ],
        "correct_index": 0,
        "why": "Treatment clears the bacteria from one person but gives no "
               "immunity, so an untreated partner simply reinfects them.",
    },
    {
        "id": "ks4-bacterial-diseases-h02",
        "subtopic_slug": "bacterial-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why gonorrhoea that is left untreated can lead to "
                "infertility in women.",
        "options": [
            "The bacteria destroy the egg cells stored in the ovaries",
            "The infection stops the pituitary gland releasing FSH and LH",
            "It spreads to the reproductive organs, causing damage there",
            "The antibodies made against it attack the lining of the uterus",
        ],
        "correct_index": 2,
        "why": "Untreated bacteria travel upwards into the reproductive "
               "tract, and the inflammation they cause scars the oviducts.",
    },
    {
        "id": "ks4-bacterial-diseases-h03",
        "subtopic_slug": "bacterial-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A food company vaccinates its chicken flocks against "
                "Salmonella. Explain how this protects human customers.",
        "options": [
            "The vaccine passes into the meat and immunises whoever eats it",
            "Fewer chickens carry the bacteria, so less meat is contaminated",
            "The vaccine kills bacteria already present in the chicken meat",
            "Vaccinated chickens make antibodies that survive the cooking",
        ],
        "correct_index": 1,
        "why": "The vaccine protects the birds, and a flock that is not "
               "infected cannot pass Salmonella into the food chain.",
    },
    {
        "id": "ks4-bacterial-diseases-h04",
        "subtopic_slug": "bacterial-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student concludes that because Salmonella is killed by "
                "heat, food poisoning cannot happen if a meal is served hot. "
                "Evaluate this conclusion.",
        "options": [
            "Correct — heat destroys the bacteria and their toxins together",
            "Correct, as long as the meal is eaten within an hour of cooking",
            "Wrong, because Salmonella bacteria are not killed by heat",
            "Wrong — cooked food can be recontaminated after it is cooked",
        ],
        "correct_index": 3,
        "why": "Cooking only makes food safe at the moment of cooking; raw "
               "meat juices or unwashed hands can put the bacteria straight "
               "back.",
    },

    # ── fungal-protist-diseases ──────────────────────────────────────────
    {
        "id": "ks4-fungal-protist-diseases-e01",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these human diseases is caused by a fungus?",
        "options": [
            "Malaria",
            "Gonorrhoea",
            "Measles",
            "Athlete's foot",
        ],
        "correct_index": 3,
        "why": "Athlete's foot is a fungal infection of the skin, spread by "
               "direct contact with contaminated surfaces.",
    },
    {
        "id": "ks4-fungal-protist-diseases-e02",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Plasmodium, the pathogen that causes malaria, belongs to "
                "which group of organisms?",
        "options": [
            "Bacteria",
            "Protists",
            "Viruses",
            "Fungi",
        ],
        "correct_index": 1,
        "why": "Plasmodium is a single-celled eukaryote — a protist — and not "
               "a bacterium, which is why antibiotics do not treat malaria.",
    },
    {
        "id": "ks4-fungal-protist-diseases-e03",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Why should a gardener not put leaves infected with rose "
                "black spot onto a compost heap?",
        "options": [
            "The leaves will not rot because the fungus has hardened them",
            "Compost made from them would be poisonous to other plants",
            "The fungal spores survive and can infect plants again",
            "The fungus would turn the whole compost heap black and sticky",
        ],
        "correct_index": 2,
        "why": "Spores are tough enough to survive in compost, so the "
               "gardener would be storing next year's infection.",
    },
    {
        "id": "ks4-fungal-protist-diseases-e04",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener buys a rose described as a disease-resistant "
                "variety. What does this mean?",
        "options": [
            "It is much less likely to develop black spot if spores land",
            "It cannot be infected by any pathogen at any time of the year",
            "It has been sprayed with fungicide before being sold",
            "It produces antibodies against the black spot fungus",
        ],
        "correct_index": 0,
        "why": "Resistance reduces the chance of infection taking hold; it is "
               "not the same as being immune, and plants make no antibodies.",
    },
    {
        "id": "ks4-fungal-protist-diseases-s01",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why rose black spot spreads faster during a warm, "
                "wet summer.",
        "options": [
            "Rain splashes spores between leaves and warmth speeds growth",
            "Warm air makes the fungus reproduce sexually instead of by "
            "spores",
            "Rain washes fungicide down into the soil, where it kills roots",
            "Wet leaves close their stomata, trapping spores inside the leaf",
        ],
        "correct_index": 0,
        "why": "The spores need water to travel and to germinate, and warmth "
               "speeds up the fungus once it is on the leaf.",
    },
    {
        "id": "ks4-fungal-protist-diseases-s02",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why draining pools of standing water near a village "
                "reduces the number of malaria cases.",
        "options": [
            "Plasmodium lives in still water and infects people who drink it",
            "Standing water dilutes the anti-malarial drugs villagers take",
            "Mosquitoes drown in moving water but not in standing water",
            "Mosquitoes breed in standing water, so fewer vectors develop",
        ],
        "correct_index": 3,
        "why": "Removing the breeding sites cuts the mosquito population, and "
               "fewer vectors means fewer bites carrying Plasmodium.",
    },
    {
        "id": "ks4-fungal-protist-diseases-s03",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person with malaria may become anaemic.",
        "options": [
            "The protist digests iron in the food before it is absorbed",
            "Plasmodium destroys red blood cells faster than replacement",
            "The high fever denatures the haemoglobin inside the cells",
            "Mosquito bites remove a large volume of blood every night",
        ],
        "correct_index": 1,
        "why": "Anaemia is a shortage of working red blood cells, and "
               "Plasmodium destroys them in cycles as it reproduces.",
    },
    {
        "id": "ks4-fungal-protist-diseases-s04",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener waters their roses at the base of the plant "
                "rather than over the leaves. Explain how this helps to "
                "prevent black spot.",
        "options": [
            "Water at the base carries fungicide directly to the roots",
            "Dry roots stop the fungus entering through the root hairs",
            "Dry leaves make it harder for spores to germinate and spread",
            "It keeps the soil dry, so spores in the soil cannot survive",
        ],
        "correct_index": 2,
        "why": "The fungus needs a film of water on the leaf to germinate, so "
               "keeping the leaves dry removes what it needs.",
    },
    {
        "id": "ks4-fungal-protist-diseases-h01",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Travellers to a malarial region take anti-malarial tablets "
                "and sleep under an insecticide-treated net. Explain why both "
                "are used rather than one.",
        "options": [
            "The tablets kill the mosquitoes and the net kills the protist",
            "The net kills the protist while the tablets repel the insects",
            "The net cuts the chance of a bite; the tablets act if one "
            "happens",
            "Both act at the same stage, so the effect is simply doubled",
        ],
        "correct_index": 2,
        "why": "The two measures attack different points in the transmission "
               "cycle, so one covers what the other misses.",
    },
    {
        "id": "ks4-fungal-protist-diseases-h02",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says malaria could be wiped out by giving everyone "
                "a vaccine against the Anopheles mosquito. Explain what is "
                "wrong with this idea.",
        "options": [
            "A vaccine works against a pathogen, and the mosquito is not one",
            "Vaccines only work against bacteria, so this one is impossible",
            "Nothing is wrong — vaccinating against mosquitoes would work",
            "Mosquitoes are too large for antibodies to bind to them",
        ],
        "correct_index": 0,
        "why": "The disease is caused by Plasmodium; the mosquito is only the "
               "vector that carries it, so it is not what the immune system "
               "would be primed against.",
    },
    {
        "id": "ks4-fungal-protist-diseases-h03",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rose grower sprays fungicide but leaves the fallen "
                "infected leaves lying on the soil. Explain why black spot "
                "returns the following year.",
        "options": [
            "Fungicide loses its effect after a week in bright sunlight",
            "The fungus becomes resistant to the fungicide within a single "
            "season",
            "New leaves grow with the disease already inside them",
            "Spores survive on the fallen leaves and splash back up in spring",
        ],
        "correct_index": 3,
        "why": "The fallen leaves are a reservoir of living spores, so rain "
               "simply reinfects the new growth.",
    },
    {
        "id": "ks4-fungal-protist-diseases-h04",
        "subtopic_slug": "fungal-protist-diseases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why anti-malarial drugs are becoming less effective "
                "in some parts of the world.",
        "options": [
            "People build up a tolerance, so they need a larger dose",
            "Plasmodium with resistance mutations survive and reproduce",
            "The mosquitoes have become immune to the drugs they carry",
            "The drugs break down in hot climates before they are taken",
        ],
        "correct_index": 1,
        "why": "The drug acts as a selection pressure on the protist "
               "population, and only the resistant individuals go on to "
               "breed.",
    },

    # ── vaccination ──────────────────────────────────────────────────────
    {
        "id": "ks4-vaccination-e01",
        "subtopic_slug": "vaccination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these can a vaccine contain?",
        "options": [
            "A dead or weakened form of the pathogen",
            "A live, full-strength pathogen that causes the disease",
            "Antibiotics that kill the pathogen before it multiplies",
            "Ready-made antibodies taken from an immune person",
        ],
        "correct_index": 0,
        "why": "A vaccine has to carry the antigens without the danger, so "
               "the pathogen in it is dead, weakened, or reduced to "
               "fragments.",
    },
    {
        "id": "ks4-vaccination-e02",
        "subtopic_slug": "vaccination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which vaccine is given to teenagers to reduce their risk of "
                "cervical cancer in later life?",
        "options": [
            "The MMR vaccine",
            "The polio vaccine",
            "The seasonal flu vaccine",
            "The HPV vaccine",
        ],
        "correct_index": 3,
        "why": "Human papillomavirus causes most cervical cancers, so "
               "vaccinating before exposure prevents the infection that "
               "leads to them.",
    },
    {
        "id": "ks4-vaccination-e03",
        "subtopic_slug": "vaccination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one common side effect of being vaccinated.",
        "options": [
            "A rash identical to the disease being vaccinated against",
            "Permanent damage to the immune system",
            "Soreness at the injection site for a day or two",
            "A long-lasting infection that needs antibiotics",
        ],
        "correct_index": 2,
        "why": "Mild soreness and a slight fever are the immune system "
               "responding to the antigens, not the disease itself.",
    },
    {
        "id": "ks4-vaccination-e04",
        "subtopic_slug": "vaccination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Some people cannot be given a vaccine. Which of these is a "
                "reason?",
        "options": [
            "They have already had a different vaccine earlier in their life",
            "They are having chemotherapy, which weakens the immune system",
            "They have a strong immune system that would reject it",
            "They are over the age of eighteen years old",
        ],
        "correct_index": 1,
        "why": "A vaccine relies on the patient mounting an immune response, "
               "which a person on chemotherapy may be unable to do safely.",
    },
    {
        "id": "ks4-vaccination-s01",
        "subtopic_slug": "vaccination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A parent says the flu vaccine gave their child flu because "
                "the child had a mild fever the next day. Explain what "
                "actually caused the fever.",
        "options": [
            "The vaccine contained live influenza virus at full strength",
            "The immune system was responding to the harmless antigens",
            "The antibodies in the vaccine attacked the child's own cells",
            "The child caught flu from the needle used for the injection",
        ],
        "correct_index": 1,
        "why": "A mild fever is the normal sign of lymphocytes being "
               "stimulated — the vaccine cannot cause the disease itself.",
    },
    {
        "id": "ks4-vaccination-s02",
        "subtopic_slug": "vaccination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Measles vaccination in a town falls from almost every child "
                "to about two thirds of children, and an outbreak follows. "
                "Explain why.",
        "options": [
            "Enough people were unprotected for the virus to pass on again",
            "The vaccine already given stopped working once rates fell",
            "The measles virus mutated because fewer children were "
            "vaccinated",
            "Unvaccinated children make antibodies that help the virus spread",
        ],
        "correct_index": 0,
        "why": "Transmission continues whenever an infected person keeps "
               "meeting susceptible people, so unprotected numbers decide "
               "whether an outbreak takes off.",
    },
    {
        "id": "ks4-vaccination-s03",
        "subtopic_slug": "vaccination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A newborn baby is too young for the MMR vaccine. Explain how "
                "vaccinating the older children in the family helps to "
                "protect the baby.",
        "options": [
            "Antibodies pass from the vaccinated children to the baby in air",
            "The baby's immune system copies the response the children made",
            "Vaccinated children carry the virus harmlessly and pass immunity",
            "Vaccinated children are unlikely to catch it, so cannot pass it "
            "on",
        ],
        "correct_index": 3,
        "why": "The baby is protected indirectly: the people closest to it "
               "are no longer able to bring the virus home.",
    },
    {
        "id": "ks4-vaccination-s04",
        "subtopic_slug": "vaccination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a country continues a polio vaccination "
                "programme even though very few cases now occur.",
        "options": [
            "Polio cases only occur in people who have been vaccinated",
            "Vaccination cures the people who already have polio",
            "Cases would rise again if the virus reached an unprotected "
            "population",
            "The vaccine kills the virus in the environment as well as in "
            "people",
        ],
        "correct_index": 2,
        "why": "Low case numbers are the result of the programme, not a "
               "reason to stop it — the virus still exists elsewhere.",
    },
    {
        "id": "ks4-vaccination-h01",
        "subtopic_slug": "vaccination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a trial, cases of a disease fell by 80% in a vaccinated "
                "area and by 20% in a neighbouring area where nobody was "
                "vaccinated. Suggest why the second area saw any fall.",
        "options": [
            "The vaccine was carried between the two areas in the air",
            "People there developed natural immunity at the same time",
            "Fewer infected people travelled in from the vaccinated area",
            "The pathogen mutated into a harmless form in both areas",
        ],
        "correct_index": 2,
        "why": "Cutting infections in one population reduces how often its "
               "neighbours are exposed, so protection spills across the "
               "boundary.",
    },
    {
        "id": "ks4-vaccination-h02",
        "subtopic_slug": "vaccination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that once you have been vaccinated you can "
                "never catch that disease. Evaluate this statement.",
        "options": [
            "Correct — vaccination gives complete protection for life",
            "Wrong — vaccination greatly lowers the risk but is not total",
            "Wrong — a vaccine only works while it remains in the blood",
            "Correct, provided a course of antibiotics is also completed",
        ],
        "correct_index": 1,
        "why": "Vaccination prepares the immune system so infection is "
               "usually stopped early, but no vaccine protects every person "
               "every time.",
    },
    {
        "id": "ks4-vaccination-h03",
        "subtopic_slug": "vaccination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a booster dose of a vaccine is given some years "
                "after the first dose.",
        "options": [
            "It stimulates the immune system again, raising memory cell "
            "numbers",
            "It replaces the antibodies from the first dose, now used up",
            "It contains a stronger pathogen than the first dose did",
            "It kills any of the pathogen that entered since the first dose",
        ],
        "correct_index": 0,
        "why": "A second exposure to the antigen builds a larger, longer "
               "lasting population of memory cells than one dose can.",
    },
    {
        "id": "ks4-vaccination-h04",
        "subtopic_slug": "vaccination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two programmes cost the same. Programme A vaccinates nearly "
                "all the children in one town; Programme B vaccinates about "
                "half the children in two towns. Suggest which better "
                "prevents an outbreak, and why.",
        "options": [
            "B, because twice as many towns are covered for the same money",
            "B, because the pathogen is spread thinly over a larger area",
            "A, because a vaccine only works when given to fewer people",
            "A, because at half coverage the pathogen still passes easily",
        ],
        "correct_index": 3,
        "why": "Transmission is only broken once most of a population is "
               "immune; half-protecting two towns leaves both able to sustain "
               "an outbreak.",
    },

    # ── antibiotics-painkillers ──────────────────────────────────────────
    {
        "id": "ks4-antibiotics-painkillers-e01",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Who discovered penicillin, and what was it produced by?",
        "options": [
            "Edward Jenner, from cowpox in dairy cattle",
            "Louis Pasteur, from soured milk",
            "Alexander Fleming, from Penicillium mould",
            "Joseph Lister, from carbolic acid",
        ],
        "correct_index": 2,
        "why": "Fleming noticed in 1928 that bacteria would not grow near a "
               "mould contaminating one of his plates.",
    },
    {
        "id": "ks4-antibiotics-painkillers-e02",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "What does it mean to call an antibiotic broad spectrum?",
        "options": [
            "It kills both bacteria and viruses",
            "It works against many different species of bacteria",
            "It can safely be taken by patients of any age",
            "It treats the symptoms as well as the infection",
        ],
        "correct_index": 1,
        "why": "Broad spectrum describes the range of bacteria affected — it "
               "says nothing about viruses, which no antibiotic touches.",
    },
    {
        "id": "ks4-antibiotics-painkillers-e03",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is a well-known example of an "
                "antibiotic-resistant bacterium?",
        "options": [
            "MRSA",
            "Plasmodium",
            "Tobacco mosaic virus",
            "Diplocarpon rosae",
        ],
        "correct_index": 0,
        "why": "MRSA is a strain of Staphylococcus aureus that survives the "
               "antibiotics that once treated it easily.",
    },
    {
        "id": "ks4-antibiotics-painkillers-e04",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Some countries have reduced the use of antibiotics on farms. "
                "State why this is done.",
        "options": [
            "To make meat cheaper for farmers to produce",
            "To stop the animals becoming immune to antibiotics",
            "To prevent antibiotics from making animals grow too quickly",
            "To slow the development of antibiotic-resistant bacteria",
        ],
        "correct_index": 3,
        "why": "Every use of an antibiotic selects for resistant bacteria, "
               "and resistant strains from livestock reach people through "
               "food.",
    },
    {
        "id": "ks4-antibiotics-painkillers-s01",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient with a bacterial chest infection is prescribed "
                "both an antibiotic and a painkiller. Explain why both are "
                "needed.",
        "options": [
            "The painkiller helps the antibiotic enter the bacterial cells",
            "The antibiotic treats the fever and the painkiller the bacteria",
            "Two drugs are given so the bacteria cannot resist either one",
            "The antibiotic treats the cause; the painkiller the symptoms",
        ],
        "correct_index": 3,
        "why": "Only the antibiotic removes the bacteria; the painkiller "
               "makes the patient comfortable while it does so.",
    },
    {
        "id": "ks4-antibiotics-painkillers-s02",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why prescribing antibiotics 'just in case' for an "
                "illness known to be viral is harmful.",
        "options": [
            "The patient's own cells become resistant to the antibiotic",
            "The antibiotic reacts with the virus to produce a stronger "
            "strain of it",
            "It exposes the body's bacteria to the drug, selecting resistant "
            "ones",
            "It uses up the patient's supply of white blood cells",
        ],
        "correct_index": 2,
        "why": "The antibiotic cannot touch the virus, but it does act as a "
               "selection pressure on every bacterium the patient carries.",
    },
    {
        "id": "ks4-antibiotics-painkillers-s03",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a mutation can make a bacterium resistant to an "
                "antibiotic.",
        "options": [
            "The bacterium copies resistance from a human cell it infects",
            "A random DNA change alters a structure the antibiotic targets",
            "The bacterium chooses to change its wall when it meets the drug",
            "The antibiotic makes the bacterium mutate in order to survive",
        ],
        "correct_index": 1,
        "why": "Mutations happen at random before the drug arrives; the "
               "antibiotic only decides which bacteria survive.",
    },
    {
        "id": "ks4-antibiotics-painkillers-s04",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an antibiotic that works well against one "
                "species of bacterium may not work against another.",
        "options": [
            "The species differ, so the drug's target may not be present",
            "One of the two species is a virus, so is unaffected by the drug",
            "Antibiotics only work on bacteria that use binary fission",
            "The second species has been vaccinated against the antibiotic",
        ],
        "correct_index": 0,
        "why": "An antibiotic attacks one particular bacterial structure, and "
               "not every species is built the same way.",
    },
    {
        "id": "ks4-antibiotics-painkillers-h01",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "MRSA infections in a hospital fall after a rule that "
                "antibiotics may only be given once a laboratory test has "
                "confirmed a bacterial infection. Explain why.",
        "options": [
            "Less antibiotic use means less selection for resistant strains",
            "Laboratory tests kill resistant bacteria before they reach wards",
            "MRSA cannot survive in a hospital where fewer drugs are used",
            "Patients are given painkillers instead, which kill MRSA slowly",
        ],
        "correct_index": 0,
        "why": "Resistant bacteria only gain an advantage while the "
               "antibiotic is present, so using less of it slows their "
               "spread.",
    },
    {
        "id": "ks4-antibiotics-painkillers-h02",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'After a course of antibiotics, the "
                "patient becomes resistant to the antibiotic.' Identify the "
                "error and correct it.",
        "options": [
            "The error is 'course' — resistance needs several courses first",
            "There is no error; patients do become resistant over time",
            "The error is 'antibiotic' — resistance develops to painkillers",
            "It is the bacteria, not the patient, that become resistant",
        ],
        "correct_index": 3,
        "why": "Resistance is a property of a bacterial population that has "
               "been selected by the drug, not something a human body "
               "acquires.",
    },
    {
        "id": "ks4-antibiotics-painkillers-h03",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A company develops a completely new antibiotic. Suggest why "
                "this may not solve the problem of resistance permanently.",
        "options": [
            "New antibiotics stop working once their patent runs out",
            "Bacteria become immune to it the first time they meet it",
            "Resistance to it will be selected for once it is widely used",
            "The bacteria will pass the new drug on to the next generation",
        ],
        "correct_index": 2,
        "why": "Any antibiotic in wide use becomes a selection pressure, and "
               "rare resistant mutants then have the advantage.",
    },
    {
        "id": "ks4-antibiotics-painkillers-h04",
        "subtopic_slug": "antibiotics-painkillers",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how a vaccine and an antibiotic act against the same "
                "bacterial disease.",
        "options": [
            "Both kill the bacteria directly once they enter the bloodstream",
            "A vaccine prepares the immune system; an antibiotic kills "
            "bacteria",
            "A vaccine kills the bacteria; an antibiotic trains the immune "
            "system",
            "Both are only useful once the symptoms have already appeared",
        ],
        "correct_index": 1,
        "why": "A vaccine is given before infection and works through the "
               "patient's own lymphocytes; an antibiotic is a drug given "
               "after infection.",
    },

    # ── drug-discovery-development ───────────────────────────────────────
    {
        "id": "ks4-drug-discovery-development-e01",
        "subtopic_slug": "drug-discovery-development",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aspirin was originally developed from a substance found in "
                "which plant?",
        "options": [
            "The opium poppy",
            "The willow tree",
            "The foxglove",
            "The cinchona tree",
        ],
        "correct_index": 1,
        "why": "Willow bark contains salicylic acid, which was used as a pain "
               "reliever long before aspirin was made from it.",
    },
    {
        "id": "ks4-drug-discovery-development-e02",
        "subtopic_slug": "drug-discovery-development",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which drug was originally extracted from the bark of the "
                "cinchona tree and used against malaria?",
        "options": [
            "Quinine",
            "Morphine",
            "Penicillin",
            "Paracetamol",
        ],
        "correct_index": 0,
        "why": "Quinine from cinchona bark was the first effective treatment "
               "for malaria and is still the basis of some drugs today.",
    },
    {
        "id": "ks4-drug-discovery-development-e03",
        "subtopic_slug": "drug-discovery-development",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which body must approve a new medicine in the UK before "
                "doctors are allowed to prescribe it?",
        "options": [
            "The World Health Organization",
            "The National Health Service",
            "The drug company's own board of directors",
            "The MHRA, the UK medicines regulator",
        ],
        "correct_index": 3,
        "why": "The MHRA reviews all the trial evidence independently before "
               "a drug can be licensed for use.",
    },
    {
        "id": "ks4-drug-discovery-development-e04",
        "subtopic_slug": "drug-discovery-development",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In drug testing, what does the toxicity of a drug mean?",
        "options": [
            "How quickly the drug is absorbed into the blood",
            "How well the drug treats the disease it is aimed at",
            "How harmful the drug is to the body",
            "How long the drug stays active inside the body",
        ],
        "correct_index": 2,
        "why": "Toxicity is about harm; how well a drug works is its "
               "efficacy, and the two are tested separately.",
    },
    {
        "id": "ks4-drug-discovery-development-s01",
        "subtopic_slug": "drug-discovery-development",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the first human volunteers to receive a new drug "
                "are given very low doses.",
        "options": [
            "A low dose is all that is needed to show the drug works",
            "A low dose stops volunteers guessing which group they are in",
            "It limits the harm done if the drug is toxic in humans",
            "Low doses stop volunteers becoming addicted to the drug",
        ],
        "correct_index": 2,
        "why": "Nothing before this point has shown how a human body will "
               "react, so the dose is kept small and raised slowly.",
    },
    {
        "id": "ks4-drug-discovery-development-s02",
        "subtopic_slug": "drug-discovery-development",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a new painkiller is tested on cells grown in the "
                "laboratory before it is given to any animal.",
        "options": [
            "Cells respond to a drug in exactly the same way as an animal",
            "Cell cultures show how the liver breaks the drug down",
            "A drug that works on cells is certain to work in a patient too",
            "It screens out toxic compounds before any animal is used",
        ],
        "correct_index": 3,
        "why": "Testing on cells removes the obviously harmful compounds "
               "early, so far fewer animals are needed.",
    },
    {
        "id": "ks4-drug-discovery-development-s03",
        "subtopic_slug": "drug-discovery-development",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a new drug is tested on animals as well as on "
                "cells grown in the laboratory.",
        "options": [
            "Only a whole organism shows how a drug is absorbed and broken "
            "down",
            "Animals have body systems identical to those of humans",
            "Animal testing removes the need for any human trials later",
            "Animals cannot show a placebo effect, so the results are much "
            "clearer",
        ],
        "correct_index": 0,
        "why": "A cell in a dish has no circulation, liver or kidneys, so it "
               "cannot show what happens to a drug in a living body.",
    },
    {
        "id": "ks4-drug-discovery-development-s04",
        "subtopic_slug": "drug-discovery-development",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A trial compares a new drug against the treatment already in "
                "use rather than against a dummy tablet. Suggest why.",
        "options": [
            "Dummy tablets are banned in trials involving ill patients",
            "It is unfair to leave ill patients untreated when a treatment "
            "exists",
            "An existing treatment acts as a dummy tablet because patients "
            "trust it",
            "Comparing against a dummy would need twice as many patients",
        ],
        "correct_index": 1,
        "why": "Where an effective treatment already exists, withholding it "
               "from seriously ill patients cannot be justified.",
    },
    {
        "id": "ks4-drug-discovery-development-h01",
        "subtopic_slug": "drug-discovery-development",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drug performs well in a trial on a few hundred patients "
                "but fails when tested on several thousand. Suggest why a "
                "much larger trial can reach a different conclusion.",
        "options": [
            "Larger trials use higher doses, which always cause failure",
            "The drug becomes less effective the longer it is stored",
            "The larger trial uses only healthy people who do not need the "
            "drug at all",
            "Rare side effects and small differences only show in large "
            "numbers",
        ],
        "correct_index": 3,
        "why": "A side effect that affects one patient in a thousand cannot "
               "appear at all in a group of two hundred.",
    },
    {
        "id": "ks4-drug-discovery-development-h02",
        "subtopic_slug": "drug-discovery-development",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Thalidomide is prescribed again today, under strict "
                "controls, to treat some cancers. Evaluate whether this was a "
                "reasonable decision.",
        "options": [
            "No — a drug that has caused harm can never be safe for anyone",
            "No — patients with cancer could be given a sedative instead",
            "Yes — the risk is acceptable if it is kept away from pregnancy",
            "Yes — the birth defects were later shown to have another cause",
        ],
        "correct_index": 2,
        "why": "The harm thalidomide caused was to developing embryos, so the "
               "benefit can outweigh the risk in patients who cannot become "
               "pregnant.",
    },
    {
        "id": "ks4-drug-discovery-development-h03",
        "subtopic_slug": "drug-discovery-development",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a trial the doctors know which patients are receiving "
                "the real drug. Suggest how this could affect the results "
                "even if every doctor is completely honest.",
        "options": [
            "The doctors would give the real drug to the healthiest patients",
            "They may judge improvement more generously in the treated group",
            "All the patients would improve because the doctors know",
            "The drug would work better because the doctors expect it to",
        ],
        "correct_index": 1,
        "why": "Expectation shifts a judgement without any dishonesty, which "
               "is exactly why the doctors are kept unaware as well as the "
               "patients.",
    },
    {
        "id": "ks4-drug-discovery-development-h04",
        "subtopic_slug": "drug-discovery-development",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A company claims its new drug works because 40 out of 50 "
                "patients improved in a study with no comparison group. "
                "Evaluate this claim.",
        "options": [
            "Weak — with no comparison group the improvement may not be due "
            "to the drug",
            "Strong — 80% is a high enough success rate to prove it works",
            "Weak — a drug must work for every single patient before it "
            "can be approved",
            "Strong, provided the patients did not know they were studied",
        ],
        "correct_index": 0,
        "why": "Without a control group there is nothing to show the patients "
               "would not have improved anyway.",
    },

    # ── plant-disease-detection-defence (TRIPLE) ─────────────────────────
    {
        "id": "ks4-plant-disease-detection-defence-e01",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which of these is a common symptom of disease in a plant?",
        "options": [
            "An increase in the number of flowers produced",
            "Faster growth than nearby plants of the same age",
            "Thicker, greener leaves than usual for the species",
            "Areas of soft, decaying tissue on the stem",
        ],
        "correct_index": 3,
        "why": "Rot, stunted growth, spots, growths and discolouration are "
               "the recognised signs; healthy vigour is not one of them.",
    },
    {
        "id": "ks4-plant-disease-detection-defence-e02",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which chemical, made by coffee and tea plants, deters "
                "insects from feeding on them?",
        "options": [
            "Caffeine",
            "Allicin",
            "Insulin",
            "Cellulose",
        ],
        "correct_index": 0,
        "why": "Caffeine is a plant alkaloid — a chemical defence that is "
               "toxic to the insects that would otherwise eat the leaves.",
    },
    {
        "id": "ks4-plant-disease-detection-defence-e03",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which physical defence protects the living tissue inside a "
                "woody stem?",
        "options": [
            "The waxy cuticle",
            "The bark",
            "The root hairs",
            "The guard cells",
        ],
        "correct_index": 1,
        "why": "Bark is a tough dead outer layer that keeps pathogens and "
               "damage away from the phloem and cambium beneath.",
    },
    {
        "id": "ks4-plant-disease-detection-defence-e04",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "How can a grower confirm which pathogen is causing the "
                "symptoms they can see on a plant?",
        "options": [
            "By counting how many leaves have fallen from the plant",
            "By measuring how tall the plant has grown this year",
            "By sending a sample to a laboratory to be examined",
            "By checking whether the plant flowered at the usual time",
        ],
        "correct_index": 2,
        "why": "Symptoms alone can have several causes, so identification "
               "needs microscopy or a test kit that detects the pathogen "
               "itself.",
    },
    {
        "id": "ks4-plant-disease-detection-defence-s01",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a plant closes its stomata when it detects a "
                "pathogen.",
        "options": [
            "Stomata are openings through which pathogens can enter the leaf",
            "Closing them starves the pathogen of the sugars it needs",
            "Closed stomata release antibacterial gases onto the surface",
            "Closing them raises leaf temperature enough to kill spores",
        ],
        "correct_index": 0,
        "why": "The stomata are the one gap in the waxy cuticle, so closing "
               "them shuts the easiest route into the leaf.",
    },
    {
        "id": "ks4-plant-disease-detection-defence-s02",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why sticky resin is a useful defence against insect "
                "pests.",
        "options": [
            "The resin dissolves an insect's exoskeleton on contact",
            "It traps insects or clogs the mouthparts they feed with",
            "It attracts predators that then eat the insects present",
            "It seals the stomata so insects cannot lay eggs inside",
        ],
        "correct_index": 1,
        "why": "An insect that cannot feed or move on does no damage and "
               "cannot carry a pathogen to the next plant.",
    },
    {
        "id": "ks4-plant-disease-detection-defence-s03",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A farmer uses a test kit in the field rather than sending "
                "leaves away to a laboratory. Suggest one advantage of this.",
        "options": [
            "The kit can identify any pathogen, known or unknown",
            "The kit also treats the disease that it has detected",
            "A result comes quickly, so the crop can be treated sooner",
            "The kit is more accurate than examination under a microscope",
        ],
        "correct_index": 2,
        "why": "Speed matters because a pathogen keeps spreading through the "
               "crop while a laboratory sample is in the post.",
    },
    {
        "id": "ks4-plant-disease-detection-defence-s04",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why thorns reduce the chance of a plant becoming "
                "infected, as well as reducing how much of it is eaten.",
        "options": [
            "Thorns release a poison into any animal that touches them",
            "Thorns close over wounds in the stem in order to seal them",
            "Thorns absorb the pathogens carried in an animal's mouth",
            "Fewer animals bite the plant, so fewer wounds let pathogens in",
        ],
        "correct_index": 3,
        "why": "A bite is a break in the plant's barrier, and pathogens enter "
               "most easily through damaged tissue.",
    },
    {
        "id": "ks4-plant-disease-detection-defence-h01",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "After one leaf is infected, the other leaves on the same "
                "plant resist the same pathogen better. Explain how this "
                "happens.",
        "options": [
            "Antibodies made in the infected leaf travel to the others",
            "Memory cells in the stem recognise the pathogen if it returns",
            "Signalling chemicals travel through the plant, switching on "
            "defences",
            "The infected leaf falls off the plant, taking the whole "
            "infection with it",
        ],
        "correct_index": 2,
        "why": "Plants have no antibodies or memory cells — resistance "
               "spreads as a chemical signal that primes defences elsewhere.",
    },
    {
        "id": "ks4-plant-disease-detection-defence-h02",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says a plant makes antibodies when bacteria "
                "attack it. Explain why this is wrong.",
        "options": [
            "Plants make antibodies, but only in the roots and not in leaves",
            "Plants make antibiotics instead, which are far stronger",
            "Plants only make antibodies after being infected twice",
            "Plants have no lymphocytes, so they use barriers and chemicals",
        ],
        "correct_index": 3,
        "why": "Antibodies are made by lymphocytes, which plants do not have; "
               "their defences are structural and chemical instead.",
    },
    {
        "id": "ks4-plant-disease-detection-defence-h03",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A plant with stunted growth and yellow leaves is growing in "
                "soil that is low in nitrate. Suggest how a grower could "
                "decide whether disease or the soil is responsible.",
        "options": [
            "Add nitrate to one plant and see whether the symptoms improve",
            "Spray the plant with fungicide and remove all of its leaves",
            "Move the plant somewhere warmer and wetter and watch it",
            "Send a leaf away, since only disease can cause yellowing",
        ],
        "correct_index": 0,
        "why": "Changing one factor and watching the response separates a "
               "mineral deficiency from an infection, which fertiliser would "
               "not cure.",
    },
    {
        "id": "ks4-plant-disease-detection-defence-h04",
        "subtopic_slug": "plant-disease-detection-defence",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Many modern medicines were first found in plants. Suggest "
                "why plant defence chemicals are a good place to look for new "
                "drugs.",
        "options": [
            "Plants only make chemicals that are harmless to human beings",
            "They are already active against living cells such as microbes",
            "Plant chemicals need no testing before they can be prescribed",
            "Plants make chemicals in larger amounts than any laboratory",
        ],
        "correct_index": 1,
        "why": "A chemical evolved to kill or deter another organism already "
               "has biological activity, which is where a drug starts.",
    },

    # ── monoclonal-antibodies (TRIPLE, HIGHER) ───────────────────────────
    {
        "id": "ks4-monoclonal-antibodies-e01",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "What does the word monoclonal tell you about these "
                "antibodies?",
        "options": [
            "They are made by many different lymphocytes together",
            "They are able to bind to many different antigens at once",
            "They are identical, produced from a single clone of cells",
            "They are made only in the body and never in a laboratory",
        ],
        "correct_index": 2,
        "why": "One clone of cells makes one antibody, so every molecule has "
               "the same binding site and the same target.",
    },
    {
        "id": "ks4-monoclonal-antibodies-e02",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Into which animal is the chosen antigen usually injected at "
                "the start of monoclonal antibody production?",
        "options": [
            "A rabbit",
            "A sheep",
            "A human volunteer",
            "A mouse",
        ],
        "correct_index": 3,
        "why": "A mouse is injected so that its lymphocytes make antibodies "
               "against the chosen antigen before they are collected.",
    },
    {
        "id": "ks4-monoclonal-antibodies-e03",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State one side effect that treatment with monoclonal "
                "antibodies can cause.",
        "options": [
            "Permanent loss of all the body's memory cells",
            "Fever, rashes or pain in the joints",
            "Immediate resistance to all antibiotics",
            "Loss of hair from the whole of the body",
        ],
        "correct_index": 1,
        "why": "Side effects such as fever, rashes and joint pain were more "
               "common than first expected when these treatments were "
               "introduced.",
    },
    {
        "id": "ks4-monoclonal-antibodies-e04",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "What word describes the ordinary antibodies a person makes "
                "during an infection?",
        "options": [
            "Polyclonal — a mixture from many different lymphocytes",
            "Monoclonal — identical copies made by a single lymphocyte",
            "Hybridoma — a fusion of two different types of cell",
            "Antigenic — able to trigger a response in another person",
        ],
        "correct_index": 0,
        "why": "A natural response uses many lymphocytes at once, so the "
               "antibodies made are a mixture rather than identical copies.",
    },
    {
        "id": "ks4-monoclonal-antibodies-s01",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a lymphocyte on its own cannot be used to make "
                "large amounts of an antibody in the laboratory.",
        "options": [
            "Lymphocytes make antibodies against the wrong antigen",
            "Lymphocytes are destroyed by the antigen they respond to",
            "Lymphocytes make their antibodies far too slowly to be useful",
            "Lymphocytes do not keep dividing in culture, so few are made",
        ],
        "correct_index": 3,
        "why": "The fusion with a tumour cell exists precisely to supply the "
               "unlimited division that a lymphocyte lacks.",
    },
    {
        "id": "ks4-monoclonal-antibodies-s02",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a monoclonal antibody made against one virus "
                "will not detect a different virus.",
        "options": [
            "The antibody is used up when it binds and cannot bind again",
            "Its binding site fits only the antigen it was made against",
            "The second virus carries no antigens on its surface at all",
            "Antibodies can bind to bacteria only, never to two viruses",
        ],
        "correct_index": 1,
        "why": "The binding site is complementary to one antigen shape, which "
               "is the property that makes these antibodies useful.",
    },
    {
        "id": "ks4-monoclonal-antibodies-s03",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Describe how a monoclonal antibody can be used to deliver a "
                "drug to a tumour.",
        "options": [
            "The drug is attached to the antibody, which binds the tumour",
            "The antibody dissolves the tumour so the drug can enter it",
            "The antibody carries the drug to the liver, which sends it on",
            "The antibody makes tumour cells absorb any drug in the blood",
        ],
        "correct_index": 0,
        "why": "Attaching the drug to an antibody that binds only the tumour "
               "concentrates the dose where it is needed.",
    },
    {
        "id": "ks4-monoclonal-antibodies-s04",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Suggest why monoclonal antibodies are useful in research for "
                "locating one particular protein in a tissue sample.",
        "options": [
            "They dissolve every protein except the one being looked for",
            "They make the tissue transparent so the proteins show up",
            "They bind only to that protein and can be labelled to show it",
            "They cause the protein to move to the surface of the sample",
        ],
        "correct_index": 2,
        "why": "Specific binding plus a visible label marks the position of "
               "one molecule among thousands of others.",
    },
    {
        "id": "ks4-monoclonal-antibodies-h01",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why some patients have an allergic reaction to "
                "treatment with monoclonal antibodies.",
        "options": [
            "The antibodies destroy the patient's own lymphocytes on contact",
            "The antibodies are foreign proteins, so the immune system reacts",
            "The antibodies carry a small dose of the tumour cells used",
            "The antibodies bind healthy cells as strongly as cancer cells",
        ],
        "correct_index": 1,
        "why": "Antibodies produced from mouse cells are recognised as "
               "foreign antigens, and the patient mounts a response against "
               "them.",
    },
    {
        "id": "ks4-monoclonal-antibodies-h02",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Monoclonal antibodies were expected to replace many cancer "
                "treatments but are used less widely than predicted. Suggest "
                "why.",
        "options": [
            "They cause more side effects than expected and cost a great deal",
            "They cannot be made in large enough amounts to treat one patient",
            "They bind to every cell in the body, so are as harmful as "
            "chemotherapy",
            "They only work on cancers that have already been fully cured",
        ],
        "correct_index": 0,
        "why": "The specificity is real, but the side effects and the cost of "
               "production have limited how widely they are used.",
    },
    {
        "id": "ks4-monoclonal-antibodies-h03",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A pregnancy test is positive on the day it is used but was "
                "negative when the same woman tested a week earlier. Explain "
                "the difference.",
        "options": [
            "The antibodies on the strip lose their shape as a test ages",
            "The hormone is only produced on certain days of the month",
            "Too little hormone was present a week earlier to give a result",
            "Antibodies take a week to be made by the woman's lymphocytes",
        ],
        "correct_index": 2,
        "why": "The test only shows a line once enough hormone is present in "
               "the urine to bind a detectable number of antibodies.",
    },
    {
        "id": "ks4-monoclonal-antibodies-h04",
        "subtopic_slug": "monoclonal-antibodies",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A lateral flow test uses monoclonal antibodies to detect a "
                "viral antigen. Explain why someone who has recovered from "
                "the virus may test negative while still feeling unwell.",
        "options": [
            "The antibodies on the test bind only to living virus particles",
            "The test detects the person's own antibodies, which fade fast",
            "The test has become resistant to the virus after repeated use",
            "The antigen is no longer present, though symptoms can persist",
        ],
        "correct_index": 3,
        "why": "The test reports whether the antigen is there now, and "
               "symptoms can outlast the infection that caused them.",
    },
]
