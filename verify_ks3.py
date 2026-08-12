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

# The served KS3 tree. Cloudflare serves from mrbadmus_site/, so this is the
# tree every gate below reads — never the ./ks3 root mirror, which is a copy.
KS3_OUT = os.path.join("mrbadmus_site", "ks3")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ks3_data
import build_ks3 as B
# Imported at module top ON PURPOSE. half_terms derives its placement at import
# time from DEFAULT_SEQUENCE_V1, and check 6 below temporarily swaps that dict
# for Rainford's map. Importing it lazily would derive half terms from a school
# scheme mid-experiment; importing it here derives them from the default, once.
from ks3_data import half_terms as HT

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
    b1 = by_code["B1"]
    authored = [l for l in c1["lessons"] if l.get("authored")]
    b1_authored = [l for l in b1["lessons"] if l.get("authored")]
    # Every authored lesson in the key stage with its unit attached, for
    # the checks that span units (the draft markers, the §10.2 done-list).
    all_authored = [(c1, l) for l in authored] + [(b1, l) for l in b1_authored]

    print("\n§9 — vertical slice done-list\n" + "=" * 60)

    # 1. Six lessons authored.
    check("C1 has six authored lessons", len(authored) == 6,
          "%d authored" % len(authored))

    # review_state: the ruling was `draft` for Mide's review, NOT frozen.
    states = {l.get("review_state") for l in authored}
    check("all six carry review_state: draft", states == {"draft"},
          "states=%s" % sorted(states))

    # 1b. MRB-198 — B1 authored: eight lessons, six statutory and two
    # carrying §7.6's declared beyond-statutory exemption. MRB-199 has no
    # ruling yet, so the two are gated here EXACTLY as Design authored
    # them; if Mide rules to drop them this check changes with the data.
    check("B1 has eight authored lessons", len(b1_authored) == 8,
          "%d authored" % len(b1_authored))
    b1_states = {l.get("review_state") for l in b1_authored}
    check("all eight B1 lessons carry review_state: draft",
          b1_states == {"draft"}, "states=%s" % sorted(b1_states))
    beyond = sorted(l["slug"] for l in b1_authored if l.get("beyond_statutory"))
    check("exactly two B1 lessons are beyond_statutory, as authored (MRB-199)",
          beyond == ["enzymes-and-rate", "stem-cells-and-meristems"],
          str(beyond))
    check("beyond_statutory is present and explicit on every B1 lesson",
          all("beyond_statutory" in l for l in b1_authored),
          "review-pack ruling 3: absent is a defect")

    manual("examiner-reviewed → frozen",
           "Mide's science gate (§5.10). Cannot be automated; the slice stops here.")

    # §5.10.1 pre-launch carve-out — draft lessons may publish, but only until
    # real students return, and only with a visible marker. Both halves are
    # checked here so the carve-out cannot lapse silently: after the expiry the
    # rule flips and this check starts failing on any unfrozen published lesson.
    unfrozen = [(u, l) for u, l in all_authored
                if l.get("review_state") != "frozen"]
    if unfrozen:
        missing_marker = []
        for u, l in unfrozen:
            page = ("mrbadmus_site/ks3/%s/%s/%s.html"
                    % (u["discipline"], u["slug"], l["slug"]))
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
                  % (CARVE_OUT_EXPIRY, len(unfrozen),
                     [l["slug"] for _, l in unfrozen]))

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
    #
    # The baseline is built HERE rather than read off disk. It used to snapshot
    # whatever mrbadmus_site/ks3 already held, which silently compared an OLD
    # build against a NEW one whenever the generator itself had changed — a
    # false FAIL at best, and at worst a real reorder defect masked by unrelated
    # generator drift. The comparison must isolate one variable: the sequence.
    # Scoped to the LESSON TREE, deliberately. Browse-layer pages are excluded
    # because this check cannot say anything true about them: the placement is
    # computed at import and the substitution below happens after, so browse
    # pages here are rendered from the original sequence either way. Comparing
    # them would be measuring nothing and reporting a pass. Check 6b covers the
    # browse layer properly.
    # What counts as "the browse layer" for the §4.5.2 split. Two things, and
    # the second is easy to miss: the year/half-term/subject tree under
    # `year-<n>/`, AND `/ks3/index.html` itself, which now renders the three
    # year cards with their unit and lesson counts. That page is the browse
    # layer's front door, so it moves with the sequence by design. Filing it
    # under "lesson tree" made check 6b fail and look like a §4.5 breach when
    # the only thing that had changed was a unit count on a nav card.
    def _is_browse(rel):
        return rel.split(os.sep)[0].startswith("year-") or rel == "index.html"

    def _lesson_tree(root_dir):
        out = {}
        for root, _, files in os.walk(root_dir):
            for f in files:
                fp = os.path.join(root, f)
                rel = os.path.relpath(fp, root_dir)
                if _is_browse(rel):
                    continue
                out[rel] = open(fp, encoding="utf-8").read()
        return out

    B.build_ks3()
    before = _lesson_tree("mrbadmus_site/ks3")

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
        after = _lesson_tree(os.path.join(tmp, "ks3"))
        same_paths = set(before) == set(after)
        same_bytes = all(before[k] == after.get(k) for k in before)
        shutil.rmtree(tmp)
    finally:
        ds.DEFAULT_SEQUENCE_V1.clear()
        ds.DEFAULT_SEQUENCE_V1.update(original)

    detail = ("%s's real scheme applied over the default — %d of %d units "
              "move" % (school_schemes.scheme(SCHOOL)["name"],
                        len(divergence), len(original)))
    check("a whole school's real reorder changes NO lesson page path",
          same_paths, detail)
    check("a whole school's real reorder changes NO lesson page content",
          same_bytes, "year is metadata, never structure (§4.5) · " + detail)

    # 6b. The browse layer is genuinely DERIVED from the sequence.
    #
    # ⚠️ Why this check has to exist, and why 6 above cannot be it.
    #
    # architecture.md §4.5.2 splits the invariant in two: lesson pages must not
    # move when the sequence changes, and browse-layer index pages MUST, because
    # they are the rendered sequence. Check 6 proves the first half. It cannot
    # prove the second, for a reason worth stating so nobody "simplifies" this
    # back: lesson pages never read half_terms at all, so check 6 would pass
    # even if the browse layer were hard-coded — and for a while it did exactly
    # that, because the placement is computed once at import and check 6
    # substitutes the sequence afterwards. The browse pages it compared were
    # rendered from the ORIGINAL placement, so "same bytes" was guaranteed by
    # construction and measured nothing.
    #
    # That is the same shape of latent flaw §12 already records once, when this
    # proof snapshotted its baseline off disk instead of building it. A proof
    # that cannot fail is not evidence.
    #
    # The perturbation is deliberately NOT Rainford's whole scheme. Rainford's
    # Year 9 biology is three lessons, which cannot be spread across six half
    # terms — half_terms.split_sizes raises, correctly, and weakening that guard
    # to make a test run would be the tail wagging the dog. Serving a school its
    # own browse layer is the Phase 5 runtime lookup (§4.5.2). So this uses the
    # smallest perturbation the default's own contract can hold: move Chemistry
    # C3 from Year 7 to Year 8. Every lane stays above the six-lesson floor
    # (Y7 chemistry 19 → 12, Y8 chemistry 22 → 29) and no SAME_YEAR_PREREQS edge
    # touches C3.
    from ks3_data import half_terms as HT

    def _split(tree_root):
        lessons, browse = {}, {}
        for root, _, files in os.walk(tree_root):
            for f in files:
                fp = os.path.join(root, f)
                rel = os.path.relpath(fp, tree_root)
                body = open(fp, encoding="utf-8").read()
                (browse if _is_browse(rel) else lessons)[rel] = body
        return lessons, browse

    base_dir = tempfile.mkdtemp()
    B.build_ks3(output_dir=base_dir, mirror_to_root=False, repo_root=".")
    base_lessons, base_browse = _split(os.path.join(base_dir, "ks3"))

    moved_dir = tempfile.mkdtemp()
    try:
        ds.DEFAULT_SEQUENCE_V1["C3"] = 8
        HT.recompute()
        B.build_ks3(output_dir=moved_dir, mirror_to_root=False, repo_root=".")
        moved_lessons, moved_browse = _split(os.path.join(moved_dir, "ks3"))
    finally:
        ds.DEFAULT_SEQUENCE_V1.clear()
        ds.DEFAULT_SEQUENCE_V1.update(original)
        HT.recompute()

    lessons_same = (set(base_lessons) == set(moved_lessons)
                    and all(base_lessons[k] == moved_lessons[k]
                            for k in base_lessons))
    browse_changed = base_browse != moved_browse
    changed_n = sum(1 for k in base_browse
                    if base_browse[k] != moved_browse.get(k))
    shutil.rmtree(base_dir)
    shutil.rmtree(moved_dir)

    check("moving a unit between years changes NO lesson page", lessons_same,
          "%d lesson-tree pages compared (§4.5.2)" % len(base_lessons))
    check("moving a unit between years DOES change the browse layer",
          browse_changed,
          "%d of %d browse pages differ — the browse layer is derived from the "
          "sequence, not hard-coded" % (changed_n, len(base_browse))
          if browse_changed else
          "browse layer is IDENTICAL after a reorder — it is not reading the "
          "sequence, so §4.5.2's second half is unproven")

    # Restore the canonical placement for everything downstream.
    HT.recompute()

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

    # 8. Zero KS4 pages changed — except the four the entry-point ruling
    #    deliberately changes.
    #
    # MRB-176 ruling 1 makes the landing a KS3/KS4 chooser and moves the old
    # landing to /ks4.html, so these four HAVE to change. They are named
    # individually rather than the check being loosened to "root pages": this
    # is an allowance, not a suppression, and any OTHER KS4 page appearing
    # here still fails, which is the property §8.2 actually wants.
    #
    # Not stale-checked, unlike KNOWN_FORWARD — this reads `git status`, so the
    # list legitimately empties the moment the work is committed.
    KS4_INTENDED = {
        "index.html",            # now the two-card chooser
        "ks4.html",              # the previous landing, verbatim, behind the KS4 card
        "combined/index.html",   # "back to home" re-pointed at /ks4.html
        "triple/index.html",     # same
        # MRB-180.1 — the KS3 "Explore topics" CTA pointed at /index.html,
        # which ruling 1 turned into the key-stage chooser, so a KS3 student
        # was sent back to choose KS3 or GCSE again. Now /ks3/index.html.
        # Same class of consequence as the four above: a KS4-tree page that
        # the entry-point ruling obliges us to change.
        "weekly-challenge.html",
    }

    # ⚠️ GATE CORRECTED 2026-08-07 (MRB-179). As written, this compared a KS4
    # page's *path* against an allow-list and failed on any other path that
    # `git status` reported. That cannot distinguish the two very different
    # things a KS4 page diff can mean:
    #
    #   (a) the page's CONTENT changed          — real KS4 drift, must fail
    #   (b) only its `?v=` cache-bust stamp moved, because a SHARED asset
    #       legitimately changed and generate_site_v5.py re-stamped every page
    #
    # (b) is not drift; it is the cache-busting machinery working as designed,
    # and it is unavoidable for any change to tokens.css — which is a shared
    # file KS3 is entitled to fix. Under the old gate, MRB-179's one-line
    # selector fix reported 1,000 "changed KS4 pages" and the honest response
    # would have been to loosen the gate, which is how a real regression gets
    # waved through later.
    #
    # So the gate now compares each page against HEAD with the version query
    # NORMALISED OUT. Stamp-only differences are counted and reported, never
    # silently dropped; ANY other byte difference still fails, on any path
    # outside KS4_INTENDED. This is strictly stronger than the path check it
    # replaces — it now catches a content change to an ALLOWED page too.
    VER = re.compile(rb"\?v=[0-9a-f]{8}")   # bytes: pages are compared raw

    def head_bytes(path):
        r = subprocess.run(["git", "show", "HEAD:%s" % path],
                           capture_output=True)
        return r.stdout if r.returncode == 0 else None

    git = subprocess.run(["git", "status", "--porcelain"],
                         capture_output=True, text=True).stdout.splitlines()
    touched = [l[3:] for l in git if l[3:].endswith(".html")]
    candidates = [t for t in touched
                  if not t.startswith("ks3/")
                  and not t.startswith("mrbadmus_site/ks3/")]

    stamp_only, content_changed = [], []
    for t in candidates:
        old = head_bytes(t)
        try:
            new = open(t, "rb").read()
        except OSError:
            new = None
        if old is None or new is None:
            content_changed.append(t)          # added or deleted — never a stamp
            continue
        if VER.sub(b"?v=NORM", old) == VER.sub(b"?v=NORM", new):
            stamp_only.append(t)
        else:
            content_changed.append(t)

    ks4 = [t for t in content_changed
           if t.replace("mrbadmus_site/", "", 1) not in KS4_INTENDED]
    check("zero UNINTENDED KS4 content changes "
          "(cache-bust restamps do not count, and are reported)",
          not ks4,
          str(ks4[:5]) if ks4 else
          "%d KS4 pages restamped (?v= only, no content change) · %d intended "
          "content changes, all in the MRB-176 ruling-1 allow-list"
          % (len(stamp_only), len(content_changed)))

    # 9. The KS4 generator must not destroy the KS3 output.
    #
    # build_site() wipes mrbadmus_site/ and rebuilds it. It used to take
    # mrbadmus_site/ks3/ with it, so running the two generators in the wrong
    # order silently shipped a site with no KS3 on it — and nothing failed,
    # because the KS4 build itself succeeded. generate_site_v5.py now lifts
    # foreign output trees out before the wipe and restores them after
    # (FOREIGN_OUTPUT_DIRS), which makes the order safe in both directions.
    #
    # This gate proves that is still true, by actually running the KS4
    # generator after the KS3 one and checking the KS3 output survived. It is
    # the check that would have caught the original hazard, so it is the check
    # that stops it coming back.
    ks3_pages_before = sorted(
        os.path.join(dp, f)
        for dp, _, fs in os.walk("mrbadmus_site/ks3") for f in fs)
    ks4_gen = subprocess.run([sys.executable, "generate_site_v5.py"],
                             capture_output=True, text=True)
    ks3_pages_after = sorted(
        os.path.join(dp, f)
        for dp, _, fs in os.walk("mrbadmus_site/ks3") for f in fs)

    check("KS4 generator ran clean", ks4_gen.returncode == 0,
          ks4_gen.stderr[-200:] if ks4_gen.returncode else "exit 0")
    check("running the KS4 generator AFTER build_ks3 does not destroy ks3/",
          bool(ks3_pages_after) and ks3_pages_after == ks3_pages_before,
          "%d KS3 files before, %d after%s"
          % (len(ks3_pages_before), len(ks3_pages_after),
             "" if ks3_pages_after == ks3_pages_before
             else "  ← generator order is load-bearing again; see "
                  "FOREIGN_OUTPUT_DIRS in generate_site_v5.py"))
    check("repo-root ks3/ mirror survives the round-trip too",
          os.path.isdir("ks3") and any(
              f.endswith(".html") for _, _, fs in os.walk("ks3") for f in fs),
          "root mirror present")

    # 10. Half-term placement (MRB-176 ruling 2).
    #
    # `ks3_data/half_terms.py` asserts most of this at import, so a broken
    # placement cannot even load. That is not a substitute for a gate: an
    # import assertion proves the module is self-consistent, and these checks
    # prove it is consistent with the curriculum the rest of the build sees —
    # the 183 slots build_units() actually produced, and the authored `requires`
    # edges the module deliberately cannot read (circular import).
    #
    # Everything here is recomputed rather than delegated back to the module's
    # own assertions, because a check that only re-runs the thing it is checking
    # verifies nothing.
    #
    # Half term is METADATA (§4.5), exactly as year is. Check 8 above already
    # proves no page changed; nothing below may ever become a reason for one to.
    placement = HT.placement()

    declared_slots = [(u["code"], l["slug"]) for u in units for l in u["lessons"]]
    expected_slots = ks3_data.structure.totals()["lessons"]
    missing = [s for s in declared_slots if s not in placement]
    extra = [s for s in placement if s not in set(declared_slots)]
    check("every lesson slot has a half term, exactly once",
          len(declared_slots) == expected_slots
          and len(placement) == expected_slots
          and not missing and not extra,
          "%d slots, %d placed%s%s"
          % (len(declared_slots), len(placement),
             "; unplaced: %s" % missing[:5] if missing else "",
             "; placed but undeclared: %s" % extra[:5] if extra else ""))

    counts = HT.counts_by_half_term()
    empty = ["Y%d %s HT%d" % (y, d, ht)
             for (y, d), row in sorted(counts.items())
             for ht, n in zip(HT.HALF_TERMS, row) if n == 0]
    check("every discipline appears in every half term of every year",
          not empty,
          "empty: %s" % empty if empty
          else "%d (year, discipline) streams × 6 half terms, none empty"
               % len(counts))

    backwards = []
    for (year, disc), codes in sorted(HT.INTRA_YEAR_UNIT_ORDER.items()):
        last = 0
        for code in codes:
            for l in by_code[code]["lessons"]:
                ht = placement[(code, l["slug"])][1]
                if ht < last:
                    backwards.append("Y%d %s %s/%s HT%d after HT%d"
                                     % (year, disc, code, l["slug"], ht, last))
                last = ht
    check("half term never goes backwards along a teaching stream",
          not backwards, str(backwards[:3]) if backwards else "9 streams monotonic")

    owner = {l["slug"]: u["code"] for u in units for l in u["lessons"]
             if not l.get("reference_to")}
    broken = []
    for dependent, prereq, why in HT.SAME_YEAR_PREREQS:
        dy, dht = placement[(owner[dependent], dependent)]
        py, pht = placement[(owner[prereq], prereq)]
        if dy != py or dht < pht:
            broken.append("%s (Y%d HT%d) requires %s (Y%d HT%d) — %s"
                          % (dependent, dy, dht, prereq, py, pht, why))
    check("every cross-discipline same-year prerequisite is reachable in time",
          not broken, str(broken[:2]) if broken
          else "%d ⇄ edges, all satisfied" % len(HT.SAME_YEAR_PREREQS))

    # The one check half_terms.py cannot make itself: reading authored lessons
    # means importing the package that would import it back.
    req_problems = HT.check_authored_requires(units)
    check("every authored `requires` edge inside one year is satisfied",
          not req_problems, str(req_problems[:3]) if req_problems
          else "checked against %d units" % len(units))

    print("\n  Lessons per half term — the distribution, stated so it is looked at:")
    print("        %s" % "  ".join("HT%d" % h for h in HT.HALF_TERMS))
    report = HT.search_report()
    for year in (7, 8, 9):
        for disc in ks3_data.structure.DISCIPLINES:
            row = counts.get((year, disc))
            if not row:
                continue
            print("    Y%d %-10s %s   (%d)"
                  % (year, ks3_data.structure.DISCIPLINE_TITLES[disc],
                     "  ".join("%2d" % n for n in row), sum(row)))
        r = report[year]
        print("    Y%d %-10s %s   (%d)   spread %d · %d of %d cuts snapped"
              % (year, "all three", "  ".join("%2d" % n for n in r["totals"]),
                 sum(r["totals"]), r["spread"], r["snapped"], r["available"]))
    print("        balance beats unit coherence — see RULED TRADE-OFF in "
          "ks3_data/half_terms.py")

    print("\n§10.2 — per-lesson done-list (automatable subset, C1 + B1)\n"
          + "=" * 60)

    for _u, l in all_authored:
        pre = "  [%s]" % l["slug"]
        # §10.2's covers rule has two legal halves: non-empty covers, OR
        # §7.6's declared exemption — beyond_statutory with covers EMPTY
        # and ks4_links non-empty. First exercised by B1 L7/L8 (MRB-199).
        ok_cov = bool(l.get("covers")) or (
            bool(l.get("beyond_statutory")) and not l.get("covers")
            and bool(l.get("ks4_links")))
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

    # ── §8.5 / MRB-179: both hooks, on every page, or the dials go dead again.
    # The KS3 token block is selected by `.rd[data-mode="ks3"]` — raised to
    # (0,2,0) so it outranks `.rd`, which had been silently winning and killing
    # every KS3 dial. The cost of that selector is that BOTH hooks are now
    # load-bearing: a page with only one gets no KS3 palette at all, and it
    # would look almost right, which is how the original defect survived. So
    # the pairing is asserted per page rather than trusted to the template.
    ks3_pages, bad_shell = [], []
    for dirpath, _dirs, files in os.walk("mrbadmus_site/ks3"):
        for fn in files:
            if not fn.endswith(".html"):
                continue
            p = os.path.join(dirpath, fn)
            ks3_pages.append(p)
            head = open(p, encoding="utf-8").read()
            if 'class="rd" data-mode="ks3"' not in head:
                bad_shell.append(p)
    check("every KS3 page carries BOTH class=\"rd\" and data-mode=\"ks3\"",
          ks3_pages and not bad_shell,
          "%d pages, all paired" % len(ks3_pages) if not bad_shell
          else "unpaired: %s" % bad_shell[:5])

    # The selector itself, so a future tidy-up cannot quietly undo the fix.
    tokens_css = open("shared/tokens.css", encoding="utf-8").read()
    check("tokens.css KS3 block outranks .rd (selector .rd[data-mode=\"ks3\"])",
          '.rd[data-mode="ks3"] {' in tokens_css
          and '\n[data-mode="ks3"] {' not in tokens_css)

    # ── §5.1.2(a) / MRB-177: a card grid discharges Law 4 by DECLARED
    # prediction, which only happens if the block asks for it in words. The
    # renderer cannot enforce a declaration — nothing is recorded — so the
    # prompt is the whole mechanism, and an author who omits it turns a
    # commitment device into a list of answers with a tap in the way.
    COMMIT_CUES = ("say", "decide", "predict", "answer", "work out", "name",
                   "think", "write")
    cardless_prompt = []
    for p in ks3_pages:
        page = open(p, encoding="utf-8").read()
        for m in re.finditer(r'<section\b[^>]*>(.*?)</section>', page, re.S):
            block = m.group(1)
            if 'class="ks3-cards"' not in block:
                continue
            before = block.split('<ul class="ks3-cards"')[0]
            texts = [re.sub(r"<[^>]+>", "", t).lower()
                     for t in re.findall(r"<p(?![^>]*\bhidden\b)[^>]*>(.*?)</p>",
                                         before, re.S)]
            prompt = " ".join(texts)
            if not (any(c in prompt for c in COMMIT_CUES)
                    and ("tap" in prompt or "check" in prompt
                         or "flip" in prompt or "turn" in prompt)):
                cardless_prompt.append(p)
                break
    n_grids = sum(1 for p in ks3_pages
                  if 'class="ks3-cards"' in open(p, encoding="utf-8").read())
    check("every reveal-card grid asks for a commitment before the tap",
          not cardless_prompt,
          "%d grids, all prompted" % n_grids if not cardless_prompt
          else "no commit prompt on %s" % cardless_prompt[:5])

    # ── MRB-181 / §8.10: the removed callout stays removed.
    check("no .ks3-browse-note survives in the built tree",
          not any("ks3-browse-note" in open(p, encoding="utf-8").read()
                  for p in ks3_pages),
          "%d pages clean" % len(ks3_pages))

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

    # ══ MRB-183 — the parity gate ══════════════════════════════════════
    #
    # Four layers, and what each does NOT catch is documented in
    # ks3_parity.py's module docstring rather than left to be discovered.
    # Layers A and B are cheap and always run. C and D need headless Chrome;
    # if it is absent they DEGRADE TO A MANUAL ITEM rather than silently
    # passing, because a skipped gate that prints PASS is worse than no gate.
    print("\n── MRB-183 parity gate ──")

    import ks3_parity as PARITY

    prov_problems, n_tokens = PARITY.check_provenance(".")
    check("A · every KS3 token colour traces to Design's frozen reference",
          not prov_problems,
          "%d colours checked" % n_tokens if not prov_problems
          else "; ".join(prov_problems[:3]))

    struct_problems, struct_notes = PARITY.check_structure(KS3_OUT)
    check("B · structural rules hold in the built tree (R3 R12 R13 R14 R15)",
          not struct_problems,
          "; ".join(struct_notes) if not struct_problems
          else "%d problem(s): %s" % (len(struct_problems),
                                      "; ".join(struct_problems[:3])))

    # MRB-203 — the gate learns to see a component that was never
    # registered. Absence-of-selector already failed; absence-of-
    # REGISTRATION passed silently, which is how B1 shipped with no
    # progress rail under a green gate.
    cov_problems, cov_rows = PARITY.check_design_coverage(".")
    check("MRB-203 · every authored family has a drawn reference screen, "
          "every rendered block type has a registered component",
          not cov_problems,
          "%d families + block types checked" % len(cov_rows)
          if not cov_problems else "; ".join(cov_problems[:2]))
    for label, detail, ok in cov_rows:
        print("       %s %-28s %s" % ("PASS" if ok else "FAIL", label, detail))

    # MRB-198 — the canvas paints text and state marks with token colours
    # layer D cannot reach through CSS; the pairs are computed from
    # tokens.css itself, the same file the canvas reads via cssVar().
    canvas_problems, canvas_rows = PARITY.check_canvas_contrast(".")
    check("D0 · canvas-drawn sim marks hold contrast (computed from tokens)",
          not canvas_problems,
          "%d pairs, worst %.2f:1"
          % (len(canvas_rows), min((r[1] for r in canvas_rows), default=0))
          if not canvas_problems else "; ".join(canvas_problems[:3]))

    try:
        import ks3_browser
        _have_browser = os.path.exists(ks3_browser.CHROME)
    except Exception as exc:                       # noqa: BLE001
        ks3_browser, _have_browser = None, False
        print("     (browser harness unavailable: %s)" % exc)

    if not _have_browser:
        manual("C+D · computed-style parity and contrast",
               "headless Chrome not available on this machine; run "
               "`python3 verify_ks3.py` where it is. NOT counted as a pass.")
    else:
        style_problems, style_rows, contrast_rows = \
            PARITY.run_browser_layers(KS3_OUT, ks3_browser)
        css_fails = [r for r in style_rows if not r[4]]
        check("C · resolved computed style matches Design, ±%gpx on lengths"
              % PARITY.TOL_PX,
              not css_fails,
              "%d assertions across %d components"
              % (len(style_rows), len(PARITY.COMPONENTS)) if not css_fails
              else "%d of %d assertions failed" % (len(css_fails),
                                                   len(style_rows)))
        cfails = [r for r in contrast_rows if not r[5]]
        # "worst" must mean the worst pair that had to CLEAR its bar. Letting a
        # WCAG-exempt row own that number reports the gate as weaker than it is
        # and buries the exemption in a headline nobody reads twice.
        held = [r for r in contrast_rows if "[exempt:" not in r[0]]
        exempt = [r for r in contrast_rows if "[exempt:" in r[0]]
        worst = min((r[3] for r in held), default=0)
        detail = "%d pairs, worst %.2f:1" % (len(contrast_rows), worst)
        if exempt:
            detail += " (+%d WCAG-exempt: %s)" % (
                len(exempt), ", ".join("%s %.2f:1" % (r[0].split(" [")[0], r[3])
                                       for r in exempt))
        check("D · every KS3 contrast pair re-measured against real grounds",
              not cfails, detail if not cfails else
              "%d FAIL: %s" % (len(cfails), ", ".join(r[0] for r in cfails[:3])))

        # MRB-202. The correct-answer state passing above only means something
        # if it is capable of failing, and for a whole release it was not —
        # the state was unregistered, so nothing compared it to anything. This
        # repaints a correct answer in the accent, exactly as the defect did,
        # and requires the gate to catch it and name the component.
        caught, mdetail = PARITY.mutation_test_correct_state(KS3_OUT, ks3_browser)
        check("C · a correct answer repainted in the accent FAILS the gate "
              "(mutation)", caught, mdetail)

        # The measured table is printed whether or not it passes — a number
        # nobody can see is a number nobody re-checks.
        print("\n     measured contrast (fg on resolved ground):")
        for name, fg, bg, ratio, need, ok in contrast_rows:
            print("       %-4s %-46s %6.2f:1  (needs %.1f)"
                  % ("PASS" if ok else "FAIL", name[:46], ratio, need))

        for p in style_problems:
            if p not in FAILS:
                print("       · %s" % p)

    print("\n" + "=" * 60)
    if FAILS:
        print("❌ %d FAILED: %s" % (len(FAILS), ", ".join(FAILS)))
        return 1
    print("✅ all automated gates pass · %d items remain MANUAL (Mide's gate)"
          % len(MANUAL))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
