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

- **The site half is not merged.** Sheet UI, multi-scope state, `Add topic`,
  `Download` on the sheet/row/marking screen, and the four MRB-340 tidy-ups are
  built and driven (52/52 at 390px and 1280px, 13/13 on the real fixture, 6/6 on
  the edit path) — **but only against a STUB backend.**
- ⚠️ **Blob handling, `Content-Disposition` parsing and the `<a download>` save
  are untested against real bytes.** The stub returned a Blob and the save path
  did not throw; that is not the same as a PDF landing in Downloads.
- **`pool_ownership`'s `SET_WORK_READERS` needs the worksheet route added.** The
  site lane deliberately did not widen the seal before the thing it guards
  existed — that judgement was right.
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
