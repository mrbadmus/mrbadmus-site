# These are a SNAPSHOT. They are not the source of truth.

**Do not edit these files expecting a change to reach a student. Do not splice
them back in. Do not read them to find out how an instrument currently works.**

## What this directory is

Twelve KS3 instruments, four files each — `<kind>.renderer.py`, `<kind>.css`,
`<kind>.js`, `<kind>.parity.py` — exactly as they were handed to
`splice_instruments.py` when C1 and B2 were folded into the engine
(MRB-228, 16 Aug 2026).

It is a record of that splice, kept deliberately. It is **not** a component
library, it is **not** live source, and nothing about its shape says so: it is
the same twelve instruments in the same four-file layout in a directory that
reads exactly like one.

## Where the real source is

| What | Lives in |
|---|---|
| the renderer (`r_<kind>()`) and its dispatch row | `build_ks3.py` |
| the CSS block | `shared/ks3.css` |
| the wiring (`wire<Name>()`) | `shared/ks3.js` |
| the parity rows and drives | `ks3_parity.py` |

Every fix, ruling and correction made since the splice landed in **those four
files and nowhere else**. Nothing has ever been written back into this
directory.

## The drift, measured — 20 Aug 2026

Not asserted. Every fragment line was compared against the shipped engine:

| Fragment | Lines the shipped engine no longer contains |
|---|---|
| `collision-counter.js` | 16 |
| `collision-counter.renderer.py` | 7 |
| `gap-test-rig.js` | 4 |
| `halving-bench.js` | 4 |
| `halving-bench.renderer.py` | 3 |
| `random-walk-bench.js` | 1 |
| the other 20 files | 0 |

**35 lines across five files, and note which instruments they are.**
`collision-counter`, `gap-test-rig` and `halving-bench` are three of the C1
instruments that were found broken and fixed. The fixes went into the engine.
They were never written back here. So the fragments are not merely old — they
are old *in exactly the places where the engine was repaired*.

Among what a splice would revert: the collision counter's per-frame distance
normalised to 60 Hz, "so the count is a property of the gas rather than of the
monitor"; its NOTES flag 6 ruling that pressure is a count and a bar and never
a pascal; the halving bench's `if (next === n) { return; }` guard; the gap
rig's box geometry.

The CSS has **not** drifted — 158 of 158 blocks still match `shared/ks3.css`.
That is worth knowing precisely because it makes the directory look healthier
than it is: a spot-check of the styling would find nothing wrong.

## Why `splice_instruments.py` now refuses to run

Because the failure would have been silent.

The script is *re-runnable by design*: everything it writes sits between
`BEGIN`/`END` markers and a second run **replaces the whole marked region**
rather than appending beside it. That is the right design — fragments arrived in
waves, and appending would have shipped two copies of a renderer with only the
second's bugs visible.

It is also what makes running it today so quiet. There would be no duplicate to
notice, no error to read, and no diff anyone was looking for — just the shipped
renderers, CSS, wiring and parity rows replaced with a stale copy, in one pass,
deterministically. The regression would surface days later, somewhere else, as
three instruments that had "mysteriously" gone wrong again.

So the script exits non-zero and does nothing, and says why. See the
`_ARMED = False` block at the top of `splice_instruments.py`.

## If you are splicing a NEW unit

That is what the script is for, and the path is open:

1. Write that unit's own fragments, in its own directory.
2. Remove the `_ARMED = False` guard **deliberately**, in a commit that says
   why.
3. Splice, then treat the fragments as spent the moment the engine is edited
   again.

Step 2 is meant to be a decision somebody makes on purpose, not a default.

## Why this directory is not simply deleted

It is the record of how these instruments entered the engine, including the
`# DISPATCH:` and `// WIRE:` lines that document each one's registration. That
is worth keeping. Retire, never delete — the same rule KS3 figures follow.

The problem was never that it exists. It was that nothing said what it was.
