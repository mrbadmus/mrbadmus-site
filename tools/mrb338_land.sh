#!/usr/bin/env bash
#
# MRB-338 · the commit gate. Rebuilt IN THE REPO.
#
#   tools/mrb338_land.sh --unit C3 --lesson filtration -- ks3_data/c3/questions_04_filtration.py
#   tools/mrb338_land.sh --subtopic stem-cells -- ks4_data/questions/biology/cell_biology__z338_stem_cells.py
#   tools/mrb338_land.sh --unit B4
#
# Everything BEFORE `--` is passed straight to `tools/mrb338_leafcheck.py`.
# Everything AFTER `--` is the pathspec: the files this lane is about to
# commit. The pathspec is reported, never committed — see below.
#
# ── WHY THIS FILE EXISTS ────────────────────────────────────────────────
#
# Night 1 ran exactly this sequence before every commit, out of a session
# scratch directory, and it went with the session. REPORT §8 makes rebuilding
# it in the repo one of the two harness changes that must land before night 2
# authors anything.
#
# ── ⚠️ IT DOES NOT COMMIT, DELIBERATELY ─────────────────────────────────
#
# REPORT §10 deviation 6: night 1 chained `check && git add && git commit`,
# and because the CHECK COMMAND ITSELF succeeded — it printed red and exited
# 0 — the commit ran anyway. `chromosomes-mitosis` landed with a near-twin
# still in it. This script reports and exits; the human commits. A gate that
# can commit is a gate that can commit the wrong thing.
#
# ── ⚠️ `set_work_scope_check` IS NOT OPTIONAL ───────────────────────────
#
# REPORT §3 / brief §9.5. It is the ONLY gate that sees a new row colliding
# with a row in a DIFFERENT LEAF of the same unit or topic — it treats a whole
# KS3 unit and a whole KS4 topic as one cell. Night 1 shipped two such
# duplicates because it was not being run. With several lanes writing one unit
# in parallel, unable to read each other's uncommitted files, nothing else in
# the estate can see them. It takes under a second.
#
# ── ⚠️ THE WORKTREE IS SHARED ───────────────────────────────────────────
#
# Several lanes write one checkout. That is why the pathspec exists: a lane
# commits ITS files by naming them, never `git commit -a`. This script prints
# the commit command with the pathspec already in it and stops there.
#
# Exit 0 = every gate green. Exit 1 = a gate is red, and its FULL output is
# printed. No gate is ever weakened to make something pass; a red gate is a
# finding.

set -u

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO" || exit 2

LEAF_ARGS=()
PATHSPEC=()
seen_sep=0
for a in "$@"; do
  if [ "$a" = "--" ] && [ $seen_sep -eq 0 ]; then seen_sep=1; continue; fi
  if [ $seen_sep -eq 0 ]; then LEAF_ARGS+=("$a"); else PATHSPEC+=("$a"); fi
done

if [ ${#LEAF_ARGS[@]} -eq 0 ]; then
  cat >&2 <<'USAGE'
usage: tools/mrb338_land.sh <leafcheck args> [-- <pathspec>...]

  tools/mrb338_land.sh --unit C3 --lesson filtration -- ks3_data/c3/questions_04_filtration.py
  tools/mrb338_land.sh --subtopic stem-cells -- ks4_data/questions/biology/cell_biology__z338_stem_cells.py

Leafcheck args: --unit CODE [--lesson SLUG]  (KS3)
                --topic ID | --subtopic SLUG (KS4)
USAGE
  exit 2
fi

OUT="$(mktemp -d)"
trap 'rm -rf "$OUT"' EXIT

echo "════════════════════════════════════════════════════════════════════════"
echo "mrb338_land — every gate that must be green before this unit commits"
echo "  repo:      $REPO"
echo "  branch:    $(git rev-parse --abbrev-ref HEAD)"
echo "  leafcheck: ${LEAF_ARGS[*]}"
if [ ${#PATHSPEC[@]} -gt 0 ]; then
  echo "  pathspec:  ${PATHSPEC[*]}"
else
  echo "  pathspec:  (none given — the commit line at the end will be generic)"
fi
echo "════════════════════════════════════════════════════════════════════════"

if [ ${#PATHSPEC[@]} -gt 0 ]; then
  echo
  echo "── what this pathspec currently holds ──────────────────────────────"
  git status --short -- "${PATHSPEC[@]}" || true
  git diff --stat -- "${PATHSPEC[@]}" || true
fi

# ⚠️ ORDER MATTERS AND IS NOT ALPHABETICAL. Cheap structural gates first, so a
# malformed row is named in one second rather than after the slow ones. The
# leaf checker runs LAST because it is an advisor: the gates decide.
#
# Each entry is one command. `python3 -m ks3_data.question_bank` is a module,
# not a script — it has no file of its own to call.
declare -a NAMES=(
  "verify_questions"
  "verify_answer_positions"
  "pool_ownership"
  "question_bank"
  "ks4_pool_check"
  "verify_answer_lengths"
  "set_work_scope_check"
  "mrb338_leafcheck"
)

run_gate () {
  local name="$1"; shift
  local log="$OUT/$name.log"
  local start=$SECONDS
  printf "\n── %-24s %s\n" "$name" "$*"
  "$@" > "$log" 2>&1
  local rc=$?
  local took=$(( SECONDS - start ))
  if [ $rc -ne 0 ]; then
    echo "   ❌ RED  (exit $rc, ${took}s) — full output follows, nothing after "
    echo "           this ran, and NOTHING IS COMMITTED."
    echo "   ────────────────────────────────────────────────────────────────"
    sed 's/^/   │ /' "$log"
    echo "   ────────────────────────────────────────────────────────────────"
    echo
    echo "mrb338_land: ❌ $name is RED. Fix the finding — never the gate."
    exit 1
  fi
  # The gate's own verdict line. ⚠️ LAST NON-BLANK, not `tail -n 1`: several
  # of these end with a blank line and the summary then showed nothing at all,
  # which reads as a gate that printed no verdict.
  echo "   ✅ green (${took}s)  $(grep -v '^[[:space:]]*$' "$log" | tail -n 1 | cut -c1-96)"
  return 0
}

run_gate "verify_questions"        python3 verify_questions.py
run_gate "verify_answer_positions" python3 verify_answer_positions.py
run_gate "pool_ownership"          python3 pool_ownership.py
run_gate "question_bank"           python3 -m ks3_data.question_bank
run_gate "ks4_pool_check"          python3 ks4_pool_check.py --python
run_gate "verify_answer_lengths"   python3 verify_answer_lengths.py
run_gate "set_work_scope_check"    python3 set_work_scope_check.py
run_gate "mrb338_leafcheck"        python3 tools/mrb338_leafcheck.py "${LEAF_ARGS[@]}"

echo
echo "── the leaf checker's own output (it is an advisor; read its notes) ──"
sed 's/^/   │ /' "$OUT/mrb338_leafcheck.log"

echo
echo "════════════════════════════════════════════════════════════════════════"
echo "mrb338_land: ✅ all ${#NAMES[@]} gates green."
echo
echo '⚠️  GREEN IS NOT A COMMIT. This script does not commit, on purpose —'
echo '    night 1 chained the check to `git add` and the commit ran while the'
echo '    check printed red (REPORT §10, deviation 6). Read the leaf checker'"'"'s'
echo '    notes above, then commit yourself:'
echo
if [ ${#PATHSPEC[@]} -gt 0 ]; then
  echo "      git add ${PATHSPEC[*]}"
  echo "      git commit -m '...'"
else
  echo "      git add <only your own files — this worktree is shared>"
  echo "      git commit -m '...'"
fi
echo
echo "    ⚠️  Name your files. Other lanes' uncommitted work is in this"
echo "        worktree; \`git commit -a\` would take it."
echo "════════════════════════════════════════════════════════════════════════"
