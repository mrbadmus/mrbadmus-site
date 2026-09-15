"""prepush_gate.py — refuses a push while any gate is red, and names which.

⊕ MRB-277, 21 Aug 2026. Read `gate_registry.py` first; it explains the defect
this exists to stop, and (⊕ MRB-346) now carries a `watches` list on every
gate — the data everything below is built on.

── WHAT IT DOES ────────────────────────────────────────────────────────

    python3 prepush_gate.py --check              # the guard. exit 0 = safe
    python3 prepush_gate.py --record NAME         # run one gate, keep a receipt
    python3 prepush_gate.py --record-all          # run every AFFECTED slow gate
    python3 prepush_gate.py --record-all --force  # run every slow gate, period
    python3 prepush_gate.py --check --force       # require a fresh receipt for
                                                   # every slow gate, ignore
                                                   # "unaffected" as an excuse

`--check` is what the `pre-push` hook calls (see `hooks/pre-push`). It:

  1. refuses outright if tracked files are dirty — a gate result cannot be
     attributed to a tree that has changed since it ran;
  2. RUNS every `fast` gate, so those can never be skipped or selected away;
  3. for every `slow` gate, either finds a receipt that's still valid (see
     below), or decides — from this branch's own commits — whether the gate
     is even reachable by what changed, and reports one of PASS / SKIPPED /
     RED accordingly, never silently;
  4. reports every gate whose precondition (`needs` / `needs_env`) is absent
     as SKIPPED, by name — never silently, and never as a pass.

── ⊕ MRB-346, 15 Sep 2026 · RECEIPTS BIND TO WATCHED PATHS, NOT THE TREE ─

A receipt used to record the whole-tree sha (`HEAD^{tree}`) a gate passed
against, which meant ANY tracked change anywhere — a docs commit, an
unrelated subsystem's one-line fix — invalidated EVERY slow gate's receipt
at once. The night-2/worksheet landing spent real hours on exactly this:
docs commits invalidating all 18 receipts, twice, and a content-only branch
running the full site-drive suite that provably reads nothing from the
question bank.

A receipt now binds to a `watch_hash` — a fingerprint of the CONTENT (blob
sha) of every tracked file matching that gate's `watches` glob list, not the
rest of the tree. A gate's receipt survives any commit that doesn't touch a
path in its own `watches`. `docs/**`, `**/*.md`, `docs/**/shots/**`, and
`README*` can never appear in a `watches` list at all (`gate_watches_check`
enforces this), so a docs-only commit can never move any gate's `watch_hash`
— proof: after a green `--record-all`, a docs-only commit pushes with zero
re-runs.

This is only as honest as `watches` is complete. A `watches` list that's too
narrow means a real change the gate should have caught leaves its
fingerprint alone and a stale receipt keeps passing — which is why
`gate_watches_check` (a FAST gate, always run) asserts every gate at least
watches its own script, and an Opus-reviewed pass checked every gate's real
dependencies by hand before this shipped. It is not proof of completeness;
it is the best mechanical floor available.

── ⊕ MRB-346 · AFFECTED GATES ONLY ──────────────────────────────────────

`--record-all` and `--check` (the pre-push hook) both compute the paths this
branch's own commits touch — `git diff --name-only` from the merge-base with
`origin/main` to `HEAD` — and, for any SLOW gate with no already-valid
receipt, ask whether any of those paths falls inside that gate's `watches`.
If none does, the gate is reported SKIPPED BY RULE rather than RED: nothing
this branch did could have changed what it would find. A branch that only
touches `ks3_data/**` therefore only has to run the KS3 content gates; one
that only touches `shared/set-work.js` only has to run the Set-work and
teacher gates.

If the merge-base can't be determined (no local `origin/main`, a detached
history), the honest answer is "don't know", and the safe reading of "don't
know" is "affected", never "unaffected" — nothing is silently skipped for a
computation that failed. `--force` bypasses this and treats every slow gate
as affected, for the rare case a full sweep is deliberately wanted (e.g. the
first run after `watches` itself changed, when the list can't yet be trusted
to select correctly).

This selection only ever widens what runs on top of an already-red gate — it
never makes a genuinely red gate look green. An inherited red the branch
truly cannot reach (see the OVERRIDE mechanism below) still needs the same
override it always did whenever a full/forced run reaches it.

── ⊕ MRB-346 · ONE RETRY ON A TRANSIENT FAILURE ─────────────────────────

A DNS blip, Chrome closing its websocket mid-frame, a Render cold start —
none of these are findings about the code, and treating them as red the
first time turned nine unrelated gates red from one blip. Any gate whose
failing output matches a known transient signature (see
`_TRANSIENT_SIGNATURES`) is retried exactly once before it counts. The
retry is never hidden: a receipt records `"retried": true`, and the printed
PASS/FAIL line says so either way. A SECOND failure — whether or not it
matches a transient signature — is a real red, full stop; there is no loop.

── THE RECEIPT, AND WHY IT IS NOT COMMITTED ─────────────────────────────

Receipts live in `.gate-receipts/` and are NOT committed. They are evidence
about one working copy at one moment, and a committed receipt would be a
receipt for somebody else's machine.

── THE OVERRIDE, AND WHY IT LANDS IN THE COMMIT MESSAGE ─────────────────

There is an override, because a guard with no escape hatch gets deleted the
first night it is wrong at 2am, and a deleted guard protects nothing.

It is deliberately expensive:

    GATE-OVERRIDE: <gate-name> — <reason>

must appear in the message of the commit being pushed, once per red gate,
naming that gate. Not a flag, not an environment variable, not a prompt — the
commit message, because that is the only record that travels with the code to
everyone who ever reads the history. A flag is forgotten by the next morning;
`git log` still says it a year later.

An override that names no gate, or names a gate that is not red, is refused:
it would otherwise become a blanket the next person copies forward.
"""

import hashlib
import json
import os
import subprocess
import sys

import gate_registry

# ⊕ MRB-306, 3 Sep 2026 — ANCHORED TO THIS FILE, NOT TO THE PROCESS CWD.
#
# This read `RECEIPTS = ".gate-receipts"` and `_git()` ran with no `cwd`, so
# BOTH the receipt location and the tree being attested followed whatever
# directory the process happened to start in. Invoke it from anywhere but the
# repo root and it records a receipt for a DIFFERENT tree, or reads one — and
# it does that while printing a PASS.
#
# It was caught in the wild: a `--record verify_ks3` returned in seconds
# announcing "receipt written for tree 2b2c66db284e", a tree two commits
# behind HEAD, while no receipt file appeared in this worktree at all. The
# re-run took minutes and wrote the right one. A gate that can attest the
# wrong tree is worse than no gate, because it fails GREEN — and this is the
# file every push in the project trusts.
#
# Every other gate in the estate already derives its root from `__file__`
# (`leaderboard_seam`, `leaderboard_tells`, `student_page_drive`, …); this
# brings the arbiter into line with the things it arbitrates.
_REPO = os.path.dirname(os.path.abspath(__file__))
RECEIPTS = os.path.join(_REPO, ".gate-receipts")
OVERRIDE = "GATE-OVERRIDE:"

# ⊕ MRB-346. Substrings (matched case-insensitively against a failed gate's
# combined stdout+stderr) that mark a failure as plausibly TRANSIENT rather
# than a finding about the code. Deliberately generous — over-matching costs
# one wasted retry on a genuine red; under-matching leaves real flakiness
# blocking a push, which is the thing this exists to stop. A second failure,
# whatever the signature, always counts.
_TRANSIENT_SIGNATURES = (
    "urlerror",
    "connection refused",
    "connection reset",
    "temporary failure in name resolution",
    "getaddrinfo failed",
    "nodename nor servname provided",
    "name or service not known",
    "closed the websocket mid-frame",
    "timed out",
    "timeout",
    "[errno 60]",
    "[errno 61]",
    "sslerror",
)


def _git(*args):
    # `cwd=_REPO` is load-bearing: without it the tree this gate attests is
    # whatever repo the caller's shell was sitting in. See the note by RECEIPTS.
    return subprocess.run(["git"] + list(args), capture_output=True,
                          text=True, cwd=_REPO).stdout.strip()


def _tracked_dirty():
    """Tracked files with changes. Untracked files are not a gate concern."""
    out = _git("status", "--porcelain", "--untracked-files=no")
    return [l for l in out.splitlines() if l.strip()]


def _tree():
    return _git("rev-parse", "HEAD^{tree}")


def _tracked_files(ref="HEAD"):
    """{path: blob_sha} for every tracked file at `ref`, repo-root-relative,
    the same path shape `watches` patterns are matched against."""
    out = _git("ls-tree", "-r", ref)
    files = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        meta, path = line.split("\t", 1)
        _mode, _type, sha = meta.split()
        files[path] = sha
    return files


def _watch_hash(gate, files):
    """A fingerprint of every tracked file this gate's `watches` cover, at
    the tree `files` was built from. THIS, not the whole-tree sha, is what a
    receipt now binds to — see the module docstring."""
    matched = sorted(p for p in files
                     if gate_registry.matches_any(p, gate["watches"]))
    h = hashlib.sha1()
    for p in matched:
        h.update(p.encode("utf-8"))
        h.update(b"\0")
        h.update(files[p].encode("utf-8"))
        h.update(b"\n")
    return h.hexdigest()


def _merge_base():
    """Where this branch forked from `origin/main`, or None if that can't be
    determined. Never fetches — a push guard must not depend on the network,
    and a slightly stale local `origin/main` only ever makes MORE gates look
    affected, never fewer, which is the safe direction to be wrong in."""
    base = _git("merge-base", "HEAD", "origin/main")
    return base or None


def _changed_since_merge_base():
    """Paths this branch's own commits touch, or None meaning "unknown" —
    which `_affected` treats as "yes, affected", never "no"."""
    base = _merge_base()
    if not base:
        return None
    out = _git("diff", "--name-only", base, "HEAD")
    return [l for l in out.splitlines() if l.strip()]


def _affected(gate, changed):
    """Whether `gate` needs to run for THIS branch's push. `changed is None`
    means the merge-base couldn't be found, and the safe reading of "don't
    know" is "yes" — a gate silently skipped because a computation failed
    would be the exact failure this whole file exists to prevent, one level
    down."""
    if changed is None:
        return True
    return any(gate_registry.matches_any(p, gate["watches"]) for p in changed)


def _receipt_path(name):
    return os.path.join(RECEIPTS, "%s.json" % name)


def _read_receipt(name):
    try:
        with open(_receipt_path(name), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def _skip_reason(gate):
    need = gate.get("needs")
    if need and not os.path.exists(need):
        return "%s does not exist" % need
    # ⊕ MRB-282. A gate that reads production cannot run without a credential.
    # The alternative — letting the gate notice that for itself and exit 0 —
    # is a PASS that measured nothing, which is the failure mode this whole
    # guard exists to make impossible.
    env = gate.get("needs_env")
    if env:
        # A row may name ALTERNATIVES — student_controls_drive accepts either
        # MRB_DRIVE_PASSWORD or MRB_TEST_STUDENT_PASSWORD. Any one present is
        # enough; the skip only fires when none of them is.
        names = (env,) if isinstance(env, str) else tuple(env)
        if not any(os.environ.get(n) for n in names):
            return ("none of %s is set, so this gate cannot reach what it "
                    "checks" % ", ".join("$" + n for n in names))
    return None


def _looks_transient(output):
    low = output.lower()
    return any(sig in low for sig in _TRANSIENT_SIGNATURES)


def _run_once(gate):
    print("  running %-20s %s" % (gate["name"], " ".join(gate["cmd"])))
    r = subprocess.run(gate["cmd"], capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def _run(gate):
    """Run a gate, retrying ONCE if it fails with a transient signature.
    Returns (exit_code, output, retried) — `retried` is True the moment a
    retry was ATTEMPTED, whether or not it then passed."""
    code, out = _run_once(gate)
    if code == 0 or not _looks_transient(out):
        return code, out, False
    print("  RETRY   %-20s transient failure signature matched — retrying "
          "once" % gate["name"])
    code2, out2 = _run_once(gate)
    return code2, out2, True


def record(names, force=False):
    """Run the named gates and keep a receipt for each that passes.

    `force=False` narrows to gates AFFECTED by this branch's own commits
    (see `_affected`) — an unaffected slow gate is reported SKIPPED BY RULE
    and not run. `--record NAME` (one explicit gate) always passes
    `force=True`: naming a gate by hand means you want IT run, not a
    computed opinion about whether it's needed.
    """
    dirty = _tracked_dirty()
    if dirty:
        print("REFUSING TO RECORD — %d tracked file(s) are modified.\n"
              "A receipt attests a gate against its WATCHED FILES' content. "
              "With those moving under it, it would attest nothing.\n  %s"
              % (len(dirty), "\n  ".join(dirty[:10])))
        return 1
    os.makedirs(RECEIPTS, exist_ok=True)
    files = _tracked_files()
    changed = None if force else _changed_since_merge_base()
    bad = 0
    for name in names:
        gate = gate_registry.by_name(name)
        why = _skip_reason(gate)
        if why:
            print("  SKIP    %-20s %s" % (name, why))
            continue
        if not force and gate["speed"] == "slow" and not _affected(gate, changed):
            print("  SKIP-BY-RULE %-14s unaffected — no path this branch's "
                  "commits changed is in its `watches`" % name)
            continue
        code, out, retried = _run(gate)
        if code == 0:
            wh = _watch_hash(gate, files)
            with open(_receipt_path(name), "w", encoding="utf-8") as fh:
                json.dump({"gate": name, "watch_hash": wh,
                          "tree_at_record": _tree(), "exit": 0,
                          "retried": retried}, fh, indent=2)
            print("  PASS    %s — receipt written%s"
                  % (name, " (retried once)" if retried else ""))
        else:
            bad += 1
            # A failing gate must not leave a stale PASS receipt behind it.
            if os.path.exists(_receipt_path(name)):
                os.remove(_receipt_path(name))
            print("  FAIL    %s (exit %d)%s\n%s"
                  % (name, code, " [retried once, still red]" if retried
                     else "", "\n".join(out.strip().splitlines()[-15:])))
    return 1 if bad else 0


def check(force=False):
    print("── pre-push gate guard (MRB-277/346) " + "─" * 30)
    dirty = _tracked_dirty()
    if dirty:
        print("\n❌ REFUSED — %d tracked file(s) are modified.\n"
              "   Every gate result describes its watched files. Commit or "
              "stash first, so that\n   what was measured is what is being "
              "pushed.\n\n   %s"
              % (len(dirty), "\n   ".join(dirty[:10])))
        return 1

    files = _tracked_files()
    msg = _git("log", "-1", "--format=%B")
    changed = None if force else _changed_since_merge_base()
    red, skipped, ran, via_receipt = [], [], 0, 0

    for gate in gate_registry.GATES:
        why = _skip_reason(gate)
        if why:
            skipped.append((gate["name"], why))
            continue
        if gate["speed"] == "fast":
            code, out, retried = _run(gate)
            if code != 0:
                red.append((gate["name"], "exit %d — %s%s"
                            % (code, (out.strip().splitlines() or [""])[-1],
                               " [retried once]" if retried else "")))
            else:
                print("  PASS    %s%s" % (gate["name"],
                                          " (retried once)" if retried
                                          else ""))
            ran += 1
            continue

        rec = _read_receipt(gate["name"])
        wh = _watch_hash(gate, files)
        if rec is not None and rec.get("watch_hash") == wh:
            print("  PASS    %-20s (receipt — watched paths unchanged)"
                  % gate["name"])
            via_receipt += 1
            continue
        if not force and not _affected(gate, changed):
            skipped.append((gate["name"],
                            "SKIPPED BY RULE — unaffected: nothing this "
                            "branch's commits changed is in its `watches`. "
                            "`python3 prepush_gate.py --record %s` still "
                            "gives it a fresh receipt if you want one; "
                            "`--force` re-requires it unconditionally."
                            % gate["name"]))
            continue
        if rec is None:
            red.append((gate["name"],
                        "NEVER RUN against these watched paths — no "
                        "receipt. python3 prepush_gate.py --record %s"
                        % gate["name"]))
        else:
            red.append((gate["name"],
                        "receipt is for different watched-path content — "
                        "code this gate watches changed since it last ran. "
                        "Re-run: python3 prepush_gate.py --record %s"
                        % gate["name"]))

    for name, why in skipped:
        print("  SKIP    %-20s %s" % (name, why))

    rule_skipped = sum(1 for _n, w in skipped if w.startswith("SKIPPED BY RULE"))
    print("\n   %d gate(s) ran fresh, %d passed via an unchanged receipt, "
          "%d skipped by rule, %d skipped for a missing precondition."
          % (ran, via_receipt, rule_skipped, len(skipped) - rule_skipped))

    if not red:
        print("\n✅ every registered gate is green — push allowed.")
        return 0

    # ── an override must NAME the gate it is excusing ────────────────────
    excused, unexcused = [], []
    for name, detail in red:
        line = next((l.strip() for l in msg.splitlines()
                     if l.strip().startswith(OVERRIDE) and name in l), None)
        (excused if line else unexcused).append((name, detail, line))

    print("\n❌ %d GATE(S) RED:" % len(red))
    for name, detail, _line in [(n, d, None) for n, d in red]:
        print("     %-20s %s" % (name, detail))

    if unexcused:
        print("\n   PUSH REFUSED. %d of them carry no override.\n"
              % len(unexcused))
        print("   A red gate is a finding, not an obstacle: fix it, and do "
              "not weaken it to pass.\n")
        print("   If it genuinely must ship red, the commit being pushed has "
              "to say so, once\n   per gate, naming it:\n")
        for name, _d, _l in unexcused:
            print("       %s %s — <why this ships red>" % (OVERRIDE, name))
        print("\n   It goes in the COMMIT MESSAGE and nowhere else, so that "
              "`git log` still\n   says it long after the night it seemed "
              "reasonable.")
        return 1

    print("\n⚠️  PUSH ALLOWED UNDER EXPLICIT OVERRIDE — recorded in the "
          "commit message:")
    for name, _d, line in excused:
        print("     %s" % line)
    print("\n   This is now part of the history of the repository.")
    return 0


def main(argv):
    force = "--force" in argv
    if "--check" in argv:
        return check(force=force)
    if "--record-all" in argv:
        return record([g["name"] for g in gate_registry.GATES
                       if g["speed"] == "slow"], force=force)
    if "--record" in argv:
        i = argv.index("--record")
        if i + 1 >= len(argv):
            print("--record needs a gate name. Registry: %s"
                  % ", ".join(g["name"] for g in gate_registry.GATES))
            return 2
        return record([argv[i + 1]], force=True)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
