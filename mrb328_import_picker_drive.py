#!/usr/bin/env python3
"""mrb328_import_picker_drive.py — MRB-328 J2: WHICH CLASS AM I IMPORTING INTO?

    python3 mrb328_import_picker_drive.py --section b        # stubbed, no network
    MRB_THROWAWAY_PASSWORD=mrb326-throwaway python3 mrb328_import_picker_drive.py --section a

⚠️ The password is the MRB-326 throwaway pair's, and `teacher_admin_real_drive.py`
is where it is documented and where it can be RE-ASSERTED (`--provision`). Three
drives share these two accounts off this one variable, so a value set by one of
them for its own convenience breaks the other two — which is exactly what
happened between 28 August and 7 September 2026.
    …                        python3 mrb328_import_picker_drive.py            # both
    …                        python3 mrb328_import_picker_drive.py --shots DIR

⚑ THE GAP THIS CLOSES.

  `teacher/import.html` carried a chip that answered "which class am I
  importing into?" and no way to answer it. Before a file was uploaded it read
  "Not chosen yet" and there was nothing to press; the only way a class ever
  got named was by parsing it back out of the CSV. Meanwhile
  `teacher/class-detail.html` had been linking here as
  `import.html?class=<id>` since MRB-325 and this page never read the
  parameter — so a teacher who pressed "Import students" from inside a class
  arrived somewhere that had forgotten which class they came from.

  MRB-328 J2 turns the chip into the control. That creates two things a gate
  has to watch, and they pull in opposite directions:

      the WIDENING   a school_admin can import into any class in the school
      the LIMIT      a plain teacher can import into her own classes and no
                     others, INCLUDING when a `?class=` in the URL asks her to

  A gate that only drove the widening would go green against a page that let
  everybody into everything, which is precisely what a widening must not
  become. So the same page, the same fixture and the SAME FOREIGN CLASS ID are
  driven twice, one `staff_scopes` row apart, and demanded to answer
  differently. That row is the only difference between B2 and B4 below.

⚑ TWO SECTIONS, AND WHY NEITHER IS THE WHOLE PROOF.

  SECTION B — stubbed, no network, runs on every push.
      The real page, the real `shared/class-entry.js`, the real
      `shared/teacher-admin-nav.js` predicate and the page's own rendering all
      run unmodified; only the Supabase client, the guard and PapaParse are
      stubbed, and the stub mechanism is IMPORTED from `import_year_drive`
      rather than retyped so the two cannot drift.
      ⚠️ THE STUB MODELS ROW VISIBILITY, IT DOES NOT PROVE RLS — the same
      honest limit `teacher_admin_foreign_class_drive.py` states. What Section
      B proves is the half no SQL can reach: given those rows, the picker
      lists what it should, groups it how it should, refuses the foreign
      preselect, and the CHOSEN class — not the file's class column — is what
      reaches `functions.invoke('roster-import', …)`.

  SECTION A — real sign-in, real RLS, a real import against TEST.
      A real school_admin opens a COLLEAGUE'S class page's import link, and
      the students land in THAT class. Read back from the database afterwards
      with the admin's own JWT, because a green success panel is a claim and a
      `class_members` row is a fact.
      ⚠️ IT WRITES ROWS ON TEST and cleans them up, so it never runs without
      `MRB_THROWAWAY_PASSWORD` — a push must not depend on the network and
      must certainly never write to a shared project by accident.

⚑ THE ASSERTION THAT MATTERS MOST, AND WHERE IT IS MADE.

  "The class is preselected" is scenery. The load-bearing claim is that a
  selection is a DESTINATION: every row lands in the chosen class and the
  file's own class column stops mattering. So the Section B fixture's CSV
  names a DIFFERENT class in its class column, and the check is on the body
  handed to `roster-import`, not on anything rendered. A page can show the
  right class in its header and send the file's class a screen later.

  Section A then proves the other end of the same claim on real data:
  `classesCreated == 0` (the class was FOUND, not duplicated) and the two
  synthetic pupils are members of that exact class id and of no other.

⛔ SCREENSHOTS GO OUTSIDE THE REPO by default (`/tmp`) — MRB-301's rule that a
  gate must not write into the tree it is attesting is clean. `--shots` is how
  MRB-328's own paired evidence was written under `docs/mrb328/shots/`.

⛔ NO REAL NAMES. Every person in Section B is invented. Every person Section A
  touches is a throwaway fixture on the sandbox project, and the two pupils it
  creates are named for this ticket and deleted at the end of the run.
"""

import argparse
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)
os.chdir(REPO)

import ks3_browser as cdp
# The stub mechanism and the CSV-feeding trick from the file that established
# both against THIS page. Imported, never copied: a second Supabase stub is a
# second thing to keep true, and it would drift on the first schema change.
import import_year_drive as iy


# ══════════════════════════════════════════════════════════════════════════
# SECTION B — the picker's scope, its grouping, and the refusal
# ══════════════════════════════════════════════════════════════════════════

TEACHER = "11111111-1111-1111-1111-111111111111"
SCHOOL = "55555555-5555-5555-5555-555555555555"

# Two years, and `is_current` still points at the wrong one — MRB-307's trap,
# kept because the picker is scoped to the WORKING year and a fixture with one
# year cannot tell a correct scope from no scope at all.
YEARS = [
    {"id": "ay-2025", "name": "2025-26", "start_date": "2025-09-01",
     "end_date": "2026-08-31", "is_current": True,
     "school_id": SCHOOL, "deleted_at": None},
    {"id": "ay-2026", "name": "2026-27", "start_date": "2026-09-01",
     "end_date": "2027-08-31", "is_current": False,
     "school_id": SCHOOL, "deleted_at": None},
]
WORKING_YEAR_ID = "ay-2026"
WHEN = "2026-09-04T09:00:00"      # frozen, so the working year is forever 2026-27

# ── The school's classes. Every row in here is doing a job. ────────────────
#
#   the three `10b/Sc…` classes    NATURAL ORDER. Lexicographically they sort
#                                  Sc1, Sc10, Sc2; a teacher means Sc1, Sc2,
#                                  Sc10. One of those is a bug and a fixture
#                                  with a single class per year cannot see it.
#   `Sixth Form Science`           NO year_group and no leading number, so it
#                                  cannot be grouped. It belongs in the
#                                  ungrouped tail, not in an invented
#                                  "Other" group and not silently dropped.
#   `7h/Sc5` in the STALE year     THE SAME NAME as a working-year class. If
#                                  the picker forgets to scope on the year it
#                                  shows two identical options and the teacher
#                                  cannot tell which is which — MRB-307's
#                                  defect wearing a dropdown.
#   `10b/Sc10`                     the FOREIGN class. Somebody else teaches it,
#                                  and it is the id both B2 and B4 arrive with.
CLASSES = [
    {"id": "cls-7a",  "name": "7h/Sc5",   "year_group": 7,  "key_stage": "KS3",
     "tier": None, "science_pathway": None,
     "academic_year_id": WORKING_YEAR_ID, "school_id": SCHOOL, "deleted_at": None},
    {"id": "cls-8a",  "name": "8r/Sc2",   "year_group": 8,  "key_stage": "KS3",
     "tier": None, "science_pathway": None,
     "academic_year_id": WORKING_YEAR_ID, "school_id": SCHOOL, "deleted_at": None},
    {"id": "cls-9a",  "name": "9r/Sc1",   "year_group": 9,  "key_stage": "KS3",
     "tier": None, "science_pathway": None,
     "academic_year_id": WORKING_YEAR_ID, "school_id": SCHOOL, "deleted_at": None},
    {"id": "cls-10a", "name": "10b/Sc1",  "year_group": 10, "key_stage": "KS4",
     "tier": "higher", "science_pathway": "triple",
     "academic_year_id": WORKING_YEAR_ID, "school_id": SCHOOL, "deleted_at": None},
    {"id": "cls-10b", "name": "10b/Sc2",  "year_group": 10, "key_stage": "KS4",
     "tier": "foundation", "science_pathway": "combined",
     "academic_year_id": WORKING_YEAR_ID, "school_id": SCHOOL, "deleted_at": None},
    {"id": "cls-10c", "name": "10b/Sc10", "year_group": 10, "key_stage": "KS4",
     # ⚠️ NO tier and NO pathway, deliberately. This is the class B4 and B5
     # import into, and an existing class whose course is unset is exactly
     # where "ask again for something the import cannot write" would bite.
     "tier": None, "science_pathway": None,
     "academic_year_id": WORKING_YEAR_ID, "school_id": SCHOOL, "deleted_at": None},
    {"id": "cls-11a", "name": "11r/Sc1",  "year_group": 11, "key_stage": "KS4",
     "tier": "higher", "science_pathway": "combined",
     "academic_year_id": WORKING_YEAR_ID, "school_id": SCHOOL, "deleted_at": None},
    {"id": "cls-nx",  "name": "Sixth Form Science", "year_group": None,
     "key_stage": None, "tier": None, "science_pathway": None,
     "academic_year_id": WORKING_YEAR_ID, "school_id": SCHOOL, "deleted_at": None},
    {"id": "cls-old", "name": "7h/Sc5",   "year_group": 7,  "key_stage": "KS3",
     "tier": None, "science_pathway": None,
     "academic_year_id": "ay-2025", "school_id": SCHOOL, "deleted_at": None},
]

OWN_A = "cls-8a"      # the teacher's own, Year 8
OWN_B = "cls-10b"     # the teacher's own, Year 10 — two years, so she is grouped
FOREIGN = "cls-10c"   # somebody else's, Year 10
FOREIGN_NAME = "10b/Sc10"

OTHER_TEACHER = "99999999-9999-9999-9999-999999999999"

LINKS = [
    {"class_id": OWN_A, "teacher_id": TEACHER, "ended_at": None, "deleted_at": None},
    {"class_id": OWN_B, "teacher_id": TEACHER, "ended_at": None, "deleted_at": None},
    {"class_id": FOREIGN, "teacher_id": OTHER_TEACHER, "ended_at": None, "deleted_at": None},
    # A SECOND teacher on the foreign class: the review step names the class
    # AND its teachers, and "names its teachers" is not testable against one.
    {"class_id": FOREIGN, "teacher_id": "99999999-9999-9999-9999-999999999998",
     "ended_at": None, "deleted_at": None},
    # An ENDED link of the teacher's own on the foreign class. It must not put
    # that class in her list: `ended_at` is how a class stops being yours in
    # September, and a picker that ignored it would hand every teacher every
    # class she has ever taught.
    {"class_id": FOREIGN, "teacher_id": TEACHER,
     "ended_at": "2026-07-20T00:00:00+00:00", "deleted_at": None},
]

# Invented staff. The two on the foreign class are what the review chip must
# read back; nobody here is a real member of staff anywhere.
STAFF = [
    {"id": TEACHER, "first_name": "Ada", "last_name": "Nwosu",
     "display_name": "Ms Nwosu", "role": "teacher", "school_id": SCHOOL},
    {"id": OTHER_TEACHER, "first_name": "Priya", "last_name": "Raman",
     "display_name": "Ms Raman", "role": "teacher", "school_id": SCHOOL},
    {"id": "99999999-9999-9999-9999-999999999998", "first_name": "Tomas",
     "last_name": "Lindqvist", "display_name": "Mr Lindqvist",
     "role": "teacher", "school_id": SCHOOL},
]

ADMIN_SCOPE = [{"profile_id": TEACHER, "scope": "school_admin",
                "started_at": "2026-01-01T00:00:00+00:00",
                "ended_at": None, "deleted_at": None}]

# ⚠️ THE CLASS COLUMN NAMES A CLASS THAT IS NOT THE CHOSEN ONE. That is the
# whole point of B5: a selection is a destination, so these two rows must land
# in the class the header names and this column must stop mattering.
# `example.invalid` is reserved by RFC 2606 and can never route anywhere.
CSV_OTHER_CLASS = (
    "email,first_name,last_name,class\n"
    "pupil.one@example.invalid,Pupil,One,9r/Sc1\n"
    "pupil.two@example.invalid,Pupil,Two,9r/Sc1\n")

# The untouched multi-class path: no selection, two classes out of one file.
CSV_TWO_CLASSES = (
    "email,first_name,last_name,class\n"
    "pupil.one@example.invalid,Pupil,One,7h/Sc5\n"
    "pupil.two@example.invalid,Pupil,Two,9r/Sc1\n")


def tables(admin_scope):
    return {
        "academic_years": YEARS,
        "classes": CLASSES,
        "class_teachers": LINKS,
        "profiles": STAFF,
        "subjects": [{"id": "subj-science", "name": "Science", "active": True}],
        "staff_scopes": ADMIN_SCOPE if admin_scope else [],
    }


# Reads the picker back the way the browser actually built it — optgroups in
# document order, options inside them — so a check can assert the GROUPING and
# not merely the membership.
READ_PICKER_JS = r"""(function () {
  var sel = document.getElementById('import-target-select');
  var chip = document.getElementById('import-target');
  var val = document.getElementById('import-target-value');
  if (!sel) { return JSON.stringify({present: false}); }
  var groups = [];
  var flat = [];
  Array.prototype.forEach.call(sel.children, function (node) {
    if (node.tagName === 'OPTGROUP') {
      groups.push({label: node.label,
                   options: Array.prototype.map.call(node.children,
                     function (o) { return o.textContent; })});
      Array.prototype.forEach.call(node.children,
        function (o) { flat.push(o.textContent); });
    } else if (node.value !== '') {
      flat.push(node.textContent);
      groups.push({label: null, options: [node.textContent]});
    }
  });
  return JSON.stringify({
    present: true,
    hidden: sel.hidden,
    blank: sel.options.length ? sel.options[0].textContent : null,
    value: sel.value,
    selectedText: sel.selectedIndex >= 0 ? sel.options[sel.selectedIndex].textContent : '',
    groups: groups,
    flat: flat,
    chipPending: chip ? chip.classList.contains('is-pending') : null,
    /* ⚠️ NOT innerText — a <select>'s innerText is every option's text, so a
       chip carrying the picker reads as the whole class list. The IDS of the
       chip's element children are the honest way to ask "did anything new get
       added to say this?": three, and the same three, on every step. */
    chipChildren: chip ? Array.prototype.map.call(chip.children,
      function (e) { return e.id || e.tagName; }) : [],
    valueText: val ? (val.textContent || '').trim() : '',
    valueHidden: val ? !!val.hidden : null
  });
})()"""

# The teacher's own press. `sel.value = …` alone changes nothing the page can
# hear, so the change event is dispatched exactly as a real selection would.
PICK_JS = r"""(function () {
  var sel = document.getElementById('import-target-select');
  if (!sel) { return 'no select'; }
  sel.value = %s;
  if (sel.value !== %s) { return 'no such option'; }
  sel.dispatchEvent(new Event('change', {bubbles: true}));
  return 'ok';
})()"""

# A native <select> shows one option when closed and CDP cannot open its
# dropdown, so the grouped list would photograph as a single word. `size`
# turns the same element into a list box — the browser's own rendering of the
# real optgroups, not a mock-up of them — and it is put back afterwards.
EXPAND_JS = r"""(function () {
  var sel = document.getElementById('import-target-select');
  if (!sel) { return 0; }
  var n = sel.querySelectorAll('option').length +
          sel.querySelectorAll('optgroup').length;
  sel.size = Math.min(n, 18);
  return n;
})()"""
COLLAPSE_JS = ("(function(){var s=document.getElementById('import-target-select');"
               "if(s){s.removeAttribute('size');}return 'ok';})()")

FEED_NAMED_JS = r"""
(function () {
  var input = document.getElementById('file-input');
  if (!input) { return 'no #file-input'; }
  var f = new File([window.__MRB_CSV__], 'roster.csv', {type: 'text/csv'});
  var dt = new DataTransfer();
  dt.items.add(f);
  input.files = dt.files;
  input.dispatchEvent(new Event('change', {bubbles: true}));
  return 'ok';
})()
"""


def open_import(b, base, *, admin_scope, class_param, csv, shots_prefix=None):
    """One stubbed load of teacher/import.html, as one persona.

    ⚠️ `cdp.Browser.page()` DOES NOT GIVE YOU A NEW TARGET. It is
    `attach().goto(url)` — one page target for the whole browser — so every
    `Page.addScriptToEvaluateOnNewDocument` here ACCUMULATES on that one
    target, newest last. This is survivable for the personas below only
    because `import_year_drive`'s `hold()` defines its globals
    `configurable: true` and each persona's script is added after the last, so
    the newest `__MRB_STUB__` and the newest `hold()` win.

    It is NOT survivable across the two sections, and that is why Section A
    gets a browser of its own in `main()`: the stub client has no
    `auth.setSession`, so a real sign-in on a target still carrying it dies
    with `c.auth.setSession is not a function` — measured, not guessed.
    """
    pre = "window.__MRB_STUB__=%s;\n" % json.dumps(
        {"uid": TEACHER, "school": SCHOOL, "tables": tables(admin_scope),
         "newBackend": False, "landedYear": "2026-27", "landedClasses": []})
    pre += "window.__MRB_CSV__=%s;\n" % json.dumps(csv)
    pre += iy.STUB_JS + (iy.FREEZE % WHEN)

    p = b.page("about:blank", settle=0.2)
    p.send("Page.addScriptToEvaluateOnNewDocument", {"source": pre})
    p.send("Network.enable")
    # A push gate must not be able to go amber because a CDN is slow.
    p.send("Network.setBlockedURLs", {"urls": [
        "*cdn.jsdelivr.net*", "*cdnjs.cloudflare.com*", "*supabase.co*"]})

    url = base + "/teacher/import.html"
    if class_param:
        url += "?class=" + class_param
    p.goto(url, settle=0.6)

    iy.wait_for(p, "document.body.style.display === 'block'",
                "the guard to reveal the page")
    # The picker is built only after the working year resolves — it is scoped
    # to that year — so waiting on the year is waiting on the picker.
    iy.wait_for(p,
                "(function(){var n=document.getElementById('working-year-note');"
                "return !!n && n.style.display !== 'none' &&"
                " n.textContent.indexOf('Checking') === -1;})()",
                "the working year to resolve")
    iy.wait_for(p,
                "(function(){var s=document.getElementById('import-target-select');"
                "return !!s && s.options.length > 0;})()",
                "the class picker to be built")
    if shots_prefix:
        # TWO frames, because the expanded one is not what ships. `size` is a
        # screenshot technique (a native dropdown cannot be opened from CDP),
        # and it stretches the pill's 999px border into an oval around a list
        # box — an artefact of the photograph, not of the page. The collapsed
        # frame is the chip as a teacher meets it.
        p.screenshot(shots_prefix + "-chip.png", width=1280)
        p.eval(EXPAND_JS)
        p.screenshot(shots_prefix + "-list.png", width=1280)
        p.eval(COLLAPSE_JS)
    return p


def section_b(b, base, shots, check):
    print("\n─── SECTION B · the picker's scope, stubbed, no network ─────────")

    # ── B1 · a plain teacher sees HER classes, grouped, naturally ordered ──
    print("\n  B1  plain teacher, no ?class=")
    p = open_import(b, base, admin_scope=False, class_param=None,
                    csv=CSV_TWO_CLASSES)
    got = json.loads(p.eval(READ_PICKER_JS))
    print("      groups: %s" % json.dumps(got["groups"]))
    check(got["flat"] == ["8r/Sc2", "10b/Sc2"],
          "B1 the list is HER two classes and nothing else",
          json.dumps(got["flat"]))
    check([g["label"] for g in got["groups"]] == ["Year 8", "Year 10"],
          "B1 grouped Year 8 → Year 10 because she spans two years",
          json.dumps([g["label"] for g in got["groups"]]))
    check(FOREIGN_NAME not in got["flat"],
          "B1 the class she USED to teach (ended_at set) is not offered")
    check(got["blank"] == "Not chosen yet",
          "B1 the blank option reuses the chip's own pending words",
          repr(got["blank"]))
    check(got["value"] == "" and got["chipPending"] is True,
          "B1 nothing is chosen and the chip says so",
          "%r / %r" % (got["value"], got["chipPending"]))

    # ── B2 · THE REFUSAL. A foreign ?class= must not select anything ───────
    print("\n  B2  plain teacher, ?class=<a class she does not teach>")
    p = open_import(b, base, admin_scope=False, class_param=FOREIGN,
                    csv=CSV_TWO_CLASSES,
                    shots_prefix=os.path.join(shots, "b2-teacher-foreign-class-refused"))
    got = json.loads(p.eval(READ_PICKER_JS))
    check(got["value"] == "",
          "B2 the foreign class is REFUSED — nothing is selected", repr(got["value"]))
    check(FOREIGN_NAME not in got["flat"],
          "B2 and it is not even in her list", json.dumps(got["flat"]))
    check(got["chipPending"] is True,
          "B2 the chip is still in its pending state")
    errs = [e for e in p.console_errors()
            if "favicon" not in e and "ERR_BLOCKED_BY_CLIENT" not in e
            and "net::ERR_" not in e]
    check(not errs, "B2 refusing it threw nothing", json.dumps(errs[:3]))

    # ── B3 · the control. Her OWN id in the same parameter DOES select ─────
    print("\n  B3  plain teacher, ?class=<her own class>")
    p = open_import(b, base, admin_scope=False, class_param=OWN_A,
                    csv=CSV_TWO_CLASSES)
    got = json.loads(p.eval(READ_PICKER_JS))
    check(got["value"] == OWN_A and got["selectedText"] == "8r/Sc2",
          "B3 her own class preselects — so B2 is a refusal, not an inert page",
          "%r / %r" % (got["value"], got["selectedText"]))

    # ── B4 · ONE staff_scopes row later, the SAME id is admitted ───────────
    print("\n  B4  school_admin, the SAME ?class= id as B2")
    p = open_import(b, base, admin_scope=True, class_param=FOREIGN,
                    csv=CSV_OTHER_CLASS,
                    shots_prefix=os.path.join(shots, "b4-admin-grouped-list"))
    got = json.loads(p.eval(READ_PICKER_JS))
    print("      groups: %s" % json.dumps(got["groups"]))
    check(got["value"] == FOREIGN and got["selectedText"] == FOREIGN_NAME,
          "B4 a colleague's class IS preselected for an admin",
          "%r / %r" % (got["value"], got["selectedText"]))
    labels = [g["label"] for g in got["groups"]]
    check(labels == ["Year 7", "Year 8", "Year 9", "Year 10", "Year 11", None],
          "B4 grouped Year 7 → Year 11, with the un-yeared class in the tail",
          json.dumps(labels))
    y10 = [g["options"] for g in got["groups"] if g["label"] == "Year 10"]
    check(y10 == [["10b/Sc1", "10b/Sc2", "10b/Sc10"]],
          "B4 natural order inside a year (Sc1, Sc2, Sc10 — not Sc1, Sc10, Sc2)",
          json.dumps(y10))
    check(got["flat"].count("7h/Sc5") == 1,
          "B4 the STALE year's twin of 7h/Sc5 is not offered a second time",
          json.dumps(got["flat"]))

    # ── B5 · a selection is a DESTINATION, and the payload is the proof ────
    print("\n  B5  school_admin, chosen class vs the file's own class column")
    p.eval(FEED_NAMED_JS)
    iy.wait_for(p, "!document.getElementById('to-screen-2').disabled",
                "the file to parse")
    p.eval(iy.CLICK_JS % "to-screen-2")
    iy.wait_for(p, "document.getElementById('screen-2').classList.contains('show')",
                "screen 2 to show")
    rows = json.loads(p.eval(
        "JSON.stringify(Array.prototype.map.call("
        "document.querySelectorAll('#class-settings-list .class-setting[data-class]'),"
        "function(e){return e.getAttribute('data-class');}))"))
    check(rows == [FOREIGN_NAME],
          "B5 screen 2 sets up the CHOSEN class, not the file's 9r/Sc1",
          json.dumps(rows))
    check(p.eval("document.getElementById('map-class-row').style.display") == "none"
          and p.eval("document.getElementById('single-class-row').style.display") == "none",
          "B5 the file's class controls are gone — one question, one control")
    # ⚠️ 10b/Sc10 is a Year 10 class with NO tier and NO pathway on its row.
    # If the wizard still demanded Combined/Triple here it would be demanding
    # something `roster-import` cannot write for a class it FINDS.
    check(not p.eval("document.getElementById('to-screen-3').disabled"),
          "B5 an existing class is not asked to restate a course it already has")
    p.eval(iy.CLICK_JS % "to-screen-3")
    iy.wait_for(p, "window.__MRB_INVOKES__.length >= 1", "the dry-run invoke")
    body = json.loads(p.eval("JSON.stringify(window.__MRB_INVOKES__[0].body)"))
    sent_classes = [c["name"] for c in body["classes"]]
    sent_rows = sorted(set(s["className"] for s in body["students"]))
    check(sent_classes == [FOREIGN_NAME],
          "B5 THE PAYLOAD names only the chosen class", json.dumps(sent_classes))
    check(sent_rows == [FOREIGN_NAME],
          "B5 THE PAYLOAD lands every row in it, whatever the CSV column said",
          json.dumps(sent_rows))
    check(body.get("academicYearName") == "2026-27",
          "B5 and still into the working year (MRB-307 holds)",
          repr(body.get("academicYearName")))

    # ── B6 · the review step names the class AND who teaches it ────────────
    iy.wait_for(p,
                "(function(){var v=document.getElementById('import-target-value');"
                "return !!v && v.textContent.indexOf('·') === 0;})()",
                "the chip to name the class's teachers")
    got = json.loads(p.eval(READ_PICKER_JS))
    print("      chip: %r" % got["valueText"])
    check(got["valueText"] == "· Priya Raman, Tomas Lindqvist",
          "B6 the review chip names both teachers of the class",
          repr(got["valueText"]))
    check(got["selectedText"] == FOREIGN_NAME,
          "B6 with the class itself still in the control, not repeated in the text")
    check(got["chipChildren"] == ["import-target-label", "import-target-select",
                                  "import-target-value"],
          "B6 and nothing was ADDED to say it — the same three-part chip",
          json.dumps(got["chipChildren"]))

    # ── B7 · with NO selection the multi-class file still works ────────────
    print("\n  B7  no selection — the untouched multi-class path")
    p = open_import(b, base, admin_scope=True, class_param=None,
                    csv=CSV_TWO_CLASSES)
    p.eval(FEED_NAMED_JS)
    iy.wait_for(p, "!document.getElementById('to-screen-2').disabled",
                "the file to parse")
    p.eval(iy.CLICK_JS % "to-screen-2")
    iy.wait_for(p, "document.getElementById('screen-2').classList.contains('show')",
                "screen 2 to show")
    rows = json.loads(p.eval(
        "JSON.stringify(Array.prototype.map.call("
        "document.querySelectorAll('#class-settings-list .class-setting[data-class]'),"
        "function(e){return e.getAttribute('data-class');}))"))
    check(sorted(rows) == ["7h/Sc5", "9r/Sc1"],
          "B7 two classes still come out of one file", json.dumps(rows))
    check(p.eval("document.getElementById('map-class-row').style.display") != "none",
          "B7 and the file's class column is still the control that decides")
    got = json.loads(p.eval(READ_PICKER_JS))
    check(got["valueText"] in ("7h/Sc5 and 9r/Sc1", "9r/Sc1 and 7h/Sc5"),
          "B7 the chip still reads the file's classes when none is chosen",
          repr(got["valueText"]))

    # ── B8 · choosing, then un-choosing, hands the question back ───────────
    print("\n  B8  choose a class, then return to 'Not chosen yet'")
    p.eval(PICK_JS % (json.dumps(OWN_A), json.dumps(OWN_A)))
    iy.wait_for(p,
                "document.querySelectorAll('#class-settings-list "
                ".class-setting[data-class]').length === 1",
                "the chosen class to take over screen 2")
    p.eval(PICK_JS % (json.dumps(""), json.dumps("")))
    iy.wait_for(p,
                "document.querySelectorAll('#class-settings-list "
                ".class-setting[data-class]').length === 2",
                "the file to get the question back")
    check(p.eval("document.getElementById('map-class-row').style.display") != "none",
          "B8 un-choosing restores the file's class column")


# ══════════════════════════════════════════════════════════════════════════
# SECTION A — a real admin, a real colleague's class, a real import on TEST
# ══════════════════════════════════════════════════════════════════════════

REF = "qeppkiswvclkkwbxmlok"                  # TEST. Never production.
URL = "https://%s.supabase.co" % REF
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
ENV_SWITCH = "MRB_THROWAWAY_PASSWORD"

# The MRB-326 fixture, reused rather than reseeded. The admin teaches NOTHING,
# which is what makes every class in the school a colleague's class.
ADMIN_EMAIL = "mrb326_admin@throwaway.test"
A_SCHOOL = "d0233615-3ee7-4b1b-a8ff-c912c5196d62"
A_YEAR = "2f560a43-73b9-422a-8fc7-ec46524a288a"

# HZ 10A Science — taught by TWO people, which is why it and not one of the
# single-teacher classes: "names the class AND its teachers" needs two.
A_CLASS = "ee000000-0000-0000-0000-000000000401"
A_CLASS_NAME = "HZ 10A Science"
# Somewhere else in the same school, to prove the pupils did not land wide.
A_OTHER_CLASS = "ee000000-0000-0000-0000-000000000402"

# The two pupils this run creates and then deletes. Named for the ticket so
# that anything left behind by a crashed run is identifiable at a glance.
A_PUPILS = [
    {"email": "mrb328_pupil_alpha@example.invalid",
     "first": "Mrb328", "last": "Alpha"},
    {"email": "mrb328_pupil_bravo@example.invalid",
     "first": "Mrb328", "last": "Bravo"},
]
A_CSV = ("email,first_name,last_name,class\n" +
         "".join("%s,%s,%s,NOT THIS CLASS\n" % (p["email"], p["first"], p["last"])
                 for p in A_PUPILS))


def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def service_key():
    """The TEST service-role key, for CLEANUP ONLY — or None.

    ⚠️ IT PROVES NOTHING. Every assertion in Section A runs on the admin's own
    JWT under real RLS. This key exists for the one job no user JWT can do:
    deleting an auth user this run created. Absent, cleanup degrades to
    listing what was left and saying so.
    """
    path = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env"
    try:
        for line in open(path, encoding="utf-8"):
            if line.startswith("SUPABASE_SERVICE_ROLE_KEY="):
                return line.split("=", 1)[1].strip()
    except OSError:
        pass
    return None


def call(method, path, key, bearer, body=None, prefer=None):
    headers = {"apikey": key, "Authorization": "Bearer " + bearer,
               "Content-Type": "application/json"}
    if prefer:
        headers["Prefer"] = prefer
    req = urllib.request.Request(
        URL + path, data=(json.dumps(body).encode() if body is not None else None),
        headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=90, context=CTX) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw.strip() else None)
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, raw[:300]


def sign_in(email, password, key):
    """⚠️ VERIFY OVER HTTP, NOT IN THE BROWSER. A sign-in that fails inside
    `auth.setSession` presents as a blank page and a silent console, which is
    indistinguishable from a rendering bug."""
    st, body = call("POST", "/auth/v1/token?grant_type=password", key, key,
                    {"email": email, "password": password})
    if st != 200 or not isinstance(body, dict) or "access_token" not in body:
        raise SystemExit(
            "\n❌ sign-in FAILED for %s — HTTP %s\n   %s\n" % (email, st, json.dumps(body)[:300]))
    return body


def section_a(b, base, shots, check, password):
    print("\n─── SECTION A · a real admin, real RLS, a real import on TEST ───")

    key = anon_key()
    admin = sign_in(ADMIN_EMAIL, password, key)
    jwt = admin["access_token"]
    A_ID = admin["user"]["id"]
    print("      admin %s" % A_ID)

    # Guard the premise. If the admin ever acquires a class of her own, "opens
    # a colleague's class" stops being what this measures and the run would go
    # green having proved something easier.
    st, links = call("GET", "/rest/v1/class_teachers?select=class_id&teacher_id=eq.%s"
                            "&ended_at=is.null&deleted_at=is.null" % A_ID, key, jwt)
    check(st == 200 and links == [],
          "A0 the fixture: the admin teaches no class at all", repr(links))

    # ── open the page exactly as class-detail.html links to it ─────────────
    p = b.page("%s/leaderboard.html?env=test" % base, settle=2.0)
    signed = p.eval("""
      (async function () {
        var c = window.supabase.createClient(%s, %s);
        var r = await c.auth.setSession({access_token: %s, refresh_token: %s});
        return r.error ? 'error: ' + r.error.message : 'ok';
      })()
    """ % (json.dumps(URL), json.dumps(key),
           json.dumps(jwt), json.dumps(admin["refresh_token"])))
    check(signed == "ok", "A1 the browser is really signed in", repr(signed))

    p.set_viewport(1280, 1400)
    p.goto("%s/teacher/import.html?class=%s&env=test" % (base, A_CLASS), settle=1.0)
    iy.wait_for(p, "document.body.style.display === 'block'", "the guard to reveal the page", 30)
    iy.wait_for(p,
                "(function(){var s=document.getElementById('import-target-select');"
                "return !!s && s.options.length > 1;})()",
                "the class picker to load from the real project", 30)

    got = json.loads(p.eval(READ_PICKER_JS))
    print("      picker: %s" % json.dumps([g["label"] for g in got["groups"]]))
    check(got["value"] == A_CLASS and got["selectedText"] == A_CLASS_NAME,
          "A2 the colleague's class arrived PRESELECTED from ?class=",
          "%r / %r" % (got["value"], got["selectedText"]))
    check(len([g for g in got["groups"] if g["label"]]) > 1,
          "A2 and the school's classes came back grouped by year",
          json.dumps([g["label"] for g in got["groups"]]))
    p.screenshot(os.path.join(shots, "a2-admin-preselect-foreign-class-chip.png"),
                 width=1280)
    p.eval(EXPAND_JS)
    p.screenshot(os.path.join(shots, "a2-admin-preselect-foreign-class-list.png"),
                 width=1280)
    p.eval(COLLAPSE_JS)

    # ── the import itself ─────────────────────────────────────────────────
    p.eval("window.__MRB_CSV__ = %s;" % json.dumps(A_CSV))
    check(p.eval(FEED_NAMED_JS) == "ok", "A3 the synthetic roster was fed to the page")
    iy.wait_for(p, "!document.getElementById('to-screen-2').disabled", "the file to parse")
    p.eval(iy.CLICK_JS % "to-screen-2")
    iy.wait_for(p, "document.getElementById('screen-2').classList.contains('show')",
                "screen 2 to show")
    rows = json.loads(p.eval(
        "JSON.stringify(Array.prototype.map.call("
        "document.querySelectorAll('#class-settings-list .class-setting[data-class]'),"
        "function(e){return e.getAttribute('data-class');}))"))
    check(rows == [A_CLASS_NAME],
          "A3 screen 2 sets up the chosen class, not the CSV's 'NOT THIS CLASS'",
          json.dumps(rows))

    iy.wait_for(p, "!document.getElementById('to-screen-3').disabled",
                "the year and the staff lists to unblock review", 30)
    p.eval(iy.CLICK_JS % "to-screen-3")
    iy.wait_for(p,
                "(function(){var s=document.getElementById('preview-sentence');"
                "return !!s && s.style.display !== 'none';})()",
                "the dry run to come back from the real edge function", 60)
    got = json.loads(p.eval(READ_PICKER_JS))
    print("      review chip: %r" % got["valueText"])
    check(got["valueText"].startswith("· ") and "," in got["valueText"],
          "A4 the review chip names the class's real teachers",
          repr(got["valueText"]))
    p.screenshot(os.path.join(shots, "a4-admin-review-names-teachers.png"), width=1280)

    iy.wait_for(p, "!document.getElementById('confirm-import').disabled",
                "a clean dry run to enable Confirm", 30)
    p.eval(iy.CLICK_JS % "confirm-import")
    iy.wait_for(p, "document.getElementById('success-panel').classList.contains('show')",
                "the real import to complete", 90)
    summary = p.eval("document.getElementById('success-summary').textContent"
                     ".replace(/[\\s\\u00a0]+/g,' ').trim()")
    print("      %s" % summary)
    p.screenshot(os.path.join(shots, "a5-admin-import-complete.png"), width=1280)
    # The page's OWN account of what it did, and the half of "landed in THAT
    # class" that A8 checks from the other side: an import that had made a
    # second class of the same name would say "created", not "existing".
    check("existing class" in summary and "creat" not in summary.lower(),
          "A5 the class was FOUND, not created", repr(summary))

    # ── ⚑ THE READ-BACK. A success panel is a claim; a row is a fact. ─────
    #
    # With the ADMIN'S OWN JWT, under the real policies — a read that a
    # service-role key would have made meaningless.
    st, members = call("GET",
                       "/rest/v1/class_members?select=student_id,class_id"
                       "&class_id=eq.%s&left_at=is.null&deleted_at=is.null" % A_CLASS,
                       key, jwt)
    ids = [m["student_id"] for m in (members or [])] if st == 200 else []
    st2, people = call("GET",
                       "/rest/v1/profiles?select=id,first_name,last_name,role"
                       "&first_name=eq.Mrb328", key, jwt)
    landed = [q for q in (people or [])] if st2 == 200 else []
    landed_ids = sorted(q["id"] for q in landed)
    print("      pupils created: %s" % json.dumps(
        sorted("%s %s" % (q["first_name"], q["last_name"]) for q in landed)))

    check(len(landed) == len(A_PUPILS),
          "A6 both synthetic pupils exist as profiles", "%d found" % len(landed))
    check(all(q["role"] == "student" for q in landed),
          "A6 and they are students, not staff")
    check(landed_ids and all(i in ids for i in landed_ids),
          "A7 THEY ARE MEMBERS OF THE CHOSEN CLASS — read back from TEST",
          "class %s members: %d" % (A_CLASS, len(ids)))

    st3, elsewhere = call("GET",
                          "/rest/v1/class_members?select=student_id,class_id"
                          "&class_id=eq.%s&left_at=is.null&deleted_at=is.null"
                          % A_OTHER_CLASS, key, jwt)
    stray = [m for m in (elsewhere or []) if m["student_id"] in landed_ids]
    check(st3 == 200 and not stray,
          "A7 and of no other class — the import did not land wide", json.dumps(stray))

    # `classesCreated == 0` is the other half of "landed in THAT class": a
    # page that sent the right name into the wrong year would have made a
    # SECOND class of the same name and every membership check above would
    # still pass, against a class nobody teaches.
    st4, twins = call("GET",
                      "/rest/v1/classes?select=id,name,academic_year_id"
                      "&school_id=eq.%s&name=eq.%s&deleted_at=is.null"
                      % (A_SCHOOL, A_CLASS_NAME.replace(" ", "%20")), key, jwt)
    check(st4 == 200 and len(twins or []) == 1 and twins[0]["id"] == A_CLASS,
          "A8 no second class of that name was created", json.dumps(twins))

    return landed_ids


def cleanup(landed_ids, check):
    """Everything this run wrote, removed. ⚠️ SERVICE ROLE, and only here."""
    svc = service_key()
    if not svc:
        print("\n   ⚠️  no service-role key — LEAVING these profiles on TEST:")
        for i in landed_ids:
            print("       profiles/auth.users %s" % i)
        return
    for i in landed_ids:
        call("DELETE", "/rest/v1/class_members?student_id=eq.%s" % i, svc, svc)
        call("DELETE", "/rest/v1/profiles?id=eq.%s" % i, svc, svc)
        st, _ = call("DELETE", "/auth/v1/admin/users/%s" % i, svc, svc)
        print("      cleaned %s (auth delete HTTP %s)" % (i, st))
    st, left = call("GET", "/rest/v1/profiles?select=id&first_name=eq.Mrb328", svc, svc)
    check(st == 200 and left == [],
          "A9 the run left nothing behind on TEST", json.dumps(left))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--section", choices=["a", "b", "both"], default="both")
    ap.add_argument("--shots", default="/tmp/mrb328-shots")
    ap.add_argument("--keep", action="store_true",
                    help="leave the rows Section A writes on TEST, and list them")
    args = ap.parse_args()
    os.makedirs(args.shots, exist_ok=True)

    fails = []

    def check(ok_, what, detail=""):
        print("      %s %s%s" % ("✅" if ok_ else "❌", what,
                                 ("  — " + detail) if detail else ""))
        if not ok_:
            fails.append(what)

    # THE REPO ROOT, not mrbadmus_site/. `teacher/import.html` is one of the
    # four hand-written teacher pages, so the repo copy is the source of truth
    # and the built copy is a stamp-restamped duplicate of it. Serving the root
    # also resolves /shared/*.js out of the same tree.
    server, port = cdp.serve(REPO)
    base = "http://127.0.0.1:%d" % port
    print("\n🔎  MRB-328 J2 — the import page's class picker")

    landed = []
    try:
        if args.section in ("b", "both"):
            with cdp.Browser() as b:
                section_b(b, base, args.shots, check)
        if args.section in ("a", "both"):
            password = os.environ.get(ENV_SWITCH)
            if not password:
                print("\n⏭  SECTION A SKIPPED — %s is not set.\n"
                      "    It signs in over the network and WRITES rows on the\n"
                      "    TEST project, so it never runs by accident.\n" % ENV_SWITCH)
            else:
                # ⚠️ ITS OWN BROWSER, and this is load-bearing rather than
                # tidy. `Browser.page()` reuses ONE page target, so Section
                # B's stub client and its CDN block would still be installed
                # here — and the stub has no `auth.setSession`, so the real
                # sign-in would die inside the browser with a TypeError that
                # looks nothing like "the stub is still loaded".
                with cdp.Browser() as b2:
                    landed = section_a(b2, base, args.shots, check, password)
    finally:
        if landed and not args.keep:
            print("\n   cleanup")
            cleanup(landed, check)
        elif landed:
            print("\n   --keep: left on TEST → %s" % json.dumps(landed))
        server.shutdown()

    print("\n   screenshots → %s" % args.shots)
    if fails:
        print("\n❌  %d FAILED\n" % len(fails))
        for f in fails:
            print("     · %s" % f)
        print()
        return 1
    print("\n✅  MRB-328 J2 picker drive: all checks passed\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
