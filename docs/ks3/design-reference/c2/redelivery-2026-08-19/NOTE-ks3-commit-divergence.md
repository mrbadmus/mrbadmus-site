# Carried in the 19 Aug C2 delivery's `_ds/tokens/shared-ks3.css`, nowhere else

Design's `_ds/` bundles re-ship the repo's own `shared/ks3.css` verbatim, so this is
not a Design drawing — it is a snapshot of `shared/ks3.css` **as it stood in some
other lane on 19 August**. It matters because that lane resolved the `.ks3-commit`
specificity trap DIFFERENTLY from the way main resolved it, and the two resolutions
will collide when that lane merges.

- **main** (`shared/ks3.css:402`, under the comment headed "⊕ GATE A"):
  `.ks3-dark .ks3-commit { color: var(--ks3-alert); }` — amber, argued from a
  browser walk showing every such commit line sits on `--ks3-ink` at 10.48:1 AAA.
- **the other lane** (MRB-245a, "gate A1", quoted verbatim below):
  `.ks3-dark .ks3-commit { color: var(--ks3-on-dark); }` — cream, explicitly
  declining to pick amber because doing so would repaint 103 hook blocks on one
  session's judgement, and flagging the choice for Mide.

Both scope the rule; they disagree only on the colour it resolves to. Both authors
flagged that the amber-vs-cream question is Mide's. It still is.

The bundle itself is not vendored — `docs/ks3/design-reference/*/_ds/` is gitignored
as packaging. Only this excerpt survives the delivery folder's removal.

```css

/* ⚠️ ELEVENTH OCCURRENCE OF THE SPECIFICITY TRAP — and the first one found by
   a gate instead of a screenshot (MRB-245a, gate A1).
   `.ks3-commit` asks for `--ks3-alert` at (0,1,0). `.ks3-dark p` is (0,1,1)
   and every commit prompt is a <p> inside a hook block, so the amber has NEVER
   rendered anywhere in the course: the class was inert for its entire life, the
   same defect class as MRB-179's inert token block. Authors reached for an
   inline `color:` to get the amber back, which is why nobody noticed.
   The scope resolves it to `--ks3-on-dark`: that is the cream that has in fact
   been shipping, brightened from body cream to full on-dark so the commit
   prompt outweighs the body text around it, which is what Law 4 wants of it.
   ⚠️ NOT resolved to amber, though amber is what the bare rule asks for.
   Amber here would repaint the commit line on all 103 hook blocks on my
   judgement alone, and `.ks3-dark .ks3-eyebrow` is already amber in the same
   block. Which of the two Design intended is a flag for Mide, not a call for
   the build. On LIGHT blocks the bare rule is untouched and still amber, which
   is correct for a prompt in an alert-tinted panel.
   This scope is a FIX, not a substitute for a gate — the gate exists, it caught
   this, and it will catch the twelfth. */
.ks3-dark .ks3-commit { color: var(--ks3-on-dark); }
```
