# QUEUE — lane: fix/site-defects

**Worktree:** `~/Documents/GitHub/mrbadmus-worktrees/fix-site-defects`
**Branch:** `fix/site-defects` (cut from `main` @ `14d9d405d`, 25 Jul 2026)
**Purpose:** small, self-contained production defects. One defect, one commit. Nothing speculative, no refactors, no redesign work.

---

## Standing rules for this lane

1. **Work only inside this worktree.** Never edit, stage, or read-modify files in
   `~/Documents/GitHub/mrbadmus-site` or in any other worktree under
   `~/Documents/GitHub/mrbadmus-worktrees/`. If a task seems to need a change elsewhere,
   stop and write it into the report instead.
2. **One session per worktree.** If another Code session is already open here, do not start a second.
3. **Commit freely.** Small, well-messaged commits are encouraged. You do not need permission to commit.
4. **NEVER push.** Mide pushes via GitHub Desktop, always. No `git push`, no PR creation.
5. **Follow the AUTONOMY CONTRACT** at the top of `CLAUDE.md` — act, don't ask. Stop only for
   irreversible loss, science/content accuracy, the production push, or genuine blockage.
6. **Run the generator before you commit.** `python3 generate_site_v5.py` — Cloudflare serves from
   `mrbadmus_site/`, not the repo root, so a generator change is not real until it is regenerated.
   Baseline verified 25 Jul 2026: the generator runs clean here and produces **zero** diff, so any
   diff you see afterwards is *your* change and nothing else.
7. **Deviations go in the final report, one line each** — not mid-run.

---

## Task 1 — MRB-141: mangled arrow function in the inline quiz stub

**Do this one first, and finish it (committed) before starting Task 2.**

### Step zero: read the ticket

**Linear was authenticated on 25 Jul 2026 — you should have Linear MCP tools available.** Read
**MRB-141** in Linear, in full, including comments, *before* you touch the code.

Everything below was reconstructed by reading the generator, not from the ticket, because the session
that wrote this queue had no Linear access. **Where the ticket and this queue disagree, the ticket
wins** — note the difference in your report. If the ticket adds acceptance criteria beyond what is
here, honour them.

### What is known

`generate_site_v5.py` emits an inline `<script>` block containing a legacy quiz stub. Around
**line 3560–3566** the `.forEach()` callback is written with a colon where the fat arrow belongs:

```
line 3563:  document.querySelectorAll('#qcard-0, ... , #qcard-4').forEach(():{{}});
```

The `{{}}` is Python f-string escaping, so the *emitted* JavaScript reads `.forEach(():{});`.
That is a hard `SyntaxError`. A SyntaxError aborts parsing of the **entire** `<script>` block,
so everything else declared in that block dies with it, on roughly 950 non-redesigned pages.

### What recon already established (verify it, don't trust it)

- The block declares exactly **one** top-level identifier: `const scoreMessages` (line 3562).
- `scoreMessages` appears **nowhere else** — not elsewhere in the generator, not in `shared/*.js`,
  and not even inside the block that declares it. It is declared and never read.
- The live quiz engine is `shared/quiz.js`, which boots off `.rd-exam[data-st]` and `.rd-checkpoint`
  and has no dependency on `scoreMessages` or any other legacy inline quiz global.

**Your job is to confirm this independently before deciding.** Re-grep for every identifier the
block declares, across the generator, `shared/`, and the generated output in `mrbadmus_site/`.
The question that decides repair-vs-delete is: *does anything downstream depend on what this block
declares?* If the answer really is "nothing", deleting the dead stub is the better fix than
repairing syntax on code nobody calls — fewer bytes on 950 pages and one less thing to rot. If you
find a genuine consumer, repair the arrow function instead and leave the block in place.

Whichever you choose, **say which and why in the commit message.**

### Proof required before you commit

Regenerate, then open real pages in a real browser (headless Chrome is fine — see the console-error
check pattern below) and confirm **zero** console errors on:

- one **biology** page
- one **physics** page
- one **non-bonding chemistry** page

…and confirm that whatever the block was supposed to power still behaves (or, if you deleted it,
that nothing regressed — the quiz UI on those pages is driven by `shared/quiz.js`).

A workable console check without a browser UI:

```bash
# adjust the chrome path if needed
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --headless --disable-gpu --dump-dom --virtual-time-budget=3000 \
  --enable-logging=stderr --v=1 \
  "file:///Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/fix-site-defects/mrbadmus_site/biology/....html" \
  2>&1 | grep -i "syntaxerror\|uncaught" || echo "NO CONSOLE ERRORS"
```

Run it **before** your fix as well, so you have a genuine before/after — a fix you cannot show
failing beforehand is a fix you have not proven.

### Regression guard — the bonding pages must not move

The bonding v2 redesign pages are freshly merged and are **not** in scope. After regenerating:

```bash
git status --porcelain -- mrbadmus_site/ | grep -i bond   # expect: no output
```

If any bonding page shows a diff, you have over-reached. Investigate before committing.

---

## Task 2 — MRB-130: dead font link and dead CSS rule on `.rd` pages

**Only start this after Task 1 is committed.**

A `<link>` to a font that is no longer used, plus a CSS rule targeting `.rd` pages that no longer
matches anything. Find both, confirm they are genuinely dead (grep the generated output for actual
usage of the font family and of the selector before removing — a rule that matches nothing *today*
may still be load-bearing for a page type you have not looked at), remove them, regenerate, and
verify no visual regression on an `.rd` page.

**Read MRB-130 in Linear first**, same as Task 1 — the ticket wins over this description, and it may
name the exact font and selector, which would save you the hunt.

---

## When you are done

Write a short report: what you changed, the before/after console evidence, the bonding-page
regression check result, and any one-line deviations. Leave the work committed on
`fix/site-defects`. **Do not push.**
