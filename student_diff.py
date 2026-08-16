#!/usr/bin/env python3
"""student_diff.py — what changes for a STUDENT between two built KS3 trees.

    python3 student_diff.py <old-root> <new-root> [path-fragment ...]

Both roots are built KS3 trees — the `ks3/` directory a `build_ks3.py` run
produces. To make the "old" one, put the commit you are replacing in a
worktree and build it there:

    git worktree add /tmp/base <ref> --detach
    cd /tmp/base && python3 build_ks3.py && cd -
    python3 student_diff.py /tmp/base/ks3 ks3 particles-and-their-behaviour

Why this exists (MRB-228, 16 Aug 2026)
──────────────────────────────────────
A unit that rebuilds pages students can already reach is a different risk from
a unit that adds pages nobody has seen. `git diff` answers "what changed in the
source", which for a rebuilt lesson is *everything* — a 1728-line module became
six modules and the diff is unreadable. The question that actually matters
before pushing over a live page is narrower and nobody was answering it:

    a student who used this page last week opens it today. What is different?

So this reads the BUILT pages, not the source, and reports only what reaches
the student: the headings they navigate by, the questions they answer, the
prose they read, and the instruments they operate. Styling, ordering of
attributes, cache-bust stamps and every internal id are deliberately ignored.

It is a reporting tool. It has no exit-code opinion, because "this lesson now
asks a different question" is a fact for Mide to weigh, not a build failure.
"""

import os
import re
import sys
from html.parser import HTMLParser

# Elements whose text a student never reads.
_MUTE = {"script", "style", "svg", "title"}

# The instrument marker attributes, which are how a page says "there is a
# mechanism here". Read from the built markup rather than from a list kept in
# step by hand: any `data-*block` attribute is one, plus the two instruments
# that take a bare marker.
_INSTRUMENT_ATTR = re.compile(r"^data-([a-z]+)block$")
_EXTRA_MARKERS = {"data-scalecards", "data-instrument"}


class Page(HTMLParser):
    """The student-visible content of one built lesson page."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.headings = []       # (level, text)
        self.prose = []          # paragraph text
        self.options = []        # option-button labels
        self.instruments = []    # marker attribute names, in document order
        self.rail = []           # (short label, ticked-on-load)
        self.keyfacts = []
        self._stack = []
        self._buf = []
        self._grab = None
        self._hidden = 0

    # ── plumbing ────────────────────────────────────────────────────────
    def _flush(self):
        text = re.sub(r"\s+", " ", "".join(self._buf)).strip()
        self._buf = []
        return text

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self._stack.append(tag)
        if tag in _MUTE:
            self._hidden += 1
            return
        # `hidden` content is in the document but not on the page. It is the
        # reveal panel before the student commits, and counting it as prose
        # would report every answer as something they already read.
        if "hidden" in a:
            self._hidden += 1
            self._stack[-1] = tag + "\x00hidden"

        for k in a:
            m = _INSTRUMENT_ATTR.match(k)
            if m:
                self.instruments.append(k)
            elif k in _EXTRA_MARKERS and k == "data-scalecards":
                self.instruments.append(k)

        cls = a.get("class", "")
        if tag in ("h1", "h2", "h3") and not self._hidden:
            self._grab = ("h", int(tag[1]))
            self._buf = []
        elif tag == "p" and not self._hidden:
            self._grab = ("p", cls)
            self._buf = []
        elif "ks3-opt-label" in cls:
            self._grab = ("opt", None)
            self._buf = []
        elif "ks3-rail-chip" in cls:
            # A rail stop's tick state on load is a MRB-208 property and a
            # student-visible one: nothing may be ticked before they do
            # anything.
            self.rail.append((a.get("data-short") or a.get("title") or "?",
                              a.get("data-done") == "1"
                              or "is-done" in cls))

    def handle_endtag(self, tag):
        while self._stack:
            top = self._stack.pop()
            base = top.split("\x00")[0]
            if "\x00hidden" in top:
                self._hidden = max(0, self._hidden - 1)
            if base in _MUTE:
                self._hidden = max(0, self._hidden - 1)
            if base == tag:
                break
        if not self._grab:
            return
        kind, meta = self._grab
        text = self._flush()
        self._grab = None
        if not text:
            return
        if kind == "h":
            self.headings.append((meta, text))
        elif kind == "p":
            # The KEY FACT statement IS a `<p>`, carrying the class itself —
            # not a `<p>` inside a wrapper, which is what the flag below was
            # built for. Routed on the paragraph's own class, which is the
            # only thing that is actually true of the markup.
            (self.keyfacts if "ks3-keyfact-body" in (meta or "")
             else self.prose).append(text)
        elif kind == "opt":
            self.options.append(text)

    def handle_data(self, data):
        if self._grab and not self._hidden:
            self._buf.append(data)


def read(path):
    p = Page()
    p.feed(open(path, encoding="utf-8").read())
    return p


def words(chunks):
    return sum(len(re.findall(r"[A-Za-z']+", c)) for c in chunks)


def compare(name, old, new, label):
    """Set-compare two lists of student-visible strings."""
    o, n = list(old), list(new)
    gone = [x for x in o if x not in n]
    came = [x for x in n if x not in o]
    if not gone and not came and o == n:
        return ["    %-12s unchanged (%d)" % (label, len(o))]
    out = ["    %-12s %d → %d" % (label, len(o), len(n))]
    for x in gone[:6]:
        out.append("        − %s" % (x if len(x) < 96 else x[:93] + "…"))
    if len(gone) > 6:
        out.append("        − …and %d more removed" % (len(gone) - 6))
    for x in came[:6]:
        out.append("        + %s" % (x if len(x) < 96 else x[:93] + "…"))
    if len(came) > 6:
        out.append("        + …and %d more added" % (len(came) - 6))
    if not gone and not came:
        out.append("        (same set, different order)")
    return out


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    old_root, new_root, filters = argv[1], argv[2], argv[3:]

    pages = []
    for d, _, fs in os.walk(new_root):
        for f in sorted(fs):
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(d, f), new_root)
            if filters and not any(x in rel for x in filters):
                continue
            pages.append(rel)

    print("student_diff · %d page(s)\n%s" % (len(pages), "=" * 60))
    changed = 0
    for rel in sorted(pages):
        op, np_ = os.path.join(old_root, rel), os.path.join(new_root, rel)
        if not os.path.exists(op):
            print("\n%s\n    NEW PAGE — nothing to compare against." % rel)
            changed += 1
            continue
        a, b = read(op), read(np_)

        lines = []
        lines += compare(rel, [t for _, t in a.headings],
                         [t for _, t in b.headings], "headings")
        lines += compare(rel, a.options, b.options, "options")
        lines += compare(rel, a.keyfacts, b.keyfacts, "key facts")
        lines += compare(rel, a.instruments, b.instruments, "instruments")

        wa, wb = words(a.prose), words(b.prose)
        pa, pb = len(a.prose), len(b.prose)
        if (wa, pa) != (wb, pb):
            lines.append("    %-12s %d paragraphs / %d words → %d / %d"
                         % ("prose", pa, wa, pb, wb))
        else:
            lines.append("    %-12s unchanged (%d paragraphs, %d words)"
                         % ("prose", pa, wa))

        # Rail ticks on load. Anything ticked here is an MRB-208 breach and is
        # called out rather than counted.
        lit_a = [s for s, done in a.rail if done]
        lit_b = [s for s, done in b.rail if done]
        if lit_a or lit_b:
            lines.append("    ⚠️ rail ticked ON LOAD — was %s, now %s"
                         % (lit_a or "nothing", lit_b or "nothing"))

        interesting = [l for l in lines if "unchanged" not in l]
        if interesting:
            changed += 1
            print("\n%s" % rel)
            for l in lines:
                print(l)

    print("\n%s\n%d of %d page(s) differ for a student."
          % ("=" * 60, changed, len(pages)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
