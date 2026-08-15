// Lift a Design-delivered KS3 lesson page's authored payload, byte-identical.
//
// Design hand-writes each B1 lesson as a standalone HTML file whose content
// lives in a `<script type="text/x-dc" data-dc-script>` block as plain JS
// object literals. The b1-inventory files are emphatic that this payload must
// be "lifted byte-identical from these lines, not retyped" — roughly 12,000
// words of science-bearing copy across the six lessons, every one of which
// crosses Mide's examiner gate. Retyping it by hand is the single largest
// source of silent drift available to this build.
//
// So: evaluate the authored constants in a sandbox and print them as JSON. The
// strings that reach ks3_data/ are then the strings Design wrote, character for
// character, and any difference is a diff rather than a typo nobody notices.
//
//   node tools/extract_design_payload.js <page.dc.html> [CONST ...]
//
// With no CONST names, dumps every top-level `const NAME = ...` the block
// declares. Output is JSON on stdout; diagnostics go to stderr so the stdout
// stream stays pipeable into a Python reader.

const fs = require('fs');
const vm = require('vm');

const file = process.argv[2];
if (!file) {
  console.error('usage: node extract_design_payload.js <page.dc.html> [CONST ...]');
  process.exit(2);
}

const src = fs.readFileSync(file, 'utf8');
const m = src.match(/<script type="text\/x-dc" data-dc-script[^>]*>([\s\S]*?)<\/script>/);
if (!m) {
  console.error('no <script data-dc-script> block in ' + file);
  process.exit(1);
}
const body = m[1];

// The block also defines the component function and calls DC runtime helpers
// that do not exist outside Design's viewer. We only want the data constants,
// so evaluate up to the first function/JSX declaration and let the rest go.
const wanted = process.argv.slice(3);
const declared = [...body.matchAll(/^const ([A-Z][A-Z0-9_]*)\s*=/gm)].map(x => x[1]);
const names = wanted.length ? wanted : declared;

// Evaluate each constant's own initialiser in isolation, so one construct the
// sandbox cannot run never costs us the others. Constants may reference earlier
// ones (b1-06's BACTERIA is built from a seeded LCG), so they share a context
// and are evaluated in declaration order.
const ctx = vm.createContext({ Math, JSON, Array, Object, String, Number, Boolean, Date: undefined });
const out = {};
const failed = {};

// Find the end of a declaration's initialiser by balancing brackets from the
// `=`, skipping over string and comment content. A heuristic "slice to the next
// top-level const" overruns whenever a page declares a helper between two data
// constants — which b1-02 does, and which cost SELF_RUNGS on the first pass.
function initialiserEnd(text, eq) {
  let depth = 0, i = eq + 1, str = null, started = false;
  while (i < text.length) {
    const c = text[i], n = text[i + 1];
    if (str) {
      if (c === '\\') { i += 2; continue; }
      if (c === str) { str = null; }
      i++; continue;
    }
    if (c === '"' || c === "'" || c === '`') { str = c; i++; continue; }
    if (c === '/' && n === '/') { const nl = text.indexOf('\n', i); i = nl < 0 ? text.length : nl; continue; }
    if (c === '/' && n === '*') { const e = text.indexOf('*/', i); i = e < 0 ? text.length : e + 2; continue; }
    if (c === '[' || c === '{' || c === '(') { depth++; started = true; i++; continue; }
    if (c === ']' || c === '}' || c === ')') {
      depth--; i++;
      if (started && depth === 0) return i;
      continue;
    }
    // A bare scalar initialiser (`const N = 180;`) ends at the newline.
    if (!started && (c === ';' || c === '\n')) return i;
    i++;
  }
  return text.length;
}

for (const name of declared) {
  const re = new RegExp('^const ' + name + '\\s*=', 'm');
  const mm = body.match(re);
  if (!mm) continue;
  const start = mm.index;
  const eq = body.indexOf('=', start);
  // `const` in a vm script is a LEXICAL binding — it never becomes a property
  // of the context, so ctx[name] would read undefined and every value would
  // vanish at JSON.stringify. `var` creates a real global property and persists
  // across runInContext calls, which is also what lets a later constant
  // reference an earlier one (b1-06 builds BACTERIA from a seeded LCG).
  const chunk = body.slice(start, initialiserEnd(body, eq)).replace(/^const /, 'var ');
  try {
    vm.runInContext(chunk, ctx, { timeout: 5000 });
    if (names.includes(name)) {
      if (ctx[name] === undefined) { failed[name] = 'evaluated to undefined'; }
      else { out[name] = ctx[name]; }
    }
  } catch (e) {
    if (names.includes(name)) failed[name] = String(e.message);
  }
}

for (const name of names) {
  if (!(name in out) && !(name in failed)) failed[name] = 'not declared in this page';
}

if (Object.keys(failed).length) {
  console.error('could not evaluate: ' + JSON.stringify(failed, null, 2));
}
console.error('extracted ' + Object.keys(out).length + ' of ' + names.length +
              ' constants from ' + file);
process.stdout.write(JSON.stringify(out, null, 2));
