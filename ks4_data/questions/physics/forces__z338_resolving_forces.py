"""Physics · Forces — the MRB-338 expansion for `resolving-forces`.

Higher tier and triple only. The leaf turns on one idea used in two directions:
a single force is equivalent to two perpendicular components, and two
perpendicular forces are equivalent to a single resultant found by Pythagoras.

The frozen twelve already own: component size against the original, a 20 N
force at 60°, a 12/5 pair recombined, the definition of resolving, a sledge
rope at 30°, a 45 N force at 45°, a vertical component of 12 N at 30°, an
8.0/15.0 bolt problem, a crate pushed at 25° below the horizontal, a wrong
24/12 pair on a 26 N force, a lamp on two ceiling wires, and a 150 N box on a
20° slope. None of those is repeated here.

The new rows take the ground they leave: the SCALE-DRAWING method itself (what
an arrow length means, tip-to-tail, reading a resultant off a diagram, when
drawing beats calculating), Pythagorean resultants using clean triples so the
arithmetic is checkable without tables (3-4-5, 6-8-10, 5-12-13, 7-24-25,
20-21-29, 9-12-15), slopes specified by rise-along-the-slope rather than by an
angle, the perpendicular-to-slope component, and the limiting cases where one
component is the whole force or zero. Every figure below was checked against
the values stated in its own stem.
"""

TOPIC = "forces"
SUBJECT = "physics"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-resolving-forces-e05',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A drawing pin is pulled by two threads at right angles to each '
                'other, one with 6.0 N and one with 8.0 N. Work out the single '
                'force that would have the same effect.',
        "options": [
            '14.0 N',
            '2.0 N',
            '10.0 N',
            '48.0 N',
        ],
        "correct_index": 2,
        "why": 'The two are perpendicular, so the resultant is the hypotenuse: '
               '6.0² + 8.0² = 100, and the square root of 100 is 10.0 N. Simply '
               'adding them gives 14.0 N and ignores the right angle.',
    },
    {
        "id": 'ks4-resolving-forces-e06',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Identify the correct description of the two components into '
                'which a force is resolved.',
        "options": [
            'Two perpendicular forces that together have the same effect as it',
            'Two smaller forces acting on two different objects at the same moment in time',
            'The parts of a force that are wasted as heat',
            'The forces that act on either end of a rope',
        ],
        "correct_index": 0,
        "why": 'Components are a replacement for one force by two at right '
               'angles, chosen so that nothing about the effect on the object '
               'changes. They act on the same object, not on two.',
    },
    {
        "id": 'ks4-resolving-forces-e07',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A pull of 50 N acts along the longest side of a 3-4-5 '
                'right-angled triangle whose horizontal side is the 4 and whose '
                'vertical side is the 3. Calculate the vertical component.',
        "options": [
            '40 N',
            '50 N',
            '37.5 N',
            '30 N',
        ],
        "correct_index": 3,
        "why": 'Scaling the triangle by 10 turns the 5 into 50 N, so the 3 '
               'becomes 30 N and the 4 becomes 40 N. The vertical side is the 3, '
               'giving 30 N.',
    },
    {
        "id": 'ks4-resolving-forces-e08',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'State what happens to the two perpendicular components of a '
                'force as its angle to the horizontal is increased from 0° '
                'towards 90°.',
        "options": [
            'Both components grow, because the force is being turned into a steeper direction',
            'The vertical component grows and the horizontal one shrinks',
            'The horizontal component grows and the vertical one shrinks',
            'Both stay the same, since the force itself is unchanged',
        ],
        "correct_index": 1,
        "why": 'Turning the force towards the vertical hands more of it to the '
               'vertical component and less to the horizontal. The two can never '
               'both grow, because the original force is fixed in size.',
    },
    {
        "id": 'ks4-resolving-forces-e09',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A box sits on a ramp. State the direction of the component of '
                'its weight that tends to make it slide.',
        "options": [
            'Vertically downwards, since weight acts straight down',
            'At right angles to the ramp surface',
            'Down the slope, acting parallel to the surface of the ramp itself',
            'Horizontally, towards the foot of the ramp',
        ],
        "correct_index": 2,
        "why": 'Weight is resolved into one part along the slope and one part '
               'pressing into it. Only the along-the-slope part can start the '
               'box moving; the other part is balanced by the ramp pushing back.',
    },
    {
        "id": 'ks4-resolving-forces-e10',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A scale drawing is being used to find the resultant of two '
                'forces. State what the length of each arrow must represent.',
        "options": [
            'The size of that force, drawn using the scale chosen for the diagram',
            'The distance over which the force acts, using the same scale',
            'The angle between the two forces',
            'The mass of the object being pushed',
        ],
        "correct_index": 0,
        "why": 'In a vector diagram, length stands for magnitude and the way the '
               'arrow points stands for direction. Distance travelled plays no '
               'part in finding a resultant.',
    },
    {
        "id": 'ks4-resolving-forces-e11',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A force is resolved into two perpendicular components that turn '
                'out to be equal in size. State the angle between the original '
                'force and either component.',
        "options": [
            '30°',
            '60°',
            '90°',
            '45°',
        ],
        "correct_index": 3,
        "why": 'The force is the diagonal of a square whose sides are the two '
               'components, and that diagonal sits at 45° to each side.',
    },
    {
        "id": 'ks4-resolving-forces-e12',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Two forces of 9.0 N and 12.0 N act at right angles at the same '
                'point. Calculate the resultant.',
        "options": [
            '21.0 N',
            '15.0 N',
            '3.0 N',
            '108 N',
        ],
        "correct_index": 1,
        "why": '9.0² + 12.0² = 81 + 144 = 225, and the square root of 225 is '
               '15.0 N. This is the 3-4-5 triangle scaled up by three.',
    },
    {
        "id": 'ks4-resolving-forces-e13',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'State why a vector triangle is drawn with the two force arrows '
                'joined tip to tail.',
        "options": [
            'So that the two forces can be measured with the same ruler at the same time',
            'So that the angle between them comes out as a right angle',
            'So that the closing side gives the resultant',
            'So that the triangle is equilateral',
        ],
        "correct_index": 2,
        "why": 'Tip-to-tail means the second force starts where the first '
               'finishes, so the single arrow closing the triangle has exactly '
               'the combined effect.',
    },
    {
        "id": 'ks4-resolving-forces-e14',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A rope pulls a sledge with a force of 100 N along a line that '
                'makes a 6-8-10 right-angled triangle with the ground, the 8 '
                'lying along the ground and the 6 vertical. Calculate the '
                'horizontal component.',
        "options": [
            '80 N',
            '60 N',
            '75 N',
            '50 N',
        ],
        "correct_index": 0,
        "why": 'Scaling the triangle by 10 makes the 10 into 100 N, so the 8 '
               'along the ground becomes 80 N. The 60 N answer is the vertical '
               'component instead.',
    },
    {
        "id": 'ks4-resolving-forces-e15',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Describe what happens to the size of the resultant when two '
                'perpendicular forces are both doubled.',
        "options": [
            'It stays the same, because both forces have changed by the same factor',
            'It becomes four times as large',
            'It is halved',
            'It doubles',
        ],
        "correct_index": 3,
        "why": 'Doubling both sides of a right-angled triangle doubles the '
               'hypotenuse too, because the shape is simply scaled up. Squaring '
               'appears in the working but not in the final ratio.',
    },
    {
        "id": 'ks4-resolving-forces-e16',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Two tugs pull on a barge from the same point: one with 30 kN '
                'due north and one with 40 kN due east. Calculate the size of '
                'the resultant pull.',
        "options": [
            '70 kN',
            '50 kN',
            '10 kN',
            '1200 kN',
        ],
        "correct_index": 1,
        "why": '30² + 40² = 2500, whose square root is 50 kN — the 3-4-5 '
               'triangle scaled by ten. Adding them would only be right if the '
               'two pulls were in the same direction.',
    },
    {
        "id": 'ks4-resolving-forces-e17',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Explain why the horizontal component of an angled rope pull is '
                'the part that matters when a crate is dragged across level '
                'ground.',
        "options": [
            'Because the vertical part of the pull is turned into heat by the friction under the crate',
            'Because only that part acts along the direction of travel',
            'Because the horizontal part is the larger of the two',
            'Because the vertical part of the pull is zero',
        ],
        "correct_index": 1,
        "why": 'Work is done, and motion produced, along the line of travel, so '
               'the horizontal component is the useful one. The vertical part '
               'lifts a little of the weight off the floor instead.',
    },
    {
        "id": 'ks4-resolving-forces-e18',
        "subtopic_slug": 'resolving-forces',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A 7.0 N force and a 24.0 N force act at right angles at one '
                'point on a bracket. Work out the resultant.',
        "options": [
            '25.0 N',
            '31.0 N',
            '17.0 N',
            '168 N',
        ],
        "correct_index": 0,
        "why": '7.0² + 24.0² = 49 + 576 = 625, and the square root of 625 is '
               '25.0 N. Subtracting gives 17.0 N, which would be right only if '
               'the two acted in opposite directions.',
    },
    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-resolving-forces-s05',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A garden roller is pushed with a force of 250 N along a line '
                'making a 3-4-5 right-angled triangle with the ground, the 4 '
                'along the ground and the 3 vertical. Calculate the downward '
                'component of the push.',
        "options": [
            '200 N',
            '150 N',
            '250 N',
            '83 N',
        ],
        "correct_index": 1,
        "why": 'Scaling by 50 turns the 5 into 250 N, so the vertical 3 becomes '
               '150 N and the horizontal 4 becomes 200 N. Pushing downwards like '
               'this presses the roller harder into the lawn.',
    },
    {
        "id": 'ks4-resolving-forces-s06',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Explain why resolving a force into two perpendicular components '
                'is useful when a crate is dragged along a floor by an angled '
                'rope.',
        "options": [
            'It replaces the single pull with two smaller pulls, so less effort is needed overall',
            'It removes the vertical part of the pull from the problem',
            'It converts the pull into a single downward force',
            'Each component can then be dealt with separately along its own line',
        ],
        "correct_index": 3,
        "why": 'Splitting the pull lets the horizontal part be set against '
               'friction and the vertical part against the weight, independently. '
               'The total effect is unchanged, so no effort is saved.',
    },
    {
        "id": 'ks4-resolving-forces-s07',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A vector triangle is drawn to a scale of 1.0 cm to 5.0 N, and '
                'the closing side measures 7.4 cm. Calculate the resultant '
                'force.',
        "options": [
            '37 N',
            '12.4 N',
            '1.5 N',
            '74 N',
        ],
        "correct_index": 0,
        "why": 'Each centimetre stands for 5.0 N, so 7.4 cm stands for 7.4 x 5.0 '
               '= 37 N. Reading a scale drawing always means multiplying the '
               'measured length by the scale.',
    },
    {
        "id": 'ks4-resolving-forces-s08',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A box of weight 400 N rests on a slope that rises 3.0 m for '
                'every 5.0 m measured along the slope. Determine the component '
                'of the weight acting down the slope.',
        "options": [
            '320 N',
            '133 N',
            '240 N',
            '400 N',
        ],
        "correct_index": 2,
        "why": 'Rise over slope length is 3.0 / 5.0 = 0.600, so the component '
               'down the slope is 0.600 x 400 = 240 N. The 320 N answer uses the '
               'other side of the triangle, which presses into the slope.',
    },
    {
        "id": 'ks4-resolving-forces-s09',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Describe how the two perpendicular components are drawn from a '
                'single force arrow on a scale diagram.',
        "options": [
            'Extend the arrow in both directions until it meets the two axes it is split along',
            'Draw a rectangle with the force arrow as its diagonal; the sides are the components',
            'Draw a circle of that radius and mark two points on it',
            'Halve the arrow and turn one half through a right angle',
        ],
        "correct_index": 1,
        "why": 'The force is the diagonal of a rectangle whose sides lie along '
               'the two chosen directions, so measuring those sides gives the '
               'two components directly.',
    },
    {
        "id": 'ks4-resolving-forces-s10',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'State one advantage of finding a resultant by scale drawing '
                'rather than by calculation.',
        "options": [
            'It gives an exact answer, whereas a calculation can only ever be approximate',
            'It avoids any arithmetic once the diagram has been drawn carefully',
            'It works for forces at any angle, not just perpendicular ones',
            'It needs neither a ruler nor a protractor',
        ],
        "correct_index": 2,
        "why": 'Pythagoras only handles a right angle, but a drawing handles any '
               'angle at all. The price is precision: a measured length is never '
               'as exact as a calculated one.',
    },
    {
        "id": 'ks4-resolving-forces-s11',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A model boat is acted on at one point by 3.0 N northwards and '
                '4.0 N eastwards. Determine the size of the resultant and the '
                'general direction in which it points.',
        "options": [
            '7.0 N, pointing between north and east, because the forces simply add',
            '12.0 N, pointing between north and east',
            '5.0 N, pointing between north and east',
            '1.0 N, pointing due north',
        ],
        "correct_index": 2,
        "why": '3.0² + 4.0² = 25, so the resultant is 5.0 N, and it must lie '
               'between the two contributing directions. Multiplying the two '
               'forces gives 12.0, which is not a force at all.',
    },
    {
        "id": 'ks4-resolving-forces-s12',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A sledge of weight 500 N rests on a slope, and the component of '
                'its weight acting down the slope is 300 N. Determine the '
                'component pressing it against the slope surface.',
        "options": [
            '200 N',
            '800 N',
            '250 N',
            '400 N',
        ],
        "correct_index": 3,
        "why": 'The two components are perpendicular, so 300² + (that component)² '
               '= 500². Since 500² - 300² = 160 000, the missing component is '
               '400 N — the 3-4-5 triangle again.',
    },
    {
        "id": 'ks4-resolving-forces-s13',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Explain why the component of weight acting down a slope gets '
                'bigger as the slope is made steeper.',
        "options": [
            'Because the weight itself grows as the object is raised further above the ground',
            'Because more of the weight now lies along the slope direction',
            'Because friction falls away as the slope steepens',
            'Because the slope becomes shorter as it steepens',
        ],
        "correct_index": 1,
        "why": 'The weight is fixed; steepening the slope simply hands a larger '
               'share of it to the along-the-slope component and a smaller share '
               'to the one pressing into the surface.',
    },
    {
        "id": 'ks4-resolving-forces-s14',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Two ropes are attached to a stuck car at the same point: one '
                'exerts 600 N due north, the other 800 N due east. Calculate the '
                'single force that would have the same effect.',
        "options": [
            '1400 N',
            '200 N',
            '480 000 N',
            '1000 N',
        ],
        "correct_index": 3,
        "why": '600² + 800² = 1 000 000, whose square root is 1000 N. That single '
               'force is the resultant: one force with the same effect as the '
               'two together.',
    },
    {
        "id": 'ks4-resolving-forces-s15',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A pair of perpendicular components is quoted as 60 N and 80 N '
                'for a single 100 N force. Describe the test that shows the pair '
                'is consistent.',
        "options": [
            'Check that 60² + 80² equals 100², which it does',
            'Check that the two components add to the original force, and 60 + 80 = 140, so they do not',
            'Check that neither component is larger than 100 N',
            'Check that the two components are equal in size',
        ],
        "correct_index": 0,
        "why": 'Perpendicular components and their force form a right-angled '
               'triangle, so the squares must agree: 3600 + 6400 = 10 000. '
               'Components add as vectors, never as plain numbers.',
    },
    {
        "id": 'ks4-resolving-forces-s16',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A wheelbarrow handle is pulled with 260 N along a line making a '
                '5-12-13 right-angled triangle with the ground, the 12 lying '
                'along the ground. Calculate the vertical component.',
        "options": [
            '240 N',
            '130 N',
            '108 N',
            '100 N',
        ],
        "correct_index": 3,
        "why": 'Scaling by 20 turns the 13 into 260 N, so the vertical 5 becomes '
               '100 N and the horizontal 12 becomes 240 N. The upward pull is '
               'the smaller of the two here.',
    },
    {
        "id": 'ks4-resolving-forces-s17',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Describe the resultant of two perpendicular forces that are '
                'equal in size.',
        "options": [
            'It is twice either force and lies along whichever was drawn first',
            'It is larger than either force and lies midway between the two',
            'It is equal to either force and lies midway between them',
            'It is zero, because the two are at right angles',
        ],
        "correct_index": 1,
        "why": 'The two equal sides make a square, so the diagonal is longer than '
               'either side and runs at 45° to both. It is about 1.4 times a '
               'side, not twice.',
    },
    {
        "id": 'ks4-resolving-forces-s18',
        "subtopic_slug": 'resolving-forces',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A 150 N force is resolved along two perpendicular directions, '
                'and the component along the first comes out as 150 N. Deduce '
                'the component along the second.',
        "options": [
            'Zero, because the force lies entirely along the first direction',
            '150 N, since the two components match in size',
            '75 N, because the force is shared between the two',
            '212 N, from 150 N multiplied by the square root of two',
        ],
        "correct_index": 0,
        "why": 'If one component is the whole force, there is nothing of the '
               'force left to point anywhere else, so the other component is '
               'zero. The squares confirm it: 150² + 0² = 150².',
    },
    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-resolving-forces-h05',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A loading ramp climbs 7.0 m for each 25 m of its sloping '
                'surface. A crate weighing 750 N is placed on it. Determine how '
                'much of that weight acts along the ramp, pulling it down.',
        "options": [
            '720 N',
            '2679 N',
            '105 N',
            '210 N',
        ],
        "correct_index": 3,
        "why": 'The ratio rise / slope length is 7.0 / 25 = 0.280, so the '
               'component down the ramp is 0.280 x 750 = 210 N. The 720 N answer '
               'uses 24 / 25 and gives the force pressing into the ramp.',
    },
    {
        "id": 'ks4-resolving-forces-h06',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A bracket carries 40 N due west and 9.0 N due south at the same '
                'point. The resultant makes an angle of 13° with the westward '
                'direction. Determine the resultant.',
        "options": [
            '49 N, at 13° south of west, since the two forces simply add',
            '41 N, at 13° south of west',
            '41 N, at 13° west of south',
            '31 N, at 13° south of west',
        ],
        "correct_index": 1,
        "why": '40² + 9.0² = 1600 + 81 = 1681, whose square root is 41 N. The '
               'small angle belongs to the west direction because the westward '
               'force is much the larger of the two.',
    },
    {
        "id": 'ks4-resolving-forces-h07',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A ladder leans against a wall. A student says the weight of the '
                'ladder may be resolved into a component along the ladder and a '
                'component at right angles to it. Evaluate this.',
        "options": [
            'Wrong: weight can be resolved into a vertical and a horizontal component and no other pair',
            'Wrong: weight acts at the centre of mass, so it cannot be resolved',
            'Right: a force can be resolved along any two perpendicular directions',
            'Right, but this holds only when the ladder sits at 45° to the ground',
        ],
        "correct_index": 2,
        "why": 'The pair of directions is a choice made for convenience, not a '
               'property of the force. Choosing them along and across the ladder '
               'is exactly what makes a sliding-ladder problem tractable.',
    },
    {
        "id": 'ks4-resolving-forces-h08',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A trailer is pulled by two cables from the same hitch: one pulls '
                'with 3.0 kN due north, the other with 4.0 kN due east. Determine '
                'the single force that could replace them.',
        "options": [
            '7.0 kN, acting between north and east, because the two cables simply add',
            '12 kN, acting between north and east, from 3.0 multiplied by 4.0',
            '5.0 kN, acting between north and east',
            '1.0 kN, acting due north',
        ],
        "correct_index": 2,
        "why": 'The cables are perpendicular, so the replacement force is the '
               'hypotenuse: 3.0² + 4.0² = 25, giving 5.0 kN, aimed between the '
               'two cable directions and nearer the larger pull.',
    },
    {
        "id": 'ks4-resolving-forces-h09',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A sledge of weight 1300 N is held at rest by a rope running '
                'straight up a slope that rises 5.0 m for every 13 m along its '
                'surface. Determine the tension, taking friction as negligible.',
        "options": [
            '1200 N',
            '1500 N',
            '650 N',
            '500 N',
        ],
        "correct_index": 3,
        "why": 'The rope has to match the component of weight down the slope, '
               'which is (5.0 / 13) x 1300 = 500 N. The 1200 N answer is the '
               'component pressing into the slope, which the surface supports.',
    },
    {
        "id": 'ks4-resolving-forces-h10',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A student draws a vector triangle for two forces but joins the '
                'arrows tail to tail instead of tip to tail. Explain what goes '
                'wrong.',
        "options": [
            'Nothing goes wrong, provided the angle between the arrows is still correct',
            'The closing side now gives the difference of the two forces, rather than their resultant',
            'The scale of the drawing is doubled without warning',
            'The resultant comes out at right angles to the true answer',
        ],
        "correct_index": 1,
        "why": 'Joined tail to tail, the line closing the gap runs from one tip '
               'to the other, which represents one force subtracted from the '
               'other. The resultant needs the second arrow to start where the '
               'first ends.',
    },
    {
        "id": 'ks4-resolving-forces-h11',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A skier of weight 800 N stands on a piste. The component of her '
                'weight at right angles to the snow surface is 640 N. Determine '
                'the component acting down the slope.',
        "options": [
            '160 N',
            '1024 N',
            '480 N',
            '600 N',
        ],
        "correct_index": 2,
        "why": 'The components are perpendicular, so 800² - 640² = 640 000 - '
               '409 600 = 230 400, whose square root is 480 N. Subtracting the '
               'forces directly gives 160 N and ignores the right angle.',
    },
    {
        "id": 'ks4-resolving-forces-h12',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Explain why a wheelchair ramp is built long and shallow rather '
                'than short and steep.',
        "options": [
            'A shallower slope leaves a smaller component of weight acting down it, so less force is needed to push up',
            'A longer ramp reduces the weight of the chair and its user',
            'A shallower slope increases the friction, which helps the push',
            'A longer ramp shortens the distance that has to be covered',
        ],
        "correct_index": 0,
        "why": 'The weight is unchanged, but a gentle slope gives it only a small '
               'component along the ramp. The trade is distance: the same work is '
               'done over a longer push.',
    },
    {
        "id": 'ks4-resolving-forces-h13',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Two perpendicular forces acting at a point give a resultant of '
                '25 N, and one of them is 24 N. Determine the other.',
        "options": [
            '1 N',
            '49 N',
            '35 N',
            '7 N',
        ],
        "correct_index": 3,
        "why": '25² - 24² = 625 - 576 = 49, whose square root is 7 N. Subtracting '
               'the forces themselves gives 1 N, which is the error the squares '
               'are there to prevent.',
    },
    {
        "id": 'ks4-resolving-forces-h14',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Two tugs pull a barge at equal angles either side of its axis, '
                'each with 5.0 kN, and each contributes 4.0 kN along the axis. '
                'Determine the total forward force on the barge.',
        "options": [
            'A total of 10.0 kN, since the two pulls simply add along the axis',
            'A total of 8.0 kN',
            'A total of 6.4 kN',
            'A total of 3.0 kN',
        ],
        "correct_index": 1,
        "why": 'Only the along-the-axis components drive the barge forwards, and '
               'they add: 4.0 + 4.0 = 8.0 kN. The sideways components are equal '
               'and opposite, so they cancel.',
    },
    {
        "id": 'ks4-resolving-forces-h15',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A framed photograph of weight 90 N is supported by two identical '
                'cords. Show why the upward part of the pull in each cord must be '
                '45 N.',
        "options": [
            'Because the two cords share the weight equally when they are vertical',
            'Because each cord is half the length of the frame it carries',
            'Because the two upward components together balance the 90 N weight',
            'Because the horizontal components add to 90 N as well',
        ],
        "correct_index": 2,
        "why": 'The frame is in equilibrium, so the upward components must sum to '
               'the weight, and identical cords share that equally: 45 N each. '
               'Their horizontal components cancel instead of adding.',
    },
    {
        "id": 'ks4-resolving-forces-h16',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A pull of 500 N acts along a line making a 3-4-5 right-angled '
                'triangle with a horizontal floor, the 4 lying along the floor. '
                'Determine both components and state which is larger.',
        "options": [
            'Horizontal 400 N and vertical 300 N; the horizontal is larger',
            'Horizontal 300 N and vertical 400 N; the vertical is larger, because the line rises',
            'Both are 250 N, so neither is larger',
            'Horizontal 500 N and vertical 400 N',
        ],
        "correct_index": 0,
        "why": 'Scaling by 100 gives 300 N along the 3 and 400 N along the 4, and '
               'the 4 is the side lying along the floor, so the horizontal '
               'component is the larger.',
    },
    {
        "id": 'ks4-resolving-forces-h17',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A student states that a resultant can never be smaller than the '
                'larger of the two forces making it. Evaluate that statement for '
                'two perpendicular forces.',
        "options": [
            'Wrong: two perpendicular forces of 6 N and 8 N give a resultant of 2 N, smaller than 8 N',
            'Wrong: the resultant of two perpendicular forces is the smaller of the two',
            'Right, and it holds for two forces at any angle whatsoever',
            'Right for perpendicular forces, because the resultant is the hypotenuse of a right-angled triangle',
        ],
        "correct_index": 3,
        "why": 'A hypotenuse is longer than either other side, so perpendicular '
               'forces always give a bigger resultant. At other angles it can '
               'fail: two opposing forces of 8 N and 6 N give only 2 N.',
    },
    {
        "id": 'ks4-resolving-forces-h18',
        "subtopic_slug": 'resolving-forces',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Two people push a heavy crate from the same corner, one with '
                '120 N due east and one with 160 N due north, hoping to send it '
                'exactly north-east. Determine what is wrong with the plan.',
        "options": [
            'Nothing is wrong: two perpendicular pushes give a resultant exactly halfway between them',
            'The resultant is 280 N, which is more than the crate can take',
            'The pushes are unequal, so the resultant leans towards the larger one',
            'The resultant is zero, because the pushes are at right angles',
        ],
        "correct_index": 2,
        "why": 'A resultant sits halfway between two perpendicular forces only '
               'when they are equal. Here the 160 N push dominates, so the crate '
               'heads north of north-east, and the resultant is 200 N, not 280 N.',
    },
]
