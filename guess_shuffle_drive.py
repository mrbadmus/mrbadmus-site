#!/usr/bin/env python3
"""guess_shuffle_drive.py — the "If you had to guess" options really do swap places.

Mide's ruling (17 Oct 2026): the two Start-here options are authored in a
fixed order, so POSITION could carry the answer. Every live KS4 opener
(ks4_rulings.py R20, one place, the compiled Ks4Guess block) and every KS3
opener (shared/ks3.js `shuffleGuess`) now shows them in a random order, once
per page load.

Other gates compare the pair as UNORDERED (ks4_parity's R18 check). This is
the gate that proves the shuffle is real and harmless. For three pages — a KS4
lesson on a Code-authored record (carbon-cycle), a KS4 lesson authored by
Design on Ks4Guess (ph-scale, batch 11) and a KS3 lesson (using-a-microscope):

  1. FORCED ORDER. With `window.MRB_GUESS_FLIP` = false then true (the test
     hook; absent in production, where it is Math.random()) the two cards
     appear in opposite orders: the first card's text under `true` is the
     second card's under `false`.
  2. REPLY FOLLOWS THE OPTION. Pressing a card, under each order, shows the
     reply that belongs to THAT option (text -> reply is the same map under
     both orders), and the "Good guess." / "The answer" mark lands on the same
     option text under both orders. On the two pages with an authored record
     the map is also checked against the record itself.
  3. UNFORCED IS RANDOM. With no hook, 16 plain loads show BOTH orders
     (a fair coin misses one in 2^15 runs, i.e. 1 in 32,768).
  4. KS3 only: the A / B badge follows position (A first, B second), each
     button keeps its authored `data-i`, and the four-option verdict block in
     the same lesson is not reordered.

Run:  python3 guess_shuffle_drive.py
"""

import json
import os
import sys
import time

import ks3_browser as cdp

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "mrbadmus_site")

KS4_A = "/combined/foundation/biology/ecology/carbon-cycle.html"      # record: correct first
KS4_B = "/combined/foundation/chemistry/chemical-changes/ph-scale.html"  # Design's own Ks4Guess
KS3 = "/ks3/biology/cells-and-organisation/using-a-microscope.html"

FAILS = []


def fail(msg):
    FAILS.append(msg)
    print("  FAIL  " + msg)


def ok(msg):
    print("  ok    " + msg)


# ── in-page readers ───────────────────────────────────────────────────────
KS4_READ = r"""
(function () {
  var s = document.querySelector('#s-hook');
  if (!s) { return null; }
  var b = Array.prototype.slice.call(s.querySelectorAll('button'));
  if (b.length !== 2) { return null; }
  return b.map(function (x) {
    var sp = x.querySelectorAll('span');
    return { text: sp[sp.length - 1].textContent.trim() };
  });
})()
"""
KS4_REPLY = r"""
(function () {
  var s = document.querySelector('#s-hook');
  var r = s.querySelector('[role="status"]');
  var answered = Array.prototype.slice.call(s.querySelectorAll('button')).filter(function (x) {
    return /The answer/.test(x.textContent);
  }).map(function (x) { var sp = x.querySelectorAll('span'); return sp[sp.length - 1].textContent.trim(); });
  return { reply: r ? r.textContent.trim() : null, answer: answered };
})()
"""
KS3_READ = r"""
(function () {
  var ul = document.querySelector('#s-hook ul[data-shuffle]');
  if (!ul) { return null; }
  return Array.prototype.slice.call(ul.children).map(function (li) {
    var b = li.querySelector('button');
    return { i: b.getAttribute('data-i'), mark: li.querySelector('.ks3-opt-mark').textContent.trim(),
             text: li.querySelector('.ks3-opt-label').textContent.trim() };
  });
})()
"""
KS3_REPLY = r"""
(function () {
  var r = document.querySelector('#s-hook .ks3-keyed-reply:not([hidden])');
  return r ? { i: r.getAttribute('data-reply'), reply: r.textContent.trim() } : null;
})()
"""
KS3_VERDICT_ORDER = r"""
(function () {
  var ul = document.querySelector('#s-verdict ul.ks3-options');
  return ul ? Array.prototype.slice.call(ul.querySelectorAll('button')).map(function (b) { return b.getAttribute('data-i'); }) : null;
})()
"""


def load(page, url, flip):
    """Fresh load. `flip` None = no hook (production behaviour)."""
    page.send("Page.addScriptToEvaluateOnNewDocument",
              {"source": "" if flip is None else "window.MRB_GUESS_FLIP = %s;" % json.dumps(flip)})
    page.goto(url, settle=0.6)


def wait_for(page, expr, tries=40):
    for _ in range(tries):
        v = page.eval(expr)
        if v:
            return v
        time.sleep(0.25)
    return None


def clear_hooks(page):
    # addScriptToEvaluateOnNewDocument scripts persist for the page; each load()
    # adds one that runs in order, so a later one overrides an earlier one. A
    # `None` load must therefore delete the flag explicitly.
    page.send("Page.addScriptToEvaluateOnNewDocument", {"source": "delete window.MRB_GUESS_FLIP;"})


def drive_ks4(b, base, path, label, record):
    print("\n%s  %s" % (label, path))
    seen = {}
    for flip in (False, True):
        for press in (0, 1):
            page = b.attach()
            page.set_viewport(390, 900)
            clear_hooks(page)
            load(page, base + path, flip)
            cards = wait_for(page, KS4_READ)
            if not cards:
                fail("%s: no two-card #s-hook (flip=%s)" % (label, flip))
                return
            seen[(flip, "order")] = [c["text"] for c in cards]
            page.eval("document.querySelectorAll('#s-hook button')[%d].click()" % press)
            time.sleep(0.4)
            got = page.eval(KS4_REPLY)
            seen[(flip, cards[press]["text"])] = (got["reply"], tuple(got["answer"]))
    a, c = seen[(False, "order")], seen[(True, "order")]
    if a != list(reversed(c)) or a[0] == a[1]:
        fail("%s: forced orders are not opposite (false=%r true=%r)" % (label, a, c))
    else:
        ok("forced orders are opposite: false=%s | true=%s" % (a[0][:28], c[0][:28]))
    for text in a:
        r0, r1 = seen[(False, text)], seen[(True, text)]
        if r0 != r1 or not r0[0]:
            fail("%s: pressing %r gave different replies by order: %r vs %r" % (label, text[:30], r0, r1))
    if all(seen[(False, t)] == seen[(True, t)] and seen[(False, t)][0] for t in a):
        ok("each option keeps its own reply and its 'The answer' mark under both orders")
    if record:
        right = [o["text"] for o in record["options"] if o["correct"]][0]
        for o in record["options"]:
            rep, ans = seen[(True, o["text"])]
            if o["reply"][:40] not in rep:
                fail("%s: reply for %r does not carry the authored reply" % (label, o["text"][:30]))
            if (right in ans) is not True:
                fail("%s: 'The answer' mark is not on the authored correct option" % label)
        ok("replies and the answer mark match ks4_lessons/start_here.py")
    # unforced
    firsts = set()
    page = b.attach()
    page.set_viewport(390, 900)
    clear_hooks(page)
    for _ in range(16):
        page.goto(base + path, settle=0.3)
        cards = wait_for(page, KS4_READ)
        if cards:
            firsts.add(cards[0]["text"])
        if len(firsts) == 2:
            break
    if len(firsts) == 2:
        ok("unforced loads show both orders")
    else:
        fail("%s: 16 unforced loads never showed both orders" % label)


def drive_ks3(b, base, path, label):
    from ks3_data import start_here as K
    rec = None
    for k, v in K.START_HERE.items():
        if path.endswith("/" + k + ".html"):
            rec = v
    print("\n%s  %s" % (label, path))
    outcomes = {}
    for flip in (False, True):
        page = b.attach()
        page.set_viewport(390, 900)
        clear_hooks(page)
        load(page, base + path, flip)
        cards = wait_for(page, KS3_READ)
        if not cards:
            fail("%s: no #s-hook ul[data-shuffle]" % label)
            return
        outcomes[flip] = [c["i"] for c in cards]
        if [c["mark"] for c in cards] != ["A", "B"]:
            fail("%s: badges do not read A, B by position (%r)" % (label, [c["mark"] for c in cards]))
        if page.eval(KS3_VERDICT_ORDER) not in (None, ["0", "1", "2", "3"]):
            fail("%s: the four-option verdict block was reordered" % label)
        for press in (0, 1):
            load(page, base + path, flip)
            cards = wait_for(page, KS3_READ)
            i = cards[press]["i"]
            page.eval("document.querySelectorAll('#s-hook ul[data-shuffle] button')[%d].click()" % press)
            time.sleep(0.3)
            got = page.eval(KS3_REPLY)
            if not got or got["i"] != i:
                fail("%s: pressing option data-i=%s showed reply %r" % (label, i, got))
            elif rec is not None:
                word = "Good guess." if int(i) == rec["answer"] else "Fair guess."
                if not got["reply"].startswith(word):
                    fail("%s: option %s should open %r, got %r" % (label, i, word, got["reply"][:20]))
    if outcomes[False] != ["0", "1"] or outcomes[True] != ["1", "0"]:
        fail("%s: forced orders wrong: false=%r true=%r" % (label, outcomes[False], outcomes[True]))
    else:
        ok("forced orders are opposite, A/B follow position, replies follow the option")
    firsts = set()
    page = b.attach()
    page.set_viewport(390, 900)
    clear_hooks(page)
    for _ in range(16):
        page.goto(base + path, settle=0.3)
        cards = wait_for(page, KS3_READ)
        if cards:
            firsts.add(cards[0]["i"])
        if len(firsts) == 2:
            break
    if len(firsts) == 2:
        ok("unforced loads show both orders")
    else:
        fail("%s: 16 unforced loads never showed both orders" % label)


def main():
    from ks4_lessons import start_here as SH
    server, port = cdp.serve(OUT)
    base = "http://127.0.0.1:%d" % port
    try:
        for p in (KS4_A, KS4_B, KS3):
            if not os.path.exists(OUT + p):
                print("missing built page %s — run build_all.py first" % p)
                return 2
        with cdp.Browser() as b:
            drive_ks4(b, base, KS4_A, "KS4 (record)", SH.START_HERE["carbon-cycle"])
            drive_ks4(b, base, KS4_B, "KS4 (Design's Ks4Guess)", None)
            drive_ks3(b, base, KS3, "KS3")
    finally:
        server.shutdown()
    print("\n%s" % ("FAILED: %d" % len(FAILS) if FAILS else "guess_shuffle_drive: all checks passed"))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
