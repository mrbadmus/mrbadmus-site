# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 P9 `electric-fields` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 7176d7049d. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'P9'
SOURCE_SLUG = 'electric-fields'
FROZEN_FROM = '7176d7049d'

LESSON = {'slug': 'electric-fields',
 'title': 'Electric fields',
 'discipline': 'physics',
 'unit': 'Static electricity',
 'family': 'MODEL',
 'covers': ['KS3.P.STAT.02'],
 'touches': ['KS3.WS.ANA.01'],
 'beyond_statutory': False,
 'threads': [{'id': 'electricity', 'level': 3}],
 'typical_year': 8,
 'typical_minutes': 60,
 'requires': ['forces-between-charges'],
 'assumes': [],
 'references': ['charging-by-rubbing',
                {'unit': 'P8', 'lesson': 'potential-difference'},
                {'unit': 'P8', 'lesson': 'current-and-circuits'}],
 'ks4_links': [],
 'meta_description': 'Nothing crosses the gap. A charged object changes the space around it '
                     'instead, and anything charged that arrives feels a push or a pull straight '
                     'away.',
 'big_question': 'How can one thing push or pull on another across a gap when nothing touches?',
 'rail': [{'anchor': 's-hook',
           'short': 'WATER',
           'label': 'Comb and water',
           'done_when': 'committed'},
          {'anchor': 's-field',
           'short': 'BENCH',
           'label': 'Move the test point',
           'done_when': 'gate_and_a_control'},
          {'anchor': 's-reach',
           'short': 'FIELDS',
           'label': 'Three forces',
           'done_when': 'gate_committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'The comb bends the water without touching it.',
                'prompt': 'Run a tap down to the thinnest steady stream it will give and bring a '
                          'comb you have just pulled through dry hair up to the side of it. The '
                          'stream bends towards the comb, from a couple of centimetres away, and '
                          'nothing is touching anything.',
                'commit': 'If you had to guess, does the comb need the air between it and the '
                          'water to bend the stream?',
                'options': ['Yes, it needs air', 'No, it does not'],
                'answer': 1,
                'reveal': 'That changed space around a charged object is called an electric field. '
                          'Next: map one and move a test point around inside it.',
                'guess': True,
                'replies': ['Air is the only thing in the gap. But charged objects push and pull '
                            'just the same with all the air pumped out.',
                            'The air plays no part. Charged objects push and pull just as strongly '
                            'with all the air pumped out, because the comb changes the space '
                            'itself.']},
 'misconceptions': [{'id': 'CHRG-09',
                     'statement': 'A field only exists when something is in it to feel it.',
                     'confronted_by': 's-think'},
                    {'id': 'CHRG-10',
                     'statement': 'The air in the gap must be carrying the force.',
                     'elicited_by': 's-hook',
                     'confronted_by': 's-think'},
                    {'id': 'CHRG-11',
                     'statement': 'The field is strongest half-way between two like charges.',
                     'elicited_by': 'field',
                     'confronted_by': 'field'},
                    {'id': 'CHRG-12',
                     'statement': 'A negative charge follows the field arrows, the same way a '
                                  'positive one does.',
                     'elicited_by': 's-ladder',
                     'confronted_by': 'field'}],
 'core': [{'type': 'hook', 'id': 'hook-commit', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Two charged objects push and pull on each other across a gap with nothing in '
                   'between, and that is genuinely strange. Physics deals with it by splitting the '
                   'problem in two. First, a charged object fills the space around it with an '
                   '<strong>electric field</strong>. Second, anything charged that finds itself in '
                   'that space feels a force from the field where it is standing.'},
          {'type': 'explainer',
           'text': 'So the field is a property of <em>space itself</em>, not of the object that '
                   'made it and not of the object that feels it. It has a value at every point, '
                   'and that value has a size and a direction. A field arrow is drawn pointing the '
                   'way a <strong>small positive charge</strong> would be pushed if you put one '
                   'there — which means arrows point away from positive charges and towards '
                   'negative ones. A negative charge put at the same point feels a force the other '
                   'way.'},
          {'type': 'explainer',
           'text': 'Two things follow. The field is there whether or not anything is in it, '
                   'waiting; and the field is what carries the interaction across the gap, so no '
                   'air, no wire and no contact is needed. In a vacuum it works exactly the same.'},
          {'type': 'practical', 'id': 'field', 'anchor': 's-field'},
          {'type': 'check', 'id': 'reach', 'anchor': 's-reach'},
          {'type': 'key-fact', 'ref': 'a-field-fills-the-space'},
          {'type': 'misconception', 'id': 'think-the-field-is-there-first', 'anchor': 's-think'},
          {'type': 'figure', 'ref': 'p9-field-point-marked', 'anchor': 's-field-point-marked'},
          {'type': 'quiz', 'anchor': 's-ladder'},
          {'type': 'summary', 'id': 's-keynote'}],
 'activities': [{'id': 'think-the-field-is-there-first',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'CHRG-09',
                 'statements': [{'quote': 'The field only exists when there is something in it to '
                                          'feel it.',
                                 'targets': 'CHRG-09',
                                 'body': ['The field is there first. That is the whole point of '
                                          'inventing it: instead of saying two objects '
                                          'mysteriously know about each other across a gap, we say '
                                          'the first one changes the space, and the second one '
                                          'only ever responds to the space it is standing in. Take '
                                          'the second object away and the field is unchanged — put '
                                          'anything charged back at that point, at any moment, and '
                                          'it is pushed the same way. Bring in something twice as '
                                          'charged and the force doubles while the field stays '
                                          'exactly as it was.']},
                                {'quote': 'The air in between must be carrying it.',
                                 'targets': 'CHRG-10',
                                 'body': ['Pump the air out and nothing changes. Two charged '
                                          'objects in an evacuated jar attract and repel exactly '
                                          "as they did, and the same is true of the Sun's "
                                          'gravitational pull on the Earth across 150 million '
                                          'kilometres of almost nothing. Air is not the messenger; '
                                          'it is not even in the way. What is between them is the '
                                          'field, and a field does not need a material to sit in — '
                                          'the same discovery that made light so strange, for '
                                          'exactly the same reason.']}]},
                {'eyebrow': 'At the bench · a field map and one test point',
                 'heading': 'Move the test point around.',
                 'progress': {'idle': 'Change a control to begin', 'live': 'Both controls live'},
                 'lead': 'The small arrows are the field, sampled on a grid: each one shows which '
                         'way a small positive charge would be pushed there, and how hard. The big '
                         'arrow is your test point.',
                 'eref': 0.00025,
                 'x0': 80,
                 'dx': 35,
                 'near': 62,
                 'band_anchor': 's-reach',
                 'band_at': 1,
                 'start_setup': 2,
                 'setup_label': 'What is making the field',
                 'convention_label': 'EVERY ARROW POINTS THE WAY A SMALL POSITIVE CHARGE WOULD BE '
                                     'PUSHED',
                 'gate': {'prompt': 'Commit first. Two equal positive charges sit a few '
                                    'centimetres apart. What is the field at the point exactly '
                                    'half-way between them?',
                          'options': ['The strongest field on the whole map, because it is close '
                                      'to both charges',
                                      'Zero — the two pushes are equal and exactly opposite, so '
                                      'they cancel',
                                      'Twice the field of one charge on its own at that distance',
                                      'Half the field of one charge on its own, because the two '
                                      'are shared'],
                          'answer': 1},
                 'pos': {'label': 'Where the test point sits',
                         'min': 0,
                         'max': 24,
                         'step': 1,
                         'start': 12,
                         'value': 'step 12 of 24'},
                 'setups': [{'id': 'one-pos',
                             'label': 'One positive charge',
                             'charges': [{'x': 490, 'q': 1}]},
                            {'id': 'one-neg',
                             'label': 'One negative charge',
                             'charges': [{'x': 490, 'q': -1}]},
                            {'id': 'dipole',
                             'label': 'A positive and a negative',
                             'charges': [{'x': 350, 'q': 1}, {'x': 650, 'q': -1}]},
                            {'id': 'two-pos',
                             'label': 'Two positives',
                             'charges': [{'x': 350, 'q': 1}, {'x': 650, 'q': 1}]}],
                 'strength_bands': [{'at_least': 90, 'word': 'very strong'},
                                    {'at_least': 35, 'word': 'strong'},
                                    {'at_least': 10, 'word': 'moderate'},
                                    {'at_least': 2, 'word': 'weak'},
                                    {'at_least': 0, 'word': 'very weak'}],
                 'readouts': [{'id': 'dir', 'label': 'The field at your point', 'sub': '—'},
                              {'id': 'strength', 'label': 'How strong it is there', 'sub': '—'},
                              {'id': 'posf', 'label': 'A small positive charge here'},
                              {'id': 'negf', 'label': 'A small negative charge here'}],
                 'branches': {'on_charge': {'sub': 'inside the charge itself',
                                            'note': 'Your test point has landed on top of a '
                                                    'charge. The model treats charges as points, '
                                                    'so it gives no sensible value there — which '
                                                    'is why the grid arrows are left out close in '
                                                    'as well. Slide the test point away and the '
                                                    'field reappears, stronger the nearer you '
                                                    'are.'},
                              'single_positive': {'sub': 'away from the positive charge',
                                                  'note': 'Every arrow on the map points away from '
                                                          'the single positive charge, because '
                                                          'that is the way a small positive charge '
                                                          'would be shoved. At your point the '
                                                          'field is {strength} — {rel} on this '
                                                          'scale — and it is stronger the closer '
                                                          'you go. A small positive charge '
                                                          'released here would move {dir}; a small '
                                                          'negative one would go the other way, '
                                                          'back towards the charge.'},
                              'single_negative': {'sub': 'towards the negative charge',
                                                  'note': 'Every arrow points inwards, towards the '
                                                          'single negative charge — same map as '
                                                          'the positive charge, arrows reversed. '
                                                          'At your point the field is {strength}, '
                                                          '{rel} on this scale. A small positive '
                                                          'charge would be pulled in {dir}; a '
                                                          'small negative one would be driven '
                                                          'away. Nothing about the map depends on '
                                                          'anything being in it: the arrows were '
                                                          'there before you put the test point '
                                                          'down.'},
                              'dipole': {'sub': 'arrows leave the positive and land on the '
                                                'negative',
                                         'note': 'With a positive charge on the left and a '
                                                 'negative one on the right, every arrow in the '
                                                 'middle runs from the positive towards the '
                                                 'negative, and the field is strongest in the gap '
                                                 'between them where the two contributions point '
                                                 'the same way and add. At your point it is '
                                                 '{strength}, {rel} on this scale, and it points '
                                                 '{dir}. Slide out beyond either charge and that '
                                                 'rule stops holding: the nearer charge decides, '
                                                 'so left of the positive charge the field points '
                                                 'away from the positive, and right of the '
                                                 'negative charge it points towards the negative. '
                                                 'The arrows thin out fast out there — there is no '
                                                 'distance at which they stop, only distances '
                                                 'where they are too small to matter.'},
                              'two_positive': {'sub': 'away from the nearer charge',
                                               'note': 'Two equal positive charges, so the arrows '
                                                       'sweep outwards from both and avoid the '
                                                       'middle. At your point the field is '
                                                       '{strength}, {rel} on this scale, pointing '
                                                       '{dir} — away from whichever charge you are '
                                                       'nearer. Slide to the exact mid-point and '
                                                       'the two pushes cancel completely.'},
                              'null_point': {'sub': 'the two pushes are equal and opposite',
                                             'note': 'You are exactly half-way between two equal '
                                                     'positive charges, and here the field is '
                                                     'zero. Both charges push a small positive '
                                                     'test charge with the same strength, in '
                                                     'exactly opposite directions, so the two '
                                                     'arrows add to nothing and there is no arrow '
                                                     'to draw. Move one step either way and the '
                                                     'nearer charge wins immediately. A point like '
                                                     'this is not a place where the field is weak '
                                                     '— it is a place where it cancels.'}},
                 'words': {'no_value': 'no value here',
                           'on_charge_dir': 'no value — you are on top of a charge',
                           'zero_dir': 'the field cancels to nothing',
                           'right': 'to the right',
                           'left': 'to the left',
                           'no_force': 'feels no force',
                           'pushed': 'pushed {dir}',
                           'scale': '{rel} on this scale',
                           'zero_scale': 'zero',
                           'zero_word': 'nothing at all',
                           'close_word': 'too close to say'},
                 'id': 'field',
                 'kind': 'field-grid',
                 'demand': 'investigate'},
                {'eyebrow': 'The figure',
                 'heading': 'Three forces that reach across a gap',
                 'lead': 'The electric field is not a special case. Every force you meet at this '
                         'stage that acts without contact is described the same way: the first '
                         'object fills the space with a field, and the second one responds to the '
                         'field where it is.',
                 'triple': {'cards': [{'title': 'Gravitational field',
                                       'kind': 'gravity',
                                       'aria_label': 'Two circles separated by a dashed gap, with '
                                                     'an arrow from each pointing towards the '
                                                     'other.',
                                       'body': 'Anything with <strong>mass</strong> makes one. '
                                               'Always a pull, never a push, which is why there is '
                                               'no opposite of mass.'},
                                      {'title': 'Magnetic field',
                                       'kind': 'magnet',
                                       'aria_label': 'Two bars separated by a dashed gap, with an '
                                                     'arrow from each pointing towards the other.',
                                       'body': 'A <strong>magnet</strong> or a current makes one. '
                                               'Pull or push, depending on which poles face each '
                                               'other.'},
                                      {'title': 'Electric field',
                                       'kind': 'charge',
                                       'aria_label': 'Two circles separated by a dashed gap, one '
                                                     'marked with a plus and one with a minus, '
                                                     'with an arrow from each pointing towards the '
                                                     'other.',
                                       'body': 'A <strong>charge</strong> makes one. Pull or push, '
                                               'depending on the two signs — and it is enormously '
                                               'stronger than gravity.'}]},
                 'close': 'In all three the arrows come in pairs of equal size and opposite '
                          'direction, and in all three the gap can be a perfect vacuum. What '
                          'crosses it is not a substance. It is a field.',
                 'id': 'reach',
                 'kind': 'charge-band',
                 'demand': 'investigate'}],
 'figures': [{'id': 'p9-field-point-marked',
              'kind': 'diagram',
              'status': 'drawn',
              'art': 'p9-field-point',
              'title': 'One marked point on a field map, with an arrow pointing right',
              'desc': 'A dashed rectangle standing for part of a larger field map. A dot near its '
                      'centre marks one point, with a bold arrow leading right from it. Three '
                      'fainter arrows of the same length, also pointing right, sit at the corners '
                      'of the rectangle.',
              'caption': 'One point on a field map, marked.'}],
 'key_facts': [{'id': 'a-field-fills-the-space',
                'eyebrow': 'Key fact',
                'ground': 'card',
                'placement': 'top-level',
                'text': 'A charged object fills the space around it with an electric field: a size '
                        'and a direction at every point. The arrow shows which way a small '
                        'positive charge would be pushed there, so arrows point away from positive '
                        'and towards negative. The field is there whether or not anything is in '
                        'it, and it needs nothing in the gap.'}],
 'ladder': {'recall': {'q': 'The electric field around a small charged object points outwards, '
                            'away from it, in every direction. What can you say about the object, '
                            'and about a small negative charge released nearby?',
                       'options': ['The object is negatively charged, and a negative charge would '
                                   'be pushed outwards along the field.',
                                   'The object is positively charged, and a negative charge would '
                                   'be pushed outwards along the field.',
                                   'The object is positively charged, and a negative charge would '
                                   'be pulled inwards, against the field.',
                                   "You cannot tell the sign from the field's direction, only its "
                                   'strength.'],
                       'answer': 2,
                       'feedback': {0: 'The field points away from a positive charge, because it '
                                       'shows the push on a small positive charge. And a negative '
                                       'charge always goes against the field.',
                                    1: 'The first half is right. But the field shows the force on '
                                       'a positive charge; a negative one feels a force in the '
                                       'opposite direction, so it moves inwards.',
                                    3: 'The direction of the field is exactly what tells you the '
                                       'sign: outwards means positive, inwards means negative.'},
                       'title': 'Rung 1 · Read the field'},
            'apply': {'q': 'A student says the field between two equal positive charges must be at '
                           'its strongest half-way between them, because that point is close to '
                           'both. What is right?',
                      'options': ['The student is right — being close to two charges instead of '
                                  'one makes it the strongest point on the map.',
                                  'It is zero there. The two charges push a positive test charge '
                                  'in exactly opposite directions with equal strength, so the '
                                  'pushes cancel.',
                                  'It is zero there, because the two charges cancel each other out '
                                  'everywhere between them.',
                                  'It is half the strength of a single charge at the same '
                                  'distance, because the two contributions are averaged.'],
                      'answer': 1,
                      'feedback': {0: 'Closeness matters, but direction matters too. The two '
                                      'pushes are equal and exactly opposite at the mid-point, so '
                                      'they cancel to nothing.',
                                   2: 'The verdict is right and the reason is too broad. It '
                                      'cancels only at that one point; move a millimetre either '
                                      'way and the nearer charge wins.',
                                   3: 'Fields are not averaged, they are added as arrows — and two '
                                      'equal arrows pointing opposite ways add to nothing, not to '
                                      'half.'},
                      'title': 'Rung 2 · The one that catches people'},
            'explain': {'q': 'A plastic comb, charged by rubbing it on a jumper, is held a '
                             'centimetre above some small pieces of paper, and they jump up to it '
                             'with nothing touching them. Explain what is happening, using the '
                             'word field, and say what would change if the whole thing were done '
                             'in a vacuum.',
                        'field_label': 'Your explanation',
                        'placeholder': 'The comb is charged, so it fills the space around it with…',
                        'success': ['Says the comb is charged and fills the space around it with '
                                    'an electric field.',
                                    'Says the field has a direction and a strength at every point, '
                                    'and is stronger closer to the comb.',
                                    'Says the paper is neutral overall but the field shifts its '
                                    'charges slightly, so the side nearest the comb becomes '
                                    'oppositely charged.',
                                    'Says the force on the paper comes from the field where the '
                                    'paper is, not from anything crossing the gap.',
                                    'Says nothing would change in a vacuum, because the field does '
                                    'not need air or any material to exist in.'],
                        'title': 'Rung 3 · Explain'},
            'produce': {'q': 'People are told they are safe from lightning inside a car, and that '
                             'it is nothing to do with the rubber tyres. Explain why, using the '
                             'idea of a field and what you know about conductors.',
                        'field_label': 'Your answer',
                        'placeholder': 'The body of a car is metal, which is a conductor, so…',
                        'success': ['Says the body of the car is metal, which is a conductor with '
                                    'free electrons.',
                                    'Says the free charges rearrange themselves on the outside '
                                    'surface of the shell.',
                                    'Says the result is that the field inside the shell is very '
                                    'nearly zero.',
                                    'Says that with almost no field inside there is almost no '
                                    'force on the charges in a person inside.',
                                    'Says the tyres are irrelevant — the protection is the metal '
                                    'shell surrounding you, not an insulating layer underneath.'],
                        'title': 'Rung 4 · Take it somewhere new'}},
 'key_note': 'An electric field is what a charged object does to the space around it: at every '
             'point there is a size and a direction. Anything charged placed at a point feels a '
             'force from the field there, so nothing has to cross the gap and no air or contact is '
             'needed. Field arrows are drawn the way a small positive charge would be pushed, so '
             'they point away from positive charges and towards negative ones; a negative charge '
             'at the same point is pushed the opposite way. The field is strongest close to a '
             'charge and weakens quickly with distance, and between two like charges there is a '
             'point where it cancels to nothing. Gravity and magnetism are described in exactly '
             'the same way.',
 'stretch': [{'id': 'faraday-and-maxwell',
              'type': 'explainer',
              'text': 'Michael Faraday invented the idea, and he was not taken seriously at first. '
                      'He had almost no mathematics and described the space around a magnet as '
                      'filled with lines of force — a picture, not an equation. It took James '
                      'Clerk Maxwell to write that picture down properly, and when he did, the '
                      'equations predicted something nobody had asked for: that a field which '
                      'changes can travel through empty space at a fixed speed. That speed turned '
                      'out to be the speed of light, and light turned out to be exactly that. '
                      "Faraday's picture of empty space having a state is now the foundation of "
                      'every field theory in physics.'},
             {'id': 'safe-inside-a-shell',
              'type': 'explainer',
              'text': 'Fields also explain why you are safe inside a car in a thunderstorm, and it '
                      'is not the tyres. A metal shell is a conductor, so its free electrons '
                      'rearrange themselves until the field <em>inside</em> the shell is very '
                      'nearly zero, whatever is happening outside — the outside surface takes the '
                      'whole strike and the inside stays quiet. The same trick shields the cable '
                      'to a television aerial, protects the electronics inside an aircraft struck '
                      'by lightning, and is why a mobile phone loses signal in a lift.'}],
 'support': [],
 'vocabulary': [{'term': 'electric field',
                 'definition': 'The state a charged object puts the space around it into. It has a '
                               'size and a direction at every point, and it is there whether or '
                               'not anything is in it.'},
                {'term': 'field arrow',
                 'definition': 'A mark showing which way a small positive charge would be pushed '
                               'at that point, and how hard. A negative charge feels a force the '
                               'other way.'},
                {'term': 'null point',
                 'definition': 'A place where two contributions to a field cancel exactly. Not a '
                               'weak field — no field at all, at that one point.'}],
 'tutor': {'anchor': 's-field',
           'prompt': 'Ask Mr Badmus AI',
           'body': 'Got a charge arrangement and want to know which way the field points?',
           'cta': 'Ask about this lesson'},
 'ks4_becomes': 'Field lines for point charges and parallel plates, field strength as force per '
                'unit charge, and the link between field and potential difference.',
 'safety_note': 'It is the metal shell that protects you, so this only works in a car with a metal '
                'roof and metal sides. A convertible, a fibreglass boat or an open tractor cab '
                'will not do it, and you should not touch metal inside the car while the storm is '
                'overhead. If you are caught outside in a storm, get indoors or into a car — never '
                'shelter under a tree.',
 'convention_note': 'The bench is a teaching model. Charges are treated as points of equal size, '
                    'and the field is calculated with the standard inverse-square rule and '
                    'reported as a relative figure with 100 set at the strongest point the grid '
                    'samples — no field strength in newtons per coulomb is given, because the unit '
                    'is beyond this stage. Grid arrows have a shortest and a longest length, so '
                    'very weak and very strong regions are drawn clipped rather than to scale, and '
                    'points closer than a small distance to a charge are left blank because the '
                    'model gives no sensible value there. The test point moves along the centre '
                    'line only, where the field happens to be horizontal; away from that line it '
                    "is not. Real charged objects are not points, and a real charged sphere's "
                    'field differs from this near its surface.',
 'ws': ['measurement'],
 'authored': True}
