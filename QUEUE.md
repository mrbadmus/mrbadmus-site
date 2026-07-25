# QUEUE — lane: content/ks3

**Worktree:** `~/Documents/GitHub/mrbadmus-worktrees/ks3`
**Branch:** `content/ks3` (cut from `main` @ `14d9d405d`, 25 Jul 2026)
**Purpose:** build KS3 Science — Years 7 to 9, all three sciences. This lane starts with **one topic
only**, built end to end, as the vertical slice every remaining topic will replicate.

---

## Standing rules for this lane

1. **Work only inside this worktree.** Never edit, stage, or read-modify files in
   `~/Documents/GitHub/mrbadmus-site` or in any other worktree under
   `~/Documents/GitHub/mrbadmus-worktrees/`. Reading `main` for reference is fine; writing to it is not.
2. **One session per worktree.** If another Code session is already open here, do not start a second.
3. **Commit freely.** You do not need permission to commit.
4. **NEVER push.** Mide pushes via GitHub Desktop, always.
5. **Follow the AUTONOMY CONTRACT** at the top of `CLAUDE.md` — act, don't ask. Stop only for
   irreversible loss, science/content accuracy, the production push, or genuine blockage.
6. **Science accuracy is Mide's gate, not yours.** Whether a KS3 explanation is correct, and whether
   it lands at the right level for Year 7 vs Year 9, is his call. Draft it; flag anything you are
   unsure of rather than quietly deciding.
7. **Deviations go in the final report, one line each** — not mid-run.

---

## Read these first, in this order

### 1. `docs/ks3/architecture.md` — the authoritative architecture

**As of 25 Jul 2026 this file DOES NOT EXIST in this worktree.** It is being written right now in a
parallel session.

**If it is still missing when you start: do not improvise. Report and stop.** Improvising a KS3
architecture and then having the real one land is the single most expensive mistake available in
this lane — it produces a slice that has to be thrown away, and a "pattern" document that teaches
the wrong pattern to every topic after it.

Before concluding it is missing, check whether it has landed since this worktree was cut:

```bash
git fetch                                   # if there is anything to fetch
git log --oneline --all -- docs/ks3/        # has any branch touched it?
ls ~/Documents/GitHub/mrbadmus-site/docs/ks3/ 2>/dev/null   # has it landed on main's checkout?
```

If it exists on `main` or another branch, bring it in (`git merge main`, or cherry-pick / checkout
just that path) and proceed. If it genuinely does not exist anywhere yet, write a one-line report
saying so and stop — that is the correct outcome, not a failure.

### 2. `docs/redesign/architecture_v2.md` — its laws apply here too

Ten laws. They govern the redesigned GCSE pages and they govern KS3 as well. The ones that will
shape your slice hardest:

- **Law 2** — the 150-word encode–act spine
- **Law 3** — three interactive scales, placed at demand peaks
- **Law 4** — predict before reveal
- **Law 6** — the production-ending exam ladder (① recall → ② apply → ③ explain → ④ extended response)
- **Law 7** — one design language
- **Law 10** — every activity exercises the demand it claims

Read the file; do not work from this summary.

---

## Task 1 — build ONE topic end to end (the vertical slice)

**Which topic:** follow `docs/ks3/architecture.md`'s own recommendation. If it names a first topic,
build that one.

If it does **not** name one, build **Particle Model**. Reasoning, so you can re-derive it if the
architecture disagrees: the existing schematic SVG library already covers particles, but has nothing
for cells, organs or body systems. Starting on a biology topic would force you to solve an unresolved
asset dependency *and* invent the pattern at the same time. Particle Model lets the slice be about
the pattern, which is the actual point.

**What "end to end" means here — all four, or the slice is not a slice:**

1. **The data structure** — how a KS3 topic is represented (whatever the architecture prescribes:
   a `.py` data module in the style of `all_subtopics_*.py`, or something new if the architecture
   says so). It must be able to express every other KS3 topic, not just this one.
2. **The renderer** — the code that turns that data into pages, consistent with how
   `generate_site_v5.py` works today. Extend rather than fork unless the architecture says otherwise.
3. **The rendered pages** — actually generated, actually opened in a browser, actually working.
   Interactions run, the exam ladder persists, no console errors.
4. **The pattern write-up** — a document (suggested: `docs/ks3/vertical_slice.md`) that turns the
   remaining topics into *assembly rather than invention*. It should tell the next session: where
   data goes, what fields mean, what the renderer expects, which parts are boilerplate, which parts
   need genuine authoring, and what the review checklist is. Write it as if for someone who has not
   read any of your reasoning — because they will not have.

**Stop after this one topic.** Do not start a second. Mide reviews the slice before the rest is
built on top of it — that review is the whole reason it is a slice.

---

## When you are done

Write a short report: which topic you built and why, how the data structure generalises, the browser
verification you ran, where the pattern write-up lives, and any one-line deviations. Leave the work
committed on `content/ks3`. **Do not push.**
