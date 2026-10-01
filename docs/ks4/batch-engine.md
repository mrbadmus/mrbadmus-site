# The KS4 batch engine

For the next author, after Mide's ruling of 1 Oct 2026 ("Let Code write
the lessons"). `build_ks4.py` now builds any number of lesson BATCHES, not
just the 14-lesson pilot ("batch 1" in code, named `pilot`). This file is
the contract between an author's `.dc.html` + lesson record and what the
build does with them — short, because the authoring brief
(`docs/ks4/AUTHORING-BRIEF.md`) and the architecture
(`docs/ks4/architecture.md`) already say how to WRITE a lesson well; this
says how the ENGINE turns it into a page.

## 1. Where a batch's source lives

```
ks4_lessons/
  __init__.py          — the pilot's 14 records (LESSONS), unchanged,
                          plus the batch registry (batch_names(),
                          lessons_for_batch(), authored_dir(), …)
  batch_<name>.py       — ONE module per non-pilot batch, e.g. batch_2.py
  authored/
    <batch>/
      <slug>.dc.html    — one file per lesson in that batch
      _ext.js           — OPTIONAL: helpers/diagrams this batch needs
```

A batch is discovered by FILENAME alone — there is no second list to keep
in step. `ks4_lessons/batch_2.py` registers as batch name `batch-2`
(`batch_<x>.py` → `batch-<x>`, underscores become hyphens). It must export
a `LESSONS` list in the same shape as the pilot's:

```python
LESSONS = [
    dict(slug="cell-structure", source_file="cell-structure.dc.html",
         subject="biology", topic_id="cell-biology",
         title="Cell structure", spec="4.1.1.1",
         family="Model", routes=["CF", "CH", "TF", "TH"],
         review_state="draft", batch="batch-2"),
    ...
]
```

Fields: `slug`, `source_file` (NOT `design_file` — that name is the
pilot's, because the pilot's source is a Design delivery; an authored
lesson's source is this batch's own `.dc.html`), `subject` (`biology` |
`chemistry` | `physics`), `topic_id`, `title`, `spec`, `routes` (the
subset of `CF`/`CH`/`TF`/`TH` this lesson ships on — a Triple-only lesson
like the pilot's `nanoparticles` writes `["TF", "TH"]` and the build
writes no Combined page, without touching whatever the OLD Combined page
at that URL already was), `review_state` (`draft` | `examiner-reviewed` |
`frozen` — feeds `showDraft`, same as the pilot), `batch` (this batch's
own name, for bookkeeping — not read by the compiler), and the optional
`family`, `block_map` (see §4) exactly as the pilot's records use them.

## 2. Write the `.dc.html` directly in its FINAL form

An authored lesson is not reverse-engineered from a React page the way
the pilot was, so it never needs the pilot's port-mechanics fixups
(`ks4_rulings.py`'s R1/R-SLUG/R-PREVNEXT/R-CONNECTS and friends). Write it
already in the shape those rulings would have produced:

- **No Route `<select>`.** One file serves all four routes; the route is
  a mount prop, never a control on the page.
- **`endPrev: this.props.mrbPrevNext.prev, endNext: this.props.
  mrbPrevNext.next,`** in the Component's render — the build fills these
  per page from the real per-route topic order in `all_subtopics_*.py`
  (`build_ks4.compute_prev_next()`, the SAME function the pilot uses), so
  a batch lesson's neighbours are correct and so are an OLD page's, when
  an old page's prev/next happens to point at a lesson this batch just
  shipped.
- **`endConnects: [{ href: K.hrefFor('<slug>', R), label: '…' }, …]`** for
  "Connects to" links — `KS4.hrefFor` resolves against EVERY registered
  batch and the pilot, so a connects link can point at a pilot lesson, a
  sibling in this batch, or — once `hrefFor` returns null for a target
  with no page on the current route — simply be dropped (`Ks4End`'s own
  filter, inherited unchanged from the pilot).
- **No hard-coded "Combined · Triple" / "Foundation · Higher" pill.** If
  the lesson head needs to say which routes it covers, write the true
  words for THIS lesson's own `routes` list directly.

## 3. Route layers — `data-route`

Tag any element (usually a `<section>` or a `<div>`) with one of:

```html
<section data-route="higher">…</section>      <!-- CH, TH -->
<section data-route="triple">…</section>      <!-- TF, TH -->
<section data-route="triple-higher">…</section> <!-- TH only -->
```

At compile time (`build_ks4.apply_route_layers()`, once per lesson — the
SAME compiled template serves every route, with the condition evaluated
client-side exactly the way the pilot's own `isHigher`/`isTriple`-gated
content already works) the element is:

1. wrapped in an `sc-if` on the matching flag (`isHigher`, `isTriple`, or
   `isHigher && isTriple`), so it is absent from the DOM entirely — not
   merely hidden — on a route it does not apply to;
2. given a route badge as its own first child, in the pilot's existing
   mono-pill style (`ks4_rulings.R9_TARGETS`'s shape): "Higher" (stretch
   tint), "Triple" (blue tint), or "Higher · Triple" (alert tint).

Authors never write the `sc-if` or the badge markup by hand — that is the
whole point of the attribute. The tag's value comes from the AQA
specification's own **HT** / **"Physics (or Chemistry/Biology) only"**
labels; cite the section in your notes (`AUTHORING-BRIEF.md` §2).

`data-route` is not supported directly on a `<dc-import>` — wrap the
import in a `<div data-route="…">` if a whole component must be
route-gated.

## 4. Classifying a lesson's sections

Every top-level `<section>` (and the `<div data-key-fact>` card) in a
lesson's body is classified into one of the registered block types
(`ks4_lessons/blocks.py`) and stamped `data-block="…"` on the page — the
SAME closed-registry mechanism the pilot uses, including for a section
that is now wrapped by `data-route`'s `sc-if` (the build classifies the
INNER section, not the synthetic wrapper). Where the heuristic cannot
infer a type, the build raises naming the section's id/index — add an
entry to that lesson's `block_map` in its record, e.g.
`block_map={"s-oscilloscope": "figure"}`.

## 5. Per-batch assets — never touch the pilot's

The pilot's shared assets (`shared/ks4-ds.css`, `ks4-theme.css`,
`ks4-lesson.css`, `ks4-source.js`, `ks4-lib.js`, `ks4-diagrams.js`,
`ks4-runtime.js`) are loaded on every KS4 page, pilot or batch, and their
`?v=` stamps are baked into all 54 pilot pages — so NOTHING in the batch
engine ever edits them. A batch gets its own, additional assets instead,
all generated from that batch's own lessons only:

| asset | what | generated from |
|---|---|---|
| `shared/ks4-source-<batch>.js` | this batch's lessons' quiz/rp/key_note/etc, keyed by slug, merging into the SAME `window.KS4SRC` the pilot's `ks4-source.js` writes to (both load fine in either order) | `all_subtopics_*.py` (now including biology) |
| `shared/ks4-lesson-<batch>.css` | this batch's lessons' own de-duplicated `<style>` blocks (deduped against each other only — not against the pilot's `ks4-lesson.css`, which every page already loads separately) | this batch's `.dc.html` files |
| `shared/ks4-ext-<batch>.js` | OPTIONAL: new helper/diagram functions this batch's lessons need, loaded after `ks4-lib.js`/`ks4-diagrams.js` | `ks4_lessons/authored/<batch>/_ext.js`, copied/stamped verbatim |
| `shared/ks4-nav.js` | ⊕ fix, 1 Oct 2026 (§7b) — ONE shared asset, not per-batch-name, rewritten (idempotently) by every batch build. Wraps `KS4.hrefFor` with a fallback to a FULL-SITE nav table, so a connects/prev/next link can resolve to ANY KS4 subtopic on the site — a sibling in this batch, a lesson in another batch, or an old (pre-port) page — not only the pilot's 14. Loaded AFTER `ks4-lib.js`, by batch pages only — never the pilot's. | `all_subtopics_*.py` ONLY (`build_ks4.build_ks4_nav_js()`) — never `ks4_lessons.LESSONS`/`all_lessons()`, so its bytes do not move when a batch is added, built, or removed |

A batch page's `<head>`/`<body>` carries the pilot's shared assets PLUS
these four (the optional one only if `_ext.js` exists) — see
`build_ks4.render_page()`'s `batch_css`/`batch_source_js`/`batch_ext_js`/
`batch_nav_js` parameters, each `""` by default so the pilot's own call
renders byte-identical output to before they existed.

## 6. Commands

```bash
python3 build_ks4.py                      # every registered batch, pilot first
python3 build_ks4.py --batch pilot        # the pilot only — identical to the old build_ks4.py
python3 build_ks4.py --batch batch-2      # one batch only (needs a prior pilot build for
                                           # the shared infra — it checks and says so if missing)
python3 build_ks4.py --batch batch-2 --freeze   # stamp ks4_lessons/frozen_batch-2.json

python3 ks4_batch_check.py                # fast, no-browser gate — every non-pilot batch
python3 ks4_batch_check.py --batch batch-2

python3 ks4_parity.py --batch batch-2     # console errors, overflow, registry, route layers,
                                           # prerendered text, keyboard — no Design reference
python3 ks4_parity.py                     # unchanged: the pilot's full Design-fidelity sweep

python3 ks4_science_rulings.py --batch batch-2   # reports 0 rulings until a batch has any

python3 check_ks4_live.py --batch batch-2 # AFTER a push+deploy — live byte-for-byte proof
python3 check_ks4_pilot_live.py           # unchanged: thin wrapper for --batch pilot
```

`build_all.py` step 1b calls `build_ks4.py` with NO flag, so every live
batch is rebuilt on every full site build — exactly as it already did for
the pilot.

## 7. The byte-identity rule

**The pilot's 54 pages, and its 17 shared assets, must never change by a
byte because a batch was added, built, or removed.** The mechanism that
guarantees this:

- `build_pilot()` is the UNCHANGED body the old `main()` always had — a
  batch build never edits it, calls it differently, or runs before/after
  it in a way that changes what it writes.
- Every shared asset the pilot's own pages LOAD (`ks4-ds.css`,
  `ks4-theme.css`, `ks4-lesson.css`, `ks4-source.js`, `ks4-lib.js`,
  `ks4-diagrams.js`, `ks4-runtime.js`) is built from data that depends
  ONLY on the pilot's own 14 lessons or on `all_subtopics_*.py` directly
  — never on `ks4_lessons.all_lessons()` or on which other batches are
  registered. In particular `shared/ks4-lib.js`'s `NAV` table (prev/next/
  connects resolution) is built from `ks4_lessons.LESSONS` — the pilot's
  14, and ONLY the pilot's 14, forever.
- Everything else a batch writes (`ks4-source-<batch>.js`,
  `ks4-lesson-<batch>.css`, its own pages, its own manifest/frozen file)
  is a NEW file under a name no pilot page references.

### §7a — the rule this section used to get wrong (1 Oct 2026)

This section used to say the opposite of the second bullet above: `NAV`
was built from `ks4_lessons.all_lessons()` (every registered batch, not
just the pilot's 14), reasoning that its CONTENT stayed byte-identical
"with no other batch registered" and that a real batch changing it was
"correct and expected… a SHARED asset precisely so a pilot page's
'Connects to' can one day point at a batch lesson." That reasoning
described the defect as the design. `shared/ks4-lib.js` is one of the 17
shared assets whose `?v=<md5>` stamp is baked into all 54 pilot pages'
own bytes (`KS4_VERSIONED`, `build_pilot()`'s `versions` dict) — so the
moment ANY second batch was registered, `ks4-lib.js`'s content moved, its
stamp moved, and all 54 pilot pages moved by those bytes. The very rule
this section exists to state would have broken on the first real batch.

### §7b — the fix: a separate, batch-only nav table

`shared/ks4-lib.js`'s `NAV` is pinned to the pilot's 14 lessons,
permanently — it cannot be a function of which batches exist. A
connects/prev/next link that needs to reach OUTSIDE those 14 (a sibling
in a batch, a lesson in a different batch, or any other KS4 subtopic that
merely has a page on the site — an old, unported design page is a real
page at a real URL too) is `shared/ks4-nav.js`'s job instead
(`build_ks4.build_ks4_nav_js()`) — a NEW, separate shared asset:

- Loaded by BATCH pages only, after `ks4-lib.js` (`render_page()`'s
  `batch_nav_js` parameter). The pilot's 54 pages never load it and never
  will.
- It WRAPS `KS4.hrefFor` rather than replacing it:
  ```js
  var base = KS4.hrefFor;
  KS4.hrefFor = function (slug, R) { return base(slug, R) || fullNavHref(slug, R); };
  ```
  so the pilot's own lookups (on a batch page, through the base function)
  keep resolving exactly as `ks4-lib.js`'s NAV always has, and only a miss
  falls through to `shared/ks4-nav.js`'s `FULL_NAV`.
- `FULL_NAV`'s content depends ONLY on `all_subtopics_*.py` (the same
  data `generate_site_v5.py` itself reads to decide which pages exist) —
  NEVER on `ks4_lessons.LESSONS`, `all_lessons()`, or which batches are
  registered. That is what makes it safe for a batch to depend on:
  registering, building or removing a batch never moves `ks4-nav.js`'s
  bytes either, so batch 2's pages do not move when batch 3 is
  registered. It is rewritten (idempotently — same bytes every time) on
  every batch build, by whichever batch happens to build, because it is
  one shared file, not named per batch.
- `ks4_pilot_check.py`'s `check_no_leakage()` needed the same kind of fix,
  for a different reason: it used to flag ANY `.html` page outside the
  pilot's own manifest that referenced `ks4-runtime.js` as a "LEAK" — true
  before batches existed (nothing else could legitimately load that
  runtime), false the moment a second batch existed (every batch's own
  pages legitimately do). It now also treats every OTHER registered
  batch's own manifest as a legitimate owner, and only flags a page that
  is outside ALL of them — pilot's and every batch's.

### Proof

Build the pilot alone, snapshot its manifest + sha256 of its 54 pages/17
assets + a repo-tree `git status`. Register a second, throwaway batch
(`ks4_lessons/batch_zz.py`, one dummy lesson at a real non-pilot slug,
`ks4_lessons/authored/batch-zz/<slug>.dc.html`), build it, and confirm:
the pilot's 54 pages and 17 assets are still byte-identical to the
snapshot (and to HEAD); `ks4_pilot_check.py` is clean; the dummy batch
page's prev/next and "Connects to" links resolve — one to a pilot lesson
(through `ks4-lib.js`'s own NAV), one to an old, unported page that has no
`ks4_lessons` record at all (through `ks4-nav.js`'s fallback). Then delete
the throwaway batch entirely (its registry module, its authored dir, its
manifest/frozen file, its own `shared/`/`mrbadmus_site/shared/` assets —
including `ks4-nav.js`, since nothing is left to load it — and a scoped
`git checkout --` of the old pages it overwrote) and confirm `git status`
is clean again. Run this exact proof again whenever this engine changes;
if a change ever moves the pilot by one byte, find out why and fix the
generator — never re-freeze `ks4_pilot_manifest.json` to make it pass.
