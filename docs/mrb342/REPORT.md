# MRB-342 · The printable worksheet, and Set work across several topics

**Backend LIVE on production 12 Sep 2026.** Site half built, reviewed and
driven; **not yet merged** — see §6.

---

## 1 · What shipped to production

`POST /api/teacher/worksheet` — a teacher picks questions in Set work and gets
them as a PDF or a Word document, with or without an answers page.

Backend commit `ddaa639`, pushed to backend `main`. Verified live three ways,
because one of them is not enough:

| check | result |
|---|---|
| `/api/health` build sha | `ddaa6391dbb10c4dc8684c531bc65ee50cd4873c`, branch `main`, `db: ok` |
| behavioural — `POST /api/teacher/worksheet` | **401**, not 404: the route exists and is auth-gated |
| regression — `POST /api/teacher/set-work` | **401**: still present |

⚠️ **The behavioural probe is not ceremony.** The first attempt returned **404
while `/api/health` was still reporting the OLD sha `e4fc690`** — the deploy
landed between the two calls. Had I checked health alone at that moment I would
have concluded the deploy failed. `/api/health` cannot prove which build is
serving; a route's own behaviour can.

## 2 · How it is sealed

It **delegates rather than re-implements**: the same `setWorkAccess` and
`setWorkContent` that `POST /api/teacher/set-work` calls — verified at both
call sites by an adversarial reviewer, not taken on trust.

- **Pathway is unreachable from the body.** `validateBody`'s output has no such
  field. Proved, not asserted: a crafted request naming a pathway produced a
  **byte-identical** document.
- **`subject` from the body cannot widen anything** — it is a filter *over*
  `treeForClass(cls)`, so a Biology-only class asking for physics gets zero hits.
  This was the reviewer's best hypothesis for a hole and it failed.
- **Pool ownership sealed** — `ks3_assignment_bank` / `ks4_assignment_bank` only.
- **Nothing is written to `assignments`.** A download is not a set.
- A question that does not exist and one that exists but was never offered
  return the **same** refusal — distinguishing them confirms a question exists.
- Rate limited 30/hour, keyed on the authenticated **user**, not the address.

**Verdict of the review: safe to merge.** On the question that matters — can a
teacher obtain questions for a class or tier they were never offered? — **no**,
attacked from five directions.

## 3 · Multi-scope Set work

A teacher can pick from several curriculum nodes in one set. One assignment per
class carries all the questions; the scope fields hold the first scope.

⚠️ **This was a gap I created by under-briefing.** The ruling says setting work
with several scopes writes one assignment carrying all picked questions, and I
briefed the backend lane on the worksheet route ONLY. The sheet learned
multi-scope; the backend did not. The site lane caught it independently, built a
compatibility shim (posting both the new `scopes[]` and the old flat fields so
an un-updated backend writes yesterday's row rather than a null one) and flagged
the assumption. Without the backend half, a two-topic set would have silently
recorded only the first topic.

**The single-scope path is proved byte-identical** to what it wrote before —
all 24 assignment columns, every `assignment_questions` row, and the audit
payload — because every new behaviour is gated on `scopes.length > 1`.

⊕ **Deviation, deliberate:** the audit payload lists `scopes` only when there is
more than one. A one-element list on every set would rewrite the journal shape
for every set written since MRB-335, contradicting the byte-identical
requirement.

## 4 · Subscripts — the ruling, and why it is not what the brief literally said

The brief said "formulae rendered with subscripts". **CLAUDE.md deliberately
excludes KS4 from the subscript pass** because there `N2` means Newton's second
law and `F2` the second filial generation.

So the worksheet **renders the characters as stored and applies no conversion in
either direction.** KS3 bank rows already carry real `₂`; KS4 stays flat. The
fix is to make the FONT capable, not the text different — DejaVu is bundled
(1.4 MB, committed) because PDFKit's built-in Helvetica is WinAnsi-encoded and
cannot draw U+2082 at all.

Proved end to end: a **real** KS3 bank row's U+2082 survives database → pool →
embedded font, verified by inflating the PDF streams and parsing the font's own
`/ToUnicode` CMap. A KS4 stem is asserted flat after the same decode.

## 5 · What the review and the fix pass found

- **A malformed RFC 8187 `Content-Disposition`.** `encodeURIComponent` leaves an
  apostrophe unescaped and the apostrophe is that header's own delimiter — and
  **nine real curriculum node names carry one** ("Newton's Laws of Motion",
  "Springs and Hooke's law"). Found by walking all 507 nodes. Fixed, six
  assertions pin it.
- **Four assertions discarded a query `error`** and could pass on data never
  read — including **both teardown re-queries**, so the proof that TEST was left
  clean was itself measured by queries that never ran.
- **`fontkit` and `jszip` were undeclared.** A missing `fontkit` made the
  glyph-coverage proof **SKIP** while the suite still exited 0 — the one
  load-bearing subscript assertion could vanish silently. Now declared, and a
  missing one fails rather than skips.
- **The page-break comment overclaimed.** Measured across all 9,348 rows of both
  banks: usable page 713.9 pt, tallest real question block **203.0 pt — 28.4%**.
  A block would need ~3,000 characters to outrun the guard. The comment now says
  what is true.
- **The page-break assertion was mutation-tested** — the guard stripped, the
  test correctly reported `q19 lost options A–D`. It kills the mutant.

**711 assertions, 0 failures, 0 skipped.** TEST confirmed from the service key's
own JWT `ref` claim (`qeppkiswvclkkwbxmlok`), never from a label.

## 6 · What has NOT shipped, and what is open

⊕ **Superseded in part, 13 Sep 2026 — see §8.** The first two bullets below are
kept rather than deleted because they are the reason §8 exists, and because
each named a thing that turned out to be BROKEN the moment it met real bytes.
The third is now done.

- **The site half is not merged.** Sheet UI, multi-scope state, `Add topic`,
  `Download` on the sheet/row/marking screen, and the four MRB-340 tidy-ups are
  built and driven (52/52 at 390px and 1280px, 13/13 on the real fixture, 6/6 on
  the edit path) — **but only against a STUB backend.**
- ⚠️ **Blob handling, `Content-Disposition` parsing and the `<a download>` save
  are untested against real bytes.** The stub returned a Blob and the save path
  did not throw; that is not the same as a PDF landing in Downloads.
- ~~**`pool_ownership`'s `SET_WORK_READERS` needs the worksheet route added.**~~
  Done, 13 Sep — and with a positive assertion rather than just a name; see §8.
- **`Set by <first name>` resolves only for the signed-in teacher's own sets.**
  `assignments.set_by` is a profile id and a teacher has no RLS read on a
  colleague's `profiles` row. The line is ABSENT on a colleague's set — never
  "Set by" over a blank or a UUID, which is the right failure. A full fix needs
  a SECURITY DEFINER function. **OPEN ON MIDE.**
- **An edit is still single-scope** — `assignments` has one scope triple.
- **A pre-existing defect fixed in passing**: `Save` was permanently disabled on
  every RELEASED set, because `stepValid`'s "release must not be in the past"
  check had no `locked` guard. **MRB-336 §6's entire purpose — moving a deadline
  on work already out — did not work**, and nothing on screen said why.

## 7 · A gate defect this work exposed

`pool_ownership` failed on the new route with *"server.js reads ks3_cards"*.
The line it matched was a **comment** the worksheet route carries:

    // nothing else. Never the ladder mirror, never `ks3_cards`.

— documentation of the very seal the check enforces. The check tested the raw
file, comments included. **A check that cannot tell code from prose punishes the
documentation that prevents the defect**, which is the wrong incentive to build
into a seal. Comments are now stripped; string literals are not, so
`from('ks3_cards')` is still caught. Proven both ways.


---

## 8 · Driven for real, 13 Sep 2026 — and the three defects that found

§6's second bullet was right to be nervous — **four defects were waiting
behind it, three of them in code that had already been driven 52/52.** The sheet was driven against the
real `POST /api/teacher/worksheet` — this run's code, the build that is live on
production (`ddaa639`), run locally against TEST on a real signed-in teacher's
JWT, exactly as `set_work_drive.py` already runs every other Set-work route —
and the bytes that came back were opened and parsed. Chrome's own download
behaviour was armed at a directory, the real `Download` control was pressed,
and the file that landed on disk was read back.

**`set_work_drive.py`: 392 checks, 0 failed**, ~56 of them new here.

### 8.1 · Four defects, and none of them was reachable from a stub

**⛔ 1. `downloadAssignment` read `q.id`, which does not exist.**
`/api/class/current-assignment` serves a question as
`{ position, question_ref, band, rung, lesson_slug, unit_code, text, options }`.
There is no `id` on it. So the row's Download and the marking screen's posted
`question_ids: [null, null, …]` and were refused `bad_question_ids` —
**every download from an existing set failed, and said `Unavailable`.** A stub
accepts any body, so a body of nulls and a body of ids are the same request to
it; nothing short of the real route could tell them apart.

**⛔ 2. A multi-topic set could not be printed from its row at all.**
`assignments` holds ONE scope triple, so a two-topic set records only the first
topic (§3, by design). Posting all of its questions under that one scope asks
the worksheet route for ids the first topic's pool does not contain, and the
route correctly answers `questions_not_in_scope`. MRB-342 created this by
shipping multi-scope writes; §6 noticed the EDIT consequence and not this one.
Fixed by trying the stored scope first — so every single-topic set posts exactly
the body it posted before and its worksheet is unchanged — and falling back to
one scope per the questions' own `lesson_slug`, which the row read already
supplies. ⚠️ The fallback sends no `subject`: a KS3 set spanning chemistry and
biology stamps the row `chemistry`, and sending `chemistry` with the BIOLOGY
subtopic is `scope_not_for_class` — a second refusal, one further in, that only
a real tree could produce.

**⛔ 3. `set_subject` was an OBJECT, so the marking screen's Download was dead
— and so was a single-topic row's.** `shared/teacher-data.js` asked PostgREST
for the scalar column `subject` AND embedded `subject:subject_id ( id, name )`
**under the same name**. The embed wins, so `a.subject` came back as
`{ id, name }` and the Set-work subject column was dropped from the answer
entirely. That object travelled through `set_subject` into `MRB_WORKSHEET` and
into `downloadAssignment`, and `validateBody` refuses a non-string `subject`
with `bad_scope` — **400 every time, `Unavailable` every time.**

⚠️ **This one nearly escaped, and how it nearly escaped is the lesson.** The
first row-download check used the TWO-topic set, which takes defect 2's
fallback body — one scope per lesson, and no `subject` on any of them — so it
sailed straight past a bug that lives entirely in the subject the STORED body
carries. A green check about the ordinary case that only ever exercised the
rare one. `row_download_single` was added for the case the first check masked.

Fixed at the source (`set_subject:subject`, aliased, with the column and the
embed now distinct) and again at the boundary: `downloadAssignment` treats a
non-string `subject` as absent, so the next producer to get it wrong loses the
subject rather than the download. ⚠️ The two really are different facts —
`subject` is the SET-WORK subject the pool is scoped by, `subject_id` is the
SCHOOL's filing subject, whose name for a KS3 combined class is "Science" and
matches no node in any tree.

**⛔ 4. (Pre-existing, MRB-336) The Edit sheet showed five BLANK rows.**
`loadStoredQuestions` read the same serving route as if it spoke the POOL's
language — `q.stem`, options as strings, `q.correct_index` — and it speaks
`text`, option OBJECTS and a `correct` boolean per option. Measured in a browser
before it was touched: `n: 5`, every `stem: ""`. Fixed here because it is the
same root cause as defect 1, and pinned by three new assertions in
`check_edit_sheet` — which had passed all along, because it asserted that the
sheet NARROWS (read-only tier, no release chips, no Swap) and all of that was
true of a panel with no questions on it.

### 8.2 · What the real bytes proved that the stub could not

- A download writes **nothing**: `assignments` snapshotted by id and
  **re-queried** on the service key before and after — six times, on the sheet,
  on a two-topic sheet, on a row, and twice through the API.
- The PDF parses: page count, every question drawn once with its stem, four
  options each, an `Answers` page when `answers: true` and **no page beginning
  `Answers`** when false — and a shorter document, so the key is absent rather
  than unlabelled.
- **No question straddles a page boundary** — stem AND all four options on ONE
  page. Mutation-tested: with the guard stripped the check reports
  `q6: stem on page 1, 1 option(s) not on it` and `q19: … 4 option(s)`, and it
  passes on the healthy control.
- The .docx parses to the same question count, options as four paragraphs, key
  present/absent — compared **byte for byte**, since OOXML has no extractor to
  invent spacing.
- **A KS3 row's real U+2082 survives to the drawn text**, in the PDF and in the
  .docx, and all the way to the file saved on disk.
- **KS4 stays flat** — and the assertion is *verbatim round-trip*, not "no
  subscripts". Three KS4 rows legitimately carry an authored subscript in a
  subscripted VARIABLE (`T₂`, `p₁`, `n₁` in `particle-motion-pressure` and
  `sampling-techniques`), so "a KS4 sheet contains no U+2082" is a FALSE claim
  that would go red on correct data.
- The saved file wears the **server's** filename, not the page's fallback —
  proved with a title (`Café ₂ sheet`) whose two naming rules disagree, so
  `nameFromHeaders` is shown to have really read `Content-Disposition`
  cross-origin. ⚠️ `₂` arrives as `2`, not as a space: NFKD maps SUBSCRIPT TWO
  onto DIGIT TWO.
- Refusals: a teacher who does not teach the class (**in the same school**, so
  the school conjunct cannot pass it for the wrong reason) and a signed-in
  CHILD both get 403 and no document bytes — and **neither writes an audit
  line**, so the journal cannot be used to learn that a class exists.
- The audit line that IS written names the class, every scope, the count, the
  format, the tier and whether the key was on, and its total agrees with the
  sum of its scopes.
- The limit is **keyed on the user**: the teacher is 429'd at 30, and a second
  account calling from the same address in the same second is served with 29 of
  its own hour left.
- 390px and 1280px with the menu open: no sideways scroll.
- Six new strings, all six really drawn, and no seventh. ⚠️ The first version of
  that sweep read only elements with no children and so skipped `Answers`,
  which contains an inline `<svg>` tick — a check that would have reported five.

### 8.3 · Three harness artefacts, named, because each mimicked a defect

None of these was a product fault, and each first appeared as a red wearing a
product defect's name.

- **`pypdf` inserts a space at a kerning pair.** See §8.4.
- **Two downloads in one directory under the same filename.** The marking
  screen shows the class's NEWEST paper, which was the single-topic set the
  previous check had just saved — same title, same filename. Chrome wrote it
  straight over the existing file, `listdir − before` was empty, and
  `take_download` waited out forty seconds and reported "nothing landed" about
  a download that had completed. The marking check now gets a directory of its
  own.
- **Measuring the second scope's rows before its `/preview` answered.** The
  section is drawn as soon as the scope exists, so `Add topic` briefly shows
  two sections and one topic's questions. The check waited on the section and
  reported "two sections, and the same ten questions".

And one selection fault of the same family: the KS3 subscript scope was chosen
by "a lesson that has some", and `/preview` draws a SUBSET — so a lesson with
two subscript rows in ninety-six legitimately offered none, and the one check
MRB-302's KS3 half rests on went red for the draw. Candidates are now ranked by
density and walked until a preview really offers one; a new
`ks3_subscript_offered` check states that precondition out loud rather than
letting it be assumed.

### 8.4 · One thing about measuring a PDF, worth keeping

`pypdf` reconstructs words from the TJ arrays PDFKit emits, and PDFKit emits a
kern adjustment between the `T` and the `a` of "Tap" — which the reader takes
for a word gap and hands back as `T ap water holds…`. The glyphs on the page are
perfect. So a "verbatim" comparison against extracted PDF text must mean *every
character, in order*, not *every byte including spacing*; `squeeze()` in the
drive removes whitespace and nothing else, so `₂` and `2` stay different and
`CO2` still does not match `CO₂`. The .docx half keeps the strict comparison,
which is why both formats are checked rather than one standing in for the other.

### 8.5 · The seal

`pool_ownership` now names `/api/teacher/worksheet` as Set work's fifth surface
AND asserts positively that it reaches the pool through `setWorkContent` and
reads no bank table of its own. Mutation-tested: renaming that one call makes
the gate fail with the reason. `teacher_behaviour` is green (24 fixtures, 952
controls) after the `teacher-data.js` change, and `build_all.py` has been run.

### 8.6 · Still open

- **The marking screen's Word path is not driven.** `PDF` is pressed there and
  parsed; `Word` is wired by the same ruling tuple and the same helper, and is
  asserted only through the sheet's own menu. Named rather than counted.
- **The fallback body is a client-side repair for a database shape.**
  `assignments` records one scope triple, so a multi-topic set's own row cannot
  say what it was made from. The honest fix is a scopes table (or a JSON column)
  on `assignments`, at which point both the fallback and §6's "an edit is still
  single-scope" go away together. **OPEN ON MIDE** — it is a schema decision,
  not a lane's call.
