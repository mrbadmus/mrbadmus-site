# KS3 Physics Audit — 28 Aug 2026 (MRB-294) — Shared Protocol

Twelve unit auditors, P1–P12, 70 live lessons. Every unit agent follows this
protocol exactly. The consolidated report is built from your record file — a
record that deviates from the shared format cannot be aggregated and wastes
your whole audit.

Model: the chemistry audit of 25 Aug 2026,
`docs/ks3/audits/2026-08-25-chem-audit/` — REPORT.md, PROTOCOL.md, and the
records. **Read REPORT.md and your equivalent chemistry record before opening a
single physics page.** You are reproducing its depth and its finding format,
and you are checking whether its systemic findings are present in physics too.

## Run constants (verified at run start — do not re-derive)

- Commit: `38fb338308d3a25f9cd6596afdbce20dc8af9921` (branch `feat/content-phys`,
  fast-forwarded to `origin/main`, tree clean).
- Live-vs-local parity: all **83** physics HTML files under
  `mrbadmus_site/ks3/physics/` are **byte-identical** to what mrbadmus.com
  serves (SHA-256, full sweep, 83/83). You may therefore drive the LOCAL copy.
- Lesson count from data: **70 lessons across 12 units** (matches the brief).
- Physics rows in `ks3_assignment_bank`: **0**. Also 0 in `ks3_ladder_questions`
  and `ks3_cards`. Out of scope — do not audit or re-derive; already in the
  preamble.

## Scope and safety (absolute)

- **Audit and report ONLY. No content fixes this run.** You never edit anything
  outside `docs/ks3/audits/2026-08-28-ks3-physics/`.
- Production content and database are READ-ONLY. No DDL, no writes, no
  `apply_migration`, no `supabase db push` (banned always). No sign-in, no
  accounts — lesson pages need none. Browse signed out.
- **DO NOT BUILD.** Never run `build_all.py`, `generate_site_v5.py`,
  `build_ks3.py`, `verify_ks3.py` or any gate. `generate_site_v5.py` opens with
  an rmtree, gates rebuild, and other sessions may be live.
- Never kill processes by name (`pkill -f chrome` etc.) — other sessions'
  processes match. `ks3_browser.Browser()` as a context manager cleans up.
- Anything trivially fixable is a FINDING, not a commit.

## What you audit

Your unit's lesson pages, as a student sees them. Live URLs are
`https://mrbadmus.com/ks3/physics/<unit-slug>/<lesson-slug>` (extensionless —
the `.html` form 308-redirects). Because parity is proven, drive the local
copy: identical bytes, faster, and does not hammer Cloudflare with twelve
headless Chromes. Also open the unit `index.html`.

## Browser harness

`ks3_browser.py` at repo root — stdlib-only CDP harness. From repo root:

```python
import ks3_browser as cdp
server, port = cdp.serve("mrbadmus_site")
with cdp.Browser() as b:
    p = b.page(f"http://localhost:{port}/ks3/physics/<unit>/<lesson>.html")
    p.eval("document.querySelector('...').click()")   # interact via JS
    errs = p.console_errors()
    p.screenshot("docs/ks3/audits/2026-08-28-ks3-physics/evidence/x.png", width=1280)
    p.screenshot(".../evidence/x-390.png", width=390)   # phone — true reflow
```

`width=390` genuinely reflows (device-metrics override, not window-size). Use
`p.eval` to press buttons, drag sliders (set `.value` + dispatch `input`/
`change`), answer ladder rungs (right AND wrong on purpose), reset mid-state
and reload mid-activity (`p.goto` again). Read DOM state back with `eval` to
verify what a press actually did. Check `console_errors()` on every page and
after interaction bursts.

## PHASE A — THINK DEEPLY, IN WRITING, BEFORE OPENING ANY PAGE

This is the instruction that separates this run from a checklist. In your
record file, under `## Pre-audit deep think`, write down for YOUR unit:

- the misconceptions a real KS3 class arrives with;
- the wrong mental models a well-meaning explanation can install;
- where AQA's language differs from everyday language;
- what diagrams of this topic usually get wrong;
- **which single sentence in this topic is most often taught wrong in British
  classrooms.**

Then go looking for those specifically, AND stay open to what you did not
predict. An auditor who opens pages first and reacts to what it sees will find
a third of what is there. Depth over speed. A page skimmed is a page not
audited.

Physics seeds — starting points, not the list:
- force arrows; contact forces and "the table doesn't push back"
- current "gets used up" going round a circuit; voltage as a substance
- energy STORES vs TRANSFERS (the AQA model) — do pages hold it, or slip into
  "types of energy"?
- weight vs mass; `g` used loosely
- speed vs velocity; distance vs displacement; average vs instantaneous
- simulations that behave perfectly while teaching the wrong model
- unit errors and unit sloppiness (N, J, W, Ω, m/s, per-second language)
- graph literacy — axes, gradient meaning, what a flat line means
- equation rearrangement, substitution, units carried through a calculation
- scale and magnitude — numbers that are right but meaningless to a child

## PHASE B — DRIVE EVERY LESSON AT READING PACE. BOTH PERSONAS, IN ORDER.

**Persona 1 — an average KS3 student (11–14, mid-class) on a 390px phone.**
Read every word top to bottom at the speed a child reads. Press every control.
Answer wrongly on purpose, then correctly, then leave things half-done and
reload. **Keep a FRICTION LOG per lesson**: every point where you had to
re-read a sentence, guess what was being asked, scroll back for something, or
would have given up. Friction is a finding, not a feeling — log it with the
exact sentence or control that caused it. Also: was anything boring enough to
abandon? Honest answer.

**Persona 2 — an AQA examiner (qualified science teacher's eye).** Re-read the
same lesson cold. Is it right? Is it in scope for KS3, and does it set up GCSE
honestly? Would this wording lose marks if a candidate repeated it? Are the
"at GCSE this becomes" statements accurate? Hunt: science errors; imprecision
that costs marks later; oversimplification past honesty; units, values,
diagram–text agreement; pitch (flag KS4-level demands, and places pitched so
low they bore); curriculum coverage of the slot; UK conventions and command
words; terminology consistent with the other eleven units.

## PHASE C — RUN EVERY SIMULATION AND INSTRUMENT TO ITS EDGES

Zero. Maximum. Negative where allowed. Rapid repeated input. Reload mid-state.
Does the caption still tell the truth at every edge? **A fixed caption on a
variable instrument is a lie waiting to happen** — chemistry found several.

Then the harder question: with the sim behaving correctly, **what model does a
child walk away with?** Correct behaviour teaching a wrong model is S1.

## PHASE D — MECHANICAL SWEEP

Console errors. Broken links, wrong next/previous targets, 404 assets. 390px
layout including header and brand. Accessibility: focus order, `aria-pressed`
agreeing with what is rendered, contrast, tap targets, meaningful alt text,
keyboard operability. Design-system conformance (`--ks3-ok` only for
marks/fills; amber only warning/loss; no retired branding — green octopus, ⚗️).
Dead controls. Visible garbage, `[object Object]`, build metadata reaching
students.

**SAFETY WORDING IS FLAGGED, NEVER REWRITTEN.** If a practical needs a safety
line and has none, or the line is inadequate, record it as a finding addressed
to Mide. Do not draft the wording. Safeguarding is his gate alone.

## PHASE E — TEST FOR CHEMISTRY'S SYSTEMIC FINDINGS ON PHYSICS PAGES

Test each explicitly and **report presence OR absence per unit — "not found" is
worth having.** Put these under `## Systemic probes` in your record.

- **SYS-1** — "Next in this unit" end-matter card pointing at the wrong lesson
  (backwards, cross-unit, or into another subject). Check the
  `connects_heading` in `ks3_data/p<N>/lesson_*.py` against the actual target.
- **SYS-2** — ladder kernel header announcing a finished verdict ("You got 0 of
  4…") the moment the FIRST rung is answered, mid-ladder.
- **SYS-3** — `.ks3-brand` header brand overflow at 390px, breadcrumb trail
  rendering on top of the wordmark.
- **SYS-5** — fixed instrument captions that lie at reachable edge states.
- **SYS-8** — answer tells in benches and hooks outside the MRB-278 gates
  (correct option longest/most qualified; chips rendered in a positional
  pattern; hooks outside the predict gate's reach).

## ALSO LOOK FOR THIS — Mide's additions

- **READING LOAD AND UNCLEAR WORDS.** Sentences too long or dense for the year
  group. Technical words used before they are defined, or defined once and
  assumed forever. Words whose everyday meaning differs from the physics
  meaning, used without warning — **work, power, energy, force, weight, moment,
  current**. Pronouns with no clear referent. **Quote the exact sentence.**
- **SCAFFOLDING GAPS.** A finished result shown with no worked route to it. A
  first practice item already harder than the worked example. A calculation
  with no fading (full example → partial → independent). No way back for a
  child who is stuck, only forward.
- **DEAD ENDS ON A WRONG ANSWER.** What actually happens when a student gets it
  wrong? Told *why*, or only *that*? Can they try again? Does the page ever
  leave a wrong answer standing uncorrected?
- **MISSING DRAWINGS.** Anywhere prose is doing a diagram's job — describing a
  circuit, a force pair, an apparatus, a graph shape, a wave in words. **Say
  what the drawing should show.** These go to the Design brief pile.
- **AI FAFF AND SLOP, hunted by name.** Meta-text explaining how the platform
  works (standing rule: cut entirely). Filler openers and hype — "let's dive
  in", "in today's lesson we will explore", "great job!" after nothing. Generic
  praise not tied to what the student did. The same sentence shape repeated
  down a page. Padding a child could skip. Lists of three where two would do.
  Hedging that avoids committing to the physics. Anything that reads as
  generated rather than taught.
- **CONSISTENCY WITHIN AND ACROSS UNITS.** Same quantity → same symbol, same
  units, everywhere. Same term for the same idea — not "energy store" here and
  "type of energy" three lessons later. Notation, decimal places and
  significant figures held steady.
- **ORDERING AND PREREQUISITES.** Does any lesson depend on something taught
  later? Does the unit's first lesson assume knowledge nothing has given?
- **TONE AND REGISTER.** Does it sound like a teacher who knows this class, or
  like a textbook? Anything condescending? Any analogy that would land wrong,
  date badly, or exclude a child?
- **THE THING YOU CANNOT NAME YET.** If a page makes you uneasy and you cannot
  articulate why, do not drop it. Sit with it, write down what you noticed, and
  file it with your honest uncertainty. Chemistry's worst find started as
  exactly that.

## Finding format — every finding, no exceptions

```
FINDING <UNIT>-<seq> · <lesson slug> · <exact location on page> · S1|S2|S3|S4
  What's wrong: <one tight paragraph>
  Evidence: <quote from the served page, and/or evidence/<file>.png, console output>
  Proposed solution: <specific, actionable — what it should SAY or DO>
  Who fixes: Code (standing authority) | Design brief | Mide ruling | Mide sign-off
  Effort: small | medium | large
```

- **S1** — science is wrong, or the page teaches a misconception. Includes
  anything a real classroom would contradict.
- **S2** — pedagogy: correct but taught badly, wrongly ordered, or leaving a
  child stuck with no way forward. Friction-log entries usually land here.
- **S3** — bug: broken, lying about state, or doing nothing.
- **S4** — polish: wording, layout, consistency, tone.

**Every finding carries a proposed solution.** "This is wrong" without "and
here is what it should say" is half a finding and Mide has said so. Findings
without evidence do not count.

**Science is NOT escalated.** You hold the national curriculum and have
standing authority: identify the error, state the correction, and check whether
the same error appears elsewhere in the estate — if it does, say where, in the
finding. Escalate to Mide ONLY: safety and safeguarding wording, brand
decisions, genuine product scope, money.

## Already ruled — DO NOT relitigate

- Flat formulae in question text — storage stays flat.
- No right-answer feedback line in v1.
- No meta-text on student pages — default is cut entirely (violations of the
  rule ARE findings).
- Covered-lessons scoping as it stands.
- Blanks over invented numbers. Counts from data, never literals.
- `is_correct` NULL means not machine-marked. It never means wrong.

EXCEPTION: a ruled item demonstrably causing OBSERVED HARM at a specific point
goes under a separate record heading `## Ruled items causing observed harm`,
with evidence. Input for Mide, not a defect claim. Do not argue the ruling.

## Record file — `records/p<N>.md`

1. `# P<N> — <unit title> — audit record`
2. `## Pre-audit deep think` — your written predictions, BEFORE any page.
3. `## <lesson-slug>` per lesson, in unit order: persona-1 walkthrough notes
   incl. the friction log, persona-2 notes, then its findings in the format
   above.
4. `## Systemic probes` — SYS-1/2/3/5/8, presence or absence, with evidence.
5. `## Ruled items causing observed harm` (if any).
6. `## Unreachable` — anything you could not reach/render/exercise, named
   honestly, with why. Empty section if none.
7. `## Evidence index` — every screenshot you kept, one line each, naming the
   finding it evidences. **PRUNE: delete every screenshot not cited by a
   finding.**
8. `## Counts` — your own tally: `S1=n S2=n S3=n S4=n TOTAL=n`, and lessons
   audited.

Evidence files: `evidence/p<N>-<lesson>-<short-desc>.png`. Keep them small
(PNG, no retina scale) and few — disk is shared across twelve agents and free
space is ~11 GB at run start. **If free disk falls below 5 GB, prune evidence
to thumbnails and keep going. Do not abort.** Check with `df -h .`.

Source-of-truth cross-checks are encouraged: authored content lives in
`ks3_data/p<N>/lesson_*.py` and `questions_*.py`; instruments and drawers in
`ks3_art/p<N>.py`. Reading them helps you verify what the page SHOULD say and
catch build-time mangling. **But the page as the student sees it is what you
audit.**

## Pre-ruled so the run never stalls

- Cannot reach a page → record under `## Unreachable` and continue. No other
  unit waits for you.
- Disk below 5 GB → prune to thumbnails, keep going, say so in your record.
- Do not mint ticket numbers. They come from chat only.
