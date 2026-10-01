# KS4 batches — run report

Mide's ruling, 1 Oct 2026: Code writes the KS4 lessons. This report is
updated after each batch. Plan: `docs/ks4/BATCH-PLAN.md`. Engine:
`docs/ks4/batch-engine.md`. Brief: `docs/ks4/AUTHORING-BRIEF.md`.

## Batch status

| batch | lessons | state |
|---|---|---|
| 1 (pilot) | 14 | live since 26 Sep 2026 |
| 2 | 16 | in progress |

## Batch 2

_(filled when the batch ships)_

## For Mide

_(numbered route/spec rulings; filled as batches are examined)_

## Decisions I made

1. **Lesson format.** Code-authored lessons use Design's own `.dc.html`
   format, compiled by the same engine as the pilot, so the runtime, blocks,
   ladder, badges and visual language are the pilot's by construction.
2. **Pilot isolation.** Each batch ships its own `shared/ks4-*-<batch>`
   assets; the pilot's shared KS4 assets never change as batches are added,
   so the 54 pilot pages stay byte-identical. Cross-lesson links on batch
   pages resolve through a separate `shared/ks4-nav.js` covering every KS4
   subtopic.
3. **Route layers are data.** `data-route="higher|triple|triple-higher"` on
   an element; the build removes it off-route and adds the badge.
4. **Current teaching week** = week 5 (week 1 starts Sun 30 Aug 2026, the
   backend's `currentTeachingWeek()` rule). No term dates exist in either
   repo, so half-terms were assumed: weeks 5–8, then 10–16.
5. **Wrong frozen quiz items** stay verbatim in the practice bank (Mide's
   brief: keep verbatim and flag), are never ladder rungs, and are listed
   for Mide. Wrong frozen theory claims are not repeated in the re-cut
   prose. A wrong frozen `rp` field is not displayed; the RP block is
   written from the spec.
6. **Pilot classify gap left as is.** `states-of-matter`'s `sc-if`-wrapped
   section has always been unclassified; fixing it would move a pilot page,
   so the fix applies to batch lessons only.
7. **Full-build proofs set `CONSUMER_SIGNUP_ENABLED=true`**, matching what
   main's committed tree was built with; without it the B2C pages differ and
   swamp the diff.
