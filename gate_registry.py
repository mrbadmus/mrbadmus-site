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

`needs_env`:
    The same idea for a credential. `export_ks3_questions.py --verify` reads
    production over the network and cannot run without a password; the guard
    reports it as SKIPPED BY NAME rather than letting the gate decide for
    itself to exit 0 having measured nothing.

── ⊕ MRB-282, 23 Aug 2026 · THE REGISTRY COULD ITSELF LOSE A MEMBER ────

The paragraphs above describe a set that cannot silently lose a gate. Two days
later it had lost four: `ks3_key_audit`, `ks3_rail_manifest`,
`ks3_instrument_liveness` and `ks3_statutory` all existed, all worked, and
none had a row. It was not hypothetical — `ks3_rail_manifest` was RED on
`origin/main` when the chemistry lane merged, because `c8-07` had been checked
in without its manifest row and the guard does not run a gate it has never
heard of.

That is the SAME defect one level up. A hand-maintained list that nothing
compares against reality is a list that drifts, whether it lists gates or
lists lessons — and the previous version of this file said exactly that about
`verify_questions` in its own opening quotation.

So the list is now CHECKED. `EXCLUDED` below names every other executable
script in the repo root and says why it is not a gate, and `coverage()`
asserts that the two sets together account for all of them. A new script is a
red gate until somebody classifies it:

    python3 gate_registry.py --check

which is itself registered as the `gate_coverage` gate, so the assertion runs
on every push. A registry that can silently omit a member has the same shape
as the problem it was built to solve; this is the fix for the shape, not for
the four instances of it.
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

    # ── ⊕ MRB-282 · THE FOUR THAT WERE OUTSIDE THE REGISTRY ────────────

    dict(name="gate_coverage",
         cmd=["python3", "gate_registry.py", "--check"],
         speed="fast",
         why="the registry against the repo — every executable script at the "
             "root is a gate here or an entry in EXCLUDED with a reason. "
             "Without this the registry is a hand-maintained list nothing "
             "checks, which is the defect it exists to stop."),

    dict(name="ks3_statutory",
         cmd=["python3", "ks3_statutory.py", "--check-only"],
         speed="fast",
         why="the 155 statutory statements, and docs/ks3/statutory-register.md "
             "against the module that renders it. --check-only IS REQUIRED: a "
             "bare run used to REWRITE the register, which destroyed MRB-232's "
             "KS3.B.NUT.02 ruling while reporting PASS, and would dirty the "
             "tree the guard is checking."),

    dict(name="ks3_key_audit",
         cmd=["python3", "ks3_key_audit.py"],
         speed="fast",
         why="every authored data key against the code that reads it. An "
             "authored key nothing reads is teaching that was written and "
             "never rendered — invisible in a screenshot, because what is "
             "missing does not draw."),

    dict(name="ks3_rail_manifest",
         cmd=["python3", "ks3_rail_manifest.py"],
         speed="fast",
         why="the rail Design DREW against the rail the manifest records. "
             "THIS ONE HAS ALREADY FIRED: it was red on origin/main when the "
             "chemistry lane merged c8-07 without a manifest row, and nothing "
             "caught it because the guard did not run it. A bare run checks; "
             "only --write writes."),

    dict(name="ks3_instrument_liveness",
         cmd=["python3", "ks3_instrument_liveness.py"],
         speed="slow",
         why="the only gate that PRESSES THE BUTTONS. Every other KS3 gate "
             "measures the page at rest, so a dead instrument passes parity, "
             "overflow and contrast and does nothing when a student touches "
             "it."),

    # ── ⊕ MRB-282 · found by the sweep that added the four above ────────

    dict(name="student_switches",
         cmd=["python3", "student_switches.py", "--check"],
         speed="slow",
         needs="student_switches.json",
         why="Design's discrete breakpoint switches, measured in a browser "
             "against the recorded table. --check IS REQUIRED: a bare run "
             "OVERWRITES student_switches.json, which is tracked, so the "
             "gate would adopt the drift it is supposed to report."),

    dict(name="student_controls_drive",
         cmd=["python3", "student_controls_drive.py"],
         speed="slow",
         needs="mrbadmus_site/student/class-fixture.html",
         why="presses every control on the student pages and fails on one "
             "that does nothing. The student-side twin of "
             "ks3_instrument_liveness."),

    dict(name="export_ks3_questions_verify",
         cmd=["python3", "export_ks3_questions.py", "--verify"],
         speed="fast",
         needs_env="MRB_TEST_STUDENT_PASSWORD",
         why="the KS3 question mirror in Postgres against these files. The "
             "only check that the tables a student is actually served still "
             "match the authored questions. Reads production over the "
             "network, so it needs a password and is SKIPPED BY NAME without "
             "one."),

    dict(name="3d_parity",
         cmd=["python3", "3d_parity.py"],
         speed="slow",
         needs="3d-studio/dist",
         why="the studio shell against Design's screens (MRB-186). Needs a "
             "built studio; skipped, by name, without one."),

    dict(name="3d_render_check",
         cmd=["python3", "3d_render_check.py"],
         speed="slow",
         needs="3d-studio/dist",
         why="the mesh renderer in a real browser (MRB-187) — including that "
             "a missing GLB routes to the flat stage. Needs a built studio."),
]


# ── EVERYTHING ELSE AT THE REPO ROOT, AND WHY IT IS NOT A GATE ──────────
#
# One row per executable script that is NOT in GATES. A REASON, not a
# category: "it is a generator, and writing is the job" is a reason; "not a
# gate" is not.
#
# `coverage()` asserts GATES + EXCLUDED account for every *.py and *.sh at the
# repo root, so a new script cannot be quietly neither.

EXCLUDED = {
    # ── generators · they WRITE the site, by design ─────────────────────
    "build_all.py":
        "the entry point — runs the four generators in their load-bearing "
        "order. Writing is the job.",
    "build_ks3.py":
        "the KS3 generator. Its output is what the gates measure.",
    "build_student.py":
        "the student PREVIEW generator, gated by student_parity.",
    "build_student_port.py":
        "the LIVE student page generator, gated by student_behaviour.",
    "generate_site_v5.py":
        "the KS4 generator.",
    "ks3_seed_sow.py":
        "a GENERATOR of two tracked seed files (supabase/seeds/"
        "*_ks3_default_sequence.sql and *_ks3_school_schemes.sql), which it "
        "rewrites whole on every successful run with no check mode — the "
        "same shape as the ks3_statutory defect MRB-282 fixed. NOT "
        "registered and NOT fixed here on purpose: the 183 -> 185 "
        "scheme_of_work rewrite is parked by Mide, and giving this a "
        "--check-only would turn a parked disagreement into a red gate.",

    # ── libraries · imported, never the thing you run ───────────────────
    # gate_registry.py is NOT here: it is the `gate_coverage` gate above, and
    # a script cannot be both — coverage() reports that as a contradiction.
    "prepush_gate.py":
        "the guard that RUNS the registry. Gating the guard with the guard "
        "is the same circularity.",
    "ks3_browser.py":
        "the headless-Chrome harness every driven gate is built on. A "
        "library with no assertions of its own.",
    "ks3_parity.py":
        "the MRB-183 parity assertions. Imported and run by verify_ks3 "
        "(verify_ks3.py:1366), which IS registered.",
    "student_rulings.py":
        "Mide's MRB-275 rulings as source. Data, consumed by "
        "build_student_port.",
    "student_template.py":
        "Design's template, compiled. A library consumed by "
        "build_student_port.",

    # ── run INSIDE verify_ks3, which is registered ──────────────────────
    "ks3_canvas.py":
        "does the canvas redraw when you touch it — invoked by verify_ks3 "
        "(verify_ks3.py:2158). A second row would run it twice.",
    "ks3_figure_sweep.py":
        "every drawn figure at three widths — invoked by verify_ks3 "
        "(verify_ks3.py:432).",
    "ks3_overflow.py":
        "the 390px sideways-scroll gate — invoked by verify_ks3 "
        "(verify_ks3.py:2175).",

    # ── diagnostics · they REPORT, and a human reads the report ─────────
    "ks3_mutation.py":
        "source-level mutation testing of the parity assertions. Its "
        "valuable output is the supplying-selector column a human reads, it "
        "defaults to one unit (B3), and a full sweep is hours. Run it by "
        "hand when a parity row is suspect.",
    "student_diff.py":
        "what changes for a student between two built KS3 trees. A "
        "comparison tool with no correct answer to assert.",
    "student_shots.py":
        "photographs the wired student pages so a human can look. Produces "
        "images, asserts nothing.",
    "student_theme_shots.py":
        "photographs the six bench themes for the same reason. The "
        "assertions about those colours live in student_themes, which IS "
        "registered.",
    "audit_content.py":
        "the KS4 Phase 1 content audit. Rewrites 15 tracked files under "
        "docs/audit/ on every run, has no pass/fail verdict, and covers the "
        "KS4 subtopic data rather than anything KS3.",

    # ── they rewrite tracked source, on purpose ─────────────────────────
    "ks3_prose_swap.py":
        "an APPLY tool: it edits the authored .py source, rebuilds, checks "
        "the page moved, and reverts if it did not. Running it as a gate "
        "would rewrite the tree the gate is measuring.",
    "splice_instruments.py":
        "disarmed. Kept only as the record of what ks3_art/ replaced.",
    "bonding_redesign.py":
        "a one-off KS4 theory-block decomposition (MRB-113 Phase B).",

    # ── they drive PRODUCTION, with real credentials ────────────────────
    "student_api_drive.py":
        "drives the weekly assignment producer against PRODUCTION as a real "
        "student. Needs credentials and the network; a push must not depend "
        "on Render being awake.",
    "student_page_drive.py":
        "drives the wired student pages against production data. Same "
        "reason.",
    "student_submit_drive.py":
        "drives POST /api/assignment-submit against production. Same "
        "reason, and it WRITES rows.",
    "check_ks3_live.sh":
        "verifies mrbadmus.com AFTER a push, including the cache-bust "
        "stamps. It cannot run before the thing it checks exists.",
    "check_b1_live.sh":
        "the same, for B1's lessons.",
}

# The KS4 subtopic corpora are DATA, not scripts: one module each of AQA spec
# content, imported by generate_site_v5. Listed as a prefix rather than as
# twelve near-identical rows.
EXCLUDED_PREFIXES = {
    "all_subtopics_":
        "AQA KS4 subtopic content data, imported by generate_site_v5. No "
        "entry point and nothing to assert — the audit of this content is "
        "audit_content.py.",
}


def gate_scripts():
    """Every repo-root script that a GATES row actually invokes."""
    out = {}
    for g in GATES:
        for token in g["cmd"]:
            if token.endswith(".py") or token.endswith(".sh"):
                out.setdefault(token, []).append(g["name"])
    return out


def coverage(root="."):
    """Problems, as strings. Empty means every root script is accounted for."""
    import os
    problems = []
    gated = gate_scripts()

    present = sorted(f for f in os.listdir(root)
                     if (f.endswith(".py") or f.endswith(".sh"))
                     and os.path.isfile(os.path.join(root, f)))

    for f in present:
        if f in gated or f in EXCLUDED:
            continue
        if any(f.startswith(p) for p in EXCLUDED_PREFIXES):
            continue
        problems.append(
            "%s is neither a gate nor excluded. Add a row to GATES if it "
            "asserts something, or a row to EXCLUDED saying WHY it does not "
            "\u2014 a script that is quietly neither is how verify_questions "
            "spent weeks outside the set." % f)

    # The other direction: a row naming a file that is gone is a row nobody
    # will notice has stopped meaning anything.
    have = set(present)
    for f in sorted(gated):
        if f not in have:
            problems.append(
                "GATES row(s) %s invoke %s, which does not exist at the repo "
                "root." % (", ".join(gated[f]), f))
    for f in sorted(EXCLUDED):
        if f not in have:
            problems.append(
                "EXCLUDED names %s, which no longer exists. Delete the row so "
                "the list stays a description of the repo." % f)
    for pre in sorted(EXCLUDED_PREFIXES):
        if not any(f.startswith(pre) for f in have):
            problems.append(
                "EXCLUDED_PREFIXES names %s*, which now matches nothing." % pre)

    # Both at once is not belt-and-braces, it is two rows disagreeing: one
    # says the script is run on every push, the other says why it never is.
    for f in sorted(set(gated) & set(EXCLUDED)):
        problems.append(
            "%s is BOTH a gate (%s) and excluded. One of those rows is wrong."
            % (f, ", ".join(gated[f])))

    # A row that EXPLAINS a required mode and does not PASS it is the
    # ks3_statutory defect waiting to happen again: the registry says
    # --check-only, the cmd says nothing, and the "gate" rewrites the tree.
    for g in GATES:
        for flag in ("--check-only", "--check"):
            # Longest first, and stop at the first MENTION rather than the
            # first problem: "--check-only" contains "--check", so a row that
            # correctly passes --check-only would otherwise be reported as
            # failing to pass --check.
            if flag in g["why"]:
                if flag not in g["cmd"]:
                    problems.append(
                        "gate %s explains that %s is required and does not "
                        "pass it." % (g["name"], flag))
                break

    for g in GATES:
        if g["speed"] not in ("fast", "slow"):
            problems.append("gate %s has speed %r, which is neither fast nor "
                            "slow." % (g["name"], g["speed"]))
    return problems


def main(argv):
    if "--list" in argv:
        for g in GATES:
            print("  %-28s %-5s %s"
                  % (g["name"], g["speed"], " ".join(g["cmd"])))
        return 0
    if "--check" not in argv:
        print(__doc__)
        return 2
    problems = coverage()
    if problems:
        print("\u274c gate coverage: %d problem(s)\n" % len(problems))
        for p in problems:
            print("   \u00b7 %s" % p)
        print()
        return 1
    import os
    present = [f for f in os.listdir(".")
               if (f.endswith(".py") or f.endswith(".sh")) and os.path.isfile(f)]
    data = [f for f in present if any(f.startswith(p) for p in EXCLUDED_PREFIXES)]
    print("\u2705 gate coverage: %d root script(s) \u2014 %d gate(s) over %d "
          "of them,\n   %d excluded with a reason, %d content-data module(s)."
          % (len(present), len(GATES), len(gate_scripts()), len(EXCLUDED),
             len(data)))
    return 0


def by_name(name):
    for g in GATES:
        if g["name"] == name:
            return g
    raise KeyError("no gate named %r — the registry is %s"
                   % (name, ", ".join(g["name"] for g in GATES)))


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))
