"""gate_registry.py — THE list of gates. One place, so a gate cannot be orphaned.

    "The gate was working; it was not run."
        — ks3_data/c7/questions_03_endothermic_reactions.py, on the defect
          that reached `main` in PR #8

⊕ MRB-277, 21 Aug 2026.

── WHY THIS FILE EXISTS ────────────────────────────────────────────────

`verify_questions.py` was written under MRB-269, works correctly, and was
referenced by NOTHING. Not by `verify_ks3.py`, not by a shell script, not by
a hook, not by CI. Grep the repo before this file existed and the only hits
are its own source, one comment in `ks3_data/c7/`, and two lines of prose in
`docs/`. It could only ever run if a human remembered it by name.

On 21 Aug 2026 nobody did, and `c7-03-e04` — a bank question restating its
apply rung verbatim, which `verify_questions` check 6 refuses — shipped to
`main` in PR #8. The run that shipped it reported "verify_ks3.py exit 0, all
automated gates" and that sentence was TRUE. The gate simply was not inside
the umbrella the sentence described.

So the defect was never "somebody ignored a red gate". It was that the set of
gates existed only in people's heads, and a set that exists only in heads
loses a member silently. This file is that set, written down, and
`prepush_gate.py` refuses a push against it.

── THE RULE FOR ADDING A GATE ──────────────────────────────────────────

A new gate script is not finished until it has a row here. A row costs one
line; the absence of one cost a defect on production and two runs to find it
by accident.

`speed`:
    "fast"  — no browser, runs in seconds. `prepush_gate.py` RUNS these
              itself on every push, so they can never be skipped.
    "slow"  — drives headless Chrome, takes minutes. Running these inside a
              hook would make the hook intolerable and an intolerable hook
              gets disabled, which is how a gate stops watching. Instead the
              guard requires a RECEIPT proving the gate passed against the
              exact tree being pushed. That turns "did you run it?" from a
              question of memory into a checkable fact.

`needs`:
    An optional path that must exist for the gate to be meaningful. A gate
    whose precondition is absent is reported as SKIPPED, by name, with the
    reason — never silently, and never as a pass.
"""

GATES = [
    dict(name="verify_questions",
         cmd=["python3", "verify_questions.py"],
         speed="fast",
         why="the KS3 question bank (MRB-269) — nine checks over every "
             "lesson's ladder and bank. THE ORPHAN: this is the gate that "
             "was red at push time in PR #8 and was not run."),

    dict(name="ks3_smoke_static",
         cmd=["python3", "ks3_smoke.py", "--static"],
         speed="fast",
         why="garbage strings in the built key stage — unsubstituted "
             "placeholders, stray markup, `undefined` reaching a page."),

    dict(name="3d_isolation",
         cmd=["python3", "3d_isolation_check.py"],
         speed="fast",
         needs="3d-studio/dist",
         why="spec §10 / MRB-194 — the published studio survives a generator "
             "run. Needs a build to publish; skipped, by name, without one."),

    dict(name="verify_ks3",
         cmd=["python3", "verify_ks3.py"],
         speed="slow",
         why="the §9 slice gates — the umbrella. Rebuilds the key stage and "
             "drives every lesson in headless Chrome."),

    dict(name="student_parity",
         cmd=["python3", "student_parity.py"],
         speed="slow",
         needs="student_parity.py",
         why="the generated student previews against Design's own file, "
             "layers A-H at 360/390/820/1460."),

    dict(name="student_behaviour",
         cmd=["python3", "student_behaviour.py"],
         speed="slow",
         needs="student_behaviour.py",
         why="the ported student pages driven against Design's own — 30 "
             "drives, visible text identical."),

    dict(name="student_themes",
         cmd=["python3", "student_themes.py"],
         speed="slow",
         needs="mrbadmus_site/student/class-fixture.html",
         why="the ported class page's COLOUR — six bench themes plus the "
             "attribute absent, grounds, tokens and every contrast ratio "
             "against the AA floor. The only gate that watches the port's "
             "palette: parity drives the PREVIEW pair and behaviour compares "
             "text, so a colour change ships unwatched without this."),
]


def by_name(name):
    for g in GATES:
        if g["name"] == name:
            return g
    raise KeyError("no gate named %r — the registry is %s"
                   % (name, ", ".join(g["name"] for g in GATES)))
