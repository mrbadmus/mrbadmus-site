# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 P9 `forces-between-charges` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 7176d7049d. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'P9'
SOURCE_SLUG = 'forces-between-charges'
FROZEN_FROM = '7176d7049d'

LESSON = {'slug': 'forces-between-charges',
 'title': 'Forces between charges',
 'discipline': 'physics',
 'unit': 'Static electricity',
 'family': 'MODEL',
 'covers': ['KS3.P.STAT.01b'],
 'touches': ['KS3.WS.ANA.01'],
 'beyond_statutory': False,
 'threads': [{'id': 'electricity', 'level': 2}],
 'typical_year': 8,
 'typical_minutes': 60,
 'requires': ['charging-by-rubbing'],
 'assumes': [],
 'references': [{'unit': 'P8', 'lesson': 'conductors-and-insulators'},
                {'unit': 'P8', 'lesson': 'current-and-circuits'}],
 'ks4_links': [],
 'meta_description': 'Like charges push apart and unlike charges pull together — and a charged '
                     'object also pulls on something with no charge at all.',
 'big_question': 'What does a charged object do to the things near it?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Two balloons', 'done_when': 'committed'},
          {'anchor': 's-spheres',
           'short': 'BENCH',
           'label': 'Charge them, move them',
           'done_when': 'gate_and_a_control'},
          {'anchor': 's-matrix',
           'short': 'TABLE',
           'label': 'Every combination',
           'done_when': 'gate_committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Two balloons, one jumper, two opposite results.',
                'prompt': 'Rub two balloons on the same jumper and hang them side by side on '
                          'threads: they swing away from each other and refuse to touch. Take '
                          'either one and hold it near the wall and it sticks there.',
                'commit': 'If you had to guess, does the wall have a charge of its own?',
                'options': ['Yes, it has a charge', 'No, it has none'],
                'answer': 1,
                'reveal': 'That shifting is called induction. Next: charge two spheres and move '
                          'them to see exactly what they do.',
                'guess': True,
                'replies': ['A charged wall would explain it, since opposite charges attract. But '
                            'the wall started with no charge and still has none overall; the '
                            "balloon just shifts the wall's own electrons.",
                            "The wall has no charge overall. The balloon shifts the wall's own "
                            'electrons, so the surface nearest it becomes slightly opposite and '
                            'pulls the balloon in.']},
 'misconceptions': [{'id': 'CHRG-05',
                     'statement': 'The rod picks up the paper, so the paper must be charged.',
                     'elicited_by': 'spheres',
                     'confronted_by': 's-think'},
                    {'id': 'CHRG-06',
                     'statement': 'They have to touch, or the air has to carry it.',
                     'elicited_by': 's-hook',
                     'confronted_by': 's-think'},
                    {'id': 'CHRG-07',
                     'statement': 'The force between two charges falls in step with the distance, '
                                  'so doubling the gap halves it.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 'spheres'},
                    {'id': 'CHRG-08',
                     'statement': 'A charged object does nothing at all to an uncharged one, '
                                  'because there is no charge for it to act on.',
                     'elicited_by': 'spheres',
                     'confronted_by': 'matrix'}],
 'core': [{'type': 'hook', 'id': 'hook-commit', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Two charged objects push or pull on each other without touching, and the rule '
                   'is short: <strong>like charges repel, unlike charges attract</strong>. Two '
                   'positives push apart. Two negatives push apart. A positive and a negative pull '
                   'together. The two forces are always equal in size and opposite in direction — '
                   'whichever object is smaller or more lightly charged, it feels exactly the same '
                   'pull as the other one.'},
          {'type': 'explainer',
           'text': 'The force gets rapidly weaker as they move apart. Doubling the separation does '
                   'not halve it: it cuts it to about a quarter. That is why static effects are '
                   'dramatic at a centimetre and undetectable across a room.'},
          {'type': 'explainer',
           'text': 'Then the case that surprises people. A charged object also attracts a '
                   'completely <strong>uncharged</strong> one. Bring a negative rod near a scrap '
                   "of paper and the rod's charge pushes the paper's own electrons to the far "
                   'side, leaving the near side slightly positive. The paper is still neutral '
                   'overall — nothing has been added or removed — but its near side is now '
                   'oppositely charged and closer, so the pull wins over the push. This is '
                   '<strong>induction</strong>, and it is the whole reason a rubbed rod picks '
                   'things up.'},
          {'type': 'practical', 'id': 'spheres', 'anchor': 's-spheres'},
          {'type': 'check', 'id': 'matrix', 'anchor': 's-matrix'},
          {'type': 'key-fact', 'ref': 'repulsion-is-the-proof'},
          {'type': 'misconception', 'id': 'think-attraction-proves-nothing', 'anchor': 's-think'},
          {'type': 'figure', 'ref': 'p9-charge-matrix-grid', 'anchor': 's-charge-matrix-grid'},
          {'type': 'quiz', 'anchor': 's-ladder'},
          {'type': 'summary', 'id': 's-keynote'}],
 'activities': [{'id': 'think-attraction-proves-nothing',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'CHRG-05',
                 'statements': [{'quote': 'The rod picks up the paper, so the paper must be '
                                          'charged.',
                                 'targets': 'CHRG-05',
                                 'body': ['The paper came out of a drawer and nobody rubbed it. It '
                                          'is neutral, and it stays neutral the whole time — its '
                                          'total charge never changes. What the rod does is push '
                                          "the paper's own electrons to the far side of it, so the "
                                          'near face becomes slightly opposite to the rod and the '
                                          'far face slightly the same. Both faces feel a force, '
                                          'but the near one is closer, and the force weakens so '
                                          'fast with distance that the near face wins. The paper '
                                          'is pulled in as a whole. Attraction is never proof of '
                                          'charge; only repulsion is.']},
                                {'quote': 'They have to be touching, or there has to be air in '
                                          'between to carry it.',
                                 'targets': 'CHRG-06',
                                 'body': ['Neither. The spheres never touch, and the force is '
                                          'undiminished in a vacuum — two charged objects in an '
                                          'evacuated jar push and pull on each other exactly as '
                                          'they did in air. There is nothing in the gap doing the '
                                          'carrying. That is such a strange claim that physics '
                                          'gives it its own name and its own lesson: the charged '
                                          'object fills the space around it with an <em>electric '
                                          'field</em>, and the field is what the other object '
                                          'responds to.']}]},
                {'eyebrow': 'At the bench · two light spheres on insulating stands',
                 'heading': 'Charge them. Move them.',
                 'progress': {'idle': 'Change a control to begin', 'live': 'Three controls live'},
                 'lead': 'Each sphere can be left neutral or given a positive or a negative charge '
                         'of the same size. The arrows show the force on each one and how strong '
                         'it is.',
                 'k': 100,
                 'ind_k': 8,
                 'ref_d': 4,
                 'band_anchor': 's-matrix',
                 'band_at': 1,
                 'start_a': 2,
                 'start_b': 1,
                 'a_label': 'Left sphere',
                 'b_label': 'Right sphere',
                 'bench_label': 'INSULATING STANDS ON A BENCH',
                 'induced_sub': 'a small fraction of the charged pair at this gap',
                 'gate': {'prompt': 'Commit first. One sphere is charged negative. The other is '
                                    'left completely neutral. What happens?',
                          'options': ['Nothing — a neutral object has no charge, so there is '
                                      'nothing to push or pull on',
                                      'They repel, because the neutral one has as many negatives '
                                      'as the charged one',
                                      'They attract weakly, because the charged one pushes the '
                                      "neutral one's electrons aside",
                                      'They attract strongly, exactly as two opposite charges '
                                      'would'],
                          'answer': 2},
                 'sep': {'label': 'How far apart',
                         'min': 4,
                         'max': 20,
                         'step': 1,
                         'start': 8,
                         'value': '8 cm'},
                 'states': [{'id': 'pos',
                             'label': 'Positive',
                             'q': 1,
                             'word': 'positively charged'},
                            {'id': 'neu', 'label': 'Neutral', 'q': 0, 'word': 'neutral'},
                            {'id': 'neg',
                             'label': 'Negative',
                             'q': -1,
                             'word': 'negatively charged'}],
                 'strength_bands': [{'at_least': 70, 'word': 'very strong'},
                                    {'at_least': 30, 'word': 'strong'},
                                    {'at_least': 10, 'word': 'moderate'},
                                    {'at_least': 3, 'word': 'weak'},
                                    {'at_least': 0.5, 'word': 'very weak'},
                                    {'at_least': 0, 'word': 'far too weak to see'}],
                 'readouts': [{'id': 'verdict', 'label': 'What happens', 'sub': '—'},
                              {'id': 'strength', 'label': 'How strong', 'sub': '—'},
                              {'id': 'sep', 'label': 'Separation', 'sub': 'centre to centre'},
                              {'id': 'pair', 'label': 'Force on each sphere'}],
                 'branches': {'none': {'verdict': 'nothing happens',
                                       'sub': 'both spheres neutral',
                                       'note': 'Neither sphere carries a charge, so there is '
                                               'nothing to push or pull with, and the arrows are '
                                               'gone. Move them as close as you like and nothing '
                                               'changes. This is the one case in the whole table '
                                               'that gives no force — which is worth noticing, '
                                               'because “neutral” is not the same as “nothing to '
                                               'do with electricity”.'},
                              'repel': {'verdict': 'they repel',
                                        'sub': 'both positive',
                                        'sub_alt': 'both negative',
                                        'note': 'Both spheres are {sign} — like charges — so each '
                                                'is pushed away from the other, with equal and '
                                                'opposite forces. At {d} cm the strength is '
                                                '{strength} on this scale. Halve the separation '
                                                'and it goes up about four times; double it and it '
                                                'drops to about a quarter. Repulsion is the only '
                                                'result that proves both objects are charged.'},
                              'attract': {'verdict': 'they attract',
                                          'sub': 'one positive, one negative',
                                          'note': 'One sphere is positive and one negative — '
                                                  'unlike charges — so each is pulled towards the '
                                                  'other, with equal and opposite forces. At {d} '
                                                  'cm the strength is {strength} on this scale, '
                                                  'the same size as the repulsion between two like '
                                                  'charges at the same distance. Only the '
                                                  'direction changed.'},
                              'induced': {'verdict': 'they attract, weakly',
                                          'sub': 'induction on the neutral sphere',
                                          'note': 'The {cside} sphere is {csign} and the {nside} '
                                                  'one has no charge at all — and they still '
                                                  'attract. Only electrons move, and only the '
                                                  "neutral sphere's own: a negative charge pushes "
                                                  'them away to the far face, a positive charge '
                                                  'pulls them towards the near face. Here that '
                                                  'leaves the near face slightly {nearsign} and '
                                                  'the far face slightly {farsign}. Both faces '
                                                  'feel a force, but the near one is closer and '
                                                  'closeness matters enormously, so the pull wins. '
                                                  'It is much weaker than the pull two oppositely '
                                                  'charged spheres would give across the same gap, '
                                                  'and it dies away faster still as you separate '
                                                  "them. The neutral sphere's total charge is "
                                                  'unchanged throughout.'}},
                 'words': {'zero_word': 'no force at all',
                           'zero_sub': 'zero on this scale',
                           'scale_sub': '{strength} where 100 is the strongest shown',
                           'pair': 'equal and opposite',
                           'pair_none': 'none on either'},
                 'id': 'spheres',
                 'kind': 'charge-pair',
                 'demand': 'investigate'},
                {'eyebrow': 'The figure',
                 'heading': 'Every combination there is',
                 'lead': 'Two objects, three states each, nine cases. Only one of the nine '
                         'produces nothing at all — which is worth noticing, because the usual '
                         'summary of this topic mentions two.',
                 'matrix': {'corner': 'Left / right',
                            'columns': ['Positive', 'Neutral', 'Negative'],
                            'rows': [{'head': 'Positive',
                                      'cells': [{'text': '<strong>Repel</strong> — like charges',
                                                 'strong': True},
                                                {'text': 'Attract weakly — induction'},
                                                {'text': '<strong>Attract</strong> — unlike '
                                                         'charges',
                                                 'strong': True}]},
                                     {'head': 'Neutral',
                                      'cells': [{'text': 'Attract weakly — induction'},
                                                {'text': 'Nothing'},
                                                {'text': 'Attract weakly — induction'}]},
                                     {'head': 'Negative',
                                      'cells': [{'text': '<strong>Attract</strong> — unlike '
                                                         'charges',
                                                 'strong': True},
                                                {'text': 'Attract weakly — induction'},
                                                {'text': '<strong>Repel</strong> — like charges',
                                                 'strong': True}]}]},
                 'close': 'This gives you a test worth remembering. <strong>Attraction proves '
                          'nothing</strong> — an object that is pulled towards a charged rod might '
                          'be oppositely charged, or might have no charge at all. Only '
                          '<strong>repulsion</strong> is proof, because nothing but a like charge '
                          'can push.',
                 'id': 'matrix',
                 'kind': 'charge-band',
                 'demand': 'investigate'}],
 'figures': [{'id': 'p9-charge-matrix-grid',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'p9-charge-matrix',
              'title': 'A 3 by 3 grid of every combination of two charged objects',
              'desc': 'A grid with a blank corner, headed Positive, Neutral and Negative across '
                      'the top and down the left side. Each of the nine cells inside holds a short '
                      'verdict: the Positive row reads Repel, Attract weakly, Attract; the Neutral '
                      'row reads Attract weakly, Nothing, Attract weakly; the Negative row reads '
                      'Attract, Attract weakly, Repel.',
              'caption': 'The same grid as earlier in this lesson.',
              'grid': {'columns': ['Positive', 'Neutral', 'Negative'],
                       'rows': [{'head': 'Positive',
                                 'cells': [{'line1': 'Repel',
                                            'line2': 'like charges',
                                            'strong': True},
                                           {'line1': 'Attract weakly', 'line2': 'induction'},
                                           {'line1': 'Attract',
                                            'line2': 'unlike charges',
                                            'strong': True}]},
                                {'head': 'Neutral',
                                 'cells': [{'line1': 'Attract weakly', 'line2': 'induction'},
                                           {'line1': 'Nothing', 'line2': ''},
                                           {'line1': 'Attract weakly', 'line2': 'induction'}]},
                                {'head': 'Negative',
                                 'cells': [{'line1': 'Attract',
                                            'line2': 'unlike charges',
                                            'strong': True},
                                           {'line1': 'Attract weakly', 'line2': 'induction'},
                                           {'line1': 'Repel',
                                            'line2': 'like charges',
                                            'strong': True}]}]}}],
 'key_facts': [{'id': 'repulsion-is-the-proof',
                'eyebrow': 'Key fact',
                'ground': 'card',
                'placement': 'top-level',
                'text': 'Like charges repel and unlike charges attract, with equal and opposite '
                        'forces that weaken quickly with distance. A charged object also attracts '
                        "a neutral one, by moving that object's own electrons to one side. So "
                        'repulsion proves an object is charged; attraction does not.'}],
 'ladder': {'recall': {'q': 'A negatively charged rod is held near a hanging metal-coated ball on '
                            'a thread. The ball swings towards the rod. What can you conclude '
                            'about the ball?',
                       'options': ['It must be positively charged, because unlike charges attract',
                                   'Nothing certain — it could be positively charged, or it could '
                                   'be neutral',
                                   'It must be neutral, because a charged ball would have been '
                                   'pushed away',
                                   'It must be negatively charged, because the rod is negative'],
                       'answer': 1,
                       'feedback': {0: 'A positive ball would be attracted, but so would a neutral '
                                       'one — by induction. Attraction cannot tell the two apart; '
                                       'only repulsion is proof.',
                                    2: 'A ball with a like charge would be pushed away. A ball '
                                       'with the opposite charge would be pulled in just as a '
                                       'neutral one is.',
                                    3: 'Two negatives repel, so a negative ball is the one thing '
                                       'this observation rules out.'},
                       'title': 'Rung 1 · Predict'},
            'apply': {'q': 'Two identical spheres carrying the same charge repel with a certain '
                           'force at 5 cm. They are moved to 10 cm apart. What happens to the '
                           'force?',
                      'options': ['It falls to about half, because the distance doubled',
                                  'It stays the same, because neither charge has changed',
                                  'It falls to about a quarter on the nearer sphere and stays the '
                                  'same on the further one',
                                  'It falls to about a quarter of what it was'],
                      'answer': 3,
                      'feedback': {0: 'The force does not simply track the distance. Doubling the '
                                      'separation cuts it to about a quarter, which is why static '
                                      'effects vanish so quickly.',
                                   1: 'The charges have not changed, but the force between charges '
                                      'depends on how far apart they are as well as how big they '
                                      'are.',
                                   2: 'The quarter is right, but it applies to both. The two '
                                      'forces are always equal in size and opposite in direction, '
                                      'however different the spheres are.'},
                      'title': 'Rung 2 · The one that catches people'},
            'explain': {'q': 'A balloon rubbed on a jumper sticks to a wall that nobody has '
                             'charged. Explain how a charged object can be attracted to an '
                             'uncharged one.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The balloon is charged and the wall is not, so…',
                        'success': ['Says the balloon is charged and the wall is neutral, and '
                                    'stays neutral throughout.',
                                    'Says the balloon’s charge pushes the wall’s own electrons to '
                                    'one side.',
                                    'Says the near surface of the wall ends up with the opposite '
                                    'charge to the balloon.',
                                    'Says the far side ends up with the same charge as the '
                                    'balloon, so it is pushed away.',
                                    'Says the near side wins because the force weakens quickly '
                                    'with distance, so the balloon is pulled in overall.'],
                        'title': 'Rung 3 · Explain'},
            'produce': {'q': 'You are given two identical hanging balls, one of which you know is '
                             'charged, and no other apparatus. Describe how you would find out '
                             'whether the second ball is charged too, and explain why one possible '
                             'result would tell you nothing.',
                        'field_label': 'Your answer',
                        'placeholder': 'Bring the two balls near each other and watch…',
                        'success': ['Describes bringing the two balls close and watching whether '
                                    'they move apart or together.',
                                    'Says that repulsion shows the second ball is charged, with '
                                    'the same sign as the first.',
                                    'Says that attraction is the ambiguous result.',
                                    'Explains why: an oppositely charged ball and a neutral ball '
                                    'both get attracted.',
                                    'Concludes that only a repulsion answers the question, so a '
                                    'single attraction is not a result you can report.'],
                        'title': 'Rung 4 · Take it somewhere new'}},
 'key_note': 'Charged objects push and pull on each other without touching. Like charges repel, '
             'unlike charges attract, and the two forces are always equal in size and opposite in '
             'direction. The force weakens quickly as the separation grows — doubling the distance '
             'cuts it to about a quarter. A charged object also attracts a neutral one, because it '
             "moves that object's own electrons to one side and the closer, opposite face wins. So "
             'repulsion is proof that an object is charged, and attraction is not.',
 'stretch': [{'id': 'stronger-than-gravity',
              'type': 'explainer',
              'text': 'The electric force is staggeringly strong compared with gravity. Between '
                      'two protons it beats their gravitational attraction by a factor of about '
                      'ten thousand million million million million million million. You never '
                      'notice, because matter is so precisely balanced: every object you have ever '
                      'picked up has its positive and negative charges matched to an extraordinary '
                      'accuracy, and the tiny imbalance a duster can produce is enough to lift '
                      'paper against the pull of the whole Earth.'},
             {'id': 'induction-at-work',
              'type': 'explainer',
              'text': 'Induction is quietly useful. Electrostatic paint spraying gives the paint '
                      'droplets a charge and the car body the opposite one, so the paint is pulled '
                      'onto the metal and wraps round edges instead of drifting past; a '
                      'power-station precipitator charges the smoke particles and collects them on '
                      'plates, taking out most of the ash before it reaches the chimney. Both work '
                      'on the case in the middle of the table — charge one thing, and something '
                      'uncharged comes to you.'}],
 'support': [],
 'vocabulary': [{'term': 'repel',
                 'definition': 'To push apart. Two charges of the same sign always repel, and '
                               'repulsion is the only proof that both objects are charged.'},
                {'term': 'attract',
                 'definition': 'To pull together. Two opposite charges attract — and so do a '
                               'charged object and a neutral one, which is why attraction proves '
                               'nothing on its own.'},
                {'term': 'induction',
                 'definition': "A charged object moving a neutral object's own electrons to one "
                               'side, so the near face becomes opposite and the whole object is '
                               "pulled in. The neutral object's total charge never changes."}],
 'tutor': {'anchor': 's-spheres',
           'prompt': 'Ask Mr Badmus AI',
           'body': 'Got two objects and want to know whether they attract, repel or do nothing?',
           'cta': 'Ask about this lesson'},
 'ks4_becomes': 'Electric field lines and their direction, and the inverse-square dependence '
                'stated properly.',
 'convention_note': 'The bench is a teaching model. Both charges are treated as equal in size and '
                    'as sitting at the centre of each sphere, and the strength is reported as a '
                    'relative figure with the closest fully charged case set to 100 — no force in '
                    'newtons is given anywhere on the bench, because the equation for it is beyond '
                    'this stage and any number in newtons here would be invented rather than '
                    'measured. Induced attraction on a neutral sphere is reported in relative '
                    'words only, never as a figure, because the size of that effect is a chosen '
                    'coefficient rather than a measurement. The relative figure falls as the '
                    'square of the separation for two charged spheres, which is the real '
                    'relationship; the much weaker attraction to a neutral sphere is modelled as '
                    'falling faster still, which is the right behaviour but the coefficient is '
                    'chosen to be readable rather than measured. Real spheres are not points, so '
                    'at the closest separations the true force is somewhat larger than the model '
                    'gives. The induced charges drawn on a neutral sphere are indicative, and the '
                    "sphere's total charge stays zero throughout.",
 'ws': ['measurement'],
 'authored': True}
