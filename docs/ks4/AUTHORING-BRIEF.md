# Writing a KS4 lesson — the brief every author works from

⊕ **Superseded 2 Oct 2026 (Mide's ruling, 2 Oct 2026).** This brief was Code's
authoring brief under the 1 Oct 2026 ruling. It records how batches 2 and 3
were written and is no longer used to author lessons. From batch 4, Design
authors from the batch's pack, and her brief is the pack's
`DESIGN-BRIEF.txt` plus `docs/ks4/architecture.md`'s two 2 Oct amendments
("Design writes the KS4 lessons again" and "four lesson rules"). Kept below
unmodified as the record of batches 2 and 3.

## 2 Oct 2026 — the four lesson rules

See `docs/ks4/architecture.md`'s "Amendment, 2 Oct 2026 — four lesson rules
(Mide)" for the full text. In one line each:

1. "Start here" is a two-option guess, not a four-option test.
2. Equations are shown as formula triangles you can cover.
3. Teach every step before you test it.
4. Practice is the same size in every lesson.

Rule 2 (formula triangles) must be in every Design brief.

---

Since Mide's ruling of 1 Oct 2026, Code writes the KS4 lessons. This is the
brief each lesson author follows. It is binding together with
`docs/ks4/architecture.md` (the ten laws, the families, the CFIFA amendment),
`docs/redesign/architecture_v2.md`, `docs/redesign/content_standards.md` and
`docs/redesign/council_bonding_review.md`. Where they disagree, the
architecture wins.

## 1. The template is the pilot

Read at least three pilot lessons in full before writing a line, including
one from the same subject and one from the family you are writing:
`docs/ks4/design-reference/pilot/KS4 Lessons/Pilot - Bonding and Electricity/`.
Also read the eleven block files (`Ks4*.dc.html`), `ks4-lib.js` and
`ks4-diagrams.js` there, and `docs/ks4/design-reference/pilot/DEPARTURES-PILOT.md`
(every science fix the examiners made to Design's pages — do not repeat them).

Write in the same `.dc.html` format: template inside `<x-dc>`, a `Component`
class in `<script type="text/x-dc" data-dc-script>`, the same blocks, the same
`ks3-*` classes and `--ks3-*` tokens, the same inline-style idiom, the same
section ids (`s-hook`, `s-ladder`, `s-keynote` …). Do not invent a new look.
A new instrument is allowed when the topic needs one; build it in the lesson's
own template + logic (or as a helper in the batch's `_ext.js`), from the same
tokens and components, and list it in your notes.

What the pilot does that you must not copy: the Route `<select>` and its
label (one route per URL — leave them out), the `Draft` banner text (the
build sets `showDraft`), any hard-coded "Combined · Triple" / "Foundation ·
Higher" pill that is not true for your lesson's routes.

## 2. Route layers

One file serves all four routes. Tag an element `data-route="higher"`
(CH, TH), `data-route="triple"` (TF, TH) or `data-route="triple-higher"` (TH).
The build removes it from other routes and adds the badge. The tag comes from
the AQA specification's own **HT** and **"Physics/Chemistry/Biology only"**
labels — look it up and cite the section in your notes. Never from the old
route copies, which drift. Higher material sits inline where it belongs, never
as a box of leftovers at the end. Content AQA says is base is never hidden
from Foundation.

Ladder rungs and the practice bank come from the verbatim route quizzes via
`K.find(slug, R.route, '<needle>')` and `K.bank(slug, R.route)`, as in the
pilot. A rung that must differ by route chooses by `R.route` in logic.

## 3. Science safety

Source: `docs/ks4/packs/<batch>/<file>.md` (verbatim live data) plus that
batch's `EXAMINATION.md` (the examiner's verdict on every point, its true
route, and what is wrong in the frozen items).

- **Verbatim, never edited:** quiz questions and their wrong-answer
  explanations, the examiner tip, the FIFA worked examples (four steps word
  for word — CFIFA puts a Convert step in front), equations, RP data. A
  frozen item the examiner marked wrong for a route is kept verbatim and
  listed in your notes; do not use it as a ladder rung on that route.
- **Re-cut:** theory prose — into explainer blocks of ≤150 words. Delete any
  paragraph an instrument now teaches.
- **New** (hook, predictions, instrument copy, misconception confrontations,
  ladder marking points, levels descriptors): every claim must trace to the
  frozen text or to a cited AQA spec section. Write from the spec and AQA
  mark-scheme conventions. Mark net-new science-bearing items `⚑` in notes.
- `docs/ks4/findings-for-mide.md` rulings carry in: Pythagoras resultants HT
  and Physics-only; area under a v–t graph HT; Ee = ½ke² HT; F = Δp/Δt
  Physics-only (HT); transformer equation HT and Physics-only; E = F/q, rms
  and "deposition" not in AQA; pV = constant HT (Physics-only). Teach each at
  its true layer or drop it, citing the spec.

## 4. The lesson, in order

Fixed start: lesson head (spec ref, `<h1>`, the big question, honest route
pills, the equation-sheet link on physics) → hook with a commitment
(`Ks4Choice`) within ~150 words → video slot (`Ks4Video`).

Middle, by family (architecture §families): explain → do cycles, ≤150 words
of prose before every commitment, ≤~700 words of body prose in total. One
flagship instrument (L), one or two mid-size activities (M), micro-widgets as
needed. Instruments sit where their idea peaks. Every reveal is predict-gated.
Motion is animated; reduced-motion gets the instant swap.

Must appear somewhere in the middle:
- **Misconception confrontation** at the moment the error is born — the
  source's `common_mistake` reborn as spot-the-flaw or a predict-trap, three
  beats (the mistake as the pupil says it → why it is wrong → the correct
  version).
- **Command words** taught as vocabulary where the lesson's ladder uses them.
- **CFIFA** (`Ks4Cfifa`) wherever there is a calculation: the source's FIFA
  examples verbatim with a Convert step in front ("Nothing to convert" or the
  conversion), plus two worked examples (one with nothing to convert, one
  with a unit to convert — g→kg, kJ→J, mA→A, min→s, cm→m) and two
  write-it-out attempts each opening with the convert decision. Foundation
  and Higher numbers must differ where tiers differ (content standards §2).
- **Required practical** block where AQA names one: method, variables, risks,
  a simulation that produces messy data, and its data processing through
  CFIFA. Name the RP by its Combined and separate-science numbers.
- **Equation** blocks label each equation "On the sheet" or "Learn it"
  (check the AQA physics equation sheet; chemistry/biology equations are all
  learn-it).

Fixed end: exam tip (the approved `examiner_tip`, text unchanged, just above
the ladder; omit the slot if the subtopic has none — never write one) →
`Ks4Ladder` (four rungs, all scored: ① recall 1 mark ② apply 2–3 marks with
units ③ explain as a chain with red herrings ④ a 4- or 6-mark extended
response with marking points or a levels-of-response descriptor, every rung
showing tariff and AQA command word) → `Ks4KeyNote` (the source key note,
cover-and-recall) → `Ks4QuizBank` → `Ks4End` (prev/next/connects are
filled by the build; tutor line; a short honest `legal` line about any
model simplification your instrument makes).

## 5. Quality bar

- Mide's standing rule: **no redundant text on any page.** Every label,
  caption, count and helper line carries information the pupil cannot
  already see. Write for a 15-year-old on a phone.
- Law 10: name each activity's demand and check it delivers it. No answer
  visible in the question; no sort solvable by word shape; every distractor a
  named misconception with feedback that corrects it; option lengths at
  parity.
- Two lessons with the same block line-up only if the content needs it.
- Works at 390 px, light and dark, by touch and keyboard (real `<button>`s,
  Enter/Space, visible focus), zero console errors.

## 6. What you hand back, per lesson

1. `ks4_lessons/authored/<batch>/<slug>.dc.html`.
2. The lesson record in `ks4_lessons/<batch module>.py` (fields in
   `docs/ks4/batch-engine.md`).
3. `docs/ks4/packs/<batch>/notes/<slug>.md`: family and why; flagship and
   mid-size activities and the demand each trains; the misconceptions and
   where each is confronted; every route tag with its spec citation; every
   ⚑ net-new science item; frozen items flagged wrong and how you handled
   them; any new instrument or helper.
