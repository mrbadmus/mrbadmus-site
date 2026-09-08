"""tools/ks3_bank_load.py — service-role mirror of the KS3 assignment bank.

⊕ MRB-335 (8 Sep 2026). `ks3_pools_ingest` is SECURITY DEFINER and guarded on
Mide's own email, so a session that is not his cannot load the KS3 bank
through it. This is the same upsert the RPC performs, done as service role —
which is exactly how `export_ks4_questions.py --load` already mirrors the KS4
bank. Same three guards on production (typed token, ~/.mrbadmus/prod.env only,
URL ref check); same chunk size; and the checksum it prints is the one
`export_ks3_questions.py --check` prints, so the two can be held together.

    python3 export_ks3_questions.py --check     # refuses an invalid bank; prints sha256
    python3 export_ks3_questions.py --json      # build/ks3-questions/bank.json
    python3 tools/ks3_bank_load.py --project test          # upsert, then verify
    python3 tools/ks3_bank_load.py --project test --verify # read-only checksum compare
    python3 tools/ks3_bank_load.py --project prod          # production: the literal token

It never deletes. A withdrawn id stays until someone removes it by hand.
"""
import json
import os
import ssl
import sys
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
os.chdir(REPO)

CHUNK = 250
TABLE = "ks3_assignment_bank"
CTX = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
PROJECTS = {
    "test": ("/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env", "qeppkiswvclkkwbxmlok"),
    "prod": (os.path.expanduser("~/.mrbadmus/prod.env"), "urklkrwevjtlfbwnipjn"),
}


def conf_for(project):
    env, ref = PROJECTS[project]
    if project == "prod" and "prod" not in sys.argv:
        sys.exit("⛔ production needs the literal token `prod` on the command line")
    conf = {}
    try:
        with open(env, encoding="utf-8") as fh:
            for line in fh:
                if "=" in line and not line.lstrip().startswith("#"):
                    k, v = line.split("=", 1)
                    conf[k.strip()] = v.strip()
    except OSError as exc:
        sys.exit("⛔ cannot read %s (%s)" % (env, exc))
    url = conf.get("SUPABASE_URL", "")
    key = conf.get("SUPABASE_SERVICE_ROLE_KEY", "")
    if ref not in url:
        sys.exit("⛔ %s: SUPABASE_URL is not the %s project" % (env, project))
    if not key:
        sys.exit("⛔ %s has no SUPABASE_SERVICE_ROLE_KEY" % env)
    return url.rstrip("/"), key


def call(url, key, method, path, body=None, headers=None):
    req = urllib.request.Request(url + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None)
    req.add_header("apikey", key)
    req.add_header("Authorization", "Bearer " + key)
    req.add_header("Content-Type", "application/json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=120) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw else None), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:400], {}


def count(url, key):
    st, _body, hdr = call(url, key, "GET", "/rest/v1/%s?select=id&limit=1" % TABLE,
                          headers={"Prefer": "count=exact"})
    if st not in (200, 206):
        sys.exit("⛔ count read failed: %s %s" % (st, _body))
    return int(hdr.get("Content-Range", "0/0").split("/")[-1])


def read_all(url, key, columns):
    rows, off = [], 0
    while True:
        st, body, _ = call(url, key, "GET", "/rest/v1/%s?select=%s&order=id&offset=%d&limit=1000"
                           % (TABLE, ",".join(columns), off))
        if st not in (200, 206):
            sys.exit("⛔ read failed: %s %s" % (st, body))
        rows.extend(body)
        if len(body) < 1000:
            return rows
        off += 1000


def main():
    import export_ks3_questions as ex
    project = "prod" if "--project" in sys.argv and sys.argv[sys.argv.index("--project") + 1] == "prod" else "test"
    verify_only = "--verify" in sys.argv
    url, key = conf_for(project)
    cols = ex.BANK_COLUMNS
    rows = ex.bank_rows()
    py_sum = ex.checksum(rows, cols)
    print("python: %d rows, sha256 %s" % (len(rows), py_sum))
    before = count(url, key)
    print("%s before: %d rows" % (project.upper(), before))
    if not verify_only:
        for i in range(0, len(rows), CHUNK):
            chunk = [{c: r.get(c) for c in cols} for r in rows[i:i + CHUNK]]
            st, body, _ = call(url, key, "POST", "/rest/v1/%s?on_conflict=id" % TABLE, chunk,
                               headers={"Prefer": "resolution=merge-duplicates,return=minimal"})
            if st not in (200, 201, 204):
                sys.exit("⛔ upsert failed on rows %d-%d: %s %s" % (i, i + len(chunk), st, body))
        print("upserted %d rows in %d chunks" % (len(rows), (len(rows) + CHUNK - 1) // CHUNK))
    after = count(url, key)
    db = read_all(url, key, cols)
    db_sum = ex.checksum(db, cols)
    print("%s after: %d rows, sha256 %s" % (project.upper(), after, db_sum))
    if db_sum != py_sum or after != len(rows):
        py_ids = {r["id"] for r in rows}; db_ids = {r["id"] for r in db}
        print("  only in python: %s" % sorted(py_ids - db_ids)[:10])
        print("  only in db:     %s" % sorted(db_ids - py_ids)[:10])
        sys.exit("⛔ MIRROR DRIFT")
    print("✅ mirror matches python exactly")


if __name__ == "__main__":
    main()
