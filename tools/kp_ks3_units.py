#!/usr/bin/env python3
"""kp_ks3_units.py — read the KS3 lesson pages the way the answer tap does.

`shared/mrbadmus.v2.js` sends one answer per QUESTION UNIT of a question-
shaped KS3 instrument (adapters A and B5C), with the id
`<slug>#<activity>-<n>`, the option text the child pressed (`optLabel`), and
— where the markup says which option is right — the right option's text.
This module runs the SAME rules over the built page HTML (no browser), so the
knowledge-point tagger can (a) give each unit a stem and its options and
(b) record the answer key exactly as the page renders it.

    units(slug) -> [{id, kind, activity, n, prompt, options: [text], key: text|None,
                     key_from: 'data-correct'|'want'|'is'|'data-answer'|'b5c'|None}]

Also: `ks3_page_options(slug)` — the rendered option texts of the lesson's
ladder MCQ rungs, Start here guess and keyed commits, by id.

The adapter rules, verbatim from mrbadmus.v2.js (round 4):
  * option = a <button> with `data-<p>-opt|pick|gopt|verdict|judge`, or class
    `ks3-option`;
  * unit = nearest ancestor (inside the block) with `data-<p>-card|item|side|
    row|case|cell|q|sample|scenario|panel|seg|test`, else the button's
    `data-<p>-of`, else the `<unit>:` prefix of its value, else the block;
  * n = the unit's order among the block's units, first seen in document order;
  * key = `data-correct` on an option; else `data-<p>-want-<unit>` on the
    block; else `data-<p>-is` in the unit; else `data-answer` on the
    button's row. (The page's last fallback — the is-correct class it sets
    after a click — does not exist in static HTML.)
"""

import os
import re
import sys

from bs4 import BeautifulSoup

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KIND_A = set("""ks3-cellbench-block ks3-removal-block ks3-sc-block ks3-meters-block ks3-clinic-block
ks3-bottle-block ks3-grain-block ks3-gapfill-block ks3-rgrid-block ks3-dcomp-block ks3-rword-block
ks3-iboard-block ks3-fault-block ks3-board ks3-cpair-block ks3-pdeck-block ks3-psort-block
ks3-tbench-block ks3-ml-block ks3-fb-block ks3-esort-block ks3-seq-block ks3-rockb-block ks3-prop-block
ks3-ctube-block ks3-touch-block ks3-pcards-block ks3-ruse-block ks3-tsort-block ks3-pass-block
ks3-spath-block ks3-plan-block ks3-sort ks3-switch-block ks3-mb-block ks3-solid-block ks3-chain-block
ks3-arr-block ks3-eqr-block ks3-rplan-block ks3-raudit-block ks3-mchoice-block ks3-cev-block
ks3-hgrid-block ks3-rstop-block ks3-gplot-block ks3-spair-block ks3-rtotal-block ks3-wsort-block
ks3-eyecam-block ks3-cplot-block ks3-chpair-block ks3-vchain-block ks3-sab-block ks3-cl-block
ks3-vp-block ks3-tb-block ks3-rd-block ks3-ajudge-block ks3-namer-block ks3-dish-block ks3-claim-block
ks3-euse-block ks3-critique-block ks3-edep-block ks3-fcard-block ks3-tuber-block ks3-mplace-block
ks3-hrig-block""".split())
KIND_B5C = {"ks3-xpanel-block", "ks3-fjobs-block", "ks3-dsort-block", "ks3-xbench-block", "ks3-jmatch-block"}
OPT_RE = re.compile(r"^data-([a-z0-9]+)-(opt|pick|gopt|verdict|judge)$")
UNIT_RE = re.compile(r"^data-[a-z0-9]+-(card|item|side|row|case|cell|q|sample|scenario|panel|seg|test)$")


def txt(el):
    return re.sub(r"\s+", " ", el.get_text() if el is not None else "").strip()


def opt_label(b):
    lab = b.select_one(".ks3-opt-label")
    return txt(lab if lab is not None else b)


def opt_attr(b):
    for k, v in b.attrs.items():
        m = OPT_RE.match(k)
        if m:
            return m.group(1), v if isinstance(v, str) else " ".join(v)
    return None


def is_option(b):
    return opt_attr(b) is not None or "ks3-option" in (b.get("class") or [])


def unit_of(b, sec):
    el = b.parent
    while el is not None and el is not sec:
        for k, v in (el.attrs or {}).items():
            if UNIT_RE.match(k):
                return el, "%s=%s" % (k, v if isinstance(v, str) else " ".join(v))
        el = el.parent
    oa = opt_attr(b)
    if oa:
        of = b.get("data-%s-of" % oa[0])
        if of:
            return None, "of=" + of
        if ":" in oa[1] and oa[1].index(":") > 0:
            return None, "v=" + oa[1].split(":")[0]
    return sec, "block"


def value_of(b):
    oa = opt_attr(b)
    x = oa[1] if oa else (b.get("data-i") or "")
    return x.split(":", 1)[1] if ":" in x and x.index(":") > 0 else x


def page_path(slug):
    """The built lesson page: ks3/<subject>/<unit-slug>/<lesson-slug>.html."""
    for subject in ("biology", "chemistry", "physics"):
        base = os.path.join(REPO, "ks3", subject)
        if not os.path.isdir(base):
            continue
        for unit in sorted(os.listdir(base)):
            p = os.path.join(base, unit, slug + ".html")
            if os.path.isfile(p):
                return p
    return None


_SOUP = {}


def soup(slug):
    if slug not in _SOUP:
        p = page_path(slug)
        _SOUP[slug] = BeautifulSoup(open(p, encoding="utf-8").read(), "lxml") if p else None
    return _SOUP[slug]


def _kind(sec, kinds):
    for c in sec.get("class") or []:
        if c in kinds:
            return c
    return None


def _prompt(scope, sec):
    if scope is not sec and scope is not None:
        parts = []
        for el in scope.find_all(["p", "h2", "h3", "h4", "li"]):
            if el.find_parent("button") or el.has_attr("data-count") or el.find_parent(attrs={"hidden": True}):
                continue
            t = txt(el)
            if t and t not in parts:
                parts.append(t)
        if parts:
            return " ".join(parts)
        return txt(scope)[:300]
    c = sec.select_one(".ks3-commit")
    if c is not None:
        return txt(c)
    h = sec.find(["h2", "h3", "h4"])
    return txt(h)


def units(slug):
    s = soup(slug)
    if s is None:
        return []
    out = []
    for sec in s.select("[data-instrument]"):
        if sec.has_attr("data-keyedblock"):
            continue
        act = sec.get("data-activity") or "block"
        kind = _kind(sec, KIND_B5C)
        if kind:
            tabs = sec.select("[data-b5c-pick]")
            for n, t in enumerate(tabs, 1):
                item = t.get("data-b5c-pick")
                w = t.find_parent(attrs={"data-b5c": True}) or sec
                opts = w.select('.ks3-b5c-opt[data-owner="%s"]' % item)
                rev = w.select_one('[data-b5c-reveal="%s"]' % item)
                right = rev.get("data-answer") if rev is not None else None
                good = None
                if right is not None:
                    good = w.select_one('.ks3-b5c-opt[data-owner="%s"][data-opt="%s"]' % (item, right))
                name = w.select_one('.ks3-b5c-item[data-for="%s"] .ks3-b5c-name' % item)
                ask = w.select_one(".ks3-b5c-ask")
                out.append({"id": "%s#%s-%d" % (slug, act, n), "kind": kind, "activity": act, "n": n,
                            "prompt": ((txt(name) + " — ") if txt(name) else "") + txt(ask),
                            "options": [opt_label(o) for o in opts],
                            "key": opt_label(good) if good is not None else None,
                            "key_from": "b5c" if good is not None else None})
            continue
        kind = _kind(sec, KIND_A)
        if not kind:
            continue
        buttons = [b for b in sec.find_all("button") if is_option(b) and not b.find_parent(class_="ks3-ladder")]
        order, groups = [], {}
        for b in buttons:
            el, key = unit_of(b, sec)
            if key not in groups:
                groups[key] = (el, [])
                order.append(key)
            groups[key][1].append(b)
        for n, key in enumerate(order, 1):
            el, bs = groups[key]
            first = bs[0]
            scope = el if el is not None else (first.parent.parent if first.parent is not None and first.parent.parent is not None else sec)
            if scope is not sec and sec not in scope.parents:
                scope = sec
            opts = [b for b in scope.find_all("button") if is_option(b)] if scope is not None else bs
            good, how = None, None
            dc = [b for b in opts if b.has_attr("data-correct")]
            if dc:
                g = [b for b in opts if (b.get("data-correct") or "") not in ("", "0", "false")]
                if g:
                    good, how = g[-1], "data-correct"
            oa = opt_attr(first)
            if good is None and oa and ":" in oa[1] and oa[1].index(":") > 0:
                uk = oa[1].split(":")[0]
                w = sec.find(attrs={"data-%s-want-%s" % (oa[0], uk): True})
                if w is not None:
                    want = w.get("data-%s-want-%s" % (oa[0], uk))
                    good = next((b for b in opts if value_of(b) == want), None)
                    how = "want"
            if good is None and oa and scope is not None:
                isel = scope.find(attrs={"data-%s-is" % oa[0]: True})
                if isel is not None:
                    want = isel.get("data-%s-is" % oa[0])
                    good = next((b for b in opts if value_of(b) == want), None)
                    how = "is"
            if good is None:
                row = first.find_parent(attrs={"data-answer": True})
                if row is not None and (row is sec or sec in row.parents):
                    want = row.get("data-answer")
                    good = next((b for b in opts if value_of(b) == want), None)
                    how = "data-answer"
            out.append({"id": "%s#%s-%d" % (slug, act, n), "kind": kind, "activity": act, "n": n,
                        "prompt": _prompt(scope, sec),
                        "options": [opt_label(b) for b in opts],
                        "values": [value_of(b) for b in opts],
                        "key": opt_label(good) if good is not None else None,
                        "key_from": how if good is not None else None})
    return out


def page_choice_keys(slug):
    """{qid: {"options": [text], "key": text|None}} for the lesson's ladder MCQ
    rungs (`<slug>#recall|apply`; the right option carries data-correct="1",
    text = `.ks3-opt-label` trimmed, as ks3.js answerParts sends it), the
    Start here guess (`<slug>#start`; right = the option whose reply begins
    "Good guess", as mrbadmus.v2.js reads it) and keyed commits
    (`<slug>#<activity>`; options only — the key comes from answer_index)."""
    s = soup(slug)
    out = {}
    if s is None:
        return out
    for rung in ("recall", "apply"):
        box = s.select_one('.ks3-ladder [data-rung="%s"]' % rung)
        if box is None:
            continue
        bs = [b for b in box.find_all("button") if "ks3-option" in (b.get("class") or [])]
        # fix 2 (display-only): a shortened label still SENDS its stored text,
        # carried on data-full (ks3.js answerParts reads it), so the key is that.
        lab = lambda b: (b.get("data-full") if b.has_attr("data-full") else (b.select_one(".ks3-opt-label") or b).get_text()).strip()
        good = [b for b in bs if (b.get("data-correct") or "") not in ("", "0", "false")]
        out["%s#%s" % (slug, rung)] = {"options": [lab(b) for b in bs],
                                         "key": lab(good[0]) if len(good) == 1 else None}
    for sec in s.select("[data-keyedblock]"):
        act = sec.get("data-activity") or ""
        keyed = sec.select_one("[data-keyed]")
        if keyed is None:
            continue
        opts = keyed.select(".ks3-option")
        if act == "hook":
            good = None
            for o in opts:
                rep = keyed.select_one('.ks3-keyed-reply[data-reply="%s"] strong' % o.get("data-i"))
                if rep is not None and txt(rep).startswith("Good guess"):
                    good = o
            out["%s#start" % slug] = {"options": [opt_label(o) for o in opts],
                                      "key": opt_label(good) if good is not None else None}
        else:
            out["%s#%s" % (slug, act)] = {"options": [opt_label(o) for o in opts],
                                          "by_i": {o.get("data-i"): opt_label(o) for o in opts},
                                          "key": None}
    return out


# ── the answer key from the AUTHORED data, for units whose markup does not
#    carry one. One rule per kind, each reading a field that names the right
#    option; anything not covered stays NULL (and is reported).

def _find_activity(lesson, aid):
    def walk(o):
        if isinstance(o, dict):
            if o.get("id") == aid and ("kind" in o or "type" in o):
                return o
            for v in o.values():
                r = walk(v)
                if r is not None:
                    return r
        elif isinstance(o, list):
            for v in o:
                r = walk(v)
                if r is not None:
                    return r
        return None
    return walk({"a": lesson.get("activities"), "c": lesson.get("core")})


def _prefix_label(prose, labels):
    """The ONE option label the authored answer prose opens with, or None.
    ("A violent reaction, and worse…" opens with "A violent reaction".)"""
    p = re.sub(r"\s+", " ", str(prose or "")).strip().lower()
    hits = [l for l in labels if l and (p == l.lower() or re.match(re.escape(l.lower()) + r"(?=[\s.,;:—–-]|$)", p))]
    return hits[0] if len(hits) == 1 else None


# kind → (authored list field, unit offset, rule)
#   rule "value:<field>"  the item's field is the option's value (data-*-opt)
#   rule "index:<field>"  the item's field is the option's index
#   rule "bool:<field>:<value if true>:<value if false>"
#   rule "prose:<field>"  the item's answer prose opens with one option label
#   rule "topid:<field>"  the item's field is an id in the activity's top-level
#                         `options`, whose position is the option's value
AUTHORED_RULES = {
    "ks3-ajudge-block": ("items", 0, "value:answer"),
    "ks3-bottle-block": ("bottles", 0, "value:answer"),
    "ks3-solid-block": ("solids", 0, "value:answer"),
    "ks3-euse-block": ("uses", 0, "value:correct"),
    "ks3-ruse-block": ("uses", 0, "value:correct"),
    "ks3-esort-block": ("items", 0, "bool:endo:endo:exo"),
    "ks3-dcomp-block": ("items", 0, "bool:yes:0:1"),
    "ks3-prop-block": ("samples", 0, "value:answer"),
    "ks3-ctube-block": ("tubes", 0, "bool:rust:rust:no"),
    "ks3-rstop-block": ("methods", 0, "bool:barrier:barrier:other"),
    "ks3-rockb-block": ("samples", 0, "value:answer"),
    "ks3-fcard-block": ("fuels", 0, "value:answer"),
    "ks3-eqr-block": ("readings", 0, "index:answer"),
    "ks3-tsort-block": ("reactions", 0, "topid:type"),
    "ks3-sc-block": ("cases", 1, "value:answer"),
    "ks3-pcards-block": ("items", 0, "prose:answer"),
    "ks3-gapfill-block": ("predictions", 0, "prose:answer"),
    "ks3-edep-block": ("entries", 0, "prose:answer"),
    "ks3-cev-block": ("entries", 0, "prose:answer"),
    "ks3-psort-block": ("samples", 0, "prose:verdict"),
    "ks3-cpair-block": ("pairs.sides", 0, "bool:chemical:1:0"),
}


def authored_key(lesson, unit):
    """(key text, how) for one unit from the authored data, or (None, reason)."""
    a = _find_activity(lesson, unit["activity"])
    if a is None:
        return None, "authored activity not found"
    rule = AUTHORED_RULES.get(unit["kind"])
    if rule is None:
        if unit["n"] == 1 and isinstance(a.get("answer_index"), int) and a.get("options"):
            vals = unit.get("values") or []
            v = str(a["answer_index"])
            if v in vals:
                return unit["options"][vals.index(v)], "authored answer_index"
        return None, "no single authored right option for this unit"
    field, offset, how = rule
    if "." in field:
        outer, inner = field.split(".")
        items = [x for o in a.get(outer) or [] for x in o.get(inner) or []]
    else:
        items = a.get(field) or []
    i = unit["n"] - 1 - offset
    if i < 0:
        return None, "this unit picks which case to look at; it is not itself a question"
    if i >= len(items):
        return None, "unit has no authored item"
    item = items[i]
    vals, labels = unit.get("values") or [], unit["options"]
    kind, _, rest = how.partition(":")
    want = None
    if kind == "value":
        want = item.get(rest)
    elif kind == "index":
        want = str(item.get(rest)) if isinstance(item.get(rest), int) else None
    elif kind == "bool":
        f, t, fl = rest.split(":")
        if isinstance(item.get(f), bool):
            want = t if item[f] else fl
    elif kind == "topid":
        ids = [o.get("id") for o in a.get("options") or [] if isinstance(o, dict)]
        if item.get(rest) in ids:
            want = str(ids.index(item[rest]))
    elif kind == "prose":
        lab = _prefix_label(item.get(rest), labels)
        if lab is None and unit["kind"] == "ks3-psort-block":
            v = str(item.get(rest) or "").strip().lower()
            lab = {"pure.": "Pure substance", "mixture.": "Mixture"}.get(v)
        if lab is not None and labels.count(lab) == 1:
            return lab, "authored %s (opens with the option)" % rest
        return None, "authored %s is prose that does not name one option" % rest
    if want is None or str(want) not in vals:
        return None, "authored %s does not match a rendered option" % how
    hits = [l for v, l in zip(vals, labels) if v == str(want)]
    return (hits[0], "authored " + how) if len(hits) == 1 else (None, "ambiguous option value")


if __name__ == "__main__":
    for u in units(sys.argv[1]):
        print(u["id"], u["kind"], u["key_from"], "|", u["prompt"][:80], "|", u["options"][:4], "→", u["key"])
