#!/usr/bin/env python3
"""ks4_brief.py — the authoring brief for one KS4 topic (MRB-332).

    python3 ks4_brief.py physics energy > brief.md
    python3 ks4_brief.py --list

An author writing the twelve assignment questions for a subtopic needs three
things in front of them, and hunting for any of the three is how a question
ends up off-spec:

  1. **What AQA says** — the spec reference, the page's own summary, its
     theory prose, its key note and its declared common mistake. All of it is
     already in `all_subtopics_*.py`; this pulls it into one place.
  2. **Who the question is for** — the derived tier and triple flags, so the
     author knows whether Higher-only physics is in scope or out of it.
  3. ⚠️ **Everything the lesson page already PRINTS** — its "Test yourself"
     questions, its worked FIFA examples and its matching block — reproduced
     in full, as a DO-NOT-DUPLICATE list.

Point 3 is the one that matters most and is the least obvious. All three are
a DIFFERENT POOL under the one-pool-per-surface law, a child can open that
page whenever they like, and all three are printed WITH their answers — a
FIFA is a fully worked solution and a matching block shows its own pairs. An
assignment question that restates any of them is homework whose answers are
printed on a page the child is being sent to read. Showing the author those
items is strictly better than hiding them: hidden, they get rediscovered by
accident; shown, they get avoided on purpose.

⊕ **`fifas` and `matching` were added on 6 Sep 2026, after the physics lanes
had already authored against a `quiz`-only list.** One lane diffed its own
draft against the page's full printed content and found six of its questions
echoing a FIFA or a matching pair — invisible defects, because the brief had
never shown it what it was colliding with. If you are reading this while
reviewing physics, that is the gap the cold review was asked to close.

The Higher-tier and Triple-only extension prose is included where the page
carries it, because for a `tier='higher'` or `triple_only` subtopic that
prose IS the content in scope.
"""

import importlib
import os
import sys
import textwrap

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)

import ks4_data  # noqa: E402

# The module that carries the FULLEST version of a page. Triple Higher is the
# superset of all twelve blocks, so its record holds the higher-tier and
# triple-only prose a Foundation module omits. An author reading the
# foundation record for a higher-tier subtopic would be reading a page that
# does not contain the content they have to examine.
FULLEST = "_triple_higher"


def _pages(subject):
    mod = importlib.import_module("all_subtopics_%s%s" % (subject, FULLEST))
    pages = getattr(mod, "%s_SUBTOPICS_ALL" % subject.upper())
    out = {}
    for topic_id, sts in pages.items():
        for st in sts:
            out[st["id"]] = (topic_id, st)
    return out


def _wrap(s, indent="  "):
    if not s:
        return ""
    return "\n".join(
        textwrap.fill(line, 96, initial_indent=indent,
                      subsequent_indent=indent) or indent
        for line in str(s).split("\n"))


def _theory(st):
    out = []
    for blk in st.get("theory") or []:
        if isinstance(blk, dict):
            head = blk.get("heading") or blk.get("title")
            if head:
                out.append("  ### %s" % head)
            body = blk.get("content") or blk.get("text") or ""
            out.append(_wrap(body, "  "))
        else:
            out.append(_wrap(blk, "  "))
    return "\n".join(out)


def brief(subject, topic):
    cls = ks4_data.classify()
    pages = _pages(subject)
    slugs = [s for s, m in sorted(cls.items(), key=lambda kv: kv[1]["order"])
             if m["subject"] == subject and m["topic"] == topic]
    if not slugs:
        raise SystemExit("ks4_brief: no subtopics for %s / %s" % (subject, topic))

    L = []
    L.append("# KS4 assignment-pool authoring brief")
    L.append("")
    L.append("**Subject:** %s   **Topic:** `%s`   **Subtopics:** %d   "
             "**Questions to write:** %d"
             % (subject, topic, len(slugs), len(slugs) * 12))
    L.append("")
    L.append("Write `ks4_data/questions/%s/%s.py`. Twelve questions per "
             "subtopic — four `easier`, four `standard`, four `harder`."
             % (subject, topic))
    L.append("")

    for slug in slugs:
        meta = cls[slug]
        entry = pages.get(slug)
        L.append("")
        L.append("=" * 100)
        L.append("## `%s`" % slug)
        L.append("")
        aud = ("BASE — every class, including Foundation Combined"
               if meta["tier"] == "foundation" and not meta["triple_only"]
               else "HIGHER TIER ONLY" if not meta["triple_only"]
               else "TRIPLE ONLY, %s tier" % meta["tier"])
        L.append("* **tier:** `%s`   **triple_only:** `%s`   → %s"
                 % (meta["tier"], meta["triple_only"], aud))
        if entry is None:
            L.append("* ⚠️ no page record found — author from the AQA spec.")
            continue
        topic_id, st = entry
        L.append("* **title:** %s" % st.get("title"))
        L.append("* **AQA spec point:** %s" % st.get("spec"))
        L.append("")
        if st.get("summary"):
            L.append("**Spec statement.**")
            L.append(_wrap(st["summary"]))
            L.append("")
        if st.get("key_note"):
            L.append("**Key note.**")
            L.append(_wrap(st["key_note"]))
            L.append("")
        if st.get("common_mistake"):
            L.append("**Declared common mistake — the best distractor source.**")
            L.append(_wrap(st["common_mistake"]))
            L.append("")
        if st.get("equations"):
            L.append("**Equations.**")
            for e in st["equations"]:
                L.append("  - %s" % (e,))
            L.append("")
        if st.get("variables"):
            L.append("**Quantities and units.**")
            for v in st["variables"]:
                L.append("  - %s" % (v,))
            L.append("")
        if st.get("rp"):
            L.append("**Required practical.**")
            L.append(_wrap(st["rp"]))
            L.append("")
        body = _theory(st)
        if body:
            L.append("**Theory (the page's own teaching).**")
            L.append(body)
            L.append("")
        if st.get("higher"):
            L.append("**HIGHER-TIER extension prose.**")
            L.append(_wrap(st["higher"]))
            L.append("")
        if st.get("triple_only"):
            L.append("**TRIPLE-ONLY extension prose.**")
            L.append(_wrap(st["triple_only"]))
            L.append("")

        # ⚠️ THREE KINDS OF PUBLISHED ITEM, NOT ONE (found in the wild,
        # MRB-332, by the electricity lane). The first version of this brief
        # printed only `quiz`, and six questions in one lane's draft turned
        # out to echo `fifas` and `matching` instead — which are ALSO printed
        # on the lesson page, and printed WITH THEIR ANSWERS: a FIFA is a
        # fully worked solution and a matching block shows its own pairs.
        # Reproducing one as homework is the same defect as reproducing a
        # quiz question, and it was invisible because the brief never showed
        # the author the thing they were colliding with.
        quiz = st.get("quiz") or []
        fifas = st.get("fifas") or []
        matching = st.get("matching") or {}
        pairs = (matching.get("pairs") or []) if isinstance(matching, dict) \
            else []

        L.append("**⚠️ DO NOT DUPLICATE — everything the lesson page already "
                 "PRINTS for this subtopic.**")
        L.append("")
        L.append("  All of it is a DIFFERENT POOL, on a page the child can "
                 "open at will, and all of it")
        L.append("  is printed WITH its answers. An assignment question that "
                 "restates any of it is")
        L.append("  homework whose answers are already published. Write "
                 "around them — same spec")
        L.append("  content, different question.")
        L.append("")
        L.append("  · \"Test yourself\" questions: %d" % len(quiz))
        L.append("  · worked FIFA examples (full solutions shown): %d"
                 % len(fifas))
        L.append("  · matching pairs (shown already paired): %d" % len(pairs))
        L.append("")

        if quiz:
            L.append("  ── \"Test yourself\" questions ──")
            for i, qz in enumerate(quiz, 1):
                L.append("  %d. %s" % (i, (qz.get("q") or qz.get("text") or "")))
                for o in (qz.get("opts") or []):
                    txt = o[0] if isinstance(o, (list, tuple)) else o
                    mark = "✓" if (isinstance(o, (list, tuple)) and o[1]) else " "
                    L.append("       [%s] %s" % (mark, txt))
            L.append("")

        if fifas:
            L.append("  ── worked FIFA examples — the page shows the whole "
                     "solution, so the numbers")
            L.append("     AND the shape of the question are both already "
                     "given away ──")
            for i, fz in enumerate(fifas, 1):
                if isinstance(fz, dict):
                    L.append("  %d. %s" % (i, fz.get("q") or fz.get("question")
                                           or fz.get("title") or ""))
                    for k in ("formula", "insert", "fix", "answer"):
                        if fz.get(k):
                            L.append("       %-8s %s" % (k + ":", fz[k]))
                else:
                    L.append("  %d. %s" % (i, fz))
            L.append("")

        if pairs:
            L.append("  ── matching block — printed already paired ──")
            if matching.get("instruction"):
                L.append("     (%s)" % matching["instruction"])
            for a, b in pairs:
                L.append("     %s  ↔  %s" % (a, b))
            L.append("")
    return "\n".join(L)


def main():
    if "--list" in sys.argv:
        cls = ks4_data.classify()
        seen = []
        for _s, m in sorted(cls.items(), key=lambda kv: kv[1]["order"]):
            key = (m["subject"], m["topic"])
            if key not in seen:
                seen.append(key)
        for subject, topic in seen:
            n = sum(1 for m in cls.values()
                    if m["subject"] == subject and m["topic"] == topic)
            print("%-10s %-24s %2d subtopics  %3d questions"
                  % (subject, topic, n, n * 12))
        return 0
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    print(brief(sys.argv[1], sys.argv[2]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
