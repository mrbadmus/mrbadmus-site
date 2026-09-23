#!/usr/bin/env python3
"""frozen_window_guard.py — MRB-352. Every frozen row is untouched, except

the 28 the ruling named.

    python3 frozen_window_guard.py                       # ⭐ THE GATE: read
                                                          #   PRODUCTION, read-only
    python3 frozen_window_guard.py --baseline <file>     # write <file> if it
                                                          #   does not exist yet,
                                                          #   else compare against it
                                                          #   instead of the network

── WHY THIS EXISTS ───────────────────────────────────────────────────────

MRB-335 froze `bank_position` 0–11 of every bank leaf (a KS3 lesson, a KS4
subtopic): those rows, and only those rows, are what the AUTOMATIC weekly
producer reads, forever (`bankFor()` in the Node backend, `compose_assignment`
/ `auto_pool()` in `ks3_data/question_bank.py`). `ks4_pool_check.py` check 4a
proves that window still holds four of each band — a SHAPE property. Nothing
in the estate proves the window's own CONTENT hasn't moved. A rewording, a
swapped option, a re-keyed `correct_index` inside that window would pass
`ks4_pool_check`, `answer_positions`, `answer_lengths` and every other
question-bank gate, and reach the classes that window has been serving since
MRB-335, silently.

Mide ruled a narrow, named exception on 23 Sep 2026 (see
`frozen_window_allowlist.py`): 28 ids, inside the frozen window, whose stems
DESCRIBE a picture in words instead of showing one — those 28, and only
those, may be edited in place, and only by attaching a `figure` and rewording
the stem/options to match it. This gate is what makes that exception SAFE by
making it NARROW: it proves every OTHER frozen row — roughly 2,800 of them —
is byte-identical to what is actually being served, and that the 28
exceptions changed nothing but the fields the ruling permits.

── WHAT IT PROVES, THE FOUR PARTS ────────────────────────────────────────

  1. every frozen row NOT on the allowlist is byte-identical to the
     reference (production, or a `--baseline` snapshot), field by field;
  2. an allowlisted row may differ ONLY in `text`, `options` and (KS3 only)
     `figure` — its `id`, `band`, `tier`, `triple_only` and `bank_position`
     must be unchanged, and a violation names the field;
  3. the allowlist is exactly 28 ids and every one of them actually exists,
     inside the frozen window, in the authored corpus today;
  4. positions 0–11 hold the same SET OF IDS in the same ORDER per leaf as
     the reference — the composition-stability property that actually
     matters, and strictly stronger than a 4/4/4 count.

── WHY IT REUSES THE EXPORTERS' `checksum()` RATHER THAN A THIRD HASH ─────

`export_ks3_questions.py` and `export_ks4_questions.py` each already define a
`checksum()` that is canonical about content — list fields walked in order
and never sorted, `None` and booleans coerced to one sentinel each, so the
same row hashes the same whether it came out of Python or out of PostgREST's
JSON. Writing a second implementation of that here would be exactly the "a
second thing to drift" MRB-335 already warned about for KS3 vs KS4's own two
checksums. So this imports both modules' real `checksum()` and uses it,
unmodified, as the equality oracle for a WHOLE row; when two rows disagree,
`_which_fields_differ()` below isolates the differing field(s) by asking the
SAME `checksum()` to hash the row with every other field held constant and
only one substituted — so the field-naming is still their normalisation,
never a second one.

── HOW IT READS PRODUCTION ───────────────────────────────────────────────

Production ref `urklkrwevjtlfbwnipjn`. READ-ONLY — every request below is an
HTTP GET against PostgREST; nothing here can write or DDL. The credential is
the service-role key from `~/.mrbadmus/prod.env` and nowhere else — the same
file `export_ks3_questions.py --load prod` and `export_ks4_questions.py
--load prod` read — and the target project is PROVED from the key's own
`ref` JWT claim via `_jwt_ref` (imported from `export_ks4_questions`, which
`export_ks3_questions` carries an identical copy of), never merely stated by
a URL sitting next to it.

If the key is not available — the file is missing, unreadable, carries no
service key, or that key belongs to a different project — this SKIPS LOUDLY:
exit 3, distinct from 1 (measured drift) and 0 (checked and clean). Same
convention `export_ks4_questions.py --verify` uses and for the same reason:
a gate that passes because it could not look is worse than no gate.

── `--baseline <FILE>` ────────────────────────────────────────────────────

Lets the same proof run with no network and no credential at all, and lets
it run TWICE around a load to prove nothing moved because of the load
itself:

    python3 frozen_window_guard.py --baseline snap.json   # BEFORE a load:
                                                          # file doesn't exist
                                                          # yet, so this WRITES
                                                          # it (from production
                                                          # if a credential is
                                                          # available, else
                                                          # from the currently
                                                          # authored Python)
    …apply the load…
    python3 frozen_window_guard.py --baseline snap.json   # AFTER: the file now
                                                          # exists, so this
                                                          # COMPARES the current
                                                          # authored Python
                                                          # against the snapshot
                                                          # taken before the load

The second run needs no network at all — it is a pure Python-vs-JSON-file
comparison — so it can be re-run as many times as wanted while a load is
being investigated.
"""

import argparse
import collections
import datetime
import json
import os
import ssl
import sys
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO)

import export_ks3_questions as ks3x
import export_ks4_questions as ks4x
import frozen_window_allowlist as fwa

PROD_REF = "urklkrwevjtlfbwnipjn"
PROD_ENV = os.path.expanduser("~/.mrbadmus/prod.env")

KS3_TABLE = "ks3_assignment_bank"
KS3_ID_FIELD = "id"
KS3_LEAF_FIELDS = ("unit_code", "lesson_slug")
KS3_COLUMNS = ks3x.BANK_COLUMNS   # id, unit_code, lesson_slug, band,
                                  # bank_position, text, figure, options
KS3_ALLOWED_DIFF = frozenset({"text", "options", "figure"})

KS4_TABLE = "ks4_assignment_bank"
KS4_ID_FIELD = "id"
KS4_LEAF_FIELDS = ("subtopic_slug",)

# ⚠️ MRB-352 gave `ks4_assignment_bank` a `figure` column, but the migration
# ships "NOT applied to production by this run" (figure-contract.md §6) — so
# `export_ks4_questions.COLUMNS` always includes `"figure"` now (it is real in
# every AUTHORED row, via `ks4_data.load_pool`), while the LIVE table may or
# may not have it. `export_ks4_questions.py` handles exactly this split with
# `OPTIONAL_COLUMNS` and a one-shot `_has_figure_column()` probe, so this
# reuses both rather than hand-rolling a second probe that could drift from
# theirs. `KS4_BASE_COLUMNS` is what is ALWAYS there; `figure` is added to it
# only once the live/reference side has proved it has the column.
KS4_OPTIONAL_COLUMNS = getattr(ks4x, "OPTIONAL_COLUMNS", frozenset())
KS4_BASE_COLUMNS = [c for c in ks4x.COLUMNS if c not in KS4_OPTIONAL_COLUMNS]


def ks4_effective_columns(has_figure):
    """The KS4 column list to compare THIS run — `figure` included only when
    the reference side (production, or a baseline snapshot) has proved it
    actually carries that column. Comparing a column that is not there yet
    would report every row as "differs in figure", which is phantom drift,
    not a finding."""
    if has_figure and "figure" in ks4x.COLUMNS:
        return list(KS4_BASE_COLUMNS) + ["figure"]
    return list(KS4_BASE_COLUMNS)


def ks4_allowed_diff(has_figure):
    base = {"text", "options"}
    return base | ({"figure"} if has_figure else set())


KS3_ALLOWED_DIFF = frozenset({"text", "options", "figure"})


def ks3_hash(row):
    return ks3x.checksum([row], KS3_COLUMNS)


def ks4_hash_with(columns):
    """A hash function bound to a specific effective column list — needed
    because, unlike KS3's, whether KS4 compares `figure` at all is decided
    per run, from what the reference side actually has."""
    def _hash(row):
        return ks4x.checksum([row], columns)
    return _hash


def _which_fields_differ(hash_fn, columns, id_field, a, b):
    """The field(s) where `a` and `b` disagree, found by asking the SAME
    `checksum()` `hash_fn` calls to hash `a` with exactly one field swapped
    for `b`'s value at a time. If that changes the hash, that field is where
    they differ — and the normalisation used to decide it is theirs, not a
    second copy of it."""
    base = hash_fn(a)
    diffs = []
    for f in columns:
        if f == id_field:
            continue
        cand = dict(a)
        cand[f] = b.get(f)
        if hash_fn(cand) != base:
            diffs.append(f)
    return diffs


def compare_pool(pool_label, id_field, leaf_fields, columns, hash_fn,
                  authored_rows, reference_rows, allowed_diff_fields):
    """The four-part proof, for one pool. `reference_rows` must already be
    restricted to the frozen window (bank_position < 12) — both the
    production fetch and the baseline writer below do that filtering."""
    problems = []
    frozen = [r for r in authored_rows if r["bank_position"] < 12]
    by_id_a = {r[id_field]: r for r in frozen}
    by_id_b = {r[id_field]: r for r in reference_rows}

    only_a = sorted(set(by_id_a) - set(by_id_b))
    only_b = sorted(set(by_id_b) - set(by_id_a))
    if only_a:
        problems.append(
            "%s: %d frozen row(s) authored but NOT in the reference — %s. "
            "Either a new row landed inside the frozen window (forbidden by "
            "MRB-335/RISKS D7) or the export/load has not been applied yet."
            % (pool_label, len(only_a), ", ".join(only_a[:8])))
    if only_b:
        problems.append(
            "%s: %d frozen row(s) the reference still serves that are no "
            "longer authored — %s. A frozen row may be EDITED in place under "
            "the MRB-352 allowlist; it may never be removed."
            % (pool_label, len(only_b), ", ".join(only_b[:8])))

    unexpected = []
    for rid in sorted(set(by_id_a) & set(by_id_b)):
        a, b = by_id_a[rid], by_id_b[rid]
        if hash_fn(a) == hash_fn(b):
            continue
        diffs = _which_fields_differ(hash_fn, columns, id_field, a, b)
        if rid not in fwa.ALLOWLIST:
            unexpected.append(rid)
            problems.append(
                "%s %s: NOT on the frozen-window allowlist but differs from "
                "the reference in %s" % (pool_label, rid, ", ".join(diffs)))
            continue
        bad = [f for f in diffs if f not in allowed_diff_fields]
        if bad:
            unexpected.append(rid)
            problems.append(
                "%s %s: ALLOWLISTED, but changed field(s) the ruling forbids "
                "— %s (only %s may change)"
                % (pool_label, rid, ", ".join(bad),
                   "/".join(sorted(allowed_diff_fields))))

    # ── property 4 — positions 0-11: same SET, same ORDER, per leaf ──────
    def leaf_of(r):
        return tuple(r[f] for f in leaf_fields)

    leaves_a = collections.defaultdict(list)
    leaves_b = collections.defaultdict(list)
    for r in frozen:
        leaves_a[leaf_of(r)].append(r)
    for r in reference_rows:
        leaves_b[leaf_of(r)].append(r)

    order_mismatches = 0
    for leaf in sorted(set(leaves_a) | set(leaves_b)):
        order_a = [r[id_field] for r in
                   sorted(leaves_a.get(leaf, []), key=lambda r: r["bank_position"])]
        order_b = [r[id_field] for r in
                   sorted(leaves_b.get(leaf, []), key=lambda r: r["bank_position"])]
        if order_a != order_b:
            order_mismatches += 1
            problems.append(
                "%s %r: the auto-composition window's id ORDER changed — "
                "python has %s, reference has %s"
                % (pool_label, leaf, order_a, order_b))

    ok = not problems
    print("  %s %-3s  %4d frozen authored, %4d frozen in reference, "
          "%d missing-from-reference, %d missing-from-authored, "
          "%d unexpected diff(s), %d leaf order mismatch(es)"
          % ("✅" if ok else "❌", pool_label, len(frozen), len(reference_rows),
             len(only_a), len(only_b), len(unexpected), order_mismatches))
    return problems


# ── reading production, read-only ───────────────────────────────────────

def _prod_credential():
    """(key, url) for production, proved from the key's own `ref` claim —
    or (None, reason). Never raises; the caller turns a reason into a loud
    skip rather than a traceback three frames from a network call."""
    try:
        conf = {}
        with open(PROD_ENV, encoding="utf-8") as fh:
            for line in fh:
                if "=" in line and not line.lstrip().startswith("#"):
                    k, v = line.split("=", 1)
                    conf[k.strip()] = v.strip()
    except OSError as exc:
        return None, "%s is not readable (%s)" % (PROD_ENV, exc)

    key = conf.get("SUPABASE_SERVICE_ROLE_KEY", "")
    if not key:
        return None, "%s sets no SUPABASE_SERVICE_ROLE_KEY" % PROD_ENV

    ref = ks4x._jwt_ref(key)
    if ref is None:
        return None, ("the SUPABASE_SERVICE_ROLE_KEY in %s is not a readable "
                      "JWT, so the project it belongs to cannot be "
                      "established" % PROD_ENV)
    if ref != PROD_REF:
        return None, ("that key belongs to project %r, not production %r — "
                      "refusing rather than reading whatever it opens"
                      % (ref, PROD_REF))

    url = conf.get("SUPABASE_URL", "") or ("https://%s.supabase.co" % ref)
    if PROD_REF not in url:
        return None, ("%s sets a SUPABASE_URL that does not match its own "
                      "key" % PROD_ENV)
    return (key, url), None


def fetch_production():
    """The frozen window (bank_position < 12) of both live tables, or
    (None, reason). Read-only: every request is a GET.

    Returns (ks3_rows, ks4_rows, ks4_has_figure), None on success.
    `ks4_has_figure` is PROBED, never assumed — MRB-352's `figure` column
    on `ks4_assignment_bank` ships in a migration that is deliberately NOT
    applied to production by that run (figure-contract.md §6), so asking
    production to `select=...,figure` today gets PostgREST's 42703
    (undefined_column), a hard 400, not an empty column. Reusing
    `export_ks4_questions._has_figure_column` — the same probe that
    exporter's own `--load`/`--verify` already run before touching the
    column — means this can never drift from what the exporter itself
    believes is live."""
    cred, err = _prod_credential()
    if err:
        return None, err
    key, url = cred
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    headers = {"apikey": key, "Authorization": "Bearer " + key}

    def get(path):
        req = urllib.request.Request(url.rstrip("/") + path, method="GET")
        req.add_header("apikey", key)
        req.add_header("Authorization", "Bearer " + key)
        with urllib.request.urlopen(req, context=ctx, timeout=90) as r:
            return json.loads(r.read().decode())

    def fetch_all(table, cols):
        out, step = [], 1000
        while True:
            page = get("/rest/v1/%s?select=%s&bank_position=lt.12&order=%s"
                       "&limit=%d&offset=%d"
                       % (table, cols, cols.split(",")[0], step, len(out)))
            out.extend(page)
            if len(page) < step:
                return out

    has_figure_probe = getattr(ks4x, "_has_figure_column", None)
    try:
        has_figure = bool(has_figure_probe(url, headers, ctx)) \
            if has_figure_probe else False
    except Exception as exc:
        return None, ("probing %s for a figure column failed (%s)"
                      % (KS4_TABLE, exc))

    ks4_cols = ks4_effective_columns(has_figure)
    if not has_figure:
        print("     ⚠️ column-absent mode: production has no `figure` "
              "column on %s yet (MRB-352 migration not applied there). "
              "Comparing KS4 without it." % KS4_TABLE)

    try:
        ks3_rows = fetch_all(
            KS3_TABLE, "id,unit_code,lesson_slug,band,bank_position,text,"
                      "figure,options")
        ks4_rows = fetch_all(KS4_TABLE, ",".join(ks4_cols))
    except urllib.error.HTTPError as exc:
        detail = ""
        try:
            detail = exc.read().decode()[:300]
        except Exception:
            pass
        return None, "reading production failed (HTTP %s) %s" % (exc.code, detail)
    except Exception as exc:
        return None, "reading production failed (%s)" % exc

    for r in ks4_rows:
        r["triple_only"] = bool(r["triple_only"])
    return (ks3_rows, ks4_rows, has_figure), None


# ── the baseline file ────────────────────────────────────────────────────

def write_baseline(path, ks3_rows, ks4_rows, ks4_has_figure, source):
    data = dict(
        generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source=source,
        ks4_has_figure=bool(ks4_has_figure),
        ks3_frozen_rows=ks3_rows,
        ks4_frozen_rows=ks4_rows,
    )
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, sort_keys=True, ensure_ascii=False)


def read_baseline(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return (data["ks3_frozen_rows"], data["ks4_frozen_rows"],
            bool(data.get("ks4_has_figure", False)), data)


# ── main ─────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--baseline",
                    help="write this JSON file if it does not exist yet "
                         "(from production if reachable, else from the "
                         "currently authored Python), or compare against it "
                         "if it does — no network needed either way once it "
                         "exists")
    args = ap.parse_args()

    print("\n🧊  frozen_window_guard — MRB-352, the 28-id exception made "
          "narrow\n")

    authored_ks3 = ks3x.bank_rows()
    from ks4_data import load_pool
    authored_ks4 = load_pool(strict=True)

    problems = []

    # ── requirement 3: the allowlist is exactly 28 ids, all real, all
    #    still inside the frozen window ───────────────────────────────────
    if len(fwa.ALLOWLIST) != 28:
        problems.append("frozen_window_allowlist.ALLOWLIST has %d id(s), "
                        "not 28" % len(fwa.ALLOWLIST))

    by_id_ks3 = {r["id"]: r for r in authored_ks3}
    by_id_ks4 = {r["id"]: r for r in authored_ks4}
    stale, moved = [], []
    for aid in sorted(fwa.ALLOWLIST):
        row = by_id_ks3.get(aid, by_id_ks4.get(aid))
        if row is None:
            stale.append(aid)
        elif row["bank_position"] >= 12:
            moved.append(aid)
    if stale:
        problems.append(
            "%d allowlisted id(s) do not exist in the authored corpus "
            "(stale): %s" % (len(stale), ", ".join(stale)))
    if moved:
        problems.append(
            "%d allowlisted id(s) exist but have moved OUTSIDE the frozen "
            "window (bank_position >= 12), so the ruling no longer applies "
            "to them: %s" % (len(moved), ", ".join(moved)))
    print("  allowlist   %d id(s) (%d confirmed, %d borderline), %d stale, "
          "%d moved outside the window"
          % (len(fwa.ALLOWLIST), len(fwa.CONFIRMED), len(fwa.BORDERLINE),
             len(stale), len(moved)))

    # ── source the reference: production, or a --baseline file ──────────
    if args.baseline:
        if os.path.exists(args.baseline):
            ks3_ref, ks4_ref, ks4_has_figure, meta = read_baseline(args.baseline)
            print("  reference   baseline %s (captured %s from %s)"
                  % (args.baseline, meta.get("generated_at", "?"),
                     meta.get("source", "?")))
            if not ks4_has_figure:
                print("     ⚠️ column-absent mode: this baseline was captured "
                      "without a `figure` column on %s. Comparing KS4 "
                      "without it." % KS4_TABLE)
        else:
            fetched, ferr = fetch_production()
            if fetched is not None:
                ks3_ref, ks4_ref, ks4_has_figure = fetched
                source = "production (%s)" % PROD_REF
                print("  writing baseline %s from PRODUCTION" % args.baseline)
            else:
                ks3_ref = [r for r in authored_ks3 if r["bank_position"] < 12]
                ks4_ref = [r for r in authored_ks4 if r["bank_position"] < 12]
                # ⚠️ Conservative on purpose: without a credential this
                # cannot PROVE production has the figure column (it does
                # not, as of MRB-352 — see figure-contract.md §6), so the
                # python-fallback snapshot never claims it either, even
                # though every authored KS4 row now carries a `figure` key.
                ks4_has_figure = False
                source = "python-snapshot (production unavailable: %s)" % ferr
                print("  ⚠️  production unavailable (%s)" % ferr)
                print("     writing baseline %s from the CURRENTLY AUTHORED "
                      "python instead — this is only as good as that being "
                      "in sync with what is live" % args.baseline)
            write_baseline(args.baseline, ks3_ref, ks4_ref, ks4_has_figure,
                           source)
            print("\n  ✅ wrote %s — %d KS3 + %d KS4 frozen row(s) "
                  "(ks4 figure column: %s).\n"
                  "     Re-run with the SAME --baseline to COMPARE against "
                  "it (no network needed for that run).\n"
                  % (args.baseline, len(ks3_ref), len(ks4_ref),
                     "present" if ks4_has_figure else "absent"))
            return 0
    else:
        fetched, err = fetch_production()
        if fetched is None:
            print("\n  ⏭️  SKIPPED (exit 3): could not read production — %s"
                  % err)
            print("      This is NOT a pass. The frozen window has not been "
                  "compared against anything.")
            print("      Use --baseline <file> to check offline instead.\n")
            return 3
        ks3_ref, ks4_ref, ks4_has_figure = fetched
        print("  reference   PRODUCTION (%s), read-only" % PROD_REF)

    ks4_columns = ks4_effective_columns(ks4_has_figure)
    problems += compare_pool("KS3", KS3_ID_FIELD, KS3_LEAF_FIELDS,
                              KS3_COLUMNS, ks3_hash, authored_ks3, ks3_ref,
                              KS3_ALLOWED_DIFF)
    problems += compare_pool("KS4", KS4_ID_FIELD, KS4_LEAF_FIELDS,
                              ks4_columns, ks4_hash_with(ks4_columns),
                              authored_ks4, ks4_ref,
                              ks4_allowed_diff(ks4_has_figure))

    print()
    if problems:
        print("❌ %d problem(s)\n" % len(problems))
        for p in problems:
            print("   · %s" % p)
        print()
        return 1

    print("✅ every frozen row not on the allowlist is byte-identical to "
          "%s; all 28 allowlisted rows changed only fields the ruling "
          "permits; positions 0-11 hold the same ids in the same order, "
          "per leaf.\n"
          % ("the baseline" if args.baseline else "production"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
