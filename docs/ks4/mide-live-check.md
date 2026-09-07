# The KS4 pool — the live check only Mide can run

**MRB-332 · about two minutes · on mrbadmus.com, signed in as yourself**

Claude has no production credential and never will: that is the standing rule,
not a gap to close. Everything that could be proved without one has been, and
is listed below so you know exactly what you are adding rather than repeating.
What is left needs your permissions, so it needs you.

Read the two corrections first — the script you were given names a class and a
topic that cannot work, and following it would look like a failure of the pool.

---

## ⚠️ Two corrections to the original script, and why

### 1. `temperature-changes-shc` cannot appear for `11h/Ph1`

It is a **Year 10** subtopic. The topic picker reads the scheme filtered by the
class's `year_group`, so a Year 11 class is never offered it. Nothing is wrong;
it is simply not that class's content. The script below uses subtopics that are
genuinely on `11h/Ph1`'s Year 11 scheme this week.

### 2. `10h/Sc2` cannot be the Foundation Combined arm — and this is a finding

`10h/Sc2` has **`tier = NULL` and `science_pathway = NULL`** on production. It
is not a Foundation Combined class in the data; it is a class with no tier and
no pathway at all.

That matters far beyond this script, so it is written up as finding **12** in
`findings-for-mide.md`. The short version:

> **36 of Rainford's 38 KS4 classes — 489 pupils — have null tier and null
> pathway, and would see an EMPTY topic picker.** Every KS4 scheme row has a
> non-null tier and pathway, and the backend matches `is null` against `is
> null`, so those classes match zero scheme rows. Only `11h/Ph1` (17 pupils)
> and `11r/Sc1` (33 pupils) are fully specified.

This is not the pool and not Set work. It is the class rows. But it decides
whether KS4 Set work does anything at all on 14 September, so it wants a
decision before then.

So the Combined arm below uses **`11r/Sc1`** (Year 11, higher, combined,
33 pupils), which *is* fully specified. It is a better comparison anyway:
`11h/Ph1` and `11r/Sc1` are both Year 11 and both Higher, so the only thing
that differs between them is **pathway** — which is precisely what we want to
see the product act on.

---

## What is already proved, without you

| proved | how |
|---|---|
| all 3,168 rows carry flags that agree with the curriculum | `ks4_pool_check` re-derives every one from `PATHWAY_TOPIC_MAP` |
| the four audiences nest and stay distinct — 2136 ⊂ 2268 ⊂ 2808 ⊂ 3168 | same gate; catches a rule that had quietly become a constant |
| 12 per subtopic, 4 per band, ids unique, four options, answer in range | same gate |
| the serving path applies the rule, not just the data | `ks4_pool_drive`, real sign-ins, nothing stubbed |
| no KS3 question can reach a KS4 class through the 8 colliding slugs | same drive, asserted on row **identity** (`ks4-` prefix), never on count |
| every subtopic the picker can offer has 12 rows behind it | prod scheme's 264 subtopics ≡ the pool's 264, set difference empty both ways |
| the pool is not readable by the public | anon-key read of `ks4_assignment_bank` returns zero rows |

**What none of that can prove** is that a real teacher, with real permissions,
on the real site, can get work to a real child. That is this page.

---

## The script

Sign in at **mrbadmus.com** as yourself. Times are a guide; the whole thing is
about two minutes.

### A · Triple Higher — the positive path

1. Open **`11h/Ph1`** → **Set work**.
2. **The topic picker lists topics.**
   ✅ Expect a list. ❌ A "no question bank for this class" refusal means the
   backend deploy did not land — stop and say so.
3. Look for **`meiosis`** in the list. It should be there.
   *(Biology, week 2, Triple-only. `11h/Ph1` is a physics class, but the scheme
   is per year-and-tier, not per subject, so all three sciences appear.)*
4. Pick a **physics** one — **`contact-noncontact-forces`** (this week) or
   **`scalar-vector-quantities`** (last week). Either has 12 questions.
5. **The preview shows real questions, with a Swap control.**
   ✅ Real GCSE physics, four options each. ❌ Placeholder text, blank options,
   or fewer than four options — stop and screenshot.
6. Press **Swap** on any one question. It should be replaced by a different
   question on the same subtopic.
7. Set it as **RELEASE LATER**, dated **after 14 September**.
   ⚠️ This is the one step that writes. The date is what guarantees no child
   can see it while you are testing.
8. Confirm it appears on **class detail** and on **Today**.
9. **Soft-delete it.** This is the only cleanup; please do not skip it.

### B · Higher Combined — the pathway difference

10. Open **`11r/Sc1`** → **Set work** → the topic picker.
11. **`meiosis` must NOT be in this list.** It is Triple-only, and this is a
    Combined class.
    ✅ Absent. ❌ Present — stop immediately and screenshot; that is a Combined
    class being offered Triple content.
12. The physics topics here are **`mass-number-isotopes`** and
    **`structure-of-atom`** — different from `11h/Ph1`'s, which is correct: the
    two pathways follow different sequences.
13. Open a preview and confirm real questions. **Do not set anything.**

---

## ⚠️ What step 11 does and does not prove

Worth being straight about, because it is easy to over-read.

`meiosis` is absent from `11r/Sc1` because the **scheme** does not offer it to a
Combined class — the topic picker filtered it out before the question pool was
ever consulted. The pool's own tier/triple filter is a **second, independent**
line of defence behind that one.

Scheme and pool were checked against each other for all 264 subtopics and they
agree exactly — 178 base, 234 foundation-reachable, 189 combined-reachable, on
both sides. That is by construction: both derive from `PATHWAY_TOPIC_MAP`.

So step 11 proves the journey is right end to end. It cannot, on its own,
distinguish "the pool filter works" from "the pool filter does nothing", because
on the default scheme there is nothing left for it to exclude. That distinction
is what `ks4_pool_drive` exists for, and it makes it on rows the scheme has
deliberately been made to allow.

Both lines are wanted. A scheme is editable; a pool filter that only works when
the scheme is already correct is not a defence.

---

## What to report back

For each step: what you saw, and a screenshot of anything unexpected.
Specifically worth a line either way:

- step 2 — did topics list, or did it refuse?
- step 5 — did the preview show real questions with four options?
- step 6 — did Swap actually change the question?
- step 8 — did it show on both class detail and Today?
- step 9 — **did the soft-delete work?**
- step 11 — was `meiosis` absent from `11r/Sc1`?

And the one that is not a step: **do you want the 36 null-tier KS4 classes
fixed before 14 September?** Without it, KS4 Set work is live for 50 pupils and
empty for 489.
