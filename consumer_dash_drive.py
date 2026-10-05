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

B2C onboarding repair (3 Oct 2026) adds signup, verification and the shared
topic picker: V1 (verified in another browser; "already have an account"),
V2 (a saved step never strands a signed-in parent), V3 (the child typed
before verifying is asked about, never a blank Child 2), V4 (two tabs; own
usernames skipped; taken explains and suggests), V5 (rail buttons, Back),
V6 (the picker in signup and in Set work), and the removed trial copy.

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


def week_repair(d):
    """B2C week repair (4 Oct 2026). Work set for a later week is listed, the
    strip is Monday-first (unit 7, ruling 3), the browser keeps no week helper, and a carried link keeps ONE '?'."""
    print("\n── the ruled week ──")
    d.open("consumer/overview.html?child=kid-ada&view=child&env=test", state="trialing", kids=2)
    check("Next week" in d.text(".dk-work") and "Photosynthesis: lesson 3" in d.text(".dk-upcoming"),
          "work set for next week is listed under its own heading")
    check("Mon" in d.text(".dk-upcoming") and "12 Oct" not in d.text(".dk-upcoming"),
          "…its day in the badge, the heading naming the week (no repeated date)",
          d.text(".dk-upcoming"))
    check("Photosynthesis: lesson 3" not in d.text(".dk-work ul:not(.dk-upcoming)"),
          "…and it is not counted as this week's work")
    strip = d.js("(function(){var s=document.querySelector('.dk-card [style*=\"display:flex;gap:6px\"]');"
                 "if(!s)return null;return Array.prototype.map.call(s.children,function(c){"
                 "return c.lastElementChild?c.lastElementChild.textContent:'';}).join('');})()")
    # ⊕ B2C unit 7 (Mide's ruling 3, 5 Oct 2026): the parent strip starts on
    # MONDAY again — the calendar week, read from `week_strip`. This asserted
    # Sunday-first under the week repair's earlier reading; the ruling
    # reversed it, so the exact order is still pinned, the other way round.
    check(strip == "MTWTFSS", "the day strip opens on Monday (ruling 3)", strip)
    h = d.js("window.MrBadmusConsumer.href('/student/assignment.html?id=abc')")
    check(h and h.count("?") == 1 and "id=abc" in h and "env=test" in h,
          "a carried link with its own query keeps ONE '?' (id=abc&env=test)", h)
    check(d.js("typeof window.MrBadmusConsumer.weekStart") == "undefined",
          "the browser computes no week of its own (the backend's ruled week is the only one)")
    h2 = d.js("window.MrBadmusConsumer.href('/consumer/report.html', {child: 'kid-ada'})")
    check(h2 == "/consumer/report.html?env=test&child=kid-ada", "a plain path still carries env + extra", h2)
    d.shot("week-repair-child-390.png")


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
    # ⊕ B2C polish (4 Oct 2026): the undo line now says what is TRUE after an
    # undo — the account stays and the children's logins work again.
    # ⊕ B2C polish 2 (defect 8): it is now its own block — "Your account is
    # staying" / "Your children can sign in again." — and, when billing is set
    # to end, says so beside Resume (driven against TEST in the unit report).
    d.wait("document.body.innerText.indexOf('Your account is staying')>=0&&"
           "document.body.innerText.indexOf('Your children can sign in again')>=0")
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


# ══════════════════════════════════════════════════════════════════════
# B2C onboarding repair (3 Oct 2026) — signup, verification, the topic
# picker. V1–V6 are the defects reproduced on TEST; each block names one.
# ══════════════════════════════════════════════════════════════════════
ORION = {"name": "Orion", "year": 8, "board": None, "tier": None, "route": None,
         "mode": "school", "user": "orionrocks", "pass": "comet-saturn-42"}


def draft(step, pending=(ORION,), **extra):
    d = {"email": "sam@example.test", "name": "Sam", "step": step, "terms": True,
         "pending": list(pending)}
    d.update(extra)
    return d


def tp_type(d, text):
    d.js("(function(){var i=document.querySelector('.tp-q');i.focus();i.value=%s;"
         "i.dispatchEvent(new Event('input'));})()" % json.dumps(text))
    time.sleep(0.15)


def tp_row(d, name):
    """{off, why, selected} for the first visible option with that name."""
    return d.js("(function(){var o=[].filter.call(document.querySelectorAll('.tp-opt'),function(li){"
                "return li.querySelector('.tp-name').textContent===%s;})[0];if(!o)return null;"
                "var w=o.querySelector('.tp-why');return {off:o.getAttribute('aria-disabled')==='true',"
                "why:w?w.textContent:'',selected:o.getAttribute('aria-selected')==='true',n:o.getAttribute('data-n')};})()"
                % json.dumps(name))


def tp_click(d, name):
    return d.js("(function(){var o=[].filter.call(document.querySelectorAll('.tp-opt'),function(li){"
                "return li.querySelector('.tp-name').textContent===%s;})[0];if(!o)return false;"
                "o.click();return true;})()" % json.dumps(name))


def onboarding(d):
    print("\n── V3/V4: the pre-verify list says what is true ──")
    d.open("consumer/signup.html", signed_in=False, state="none", kids=0, draft=draft("children"))
    d.wait("document.querySelector('#su-main h1')")
    h = d.text("#su-main h1")
    check(h == "Orion is added", "pre-verify: the heading does not claim Orion is set up", h)
    check("We’ll make Orion’s login once your email is verified." in d.text("#su-main"),
          "pre-verify: …and says when the login is made")
    d.shot("onb-pre-verify-children-390.png")

    print("\n── V5: rail steps are buttons, Back stays in the flow ──")
    d.open("consumer/signup.html", width=1280, signed_in=False, state="none", kids=0,
           draft=draft("children"))
    d.wait("document.querySelector('[data-rail]')")
    rails = d.js("[].map.call(document.querySelectorAll('#rail-steps [data-rail]'),function(b){return b.tagName+':'+b.getAttribute('data-rail')})")
    check(rails == ["BUTTON:0", "BUTTON:1"], "rail: the two finished steps are buttons", rails)
    d.click("[data-rail='0']")
    d.wait("!!document.getElementById('v-done')")
    check(d.js("!!document.getElementById('v-pass')"),
          "rail → 'Your account' opens Check your inbox, with a way on (password + button)")
    d.shot("onb-verify-1280.png", 1280)
    d.js("history.back()")
    d.wait("document.querySelector('#su-main h1').textContent==='Orion is added'")
    check(True, "Back from Check your inbox returns to the list, not out of signup")
    d.click("#add-another")
    d.wait("!!document.getElementById('c-name')")
    check(d.text("#su-main h1") == "Add another child" and "CHILD 2" in d.text("#su-main").upper(),
          "a second child is presented as 'Add another child'", d.text("#su-main h1"))
    d.js("history.back()")
    d.wait("!!document.getElementById('add-another')")
    check(True, "Back from the child form returns to the list")

    print("\n── V1: verified in ANOTHER browser — this tab's way on ──")
    d.open("consumer/signup.html", signed_in=False, state="none", kids=0,
           draft=draft("verify"), password_ok=True)
    d.wait("!!document.getElementById('v-done')")
    d.js("(function(){var i=document.getElementById('v-pass');i.value='Sam-password-1';})()")
    d.click("#v-done")
    try:
        d.wait("document.querySelector('#su-main h1')&&document.querySelector('#su-main h1').textContent==='Where is Orion up to?'", 8000)
        check(True, "'I've clicked the link' signs this tab in, creates Orion, asks where Orion is up to")
    except Exception as e:  # noqa: BLE001
        check(False, "'I've clicked the link' carries on", d.text("#su-main")[:200])
    posts = d.calls("/api/consumer/children")
    check(len(posts) == 1 and posts[0]["body"]["username"] == "orionrocks", "…Orion created once", posts)
    names = [c for c in d.js("window.__CF__.calls") if c["path"] == "/api/consumer/parent"]
    check(any((c.get("body") or {}).get("first_name") == "Sam" for c in names),
          "the parent's name is sent on its own (not only with the terms)", names)

    print("\n── V1: 'already have an account' signs in and continues ──")
    d.open("consumer/signup.html?step=account", signed_in=False, state="none", kids=0,
           draft=draft("account"), existing=True, password_ok=True)
    d.wait("!!document.getElementById('continue')")
    d.js("(function(){document.getElementById('email').value='sam@example.test';"
         "document.getElementById('email').dispatchEvent(new Event('input'));"
         "document.getElementById('password').value='Sam-password-1';})()")
    d.click("#continue")
    try:
        d.wait("document.querySelector('#su-main h1')&&document.querySelector('#su-main h1').textContent==='Where is Orion up to?'", 8000)
        check(True, "an address that already has an account signs in with what was typed and carries on")
    except Exception:  # noqa: BLE001
        check(False, "'already have an account' is not a dead end", d.text("#su-main")[:200])
    check("try signing in instead" not in d.text(), "…and never says 'try signing in instead'")
    meta = [c for c in d.js("window.__CF__.calls") if c["path"] == "signUp"]
    check(meta and meta[0]["body"]["options"]["data"].get("first_name") == "Sam"
          and meta[0]["body"]["options"]["data"].get("terms_accepted") is True,
          "signUp carries the name and the tick on the account (for another browser)",
          meta and meta[0]["body"]["options"]["data"])

    print("\n── V3 + V6: after verifying, the topic step for the child typed before ──")
    d.open("consumer/signup.html?step=child", state="none", kids=0, draft=draft("verify"))
    d.wait("document.querySelector('.tp-q')")
    check(d.text("#su-main h1") == "Where is Orion up to?",
          "?step=child (the old verify link) still asks about Orion, not a blank Child 2")
    combo = d.js("(function(){var q=document.querySelector('.tp-q');var l=document.getElementById(q.getAttribute('aria-controls'));"
                 "return [q.getAttribute('role'),q.getAttribute('aria-expanded'),l&&l.getAttribute('role')];})()")
    check(combo == ["combobox", "true", "listbox"], "the search box is a combobox over a listbox", combo)
    r = tp_row(d, "Breathing and gas exchange")
    check(r and not r["off"], "in-year unit is choosable", r)
    tp_type(d, "food tests")
    r = tp_row(d, "Food tests")
    check(r and r["off"] and r["why"] == "taught in Year 7", "Year 7 lesson is greyed: taught in Year 7", r)
    tp_click(d, "Food tests")
    check(not d.js("window.__CF__.calls.some(function(c){return /position$/.test(c.path)})") and
          d.js("document.getElementById('u-save').getAttribute('aria-disabled')") == "true",
          "…and cannot be chosen")
    tp_type(d, "bonding")
    r = tp_row(d, "Bonding, Structure and Properties of Matter")
    check(r and r["off"] and r["why"] == "taught in Year 10", "GCSE topic is greyed: taught in Year 10", r)
    d.shot("onb-picker-greyed-390.png")
    # browse: Subject → Topic narrows; typing then filters inside it
    d.js("(function(){var s=document.querySelector('.tp-browse select');s.value='biology';s.dispatchEvent(new Event('change'));"
         "var t=document.querySelectorAll('.tp-browse select')[1];t.value='ks3-B4';t.dispatchEvent(new Event('change'));})()")
    time.sleep(0.15)
    names = d.js("[].map.call(document.querySelectorAll('.tp-opt .tp-name'),function(e){return e.textContent})")
    check(names and names[0] == "Breathing and gas exchange" and "How breathing works" in names,
          "browsing Biology → B4 narrows the list to that unit and its lessons", names)
    tp_type(d, "how")
    names = d.js("[].map.call(document.querySelectorAll('.tp-opt .tp-name'),function(e){return e.textContent})")
    check(names == ["How breathing works"], "typing filters inside the browsed unit", names)
    # keyboard: ArrowDown + Enter chooses
    d.js("(function(){var q=document.querySelector('.tp-q');q.dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowDown',bubbles:true}));"
         "q.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',bubbles:true}));})()")
    time.sleep(0.15)
    check(d.text("#u-save") == "Start Orion from How breathing works", "keyboard: ArrowDown + Enter chooses",
          d.text("#u-save"))
    d.shot("onb-picker-chosen-390.png")
    d.click("#u-save")
    d.wait("document.querySelector('#su-main h1').textContent==='Orion is set up'")
    pos = d.calls("/api/consumer/children/kid-new0/position")
    check(pos and pos[0]["body"] == {"cursors": {"Biology": 2}},
          "a lesson places Orion at that lesson's week in its subject", pos)
    check(len(d.calls("/api/consumer/children")) == 1, "Orion was created once")

    print("\n── V2: a saved step never strands a signed-in parent ──")
    for st in ("unit", "stripe"):
        d.open("consumer/signup.html", state="none", kids=2, draft=draft(st, pending=()))
        d.wait("document.querySelector('#su-main h1')")
        h = d.text("#su-main h1")
        check(h == "2 children set up", "draft step '%s' → the children list from the server" % st, h)
    d.open("consumer/signup.html?step=child", state="trialing", kids=2, draft=draft("plan", pending=()))
    d.wait("!!document.getElementById('c-name')")
    check(d.text("#su-main h1") == "Add another child", "dashboard 'Add a child' (paid family) → Add another child")
    d.click("#c-cancel")
    d.wait("!!document.getElementById('add-another')")
    check(d.js("!!document.getElementById('to-dash')") and not d.js("!!document.getElementById('to-plan')"),
          "a family already through Stripe gets 'Back to your dashboard', never the plan again")

    print("\n── V4: a child already in this family is skipped, never 'taken' ──")
    ada = dict(ORION, name="Ada", user="ada.comet")
    d.open("consumer/signup.html", state="none", kids=2, draft=draft("verify", pending=(ada,)))
    d.wait("document.querySelector('#su-main h1')")
    check(len(d.calls("/api/consumer/children")) == 0, "no second create for a username this family has")
    check("taken" not in d.text().lower() and "already uses" not in d.text(),
          "…and no username-taken message", d.text("#su-main")[:120])
    check(d.js("JSON.parse(localStorage.getItem('mrb.consumer.signup')||'{}').pending") is None,
          "…and the draft no longer holds it")

    d.open("consumer/signup.html", state="none", kids=0, draft=draft("verify"), taken=["orionrocks"])
    d.wait("!!document.getElementById('c-user-state')")
    t = d.text("#c-user-state")
    check("Someone already uses orionrocks." in t and "orionrocks7" in t and "orionrocksx" in t,
          "taken by someone else: explains and offers two names", t)
    d.shot("onb-username-taken-390.png")
    d.js("document.querySelector('[data-take]').click()")
    time.sleep(0.6)
    check(d.js("document.getElementById('c-user').value") == "orionrocks7", "a suggestion is one tap")

    print("\n── V6: the dashboard's Set work uses the same picker ──")
    d.open("consumer/overview.html?child=kid-ada&view=setwork", state="trialing", kids=2)
    d.wait("document.querySelector('.tp-q')")
    tp_type(d, "how breathing")
    tp_click(d, "How breathing works")
    d.click("[data-act=submit-work]")
    d.wait("window.__CF__.calls.some(function(c){return /kid-ada\\/work$/.test(c.path)})")
    w = [c for c in d.js("window.__CF__.calls") if c["path"].endswith("kid-ada/work")]
    check(w and w[0]["body"].get("lesson_slug") == "how-breathing-works" and "unit_code" not in w[0]["body"],
          "set work: a chosen lesson is sent as that lesson", w and w[0]["body"])
    d.open("consumer/overview.html?child=kid-ben&view=setwork", state="trialing", kids=2)
    d.wait("document.querySelector('.tp-q')")
    r = tp_row(d, "Cell Biology")
    check(r and not r["off"], "GCSE child: their own topic is choosable", r)
    tp_type(d, "cells and organisation")
    r = tp_row(d, "Cells and organisation")
    check(r and r["off"] and r["why"] == "taught in Year 7", "GCSE child: KS3 unit greyed, taught in Year 7", r)
    tp_type(d, "space physics")
    r = tp_row(d, "Space Physics")
    check(r and r["off"] and r["why"] == "not in Year 10’s plan",
          "combined child: a triple-only topic says 'not in Year 10’s plan'", r)
    tp_type(d, "cell biology")
    tp_click(d, "Cell Biology")
    d.click("[data-act=submit-work]")
    d.wait("window.__CF__.calls.some(function(c){return /kid-ben\\/work$/.test(c.path)})")
    w = [c for c in d.js("window.__CF__.calls") if c["path"].endswith("kid-ben/work")]
    check(w and w[0]["body"].get("unit_code") == "Cell Biology",
          "set work: a GCSE topic is sent by its title (KS4 has no unit codes)", w and w[0]["body"])
    d.shot("onb-setwork-ks4-390.png")
    d.open("consumer/overview.html?child=kid-ada&view=setwork", state="trialing", kids=2)
    d.wait("document.querySelector('.tp-q')")
    d.js("document.querySelector('[data-act=pick-kind][data-id=exam]').click()")
    time.sleep(0.2)
    d.click("[data-act=submit-work]")
    d.wait("window.__CF__.calls.some(function(c){return /kid-ada\\/work$/.test(c.path)})")
    w = [c for c in d.js("window.__CF__.calls") if c["path"].endswith("kid-ada/work")]
    check(w and w[0]["body"]["kind"] == "exam" and not d.js("!!document.querySelector('.tp-q')"),
          "an exam question asks no topic and sets", w and w[0]["body"])


def onboarding_copy(d):
    print("\n── the removed onboarding copy ──")
    d.open("consumer/signup.html?step=plan", state="none", kids=2)
    d.wait("!!document.getElementById('to-stripe')")
    t = d.text()
    for gone in ("pay nothing", "Seven days free, full access", "isn't charged until",
                 "Work is set every Sunday", "Nothing is charged for seven days"):
        check(gone not in t, "signup: \"%s\" is gone" % gone)
    check(d.js("document.body.innerHTML.indexOf('Free for seven days</p>\\n    <p')") == -1,
          "signup: the rail's 'Free for seven days' card is gone")
    for path, gone in (("parents/pricing.html", "costs nothing"),
                       ("parents/how-it-works.html", "Card needed, nothing charged")):
        d.p.goto("http://127.0.0.1:%d/%s" % (d.port, path))
        time.sleep(0.6)
        check(gone not in (d.js("document.documentElement.innerHTML") or ""), "%s: \"%s\" is gone" % (path, gone))


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
            week_repair(d)
            checkout_cases(d, args.skip_timeout)
            stale_message(d)
            refresh_b7(d)
            delete_flow(d)
            copy_gone(d)
            onboarding(d)
            onboarding_copy(d)
    finally:
        server.shutdown()
    print("\n%s — %d failure(s)" % ("PASS" if not FAILS else "FAIL", len(FAILS)))
    for f in FAILS:
        print("   ✗ " + f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())
