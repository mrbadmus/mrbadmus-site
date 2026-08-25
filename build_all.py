"""build_all.py — build the whole site, every generator, correct order.

Run it:

    python3 build_all.py

**This is the entrypoint to use.** The site is produced by two deliberately
separate generators:

* ``generate_site_v5.py`` → the KS4 site (982 pages: combined/, triple/, the
  hand-written root pages, shared/).
* ``build_ks3.py``        → the KS3 site (221 pages under ks3/).

They are separate on purpose — see the module docstring in ``build_ks3.py``.
Wiring KS3 into ``build_site()`` would rebuild 300+ KS4 pages on every KS3
content change and make architecture.md §9's "zero KS4 pages changed" gate
impossible to demonstrate.

Separate generators used to mean an order that mattered: ``build_site()``
wipes ``mrbadmus_site/`` and rebuilt it, which silently deleted
``mrbadmus_site/ks3/`` whenever the KS4 generator ran second. That hazard is
now fixed at source — ``build_site()`` SKIPS the foreign output trees named in
its ``FOREIGN_OUTPUT_DIRS`` where they stand, so the two generators are safe in
either order. (This paragraph used to say the trees were lifted out and put
back afterwards. That was an earlier fix, and it was replaced precisely because
it stranded the KS3 output in a temp directory if the build raised in between;
nothing is moved now.) This script exists so nobody has to know any of that:
run one command, get a complete site, every time.

``mrbadmus_site/3d/`` is on the same list as of MRB-194, but it is NOT built
here: 3D Studio is a Vite app, and ``npm run build`` inside ``3d-studio/`` is a
manual pre-step (see CLAUDE.md). A Node failure must not be able to fail a KS3
or KS4 build. The generator publishes whatever build exists and shouts, loudly
and twice, when that build is stale or missing.

The KS4 generator still runs first here, because that is the order the deploy
notes and the commit history describe, and there is no reason to diverge from
it now that either order is safe.
"""

import os
import subprocess
import sys

STEPS = [
    ("KS4 site — combined/, triple/, root pages, shared/", "generate_site_v5.py"),
    ("KS3 site — ks3/ (33 units, 185 lesson slots)",       "build_ks3.py"),
    # ⊕ MRB-270 phase 8a. LAST, and that ordering is load-bearing.
    # generate_site_v5.py rmtree's mrbadmus_site/ on the way in, so anything
    # emitted before it is deleted by it. build_student.py writes straight into
    # mrbadmus_site/student/ and mirrors to student/, exactly as build_ks3.py
    # does for ks3/, so it has to run after the tree exists.
    ("student preview pages — student/*-preview.html",     "build_student.py"),
    # ⊕ 22 Aug 2026 — ADDED WITH THE SWAP, and it is now load-bearing.
    #
    # This build used to write only previews, so leaving it out of the entry
    # point cost nothing. Since tonight it writes student/class.html and
    # student/assignment.html — the pages a signed-in student actually reaches.
    # Out of this list, editing student_rulings.py and running build_all.py
    # would print a successful build and change nothing, which is precisely
    # the silent-green failure this file's own docstring warns about for KS3.
    #
    # AFTER generate_site_v5.py, for the same reason build_student.py is:
    # the KS4 generator rmtree's mrbadmus_site/ on the way in and student/ is
    # not on its skip list, so anything written before it is deleted by it.
    ("student pages — student/class.html, student/assignment.html",
     "build_student_port.py"),
    # ⊕ MRB-287, 24 Aug 2026 — the teacher dashboard's seven pages.
    #
    # AFTER generate_site_v5.py, for exactly the reason the two student steps
    # are: the KS4 generator rmtree's mrbadmus_site/ on the way in, `teacher/`
    # is not on its FOREIGN_OUTPUT_DIRS skip list, and anything written before
    # it is deleted by it.
    #
    # And IN this list rather than left to be remembered, for the reason the
    # student port's own note gives: four of these seven — classes,
    # class-detail, student-detail and import — are the pages a signed-in
    # teacher actually reaches, and they are generated output as of tonight.
    # Left out, editing teacher_rulings.py and running build_all.py would
    # print a successful build and change nothing.
    ("teacher pages — teacher/*.html (6 screens, one URL each;\n    import.html is NOT ported and stays hand-written — see teacher_rulings)",
     "build_teacher_port.py"),
    # ⊕ MRB-290, 25 Aug 2026 — the KS4 weekly leaderboard.
    #
    # AFTER generate_site_v5.py for the reason the three steps above are: the
    # KS4 generator rmtree's mrbadmus_site/ on the way in and the site root is
    # not a foreign output tree.
    #
    # And there is a SECOND reason here that none of the others have.
    # generate_site_v5's own `_auth_file` list still names leaderboard.html
    # and copies the ROOT copy into mrbadmus_site/. Run before it, this
    # build's output would be overwritten by whatever sat at the root; run
    # after it, this build writes BOTH trees itself, which is what it does.
    # Do not reorder.
    #
    # ⊕ On the FIRST build_all after the retirement, step 1 prints
    # "⚠️ leaderboard.html not found — skipping", because this build has moved
    # the hand-written original to docs/ks3/retired/ and has not yet written
    # its replacement. That warning is expected, appears exactly once, and is
    # not a symptom: `_auth_file` skips a missing source rather than failing.
    ("KS4 weekly leaderboard — leaderboard.html (site root, both trees)",
     "build_leaderboard_port.py"),
]


def main():
    # ⊕ MRB-271 — the steps below are BARE SCRIPT NAMES, and a bare name
    # resolves against the current directory. Without this, running
    # `python3 /elsewhere/build_all.py` from inside a worktree ran the
    # WORKTREE's generators while reporting /elsewhere's name, and running it
    # from a directory with no generators at all failed three times over with
    # "can't open file". Anchor to this file's own directory: build_all always
    # builds the checkout it belongs to, whatever the invocation path.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("\n🏗️  build_all — %d generators, in order\n" % len(STEPS))

    for i, (label, script) in enumerate(STEPS, 1):
        print("─" * 72)
        print("  [%d/%d] %s" % (i, len(STEPS), label))
        print("         python3 %s" % script)
        print("─" * 72)

        result = subprocess.run([sys.executable, script])
        if result.returncode != 0:
            print("\n❌ build_all FAILED at step %d/%d (%s), exit code %d."
                  % (i, len(STEPS), script, result.returncode))
            print("   Later steps were NOT run — the output tree is incomplete.")
            return result.returncode
        print()

    print("─" * 72)
    print("✅ build_all complete — both generators ran, in order.")
    # ⊕ MRB-228 — this used to say "then Mide pushes via GitHub Desktop".
    # Push authorisation is standing and permanent; see CLAUDE.md's Autonomy
    # Contract. The shipping discipline is one unit, one commit, one push.
    print("   Next: check `git status`, run the unit's gates, commit and push,")
    print("         then verify live with ./check_ks3_live.sh <UNIT>.")
    print("─" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
