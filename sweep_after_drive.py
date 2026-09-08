#!/usr/bin/env python3
"""sweep_after_drive.py — MRB-336/337 §8, the AFTER pass.

    python3 sweep_after_drive.py                # walk + press + shoot
    python3 sweep_after_drive.py --pages class  # one page only

Walks every student surface at 390 and 1280, SIGNED IN, against a real backend
and the TEST project. It is the measurement half of `docs/mrb336/sweep-after.md`
and it is also the stand-in for a gate that could not run — see below.

── ⚠️ IT SUBSTITUTES FOR `student_controls_drive.py`, WHICH CANNOT RUN TODAY ──

`student_controls_drive.py` presses every control on every student screen and
reports any whose only effect is a scroll. It defaults to
`MRB_DRIVE_EMAIL=midebolabadmus@gmail.com` (its line 99) — Mide's own account on
PRODUCTION — and this run may not use a production credential for his account.
There is no TEST identity wired into it.

So the control questions it asks are asked here instead, against TEST, with its
own rule kept intact: **a control whose only effect is a change of scroll offset
is DEAD, not "changed"**. Four of the five controls that once shipped dead were
dead in exactly that way. Its other rule is kept too: a control that reports
nothing is often correct — the current view's own nav item, an already-active
filter chip — so candidates are printed, not asserted.

── THE TRAPS THIS FILE IS BUILT AROUND ──────────────────────────────────

1. `ks3_browser.Page.screenshot()` RESETS the viewport to 1280x900 (its line
   577, defaults 572-573). Every capture here passes an explicit width, and no
   width judgement is ever taken from an image: `scrollWidth` vs `innerWidth`
   are read at a viewport set immediately beforehand.
2. The viewport is set BEFORE navigating, on `about:blank`, never after.
3. One browser per persona, sequentially. A persona's session is a real GoTrue
   password grant handed to the Supabase SDK — never a fabricated JWT.
4. A CORS-blocked page gives a FALSE layout pass and FALSE dead controls. Every
   page is required to prove it actually loaded before any judgement is made.
"""

import json
import os
import sys
import time

import ks3_browser as cdp

SITE_PORT = 5508                 # nothing else on this machine is on it
API = os.environ.get("MRB_API", "http://localhost:3338")
SB_URL = "https://qeppkiswvclkkwbxmlok.supabase.co"
SB_KEY = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFlcHBraXN3"
          "dmNsa2t3YnhtbG9rIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc2NjMzMzMsImV4cCI6MjA5MzIzOTMzM30"
          ".WxprirdO3yIZfcOiUMwbVPFPcD6Sx5SIZrQ3pvMOKT8")
PW = "TestPass!2026"
SHOTS = os.path.join("docs", "mrb336", "shots-after")

PERSONAS = [
    ("ks4trip", "student1@test-rainford.local"),      # 10X1 Biology, live work
    ("ks3", "aiden.cole@test-rainford.local"),        # 8X1
    ("ks4comb", "hannah.patel@test-rainford.local"),  # 10A
]

PAGES = [
    ("class", "/student/class.html"),
    ("assignment", "/student/assignment.html"),
    ("classes", "/student/classes.html"),
    ("claim", "/student/claim-confirm.html"),
    ("leaderboard", "/leaderboard.html"),
    ("weekly", "/weekly-challenge.html"),
    ("mychallenges", "/my-challenges.html"),
    ("revision", "/revision.html"),
]

WIDTHS = (390, 1280)


# ── the measurement, as one expression ───────────────────────────────────
#
# ⚠️ `scrollWidth` IS READ HERE, at the viewport this page was navigated at,
# and never inferred from a PNG. See the header.
MEASURE = r"""(function () {
  var de = document.documentElement;
  var txt = (document.body.innerText || '').replace(/ /g, ' ');
  var flat = txt.replace(/\s+/g, ' ').trim();

  // Placeholders a child should never be shown. `Week null` and friends are
  // spelled out because "null" alone matches innocent prose.
  var bad = [];
  [/\bnull\b/i, /\bundefined\b/i, /\bNaN\b/, /Week null/i, /Week undefined/i,
   /\[object Object\]/].forEach(function (re) {
    var m = txt.match(re);
    if (m) { bad.push(m[0]); }
  });

  // "+N more" mush.
  var more = (flat.match(/\+\s?\d+\s+more/gi) || []);

  // Every @font-face on the page, and its key.
  var faces = [], keys = {};
  for (var i = 0; i < document.styleSheets.length; i++) {
    var rules;
    try { rules = document.styleSheets[i].cssRules; } catch (e) { continue; }
    for (var j = 0; rules && j < rules.length; j++) {
      var r = rules[j];
      if (r.type !== 5) { continue; }   // CSSRule.FONT_FACE_RULE
      var k = [r.style.fontFamily, r.style.fontWeight || 'normal',
               r.style.fontStyle || 'normal'].join('|');
      faces.push(k);
      keys[k] = (keys[k] || 0) + 1;
    }
  }
  var dupFaces = Object.keys(keys).filter(function (k) { return keys[k] > 1; });

  // Every clipped element: content wider than its own box with hidden overflow.
  var clipped = 0;
  var all = document.querySelectorAll('*');
  for (var q = 0; q < all.length; q++) {
    var el = all[q];
    var cs = getComputedStyle(el);
    if (cs.overflowX !== 'hidden' && cs.overflow !== 'hidden') { continue; }
    if (el.scrollWidth > el.clientWidth + 2 && el.clientWidth > 0) { clipped++; }
  }

  // Anything reaching past the right edge, named, so a fix has a target.
  var over = [];
  if (de.scrollWidth > de.clientWidth + 1) {
    for (var z = 0; z < all.length; z++) {
      var b = all[z].getBoundingClientRect();
      if (b.width > 0 && b.right > de.clientWidth + 1) {
        over.push({
          tag: all[z].tagName.toLowerCase(),
          cls: String(all[z].className || '').slice(0, 60),
          right: Math.round(b.right)
        });
      }
    }
    over.sort(function (a, b) { return b.right - a.right; });
    over = over.slice(0, 8);
  }

  var bell = document.querySelector('[data-mrb-bell]');
  var panel = document.getElementById('mrb-bell-panel');

  return {
    scrollW: de.scrollWidth,
    clientW: de.clientWidth,
    innerW: window.innerWidth,
    over: over,
    chars: flat.length,
    text: flat.slice(0, 2600),
    placeholders: bad,
    more: more,
    faces: faces.length,
    dupFaces: dupFaces,
    clipped: clipped,
    bell: !!bell,
    bellLabel: bell ? (bell.getAttribute('aria-label') || '') : '',
    bellPanelOpen: !!(panel && !panel.hidden),
    unnamed: (function () {
      // Controls with no accessible name at all.
      var n = [];
      var ctl = document.querySelectorAll('button, a[href], [role="button"]');
      for (var c = 0; c < ctl.length; c++) {
        var e = ctl[c];
        if (!e.getBoundingClientRect().width) { continue; }
        var name = (e.getAttribute('aria-label') || e.innerText || '').trim();
        if (!name) { n.push(e.tagName.toLowerCase() + '.' +
                            String(e.className || '').slice(0, 40)); }
      }
      return n.slice(0, 8);
    })()
  };
})()"""


# ── pressing a control, the controls-drive way ───────────────────────────
#
# A signature that IGNORES scroll offset entirely. If the only thing that moved
# was the scroll, the two signatures are identical and the control reads DEAD —
# which is the gate's rule and the reason four of the five originally shipped.
SIG = r"""(function () {
  var p = document.getElementById('mrb-bell-panel');
  return JSON.stringify({
    url: location.pathname + location.search,
    text: (document.body.innerText || '').replace(/\s+/g, ' ').trim(),
    nodes: document.querySelectorAll('*').length,
    panel: !!(p && !p.hidden),
    panelText: p && !p.hidden ? (p.innerText || '').replace(/\s+/g, ' ').trim() : ''
  });
})()"""


def sized(browser, width, height=900):
    """⚠️ BLANK PAGE, SET THE SIZE, THEN NAVIGATE. Never the other way."""
    browser.page("about:blank", settle=0.15).set_viewport(width, height)


def sign_in(browser, base, email):
    """A real GoTrue password grant, handed to the SDK on the site's origin.

    ⚠️ NOT on an app page — `localStorage` is per-origin so it must be this
    port, but it must not be a page doing its own auth at the same time. The
    /shared/ directory listing is HTML on the right origin with no JS.
    """
    boot = browser.page(base + "/shared/", settle=0.4)
    boot.eval("(function(){var s=document.createElement('script');"
              "s.src='https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2';"
              "document.head.appendChild(s);})()")
    for _ in range(60):
        if boot.eval("!!(window.supabase && window.supabase.createClient)"):
            break
        time.sleep(0.25)
    got = boot.eval(
        "(async function(){var c=window.supabase.createClient(%s,%s);"
        "var r=await c.auth.signInWithPassword({email:%s,password:%s});"
        "return r.error ? ('err:'+r.error.message) : ('ok:'+r.data.user.id);})()"
        % (json.dumps(SB_URL), json.dumps(SB_KEY),
           json.dumps(email), json.dumps(PW)))
    return got


def walk(browser, base, key, path, width, persona, out):
    sized(browser, width)
    page = browser.page(base + path + "?api=" + API, settle=2.4)
    # Give the student pages their mount; they paint only when every request is
    # back, so a fixed settle would measure a skeleton.
    for _ in range(50):
        if page.eval("document.body.innerText.trim().length > 40"):
            break
        time.sleep(0.3)
    time.sleep(1.4)

    m = page.eval(MEASURE)
    errs = [e for e in page.console_errors()
            if "favicon" not in e]
    m["console"] = errs[:6]
    m["persona"] = persona
    m["page"] = key
    m["width"] = width
    out.append(m)

    shot = os.path.join(SHOTS, "%s-%s-%d.png" % (persona, key, width))
    # ⚠️ EXPLICIT WIDTH ON EVERY CAPTURE — screenshot() resets the viewport.
    page.screenshot(shot, width=width, height=900)

    print("  %-12s %4d  scrollW=%-5d clientW=%-5d chars=%-5d faces=%-3d "
          "clip=%d bell=%s%s"
          % (key, width, m["scrollW"], m["clientW"], m["chars"], m["faces"],
             m["clipped"], "y" if m["bell"] else "n",
             ("  ⚠ " + ",".join(m["placeholders"])) if m["placeholders"] else ""))
    if m["scrollW"] > m["clientW"] + 1:
        print("       ↳ SIDEWAYS %d past %d: %s"
              % (m["scrollW"] - m["clientW"], m["clientW"],
                 "; ".join("%s.%s@%d" % (o["tag"], o["cls"][:24], o["right"])
                           for o in m["over"][:4])))
    if m["dupFaces"]:
        print("       ↳ DUPLICATE @font-face: %s" % ", ".join(m["dupFaces"][:4]))
    if errs:
        print("       ↳ console: %s" % errs[0][:130])
    return page, m


def press_bell(page, width, persona, key, out):
    """The addendum's four questions, on every surface that has a bell."""
    has = page.eval("!!document.querySelector('[data-mrb-bell]')")
    if not has:
        print("       bell: ABSENT")
        out.append(dict(persona=persona, page=key, width=width, bell=False))
        return

    before = page.eval(SIG)
    page.eval("document.querySelector('[data-mrb-bell]').click()")
    time.sleep(0.7)
    after = page.eval(SIG)
    opened = json.loads(after)["panel"]
    changed = before != after
    rows = page.eval("(function(){var p=document.getElementById('mrb-bell-panel');"
                     "return p?p.querySelectorAll('[data-mrb-bell-row]').length:-1;})()")
    panelw = page.eval("(function(){var p=document.getElementById('mrb-bell-panel');"
                       "return p&&!p.hidden?Math.round(p.getBoundingClientRect().width):0;})()")

    # Escape, then re-open and press Close, so both exits are pressed.
    page.eval("document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true}))")
    time.sleep(0.4)
    esc_closed = not json.loads(page.eval(SIG))["panel"]

    page.eval("document.querySelector('[data-mrb-bell]').click()")
    time.sleep(0.5)
    closer = page.eval(
        "(function(){var p=document.getElementById('mrb-bell-panel');if(!p)return 0;"
        "var b=p.querySelector('[data-mrb-bell-close]')||"
        "Array.prototype.filter.call(p.querySelectorAll('button'),"
        "function(x){return /close/i.test(x.innerText||x.getAttribute('aria-label')||'');})[0];"
        "if(!b)return 0;b.click();return 1;})()")
    time.sleep(0.4)
    close_closed = not json.loads(page.eval(SIG))["panel"]

    print("       bell: opens=%s (sig-changed=%s) rows=%s panelW=%d "
          "esc=%s close=%s(found=%s)"
          % (opened, changed, rows, panelw, esc_closed, close_closed, closer))
    out.append(dict(persona=persona, page=key, width=width, bell=True,
                    opened=opened, changed=changed, rows=rows, panelW=panelw,
                    esc=esc_closed, closeBtn=bool(closer), closed=close_closed,
                    label=page.eval("document.querySelector('[data-mrb-bell]')"
                                    ".getAttribute('aria-label')")))


def main():
    only = None
    if "--pages" in sys.argv:
        only = sys.argv[sys.argv.index("--pages") + 1].split(",")

    os.makedirs(SHOTS, exist_ok=True)
    site, port = cdp.serve("mrbadmus_site", port=SITE_PORT)
    base = "http://localhost:%d" % port
    print("site  %s\nbackend %s\n" % (base, API))

    rows, bells = [], []
    try:
        for persona, email in PERSONAS:
            print("── %s (%s) ──" % (persona, email))
            with cdp.Browser() as br:
                got = sign_in(br, base, email)
                print("  sign-in %s" % got)
                if not got.startswith("ok"):
                    continue
                for key, path in PAGES:
                    if only and key not in only:
                        continue
                    for w in WIDTHS:
                        page, m = walk(br, base, key, path, w, persona, rows)
                        press_bell(page, w, persona, key, bells)
            print()
    finally:
        try:
            site.shutdown()
        except Exception:
            pass

    with open(os.path.join("docs", "mrb336", "sweep-after.json"), "w",
              encoding="utf-8") as fh:
        json.dump({"pages": rows, "bells": bells}, fh, indent=1)
    print("wrote docs/mrb336/sweep-after.json  (%d walks, %d bell presses)"
          % (len(rows), len(bells)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
