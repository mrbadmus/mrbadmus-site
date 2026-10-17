#!/usr/bin/env python3
"""Writes docs/ks4/LOOSE-ENDS-DISTRACTOR-SWEEP.md (fix 2, Oct 2026).

Every live quiz question whose options carry " — reason", the page(s) it renders
on, and before -> after for each option, from `option_labels.plan()` (the one
rule; `option_labels_check.py` proves the JS twin agrees with it).

Reads the BUILT site in mrbadmus_site/ to decide where a question renders; run it
after a build and the page list is exact.  No browser; node is used only to
evaluate the inline V()/Q() calls the Design batch pages embed.

    python3 tools/option_labels_sweep.py
"""
import collections
import glob
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import option_labels as OL  # noqa: E402
import option_labels_check as C  # noqa: E402

SITE = os.path.join(ROOT, "mrbadmus_site")
OUT = os.path.join(ROOT, "docs", "ks4", "LOOSE-ENDS-DISTRACTOR-SWEEP.md")
ROUTE_PATH = {"CF": "combined/foundation", "CH": "combined/higher",
              "TF": "triple/foundation", "TH": "triple/higher"}

NODE = r"""
const fs = require('fs'), vm = require('vm');
const files = JSON.parse(fs.readFileSync(0, 'utf8'));
const out = {};
// Walk a page's script text; wherever a V( or Q( CALL starts, find its matching
// close paren (respecting string literals) and evaluate that one call with the
// page's own helper definitions.  Multi-line lists and baseItems[...] references
// need no special case.
function calls(t, name) {
  const res = []; const re = new RegExp('(^|[^A-Za-z0-9_$.])' + name + '\\(', 'g'); let m;
  while ((m = re.exec(t))) {
    const start = m.index + m[1].length; let i = start + name.length, depth = 0, q = null;
    for (; i < t.length; i++) {
      const c = t[i];
      if (q) { if (c === '\\') i++; else if (c === q) q = null; continue; }
      if (c === "'" || c === '"' || c === '`') { q = c; continue; }
      if (c === '(') depth++; else if (c === ')') { depth--; if (depth === 0) { i++; break; } }
    }
    res.push([start, t.slice(start, i)]);
    re.lastIndex = i;
  }
  return res;
}
for (const f of files) {
  const t = fs.readFileSync(f, 'utf8');
  const helpers = t.split('\n').filter(l => /^const (V|Q) = \(/.test(l)).join('\n').replace(/^const /gm, 'var ');
  const ctx = vm.createContext({});
  try { vm.runInContext(helpers, ctx); } catch (e) { out[f] = {error: String(e)}; continue; }
  const items = [];
  for (const name of ['V', 'Q']) {
    if (!new RegExp('^const ' + name + ' = \\(', 'm').test(t)) continue;
    for (const [pos, expr] of calls(t, name)) {
      if (expr.indexOf(' \u2014 ') < 0) continue;
      try { const v = vm.runInContext('(' + expr + ')', ctx); if (v && v.opts) items.push(v); }
      catch (e) { items.push({error: String(e), line: expr.slice(0, 120)}); }
    }
  }
  out[f] = items;
}
process.stdout.write(JSON.stringify(out));
"""


def site_url(path):
    return "/" + os.path.relpath(path, SITE)


def stem_in(text, stem):
    if stem in text:
        return True
    j = json.dumps(stem, ensure_ascii=False)[1:-1]
    return j in text or j.replace("\\u2082", "₂") in text


def unesc(s):
    s = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), s)
    return s.replace("\\'", "'").replace('\\"', '"').replace("\\\\", "\\")


def fmt_opts(stem, opts, expl, indent=""):
    """before -> after lines for one question + (changed, relocated, dropped)."""
    pl = OL.plan(stem, opts, expl)
    lines = []
    reloc = drop = 0
    for i, (t, ok) in enumerate(opts):
        after = pl["labels"][i]
        mark = "[x]" if ok else "[ ]"
        if after != t:
            where = ""
            if ok:
                where = "  (reason kept in the answer note)" if i in pl["right"] and "lesson" in indent else ""
                drop += 1
            elif i in pl["feedback"]:
                where = "  (reason moved to the wrong-answer feedback)"
                reloc += 1
            else:
                where = "  (feedback already authored; reason dropped)"
            lines.append("%s- %s `%s` -> `%s`%s" % (indent, mark, t, after, where))
        else:
            lines.append("%s- %s `%s` (unchanged)" % (indent, mark, t))
    return pl, lines, reloc, drop


def main():
    qs = C.ks4_questions()
    rungs = C.ks3_rungs()
    built = os.path.isdir(SITE)

    # ---- page text cache -------------------------------------------------
    cache = {}

    def page(route, subject, topic, slug):
        p = os.path.join(SITE, ROUTE_PATH[route], subject, topic, slug + ".html")
        if not os.path.isfile(p):
            return p, None
        if p not in cache:
            cache[p] = open(p, encoding="utf-8").read()
        return p, cache[p]

    # ---- KS4 topic-bank questions ----------------------------------------
    # identity: (subject, topic, slug, stem, option texts); gather routes
    ident = collections.OrderedDict()
    for (subject, route, topic, slug, i, q) in qs:
        k = (subject, topic, slug, q["q"], tuple(t for t, _ in q["opts"]))
        ident.setdefault(k, {"q": q, "routes": []})["routes"].append(route)

    lesson_pages = set()
    ks4_rows = []        # (subject, topic, slug, q, routes, renders: {route: (url, kind)})
    unseen = 0
    for k, v in ident.items():
        subject, topic, slug, stem, _ = k
        q = v["q"]
        if not any(OL.SEP in t for t, _ in q["opts"]):
            continue
        renders = {}
        for route in v["routes"]:
            p, t = page(route, subject, topic, slug)
            if t is None:
                continue
            if "K.item(" in t or ".bank(" in t or ".find(" in t:     # lesson-batch / pilot page
                lesson_pages.add(p)
                if re.search(r"K\.bank\(", t):
                    renders[route] = (site_url(p), "lesson (whole bank)")
                else:
                    needles = [unesc(n) for n in re.findall(r"K\.find\(\s*[^,]+,\s*[^,]+,\s*'((?:\\.|[^'\\])*)'", t)]
                    hit = [n for n in needles if n in stem]
                    first = None
                    for qq in [x[5] for x in qs if x[0] == subject and x[3] == slug and x[1] == route]:
                        for n in needles:
                            if n in qq["q"]:
                                first = qq if first is None else first
                    if hit and first is not None and first["q"] == stem:
                        renders[route] = (site_url(p), "lesson (K.find)")
            else:
                if stem_in(t, stem):
                    renders[route] = (site_url(p), "topic page")
        ks4_rows.append((subject, topic, slug, q, v["routes"], renders))

    # ---- inline V()/Q() items on the batch pages -------------------------
    inline = {}
    files = sorted(lesson_pages | {os.path.join(SITE, r) for r in
                                   [os.path.relpath(f, SITE) for f in glob.glob(os.path.join(SITE, "*", "*", "*", "*", "*.html"))
                                    if os.path.relpath(f, SITE).split(os.sep)[0] in ("combined", "triple")]})
    cand = []
    for f in files:
        if f not in cache:
            try:
                cache[f] = open(f, encoding="utf-8").read()
            except OSError:
                continue
        if "const V =" in cache[f] or "const Q =" in cache[f]:
            cand.append(f)
    inline_err = 0
    if cand:
        p = subprocess.run(["node", "-e", NODE], input=json.dumps(cand), capture_output=True, text=True)
        if p.returncode == 0:
            inline = json.loads(p.stdout)
        else:
            print("node failed:", p.stderr[-300:])
    inline_rows = []     # (url, q-dict, changed)
    for f, items in sorted(inline.items()):
        if isinstance(items, dict):
            inline_err += 1
            continue
        for it in items:
            if "error" in it:
                inline_err += 1
                continue
            inline_rows.append((site_url(f), it))

    # ---- KS3 ladders -----------------------------------------------------
    ks3_paths = {}
    for f in glob.glob(os.path.join(SITE, "ks3", "*", "*", "*.html")):
        ks3_paths.setdefault(os.path.basename(f)[:-5], []).append(f)
    ks3_rows = []
    for (unit, slug, rung, r) in rungs:
        if not any(OL.SEP in o for o in r["options"]):
            continue
        urls = [site_url(f) for f in sorted(ks3_paths.get(slug, []))]
        ks3_rows.append((unit, slug, rung, r, urls))

    # ---- counts ----------------------------------------------------------
    S = collections.defaultdict(lambda: collections.Counter())
    page_set = collections.defaultdict(set)
    exceptions = []
    ex_seen = set()
    totals = collections.Counter()

    def tally(key, pl, opts, urls, kind):
        S[key]["questions with a reason"] += 1
        if pl["strip"]:
            S[key]["stripped"] += 1
            S[key]["option labels shortened"] += sum(1 for t, _ in opts if OL.SEP in t)
            for u in urls:
                page_set[key].add(u)
        else:
            S[key]["exceptions (left as authored)"] += 1

    body = []
    body.append("## 4. KS4 topic-bank questions, by subject / topic / subtopic\n")
    body.append("A question that is identical on several routes is listed once, with its routes. "
                "`topic page` = the generated page's own Test-yourself quiz; `lesson` = a Design "
                "lesson page whose practice reads this question through `KS4.item()`. "
                "A question the current build does not show on any page is marked **not rendered**.\n")
    cur = None
    for (subject, topic, slug, q, routes, renders) in sorted(ks4_rows, key=lambda r: (r[0], r[1], r[2])):
        if (subject, topic, slug) != cur:
            cur = (subject, topic, slug)
            body.append("\n### %s / %s / %s\n" % cur)
        pl = OL.plan(q["q"], q["opts"], q.get("wrong_explanations"))
        urls = sorted({u for u, _ in renders.values()})
        kinds = sorted({k for _, k in renders.values()})
        tally("KS4 %s" % subject, pl, q["opts"], urls if renders else [], "ks4")
        totals["ks4"] += 1
        if pl["reason"]:
            key = (q["q"], tuple(t for t, _ in q["opts"]))
            if key not in ex_seen:
                ex_seen.add(key)
                exceptions.append(("KS4 %s/%s/%s" % (subject, topic, slug), q["q"], q["opts"], pl["reason"], routes, urls))
        body.append("- **%s** - routes %s - %s" % (q["q"].replace("\n", " "), "/".join(routes),
                    ("renders on " + ", ".join(urls) + " (%s)" % ", ".join(kinds)) if renders else "**not rendered** on any current page"))
        _, lines, reloc, drop = fmt_opts(q["q"], q["opts"], q.get("wrong_explanations"), indent="    ")
        if not pl["strip"]:
            body.append("    - EXCEPTION `%s` - left exactly as authored" % pl["reason"])
        body.extend(lines)
        for rt, (u, k) in sorted(renders.items()):
            pass

    body.append("\n## 5. Inline questions on the Design lesson pages (V() and Q() lists)\n")
    body.append("These sit inside the lesson page itself, not in `all_subtopics_*.py`, and reach the pupil "
                "through the same `KS4.item()` doorway.\n")
    seen_inline = set()
    cur = None
    for url, it in inline_rows:
        stem = it["q"]
        opts = [(o[0], bool(o[1])) for o in it["opts"]]
        if not any(OL.SEP in t for t, _ in opts):
            continue
        expl = it.get("wrong_explanations") or {}
        pl = OL.plan(stem, opts, expl)
        ident_k = (stem, tuple(t for t, _ in opts))
        key = ("lesson inline",)
        S[key]["questions with a reason"] += 0
        tally(("KS4 lesson inline",), pl, opts, [url], "inline")
        if pl["reason"] and ident_k not in ex_seen:
            ex_seen.add(ident_k)
            exceptions.append(("inline " + url, stem, opts, pl["reason"], [], [url]))
        if url != cur:
            cur = url
            body.append("\n### %s\n" % url)
        body.append("- **%s**" % stem)
        if not pl["strip"]:
            body.append("    - EXCEPTION `%s` - left exactly as authored" % pl["reason"])
        _, lines, _, _ = fmt_opts(stem, opts, expl, indent="    ")
        body.extend(lines)

    body.append("\n## 6. KS3 mastery-ladder questions (scored rungs), by unit / lesson\n")
    cur = None
    for (unit, slug, rung, r, urls) in sorted(ks3_rows, key=lambda x: (x[0], x[1], x[2])):
        opts = [(o, k == r["answer"]) for k, o in enumerate(r["options"])]
        pl = OL.plan(r.get("q", ""), opts, r.get("feedback"))
        tally(("KS3 ladder",), pl, opts, urls, "ks3")
        if pl["reason"]:
            exceptions.append(("KS3 %s/%s/%s" % (unit, slug, rung), r.get("q", ""), opts, pl["reason"], [], urls))
        if (unit, slug) != cur:
            cur = (unit, slug)
            body.append("\n### %s / %s - %s\n" % (unit, slug, ", ".join(urls) or "no page found"))
        body.append("- **%s** (%s)" % (r.get("q", "").replace("\n", " "), rung))
        if not pl["strip"]:
            body.append("    - EXCEPTION `%s` - left exactly as authored" % pl["reason"])
        _, lines, _, _ = fmt_opts(r.get("q", ""), opts, r.get("feedback"), indent="    ")
        body.extend(lines)

    # ---- KS3 unscored activity options (NOT changed - needs a ruling) -----
    body.append("\n## 7. KS3 unscored activity options with a reason - NOT changed, needs Mide's ruling\n")
    body.append("Commit-before-you-reveal gates, predictions and instrument choices (`ks3-option` without "
                "`data-correct`). Nothing marks them; the reveal panel follows. Stripping the tail here would "
                "also strip the claim half of 'Right - reason' / 'Wrong - reason' verdict options, so this run "
                "leaves them alone and lists them.\n")
    pat = re.compile(r'<button[^>]*class="ks3-option[^"]*"([^>]*)>\s*(?:<span class="ks3-opt-mark"[^>]*>[^<]*</span>\s*)?'
                     r'<span class="ks3-opt-label">(.*?)</span>', re.S)
    n_act = n_pg = 0
    for f in sorted(glob.glob(os.path.join(SITE, "ks3", "**", "*.html"), recursive=True)):
        t = open(f, encoding="utf-8").read()
        rows = []
        for m in pat.finditer(t):
            if "data-correct" in m.group(1):
                continue
            lab = re.sub(r"<[^>]+>", "", m.group(2))
            if OL.SEP in lab:
                rows.append(lab)
        if rows:
            n_pg += 1
            n_act += len(rows)
            body.append("\n### %s (%d)\n" % (site_url(f), len(rows)))
            body.extend("- `%s`" % r for r in rows)
    body.append("\nTotal: %d unscored option labels on %d KS3 pages.\n" % (n_act, n_pg))
    SECTION7 = (n_act, n_pg)

    # ---- parked follow-up: colon tails on authored Q() items ---------------
    body.append("\n## 8. Parked follow-up (out of scope, Mide 17 Oct 2026): colon tails\n")
    body.append("Authored `Q()` items on the Design batch pages put the reason or working after a COLON "
                "instead of an em-dash (`100 mol: 2.7 kg = 2700 g, and 2700 / 27 = 100`). Same giveaway, "
                "outside the ruling, NOT changed. Questions whose correct option carries a colon tail:\n")
    allq = [f for f in cache if "const Q = (" in cache[f]]
    if allq:
        pc = subprocess.run(["node", "-e", NODE.replace("if (expr.indexOf(' \\u2014 ') < 0) continue;", "")],
                            input=json.dumps(sorted(allq)), capture_output=True, text=True)
        seen_c = set()
        n_c = 0
        if pc.returncode == 0:
            for f, its in sorted(json.loads(pc.stdout).items()):
                if isinstance(its, dict):
                    continue
                for it in its:
                    if "opts" not in it or it["q"] in seen_c:
                        continue
                    right = [o[0] for o in it["opts"] if o[1]]
                    if right and re.search(r"\S: \S", right[0]) and OL.SEP not in right[0]:
                        seen_c.add(it["q"])
                        n_c += 1
                        body.append("- %s - **%s** -> correct: `%s`" % (site_url(f), it["q"].replace("\n", " "), right[0]))
        body.append("\nTotal: %d questions.\n" % n_c)

    # ---- assemble --------------------------------------------------------
    head = []
    head.append("# Loose ends, fix 2 - the distractor sweep\n")
    head.append("Mide's ruling: a practice option must not carry its mistake or working in its label. "
                "The label is the text before the first spaced em-dash; the reason moves into the feedback. "
                "Generated by `tools/option_labels_sweep.py` from the built site and the one rule in "
                "`option_labels.py`; regenerate after any content change.\n")
    head.append("## 1. Mechanism\n")
    head.append("One display-time rule (`option_labels.plan`), applied where the options are drawn - "
                "stored data, mirrors, knowledge points and shuffle seeds are untouched, and the shuffle "
                "is still seeded from the ORIGINAL text so no option moves.\n\n"
                "| renderer | file | where the reason goes |\n|---|---|---|\n"
                "| KS4 topic-page quiz (4 emitters) | `generate_site_v5.py` | a wrong option with no authored explanation gets its reason as the wrong-answer feedback; a correct option's reason has no slot on these pages (the page says only \"Correct\") and is dropped from the label |\n"
                "| KS4 lesson pages (pilot + batches; `K.find`, `K.bank`, inline `V()`/`Q()`) | `shared/ks4-lib.js` `item()`, text written by `ks4_rulings.py` R21 from `option_labels.js_source()` | wrong option: authored explanation, else the reason; correct option: the standard line plus the reason |\n"
                "| KS3 mastery ladder | `build_ks3.py` `_rung_marked` | wrong option: authored correction, else the reason; a correct option's reason has no slot (the page says only \"Correct.\") and is dropped from the label |\n")
    head.append("A question is left EXACTLY as authored (and listed in section 3) when stripping would damage it: "
                "an empty or bare-connective head, two options collapsing to the same label, a pairing/matching "
                "stem, or a short head-plus-descriptor pair.\n")
    head.append("## 2. Summary\n")
    head.append("| corpus | questions with a reason | stripped | option labels shortened | exceptions | pages affected |\n|---|---|---|---|---|---|")
    gt = collections.Counter()
    allpages = set()
    for key in sorted(S, key=lambda k: str(k)):
        c = S[key]
        if not c["questions with a reason"]:
            continue
        name = key if isinstance(key, str) else key[0]
        np_ = len(page_set[key])
        allpages |= page_set[key]
        head.append("| %s | %d | %d | %d | %d | %d |" % (name, c["questions with a reason"], c["stripped"],
                    c["option labels shortened"], c["exceptions (left as authored)"], np_))
        for k2 in c:
            gt[k2] += c[k2]
    head.append("| **total** | %d | %d | %d | %d | %d (distinct) |" % (gt["questions with a reason"], gt["stripped"],
                gt["option labels shortened"], gt["exceptions (left as authored)"], len(allpages)))
    head.append("\nKS4 counts are per DISTINCT question (the same question on several routes counts once); "
                "page counts are distinct URLs where a stripped question actually renders in the current build"
                + ("" if built else " (**mrbadmus_site/ absent - page counts unavailable**)")
                + ". %d inline V()/Q() evaluation errors.\n" % inline_err)
    head.append("Not counted above: %d unscored KS3 activity options on %d pages (section 7) - not changed, ruling needed.\n" % SECTION7)
    head.append("## 3. Exceptions (left as authored) and proposed handling\n")
    head.append("| # | where | reason | proposed handling |\n|---|---|---|---|")
    handling = {
        OL.EX_DUPLICATE: "Leave as authored. The dash text is part of the answer (two options share a head and differ only after it), so a display strip would make the options indistinguishable. Needs a rewrite of the distractor set so the head decides, which is a content run, not a display fix.",
        OL.EX_PAIRING: "Leave as authored. The stem asks for a pair / match; the tail is the other half of the pair.",
        OL.EX_DESCRIPTOR: "Leave as authored. Head and tail are both short; the tail reads as the answer, not a reason.",
        OL.EX_CONNECTIVE: "Leave as authored. The head is only a joining word.",
        OL.EX_EMPTY: "Leave as authored. Nothing would be left of the label.",
    }
    for n, (where, stem, opts, reason, routes, urls) in enumerate(exceptions, 1):
        head.append("| %d | %s - %s | %s | %s |" % (n, where, stem.replace("|", "/")[:80], reason, handling[reason]))
    head.append("\n### Exception detail\n")
    for n, (where, stem, opts, reason, routes, urls) in enumerate(exceptions, 1):
        head.append("**%d. %s** `%s` - %s" % (n, where, reason, stem.replace("\n", " ")))
        for t, ok in opts:
            head.append("    - %s `%s`" % ("[x]" if ok else "[ ]", t))
        head.append("    - pages: %s\n" % (", ".join(urls) or "not rendered"))
    open(OUT, "w", encoding="utf-8").write("\n".join(head) + "\n\n" + "\n".join(body) + "\n")
    print("wrote", OUT, "(%d lines)" % (len(head) + len(body)))
    print("exceptions:", len(exceptions), "| inline items w/ reason:", len(inline_rows), "| pages:", len(allpages))


if __name__ == "__main__":
    main()
