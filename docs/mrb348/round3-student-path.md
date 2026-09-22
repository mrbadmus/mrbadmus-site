# MRB-348 round three — the student class page's opening wave

22 September 2026. Follow-up item 1 of `docs/mrb348/REPORT.md` §5.

> ⚠️ **`/api/class/practice` failing takes the whole class page down.** Not the
> practice panel — the whole page. It is one arm of the opening `Promise.all`,
> so if Render is cold or blips, a student sees "We could not load your class
> just now" instead of their work.

That is fixed, and so are three quieter versions of the same defect on other
arms of the same wave. **Nothing on a healthy page changed** — proven against
the real page, as real students, on all three of the equivalence cases.

**Short version.**

| | |
|---|---|
| Practice out of the critical path, folded in after mount | done, proven twice |
| The other non-critical arms audited and soft-failed | 3 changed, 2 left critical, 2 already safe |
| Healthy page unchanged | 3/3 cases byte-identical — text, controls, address |
| The defect, reproduced and then fixed | old build dies, new build mounts with the work intact |
| Gates | 6 green, 1 skipped for want of a production credential |
| Mid-flight rebase onto `origin/main` | reconciled, see Deviations |

---

## 1 · What changed, and where

Two files. Everything else in the diff is generator output.

### `shared/student-live.js`

| line | what |
|---|---|
| ~1112 | `var pendingLate = null;` — the hand-off from `buildClass` to `run()`, the same shape `pendingSink` already uses, and for the same stated reason: the data object is what the page renders from, and a function owning two database reads is not data. |
| ~2007 | `var practiceP = api("/api/class/practice…")` — **started above the wave, boxed, and not awaited by it.** |
| ~2036 | `function _soft(p, what)` — turns a rejection into supabase-js's own `{ data: null, error }`, which is the shape the consumer already handles. |
| ~2044 | the opening `Promise.all`, now **seven arms, not eight** |
| ~2197 | `var practice = null;` and the re-indexed arms |
| ~2700 | `fillQuestions(src)` — returns a fresh array, callable twice |
| ~2770 | `coverFromPractice(src)` — returns the slugs practice ADDS, so the late read is supplementary rather than a repeat |
| ~2830 | `startCards(slugs)` / `startBank(slugs)` — the two deck reads parameterised |
| ~2900 / ~3030 | `mapCards(rows)` / `mapBank(rows)` — the two row shapings extracted; `cardsAll` / `bankAll` hold the UNRANKED rows |
| ~2980 / ~3090 | `rankDeck()` / `rankBank()` — one ranking, callable again |
| ~3195 | `weekFrom(p)` — the week fallback, askable again |
| ~3423 | `pendingLate = function foldInPractice(app) { … }` |
| ~4760 | `run()` — `var app = window.__MRB_MOUNT__();` then `pendingLate(app)`, after the paint, never awaited, in a try/catch |

### `shared/student-runtime.js`

| line | what |
|---|---|
| ~504 | `api.rebind(roots)` — replace the bound template and draw. 6 lines. See §4. |

**Not one request was added or removed on a healthy page.** The page fetches
exactly what it always did; the supplementary read in §3 only ever fires for
lessons the first read did not cover, and only when practice names some.

---

## 2 · The per-arm table

The rule I worked to: **an arm may only be soft-failed to a shape its EXISTING
consumer already handles.** Each row below names the consumer I read, and what
a student actually loses.

| # | arm | verdict | consumer I read | what a student loses when it fails |
|---|---|---|---|---|
| — | `api("/api/class/practice")` | **OUT OF THE WAVE** | three, see §3 | the flashcard deck's scheme-taught lessons (55 cards → 16 on 8X1), the practice round's rungs from those lessons, and the teaching week ONLY on a class with no current assignment. Nothing else. |
| 0 | `D.loadStudentClass` | **CRITICAL — kept** | the whole function; `detail.class`, `detail.viewer`, `detail.assignmentsDueNow/ComingUp/Done` | everything. It is the class, the child and the work. `student-data.js` rethrows (line ~314), and `not_authorised` / `class_not_found` are distinct ruled sentences. Soft-failing it would mean drawing an empty page as though the class had no work. |
| 1 | `api("/api/class/current-assignment")` | **CRITICAL — kept** | `current.assignment`, `current.questions`, `current.week`, `current.progress`, `benchWork`, `lessonDefs`, `docket*`, the reminder line's progress clause | the child's actual work for this week. If it fails the page genuinely has nothing to show. ⚠️ **This means the page still depends on Render**, and practice being parallel to it means **the latency win from this change is small. The win is availability.** I have not measured a speed gain and am not claiming one. |
| 2 | `assignments` (`id, academic_week`) | **soft** | `aw.data \|\| []` at two sites | the teaching week on each work row (falls back to the `due_at` arithmetic), the "Open the lesson" links, FROM YOUR WORK ordering, the deck and round's assignment-side lessons, and — since the first-week-fixes landing — the completion bar, which is exactly the "both fields or neither" behaviour that ruling asks for. The work list itself comes from arm 0 and survives. |
| 3 | `academic_years` | **soft** | `if (!yrs.error)` | only `weekOf`'s `due_at` fallback, and only for a work row whose `academic_week` is null. ⚠️ **The MRB-261 hazard is not on this arm.** I checked rather than assumed: `year` has exactly one reader inside `buildClass`. The year-scoped CLASS LIST is decided by `loadStudentClasses`/`pickClass` in `run()`, one level up, out of this arm's reach — so failing it cannot show a Year 11 the class they left in July. And a soft failure lands in the `error` branch, so `year` is null and **never an empty list read as "there are no years"**. |
| 4 | `student_reminders_for_viewer` RPC | **soft** | `unreadNotes && !unreadNotes.error && unreadNotes.data && …` | the one-sentence teacher reminder banner. The BELL is a separate read injected after the mount and is unaffected. |
| 5 | shout-outs | **already soft** | its own `.catch(→ {shoutouts: []})` | unchanged. This was the model; I copied its shape and its reasoning. |
| 6 | `D.loadClassTeacherNames` | **never throws — left alone** | `classTeachers.length === 1 ? … : "Your teacher"` | confirmed as briefed: `shared/student-data.js` line ~1066 catches internally and returns `[]`. The chip falls back to "Your teacher" with no initials, which is the ruled fallback. |

### ⚠️ The error case was not the worst half

Boxing practice's rejection *inside* the wave would have fixed the 500 and left
the **slow** case exactly where it was. `Promise.all` waits for a `catch` to
resolve just as it waits for a value, so a practice call that hangs to its
ceiling would still have held the first paint — up to `COLD_MS`, **seventy-five
seconds** of blank page, for a panel nobody had opened. It has to leave the
wave, not merely be forgiven inside it. The three soft-failed arms above carry
the same argument in miniature: their consumers already handled a REFUSAL, and
what killed the page was `withDbDeadline`'s **timeout**, which rejects.

### One thing that moved and should be named

`serverNow` is set by `api()` from the response `Date` header, and the old
comment said "whichever of the **two** api calls answers first". There is now
one api call in the wave, so `serverNow` comes from `current-assignment` alone.
That was already true whenever practice was the slower of the two, and
`current-assignment` is awaited and is the same server — but it is a narrowing,
so it is written into the file rather than left to be discovered.

---

## 3 · The fold-in

Practice has exactly three consumers, and they behave very differently under a
late fill.

**`questions[]`** — published, and read by nothing. The old recall round that
consumed it was retired on 23 Aug 2026; `student/class.html` assigns
`this.questions = MRB_DATA("questions")` at construction and never reads the
field again. Refilled so the published data is honest; it is not the reason for
any redraw.

**`coveredSlugs`** — the real work. Neither slug set contains the other: (a) is
every lesson behind every assignment the class has been set, (b) is every
lesson the scheme says it has been taught. On 8X1 today (b) is much the larger:
the deck is **55 cards with practice answering and 16 without it**. So the
fold-in reads the two corpora for **only the slugs (b) adds**, concatenates,
and re-ranks the union with the same `rankForPractice` call the first paint
used. `cardsAll`/`bankAll` hold the unranked rows so the second ranking sees
the same input the first did.

> ⚠️ **It is still exactly one serving read per pool.** `pool_ownership` counts
> `from("ks3_cards").select(…)` sites in this file, by design, because a second
> serving read is how a cross-feed starts. Parameterising the one read keeps the
> count at one and makes the claim *more* true: there is now literally a single
> place in the file that serves a card and a single place that serves a rung.
> The gate is green.

**`weekNo`** — `current.week` still wins. Practice's week is consulted only on a
class with no current assignment, where it is null at first paint and becomes
that value when practice lands.

### The redraw, and why it is gated

`student-runtime.js` `draw()` empties the mount host and rebuilds the template.
It restores focus, every form field's value and the DOCUMENT's scroll — but not
any element's own `scrollTop`.

Measured against the compiled template rather than assumed: **the class view
contains no `overflow:auto` at all.** There are exactly two inner scrollers on
the page and both are overlays — the **account sheet** and the **practice
round**. A third surface is worse than a lost scroll position: the **flashcard
overlay** draws `deck[idx]`, so re-ranking the deck under an open overlay
changes the card physically under the student's finger, and the round has the
same problem with `practiceBank`.

**So the honest answer is the one the brief anticipated: the fold-in is gated
on the student not being inside the deck, the round or the account sheet.** It
applies immediately on the class view; otherwise it registers an
`__MRB_AFTER_DRAW__` hook and lands on the first draw after the overlay closes
— which is the draw that closing it already caused. It is deferred, never
dropped.

### ⚠️ And one thing a redraw alone cannot do

`practiceLabel` is a **binding**, not a render value. `applyBindings` writes it
into a clone of the compiled template once, before the first paint, and it is
marked `drop` — an empty value removes the Practice button's element outright.
A later `setState` cannot bring it back.

That case is real, not theoretical: **a class in its first week has no
assignments**, so the assignment walk covers no lessons, so the bank is empty at
mount and the button is dropped — and practice is precisely the source that
would have filled it. So when, and only when, the bank goes from empty to
non-empty, `api.rebind()` applies the bindings again to a fresh clone of the
untouched compiled template. `applyBindings` only ever removes, never adds or
reorders; a throw inside it is caught and costs the button and nothing more.

That is the whole of the six-line addition to `student-runtime.js`, and it is
deliberately the only way in: the runtime never re-binds on its own.

---

## 4 · The proofs

### (a) A healthy page is unchanged — `mrb348_student_equiv.py --compare`

Real page, real students, TEST, local backend, one discarded warm-up load per
case (auto-composition is lazy — see the script's own note).

```
  ks3-own — KS3 8X1, the student's own class
     ✅ visible text   (1432 vs 1432 chars)
     ✅ control set    (41 vs 41)
     ✅ address        old='?class=2a0000…001' new='?class=2a0000…001'

  ks4-own — KS4 10A, the student's own class
     ✅ visible text   (2296 vs 2296 chars)
     ✅ control set    (53 vs 53)
     ✅ address        old='?class=2a0000…002' new='?class=2a0000…002'

  ks3-foreign — RULED: a class that is NOT this student's
     ✅ visible text   (1432 vs 1432 chars)
     ✅ control set    (41 vs 41)
     ✅ address        old='' new='' (ruled: no class parameter)

  ✅ every case renders the same visible text, the same controls, and the same address.
```

⚠️ Both captures were taken **after** the rebase, against `origin/main`'s tip as
the OLD side. The pre-rebase captures were discarded — they would have reported
the first-week-fixes completion bar as my regression.

This is also the strongest evidence that the fold-in is faithful: the 55-card
deck the old blocking read produced is the same 55-card deck the fold-in
produces, down to the leading card.

### (b) The defect reproduced, then fixed — `--compare-down`

**The failure is real, not simulated.** Nothing in the page's own code is edited
and no flag is set. A reverse proxy stands in front of the local backend, 503s
`/api/class/practice` **and only that path**, and forwards everything else; the
page is pointed at it with `?api=`, the localhost-only override `config.js`
already carries.

```
  /api/class/practice forced to 503 — the defect, and the fix

  BEFORE (the defect reproduced)
     ✅ the page never mounted — the failure card is up

  AFTER (this change)
     ✅ the page mounted with the practice route answering 503
     ✅ no failure sentence anywhere on it
     ✅ every control that is not practice-fed is identical to the healthy page (39 of them)

     what the degradation costs, stated rather than hidden:
       healthy page    1432 chars,  41 controls,  411 nodes
       practice down   1429 chars,  41 controls,  411 nodes
       controls lost: ['BUTTON|FLASHCARDS 55 Define: limewater 01 / 55']

  ✅ practice can fail and the child still gets their work.
```

The deck falls 55 → 16 and its top card changes. That is the whole degradation,
and it is printed rather than asserted away.

> ⚠️ `MOUNTED` is not `READY`. `READY` counts characters, and the failure card
> is comfortably over eighty of them — the §0 trap. `data-mrb-renders` is
> written by `draw()` and by nothing else, so it is the one signal that says THE
> RUNTIME DREW rather than THE HOST HAS TEXT IN IT.

### (c) The page does not WAIT for practice — `--slow-fold`

The same proxy stalls the route by 3 s and then answers it normally.

```
  /api/class/practice stalled by 3.0s

     t= 1.43s  renders=2    FLASHCARDS 16 Define: floats 01 / 16
     t= 3.54s  renders=3    FLASHCARDS 55 Define: limewater 01 / 55

     ✅ first paint at 1.43s, before the 3.0s stall ended
     ✅ the deck changed at t=3.54s, after the stall — that is the fold-in
```

First paint at 1.43 s with the practice call still 1.6 s from answering; the
deck fills at 3.54 s. Both halves of §3, in one timeline.

### (d) Gates

| gate | result |
|---|---|
| `pool_ownership` | ✅ — still exactly one serving read per pool |
| `student_behaviour` | ✅ (re-run after the rebase, against upstream's own updated copy) |
| `student_parity` | ✅ — and per CLAUDE.md its green is **not evidence about this change**: it drives `student/class-preview.html` and has no path to the ported page. Recorded as a non-regression, nothing more. |
| `student_themes` | ✅ (re-run after the rebase) |
| `leaderboard_behaviour` | ✅ — it watches `student-runtime.js`, which I changed |
| `student_bell_drive` | ✅ ×3 — but see below |
| `student_controls_drive` | ⏭ **skipped by name** — it signs in as `midebolabadmus@gmail.com` against **production** (`urklkrwevjtlfbwnipjn`) and needs `MRB_DRIVE_PASSWORD` / `MRB_TEST_STUDENT_PASSWORD`. I do not hold that credential and did not try to obtain one. |
| `python3 build_all.py` | ✅, and **run twice: the second build changed nothing**, so the merge invented no page a generator would not produce |

**`student_bell_drive` — one red I could not fully exonerate.** On my *first*
run of the pre-rebase build, `bell_on_real_route` failed: the route returned 3
messages, the panel drew 0 rows and the badge read `0`. I baselined it against
the old build (green), then ran the new build three more times — **green every
time**, including twice after the rebase.

What I can say: the failure was `state.items` empty, not a DOM loss — the bell
button was present and clickable, and phase 2's `bell_survives_redraw` and
`panel_survives_redraw` passed in the same run. Phase 8's window is `wait_bell`
(which returns as soon as the BUTTON exists, before the bell's fetch resolves)
plus 0.7 s, so a slow real-route fetch fails it with nothing wrong.

What I cannot say is that my change had nothing to do with it. My fold-in adds
one extra `draw()` about a second after mount, which re-runs the bell's
after-draw hook; `place_button` is idempotent and `repaintButtons` reads
`state`, so I can see no mechanism — but 1 red in 4 is a thing to watch, not a
thing to dismiss. **Named here rather than buried.**

---

## 5 · What I did not prove

- **No speed claim.** `current-assignment` is still a blocking call to the same
  backend, so the cold start is still paid. I did not measure a mount-time
  improvement and am not claiming one. The win is availability, plus the removal
  of a path where a slow practice call could hold the paint for up to 75 s.
- **No matched `perf_waterfall` before/after.** Port 5531 is held by a
  **concurrent session** running the teacher journeys; I killed one such process
  before realising it was live (see Deviations) and did not touch the second.
  The `--slow-fold` timeline above answers the same shape question directly.
- **Production was never touched.** Every drive ran against TEST
  (`qeppkiswvclkkwbxmlok`, proved from the service key's own `ref` claim in the
  backend `.env`), with the backend running locally.
- **The rebind path is proven by construction and by reading, not by a drive.**
  The forced-failure and slow-fold cases both exercise 8X1, whose bank is
  non-empty at mount, so `rebind()` is not entered. The case it exists for — a
  class with no assignments at all — has no fixture on TEST. It is guarded
  (`try/catch`, and it only ever runs when the bank goes empty → non-empty), and
  its failure costs the Practice button and nothing else.
- **The deferral path (overlay open when practice lands) is not driven either.**
  Reaching it needs a student to open the deck within ~1 s of mount. It is 12
  lines, it only ever delays, and the applied state is identical either way.
- **One arm still has no deadline:** `loadClassTeacherNames` is not wrapped in
  `withDbDeadline`. It catches internally so it cannot reject, but a hung read
  inside it would hold the wave. Out of scope tonight; noted.

---

## 6 · Deviations

- **Mid-flight rebase onto `origin/main`.** This checkout was two commits behind
  and never fetched; `origin/main` carried the first-week fixes
  (`ce6538e36`, `db70b452d`), already live, which edit the same file. I created
  `backup/pre-rebase-mrb348r3`, saved my source diff, rebased the two local
  MRB-348 WS-3 commits onto `origin/main` (clean), and re-applied my diff with
  `git apply -3` — **clean, no conflicts**. I then verified BY READING that both
  halves survived: `qTotalFor`, `answeredFor`, `attempt_no`, the
  `status === "missed"` assignment href and the `row.qtotal`/`row.answered`
  block are all present and untouched, and every line my diff removes is a line
  I wrote. Every generated file was settled by `build_all.py`, never by hand,
  and a second build changed nothing. All captures and gates were re-run after
  the rebase; nothing from before it is quoted here.
- **I did not commit.** The brief says to leave the tree with the changes in it,
  so the rebase was done with my work stashed and restored, and nothing of mine
  is in any commit. The branch history now contains only the two pre-existing
  WS-3 commits, replayed onto `origin/main`.
- **The first-week rulings need nothing from the fold-in.** I checked: the
  completion bar reads `work`, which is assignment-derived and untouched by
  practice. My redraw re-renders it from the same data.
- **I killed another session's process.** Port 5531 was held by a stale-looking
  `perf_waterfall.py --journey teacher-*`; I killed it, and a second one took
  the port moments later, which means it was a live concurrent run and my kill
  cost it. My mistake — I should have checked for a live session before killing
  a listener on a shared port. No repo state was affected.
- **Two harness defects in my own new proxy, both of which produced a false red
  and are now documented in the script**: (1) it copied the backend's `Date`
  header on top of the one `BaseHTTPRequestHandler` emits, so `res.headers
  .get('date')` came back comma-joined, `serverNow` was never set and the page
  threw "no server clock on the response"; (2) it forwarded
  `Access-Control-Allow-Origin` without `-Allow-Headers`, so Chrome refused the
  preflight for `current-assignment` and the CRITICAL arm failed. Both look
  exactly like the fix not working.
- **`Date` must be CORS-exposed.** The backend's `exposedHeaders: ['Date',
  'Content-Disposition']` is load-bearing for `serverNow`, and `Date` is not a
  CORS-safelisted response header. Written into the proxy with the reason.
- **TEST fixture password.** I used the standing `mrb293-drive-only` from
  `tools/test_fixture_password.py`; no new credential was created and nothing
  on TEST was modified except by the drives' own throwaway seeds, which clean up
  after themselves.
