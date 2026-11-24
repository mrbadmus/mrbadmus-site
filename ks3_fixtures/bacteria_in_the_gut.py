# -*- coding: utf-8 -*-
"""Frozen classic snapshot of KS3 B3 `bacteria-in-the-gut` (ks3_fixtures/__init__.py).

Written by tools/freeze_ks3_fixtures.py from 61b38f0377. Do not edit, and do not refreeze to
make a check pass: the checks that read this page assert what it held on that commit.
"""

UNIT = 'B3'
SOURCE_SLUG = 'bacteria-in-the-gut'
FROZEN_FROM = '61b38f0377'

LESSON = {'slug': 'bacteria-in-the-gut',
 'title': 'Bacteria in the gut',
 'discipline': 'biology',
 'unit': 'nutrition-and-digestion',
 'family': 'SYSTEM',
 'covers': ['KS3.B.NUT.05'],
 'touches': [],
 'beyond_statutory': False,
 'threads': [{'id': 'cells-and-systems', 'level': 3}, {'id': 'structure-function', 'level': 1}],
 'typical_year': 7,
 'typical_minutes': 45,
 'requires': ['absorption-and-the-small-intestine'],
 'assumes': [],
 'references': [{'unit': 'B1', 'lesson': 'unicellular-organisms'}, 'a-balanced-diet'],
 'ks4_links': [],
 'ks4_becomes': 'Communicable disease, antibiotic resistance, and the role of the microbiome in '
                'health.',
 'big_question': 'Your gut is home to trillions of bacteria. What are they doing there?',
 'rail': [{'anchor': 's-hook',
           'short': 'HOOK',
           'label': 'Germ-free mouse',
           'done_when': 'committed'},
          {'anchor': 's-jobs',
           'short': 'JOBS',
           'label': 'Five jobs',
           'done_when': 'all_five_jobs_off'},
          {'anchor': 's-deal',
           'short': 'DEAL',
           'label': 'Both sides',
           'mirrors': 's-hook',
           'done_when': 'committed'},
          {'anchor': 's-ladder',
           'short': 'LADDER',
           'label': 'Mastery ladder',
           'done_when': 'ladder_complete'}],
 'phenomenon': {'kind': 'narrative',
                'title': 'Raise a mouse in a sterile bubble with no bacteria at all.',
                'prompt': 'Sterile food, sterile air, sterile water, no bacteria anywhere in or on '
                          'it, ever. The mouse lives its whole life in a sealed, germ-free bubble.',
                'commit': 'If you had to guess, does a mouse with no bacteria need more food than '
                          'a normal mouse, or less?',
                'options': ['More food', 'Less food'],
                'reveal': 'Food is only one of the jobs the bacteria were doing. Next: switch off '
                          'their five jobs one at a time and see what breaks.',
                'guess': True,
                'replies': ['About 30% more. Gut bacteria release energy from parts of the food '
                            'the mouse cannot digest itself, so without them that energy is lost.',
                            'That makes sense if bacteria just share your food. But this mouse '
                            'needs about 30% more, because gut bacteria release energy from fibre '
                            'it cannot digest itself.'],
                'answer': 0},
 'misconceptions': [{'id': 'DIET-17',
                     'statement': 'Bacteria are germs. Having bacteria inside you means you are '
                                  'ill.',
                     'elicited_by': 'hook',
                     'confronted_by': 'germs-and-simplicity'},
                    {'id': 'CELL-08',
                     'statement': 'A single-celled organism is just a simpler version of one of '
                                  'our cells — the same parts, doing less.',
                     'elicited_by': 'job-switch',
                     'confronted_by': 'germs-and-simplicity'}],
 'vocabulary': [{'term': 'cellulose',
                 'definition': 'The tough material plant cell walls are built from. Human enzymes '
                               'cannot break it down.',
                 'note': None},
                {'term': 'ferment',
                 'definition': 'To break a substance down without using oxygen. Gut bacteria '
                               'ferment the fibre you cannot digest.',
                 'note': None},
                {'term': 'microbiome',
                 'definition': 'The whole community of microorganisms living in one place — for '
                               'example, in your large intestine.',
                 'note': None},
                {'term': 'antibiotic',
                 'definition': 'A medicine that kills bacteria or stops them multiplying.',
                 'note': 'It cannot tell a useful species from a harmful one, which is why '
                         'clearing an infection can clear the competition too.'}],
 'figures': [],
 'core': [{'type': 'hook', 'ref': 'phenomenon', 'anchor': 's-hook'},
          {'type': 'practical', 'id': 'job-switch', 'anchor': 's-jobs'},
          {'type': 'rule',
           'anchor': 's-deal',
           'eyebrow': 'Both sides of the deal',
           'statement': 'What each side gets, and what happens when the balance shifts.',
           'cards': [{'term': 'What you get · Chemistry you do not have',
                      'gloss': 'Energy from fibre, vitamin K and B vitamins, a defended gut, a '
                               'trained immune system and a maintained wall. Five jobs, none of '
                               'which your own twenty thousand genes can do.'},
                     {'term': 'What they get · A warm, fed, stable habitat',
                      'gloss': 'Constant 37 °C, a steady supply of food arriving from above, no '
                               'competition from outside, and no immune attack. From the '
                               'bacteria’s point of view your large intestine is excellent '
                               'property.'},
                     {'term': 'When it shifts · The same species, the wrong place',
                      'gloss': 'A useful community in the large intestine becomes a serious '
                               'problem if it crosses into the blood, or if antibiotics clear the '
                               'space and one harmful species takes over. What makes a bacterium '
                               'dangerous is usually location and abundance, not identity.'}]},
          {'type': 'key-fact', 'ref': 'helpful-or-harmful-is-where'},
          {'type': 'misconception',
           'id': 'germs-and-simplicity',
           'anchor': 's-think',
           'targets': ['DIET-17', 'CELL-08']},
          {'type': 'quiz', 'ref': 'ladder', 'anchor': 's-ladder'},
          {'type': 'summary', 'ref': 'key_note', 'anchor': 's-keynote'}],
 'key_facts': [{'id': 'helpful-or-harmful-is-where',
                'text': 'Most bacteria in your gut are helpful and a few can be harmful. Which '
                        'they are depends on the species and on where they are — the same '
                        'bacterium can be useful in the large intestine and dangerous in the '
                        'blood.',
                'ground': 'card',
                'eyebrow': 'Key fact'}],
 'activities': [{'id': 'germs-and-simplicity',
                 'kind': 'confrontation',
                 'demand': 'confront the germ error and the one-cell-means-simple error in one '
                           'pass',
                 'targets': ['DIET-17', 'CELL-08'],
                 'statements': [{'quote': 'Bacteria are germs. Having bacteria inside you means '
                                          'you are ill.',
                                 'answer': 'Of the many thousands of bacterial species that live '
                                           'on and in humans, the number that reliably cause '
                                           'disease is a small minority. The rest are neutral or '
                                           'useful, and the useful ones are doing work you cannot '
                                           'do without: about a tenth of the energy some people '
                                           'get from their food comes from bacteria fermenting '
                                           'fibre, and a large part of your vitamin K is made by '
                                           'bacteria in your own large intestine. The word germ is '
                                           'not a biological category at all — it is a word for '
                                           '“microorganism I do not want here”, and the here '
                                           'matters more than the what. <em>E. coli</em> lives '
                                           'harmlessly in almost every human large intestine; the '
                                           'same species in your bladder is a urinary infection '
                                           'and in your blood it can kill you. Nothing about the '
                                           'bacterium changed.'},
                                {'quote': 'One cell means simple, so gut bacteria cannot be doing '
                                          'anything complicated.',
                                 'answer': 'You met this in Unicellular organisms and it comes '
                                           'back with a bigger consequence. Your gut bacteria '
                                           'collectively carry several million genes; you carry '
                                           'about twenty thousand. They can build enzymes for '
                                           'reactions no human cell can perform, which is exactly '
                                           'why they can digest cellulose and make vitamins and '
                                           'you cannot. It is not that they are helping with your '
                                           'chemistry. They are running chemistry you do not '
                                           'have.'}]},
                {'demand': 'investigate',
                 'targets': 'CELL-08',
                 'eyebrow': 'Switch them off · five jobs',
                 'heading': 'Take one job away and see what breaks',
                 'head_counter': {'format': '{n} of 5 switched off', 'total': 5, 'start': 0},
                 'prompt': 'Every one of these is something your gut bacteria do that your own '
                           'cells cannot.',
                 'jobs': [{'id': 'fibre',
                           'tag': 'Job 1',
                           'name': 'Fermenting fibre',
                           'what': 'Your own enzymes cannot break cellulose. Gut bacteria can, and '
                                   'the fatty acids they release are absorbed through the large '
                                   'intestine wall and used by your cells.',
                           'without': 'A share of the energy in your food — up to about a tenth '
                                      'for some people — simply leaves the body undigested. The '
                                      'germ-free mouse needs 30% more food for the same growth, '
                                      'and this is most of the reason.'},
                          {'id': 'vitamins',
                           'tag': 'Job 2',
                           'name': 'Making vitamins',
                           'what': 'Bacteria in the large intestine make vitamin K and several B '
                                   'vitamins as by-products of their own metabolism, and you '
                                   'absorb them.',
                           'without': 'Vitamin K deficiency, and blood that clots poorly. Newborn '
                                      'babies have almost no gut bacteria yet, which is exactly '
                                      'why they are given a vitamin K injection at birth.'},
                          {'id': 'space',
                           'tag': 'Job 3',
                           'name': 'Occupying the space',
                           'what': 'Harmful species need somewhere to settle and something to eat. '
                                   'A gut already full of established bacteria offers neither.',
                           'without': 'Empty space and free food. This is why a course of '
                                      'antibiotics can be followed by an infection that the '
                                      'antibiotic was not treating — the competition was cleared '
                                      'away.'},
                          {'id': 'immune',
                           'tag': 'Job 4',
                           'name': 'Training the immune system',
                           'what': 'A developing immune system learns what to attack and what to '
                                   'leave alone by encountering harmless bacteria early. The gut '
                                   'community is most of that encounter.',
                           'without': 'An immune system that has never been calibrated — slower '
                                      'against real threats, and more likely to react to things '
                                      'that are not threats at all.'},
                          {'id': 'wall',
                           'tag': 'Job 5',
                           'name': 'Maintaining the gut wall',
                           'what': 'The fatty acids bacteria release are the preferred fuel of the '
                                   'cells lining the large intestine, and they signal those cells '
                                   'to keep the wall thick and the mucus layer intact.',
                           'without': 'A thin, poorly developed wall — measurable in the germ-free '
                                      'mouse, and a route for bacteria to cross where they should '
                                      'not.'}],
                 'labels': {'on': 'Switch it off', 'off': 'Switched off', 'without': 'Without it:'},
                 'all_off': {'tag': 'All five off',
                             'headline': 'You have just built the germ-free mouse.',
                             'body': 'It lives. It is simply worse at everything — more food for '
                                     'the same growth, a weaker gut wall, missing vitamins, and no '
                                     'defence in place when a harmful species arrives. The '
                                     'bacteria were not tolerated. They were part of the system.'},
                 'id': 'job-switch',
                 'kind': 'job-switch'}],
 'ladder': {'recall': {'title': 'Rung 1 · What they do for you',
                       'q': 'Which of these can your gut bacteria do that your own cells cannot?',
                       'options': ['Absorb glucose and pass it into the blood',
                                   'Produce the hydrochloric acid that kills arriving bacteria',
                                   'Digest protein into the amino acids you absorb',
                                   'Break down fibre and make vitamin K'],
                       'answer': 3,
                       'feedback': {0: 'Your own villus cells absorb glucose. Bacteria are not '
                                       'needed for that.',
                                    1: 'Your stomach lining makes the acid. The acid kills most '
                                       'bacteria that arrive.',
                                    2: 'Your own protease enzymes digest protein. Bacteria are not '
                                       'needed for that.'}},
            'apply': {'title': 'Rung 2 · The one that catches people',
                      'q': 'A patient takes an antibiotic for a chest infection. Two weeks later, '
                           'a gut bacterium called C. difficile causes severe diarrhoea. Why did '
                           'killing bacteria make this infection more likely?',
                      'options': ['The antibiotic made C. difficile much stronger, so it was much '
                                  'harder to kill',
                                  'The antibiotic killed competing bacteria, so C. difficile had '
                                  'space and food',
                                  'The antibiotic irritated the gut, so it caused diarrhoea with '
                                  'no bacterium',
                                  'The chest infection spread down into the gut, so its bacteria '
                                  'multiplied there'],
                      'answer': 1,
                      'feedback': {0: 'The antibiotic did not change C. difficile. It removed its '
                                      'competitors.',
                                   2: 'This diarrhoea was caused by C. difficile, a bacterium that '
                                      'grew in the gut.',
                                   3: 'Chest bacteria did not cause it. C. difficile grew because '
                                      'its competitors were gone.'}},
            'explain': {'title': 'Rung 3 · Explain the germ-free mouse',
                        'q': 'Explain why a germ-free mouse needs about 30% more food than a '
                             'normal mouse, and why it is also more vulnerable to infection. Use '
                             'at least three of the five jobs.',
                        'field_label': 'Your explanation',
                        'placeholder': 'It needs more food because… and it is more vulnerable '
                                       'because…',
                        'success': ['Says fibre is not fermented, so the energy in it is lost '
                                    'rather than absorbed.',
                                    'Says vitamins normally made by bacteria are absent and must '
                                    'come from food or be missing.',
                                    'Says nothing is occupying the gut, so an arriving harmful '
                                    'species meets no competition.',
                                    'Says the immune system has not been trained by harmless '
                                    'bacteria, so it responds less well.',
                                    'Ends on the general point: the bacteria were doing jobs, not '
                                    'being tolerated.']},
            'produce': {'title': 'Rung 4 · Take it somewhere new',
                        'q': 'Cows digest grass; humans cannot. Cows have no cellulase enzyme of '
                             'their own either. Using this lesson, explain how a cow manages it, '
                             'and say what this suggests about the size of a cow’s gut compared '
                             'with ours.',
                        'field_label': 'Your answer',
                        'placeholder': 'A cow can digest grass because…',
                        'success': ['Says the cow relies on bacteria — and other microorganisms — '
                                    'to break down cellulose, not on its own enzymes.',
                                    'Says the products of that fermentation are then absorbed by '
                                    'the cow.',
                                    'Reasons that fermentation is slow, so the gut must hold food '
                                    'for a long time.',
                                    'Concludes the cow needs a much larger fermentation chamber '
                                    'than a human has — hence the multi-chambered stomach.']}},
 'key_note': 'The large intestine holds trillions of bacteria. They ferment fibre your own enzymes '
             'cannot digest, make vitamin K and some B vitamins, occupy space that harmful species '
             'would otherwise take, and help the immune system develop. A few species can cause '
             'disease, and antibiotics disturb the whole community rather than only the target.',
 'stretch': [{'type': 'explainer',
              'id': 'faecal-microbiota-transplant',
              'text': 'One of the more startling treatments in modern medicine is a faecal '
                      "microbiota transplant: bacteria from a healthy donor's gut, screened and "
                      'prepared, introduced into a patient whose own gut community has been '
                      'destroyed — usually by antibiotics, allowing <em>Clostridioides '
                      'difficile</em> to take over the empty space and cause a severe, stubborn '
                      'infection. Antibiotics alone often fail, because they clear the space again '
                      'for the same organism to reoccupy. Restoring a full community of '
                      'competitors works in around nine cases out of ten. It is a treatment that '
                      'only makes sense once you stop thinking of bacteria as contamination and '
                      'start thinking of a gut community as an ecosystem with vacancies.'}],
 'support': [],
 'tutor': {'prompt': 'Ask Mr Badmus AI',
           'body': 'Want to talk through why the same bacterium can be helpful or harmful?',
           'cta': 'Ask about this lesson',
           'anchor': 's-deal'},
 'convention_note': 'Figures for bacterial numbers and gene counts are order-of-magnitude '
                    'estimates from current research and are revised regularly. Nothing here is '
                    'advice about antibiotics or probiotics — those decisions belong with a '
                    'doctor.',
 'ws': ['analysis-and-evaluation', 'scientific-attitudes'],
 'review_state': 'draft',
 'authored': True}
