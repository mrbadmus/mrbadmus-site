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

---

## 8 · The rate-limit constraint, and a follow-up for the next product run

### 8.1 · `set_work_drive`'s rate-limit check cannot run twice in an hour

The worksheet route is limited to **30 downloads per hour per user**, and the
drive proves that by making a burst of calls until it is refused. That works
once. On a second run inside the same hour the bucket is already part-spent, so
the burst is refused early and the check fails:

```
❌  392 checks, 1 failed
    429 on call 15 of this burst (the drive had already spent part of the hour)
```

⚠️ **This is the limiter working, not a defect**, and the proof is the very next
check, which PASSED:

```
✅ worksheet_limit_is_keyed_on_the_user — a SECOND account calling from the same
   address, in the same second, is not refused: the bucket is the user, never
   the IP a whole school shares
   the second account was answered 200 with 29 of its own hour left
```

A fresh account has its full 30. The first account was simply spent — by **my own
repeated runs** (receipts at 14:45 and 15:53, plus a standalone drive).

**No override was written for it.** Ruled by Mide, 13 Sep: wait for the bucket and
re-record `set_work` alone. An override is a permanent line in `git log` asserting
a gate shipped red, and writing one for a self-inflicted 429 would put a false
claim in the history.

⚠️ **Anyone re-running this drive will hit this**, and the natural reading —
"the rate limiter is broken" or "the route is refusing valid calls" — is wrong in
the direction that wastes a night.

### 8.2 · FOLLOW-UP for the next product run (deliberately NOT in this tree)

> **Give the rate-limit checks a FRESH throwaway account per run**, so a re-run
> can never exhaust its own bucket and block receipts.

The drive already creates a throwaway world per run and tears it down by a
snapshotted id list; the rate-limit burst should draw on an actor from that
world rather than on the standing test teacher. Then the check is idempotent
across runs, which is what every other check in the drive already is.

⚠️ **Not done tonight, on purpose**: receipts are bound to a tree, and this
tree's receipts are already recorded. Changing the drive now would invalidate
them and cost another full slow-gate pass. It is a one-file change for the next
product run.

---

# 342.1 · Five corrections, so a teacher can hand the sheet out

**23 September 2026.** Mide reviewed the first real worksheets and found five
things wrong with them. All five are done. Backend landed first and is live;
the site half followed.

| # | correction | where it was fixed |
|---|---|---|
| 1 | `Multiple choice` and `Answers` are real checkboxes, keyboard and focus included | `shared/set-work.js` + `shared/set-work.css` |
| 2 | The header is the worksheet title and nothing else | `worksheet.js` — both renderers |
| 3 | The footer is the chevron mark only; "MrBadmus" appears nowhere, metadata included | `worksheet.js` — both renderers |
| 4 | Multiple choice off ⇒ ruled answer lines, except where the stem needs its options | `worksheet.js` — one server-side rule |
| 5 | Each answer is the key phrase plus the `why`; no bare option letters | `worksheet.js` — both renderers |

**Fixed where the document is built.** Nothing post-processes the output: there
is no pass over a finished PDF and no rewrite of a finished `.docx`. Every
change is in the two renderers or in the one model pass that feeds them.

## 342.1.1 · What shipped, and how the order was proved

| | |
|---|---|
| backend commit | `57f4345` — `MRB-342.1: a worksheet a teacher can hand out` |
| Render `/api/health` `build` | `57f434533defdb05e4c125dab2c615b850d5cf26` ✅ **matches**, branch `main`, `db: ok` |
| site commit | see §342.1.7 |

Backend first, and the health `build` sha checked **before** the site went
anywhere — the site's only new outbound fact is a `multiple_choice` boolean,
and a site that sent it to a backend that did not yet know the field would have
had every download refused with `bad_multiple_choice`.

⚠️ **Both halves default the flag to TRUE**, which is what makes the ordering
merely correct rather than critical: an old site talking to the new backend
sends no flag and gets exactly the file it got yesterday.

## 342.1.2 · Correction 1 — real checkboxes

They were `<button role="menuitemcheckbox">` elements carrying an inline SVG
tick. That *looks* like a checkbox and behaves like one only for as long as
somebody keeps writing the behaviour by hand — and the keyboard half had never
been written at all.

Both are now `<input type="checkbox">` inside their own `<label>`. Space
toggles them, Tab reaches them, a screen reader announces a checkbox with a
state, and the browser draws the focus ring.

⚠️ **The menu ARIA roles came off with them, and that is part of the fix.** A
native checkbox inside `role="menu"` is a contradiction: the menu pattern owns
the arrow keys and expects `menuitemcheckbox` children, so a real checkbox in
one is announced as a menu item that is also not a menu item. The panel is now
an ordinary labelled group, which is what it always was.

⚠️ **No `appearance: none`.** What a teacher sees is their own platform's
checkbox — already correct in light and dark, already finger-sized on iPadOS.
`accent-color` tints the checked fill to the sheet's orange and is the whole of
the styling.

The drive proves the shape, the state and the keyboard, and the keyboard proof
needed a real key: **a JS-dispatched `KeyboardEvent` would have proved nothing
and failed**, because a browser runs no default action for an untrusted event —
the box would not have toggled and the check would have reported a dead control
that is in fact perfectly alive. It presses Space through CDP
(`Input.dispatchKeyEvent`), down-char-up, because Chrome activates a checkbox on
the key *up*.

`Multiple choice` is a seventh word on RISKS A9's allowed list, beside
`Answers`. There is deliberately no eighth for correction 4's exception: a
control that said "mostly" would be a control a teacher has to think about, and
the sheet is right either way.

## 342.1.3 · Corrections 2 and 3 — the header, the footer, the metadata

The header carried a second line: `10X1 Biology · Higher · 12 September 2026`.
Every part of that was a fact about the **request** rather than about the sheet,
and each was wrong in a way a teacher would have to explain away — the class
name is the class the questions were drawn *for*, the tier is the teacher's own
filter, and the date is the day the file was made rather than the day the work
is due. A sheet printed in September and used again in March should not argue
with itself. The rule under it went too; the title is now the only thing in the
header.

The footer said `MrBadmusAI` on the left and `Page 1 of 3` on the right. It is
now Claude Design's `BrandMark` alone, centred: the right-pointing double
chevron in `#E4572E`, leading chevron solid, trailing chevron at 34%.

⚠️ **The geometry is copied, not redrawn.** These are the exact two paths of
`_C_BRANDMARK` in `generate_site_v5.py`. CLAUDE.md warns in as many words that
the difference between Design's two marks "is a stroke width and a direction,
which is exactly the kind of difference an eye reproduces wrongly."

⚠️ **The PDF strokes it; Word gets a picture rasterised from the same two
polylines at module load.** A `.docx` has no vector primitive a paragraph can
hold. Rather than commit a PNG beside the fonts — a binary that could drift
from the constants in silence — the bitmap is generated from them, anti-aliased
by distance to the stroke. One geometry, two outputs.

⚠️ **THE PAGE NUMBERS WENT WITH THE WORDMARK.** "The chevron mark only" is
read literally. This is the one judgement call in the five and it is the easiest
to reverse: if you want them back they belong in `renderPdf`'s footer loop and
nowhere else, where the number is already computed as `i - range.start + 1`.
Say the word and it is a two-line change.

**The metadata.** `Author` and `Creator` both said `MrBadmusAI`, and PDFKit's
own default for `Creator` and `Producer` is `PDFKit`. All four are blanked. The
Word file's `docProps/core.xml` never said MrBadmusAI — `docx` writes
`Un-named` when not told otherwise, and `app.xml` is empty — but `title`,
`creator`, `lastModifiedBy`, `subject` and `description` are now set
**explicitly**, because a default is a thing a dependency may change in a minor
version and this one is now a promise to a school.

The only text left in either file's metadata is the **title the teacher typed**.

## 342.1.4 · Correction 4 — the stem rule, measured against the real banks

With multiple choice off a question draws ruled answer lines. But a stem is not
always separable from its options: *"Which of these is endothermic?"* has no
answer once the four are taken away. It is not a harder question, it is not a
question.

One rule decides, in `worksheet.js`, for both renderers and both key stages. It
is a test of **reference**, not of the word "which":

| rule | fires on |
|---|---|
| `deixis` | `of these`, `of the following`, `of the options/statements/answers/choices` |
| `deixis_those` | `of those`, but only under a question word within a clause of it |
| `optionless_noun` | `which statement / row / option / answer / description / definition` |
| `correct_noun` | `the correct statement`, `the true sentence`, … |
| `list_reference` | `listed below`, `option C`, `A, B or C` |
| `bare_which` | a sentence **opening** `Which is/are/does/shows…` — no noun at all |
| `pick_verb` | a sentence opening `choose / select / pick / tick / circle / underline` |

### The counts, against every row on TEST

| bank | rows | keep their options | share |
|---|---|---|---|
| **KS3** `ks3_assignment_bank` | 16,946 | **891** | 5.3% |
| **KS4** `ks4_assignment_bank` | 16,765 | **204** | 1.2% |

By rule — KS3: deixis 484, bare_which 205, optionless_noun 167,
deixis_those 15, correct_noun 15, list_reference 3, pick_verb 2.
KS4: deixis 144, optionless_noun 40, pick_verb 10, correct_noun 5,
bare_which 4, deixis_those 1.

**The number that matters is the other one.** 3,453 KS3 stems contain the word
"which", and the rule leaves **2,562 of them open**. *"Which part of a cell
holds the instructions?"*, *"Which gas turns limewater milky?"* and *"Which of
the five levels are missing from it?"* are all answerable with nothing in front
of you. A rule that fired on "which" would have put ruled lines on almost
nothing, which is the failure this was written to avoid.

Reproduce it: `node tools/measure_stem_rule.js` (add `--all` for every flagged
stem). It requires `worksheet.js` itself rather than restating the regexes, so
it cannot agree with itself while disagreeing with what ships.

### ⚠️ The error is deliberately one-sided

Keeping options on a question that did not need them costs a teacher nothing —
it is the sheet they get today. Taking them off one that did need them puts an
unanswerable line in a child's hands. **Every rule is written to fire when in
doubt.**

Three rules were **withdrawn during the measurement** for firing on subject
matter rather than on the option list:

- `best` — *"Evaluate the claim that a transition metal is the **best choice**
  for any job that needs a metal"* is a question about metals.
- `identify which` — *"Identify which salt could not be made…"* is answerable
  by naming the salt, and the banks are full of *"Determine which change…"* and
  *"State which quantity…"* which were correctly left open. Flagging one of the
  three verbs and not the other two was an inconsistency the measurement made
  visible.
- bare `of those` — *"each of those cells is 0.20 µm thick"* is the middle of a
  diffusion calculation. It now needs a question word nearby.

### Two residual false positives, named rather than tuned away

Both err in the safe direction (options kept):

1. *"Explain why conservation decisions are usually described as a balance
   rather than as simple **right answers**."* → `correct_noun`.
2. *"…infers that since fermentation is anaerobic, none **of these** organisms
   can ever use oxygen…"* → `deixis`, where "these" means the three named in
   the stem.

Tightening either would need the rule to understand what the stem is *about*,
and the cost of being wrong the other way is a child holding a question with no
answer.

### A sample of 20 for your judgement

**KS3**

1. `deixis` Which one of these is one of the seven life processes?
2. `bare_which` A retired grandparent … and a delivery cyclist … eat identical meals for a month … **Which is which, and why?**
3. `deixis` … infers that since fermentation is anaerobic, none of these organisms can ever use oxygen … *(false positive — safe)*
4. `deixis_those` Clearing a forest both stops it absorbing future CO₂ AND can release carbon it had already stored. Which of those two effects would you expect to show up first?
5. `deixis` Which of these could never appear in the line of substances in a word equation?
6. `deixis` Which of these is a non-metal?
7. `deixis` Which of these would make the best handle for a hot frying pan?
8. `optionless_noun` An astronaut's mass is 75 kg on Earth. Which statement about their mass in orbit … is correct?
9. `deixis` A car travelling at 15 m/s has friction and air resistance acting on it. Which of these is NOT a force?
10. `optionless_noun` A note's amplitude is increased while its frequency is decreased … Which statement is definitely true?

**KS4**

11. `deixis` Which of these is a biotic factor affecting a population of oak trees?
12. `deixis` Which of these contributions to background radiation is an artificial source?
13. `deixis` Which of these compounds is a hydrocarbon?
14. `deixis` Which of these is a natural ecosystem rather than one created by humans?
15. `optionless_noun` A crate is dragged at a constant velocity … Which statement about its free body diagram is correct?
16. `correct_noun` Explain why conservation decisions are usually described as a balance rather than as simple right answers. *(false positive — safe)*
17. `deixis` Identify which of these is a reactant of photosynthesis rather than a product.
18. `pick_verb` Sodium carbonate is tipped into dilute sulfuric acid. Select the symbol equation that is balanced.
19. `deixis` Which of the following quantities is a scalar?
20. `deixis` Determine which of these would give the strongest evidence that a patient's thermoregulation is failing.

And eight the rule **left open**, which is the half worth checking hardest:

- Which pair of substances crosses the placenta out of the foetus's blood?
- A newton is the unit of which quantity?
- Which gas turns limewater milky?
- State which quantity is given by the gradient of a distance–time graph.
- Determine which change to the ruler drop method would most improve the data.
- Name the biotic factor in which one organism hunts and eats another.
- Over which weeks does the placenta grow into the wall of the uterus?
- An alveolus wall … each of those cells is 0.20 µm thick. Calculate the distance oxygen diffuses.

**Two ruled lines per question**, 22pt pitch — between an exercise book's 8 mm
and an AQA answer booklet's 7 mm. In Word they are paragraph bottom borders:
there is no line primitive a body paragraph can hold, and a row of underscores
breaks where the text engine decides and never reaches the margin.

## 342.1.5 · Correction 5 — the answer key

It read `1.  A  —  two oxygen atoms`. The letter was the problem: with multiple
choice off there are no letters on the sheet at all, so `3. B — kinetic energy`
answers a question the child was never asked. A letter is also the one part of
a key that is useless to the person marking.

It now reads the **key phrase**, with the bank's **`why`** indented under it
where there is one. Both banks already supply it — KS4 in a `why` column, KS3
on the correct option — and `swShapeKs4` / `swShapeKs3` already flatten the two
spellings into one field, so the route passes `why` through and nothing else
changed.

⚠️ **The reasoning still does not reach the child.** The old comment said so
and it is still true: the answers page is a separate page a teacher chooses to
print, and a teacher who prints it has the marking to do.

The key now **hangs**: the number sits in its own column so a phrase that wraps
continues under itself rather than back at the margin, where it reads as the
start of a new answer. The old key never needed this because `A — two oxygen
atoms` always fitted on one line.

## 342.1.6 · Proof — against the real TEST backend, not stubs

`tools/worksheet_artefacts.js` drives **all eight option combinations** over
HTTP against the real backend under a real signed-in teacher, saves every file,
and reads them back with the tools a teacher's own computer would use.

```
SUPABASE_ANON_KEY=… node tools/worksheet_artefacts.js
```

| | |
|---|---|
| files | 4 PDF × 4 DOCX = `{pdf,docx} × answers {on,off} × multiple choice {on,off}` |
| read back with | `pdftotext -layout`, `pdfinfo`, `unzip` over every XML part incl. `docProps/` |
| `MrBadmus` hits | **0**, in all eight, in text, in metadata, and in the raw PDF bytes |
| result | **42 passed, 0 failed** |
| saved to | `$MRB_SHOTS/mrb342.1-worksheets/` — **outside the repo**, per MRB-346 rule 5 |

⚠️ **The raw-bytes check is not belt-and-braces.** The PDF information
dictionary is in no content stream, so `pdftotext` would never have seen
`/Author (MrBadmusAI)` — which is exactly where it used to live. `pdfinfo` reads
it, and the raw-byte scan catches anything neither tool prints.

`pdfinfo` on a finished sheet:

```
Title:           Cell Biology · revision
Subject:
Keywords:
Author:
Creator:
Producer:
```

Unit and route tests: `node test_worksheet.js` — **208 passed, 0 failed,
1 skipped** (the skip is a KS3 subscript fixture, inherited). The stem rule is
tested on **real stems copied out of both banks**, both the flagged and the
left-open side; a rule tested only on sentences invented to exercise it is a
rule tested against its own author.

The throwaway teacher each run creates is torn down **by a snapshotted id
list**, never by a predicate.

## 342.1.7 · Gates, and which reds are inherited

`set_work_drive.py` was updated where it asserted the old behaviour — it is a
gate that had to change, not a gate that was weakened:

- `pdf_brand_footer` **was its own opposite**: "the MrBadmusAI wordmark is on
  every page". It now asserts the word appears on **no** page, *and* that
  Design's double chevron is drawn on every page — two strokes, both `#E4572E`,
  the trailing one at stroke alpha 0.34. ⚠️ **Read out of the page content
  stream**, because a vector footer has no text to extract and
  `extract_text` cannot see it. Asserting only "the word is gone" would also
  pass for a footer that failed to draw at all.
- `pdf_answers_page_present` / `docx_answers_present` looked for the bare
  letter. They now look for the key phrase and the number.
- The `Answers` toggle is read as `.checked` rather than `aria-checked`, plus
  new checks for shape, focusability, the Space key, and `Multiple choice`.
- RISKS A9's allowed list gains `Multiple choice`; `WS_NEW_STRINGS` becomes
  seven. ⚠️ The panel's string sweep had to descend one level: the two toggles
  now sit inside a `.sw-dl-checks` wrapper, and reading only the panel's own
  children would have read that wrapper as a single item saying
  `Multiple choiceAnswers` — failing as a stray rather than as two real labels.

**Inherited reds, proved inherited** by running the same drive on a pristine
`origin/main` worktree against the pre-change backend (`b630c11`) before
touching anything:

| baseline `origin/main` | 398 checks, **4 failed** |
|---|---|
| · `a small KS3 lesson exists to drain` | data — MRB-338 grew the banks; no KS3 lesson has ≤ 8 rows at one tier any more |
| · `a scope of 5–9 questions exists to cap against` | same cause |
| · `a scope of 10–14 questions exists` | same cause |
| · `ks4_stays_flat` | sampling — the preview happened to offer no flat-formula row |

None of the four is reachable from this work: they are searches of the TEST
tree for scopes that no longer exist at those sizes. They are **not fixed
here** — they are a content-fixture problem and fixing them inside a brand and
rendering change would be the wrong ticket.

⚠️ **This baseline run is why `row_download_lands` was not written off.** It
failed on the first run of the changed tree and appears in **no** baseline
failure list, so it could not be waved through as inherited.

It **passed on the re-run**, and the rest of the drive is unchanged around it,
so it was a download-timing flake — `take_download` waiting on a file the
browser had not finished writing. MRB-346 rule 4 exists for exactly this class
of failure. It is recorded rather than quietly dropped because "it passed the
second time" is a claim that needs the first run's evidence beside it.

| run | tree | result |
|---|---|---|
| baseline | pristine `origin/main` + backend `b630c11` | 398 checks, 4 failed *(all data/sampling)* |
| run 1 | changed tree, old assertions | 397 checks, 7 failed *(4 inherited + 3 asserting the old behaviour + `row_download_lands`)* |
| **run 2** | **changed tree, updated assertions** | **406 checks, 4 failed — the same four, and only those four** |

Eight new checks, all green: `answers_is_a_real_checkbox`,
`answers_is_focusable`, `answers_space_toggles`,
`multiple_choice_is_a_real_checkbox` and its label, `pdf_no_wordmark`,
`pdf_brand_footer`, and the faded-chevron alpha.

## 342.1.8 · Deviations

**Deviation:** the footer's page numbers were removed along with the wordmark
→ "the chevron mark only" read literally → flagged above in §342.1.3; it is a
two-line restore if that is not what you meant.

**Deviation:** the rule in the header (the thin line under the title) went with
the class/tier/date line → "the worksheet title only, nothing else" → the
header is now a bare title.

**Deviation:** the answer key gained a **hanging indent**, which is a sixth
change nobody asked for → a wrapped key phrase was continuing at the left
margin, where it reads as the start of the next answer → it is inside
correction 5's own surface and was visible in the first rendered proof, so it
was fixed rather than filed.

**Deviation:** `why` is printed for **KS3 as well as KS4** → the brief says
"the KS4 `why` where it exists" → KS3 carries one on the correct option and
`swShapeKs3` already flattens it into the same field, so excluding it would
have meant writing code to suppress information the teacher wants.

**Deviation:** three detection rules were withdrawn mid-measurement (`best`,
`identify which`, bare `of those`) → each fired on subject matter rather than
on the option list → §342.1.4.

**Deviation:** `brew install poppler` was needed for `pdftotext`/`pdfinfo`;
neither was on this machine.

## 342.1.9 · Still open

- **Page numbers** — removed by the literal reading of correction 3. Your call.
- **The four inherited drive reds** are a content-fixture problem: the drive
  looks for KS3 lessons with ≤ 8 rows at one tier and scopes of 5–9 and 10–14
  questions, and MRB-338's bank expansion left none. They want a different
  ticket — either fixtures sized for the checks, or checks that pick the
  smallest scope that exists rather than one in a fixed band.
- `teacher_admin_foreign_class` (C7 REMINDERS × 3) is still the inherited red
  CLAUDE.md names. Untouched here.
