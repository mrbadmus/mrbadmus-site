# C2 redelivery, 19 August 2026 — held, not adopted

One file in this folder: a second, later drawing of **c2-06 Conservation of mass**.

## Why it is here and not in `../`

C2 was vendored on 16 August from Design's first delivery (commit `0eca304a0`) and
**built from that**. On 19 August a fresh `KS3 C2 lessons/` delivery arrived in the repo
root carrying a redrawn `c2-06`. Two drawings of one lesson, three days apart.

The standing rule for a root delivery that disagrees with a vendored one is: **keep the
vendored one.** The stated reason for that rule is that a vendored page may carry
post-delivery repairs the fresh delivery would silently undo. That reason does **not**
apply here — `git log` shows `../c2-06-conservation-of-mass.dc.html` has never been
touched since it landed, so there is nothing of ours to lose. But the rule was applied
anyway, because the vendored drawing is the one C2 was **built** from, and swapping the
reference under a built unit would put the built pages and their reference out of step
for no reason anybody asked for.

So the vendored `../c2-06` stays authoritative, and the newer drawing is kept here rather
than discarded. Retire, never delete.

## What actually differs

Both drawings teach the same physics and reach the same conclusion. The differences are
presentational, plus one data binding:

| | vendored (16 Aug, authoritative) | this redelivery (19 Aug) |
|---|---|---|
| the law statement | plain centred line, followed by a mono note — *"everything means the gases too / mass is measured in grams (g)"* | boxed in a bordered card, no units note |
| bar-model fills | `--ks3-card` | `--ks3-blue-tint` |
| bar-model row | centred (`justify-content: center`) | left-aligned |
| after the cover result | `{{ coverSentence }}` — a per-state sentence, then the shared explainer | shared explainer only, then three "g" unit pills |
| JS bindings | binds `COVERS[s.cover].sentence` | no `sentence` binding |

The vendored drawing is the stronger teach on the science: it names the units at the point
of stating the law and it varies the sentence with which part the student covered. The
redelivery's boxed statement is the stronger visual emphasis. Neither is wrong.

## What to do with it

Nothing, until C2 is next opened. When it is, this is the file to diff against — the
`coverSentence` binding in particular is worth keeping whichever drawing wins, because a
result line that changes with the student's choice is doing more teaching than one that
does not.
