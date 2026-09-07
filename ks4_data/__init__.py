"""ks4_data — the KS4 ASSIGNMENT question pool, authored in Python.

    from ks4_data import load_pool, classify
    rows = load_pool()          # every authored question, validated
    rows = load_pool("physics") # one subject

── WHAT THIS IS, AND WHAT IT IS NOT (MRB-332) ──────────────────────────

This package holds the questions a KS4 weekly assignment is composed from,
and NOTHING ELSE. It is the KS4 half of the one-pool-per-surface law that
MRB-288 ruled at KS3:

    KS4 lesson-page "Test yourself"  → `all_subtopics_*.py` `quiz`, baked
                                       into the page by generate_site_v5
    KS4 weekly assignment            → **this package** (mirrored as
                                       `ks4_assignment_bank`)

⚠️ **The lesson pages' `quiz` entries are a DIFFERENT POOL and may never be
reused here.** They are printed on the lesson page a child can open at any
time, so serving them as homework hands the child the answers in advance. A
question authored here is authored here; nothing copies one across, and
`pool_ownership.py` fails the build if a surface reaches into the pool it
does not own.

── WHY ITS OWN TABLE, RATHER THAN A `key_stage` COLUMN ON KS3'S ────────

`ks3_assignment_bank` is joined on `lesson_slug` alone and has no key-stage
column. Eight KS4 subtopic slugs are BYTE-IDENTICAL to KS3 lesson slugs —
`catalysts`, `distance-time-graphs`, `chromatography` and five more — so a
KS4 lookup against that table returns twelve KS3 questions: real science,
correct, and three years too easy, with nothing anywhere saying so. A
separate table ends the collision structurally rather than by remembering to
filter, which is the only way it stays ended.

── THE CONTENT RULE (standing, ruled by Mide) ──────────────────────────

Every question carries a `tier` and a `triple_only` flag, and the two
together decide who may be served it:

    tier='foundation', triple_only=False → BASE. Everyone sees it.
    tier='higher',     triple_only=False → higher-tier only.
    triple_only=True                     → Triple Science only.

**A Foundation Combined class must NEVER be served a higher or a
triple_only question.** A Triple Higher class gets all three sets.

The flags are NOT free text on the question — they are DERIVED from which
of the twelve (pathway, tier, subject) blocks teaches the subtopic, by
`classify()` below, and `load_pool()` refuses any authored file whose stated
flags disagree. The site's own curriculum data is the authority on who is
taught what; restating it by hand in 264 files would be a second description
that drifts, and a drifted flag is a Foundation child sitting a Higher paper
question with nothing saying so.

── THE SHAPE OF A QUESTION ─────────────────────────────────────────────

    {
      "id":            "ks4-specific-heat-capacity-s02",  # permanent, unique
      "subtopic_slug": "specific-heat-capacity",          # the KS4 scheme key
      "band":          "easier" | "standard" | "harder",
      "tier":          "foundation" | "higher",
      "triple_only":   False,
      "text":          "the stem",
      "options":       ["A", "B", "C", "D"],   # exactly four, plain strings
      "correct_index": 0..3,
      "why":           "one line on why the correct answer is correct",
    }

Twelve per subtopic — four per band — and the correct answer is spread
across A–D, which `verify_answer_positions.py` proves rather than trusts.

⚠️ `options` is a list of STRINGS and the answer is an INDEX. That is not
the shape KS3 uses (`[{text, correct, why}]`, one `why` per distractor) and
the difference is deliberate: this is the shape MRB-332 specified, and
`correct_index` is what the answer-position gate measures.
"""

import importlib
import os
import pkgutil
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

SUBJECTS = ("biology", "chemistry", "physics")
BANDS = ("easier", "standard", "harder")
PER_BAND = 4
PER_SUBTOPIC = PER_BAND * len(BANDS)   # 12

_CLASSIFY_CACHE = {}


# ── who is taught what ──────────────────────────────────────────────────

def classify():
    """subtopic slug → {subject, topic, tier, triple_only, order}.

    Derived from `generate_site_v5.PATHWAY_TOPIC_MAP` via `ks4_seed_sow`, the
    same projection the scheme-of-work seed is built from, so a question's
    audience and a teacher's scheme row can never disagree.

    The twelve blocks nest — Combined Foundation ⊆ Combined Higher ⊆ Triple
    Higher, and Combined Foundation ⊆ Triple Foundation ⊆ Triple Higher — so
    a subtopic's first appearance across that lattice names its audience
    exactly:

        in Combined Foundation          → base
        added by Combined Higher        → higher, not triple
        added by Triple Foundation      → triple, both tiers
        added only by Triple Higher     → triple AND higher

    The nesting is asserted, not assumed: if a future spec revision breaks it
    (a subtopic taught at Foundation but dropped at Higher, say) this raises
    rather than silently mis-flagging the question.
    """
    if _CLASSIFY_CACHE:
        return _CLASSIFY_CACHE

    import ks4_seed_sow as sow

    for subject in SUBJECTS:
        sets = {}
        for pathway in ("combined", "triple"):
            for tier in ("foundation", "higher"):
                sets[(pathway, tier)] = {
                    sid for _t, _tt, sid
                    in sow.subtopics_for(pathway, tier, subject)}
        CF = sets[("combined", "foundation")]
        CH = sets[("combined", "higher")]
        TF = sets[("triple", "foundation")]
        TH = sets[("triple", "higher")]

        if not (CF <= CH <= TH) or not (CF <= TF <= TH):
            raise AssertionError(
                "ks4_data.classify: the %s blocks no longer nest "
                "(CF⊆CH⊆TH and CF⊆TF⊆TH). A subtopic taught at one tier and "
                "dropped at a higher one cannot be flagged by first "
                "appearance, and this function's whole derivation rests on "
                "the nesting. Re-derive the rule before trusting a flag."
                % subject)

        # Triple Higher is the superset, so walking it in teaching order
        # visits every subtopic in the subject exactly once, in the order the
        # site itself lists them.
        order = 0
        for topic_id, _title, slug in sow.subtopics_for("triple", "higher",
                                                        subject):
            if slug in CF:
                tier, triple = "foundation", False
            elif slug in CH:
                tier, triple = "higher", False
            elif slug in TF:
                tier, triple = "foundation", True
            else:
                tier, triple = "higher", True
            if slug in _CLASSIFY_CACHE:
                raise AssertionError(
                    "ks4_data.classify: subtopic slug %r appears twice. Slugs "
                    "are this pool's join key and must be unique across all "
                    "three sciences." % slug)
            _CLASSIFY_CACHE[slug] = dict(
                subject=subject, topic=topic_id, tier=tier,
                triple_only=triple, order=order)
            order += 1

    return _CLASSIFY_CACHE


# ── loading the authored files ──────────────────────────────────────────

def _modules(subject=None):
    """Every authored question module, as (subject, topic, module)."""
    import ks4_data.questions as root
    for subj in SUBJECTS:
        if subject and subj != subject:
            continue
        pkg_name = "ks4_data.questions.%s" % subj
        try:
            pkg = importlib.import_module(pkg_name)
        except ModuleNotFoundError:
            continue
        for info in sorted(pkgutil.iter_modules(pkg.__path__),
                           key=lambda i: i.name):
            if info.name.startswith("_"):
                continue
            # `forces__a.py`, `forces__b.py` — a big topic is authored in
            # parts, one file per author, so that two people writing 216
            # questions between them never edit the same file. Everything
            # before the double underscore is the topic.
            #
            # ⚠️ Topic ids contain hyphens (`particle-model`) and a module
            # name cannot, so a file spells its topic with underscores and
            # this maps it back. `particle_model__a.py` → `particle-model`.
            stem = info.name.split("__")[0].replace("_", "-")
            dotted = "%s.%s" % (pkg_name, info.name)
            try:
                mod = importlib.import_module(dotted)
            except SyntaxError as exc:
                # ⚠️ A half-written file is NORMAL while the pool is being
                # authored: 264 subtopics are written by many hands at once,
                # and a reader that happens to import mid-save sees a truncated
                # list. Letting that raise would mean an author validating
                # THEIR file gets a traceback about somebody else's, which
                # reads as their own bug and costs a round trip.
                #
                # It is reported, not swallowed: `load_pool` turns it into a
                # named problem like any other, so a syntax error that is still
                # there at export time still fails the export.
                yield subj, stem, _Broken(dotted, exc)
                continue
            yield subj, stem, mod
    del root


class _Broken:
    """A module that would not import. Carries the reason to `load_pool`."""

    def __init__(self, dotted, exc):
        self.__name__ = dotted
        self.exc = exc


def load_pool(subject=None, strict=True):
    """Every authored question, validated, in a deterministic order.

    Returns rows ready for export: the authored fields plus `subject` and a
    `bank_position` — the question's index inside its own subtopic, 0..n-1.
    That position is what makes composition deterministic (the producer takes
    questions in bank order), so it is computed here, from authored order,
    rather than left to the database's row order.

    ── ⊕ MRB-335: a subtopic may now hold MORE than twelve ──────────────

    The rule used to be "exactly PER_BAND per band", and a subtopic was
    twelve questions, full stop. Set work v2 lets a teacher hand-pick up to
    twenty questions from a whole TOPIC at one tier, and the 7 Sep 2026
    availability table found twenty-two (topic, tier) cells below the
    fifty-question floor that makes picking meaningful — Combined Higher on
    `energy-changes` offered twenty-eight. So the pool grows.

    The rule is now **at least PER_BAND per band, and the first PER_BAND of
    each band sit at bank positions 0–11**, which is the invariant the
    AUTOMATIC weekly assignment depends on (RISKS D7). `composeFromBank` in
    the backend and `compose_assignment` in Python both read
    `bank_position < 12` and take every row of a band from there; if a
    thirteenth question could land inside that window, every auto-composed
    set in the estate would change the day the pool grew.

    So the emission order below is NOT simply "all easier, then all
    standard, then all harder" any more. It is:

        first four easier · first four standard · first four harder   → 0–11
        then the easier extras, the standard extras, the harder extras → 12+

    The first twelve rows of a subtopic therefore keep the ids, the order and
    the positions they had before this change, byte for byte. Set work reads
    ALL positions; auto reads only the first twelve.

    `strict=False` skips the completeness check (at least twelve per
    subtopic) so a part-authored subject can still be inspected mid-run.
    Everything else is checked either way: nothing malformed loads, ever.
    """
    cls = classify()
    rows, problems = [], []
    seen_ids = {}
    by_subtopic = {}

    for subj, topic, mod in _modules(subject):
        if isinstance(mod, _Broken):
            problems.append(
                "%s does not parse: %s (line %s). If another author is still "
                "writing it, re-run in a moment; if it is your file, fix the "
                "syntax." % (mod.__name__.replace(".", "/") + ".py",
                             mod.exc.msg, mod.exc.lineno))
            continue
        qs = getattr(mod, "QUESTIONS", None)
        if qs is None:
            problems.append("%s/%s.py has no QUESTIONS list" % (subj, topic))
            continue
        where = mod.__name__.replace(".", "/") + ".py"
        for n, q in enumerate(qs):
            problems.extend(_check(q, n, where, subj, topic, cls, seen_ids))
            by_subtopic.setdefault(q.get("subtopic_slug"), []).append(
                (where, q))

    if strict:
        for slug, meta in sorted(cls.items(), key=lambda kv: kv[1]["order"]):
            if subject and meta["subject"] != subject:
                continue
            got = by_subtopic.get(slug, [])
            if len(got) < PER_SUBTOPIC:
                problems.append(
                    "%s (%s/%s): %d question(s), expected at least %d"
                    % (slug, meta["subject"], meta["topic"], len(got),
                       PER_SUBTOPIC))
                continue
            for band in BANDS:
                n = sum(1 for _w, q in got if q.get("band") == band)
                if n < PER_BAND:
                    problems.append(
                        "%s: %d %r question(s), expected at least %d — the "
                        "first %d of every band are what the AUTOMATIC weekly "
                        "assignment composes from (bank positions 0-11), so a "
                        "band may grow but may never fall below %d."
                        % (slug, n, band, PER_BAND, PER_BAND, PER_BAND))

    if problems:
        raise SystemExit(
            "ks4_data.load_pool: %d problem(s)\n  · %s"
            % (len(problems), "\n  · ".join(problems[:60])))

    # Emit in curriculum order, then band order, then authored order — so the
    # exported file is stable across runs and diffs readably.
    #
    # ⚠️ THE FIRST FOUR OF EACH BAND COME FIRST, and that is load-bearing
    # (MRB-335 / RISKS D7). Positions 0-11 are the window the automatic
    # weekly assignment composes from, in both mirrors; a subtopic's
    # thirteenth question must land at 12 or later or every auto-composed set
    # in the estate changes silently. Taking `[:PER_BAND]` of each band first
    # and the extras afterwards keeps the original twelve at their original
    # positions, in their original order, for every subtopic authored before
    # the pool grew.
    for slug in sorted(by_subtopic, key=lambda s: cls[s]["order"]):
        meta = cls[slug]
        pos = 0
        banded = {band: [e for e in by_subtopic[slug] if e[1]["band"] == band]
                  for band in BANDS}
        emit = []
        for band in BANDS:
            emit.extend((band, e) for e in banded[band][:PER_BAND])
        for band in BANDS:
            emit.extend((band, e) for e in banded[band][PER_BAND:])
        for band, (_where, q) in emit:
            rows.append(dict(
                id=q["id"],
                subtopic_slug=slug,
                subject=meta["subject"],
                band=band,
                tier=meta["tier"],
                triple_only=meta["triple_only"],
                text=q["text"],
                options=list(q["options"]),
                correct_index=q["correct_index"],
                why=q["why"],
                bank_position=pos,
            ))
            pos += 1
    return rows


def _check(q, n, where, subj, topic, cls, seen_ids):
    """One question. Returns a list of problems, never raises."""
    out = []

    def bad(msg):
        out.append("%s[%d] (%s): %s" % (where, n, q.get("id", "no id"), msg))

    for field in ("id", "subtopic_slug", "band", "tier", "text", "options",
                  "correct_index", "why"):
        if field not in q:
            bad("missing %r" % field)
    if out:
        return out
    if "triple_only" not in q:
        bad("missing 'triple_only'")
        return out

    if not isinstance(q["id"], str) or not q["id"].startswith("ks4-"):
        bad("id must be a string starting 'ks4-'")
    if q["id"] in seen_ids:
        bad("duplicate id — already used in %s" % seen_ids[q["id"]])
    seen_ids[q["id"]] = where

    slug = q["subtopic_slug"]
    meta = cls.get(slug)
    if meta is None:
        bad("subtopic_slug %r is not in the KS4 scheme" % slug)
        return out
    if meta["subject"] != subj:
        bad("is filed under %s but %r is a %s subtopic"
            % (subj, slug, meta["subject"]))
    if meta["topic"] != topic:
        bad("is filed under topic %r but %r belongs to %r"
            % (topic, slug, meta["topic"]))

    # ⚠️ The flags are derived, never trusted. An authored file states them so
    # a reader can see the audience without a lookup; a disagreement means the
    # author's mental model and the curriculum have parted company, and the
    # question may be aimed at the wrong children.
    if q["tier"] != meta["tier"]:
        bad("says tier=%r; the curriculum says %r (%s is first taught in a "
            "%s block)" % (q["tier"], meta["tier"], slug, meta["tier"]))
    if bool(q["triple_only"]) != meta["triple_only"]:
        bad("says triple_only=%r; the curriculum says %r"
            % (bool(q["triple_only"]), meta["triple_only"]))

    if q["band"] not in BANDS:
        bad("band %r is not one of %s" % (q["band"], BANDS))

    opts = q["options"]
    if not isinstance(opts, (list, tuple)) or len(opts) != 4:
        bad("needs exactly 4 options, has %s"
            % (len(opts) if isinstance(opts, (list, tuple)) else type(opts)))
    else:
        if any(not isinstance(o, str) or not o.strip() for o in opts):
            bad("every option must be a non-empty string")
        # ⚠️ CASE-INSENSITIVE ON PURPOSE, and it has one known false
        # positive: in genetics, case is MEANING — `Rr` and `RR` are
        # different genotypes and this check calls them duplicates.
        #
        # It is left strict rather than relaxed, for two reasons. The
        # comparison can only ever over-report (it never misses a real
        # duplicate), so the failure mode is a nuisance and not a hole. And
        # the fix it forces is the better question anyway: an option reading
        # "rr — two recessive alleles" teaches where a bare "rr" only tests
        # whether the child can read a subscript. The inheritance lane hit
        # this and glossed all its genotype options, which is what a marker
        # would want regardless.
        if len({o.strip().lower() for o in opts}) != 4:
            bad("two options are the same — a four-option question with a "
                "repeat is a three-option question. (If these are genotypes "
                "differing only in case, gloss them: 'Rr — one of each "
                "allele'.)")

    ci = q["correct_index"]
    if not isinstance(ci, int) or isinstance(ci, bool) or not 0 <= ci <= 3:
        bad("correct_index must be an int 0..3, got %r" % (ci,))

    for field in ("text", "why"):
        if not isinstance(q[field], str) or not q[field].strip():
            bad("%r must be a non-empty string" % field)

    return out
