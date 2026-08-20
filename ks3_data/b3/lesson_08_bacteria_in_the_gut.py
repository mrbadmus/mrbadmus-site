"""B3 L8 — Bacteria in the gut (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b3/b3-08-bacteria-in-the-gut.dc.html` (520 lines), and its
author's notes, `docs/ks3/design-reference/b3/NOTES-B3.md` §3.6 and flags 20–23. Schema per
architecture.md §4.8 as amended by §4.8.1 and §4.8.2; shape follows
`ks3_data/c1/lesson_02_solids_liquids_and_gases.py`.

Every student-facing string is byte-identical to the approved page, with the
five documented exceptions listed under "What could not be lifted" below.

── FOUR rail stops — Design's fourth restored (MRB-249) ────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to read "the rail is
THREE stops, not Design's four", on MRB-208 rule 2, and called this the plainer
of the two cases in the pair. Design's rail lists `s-hook`, `s-jobs`, `s-deal`,
`s-ladder`, and its own tick function reads:

    if (id === 's-hook') return s.hookChoice !== null;
    if (id === 's-jobs') return JOBS.every((j) => s.off[j.id]);
    if (id === 's-deal') return s.hookChoice !== null;

The argument was that `#s-deal` is an eyebrow, a statement, three cards and a
key fact — no control, no commitment, no field — so
`ks3_parity.check_rail_reachable` would fail it for carrying none of the
signals `doneByDom()` reads, and that inventing a control Design did not draw
is closed to this build. So the stop came off.

Two things overrule that.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine.

And the third line above is Design stating how `#s-deal` ticks. `isDone()` is a
rail-level function; writing `s.hookChoice !== null` against `s-deal` is a
declaration, not an oversight. Both sides of the deal is the reading-back of
the germ-free mouse the student already answered on, so the section carries no
control of its own. That is a MIRROR, resolved at rail level in `wireRail`'s
`paint()`.

So the stop is declared: anchor `s-deal`, `mirrors: "s-hook"`,
`done_when: "committed"` — stage one's predicate, named as borrowed rather than
smuggled, and gated by `ks3_parity.check_rail_matches_design` against
`docs/ks3/rail-manifest.md`.

⚠️ One observation from the old argument SURVIVES the reversal and is not
answered by it: this mirror reaches BACKWARDS PAST a section, to `s-hook` two
stops earlier rather than to `s-jobs` next door. So a student who answers the
hook and never scrolls to `#s-deal` sees its stop ticked. That is what Design
drew and MRB-205 settles which of us wins, but it is the one page in B3 where
the mirror is not simply "the payoff of the instrument beside it", and it is
recorded here rather than quietly dropped.

`#s-think` is still not a candidate — Design draws no stop on it, and on this
page it is two quotes and two paragraphs with nothing to answer. `#s-deal`
keeps its anchor, as it always did: hash links into it still work, and the
tutor card still points at it.

── What could not be lifted byte-identical, and why ────────────────────

1. **The inline link in `#s-think`.** Design writes "You met this in <a
   href="b1-06-unicellular-organisms.html">Unicellular organisms</a>".
   `rich()` allows `<em>` and `<strong>` and nothing else, so the WORDS are
   unchanged and the hyperlink is dropped; `references` renders the
   destination in the end matter, which is where the engine puts cross-lesson
   navigation.
2. **Italics on the binomial, in the LADDER only.** `_rung_marked` escapes a
   rung's question and its options with `t()`, not `rich()` — correctly, since
   an option's feedback also travels inside an attribute — so
   `<em>C. difficile</em>` would render as visible tag soup there. The italics
   are dropped from rung 2's question, options and feedback and kept
   everywhere else on the page, where `rich()` runs: `#s-think`'s
   *E. coli* and the stretch layer's *Clostridioides difficile* are intact.
3. **The `#s-deal` card TAGS.** Design's card carries a mono accent tag
   ("What you get") above the name; the shipped `rule` card is `term` +
   `gloss` and has no tag slot. Tag and name are joined with Design's own
   middle-dot idiom, so both strings survive and neither is invented. These
   three tags are not ordinals — they say which side of the deal the card is —
   so losing them would have cost the section its argument.
4. **The `#s-jobs` reveal loses its 340 ms arrive animation.** Design defines
   a `b308-arrive` keyframe in the page's own `<style>`; the shipped
   stylesheet has no such keyframe and this build does not add one for two
   pages. The paragraph appears rather than rising into place. Nothing else
   about it moves, and the reduced-motion path Design guards is now the only
   path.
5. **The `#s-deal` key fact renders below the panel, not inside it.** The
   engine's key-fact box is a direct child of `.ks3-lesson`, positioned by
   document order. Same sequence, same treatment.

── Design decisions corrected ──────────────────────────────────────────

The rail (above), and the ladder's two page-marked rungs, which both failed
MRB-177 length parity as drawn. Both fixes complete the DISTRACTORS and leave
the correct answers untouched; each distractor keeps its misconception exactly.
The measurements are recorded on the rungs themselves.
"""

# ── the five jobs (page lines 304–320) ──────────────────────────────────
# ⚑ For Mide's gate, NOTES-B3 flag 21: the germ-free mouse needing about 30%
# more food, and whether these are the right consequences to list. Flag 22:
# the newborn vitamin K injection is used as the evidence for job 2 — correct
# and clinically real, and it names a routine medical intervention.
JOBS = [
    {"id": "fibre", "tag": "Job 1", "name": "Fermenting fibre",
     "what": "Your own enzymes cannot break cellulose. Gut bacteria can, and "
             "the fatty acids they release are absorbed through the large "
             "intestine wall and used by your cells.",
     "without": "A share of the energy in your food — up to about a tenth for "
                "some people — simply leaves the body undigested. The "
                "germ-free mouse needs 30% more food for the same growth, and "
                "this is most of the reason."},
    {"id": "vitamins", "tag": "Job 2", "name": "Making vitamins",
     "what": "Bacteria in the large intestine make vitamin K and several B "
             "vitamins as by-products of their own metabolism, and you "
             "absorb them.",
     "without": "Vitamin K deficiency, and blood that clots poorly. Newborn "
                "babies have almost no gut bacteria yet, which is exactly why "
                "they are given a vitamin K injection at birth."},
    {"id": "space", "tag": "Job 3", "name": "Occupying the space",
     "what": "Harmful species need somewhere to settle and something to eat. "
             "A gut already full of established bacteria offers neither.",
     "without": "Empty space and free food. This is why a course of "
                "antibiotics can be followed by an infection that the "
                "antibiotic was not treating — the competition was cleared "
                "away."},
    {"id": "immune", "tag": "Job 4", "name": "Training the immune system",
     "what": "A developing immune system learns what to attack and what to "
             "leave alone by encountering harmless bacteria early. The gut "
             "community is most of that encounter.",
     "without": "An immune system that has never been calibrated — slower "
                "against real threats, and more likely to react to things "
                "that are not threats at all."},
    {"id": "wall", "tag": "Job 5", "name": "Maintaining the gut wall",
     "what": "The fatty acids bacteria release are the preferred fuel of the "
             "cells lining the large intestine, and they signal those cells "
             "to keep the wall thick and the mucus layer intact.",
     "without": "A thin, poorly developed wall — measurable in the germ-free "
                "mouse, and a route for bacteria to cross where they should "
                "not."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 110 character for character.
    "slug":        "bacteria-in-the-gut",
    "title":       "Bacteria in the gut",
    "discipline":  "biology",
    "unit":        "nutrition-and-digestion",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # The whole statement, uncompounded: "the importance of bacteria in the
    # human digestive system". No sub-ID is needed or wanted — `substatements`
    # rule 3 mints lazily, and most bullets will never be split.
    "covers":      ["KS3.B.NUT.05"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 3},
                    {"id": "structure-function", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 45,

    # ── progression edges ───────────────────────────────────────────────────
    # Design draws all three end-matter cards here and they map one to one:
    # "Before this lesson" → the previous lesson, "Connects to" → two sideways
    # links, "At GCSE this becomes" → prose.
    "requires":    ["absorption-and-the-small-intestine"],
    "assumes":     [],
    "references":  [{"unit": "B1", "lesson": "unicellular-organisms"},
                    "a-balanced-diet"],
    "ks4_links":   [],
    "ks4_becomes": "Communicable disease, antibiotic resistance, and the role "
                   "of the microbiome in health.",

    # ── framing ─────────────────────────────────────────────────────────────
    # ⚑ NOTES-B3 flag 20, for Mide's gate: ~30 trillion bacteria, and "several
    # million" bacterial genes against ~20 000 human. Order-of-magnitude
    # figures that are revised regularly; the legal line says so.
    "big_question": "You are carrying around thirty trillion bacteria in your "
                    "large intestine. Your immune system knows they are there "
                    "and leaves them alone. That is not a failure — it is the "
                    "arrangement.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-deal` is the third: no control of
    # its own, so it mirrors `s-hook` — two stops back, not next door — and
    # ticks on the hook's predicate. See the docstring. `short` and `label` are
    # Design's own `RAIL_SHORT` and `RAIL` strings (page lines 296–302).
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Germ-free mouse",
         "done_when": "committed"},
        {"anchor": "s-jobs",   "short": "JOBS",   "label": "Five jobs",
         "done_when": "all_five_jobs_off"},
        {"anchor": "s-deal", "short": "DEAL", "label": "Both sides",
         "mirrors": "s-hook", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # ⚠️ MRB-225. The germ-free mouse is introduced HERE and paid off in the
    # instrument's summary panel; nothing later takes it back. The four
    # consequences named in the prompt are what the five jobs then explain.
    # ⊕ MRB-269 finding 25: the two lists are NOT the same four in the same
    # order — the reveal includes vitamins and excludes the gut wall, and the
    # prompt does the reverse — so the reveal reads "all of these", not "all
    # four". The payoff is still a conclusion rather than a repeat.
    "phenomenon": {
        "kind": "narrative",
        "title": "Raise a mouse in a sterile bubble with no bacteria at all.",
        "prompt": "Sterile food, sterile air, sterile water, no bacteria "
                  "anywhere in or on it. The mouse survives — and it needs "
                  "about 30% more food than a normal mouse, has a thin and "
                  "poorly developed gut wall, an underdeveloped immune "
                  "system, and it is far easier to kill with an infection.",
        "commit": "Removing every bacterium made the mouse worse. Why?",
        "options": [
            "The sterile food was less nutritious",
            "Its gut bacteria had been doing jobs it cannot do itself",
            "Living in a bubble is stressful",
            "It could not digest anything at all without bacteria",
        ],
        "reveal": "Because the bacteria were doing jobs. Extracting energy "
                  "from fibre your own enzymes cannot touch, making vitamins "
                  "you cannot make, occupying space so that harmful species "
                  "have nowhere to settle, and training the immune system by "
                  "being there. The mouse lost all of these at once.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ THE `DIET` FAMILY IS NOT YET IN `docs/ks3/misconception-register.md`.
    # NOTES-B3 §5 says fifteen entries were "minted, not proposed", and the
    # register has no `DIET` row at all — so the ids are the unit's to register
    # in one pass, and this module deliberately does not write them (the
    # register is shared with the other seven lessons, authored in parallel).
    # Nothing fails meanwhile: `_misconception_quote` resolves from THIS list,
    # and both blocks carry their own `statements`, which win over the register
    # (build_ks3.py:2504).
    #
    # ⊕ THE SECOND ENTRY IS A RE-CONFRONTATION OF AN EXISTING ROW, not a new
    # id, and Design's own copy is the evidence: "You met this in Unicellular
    # organisms and it comes back with a bigger consequence." `CELL-08` is
    # owned by exactly that lesson and is the register's nearest statement of
    # the same belief. NOTES-B3 §5 asks for precisely this treatment in the
    # parallel enzymes case — "re-confront rather than restate" — and the
    # register's `reappears_in` column exists for it. `statement` below is the
    # register's own wording, so the two cannot drift; the costume the student
    # reads is in `statements[]` on the activity.
    "misconceptions": [
        {"id": "DIET-17",
         "statement": "Bacteria are germs. Having bacteria inside you means "
                      "you are ill.",
         "elicited_by": "hook",
         "confronted_by": "germs-and-simplicity"},
        {"id": "CELL-08",
         "statement": "A single-celled organism is just a simpler version of "
                      "one of our cells — the same parts, doing less.",
         "elicited_by": "job-switch",
         "confronted_by": "germs-and-simplicity"},
    ],

    # Design draws no keyword block anywhere in B3, so these definitions never
    # reach the lesson body. The TERMS reach a student as the unit page's
    # "Words this unit gives you" chips, and the reading-age gate reads them as
    # its exclusion list.
    "vocabulary": [
        {"term": "cellulose",
         "definition": "The tough material plant cell walls are built from. "
                       "Human enzymes cannot break it down.",
         "note": None},
        {"term": "ferment",
         "definition": "To break a substance down without using oxygen. Gut "
                       "bacteria ferment the fibre you cannot digest.",
         "note": None},
        {"term": "microbiome",
         "definition": "The whole community of microorganisms living in one "
                       "place — for example, in your large intestine.",
         "note": None},
        {"term": "antibiotic",
         "definition": "A medicine that kills bacteria or stops them "
                       "multiplying.",
         "note": "It cannot tell a useful species from a harmful one, which "
                 "is why clearing an infection can clear the competition too."},
    ],

    # NOTES-B3 flag 24 names two figure slots for this unit and neither is
    # this lesson's: `b3-gut-labelled` belongs to `the-digestive-system` and
    # `b3-villus-labelled` to `absorption-and-the-small-intestine`, which
    # registers it. Nothing on this page references a figure and none is
    # declared. Present and empty, never absent.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-jobs — the flagship. Ink-dark `practical`, per the measured table
        # in `ks3_data/b3/__init__.py`. Authored inline here and lifted into
        # `activities[]` by `_normalise`, which leaves the shell behind it.
        {"type": "job-switch", "id": "job-switch", "anchor": "s-jobs",
         "demand": "investigate",
         "targets": "CELL-08",
         "eyebrow": "Switch them off · five jobs",
         "heading": "Take one job away and see what breaks",
         "head_counter": {"format": "{n} of 5 switched off", "total": 5,
                          "start": 0},
         "prompt": "Every one of these is something your gut bacteria do "
                   "that your own cells cannot.",

         "jobs": JOBS,
         "labels": {"on": "Switch it off", "off": "Switched off",
                    "without": "Without it:"},

         # ⚖️ THE PAYOFF, and the reason the block exists. Five jobs off IS
         # the germ-free mouse from the hook, and the panel says so. The
         # renderer refuses a payload without it.
         "all_off": {
             "tag": "All five off",
             "headline": "You have just built the germ-free mouse.",
             "body": "It lives. It is simply worse at everything — more food "
                     "for the same growth, a weaker gut wall, missing "
                     "vitamins, and no defence in place when a harmful "
                     "species arrives. The bacteria were not tolerated. They "
                     "were part of the system."}},

        # #s-deal — Design's band-on-3px-ink statement panel with three cards.
        # That IS the `rule` shell (§5.1.1). NOT a `check` activity: there is
        # nothing to do in it, which is why its rail stop mirrors `s-hook`
        # rather than carrying a predicate of its own.
        {"type": "rule", "anchor": "s-deal",
         "eyebrow": "Both sides of the deal",
         "statement": "What each side gets, and what happens when the balance "
                      "shifts.",
         "cards": [
             {"term": "What you get · Chemistry you do not have",
              "gloss": "Energy from fibre, vitamin K and B vitamins, a "
                       "defended gut, a trained immune system and a "
                       "maintained wall. Five jobs, none of which your own "
                       "twenty thousand genes can do."},
             {"term": "What they get · A warm, fed, stable habitat",
              "gloss": "Constant 37 °C, a steady supply of food arriving from "
                       "above, no competition from outside, and no immune "
                       "attack. From the bacteria’s point of view your large "
                       "intestine is excellent property."},
             {"term": "When it shifts · The same species, the wrong place",
              "gloss": "A useful community in the large intestine becomes a "
                       "serious problem if it crosses into the blood, or if "
                       "antibiotics clear the space and one harmful species "
                       "takes over. What makes a bacterium dangerous is "
                       "usually location and abundance, not identity."},
         ]},

        {"type": "key-fact", "ref": "helpful-or-harmful-is-where"},

        {"type": "misconception", "id": "germs-and-simplicity",
         "anchor": "s-think", "targets": ["DIET-17", "CELL-08"]},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "helpful-or-harmful-is-where",
         "text": "Most bacteria in your gut are helpful and a few can be "
                 "harmful. Which they are depends on the species and on where "
                 "they are — the same bacterium can be useful in the large "
                 "intestine and dangerous in the blood.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # One entry. `job-switch` is authored inline in `core` and lifted here by
    # `ks3_data/b3/__init__.py::_normalise`.
    "activities": [
        # Design's `#s-think` is STATIC on this page — two quotes and two
        # paragraphs, nothing to answer — so it is a `confrontation` and not
        # C1's `predict`. Measured off the markup: no `ks3-options`, no
        # commit, no reveal. It carries no completion contract and is
        # correctly absent from the rail.
        #
        # ⚠️ The second `answer` drops an inline `<a href>` and keeps every
        # word; the two `<em>` runs on *E. coli* survive, because `rich()`
        # allows them. See "What could not be lifted" 1.
        {"id": "germs-and-simplicity",
         "kind": "confrontation",
         "demand": "confront the germ error and the one-cell-means-simple "
                   "error in one pass",
         "targets": ["DIET-17", "CELL-08"],
         "statements": [
             {"quote": "Bacteria are germs. Having bacteria inside you means "
                       "you are ill.",
              "answer": "Of the many thousands of bacterial species that "
                        "live on and in humans, the number that reliably "
                        "cause disease is a small minority. The rest are "
                        "neutral or useful, and the useful ones are doing "
                        "work you cannot do without: about a tenth of the "
                        "energy some people get from their food comes from "
                        "bacteria fermenting fibre, and a large part of "
                        "your vitamin K is made by bacteria in your own "
                        "large intestine. The word germ is not a biological "
                        "category at all — it is a word for “microorganism "
                        "I do not want here”, and the here matters more "
                        "than the what. <em>E. coli</em> lives harmlessly "
                        "in almost every human large intestine; the same "
                        "species in your bladder is a urinary infection and "
                        "in your blood it can kill you. Nothing about the "
                        "bacterium changed."},
             {"quote": "One cell means simple, so gut bacteria cannot be "
                       "doing anything complicated.",
              "answer": "You met this in Unicellular organisms and it comes "
                        "back with a bigger consequence. Your gut bacteria "
                        "collectively carry several million genes; you carry "
                        "about twenty thousand. They can build enzymes for "
                        "reactions no human cell can perform, which is "
                        "exactly why they can digest cellulose and make "
                        "vitamins and you cannot. It is not that they are "
                        "helping with your chemistry. They are running "
                        "chemistry you do not have."},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    "ladder": {
        "recall": {
            "title": "Rung 1 · What they do for you",
            "q": "Which of these can your gut bacteria do that your own cells "
                 "cannot?",
            # ⚖️ **CORRECTED FROM DESIGN — the distractors were too short
            # (MRB-177 length parity).**
            #
            # Design's set ran 5 / 7 / 3 / 5 words. The correct answer was
            # strictly the longest and beat the longest distractor 7 : 5,
            # which is exactly ×1.4 — the threshold, met. A student who has
            # worked out that the long one is usually right, which a class
            # works out early, could take this rung without reading it.
            #
            # Each distractor keeps its misconception EXACTLY: bacteria do the
            # absorbing, bacteria make the stomach acid, bacteria digest the
            # protein. Only the sentences are completed, and each completion
            # is a claim the option's own feedback already answers. All four
            # now read as full claims at 7–8 words, and the correct option is
            # no longer the longest. The correct option is unchanged, because
            # it is the science.
            "options": [
                "Absorb glucose from the gut into the blood",
                "Break down cellulose and make vitamin K",
                "Produce the hydrochloric acid that kills arriving bacteria",
                "Digest protein into the amino acids you absorb",
            ],
            "answer": 1,
            "feedback": {
                0: "Absorption is done by your own villus cells, in the small "
                   "intestine, and it happens perfectly well without bacteria.",
                2: "That is your stomach lining, and the acid actually kills "
                   "most bacteria that arrive with a meal.",
                3: "Your own protease does this, in the stomach and small "
                   "intestine. Bacteria are not needed for it.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            # ⚠️ Italics dropped throughout this rung: `_rung_marked` escapes
            # the question and the options with `t()` and puts the feedback in
            # an attribute, so `<em>` would render as tag soup. Words
            # unchanged. See "What could not be lifted" 2.
            "q": "A patient takes a broad-spectrum antibiotic for a chest "
                 "infection and two weeks later develops severe diarrhoea "
                 "from C. difficile. Why did clearing bacteria make a "
                 "bacterial infection more likely?",
            # ⚖️ **CORRECTED FROM DESIGN — the distractors were too short
            # (MRB-177 length parity).**
            #
            # Design's set ran 6 / 13 / 9 / 7 words. The correct answer was
            # strictly the longest, beat the longest distractor by 4 words AND
            # by ×1.44 — both limbs of the rule, on the rung that is supposed
            # to be the trap. A trap you can walk past by counting words is
            # not a trap.
            #
            # Each distractor keeps its misconception EXACTLY: the drug made
            # the organism stronger, the drug caused the diarrhoea directly,
            # the infection travelled. Only the sentences are completed, to
            # 11 / 12 / 11 words, so the correct answer at 13 leads by one
            # word and ×1.08.
            "options": [
                "The antibiotic made C. difficile itself stronger and harder "
                "to kill",
                "The antibiotic cleared the competing species, leaving space "
                "and food for C. difficile",
                "Antibiotics irritate the gut and cause diarrhoea directly, "
                "with no bacterium involved",
                "The chest infection spread down to the gut and multiplied "
                "there",
            ],
            "answer": 1,
            "feedback": {
                0: "The antibiotic did not improve it. What changed was its "
                   "situation — it faced no competition for space or food.",
                2: "They can irritate the gut, but this case names a specific "
                   "organism that has multiplied. That needs an explanation "
                   "about competition.",
                3: "Nothing travelled. The organism was almost certainly "
                   "already present in small numbers and was being held in "
                   "check.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the germ-free mouse",
            "q": "Explain why a germ-free mouse needs about 30% more food "
                 "than a normal mouse, and why it is also more vulnerable to "
                 "infection. Use at least three of the five jobs.",
            "field_label": "Your explanation",
            "placeholder": "It needs more food because… and it is more "
                           "vulnerable because…",
            "success": [
                "Says fibre is not fermented, so the energy in it is lost "
                "rather than absorbed.",
                "Says vitamins normally made by bacteria are absent and must "
                "come from food or be missing.",
                "Says nothing is occupying the gut, so an arriving harmful "
                "species meets no competition.",
                "Says the immune system has not been trained by harmless "
                "bacteria, so it responds less well.",
                "Ends on the general point: the bacteria were doing jobs, not "
                "being tolerated.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "Cows digest grass; humans cannot. Cows have no cellulase "
                 "enzyme of their own either. Using this lesson, explain how "
                 "a cow manages it, and say what this suggests about the size "
                 "of a cow’s gut compared with ours.",
            "field_label": "Your answer",
            "placeholder": "A cow can digest grass because…",
            "success": [
                "Says the cow relies on bacteria — and other microorganisms — "
                "to break down cellulose, not on its own enzymes.",
                "Says the products of that fermentation are then absorbed by "
                "the cow.",
                "Reasons that fermentation is slow, so the gut must hold food "
                "for a long time.",
                "Concludes the cow needs a much larger fermentation chamber "
                "than a human has — hence the multi-chambered stomach.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "The large intestine holds trillions of bacteria. They ferment "
                "fibre your own enzymes cannot digest, make vitamin K and some "
                "B vitamins, occupy space that harmful species would otherwise "
                "take, and help the immune system develop. A few species can "
                "cause disease, and antibiotics disturb the whole community "
                "rather than only the target.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚠️ MRB-225: the faecal transplant lives HERE and nowhere above, which is
    # where Design put it, and nothing earlier is retracted by it. The page's
    # argument — a gut community is an ecosystem with vacancies — is not
    # withdrawn by the stretch layer; the stretch layer is that argument taken
    # one step further into a treatment.
    #
    # ⚑ NOTES-B3 flag 23, for Mide's gate: the ~90% success rate for recurrent
    # C. difficile, and whether this example is wanted at KS3 at all. It is
    # the most startling thing in the unit. Lifted unchanged.
    "stretch": [
        {"type": "explainer", "id": "faecal-microbiota-transplant",
         "text": "One of the more startling treatments in modern medicine is "
                 "a faecal microbiota transplant: bacteria from a healthy "
                 "donor's gut, screened and prepared, introduced into a "
                 "patient whose own gut community has been destroyed — "
                 "usually by antibiotics, allowing "
                 "<em>Clostridioides difficile</em> to take over the empty "
                 "space and cause a severe, stubborn infection. Antibiotics "
                 "alone often fail, because they clear the space again for "
                 "the same organism to reoccupy. Restoring a full community "
                 "of competitors works in around nine cases out of ten. It is "
                 "a treatment that only makes sense once you stop thinking of "
                 "bacteria as contamination and start thinking of a gut "
                 "community as an ecosystem with vacancies."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to talk through why the same bacterium can be "
                      "helpful or harmful?",
              "cta": "Ask about this lesson",
              "anchor": "s-deal"},

    # ⊕ `convention_note`, not `safety_note`, and it is a judgement call worth
    # naming. Design draws ONE plain `.ks3-legal` paragraph carrying both
    # sentences. Splitting the second into `safety_note` would print it in the
    # treatment reserved for physical-hazard lines ("never light a candle
    # without an adult") and would split one paragraph into two. The page wins,
    # so both sentences stay together in the plain treatment Design chose.
    # ⚑ Flagged for Mide: this is the only medical-advice disclaimer in the
    # unit and he may want it in the heavier treatment after all.
    "convention_note": "Figures for bacterial numbers and gene counts are "
                       "order-of-magnitude estimates from current research "
                       "and are revised regularly. Nothing here is advice "
                       "about antibiotics or probiotics — those decisions "
                       "belong with a doctor.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # `analysis-and-evaluation` for the switch-it-off-and-follow-the-damage
    # method the whole instrument runs on; `scientific-attitudes` for the
    # order-of-magnitude figures the page states and then flags as revisable.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
