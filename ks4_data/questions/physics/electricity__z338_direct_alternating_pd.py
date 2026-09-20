"""Physics · Electricity — the MRB-338 expansion of `direct-alternating-pd`.

The weight falls on reading an oscilloscope, because that is where this spec
point's only real skill lives: the baseline rows read a period off the time
base, so these rows take the vertical axis (peak pd from volts per division),
the inverse calculation (period from frequency), and the settings themselves
(determining a time base or a y-gain from a known supply). The rest spreads
across the facts the lesson states but never works with — 60 Hz abroad against
50 Hz here, a steady supply having no frequency at all, why a generator gives
an alternating pd in the first place — and the misconceptions the lesson names:
a quoted mains value read as a peak, a y-gain confused with a time base, and a
period written down as though it were a frequency.
"""

TOPIC = "electricity"
SUBJECT = "physics"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-direct-alternating-pd-e05",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a direct current.",
        "options": [
            "A current that flows in both directions along a cable at once",
            "A current that always flows the same way round the circuit",
            "A current that reverses its direction at a steady rate of 50 Hz",
            "A current that flows straight from the live wire to the earth "
            "wire without passing through the appliance",
        ],
        "correct_index": 1,
        "why": "Direct current is charge flowing one way only, driven by a "
               "potential difference that never reverses.",
    },
    {
        "id": "ks4-direct-alternating-pd-e06",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The mains supply in the USA has a frequency of 60 Hz. State "
                "what this value tells you about that supply.",
        "options": [
            "It takes 60 seconds to work through one complete cycle, so one "
            "cycle lasts a whole minute",
            "It reverses its direction 60 times in every minute",
            "It completes 60 whole cycles in every second",
            "It supplies a potential difference of 60 volts",
        ],
        "correct_index": 2,
        "why": "Frequency is the number of complete cycles each second, so "
               "60 Hz means sixty cycles every second.",
    },
    {
        "id": "ks4-direct-alternating-pd-e07",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which one of these supplies an alternating potential "
                "difference?",
        "options": [
            "A 9 V battery inside a smoke alarm",
            "A solar cell on the back of a calculator, which reverses with "
            "the flicker of the room lights",
            "A laboratory dc power pack set to 6 V",
            "A socket on the classroom wall",
        ],
        "correct_index": 3,
        "why": "A wall socket carries mains electricity, which is generated as "
               "an alternating supply; the other three push charge one way "
               "only.",
    },
    {
        "id": "ks4-direct-alternating-pd-e08",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A signal generator is set to 200 Hz. Calculate the period "
                "of the supply it produces.",
        "options": ["0.020 s", "0.0050 s", "5.0 s", "0.20 s"],
        "correct_index": 1,
        "why": "T = 1 ÷ f = 1 ÷ 200 = 0.0050 s, which is 5.0 ms for one "
               "complete cycle.",
    },
    {
        "id": "ks4-direct-alternating-pd-e09",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The trace of an alternating supply reaches 3.0 vertical "
                "divisions above the zero line, with the y-gain set to 4.0 V "
                "per division. Calculate the peak potential difference.",
        "options": ["12 V", "1.3 V", "7.0 V", "0.75 V"],
        "correct_index": 0,
        "why": "Peak pd = divisions × volts per division = 3.0 × 4.0 = 12 V.",
    },
    {
        "id": "ks4-direct-alternating-pd-e10",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why mains electricity is produced as an alternating "
                "supply.",
        "options": [
            "A direct current would melt the wiring inside household "
            "appliances",
            "The generators turning in power stations produce an alternating "
            "potential difference",
            "Alternating current travels along a cable faster than direct "
            "current",
            "Current passes through an insulated cable only while it keeps "
            "reversing",
        ],
        "correct_index": 1,
        "why": "A coil turning in a magnetic field produces a potential "
               "difference that reverses on each half turn, so a generator "
               "gives ac without anything being done to it.",
    },
    {
        "id": "ks4-direct-alternating-pd-e11",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1.5 V cell is connected to an oscilloscope. State the "
                "frequency of the supply it provides.",
        "options": [
            "1.5 Hz, matching the potential difference of the cell",
            "50 Hz, because every supply used in the UK is made to alternate "
            "at the mains frequency",
            "0 Hz, because the potential difference never reverses",
            "It is too small a current for a frequency to exist",
        ],
        "correct_index": 2,
        "why": "A cell gives a steady pd in one direction, so there are no "
               "cycles to count and the frequency is zero.",
    },
    {
        "id": "ks4-direct-alternating-pd-e12",
        "subtopic_slug": "direct-alternating-pd",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the peak potential difference of an "
                "alternating supply.",
        "options": [
            "The largest potential difference it reaches, measured from the "
            "zero line",
            "The potential difference it holds for most of each complete "
            "cycle",
            "The difference between its largest and smallest potential "
            "differences",
            "The potential difference it reaches at the moment it is first "
            "switched on",
        ],
        "correct_index": 0,
        "why": "Peak pd is the maximum the supply swings to from zero, and "
               "for UK mains that is about 325 V rather than the quoted "
               "230 V.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-direct-alternating-pd-s05",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The frequency of an alternating supply is tripled and "
                "nothing else is changed. Describe the effect on its period.",
        "options": [
            "The period falls to one third of the value it had before",
            "The period rises to three times the value it had before",
            "The period falls to one ninth of the value it had before",
            "The period is unchanged, as it is fixed by the supply itself",
        ],
        "correct_index": 0,
        "why": "T = 1 ÷ f, so multiplying the frequency by three divides the "
               "time for one complete cycle by three.",
    },
    {
        "id": "ks4-direct-alternating-pd-s06",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 250 Hz alternating supply is displayed with the time base "
                "set to 1.0 ms per division. Determine how many horizontal "
                "divisions one complete cycle spans.",
        "options": [
            "4.0 divisions",
            "2.5 divisions",
            "250 divisions",
            "0.25 divisions",
        ],
        "correct_index": 0,
        "why": "T = 1 ÷ 250 = 0.0040 s = 4.0 ms, and each division is 1.0 ms, "
               "so one cycle covers 4.0 divisions.",
    },
    {
        "id": "ks4-direct-alternating-pd-s07",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An oscilloscope screen is 10 divisions wide and its time "
                "base is set to 10 ms per division. Determine how many "
                "complete cycles of a 40 Hz supply fit across the screen.",
        "options": ["10 cycles", "40 cycles", "4 cycles", "2.5 cycles"],
        "correct_index": 2,
        "why": "The screen covers 10 × 10 = 100 ms, and each cycle lasts "
               "1 ÷ 40 = 0.025 s = 25 ms, so 100 ÷ 25 = 4 cycles fit.",
    },
    {
        "id": "ks4-direct-alternating-pd-s08",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An oscilloscope displays a wave that rises 2.5 divisions "
                "above the centre line and falls the same 2.5 divisions "
                "below it, using a y-gain setting of 2.0 V per division. "
                "Determine the peak potential difference shown.",
        "options": ["5.0 V", "1.25 V", "10 V", "2.5 V"],
        "correct_index": 0,
        "why": "Peak pd is measured from the zero line to one peak, so it is "
               "2.5 × 2.0 = 5.0 V; 10 V would be the full crest-to-trough "
               "height.",
    },
    {
        "id": "ks4-direct-alternating-pd-s09",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dc power pack set to 9.0 V is connected to an oscilloscope "
                "whose y-gain is 3.0 V per division. Describe the trace that "
                "appears on the screen.",
        "options": [
            "A horizontal line sitting three divisions above the zero line",
            "A line that slopes steadily upwards across the whole screen as "
            "the pack charges up to 9.0 V",
            "A wave whose peaks rise three divisions above the zero line",
            "A horizontal line sitting nine divisions above the zero line",
        ],
        "correct_index": 0,
        "why": "The pd is steady, so the trace is flat, and 9.0 ÷ 3.0 = 3.0 "
               "divisions sets how far above zero the line sits.",
    },
    {
        "id": "ks4-direct-alternating-pd-s10",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The time base of an oscilloscope is changed from 5.0 ms per "
                "division to 10 ms per division while the same alternating "
                "supply stays connected. Describe how the trace changes.",
        "options": [
            "The frequency of the supply doubles, so each cycle carries twice "
            "the energy",
            "Twice as many complete cycles fit across the screen, and the "
            "height is unchanged",
            "Half as many complete cycles fit across the screen, and the "
            "height is halved",
            "The trace becomes twice as tall, and the number of cycles across "
            "it is unchanged, because the time base sets the height",
        ],
        "correct_index": 1,
        "why": "Each division now covers twice as long, so the screen holds "
               "twice the time and twice as many cycles; the vertical scale "
               "has not been touched.",
    },
    {
        "id": "ks4-direct-alternating-pd-s11",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil doubles the volts per division setting from 5.0 V to "
                "10 V while an alternating supply stays connected. Predict "
                "the effect on the height of the trace and on the number of "
                "cycles seen.",
        "options": [
            "The trace keeps its height, but each cycle now takes twice as "
            "long to complete",
            "The trace becomes twice as tall, because every division now "
            "covers a larger pd",
            "The trace becomes half as tall, and the number of cycles seen "
            "does not change",
            "The trace keeps its height, but half as many complete cycles "
            "now fit on the screen",
        ],
        "correct_index": 2,
        "why": "Each division now stands for twice the pd, so the same peak "
               "needs half as many divisions; the horizontal scale is set by "
               "the time base and is untouched.",
    },
    {
        "id": "ks4-direct-alternating-pd-s12",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The UK mains supply has a frequency of 50 Hz. Calculate the "
                "number of complete cycles it makes in 2.0 minutes.",
        "options": ["6000 cycles", "100 cycles", "3000 cycles", "120 cycles"],
        "correct_index": 0,
        "why": "2.0 minutes is 120 s, and 50 cycles happen each second, so "
               "50 × 120 = 6000 cycles.",
    },
    {
        "id": "ks4-direct-alternating-pd-s13",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alternating supply completes 750 whole cycles in 3.0 s. "
                "Calculate its frequency.",
        "options": ["750 Hz", "2250 Hz", "250 Hz", "0.0040 Hz"],
        "correct_index": 2,
        "why": "Frequency is cycles per second, so f = 750 ÷ 3.0 = 250 Hz.",
    },
    {
        "id": "ks4-direct-alternating-pd-s14",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rotating generator produces 80 complete cycles of output "
                "every 2.0 s. Work out the time period of one cycle.",
        "options": ["40 s", "0.050 s", "0.025 s", "2.5 s"],
        "correct_index": 2,
        "why": "f = 80 ÷ 2.0 = 40 Hz, so T = 1 ÷ 40 = 0.025 s for one cycle.",
    },
    {
        "id": "ks4-direct-alternating-pd-s15",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The UK mains supply alternates at 50 Hz and the mains supply "
                "in the USA alternates at 60 Hz. Determine which of the two "
                "has the shorter period, and why.",
        "options": [
            "The UK supply, because a lower frequency means each cycle takes "
            "less time",
            "The USA supply, because a higher frequency means each cycle "
            "takes less time",
            "The UK supply, because its larger potential difference pushes "
            "the charge round and shortens every cycle",
            "Neither, because the period of a supply does not depend on its "
            "frequency",
        ],
        "correct_index": 1,
        "why": "T = 1 ÷ f, so the 60 Hz supply has a period of about 0.017 s "
               "against the UK's 0.020 s.",
    },
    {
        "id": "ks4-direct-alternating-pd-s16",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a filament lamp connected to the mains lights "
                "normally even though the current in it keeps reversing.",
        "options": [
            "The lamp lights only during the half of each cycle when the "
            "charge flows the correct way through the filament",
            "The lamp holds a component that turns the alternating current "
            "into a direct one first",
            "The filament heats up whichever way the charge flows, so both "
            "halves of a cycle count",
            "The current reverses so slowly that the filament has time to "
            "cool and then reheat",
        ],
        "correct_index": 2,
        "why": "Heating does not depend on the direction of the charge flow, "
               "so energy is transferred to the filament throughout every "
               "cycle.",
    },
    {
        "id": "ks4-direct-alternating-pd-s17",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The trace of an alternating supply reaches 3.0 divisions "
                "above the zero line and the supply's peak potential "
                "difference is 15 V. Determine the y-gain setting.",
        "options": [
            "45 V per division",
            "15 V per division",
            "0.20 V per division",
            "5.0 V per division",
        ],
        "correct_index": 3,
        "why": "Peak pd = divisions × volts per division, so the setting is "
               "15 ÷ 3.0 = 5.0 V per division.",
    },
    {
        "id": "ks4-direct-alternating-pd-s18",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One complete cycle of a 400 Hz supply spans 5.0 horizontal "
                "divisions on an oscilloscope. Determine the time base "
                "setting.",
        "options": [
            "2.5 ms per division",
            "0.50 ms per division",
            "80 ms per division",
            "12.5 ms per division",
        ],
        "correct_index": 1,
        "why": "T = 1 ÷ 400 = 0.0025 s = 2.5 ms, spread over 5.0 divisions, "
               "so each division is 0.50 ms.",
    },
    {
        "id": "ks4-direct-alternating-pd-s19",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the output of a solar cell is described as a "
                "direct current.",
        "options": [
            "The cell is joined straight to the appliance, with no "
            "transformer in between",
            "The cell drives charge one way only, so its potential "
            "difference never reverses",
            "The cell's current reverses too slowly for an oscilloscope to "
            "show the change",
            "The cell sends its current directly to earth without first "
            "passing through the rest of the circuit",
        ],
        "correct_index": 1,
        "why": "Light falling on the cell pushes charge in a single "
               "direction, which is exactly what direct current means.",
    },
    {
        "id": "ks4-direct-alternating-pd-s20",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an oscilloscope is more useful than a voltmeter "
                "for investigating a mains supply.",
        "options": [
            "It reads in hertz rather than in volts, as no voltmeter can",
            "It turns the alternating supply into a steady direct one",
            "It shows how the potential difference changes with time, so the "
            "period can be read too",
            "It is the one instrument that connects safely to a socket",
        ],
        "correct_index": 2,
        "why": "The screen plots pd against time, so the period, the "
               "frequency and the peak pd can all be taken from one trace.",
    },
    {
        "id": "ks4-direct-alternating-pd-s21",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A signal generator is set to output 2.0 kHz. Work out the "
                "time taken for one complete cycle, giving your answer in "
                "milliseconds.",
        "options": ["2.0 ms", "500 ms", "0.50 ms", "0.0020 ms"],
        "correct_index": 2,
        "why": "2.0 kHz is 2000 Hz, so T = 1 ÷ 2000 = 0.00050 s, which is "
               "0.50 ms.",
    },
    {
        "id": "ks4-direct-alternating-pd-s22",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alternating supply has a period of 0.010 s. Calculate the "
                "number of complete cycles it makes in 0.25 s.",
        "options": ["25 cycles", "250 cycles", "2.5 cycles", "100 cycles"],
        "correct_index": 0,
        "why": "Each cycle lasts 0.010 s, so 0.25 ÷ 0.010 = 25 complete "
               "cycles.",
    },
    {
        "id": "ks4-direct-alternating-pd-s23",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how many more complete cycles a 60 Hz supply makes "
                "than a 50 Hz supply in one minute.",
        "options": ["10 cycles", "600 cycles", "60 cycles", "6000 cycles"],
        "correct_index": 1,
        "why": "In 60 s the supplies make 60 × 60 = 3600 and 50 × 60 = 3000 "
               "cycles, a difference of 600.",
    },
    {
        "id": "ks4-direct-alternating-pd-s24",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A signal generator is set to a frequency of 500 Hz. "
                "Calculate the time taken for 25 complete cycles.",
        "options": ["0.0020 s", "0.50 s", "20 s", "0.050 s"],
        "correct_index": 3,
        "why": "One cycle takes 1 ÷ 500 = 0.0020 s, so 25 cycles take "
               "25 × 0.0020 = 0.050 s.",
    },
    {
        "id": "ks4-direct-alternating-pd-s25",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how an oscilloscope is used to find the frequency "
                "of an unknown alternating supply.",
        "options": [
            "Count how many whole cycles appear across the screen and quote "
            "that number as the frequency",
            "Count the divisions in one whole cycle, multiply by the time "
            "base, then work out 1 ÷ period",
            "Measure the height of the trace in divisions, multiply by the "
            "volts per division, then divide by 1 s",
            "Take the time base setting, divide it by the divisions in one "
            "cycle, and quote that in hertz",
        ],
        "correct_index": 1,
        "why": "The width of one cycle in divisions times the time base gives "
               "the period, and the frequency is one divided by it.",
    },
    {
        "id": "ks4-direct-alternating-pd-s26",
        "subtopic_slug": "direct-alternating-pd",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A trace shows 2.5 complete cycles across a screen 10 "
                "divisions wide, with the time base at 4.0 ms per division. "
                "Calculate the frequency of the supply.",
        "options": ["25 Hz", "62.5 Hz", "160 Hz", "16 Hz"],
        "correct_index": 1,
        "why": "The screen covers 10 × 4.0 = 40 ms, so one cycle takes "
               "40 ÷ 2.5 = 16 ms = 0.016 s and f = 1 ÷ 0.016 = 62.5 Hz.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-direct-alternating-pd-h05",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mains supply in another country is quoted as 120 V and "
                "reaches a peak of 170 V, while UK mains is quoted as 230 V "
                "and peaks at 325 V. Compare what the two quoted values "
                "describe.",
        "options": [
            "Each quoted value is the effective value, roughly 1.4 times "
            "smaller than that supply's peak",
            "Each quoted value is the pd measured between the live wire and "
            "the earth wire of that supply",
            "The 120 V figure is an effective value, while the 230 V figure "
            "is the UK supply's peak pd",
            "Each quoted value is the average of the two peaks a supply "
            "reaches in opposite directions",
        ],
        "correct_index": 0,
        "why": "Both countries quote the steady pd that would transfer energy "
               "at the same rate as their alternating supply, and in each "
               "case the peak is about 1.4 times larger.",
    },
    {
        "id": "ks4-direct-alternating-pd-h06",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "For a sinusoidal supply the peak potential difference is "
                "about 1.4 times the quoted effective value. A laboratory ac "
                "supply is quoted as 12 V. Calculate its approximate peak "
                "potential difference.",
        "options": ["12 V", "8.6 V", "24 V", "17 V"],
        "correct_index": 3,
        "why": "Peak pd = 1.4 × 12 = 16.8 V, which is about 17 V.",
    },
    {
        "id": "ks4-direct-alternating-pd-h07",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil finds that one complete cycle spans 6.0 divisions "
                "with the time base at 5.0 ms per division, and writes down a "
                "frequency of 30 Hz. Determine the mistake made.",
        "options": [
            "They read the wrong axis; 6.0 divisions gives a peak pd of 30 V "
            "rather than a frequency",
            "They multiplied the divisions by the time base when the rule is "
            "to divide one by the other, giving 1.2 Hz",
            "They quoted the period of 30 ms as a frequency; the frequency is "
            "about 33 Hz",
            "They forgot to double the period before dividing, so the answer "
            "should be about 17 Hz",
        ],
        "correct_index": 2,
        "why": "6.0 × 5.0 = 30 ms is the period, so f = 1 ÷ 0.030 = 33 Hz to "
               "two significant figures.",
    },
    {
        "id": "ks4-direct-alternating-pd-h08",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Supply P has a period of 4.0 ms. Supply Q completes 500 "
                "whole cycles in 2.0 s. Compare the frequencies of the two "
                "supplies.",
        "options": [
            "P has a frequency of 4.0 Hz and Q has a frequency of 250 Hz",
            "P has twice the frequency of Q, since its period is quoted in "
            "milliseconds",
            "P has a frequency of 250 Hz and Q has a frequency of 500 Hz",
            "Both supplies have the same frequency, 250 Hz",
        ],
        "correct_index": 3,
        "why": "P: f = 1 ÷ 0.0040 = 250 Hz. Q: f = 500 ÷ 2.0 = 250 Hz, so the "
               "two are equal.",
    },
    {
        "id": "ks4-direct-alternating-pd-h09",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An oscilloscope screen is 8.0 divisions wide. Determine the "
                "smallest time base setting that still shows at least four "
                "complete cycles of a 100 Hz supply.",
        "options": [
            "1.25 ms per division",
            "5.0 ms per division",
            "40 ms per division",
            "2.5 ms per division",
        ],
        "correct_index": 1,
        "why": "One cycle lasts 1 ÷ 100 = 10 ms, so four cycles need 40 ms "
               "across 8.0 divisions, which is 5.0 ms per division.",
    },
    {
        "id": "ks4-direct-alternating-pd-h10",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A solar panel on a roof produces a direct current. Suggest "
                "why its output must be changed before it can be supplied to "
                "the national grid.",
        "options": [
            "A direct current cannot travel more than a few hundred metres "
            "along a cable",
            "The panel's direct current would flow back into the power "
            "station and damage it",
            "The grid carries an alternating potential difference at 50 Hz, "
            "so the output must alternate",
            "The grid carries a direct current at a far higher frequency "
            "than a panel can reach",
        ],
        "correct_index": 2,
        "why": "Everything joined to the grid must alternate in step with it "
               "at 50 Hz, so the panel's steady dc output has to be converted "
               "into ac first.",
    },
    {
        "id": "ks4-direct-alternating-pd-h11",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a transformer cannot be used to raise the "
                "potential difference of a 12 V car battery.",
        "options": [
            "A transformer works only above a certain potential difference, "
            "and 12 V is well below the value it needs",
            "A transformer needs a potential difference that keeps changing, "
            "and a battery's is steady",
            "A car battery drives too large a current for the coils of a "
            "transformer to carry safely",
            "A transformer is able to lower a potential difference, so it "
            "could never raise one",
        ],
        "correct_index": 1,
        "why": "A transformer depends on a continually changing pd, which "
               "only an alternating supply provides; a battery's pd does not "
               "change.",
    },
    {
        "id": "ks4-direct-alternating-pd-h12",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil says that a trace which stays above the zero line at "
                "all times must come from a supply whose potential difference "
                "is constant. Evaluate this statement.",
        "options": [
            "Correct, because a trace drawn above the zero line can come only "
            "from a steady supply",
            "Incorrect, because a trace above the zero line shows the average "
            "pd of an alternating supply",
            "Incorrect, because the pd stays in one direction but could still "
            "be changing in size",
            "Incorrect, because a trace drawn above the zero line must be an "
            "alternating one shifted upwards",
        ],
        "correct_index": 2,
        "why": "Staying above zero shows only that the pd never reverses; a "
               "direct supply can still rise and fall in size.",
    },
    {
        "id": "ks4-direct-alternating-pd-h13",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three complete cycles of an alternating supply span 12 "
                "divisions, with the time base set to 0.50 ms per division. "
                "Calculate the frequency of the supply.",
        "options": ["167 Hz", "1500 Hz", "500 Hz", "2.0 Hz"],
        "correct_index": 2,
        "why": "12 × 0.50 = 6.0 ms holds three cycles, so T = 2.0 ms and "
               "f = 1 ÷ 0.0020 = 500 Hz.",
    },
    {
        "id": "ks4-direct-alternating-pd-h14",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alternating supply has a peak potential difference of "
                "48 V. Its trace must not rise more than 4.0 divisions above "
                "the zero line. Determine the smallest y-gain setting that "
                "can be used.",
        "options": [
            "6.0 V per division",
            "192 V per division",
            "0.083 V per division",
            "12 V per division",
        ],
        "correct_index": 3,
        "why": "48 ÷ 4.0 = 12 V per division; anything smaller would push the "
               "peak past four divisions and off the screen.",
    },
    {
        "id": "ks4-direct-alternating-pd-h15",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lamp is connected first to a 9.0 V dc supply and then to "
                "an alternating supply whose effective value is 9.0 V. "
                "Compare the energy transferred to the lamp each second.",
        "options": [
            "More on the alternating supply, because its pd climbs above "
            "9.0 V at each peak",
            "The same, because the effective value is the steady pd that "
            "would transfer energy at that rate",
            "Less on the alternating supply, because half of every cycle "
            "drives the charge the wrong way",
            "More on the direct supply, because a steady current transfers "
            "energy faster than a reversing one",
        ],
        "correct_index": 1,
        "why": "An effective value is defined by equal energy transfer, so a "
               "9.0 V effective ac supply and a 9.0 V dc supply light the "
               "lamp identically.",
    },
    {
        "id": "ks4-direct-alternating-pd-h16",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The potential difference of an alternating supply averages "
                "zero over a complete cycle. Explain why the supply still "
                "transfers energy to a heater.",
        "options": [
            "The heater keeps the energy from the first half of each cycle "
            "and gives it out in the second",
            "The average is zero only on paper; across a real circuit the pd "
            "stays positive the whole time",
            "The supply reaches the heater through a component that removes "
            "the negative half of each cycle",
            "Energy is transferred whichever way the charge is pushed, so the "
            "two halves add rather than cancel",
        ],
        "correct_index": 3,
        "why": "Heating depends on charge flowing, not on which way it flows, "
               "so both halves of every cycle warm the element.",
    },
    {
        "id": "ks4-direct-alternating-pd-h17",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The frequency of a supply is doubled and, at the same time, "
                "the time base setting is doubled. Predict how the trace on "
                "the screen changes.",
        "options": [
            "It looks the same as before, because each cycle halves while "
            "each division doubles",
            "Four times as many complete cycles now fit across the width of "
            "the screen",
            "The trace becomes twice as tall, because doubling the frequency "
            "doubles the peak pd",
            "The trace flattens into a horizontal line, because the two "
            "changes cancel the oscillation",
        ],
        "correct_index": 0,
        "why": "Doubling f halves the period, and doubling the time base "
               "doubles the time each division represents, so a cycle still "
               "covers the same number of divisions.",
    },
    {
        "id": "ks4-direct-alternating-pd-h18",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An oscilloscope trace initially shows 4 complete cycles "
                "spread across a 10-division-wide screen, with the time "
                "base set to 2.0 ms per division. The supply's frequency "
                "is then halved while the time base stays the same. Work "
                "out how many complete cycles now appear across the "
                "screen.",
        "options": ["4 cycles", "8 cycles", "1 cycle", "2 cycles"],
        "correct_index": 3,
        "why": "The screen covers 20 ms, so each of the 4 cycles lasted 5.0 "
               "ms; halving the frequency doubles the period to 10 ms, and "
               "20 ÷ 10 = 2 cycles.",
    },
    {
        "id": "ks4-direct-alternating-pd-h19",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The frequency of a signal generator is increased from 100 Hz "
                "to 400 Hz. Calculate the change in the period of the supply.",
        "options": [
            "A decrease of 7.5 ms",
            "An increase of 7.5 ms",
            "A decrease of 2.5 ms",
            "A decrease of 300 ms",
        ],
        "correct_index": 0,
        "why": "T falls from 1 ÷ 100 = 10 ms to 1 ÷ 400 = 2.5 ms, a decrease "
               "of 7.5 ms.",
    },
    {
        "id": "ks4-direct-alternating-pd-h20",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a supply with a higher frequency "
                "must also have a higher peak potential difference.",
        "options": [
            "Correct, because more cycles each second lifts the peak pd",
            "Incorrect, because the peak pd is read up the screen and the "
            "frequency across it, separately",
            "Correct, because peak pd and frequency rise in proportion",
            "Incorrect, because a shorter cycle gives a lower peak pd",
        ],
        "correct_index": 1,
        "why": "Frequency is how often the pd cycles and peak pd is how far "
               "it swings; a signal generator can change either one without "
               "the other.",
    },
    {
        "id": "ks4-direct-alternating-pd-h21",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An appliance designed for a 120 V, 60 Hz mains supply is "
                "plugged into UK mains. Suggest why it may be damaged.",
        "options": [
            "UK mains supplies a direct current, which the appliance's motor "
            "cannot turn on",
            "UK mains reverses direction, while a 120 V supply pushes charge "
            "one way only",
            "UK mains has the higher frequency, so the appliance is given "
            "more cycles each second",
            "UK mains supplies roughly twice the potential difference, so a "
            "far larger current flows",
        ],
        "correct_index": 3,
        "why": "230 V is close to double 120 V, so the current through the "
               "appliance is about twice as large and it heats far more than "
               "it was built for.",
    },
    {
        "id": "ks4-direct-alternating-pd-h22",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil measures the time for 10 complete cycles of an "
                "alternating supply as 0.25 s. Calculate the frequency of "
                "the supply.",
        "options": ["40 Hz", "0.025 Hz", "10 Hz", "2.5 Hz"],
        "correct_index": 0,
        "why": "One cycle takes 0.25 ÷ 10 = 0.025 s, so f = 1 ÷ 0.025 = "
               "40 Hz.",
    },
    {
        "id": "ks4-direct-alternating-pd-h23",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An oscilloscope displays a supply whose period is 0.0025 s. "
                "Determine whether this supply could be UK mains.",
        "options": [
            "Yes, because that period works out as 50 Hz",
            "No, because that period gives a frequency of 2500 Hz",
            "Yes, because every mains supply has this same period",
            "No, because that period gives a frequency of 400 Hz, while UK "
            "mains runs at 50 Hz",
        ],
        "correct_index": 3,
        "why": "f = 1 ÷ 0.0025 = 400 Hz, eight times the 50 Hz of the UK "
               "mains supply.",
    },
    {
        "id": "ks4-direct-alternating-pd-h24",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the period of a 5.0 kHz signal with the period of a "
                "100 Hz supply.",
        "options": [
            "The 5.0 kHz signal has a period 50 times longer than the 100 Hz "
            "supply",
            "The 100 Hz supply has a period 500 times longer than the 5.0 kHz "
            "signal",
            "The 100 Hz supply has a period 50 times longer than the 5.0 kHz "
            "signal",
            "Both have the same period, because period is fixed and does not "
            "follow frequency",
        ],
        "correct_index": 2,
        "why": "T = 1 ÷ 5000 = 0.20 ms and T = 1 ÷ 100 = 10 ms, and 10 ÷ 0.20 "
               "= 50.",
    },
    {
        "id": "ks4-direct-alternating-pd-h25",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why changing the y-gain of an oscilloscope does not "
                "change the frequency worked out from its trace.",
        "options": [
            "The y-gain stretches the height and the width of the trace by "
            "the same factor each time",
            "The frequency is fixed by the oscilloscope itself rather than by "
            "the supply connected to it",
            "Changing the y-gain changes the peak pd of the supply but leaves "
            "its period untouched",
            "The frequency comes from the time for one cycle, read across the "
            "screen using the time base",
        ],
        "correct_index": 3,
        "why": "The y-gain only sets how many volts a vertical division "
               "stands for; the period is measured horizontally and is "
               "unaffected.",
    },
    {
        "id": "ks4-direct-alternating-pd-h26",
        "subtopic_slug": "direct-alternating-pd",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One complete cycle of a 20 Hz supply fills the whole width "
                "of a screen that is 10 divisions wide. Determine the time "
                "base setting.",
        "options": [
            "0.50 ms per division",
            "50 ms per division",
            "5.0 ms per division",
            "2.0 ms per division",
        ],
        "correct_index": 2,
        "why": "T = 1 ÷ 20 = 0.050 s = 50 ms, spread across 10 divisions, so "
               "each division is 5.0 ms.",
    },
]
