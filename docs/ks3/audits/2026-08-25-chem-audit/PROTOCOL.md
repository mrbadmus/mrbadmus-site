# Chemistry Lesson Audit — 25 Aug 2026 — Shared Protocol

Every unit agent follows this protocol exactly. The consolidated report is built
from your record file — a record that deviates from the shared format cannot be
aggregated and wastes your whole audit.

## Scope and safety (absolute)

- **Audit and report ONLY. No content fixes this run.** You never edit anything
  outside `docs/ks3/audits/2026-08-25-chem-audit/`.
- Production content and database are READ-ONLY. No DDL, no data writes, no
  sign-in, no accounts. Browse signed out. If something demonstrably requires
  auth to exercise, record it under "unreachable" — do not create accounts.
- Never complete or submit anything attached to a real class.
- Do NOT run `verify_ks3.py`, `build_all.py`, or any generator/gate — another
  session may be live, gates rebuild, and this run is read-only.
- Never kill processes by name (`pkill -f chrome` etc.) — other sessions'
  processes match. `ks3_browser.Browser()` as a context manager cleans up its
  own Chrome.

## What you audit

The LIVE pages at `https://mrbadmus.com/ks3/chemistry/<unit-slug>/<lesson-slug>`
(extensionless — the `.html` form 308-redirects). Verified at run start: live
serves the committed build (`mrbadmus_site/`) with matching cache stamps.

**Per lesson, first prove live = local**: fetch the live page with
`curl -sL`, strip volatile noise if any, and compare against
`mrbadmus_site/ks3/chemistry/<unit>/<lesson>.html`. If they differ beyond the
redirect canonicalisation, RECORD THAT as an S3 finding (stale cache) and audit
the LIVE bytes. If identical, drive the LOCAL copy in the browser (serve
`mrbadmus_site/` with `ks3_browser.serve()`) — identical bytes, faster, and
does not hammer Cloudflare with ten headless Chromes.

## Browser harness

`ks3_browser.py` at repo root — stdlib-only CDP harness. From repo root:

```python
import ks3_browser as cdp
server, port = cdp.serve("mrbadmus_site")
with cdp.Browser() as b:
    p = b.page(f"http://localhost:{port}/ks3/chemistry/<unit>/<lesson>.html")
    p.eval("document.querySelector('...').click()")   # interact via JS
    errs = p.console_errors()
    p.screenshot("evidence/....png", width=1280)      # desktop
    p.screenshot("evidence/....png", width=390)       # phone — true reflow
```

`width=390` genuinely reflows (device-metrics override, not window-size). Use
`p.eval` to press buttons, drag sliders (set `.value` + dispatch `input`/
`change` events), answer ladder questions (right AND wrong on purpose), reset
mid-state, and reload mid-activity (`p.goto` again). Read DOM state back with
`eval` to verify what a press actually did. Check `console_errors()` on every
page and after interaction bursts.

## The protocol — every lesson, BOTH personas, in this order

**BEFORE opening any page in the unit: think deeply, in writing, in your record
file.** For this unit's chemistry: which misconceptions does the topic
classically breed, which models are hard to render honestly, which words trip
an 11-year-old, where could a simulation teach the WRONG model while working
perfectly. Then browse to test those predictions AND stay open to what you
didn't predict. Depth over speed. A page skimmed is a page not audited.

### Persona 1 — the average KS3 student (11–14, mid-class, phone as often as laptop)
Read every word top to bottom at reading pace. Run every simulation, press
every control — sliders to extremes, buttons twice, reset mid-state, reload
mid-activity. Click every activity and ladder question; answer some wrong on
purpose. Report the FRICTION:
- Where did understanding stall? Which sentence needs reading twice? Which word
  arrives before it's explained?
- Where does the lesson assume something a Year 7 hasn't met yet?
- Where is a wall of text doing a drawing's job? Where would one more worked
  example or scaffold step carry a struggling student over?
- Is each ladder question answerable FROM THIS LESSON? (Fairness is a defect.)
- Was anything boring enough to abandon? Honest answer.

### Persona 2 — the AQA examiner (qualified science teacher's eye)
Re-read the same lesson cold and hunt:
- SCIENCE ERRORS: factually wrong, imprecise in a way that costs marks later,
  oversimplified past honesty. Units, values, state symbols, diagram–text
  agreement.
- MISCONCEPTIONS: wording/diagram/simulation planting or reinforcing known
  wrong ideas — particles expanding when heated, dissolving vs melting vs
  disappearing, mass not conserved, bubbles "made of air", atoms "used up",
  weight for mass, chemical/physical blur. Test simulations against the model
  they IMPLY, not just whether they run.
- PITCH: right for KS3 and consistent? Flag KS4-level symbol equations or
  quantitative demands; flag places pitched so low they bore.
- CURRICULUM: does the lesson cover its slot's national-curriculum ground?
  (KS3.C.PT.06 is a KNOWN gap — don't rediscover it; note anything similar.)
- LANGUAGE: UK conventions — "sulfur" not "sulphur", UK spellings, correct
  command words, terminology consistent with the other nine units.
- SCAFFOLDING/DRAWINGS: name the exact place needing one more diagram/step/
  worked example — and say what the drawing should show, written as a Design
  brief.
- AI FAFF/SLOP: meta-text, filler, hedge-words, content-free paragraphs,
  chirpy summaries. The standing rule is "cut entirely by default" — report
  every survivor.

### Both personas — mechanical sweep
- Bugs: broken/inert controls, console errors, broken images, 404 assets,
  layout breaks, bar-cover-class defects, activities losing state on reload.
- Mobile at 390px: overflow, tap targets, finger-usable sims, legible text.
- Accessibility: contrast vs the design system, keyboard operability of
  interactives, meaningful alt text, focus states.
- Design system: `--ks3-ok` only for marks/fills; amber only warning/loss; no
  retired branding (green octopus, ⚗️).
- Safety wording wherever a practical/hazard appears — FLAG for Mide's
  sign-off, never propose a rewrite yourself.

## Already ruled — do not report as findings
- Flat formulae (H2SO4 not H₂SO₄) — deliberate mirror-consistency call.
- No right-answer feedback line in v1.
- The no-meta-text rule stands (violations of it ARE findings).
- (The old "c6-05 / C8 oxides ship as coming-soon" ruling is overtaken: both
  are authored and live — audit them as normal lessons.)

EXCEPTION: a ruled item demonstrably blocking learning at a specific point goes
under a separate record heading "Ruled items causing observed harm", with
evidence. Input for Mide, not a defect claim.

## Finding format — every finding, no exceptions

```
FINDING <unit>-<seq> · <lesson slug> · <exact location on page> · S1|S2|S3|S4
  What's wrong: <one tight paragraph>
  Evidence: <quote from the page, and/or evidence/<file>.png>
  Proposed solution: <specific, actionable>
  Who fixes: Code (standing authority) | Design brief | Mide ruling | Mide sign-off
  Effort: small | medium | large
```

S1 science error or misconception risk · S2 pedagogy (friction, pitch,
scaffolding, fairness) · S3 functional bug · S4 polish and slop.
Findings without evidence don't count; findings without a proposed solution
are half-findings.

## Record file — `records/<unit>.md`

1. `# <Unit code> — <unit title> — audit record`
2. `## Pre-audit deep think` — your written predictions (before any page).
3. `## <lesson code> <lesson-slug>` per lesson, in order: brief persona-1
   walkthrough notes, persona-2 notes, then its findings in the format above.
4. `## Ruled items causing observed harm` (if any)
5. `## Unreachable` — anything you could not reach/render/exercise, named
   honestly, with why. Empty section if none.
6. `## Evidence index` — every screenshot you kept, one line each, which
   finding it evidences. PRUNE: delete every screenshot not cited by a finding.

Evidence files: `evidence/<unit>-<lesson>-<short-desc>.png`. Keep them small
(PNG, no retina scale) and few — disk is shared across ten agents.

Source-of-truth cross-checks are allowed and encouraged: the authored content
lives in `ks3_data/<unit dir>/lesson_*.py` and `questions_*.py` — reading it
helps you verify what the page SHOULD say and catch build-time mangling. But
the page as the student sees it is what you audit.
