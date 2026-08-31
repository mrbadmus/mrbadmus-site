import zipfile, re, json, sys
from xml.etree import ElementTree as ET
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
MT='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
XLSX='/Users/midebadmus/Documents/GitHub/mrbadmus-site/26:27 Timetable/Science TT 2026-27.xlsx'

def load():
    z=zipfile.ZipFile(XLSX); ss=[]
    r=ET.fromstring(z.read('xl/sharedStrings.xml'))
    for si in r.findall('m:si',NS):
        ss.append(''.join(t.text or '' for t in si.iter(MT+'t')))
    sh=ET.fromstring(z.read('xl/worksheets/sheet1.xml')); rows={}
    for row in sh.iter(MT+'row'):
        rn=int(row.get('r')); cells={}
        for c in row.findall('m:c',NS):
            col=re.match(r'[A-Z]+',c.get('r')).group()
            v=c.find('m:v',NS); t=c.get('t')
            val=(ss[int(v.text)] if t=='s' else (v.text or '')) if v is not None else ''
            if val.strip(): cells[col]=val.strip()
        if cells: rows[rn]=cells
    return rows

rows=load()
hdr=rows[1]                      # col -> "Mon:1"
DAY={'Mon':1,'Tue':2,'Wed':3,'Thu':4,'Fri':5}
# class token: "11h/Ph1 $BDA (#S02B)"  -> class name is the leading token
TOKEN=re.compile(r'^([0-9]{1,2}[A-Za-z]{1,2}/[A-Za-z]{2}[0-9]?)\s+\$([A-Z]{3})')
Y1213=re.compile(r'^1[23]')

entries=[]; skipped={}
for rn in range(2,16):
    if rn not in rows: continue
    r=rows[rn]; teacher=r.get('A')
    if not teacher: continue
    for col,cell in r.items():
        if col=='A': continue
        h=hdr.get(col)
        if not h: continue
        day,per=h.split(':')
        if per=='Reg': continue                      # registration, never a lesson
        m=TOKEN.match(cell)
        if not m:
            skipped.setdefault(teacher,[]).append(cell); continue
        cls=m.group(1)
        if cls.startswith('[') or cell.startswith('EMC/'):
            skipped.setdefault(teacher,[]).append(cell); continue
        if Y1213.match(cls):
            skipped.setdefault(teacher,[]).append(cell); continue
        entries.append({'teacher':teacher,'class':cls,'weekday':DAY[day],'period':int(per),'raw':cell})

if __name__=='__main__':
    print(json.dumps({'entries':entries},indent=None)[:200])
