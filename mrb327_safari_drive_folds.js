/* mrb327_safari_drive_folds.js — MRB-327 §2.1, the fold analysis done properly.
 *
 * The per-page screenshots in the first pass are viewport captures at scroll
 * offsets, and the browser CLAMPS the last scroll, so the final two images
 * overlap and are not the real page boxes. This measures the folds in DOCUMENT
 * coordinates instead — where each A4 fold lands and what it cuts through —
 * which is the thing the print question actually asks.
 */
const fs=require('fs'),path=require('path'),playwright=require('playwright');
const SCRATCH='/private/tmp/claude-501/-Users-midebadmus-Documents-GitHub-mrbadmus-worktrees-b2c-launch/06d799b1-12f9-481b-9871-424a2321715f/scratchpad';
const STATE=JSON.parse(fs.readFileSync(path.join(SCRATCH,'safari_fixtures.json'),'utf8'));
const BASE='http://localhost:8171',API='http://localhost:3100',SB_KEY='sb-qeppkiswvclkkwbxmlok-auth-token';
const ENGINE=process.argv[process.argv.indexOf('--engine')+1]||'webkit';
const SHOTS=path.join(SCRATCH,'shots','safari',ENGINE); fs.mkdirSync(SHOTS,{recursive:true});
const FLAG=`(function(){var c=null;Object.defineProperty(window,'MrBadmusConfig',{configurable:true,get:function(){return c;},set:function(v){if(v&&typeof v==='object'){v.CONSUMER_SIGNUP_ENABLED=true;}c=v;}});})();`;
const qs=(p)=>BASE+p+(p.includes('?')?'&':'?')+'env=test&api='+API;

(async()=>{
const b=await playwright[ENGINE].launch();
console.log('\n══ folds '+ENGINE+' '+b.version()+' ══');
const ctx=await b.newContext({viewport:{width:794,height:1123}});
await ctx.addInitScript(FLAG);
const s=await ctx.newPage();
await s.goto(BASE+'/404.html?env=test');
await s.evaluate(([k,v])=>{localStorage.clear();localStorage.setItem(k,v);},[SB_KEY,JSON.stringify(STATE.parent_session)]);
await s.close();

const p=await ctx.newPage();
await p.goto(qs('/consumer/report.html?child='+STATE.child+'&term=autumn-2026'),{waitUntil:'networkidle'});
await p.waitForFunction(()=>/Amara/.test(document.body.innerText),null,{timeout:20000}).catch(()=>{});
await p.emulateMedia({media:'print'});
await p.waitForTimeout(600);

const folds=await p.evaluate(()=>{
  var PAGE_H=1123, PAGE_W=794;
  var se=document.scrollingElement||document.documentElement;
  var docTop=se.scrollTop;                       // measure from wherever we are
  var H=se.scrollHeight, nPages=Math.ceil(H/PAGE_H);
  var report=[];
  // Only leaf-ish blocks: a paragraph, a row, a heading, a figure. A wrapper
  // spanning the whole document "crossing a fold" says nothing.
  var els=Array.from(document.querySelectorAll('.rpt-sheet *')).filter(function(e){
    var c=getComputedStyle(e);
    if(c.display==='none'||c.visibility==='hidden')return false;
    var r=e.getBoundingClientRect(); if(r.width<1||r.height<1)return false;
    return r.height<PAGE_H*0.9;                  // not a page-sized container
  });
  for(var f=1;f<nPages;f++){
    var y=f*PAGE_H;
    var cut=[];
    els.forEach(function(e){
      var r=e.getBoundingClientRect();
      var top=r.top+docTop, bot=top+r.height;
      if(top<y-0.5 && bot>y+0.5){
        var c=getComputedStyle(e);
        // how badly: how much of the element is on each side of the fold
        cut.push({tag:e.tagName.toLowerCase(), cls:String(e.className||'').slice(0,26),
          h:Math.round(r.height), above:Math.round(y-top), below:Math.round(bot-y),
          protects:/avoid/.test(c.breakInside||'')||/avoid/.test(c.pageBreakInside||''),
          text:(e.textContent||'').replace(/\s+/g,' ').trim().slice(0,55)});
      }
    });
    // The worst cut is the innermost element — the one with no cut child.
    report.push({fold:f, atY:y, cutCount:cut.length, cuts:cut.slice(-6)});
  }
  // Where every section heading sits relative to its fold.
  var heads=Array.from(document.querySelectorAll('.rpt-h2')).map(function(h){
    var r=h.getBoundingClientRect(), top=r.top+docTop;
    var page=Math.floor(top/PAGE_H)+1, spaceBelow=PAGE_H-(top%PAGE_H);
    return {text:h.textContent.trim().slice(0,30), docY:Math.round(top), page:page,
            spaceBelowOnPage:Math.round(spaceBelow),
            /* a heading with less than ~90px under it is stranded at the
               bottom of a page with its section starting on the next */
            stranded: spaceBelow < 90};
  });
  return {docHeight:Math.round(H), pageBox:{w:PAGE_W,h:PAGE_H}, pages:nPages,
          lastPageUsed:Math.round(H%PAGE_H||PAGE_H), folds:report, headings:heads};
});

console.log('  doc='+folds.docHeight+'px → '+folds.pages+' A4 pages (last page uses '+folds.lastPageUsed+'px)');
folds.folds.forEach(f=>{
  console.log('  fold '+f.fold+' at y='+f.atY+' cuts '+f.cutCount+' element(s):');
  f.cuts.forEach(c=>console.log('     '+(c.protects?'⚠PROTECTED ':'           ')+
    c.tag+'.'+c.cls+' h='+c.h+' ('+c.above+' above / '+c.below+' below) “'+c.text+'”'));
});
folds.headings.forEach(h=>console.log('  heading “'+h.text+'” page '+h.page+
  ' with '+h.spaceBelowOnPage+'px under it'+(h.stranded?'  ⚠ STRANDED':'')));

await p.emulateMedia({media:'screen'});
await p.close(); await ctx.close(); await b.close();
fs.writeFileSync(path.join(SCRATCH,'safari_folds_'+ENGINE+'.json'),JSON.stringify(folds,null,1));
})().catch(e=>{console.error('FATAL',e);process.exit(1);});
