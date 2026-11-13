# -*- coding: utf-8 -*-
"""lean_ks4.py: the KS4 lean lesson page source.

`source(lesson)` returns `(template_text, logic_text, port_report)` for a lesson that
carries a lean record (`lesson["lean"]`, see docs/lessons/LEAN-RECORD.md). It is what
build_ks4.compile_batch_lesson compiles INSTEAD of reading a .dc.html.

The page (all four routes, one compiled template, the route flags decide at run time):

    Ks4Chrome, h1, route switch (and the equation-sheet link, if the lesson had one)
    Start here         Ks4Guess (lean copy: no title, no "Good guess", no bridge)
    Key words          lean_blocks HTML
    Key knowledge      lean_blocks HTML, cards closed until tapped; slots are compiled blocks
    Key fact           lean_blocks HTML
    Try it             only when the record names a simulation
    Practice           the ladder and the QuizBank sections, verbatim from the legacy page
                       (or a generic pair for a lesson with no legacy page)
    Dive deeper        lean_blocks HTML, closed until tapped
    Ks4End

Two kinds of lesson:

  LEGACY  (record["legacy"]["batch"]): a live Design lesson. Its post-ruling template and
          logic (ks4_batch_rulings.port_lesson + ks4_science_rulings, exactly what
          compile_batch_lesson used) are the starting point. The logic class is kept, so
          rungs, quiz bank and every quiz item stay verbatim. Only these are edited, by
          exact match, and each edit fails loudly if its target is not found once:
              the RAIL constant               three stops, Start here / Key knowledge / Practice
              the rail done[] array           [hook, knowledge opened, ladder]
              `onLadder:` line                gains `onKnow`
              `hookOptions:`                  built from the record's start
              the first cfExamples entry      only when the record has `cfifa_first`
              `return Object.assign({}, R, {` gains LEAN_PROPS (record equations / cfifa)
  GENERIC (no legacy): a small data-driven logic class. Rungs come from the record, the
          bank from K.bank (the per-route quiz data in all_subtopics_*.py). This is the
          pattern later batches reuse.

STATE IS NOT IN THE TEMPLATE. Open cards carry `data-lean-open` and `aria-expanded`, put on
by shared/lean.js, because ks4-runtime.js rewrites any attribute a template names back to
the template's value on every render (lean_blocks.py's docstring says why). The Key
knowledge section carries `onClick="{{ onKnow }}"`: a tap inside it, or a swipe (lean.js
sends the section a click), sets `know`, which ticks the rail.
"""
import html
import json
import re

import lean_blocks

# ── the three rail stops ────────────────────────────────────────────────
RAIL_JS = ("const RAIL = [\n"
           "  { id: 's-hook', label: 'Start here', short: 'START' },\n"
           "  { id: 's-knowledge', label: 'Key knowledge', short: 'KNOW' },\n"
           "  { id: 's-ladder', label: 'Practice', short: 'PRACTICE' }\n"
           "];")
DONE_JS = "const done = [s.hook !== null, !!s.know, s.ladder];"

# Slots that describe a figure the legacy page's `legal` line is about. Without one of these
# the legacy legal line ("The bench uses g = 9.8 ...") describes something no longer on the page.
LEGAL_SLOTS = {"sankey", "mix"}

_FIG_DIV = ('<div style="border-radius: var(--ks3-r-panel); overflow: hidden; '
            'border: 2px solid var(--ks3-ink);">{{ %s }}</div>')
SIMPLE_FIG_SLOTS = {"rp-fig": "rpFig", "particle-fig": "particleFig"}

_STYLE_ARRIVE = """<style>
  html, body { margin: 0; padding: 0; background: #FBF3E6; }
  a { color: var(--ks3-accent-text); }
  a:hover { color: var(--ks3-accent-hover); }
  @keyframes ks4-arrive { 0% { transform: translateY(6px); opacity: 0; } 100% { transform: translateY(0); opacity: 1; } }
  [data-arrive] { animation: ks4-arrive .34s ease-out both; }
  @media (prefers-reduced-motion: reduce) { [data-arrive] { animation: none !important; } * { transition: none !important; } }
  button:focus-visible, a:focus-visible, select:focus-visible, input:focus-visible, textarea:focus-visible { outline: 3px solid var(--ks3-accent-text); outline-offset: 2px; }
  input[type="range"] { accent-color: #A93411; }
</style>"""

GENERIC_HELMET = ("<helmet>\n"
                  '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
                  "<title>@@TITLE@@</title>\n"
                  '<link rel="stylesheet" href="../../_ds/mrbadmusai-design-system-53dad5ae-951a-44a1-95e1-394b9762b2d1/styles.css">\n'
                  '<link rel="stylesheet" href="ks4-theme.css">\n'
                  '<script src="ks4-lib.js"></script>\n'
                  '<script src="ks4-diagrams.js"></script>\n'
                  + _STYLE_ARRIVE + "\n</helmet>")

RD_OPEN = ('<div class="rd" data-mode="ks3" data-theme="{{ theme }}" style="background: var(--ks3-ground); '
           'color: var(--ks3-ink); font-family: var(--ks3-font-body); font-size: 19px; line-height: 1.6; '
           'min-height: 100vh; -webkit-font-smoothing: antialiased; text-wrap: pretty;">')

ROUTE_SWITCH = """        <div style="margin-top: 16px; display: flex; flex-wrap: wrap; align-items: center; gap: 8px 10px;">
          <details class="ks3-route-switch">
            <summary class="ks3-route-chip" aria-expanded="false"><span>{{ routeWords }}</span><svg aria-hidden="true" focusable="false" width="12" height="12" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg></summary>
            <ul class="ks3-route-menu" role="list">
              <sc-for list="{{ routeSwitchOptions }}" as="o"><li><a href="{{ o.href }}">{{ o.label }}</a></li></sc-for>
            </ul>
          </details>
        </div>"""

EQ_SHEET_LINK = """        <div style="margin-top: 14px; display: flex; flex-wrap: wrap; align-items: center; gap: 8px 14px;">
          <a href="{{ eqSheetHref }}" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 10px; min-height: 44px; padding: 10px 16px; border-radius: var(--ks3-r-control); border: 2px solid var(--ks3-ink); background: var(--ks3-card); color: var(--ks3-ink); font-size: 16px; font-weight: 700; text-decoration: none;" style-hover="background: var(--ks3-accent-tint); border-color: var(--ks3-accent);">View the full equation sheet<svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3H3v10h10v-3"></path><path d="M9 3h4v4"></path><path d="M13 3L7 9"></path></svg></a>
          <span style="font-family: var(--ks3-font-mono); font-size: 14px; color: var(--ks3-ink-muted);">AQA · {{ eqSheetLabel }} · PDF</span>
        </div>"""

GENERIC_LADDER = """      <section id="s-ladder" style="scroll-margin-top: 92px; margin-top: 28px;">
        <sc-if value="{{ ready }}" hint-placeholder-val="{{ true }}">
          <dc-import name="Ks4Practice" slug="%(slug)s" rungs="{{ rungs }}" on-done="{{ onLadder }}" hint-size="100%%,1400px"></dc-import>
        </sc-if>
      </section>"""

GENERIC_QUIZ = """      <section style="margin-top: 34px;">
        <sc-if value="{{ ready }}" hint-placeholder-val="{{ true }}">
          <dc-import name="Ks4QuizBank" questions="{{ bank }}" route-label="{{ route }}" hint-size="100%,300px"></dc-import>
        </sc-if>
      </section>"""

GENERIC_END = ('      <dc-import name="Ks4End" subject="%(subject)s" prev="{{ endPrev }}" next="{{ endNext }}" '
               'connects="{{ endConnects }}" tutor-line="Not sure about something in this lesson?" '
               'legal="" hint-size="100%%,420px"></dc-import>')

GENERIC_TAIL = "\n    </div>\n  </main>\n</div>\n</x-dc>"


# ── small text tools ────────────────────────────────────────────────────

def _once(text, old, new, what):
    n = text.count(old)
    if n != 1:
        raise SystemExit("lean_ks4: %s: expected exactly one %r, found %d" % (what, old[:70], n))
    return text.replace(old, new)


def _match_close(text, i, open_ch, close_ch):
    """Index just past the bracket that closes the one at text[i]. String aware."""
    assert text[i] == open_ch, (text[i:i + 20], open_ch)
    depth, j, n = 0, i, len(text)
    while j < n:
        c = text[j]
        if c in "'\"`":
            q = c
            j += 1
            while j < n and text[j] != q:
                j += 2 if text[j] == "\\" else 1
        elif c == "/" and text[j:j + 2] == "//":
            j = text.index("\n", j)
        elif c == "/" and text[j:j + 2] == "/*":
            j = text.index("*/", j) + 1
        elif c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    raise SystemExit("lean_ks4: unbalanced %s%s" % (open_ch, close_ch))


def _attr(s):
    return html.escape(str(s), quote=True)


def js(value):
    """A JS literal for plain data (JSON is JS)."""
    return json.dumps(value, ensure_ascii=True)


# ── slots ───────────────────────────────────────────────────────────────

def _wrap_fig_div(markup, prop):
    """Wrap the bordered div that holds `{{ <prop> }}` in lean_blocks.fig_wrap, in place."""
    pat = re.compile(r'<div style="border-radius: var\(--ks3-r-panel\); overflow: hidden; '
                     r'border: 2px solid var\(--ks3-ink\);">\{\{ %s \}\}</div>' % prop)
    if len(pat.findall(markup)) != 1:
        raise SystemExit("lean_ks4: the legacy figure div for {{ %s }} is not found once" % prop)
    return pat.sub(lambda m: lean_blocks.fig_wrap(m.group(0)), markup)


def _legacy_slot_sources(tpl):
    """Markup the legacy template already draws, for slots that reuse it unchanged."""
    out = {}
    if tpl is None:
        return out
    m = re.search(r'<section id="s-sankey".*?</section>', tpl, re.S)
    if m:
        sec = m.group(0)
        sec = re.sub(r'\s*<p class="ks3-eyebrow"[^>]*>.*?</p>', "", sec, count=1, flags=re.S)
        sec = re.sub(r"\s*<h2[^>]*>.*?</h2>", "", sec, count=1, flags=re.S)
        sec = re.sub(r'\s*<p style="margin: 12px 0 0; max-width: 62ch;">.*?</p>', "", sec,
                     count=1, flags=re.S)
        sec = re.sub(r"^<section[^>]*>", "", sec)
        sk = re.sub(r"</section>$", "", sec).strip()
        out["sankey"] = _wrap_fig_div(sk, "sankeyFig")
    for mode in ("worked", "attempt"):
        m = re.search(r'<dc-import name="Ks4Steps" mode="%s"[^>]*></dc-import>' % mode, tpl)
        if m:
            out["steps-" + mode] = ('<sc-if value="{{ ready }}" hint-placeholder-val="{{ true }}">'
                                    + m.group(0) + "</sc-if>")
    m = re.search(r'<div style="margin-top: 14px; display: flex; gap: 6px; flex-wrap: wrap;">\s*'
                  r'<sc-for list="\{\{ years \}\}".*?</sc-for>\s*</div>', tpl, re.S)
    fig = re.search(r'<div style="border-radius: var\(--ks3-r-panel\); overflow: hidden; '
                    r'border: 2px solid var\(--ks3-ink\);">\{\{ mixFig \}\}</div>', tpl)
    line = re.search(r'<p aria-live="polite" style="[^"]*">\{\{ yearLine \}\}</p>', tpl)
    if m and fig and line:
        out["mix"] = "%s\n%s\n%s" % (m.group(0), lean_blocks.fig_wrap(fig.group(0)), line.group(0))
    return out


class _Slots:
    def __init__(self, rec, legacy_tpl):
        self.rec = rec
        self.legacy = _legacy_slot_sources(legacy_tpl)
        self.used = set()

    def __call__(self, part):
        if "figure" in part:
            raise ValueError("lean KS4 record: {'figure': ...} is KS3 only")
        name = part["slot"]
        self.used.add(name)
        if name.startswith("fig:"):
            # a drawn figure for a card (figlib/ks4lean.py): inline SVG, checked, unknown names raise
            from figlib import ks4lean
            return lean_blocks.fig_wrap(ks4lean.svg(name[4:]))
        if name in SIMPLE_FIG_SLOTS:
            return lean_blocks.fig_wrap(_FIG_DIV % SIMPLE_FIG_SLOTS[name])
        if name == "triangle-energy":
            return self._triangle("eqEnergy")
        if name == "triangle-power":
            return self._triangle("eqPower")
        if name.startswith("triangle:"):
            eq = name.split(":", 1)[1]
            if eq not in (self.rec.get("equations") or {}):
                raise ValueError("lean KS4 record %r: slot %r names an equation the record "
                                 "does not define" % (self.rec["slug"], name))
            if not self.rec["equations"][eq].get("top"):
                raise ValueError("lean KS4 record %r: slot %r names a sheet equation (no top/bottom), "
                                 "which cannot be a triangle" % (self.rec["slug"], name))
            return self._triangle("leanEq_" + eq)
        if name == "cfifa":
            ex, qs = (("leanCfExamples", "leanCfQuestions") if self.rec.get("cfifa")
                      else ("cfExamples", "cfQuestions"))
            return ('<sc-if value="{{ ready }}" hint-placeholder-val="{{ true }}">'
                    '<dc-import name="Ks4Cfifa" examples="{{ %s }}" questions="{{ %s }}" '
                    'on-open="{{ onCalc }}" hint-size="100%%,900px"></dc-import></sc-if>' % (ex, qs))
        if name in self.legacy:
            return self.legacy[name]
        raise ValueError("lean KS4 record %r: slot %r has no markup (a legacy lesson's own "
                         "figure must exist in its page)" % (self.rec["slug"], name))

    @staticmethod
    def _triangle(prop):
        return ('<sc-if value="{{ ready }}" hint-placeholder-val="{{ true }}">'
                '<dc-import name="Ks4Triangle" eq="{{ %s }}" variant="full" '
                'hint-size="100%%,420px"></dc-import></sc-if>' % prop)


def _route_wrap(flag, out):
    return '<sc-if value="{{ %s }}">%s</sc-if>' % (flag, out)


# ── the spec eyebrow, route-aware ───────────────────────────────────────
#
# AQA Combined Science (8464) numbers physics 6.x; AQA Physics (8463) numbers the same sections
# 4.x with the same sub-numbers. A legacy page that writes the Combined number as a literal would
# show it on every Triple route, so the literal becomes `{{ leanEyebrow }}`, which the logic
# resolves from the route (the same mechanism power and changes-in-energy already use).

_EYEBROW_LITERAL = re.compile(r'<p class="ks3-eyebrow">AQA Physics (6\.[\d.]+)</p>')


def _eyebrow_js(lesson, spec):
    if lesson["subject"] != "physics" or not spec.startswith("6."):
        raise SystemExit("lean_ks4: %s: the 6.x to 4.x eyebrow rule is for physics sections, got %r"
                         % (lesson["slug"], spec))
    tail = (" \u00b7 %s" % lesson["family"]) if lesson.get("family") else ""
    comb = "AQA Combined Science (8464) %s%s" % (spec, tail)
    tri = "AQA Physics (8463) 4.%s%s" % (spec[2:], tail)
    return "const LEAN_EYEBROW = %s;\n" % js({"c": comb, "t": tri})


# ── the template ────────────────────────────────────────────────────────

def _start_here(rec):
    st = rec["start"]
    attrs = []
    if st.get("setup"):
        attrs.append('scene="%s"' % _attr(st["setup"]))
    attrs.append('question="%s"' % _attr(st["question"]))
    return ('      <section id="s-hook" class="ks3-block ks3-hook" style="scroll-margin-top: 92px;">\n'
            '        <dc-import name="Ks4Guess" %s options="{{ hookOptions }}" on-commit="{{ onHook }}" '
            'hint-size="100%%,420px"></dc-import>\n      </section>' % " ".join(attrs))


def _lean_sections(rec, slots):
    ctx = lean_blocks.Ctx(prefix="lean", state_attrs=False, part=slots, route_wrap=_route_wrap)
    parts = [lean_blocks.key_words(ctx, rec["words"], sid="s-words"),
             lean_blocks.knowledge(ctx, rec["knowledge"], sid="s-knowledge",
                                   extra=' onClick="{{ onKnow }}"'),
             lean_blocks.key_fact(ctx, rec["key_fact"], sid="s-fact"),
             lean_blocks.try_link(rec.get("try")),
             ]
    deeper = lean_blocks.deeper(ctx, rec["deeper"], sid="s-deeper")
    return "\n".join("      " + p for p in parts if p), "      " + deeper


def _legacy_template(lesson, rec, tpl):
    slots = _Slots(rec, tpl)
    helmet = tpl[:tpl.index("</helmet>") + len("</helmet>")]

    chrome = re.search(r'<dc-import name="Ks4Chrome"[^>]*></dc-import>', tpl)
    rd = re.search(r'<div class="rd"', tpl)
    header = re.search(r'<header class="ks3-lesson-head">.*?</header>', tpl, re.S)
    ladder = re.search(r'<section id="s-ladder".*?</section>', tpl, re.S)
    qi = tpl.index('name="Ks4QuizBank"')
    qa = tpl.rindex("<section", 0, qi)
    qb = tpl.index("</section>", qi) + len("</section>")
    end = re.search(r'<dc-import name="Ks4End"[^>]*></dc-import>', tpl)
    if not all((chrome, rd, header, ladder, end)):
        raise SystemExit("lean_ks4: %s: the legacy template is missing a part this build reads"
                         % lesson["slug"])

    hdr = header.group(0)
    # no big question; no compact triangles in the header; no Draft flag
    hdr, n1 = re.subn(r'\s*<p class="ks3-bigq">.*?</p>', "", hdr, count=1, flags=re.S)
    hdr, n2 = re.subn(r'\s*<div style="[^"]*">\s*(?:<dc-import name="Ks4Triangle"[^>]*'
                      r'variant="compact"[^>]*></dc-import>\s*)+</div>', "", hdr, flags=re.S)
    hdr, n3 = re.subn(r'\s*<sc-if value="\{\{ draftVisible \}\}"[^>]*>.*?</sc-if>', "", hdr,
                      count=1, flags=re.S)
    if n1 != 1 or n3 != 1:
        raise SystemExit("lean_ks4: %s: header has %d big question(s), %d draft flag(s)"
                         % (lesson["slug"], n1, n3))

    m = _EYEBROW_LITERAL.search(hdr)
    slots.spec = m.group(1) if m else None
    if m:
        hdr = hdr.replace(m.group(0), '<p class="ks3-eyebrow">{{ leanEyebrow }}</p>', 1)

    words_know_fact_try, deeper = _lean_sections(rec, slots)
    end_tag = end.group(0)
    if not (slots.used & LEGAL_SLOTS):
        end_tag = re.sub(r' legal="[^"]*"', ' legal=""', end_tag, count=1)

    body = [helmet, "", tpl[rd.start():chrome.start()].rstrip() + "\n  " + chrome.group(0), "",
            '  <main class="ks3-main">', '    <div class="ks3-lesson">',
            "      " + hdr, _start_here(rec), words_know_fact_try,
            "      " + ladder.group(0), "      " + tpl[qa:qb], deeper, "      " + end_tag]
    return "\n".join(body) + tpl[end.end():], slots


def _generic_template(lesson, rec):
    slots = _Slots(rec, None)
    slots.spec = str(lesson["spec"])
    title = lesson["title"]
    hdr = ['      <header class="ks3-lesson-head">',
           '        <p class="ks3-eyebrow">{{ leanEyebrow }}</p>',
           "        <h1>%s</h1>" % html.escape(title), ROUTE_SWITCH]
    if rec.get("equations"):
        hdr.append(EQ_SHEET_LINK)
    hdr.append("      </header>")
    chrome = ('<dc-import name="Ks4Chrome" subject="%s" unit="%s" title="%s" rv="{{ railV }}" '
              'hint-size="100%%,72px"></dc-import>'
              % (lesson["subject"].capitalize(), _attr(lesson.get("unit", "")), _attr(title)))
    words_know_fact_try, deeper = _lean_sections(rec, slots)
    body = [GENERIC_HELMET.replace("@@TITLE@@", html.escape(title)), "", RD_OPEN, "  " + chrome, "",
            '  <main class="ks3-main">', '    <div class="ks3-lesson">', "\n".join(hdr),
            _start_here(rec), words_know_fact_try,
            GENERIC_LADDER % {"slug": lesson["slug"]}, GENERIC_QUIZ, deeper,
            GENERIC_END % {"subject": lesson["subject"].capitalize()}]
    return "\n".join(body) + GENERIC_TAIL, slots


# ── the logic ───────────────────────────────────────────────────────────

def _hook_options_js(rec):
    st = rec["start"]
    return "[%s]" % ", ".join(
        "{ text: %s, correct: %s, reply: %s }" % (js(t), "true" if i == st["answer"] else "false", js(r))
        for i, (t, r) in enumerate(st["options"]))


def _example_js(ex, rec):
    steps = []
    for st in ex["steps"]:
        o = {"letter": st[0], "label": st[1], "line": st[2]}
        if len(st) > 3 and st[3]:
            o["note"] = st[3]
        steps.append(o)
    eq = ex["eq"]
    # the record's own equation, else one of the legacy logic's constants (EQ_E ...)
    eq_js = "LEAN_EQ." + eq if eq in (rec.get("equations") or {}) else eq
    fields = ["tab: %s" % js(ex["tab"]), "eq: %s" % eq_js, "find: %s" % js(ex["find"])]
    if ex.get("next"):
        fields.append("next: %s" % js(ex["next"]))
    fields += ["head: %s" % js(ex["head"]), "steps: %s" % js(steps)]
    return "{ " + ", ".join(fields) + " }"


def _lean_props_js(rec):
    """`const LEAN_EQ` and `const LEAN_PROPS`: the record's equations and CFIFA data as props."""
    eqs = rec.get("equations") or {}
    lines = []
    if eqs:
        lines.append("const LEAN_EQ = %s;" % js(eqs))
    props = ["leanEq_%s: LEAN_EQ.%s" % (k, k) for k in eqs]
    cf = rec.get("cfifa")
    if cf:
        props.append("leanCfExamples: [%s]" % ", ".join(_example_js(e, rec) for e in cf["examples"]))
        props.append("leanCfQuestions: %s" % js(cf.get("questions") or []))
    lines.append("const LEAN_PROPS = { %s };" % ", ".join(props))
    return "\n".join(lines) + "\n"


def _legacy_logic(lesson, rec, logic, spec=None):
    what = lesson["slug"] + " logic"
    m = re.search(r"const RAIL = \[.*?\n\];", logic, re.S)
    if not m or len(re.findall(r"const RAIL = \[", logic)) != 1:
        raise SystemExit("lean_ks4: %s: cannot find the RAIL constant" % what)
    logic = logic[:m.start()] + RAIL_JS + logic[m.end():]

    ms = re.findall(r"const done = \[[^\n]*\];", logic)
    if len(ms) != 1:
        raise SystemExit("lean_ks4: %s: cannot find the rail done[] array" % what)
    logic = logic.replace(ms[0], DONE_JS)

    # the record's own exact-match edits to the legacy logic (placeholders, one prompt): each
    # `old` must be in the logic; every occurrence is replaced
    for old, new in (rec.get("legacy") or {}).get("logic_edits") or []:
        if old not in logic:
            raise SystemExit("lean_ks4: %s: logic_edits target %r is not in the legacy logic"
                             % (what, old[:70]))
        logic = logic.replace(old, new)
    logic = _once(logic, "onLadder: () => this.setState({ ladder: true }),",
                  "onLadder: () => this.setState({ ladder: true }),\n"
                  "      onKnow: () => this.setState({ know: true }),", what)

    i = logic.index("hookOptions: [") + len("hookOptions: ")
    logic = logic[:i] + _hook_options_js(rec) + logic[_match_close(logic, i, "[", "]"):]

    cff = (rec.get("legacy") or {}).get("cfifa_first")
    if cff:
        i = logic.index("cfExamples: [") + len("cfExamples: ")
        j = logic.index("{", i)
        k = _match_close(logic, j, "{", "}")
        logic = logic[:j] + _example_js(cff, rec) + logic[k:]

    if rec.get("equations") or rec.get("cfifa"):
        logic = _once(logic, "return Object.assign({}, R, {",
                      "return Object.assign({}, R, LEAN_PROPS, {", what)
        logic = _lean_props_js(rec) + logic
    if spec:
        # the eyebrow literal became {{ leanEyebrow }}: resolve it from the route
        logic = _once(logic, "return Object.assign({}, R, ",
                      "return Object.assign({}, R, { leanEyebrow: R.isTriple ? LEAN_EYEBROW.t : LEAN_EYEBROW.c }, ", what)
        logic = _eyebrow_js(lesson, spec) + logic
    return logic


def _generic_logic(lesson, rec):
    rungs = rec.get("rungs")
    if not rungs or set(rungs) != {"r1", "r2", "r3", "r4"}:
        raise SystemExit("lean_ks4: %s has no legacy page, so its record needs rungs r1..r4"
                         % lesson["slug"])
    flat = ("{ route: 'Triple Higher', routeOptions: [], onRoute: () => {}, isHigher: true, "
            "isTriple: true, isTH: true, notHigher: false, notTriple: false, eqSheetHref: '#', "
            "eqSheetLabel: '' }")
    return (RAIL_JS + "\n" + _eyebrow_js(lesson, str(lesson["spec"])) + _lean_props_js(rec) + """
class Component extends DCLogic {
  state = { active: 0, libReady: false, route: null, hook: null, know: false, calc: 0, ladder: false };
  componentDidMount() {
    const t = setInterval(() => { if (window.KS4 && window.KS4D) { clearInterval(t); this.setState({ libReady: true }); this.io = window.KS4.observe(this, RAIL); } }, 40);
  }
  componentWillUnmount() { if (this.io) this.io.disconnect(); }
  renderVals() {
    const s = this.state; const K = window.KS4;
    const R = K ? K.route(this) : %(flat)s;
    const ready = !!(s.libReady && K && window.KS4D);
    %(done)s
    const railV = K ? K.rail(RAIL, done, s.active) : { rail: [] };
    const theme = this.props.theme && this.props.theme !== 'auto' ? this.props.theme : undefined;
    const slug = %(slug)s;
    return Object.assign({}, R, LEAN_PROPS, {
      railV, theme, ready, leanEyebrow: R.isTriple ? LEAN_EYEBROW.t : LEAN_EYEBROW.c,
      hookOptions: %(hook)s,
      onHook: (i) => this.setState({ hook: i }),
      onKnow: () => this.setState({ know: true }),
      onCalc: (n) => this.setState({ calc: n }),
      onLadder: () => this.setState({ ladder: true }),
      rungs: %(rungs)s,
      bank: ready ? K.bank(slug, R.route) : [],
      endPrev: this.props.mrbPrevNext.prev, endNext: this.props.mrbPrevNext.next,
      endConnects: []
    });
  }
}
""" % {"flat": flat, "done": DONE_JS, "slug": js(lesson["slug"]), "hook": _hook_options_js(rec),
       "rungs": js(rungs)})


# ── entry point ─────────────────────────────────────────────────────────

def source(lesson, legacy=None):
    """(template_text, logic_text, port_report) for a lesson carrying a lean record.

    `legacy` is `(tpl, logic, port_report)` after ks4_batch_rulings.port_lesson and
    ks4_science_rulings, from build_ks4.legacy_texts(); None for a lesson with no legacy page."""
    rec = lesson["lean"]
    for k, e in (rec.get("equations") or {}).items():
        # an equation is a triangle (top and bottom) or a sheet equation: name, written, source "sheet"
        if bool(e.get("top")) != bool(e.get("bottom")) or (not e.get("top") and (
                e.get("source") != "sheet" or not e.get("written"))):
            raise ValueError("lean KS4 record %r: equation %s needs top+bottom (a triangle) or "
                             "source 'sheet' with name and written" % (rec["slug"], k))
    for it in rec["knowledge"] + rec["deeper"]:
        lean_blocks.route_flag(it.get("routes"))          # rejects any route set we cannot gate
    if legacy is not None:
        tpl, logic, report = legacy
        template, slots = _legacy_template(lesson, rec, tpl)
        logic = _legacy_logic(lesson, rec, logic, slots.spec)
    else:
        template, slots = _generic_template(lesson, rec)
        logic, report = _generic_logic(lesson, rec), {}
    return template, logic, report
