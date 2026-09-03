#!/usr/bin/env python3
"""
seating_tells.py — MRB-322. The static gate on the seating-plans surface.

Five things this watches, each of which failed silently somewhere else in this
estate before it was gated here.

1. THE ROOM LIST IS ONE LIST.
   It is written down three times — the dropdown in `shared/seating-data.js`,
   the CHECK constraint in the migration, and this file. Three copies is two
   too many, but the two that exist are load-bearing (the browser needs it to
   draw a dropdown; the database needs it to refuse anything else) and neither
   can import the other. So the third copy's whole job is to fail the build the
   moment the first two stop agreeing. A room silently dropped from the
   dropdown looks exactly like a room nobody has drawn yet.

2. NO FIXTURE DATA SHIPS.
   The canvas harness fills seats with `ZZ Test-Seat 1`; the RLS rehearsal
   built a throwaway school whose ids all start `bbbb3220`. Neither is a
   plausible thing to find on a live page, which is exactly why both carry a
   tell and why this gate greps for the tells rather than for plausibility.

3. THE PHOTO IS NEVER PERSISTED.
   The room-scan endpoint holds a photograph of a real classroom in a real
   school. It is held in memory and discarded. This walks the handler in the
   backend repo and fails on any filesystem write, storage upload, or log call
   that could reach the image bytes. `pool_ownership.py` already reads that
   repo by absolute path; this follows it.

4. THE UNCONFIGURED CONTRACT MATCHES ON BOTH SIDES.
   The frontend decides whether to show "Photo scan isn't switched on yet" by
   testing one exact string against the backend's error code. Two repos, one
   string, no shared type — so it gets gated.

5. THE DEV HARNESS NEVER REACHES THE OUTPUT TREE.
   `seating_harness.html` is a bench for working on the canvas. It carries
   placeholder labels by design, so the one thing that must stay true is that
   it never appears under `mrbadmus_site/`.

Run:  python3 seating_tells.py
Exit: 0 clean, 1 on any finding.
"""

import os
import re
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
BACKEND = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend/server.js"

# ── 1. The canonical room list ───────────────────────────────────────────
# Verbatim, in the order Mide gave it.
ROOMS = ["S01", "S02a", "S02b", "S02c", "S04",
         "S08a", "S08b", "S08c", "S09a", "S09b", "S010"]

MIGRATION = "supabase/migrations/20260902214105_mrb322_seating_plans.sql"
DATA_JS = "shared/seating-data.js"
PHOTO_JS = "shared/seating-photo.js"
PAGE = "teacher/seating.html"
HARNESS = "seating_harness.html"

SHIPPED = [DATA_JS, PHOTO_JS, PAGE, "shared/seating-canvas.js", "shared/seating.css"]

# ── 2. Fixture tells that must never ship ────────────────────────────────
TELLS = [
    ("ZZ Test-",   "the canvas harness's placeholder seat labels"),
    ("ZZ-MRB322",  "the RLS rehearsal's throwaway school"),
    ("zz-mrb322",  "the RLS rehearsal's throwaway sign-ins"),
    ("bbbb3220",   "the RLS rehearsal's throwaway row ids"),
    ("ZZ-Pupil",   "the RLS rehearsal's throwaway pupils"),
]

UNCONFIGURED = "photo_scan_unconfigured"

findings = []


def fail(check, detail):
    findings.append((check, detail))


def read(rel, root=REPO):
    p = rel if os.path.isabs(rel) else os.path.join(root, rel)
    if not os.path.exists(p):
        return None
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


# ═════════════════════════════════════════════════════════════════════════
# 1 · the room list agrees in all three places
# ═════════════════════════════════════════════════════════════════════════
def check_rooms():
    js = read(DATA_JS)
    if js is None:
        fail("rooms", "%s is missing" % DATA_JS)
    else:
        m = re.search(r"const ROOMS = \[(.*?)\];", js, re.S)
        if not m:
            fail("rooms", "%s: no `const ROOMS = [...]` to check" % DATA_JS)
        else:
            found = re.findall(r"'([^']+)'", m.group(1))
            if found != ROOMS:
                fail("rooms", "%s room list drifted.\n     want: %s\n     got:  %s"
                     % (DATA_JS, ROOMS, found))

    sql = read(MIGRATION)
    if sql is None:
        fail("rooms", "%s is missing" % MIGRATION)
    else:
        m = re.search(r"room_code in\s*\((.*?)\)", sql, re.S)
        if not m:
            fail("rooms", "%s: no room_code CHECK constraint to check" % MIGRATION)
        else:
            found = re.findall(r"'([^']+)'", m.group(1))
            if found != ROOMS:
                fail("rooms", "%s CHECK drifted.\n     want: %s\n     got:  %s"
                     % (MIGRATION, ROOMS, found))

    # The page must not carry a fourth copy — it reads the list from the data
    # layer. A hard-coded <option> list is how the dropdown and the constraint
    # come apart without either file being touched.
    page = read(PAGE)
    if page is not None:
        hard = [r for r in ROOMS if ('"%s"' % r) in page or ("'%s'" % r) in page]
        if len(hard) > 2:
            fail("rooms", "%s appears to hard-code the room list (%d of the "
                          "codes as literals). It must read "
                          "MrBadmusSeatingData.ROOMS." % (PAGE, len(hard)))


# ═════════════════════════════════════════════════════════════════════════
# 2 · no fixture data in anything that ships
# ═════════════════════════════════════════════════════════════════════════
def check_tells():
    targets = list(SHIPPED)

    out = os.path.join(REPO, "mrbadmus_site")
    if os.path.isdir(out):
        for root, _dirs, files in os.walk(out):
            for fn in files:
                if not fn.endswith((".html", ".js", ".css")):
                    continue
                if "seating" not in fn:
                    continue
                targets.append(os.path.relpath(os.path.join(root, fn), REPO))

    for rel in targets:
        body = read(rel)
        if body is None:
            continue
        for tell, what in TELLS:
            if tell in body:
                fail("tells", "%s contains %r — %s" % (rel, tell, what))


# ═════════════════════════════════════════════════════════════════════════
# 3 · the scanned photo is never persisted or logged
# ═════════════════════════════════════════════════════════════════════════
#
# Scoped to the room-scan handler rather than the whole file: the backend
# legitimately logs and writes elsewhere, and a repo-wide grep would either
# be noise or would have to be so narrow it caught nothing.
PERSIST = [
    (r"\bfs\.", "a filesystem call"),
    (r"\brequire\(['\"]fs['\"]\)", "a filesystem require"),
    (r"writeFile", "a file write"),
    (r"createWriteStream", "a file write"),
    (r"\.storage\b", "a Supabase storage call"),
    (r"\.upload\(", "an upload call"),
    (r"putObject", "an object-store write"),
]

# Names that would carry image bytes into a log line.
IMAGE_BINDINGS = r"(req\.body|imageBuffer|imageBase64|b64|base64Data|buf\b|buffer\b)"


def _scan_region(label, body):
    for pat, what in PERSIST:
        m = re.search(pat, body)
        if m:
            line = body[:m.start()].count("\n")
            fail("photo-privacy",
                 "%s contains %s (%r, ~line %d). The photo is held in memory "
                 "and discarded — it is never written, uploaded or stored."
                 % (label, what, m.group(0), line + 1))

    for m in re.finditer(r"console\.(log|info|warn|error)\(([^\n]*)", body):
        if re.search(IMAGE_BINDINGS, m.group(2)):
            line = body[:m.start()].count("\n")
            fail("photo-privacy",
                 "%s logs something that may carry image bytes (~line %d): %s"
                 % (label, line + 1, m.group(0)[:90]))


def check_photo_not_persisted():
    src = read(BACKEND)
    if src is None:
        fail("photo-privacy",
             "backend server.js not readable at %s — cannot prove the photo "
             "is not persisted. (This gate reads the backend repo by absolute "
             "path, as pool_ownership.py does.)" % BACKEND)
        return

    if "/api/room-scan" not in src:
        fail("photo-privacy", "backend has no /api/room-scan route to check")
        return

    start = src.index("/api/room-scan")
    # The handler ends where the next route begins.
    nxt = re.search(r"\napp\.(get|post|put|patch|delete|use)\(", src[start + 20:])
    end = start + 20 + (nxt.start() if nxt else len(src) - start - 20)
    _scan_region("the /api/room-scan handler", src[start:end])

    # ⚠️ The handler delegates its prompt and validation to a module. Scanning
    # only the route would leave everything the image is actually passed TO
    # unwatched, which is precisely where a stray write would live.
    helper = os.path.join(os.path.dirname(BACKEND), "room-scan.js")
    body = read(helper)
    if body is None:
        if "room-scan" in src and "require(" in src:
            fail("photo-privacy",
                 "server.js appears to require a room-scan module that is not "
                 "at %s — the gate cannot see the code the image is handed to."
                 % helper)
    else:
        _scan_region("room-scan.js", body)


# ═════════════════════════════════════════════════════════════════════════
# 4 · the unconfigured contract matches across the two repos
# ═════════════════════════════════════════════════════════════════════════
def check_unconfigured_contract():
    fe = read(PHOTO_JS)
    if fe is None:
        fail("degrade", "%s is missing" % PHOTO_JS)
    elif UNCONFIGURED not in fe:
        fail("degrade", "%s does not test for %r — the honest degrade cannot "
                        "fire." % (PHOTO_JS, UNCONFIGURED))

    be = read(BACKEND)
    if be is None:
        fail("degrade", "backend not readable; cannot confirm %r is emitted"
             % UNCONFIGURED)
    elif UNCONFIGURED not in be:
        fail("degrade", "backend never emits %r — the frontend's degrade "
                        "branch is unreachable." % UNCONFIGURED)


# ═════════════════════════════════════════════════════════════════════════
# 5 · the dev harness never reaches the output tree
# ═════════════════════════════════════════════════════════════════════════
def check_harness_not_published():
    for rel in ("mrbadmus_site/" + HARNESS,
                "mrbadmus_site/teacher/" + HARNESS):
        if os.path.exists(os.path.join(REPO, rel)):
            fail("harness", "%s is published. It is a canvas workbench and "
                            "carries placeholder seat labels by design." % rel)


def check_files_present():
    """
    A gate that goes green because the thing it watches is not there yet is
    worse than no gate: it reports a clean surface it never looked at. Every
    file this gate reasons about is named here, and a missing one is a finding.
    """
    for rel in SHIPPED + [MIGRATION, HARNESS]:
        if not os.path.exists(os.path.join(REPO, rel)):
            fail("present", "%s is missing — this gate's other checks cannot "
                            "see it." % rel)


def main():
    check_files_present()
    check_rooms()
    check_tells()
    check_photo_not_persisted()
    check_unconfigured_contract()
    check_harness_not_published()

    print("seating_tells — MRB-322")
    print("  present        every watched file exists")
    print("  rooms          the dropdown, the CHECK and this file agree")
    print("  tells          no harness or rehearsal data in anything shipped")
    print("  photo-privacy  the scanned image is never written or logged")
    print("  degrade        photo_scan_unconfigured matches across both repos")
    print("  harness        the canvas workbench is not published")
    print()

    if not findings:
        print("✅ clean — 5 checks, 0 findings")
        return 0

    by_check = {}
    for check, detail in findings:
        by_check.setdefault(check, []).append(detail)
    for check in sorted(by_check):
        print("❌ %s" % check)
        for d in by_check[check]:
            print("   • %s" % d)
    print()
    print("%d finding(s)" % len(findings))
    return 1


if __name__ == "__main__":
    sys.exit(main())
