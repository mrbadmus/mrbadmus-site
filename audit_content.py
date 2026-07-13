#!/usr/bin/env python3
"""
Phase 1 content audit — checks the generator's source data
(all_subtopics_*.py) against docs/redesign/content_standards.md.

Audit only: reads the 12 variant data files, writes a defect table to
docs/audit/. Never modifies content. Re-run after content fixes
(Phase 2c definition of done: zero critical/major on fixed pages).

Outputs:
  docs/audit/phase1_defects.csv    — one row per defect, worst pages first
  docs/audit/phase1_page_stats.csv — one row per page-variant (counts, fingerprint)
  docs/audit/phase1_summary.md     — counts by rule/severity, lineup clusters
  docs/audit/extracts/<subject>_<pathway>.json — compact quiz/mistake/FIFA
      extracts for the AI judgement pass (distractors, register, tier integrity)
"""
import csv
import importlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
OUT_DIR = os.path.join(ROOT, "docs", "audit")
EXTRACT_DIR = os.path.join(OUT_DIR, "extracts")

SUBJECTS = ["physics", "chemistry", "biology"]
VARIANTS = [
    ("combined", "foundation", "all_subtopics_{s}"),
    ("combined", "higher", "all_subtopics_{s}_higher"),
    ("triple", "foundation", "all_subtopics_{s}_triple_foundation"),
    ("triple", "higher", "all_subtopics_{s}_triple_higher"),
]
DATA_VAR = {
    "physics": "PHYSICS_SUBTOPICS_ALL",
    "chemistry": "CHEMISTRY_SUBTOPICS_ALL",
    "biology": "BIOLOGY_SUBTOPICS_ALL",
}

OPTIONAL_BLOCKS = ["variables", "equations", "key_note", "common_mistake",
                   "higher", "triple_only", "rp", "matching", "fifas", "quiz"]

COMMAND_WORDS = re.compile(
    r"\b(state|describe|explain|compare|calculate|predict|evaluate|suggest|"
    r"estimate|determine|work out|deduce|justify|plot|sketch|measure)\b", re.I)

# First-sentence patterns that indicate the block opens with the MISTAKE
# (a student action/belief) rather than with correct information.
MISTAKE_FIRST = [
    re.compile(r"\b(students?|pupils?|candidates?|people|everyone|many|some)\b[^.!?]*\b"
               r"(say|says|write|writes|think|thinks|confus\w*|forget\w*|mix\w*|assume\w*|"
               r"believe\w*|use\w*|call\w*|treat\w*|swap\w*|state\w*|connect\w*|draw\w*|"
               r"pick\w*|label\w*|add\w*|drop\w*|lose\w*|divid\w*|multipl\w*|subtract\w*|"
               r"round\w*|copy\w*|answer\w*|leave\w*|miss\w*|skip\w*|put\w*|get\w*)\b", re.I),
    re.compile(r"^\s*(don'?t|never|do not|avoid|stop)\b", re.I),
    re.compile(r"^\s*(a\s+)?(common|classic|frequent)\s+(error|mistake|misconception|slip)", re.I),
    re.compile(r"^\s*(it'?s\s+(easy|tempting)|easy to|tempting to)", re.I),
    re.compile(r"^\s*(mixing up|confusing|forgetting|writing|saying|thinking|using|"
               r"calling|swapping|muddling|assuming|treating)\b", re.I),
    re.compile(r"\bwrong(ly)?\b.*\b(answer|because|if you|when you)\b", re.I),
]

NUM_RE = re.compile(r"\d+(?:\.\d+)?")


def length_tell(opts):
    """Rule 1 (length parity) heuristic. Flag an MCQ where the CORRECT option
    is a length tell: strictly the longest option AND longer than the longest
    distractor by >=4 words OR by >=1.4x. Either sub-condition catches a tell
    (a big absolute gap on long options, or a big proportional gap on short
    ones), so a student can score by picking the longest line without reading.
    Returns (correct_wc, max_distractor_wc) if flagged, else None."""
    if not opts or len(opts) < 3:
        return None
    ci = next((j for j, o in enumerate(opts) if o[1]), None)
    if ci is None:
        return None
    wc = [len(str(o[0]).split()) for o in opts]
    cwc = wc[ci]
    dwc = [wc[j] for j in range(len(opts)) if j != ci]
    maxd = max(dwc)
    if cwc == max(wc) and cwc > maxd and ((cwc - maxd) >= 4 or cwc >= 1.4 * maxd):
        return (cwc, maxd)
    return None


def first_sentence(text):
    text = text.strip()
    m = re.search(r"(?<=[.!?])\s", text)
    return text[:m.start()] if m else text


def mistake_first(text):
    fs = first_sentence(text)
    return any(p.search(fs) for p in MISTAKE_FIRST), fs


def fifa_text(fifas):
    parts = []
    for f in fifas or []:
        parts.append(str(f.get("question", "")))
        for step in f.get("steps", []):
            parts.append(str(step[1] if len(step) > 1 else step))
    return " ".join(parts)


def load_all():
    """-> data[(subject, pathway, tier)] = {topic_id: [subtopic, ...]}"""
    data = {}
    for s in SUBJECTS:
        for pathway, tier, mod_tpl in VARIANTS:
            mod = importlib.import_module(mod_tpl.format(s=s))
            data[(s, pathway, tier)] = getattr(mod, DATA_VAR[s])
    return data


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(EXTRACT_DIR, exist_ok=True)
    data = load_all()

    defects = []   # dicts: page, subject, pathway, tier, block, rule, severity, evidence
    stats = []     # per page-variant stats
    fingerprints = defaultdict(list)

    def add(subject, pathway, tier, topic, st_id, block, rule, severity, evidence):
        defects.append({
            "page": f"{subject}/{topic}/{st_id}",
            "subject": subject, "pathway": pathway, "tier": tier,
            "block": block, "rule": rule, "severity": severity,
            "evidence": evidence,
        })

    # ---- per-variant mechanical checks ----
    for (subject, pathway, tier), topics in sorted(data.items()):
        for topic, sts in topics.items():
            for st in sts:
                st_id = st.get("id", "?")
                quiz = st.get("quiz") or []
                fifas = st.get("fifas") or []

                # Rule 1 — Test Yourself counts
                n = len(quiz)
                if n < 5:
                    add(subject, pathway, tier, topic, st_id, "quiz", "1-count",
                        "critical", f"{n} questions — below absolute floor of 5")
                elif n < 10:
                    add(subject, pathway, tier, topic, st_id, "quiz", "1-count",
                        "major", f"{n} questions — below target 10 "
                        f"(6-7 acceptable only if page is 'genuinely light')")

                # Rule 1 — command-word register (mechanical proxy; AI pass refines)
                if quiz:
                    with_cw = sum(1 for q in quiz if COMMAND_WORDS.search(str(q.get("q", ""))))
                    if with_cw == 0:
                        add(subject, pathway, tier, topic, st_id, "quiz", "1-register",
                            "minor", f"0/{n} stems use an AQA command word (AI review)")

                # Rule 1 — length parity (correct option is a length tell)
                for qi, q in enumerate(quiz, 1):
                    lt = length_tell(q.get("opts"))
                    if lt:
                        add(subject, pathway, tier, topic, st_id, "quiz",
                            "1-length-parity", "minor",
                            f"Q{qi}: correct option is longest ({lt[0]}w vs "
                            f"longest distractor {lt[1]}w) — length tell, "
                            f"rewrite for parity")

                # Rule 2 — FIFA
                if fifas:
                    if len(fifas) < 3:
                        add(subject, pathway, tier, topic, st_id, "fifa", "2-example-count",
                            "major", f"{len(fifas)} worked example(s) — minimum 3")
                    add(subject, pathway, tier, topic, st_id, "fifa", "2-practice-absent",
                        "major", "no interactive practice mode "
                        "(systemic: current template renders static steps only)")
                elif st.get("equations"):
                    add(subject, pathway, tier, topic, st_id, "fifa", "4-menu",
                        "info", "page has equations but no FIFA block — "
                        "deliberate-choice check when unit is ported")

                # Rule 3 — Common Mistake first-sentence pattern
                cm = st.get("common_mistake")
                if cm:
                    ok, fs = mistake_first(cm)
                    if not ok:
                        add(subject, pathway, tier, topic, st_id, "common_mistake",
                            "3-mistake-first", "major",
                            f"first sentence states info, not a student mistake "
                            f"(AI review): \"{fs[:90]}\"")

                # Rule 8 — Examiner Tip coverage (info: tracks rollout, not a
                # defect). One Examiner Tip per page is the standard (§8), but
                # during rollout a missing tip is reported info-only — weight 0,
                # so it never inflates a page's severity score or drowns defects.
                if not st.get("examiner_tip"):
                    add(subject, pathway, tier, topic, st_id, "examiner_tip",
                        "8-examiner-tip", "info",
                        "no Examiner Tip — one per page is the standard (rollout coverage)")

                # Rule 4 — lineup fingerprint
                fp = "".join("1" if st.get(k) else "0" for k in OPTIONAL_BLOCKS)
                fingerprints[fp].append(f"{subject}/{pathway}/{tier}/{topic}/{st_id}")

                stats.append({
                    "page": f"{subject}/{topic}/{st_id}",
                    "subject": subject, "pathway": pathway, "tier": tier,
                    "quiz_count": n, "fifa_count": len(fifas),
                    "has_common_mistake": bool(cm), "has_matching": bool(st.get("matching")),
                    "has_equations": bool(st.get("equations")), "has_rp": bool(st.get("rp")),
                    "has_examiner_tip": bool(st.get("examiner_tip")),
                    "lineup": fp,
                })

    # ---- cross-variant checks (rule 2 duplication, rule 5 tier integrity) ----
    def by_key(subject, pathway, tier):
        out = {}
        for topic, sts in data[(subject, pathway, tier)].items():
            for st in sts:
                out[(topic, st.get("id"))] = st
        return out

    for subject in SUBJECTS:
        for pathway in ["combined", "triple"]:
            fnd = by_key(subject, pathway, "foundation")
            hgh = by_key(subject, pathway, "higher")
            for key, h_st in hgh.items():
                f_st = fnd.get(key)
                if not f_st:
                    continue
                topic, st_id = key
                h_fifa, f_fifa = h_st.get("fifas") or [], f_st.get("fifas") or []
                if h_fifa and f_fifa:
                    if h_fifa == f_fifa:
                        add(subject, pathway, "higher", topic, st_id, "fifa",
                            "2-tier-duplication", "major",
                            "FIFA block identical to Foundation variant — fake differentiation")
                    else:
                        h_nums = Counter(NUM_RE.findall(fifa_text(h_fifa)))
                        f_nums = Counter(NUM_RE.findall(fifa_text(f_fifa)))
                        if h_nums == f_nums and sum(h_nums.values()) > 0:
                            add(subject, pathway, "higher", topic, st_id, "fifa",
                                "2-tier-duplication", "major",
                                "FIFA example values identical to Foundation — fake differentiation")
                if h_st.get("quiz") and h_st.get("quiz") == f_st.get("quiz"):
                    add(subject, pathway, "higher", topic, st_id, "quiz",
                        "5-tier-integrity", "major",
                        "Test Yourself identical to Foundation variant — same page, harder badge")

        # Triple depth: triple variant identical to combined variant of same tier
        for tier in ["foundation", "higher"]:
            comb = by_key(subject, "combined", tier)
            trip = by_key(subject, "triple", tier)
            for key, t_st in trip.items():
                c_st = comb.get(key)
                if not c_st:
                    continue
                topic, st_id = key
                if t_st.get("quiz") and t_st.get("quiz") == c_st.get("quiz"):
                    add(subject, "triple", tier, topic, st_id, "quiz",
                        "1-triple-depth", "major",
                        f"Test Yourself identical to Combined {tier} — "
                        "no Triple-only depth questions (rule 1 asks for ≥2)")

    # ---- lineup clusters (rule 4, informational) ----
    clusters = sorted(((fp, pages) for fp, pages in fingerprints.items() if len(pages) >= 15),
                      key=lambda x: -len(x[1]))

    # ---- worst-first ordering ----
    sev_w = {"critical": 10, "major": 3, "minor": 1, "info": 0}
    page_score = defaultdict(int)
    for d in defects:
        k = (d["page"], d["pathway"], d["tier"])
        page_score[k] += sev_w[d["severity"]]
    tier_w = {"higher": 1, "foundation": 0}

    def sort_key(d):
        k = (d["page"], d["pathway"], d["tier"])
        return (-page_score[k],
                -(tier_w[d["tier"]] + (1 if d["pathway"] == "triple" else 0)),
                d["page"], -sev_w[d["severity"]])

    defects.sort(key=sort_key)

    # ---- write outputs ----
    cols = ["page", "subject", "pathway", "tier", "block", "rule", "severity", "evidence"]
    with open(os.path.join(OUT_DIR, "phase1_defects.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(defects)

    with open(os.path.join(OUT_DIR, "phase1_page_stats.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(stats[0].keys()))
        w.writeheader()
        w.writerows(stats)

    # extracts for the AI judgement pass
    for subject in SUBJECTS:
        for pathway in ["combined", "triple"]:
            extract = {}
            for tier in ["foundation", "higher"]:
                for topic, sts in data[(subject, pathway, tier)].items():
                    for st in sts:
                        node = extract.setdefault(f"{topic}/{st.get('id')}", {
                            "summary": st.get("summary", ""), "tiers": {}})
                        node["tiers"][tier] = {
                            "quiz": [{"q": q.get("q"),
                                      "opts": [(o[0], o[1]) for o in q.get("opts", [])],
                                      "wrong_explanations": q.get("wrong_explanations", {})}
                                     for q in st.get("quiz") or []],
                            "common_mistake": st.get("common_mistake"),
                            "fifas": [{"label": f.get("label"), "question": f.get("question"),
                                       "steps": f.get("steps")}
                                      for f in st.get("fifas") or []],
                            "higher_box": st.get("higher"),
                            "triple_box": st.get("triple_only"),
                        }
            path = os.path.join(EXTRACT_DIR, f"{subject}_{pathway}.json")
            with open(path, "w") as f:
                json.dump(extract, f, indent=1, ensure_ascii=False)

    # summary markdown
    by_rule = Counter((d["rule"], d["severity"]) for d in defects)
    by_sev = Counter(d["severity"] for d in defects)
    n_pages = len(stats)
    n_unique = len({s["page"] for s in stats})
    worst = sorted({(d["page"], d["pathway"], d["tier"]): page_score[(d["page"], d["pathway"], d["tier"])]
                    for d in defects}.items(), key=lambda x: -x[1])[:25]

    lines = [
        "# Phase 1 content audit — summary",
        "",
        f"Source: the 12 `all_subtopics_*.py` files (audited at source, not generated HTML).",
        f"Coverage: **{n_unique} unique subtopic pages**, **{n_pages} page-variants** "
        f"(subject × pathway × tier).",
        "",
        "## Defects by severity",
        "",
        "| severity | count |", "|---|---|",
    ]
    for sev in ["critical", "major", "minor", "info"]:
        lines.append(f"| {sev} | {by_sev.get(sev, 0)} |")
    lines += ["", "## Defects by rule", "", "| rule | severity | count |", "|---|---|---|"]
    for (rule, sev), c in sorted(by_rule.items()):
        lines.append(f"| {rule} | {sev} | {c} |")
    lines += ["", "## Worst 25 page-variants (by severity score)", "",
              "| page | pathway | tier | score |", "|---|---|---|---|"]
    for (page, pathway, tier), score in worst:
        lines.append(f"| {page} | {pathway} | {tier} | {score} |")
    lines += ["", "## Lineup fingerprint clusters (rule 4, informational)", "",
              "Optional-block lineups shared by ≥15 page-variants — check the lineup is a "
              "coincidence of need, not a default. Key: " + ", ".join(OPTIONAL_BLOCKS), ""]
    for fp, pages in clusters:
        lines.append(f"- `{fp}` × {len(pages)} (e.g. {pages[0]})")
    with open(os.path.join(OUT_DIR, "phase1_summary.md"), "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"pages: {n_unique} unique, {n_pages} variants")
    print(f"defects: {dict(by_sev)}")
    print(f"wrote {OUT_DIR}/phase1_defects.csv, phase1_page_stats.csv, phase1_summary.md")
    print(f"extracts for AI pass: {EXTRACT_DIR}/")


if __name__ == "__main__":
    main()
