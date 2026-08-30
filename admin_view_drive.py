#!/usr/bin/env python3
"""MRB-303 J2 — drive `teacher/admin.html`, the read-only school view.

    python3 admin_view_drive.py            # everything
    python3 admin_view_drive.py --shots DIR  # write screenshots somewhere

⚑ WHY THIS DRIVE IS SPLIT IN TWO, and it is the finding rather than a
  convenience.

  The NEGATIVE half signs in for real. `hz_rich` (hod scope) and `hz_amy`
  (plain teacher) have real passwords on the TEST project, so those personas
  are driven against the real database under real RLS: no Admin link in the
  nav, and the honest refusal when they type the URL by hand. Those are the
  security-critical cases and they are proved the strong way.

  The POSITIVE half cannot be. `hz_admin`, `hz_slt`, `hz_legacyadmin` and
  `hz_t2` have NO PASSWORD AT ALL on the TEST project — verified, not
  assumed: `auth.users.encrypted_password` is null for all four — and
  MRB-303's brief bans setting one, because that is a write. There is no
  JWT secret available locally to mint a token with either, and an unsigned
  token is refused by PostgREST, so the fake-session trick the KS4 chrome
  drive uses (which only ever needed the page to LOOK signed in) cannot
  reach real rows.

  So the positive half drives the REAL PAGE with a STUBBED CLIENT: the
  page's own guard, its own scope predicate, its own data layer
  (`teacher-data.js`'s `loadAcademicYears` and `loadClassMatrices`) and its
  own rendering all run unmodified, against fixture rows shaped exactly like
  the ones the real RLS policies return. What that proves is everything
  between the rows arriving and the pixels; what it does NOT prove is the
  RLS itself, which is proved separately by SQL and written up in the
  report. The two halves together cover what a single signed-in drive would
  have, and neither of them writes a byte to either project.

⚠️ THE FIXTURE IS CONSTRUCTED, NOT FOUND, and deliberately so — same
  reasoning as `teacher_behaviour.py`'s empty fixtures. Its shapes are taken
  from the real TEST rows (a co-taught class, a class nobody teaches, a
  teacher holding two subject links to one class, an EXPIRED hod grant, a
  legacy `role='admin'` with no scope row), but it also carries a CLAIMED
  invitation, which exists nowhere in either database today. That path —
  a claim must annotate the live teacher's row and must NOT render a second
  row — is otherwise untestable, and it is the one the ruling is most
  specific about.

⛔ SCREENSHOTS GO OUTSIDE THE REPO by default (`/tmp`). MRB-301 landed the
  rule the hard way: a gate must not write into the tree it is attesting is
  clean.
"""
import argparse, json, os, re, ssl, sys, urllib.request

REPO = "/Users/midebadmus/Documents/GitHub/mrbadmus-site"
sys.path.insert(0, REPO)
os.chdir(REPO)
import ks3_browser as cdp

REF = "qeppkiswvclkkwbxmlok"
URL = "https://%s.supabase.co" % REF
PORT = 5507
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")

# Set on these TEST fixtures by SQL in MRB-293. Fake accounts on a sandbox
# project; nothing here is a production credential.
DRIVE_PW = "mrb293-drive-only"

SCHOOL = "d0233615-3ee7-4b1b-a8ff-c912c5196d62"
YEAR = "2f560a43-73b9-422a-8fc7-ec46524a288a"

# The three subject ids the TEST rows actually use, so `derivePill` has
# something real to resolve.
SUBJ_SC = "26000000-0000-0000-0000-000000000001"
SUBJ_PH = "b7cc103d-53af-45d4-b9fc-4dba20994009"

ADMIN = "ee000000-0000-0000-0000-000000001005"     # Ada Nwosu, school_admin
SLT = "ee000000-0000-0000-0000-000000001006"       # Sam Vine, slt
LEGACY = "ee000000-0000-0000-0000-000000001011"    # Len Legacy, role=admin only
AMY = "ee000000-0000-0000-0000-000000001002"
BEN = "ee000000-0000-0000-0000-000000001003"
RICH = "ee000000-0000-0000-0000-000000001001"      # hod — NOT admin
OLIVE = "ee000000-0000-0000-0000-000000001004"     # hod, EXPIRED
NIA = "ee000000-0000-0000-0000-000000001007"       # no scope, no classes

NOW = "2026-08-30T00:00:00+00:00"
PAST = "2026-01-01T00:00:00+00:00"
EXPIRED = "2026-06-03T00:00:00+00:00"

C_CO = "ee000000-0000-0000-0000-000000000401"      # co-taught: Amy + Ben
C_RICH = "ee000000-0000-0000-0000-000000000402"    # Rich alone
C_NONE = "ee000000-0000-0000-0000-000000000403"    # NOBODY teaches it
C_DUP = "2a000000-0000-0000-0000-000000000002"     # one teacher, two links


def klass(cid, name, ks, yg):
    return {"id": cid, "name": name, "key_stage": ks, "year_group": yg,
            "academic_year_id": YEAR, "school_id": SCHOOL, "tier": None,
            "science_pathway": None, "assignment_day_of_week": None,
            "deleted_at": None}


CLASSES = [
    klass(C_CO, "10h/Sc1", "KS4", 10),
    klass(C_RICH, "10h/Ph1", "KS4", 10),
    klass(C_NONE, "9r/Sc4", "KS3", 9),
    klass(C_DUP, "8r/Sc1", "KS3", 8),
]


def link(cid, tid, sid):
    """A `class_teachers` row with the embeds PostgREST would have sent.

    The stub does not implement embedding — it serves rows as given — so the
    fixture carries `class` and `subject` already resolved, exactly as the
    real select's `class:class_id ( … )` and `subject:subject_id ( … )`
    would have returned them. That is what lets `loadClassMatrices` and
    `derivePill` run completely unmodified.
    """
    cls = [c for c in CLASSES if c["id"] == cid][0]
    return {"class_id": cid, "teacher_id": tid, "subject_id": sid,
            "deleted_at": None, "ended_at": None,
            "subject": {"id": sid,
                        "name": "Combined Science" if sid == SUBJ_SC else "Physics"},
            "class": dict(cls)}


LINKS = [
    link(C_CO, AMY, SUBJ_SC),
    link(C_CO, BEN, SUBJ_SC),            # co-taught — must show under BOTH
    link(C_RICH, RICH, SUBJ_PH),
    link(C_DUP, ADMIN, SUBJ_SC),
    link(C_DUP, ADMIN, SUBJ_PH),         # SAME teacher, second subject:
                                         # one class, not two
]


def member(cid, sid, first, last, left=None):
    return {"class_id": cid, "student_id": sid, "joined_at": PAST,
            "left_at": left, "deleted_at": None,
            "student": {"id": sid, "first_name": first, "last_name": last,
                        "avatar_url": None, "deleted_at": None}}


MEMBERS = [
    member(C_CO, "ee000000-0000-0000-0000-000000001101", "Stu", "One"),
    member(C_CO, "ee000000-0000-0000-0000-000000001102", "Stu", "Two"),
    member(C_RICH, "ee000000-0000-0000-0000-000000001103", "Stu", "Three"),
    # A departed student — must NOT be counted, on either code path.
    member(C_RICH, "ee000000-0000-0000-0000-000000001104", "Stu", "Gone", left=PAST),
    # On the class NOBODY teaches, so this count can only come from the
    # `countMembers` fallback — `loadClassMatrices` refuses this class.
    member(C_NONE, "ee000000-0000-0000-0000-000000001105", "Stu", "Five"),
    member(C_NONE, "ee000000-0000-0000-0000-000000001106", "Stu", "Six"),
    member(C_DUP, "ee000000-0000-0000-0000-000000001107", "Stu", "Seven"),
]

PROFILES = [
    {"id": ADMIN, "first_name": "Ada", "last_name": "Nwosu",
     "display_name": None, "role": "teacher", "school_id": SCHOOL, "deleted_at": None},
    {"id": SLT, "first_name": "Sam", "last_name": "Vine",
     "display_name": None, "role": "teacher", "school_id": SCHOOL, "deleted_at": None},
    {"id": LEGACY, "first_name": "Len", "last_name": "Legacy",
     "display_name": None, "role": "admin", "school_id": SCHOOL, "deleted_at": None},
    {"id": AMY, "first_name": "Amy", "last_name": "Barlow",
     "display_name": "Ms Barlow", "role": "teacher", "school_id": SCHOOL, "deleted_at": None},
    {"id": BEN, "first_name": "Ben", "last_name": "Hough",
     "display_name": None, "role": "teacher", "school_id": SCHOOL, "deleted_at": None},
    {"id": RICH, "first_name": "Rich", "last_name": "Spedding",
     "display_name": "Mr Spedding", "role": "teacher", "school_id": SCHOOL, "deleted_at": None},
    {"id": OLIVE, "first_name": "Olive", "last_name": "Drury",
     "display_name": None, "role": "teacher", "school_id": SCHOOL, "deleted_at": None},
    {"id": NIA, "first_name": "Nia", "last_name": "Fresh",
     "display_name": None, "role": "teacher", "school_id": SCHOOL, "deleted_at": None},
]

SCOPES = [
    {"profile_id": ADMIN, "scope": "school_admin", "department": None,
     "started_at": PAST, "ended_at": None, "deleted_at": None, "school_id": SCHOOL},
    {"profile_id": SLT, "scope": "slt", "department": None,
     "started_at": PAST, "ended_at": None, "deleted_at": None, "school_id": SCHOOL},
    {"profile_id": RICH, "scope": "hod", "department": "Science",
     "started_at": PAST, "ended_at": None, "deleted_at": None, "school_id": SCHOOL},
    # EXPIRED — Olive must show NO access label. An expired grant that still
    # printed "Head of Science" would be the page telling an admin something
    # the database disagrees with.
    {"profile_id": OLIVE, "scope": "hod", "department": "Science",
     "started_at": PAST, "ended_at": EXPIRED, "deleted_at": None, "school_id": SCHOOL},
]

# ⚠️ THE CLAIMED ROW IS THE POINT. Ben's invitation has been claimed, so it
# must become an annotation on Ben's LIVE row and must not render a second
# "Ben Hough". Nothing in either database exercises this today.
PENDING = [
    {"id": "aa000000-0000-0000-0000-000000000001", "school_id": SCHOOL,
     "first_name": "Priya", "last_name": "Adeyemi", "email": "p.adeyemi@example.invalid",
     "profile_role": "teacher", "claimed_at": None, "claimed_profile_id": None,
     "deleted_at": None},
    {"id": "aa000000-0000-0000-0000-000000000002", "school_id": SCHOOL,
     "first_name": "Tom", "last_name": "Ferris", "email": "t.ferris@example.invalid",
     "profile_role": "teacher", "claimed_at": None, "claimed_profile_id": None,
     "deleted_at": None},
    {"id": "aa000000-0000-0000-0000-000000000003", "school_id": SCHOOL,
     "first_name": "Ben", "last_name": "Hough", "email": "b.hough@example.invalid",
     "profile_role": "teacher", "claimed_at": "2026-08-14T09:00:00+00:00",
     "claimed_profile_id": BEN, "deleted_at": None},
]

TABLES = {
    "schools": [{"id": SCHOOL, "name": "Rainford High School"}],
    "academic_years": [
        {"id": YEAR, "name": "2026-27", "start_date": "2026-09-01",
         "end_date": "2027-08-31", "school_id": SCHOOL, "deleted_at": None},
    ],
    "classes": CLASSES,
    "class_teachers": LINKS,
    "class_members": MEMBERS,
    "assignments": [],
    "assignment_submissions": [],
    "profiles": PROFILES,
    "staff_scopes": SCOPES,
    "pending_staff": PENDING,
}

# ── the stub ─────────────────────────────────────────────────────────────
#
# A PostgREST-shaped builder: every filter method records and returns itself,
# and the object is thenable so `await` runs it. It implements exactly the
# four operators the page and `teacher-data.js` use between them — eq, is,
# in, single — and nothing else, so an unimplemented call is a loud
# TypeError rather than a silently wrong answer.
STUB_JS = r"""
(function () {
  var S = window.__MRB_STUB__;
  function rows(t) { return (S.tables[t] || []).slice(); }
  function ok(row, f) {
    var v = row[f.col];
    if (f.op === 'eq') { return v === f.val; }
    if (f.op === 'is') { return f.val === null ? (v === null || v === undefined) : v === f.val; }
    if (f.op === 'in') { return f.val.indexOf(v) !== -1; }
    return true;
  }
  function Q(table) {
    var fs = [], one = false;
    var api = {
      select: function () { return api; },
      order:  function () { return api; },
      limit:  function () { return api; },
      eq: function (c, v) { fs.push({op:'eq', col:c, val:v}); return api; },
      is: function (c, v) { fs.push({op:'is', col:c, val:v}); return api; },
      in: function (c, v) { fs.push({op:'in', col:c, val:v}); return api; },
      single: function () { one = true; return api; },
      maybeSingle: function () { one = true; return api; },
      then: function (res, rej) {
        var out = rows(table).filter(function (r) {
          for (var i = 0; i < fs.length; i++) { if (!ok(r, fs[i])) { return false; } }
          return true;
        });
        var payload = one
          ? {data: out[0] || null, error: out.length ? null : {code: 'PGRST116'}}
          : {data: out, error: null};
        S.log.push(table);
        return Promise.resolve(payload).then(res, rej);
      }
    };
    return api;
  }
  var user = {id: S.uid, aud: 'authenticated', role: 'authenticated',
              email: 'stub@drive.invalid', app_metadata: {}, user_metadata: {}};
  var client = {
    from: Q,
    rpc: function () { return Promise.resolve({data: null, error: null}); },
    auth: {
      getUser: function () { return Promise.resolve({data: {user: user}, error: null}); },
      getSession: function () {
        return Promise.resolve({data: {session: {user: user, access_token: 'stub'}}, error: null});
      },
      signOut: function () { return Promise.resolve({error: null}); },
      onAuthStateChange: function () {
        return {data: {subscription: {unsubscribe: function () {}}}};
      }
    }
  };
  /* ⚠️ A GETTER, NOT AN ASSIGNMENT, AND THAT IS THE WHOLE TRICK.
     This script runs at document-start, but the page then loads the real
     supabase-js UMD bundle from the CDN, and that bundle's last act is to
     assign `window.supabase`. A plain assignment here is overwritten by it a
     few milliseconds later, the guard then builds a REAL client with no
     session, `getUser()` fails and the page bounces to auth.html — which
     presents as "the drive renders nothing" with a completely silent
     console. Swallowing the CDN's write keeps the stub in place. */
  var sdk = {createClient: function () { return client; }};
  Object.defineProperty(window, 'supabase', {
    configurable: true,
    get: function () { return sdk; },
    set: function () { /* the CDN bundle's own assignment, ignored */ }
  });
})();
"""


def anon_key():
    src = open("shared/config.js", encoding="utf-8").read()
    return re.search(r"'(eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+)'",
                     src[src.index("const TEST"):]).group(1)


def sign_in(email, key):
    req = urllib.request.Request(
        URL + "/auth/v1/token?grant_type=password",
        data=json.dumps({"email": email, "password": DRIVE_PW}).encode(),
        headers={"apikey": key, "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return json.loads(r.read().decode())


def stub_world(uid, tables=None, drop=()):
    """The injected pre-load script for one persona.

    `drop` names tables the database would refuse this viewer — that is how
    the slt case is driven: `pending_staff` RLS is `school_admin` only, so an
    slt viewer is handed an EMPTY LIST, and the page must degrade to silence
    rather than to an error.
    """
    t = dict(tables or TABLES)
    for name in drop:
        t[name] = []
    payload = {"uid": uid, "tables": t, "log": []}
    return ("window.__MRB_STUB__=%s;\n" % json.dumps(payload)) + STUB_JS


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", default="/tmp/mrb303-admin")
    args = ap.parse_args()
    os.makedirs(args.shots, exist_ok=True)

    key = anon_key()
    fails = []

    def check(ok_, what, detail=""):
        print("     %s %s%s" % ("✅" if ok_ else "❌", what,
                                ("  — " + detail) if detail else ""))
        if not ok_:
            fails.append(what)

    print("\n🔐  MRB-303 J2 — the admin school view, driven\n")
    server, port = cdp.serve("mrbadmus_site", port=PORT)
    base = "http://localhost:%d" % port

    try:
        with cdp.Browser() as b:

            # ── 1. the positive cases, on a stubbed client ────────────────
            for label, uid, drop, shot in [
                ("Ada Nwosu — school_admin", ADMIN, (), "admin-school-view.png"),
                ("Sam Vine — slt (pending_staff refused by RLS)", SLT,
                 ("pending_staff",), "slt-school-view.png"),
                ("Len Legacy — legacy profiles.role='admin', no scope row",
                 LEGACY, (), "legacy-admin-school-view.png"),
            ]:
                print("\n  ── %s ──────────────────────" % label)
                p = b.page("about:blank", settle=0.2)
                # ⚠️ THE IDENTIFIER IS KEPT SO THE STUB CAN BE TAKEN OUT
                # AGAIN. `addScriptToEvaluateOnNewDocument` is per-TARGET and
                # this drive reuses one target, so a stub left armed follows
                # the browser into the real-sign-in section below — where it
                # replaces the genuine SDK and `auth.setSession` simply is not
                # a function. Removed the moment the persona is done.
                added = p.send("Page.addScriptToEvaluateOnNewDocument",
                               {"source": stub_world(uid, drop=drop)})
                armed = added.get("identifier")
                p.set_viewport(1280, 1400)
                p.goto(base + "/teacher/admin.html", settle=3.0)

                # ⚠️ READ AS FIELDS, NOT AS CONCATENATED TEXT. `textContent`
                # over a row glues "School admin" to "1" and produces
                # "School admin1 class", so a substring matcher looking for
                # " 1 class" reports a perfectly correct page as broken —
                # which is exactly what the first run of this drive did, four
                # times. Each row is read through the elements that carry the
                # values instead.
                got = p.eval("""(function(){
                  function t(el){ return el ? el.textContent.trim() : ''; }
                  var main = document.getElementById('main');
                  var vis = main && main.style.display !== 'none';
                  // ⊕ Mide's UI change (30 Aug 2026): a teacher row no
                  // longer carries a .classlist span (the inline class-name
                  // list was dropped) — nothing here reads a "classes" field
                  // off it any more, only .count.
                  var rows = [].slice.call(document.querySelectorAll('#teachers .row'))
                    .map(function(r){
                      return {name: t(r.querySelector('.name')),
                              count: t(r.querySelector('.count')),
                              tags: [].slice.call(r.querySelectorAll('.tag')).map(t),
                              metas: [].slice.call(r.querySelectorAll('.meta')).map(t)};
                    });
                  var cls = [].slice.call(document.querySelectorAll('#classes .row'))
                    .map(function(r){
                      return {code: t(r.querySelector('a.classlink')),
                              href: (r.querySelector('a.classlink')||{}).getAttribute
                                    ? r.querySelector('a.classlink').getAttribute('href') : '',
                              count: t(r.querySelector('.count')),
                              tags: [].slice.call(r.querySelectorAll('.tag')).map(t),
                              who: t(r.querySelector('.classlist'))};
                    });
                  // ⊕ Mide's UI change (30 Aug 2026): classes are now
                  // grouped under a "Year N" heading per .year-group. Read
                  // the headings in DOM order, each with the class names
                  // nested under it, so ordering AND bucketing can both be
                  // asserted.
                  var yearGroups = [].slice.call(document.querySelectorAll('#classes .year-group'))
                    .map(function(g){
                      return {heading: t(g.querySelector('.year-heading')),
                              codes: [].slice.call(g.querySelectorAll('a.classlink')).map(t)};
                    });
                  return {vis: !!vis,
                          body: document.body.style.display,
                          sub: t(document.getElementById('school-line')),
                          stats: t(document.getElementById('stats')),
                          teachers: rows, classes: cls, yearGroups: yearGroups,
                          notice: (document.getElementById('notice')||{style:{}}).style.display,
                          at: location.pathname,
                          title: t(document.getElementById('notice-title'))};
                })()""")

                check(got["vis"], "the school view rendered",
                      "at %s, body=%s, notice=%r" % (got["at"], got["body"], got["title"]))
                check("2026-27" in got["sub"] and "Rainford" in got["sub"],
                      "school and WORKING year in the header", got["sub"])

                T = {r["name"]: r for r in got["teachers"]}
                C = {r["code"]: r for r in got["classes"]}
                names = [r["name"] for r in got["teachers"]]

                # Every teacher appears exactly once — a claimed invitation
                # must not have produced a second Ben.
                check(names.count("Ben Hough") == 1,
                      "a CLAIMED invitation annotates the live row, no duplicate",
                      "Ben Hough x%d" % names.count("Ben Hough"))

                # Co-teaching: one class, its "who" line naming both teachers.
                # ⊕ Mide's UI change (30 Aug 2026) dropped the per-teacher
                # classlist span, so this used to read from
                # T[name]["classes"]. The count-per-teacher check right below
                # already proves each teacher's OWN tally is right; this one
                # is only about the class row's "who teaches this" line, so
                # it now reads that instead — same property, surviving
                # element.
                who = C.get("10h/Sc1", {}).get("who", "")
                check("Amy Barlow" in who and "Ben Hough" in who,
                      "a co-taught class's row names BOTH teachers", who)

                # The de-dup: Ada holds TWO subject links to 8r/Sc1.
                check(T.get("Ada Nwosu", {}).get("count") == "1",
                      "two subject links to one class count as ONE class",
                      repr(T.get("Ada Nwosu")))

                # An expired grant is not access.
                check("Head of Science" not in T.get("Olive Drury", {}).get("tags", []),
                      "an EXPIRED hod grant shows no access label",
                      repr(T.get("Olive Drury", {}).get("tags")))
                check("Head of Science" in T.get("Rich Spedding", {}).get("tags", []),
                      "a LIVE hod grant does show",
                      repr(T.get("Rich Spedding", {}).get("tags")))

                # The legacy dual-read path is real access and is labelled.
                check("School admin" in T.get("Len Legacy", {}).get("tags", []),
                      "legacy profiles.role='admin' is labelled School admin",
                      repr(T.get("Len Legacy", {}).get("tags")))

                # An honest zero, never a blank.
                check(T.get("Nia Fresh", {}).get("count") == "0",
                      "a teacher with no classes shows an honest 0",
                      repr(T.get("Nia Fresh")))

                # The split: the class nobody teaches still gets a real count
                # from the fallback, because loadClassMatrices refuses it.
                check(C.get("9r/Sc4", {}).get("count") == "2"
                      and C.get("9r/Sc4", {}).get("who") == "No teacher assigned",
                      "a teacher-less class counts its roster and says so",
                      repr(C.get("9r/Sc4")))

                # A departed student is not on the roster.
                check(C.get("10h/Ph1", {}).get("count") == "1",
                      "a departed student is not counted", repr(C.get("10h/Ph1")))

                # Every class link points at the detail page this run does not
                # modify, with the id it reads.
                bad_href = [c for c in got["classes"]
                            if not c["href"].startswith("/teacher/class-detail.html?class=")]
                check(not bad_href, "every class links to class-detail.html?class=<id>",
                      repr(bad_href[:1]))

                check(len(got["classes"]) == 4,
                      "every class in the school-year is listed",
                      "%d row(s)" % len(got["classes"]))

                # Year grouping: 8r/Sc1=8, 9r/Sc4=9, 10h/Ph1 & 10h/Sc1=10 —
                # three headings, ascending, each bucket right, and 10h/Ph1
                # before 10h/Sc1 within the tied year (name sort survives
                # the regrouping).
                yg = got["yearGroups"]
                check([g["heading"] for g in yg] == ["Year 8", "Year 9", "Year 10"],
                      "year headings appear once each, ascending",
                      repr([g["heading"] for g in yg]))
                by_heading = {g["heading"]: g["codes"] for g in yg}
                check(by_heading.get("Year 8") == ["8r/Sc1"],
                      "Year 8 bucket holds exactly its class", repr(by_heading.get("Year 8")))
                check(by_heading.get("Year 9") == ["9r/Sc4"],
                      "Year 9 bucket holds exactly its class", repr(by_heading.get("Year 9")))
                check(by_heading.get("Year 10") == ["10h/Ph1", "10h/Sc1"],
                      "Year 10 bucket holds both classes, name-sorted",
                      repr(by_heading.get("Year 10")))

                # The pending half, and the slt degradation.
                invited = [r for r in got["teachers"] if "Invited" in r["tags"]]
                if "pending_staff" in drop:
                    check(not invited,
                          "slt is handed no invitations and the page stays quiet",
                          "%d" % len(invited))
                    check(len(got["teachers"]) == 8,
                          "…and still renders every live teacher",
                          "%d row(s)" % len(got["teachers"]))
                else:
                    check(len(invited) == 2,
                          "both UNCLAIMED invitations show as invited",
                          "%d" % len(invited))
                    check(any("Priya Adeyemi" == r["name"] for r in invited),
                          "an invited teacher shows the seeded name")
                    check(any("Joined 14 Aug 2026" in m
                              for m in T.get("Ben Hough", {}).get("metas", [])),
                          "the claim date shows on that teacher's row",
                          repr(T.get("Ben Hough", {}).get("metas")))

                errs = [e for e in p.console_errors() if "favicon" not in e]
                check(not errs, "console stayed quiet", "; ".join(errs[:2]))
                p.screenshot(os.path.join(args.shots, shot), width=1280)
                if armed:
                    p.send("Page.removeScriptToEvaluateOnNewDocument",
                           {"identifier": armed})

            # ── 1b. the link must APPEAR, and SURVIVE A REDRAW ──────────
            #
            # The negatives below prove the link is absent for a hod and for a
            # plain teacher. This proves the other half — that it is there for
            # an admin — on BOTH nav families, and that the ported dashboard's
            # copy outlives a redraw. The runtime's `draw()` does
            # `host.textContent = ""` and rebuilds the entire tree on every
            # state change, so a one-shot append is destroyed by the teacher's
            # first click. Opening the search sheet forces exactly that redraw.
            print("\n  ── the Admin entry APPEARS for an admin ───────")
            p = b.page("about:blank", settle=0.2)
            armed = p.send("Page.addScriptToEvaluateOnNewDocument",
                           {"source": stub_world(ADMIN)}).get("identifier")
            p.set_viewport(1280, 1200)

            # (a) a hand-written staff page — static nav, no runtime
            p.goto(base + "/teacher-profile.html", settle=3.0)
            prof = p.eval("""(function(){
              var a = document.querySelector('nav.top-nav [data-mrb-admin-nav]');
              var out = document.querySelector('nav.top-nav .signout-btn');
              return {found: !!a, text: a ? a.textContent : '',
                      href: a ? a.getAttribute('href') : '',
                      beforeSignOut: !!(a && out &&
                        (a.compareDocumentPosition(out) & Node.DOCUMENT_POSITION_FOLLOWING)),
                      dupes: document.querySelectorAll('nav.top-nav [data-mrb-admin-nav]').length,
                      myClasses: document.querySelectorAll(
                        'nav.top-nav a[href="/teacher/classes.html"]').length};
            })()""")
            check(prof["found"] and prof["text"] == "Admin",
                  "teacher-profile.html: the Admin entry is there", repr(prof))
            check(prof["beforeSignOut"], "…and sits before Sign out")
            check(prof["dupes"] == 1, "…exactly once", "%s" % prof["dupes"])
            # ⚠️ A WEAK CHECK, AND LABELLED AS ONE. Job 1's de-dup lives in
            # `class-entry.js`, which renders its "My classes" entry only for
            # a real stored session — and this persona is a stub, so the
            # module no-ops and the honest expected answer here is ZERO. This
            # asserts only that nothing on THIS page doubles the entry; it is
            # NOT a re-verification of Job 1, which needs a real session.
            check(prof["myClasses"] <= 1,
                  "nothing doubles a \"My classes\" entry on this page "
                  "(NOT a Job 1 re-check — stubbed session)",
                  "%s" % prof["myClasses"])
            p.screenshot(os.path.join(args.shots, "admin-nav-profile.png"), width=1280)

            # (b) a ported page — runtime-drawn topbar, then a forced redraw
            p.goto(base + "/teacher/classes.html", settle=6.0)
            before = p.eval("document.querySelectorAll("
                            "'[data-port-region=\"topbar\"] [data-mrb-admin-nav]').length")
            check(before == 1, "classes.html: the Admin entry is in the topbar",
                  "%s" % before)

            renders0 = p.eval("document.getElementById('mrb-teacher')"
                              ".getAttribute('data-mrb-renders')")
            p.eval("""(function(){
              var b = [].slice.call(document.querySelectorAll(
                '[data-port-region=\"topbar\"] button'));
              for (var i=0;i<b.length;i++){
                if (/find a student/i.test(b[i].textContent)) { b[i].click(); return 1; }
              }
              return 0;
            })()""")
            import time as _t; _t.sleep(1.2)
            renders1 = p.eval("document.getElementById('mrb-teacher')"
                              ".getAttribute('data-mrb-renders')")
            after = p.eval("document.querySelectorAll("
                           "'[data-port-region=\"topbar\"] [data-mrb-admin-nav]').length")
            check(renders1 != renders0, "a redraw really happened",
                  "%s -> %s" % (renders0, renders1))
            check(after == 1, "…and the Admin entry survived it, exactly once",
                  "%s" % after)
            p.screenshot(os.path.join(args.shots, "admin-nav-classes.png"), width=1280)
            if armed:
                p.send("Page.removeScriptToEvaluateOnNewDocument",
                       {"identifier": armed})

            # ── 2. 390px ────────────────────────────────────────────────
            print("\n  ── 390px, the admin view ──────────────────────")
            p = b.page("about:blank", settle=0.2)
            armed = p.send("Page.addScriptToEvaluateOnNewDocument",
                           {"source": stub_world(ADMIN)}).get("identifier")
            p.set_viewport(390, 900)
            p.goto(base + "/teacher/admin.html", settle=3.0)
            over = p.eval("Math.max(0, document.documentElement.scrollWidth - "
                          "document.documentElement.clientWidth)")
            check(over == 0, "no sideways scroll at 390px", "overflow %spx" % over)
            p.screenshot(os.path.join(args.shots, "admin-390.png"), width=390)
            if armed:
                p.send("Page.removeScriptToEvaluateOnNewDocument",
                       {"identifier": armed})

            # ── 3. the negatives, SIGNED IN FOR REAL ────────────────────
            for label, email, uid in [
                ("Rich — hod scope, which is NOT admin", "hz_rich@test.mrbadmus", RICH),
                ("Amy — a plain teacher", "hz_amy@test.mrbadmus", AMY),
            ]:
                print("\n  ── %s (real session, real RLS) ───────" % label)
                sess = sign_in(email, key)

                p = b.page(base + "/leaderboard.html?env=test", settle=2.0)
                signed = p.eval("""
                  (async function () {
                    var c = window.supabase.createClient(%s, %s);
                    var r = await c.auth.setSession({access_token: %s, refresh_token: %s});
                    return r.error ? 'error: ' + r.error.message : 'ok';
                  })()
                """ % (json.dumps(URL), json.dumps(key),
                       json.dumps(sess["access_token"]),
                       json.dumps(sess["refresh_token"])))
                check(signed == "ok", "signed in for real", str(signed))

                # 3a. the dashboard must carry NO Admin entry
                p.set_viewport(1280, 1200)
                p.goto(base + "/teacher/classes.html?env=test", settle=6.0)
                seen = p.eval("!!document.querySelector('[data-mrb-admin-nav]')")
                check(not seen, "no Admin entry in the topbar",
                      "querySelector -> %r" % (seen,))
                p.screenshot(os.path.join(
                    args.shots, "no-admin-nav-%s.png" % uid[-4:]), width=1280)

                # 3b. …and the page itself refuses, in plain words
                p.goto(base + "/teacher/admin.html?env=test", settle=5.0)
                ref = p.eval("""(function(){
                  var n = document.getElementById('notice');
                  return {shown: n && n.style.display === 'block',
                          body: document.body.style.display,
                          title: (document.getElementById('notice-title')||{}).textContent||'',
                          text: (document.getElementById('notice-body')||{}).textContent||'',
                          main: (document.getElementById('main')||{style:{}}).style.display,
                          leaked: (document.getElementById('teachers')||{}).innerHTML||''};
                })()""")
                check(ref["shown"] and ref["body"] == "block",
                      "the refusal is VISIBLE — never a blank page", str(ref["body"]))
                check("school admins" in ref["title"],
                      "…and says so in plain words", ref["title"])
                blob = (ref["title"] + " " + ref["text"]).lower()
                check(not any(w in blob for w in ("403", "rls", "policy", "scope",
                                                 "unauthor", "forbidden")),
                      "no jargon, no status code, no leaked mechanism")
                check(ref["main"] == "none" and not ref["leaked"],
                      "no school data rendered behind the refusal")
                p.screenshot(os.path.join(
                    args.shots, "refusal-%s.png" % uid[-4:]), width=1280)

    finally:
        server.shutdown()

    print("\n" + "─" * 68)
    if fails:
        print("❌ admin_view_drive: %d check(s) failed" % len(fails))
        for f in fails:
            print("   · " + f)
        return 1
    print("✅ admin_view_drive: every check passed. Screenshots in %s" % args.shots)
    return 0


if __name__ == "__main__":
    sys.exit(main())
