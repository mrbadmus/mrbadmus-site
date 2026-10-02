#!/usr/bin/env python3
"""mrb354_body_diff.py — MRB-354: secured, one rule (Mide, 2 Oct 2026).

    python3 tools/mrb354_body_diff.py [--deployed-card-state-md5 MD5] [--deployed-record-md5 MD5]

For EACH of flashcard_card_state and flashcard_record, reads two bodies (the
bytes between the `$$` markers — exactly what `pg_proc.prosrc` holds):
  · BASE — the rollback file's body, which must be:
      - flashcard_card_state: production's CURRENT body
        (prosrc md5 2ed66c5fa80fc0b1151f0e7d8729dbf4)
      - flashcard_record: MRB-353's body — production's PARKED next body,
        not production's live one (prosrc md5 85643a2ba4e2ab5bf718b0356a2401d8)
  · NEW  — the migration file's body.
and diffs them line by line. Exit 0 only when:
  · both BASE md5s match the named bodies above;
  · every line REMOVED is one of the named replaced lines below, and every
    line ADDED sits inside a `-- ⊕ MRB-354` / `-- /⊕ MRB-354` block or is one
    of the named replacement lines (the two-line `secured` select in
    card_state; the three-line ⊕ MRB-354 declare-block header in record);
  · with --deployed-card-state-md5 / --deployed-record-md5 (TEST's or
    production's `select md5(prosrc) from pg_proc where proname = …` after
    apply), the deployed body IS the migration's body.
"""
import argparse, difflib, hashlib, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIG = os.path.join(ROOT, "supabase/migrations/20261002120000_mrb354_one_word_secured.sql")
RB = os.path.join(ROOT, "supabase/rollbacks/20261002120000_mrb354_one_word_secured_rollback.sql")

BASE_MD5 = {
    "flashcard_card_state": "2ed66c5fa80fc0b1151f0e7d8729dbf4",
    "flashcard_record": "85643a2ba4e2ab5bf718b0356a2401d8",
}

# Lines of the BASE body each migration REPLACES (never just deletes), and
# their replacements. Keyed by function name.
REMOVED_OK = {
    "flashcard_card_state": {
        "  select per.id, per.position, per.made, per.known,",
        "         case when (select completion_rule from a) = 'quick' then per.known else per.twice end,",
    },
    "flashcard_record": {
        "  -- ⊕ MRB-353 finish walk: the round-aware walkReview()/finishedAt() walk, in SQL.",
        "  v_deck_ids     uuid[];",
        "  v_latest       jsonb := '{}'::jsonb;",
        "  v_made         jsonb := '{}'::jsonb;",
        "  v_targets      uuid[];",
        "  v_round_done   jsonb := '{}'::jsonb;",
        "  v_round_complete boolean := false;",
        "  v_last_at      timestamptz;",
        "  -- /⊕ MRB-353 finish walk",
        "  -- ⊕ MRB-353 finish walk: DONE = the pupil reached the engine's Done screen",
        "  -- once (Mide, 1 Oct 2026), found by the same round-aware walk as",
        "  -- shared/flashcard-homework.js walkReview()/finishedAt(). Secured is the",
        "  -- separate, smaller fact and no longer gates the submission.",
        "  select array_agg(id) into v_deck_ids from public.assignment_flashcards where assignment_id = p_assignment;",
        "  v_targets := v_deck_ids;",
        "  if v_n > 0 then",
        "    for r in select rv.card_id, rv.rating, rv.phase, rv.event_id, rv.rated_at",
        "               from public.flashcard_reviews rv",
        "              where rv.assignment_id = p_assignment and rv.pupil_id = v_uid",
        "                and rv.card_id = any (v_deck_ids)",
        "                and rv.rating in ('got_it', 'nearly', 'not_yet')",
        "              order by rv.rated_at, rv.id",
        "    loop",
        "      if coalesce(r.phase, 'review') = 'make' then",
        "        v_made := v_made || jsonb_build_object(r.card_id::text, true);",
        "        continue;",
        "      end if;",
        "      -- make mode: a review row counts only once every card has a make row.",
        "      continue when v_a.flashcard_mode = 'make'",
        "        and exists (select 1 from unnest(v_deck_ids) d(id) where not (v_made ? d.id::text));",
        "      -- a finished round that was not all right: back within the hour →",
        "      -- the leftovers, round n+1; gone an hour → a fresh pass (reset()).",
        "      if v_round_complete then",
        "        if v_last_at is not null and r.rated_at - v_last_at >= interval '60 minutes' then",
        "          v_latest := '{}'::jsonb; v_targets := v_deck_ids; v_round_done := '{}'::jsonb;",
        "        else",
        "          select coalesce(array_agg(d.id), '{}'::uuid[]) into v_targets",
        "            from unnest(v_deck_ids) d(id)",
        "           where coalesce(v_latest ->> d.id::text, '') <> 'got_it';",
        "          v_round_done := '{}'::jsonb;",
        "        end if;",
        "        v_round_complete := false;",
        "      end if;",
        "      v_latest := v_latest || jsonb_build_object(r.card_id::text, r.rating);",
        "      if r.card_id = any (v_targets) then",
        "        v_round_done := v_round_done || jsonb_build_object(r.card_id::text, true);",
        "      end if;",
        "      v_last_at := r.rated_at;",
        "      -- every card's latest rating in the pass showing now is Got it → Done.",
        "      if not exists (select 1 from unnest(v_deck_ids) d(id)",
        "                      where coalesce(v_latest ->> d.id::text, '') <> 'got_it') then",
        "        v_finish_event := r.event_id;",
        "        v_finish_at := r.rated_at;",
        "        exit;",
        "      end if;",
        "      if not exists (select 1 from unnest(v_targets) t(id) where not (v_round_done ? t.id::text)) then",
        "        v_round_complete := true;",
        "      end if;",
        "    end loop;",
        "  end if;",
        "  v_done := v_finish_at is not null;",
        "  -- the SERVER time of the finishing rating, never the device clock and",
        "  -- never this call's now() (re-deriving later must stamp the same instant).",
        "  if v_done then",
        "    select ev.server_at into v_finish_server from public.flashcard_events ev where ev.id = v_finish_event;",
        "    v_finish_server := coalesce(v_finish_server, least(v_finish_at, v_now));",
        "  end if;",
        "  -- /⊕ MRB-353 finish walk",
    },
}

NAMED_ADDED_OK = {
    "flashcard_card_state": {
        "  select per.id, per.position, per.made, per.known,",
        "         per.known,",
    },
    "flashcard_record": {
        "  -- ⊕ MRB-354: secured, one rule (Mide, 2 Oct 2026).",
        "  v_finish_at    timestamptz;",
        "  v_finish_event uuid;",
        "  v_finish_server timestamptz;",
        "  -- /⊕ MRB-354",
        "  if v_done then",
        "    select ev.server_at into v_finish_server from public.flashcard_events ev where ev.id = v_finish_event;",
        "    v_finish_server := coalesce(v_finish_server, least(v_finish_at, v_now));",
        "  end if;",
        "  -- /⊕ MRB-354",
    },
}


def body(path, fname):
    t = open(path, encoding="utf-8").read()
    pat = r"create or replace function public\." + fname + r"\(.*?\bas \$(\w*)\$(.*?)\$\1\$"
    m = re.search(pat, t, re.S | re.I)
    if not m:
        sys.exit("no %s body in %s" % (fname, path))
    return m.group(2)


def check_one(fname, args_md5):
    base, new = body(RB, fname), body(MIG, fname)
    bmd5 = hashlib.md5(base.encode()).hexdigest()
    nmd5 = hashlib.md5(new.encode()).hexdigest()
    print("== %s ==" % fname)
    print("base (rollback) md5 %s  len %d" % (bmd5, len(base)))
    print("new  (migration) md5 %s  len %d" % (nmd5, len(new)))
    bad = []
    if bmd5 != BASE_MD5[fname]:
        bad.append("%s: rollback body is not the named base (%s)" % (fname, BASE_MD5[fname]))
    if args_md5 and args_md5 != nmd5:
        bad.append("%s: deployed body %s is not the migration's body" % (fname, args_md5))

    a, b = base.split("\n"), new.split("\n")
    marked = set()
    in_block = False
    for i, line in enumerate(b):
        s = line.strip()
        if s.startswith("-- ⊕ MRB-354"):
            in_block = True
        if in_block:
            marked.add(i)
        if s.startswith("-- /⊕ MRB-354"):
            in_block = False

    removed, added = [], []
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ("delete", "replace"):
            removed += a[i1:i2]
        if op in ("insert", "replace"):
            added += [(j, b[j]) for j in range(j1, j2)]

    for line in removed:
        if line not in REMOVED_OK[fname]:
            bad.append("%s: REMOVED a base line not named as replaced: %r" % (fname, line))
    unexplained_added = [l for j, l in added if j not in marked and l not in NAMED_ADDED_OK[fname]]
    for line in unexplained_added:
        bad.append("%s: ADDED outside a ⊕ MRB-354 block: %r" % (fname, line))

    print("lines removed: %d (all named: %s)" % (len(removed), all(l in REMOVED_OK[fname] for l in removed)))
    print("lines added:   %d (%d inside ⊕ MRB-354 blocks, %d named)"
          % (len(added), sum(1 for j, _ in added if j in marked),
             sum(1 for j, l in added if j not in marked and l in NAMED_ADDED_OK[fname])))
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--deployed-card-state-md5")
    ap.add_argument("--deployed-record-md5")
    args = ap.parse_args()

    bad = []
    bad += check_one("flashcard_card_state", args.deployed_card_state_md5)
    bad += check_one("flashcard_record", args.deployed_record_md5)

    if bad:
        for x in bad:
            print("FAIL " + x)
        sys.exit(1)
    print("\nPASS both bodies = named base + only ⊕ MRB-354 changes")


if __name__ == "__main__":
    main()
