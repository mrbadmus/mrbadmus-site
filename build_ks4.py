#!/usr/bin/env python3
"""build_ks4.py — the KS4 pilot generator (docs/ks4/pilot-build-contract.md).

    python3 build_ks4.py

Compiles Design's 14 lesson `.dc.html` files and 11 shared block `.dc.html`
files (docs/ks4/design-reference/pilot/KS4 Lessons/Pilot - Bonding and
Electricity/) into 54 static pages under `mrbadmus_site/{combined,triple}/
{foundation,higher}/{chemistry,physics}/{bonding,electricity}/<slug>.html` —
the SAME URLs the old (pre-port) KS4 generator already serves for these 14
subtopics. `generate_site_v5.py` writes the old design there first (it
always runs); this script OVERWRITES those 54 paths with the ported design
immediately after — see the note next to its `build_all.py` step.

No React, no Babel, no `support.js`: `shared/ks4-runtime.js` renders
Design's compiled templates and her (verbatim, ruling-corrected) logic
classes without them. See that file's own docstring for the runtime; see
`ks4_rulings.py` for every correction applied to Design's delivery and why.

⚠️ `ks4_data/` (the KS4 question-pool package) is NEVER imported or touched
here — a hard line (contract §2). This script reads `all_subtopics_*.py`
only, the same files `generate_site_v5.py` reads.
"""

import hashlib
import importlib
import json
import os
import re
import sys
import time

import ks4_lessons
from ks4_lessons import blocks as ks4_blocks
import ks4_rulings

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
DESIGN_DIR = ks4_lessons.DESIGN_DIR
DS_DIR = os.path.join("docs", "ks4", "design-reference", "pilot", "_ds",
                       "mrbadmusai-design-system-53dad5ae-951a-44a1-95e1-394b9762b2d1")
OUT_ROOT = "mrbadmus_site"
INVENTORY_DIR = os.path.join("docs", "ks4", "pilot-inventory")
MANIFEST_PATH = "ks4_pilot_manifest.json"

BLOCK_NAMES = ["Ks4Chrome", "Ks4Choice", "Ks4Sort", "Ks4Chain", "Ks4Write",
               "Ks4Cfifa", "Ks4Ladder", "Ks4KeyNote", "Ks4QuizBank", "Ks4End",
               "Ks4Video"]

ROUTE_CODES = ["CF", "CH", "TF", "TH"]
ROUTE_LABEL = ks4_lessons.ROUTE_LABELS
ROUTE_URL = ks4_lessons.ROUTE_URL

# ⊕ these are OUR OWN new assets, a SEPARATE list from build_ks3.py's
# VERSIONED_ASSETS tuple (contract §1: "add a KS4 list in build_ks4.py — do
# not edit build_ks3.py's tuple in place"). mrbadmus.v2.js is included
# because our pages load it too, even though we never write it ourselves.
KS4_VERSIONED = ("ks4-ds.css", "ks4-theme.css", "ks4-lesson.css",
                  "ks4-source.js", "ks4-lib.js", "ks4-diagrams.js",
                  "ks4-runtime.js", "mrbadmus.v2.js")

# The subset of KS4_VERSIONED this script itself WRITES (excludes
# mrbadmus.v2.js, which it only reads — that one is generate_site_v5.py's,
# already synced by its own round-trip). Cloudflare serves from
# mrbadmus_site/, not the repo root, so a page linking /shared/ks4-lib.js
# 404s unless the file is copied there too — the same reason build_ks3.py
# copies ks3.css/ks3.js/tokens.css into mrbadmus_site/shared/ itself rather
# than trusting generate_site_v5.py to have done it: generate_site_v5.py's
# copy of shared/ happens BEFORE this script runs (build_all.py's step
# order), so anything this script writes into shared/ AFTER that has to be
# synced here, not assumed.
KS4_OWN_ASSETS = ("ks4-ds.css", "ks4-theme.css", "ks4-lesson.css",
                   "ks4-source.js", "ks4-lib.js", "ks4-diagrams.js",
                   "ks4-runtime.js")


def _shared(name):
    return os.path.join("shared", name)


# ═══════════════════════════════════════════════════════════════════════
# STEP A — shared/ks4-source.js, GENERATED from all_subtopics_*.py
# ═══════════════════════════════════════════════════════════════════════
SOURCE_MODULES = {
    "chemistry": {"CF": "all_subtopics_chemistry",
                  "CH": "all_subtopics_chemistry_higher",
                  "TF": "all_subtopics_chemistry_triple_foundation",
                  "TH": "all_subtopics_chemistry_triple_higher"},
    "physics": {"CF": "all_subtopics_physics",
                "CH": "all_subtopics_physics_higher",
                "TF": "all_subtopics_physics_triple_foundation",
                "TH": "all_subtopics_physics_triple_higher"},
}
SOURCE_ATTR = {"chemistry": "CHEMISTRY_SUBTOPICS_ALL", "physics": "PHYSICS_SUBTOPICS_ALL"}

# The non-quiz fields Design's ks4-source.js carries. `quiz` is handled
# separately below because it is the one field that genuinely varies by
# route; every other field is taken from ONE canonical record (see
# `build_source_record`).
NONQUIZ_FIELDS = ["summary", "theory", "common_mistake", "examiner_tip",
                   "key_note", "matching", "fifas", "equations", "rp",
                   "variables", "higher"]


def load_subtopics_by_route():
    """{subject: {route_code: SUBTOPICS_ALL dict}} — the same four files per
    subject `generate_site_v5.py` imports, aliased the same way it does."""
    out = {}
    for subject, routes in SOURCE_MODULES.items():
        out[subject] = {}
        for route, modname in routes.items():
            mod = importlib.import_module(modname)
            out[subject][route] = getattr(mod, SOURCE_ATTR[subject])
    return out


def find_subtopic(data, subject, route, topic_id, slug):
    lst = data[subject][route].get(topic_id, [])
    return next((s for s in lst if s["id"] == slug), None)


def build_source_record(data, lesson):
    """One lesson's record for shared/ks4-source.js. Non-quiz fields are
    taken from the TRIPLE HIGHER file — always present for all 14 lessons
    (it is the "everything" tier) — so there is exactly one canonical
    theory/summary/key_note/examiner_tip/common_mistake per lesson, the way
    Design's own file has one. `quiz` is the one field built per route."""
    slug, subject, topic = lesson["slug"], lesson["subject"], lesson["topic_id"]
    canon = find_subtopic(data, subject, "TH", topic, slug)
    if canon is None:
        raise SystemExit("build_ks4.build_source_record: no TH record for %r" % slug)
    rec = {}
    for f in NONQUIZ_FIELDS:
        v = canon.get(f)
        if v:
            rec[f] = v
    quiz = {}
    for route in lesson["routes"]:
        st = find_subtopic(data, subject, route, topic, slug)
        if st and st.get("quiz"):
            quiz[route] = st["quiz"]
    rec["quiz"] = quiz
    return rec


def build_source_js(data):
    lines = [
        "/* shared/ks4-source.js — GENERATED by build_ks4.py from "
        "all_subtopics_chemistry*.py / all_subtopics_physics*.py.",
        "   Never hand-edit — re-run build_ks4.py. Keyed by SITE slug "
        "(see ks4_rulings.py R-SLUG for the three lessons whose OWN",
        "   `const slug` differs from it). A build check diffs this against "
        "Design's own ks4-source.js field by field —",
        "   docs/ks4/pilot-inventory/source-diff.md. */",
        "window.KS4SRC = window.KS4SRC || {};",
    ]
    per_slug = {}
    for lesson in ks4_lessons.LESSONS:
        rec = build_source_record(data, lesson)
        per_slug[lesson["slug"]] = rec
        lines.append('window.KS4SRC["%s"] = %s;'
                      % (lesson["slug"], json.dumps(rec, sort_keys=True)))
    return "\n".join(lines) + "\n", per_slug


_KS4SRC_LINE_RE = re.compile(r'window\.KS4SRC\["([^"]+)"\]\s*=\s*(\{.*?\});', re.S)


def load_design_source_js():
    path = os.path.join(DESIGN_DIR, "ks4-source.js")
    text = open(path, encoding="utf-8").read()
    out = {}
    for m in _KS4SRC_LINE_RE.finditer(text):
        out[m.group(1)] = json.loads(m.group(2))
    return out


def _first_diff_note(a, b, path=""):
    """STRUCTURE-AWARE: walks matching dict keys / list indices rather than
    comparing two serialized strings character-by-character, which drifts
    out of alignment the moment the two sides serialize ONE field with a
    different length (whitespace, key order, unicode-escaping) and then
    "diffs" a hundred unrelated characters later. Returns the first leaf
    value that genuinely differs, with its path."""
    if a is None and b is None:
        return ""
    if a is None:
        return " — design has no value at %s; ours: %s" % (path or "(root)", json.dumps(b)[:160])
    if b is None:
        return " — ours has no value at %s; design's: %s" % (path or "(root)", json.dumps(a)[:160])
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a:
                return " — design is missing key %r (at %s)" % (k, path)
            if k not in b:
                return " — ours is missing key %r (at %s)" % (k, path)
            if a[k] != b[k]:
                return _first_diff_note(a[k], b[k], "%s.%s" % (path, k) if path else k)
        return ""
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return (" — length differs at %s: design has %d, ours has %d"
                    % (path or "(root)", len(a), len(b)))
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                return _first_diff_note(x, y, "%s[%d]" % (path, i))
        return ""
    return (" — at %s: design=%r vs ours=%r"
            % (path or "(root)", _shorten(a), _shorten(b)))


def _shorten(v):
    s = v if isinstance(v, str) else json.dumps(v)
    return s if len(s) <= 140 else s[:140] + "…"


def _json_normalize(v):
    """Round-trip through JSON so a Python tuple (`[('Ionic', '…'), …]` is
    how every `opts`/`matching.pairs`/`fifas` list is AUTHORED in
    all_subtopics_*.py) compares equal to the JSON array it is semantically
    identical to. Without this, `[('a', True)] == [['a', True]]` is FALSE in
    Python — tuple vs list — and every quiz/matching field in this diff
    reported DIFFERS for a reason that had nothing to do with content."""
    return json.loads(json.dumps(v, sort_keys=True))


def write_source_diff(per_slug):
    design = load_design_source_js()
    per_slug = {slug: _json_normalize(rec) for slug, rec in per_slug.items()}
    lines = [
        "# KS4 pilot — shared/ks4-source.js vs Design's ks4-source.js",
        "",
        "Generated by build_ks4.py's `write_source_diff()`. Byte equality is "
        "the expectation for every field except where a ruling documents a "
        "departure; a difference below is a FINDING for the inventory "
        "executor / examiners, not something this script papers over.",
        "",
    ]
    equal_count = diff_count = 0
    for lesson in ks4_lessons.LESSONS:
        slug = lesson["slug"]
        design_key = ks4_rulings.SLUG_MISMATCHES.get(slug, slug)
        d = design.get(design_key)
        ours = per_slug[slug]
        lines.append("## `%s` (Design's key: `%s`)" % (slug, design_key))
        if d is None:
            lines.append("- Design's ks4-source.js has no entry under this key. SKIPPED.")
            lines.append("")
            continue
        fields = sorted(set(list(d.keys()) + list(ours.keys()) + ["quiz"]))
        for f in fields:
            if f == "file":
                continue  # Design's authoring-markdown filename; we never had one
            if f == "quiz":
                for route in ROUTE_CODES:
                    dq = (d.get("quiz") or {}).get(route)
                    oq = (ours.get("quiz") or {}).get(route)
                    if dq is None and oq is None:
                        continue
                    if dq == oq:
                        lines.append("- quiz.%s: EQUAL (%d questions)" % (route, len(oq or [])))
                        equal_count += 1
                    else:
                        lines.append("- quiz.%s: DIFFERS%s" % (route, _first_diff_note(dq, oq)))
                        diff_count += 1
                continue
            dv, ov = d.get(f), ours.get(f)
            if dv == ov:
                if dv is not None:
                    lines.append("- %s: EQUAL" % f)
                    equal_count += 1
                continue
            lines.append("- %s: DIFFERS%s" % (f, _first_diff_note(dv, ov)))
            diff_count += 1
        lines.append("")
    lines.insert(4, "Summary: %d field/route comparisons EQUAL, %d DIFFER.\n"
                 % (equal_count, diff_count))
    os.makedirs(INVENTORY_DIR, exist_ok=True)
    out_path = os.path.join(INVENTORY_DIR, "source-diff.md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return out_path, equal_count, diff_count


# ═══════════════════════════════════════════════════════════════════════
# STEP B — the small shared assets: ks4-ds.css (generated), ks4-theme.css
# and ks4-diagrams.js (copied verbatim), ks4-lib.js (ported: R2's fig
# marker + the hrefFor/NAV addition).
# ═══════════════════════════════════════════════════════════════════════
_FONT_URL_RE = re.compile(r"url\('(?:\.\./fonts/|\./)?([A-Za-z0-9_-]+\.woff2)'\)")

_DS_CSS_HEADER = """/* shared/ks4-ds.css — GENERATED by build_ks4.py from Design's own
   delivered bundle (docs/ks4/design-reference/pilot/_ds/.../styles.css and
   its @import chain), concatenated in her own import order:
     tokens/src-styles-tokens.css, tokens/shared-tokens.css,
     tokens/shared-ks3.css, fonts/fonts.css, _ds_bundle.css

   WHY A NEW FILE rather than shared/tokens.css + shared/ks3.css (which the
   rest of the site already loads): neither is byte-identical to what
   Design's page was built against — shared/ks3.css alone is ~29,850
   lines against her 1,403 (the diff has real content on BOTH sides, not
   just a subset), and shared/tokens.css differs beyond its font paths.
   Loading the site's evolved stylesheets here would risk months of OTHER
   KS3 unit CSS cascading onto a page Design never tested against it. The
   contract's "the page wins" rule settles this: ship what she built
   against, verbatim, as one new asset. shared/fonts/*.woff2 IS reused
   as-is — confirmed byte-identical to the seven fonts this bundle needs.

   The ONLY bytes changed from Design's originals are the font url() paths,
   rewritten to /shared/fonts/X.woff2. Never hand-edit; re-run build_ks4.py. */

"""


def build_ds_css():
    parts = []
    for rel in ("tokens/src-styles-tokens.css", "tokens/shared-tokens.css",
                "tokens/shared-ks3.css", "fonts/fonts.css", "_ds_bundle.css"):
        parts.append(open(os.path.join(DS_DIR, rel), encoding="utf-8").read())
    body = "\n\n".join(parts)
    body = _FONT_URL_RE.sub(lambda m: "url('/shared/fonts/%s')" % m.group(1), body)
    return _DS_CSS_HEADER + body


def build_ks4_lib_js():
    text = open(os.path.join(DESIGN_DIR, "ks4-lib.js"), encoding="utf-8").read()
    text = ks4_rulings.apply_r2_ks4lib(text)

    nav = {L["slug"]: {"subject": L["subject"], "topic": L["topic_id"],
                        "routes": L["routes"]} for L in ks4_lessons.LESSONS}
    addition = (
        "\n  /* ⊕ ENGINE ADDITION — not in Design's delivery. Her page "
        "never needed a\n"
        "     real href (Route was a review selector, and her prev/next/"
        "connects\n"
        "     hrefs were sibling .dc.html filenames for local review). NAV "
        "is\n"
        "     generated from ks4_lessons.LESSONS by build_ks4.py. Falls back "
        "to\n"
        "     the Triple pathway at the same tier when the target does not "
        "ship\n"
        "     on the current pathway (nanoparticles is Triple-only — see\n"
        "     ks4_rulings.py R-CONNECTS). */\n"
        "  var NAV = %s;\n"
        "  function hrefFor(slug, R) {\n"
        "    var n = NAV[slug];\n"
        "    if (!n) { return '#'; }\n"
        "    var pathway = (R && R.isTriple) ? 'triple' : 'combined';\n"
        "    var tier = (R && R.isHigher) ? 'higher' : 'foundation';\n"
        "    var code = (pathway === 'triple' ? 'T' : 'C') + (tier === "
        "'higher' ? 'H' : 'F');\n"
        "    if (n.routes.indexOf(code) === -1) { pathway = 'triple'; }\n"
        "    return '/' + pathway + '/' + tier + '/' + n.subject + '/' + "
        "n.topic + '/' + slug + '.html';\n"
        "  }\n"
    ) % json.dumps(nav, sort_keys=True)

    marker = "  return { rail: rail,"
    if text.count(marker) != 1:
        raise SystemExit("build_ks4_lib_js: expected exactly one %r" % marker)
    idx = text.index(marker)
    text = text[:idx] + addition + text[idx:]

    tail_from = "commonMistake: commonMistake, cfifa: cfifa, fifas: fifas, load: load, save: save, hash: hash };"
    tail_to = "commonMistake: commonMistake, cfifa: cfifa, fifas: fifas, load: load, save: save, hash: hash, hrefFor: hrefFor };"
    if text.count(tail_from) != 1:
        raise SystemExit("build_ks4_lib_js: expected exactly one %r" % tail_from)
    text = text.replace(tail_from, tail_to, 1)
    return text


def build_shared_assets():
    written = {}
    for name, content in (
        ("ks4-ds.css", build_ds_css()),
        ("ks4-theme.css", open(os.path.join(DESIGN_DIR, "ks4-theme.css"), encoding="utf-8").read()),
        ("ks4-diagrams.js", open(os.path.join(DESIGN_DIR, "ks4-diagrams.js"), encoding="utf-8").read()),
        ("ks4-lib.js", build_ks4_lib_js()),
    ):
        path = _shared(name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        written[name] = path
    return written


# ═══════════════════════════════════════════════════════════════════════
# STEP C — shared/ks4-lesson.css: every per-page <style> block, deduplicated
# ═══════════════════════════════════════════════════════════════════════
_STYLE_RE = re.compile(r"<style>(.*?)</style>", re.S)


def collect_lesson_css(all_files):
    seen = set()
    chunks = []
    for fname in all_files:
        text = open(os.path.join(DESIGN_DIR, fname), encoding="utf-8").read()
        helmet_end = text.find("</helmet>")
        helmet = text[:helmet_end] if helmet_end != -1 else text
        for m in _STYLE_RE.finditer(helmet):
            block = m.group(1).strip()
            if not block or block in seen:
                continue
            seen.add(block)
            chunks.append("/* from %s */\n%s" % (fname, block))
    header = ("/* shared/ks4-lesson.css — GENERATED by build_ks4.py: every "
               "distinct <style> block found in the\n"
               "   <helmet> of the 14 lessons + 11 blocks, deduplicated "
               "(exact text match), first-seen order.\n"
               "   Never hand-edit; re-run build_ks4.py. */\n\n")
    return header + "\n\n".join(chunks) + "\n"


# ═══════════════════════════════════════════════════════════════════════
# STEP D — the browser-side template compiler (extends student_template.py's
# _COMPILE_JS with `dc-import` → `t: 'child'`).
# ═══════════════════════════════════════════════════════════════════════
_COMPILE_JS = r"""
(function (html) {
  var t = document.createElement('template');
  t.innerHTML = html;

  function interp(s) {
    if (s.indexOf('{{') === -1) { return s; }
    var parts = [], re = /\{\{\s*([^}]+?)\s*\}\}/g, last = 0, m;
    while ((m = re.exec(s)) !== null) {
      if (m.index > last) { parts.push(s.slice(last, m.index)); }
      parts.push({e: m[1]});
      last = m.index + m[0].length;
    }
    if (last < s.length) { parts.push(s.slice(last)); }
    return {parts: parts};
  }

  var n = 0;
  function walk(node) {
    if (node.nodeType === 3) {
      var v = node.nodeValue;
      if (!v.trim()) { return null; }
      return {t: '#', v: interp(v)};
    }
    if (node.nodeType !== 1) { return null; }

    var tag = node.tagName.toLowerCase();
    var idx = n++;

    if (tag === 'sc-if') {
      return {t: 'if', i: idx, e: (node.getAttribute('value') || '')
                .replace(/^\{\{\s*|\s*\}\}$/g, ''),
              c: kids(node)};
    }
    if (tag === 'sc-for') {
      return {t: 'for', i: idx,
              e: (node.getAttribute('list') || '')
                 .replace(/^\{\{\s*|\s*\}\}$/g, ''),
              as: node.getAttribute('as') || 'it', c: kids(node)};
    }
    if (tag === 'x-import') {
      return {t: 'import', i: idx,
              from: node.getAttribute('component-from-global-scope') || '',
              size: node.getAttribute('size') || ''};
    }
    if (tag === 'dc-import') {
      var comp = node.getAttribute('name') || '';
      var attrs = {};
      for (var k2 = 0; k2 < node.attributes.length; k2++) {
        var at2 = node.attributes[k2], name2 = at2.name, val2 = at2.value;
        if (name2 === 'name' || name2 === 'hint-placeholder-count' ||
            name2 === 'hint-placeholder-val' || name2 === 'hint-size' ||
            name2 === 'sc-name') { continue; }
        attrs[name2] = interp(val2);
      }
      return {t: 'child', i: idx, comp: comp, a: attrs};
    }

    var out = {t: tag, i: idx, a: {}, c: kids(node)};
    for (var k = 0; k < node.attributes.length; k++) {
      var at = node.attributes[k], name = at.name, val = at.value;
      if (name === 'hint-placeholder-count' || name === 'hint-placeholder-val' ||
          name === 'hint-size' || name === 'sc-name') { continue; }
      if (name === 'onclick') { out.on = val.replace(/^\{\{\s*|\s*\}\}$/g, ''); continue; }
      if (name === 'onchange' || name === 'oninput') {
        out.onch = val.replace(/^\{\{\s*|\s*\}\}$/g, ''); continue;
      }
      if (name === 'ref') { out.ref = val.replace(/^\{\{\s*|\s*\}\}$/g, ''); continue; }
      if (name === 'style-hover') { out.hov = val; continue; }
      out.a[name] = interp(val);
    }
    if (!Object.keys(out.a).length) { delete out.a; }
    if (!out.c.length) { delete out.c; }
    return out;
  }

  function kids(node) {
    var out = [];
    for (var i = 0; i < node.childNodes.length; i++) {
      var c = walk(node.childNodes[i]);
      if (c) { out.push(c); }
    }
    return out;
  }

  var roots = [];
  for (var i = 0; i < t.content.childNodes.length; i++) {
    var r = walk(t.content.childNodes[i]);
    if (r) { roots.push(r); }
  }
  return JSON.stringify({n: n, roots: roots});
})(%s)
"""


def template_and_logic(path):
    """Split a `.dc.html` into (template markup, logic-class source). Same
    slicing rule as student_template.py's — the template starts at
    `<helmet`, NOT after it, because `data-dc-tpl` numbering (and every
    node index this build relies on) is stamped from zero across the whole
    document, helmet included."""
    src = open(path, encoding="utf-8").read()
    a = src.index("<helmet")
    m = re.search(r'<script[^>]*data-dc-script[^>]*>', src)
    if not m:
        raise SystemExit("build_ks4: %s has no <script data-dc-script>" % path)
    tpl = src[a:m.start()]
    logic = src[m.end():]
    logic = logic[:logic.rindex("</script>")]
    return tpl.strip(), logic.strip()


def compile_template_text(page, tpl_text):
    got = json.loads(page.eval(_COMPILE_JS % json.dumps(tpl_text)))
    return {"n": got["n"], "roots": got["roots"]}


# ═══════════════════════════════════════════════════════════════════════
# STEP E — compile the 11 blocks
# ═══════════════════════════════════════════════════════════════════════
_BLOCK_R2 = {
    "Ks4Choice": ks4_rulings.apply_r2_choice,
    "Ks4Write": ks4_rulings.apply_r2_write,
    "Ks4Ladder": ks4_rulings.apply_r2_ladder,
}


def compile_block(page, name):
    path = os.path.join(DESIGN_DIR, name + ".dc.html")
    tpl, logic = template_and_logic(path)
    if name == "Ks4Chrome":
        tpl = ks4_rulings.apply_r_breadcrumb(tpl)
    if name in _BLOCK_R2:
        logic = _BLOCK_R2[name](logic)
    template = compile_template_text(page, tpl)
    return {"template": template, "logic": logic}


# ═══════════════════════════════════════════════════════════════════════
# STEP F — compile the 14 lessons
# ═══════════════════════════════════════════════════════════════════════
def compile_lesson(page, lesson, report):
    path = os.path.join(DESIGN_DIR, lesson["design_file"])
    tpl, logic = template_and_logic(path)

    # structural template edits BEFORE the browser compile — removing a node
    # renumbers everything after it (student_template.py's rule, carried
    # over unchanged: R1/R6/R7 all touch the template, so all three run here).
    tpl = ks4_rulings.apply_r1_route_selector(lesson["design_file"], tpl)
    tpl, r9_fired = ks4_rulings.apply_r9_badge_gate(lesson["slug"], tpl)
    ks4_rulings.check_r3_ready_unused(logic)
    draft_tip = None
    if lesson["slug"] == "nanoparticles":
        ks4_rulings.check_r5_nanoparticles_spec(tpl)
    if lesson["slug"] == "series-parallel-circuits":
        tpl = ks4_rulings.apply_r6_rtotal_chip(tpl)
        tpl, draft_tip = ks4_rulings.apply_r7_remove_draft_tip(lesson["design_file"], tpl)
    if lesson["slug"] == "resistors":
        tpl, draft_tip = ks4_rulings.apply_r7_remove_draft_tip(lesson["design_file"], tpl)
    if lesson["slug"] == "metals-alloys":
        logic = ks4_rulings.apply_r8_model_data(logic)

    logic, tpl, slug_renamed = ks4_rulings.apply_r_slug(lesson["slug"], logic, tpl)
    logic, n_prev, n_next = ks4_rulings.apply_r_prevnext(lesson["design_file"], logic)
    logic, connects_targets = ks4_rulings.apply_r_connects(lesson["design_file"], logic)

    template = compile_template_text(page, tpl)

    block_map = lesson.get("block_map", {})
    classified = classify_lesson_sections(template, lesson["slug"], block_map)

    report.append(dict(slug=lesson["slug"], slug_renamed=slug_renamed,
                        r9_fired=r9_fired,
                        has_prev=bool(n_prev), has_next=bool(n_next),
                        connects=connects_targets, draft_tip=draft_tip,
                        sections=classified))
    return {"template": template, "logic": logic, "draft_tip": draft_tip}


def classify_lesson_sections(template, slug, block_map):
    def find_lesson_div(nodes):
        for n in nodes:
            if n.get("t") == "div" and ks4_blocks._class_of(n) == "ks3-lesson":
                return n
            found = find_lesson_div(n.get("c") or [])
            if found is not None:
                return found
        return None

    lesson_div = find_lesson_div(template["roots"])
    if lesson_div is None:
        raise SystemExit("build_ks4: %s has no .ks3-lesson div to classify" % slug)
    out = []
    idx = 0
    for child in lesson_div.get("c") or []:
        a = child.get("a") or {}
        is_section = child.get("t") == "section" or "data-key-fact" in a
        if not is_section:
            continue
        ctype = ks4_blocks.classify_section(child, slug, idx, block_map)
        child.setdefault("a", {})["data-block"] = ctype
        out.append({"index": idx, "id": a.get("id", ""), "type": ctype})
        idx += 1
    return out


# ═══════════════════════════════════════════════════════════════════════
# STEP G — prev/next, computed exactly as generate_site_v5.make_pathway_
# subtopic_page does: index neighbours within the ROUTE'S OWN topic list.
# ═══════════════════════════════════════════════════════════════════════
def compute_prev_next(data, lesson, route):
    subject, topic, slug = lesson["subject"], lesson["topic_id"], lesson["slug"]
    lst = data[subject][route].get(topic, [])
    ids = [s["id"] for s in lst]
    if slug not in ids:
        return None, None
    i = ids.index(slug)
    pathway, tier = ROUTE_URL[route]

    def entry(idx):
        if idx < 0 or idx >= len(lst):
            return None
        s = lst[idx]
        return {"href": "/%s/%s/%s/%s/%s.html" % (pathway, tier, subject, topic, s["id"]),
                "label": s["title"]}
    return entry(i - 1), entry(i + 1)


# ═══════════════════════════════════════════════════════════════════════
# STEP H — the rung-1 fallback check (examiner finding, 25 Sep 2026).
# Static analysis only — never changes KS4.find()'s runtime behaviour.
# ═══════════════════════════════════════════════════════════════════════
_FIND_RE = re.compile(r"K\.find\(slug,\s*R\.route,\s*'((?:[^'\\]|\\.)*)'\)")
_JS_UNICODE_RE = re.compile(r"\\u([0-9a-fA-F]{4})")
# ⚠️ SCOPED TO THE r1: LINE, not every K.find in the file. states-of-matter
# has a SECOND, unrelated K.find at its `lim = …` line (feeding an
# isHigher-only widget, not rung 1) — an unscoped regex mislabelled that as
# a "rung1-fallback" in the first version of this check. All 14 lessons
# write `r1: Object.assign(K.find(...) [|| K.find(...)] || {...}, {...}),`
# immediately followed by `r2:` (verified across all 14 by grep before this
# was written), so the text between those two literal keys is exactly
# rung 1's needle(s) and nothing else.
_R1_BLOCK_RE = re.compile(r"r1:\s*(.*?),\s*r2:", re.S)


def _decode_js_string(s):
    s = _JS_UNICODE_RE.sub(lambda m: chr(int(m.group(1), 16)), s)
    return s.replace("\\'", "'")


def extract_rung1_needles(raw_logic_text):
    """Rung 1's needle(s), in the order `K.find(...) || K.find(...)` tries
    them, as WRITTEN in Design's original (pre-ruling) logic text."""
    m = _R1_BLOCK_RE.search(raw_logic_text)
    if not m:
        raise SystemExit(
            "build_ks4.extract_rung1_needles: no `r1: … , r2:` block found "
            "— Design's ladder-rung shape moved; this check needs "
            "re-scoping, not silently returning nothing.")
    return [_decode_js_string(x) for x in _FIND_RE.findall(m.group(1))]


def check_rung1_fallback(data, lesson, needles):
    """For every route this lesson ships on: does the FIRST needle that
    resolves (own-route copy, else TH copy, in K.find's own order) come
    from the route's OWN quiz, or did it fall back to TH? Prints one
    WARNING line per fallback and one per total miss. Returns the count."""
    if not needles:
        return 0
    warnings = 0
    subject, topic, slug = lesson["subject"], lesson["topic_id"], lesson["slug"]
    for route in lesson["routes"]:
        st = find_subtopic(data, subject, route, topic, slug)
        own_qs = [q["q"] for q in (st["quiz"] if st else [])]
        th = find_subtopic(data, subject, "TH", topic, slug)
        th_qs = [q["q"] for q in (th["quiz"] if th else [])]
        resolved = False
        for needle in needles:
            if any(needle in q for q in own_qs):
                resolved = True
                break
            if any(needle in q for q in th_qs):
                print("  WARNING rung1-fallback %s %s needle=%r"
                      % (slug, route, needle))
                warnings += 1
                resolved = True
                break
        if not resolved:
            print("  WARNING rung1-nomatch %s %s — no needle in %r matched "
                  "own-route or TH copy; rung 1 would render with no options"
                  % (slug, route, needles))
            warnings += 1
    return warnings


# ═══════════════════════════════════════════════════════════════════════
# STEP I — page assembly
# ═══════════════════════════════════════════════════════════════════════
def block_registration_scripts(compiled_blocks):
    out = []
    for name in BLOCK_NAMES:
        b = compiled_blocks[name]
        out.append(
            "<script>\nwindow.KS4_BLOCKS = window.KS4_BLOCKS || {};\n"
            "(function () {\n%s\n"
            "window.KS4_BLOCKS[%s] = {Component: Component, template: %s};\n"
            "})();\n</script>"
            % (b["logic"], json.dumps(name), json.dumps(b["template"])))
    return "\n".join(out)


def lesson_mount_script(compiled_lesson, route, lesson, prev_next, subject_label):
    prev, nxt = prev_next
    props = {
        "route": ROUTE_LABEL[route],
        "theme": "auto",
        "showDraft": lesson["review_state"] == "draft",
        "mrbPrevNext": {"prev": prev, "next": nxt},
    }
    return (
        "<script>\n(function () {\n%s\n"
        "window.MrBadmusKS4Runtime.mount({\n"
        "  into: '#ks4-mount', Component: Component,\n"
        "  props: %s,\n"
        "  template: %s\n"
        "});\n})();\n</script>"
        % (compiled_lesson["logic"], json.dumps(props, sort_keys=True),
           json.dumps(compiled_lesson["template"])))


TUTOR_OVERLAY = None  # filled from build_ks3.KS3_CHAT_OVERLAY in main()


def tutor_block(lesson, route):
    """The tutor overlay, wired like build_ks3.py's `tutor_mount()` — same
    markup, same MrBadmus.init() call shape, same deferred-script /
    DOMContentLoaded ordering. Differs only in the config: KS4 pages never
    pass `keyStage`, matching every OLD KS4 lesson page's own
    `MrBadmus.init({subject, topic})` call (mrbadmus.v2.js reads tier/
    pathway from the STUDENT'S OWN profile for any non-KS3 page, and takes
    no tier/pathway override in its config at all — contract's "supply
    tier/pathway from the route" is honoured by folding the route into
    `topic`, so the tutor has that context even for a student whose own
    profile tier differs from the page they are revising on)."""
    topic = "%s (AQA %s) — %s" % (lesson["title"], lesson["spec"], ROUTE_LABEL[route])
    cfg = json.dumps({"subject": lesson["subject"], "topic": topic}, sort_keys=True)
    cfg = cfg.replace("<", "\\u003c")
    return (TUTOR_OVERLAY +
            '<script src="/shared/mrbadmus.v2.js" defer fetchpriority="low"></script>\n'
            '<script>document.addEventListener("DOMContentLoaded",'
            'function(){if(window.MrBadmus){MrBadmus.init(%s);}});</script>\n' % cfg)


def render_page(lesson, route, compiled_lesson, block_scripts, prev_next, versions):
    url = ks4_lessons.site_url(lesson["slug"], route)
    subject_label = lesson["subject"].capitalize()
    title = "%s · MrBadmusAI GCSE %s" % (lesson["title"], subject_label)
    mount_script = lesson_mount_script(compiled_lesson, route, lesson, prev_next, subject_label)
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<link rel="canonical" href="https://mrbadmus.com%(url)s">
<link rel="stylesheet" href="/shared/ks4-ds.css">
<link rel="stylesheet" href="/shared/ks4-theme.css">
<link rel="stylesheet" href="/shared/ks4-lesson.css">
<style>html,body{margin:0;padding:0;background:#FBF3E6;}</style>
</head>
<body>
<div id="ks4-mount"></div>
<script src="/shared/ks4-source.js"></script>
<script src="/shared/ks4-lib.js"></script>
<script src="/shared/ks4-diagrams.js"></script>
<script src="/shared/ks4-runtime.js"></script>
%(block_scripts)s
%(mount_script)s
%(tutor)s
</body>
</html>
""" % dict(title=title, url=url, block_scripts=block_scripts, mount_script=mount_script,
           tutor=tutor_block(lesson, route))
    import build_ks3
    return build_ks3.stamp_versions(html, versions)


# ═══════════════════════════════════════════════════════════════════════
# STEP J — prerender in headless Chrome: bake the mounted DOM's static text
# into the page, assert zero console errors at 1280 and 360.
# ═══════════════════════════════════════════════════════════════════════
# ⊕ MRB-267 precedent (ks3_smoke.py, ks3_parity.py): `shared/mrbadmus.v2.js`
# pings mrbadmus-backend.onrender.com/api/health on every page load to keep
# Render warm. It is `.catch()`-ed in JS, but Chrome logs the network/CORS
# failure to the console regardless — from a 127.0.0.1 test origin it always
# fails CORS, so this is a property of testing from localhost, not a defect
# in the page. Demoted here exactly as it is in the two gates above.
BACKEND_HOST = "mrbadmus-backend.onrender.com"


def _real_errors(errs):
    return [e for e in errs if "favicon.ico" not in e and BACKEND_HOST not in e]


def prerender_all(cdp, pages):
    """`pages`: [(out_path, url_path)]. Bakes #ks4-mount's innerHTML into
    each file and returns [(url_path, errors_1280, errors_360)]."""
    server, port = cdp.serve(OUT_ROOT)
    results = []
    try:
        with cdp.Browser() as b:
            page = b.attach()
            for out_path, url_path in pages:
                page.set_viewport(1280, 1000)
                page.goto("http://127.0.0.1:%d%s" % (port, url_path))
                # the mount script is a plain synchronous <script>, run by
                # the time `load` fires; poll briefly for belt and braces.
                baked = None
                for _ in range(40):
                    try:
                        renders = page.eval(
                            "document.querySelector('#ks4-mount').getAttribute('data-mrb-renders')")
                    except Exception:
                        renders = None
                    if renders:
                        baked = page.eval("document.querySelector('#ks4-mount').innerHTML")
                        break
                    time.sleep(0.1)
                errors_1280 = _real_errors(page.console_errors())
                page.set_viewport(360, 900)
                time.sleep(0.15)
                errors_360 = _real_errors(page.console_errors())
                results.append((url_path, errors_1280, errors_360))
                if baked is not None:
                    full = open(out_path, encoding="utf-8").read()
                    full = full.replace('<div id="ks4-mount"></div>',
                                         '<div id="ks4-mount">%s</div>' % baked, 1)
                    with open(out_path, "w", encoding="utf-8") as fh:
                        fh.write(full)
    finally:
        server.shutdown()
    return results


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════
def main():
    os.chdir(REPO_ROOT)
    sys.path.insert(0, REPO_ROOT)
    import ks3_browser as cdp
    import build_ks3

    global TUTOR_OVERLAY
    TUTOR_OVERLAY = build_ks3.KS3_CHAT_OVERLAY

    print("\n\U0001f9f1  build_ks4 — the KS4 pilot (14 lessons, 54 pages)\n")

    ks4_lessons.verify_slugs()
    print("  ✓ all 14 slugs verified against all_subtopics_*.py")

    data = load_subtopics_by_route()
    source_js, per_slug = build_source_js(data)
    with open(_shared("ks4-source.js"), "w", encoding="utf-8") as fh:
        fh.write(source_js)
    diff_path, n_eq, n_diff = write_source_diff(per_slug)
    print("  ✓ shared/ks4-source.js written; diff vs Design's own: "
          "%d EQUAL, %d DIFFER (%s)" % (n_eq, n_diff, diff_path))

    build_shared_assets()
    print("  ✓ shared/ks4-ds.css, ks4-theme.css, ks4-diagrams.js, ks4-lib.js written")

    all_files = [L["design_file"] for L in ks4_lessons.LESSONS] + \
        [n + ".dc.html" for n in BLOCK_NAMES]
    lesson_css = collect_lesson_css(all_files)
    with open(_shared("ks4-lesson.css"), "w", encoding="utf-8") as fh:
        fh.write(lesson_css)
    print("  ✓ shared/ks4-lesson.css written (%d bytes)" % len(lesson_css))

    # ks4-runtime.js is hand-written engine code (not regenerated here); just
    # confirm it exists before anything tries to load it.
    if not os.path.exists(_shared("ks4-runtime.js")):
        raise SystemExit("build_ks4: shared/ks4-runtime.js is missing")

    import shutil
    dst_shared = os.path.join(OUT_ROOT, "shared")
    os.makedirs(dst_shared, exist_ok=True)
    for name in KS4_OWN_ASSETS:
        src = _shared(name)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dst_shared, name))
    print("  ✓ synced %d shared asset(s) into %s (Cloudflare serves "
          "from there, not the repo root)" % (len(KS4_OWN_ASSETS), dst_shared))

    stub_dir = os.path.join(REPO_ROOT, ".ks4_compile_stub")
    os.makedirs(stub_dir, exist_ok=True)
    with open(os.path.join(stub_dir, "stub.html"), "w", encoding="utf-8") as fh:
        fh.write("<!doctype html><html><body></body></html>")

    compiled_blocks = {}
    lesson_report = []
    compiled_lessons = {}
    stub_server, stub_port = cdp.serve(stub_dir)
    try:
        with cdp.Browser() as b:
            page = b.attach()
            page.goto("http://127.0.0.1:%d/stub.html" % stub_port)
            for name in BLOCK_NAMES:
                compiled_blocks[name] = compile_block(page, name)
            print("  ✓ %d shared blocks compiled" % len(compiled_blocks))

            for lesson in ks4_lessons.LESSONS:
                compiled_lessons[lesson["slug"]] = compile_lesson(page, lesson, lesson_report)
    finally:
        stub_server.shutdown()
    print("  ✓ %d lessons compiled" % len(compiled_lessons))

    for row in lesson_report:
        if row["slug_renamed"]:
            print("     R-SLUG fired: %s" % row["slug"])
        if row["r9_fired"]:
            print("     R9 fired: %s" % row["slug"])

    # ── rung-1 fallback check (examiner finding) ───────────────────────
    fallback_warnings = 0
    for lesson in ks4_lessons.LESSONS:
        raw_tpl, raw_logic = template_and_logic(
            os.path.join(DESIGN_DIR, lesson["design_file"]))
        needles = extract_rung1_needles(raw_logic)
        fallback_warnings += check_rung1_fallback(data, lesson, needles)
    print("  ✓ rung-1 fallback check: %d warning(s) printed above" % fallback_warnings)

    # ── draft exam tips, preserved verbatim ────────────────────────────
    draft_tips = []
    for lesson in ks4_lessons.LESSONS:
        tip = compiled_lessons[lesson["slug"]]["draft_tip"]
        if tip:
            draft_tips.append((lesson["slug"], lesson["title"], tip))
    os.makedirs(INVENTORY_DIR, exist_ok=True)
    with open(os.path.join(INVENTORY_DIR, "draft-exam-tips.md"), "w", encoding="utf-8") as fh:
        fh.write("# Draft examiner tips removed by R7 (not yet approved)\n\n"
                  "Verbatim, for Mide/the examiners to approve or replace. "
                  "Removed from the live page — no draft chip may reach a "
                  "student (pilot-build-contract.md R7).\n\n")
        for slug, title, tip in draft_tips:
            fh.write("## %s (%s)\n\n%s\n\n" % (title, slug, tip))
    print("  ✓ %d draft exam tip(s) preserved in docs/ks4/pilot-inventory/draft-exam-tips.md"
          % len(draft_tips))

    # ── cache-bust: hash our own new assets ────────────────────────────
    versions = {}
    for name in KS4_VERSIONED:
        path = _shared(name)
        if os.path.exists(path):
            with open(path, "rb") as fh:
                versions[name] = hashlib.md5(fh.read()).hexdigest()[:8]
    print("  ✓ %d shared asset(s) versioned" % len(versions))

    # ── emit the 54 pages ───────────────────────────────────────────────
    block_scripts = block_registration_scripts(compiled_blocks)
    written_pages = []
    for lesson in ks4_lessons.LESSONS:
        compiled_lesson = compiled_lessons[lesson["slug"]]
        for route in lesson["routes"]:
            prev_next = compute_prev_next(data, lesson, route)
            html = render_page(lesson, route, compiled_lesson, block_scripts,
                                prev_next, versions)
            url = ks4_lessons.site_url(lesson["slug"], route)
            out_path = os.path.join(OUT_ROOT, url.lstrip("/"))
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(html)
            written_pages.append((out_path, url))
    print("  ✓ %d pages written" % len(written_pages))

    # ── prerender + console-error gate ──────────────────────────────────
    results = prerender_all(cdp, written_pages)
    total_errors = 0
    for url, e1280, e360 in results:
        if e1280 or e360:
            total_errors += len(e1280) + len(e360)
            print("  ✗ console errors on %s" % url)
            for e in e1280:
                print("      [1280] %s" % e)
            for e in e360:
                print("      [360]  %s" % e)
    if total_errors:
        raise SystemExit("build_ks4: %d console error(s) across the 54 pages "
                          "— a build failure (see above)." % total_errors)
    print("  ✓ zero console errors across %d pages at 1280 and 360px" % len(results))

    # ── root-level mirror ────────────────────────────────────────────────
    # ⚠️ `generate_site_v5.py`'s own "Copy to repo root" step rmtree's and
    # copytree's the WHOLE `combined/`/`triple/` top-level dirs from
    # `mrbadmus_site/` back to the repo root — but it does that BEFORE this
    # script runs (build_all.py's step order), so by the time build_ks4.py
    # has overwritten these 54 pages under mrbadmus_site/, the root mirror
    # still holds the OLD design. `git ls-files combined/` proves the repo
    # DOES track this mirror (424 files), so it has to be kept in step.
    # Mirrors ONLY the 54 files this script itself wrote — never a wholesale
    # rmtree+copytree of the whole tree, which would needlessly re-touch the
    # other ~250 untouched KS4 pages living in the same directories (the
    # bytes would end up identical either way, since nothing else in this
    # run wrote them, but touching 250 files this run has no business
    # touching is exactly the kind of scope creep the hard line — "the
    # other 250 KS4 lesson pages do not change by a byte" — exists to catch).
    for out_path, _url in written_pages:
        root_path = out_path[len(OUT_ROOT):].lstrip(os.sep)
        os.makedirs(os.path.dirname(root_path), exist_ok=True)
        import shutil as _shutil
        _shutil.copy2(out_path, root_path)
    print("  ✓ mirrored %d page(s) to the repo-root combined/triple/ "
          "trees" % len(written_pages))

    # ── manifest ─────────────────────────────────────────────────────────
    manifest = {"pages": {}, "assets": {}}
    for out_path, url in written_pages:
        with open(out_path, "rb") as fh:
            manifest["pages"][out_path.replace(os.sep, "/")] = hashlib.sha256(fh.read()).hexdigest()
    for name in KS4_VERSIONED:
        path = _shared(name)
        if os.path.exists(path):
            with open(path, "rb") as fh:
                manifest["assets"][path.replace(os.sep, "/")] = hashlib.sha256(fh.read()).hexdigest()
    with open(MANIFEST_PATH, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print("  ✓ %s written (%d pages, %d assets)"
          % (MANIFEST_PATH, len(manifest["pages"]), len(manifest["assets"])))

    import shutil
    shutil.rmtree(stub_dir, ignore_errors=True)

    print("\n✅ build_ks4 complete — %d pages, %d fallback warning(s).\n"
          % (len(written_pages), fallback_warnings))
    return 0


if __name__ == "__main__":
    sys.exit(main())
