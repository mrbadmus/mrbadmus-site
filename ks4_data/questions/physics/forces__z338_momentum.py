"""Physics · Forces — the MRB-338 expansion for `momentum`.

Higher tier, and the leaf turns on two separate ideas that pupils merge: that
momentum is a VECTOR, so a rebound is a change of 2mv rather than zero, and
that a force is a RATE of change of momentum, so lengthening a collision is
what makes it survivable.

The frozen twelve already own the unit kg m/s, a single p = m v car
calculation, "why is momentum a vector", the closed-system sentence, a tennis
ball, two trolleys meeting head-on, a golf-vs-bowling comparison, a ball
rebounding off a wall, a rear-end car collision, a firework shell explosion, a
cricket catch, and the cannon-recoil claim. None of those is asked again here.

The new rows take the ground they leave: rearranging p = m v for mass and for
velocity, the word equation F = change in momentum / time, recoil in the other
directions (rifle, rocket, skaters, a thrown medicine ball), collisions where
the objects SEPARATE rather than stick, conservation with one body initially at
rest, the unit conversion km/h -> m/s inside a force calculation, and the whole
family of safety applications the twelve never touch — crumple zones, air bags,
seat belts, crash mats, climbing rope and bending the knees. Every arithmetic
answer below was checked against the values stated in its own stem.
"""

TOPIC = "forces"
SUBJECT = "physics"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-momentum-e05',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Momentum is calculated from two quantities. Name them.',
        "options": [
            'Mass and velocity',
            'Mass and acceleration',
            'Weight and velocity',
            'The force acting and the time it acts for',
        ],
        "correct_index": 0,
        "why": 'p = m v, so momentum comes from mass in kg and velocity in m/s. '
               'Force and time give the CHANGE in momentum, not the momentum '
               'itself.',
    },
    {
        "id": 'ks4-momentum-e06',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A skateboarder and her board have a combined mass of 55 kg and '
                'roll along at 4.0 m/s. Calculate the momentum.',
        "options": [
            '13.8 kg m/s',
            '220 kg m/s',
            '59 kg m/s',
            '110 kg m/s',
        ],
        "correct_index": 1,
        "why": 'p = m v = 55 x 4.0 = 220 kg m/s. Dividing the mass by the '
               'velocity gives 13.8, which is the commonest slip here.',
    },
    {
        "id": 'ks4-momentum-e07',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A football of mass 0.42 kg leaves a boot at 15 m/s. Work out '
                'its momentum.',
        "options": [
            '35.7 kg m/s',
            '0.028 kg m/s',
            '6.3 kg m/s',
            '15.4 kg m/s',
        ],
        "correct_index": 2,
        "why": 'p = 0.42 x 15 = 6.3 kg m/s. A mass smaller than 1 kg gives a '
               'momentum smaller than the speed, which is worth expecting '
               'before the arithmetic starts.',
    },
    {
        "id": 'ks4-momentum-e08',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Two identical trolleys have the same mass and the same speed '
                'but travel in opposite directions. Compare their momenta.',
        "options": [
            'The momenta are identical, since both depend on mass and speed alone',
            'The trolley moving forwards has the greater momentum',
            'Neither has any momentum, because the two cancel out',
            'Equal in size but opposite in direction',
        ],
        "correct_index": 3,
        "why": 'Momentum is a vector, so identical masses and speeds give equal '
               'magnitudes with opposite signs. The momenta cancel only when '
               'you ADD them for the pair; each trolley still has its own.',
    },
    {
        "id": 'ks4-momentum-e09',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what is meant by a closed system when momentum is being '
                'discussed.',
        "options": [
            'A system in which no external force acts, so the total momentum stays the same',
            'A system in which nothing is moving',
            'A system that is sealed so that no air can get in or out',
            'A system in which all the objects have the same mass',
        ],
        "correct_index": 0,
        "why": 'Closed means no force from outside the group of objects, which '
               'is the condition for the total momentum to be unchanged. It '
               'has nothing to do with air or with sealing anything.',
    },
    {
        "id": 'ks4-momentum-e10',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A laboratory trolley of mass 2.5 kg has a momentum of '
                '7.5 kg m/s. Find its velocity.',
        "options": [
            '18.8 m/s',
            '3.0 m/s',
            '0.33 m/s',
            '5.0 m/s',
        ],
        "correct_index": 1,
        "why": 'Rearranging p = m v gives v = p / m = 7.5 / 2.5 = 3.0 m/s. '
               'Multiplying instead of dividing gives 18.8, and subtracting '
               'gives 5.0.',
    },
    {
        "id": 'ks4-momentum-e11',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A dodgem car moving at 2.0 m/s carries a momentum of '
                '260 kg m/s. Find its mass.',
        "options": [
            '0.0077 kg',
            '520 kg',
            '130 kg',
            '258 kg',
        ],
        "correct_index": 2,
        "why": 'm = p / v = 260 / 2.0 = 130 kg. The units help: kg m/s divided '
               'by m/s leaves kg.',
    },
    {
        "id": 'ks4-momentum-e12',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A gymnast bends her knees as she lands from a vault. State the '
                'effect this has on the landing.',
        "options": [
            'Her momentum is reduced before she lands, so there is less to take away',
            'The force is larger but acts for a shorter time',
            'Her change in momentum becomes zero',
            'The stopping time is longer, so the force on her is smaller',
        ],
        "correct_index": 3,
        "why": 'She has the same momentum to lose either way; bending the knees '
               'spreads that loss over a longer time, and force is change in '
               'momentum divided by time.',
    },
    {
        "id": 'ks4-momentum-e13',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A rifle recoils backwards when it fires a bullet forwards. '
                'Identify the reason.',
        "options": [
            'The explosion gives the rifle a backward push that is bigger than the forward push on the bullet',
            'Momentum forwards must be balanced by momentum backwards',
            'The bullet drags a column of air backwards past the rifle',
            'The rifle has a larger mass than the bullet',
        ],
        "correct_index": 1,
        "why": 'Rifle and bullet start with zero total momentum, so the forward '
               'momentum of the bullet must be matched by backward momentum of '
               'the rifle. The two pushes are equal in size, not different.',
    },
    {
        "id": 'ks4-momentum-e14',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A pupil of mass 48 kg walks at a typical walking speed of '
                '1.5 m/s. Calculate his momentum.',
        "options": [
            '72 kg m/s',
            '32 kg m/s',
            '49.5 kg m/s',
            '108 kg m/s',
        ],
        "correct_index": 0,
        "why": 'p = 48 x 1.5 = 72 kg m/s. Dividing gives 32 and adding gives '
               '49.5; neither has the units kg m/s.',
    },
    {
        "id": 'ks4-momentum-e15',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Write the word equation that links force to momentum.',
        "options": [
            'force = momentum x time taken',
            'force = momentum / mass',
            'force = change in momentum / time taken',
            'force = change in velocity / change in momentum',
        ],
        "correct_index": 2,
        "why": 'Force is the RATE of change of momentum, so the change is '
               'divided by the time it took. In symbols, F = change in p / '
               'change in t.',
    },
    {
        "id": 'ks4-momentum-e16',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A shopping trolley is pushed so that its momentum doubles, '
                'while its mass is unchanged. State what has happened to its '
                'velocity.',
        "options": [
            'It has increased four times',
            'It is unchanged',
            'It has halved',
            'It has doubled',
        ],
        "correct_index": 3,
        "why": 'p = m v with m fixed makes p directly proportional to v, so '
               'doubling one doubles the other. The four-times answer belongs '
               'to kinetic energy, which depends on v squared.',
    },
    {
        "id": 'ks4-momentum-e17',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Modern cars are built with crumple zones at the front. State '
                'what a crumple zone does in a crash.',
        "options": [
            'It increases the time over which the car stops, lowering the force on the people inside',
            'It makes the car stop more quickly',
            'It prevents the car losing any momentum',
            'It makes the front of the car heavier',
        ],
        "correct_index": 0,
        "why": 'Crumpling metal takes time, and stretching the stop out over a '
               'longer time cuts the rate of change of momentum, which is the '
               'force.',
    },
    {
        "id": 'ks4-momentum-e18',
        "subtopic_slug": 'momentum',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A lorry and a bicycle travel along the same road at the same '
                'speed. Compare their momenta.',
        "options": [
            'The bicycle, because a smaller mass is easier to accelerate to that speed',
            'Neither, because a momentum comparison needs the directions as well',
            'The lorry: greater mass at the same speed means greater momentum',
            'They are equal, as they share the same speed',
        ],
        "correct_index": 2,
        "why": 'With v the same for both, p = m v makes momentum depend on mass '
               'alone. Both are travelling the same way along the road, so the '
               'directions do not separate them.',
    },
    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-momentum-s05',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 4.0 kg trolley moving at 3.0 m/s runs into a stationary '
                '2.0 kg trolley, and the two move off together. Calculate their '
                'common velocity.',
        "options": [
            '2.0 m/s',
            '1.5 m/s',
            '3.0 m/s',
            '6.0 m/s',
        ],
        "correct_index": 0,
        "why": 'Momentum before = 4.0 x 3.0 = 12 kg m/s, and the combined mass '
               'is 6.0 kg, so v = 12 / 6.0 = 2.0 m/s. The moving trolley must '
               'slow, because the same momentum now carries more mass.',
    },
    {
        "id": 'ks4-momentum-s06',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'During a serve, the momentum of a tennis ball changes by '
                '3.5 kg m/s while the racket is in contact with it for 0.025 s. '
                'Calculate the average force.',
        "options": [
            '0.0875 N',
            '87.5 N',
            '0.14 N',
            '140 N',
        ],
        "correct_index": 3,
        "why": 'F = change in p / t = 3.5 / 0.025 = 140 N. Multiplying by the '
               'time rather than dividing gives 0.0875 N, which is far too '
               'small to send a ball anywhere.',
    },
    {
        "id": 'ks4-momentum-s07',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain how a seat belt that stretches slightly reduces injury '
                'in a crash.',
        "options": [
            'It reduces the momentum the wearer had before the crash, so less of it has to go',
            'It lengthens the time over which the wearer slows down',
            "It transfers the wearer's momentum into the body of the car",
            'It makes the momentum change smaller and quicker',
        ],
        "correct_index": 1,
        "why": 'The wearer arrives with whatever momentum the car had; the belt '
               'cannot change that. Stretching lets the same change happen over '
               'a longer time, so the average force is smaller.',
    },
    {
        "id": 'ks4-momentum-s08',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A hockey ball of mass 0.25 kg is travelling east at 12 m/s when '
                'a player strikes it so that it moves west at 8.0 m/s. Taking '
                'east as the positive direction, determine the change in '
                'momentum.',
        "options": [
            '1.0 kg m/s west',
            '5.0 kg m/s east',
            '5.0 kg m/s west',
            '1.0 kg m/s east',
        ],
        "correct_index": 2,
        "why": 'Momentum after is -2.0 kg m/s and before is +3.0 kg m/s, so the '
               'change is -5.0 kg m/s, that is 5.0 kg m/s westwards. Ignoring '
               'the sign change and subtracting the sizes gives 1.0.',
    },
    {
        "id": 'ks4-momentum-s09',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Two skaters stand at rest on ice facing each other and push '
                'apart. The 45 kg skater moves off at 2.0 m/s. Calculate the '
                'speed of the 60 kg skater.',
        "options": [
            '1.5 m/s',
            '2.0 m/s',
            '2.7 m/s',
            '0.86 m/s',
        ],
        "correct_index": 0,
        "why": 'Total momentum starts at zero, so the 60 kg skater must carry '
               '90 kg m/s the other way: v = 90 / 60 = 1.5 m/s. Dividing by the '
               'combined 105 kg gives 0.86 and forgets that only one skater '
               'moves that way.',
    },
    {
        "id": 'ks4-momentum-s10',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A collision takes place inside a closed system. Identify the '
                'statement that must be true.',
        "options": [
            'Each object ends with the momentum it started with',
            'The total momentum after the collision is always the same as the total momentum before it',
            'The kinetic energy is unchanged by the collision too',
            'Momentum is shared out equally between the two objects',
        ],
        "correct_index": 1,
        "why": 'Conservation applies to the TOTAL, not to each object, and not '
               'to kinetic energy, which can be transferred to thermal and '
               'sound stores during the impact.',
    },
    {
        "id": 'ks4-momentum-s11',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 1200 kg car travelling at 15 m/s is brought to rest in 6.0 s. '
                'Calculate the average braking force.',
        "options": [
            '3000 N',
            '18 000 N',
            '2000 N',
            '300 N',
        ],
        "correct_index": 0,
        "why": 'The momentum to remove is 1200 x 15 = 18 000 kg m/s, and '
               '18 000 / 6.0 = 3000 N. Quoting 18 000 N forgets to divide by '
               'the time.',
    },
    {
        "id": 'ks4-momentum-s12',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'An air bag inflates in a front-end collision. Describe its '
                'effect on the driver.',
        "options": [
            "The air bag absorbs the driver's momentum, so no force is needed to stop him",
            "The driver's change in momentum is made smaller by the bag",
            'The driver stops over a longer time, so the force is smaller',
            'The driver stops in a shorter time and so feels less force',
        ],
        "correct_index": 2,
        "why": 'The driver still has to lose all his momentum. The bag simply '
               'spreads the loss over a longer time and a larger area, cutting '
               'the force.',
    },
    {
        "id": 'ks4-momentum-s13',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A rocket engine pushes exhaust gases backwards. Use momentum to '
                'explain why the rocket moves forwards.',
        "options": [
            'The escaping gases push against the air behind the rocket, driving it forwards',
            'The rocket loses mass, so its velocity has to rise',
            'The exhaust gases carry no momentum away with them',
            'The gases gain backward momentum, so the rocket gains forward momentum',
        ],
        "correct_index": 3,
        "why": 'Rocket plus gases form a closed system, so backward momentum in '
               'the exhaust is matched by forward momentum in the rocket. This '
               'is why rockets work in space, where there is no air to push on.',
    },
    {
        "id": 'ks4-momentum-s14',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 3.0 kg trolley moving at 4.0 m/s strikes a 1.0 kg trolley at '
                'rest. Afterwards the heavier trolley is still moving forwards, '
                'at 2.0 m/s. Calculate the velocity of the lighter trolley.',
        "options": [
            '12 m/s',
            '6.0 m/s',
            '2.0 m/s',
            '4.0 m/s',
        ],
        "correct_index": 1,
        "why": 'Before, the total is 12 kg m/s; afterwards the heavy trolley '
               'holds 3.0 x 2.0 = 6.0 kg m/s, so the light one holds the other '
               '6.0 kg m/s, giving 6.0 / 1.0 = 6.0 m/s.',
    },
    {
        "id": 'ks4-momentum-s15',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A high jumper lands on a thick foam crash mat rather than on '
                'bare ground. Explain the advantage.',
        "options": [
            "The mat lowers the jumper's weight while the landing takes place",
            'The mat reduces the momentum the jumper has on the way down',
            'The change in momentum is made to happen more quickly',
            'The stopping time is longer, so the force is smaller',
        ],
        "correct_index": 3,
        "why": 'Foam compresses, so the jumper sinks in and comes to rest over a '
               'longer time. Her weight and her momentum on arrival are exactly '
               'the same as they would be on bare ground.',
    },
    {
        "id": 'ks4-momentum-s16',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A loaded supermarket trolley carries a momentum of 96 kg m/s '
                'while moving at 1.6 m/s. Calculate its total mass.',
        "options": [
            '154 kg',
            '0.017 kg',
            '60 kg',
            '61.6 kg',
        ],
        "correct_index": 2,
        "why": 'm = p / v = 96 / 1.6 = 60 kg. Multiplying gives 154 kg, which is '
               'heavier than the trolley and its shopping put together.',
    },
    {
        "id": 'ks4-momentum-s17',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what must act on an object for its momentum to change.',
        "options": [
            'A change in its mass brought about by the collision',
            'An equal and opposite reaction force',
            'A change in the direction of gravity',
            'A resultant force',
        ],
        "correct_index": 3,
        "why": 'Force equals rate of change of momentum, so a non-zero resultant '
               'force is exactly the condition for momentum to change. With zero '
               'resultant force the momentum is constant.',
    },
    {
        "id": 'ks4-momentum-s18',
        "subtopic_slug": 'momentum',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A baseball of mass 0.15 kg is given a momentum of 6.0 kg m/s by '
                'an average force of 1500 N. Calculate how long the bat was in '
                'contact with it.',
        "options": [
            '0.25 s',
            '0.0040 s',
            '9000 s',
            '250 s',
        ],
        "correct_index": 1,
        "why": 'Rearranging F = change in p / t gives t = 6.0 / 1500 = 0.0040 s. '
               'Contact times in bat and racket sports are always a few '
               'thousandths of a second, which is why the forces are so large.',
    },
    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-momentum-h05',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'On an air track a 0.80 kg glider moving right at 5.0 m/s meets '
                'a 1.2 kg glider moving left at 2.0 m/s, and the two lock '
                'together on impact. Determine their velocity afterwards.',
        "options": [
            '3.2 m/s to the right',
            '0.80 m/s to the left',
            '0.80 m/s to the right',
            '1.6 m/s to the right',
        ],
        "correct_index": 2,
        "why": 'Taking right as positive, the total is (0.80 x 5.0) - (1.2 x '
               '2.0) = 4.0 - 2.4 = 1.6 kg m/s, shared by 2.0 kg, so v = 0.80 m/s '
               'to the right. Adding the two momenta instead of subtracting '
               'gives 3.2 m/s.',
    },
    {
        "id": 'ks4-momentum-h06',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 0.42 kg football is driven into a wall at 12 m/s and bounces '
                'straight back along the same line at 8.0 m/s, the contact '
                'lasting 0.050 s. Determine the average force the wall exerted '
                'on it.',
        "options": [
            '168 N',
            '33.6 N',
            '84 N',
            '1.68 N',
        ],
        "correct_index": 0,
        "why": 'The velocity reverses, so the change in momentum is 0.42 x (12 + '
               '8.0) = 8.4 kg m/s, and 8.4 / 0.050 = 168 N. Using 12 - 8.0 '
               'instead treats momentum as a scalar and halves the answer twice '
               'over.',
    },
    {
        "id": 'ks4-momentum-h07',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student writes that a crumple zone works because it reduces '
                'the momentum a car has before the crash begins. Evaluate that '
                'claim.',
        "options": [
            "Correct: a crumple zone lowers the car's momentum as it approaches the obstacle",
            'Wrong: the momentum before the crash is unchanged; the crumple zone lengthens the time taken to lose it',
            'Wrong: a crumple zone increases the force but shortens the crash',
            'Correct, because a lighter front end carries less momentum',
        ],
        "correct_index": 1,
        "why": 'Nothing at the front of a moving car alters the momentum it is '
               'carrying on the way in. The zone acts during the impact, '
               'stretching the stop out in time so that the force is smaller.',
    },
    {
        "id": 'ks4-momentum-h08',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 60 kg student stands on a 2.0 kg skateboard, both at rest on '
                'level ground, and throws a 4.0 kg medicine ball horizontally '
                'at 6.0 m/s. Determine the recoil speed of the student and '
                'board.',
        "options": [
            '0.40 m/s',
            '6.0 m/s',
            '0.097 m/s',
            '0.39 m/s',
        ],
        "correct_index": 3,
        "why": 'The ball carries 4.0 x 6.0 = 24 kg m/s away, so the student and '
               'board take 24 kg m/s the other way: v = 24 / 62 = 0.39 m/s. '
               'Leaving the 2.0 kg board out gives 0.40 m/s.',
    },
    {
        "id": 'ks4-momentum-h09',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Two railway trucks couple together in a collision. Explain why '
                'momentum is conserved here but kinetic energy is not.',
        "options": [
            'Kinetic energy is destroyed in the collision, while momentum is simply passed from one truck to the other',
            'Momentum is a vector and kinetic energy is a scalar, which is the whole reason',
            'No external force acts, so momentum is conserved; some kinetic energy becomes thermal and sound',
            'Both are conserved; the kinetic energy is simply harder to measure',
        ],
        "correct_index": 2,
        "why": 'Conservation of momentum needs only the absence of an external '
               'force. Kinetic energy has somewhere else to go — the buckling '
               'couplings warm up and the bang carries energy away — so it is '
               'not conserved, though the total energy is.',
    },
    {
        "id": 'ks4-momentum-h10',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Two identical pucks slide towards each other at equal speeds of '
                '3.0 m/s and stick together the moment they meet. Predict their '
                'motion afterwards and justify it.',
        "options": [
            'They stay at rest, because the total momentum before the impact was zero',
            'They move off at 3.0 m/s in the direction the first puck was going, since the momentum has to go somewhere',
            'They move off together at 1.5 m/s in the original direction of the first puck',
            'They rebound at 3.0 m/s each, because momentum is conserved',
        ],
        "correct_index": 0,
        "why": 'Equal masses at equal and opposite velocities give a total '
               'momentum of zero, and zero is what the joined pair must have. '
               'Their kinetic energy, unlike their momentum, is transferred away '
               'entirely.',
    },
    {
        "id": 'ks4-momentum-h11',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 1500 kg van travelling at 72 km/h is brought to rest by a '
                'constant force acting for 4.0 s. Determine the size of that '
                'force.',
        "options": [
            '27 000 N',
            '7500 N',
            '30 000 N',
            '1875 N',
        ],
        "correct_index": 1,
        "why": '72 km/h is 72 000 / 3600 = 20 m/s, so the momentum is 1500 x 20 '
               '= 30 000 kg m/s and F = 30 000 / 4.0 = 7500 N. Using 72 in the '
               'formula without converting gives 27 000 N.',
    },
    {
        "id": 'ks4-momentum-h12',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why a climbing rope designed to stretch is safer in a '
                'fall than one that does not stretch.',
        "options": [
            "A stretching rope reduces the climber's momentum during the fall",
            'A stretching rope makes the climber fall more slowly from the start',
            "A stretching rope lowers the climber's weight at the moment of impact",
            'A stretching rope brings the climber to rest over a longer time, so the rate of change of momentum, and with it the force, is smaller',
        ],
        "correct_index": 3,
        "why": 'The climber reaches the end of the rope with the same momentum '
               'whatever the rope is made of. Stretching only changes how long '
               'the stop takes, and force is change in momentum divided by time.',
    },
    {
        "id": 'ks4-momentum-h13',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 2000 kg railway wagon rolling at 3.0 m/s couples to a '
                'stationary wagon, and the pair then move at 1.2 m/s. Determine '
                'the mass of the stationary wagon.',
        "options": [
            '5000 kg',
            '2400 kg',
            '3000 kg',
            '1200 kg',
        ],
        "correct_index": 2,
        "why": 'Momentum before is 6000 kg m/s, so the joined mass is 6000 / 1.2 '
               '= 5000 kg, and the stationary wagon is 5000 - 2000 = 3000 kg. '
               'Quoting 5000 kg forgets to take the rolling wagon out.',
    },
    {
        "id": 'ks4-momentum-h14',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A ball rolling across a rough floor gradually slows down. '
                'Explain why this does not break conservation of momentum.',
        "options": [
            'Friction is an external force, so the ball on its own is not a closed system',
            'Momentum is always lost to friction, so the rule is an approximation in real situations',
            'The ball keeps its momentum; only its speed is falling',
            'Momentum is conserved for a single object but not for a pair',
        ],
        "correct_index": 0,
        "why": 'The rule applies to a closed system. Widen the system to include '
               'the floor and the Earth and the momentum the ball loses turns up '
               'there; the ball by itself has a force from outside acting on it.',
    },
    {
        "id": 'ks4-momentum-h15',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 55 kg student runs at 4.0 m/s and jumps onto a 5.0 kg sled '
                'that is at rest on ice. Determine how fast the student and sled '
                'then slide.',
        "options": [
            '4.0 m/s',
            '3.7 m/s',
            '44 m/s',
            '0.067 m/s',
        ],
        "correct_index": 1,
        "why": 'The momentum brought in is 55 x 4.0 = 220 kg m/s, carried '
               'afterwards by 60 kg, so v = 220 / 60 = 3.7 m/s. Adding mass at '
               'constant momentum must lower the speed a little.',
    },
    {
        "id": 'ks4-momentum-h16',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A tennis ball and a bowling ball collide head-on. Compare the '
                'forces they exert on each other and the changes in their '
                'velocities.',
        "options": [
            'The bowling ball exerts the larger force, so its velocity is the one that changes least',
            'The forces are equal, so both velocities change by the same amount',
            'The tennis ball exerts the larger force because it is moving faster',
            "The forces are equal and opposite, but the lighter ball's velocity changes far more",
        ],
        "correct_index": 3,
        "why": 'Newton\'s Third Law makes the forces an interaction pair, equal '
               'and opposite, so each ball receives the same size of momentum '
               'change. Dividing that by a small mass gives a large velocity '
               'change.',
    },
    {
        "id": 'ks4-momentum-h17',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A parachutist of mass 70 kg lands and is brought to rest in '
                '0.60 s. Just before touching down her momentum was 420 kg m/s. '
                'Determine the average stopping force.',
        "options": [
            '252 N',
            '117 N',
            '700 N',
            '420 N',
        ],
        "correct_index": 2,
        "why": 'F = 420 / 0.60 = 700 N. The 70 kg is there to be left alone: the '
               'momentum is already given, so the mass is not needed twice.',
    },
    {
        "id": 'ks4-momentum-h18',
        "subtopic_slug": 'momentum',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A hockey player receives a pass carrying 4.0 kg m/s of momentum '
                'northwards and returns it carrying 4.0 kg m/s southwards. A '
                'student claims the change in momentum is zero. Evaluate this '
                'claim.',
        "options": [
            'Wrong: momentum is a vector, so the change is 8.0 kg m/s southwards',
            'Correct, because the size of the momentum is the same before and after, so nothing has changed',
            'Wrong: the change is 4.0 kg m/s southwards',
            'Correct, since the stick gains no momentum of its own',
        ],
        "correct_index": 0,
        "why": 'Taking north as positive, the momentum goes from +4.0 to -4.0, a '
               'change of -8.0 kg m/s. Equal sizes in opposite directions is the '
               'largest change available, not the smallest.',
    },
]
