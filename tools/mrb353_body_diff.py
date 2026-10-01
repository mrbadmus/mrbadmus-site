#!/usr/bin/env python3
"""mrb353_body_diff.py — MRB-353: the new flashcard_record differs from
production's ONLY by the finish walk and the verdict lookup. Nothing removed.

    python3 tools/mrb353_body_diff.py [--deployed-md5 MD5]

Reads two bodies (the bytes between the `$$` markers — exactly what
`pg_proc.prosrc` holds):
  · BASE — the rollback file's flashcard_record, which must be production's
    live body (prosrc md5 5380b3e22fee33b2d0fd197fa3032916);
  · NEW  — the migration file's flashcard_record.
and diffs them line by line. Exit 0 only when:
  · BASE md5 is production's;
  · every line ADDED sits inside a `-- ⊕ MRB-353 verdict` / `-- ⊕ MRB-353
    finish walk` block, or is one of the named replacement lines below;
  · every line REMOVED is one of the named replaced lines below (the old
    completion test and the three `v_now` stamps, and the two
    `coalesce(…, 'pending')` lines the verdict lookup extends);
  · with --deployed-md5 (TEST's `select md5(prosrc) from pg_proc where
    proname='flashcard_record'` after apply), the deployed body IS the NEW
    body — so the diff above is the diff of what is deployed.
"""
import argparse, difflib, hashlib, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIG = os.path.join(ROOT, "supabase/migrations/20261001190000_mrb353_flashcard_verdicts_finish.sql")
RB = os.path.join(ROOT, "supabase/rollbacks/20261001190000_mrb353_flashcard_verdicts_finish_rollback.sql")
PROD_MD5 = "5380b3e22fee33b2d0fd197fa3032916"

# Lines of production's body the migration REPLACES (never just deletes).
REMOVED_OK = {
    "                 coalesce(public.flashcard_quick_check(e->>'answer', af.answer), 'pending')",
    "                     (select af.answer from public.assignment_flashcards af where af.id = r.card_id)), 'pending') end)",
    "  select v_n > 0 and bool_and(cs.secured and (v_a.flashcard_mode <> 'make' or cs.made))",
    "    into v_done from public.flashcard_card_state(p_assignment, v_uid) cs;",
    "              v_now, v_now,",
    "              'complete', (v_a.due_at is not null and v_now > v_a.due_at), 1, 1)",
    "      update public.assignment_submissions set score = v_n, max_score = v_n, submitted_at = v_now,",
    "             completed_at = v_now, status = 'complete',",
    "             is_late = (v_a.due_at is not null and v_now > v_a.due_at), updated_at = v_now",
}
# Their replacements, outside the marked blocks.
ADDED_OK = {
    "                 coalesce(public.flashcard_quick_check(e->>'answer', af.answer),",
    "                          'pending')",
    "                     (select af.answer from public.assignment_flashcards af where af.id = r.card_id)),",
    "                     'pending') end)",
    "              v_finish_server, v_finish_server,",
    "              'complete', (v_a.due_at is not null and v_finish_server > v_a.due_at), 1, 1)",
    "      update public.assignment_submissions set score = v_n, max_score = v_n, submitted_at = v_finish_server,",
    "             completed_at = v_finish_server, status = 'complete',",
    "             is_late = (v_a.due_at is not null and v_finish_server > v_a.due_at), updated_at = v_now",
}


def body(path):
    t = open(path, encoding="utf-8").read()
    m = re.search(r"create or replace function public\.flashcard_record\(.*?as \$\$(.*?)\$\$;", t, re.S)
    if not m:
        sys.exit("no flashcard_record body in " + path)
    return m.group(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--deployed-md5")
    args = ap.parse_args()
    base, new = body(RB), body(MIG)
    bad = []
    bmd5 = hashlib.md5(base.encode()).hexdigest()
    nmd5 = hashlib.md5(new.encode()).hexdigest()
    print("base (rollback) md5 %s  len %d" % (bmd5, len(base)))
    print("new  (migration) md5 %s  len %d" % (nmd5, len(new)))
    if bmd5 != PROD_MD5:
        bad.append("rollback body is not production's (%s)" % PROD_MD5)
    if args.deployed_md5 and args.deployed_md5 != nmd5:
        bad.append("deployed body %s is not the migration's body" % args.deployed_md5)

    a, b = base.split("\n"), new.split("\n")
    added, removed, in_block = [], [], None
    marked = set()
    for i, line in enumerate(b):              # which NEW lines sit in a marked block
        s = line.strip()
        if s.startswith("-- ⊕ MRB-353"):
            in_block = s
        if in_block:
            marked.add(i)
        if s.startswith("-- /⊕ MRB-353"):
            in_block = None
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ("delete", "replace"):
            removed += a[i1:i2]
        if op in ("insert", "replace"):
            added += [(j, b[j]) for j in range(j1, j2)]
    for line in removed:
        if line not in REMOVED_OK:
            bad.append("REMOVED a production line: %r" % line)
    unexplained = [l for j, l in added if j not in marked and l not in ADDED_OK]
    for line in unexplained:
        bad.append("ADDED outside a ⊕ MRB-353 block: %r" % line)
    print("lines removed: %d (all named replacements: %s)" % (len(removed), all(l in REMOVED_OK for l in removed)))
    print("lines added:   %d (%d inside ⊕ MRB-353 blocks, %d named replacements)"
          % (len(added), sum(1 for j, _ in added if j in marked), sum(1 for j, l in added if j not in marked and l in ADDED_OK)))
    blocks = sorted({b[j].strip() for j in marked if b[j].strip().startswith("-- ⊕ MRB-353")})
    print("blocks: " + "; ".join(blocks))
    if bad:
        for x in bad:
            print("FAIL " + x)
        sys.exit(1)
    print("PASS flashcard_record = production's body + the finish walk + the verdict lookup; nothing removed")


if __name__ == "__main__":
    main()
