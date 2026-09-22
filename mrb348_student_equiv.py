#!/usr/bin/env python3
"""
mrb348_student_equiv.py — the student class page renders the SAME PAGE after
the load-order change as before it.

    MRB_TEST_TEACHER_PASSWORD=… python3 mrb348_student_equiv.py --capture new
    MRB_TEST_TEACHER_PASSWORD=… python3 mrb348_student_equiv.py --capture old
    python3 mrb348_student_equiv.py --compare

WHY A DRIVE AND NOT `student_behaviour`

`student_behaviour.py` is green on this change and cannot have been anything
else: it drives `student/class-fixture.html`, whose data is BAKED IN by
`build_student_port.py`. MRB-348 changes when the page's reads leave and which
class it speculates on — neither of which a fixture with no network exercises.
A gate that passes without looking is not evidence, and CLAUDE.md's own note
about `student_parity` not watching the ported page is the same lesson.

So this signs in as real students on TEST, loads the real page, and compares
the rendered TEXT and the CONTROL set, which is the same bar
`student_behaviour` holds the fixture to.

THE THREE CASES, and the third is the one that matters

  1. KS3, own class named in `?class=`      — the ordinary journey
  2. KS4, own class named in `?class=`      — the longest work list on TEST
  3. KS3 student, ANOTHER student's class id in `?class=` — the RULED path
     (23 Aug 2026): the student is shown THEIR OWN class, silently, with the
     parameter dropped from the address. No banner, no message. This is the
     behaviour the speculative build could plausibly break, because it is the
     one case where the speculation must be thrown away unused — so it is
     asserted explicitly, including the final URL.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp  # noqa: E402

TEST_REF = "qeppkiswvclkkwbxmlok"
URL = "https://%s.supabase.co" % TEST_REF
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
PORT = 5537
OUT = os.environ.get("MRB_SHOTS") or os.path.expanduser("~/tmp/ks3-gates")

KS3_CLASS = "2a000000-0000-0000-0000-000000000001"   # 8X1, Aiden's
KS4_CLASS = "2a000000-0000-0000-0000-000000000002"   # 10A, Hannah's

CASES = [
    dict(key="ks3-own", who="aiden.cole@test-rainford.local",
         q="?class=" + KS3_CLASS,
         expect_param=KS3_CLASS,
         note="KS3 8X1, the student's own class"),
    dict(key="ks4-own", who="hannah.patel@test-rainford.local",
         q="?class=" + KS4_CLASS,
         expect_param=KS4_CLASS,
         note="KS4 10A, the student's own class"),
    dict(key="ks3-foreign", who="aiden.cole@test-rainford.local",
         q="?class=" + KS4_CLASS,
         expect_param=None,
         note="RULED: a class that is NOT this student's — own class, "
              "parameter dropped, nothing said"),
]


def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def sign_in(email, key, pw):
    req = urllib.request.Request(
        URL + "/auth/v1/token?grant_type=password",
        data=json.dumps({"email": email, "password": pw}).encode(),
        headers={"apikey": key, "Content-Type": "application/json"},
        method="POST")
    return json.load(urllib.request.urlopen(req, timeout=30, context=CTX))


def put_session(page, base, sess):
    payload = json.dumps({
        "access_token": sess["access_token"],
        "refresh_token": sess.get("refresh_token", ""),
        "expires_at": int(time.time()) + int(sess.get("expires_in", 3600)),
        "expires_in": int(sess.get("expires_in", 3600)),
        "token_type": "bearer", "user": sess["user"],
    })
    page.goto(base + "/student/class.html", settle=0.2)
    page.eval("localStorage.setItem(%s, %s)"
              % (json.dumps("sb-%s-auth-token" % TEST_REF), json.dumps(payload)))


READY = """(function(){
    var h = document.querySelector('[data-port-region], #mrb-student, main');
    if (!h) { return false; }
    if (document.querySelector('.skeleton, [data-skeleton]')) { return false; }
    return (h.textContent||'').trim().length > 80;
})()"""

# Visible text and the control set — the same two things `student_behaviour`
# compares, so a difference here means the same kind of difference it would
# have caught had it been able to see this page.
SNAP = """(function(){
    var h = document.querySelector('[data-port-region], #mrb-student, main')
            || document.body;
    var txt = (h.innerText || h.textContent || '')
              .replace(/\\s+/g, ' ').trim();
    var ctl = [];
    var nodes = h.querySelectorAll(
        'button, a, input, select, textarea, [role=button], [tabindex]');
    for (var i = 0; i < nodes.length; i++) {
        var n = nodes[i];
        ctl.push((n.tagName || '') + '|' +
                 ((n.innerText || n.value || n.getAttribute('aria-label') || '')
                   .replace(/\\s+/g,' ').trim().slice(0, 60)));
    }
    return { text: txt, controls: ctl, nodes: h.querySelectorAll('*').length,
             url: window.location.search };
})()"""


def capture(tag, pw):
    """
    ⚠️ A WARM-UP LOAD PER CASE, AND IT IS NOT OPTIONAL.

    Auto-composition is LAZY: the weekly assignment is composed by the backend
    on the FIRST class-page read of the week, not by a cron. So the first load
    of a class CREATES a piece of work that every later load then sees.

    Run without this, the two captures are not comparable and the difference
    is spectacular and entirely false: whichever side ran FIRST composed the
    assignment, and the side that ran SECOND reported one extra piece of work,
    a different `COMPLETED n/m`, and an extra filter button. It read exactly
    like a real regression in the load path — `COMPLETED 4/5` against
    `COMPLETED 4/4`, a whole `TO DO 1` gone — and it was the harness.

    One discarded load per case first, then the measured one. Both sides then
    observe the same composed world.
    """
    key = anon_key()
    server, port = cdp.serve("mrbadmus_site", PORT)
    base = "http://127.0.0.1:%d" % port
    snaps, who = {}, None
    try:
        with cdp.Browser() as b:
            page = b.attach()
            for c in CASES:
                if c["who"] != who:
                    put_session(page, base, sign_in(c["who"], key, pw))
                    who = c["who"]
                # The discarded warm-up. See the note above: it is what makes
                # the two captures describe the same world.
                page.goto(base + "/student/class.html" + c["q"], settle=0.3)
                warm = time.time() + 40
                while time.time() < warm:
                    try:
                        if page.eval(READY, timeout=5) is True:
                            break
                    except Exception:
                        pass
                    time.sleep(0.08)

                page.goto(base + "/student/class.html" + c["q"], settle=0.3)
                end = time.time() + 40
                ok = False
                while time.time() < end:
                    try:
                        if page.eval(READY, timeout=5) is True:
                            ok = True
                            break
                    except Exception:
                        pass
                    time.sleep(0.08)
                if not ok:
                    snaps[c["key"]] = {"error": "never mounted"}
                    print("  ❌ %-13s never mounted" % c["key"])
                    continue
                time.sleep(0.6)          # let any post-mount work settle
                s = page.eval(SNAP, timeout=15)
                snaps[c["key"]] = s
                print("  ✅ %-13s %6d chars, %3d controls, %4d nodes, url=%r"
                      % (c["key"], len(s["text"]), len(s["controls"]),
                         s["nodes"], s["url"]))
    finally:
        try:
            server.shutdown()
        except Exception:
            pass
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "mrb348_student_%s.json" % tag)
    with open(path, "w") as fh:
        json.dump(snaps, fh, indent=2)
    print("  wrote %s" % path)
    return snaps


def compare():
    fails = []
    a = json.load(open(os.path.join(OUT, "mrb348_student_old.json")))
    b = json.load(open(os.path.join(OUT, "mrb348_student_new.json")))
    print("\n  comparing OLD (before MRB-348) with NEW (after)\n")
    for c in CASES:
        k = c["key"]
        oldc, newc = a.get(k, {}), b.get(k, {})
        print("  %s — %s" % (k, c["note"]))
        if oldc.get("error") or newc.get("error"):
            fails.append("%s: %s / %s" % (k, oldc.get("error"), newc.get("error")))
            print("     ❌ %s / %s" % (oldc.get("error"), newc.get("error")))
            continue
        same_text = oldc.get("text") == newc.get("text")
        same_ctl = oldc.get("controls") == newc.get("controls")
        print("     %s visible text   (%d vs %d chars)"
              % ("✅" if same_text else "❌",
                 len(oldc.get("text", "")), len(newc.get("text", ""))))
        print("     %s control set    (%d vs %d)"
              % ("✅" if same_ctl else "❌",
                 len(oldc.get("controls", [])), len(newc.get("controls", []))))
        if not same_text:
            fails.append(k + ": visible text differs")
            ot, nt = oldc.get("text", ""), newc.get("text", "")
            for i in range(min(len(ot), len(nt))):
                if ot[i] != nt[i]:
                    print("        first difference at char %d:" % i)
                    print("        old …%s…" % ot[max(0, i-60):i+60])
                    print("        new …%s…" % nt[max(0, i-60):i+60])
                    break
            else:
                print("        one is a prefix of the other")
        if not same_ctl:
            fails.append(k + ": control set differs")
            so, sn = set(oldc.get("controls", [])), set(newc.get("controls", []))
            for x in sorted(so - sn)[:6]:
                print("        only OLD: %s" % x)
            for x in sorted(sn - so)[:6]:
                print("        only NEW: %s" % x)

        # The ruled address behaviour, asserted on its own rather than folded
        # into the text comparison — a wrong URL is invisible in innerText and
        # is exactly what the 23 Aug ruling is about.
        want = c["expect_param"]
        got_old, got_new = oldc.get("url", ""), newc.get("url", "")
        def has(u):
            return (re.search(r"class=([0-9a-f-]{36})", u or "") or [None, None])[1] \
                if re.search(r"class=([0-9a-f-]{36})", u or "") else None
        po, pn = has(got_old), has(got_new)
        ok_old, ok_new = (po == want), (pn == want)
        print("     %s address        old=%r new=%r (ruled: %s)"
              % ("✅" if (ok_old and ok_new) else "❌", got_old, got_new,
                 want or "no class parameter"))
        if not (ok_old and ok_new):
            fails.append(k + ": address parameter wrong")
        print()

    if fails:
        print("  ❌ %d difference(s):" % len(fails))
        for f in fails:
            print("     · %s" % f)
        return 1
    print("  ✅ every case renders the same visible text, the same controls, "
          "and the same address.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture", choices=["old", "new"])
    ap.add_argument("--compare", action="store_true")
    a = ap.parse_args()
    if a.capture:
        pw = os.environ.get("MRB_TEST_TEACHER_PASSWORD")
        if not pw:
            raise SystemExit("$MRB_TEST_TEACHER_PASSWORD is not set.")
        print("capturing %s" % a.capture.upper())
        capture(a.capture, pw)
        return 0
    if a.compare:
        return compare()
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
