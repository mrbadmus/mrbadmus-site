#!/usr/bin/env node
/* kp_root_forms.js — the question stems ROOT_FORMS sends, for the tagger.
 *
 *     node tools/kp_root_forms.js REPO
 *
 * prints {slug: [{id, text}]}. A form's rows are `ks4:<slug>:<route>#<id>` or
 * `…#<id>-<entry>`; the entry is often the child's own (a run number, a tube),
 * so the tag lives on the stem and the backend's kpOf falls back to it. Runs the
 * `<ks4-root-forms>` block of shared/mrbadmus.v2.js for the ids, and reads each
 * form's own words (its `q:`, else its other long strings) from the table text.
 */
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const js = fs.readFileSync(path.join(process.argv[2] || '.', 'shared', 'mrbadmus.v2.js'), 'utf8');
const A = '/* <ks4-root-forms> */', Z = '/* </ks4-root-forms> */';
const block = js.slice(js.indexOf(A) + A.length, js.indexOf(Z));
const box = { same: () => false, KS4RootActs: {}, console };
vm.runInNewContext(block + '\nthis.__forms = ROOT_FORMS;', box);
const forms = box.__forms;

// The table's array elements, by slug: strings and regexes never count as brackets.
function elements(src, at) {
  const out = [];
  let depth = 0, start = -1, prev = '';
  for (let i = at; i < src.length; i += 1) {
    const c = src[i];
    if (c === "'" || c === '"' || c === '`') {
      for (i += 1; src[i] !== c; i += 1) { if (src[i] === '\\') { i += 1; } }
      prev = c;
      continue;
    }
    if (c === '/' && src[i + 1] === '/') { i = src.indexOf('\n', i); continue; }
    if (c === '/' && src[i + 1] === '*') { i = src.indexOf('*/', i) + 1; continue; }
    if (c === '/' && /[(,:=!&|?\[{;]/.test(prev)) {
      for (i += 1; src[i] !== '/'; i += 1) {
        if (src[i] === '\\') { i += 1; } else if (src[i] === '[') { while (src[i] !== ']') { if (src[i] === '\\') { i += 1; } i += 1; } }
      }
      prev = '/';
      continue;
    }
    if (/\s/.test(c)) { continue; }
    if (c === '[' || c === '{' || c === '(') {
      if (depth === 1 && start < 0) { start = i; }
      depth += 1;
    } else if (c === ']' || c === '}' || c === ')') {
      depth -= 1;
      if (depth === 1 && start >= 0) { out.push(src.slice(start, i + 1)); start = -1; }
      if (depth === 0) { return out; }
    } else if (depth === 1 && start < 0 && c !== ',') {
      start = i;
    }
    prev = c;
  }
  return out;
}
function literals(s) {
  const re = /'((?:[^'\\]|\\.)*)'/g, out = [];
  let m;
  while ((m = re.exec(s))) { out.push(m[1].replace(/\\(.)/g, '$1')); }
  return out;
}
function words(el) {
  const q = /\bq:\s*'((?:[^'\\]|\\.)*)'/.exec(el);
  if (q) { return q[1].replace(/\\(.)/g, '$1'); }
  return literals(el).filter((t) => t.length >= 12).slice(0, 4).join(' / ');
}

const res = {};
Object.keys(forms).forEach((slug) => {
  const at = block.search(new RegExp("'" + slug + "':\\s*\\["));
  const els = at < 0 ? [] : elements(block, block.indexOf('[', at));
  const seen = new Set();
  res[slug] = [];
  forms[slug].forEach((f, i) => {
    if (seen.has(f.id)) { return; }
    seen.add(f.id);
    const el = els.length === forms[slug].length ? els[i] : els.join(' ');
    res[slug].push({ id: f.id, text: words(el || '') });
  });
});
process.stdout.write(JSON.stringify(res));
