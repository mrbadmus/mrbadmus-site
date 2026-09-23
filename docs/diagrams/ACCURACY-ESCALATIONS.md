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

## E4 · The worksheet concurrency ceiling was sized without diagrams in it

**Not a defect — a threshold that a measurement has now outgrown.** Flagged
rather than changed, because the right value is an operational call.

Measured on this machine, cold process, PDF with answers page:

| questions | no figures | with figures | delta |
|---:|---:|---:|---:|
| 200 | 101.1 MB | 119.6 MB | +18 MB (+18%) |
| 1,450 | 191.3 MB | **291.1 MB** | **+100 MB (+52%)** |

The growth is NOT the raster cache — that is bounded by the figure catalogue
(tens of distinct ids) and is why the cache exists. It is the PDF document
itself: output grew 379 KB → 696 KB, and PDFKit buffers pages until the
document is finalised. So it scales with question count, exactly the axis the
existing guard was sized along.

**Why this needs Mide's call.** The guard
(`MRB_WORKSHEET_LARGE_THRESHOLD=200`, `MRB_WORKSHEET_MAX_CONCURRENT_LARGE=2`)
was measured at MRB-342.2 on Render Starter (512 MB): peak 326 MB at N=1 and
331 MB at N=2, for 1,450 questions with **no image work in the pipeline at
all**. This machine measures the same no-figure case at 191 MB, so Render's
baseline sits roughly 135 MB above mine and the two sets of numbers cannot be
compared directly.

What CAN be carried across is the delta. If diagrams add ~100 MB per large
render on Render too, then N=2 moves from ~331 MB to roughly **530 MB — over
the 512 MB limit.**

⚠️ That is an extrapolation, not a measurement. It should be measured on
Render before it is trusted, and it is the reason this is written down rather
than acted on.

**Recommended, not applied:** lower `MRB_WORKSHEET_MAX_CONCURRENT_LARGE` to 1,
or `MRB_WORKSHEET_LARGE_THRESHOLD` below 200, until a real Render measurement
exists. Both are env-tunable precisely so this is a dashboard change and a
restart rather than a deploy — which is why the right move now is to hand Mide
the number, not to pick one.

⚠️ Note the failure mode is not a crash a test would catch: it is an OOM under
concurrent load, on the largest real scope, at the moment several teachers
print at once.
