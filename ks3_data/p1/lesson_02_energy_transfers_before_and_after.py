"""p1-02 — *Energy transfers: before and after*.

Ported from Claude Design's `p1-02-energy-transfers-before-and-after.dc.html`.
Her page is the structure and, under MRB-205, the default for the content too.

── WHAT THIS LESSON OWNS ───────────────────────────────────────────────

`KS3.P.CIS.02b` — comparing the starting with the final conditions of a
system, and describing which stores increased and which decreased — and
`KS3.P.ECT.03`, the list of transfer PROCESSES. The `ECT.03` allocation is
argued in `ks3_data/p1/__init__.py`: every process in that bullet is a
before-and-after situation, and Design's `DEVICES` bench is literally that
list, so the lesson that names the stores (`p1-01`) cannot also be the one
that works the transfers.

── ⚖️ MRB-204 · NO FORMULA BLOCK ON THIS PAGE ──────────────────────────

Design draws no triangle and no beam here, and none is added. The tally's
arithmetic is a SUM — `useful + wasted = total` — and had she drawn a shape
for it, a beam is what the rule would require. She states the sum as a line
of text (`sumLine`) instead, which is not a formula diagram and needs no
diagram treatment. The unit's two formula blocks are on `p1-03` and `p1-08`.

── ⚖️ MRB-278 · WHERE THE CORRECT ANSWER SITS ─────────────────────────

Design puts the correct option FIRST in both marked rungs, as she does on
every page. P1's sixteen marked rungs are planned 4/4/4/4 across the four
indices; `p1-01` took 0 and 2, and this lesson takes **1 and 3**.

⚠️ Every option's words and every distractor's correction are Design's,
verbatim. What moved is the order of four buttons. A rung is not a picture.

── ⚑ MISCONCEPTIONS · `ENER`, NOT `ENERGY` ────────────────────────────

Design's `NOTES-P1.md` §1 calls this lesson's misconception `ENERGY-03` and
says the `ENERGY-01`..`ENERGY-14` block was added to the register on
15 Aug 2026. No `ENERGY-` id has ever existed there, and the register's
prefix table carries a dated ruling that forbids one outright:

    "A physics lane meeting an energy misconception adds to `ENER`; it does
     not open `ENERGY`."

The `ENERGY` reservation was DISCHARGED when C7 opened `ENER` on
21 Aug 2026. `p1-01` minted `ENER-09` and `ENER-10`; this lesson mints
`ENER-11` and continues C7's numbering.

The section also carries a SECOND misconception quote — the torch beam as a
store — which re-confronts `ENER-10` rather than minting anything. It is
Design's own second quote, added across P1–P3 in her 23 Aug pass so that
every physics lesson matches the P4–P12 convention.
"""

LESSON = {
    "slug":  "energy-transfers-before-and-after",
    "title": "Energy transfers: before and after",
    "discipline": "physics",
    "unit": "Energy transfers",
    "family": "MODEL",

    "covers": ["KS3.P.CIS.02b", "KS3.P.ECT.03"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "energy", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 55,

    "requires": ["energy-stores"],
    "assumes": [],
    "references": [],
    "ks4_links": [],

    "meta_description": "A phone battery holds about 40,000 joules. Run it "
                        "flat and it weighs exactly the same. Learn the "
                        "before-and-after method: two columns, one total, "
                        "and what physicists really mean by wasted.",

    "big_question": "A phone battery holds about 40,000 joules. Run it flat "
                    "and the phone weighs exactly the same as it did when "
                    "full. So what actually left it?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Weigh it twice",          "done_when": "committed"},
        {"anchor": "s-tally",  "short": "TALLY",
         "label": "Before-and-after tally",  "done_when": "three_devices_tallied"},
        {"anchor": "s-waste",  "short": "WASTED",
         "label": "The word wasted",         "done_when": "all_four_judged"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",          "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Weigh the battery. Twice.",
        "prompt": "A fully charged power bank on a balance accurate to a "
                  "milligram. Use it until it is completely flat, then put "
                  "it back on the same balance. The reading has not "
                  "changed.",
        "commit": "Commit to what that tells you about energy.",
        # ⚑ MRB-177 — four accounts a real student gives, at one length.
        # Design's four, verbatim and in her order.
        "options": [
            "The balance is not sensitive enough to detect it",
            "Energy has no mass — it is a number, not a substance",
            "The energy is still in there, just unusable",
            "Air rushed in to replace what left",
        ],
        "reveal": "Energy is not stuff. Nothing was poured out of the "
                  "battery and nothing was consumed. The chemicals inside "
                  "were rearranged, and a number you can calculate about "
                  "that arrangement got smaller — while the same number, "
                  "calculated about the room, got bigger by exactly as "
                  "much. <strong>There is no substance to weigh, which is "
                  "why the balance has nothing to report.</strong>",
    },

    "misconceptions": [
        {"id": "ENER-11",
         "statement": "There is energy inside the battery, and using the "
                      "phone lets it leak out until there is none left.",
         "elicited_by": "s-hook",
         "confronted_by": "before-after-tally"},
        # Design's second quote. Re-confronts p1-01's mint; mints nothing.
        # ⚠️ NAMES THE ACTIVITY, NOT THE SECTION. MRB-244/248 resolve
        # `elicited_by` / `confronted_by` against elements the page actually
        # carries, and a section anchor is not one — `s-think` failed both
        # gates until this pointed at the confrontation's own id.
        {"id": "ENER-10",
         "statement": "Light, sound and electricity are kinds of energy that "
                      "things store.",
         "elicited_by": "think-battery-leak",
         "confronted_by": "think-battery-leak"},
    ],

    "core": [
        {"type": "hook", "anchor": "s-hook", "id": "hook-commit"},

        {"type": "explainer",
         "text": "Last lesson you learned where energy can sit. This lesson "
                 "is about the only thing you ever actually do with that "
                 "list: put a number next to each store before, put a "
                 "number next to each store after, and check that the two "
                 "columns add up to the same total. <strong>That check is "
                 "the whole of energy physics.</strong> Everything else is "
                 "arithmetic."},

        # ── #s-tally — bare `ks3-block` on Design's markup → `check`.
        {"type": "before-after-tally", "id": "before-after-tally",
         "anchor": "s-tally",
         "demand": "investigate",
         "targets": "ENER-11",
         "eyebrow": "The before-and-after tally · put numbers on it",
         "heading": "Two columns. One total.",
         "prompt": "Pick a transfer, then drag the slider to decide how "
                   "much of the starting energy ends up doing the job you "
                   "wanted. The rest is not lost — watch where the tally "
                   "puts it.",
         "head_counter": {"format": "{n} of 4 devices tallied", "total": 4,
                          "done": "all four tallied"},
         # The commit gate. Design opens the bench only once this is
         # answered, and answering it marks the bulb as seen.
         "gate": {
             "prompt": "Commit first. An old filament bulb takes in 60 J of "
                       "energy each second and gives out about 3 J as "
                       "light. Where are the other 57 J?",
             "options": [
                 "Used up making the bulb work",
                 "Filling a thermal store in the bulb and the room",
                 "Lost — that is what makes it inefficient",
                 "Still in the wires as electrical energy",
             ],
             "marks": "bulb",
         },
         "slider": {"min": 0, "max": 100, "step": 1, "start": 50,
                    "near": 6},
         "devices": [
             {"id": "bulb", "label": "Filament bulb", "total": 60, "real": 5,
              "from": "Chemical store, at the power station",
              "job": "Light leaving the bulb",
              "note": "A filament bulb is a heater that happens to glow. "
                      "About 3 J of every 60 leaves as light and the rest "
                      "warms the room — which is why they were banned, and "
                      "why an LED doing the same job takes 8 J instead of "
                      "60."},
             {"id": "kettle", "label": "Kettle", "total": 100, "real": 90,
              "from": "Chemical store, at the power station",
              "job": "Thermal store of the water",
              "note": "A kettle is close to the best a device can be, and "
                      "for a simple reason: the job you want is a thermal "
                      "store, and the energy that escapes to the room is "
                      "thermal too. There is almost nothing for it to be "
                      "wasted as."},
             {"id": "lift", "label": "Electric winch", "total": 500,
              "real": 70,
              "from": "Chemical store, at the power station",
              "job": "Gravitational store of the load",
              "note": "The 30 J in every 100 that does not lift the load "
                      "warms the motor windings, the gearbox and the "
                      "cable. Run a winch hard for ten minutes and you can "
                      "feel every joule of it."},
             {"id": "runner", "label": "Sprinter", "total": 400, "real": 25,
              "from": "Chemical store, in food",
              "job": "Kinetic store of the runner",
              "note": "A human is a poor machine and a good heater. "
                      "Three-quarters of the chemical store you spend "
                      "sprinting ends up as a thermal store in your own "
                      "body, which is precisely why you sweat."},
         ]},

        {"type": "key-fact", "id": "two-columns-one-total",
         "ground": "card",
         "text": "To describe any transfer, say which store empties, which "
                 "stores fill, and by how much. The two columns must add to "
                 "the same total."},

        # ── #s-waste — `ks3-block ks3-dark ks3-practical` → `practical`.
        #
        # ⚠️ THE PAYLOAD KEY IS `items`, NOT `cards`. `cards` is claimed by
        # `r_activity` (build_ks3.py — `if a.get("cards"): parts.append(
        # r_cards(...))`), so a payload carrying it gets a second, blank
        # flip-card renderer on top of its own and the instrument renders
        # twice. c8 raises on the name for the same reason.
        {"type": "waste-sort", "id": "waste-sort",
         "anchor": "s-waste",
         "demand": "classify",
         "eyebrow": "The word “wasted” · say what you mean",
         "heading": "Wasted energy has not gone anywhere strange",
         "prompt": "For each of these, decide whether the energy ending up "
                   "in the surroundings is a problem or the entire point.",
         "choices": ["Wasted", "The point"],
         "sort_items": [
             {"id": "w1",
              "text": "A filament bulb warms the room it is lighting.",
              "answer": "Wasted",
              "right": "Wasted — you were buying light, and you are paying "
                       "for 57 J of warm room you did not ask for.",
              "wrong": "You were paying for light. The warm room is real "
                       "energy in a real store, but it is not the job you "
                       "wanted done."},
             {"id": "w2",
              "text": "An electric heater warms the room it is in.",
              "answer": "The point",
              "right": "The point. Identical physics to the bulb, opposite "
                       "verdict — because this time the warm room is what "
                       "you were buying.",
              "wrong": "Not wasted. This is the one device where "
                       "“energy ends up as a thermal store in the "
                       "room” is exactly the job."},
             {"id": "w3",
              "text": "A phone gets warm while charging.",
              "answer": "Wasted",
              "right": "Wasted. You wanted the chemical store filled, not "
                       "the back of the phone warmed — and it is why fast "
                       "charging is harder than it sounds.",
              "wrong": "You were trying to fill the battery. Warmth in the "
                       "phone case is energy that did not get there."},
             {"id": "w4",
              "text": "A tumble dryer warms the clothes inside it.",
              "answer": "The point",
              "right": "The point — warming the water in the clothes is "
                       "exactly how a dryer works.",
              "wrong": "This one is genuinely the job. The dryer warms the "
                       "water so it evaporates; the thermal store is the "
                       "mechanism, not a side effect."},
         ],
         "close": "Identical physics, opposite verdicts. A heater and a "
                  "kettle and a filament bulb all end with energy spread "
                  "thinly through a warm room; the only difference is "
                  "whether that was what you were paying for. "
                  "“Wasted” is a judgement about your intentions, "
                  "not a statement about where the joules went — and a "
                  "physicist who says “wasted” always means "
                  "“ended up somewhere too spread out to be "
                  "useful”, never “ceased to exist”."},

        # ── #s-think — `ks3-block ks3-misconception` → `misconception`.
        #
        # ⚠️ A REFERENCE, NOT THE BODY. `build_ks3` routes a `misconception`
        # block through `r_activity` by its id, so the payload lives in
        # `activities[]` below. Authored inline here it rendered NOTHING,
        # silently — the section did not exist, `#s-think` was on no element,
        # and MRB-208/244/248 all failed on the same missing anchor.
        #
        # ⚠️ A SECTION, NOT A RAIL STOP. Design's RAIL const on this page is
        # [s-hook, s-tally, s-waste, s-ladder]; `s-think` keeps its id so the
        # in-page anchor and the tutor link still land, and is absent from the
        # rail. Counted off her const, not off her audit prose.
        {"type": "misconception", "id": "think-battery-leak",
         "anchor": "s-think", "targets": "ENER-11"},

        {"type": "key-fact", "id": "name-store-store-pathway",
         "ground": "card",
         "text": "Describe a transfer by naming the store it started in, "
                 "the store it ended in, and the pathway between the two. "
                 "Before and after is the whole method — and the total is "
                 "the same in both pictures."},

        # ⚠️ WITHOUT THESE THE LADDER SECTION IS NEVER EMITTED. `#s-ladder`
        # is a rail stop on every page in the key stage, and MRB-208 fails a
        # stop whose anchor is on no element. Omitting them is silent: the
        # ladder data is authored, validated and simply never rendered.
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── activities ──────────────────────────────────────────────────────
    #
    # The two instruments are lifted into here from `core[]` by
    # `ks3_data/p1/__init__.py`'s `_normalise`, which is why they are not
    # written out. The confrontation is not an instrument and is authored
    # directly.
    "activities": [
        # ⊕ #s-think — ONE "Think again", TWO wrong ideas, which is the shape
        # Design draws and the shape `r_confrontation` was built for: the
        # second sits behind an amber-topped divider rather than in a block
        # of its own. `statements[]` is the authored form (b1-03 is the live
        # precedent); without it the block falls back to the register's
        # single quote and Design's second confrontation is dropped in
        # silence.
        {"id": "think-battery-leak",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-11",
         "statements": [
             {"targets": "ENER-11",
              "quote": "There is energy inside the battery, and using the "
                       "phone lets it leak out until there is none left.",
              "body": [
                  "Two things. First, a battery does not contain energy the "
                  "way a bottle contains water — it contains chemicals in a "
                  "particular arrangement, and the energy is a number you "
                  "calculate about that arrangement. Nothing physically "
                  "drains. Second, and worse: the leaking picture has energy "
                  "vanishing at the far end. Follow it honestly and you have "
                  "to ask where the leak goes, and the answer is always "
                  "another store you could point at and measure.",
                  "The test is the balance from the hook. A flat battery "
                  "weighs the same as a full one to a milligram. Whatever "
                  "left it, it was not a substance — and the phone, the "
                  "charger and the air around them are all very slightly "
                  "warmer than they would otherwise have been, by an amount "
                  "that adds up to exactly what the battery started with.",
              ]},
             {"targets": "ENER-10",
              "quote": "The light between the torch and the wall is a store "
                       "of energy.",
              "body": [
                  "A pathway is a route, not a container. Light, sound, an "
                  "electric current and heating are all ways energy gets "
                  "from one store to another; none of them holds it. If you "
                  "switch the torch off, the light in the room is gone in a "
                  "few billionths of a second, because there was never "
                  "anything there to empty. The chemical store in the cell "
                  "is what emptied, and the thermal store of the wall is "
                  "what filled.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [],

    "ladder": {
        "recall": {
            "q": "What must be true about the total energy before and after "
                 "any transfer?",
            # MRB-278: correct at index 1.
            "options": [
                "The total afterwards is smaller, because some is used up",
                "The two totals are equal",
                "The total afterwards is larger, because the device adds "
                "energy",
                "It depends how efficient the device is",
            ],
            "answer": 1,
            "feedback": {
                0: "Nothing is used up. If your two columns do not match, "
                   "you have missed a store — usually a thermal one.",
                2: "No device creates energy. A device only moves it "
                   "between stores.",
                3: "Efficiency changes how the energy is shared out at the "
                   "end, never the total.",
            }},
        "apply": {
            "q": "A 60 W filament bulb takes in 60 J each second and emits "
                 "3 J of light. What is the correct thing to say about the "
                 "other 57 J?",
            # MRB-278: correct at index 3.
            "options": [
                "It is lost, the way water is lost down a drain",
                "It is used up in the work of lighting the bulb",
                "It stays in the wires as electrical energy, ready for "
                "later",
                "It fills a thermal store in the bulb and the room",
            ],
            "answer": 3,
            "feedback": {
                0: "“Lost” is the word to avoid — it is "
                   "somewhere specific, and a thermometer can find it.",
                1: "Making the bulb work is not a place energy can go. "
                   "Name the store.",
                2: "Electrical is a pathway, not a store — nothing sits in "
                   "the wires holding it.",
            }},
        "explain": {
            # ⚠️ No markup in a rung question — `r_ladder` escapes it.
            "q": "An electric winch uses 500 J to lift a crate, and the "
                 "crate gains 350 J in its gravitational store. Account "
                 "for all 500 J, and explain why the missing amount is not "
                 "a failure of conservation.",
            "field_label": "Your account",
            "placeholder": "Of the 500 J supplied…",
            "success": [
                "States that 350 J fills the gravitational store of the "
                "crate.",
                "States that the remaining 150 J fills thermal stores.",
                "Names where those thermal stores are — motor, gearbox, "
                "cable, air.",
                "Says the two columns still total 500 J.",
                "Says the 150 J is wasted rather than lost, and explains "
                "that “wasted” means not doing the job you "
                "wanted.",
            ]},
        "produce": {
            "q": "A shopkeeper replaces every filament bulb in a shop with "
                 "LEDs and finds that the heating bill goes up slightly in "
                 "winter. Explain why, and say whether the change was "
                 "still worth making.",
            "field_label": "Your answer",
            "placeholder": "The old bulbs were filling a thermal store…",
            "success": [
                "Says the old bulbs were filling a thermal store in the "
                "shop as well as giving light.",
                "Says that warmth was doing part of the heater’s job, "
                "whether or not anyone intended it.",
                "Says the LEDs use far less energy in total for the same "
                "light.",
                "Says the heating system has to make up a small part of "
                "the difference.",
                "Concludes that the total energy used still falls, and "
                "notes that in summer the old bulbs made the cooling "
                "problem worse.",
            ]},
    },

    "key_note": "Name the store that empties, name every store that fills, "
                "and make the two totals match. Energy that ends up spread "
                "thinly through the surroundings is called wasted — it has "
                "not gone anywhere you cannot point at.",

    "stretch": [
        {"type": "explainer", "id": "second-law-seed",
         "text": "There is a direction to all of this that the tally does "
                 "not show. You can take 60 J of chemical store and end up "
                 "with 60 J spread through a warm room, easily, every "
                 "time. You cannot take a warm room and get the 60 J back "
                 "into a battery — not because it would break the sum, but "
                 "because the energy is now shared out among so many "
                 "particles, moving so randomly, that there is no way to "
                 "gather it up. Every transfer in this lesson runs "
                 "downhill in that sense, from concentrated to spread out, "
                 "and none of them will run backwards on their own. This "
                 "is the <em>second law of thermodynamics</em>, and it is "
                 "the reason the universe has a past and a future rather "
                 "than just a sequence of frames."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "transfer",
         "definition": "A change that moves energy from one store to "
                       "another. Described by saying which store emptied, "
                       "which filled, and by how much."},
        {"term": "wasted energy",
         "definition": "Energy that ends up in a store you did not want "
                       "filled — almost always a thermal store in the "
                       "surroundings. It has not been destroyed, only "
                       "spread out too thinly to be useful."},
        {"term": "useful energy",
         "definition": "The part of the energy that ends up doing the job "
                       "the device was chosen for."},
        {"term": "surroundings",
         "definition": "Everything around the thing you are studying — the "
                       "air, the bench, the room. Where wasted energy "
                       "ends up."},
    ],

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still picturing energy as something that drains?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Sankey diagrams and efficiency — the same two columns, "
                   "drawn to scale and turned into a percentage.",

    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ⊕ Design's closing note, kept because it is the honesty about the model
    # that the page is teaching with — and authored as `convention_note`,
    # which is the slot `build_ks3` actually reads for it.
    #
    # ⚠️ IT SHIPPED AS `model_note` FIRST AND RENDERED NOTHING. `ks3_key_audit`
    # caught it on the pre-push hook — "1 authored key(s) read by nothing. A
    # key with no read site is content that never reaches a student." The
    # engine has three foot slots and this is the third: `safeguarding_note`
    # and `safety_note` both ship `ks3-safety` treatment, and `convention_note`
    # is plain `ks3-legal`, described in build_ks3 as "a note about how the
    # numbers on this page were taken". That is exactly what this is, so it
    # takes that slot rather than a new one.
    "convention_note": "The tally is a teaching model. Each device is given a "
                  "round input in joules and a single useful output, so "
                  "that the before and after columns balance exactly. Real "
                  "efficiencies vary with the model, its age and how it is "
                  "used, and no appliance matches its figure to the joule. "
                  "The useful and wasted split depends on the job you "
                  "wanted done, which is why the same warm room counts as "
                  "waste from a bulb and as the whole point of a heater.",
}
