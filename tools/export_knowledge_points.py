#!/usr/bin/env python3
"""export_knowledge_points.py — check, report and load the knowledge-point tags.

    python3 tools/export_knowledge_points.py --check      # the gate (knowledge_points_check)
    python3 tools/export_knowledge_points.py --coverage   # the coverage report
    python3 tools/export_knowledge_points.py --load test  # upsert into TEST, then verify
    python3 tools/export_knowledge_points.py --verify test
    python3 tools/export_knowledge_points.py --backend [DIR]        # write DIR/knowledge-points.json
    python3 tools/export_knowledge_points.py --check-backend [DIR]  # the gate (knowledge_points_mirror)

The data is `knowledge_points/ks3.json`, `ks4.json` and `untagged.json`,
drafted by `tools/kp_classify.py` (see `knowledge_points/README.md`).

── --backend / --check-backend (13 Oct 2026) ─────────────────────────

Production will not get the `knowledge_points` tables (42k rows cannot be
loaded there), so the backend reads the tags from a FILE it ships with:
`knowledge-points.json` in the backend repo root, read by
`consumer/knowledge-index.js`. `--backend` writes it from ks3.json + ks4.json;
`--check-backend` rebuilds it in memory and compares byte for byte, exit 1 on
drift (the `knowledge_points_mirror` gate — the same pattern as
`export_curriculum_tree.py --check`). DIR defaults to `MRB_BACKEND_DIR`, then
the sibling backend checkout, exactly as export_curriculum_tree finds it.
Shape (one entry per line, so a re-draft diffs as lines):

    {"v": 1,
     "points": {"<kp id>": {"label", "key_stage", "scope"}, …},
     "questions": {"<question id>": ["<kp id>", "<answer key>" | null], …}}

── --check ─────────────────────────────────────────────────────────────

Reads every question the site can show a pupil, through the LOADERS (never a
grep), and proves the JSON accounts for each one exactly once:

  * KS3 bank rows, KS3 ladder rungs `<slug>#<rung>`, their exam twins
    `ks3-<unit>-<slug>-<rung>` (which must carry their rung's point);
  * KS4 bank rows, every classic quiz card `ks4q:<subtopic>:<h>`, every
    rebuilt lesson's rungs `ks4:<slug>#r1..r4`;
  * every round-2/3/4 id (kp_classify.extras_inventory, round3_inventory,
    round4_inventory — round 4 is the lesson-authored practice-set items);
  * KS4 exam rows (`bv2-…` named by shared/exam-content, `cs-…` the code seed).

Each must be tagged with a point of ITS OWN scope, or listed in
`untagged.json` with a reason. No point id may dangle, ids are
`<ks>.<scope>.<n>` numbered from 1, and `ks4_quiz_id` must still produce the
contract's test vector — the backend computes the same id from the same text,
and a drift on either side would silently untag every classic card.

── --load ──────────────────────────────────────────────────────────────

TEST only, this round. The service key is read from the backend .env and the
load refuses unless the key's own JWT `ref` claim is the TEST project
(the guard pattern from export_ks4_questions.py). Production has no
`knowledge_points` tables — migration 20261011124719 is not applied there —
so `--load prod` refuses.
"""

import argparse
import collections
import json
import os
import re
import ssl
import statistics
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kp_classify as kpc  # noqa: E402

REPO = kpc.REPO
KP_DIR = kpc.KP_DIR

SOURCE_LABEL = {  # the coverage report's rows
    "ks3_bank": "KS3 bank", "ks4_bank": "KS4 bank", "ks3_ladder": "KS3 ladder",
    "exam_ks3": "exam KS3", "exam_ks4": "exam KS4", "ks4_quiz": "KS4 classic quiz",
    "ks3_start": "KS3 start here", "ks3_predict": "KS3 prediction", "ks3_keyed": "KS3 keyed commit",
    "ks3_yourturn": "KS3 your turn", "ks3_instrument": "KS3 instrument",
    "ks4_match": "KS4 classic matching",
    "ks4_pilot_start": "KS4 pilot start", "ks4_pilot_choice": "KS4 pilot choice",
    "ks4_pilot_sort": "KS4 pilot sort", "ks4_pilot_cfifa": "KS4 pilot cfifa",
    "ks4_pilot_steps": "KS4 pilot steps", "ks4_pilot_ladder": "KS4 pilot ladder",
    "ks4_pilot_practice": "KS4 pilot practice", "ks4_pilot_chain": "KS4 pilot chain",
    "ks4_pilot_write": "KS4 pilot write", "ks4_quizbank": "KS4 practice set (ruled text)",
    "ks4_lessonbank": "KS4 practice set (lesson-authored)",
}
REPORT_ORDER = ["ks3_bank", "ks4_bank", "ks3_ladder", "exam_ks3", "exam_ks4", "ks4_quiz",
                "ks3_start", "ks3_predict", "ks3_keyed", "ks3_yourturn", "ks3_instrument", "ks4_match",
                "ks4_pilot_start", "ks4_pilot_choice", "ks4_pilot_sort", "ks4_pilot_cfifa",
                "ks4_pilot_steps", "ks4_pilot_ladder", "ks4_pilot_practice", "ks4_pilot_chain",
                "ks4_pilot_write", "ks4_quizbank", "ks4_lessonbank"]
CS_ID = re.compile(r"^cs-(bio|chem|phys)-[a-z0-9-]+$")


def load_data():
    out = {}
    for name in ("ks3", "ks4", "untagged"):
        with open(os.path.join(KP_DIR, name + ".json"), encoding="utf-8") as fh:
            out[name] = json.load(fh)
    return out


def report_source(qid, exp=None):
    if exp and qid in exp:
        return exp[qid][0]
    s = kpc.source_of(qid)
    if s == "exam":
        return "exam_ks3" if qid.startswith("ks3-") else "exam_ks4"
    return s


def expected(inv, extras=None):
    """question id → (report source, key stage, scope ref) for every question
    the loaders know about. KS4 exam ids are not knowable offline; they are
    validated by shape instead (see check()). Round 1's route-less KS4 ladder
    ids (`ks4:<slug>#rN`) are retired and expected NOWHERE."""
    exp = {}
    for ks in ("KS3", "KS4"):
        for ref, sc in inv[ks].items():
            for q in sc["questions"]:
                if q[1] != "ks4_rung":
                    exp[q[0]] = (q[1], ks, ref)
    for exam_id, _rung, slug in inv["exam_ks3"]:
        exp[exam_id] = ("exam_ks3", "KS3", slug)
    if extras is None:
        extras = {}
        for inv_ in (kpc.extras_inventory(), kpc.round3_inventory(), kpc.round4_inventory()):
            for k_, v_ in inv_.items():
                extras.setdefault(k_, []).extend(v_)
    for (ks, ref), items in extras.items():
        for q in items:
            exp[q[0]] = (q[1], ks, ref)
    return exp


class _QText(HTMLParser):
    """textContent of every `.q-text` element (tags stripped, entities
    unescaped, nothing inserted between child nodes — as the DOM does)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.cur, self.depth, self.out = None, 0, []

    def handle_starttag(self, tag, attrs):
        if self.cur is not None:
            if tag not in ("br", "img", "wbr", "input", "hr", "meta", "link"):
                self.depth += 1
            return
        if "q-text" in (dict(attrs).get("class") or "").split():
            self.cur, self.depth = [], 1

    def handle_endtag(self, tag):
        if self.cur is None:
            return
        self.depth -= 1
        if self.depth == 0:
            self.out.append("".join(self.cur))
            self.cur = None

    def handle_data(self, d):
        if self.cur is not None:
            self.cur.append(d)


def page_quiz_ids():
    """(pages read, {ks4q id}) from the generated classic pages under
    combined/ and triple/, when they are present. The page text is the
    backend's input, so every id here must be one the JSON tags."""
    ids, pages = set(), 0
    for top in ("combined", "triple"):
        for dp, _dn, fn in os.walk(os.path.join(REPO, top)):
            for f in fn:
                if not f.endswith(".html"):
                    continue
                p = _QText()
                with open(os.path.join(dp, f), encoding="utf-8") as fh:
                    p.feed(fh.read())
                if p.out:
                    pages += 1
                for t in p.out:
                    ids.add(kpc.ks4_quiz_id(f[:-5], t))
    return pages, ids


def sender_reads_full_errors():
    """fix 2 (display-only option labels). A shortened option label still SENDS
    its stored text, carried on `data-full` (KS3 ladder, KS4 classic quiz) or
    on the option's `full` (KS4 lesson, via shared/ks4-lib.js item()). The
    answer keys above are compared against that stored text, so this asserts,
    for every kind of page that carries a stripped option, that the sender
    really reads the attribute -- otherwise the key and the send would drift
    apart silently."""
    errs = []

    def read(rel):
        with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
            return fh.read()

    def any_page(top, needle):
        for dp, _dn, fn in os.walk(os.path.join(REPO, top)):
            for f in fn:
                if f.endswith(".html"):
                    with open(os.path.join(dp, f), encoding="utf-8") as fh:
                        if needle in fh.read():
                            return True
        return False

    v2, ks3, lib = read("shared/mrbadmus.v2.js"), read("shared/ks3.js"), read("shared/ks4-lib.js")
    if any_page("ks3", ' data-full="'):
        if not re.search(r"function answerParts\(i, btn\) \{[^}]*?data-full", ks3, re.S):
            errs.append("KS3 pages carry data-full but ks3.js answerParts does not send it")
        if ks3.count('getAttribute("data-full")') < 2:
            errs.append("KS3 pages carry data-full but ks3.js saved-work restore does not read it")
        if not re.search(r"var optLabel = function \(b\) \{[^;]*data-full", v2):
            errs.append("KS3 pages carry data-full but mrbadmus.v2.js optLabel does not read it")
    for top in ("combined", "triple"):
        if any_page(top, 'class="quiz-opt"') and any_page(top, ' data-full="'):
            if not re.search(r"function sentOpt\(b\) \{[^}]*data-full", v2) or "answer: sentOpt(btn)" not in v2 \
                    or "correct_answer: opts[right] ? sentOpt(opts[right])" not in v2:
                errs.append("KS4 classic pages carry data-full but mrbadmus.v2.js does not send it")
            break
    if "full: o[0]" in lib or "full: o.full" in lib:
        if not ("full: o[0]" in lib and "full: o.full" in lib):
            errs.append("shared/ks4-lib.js item() sets `full` on only one of its two maps")
        if not re.search(r"function optText\(o\) \{[^}]*o\.full", v2) or "opts[i].full != null" not in v2:
            errs.append("KS4 lesson options carry `full` but mrbadmus.v2.js optText/idxOf do not read it")
    else:
        errs.append("shared/ks4-lib.js item() no longer carries the stored text as `full`")
    return errs


def check(data=None, inv=None, quiet=False):
    data = data or load_data()
    inv = inv or kpc.inventory()
    errs = []

    got = kpc.ks4_quiz_id(*kpc.TEST_VECTOR_ARGS)
    if got != kpc.TEST_VECTOR_ID:
        errs.append("ks4_quiz_id test vector: got %s, the contract says %s" % (got, kpc.TEST_VECTOR_ID))

    exp = expected(inv)
    bv2 = kpc.bv2_subtopic_of()
    where = {}                   # question id → (ks, scope)
    kp_scope = {}                # kp id → (ks, scope)
    for name, ks, prefix in (("ks3", "KS3", "ks3"), ("ks4", "KS4", "ks4")):
        for key, e in data[name].items():
            if e.get("scope_ref") != key or e.get("key_stage") != ks:
                errs.append("%s.json[%s]: scope_ref/key_stage disagree with the key" % (name, key))
            if key not in inv[ks]:
                errs.append("%s.json[%s]: not a %s %s" % (name, key, ks, "lesson" if ks == "KS3" else "subtopic"))
            pts = e.get("points") or []
            if not 3 <= len(pts) <= 12:
                errs.append("%s.json[%s]: %d points (3-12)" % (name, key, len(pts)))
            for i, p in enumerate(pts, 1):
                want = "%s.%s.%d" % (prefix, key, i)
                if p.get("id") != want:
                    errs.append("%s.json[%s]: point %d id %r, want %r" % (name, key, i, p.get("id"), want))
                lab = p.get("label")
                if not isinstance(lab, str) or not 3 <= len(lab) <= 120:
                    errs.append("%s: label must be 3-120 characters" % want)
                kp_scope[want] = (ks, key)
            used = set()
            for qid, kp in (e.get("questions") or {}).items():
                if kp_scope.get(kp) != (ks, key):
                    errs.append("%s → %s: not a point of %s %s (dangling or cross-scope)" % (qid, kp, ks, key))
                used.add(kp)
                if qid in where:
                    errs.append("%s is tagged twice (%s and %s)" % (qid, where[qid], (ks, key)))
                where[qid] = (ks, key)
                if qid in exp:
                    _src, eks, eref = exp[qid]
                    if (eks, eref) != (ks, key):
                        errs.append("%s belongs to %s %s, tagged in %s %s" % (qid, eks, eref, ks, key))
                elif qid in bv2:
                    if ks != "KS4":
                        errs.append("%s is a KS4 exam row tagged in %s" % (qid, ks))
                elif kpc.source_of(qid) == "ks4_rung":
                    errs.append("%s: a retired route-less KS4 ladder id (the page sends "
                                "ks4:<slug>:<route>#rN now)" % qid)
                elif not (ks == "KS4" and CS_ID.match(qid)):
                    errs.append("%s: no loader knows this question id" % qid)
            for p in pts:
                if p.get("id") not in used:
                    errs.append("%s has no questions" % p.get("id"))

    unt = data["untagged"].get("questions") or {}
    for qid, info in unt.items():
        if qid in where:
            errs.append("%s is both tagged and listed as untagged" % qid)
        if not (isinstance(info, dict) and info.get("reason")):
            errs.append("untagged %s has no reason" % qid)
        if qid not in exp and qid not in bv2 and not CS_ID.match(qid):
            errs.append("untagged %s: no loader knows this question id" % qid)

    missing = [q for q in exp if q not in where and q not in unt]
    if missing:
        errs.append("%d question(s) neither tagged nor listed untagged, e.g. %s"
                    % (len(missing), ", ".join(sorted(missing)[:8])))
    missing_bv2 = [q for q in bv2 if q not in where and q not in unt]
    if missing_bv2:
        errs.append("bonding_v2 exam row(s) neither tagged nor untagged: %s" % ", ".join(sorted(missing_bv2)))

    for exam_id, rung_id, _slug in inv["exam_ks3"]:
        if exam_id in where and rung_id in where:
            a = data["ks3"][where[exam_id][1]]["questions"][exam_id]
            b = data["ks3"][where[rung_id][1]]["questions"][rung_id]
            if a != b:
                errs.append("%s is tagged %s but its rung %s is %s" % (exam_id, a, rung_id, b))

    # answer keys: each must be the question's one right option exactly as
    # the page renders it — recomputed from the sources and compared
    want_keys = {q: v for q, v in kpc.answer_keys().items() if v[0] is not None}
    have_keys = {}
    for name in ("ks3", "ks4"):
        for key, e in data[name].items():
            for q, k in (e.get("keys") or {}).items():
                if q not in (e.get("questions") or {}):
                    errs.append("%s has an answer key but is not a question of %s" % (q, key))
                have_keys[q] = k
    for q, k in have_keys.items():
        w = want_keys.get(q)
        if w is None:
            errs.append("%s: answer key %r, but the sources name no single right option" % (q, k))
        elif k != w[0]:
            errs.append("%s: answer key %r, the sources say %r" % (q, k, w[0]))
        elif k not in w[1]:
            errs.append("%s: answer key %r is not one of its rendered options" % (q, k))
    for q in want_keys:
        if q not in have_keys and q in where:
            errs.append("%s: has a single right option (%r) but no answer key" % (q, want_keys[q][0]))

    errs.extend(sender_reads_full_errors())

    pages, pids = page_quiz_ids()
    stray = sorted(pids - set(exp))
    if stray:
        errs.append("%d classic quiz card(s) on the generated pages have no inventory id, e.g. %s"
                    % (len(stray), ", ".join(stray[:5])))

    if not quiet:
        tagged = len(where)
        print("knowledge_points_check: %d scope(s), %d point(s), %d question(s) tagged, %d untagged, "
              "%d answer key(s); %d classic page(s) read, %d card id(s) all known; test vector %s"
              % (len(data["ks3"]) + len(data["ks4"]), len(kp_scope), tagged, len(unt), len(have_keys),
                 pages, len(pids), got))
        for e in errs[:60]:
            print("  ✗ " + e)
        if len(errs) > 60:
            print("  … and %d more" % (len(errs) - 60))
        print("  %s" % ("PASS" if not errs else "FAIL (%d problem(s))" % len(errs)))
    return errs


# ── coverage ────────────────────────────────────────────────────────────

def coverage():
    data = load_data()
    inv = kpc.inventory()
    exp = expected(inv)
    tagged = {}
    for name in ("ks3", "ks4"):
        for e in data[name].values():
            tagged.update(e["questions"])
    unt = data["untagged"]["questions"]
    # KS4 exam ids are only known through the JSON (tagged + untagged).
    ids_by_src = collections.defaultdict(set)
    for q, (src, _ks, _ref) in exp.items():
        ids_by_src[src].add(q)
    for q in list(tagged) + list(unt):
        if report_source(q) == "exam_ks4":
            ids_by_src["exam_ks4"].add(q)

    lines = ["Knowledge-point coverage (knowledge_points/*.json)", ""]
    lines.append("%-18s %9s %9s %9s" % ("source", "questions", "tagged", "untagged"))
    tot = [0, 0, 0]
    for src in REPORT_ORDER:
        ids = ids_by_src[src]
        t = sum(1 for q in ids if q in tagged)
        u = len(ids) - t
        tot = [tot[0] + len(ids), tot[1] + t, tot[2] + u]
        lines.append("%-18s %9d %9d %9d" % (SOURCE_LABEL[src], len(ids), t, u))
    lines.append("%-18s %9d %9d %9d" % ("TOTAL", *tot))

    count_all = collections.Counter(tagged.values())
    bank_only = collections.Counter(kp for q, kp in tagged.items()
                                    if report_source(q) in ("ks3_bank", "ks4_bank"))
    pts = [p["id"] for name in ("ks3", "ks4") for e in data[name].values() for p in e["points"]]
    by_ks = collections.Counter(p.split(".")[0].upper() for p in pts)
    lines += ["", "knowledge points: %d (KS3 %d, KS4 %d)" % (len(pts), by_ks["KS3"], by_ks["KS4"])]
    lines.append("points with < 3 questions, all sources: %d" % sum(1 for p in pts if count_all[p] < 3))
    lines.append("points with < 3 questions, bank only:   %d" % sum(1 for p in pts if bank_only[p] < 3))
    lines.append("points with 0 bank questions:           %d" % sum(1 for p in pts if bank_only[p] == 0))
    vals = sorted(count_all[p] for p in pts)
    if vals:
        lines.append("questions per point (all sources): min %d, median %g, mean %.1f, max %d"
                     % (vals[0], statistics.median(vals), statistics.mean(vals), vals[-1]))
    buckets = [(1, 2), (3, 5), (6, 10), (11, 20), (21, 40), (41, 10 ** 9)]
    lines.append("distribution: " + ", ".join(
        "%s: %d" % ("%d-%d" % (a, b) if b < 10 ** 9 else "%d+" % a, sum(1 for v in vals if a <= v <= b))
        for a, b in buckets))
    per_scope = [len(e["points"]) for name in ("ks3", "ks4") for e in data[name].values()]
    if per_scope:
        lines.append("points per scope: min %d, median %g, max %d"
                     % (min(per_scope), statistics.median(per_scope), max(per_scope)))
    fs = data["untagged"]["failed_scopes"]
    lines.append("scopes that failed: %d%s" % (len(fs), (" — " + ", ".join(fs)) if fs else ""))
    added = [(p["id"], p["label"], p["added"]) for name in ("ks3", "ks4") for e in data[name].values()
             for p in e["points"] if p.get("added")]
    lines.append("points added after round 1 (no existing point fitted): %d (%s)" % (
        len(added), ", ".join("%s %d" % (r, n) for r, n in sorted(collections.Counter(a[2] for a in added).items()))))
    for pid, lab, rnd in added:
        lines.append("  + [%s] %s  %s  (%d question(s))" % (rnd, pid, lab, count_all[pid]))
    reasons = collections.Counter(v["reason"] for v in unt.values())
    if reasons:
        lines.append("untagged reasons: " + "; ".join("%s ×%d" % kv for kv in reasons.most_common()))
    ak = kpc.answer_keys()
    kc, nk, why = collections.Counter(), collections.Counter(), collections.Counter()
    jkeys = {q: k for name in ("ks3", "ks4") for e in data[name].values() for q, k in (e.get("keys") or {}).items()}
    for q, (k, _o, w) in ak.items():
        src = report_source(q, exp)
        if q in jkeys:
            kc[src] += 1
        else:
            nk[src] += 1
            why["%s: %s" % (SOURCE_LABEL.get(src, src), w)] += 1
    lines += ["", "answer keys (lesson-page questions with options): %d keyed, %d without a single right option"
              % (sum(kc.values()), sum(nk.values()))]
    for src in REPORT_ORDER:
        if kc[src] or nk[src]:
            lines.append("  %-30s keyed %5d   no key %4d" % (SOURCE_LABEL[src], kc[src], nk[src]))
    lines.append("  why no key:")
    for w, n in why.most_common():
        lines.append("    %4d  %s" % (n, w))
    pages, pids = page_quiz_ids()
    lines.append("classic quiz cards on the generated pages: %d unique on %d page(s), %d tagged"
                 % (len(pids), pages, sum(1 for q in pids if q in tagged)))
    lines.append("ks4QuizId test vector: %s" % kpc.ks4_quiz_id(*kpc.TEST_VECTOR_ARGS))
    lines += [""] + bank_coverage(data, exp, tagged, unt)
    text = "\n".join(lines)
    print(text)
    return text


# The two banks Set work and the family practice sets serve from, by name,
# with the knowledge points that bank can barely test. A bank is the repo's
# Python source of that table (ks3_data/question_bank.py → ks3_assignment_bank,
# ks4_data → ks4_assignment_bank), read through kpc.inventory().
BANKS = (("ks3_assignment_bank", "ks3_bank", "ks3"), ("ks4_assignment_bank", "ks4_bank", "ks4"))


def bank_coverage(data, exp, tagged, unt):
    lines = ["Per bank (the Python sources of the two assignment banks), and every other source together", ""]
    count = collections.Counter()           # (source group, kp) → questions
    for q, kp in tagged.items():
        src = report_source(q, exp)
        count[(src if src in ("ks3_bank", "ks4_bank") else "other", kp)] += 1
    every = collections.Counter(tagged.values())
    for table, src, name in BANKS:
        ids = [q for q, v in exp.items() if v[0] == src]
        t = sum(1 for q in ids if q in tagged)
        pts = [p["id"] for e in data[name].values() for p in e["points"]]
        scopes = {e["scope_ref"] for e in data[name].values()
                  if any(report_source(q, exp) == src for q in e["questions"])}
        in_scope = [p for e in data[name].values() if e["scope_ref"] in scopes for p in [x["id"] for x in e["points"]]]
        thin = sorted((p for p in in_scope if count[(src, p)] < 3), key=lambda p: (count[(src, p)], p))
        lines.append("%s (%s): %d question(s), %d tagged, %d untagged (%d listed in untagged.json)"
                     % (table, src, len(ids), t, len(ids) - t, sum(1 for q in ids if q in unt)))
        lines.append("  %d %s scope(s) with bank rows, %d knowledge point(s) in them (of %d %s points)"
                     % (len(scopes), name.upper(), len(in_scope), len(pts), name.upper()))
        lines.append("  knowledge points with fewer than 3 %s questions: %d (0: %d, 1: %d, 2: %d)"
                     % (table, len(thin), *(sum(1 for p in thin if count[(src, p)] == n) for n in (0, 1, 2))))
        for p in thin:
            lines.append("    %d  %s" % (count[(src, p)], p))
    other = [q for q, v in exp.items() if v[0] not in ("ks3_bank", "ks4_bank")]
    other += [q for q in list(tagged) + list(unt) if report_source(q) == "exam_ks4" and q not in exp]
    t = sum(1 for q in other if q in tagged)
    pts = [p["id"] for name in ("ks3", "ks4") for e in data[name].values() for p in e["points"]]
    thin = sorted((p for p in pts if count[("other", p)] < 3), key=lambda p: (count[("other", p)], p))
    lines.append("every other source (ladder, exam, lesson pages): %d question(s), %d tagged, %d untagged"
                 % (len(other), t, len(other) - t))
    lines.append("  knowledge points with fewer than 3 questions from these sources: %d (0: %d, 1: %d, 2: %d)"
                 % (len(thin), *(sum(1 for p in thin if count[("other", p)] == n) for n in (0, 1, 2))))
    thin_all = sorted((p for p in pts if every[p] < 3), key=lambda p: (every[p], p))
    lines.append("all sources together: knowledge points with fewer than 3 questions: %d" % len(thin_all))
    for p in thin_all:
        lines.append("    %d  %s" % (every[p], p))
    return lines


# ── the backend's copy (13 Oct 2026) ───────────────────────────────────

BACKEND_NAME = "knowledge-points.json"


def build_backend_index(data=None):
    data = data or load_data()
    points, questions = {}, {}
    for name, ks in (("ks3", "KS3"), ("ks4", "KS4")):
        for ref, e in data[name].items():
            for p in e["points"]:
                points[p["id"]] = {"label": p["label"], "key_stage": ks, "scope": ref}
            keys = e.get("keys") or {}
            for qid, kp in e["questions"].items():
                if qid in questions:
                    raise SystemExit("export_knowledge_points: %s is tagged twice" % qid)
                questions[qid] = [kp, keys.get(qid)]
    return {"v": 1, "points": points, "questions": questions}


def serialise_backend(index):
    """One entry per line, keys sorted: deterministic, and a re-drafted scope
    diffs as the lines that moved rather than one 2.5 MB line."""
    dump = lambda v: json.dumps(v, ensure_ascii=False, separators=(",", ":"))
    out = ['{"v":%d,' % index["v"], '"points":{']
    out.append(",\n".join("%s:%s" % (dump(k), dump(index["points"][k])) for k in sorted(index["points"])))
    out.append('},\n"questions":{')
    out.append(",\n".join("%s:%s" % (dump(k), dump(index["questions"][k])) for k in sorted(index["questions"])))
    out.append("}}")
    return "\n".join(out) + "\n"


def backend_dir(arg):
    if arg:
        return arg
    import export_curriculum_tree as ect
    return ect.default_out_dir()


def write_backend(arg):
    path = os.path.join(backend_dir(arg), BACKEND_NAME)
    index = build_backend_index()
    text = serialise_backend(index)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote %s — %d point(s), %d question(s), %d answer key(s), %d bytes"
          % (path, len(index["points"]), len(index["questions"]),
             sum(1 for v in index["questions"].values() if v[1] is not None), len(text.encode("utf-8"))))
    return 0


def check_backend(arg):
    path = os.path.join(backend_dir(arg), BACKEND_NAME)
    index = build_backend_index()
    text = serialise_backend(index)
    summary = "%d point(s), %d question(s)" % (len(index["points"]), len(index["questions"]))
    if not os.path.isfile(path):
        print("❌ %s does not exist — the backend has no knowledge-point mirror. "
              "Write it: python3 tools/export_knowledge_points.py --backend <backend dir>" % path)
        return 1
    with open(path, encoding="utf-8") as fh:
        have = fh.read()
    if have == text:
        print("✅ %s matches knowledge_points/*.json — %s" % (path, summary))
        return 0
    try:
        old = json.loads(have)
        moved_q = sorted(q for q in set(old.get("questions", {})) | set(index["questions"])
                         if old.get("questions", {}).get(q) != index["questions"].get(q))
        moved_p = sorted(p for p in set(old.get("points", {})) | set(index["points"])
                         if old.get("points", {}).get(p) != index["points"].get(p))
        print("❌ %s has DRIFTED from knowledge_points/*.json: %d question(s) and %d point(s) differ%s"
              % (path, len(moved_q), len(moved_p),
                 (" — e.g. " + ", ".join((moved_q + moved_p)[:6])) if moved_q or moved_p else
                 " (same content, different bytes)"))
    except ValueError:
        print("❌ %s is not valid JSON." % path)
    print("   Rebuild: python3 tools/export_knowledge_points.py --backend <backend dir>")
    return 1


# ── load (TEST only) ────────────────────────────────────────────────────

DB_SRC = {}


def rows_from(data):
    if not DB_SRC:
        for (ks, ref), items in kpc.round3_inventory().items():
            for q in items:
                DB_SRC[q[0]] = kpc.DB_SOURCE[q[1]]
    kps, qkps = [], []
    for name, ks, kind in (("ks3", "KS3", "lesson"), ("ks4", "KS4", "subtopic")):
        for ref, e in sorted(data[name].items()):
            for i, p in enumerate(e["points"], 1):
                kps.append({"id": p["id"], "key_stage": ks, "subject": e["subject"],
                            "scope_kind": kind, "scope_ref": ref, "position": i, "label": p["label"]})
            keys = e.get("keys") or {}
            for qid, kp in sorted(e["questions"].items()):
                qkps.append({"question_id": qid, "source": DB_SRC.get(qid) or kpc.DB_SOURCE[kpc.source_of(qid)],
                             "knowledge_point_id": kp, "answer_key": keys.get(qid)})
    return kps, qkps


def _req(url, key, method="GET", body=None, headers=None):
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    rq = urllib.request.Request(url, data=body, method=method)
    rq.add_header("apikey", key)
    rq.add_header("Authorization", "Bearer " + key)
    for k, v in (headers or {}).items():
        rq.add_header(k, v)
    with urllib.request.urlopen(rq, context=ctx, timeout=120) as r:
        raw = r.read()
        return r.headers, (json.loads(raw) if raw else None)


def fetch_all(base, key, table, cols, order):
    out, off, page = [], 0, 1000
    while True:
        _h, rows = _req("%s/rest/v1/%s?select=%s&order=%s&limit=%d&offset=%d"
                        % (base, table, cols, order, page, off), key)
        out.extend(rows)
        if len(rows) < page:
            return out
        off += page


def credentials(project):
    if project == "prod":
        print("⛔ --load/--verify prod: production does not have the knowledge_points tables — "
              "migration 20261011124719_b2c_parent_truth is not applied there. There is no "
              "production load path this round. Refusing.")
        sys.exit(3)
    return kpc.test_credentials()


def verify(project, data=None):
    base, key = credentials(project)
    data = data or load_data()
    kps, qkps = rows_from(data)
    db_k = fetch_all(base, key, "knowledge_points", "id,key_stage,subject,scope_kind,scope_ref,position,label", "id")
    db_q = fetch_all(base, key, "question_knowledge_points", "question_id,source,knowledge_point_id,answer_key",
                     "question_id")
    want_k = {r["id"]: r for r in kps}
    want_q = {r["question_id"]: r for r in qkps}
    have_k = {r["id"]: r for r in db_k}
    have_q = {r["question_id"]: r for r in db_q}
    bad_k = [i for i in set(want_k) | set(have_k) if want_k.get(i) != have_k.get(i)]
    bad_q = [i for i in set(want_q) | set(have_q) if want_q.get(i) != have_q.get(i)]
    print("verify TEST: knowledge_points %d in TEST / %d in JSON, %d differ; "
          "question_knowledge_points %d in TEST / %d in JSON, %d differ; answer_key set on %d in TEST / %d in JSON"
          % (len(have_k), len(want_k), len(bad_k), len(have_q), len(want_q), len(bad_q),
             sum(1 for r in db_q if r.get("answer_key") is not None),
             sum(1 for r in qkps if r.get("answer_key") is not None)))
    for i in sorted(bad_k)[:5] + sorted(bad_q)[:5]:
        print("   differs: %s" % i)
    return 0 if not bad_k and not bad_q else 1


def load(project):
    if project != "test":
        credentials(project)
    errs = check(quiet=True)
    if errs:
        print("⛔ --load: --check fails (%d problem(s)); fix the data first." % len(errs))
        return 2
    base, key = credentials(project)
    data = load_data()
    kps, qkps = rows_from(data)
    want_k = {r["id"] for r in kps}
    want_q = {r["question_id"] for r in qkps}

    # Prune by a SNAPSHOTTED id list, never a predicate: only rows this data
    # no longer names (a re-run scope with fewer points, a question untagged).
    have_q = {r["question_id"] for r in fetch_all(base, key, "question_knowledge_points", "question_id", "question_id")}
    have_k = {r["id"] for r in fetch_all(base, key, "knowledge_points", "id", "id")}
    for table, col, stale in (("question_knowledge_points", "question_id", sorted(have_q - want_q)),
                              ("knowledge_points", "id", sorted(have_k - want_k))):
        for i in range(0, len(stale), 100):
            ids = ",".join('"%s"' % s.replace('"', '\\"') for s in stale[i:i + 100])
            _req("%s/rest/v1/%s?%s=in.(%s)" % (base, table, col, urllib.parse.quote(ids, safe=",\"")),
                 key, method="DELETE", headers={"Prefer": "return=minimal"})
        if stale:
            print("pruned %d stale row(s) from %s" % (len(stale), table))

    for table, rows in (("knowledge_points", kps), ("question_knowledge_points", qkps)):
        for i in range(0, len(rows), 500):
            body = json.dumps(rows[i:i + 500], ensure_ascii=False).encode("utf-8")
            try:
                _req("%s/rest/v1/%s" % (base, table), key, method="POST", body=body,
                     headers={"Content-Type": "application/json",
                              "Prefer": "resolution=merge-duplicates,return=minimal"})
            except urllib.error.HTTPError as e:
                print("⛔ load failed on %s rows %d+: HTTP %s %s"
                      % (table, i, e.code, e.read().decode("utf-8", "replace")[:300]))
                return 1
        print("upserted %d row(s) into TEST %s" % (len(rows), table))
    return verify(project, data)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--coverage", action="store_true")
    g.add_argument("--load", choices=["test", "prod"])
    g.add_argument("--verify", choices=["test", "prod"])
    g.add_argument("--backend", nargs="?", const="", metavar="DIR",
                   help="write DIR/%s (DIR: MRB_BACKEND_DIR, else the sibling backend)" % BACKEND_NAME)
    g.add_argument("--check-backend", nargs="?", const="", metavar="DIR",
                   help="exit 1 if DIR/%s has drifted from the JSON" % BACKEND_NAME)
    a = ap.parse_args()
    if a.backend is not None:
        return write_backend(a.backend)
    if a.check_backend is not None:
        return check_backend(a.check_backend)
    if a.check:
        return 1 if check() else 0
    if a.coverage:
        coverage()
        return 0
    if a.load:
        return load(a.load)
    return verify(a.verify)


if __name__ == "__main__":
    sys.exit(main())
