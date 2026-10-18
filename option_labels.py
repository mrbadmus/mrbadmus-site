"""The ONE rule for a quiz option that carries its reason (fix 2, Oct 2026).

Mide's ruling: a practice option must not carry its mistake or its working in
the label.  `('0.5 g — confusing moles with grams', False)` tells the pupil the
answer is wrong before they answer.  The label a pupil sees is the text BEFORE
the first spaced em-dash " — "; what follows is the reason.

This module is a DISPLAY-TIME transform, in the same spirit as `formulae()` in
`ks3_art/kit.py`: the stored data (the `all_subtopics_*.py` option tuples, the
KS3 `ks3_data` ladders, the question mirror, the knowledge points) is never
edited, so marking, shuffle seeds (derived from the ORIGINAL text), mirrors and
tutor knowledge are untouched.

Three renderers apply it, and they must agree:

  * `generate_site_v5.py`  — the KS4 topic-page quizzes (Python).
  * `build_ks3.py`         — the KS3 mastery ladder, `_rung_marked` (Python).
  * `shared/ks4-lib.js`    — `item()`, the one doorway every KS4 lesson-batch
                             practice question passes through (JavaScript).
                             Its function text is GENERATED here by `js_source()`
                             from the same constants, via `ks4_rulings.py`
                             R21, so the two cannot drift; `option_labels_check.py`
                             proves they agree over the whole corpus.

`plan()` is all-or-nothing PER QUESTION.  If stripping would damage the
question (an empty or bare-connective head, two options collapsing to the same
label, a pairing/matching stem, a short head+descriptor pair) the whole
question is left exactly as authored and reported as an exception.
"""
import re

SEP = " — "          # the spaced em-dash; an unspaced dash is never split

# A head that is only a joining word has been cut off from its meaning.
CONNECTIVES = ["because", "so", "and", "but", "as", "since", "then", "which",
               "while", "hence", "therefore", "if", "or", "thus", "when"]
# A stem that asks the pupil to pair/match/sort: the tail is the other half
# of the pair, not a reason.
PAIRING_STEM = r"\b(match(ed|es|ing)?|pair(s|ed|ing)?|sort(ed)?|categori[sz]e|classify|which (goes|belongs) with)\b"
# head + descriptor ("Pig — herbivore"): both halves short, tail has no reasoning.
SHORT_HEAD_WORDS = 2
SHORT_TAIL_WORDS = 3

EX_EMPTY = "empty-head"
EX_CONNECTIVE = "bare-connective"
EX_DUPLICATE = "duplicate-labels"
EX_PAIRING = "pairing-stem"
EX_DESCRIPTOR = "short-head-descriptor"


def split_tail(text):
    """(head, tail) at the FIRST spaced em-dash; tail is '' when there is none."""
    i = text.find(SEP)
    if i < 0:
        return text, ""
    return text[:i].strip(), text[i + len(SEP):].strip()


def _norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def _words(s):
    return [w for w in re.split(r"\s+", s.strip()) if w]


def plan(stem, options, explanations=None):
    """Decide the display of ONE question.

    stem          the question text
    options       list of (text, is_correct)
    explanations  {index: text} wrong-option explanations already authored
                  (keys may be int or str)

    Returns a dict:
      strip     True when labels are shortened
      reason    None, or the exception code when `strip` is False but a tail exists
      labels    the text to show, per option (== the original when not stripped)
      feedback  {index: text} to use for a WRONG option that had no authored
                explanation (the relocated tail)
      right     {index: text} the tail of a CORRECT option, for a renderer
                that has a slot for it
      tails     number of options that carried a tail
    """
    expl = {}
    for k, v in (explanations or {}).items():
        expl[int(k)] = v
    texts = [o[0] for o in options]
    parts = [split_tail(t) for t in texts]
    tails = sum(1 for h, tl in parts if tl)
    out = {"strip": False, "reason": None, "labels": list(texts),
           "feedback": {}, "right": {}, "tails": tails}
    if not tails:
        return out
    heads = [h for h, _ in parts]
    reason = None
    if any(len(h) < 1 for h in heads):
        reason = EX_EMPTY
    elif any(re.sub(r"[^a-z]+$", "", h.lower()) in CONNECTIVES for h in heads):
        reason = EX_CONNECTIVE
    elif len({_norm(h) for h in heads}) < len(heads):
        reason = EX_DUPLICATE
    elif re.search(PAIRING_STEM, stem or "", re.I):
        reason = EX_PAIRING
    else:
        tailed = [(h, tl) for h, tl in parts if tl]
        if all(len(_words(h)) <= SHORT_HEAD_WORDS
               and len(_words(tl)) <= SHORT_TAIL_WORDS
               and not re.search(r"[0-9=÷×+]", tl) for h, tl in tailed):
            reason = EX_DESCRIPTOR
    if reason:
        out["reason"] = reason
        return out
    out["strip"] = True
    out["labels"] = heads
    for i, ((h, tl), (_, ok)) in enumerate(zip(parts, options)):
        if not tl:
            continue
        if ok:
            out["right"][i] = tl
        elif not expl.get(i):
            out["feedback"][i] = tl
    return out


def sent_text(raw):
    """What a page's option button used to SEND as its text: the rendered
    textContent of the stored option (tags dropped, entities decoded, trimmed).
    Display-only rule (Mide, D): the pupil sees the short label, but the page
    keeps sending exactly this for the chosen / right option."""
    import html as _h
    return _h.unescape(re.sub(r"<[^>]+>", "", raw)).strip()


def full_attr(label, raw, sent=None):
    """` data-full="..."` for an option whose label was shortened, else ''.
    `sent` overrides the text carried (KS3, where textContent is of sci())."""
    if label == raw:
        return ""
    import html as _h
    return ' data-full="%s"' % _h.escape(sent if sent is not None else sent_text(raw), quote=True)


def js_source():
    """The JavaScript twin of `plan()`, as ES5 text for `shared/ks4-lib.js`.

    Generated from the constants above so the two cannot drift.  Defines
    `optionPlan(stem, opts, we)` where `opts` is [[text, correct], ...] and
    `we` is the wrong_explanations object; returns the same shape as plan()
    (labels as an array, feedback/right as objects keyed by index).
    """
    import json
    return (
        "  /* ⊕ R21 (ks4_rulings.py; option_labels.py is the one rule): a practice option\n"
        "     shows only the text BEFORE its first \" — \"; the reason moves into the\n"
        "     feedback. GENERATED from option_labels.py. The shuffle key below is still\n"
        "     computed from the ORIGINAL text, so option order does not move. */\n"
        "  var OPT_SEP = " + json.dumps(SEP) + ";\n"
        "  var OPT_CONNECTIVES = " + json.dumps(CONNECTIVES) + ";\n"
        "  var OPT_PAIRING = new RegExp(" + json.dumps(PAIRING_STEM) + ", 'i');\n"
        "  var OPT_DESC_RE = /[0-9=\\u00f7\\u00d7+]/;\n"
        "  function optWords(s) { return s.trim().split(/\\s+/).filter(Boolean); }\n"
        "  function optSplit(t) {\n"
        "    var i = t.indexOf(OPT_SEP);\n"
        "    if (i < 0) return [t, ''];\n"
        "    return [t.slice(0, i).trim(), t.slice(i + OPT_SEP.length).trim()];\n"
        "  }\n"
        "  function optNorm(s) { return s.replace(/\\s+/g, ' ').trim().toLowerCase(); }\n"
        "  function optionPlan(stem, opts, we) {\n"
        "    var parts = opts.map(function (o) { return optSplit(o[0]); });\n"
        "    var out = { strip: false, labels: opts.map(function (o) { return o[0]; }), feedback: {}, right: {} };\n"
        "    var tailed = parts.filter(function (p) { return p[1]; });\n"
        "    if (!tailed.length) return out;\n"
        "    var heads = parts.map(function (p) { return p[0]; });\n"
        "    var bad = heads.some(function (h) { return h.length < 1; })\n"
        "      || heads.some(function (h) { return OPT_CONNECTIVES.indexOf(h.toLowerCase().replace(/[^a-z]+$/, '')) >= 0; })\n"
        "      || (function () { var seen = {}, dup = false; heads.forEach(function (h) { var k = optNorm(h); if (seen[k]) dup = true; seen[k] = 1; }); return dup; })()\n"
        "      || OPT_PAIRING.test(stem || '')\n"
        "      || tailed.every(function (p) { return optWords(p[0]).length <= " + str(SHORT_HEAD_WORDS) + " && optWords(p[1]).length <= " + str(SHORT_TAIL_WORDS) + " && !OPT_DESC_RE.test(p[1]); });\n"
        "    if (bad) return out;\n"
        "    out.strip = true; out.labels = heads;\n"
        "    parts.forEach(function (p, i) {\n"
        "      if (!p[1]) return;\n"
        "      if (opts[i][1]) out.right[i] = p[1];\n"
        "      else if (!(we && we[String(i)])) out.feedback[i] = p[1];\n"
        "    });\n"
        "    return out;\n"
        "  }\n")
