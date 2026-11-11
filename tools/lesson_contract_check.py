#!/usr/bin/env python3
"""lesson_contract_check.py -- prove a rebuilt lesson still saves, restores
and is tagged for a family (B2C) child. Read docs/b2c/LESSON-DEPENDENCIES.md.

Compares the lesson pages in this checkout with a baseline captured from main
before the rebuild (tools/lesson_contract_baseline.json): every question id the
page can send, the page selectors the saving code reads, and which activities
save. Nothing is parsed separately: the ids come from the same code the
knowledge-point tagger and the save-coverage report use (tools/kp_classify.py,
tools/kp_ks3_units.py, tools/kp_ks4_eval.js in Node, tools/activity_save_coverage.py).

Pick the lessons:
  --unit P4                  a KS3 unit code
  --unit physics/energy      a KS4 topic (subject/topic, all routes)
  --slugs a,b,c              lesson slugs (a slug shared by KS3 and KS4 picks both)
  --pages 'ks3/physics/forces/*.html'   a path glob, from the repo root

The check FAILS (exit 1) when:
  * a page in the baseline has gone from its URL (URLs may not move);
  * a question id vanished and is not in the unit's id map
    (docs/b2c/id-maps/<unit>.json, {"old_id": "new_id" | null}, null = retired);
  * a map entry points at an id the page does not send;
  * a new id has no knowledge-point tag (run tools/kp_classify.py --top-up);
  * a selector the saving code reads has disappeared;
  * an activity that saved no longer does, or a new answerable one does not;
  * a committed answer key no longer matches the page (top-up again);
  * an id breaks the server's shape rule.
It REPORTS without failing a knowledge point left pointing at a removed id
(a top-up prunes it) and a ladder question whose options changed (the DB
mirror ks3_ladder_questions needs reloading when this ships).

--drive adds the live part, in headless Chrome, for each chosen page: the
page's controls are pressed as a family child on device A, then a fresh
browser (device B) must show the work back and POST nothing. It reuses
activity_save_drive.py's site server, in-process pretend backend and browser
helpers, so it needs no account and no database: nothing leaves 127.0.0.1
(every other host is blocked) and the configured backend must not be
production or it refuses. That drive cannot be restricted to named pages for
its own fixed cases, so this runs the closest equivalent: the drive's own
"--units" press routine on just the chosen pages and blocks. On a rebuilt KS4
page device B is compared on the shared answer blocks only; a lesson's own
activities are proven by the named cases in that drive, and a classic KS4 page
is not pressed here at all. MRB_BACKEND_DIR
(the backend checkout) is needed for the check against the server's real
validateAnswerBody; without it that one step is reported as skipped.

--write-baseline regenerates the baseline. ONLY from main, before a rebuild
starts, and NEVER to make a failing check pass: it refuses a checkout that is
ahead of origin/main or has uncommitted lesson changes.

  python3 tools/lesson_contract_check.py --unit P4
  python3 tools/lesson_contract_check.py --slugs efficiency --drive
  python3 tools/lesson_contract_check.py --unit P4 --ledger-sql

Exit 0 = safe, 1 = not safe, 2 = could not run.
"""

import argparse
import collections
import fnmatch
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import time

TOOLS = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.dirname(TOOLS)
BASELINE = os.path.join(TOOLS, "lesson_contract_baseline.json")
MAP_DIR = os.path.join("docs", "b2c", "id-maps")
# backend consumer/answers.js QUESTION_ID_SHAPE: the server refuses anything else.
QUESTION_ID_SHAPE = re.compile(r"^[a-z0-9:#._-]{1,200}$")
LESSON_DONE = "lesson-done / quiz-score signal"

# The selectors the saving and restoring code reads, one row per thing, written
# as the capture writes them. (name shown to a person, CSS test or raw test).
KS3_SELECTORS = [
    ("script /shared/config.js", ("raw", "/shared/config.js")),
    ("script /shared/mrbadmus.v2.js", ("raw", "/shared/mrbadmus.v2.js")),
    ("script /shared/ks3.js", ("raw", "/shared/ks3.js")),
    ("body[data-ks3-lesson]", ("css", "body[data-ks3-lesson]")),
    (".ks3-lesson", ("css", ".ks3-lesson")),
    (".ks3-ladder[data-lesson]", ("css", ".ks3-ladder[data-lesson]")),
    ("#s-ladder", ("css", "#s-ladder")),
    (".ks3-rung[data-rung]", ("css", ".ks3-ladder .ks3-rung[data-rung]")),
    (".ks3-rung[data-mode]", ("css", ".ks3-ladder .ks3-rung[data-mode]")),
    (".ks3-rung-q", ("css", ".ks3-ladder .ks3-rung-q")),
    ("[data-score]", ("css", ".ks3-ladder [data-score]")),
    (".ks3-option", ("css", ".ks3-option")),
    (".ks3-opt-label", ("css", ".ks3-opt-label")),
    ("[data-activity]", ("css", "[data-activity]")),
    ('[data-keyedblock][data-activity="hook"]', ("css", '[data-keyedblock][data-activity="hook"]')),
    ("[data-keyed]", ("css", "[data-keyedblock] [data-keyed]")),
    (".ks3-keyed-reply[data-reply]", ("css", ".ks3-keyed-reply[data-reply]")),
]
KS4_REBUILT_SELECTORS = [
    ("script /shared/config.js", ("raw", "/shared/config.js")),
    ("script /shared/mrbadmus.v2.js", ("raw", "/shared/mrbadmus.v2.js")),
    ("script /shared/ks4-runtime.js", ("raw", "/shared/ks4-runtime.js")),
    ("script /shared/ks4-lib.js", ("raw", "/shared/ks4-lib.js")),
    ("#ks4-mount", ("css", "#ks4-mount")),
    ("MrBadmusKS4Runtime.mount", ("raw", "MrBadmusKS4Runtime.mount")),
    (".ks3-ladder-score .ks3-score (" + LESSON_DONE + ")", ("raw", "ks3-ladder-score")),
]
KS4_CLASSIC_SELECTORS = [
    ("script /shared/config.js", ("raw", "/shared/config.js")),
    ("script /shared/mrbadmus.v2.js", ("raw", "/shared/mrbadmus.v2.js")),
    (".q-text", ("css", ".q-text")),
    (".quiz-opt", ("css", ".quiz-opt")),
    ("#quizEndMsg (" + LESSON_DONE + ")", ("css", "#quizEndMsg")),
    (".match-check-btn", ("css", ".match-check-btn")),
    (".match-drop[data-accepts]", ("css", ".match-drop[data-accepts]")),
    (".match-def[data-index]", ("css", ".match-def[data-index]")),
]
SELECTORS = {"ks3": KS3_SELECTORS, "ks4-rebuilt": KS4_REBUILT_SELECTORS, "ks4-classic": KS4_CLASSIC_SELECTORS}
# As tools/activity_save_coverage.py main() names them: option groups its classifier cannot judge.
UNSEEN = ("part of a form another button commits", "no single place the choice is kept", "a list of picks (choose several)")


def die(msg):
    print("Could not run: " + msg)
    raise SystemExit(2)


def load_tools(root):
    """Import the existing derivations and point them at `root`."""
    for p in (TOOLS, root):
        if p not in sys.path:
            sys.path.insert(0, p)
    from bs4 import BeautifulSoup
    import activity_save_coverage as asc
    import export_knowledge_points as ekp
    import kp_classify as kpc
    import kp_ks3_units as U
    import ks3_data
    import ks4_lessons as K
    kpc.REPO = U.REPO = asc.REPO = ekp.REPO = root
    kpc.KP_DIR = ekp.KP_DIR = os.path.join(root, "knowledge_points")
    U._SOUP.clear()
    return {"soup": BeautifulSoup, "asc": asc, "ekp": ekp, "kpc": kpc, "U": U, "ks3_data": ks3_data, "K": K}


def has_selector(soup, html, test):
    how, what = test
    return what in html if how == "raw" else soup.select_one(what) is not None


def short_hash(text):
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]


class Site:
    """One pass over every lesson page, by the existing derivations."""

    def __init__(self, tools, root):
        self.t, self.root = tools, root
        asc, kpc = tools["asc"], tools["kpc"]
        js = open(os.path.join(root, "shared", "mrbadmus.v2.js"), encoding="utf-8").read()
        self.tables = asc.capture_tables(js)
        self.shapes = json.load(open(os.path.join(root, "tools", "ks3_instrument_shapes.json"), encoding="utf-8"))["kinds"]
        self.explored = json.load(open(os.path.join(root, "tools", "ks4_root_explorations.json"), encoding="utf-8"))
        _lessons, _c, self.ks3_rows = asc.ks3(self.tables, self.shapes)
        self.ks3_by_page = collections.defaultdict(list)
        for r in self.ks3_rows:
            self.ks3_by_page[r["page"]].append(r)
        self.ks3_extra = {}          # slug -> {id: where} -- only page-derived
        self.pilot = kpc.ks4_pilot_items()
        self.ev = kpc.ks4_pilot_eval()
        self.batch = {L["slug"]: L["batch"] for L in tools["K"].all_lessons()}
        self.round5 = kpc.round5_inventory()
        self.matching = kpc.ks4_matching()
        _pages, self.ks4_groups = asc.ks4(self.tables, None)
        self.keys = kpc.answer_keys()
        self.records = {}
        self.read_all()

    # ------------------------------------------------------------------ KS3
    def ks3_ids(self, slug, rel, soup):
        """The ids a KS3 lesson page can send: the same reads as the capture."""
        U = self.t["U"]
        out = {}
        # The ladder: shared/ks3.js wireLadder, slug + "#" + data-rung.
        for lad in soup.select(".ks3-ladder"):
            ls = lad.get("data-lesson") or "lesson"
            for rung in lad.select(".ks3-rung[data-rung]"):
                out.setdefault("%s#%s" % (ls, rung.get("data-rung")), "ladder")
        # The Start here guess and keyed commits.
        for qid in U.page_choice_keys(slug):
            out.setdefault(qid, "guess or keyed commit")
        # Instruments: adapter A/B5C, then the <ks3-specs> kinds.
        for u in U.units(slug) + U.spec_units(slug):
            out.setdefault(u["id"], "instrument")
        # Predictions, no-reveal commits, "Your turn" calculations.
        for r in self.ks3_by_page.get(rel, []):
            cls, act = r["class"], r["activity"]
            if cls.startswith(("prediction", "commitment")):
                out.setdefault("%s#%s" % (slug, act), "prediction")
            elif cls.startswith('"Your turn"'):
                sec = soup.select_one('[data-activity="%s"]' % act)
                for q in sec.find_all(True) if sec is not None else []:
                    for k, v in q.attrs.items():
                        if re.match(r"^data-p\d+cfa-q$", k):
                            n = int(v) if str(v).isdigit() else 0
                            out.setdefault("%s#%s-%d" % (slug, act, n + 1), "your turn")
        return out

    def ks3_activities(self, rel):
        out = {}
        for r in self.ks3_by_page.get(rel, []):
            state = "saves" if (r["answerable"] and r["captured"]) else ("NOT saved" if r["answerable"] else "no answer")
            out[r["activity"]] = state
        return out

    def ladder_options(self, soup):
        """A fingerprint of each MCQ rung's options (the DB mirror holds them)."""
        out = {}
        for rung in soup.select(".ks3-ladder .ks3-rung[data-rung]"):
            opts = [(b.select_one(".ks3-opt-label") or b).get_text(" ", strip=True) for b in rung.select(".ks3-option")]
            if opts:
                out[rung.get("data-rung")] = short_hash("|".join(opts))
        return out

    # ------------------------------------------------------------------ KS4
    def ks4_rebuilt_ids(self, slug, route):
        kpc = self.t["kpc"]
        out = {}
        prefix = "ks4:%s:%s#" % (slug, route)
        for it in self.pilot.get(slug, []):
            if it[0].startswith(prefix):
                out[it[0]] = it[1]
        for it in self.round5.get(("KS4", slug), []):
            if it[0].startswith(prefix):
                out[it[0]] = it[1]
        # The practice set sends question_id null; the server hashes the prompt.
        for block in (self.ev.get(slug) or {}).get(route, []):
            if block.get("name") != "Ks4QuizBank":
                continue
            qs = [q for q in (block.get("props") or {}).get("questions") or [] if q]
            limit = len(qs) if self.batch.get(slug) == "pilot" else kpc.QUIZBANK_SENT
            for q in qs[:limit]:
                if isinstance(q, dict) and q.get("prompt"):
                    out[kpc.ks4_quiz_id(slug, str(q["prompt"]))] = "practice set"
        return out

    def ks4_classic_ids(self, slug, html, soup):
        kpc, ekp = self.t["kpc"], self.t["ekp"]
        out = {}
        p = ekp._QText()
        p.feed(html)
        for t in p.out:
            out[kpc.ks4_quiz_id(slug, t)] = "quiz card"
        if soup.select_one(".match-check-btn") is not None:
            for it in self.matching.get(slug, []):
                out[it[0]] = "matching card"
        return out

    def ks4_activities(self, rel, slug):
        """As tools/activity_save_coverage.py classifies a rebuilt page's own activities."""
        r = self.ks4_groups.get(rel) or {}
        forms = self.tables["forms"].get(slug, ())
        explored = self.explored.get(slug, {})
        out = {}

        def place(name):
            if name in forms:
                return "saves"
            return "explores" if name in explored else "NOT saved"
        for g in r.get("groups") or []:
            if g["kind"] in ("pick", "gate", "multi"):
                out[g["g"]] = "saves" if self.tables["generic_root"] or g["e"] in self.tables["ROOT_SPECS"].get(slug, set()) else "NOT saved"
            elif g.get("why") in UNSEEN or g["e"] in forms or g["e"] in explored:
                out[g["g"]] = place(g["e"])
        for f in r.get("fields") or []:
            out["field:" + f["on"]] = "explores" if f["type"] == "range" else place(f["on"])
        return out

    # ------------------------------------------------------------------ all
    def read_all(self):
        Soup = self.t["soup"]
        U = self.t["U"]
        for path in sorted(glob.glob(os.path.join(self.root, "ks3", "*", "*", "*.html"))):
            rel = os.path.relpath(path, self.root)
            html = open(path, encoding="utf-8").read()
            if "data-ks3-lesson" not in html:
                continue
            slug = os.path.basename(path)[:-5]
            soup = U.soup(slug)
            if soup is None or U.page_path(slug) != path:     # a slug only ever has one page
                soup = Soup(html, "lxml")
            self.records[rel] = self.record("ks3", slug, rel, html, soup, self.ks3_ids(slug, rel, soup),
                                            self.ks3_activities(rel), self.ladder_options(soup))
        pats = ("combined", "triple")
        for top in pats:
            for path in sorted(glob.glob(os.path.join(self.root, top, "*", "*", "*", "*.html"))):
                rel = os.path.relpath(path, self.root)
                html = open(path, encoding="utf-8").read()
                slug = os.path.basename(path)[:-5]
                parts = rel.split(os.sep)
                route = parts[0][0] + parts[1][0]
                soup = Soup(html, "lxml")
                if "ks4-mount" in html:
                    self.records[rel] = self.record("ks4-rebuilt", slug, rel, html, soup, self.ks4_rebuilt_ids(slug, route),
                                                    self.ks4_activities(rel, slug), None)
                elif ".q-text" in html or "q-text" in html or "match-check-btn" in html:
                    self.records[rel] = self.record("ks4-classic", slug, rel, html, soup, self.ks4_classic_ids(slug, html, soup), {}, None)

    def record(self, kind, slug, rel, html, soup, ids, activities, ladder):
        return {"kind": kind, "slug": slug, "ids": sorted(ids),
                "selectors": sorted(name for name, test in SELECTORS[kind] if has_selector(soup, html, test)),
                "activities": activities, "ladder_options": ladder or {}}


# ---------------------------------------------------------------- comparing

def load_tags(root):
    tagged, keys, scope_of, stale_pool = {}, {}, {}, collections.defaultdict(set)
    for name in ("ks3", "ks4"):
        d = json.load(open(os.path.join(root, "knowledge_points", name + ".json"), encoding="utf-8"))
        for ref, e in d.items():
            for q, kp in e["questions"].items():
                tagged[q] = kp
                scope_of[q] = (name, ref)
                stale_pool[(name, ref)].add(q)
            for q, k in (e.get("keys") or {}).items():
                keys[q] = k
    return tagged, keys, scope_of, stale_pool


def tag_of(qid, tagged):
    """The backend's kpOf fallbacks (consumer/answers.js), minus the exam twin."""
    if qid in tagged:
        return tagged[qid]
    if qid.startswith("ks4:") and "#" in qid:
        stem = qid
        while stem.rfind("-") > stem.index("#"):
            stem = stem[:stem.rfind("-")]
            if stem in tagged:
                return tagged[stem]
    m = re.match(r"^(.*#[^#]+?)-run-\d+$", qid)
    if m and (m.group(1) in tagged or m.group(1) + "-1" in tagged):
        return tagged.get(m.group(1)) or tagged.get(m.group(1) + "-1")
    return None


def load_map(args):
    def read(p):
        try:
            data = json.load(open(p, encoding="utf-8"))
        except (OSError, ValueError) as e:
            die("id map %s could not be read: %s" % (p, e))
        if not isinstance(data, dict) or any(not (v is None or isinstance(v, str)) for v in data.values()):
            die('id map %s must be {"old_id": "new_id" or null, ...}' % p)
        return data
    if args.map:
        files = args.map
    elif args.unit:
        files = [os.path.join(args.root, MAP_DIR, args.unit.replace("/", "-") + ".json")]
    else:
        files = sorted(glob.glob(os.path.join(args.root, MAP_DIR, "*.json")))
    out = {}
    used = []
    for f in files:
        if os.path.exists(f):
            out.update(read(f))
            used.append(os.path.relpath(f, args.root))
    return out, used


def select_pages(args, base, cur, tools):
    pages = set(base) | set(cur)
    if args.unit:
        hit = set()
        if re.match(r"^[A-Z]\d+$", args.unit):
            reg = tools["ks3_data"].lesson_registry()
            slugs = {s for s, L in reg.items() if L["_unit"] == args.unit}
            hit = {p for p in pages if p.startswith("ks3" + os.sep) and os.path.basename(p)[:-5] in slugs}
        else:
            want = args.unit if "/" in args.unit else "*/" + args.unit
            hit = {p for p in pages if p.split(os.sep)[0] in ("combined", "triple") and fnmatch.fnmatch("/".join(p.split(os.sep)[2:4]), want)}
        if not hit:
            die("no lesson pages found for unit %s" % args.unit)
        return sorted(hit)
    if args.slugs:
        slugs = {s.strip() for s in args.slugs.split(",") if s.strip()}
        hit = {p for p in pages if os.path.basename(p)[:-5] in slugs}
        if not hit:
            die("no lesson pages found for those slugs")
        return sorted(hit)
    hit = {p for p in pages if any(fnmatch.fnmatch(p, g) for g in args.pages)}
    if not hit:
        die("no lesson pages found for %s" % args.pages)
    return sorted(hit)


def check(pages, base, cur, idmap, tags, recomputed_keys, chk):
    tagged, keys, _scope, _pool = tags
    good_targets = set()
    for p in pages:
        r = cur.get(p)
        if r:
            good_targets.update(r["ids"])
    known = {q for p in pages for q in (base.get(p) or {}).get("ids", ())}
    for old, new in idmap.items():
        if new is not None and new not in good_targets:
            chk.fail("id map", '%s -> %s, but no chosen page sends %s' % (old, new, new))
        if old not in known:
            chk.note("id map", "%s is in the map but no chosen page ever sent it (outside this selection, or a typo)." % old)
    for p in pages:
        b, r = base.get(p), cur.get(p)
        if r is None:
            if b is not None:
                chk.fail("page gone", "%s is in the baseline but missing. Children's work items link to this exact URL." % p)
            continue
        if b is None:
            chk.note("new page", "%s is not in the baseline (a new lesson): checked for tags only." % p)
            chk.tagged_ids(p, r["ids"], tagged)
            continue
        for qid in b["ids"]:
            if qid in r["ids"]:
                continue
            if qid in idmap:
                continue
            chk.fail("id vanished", "%s: %s is gone and is not in the id map" % (p, qid))
        chk.tagged_ids(p, [q for q in r["ids"] if q not in set(b["ids"])], tagged)
        for qid in r["ids"]:
            if not QUESTION_ID_SHAPE.match(qid):
                chk.fail("id shape", "%s: %s breaks the server's id shape" % (p, qid))
        if b["kind"] != r["kind"]:
            chk.note("page type changed", "%s went from %s to %s: its selectors are checked against the new type." % (p, b["kind"], r["kind"]))
        else:
            for name in b["selectors"]:
                if name not in r["selectors"]:
                    chk.fail("selector gone", "%s: %s has disappeared" % (p, name))
        for act, state in b["activities"].items():
            if act not in r["activities"]:
                continue
            if state == "saves" and r["activities"][act] != "saves":
                chk.fail("stopped saving", '%s: activity "%s" saved and now does not (%s)' % (p, act, r["activities"][act]))
        for act, state in r["activities"].items():
            if state == "NOT saved" and act not in b["activities"]:
                chk.fail("new activity not saved", '%s: new activity "%s" takes an answer that does not save' % (p, act))
        for rung, h in b["ladder_options"].items():
            if rung in r["ladder_options"] and r["ladder_options"][rung] != h:
                chk.note("ladder options changed", "%s: the %s options changed, so ks3_ladder_questions must be reloaded when this ships." % (p, rung))
        for qid in r["ids"]:
            if qid in recomputed_keys and qid in tagged:
                now = recomputed_keys[qid][0]
                if qid in keys and now != keys[qid]:
                    chk.fail("answer key stale", "%s: %s key is %r in knowledge_points, the page now says %r. Run the top-up." % (p, qid, keys[qid], now))


def report_stale_tags(pages, base, cur, tags, chk):
    """A tag still pointing at an id this rebuild removed. Baseline ids only:
    the JSON holds older tags no page sends (classic cards a rebuilt lesson
    replaced) which the loaders still know, so they are not news."""
    tagged, _keys, _scope, _pool = tags
    wanted = collections.defaultdict(set)
    for r in cur.values():
        wanted[("ks3" if r["kind"] == "ks3" else "ks4", r["slug"])].update(r["ids"])
    for p in pages:
        b = base.get(p)
        if b is None:
            continue
        now = wanted.get(("ks3" if p.startswith("ks3" + os.sep) else "ks4", b["slug"]), set())
        for q in b["ids"]:
            if q in tagged and q not in now:
                chk.note("tag points at a removed id", "%s points at %s, which no page of this lesson sends now. The next top-up prunes it." % (tagged[q], q))


class Checker:
    def __init__(self):
        self.fails, self.notes = collections.defaultdict(list), collections.defaultdict(list)

    def fail(self, what, msg):
        self.fails[what].append(msg)

    def note(self, what, msg):
        if msg not in self.notes[what]:
            self.notes[what].append(msg)

    def tagged_ids(self, page, ids, tagged):
        for qid in ids:
            if not tag_of(qid, tagged):
                self.fail("new id has no tag", "%s: %s has no knowledge-point tag" % (page, qid))


# ---------------------------------------------------------------- the drive

PATCH_UN = """(function () {
  var o = UN.sec;
  UN.sec = function (k) { return (k.charAt(0) === '[' || k.charAt(0) === '#') ? document.querySelector(k) : o(k); };
  // The KS3 ladder marks a resolved rung on its element rather than with aria-pressed.
  var osig = UN.sig;
  UN.sig = function (sec) {
    if (sec.id !== 's-ladder') { return osig(sec); }
    return Array.prototype.map.call(sec.querySelectorAll('.ks3-rung'), function (r) { return r.getAttribute('data-rung-resolved') === '1' ? '1' : '0'; }).join('');
  };
  // A rebuilt KS4 page: the state of each shared answer block, keys sorted so
  // two runs compare; what the worked-example viewer shows is not an answer.
  UN.ks4States = function () {
    var ANSWER = /^Ks4(Guess|Choice|Cfifa|QuizBank|Write|Practice|Ladder|Sort)$/, skip = { workedEx: 1, workedStep: 1 };
    var canon = function (v) {
      if (Array.isArray(v)) { return v.map(canon); }
      if (v && typeof v === 'object') { var o = {}; Object.keys(v).sort().forEach(function (k) { if (!skip[k]) { o[k] = canon(v[k]); } }); return o; }
      return v;
    };
    return Array.prototype.filter.call(document.querySelectorAll('[data-dc-tpl]'), function (e) { return e.__mrbKs4 && ANSWER.test(e.__mrbKs4.comp || ''); })
      .map(function (e) { return e.__mrbKs4.comp + ' ' + JSON.stringify(canon(e.__mrbKs4.logic.state)); });
  };
  window.__fillIn = function (sec) {
    Array.prototype.forEach.call(sec.querySelectorAll('textarea, input[type=text], input:not([type])'), function (f) {
      if (!f.disabled && !f.value) {
        f.value = 'A force is a push or pull that acts between objects, because the reading stays the same.';
        f.dispatchEvent(new Event('input', { bubbles: true }));
        f.dispatchEvent(new Event('change', { bubbles: true }));
      }
    });
  };
})();"""


def refuse_production():
    """The configured backend, and anything in the environment naming one, must not be production."""
    import config_env
    config_env.backend()      # exits if MRB_API (or the TEST block) resolves to production
    for name in ("MRB_API", "SUPABASE_URL", "BACKEND_URL", "API_URL"):
        v = os.environ.get(name) or ""
        if v and (config_env.is_prod_url(v) or config_env.PROD_REF in v):
            die("%s names the production backend; this drive runs on TEST only." % name)


def drive(pages, cur, args, chk):
    refuse_production()
    import activity_save_drive as D
    import ks3_browser as KB
    D.REPO = args.root
    site, sport = D.start(D.Site)
    api, aport = D.start(D.Api)
    print("\nDrive: serving this checkout on 127.0.0.1 with the drive's pretend backend; every other host is blocked.")
    all_bodies, total = [], 0

    def blocks_of(r):
        if r["kind"] == "ks4-rebuilt":
            return ["ks4"]
        if r["kind"] == "ks4-classic":
            return [".quiz-opt"]
        out = ["#s-ladder"] if "#s-ladder" in r["selectors"] else []
        return out + ['[data-activity="%s"]' % a for a, s in sorted(r["activities"].items()) if s == "saves"]

    def run_page(page, r):
        """Device A presses, device B must show it back and send nothing."""
        url = "/" + page.replace(os.sep, "/")
        D.LEDGER.reset()
        sigs = {}
        with KB.Browser() as br:
            pg = D.open_page(br, sport, aport, url, D.session(True), args.width, pin_random=True)
            D.wait_saved(pg)
            pg.eval(D.UNITS_JS)
            pg.eval(PATCH_UN)
            for sel in blocks_of(r):
                if sel == ".quiz-opt":
                    continue
                exists = pg.eval("!!UN.sec(%s)" % json.dumps(sel))
                if not exists:
                    chk.fail("drive", "%s: block %s is not on the page" % (page, sel))
                    continue
                if r["kind"] != "ks4-rebuilt":
                    pg.eval("__fillIn(UN.sec(%s))" % json.dumps(sel))
                n0 = len(D.LEDGER.bodies)
                res = json.loads(pg.eval("UN.go(%s)" % json.dumps(sel), timeout=90))
                time.sleep(0.4)
                sigs[sel] = (res["sig"], len(D.LEDGER.bodies) - n0)
            time.sleep(0.8)
            states_a = pg.eval("UN.ks4States()") if r["kind"] == "ks4-rebuilt" else []
            errs = [e for e in pg.console_errors() if "ERR_BLOCKED" not in e and "429" not in e]
        bodies = list(D.LEDGER.bodies)
        sent = [row["question_id"] for row in D.LEDGER.rows]
        if errs:
            chk.fail("drive", "%s: page errors: %s" % (page, errs[:2]))
        unknown = sorted({q for q in sent if q not in r["ids"] and not tag_of(q, {x: 1 for x in r["ids"]}) and not any(i.startswith(q + "-") for i in r["ids"])})
        for q in unknown:
            chk.note("drive saw an id the static list lacks", "%s sent %s" % (page, q))
        n_before = len(D.LEDGER.bodies)
        back_ok, compared = True, 0
        with KB.Browser() as br:
            pg = D.open_page(br, sport, aport, url, D.session(True), args.width, pin_random=True)
            st = D.wait_saved(pg)
            time.sleep(1.2)
            pg.eval(D.UNITS_JS)
            pg.eval(PATCH_UN)
            if st != "done":
                chk.fail("drive", "%s: device B never finished restoring (state %s)" % (page, st))
            for sel, (sig_a, posted) in sigs.items():
                if not posted or r["kind"] == "ks4-rebuilt" or not pg.eval("!!UN.sec(%s)" % json.dumps(sel)):
                    continue
                sig_b = pg.eval("UN.sig(UN.sec(%s))" % json.dumps(sel))
                compared += 1
                # Something this block saved must be on screen on device B. A block
                # showing one tab at a time ends device A on whichever tab was last
                # pressed, so device A's count can be lower; never higher.
                a_n, b_n = sig_a.count("1"), sig_b.count("1")
                if (a_n and not b_n) or b_n < a_n:
                    back_ok = False
                    chk.fail("drive", "%s: %s did not come back on device B (%d pressed on A, %d on B)" % (page, sel, a_n, b_n))
            if r["kind"] == "ks4-rebuilt":
                states_b = pg.eval("UN.ks4States()")
                compared = len(states_b)
                for x, y in zip(states_a, states_b):
                    if x != y:
                        back_ok = False
                        chk.fail("drive", "%s: the saved state of %s did not come back on device B" % (page, x.split(" ")[0]))
                if len(states_a) != len(states_b):
                    back_ok = False
                    chk.fail("drive", "%s: device B drew %d answer blocks, device A %d" % (page, len(states_b), len(states_a)))
            time.sleep(0.6)
        if len(D.LEDGER.bodies) != n_before:
            back_ok = False
            chk.fail("drive", "%s: device B POSTED %d answer(s) while restoring" % (page, len(D.LEDGER.bodies) - n_before))
        if not bodies:
            chk.fail("drive", "%s: pressing the page's controls saved nothing" % page)
        print("  %s  %s: %d answers saved (%d ids), %d block(s) back on device B" % ("ok " if back_ok and bodies else "XX", page, len(bodies), len(set(sent)), compared))
        return bodies

    for page in pages:
        r = cur.get(page)
        if r is None:
            continue
        if r["kind"] == "ks4-classic":
            print("  --  %s: a classic page has its own fixed cases in activity_save_drive.py; not pressed here." % page)
            continue
        for attempt in (1, 2):
            try:
                all_bodies.extend(run_page(page, r))
                total += 1
                break
            except KB.CDPError as e:
                if attempt == 2:
                    chk.fail("drive", "%s: Chrome stopped answering twice (%s)" % (page, str(e)[:100]))
    if not all_bodies:
        return
    if not os.path.isdir(D.BACKEND):
        chk.note("drive", "MRB_BACKEND_DIR not set or not found: bodies were not run through the server's validateAnswerBody.")
    else:
        bad = D.validate(all_bodies)
        if bad and bad[0][0] == "(validator did not run)":
            chk.note("drive", "the server's validator did not run: %s" % bad[0][1])
        else:
            for q, why in bad:
                chk.fail("drive", "the real server would refuse %s (%s)" % (q, why))
    print("  Pressed %d page(s), %d answers." % (total, len(all_bodies)))


# ---------------------------------------------------------------- the baseline

def git(args, *cmd):
    return subprocess.run(["git", "-C", args.root] + list(cmd), capture_output=True, text=True)


def write_baseline(site, args):
    ahead = git(args, "rev-list", "--count", "origin/main..HEAD").stdout.strip()
    dirty = git(args, "status", "--porcelain", "--", "ks3", "combined", "triple", "knowledge_points", "shared/mrbadmus.v2.js", "shared/ks3.js").stdout.strip()
    if ahead != "0" or dirty:
        die("--write-baseline is only for a clean checkout of main, before a rebuild starts. "
            "This checkout is %s commit(s) ahead of origin/main and has %s uncommitted lesson change(s). "
            "It must never be run to make a failing check pass." % (ahead, "some" if dirty else "no"))
    commit = git(args, "rev-parse", "--short", "HEAD").stdout.strip()
    data = {"note": "Captured by tools/lesson_contract_check.py --write-baseline, from main before a rebuild.",
            "commit": commit, "lessons": site.records}
    lines = ['{"commit":%s,"note":%s,"lessons":{' % (json.dumps(commit), json.dumps(data["note"]))]
    body = []
    for p in sorted(site.records):
        body.append("%s:%s" % (json.dumps(p), json.dumps(site.records[p], separators=(",", ":"), sort_keys=True, ensure_ascii=False)))
    lines.append(",\n".join(body))
    lines.append("}}")
    with open(args.baseline, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    n = sum(len(r["ids"]) for r in site.records.values())
    print("Baseline written: %d lesson pages, %d question ids, from %s, to %s." % (len(site.records), n, commit, os.path.relpath(args.baseline, args.root)))


def ledger_sql(idmap, used):
    print("-- id map(s): %s" % (", ".join(used) or "none"))
    print("-- Paste into the Supabase SQL editor when the rebuilt unit ships (Mide's step).")
    print("-- Moves saved answers onto the new ids. Retired ids (null) stay as they are.")
    print("begin;")
    for old, new in sorted(idmap.items()):
        if new is not None:
            print("update public.child_answers set question_id = '%s' where question_id = '%s';" % (new.replace("'", "''"), old.replace("'", "''")))
    print("commit;")


# ---------------------------------------------------------------- main

def summary(chk, pages, cur, base, args):
    print("")
    for what, msgs in sorted(chk.notes.items()):
        print("NOTE (%s, %d):" % (what, len(msgs)))
        for m in msgs[:40]:
            print("   - " + m)
        if len(msgs) > 40:
            print("   ... and %d more" % (len(msgs) - 40))
    for what, msgs in sorted(chk.fails.items()):
        print("FAIL (%s, %d):" % (what, len(msgs)))
        for m in msgs[:60]:
            print("   - " + m)
        if len(msgs) > 60:
            print("   ... and %d more" % (len(msgs) - 60))
    n_ids = sum(len(cur[p]["ids"]) for p in pages if p in cur)
    n_fail = sum(len(v) for v in chk.fails.values())
    print("")
    if n_fail:
        print("NOT SAFE: %d problem(s) on %d lesson page(s). A family child's saved work or tags would break. Fix each line above." % (n_fail, len(pages)))
        return 1
    print("SAFE: %d lesson page(s), %d question id(s) checked. Saving, restoring and tags are intact%s."
          % (len(pages), n_ids, " (live drive included)" if args.drive else " (static check; add --drive for the live part)"))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--unit", help="a KS3 unit code (P4) or KS4 subject/topic (physics/energy)")
    ap.add_argument("--slugs", help="comma-separated lesson slugs")
    ap.add_argument("--pages", nargs="+", help="path glob(s), from the repo root")
    ap.add_argument("--map", action="append", help="an id map file (default: docs/b2c/id-maps/<unit>.json, or all maps there)")
    ap.add_argument("--root", default=HOME, help="the site tree to check (default: this checkout). A complete copy; used to prove the check.")
    ap.add_argument("--baseline", default=BASELINE, help=argparse.SUPPRESS)
    ap.add_argument("--drive", action="store_true", help="also press the pages in headless Chrome, TEST only; see above")
    ap.add_argument("--width", type=int, default=1280, help=argparse.SUPPRESS)
    ap.add_argument("--write-baseline", action="store_true", help="regenerate the baseline: only from a clean main, before a rebuild")
    ap.add_argument("--ledger-sql", action="store_true", help="print the SQL that moves saved answers onto the new ids in the map")
    args = ap.parse_args()
    args.root = os.path.abspath(args.root)
    if not args.write_baseline and not (args.unit or args.slugs or args.pages):
        ap.error("say which lessons: --unit, --slugs or --pages (or --write-baseline)")

    tools = load_tools(args.root)
    site = Site(tools, args.root)
    if args.write_baseline:
        write_baseline(site, args)
        return 0
    if not os.path.exists(args.baseline):
        die("no baseline at %s. Run --write-baseline from a clean main first." % args.baseline)
    baseline = json.load(open(args.baseline, encoding="utf-8"))
    base, cur = baseline["lessons"], site.records

    pages = select_pages(args, base, cur, tools)
    idmap, used = load_map(args)
    if args.ledger_sql:
        ledger_sql(idmap, used)
        return 0
    print("Checking %d lesson page(s) against the baseline from %s." % (len(pages), baseline.get("commit")))
    print("Id map: %s (%d entries)." % (", ".join(used) or "none", len(idmap)))
    chk = Checker()
    tags = load_tags(args.root)
    check(pages, base, cur, idmap, tags, site.keys, chk)
    report_stale_tags(pages, base, cur, tags, chk)
    if args.drive and not chk.fails:
        drive(pages, cur, args, chk)
    elif args.drive:
        print("\nDrive skipped: the static check failed first.")
    return summary(chk, pages, cur, base, args)


if __name__ == "__main__":
    sys.exit(main())
