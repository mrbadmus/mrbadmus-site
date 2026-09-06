/* mrb327_safari_drive_fixcheck.js — MRB-327 §2.
 *
 * A. The termly report scrolls sideways on a phone. Reproduce it, then apply
 *    the proposed rule IN THE PAGE and re-measure, so the diff handed to the
 *    commander comes with proof rather than an assertion.
 * B. The unit-check layout numbers differed between engines. Show that the
 *    cause is the question SHUFFLE (a different attempt draws different
 *    questions) and not the engine, by taking two attempts in ONE engine and
 *    finding the same spread.
 */
const fs=require('fs'),path=require('path'),playwright=require('playwright');
const SCRATCH='/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-mrbadmus-worktrees-b2c-launch/06d799b1-12f9-481b-9871-424a2321715f/scratchpad';
const STATE=JSON.parse(fs.readFileSync(path.join(SCRATCH,'safari_fixtures.json'),'utf8'));
const BASE='http://localhost:8171',API='http://localhost:3100';
const SB_KEY='sb-qeppkiswvclkkwbxmlok-auth-token';
const ENGINE=process.argv[process.argv.indexOf('--engine')+1]||'webkit';
const SHOTS=path.join(SCRATCH,'shots','safari',ENGINE); fs.mkdirSync(SHOTS,{recursive:true});
const FLAG=`(function(){var c=null;Object.defineProperty(window,'MrBadmusConfig',{configurable:true,get:function(){return c;},set:function(v){if(v&&typeof v==='object'){v.CONSUMER_SIGNUP_ENABLED=true;}c=v;}});})();`;
const qs=(p)=>BASE+p+(p.includes('?')?'&':'?')+'env=test&api='+API;

/* The proposed rule, exactly as the diff would add it to report.html's
   <style>. Below 560px four stat boxes cannot each hold their widest word
   and stay inside an A4 sheet scaled to a phone, so they go two-up. Print is
   untouched — the @media print block is later and the sheet is 794px wide
   there, so this query never applies to paper. */
const PROPOSED = `@media (max-width: 560px) {
  .rpt-stats { grid-template-columns: repeat(2, 1fr) !important; }
}`;

const OV = `(function(){
  var vw=document.documentElement.clientWidth, se=document.scrollingElement||document.documentElement;
  var over=[]; var all=document.querySelectorAll('body *');
  for(var i=0;i<all.length;i++){var el=all[i],cs=getComputedStyle(el);
    if(cs.display==='none'||cs.visibility==='hidden'||cs.position==='fixed')continue;
    var r=el.getBoundingClientRect(); if(r.width<1||r.height<1)continue;
    if(r.right>vw+1) over.push({cls:String(el.className||'').slice(0,30),right:Math.round(r.right),
      text:(el.textContent||'').replace(/\s+/g,' ').trim().slice(0,40)});}
  return {overflowX:Math.round(se.scrollWidth-se.clientWidth),count:over.length,over:over.slice(0,6)};
})()`;

(async()=>{
const b=await playwright[ENGINE].launch();
console.log('\n══ fixcheck '+ENGINE+' '+b.version()+' ══');
const ctx=await b.newContext({viewport:{width:390,height:844}});
await ctx.addInitScript(FLAG);
const s=await ctx.newPage();
await s.goto(BASE+'/404.html?env=test');
await s.evaluate(([k,v])=>{localStorage.clear();localStorage.setItem(k,v);},[SB_KEY,JSON.stringify(STATE.parent_session)]);
await s.close();

const p=await ctx.newPage();
await p.goto(qs('/consumer/report.html?child='+STATE.child+'&term=autumn-2026'),{waitUntil:'networkidle'});
await p.waitForFunction(()=>/Amara/.test(document.body.innerText),null,{timeout:20000}).catch(()=>{});
await p.waitForTimeout(800);

const before=await p.evaluate(OV);
await p.screenshot({path:path.join(SHOTS,'A1-report-390-BEFORE.png'),fullPage:true});
console.log('  BEFORE overflowX='+before.overflowX+' offenders='+before.count);
before.over.forEach(o=>console.log('    ',JSON.stringify(o)));

// Tag the stat row the way the diff does, then add the proposed rule.
const tagged=await p.evaluate(()=>{
  var g=Array.from(document.querySelectorAll('.rpt-keep')).find(function(e){
    return getComputedStyle(e).display==='grid' && /Sessions|Time on task|Unit checks|Best streak/.test(e.textContent||'');});
  if(!g) return null;
  g.classList.add('rpt-stats');
  return {cols:getComputedStyle(g).gridTemplateColumns, boxes:g.children.length};
});
await p.addStyleTag({content:PROPOSED});
await p.waitForTimeout(400);
const after=await p.evaluate(OV);
const afterCols=await p.evaluate(()=>{var g=document.querySelector('.rpt-stats');
  return g?{cols:getComputedStyle(g).gridTemplateColumns,h:Math.round(g.getBoundingClientRect().height),
            right:Math.round(g.getBoundingClientRect().right)}:null;});
await p.screenshot({path:path.join(SHOTS,'A2-report-390-AFTER.png'),fullPage:true});
console.log('  tagged '+JSON.stringify(tagged));
console.log('  AFTER  overflowX='+after.overflowX+' offenders='+after.count+' '+JSON.stringify(afterCols));

// The fix must not reach paper. Print media, A4 viewport, rule still loaded.
await p.setViewportSize({width:794,height:1123});
await p.emulateMedia({media:'print'});
await p.waitForTimeout(400);
const print=await p.evaluate(()=>{var g=document.querySelector('.rpt-stats');
  var se=document.scrollingElement||document.documentElement;
  return {cols:g?getComputedStyle(g).gridTemplateColumns:null,
          pages:Math.ceil(se.scrollHeight/1123), overflowX:Math.round(se.scrollWidth-se.clientWidth)};});
console.log('  PRINT (A4, rule loaded) '+JSON.stringify(print));
await p.emulateMedia({media:'screen'});
await p.close();
await ctx.close();

// ── B. two unit-check attempts in ONE engine ────────────────────────────
const cctx=await b.newContext({viewport:{width:390,height:844}});
await cctx.addInitScript(FLAG);
const seen=[];
try{
  const lg=await cctx.newPage();
  await lg.goto(qs('/go/index.html'),{waitUntil:'networkidle'});
  await lg.fill('#gl-user',STATE.child_username); await lg.fill('#gl-pass',STATE.child_password);
  await lg.click('#gl-go');
  await lg.waitForURL(/today\.html/,{timeout:25000});
  await lg.close();
  for(let i=0;i<2;i++){
    const u=await cctx.newPage();
    await u.goto(qs('/consumer/unit-check.html?unit=B1'),{waitUntil:'networkidle'});
    await u.waitForSelector('#uc-start',{timeout:20000});
    await u.click('#uc-start');
    await u.waitForFunction(()=>{var t=document.getElementById('uc-timer');return t&&!t.hidden;},null,{timeout:20000});
    await u.waitForTimeout(900);
    const q=await u.evaluate(()=>{
      var se=document.scrollingElement||document.documentElement;
      return {q1:(document.body.innerText.match(/QUESTION 1 OF 10[^]*/)||[''])[0].replace(/\s+/g,' ').slice(0,110),
              h1h:Math.round((document.querySelector('h1')||{getBoundingClientRect:()=>({height:0})}).getBoundingClientRect().height),
              scrollHeight:Math.round(se.scrollHeight)};});
    seen.push(q);
    console.log('  attempt '+(i+1)+' h1h='+q.h1h+' scrollH='+q.scrollHeight+'  '+q.q1.slice(0,80));
    await u.close();
  }
}catch(e){ console.log('  (unit-check pass skipped: '+String(e.message).slice(0,80)+')'); }
await cctx.close();
await b.close();
fs.writeFileSync(path.join(SCRATCH,'safari_fixcheck_'+ENGINE+'.json'),
  JSON.stringify({before,tagged,after,afterCols,print,unitAttempts:seen},null,1));
})().catch(e=>{console.error('FATAL',e);process.exit(1);});
