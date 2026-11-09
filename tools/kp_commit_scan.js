#!/usr/bin/env node
/* Every option group on a rebuilt KS4 lesson whose answers are locked in by a
   separate press (a "Close the switch" that a pick switches on), named by reading
   the lesson's own code: a *Locked/*Off/*Disabled flag that goes from true to false
   once every item in the group has a pick. A group ROOT_FORMS covers is left out, so
   whatever this prints is posting per tap before its commit. One slug per line in,
   one `slug group flips` line out. Run from the repo root by activity_save_drive --commits. */
const fs = require('fs'), path = require('path'), vm = require('vm');
process.argv[2] = process.argv[2] || '.';
let src = fs.readFileSync('tools/activity_save_coverage.js', 'utf8');
src = src.slice(0, src.indexOf('const out = {};')).replace('const pages = fs.readFileSync(0, "utf8").split("\\n").map((s) => s.trim()).filter(Boolean);', 'const pages = [];');
eval(src.replace(/^#!.*\n/, '').replace(/"use strict";/, '').replace(/const (fs|path|vm) =[^\n]*\n/g, '') + 'global.__mk=makeContext;global.__ra=RA_SRC;');
const js = fs.readFileSync('shared/mrbadmus.v2.js', 'utf8');
const a = js.indexOf('/* <ks4-root-forms> */'), b = js.indexOf('/* </ks4-root-forms> */');
const covers = {};
let cur = null;
for (const line of js.slice(a, b).split('\n')) {
  const m = /^\s{8}'([a-z0-9-]+)':/.exec(line);
  if (m) { cur = m[1]; }
  if (cur) { for (const c of line.matchAll(/covers: \[([^\]]*)\]/g)) { for (const w of c[1].matchAll(/'([^']+)'/g)) { (covers[cur] = covers[cur] || {})[w[1]] = 1; } } }
}
for (const p of fs.readFileSync(0, 'utf8').split('\n').filter(Boolean)) {
  const html = fs.readFileSync(p, 'utf8'), slug = path.basename(p, '.html'), sb = __mk(p), re = /<script>([\s\S]*?)<\/script>/g;
  let m, L, vals, RA;
  try {
    while ((m = re.exec(html))) { if (/MrBadmusKS4Runtime\.mount|KS4_BLOCKS/.test(m[1])) { vm.runInContext(m[1], sb); } }
    vm.runInContext(__ra + '\n;globalThis.__RA = KS4RootActs;', sb);
    RA = sb.__RA;
    if (!sb.__mounted) { continue; }
    L = new sb.__mounted.Component(sb.__mounted.props);
    try { if (L.componentDidMount) { L.componentDidMount(); } } catch (e) { /* the lesson's own */ }
    L.state = Object.assign({}, L.state, { libReady: true });
    vals = RA.valsAt(L, RA.clone(L.state));
  } catch (e) { continue; }
  const init = RA.clone(L.state);
  for (const g of RA.groupsOf(sb.__mounted.template)) {
    if ((covers[slug] || {})[g.e]) { continue; }
    const ois = g.inner ? [...new Set(RA.itemsOf(g, vals).map((x) => x.oi))] : [null];
    let r;
    try { r = RA.analyse(L, g, init, init, ois[0]); } catch (e) { continue; }
    if (!['pick', 'gate', 'multi'].includes(r.kind)) { continue; }
    let st = RA.clone(init);
    for (const oj of ois) { const op = RA.probe(L, g, st, oj).filter((x) => x.patch && x.ws.length); if (op[0]) { st = RA.apply(st, op[0].patch); } }
    const v1 = RA.valsAt(L, st), flips = [];
    for (const k in vals) { if (/Locked$|Off$|Disabled$/.test(k) && vals[k] === true && v1[k] === false) { flips.push(k); } }
    if (flips.length) { console.log(slug, g.e, flips.join(',')); }
  }
}
