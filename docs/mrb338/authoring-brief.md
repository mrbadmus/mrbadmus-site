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

- the key is the **longest** option about **one time in four** — not more;
- the key's length **rank** (1 = longest … 4 = shortest) **varies** across the
  leaf, roughly evenly. Never park it at rank 2 with a wide gap.
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
