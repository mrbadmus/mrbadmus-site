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
check("lists stay as lines", f("- one\n- two\n1. three"), "- one<br>- two<br>1. three");
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

console.log(failures ? `\n${failures} FAILED` : "\nall passed");
process.exit(failures ? 1 : 0);
