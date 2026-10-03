#!/usr/bin/env python3
"""consumer_dash_drive.py — the family dashboard and account page, driven
OFFLINE in headless Chrome against `consumer_dash_fixture` (no backend, no
Supabase, no Stripe).

B2C repair, 3 Oct 2026 — proves Mide's seven rulings on screen:

  1  one checkout path: spinner only, no second press, gives up after 25s,
     a plain failure line under the control with "Try again" (or "Add a
     child" on no_children), the control restored — on the dashboard banner,
     the account page and the signup plan step;
  2  pre-trial: one line + "Start your free week"; Set work / message box /
     Send are not drawn; reset password, edit, pause, remove all work; no
     `disabled` attribute anywhere in the family dashboard at rest;
  3  a message from an earlier press is gone at the next press; no children
     → "Add a child", and no claim that children can sign in;
  4  B7: the family is re-read on a back/forward-cache restore and on
     returning to the tab; the account page lists every child's reports;
  5  delete: a text link at the very bottom → consequences + tick box →
     "Delete my account" beside "Keep my account" (focused) → scheduled +
     Undo, sending {confirm: 'DELETE'};
  6  the removed copy is gone.

    python3 consumer_dash_drive.py [--shots DIR] [--skip-timeout]

`--skip-timeout` skips the one 26-second wait (the hanging checkout).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)

import ks3_browser as cdp  # noqa: E402
import consumer_dash_fixture as fx  # noqa: E402

FAILS: list[str] = []


def check(ok, label, evidence=""):
    print(("  OK  " if ok else "  XX  ") + label +
          (("  — " + str(evidence)[:300]) if evidence not in ("", None) else ""))
    if not ok:
        FAILS.append(label)


POLL = (
    "function __poll(fn,t){return new Promise(function(ok,bad){var t0=Date.now();"
    "(function tick(){var v;try{v=fn();}catch(e){v=false;}if(v)return ok(v);"
    "if(Date.now()-t0>(t||5000))return bad(new Error('poll timeout'));"
    "setTimeout(tick,50);})();});}"
)


class Drive:
    def __init__(self, browser, port, shots):
        self.b = browser
        self.port = port
        self.shots = shots
        self.p = browser.attach()
        self.pre = None

    def open(self, path, width=390, theme="light", **fixture):
        p = self.p
        if self.pre is not None:
            p.send("Page.removeScriptToEvaluateOnNewDocument", {"identifier": self.pre})
        self.pre = p.send("Page.addScriptToEvaluateOnNewDocument",
                          {"source": fx.prescript(**fixture)}).get("identifier")
        p.set_viewport(width, 1400 if width > 500 else 1800)
        url = "http://127.0.0.1:%d/%s" % (self.port, path)
        p.goto(url)
        p.eval("try{localStorage.setItem('mrb-theme',%s)}catch(e){}" % json.dumps(theme))
        p.goto(url)
        self.wait("document.body.style.display==='block'&&"
                  "document.getElementById('c-main')&&"
                  "document.getElementById('c-main').children.length>0")
        time.sleep(0.2)

    def js(self, expr):
        return self.p.eval(expr)

    def wait(self, cond, timeout=6000):
        return self.p.eval("(async function(){" + POLL +
                           "return await __poll(function(){return (%s);},%d);})()"
                           % (cond, timeout), timeout=timeout / 1000 + 10)

    def click(self, selector):
        return self.js("(function(){var e=document.querySelector(%s);"
                       "if(!e)return false;e.click();return true;})()" % json.dumps(selector))

    def text(self, selector="body"):
        return self.js("(function(){var e=document.querySelector(%s);"
                       "return e?e.innerText:'';})()" % json.dumps(selector)) or ""

    def calls(self, path):
        return self.js("window.__CF__.calls.filter(function(c){return c.path===%s;})"
                       % json.dumps(path)) or []

    def shot(self, name, width=390):
        if not self.shots:
            return
        os.makedirs(self.shots, exist_ok=True)
        try:
            self.p.screenshot(os.path.join(self.shots, name), width=width,
                              height=1400 if width > 500 else 900)
        except Exception as e:  # noqa: BLE001
            print("  (screenshot %s failed: %s)" % (name, e))

    def disabled_count(self):
        return self.js("document.querySelectorAll('#dk-root [disabled]').length")


def pre_trial(d):
    print("\n── pre-trial, two children (dashboard) ──")
    for width in (390, 1280):
        d.open("consumer/overview.html", width=width, state="none", kids=2)
        body = d.text()
        check("Your family hasn’t started yet." in body,
              "@%d the one line says the family hasn't started" % width)
        check(d.js("document.querySelectorAll('.dk-gate [data-act=checkout]').length") == 1,
              "@%d the line's one action is a checkout control" % width)
        check("Start your free week" in d.text(".dk-gate"),
              "@%d …labelled Start your free week" % width)
        check(d.js("getComputedStyle(document.querySelector('.dk-gate')).display") != "none",
              "@%d the line is visible at this width" % width)
        check("Ada" in body and "Ben" in body, "@%d both children are on the dashboard" % width)
        check(d.disabled_count() == 0, "@%d no [disabled] on the overview" % width,
              d.disabled_count())
        d.shot("pretrial-overview-%d.png" % width, width)

    d.open("consumer/overview.html?child=kid-ada&view=child", state="none", kids=2)
    check(d.js("document.querySelectorAll('[data-write]').length") == 0,
          "child view draws no write control the backend refuses (Set work)")
    check(not d.js("!!document.querySelector('[data-act=open-setwork]')"),
          "no Set work button pre-trial")
    check(d.js("!!document.querySelector('[data-act=pause]')"), "Pause is there")
    check(d.disabled_count() == 0, "no [disabled] on the child view", d.disabled_count())
    check("set and waiting" not in d.text() and "waiting" not in d.text(".dk-card") ,
          "no claim the first week is waiting")
    d.shot("pretrial-child-390.png")

    d.click("[data-act=pause]")
    d.wait("document.body.innerText.indexOf('plan is paused')>=0")
    check(len(d.calls("/api/consumer/children/kid-ada/pause")) == 1,
          "Pause works pre-trial (one POST, success line)")

    d.open("consumer/overview.html?child=kid-ada&view=setwork", state="none", kids=2)
    check(d.js("new URLSearchParams(location.search).get('view')") in ("setwork", "child") and
          not d.js("!!document.querySelector('[data-act=submit-work]')"),
          "?view=setwork pre-trial shows no Set work form")

    d.open("consumer/overview.html?child=kid-ada&view=chat", state="none", kids=2)
    check(not d.js("!!document.getElementById('dk-draft')") and
          not d.js("!!document.querySelector('[data-act=send]')"),
          "chat pre-trial: no message box and no Send")
    check(d.js("document.querySelectorAll('[data-act=starter]').length") == 0,
          "chat pre-trial: no conversation starters")
    check(d.disabled_count() == 0, "no [disabled] on the chat view")
    d.shot("pretrial-chat-390.png")

    d.open("consumer/overview.html?child=kid-ada&view=manage", state="none", kids=2)
    check(d.disabled_count() == 0, "no [disabled] on the settings view", d.disabled_count())
    d.click("[data-act=reset-pass]")
    d.wait("!!document.getElementById('dk-newpass')")
    check(d.text("#dk-newpass") == "comet-saturn-42", "Reset password works pre-trial")
    d.click("[data-act=pick-year][data-id='9']")
    d.click("[data-act=save-manage]")
    d.wait("document.body.innerText.indexOf('Saved.')>=0")
    patch = [c for c in d.js("window.__CF__.calls") if c["method"] == "PATCH"]
    check(len(patch) == 1 and patch[0]["body"].get("year_group") == 9,
          "Edit child (Save changes) works pre-trial", patch)
    d.open("consumer/overview.html?child=kid-ada&view=manage", state="none", kids=2)
    d.click("[data-act=ask-remove]")
    d.click("[data-act=do-remove]")
    d.wait("document.body.innerText.indexOf('has been removed')>=0")
    dels = [c for c in d.js("window.__CF__.calls") if c["method"] == "DELETE"]
    check(len(dels) == 1 and dels[0]["path"].endswith("/kid-ada"),
          "Remove child works pre-trial", dels)


def no_children(d):
    print("\n── pre-trial, no children ──")
    for width in (390, 1280):
        d.open("consumer/overview.html", width=width, state="none", kids=0)
        body = d.text()
        check("can sign in" not in body, "@%d never claims children can sign in" % width)
        href = d.js("(function(){var a=document.querySelector('.dk-dashed a');"
                    "return a?a.getAttribute('href'):'';})()") or ""
        check("signup.html" in href and "step=child" in href and
              d.text(".dk-dashed a") == "Add a child",
              "@%d the screen offers Add a child (→ %s)" % (width, href))
        check(not d.js("!!document.querySelector('.dk-gate')"),
              "@%d no checkout line with nothing to check out" % width)
        d.shot("nokids-overview-%d.png" % width, width)


def trialing(d):
    print("\n── trialing ──")
    d.open("consumer/overview.html?child=kid-ada&view=child", state="trialing", kids=2)
    check(d.js("!!document.querySelector('[data-act=open-setwork]')"), "Set work is there")
    check(not d.js("!!document.querySelector('.dk-gate')"), "no gate line")
    d.shot("trialing-child-390.png")
    d.open("consumer/overview.html?child=kid-ada&view=chat", state="trialing", kids=2)
    check(d.js("!!document.getElementById('dk-draft')"), "message box is there")
    d.shot("trialing-chat-390.png")


def checkout_cases(d, skip_timeout):
    print("\n── checkout: one path, never a dead control ──")
    if not skip_timeout:
        d.open("consumer/overview.html", state="none", kids=2, checkout="hang")
        d.click(".dk-gate [data-act=checkout]")
        time.sleep(0.3)
        btn = "document.querySelector('.dk-gate [data-act=checkout]')"
        check(d.js(btn + ".getAttribute('aria-busy')") == "true" and
              d.js("!!" + btn + ".querySelector('.c-spin')") and
              d.js(btn + ".innerText.trim()") == "",
              "busy: a spinner and no words")
        d.shot("checkout-busy-390.png")
        d.click(".dk-gate [data-act=checkout]")
        d.click(".dk-gate [data-act=checkout]")
        check(len(d.calls("/api/consumer/checkout")) == 1, "a second press sends nothing",
              len(d.calls("/api/consumer/checkout")))
        t0 = time.time()
        d.wait("document.getElementById('dk-gate-msg').innerText.length>0", timeout=32000)
        took = time.time() - t0
        msgt = d.text("#dk-gate-msg")
        check("took too long" in msgt and "Try again" in msgt,
              "a hanging checkout gives up (%.0fs) and says so with Try again" % (took + 0.3), msgt)
        check(d.js(btn + ".getAttribute('aria-busy')") is None and
              d.js(btn + ".innerText.trim()") == "Start your free week",
              "the control is restored")
        d.shot("checkout-timeout-390.png")

    d.open("consumer/overview.html", state="none", kids=2, checkout="500")
    d.click(".dk-gate [data-act=checkout]")
    d.wait("document.getElementById('dk-gate-msg').innerText.length>0")
    msgt = d.text("#dk-gate-msg")
    check("didn’t open" in msgt and "Try again" in msgt, "a 500 shows a plain line + Try again", msgt)
    d.shot("checkout-500-390.png")
    d.shot("checkout-500-1280.png", 1280)
    d.click("#dk-gate-msg [data-c-retry]")
    d.wait("document.getElementById('dk-gate-msg').innerText.length>0")
    check(len(d.calls("/api/consumer/checkout")) == 2, "Try again tries again")

    d.open("consumer/overview.html", state="none", kids=2, checkout="no_url")
    d.click(".dk-gate [data-act=checkout]")
    d.wait("document.getElementById('dk-gate-msg').innerText.length>0")
    check("didn’t open" in d.text("#dk-gate-msg"), "a 200 with no url is a failure too")

    d.open("consumer/overview.html", state="none", kids=2, checkout="no_children")
    d.click(".dk-gate [data-act=checkout]")
    d.wait("document.getElementById('dk-gate-msg').innerText.length>0")
    href = d.js("(function(){var a=document.querySelector('#dk-gate-msg a');"
                "return a?a.getAttribute('href'):'';})()") or ""
    check("step=child" in href and "Add a child" in d.text("#dk-gate-msg"),
          "no_children offers Add a child", d.text("#dk-gate-msg"))
    d.shot("checkout-nochildren-390.png")

    d.open("consumer/overview.html", state="none", kids=2, checkout="ok")
    d.click(".dk-gate [data-act=checkout]")
    time.sleep(1.2)
    check(d.js("location.pathname+location.hash") == "/404.html#stripe-checkout",
          "a good answer goes to Stripe", d.js("location.href"))

    print("\n── checkout from the account page ──")
    d.open("consumer/account.html", state="none", kids=2, checkout="500")
    d.click("[data-act=checkout]")
    d.wait("document.getElementById('ak-plan-msg').innerText.length>0")
    check("didn’t open" in d.text("#ak-plan-msg") and
          d.js("document.getElementById('ak-plan-msg').previousElementSibling"
               ".getAttribute('data-act')") in ("checkout", None),
          "account: the failure sits under the button", d.text("#ak-plan-msg"))
    d.shot("account-checkout-500-390.png")

    print("\n── checkout from the signup plan step ──")
    d.open("consumer/signup.html?step=plan", state="none", kids=2, checkout="500")
    try:
        d.wait("!!document.getElementById('to-stripe')")
        d.click("#to-stripe")
        d.wait("(function(){var b=document.getElementById('to-stripe');"
               "var m=b&&b.nextElementSibling;return m&&m.innerText.length>0;})()")
        check("didn’t open" in d.js("document.getElementById('to-stripe').nextElementSibling.innerText"),
              "signup: the failure sits under the button and the step stays put")
        check(d.js("!!document.getElementById('to-stripe')") and
              d.js("document.getElementById('to-stripe').getAttribute('aria-busy')") is None,
              "signup: the button is restored, not a forever spinner")
        d.shot("signup-checkout-500-390.png")
    except Exception as e:  # noqa: BLE001
        check(False, "signup plan step reachable with the fixture", e)


def stale_message(d):
    print("\n── a message belongs to the press that caused it ──")
    d.open("consumer/overview.html?child=kid-ada&view=chat", state="trialing", kids=2,
           fail=[r"/chat/send$"])
    d.js("(function(){var i=document.getElementById('dk-draft');i.value='hello';"
         "i.dispatchEvent(new Event('input'));})()")
    d.click("[data-act=send]")
    d.wait("document.getElementById('dk-msg').innerText.length>0")
    check("refused" in d.text("#dk-msg"), "a failed send shows its line")
    # A starter chip fills the box and re-renders NOTHING — so if the line
    # goes, it went because the press cleared it (ruling 3), not a redraw.
    d.wait("document.querySelectorAll('[data-act=starter]').length>0")
    d.click("[data-act=starter]")
    check(d.text("#dk-msg") == "", "…and it is gone at the next press", d.text("#dk-msg"))


def refresh_b7(d):
    print("\n── B7: coming back re-reads the family ──")
    d.open("consumer/overview.html", state="none", kids=2)
    d.js("window.__CF__.family.billing.state='trialing';window.__CF__.family.billing.access='full';"
         "window.__CF__.family.billing.days_left=6;")
    d.js("window.dispatchEvent(new PageTransitionEvent('pageshow',{persisted:true}))")
    d.wait("!document.querySelector('.dk-gate')")
    check(True, "dashboard: a back/forward-cache restore re-reads (the not-started line goes)")
    time.sleep(2.1)
    d.js("window.__CF__.family.children[0].first_name='Adaline'")
    d.js("document.dispatchEvent(new Event('visibilitychange'))")
    d.wait("document.body.innerText.indexOf('Adaline')>=0")
    check(True, "dashboard: returning to the tab re-reads")

    d.open("consumer/account.html", state="trialing", kids=2)
    rows = d.js("[].map.call(document.querySelectorAll('a.ak-datarow'),function(a){return a.innerText})")
    check(any("Ada" in r for r in rows) and any("Ben" in r for r in rows),
          "account: every child's reports are listed", rows)
    d.js("window.__CF__.family.billing.state='none';window.__CF__.family.billing.access='none';"
         "window.__CF__.family.billing.can_checkout=true;")
    d.js("window.dispatchEvent(new PageTransitionEvent('pageshow',{persisted:true}))")
    d.wait("document.body.innerText.indexOf('Start your free week')>=0")
    check(True, "account: a back/forward-cache restore re-reads")


def delete_flow(d):
    print("\n── account deletion ──")
    for width in (390, 1280):
        d.open("consumer/account.html", width=width, state="trialing", kids=2)
        last = d.js("(function(){var m=document.getElementById('c-main');"
                    "return m.lastElementChild.id;})()")
        check(last == "ak-delete", "@%d Delete is the last thing on the page" % width, last)
        bottom = d.js("(function(){var r=document.querySelector('[data-act=ask-delete]')"
                      ".getBoundingClientRect();var max=0;document.querySelectorAll('#c-main *')"
                      ".forEach(function(e){var b=e.getBoundingClientRect();if(b.height)max=Math.max(max,b.bottom);});"
                      "return max-r.bottom;})()")
        check(bottom is not None and bottom < 30, "@%d …at the very bottom" % width, bottom)
        cls = d.js("document.querySelector('[data-act=ask-delete]').className")
        check(cls == "ak-textlink", "@%d …as an ordinary text link" % width, cls)
        d.shot("account-%d.png" % width, width)
    d.open("consumer/account.html", state="trialing", kids=2)
    d.click("[data-act=ask-delete]")
    check(d.js("document.activeElement&&document.activeElement.id") == "ak-keep",
          "the confirm opens with focus on Keep my account")
    body = d.text("#ak-delete")
    check("Delete my account" in body and "Keep my account" in body and "I understand" in body
          and "Type DELETE" not in body and not d.js("!!document.querySelector('#ak-delete input[type=text], #ak-confirm')"),
          "consequences + tick box + the two buttons, no typing")
    check(d.js("document.querySelectorAll('#ak-delete [disabled]').length") == 0,
          "no [disabled] in the confirm")
    d.shot("account-delete-confirm-390.png")
    d.click("[data-act=do-delete]")
    check("Tick" in d.text("#ak-del-msg") and
          len([c for c in d.js("window.__CF__.calls") if c["path"].endswith("delete-request")]) == 0,
          "Delete without the tick sends nothing and says why")
    d.js("(function(){var t=document.getElementById('ak-del-tick');t.click();})()")
    d.click("[data-act=do-delete]")
    d.wait("document.body.innerText.indexOf('Account scheduled for deletion')>=0")
    posts = [c for c in d.js("window.__CF__.calls")
             if c["path"].endswith("delete-request") and c["method"] == "POST"]
    check(len(posts) == 1 and posts[0]["body"] == {"confirm": "DELETE"},
          "it sends {confirm:'DELETE'} — the backend contract is unchanged", posts)
    check(d.js("!!document.querySelector('[data-act=undo-delete]')"), "scheduled, with Undo")
    d.shot("account-delete-scheduled-390.png")
    d.click("[data-act=undo-delete]")
    d.wait("document.body.innerText.indexOf('Nothing was deleted')>=0")
    check(d.js("!!document.querySelector('[data-act=ask-delete]')"), "Undo puts it back")


def copy_gone(d):
    print("\n── the removed copy ──")
    d.open("consumer/account.html", state="none", kids=2)
    t = d.text()
    for gone in ("The first week is free", "A card is needed to start",
                 "Nothing is taken until the free week ends"):
        check(gone not in t, "account: \"%s\" is gone" % gone)
    check("Add or remove children from the dashboard. Changes show on the next bill, pro-rated."
          in t, "account: the seats sentence is kept verbatim")
    d.open("consumer/overview.html", state="none", kids=2)
    check("Seven days free" not in d.text(), "dashboard: \"Seven days free…\" is gone")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None)
    ap.add_argument("--skip-timeout", action="store_true")
    ap.add_argument("--port", type=int, default=0, help="static server port")
    ap.add_argument("--cdp-port", type=int, default=0, help="Chrome remote-debugging port")
    args = ap.parse_args()

    if args.cdp_port:
        cdp.Browser._free_port = staticmethod(lambda: args.cdp_port)
    server, port = cdp.serve(REPO, args.port)
    try:
        with cdp.Browser() as b:
            d = Drive(b, port, args.shots)
            pre_trial(d)
            no_children(d)
            trialing(d)
            checkout_cases(d, args.skip_timeout)
            stale_message(d)
            refresh_b7(d)
            delete_flow(d)
            copy_gone(d)
    finally:
        server.shutdown()
    print("\n%s — %d failure(s)" % ("PASS" if not FAILS else "FAIL", len(FAILS)))
    for f in FAILS:
        print("   ✗ " + f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())
