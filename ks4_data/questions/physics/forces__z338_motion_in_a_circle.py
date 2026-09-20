"""Physics · Forces — the MRB-338 expansion for `motion-in-a-circle`.

Higher tier and triple only. AQA asks for this QUALITATIVELY: steady speed with
a changing velocity because the direction changes, therefore an acceleration,
therefore a resultant force, and that force points at the centre of the circle.
No equation for centripetal force is required at GCSE and none is used here —
every comparison below is argued in words, and the only arithmetic is ordinary
speed from a path length and a time.

The frozen twelve already own: which quantity changes at steady speed, the
direction of the acceleration, the fairground rotor, the definition of a
centripetal force, why the motion is not equilibrium, the snapped string, a
cyclist's acceleration, the bottom of a vertical loop, the centrifugal claim,
two satellites' orbital speeds, why the Sun does no work on a planet, and
velocity against acceleration half a revolution apart.

The new rows take what they leave: the other suppliers of the inward force
(rail flanges, a banked track, a wall of death, the pull of a string, the push
of a bus seat), what happens when the supply fails (mud, a spin dryer, an icy
bend, a shopping bag, a coin on a turntable), the qualitative effect of speed,
radius and mass, the top-versus-bottom tension of a vertical circle, and the
perpendicular-force argument for why an orbit neither speeds up nor closes in.
"""

TOPIC = "forces"
SUBJECT = "physics"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-motion-in-a-circle-e05',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A conker is whirled round steadily on the end of a string. '
                'State the direction of the force the string exerts on it.',
        "options": [
            'Along the direction the conker is moving',
            'Towards the centre of the circle',
            'Outwards, away from the hand',
            'Vertically downwards',
        ],
        "correct_index": 1,
        "why": 'The string can only pull, and it pulls back along its own length '
               'towards the hand at the centre. That inward pull is what keeps '
               'the conker turning.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e06',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Name the force that keeps the Moon in its near-circular path '
                'around the Earth.',
        "options": [
            'The gravitational pull of the Earth',
            'A centrifugal force that pushes the Moon outwards and holds it clear',
            'Air resistance acting on the Moon',
            'The magnetic field of the Earth',
        ],
        "correct_index": 0,
        "why": 'Gravity is a non-contact force that acts across the gap and '
               'points from the Moon towards the Earth, which is the centre of '
               'the circle. There is no air in space to resist anything.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e07',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A child sits 2.0 m from the centre of a playground roundabout '
                'that completes one turn in 4.0 s. Calculate her speed.',
        "options": [
            '12.6 m/s',
            '0.50 m/s',
            '3.1 m/s',
            '1.6 m/s',
        ],
        "correct_index": 2,
        "why": 'One turn covers a circumference of 2 x pi x 2.0 = 12.6 m, so the '
               'speed is 12.6 / 4.0 = 3.1 m/s. Using the radius instead of the '
               'circumference gives 0.50 m/s.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e08',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'State what happens to the velocity of an object driven round a '
                'circular track at a steady speed.',
        "options": [
            'It stays the same, because velocity and speed mean the same thing when the speed is steady',
            'It increases steadily all the way round',
            'It is zero, since the object returns to its start',
            'It changes, because the direction of travel keeps changing',
        ],
        "correct_index": 3,
        "why": 'Velocity is a vector, so a change of direction is a change of '
               'velocity even when the number of metres per second never moves. '
               'That is what separates it from speed.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e09',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A car is driven round a bend on a flat, level road. Identify '
                'what provides the centripetal force.',
        "options": [
            'The push of the air on the side of the car as it turns',
            'Friction between the tyres and the road',
            'The force of the engine driving it forwards',
            'The weight of the car acting downwards',
        ],
        "correct_index": 1,
        "why": 'Sideways friction where rubber meets road is the only inward '
               'force available on a flat bend. The weight acts downwards and '
               'the engine acts forwards, so neither can turn the car.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e10',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A satellite travels around the Earth in a circular orbit at a '
                'steady speed. State whether it is accelerating.',
        "options": [
            'Yes, because its direction, and so its velocity, is changing',
            'Yes, because gravity makes everything speed up as it falls',
            'No, because there is no air resistance in space',
            'No, because its speed does not change',
        ],
        "correct_index": 0,
        "why": 'Acceleration is the rate of change of velocity, and velocity '
               'includes direction. A steady speed round a circle is therefore '
               'still an accelerated motion.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e11',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A bucket of water is swung quickly in a vertical circle and the '
                'water stays in the bucket even at the top. Identify the reason.',
        "options": [
            'A centrifugal force presses the water against the base',
            'The water is weightless while the bucket is moving',
            'At the top the water needs a downward force towards the centre, which its weight provides',
            'Air pressure holds the water inside the bucket',
        ],
        "correct_index": 2,
        "why": 'At the top of the circle the centre is below the bucket, so the '
               'force needed points downwards — and weight already points that '
               'way. The water is not held up; it is being pulled round.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e12',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A racing car takes a bend too quickly and slides off the track. '
                'Explain what has happened to the centripetal force.',
        "options": [
            'The centrifugal force has grown larger than the centripetal force and thrown the car out',
            'The centripetal force started acting outwards instead',
            'The car lost every bit of its momentum on the bend',
            'Friction could not supply the larger force the faster turn needed',
        ],
        "correct_index": 3,
        "why": 'A faster turn round the same bend needs a bigger inward force, '
               'and friction has a limit. Once the demand passes that limit the '
               'car carries on closer to a straight line.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e13',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Mud thrown off the tyre of a moving bicycle travels away in a '
                'straight line. State why.',
        "options": [
            'Nothing supplies the inward force once the mud leaves the tyre',
            'The spinning tyre flings it outwards with a force directed away from the centre',
            'Gravity takes over as soon as the mud leaves, pulling it away from the wheel',
            'The mud is repelled by the rubber of the tyre',
        ],
        "correct_index": 0,
        "why": 'While the mud is stuck to the tyre, the tyre pulls it round. Once '
               'it is free there is no inward force, so it carries straight on '
               'as Newton\'s First Law requires.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e14',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A satellite covers a circular orbit of total path length '
                '42 000 km in 5000 s. Calculate its average speed in m/s.',
        "options": [
            '84 000 m/s',
            '8.4 m/s',
            '8400 m/s',
            '4200 m/s',
        ],
        "correct_index": 2,
        "why": '42 000 km is 42 000 000 m, and 42 000 000 / 5000 = 8400 m/s. '
               'Working in kilometres without converting leaves the answer a '
               'thousand times too small.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e15',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A hammer thrower lets go of the hammer. Describe the path it '
                'takes at the instant of release.',
        "options": [
            'A curve that opens outwards, carrying on the circular motion it had',
            'A straight line along the tangent',
            'Straight outwards along the radius',
            'Straight down towards the ground',
        ],
        "correct_index": 1,
        "why": 'Its velocity at that instant is along the tangent, and with the '
               'inward pull gone nothing bends the path any more, so it keeps '
               'that direction.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e16',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Complete the sentence: the centripetal force on a body moving '
                'in a circle is ...',
        "options": [
            'an extra force that appears as soon as the body starts to turn',
            'the force the body exerts on whatever supports it',
            'equal in size to the weight of the body',
            'the resultant of the forces already acting on it',
        ],
        "correct_index": 3,
        "why": 'Centripetal names a JOB rather than a new kind of force: whatever '
               'the forces on the body happen to be, their resultant points at '
               'the centre.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e17',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A spin dryer turns wet clothes rapidly inside a drum with holes '
                'in its wall. Explain how the water leaves the clothes.',
        "options": [
            'The drum wall can push the clothes inwards but not the water, so the water carries straight on through the holes',
            'A centrifugal force throws the water outwards through the holes',
            'The spinning heats the water so that it evaporates',
            'The water is squeezed out by the weight of the clothes',
        ],
        "correct_index": 0,
        "why": 'The wall supplies the inward force that keeps the clothes on a '
               'circle. Water at a hole has nothing to push it inwards, so it '
               'continues in a straight line and leaves.',
    },
    {
        "id": 'ks4-motion-in-a-circle-e18',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": True,
        "text": 'State how the centripetal force needed changes when the same '
                'bend is taken at a higher speed.',
        "options": [
            'A smaller force is needed, because the car spends less time on the bend',
            'No force is needed once the car is moving quickly',
            'A larger force is needed',
            'The force needed stays the same',
        ],
        "correct_index": 2,
        "why": 'A faster body has to have its direction turned more sharply in '
               'each second, so a bigger inward force is required. This is why '
               'bends carry speed limits.',
    },
    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-motion-in-a-circle-s05',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A ball on a string is whirled in a horizontal circle. Describe '
                'how the tension changes if the ball is whirled faster on the '
                'same length of string.',
        "options": [
            'The tension decreases, because a faster ball spends less time on each part of the circle',
            'The tension stays the same',
            'The tension falls to zero',
            'The tension increases',
        ],
        "correct_index": 3,
        "why": 'The string supplies the whole inward force, and a faster circle '
               'of the same radius demands more of it, so the tension rises. '
               'Whirl hard enough and the string breaks.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s06',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A student says a satellite in a steady circular orbit has no '
                'resultant force on it because its speed is constant. Identify '
                'the flaw.',
        "options": [
            'Speed is constant, so there is indeed no resultant force; the flaw is in the wording',
            'Velocity changes direction, so there is an acceleration and a resultant force',
            'The satellite does have a resultant force, and it acts forwards',
            'The satellite is in equilibrium but still accelerates',
        ],
        "correct_index": 1,
        "why": 'Constant speed is not constant velocity. Since the velocity '
               'turns, the satellite accelerates, and an acceleration requires a '
               'resultant force — here, gravity.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s07',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Compare the direction of the velocity with the direction of the '
                'resultant force for a car going round a roundabout at a steady '
                'speed.',
        "options": [
            'They are at right angles: the velocity is along the tangent, the force towards the centre',
            'They both point towards the centre of the roundabout',
            'They point in opposite directions along the same line',
            'They both point along the tangent, in the direction of travel',
        ],
        "correct_index": 0,
        "why": 'The velocity is always tangential and the resultant force always '
               'radial and inward, so the two are perpendicular at every instant '
               'of the turn.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s08',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A stone tied to a 0.80 m string is whirled in a horizontal '
                'circle and completes 5.0 turns every second. Calculate its '
                'speed.',
        "options": [
            '4.0 m/s',
            '5.0 m/s',
            '25 m/s',
            '13 m/s',
        ],
        "correct_index": 2,
        "why": 'One turn is 2 x pi x 0.80 = 5.0 m, and five of those each second '
               'gives 25 m/s. Multiplying the radius by the turns instead gives '
               '4.0 m/s.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s09',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Describe what provides the centripetal force on a train rounding '
                'a curved section of track.',
        "options": [
            'The forward push of the engine, redirected around the curve by the rails',
            'The weight of the train pressing down on the curved track',
            'The friction of the brakes on the wheels',
            'The sideways push of the rails on the wheel flanges',
        ],
        "correct_index": 3,
        "why": 'The flanges bear against the inner faces of the rails, and the '
               'rails push back sideways towards the centre of the curve. The '
               'weight acts vertically and cannot turn anything.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s10',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A ball is swung above the head on a string; more string is then '
                'let out while the speed is kept the same. Describe how the '
                'force required changes.',
        "options": [
            'A larger force is needed, because the ball now has further to travel each turn',
            'A smaller force is needed, because the circle is now wider',
            'The force needed is unchanged, since the speed is unchanged',
            'No force is needed once the string is long enough',
        ],
        "correct_index": 1,
        "why": 'A wider circle bends the path more gently, so at the same speed '
               'less inward force is required. This is why motorway curves are '
               'made long and shallow.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s11',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Explain why the Moon does not simply drop onto the Earth even '
                'though the Earth pulls on it constantly.',
        "options": [
            "The Earth's pull is balanced by an equal outward force on the Moon",
            'It keeps moving sideways fast enough to stay in its orbit',
            'The Moon is too far away for gravity to reach it',
            'The Moon is held up by the pressure of sunlight',
        ],
        "correct_index": 1,
        "why": 'The pull does bend the path towards the Earth, but the sideways '
               'motion carries the Moon on past. The result is a closed curve '
               'rather than a fall.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s12',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A car drives at a steady speed over a humpback bridge. Describe '
                'the direction of the resultant force on it at the very top of '
                'the hump.',
        "options": [
            'Vertically upwards, because the road pushes harder than the weight there',
            'Zero, because the speed is steady over the whole bridge',
            'Vertically downwards, towards the centre',
            'Forwards, along the direction the car is travelling',
        ],
        "correct_index": 2,
        "why": 'The top of a hump is the top of a circular arc whose centre is '
               'below the road, so the resultant points down. That is why a car '
               'feels light there: the road pushes up with less than the weight.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s13',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A big wheel of radius 12 m turns steadily and carries a rider '
                'once round every 40 s. Calculate the speed of the rider.',
        "options": [
            '0.30 m/s',
            '0.94 m/s',
            '3.8 m/s',
            '1.9 m/s',
        ],
        "correct_index": 3,
        "why": 'The circumference is 2 x pi x 12 = 75 m, and 75 / 40 = 1.9 m/s. '
               'Dividing the radius rather than the circumference by the time '
               'gives 0.30 m/s.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s14',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A satellite in a circular orbit carries no working engine. '
                'Explain why its speed does not rise even though a force acts on '
                'it.',
        "options": [
            'The force is exactly cancelled by an equal outward force, so nothing changes',
            'The force always acts at right angles to the motion',
            'The satellite is too heavy to be speeded up by gravity',
            'Gravity in space is far too weak to change any speed',
        ],
        "correct_index": 1,
        "why": 'A force perpendicular to the velocity turns the motion without '
               'adding to it, so the direction changes and the speed does not. '
               'The force is real, so it is not cancelled by anything.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s15',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'On a steeply banked velodrome a cyclist rides round the bend '
                'without relying on friction. Identify what supplies the '
                'centripetal force.',
        "options": [
            "A sideways component of the track's push on the tyres",
            'The forward drive from the pedals, turned sideways by the slope of the track',
            'The weight of the cyclist acting straight down',
            'The air pushing on the side of the cyclist',
        ],
        "correct_index": 0,
        "why": 'The banked surface pushes at right angles to itself, and because '
               'it is tilted that push has a horizontal part pointing at the '
               'centre of the bend.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s16',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Two cars take the same bend at the same speed, but one is twice '
                'as heavy as the other. Compare the centripetal force each '
                'needs.',
        "options": [
            'They need the same force, because the bend and the speed are the same',
            'The heavier car needs four times the force',
            'The heavier car needs twice the force',
            'The heavier car needs half the force',
        ],
        "correct_index": 2,
        "why": 'Twice the mass has twice the momentum to be turned each second, '
               'so twice the inward force is required. Heavier vehicles need '
               'more grip to take the same bend.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s17',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A student writes that a body going round a circle at a steady '
                'speed has zero acceleration. Give the correction.',
        "options": [
            'The statement is right; acceleration means a change of speed, and the speed is steady',
            'The acceleration is along the tangent, in the direction of travel',
            'The acceleration points outwards, away from the centre',
            'Acceleration means a change of velocity, and the direction is changing',
        ],
        "correct_index": 3,
        "why": 'Acceleration is defined on velocity, not on speed, so turning '
               'counts. The acceleration is inward, which is neither along the '
               'tangent nor outward.',
    },
    {
        "id": 'ks4-motion-in-a-circle-s18',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": True,
        "text": 'An athlete runs one lap of a circular track of circumference '
                '400 m in 50 s at a steady speed. Calculate that speed.',
        "options": [
            '0.13 m/s',
            '8.0 m/s',
            '20 000 m/s',
            '4.0 m/s',
        ],
        "correct_index": 1,
        "why": 'Speed = distance / time = 400 / 50 = 8.0 m/s. Her average '
               'VELOCITY over the lap is zero, because she finishes where she '
               'started, which is a different question.',
    },
    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-motion-in-a-circle-h05',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A shopping bag resting on a bus seat slides towards the window '
                'as the bus goes round a roundabout. Explain the motion in terms '
                'of forces.',
        "options": [
            'An outward force acts on the bag and pushes it across the seat towards the window',
            'Gravity acts sideways for as long as the bus is turning',
            'The bag keeps going straight while the seat turns',
            'The seat pulls the bag outwards as the bus turns',
        ],
        "correct_index": 2,
        "why": 'Friction from the seat is too weak to turn the bag, so the bag '
               'keeps its straight-line motion while the bus curves away beneath '
               'it. No force pushes it outwards.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h06',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'The International Space Station circles about 400 km above the '
                'Earth while the Moon circles about 380 000 km away. Deduce '
                'which needs the larger inward force for each kilogram of its '
                'mass.',
        "options": [
            'The Moon, because it has a far greater distance to cover in one complete orbit',
            'The Moon, since its much greater mass demands more force per kilogram',
            'They are equal, because both are in free fall around the Earth',
            'The Station: gravity is far stronger that close to the Earth',
        ],
        "correct_index": 3,
        "why": 'The inward force is gravity, and gravity weakens rapidly with '
               'distance, so the close orbit demands far more per kilogram. Mass '
               'cancels out when the force is quoted per kilogram.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h07',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A spacecraft in a circular orbit fires a rocket briefly so that '
                'it speeds up, while the gravity acting on it is unchanged. '
                'Predict what happens to its path.',
        "options": [
            'It stays in the same circle but goes round faster',
            'It drops straight down towards the Earth',
            'It flies off along a straight line at once',
            'It moves into a larger orbit, because gravity can no longer bend its path so tightly',
        ],
        "correct_index": 3,
        "why": 'A faster craft needs a bigger inward force to hold the same '
               'circle. Gravity has not grown, so the path bends less sharply '
               'and the craft climbs into a wider orbit.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h08',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Explain, in terms of the centripetal force, why drivers are told '
                'to slow down on an icy bend.',
        "options": [
            'Ice adds an extra outward force on the car, which the brakes then have to overcome',
            'Ice cuts the friction available, so a smaller inward force is possible',
            'Ice makes the car heavier and harder to steer',
            'Ice increases the radius of every bend',
        ],
        "correct_index": 1,
        "why": 'The bend can only be taken if friction can supply the inward '
               'force it demands. Ice lowers the friction on offer, so the '
               'demand has to be lowered too — by going slower.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h09',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A ball is whirled on a string in a vertical circle at a steady '
                'speed. Compare the tension in the string at the top with the '
                'tension at the bottom.',
        "options": [
            'Larger at the top, because there the ball is furthest from the ground and moving fastest',
            'Larger at the top, as gravity tries to pull the ball off there',
            'Larger at the bottom, where the string must overcome the weight as well',
            'The same at both points, since the speed is the same',
        ],
        "correct_index": 2,
        "why": 'At the bottom the centre is above the ball, so the string has to '
               'pull up against the weight AND supply the inward force. At the '
               'top the weight already points inward, so the string does less.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h10',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A student claims that because the resultant force on an orbiting '
                'satellite is not zero, the satellite must be gaining speed. '
                'Evaluate the claim.',
        "options": [
            'Wrong: the force acts at right angles to the motion',
            "Correct: a resultant force always produces an increase in speed, by Newton's Second Law",
            'Correct, and this is why satellites must fire engines to stay in orbit',
            'Wrong: the resultant force on an orbiting satellite is in fact zero',
        ],
        "correct_index": 0,
        "why": 'A resultant force produces an acceleration, and an acceleration '
               'can be a pure change of direction. Here it is, so the speed is '
               'untouched while the velocity turns.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h11',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A cyclist rides eight complete laps of a circular track of '
                'circumference 250 m in 200 s at a steady speed. Determine her '
                'speed, and state whether she is accelerating.',
        "options": [
            '1.25 m/s, and she is accelerating throughout',
            '10 m/s, and she is not accelerating',
            '80 m/s, and she is not accelerating',
            '10 m/s, and she is accelerating throughout',
        ],
        "correct_index": 3,
        "why": 'Eight laps is 2000 m, so 2000 / 200 = 10 m/s. Her direction is '
               'changing the whole way, so she accelerates throughout despite '
               'the steady speed.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h12',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A car is driven at a steady speed once around a large circular '
                'test track. State the total work done on it by the centripetal '
                'force, and explain.',
        "options": [
            'Equal to the force multiplied by the circumference of the track, since work is force times distance',
            'The camber matters more than the force, so no figure can be given',
            'Zero: the force is always perpendicular to the motion',
            'Zero, because the car finishes where it started',
        ],
        "correct_index": 2,
        "why": 'Work needs a force component along the direction of movement, '
               'and there is none here. The returning-to-the-start answer gets '
               'the number right for the wrong reason.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h13',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Describe what a road engineer must change about a bend so that '
                'vehicles can take it safely at a higher speed, without any gain '
                'in grip.',
        "options": [
            'The bend must be made tighter, so the tyres have a shorter turn to grip through',
            'The camber of the road must be reversed so that it slopes outwards',
            'The bend must be made less tight, with a larger radius',
            'The bend must be made narrower',
        ],
        "correct_index": 2,
        "why": 'A larger radius bends the path more gently, so the same friction '
               'can hold a faster vehicle. Tightening the bend or tipping it '
               'outwards both raise the demand instead.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h14',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A bucket of water is swung in a vertical circle and the swing is '
                'then slowed right down. Predict what happens as the bucket '
                'passes the highest point, and explain.',
        "options": [
            'The water falls out, because its weight is now more than the inward force needed',
            'The water stays in, because the bucket is upside down',
            'The water falls out, because gravity grows stronger higher up',
            'The water stays in, since it has lost its momentum',
        ],
        "correct_index": 0,
        "why": 'A slow circle needs only a small inward force at the top, and '
               'weight alone supplies more than that, so the water is pulled out '
               'of the circle and leaves the bucket.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h15',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'In a thought experiment, the gravity of a planet is switched off '
                'while a probe circles it. Describe the motion of the probe from '
                'that moment on.',
        "options": [
            'It would spiral slowly outwards, gradually widening its orbit as it went',
            'It would stop where it was and stay there',
            'It would continue in the same circle',
            'It would travel in a straight line at a constant speed',
        ],
        "correct_index": 3,
        "why": 'With no resultant force, Newton\'s First Law takes over and the '
               'probe keeps the velocity it had at that instant — tangential, '
               'steady, and straight.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h16',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Explain how a satellite can be accelerating towards the Earth at '
                'every instant and yet never get any closer to it.',
        "options": [
            'It is not accelerating; the term is being used loosely to describe orbital motion',
            'Its sideways motion carries it around as fast as it is pulled inwards',
            'The acceleration is cancelled by an outward force of the same size',
            'It does get closer, but by an amount too small to detect',
        ],
        "correct_index": 1,
        "why": 'The inward acceleration changes the DIRECTION of the velocity '
               'rather than shortening the distance. The curve of the orbit '
               'matches the curve of the fall.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h17',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'Two identical coins rest on a turntable, one near the spindle '
                'and one near the rim. As the turntable is speeded up, predict '
                'which slides off first.',
        "options": [
            'The inner one, because it sits on the part of the turntable that turns most quickly',
            'They slide off together, since the coins are identical',
            'The outer one: it moves faster and needs more grip than friction can give',
            'Neither, because friction rises with speed to match the demand',
        ],
        "correct_index": 2,
        "why": 'Both coins take the same time for a turn, so the outer one covers '
               'a longer circle and moves faster. Friction has the same limit for '
               'each, and the outer coin reaches it first.',
    },
    {
        "id": 'ks4-motion-in-a-circle-h18',
        "subtopic_slug": 'motion-in-a-circle',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": True,
        "text": 'A theme park designer wants riders to go round a horizontal '
                'circle faster than before, using the same restraints. State '
                'what must be done to the ride.',
        "options": [
            'Widen the circle, so the same restraints can still supply the force needed',
            'Narrow the circle, so the riders are held closer in and need less force',
            'Raise the ride higher, to lower the effect of gravity',
            'Add weight to the cars, so they hold the track better',
        ],
        "correct_index": 0,
        "why": 'Going faster raises the inward force demanded, but a wider circle '
               'lowers it, so widening can keep the demand within what the '
               'restraints already provide.',
    },
]
