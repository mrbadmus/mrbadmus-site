"""C2 L4 — Chemical symbols (CLASSIFY).

Authored against Design's approved page,
`docs/ks3/design-reference/c2/c2-04-chemical-symbols.dc.html` (601 lines), and
its measured specification, `docs/ks3/c2-inventory/PAYLOAD-MAP.md` §5.

Every student-facing string is byte-identical to the approved page.

── Two grids, one component ─────────────────────────────────────────────

NOTES §3 says *"c2-04 needs no instrument: it is two commit-and-reveal
grids."* That is true as a description and false as a build instruction —
neither grid existed. Both are `verdict-cards`, which is also c2-03's sorter:
one component, two layouts, three headline types. `#s-sort` is the auto-fit
grid with the 42px display SYMBOL as its headline; `#s-read` is the column
with a mono FORMULA. The contract is identical in all three instances — one
shot per card, unchosen options dim, the card's border goes to ink, a
display-font answer word and a why paragraph.

── The coming-soon row is dead ─────────────────────────────────────────

NOTES §7 says this page links forward to a lesson that "does not exist yet"
and should render a coming-soon row. §8 supersedes it and the page agrees:
line 298 is a plain live link, identical in shape to every other `Next in
this unit` row in the unit. `formulae` is authored, so `references` points
straight at it.

── Non-ASCII that carries science ──────────────────────────────────────

`CaCO₃` in READS item f4 uses U+2083, and it is the whole answer to that item
("Three capitals: Ca, C and O … The small 3 is a count, not an element"). The
hook prose carries `H₂O` and `CO₂` (U+2082 ×2), and the big question carries
`ã` in São Paulo. All four are lifted, not retyped.

⚑ For Mide's science gate, from Design's NOTES:
  * flag 11 — Mg given as "first and third letter, not the first two" and Cl
    as "not Ch". The page admits its own exceptions ("the rule is looser than
    it looks") rather than stating a clean rule that is false.
  * flag 12 — Berzelius, 1813, in the stretch layer.
"""

# ── the three buckets, offered against all nine symbols ──────────────────
# Page line 329. Shared, which is what makes `#s-sort` the shared-option case;
# `#s-read` authors four options per item instead.
ORIGINS = ["First letter", "First two letters", "From an older name"]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 170 character for character.
    "slug":        "chemical-symbols",
    "title":       "Chemical symbols",
    "discipline":  "chemistry",
    "unit":        "atoms-elements-and-compounds",
    "family":      "CLASSIFY",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚑ The symbols half of AEC.03; `formulae` owns the formulae half.
    "covers":      ["KS3.C.AEC.03a"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 45,

    # ── progression edges ───────────────────────────────────────────────────
    "requires":    ["compounds"],
    "assumes":     [],
    "references":  ["formulae"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    # ⚠️ Straight ASCII double quotes around "salt", and `ã` in São Paulo.
    # Both are the page's own bytes.
    "big_question": "A chemist in Lagos, one in Osaka and one in S\u00e3o Paulo "
                    "write the same thing for salt. None of them writes "
                    "\"salt\".",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FIVE stops. The page's `hint-placeholder-count="4"` at line 55 is a
    # stale Design-tool affordance with no effect on the hydrated page.
    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",  "label": "Why symbols",
         "done_when": "committed"},
        {"anchor": "s-sort",  "short": "SORT",  "label": "Nine symbols",
         "done_when": "all_items_decided"},
        {"anchor": "s-read",  "short": "READ",  "label": "Read four labels",
         "done_when": "all_items_decided"},
        {"anchor": "s-think", "short": "THINK", "label": "CO and Co",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "title": "You can read part of a chemistry book in a language you do "
                 "not speak.",
        "prompt": "Open a Japanese chemistry textbook and almost none of it is "
                  "available to you. Then you reach an equation, and there it "
                  "is: NaCl, H\u2082O, CO\u2082 — exactly as you would write "
                  "it. The words changed and the chemistry did not.",
        "commit": "Why do chemists write in symbols instead of names?",
        "options": [
            "To save time writing",
            "So that one written symbol means one element, in every language",
            "To make chemistry look more scientific",
            "Because some element names are very long",
        ],
        "reveal": "Saving letters is the least of it. A symbol means exactly "
                  "one element, in every country, with no translation and no "
                  "argument about which substance was meant. That is worth far "
                  "more than the eight characters it saves.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    "misconceptions": [
        {"id": "ATOM-08",
         "statement": "The symbol is just a short version of the name, so "
                      "sodium should be So and it does not matter much if you "
                      "write NA.",
         "elicited_by": "think-commit-co",
         "confronted_by": "think-commit-co"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every element has a symbol of one or two letters. The first "
                 "is always a capital; the second, if there is one, is always "
                 "lower case. That rule looks fussy until you meet the pair it "
                 "exists for."},

        # #s-sort — verdict-cards, GRID layout, 42px display symbol headline.
        # A light `.ks3-block` with no ground override (the one sorter in the
        # unit that sits on the shell's own card).
        {"type": "verdict-cards", "id": "where-symbols-come-from",
         "anchor": "s-sort",
         "eyebrow": "Your turn · nine symbols",
         "heading": "Where does each symbol come from?",
         "head_counter": {"format": "{n} of 9 placed", "total": 9},
         "demand": "classify",
         "prompt": "Some symbols are the first letter of the English name. "
                   "Some are the first two. And some look like a mistake until "
                   "you know where they came from.",
         "layout": "grid",
         "headline": "symbol",
         "options": ORIGINS,
         "items": [
             {"id": "H", "headline": "H", "sub": "Hydrogen",
              # `origin` is authored and read by nothing (map N16): the card
              # reveals `why` on any pick. Design's intent, kept and flagged.
              "origin": 0,
              "why": "First letter of the English name, and it got there first — no other element beginning with H could have it."},
             {"id": "C", "headline": "C", "sub": "Carbon",
              # `origin` is authored and read by nothing (map N16): the card
              # reveals `why` on any pick. Design's intent, kept and flagged.
              "origin": 0,
              "why": "First letter. Calcium arrived later and had to take two letters instead."},
             {"id": "Ca", "headline": "Ca", "sub": "Calcium",
              # `origin` is authored and read by nothing (map N16): the card
              # reveals `why` on any pick. Design's intent, kept and flagged.
              "origin": 1,
              "why": "C was already taken by carbon, so calcium takes the first two letters of its name."},
             {"id": "Cl", "headline": "Cl", "sub": "Chlorine",
              # `origin` is authored and read by nothing (map N16): the card
              # reveals `why` on any pick. Design's intent, kept and flagged.
              "origin": 1,
              "why": "First two letters — except it is not Ch, because that was already spoken for elsewhere. The rule is looser than it looks."},
             {"id": "Mg", "headline": "Mg", "sub": "Magnesium",
              # `origin` is authored and read by nothing (map N16): the card
              # reveals `why` on any pick. Design's intent, kept and flagged.
              "origin": 1,
              "why": "Two letters, and not the first two: Ma would have clashed, so it uses the first and third."},
             {"id": "Na", "headline": "Na", "sub": "Sodium",
              # `origin` is authored and read by nothing (map N16): the card
              # reveals `why` on any pick. Design's intent, kept and flagged.
              "origin": 2,
              "why": "From natrium, the Latin name. It is why its compounds have been called soda for centuries."},
             {"id": "Fe", "headline": "Fe", "sub": "Iron",
              # `origin` is authored and read by nothing (map N16): the card
              # reveals `why` on any pick. Design's intent, kept and flagged.
              "origin": 2,
              "why": "From ferrum, the Latin for iron — which is also where ferry, farrier and ferrous come from."},
             {"id": "Pb", "headline": "Pb", "sub": "Lead",
              # `origin` is authored and read by nothing (map N16): the card
              # reveals `why` on any pick. Design's intent, kept and flagged.
              "origin": 2,
              "why": "From plumbum, the Latin for lead, and the reason a person who fits water pipes is called a plumber."},
             {"id": "Au", "headline": "Au", "sub": "Gold",
              # `origin` is authored and read by nothing (map N16): the card
              # reveals `why` on any pick. Design's intent, kept and flagged.
              "origin": 2,
              "why": "From aurum. Every element with a Latin symbol is one that people were already working with thousands of years ago."},
         ],
         "close": "The odd ones are not random. They are Latin, and they are "
                  "the elements people had already been working with for "
                  "thousands of years before English existed — gold, iron, "
                  "lead, copper, sodium, potassium. A symbol that looks wrong "
                  "is usually a fossil."},

        {"type": "key-fact", "ref": "one-capital"},

        # #s-read — the same component, COLUMN layout, mono formula headline,
        # four options authored per item, on inset ground.
        {"type": "verdict-cards", "id": "read-four-labels", "anchor": "s-read",
         "ground": "inset",
         "eyebrow": "Read it back · four labels",
         "heading": "How many elements are in this?",
         "head_counter": {"format": "{n} of 4 read", "total": 4},
         "demand": "classify",
         "prompt": "Count the capital letters. Each one starts a new element, "
                   "and a lower-case letter always belongs to the capital in "
                   "front of it.",
         "layout": "column",
         "headline": "formula",
         "items": [
             {"id": "f1", "headline": "NaCl", "sub": "Table salt",
              "answer": "Two elements.",
              "options": ["One", "Two", "Three", "Four"],
              "why": "Two capitals: Na and Cl. Sodium and chlorine. Four letters, two elements."},
             {"id": "f2", "headline": "CO", "sub": "The gas from a faulty boiler",
              "answer": "Two elements.",
              "options": ["One", "Two", "Three", "Four"],
              "why": "Two capitals: C and O. Carbon and oxygen — carbon monoxide."},
             {"id": "f3", "headline": "Co", "sub": "A hard silvery metal",
              "answer": "One element.",
              "options": ["One", "Two", "Three", "Four"],
              "why": "One capital, one lower-case letter. Cobalt. The same two letters as the line above, and a completely different substance."},
             {"id": "f4", "headline": "CaCO₃", "sub": "Chalk, limestone and marble",
              "answer": "Three elements.",
              "options": ["One", "Two", "Three", "Four"],
              "why": "Three capitals: Ca, C and O. Calcium, carbon and oxygen. The small 3 is a count, not an element."},
         ]},

        {"type": "misconception", "id": "think-commit-co", "anchor": "s-think",
         "targets": "ATOM-08"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "one-capital",
         "text": "One capital letter starts one element. CO is carbon and "
                 "oxygen; Co is cobalt. The case of the second letter is not a "
                 "style choice.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        {"id": "think-commit-co",
         "kind": "predict",
         "demand": "explain",
         "targets": "ATOM-08",
         "prompt": "Commit to what CO and Co mean before you read on.",
         "options": [
             "They are the same thing written two ways",
             "CO is two elements joined; Co is one element, cobalt",
             "CO is cobalt; Co is carbon monoxide",
             "Only one of them is a real substance",
         ],
         "reveal": [
             "<strong>CO</strong> is two capitals, so it is two elements: "
             "carbon and oxygen, joined — carbon monoxide, the gas that kills "
             "people in their sleep. <strong>Co</strong> is one capital with a "
             "lower-case letter after it, so it is one element: cobalt, a hard "
             "silvery metal used in magnets and batteries.",
             "Writing NA instead of Na is not untidy handwriting; it says "
             "nitrogen-and-something. And sodium is Na because its old name is "
             "<em>natrium</em>, which is also why its compounds were called "
             "soda long before anyone knew what was in them.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        "recall": {
            "q": "How many elements are in the formula MgO?",
            "options": [
                "Two",
                "One",
                "Three",
                "It depends on the amounts",
            ],
            "answer": 0,
            "feedback": {
                1: "Two capitals means two elements. Mg is magnesium and O is oxygen.",
                2: "The lower-case g belongs to the M in front of it. Only capitals start elements.",
                3: "Counting elements is just counting capital letters. Amounts come from the small numbers.",
            }},
        "apply": {
            "q": "A student writes the formula for carbon monoxide as Co. What have they written?",
            "options": [
                "Cobalt — one element, and a metal",
                "Carbon monoxide, just written untidily",
                "Carbon, on its own",
                "Nothing — Co is not an element",
            ],
            "answer": 0,
            "feedback": {
                1: "There is no untidy in this notation. One capital followed by a lower-case letter is one element, and that element is cobalt.",
                2: "Carbon alone is C. Adding a lower-case o makes a different symbol altogether.",
                3: "Co is cobalt, atomic number 27. That is exactly why the mistake is dangerous.",
            }},
        "explain": {
            "q": "Explain why chemists agreed on symbols rather than names, using two things symbols can do that names cannot.",
            "field_label": "Your explanation",
            "placeholder": "A name changes depending on…",
            "success": [
                "Says names differ between languages while symbols are the same everywhere.",
                "Says a symbol refers to exactly one element with no ambiguity.",
                "Says symbols can be combined into formulae that can be read at a glance.",
                "Mentions that some symbols come from older Latin names, so the symbol is not always the name shortened.",
                "Does not give \"it is quicker to write\" as the main reason.",
            ]},
        "produce": {
            "q": "A new element is made in a laboratory and needs a symbol. Every one-letter and most two-letter options are taken. Say what rules the symbol must follow, suggest one, and say how you checked it was free.",
            "field_label": "Your answer",
            "placeholder": "The symbol must start with…",
            "success": [
                "Says the first letter must be a capital and any second letter lower case.",
                "Says it must not already belong to another element.",
                "Suggests a specific symbol and links it to a name or a reason.",
                "Says how the check was done — against the periodic table.",
                "Notes that the symbol will be used in every language, so it should not depend on English.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Every element has a one- or two-letter symbol: capital first, "
                "lower case second. A capital letter always starts a new "
                "element, so counting capitals counts elements. Some symbols "
                "come from Latin names — Na, K, Fe, Pb, Au, Cu — and those are "
                "the elements people knew first.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    "stretch": [
        {"type": "explainer", "id": "berzelius",
         "text": "Before symbols, alchemists used pictures — a crescent for "
                 "silver, a circle with a dot for gold — and kept them "
                 "deliberately obscure so that rivals could not read their "
                 "notes. Chemistry only became a subject that could be shared "
                 "when Berzelius proposed letters taken from the Latin names "
                 "in 1813. The change from a private code to a public notation "
                 "is not a footnote in the history of chemistry; it is most of "
                 "the reason there is one."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why Na is not So?",
              "cta": "Ask about this lesson",
              "anchor": "s-sort"},

    "ks4_becomes": "Balanced symbol equations, and reading a formula for what "
                   "it says about the amounts.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
