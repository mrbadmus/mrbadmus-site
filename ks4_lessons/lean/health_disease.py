# -*- coding: utf-8 -*-
"""Health, disease and risk factors, in the lean shape. Spec table: ks4-health-disease.md (AQA 8464
4.2.2.5 and 4.2.2.6 / 8461 the same, word for word; no HT-only or Biology-only lines). One page
serves both points.

LEGACY (batch 6). The ladder and the practice set stay from the Design page. The practice set is
the page's own hard-coded `bankSrc` (same five items on every route), so its fixes are
logic_edits. No practice-set stem is edited, so every ks4q: id survives (the "LIFESTYLE" stem
keeps its capitals for that reason); rung prompts keep their positions, so rung ids survive.

The scatter graph was drawn point by point on the Design page's bench, which the lean page does
not have, so Rung 2 Q1 ("Use the scatter graph") pointed at empty axes. scatterFig now draws all
five points and the line of best fit. A new worked item (MS 2c) turns a frequency table into a
bar chart: fig:lung-cancer-bar-chart.
"""


def _js(s):
    """This batch's logic is plain ASCII with \\uXXXX escapes: spell a target the way the file does."""
    # Every non-ASCII character as backslash-u + 4 lower-case hex, the way these logic files spell
    # them (backslashreplace gave \\xNN for U+0080-U+00FF: µ ° ÷ × would never match).
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in s)


_EDITS = [
    # scatterFig drawn complete (the plotting bench is not on the lean page).
    ("scatterFig: ready ? K.fig(this.scatter(s.plotted), '') : null,",
     "scatterFig: ready ? K.fig(this.scatter(DATA.length), '') : null,"),
    # Rung 1 Q1: credited option the longest by 10.
    ("{ text: 'Being able to run fast', correct: false, reply: 'Fitness is only part of physical well-being.' }",
     "{ text: 'Being fit enough to run a long way', correct: false, reply: 'Fitness is only part of physical well-being.' }"),
    # Rung 2 Q2: credited option the longest by 12.
    ("{ text: 'They are more likely to suffer from infectious diseases', correct: true }",
     "{ text: 'They are more likely to get infectious diseases', correct: true }"),
    # Rung 3 Q2 link 3: said closer to the spec ("A causal mechanism has been proven for some risk
    # factors, but not in others").
    ("'A cause is only shown when scientists find how the factor leads to the disease.'",
     "'The factor is only proven to cause the disease when a causal mechanism is found.'"),
    # Practice Q1 (communicable), stem kept: credited option the longest (+20), a dash in an
    # option, capitals style in a reply.
    ("opts: [['Communicable diseases are caused by pathogens and can spread between organisms. Non-communicable diseases cannot spread.', true], ['Communicable diseases are always fatal. Non-communicable diseases are always mild.', false], ['Communicable diseases are caused by lifestyle. Non-communicable diseases are caused by pathogens.', false], ['They are the same thing — both terms describe infectious disease.', false]],",
     "opts: [['Communicable diseases are caused by pathogens and can spread. Non-communicable diseases cannot.', true], ['Communicable diseases are always fatal. Non-communicable diseases are always mild.', false], ['Communicable diseases are caused by lifestyle. Non-communicable diseases are caused by pathogens.', false], ['They are the same thing: both mean an infectious disease.', false]],"),
    ("wrong_explanations: { 1: 'Neither type is always fatal or always mild — severity varies enormously in both categories.', 2: 'This is exactly the wrong way round. Communicable = pathogens. Non-communicable = lifestyle, genetics, environment.', 3: 'They are not the same — the key difference is whether the disease can be spread from person to person.' }",
     "wrong_explanations: { 1: 'Both types can be mild or serious.', 2: 'This is the wrong way round. Communicable diseases are caused by pathogens.', 3: 'They are different. Only communicable diseases can spread from person to person.' }"),
    # Practice Q2 (red meat), stem kept: credited option visibly the longest (+37), dash,
    # capitals; muddled replies ("doesn't fit the timeline", "an important first step").
    ("opts: [['A correlation between red meat consumption and bowel cancer — further research is needed to establish causation', true], ['Red meat DEFINITELY causes bowel cancer in everyone who eats it', false], ['Bowel cancer causes people to eat more red meat', false], ['This is meaningless data — correlations in diet studies are never reliable', false]],",
     "opts: [['A correlation between eating red meat and bowel cancer', true], ['Red meat definitely causes bowel cancer in everyone who eats it', false], ['Bowel cancer causes people to eat more red meat', false], ['The data is meaningless, because diet studies are never useful', false]],"),
    ("wrong_explanations: { 1: 'Correlation does not automatically mean causation — the relationship could be due to other factors (e.g. diet quality overall, exercise levels).', 2: 'This would be reverse causation — the data shows a link, but the disease developing before changing diet doesn’t fit the timeline.', 3: 'Epidemiological (population-based) data is valuable scientific evidence — correlation studies are an important first step in identifying risk factors.' }",
     "wrong_explanations: { 1: 'A correlation shows a link. It does not prove a cause, or that everyone who eats red meat gets ill.', 2: 'Nothing in the study shows the cancer coming first and changing what people eat.', 3: 'Studies like this are useful evidence of a link. Scientists then look for a cause.' }"),
    # Practice Q3 (lifestyle risk factor), stem kept: replies used capitals, "non-modifiable" (not
    # in the spec) and weakened the motorway distractor.
    ("wrong_explanations: { 1: 'Age is a NON-LIFESTYLE (non-modifiable) risk factor — everyone ages and it cannot be changed.', 2: 'Family history = GENETIC risk factor — also non-modifiable. You cannot choose your genes.', 3: 'Living near a motorway = ENVIRONMENTAL risk factor — though this can sometimes be changed (by moving), it is generally classified as environmental rather than lifestyle.' }",
     "wrong_explanations: { 1: 'Age is a risk factor, but it is not part of a lifestyle.', 2: 'Family history is a risk factor, but it is not part of a lifestyle.', 3: 'Air pollution is a substance in the environment, not part of a lifestyle.' }"),
    # Practice Q5 (sample size), stem kept: credited option visibly the longest (+27).
    ("opts: [['The larger random sample is more representative of the population', true], ['Larger studies always prove a cause', false], ['Small studies can’t be put on a graph', false], ['Randomly chosen people are healthier', false]],",
     "opts: [['A large random sample better represents the population', true], ['Larger studies always prove that one factor causes the disease', false], ['Small studies cannot be shown on a graph or a chart', false], ['Randomly chosen people are healthier than other people', false]],"),
]

# Examiner pass (EXAMINER.md) and blind pass, 18 Nov 2026. Each old string is the logic AFTER the
# edits above, and occurs exactly once (validate.py checks).
_EDITS += [
    ("{ text: 'Not having a communicable disease', correct: false, reply: 'Health is more than not having an infection.' }, { text: 'Being fit enough to run a long way', correct: false,",
     "{ text: 'Not having any communicable disease at all', correct: false, reply: 'Health is more than not having an infection.' }, { text: 'Being fit enough to run a long way easily', correct: false,"),
    ("links: ['A correlation shows the two change together.', 'Another factor could be causing both, or it could be chance in a small sample.', 'The factor is only proven to cause the disease when a causal mechanism is found.'],",
     "links: ['A correlation only shows that the factor and the disease change together.', 'So another factor could be causing both, or the link could be chance in a small sample.', 'To rule these out, a causal mechanism must be found that links the factor to the disease.'],"),
]

LESSON = {
    "slug": "health-disease",
    "start": {
        "setup": "A person with a weak immune system catches infections more often.",
        "question": "If you had to guess, can one kind of illness make another more likely?",
        "options": [
            ("Yes",
             "Yes. Different types of disease may interact. A defect in the immune system makes "
             "a person more likely to suffer from infectious diseases."),
            ("No",
             "Yes. Different types of disease may interact. A defect in the immune system makes "
             "a person more likely to suffer from infectious diseases."),
        ],
        "answer": 0,
    },
    "words": ["health", "non-communicable", "risk factor", "correlation"],
    "knowledge": [
        {"kind": "card", "title": "Health and disease",
         "body": ["Health is the state of physical and mental well-being.",
                  "Diseases, both communicable and non-communicable, are major causes of ill "
                  "health.",
                  {"points": [
                      "Communicable diseases are caused by pathogens and can spread from one "
                      "person to another.",
                      "Non-communicable diseases cannot be passed from one person to another.",
                  ]},
                  "Diet, stress and life situations may have a profound effect on both physical "
                  "and mental health."]},
        {"kind": "card", "title": "Diseases can interact",
         "body": [{"points": [
             "Defects in the immune system mean a person is more likely to suffer from "
             "infectious diseases.",
             "Viruses living in cells can be the trigger for cancers.",
             "Immune reactions first caused by a pathogen can trigger allergies, such as skin "
             "rashes and asthma.",
             "Severe physical ill health can lead to depression and other mental illness.",
         ]}]},
        {"kind": "card", "title": "Risk factors",
         "body": ["Risk factors are linked to an increased rate of a disease. They can be:",
                  {"points": [
                      "aspects of a person's lifestyle, such as smoking",
                      "substances in the person's body or environment, such as ionising "
                      "radiation",
                  ]},
                  "A causal mechanism has been proven for some risk factors, but not in others.",
                  "Many diseases are caused by the interaction of a number of factors."]},
        {"kind": "reveal", "title": "Risk factors and their effects",
         "cols": ["Linked to"],
         "rows": [
             ("Diet, smoking and lack of exercise", "Cardiovascular disease"),
             ("Obesity", "Type 2 diabetes"),
             ("Alcohol", "Damage to the liver and to brain function"),
             ("Smoking", "Lung disease and lung cancer"),
             ("Smoking and alcohol in pregnancy", "Harm to the unborn baby, such as a lower "
                                                  "birth weight"),
             ("Carcinogens, including ionising radiation", "Cancer"),
         ]},
        {"kind": "card", "title": "The cost of non-communicable diseases",
         "body": [{"points": [
             "To the person: illness, a lower quality of life, lost earnings, an early death.",
             "To the community and the nation: the cost of treatment and care, and fewer people "
             "able to work.",
             "Globally: these diseases are very common, so the total cost is very large.",
         ]},
             "Lifestyle factors, including diet, alcohol and smoking, change how common these "
             "diseases are locally, nationally and globally. Where more people smoke, more people "
             "get lung cancer."]},
        {"kind": "card", "title": "Reading a scatter graph",
         "body": ["Made-up data: cigarettes smoked a day against lung cancer cases per 100 000 "
                  "people.",
                  {"slot": "legacy-fig:scatterFig"},
                  "The points rise from left to right: a positive correlation. A correlation shows "
                  "a link. It does not prove that one causes the other.",
                  "A large, randomly chosen sample gives more valid conclusions, because it "
                  "represents the whole population better."]},
        {"kind": "card", "title": "From a table to a bar chart",
         "body": ["Made-up data: lung cancer cases per 100 000 people in one year.",
                  {"points": [
                      "Never smoked: 15",
                      "Smoked in the past: 60",
                      "Smoke now: 150",
                  ]},
                  {"slot": "fig:lung-cancer-bar-chart"},
                  "Each group gets its own bar, with gaps between the bars. The height of each "
                  "bar is the number of cases.",
                  "Reading back: people who smoke now have 150 ÷ 15 = 10 times as many cases as "
                  "people who never smoked."]},
        # Supervising ruling, 18 Nov 2026: spec 4.2.2.5 and MS 2c both name histograms, and this
        # lesson's disease-incidence data is where they are used, so one drawn example is taught.
        {"kind": "card", "title": "Reading a histogram",
         "body": ["Made-up data: the ages at which 200 people were diagnosed with coronary heart "
                  "disease.",
                  {"slot": "fig:chd-age-histogram"},
                  "Age is continuous data, so it is grouped into equal class intervals, such as 60 "
                  "to 70 years. The bars touch, because each interval runs straight into the next. "
                  "A bar chart of separate groups has gaps instead.",
                  "The height of each bar is the number of people in that interval. Most people "
                  "were diagnosed aged 70 to 80: 70 of the 200."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A risk factor means you will get the disease.",
              "A risk factor is linked to an increased rate of the disease. Not everyone with it "
              "gets ill."),
             ("A correlation proves a cause.",
              "A correlation shows a link. A cause is proven only when the causal mechanism is "
              "found."),
             ("Health just means not having a disease.",
              "Health is the state of physical and mental well-being."),
         ]}]},
    ],
    "key_fact": "Health is the state of physical and mental well-being, and diseases, both "
                "communicable and non-communicable, are major causes of ill health. Risk factors, "
                "such as smoking, diet and alcohol, are linked to an increased rate of a disease; a "
                "causal mechanism has been proven for some risk factors, but not in others.",
    "deeper": [
        {"kind": "card", "title": "A proven cause",
         "body": ["Smoking and lung cancer is a link where the causal mechanism has been found. "
                  "Tobacco smoke contains carcinogens, which damage the DNA in lung cells."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong> a graph: say how one variable changes as the other "
             "increases, and quote numbers.",
             "<strong>Suggest</strong> why: use the information to give a likely reason.",
             "<strong>Discuss</strong> the costs: human and financial costs, for the person, "
             "the community and the nation.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-6", "logic_edits": [(_js(a), _js(b)) for a, b in _EDITS]},
}
