"""B11 L4 — Biodiversity and gene banks (SYSTEM). The last lesson of KS3 Biology.

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b11/b11-04-biodiversity-and-gene-banks.dc.html`
(559 lines), her author's notes `docs/ks3/design-reference/b11/NOTES-B11.md` §2
flags 12–15, and the B11 payload schema
`docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md` §0, §1, §5, §6, §7, §8, §9, §11, §12,
§13 and §14, under the MRB-220 build contract.

Every student-facing string is lifted byte-identical from the approved page
except the four listed under "What could not be lifted". The four fields, the
four bank cards, both marked rungs and both self-marked rungs came out of the
page's own `FIELDS`, `BANK_CARDS`, `RUNGS` and `SELF_RUNGS` arrays via
`node tools/extract_design_payload.js`, not off a keyboard. No option, verdict,
correction, criterion or bar figure was retyped.

── `covers` is one clause and this lesson owns the whole of it ─────────

`KS3.B.INH.07` reads, in full: *the importance of maintaining biodiversity and
the use of gene banks to preserve hereditary material*
(`docs/ks3/statutory-register.md` line 187). It has two halves and the page has
two answers — `#s-hook` and `#s-bench` are the importance, argued rather than
asserted, and `#s-banks` is the four methods with what each one cannot do. It is
not sub-split in `ks3_data/substatements.py`, so it is owned whole. INH.05a and
b are b11-01's and b11-02's, INH.06 is b11-03's; this record `touches` INH.05
and INH.06 and owns neither.

── ⚖️ THE LESSON IS THAT VARIATION IS WHAT A POPULATION HAS INSTEAD OF A PLAN ─

The bench is an argument in three bars and the middle one is the point: variation
runs 9 → 36 → 90 → 100 while yield per plant runs 100 → 85 → 85 → 55. **The
trade-off that makes a monoculture attractive is drawn rather than asserted**,
which is why the clone field is allowed to be genuinely best at something. A
student who has only been told monoculture is bad has learned a slogan; a student
who has watched the yield bar fall as the variation bar rises has learned the
decision a farmer actually faces.

⛔ **The clone field returns EXACTLY ZERO** — `resistant: 0` over `varieties: 1`
is zero by construction, not by rounding, and there is no arithmetic path to a
single survivor (schema §5). That number is the payoff of the whole page and it
must stay integer-exact. Nothing else on the bench is allowed to soften it: the
verdict says *Nothing survives. Not one plant in a thousand*.

── ⚑ FLAG 13 — THE IRISH POTATO FAMINE. THE CLAUSE WAS CHECKED AND CHANGED ──

Schema §14 rules the shape (one clause, about the crop, no politics) and requires
the b11-04 author to check what the delivered clause actually SAYS. Checked, and
it did not pass the test §14 sets. Design's clone verdict, verbatim:

    Design:  This is the Irish potato famine of the 1840s in miniature, and it
             is the shape of the Gros Michel banana as well.
    Built:   This is what happened to Ireland's potato crop in the 1840s, in
             miniature, and it is the shape of the Gros Michel banana as well.

The thing the sentence points at — `This` — is a field of a thousand dead potato
plants. Calling that field *the famine in miniature* says the famine WAS a
destroyed potato crop, scaled up, which is the false causal story §14 names: the
blight destroyed the crop, and what followed, roughly a million deaths and a
million more emigrating, followed from far more than a fungus. The repair moves
the referent from the famine to the crop and changes nothing else — same length,
same position, same clause count, the Gros Michel half untouched. **The politics
are NOT added**; §14 is explicit that expanding into them is the other failure
mode and that this is a science lesson.

── The instrument: three bars, and two of them run opposite ────────────

`#s-bench` is `blight-bench`, on `ks3-block ks3-dark ks3-practical` (page line
104), so `practical` is MEASURED from Design's own class attribute rather than
inferred from the kind name — schema §0 rule 3, and contract §4 records that B1
got two of six wrong by inferring it.

⚖️ **`survivors` AND `pct` ARE DERIVED AND MUST NEVER BE AUTHORED.** Design
computes `survivors = round(TOTAL × resistant / varieties)` and
`pct = round(survivors / TOTAL × 100)` once per release, so the four percentages
0 / 25 / 40 / 62 are a consequence of `varieties` and `resistant` rather than
four authored numbers that could drift apart from them. There is no `survivors`
key, no `pct` key and no `percent` key in this record. `verdicts` carries `{pct}`
as a placeholder for the same reason — an authored "25%" would be a second
statement of a number the bench already knows, and the two could disagree.

⚠️ **`variation_word`, `yield_word` and `yield_bar` ARE AUTHORED PER FIELD, and
Design derives them from the field `id`** with a chain of
`f.id === 'clone' ? … : (f.id === 'landrace' ? … : …)`. Schema §5 rules the
departure and gives the reason: a fifth field would fall silently into her `else`
and be drawn as *good / 85*. Same drawn output for these four, portable for any
fifth. `variation_bar` is authored for the same reason — Design's
`min(100, varieties × 9)` is a formula that happens to fit four cases.

⚠️ **`verdicts` IS KEYED BY FIELD ID, ALL FOUR WRITTEN OUT**, though Design has
three branches. `four` and `ten` carry IDENTICAL template text — schema §5 calls
that a deliberate duplication and not drift, and the two fields already print
different sentences because `{pct}` resolves to 25 and 40.

⛔ **NO RUNTIME STATE IS AUTHORED** (schema §0 rule 4). Design's state bag holds
`field`, `released` and `tried`; all three are the runtime's. Nor is an opening
selection authored: her `field` opens on `clone`, and `clone` IS `fields[0]`, so
the renderer's default of index 0 already ships Design's page.

── FOUR rail stops, and the third is a MIRROR (MRB-249) ────────────────

Design draws four (page lines 296–301) and her `isDone()` gives `s-banks` the
BENCH's predicate, character for character, one line below:

    if (id === 's-bench') return n >= 2;
    if (id === 's-banks') return n >= 2;          // page lines 386–387

`#s-banks` is an eyebrow, a display statement, four static cards and a key fact:
no control, no commitment, no field, no reveal. It is the PAYOFF of the bench
beside it and carries no control precisely because the bench has already taken
the student's commitment. That relationship is a MIRROR, `wireRail`'s `paint()`
resolves it at rail level — which is the level Design computes it at — and
`ks3_parity.check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md`, whose row for this page reads
`s-hook s-bench s-banks s-ladder | s-banks=s-bench`.

⚠️ Schema §8's struck verdict — *author three stops and drop the band* — is
REVERSED at the head of the same section by the ⊕ block. Four is what Design drew
and four is what ships. Shipping three fails the build.

⚖️ **TWO FIELDS BLIGHTED IS DESIGN'S OWN THRESHOLD AND IT IS READ TWICE**, once
for the bench and once for the mirror. `tried` is a set that is only ever added
to — `Clear the field` clears `released` and keeps `tried` — so the stop is
sticky by her design and monotonic by ours. Two of four is also the point at
which a student has necessarily compared a field against another field, which is
the only way the trade-off is visible at all.

`#s-think` and `#s-keynote` are on no rail, and that is Design's too:
`#s-keynote` asks nothing, and `#s-think` here is static markup — two quotes, two
bodies, no options, no reveal, no button — so it is a `confrontation` and not
contract R1's `predict`. Schema §7, measured on all four pages.

── What could not be lifted byte-identical, and why ────────────────────

1. **`b11-02` AS HYPERLINK TEXT IN THE HOOK'S REVEAL.** Design writes *"…which is
   the whole mechanism from `<a href="b11-02-natural-selection.html">b11-02</a>`
   removed at a stroke."* `rich()` allows `<em>` and `<strong>` and nothing else,
   so no anchor survives anywhere on the page — and here the link TEXT is a slot
   code, which a student cannot resolve and which is exactly the platform leakage
   §8.10 exists to stop. Resolved to the lesson TITLE, the way b9-02, b9-03 and
   b10-01 resolved the identical shape:

       Design:  the whole mechanism from b11-02 removed at a stroke
       Built:   the whole mechanism from Natural selection removed at a stroke

   The destination is not lost — `natural-selection` is Design's own second
   *Before this lesson* card and is carried in `requires`.

2. **`the last lesson` IN THE FIRST CONFRONTATION — a POSITIONAL reference behind
   a stripped link.** Design writes *"…risk factor four in
   `<a href="b11-03-…">the last lesson</a>`."* Dropping the tag would leave a
   student reading *risk factor four in the last lesson* with nothing to follow
   and an ordering claim a school's own scheme may not honour — b9-02's finding,
   and the same repair:

       Design:  risk factor four in the last lesson
       Built:   risk factor four in When the environment changes: extinction

   `when-the-environment-changes-extinction` is carried in `requires`, and it is
   Design's own first *Before this lesson* card.

3. **A `\\u2014` ESCAPE THAT LEAKED INTO THE MARKUP.** Page line 288 ends the
   *Going further* paragraph *"…in one story \\u2014 and also for why the seeds
   have to be regrown…"* — a literal backslash-u-2014 in the HTML body, not in
   the script block. Every other em dash in this page's markup is the character
   itself (the key fact, the keynote, the hook reveal), and every `\\u2014` inside
   the `<script>` is an ordinary JS escape that resolves. This one resolves to
   nothing: a browser would print the six characters. Authored as the em dash
   Design meant. **Reported as a defect in the delivered page rather than fixed
   silently** — and it is the SECOND time this exact leak has been found in a
   delivery, b10-01 having reported the first at its own page line 129.

4. **The clone verdict's famine clause** — flag 13, worked in full above. It is a
   science ruling performed, not a lift that failed.

── ⊕ MRB-177 LENGTH PARITY — RUNG 1 CLEAN, RUNG 2 REPAIRED AT THE DISTRACTORS ─

Measured with `length_tell()` copied out of `verify_ks3.py` (tokens are
`re.findall(r"[^\\s]+", text)`, so an em dash counts as one). The gate flags a
correct option that is strictly the longest AND clears the longest distractor by
≥4 words or by ≥1.4×.

    rung 1  correct  9w vs  8 /  6 /  7  — gap 1, ratio 1.13    ✓ as drawn
    rung 2  correct 23w vs  5 /  9 / 10  — gap 13, ratio 2.30   ✗ TRIPPED (both)
    rung 2  correct 23w vs 18 / 19 / 24  — not strictly longest ✓ repaired

**No correct option was shortened, no `answer` index moved, and no correction was
edited.** The repair is at the three distractors of rung 2 and nowhere else:

    rung 2 option A   5w →  18w   (correct option untouched at 23w)
    rung 2 option C   9w →  19w
    rung 2 option D  10w →  24w

⚖️ **THE REPAIR IS THE CONSTRUCT, NOT THE PADDING.** MRB-177's ruling is that a
distractor on a rule-stating rung states a WRONG RULE in the same three-part
shape — claim, condition, consequence — rather than a one-clause wrong reason.
Design's correct option already had that shape (*the seed can be regrown, BUT the
ecosystem is not in the bank, SO the objection stands*) and her three distractors
were bare assertions with no consequence attached. Each now carries the
consequence its own assertion implies, which is what makes it a rival ANSWER to
the question *what is the strongest objection?* rather than a fragment:

  * **A** — *seeds do not survive freezing* → …*so a stored sample is already
    dead by the time anyone needs it.* The consequence a student who believes it
    would draw. Her correction, untouched, answers exactly this: *many do, which
    is what makes seed banks work.*
  * **C** — *gene banks are too expensive* → …*so the money would always be
    better spent somewhere else.* The correction, untouched, refuses precisely
    that: *cost is not the objection that matters.*
  * **D** — *nobody knows how to plant a seed from a gene bank* → …*so a species
    stored in one could never be brought back at all.* The correction, untouched,
    answers it twice over: *it has been done, repeatedly and successfully. The
    difficulty is what the seedling comes back to, not the planting.*

The outcome is the cleanest of the three available: **the longest option on the
rung is now a DISTRACTOR**, so the correct answer is not strictly longest and a
student who counts words is led AWAY from it. Rung 1 needed nothing — all four
options name a field and nothing else, there is no rule anywhere in the set for a
correct answer to be longer than, and the spread is 6 to 9 words.

── Misconception ids: EVOL-07 and EVOL-08, and EVOL-12 is UNUSED ───────

Schema §12's pre-allocation for b11-04, and the two beliefs Design's `#s-think`
quotes, in her page order. Both statements are her own bytes (page lines 178 and
182), in register voice with the curly quotes stripped — the renderer draws
those.

**Two beliefs were found and two ids were used. `EVOL-12`, this lesson's named
spare, is UNCLAIMED and stays permanently unused**, exactly like `DRUG-07`. It is
never re-pointed at a different belief in a later pass. Schema §12's escalation —
an author needing a SECOND spare stops and reports rather than reaching past the
table — was not reached: no third belief is quoted anywhere on this page.

⊕ **THE `EVOL` PREFIX ROW IS OPEN, AND IT AGREES WITH THIS FILE.** Schema §11
item 5 recorded that NOTES-B11 §4's claim of eight rows "written into" the
register was false when the schema was written, so it was checked rather than
assumed. It was opened during this run (register line 120, prefix row; lines
1037–1044, the eight entries), and re-checked at the end for that reason: that
file is in flight this session and is not this pass's to edit (contract §0). Its
`EVOL-07` and `EVOL-08` rows match the two authored here on statement, on
`elicited_by` and on `confronted_by`, arrived at independently. Nothing to
reconcile.

Both `elicited_by` values are `s-ladder` and both are real elicitations rather
than a default, which is the check the register's `EVOL-06` note demands:

  * `EVOL-07` → rung 1. *Which field has the lowest biodiversity?* offers *a
    field with two species of grass* as option D, and a student who believes
    biodiversity is a species count MUST choose it — two species is fewer than a
    thousand plants. The belief is what makes the wrong answer attractive, and
    the ladder is the only place on the page where it is MARKED.
  * `EVOL-08` → rung 2. The belief is the stem — *a seed bank means a plant
    species can never truly be lost* — and the three distractors are the weak
    objections a student holding it would reach for. Choosing one is holding the
    belief in public.

Both `confronted_by` values are `s-think` and both resolve against the BUILT page
(MRB-244).

── Keys this pass authors that the RENDERER reads (contract R5) ────────

Named explicitly rather than left to be discovered, and every one is schema §5's
spelling rather than this author's:

    tabs_label        the mono label over the four field tabs
    fields            tabs + one panel each, every field carrying `varieties`
                      and `resistant` (which DERIVE the survivor bar),
                      `variation_word` / `variation_bar`, `yield_word` /
                      `yield_bar`, `name` and `note`
    total             the thousand plants — the denominator of every bar
    bar_labels        the three bar names, in Design's order
    run_label /       the release button before and after
    ran_label
    reset_label       `Clear the field` — authored, because Design DRAWS it
                      (page line 143) and it is never disabled
    verdicts          the cream panel under the bars, keyed by field id
    progress_suffix / the head-row counter and its resting state
    progress_zero
    eyebrow /         the practical shell's head row
    title / intro

⚠️ **`blight-bench` IS NOT YET REGISTERED IN `ACTIVITY_KIND_RENDERERS`** — the
engine pass holds `build_ks3.py`, `shared/ks3.css`, `shared/ks3.js`,
`ks3_parity.py` and the coverage manifest, and is mid-flight as this record
lands. That is expected and no renderer is added here (contract §0). Until it
registers, `ks3_key_audit.py B11` will report this payload's keys as unread; the
keys are schema §5's, named above, and the engine pass is authoring against the
same section.

── figures: [] and MEASURED ───────────────────────────────────────────

`<img>`, `<figure>` and `<picture>` each appear ZERO times on this page —
grepped, not assumed — and every `<svg>` is the nav chevron, a rail tick, a
ladder mark or an endmatter arrow. Schema §13 says the same across all four B11
pages. The unit's one ruled diagram is NOTES flag 16's peppered-moth pair, which
is b11-02's and is drawn there; nothing in THIS lesson is spatial — the argument
is three bars whose lengths disagree with each other, and the bench draws them
out of DOM.

── ⚑ For Mide's science gate — every NOTES-B11 flag landing on THIS lesson ─

Four flags, four checked, **one corrected** (flag 13, above). Schema §14 already
ruled all four under this run's standing authority; none is re-opened here, and
the three below are recorded as checked rather than re-derived.

  * flag 12  **Gros Michel and Cavendish, and the current Panama disease strain
             moving through Cavendish plantations.** Ruled right and current
             (§14). Ships as drawn, in the hook, and it is the case that makes
             the lesson contemporary rather than historical.
  * flag 14  **Svalbard** — about 1,300 km from the North Pole, well over a
             million samples, minus eighteen degrees, permafrost backup, and the
             Aleppo/ICARDA withdrawal and return. Ruled right (§14), and *"well
             over a million"* is the correct hedge for a holding that grows: a
             precise number would date the page. The Aleppo story is real and is
             the whole argument for gene banks in one paragraph. Ships as drawn.
  * flag 15  **Landrace resistance at 62%.** Invented, ruled chosen well (§14) —
             it beats the ten-variety field clearly without reading as immunity —
             and the legal line covers it: *"The blight bench is a teaching
             model…"*. Ships as drawn, and the number is carried as
             `resistant: 620` over `varieties: 1000` so that the bench derives
             the 62% rather than being told it.

── One phrase a later pass might read as a sequence leak, and should not ─

`Year 7`, `Year 8`, `Year 9` and `half-term` appear ZERO times in this record —
checked rather than assumed, and now gated in `verify_ks3.py`. The word `year`
appears only lowercase and only as a duration or a growing season: *yield per
plant in a good year*, *next year every one of those survivors*, *the yield in
the year of a blight*. The 1840s and the 1950s are historical dates the science
needs, which §14 confirms are content.

── MRB-225, checked across the whole lesson: NO body sentence is retracted ─

Traced the claim the lesson makes: *variation is what allows a population to
survive a change, and a gene bank stores the variation but not the world it lived
in*. The hook's reveal, all four verdicts, both `#s-think` bodies, the key fact,
rung 2's correct option, rung 3's fifth criterion, the key note and every one of
the four bank cards' limit sentences say it at the same size. The *Going further*
layer adds Svalbard and retracts nothing: the Aleppo withdrawal is the insurance
policy being claimed on, and its last clause — that the seeds have to be regrown
rather than simply left in a freezer — is the same limitation the second
confrontation already states.
"""


# ── the four fields (page lines 331–340) ─────────────────────────────────
#
# In Design's order, and THE ORDER IS THE ARGUMENT: `clone` is `fields[0]` and
# therefore the field the page opens on — the one with the highest yield and no
# survivors at all — and every field after it trades yield away for variation.
# The student meets the trade-off in the direction a farmer meets it.
#
# ⛔ `varieties` AND `resistant` ARE NOT LABELS. Together they decide the
# survivor count and the percentage in every verdict, so a wrong pair would draw
# a plausible graph and print a wrong number under it. `resistant: 0` over
# `varieties: 1` is the zero the whole lesson turns on.
#
# ⚠️ `variation_word`, `variation_bar`, `yield_word` and `yield_bar` are authored
# rather than derived — schema §5, and the reason is in the docstring. The values
# are Design's own drawn output, measured: variation 9 / 36 / 90 / 100 against
# yield 100 / 85 / 85 / 55, monotone opposite at the two ends with `four` and
# `ten` deliberately TIED at 85 in the middle. The trade-off bites at the
# extremes, not smoothly across the range, and a later pass smoothing the middle
# would be inventing a claim.
FIELDS = [
    {"id": "clone", "label": "One variety",
     "name": "One variety, a thousand identical plants",
     "note": "Every plant grown from cuttings of the same original, easiest "
             "to harvest by machine, and every plant has exactly the same "
             "weaknesses.",
     "varieties": 1, "resistant": 0,
     "variation_word": "none", "variation_bar": 9,
     "yield_word": "highest", "yield_bar": 100},
    {"id": "four", "label": "Four varieties",
     "name": "Four varieties, 250 plants of each",
     "note": "A little less convenient — four harvest dates, four sets of "
             "instructions — and one of the four happens to carry resistance "
             "to this particular blight.",
     "varieties": 4, "resistant": 1,
     "variation_word": "4 varieties", "variation_bar": 36,
     "yield_word": "good", "yield_bar": 85},
    {"id": "ten", "label": "Ten varieties",
     "name": "Ten varieties, 100 plants of each",
     "note": "The way small farms grew potatoes for centuries, and still do in "
             "the Andes where the crop originated. Awkward to manage, and four "
             "of the ten resist this blight.",
     "varieties": 10, "resistant": 4,
     "variation_word": "10 varieties", "variation_bar": 90,
     "yield_word": "good", "yield_bar": 85},
    {"id": "landrace", "label": "A mixed landrace",
     "name": "A mixed landrace, every plant slightly different",
     "note": "Not varieties at all — a population grown from seed, so no two "
             "plants are genetically identical. Yields less per plant and is "
             "nearly impossible to harvest mechanically.",
     "varieties": 1000, "resistant": 620,
     "variation_word": "very high", "variation_bar": 100,
     "yield_word": "lowest", "yield_bar": 55},
]

# ── the four cards in the band section (page lines 341–346) ──────────────
#
# TWO GROUPS AND A THIRD, and the grouping is the section: Design's `kind` is the
# mono accent tag and it reads "In the wild" once, "In storage" twice and "Living
# collections" once — so the card grid IS the statement above it, *Two places to
# store it, and only one of them is alive.* `kind` maps to `role` and `name` to
# `name`, which are the slots `_rule_card()` reads for them.
#
# ⚠️ DESIGN'S FOURTH PART, `limit`, HAS NO SLOT IN `_rule_card()` — it reads
# initials/num, role/label, term/name/title, chips, gloss/body/close and
# examples, and nothing else. `examples` is the only free slot and it is MONO
# 15px (`shared/ks3.css` line 2595), which is a foot line for "Height, mass, hand
# span" and not for two sentences of prose. So each `limit` is JOINED to its own
# `body` with a single space: every byte of both strings survives, in Design's
# order, in the body font she drew them in. What is lost is one paragraph break
# and the muted tone on the second half.
#
# ⚖️ NOT ONE `limit` IS DROPPED, and that is the load-bearing part: the limit is
# what makes each card an honest one. "Vulnerable to exactly the pressures that
# made protection necessary", "they die quietly in the dark", "a stored
# population cannot be a functioning one", "captive populations lose variation
# and adapt to captivity" — those four sentences ARE the second confrontation,
# stated once per method, and a card grid without them would read as four
# solutions rather than four partial ones.
BANK_CARDS = [
    {"role": "In the wild",
     "name": "Protected habitat",
     "body": "Populations left where they are, still breeding, still "
             "varying, still evolving in response to whatever happens. The "
             "only method that preserves the ecosystem along with the "
             "species.",
     "limit": "Needs land, and land has other uses. Vulnerable to exactly the "
              "pressures that made protection necessary."},
    {"role": "In storage",
     "name": "Seed banks",
     "body": "Dried seeds at around minus eighteen degrees, catalogued and "
             "duplicated between countries. Cheap per sample and enormous "
             "numbers can be held in one building.",
     "limit": "Only works for seeds that survive drying and freezing, and "
              "they must be tested and regrown on a cycle or they die quietly "
              "in the dark."},
    {"role": "In storage",
     "name": "Frozen sperm, eggs and tissue",
     "body": "For animals, where you cannot store a seed. Frozen zoos hold "
             "material from thousands of species, including some already "
             "extinct in the wild.",
     "limit": "Bringing an animal back from frozen cells needs a surrogate "
              "mother of a close species, and a stored population cannot be a "
              "functioning one."},
    {"role": "Living collections",
     "name": "Botanic gardens and zoos",
     "body": "Living organisms maintained and bred deliberately, with "
             "studbooks tracking relatedness to keep as much variation as "
             "possible.",
     "limit": "Expensive per individual, holds small numbers, and captive "
              "populations lose variation and adapt to captivity over "
              "generations."},
]


LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 174 character for character.
    "slug":        "biodiversity-and-gene-banks",
    "title":       "Biodiversity and gene banks",
    "discipline":  "biology",
    "unit":        "evolution-extinction-and-biodiversity",
    "family":      "SYSTEM",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.B.INH.07` — the importance of maintaining biodiversity and the use of
    # gene banks to preserve hereditary material — owned WHOLE. It is not
    # sub-split in `substatements.py`; see the docstring.
    "covers":      ["KS3.B.INH.07"],
    # Named, used, and owned elsewhere. INH.05 is b11-01's and b11-02's: this
    # page says selection can only act on variation that already exists and does
    # not re-teach the mechanism — rung 3's fourth criterion ASKS for the link
    # rather than supplying it. INH.06 is b11-03's: risk factor four, low genetic
    # variation, is named in the first confrontation and pointed back at the
    # lesson that owns it.
    "touches":     ["KS3.B.INH.05", "KS3.B.INH.06"],
    "beyond_statutory": False,
    # `genes-and-evolution` reaches `secure` here and this is the last lesson in
    # the thread across KS3 biology: the student has variation from b10-01,
    # inheritance from b10-04, competitive success from b11-01 and selection from
    # b11-02, and this is where all four are used on a decision rather than on an
    # explanation. `interdependence` is at `secure` too and is genuinely run
    # rather than name-checked — the second confrontation's whole argument is
    # that a seed is not a functioning member of anything until the pollinator,
    # the soil fungus and the disperser are also there, which is B9's web stated
    # from the other end.
    "threads":     [{"id": "genes-and-evolution", "level": 3},
                    {"id": "interdependence", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # Design's "Before this lesson" card, in her order. Both are bare slugs:
    # `requires` resolves across the whole key stage. Both are also the two
    # destinations the stripped hyperlinks in "What could not be lifted" 1 and 2
    # pointed at, so neither reference is lost with the tag.
    #
    # ⚠️ Both are B11 slots authored by sibling passes in this same run. They
    # resolve regardless: `validate()` checks `requires` against the lesson
    # REGISTRY, which is built from `structure.py` and holds every slot whether
    # authored or not, so an unauthored sibling renders an honest coming-soon
    # page rather than failing the build (§11 decision 8).
    "requires":    ["when-the-environment-changes-extinction",
                    "natural-selection"],
    "assumes":     [],
    # Design's "Connects to" card, in her order.
    #
    # ⚠️ BOTH MUST CARRY THEIR UNIT. A bare slug in `references` is resolved
    # against the CURRENT unit — unlike `requires` — so the bare form would build
    # a link to a B11 page that does not exist. Both targets are B9 and both are
    # authored and shipped, so both render as live cards rather than coming-soon.
    "references":  [{"unit": "B9", "lesson": "pollinators-and-food-security"},
                    {"unit": "B9", "lesson": "disturbing-a-food-web"}],
    "connects_heading": "Connects to",
    "ks4_links":   [],
    "ks4_becomes": "Maintaining biodiversity, the trade-offs in conservation "
                   "programmes, and the biological arguments behind "
                   "agricultural policy.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Variation is what a population has instead of a plan. "
                    "Keeping it — in the wild where possible, in a freezer "
                    "where necessary — is the closest thing biology has to an "
                    "insurance policy.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them (page lines 296–301). `s-banks` is the
    # third: no control of its own, so it mirrors `s-bench` and ticks on the
    # bench's predicate — Design's own `isDone()`, page lines 386–387. `short`
    # and `label` are her `RAIL_SHORT` and `RAIL` strings, "One banana"
    # included. Shipping three fails `check_rail_matches_design`, whose row for
    # this page reads `s-hook s-bench s-banks s-ladder | s-banks=s-bench`.
    "rail": [
        {"anchor": "s-hook", "short": "HOOK", "label": "One banana",
         "done_when": "committed"},
        # Design's own threshold, kept: two of the four blighted (page line
        # 386). Sticky by her design and monotonic by ours — `tried` is a set
        # that is only ever added to, and `Clear the field` clears `released`
        # while keeping it.
        {"anchor": "s-bench", "short": "BENCH", "label": "The blight",
         "done_when": "two_blighted"},
        # The MIRROR. Design gives it the bench's predicate character for
        # character one line further down, so the stop ticks the moment the
        # bench does and nothing ticks on load.
        {"anchor": "s-banks", "short": "BANKS", "label": "Gene banks",
         "mirrors": "s-bench",
         "done_when": "two_blighted"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key, and Design's own
    # reveal is gated on `hookChoice !== null` rather than on a right answer
    # (schema §6: no option is correct, any choice reveals the same paragraph).
    # B is the one the reveal endorses and it says so at once, in the same words.
    #
    # ⚖️ THE THREE WRONG OPTIONS ARE THREE DIFFERENT WAYS OF MISSING THE SAME
    # THING. A says clones are inherently weaker — a property of the individual
    # rather than of the population; C says the disease spreads faster when
    # plants are close — true of any dense crop, and nothing to do with genetics;
    # D is a real fact about bananas that explains why they are cloned rather
    # than why cloning is dangerous. All three are about the plant. The answer is
    # about the population, which is the move the whole lesson asks for.
    "phenomenon": {
        "kind": "narrative",
        "title": "Every Cavendish banana in every shop is a clone of every "
                 "other one.",
        "prompt": "Not a variety in the ordinary sense — a single genetic "
                  "individual, propagated by cuttings, grown by the billion. "
                  "The Cavendish is only the current banana because the "
                  "previous one, the Gros Michel, was wiped out commercially "
                  "by a fungus in the 1950s. The same kind of fungus is now "
                  "moving through Cavendish plantations.",
        "commit": "Why is a crop of genetically identical plants so "
                  "vulnerable?",
        "options": [
            # A: a property of the individual, not of the population
            "Because clones are weaker than plants grown from seed",
            # B: the one the reveal endorses, in the reveal's own words
            "Because if one plant can be killed by the disease, every plant "
            "can",
            # C: true of any dense crop, and nothing to do with genetics
            "Because diseases spread faster between plants that are close "
            "together",
            # D: a real fact, and the reason bananas ARE cloned rather than the
            # reason cloning is dangerous
            "Because bananas have no seeds to replant",
        ],
        # ⚠️ `b11-02` RESOLVED TO ITS LESSON TITLE — "What could not be lifted"
        # 1. `rich()` strips the anchor and the link text was a slot code.
        "reveal": "Because if one plant can be killed by a disease, every "
                  "plant can — they are the same plant. There is no resistant "
                  "minority for selection to work with, which is the whole "
                  "mechanism from Natural selection removed at a stroke. "
                  "Genetic variation is not a nice-to-have; it is what stops a "
                  "single event taking everything.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Schema §12's pre-allocation for b11-04, and the two beliefs Design's
    # `#s-think` quotes, in her page order. Both statements are her own bytes,
    # page lines 178 and 182, in register voice.
    #
    # ⊕ The `EVOL` prefix row and both of these rows were opened in
    # `docs/ks3/misconception-register.md` during this run, and they agree with
    # these on all three fields. That file is not this pass's to edit (contract
    # §0); re-checked at the end of the run because it was in flight.
    #
    # ⛔ `EVOL-12` is this lesson's named SPARE and is NOT claimed: two beliefs
    # were found and two ids were used. It stays permanently unused rather than
    # being re-pointed at anything later (schema §12).
    "misconceptions": [
        {"id": "EVOL-07",
         "statement": "Biodiversity means how many different species there "
                      "are.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "EVOL-08",
         "statement": "We have gene banks, so it does not matter if species "
                      "are lost in the wild.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
    ],

    # Design draws no keyword block anywhere in B11, so these never reach the
    # lesson body. The TERMS reach a student as the browse page's "Words this
    # unit gives you" chips, and the reading-age gate reads them as its exclusion
    # list. Every definition below is authored, not lifted.
    #
    # ⚖️ `biodiversity` is glossed as TWO measures rather than one, because the
    # whole of `EVOL-07` is a student holding only the first. `gene bank` is
    # glossed as insurance rather than as a solution, for `EVOL-08`. `variety`
    # and `landrace` are the two words the bench's four tabs turn on and a
    # student who has not met either reads the tabs as four sizes of the same
    # thing.
    "vocabulary": [
        {"term": "biodiversity",
         "definition": "The variety of living things: the number of different "
                       "species, and the genetic variation within each one.",
         "note": "Two measures, and the second is the one this lesson turns "
                 "on."},
        {"term": "gene bank",
         "definition": "A store of hereditary material — seeds, sperm, eggs or "
                       "tissue — kept so that variation can be recovered "
                       "later.",
         "note": "Insurance against a loss, not a way of preventing one."},
        {"term": "monoculture",
         "definition": "A crop grown as a single variety across a whole field "
                       "or region.",
         "note": "The highest yield in a good year, and nothing to fall back "
                 "on in a bad one."},
        {"term": "variety",
         "definition": "A named type of a crop species, bred to be consistent, "
                       "so all its plants are closely related.",
         "note": "Four varieties is four kinds of plant, not four thousand."},
        {"term": "landrace",
         "definition": "A crop population grown from seed in one place over "
                       "many generations, so no two plants are genetically "
                       "identical.",
         "note": "Less per plant in a good year, and something left in a bad "
                 "one."},
        {"term": "clone",
         "definition": "An organism genetically identical to the one it was "
                       "grown or copied from.",
         "note": "A thousand cloned plants is one plant repeated a thousand "
                 "times."},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⚠️ EMPTY, AND MEASURED. `<img>`, `<figure>` and `<picture>` each appear
    # zero times on this page — grepped — and every `<svg>` is chrome. Schema §13
    # says the same of all four B11 pages. The unit's one ruled diagram is the
    # peppered-moth pair and it belongs to b11-02.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-bench — the flagship, authored inline and lifted into activities[]
        # by ks3_data/b11/__init__.py::_normalise, which leaves the `practical`
        # shell behind it. Design's block is `ks3-block ks3-dark ks3-practical`
        # (page line 104), so the segment is MEASURED and not inherited.
        #
        # Payload keys follow docs/ks3/b11-inventory/PAYLOAD-SCHEMA.md §5. The
        # read sites are listed in the docstring; `survivors`, `pct`, an opening
        # selection, and every one of `field`, `released` and `tried` are
        # deliberately absent and each has its own reason there.
        {"type": "blight-bench", "id": "plant-it-then-release-the-blight",
         "anchor": "s-bench", "segment": "practical",
         "demand": "investigate",
         "eyebrow": "At the bench · four fields, one disease",
         "title": "Plant it, then release the blight",
         "intro": "A thousand potato plants, and a blight that a few "
                  "varieties happen to resist. Watch what is left to plant "
                  "next year.",

         # The mono label over the four field tabs, and the head-row counter.
         # `progress_zero` is the resting state Design draws before anything has
         # been released — "no blight released yet", not "0 fields tested" —
         # which is MRB-208's nothing-ticks-on-load stated in words.
         "tabs_label": "What you planted",
         "progress_suffix": "field(s) tested",
         "progress_zero": "no blight released yet",

         # ⛔ THE DENOMINATOR OF EVERY BAR, and the number the clone verdict's
         # "not one plant in a thousand" quotes. It is authored ONCE; the four
         # survivor counts are derived from it and never authored beside it.
         "total": 1000,

         "fields": FIELDS,

         # ⚖️ THE THREE BARS, AND THE SECOND AND THIRD RUN OPPOSITE. The first is
         # the outcome, the second is the cause and the third is the price — and
         # the third is why the first is a trade-off rather than a lesson in
         # being sensible. Design's order, kept: a student reads the consequence
         # before the explanation, which is the order the bench asks the question
         # in.
         "bar_labels": ["Plants surviving the blight",
                        "Genetic variation in the field",
                        "Yield per plant in a good year"],
         # ⊕ MRB-257 (5.41) — the SAME ROW, before the blight. It was sharing
         # `bar_labels[0]`, so the resting page read "Plants surviving the
         # blight — 1000 of 1000" with a full green bar, about a blight nobody
         # had released. Before the release the number is a count of what was
         # planted; the row only becomes a survivor count once the blight has
         # passed through, and the two states now say which they are.
         "bar_label_before": "Plants standing in the field",

         "run_label": "Release the blight",
         "ran_label": "Blight has passed through",
         # Design DRAWS this button (page line 143) and never disables it. It
         # clears `released` only — `tried` survives, so the rail cannot be
         # unticked by pressing it, which is MRB-208's rule that participation
         # is not undone.
         "reset_label": "Clear the field",

         # ⛔ KEYED BY FIELD ID, ALL FOUR WRITTEN OUT (schema §5). `four` and
         # `ten` carry IDENTICAL text and that is deliberate, not drift: Design
         # has one shared `else` branch for them, and `{pct}` already resolves to
         # 25 and 40. Keying by id removes the silent-`else` trap where a fifth
         # field would inherit a verdict written for two others.
         #
         # ⚑ FLAG 13 — THE FAMINE CLAUSE, CHANGED. Design's clone verdict read
         # "This is the Irish potato famine of the 1840s in miniature"; the thing
         # it points at is a dead CROP, and calling a dead crop the famine in
         # miniature teaches that the blight caused the famine. Schema §14 sets
         # the test — the clause must be about the crop failing, not about the
         # famine's death toll or its causes — and rules that the politics are
         # history's to teach and must NOT be added here. One clause, still one
         # clause, now about the crop. Full working in the docstring.
         "verdicts": {
             "clone": "Nothing survives. Not one plant in a thousand, because "
                      "there was only ever one plant repeated a thousand times "
                      "— and this blight kills it. This is what happened to "
                      "Ireland's potato crop in the 1840s, in miniature, and "
                      "it is the shape of the Gros Michel banana as well.",
             "four": "About {pct}% survives — not a good year, and not a "
                     "catastrophe. There is a crop to eat and, more "
                     "importantly, seed to plant that is known to resist. "
                     "Variation is what turns a total loss into a bad harvest.",
             "ten": "About {pct}% survives — not a good year, and not a "
                    "catastrophe. There is a crop to eat and, more "
                    "importantly, seed to plant that is known to resist. "
                    "Variation is what turns a total loss into a bad harvest.",
             "landrace": "Around {pct}% of the crop comes through, and next "
                         "year every one of those survivors is a plant that "
                         "resisted. The yield per plant was never the highest "
                         "here; the yield in the year of a blight is the only "
                         "one that decides whether anyone eats."}},

        # #s-banks — the band panel, rail stop 3, mirroring `s-bench`. Design
        # draws eyebrow, statement, four cards, key fact — and NO closing
        # paragraph, so `close` is absent.
        {"type": "rule", "anchor": "s-banks",
         "eyebrow": "Keeping the variation",
         "statement": "Two places to store it, and only one of them is alive.",

         "cards": BANK_CARDS,

         # Design nests the key fact inside this section (page lines 167–170) on
         # the CARD ground with the 5px accent offset shadow. `card`, because the
         # section itself is `--ks3-band` and band on band is invisible — the
         # same arrangement and the same reason as b7-01's, b8-01's, b9-01's and
         # b10-01's.
         "key_fact": {"ref": "biodiversity-is-two-things",
                      "ground": "card"}},

        {"type": "misconception", "id": "biodiversity-and-what-a-bank-holds",
         "anchor": "s-think", "targets": "EVOL-07"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Nested inside #s-banks on the card ground — Design's own arrangement,
    # measured: `--ks3-card`, 2px ink border, `box-shadow: 5px 5px 0
    # var(--ks3-accent)`. Never amber. Lifted byte-identical from page line 170
    # and identical to payload schema §9's b11-04 entry.
    #
    # ⚖️ ITS FIRST SENTENCE IS `EVOL-07` ANSWERED AND ITS LAST IS `EVOL-08`
    # ANSWERED, and no later pass may compress them: "between species, AND
    # between individuals within a species" is the half a species count leaves
    # out, and "so that variation is not lost for ever if a population is" is a
    # claim about the VARIATION, carefully not a claim about the population.
    "key_facts": [
        {"id": "biodiversity-is-two-things",
         "text": "Biodiversity is the variety of living things — between "
                 "species, and between individuals within a species. It "
                 "matters because variation is what allows populations to "
                 "survive change. Gene banks store seeds, sperm, eggs and "
                 "tissue so that variation is not lost for ever if a "
                 "population is.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [
        # TWO wrong ideas in one "Think again" block, the second behind an
        # amber-topped divider — `r_confrontation` renders exactly that from
        # `statements[]`. The block asks for no commitment on Design's page
        # (measured: static markup, no options, no reveal, no button, no `sc-if`,
        # schema §7), so it is a `confrontation` and not a `predict`, it is not a
        # rail stop, and it emits no completion contract.
        {"id": "biodiversity-and-what-a-bank-holds",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "EVOL-07",
         "statements": [
             # EVOL-07. The `<em>` run is kept — `rich()` renders it — because
             # "the variation WITHIN each species" is the half of the definition
             # the belief omits, and the italics are how Design marks the word
             # the whole correction turns on. ⚖️ Note what the correction does
             # NOT do: it does not tell the student that species counts are
             # wrong. It says there are two measures and names when each one is
             # the right question, which leaves both standing.
             #
             # ⚠️ `the last lesson` RESOLVED TO ITS LESSON TITLE — "What could
             # not be lifted" 2.
             {"quote": "Biodiversity means how many different species there "
                       "are.",
              "body": ["That is one of the two things it means, and the "
                       "other one is doing more work in this unit. "
                       "Biodiversity includes the variation <em>within</em> "
                       "each species — how genetically different the "
                       "individuals of one population are from each other. "
                       "A wood with forty species in it, each reduced to a "
                       "handful of closely related survivors, is in far "
                       "more trouble than the species count suggests, and "
                       "this is exactly the vulnerability that appeared as "
                       "risk factor four in When the environment changes: "
                       "extinction. It is also the sense in which a field "
                       "of one thousand identical potato plants has a "
                       "biodiversity of almost nothing, despite being a "
                       "thousand living organisms. Count species when you "
                       "want to describe a habitat; ask about variation "
                       "within a species when you want to know whether it "
                       "can survive what happens next."]},
             # EVOL-08. ⚖️ The last sentence is the one that makes this a
             # correction rather than a dismissal — gene banks are "worth every
             # penny", and the objection is to what they are being claimed to
             # do, not to their existence. A later pass that trimmed it would
             # turn a nuanced position into an argument against seed banks,
             # which is not what the page says and not what rung 4 marks.
             {"quote": "We have gene banks, so it does not matter if species "
                       "are lost in the wild.",
              "body": ["A seed bank stores a species; it does not store the "
                       "thing the species was part of. Put a seed back into a "
                       "landscape and it needs the soil fungi it partners "
                       "with, the insect that pollinates it, the animal that "
                       "disperses it, and a climate resembling the one it "
                       "left — none of which is in the freezer. Seeds also do "
                       "not last for ever: they need testing, regrowing and "
                       "replacing on a cycle, which is expensive and only as "
                       "reliable as the funding. And a stored population "
                       "cannot go on evolving; it is frozen in the state it "
                       "was collected in, while the world outside carries on "
                       "changing. Gene banks are worth every penny as an "
                       "insurance policy, and the honest description of them "
                       "is exactly that — insurance, taken out against a loss "
                       "you are still trying to prevent, not a substitute for "
                       "preventing it."]},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 LENGTH PARITY — RUNG 1 CLEAN AS DRAWN, RUNG 2 REPAIRED AT THE
    # DISTRACTORS. rung 1 correct 9w against 8 / 6 / 7 (gap 1, ratio 1.13);
    # rung 2 correct 23w against 5 / 9 / 10 as drawn — gap 13, ratio 2.30, both
    # limbs of the gate tripped — repaired to 23w against 18 / 19 / 24, so the
    # correct answer is no longer strictly the longest and the longest option on
    # the rung is a DISTRACTOR. **No correct option was shortened, no `answer`
    # index moved and no correction edited.** Full working in the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · What biodiversity includes",
            "q": "Which field has the lowest biodiversity?",
            # Design's four, UNTOUCHED. All four name a field and nothing else,
            # so there is no rule anywhere in the set for a correct answer to be
            # longer than, and the spread is 6 to 9 words.
            #
            #   A  correct — a thousand organisms and no variation at all
            #   B  the most plants, which is what "biodiversity" sounds like it
            #      is asking about if you read it as a count of individuals
            #   C  the bench's own third field, offered to a student who has just
            #      watched ten varieties do badly
            #   D  EVOL-07 — the fewest SPECIES, and therefore the answer a
            #      student who reads biodiversity as a species count must give
            "options": [
                "A thousand potato plants, all clones of one variety",
                "A field with fifty plant species in it",
                "A field with ten potato varieties",
                "A field with two species of grass",
            ],
            "answer": 0,
            # Design's three corrections, byte-identical. D's is the one doing
            # the real work: it CONCEDES that two species is low and then makes
            # the distinction the belief is missing.
            "feedback": {
                1: "Fifty species is high biodiversity by any measure. The "
                   "question is looking for the least variety, not the most "
                   "plants.",
                2: "Ten varieties is far more variation than one. Not as much "
                   "as a mixed population, but nothing like the lowest.",
                3: "Low, but each species is a population of individuals that "
                   "differ from one another. A clone field has no variation at "
                   "all.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A conservation charity says a seed bank means a plant "
                 "species can never truly be lost. What is the strongest "
                 "objection?",
            # ⊕ MRB-177 — THE CORRECT OPTION IS DESIGN'S, UNTOUCHED AT 23 WORDS.
            # The three distractors were 5 / 9 / 10 and are now 18 / 19 / 24,
            # each extended into the same claim-plus-consequence shape the
            # correct option already had, so that each is a rival ANSWER to
            # "what is the strongest objection?" rather than a fragment. Every
            # correction below is Design's and answers its own option exactly as
            # before; not one was edited. Working in the docstring.
            #
            #   A  extended: seeds do not survive freezing → so the sample is
            #      already dead
            #   B  correct, Design's own words, untouched
            #   C  extended: too expensive → so the money is better spent
            #      elsewhere
            #   D  extended: nobody knows how to plant one → so a stored species
            #      could never come back at all
            "options": [
                "Seeds do not survive freezing, so a stored sample is already "
                "dead by the time anyone needs it",
                "Gene banks are too expensive to be worth building, so the "
                "money would always be better spent somewhere else",
                "Nobody knows how to plant a seed from a gene bank, so a "
                "species stored in one could never be brought back at all",
                "The seed can be regrown, but the ecosystem it depended on — "
                "pollinators, soil fungi, seed dispersers — is not in the bank",
            ],
            "answer": 3,
            "feedback": {
                0: "Many do, which is what makes seed banks work. Some species "
                   "have seeds that cannot be dried or frozen, and those are a "
                   "real and separate problem.",
                1: "They are cheap relative to what they protect, and the "
                   "Svalbard example shows they get used. Cost is not the "
                   "objection that matters.",
                2: "It has been done, repeatedly and successfully. The "
                   "difficulty is what the seedling comes back to, not the "
                   "planting.",
            }},
        "explain": {
            # ⚖️ THE RUNG THE BENCH IS BUILT FOR. Criterion 4 is the one that
            # makes this a B11 rung rather than a crop-science one: it asks for
            # the link to natural selection explicitly, and criterion 5 states
            # the consequence — a clone population has nothing for selection to
            # act on. That is `EVOL-08`'s cousin refuted by construction: the
            # variation has to exist BEFORE it is needed, which is also the whole
            # argument for storing it.
            "title": "Rung 3 · Explain the monoculture risk",
            "q": "Explain why a field of genetically identical crop plants can "
                 "be completely destroyed by a disease, while a field of many "
                 "varieties usually is not — and link your answer to natural "
                 "selection.",
            "field_label": "Your explanation",
            "placeholder": "If every plant is genetically identical…",
            "success": [
                "Says genetically identical plants all have the same "
                "susceptibility, so if one can be infected they all can.",
                "Says a mixed field contains plants with different versions of "
                "genes, some of which may resist the disease.",
                "Says the resistant plants survive and can be harvested and "
                "replanted.",
                "Links this to natural selection: selection can only act on "
                "variation that already exists in the population.",
                "Concludes that a clone population has no variation for "
                "selection to act on, so there is no possibility of a "
                "resistant survivor.",
            ]},
        "produce": {
            # ⚖️ A DECISION WITH NO RIGHT ANSWER, MARKED ON THE REASONING. The
            # criteria never say which option to fund — criterion 3 asks only
            # that the choice be grounded in biology rather than preference, and
            # criterion 4 asks the student to name what their OWN choice fails to
            # protect. That is the honest shape for a trade-off, and it is the
            # same shape the bench draws: the clone field really is best at
            # something.
            "title": "Rung 4 · Take it somewhere new",
            "q": "A government has a fixed conservation budget and must divide "
                 "it between protecting habitat and expanding a national seed "
                 "bank. Set out the argument for each, say which you would "
                 "fund more heavily and why, and identify one thing your "
                 "choice would fail to protect.",
            "field_label": "Your answer",
            "placeholder": "Protecting habitat keeps…",
            "success": [
                "States what habitat protection achieves: living populations "
                "that keep varying and evolving, with their ecosystem intact.",
                "States what a seed bank achieves: many species stored cheaply "
                "and safely, including some already lost from the wild.",
                "Makes a clear choice with a reason grounded in biology rather "
                "than preference.",
                "Identifies a real limitation of the chosen option — land use "
                "conflict, or the fact that stored material stops evolving.",
                "Recognises the two are complementary rather than "
                "alternatives, or explains why a split would still involve a "
                "trade-off.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Biodiversity is the variety of life: the number of species, "
                "and the genetic variation within each one. Variation is what "
                "allows a population to survive a change, so losing it raises "
                "the risk of extinction and, in crops, of total crop failure. "
                "Gene banks preserve hereditary material — seeds, sperm, eggs, "
                "tissue — as insurance, but they cannot store an ecosystem and "
                "a stored population stops evolving.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ NOTES-B11 flag 14, ruled right in schema §14 and shipped as drawn: about
    # 1,300 km from the North Pole, well over a million samples, minus eighteen
    # degrees, permafrost backup, and the real Aleppo/ICARDA withdrawal and
    # return. ⚖️ MRB-225 holds: the layer is the insurance policy being CLAIMED
    # ON, which is the lesson's own claim tested rather than a new one, and its
    # last clause repeats the second confrontation's limitation rather than
    # retracting it.
    #
    # ⚠️ ONE `—` ESCAPE REPAIRED — "What could not be lifted" 3. Page line
    # 288 prints six literal characters where the em dash belongs.
    "stretch": [
        {"type": "explainer", "id": "the-svalbard-global-seed-vault",
         "text": "The Svalbard Global Seed Vault sits inside a mountain on an "
                 "Arctic island, about 1,300 km from the North Pole. It holds "
                 "well over a million seed samples sent by seed banks all over "
                 "the world, in sealed foil packets at minus eighteen degrees, "
                 "and it is designed to keep them cold even if the power "
                 "fails, because the surrounding rock is permanently frozen. "
                 "It is a backup of backups: countries deposit duplicates of "
                 "what their own national banks already hold. It has been used "
                 "for real. Syria's seed bank at Aleppo, which held varieties "
                 "of wheat and barley from across the Middle East, became "
                 "inaccessible during the civil war, and researchers withdrew "
                 "their duplicate samples from Svalbard, grew them on in "
                 "Lebanon and Morocco, and sent fresh seed back to the vault. "
                 "That is the whole argument for gene banks in one story — and "
                 "also for why the seeds have to be regrown periodically "
                 "rather than simply left in a freezer."},
    ],

    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The card points at this lesson's own bench, which is a real destination on
    # the page it is printed on (§4.8.1 C) — and rung 4 is the conservation
    # decision the body offers to argue.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to argue the case for or against a conservation "
                      "decision?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ⊕ `convention_note`, not `safety_note`. Design draws ONE plain
    # `.ks3-legal` paragraph (page line 320) and nothing in it is a safety
    # instruction — it is a note about what the model simplifies and which of the
    # three real-world cases are real. Routing it through `safety_note` would
    # print it in the treatment reserved for "never light a candle without an
    # adult".
    #
    # ⚑ NOTES-B11 flag 15 lands here: the invented 62% is covered by the first
    # sentence, and the last sentence is the line that keeps the Gros Michel,
    # the Cavendish and Svalbard on the right side of the model/real boundary.
    # It must keep saying the same thing as the bench, which derives its
    # percentages from `resistant` over `varieties` and nothing else.
    "convention_note": "The blight bench is a teaching model: the disease "
                       "affects whole varieties rather than individual plants, "
                       "resistance is all-or-nothing, and yield is treated as "
                       "directly proportional to surviving plants. Real blight "
                       "resistance is partial and varies with weather, and "
                       "real fields lose some of every variety. The Gros "
                       "Michel, Cavendish and Svalbard accounts are real.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # The bench is `interpret observations and data` (ANA.03) performed rather
    # than described — three bars that disagree, and the student has to say what
    # the disagreement means — and rung 3 is the same strand written out. Rung 4
    # is an argument about the application of science to a real decision with a
    # real cost, which is the attitudes strand rather than the analytical one.
    # Nothing here is measured or planned by the student, so the experimental
    # strand is not claimed.
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
