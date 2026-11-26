# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 P9 `charging-by-rubbing` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 7176d7049d. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'P9'
SOURCE_SLUG = 'charging-by-rubbing'
FROZEN_FROM = '7176d7049d'

LESSON = {'slug': 'charging-by-rubbing',
 'title': 'Charging by rubbing',
 'discipline': 'physics',
 'unit': 'Static electricity',
 'family': 'PROCESS',
 'covers': ['KS3.P.STAT.01a'],
 'touches': ['KS3.WS.ANA.01'],
 'beyond_statutory': False,
 'threads': [{'id': 'electricity', 'level': 2}],
 'typical_year': 8,
 'typical_minutes': 60,
 'requires': [{'unit': 'P8', 'lesson': 'conductors-and-insulators'}],
 'assumes': [],
 'references': ['electric-fields', {'unit': 'P8', 'lesson': 'current-and-circuits'}],
 'ks4_links': [],
 'meta_description': 'Rubbing does not make charge. It moves electrons from one surface to the '
                     'other, so the two objects end up equally and oppositely charged.',
 'big_question': 'Where does the charge come from when you rub two things together?',
 'rail': [{'anchor': 's-hook', 'short': 'ROD', 'label': 'Rod and duster', 'done_when': 'committed'},
          {'anchor': 's-rub',
           'short': 'BENCH',
           'label': 'Pick the pair',
           'done_when': 'gate_and_a_control'},
          {'anchor': 's-think',
           'short': 'THINK',
           'label': 'Nothing is created',
           'done_when': 'gate_committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'The rod comes out negative. What about the duster?',
                'prompt': 'A polythene rod rubbed with a woollen duster picks up small pieces of '
                          'paper, and a careful test shows the rod is negatively charged. The '
                          'duster was neutral before you started, and so was the rod.',
                'commit': 'If you had to guess, what charge does the duster have now?',
                'options': ['Still neutral', 'Positive'],
                'answer': 1,
                'reveal': 'Nothing was made: charge was only moved from one to the other. Next: '
                          'pick different materials and see which way the electrons go.',
                'guess': True,
                'replies': ["It was the rod that changed, so that makes sense. But the rod's extra "
                            'electrons came off the duster, which leaves the duster short of '
                            'electrons, so it is positive.',
                            'Every electron the rod gained came off the duster. That leaves the '
                            'duster short of electrons, so it is positive, by exactly as much as '
                            'the rod is negative.']},
 'misconceptions': [{'id': 'CHRG-01',
                     'statement': 'Rubbing creates charge.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 's-think'},
                    {'id': 'CHRG-02',
                     'statement': 'A positive object has had positive charge added to it.',
                     'confronted_by': 's-think'},
                    {'id': 'CHRG-03',
                     'statement': 'Only one of the two objects ends up charged.',
                     'elicited_by': 's-hook',
                     'confronted_by': 'rub'},
                    {'id': 'CHRG-04',
                     'statement': 'A material has a charge of its own that it always takes, '
                                  'whatever it is rubbed with.',
                     'elicited_by': 'rub',
                     'confronted_by': 'rub'}],
 'core': [{'type': 'hook', 'id': 'hook-commit', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Every atom holds positive protons in a nucleus and negative electrons around '
                   'it, and in a neutral object the two exactly balance. The protons are locked '
                   'into the nuclei and cannot go anywhere. <strong>Only the electrons can '
                   'move</strong> — which means every piece of static electricity you have ever '
                   'met is a story about electrons and nothing else.'},
          {'type': 'explainer',
           'text': 'Rubbing two surfaces together presses them into contact at millions of tiny '
                   'points. Some materials hold their outer electrons more tightly than others, so '
                   'at those points of contact electrons cross over from the looser material to '
                   'the tighter one. Pull the surfaces apart and the electrons stay where they '
                   'went.'},
          {'type': 'explainer',
           'text': 'So the object that <strong>lost</strong> electrons is left with more protons '
                   'than electrons: it is <strong>positively charged</strong>. The object that '
                   '<strong>gained</strong> them has more electrons than protons: it is '
                   '<strong>negatively charged</strong>. Both are charged, by exactly the same '
                   'amount, in opposite directions — and nothing was created. This only works with '
                   'insulators, because a conductor would let the charge run straight back or away '
                   'to earth through your hand.'},
          {'type': 'practical', 'id': 'rub', 'anchor': 's-rub'},
          {'type': 'check', 'id': 'tribo', 'anchor': 's-tribo'},
          {'type': 'key-fact', 'ref': 'rubbing-separates-charge'},
          {'type': 'misconception', 'id': 'think-nothing-is-created', 'anchor': 's-think'},
          {'type': 'quiz', 'anchor': 's-ladder'},
          {'type': 'summary', 'id': 's-keynote'}],
 'activities': [{'id': 'think-nothing-is-created',
                 'kind': 'charge-think',
                 'demand': 'explain',
                 'targets': 'CHRG-01',
                 'band_target': 'rub',
                 'statements': [{'quote': 'Rubbing makes the charge — the friction creates it.',
                                 'targets': 'CHRG-01',
                                 'body': ['Nothing is made. Every electron that ends up on the rod '
                                          'was on the duster a moment earlier, and the two objects '
                                          'together carry exactly the charge they carried before '
                                          'you touched them: none. The rubbing supplies contact, '
                                          'not charge. It matters because it presses the surfaces '
                                          'together at millions of points and then peels them '
                                          'apart, and each of those contacts is a chance for an '
                                          'electron to change sides. Press two surfaces together '
                                          'firmly and lift them straight off and you get some '
                                          'charge without rubbing at all.']},
                                {'quote': 'A positively charged rod has had positive charge added '
                                          'to it.',
                                 'targets': 'CHRG-02',
                                 'body': ['Nothing positive was added. It has had electrons taken '
                                          'away, and the protons that were always there are now '
                                          'unbalanced. This is worth being fussy about, because it '
                                          'is the reason the two objects always end up opposite: '
                                          'one loses exactly what the other gains. Protons sit in '
                                          'nuclei, bound by a force enormously stronger than '
                                          'anything a duster can supply, and in ordinary matter '
                                          'they never go anywhere.']}]},
                {'eyebrow': 'At the bench · two dry insulators, rubbed together',
                 'heading': 'Pick the pair. Count the rubs.',
                 'progress': {'idle': 'Change a control to begin', 'live': 'Three controls live'},
                 'lead': 'Two objects, both neutral to start with, both dry. Choose what is in '
                         'each hand and how many strokes you give them.',
                 'per': 2000000000.0,
                 'stroke_tau': 14,
                 'stroke_ceil': 26.3,
                 'band_anchor': 's-think',
                 'band_at': 1,
                 'start_a': 5,
                 'start_b': 2,
                 'a_label': 'In your left hand',
                 'b_label': 'In your right hand',
                 'gap_label': 'ELECTRONS',
                 'left_label': 'LEFT HAND',
                 'right_label': 'RIGHT HAND',
                 'proton_label': 'PROTONS DO NOT MOVE',
                 'gate': {'prompt': 'Commit first. You rub a polythene rod with a second, '
                                    'identical polythene rod. What happens?',
                          'options': ['Both become negative, because polythene always ends up '
                                      'negative',
                                      'Nothing happens — identical materials hold their electrons '
                                      'equally tightly, so none cross',
                                      'One becomes positive and the other negative, chosen at '
                                      'random',
                                      'Both become positive, because the friction removes '
                                      'electrons into the air'],
                          'answer': 1},
                 'rubs': {'label': 'Strokes',
                          'min': 1,
                          'max': 20,
                          'step': 1,
                          'start': 8,
                          'value': '8 strokes'},
                 'materials': [{'id': 'hair', 'label': 'Hair', 'name': 'HUMAN HAIR'},
                               {'id': 'glass', 'label': 'Glass', 'name': 'GLASS ROD'},
                               {'id': 'acetate', 'label': 'Acetate', 'name': 'ACETATE STRIP'},
                               {'id': 'wool', 'label': 'Wool', 'name': 'WOOL DUSTER'},
                               {'id': 'cotton', 'label': 'Cotton', 'name': 'COTTON CLOTH'},
                               {'id': 'polythene', 'label': 'Polythene', 'name': 'POLYTHENE ROD'},
                               {'id': 'pvc', 'label': 'PVC', 'name': 'PVC PIPE'}],
                 'readouts': [{'id': 'crossed', 'label': 'Electrons that crossed', 'sub': '—'},
                              {'id': 'a', 'label': 'Left-hand object', 'sub': '—'},
                              {'id': 'b', 'label': 'Right-hand object', 'sub': '—'},
                              {'id': 'total',
                               'label': 'The two added together',
                               'value': '0.0 nC',
                               'sub': 'nothing was created'}],
                 'branches': {'same': {'dir': 'neither way',
                                       'note': 'Both hands hold {aname}, so the two surfaces hold '
                                               'their electrons equally tightly and there is no '
                                               'reason for any of them to prefer one side. Nothing '
                                               'crosses, both objects stay neutral, and neither '
                                               'will pick up a scrap of paper. Rubbing on its own '
                                               'does nothing — it takes two different materials.'},
                              'left_above': {'dir': 'left hand to right hand',
                                             'note': '{aname} sits above {bname} on the list, so '
                                                     'it holds its electrons less tightly and '
                                                     'gives them up: {n} of them cross to the '
                                                     'right hand. That leaves the {a} with more '
                                                     'protons than electrons, at {aq}, and the {b} '
                                                     'with more electrons than protons, at {bq}. '
                                                     'Equal and opposite, from one transfer. They '
                                                     'are {steps} apart on the list and you gave '
                                                     '{rubs}, and both of those raise the count. '
                                                     '{ceiling}'},
                              'left_below': {'dir': 'right hand to left hand',
                                             'note': '{aname} sits below {bname} on the list, so '
                                                     'it holds its electrons more tightly and '
                                                     'takes some: {n} of them cross from the right '
                                                     'hand to the left. The {a} ends up at {aq} '
                                                     'and the {b} at {bq}. Swapping which hand '
                                                     'holds which object changes nothing about who '
                                                     'gains and who loses — that is set by the '
                                                     'materials, not by the hands. {ceiling}'}},
                 'words': {'unchanged': 'unchanged',
                           'short': 'short of electrons',
                           'extra': 'extra electrons',
                           'ceiling': 'Keep stroking and the gain per stroke gets smaller — the '
                                      'charge levels off towards a ceiling rather than climbing '
                                      'without limit.',
                           'ceiling_near': 'Each extra stroke is now adding less than the one '
                                           'before it: the charge is levelling off towards a '
                                           'ceiling, because it leaks away into the air as fast as '
                                           'more of it is separated.'},
                 'id': 'rub',
                 'kind': 'transfer-pair',
                 'demand': 'investigate'},
                {'eyebrow': 'The figure',
                 'heading': 'Which way the electrons go',
                 'lead': 'Materials can be put in an order by how tightly they hold their outer '
                         'electrons. Rub any two together and the one higher up this list loses '
                         'electrons to the one lower down, so the higher one ends up positive. The '
                         'further apart they are on the list, the more electrons cross.',
                 'ladder': {'top_label': 'Loses electrons',
                            'bottom_label': 'Gains electrons',
                            'rows': [{'num': '1',
                                      'name': 'Human hair',
                                      'tone': 'loses',
                                      'tell': 'most likely to end up positive'},
                                     {'num': '2', 'name': 'Glass rod', 'tone': 'loses'},
                                     {'num': '3', 'name': 'Acetate strip', 'tone': 'loses'},
                                     {'num': '4', 'name': 'Wool duster', 'tone': 'loses'},
                                     {'num': '5',
                                      'name': 'Cotton cloth',
                                      'tone': 'middle',
                                      'tell': 'middling — poor at either job'},
                                     {'num': '6', 'name': 'Polythene rod', 'tone': 'gains'},
                                     {'num': '7',
                                      'name': 'PVC pipe',
                                      'tone': 'gains',
                                      'tell': 'most likely to end up negative'}]},
                 'close': 'Nothing on this list is a conductor or an insulator by accident: every '
                          'one is an insulator, which is what lets the charge stay where the '
                          'rubbing put it. Try the same experiment with a metal rod held in your '
                          'hand and no charge builds up at all — it runs away through you.',
                 'id': 'tribo',
                 'kind': 'charge-band',
                 'demand': 'investigate'}],
 'figures': [],
 'key_facts': [{'id': 'rubbing-separates-charge',
                'eyebrow': 'Key fact',
                'ground': 'card',
                'placement': 'top-level',
                'text': 'Rubbing two insulators together transfers electrons from one surface to '
                        'the other. Protons never move. The object that loses electrons is left '
                        'positive, the one that gains them is negative, both by the same amount — '
                        'so no charge is created and the two together are still neutral.'}],
 'ladder': {'recall': {'q': 'A glass rod is rubbed with a wool duster. Glass sits above wool on '
                            'the list, so which statement is right?',
                       'options': ['The glass loses electrons and becomes positive; the wool gains '
                                   'them and becomes negative.',
                                   'The glass gains electrons and becomes negative; the wool loses '
                                   'them and becomes positive.',
                                   'The glass becomes positive because protons move onto it from '
                                   'the wool.',
                                   'The glass becomes positive and the wool stays neutral, because '
                                   'only one object is rubbed.'],
                       'answer': 0,
                       'feedback': {1: 'That is the transfer the wrong way. Material higher on the '
                                       'list holds its electrons less tightly, so glass gives them '
                                       'up and ends positive.',
                                    2: 'The sign is right and the mechanism is not. Protons are '
                                       'locked in nuclei; the glass is positive because electrons '
                                       'have left it.',
                                    3: 'Both surfaces take part. Every electron that leaves the '
                                       'glass arrives on the wool, so the wool must end up '
                                       'negatively charged by the same amount.'},
                       'title': 'Rung 1 · Predict the signs'},
            'apply': {'q': 'A student rubs a balloon on a jumper, finds the balloon negative, and '
                           'says the friction created the negative charge. What is right?',
                      'options': ['The student is right — friction turns movement into electric '
                                  'charge, which is why you have to rub hard.',
                                  'No charge was created, because the balloon and the jumper end '
                                  'up with the same charge as each other.',
                                  'No charge was created. Electrons moved from the jumper to the '
                                  'balloon, so the jumper is now positive by exactly as much as '
                                  'the balloon is negative.',
                                  'Charge was created, but an equal amount of positive charge was '
                                  'created on the jumper at the same time, so the two new charges '
                                  'balance and the total stays zero.'],
                      'answer': 2,
                      'feedback': {0: 'Rubbing hard makes more contact, not more charge from '
                                      'nothing. The electrons on the balloon all came off the '
                                      'jumper.',
                                   1: 'The verdict is right and the detail is wrong. They end up '
                                      'with opposite charges of the same size — that is what makes '
                                      'the total still zero.',
                                   3: 'Nothing was created on either side. The positive charge on '
                                      'the jumper is protons that were always there, left '
                                      'unbalanced by the electrons that walked off.'},
                      'title': 'Rung 2 · The one that catches people'},
            'explain': {'q': 'A polythene rod is rubbed with a woollen duster and ends up '
                             'negatively charged. Explain what has happened, naming what moves and '
                             'what does not, and say what the duster is now.',
                        'field_label': 'Your explanation',
                        'placeholder': 'Both objects started neutral, so…',
                        'success': ['Says both objects started neutral, with protons and electrons '
                                    'balanced.',
                                    'Says electrons moved from the wool to the polythene.',
                                    'Says protons do not move, because they are held in the '
                                    'nuclei.',
                                    'Says the rod is negative because it has more electrons than '
                                    'protons.',
                                    'Says the duster is now positively charged, by the same '
                                    'amount, so the total charge is still zero.'],
                        'title': 'Rung 3 · Explain'},
            'produce': {'q': 'A road tanker delivering fuel is connected to a metal spike in the '
                             'ground before any fuel is pumped, and the pumping is stopped if the '
                             'connection comes off. Explain what is being prevented, and why the '
                             'same precaution is pointless for a plastic bottle of water.',
                        'field_label': 'Your answer',
                        'placeholder': 'Fuel rubbing through the pipe…',
                        'success': ['Says fuel flowing through a pipe rubs against it, so charge '
                                    'is separated.',
                                    'Says charge building up on the tanker or the fuel could reach '
                                    'a p.d. large enough to spark.',
                                    'Says a spark near fuel vapour could ignite it.',
                                    'Says the earthing wire is a conductor, so it lets the '
                                    'separated charge flow away instead of building up.',
                                    'Says earthing a plastic bottle achieves nothing, because '
                                    'plastic is an insulator and the charge cannot travel along it '
                                    'to the wire.'],
                        'title': 'Rung 4 · Take it somewhere new'}},
 'key_note': 'In a neutral object the protons and electrons balance. Rubbing two insulators '
             'together presses their surfaces into contact at many points, and electrons cross '
             'from the material that holds them less tightly to the one that holds them more '
             'tightly. Protons never move. The object that loses electrons is left positively '
             'charged and the one that gains them negatively charged, by exactly the same amount, '
             'so no charge has been created — it has been separated. It only works with '
             'insulators, because a conductor lets the charge escape.',
 'stretch': [{'id': 'the-order-of-materials',
              'type': 'explainer',
              'text': 'The order of materials is called the triboelectric series, and the honest '
                      'truth is that published versions disagree with each other. Where a material '
                      'lands depends on how rough its surface is, how clean it is, how humid the '
                      'room is and even which way it was rubbed, and some pairs reverse if you '
                      'swap a polished sample for a scratched one. The list is a reliable guide '
                      'for glass, polythene and PVC, and a rough one in the middle — which is why '
                      'cotton, sitting near the middle, is a poor choice for a demonstration.'},
             {'id': 'humidity',
              'type': 'explainer',
              'text': 'Humidity is the reason this experiment fails on a wet day. Water is a far '
                      'better conductor than any of these materials, and a film of it a few '
                      'molecules thick on the surface is enough to let charge creep away as fast '
                      'as the rubbing separates it. Winter is the season of static shocks for the '
                      'same reason: cold air holds very little water, so indoor air that has been '
                      'heated is extremely dry, and charge separated by your shoes on a carpet has '
                      'nowhere to go until you touch a door handle.'}],
 'support': [],
 'vocabulary': [{'term': 'charge',
                 'definition': 'What an object has when its protons and electrons no longer '
                               'balance. Positive means short of electrons, negative means holding '
                               'extra ones.'},
                {'term': 'electron',
                 'definition': 'The negatively charged particle on the outside of an atom, and the '
                               'only thing that moves when something is charged by rubbing.'},
                {'term': 'insulator',
                 'definition': 'A material charge cannot travel through. Rubbing only charges '
                               'insulators, because a conductor lets the charge run away.'},
                {'term': 'triboelectric series',
                 'definition': 'Materials put in order of how tightly they hold their outer '
                               'electrons. A likely guide to which way the transfer goes, not a '
                               'guarantee.'}],
 'tutor': {'anchor': 's-rub',
           'prompt': 'Ask Mr Badmus AI',
           'body': 'Got two materials and want to know which one ends up negative?',
           'cta': 'Ask about this lesson'},
 'ks4_becomes': 'Charge measured in coulombs, sparking and the breakdown of air, and the uses and '
                'dangers of static charge in industry.',
 'convention_note': 'The bench is a teaching model. The order of the seven materials is the '
                    'commonly published one, but real triboelectric series disagree with each '
                    "other and a material's position shifts with surface roughness, cleanliness "
                    'and humidity — so the direction of transfer for two materials close together '
                    'on the list should be treated as a likely outcome, not a certainty. The '
                    'number of electrons is generated by a simple rule — it rises with the number '
                    'of steps apart on the list and with the number of strokes, but the stroke '
                    'term levels off towards a ceiling rather than climbing without limit, because '
                    'a real charge leaks away and because the air eventually breaks down. The '
                    'figures are chosen to give charges of the order of a few nanocoulombs, which '
                    'is typical of a rubbed rod, and are not measurements. Charges are rounded to '
                    'one decimal place.',
 'ws': ['measurement'],
 'authored': True}
