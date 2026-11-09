#!/usr/bin/env python3
"""option_labels_check.py — a practice option never shows its reason.

Fast and static: no browser, no network.  The rule is `option_labels.py`
(fix 2, Oct 2026): the label a pupil sees is the text before the first spaced
em-dash; the reason moves into feedback.  Three jobs:

  1. TWINS AGREE.  The JavaScript twin that `ks4_rulings.py` R21 writes into
     `shared/ks4-lib.js` is run under node over EVERY KS4 quiz question in the
     twelve `all_subtopics_*.py` files, and its labels / replies / shuffle order
     must equal what `option_labels.plan()` says.  Shuffle order is compared
     too: the sort key is the hash of the ORIGINAL text, so the order of
     options must not move.
  2. THE RULE HOLDS.  Over the same KS4 corpus and every authored KS3 ladder
     rung: a question that is stripped shows no " — " in any label, no two
     labels coincide, no label is empty; a question that is not stripped is
     one of the named exceptions.
  3. THE BUILT PAGES.  Every scored option on a built page (`quiz-opt` on a KS4
     topic page, `ks3-option` with `data-correct` on a KS3 ladder) that still
     contains " — " must belong to a named exception question.  Skipped, by
     name, when `mrbadmus_site/` is absent.

Exit 0 = green.
"""
import glob
import html as _html
import importlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import option_labels as OL  # noqa: E402

FILES = {
    "all_subtopics_biology": ("biology", "CF"),
    "all_subtopics_biology_higher": ("biology", "CH"),
    "all_subtopics_biology_triple_foundation": ("biology", "TF"),
    "all_subtopics_biology_triple_higher": ("biology", "TH"),
    "all_subtopics_chemistry": ("chemistry", "CF"),
    "all_subtopics_chemistry_higher": ("chemistry", "CH"),
    "all_subtopics_chemistry_triple_foundation": ("chemistry", "TF"),
    "all_subtopics_chemistry_triple_higher": ("chemistry", "TH"),
    "all_subtopics_physics": ("physics", "CF"),
    "all_subtopics_physics_higher": ("physics", "CH"),
    "all_subtopics_physics_triple_foundation": ("physics", "TF"),
    "all_subtopics_physics_triple_higher": ("physics", "TH"),
}
ATTR = {"biology": "BIOLOGY_SUBTOPICS_ALL", "chemistry": "CHEMISTRY_SUBTOPICS_ALL",
        "physics": "PHYSICS_SUBTOPICS_ALL"}


def ks4_questions():
    """(subject, route, topic, slug, index, question dict)."""
    out = []
    for modname, (subject, route) in FILES.items():
        data = getattr(importlib.import_module(modname), ATTR[subject])
        for topic, lst in data.items():
            for st in lst:
                for i, q in enumerate(st.get("quiz") or []):
                    out.append((subject, route, topic, st["id"], i, q))
    return out


def ks3_rungs():
    """(unit, lesson slug, rung, rung dict) for every authored marked rung."""
    import ks3_data
    out = []
    for u in ks3_data.build_units():
        for l in u.get("lessons", []):
            if not l.get("authored"):
                continue
            for rung, r in (l.get("ladder") or {}).items():
                if isinstance(r, dict) and r.get("options") and isinstance(r.get("answer"), int):
                    out.append((u.get("code"), l["slug"], rung, r))
    return out


def ks3_plan(r):
    ans = r.get("answer")
    return OL.plan(r.get("q", ""), [(o, i == ans) for i, o in enumerate(r["options"])],
                   r.get("feedback") or {})


def js_expected(q, pl):
    """What KS4.item(q) should return, in the shuffle order, as comparable rows."""
    RIGHT = "This is the answer the mark scheme credits."
    we = q.get("wrong_explanations") or {}
    rows = []
    for i, (t, ok) in enumerate(q["opts"]):
        if ok:
            reply = RIGHT + " " + pl["right"][i] if i in pl["right"] else RIGHT
        else:
            reply = we.get(i) or we.get(str(i)) or pl["feedback"].get(i, "")
        rows.append((hash_key(q["q"], t), pl["labels"][i], bool(ok), reply))
    rows.sort(key=lambda r: r[0])
    return [list(r[1:]) for r in rows]


def hash_key(stem, text):
    h = 2166136261
    s = stem + "|" + text
    units = []
    for c in s:
        cp = ord(c)
        if cp > 0xFFFF:
            cp -= 0x10000
            units += [0xD800 + (cp >> 10), 0xDC00 + (cp & 0x3FF)]
        else:
            units.append(cp)
    for u in units:
        h ^= u
        h = (h * 16777619) & 0xFFFFFFFF
    return h


def check_twins(qs, problems):
    import build_ks4
    lib = build_ks4.build_ks4_lib_js()
    runner = ("var window = { KS4SRC: {}, addEventListener: function () {}, requestAnimationFrame: function () {}, pageYOffset: 0 };\n"
              "var localStorage = {}; var document = { documentElement: { classList: { add: function () {}, remove: function () {} } }, addEventListener: function () {} };\n" + lib +
              "\nvar qs = JSON.parse(require('fs').readFileSync(0, 'utf8'));\n"
              "var out = qs.map(function (q) { var it = window.KS4.item(q); "
              "return it.options.map(function (o) { return [o.text, o.correct, o.reply, o.full]; }); });\n"
              "process.stdout.write(JSON.stringify(out));\n")
    payload = []
    for (_s, _r, _t, _slug, _i, q) in qs:
        payload.append({"q": q["q"], "opts": [[t, bool(ok)] for t, ok in q["opts"]],
                        "wrong_explanations": {str(k): v for k, v in (q.get("wrong_explanations") or {}).items()}})
    p = subprocess.run(["node", "-e", runner], input=json.dumps(payload),
                       capture_output=True, text=True)
    if p.returncode != 0:
        problems.append("node could not run the generated ks4-lib.js: %s" % p.stderr[-400:])
        return
    got = json.loads(p.stdout)
    bad = 0
    for (subject, route, topic, slug, i, q), g in zip(qs, got):
        pl = OL.plan(q["q"], q["opts"], q.get("wrong_explanations"))
        want = js_expected(q, pl)
        # display-only: every option still carries its STORED text as `full`
        if sorted(x[3] for x in g) != sorted(t for t, _ok in q["opts"]):
            bad += 1
            problems.append("KS4 lesson option `full` != stored text on %s/%s %s q%d" % (subject, slug, route, i))
        g = [x[:3] for x in g]
        if g != want:
            bad += 1
            if bad <= 5:
                problems.append("JS twin disagrees on %s/%s %s q%d: js=%r py=%r"
                                % (subject, slug, route, i, g[:2], want[:2]))
    if bad:
        problems.append("%d of %d KS4 questions: JS and Python disagree" % (bad, len(qs)))
    return len(qs) - bad


def check_rule(qs, rungs, problems):
    exc_texts = set()
    n_strip = n_exc = 0
    corpora = [(q["q"], q["opts"], q.get("wrong_explanations"), "KS4 %s/%s %s q%d" % (s, slug, r, i))
               for (s, r, _t, slug, i, q) in qs]
    corpora += [(r.get("q", ""), [(o, k == r.get("answer")) for k, o in enumerate(r["options"])],
                 r.get("feedback"), "KS3 %s/%s/%s" % (u, slug, rung)) for (u, slug, rung, r) in rungs]
    for stem, opts, expl, where in corpora:
        pl = OL.plan(stem, opts, expl)
        if pl["strip"]:
            n_strip += 1
            labels = pl["labels"]
            if any(OL.SEP in x for x in labels):
                problems.append("%s: a stripped label still contains the dash" % where)
            if len({re.sub(r"\s+", " ", x).lower() for x in labels}) != len(labels):
                problems.append("%s: stripped labels coincide" % where)
            if any(not x for x in labels):
                problems.append("%s: an empty label" % where)
        elif pl["reason"]:
            n_exc += 1
            for t, _ok in opts:
                exc_texts.add(t)
    return n_strip, n_exc, exc_texts


_SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉"
                     "⁰¹²³⁴⁵⁶⁷⁸⁹",
                     "01234567890123456789")


def _norm(s):
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", _html.unescape(s)).translate(_SUB).strip()


def check_built(exc_texts, problems):
    site = os.path.join(ROOT, "mrbadmus_site")
    if not os.path.isdir(site):
        print("SKIPPED built-page guard: mrbadmus_site/ absent")
        return None
    allowed = {_norm(t) for t in exc_texts}
    pat4 = re.compile(r'<button class="quiz-opt"[^>]*>(.*?)</button>', re.S)
    pat3 = re.compile(r'<button[^>]*class="ks3-option"[^>]*data-correct=[^>]*>\s*'
                      r'<span class="ks3-opt-mark"[^>]*>[^<]*</span>\s*'
                      r'<span class="ks3-opt-label">(.*?)</span>', re.S)
    bad = pages = 0
    for f in glob.glob(os.path.join(site, "**", "*.html"), recursive=True):
        rel = os.path.relpath(f, site)
        if not rel.startswith(("combined", "triple", "physics", "chemistry", "biology", "ks3")):
            continue
        t = open(f, encoding="utf-8").read()
        hit = False
        for pat in (pat4, pat3):
            for m in pat.finditer(t):
                lab = _norm(m.group(1))
                if OL.SEP in lab and lab not in allowed:
                    bad += 1
                    hit = True
                    if bad <= 8:
                        problems.append("built page %s: option still carries its reason: %r"
                                        % (rel, lab[:90]))
        pages += hit
    if bad:
        problems.append("%d scored option labels on %d built pages still contain \" — \" "
                        "outside a named exception" % (bad, pages))
    return bad


def short_texts(qs, rungs):
    """Every option text a page shows shortened, normalised, and every one it shows
    whole though it has a dash. KS3's page sends the rendered text, so both forms."""
    from ks3_art.kit import sci
    short, whole = {}, set()
    for (_s, _r, _t, _slug, _i, q) in qs:
        pl = OL.plan(q["q"], q["opts"], q.get("wrong_explanations"))
        for k, (o, _ok) in enumerate(q["opts"]):
            if OL.SEP in o:
                if pl["strip"]:
                    short[_norm(o)] = _norm(pl["labels"][k])
                else:
                    whole.add(_norm(o))
    for (_u, _slug, _rung, r) in rungs:
        pl = ks3_plan(r)
        for k, o in enumerate(r["options"]):
            if OL.SEP in o:
                for form in (o, OL.sent_text(sci(o))):
                    if pl["strip"]:
                        short[_norm(form)] = _norm(pl["labels"][k])
                    else:
                        whole.add(_norm(form))
    return short, whole


def page_truth():
    """What the pages themselves show: `data-full` on a built page, and KS4's real
    `item()` over every question the rebuilt lessons serve. None when there is no build."""
    truth = {}
    site = os.path.join(ROOT, "mrbadmus_site")
    if not os.path.isdir(site):
        return None
    btn = re.compile(r'<button[^>]*data-full="([^"]*)"[^>]*>(.*?)</button>', re.S)
    mark = re.compile(r'<span class="ks3-opt-mark"[^>]*>[^<]*</span>')
    for rel in ("ks3", "combined", "triple"):
        for f in glob.glob(os.path.join(site, rel, "**", "*.html"), recursive=True):
            for m in btn.finditer(open(f, encoding="utf-8").read()):
                truth[_norm(m.group(1))] = _norm(mark.sub("", m.group(2)))
    runner = (
        "const fs=require('fs'),path=require('path');var window={KS4SRC:{},addEventListener(){},requestAnimationFrame(){},pageYOffset:0};"
        "var localStorage={};var document={documentElement:{classList:{add(){},remove(){}}},addEventListener(){}};"
        "const dir=%s;for(const f of fs.readdirSync(dir)){if(/^ks4-source.*\\.js$/.test(f))eval(fs.readFileSync(path.join(dir,f),'utf8'));}"
        "eval(fs.readFileSync(path.join(dir,'ks4-lib.js'),'utf8'));const out=[];"
        "(function w(o){if(!o||typeof o!=='object')return;if(Array.isArray(o)){o.forEach(w);return;}"
        "if(typeof o.q==='string'&&Array.isArray(o.opts)){window.KS4.item(o).options.forEach(function(x){if(x.full!=null&&x.full!==x.text)out.push([x.full,x.text]);});}"
        "else Object.values(o).forEach(w);})(window.KS4SRC);process.stdout.write(JSON.stringify(out));"
    ) % json.dumps(os.path.join(ROOT, "shared"))
    p = subprocess.run(["node", "-e", runner], capture_output=True, text=True)
    if p.returncode != 0:
        raise SystemExit("option_labels_check: could not run KS4's item(): " + p.stderr[-400:])
    for full, label in json.loads(p.stdout):
        truth[_norm(full)] = _norm(label)
    return truth


def check_panel_list(qs, rungs, problems):
    """The panel's list: exact, against the pages, and the two cases that matter."""
    short, whole = short_texts(qs, rungs)
    both = set(short) & whole
    if both:
        problems.append("%d option texts are shortened in one question and whole in another: %r" % (len(both), sorted(both)[:3]))
    path = os.path.join(ROOT, "consumer", "option-label.js")
    want = OL.consumer_js({OL.text_hash(t) for t in short})
    if "--write" in sys.argv:
        with open(path, "w", encoding="utf-8") as f:
            f.write(want)
    got = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    if got != want:
        problems.append("consumer/option-label.js is out of date: python3 option_labels_check.py --write")
    if len({OL.text_hash(t) for t in short}) != len(short):
        problems.append("two shortened option texts hash alike")
    truth = page_truth()
    if truth is None:
        print("SKIPPED panel list against the pages: mrbadmus_site/ absent")
    else:
        extra = [t for t in short if t not in truth]
        missing = [t for t in truth if t not in short]
        differ = [t for t in short if t in truth and truth[t] != short[t]]
        for name, lst in (("the list shortens but no page does", extra), ("a page shortens but the list doesn't", missing), ("label differs from the page", differ)):
            if lst:
                problems.append("panel list: %d option(s) %s, e.g. %r" % (len(lst), name, lst[:3]))
        print("panel list: %d option texts shortened, %d confirmed on the pages, %d mismatches" % (
            len(short), len(set(short) & set(truth)), len(extra) + len(missing) + len(differ)))
    cases = json.dumps([
        "No \u2014 every rock must be metamorphosed before it can become sediment",
        "Yes \u2014 weathering and erosion can act on any rock at the surface",
        "180 Pa \u2014 multiply the force by the area",
        "2000 Pa \u2014 600 N shared over 0.30 m\u00b2",
        "No dash here",
    ])
    p = subprocess.run(["node", "-e", "var window={};" + got + "process.stdout.write(JSON.stringify(%s.map(window.MrBadmusShortOption)));" % cases],
                       capture_output=True, text=True)
    res = json.loads(p.stdout) if p.returncode == 0 else p.stderr[-300:]
    exp = ["No \u2014 every rock must be metamorphosed before it can become sediment",
           "Yes \u2014 weathering and erosion can act on any rock at the surface", "180 Pa", "2000 Pa", "No dash here"]
    if res != exp:
        problems.append("panel list: the rock cycle stays whole and 180 Pa short: got %r" % (res,))


def main():
    problems = []
    qs = ks4_questions()
    rungs = ks3_rungs()
    agree = check_twins(qs, problems)
    check_panel_list(qs, rungs, problems)
    n_strip, n_exc, exc_texts = check_rule(qs, rungs, problems)
    built = check_built(exc_texts, problems)
    print("option_labels_check: %d KS4 questions, %d KS3 rungs; %d stripped, %d named exceptions; "
          "JS twin agrees on %s; built pages: %s"
          % (len(qs), len(rungs), n_strip, n_exc, agree,
             "skipped" if built is None else "%d stray" % built))
    for p in problems:
        print("FAIL:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
