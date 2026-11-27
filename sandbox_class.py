#!/usr/bin/env python3
"""sandbox_class.py — the ONE place that names the production sandbox class,
and the guard every live drive runs before it writes to a class.

⊕ 27 Nov 2026 (sandbox move). 8r/Sc1 (d9740ab8-…) WAS the production sandbox.
On 16 Nov 2026 it became Mide's real Year 8 class; its real pupils are being
uploaded. The supervising chat moved the two test pupils, and all of their
history, into a new class built for the job:

    "Test class (Mr Badmus)"  e8eb5833-fa52-4d01-9ff6-678145ee48c7
    Rainford, Year 8, KS3, production (PROD_REF in shared/config.js)
    teacher: Mr Badmus only        pupils: the two test accounts only

A drive that sets work, submits answers or makes flashcards in a real class
puts test homework in front of real children. So this is not a convention, it
is a refusal:

    import sandbox_class
    sandbox_class.assert_writable(class_id, supabase_url, service_key)

* A RETIRED sandbox id (8r/Sc1) is refused ALWAYS, on any project, with or
  without a key — there is no world in which a script should write to it.
* On PRODUCTION the class must prove it is a sandbox, every time, from the
  database, not from a label: it must exist and not be deleted, have at least
  one active pupil, every active pupil must be one of TEST_PUPILS, and every
  active teacher must be one of SANDBOX_TEACHERS. An empty class is REFUSED —
  that is 8r/Sc1's exact shape today (no pupils yet, two real teachers), and a
  pupil-only check would have let it through.
* Every failure to find out is a refusal: no service key, a network error, an
  unreadable row. "Could not check" never means "go ahead".
* On TEST the check is off by default (TEST is the sandbox project; its drives
  mint throwaway pupils). `enforce=True`, or MRB_SANDBOX_ENFORCE=1, turns it on
  for any project — that is how the guard is proven on TEST without touching
  production.

The decision itself is `decide()`, a pure function. `membership_sql()` is the
same read as `fetch_membership()` written as SQL, for running through a
per-call-scoped connector; the `sandbox_class` fast gate proves the two agree
on the filters they apply.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config_env  # noqa: E402

SANDBOX_CLASS_ID = "e8eb5833-fa52-4d01-9ff6-678145ee48c7"
SANDBOX_CLASS_NAME = "Test class (Mr Badmus)"

TEST_PUPILS = frozenset({"midebolabadmus@gmail.com", "anifabalo@gmail.com"})
SANDBOX_TEACHERS = frozenset({"a.badmus@rainford.org.uk"})

# Classes that were once a sandbox and are now REAL. Refused on every project.
RETIRED = {
    "d9740ab8-c4e3-4c22-bce9-629b650782c5":
        "8r/Sc1 — Mide's real Year 8 class since 16 Nov 2026",
}

_UUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")


class SandboxRefused(SystemExit):
    """Raised (and exits non-zero if uncaught) when a write target is not a sandbox."""


def _refuse(class_id, name, why):
    label = "%s (%s)" % (name, class_id) if name else class_id
    raise SandboxRefused(
        "\n!!!! SANDBOX GUARD: refusing to write to class %s\n!!!! %s\n"
        "!!!! Live drives write only to %r (%s).\n"
        % (label, why, SANDBOX_CLASS_NAME, SANDBOX_CLASS_ID))


def project_ref(supabase_url):
    m = re.match(r"https://([a-z0-9]+)\.supabase\.co", (supabase_url or "").strip())
    return m.group(1) if m else ""


def enforced(supabase_url, enforce=None):
    """Whether membership must be proven for writes against this project."""
    if enforce is not None:
        return bool(enforce)
    if os.environ.get("MRB_SANDBOX_ENFORCE") == "1":
        return True
    # Anything that is not positively TEST is treated as production.
    return project_ref(supabase_url) != config_env.TEST_REF


def decide(class_id, found):
    """Pure decision. `found` is None (no such class) or a dict with
    name, deleted (bool), pupils [emails], teachers [emails]. Returns None
    when the write is allowed; raises SandboxRefused otherwise."""
    if class_id in RETIRED:
        _refuse(class_id, None, "it is a RETIRED sandbox: " + RETIRED[class_id])
    if not found:
        _refuse(class_id, None, "no such class could be read.")
    name = found.get("name")
    if found.get("deleted"):
        _refuse(class_id, name, "the class is deleted.")
    pupils = [(e or "").strip().lower() for e in found.get("pupils") or []]
    teachers = [(e or "").strip().lower() for e in found.get("teachers") or []]
    if not pupils:
        _refuse(class_id, name, "it has no pupils, so it cannot prove it is a "
                "sandbox (a real class waiting for its pupils looks like this).")
    strangers = sorted(p for p in pupils if p not in TEST_PUPILS)
    if strangers:
        _refuse(class_id, name, "it has %d pupil(s) who are not test accounts."
                % len(strangers))
    staff = sorted(t for t in teachers if t not in SANDBOX_TEACHERS)
    if staff:
        _refuse(class_id, name, "it has %d teacher(s) other than the sandbox "
                "teacher." % len(staff))
    return None


def membership_sql(class_id):
    """The membership read as one SQL statement (for a per-call connector)."""
    if not _UUID.match(class_id or ""):
        raise ValueError("not a class id: %r" % class_id)
    return (
        "select c.name, c.deleted_at is not null as deleted,"
        " coalesce((select json_agg(lower(u.email)) from class_members m"
        " join auth.users u on u.id = m.student_id"
        " where m.class_id = c.id and m.left_at is null and m.deleted_at is null),"
        " '[]') as pupils,"
        " coalesce((select json_agg(lower(u.email)) from class_teachers t"
        " join auth.users u on u.id = t.teacher_id"
        " where t.class_id = c.id and (t.ended_at is null or t.ended_at > now())"
        " and t.deleted_at is null), '[]') as teachers"
        " from classes c where c.id = '%s';" % class_id)


def _get(url, key):
    req = urllib.request.Request(url, headers={"apikey": key,
                                               "Authorization": "Bearer " + key})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_membership(class_id, supabase_url, service_key):
    """The same read as membership_sql(), over PostgREST + the auth admin API."""
    base = supabase_url.rstrip("/")
    q = urllib.parse.quote
    rows = _get(base + "/rest/v1/classes?select=name,deleted_at&id=eq." + q(class_id),
                service_key)
    if not rows:
        return None
    pupil_ids = [r["student_id"] for r in _get(
        base + "/rest/v1/class_members?select=student_id&left_at=is.null"
        "&deleted_at=is.null&class_id=eq." + q(class_id), service_key)]
    teacher_ids = [r["teacher_id"] for r in _get(
        base + "/rest/v1/class_teachers?select=teacher_id&deleted_at=is.null"
        "&or=(ended_at.is.null,ended_at.gt.now())&class_id=eq." + q(class_id),
        service_key)]

    def email(uid):
        return (_get(base + "/auth/v1/admin/users/" + q(uid), service_key)
                .get("email") or "")
    return {"name": rows[0].get("name"),
            "deleted": rows[0].get("deleted_at") is not None,
            "pupils": [email(u) for u in pupil_ids],
            "teachers": [email(u) for u in teacher_ids]}


def assert_writable(class_id, supabase_url, service_key=None, enforce=None):
    """Call before ANY write that names a class. Returns class_id, or raises."""
    if class_id in RETIRED:
        decide(class_id, None)
    if not enforced(supabase_url, enforce):
        return class_id
    if not service_key:
        _refuse(class_id, None, "no service key to prove its membership with, "
                "and an unproven class is refused.")
    try:
        found = fetch_membership(class_id, supabase_url, service_key)
    except (urllib.error.URLError, ValueError, KeyError) as e:
        _refuse(class_id, None, "its membership could not be read (%s)."
                % type(e).__name__)
    decide(class_id, found)
    return class_id


_CLASS_KEYS = ("class_id", "p_class_id", "class_ids", "p_class_ids")
_ANY_UUID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")


def class_ids_in(body=None, url=""):
    """Every class id a request names: body keys class_id / p_class_id /
    class_ids / p_class_ids (at any depth, in lists of rows too), and any
    `class_id=` or `id=` filter on /rest/v1/classes in the URL's query."""
    out = []

    def walk(v):
        if isinstance(v, dict):
            for k, x in v.items():
                if k in _CLASS_KEYS:
                    out.extend(x if isinstance(x, list) else [x])
                else:
                    walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)
    walk(body)
    parsed = urllib.parse.urlparse(url or "")
    for k, vals in urllib.parse.parse_qs(parsed.query).items():
        if k in _CLASS_KEYS or (k == "id" and parsed.path.endswith("/classes")):
            for v in vals:
                out.extend(_ANY_UUID.findall(v))
    seen, ids = set(), []
    for c in out:
        if isinstance(c, str) and c not in seen:
            seen.add(c)
            ids.append(c)
    return ids


def guard_request(method, url, body, supabase_url, service_key=None, enforce=None):
    """For a shared client: run assert_writable on every class a WRITE names.
    Reads (GET/HEAD) pass untouched. On TEST this costs nothing unless a
    retired id is named."""
    if (method or "GET").upper() in ("GET", "HEAD"):
        return
    for cid in class_ids_in(body, url):
        assert_writable(cid, supabase_url, service_key, enforce)


if __name__ == "__main__":
    # `python3 sandbox_class.py --decide <class_id> <json>` — run decide() on
    # a membership row read elsewhere (membership_sql through a connector).
    # `python3 sandbox_class.py --sql <class_id>` prints that read.
    if len(sys.argv) >= 3 and sys.argv[1] == "--sql":
        print(membership_sql(sys.argv[2]))
    elif len(sys.argv) >= 4 and sys.argv[1] == "--decide":
        rows = json.loads(sys.argv[3])
        row = rows[0] if isinstance(rows, list) and rows else (rows or None)
        try:
            decide(sys.argv[2], row)
        except SandboxRefused as e:
            print("REFUSED" + str(e))
            sys.exit(3)
        print("ALLOWED  %s (%s)" % (row.get("name"), sys.argv[2]))
    else:
        print(__doc__)
