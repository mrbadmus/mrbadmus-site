# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 C1 `testing-the-model` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 60e475b703. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'C1'
SOURCE_SLUG = 'testing-the-model'
FROZEN_FROM = '60e475b703'

LESSON = {'slug': 'testing-the-model',
 'title': 'Testing the model: does it explain everything?',
 'discipline': 'chemistry',
 'unit': 'particles-and-their-behaviour',
 'family': 'INVESTIGATION',
 'covers': ['KS3.WS.ATT.02'],
 'touches': ['KS3.C.PNM.01a', 'KS3.C.PNM.02', 'KS3.C.PIS.03'],
 'beyond_statutory': False,
 'threads': [{'id': 'particles', 'level': 3}],
 'typical_year': 7,
 'typical_minutes': 45,
 'requires': ['diffusion'],
 'assumes': [],
 'references': [{'unit': 'P11',
                 'lesson': 'why-ice-floats',
                 'why': 'Nearly everything shrinks when it freezes. Water does the opposite, which '
                        'is why ice floats instead of sinking — and it is the hardest thing this '
                        'model has to explain.'},
                {'unit': 'C2', 'lesson': 'the-atom-daltons-model'}],
 'connects_heading': 'Next unit',
 'ks4_links': [],
 'big_question': 'You have spent five lessons being shown how well the particle model works. Here '
                 'are seven things it has to account for. Three of them it cannot. What should be '
                 'done about that?',
 'rail': [{'anchor': 's-hook', 'short': 'HOOK', 'label': 'Ice floats', 'done_when': 'committed'},
          {'anchor': 's-bench',
           'short': 'EVIDENCE',
           'label': 'Evidence bench',
           'done_when': 'all_seven_judged'},
          {'anchor': 's-verdict',
           'short': 'VERDICT',
           'label': 'The verdict',
           'done_when': 'committed'},
          {'anchor': 's-history',
           'short': 'HISTORY',
           'label': 'Five models',
           'done_when': 'visited_beyond_default'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Ice floats. What about wax?',
                'prompt': 'Ice floats on water. Now some candle wax is melted in a pan, and a lump '
                          'of solid wax is dropped into it.',
                'commit': 'If you had to guess, will the lump float on the melted wax, or sink in '
                          'it?',
                'options': ['It floats', 'It sinks'],
                'reveal': 'So why does ice float? Next: seven observations, ice among them, and '
                          'whether the particle model can explain each one.',
                'guess': True,
                'replies': ['That is what ice does on water. But ice is the odd one out. For '
                            'almost everything else, wax included, the solid sinks.',
                            'Almost every solid sinks in its own liquid. Its particles are packed '
                            'more tightly, so a lump of it is heavier than the same amount of '
                            'liquid.'],
                'answer': 1},
 'misconceptions': [{'id': 'NOS-01',
                     'statement': 'A scientific model is either true or false, and one exception '
                                  'proves it wrong.',
                     'elicited_by': 'the-verdict',
                     'confronted_by': 'the-verdict'},
                    {'id': 'NOS-02',
                     'statement': "Scientists' models never change once they are agreed.",
                     'elicited_by': 'settled-science',
                     'confronted_by': 'settled-science'}],
 'vocabulary': [{'term': 'evidence',
                 'definition': 'Observations or measurements used to decide whether an idea works.',
                 'note': None},
                {'term': 'prediction',
                 'definition': 'What a model says should happen, worked out before anyone checks.',
                 'note': 'A wrong prediction is not a disgrace. It is the most useful thing a '
                         'model can produce, because it tells you where to look next.'},
                {'term': 'limit',
                 'definition': 'The point where a model stops giving the right answer.',
                 'note': 'Every model has limits. Knowing where they are is part of understanding '
                         'it, not a reason to throw it away.'}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'explainer',
           'text': 'Every lesson so far has handed you evidence that fits. That is not how the '
                   'model was tested and it is not how you should judge it. A model is only worth '
                   'anything if you know where its edges are — so this lesson goes looking for '
                   'them deliberately.'},
          {'type': 'check', 'id': 'seven-observations', 'anchor': 's-bench'},
          {'type': 'practical', 'id': 'the-verdict', 'anchor': 's-verdict'},
          {'type': 'key-fact', 'ref': 'judged-by-what-it-explains'},
          {'type': 'check', 'id': 'five-models', 'anchor': 's-history'},
          {'type': 'misconception',
           'id': 'settled-science',
           'anchor': 's-think',
           'targets': 'NOS-02'},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note'}],
 'key_facts': [{'id': 'judged-by-what-it-explains',
                'text': 'A scientific model is judged by what it explains and where it fails — not '
                        "by being completely true. Knowing a model's limits is part of "
                        'understanding it.',
                'placement': 'top-level',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'settled-science',
                 'kind': 'predict',
                 'demand': 'explain',
                 'targets': 'NOS-02',
                 'statements': ['Once scientists agree on something, it is settled — that is what '
                                'makes it science.'],
                 'prompt': 'Commit before you read on.',
                 'options': ['True — agreement is what makes something scientific',
                             'Being open to revision by evidence is what makes it scientific',
                             'Nothing in science can be trusted, then',
                             'Only old science gets overturned; modern science is settled'],
                 'reveal': ['The opposite is nearer the truth. What makes an idea scientific is '
                            'that it is the kind of thing evidence could overturn — and the '
                            'timeline above is five overturnings in a row, each by people who were '
                            'not being careless. Dalton was not sloppy; he was working with the '
                            'evidence he had.',
                            'This does not mean nothing is reliable. The particle model has '
                            'survived two centuries of people trying to break it, and the parts '
                            'that survived are about as solid as human knowledge gets. "Open to '
                            'revision" and "as good as we have got" are not opposites — they are '
                            'the same sentence, said twice.']},
                {'demand': 'evaluate',
                 'eyebrow': 'The evidence bench · judge each one',
                 'heading': 'Seven observations. Does the model handle it?',
                 'head_counter': {'format': '{n} of {total} judged', 'total': 7},
                 'progress_all': 'all seven judged',
                 'prompt': 'Decide before you open the verdict. You are not being marked on the '
                           'sorting — you are being asked to commit, so that a surprise can land.',
                 'buttons': {'yes': 'Explains it', 'no': 'Cannot'},
                 'verdict_labels': {'ok': 'The model handles this',
                                    'fail': 'The model cannot do this'},
                 'cases': [{'id': 'k1',
                            'tag': 'Observation 1',
                            'text': 'A gas can be squashed into a fraction of its volume; a liquid '
                                    'hardly squashes at all.',
                            'ok': True,
                            'verdict': 'Handled completely. A gas is mostly empty space and a '
                                       'liquid is not. Nothing else needs to be added to the model '
                                       'to get this right.'},
                           {'id': 'k2',
                            'tag': 'Observation 2',
                            'text': 'A smell spreads through a room. Draughts and convection carry '
                                    'it most of the way; diffusion covers the last stretch.',
                            'ok': True,
                            'verdict': 'Handled completely. Random movement plus collisions gives '
                                       'the spreading — and explains why diffusion on its own '
                                       'would be far too slow to do the whole job.'},
                           {'id': 'k3',
                            'tag': 'Observation 3',
                            'text': 'Ice floats on water. Almost every other solid sinks in its '
                                    'own liquid.',
                            'ok': False,
                            'verdict': 'Fails. The model predicts that a solid — packed and '
                                       'ordered — must be denser than the same substance jumbled '
                                       'and looser. For water it is the other way round. Identical '
                                       'spheres cannot produce this; you need particles with a '
                                       'shape, that hold each other at arm’s length in a fixed '
                                       'pattern.'},
                           {'id': 'k4',
                            'tag': 'Observation 4',
                            'text': 'Seal a melting ice cube in a bag and the mass does not change '
                                    'by a milligram.',
                            'ok': True,
                            'verdict': 'Handled completely. Particles are neither made nor '
                                       'destroyed by a change of state — they are only '
                                       'rearranged.'},
                           {'id': 'k5',
                            'tag': 'Observation 5',
                            'text': 'Diamond and graphite are both nothing but carbon. Diamond is '
                                    'the hardest natural substance known; graphite is soft enough '
                                    'to write with.',
                            'ok': False,
                            'verdict': 'Fails, and badly. In this model the particles are '
                                       'identical, so the same substance can only have one set of '
                                       'properties. To explain this you need the particles to be '
                                       'joined together in different arrangements — which means '
                                       'particles that can bond, and the model has no bonds in '
                                       'it.'},
                           {'id': 'k6',
                            'tag': 'Observation 6',
                            'text': 'A rubber band stretches to five times its length and snaps '
                                    'back. A glass rod of the same thickness shatters.',
                            'ok': False,
                            'verdict': 'Fails. Loose spheres sliding past each other cannot '
                                       'stretch and recoil. Rubber needs particles joined into '
                                       'long tangled chains that straighten out and spring back — '
                                       'a structure this model cannot represent at all.'},
                           {'id': 'k7',
                            'tag': 'Observation 7',
                            'text': 'A sealed helium balloon is noticeably smaller after three '
                                    'days, even though it has no hole.',
                            'ok': True,
                            'verdict': 'Handled completely — and it is a good test, because the '
                                       'answer is not obvious. The rubber is itself made of '
                                       'particles with gaps between them, and helium particles are '
                                       'small enough to work their way through.'}],
                 'tally': 'Four explained, three not — and you called {n} of the seven before '
                          'opening the verdict.',
                 'shared_cause': 'The three failures have one thing in common, and it is worth '
                                 'naming: every one of them needs the particles to be '
                                 '<em>different from each other</em>, or to be joined together in '
                                 'some particular way. The model you have is a model of identical '
                                 'featureless spheres. That is exactly the assumption that is '
                                 'about to be replaced.',
                 'id': 'seven-observations',
                 'kind': 'evidence-bench'},
                {'demand': 'evaluate',
                 'targets': 'NOS-01',
                 'eyebrow': 'The verdict · this is the real question',
                 'heading': 'Three failures. What should be done?',
                 'prompt': 'Commit to one. Then read what scientists actually did, which is on the '
                           'record and is not a matter of opinion.',
                 'options': [{'text': 'Throw the model away — it makes wrong predictions',
                              'reply': 'That is the strictest possible standard, and no model in '
                                       'science survives it. Applied consistently it would leave '
                                       'you with nothing to think with.'},
                             {'text': 'Keep using it where it works, and record exactly where it '
                                      'fails',
                              'reply': 'This is what was actually done, and it is the answer.'},
                             {'text': 'The exceptions are rare, so they can safely be ignored',
                              'reply': 'Ice floating is not a curiosity — it is why lakes do not '
                                       'freeze solid and why life survives winter. And the '
                                       'exceptions are where the next model came from, so ignoring '
                                       'them costs you the discovery.'},
                             {'text': 'Change the name to a theory, which is allowed to have '
                                      'exceptions',
                              'reply': 'A word change fixes nothing. A theory that predicts ice '
                                       'will sink has exactly the same problem as a model that '
                                       'does.'}],
                 'answer_index': 1,
                 'closing': ['Nobody threw it away. The particle model is still used every day, by '
                             'everyone, including the people who know exactly where it breaks — '
                             'because for melting, pressure, diffusion and dissolving it gives the '
                             'right answer with almost no effort. What happened instead is that '
                             'the failures were treated as a map: each one marked a place where a '
                             'better model was needed, and each one eventually got built. Ice '
                             'floating was explained once particles could be shaped and could pull '
                             'on each other in particular directions. Diamond and graphite were '
                             'explained once particles could be joined in patterns. Rubber was '
                             'explained once particles could be long chains.',
                             'A wrong prediction is not a disgrace. It is the most useful thing a '
                             'model can produce, because it tells you where to look next.'],
                 'id': 'the-verdict',
                 'kind': 'keyed-commit'},
                {'demand': 'explain',
                 'eyebrow': 'Not a straight line',
                 'heading': 'The model has already been replaced four times',
                 'prompt': 'Each one of these was, in its day, what "everyone knew". Each was '
                           'overturned by evidence, and each left something behind that is still '
                           'in use.',
                 'steps': [{'year': 'c. 400 BC',
                            'who': 'Democritus',
                            'label': 'The uncuttable',
                            'claim': 'Matter cannot be divided forever — there must be a smallest '
                                     'piece.',
                            'body': 'Reached by pure argument, with no experiment behind it and no '
                                    'way to test it. For two thousand years it sat alongside the '
                                    'rival view that matter is continuous, and there was nothing '
                                    'to choose between them.',
                            'broke': 'Nothing broke it — which was the problem. An idea that '
                                     'cannot be tested cannot win, and it did not, for twenty '
                                     'centuries.'},
                           {'year': '1803',
                            'who': 'Dalton',
                            'label': 'Solid spheres',
                            'claim': 'Every element is made of identical solid atoms that cannot '
                                     'be split, created or destroyed.',
                            'body': 'The first version with numbers attached: fixed proportions by '
                                    'mass, whole-number ratios, mass conserved through reactions. '
                                    'This is the model you have been using all unit.',
                            'broke': 'Thomson found electrons — pieces knocked off an atom that '
                                     'was supposed to have no pieces. And atoms of one element '
                                     'turned out to have different masses.'},
                           {'year': '1897',
                            'who': 'Thomson',
                            'label': 'Plum pudding',
                            'claim': 'An atom is a ball of positive charge with tiny negative '
                                     'electrons dotted through it.',
                            'body': 'Kept everything Dalton got right about reactions, and added '
                                    'the one thing he could not have known: atoms have parts, and '
                                    'one of those parts carries charge.',
                            'broke': 'Rutherford fired alpha particles at gold foil and a few '
                                     'bounced straight back — impossible if the positive charge '
                                     'were spread thinly through the whole atom.'},
                           {'year': '1911',
                            'who': 'Rutherford',
                            'label': 'The nucleus',
                            'claim': 'Almost all the mass sits in a tiny dense nucleus, with '
                                     'electrons somewhere around it and empty space in between.',
                            'body': 'An atom turns out to be overwhelmingly empty. If the nucleus '
                                    'were a marble on the centre spot of a football pitch, the '
                                    'nearest electron would be somewhere in the stands.',
                            'broke': 'The maths said the orbiting electrons should spiral into the '
                                     'nucleus within a fraction of a second. Every atom in '
                                     'existence should have collapsed already.'},
                           {'year': '1913 → now',
                            'who': 'Bohr and after',
                            'label': 'Shells, then clouds',
                            'claim': 'Electrons are restricted to particular energy levels, and '
                                     'are better described as clouds of probability than as balls.',
                            'body': 'This is the model behind the periodic table, chemical bonding '
                                    'and every reaction you will meet at GCSE and beyond.',
                            'broke': 'Nothing yet, for chemistry. It has limits of its own at very '
                                     'high energies, and the search for what lies past them is a '
                                     'live field of research right now.'}],
                 'default_index': 1,
                 'broke_label': 'What broke it:',
                 'id': 'five-models',
                 'kind': 'model-timeline'}],
 'ladder': {'recall': {'q': 'Name one thing the simple particle model cannot explain.',
                       'options': ['Why a gas can be squashed',
                                   'Why a smell spreads across a room',
                                   'Why ice floats on water',
                                   'Why mass stays the same when ice melts'],
                       'answer': 2,
                       'feedback': {0: 'It explains this well — a gas is mostly empty space.',
                                    1: 'It explains this well — random movement and collisions.',
                                    3: 'It explains this well — particles are rearranged, not '
                                       'destroyed.'}},
            'apply': {'q': 'The particle model makes a wrong prediction about ice. What is the '
                           'right response?',
                      'options': ['Throw it out — a model that gets something wrong is worthless',
                                  'Keep using it where it works, and note the limit',
                                  'Ignore the exception, since it is only water',
                                  'Call it a theory instead of a model, which allows exceptions'],
                      'answer': 1,
                      'feedback': {0: 'Then chemistry would have no models at all. Every one of '
                                      'them has limits, including the current ones.',
                                   2: 'Ignoring the failure is how you miss the discovery. The '
                                      'exceptions are where the next model comes from.',
                                   3: 'Renaming it changes nothing. A theory that makes a wrong '
                                      'prediction has exactly the same problem.'}},
            'explain': {'q': 'The particle model cannot explain why diamond and graphite — both '
                             'pure carbon — have completely different properties. Explain why not, '
                             'and say what would have to be added to the model to fix it.',
                        'field_label': 'Your explanation',
                        'placeholder': 'In this model, all the particles of one substance are…',
                        'success': ['Says the model treats all particles of a substance as '
                                    'identical featureless spheres.',
                                    'Says identical particles should give identical properties, so '
                                    'one substance could only ever behave one way.',
                                    'States the observation clearly: same element, two very '
                                    'different materials.',
                                    'Says the model would need particles that can be joined '
                                    'together in different arrangements.',
                                    'Says this is a limit of the model, not a mistake in the '
                                    'observation.']},
            'produce': {'q': 'A student reads the timeline and concludes: "Scientists keep being '
                             'wrong, so there is no point trusting what they say now." Reply to '
                             'them, using at least one specific example from this lesson.',
                        'field_label': 'Your reply',
                        'placeholder': 'Each new model had to explain…',
                        'success': ['Says each new model had to reproduce everything the old one '
                                    'already explained.',
                                    'Gives a specific example — Dalton’s explanation of '
                                    'conservation of mass is still used, or Newton is still used '
                                    'to land spacecraft.',
                                    'Says being open to revision by evidence is what makes an idea '
                                    'scientific, not a weakness in it.',
                                    'Distinguishes between an idea being replaced and an idea '
                                    'being useless.',
                                    'Says the current model is the best-tested account available, '
                                    'not a guess.']}},
 'key_note': 'The particle model explains melting, pressure, diffusion and dissolving, and fails '
             'on ice floating, diamond versus graphite, and stretchy materials. All three failures '
             'come from the same assumption — that particles are identical featureless spheres. '
             'That is the assumption the next unit removes.',
 'stretch': [{'type': 'explainer',
              'id': 'over-correction',
              'text': 'There is a version of this that goes too far. "Scientists are always '
                      'changing their minds, so you cannot trust any of it" is a conclusion people '
                      'reach from exactly the evidence on this page, and it does not follow. Look '
                      'at what actually survived each revision: Dalton was wrong that atoms cannot '
                      'be split, and every single thing he used that claim to explain is still '
                      'explained the same way today. Newton was superseded by Einstein, and NASA '
                      'still uses Newton to land spacecraft. Replacement in science is almost '
                      'never demolition — it is a new model that has to reproduce everything the '
                      'old one got right, plus the thing that broke it. That constraint is why the '
                      'changes accumulate instead of cancelling out.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Unsure how a model can be wrong and still be right to use?',
           'cta': 'Ask about this lesson',
           'anchor': 's-verdict'},
 'ks4_becomes': 'Bonding and structure — where every failure on this page gets its proper '
                'explanation.',
 'ws': ['scientific-attitudes',
        'analysis-and-evaluation',
        'experimental-skills-and-investigations'],
 'review_state': 'draft',
 'authored': True}
