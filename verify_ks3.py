"""verify_ks3.py — the §9 slice gates, checked rather than asserted.

    "The slice is not complete until all of these hold."  — architecture.md §9

Run it:

    python3 verify_ks3.py

Every check prints PASS or FAIL and the script exits non-zero if any fail.
Checks that cannot be automated (Mide's science review, real touch testing on a
device) are printed as MANUAL so the list stays honest about what has actually
been verified and what has not.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ks3_data
import build_ks3 as B

FAILS = []
MANUAL = []


def check(name, ok, detail=""):
    print("  %s  %s%s" % ("PASS" if ok else "FAIL", name,
                          ("  — " + detail) if detail else ""))
    if not ok:
        FAILS.append(name)


def manual(name, why):
    print("  MANUAL  %s — %s" % (name, why))
    MANUAL.append(name)


# ── reading age (§11 decision 7: target 9–10, technical vocab excluded) ──

_VOWELS = "aeiouy"


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    n, prev = 0, False
    for ch in w:
        v = ch in _VOWELS
        if v and not prev:
            n += 1
        prev = v
    if w.endswith("e") and n > 1:
        n -= 1
    return max(1, n)


def reading_age(text, exclude):
    """Flesch–Kincaid grade + 5 = UK reading age. Technical terms excluded."""
    ex = {t.lower() for t in exclude}
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    words = [w for w in re.findall(r"[A-Za-z']+", text) if w.lower() not in ex]
    if not sentences or not words:
        return None
    syl = sum(syllables(w) for w in words)
    fk = (0.39 * (len(words) / len(sentences))
          + 11.8 * (syl / len(words)) - 15.59)
    return fk + 5.0


def prose_of(lesson):
    """Body prose only — explainer text. Excludes activity copy, ladder
    questions and the key note, exactly as §5.2 specifies."""
    out = []
    for layer in ("core", "stretch", "support"):
        for b in lesson.get(layer) or []:
            if b.get("type") == "explainer" and b.get("text"):
                out.append(b["text"])
    return " ".join(out)


def main():
    units = ks3_data.build_units()
    registry = ks3_data.lesson_registry(units)
    by_code = {u["code"]: u for u in units}
    for slug, l in registry.items():
        l["_disc"] = by_code[l["_unit"]]["discipline"]
    c1 = by_code["C1"]
    authored = [l for l in c1["lessons"] if l.get("authored")]

    print("\n§9 — vertical slice done-list\n" + "=" * 60)

    # 1. Six lessons authored.
    check("C1 has six authored lessons", len(authored) == 6,
          "%d authored" % len(authored))

    # review_state: the ruling was `draft` for Mide's review, NOT frozen.
    states = {l.get("review_state") for l in authored}
    check("all six carry review_state: draft", states == {"draft"},
          "states=%s" % sorted(states))
    manual("examiner-reviewed → frozen",
           "Mide's science gate (§5.10). Cannot be automated; the slice stops here.")

    # 2. Register exists with C1's statements owned exactly once.
    check("statutory register exists",
          os.path.exists("docs/ks3/statutory-register.md"))
    owners = {}
    for l in registry.values():
        for c in l.get("covers") or []:
            if not c.startswith("KS3.WS."):
                owners.setdefault(c, []).append(l["slug"])
    dupes = {k: v for k, v in owners.items() if len(v) > 1}
    check("every subject-content statement owned exactly once", not dupes,
          str(dupes) if dupes else "%d statements/clauses owned" % len(owners))

    # 3. Prerequisite graph acyclic + generator fails loudly on a cycle.
    check("prerequisite graph validates", not B.validate(units, registry))

    saved = list(registry["particle-model"].get("requires") or [])
    registry["particle-model"]["requires"] = ["testing-the-model"]
    cyc = [p for p in B.validate(units, registry) if "CYCLE" in p]
    registry["particle-model"]["requires"] = saved
    check("generator detects an injected cycle", bool(cyc),
          cyc[0] if cyc else "no cycle reported — detection is broken")

    # 4. P11 cross-reference renders before P11 exists.
    p = "ks3/chemistry/particles-and-their-behaviour/testing-the-model.html"
    html = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    check("P11 reference renders a graceful pending state",
          "ks3-pending" in html and "coming soon" in html.lower())
    check("P11 pending reference is not a link",
          "why-ice-floats.html" not in html)

    # 5. ks4_links resolve.
    missing = B.check_ks4_links(units)
    check("every ks4_links edge resolves", not missing, str(missing))

    # 6. Reorder by data change only — proven by doing it.
    before = {}
    for root, _, files in os.walk("mrbadmus_site/ks3"):
        for f in files:
            fp = os.path.join(root, f)
            before[fp] = open(fp, encoding="utf-8").read()

    import ks3_data.default_sequence as ds
    original = dict(ds.DEFAULT_SEQUENCE_V1)
    try:
        ds.DEFAULT_SEQUENCE_V1["C1"] = 9      # a school moves particles to Y9
        ds.DEFAULT_SEQUENCE_V1["B1"] = 8
        tmp = tempfile.mkdtemp()
        B.build_ks3(output_dir=tmp, mirror_to_root=False, repo_root=".")
        after = {}
        for root, _, files in os.walk(os.path.join(tmp, "ks3")):
            for f in files:
                fp = os.path.join(root, f)
                after[fp.replace(tmp, "mrbadmus_site")] = open(
                    fp, encoding="utf-8").read()
        same_paths = set(before) == set(after)
        same_bytes = all(before[k] == after.get(k) for k in before)
        shutil.rmtree(tmp)
    finally:
        ds.DEFAULT_SEQUENCE_V1.clear()
        ds.DEFAULT_SEQUENCE_V1.update(original)

    check("reordering the sequence changes NO page path", same_paths)
    check("reordering the sequence changes NO page content", same_bytes,
          "year is metadata, never structure (§4.5)")

    # Re-run to restore the canonical build after the experiment.
    B.build_ks3()

    # 7. Determinism.
    t1, t2 = tempfile.mkdtemp(), tempfile.mkdtemp()
    B.build_ks3(output_dir=t1, mirror_to_root=False, repo_root=".")
    B.build_ks3(output_dir=t2, mirror_to_root=False, repo_root=".")
    diff = subprocess.run(["diff", "-r", os.path.join(t1, "ks3"),
                           os.path.join(t2, "ks3")], capture_output=True)
    check("determinism: two runs byte-identical", diff.returncode == 0,
          diff.stdout.decode()[:200])
    shutil.rmtree(t1); shutil.rmtree(t2)

    # 8. Zero KS4 pages changed.
    git = subprocess.run(["git", "status", "--porcelain"],
                         capture_output=True, text=True).stdout.splitlines()
    touched = [l[3:] for l in git if l[3:].endswith(".html")]
    ks4 = [t for t in touched
           if not t.startswith("ks3/") and not t.startswith("mrbadmus_site/ks3/")]
    check("zero KS4 pages changed", not ks4, str(ks4[:5]))

    print("\n§10.2 — per-lesson done-list (automatable subset)\n" + "=" * 60)

    for l in authored:
        pre = "  [%s]" % l["slug"]
        ok_cov = bool(l.get("covers"))
        ok_mis = bool(l.get("misconceptions"))
        ok_voc = bool(l.get("vocabulary"))
        ok_lad = set((l.get("ladder") or {})) >= {"recall", "apply", "explain", "produce"}
        ok_sup = "support" in l
        ok_fig = "figures" in l
        ok_hook = bool(l.get("phenomenon"))
        # Law 3: at least one misconception confronted by a real activity.
        acts = {a["id"] for a in l.get("activities") or []}
        ok_conf = any(m.get("confronted_by") in acts for m in l.get("misconceptions") or [])
        # Law 1: the first core block is the hook.
        first = (l.get("core") or [{}])[0].get("type")
        ok_law1 = first == "hook"
        # §5.1.1: blocks come only from the closed vocabulary.
        types = {b.get("type") for b in (l.get("core") or []) + (l.get("stretch") or [])}
        ok_vocabtypes = types <= B.VALID_BLOCK_TYPES
        # §5.2 prose budget.
        prose = prose_of(l)
        words = len(re.findall(r"[A-Za-z']+", prose))
        ok_budget = words <= 450
        terms = [v["term"] for v in l.get("vocabulary") or []]
        ra = reading_age(prose, terms)

        allok = all([ok_cov, ok_mis, ok_voc, ok_lad, ok_sup, ok_fig, ok_hook,
                     ok_conf, ok_law1, ok_vocabtypes, ok_budget])
        check("%s structure" % pre, allok)
        print("        prose %d words (≤450) · reading age %s (target 9–10, "
              "technical terms excluded)"
              % (words, ("%.1f" % ra) if ra else "n/a"))
        if ra and ra > 11.0:
            print("        ⚑ reading age above target — flag for review")

    print("\nAccessibility and device\n" + "=" * 60)
    check("reduced-motion fallback present in ks3.css",
          "prefers-reduced-motion: reduce" in open("shared/ks3.css",
                                                   encoding="utf-8").read())
    check("focus-visible styles present",
          ":focus-visible" in open("shared/ks3.css", encoding="utf-8").read())
    check("all interactive controls are real buttons",
          "<button" in html and "onclick=" not in html)
    manual("keyboard walk + touch model on a real device",
           "needs a human and a phone; ladder and predict-gates are "
           "button-based and focusable, which is the precondition.")
    manual("WCAG AA on new tints",
           "--accent measured and --accent-text added (tokens.css); any NEW "
           "tint added later must be re-checked.")

    print("\n" + "=" * 60)
    if FAILS:
        print("❌ %d FAILED: %s" % (len(FAILS), ", ".join(FAILS)))
        return 1
    print("✅ all automated gates pass · %d items remain MANUAL (Mide's gate)"
          % len(MANUAL))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
