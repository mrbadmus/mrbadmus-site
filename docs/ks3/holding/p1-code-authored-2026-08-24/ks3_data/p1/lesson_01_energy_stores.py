"""P1 L1 — Energy stores (CLASSIFY).

The first physics lesson in the key stage, and it exists to give the student
the nouns. Everything P1 does afterwards is a sentence built out of them.

── ⚖️ THE SCIENCE RULING THIS LESSON IS BUILT ON ────────────────────────

**Stores and pathways, not "types of energy".** `KS3.P.CIS.02` names the
stores by their physical situations — "movements, temperatures, changes in
positions in a field, elastic distortions and chemical compositions" — and
names no others. It does not say sound energy, light energy or electrical
energy, and that is not an oversight: sound, light and an electric current are
things that HAPPEN BETWEEN two moments, not amounts a thing holds. A student
who learns nine "types" that "change into" each other has learned a list that
GCSE will take back off them in Year 10.

So the lesson teaches five stores and one discrimination, and `#s-sort` is the
discrimination. The word `pathway` is used because it is the word the student
will meet again; the idea is carried by the phrase "a way of transferring",
which is what the bin is labelled.

⚠️ **Every store is a property of a SITUATION, not of an object**, and the
store cards say so one at a time rather than announcing it. It is the seed of
`ENER-10`, which p1-02 confronts: a gravitational store belongs to the object,
the Earth and the gap between them, and a student who thinks it lives inside
the object alone cannot say why raising it fills anything.

── The five, and why five ──────────────────────────────────────────────

Kinetic, thermal, gravitational, elastic, chemical. One per phrase in the
bullet, in the bullet's own order except that gravitational is put third
because it is the one the hook uses.

Magnetic and electrostatic are the SAME clause — "changes in positions in a
field" — and they are in `stretch`, not in the five. Putting them in the five
would give a Year 7 seven cards to hold on the day they meet the idea, and
neither has a statement of its own to answer for here: the magnet case belongs
to P10 and the charge case to P9.

── No figures ──────────────────────────────────────────────────────────

Every figure in this lesson would be a picture of a situation the words
already carry. `figure=None` throughout, in the record and in the bank.
"""

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py character for character.
    "slug":        "energy-stores",
    "title":       "Energy stores",
    "discipline":  "physics",
    "unit":        "energy-transfers",
    "family":      "CLASSIFY",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.P.CIS.02` is clause-split; clause `a` is the stores themselves and
    # clause `b` (comparing a system before and after) is p1-02's. The mint and
    # the reasoning are in `ks3_data/substatements.py`.
    "covers":      ["KS3.P.CIS.02a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 60,

    # ── progression edges ───────────────────────────────────────────────────
    "requires":    [],
    "assumes":     [],
    "references":  [],
    "ks4_links":   [],
    "connects_heading": "Next in this unit",

    # ── framing ─────────────────────────────────────────────────────────────
    # ⊕ Authored so the page keeps its own 160-character summary
    # rather than a truncated `big_question` (MRB-257 audit 6.12).
    "meta_description": "Five energy stores — kinetic, thermal, gravitational, "
                        "elastic and chemical — and why sound, light and electric "
                        "current are none of them.",

    "big_question": "A wind-up torch has no battery in it and it lights up "
                    "anyway. Something in that torch was filled up when you "
                    "turned the handle. The question is what.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The torch with no battery", "done_when": "committed"},
        {"anchor": "s-stores", "short": "STORES",
         "label": "The five stores", "done_when": "all_stores_opened"},
        {"anchor": "s-sort",   "short": "SORT",
         "label": "Store or way of transferring", "done_when": "all_sorted"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Is sound a store?", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "title": "Turn the handle for thirty seconds and it shines for two "
                 "minutes.",
        "prompt": "A wind-up torch has no battery and nothing goes into it "
                  "except the turning of your hand. Stop turning and it keeps "
                  "shining for a while, then fades. Turn it again and it "
                  "starts over.",
        "commit": "While you were turning the handle, what was being filled?",
        "options": [
            "Nothing — the turning made the light directly",
            "A spring inside, wound tighter and tighter",
            "The bulb, which holds light until it is needed",
            "The air inside the case, squashed by the handle",
        ],
        "reveal": "A spring. Turning the handle winds it, and a wound spring "
                  "is a filled store — the same kind of store as a stretched "
                  "elastic band. The torch then lets it unwind slowly, and "
                  "that is what runs the bulb. Nothing was made and nothing "
                  "was destroyed; something was filled and then emptied.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    "misconceptions": [
        {"id": "ENER-09",
         "statement": "Sound, light and electricity are kinds of energy that "
                      "things store.",
         "elicited_by": "think-commit-sound",
         "confronted_by": "think-commit-sound"},
    ],

    # ── core, in document order ─────────────────────────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Energy is not a substance. You cannot bottle it, and there "
                 "is no jar of it anywhere. It is an <em>amount</em>, "
                 "measured in joules, that goes with a situation — how fast "
                 "something is going, how hot it is, how high it is, how far "
                 "it is stretched, what it is made of. Change the situation "
                 "and the amount changes with it. A store is one of those "
                 "situations, and there are five worth knowing."},

        # #s-stores — the reference bench. Five cards, read one at a time.
        {"type": "store-audit", "id": "the-five-stores", "anchor": "s-stores",
         "eyebrow": "The accounts · five stores",
         "heading": "Five situations that hold an amount",
         "head_counter": {"format": "{n} of 5 stores opened", "total": 5},
         "demand": "explain",
         "prompt": "Open each one. For every store, the two lines that matter "
                   "are what fills it and what empties it — those are the two "
                   "you will be asked for.",
         "resting": "Pick a store to open it.",
         "stores": [
             {"id": "kinetic", "name": "Kinetic", "sub": "movement",
              "belongs": "the moving object",
              "fills": "Anything speeds up.",
              "empties": "Anything slows down.",
              "example": "A cyclist freewheeling down a hill is filling a "
                         "kinetic store the whole way down. At the bottom she "
                         "brakes and it empties again.",
              "watch": "Standing still is a kinetic store with nothing in it, "
                       "not a missing store."},
             {"id": "thermal", "name": "Thermal", "sub": "temperature",
              "belongs": "the object that is hot",
              "fills": "Anything gets hotter.",
              "empties": "Anything gets cooler.",
              "example": "A mug of tea cooling on a desk is emptying a "
                         "thermal store. The desk and the room are filling "
                         "theirs by the same amount.",
              "watch": "Cold is not a store. A cold thing has a thermal store "
                       "with less in it than a hot one, and that is the whole "
                       "difference."},
             {"id": "gravitational", "name": "Gravitational",
              "sub": "position in a field",
              "belongs": "the object AND the Earth, together",
              "fills": "Anything is raised.",
              "empties": "Anything falls.",
              "example": "Lifting a book onto a shelf fills a gravitational "
                         "store. It stays filled while the book sits there, "
                         "and empties the moment the book falls off.",
              "watch": "This one does not live inside the book. It is about "
                       "the book, the Earth, and the gap between them — take "
                       "the Earth away and there is no store at all."},
             {"id": "elastic", "name": "Elastic", "sub": "distortion",
              "belongs": "the stretched or squashed object",
              "fills": "Anything is stretched, squashed or bent.",
              "empties": "It springs back.",
              "example": "The wind-up torch in the hook. Turning the handle "
                         "winds a spring tighter, and letting it unwind runs "
                         "the bulb.",
              "watch": "The object has to spring back. Squashing a lump of "
                       "clay fills no elastic store, because clay stays "
                       "squashed."},
             {"id": "chemical", "name": "Chemical", "sub": "composition",
              "belongs": "the substances, as they are arranged now",
              "fills": "Substances are made whose atoms are arranged in a way "
                       "that holds more.",
              "empties": "They react into substances that hold less.",
              "example": "Petrol, food and a battery are all chemical stores. "
                         "Burning, digesting and using are all ways of "
                         "emptying one.",
              "watch": "It is about which substances exist, not about how "
                       "much there is of them. A full tank and a half tank "
                       "are the same substance with different amounts in it."},
         ],
         "close": [
             "Five stores, ten lines. Every situation you meet for the rest "
             "of this unit fills at least one of them and empties at least "
             "one other.",
             "Notice that not one of the five is called sound, light or "
             "electricity. That is deliberate, and it is what the next block "
             "is about.",
         ]},

        # #s-sort — the CLASSIFY discrimination, with MRB-196 R10's self-check.
        {"type": "store-or-pathway", "id": "store-or-way", "anchor": "s-sort",
         "eyebrow": "The discrimination · this is the lesson",
         "heading": "A store, or a way of getting there?",
         "head_counter": {"format": "{n} of 8 sorted", "total": 8},
         "demand": "classify",
         "prompt": "A store is something a situation HOLDS and you could "
                   "come back tomorrow and find still there. A way of "
                   "transferring is something that HAPPENS between two "
                   "moments, and when it stops there is nothing left of it. "
                   "Sort all eight, then read them back.",
         "bins": [
             {"id": "store", "label": "A store",
              "gloss": "still there tomorrow"},
             {"id": "pathway", "label": "A way of transferring",
              "gloss": "only while it is happening"},
         ],
         "items": [
             {"id": "skateboard", "label": "A skateboard rolling downhill",
              "bin": "store",
              "why": "A kinetic store, filling as it speeds up. Stop the "
                     "clock at any moment and there is an amount there."},
             {"id": "sound", "label": "Sound", "bin": "pathway",
              "why": "Sound is air being pushed back and forth by something "
                     "vibrating. Stop the vibration and there is no sound "
                     "left anywhere — nothing was stored, something was "
                     "carried."},
             {"id": "oven", "label": "An oven at 200 degrees", "bin": "store",
              "why": "A thermal store, and a full one. Switch it off and come "
                     "back in ten minutes; it is still hot, so it is still "
                     "there."},
             {"id": "light", "label": "Light", "bin": "pathway",
              "why": "Light is how a lamp reaches the wall. The wall's "
                     "thermal store fills while the lamp is on and stops "
                     "filling the instant it goes off. Nothing anywhere "
                     "holds light."},
             {"id": "battery", "label": "A charged phone battery",
              "bin": "store",
              "why": "A chemical store. Leave the phone in a drawer for a "
                     "week and the charge is still there, because the "
                     "substances inside it are still the ones that hold "
                     "more."},
             {"id": "current", "label": "An electric current", "bin": "pathway",
              "why": "A current is charge moving round a circuit. Open the "
                     "switch and the current is gone at once — what is left "
                     "is the battery's chemical store, which is the thing "
                     "that was holding anything."},
             {"id": "band", "label": "A stretched elastic band", "bin": "store",
              "why": "An elastic store. Hold it stretched all afternoon and "
                     "it is still loaded, which is exactly what a store "
                     "means."},
             {"id": "heating", "label": "Heating a pan on a hob",
              "bin": "pathway",
              "why": "Heating is the hob's thermal store emptying into the "
                     "pan's. It is the route between two stores, and when "
                     "the hob is off there is no heating left over."},
         ],
         # MRB-196 R10 — no mark on any option, and no answer key here.
         "self_check": {
             "question": "Now the eight are read back. How many did you have "
                         "in the right bin?",
             "options": ["All eight", "Six or seven", "Four or five",
                         "Fewer than four"],
             "note": "The four ways of transferring are sound, light, an "
                     "electric current and heating. If those were the ones "
                     "that caught you, that is the exact thing this block is "
                     "for — and it catches most people the first time.",
         },
         "close": [
             "Four stores, four ways of getting from one store to another. "
             "The stores are what hold; the ways are what carry.",
             "The word for the second column is a <strong>pathway</strong>, "
             "and there are only four of them in the whole of physics: "
             "heating, an electric current, a force moving something, and "
             "radiation — which is what light is.",
         ]},

        {"type": "key-fact", "ref": "stores-not-types"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. "
                 "If you cannot say it, you do not know it yet.",
         "terms": ["Energy", "Joule", "Store", "Pathway", "Kinetic store"]},

        {"type": "misconception", "id": "think-commit-sound",
         "anchor": "s-think", "targets": "ENER-09"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "stores-not-types",
         "text": "There are five stores worth knowing: kinetic, thermal, "
                 "gravitational, elastic and chemical. Sound, light and "
                 "electric current are not stores — they are how energy gets "
                 "from one store to another.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── vocabulary (Law 7) ──────────────────────────────────────────────────
    "vocabulary": [
        {"term": "Energy",
         "definition": "An amount, measured in joules, that goes with a "
                       "situation — how fast, how hot, how high, how "
                       "stretched, what it is made of.",
         "note": "Not a substance and not a fuel. Nothing anywhere is a jar "
                 "of it."},
        {"term": "Joule",
         "definition": "The unit energy is measured in, written J.",
         "note": "Lifting an apple from the floor to a table takes about one "
                 "joule. A slice of bread holds about 300,000."},
        {"term": "Store",
         "definition": "A situation that holds an amount of energy, and still "
                       "holds it if you come back later.",
         "note": "Kinetic, thermal, gravitational, elastic, chemical."},
        {"term": "Pathway",
         "definition": "A way energy gets from one store to another. It "
                       "exists only while it is happening.",
         "note": "Heating, an electric current, a force moving something, and "
                 "radiation."},
        {"term": "Kinetic store",
         "definition": "The store that fills when something speeds up and "
                       "empties when it slows down.",
         "note": "Kinetic means to do with movement. A parked car's kinetic "
                 "store is empty, not absent."},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-sound",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-09",
         "prompt": "A speaker is playing loudly in an empty hall. Commit "
                   "before you read on.",
         "options": [
             "The room is filling up with stored sound energy",
             "The speaker holds sound and lets it out slowly",
             "Nothing is storing sound anywhere in the hall",
             "The walls are absorbing sound and storing it as sound",
         ],
         "reveal": [
             "Nothing in the hall stores sound. The cone of the speaker "
             "pushes the air, the air pushes the next bit of air, and that "
             "travelling push is what your ear picks up. Cut the power and "
             "the hall is silent within a fraction of a second, because "
             "there was never anything holding it.",
             "What the walls do absorb is real, and it is worth being exact "
             "about: the pushing warms them very slightly, so the walls' "
             "<strong>thermal</strong> store fills. Sound went in; a "
             "thermal store came out. That is a pathway ending at a store, "
             "which is what every pathway does.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        "recall": {
            "q": "Which of these is a store of energy?",
            "options": [
                "A stretched elastic band",
                "A beam of light crossing a room",
                "An electric current in a wire",
                "A sound travelling through air",
            ],
            "answer": 0,
            "feedback": {
                1: "Light is a way of transferring, not a store. Block the "
                   "beam and there is nothing left of it anywhere.",
                2: "A current is charge on the move. Open the switch and it "
                   "stops at once — the battery is what was holding anything.",
                3: "Sound is air being pushed back and forth. Stop the "
                   "vibration and there is no sound left to find.",
            }},
        "apply": {
            "q": "A ball is thrown straight up. On the way up it slows down "
                 "and gets higher. Which pair of stores is changing?",
            "options": [
                "Chemical filling, elastic emptying",
                "Thermal filling, kinetic emptying",
                "Elastic filling, gravitational emptying",
                "Kinetic emptying, gravitational filling",
            ],
            "answer": 3,
            "feedback": {
                0: "Nothing is stretched and no substance is reacting. Look "
                   "at what is changing: the speed and the height.",
                1: "The ball is not getting noticeably hotter. Slowing down "
                   "empties a kinetic store, and the store that fills is the "
                   "one to do with height.",
                2: "Nothing is being stretched, and the ball is going up, "
                   "not down. A gravitational store fills as something is "
                   "raised.",
            }},
        "explain": {
            "q": "A student says: \"When you switch a lamp on, the electrical "
                 "energy in the wire turns into light energy, and then the "
                 "light energy is stored in the room.\" Rewrite that sentence "
                 "correctly, and say what is wrong with each part.",
            "field_label": "Your rewrite, then what was wrong",
            "placeholder": "The chemical store in the…",
            "success": [
                "Names a store that empties — the chemical store in the "
                "battery, or the power station's fuel.",
                "Says the electric current is a pathway, not a store.",
                "Says light is a pathway too, not something that gets "
                "stored.",
                "Names the store that fills at the end: the thermal store of "
                "the room and everything in it.",
                "Says that nothing in the room holds light, and that the "
                "room simply ends up very slightly warmer.",
            ]},
        "produce": {
            "q": "Write down a situation of your own in which exactly three "
                 "of the five stores change. Say which one empties, which two "
                 "fill, and how you would know each one had changed without "
                 "being told.",
            "field_label": "Your situation",
            "placeholder": "A cyclist at the top of a hill…",
            "success": [
                "Describes one situation, not three separate ones.",
                "Names three of the five stores by their proper names.",
                "Says clearly which store empties and which two fill.",
                "Gives an observation for each store — a speed, a "
                "temperature, a height, a stretch or a substance changing.",
                "Does not name sound, light or electric current as a store.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Energy is an amount that goes with a situation, measured in "
                "joules. Five situations hold it: movement, temperature, "
                "height, stretch and what a substance is made of. Sound, "
                "light and electric current are not stores; they are how one "
                "store empties into another.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    "stretch": [
        {"type": "explainer", "id": "two-more-fields",
         "text": "\"A change in position in a field\" is one phrase covering "
                 "more than gravity. Push two north poles of two magnets "
                 "together and let go: they fly apart, so something was "
                 "filled while you pushed. Rub a balloon on your jumper and "
                 "hold it near the wall and the same thing is true of "
                 "electric charge. Both are the same idea as lifting a book "
                 "— you moved something to where a field did not want it, and "
                 "the store filled by exactly what it cost you. You will meet "
                 "the magnetic one properly in <em>Magnetism and "
                 "electromagnetism</em> and the charge one in <em>Static "
                 "electricity</em>."},
    ],

    "support": [],

    "safety_note": "",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why light is not a store?",
              "cta": "Ask about this lesson",
              "anchor": "s-sort"},

    "ks4_becomes": "Energy stores and pathways used to account for a whole "
                   "change quantitatively, including efficiency and Sankey "
                   "diagrams.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
