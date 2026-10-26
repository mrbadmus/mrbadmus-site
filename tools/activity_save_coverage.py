#!/usr/bin/env python3
"""activity_save_coverage.py — which lesson activities a family child's work is
SAVED from (POST /api/consumer/child/answer) and RESTORED to (GET
/api/consumer/child/saved), counted over the BUILT pages.

Static: no browser. Reads the built KS3 pages (ks3/**) and KS4 lesson pages
(combined/**, triple/**) and the capture code itself (shared/mrbadmus.v2.js),
and reports, for every answerable activity, whether the capture handles it.

  KS3   every `[data-activity]` block outside the ladder (the ladder saves
        itself through shared/ks3.js). An instrument is handled when its kind
        is in the capture's tables (KIND_A, KIND_B5C, the `<ks3-specs>` table)
        or it is a "Your turn" calculation (data-p<N>cfa). An unhandled kind is
        answerable or not according to tools/ks3_instrument_shapes.json (each
        kind classified from its shared/ks3.js wire function).
  KS4   every ROOT option group on a rebuilt (pilot) lesson — a lesson's own
        activity, outside the shared blocks — classified by the page's own
        classifier (tools/activity_save_coverage.js runs the `<ks4-root-acts>`
        block of shared/mrbadmus.v2.js in Node). Handled when the generic
        capture is present, or (before it) when ROOT_SPECS names the group.
        Plus every Ks4Write marked by LEVELS (the child picks a level): handled
        when the capture saves the pick (`levelTicks`).

Usage:
  python3 tools/activity_save_coverage.py [--classifier FILE] [--json OUT] [--md]
"""
import argparse
import collections
import glob
import json
import os
import re
import subprocess
import sys
from html.parser import HTMLParser

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOID = {'br', 'img', 'input', 'meta', 'link', 'hr', 'source', 'track', 'wbr', 'area', 'col', 'embed', 'param'}


def capture_tables(js):
    def obj(name):
        m = re.search(r'var %s = (\{.*?\});' % name, js)
        return set(json.loads(m.group(1))) if m else set()
    specs = set()
    a, b = js.find('/* <ks3-specs> */'), js.find('/* </ks3-specs> */')
    if a >= 0 and b > a:
        specs = set(re.findall(r"'(ks3-[a-z0-9-]+)'\s*:", js[a:b]))
    root_specs = collections.defaultdict(set)
    ra, rb = js.find('var ROOT_SPECS = {'), js.find('var rootPrev = {};')
    if ra >= 0 and rb > ra:
        cur = None
        for line in js[ra:rb].split('\n'):
            m = re.match(r"\s*'([a-z0-9-]+)': \[", line)
            if m:
                cur = m.group(1)
            for o in re.findall(r"opts: '([A-Za-z0-9_.]+)'", line):
                if cur:
                    root_specs[cur].add(o)
    return {
        'KIND_A': obj('KIND_A'), 'KIND_B5C': obj('KIND_B5C'), 'SPECS': specs,
        'ROOT_SPECS': root_specs,
        'generic_root': '/* <ks4-root-acts>' in js and 'rootActClick' in js,
        'level_ticks': 'function levelTicks' in js,
        'commit_no_reveal': 'commitNoReveal' in js,
    }


class Blocks(HTMLParser):
    """Each `[data-activity]` section outside the ladder, with what it holds."""

    def __init__(self):
        super().__init__()
        self.stack, self.blocks, self.cur = [], [], None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get('class') or '').split()
        in_ladder = any('ks3-ladder' in c for _, cs in self.stack for c in cs)
        if self.cur is None and 'data-activity' in a and not in_ladder:
            self.cur = {'activity': a.get('data-activity'), 'classes': cls, 'attrs': set(a),
                        'instrument': 'data-instrument' in a, 'keyed': 'data-keyedblock' in a,
                        'depth': len(self.stack), 'buttons': 0, 'inputs': 0, 'options': 0,
                        'reveal': False, 'cfa': False, 'battrs': set()}
            self.blocks.append(self.cur)
        elif self.cur is not None:
            if tag == 'button':
                self.cur['buttons'] += 1
                self.cur['battrs'].update(n for n in a if n.startswith('data-'))
                if 'ks3-option' in cls:
                    self.cur['options'] += 1
                if any(re.match(r'data-p\d+cfa-check$', n) for n in a):
                    self.cur['cfa'] = True
            if tag in ('input', 'select', 'textarea'):
                self.cur['inputs'] += 1
            if 'data-reveal' in a:
                self.cur['reveal'] = True
        if tag not in VOID:
            self.stack.append((tag, cls))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                if self.cur is not None and len(self.stack) <= self.cur['depth']:
                    self.cur = None
                break


def kind_of(b):
    for c in b['classes']:
        if (c.endswith('-block') and c != 'ks3-block' and c != 'ks3-keyed-block') or c in ('ks3-board', 'ks3-sort'):
            return c
    for c in b['classes']:
        if c not in ('ks3-block', 'ks3-dark', 'ks3-check', 'ks3-practical', 'ks3-hook', 'ks3-misconception'):
            return c
    return '?'


def ks3(tables, shapes):
    out = collections.Counter()
    rows = []
    lessons = 0
    for p in sorted(glob.glob(os.path.join(REPO, 'ks3', '**', '*.html'), recursive=True)):
        html = open(p, encoding='utf-8').read()
        if 'data-lesson' not in html:
            continue
        lessons += 1
        parser = Blocks()
        parser.feed(html)
        rel = os.path.relpath(p, REPO)
        for b in parser.blocks:
            if b['keyed']:
                cls, ans, cap = 'keyed commit (Start here / keyed)', True, True
            elif b['instrument']:
                k = kind_of(b)
                if b['cfa'] or re.match(r'ks3-p\d+cfa-block$', k):
                    cls, ans, cap = '"Your turn" calculation', True, True
                elif k in tables['KIND_A'] or k in tables['KIND_B5C']:
                    cls, ans, cap = 'instrument (adapter A / B5C)', True, True
                else:
                    sh = shapes.get(k, {}).get('shape')
                    if sh in ('G', 'A', 'M', 'S', 'T'):
                        cls, ans, cap = 'instrument shape ' + sh, True, k in tables['SPECS']
                    elif sh in ('X', 'R', 'D'):
                        cls, ans, cap = 'instrument shape ' + sh, False, False
                    else:
                        cls, ans, cap = 'instrument (unclassified)', None, False
                rows.append({'page': rel, 'activity': b['activity'], 'kind': k, 'class': cls, 'answerable': ans, 'captured': cap})
                out[(cls, ans, cap)] += 1
                continue
            else:
                if b['options'] and b['reveal']:
                    cls, ans, cap = 'prediction (options + reveal)', True, True
                elif b['options'] and not b['inputs']:
                    cls, ans, cap = 'commitment (options, nothing revealed)', True, tables['commit_no_reveal']
                elif b['buttons'] and not b['inputs'] and b['battrs'] <= {'data-step-next'}:
                    cls, ans, cap = 'worked example (reveal the next step)', False, False
                elif b['buttons'] or b['inputs']:
                    cls, ans, cap = 'other block with controls', None, False
                else:
                    cls, ans, cap = 'reading (no controls)', False, False
            rows.append({'page': rel, 'activity': b['activity'], 'kind': None, 'class': cls, 'answerable': ans, 'captured': cap})
            out[(cls, ans, cap)] += 1
    return lessons, out, rows


def ks4(tables, classifier):
    pages = []
    for p in sorted(glob.glob(os.path.join(REPO, 'combined', '*', '*', '*', '*.html')) +
                    glob.glob(os.path.join(REPO, 'triple', '*', '*', '*', '*.html'))):
        with open(p, encoding='utf-8') as f:
            if 'ks4-mount' in f.read():
                pages.append(os.path.relpath(p, REPO))
    cmd = ['node', os.path.join(REPO, 'tools', 'activity_save_coverage.js'), REPO] + ([classifier] if classifier else [])
    res = subprocess.run(cmd, input='\n'.join(pages), capture_output=True, text=True, check=True)
    data = json.loads(res.stdout)
    return pages, data


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--classifier', help='the <ks4-root-acts> text to use instead of shared/mrbadmus.v2.js')
    ap.add_argument('--json', help='write every row here')
    ap.add_argument('--md', action='store_true', help='print a Markdown report')
    args = ap.parse_args()

    js = open(os.path.join(REPO, 'shared', 'mrbadmus.v2.js'), encoding='utf-8').read()
    tables = capture_tables(js)
    shapes = json.load(open(os.path.join(REPO, 'tools', 'ks3_instrument_shapes.json'), encoding='utf-8'))['kinds']

    lessons3, c3, rows3 = ks3(tables, shapes)
    pages4, d4 = ks4(tables, args.classifier)

    # KS4: per lesson (slug), across its routes.
    by_lesson = collections.defaultdict(lambda: {'answer_groups': set(), 'uncaptured': set(), 'levels': 0, 'level_uncaptured': 0, 'explore': collections.Counter(), 'routes': 0})
    kinds4 = collections.Counter()
    errors4 = []
    for page, r in d4.items():
        L = by_lesson[r['slug']]
        if r.get('error'):
            errors4.append((page, r['error']))
            continue
        L['routes'] += 1
        L['levels'] += r['levels']
        if not tables['level_ticks']:
            L['level_uncaptured'] += r['levels']
        for g in r['groups']:
            if g['kind'] in ('pick', 'gate', 'multi'):
                key = (g['g'], g['id'])
                L['answer_groups'].add(key)
                handled = tables['generic_root'] or g['e'] in tables['ROOT_SPECS'].get(r['slug'], set())
                if not handled:
                    L['uncaptured'].add(key)
                kinds4[('answer', g['kind'], g['by'] or 'unjudged', handled)] += 1
            else:
                L['explore'][g['why'] or g['kind']] += 1
                kinds4[('not an answer', g['kind'], g['why'], False)] += 1

    ks4_with_answers = [s for s, L in by_lesson.items() if L['answer_groups']]
    ks4_uncaptured = sorted(s for s, L in by_lesson.items() if L['uncaptured'])
    level_lessons = sorted(s for s, L in by_lesson.items() if L['levels'])
    level_instances = sum(L['levels'] for L in by_lesson.values())
    level_uncaptured = sum(L['level_uncaptured'] for L in by_lesson.values())

    ks3_answerable = sum(v for (cls, ans, cap), v in c3.items() if ans)
    ks3_captured = sum(v for (cls, ans, cap), v in c3.items() if ans and cap)
    ks3_uncaptured = sum(v for (cls, ans, cap), v in c3.items() if ans and not cap)
    ks3_inst_uncaptured = sum(1 for r in rows3 if r['kind'] and not r['captured'])

    summary = {
        'capture': {'generic_ks4_root': tables['generic_root'], 'ks4_level_picks': tables['level_ticks'],
                    'ks3_spec_kinds': len(tables['SPECS'])},
        'ks3': {'lessons': lessons3, 'blocks': len(rows3), 'answerable': ks3_answerable, 'captured': ks3_captured,
                'answerable_uncaptured': ks3_uncaptured, 'instrument_blocks_uncaptured_any_shape': ks3_inst_uncaptured},
        'ks4': {'rebuilt_pages': len(pages4), 'lessons': len(by_lesson), 'lessons_with_root_answers': len(ks4_with_answers),
                'lessons_with_uncaptured_root_answers': len(ks4_uncaptured),
                'root_answer_groups': sum(len(L['answer_groups']) for L in by_lesson.values()),
                'root_answer_groups_uncaptured': sum(len(L['uncaptured']) for L in by_lesson.values()),
                'level_pick_lessons': len(level_lessons), 'level_pick_instances_all_routes': level_instances,
                'level_pick_instances_uncaptured': level_uncaptured, 'errors': errors4},
    }
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as f:
            json.dump({'summary': summary, 'ks3_rows': rows3, 'ks4': d4}, f, indent=1)

    if not args.md:
        print(json.dumps(summary, indent=1))
        return

    print('### KS3 (%d lessons, %d activity blocks outside the ladder)\n' % (lessons3, len(rows3)))
    print('| block class | answerable | saved + restored | blocks |')
    print('|---|---|---|---|')
    for (cls, ans, cap), v in sorted(c3.items(), key=lambda kv: (-kv[1], kv[0][0])):
        print('| %s | %s | %s | %d |' % (cls, {True: 'yes', False: 'no', None: '?'}[ans], 'yes' if cap else 'no', v))
    print('\nKS3 answerable blocks: **%d**, saved: **%d**, not saved: **%d**. Instrument blocks not handled (any shape): **%d**.\n'
          % (ks3_answerable, ks3_captured, ks3_uncaptured, ks3_inst_uncaptured))
    print('### KS4 rebuilt lessons (%d lessons, %d route pages)\n' % (len(by_lesson), len(pages4)))
    print('| root option group | kind | verdict from | saved + restored | groups (all routes) |')
    print('|---|---|---|---|---|')
    for (a, k, by, cap), v in sorted(kinds4.items(), key=lambda kv: (kv[0][0], -kv[1])):
        print('| %s | %s | %s | %s | %d |' % (a, k, by, 'yes' if cap else 'no', v))
    print('\nKS4 lessons with an answerable root activity: **%d**; with one NOT saved: **%d**.' % (len(ks4_with_answers), len(ks4_uncaptured)))
    print('Distinct root answer groups (per lesson, across routes): **%d**, not saved: **%d**.' %
          (summary['ks4']['root_answer_groups'], summary['ks4']['root_answer_groups_uncaptured']))
    print('KS4 level picks (Ks4Write marked by levels): **%d** instances over all routes in **%d** lessons; not saved: **%d**.\n'
          % (level_instances, len(level_lessons), level_uncaptured))
    if errors4:
        print('Pages the KS4 sandbox could not load: %d (%s)\n' % (len(errors4), '; '.join('%s: %s' % e for e in errors4[:5])))


if __name__ == '__main__':
    main()
