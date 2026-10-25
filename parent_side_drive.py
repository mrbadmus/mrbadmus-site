#!/usr/bin/env python3
"""parent_side_drive.py — the parent-side rebuild, driven offline (25 Oct 2026).

consumer/family.html (Home, a child, Past work, the work panel),
consumer/done.html (the child's "Everything you've done") and the desktop
child Today, on consumer_dash_fixture's stubbed session with the
parent-side payloads from parent_side_fixture.py. No backend, no TEST, no
production request: BACKEND_URL points at a host that cannot resolve.

What it holds (docs/b2c/parent-side-plan.md, hard rules):
  * every number on screen is the fixture's — done counts, scores, the
    panel's score line, topic counts and bases, wrong counts;
  * the work panel shows EVERY question, an unmarked answer is never
    "Right", a self-check says so, a 6-mark answer shows its AQA level,
    a time appears only where one was measured, and an item that saves no
    answers says "This activity isn't tracked yet.";
  * past work sorts and filters (and works the same without /past-work);
  * Back returns to where the parent came from; Escape closes the panel;
  * nothing scrolls sideways at 390 or 1920; the panel is full screen
    below 700px; the desktop Today has two columns.

Contrast is NOT measured here — contrast_audit.py measures these pages in
light and dark (its "parent-side/" entries).

Usage: python3 parent_side_drive.py [--shots DIR]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import ks3_browser as cdp  # noqa: E402
import parent_side_fixture as psf  # noqa: E402
import consumer_dash_drive as cdd  # noqa: E402

check = cdd.check
PS = {"ps": {}}


def expected_chip(it, today=psf.TODAY):
    """The row chip's word, from the fixture by the plan's rules — written
    out independently of parent-side.js."""
    if it["status"] == "done":
        if not it["tracked"]:
            return "Done"
        s = it["summary"]
        if s["marks_available"]:
            return "%d/%d" % (s["marks_scored"], s["marks_available"])
        if s["self_checked"] and s["unmarked"] == s["self_checked"]:
            return "Self-checked"
        if s["unmarked"]:
            return "Not marked"
        return "Done"
    d = it["scheduled_for"]
    if d < today:
        return "Not done"
    if d == today:
        return "Today"
    return "Opens " + ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][
        __import__("datetime").date.fromisoformat(d).weekday()]


def no_sideways(d, label):
    sw = d.js("document.documentElement.scrollWidth - window.innerWidth")
    check(sw is not None and sw <= 0, "%s: nothing scrolls sideways" % label, sw)


def home(d):
    print("\n── Home ──")
    d.open("consumer/family.html", width=1440, state="trialing", kids=2, **PS)
    t = d.text("#c-main")
    h = psf.family_home(cdd.fx.KIDS[:2])["children"][0]
    check("%d of %d done" % (h["week"]["done"], h["week"]["total"]) in t,
          "Ada's card: this week's done count is the API's", h["week"])
    states = d.js("[].map.call(document.querySelectorAll('.ps-kid')[0].querySelectorAll('.ps-day'),"
                  "function(e){return e.className.replace('ps-day','').trim();})")
    check(states == ["is-done", "is-done", "is-today", "is-set", "", "", "is-set"],
          "the Mon–Sun strip follows the API's day states", states)
    check("Exam question: Changes of state · 3/6 marked" in t, "most recent: title and marked score")
    check("1 piece from earlier this week not done." in d.text(".ps-kid"),
          "Ada's card: her first attention line (overdue)")
    check("Wrong 2 times over 2 weeks: Why does the temperature stay the same while ice melts? (and 1 more)"
          in d.text(".ps-aside"), "the column lists the repeated wrong, count first")
    check("overdue" not in t and t.count("from earlier this week not done") == 1 and
          "Hasn’t logged in" not in d.text(".ps-aside"),
          "no attention line is said twice (card and column)")
    check("Nothing done yet." in t and "Username ben.saturn" in t, "Ben: nothing yet, with his username")
    check("across" in t, "two children: the family total line is shown")
    check(d.js("document.querySelector('.ps-nav a[href*=\"view=chat\"] .ps-badge')&&"
               "document.querySelector('.ps-nav a[href*=\"view=chat\"] .ps-badge').textContent.indexOf('1')>=0"),
          "Messages links to the existing chat, with the unread count")
    check("£" not in t, "no price on the home during the free week")
    no_sideways(d, "home 1440")
    d.shot("home-1440.png", 1440)
    d.open("consumer/family.html", width=1440, state="trialing", kids=1, **PS)
    check("across" not in d.text("#c-main"), "one child: no total line repeating the card")
    d.open("consumer/family.html", width=390, state="trialing", kids=2, **PS)
    check(d.js("getComputedStyle(document.getElementById('ps-tabbar')).display") == "grid",
          "390: the tab bar carries Home · Past work · Messages · Account")
    no_sideways(d, "home 390")
    d.open("consumer/family.html", width=1920, state="trialing", kids=2, **PS)
    no_sideways(d, "home 1920")
    # Without /family/home the page still draws from /family.
    d.open("consumer/family.html", width=1440, state="trialing", kids=2, ps={"homeMissing": True})
    check("1 of 3 done" in d.text(".ps-kid"),
          "without /family/home: Ada's card drawn from /family's week", d.text(".ps-kid")[:160])


def child(d):
    print("\n── a child ──")
    d.open("consumer/family.html?view=child&child=kid-ada", width=1440, state="trialing", kids=2, **PS)
    d.wait("document.querySelectorAll('#week .ps-row').length>0")
    items = [i for i in psf.ada_items() if psf.WEEK <= i["scheduled_for"] <= "2026-10-04"]
    items.sort(key=lambda i: i["scheduled_for"])
    chips = d.js("[].map.call(document.querySelectorAll('#week .ps-row .ps-chip'),function(e){return e.textContent.trim();})")
    check(sorted(chips) == sorted(expected_chip(i) for i in items),
          "This week: every row's chip is the fixture's (scores marked-only, Today/Opens/Not done)", chips)
    done = sum(1 for i in items if i["status"] == "done")
    check("%d of %d done" % (done, len(items)) in d.text("#week"), "This week: done count")
    check(d.js("document.querySelectorAll('#week .ps-row[disabled]').length") == len(items) - done,
          "only finished work opens")
    tops = psf.topics()
    for st, label in (("secure", "Secure"), ("shaky", "Shaky"), ("not_yet", "Not yet")):
        n = d.js("(function(){var h=document.querySelector('.ps-tg-%s .ps-mono');return h&&h.textContent;})()" % st)
        check(n == str(sum(1 for t in tops if t["status"] == st)), "Topic picture: %s count" % label, n)
    tp = d.text("#topics")
    check("based on 12 answers" in tp and "based on 1 answer · 1 not marked" in tp and "1 answer, not marked yet" in tp,
          "each topic says what its status is based on")
    kw = psf.keeps_wrong(psf.ada_items())
    for r in kw:
        check(("Wrong %d times" % r["wrong_count"]) in d.text("#wrong"), "keeps wrong: %s count" % r["kind"])
    check(d.js("document.querySelectorAll('#wrong .ps-wrong li').length") == sum(len(r["answers"]) for r in kw),
          "keeps wrong: each wrong answer is shown")
    check(d.js("!!document.querySelector('#tutor .ps-reply sub')"), "tutor reply: the backend's <sub> renders as markup")
    check("The reply wasn’t saved." in d.text("#tutor"), "a reply that was not saved says so")
    check(d.js("document.querySelectorAll('#tutor .ps-tutor-row').length") == len(psf.TUTOR), "every tutor question")
    no_sideways(d, "child 1440")
    d.shot("child-1440.png", 1440)

    print("\n── the work panel ──")
    d.click("#week .ps-row[data-open='ada-w1']")
    d.wait("!!document.querySelector('.ps-panel')")
    it = [i for i in psf.ada_items() if i["id"] == "ada-w1"][0]
    qids = []
    for a in it["answers"]:
        if a["question_id"] not in qids:
            qids.append(a["question_id"])
    check(d.js("document.querySelectorAll('.ps-panel .ps-q').length") == len(qids), "every question is shown", len(qids))
    check("Score 5/10 marked · 1 answer not marked" in d.text(".ps-panel"), "panel score counts marked answers only",
          d.text(".ps-panel-stats"))
    unm = d.js("[].filter.call(document.querySelectorAll('.ps-panel .ps-q'),function(q){"
               "return q.querySelector('.ps-q-top .ps-chip').textContent.indexOf('Not marked')>=0;}).length")
    check(unm == 1, "the unmarked 6-mark answer reads Not marked (never Right)", unm)
    check("Attempt 1" in d.text(".ps-panel") and "Attempt 2" in d.text(".ps-panel") and "2 attempts" in d.text(".ps-panel"),
          "both attempts at a retried question are listed")
    times = d.js("[].map.call(document.querySelectorAll('.ps-panel .ps-q'),function(q){return q.querySelector('.ps-q-meta').textContent;})")
    check(times and times[3] == "Attempt 1Marked by AI",
          "an answer with no measured time shows no time", times[3] if times else None)
    d.js("document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true}))")
    d.wait("!document.querySelector('.ps-panel')")
    check(not d.js("new URLSearchParams(location.search).get('open')"), "Escape closes the panel and Back state with it")
    d.open("consumer/family.html?view=child&child=kid-ada&open=ada-w3", width=1440, state="trialing", kids=2, **PS)
    d.wait("!!document.querySelector('.ps-panel')")
    p = d.text(".ps-panel")
    check("AQA level" in p and "Level 2" in p and "Next step" in p, "a 6-mark answer shows its AQA level and next step")
    check("9 min 12 s" in p, "a measured time is shown")
    d.open("consumer/family.html?view=child&child=kid-ada&open=ada-w7", width=1440, state="trialing", kids=2, **PS)
    d.wait("!!document.querySelector('.ps-panel')")
    check("This activity isn’t tracked yet." in d.text(".ps-panel"), "an item that saves no answers says so")
    d.open("consumer/family.html?view=child&child=kid-ada&open=ada-w8", width=390, state="trialing", kids=2, **PS)
    d.wait("!!document.querySelector('.ps-panel')")
    check("Self-checked" in d.text(".ps-panel") and "Right" not in d.text(".ps-panel"), "a self-check says so, never Right")
    check(d.js("Math.round(document.querySelector('.ps-panel').getBoundingClientRect().width)===window.innerWidth"),
          "390: the panel is full screen")
    d.shot("panel-390.png")


def back_nav(d):
    print("\n── back goes where you came from ──")
    d.open("consumer/family.html", width=1440, state="trialing", kids=2, **PS)
    d.click(".ps-kid-head[data-go-child='kid-ada']")
    d.wait("new URLSearchParams(location.search).get('view')==='child'")
    d.wait("document.querySelectorAll('#week .ps-row').length>0")
    d.click("[data-act=back]")
    d.wait("!new URLSearchParams(location.search).get('view')")
    check(d.js("!!document.querySelector('.ps-kid')"), "child → Back → Home")
    d.click(".ps-nav a[data-nav=nav-past]")
    d.wait("document.querySelectorAll('.ps-weeks .ps-row').length>0")
    d.click(".ps-weeks .ps-row[data-open]")
    d.wait("!!document.querySelector('.ps-panel')")
    d.js("history.back()")
    d.wait("!document.querySelector('.ps-panel')")
    check(d.js("new URLSearchParams(location.search).get('view')") == "past",
          "Past work → open an item → Back closes it and stays on Past work")


def past(d):
    print("\n── Past work ──")
    d.open("consumer/family.html?view=past&sort=lowest", width=1440, state="trialing", kids=2, **PS)
    d.wait("document.querySelectorAll('.ps-week-h h2').length>0")
    heads = d.js("[].map.call(document.querySelectorAll('.ps-week-h h2'),function(e){return e.textContent;})")
    exp = ["Week of " + g["label"] for g in psf.past_work(("kid-ada", "kid-ben"), sort="lowest")["weeks"]]
    check(heads == exp, "lowest score first: weeks in the API's order", heads)
    d.click("[data-act=subj][data-v=Chemistry]")
    d.wait("document.querySelector('[data-v=Chemistry]').getAttribute('aria-pressed')==='true'&&"
           "document.querySelectorAll('.ps-weeks .ps-row').length>0")
    subs = d.js("[].map.call(document.querySelectorAll('.ps-weeks .ps-row-sub'),function(e){return e.textContent;})")
    check(subs and all("Chemistry" in s for s in subs), "subject filter: only Chemistry", subs)
    d.open("consumer/family.html?view=past", width=1440, state="trialing", kids=2, ps={"pastMissing": True})
    d.wait("document.querySelectorAll('.ps-week-h h2').length>0")
    heads2 = d.js("[].map.call(document.querySelectorAll('.ps-week-h h2'),function(e){return e.textContent;})")
    exp2 = ["Week of " + g["label"] for g in psf.past_work(("kid-ada",), sort="newest")["weeks"]]
    check(heads2 == exp2, "without /past-work: the same weeks, grouped by the same rule", heads2)
    d.click(".ps-weeks .ps-row[data-open='ada-w2']")
    d.wait("!!document.querySelector('.ps-panel .ps-q')")
    check(d.js("document.querySelectorAll('.ps-panel .ps-q').length") == 8, "opening a past item shows every question")
    no_sideways(d, "past 1440")
    d.open("consumer/family.html?view=past", width=390, state="trialing", kids=2, **PS)
    d.wait("document.querySelectorAll('.ps-week-h h2').length>0")
    no_sideways(d, "past 390")


def kid(d):
    print("\n── the child's pages ──")
    d.open("consumer/done.html", width=1440, state="trialing", kids=2, who="child", **PS)
    d.wait("document.querySelectorAll('.ps-wcard').length>0")
    n = sum(1 for i in psf.ada_items() if i["status"] == "done")
    check(d.text("h1") == "%d things done." % n, "Everything you've done: the count is the API's", d.text("h1"))
    d.click(".ps-wcard[data-open='ada-w3']")
    d.wait("!!document.querySelector('.ps-panel')")
    check("You answered" in d.text(".ps-panel"), "the child's panel says You")
    no_sideways(d, "done 1440")
    d.open("consumer/done.html", width=390, state="trialing", kids=2, who="child", **PS)
    d.wait("document.querySelectorAll('.ps-wcard').length>0")
    no_sideways(d, "done 390")
    d.open("consumer/today.html", width=1440, state="trialing", kids=2, who="child")
    d.wait("!document.getElementById('td-stats').hidden")
    check(d.js("document.querySelector('.td-aside').getBoundingClientRect().left>"
               "document.querySelector('.td-col-main').getBoundingClientRect().right"),
          "desktop Today: the week column sits to the right of the day's work")
    check("/consumer/done.html" in (d.js("document.getElementById('td-done').getAttribute('href')") or ""),
          "Today links to Everything you've done")
    d.open("consumer/today.html", width=390, state="trialing", kids=2, who="child")
    d.wait("!document.getElementById('td-stats').hidden")
    check(d.js("document.getElementById('td-stats').getBoundingClientRect().top<"
               "document.querySelector('.td-main .td-h2').getBoundingClientRect().top"),
          "phone Today: one column, the streak still above Today")
    no_sideways(d, "today 390")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default=None)
    args = ap.parse_args()
    shots = args.shots or os.path.join(cdp.gate_tmp() if hasattr(cdp, "gate_tmp") else
                                       os.path.expanduser("~/tmp/ks3-gates"), "parent-side")
    server, port = cdp.serve(HERE, 0)
    try:
        with cdp.Browser() as b:
            d = cdd.Drive(b, port, shots)
            home(d)
            child(d)
            back_nav(d)
            past(d)
            kid(d)
    finally:
        server.shutdown()
    fails = cdd.FAILS
    print("\n%s — %d failure(s)" % ("PASS" if not fails else "FAIL", len(fails)))
    for f in fails:
        print("   ✗ " + f)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
