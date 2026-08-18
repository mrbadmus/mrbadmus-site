"""verify_ks3.py — the §9 slice gates, checked rather than asserted.

    "The slice is not complete until all of these hold."  — architecture.md §9

Run it:

    python3 verify_ks3.py

Every check prints PASS or FAIL and the script exits non-zero if any fail.
Checks that cannot be automated (Mide's science review, real touch testing on a
device) are printed as MANUAL so the list stays honest about what has actually
been verified and what has not.
"""

import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

# ⊕ MRB-221 (Mide, 16 Aug 2026) — `CARVE_OUT_EXPIRY` and the pair of checks it
# drove are DELETED, not disabled. Architecture §5.10.1 is revoked: the content
# has been reviewed, publishing is no longer conditioned on `review_state`, and
# the page marker the checks demanded is no longer emitted. The assertion had to
# go in the same commit as the marker — an assertion that passes only when it
# FINDS a string the build no longer writes turns every live lesson red.

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

    # ⊕ MRB-221 — this used to pin every lesson to `draft`, which was correct
    # only while §5.10.1's carve-out made `draft` the publishing state. With the
    # carve-out revoked, publishing no longer consults `review_state` at all, so
    # pinning a value asserts nothing and would fail a later pass that legitimately
    # freezes a reviewed lesson. What survives is the field's §5.10 contract: it
    # must carry one of the three legal states, on every lesson.
    LEGAL_STATES = {"draft", "examiner-reviewed", "frozen"}
    states = {l.get("review_state") for l in authored}
    check("every C1 lesson carries a legal §5.10 review_state",
          states and states <= LEGAL_STATES, "states=%s" % sorted(states))

    # 1b. B1 authored. MRB-199 is now RULED: both slots that owned no statutory
    # statement are gone. `stem-cells-and-meristems` has no statement anywhere
    # in the KS3 spine. `enzymes-and-rate` was dropped OUTRIGHT rather than
    # moved to B3 — the catalyst clause it would have carried, KS3.B.NUT.04, is
    # already owned by B3's existing `enzymes-in-digestion` slot, and two
    # lessons competing for one ownable statement is the defect this ticket
    # closes. Enzyme rate has no KS3 statement at all and belongs in §7.6's
    # Year 9 bridge. B1 is six lessons, every one of them statutory.
    check("B1 has six authored lessons", len(b1_authored) == 6,
          "%d authored" % len(b1_authored))
    b1_states = {l.get("review_state") for l in b1_authored}
    check("every B1 lesson carries a legal §5.10 review_state",
          b1_states and b1_states <= LEGAL_STATES,
          "states=%s" % sorted(b1_states))
    # The §7.6 exemption machinery is deliberately KEPT and stays
    # mutation-tested — the Year 9 bridge unit will exercise it for real. What
    # MRB-199 changes is only the expected COUNT, which is now zero: no Year 7
    # lesson claims the exemption. If this ever goes non-empty again without a
    # bridge unit existing, that is precisely the defect MRB-199 was raised
    # about, and it fails here by name rather than shipping.
    beyond = sorted(l["slug"] for l in b1_authored if l.get("beyond_statutory"))
    check("no B1 lesson is beyond_statutory (MRB-199 ruled)",
          beyond == [], str(beyond))
    check("beyond_statutory is present and explicit on every B1 lesson",
          all("beyond_statutory" in l for l in b1_authored),
          "review-pack ruling 3: absent is a defect")

    manual("examiner-reviewed → frozen",
           "Mide's science gate (§5.10). Cannot be automated; the slice stops here.")

    # ⊕ MRB-221 — the under-review marker and the two checks that policed it are
    # gone. What replaces them is the inverse assertion: the marker must NOT
    # reach a page. Removing an emission without asserting its absence is how a
    # deleted mechanism grows back — a later pass copies a header from a page
    # built before the deletion and nothing notices.
    # Deliberately swept over EVERY authored lesson in the key stage, not over
    # `all_authored` — that list is C1 + B1 only, which was the whole key stage
    # when it was written and is now 12 of 30. A gate whose coverage silently
    # stops growing with the build is the same defect as no gate.
    marker_back = []
    for u in units:
        for l in u["lessons"]:
            if not l.get("authored"):
                continue
            page = ("mrbadmus_site/ks3/%s/%s/%s.html"
                    % (u["discipline"], u["slug"], l["slug"]))
            html = open(page).read() if os.path.exists(page) else ""
            if "ks3-review-flag" in html or "science-reviewed" in html:
                marker_back.append(l["slug"])
    swept = sum(1 for u in units for l in u["lessons"] if l.get("authored"))
    check("no lesson page carries the revoked under-review marker (MRB-221)",
          not marker_back,
          "marker is back on %s" % marker_back if marker_back
          else "%d authored lessons swept, none marked" % swept)

    # ⊕ MRB-248 — SEQUENCE MUST NOT LEAK ONTO A LESSON PAGE, and until now
    # nothing checked it.
    #
    # "Sequence is data — year and half-term never appear in a lesson URL or in
    # a lesson page's bytes. Write 'a student your age', never 'a Year 7'" has
    # been settled law since MRB-220. Grepped before writing this: there was no
    # assertion anywhere in this file that a page's bytes are free of either.
    # It has been kept for thirty lessons by authors reading the contract, which
    # is an arrangement that holds exactly until the first pass that does not —
    # and unlike most drift, this kind is invisible in review, because "Year 9
    # should already know this" reads as a helpful sentence rather than a defect.
    #
    # It matters because a school teaches these units in ITS OWN order. A page
    # that names a year contradicts the timetable of every school that sequences
    # differently, and the whole point of holding sequence in `half_terms.py`
    # and `school_schemes.py` is that the pages stay neutral.
    #
    # ⚖️ WHAT IT MUST NOT CATCH, and this is the harder half. b10-01's bench
    # prompt opens "Data from one year group." — ruled ALLOWED on 18 Aug 2026.
    # It names no year, pins the lesson nowhere, and describes the SAMPLE: sixty
    # people of roughly one age, which is why the height data has the spread it
    # has and is doing real teaching in a lesson about variation. The test is
    # the discernment §8.10 uses, not a word list: does the sentence say WHERE
    # THIS LESSON SITS, or something about the science in front of the student?
    # So the pattern requires a NUMBER beside the year — "Year 9" — and does not
    # fire on the bare phrase. A four-digit year is not matched either, or
    # b10-03's 1953 and 1962 would fail a gate about timetables.
    #
    # Swept over every authored lesson in the key stage, for the reason the
    # marker gate above gives: a gate whose coverage stops growing with the
    # build is the same defect as no gate. Lesson pages only — the browse layer
    # is ORGANISED by year and is where sequence legitimately lives.
    # ⚠️ THE PATTERN IS NARROW ON PURPOSE, and its first firing is why. Written
    # as `[Yy]ears?\s+[1-9]` it reported b6-02 `alcohol-and-smoking` leaking
    # "YEARS 4" — which is the PROGRESS RAIL: stop 3 is labelled YEARS (that
    # lesson's band is about years of life lost) and the 4 is the next stop's
    # number. Two separate elements, welded into a phrase by tag-stripping.
    #
    # Both halves of that are fixed below. Tags are replaced with a NEWLINE
    # rather than a space, so text from two elements can never form a phrase
    # that neither element contains. And the pattern wants capitalised singular
    # `Year` followed by a school year, which "YEARS" is not.
    #
    # Restricted to 7–11 because those are the school years this content could
    # plausibly name; a bare `[1-9]` would fire on every duration in the key
    # stage ("4 years", "one year 9 times over") and a gate that cries wolf gets
    # switched off. `half-term` needs no number and is never anything but
    # sequence, so it matches on its own, case-insensitively.
    YEAR_LEAK = re.compile(r"\bYear\s+(?:7|8|9|10|11)\b|\bhalf[-\s]?terms?\b",
                           re.M)
    seq_leaks = []
    for u in units:
        for l in u["lessons"]:
            if not l.get("authored"):
                continue
            page = ("mrbadmus_site/ks3/%s/%s/%s.html"
                    % (u["discipline"], u["slug"], l["slug"]))
            if not os.path.exists(page):
                continue
            # Tags stripped first: `data-year` and the like are structure, not
            # something a student reads, and the rule is about what is READ.
            text = re.sub(r"<[^>]+>", "\n", open(page).read())
            for hit in YEAR_LEAK.findall(text):
                seq_leaks.append("%s: %r" % (l["slug"], hit))
    check("no lesson page leaks a year or a half-term (sequence is data)",
          not seq_leaks,
          "%s" % seq_leaks[:5] if seq_leaks
          else "%d authored lessons swept, none names a year or a half-term"
               % swept)

    # ⊕ MRB-228 · the rung heading a student actually reads.
    #
    # `ladder.<rung>.title` was authored on four live B1 lessons and read by
    # NOTHING — every one of them shipped the engine's "2 · Apply" over the
    # wording Design wrote. The relabel wired it. This assertion is what stops
    # it going dead again, and it is deliberately an assertion about the BUILT
    # PAGE rather than about the renderer: a read site that stops being called
    # is exactly as silent as no read site at all.
    #
    # It checks the label reaches the page AND that the engine's number is in
    # front of it, which is the other half of the same defect — Design writes
    # the title as a whole heading ("Rung 1 · Name the job"), so a renderer that
    # forwarded it verbatim would drop no text and still be wrong.
    rung_misses = []
    for u, l in all_authored:
        page = ("mrbadmus_site/ks3/%s/%s/%s.html"
                % (u["discipline"], u["slug"], l["slug"]))
        if not os.path.exists(page):
            continue
        html = open(page).read()
        for key, num, name in B.LADDER_RUNGS:
            q = (l.get("ladder") or {}).get(key)
            if not q or not q.get("title"):
                continue
            want = ('<h3 tabindex="-1">Rung %d · %s</h3>'
                    % (num, B.e(B._rung_title(name, q))))
            if want not in html:
                rung_misses.append("%s/%s" % (l["slug"], key))
    authored_titles = sum(
        1 for _, l in all_authored for key, _n, _t in B.LADDER_RUNGS
        if ((l.get("ladder") or {}).get(key) or {}).get("title"))
    check("every authored ladder rung title reaches its built page",
          not rung_misses,
          "not on the page: %s" % rung_misses if rung_misses
          else "%d authored rung titles, all rendered under their number"
               % authored_titles)

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
    # KNOWN_FORWARD holds the cases Mide has not yet ruled on (§4.5). It is an
    # allowance, not a suppression: anything NOT in this set fails the build, so
    # the set can only shrink by a ruling, never grow by an accident.
    #
    # ⊖ EMPTY since 16 Aug 2026 (MRB-228), and it emptied by a RULING, which is
    # the only way it is allowed to. Its single entry was
    # `("energy-in-food", "P2")` — B3's slot pointing forward at a Physics unit
    # taught a year later. MRB-232 split `KS3.B.NUT.02` and gave B3 its own
    # owned lesson, so the reference slot that created the forward edge no
    # longer exists and there is nothing left to allow.
    #
    # The `stale` check below is what made this visible rather than leaving a
    # dead allowance sitting here: an entry that no longer describes a real
    # forward reference is a standing permission for a defect nobody is
    # watching for. It failed the build the moment the ruling landed, which is
    # exactly what it is for.
    KNOWN_FORWARD = set()

    year_of_unit = {u["code"]: u["typical_year"] for u in units}
    slug_unit = {l["slug"]: u["code"] for u in units for l in u["lessons"]}

    forward = set()
    for u in units:
        here = year_of_unit[u["code"]]
        for l in u["lessons"]:
            # hard prerequisites on authored lessons.
            #
            # ⊕ MRB-245 — through `B._require_slug`, because a `requires` edge
            # may now be a `{unit, lesson}` record as well as a bare slug (the
            # shape `references` has taken since B1, and the one b7-03 uses to
            # require B3's `food-tests`). Reading the raw entry here raised
            # `unhashable type: 'dict'` out of a dict lookup, three functions
            # from the record — the same failure the generator's own cycle
            # check hit. One normaliser, so the gate and the build cannot
            # disagree about what a prerequisite is.
            for r in map(B._require_slug, l.get("requires") or []):
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

    # ⊕ MRB-248, 18 Aug 2026 — `docs/` is excluded, and that is a SCOPE
    # correction, not a loosening.
    #
    # This gate asks one question: did a KS3 change alter a page a KS4 student
    # is served? It answered it by taking every touched `.html` outside `ks3/`
    # to be a KS4 page. Design's delivered lesson references are `.dc.html`
    # under `docs/ks3/design-reference/`, so they satisfied that test while
    # being neither KS4 nor served — they are the SOURCE the KS3 build is
    # measured against.
    #
    # It never fired before because the gate only inspects files `git status`
    # reports, and the four frozen units sat unchanged. MRB-248 checked in the
    # remaining nine deliveries, every one of them an addition, and the gate
    # reported Design's own reference pages as KS4 drift.
    #
    # The exclusion is guarded rather than trusted: `docs/` is asserted below
    # to be absent from the published tree. If that ever stops being true the
    # assertion fails, instead of this filter quietly hiding a real page.
    published_docs = os.path.isdir(os.path.join("mrbadmus_site", "docs"))
    check("the tree excluded from the KS4-drift scan is genuinely not published",
          not published_docs,
          "mrbadmus_site/docs/ does not exist" if not published_docs else
          "mrbadmus_site/docs/ EXISTS — docs/ is now served, so excluding it "
          "from the KS4-drift scan would hide student-facing pages")

    candidates = [t for t in touched
                  if not t.startswith("ks3/")
                  and not t.startswith("mrbadmus_site/ks3/")
                  and not t.startswith("docs/")]

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

    # ── the font subset, against the characters that carry science ──────
    #
    # ⊕ MRB-220. Design's NOTES-C2 flag 13 asks whether `CaCO₃`'s subscript
    # survives the generator's font subset. It does not, and the flag
    # understates the count: FIVE subscripts are used across C2 (₁₂₃₄₆) and
    # none of them is in any shipped woff2. Every other meaning-bearing
    # codepoint in the unit IS — U+2212 MINUS, °, ³, ã — and this gate is
    # what keeps that true.
    #
    # The build's own precedent for taking this seriously is in `build_ks3.py`
    # beside LADDER_RUNGS: circled digits U+2460–2463 "are not [in the subset],
    # and rendered as tofu inside a Bricolage-800 heading."
    #
    # Two halves, deliberately. The COVERED set is a real check and fails the
    # build if a font is ever re-subset smaller. The uncovered subscripts are
    # a MANUAL item, not a FAIL: the characters are Design's own bytes on an
    # approved page (MRB-205 — page wins), a browser renders them through
    # system fallback rather than as tofu on every platform measured, and the
    # fix is either re-subsetting the fonts or changing science-bearing copy.
    # Both are Mide's, and neither is something a build should decide.
    def _font_coverage():
        try:
            from fontTools.ttLib import TTFont
        except ImportError:
            return None, None
        covered, faces = {}, sorted(glob.glob("shared/fonts/*.woff2"))
        for path in faces:
            f = TTFont(path, fontNumber=0, lazy=True)
            cps = set()
            for tbl in f["cmap"].tables:
                cps |= set(tbl.cmap.keys())
            f.close()
            covered[os.path.basename(path)] = cps
        return covered, faces

    # Every meaning-bearing non-ASCII codepoint C2 uses, measured over the six
    # frozen pages (PAYLOAD-MAP §0 F3), plus the typographic set every unit
    # relies on. Name each, so a failure says what broke rather than a number.
    SCIENCE_CHARS = [
        (0x2212, "U+2212 MINUS — c2-06's arithmetic, five times"),
        (0x00B0, "U+00B0 DEGREE — `0 °C` in c2-02's rung 2"),
        (0x00E3, "U+00E3 a-tilde — `São Paulo` in c2-04's big question"),
        (0x00B7, "U+00B7 MIDDLE DOT — every eyebrow and rung title"),
        (0x2014, "U+2014 EM DASH — prose punctuation throughout"),
        (0x201C, "U+201C LEFT DOUBLE QUOTE — every misconception quote"),
        (0x201D, "U+201D RIGHT DOUBLE QUOTE — every misconception quote"),
        (0x2026, "U+2026 ELLIPSIS — every self-rung placeholder"),
        (0x203A, "U+203A SINGLE ANGLE — every breadcrumb separator"),
    ]
    # The gaps. Five subscripts, absent from all three KS3 faces; and ³, which
    # is present in the display and mono faces and absent from the BODY face —
    # the one `cm³` actually lands on, because `.ks3-sim-units` is
    # `font: inherit`. Grouped with the subscripts because the fix and the
    # decision are the same one.
    SUBSCRIPTS = [(0x2081, "₁"), (0x2082, "₂"), (0x2083, "₃"),
                  (0x2084, "₄"), (0x2086, "₆"), (0x00B3, "³")]

    covered, faces = _font_coverage()
    if covered is None:
        manual("font subset covers the characters that carry science",
               "fontTools is not installed on this machine; run "
               "`pip install fonttools` to turn this into a real gate.")
    else:
        # Only the faces KS3 actually loads. Fraunces and Plus Jakarta are
        # KS4's, and asserting against them would fail on somebody else's
        # stylesheet.
        ks3_faces = [n for n in covered
                     if n.startswith(("bricolage", "instrument", "dm-mono"))]
        gaps = ["%s absent from %s" % (why, face)
                for cp, why in SCIENCE_CHARS
                for face in ks3_faces if cp not in covered[face]]
        check("font subset covers the non-ASCII that carries science",
              not gaps,
              "%d codepoints × %d KS3 faces"
              % (len(SCIENCE_CHARS), len(ks3_faces)) if not gaps
              else "; ".join(gaps[:4]))

        dead = [ch for cp, ch in SUBSCRIPTS
                if any(cp not in covered[f] for f in ks3_faces)]
        if dead:
            manual("%s are not in every shipped KS3 woff2 subset"
                   % "".join(dead),
                   "NOTES-C2 flag 13, and it understates it — five subscripts, "
                   "not one, plus ³ (absent from the BODY face, which is the "
                   "one `cm³` lands on because `.ks3-sim-units` is "
                   "`font: inherit`). They are Design's own bytes on approved "
                   "pages (c2-04 CaCO₃, c2-05 throughout, c2-06's unit "
                   "picker), so MRB-205 says the page wins and nothing is "
                   "ASCII-folded here. Measured in headless Chrome: they "
                   "render through system fallback rather than as tofu, at a "
                   "matching advance in the mono face. Mide's call — re-subset "
                   "the three KS3 faces to include U+2080–208E and U+00B3, or "
                   "accept the fallback.")

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

    # MRB-210 §2 — range controls bound on both events.
    rng_problems, rng_rows = PARITY.check_range_binding(".")
    check("MRB-210 · every range control is bound on `input` AND `change`",
          not rng_problems,
          "; ".join("%s: %s" % (l, d) for l, d, _ in rng_rows)
          if not rng_problems else rng_problems[0][:140])

    # MRB-209 §4 — prose and endmatter links were never gated.
    link_problems, link_count = PARITY.check_internal_links(KS3_OUT)
    check("MRB-209 · every internal cross-lesson link resolves",
          not link_problems,
          "%d internal /ks3/ links checked" % link_count
          if not link_problems
          else "%d dead: %s" % (len(link_problems), link_problems[0][:120]))

    # ── MRB-208, one level down: a rail stop pointing at nothing ────────
    #
    # The rail was gated on the things a reader thinks to check — that both
    # variants exist, that the threshold flips at 1340, that nothing ticks on
    # load — and not on the one that makes it work at all: that each stop's
    # `anchor` names an element that is really on the page.
    #
    # It did not, on any lesson in the key stage. `BLOCK_RENDERERS["hook"]` and
    # `["quiz"]` were `lambda l, b: r_hook(l)` and `lambda l, b: r_ladder(l)`,
    # which threw the block away and with it the anchor, so `#s-hook` and
    # `#s-ladder` were emitted nowhere. Every lesson's rail therefore had a dead
    # FIRST stop and a dead LAST stop: the links went nowhere, and
    # `doneByDom(null)` is false forever, so a six-stop lesson could reach four
    # and no student could complete a rail.
    #
    # Neither the six-lesson inventory nor any ticket carried this. Two
    # independent audits found it on the same afternoon by asking the question
    # this gate now asks on every build.
    anchor_problems, anchor_count = PARITY.check_rail_anchors(KS3_OUT)
    check("MRB-208 · every rail stop's anchor exists on its page",
          not anchor_problems,
          "%d rail stops checked across the key stage" % anchor_count
          if not anchor_problems
          else "%d dead: %s" % (len(anchor_problems), anchor_problems[0][:160]))

    # ⊕ MRB-228 ruling R2 — `done_when` becomes load-bearing HERE, in the gate,
    # and deliberately not in the runtime. The check above proves a rail stop's
    # anchor names a real element; this one proves that element can finish.
    # Together they are what stops a rail stop being decorative.
    reach_problems, reach_count = PARITY.check_rail_reachable(KS3_OUT)
    check("MRB-208 · every rail stop can actually reach done (R2)",
          not reach_problems,
          "%d rail stops carry a done_when and a completion signal"
          % reach_count
          if not reach_problems
          else "%d unreachable: %s" % (len(reach_problems),
                                       reach_problems[0][:200]))

    # ⊕ MRB-249 — the two checks above are both about the stops we EMITTED, and
    # neither can see a stop we never emitted. That is how 33 pages shipped a
    # three-stop rail where Design drew four: dropping the stop is what made
    # the reachability check pass. This one asserts the built rail against
    # `docs/ks3/rail-manifest.md`, which is generated from Design's own pages,
    # so the build cannot satisfy it by removing content.
    drawn_problems, drawn_count = PARITY.check_rail_matches_design(KS3_OUT, ".")
    check("MRB-249 · the built rail is the rail Design drew",
          not drawn_problems,
          "%d rails match the drawn rail, stop for stop" % drawn_count
          if not drawn_problems
          else "%d differ: %s" % (len(drawn_problems), drawn_problems[0][:220]))

    # ── ⊕ MRB-244: a `confronted_by` pointing at another page ───────────
    #
    # The same question as the two gates above, asked of the misconception
    # register's own join. `confronted_by` names WHERE a wrong idea is taken
    # apart, and Law 3's existing check (in the per-lesson done-list) only asks
    # whether AT LEAST ONE misconception on a lesson names a real activity. A
    # lesson can therefore satisfy Law 3 on its first entry and carry two more
    # that point at nothing, which is exactly what happened.
    #
    # B6 surfaced the shape of it: b6-02's first cut named a LESSON SLUG,
    # because that page's big question IS b6-01's belief and the honest thing
    # felt like pointing at b6-01. But a cross-page pointer is one no page can
    # resolve — the student is on THIS page, and the claim "this belief is
    # confronted here" has to be true HERE. It reads as working precisely
    # because nothing checked it.
    #
    # Two more failed once the question was asked of all thirty values:
    #   b2-02 BODY-06  -> "ladder"           the page declares `s-ladder`
    #   c2-01 ATOM-02  -> "stretch-boundary" authored on the block's `id` key,
    #                                        which names an ACTIVITY, not a
    #                                        section — see `_id_attr`
    # Both named a real place in the author's head and no element in the
    # document. Neither is a typo; both are the register drifting away from the
    # page while every gate stayed green.
    #
    # Resolution is measured against the BUILT PAGE rather than the record, so
    # the gate cannot be satisfied by a key that renders to nothing: a value
    # counts only if it is emitted as `id="…"` (a section anchor, via
    # `_id_attr`) or `data-activity="…"` (an activity, via `r_activity`). That
    # is the whole universe of names a student's browser can reach.
    # ── ⊕ MRB-248: `elicited_by` carries the IDENTICAL defect ───────────
    #
    # MRB-244 asked the question of `confronted_by` and stopped there. The
    # other half of the same join was never checked, and it drifts the same
    # way for the same reason: an author writes down the place where the
    # student commits to the belief, describing the page from memory rather
    # than reading it, and nothing anywhere disagrees.
    #
    # A parallel session found it on ALL EIGHT `PLANT` entries at once —
    # every one of B7's `elicited_by` values named something the built page
    # does not emit. Eight out of eight is not a slip; it is a field that has
    # never been read by anything. `confronted_by` was fixed in isolation
    # because the ticket said `confronted_by`, and the sibling key sitting on
    # the same dict line went past three separate audits untouched.
    #
    # ⚠️ ONE RULE DIFFERS, DELIBERATELY: absence is LEGAL for `elicited_by`
    # and is NOT legal for `confronted_by`. Law 3 requires a wrong idea to be
    # taken apart somewhere the student is standing, so a missing
    # `confronted_by` is itself the failure. Eliciting is a different claim:
    # the register documents pages where a belief is stated in static markup
    # with no gate in front of it and nothing asks the student to commit —
    # `CELL-13`'s row carries "—" in the Elicited-by column and the note
    # under it calls that honest rather than an omission. Recording the gap
    # is the right answer there, and a gate that forced a value would be a
    # gate that forced an author to invent one. So: absent or empty passes;
    # a value that is PRESENT must resolve, against the same universe of
    # names — `id="…"` and `data-activity="…"` on the built page.
    #
    # Both counts are reported separately so a future reader can see that
    # both keys were measured and how many of each.
    conf_problems, conf_count = [], 0
    elic_problems, elic_count = [], 0
    _ID_RE = re.compile(r'\bid="([^"]+)"')
    _ACT_RE = re.compile(r'\bdata-activity="([^"]+)"')
    for _u in ks3_data.build_units():
        for _l in _u.get("lessons") or []:
            _mis = _l.get("misconceptions") or []
            if not _mis:
                continue
            _p = os.path.join(KS3_OUT, _u["discipline"], _u["slug"],
                              _l["slug"] + ".html")
            if not os.path.exists(_p):
                continue
            _html = open(_p, encoding="utf-8").read()
            _names = set(_ID_RE.findall(_html)) | set(_ACT_RE.findall(_html))
            for _m in _mis:
                conf_count += 1
                _v = _m.get("confronted_by")
                if not _v:
                    conf_problems.append(
                        "%s/%s: %s declares no confronted_by"
                        % (_u["code"], _l["slug"], _m.get("id")))
                elif _v not in _names:
                    conf_problems.append(
                        "%s/%s: %s confronted_by %r names no element on its "
                        "own page" % (_u["code"], _l["slug"], _m.get("id"), _v))
                # ⊕ MRB-248 — absence is legal here, a present value is not
                # exempt from having to be true.
                _e = _m.get("elicited_by")
                if not _e:
                    continue
                elic_count += 1
                if _e not in _names:
                    elic_problems.append(
                        "%s/%s: %s elicited_by %r names no element on its "
                        "own page" % (_u["code"], _l["slug"], _m.get("id"), _e))
    check("⊕ MRB-244 · every `confronted_by` names a place on its OWN page",
          not conf_problems,
          "%d misconception(s) across the key stage, every one confronted on "
          "the page that declares it" % conf_count if not conf_problems
          else "%d unresolvable: %s" % (len(conf_problems),
                                        "; ".join(conf_problems[:3])))
    check("⊕ MRB-248 · every `elicited_by` present names a place on its OWN "
          "page",
          not elic_problems,
          "%d of %d misconception(s) declare an `elicited_by`, every one "
          "elicited on the page that declares it; %d declare none, which is "
          "legal" % (elic_count, conf_count, conf_count - elic_count)
          if not elic_problems
          else "%d unresolvable of %d declared (%d declare none, which is "
               "legal): %s" % (len(elic_problems), elic_count,
                               conf_count - elic_count,
                               "; ".join(elic_problems[:3])))

    # ── MRB-203, one level down: an activity KIND with no renderer ──────
    #
    # MRB-203's registry asks whether a BLOCK TYPE has a registered component.
    # It cannot see the hole one level below it: `r_activity` dispatches on
    # `activities[].kind`, and a kind it does not know falls through to the
    # generic shell — prompt, options, reveal — which renders, validates, and
    # passes every gate while being the wrong component.
    #
    # That is not hypothetical. It is exactly what Mide rejected on 11 August:
    # B1-06's task is "name the level for each of these eight and say what
    # settled it" and it rendered as a four-option multiple choice with eight
    # items in the prompt. MRB-205's words: "CLASSIFY has no reference screen,
    # so there was no sorting component to render into, and the content was
    # forced into the nearest shape that existed."
    #
    # So: every authored kind must have a dedicated branch in `r_activity`, or
    # the build says which ones do not and how much of the page they are. It
    # reports rather than fails, because failing would delete the six pages
    # Mide is comparing — but it is loud, it names each kind and the lessons it
    # costs, and it cannot be satisfied by the silence that produced the
    # original defect.
    import build_ks3 as _B
    # The map is a module-level constant so this gate reads the real dispatch
    # table rather than a copy that drifts. `getattr` only so that the gate
    # degrades to "nothing is dispatched" instead of crashing if the constant
    # is ever renamed — a gate that dies is a gate that gets deleted.
    # ⊕ MRB-228 — read the DRAWING table, not the shell table.
    #
    # This gate used to ask whether a kind appeared in
    # `ACTIVITY_KIND_RENDERERS`, which registers a modifier class and the
    # marker attribute ks3.js dispatches on — the SHELL. It does not draw
    # anything. C1's thirteen instruments were all registered there and none of
    # them was drawn, and this gate reported "none unrendered" while every C1
    # page rendered Python dict reprs into its option buttons.
    #
    # `ACTIVITY_KIND_FN` maps a kind to the function that draws it, and
    # build_ks3 now refuses to import if the two tables disagree. Reading the
    # union is deliberate belt-and-braces: if the shell table ever regains an
    # entry the drawing table lacks, this gate must not be the thing that
    # excuses it.
    dispatched = (set(getattr(_B, "ACTIVITY_KIND_FN", {}))
                  | set(getattr(_B, "_KIND_FN_BY_BLOCK_TYPE", set())))
    generic = set(getattr(_B, "GENERIC_ACTIVITY_KINDS", set()))
    authored = {}
    for u in _B.ks3_data.build_units():
        for l in u.get("lessons", []):
            for a in l.get("activities", []):
                k = a.get("kind")
                if k and k not in dispatched and k not in generic:
                    authored.setdefault(k, set()).add(l["slug"])
    unrendered = sorted(authored)
    check("MRB-203 (kinds) · every instrument kind has its own renderer",
          not unrendered,
          "%d instrument kinds dispatched, %d declared generic, none "
          "unrendered" % (len(dispatched), len(generic))
          if not unrendered else
          "%d instrument kind(s) fall through to the GENERIC prompt/options/"
          "reveal shell — the page renders and every other gate passes, but it "
          "is NOT Design's component: %s"
          % (len(unrendered),
             "; ".join("%s (%s)" % (k, ", ".join(sorted(authored[k])))
                       for k in unrendered)))

    # ── MRB-177 · distractor length parity ──────────────────────────────
    #
    # ⊕ MRB-228, 16 Aug 2026. The last open MRB-177 item, and the one that
    # could fail silently: PAYLOAD-MAP §7.5 recorded it as "Design's sets look
    # balanced on inspection but this was not measured. **Open.**" Inspection is
    # not measurement, and there were 21 lessons to inspect.
    #
    # The property: if the correct option is reliably the longest one, a student
    # can score without knowing any science. They do learn this — it is one of
    # the first things a class works out about multiple choice — and every
    # question it works on is a question that measured nothing.
    #
    # The heuristic is `audit_content.py`'s `length_tell()`, which has been
    # auditing KS4 since before KS3 existed. Porting rather than reinventing is
    # deliberate: the same defect should have the same definition in both key
    # stages, or a question that fails at KS4 passes at KS3 for no reason a
    # student could name. Flag when the correct option is STRICTLY the longest
    # AND clears the longest distractor by ≥4 words or by ≥1.4×. Two thresholds
    # because a 2-vs-6-word gap is a tell at a ratio 4 words would miss, and a
    # 20-vs-28 is a tell at a gap the ratio would miss.
    #
    # Sets of fewer than three options are skipped, as at KS4: with two options
    # the longer one is longer half the time by construction.
    def length_tell(texts, correct):
        if correct is None or len(texts) < 3 or not (0 <= correct < len(texts)):
            return None
        wc = [len(re.findall(r"[^\s]+", str(t))) for t in texts]
        others = [w for i, w in enumerate(wc) if i != correct]
        top = max(others)
        if wc[correct] == max(wc) and wc[correct] > top and (
                wc[correct] - top >= 4 or wc[correct] >= 1.4 * top):
            return (wc[correct], top)
        return None

    # Every option set in KS3, wherever it is authored. The ladder's four rungs
    # and the activities are different shapes and both are marked, so both are
    # measured. An option may be a plain string or a dict carrying `text` —
    # `keyed-commit` and `verdict-cards` use the dict form — and the reply
    # attached to a dict option is NOT part of what the student reads before
    # choosing, so only `text` is counted.
    def _opt_text(o):
        return o.get("text", "") if isinstance(o, dict) else o

    # ── the register of tells: EMPTY, and it stays that way ──────────────
    #
    # ⊕ MRB-177 RULED 17 Aug 2026 (Mide). All twenty entries are gone because
    # all twenty rungs are FIXED, not because the gate was relaxed. The
    # threshold below is untouched and no correct answer was shortened.
    #
    # ── THE SHAPE, kept as the standing finding ──────────────────────────
    #
    # This register grew nine → twelve → twenty across five units, and the
    # twenty were authored by people who never spoke to each other. That is
    # not twenty slips; it is one construct, measured twenty times:
    #
    #     on a KS3 recall or apply rung the correct answer states a RULE
    #     (subject, condition, consequence) while each distractor states a
    #     short wrong REASON — one clause. A rule needs three parts and a
    #     wrong reason needs one, so the correct answer is longer BY
    #     CONSTRUCTION and `length_tell()` measures the construction.
    #
    # The ruling fixes the CONSTRUCT rather than the threshold: distractors on
    # a rule-stating rung now state WRONG RULES — the same three-part shape,
    # with the misconception as the consequence. Length parity then follows
    # from how the question is built instead of being imposed on top of it.
    # On the two "which of these is X?" rungs the correct answer names an
    # EVENT rather than a rule, so its distractors name events; same
    # principle, different shape.
    #
    # ⚠️ READ THIS BEFORE ADDING A TWENTY-FIRST ENTRY. If a new tell appears,
    # it is almost certainly this construct again and NOT a one-off. Rewrite
    # the distractors as wrong rules. Adding a line here is what turned a
    # finding into a nine-month exemption the first time, and the register is
    # deliberately left empty so that reaching for it feels like the
    # regression it would be.
    #
    # A stale entry still fails below, so this set cannot quietly refill.
    KNOWN_TELLS = set()

    tells, known_seen = [], set()
    for u in _B.ks3_data.build_units():
        for l in u.get("lessons", []):
            sets = []
            for rung, r in (l.get("ladder") or {}).items():
                if isinstance(r, dict) and r.get("options"):
                    sets.append(("ladder %s" % rung, r["options"],
                                 r.get("answer")))
            for a in l.get("activities", []):
                if a.get("options"):
                    sets.append(("activity %s" % a.get("id"), a["options"],
                                 a.get("answer")))
                # A `verdict-cards` item carries its own options and its own
                # answer, and the answer is a STRING matched against them
                # rather than an index — c2-04's are counts ("Three") and
                # c2-03's are sentences. Resolve it to an index or skip.
                for it in a.get("items") or []:
                    opts = it.get("options") or a.get("options")
                    if not opts:
                        continue
                    ans = it.get("answer")
                    if isinstance(ans, str):
                        texts = [_opt_text(o) for o in opts]
                        ans = texts.index(ans) if ans in texts else None
                    sets.append(("card %s" % (it.get("id") or a.get("id")),
                                 opts, ans))
            for where, opts, ans in sets:
                t = length_tell([_opt_text(o) for o in opts], ans)
                if not t:
                    continue
                if (l["slug"], where) in KNOWN_TELLS:
                    known_seen.add((l["slug"], where))
                    continue
                tells.append("%s · %s: correct is %dw against a longest "
                             "distractor of %dw" % (l["slug"], where,
                                                    t[0], t[1]))

    # A register entry that no longer describes a real tell is worse than
    # useless: it is a live exemption for a question nobody is looking at any
    # more. Fixing one is deleting its line, and forgetting to delete it fails
    # here rather than quietly widening the gate.
    stale = sorted(KNOWN_TELLS - known_seen)
    check("MRB-177 · no option set gives its answer away by length",
          not tells and not stale,
          "measured every ladder rung and every activity option set in the "
          "key stage — no length tell anywhere, and %d registered "
          "exemptions: MRB-177 was ruled on 17 Aug 2026 and all twenty were "
          "fixed at the distractor" % len(KNOWN_TELLS)
          if not tells and not stale else
          "; ".join(
              (["%d option set(s) where the correct answer is a length tell — "
                "a student can score these without reading them: %s"
                % (len(tells), "; ".join(tells))] if tells else [])
              + (["%d register entr(ies) no longer describe a real tell and "
                  "must be deleted: %s"
                  % (len(stale), ", ".join("%s · %s" % s for s in stale))]
                 if stale else [])))

    # §8.10 — the platform does not explain itself on the page.
    #
    # §8.10 is deliberately a discernment test and NOT a banned-phrase list,
    # and architecture.md is explicit that a blanket rule here would repeat the
    # failure it was written to stop. So this gate does not try to judge tone.
    # It catches one mechanical tell that is never legitimate in student prose:
    # a §-numbered reference to this project's own architecture document. A
    # twelve-year-old has no §7.4. The discernment stays with the author; only
    # the unarguable case is automated.
    #
    # Found live: the `references[].why` field renders into the "Connects to"
    # card, and C1's read "P11 owns it (§7.4); this lesson points at it and must
    # render gracefully before P11 exists" on the published draft.
    sec_problems, sec_pages = PARITY.check_no_section_refs(KS3_OUT)
    check("§8.10 · no architecture §-reference reaches student prose",
          not sec_problems,
          "%d pages' visible text scanned" % sec_pages
          if not sec_problems
          else "%d page(s): %s" % (len(sec_problems), sec_problems[0][:150]))

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
        style_problems, style_rows, contrast_rows, hidden_audit, dark_audit = \
            PARITY.run_browser_layers(KS3_OUT, ks3_browser)
        css_fails = [r for r in style_rows if not r[4]]

        # ⊕ MRB-242 — an element the generator wrote `hidden` on must load
        # hidden. Its own check, not folded into `style_problems`: that list
        # means "a registered component stopped being rendered", and a staged
        # step that is showing when it should not be is the opposite problem.
        #
        # ⊕ GATE C — this now asks the CASCADE, not the painted page. A chassis
        # that draws on load writes an inline `display:none`, which masks any
        # author rule beneath it; the audit drops the inline value for the
        # length of one read so a stylesheet that un-hides the element cannot
        # hide behind JS having already run.
        hidden_problems, n_hidden = hidden_audit
        check("⊕ MRB-242 · every element shipped `hidden` loads hidden "
              "(asked of the cascade, not of the painted page)",
              not hidden_problems,
              "%d hidden element(s) across the key stage, all display:none "
              "with their inline styles lifted" % n_hidden
              if not hidden_problems
              else "%d of %d un-hidden by the stylesheet — an author `display` "
                   "is beating the UA [hidden] rule: %s"
                   % (len(hidden_problems), n_hidden,
                      "; ".join(hidden_problems[:3])))

        # ⊕ GATE A — `.ks3-dark p` is (0,1,1) and a bare instrument class is
        # (0,1,0), so on an ink-dark block the component's own colour loses
        # silently and the text ships present, correct and invisible. It has
        # happened ten times. Every previous fix scoped one instance; this
        # asks the browser which colour rule actually WON, on every element on
        # every ink-dark ground, and fails when a generic on-dark type rule
        # beat a `.ks3-*` rule the element carries.
        dark_problems, n_dark = dark_audit
        check("⊕ GATE A · no component's own colour loses to a generic "
              "`.ks3-dark <type>` rule",
              not dark_problems,
              "%d element(s) on ink-dark grounds resolved against the full "
              "cascade" % n_dark if not dark_problems
              else "%d of %d painted by a generic on-dark rule that beat the "
                   "component's own colour: %s"
                   % (len(dark_problems), n_dark,
                      "; ".join(dark_problems[:3])))

        # ⊕ MRB-228 — `style_problems` was ASSIGNED AND NEVER READ, and that is
        # the whole of this defect.
        #
        # `run_browser_layers` already does the right thing: a registered
        # component whose selector matches nothing on its page appends a
        # "selector not present" problem and `continue`s. But `continue` means
        # it appends no ROW, and this check was driven off `style_rows` alone —
        # so a component that vanished contributed zero failures, zero rows,
        # and the gate went green. It then printed "N assertions across
        # len(COMPONENTS) components", claiming coverage of all 144 while
        # measuring fewer.
        #
        # That is the exact failure MRB-203 exists to prevent, one level down:
        # the registry gate catches a component that was never registered, and
        # nothing caught a registered component that stopped being rendered.
        # A gate that cannot tell "measured and correct" from "not measured at
        # all" is not measuring.
        #
        # It matters most on a REBUILD. C1's six pages carry a third of the
        # registry between them, so replacing them silently drops any component
        # whose block the new pages do not use — and the build would have said
        # nothing. A component that no page renders any more is a real event:
        # either it moves to a page that does render it, or it is PARKED with a
        # reason (the mechanism already exists, and prints, and is honest).
        check("C · every registered component is still ON its page",
              not style_problems,
              "%d component(s) registered but not rendered: %s"
              % (len(style_problems),
                 "; ".join(p.split(" — ")[0].replace("PARITY: ", "")
                           for p in style_problems[:4]))
              if style_problems
              else "all %d components resolved on their reference page"
                   % len(PARITY.COMPONENTS))

        # ⊕ MRB-228 — say how many assertions DID NOT RUN, in the headline.
        #
        # A component whose selector is not on its page is skipped: the runner
        # records the problem and `continue`s WITHOUT appending a style row. So
        # `css_fails` stays 0 and this line used to print
        # "543 assertions across 196 components" whether all 196 resolved or
        # forty of them had vanished. The build did go red — on the check above
        # — but the coverage headline went on claiming full coverage at an
        # unchanged count, which is the number a person reads to decide whether
        # the gate is watching. A gate that reports coverage it does not have is
        # the same failure as one that reports none.
        skipped = len(style_problems)
        check("C · resolved computed style matches Design, ±%gpx on lengths"
              % PARITY.TOL_PX,
              not css_fails,
              ("%d assertions across %d components"
               % (len(style_rows), len(PARITY.COMPONENTS))
               + ("" if not skipped else
                  " — ⚠️ %d component(s) NOT MEASURED (see the check above); "
                  "this count covers the rest" % skipped))
              if not css_fails
              else "%d of %d assertions failed%s"
                   % (len(css_fails), len(style_rows),
                      "" if not skipped
                      else ", and %d component(s) were not measured at all"
                           % skipped))
        cfails = [r for r in contrast_rows if not r[5]]
        # "worst" must mean the worst pair that had to CLEAR its bar. Letting a
        # WCAG-exempt row own that number reports the gate as weaker than it is
        # and buries the exemption in a headline nobody reads twice.
        # A PARKED pair was never measured, so it has no ratio. It must not
        # own the headline and it must not crash the comparison — same
        # reasoning as the exemption below, one step further: a pair that did
        # not run is not a pair that passed.
        parked = [r for r in contrast_rows if r[3] is None]
        measured = [r for r in contrast_rows if r[3] is not None]
        held = [r for r in measured if "[exempt:" not in r[0]]
        exempt = [r for r in measured if "[exempt:" in r[0]]
        worst = min((r[3] for r in held), default=0)
        detail = "%d pairs measured, worst %.2f:1" % (len(measured), worst)
        if parked:
            detail += " (+%d parked: %s)" % (
                len(parked),
                ", ".join(r[0].split(" [")[0] for r in parked[:3]))
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
            if ratio is None:          # PARKED — never measured, so no number
                print("       %-4s %-46s %8s  (needs %.1f)"
                      % ("----", name[:46], "parked", need or 0))
                continue
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
