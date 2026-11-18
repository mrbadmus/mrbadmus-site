# -*- coding: utf-8 -*-
"""Coronary heart disease, in the lean shape. Spec table: ks4-coronary-heart-disease.md (AQA 8464
4.2.2.4 / 8461 4.2.2.4, word for word the same; no HT-only or Biology-only lines). Risk factors
are 4.2.2.6 (Health, disease and risk factors): one line here. Pacemakers are on The heart and
blood vessels.

LEGACY (batch 4). The ladder and the practice set stay from the Design page. The practice set is
the page's own hard-coded `bankSrc` (same five items on every route), so its fixes are
logic_edits. No practice-set stem is edited, so every ks4q: id survives (the "CAN be changed"
stem keeps its capitals for that reason); rung prompts keep their positions, so rung ids survive.
"""


def _js(s):
    """This batch's logic is plain ASCII with \\uXXXX escapes: spell a target the way the file does."""
    # Every non-ASCII character as backslash-u + 4 lower-case hex, the way these logic files spell
    # them (backslashreplace gave \\xNN for U+0080-U+00FF: µ ° ÷ × would never match).
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in s)


_EDITS = [
    # Rung 2 Q1: credited option visibly the longest (+22); "blood clots more easily" was not
    # definitely wrong for a narrowed valve. Replaced.
    ("{ text: 'They feel tired and breathless, because less oxygenated blood reaches the body', correct: true },",
     "{ text: 'Less oxygenated blood reaches the body, so they feel tired', correct: true },"),
    ("{ text: 'Their blood clots more easily', correct: false, reply: 'The main effect is less blood pumped round the body.' }",
     "{ text: 'Their heart pumps more blood than before', correct: false, reply: 'Less blood gets through a valve that does not open fully.' }"),
    # Rung 2 Q2: the credited option was the longest by 11 characters.
    ("{ text: 'Statins', correct: false, reply: 'Statins slow fatty build-up; they can’t support a failing heart.' }",
     "{ text: 'A course of statins', correct: false, reply: 'Statins slow fatty build-up; they can’t support a failing heart.' }"),
    ("{ text: 'A stent', correct: false, reply: 'A stent opens one artery; the whole heart is failing here.' }",
     "{ text: 'A stent in one artery', correct: false, reply: 'A stent opens one artery; the whole heart is failing here.' }"),
    # Rung 4 point: the judgement read as the one right answer to an "evaluate".
    ("'Judgement: statins for early disease, a stent for a narrowed artery, a transplant only for heart failure.'",
     "'A judgement, such as: statins to slow early disease, a stent for a narrowed artery, a transplant only for heart failure.'"),
    # Practice Q1 (cause), stem kept: credited option visibly the longest (+51); "plaques" and
    # "atherosclerosis" are not the spec's words; one reply contradicted "risk rises with age".
    ("['Fatty plaques (atherosclerosis) build up in the coronary arteries, narrowing them and reducing blood flow to the heart muscle', true]",
     "['Layers of fatty material build up inside the coronary arteries', true]"),
    ("wrong_explanations: { 1: 'Heart muscle weakness (heart failure) is a consequence of CHD, not the cause — the cause is specifically fatty plaque build-up.', 2: 'Blood viscosity can affect flow, but CHD is specifically about PLAQUE build-up in artery walls, not blood thickness.', 3: 'Arteries don’t naturally narrow with age — they narrow because of PLAQUES (fatty deposits) accumulating over time due to risk factors.' }",
     "wrong_explanations: { 1: 'A weak heart can be a result of coronary heart disease, not its cause.', 2: 'The problem is fatty material building up inside the artery, not thick blood.', 3: 'The arteries narrow because fatty material builds up inside them.' }"),
    # Practice Q2 (stent), stem kept: credited option the longest (+20), dash; one option and
    # its reply taught bypass surgery (not in the spec).
    ("opts: [['It is inserted into the narrowed artery and expands to hold it open — restoring blood flow', true], ['It dissolves the fatty plaques blocking the artery', false], ['It reroutes blood around the blocked artery using a grafted vessel', false], ['It lowers blood cholesterol levels to prevent further plaque formation', false]],",
     "opts: [['It is put into the narrowed artery and holds it open', true], ['It dissolves the fatty material blocking the artery', false], ['It replaces the coronary artery with a new one', false], ['It lowers the cholesterol level in the blood', false]],"),
    ("wrong_explanations: { 1: 'Stents do not dissolve plaques — they physically hold the narrowed artery open.', 2: 'Rerouting blood around a blockage using a grafted vessel = BYPASS SURGERY, not a stent.', 3: 'Lowering cholesterol = STATINS (medication), not a stent.' }",
     "wrong_explanations: { 1: 'A stent does not remove the fatty material. It holds the artery open.', 2: 'A stent sits inside the existing artery and holds it open.', 3: 'Statins lower blood cholesterol.' }"),
    # Practice Q3 (risk factor that can be changed), stem kept: replies used capitals, dashes
    # and "non-modifiable" (not in the spec).
    ("wrong_explanations: { 1: 'Genetics is a risk factor — but you cannot change your DNA. It is a non-modifiable risk factor.', 2: 'Sex (being male) slightly increases CHD risk, particularly at younger ages — but you cannot change this.', 3: 'Age increases CHD risk, but everyone ages — you cannot avoid this risk factor.' }",
     "wrong_explanations: { 1: 'Family history is a risk factor, but you cannot change it.', 2: 'Being male is a risk factor, but you cannot change it.', 3: 'Age is a risk factor, but you cannot stop getting older.' }"),
    # Practice Q4 (leaking valve), stem kept: credited option visibly the longest (+26).
    ("['Blood flows backwards through the valve, so less oxygenated blood reaches the body', true]",
     "['Some blood flows backwards, so less reaches the body', true]"),
    # Practice Q5 (artificial hearts), stem kept: credited option visibly the longest (+39).
    ("['To keep a patient alive while waiting for a transplant, or to let the heart rest as an aid to recovery', true]",
     "['While waiting for a transplant, or to let the heart rest', true]"),
]

LESSON = {
    "slug": "coronary-heart-disease",
    "start": {
        "question": "If you had to guess, where does the heart muscle get its oxygen from?",
        "options": [
            ("The blood inside its chambers",
             "From the coronary arteries. They branch over the outside of the heart and supply the "
             "heart muscle with oxygenated blood."),
            ("Arteries on the outside of the heart",
             "From the coronary arteries. They branch over the outside of the heart and supply the "
             "heart muscle with oxygenated blood."),
        ],
        "answer": 1,
    },
    "words": ["coronary heart disease", "stent", "statin", "heart failure"],
    "knowledge": [
        {"kind": "card", "title": "What coronary heart disease is",
         "body": [{"slot": "legacy-fig:heartFig"},
                  "In coronary heart disease, layers of fatty material build up inside the "
                  "coronary arteries, narrowing them.",
                  "This reduces the flow of blood through the coronary arteries, resulting in a "
                  "lack of oxygen for the heart muscle. The heart muscle can be damaged.",
                  "Smoking, a poor diet and too little exercise increase the risk. Health, "
                  "disease and risk factors has the details."]},
        {"kind": "card", "title": "Stents",
         "body": ["Stents are used to keep the coronary arteries open.",
                  {"slot": "legacy-fig:stentFig"},
                  "A stent is a small mesh tube put inside the narrowed artery. It holds the "
                  "artery open, so blood can flow to the heart muscle again."]},
        {"kind": "card", "title": "Statins",
         "body": ["Statins are widely used to reduce blood cholesterol levels, which slows down "
                  "the rate of fatty material deposit.",
                  "Statins do not remove fatty material that is already there."]},
        {"kind": "card", "title": "Faulty heart valves",
         "body": ["Heart valves can become faulty in two ways.",
                  {"slot": "legacy-fig:valveFig"},
                  {"points": [
                      "The valve may not open fully, so less blood gets through.",
                      "The valve may leak, so some blood flows backwards.",
                  ]},
                  "Either way, less oxygenated blood is pumped round the body, so the person "
                  "feels tired and breathless.",
                  "Faulty heart valves can be replaced using biological or mechanical valves."]},
        {"kind": "card", "title": "Heart failure",
         "body": ["In heart failure, a donor heart, or a heart and lungs, can be transplanted.",
                  "Artificial hearts are occasionally used to keep patients alive while they "
                  "wait for a heart transplant, or to allow the heart to rest as an aid to "
                  "recovery."]},
        {"kind": "reveal", "title": "Weighing up the treatments",
         "cols": ["Advantages", "Dis\u00adadvantages"],
         "rows": [
             ("Statins", "No surgery; slow the build-up of fatty material",
              "Must be taken for a long time; can have side effects; act slowly"),
             ("Stent", "Restores blood flow quickly; a short recovery",
              "Surgery has risks; the artery can narrow again"),
             ("Transplant", "Replaces a heart that has failed",
              "Too few donors; the new heart may be rejected; drugs to stop rejection for life"),
             ("Artificial heart", "Keeps a patient alive while waiting, or lets the heart rest",
              "Only used for a short time; risk of blood clots and infection"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A stent removes the fatty material.",
              "A stent holds the artery open. The fatty material is still there."),
             ("Statins clear blocked arteries.",
              "Statins lower blood cholesterol, which slows down the build-up of fatty material."),
             ("The fatty material builds up inside the heart's chambers.",
              "It builds up inside the coronary arteries."),
         ]}]},
    ],
    "key_fact": "In coronary heart disease, layers of fatty material build up inside the coronary "
                "arteries, narrowing them and reducing the flow of blood, so the heart muscle gets "
                "less oxygen. Stents keep the arteries open, statins reduce blood cholesterol to "
                "slow the build-up, faulty valves can be replaced, and heart failure can be treated "
                "with a transplant.",
    "deeper": [
        {"kind": "card", "title": "Writing an evaluation",
         "body": [{"points": [
             "Give at least one advantage and one disadvantage of each treatment.",
             "Use the information about the patient, such as how far the disease has gone.",
             "Finish with a judgement and a reason for it.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong> how CHD harms the heart: fatty material, narrower "
             "arteries, less blood flow, less oxygen for the heart muscle.",
             "<strong>Suggest</strong> a treatment: match it to the problem in the question.",
             "<strong>Evaluate</strong>: advantages, disadvantages, then a judgement.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-4", "logic_edits": [(_js(a), _js(b)) for a, b in _EDITS]},
}
