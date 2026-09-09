# MRB-338 · the authoring brief every lane works from

One executor task = **one leaf**. Read this whole file before writing a row.

## 0 · The one rule that breaks the school if you get it wrong

**Never modify or reorder an existing question.** Every automatically-composed
weekly assignment in Rainford is drawn from `bank_position < 12`, and position
is the row's index in the file. So:

- **Append only.** New rows go at the END of the `QUESTIONS` list.
- Never edit, delete, reorder or renumber a row that is already there.
- Never write an id whose number is ≤ 04 in a band that already has 01–04.

Continue each band's id sequence from the leaf's current maximum. If a leaf
already has `e01…e09`, your first easier row is `e10`.

## 1 · KS3 — where the rows go

File: **`ks3_data/<unit>/questions_<NN>_<lesson_with_underscores>.py`** — the
lesson's existing file. Append to `QUESTIONS`.

Target **32 easier / 32 standard / 32 harder**. Row shape, exactly:

```python
    {
        "id": "b1-02-e10",          # <unit lower>-<lesson NN>-<e|s|h><nn>
        "band": "easier",           # easier | standard | harder
        "text": "The stem, as one string.",
        "options": [
            {"text": "A distractor.", "correct": False,
             "why": "Names the misconception and corrects it, in the voice "
                    "the rows above already use."},
            {"text": "The key.", "correct": True},
            {"text": "Another distractor.", "correct": False,
             "why": "…"},
            {"text": "A third distractor.", "correct": False,
             "why": "…"},
        ],
        "figure": None,
    },
```

Exactly four options, exactly one `"correct": True`. **Every distractor carries
a `why`; the key carries none at all** (omit the key, do not write
`"why": None`).

⚠️ **KS3 bank text is NOT run through `ks3_art.kit.formulae()`** — it is built
with `document.createTextNode`, so the child sees exactly the characters you
type. Write `CO₂` if you want a subscript; **never `<sub>`**, which is shown
literally.

## 2 · KS4 — where the rows go

File: **`ks4_data/questions/<subject>/<topic>__z338_<subtopic>.py`**, both with
underscores for hyphens — a NEW file, yours alone. The loader maps everything
before the double underscore to the topic, so
`cell_biology__z338_stem_cells.py` is the `cell-biology` topic.

⚠️ **The name starts `z338` for a load-bearing reason, not a decorative one.**
`load_pool` assigns `bank_position` in module load order, which is filename
sort order: the first four of each band take positions 0–11, and *everything
after that is positioned in the order the files are read*. A file named
`analysis__m338_…` sorts BEFORE the existing `analysis__setwork.py`, so it
would insert its rows ahead of that file's and push already-shipped rows to
new positions — mutating rows this programme is supposed to leave alone. `z`
sorts after `a`, `b`, `c` and `setwork`, so new rows always land last and no
existing row moves. Do not rename it.

Start the file:

```python
"""<Subject> · <Topic> — the MRB-338 expansion.

<Two or three sentences on which subtopics are here and why the weight
falls where it does. Follow the CONTENT, not the arithmetic.>
"""

TOPIC = "energy"          # hyphenated topic id
SUBJECT = "physics"

QUESTIONS = [
```

Row shape, exactly:

```python
    {
        "id": "ks4-energy-stores-systems-s05",   # ks4-<subtopic-slug>-<e|s|h><nn>
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",        # ⚠️ COPY FROM THE BRIEF — never chosen
        "triple_only": False,        # ⚠️ COPY FROM THE BRIEF — never chosen
        "text": "The stem, as one string.",
        "options": [
            "First option",          # plain strings, not dicts
            "Second option",
            "Third option",
            "Fourth option",
        ],
        "correct_index": 2,
        "why": "One sentence of the actual science — why the key is right.",
    },
```

`tier` and `triple_only` are **derived from the curriculum** by
`ks4_data.classify()` and are given to you per subtopic in your task. Copy them
onto every row. Getting them wrong is a child being handed content they have
not been taught.

**Targets.** A *base* subtopic needs **12 / 26 / 26**; a *higher-only* subtopic
needs **18 / 18 / 18**. Your task names which, and how many of each band to add.

⚠️ **KS4 formulae stay FLAT** — write `CO2`, `N2`, `H2O`. KS4 is deliberately
not wired to the subscript pass, because on KS4 `N2` means Newton's second law
and `F2` the second filial generation.

## 3 · Coverage before quota — the rule that stops paraphrase

**Before writing anything**, list every distinct teachable point in the leaf and
map the quota onto them. Write that list at the top of your report.

When a leaf runs out of distinct points, go **wider across its own material**,
never round again:

- named real examples (a specific metal, organ, instrument, planet, reaction)
- data with units — a number to work with, cleanly, coming out exact
- the required practical: apparatus, method order, the control variable, the
  error a student actually makes, how the result would change
- the misconception set — one question per misconception, from the wrong side
- comparison and evaluation: two cases, which and why
- rearrangement of an equation, and the unit that comes out

**Two stems in one leaf sharing ≥ 70% of their tokens is a defect.** So is
asking the same fact with the options shuffled.

## 3.5 · Pool ownership — read the lesson for the SCIENCE, never lift its tasks

You will read the lesson to find the teachable points. That is intended. What
is forbidden is carrying its **questions** across:

- **KS3**: the lesson's own ladder rungs (recall / apply / explain / produce)
  in `ks3_data/<unit>/lesson_<nn>_<slug>.py`.
- **KS4**: the `quiz` entries and the `fifas` worked examples in
  `all_subtopics_<subject>*.py`.

A `quiz` item and a `fifas` worked example are **tasks**, and reproducing one —
even reworded, even with the numbers changed — is a **hard failure** in
`pool_ownership.py`, not a warning. The lesson already prints them with their
answers, so a child who revised the page has seen the answer to your question.

A **fact** is different: if the spec point is genuinely the only thing there is
to say, you may examine the fact, in your own task, from your own angle. The
test is *"is this the same thing to DO, or the same thing to KNOW?"*

⚠️ Do not open a lesson's questions in order to avoid them. Derive the
teachable points from the lesson's **prose, keywords, practical and
misconceptions**, then write your own tasks from the specification.

## 4 · Content standards

- AQA (8461/8462/8463) or KS3 National Curriculum wording, at the right depth
  for the band. **AQA command words**: state, describe, explain, calculate,
  determine, compare, evaluate, predict, suggest.
- **UK spellings**: sulfur, aluminium, colour, metre, litre, fibre, analyse,
  haemoglobin, oesophagus.
- **Units on every quantity.** Calculations come out cleanly; keep significant
  figures consistent across all four options.
- **Every stem must be answerable away from the lesson.** No "look at the
  diagram", no "in the graph above", no reference to a figure or a page.
- **No "all of the above"**, no "none of the above", no negatives-in-caps
  trickery.
- Each distractor encodes a **real misconception** — plausible to a student who
  holds it, plainly wrong to one who does not. For calculations, make them
  error-based: forgot the unit conversion, used the final value not the change,
  divided instead of multiplied, dropped a power of ten.
- **Register safety**: reproduction, drugs and alcohol are taught matter-of-
  factly and without moralising; evolution is Darwinian only. Physics
  quantities take their definitions from `ks3_data/quantities.py` — check
  there before defining a core quantity, never retype one.

## 5 · The three bands

| band | what it asks |
|---|---|
| **easier** | recall, a definition, one-step substitution — reachable from memory of the lesson |
| **standard** | apply to a familiar context, two-step calculation, explain a cause |
| **harder** | unfamiliar context, multi-step or rearranged calculation, compare, evaluate |

A band is a rung of **demand**, not a different topic and not a different child.

## 6 · Length parity — an authoring rule, not a post-hoc fix

A pupil who cannot answer picks the longest option. Across the rows YOU write
in one leaf:

### ⚠️ Measure it the way the gate measures it — the 6-character margin

**Do not count "how often is the key the longest option".** That is not the
question `verify_answer_lengths` asks, and counting it that way will tell you
you are fine when you are not.

The gate throws away every set whose top two options are within **6
characters** of each other — those have no *visibly* longest option, so they
give a pupil nothing — and then asks, **of the sets that remain**, how often
the key is the long one. Chance is 25%; **32% is the ceiling**.

Those two measures come apart badly. Park the key at rank 2 in most rows but
let it run away whenever it *is* longest, and "key is longest" reads a healthy
20% while the gate reads **65%**. Two lanes did exactly that before this was
written down, and a third shipped a leaf at 66.7%.

So count it like this:

```python
MARGIN = 6
visible = correct = 0
for q in my_rows:
    lens = sorted((len(o) for o in options(q)), reverse=True)
    if lens[0] - lens[1] < MARGIN:
        continue                      # no visibly longest option — skip it
    visible += 1
    if len(key(q)) == lens[0]:
        correct += 1
print(correct, "/", visible, "=", 100.0 * correct / visible, "%")   # aim <= 32
```

⚠️ **And note which way the fix runs.** Lengthening the key to escape the
"key is shortest" tell pushes this number UP. The fix for both is the same and
it is not trimming keys: **give the distractors their own reasons, at the
key's level of detail**, so that the top two options are usually within six
characters of each other and there is no visibly longest option at all. A leaf
where most sets have no long option is a leaf where length answers nothing.

- the key is the **longest** option about **one time in four** — not more;
- the key's length **rank** (1 = longest … 4 = shortest) **varies** across the
  leaf, roughly evenly — **no single rank may hold more than 40% of the keys.**
  Never park it at rank 2 with a wide gap.

  ⚠️ **This is a floor as well as a ceiling, and the floor is the one that gets
  missed.** Driving "the key is longest" down towards zero is easy, and it lands
  straight in the opposite tell: a key that is the *shortest* option most of the
  time is exactly as learnable as one that is the longest, and a pupil finds it
  just as fast. The first KS3 leaf authored under this brief came back with the
  key shortest in 42 of 69 rows while its longest-is-correct rate looked
  healthy at 15%. Aim for the key sitting at each of the four ranks about a
  quarter of the time.
- **three times in four the longest option is a DISTRACTOR**, written to the
  key's level of detail — if the key earns a "…, because …" clause, give the
  distractors their own reason too, rather than trimming the key.

Same rule for position: spread `correct_index` (KS4) / the key's index (KS3)
roughly evenly over 0, 1, 2, 3 across your rows. Never leave an index unused.

## 7 · Before you report

Run these over your own leaf and fix what they find:

1. **Duplicate stems** — normalised for case, whitespace, trailing punctuation.
2. **Duplicate answer-sets** — no two rows sharing all four options.
3. **Paraphrase** — no two stems ≥ 70% token overlap.
4. **Length parity** — count how often the key is longest, and the rank spread.
5. **Position spread** — count the key's index across 0–3.
6. **Python parses**: `python3 -c "import ast; ast.parse(open('<file>').read())"`

Then **re-read every row cold, as an examiner**: is the key unarguably right,
is every distractor unarguably wrong, is the science correct, would AQA credit
it. Log every fix you made in your report.

## 8 · Report back

- the distinct-teachable-points list and how the quota mapped onto it
- rows added, per band
- the six self-check results, with numbers
- every cold-read fix
- anything you could not do, and why — **never pad to hit a number**

---

# 9 · STANDING RULES — everything night 1 learned the hard way

Ruled into the brief 9 Sep 2026. Every rule below cost a real defect to find.
Read this section before you write a row; it is not a summary of §1–8, it is
the set of things §1–8 did not say and should have.

## 9.1 · Measure length parity the way the gate measures it

Restating §6 because it is the one that got shipped wrong. **Not** "how often
is the key the longest option" — that number can read 20% while the real one
reads 65%. Discard every set whose top two options are within **6 characters**;
of the sets that remain, the key must be the long one **no more than 32%** of
the time (chance is 25%).

```python
MARGIN = 6
visible = correct = 0
for q in my_rows:
    lens = sorted((len(o) for o in options(q)), reverse=True)
    if lens[0] - lens[1] < MARGIN:
        continue
    visible += 1
    if len(key(q)) == lens[0]:
        correct += 1
```

⚠️ **Do not drive the denominator to zero.** A leaf where four sets are
visible and two are giveaways reads 50% on n=4, which the gate's binomial test
cannot even speak to. Flattening every set hides the number rather than
earning it. Aim for a real population of visible sets in which the long option
is usually a **distractor**.

⚠️ **Check the mirror too.** The gate fails below `LO = 0.12` as well. A key
that is reliably *not* the long option is exactly as learnable as one that is.
Sweep margins 3–10, not just 6, the way the gate's own sweep does.

## 9.2 · The fix is always the distractors

**Never trim a key. Never lengthen a key.** A key that states less than its
distractors is a worse question, and lengthening keys is what drives 9.1's
number up in the first place. Give the **distractors** their own reasons at the
key's level of detail.

For calculations: if the key carries the working and the distractors are bare
values, the answer is the long option every time. **Keep working in the `why`,
never in an option.**

## 9.3 · No length edit may touch an option marked correct — prove it

A lane rewriting option text for parity replaced the text of a **correct**
option with distractor prose. The row briefly stated something false as its
answer and the true answer was no longer among the four. **Nothing in the
estate catches this**: `question_bank` checks that exactly one option carries
`correct: True` and that the key has no `why`; `ks4_pool_check` checks that
`correct_index` is in range. Neither asks whether the key is still true.

So: no parity edit touches a key, and you **prove** it before reporting, by
comparing every row's key text against `git show HEAD:<file>`. At KS3 also
prove no `why` travelled onto a key and none fell off a distractor.

## 9.3b · ⚠️ A PARITY PATCH TABLE ADDRESSED BY POSITION GOES STALE

Two of the three defects this programme has caused itself came from the same
pass — rewriting option text for length — and neither was caught by a gate.

The first overwrote a key (§9.3). The second is subtler and is the reason this
rule is separate: a lane collected its edits into a patch table keyed on
**(row id, option index)**, then replaced one row's content late in the run.
The earlier patch still matched that id and index, so it landed on the **new**
row and dropped *"Push the container along the bench, or roll it over onto its
side"* into a question about an aerosol.

**Every gate passes that row.** Four options, exactly one correct, index in
range, ids unique, no duplicate stem. It is a perfectly well-formed question
whose third option is about something else entirely. Only a cold read finds it.

So:

- **Address a patch by its CONTENT, not its position** — match the exact option
  string you intend to replace, and assert it matched exactly once.
- **Re-derive the patch table after any row is replaced.** A table built before
  a content change is a table about a file that no longer exists.
- **Assert the target is not the key** on every entry, as §9.3 requires.
- **Cold-read every row you patched**, not only the ones you rewrote by hand.

## 9.4 · Sweep for duplicates across the whole UNIT or TOPIC, never the leaf

`set_work_scope_check` treats a whole KS3 unit and a whole KS4 topic as **one
cell** and fails on a repeated stem anywhere inside it. Two rows written on
one night duplicated a stem in a *different leaf* — and neither a per-leaf
check nor the lanes' own measurements could see it, because lanes cannot read
each other's uncommitted files.

Measure duplicate stems, duplicate option-sets and Jaccard across **every row
of your unit or topic**, including leaves other lanes are writing right now.

⚠️ And watch for the shared-fact case: three leaves of `cell-biology` each
wanted the same easier unit-conversion row. Only one may own it. If your leaf
needs a fact a neighbour has, ask it as a **different task**, or take a
different fact.

## 9.5 · Run `set_work_scope_check.py` before every commit

It is the only gate that sees 9.4. It is not optional and it is not slow.

## 9.6 · A stem must not state another row's keyed answer

Two stems in one leaf quoted "about two million every second" and "last about
four months" — both the keyed answers to other rows in the same leaf. A pupil
meeting them in one assignment is handed two answers free.

⚠️ Duplicate-stem and duplicate-option checks are **blind** to this: the
collision is between one row's STEM and another row's KEY. Check it yourself.

## 9.7 · All four options must read as though one hand wrote them

A short key beside three long explanatory distractors passes 9.1 easily — the
key is nowhere near longest — and still gives the answer away, because a pupil
spots the odd one out instantly and it is the right one.

Length parity is a proxy. The rule it stands for is that **nothing about an
option's shape, register, grammar or length should mark it out**. Other tells
found in one night: the key was the only option not beginning "They"; the key
was the only option naming a route; three distractors confessed their own
arithmetic error in the option text.

## 9.8 · Never reproduce a lesson's own rung, even when the brief names it

If a coverage list hands you a teachable point that **is** a ladder rung's task
— the germinating-peas and boiled-seed control, say — you do not write it. That
is a hard `pool_ownership` failure and the brief is wrong, not the rule. Write
the rung's underlying skill without its apparatus instead, and say in your
report what you declined and why.

## 9.9 · A distractor must be unarguably wrong, not merely not-the-best

Distractors thrown out in one night for being **defensible**: bacteria really
do take up DNA from their surroundings; surface-area-to-volume really does
fall then rise once a cell divides; a cell wall really is a barrier water
crosses; 0.1 mm really is about the naked-eye limit; the diaphragm really does
attach to the lower ribs; a marrow transplant really can change a blood group.

Also reject the **creditable** distractor — one that reaches a wrong conclusion
through a true clause an examiner would credit — and the distractor that is
wrong in your leaf but defensible **elsewhere in the unit** ("respiration needs
no oxygen" is wrong for aerobic respiration and arguable once the unit reaches
anaerobic).

⚠️ If you must lengthen a distractor for 9.1, lengthen it with a **false**
justification. Padding a wrong option with a true clause strengthens it.

## 9.10 · Every stem is read away from the lesson

No diagram, no graph, no table, no "the picture above", no "in this lesson".
A shipped row asking "which fact **from the table** explains that?" had no
table on the assignment page. If a stem needs a fact, the stem carries it.

⚠️ And write real characters: a stem carrying a literal `\n` becomes a real
newline plus indentation inside the question. Sweep your file for `\n` and
`<sub>` before reporting.
