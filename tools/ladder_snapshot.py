#!/usr/bin/env python3
"""Snapshot the SEMANTICS of every marked ladder rung, so a rebalance can be
proved to have moved positions and changed nothing else (MRB-278)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ks3_data

def snap():
    out = {}
    for u in ks3_data.build_units():
        for l in u.get("lessons", []):
            if not l.get("authored"):
                continue
            for rung, r in (l.get("ladder") or {}).items():
                if not (isinstance(r, dict) and r.get("options")):
                    continue
                a = r.get("answer")
                if not isinstance(a, int):
                    continue
                opts = [o.get("text", "") if isinstance(o, dict) else o
                        for o in r["options"]]
                fb = r.get("feedback") or {}
                out["%s|%s" % (l["slug"], rung)] = {
                    "unit": u.get("code"),
                    # the SET of option texts — order is what we are allowed
                    # to change, membership is not
                    "texts": sorted(opts),
                    # the text that is correct — must survive identically
                    "correct_text": opts[a],
                    # each correction paired with the DISTRACTOR it corrects,
                    # by text: a correction must never move to another option
                    "pairs": sorted((opts[i], v) for i, v in fb.items()
                                    if isinstance(i, int) and 0 <= i < len(opts)),
                    "answer": a,
                }
    return out

if __name__ == "__main__":
    json.dump(snap(), open(sys.argv[1], "w"), indent=0, sort_keys=True)
    print("snapshotted %d rungs -> %s" % (len(snap()), sys.argv[1]))
