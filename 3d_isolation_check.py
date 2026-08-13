#!/usr/bin/env python3
"""3D Studio ↔ site generator isolation gate — spec §10, MRB-194.

The claim under test: a full generator run leaves `mrbadmus_site/3d/`
byte-identical, however the generator is invoked, and never deletes it even
when there is no Vite build to republish from.

`generate_site_v5.py` opens `build_site()` with a wipe loop that rmtree's
every top-level entry of `mrbadmus_site/` not named in `FOREIGN_OUTPUT_DIRS`,
and then exits 0. That loop has already silently deleted a whole generated
tree once (MRB-88: 221 KS3 pages before, 0 after, nothing complained). The
studio's protection is one string in one list, so this gate watches the
protection actually fail when that string is removed — a guard nobody has
seen fail is a guess, not a guard.

Six checks:

  1  publish        `3d-studio/dist/` → `mrbadmus_site/3d/`, files land
  2  identity       a second full generator run changes not one byte
  3  build_all      the same holds when invoked via build_all.py
  4  no-build       with dist/ absent, `3d/` survives untouched + shouts
  5  NEGATIVE       with "3d" out of the skip list, the run DELETES it
  6  staleness      with dist/ older than source, the run shouts

Checks 5 and 6 mutate state deliberately; every one of them restores it in a
`finally`, and the run ends by republishing from the real generator so the
tree is left exactly as a normal build leaves it.

Prerequisite: a Vite build must exist.

    cd 3d-studio && npm run build && cd ..
    python3 3d_isolation_check.py
"""

import hashlib
import os
import shutil
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(REPO, "3d-studio", "dist")
DIST_PARKED = os.path.join(REPO, "3d-studio", "_dist.isolation-check-parked")
DEPLOYED = os.path.join(REPO, "mrbadmus_site", "3d")
GENERATOR = os.path.join(REPO, "generate_site_v5.py")
NEG_GENERATOR = os.path.join(REPO, "_isolation_negative_generator.py")
SRC_TOUCH = os.path.join(REPO, "3d-studio", "src")

SKIP_LIST_REAL = 'FOREIGN_OUTPUT_DIRS = ["ks3", "3d"]'
SKIP_LIST_UNPROTECTED = 'FOREIGN_OUTPUT_DIRS = ["ks3"]'

failures = []
checks_run = 0


def ok(label, detail=""):
    global checks_run
    checks_run += 1
    print(f"  ✅ {label}" + (f" — {detail}" if detail else ""))


def fail(label, detail):
    global checks_run
    checks_run += 1
    failures.append(f"{label}: {detail}")
    print(f"  ❌ {label} — {detail}")


def fingerprint(root):
    """{relative path: sha256} for every file under root. {} if root is absent.

    Content only. Mtimes are deliberately excluded: copytree does not preserve
    them faithfully across every platform, and the claim is about bytes served
    to a student, not about filesystem metadata.
    """
    if not os.path.isdir(root):
        return {}
    out = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for name in sorted(filenames):
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, root)
            with open(path, "rb") as fh:
                out[rel] = hashlib.sha256(fh.read()).hexdigest()
    return out


def diff_fingerprints(before, after):
    """Human-readable account of what moved between two fingerprints."""
    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    changed = sorted(p for p in set(before) & set(after) if before[p] != after[p])
    parts = []
    if removed:
        parts.append(f"{len(removed)} deleted ({', '.join(removed[:4])})")
    if added:
        parts.append(f"{len(added)} added ({', '.join(added[:4])})")
    if changed:
        parts.append(f"{len(changed)} changed ({', '.join(changed[:4])})")
    return "; ".join(parts)


def run(cmd, label):
    """Run a build command from the repo root, returning (exit code, output)."""
    print(f"     ↻ {label} …", flush=True)
    started = time.time()
    proc = subprocess.run(
        cmd, cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )
    print(f"       done in {time.time() - started:.1f}s (exit {proc.returncode})")
    return proc.returncode, proc.stdout


def park_dist():
    """Move dist/ aside so the publication step takes its dist-absent branch."""
    if os.path.exists(DIST_PARKED):
        shutil.rmtree(DIST_PARKED)
    os.rename(DIST, DIST_PARKED)


def unpark_dist():
    if os.path.isdir(DIST_PARKED):
        if os.path.isdir(DIST):
            shutil.rmtree(DIST)
        os.rename(DIST_PARKED, DIST)


def main():
    print("\n🧪 3D Studio ↔ generator isolation gate (spec §10)\n")

    if not os.path.isdir(DIST):
        print("❌ ABORT: 3d-studio/dist/ does not exist.")
        print("   This gate proves the published studio survives a generator run;")
        print("   it needs a build to publish. Run:")
        print("       cd 3d-studio && npm run build && cd ..")
        return 1

    generator_source = open(GENERATOR, encoding="utf-8").read()
    if SKIP_LIST_REAL not in generator_source:
        print(f"❌ ABORT: could not find {SKIP_LIST_REAL!r} in generate_site_v5.py.")
        print("   The skip list moved or was renamed; check 5 cannot be built.")
        return 1

    # ── 1. Publish ────────────────────────────────────────────────────────
    print("1. Publication — dist/ reaches mrbadmus_site/3d/")
    code, _ = run([sys.executable, "generate_site_v5.py"], "generate_site_v5.py")
    if code != 0:
        fail("generator exits 0", f"exit {code}")
        return 1
    baseline = fingerprint(DEPLOYED)
    dist_print = fingerprint(DIST)
    if not baseline:
        fail("mrbadmus_site/3d/ populated", "nothing published")
        return 1
    ok("mrbadmus_site/3d/ populated", f"{len(baseline)} files")
    if baseline == dist_print:
        ok("published tree matches dist/ exactly", "file for file, byte for byte")
    else:
        fail("published tree matches dist/", diff_fingerprints(dist_print, baseline))

    # The whole point of hunk 3: no repo-root mirror of multi-MB GLBs.
    if os.path.exists(os.path.join(REPO, "3d")):
        fail("no repo-root ./3d/ mirror", "the round-trip created one")
    else:
        ok("no repo-root ./3d/ mirror", "round-trip opts 3d out")

    # ── 2. Byte-identity across a full generator run ──────────────────────
    print("\n2. Byte-identity — a second full generate_site_v5.py run")
    code, _ = run([sys.executable, "generate_site_v5.py"], "generate_site_v5.py")
    after = fingerprint(DEPLOYED)
    if code != 0:
        fail("generator exits 0", f"exit {code}")
    if after == baseline:
        ok("3d/ byte-identical after a full generator run", f"{len(after)} files unchanged")
    else:
        fail("3d/ byte-identical after a full generator run", diff_fingerprints(baseline, after))

    # ── 3. …and via build_all.py ──────────────────────────────────────────
    print("\n3. Byte-identity — via build_all.py (generator + build_ks3.py)")
    code, _ = run([sys.executable, "build_all.py"], "build_all.py")
    after = fingerprint(DEPLOYED)
    if code != 0:
        fail("build_all.py exits 0", f"exit {code}")
    if after == baseline:
        ok("3d/ byte-identical after build_all.py", f"{len(after)} files unchanged")
    else:
        fail("3d/ byte-identical after build_all.py", diff_fingerprints(baseline, after))

    # ── 4. dist/ absent → leave the deployed studio alone, loudly ─────────
    print("\n4. No build present — deployed studio survives, run shouts")
    park_dist()
    try:
        code, out = run([sys.executable, "generate_site_v5.py"], "generate_site_v5.py (no dist/)")
        after = fingerprint(DEPLOYED)
        if code != 0:
            fail("generator still exits 0 without a Node build", f"exit {code}")
        else:
            ok("generator still exits 0 without a Node build", "KS3/KS4 unaffected")
        if after == baseline:
            ok("3d/ left untouched when dist/ is absent", f"{len(after)} files unchanged")
        else:
            fail("3d/ left untouched when dist/ is absent", diff_fingerprints(baseline, after))
        if out.count("NO 3D STUDIO BUILD FOUND") >= 2:
            ok("absence is shouted, and repeated at the end of the run")
        elif "NO 3D STUDIO BUILD FOUND" in out:
            fail("absence repeated at the end of the run", "warned once, will scroll away")
        else:
            fail("absence is shouted", "no warning in the generator's output")
    finally:
        unpark_dist()

    # ── 5. THE NEGATIVE — remove the protection, watch it die ─────────────
    # dist/ stays parked for this one on purpose. With a dist present, the
    # publication step would rebuild 3d/ moments after the wipe deleted it,
    # and the deletion would be invisible — which is precisely the class of
    # silent failure this gate exists to make visible.
    print("\n5. Negative — with \"3d\" out of the skip list, the run deletes it")
    park_dist()
    try:
        unprotected = generator_source.replace(SKIP_LIST_REAL, SKIP_LIST_UNPROTECTED)
        if unprotected == generator_source:
            fail("negative variant built", "skip-list substitution did not apply")
        else:
            with open(NEG_GENERATOR, "w", encoding="utf-8") as fh:
                fh.write(unprotected)
            # Sits at the repo root because Python puts the *script's* directory
            # on sys.path, not the cwd — the all_subtopics_* imports need it.
            code, _ = run([sys.executable, os.path.basename(NEG_GENERATOR)],
                          "generator with 3d unprotected")
            survivors = fingerprint(DEPLOYED)
            if code != 0:
                fail("unprotected run still exits 0", f"exit {code} — the point is that it does not fail")
            if survivors:
                fail("unprotected run deletes 3d/",
                     f"{len(survivors)} files survived — the skip list is not what is protecting it")
            else:
                ok("unprotected run deletes 3d/",
                   f"all {len(baseline)} files gone, exit 0, no error — the MRB-88 failure mode")
    finally:
        if os.path.exists(NEG_GENERATOR):
            os.remove(NEG_GENERATOR)
        unpark_dist()
        run([sys.executable, "generate_site_v5.py"], "republishing after the negative")
        restored = fingerprint(DEPLOYED)
        if restored == baseline:
            print("     ↻ restored: 3d/ back, byte-identical to the baseline")
        else:
            failures.append(
                "restore after negative: 3d/ did not come back identical — "
                + diff_fingerprints(baseline, restored)
            )
            print("     ⚠️  restore imperfect — see failures")

    # ── 6. Staleness ──────────────────────────────────────────────────────
    # Mide's workflow is `python3 generate_site_v5.py` then GitHub Desktop.
    # There is no npm step in it, so a guarded publication ships the previous
    # build silently unless the run says otherwise, loudly.
    print("\n6. Staleness — source newer than dist/ is shouted, not noted")
    marker = os.path.join(SRC_TOUCH, "main.tsx")
    if not os.path.isfile(marker):
        candidates = [os.path.join(SRC_TOUCH, f) for f in sorted(os.listdir(SRC_TOUCH))]
        marker = next((c for c in candidates if os.path.isfile(c)), None)
    if marker is None:
        fail("staleness detectable", "no file in 3d-studio/src/ to age against")
    else:
        original_times = (os.path.getatime(marker), os.path.getmtime(marker))
        try:
            future = time.time() + 5
            os.utime(marker, (future, future))
            code, out = run([sys.executable, "generate_site_v5.py"], "generate_site_v5.py (stale dist/)")
            after = fingerprint(DEPLOYED)
            if code != 0:
                fail("stale build still exits 0", f"exit {code}")
            else:
                ok("stale build still exits 0", "KS3/KS4 unaffected by a stale studio")
            if out.count("STALE 3D STUDIO BUILD") >= 2:
                ok("staleness is shouted, and repeated at the end of the run")
            elif "STALE 3D STUDIO BUILD" in out:
                fail("staleness repeated at the end of the run", "warned once, will scroll away")
            else:
                fail("staleness is shouted", "a stale studio published silently")
            if after == baseline:
                ok("stale run still publishes dist/", "dist stays the single source of truth")
            else:
                fail("stale run still publishes dist/", diff_fingerprints(baseline, after))
        finally:
            os.utime(marker, original_times)

    # ── Verdict ───────────────────────────────────────────────────────────
    print("\n" + "─" * 70)
    if failures:
        print(f"❌ {len(failures)} of {checks_run} checks FAILED\n")
        for f in failures:
            print(f"   • {f}")
        print()
        return 1
    print(f"✅ all {checks_run} checks passed — mrbadmus_site/3d/ is isolated from the generator\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
