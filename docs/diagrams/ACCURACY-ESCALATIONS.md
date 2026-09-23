# Accuracy escalations — for Mide's gate, not for this run to decide

CLAUDE.md's Autonomy Contract item 2: **science/content accuracy — whether
GCSE science is correct, or whether AQA would credit a given answer — is
Mide's sole gate.** This run does not overrule it. Rows here are NOT repaired;
they are named, with the reasoning, and left exactly as they are.

---

## E1 · `ks4-circuit-symbols-h02` (FROZEN, pos 9, harder/foundation)

**Stem:** "Two students draw the sensing part of a fire alarm. Student A draws
a resistor rectangle with a diagonal line through it; student B draws a
resistor rectangle with two arrows pointing in towards it. Evaluate which
student is correct."

**Marked correct:** "Student A, because a diagonal line through the resistor
is the thermistor symbol."

**The problem.** On the AQA GCSE physics symbol sheet that is not the
thermistor:

| symbol | AQA component |
|---|---|
| rectangle with a **diagonal arrow** through it | **variable resistor** (rheostat) |
| rectangle with a line along it turning **up at the end** | **thermistor** |
| rectangle with **two arrows pointing in** | **LDR** (light-dependent resistor) |

So as written, the marked-correct option identifies the variable-resistor
drawing as a thermistor, and the distractor describes the LDR drawing as
"heat being absorbed" when arrows-in denote incident **light**. For a fire
alarm — a temperature sensor — the right component is a thermistor, and
neither student as described has drawn one.

**Why this matters more once a figure is attached.** The whole point of this
run is that the diagram is now SHOWN. Drawing the stem faithfully means
drawing a variable resistor and then marking "thermistor" correct — printing
the error rather than merely describing it. Repairing this row would require
changing the SCIENCE, which is (a) outside the frozen-window ruling, which
permits only a figure plus a reword that points at it, and (b) Mide's call,
not mine.

**Action taken: NONE.** The row is left byte-identical. It is excluded from
the repair set and recorded here. It is one of the 28 allowlisted ids, so
permission to edit exists — the reason for not editing is accuracy, not
permission.

**What Mide needs to decide:** whether the intended answer was the thermistor
(in which case the stem's description of student A is wrong and should become
the correct AQA thermistor symbol) or the variable resistor (in which case the
"fire alarm" framing and the explanation are wrong). Either way it is a
content change, which needs his ruling.

⚠️ This is a PRE-EXISTING defect. It was not introduced by this run, and it is
independent of the described-diagram fault — the audit flagged the row for
describing a picture, and this was found underneath while drawing it.

---

## E2 · Two bonding lesson-page quiz rows sit under a DIFFERENT freeze

**Rows:** `bonding/covalent-bonding#quiz7(higher)` (CONFIRMED) and
`bonding/states-of-matter#quiz11(triple_higher)` (BORDERLINE).

**The freeze.** `docs/redesign/architecture_v2.md` line 5 — a document whose
own header says *"Status: law for all bonding builds from Phase 0 onward"* —
states:

> "the 8 frozen science fields (`quiz`, `matching`, `common_mistake`,
> `key_note`, `theory`, `fifas`, `higher`, `triple_only`) are never edited —
> interactives are built *from* frozen science, and any net-new activity
> content is flagged ⚑ for Mide's examiner review."

Its scope is `BONDING_REDESIGN` in `bonding_redesign.py` — the twelve bonding
subtopics. Both rows above are in it.

⚠️ **This is NOT the same freeze as MRB-335's frozen window**, and the two are
easy to conflate. MRB-335 freezes `bank_position ≤ 11` in
`ks4_data/questions/**` — the assignment bank. This one freezes eight authored
content fields in `all_subtopics_*.py` — the lesson page. **Mide's 23 Sep
ruling covers the first and says nothing about the second.** Having permission
for one is not permission for the other.

**No gate enforces it** (`bonding_redesign.py` is deliberately unregistered in
`gate_registry.py`; the SHA checks were one-off port-time verifications). So
nothing would have stopped an edit here — which is exactly why it needed
looking up rather than testing.

**Action taken: NONE.** Both rows left byte-identical. The documented
precedent for a real defect inside a frozen field is *flag → ticket → Mide's
review → fix in its own pass*, set by `council_bonding_review.md`, which hit an
MCQ-craft defect mid-build and recorded: *"(Frozen content: flag, don't fix.)"*

**What Mide needs to decide:** whether the described-diagram repair may be
applied to these two under the same reasoning as the 23 Sep ruling. It is a
small extension of a ruling he has already made once, on a freeze that exists
for a different reason (protecting authored science from a presentation
build) — but it is his to make, not this run's.

### The other five lesson-quiz rows are NOT affected
`electricity/circuit-symbols#quiz2`, `electricity/direct-alternating-pd#quiz1`,
`forces/distance-time-graphs#quiz1` and `#quiz2`, and
`magnetism/magnetic-fields#quiz1` are all in `all_subtopics_physics.py`, none
is in `BONDING_REDESIGN`, and no written freeze covers them. They are repaired
by this run as ordinary content.

---

## E3 · `b1-03-e04` points at a figure the manifest cannot serve (pre-existing)

Found by `build_figures.py`, which warns rather than failing:

> WARNING — a question references figure `b1-cell-bench` (KS3 B1 /
> animal-and-plant-cells), but it is `kind='css-art'` / `status='drafted'`,
> not an SVG 'diagram' this manifest can serve.

**What this means.** `b1-cell-bench` is drawn with CSS on the lesson page, not
as an SVG a drawer emits. The manifest serialises SVG; a CSS-art figure has no
SVG form to serialise, so the id resolves to nothing at question time.

So `b1-03-e04` — *"In the drawing of a leaf cell the nucleus sits over at one
side, not in the middle. What has pushed it there?"*, `bank_position` 3, inside
the automatic composition window — **remains a landmine after this run.** It is
the same defect as §2 of the report: a stem that points at a drawing the pupil
is not shown. This fix does not reach it, because the figure it names is the
wrong KIND of figure, not a missing one.

**Why it is not repaired here.** `b1-03-e04` is not among the audit's 110
confirmed or 92 borderline rows — the audit's net never flagged it, because it
HAS a figure id and the audit was looking for stems with none. It is also not
on Mide's 28-id allowlist, and it sits at position 3, inside the frozen window.
**So this run has no permission to touch it**, and the hard line "no frozen row
outside the 28 ids changes by a single byte" is absolute.

**The fix when Mide rules on it** is small and already has all its parts: draw
`b1-cell-bench` as a real SVG drawer in `ks3_art/b1.py` (the kit primitives now
exist), set `status:"drawn"`, and the existing id keeps working everywhere —
the question row itself would not change by a byte, which may put it outside
the frozen-window problem entirely. That is worth checking before assuming a
ruling is even needed.

⚠️ **The warning is deliberately non-fatal.** Failing the build would block
every unrelated figure over one pre-existing content gap. It prints loudly on
every run instead, so it cannot be forgotten.

---

## E4 · Worksheet memory with diagrams — measured, and no change is needed

⊕ **Resolved.** Two earlier readings of this — one of mine, one from the
backend work — both recommended tightening the concurrency ceiling. **Both
were wrong, for the same reason: they measured a scenario that cannot
occur.** No change is needed. The reasoning is kept because the mistake is
easy to repeat.

### The two wrong readings, and why

**Mine:** I scaled a single-render delta as if concurrent renders stacked
additively. They do not — PDFKit's content-stream buffering dominates, and
MRB-342.2 had already found it does not stack. Going from one render to two
costs +38 MB, not +298.

**The second:** measured a worksheet where **every one of 1,450 questions
carries a figure**, got +157 MB, and recommended dropping
`MRB_WORKSHEET_MAX_CONCURRENT_LARGE` from 2 to 1. The measurement was sound;
the scenario is unreachable.

### The content fact that makes the measurement interpretable

Counted from the bank rather than assumed: **no leaf has more than 2
figure-bearing rows**, and there are 18 in all of KS3. A worksheet is scoped
to a topic or unit, so even the largest real scope carries a handful of
figures among its questions — not one per question. The KS4 circuit-symbols
cluster is the densest in the estate and tops out around 40.

### What it actually costs (this machine, cold, PDF, 1,450 questions)

| scenario | peak RSS | delta |
|---|---:|---:|
| no figures | 201.6 MB | — |
| **~40 figures — the realistic worst case** | **217.6 MB** | **+16 MB** |
| ~97 figures — generous | 227.2 MB | +26 MB |
| every question (synthetic, unreachable) | 358.5 MB | +157 MB |

**+16 MB on the largest scope anyone can actually print.** Against ~180 MB of
headroom at the configured ceiling, that is noise.

### One real memory bug was found and fixed along the way

`resvg`'s default is `font.loadSystemFonts: true` — it enumerates and loads
every font on the machine at first use, measured at **~210 MB of one-time
RSS** for a trivial SVG. It now loads only the bundled DejaVu faces the PDF
path already embeds: ~5 MB. That single fix is worth an order of magnitude
more than anything the concurrency ceiling could have bought.

### Verdict

**`MRB_WORKSHEET_MAX_CONCURRENT_LARGE=2` stays as it is.** Throttling
production to N=1 on the strength of an unreachable scenario would have made
printing slower for every teacher and bought nothing.

⚠️ The one thing worth re-checking later: if a future run gives most questions
in a dense topic a figure, the realistic case moves toward the synthetic one.
The number to watch is figures-per-worksheet, not figures-in-the-estate.
