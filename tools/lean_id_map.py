#!/usr/bin/env python3
"""tools/lean_id_map.py: the old-to-new question and activity ID map for the lean pilot.

Mide's rule (11 Nov 2026): keep every existing question and activity id wherever the
question survives; ship an old-to-new map; never delete or rewrite a saved answer; every new
question carries a knowledge-point tag.

    python3 tools/lean_id_map.py            write the two maps
    python3 tools/lean_id_map.py --check    exit 1 if a committed map differs from a fresh one
    python3 tools/lean_id_map.py --wave wave1            the KS3 wave's maps only, one per UNIT:
                                            docs/lessons/wave1/ID-MAP-ks3-<unit name>.json
                                            (photosynthesis, respiration) and
                                            docs/b2c/id-maps/B7.json, B8.json (add --check too)

OLD set: the ids in knowledge_points/{ks3,ks4}.json at --base (default origin/main), one scope
per lesson. NEW set: every id the lean pages can send, from tools/kp_classify's inventory
(bank rows, ladder rungs, Start here, KS4 per-route block ids). One entry per id:

    {"status": "kept" | "changed" | "added" | "removed",
     "new": the id as it is now (null if removed),
     "kp": the knowledge point it is tagged to,
     "note": why}

`kept`    the id is asked on the lean page exactly as before (its wording may differ: say so).
`removed` the page no longer asks it. The id stays in knowledge_points/*.json so a child's saved
          answer still resolves; export_knowledge_points --check accepts an id only if it is
          listed `removed` here, and still fails on any other unknown id.
`added`   a new question; its tag is in knowledge_points/ks4.json.
`changed` never produced by default: a changed id needs a reason written into CHANGED below.

Written to docs/lessons/pilot/ID-MAP-ks3-breathing-and-gas-exchange.json and
docs/lessons/pilot/ID-MAP-ks4-energy.json.

A later KS4 unit gets its own map, by unit:

    python3 tools/lean_id_map.py --unit physics-magnetism --wave wave1            write
    python3 tools/lean_id_map.py --unit physics-magnetism --wave wave1 --check    exit 1 if stale

`--unit <subject>-<topic>` covers every subtopic of that topic (all four routes). It writes
docs/lessons/<wave>/ID-MAP-ks4-<topic>.json and docs/b2c/id-maps/<subject>-<topic>.json (the file
tools/lesson_contract_check.py --unit <subject>/<topic> reads). The pilot maps are untouched.
A lesson with no lean record yet is still its classic page, so its classic matching cards (ks4c:)
are `kept`; they become `removed` when its record lands. Re-run the map after every record.
Classic ids (what the old page sent): ks4q:<slug>:<hash> quiz cards, ks4c:<slug>:match-<n>
matching pairs (shared/mrbadmus.v2.js sends nothing else from a classic KS4 page); the
assignment-bank rows ks4-<slug>-e01.. are never asked on a lesson page and stay `kept`.
"""
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "tools"))
OUT_DIR = os.path.join(REPO, "docs", "lessons", "pilot")
FILES = {"KS3": "ID-MAP-ks3-breathing-and-gas-exchange.json", "KS4": "ID-MAP-ks4-energy.json"}
# The same maps in the shape docs/b2c/LESSON-DEPENDENCIES.md asks for, read by
# tools/lesson_contract_check.py: one key per id that moved or went, null = retired.
B2C_DIR = os.path.join(REPO, "docs", "b2c", "id-maps")
B2C_FILES = {"KS3": "B4.json", "KS4": "physics-energy.json"}


def b2c_map(m):
    return {q: e["new"] for q, e in sorted(m["ids"].items())
            if e["status"] in ("removed", "changed")}


def render_b2c(m):
    return json.dumps(b2c_map(m), indent=1, sort_keys=True, ensure_ascii=False) + "\n"

# The pilot maps were written against main BEFORE the pilot's own tags landed in
# knowledge_points/ks4.json (the parent of 654ff891c). Read against today's origin/main, which
# holds those tags, every pilot "added" id would turn "kept" and --check would go red for a reason
# that is not drift. The map still labels its base "origin/main"; this is the ref it reads.
PILOT_BASE_REF = "654ff891c^"

# The pilot's KS3 scope is frozen at B4's five lessons; a wave names its own lessons, so a later
# wave never rewrites an earlier map. A wave writes KS3 only (no KS4 scope).
PILOT_KS3 = ["alveoli-built-for-exchange", "exercise-asthma-and-smoking", "how-breathing-works",
             "stomata-and-gas-exchange-in-plants", "the-gas-exchange-system"]
# wave -> [(unit code, unit name, [lesson slugs])]; a unit's maps are named by it.
WAVES = {
    "wave1": [
        ("B7", "photosynthesis", ["the-photosynthesis-reaction", "leaves-built-for-the-job",
                                  "testing-a-leaf-for-starch"]),
        ("B8", "respiration", ["aerobic-respiration", "why-every-cell-respires",
                               "anaerobic-respiration-in-humans", "fermentation", "aerobic-vs-anaerobic"]),
        ("C2", "atoms-elements-and-compounds", ["the-atom-daltons-model", "elements", "compounds",
                                                "chemical-symbols", "formulae", "conservation-of-mass"]),
    ],
}

# old id -> (new id, reason). Empty on purpose: the pilot keeps every surviving id.
CHANGED = {}

_ROUTE_DIRS = {"cf": "combined/foundation", "ch": "combined/higher", "tf": "triple/foundation", "th": "triple/higher"}


def root_covers():
    """{slug: {activity id: [the lesson values its controls are drawn from]}}, read from
    ROOT_FORMS in shared/mrbadmus.v2.js (the `covers` each entry names)."""
    src = open(os.path.join(REPO, "shared", "mrbadmus.v2.js"), encoding="utf-8").read()
    start = src.index("var ROOT_FORMS")
    end = src.index("<ks4-root-drafts>", start)
    body = src[start:end]
    keys = list(re.finditer(r"\n {8}'([a-z0-9-]+)': \[", body))
    out = {}
    for i, k in enumerate(keys):
        chunk = body[k.end():keys[i + 1].start() if i + 1 < len(keys) else len(body)]
        forms = {}
        for m in re.finditer(r"(?:\bid|\bpick): '(\w+)'(?:(?!\bid: ').)*?covers: \[([^\]]*)\]", chunk, re.S):
            forms.setdefault(m.group(1), re.findall(r"'(\w+)'", m.group(2)))
        out[k.group(1)] = forms
    return out


def drawn(slug, route):
    """The lesson values the built lean page's template draws a list of controls from."""
    import glob
    hits = glob.glob(os.path.join(REPO, "mrbadmus_site", _ROUTE_DIRS[route], "*", "*", slug + ".html"))
    if len(hits) != 1:
        raise SystemExit("lean_id_map: expected one %s page for %s, found %d" % (route, slug, len(hits)))
    return set(re.findall(r'"e": "(\w+)', open(hits[0], encoding="utf-8").read()))


def undrawn_root_activity(qid, covers):
    """For a KS4 lesson's own activity id (a ROOT_FORMS entry): the values it covers when
    none of them is drawn on the lean page any more, else None. The old logic stays bundled
    (the lean page reuses some of it), so an inventory that reads the logic still lists the
    id; only the template says whether a child can press it."""
    m = re.match(r"ks4:([^:]+):(\w\w)#([A-Za-z]\w*)", qid)
    if not m:
        return None
    slug, route, key = m.groups()
    cov = (covers.get(slug) or {}).get(key)
    if cov is None:
        return None
    if not cov:
        raise SystemExit("lean_id_map: ROOT_FORMS %s.%s names no covers; cannot tell if it is drawn" % (slug, key))
    if drawn(slug, route) & set(cov):
        return None
    return cov

# Why an id was removed, by the shape of the id.
_WHY = [
    (r"#sort-", "the sorting activity is not on the lean page"),
    (r"#choice-", "the Think again question is not on the lean page"),
    (r"#(placed|tried)$", "the resource cards activity is not on the lean page"),
    (r"#steps-", "the worked steps activity is not on the lean page"),
    (r"#cfifa-", "the worked-calculation questions are not on the lean page"),
    (r"#chain-|#write-", "this practice item is not on the lean page"),
    (r"#locate-the-fault-|#two-bags-|#gas-|#work-the-diaphragm", "the instrument was removed from the lean page"),
    (r"ks4c:", "the classic matching card is not on the lean page"),
    (r"#think-commit-", "the Think first question is not on the lean page"),
    (r"#where-it-runs-out$", "the where-the-model-runs-out activity is not on the lean page"),
]


def ks3_undrawn(ref, qid):
    """For a KS3 lean lesson: True when the built page never mentions the id's own part, so it
    cannot send it, although the lesson data still lists the item (e.g. a Think first commit the
    lean page does not draw). Conservative: any mention of the id on the page counts as drawn,
    and lesson_contract_check still checks every page's real ids against this map."""
    import glob
    if "#" not in qid:
        return False              # not a page-local id (e.g. a bank row): leave it to the rules below
    hits = glob.glob(os.path.join(REPO, "mrbadmus_site", "ks3", "*", "*", ref + ".html"))
    if len(hits) != 1:
        raise SystemExit("lean_id_map: expected one KS3 page for %s, found %d" % (ref, len(hits)))
    return qid.split("#", 1)[1] not in open(hits[0], encoding="utf-8").read()


def _why(qid):
    for pat, why in _WHY:
        if re.search(pat, qid):
            return why
    return "the question is not on the lean page"


# The tags for the questions the three rebuilt (old-format) lessons gained, as Mide's table gave
# them: suffix -> point number N, meaning point id `ks4.<slug>.N`, on all four routes.
NEW_TAGS = {
    "energy-stores-systems": {"start": 4, "r1-1": 7, "r1-2": 2, "r2-1": 4, "r2-2": 5, "r3-1": 4, "r3-2": 4, "r4-1": 4},
    "energy-changes-in-systems": {"start": 7, "r1-1": 1, "r1-2": 1, "r2-1": 3, "r2-2": 3, "r3-1": 6, "r3-2": 7, "r4-1": 6},
    "energy-transfers-in-a-system": {"start": 2, "r1-1": 1, "r1-2": 2, "r2-1": 4, "r2-2": 3, "r3-1": 2, "r3-2": 6, "r4-1": 1},
}


def apply_tags():
    """Write NEW_TAGS into knowledge_points/ks4.json (idempotent; touches only these ids)."""
    import kp_classify as kpc
    want_keys = {q: v for q, v in kpc.answer_keys().items() if v[0] is not None}
    path = os.path.join(REPO, "knowledge_points", "ks4.json")
    raw = open(path, encoding="utf-8").read()
    data = json.loads(raw)
    n = 0
    for slug, tags in NEW_TAGS.items():
        qs = data[slug]["questions"]
        pts = {p["id"] for p in data[slug]["points"]}
        for route in ("cf", "ch", "tf", "th"):
            for suffix, num in tags.items():
                kp = "ks4.%s.%d" % (slug, num)
                if kp not in pts:
                    raise SystemExit("lean_id_map: %s is not a point of %s" % (kp, slug))
                qid = "ks4:%s:%s#%s" % (slug, route, suffix)
                if qs.get(qid) != kp:
                    qs[qid] = kp
                    n += 1
                # a question with one right option also carries its answer key, as every
                # other tagged question does (the check recomputes it from the sources)
                if qid in want_keys:
                    keys = data[slug].setdefault("keys", {})
                    if keys.get(qid) != want_keys[qid][0]:
                        keys[qid] = want_keys[qid][0]
                        n += 1
        data[slug]["questions"] = dict(sorted(qs.items()))
        if "keys" in data[slug]:
            data[slug]["keys"] = dict(sorted(data[slug]["keys"].items()))
    # keep the file's own formatting: re-dump only if something changed
    if n:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(data, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
    return n


def _git_json(base, rel):
    r = subprocess.run(["git", "show", "%s:%s" % (base, rel)], cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("lean_id_map: cannot read %s at %s: %s" % (rel, base, r.stderr.strip()))
    return json.loads(r.stdout)


# The pilot maps cover the pilot's own lessons and nothing else. Later lean units (a KS3 wave's
# units, KS4 units such as Magnetism) have their own unit maps, so the pilot scope is pinned here
# rather than read from whatever lean records exist today.
def scopes(wave=None):
    import ks3_data.lean as k3
    if wave:
        if wave not in WAVES:
            raise SystemExit("lean_id_map: unknown wave %r; known: %s" % (wave, ", ".join(sorted(WAVES))))
        slugs = [x for _c, _n, ss in WAVES[wave] for x in ss]
        missing = [x for x in slugs if x not in k3.records()]
        if missing:
            raise SystemExit("lean_id_map: no lean record for %s" % ", ".join(missing))
        return {"KS3": sorted(slugs), "KS4": []}
    from ks4_lessons import batch_lean
    return {"KS3": sorted(PILOT_KS3), "KS4": sorted(batch_lean.SLUGS)}


def unit_parts(unit):
    """'physics-magnetism' -> ('physics', 'magnetism'). Subjects have no hyphen; topics may."""
    if "-" not in unit:
        raise SystemExit("lean_id_map: --unit is <subject>-<topic>, e.g. physics-magnetism")
    return tuple(unit.split("-", 1))


def unit_scopes(unit):
    """{'KS3': [], 'KS4': every subtopic slug of the unit's topic, on any route}."""
    import build_ks4 as B
    subject, topic = unit_parts(unit)
    data = B.load_subtopics_by_route()
    if subject not in data:
        raise SystemExit("lean_id_map: unknown subject %r" % subject)
    slugs = sorted({st["id"] for tree in data[subject].values() for st in tree.get(topic, [])})
    if not slugs:
        raise SystemExit("lean_id_map: no subtopics for %s/%s" % (subject, topic))
    return {"KS3": [], "KS4": slugs}


def build(base="origin/main", unit=None, ref=None, wave=None):
    """unit: a KS4 unit map. wave without unit: a KS3 wave's maps, one per unit. Neither: the pilot."""
    import kp_classify as kpc
    import export_knowledge_points as ekp
    from ks3_data import lean as lean3
    inv = kpc.inventory()
    exp = ekp.expected(inv)
    ref = ref or base
    old = {"KS3": _git_json(ref, "knowledge_points/ks3.json"), "KS4": _git_json(ref, "knowledge_points/ks4.json")}
    now = {"KS3": json.load(open(os.path.join(REPO, "knowledge_points", "ks3.json"))),
           "KS4": json.load(open(os.path.join(REPO, "knowledge_points", "ks4.json")))}
    wave = None if unit else wave
    sc = unit_scopes(unit) if unit else scopes(wave)
    import ks4_lessons
    lean_slugs = {L["slug"] for L in ks4_lessons.lean_lessons()}
    covers = root_covers()
    # Every ROOT_FORMS activity of a lean lesson must have been read with its covers, or a
    # later batch could keep an id the page can no longer send without anyone noticing.
    forms = ({} if not sc["KS4"] else
             json.loads(subprocess.run(["node", os.path.join(REPO, "tools", "kp_root_forms.js"), REPO],
                                       capture_output=True, text=True, check=True).stdout))
    for slug in sc["KS4"]:
        for f in forms.get(slug) or []:
            if f["id"] not in (covers.get(slug) or {}):
                raise SystemExit("lean_id_map: cannot read the covers of ROOT_FORMS %s.%s; teach "
                                 "root_covers() its shape before mapping this lesson" % (slug, f["id"]))
    maps, problems = {}, []
    runs = ([(code, "KS3", ss) for code, _n, ss in WAVES[wave]] if wave
            else [("KS3", "KS3", sc["KS3"]), ("KS4", "KS4", sc["KS4"])])
    for key, ks, refs in runs:
        if not refs:
            continue
        ids = {}
        for ref in refs:
            old_q = (old[ks].get(ref) or {}).get("questions") or {}
            new_q = {q for q, (_s, k, r) in exp.items() if k == ks and r == ref}
            tags_now = (now[ks].get(ref) or {}).get("questions") or {}
            for qid in sorted(set(old_q) | new_q):
                if qid in CHANGED:
                    new_id, why = CHANGED[qid]
                    ids[qid] = {"status": "changed", "new": new_id, "kp": old_q[qid], "note": why}
                elif qid in old_q and qid in new_q and ks == "KS4" and undrawn_root_activity(qid, covers):
                    ids[qid] = {"status": "removed", "new": None, "kp": old_q[qid],
                                "note": "the lesson's own activity (%s) is not drawn on the lean page"
                                        % ", ".join(undrawn_root_activity(qid, covers))}
                elif qid in old_q and qid in new_q and ks == "KS3" and ks3_undrawn(ref, qid):
                    ids[qid] = {"status": "removed", "new": None, "kp": old_q[qid], "note": _why(qid)}
                elif qid in old_q and qid in new_q and not (
                        ks == "KS4" and qid.startswith("ks4c:") and ref in lean_slugs):
                    # (a ks4c: matching card belongs to the classic page; a lean page never
                    # sends one, though the inventory still lists the lesson's old pairs. A
                    # lesson with no lean record yet is still its classic page: kept.)
                    note = "the id is unchanged"
                    if qid.endswith("#start"):
                        note = _start_note(ks, ref, lean3)
                    ids[qid] = {"status": "kept", "new": qid, "kp": old_q[qid], "note": note}
                elif qid in old_q:
                    if qid.startswith(("cs-", "bv2-")):
                        # A consumer exam-bank row in the database, never asked on a lesson
                        # page: rebuilding the page cannot remove it.
                        ids[qid] = {"status": "kept", "new": qid, "kp": old_q[qid],
                                    "note": "a B2C exam-bank row, not on any lesson page; untouched"}
                        continue
                    ids[qid] = {"status": "removed", "new": None, "kp": old_q[qid], "note": _why(qid)}
                else:
                    kp = tags_now.get(qid)
                    if not kp:
                        problems.append("%s: new id %s has no knowledge-point tag in knowledge_points/%s.json"
                                        % (ref, qid, ks.lower()))
                    ids[qid] = {"status": "added", "new": qid, "kp": kp, "note": "a new question on the lean page"}
        maps[key] = {"scope": sorted(refs), "base": base, "ids": ids}
    return maps, problems


def _start_note(ks, ref, lean3):
    """`kept`, with a note when the Start here wording differs from the page at the base."""
    if ks != "KS3":
        return "Start here, asked on the lean page"
    try:
        src = subprocess.run(["git", "show", "origin/main:ks3_data/start_here.py"], cwd=REPO,
                             capture_output=True, text=True).stdout
        ns = {"__name__": "start_here_at_base"}
        exec(compile(src, "start_here.py", "exec"), ns)          # plain data; no imports of ours
        old_q = (ns["START_HERE"].get(ref) or {}).get("question")
        new_q = lean3.records()[ref]["start"]["question"]
        if old_q is None:
            return "Start here, asked on the lean page"
        if old_q == new_q:
            return "Start here, the same question as before"
        return "Start here kept; the question wording changed (was: %s)" % old_q
    except Exception as exc:        # a note is not worth failing the map over
        return "Start here, asked on the lean page (%s)" % type(exc).__name__


def render(m):
    return json.dumps(m, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


def _arg(argv, flag):
    return argv[argv.index(flag) + 1] if flag in argv else None


def _sha(ref):
    r = subprocess.run(["git", "rev-parse", "--verify", ref + "^{commit}"], cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("lean_id_map: cannot resolve %s: %s" % (ref, r.stderr.strip()))
    return r.stdout.strip()


def _base_args(unit, wave, argv):
    """The `build()` arguments. The pilot reads PILOT_BASE_REF. A unit map records the commit SHA
    it was written against (`--base`, default origin/main) and --check reads that same commit, so
    a unit's map does not go stale when main moves on (its own tags merge into main)."""
    if wave and not unit:
        return {"wave": wave}
    if not unit:
        return {"unit": None, "ref": PILOT_BASE_REF}
    base = _arg(argv, "--base")
    if "--check" in argv and not base:
        path = os.path.join(REPO, "docs", "lessons", wave, "ID-MAP-ks4-%s.json" % unit_parts(unit)[1])
        if os.path.exists(path):
            base = json.load(open(path, encoding="utf-8")).get("base")
    return {"unit": unit, "base": _sha(base or "origin/main")}


def main(argv):
    unit, wave = _arg(argv, "--unit"), _arg(argv, "--wave")
    if unit and not wave:
        raise SystemExit("lean_id_map: --unit needs --wave (e.g. --wave wave1)")
    if "--tag" in argv and not unit:
        print("lean_id_map: %d tag(s) written to knowledge_points/ks4.json" % apply_tags())
    maps, problems = build(**_base_args(unit, wave, argv))
    if problems:
        print("lean_id_map: %d problem(s)" % len(problems))
        for p in problems[:20]:
            print("  - " + p)
        return 1
    bad = 0
    for ks, m in maps.items():
        if unit:
            out_dir = os.path.join(REPO, "docs", "lessons", wave)
            path = os.path.join(out_dir, "ID-MAP-ks4-%s.json" % unit_parts(unit)[1])
            bpath = os.path.join(B2C_DIR, "%s.json" % unit)
            import ks4_lessons
            lean_slugs = {L["slug"] for L in ks4_lessons.lean_lessons()}
            todo = [s for s in m["scope"] if s not in lean_slugs]
            if todo:
                print("lean_id_map: %s: %d of %d lessons have no lean record yet (%s); their classic "
                      "ids are `kept`. Re-run when the records land." % (unit, len(todo), len(m["scope"]), ", ".join(todo)))
        elif wave:
            out_dir = os.path.join(REPO, "docs", "lessons", wave)
            uname = {c: n for c, n, _s in WAVES[wave]}.get(ks)
            path = os.path.join(out_dir, "ID-MAP-ks3-%s.json" % uname)
            bpath = os.path.join(B2C_DIR, "%s.json" % ks)
        else:
            out_dir = OUT_DIR
            path = os.path.join(OUT_DIR, FILES[ks])
            bpath = os.path.join(B2C_DIR, B2C_FILES[ks])
        text = render(m)
        counts = {}
        for e in m["ids"].values():
            counts[e["status"]] = counts.get(e["status"], 0) + 1
        btext = render_b2c(m)
        if "--check" in argv:
            for p, t in ((path, text), (bpath, btext)):
                cur = open(p, encoding="utf-8").read() if os.path.exists(p) else None
                if cur != t:
                    print("lean_id_map: %s is stale" % os.path.relpath(p, REPO))
                    bad += 1
            continue
        os.makedirs(out_dir, exist_ok=True)
        os.makedirs(B2C_DIR, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        with open(bpath, "w", encoding="utf-8") as fh:
            fh.write(btext)
        print("wrote %s: %d ids %s; %s: %d moved or retired"
              % (os.path.relpath(path, REPO), len(m["ids"]), counts, os.path.relpath(bpath, REPO), len(b2c_map(m))))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
