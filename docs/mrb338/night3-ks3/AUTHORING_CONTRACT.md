# MRB-338 Night 3 — KS3 authoring contract (read this in full before writing a single row)

You are one of several parallel unit-lanes authoring new KS3 question-bank rows in this worktree
(`feat/bank-night3-ks3`, branched from origin/main at 8a10c7809). Every lane owns disjoint files
(different `ks3_data/<unit>/questions_*.py` files) so there is no collision risk as long as you
touch ONLY the files named in your own task. Do not touch `ks4_data/**` at all — a separate session
owns KS4. Do not touch any `ks3_data/<other-unit>/` directory. Do not run `git commit` or `git push`.
Nobody is available to answer questions during this run — if you hit an ambiguous call, make the
reasonable decision yourself, note it in your final report, and continue; do not stop and wait.

Read `docs/mrb338/authoring-brief.md` in full (all of §1–§9, especially §9.11) before writing
anything. What follows is a condensed restatement of the parts that have cost a night each when
missed — it does not replace the brief, it is here so you don't have to hold all of it in working
memory while also authoring.

## Row shape

```python
{
    "id": "<unit-lower>-<lesson-NN>-<band-letter><NN>",   # e.g. "b1-01-e10"
    "band": "easier" | "standard" | "harder",
    "text": "...",       # the stem — a full question, no "look at the diagram", no page references
    "options": [
        {"text": "...", "correct": True},                     # the key: NO "why" key
        {"text": "...", "correct": False, "why": "..."},       # every distractor has "why"
        {"text": "...", "correct": False, "why": "..."},
        {"text": "...", "correct": False, "why": "..."},
    ],
    "figure": None,
}
```
Exactly 4 options, exactly one `correct: True`. The key never carries a `"why"`.

## Append-only, frozen window (brief §0, §9 check 9)

- **`bank_position` 0–11 (i.e. the leaf's first 12 rows overall, across all bands as originally
  authored) are frozen** — every automatic assignment ever drawn from this leaf came from there.
  Never edit, reorder, or delete an existing row. You are ADDING rows only.
- New rows go at the END of the `QUESTIONS` list (or grouped sensibly by band if the file already
  groups by band — follow the existing file's convention, just never insert before an existing row).
- **Continue each band's id sequence from the leaf's current maximum.** If a leaf's easier rows run
  `e01…e09`, your first new easier row is `e10`. Never reuse or renumber an existing id.
- Never write an id numbered at or below an existing maximum in that band.

## The 6-character length-margin rule (brief §6, §9.1) — exact measurement

Do not eyeball "does the key look long." Measure exactly like the gate does:

```python
MARGIN = 6
visible = correct = 0
for q in rows:
    lens = sorted((len(o["text"]) for o in q["options"]), reverse=True)
    if lens[0] - lens[1] < MARGIN:
        continue                      # no visibly-longest option — not counted
    visible += 1
    if len(key_text) == lens[0]:
        correct += 1
# aim: 100 * correct / visible <= 32, across margins 3-10, not just margin 6
```
**32% is the ceiling on visible sets.** Sweep margins 3–10, not just 6 — the gate does, and a leaf
that only looks clean at margin 6 is not clean.

Also check the MIRROR direction (this is the exact defect night 3's repair lane is fixing on old
rows — do not reintroduce it in new rows): the key must not be disproportionately the SHORTEST
option either. Use the same formula with `lens` ascending and check `lens[1]-lens[0] >= MARGIN`
for "visibly shortest." Keep this in the same healthy range as the longest check — roughly 20-32%,
never concentrated above ~35%.

⚠️ **This has gone wrong in practice, repeatedly, on the first night-3 wave — do not treat it as a
formality.** The failure mode: when you write a KEY, it's naturally a concise, precise statement of
the correct fact. When you write a DISTRACTOR, the temptation is to make it sound plausible by
adding elaboration — which makes distractors longer than keys as a matter of habit, not by design.
Measured leaves came in at 45-65% "key is shortest" despite the author believing they'd checked for
it. **Do not just check this once at the end and hope it's fine.** Measure it after every 10-15 rows
you write, not only at the very end — catching a drift early costs a few edits; catching it after 60
rows costs a rewrite of a third of them. If you notice yourself writing a short punchy key against
three longer explanatory distractors more than once or twice in a row, stop and vary it: on some
rows, let a distractor be the short one (a wrong-but-plausible short claim) and let the key be more
fully stated. The KEY's own length should vary row to row — sometimes short, sometimes long —
independent of correctness; that's what makes both the longest-tell and the shortest-tell measures
land near chance.

## Key length-rank and position spread (brief §6)

- Across a band's rows, the key must not hold more than 40% of positions in any single length-rank
  (1 = longest of the 4, down to 4 = shortest).
- The key's INDEX in the `options` list (0–3) must be spread roughly evenly across a band — don't
  put the correct answer at index 0 (or any one index) disproportionately. No index left unused.

## Distractor rules (brief §9)

- **§9.2 — all options at the key's level of detail.** Never trim or pad the key. Never cram
  justification into an option's `text` — reasoning belongs in `why`, never in the visible option.
- **§9.7 — all four options from the same hand.** Nothing about shape, register, grammar, or length
  should mark one option out as different in kind from the others. No short flat key against three
  long reasoned distractors (or vice versa).
- **§9.9 — distractors are unarguably wrong.** Not defensible, not creditable, not "wrong only in
  this leaf's framing." If a distractor is wrong, a competent examiner would agree it's wrong with
  no argument.
- **§9.6 — a stem never states another row's key.** Before finalising a lesson, check your own new
  stems against every key in the leaf (old and new) — don't have a stem casually assert a fact that
  is itself the answer to a different row.
- **§9.10 — no page references.** Every stem must be answerable having only read the lesson's prose,
  not "the diagram", "the graph above", "the picture." Never write a literal `\n` or `<sub>` in
  question text.
- **Chemical formulae are stored FLAT, always** (CLAUDE.md, MRB-302) — write `CO2`, `H2O`, `Fe2O3`,
  never a Unicode subscript character. This applies to every KS3 chemistry file without exception.
  `sci()`/`formulae()` render the subscript at DISPLAY time from the flat stored string; a bank row
  that hand-writes a subscript breaks that pipeline. Match whatever convention the file's own shipped
  rows already use — it will be flat.
- **§9.11 — absolutes must not mark the wrong answer.** "always / never / only / at all / genuinely
  / truly / actually" must not appear in distractors at a rate meaningfully above chance relative to
  keys. `mrb338_leafcheck` check 10 flags a leaf above 85% (on n ≥ 12 occurrences). If a claim
  genuinely turns on an absolute, it's fine to use one — just don't let the PATTERN become "absolute
  word ⇒ wrong option."

## Duplicate / cross-row sweep (brief §9.4–9.5) — WHOLE UNIT, not just one leaf

- No two rows in the unit (across all its lessons) share a normalised stem.
- No two rows share all four options.
- No stem pair in the unit has Jaccard similarity ≥ 0.60 (on stems with ≥10 tokens) — i.e. don't
  paraphrase the same question twice across two lessons in the unit.
- If two lessons in your unit would both naturally want the same easy factual row (e.g. a shared
  unit-conversion fact), only ONE of them may own it — write it once, and write something else for
  the other lesson's slot.
- **Run `python3 tools/mrb338_leafcheck.py --unit <UNIT>` (whole-unit, no `--lesson`) before you
  consider the unit done** — this is the only check that sees cross-leaf collisions inside the unit.

## Drafting method (brief, "draft blind then check")

Draft each lesson's new rows without re-reading that SAME lesson's existing rungs while composing
(so you're not just rephrasing what's already there), then afterward check your drafts against the
lesson's own rungs to confirm no duplication and consistent register/difficulty banding. Never reuse
a lesson's own existing task/scenario verbatim for a "new" row.

## Quantities (brief §4)

Any core physical/chemical quantity referenced (temperature, energy, pressure, speed, etc.) must use
the definition already established in `ks3_data/quantities.py` — import it, never retype a
definition that lives there. Check that file before writing a definitional row.

## Register

Match the existing lesson's register and reading age — KS3, plain English, no jargon introduced
without having been taught in that lesson's own prose (read the lesson's content file, not just its
existing questions, to know what vocabulary is fair game).

## Per-lesson and per-unit self-check, before reporting done

1. Per lesson: `python3 tools/mrb338_leafcheck.py --unit <UNIT> --lesson <lesson-slug>` — must exit 0.
2. Per unit (once all lessons in your unit are done): `python3 tools/mrb338_leafcheck.py --unit <UNIT>`
   — must exit 0. This is the cross-leaf sweep; do not skip it.
3. `tools/mrb338_land.sh --unit <UNIT> --lesson <lesson-slug> -- <file>` per lesson (check
   `tools/mrb338_land.sh --help` for how it wants multiple lessons in one unit passed, and use that
   form for your final combined run covering every file you touched). **This does not commit** — it
   runs the 8 gates and reports; a human commits afterward. If any gate is red, fix and re-run. Never
   weaken a gate.

## What to report back

Per lesson: rows added per band, final counts per band, any notable content decisions. Confirm the
whole-unit `mrb338_leafcheck` and the combined `mrb338_land.sh` are green. Flag anything you're
unsure about (a science point, an ambiguous call) rather than silently guessing past it — note it,
make the reasonable call, and continue. `git diff --stat` at the end so the commander can see exactly
what's ready to commit.
