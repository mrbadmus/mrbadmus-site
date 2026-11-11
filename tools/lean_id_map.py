#!/usr/bin/env python3
"""tools/lean_id_map.py: the old-to-new question and activity ID map for the lean pilot.

Mide's rule (11 Nov 2026): keep every existing question and activity id wherever the
question survives; ship an old-to-new map; never delete or rewrite a saved answer; every new
question carries a knowledge-point tag.

    python3 tools/lean_id_map.py            write the two maps
    python3 tools/lean_id_map.py --check    exit 1 if a committed map differs from a fresh one

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

# old id -> (new id, reason). Empty on purpose: the pilot keeps every surviving id.
CHANGED = {}

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
]


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


def scopes():
    import ks3_data.lean as k3
    import ks4_lessons
    return {"KS3": sorted(k3.records()), "KS4": sorted(L["slug"] for L in ks4_lessons.lean_lessons())}


def build(base="origin/main"):
    import kp_classify as kpc
    import export_knowledge_points as ekp
    from ks3_data import lean as lean3
    inv = kpc.inventory()
    exp = ekp.expected(inv)
    old = {"KS3": _git_json(base, "knowledge_points/ks3.json"), "KS4": _git_json(base, "knowledge_points/ks4.json")}
    now = {"KS3": json.load(open(os.path.join(REPO, "knowledge_points", "ks3.json"))),
           "KS4": json.load(open(os.path.join(REPO, "knowledge_points", "ks4.json")))}
    sc = scopes()
    maps, problems = {}, []
    for ks in ("KS3", "KS4"):
        ids = {}
        for ref in sc[ks]:
            old_q = (old[ks].get(ref) or {}).get("questions") or {}
            new_q = {q for q, (_s, k, r) in exp.items() if k == ks and r == ref}
            tags_now = (now[ks].get(ref) or {}).get("questions") or {}
            for qid in sorted(set(old_q) | new_q):
                if qid in CHANGED:
                    new_id, why = CHANGED[qid]
                    ids[qid] = {"status": "changed", "new": new_id, "kp": old_q[qid], "note": why}
                elif qid in old_q and qid in new_q:
                    note = "the id is unchanged"
                    if qid.endswith("#start"):
                        note = _start_note(ks, ref, lean3)
                    ids[qid] = {"status": "kept", "new": qid, "kp": old_q[qid], "note": note}
                elif qid in old_q:
                    ids[qid] = {"status": "removed", "new": None, "kp": old_q[qid], "note": _why(qid)}
                else:
                    kp = tags_now.get(qid)
                    if not kp:
                        problems.append("%s: new id %s has no knowledge-point tag in knowledge_points/%s.json"
                                        % (ref, qid, ks.lower()))
                    ids[qid] = {"status": "added", "new": qid, "kp": kp, "note": "a new question on the lean page"}
        maps[ks] = {"scope": sc[ks], "base": base, "ids": ids}
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


def main(argv):
    if "--tag" in argv:
        print("lean_id_map: %d tag(s) written to knowledge_points/ks4.json" % apply_tags())
    maps, problems = build()
    if problems:
        print("lean_id_map: %d problem(s)" % len(problems))
        for p in problems[:20]:
            print("  - " + p)
        return 1
    bad = 0
    for ks, m in maps.items():
        path = os.path.join(OUT_DIR, FILES[ks])
        text = render(m)
        counts = {}
        for e in m["ids"].values():
            counts[e["status"]] = counts.get(e["status"], 0) + 1
        if "--check" in argv:
            cur = open(path, encoding="utf-8").read() if os.path.exists(path) else None
            if cur != text:
                print("lean_id_map: %s is stale" % FILES[ks])
                bad += 1
            continue
        os.makedirs(OUT_DIR, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("wrote %s: %d ids %s" % (os.path.relpath(path, REPO), len(m["ids"]), counts))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
