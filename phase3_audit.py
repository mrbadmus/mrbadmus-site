#!/usr/bin/env python3
"""Phase 3 — assume something is wrong and go and find it.

Checks the BUILT tree against Design's delivered pages and against the claims
this run is about to make, rather than against what it intended.

Run from the repo root:  python3 phase3_audit.py
"""
import collections
import json
import os
import re
import sys

REF = "docs/ks3/design-reference/p1"
OUT = "ks3/physics/energy-transfers"
SLUGS = ["energy-stores", "energy-transfers-before-and-after",
         "conservation-of-energy", "heating-and-thermal-equilibrium",
         "conduction", "radiation", "insulation", "simple-machines"]

fails = []
notes = []


def check(name, ok, detail):
    print(("  OK   " if ok else "  FAIL ") + name + " — " + detail)
    if not ok:
        fails.append(name)


def ref_pages():
    return sorted(f for f in os.listdir(REF)
                  if f.startswith("p1-") and f.endswith(".dc.html"))


def main():
    refs = ref_pages()
    print("── 1 · every lesson built, and paired with a delivered page ──")
    check("eight pages built", len(SLUGS) == 8 and all(
        os.path.exists(os.path.join(OUT, s + ".html")) for s in SLUGS),
        "%d slugs, all present in %s" % (len(SLUGS), OUT))
    check("eight delivered pages", len(refs) == 8,
          "%d .dc.html in %s" % (len(refs), REF))

    print("\n── 2 · rails, element for element against her RAIL const ──")
    bad = []
    for slug, ref in zip(SLUGS, refs):
        html = open(os.path.join(OUT, slug + ".html"), encoding="utf-8").read()
        m = re.search(r'data-rail-stages="([^"]*)"', html)
        got = [s["anchor"] for s in
               json.loads(m.group(1).replace("&quot;", '"'))] if m else []
        page = open(os.path.join(REF, ref), encoding="utf-8").read()
        rail = re.search(r"const RAIL\s*=\s*(\[.*?\]);", page, re.S)
        want = re.findall(r"id: '([^']+)'", rail.group(1)) if rail else []
        if got != want:
            bad.append("%s built=%s design=%s" % (slug, got, want))
    check("all eight rails match", not bad, "; ".join(bad) or "8/8 identical")

    print("\n── 3 · every SECTION she draws exists on the built page ──")
    missing = []
    for slug, ref in zip(SLUGS, refs):
        page = open(os.path.join(REF, ref), encoding="utf-8").read()
        want = re.findall(r'<section id="(s-[a-z0-9-]+)"', page)
        html = open(os.path.join(OUT, slug + ".html"), encoding="utf-8").read()
        for sec in want:
            if ('id="%s"' % sec) not in html:
                missing.append("%s missing #%s" % (slug, sec))
    check("no section dropped", not missing,
          "; ".join(missing) or "every #s-* she draws is on the built page")

    print("\n── 4 · no draft / review language anywhere a student can see ──")
    hits = []
    for slug in SLUGS:
        html = open(os.path.join(OUT, slug + ".html"), encoding="utf-8").read()
        for word in ("draft", "not yet science", "not yet checked",
                     "provisional", "review-flag", "unreviewed"):
            if re.search(word, html, re.I):
                hits.append("%s: %s" % (slug, word))
    check("no draft language", not hits,
          "; ".join(hits) or "swept for the CONCEPT on all 8 pages")

    print("\n── 5 · MRB-204 · formula shapes against their arithmetic ──")
    sys.path.insert(0, ".")
    import ks3_data
    beam_bad, tri_bad = [], []
    for u in ks3_data.build_units():
        if u.get("code") != "P1":
            continue
        for l in u.get("lessons", []):
            for a in l.get("activities", []):
                if a.get("id") == "conservation-beam":
                    tot = int(a.get("total") or 0)
                    for s in a.get("splits") or []:
                        got = sum(int(s.get(k) or 0)
                                  for k in ("grav", "kin", "therm"))
                        if got != tot:
                            beam_bad.append("%s %s=%d≠%d"
                                            % (l["slug"], s.get("id"), got, tot))
            for b in l.get("core", []):
                if isinstance(b, dict) and b.get("type") == "formula":
                    # A triangle is only legitimate over a PRODUCT.
                    st = (b.get("statement") or "").lower()
                    if b.get("triangle") and ("=" in st and "+" in st):
                        tri_bad.append("%s: triangle over a sum" % l["slug"])
                    if b.get("figure", {}).get("shape") == "balance" and \
                            not b.get("statement"):
                        tri_bad.append("%s: beam with no statement" % l["slug"])
    check("every beam split totals the whole", not beam_bad,
          "; ".join(beam_bad) or "all splits sum to their total")
    check("no triangle over a sum", not tri_bad,
          "; ".join(tri_bad) or "triangles sit only over products")

    print("\n── 6 · MRB-278 and MRB-177 on the BUILT corpus ──")

    def W(t):
        return len(re.findall(r"[^\s]+", re.sub(r"<[^>]+>", " ", str(t))))

    def otext(o):
        return o.get("text", "") if isinstance(o, dict) else o

    tells, lad = [], collections.Counter()
    for u in ks3_data.build_units():
        for l in u.get("lessons", []):
            if not l.get("authored"):
                continue
            for rung, r in (l.get("ladder") or {}).items():
                if not (isinstance(r, dict) and r.get("options")):
                    continue
                c = r.get("answer")
                if u.get("code") == "P1" and isinstance(c, int):
                    lad[c] += 1
                wc = [W(otext(o)) for o in r["options"]]
                if c is None or not (0 <= c < len(wc)):
                    continue
                top = max(w for i, w in enumerate(wc) if i != c)
                if wc[c] == max(wc) and wc[c] > top and (
                        wc[c] - top >= 4 or wc[c] >= 1.4 * top):
                    tells.append("%s %s" % (l["slug"], rung))
    row = [lad.get(i, 0) for i in range(4)]
    check("no length tell in any ladder rung", not tells,
          "; ".join(tells) or "key stage clean")
    check("P1 answer positions spread", 0 not in row and max(row) * 2 <= sum(row),
          "P1 ladder index counts %s" % row)

    print("\n── 7 · misconception ids exist in the register ──")
    reg = open("docs/ks3/misconception-register.md", encoding="utf-8").read()
    want, missing = set(), []
    for u in ks3_data.build_units():
        if u.get("code") != "P1":
            continue
        for l in u.get("lessons", []):
            for m in l.get("misconceptions") or []:
                want.add(m["id"])
    for i in sorted(want):
        if ("| `%s` |" % i) not in reg:
            missing.append(i)
    check("every cited id is registered", not missing,
          "; ".join(missing) or "%d ids, all present: %s"
          % (len(want), " ".join(sorted(want))))
    bad_prefix = [i for i in want if i.startswith("ENERGY-")]
    check("no ENERGY- prefix used", not bad_prefix,
          "; ".join(bad_prefix) or "all ids use the ruled ENER prefix")

    print("\n── 8 · student-visible convention checks ──")
    subs, arrows = [], []
    for slug in SLUGS:
        html = open(os.path.join(OUT, slug + ".html"), encoding="utf-8").read()
        body = re.sub(r"<script.*?</script>", "", html, flags=re.S)
        if re.search(r"[₀-₉]", body):
            subs.append(slug)
        # A typed arrow INSIDE a formula block is the thing MRB-204 forbids.
        for blk in re.findall(r'<section[^>]*ks3-formula.*?</section>', body, re.S):
            if "→" in blk or "->" in blk:
                arrows.append(slug)
    check("no Unicode subscripts in student text", not subs,
          "; ".join(subs) or "none on any page (use <sub> in markup)")
    check("no typed arrow inside a formula block", not arrows,
          "; ".join(arrows) or "formula blocks carry no typed arrows")

    print("\n" + "=" * 62)
    if fails:
        print("❌ %d PHASE-3 CHECK(S) FAILED: %s" % (len(fails), ", ".join(fails)))
        return 1
    print("✅ phase 3: every check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
