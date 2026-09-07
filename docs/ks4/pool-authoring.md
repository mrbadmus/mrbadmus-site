# KS4 assignment pool — the authoring standard (MRB-332)

Every question in `ks4_data/questions/` is written to this standard. A cold
science reviewer checks every one against it before anything is exported, and
nothing exports unreviewed.

---

## 1. What you are writing

**At least** twelve multiple-choice questions per KS4 subtopic — **at least
four `easier`, four `standard`, four `harder`** — that a Year 10 or Year 11
student meets as *homework*, set by their teacher alongside Sparx.

### ⊕ MRB-335, 8 Sep 2026 — a subtopic may now hold MORE than twelve

This said "twelve … four of each band", full stop, and for MRB-332 that was
right: a subtopic WAS twelve questions, and the automatic weekly assignment
took all of them.

Set work v2 changed what the pool is for. A teacher hand-picks up to twenty
questions from a whole TOPIC at one tier, and the 7 Sep 2026 availability
table found twenty-two (topic, tier) cells below the fifty-question floor
that makes picking meaningful — Combined Higher on `energy-changes` offered
twenty-eight. So the pool grows, and thirty-eight subtopics now hold between
fourteen and thirty-five questions.

**What did NOT change is the floor, or the first twelve.**

> **At least four per band, and the FIRST four of each band sit at bank
> positions 0–11.**

⚠️ **Positions 0–11 are the AUTOMATIC weekly assignment's window, and it is
load-bearing** (MRB-335 / RISKS D7). `composeFromBank` in the backend and
`compose_assignment` in Python both read `bank_position < 12` and take every
row of a band they find there. If a thirteenth question could land inside
that window, every auto-composed set in the estate would change the day the
pool grew — silently, with nothing saying so. `ks4_data.load_pool()` emits
the first four of each band FIRST and the extras afterwards, so the original
twelve keep their ids, their order and their positions, byte for byte;
`ks4_pool_check`'s *positions 0-11 are still four of each band* proves it
rather than trusting it.

**If you are ADDING to a subtopic that already has twelve:** continue each
band's id sequence (`e05`, `s05`, `h05` …), leave the existing twelve
untouched, and put the new rows in a separate `<topic>__setwork.py` module so
the diff shows what is new. Do not renumber anything.

They are not lesson questions. They are not a quiz on the page. They are the
work a teacher sets when they want a class to practise one subtopic, and the
student sits them once, away from the lesson, and gets a mark.

## 2. The one rule that outranks everything else

⚠️ **Never reuse, restate or lightly reword a lesson page's own "Test
yourself" question.**

Those live in `all_subtopics_*.py` under `quiz`, they are printed on a page
the child can open whenever they like, and they belong to a **different pool**
under the one-pool-per-surface law. An assignment question that restates one
is homework with the answers already published, and it fails the
`pool_ownership` gate.

Your brief (`python3 ks4_brief.py <subject> <topic>`) reproduces **everything
the page prints** in full, marked **DO NOT DUPLICATE**: the `quiz` questions,
the worked `fifas` (shown with their full solutions) and the `matching` block
(shown already paired). Read them first, then write *around* them: same spec
content, different question — a different quantity, a different direction of
reasoning, a different context, a different misconception under the knife.

### ⊕ The TASK/FACT line (ruled 6 Sep 2026, MRB-332)

A cold reviewer found 63 questions in one subject restating a printed matching
pair, and could only rewrite 26 of them: in six subtopics — `uses-of-nuclear-
radiation`, `stellar-evolution`, `poles-of-a-magnet` among them — the matching
block prints **the whole examinable core**, already paired. Every honest
replacement either duplicated another of the same twelve or left the spec.

So the rule is not "never touch anything printed". It is:

> **A published TASK may never be reproduced. A published FACT may be
> examined.**

| printed item | what it is | may a question restate it? |
|---|---|---|
| a `quiz` question | a task, printed with its answer | **No.** Reproducing it hands the child the exact thing they are being asked to do. |
| a `fifas` worked example | a task, printed with its full solution — and with its NUMBERS | **No**, and its numbers are off-limits too: reusing the mass, the voltage or the focal length makes a differently-shaped question answerable from memory of the printed solution. |
| a `matching` pair | a fact, printed as a pairing | **Yes, if the subtopic has no other spec content left.** A pair is not a question; a child still has to have read the page and retrieved the right half. |

Prefer to write around a matching pair where you can — an `easier` question is
better for reaching past a printed pairing than a `harder` one, and a `harder`
question built on a printed pair is usually a sign the band is wrong. But when
the spec point IS the matching block, examining it is correct, and inventing an
off-spec question to avoid it is worse. **A question that leaves the spec to
dodge a pairing is the real defect.**

The two thin cases found so far — `uses-of-nuclear-radiation` (four uses, all
printed) and `stellar-evolution` (one life cycle, printed) — cannot support
twelve non-overlapping questions against the current pages, and that is a
LESSON-PAGE finding, not a question finding. Note it and move on.

## 3. Spec fidelity

- Author to the **AQA specification point** printed in the brief (8461
  Biology, 8462 Chemistry, 8463 Physics). If a fact is not in the spec, it is
  not examinable, and it does not go in a distractor as though it were.
- Use **AQA command words** in stems: *state, describe, explain, calculate,
  determine, compare, evaluate, predict, suggest*. A `harder` question that
  says "what is" is an `easier` question wearing a coat.
- **UK spellings throughout**: sulfur (AQA's own), sulfate, sulfuric,
  aluminium, colour, metre, litre, fibre, analyse, catalyse, haemoglobin,
  oesophagus, ageing, practise (verb) / practice (noun).
- **Units on every quantity**, in the stem and in every option. Get the sig
  figs right and keep them consistent across the four options — a student
  must never be able to pick the answer because it is the only one written to
  2 s.f.
- **No question may require a figure.** No "look at the graph", no "in the
  diagram", no "the circuit shown". Everything needed to answer is in the
  words. Describe the setup in prose if you need one.

## 4. The three bands

| band | what it asks | a Year 10 should… |
|---|---|---|
| `easier` | recall, definition, identification, one-step substitution | be able to do it from memory of the lesson |
| `standard` | apply to a familiar context, two-step calculation, explain a mechanism | have to think, but not to be stuck |
| `harder` | unfamiliar context, multi-step or rearranged calculation, compare two cases, evaluate, spot the error in a stated line of reasoning | be stretched — this is where the grade 7–9 discrimination lives |

The bands are a difficulty ladder **within what that class may be asked**.
They are not tiers: a Foundation class receives all three bands.

## 5. Distractors

Four options. One correct. **Three distractors, each built on a real
misconception a teacher has actually met** — the brief's *"Declared common
mistake"* field is the first place to look, and the lesson's own theory prose
is the second.

- Every distractor must be **plausible to a student who has the misconception**
  and **wrong to one who does not**. "None of the above", joke options and
  obviously-absurd magnitudes are all wasted slots.
- For a calculation, distractors come from the **error**, not from noise:
  forgetting to convert grams to kilograms, using the final temperature
  instead of the change, dividing when you should multiply, dropping a power
  of ten, using the radius for the diameter.
- Options should be **similar in length and grammatical shape**. The longest
  option must not be the answer more often than chance — a student who has
  learned that heuristic should gain nothing here.
- No two options may say the same thing in different words.

## 6. Answer positions

**Spread the correct answer across A, B, C and D.** Within a subtopic aim for
roughly a quarter at each index, and never leave an index unused.

⊕ **MRB-335: measure the rows YOU wrote, not the corpus.** The longest-option
check in `ks4_pool_check` reads the whole pool against a 40% threshold, and a
few hundred skewed new rows inside 3,417 read as 24% — at chance, green, and
wrong. MRB-335's cold review measured its own 249 rows on their own and found
the correct option was the longest in 65% of them, because the answer carried
a "…, because …" clause its distractors did not. Give a distractor its own
reason, or move the correct option's reason into the `why` where it belongs.
A useful second measure: at 390 px a phone wraps an option every ~46
characters, so what a student can actually SEE is a correct option occupying
more LINES than any other. Keep that figure near 25% too.

This is measured, not trusted: `verify_answer_positions.py` fails the build if
any index holds more than half a corpus's answers or is never the answer at
all. It exists because KS3's bank once had a skew a student could have played.

## 7. The `why`

One line. It says **why the correct answer is correct** — the physics, not the
procedure. "Because ΔE = mcΔθ and Δθ is 40 °C, not 60 °C" teaches; "Option B
is correct" does not. Keep it to a sentence a student reads in the moment they
get the question wrong.

## 8. Tier and triple flags

Every question carries `tier` and `triple_only`. **You do not choose them** —
they are a property of the subtopic, printed at the top of each subtopic's
section in your brief, and `ks4_data.load_pool()` refuses any file whose
stated flags disagree with the curriculum. Copy them exactly as the brief
gives them.

What they mean for your writing:

- **BASE** (`tier='foundation'`, `triple_only=False`) — a Foundation Combined
  class will sit this. **Higher-tier content must not appear in it, in the
  stem or in any option.** No rearranged equations that only Higher meets, no
  Higher-only vocabulary.
- **HIGHER** (`tier='higher'`) — Higher tier only. The Higher extension prose
  in the brief is in scope.
- **TRIPLE** (`triple_only=True`) — Triple Science only. The Triple extension
  prose is in scope.

## 9. The file you write

`ks4_data/questions/<subject>/<topic_with_underscores>[__<part>].py`

```python
"""Physics · Particle model — specific heat capacity and latent heat.

A sentence or two on what these questions probe and where the distractors
come from. Written for the next person who has to change one.
"""

TOPIC = "particle-model"
SUBJECT = "physics"

QUESTIONS = [
    # ── temperature-changes-shc ─────────────────────────────────────────
    {
        "id": "ks4-temperature-changes-shc-e01",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which quantity does the symbol c represent in the equation "
                "ΔE = mcΔθ?",
        "options": [
            "The change in thermal energy, in joules",
            "The specific heat capacity, in J/kg°C",
            "The temperature change, in °C",
            "The mass of the substance, in kg",
        ],
        "correct_index": 1,
        "why": "c is the specific heat capacity — the energy needed to raise "
               "1 kg of the substance by 1 °C.",
    },
    # ... eleven more for this subtopic, then the next subtopic
]
```

**Ids** are `ks4-<subtopic-slug>-<e|s|h><nn>`, numbered from 01 within the
band. They are permanent and never reused.

Group the file by subtopic, in the order the brief gives them, with a comment
banner between subtopics. Within a subtopic write the four `easier`, then the
four `standard`, then the four `harder`.

## 10. Before you finish

Run, from the repo root:

```bash
python3 -c "import ks4_data; ks4_data.load_pool('<subject>', strict=False)"
```

It validates ids, flags, option counts, duplicate options and index ranges,
and it names the file and question of anything wrong. Fix everything it
reports. `strict=True` additionally requires at least twelve per subtopic and
at least four per band, and is what the export runs.

Then run the content gate, which also proves the auto-composition window is
intact:

```bash
python3 ks4_pool_check.py --python
```

And sweep your own rows for the two things no gate measures per-author: the
longest-option skew (§6) and near-duplicate stems inside one subtopic. A pair
that differs only in its numbers is the same question twice.
