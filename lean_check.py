#!/usr/bin/env python3
"""lean_check.py: the lean lesson standard, as a fast gate (docs/lessons/LEAN-STANDARD.md).

Checks every lean record (ks3_data/lean/*.py, ks4_lessons/lean/*.py) and the page it
builds. No browser. The generators call run() too, so a hit stops the full build.

Teaching text is everything a record writes: Start here, key words, every card and
reveal table, Key fact, Dive deeper, the KS3 ladder feedback. It is NOT the quiz
(ladder questions and options, quiz items, CFIFA numbers), which this standard does not
reword.

    voice      every phrase in the standard's "Never use" list; "not X, it's Y" and
               "isn't just X, it's Y" contrasts; em and en dashes used as punctuation;
               a question mark anywhere outside Start here and a ladder stem
    length     KS3: no sentence over 15 words
    shape      exactly 3 or 4 key words; exactly two Start here options with answer 0 or 1;
               KS4 route sets the template can gate; rung labels are "Rung 1".."Rung 4";
               no embedded bench or instrument on the page
    spec       docs/lessons/pilot/ks3-<slug>.md / ks4-<slug>.md exists. A WARNING until
               the spec tables are all in; STRICT_SPEC (or --strict-spec) makes it a failure.

    python3 lean_check.py [--strict-spec]
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STRICT_SPEC = False   # flipped to True when every spec table is written

# The standard's "Never use" list. Matched case-insensitively on whole words.
PHRASES = [
    "it's important to note", "it is important to note", "it's worth noting",
    "it is worth noting", "notice that", "remember that",
    "this is not a technicality", "the whole explanation", "precisely", "crucially",
    "essentially", "fundamentally", "in fact", "simply put", "let's explore",
    "let us explore", "dive into", "persuade", "settles it",
    "the atmosphere does all the work",
]
_PHRASE_RES = [(p, re.compile(r"(?<![\w])" + re.escape(p).replace(r"\ ", r"\s+") + r"(?![\w])", re.I))
               for p in PHRASES]

# "not X, it's Y" / "isn't just X, it's Y" contrasts used for effect.
_CONTRASTS = [
    ("'not X, it's Y' contrast",
     re.compile(r"\bnot\b[^.?!;]{1,70}[,;]\s*(?:it'?s|it is|that'?s|this is)\b", re.I)),
    ("'isn't just X, it's Y' contrast",
     re.compile(r"\b(?:isn'?t|aren'?t|is not|are not)\s+(?:just|only|simply|merely)\b", re.I)),
    ("'not just X, but Y' contrast",
     re.compile(r"\bnot\s+(?:just|only|simply|merely)\b[^.?!;]{1,70},?\s+but\b", re.I)),
]

_TAG = re.compile(r"<[^>]+>")


def _norm(s):
    s = _TAG.sub("", str(s)).replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", s).strip()


# ── pulling the teaching text out of a record ───────────────────────────

def _strings(obj, skip_slots=True):
    """Every string in a card or table, in order."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        if "slot" in obj or "figure" in obj:
            return
        for k in ("title", "body", "points", "cols", "rows"):
            if k in obj:
                yield from _strings(obj[k])
        if "mistakes" in obj:
            for pair in obj["mistakes"]:
                yield from _strings(list(pair))
    elif isinstance(obj, (list, tuple)):
        for x in obj:
            yield from _strings(x)


def teaching_texts(rec):
    """[(where, text, kind)]. kind: 'start' (a question mark is fine), 'stem' (a
    ladder stem, ditto) or 'teach'."""
    out = []
    st = rec.get("start") or {}
    if st.get("setup"):
        out.append(("start.setup", st["setup"], "start"))
    # the Start here question is an existing question kept as it was (Mide, 11 Nov): its
    # id and wording stay, so the 15-word sentence limit does not apply to it
    out.append(("start.question", st.get("question", ""), "startq"))
    for i, o in enumerate(st.get("options") or []):
        out.append(("start.options[%d] label" % i, o[0], "start"))
        out.append(("start.options[%d] reply" % i, o[1], "start"))
    for i, w in enumerate(rec.get("words") or []):
        out.append(("words[%d]" % i, w, "teach"))
    for part, key in (("knowledge", "knowledge"), ("deeper", "deeper")):
        for i, item in enumerate(rec.get(key) or []):
            t = item.get("title", "?")
            for s in _strings(item):
                out.append(("%s[%d] %r" % (part, i, t), s, "teach"))
    out.append(("key_fact", rec.get("key_fact", ""), "teach"))
    if rec.get("try"):
        out.append(("try.label", rec["try"].get("label", ""), "teach"))
    for rung, fb in (rec.get("ladder_feedback") or {}).items():
        for k, s in fb.items():
            out.append(("ladder_feedback[%s][%s]" % (rung, k), s, "teach"))
    for rung, s in (rec.get("ladder_stem") or {}).items():
        out.append(("ladder_stem[%s]" % rung, s, "stem"))
    # render-only overlays: wording a pupil reads on the lean page (marking points are quiz items)
    for k, v in (rec.get("connects") or {}).items():
        out.append(("connects[%s]" % k, v, "teach"))
    for k, v in (rec.get("figure_caption") or {}).items():
        if v:
            out.append(("figure_caption[%s]" % k, v, "teach"))
    for k, v in (rec.get("word_defs") or {}).items():
        out.append(("word_defs[%s]" % k, v, "teach"))
    for i, (_old, new) in enumerate(rec.get("ladder_ticks") or []):
        out.append(("ladder_ticks[%d]" % i, new, "stem"))
    if rec.get("convention_note"):
        out.append(("convention_note", rec["convention_note"], "teach"))
    return out


# ── the per-text checks ─────────────────────────────────────────────────

def check_text(where, text, kind, ks):
    """Problems for one string. `ks` is 3 or 4."""
    t = _norm(text)
    probs = []
    if not t:
        return probs
    for p, rx in _PHRASE_RES:
        if rx.search(t):
            probs.append("%s: never-use phrase %r in %r" % (where, p, t[:90]))
    for label, rx in _CONTRASTS:
        m = rx.search(t)
        if m:
            probs.append("%s: %s: %r" % (where, label, m.group(0)[:80]))
    if kind == "stem":
        return probs   # a ladder stem is a quiz item: only the never-use phrases apply
    if "—" in t:
        probs.append("%s: em dash in %r" % (where, t[:90]))
    if re.search(r"(?<!\d)–|–(?!\d)", t):
        probs.append("%s: en dash in %r" % (where, t[:90]))
    if re.search(r"\s-\s", t):
        probs.append("%s: spaced hyphen used as a dash in %r" % (where, t[:90]))
    if "?" in t and kind == "teach":
        probs.append("%s: question mark in teaching text: %r" % (where, t[:90]))
    if ks == 3 and kind != "startq":
        for sent in re.split(r"(?<=[.!?])\s+", t):
            n = len(sent.split())
            if n > 15:
                probs.append("%s: KS3 sentence of %d words (limit 15): %r" % (where, n, sent[:90]))
    return probs


def check_record(rec, ks, key_slug=None):
    slug = rec.get("slug", "?")
    tag = "ks%d %s" % (ks, slug)
    probs = []
    words = rec.get("words") or []
    if not 3 <= len(words) <= 4:
        probs.append("%s: %d key words (need 3 or 4)" % (tag, len(words)))
    st = rec.get("start") or {}
    if len(st.get("options") or []) != 2:
        probs.append("%s: Start here has %d options (need exactly 2)"
                     % (tag, len(st.get("options") or [])))
    if st.get("answer") not in (0, 1):
        probs.append("%s: Start here answer must be 0 or 1" % tag)
    for where, text, kind in teaching_texts(rec):
        probs.extend("%s: %s" % (tag, p) for p in check_text(where, text, kind, ks))
    if ks == 4:
        import lean_blocks
        for part in ("knowledge", "deeper"):
            for it in rec.get(part) or []:
                try:
                    lean_blocks.route_flag(it.get("routes"))
                except ValueError as e:
                    probs.append("%s: %s[%r]: %s" % (tag, part, it.get("title"), e))
    return probs


# ── the page-level checks ───────────────────────────────────────────────

_KS4_IMPORT_OK = {"Ks4Chrome", "Ks4Guess", "Ks4Practice", "Ks4Ladder", "Ks4QuizBank", "Ks4End",
                  "Ks4Triangle", "Ks4Cfifa", "Ks4Steps"}


def check_ks3_pages(records):
    import build_ks3
    import ks3_data
    probs = []
    reg = ks3_data.lesson_registry()
    for slug in sorted(records):
        l = reg.get(slug)
        if l is None or not l.get("lean"):
            probs.append("ks3 %s: has a lean record but the lesson does not carry it" % slug)
            continue
        core = l.get("core") or []
        bad = [b["type"] for b in core
               if not (b["type"].startswith("lean-") or b["type"] == "quiz")]
        if bad:
            probs.append("ks3 %s: core still holds %s (a lean page has only lean blocks and the ladder)"
                         % (slug, bad))
        # the big question stays on the lesson data (browse pages print it) but not on the lean page
        units = ks3_data.build_units()
        reg2 = ks3_data.lesson_registry(units)
        ubc = {u["code"]: u for u in units}
        for x in reg2.values():
            x["_disc"] = ubc[x["_unit"]]["discipline"]
        page = build_ks3.lesson_page(ubc[l["_unit"]], reg2[slug], reg2, ubc, build_ks3.lesson_neighbours(units))
        if "ks3-bigq" in page:
            probs.append("ks3 %s: a big question is still on the page" % slug)
        html = build_ks3.render_blocks(l, core)
        if html.count("data-instrument") != 1:
            probs.append("ks3 %s: %d instrument shells on the page (only Start here may have one)"
                         % (slug, html.count("data-instrument")))
        for marker in ("ks3-bell", "data-sim", "<canvas", "data-bench"):
            if marker in html:
                probs.append("ks3 %s: embedded bench or simulation markup (%s)" % (slug, marker))
        heads = re.findall(r'<h3 tabindex="-1">([^<]*)</h3>', html)
        want = ["Rung %d" % i for i in range(1, 5)]
        if heads != want:
            probs.append("ks3 %s: rung labels are %r, need exactly %r" % (slug, heads, want))
    return probs


def check_ks4_pages(lessons):
    import build_ks4
    import lean_ks4
    probs = []
    for L in lessons:
        slug = L["slug"]
        try:
            build_ks4.ks4_science_rulings.reset_applied()
            legacy = (build_ks4.legacy_texts(L["legacy_batch"], L)
                      if L.get("legacy_batch") else None)
            tpl, logic, _ = lean_ks4.source(L, legacy)
        except SystemExit as e:
            probs.append("ks4 %s: the page source does not build: %s" % (slug, e))
            continue
        names = set(re.findall(r'<dc-import name="(Ks4\w+)"', tpl))
        bad = sorted(names - _KS4_IMPORT_OK)
        if bad:
            probs.append("ks4 %s: embedded bench or instrument block(s) %s" % (slug, bad))
        if "bigq" in tpl or "draftVisible" in tpl:
            probs.append("ks4 %s: a big-question line or Draft flag is still in the header" % slug)
    # rung labels live in the lean batch's own blocks
    for n in ("Ks4Practice", "Ks4Ladder"):
        p = os.path.join(HERE, "ks4_lessons", "lean", "blocks", n + ".dc.html")
        if os.path.exists(p):
            text = open(p, encoding="utf-8").read()
            if re.search(r"Rung\s*['\"+ ()\w]*\s*(?:\\u00b7|·)", text):
                probs.append("ks4 %s block: a rung label still carries a tag line" % n)
            if "ks3-ladder-sub" in text:
                probs.append("ks4 %s block: the 'Four rungs...' sub line is still there" % n)
    return probs


def spec_table_problems(ks3_slugs, ks4_slugs):
    missing = []
    for ks, slugs in (("ks3", ks3_slugs), ("ks4", ks4_slugs)):
        for s in sorted(slugs):
            if not os.path.exists(os.path.join(HERE, "docs", "lessons", "pilot", "%s-%s.md" % (ks, s))):
                missing.append("%s %s: no spec table at docs/lessons/pilot/%s-%s.md" % (ks, s, ks, s))
    return missing


def duplicate_keys():
    """A record is one dict literal; Python keeps the LAST of two equal keys and says nothing.
    Two `"ladder_stem"` entries lost one's words silently, so refuse any repeated top-level key."""
    import ast
    import glob
    problems = []
    for path in sorted(glob.glob(os.path.join(HERE, "ks3_data", "lean", "*.py"))
                       + glob.glob(os.path.join(HERE, "ks4_lessons", "lean", "*.py"))):
        if os.path.basename(path).startswith("_"):
            continue
        tree = ast.parse(open(path, encoding="utf-8").read())
        for node in tree.body:
            if (isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "LESSON" for t in node.targets)
                    and isinstance(node.value, ast.Dict)):
                seen = set()
                for k in node.value.keys:
                    name = getattr(k, "value", None)
                    if name in seen:
                        problems.append("%s: the record has the key %r twice (the second silently wins)"
                                        % (os.path.relpath(path, HERE), name))
                    seen.add(name)
    return problems


def run(strict_spec=None, pages=True, ks=(3, 4)):
    """(problems, warnings). `pages=False` checks the records only; `ks` picks the key stage(s)."""
    if strict_spec is None:
        strict_spec = STRICT_SPEC
    sys.path.insert(0, HERE)
    import ks3_data.lean as k3
    import ks4_lessons
    ks3 = k3.records()
    k4_lessons = ks4_lessons.lean_lessons()
    problems = list(duplicate_keys())
    ks3 = ks3 if 3 in ks else {}
    k4_lessons = k4_lessons if 4 in ks else []
    for slug, rec in sorted(ks3.items()):
        problems += check_record(rec, 3)
    for L in k4_lessons:
        problems += check_record(L["lean"], 4)
    if pages:
        problems += check_ks3_pages(ks3)
        problems += check_ks4_pages(k4_lessons)
    spec = spec_table_problems(ks3, [L["slug"] for L in k4_lessons])
    warnings = []
    (problems if strict_spec else warnings).extend(spec)
    return problems, warnings


def main(argv):
    strict = "--strict-spec" in argv
    problems, warnings = run(strict_spec=strict or None)
    for w in warnings:
        print("  warn  %s" % w)
    if problems:
        print("❌ lean_check: %d problem(s)\n" % len(problems))
        for p in problems:
            print("   · %s" % p)
        return 1
    import ks3_data.lean as k3
    import ks4_lessons
    print("✅ lean_check: %d KS3 and %d KS4 lean record(s) clean%s"
          % (len(k3.records()), len(ks4_lessons.lean_lessons()),
             " (%d spec table(s) still to write)" % len(warnings) if warnings else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
