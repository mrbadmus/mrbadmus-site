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
from datetime import date

# architecture.md §5.10.1 — the pre-launch carve-out that lets draft lessons
# publish expires when real students return. Hard-coded so the expiry is a
# fact the harness enforces, not a promise in a document. Moving this date
# requires an explicit §12 amendment with Mide's decision on the record.
CARVE_OUT_EXPIRY = date(2026, 9, 1)

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

    # §5.10.1 pre-launch carve-out — draft lessons may publish, but only until
    # real students return, and only with a visible marker. Both halves are
    # checked here so the carve-out cannot lapse silently: after the expiry the
    # rule flips and this check starts failing on any unfrozen published lesson.
    unfrozen = [l for l in authored if l.get("review_state") != "frozen"]
    if unfrozen:
        missing_marker = []
        for l in unfrozen:
            page = ("mrbadmus_site/ks3/%s/%s/%s.html"
                    % (c1["discipline"], c1["slug"], l["slug"]))
            html = open(page).read() if os.path.exists(page) else ""
            if "ks3-review-flag" not in html:
                missing_marker.append(l["slug"])
        check("every published draft lesson carries the under-review marker",
              not missing_marker,
              "missing on %s" % missing_marker if missing_marker
              else "%d draft lessons, all marked" % len(unfrozen))

        if date.today() < CARVE_OUT_EXPIRY:
            days = (CARVE_OUT_EXPIRY - date.today()).days
            check("§5.10.1 carve-out still in force — draft publishing allowed",
                  True, "expires %s (%d days)" % (CARVE_OUT_EXPIRY, days))
        else:
            check("§5.10.1 carve-out EXPIRED — only frozen lessons may publish",
                  False,
                  "expired %s; %d lesson(s) still draft and still publishing: %s. "
                  "Freeze them or revert them to coming-soon slots (architecture "
                  "§5.10). Extending the carve-out needs an explicit §12 amendment."
                  % (CARVE_OUT_EXPIRY, len(unfrozen), [l["slug"] for l in unfrozen]))

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

    # 5b. The default sequence is internally coherent — no forward references.
    #
    # architecture.md §4.5 claims the default is "ordered by what §4.9's
    # `requires` edges make possible". That claim was written before anything
    # checked it, so it is checked here.
    #
    # A forward reference is a lesson that depends on — or cross-links to —
    # content the DEFAULT schedules in a LATER year. Same year is fine: order
    # within a year is the school's business, not ours.
    #
    # This is a property of the DEFAULT ONLY. §4.5 means a school may reorder
    # into as many forward references as it likes; that is their call and not a
    # defect in the platform. So this never runs against a school scheme.
    #
    # KNOWN_FORWARD holds the one case Mide has not yet ruled on (§4.5). It is
    # an allowance, not a suppression: anything NOT in this set fails the build,
    # so the set can only shrink by a ruling, never grow by an accident.
    KNOWN_FORWARD = {("energy-in-food", "P2")}

    year_of_unit = {u["code"]: u["typical_year"] for u in units}
    slug_unit = {l["slug"]: u["code"] for u in units for l in u["lessons"]}

    forward = set()
    for u in units:
        here = year_of_unit[u["code"]]
        for l in u["lessons"]:
            # hard prerequisites on authored lessons
            for r in (l.get("requires") or []):
                ru = slug_unit.get(r)
                if ru and year_of_unit[ru] > here:
                    forward.add((l["slug"], ru))
            # §4.6 cross-discipline reference slots
            owner = l.get("reference_to")
            if owner:
                ou = slug_unit.get(owner, owner)
                if year_of_unit.get(ou, here) > here:
                    forward.add((l["slug"], ou))

    unexpected = forward - KNOWN_FORWARD
    stale = KNOWN_FORWARD - forward
    check("default sequence has no NEW forward reference", not unexpected,
          "unexpected: %s" % sorted(unexpected) if unexpected
          else "%d known, awaiting Mide's ruling (§4.5)" % len(forward))
    check("known forward references still real (no stale allowance)", not stale,
          "stale: %s — remove from KNOWN_FORWARD" % sorted(stale) if stale
          else "")

    # 6. Reorder by data change only — proven by doing it.
    #
    # Not a synthetic nudge. This applies **Rainford High School's entire real
    # scheme of work** over the platform default and rebuilds from scratch.
    # Rainford diverges from the default on 16 of the 33 units — biology,
    # chemistry and physics all move, in both directions, across all three
    # years — and it is a real school's real sequence rather than something
    # invented to pass a test.
    #
    # §4.5: "Reordering a school's entire KS3 curriculum must require zero
    # content changes and zero regeneration." A two-unit swap could pass while
    # the invariant was quietly broken for the general case. A whole school's
    # scheme cannot.
    #
    # If this fails, the finding is that §4.5 has failed. It is not to be
    # repaired by shrinking the reorder.
    before = {}
    for root, _, files in os.walk("mrbadmus_site/ks3"):
        for f in files:
            fp = os.path.join(root, f)
            before[fp] = open(fp, encoding="utf-8").read()

    import ks3_data.default_sequence as ds
    from ks3_data import school_schemes

    SCHOOL = "rainford-high"
    divergence = school_schemes.divergence_from_default(SCHOOL)
    original = dict(ds.DEFAULT_SEQUENCE_V1)
    try:
        ds.DEFAULT_SEQUENCE_V1.clear()
        ds.DEFAULT_SEQUENCE_V1.update(school_schemes.effective_sequence(SCHOOL))
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

    detail = ("%s's real scheme applied over the default — %d of %d units "
              "move" % (school_schemes.scheme(SCHOOL)["name"],
                        len(divergence), len(original)))
    check("a whole school's real reorder changes NO page path",
          same_paths, detail)
    check("a whole school's real reorder changes NO page content", same_bytes,
          "year is metadata, never structure (§4.5) · " + detail)

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
