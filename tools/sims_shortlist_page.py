#!/usr/bin/env python3
"""sims_shortlist_page.py: builds docs/lessons/SIMS-SHORTLIST.html from the drive's results.

Inputs (outside the repo):
  /private/tmp/claude-501/sims-shortlist/results.json   from tools/sims_shortlist_drive.py
  /private/tmp/claude-501/sims-shortlist/verdicts.json  {lesson path: {"verdict": ..., "line": ...}}

    python3 tools/sims_shortlist_page.py
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "/private/tmp/claude-501/sims-shortlist"
OUT_HTML = os.path.join(ROOT, "docs", "lessons", "SIMS-SHORTLIST.html")
OUT_IMG = os.path.join(ROOT, "docs", "lessons", "sims-shortlist")
IMG_W = 600

SUBJECTS = {"biology": "Biology", "chemistry": "Chemistry", "physics": "Physics"}


def esc(s):
    return html.escape(str(s), quote=True)


def nice(slug):
    return slug.replace("-", " ").capitalize()


def group_of(path):
    """('KS3', subject, unit) or ('KS4', subject, topic) from a lesson path."""
    parts = path.split("/")
    ks = parts[0].upper() if parts and parts[0].lower() in ("ks3", "ks4") else "KS3"
    subj = parts[1] if len(parts) > 1 else "other"
    unit = parts[2] if len(parts) > 3 else ""
    return ks, subj, unit


def downscale(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    try:
        from PIL import Image
        im = Image.open(src).convert("RGB")
        if im.width > IMG_W:
            im = im.resize((IMG_W, max(1, round(im.height * IMG_W / im.width))), Image.LANCZOS)
        im.save(dst, "JPEG", quality=55, optimize=True)
    except ImportError:
        subprocess.run(["sips", "-Z", str(IMG_W), "-s", "format", "jpeg", "-s", "formatOptions", "55",
                        src, "--out", dst], check=True, capture_output=True)


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:90]


def item_html(path, rec, verdict, imgs):
    title = rec.get("title") or nice(path.rsplit("/", 1)[-1].replace(".html", ""))
    routes = ""
    if path.startswith("ks4/"):
        routes = '<details><summary>Routes</summary><ul class="routes">%s</ul></details>' % "".join(
            "<li>%s</li>" % esc(r) for r in rec.get("routes_all", [rec.get("route", "")]))
    pics = "".join('<img src="%s" alt="%s" loading="lazy" width="300">' % (esc(i), esc(title + " simulation"))
                   for i in imgs) or '<p class="none">No simulation was found on this page.</p>'
    if verdict:
        v = '<p class="verdict"><strong>%s.</strong> %s</p>' % (esc(verdict.get("verdict", "")), esc(verdict.get("line", "")))
    else:
        v = '<p class="verdict pending">Verdict pending</p>'
    p = esc(path)
    return (
        '<article class="item" data-path="%s">'
        '<h4>%s</h4><p class="path">%s</p>%s'
        '<div class="shots">%s</div>%s'
        '<div class="btns"><button type="button" class="keep" aria-pressed="false">Keep</button>'
        '<button type="button" class="remove" aria-pressed="false">Remove</button></div>'
        '</article>' % (p, esc(title), p, routes, pics, v))


CSS = """
:root{--bg:#FBF3E6;--card:#fff;--ink:#221E1B;--mute:#6b625a;--line:#e3d6c1;--accent:#E4572E;--keep:#1f7a4d;--rm:#b3261e;--on:#fff}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#1a1613;--card:#26201b;--ink:#FBF3E6;--mute:#b5a999;--line:#40372e;--accent:#ff7a52;--keep:#3ec585;--rm:#ff8a80;--on:#1a1613}}
:root[data-theme="dark"]{--bg:#1a1613;--card:#26201b;--ink:#FBF3E6;--mute:#b5a999;--line:#40372e;--accent:#ff7a52;--keep:#3ec585;--rm:#ff8a80;--on:#1a1613}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;overflow-x:hidden}
.wrap{padding:0 16px 40px;max-width:640px;margin:0 auto}
header.top{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:10px 16px}
.bar{max-width:640px;margin:0 auto;display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center;justify-content:space-between}
.counts{font-size:14px;margin:0}
.counts b{font-weight:700}
.copy{min-height:44px;padding:0 14px;border-radius:10px;border:1px solid var(--accent);background:var(--accent);color:var(--on);font:inherit;font-weight:700}
h1{font-size:24px;margin:16px 0 6px}
h2{font-size:20px;margin:28px 0 4px;color:var(--accent)}
h3{font-size:16px;margin:18px 0 8px;color:var(--mute);text-transform:capitalize}
h4{font-size:17px;margin:0 0 2px}
.intro{margin:0 0 8px}
.item{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px;margin:0 0 14px}
.path{margin:0 0 8px;font-size:12px;color:var(--mute);word-break:break-all}
.shots img{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:8px;margin:0 0 8px}
.none{color:var(--mute);font-style:italic}
.verdict{margin:8px 0}
.verdict.pending{color:var(--mute);font-style:italic}
.routes{margin:4px 0;padding-left:18px;font-size:12px;color:var(--mute);word-break:break-all}
details{margin:0 0 8px;font-size:13px}
.btns{display:flex;gap:10px}
.btns button{flex:1;min-height:44px;border-radius:10px;border:2px solid var(--line);background:transparent;color:var(--ink);font:inherit;font-weight:700;font-size:16px}
.btns .keep[aria-pressed=true]{background:var(--keep);border-color:var(--keep);color:var(--on)}
.btns .remove[aria-pressed=true]{background:var(--rm);border-color:var(--rm);color:var(--on)}
.out{display:none;margin:12px 0}
.out textarea{width:100%;min-height:160px;font:13px/1.4 ui-monospace,Menlo,monospace;background:var(--card);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:8px}
"""

JS = """
(function(){
var KEY='sims-shortlist-v1',state={};
try{state=JSON.parse(localStorage.getItem(KEY)||'{}')||{};}catch(e){state={};}
var items=[].slice.call(document.querySelectorAll('.item'));
function save(){try{localStorage.setItem(KEY,JSON.stringify(state));}catch(e){}}
function paint(){
  var k=0,r=0;
  items.forEach(function(it){
    var c=state[it.getAttribute('data-path')];
    it.querySelector('.keep').setAttribute('aria-pressed',c==='keep'?'true':'false');
    it.querySelector('.remove').setAttribute('aria-pressed',c==='remove'?'true':'false');
    if(c==='keep')k++;else if(c==='remove')r++;
  });
  document.getElementById('nk').textContent=k;
  document.getElementById('nr').textContent=r;
  document.getElementById('nn').textContent=items.length-k-r;
}
items.forEach(function(it){
  var p=it.getAttribute('data-path');
  it.querySelector('.keep').addEventListener('click',function(){state[p]=state[p]==='keep'?'':'keep';save();paint();});
  it.querySelector('.remove').addEventListener('click',function(){state[p]=state[p]==='remove'?'':'remove';save();paint();});
});
function list(){
  var rm=[],kp=[];
  items.forEach(function(it){var p=it.getAttribute('data-path'),c=state[p];
    if(c==='remove')rm.push('REMOVE: '+p);else if(c==='keep')kp.push('KEEP: '+p);});
  return rm.concat(kp).join('\\n');
}
document.getElementById('copy').addEventListener('click',function(){
  var t=list(),box=document.getElementById('out'),ta=box.querySelector('textarea');
  ta.value=t;
  function fallback(){box.style.display='block';ta.focus();ta.select();}
  try{
    if(navigator.clipboard&&navigator.clipboard.writeText){
      navigator.clipboard.writeText(t).then(function(){box.style.display='none';},fallback);
    }else fallback();
  }catch(e){fallback();}
});
paint();
})();
"""

INTRO = ("A simulation here is a block in a lesson where the pupil changes a control "
         "(a slider, a button, a canvas or a bench) and a model responds. "
         "Mark each lesson Keep or Remove, then copy your choices.")


def build_page(results, verdicts, copy_images=True, src_dir=SRC, out_img=OUT_IMG, all_routes=None):
    groups = {}
    for path, rec in results.items():
        ks, subj, unit = group_of(path)
        groups.setdefault(ks, {}).setdefault(subj, {}).setdefault(unit, []).append((path, rec))
    body = []
    for ks in ("KS3", "KS4"):
        if ks not in groups:
            continue
        body.append("<h2>%s</h2>" % ks)
        for subj in sorted(groups[ks]):
            body.append("<h3>%s</h3>" % esc(SUBJECTS.get(subj, nice(subj))))
            for unit in sorted(groups[ks][subj]):
                if unit:
                    body.append("<h3>%s</h3>" % esc(nice(unit)))
                for path, rec in sorted(groups[ks][subj][unit]):
                    imgs = []
                    for n, blk in enumerate(rec.get("blocks", [])):
                        if not blk.get("found") or not blk.get("after_img"):
                            continue
                        name = "%s-%d.jpg" % (slugify(path), n)
                        if copy_images:
                            src = os.path.join(src_dir, blk["after_img"])
                            if os.path.exists(src):
                                downscale(src, os.path.join(out_img, name))
                                imgs.append("sims-shortlist/" + name)
                        else:
                            imgs.append("sims-shortlist/" + name)
                    rec = dict(rec)
                    if all_routes and path in all_routes:
                        rec["routes_all"] = all_routes[path]
                    body.append(item_html(path, rec, verdicts.get(path), imgs))
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="color-scheme" content="light dark">'
        '<title>Sims shortlist</title><style>%s</style></head><body>'
        '<header class="top"><div class="bar"><p class="counts"><b id="nk">0</b> kept, '
        '<b id="nr">0</b> removed, <b id="nn">0</b> not marked</p>'
        '<button type="button" class="copy" id="copy">Copy my choices</button></div></header>'
        '<main class="wrap"><h1>Sims shortlist</h1><p class="intro">%s</p>'
        '<div class="out" id="out"><textarea readonly aria-label="Your choices"></textarea></div>%s</main>'
        '<script>%s</script></body></html>' % (CSS, esc(INTRO), "\n".join(body), JS))


def main():
    with open(os.path.join(SRC, "results.json")) as fh:
        results = json.load(fh)
    try:
        with open(os.path.join(SRC, "verdicts.json")) as fh:
            verdicts = json.load(fh)
    except (OSError, ValueError):
        verdicts = {}
    all_routes = {}
    try:
        with open("/private/tmp/claude-501/lean-sims.json") as fh:
            all_routes = {k: v["routes"] for k, v in json.load(fh).items()}
    except (OSError, ValueError):
        pass
    if os.path.isdir(OUT_IMG):
        shutil.rmtree(OUT_IMG)
    page = build_page(results, verdicts, all_routes=all_routes)
    os.makedirs(os.path.dirname(OUT_HTML), exist_ok=True)
    with open(OUT_HTML, "w") as fh:
        fh.write(page)
    size = sum(os.path.getsize(os.path.join(OUT_IMG, f)) for f in os.listdir(OUT_IMG)) if os.path.isdir(OUT_IMG) else 0
    print("wrote %s (%d lessons, images %.1f MB)" % (OUT_HTML, len(results), size / 1e6))


if __name__ == "__main__":
    sys.exit(main())
