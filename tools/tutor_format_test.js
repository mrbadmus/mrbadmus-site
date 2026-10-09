/* tutor_format_test.js — the tutor bubble's Markdown, from the REAL
 * shared/mrbadmus.v2.js (formatReply, exposed only on
 * window.MRB_TUTOR_TEST_HOOK).
 *
 *   node tools/tutor_format_test.js
 *
 * ⊕ B2C polish (9 Oct 2026): real answers showed literal "---" lines and a
 * leading "> ". Escape first, then format; everything else as before.
 * Not a registered gate (see tools/set_work_time_test.js); run by hand.
 */
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const SRC = path.join(__dirname, "..", "shared", "mrbadmus.v2.js");
const noop = () => {};
const win = { MRB_TUTOR_TEST_HOOK: {}, addEventListener: noop };
const sandbox = { window: win, setInterval: noop, setTimeout: noop, clearTimeout: noop,
  fetch: () => Promise.resolve({ ok: false }), document: { addEventListener: noop, querySelector: () => null,
  getElementById: () => null }, console, localStorage: { getItem: () => null } };
vm.createContext(sandbox);
vm.runInContext(fs.readFileSync(SRC, "utf8"), sandbox, { filename: SRC });
const f = win.MRB_TUTOR_TEST_HOOK.formatReply;
if (typeof f !== "function") { console.error("FAIL formatReply not exposed"); process.exit(2); }

let failures = 0;
function check(name, got, want) {
  const ok = got === want;
  if (!ok) { failures += 1; }
  console.log(`${ok ? "  ok  " : "  FAIL"}  ${name}${ok ? "" : `\n           got  ${got}\n           want ${want}`}`);
}

// Unchanged behaviour.
check("bold / italics / code", f("**diffusion** is *passive* `net`"),
      "<strong>diffusion</strong> is <em>passive</em> <code>net</code>");
check("newline is <br>, blank line is <br><br>", f("a\nb\n\nc"), "a<br>b<br><br>c");
// ⊕ Round 2 (9 Oct 2026): lists are real lists now.
check("bullets and numbers are lists", f("- one\n- two\n1. three"),
      "<ul><li>one</li><li>two</li></ul><ol><li>three</li></ol>");
check("trailing newline", f("a\n"), "a<br>");
// Escaped first.
check("HTML in a reply is text", f("<img src=x onerror=alert(1)> **b**"),
      "&lt;img src=x onerror=alert(1)&gt; <strong>b</strong>");
check("x < 5 & y > 2 inline", f("x < 5 & y > 2"), "x &lt; 5 &amp; y &gt; 2");
check("a script tag in a quote is still text", f("> <script>x</script>"),
      '<blockquote class="chat-quote">&lt;script&gt;x&lt;/script&gt;</blockquote>');
// Rules.
check("--- is a rule, blank lines round it dropped", f("Top\n\n---\n\nBottom"),
      'Top<hr class="chat-rule">Bottom');
check("*** and ___ and - - - are rules", f("a\n***\nb\n___\nc\n- - -\nd"),
      'a<hr class="chat-rule">b<hr class="chat-rule">c<hr class="chat-rule">d');
check("-- is not a rule", f("a\n--\nb"), "a<br>--<br>b");
check("a dash inside a sentence is not a rule", f("energy --- the stores"), "energy --- the stores");
// Quotes.
check("leading > is a quote", f("> Remember: **ATP**\n\nNext"),
      '<blockquote class="chat-quote">Remember: <strong>ATP</strong></blockquote>Next');
check("consecutive > lines are one quote", f("Intro\n> one\n> two\n>\n> three\nOut"),
      'Intro<blockquote class="chat-quote">one<br>two<br><br>three</blockquote>Out');
check("> with no space", f(">tight"), '<blockquote class="chat-quote">tight</blockquote>');
check("a > mid-line is not a quote", f("A > B"), "A &gt; B");
// Headings (same defect: raw ## marks).
check("## heading is a bold line", f("## Diffusion\nIt is net movement"),
      "<strong>Diffusion</strong><br>It is net movement");
check("#hashtag without space is text", f("#1 tip"), "#1 tip");
// A real-shaped reply.
check("real reply shape", f("> Great question!\n\n**Diffusion** is...\n\n---\n\n✅ Key exam words: **net**"),
      '<blockquote class="chat-quote">Great question!</blockquote><strong>Diffusion</strong> is...<hr class="chat-rule">✅ Key exam words: <strong>net</strong>');

// ── Round 2 (Mide, 9 Oct 2026): the allow-list ─────────────────────────
// Allowed, bare: sub sup b strong em i br p ul ol li.
check("<sub> formula renders", f("H<sub>2</sub>SO<sub>4</sub>"), "H<sub>2</sub>SO<sub>4</sub>");
check("<sup> renders", f("10<sup>-3</sup> m"), "10<sup>-3</sup> m");
check("<b> <strong> <em> <i>", f("<b>a</b> <strong>b</strong> <em>c</em> <i>d</i>"),
      "<b>a</b> <strong>b</strong> <em>c</em> <i>d</i>");
check("<br>, <br/>, <br /> all one <br>", f("a<br>b<br/>c<br />d"), "a<br>b<br>c<br>d");
check("upper-case tag is canonical lower", f("CO<SUB>2</SUB>"), "CO<sub>2</sub>");
check("Unicode subscripts untouched", f("CO₂ and H₂SO₄"), "CO₂ and H₂SO₄");
check("an HTML list renders, no stray <br>", f("<ul>\n<li>a</li>\n<li>b</li>\n</ul>\nAfter"),
      "<ul><li>a</li><li>b</li></ul>After");
check("<p> renders", f("<p>One</p><p>Two</p>"), "<p>One</p><p>Two</p>");
// Everything else is text.
check("<script> is text", f("<script>alert(1)</script>"), "&lt;script&gt;alert(1)&lt;/script&gt;");
check("<img onerror> is text", f('<img src=x onerror="alert(1)">'), '&lt;img src=x onerror="alert(1)"&gt;');
check("<a href=javascript:> is text", f('<a href="javascript:alert(1)">x</a>'),
      '&lt;a href="javascript:alert(1)"&gt;x&lt;/a&gt;');
check("<svg onload> is text", f("<svg onload=alert(1)>"), "&lt;svg onload=alert(1)&gt;");
check("<sub onclick> is text (no attributes, ever)", f('<sub onclick="alert(1)">2</sub>'),
      '&lt;sub onclick="alert(1)"&gt;2');
check("<b style> is text", f('<b style="color:red">x</b>'), '&lt;b style="color:red"&gt;x');
check("<i class> is text", f('<i class=x>y</i>'), "&lt;i class=x&gt;y");
check("<iframe> / <style> / <object> are text", f("<iframe></iframe><style></style><object>"),
      "&lt;iframe&gt;&lt;/iframe&gt;&lt;style&gt;&lt;/style&gt;&lt;object&gt;");
check("<img> is not <i>", f("<img>"), "&lt;img&gt;");
check("<bdo>/<big>/<button> are not <b>", f("<bdo><big><button>"), "&lt;bdo&gt;&lt;big&gt;&lt;button&gt;");
check("<pre>/<param> are not <p>", f("<pre><param>"), "&lt;pre&gt;&lt;param&gt;");
check("<summary>/<svg> are not <sub>/<sup>", f("<summary><supx>"), "&lt;summary&gt;&lt;supx&gt;");
check("a tag split by a newline is text", f("<b\nonclick=x>"), "&lt;b<br>onclick=x&gt;");
check("a tag smuggled round an allowed one", f("<scr<b>ipt>alert(1)</scr</b>ipt>"),
      "&lt;scr<b>ipt&gt;alert(1)&lt;/scr</b>ipt&gt;");
// Balancing.
check("unclosed tag is closed at the end", f("<b>bold to the end"), "<b>bold to the end</b>");
check("stray close is dropped", f("text</strong> more</li>"), "text more");
check("misnested tags are re-nested", f("<b><i>x</b>y</i>"), "<b><i>x</i></b>y");
check("</br> is dropped", f("a</br>b"), "ab");
// Entities stay text.
check("&lt;script&gt; stays text", f("&lt;script&gt;alert(1)&lt;/script&gt;"),
      "&amp;lt;script&amp;gt;alert(1)&amp;lt;/script&amp;gt;");
check("&#60;script&#62; stays text", f("&#60;script&#62;"), "&amp;#60;script&amp;#62;");
check("placeholder characters in the reply are stripped", f("a0b<b>c</b>"), "a0b<b>c</b>");
// Markdown lists.
check("numbered list keeps its numbering across a blank line", f("1. one\n\n2. two\n\n3. three"),
      "<ol><li>one</li><li>two</li><li>three</li></ol>");
check("a list starting at 3 says so", f("3. three\n4. four"), '<ol start="3"><li>three</li><li>four</li></ol>');
check("bullets with * and • and bold", f("* **CO₂** gas\n• **H₂O** liquid"),
      "<ul><li><strong>CO₂</strong> gas</li><li><strong>H₂O</strong> liquid</li></ul>");
check("an indented line continues its item", f("1. Add acid\n   until it stops fizzing\n2. Filter"),
      "<ol><li>Add acid<br>until it stops fizzing</li><li>Filter</li></ol>");
check("an indented bullet is a nested list", f("1. Steps\n   - heat\n   - stir\n2. Done"),
      "<ol><li>Steps<ul><li>heat</li><li>stir</li></ul></li><li>Done</li></ol>");
check("text, list, text", f("Here:\n\n- a\n- b\n\nThat's it"), "Here:<ul><li>a</li><li>b</li></ul>That's it");
check("**bold** at a line start is not a bullet", f("**Key words:**\n- a"),
      "<strong>Key words:</strong><ul><li>a</li></ul>");
check("a number mid-line is not a list", f("It was 1. odd"), "It was 1. odd");
check("2.5 g is not a list", f("2.5 g of salt"), "2.5 g of salt");
check("--- after a list is still a rule", f("- a\n\n---\n\nb"), '<ul><li>a</li></ul><hr class="chat-rule">b');
check("script inside a list item is text", f("- <script>x</script>\n- H<sub>2</sub>"),
      "<ul><li>&lt;script&gt;x&lt;/script&gt;</li><li>H<sub>2</sub></li></ul>");
// A reply mixing allowed tags with Markdown.
check("allowed tags and Markdown together",
      f("> Nice one!\n\n**Formulae:** CO<sub>2</sub> and H<sub>2</sub>SO<sub>4</sub>\n\n1. **Add** acid<br>slowly\n2. <i>Filter</i>\n\n---\n\n<b>Done</b> <img src=x onerror=alert(1)>"),
      '<blockquote class="chat-quote">Nice one!</blockquote><strong>Formulae:</strong> CO<sub>2</sub> and H<sub>2</sub>SO<sub>4</sub><ol><li><strong>Add</strong> acid<br>slowly</li><li><i>Filter</i></li></ol><hr class="chat-rule"><b>Done</b> &lt;img src=x onerror=alert(1)&gt;');
// The real model replies captured from /api/chat on 9 Oct 2026 (TEST backend).
check("real reply: formulae + bullets",
      f('Hey! Great question to start with 🙌\n\n**Carbon dioxide:** CO₂\n\n**Sulfuric acid:** H₂SO₄\n\n---\n\n**Quick breakdown:**\n\n- CO₂ → 1 carbon + 2 oxygen atoms\n- H₂SO₄ → 2 hydrogen + 1 sulfur + 4 oxygen atoms\n\nWant me to walk you through it? 🔥'),
      'Hey! Great question to start with 🙌<br><br><strong>Carbon dioxide:</strong> CO₂<br><br><strong>Sulfuric acid:</strong> H₂SO₄<hr class="chat-rule"><strong>Quick breakdown:</strong><ul><li>CO₂ → 1 carbon + 2 oxygen atoms</li><li>H₂SO₄ → 2 hydrogen + 1 sulfur + 4 oxygen atoms</li></ul>Want me to walk you through it? 🔥');

// ── Round 3 (9 Oct 2026): Markdown tables, drawn with allowed tags only ──
// No table elements on the allow-list: the separator row goes, the header is
// one bold line, each body row is a list item with its cells joined by " — ".
const TBL = "<strong>Substance — Formula</strong><ul><li>Carbon dioxide — CO₂</li><li>Sulfuric acid — H₂SO₄</li></ul>";
check("real reply: a Markdown table",
      f("| Substance | Formula |\n|---|---|\n| Carbon dioxide | CO₂ |\n| Sulfuric acid | H₂SO₄ |"), TBL);
check("real reply: **bold** inside a cell",
      f("| Substance | Formula |\n|---|---|\n| Carbon dioxide | **CO₂** |\n| Sulfuric acid | H₂SO₄ |"),
      "<strong>Substance — Formula</strong><ul><li>Carbon dioxide — <strong>CO₂</strong></li><li>Sulfuric acid — H₂SO₄</li></ul>");
check("real reply: the whole table collapsed onto one line",
      f("| Substance | Formula | |-----------|---------| | Carbon dioxide | CO₂ | | Sulfuric acid | H₂SO₄ |"), TBL);
check("no outer pipes, alignment colons, three columns, prose round it",
      f("Here:\n\nSubstance | Formula | State\n:---|:---:|---:\nWater | H₂O | liquid\n\nDone"),
      "Here:<br><br><strong>Substance — Formula — State</strong><ul><li>Water — H₂O — liquid</li></ul>Done");
check("one-line table with prose before and after, <sub> in a cell",
      f("Here you go: | Substance | Formula | |---|---| | Carbon dioxide | CO<sub>2</sub> | | Water | H₂O | Hope that helps!"),
      "Here you go:<br><strong>Substance — Formula</strong><ul><li>Carbon dioxide — CO<sub>2</sub></li><li>Water — H₂O</li></ul>Hope that helps!");
check("header on its own line, separator and rows collapsed",
      f("| Substance | Formula |\n|---|---| | Carbon dioxide | CO₂ | | Sulfuric acid | H₂SO₄ |"), TBL);
check("a table ends at a line with no pipe", f("| a | b |\n|---|---|\n| c | d |\nAfter"),
      "<strong>a — b</strong><ul><li>c — d</li></ul>After");
check("an escaped pipe is a literal pipe in a cell", f("| a \\| b | c |\n|---|---|\n| x | y |"),
      "<strong>a | b — c</strong><ul><li>x — y</li></ul>");
check("an empty cell is skipped, not a dangling dash", f("| Ion | Charge |\n|---|---|\n| Na | +1 |\n| Cl |  |"),
      "<strong>Ion — Charge</strong><ul><li>Na — +1</li><li>Cl</li></ul>");
check("a lone | in prose is not a table", f("Use |x| for size, and a | b here"), "Use |x| for size, and a | b here");
check("pipe lines with no separator are not a table", f("a | b\nc | d"), "a | b<br>c | d");
check("a separator with a different column count is not a table", f("| a | b | c |\n|---|---|\n| x | y |"),
      "| a | b | c |<br>|---|---|<br>| x | y |");
check("a --- rule is still a rule, not a separator", f("a | b\n---\nc"), 'a | b<hr class="chat-rule">c');
check("script and attributes in a cell are text", f("| Metal | Note |\n|---|---|\n| <script>x</script> | <b onclick=1>y</b> |"),
      "<strong>Metal — Note</strong><ul><li>&lt;script&gt;x&lt;/script&gt; — &lt;b onclick=1&gt;y</li></ul>");

// No reply, however hostile, may produce an attribute or a tag outside the list
// other than the ones formatReply writes itself.
const OWN = /^<(\/?(sub|sup|b|strong|em|i|br|p|ul|ol|li|code|blockquote)|hr class="chat-rule"|blockquote class="chat-quote"|ol start="\d+")>$/;
const hostile = ["<script>", "<img src=x onerror=1>", "<svg/onload=1>", "<sub onclick=1>", "<b style=x>",
  "<a href=javascript:1>", "<<b>script>", "<p\tonclick=1>", "<li/onclick=1>", "<ol start=1>", "<iframe srcdoc=x>",
  "</textarea><script>", "<!--", "| <b> | x |\n|---|---|", "|---|---| | <i onclick=1> |", "<![CDATA[", "<math><mi>", "\"><script>", "`<b>`", "<br onmouseover=1>"];
let fuzzBad = 0;
for (let n = 0; n < 2000; n++) {
  let s = "";
  for (let k = 0; k < 6; k++) s += hostile[(n * 7 + k * 13) % hostile.length] + (k % 2 ? "\n- " : " **x** ");
  const html = f(s);
  for (const tag of html.match(/<[^>]*>/g) || []) if (!OWN.test(tag)) { fuzzBad++; if (fuzzBad < 4) console.log("  FAIL  fuzz", JSON.stringify(s), tag); }
}
check("fuzz: 2000 hostile replies emit only formatReply's own tags", fuzzBad, 0);

// shared/tutor-panel.css is a scoped second copy of styles.css's chat rules
// (KS4 lesson pages do not load styles.css). Every chat selector styles.css
// draws must be drawn there too.
{
  const css = fs.readFileSync(path.join(__dirname, "..", "shared", "styles.css"), "utf8");
  const panel = fs.readFileSync(path.join(__dirname, "..", "shared", "tutor-panel.css"), "utf8");
  const a = css.indexOf("/* ── CHAT OVERLAY ── */"), b = css.indexOf("/* ── PATHWAY CARDS");
  const block = css.slice(a, b).replace(/\/\*[\s\S]*?\*\//g, "").replace(/@keyframes[^{]*\{(?:[^{}]*\{[^}]*\})*[^}]*\}/g, "");
  const missing = [];
  for (const m of block.matchAll(/([^{}]+)\{[^}]*\}/g)) {
    for (let sel of m[1].split(",")) {
      sel = sel.trim().replace(/\s+/g, " ");
      if (!sel) continue;
      const scoped = sel.startsWith(".chat-overlay") ? "#chatOverlay" + sel : "#chatOverlay " + sel;
      if (!panel.includes(scoped)) missing.push(sel);
    }
  }
  check("tutor-panel.css draws every chat selector styles.css does", missing.join(" | "), "");
}

console.log(failures ? `\n${failures} FAILED` : "\nall passed");
process.exit(failures ? 1 : 0);
