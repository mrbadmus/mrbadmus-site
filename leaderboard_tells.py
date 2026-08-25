"""leaderboard_tells.py — no invented student reaches the live leaderboard.

MRB-290, the fast gate. Runs in well under a second and asserts one thing:
the built `leaderboard.html`, in BOTH trees, carries nothing Design invented.

⚑ THE CORPUS IS DERIVED FROM THE DELIVERY, ON EVERY RUN, AND NEVER TYPED.

The hand-written ancestor of this check records what a typed list costs —
`student_page_drive.py`: *"THIS LIST WAS TOO SHORT AND THE DRIVE PASSED
BECAUSE OF IT."* So this file opens the vendored `.dc.html`, parses `FIRST`,
`LAST` and `VIEWER` out of its own source, runs Design's own roster formula

    FIRST[i] + LAST[(i * 7 + off) % 20] + (21 + ((i * 13 + off) % 58))

for both tier offsets (0 Higher, 3 Foundation), adds `VIEWER`, and pins the
sixty-one strings that come out. The day Design ships a thirty-first first
name, the corpus grows by itself.

⚠️ IT PINS EXACT STRINGS, NOT SHAPES, AND THAT IS THE WHOLE CALIBRATION.

Real MrBadmusAI usernames are generator-built from the SAME vocabulary as
Design's sample. These are real students on the live board:

    FoxWave36   FalconGlide41   BlazeCove46   WolfSummit53   WafflePulse21

and these are Design's inventions:

    FoxWave21   FalconSpark34   BlazeVault47   WolfCrest86    WaffleDrift27

A gate that matched "capitalised word + capitalised word + two digits", or
that matched on the `FIRST`/`LAST` tokens alone, would fire on every real
student on the board — and a gate that cries wolf gets switched off. So the
match is the whole handle, exactly. (Checked 25 Aug 2026 against the live
board: zero collisions between the derived sixty-one and the real cohort. If
that ever stops being true the collision is REPORTED as a limitation rather
than silently subtracted, because a real handle that happens to equal an
invented one is indistinguishable to this file and to a reader.)

⛔ THE FIXTURES ARE EXEMPT, BY NAME AND NOT BY PATTERN. `leaderboard_fixtures/`
carries Design's sample on purpose — that is what lets the behaviour gate
drive every control with no network. It is outside every tree
`generate_site_v5.py` publishes or round-trips, which is why the sample being
in it is safe. This file scans the two LIVE paths and nothing else; it never
globs, so a fixture cannot be exempted by accident and a new live page cannot
be scanned by accident either.
"""

import os
import re
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
DELIVERY = os.path.join("docs", "ks3", "design-reference", "leaderboard",
                        "source", "KS4 Weekly Leaderboard.dc.html")

# The two trees the page is served from. Named, never globbed.
LIVE_PAGES = [
    os.path.join("leaderboard.html"),
    os.path.join("mrbadmus_site", "leaderboard.html"),
]

# ⚑ THE FABRICATORS, BY NAME. Every one is dropped by a ruling in
# build_leaderboard_port.RULINGS, so every one must be absent from the built
# page. A name still present means a ruling matched nothing — which is the
# silent-green failure the whole port is written against.
GONE = {
    "const FIRST": "R5 — the thirty invented first-name tokens",
    "const LAST": "R5 — the twenty invented last-name tokens",
    "const VIEWER": "R3 — Design's one hard-typed identity",
    "const WEEKS": "R4 — a fixed nine weeks",
    "const LIVE": "R4 — LIVE = WEEKS - 1",
    "roster(": "R6 — the cohort fabricator",
    "entered(": "R6 — who sat, invented",
    "this.seed(": "R6 — the per-name PRNG seed",
    "AmberYew12": "R3 — the sample viewer's handle",
}

# ⊕ `hash(` AND `rng(` ARE ALLOWED, AND EXACTLY TWICE EACH.
#
# Design's confetti is the only remaining caller, and confetti is
# presentation, which Mide's first ruling preserves. This is the same
# allowance `teacher_tells` makes for `seed(` in `hueFor`, for the same
# reason: banning the primitive outright would force the port to
# re-implement an identical PRNG under another name purely to pass a gate.
#
# Two each = the function's own declaration, plus the one call in `confetti`.
# A THIRD is a fabricator that survived a ruling, so the count is asserted
# rather than the name merely allowed. See RULINGS R23.
PRNG_BUDGET = {"hash(": 2, "rng(": 2}


def roster_corpus(path=DELIVERY):
    """Design's sixty-one handles, derived from her own constants."""
    src = open(path, encoding="utf-8").read()

    def arr(name):
        m = re.search(r"^const %s = \[(.*?)\];" % name, src, re.S | re.M)
        if not m:
            raise SystemExit(
                "leaderboard_tells.py: the delivery has no `const %s = [...]`."
                "\n  The corpus is DERIVED from the delivery and never typed, "
                "so a renamed constant must be re-anchored here — not worked "
                "around. A corpus that silently came out empty would pass "
                "this gate on a page carrying every invented name."
                % name)
        return re.findall(r"'([^']*)'", m.group(1))

    first, last = arr("FIRST"), arr("LAST")
    m = re.search(r"^const VIEWER = '([^']*)'", src, re.M)
    if not m:
        raise SystemExit("leaderboard_tells.py: the delivery has no "
                         "`const VIEWER = '...'`.")
    viewer = m.group(1)

    out = set()
    # Design's `roster(tier)`: off = 0 for Higher, 3 for Foundation.
    for off in (0, 3):
        for i, f in enumerate(first):
            out.add(f + last[(i * 7 + off) % len(last)]
                    + str(21 + ((i * 13 + off) % 58)))
    out.add(viewer)
    return out, viewer


def check_page(path, corpus):
    problems = []
    page = open(path, encoding="utf-8").read()

    hits = sorted(h for h in corpus if h in page)
    if hits:
        problems.append(
            "carries %d of Design's invented handle(s): %s%s. None of these "
            "students exist — but on a public page they are indistinguishable "
            "from a real student's username leaking."
            % (len(hits), ", ".join(hits[:6]),
               "" if len(hits) <= 6 else ", …"))

    for tell, why in sorted(GONE.items()):
        if tell in page:
            problems.append(
                "still contains %r (%s). A ruling that was supposed to remove "
                "it matched nothing, or matched and was undone." % (tell, why))

    # ⚠️ THE UNBOUND MONOGRAM. `>AY<` is Design's typed initials sitting in a
    # text node — R2 rewrites both of them to `{{ me.initials }}`, so a
    # surviving one is a binding that did not apply. It is two characters
    # long and would be invisible to any substring corpus, which is exactly
    # why it is checked by its markup shape instead.
    n_ay = len(re.findall(r">\s*AY\s*<", page))
    if n_ay:
        problems.append(
            "carries %d unbound 'AY' monogram(s) — Design's sample viewer's "
            "initials, typed into the markup. R2 binds both to "
            "`me.initials`; a survivor means the binding did not apply, and "
            "every real student would read another student's initials in the "
            "card headed YOUR STANDING." % n_ay)

    for tell, budget in sorted(PRNG_BUDGET.items()):
        got = page.count(tell)
        if got > budget:
            problems.append(
                "calls %s %d time(s); the budget is %d (the declaration plus "
                "Design's confetti, RULINGS R23). A third caller is a data "
                "fabricator that survived a ruling." % (tell, got, budget))

    return problems


def main(argv=None):
    os.chdir(REPO)
    print("\n\U0001F50E  leaderboard_tells — no invented student on the live "
          "page\n")

    if not os.path.exists(DELIVERY):
        raise SystemExit(
            "leaderboard_tells.py: the vendored delivery is missing at %s. "
            "The corpus is derived from it, so without it this gate cannot "
            "assert anything — and passing would be a lie." % DELIVERY)

    corpus, viewer = roster_corpus()
    if len(corpus) < 61:
        raise SystemExit(
            "leaderboard_tells.py: derived only %d handle(s) from the "
            "delivery and expected at least 61. The formula or the constants "
            "have moved; a short corpus is the defect this file's own header "
            "warns about." % len(corpus))
    print("     corpus  %d handle(s) derived from the delivery's own "
          "constants" % len(corpus))
    print("     viewer  %s (the one hard-typed identity)" % viewer)

    failed = checked = 0
    for path in LIVE_PAGES:
        if not os.path.exists(path):
            print("     %-30s ⚠️  not built" % path)
            failed += 1
            continue
        problems = check_page(path, corpus)
        checked += 1
        if problems:
            failed += 1
            print("     %-30s ❌ %d problem(s)" % (path, len(problems)))
            for p in problems:
                print("          · %s" % p)
        else:
            print("     %-30s ✅" % path)

    print("\n     ⊕ %s/ is EXEMPT and is never scanned: it carries Design's\n"
          "       sample on purpose, and sits outside every tree "
          "generate_site_v5\n       publishes or round-trips."
          % "leaderboard_fixtures")

    if failed:
        print("\n  FAIL  %d of %d live page(s).\n" % (failed, len(LIVE_PAGES)))
        return 1
    print("\n  PASS  %d live page(s): no invented handle, no fabricator, no "
          "unbound\n        monogram, the PRNG budget intact.\n" % checked)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
