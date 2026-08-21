#!/usr/bin/env python3
"""student_shots.py — photograph the wired student pages, carrying REAL data.

    MRB_DRIVE_EMAIL=… MRB_DRIVE_PASSWORD=… python3 student_shots.py

Writes four PNGs into `docs/ks3/shots/` with plain, dated names:

    class-390-<date>.png        class-1460-<date>.png
    assignment-390-<date>.png   assignment-1460-<date>.png

── WHY THIS EXISTS AS ITS OWN SCRIPT ────────────────────────────────────

`student_page_drive.py` is a GATE: it asserts and it exits non-zero. This is a
DELIVERABLE: Mide has to be able to look at the page, and the last two runs
both turned on something a text check could not see and a picture could. On
21 August the docket told a student the wrong number of questions and the wrong
due date while the automated check reported the page clean, because the list of
tells held names and no numbers. The screenshot is not decoration next to the
gate; it is the instrument that caught the gate being wrong.

Keeping them separate means a red gate still produces pictures to look at,
which is exactly the morning when they are most wanted.

⚠️ `?env=prod` is not optional. `shared/config.js` deliberately selects the TEST
Supabase project on localhost, so without it the guard finds no session under
the test project's storage key and bounces to /auth.html — a signed-out page,
photographed, which looks like a broken build.
"""

import datetime
import json
import os
import sys

import ks3_browser as cdp
import student_page_drive as drive

SHOTS = os.path.join("docs", "ks3", "shots")
PAGES = [
    ("class", "/student/class-ported.html"),
    ("assignment", "/student/assignment-ported.html"),
]
# The two widths Mide is asked to look at: a phone, and the desktop the
# parity gate already measures at.
WIDTHS = [390, 1460]


def main():
    stamp = os.environ.get("MRB_SHOT_DATE") or datetime.date.today().isoformat()
    os.makedirs(SHOTS, exist_ok=True)

    key = drive.anon_key()
    sess = drive.sign_in(key)
    print("\n📸  student_shots — the wired pages, with real data\n")
    print("     signed in as %s (token %s…)"
          % (drive.EMAIL, sess["access_token"][:8]))

    server, port = cdp.serve("mrbadmus_site", port=drive.PORT + 1)
    written = []
    try:
        with cdp.Browser() as b:
            # Let the SDK persist the session in whatever shape its version
            # uses — see the long note in student_page_drive.py.
            p = b.page("http://localhost:%d/leaderboard.html?env=prod" % port,
                       settle=2.0)
            ok = p.eval("""
              (async function () {
                if (!window.supabase) return 'no sdk';
                var c = window.supabase.createClient(%s, %s);
                var r = await c.auth.setSession({
                  access_token: %s, refresh_token: %s });
                if (r.error) return 'error: ' + r.error.message;
                var g = await c.auth.getSession();
                return g.data.session ? 'ok' : 'no session';
              })()
            """ % (json.dumps(drive.SUPABASE_URL), json.dumps(key),
                   json.dumps(sess["access_token"]),
                   json.dumps(sess["refresh_token"])))
            print("     browser session: %s" % ok)
            if not str(ok).startswith("ok"):
                raise SystemExit("could not sign the browser in: %s" % ok)

            for name, path in PAGES:
                url = "http://localhost:%d%s?env=prod" % (port, path)
                for w in WIDTHS:
                    # A fresh page per width. Re-using one and resizing leaves
                    # the previous layout's measured values in component state,
                    # and the page reads its own width on mount.
                    page = b.page(url, settle=4.0)
                    page.set_viewport(w, 900)
                    out = os.path.join(SHOTS, "%s-%d-%s.png" % (name, w, stamp))
                    page.screenshot(out, width=w)
                    text = (page.eval("document.body.innerText") or "")
                    errs = page.console_errors()

                    # A photograph of an error message is still a photograph.
                    # Say which it is, in the run output, rather than leaving
                    # somebody to open the file and find out.
                    verdict = "renders"
                    for say in ("could not load", "not ready yet",
                                "No work has been set", "not in a class"):
                        if say.lower() in text.lower():
                            verdict = "EMPTY STATE — %r" % say
                    leaked = [t for t in drive.FIXTURE_TELLS if t in text]
                    print("     %-11s %4dpx  %-28s %s%s"
                          % (name, w, verdict,
                             "%d chars" % len(text),
                             ("  ⚠️ leaked: " + ", ".join(leaked[:4])) if leaked else ""))
                    if errs:
                        print("                 console: %s" % errs[0][:100])
                    written.append(out)
    finally:
        server.shutdown()

    print("\n     %d written:" % len(written))
    for w in written:
        print("       %s  (%d KB)" % (w, os.path.getsize(w) // 1024))
    print()


if __name__ == "__main__":
    main()
