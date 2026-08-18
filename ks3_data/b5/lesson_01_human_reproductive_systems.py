"""B5 L1 — Human reproductive systems (SYSTEM).

Authored against Design's approved page,
`docs/ks3/design-reference/b5/b5-01-human-reproductive-systems.dc.html` (601 lines), under the
MRB-220 build contract (`docs/ks3/mrb-220-build-contract.md`).

Every student-facing string is lifted byte-identical from the approved page
except the items listed under "What could not be lifted", none of which is a
sentence of science. The nine functions, the eight structures with their
four-option pools, the five job rows and all four ladder rungs came out of
`node tools/extract_design_payload.js`, not off a keyboard.

── ⚠️ TONE IS A GATE ON THIS LESSON, AND DESIGN'S REGISTER STANDS ───────

Ruled 16 Aug 2026 (MRB-244) and set out in `ks3_data/b5/__init__.py`. This
lesson is read by 12- and 13-year-olds. Design's treatment is clinical and
function-first; anatomical names are used plainly with no euphemism; there is
no sexual detail beyond the statutory clause; nothing normative is said about
family structure; and "male system" / "female system" are properties of ORGANS
throughout — the page never makes a claim about a reader's identity, and the
five-job section is careful to say *the male system has no equivalent* rather
than anything about people.

**Nothing here was softened, sharpened or annotated.** No warning was added,
no sentence was hedged, and the legal line is carried whole. Where the authoring
brief and the page disagree about register the PAGE wins (MRB-205), and the two
places they do are reported below rather than resolved silently.

── `covers` is the SUB-ID, not the whole bullet ─────────────────────────

`KS3.B.REP.01` is the longest bullet in the KS3 biology spine and
`ks3_data/substatements.py` splits it at its own clause list. This lesson owns
**`KS3.B.REP.01a`** — the structure and function of the male and female
reproductive systems. It must NOT claim `REP.01` whole: `gametes-and-
fertilisation` owns `b`, `the-menstrual-cycle` owns `c`,
`gestation-placenta-and-birth` owns `d` and `lifestyle-and-the-developing-
foetus` owns `e`, and §5.7's exactly-once rule would fail the build on the
overlap. The page names the placenta and names fertilisation, and teaches
neither; both are `touches`.

── The flagship: eight structures, and every distractor is a real job ───

`#s-jobs` is `job-match`, on `ks3-block ks3-dark ks3-practical` (page line 104),
so `practical` is MEASURED from Design's own markup rather than inherited from
the hook above it. Nine functions, eight structures, four options per structure,
and **every option in every pool is the correct function of a different
structure** — no invented wrong answers anywhere. That is the instrument's
second purpose and NOTES-B5 §2.4 states the rule in terms for b5-06, which is
this instrument in a plant. A student who mis-assigns *hold* to the oviduct has
not chosen nonsense; they have chosen the uterus's job, which is the confusion
the lesson exists to find.

`close` — "Closes the lower end of the uterus and opens for birth" — is the one
function whose text names another structure. Kept as Design wrote it.

── FOUR rail stops — Design's fourth restored (MRB-249) ─────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to argue that `#s-pair`
came off the rail. Design draws FOUR stops and `#s-pair` ticks on
`Object.keys(s.opened).length >= 8` (page line 436) — the INSTRUMENT's
predicate, verbatim, one section to the left — and because `#s-pair` is an
eyebrow, a display statement, a lede, a five-row table and a key fact, with no
control, no commitment and no field, the reading was that MRB-208's
completion rule ruled it out and `ks3_parity.check_rail_reachable` would fail
it for exactly that. So the lesson shipped THREE stops.

Two things overrule that inference.

MRB-205 binds and is not re-argued: Design draws, we render; nothing invented,
nothing dropped; page wins over engine. Dropping a stop Design drew is not
rendering what Design drew.

And Design's `isDone()` states the tick condition. It is a rail-level function
and it returns the identical expression for `#s-jobs` and then for `#s-pair`.
The five jobs table is the payoff of the matching the student just did; the
section holds no control because the instrument already took the commitment.
That is a MIRROR, resolved at rail level in `wireRail`'s `paint()`.

So the fourth stop is declared: anchor `s-pair`, `mirrors: "s-jobs"`,
`done_when: "all_eight_checked"` — the instrument's own predicate, named as
borrowed, and gated by `check_rail_matches_design` against
`docs/ks3/rail-manifest.md`. b4-01's `#s-parts`, c1-02's `#s-matrix`, c1-05's
`#s-scale`, b3-01's `#s-nutrients` and b3-02's `#s-limits` are restored the
same way. **The section keeps its anchor**, as it always did, so every hash
link into it still works.

── What could not be lifted, and why ────────────────────────────────────

1. **The `#s-pair` lede paragraph.** Design writes *"Reproduction requires five
   things to happen. Read down the column and notice how much of the list falls
   to one system only."* between the display statement and the table.
   `r_comparison` has an eyebrow, a statement, columns, rows and a nested key
   fact, and no lede slot. `r_rule` has a `close` that would take it — but
   `rule` has no two-column table and no nested key-fact slot, and the table IS
   this section, so the component is not in question. The sentence is DROPPED
   rather than folded into the display statement, which is 40px type and would
   have printed two sentences in a slot Design gave one. Reported. The fix, if
   the lede is to win, is a `lede` key on `comparison` — b3-01, b4-03 and this
   lesson are three pages asking for the same slot.

2. **The `#s-pair` mono job labels keep their separators.** Design sets
   `Job 1 · Make gametes — shared` as one accent-mono line above the two cells;
   `r_comparison`'s row `name` is exactly that slot, so the string survives
   whole, separators included.

3. **Design draws TWO endmatter link cards; the engine emits one.** Her "Next in
   this unit" (`gametes-and-fertilisation`) and "Connects to"
   (`specialised-cells`, `levels-of-organisation`) are one card in
   `r_endmatter`, headed by `connects_heading`. All three links live in it, the
   forward one first, under "Connects to" — b3-01 and b4-01 resolved the
   identical layout the identical way. The heading "Next in this unit" is what
   is given up; no link is.

4. **`ks4_links` gives way to `ks4_becomes`.** Design's third endmatter card is
   authored prose and §4.8.1 D makes the two mutually exclusive.

5. **The legal line's two mono spans render as body text.** Design sets
   `b5-male-system-labelled` and `b5-female-system-labelled` in mono inside the
   sentence; a foot line is escaped, so the ids render in body copy. The words
   are unchanged. Same resolution as b4-01.

⚑ For Mide's science gate — NOTES-B5 flags landing on THIS lesson:
  * flag 1 — ~1 million immature egg cells at birth, ~400 maturing in a
    lifetime. In the hook, in the second confrontation and in the `#s-pair`
    table. Sources give 1–2 million for the birth figure.
  * flag 2 — "around a thousand sperm per second" (~1500/s is the usual
    figure). In the hook and in job row 1.
  * flag 4 — fertilisation in the oviduct, with *fallopian tube* as the
    parenthetical. The structure's `name` is the only place the second term
    appears.
  * flag 10 — the testes at ~34 °C, and the undescended testis corrected
    surgically in infancy. The whole stretch layer.
  * flag 11 — the penis described as also carrying urine, through the urethra.
  * flag 12 — glandular fluid containing sugar for the sperm to respire.
    Rung 4 is built on it.
  * flag 13 — `b5-male-system-labelled` and `b5-female-system-labelled` are
    named in Design's legal line and are in no manifest. Declared here at
    `status: "needed"` (§4.10, not a build blocker) so they are tracked
    sourcing tasks rather than dangling references. Nothing is invented to fill
    them, and the captions describe only what this lesson teaches.

⚑ Two places Design's page and this brief's tone rule disagree, PAGE WINS:
  1. **The legal line is second person** — "your RSE and PSHE lessons", "a
     worry about yourself", "your school nurse". The brief says third person
     throughout, never "your". This is safeguarding copy and it is carried
     EXACTLY; a signpost to help that does not address the reader is not a
     signpost. Reported, not altered.
  2. **Two teaching sentences address the reader.** The oviduct's `why` says
     *"this is the structure the reveal warned you about"* and the first
     confrontation ends *"will cost you marks"*. Both are about answering an
     exam question, not about the reader's body, which is where the unit's
     third-person rule actually bites. Lifted unchanged.

⚑ One rendering flag of my own: Design's `why` on the ovaries and her rung 2
  feedback both use Markdown emphasis — *contain* / *make*, *matures and is
  released* — inside strings her own page prints as plain text, so the asterisks
  are visible on the approved screen. `rich()` would take `<em>`, but converting
  them would be an edit to delivered copy. Lifted with the asterisks. Mide's
  call whether Design re-cuts them as `<em>`.
"""

# ── the nine functions (page lines 325–335, via extract_design_payload.js) ──
#
# ⚠️ This is a POOL, not a per-structure list. Each structure offers four of
# these nine and the other three in each pool are the correct functions of other
# structures — see the docstring. Editing a pool to make an item "more wrong"
# destroys the instrument.
FUNCTIONS = [
    {"id": "make-sperm",     "text": "Makes sperm cells"},
    {"id": "make-eggs",      "text": "Makes and releases egg cells"},
    {"id": "carry",          "text": "Carries gametes from where they are made"},
    {"id": "add-fluid",      "text": "Adds fluid that gametes can swim in"},
    {"id": "transfer",       "text": "Transfers gametes into the other system"},
    {"id": "receive",        "text": "Receives gametes and leads towards the egg"},
    {"id": "fertilise-site", "text": "The place where sperm and egg meet"},
    {"id": "hold",           "text": "Holds and supplies a developing embryo"},
    {"id": "close",
     "text": "Closes the lower end of the uterus and opens for birth"},
]

# ── the eight structures (page lines 337–370) ───────────────────────────
#
# `label` is the tab face and `name` is the panel heading: they differ on
# exactly one row, the oviduct, where the panel carries the second term
# (NOTES-B5 flag 4). Both are authored rather than derived for that reason.
STRUCTURES = [
    {"id": "testes", "label": "Testes", "name": "Testes",
     "system": "Male system", "func": "make-sperm",
     "answer": "They make sperm cells — continuously, from puberty onwards.",
     "why": "The direct counterpart of the ovaries: both are gamete-making "
            "organs. This is the one place where the two systems really do "
            "pair up.",
     "options": ["make-sperm", "carry", "add-fluid", "transfer"]},

    {"id": "spermduct", "label": "Sperm duct", "name": "Sperm duct",
     "system": "Male system", "func": "carry",
     "answer": "It carries sperm from the testes towards the urethra.",
     "why": "A transport tube and nothing more. Sperm are made in the testes "
            "and are not made anywhere along this tube.",
     "options": ["make-sperm", "carry", "hold", "fertilise-site"]},

    {"id": "glands", "label": "Glands", "name": "Glands",
     "system": "Male system", "func": "add-fluid",
     "answer": "They add fluid, which together with the sperm makes semen.",
     "why": "The fluid does two jobs: it lets the sperm swim, and it supplies "
            "them with sugar to respire. Sperm on their own cannot travel.",
     "options": ["add-fluid", "make-sperm", "close", "receive"]},

    {"id": "penis", "label": "Penis", "name": "Penis",
     "system": "Male system", "func": "transfer",
     "answer": "It transfers semen into the vagina.",
     "why": "Also carries urine out of the body through the same tube, the "
            "urethra — the one structure in either system with a job outside "
            "reproduction.",
     "options": ["transfer", "add-fluid", "carry", "receive"]},

    {"id": "ovaries", "label": "Ovaries", "name": "Ovaries",
     "system": "Female system", "func": "make-eggs",
     "answer": "They contain the egg cells and release one about every month.",
     # ⚑ The asterisks are Design's and her page prints them literally. See the
     # docstring's rendering flag; they are not converted here.
     "why": "Note the wording: they *contain* rather than *make*. All the "
            "immature egg cells were present before birth. The ovary matures "
            "and releases them; it does not make new ones.",
     "options": ["make-eggs", "fertilise-site", "hold", "carry"]},

    {"id": "oviduct", "label": "Oviduct", "name": "Oviduct (fallopian tube)",
     "system": "Female system", "func": "fertilise-site",
     "answer": "It carries the egg towards the uterus, and it is where "
               "fertilisation happens.",
     "why": "Two jobs, and this is the structure the reveal warned you about. "
            "Fertilisation does not happen in the uterus — it happens here, "
            "and the fertilised egg then travels on.",
     "options": ["fertilise-site", "hold", "make-eggs", "close"]},

    {"id": "uterus", "label": "Uterus", "name": "Uterus",
     "system": "Female system", "func": "hold",
     "answer": "It holds and supplies the developing embryo for nine months.",
     "why": "A muscular organ with a thick blood-rich lining. Nothing in the "
            "male system corresponds to it, which is the point of the next "
            "section.",
     "options": ["hold", "fertilise-site", "receive", "make-eggs"]},

    {"id": "cervix", "label": "Cervix", "name": "Cervix",
     "system": "Female system", "func": "close",
     "answer": "It closes the lower end of the uterus, and opens during birth.",
     "why": "A ring of muscle. Keeping the uterus closed for nine months is as "
            "much a job as opening it at the end, and the second one takes "
            "hours.",
     "options": ["close", "transfer", "carry", "add-fluid"]},
]

# ── the five jobs (page lines 372–388) ──────────────────────────────────
#
# Three of the five have "No structure." in the male cell, and that repetition
# is the section's whole argument — it is not a gap to be filled or varied.
JOBS_COMPARE = [
    ("Job 1 · Make gametes — shared",
     "Testes, from puberty onwards, at around a thousand sperm per second.",
     "Ovaries — which release, rather than make. All the immature eggs were "
     "there at birth; about four hundred ever mature."),

    ("Job 2 · Deliver gametes — shared, but differently",
     "Sperm duct, glands and penis: transport out, fluid to swim in, and "
     "transfer.",
     "Oviduct: the egg is moved along it by cilia and muscle towards the "
     "sperm. It travels a few centimetres, not the sperm’s several inches."),

    ("Job 3 · Receive a gamete — female only",
     "No structure. The male system has no equivalent, because it never "
     "receives anything.",
     "Vagina and cervix, leading to the oviduct where fertilisation takes "
     "place."),

    ("Job 4 · Protect a developing embryo — female only",
     "No structure.",
     "Uterus — muscular walls, a blood-rich lining, and a cervix that stays "
     "shut."),

    ("Job 5 · Supply a developing embryo — female only",
     "No structure.",
     "The placenta, grown for the purpose and discarded afterwards. It is the "
     "only organ a human body builds and then throws away."),
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 122 character for character.
    "slug":        "human-reproductive-systems",
    "title":       "Human reproductive systems",
    "discipline":  "biology",
    "unit":        "reproduction",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # The `a` clause of the split bullet — the structure and function of the two
    # systems. See the docstring; `b` to `e` belong to lessons 2 to 5.
    "covers":      ["KS3.B.REP.01a"],
    # Named but not taught. Fertilisation is the oviduct's job and the next
    # lesson's subject; the placenta is job row 5 and lesson 4's subject; rung 4
    # leans on respiration (B8) and on the sperm cell as a specialised cell,
    # which the student met in B1's diffusion and organisation lessons.
    "touches":     ["KS3.B.REP.01b", "KS3.B.RESP.01", "KS3.B.CELLS.06"],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 2},
                    {"id": "structure-function", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # No `requires`: Design draws no "Before this lesson" card, this is the
    # unit's first lesson, and the engine omits an empty card. All three of her
    # forward and sideways links live in the middle card — see "What could not
    # be lifted" 3.
    "requires":    [],
    "assumes":     [],
    "references":  ["gametes-and-fertilisation",
                    {"unit": "B1", "lesson": "specialised-cells"},
                    {"unit": "B1", "lesson": "levels-of-organisation"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Hormonal control of reproduction, fertility treatment, and "
                   "contraception.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Two organ systems with one shared purpose and almost "
                    "nothing else in common. Learning the names is the easy "
                    "part; the useful question is what each structure is for.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-pair` is the third: no control of
    # its own, so it mirrors `s-jobs` and ticks on the instrument's predicate —
    # see the docstring. `short` and `label` are Design's own `RAIL_SHORT` and
    # `RAIL` strings (page lines 317–323).
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "A million eggs",
         "done_when": "committed"},
        # Design's own threshold, kept: the stage ticks when all eight
        # structures have been CHECKED, not when the first one is picked. A
        # stop that ticked on the first check would call the instrument
        # finished at an eighth of it.
        {"anchor": "s-jobs", "short": "MATCH", "label": "Match the job",
         "done_when": "all_eight_checked"},
        {"anchor": "s-pair", "short": "PAIR", "label": "Not mirrors",
         "mirrors": "s-jobs", "done_when": "all_eight_checked"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3).
    "phenomenon": {
        "kind": "narrative",
        "title": "Every egg cell a person will ever have was already made "
                 "before they were born.",
        "prompt": "About a million immature egg cells are present in the "
                  "ovaries of a newborn baby. No more are ever made. Sperm "
                  "cells, by contrast, are produced continuously from puberty "
                  "onwards, at something like a thousand per second.",
        "commit": "Two systems with the same purpose. Why such different "
                  "strategies?",
        "options": [
            "One system is more efficient than the other",
            "The two gametes have very different jobs, so they cost very "
            "different amounts to make",
            "Egg cells last longer, so fewer are needed",
            "It is a coincidence with no biological reason",
        ],
        "reveal": "Because the two gametes are doing different jobs. An egg "
                  "carries everything a new organism needs to start with — "
                  "food store, machinery, half the instructions — so it is "
                  "large, expensive, and made in small numbers. A sperm "
                  "carries half the instructions and a tail, so it is tiny, "
                  "cheap, and made in enormous numbers. The whole design of "
                  "both systems follows from that one difference.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ `REPRO-01` and `REPRO-02` are this lesson's allocation and it takes no
    # other number: five parallel authors collided on B4's family and the
    # `REPRO` range was pre-allocated for that reason. NOTES-B5 §5 mints
    # seventeen for the unit; the register itself carries none of them yet and
    # the commander maintains it centrally.
    #
    # The page confronts exactly two beliefs and both are here. A third — that
    # fertilisation happens in the uterus — appears as rung 1's first
    # distractor rather than as a confrontation, and NOTES-B5 flag 4 assigns it
    # to `REPRO-03`, owned by `gametes-and-fertilisation`. It is deliberately
    # NOT declared here: two lessons declaring one id is the collision the
    # allocation exists to prevent.
    #
    # `elicited_by` is honest per entry. The instrument really does surface 01:
    # every option pool mixes both systems' functions, so a student who expects
    # a mirror image mis-assigns before anything corrects them. 02 is not asked
    # for anywhere before the block that kills it, so the block is named for
    # both — b3-04 and b4-01 use the same pattern.
    "misconceptions": [
        {"id": "REPRO-01",
         # Byte-identical to Design's quote, so the register entry and the page
         # cannot drift apart — b1-01 shipped a block where they had.
         "statement": "The two systems are mirror images — every part has a "
                      "matching part in the other.",
         "elicited_by": "match-the-job",
         "confronted_by": "think-not-mirrors"},
        {"id": "REPRO-02",
         "statement": "Egg cells are made all the time, like sperm cells.",
         "elicited_by": "think-not-mirrors",
         "confronted_by": "think-not-mirrors"},
    ],

    # Design draws no keyword block anywhere in B5, so these never reach the
    # lesson body. The TERMS reach a student as the unit page's chips, and the
    # reading-age gate reads them as its exclusion list — which matters here,
    # because "oviduct", "cervix", "uterus" and "gamete" would otherwise all
    # count against the page. Each definition is the page's own answer line for
    # that structure, cut to a definition; nothing new is claimed.
    "vocabulary": [
        {"term": "gamete",
         "definition": "A sex cell — a sperm cell or an egg cell.",
         "note": "Sperm are made continuously from puberty; all the immature "
                 "egg cells are present at birth."},
        {"term": "testes",
         "definition": "The organs that make sperm cells, continuously, from "
                       "puberty onwards.",
         "note": None},
        {"term": "sperm duct",
         "definition": "The tube that carries sperm from the testes towards "
                       "the urethra.",
         "note": "A transport tube and nothing more."},
        {"term": "semen",
         "definition": "Sperm cells together with the fluid added by the "
                       "glands.",
         "note": "The fluid lets the sperm swim and supplies them with sugar "
                 "to respire."},
        {"term": "ovaries",
         "definition": "The organs that contain the egg cells and release one "
                       "about every month.",
         "note": "They contain rather than make: the stock was complete "
                 "before birth."},
        {"term": "oviduct",
         "definition": "The tube that carries the egg towards the uterus, and "
                       "where fertilisation happens.",
         "note": "Also called the fallopian tube."},
        {"term": "uterus",
         "definition": "The muscular organ that holds and supplies the "
                       "developing embryo for nine months.",
         "note": "Nothing in the male system corresponds to it."},
        {"term": "cervix",
         "definition": "The ring of muscle that closes the lower end of the "
                       "uterus, and opens during birth.",
         "note": None},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # Design's legal line names BOTH slots and no artwork exists for either, so
    # they are DECLARED at `needed` rather than dropped: the manifest is
    # generated from this field, which turns two dangling references into two
    # tracked sourcing tasks. `needed` is not a build blocker. No `figure` block
    # is added to `core` — Design draws no figure slot on the page, and one
    # here would be a component nobody drew. NOTES-B5 flag 13 asks Mide to
    # confirm what is illustrated and at what level of detail BEFORE anything
    # is commissioned; the captions below name only the structures this lesson
    # teaches, in the page's own order and words.
    "figures": [
        {"id": "b5-male-system-labelled",
         "kind": "diagram",
         "caption": "The male reproductive system, labelled: the testes, the "
                    "sperm duct, the glands that add fluid, the urethra and "
                    "the penis.",
         "status": "needed"},
        {"id": "b5-female-system-labelled",
         "kind": "diagram",
         "caption": "The female reproductive system, labelled: the ovaries, "
                    "the oviducts, the uterus, the cervix and the vagina.",
         "status": "needed"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-jobs — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b5/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 104), so the segment is measured and not inherited.
        #
        # ⚠️ INK-DARK. `.ks3-dark p` is (0,1,1) and beats a bare instrument
        # class at (0,1,0); every text rule in this instrument has to be scoped
        # to at least (0,2,0) or it ships invisible past a green kinds gate.
        # That is an engine note, recorded here because the block is authored
        # here — see ks3_data/b5/__init__.py.
        {"type": "job-match", "id": "match-the-job", "anchor": "s-jobs",
         "demand": "investigate",
         "targets": "REPRO-01",
         "eyebrow": "Match the job · eight structures",
         "heading": "What is each one actually for?",
         "head_counter": {"format": "{n} of 8 checked", "total": 8},
         "prompt": "Pick a structure, then choose the function that belongs to "
                   "it. Only one structure has more than one job, and the "
                   "reveal says which.",

         "functions": FUNCTIONS,
         "structures": STRUCTURES,

         # The mono label over the option list, and the control that buys the
         # answer. `check_label` is the only words the button has.
         "options_label": "Which function belongs to it?",
         "check_label": "Check it",
         # The mono line beside the button, in its three states — Design's
         # `openHint` (page line 535).
         "hints": {"empty": "choose a function first",
                   "ready": "ready",
                   "checked": "checked"},
         # ⚠️ NOT a verdict on the student in the R3 sense: it names whether the
         # function they chose is that structure's function, which is the
         # instrument's entire output. Design's `structVerdict` (page line 538).
         "verdicts": {"right": "Correct", "wrong": "Not that one"}},

        # #s-pair — the band panel with the five jobs. Rail stop 3, mirroring
        # `s-jobs`; see the docstring. `comparison` is the component: band ground, 3px ink
        # border, accent-text eyebrow, display statement, two captioned
        # columns, zebra rows and a nested key fact — Design's markup (page
        # lines 153–180) element for element, minus the lede.
        {"type": "comparison", "anchor": "s-pair",
         "eyebrow": "Not mirror images",
         "eyebrow_tone": "accent-text",
         "statement": "Five jobs, and only two of them are shared.",
         "ground": "band",
         "columns": [
             {"caption": "Male system", "tone": "on-dark"},
             {"caption": "Female system", "tone": "on-dark"},
         ],
         # Design paints both cells at the same weight and colour — neither
         # system is the quiet one, which is the point of the row.
         "row_tones": ["ink", "ink"],
         "rows": [{"name": job, "cells": [male, female]}
                  for job, male, female in JOBS_COMPARE],
         # Design nests the box inside the panel, on the card ground with the
         # accent offset shadow. `r_comparison` is the one block with a nested
         # key-fact slot, so this renders exactly where she drew it.
         "key_fact": {"ref": "two-shared-three-not", "ground": "card"}},

        {"type": "misconception", "id": "think-not-mirrors",
         "anchor": "s-think", "targets": ["REPRO-01", "REPRO-02"]},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # One per lesson, nested in the comparison above. Never amber (MRB-208).
    "key_facts": [
        {"id": "two-shared-three-not",
         "text": "Both systems make gametes and both deliver them. Only the "
                 "female system also receives a gamete, protects a developing "
                 "embryo and supplies it for nine months — which is why it "
                 "has structures the male system has no equivalent of at all.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # One entry beyond the flagship, which is authored inline in `core` and
    # lifted here by `ks3_data/b5/__init__.py::_normalise`.
    "activities": [
        # Design's `#s-think` is STATIC on this page — two quotes and two
        # paragraphs, the second behind an amber-topped divider, with nothing
        # to answer. That is measured off the markup and not assumed: the
        # section contains no `ks3-options`, no commit and no reveal. So it is
        # a `confrontation`, it is not a rail stop, and it emits no
        # `data-stage-done` — a section that asks for nothing can never
        # discharge a completion contract. MRB-220 R1 (which makes `#s-think` a
        # `predict`) is scoped to pages whose `#s-think` demands a commitment;
        # this one does not.
        #
        # An authored statement wins over the register (build_ks3.py:2504),
        # which is what keeps Design's wording rather than a paraphrase.
        {"id": "think-not-mirrors",
         "kind": "confrontation",
         "demand": "explain",
         "targets": ["REPRO-01", "REPRO-02"],
         "statements": [
             {"quote": "The two systems are mirror images — every part has a "
                       "matching part in the other.",
              "body": ["They are not, and expecting them to be is what makes "
                       "this topic hard to hold on to. There is a rough "
                       "pairing at one point only: testes and ovaries both "
                       "make gametes, and both are the same kind of organ "
                       "doing the same kind of job. After that the lists "
                       "diverge completely. The female system contains a "
                       "uterus, and nothing in the male system corresponds to "
                       "it, because no male structure has to hold and supply "
                       "another organism for nine months. The male system "
                       "contains structures whose whole purpose is "
                       "transferring gametes out, and the female system's "
                       "equivalent problem is entirely different: getting a "
                       "gamete <em>towards</em> another one. Learning the two "
                       "lists as parallel columns will cost you marks; "
                       "learning them as two solutions to two different "
                       "halves of one problem will not."]},
             {"quote": "Egg cells are made all the time, like sperm cells.",
              "body": ["The numbers are worth sitting with. All the immature "
                       "egg cells a person will ever have — around a million "
                       "— are present in the ovaries at birth, and the count "
                       "only ever falls from there; roughly four hundred will "
                       "complete maturing and be released across a lifetime. "
                       "Sperm production is the opposite in every respect: it "
                       "begins at puberty, continues indefinitely, and runs "
                       "at hundreds of millions a day. This is not a detail "
                       "about timing. It is the reason age affects the two "
                       "systems so differently, and it is the reason the "
                       "ovary is the organ that runs out."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⚖️ MRB-177 LENGTH PARITY — MEASURED, AND BOTH MARKED RUNGS PASS.
    #   rung 1: correct 3w against distractors of 3 / 3 / 3 — every option is
    #           the same shape, so length is no tell.
    #   rung 2: correct 10w against distractors of 8 / 11 / 11 — the correct
    #           option is not the longest.
    # No distractor was rewritten, because there was nothing to repair.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Where does it happen",
            "q": "Where does fertilisation take place?",
            "options": [
                "In the uterus",
                "In the oviduct",
                "In the ovary",
                "In the cervix",
            ],
            "answer": 1,
            "feedback": {
                0: "A very common answer and it is wrong. The uterus is where "
                   "the already-fertilised egg implants and develops — "
                   "fertilisation happens further up.",
                2: "The egg is released from the ovary before it can meet a "
                   "sperm. Fertilisation in the ovary would be a serious "
                   "medical emergency.",
                3: "The cervix is a muscular ring the sperm pass through. "
                   "Nothing meets there.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "Which statement about egg cells is correct?",
            "options": [
                "They are made continuously from puberty, like sperm",
                "All the immature egg cells are already present at birth",
                "A new egg cell is made each month by the ovary",
                "They are made in the oviduct and stored in the ovary",
            ],
            "answer": 1,
            "feedback": {
                0: "This is the sperm pattern applied to eggs. The two systems "
                   "differ here more sharply than anywhere else.",
                # ⚑ Design's asterisks, printed literally on her own page. See
                # the docstring's rendering flag.
                2: "One egg *matures and is released* each month, from a stock "
                   "that was complete before birth. Released is not the same "
                   "as made.",
                3: "Nothing is made in the oviduct. It is a transport tube and "
                   "the site of fertilisation.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the asymmetry",
            "q": "The female system has structures the male system has no "
                 "equivalent of. Explain which they are and why, using the "
                 "five jobs. Do not describe the two systems as opposites.",
            "field_label": "Your explanation",
            "placeholder": "Both systems make gametes, but…",
            "success": [
                "Identifies making and delivering gametes as the two shared "
                "jobs.",
                "Names the uterus, and says nothing in the male system "
                "corresponds to it.",
                "Explains why: only the female system holds and supplies a "
                "developing embryo.",
                "Notes that testes and ovaries are the one genuine pairing "
                "between the two systems.",
                "Avoids treating the systems as mirror images or as opposites.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "The fluid added by the glands contains sugar. Using what you "
                 "know about respiration and about specialised cells, explain "
                 "why, and predict what would happen to a sperm cell placed in "
                 "pure water instead.",
            "field_label": "Your answer",
            "placeholder": "The sugar is there because…",
            "success": [
                "Says the sugar is respired by the sperm to release energy for "
                "swimming.",
                "Links this to the sperm cell’s many mitochondria — a "
                "specialised cell built for one job.",
                "Predicts that in pure water a sperm would soon run out of "
                "usable fuel and stop swimming.",
                "Notes that the sperm carries almost no food store of its own, "
                "unlike the egg.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "The testes make sperm; the sperm duct carries them and the "
                "glands add fluid to make semen; the penis transfers semen "
                "into the vagina. The ovaries make and release egg cells; the "
                "oviduct carries the egg towards the uterus and is where "
                "fertilisation happens; the uterus holds and supplies a "
                "developing embryo; the cervix is its lower opening. All "
                "immature egg cells are present at birth; sperm are made "
                "continuously from puberty.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # NOTES-B5 flag 10 lands here: the 34 °C figure, and the undescended testis
    # named as a condition corrected surgically in infancy.
    "stretch": [
        {"type": "explainer", "id": "why-they-sit-outside",
         "text": "The testes sit outside the body cavity, which looks like "
                 "poor design until you measure the temperature. Sperm "
                 "production works best a few degrees below core body "
                 "temperature, around 34 °C, and fails at 37 °C — so the organ "
                 "is held outside where it can run cool, with a muscle that "
                 "raises it towards the body in cold conditions and lets it "
                 "hang further away in warm ones. It is a "
                 "temperature-regulation system, and it explains a clinical "
                 "detail: a testis that fails to descend before birth will not "
                 "produce sperm if it is left in the abdomen, which is why the "
                 "condition is corrected surgically in infancy. Whales and "
                 "elephants, awkwardly for the theory, keep theirs internal "
                 "and cool them with blood returning from the skin instead. "
                 "The problem is real; there is more than one solution to it."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check which structure does which job?",
              "cta": "Ask about this lesson",
              "anchor": "s-jobs"},

    # ⊕ MRB-228's `convention_note`, not `safety_note`. MEASURED: Design draws
    # ONE plain `.ks3-legal` paragraph (page line 306) with no `ks3-safety`
    # modifier, and nothing in it is a safety instruction — it is a scope note
    # about what this lesson is and is not, a signpost to the people who own
    # the rest, and a declaration about two diagrams that have not been drawn.
    # Routing it through `safety_note` would print it in the treatment reserved
    # for "never light a candle without an adult", which is a different kind of
    # sentence and would devalue both.
    #
    # ⚠️ CARRIED WHOLE AND UNALTERED. This is safeguarding copy on the unit
    # where tone is a gate. Its second person is Design's and is deliberate —
    # see the docstring's second tone flag. The two figure ids keep their plain
    # text; Design sets them in mono inside the sentence and a foot line is
    # escaped, so they render in body copy and the words are unchanged.
    "convention_note": "This is the biology: the structures and what each one "
                       "does. Relationships, consent and staying safe are "
                       "covered in your RSE and PSHE lessons, and those "
                       "lessons are where questions about them belong. If "
                       "anything here raises a question or a worry about "
                       "yourself, a trusted adult, your school nurse or a "
                       "doctor is the right person to ask. The labelled "
                       "diagrams are declared in the lesson records as "
                       "b5-male-system-labelled and b5-female-system-labelled, "
                       "awaiting illustration.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The instrument is commit-then-check against a shared pool of functions:
    # the student assigns a structure to a job and then reads whether the
    # evidence supports the assignment. No measurement is taken anywhere on
    # this page, so `measurement` and `experimental-skills` would both be
    # claims the lesson does not earn.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
