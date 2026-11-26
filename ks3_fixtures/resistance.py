# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 P8 `resistance` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 7176d7049d. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'P8'
SOURCE_SLUG = 'resistance'
FROZEN_FROM = '7176d7049d'

LESSON = {'slug': 'resistance',
 'title': 'Resistance',
 'discipline': 'physics',
 'unit': 'Electric circuits',
 'family': 'QUANTITATIVE',
 'covers': ['KS3.P.CUR.02b'],
 'touches': ['KS3.WS.ANA.01'],
 'beyond_statutory': False,
 'threads': [{'id': 'electricity', 'level': 3}],
 'typical_year': 8,
 'typical_minutes': 60,
 'requires': ['potential-difference'],
 'assumes': [],
 'references': ['building-and-measuring-a-circuit', 'current-and-circuits'],
 'ks4_links': [],
 'meta_description': 'Resistance is not something you measure directly. You measure the push, you '
                     'measure the flow, and you divide one by the other. That ratio is the number.',
 'big_question': 'Resistance is not something you measure directly. You measure the push, you '
                 'measure the flow, and you divide one by the other. That ratio is the number.',
 'rail': [{'anchor': 's-hook',
           'short': 'WIRE',
           'label': 'A metre of thin wire',
           'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'BENCH',
           'label': 'Two readings, one division',
           'done_when': 'gate_and_a_control'},
          {'anchor': 's-triangle',
           'short': 'CFIFA',
           'label': 'Triangle and five steps',
           'done_when': 'attempt_checked'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Add a metre of thin wire. The bulb dims.',
                'prompt': 'A torch bulb on two cells is bright. Break the loop and splice in a '
                          'metre of thin nichrome wire — no extra components, nothing removed — '
                          'and the bulb goes noticeably dimmer. The wire gets warm.',
                'commit': 'If you had to guess, is less electricity flowing only through the bulb, '
                          'or all the way round?',
                'options': ['Only through the bulb', 'All the way round'],
                'answer': 1,
                'reveal': 'How hard something makes it for charge to get through has a name: '
                          'resistance. Next: what resistance is, and why measuring it takes two '
                          'meters.',
                'guess': True,
                'replies': ['It is easy to picture the wire using some up before it reaches the '
                            'bulb. But in one loop the flow is the same everywhere, so it has '
                            'fallen all the way round.',
                            'In one loop the flow is the same at every point. The thin wire makes '
                            'the whole loop harder to get through, so less flows everywhere.']},
 'misconceptions': [{'id': 'CIRC-17',
                     'statement': 'Resistance is a force pushing back against the current.',
                     'confronted_by': 's-think'},
                    {'id': 'CIRC-18',
                     'statement': 'A component has one resistance, so it does not matter what '
                                  'supply you test it on.',
                     'elicited_by': 'bench',
                     'confronted_by': 'bench'},
                    {'id': 'CIRC-19',
                     'statement': 'You find a resistance by multiplying the voltmeter reading by '
                                  'the ammeter reading.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 'your-turn-resistance'},
                    {'id': 'CIRC-20',
                     'statement': 'If one component gives two different resistances, one of the '
                                  'meters must be faulty.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-think'}],
 'core': [{'type': 'hook', 'id': 'hook-commit', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': '<strong>Resistance</strong> is how hard a component makes it for charge to get '
                   'through. It is measured in <strong>ohms</strong>, written with the Greek '
                   'letter <strong>Ω</strong>. A short piece of copper wire is a few hundredths of '
                   'an ohm; a thin nichrome wire is several; a resistor is whatever it says on the '
                   'packet; a filament is tens of ohms once it is glowing.'},
          {'type': 'explainer',
           'text': 'There is no such thing as an ohm-meter that reads resistance off the component '
                   'the way a ruler reads a length. Resistance is defined as a '
                   '<strong>ratio</strong>: the potential difference across a component divided by '
                   'the current through it. So you take two measurements and do one division. '
                   '<strong>R = V ÷ I.</strong>'},
          {'type': 'explainer',
           'text': 'Read that ratio as a price. A component of 15 Ω charges you 15 volts for every '
                   'amp you want through it. Something with a low resistance is cheap: a small '
                   'push gets a big flow. Something with a high resistance is expensive, and if '
                   'the price is high enough — a piece of plastic, a gap of air — no push you can '
                   'safely arrange will buy you any current at all.'},
          {'type': 'practical', 'id': 'bench', 'anchor': 's-bench'},
          {'type': 'check', 'id': 'same-division-four-times', 'anchor': None},
          {'type': 'formula',
           'id': 'resistance-rule',
           'eyebrow': 'Writing it down · the shape of this relationship',
           'statement': 'Potential difference = current × resistance',
           'triangle': {'eyebrow': 'The triangle',
                        'heading': 'Cover the one you want',
                        'aria_label': 'A formula triangle. The potential difference V sits above a '
                                      'dividing line; the current I and the resistance R sit below '
                                      'it, multiplied together. Covering one letter leaves the way '
                                      'to work it out.',
                        'order': ['top', 'left', 'right'],
                        'covered': 'right',
                        'top': {'label': 'V',
                                'button': 'Cover V',
                                'result': 'V = I × R',
                                'text': 'Cover V and I and R are left side by side — multiply '
                                        'them.'},
                        'left': {'label': 'I',
                                 'button': 'Cover I',
                                 'result': 'I = V ÷ R',
                                 'text': 'Cover I on the triangle: V sits over R, so you divide.'},
                        'right': {'label': 'R',
                                  'button': 'Cover R',
                                  'result': 'R = V ÷ I',
                                  'text': 'Cover R on the triangle: V sits over I, so you divide.'},
                        'close': {'rule': 'Two things side by side means multiply. One thing over '
                                          'another means divide.',
                                  'units': ['V · potential difference across the component · V',
                                            'I · current through the same component · A',
                                            'R · resistance of that component, at that moment · Ω'],
                                  'condition': '1 Ω is 1 V for each 1 A'}}},
          {'type': 'worked-example', 'id': 'cfifa-resistance-plain'},
          {'type': 'worked-example', 'id': 'cfifa-resistance-convert'},
          {'type': 'check', 'id': 'your-turn-resistance', 'anchor': 's-triangle'},
          {'type': 'key-fact', 'ref': 'resistance-is-a-ratio'},
          {'type': 'misconception', 'id': 'think-resistance-pushes-back', 'anchor': 's-think'},
          {'type': 'quiz', 'anchor': 's-ladder'},
          {'type': 'summary', 'id': 's-keynote'}],
 'activities': [{'id': 'cfifa-resistance-plain',
                 'kind': 'worked-example',
                 'demand': 'calculate',
                 'eyebrow': 'Worked example · one step at a time',
                 'heading': 'A voltmeter across a resistor reads 6.0 V. The ammeter in the loop '
                            'reads 0.40 A. What is the resistance?',
                 'head_counter': {'format': 'Step {n} of 5', 'total': 5},
                 'buttons': {'first': 'Show the first step',
                             'next': 'Show the next step',
                             'done': 'All five shown',
                             'done_note': 'Nothing needed converting there. Now the one that '
                                          'does.'},
                 'staged': True,
                 'fifa': [{'letter': 'C',
                           'label': 'Convert',
                           'line': '6.0 V stays 6.0 V · 0.40 A stays 0.40 A',
                           'note': 'The p.d. is already in volts and the current is already in '
                                   'amps, so there is nothing to convert.'},
                          {'letter': 'F',
                           'label': 'Formula',
                           'line': 'R = V ÷ I',
                           'note': 'Cover R on the triangle: V sits over I, so you divide.'},
                          {'letter': 'I',
                           'label': 'Insert',
                           'line': 'R = 6.0 V ÷ 0.40 A',
                           'note': 'Both readings come from the same setting of the supply.'},
                          {'letter': 'F',
                           'label': 'Fine-tune',
                           'line': '6.0 ÷ 0.40 = 15',
                           'note': 'Volts divided by amps leaves ohms.'},
                          {'letter': 'A',
                           'label': 'Answer',
                           'line': 'R = 15 Ω',
                           'note': 'It takes 15 V across this resistor to drive 1 A through it.'}]},
                {'id': 'cfifa-resistance-convert',
                 'kind': 'worked-example',
                 'demand': 'calculate',
                 'eyebrow': 'Worked example · one step at a time',
                 'heading': 'A voltmeter across a torch lamp reads 3.0 V. The ammeter reads 250 '
                            'mA. What is the resistance?',
                 'head_counter': {'format': 'Step {n} of 5', 'total': 5},
                 'buttons': {'first': 'Show the first step',
                             'next': 'Show the next step',
                             'done': 'All five shown',
                             'done_note': 'Convert first, then the same four lines. Your turn '
                                          'below.'},
                 'staged': True,
                 'fifa': [{'letter': 'C',
                           'label': 'Convert',
                           'line': '250 mA ÷ 1000 = 0.250 A',
                           'note': 'The formula wants amps, and a milliamp is a thousandth of an '
                                   'amp, so divide by 1000.'},
                          {'letter': 'F',
                           'label': 'Formula',
                           'line': 'R = V ÷ I',
                           'note': 'Cover R on the triangle: V sits over I, so you divide.'},
                          {'letter': 'I',
                           'label': 'Insert',
                           'line': 'R = 3.0 V ÷ 0.250 A',
                           'note': 'The converted current goes in. The milliamp reading never '
                                   'does.'},
                          {'letter': 'F',
                           'label': 'Fine-tune',
                           'line': '3.0 ÷ 0.250 = 12',
                           'note': 'Volts divided by amps leaves ohms.'},
                          {'letter': 'A',
                           'label': 'Answer',
                           'line': 'R = 12 Ω',
                           'note': 'Put 250 in instead of 0.250 and the answer comes out 1000 '
                                   'times too small.'}]},
                {'id': 'your-turn-resistance',
                 'kind': 'p8-attempt',
                 'demand': 'calculate',
                 'eyebrow': 'Your turn · the same five steps',
                 'rest': {'v': '6.00 V',
                          'i': '0.600 A',
                          'r': '10.0 Ω',
                          'vnum': '6.00',
                          'inum': '0.600',
                          'rnum': '10.0',
                          'name': '10 ohm resistor',
                          'anote': 'It takes 10.0 V across this component to drive 1 A through '
                                   'it.'},
                 'questions': [{'id': 'q1',
                                'tab': 'Question 1',
                                'head': 'Your component: the voltmeter reads {v} and the ammeter '
                                        'reads {i}.',
                                'lead': 'Write each line out yourself — starting by deciding '
                                        'whether anything needs converting. Then check your '
                                        'working and tick the lines you had.',
                                'steps': [{'letter': 'C',
                                           'label': 'Convert',
                                           'placeholder': 'anything to convert?',
                                           'line': '{v} stays {v} · {i} stays {i}',
                                           'note': 'Both meters already read in the units the '
                                                   'formula wants, so nothing changes.'},
                                          {'letter': 'F',
                                           'label': 'Formula',
                                           'line': 'R = V ÷ I',
                                           'note': 'Cover R on the triangle: V sits over I, so you '
                                                   'divide.'},
                                          {'letter': 'I',
                                           'label': 'Insert',
                                           'line': 'R = {v} ÷ {i}',
                                           'note': 'Both readings come from the same setting of '
                                                   'the supply.'},
                                          {'letter': 'F',
                                           'label': 'Fine-tune',
                                           'line': '{vnum} ÷ {inum} = {rnum}',
                                           'note': 'Volts divided by amps leaves ohms.'},
                                          {'letter': 'A',
                                           'label': 'Answer',
                                           'placeholder': 'remember the unit',
                                           'line': 'R = {r}',
                                           'note': '{anote}'}],
                                'close': 'The five lines give {r} for the {name} at {v}.'},
                               {'id': 'q2',
                                'tab': 'Question 2',
                                'head': 'A torch bulb on a 4.5 V supply. The ammeter reads 150 mA.',
                                'lead': 'This one needs the Convert line to do some work.',
                                'steps': [{'letter': 'C',
                                           'label': 'Convert',
                                           'placeholder': 'anything to convert?',
                                           'line': '150 mA ÷ 1000 = 0.150 A',
                                           'note': 'A milliamp is a thousandth of an amp, so '
                                                   'divide by 1000 before you go any further.'},
                                          {'letter': 'F',
                                           'label': 'Formula',
                                           'line': 'R = V ÷ I',
                                           'note': 'Cover R on the triangle: V sits over I, so you '
                                                   'divide.'},
                                          {'letter': 'I',
                                           'label': 'Insert',
                                           'line': 'R = 4.5 V ÷ 0.150 A',
                                           'note': 'The converted current goes in. The milliamp '
                                                   'reading never does.'},
                                          {'letter': 'F',
                                           'label': 'Fine-tune',
                                           'line': '4.5 ÷ 0.150 = 30',
                                           'note': 'Volts divided by amps leaves ohms.'},
                                          {'letter': 'A',
                                           'label': 'Answer',
                                           'placeholder': 'remember the unit',
                                           'line': 'R = 30 Ω',
                                           'note': 'Put 150 in instead of 0.150 and the answer '
                                                   'comes out 0.03 Ω — 1000 times too small.'}],
                                'close': 'The five lines give 30 Ω. The whole question turned on '
                                         'the first one.'}]},
                {'id': 'think-resistance-pushes-back',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'CIRC-17',
                 'statements': [{'quote': 'Resistance is a force pushing back against the current.',
                                 'targets': 'CIRC-17',
                                 'body': ['There is no push-back. Resistance is a ratio — one '
                                          'measurement divided by another — and a ratio is not a '
                                          'force. What actually happens inside the metal is that '
                                          'the drifting electrons keep colliding with the atoms of '
                                          'the lattice, which are themselves jiggling with heat. '
                                          'Each collision hands over a little energy, the metal '
                                          'warms up, and the drift is slower than the push alone '
                                          'would suggest. A thin wire has fewer routes and a long '
                                          'wire has more collisions, so both resist more.']},
                                {'quote': 'A component has one resistance, so it does not matter '
                                          'what supply you test it on.',
                                 'targets': 'CIRC-18',
                                 'body': ['True for a resistor, and that is exactly why resistors '
                                          'are sold with a number printed on them. Not true for a '
                                          'filament lamp: turn the supply up, the filament gets '
                                          'hotter, the atoms jiggle harder, the collisions get '
                                          'worse and the resistance climbs — from about 6 Ω cold '
                                          'to about 18 Ω at full brightness. Both readings are '
                                          'right. Resistance belongs to a component <em>in a '
                                          'state</em>, and for a lamp the state is its '
                                          'temperature.']}]},
                {'eyebrow': 'At the bench · one component under test, an ammeter and a voltmeter',
                 'heading': 'Two readings. One division.',
                 'progress': {'idle': 'Change a control to begin', 'live': 'Both controls live'},
                 'lead': 'Clip a component between the terminals, set the supply, and read both '
                         'meters. The resistance is whatever the division gives.',
                 'lamp_base': 4,
                 'lamp_slope': 1.2,
                 'volts': [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0],
                 'start_comp': 2,
                 'supply_label_svg': 'VARIABLE SUPPLY',
                 'loop_label': 'ONE LOOP, ONE CURRENT',
                 'comp_label': 'The component under test',
                 'supply': {'label': 'The supply',
                            'min': 0,
                            'max': 7,
                            'step': 1,
                            'start': 3,
                            'value': '6.0 V'},
                 'gate': {'prompt': 'Commit first. A 10 Ω resistor is tested at 3.0 V, then at 6.0 '
                                    'V. What happens to the resistance you calculate?',
                          'options': ['It doubles, because you doubled the p.d.',
                                      'It halves, because the current doubled',
                                      'It stays at 10 Ω, because both readings doubled and the '
                                      'ratio did not change',
                                      'It cannot be worked out without knowing the length of the '
                                      'resistor'],
                          'answer': 2},
                 'components': [{'id': 'r2',
                                 'label': '2 Ω resistor',
                                 'name': '2 OHM RESISTOR',
                                 'ohms': 2,
                                 'band': 'low',
                                 'shape': 'res'},
                                {'id': 'nichrome',
                                 'label': 'Thin nichrome wire',
                                 'name': 'THIN NICHROME WIRE',
                                 'ohms': 5,
                                 'band': 'low',
                                 'shape': 'wire',
                                 'stroke': 7},
                                {'id': 'r10',
                                 'label': '10 Ω resistor',
                                 'name': '10 OHM RESISTOR',
                                 'ohms': 10,
                                 'band': 'high',
                                 'shape': 'res'},
                                {'id': 'r30',
                                 'label': '30 Ω resistor',
                                 'name': '30 OHM RESISTOR',
                                 'ohms': 30,
                                 'band': 'high',
                                 'shape': 'res'},
                                {'id': 'lamp',
                                 'label': 'Filament lamp',
                                 'name': 'FILAMENT LAMP',
                                 'band': 'lamp',
                                 'shape': 'lamp'}],
                 'readouts': [{'id': 'v',
                               'label': 'The voltmeter reads',
                               'sub': 'across the component'},
                              {'id': 'i',
                               'label': 'The ammeter reads',
                               'sub': 'through the component'},
                              {'id': 'r', 'label': 'So the resistance is', 'sub': '—'},
                              {'id': 'verdict', 'label': 'Turn the supply up and', 'word': True}],
                 'branches': {'lamp': 'At {v} the lamp passes {i}, so V ÷ I gives {r}. Turn the '
                                      'supply down to 1.5 V and the same division gives about '
                                      '{rcold} Ω; turn it up to 12 V and it gives about {rhot} Ω. '
                                      'Nothing is wrong with the meters. The filament is hotter at '
                                      'a bigger p.d., the atoms jiggle harder, the drifting '
                                      'electrons collide more often, and the resistance genuinely '
                                      'rises. Every one of those numbers is the real resistance of '
                                      'the lamp at that temperature.',
                              'low': 'At {v} this {name} passes {i}, {size}, and V ÷ I gives {r}. '
                                     'Move the supply anywhere on the slider and the two readings '
                                     'change together, so the division keeps giving {r}. That is '
                                     'what a low resistance means — a small push buys a lot of '
                                     'flow — and a fixed ratio is what lets one number describe '
                                     'the component.',
                              'high': 'At {v} this {name} passes {i}, {size}, and V ÷ I gives {r}. '
                                      'The current is held down by the resistance, which charges '
                                      '{rint} volts for every amp. Change the supply and both '
                                      'meters move, but the ratio comes back to {r} every time, '
                                      'which is why the value can be printed on the component.'},
                 'id': 'bench',
                 'kind': 'component-under-test',
                 'demand': 'investigate'},
                {'eyebrow': 'The figure',
                 'heading': 'The same division, four times over',
                 'lead': 'Two components, each tested at four supply settings. Every row is one '
                         'reading of the voltmeter, one reading of the ammeter, and one division. '
                         'Watch the last column.',
                 'table': {'corner': 'Component',
                           'min_width': 640,
                           'columns': ['V', 'I', 'R = V ÷ I'],
                           'rows': [{'head': '10 Ω resistor',
                                     'cells': ['3.00 V', '0.300 A', '<strong>10.0 Ω</strong>']},
                                    {'head': 'same resistor',
                                     'same': True,
                                     'cells': ['6.00 V', '0.600 A', '<strong>10.0 Ω</strong>']},
                                    {'head': 'same resistor',
                                     'same': True,
                                     'cells': ['12.00 V', '1.200 A', '<strong>10.0 Ω</strong>']},
                                    {'head': 'Filament lamp',
                                     'cells': ['1.50 V', '0.259 A', '<strong>5.8 Ω</strong>']},
                                    {'head': 'same lamp',
                                     'same': True,
                                     'cells': ['6.00 V', '0.536 A', '<strong>11.2 Ω</strong>']},
                                    {'head': 'same lamp',
                                     'same': True,
                                     'cells': ['12.00 V', '0.652 A', '<strong>18.4 Ω</strong>']}]},
                 'close': 'The resistor gives the same answer every time, which is why one number '
                          'on the packet is enough to describe it. The lamp does not: its filament '
                          'gets hotter as you turn the supply up, and hot metal resists more. '
                          'Every one of those readings is a correct resistance — of that lamp, at '
                          'that moment, at that temperature.',
                 'id': 'same-division-four-times',
                 'kind': 'circ-band',
                 'demand': 'investigate'}],
 'figures': [],
 'key_facts': [{'id': 'resistance-is-a-ratio',
                'eyebrow': 'Key fact',
                'ground': 'card',
                'placement': 'top-level',
                'text': 'Resistance is the ratio of potential difference to current: R = V ÷ I, '
                        'measured in ohms (Ω). One ohm is one volt for each amp. You never measure '
                        'it directly — you measure V across a component and I through it, and '
                        'divide.'}],
 'ladder': {'recall': {'q': 'A voltmeter across a wire reads 4.5 V and the ammeter in the loop '
                            'reads 0.90 A. What is the resistance of the wire?',
                       'options': ['4.05 Ω — multiply the two readings',
                                   '0.2 Ω — divide the current by the p.d.',
                                   '5.0 Ω',
                                   '5.0 V — the number is the p.d. needed for one amp'],
                       'answer': 2,
                       'feedback': {0: 'Multiplying V by I gives you the power in watts, not the '
                                       'resistance. Cover R on the triangle and V sits over I, so '
                                       'you divide.',
                                    1: 'That is the division the wrong way up. Resistance is volts '
                                       'per amp, so the volts go on top.',
                                    3: 'The number is right and the unit is wrong. Volts divided '
                                       'by amps leaves ohms, and the question asked for a '
                                       'resistance.'},
                       'title': 'Rung 1 · Calculate'},
            'apply': {'q': 'A student tests a filament lamp at 2 V and gets 6.4 Ω, then at 10 V '
                           'and gets 16.0 Ω, and decides one of the measurements must be a '
                           'mistake. What is right?',
                      'options': ['Both are right. The filament is hotter at 10 V, and hot metal '
                                  'resists more — so the lamp genuinely has a different resistance '
                                  'in each state.',
                                  'The 6.4 Ω reading is the real resistance, and the 16.0 Ω '
                                  'reading is wrong because the meters are affected by the heat '
                                  'coming off the filament, so a reading taken while a lamp is '
                                  "glowing is never the component's own value.",
                                  'The student is right — R = V ÷ I is a law, so a component can '
                                  'only have one resistance.',
                                  'Both are right, because the resistance of any component always '
                                  'goes up when you turn the supply up.'],
                      'answer': 0,
                      'feedback': {1: 'The meters are fine. What changed is the filament: its '
                                      'resistance really is different when it is white-hot.',
                                   2: 'R = V ÷ I is a definition and always applies. What is not '
                                      'always true is that R stays the same, and a filament lamp '
                                      'is the standard example of a component where it does not.',
                                   3: 'The verdict is right and the reason is not. A resistor '
                                      'tested at 2 V and at 10 V gives the same answer both times; '
                                      'it is the lamp’s changing temperature that does this.'},
                      'title': 'Rung 2 · The one that catches people'},
            'explain': {'q': 'Describe how you would find the resistance of a length of nichrome '
                             'wire using a battery, an ammeter and a voltmeter, and explain why '
                             'you need both meters.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Put the ammeter in the loop and…',
                        'success': ['Puts the ammeter in the loop, in series with the wire.',
                                    'Puts the voltmeter across the wire, in parallel with it.',
                                    'Says to record both readings for the same setting.',
                                    'Divides the p.d. by the current, and gives the unit as ohms.',
                                    'Explains that resistance is a ratio of the two, so neither '
                                    'meter alone can give it.'],
                        'title': 'Rung 3 · Explain'},
            'produce': {'q': 'An electric kettle element is a coil of wire that must produce a lot '
                             'of heat. A lighting flex must carry a similar current and stay cool. '
                             'Explain what the resistance of each has to be, and how a '
                             'manufacturer would achieve it with the same kind of metal.',
                        'field_label': 'Your answer',
                        'placeholder': 'The element needs a high resistance because…',
                        'success': ['Says the kettle element needs a fairly high resistance so '
                                    'that energy is transferred to heat in it.',
                                    'Says the flex needs a very low resistance so that almost no '
                                    'energy is transferred to heat in the cable.',
                                    'Says a thinner wire has a higher resistance and a thicker '
                                    'wire a lower one.',
                                    'Says a longer wire has a higher resistance and a shorter one '
                                    'a lower one — so the element is a long thin coil.',
                                    'Says the danger of getting the flex wrong is the cable '
                                    'heating up rather than the appliance failing.'],
                        'title': 'Rung 4 · Take it somewhere new'}},
 'key_note': 'Resistance measures how hard a component makes it for charge to get through, in ohms '
             '(Ω). It is defined as a ratio: the potential difference across the component divided '
             'by the current through it, R = V ÷ I, so finding it always means two measurements '
             'and one division. One ohm is one volt for each amp. A resistor gives the same ratio '
             'at every supply setting, which is why one number describes it; a filament lamp does '
             'not, because its resistance climbs as it heats.',
 'stretch': [{'id': 'ohm-published-in-1827',
              'type': 'explainer',
              'text': 'Georg Ohm published the relationship in 1827 and was largely ignored for a '
                      'decade; his own colleagues called the work a web of naked fancies. What he '
                      'had found is now stated carefully as a special case: for a metal at '
                      'constant temperature the ratio V ÷ I is constant. The words "at constant '
                      'temperature" are doing real work — a filament lamp obeys no such rule, and '
                      'neither does a diode, a thermistor or a light-dependent resistor. The '
                      "equation R = V ÷ I is always true, because it is a definition. Ohm's law is "
                      'the extra claim that R stays the same, and plenty of components refuse it.'},
             {'id': 'components-that-refuse-it',
              'type': 'explainer',
              'text': "Components that refuse it on purpose are the useful ones. A thermistor's "
                      'resistance drops sharply as it warms, which is how an oven, a kettle and a '
                      'car engine all know their own temperature: the circuit is not measuring '
                      'heat, it is measuring a resistance and reading the temperature off it. A '
                      'light-dependent resistor does the same trick with brightness, which is what '
                      'switches a street light on at dusk.'}],
 'support': [],
 'vocabulary': [{'term': 'resistance',
                 'definition': 'How hard a component makes it for charge to get through. Defined '
                               'as the p.d. across it divided by the current through it.'},
                {'term': 'ohm',
                 'definition': 'The unit of resistance, written Ω. One ohm is one volt for each '
                               'amp.'},
                {'term': 'ratio',
                 'definition': 'One quantity divided by another. Resistance is a ratio, which is '
                               'why it takes two measurements and never one.'}],
 'tutor': {'anchor': 's-bench',
           'prompt': 'Ask Mr Badmus AI',
           'body': 'Got a voltmeter reading and an ammeter reading and want the resistance?',
           'cta': 'Ask about this lesson'},
 'ks4_becomes': "Ohm's law as a special case, current–p.d. graphs for a wire, a lamp and a diode, "
                'and resistances added in series and in parallel.',
 'convention_note': 'The bench is a teaching model. The four ohmic components are given fixed '
                    'resistances of 2, 5, 10 and 30 ohms; real wires and resistors vary with '
                    "temperature by a small amount, and a resistor's printed value carries a "
                    'tolerance of a few per cent. The filament lamp is modelled by taking its '
                    'resistance as rising with the p.d. across it, from about 6 ohms at 1.5 V to '
                    'about 18 ohms at 12 V; the model fixes the two ends of that rise and makes no '
                    'claim about its shape in between, and the values here are typical of a small '
                    'lamp rather than measurements of a particular one. The supply, the wires and '
                    'the ammeter are treated as having no resistance and the voltmeter as drawing '
                    'no current. Currents are rounded to three decimal places and resistances to '
                    'one.',
 'ws': ['measurement', 'analysis'],
 'authored': True}
