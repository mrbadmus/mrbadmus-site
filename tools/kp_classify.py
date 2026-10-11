#!/usr/bin/env python3
"""kp_classify.py — draft the knowledge points, and tag every question with one.

    python3 tools/kp_classify.py --cache DIR                 # classify all, resume from cache
    python3 tools/kp_classify.py --cache DIR --scope enzymes --force   # redo ONE scope
    python3 tools/kp_classify.py --cache DIR --assemble-only # rebuild the JSON from cache, no calls
    python3 tools/kp_classify.py --inventory                 # count what would be classified

── WHAT THIS IS (parent truth, 11 Oct 2026) ────────────────────────────

A KNOWLEDGE POINT is one fact, idea or skill a pupil must know or be able to
do, written as a short plain-English statement a parent can read. Every
question on the site is tagged with exactly one, so "a different question
testing the same point" can be found, and a parent can be shown which points
their child has and has not got yet.

Nothing like this existed before: no question in either bank carried a topic
tag finer than its lesson. So the points and the tags are DRAFTED BY A MODEL
from each scope's own authored teaching content and questions, and kept as
reviewable data in `knowledge_points/*.json`. They await Mide's examiner
review; `knowledge_points/README.md` says how to change them.

── SCOPES ──────────────────────────────────────────────────────────────

One model call per scope, and a scope's questions are classified TOGETHER so
the points are drawn from what the questions actually test:

  KS3 lesson (185)   — bank rows (`b1-04-s01`), the four ladder rungs
                       (`<slug>#recall|apply|explain|produce`). The exam twins
                       of the written rungs (`ks3-<unit>-<slug>-explain|produce`)
                       are NOT sent: they are the same question, so they take
                       their rung's point.
  KS4 subtopic (264) — bank rows (`ks4-<subtopic>-e01`), every classic
                       lesson-page quiz card (`ks4q:<subtopic>:<h>`, see
                       `ks4_quiz_id`), and, for the 85 rebuilt lessons, the
                       four Ks4Ladder rungs (`ks4:<slug>#r1..r4`). A rebuilt
                       lesson's slug IS its subtopic id (`ks4_lessons.
                       verify_slugs()` proves it; `inventory()` re-asserts it).

Then a second, small pass over the KS4 exam_questions rows (bonding_v2 and the
code seed): each is shown the points of its own subtopic (bonding_v2 — the
exam-content file is named for it) or of every subtopic in its AQA topic
(code seed), and picks one, or none. None means untagged, never a guess.

── MODEL ACCESS ────────────────────────────────────────────────────────

The Anthropic key is read from the backend's .env INTO MEMORY ONLY. It is
never printed, logged, written, or put on a command line.
"""

import argparse
import concurrent.futures as cf
import glob
import hashlib
import html
import importlib
import json
import os
import re
import ssl
import sys
import threading
import time
import unicodedata
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

BACKEND_ENV = "/Users/midebadmus/Documents/GitHub/mrbadmus---backend/.env"
MODEL = "claude-sonnet-4-6"          # the backend's model
KP_DIR = os.path.join(REPO, "knowledge_points")
RUNGS_KS3 = ("recall", "apply", "explain", "produce")
SUBJECT_OF_UNIT = {"B": "biology", "C": "chemistry", "P": "physics"}

# The contract's test vector (docs: CONTRACT.md "Stable question IDs").
# The backend's ks4QuizId must produce exactly this.
TEST_VECTOR_ARGS = ("scalar-vector-quantities",
                    "1. A runner completes one full lap of a 400 m circular "
                    "track. What is the runner's distance and displacement?")
TEST_VECTOR_ID = "ks4q:scalar-vector-quantities:3616a6034c"


# ── the classic quiz card id ────────────────────────────────────────────

def ks4_quiz_norm(text):
    """NFKC → strip a leading card number ("1. " / "1) ") → collapse every
    whitespace run to one space → trim → lowercase. In that order."""
    t = unicodedata.normalize("NFKC", text)
    t = re.sub(r"^\s*\d+[.)]\s*", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t.lower()


def ks4_quiz_id(slug, text):
    """`ks4q:<subtopic-slug>:<first 10 hex of sha1(normalised text)>`.

    `text` is the card's `.q-text` textContent (HTML-unescaped, tags
    stripped). Identical to the backend's `ks4QuizId(slug, text)`."""
    h = hashlib.sha1(ks4_quiz_norm(text).encode("utf-8")).hexdigest()[:10]
    return "ks4q:%s:%s" % (slug, h)


# ── text helpers ────────────────────────────────────────────────────────

_TAG = re.compile(r"<[^>]+>")


def plain(s):
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    return re.sub(r"\s+", " ", html.unescape(_TAG.sub("", s))).strip()


def clip(s, n):
    s = plain(s)
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


# ── the KS4 subtopic records ────────────────────────────────────────────

def ks4_subtopics():
    """subtopic id → {subject, topic_id, record}. A subtopic appears in up to
    twelve tier/pathway files with growing content; the richest record (the
    longest serialisation) is the one used for teaching content. Every quiz
    card across ALL of its records is collected, because each tier's page
    shows its own file's cards."""
    out = {}
    for f in sorted(glob.glob(os.path.join(REPO, "all_subtopics_*.py"))):
        name = os.path.basename(f)[:-3]
        subject = name.split("_")[2]
        mod = importlib.import_module(name)
        d = [v for k, v in vars(mod).items() if k.endswith("_SUBTOPICS_ALL")][0]
        for topic_id, lst in d.items():
            for s in lst:
                e = out.setdefault(s["id"], {"subject": subject,
                                             "topic_id": topic_id,
                                             "record": s, "quiz": {}})
                if (e["subject"], e["topic_id"]) != (subject, topic_id):
                    raise SystemExit("kp: subtopic %r is in two topics" % s["id"])
                if len(json.dumps(s, default=str)) > len(json.dumps(e["record"], default=str)):
                    e["record"] = s
                for q in s.get("quiz") or []:
                    # The page numbers its cards ("1. …") and the id is taken
                    # from the PAGE text, whose leading number the normaliser
                    # strips. Hash the authored stem the same way — numbered —
                    # or a stem that itself opens with a number ("4.8 g of
                    # magnesium…") would lose "4." to the normaliser here and
                    # not on the page. Any card number gives the same id.
                    qid = ks4_quiz_id(s["id"], "1. " + plain(q["q"]))
                    if qid not in e["quiz"]:
                        correct = [t for t, ok in q.get("opts") or [] if ok]
                        e["quiz"][qid] = (plain(q["q"]), plain(correct[0]) if correct else "")
    return out


# ── the KS4 rebuilt-lesson ladder rungs ─────────────────────────────────

_JS_STR = r"'((?:[^'\\]|\\.)*)'"


def _lesson_source(L):
    import ks4_lessons as K
    if L["batch"] == "pilot":
        return os.path.join(REPO, K.DESIGN_DIR, L["design_file"])
    return os.path.join(REPO, K.authored_dir(L["batch"]), L["source_file"])


def ks4_rungs():
    """slug → {r1..r4: text}. The rungs are JavaScript inside Design's
    `.dc.html` (often one variant per route), so this reads the prompt /
    question strings — and the stem prefix a `K.find()` rung looks its quiz
    card up by — from each rung's own stretch of source. Every variant's text
    is kept, joined; they test the same point by construction."""
    import ks4_lessons as K
    out = {}
    for L in K.all_lessons():
        src = open(_lesson_source(L), encoding="utf-8").read()
        # `const rungs =` or `rungs:` in the script — never the HTML
        # attribute `rungs="{{ rungs }}"` on the dc-import tag.
        m = re.search(r"(?:\bconst\s+rungs\s*=|\brungs\s*:)", src)
        start = m.start() if m else src.find("r1:")
        region = src[start:start + 40000]
        rungs = {}
        for n in (1, 2, 3, 4):
            texts = []
            for mm in re.finditer(r"\br%d\b\s*[:=,]" % n, region):
                nxt = re.search(r"\br%d\b\s*[:=,]" % (n + 1), region[mm.end():]) if n < 4 else None
                win = region[mm.end(): mm.end() + (nxt.start() if nxt else 3000)][:3000]
                for k in re.finditer(r"\b(?:prompt|question)\s*:\s*" + _JS_STR, win):
                    texts.append(k.group(1))
                for k in re.finditer(r"K\.find\([^,]+,[^,]+,\s*" + _JS_STR, win):
                    texts.append(k.group(1) + "…")
            if not texts:
                # `rN: R.isHigher ? rungTH : rungTF` — the rung objects are
                # consts declared earlier; read each named one.
                for mm in re.finditer(r"\br%d\b\s*:\s*([^,\n]{0,160})" % n, region):
                    for ident in re.findall(r"\b([A-Za-z_]\w*)\b", mm.group(1)):
                        d = re.search(r"\bconst\s+%s\s*=" % re.escape(ident), src)
                        if d:
                            for k in re.finditer(r"\b(?:prompt|question)\s*:\s*" + _JS_STR,
                                                 src[d.end(): d.end() + 3000][:3000]):
                                texts.append(k.group(1))
                                break
            if n == 1 and not texts:
                # r1 built ahead of the object literal (microscopy): read the
                # K.find stem prefix and the fallback prompt before `return {`.
                for k in re.finditer(r"K\.find\([^,]+,[^,]+,\s*" + _JS_STR, region[:4000]):
                    texts.append(k.group(1) + "…")
            seen, uniq = set(), []
            for t in texts:
                t = re.sub(r"\\u([0-9a-fA-F]{4})", lambda u: chr(int(u.group(1), 16)), t)
                t = plain(t.replace("\\'", "'"))
                if t and t not in seen:
                    seen.add(t)
                    uniq.append(t)
            rungs["r%d" % n] = " / ".join(uniq) or "(ladder rung %d)" % n
        out[L["slug"]] = rungs
    return out


# ── the inventory: every question, by scope ─────────────────────────────

def inventory():
    """{'KS3': {slug: scope}, 'KS4': {subtopic: scope}, 'exam_ks3': [...],
    'exam_ks4_ids': set} — scope = {scope_ref, key_stage, subject, title,
    content, questions: [(qid, source, stem, correct)]}."""
    import ks3_data
    from ks3_data import question_bank as qb
    import ks4_data
    import export_ks3_extended

    reg = ks3_data.lesson_registry()
    bank = {r["lesson"]: r for r in qb.load_bank()}
    ks3 = {}
    for slug, L in reg.items():
        unit = L["_unit"]
        lad = L.get("ladder") or {}
        content = ["Lesson: %s (unit %s)" % (plain(L["title"]), unit)]
        if L.get("big_question"):
            content.append("Big question: " + plain(L["big_question"]))
        for kf in L.get("key_facts") or []:
            content.append("Key fact: " + clip(kf.get("text"), 400))
        for mc in L.get("misconceptions") or []:
            content.append("Misconception to fix: " + clip(mc.get("statement"), 300))
        for v in L.get("vocabulary") or []:
            content.append("Term: %s — %s" % (plain(v.get("term")), clip(v.get("definition"), 200)))
        qs = []
        for q in (bank.get(slug) or {}).get("questions", []):
            corr = [o["text"] for o in q["options"] if o.get("correct")]
            qs.append((q["id"], "ks3_bank", plain(q["text"]), plain(corr[0]) if corr else ""))
        for rung in RUNGS_KS3:
            r = lad.get(rung)
            if not r:
                continue
            if r.get("options"):
                ans = r["options"][r["answer"]] if isinstance(r.get("answer"), int) else ""
                qs.append(("%s#%s" % (slug, rung), "ks3_ladder", plain(r["q"]), plain(ans)))
            else:
                crit = "; ".join(plain(s) for s in r.get("success") or [])
                qs.append(("%s#%s" % (slug, rung), "ks3_ladder", plain(r["q"]),
                           "(written answer; marking points: %s)" % clip(crit, 600)))
        ks3[slug] = {"scope_ref": slug, "key_stage": "KS3",
                     "subject": SUBJECT_OF_UNIT[unit[0]], "unit": unit,
                     "title": plain(L["title"]), "content": "\n".join(content),
                     "questions": qs}
    if set(bank) - set(reg):
        raise SystemExit("kp: bank lessons with no registry entry: %s" % sorted(set(bank) - set(reg)))

    exam_ks3 = []
    for r in export_ks3_extended.rows():
        slug = r["id"][len("ks3-%s-" % r["unit_code"].lower()):].rsplit("-", 1)[0]
        rung = r["id"].rsplit("-", 1)[1]
        if slug not in ks3 or "%s#%s" % (slug, rung) not in {q[0] for q in ks3[slug]["questions"]}:
            raise SystemExit("kp: exam twin %s has no rung" % r["id"])
        exam_ks3.append((r["id"], "%s#%s" % (slug, rung), slug))

    subs = ks4_subtopics()
    pool = {}
    for q in ks4_data.load_pool():
        pool.setdefault(q["subtopic_slug"], []).append(q)
    rungs = ks4_rungs()
    stray = set(rungs) - set(subs)
    if stray:
        raise SystemExit("kp: rebuilt lessons whose slug is not a subtopic id: %s" % sorted(stray))
    ks4 = {}
    for sid, e in subs.items():
        s = e["record"]
        content = ["Subtopic: %s (AQA %s, topic %s)" % (plain(s.get("title")), plain(s.get("spec")), e["topic_id"])]
        if s.get("summary"):
            content.append("Summary: " + clip(s["summary"], 800))
        budget = 3500
        for th in s.get("theory") or []:
            line = "Theory — %s: %s" % (plain(th.get("heading")), clip(th.get("content"), 600))
            if budget - len(line) < 0:
                content.append("Theory — %s" % plain(th.get("heading")))
                continue
            budget -= len(line)
            content.append(line)
        if s.get("key_note"):
            content.append("Key note: " + clip(s["key_note"], 600))
        if s.get("common_mistake"):
            content.append("Common mistake: " + clip(s["common_mistake"], 600))
        qs = []
        for q in sorted(pool.get(sid, []), key=lambda r: r["id"]):
            qs.append((q["id"], "ks4_bank", plain(q["text"]), plain(q["options"][q["correct_index"]])))
        for qid in sorted(e["quiz"]):
            stem, corr = e["quiz"][qid]
            qs.append((qid, "ks4_quiz", stem, corr))
        for n in (1, 2, 3, 4):
            if sid in rungs:
                qs.append(("ks4:%s#r%d" % (sid, n), "ks4_rung",
                           "(lesson ladder rung %d) %s" % (n, rungs[sid]["r%d" % n]), ""))
        ks4[sid] = {"scope_ref": sid, "key_stage": "KS4", "subject": e["subject"],
                    "topic_id": e["topic_id"], "title": plain(s.get("title")),
                    "content": "\n".join(content), "questions": qs}
    return {"KS3": ks3, "KS4": ks4, "exam_ks3": exam_ks3}


# Source label as the DB stores it (question_knowledge_points.source).
DB_SOURCE = {"ks3_bank": "ks3_bank", "ks3_ladder": "ks3_ladder", "ks4_bank": "ks4_bank",
             "ks4_quiz": "ks4_lesson", "ks4_rung": "ks4_lesson", "exam": "exam"}


def source_of(qid):
    """Inventory source of a question id, read off its shape."""
    if qid.startswith("ks4q:"):
        return "ks4_quiz"
    if qid.startswith("ks4:"):
        return "ks4_rung"
    if qid.startswith("ks4-"):
        return "ks4_bank"
    if qid.startswith(("ks3-", "bv2-", "cs-")):
        return "exam"
    if "#" in qid:
        return "ks3_ladder"
    return "ks3_bank"


# ── the model ───────────────────────────────────────────────────────────

_KEY = None
_KEY_LOCK = threading.Lock()
USAGE = {"input_tokens": 0, "output_tokens": 0, "calls": 0}
_USAGE_LOCK = threading.Lock()


def _api_key():
    global _KEY
    with _KEY_LOCK:
        if _KEY is None:
            with open(BACKEND_ENV, encoding="utf-8") as fh:
                for line in fh:
                    if line.startswith("ANTHROPIC_API_KEY="):
                        _KEY = line.split("=", 1)[1].strip().strip('"').strip("'")
            if not _KEY:
                raise SystemExit("kp: ANTHROPIC_API_KEY is not set in the backend .env")
        return _KEY


def call_model(prompt, max_tokens=4000):
    body = json.dumps({"model": MODEL, "max_tokens": max_tokens, "temperature": 0,
                       "messages": [{"role": "user", "content": prompt}]}).encode("utf-8")
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    delay = 5
    for attempt in range(6):
        rq = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, method="POST")
        rq.add_header("x-api-key", _api_key())
        rq.add_header("anthropic-version", "2023-06-01")
        rq.add_header("content-type", "application/json")
        try:
            with urllib.request.urlopen(rq, context=ctx, timeout=180) as r:
                out = json.load(r)
            u = out.get("usage") or {}
            with _USAGE_LOCK:
                USAGE["input_tokens"] += u.get("input_tokens", 0)
                USAGE["output_tokens"] += u.get("output_tokens", 0)
                USAGE["calls"] += 1
            text = "".join(b.get("text", "") for b in out.get("content", []) if b.get("type") == "text")
            return text, u
        except urllib.error.HTTPError as e:
            code = e.code
            e.read()
            if code in (429, 500, 502, 503, 504, 529) and attempt < 5:
                time.sleep(delay)
                delay = min(delay * 2, 60)
                continue
            raise RuntimeError("model HTTP %s" % code)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            if attempt < 5:
                time.sleep(delay)
                delay = min(delay * 2, 60)
                continue
            raise RuntimeError("model unreachable: %s" % type(e).__name__)
    raise RuntimeError("model: retries exhausted")


def extract_json(text):
    """The first complete JSON object in the reply (code fences and any
    trailing commentary ignored)."""
    i = text.find("{")
    if i < 0:
        raise ValueError("no JSON object in the reply")
    obj, _end = json.JSONDecoder().raw_decode(text[i:])
    return obj


# ── pass 1: one scope ───────────────────────────────────────────────────

def scope_prompt(scope, error=None):
    ks3 = scope["key_stage"] == "KS3"
    kind = "Key Stage 3 science lesson" if ks3 else "GCSE (AQA) science subtopic"
    lines = []
    for i, (_qid, _src, stem, corr) in enumerate(scope["questions"], 1):
        lines.append("%d. %s → %s" % (i, clip(stem, 500), clip(corr, 300) if corr else "(see stem)"))
    n = len(scope["questions"])
    p = """You are an experienced UK science teacher and examiner. You are drafting KNOWLEDGE POINTS for one %s on a revision website. A knowledge point is one fact, idea or skill a pupil must know or be able to do. Parents will read the labels to see which points their child has secured and which not yet.

TEACHING CONTENT
%s

QUESTIONS (number. question → correct answer)
%s

TASK
1. Write between 4 and 10 knowledge points for this %s.
   - Each label is a short plain-English statement of the fact, idea or skill itself, at most 15 words, written so a parent can follow it (for example "Enzymes stop working when heat changes the shape of the active site" or "Calculate speed from distance and time"). Do not start with "The pupil", "Students" or "Understand".
   - Specific enough that two questions with the same point really test the same thing; broad enough that most points cover at least 3 of the questions.
   - Only use science present in the teaching content and questions above. Do not add anything else.
2. Then go through the questions IN ORDER, 1 to %d, and give each one the number of the ONE point it mainly tests. Every question number must appear exactly once.

Reply with JSON only, no commentary, in exactly this shape:
{"points": [{"n": 1, "label": "..."}, {"n": 2, "label": "..."}],
 "assign": {"1": <point n>, "2": <point n>, ..., "%d": <point n>}}""" % (
        kind, scope["content"], "\n".join(lines), "lesson" if ks3 else "subtopic", n, n)
    if error:
        p += "\n\nYour previous reply was rejected: %s. Reply again, correctly." % error
    return p


def validate_points(obj):
    pts = obj.get("points") if isinstance(obj, dict) else None
    if not isinstance(pts, list):
        raise ValueError("no 'points' list")
    if not 3 <= len(pts) <= 12:
        raise ValueError("%d points; need between 4 and 10" % len(pts))
    labels = []
    for k, p in enumerate(pts, 1):
        lab = p.get("label") if isinstance(p, dict) else None
        if not isinstance(lab, str) or not 3 <= len(lab.strip()) <= 120:
            raise ValueError("point %d's label is %d characters; every label must be at most 15 "
                             "words and under 120 characters — state the point, do not list "
                             "examples" % (k, len(lab.strip()) if isinstance(lab, str) else 0))
        if isinstance(p, dict) and p.get("n") not in (None, k):
            raise ValueError("points must be numbered 1, 2, 3… in order")
        labels.append(re.sub(r"\s+", " ", lab).strip())
    return labels


def read_assign(obj, n, npts):
    """{question number: point number} from the reply's `assign`, plus the
    numbers that are missing. Raises on a number that does not exist."""
    raw = obj.get("assign") if isinstance(obj, dict) else None
    if not isinstance(raw, dict):
        raise ValueError("no 'assign' object")
    got = {}
    for k, v in raw.items():
        try:
            q = int(k)
        except (TypeError, ValueError):
            raise ValueError("assign key %r is not a question number" % k)
        if not 1 <= q <= n:
            raise ValueError("question number %d does not exist (1-%d)" % (q, n))
        if not isinstance(v, int) or not 1 <= v <= npts:
            raise ValueError("question %d is given point %r; points are 1-%d" % (q, v, npts))
        got[q] = v
    return got, [i for i in range(1, n + 1) if i not in got]


def to_points(labels, assign):
    pts = [{"label": lab, "questions": []} for lab in labels]
    for q in sorted(assign):
        pts[assign[q] - 1]["questions"].append(q)
    empty = [i + 1 for i, p in enumerate(pts) if not p["questions"]]
    if empty:
        raise ValueError("point(s) %s have no questions; drop them or give them questions"
                         % ", ".join(map(str, empty)))
    return pts


def scope_hash(scope):
    h = hashlib.sha256()
    h.update(scope["content"].encode("utf-8"))
    for q in scope["questions"]:
        h.update(("\x00" + "\x01".join(q)).encode("utf-8"))
    return h.hexdigest()[:16]


def cache_path(cache, ks, ref):
    return os.path.join(cache, "%s__%s.json" % (ks.lower(), ref))


def repair_missing(scope, labels, assign, missing, attempts):
    listing = "\n".join("%d. %s" % (i, lab) for i, lab in enumerate(labels, 1))
    qs = "\n".join("%d. %s → %s" % (k, clip(scope["questions"][k - 1][2], 500),
                                     clip(scope["questions"][k - 1][3], 300) or "(see stem)")
                    for k in missing)
    prompt = """These knowledge points were written for one science %s:
%s

Give each question below the number of the ONE point it mainly tests.
%s

Reply with JSON only: {"assign": {"<question number>": <point n>, ...}} with an entry for every question listed.""" % (
        "lesson" if scope["key_stage"] == "KS3" else "subtopic", listing, qs)
    text, _u = call_model(prompt, max_tokens=1500)
    got, _ = read_assign(extract_json(text), len(scope["questions"]), len(labels))
    still = [k for k in missing if k not in got]
    attempts.append({"repaired": missing, "raw": text[:3000]})
    if still:
        raise ValueError("question(s) %s not assigned to any point" % ", ".join(map(str, still)))
    out = dict(assign)
    out.update({k: got[k] for k in missing})
    return out


def classify_scope(scope, cache, force=False):
    path = cache_path(cache, scope["key_stage"], scope["scope_ref"])
    hsh = scope_hash(scope)
    if not force and os.path.exists(path):
        c = json.load(open(path, encoding="utf-8"))
        if c.get("hash") == hsh and (c.get("points") or c.get("failed")):
            return c
    error, attempts = None, []
    for attempt in range(3):
        try:
            text, usage = call_model(scope_prompt(scope, error))
        except RuntimeError as e:
            attempts.append({"error": str(e)})
            error = None
            continue
        try:
            obj = extract_json(text)
            labels = validate_points(obj)
            assign, missing = read_assign(obj, len(scope["questions"]), len(labels))
            if missing:
                # Repair, once: ask for just the questions it skipped.
                assign = repair_missing(scope, labels, assign, missing, attempts)
            pts = to_points(labels, assign)
            c = {"hash": hsh, "scope_ref": scope["scope_ref"], "key_stage": scope["key_stage"],
                 "raw": text, "usage": usage, "attempts": attempts, "points": pts,
                 "question_ids": [q[0] for q in scope["questions"]]}
            json.dump(c, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            return c
        except (ValueError, json.JSONDecodeError, RuntimeError) as e:
            error = str(e)
            attempts.append({"error": error, "raw": text[:6000]})
    c = {"hash": hsh, "scope_ref": scope["scope_ref"], "key_stage": scope["key_stage"],
         "failed": True, "attempts": attempts}
    json.dump(c, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return c


# ── pass 2: KS4 exam rows ───────────────────────────────────────────────

# exam_questions.topic (AQA topic name) → the site's topic id, per subject.
AQA_TOPIC = {
    "biology": {"cell biology": "cell-biology", "organisation": "organisation",
                "infection and response": "infection-response", "bioenergetics": "bioenergetics",
                "homeostasis and response": "homeostasis",
                "inheritance, variation and evolution": "inheritance", "ecology": "ecology"},
    "chemistry": {"atomic structure and the periodic table": "atomic-structure",
                  "bonding, structure and the properties of matter": "bonding",
                  "quantitative chemistry": "quantitative", "chemical changes": "chemical-changes",
                  "energy changes": "energy-changes",
                  "the rate and extent of chemical change": "rates-equilibrium",
                  "organic chemistry": "organic", "chemical analysis": "analysis",
                  "chemistry of the atmosphere": "atmosphere", "using resources": "resources"},
    "physics": {"energy": "energy", "electricity": "electricity",
                "particle model of matter": "particle-model", "atomic structure": "atomic-structure",
                "forces": "forces", "waves": "waves",
                "magnetism and electromagnetism": "magnetism", "space physics": "space"},
}


def _wtm_item_ids(src):
    """The ids of the TOP-LEVEL items of every `writeThenMark: [...]` array
    (not the mark-point ids nested inside them). A small scanner that skips
    JS string literals so a bracket inside a string cannot miscount."""
    out = []
    for m in re.finditer(r"\bwriteThenMark\s*:\s*\[", src):
        i, depth, quote = m.end(), 1, None   # depth 1 = inside the array
        start_obj = None
        while i < len(src) and depth > 0:
            ch = src[i]
            if quote:
                if ch == "\\":
                    i += 2
                    continue
                if ch == quote:
                    quote = None
            elif ch in "'\"`":
                quote = ch
            elif ch in "[{(":
                depth += 1
                if depth == 2 and ch == "{":
                    start_obj = i
            elif ch in "]})":
                depth -= 1
                if depth == 1 and ch == "}" and start_obj is not None:
                    body = src[start_obj:i]
                    # the item's own id: the first `id:` at nesting depth 0 of the object
                    d, q2, k = 0, None, 1
                    while k < len(body):
                        c = body[k]
                        if q2:
                            if c == "\\":
                                k += 2
                                continue
                            if c == q2:
                                q2 = None
                        elif c in "'\"`":
                            q2 = c
                        elif c in "[{(":
                            d += 1
                        elif c in "]})":
                            d -= 1
                        elif d == 0 and body.startswith("id:", k) and not body[k - 1].isalnum():
                            mm = re.match(r"id:\s*'([^']+)'", body[k:])
                            if mm:
                                out.append(mm.group(1))
                            break
                        k += 1
                    start_obj = None
            i += 1
    return out


def bv2_subtopic_of():
    """bonding_v2 exam row id → subtopic slug: each writeThenMark item in
    shared/exam-content/<subtopic>.js is exam row `bv2-<item.id>`, and the
    file is named for its subtopic."""
    out = {}
    for f in sorted(glob.glob(os.path.join(REPO, "shared", "exam-content", "*.js"))):
        slug = os.path.basename(f)[:-3]
        for item in _wtm_item_ids(open(f, encoding="utf-8").read()):
            out.setdefault("bv2-" + item, slug)
    return out


TEST_REF = "qeppkiswvclkkwbxmlok"


def jwt_ref(token):
    """The Supabase project ref a JWT was issued for, or None (payload only,
    no signature check — it answers WHICH project, not whether it is real).
    Same as export_ks4_questions._jwt_ref."""
    import base64
    try:
        payload = token.split(".")[1]
        payload += "=" * (-len(payload) % 4)
        claims = json.loads(base64.urlsafe_b64decode(payload).decode("utf-8"))
    except Exception:
        return None
    ref = claims.get("ref")
    return ref if isinstance(ref, str) and ref else None


def test_credentials():
    """(url, service key) for TEST, read from the backend .env, refusing
    unless the KEY's own ref claim is the TEST project. Never prints either."""
    conf = {}
    with open(BACKEND_ENV, encoding="utf-8") as fh:
        for line in fh:
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                conf[k.strip()] = v.strip()
    key = conf.get("SUPABASE_SERVICE_ROLE_KEY", "")
    url = conf.get("SUPABASE_URL", "")
    ref = jwt_ref(key) if key else None
    if ref != TEST_REF:
        raise SystemExit("kp: the service key in %s belongs to project %r, not TEST %r. Refusing."
                         % (BACKEND_ENV, ref, TEST_REF))
    if url and TEST_REF not in url:
        raise SystemExit("kp: %s sets a SUPABASE_URL that does not match its own key. Refusing." % BACKEND_ENV)
    return (url or "https://%s.supabase.co" % TEST_REF).rstrip("/"), key


def fetch_exam_rows():
    """KS4 exam_questions rows from TEST (read-only; service key from the
    backend .env, which is the TEST project — proven from the key's ref)."""
    url, key = test_credentials()
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem")
    rq = urllib.request.Request(
        url + "/rest/v1/exam_questions?select=id,key_stage,subject,topic,text,scheme,source"
              "&key_stage=eq.KS4&order=id&limit=1000",
        headers={"apikey": key, "Authorization": "Bearer " + key})
    with urllib.request.urlopen(rq, context=ctx, timeout=60) as r:
        return json.load(r)


def exam_candidates(row, inv, kp):
    """[(kp_id, label, subtopic)] the row may be tagged with."""
    subj = (row.get("subject") or "").lower()
    if row["id"].startswith("bv2-"):
        sub = bv2_subtopic_of().get(row["id"])
        subs = [sub] if sub in inv["KS4"] else []
    else:
        tid = AQA_TOPIC.get(subj, {}).get((row.get("topic") or "").strip().lower())
        subs = sorted(s for s, sc in inv["KS4"].items()
                      if sc["subject"] == subj and sc["topic_id"] == tid)
    out = []
    for s in subs:
        sc = kp.get(s)
        if not sc:
            continue
        for p in sc["points"]:
            out.append((p["id"], p["label"], inv["KS4"][s]["title"]))
    return out


def classify_exam_row(row, cands, cache, force=False):
    path = os.path.join(cache, "exam__%s.json" % row["id"])
    hsh = hashlib.sha256(json.dumps([row["text"], [list(c) for c in cands]],
                                    ensure_ascii=False).encode()).hexdigest()[:16]
    if not force and os.path.exists(path):
        c = json.load(open(path, encoding="utf-8"))
        if c.get("hash") == hsh:
            return c
    if not cands:
        c = {"hash": hsh, "id": row["id"], "kp": None, "reason": "no candidate points for its topic"}
        json.dump(c, open(path, "w"), indent=1)
        return c
    scheme = row.get("scheme") or []
    pts = "; ".join(plain(s.get("text") if isinstance(s, dict) else s) for s in scheme)
    listing = "\n".join("%d. [%s] %s" % (i, sub, lab) for i, (_k, lab, sub) in enumerate(cands, 1))
    prompt = """You are an experienced UK GCSE science examiner. Below is one exam question and a numbered list of knowledge points (each tagged with its subtopic). Pick the ONE knowledge point that the question mainly tests. If none of them fits the main thing the question tests, answer 0.

QUESTION
%s
Mark scheme points: %s

KNOWLEDGE POINTS
%s

Reply with JSON only: {"point": <number, or 0 for none>}""" % (plain(row["text"]), clip(pts, 1500), listing)
    error, last = None, None
    for attempt in range(3):
        try:
            text, _u = call_model(prompt + ("\n\nYour previous reply was rejected: %s." % error if error else ""),
                                  max_tokens=200)
            last = text
            n = extract_json(text).get("point")
            if not isinstance(n, int) or not 0 <= n <= len(cands):
                raise ValueError("point must be 0..%d" % len(cands))
            c = {"hash": hsh, "id": row["id"], "kp": cands[n - 1][0] if n else None,
                 "reason": None if n else "model: no point fits", "raw": text}
            json.dump(c, open(path, "w"), ensure_ascii=False, indent=1)
            return c
        except (ValueError, json.JSONDecodeError, RuntimeError) as e:
            error = str(e)
    c = {"hash": hsh, "id": row["id"], "kp": None, "reason": "failed: %s" % error, "raw": last}
    json.dump(c, open(path, "w"), ensure_ascii=False, indent=1)
    return c


# ── assembly: cache → knowledge_points/*.json ───────────────────────────

def assemble(inv, results, exam_results):
    """Build the three data files from the per-scope results. Returns
    (ks3, ks4, untagged)."""
    data = {"KS3": {}, "KS4": {}}
    untagged = {"failed_scopes": [], "questions": {}}
    for ks in ("KS3", "KS4"):
        for ref, scope in sorted(inv[ks].items()):
            c = results.get((ks, ref))
            if not c or c.get("failed") or c.get("hash") != scope_hash(scope):
                untagged["failed_scopes"].append("%s:%s" % (ks, ref))
                for q in scope["questions"]:
                    untagged["questions"][q[0]] = {"source": DB_SOURCE[q[1]], "scope_ref": ref,
                                                   "reason": "scope classification failed"}
                continue
            prefix = "ks3" if ks == "KS3" else "ks4"
            points = [{"id": "%s.%s.%d" % (prefix, ref, i), "label": p["label"]}
                      for i, p in enumerate(c["points"], 1)]
            qmap = {}
            for i, p in enumerate(c["points"], 1):
                for n in p["questions"]:
                    qmap[scope["questions"][n - 1][0]] = "%s.%s.%d" % (prefix, ref, i)
            entry = {"scope_ref": ref, "key_stage": ks, "subject": scope["subject"],
                     "title": scope["title"], "points": points, "questions": qmap}
            data[ks][ref] = entry
    # KS3 exam twins take their rung's point.
    for exam_id, rung_id, slug in inv["exam_ks3"]:
        e = data["KS3"].get(slug)
        if e and rung_id in e["questions"]:
            e["questions"][exam_id] = e["questions"][rung_id]
        else:
            untagged["questions"][exam_id] = {"source": "exam", "scope_ref": slug,
                                              "reason": "its rung is untagged"}
    for rid, c in sorted(exam_results.items()):
        if c.get("kp"):
            ref = c["kp"].split(".")[1]
            data["KS4"][ref]["questions"][rid] = c["kp"]
        else:
            untagged["questions"][rid] = {"source": "exam", "scope_ref": None,
                                          "reason": c.get("reason") or "untagged"}
    for ks in data:
        for e in data[ks].values():
            e["questions"] = dict(sorted(e["questions"].items()))
    untagged["questions"] = dict(sorted(untagged["questions"].items()))
    untagged["failed_scopes"].sort()
    return data["KS3"], data["KS4"], untagged


def write_json(path, obj):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--cache", default=os.environ.get("KP_CACHE") or os.path.expanduser("~/tmp/kp-cache"))
    ap.add_argument("--scope", action="append", default=[],
                    help="classify only this scope ref (repeatable); every other scope is read from cache")
    ap.add_argument("--force", action="store_true", help="re-run the named scopes even if cached")
    ap.add_argument("--assemble-only", action="store_true", help="no model calls; build the JSON from cache")
    ap.add_argument("--no-exam", action="store_true", help="skip the KS4 exam-row pass")
    ap.add_argument("--workers", type=int, default=5)
    ap.add_argument("--inventory", action="store_true")
    a = ap.parse_args()

    inv = inventory()
    if a.inventory:
        from collections import Counter
        c = Counter(q[1] for ks in ("KS3", "KS4") for s in inv[ks].values() for q in s["questions"])
        print("scopes: KS3 %d, KS4 %d; questions by source: %s; KS3 exam twins %d"
              % (len(inv["KS3"]), len(inv["KS4"]), dict(c), len(inv["exam_ks3"])))
        return 0
    os.makedirs(a.cache, exist_ok=True)

    jobs = [(ks, ref) for ks in ("KS3", "KS4") for ref in sorted(inv[ks])]
    named = set(a.scope)
    results = {}
    todo = []
    for ks, ref in jobs:
        scope = inv[ks][ref]
        p = cache_path(a.cache, ks, ref)
        cached = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None
        if cached and cached.get("hash") == scope_hash(scope) and not (a.force and ref in named):
            if not (cached.get("failed") and ref in named):
                results[(ks, ref)] = cached
                continue
        if a.assemble_only or (named and ref not in named):
            if cached:
                results[(ks, ref)] = cached
            continue
        todo.append((ks, ref))

    print("kp: %d scope(s) cached, %d to classify with %s" % (len(results), len(todo), MODEL))
    done = [0]
    lock = threading.Lock()

    def run(job):
        ks, ref = job
        c = classify_scope(inv[ks][ref], a.cache, force=True)
        with lock:
            done[0] += 1
            print("  [%d/%d] %s %s %s" % (done[0], len(todo), ks, ref,
                                          "FAILED" if c.get("failed") else "%d points" % len(c["points"])),
                  flush=True)
        return job, c

    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        for job, c in ex.map(run, todo):
            results[job] = c

    # the provisional KS4 scope data the exam pass chooses from
    ks3, ks4, _ = assemble(inv, results, {})
    exam_results = {}
    if not a.no_exam:
        cached_only = a.assemble_only
        rows = []
        if cached_only:
            for p in sorted(glob.glob(os.path.join(a.cache, "exam__*.json"))):
                c = json.load(open(p, encoding="utf-8"))
                exam_results[c["id"]] = c
        else:
            rows = fetch_exam_rows()
            print("kp: %d KS4 exam row(s) to place" % len(rows))

            def run_exam(row):
                return row["id"], classify_exam_row(row, exam_candidates(row, inv, ks4), a.cache)

            with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
                for rid, c in ex.map(run_exam, rows):
                    exam_results[rid] = c
    ks3, ks4, untagged = assemble(inv, results, exam_results)
    os.makedirs(KP_DIR, exist_ok=True)
    write_json(os.path.join(KP_DIR, "ks3.json"), ks3)
    write_json(os.path.join(KP_DIR, "ks4.json"), ks4)
    write_json(os.path.join(KP_DIR, "untagged.json"), untagged)
    print("kp: wrote knowledge_points/ks3.json (%d scopes), ks4.json (%d scopes), untagged.json "
          "(%d question(s), %d failed scope(s))" % (len(ks3), len(ks4), len(untagged["questions"]),
                                                   len(untagged["failed_scopes"])))
    print("kp: this run's model usage — %d call(s), %d input token(s), %d output token(s)"
          % (USAGE["calls"], USAGE["input_tokens"], USAGE["output_tokens"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
