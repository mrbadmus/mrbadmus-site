# Rates & Equilibrium unit — content review (MRB-105)

_AQA 5.6 Rate and Extent of Chemical Change. Drafted for Mide's review before the Phase 2 merge. Every question, its options (✔︎ = correct), and a diagnostic line for each wrong option are shown here — you never need to read the Python._

## How the tiers work (the difficulty model you set)

- **Difficulty follows the tier, not the pathway.** Combined-Foundation and Triple-Foundation are the **same difficulty**; Combined-Higher and Triple-Higher both **scale up** to genuine Higher demand (unit conversions, gradients from graphs, Le Chatelier reasoning).
- **Triple's extra is coverage, not a harder version of the same content.** Triple-Foundation = the exact Combined-Foundation set **+ 2 extra Foundation-level questions**; Triple-Higher = the exact Combined-Higher set **+ 2 extra Higher/depth questions**. Foundation students see the same difficulty on both pathways; Triple students simply get more. (Rate & equilibrium has **no AQA Triple-only content**, so the extra is always same-difficulty coverage.)
- **Every stem is exam-register** (uses an AQA command word) and **every wrong option carries a diagnostic** naming the misconception or error.
- **FIFA (Formula → Insert → Fine-tune → Answer)** appears on **one page only — `calculating-rates`** — the single page with a real calculation. Foundation FIFA reads a mean rate off given values; Higher FIFA adds unit conversions (min→s, dm³→cm³) and gradient-of-a-tangent. The descriptive pages carry no FIFA by design.
- **Counts:** Combined 10 / tier, Triple 12 / tier (10 + 2 extra). `effect-of-conditions-equilibrium` (Le Chatelier) is **Higher-only** — no Foundation cell.

### ⭐ Full-review checklist (per the review-tiering rule)

All calculation items and all FIFA are flagged ⭐ for your full review; recall/comprehension items are left for your sampling. The ⭐ items are:

- **Rate of Reaction and Calculations** — 6 calculation item(s), FIFA worked examples (Foundation ×3 + Higher ×3)

### Audit status (self-checked with `audit_content.py`)

- **Before:** every rate/equilibrium page carried only **2 questions** per tier variant, identical across Foundation/Higher and across Combined/Triple. That is **22 count-criticals** (2 < the floor of 5), plus **5 tier-integrity majors** (Higher = Foundation), **5 triple-depth majors** (Triple = Combined), and **mistake-first majors** on every Common Mistake (all opened with correct info, not a named mistake).
- **After:** **zero critical, zero content majors.** The only remaining flags are: **(a)** the systemic `no interactive practice mode` **major** on `calculating-rates` (all four cells) — the current template renders static FIFA steps only, which is the redesign port's job (**MRB-113**), **not** a content defect; and **(b)** 6 `info` notes on `reversible-reactions-equilibrium` and `effect-of-conditions-equilibrium` (they keep their reaction equations but carry no FIFA — expected, since neither page has a calculation).

---

## Rate of Reaction and Calculations  ·  `calculating-rates`  ·  AQA 5.6.1.1

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.6.1.1 is shared content: Combined and Triple both cover calculating rates. There is no Triple-only rate content, so Triple = the exact Combined set + 2 extra same-difficulty questions per tier.

**Common Mistake (mistake-first, three-beat):**

> Students often think the rate of a reaction stays the same from start to finish. It does not: as the reactants are used up there are fewer reactant particles, so fewer collisions happen each second and the rate falls. On a volume–time graph this is why the line is steepest at the very start (fastest rate) and gradually becomes less steep, going flat only when the reaction has finished and a reactant has run out.

**FIFA worked examples — Foundation (Combined + Triple)** (⭐ full review):

- **Mean rate from gas volume** — A reaction between calcium carbonate and hydrochloric acid gives off 84 cm³ of carbon dioxide in 60 s. Calculate the mean rate of reaction.
    - *F* Rate = quantity of gas ÷ time  *I* Rate = 84 cm³ ÷ 60 s  *F* Rate = 1.4  *A* Rate = 1.4 cm³/s
- **Mean rate from mass loss** — A flask of reacting acid and marble chips loses 4 g of mass in 50 s as CO₂ escapes. Calculate the mean rate of reaction.
    - *F* Rate = mass lost ÷ time  *I* Rate = 4 g ÷ 50 s  *F* Rate = 0.08  *A* Rate = 0.08 g/s
- **Mean rate in cm³/min** — A reaction collects 150 cm³ of hydrogen in 5 minutes. Calculate the mean rate of reaction in cm³/min.
    - *F* Rate = volume of gas ÷ time  *I* Rate = 150 cm³ ÷ 5 min  *F* Rate = 30  *A* Rate = 30 cm³/min

**FIFA worked examples — Higher (Combined + Triple)** (⭐ full review):

- **Convert the time unit first** — A gas syringe collects 72 cm³ of gas in 1.5 minutes. Calculate the mean rate of reaction in cm³/s.
    - *F* Rate = volume ÷ time, with time in seconds  *I* Time = 1.5 × 60 = 90 s, so Rate = 72 cm³ ÷ 90 s  *F* Rate = 0.8  *A* Rate = 0.8 cm³/s
- **Convert the volume unit first** — A reaction collects 0.048 dm³ of gas in 40 s. Calculate the mean rate of reaction in cm³/s.
    - *F* Rate = volume ÷ time, with volume in cm³  *I* Volume = 0.048 × 1000 = 48 cm³, so Rate = 48 cm³ ÷ 40 s  *F* Rate = 1.2  *A* Rate = 1.2 cm³/s
- **Instantaneous rate from a tangent** — A tangent drawn to a volume–time curve at t = 20 s passes through the points (10 s, 12 cm³) and (30 s, 54 cm³). Calculate the instantaneous rate at 20 s.
    - *F* Rate = gradient of tangent = change in volume ÷ change in time  *I* Rate = (54 − 12) ÷ (30 − 10) = 42 ÷ 20  *F* Rate = 2.1  *A* Rate = 2.1 cm³/s

**Question sets by tier** (each item shows the tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (3 recall / 7 apply+reason+calc)

**Q1. [calc · CFCHTFTH ⭐]** A gas syringe collects 48 cm³ of gas in 60 s. Calculate the mean rate of reaction.
- [✔︎] 0.8 cm³/s — rate = 48 ÷ 60
- [ ] 2880 cm³/s — rate = 48 × 60
    - *why wrong:* This multiplies the volume by the time. Mean rate = quantity ÷ time, so you divide.
- [ ] 1.25 cm³/s — rate = 60 ÷ 48
    - *why wrong:* This divides time by volume — the wrong way round. Rate = volume ÷ time = 48 ÷ 60.
- [ ] 48 cm³/s — the volume of gas collected
    - *why wrong:* This just reads off the volume and ignores the time. Rate must be a quantity per second.

**Q2. [apply · CFCHTFTH]** On a graph of gas volume against time, describe what a steeper part of the curve tells you about the reaction.
- [✔︎] The reaction is faster there — more gas is being produced each second
- [ ] The reaction is slower there — a steep line means it is struggling
    - *why wrong:* A steeper gradient means MORE volume per second, which is a faster rate, not slower.
- [ ] The reaction has finished — no more gas is being made
    - *why wrong:* A FLAT (horizontal) line means the reaction has finished; a steep line means it is going quickly.
- [ ] More gas has been collected in total, but the rate is unchanged
    - *why wrong:* The steepness (gradient) represents the RATE, not the total amount collected.

**Q3. [reason · CFCHTFTH]** Explain why the curve on a volume–time graph becomes less steep and eventually flattens as the reaction proceeds.
- [✔︎] The reactants are being used up, so there are fewer collisions each second (slower rate); flat means the reaction has finished
- [ ] More product keeps forming, which speeds the reaction up over time
    - *why wrong:* The rate DECREASES over time as reactants run out — the line gets less steep, not steeper.
- [ ] The reaction runs out of time, so it is forced to slow down
    - *why wrong:* Time does not limit the rate; the falling rate is caused by reactant particles being used up.
- [ ] The temperature drops as the reaction goes on, flattening the line
    - *why wrong:* The slowing is due to reactants being used up (fewer collisions), not a temperature change.

**Q4. [apply · CFCHTFTH]** Describe two things you could measure over time to follow the rate of the reaction between marble chips and hydrochloric acid.
- [✔︎] The volume of carbon dioxide gas given off, or the loss in mass of the flask
- [ ] The colour of the acid and the temperature of the room
    - *why wrong:* The acid stays colourless and room temperature is not a product — neither tracks how fast CO₂ forms.
- [ ] The mass of the marble chips only, weighed once at the end
    - *why wrong:* A single end measurement gives no rate — you must record how a quantity changes over TIME.
- [ ] The volume of the acid and the volume of the flask
    - *why wrong:* These do not change as the reaction proceeds, so they cannot measure the rate.

**Q5. [calc · CFCHTFTH ⭐]** A reaction flask loses 6 g of mass in 120 s as gas escapes. Calculate the mean rate of reaction in g/s.
- [✔︎] 0.05 g/s — rate = 6 ÷ 120
- [ ] 20 g/s — rate = 120 ÷ 6
    - *why wrong:* This divides time by mass — the wrong way round. Rate = mass lost ÷ time = 6 ÷ 120.
- [ ] 720 g/s — rate = 6 × 120
    - *why wrong:* This multiplies instead of dividing. Mean rate = quantity ÷ time.
- [ ] 0.5 g/s — rate = 6 ÷ 12
    - *why wrong:* The time is 120 s, not 12 s. Rate = 6 ÷ 120 = 0.05 g/s.

**Q6. [recall · CFTF]** State what is meant by the 'rate' of a chemical reaction.
- [✔︎] How quickly reactants are used up or products are formed
- [ ] How much product is made in total by the end
    - *why wrong:* That is the total yield, not the rate. Rate is about how QUICKLY, per unit time.
- [ ] How much energy is released by the reaction
    - *why wrong:* That is the energy change, not the rate. Rate measures speed, not energy.
- [ ] Whether the reaction is reversible or not
    - *why wrong:* That describes the reaction type, not how fast it goes.

**Q7. [recall · CFTF]** State the two quantities you divide to calculate the mean rate of a reaction.
- [✔︎] The quantity of reactant used or product formed, divided by the time taken
- [ ] The mass of reactant divided by the mass of product
    - *why wrong:* Rate compares an amount with TIME, not one mass with another.
- [ ] The volume of gas multiplied by the time taken
    - *why wrong:* Rate is quantity ÷ time (a division), not a multiplication.
- [ ] The temperature rise divided by the concentration
    - *why wrong:* Neither of these is used to calculate rate; rate = quantity ÷ time.

**Q8. [recall · CFTF]** Give a suitable unit for the rate of a reaction in which the gas produced is collected in a syringe.
- [✔︎] cm³/s (cubic centimetres per second)
- [ ] cm³ (cubic centimetres)
    - *why wrong:* cm³ is a volume, not a rate. A rate needs a quantity PER unit of time, e.g. cm³/s.
- [ ] s (seconds)
    - *why wrong:* Seconds is a time, not a rate. The unit must combine the gas volume with time.
- [ ] g/cm³ (grams per cubic centimetre)
    - *why wrong:* That is a density. For gas volume over time the unit is cm³/s.

**Q9. [apply · CFTF]** A volume–time graph becomes flat (horizontal). State what this tells you about the reactants.
- [✔︎] At least one reactant has been completely used up, so the reaction has stopped
- [ ] The reactants are reacting as fast as possible
    - *why wrong:* The fastest rate is the STEEPEST part (the start); a flat line means the reaction has stopped.
- [ ] The reactants have just been added to the flask
    - *why wrong:* Adding reactants would start a steep rise, not a flat line.
- [ ] The temperature has reached its highest point
    - *why wrong:* A flat line shows no more product is forming — a reactant has run out, not a temperature peak.

**Q10. [apply · CFTF]** Identify which of these is the slowest reaction.
- [✔︎] The rusting of an iron gate over several months
- [ ] A firework exploding
    - *why wrong:* An explosion is one of the FASTEST reactions — over in a fraction of a second.
- [ ] Magnesium ribbon burning in air
    - *why wrong:* Burning magnesium is a fast reaction, giving out light and heat quickly.
- [ ] An indigestion tablet fizzing in water
    - *why wrong:* Fizzing happens in seconds — much faster than rusting, which takes months.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [calc · CFCHTFTH ⭐]** A gas syringe collects 48 cm³ of gas in 60 s. Calculate the mean rate of reaction.
- [✔︎] 0.8 cm³/s — rate = 48 ÷ 60
- [ ] 2880 cm³/s — rate = 48 × 60
    - *why wrong:* This multiplies the volume by the time. Mean rate = quantity ÷ time, so you divide.
- [ ] 1.25 cm³/s — rate = 60 ÷ 48
    - *why wrong:* This divides time by volume — the wrong way round. Rate = volume ÷ time = 48 ÷ 60.
- [ ] 48 cm³/s — the volume of gas collected
    - *why wrong:* This just reads off the volume and ignores the time. Rate must be a quantity per second.

**Q2. [apply · CFCHTFTH]** On a graph of gas volume against time, describe what a steeper part of the curve tells you about the reaction.
- [✔︎] The reaction is faster there — more gas is being produced each second
- [ ] The reaction is slower there — a steep line means it is struggling
    - *why wrong:* A steeper gradient means MORE volume per second, which is a faster rate, not slower.
- [ ] The reaction has finished — no more gas is being made
    - *why wrong:* A FLAT (horizontal) line means the reaction has finished; a steep line means it is going quickly.
- [ ] More gas has been collected in total, but the rate is unchanged
    - *why wrong:* The steepness (gradient) represents the RATE, not the total amount collected.

**Q3. [reason · CFCHTFTH]** Explain why the curve on a volume–time graph becomes less steep and eventually flattens as the reaction proceeds.
- [✔︎] The reactants are being used up, so there are fewer collisions each second (slower rate); flat means the reaction has finished
- [ ] More product keeps forming, which speeds the reaction up over time
    - *why wrong:* The rate DECREASES over time as reactants run out — the line gets less steep, not steeper.
- [ ] The reaction runs out of time, so it is forced to slow down
    - *why wrong:* Time does not limit the rate; the falling rate is caused by reactant particles being used up.
- [ ] The temperature drops as the reaction goes on, flattening the line
    - *why wrong:* The slowing is due to reactants being used up (fewer collisions), not a temperature change.

**Q4. [apply · CFCHTFTH]** Describe two things you could measure over time to follow the rate of the reaction between marble chips and hydrochloric acid.
- [✔︎] The volume of carbon dioxide gas given off, or the loss in mass of the flask
- [ ] The colour of the acid and the temperature of the room
    - *why wrong:* The acid stays colourless and room temperature is not a product — neither tracks how fast CO₂ forms.
- [ ] The mass of the marble chips only, weighed once at the end
    - *why wrong:* A single end measurement gives no rate — you must record how a quantity changes over TIME.
- [ ] The volume of the acid and the volume of the flask
    - *why wrong:* These do not change as the reaction proceeds, so they cannot measure the rate.

**Q5. [calc · CFCHTFTH ⭐]** A reaction flask loses 6 g of mass in 120 s as gas escapes. Calculate the mean rate of reaction in g/s.
- [✔︎] 0.05 g/s — rate = 6 ÷ 120
- [ ] 20 g/s — rate = 120 ÷ 6
    - *why wrong:* This divides time by mass — the wrong way round. Rate = mass lost ÷ time = 6 ÷ 120.
- [ ] 720 g/s — rate = 6 × 120
    - *why wrong:* This multiplies instead of dividing. Mean rate = quantity ÷ time.
- [ ] 0.5 g/s — rate = 6 ÷ 12
    - *why wrong:* The time is 120 s, not 12 s. Rate = 6 ÷ 120 = 0.05 g/s.

**Q6. [calc · CHTH ⭐]** A gas syringe collects 72 cm³ of gas in 1.5 minutes. Calculate the mean rate of reaction in cm³/s.
- [✔︎] 0.8 cm³/s — time = 1.5 × 60 = 90 s, so rate = 72 ÷ 90
- [ ] 48 cm³/s — rate = 72 ÷ 1.5
    - *why wrong:* The time was left in minutes. For cm³/s you must convert: 1.5 min = 90 s, then 72 ÷ 90 = 0.8.
- [ ] 108 cm³/s — rate = 72 × 1.5
    - *why wrong:* This multiplies instead of dividing, and does not convert the time to seconds.
- [ ] 1.25 cm³/s — rate = 90 ÷ 72
    - *why wrong:* This divides time by volume — the wrong way round. Rate = volume ÷ time = 72 ÷ 90.

**Q7. [reason · CHTH]** Explain how you would find the rate of reaction at exactly 30 s from a curved volume–time graph.
- [✔︎] Draw a tangent to the curve at 30 s and calculate its gradient (change in volume ÷ change in time)
- [ ] Read the volume at 30 s and divide it by 30
    - *why wrong:* That gives the MEAN rate up to 30 s, not the instantaneous rate at 30 s — you need a tangent.
- [ ] Measure the gradient of a straight line from the start to the end of the curve
    - *why wrong:* That is the overall mean rate, not the rate at one instant. Draw a tangent at 30 s instead.
- [ ] Read the volume at 30 s straight off the graph
    - *why wrong:* The volume at 30 s is an amount, not a rate. The rate is the gradient of the tangent there.

**Q8. [calc · CHTH ⭐]** A tangent drawn to a volume–time curve at t = 20 s rises from 12 cm³ (at 10 s) to 54 cm³ (at 30 s). Calculate the instantaneous rate at 20 s.
- [✔︎] 2.1 cm³/s — gradient = (54 − 12) ÷ (30 − 10) = 42 ÷ 20
- [ ] 1.8 cm³/s — gradient = 54 ÷ 30
    - *why wrong:* This uses one point instead of the change between two points. Gradient = Δvolume ÷ Δtime = 42 ÷ 20.
- [ ] 42 cm³/s — the change in volume
    - *why wrong:* 42 cm³ is the rise (Δvolume); you must divide it by the time interval (20 s) to get the rate.
- [ ] 0.48 cm³/s — gradient = 20 ÷ 42
    - *why wrong:* This divides Δtime by Δvolume — the wrong way round. Gradient = Δvolume ÷ Δtime.

**Q9. [reason · CHTH]** Explain why the instantaneous rate at the very start of a reaction is greater than the mean rate over the whole reaction.
- [✔︎] The reaction is fastest at the start (steepest gradient) and slows as reactants are used up, so the average over the whole reaction is lower
- [ ] The mean rate ignores the products, so it is always smaller
    - *why wrong:* The mean rate does account for product formed; it is smaller because the rate falls over time.
- [ ] The instantaneous rate is measured in different units, making it larger
    - *why wrong:* Both are measured in the same units (e.g. cm³/s); the difference is real, not a unit effect.
- [ ] The start of the reaction has the most product, so it is fastest
    - *why wrong:* The start has the most REACTANT (and least product); plenty of reactant is why it is fastest.

**Q10. [apply · CHTH]** A table shows the gas volume every 10 s; the increase in each 10 s interval gets smaller as the reaction proceeds. Explain what this pattern shows about the rate.
- [✔︎] The rate is decreasing over time, because reactant particles are being used up so there are fewer successful collisions each second
- [ ] The rate is constant, because gas is still being produced
    - *why wrong:* Gas is still produced, but LESS each interval — that is a falling rate, not a constant one.
- [ ] The rate is increasing, because the total volume keeps rising
    - *why wrong:* The total rises, but by smaller amounts each time, so the rate is falling, not rising.
- [ ] The reaction has already finished at the first interval
    - *why wrong:* It cannot have finished — gas is still being produced in every interval, just more slowly.

### Triple Foundation — 12 questions (3 recall / 9 apply+reason+calc)

**Q1. [calc · CFCHTFTH ⭐]** A gas syringe collects 48 cm³ of gas in 60 s. Calculate the mean rate of reaction.
- [✔︎] 0.8 cm³/s — rate = 48 ÷ 60
- [ ] 2880 cm³/s — rate = 48 × 60
    - *why wrong:* This multiplies the volume by the time. Mean rate = quantity ÷ time, so you divide.
- [ ] 1.25 cm³/s — rate = 60 ÷ 48
    - *why wrong:* This divides time by volume — the wrong way round. Rate = volume ÷ time = 48 ÷ 60.
- [ ] 48 cm³/s — the volume of gas collected
    - *why wrong:* This just reads off the volume and ignores the time. Rate must be a quantity per second.

**Q2. [apply · CFCHTFTH]** On a graph of gas volume against time, describe what a steeper part of the curve tells you about the reaction.
- [✔︎] The reaction is faster there — more gas is being produced each second
- [ ] The reaction is slower there — a steep line means it is struggling
    - *why wrong:* A steeper gradient means MORE volume per second, which is a faster rate, not slower.
- [ ] The reaction has finished — no more gas is being made
    - *why wrong:* A FLAT (horizontal) line means the reaction has finished; a steep line means it is going quickly.
- [ ] More gas has been collected in total, but the rate is unchanged
    - *why wrong:* The steepness (gradient) represents the RATE, not the total amount collected.

**Q3. [reason · CFCHTFTH]** Explain why the curve on a volume–time graph becomes less steep and eventually flattens as the reaction proceeds.
- [✔︎] The reactants are being used up, so there are fewer collisions each second (slower rate); flat means the reaction has finished
- [ ] More product keeps forming, which speeds the reaction up over time
    - *why wrong:* The rate DECREASES over time as reactants run out — the line gets less steep, not steeper.
- [ ] The reaction runs out of time, so it is forced to slow down
    - *why wrong:* Time does not limit the rate; the falling rate is caused by reactant particles being used up.
- [ ] The temperature drops as the reaction goes on, flattening the line
    - *why wrong:* The slowing is due to reactants being used up (fewer collisions), not a temperature change.

**Q4. [apply · CFCHTFTH]** Describe two things you could measure over time to follow the rate of the reaction between marble chips and hydrochloric acid.
- [✔︎] The volume of carbon dioxide gas given off, or the loss in mass of the flask
- [ ] The colour of the acid and the temperature of the room
    - *why wrong:* The acid stays colourless and room temperature is not a product — neither tracks how fast CO₂ forms.
- [ ] The mass of the marble chips only, weighed once at the end
    - *why wrong:* A single end measurement gives no rate — you must record how a quantity changes over TIME.
- [ ] The volume of the acid and the volume of the flask
    - *why wrong:* These do not change as the reaction proceeds, so they cannot measure the rate.

**Q5. [calc · CFCHTFTH ⭐]** A reaction flask loses 6 g of mass in 120 s as gas escapes. Calculate the mean rate of reaction in g/s.
- [✔︎] 0.05 g/s — rate = 6 ÷ 120
- [ ] 20 g/s — rate = 120 ÷ 6
    - *why wrong:* This divides time by mass — the wrong way round. Rate = mass lost ÷ time = 6 ÷ 120.
- [ ] 720 g/s — rate = 6 × 120
    - *why wrong:* This multiplies instead of dividing. Mean rate = quantity ÷ time.
- [ ] 0.5 g/s — rate = 6 ÷ 12
    - *why wrong:* The time is 120 s, not 12 s. Rate = 6 ÷ 120 = 0.05 g/s.

**Q6. [recall · CFTF]** State what is meant by the 'rate' of a chemical reaction.
- [✔︎] How quickly reactants are used up or products are formed
- [ ] How much product is made in total by the end
    - *why wrong:* That is the total yield, not the rate. Rate is about how QUICKLY, per unit time.
- [ ] How much energy is released by the reaction
    - *why wrong:* That is the energy change, not the rate. Rate measures speed, not energy.
- [ ] Whether the reaction is reversible or not
    - *why wrong:* That describes the reaction type, not how fast it goes.

**Q7. [recall · CFTF]** State the two quantities you divide to calculate the mean rate of a reaction.
- [✔︎] The quantity of reactant used or product formed, divided by the time taken
- [ ] The mass of reactant divided by the mass of product
    - *why wrong:* Rate compares an amount with TIME, not one mass with another.
- [ ] The volume of gas multiplied by the time taken
    - *why wrong:* Rate is quantity ÷ time (a division), not a multiplication.
- [ ] The temperature rise divided by the concentration
    - *why wrong:* Neither of these is used to calculate rate; rate = quantity ÷ time.

**Q8. [recall · CFTF]** Give a suitable unit for the rate of a reaction in which the gas produced is collected in a syringe.
- [✔︎] cm³/s (cubic centimetres per second)
- [ ] cm³ (cubic centimetres)
    - *why wrong:* cm³ is a volume, not a rate. A rate needs a quantity PER unit of time, e.g. cm³/s.
- [ ] s (seconds)
    - *why wrong:* Seconds is a time, not a rate. The unit must combine the gas volume with time.
- [ ] g/cm³ (grams per cubic centimetre)
    - *why wrong:* That is a density. For gas volume over time the unit is cm³/s.

**Q9. [apply · CFTF]** A volume–time graph becomes flat (horizontal). State what this tells you about the reactants.
- [✔︎] At least one reactant has been completely used up, so the reaction has stopped
- [ ] The reactants are reacting as fast as possible
    - *why wrong:* The fastest rate is the STEEPEST part (the start); a flat line means the reaction has stopped.
- [ ] The reactants have just been added to the flask
    - *why wrong:* Adding reactants would start a steep rise, not a flat line.
- [ ] The temperature has reached its highest point
    - *why wrong:* A flat line shows no more product is forming — a reactant has run out, not a temperature peak.

**Q10. [apply · CFTF]** Identify which of these is the slowest reaction.
- [✔︎] The rusting of an iron gate over several months
- [ ] A firework exploding
    - *why wrong:* An explosion is one of the FASTEST reactions — over in a fraction of a second.
- [ ] Magnesium ribbon burning in air
    - *why wrong:* Burning magnesium is a fast reaction, giving out light and heat quickly.
- [ ] An indigestion tablet fizzing in water
    - *why wrong:* Fizzing happens in seconds — much faster than rusting, which takes months.

**Q11. [calc · TF ⭐]** A reaction produces 90 cm³ of gas in 3 minutes. Calculate the mean rate of reaction in cm³/min.
- [✔︎] 30 cm³/min — rate = 90 ÷ 3
- [ ] 270 cm³/min — rate = 90 × 3
    - *why wrong:* This multiplies instead of dividing. Mean rate = quantity ÷ time = 90 ÷ 3.
- [ ] 0.5 cm³/min — rate = 90 ÷ 180
    - *why wrong:* The unit asked for is cm³/min, so keep the time in minutes (3), not seconds (180).
- [ ] 3 cm³/min — the time taken
    - *why wrong:* 3 is the time in minutes, not the rate. Rate = 90 ÷ 3 = 30 cm³/min.

**Q12. [apply · TF]** Two reactions, A and B, are plotted on the same volume–time axes. Line A is steeper than line B at the start. State which reaction is faster at the start and give a reason.
- [✔︎] Reaction A — a steeper line means more gas is produced each second
- [ ] Reaction B — the less steep line lasts longer so makes more gas
    - *why wrong:* How long a line lasts is not the rate; the STEEPER line (A) is the faster reaction at the start.
- [ ] Both are the same — they are on the same axes
    - *why wrong:* Being on the same axes does not make the rates equal; A is steeper, so A is faster.
- [ ] Reaction B — flatter lines always show faster reactions
    - *why wrong:* This is backwards: a flatter line is a SLOWER rate; steeper (A) is faster.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [calc · CFCHTFTH ⭐]** A gas syringe collects 48 cm³ of gas in 60 s. Calculate the mean rate of reaction.
- [✔︎] 0.8 cm³/s — rate = 48 ÷ 60
- [ ] 2880 cm³/s — rate = 48 × 60
    - *why wrong:* This multiplies the volume by the time. Mean rate = quantity ÷ time, so you divide.
- [ ] 1.25 cm³/s — rate = 60 ÷ 48
    - *why wrong:* This divides time by volume — the wrong way round. Rate = volume ÷ time = 48 ÷ 60.
- [ ] 48 cm³/s — the volume of gas collected
    - *why wrong:* This just reads off the volume and ignores the time. Rate must be a quantity per second.

**Q2. [apply · CFCHTFTH]** On a graph of gas volume against time, describe what a steeper part of the curve tells you about the reaction.
- [✔︎] The reaction is faster there — more gas is being produced each second
- [ ] The reaction is slower there — a steep line means it is struggling
    - *why wrong:* A steeper gradient means MORE volume per second, which is a faster rate, not slower.
- [ ] The reaction has finished — no more gas is being made
    - *why wrong:* A FLAT (horizontal) line means the reaction has finished; a steep line means it is going quickly.
- [ ] More gas has been collected in total, but the rate is unchanged
    - *why wrong:* The steepness (gradient) represents the RATE, not the total amount collected.

**Q3. [reason · CFCHTFTH]** Explain why the curve on a volume–time graph becomes less steep and eventually flattens as the reaction proceeds.
- [✔︎] The reactants are being used up, so there are fewer collisions each second (slower rate); flat means the reaction has finished
- [ ] More product keeps forming, which speeds the reaction up over time
    - *why wrong:* The rate DECREASES over time as reactants run out — the line gets less steep, not steeper.
- [ ] The reaction runs out of time, so it is forced to slow down
    - *why wrong:* Time does not limit the rate; the falling rate is caused by reactant particles being used up.
- [ ] The temperature drops as the reaction goes on, flattening the line
    - *why wrong:* The slowing is due to reactants being used up (fewer collisions), not a temperature change.

**Q4. [apply · CFCHTFTH]** Describe two things you could measure over time to follow the rate of the reaction between marble chips and hydrochloric acid.
- [✔︎] The volume of carbon dioxide gas given off, or the loss in mass of the flask
- [ ] The colour of the acid and the temperature of the room
    - *why wrong:* The acid stays colourless and room temperature is not a product — neither tracks how fast CO₂ forms.
- [ ] The mass of the marble chips only, weighed once at the end
    - *why wrong:* A single end measurement gives no rate — you must record how a quantity changes over TIME.
- [ ] The volume of the acid and the volume of the flask
    - *why wrong:* These do not change as the reaction proceeds, so they cannot measure the rate.

**Q5. [calc · CFCHTFTH ⭐]** A reaction flask loses 6 g of mass in 120 s as gas escapes. Calculate the mean rate of reaction in g/s.
- [✔︎] 0.05 g/s — rate = 6 ÷ 120
- [ ] 20 g/s — rate = 120 ÷ 6
    - *why wrong:* This divides time by mass — the wrong way round. Rate = mass lost ÷ time = 6 ÷ 120.
- [ ] 720 g/s — rate = 6 × 120
    - *why wrong:* This multiplies instead of dividing. Mean rate = quantity ÷ time.
- [ ] 0.5 g/s — rate = 6 ÷ 12
    - *why wrong:* The time is 120 s, not 12 s. Rate = 6 ÷ 120 = 0.05 g/s.

**Q6. [calc · CHTH ⭐]** A gas syringe collects 72 cm³ of gas in 1.5 minutes. Calculate the mean rate of reaction in cm³/s.
- [✔︎] 0.8 cm³/s — time = 1.5 × 60 = 90 s, so rate = 72 ÷ 90
- [ ] 48 cm³/s — rate = 72 ÷ 1.5
    - *why wrong:* The time was left in minutes. For cm³/s you must convert: 1.5 min = 90 s, then 72 ÷ 90 = 0.8.
- [ ] 108 cm³/s — rate = 72 × 1.5
    - *why wrong:* This multiplies instead of dividing, and does not convert the time to seconds.
- [ ] 1.25 cm³/s — rate = 90 ÷ 72
    - *why wrong:* This divides time by volume — the wrong way round. Rate = volume ÷ time = 72 ÷ 90.

**Q7. [reason · CHTH]** Explain how you would find the rate of reaction at exactly 30 s from a curved volume–time graph.
- [✔︎] Draw a tangent to the curve at 30 s and calculate its gradient (change in volume ÷ change in time)
- [ ] Read the volume at 30 s and divide it by 30
    - *why wrong:* That gives the MEAN rate up to 30 s, not the instantaneous rate at 30 s — you need a tangent.
- [ ] Measure the gradient of a straight line from the start to the end of the curve
    - *why wrong:* That is the overall mean rate, not the rate at one instant. Draw a tangent at 30 s instead.
- [ ] Read the volume at 30 s straight off the graph
    - *why wrong:* The volume at 30 s is an amount, not a rate. The rate is the gradient of the tangent there.

**Q8. [calc · CHTH ⭐]** A tangent drawn to a volume–time curve at t = 20 s rises from 12 cm³ (at 10 s) to 54 cm³ (at 30 s). Calculate the instantaneous rate at 20 s.
- [✔︎] 2.1 cm³/s — gradient = (54 − 12) ÷ (30 − 10) = 42 ÷ 20
- [ ] 1.8 cm³/s — gradient = 54 ÷ 30
    - *why wrong:* This uses one point instead of the change between two points. Gradient = Δvolume ÷ Δtime = 42 ÷ 20.
- [ ] 42 cm³/s — the change in volume
    - *why wrong:* 42 cm³ is the rise (Δvolume); you must divide it by the time interval (20 s) to get the rate.
- [ ] 0.48 cm³/s — gradient = 20 ÷ 42
    - *why wrong:* This divides Δtime by Δvolume — the wrong way round. Gradient = Δvolume ÷ Δtime.

**Q9. [reason · CHTH]** Explain why the instantaneous rate at the very start of a reaction is greater than the mean rate over the whole reaction.
- [✔︎] The reaction is fastest at the start (steepest gradient) and slows as reactants are used up, so the average over the whole reaction is lower
- [ ] The mean rate ignores the products, so it is always smaller
    - *why wrong:* The mean rate does account for product formed; it is smaller because the rate falls over time.
- [ ] The instantaneous rate is measured in different units, making it larger
    - *why wrong:* Both are measured in the same units (e.g. cm³/s); the difference is real, not a unit effect.
- [ ] The start of the reaction has the most product, so it is fastest
    - *why wrong:* The start has the most REACTANT (and least product); plenty of reactant is why it is fastest.

**Q10. [apply · CHTH]** A table shows the gas volume every 10 s; the increase in each 10 s interval gets smaller as the reaction proceeds. Explain what this pattern shows about the rate.
- [✔︎] The rate is decreasing over time, because reactant particles are being used up so there are fewer successful collisions each second
- [ ] The rate is constant, because gas is still being produced
    - *why wrong:* Gas is still produced, but LESS each interval — that is a falling rate, not a constant one.
- [ ] The rate is increasing, because the total volume keeps rising
    - *why wrong:* The total rises, but by smaller amounts each time, so the rate is falling, not rising.
- [ ] The reaction has already finished at the first interval
    - *why wrong:* It cannot have finished — gas is still being produced in every interval, just more slowly.

**Q11. [calc · TH ⭐]** A reaction produces 2.4 dm³ of gas in 2 minutes. Calculate the mean rate of reaction in cm³/s.
- [✔︎] 20 cm³/s — 2.4 dm³ = 2400 cm³ and 2 min = 120 s, so rate = 2400 ÷ 120
- [ ] 1200 cm³/s — rate = 2400 ÷ 2
    - *why wrong:* The volume was converted to cm³ but the time was left in minutes. Convert 2 min = 120 s: 2400 ÷ 120 = 20.
- [ ] 0.02 cm³/s — rate = 2.4 ÷ 120
    - *why wrong:* The time was converted to seconds but the volume was left in dm³. Convert 2.4 dm³ = 2400 cm³: 2400 ÷ 120 = 20.
- [ ] 1.2 cm³/s — rate = 2.4 ÷ 2
    - *why wrong:* Neither unit was converted. You must change dm³ to cm³ (×1000) and minutes to seconds (×60) first.

**Q12. [reason · TH]** Two experiments, using different acid concentrations but the same amount (moles) of the limiting reactant, are plotted on the same volume–time axes. Explain how the two curves compare in both their steepness and their final volume.
- [✔︎] The higher-concentration curve is steeper at the start (faster initial rate) but both curves reach the same final volume, because the same amount of reactant makes the same amount of gas
- [ ] The higher-concentration curve is steeper and reaches a higher final volume
    - *why wrong:* The final volume depends on the AMOUNT of reactant, which is the same, so both plateaus are at the same height.
- [ ] The higher-concentration curve is less steep but reaches the same final volume
    - *why wrong:* Higher concentration gives a FASTER initial rate, so its curve is steeper at the start, not less steep.
- [ ] The two curves are identical the whole way
    - *why wrong:* Different concentrations give different initial steepness; only the final volume is the same.

---

## Factors Affecting the Rate of Reaction  ·  `factors-affecting-rate`  ·  AQA 5.6.1.2

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.6.1.2 is shared content. No Triple-only material; Triple = the exact Combined set + 2 extra same-difficulty questions per tier.

**Common Mistake (mistake-first, three-beat):**

> Students often say a reaction is faster at a higher temperature simply because 'the particles move faster'. On its own this is not enough for full marks, because it only explains part of the effect. The full answer is that faster particles collide MORE OFTEN, and — just as importantly — a greater proportion of them now have energy above the activation energy, so a greater fraction of collisions are successful. Always link a rate change back to the frequency of successful collisions.

**Question sets by tier** (each item shows the tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (3 recall / 7 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Predict the effect of increasing the concentration of the acid on the rate of its reaction with magnesium, and give a reason.
- [✔︎] The rate increases — there are more acid particles in the same volume, so collisions happen more often
- [ ] The rate decreases — the acid particles get in each other's way
    - *why wrong:* More particles do not block each other; they collide MORE often, so the rate increases.
- [ ] The rate stays the same — concentration does not affect rate
    - *why wrong:* Concentration is one of the main factors: more concentrated means more frequent collisions, so faster.
- [ ] The rate increases — the particles are given more energy
    - *why wrong:* Concentration does not change the particles' energy (that is temperature); it changes how OFTEN they collide.

**Q2. [apply · CFCHTFTH]** Predict the effect of using powdered marble instead of large marble chips on the rate of reaction with acid, and explain why.
- [✔︎] The rate increases — powder has a larger surface area, so more particles are exposed to collide with the acid
- [ ] The rate decreases — powder has less surface area than chips
    - *why wrong:* Powder has a much LARGER total surface area than lumps, so the rate increases, not decreases.
- [ ] The rate stays the same — it is the same substance and mass
    - *why wrong:* Same substance and mass, but breaking it up exposes more surface, so more collisions and a faster rate.
- [ ] The rate increases — powder is a stronger form of marble
    - *why wrong:* Powder is not 'stronger'; it simply has more exposed surface area for collisions.

**Q3. [apply · CFCHTFTH]** Predict the effect of raising the temperature on the rate of a reaction, and explain your answer.
- [✔︎] The rate increases — particles move faster and more of them have enough energy, so collisions are more frequent and more successful
- [ ] The rate increases — the particles get bigger with heat
    - *why wrong:* Particles do not change size; they move faster and more have energy above the activation energy.
- [ ] The rate decreases — heat makes particles spread out and miss each other
    - *why wrong:* Higher temperature makes particles collide MORE often and more energetically, so the rate increases.
- [ ] The rate stays the same — temperature only changes the amount of product
    - *why wrong:* Temperature changes the RATE (how fast), and here it increases it; the amount of product is a separate idea.

**Q4. [apply · CFCHTFTH]** For a reaction between two gases, predict the effect of increasing the pressure on the rate, and give a reason.
- [✔︎] The rate increases — the gas particles are squeezed into a smaller volume, so they collide more often
- [ ] The rate decreases — high pressure holds the particles still
    - *why wrong:* Higher pressure does not hold particles still; it packs them closer so they collide MORE often.
- [ ] The rate stays the same — pressure has no effect on gases
    - *why wrong:* Pressure is a key factor for GAS reactions: more pressure means more frequent collisions, so faster.
- [ ] The rate increases — pressure gives each particle more energy
    - *why wrong:* Pressure does not change particle energy (that is temperature); it increases how OFTEN they collide.

**Q5. [reason · CFCHTFTH]** All four factors — temperature, concentration, surface area and pressure — can speed a reaction up. Explain what they all have in common in terms of collisions.
- [✔︎] They all increase the frequency of successful collisions between the reacting particles
- [ ] They all give the particles more energy
    - *why wrong:* Only temperature increases particle energy; concentration, surface area and pressure change how OFTEN particles collide.
- [ ] They all increase the amount of product that can form
    - *why wrong:* They change how FAST the product forms, not the maximum amount — that depends on how much reactant there is.
- [ ] They all lower the activation energy of the reaction
    - *why wrong:* Only a catalyst lowers the activation energy; these four increase the number of successful collisions instead.

**Q6. [recall · CFTF]** Name four factors that can increase the rate of a chemical reaction.
- [✔︎] Temperature, concentration, surface area, and a catalyst
- [ ] Colour, smell, mass and volume
    - *why wrong:* These are properties you might observe, not factors that change the rate.
- [ ] Time, cost, size of flask and stirring speed
    - *why wrong:* Only stirring has any effect; the recognised factors are temperature, concentration, surface area and a catalyst.
- [ ] The amount of product, the type of glassware and the day of the week
    - *why wrong:* None of these change the rate; the factors are temperature, concentration, surface area and a catalyst.

**Q7. [recall · CFTF]** State what happens to the rate of most reactions when the temperature is decreased.
- [✔︎] The rate decreases (the reaction goes more slowly)
- [ ] The rate increases
    - *why wrong:* Lower temperature means slower particles and fewer successful collisions, so the rate DECREASES.
- [ ] The rate stays exactly the same
    - *why wrong:* Temperature is a major factor; lowering it slows the reaction down.
- [ ] The reaction stops completely and cannot restart
    - *why wrong:* It slows down but does not usually stop completely; warming it again would speed it back up.

**Q8. [apply · CFTF]** Identify which will react faster with acid: a single large lump of zinc, or the same mass of zinc powder.
- [✔︎] The zinc powder
- [ ] The large lump of zinc
    - *why wrong:* The lump has less exposed surface, so it reacts more slowly than the powder.
- [ ] Both react at exactly the same rate
    - *why wrong:* Same mass, but the powder has far more surface area, so it reacts faster.
- [ ] Neither will react with acid
    - *why wrong:* Zinc does react with acid; the powder simply reacts faster because of its larger surface area.

**Q9. [recall · CFTF]** State the effect of adding a suitable catalyst on the rate of a reaction.
- [✔︎] It increases (speeds up) the rate
- [ ] It decreases the rate
    - *why wrong:* A catalyst speeds a reaction up, it does not slow it down.
- [ ] It has no effect on the rate
    - *why wrong:* A catalyst increases the rate — that is its whole purpose.
- [ ] It stops the reaction happening
    - *why wrong:* A catalyst speeds a reaction up; it does not stop it.

**Q10. [apply · CFTF]** A student wants a reaction between acid and a metal to go more slowly. Suggest one change they could make.
- [✔︎] Lower the temperature (or use a more dilute acid, or use larger lumps of metal)
- [ ] Raise the temperature
    - *why wrong:* Raising the temperature speeds a reaction UP; to slow it down you would lower the temperature.
- [ ] Crush the metal into a powder
    - *why wrong:* Powder has more surface area, which speeds the reaction up — the opposite of what is wanted.
- [ ] Use a more concentrated acid
    - *why wrong:* More concentrated acid speeds the reaction up; a more dilute acid would slow it down.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Predict the effect of increasing the concentration of the acid on the rate of its reaction with magnesium, and give a reason.
- [✔︎] The rate increases — there are more acid particles in the same volume, so collisions happen more often
- [ ] The rate decreases — the acid particles get in each other's way
    - *why wrong:* More particles do not block each other; they collide MORE often, so the rate increases.
- [ ] The rate stays the same — concentration does not affect rate
    - *why wrong:* Concentration is one of the main factors: more concentrated means more frequent collisions, so faster.
- [ ] The rate increases — the particles are given more energy
    - *why wrong:* Concentration does not change the particles' energy (that is temperature); it changes how OFTEN they collide.

**Q2. [apply · CFCHTFTH]** Predict the effect of using powdered marble instead of large marble chips on the rate of reaction with acid, and explain why.
- [✔︎] The rate increases — powder has a larger surface area, so more particles are exposed to collide with the acid
- [ ] The rate decreases — powder has less surface area than chips
    - *why wrong:* Powder has a much LARGER total surface area than lumps, so the rate increases, not decreases.
- [ ] The rate stays the same — it is the same substance and mass
    - *why wrong:* Same substance and mass, but breaking it up exposes more surface, so more collisions and a faster rate.
- [ ] The rate increases — powder is a stronger form of marble
    - *why wrong:* Powder is not 'stronger'; it simply has more exposed surface area for collisions.

**Q3. [apply · CFCHTFTH]** Predict the effect of raising the temperature on the rate of a reaction, and explain your answer.
- [✔︎] The rate increases — particles move faster and more of them have enough energy, so collisions are more frequent and more successful
- [ ] The rate increases — the particles get bigger with heat
    - *why wrong:* Particles do not change size; they move faster and more have energy above the activation energy.
- [ ] The rate decreases — heat makes particles spread out and miss each other
    - *why wrong:* Higher temperature makes particles collide MORE often and more energetically, so the rate increases.
- [ ] The rate stays the same — temperature only changes the amount of product
    - *why wrong:* Temperature changes the RATE (how fast), and here it increases it; the amount of product is a separate idea.

**Q4. [apply · CFCHTFTH]** For a reaction between two gases, predict the effect of increasing the pressure on the rate, and give a reason.
- [✔︎] The rate increases — the gas particles are squeezed into a smaller volume, so they collide more often
- [ ] The rate decreases — high pressure holds the particles still
    - *why wrong:* Higher pressure does not hold particles still; it packs them closer so they collide MORE often.
- [ ] The rate stays the same — pressure has no effect on gases
    - *why wrong:* Pressure is a key factor for GAS reactions: more pressure means more frequent collisions, so faster.
- [ ] The rate increases — pressure gives each particle more energy
    - *why wrong:* Pressure does not change particle energy (that is temperature); it increases how OFTEN they collide.

**Q5. [reason · CFCHTFTH]** All four factors — temperature, concentration, surface area and pressure — can speed a reaction up. Explain what they all have in common in terms of collisions.
- [✔︎] They all increase the frequency of successful collisions between the reacting particles
- [ ] They all give the particles more energy
    - *why wrong:* Only temperature increases particle energy; concentration, surface area and pressure change how OFTEN particles collide.
- [ ] They all increase the amount of product that can form
    - *why wrong:* They change how FAST the product forms, not the maximum amount — that depends on how much reactant there is.
- [ ] They all lower the activation energy of the reaction
    - *why wrong:* Only a catalyst lowers the activation energy; these four increase the number of successful collisions instead.

**Q6. [reason · CHTH]** Explain, in terms of collision theory, why increasing the concentration of a reactant in solution increases the rate.
- [✔︎] There are more reactant particles in the same volume, so collisions happen more frequently, giving more successful collisions each second
- [ ] The extra particles react without needing to collide
    - *why wrong:* All reactions still need collisions; concentration works by making those collisions more frequent.
- [ ] Each particle is given more energy, so more collisions succeed
    - *why wrong:* Concentration does not change particle energy (that is temperature); it increases the FREQUENCY of collisions.
- [ ] The activation energy is lowered by the extra particles
    - *why wrong:* Only a catalyst lowers the activation energy; concentration increases how often particles collide.

**Q7. [reason · CHTH]** Explain why increasing the surface area of a solid reactant increases the rate but does not change the total amount of product formed.
- [✔︎] More particles are exposed to collide, so the rate is faster, but the number of reactant particles (moles) is unchanged, so the final amount of product is the same
- [ ] More surface area means more reactant, so more product forms
    - *why wrong:* Breaking a solid up does not add any reactant — the mass and moles are unchanged, so the final product amount is the same.
- [ ] More surface area lowers the activation energy, speeding the reaction and making more product
    - *why wrong:* Surface area does not change the activation energy or the amount of reactant; it only exposes more particles to collide.
- [ ] The rate and the amount of product both stay the same
    - *why wrong:* The rate does increase (more exposed particles collide); it is only the FINAL amount that is unchanged.

**Q8. [apply · CHTH]** A gas-producing reaction is repeated using a higher concentration of acid but the same amount (moles) of the limiting reactant. Describe how the new volume–time curve compares with the original.
- [✔︎] It is steeper at the start (faster rate) but reaches the same final volume, because the same amount of reactant is used
- [ ] It is steeper at the start and reaches a higher final volume
    - *why wrong:* The amount of limiting reactant is unchanged, so the final volume is the same — only the initial steepness increases.
- [ ] It is less steep at the start but reaches the same final volume
    - *why wrong:* Higher concentration makes the reaction FASTER, so the curve is steeper at the start, not less steep.
- [ ] It is identical to the original curve
    - *why wrong:* Higher concentration increases the rate, so the start is steeper even though the final volume is the same.

**Q9. [reason · CHTH]** A student says that increasing the pressure will speed up the reaction between magnesium and dilute hydrochloric acid. Evaluate this statement.
- [✔︎] Pressure has almost no effect here, because the reactants are a solid and a solution, not gases — pressure only changes the rate when gases are involved
- [ ] The student is correct — increasing pressure always speeds up reactions
    - *why wrong:* Pressure changes the rate only for reactions involving GASES; here the reactants are a solid and a solution.
- [ ] The student is correct — pressure squeezes the acid particles closer together
    - *why wrong:* Liquids and solutions are almost incompressible, so pressure does not pack their particles closer; only gases respond to pressure.
- [ ] The student is wrong — increasing pressure would slow this reaction down
    - *why wrong:* It does not slow it down either; pressure simply has almost no effect when there are no gaseous reactants.

**Q10. [reason · CHTH]** Explain why raising the temperature increases the rate more effectively than raising the concentration by the same proportion, in terms of collisions and energy.
- [✔︎] Raising the temperature increases both the collision frequency AND the proportion of particles with energy ≥ the activation energy; concentration increases only the collision frequency
- [ ] Raising the temperature adds more particles, but concentration does not
    - *why wrong:* Temperature does not add particles; it makes existing particles move faster and gives more of them enough energy.
- [ ] Concentration lowers the activation energy, so it is actually the stronger factor
    - *why wrong:* Concentration does not lower the activation energy; temperature is more effective because it also raises the energy of the particles.
- [ ] They have exactly the same effect, so neither is more effective
    - *why wrong:* Temperature is more effective because it raises particle energy as well as collision frequency, unlike concentration.

### Triple Foundation — 12 questions (3 recall / 9 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Predict the effect of increasing the concentration of the acid on the rate of its reaction with magnesium, and give a reason.
- [✔︎] The rate increases — there are more acid particles in the same volume, so collisions happen more often
- [ ] The rate decreases — the acid particles get in each other's way
    - *why wrong:* More particles do not block each other; they collide MORE often, so the rate increases.
- [ ] The rate stays the same — concentration does not affect rate
    - *why wrong:* Concentration is one of the main factors: more concentrated means more frequent collisions, so faster.
- [ ] The rate increases — the particles are given more energy
    - *why wrong:* Concentration does not change the particles' energy (that is temperature); it changes how OFTEN they collide.

**Q2. [apply · CFCHTFTH]** Predict the effect of using powdered marble instead of large marble chips on the rate of reaction with acid, and explain why.
- [✔︎] The rate increases — powder has a larger surface area, so more particles are exposed to collide with the acid
- [ ] The rate decreases — powder has less surface area than chips
    - *why wrong:* Powder has a much LARGER total surface area than lumps, so the rate increases, not decreases.
- [ ] The rate stays the same — it is the same substance and mass
    - *why wrong:* Same substance and mass, but breaking it up exposes more surface, so more collisions and a faster rate.
- [ ] The rate increases — powder is a stronger form of marble
    - *why wrong:* Powder is not 'stronger'; it simply has more exposed surface area for collisions.

**Q3. [apply · CFCHTFTH]** Predict the effect of raising the temperature on the rate of a reaction, and explain your answer.
- [✔︎] The rate increases — particles move faster and more of them have enough energy, so collisions are more frequent and more successful
- [ ] The rate increases — the particles get bigger with heat
    - *why wrong:* Particles do not change size; they move faster and more have energy above the activation energy.
- [ ] The rate decreases — heat makes particles spread out and miss each other
    - *why wrong:* Higher temperature makes particles collide MORE often and more energetically, so the rate increases.
- [ ] The rate stays the same — temperature only changes the amount of product
    - *why wrong:* Temperature changes the RATE (how fast), and here it increases it; the amount of product is a separate idea.

**Q4. [apply · CFCHTFTH]** For a reaction between two gases, predict the effect of increasing the pressure on the rate, and give a reason.
- [✔︎] The rate increases — the gas particles are squeezed into a smaller volume, so they collide more often
- [ ] The rate decreases — high pressure holds the particles still
    - *why wrong:* Higher pressure does not hold particles still; it packs them closer so they collide MORE often.
- [ ] The rate stays the same — pressure has no effect on gases
    - *why wrong:* Pressure is a key factor for GAS reactions: more pressure means more frequent collisions, so faster.
- [ ] The rate increases — pressure gives each particle more energy
    - *why wrong:* Pressure does not change particle energy (that is temperature); it increases how OFTEN they collide.

**Q5. [reason · CFCHTFTH]** All four factors — temperature, concentration, surface area and pressure — can speed a reaction up. Explain what they all have in common in terms of collisions.
- [✔︎] They all increase the frequency of successful collisions between the reacting particles
- [ ] They all give the particles more energy
    - *why wrong:* Only temperature increases particle energy; concentration, surface area and pressure change how OFTEN particles collide.
- [ ] They all increase the amount of product that can form
    - *why wrong:* They change how FAST the product forms, not the maximum amount — that depends on how much reactant there is.
- [ ] They all lower the activation energy of the reaction
    - *why wrong:* Only a catalyst lowers the activation energy; these four increase the number of successful collisions instead.

**Q6. [recall · CFTF]** Name four factors that can increase the rate of a chemical reaction.
- [✔︎] Temperature, concentration, surface area, and a catalyst
- [ ] Colour, smell, mass and volume
    - *why wrong:* These are properties you might observe, not factors that change the rate.
- [ ] Time, cost, size of flask and stirring speed
    - *why wrong:* Only stirring has any effect; the recognised factors are temperature, concentration, surface area and a catalyst.
- [ ] The amount of product, the type of glassware and the day of the week
    - *why wrong:* None of these change the rate; the factors are temperature, concentration, surface area and a catalyst.

**Q7. [recall · CFTF]** State what happens to the rate of most reactions when the temperature is decreased.
- [✔︎] The rate decreases (the reaction goes more slowly)
- [ ] The rate increases
    - *why wrong:* Lower temperature means slower particles and fewer successful collisions, so the rate DECREASES.
- [ ] The rate stays exactly the same
    - *why wrong:* Temperature is a major factor; lowering it slows the reaction down.
- [ ] The reaction stops completely and cannot restart
    - *why wrong:* It slows down but does not usually stop completely; warming it again would speed it back up.

**Q8. [apply · CFTF]** Identify which will react faster with acid: a single large lump of zinc, or the same mass of zinc powder.
- [✔︎] The zinc powder
- [ ] The large lump of zinc
    - *why wrong:* The lump has less exposed surface, so it reacts more slowly than the powder.
- [ ] Both react at exactly the same rate
    - *why wrong:* Same mass, but the powder has far more surface area, so it reacts faster.
- [ ] Neither will react with acid
    - *why wrong:* Zinc does react with acid; the powder simply reacts faster because of its larger surface area.

**Q9. [recall · CFTF]** State the effect of adding a suitable catalyst on the rate of a reaction.
- [✔︎] It increases (speeds up) the rate
- [ ] It decreases the rate
    - *why wrong:* A catalyst speeds a reaction up, it does not slow it down.
- [ ] It has no effect on the rate
    - *why wrong:* A catalyst increases the rate — that is its whole purpose.
- [ ] It stops the reaction happening
    - *why wrong:* A catalyst speeds a reaction up; it does not stop it.

**Q10. [apply · CFTF]** A student wants a reaction between acid and a metal to go more slowly. Suggest one change they could make.
- [✔︎] Lower the temperature (or use a more dilute acid, or use larger lumps of metal)
- [ ] Raise the temperature
    - *why wrong:* Raising the temperature speeds a reaction UP; to slow it down you would lower the temperature.
- [ ] Crush the metal into a powder
    - *why wrong:* Powder has more surface area, which speeds the reaction up — the opposite of what is wanted.
- [ ] Use a more concentrated acid
    - *why wrong:* More concentrated acid speeds the reaction up; a more dilute acid would slow it down.

**Q11. [apply · TF]** Explain why milk turns sour more slowly when kept in a fridge than when left out on a warm kitchen table.
- [✔︎] The lower temperature in the fridge slows the reactions down — the particles move more slowly and collide less often and with less energy
- [ ] The fridge removes all the bacteria from the milk
    - *why wrong:* The fridge does not remove bacteria; it lowers the temperature, which slows the reactions that spoil the milk.
- [ ] The cold makes the milk particles bigger so they cannot react
    - *why wrong:* Particles do not change size; the cold simply makes them move more slowly, so they react less quickly.
- [ ] Milk only goes off in warm places, never in the cold
    - *why wrong:* Milk still goes off in the fridge, just much more slowly, because the reactions are slower at low temperature.

**Q12. [apply · TF]** Identify the change that would slow down the reaction between marble chips and hydrochloric acid.
- [✔︎] Diluting the acid with water
- [ ] Warming the acid before adding the chips
    - *why wrong:* Warming the acid speeds the reaction up, because the particles collide more often and more successfully.
- [ ] Crushing the marble chips into a powder
    - *why wrong:* Crushing increases the surface area, which speeds the reaction up, not down.
- [ ] Using more concentrated acid
    - *why wrong:* More concentrated acid has more particles per volume, so it speeds the reaction up.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Predict the effect of increasing the concentration of the acid on the rate of its reaction with magnesium, and give a reason.
- [✔︎] The rate increases — there are more acid particles in the same volume, so collisions happen more often
- [ ] The rate decreases — the acid particles get in each other's way
    - *why wrong:* More particles do not block each other; they collide MORE often, so the rate increases.
- [ ] The rate stays the same — concentration does not affect rate
    - *why wrong:* Concentration is one of the main factors: more concentrated means more frequent collisions, so faster.
- [ ] The rate increases — the particles are given more energy
    - *why wrong:* Concentration does not change the particles' energy (that is temperature); it changes how OFTEN they collide.

**Q2. [apply · CFCHTFTH]** Predict the effect of using powdered marble instead of large marble chips on the rate of reaction with acid, and explain why.
- [✔︎] The rate increases — powder has a larger surface area, so more particles are exposed to collide with the acid
- [ ] The rate decreases — powder has less surface area than chips
    - *why wrong:* Powder has a much LARGER total surface area than lumps, so the rate increases, not decreases.
- [ ] The rate stays the same — it is the same substance and mass
    - *why wrong:* Same substance and mass, but breaking it up exposes more surface, so more collisions and a faster rate.
- [ ] The rate increases — powder is a stronger form of marble
    - *why wrong:* Powder is not 'stronger'; it simply has more exposed surface area for collisions.

**Q3. [apply · CFCHTFTH]** Predict the effect of raising the temperature on the rate of a reaction, and explain your answer.
- [✔︎] The rate increases — particles move faster and more of them have enough energy, so collisions are more frequent and more successful
- [ ] The rate increases — the particles get bigger with heat
    - *why wrong:* Particles do not change size; they move faster and more have energy above the activation energy.
- [ ] The rate decreases — heat makes particles spread out and miss each other
    - *why wrong:* Higher temperature makes particles collide MORE often and more energetically, so the rate increases.
- [ ] The rate stays the same — temperature only changes the amount of product
    - *why wrong:* Temperature changes the RATE (how fast), and here it increases it; the amount of product is a separate idea.

**Q4. [apply · CFCHTFTH]** For a reaction between two gases, predict the effect of increasing the pressure on the rate, and give a reason.
- [✔︎] The rate increases — the gas particles are squeezed into a smaller volume, so they collide more often
- [ ] The rate decreases — high pressure holds the particles still
    - *why wrong:* Higher pressure does not hold particles still; it packs them closer so they collide MORE often.
- [ ] The rate stays the same — pressure has no effect on gases
    - *why wrong:* Pressure is a key factor for GAS reactions: more pressure means more frequent collisions, so faster.
- [ ] The rate increases — pressure gives each particle more energy
    - *why wrong:* Pressure does not change particle energy (that is temperature); it increases how OFTEN they collide.

**Q5. [reason · CFCHTFTH]** All four factors — temperature, concentration, surface area and pressure — can speed a reaction up. Explain what they all have in common in terms of collisions.
- [✔︎] They all increase the frequency of successful collisions between the reacting particles
- [ ] They all give the particles more energy
    - *why wrong:* Only temperature increases particle energy; concentration, surface area and pressure change how OFTEN particles collide.
- [ ] They all increase the amount of product that can form
    - *why wrong:* They change how FAST the product forms, not the maximum amount — that depends on how much reactant there is.
- [ ] They all lower the activation energy of the reaction
    - *why wrong:* Only a catalyst lowers the activation energy; these four increase the number of successful collisions instead.

**Q6. [reason · CHTH]** Explain, in terms of collision theory, why increasing the concentration of a reactant in solution increases the rate.
- [✔︎] There are more reactant particles in the same volume, so collisions happen more frequently, giving more successful collisions each second
- [ ] The extra particles react without needing to collide
    - *why wrong:* All reactions still need collisions; concentration works by making those collisions more frequent.
- [ ] Each particle is given more energy, so more collisions succeed
    - *why wrong:* Concentration does not change particle energy (that is temperature); it increases the FREQUENCY of collisions.
- [ ] The activation energy is lowered by the extra particles
    - *why wrong:* Only a catalyst lowers the activation energy; concentration increases how often particles collide.

**Q7. [reason · CHTH]** Explain why increasing the surface area of a solid reactant increases the rate but does not change the total amount of product formed.
- [✔︎] More particles are exposed to collide, so the rate is faster, but the number of reactant particles (moles) is unchanged, so the final amount of product is the same
- [ ] More surface area means more reactant, so more product forms
    - *why wrong:* Breaking a solid up does not add any reactant — the mass and moles are unchanged, so the final product amount is the same.
- [ ] More surface area lowers the activation energy, speeding the reaction and making more product
    - *why wrong:* Surface area does not change the activation energy or the amount of reactant; it only exposes more particles to collide.
- [ ] The rate and the amount of product both stay the same
    - *why wrong:* The rate does increase (more exposed particles collide); it is only the FINAL amount that is unchanged.

**Q8. [apply · CHTH]** A gas-producing reaction is repeated using a higher concentration of acid but the same amount (moles) of the limiting reactant. Describe how the new volume–time curve compares with the original.
- [✔︎] It is steeper at the start (faster rate) but reaches the same final volume, because the same amount of reactant is used
- [ ] It is steeper at the start and reaches a higher final volume
    - *why wrong:* The amount of limiting reactant is unchanged, so the final volume is the same — only the initial steepness increases.
- [ ] It is less steep at the start but reaches the same final volume
    - *why wrong:* Higher concentration makes the reaction FASTER, so the curve is steeper at the start, not less steep.
- [ ] It is identical to the original curve
    - *why wrong:* Higher concentration increases the rate, so the start is steeper even though the final volume is the same.

**Q9. [reason · CHTH]** A student says that increasing the pressure will speed up the reaction between magnesium and dilute hydrochloric acid. Evaluate this statement.
- [✔︎] Pressure has almost no effect here, because the reactants are a solid and a solution, not gases — pressure only changes the rate when gases are involved
- [ ] The student is correct — increasing pressure always speeds up reactions
    - *why wrong:* Pressure changes the rate only for reactions involving GASES; here the reactants are a solid and a solution.
- [ ] The student is correct — pressure squeezes the acid particles closer together
    - *why wrong:* Liquids and solutions are almost incompressible, so pressure does not pack their particles closer; only gases respond to pressure.
- [ ] The student is wrong — increasing pressure would slow this reaction down
    - *why wrong:* It does not slow it down either; pressure simply has almost no effect when there are no gaseous reactants.

**Q10. [reason · CHTH]** Explain why raising the temperature increases the rate more effectively than raising the concentration by the same proportion, in terms of collisions and energy.
- [✔︎] Raising the temperature increases both the collision frequency AND the proportion of particles with energy ≥ the activation energy; concentration increases only the collision frequency
- [ ] Raising the temperature adds more particles, but concentration does not
    - *why wrong:* Temperature does not add particles; it makes existing particles move faster and gives more of them enough energy.
- [ ] Concentration lowers the activation energy, so it is actually the stronger factor
    - *why wrong:* Concentration does not lower the activation energy; temperature is more effective because it also raises the energy of the particles.
- [ ] They have exactly the same effect, so neither is more effective
    - *why wrong:* Temperature is more effective because it raises particle energy as well as collision frequency, unlike concentration.

**Q11. [reason · TH]** In an experiment the time taken to collect a fixed volume of gas roughly halves for each 10 °C rise in temperature (from 20 °C to 50 °C). Explain what this shows about the effect of temperature on the rate.
- [✔︎] The rate roughly doubles for every 10 °C rise, because collecting the same volume of gas in half the time means the reaction is going twice as fast
- [ ] The rate roughly halves for every 10 °C rise
    - *why wrong:* A SHORTER time to collect the same gas means a FASTER rate, so the rate doubles, not halves.
- [ ] The rate is unchanged, because the same volume of gas is collected each time
    - *why wrong:* The same volume is collected in LESS time as temperature rises, so the rate increases each time.
- [ ] The rate roughly doubles for every 1 °C rise
    - *why wrong:* The data show the time halving for each 10 °C rise, so the rate doubles per 10 °C, not per 1 °C.

**Q12. [reason · TH]** Explain, using collision theory, why increasing the pressure speeds up a reaction between two gases but has almost no effect on a reaction between two solids.
- [✔︎] Higher pressure pushes gas particles closer together so they collide more often; the particles in a solid are already touching and cannot be squeezed closer, so pressure barely changes the rate
- [ ] Solids are affected more by pressure because they are denser than gases
    - *why wrong:* Solids barely respond to pressure because their particles are already packed together and cannot be pushed closer.
- [ ] Pressure has no effect on gases because gases always fill their container
    - *why wrong:* Increasing the pressure forces gas particles closer together, so they collide more often — pressure does speed up gas reactions.
- [ ] Both the gas and the solid reaction speed up equally when pressure increases
    - *why wrong:* Only the gas reaction speeds up; the solid reaction is almost unaffected because its particles cannot be pushed closer.

---

## Collision Theory and Activation Energy  ·  `collision-theory`  ·  AQA 5.6.1.3

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.6.1.3 is shared content. No Triple-only material; Triple = the exact Combined set + 2 extra same-difficulty questions per tier.

**Common Mistake (mistake-first, three-beat):**

> Students often think that every collision between reactant particles leads to a reaction. In fact most collisions do nothing, because the particles either do not have enough energy or hit in the wrong orientation. Only a collision with energy greater than or equal to the activation energy, and with the correct orientation, is 'successful' and leads to a reaction — and these make up only a small fraction of all the collisions taking place.

**Question sets by tier** (each item shows the tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (4 recall / 6 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain the two conditions that must be met for a collision between reactant particles to lead to a reaction.
- [✔︎] The particles must collide with energy greater than or equal to the activation energy, AND collide in the correct orientation
- [ ] The particles must collide gently and slowly
    - *why wrong:* A successful collision needs ENOUGH energy (≥ the activation energy), not a gentle one.
- [ ] The particles must simply touch each other at any speed
    - *why wrong:* Just touching is not enough — the collision must have energy ≥ the activation energy and the right orientation.
- [ ] The particles must be at the same temperature and the same size
    - *why wrong:* Neither matching temperature nor size is required; the collision needs enough energy and the correct orientation.

**Q2. [apply · CFCHTFTH]** Explain, in terms of collisions, why increasing the temperature increases the rate of a reaction.
- [✔︎] The particles move faster so collide more frequently, and more of them have energy ≥ the activation energy, so more collisions are successful
- [ ] The particles get larger, so they are easier to hit
    - *why wrong:* Particles do not change size; higher temperature makes them move faster and gives more of them enough energy.
- [ ] The particles collide less often but each collision is stronger
    - *why wrong:* Higher temperature makes collisions MORE frequent (as well as more energetic), not less frequent.
- [ ] The activation energy of the reaction is lowered
    - *why wrong:* Temperature does not lower the activation energy; it raises the energy of the particles so more clear the barrier.

**Q3. [apply · CFCHTFTH]** Explain, in terms of collision theory, why a higher concentration of a dissolved reactant increases the rate.
- [✔︎] There are more reactant particles in the same volume, so collisions happen more frequently, giving more successful collisions each second
- [ ] The particles each carry more energy at higher concentration
    - *why wrong:* Concentration does not change particle energy; it increases how OFTEN particles collide.
- [ ] The reaction needs fewer collisions when the concentration is higher
    - *why wrong:* The reaction still needs collisions; higher concentration simply makes them happen more often.
- [ ] Higher concentration lowers the activation energy
    - *why wrong:* Only a catalyst lowers the activation energy; concentration increases collision frequency.

**Q4. [reason · CFCHTFTH]** Describe what happens when two reactant particles collide with less energy than the activation energy.
- [✔︎] They do not react — they simply bounce apart unchanged
- [ ] They react slowly but still form some product
    - *why wrong:* Below the activation energy no reaction occurs at all — the particles bounce apart unchanged.
- [ ] They stick together and wait until they gain more energy
    - *why wrong:* They do not stick; a collision without enough energy just bounces apart with no reaction.
- [ ] They always react, because any collision causes a reaction
    - *why wrong:* Not every collision reacts — only those with energy ≥ the activation energy (and the right orientation).

**Q5. [apply · CFCHTFTH]** Explain, using collision theory, why increasing the surface area of a solid reactant increases the rate.
- [✔︎] More particles are exposed at the surface, so collisions with the other reactant happen more frequently
- [ ] The exposed particles are given more energy
    - *why wrong:* Surface area does not change particle energy; it exposes more particles to collide.
- [ ] A larger surface lowers the activation energy
    - *why wrong:* Surface area does not change the activation energy; it increases the frequency of collisions.
- [ ] The solid dissolves faster, adding new particles to the mixture
    - *why wrong:* No new particles are added; breaking the solid up simply exposes more of its existing particles to collide.

**Q6. [recall · CFTF]** State what must happen between reactant particles before a reaction can occur.
- [✔︎] They must collide with each other
- [ ] They must be heated until they melt
    - *why wrong:* Particles do not need to melt; they need to COLLIDE (with enough energy).
- [ ] They must be the same size
    - *why wrong:* Size does not matter; particles simply have to collide with enough energy.
- [ ] They must be pushed apart
    - *why wrong:* Pushing apart prevents reaction; particles must come together and collide.

**Q7. [recall · CFTF]** Define the term 'activation energy'.
- [✔︎] The minimum energy that colliding particles must have for a reaction to occur
- [ ] The energy given out by a reaction
    - *why wrong:* That is the energy released; activation energy is the minimum energy NEEDED to start the reaction.
- [ ] The total energy of all the particles added together
    - *why wrong:* Activation energy is a minimum threshold per collision, not the total energy of every particle.
- [ ] The energy needed to melt the reactants
    - *why wrong:* Activation energy is about starting the reaction, not melting; it is the minimum energy for a successful collision.

**Q8. [recall · CFTF]** State the two things a collision needs in order to be successful.
- [✔︎] Enough energy (at least the activation energy) and the correct orientation
- [ ] A low temperature and a large container
    - *why wrong:* Neither helps; a successful collision needs enough energy and the correct orientation.
- [ ] A catalyst and a high pressure
    - *why wrong:* These can change the rate, but a single successful collision itself just needs enough energy and the right orientation.
- [ ] Two particles of exactly equal mass
    - *why wrong:* Equal mass is not required; the collision needs enough energy and the correct orientation.

**Q9. [apply · CFTF]** Identify which particle is more likely to react in a collision: a fast-moving particle or a slow-moving particle (in the same reaction).
- [✔︎] The fast-moving particle, because it has more energy
- [ ] The slow-moving particle, because it has more time to react
    - *why wrong:* More energy, not more time, makes a collision successful — the faster particle is more likely to react.
- [ ] Both are equally likely, because they are the same substance
    - *why wrong:* Being the same substance does not matter; the faster particle has more energy, so it is more likely to react.
- [ ] Neither, because speed has no effect on reactions
    - *why wrong:* Speed affects the energy of a collision; a faster particle is more likely to have enough energy to react.

**Q10. [recall · CFTF]** State what happens to the rate of reaction if the number of successful collisions each second increases.
- [✔︎] The rate of reaction increases
- [ ] The rate of reaction decreases
    - *why wrong:* More successful collisions each second means a FASTER reaction, so the rate increases.
- [ ] The rate stays the same
    - *why wrong:* Rate depends directly on how many successful collisions happen each second, so it increases.
- [ ] The reaction stops
    - *why wrong:* More successful collisions speed the reaction up; they do not stop it.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain the two conditions that must be met for a collision between reactant particles to lead to a reaction.
- [✔︎] The particles must collide with energy greater than or equal to the activation energy, AND collide in the correct orientation
- [ ] The particles must collide gently and slowly
    - *why wrong:* A successful collision needs ENOUGH energy (≥ the activation energy), not a gentle one.
- [ ] The particles must simply touch each other at any speed
    - *why wrong:* Just touching is not enough — the collision must have energy ≥ the activation energy and the right orientation.
- [ ] The particles must be at the same temperature and the same size
    - *why wrong:* Neither matching temperature nor size is required; the collision needs enough energy and the correct orientation.

**Q2. [apply · CFCHTFTH]** Explain, in terms of collisions, why increasing the temperature increases the rate of a reaction.
- [✔︎] The particles move faster so collide more frequently, and more of them have energy ≥ the activation energy, so more collisions are successful
- [ ] The particles get larger, so they are easier to hit
    - *why wrong:* Particles do not change size; higher temperature makes them move faster and gives more of them enough energy.
- [ ] The particles collide less often but each collision is stronger
    - *why wrong:* Higher temperature makes collisions MORE frequent (as well as more energetic), not less frequent.
- [ ] The activation energy of the reaction is lowered
    - *why wrong:* Temperature does not lower the activation energy; it raises the energy of the particles so more clear the barrier.

**Q3. [apply · CFCHTFTH]** Explain, in terms of collision theory, why a higher concentration of a dissolved reactant increases the rate.
- [✔︎] There are more reactant particles in the same volume, so collisions happen more frequently, giving more successful collisions each second
- [ ] The particles each carry more energy at higher concentration
    - *why wrong:* Concentration does not change particle energy; it increases how OFTEN particles collide.
- [ ] The reaction needs fewer collisions when the concentration is higher
    - *why wrong:* The reaction still needs collisions; higher concentration simply makes them happen more often.
- [ ] Higher concentration lowers the activation energy
    - *why wrong:* Only a catalyst lowers the activation energy; concentration increases collision frequency.

**Q4. [reason · CFCHTFTH]** Describe what happens when two reactant particles collide with less energy than the activation energy.
- [✔︎] They do not react — they simply bounce apart unchanged
- [ ] They react slowly but still form some product
    - *why wrong:* Below the activation energy no reaction occurs at all — the particles bounce apart unchanged.
- [ ] They stick together and wait until they gain more energy
    - *why wrong:* They do not stick; a collision without enough energy just bounces apart with no reaction.
- [ ] They always react, because any collision causes a reaction
    - *why wrong:* Not every collision reacts — only those with energy ≥ the activation energy (and the right orientation).

**Q5. [apply · CFCHTFTH]** Explain, using collision theory, why increasing the surface area of a solid reactant increases the rate.
- [✔︎] More particles are exposed at the surface, so collisions with the other reactant happen more frequently
- [ ] The exposed particles are given more energy
    - *why wrong:* Surface area does not change particle energy; it exposes more particles to collide.
- [ ] A larger surface lowers the activation energy
    - *why wrong:* Surface area does not change the activation energy; it increases the frequency of collisions.
- [ ] The solid dissolves faster, adding new particles to the mixture
    - *why wrong:* No new particles are added; breaking the solid up simply exposes more of its existing particles to collide.

**Q6. [reason · CHTH]** The Maxwell–Boltzmann distribution shows the spread of energies of the particles. Explain how raising the temperature changes this distribution and why that increases the rate.
- [✔︎] The curve becomes lower and flatter and shifts to higher energies, so a greater proportion of particles have energy ≥ the activation energy, meaning more collisions are successful
- [ ] The whole curve shifts to lower energies, so more particles can react
    - *why wrong:* Raising the temperature shifts the curve to HIGHER energies, not lower; that is why more particles exceed the activation energy.
- [ ] The curve gets taller and narrower, lowering the activation energy
    - *why wrong:* Higher temperature makes the curve lower and broader, and it does not change the activation energy itself.
- [ ] The activation energy line moves to the left
    - *why wrong:* The activation energy is fixed; it is the distribution of particle energies that shifts, not the Ea line (only a catalyst moves Ea).

**Q7. [reason · CHTH]** Explain why increasing the concentration increases the frequency of collisions but does NOT change the proportion of collisions that are successful.
- [✔︎] More particles in the same volume means more collisions, but their energies are unchanged, so the fraction with energy ≥ the activation energy stays the same
- [ ] It increases both, because more particles means more energy
    - *why wrong:* Concentration adds particles but does not change their energies, so the SUCCESS fraction is unchanged.
- [ ] It lowers the proportion that succeed, because collisions get crowded
    - *why wrong:* Crowding does not lower the success fraction; the particles' energies are unchanged, so the fraction is the same.
- [ ] It changes neither the frequency nor the success rate
    - *why wrong:* It does increase the FREQUENCY of collisions; it just leaves the success fraction unchanged.

**Q8. [apply · CHTH]** On a Maxwell–Boltzmann distribution, the activation energy is marked by a vertical line. Describe what the area under the curve to the right of this line represents.
- [✔︎] The proportion (number) of particles that have enough energy to react
- [ ] The average energy of all the particles
    - *why wrong:* The average is a single point on the axis; the area to the right of Ea is the number of particles ABOVE that energy.
- [ ] The total number of collisions per second
    - *why wrong:* The area shows how many particles have enough energy, not the collision frequency.
- [ ] The particles that have too little energy to react
    - *why wrong:* Those particles are to the LEFT of the Ea line; the area to the right shows particles WITH enough energy.

**Q9. [reason · CHTH]** Explain why even a small rise in temperature can cause a large increase in the rate of reaction, referring to the Maxwell–Boltzmann distribution.
- [✔︎] A small temperature rise moves many particles from below to above the activation energy, greatly increasing the number of successful collisions
- [ ] A small rise doubles the size of every particle
    - *why wrong:* Particles do not change size; the rise moves many of them above the activation energy.
- [ ] A small rise lowers the activation energy a lot
    - *why wrong:* Temperature does not lower the activation energy; it raises particle energies so many more clear the fixed barrier.
- [ ] A small rise mainly increases how often particles collide
    - *why wrong:* The collision frequency rises only slightly; the big effect is the jump in the number of particles above the activation energy.

**Q10. [reason · CHTH]** A student says 'increasing the temperature speeds a reaction up only because the particles collide more often'. Evaluate this statement.
- [✔︎] It is incomplete — the main reason is that more particles now have energy ≥ the activation energy, so more collisions succeed; the rise in collision frequency is a smaller effect
- [ ] The student is completely correct
    - *why wrong:* It is only part of the answer; the dominant effect is the increase in the proportion of particles above the activation energy.
- [ ] The student is wrong — collision frequency does not change with temperature
    - *why wrong:* Collision frequency does increase a little with temperature; the point is that the energy effect is the bigger one.
- [ ] The student is wrong — temperature only changes the amount of product
    - *why wrong:* Temperature changes the rate (how fast), mainly through the energy of the particles, not just the final amount of product.

### Triple Foundation — 12 questions (4 recall / 8 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain the two conditions that must be met for a collision between reactant particles to lead to a reaction.
- [✔︎] The particles must collide with energy greater than or equal to the activation energy, AND collide in the correct orientation
- [ ] The particles must collide gently and slowly
    - *why wrong:* A successful collision needs ENOUGH energy (≥ the activation energy), not a gentle one.
- [ ] The particles must simply touch each other at any speed
    - *why wrong:* Just touching is not enough — the collision must have energy ≥ the activation energy and the right orientation.
- [ ] The particles must be at the same temperature and the same size
    - *why wrong:* Neither matching temperature nor size is required; the collision needs enough energy and the correct orientation.

**Q2. [apply · CFCHTFTH]** Explain, in terms of collisions, why increasing the temperature increases the rate of a reaction.
- [✔︎] The particles move faster so collide more frequently, and more of them have energy ≥ the activation energy, so more collisions are successful
- [ ] The particles get larger, so they are easier to hit
    - *why wrong:* Particles do not change size; higher temperature makes them move faster and gives more of them enough energy.
- [ ] The particles collide less often but each collision is stronger
    - *why wrong:* Higher temperature makes collisions MORE frequent (as well as more energetic), not less frequent.
- [ ] The activation energy of the reaction is lowered
    - *why wrong:* Temperature does not lower the activation energy; it raises the energy of the particles so more clear the barrier.

**Q3. [apply · CFCHTFTH]** Explain, in terms of collision theory, why a higher concentration of a dissolved reactant increases the rate.
- [✔︎] There are more reactant particles in the same volume, so collisions happen more frequently, giving more successful collisions each second
- [ ] The particles each carry more energy at higher concentration
    - *why wrong:* Concentration does not change particle energy; it increases how OFTEN particles collide.
- [ ] The reaction needs fewer collisions when the concentration is higher
    - *why wrong:* The reaction still needs collisions; higher concentration simply makes them happen more often.
- [ ] Higher concentration lowers the activation energy
    - *why wrong:* Only a catalyst lowers the activation energy; concentration increases collision frequency.

**Q4. [reason · CFCHTFTH]** Describe what happens when two reactant particles collide with less energy than the activation energy.
- [✔︎] They do not react — they simply bounce apart unchanged
- [ ] They react slowly but still form some product
    - *why wrong:* Below the activation energy no reaction occurs at all — the particles bounce apart unchanged.
- [ ] They stick together and wait until they gain more energy
    - *why wrong:* They do not stick; a collision without enough energy just bounces apart with no reaction.
- [ ] They always react, because any collision causes a reaction
    - *why wrong:* Not every collision reacts — only those with energy ≥ the activation energy (and the right orientation).

**Q5. [apply · CFCHTFTH]** Explain, using collision theory, why increasing the surface area of a solid reactant increases the rate.
- [✔︎] More particles are exposed at the surface, so collisions with the other reactant happen more frequently
- [ ] The exposed particles are given more energy
    - *why wrong:* Surface area does not change particle energy; it exposes more particles to collide.
- [ ] A larger surface lowers the activation energy
    - *why wrong:* Surface area does not change the activation energy; it increases the frequency of collisions.
- [ ] The solid dissolves faster, adding new particles to the mixture
    - *why wrong:* No new particles are added; breaking the solid up simply exposes more of its existing particles to collide.

**Q6. [recall · CFTF]** State what must happen between reactant particles before a reaction can occur.
- [✔︎] They must collide with each other
- [ ] They must be heated until they melt
    - *why wrong:* Particles do not need to melt; they need to COLLIDE (with enough energy).
- [ ] They must be the same size
    - *why wrong:* Size does not matter; particles simply have to collide with enough energy.
- [ ] They must be pushed apart
    - *why wrong:* Pushing apart prevents reaction; particles must come together and collide.

**Q7. [recall · CFTF]** Define the term 'activation energy'.
- [✔︎] The minimum energy that colliding particles must have for a reaction to occur
- [ ] The energy given out by a reaction
    - *why wrong:* That is the energy released; activation energy is the minimum energy NEEDED to start the reaction.
- [ ] The total energy of all the particles added together
    - *why wrong:* Activation energy is a minimum threshold per collision, not the total energy of every particle.
- [ ] The energy needed to melt the reactants
    - *why wrong:* Activation energy is about starting the reaction, not melting; it is the minimum energy for a successful collision.

**Q8. [recall · CFTF]** State the two things a collision needs in order to be successful.
- [✔︎] Enough energy (at least the activation energy) and the correct orientation
- [ ] A low temperature and a large container
    - *why wrong:* Neither helps; a successful collision needs enough energy and the correct orientation.
- [ ] A catalyst and a high pressure
    - *why wrong:* These can change the rate, but a single successful collision itself just needs enough energy and the right orientation.
- [ ] Two particles of exactly equal mass
    - *why wrong:* Equal mass is not required; the collision needs enough energy and the correct orientation.

**Q9. [apply · CFTF]** Identify which particle is more likely to react in a collision: a fast-moving particle or a slow-moving particle (in the same reaction).
- [✔︎] The fast-moving particle, because it has more energy
- [ ] The slow-moving particle, because it has more time to react
    - *why wrong:* More energy, not more time, makes a collision successful — the faster particle is more likely to react.
- [ ] Both are equally likely, because they are the same substance
    - *why wrong:* Being the same substance does not matter; the faster particle has more energy, so it is more likely to react.
- [ ] Neither, because speed has no effect on reactions
    - *why wrong:* Speed affects the energy of a collision; a faster particle is more likely to have enough energy to react.

**Q10. [recall · CFTF]** State what happens to the rate of reaction if the number of successful collisions each second increases.
- [✔︎] The rate of reaction increases
- [ ] The rate of reaction decreases
    - *why wrong:* More successful collisions each second means a FASTER reaction, so the rate increases.
- [ ] The rate stays the same
    - *why wrong:* Rate depends directly on how many successful collisions happen each second, so it increases.
- [ ] The reaction stops
    - *why wrong:* More successful collisions speed the reaction up; they do not stop it.

**Q11. [apply · TF]** Use collision theory to explain why food stored in a freezer keeps for much longer than food left at room temperature.
- [✔︎] At the low temperature the particles move more slowly, so they collide less often and with less energy, making the reactions that spoil food much slower
- [ ] The freezer kills all the reactions permanently
    - *why wrong:* The reactions are slowed, not permanently stopped; the food would still spoil eventually, just far more slowly.
- [ ] The cold gives the particles more energy to react
    - *why wrong:* Cold gives particles LESS energy, so they react more slowly — that is why the food keeps longer.
- [ ] Freezing removes the particles that cause food to spoil
    - *why wrong:* Freezing does not remove particles; it lowers their energy and collision frequency, slowing the spoiling reactions.

**Q12. [apply · TF]** A reaction speeds up when the solid reactant is crushed into a fine powder. Describe, in terms of particles colliding, why this works.
- [✔︎] Crushing exposes more of the solid's particles at the surface, so there are more collisions each second with the other reactant
- [ ] Crushing gives each particle more energy to collide
    - *why wrong:* Crushing does not change particle energy; it exposes more particles to collide, increasing the collision frequency.
- [ ] Crushing lowers the activation energy of the reaction
    - *why wrong:* Crushing does not change the activation energy; it increases how many particles are exposed to collide.
- [ ] Crushing turns the solid into a gas so it reacts faster
    - *why wrong:* Crushing does not change the state; it simply exposes more surface particles to collide with the other reactant.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [reason · CFCHTFTH]** Explain the two conditions that must be met for a collision between reactant particles to lead to a reaction.
- [✔︎] The particles must collide with energy greater than or equal to the activation energy, AND collide in the correct orientation
- [ ] The particles must collide gently and slowly
    - *why wrong:* A successful collision needs ENOUGH energy (≥ the activation energy), not a gentle one.
- [ ] The particles must simply touch each other at any speed
    - *why wrong:* Just touching is not enough — the collision must have energy ≥ the activation energy and the right orientation.
- [ ] The particles must be at the same temperature and the same size
    - *why wrong:* Neither matching temperature nor size is required; the collision needs enough energy and the correct orientation.

**Q2. [apply · CFCHTFTH]** Explain, in terms of collisions, why increasing the temperature increases the rate of a reaction.
- [✔︎] The particles move faster so collide more frequently, and more of them have energy ≥ the activation energy, so more collisions are successful
- [ ] The particles get larger, so they are easier to hit
    - *why wrong:* Particles do not change size; higher temperature makes them move faster and gives more of them enough energy.
- [ ] The particles collide less often but each collision is stronger
    - *why wrong:* Higher temperature makes collisions MORE frequent (as well as more energetic), not less frequent.
- [ ] The activation energy of the reaction is lowered
    - *why wrong:* Temperature does not lower the activation energy; it raises the energy of the particles so more clear the barrier.

**Q3. [apply · CFCHTFTH]** Explain, in terms of collision theory, why a higher concentration of a dissolved reactant increases the rate.
- [✔︎] There are more reactant particles in the same volume, so collisions happen more frequently, giving more successful collisions each second
- [ ] The particles each carry more energy at higher concentration
    - *why wrong:* Concentration does not change particle energy; it increases how OFTEN particles collide.
- [ ] The reaction needs fewer collisions when the concentration is higher
    - *why wrong:* The reaction still needs collisions; higher concentration simply makes them happen more often.
- [ ] Higher concentration lowers the activation energy
    - *why wrong:* Only a catalyst lowers the activation energy; concentration increases collision frequency.

**Q4. [reason · CFCHTFTH]** Describe what happens when two reactant particles collide with less energy than the activation energy.
- [✔︎] They do not react — they simply bounce apart unchanged
- [ ] They react slowly but still form some product
    - *why wrong:* Below the activation energy no reaction occurs at all — the particles bounce apart unchanged.
- [ ] They stick together and wait until they gain more energy
    - *why wrong:* They do not stick; a collision without enough energy just bounces apart with no reaction.
- [ ] They always react, because any collision causes a reaction
    - *why wrong:* Not every collision reacts — only those with energy ≥ the activation energy (and the right orientation).

**Q5. [apply · CFCHTFTH]** Explain, using collision theory, why increasing the surface area of a solid reactant increases the rate.
- [✔︎] More particles are exposed at the surface, so collisions with the other reactant happen more frequently
- [ ] The exposed particles are given more energy
    - *why wrong:* Surface area does not change particle energy; it exposes more particles to collide.
- [ ] A larger surface lowers the activation energy
    - *why wrong:* Surface area does not change the activation energy; it increases the frequency of collisions.
- [ ] The solid dissolves faster, adding new particles to the mixture
    - *why wrong:* No new particles are added; breaking the solid up simply exposes more of its existing particles to collide.

**Q6. [reason · CHTH]** The Maxwell–Boltzmann distribution shows the spread of energies of the particles. Explain how raising the temperature changes this distribution and why that increases the rate.
- [✔︎] The curve becomes lower and flatter and shifts to higher energies, so a greater proportion of particles have energy ≥ the activation energy, meaning more collisions are successful
- [ ] The whole curve shifts to lower energies, so more particles can react
    - *why wrong:* Raising the temperature shifts the curve to HIGHER energies, not lower; that is why more particles exceed the activation energy.
- [ ] The curve gets taller and narrower, lowering the activation energy
    - *why wrong:* Higher temperature makes the curve lower and broader, and it does not change the activation energy itself.
- [ ] The activation energy line moves to the left
    - *why wrong:* The activation energy is fixed; it is the distribution of particle energies that shifts, not the Ea line (only a catalyst moves Ea).

**Q7. [reason · CHTH]** Explain why increasing the concentration increases the frequency of collisions but does NOT change the proportion of collisions that are successful.
- [✔︎] More particles in the same volume means more collisions, but their energies are unchanged, so the fraction with energy ≥ the activation energy stays the same
- [ ] It increases both, because more particles means more energy
    - *why wrong:* Concentration adds particles but does not change their energies, so the SUCCESS fraction is unchanged.
- [ ] It lowers the proportion that succeed, because collisions get crowded
    - *why wrong:* Crowding does not lower the success fraction; the particles' energies are unchanged, so the fraction is the same.
- [ ] It changes neither the frequency nor the success rate
    - *why wrong:* It does increase the FREQUENCY of collisions; it just leaves the success fraction unchanged.

**Q8. [apply · CHTH]** On a Maxwell–Boltzmann distribution, the activation energy is marked by a vertical line. Describe what the area under the curve to the right of this line represents.
- [✔︎] The proportion (number) of particles that have enough energy to react
- [ ] The average energy of all the particles
    - *why wrong:* The average is a single point on the axis; the area to the right of Ea is the number of particles ABOVE that energy.
- [ ] The total number of collisions per second
    - *why wrong:* The area shows how many particles have enough energy, not the collision frequency.
- [ ] The particles that have too little energy to react
    - *why wrong:* Those particles are to the LEFT of the Ea line; the area to the right shows particles WITH enough energy.

**Q9. [reason · CHTH]** Explain why even a small rise in temperature can cause a large increase in the rate of reaction, referring to the Maxwell–Boltzmann distribution.
- [✔︎] A small temperature rise moves many particles from below to above the activation energy, greatly increasing the number of successful collisions
- [ ] A small rise doubles the size of every particle
    - *why wrong:* Particles do not change size; the rise moves many of them above the activation energy.
- [ ] A small rise lowers the activation energy a lot
    - *why wrong:* Temperature does not lower the activation energy; it raises particle energies so many more clear the fixed barrier.
- [ ] A small rise mainly increases how often particles collide
    - *why wrong:* The collision frequency rises only slightly; the big effect is the jump in the number of particles above the activation energy.

**Q10. [reason · CHTH]** A student says 'increasing the temperature speeds a reaction up only because the particles collide more often'. Evaluate this statement.
- [✔︎] It is incomplete — the main reason is that more particles now have energy ≥ the activation energy, so more collisions succeed; the rise in collision frequency is a smaller effect
- [ ] The student is completely correct
    - *why wrong:* It is only part of the answer; the dominant effect is the increase in the proportion of particles above the activation energy.
- [ ] The student is wrong — collision frequency does not change with temperature
    - *why wrong:* Collision frequency does increase a little with temperature; the point is that the energy effect is the bigger one.
- [ ] The student is wrong — temperature only changes the amount of product
    - *why wrong:* Temperature changes the rate (how fast), mainly through the energy of the particles, not just the final amount of product.

**Q11. [reason · TH]** On a Maxwell–Boltzmann distribution, explain how adding a catalyst increases the number of successful collisions even though the temperature is unchanged.
- [✔︎] A catalyst lowers the activation energy, moving the Ea line to the left, so a greater proportion of the particles now have enough energy to react
- [ ] A catalyst shifts the whole energy-distribution curve to the right
    - *why wrong:* The shape of the distribution depends only on temperature, which is unchanged; the catalyst moves the Ea line, not the curve.
- [ ] A catalyst makes the curve taller so more particles react
    - *why wrong:* The curve's shape is fixed by the temperature; the catalyst lowers the Ea line instead of changing the curve.
- [ ] A catalyst raises the activation energy, so only the strongest collisions react
    - *why wrong:* A catalyst LOWERS the activation energy, so MORE collisions succeed, not fewer.

**Q12. [reason · TH]** The Maxwell–Boltzmann curve starts at the origin and, at high energy, gets closer and closer to the energy axis without ever touching it. Explain why the curve has this shape.
- [✔︎] No particles have zero energy (they are always moving), so the curve starts at the origin; and there is no upper limit on energy, so a few particles always have very high energy — the curve approaches but never reaches the axis
- [ ] All the particles have the same energy, so the curve is a single tall spike
    - *why wrong:* The particles have a wide SPREAD of energies, which is why the curve is a broad hump rather than a spike.
- [ ] The curve touches the axis at high energy because no particle can have more than the activation energy
    - *why wrong:* Many particles have more than the activation energy; there is no upper limit, so the curve never quite reaches the axis.
- [ ] The curve starts high because most particles have zero energy
    - *why wrong:* No particles have zero energy, so the curve starts at the origin (zero height) and then rises.

---

## Catalysts  ·  `catalysts`  ·  AQA 5.6.1.4

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.6.1.4 is shared content. No Triple-only material; Triple = the exact Combined set + 2 extra same-difficulty questions per tier.

**Common Mistake (mistake-first, three-beat):**

> Students often think a catalyst is used up during a reaction, or that it increases the amount of product made. Neither is true: a catalyst is chemically unchanged at the end and does not appear in the balanced equation, and it does not change how much product forms or the position of any equilibrium. What a catalyst actually does is speed the reaction up by providing an alternative pathway with a lower activation energy — you get the same amount of product, just sooner, and the catalyst is left over ready to be used again.

**Question sets by tier** (each item shows the tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (4 recall / 6 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Explain how a catalyst increases the rate of a chemical reaction.
- [✔︎] It provides an alternative reaction pathway with a lower activation energy, so a greater proportion of collisions are successful
- [ ] It gives all the reactant particles more energy
    - *why wrong:* A catalyst does not add energy to the particles; it lowers the activation energy they need to react.
- [ ] It increases the number of reactant particles in the mixture
    - *why wrong:* A catalyst adds no reactant particles; it lowers the activation energy so more collisions succeed.
- [ ] It makes the particles collide more often by pushing them together
    - *why wrong:* A catalyst does not increase collision frequency; it lowers the activation energy so more of the existing collisions succeed.

**Q2. [reason · CFCHTFTH]** Explain why a catalyst is not included in the balanced equation for a reaction.
- [✔︎] It is not used up — it is chemically unchanged at the end, so the same mass is present before and after
- [ ] It is used up, so there is no point writing it
    - *why wrong:* The opposite is true: a catalyst is NOT used up, which is exactly why it is left out of the equation.
- [ ] It is a gas, so it escapes before the equation is written
    - *why wrong:* Whether it is left out has nothing to do with state; it is left out because it is unchanged by the reaction.
- [ ] It turns into one of the products during the reaction
    - *why wrong:* A catalyst does not turn into a product; it is recovered chemically unchanged, so it is not in the equation.

**Q3. [apply · CFCHTFTH]** A catalyst speeds up a reaction. Predict its effect on the total amount of product finally made, and explain.
- [✔︎] No change — a catalyst changes only how fast the product forms, not how much is formed
- [ ] More product is made, because the catalyst adds extra reactant
    - *why wrong:* A catalyst adds no reactant; it only speeds the reaction up, so the final amount of product is unchanged.
- [ ] Less product is made, because some is used to regenerate the catalyst
    - *why wrong:* The catalyst is not consumed and uses up no product; the final amount of product is unchanged.
- [ ] The amount of product depends on how much catalyst is added
    - *why wrong:* The amount of product depends on the amount of reactant, not the catalyst; the catalyst only changes the speed.

**Q4. [reason · CFCHTFTH]** Explain why enzymes are described as biological catalysts.
- [✔︎] They speed up reactions in living organisms without being used up, by providing a pathway with a lower activation energy
- [ ] They are catalysts made only in factories for use in living things
    - *why wrong:* Enzymes are made BY living organisms; they are natural catalysts, not manufactured ones.
- [ ] They are reactants that are used up as the body reacts
    - *why wrong:* Enzymes are catalysts, so they are not used up; they can be reused many times.
- [ ] They provide the energy that living reactions need
    - *why wrong:* Enzymes do not provide energy; like all catalysts they lower the activation energy needed for the reaction.

**Q5. [apply · CFCHTFTH]** On a reaction profile diagram, describe how the curve for a catalysed reaction differs from the uncatalysed one.
- [✔︎] The activation energy 'hump' is lower, but the energy levels of the reactants and products (and ΔH) are unchanged
- [ ] The whole curve is lower, including the reactant and product energy levels
    - *why wrong:* Only the activation energy hump is lowered; the reactant and product energy levels stay exactly the same.
- [ ] The products end up at a lower energy, releasing more energy overall
    - *why wrong:* A catalyst does not change the product energy or ΔH; it only lowers the activation energy barrier.
- [ ] The hump is taller because the reaction goes faster
    - *why wrong:* A catalyst LOWERS the activation energy hump; a lower barrier is why the reaction goes faster.

**Q6. [recall · CFTF]** State what a catalyst does to the rate of a reaction.
- [✔︎] It increases (speeds up) the rate
- [ ] It decreases the rate
    - *why wrong:* A catalyst speeds a reaction up, not down.
- [ ] It has no effect on the rate
    - *why wrong:* A catalyst's purpose is to increase the rate.
- [ ] It changes the rate only if the reaction is reversible
    - *why wrong:* A catalyst speeds up reactions whether or not they are reversible.

**Q7. [recall · CFTF]** State what happens to the mass of a catalyst by the end of a reaction.
- [✔︎] It is unchanged — the same mass of catalyst remains
- [ ] It decreases, because the catalyst is used up
    - *why wrong:* A catalyst is NOT used up; the same mass remains at the end.
- [ ] It increases, because product sticks to it
    - *why wrong:* A catalyst is recovered chemically unchanged; its mass is the same at the end.
- [ ] It falls to zero by the end of the reaction
    - *why wrong:* A catalyst is not consumed, so its mass does not fall — it is unchanged.

**Q8. [recall · CFTF]** Name the type of catalyst found in living organisms.
- [✔︎] Enzymes
- [ ] Hormones
    - *why wrong:* Hormones are chemical messengers, not catalysts; the biological catalysts are enzymes.
- [ ] Minerals
    - *why wrong:* Minerals are not catalysts; biological reactions are catalysed by enzymes.
- [ ] Antibodies
    - *why wrong:* Antibodies fight infection; the catalysts in living things are enzymes.

**Q9. [apply · CFTF]** Identify the main advantage of using a catalyst in an industrial process.
- [✔︎] The reaction happens faster, often at a lower temperature, which saves energy and money
- [ ] It increases the amount of product that can be made from the reactants
    - *why wrong:* A catalyst does not increase the amount of product; its advantage is making the reaction faster and cheaper.
- [ ] It removes the need for any reactants
    - *why wrong:* Reactants are still needed; the catalyst only speeds the reaction up.
- [ ] It makes the product purer by removing impurities
    - *why wrong:* A catalyst speeds the reaction up; it is not there to purify the product.

**Q10. [recall · CFTF]** State whether a catalyst is used up during a reaction.
- [✔︎] No — a catalyst is not used up
- [ ] Yes — it is used up like a reactant
    - *why wrong:* A catalyst is not used up; it is recovered unchanged and can be reused.
- [ ] Only some of it is used up each time
    - *why wrong:* None of the catalyst is used up; it is chemically unchanged at the end.
- [ ] It is used up only in reversible reactions
    - *why wrong:* A catalyst is never used up, whether the reaction is reversible or not.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Explain how a catalyst increases the rate of a chemical reaction.
- [✔︎] It provides an alternative reaction pathway with a lower activation energy, so a greater proportion of collisions are successful
- [ ] It gives all the reactant particles more energy
    - *why wrong:* A catalyst does not add energy to the particles; it lowers the activation energy they need to react.
- [ ] It increases the number of reactant particles in the mixture
    - *why wrong:* A catalyst adds no reactant particles; it lowers the activation energy so more collisions succeed.
- [ ] It makes the particles collide more often by pushing them together
    - *why wrong:* A catalyst does not increase collision frequency; it lowers the activation energy so more of the existing collisions succeed.

**Q2. [reason · CFCHTFTH]** Explain why a catalyst is not included in the balanced equation for a reaction.
- [✔︎] It is not used up — it is chemically unchanged at the end, so the same mass is present before and after
- [ ] It is used up, so there is no point writing it
    - *why wrong:* The opposite is true: a catalyst is NOT used up, which is exactly why it is left out of the equation.
- [ ] It is a gas, so it escapes before the equation is written
    - *why wrong:* Whether it is left out has nothing to do with state; it is left out because it is unchanged by the reaction.
- [ ] It turns into one of the products during the reaction
    - *why wrong:* A catalyst does not turn into a product; it is recovered chemically unchanged, so it is not in the equation.

**Q3. [apply · CFCHTFTH]** A catalyst speeds up a reaction. Predict its effect on the total amount of product finally made, and explain.
- [✔︎] No change — a catalyst changes only how fast the product forms, not how much is formed
- [ ] More product is made, because the catalyst adds extra reactant
    - *why wrong:* A catalyst adds no reactant; it only speeds the reaction up, so the final amount of product is unchanged.
- [ ] Less product is made, because some is used to regenerate the catalyst
    - *why wrong:* The catalyst is not consumed and uses up no product; the final amount of product is unchanged.
- [ ] The amount of product depends on how much catalyst is added
    - *why wrong:* The amount of product depends on the amount of reactant, not the catalyst; the catalyst only changes the speed.

**Q4. [reason · CFCHTFTH]** Explain why enzymes are described as biological catalysts.
- [✔︎] They speed up reactions in living organisms without being used up, by providing a pathway with a lower activation energy
- [ ] They are catalysts made only in factories for use in living things
    - *why wrong:* Enzymes are made BY living organisms; they are natural catalysts, not manufactured ones.
- [ ] They are reactants that are used up as the body reacts
    - *why wrong:* Enzymes are catalysts, so they are not used up; they can be reused many times.
- [ ] They provide the energy that living reactions need
    - *why wrong:* Enzymes do not provide energy; like all catalysts they lower the activation energy needed for the reaction.

**Q5. [apply · CFCHTFTH]** On a reaction profile diagram, describe how the curve for a catalysed reaction differs from the uncatalysed one.
- [✔︎] The activation energy 'hump' is lower, but the energy levels of the reactants and products (and ΔH) are unchanged
- [ ] The whole curve is lower, including the reactant and product energy levels
    - *why wrong:* Only the activation energy hump is lowered; the reactant and product energy levels stay exactly the same.
- [ ] The products end up at a lower energy, releasing more energy overall
    - *why wrong:* A catalyst does not change the product energy or ΔH; it only lowers the activation energy barrier.
- [ ] The hump is taller because the reaction goes faster
    - *why wrong:* A catalyst LOWERS the activation energy hump; a lower barrier is why the reaction goes faster.

**Q6. [reason · CHTH]** Explain, in terms of activation energy, why a catalyst increases the proportion of collisions that are successful.
- [✔︎] It provides an alternative pathway with a lower activation energy, so a greater proportion of colliding particles have enough energy to react
- [ ] It raises the energy of the colliding particles above the barrier
    - *why wrong:* A catalyst does not raise the particles' energy; it LOWERS the activation energy barrier they must clear.
- [ ] It removes the need for the particles to collide at all
    - *why wrong:* Collisions are still required; the catalyst just lowers the energy those collisions need to succeed.
- [ ] It increases the activation energy so only strong collisions react
    - *why wrong:* A catalyst LOWERS the activation energy, so more collisions succeed — not fewer.

**Q7. [reason · CHTH]** A catalyst is added to a reversible reaction that has reached equilibrium. Explain its effect on the position of equilibrium.
- [✔︎] None — a catalyst speeds up the forward and reverse reactions equally, so equilibrium is reached faster but its position (and the yield) is unchanged
- [ ] It shifts the equilibrium towards the products, increasing the yield
    - *why wrong:* A catalyst does not shift the equilibrium; it speeds both directions equally, so the yield is unchanged.
- [ ] It shifts the equilibrium towards the reactants
    - *why wrong:* A catalyst has no effect on the position of equilibrium; it only changes how quickly equilibrium is reached.
- [ ] It speeds up only the forward reaction, making more product
    - *why wrong:* A catalyst speeds up the forward AND reverse reactions equally, so the position of equilibrium does not move.

**Q8. [reason · CHTH]** On a reaction profile, explain why adding a catalyst lowers the activation energy but does not change ΔH.
- [✔︎] The catalyst only lowers the energy barrier between reactants and products; the energy levels of the reactants and products are unchanged, so their difference (ΔH) is the same
- [ ] The catalyst lowers the product energy level, so ΔH gets bigger
    - *why wrong:* A catalyst does not change the product energy level; ΔH is unchanged because only the barrier is lowered.
- [ ] The catalyst changes ΔH because the reaction now releases energy faster
    - *why wrong:* Releasing energy faster is a rate effect; ΔH depends only on the reactant and product energies, which are unchanged.
- [ ] ΔH falls by the same amount as the activation energy
    - *why wrong:* ΔH is unrelated to the height of the barrier; lowering the activation energy leaves ΔH unchanged.

**Q9. [reason · CHTH]** Explain why only a small amount of catalyst is needed to catalyse a large amount of reactant.
- [✔︎] The catalyst is not used up — it is regenerated after each reaction and can be used over and over again
- [ ] A small amount is enough because the catalyst is very concentrated
    - *why wrong:* It is not about concentration; the catalyst works because it is reused repeatedly without being consumed.
- [ ] A small amount dissolves to make a large amount during the reaction
    - *why wrong:* The catalyst does not multiply; a small amount suffices because it is regenerated and reused.
- [ ] Only a little is needed because it is slowly used up
    - *why wrong:* The catalyst is not used up at all; that is exactly why a small amount can process a lot of reactant.

**Q10. [apply · CHTH]** Different reactions need different catalysts. Suggest why a catalyst that works well for one reaction may not work for another.
- [✔︎] A catalyst provides a specific alternative pathway, so it must suit the particular reactants — it is specific to that reaction, much like an enzyme
- [ ] Because catalysts are always used up, so each reaction needs a fresh one
    - *why wrong:* Catalysts are not used up; the reason is that each catalyst suits a specific reaction and its reactants.
- [ ] Because a catalyst can only lower the activation energy of a gas reaction
    - *why wrong:* Catalysts are used for many kinds of reactions, not only gases; they are specific to the reactants involved.
- [ ] Because using the wrong catalyst would change the ΔH of the reaction
    - *why wrong:* A catalyst never changes ΔH; the point is that each catalyst provides a pathway suited to particular reactants.

### Triple Foundation — 12 questions (4 recall / 8 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Explain how a catalyst increases the rate of a chemical reaction.
- [✔︎] It provides an alternative reaction pathway with a lower activation energy, so a greater proportion of collisions are successful
- [ ] It gives all the reactant particles more energy
    - *why wrong:* A catalyst does not add energy to the particles; it lowers the activation energy they need to react.
- [ ] It increases the number of reactant particles in the mixture
    - *why wrong:* A catalyst adds no reactant particles; it lowers the activation energy so more collisions succeed.
- [ ] It makes the particles collide more often by pushing them together
    - *why wrong:* A catalyst does not increase collision frequency; it lowers the activation energy so more of the existing collisions succeed.

**Q2. [reason · CFCHTFTH]** Explain why a catalyst is not included in the balanced equation for a reaction.
- [✔︎] It is not used up — it is chemically unchanged at the end, so the same mass is present before and after
- [ ] It is used up, so there is no point writing it
    - *why wrong:* The opposite is true: a catalyst is NOT used up, which is exactly why it is left out of the equation.
- [ ] It is a gas, so it escapes before the equation is written
    - *why wrong:* Whether it is left out has nothing to do with state; it is left out because it is unchanged by the reaction.
- [ ] It turns into one of the products during the reaction
    - *why wrong:* A catalyst does not turn into a product; it is recovered chemically unchanged, so it is not in the equation.

**Q3. [apply · CFCHTFTH]** A catalyst speeds up a reaction. Predict its effect on the total amount of product finally made, and explain.
- [✔︎] No change — a catalyst changes only how fast the product forms, not how much is formed
- [ ] More product is made, because the catalyst adds extra reactant
    - *why wrong:* A catalyst adds no reactant; it only speeds the reaction up, so the final amount of product is unchanged.
- [ ] Less product is made, because some is used to regenerate the catalyst
    - *why wrong:* The catalyst is not consumed and uses up no product; the final amount of product is unchanged.
- [ ] The amount of product depends on how much catalyst is added
    - *why wrong:* The amount of product depends on the amount of reactant, not the catalyst; the catalyst only changes the speed.

**Q4. [reason · CFCHTFTH]** Explain why enzymes are described as biological catalysts.
- [✔︎] They speed up reactions in living organisms without being used up, by providing a pathway with a lower activation energy
- [ ] They are catalysts made only in factories for use in living things
    - *why wrong:* Enzymes are made BY living organisms; they are natural catalysts, not manufactured ones.
- [ ] They are reactants that are used up as the body reacts
    - *why wrong:* Enzymes are catalysts, so they are not used up; they can be reused many times.
- [ ] They provide the energy that living reactions need
    - *why wrong:* Enzymes do not provide energy; like all catalysts they lower the activation energy needed for the reaction.

**Q5. [apply · CFCHTFTH]** On a reaction profile diagram, describe how the curve for a catalysed reaction differs from the uncatalysed one.
- [✔︎] The activation energy 'hump' is lower, but the energy levels of the reactants and products (and ΔH) are unchanged
- [ ] The whole curve is lower, including the reactant and product energy levels
    - *why wrong:* Only the activation energy hump is lowered; the reactant and product energy levels stay exactly the same.
- [ ] The products end up at a lower energy, releasing more energy overall
    - *why wrong:* A catalyst does not change the product energy or ΔH; it only lowers the activation energy barrier.
- [ ] The hump is taller because the reaction goes faster
    - *why wrong:* A catalyst LOWERS the activation energy hump; a lower barrier is why the reaction goes faster.

**Q6. [recall · CFTF]** State what a catalyst does to the rate of a reaction.
- [✔︎] It increases (speeds up) the rate
- [ ] It decreases the rate
    - *why wrong:* A catalyst speeds a reaction up, not down.
- [ ] It has no effect on the rate
    - *why wrong:* A catalyst's purpose is to increase the rate.
- [ ] It changes the rate only if the reaction is reversible
    - *why wrong:* A catalyst speeds up reactions whether or not they are reversible.

**Q7. [recall · CFTF]** State what happens to the mass of a catalyst by the end of a reaction.
- [✔︎] It is unchanged — the same mass of catalyst remains
- [ ] It decreases, because the catalyst is used up
    - *why wrong:* A catalyst is NOT used up; the same mass remains at the end.
- [ ] It increases, because product sticks to it
    - *why wrong:* A catalyst is recovered chemically unchanged; its mass is the same at the end.
- [ ] It falls to zero by the end of the reaction
    - *why wrong:* A catalyst is not consumed, so its mass does not fall — it is unchanged.

**Q8. [recall · CFTF]** Name the type of catalyst found in living organisms.
- [✔︎] Enzymes
- [ ] Hormones
    - *why wrong:* Hormones are chemical messengers, not catalysts; the biological catalysts are enzymes.
- [ ] Minerals
    - *why wrong:* Minerals are not catalysts; biological reactions are catalysed by enzymes.
- [ ] Antibodies
    - *why wrong:* Antibodies fight infection; the catalysts in living things are enzymes.

**Q9. [apply · CFTF]** Identify the main advantage of using a catalyst in an industrial process.
- [✔︎] The reaction happens faster, often at a lower temperature, which saves energy and money
- [ ] It increases the amount of product that can be made from the reactants
    - *why wrong:* A catalyst does not increase the amount of product; its advantage is making the reaction faster and cheaper.
- [ ] It removes the need for any reactants
    - *why wrong:* Reactants are still needed; the catalyst only speeds the reaction up.
- [ ] It makes the product purer by removing impurities
    - *why wrong:* A catalyst speeds the reaction up; it is not there to purify the product.

**Q10. [recall · CFTF]** State whether a catalyst is used up during a reaction.
- [✔︎] No — a catalyst is not used up
- [ ] Yes — it is used up like a reactant
    - *why wrong:* A catalyst is not used up; it is recovered unchanged and can be reused.
- [ ] Only some of it is used up each time
    - *why wrong:* None of the catalyst is used up; it is chemically unchanged at the end.
- [ ] It is used up only in reversible reactions
    - *why wrong:* A catalyst is never used up, whether the reaction is reversible or not.

**Q11. [apply · TF]** A small amount of manganese(IV) oxide makes hydrogen peroxide decompose much faster, and it can be recovered unchanged afterwards. Explain why manganese(IV) oxide is acting as a catalyst here.
- [✔︎] It speeds the reaction up and is chemically unchanged at the end, which is exactly what a catalyst does
- [ ] It is a reactant, because it takes part in the reaction
    - *why wrong:* Because it is recovered unchanged and not used up, it is a catalyst, not a reactant.
- [ ] It is a product, because it is collected at the end
    - *why wrong:* It was present at the start and is unchanged at the end, so it is a catalyst, not a product.
- [ ] It is a catalyst because it turns the hydrogen peroxide blue
    - *why wrong:* Being a catalyst is about speeding the reaction up while staying unchanged, not about any colour change.

**Q12. [apply · TF]** Suggest why using a catalyst can make an industrial process cheaper.
- [✔︎] The reaction can run faster and at a lower temperature, so less energy (fuel) is needed and more product is made per hour
- [ ] The catalyst replaces the reactants, so less raw material is bought
    - *why wrong:* The catalyst does not replace reactants; it saves money by letting the reaction run faster and at lower temperature.
- [ ] The catalyst is used up, so it does not need storing
    - *why wrong:* A catalyst is not used up — it is reused, which is part of why it saves money.
- [ ] The catalyst increases the maximum amount of product from the reactants
    - *why wrong:* A catalyst does not increase the maximum yield; it saves money by speeding the reaction up and lowering the temperature needed.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Explain how a catalyst increases the rate of a chemical reaction.
- [✔︎] It provides an alternative reaction pathway with a lower activation energy, so a greater proportion of collisions are successful
- [ ] It gives all the reactant particles more energy
    - *why wrong:* A catalyst does not add energy to the particles; it lowers the activation energy they need to react.
- [ ] It increases the number of reactant particles in the mixture
    - *why wrong:* A catalyst adds no reactant particles; it lowers the activation energy so more collisions succeed.
- [ ] It makes the particles collide more often by pushing them together
    - *why wrong:* A catalyst does not increase collision frequency; it lowers the activation energy so more of the existing collisions succeed.

**Q2. [reason · CFCHTFTH]** Explain why a catalyst is not included in the balanced equation for a reaction.
- [✔︎] It is not used up — it is chemically unchanged at the end, so the same mass is present before and after
- [ ] It is used up, so there is no point writing it
    - *why wrong:* The opposite is true: a catalyst is NOT used up, which is exactly why it is left out of the equation.
- [ ] It is a gas, so it escapes before the equation is written
    - *why wrong:* Whether it is left out has nothing to do with state; it is left out because it is unchanged by the reaction.
- [ ] It turns into one of the products during the reaction
    - *why wrong:* A catalyst does not turn into a product; it is recovered chemically unchanged, so it is not in the equation.

**Q3. [apply · CFCHTFTH]** A catalyst speeds up a reaction. Predict its effect on the total amount of product finally made, and explain.
- [✔︎] No change — a catalyst changes only how fast the product forms, not how much is formed
- [ ] More product is made, because the catalyst adds extra reactant
    - *why wrong:* A catalyst adds no reactant; it only speeds the reaction up, so the final amount of product is unchanged.
- [ ] Less product is made, because some is used to regenerate the catalyst
    - *why wrong:* The catalyst is not consumed and uses up no product; the final amount of product is unchanged.
- [ ] The amount of product depends on how much catalyst is added
    - *why wrong:* The amount of product depends on the amount of reactant, not the catalyst; the catalyst only changes the speed.

**Q4. [reason · CFCHTFTH]** Explain why enzymes are described as biological catalysts.
- [✔︎] They speed up reactions in living organisms without being used up, by providing a pathway with a lower activation energy
- [ ] They are catalysts made only in factories for use in living things
    - *why wrong:* Enzymes are made BY living organisms; they are natural catalysts, not manufactured ones.
- [ ] They are reactants that are used up as the body reacts
    - *why wrong:* Enzymes are catalysts, so they are not used up; they can be reused many times.
- [ ] They provide the energy that living reactions need
    - *why wrong:* Enzymes do not provide energy; like all catalysts they lower the activation energy needed for the reaction.

**Q5. [apply · CFCHTFTH]** On a reaction profile diagram, describe how the curve for a catalysed reaction differs from the uncatalysed one.
- [✔︎] The activation energy 'hump' is lower, but the energy levels of the reactants and products (and ΔH) are unchanged
- [ ] The whole curve is lower, including the reactant and product energy levels
    - *why wrong:* Only the activation energy hump is lowered; the reactant and product energy levels stay exactly the same.
- [ ] The products end up at a lower energy, releasing more energy overall
    - *why wrong:* A catalyst does not change the product energy or ΔH; it only lowers the activation energy barrier.
- [ ] The hump is taller because the reaction goes faster
    - *why wrong:* A catalyst LOWERS the activation energy hump; a lower barrier is why the reaction goes faster.

**Q6. [reason · CHTH]** Explain, in terms of activation energy, why a catalyst increases the proportion of collisions that are successful.
- [✔︎] It provides an alternative pathway with a lower activation energy, so a greater proportion of colliding particles have enough energy to react
- [ ] It raises the energy of the colliding particles above the barrier
    - *why wrong:* A catalyst does not raise the particles' energy; it LOWERS the activation energy barrier they must clear.
- [ ] It removes the need for the particles to collide at all
    - *why wrong:* Collisions are still required; the catalyst just lowers the energy those collisions need to succeed.
- [ ] It increases the activation energy so only strong collisions react
    - *why wrong:* A catalyst LOWERS the activation energy, so more collisions succeed — not fewer.

**Q7. [reason · CHTH]** A catalyst is added to a reversible reaction that has reached equilibrium. Explain its effect on the position of equilibrium.
- [✔︎] None — a catalyst speeds up the forward and reverse reactions equally, so equilibrium is reached faster but its position (and the yield) is unchanged
- [ ] It shifts the equilibrium towards the products, increasing the yield
    - *why wrong:* A catalyst does not shift the equilibrium; it speeds both directions equally, so the yield is unchanged.
- [ ] It shifts the equilibrium towards the reactants
    - *why wrong:* A catalyst has no effect on the position of equilibrium; it only changes how quickly equilibrium is reached.
- [ ] It speeds up only the forward reaction, making more product
    - *why wrong:* A catalyst speeds up the forward AND reverse reactions equally, so the position of equilibrium does not move.

**Q8. [reason · CHTH]** On a reaction profile, explain why adding a catalyst lowers the activation energy but does not change ΔH.
- [✔︎] The catalyst only lowers the energy barrier between reactants and products; the energy levels of the reactants and products are unchanged, so their difference (ΔH) is the same
- [ ] The catalyst lowers the product energy level, so ΔH gets bigger
    - *why wrong:* A catalyst does not change the product energy level; ΔH is unchanged because only the barrier is lowered.
- [ ] The catalyst changes ΔH because the reaction now releases energy faster
    - *why wrong:* Releasing energy faster is a rate effect; ΔH depends only on the reactant and product energies, which are unchanged.
- [ ] ΔH falls by the same amount as the activation energy
    - *why wrong:* ΔH is unrelated to the height of the barrier; lowering the activation energy leaves ΔH unchanged.

**Q9. [reason · CHTH]** Explain why only a small amount of catalyst is needed to catalyse a large amount of reactant.
- [✔︎] The catalyst is not used up — it is regenerated after each reaction and can be used over and over again
- [ ] A small amount is enough because the catalyst is very concentrated
    - *why wrong:* It is not about concentration; the catalyst works because it is reused repeatedly without being consumed.
- [ ] A small amount dissolves to make a large amount during the reaction
    - *why wrong:* The catalyst does not multiply; a small amount suffices because it is regenerated and reused.
- [ ] Only a little is needed because it is slowly used up
    - *why wrong:* The catalyst is not used up at all; that is exactly why a small amount can process a lot of reactant.

**Q10. [apply · CHTH]** Different reactions need different catalysts. Suggest why a catalyst that works well for one reaction may not work for another.
- [✔︎] A catalyst provides a specific alternative pathway, so it must suit the particular reactants — it is specific to that reaction, much like an enzyme
- [ ] Because catalysts are always used up, so each reaction needs a fresh one
    - *why wrong:* Catalysts are not used up; the reason is that each catalyst suits a specific reaction and its reactants.
- [ ] Because a catalyst can only lower the activation energy of a gas reaction
    - *why wrong:* Catalysts are used for many kinds of reactions, not only gases; they are specific to the reactants involved.
- [ ] Because using the wrong catalyst would change the ΔH of the reaction
    - *why wrong:* A catalyst never changes ΔH; the point is that each catalyst provides a pathway suited to particular reactants.

**Q11. [reason · TH]** A solid catalyst speeds up a reaction between gases by adsorbing the gas molecules onto its surface. Explain how this lowers the activation energy.
- [✔︎] The reactant molecules bond to the catalyst surface, which weakens their bonds and holds them close together in the correct orientation, so they react more easily (a lower activation energy)
- [ ] The surface heats the gases up, giving them more energy to react
    - *why wrong:* The surface does not add energy; it lowers the activation energy by weakening bonds and positioning the molecules.
- [ ] The surface increases the pressure of the gases so they collide more often
    - *why wrong:* Adsorption works by lowering the activation energy, not by acting like a pressure (collision-frequency) increase.
- [ ] The surface adds extra reactant molecules, so more product forms
    - *why wrong:* The catalyst adds no reactant; it provides a surface that lowers the activation energy for the existing molecules.

**Q12. [apply · TH]** A student claims that adding an iron catalyst increases the yield of ammonia in the Haber process. Evaluate this claim.
- [✔︎] It is wrong — the iron catalyst only speeds up how quickly equilibrium is reached; the yield (the position of equilibrium) is unchanged
- [ ] It is correct — a catalyst always increases the yield of a reversible reaction
    - *why wrong:* A catalyst never changes the position of equilibrium, so the yield of a reversible reaction is unchanged.
- [ ] It is correct — the catalyst shifts the equilibrium towards the ammonia
    - *why wrong:* A catalyst speeds up the forward and reverse reactions equally and does not shift the equilibrium.
- [ ] It is wrong — the catalyst actually lowers the yield of ammonia
    - *why wrong:* The catalyst leaves the yield unchanged; it neither raises nor lowers the position of equilibrium.

---

## Reversible Reactions and Equilibrium  ·  `reversible-reactions-equilibrium`  ·  AQA 5.6.2.1–5.6.2.3

> 🚩 **Triple-depth call (your review):** MATCHED — AQA 5.6.2.1–5.6.2.3 is shared content. No Triple-only material; Triple = the exact Combined set + 2 extra same-difficulty questions per tier.

**Common Mistake (mistake-first, three-beat):**

> Students often think that at equilibrium the reaction has stopped, or that the amounts of reactants and products must be equal. Neither is right: at equilibrium the forward and reverse reactions are both still going, they simply happen at the same rate, so nothing appears to change. And 'constant' does not mean 'equal' — the concentrations stay steady but are usually different, because the position of equilibrium can lie mostly towards the reactants or mostly towards the products.

**Question sets by tier** (each item shows the tiers it appears in; ⭐ = full-review flag):

### Combined Foundation — 10 questions (3 recall / 7 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Describe what is meant by a reversible reaction, using an example.
- [✔︎] One that can go both ways — the products can react to reform the reactants, e.g. hydrated copper(II) sulfate ⇌ anhydrous copper(II) sulfate + water
- [ ] One that gives out energy and then takes it back in at the end
    - *why wrong:* That describes energy transfer, not reversibility. A reversible reaction is one whose products can reform the reactants.
- [ ] One that can only go forwards but very quickly
    - *why wrong:* A reversible reaction goes BOTH ways; a reaction that only goes forwards is not reversible.
- [ ] One that produces a gas which then escapes
    - *why wrong:* Escaping gas is not what 'reversible' means; it means the products can react to reform the reactants.

**Q2. [reason · CFCHTFTH]** Explain what is meant by 'dynamic equilibrium' in a reversible reaction.
- [✔︎] The forward and reverse reactions are still happening, but at equal rates, so the concentrations of reactants and products stay constant
- [ ] Both reactions have stopped, so nothing changes
    - *why wrong:* The reactions have not stopped — they continue at EQUAL rates, which is why it is called dynamic.
- [ ] Only the forward reaction is happening, but very slowly
    - *why wrong:* At equilibrium both the forward and reverse reactions occur, at equal rates — not just the forward one.
- [ ] The reactants and products are present in exactly equal amounts
    - *why wrong:* 'Constant' does not mean 'equal' — the amounts stay steady but are usually not equal.

**Q3. [apply · CFCHTFTH]** State the condition a reversible reaction must be kept in for it to reach equilibrium.
- [✔︎] A closed system, where no reactants or products can enter or leave
- [ ] An open container, so gases can escape freely
    - *why wrong:* In an open container products escape and cannot react back, so equilibrium cannot be reached — it must be closed.
- [ ] A vacuum, with no air present
    - *why wrong:* It is not about air; the system must be CLOSED so nothing can enter or leave.
- [ ] A constantly heated flask
    - *why wrong:* Heating is not the requirement; the system must be closed so the reverse reaction can balance the forward one.

**Q4. [reason · CFCHTFTH]** A reversible reaction is exothermic in the forward direction. Predict the energy change in the reverse direction.
- [✔︎] It is endothermic, and exactly the same amount of energy is transferred
- [ ] It is also exothermic, giving out energy both ways
    - *why wrong:* If the forward reaction gives out energy, the reverse must TAKE IN the same amount — it is endothermic.
- [ ] It is endothermic, but it takes in twice as much energy
    - *why wrong:* The energy transferred is the SAME size in both directions, not doubled.
- [ ] No energy change happens in the reverse direction
    - *why wrong:* The reverse direction transfers the same amount of energy as the forward, but in the opposite sense (endothermic).

**Q5. [apply · CFCHTFTH]** When blue hydrated copper(II) sulfate is heated it turns white; adding water turns it blue again. Explain why this is described as a reversible reaction.
- [✔︎] The change can be reversed — heating drives water off to form the white solid, and adding water reforms the blue solid
- [ ] Because heating always makes a reaction reversible
    - *why wrong:* Heating does not make reactions reversible; this one is reversible because the change can be undone by adding water.
- [ ] Because the copper sulfate is used up and cannot come back
    - *why wrong:* The copper sulfate is not used up — it changes back to blue when water is added, which is why it is reversible.
- [ ] Because a gas is given off when it is heated
    - *why wrong:* Giving off a gas does not make it reversible; it is reversible because adding water reforms the original blue solid.

**Q6. [recall · CFTF]** State the symbol used to show that a reaction is reversible.
- [✔︎] ⇌ (two half-arrows pointing in opposite directions)
- [ ] → (a single arrow pointing right)
    - *why wrong:* A single arrow shows a reaction that goes only one way; reversible reactions use ⇌.
- [ ] = (an equals sign)
    - *why wrong:* An equals sign is used in maths, not to show a reversible reaction; the symbol is ⇌.
- [ ] ↓ (a downward arrow)
    - *why wrong:* A downward arrow shows a precipitate forming; a reversible reaction is shown by ⇌.

**Q7. [recall · CFTF]** State what 'equilibrium' means in terms of the forward and reverse reaction rates.
- [✔︎] The forward and reverse reactions are happening at the same rate
- [ ] The forward reaction is faster than the reverse reaction
    - *why wrong:* At equilibrium the two rates are EQUAL; if the forward were faster it would not yet be at equilibrium.
- [ ] Both reactions have completely stopped
    - *why wrong:* The reactions have not stopped; they continue at equal rates.
- [ ] The reactants have all turned into products
    - *why wrong:* At equilibrium both reactants and products are present; the reactions simply proceed at equal rates.

**Q8. [apply · CFTF]** Identify what you would observe when blue hydrated copper(II) sulfate crystals are heated.
- [✔︎] The blue crystals turn white as water is driven off
- [ ] The blue crystals turn black
    - *why wrong:* Heating hydrated copper sulfate turns it WHITE (anhydrous), not black.
- [ ] The crystals stay blue but get bigger
    - *why wrong:* Heating drives off the water and turns the crystals white; they do not stay blue.
- [ ] The crystals dissolve into a colourless liquid
    - *why wrong:* No liquid forms; the water is driven off as vapour and the solid turns white.

**Q9. [recall · CFTF]** State what is meant by a 'closed system'.
- [✔︎] One in which no reactants or products can escape or be added
- [ ] One that is kept in the dark
    - *why wrong:* Light has nothing to do with it; a closed system is one where nothing can enter or leave.
- [ ] One that has no reactants left in it
    - *why wrong:* A closed system can be full of reactants; the point is that nothing can enter or leave it.
- [ ] One that is completely full of gas
    - *why wrong:* It does not have to be full of gas; a closed system simply prevents anything entering or leaving.

**Q10. [apply · CFTF]** Ammonium chloride ⇌ ammonia + hydrogen chloride is a reversible reaction. State what can happen to the products if they are trapped together in a closed tube.
- [✔︎] They can react together again to reform ammonium chloride
- [ ] They escape from the tube as gases
    - *why wrong:* In a CLOSED tube they cannot escape; instead they can recombine to reform ammonium chloride.
- [ ] They stay as ammonia and hydrogen chloride and never react again
    - *why wrong:* Because the reaction is reversible, the products can react back together to reform ammonium chloride.
- [ ] They turn into a completely different compound
    - *why wrong:* They reform the original reactant, ammonium chloride, because the reaction is reversible.

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Describe what is meant by a reversible reaction, using an example.
- [✔︎] One that can go both ways — the products can react to reform the reactants, e.g. hydrated copper(II) sulfate ⇌ anhydrous copper(II) sulfate + water
- [ ] One that gives out energy and then takes it back in at the end
    - *why wrong:* That describes energy transfer, not reversibility. A reversible reaction is one whose products can reform the reactants.
- [ ] One that can only go forwards but very quickly
    - *why wrong:* A reversible reaction goes BOTH ways; a reaction that only goes forwards is not reversible.
- [ ] One that produces a gas which then escapes
    - *why wrong:* Escaping gas is not what 'reversible' means; it means the products can react to reform the reactants.

**Q2. [reason · CFCHTFTH]** Explain what is meant by 'dynamic equilibrium' in a reversible reaction.
- [✔︎] The forward and reverse reactions are still happening, but at equal rates, so the concentrations of reactants and products stay constant
- [ ] Both reactions have stopped, so nothing changes
    - *why wrong:* The reactions have not stopped — they continue at EQUAL rates, which is why it is called dynamic.
- [ ] Only the forward reaction is happening, but very slowly
    - *why wrong:* At equilibrium both the forward and reverse reactions occur, at equal rates — not just the forward one.
- [ ] The reactants and products are present in exactly equal amounts
    - *why wrong:* 'Constant' does not mean 'equal' — the amounts stay steady but are usually not equal.

**Q3. [apply · CFCHTFTH]** State the condition a reversible reaction must be kept in for it to reach equilibrium.
- [✔︎] A closed system, where no reactants or products can enter or leave
- [ ] An open container, so gases can escape freely
    - *why wrong:* In an open container products escape and cannot react back, so equilibrium cannot be reached — it must be closed.
- [ ] A vacuum, with no air present
    - *why wrong:* It is not about air; the system must be CLOSED so nothing can enter or leave.
- [ ] A constantly heated flask
    - *why wrong:* Heating is not the requirement; the system must be closed so the reverse reaction can balance the forward one.

**Q4. [reason · CFCHTFTH]** A reversible reaction is exothermic in the forward direction. Predict the energy change in the reverse direction.
- [✔︎] It is endothermic, and exactly the same amount of energy is transferred
- [ ] It is also exothermic, giving out energy both ways
    - *why wrong:* If the forward reaction gives out energy, the reverse must TAKE IN the same amount — it is endothermic.
- [ ] It is endothermic, but it takes in twice as much energy
    - *why wrong:* The energy transferred is the SAME size in both directions, not doubled.
- [ ] No energy change happens in the reverse direction
    - *why wrong:* The reverse direction transfers the same amount of energy as the forward, but in the opposite sense (endothermic).

**Q5. [apply · CFCHTFTH]** When blue hydrated copper(II) sulfate is heated it turns white; adding water turns it blue again. Explain why this is described as a reversible reaction.
- [✔︎] The change can be reversed — heating drives water off to form the white solid, and adding water reforms the blue solid
- [ ] Because heating always makes a reaction reversible
    - *why wrong:* Heating does not make reactions reversible; this one is reversible because the change can be undone by adding water.
- [ ] Because the copper sulfate is used up and cannot come back
    - *why wrong:* The copper sulfate is not used up — it changes back to blue when water is added, which is why it is reversible.
- [ ] Because a gas is given off when it is heated
    - *why wrong:* Giving off a gas does not make it reversible; it is reversible because adding water reforms the original blue solid.

**Q6. [reason · CHTH]** Explain why a reversible reaction can only reach equilibrium in a closed system.
- [✔︎] In an open system some products escape and cannot react back, so the reverse reaction can never balance the forward reaction
- [ ] Because a closed system keeps the reaction warm enough to continue
    - *why wrong:* It is not about temperature; a closed system stops products escaping, so the reverse reaction can balance the forward one.
- [ ] Because a closed system has no reactants to begin with
    - *why wrong:* A closed system is full of reactants; being closed simply stops anything escaping so equilibrium can be established.
- [ ] Because equilibrium needs the pressure to keep rising
    - *why wrong:* Equilibrium does not need rising pressure; it needs a closed system so nothing enters or leaves.

**Q7. [reason · CHTH]** At equilibrium the concentrations are constant. Explain why this does NOT mean that the reactant and product concentrations are equal.
- [✔︎] 'Constant' means unchanging, not equal — the equilibrium can lie mostly towards the reactants or mostly towards the products, depending on the conditions
- [ ] They must be equal, because the two rates are equal
    - *why wrong:* Equal RATES do not mean equal AMOUNTS; the concentrations are steady but usually different.
- [ ] They are equal because the forward and reverse reactions cancel out
    - *why wrong:* The reactions balance in RATE, keeping amounts steady, but those steady amounts are usually not equal.
- [ ] They are always equal in a closed system
    - *why wrong:* A closed system keeps amounts constant, but constant does not mean equal — the position of equilibrium sets the amounts.

**Q8. [reason · CHTH]** Explain why equilibrium is described as 'dynamic' rather than 'static'.
- [✔︎] Both the forward and reverse reactions are still occurring (dynamic), just at equal rates — the reaction has not stopped
- [ ] Because the amounts of reactants and products keep changing
    - *why wrong:* The amounts stay constant at equilibrium; 'dynamic' refers to the reactions still occurring, not the amounts changing.
- [ ] Because the reaction moves the flask around as it goes
    - *why wrong:* 'Dynamic' refers to the ongoing forward and reverse reactions at the particle level, not any movement of the flask.
- [ ] Because the reaction has stopped but could restart
    - *why wrong:* The reactions have not stopped — they continue at equal rates, which is exactly why it is called dynamic.

**Q9. [apply · CHTH]** In a reversible reaction the forward reaction is exothermic. Explain what this tells you about the reverse reaction and why.
- [✔︎] The reverse reaction is endothermic by the same amount, because reversing a reaction reverses the direction of energy transfer and energy is conserved
- [ ] The reverse reaction is also exothermic, releasing energy both ways
    - *why wrong:* Energy cannot be released in both directions; if forward is exothermic, reverse must take the same energy back in (endothermic).
- [ ] The reverse reaction is endothermic but transfers a different amount of energy
    - *why wrong:* The amount of energy is the SAME in both directions; only the direction of transfer is reversed.
- [ ] The reverse reaction releases no energy at all
    - *why wrong:* The reverse reaction transfers the same amount of energy as the forward, but takes it in rather than gives it out.

**Q10. [reason · CHTH]** At the very start of a reversible reaction in a closed container, explain why the forward rate is high and the reverse rate is zero, and how these change until equilibrium is reached.
- [✔︎] At first there are only reactants (high forward rate) and no products (zero reverse rate); as products build up the reverse rate rises and the forward rate falls, until the two rates become equal at equilibrium
- [ ] The forward rate stays high and the reverse rate stays zero forever
    - *why wrong:* As products build up the reverse rate rises and the forward rate falls; they meet at equilibrium, so they do not stay fixed.
- [ ] Both rates start high and both fall to zero at equilibrium
    - *why wrong:* The reverse rate starts at zero (no products yet) and rises; at equilibrium the rates are equal but not zero.
- [ ] The reverse rate is high at first because there is plenty of reactant
    - *why wrong:* Reactant drives the FORWARD reaction; the reverse rate starts at zero because there is no product yet to react back.

### Triple Foundation — 12 questions (3 recall / 9 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Describe what is meant by a reversible reaction, using an example.
- [✔︎] One that can go both ways — the products can react to reform the reactants, e.g. hydrated copper(II) sulfate ⇌ anhydrous copper(II) sulfate + water
- [ ] One that gives out energy and then takes it back in at the end
    - *why wrong:* That describes energy transfer, not reversibility. A reversible reaction is one whose products can reform the reactants.
- [ ] One that can only go forwards but very quickly
    - *why wrong:* A reversible reaction goes BOTH ways; a reaction that only goes forwards is not reversible.
- [ ] One that produces a gas which then escapes
    - *why wrong:* Escaping gas is not what 'reversible' means; it means the products can react to reform the reactants.

**Q2. [reason · CFCHTFTH]** Explain what is meant by 'dynamic equilibrium' in a reversible reaction.
- [✔︎] The forward and reverse reactions are still happening, but at equal rates, so the concentrations of reactants and products stay constant
- [ ] Both reactions have stopped, so nothing changes
    - *why wrong:* The reactions have not stopped — they continue at EQUAL rates, which is why it is called dynamic.
- [ ] Only the forward reaction is happening, but very slowly
    - *why wrong:* At equilibrium both the forward and reverse reactions occur, at equal rates — not just the forward one.
- [ ] The reactants and products are present in exactly equal amounts
    - *why wrong:* 'Constant' does not mean 'equal' — the amounts stay steady but are usually not equal.

**Q3. [apply · CFCHTFTH]** State the condition a reversible reaction must be kept in for it to reach equilibrium.
- [✔︎] A closed system, where no reactants or products can enter or leave
- [ ] An open container, so gases can escape freely
    - *why wrong:* In an open container products escape and cannot react back, so equilibrium cannot be reached — it must be closed.
- [ ] A vacuum, with no air present
    - *why wrong:* It is not about air; the system must be CLOSED so nothing can enter or leave.
- [ ] A constantly heated flask
    - *why wrong:* Heating is not the requirement; the system must be closed so the reverse reaction can balance the forward one.

**Q4. [reason · CFCHTFTH]** A reversible reaction is exothermic in the forward direction. Predict the energy change in the reverse direction.
- [✔︎] It is endothermic, and exactly the same amount of energy is transferred
- [ ] It is also exothermic, giving out energy both ways
    - *why wrong:* If the forward reaction gives out energy, the reverse must TAKE IN the same amount — it is endothermic.
- [ ] It is endothermic, but it takes in twice as much energy
    - *why wrong:* The energy transferred is the SAME size in both directions, not doubled.
- [ ] No energy change happens in the reverse direction
    - *why wrong:* The reverse direction transfers the same amount of energy as the forward, but in the opposite sense (endothermic).

**Q5. [apply · CFCHTFTH]** When blue hydrated copper(II) sulfate is heated it turns white; adding water turns it blue again. Explain why this is described as a reversible reaction.
- [✔︎] The change can be reversed — heating drives water off to form the white solid, and adding water reforms the blue solid
- [ ] Because heating always makes a reaction reversible
    - *why wrong:* Heating does not make reactions reversible; this one is reversible because the change can be undone by adding water.
- [ ] Because the copper sulfate is used up and cannot come back
    - *why wrong:* The copper sulfate is not used up — it changes back to blue when water is added, which is why it is reversible.
- [ ] Because a gas is given off when it is heated
    - *why wrong:* Giving off a gas does not make it reversible; it is reversible because adding water reforms the original blue solid.

**Q6. [recall · CFTF]** State the symbol used to show that a reaction is reversible.
- [✔︎] ⇌ (two half-arrows pointing in opposite directions)
- [ ] → (a single arrow pointing right)
    - *why wrong:* A single arrow shows a reaction that goes only one way; reversible reactions use ⇌.
- [ ] = (an equals sign)
    - *why wrong:* An equals sign is used in maths, not to show a reversible reaction; the symbol is ⇌.
- [ ] ↓ (a downward arrow)
    - *why wrong:* A downward arrow shows a precipitate forming; a reversible reaction is shown by ⇌.

**Q7. [recall · CFTF]** State what 'equilibrium' means in terms of the forward and reverse reaction rates.
- [✔︎] The forward and reverse reactions are happening at the same rate
- [ ] The forward reaction is faster than the reverse reaction
    - *why wrong:* At equilibrium the two rates are EQUAL; if the forward were faster it would not yet be at equilibrium.
- [ ] Both reactions have completely stopped
    - *why wrong:* The reactions have not stopped; they continue at equal rates.
- [ ] The reactants have all turned into products
    - *why wrong:* At equilibrium both reactants and products are present; the reactions simply proceed at equal rates.

**Q8. [apply · CFTF]** Identify what you would observe when blue hydrated copper(II) sulfate crystals are heated.
- [✔︎] The blue crystals turn white as water is driven off
- [ ] The blue crystals turn black
    - *why wrong:* Heating hydrated copper sulfate turns it WHITE (anhydrous), not black.
- [ ] The crystals stay blue but get bigger
    - *why wrong:* Heating drives off the water and turns the crystals white; they do not stay blue.
- [ ] The crystals dissolve into a colourless liquid
    - *why wrong:* No liquid forms; the water is driven off as vapour and the solid turns white.

**Q9. [recall · CFTF]** State what is meant by a 'closed system'.
- [✔︎] One in which no reactants or products can escape or be added
- [ ] One that is kept in the dark
    - *why wrong:* Light has nothing to do with it; a closed system is one where nothing can enter or leave.
- [ ] One that has no reactants left in it
    - *why wrong:* A closed system can be full of reactants; the point is that nothing can enter or leave it.
- [ ] One that is completely full of gas
    - *why wrong:* It does not have to be full of gas; a closed system simply prevents anything entering or leaving.

**Q10. [apply · CFTF]** Ammonium chloride ⇌ ammonia + hydrogen chloride is a reversible reaction. State what can happen to the products if they are trapped together in a closed tube.
- [✔︎] They can react together again to reform ammonium chloride
- [ ] They escape from the tube as gases
    - *why wrong:* In a CLOSED tube they cannot escape; instead they can recombine to reform ammonium chloride.
- [ ] They stay as ammonia and hydrogen chloride and never react again
    - *why wrong:* Because the reaction is reversible, the products can react back together to reform ammonium chloride.
- [ ] They turn into a completely different compound
    - *why wrong:* They reform the original reactant, ammonium chloride, because the reaction is reversible.

**Q11. [apply · TF]** Explain why the amounts of reactants and products stay constant once a reversible reaction has reached equilibrium.
- [✔︎] The forward and reverse reactions are happening at the same rate, so as fast as products form they are turned back into reactants
- [ ] The reaction has stopped, so nothing can change
    - *why wrong:* The reactions have not stopped; they continue at equal rates, which keeps the amounts constant.
- [ ] All the reactants have been used up, leaving only products
    - *why wrong:* Both reactants and products are still present; the amounts stay constant because the two rates are equal.
- [ ] The products escape as fast as they form
    - *why wrong:* In a closed system nothing escapes; the amounts stay constant because the forward and reverse rates are equal.

**Q12. [apply · TF]** A reversible reaction is endothermic in the forward direction. State whether the forward or reverse reaction takes in energy, and how much energy the reverse reaction gives out.
- [✔︎] The forward reaction takes in energy; the reverse reaction gives out the same amount of energy
- [ ] The reverse reaction takes in energy; the forward gives it out
    - *why wrong:* It is the forward reaction that is endothermic (takes in energy); the reverse gives out the same amount.
- [ ] Both directions take in energy
    - *why wrong:* Energy cannot be taken in both ways; if the forward takes energy in, the reverse gives the same amount out.
- [ ] The reverse reaction gives out twice as much energy as the forward takes in
    - *why wrong:* The energy is the SAME size in both directions, not doubled.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [apply · CFCHTFTH]** Describe what is meant by a reversible reaction, using an example.
- [✔︎] One that can go both ways — the products can react to reform the reactants, e.g. hydrated copper(II) sulfate ⇌ anhydrous copper(II) sulfate + water
- [ ] One that gives out energy and then takes it back in at the end
    - *why wrong:* That describes energy transfer, not reversibility. A reversible reaction is one whose products can reform the reactants.
- [ ] One that can only go forwards but very quickly
    - *why wrong:* A reversible reaction goes BOTH ways; a reaction that only goes forwards is not reversible.
- [ ] One that produces a gas which then escapes
    - *why wrong:* Escaping gas is not what 'reversible' means; it means the products can react to reform the reactants.

**Q2. [reason · CFCHTFTH]** Explain what is meant by 'dynamic equilibrium' in a reversible reaction.
- [✔︎] The forward and reverse reactions are still happening, but at equal rates, so the concentrations of reactants and products stay constant
- [ ] Both reactions have stopped, so nothing changes
    - *why wrong:* The reactions have not stopped — they continue at EQUAL rates, which is why it is called dynamic.
- [ ] Only the forward reaction is happening, but very slowly
    - *why wrong:* At equilibrium both the forward and reverse reactions occur, at equal rates — not just the forward one.
- [ ] The reactants and products are present in exactly equal amounts
    - *why wrong:* 'Constant' does not mean 'equal' — the amounts stay steady but are usually not equal.

**Q3. [apply · CFCHTFTH]** State the condition a reversible reaction must be kept in for it to reach equilibrium.
- [✔︎] A closed system, where no reactants or products can enter or leave
- [ ] An open container, so gases can escape freely
    - *why wrong:* In an open container products escape and cannot react back, so equilibrium cannot be reached — it must be closed.
- [ ] A vacuum, with no air present
    - *why wrong:* It is not about air; the system must be CLOSED so nothing can enter or leave.
- [ ] A constantly heated flask
    - *why wrong:* Heating is not the requirement; the system must be closed so the reverse reaction can balance the forward one.

**Q4. [reason · CFCHTFTH]** A reversible reaction is exothermic in the forward direction. Predict the energy change in the reverse direction.
- [✔︎] It is endothermic, and exactly the same amount of energy is transferred
- [ ] It is also exothermic, giving out energy both ways
    - *why wrong:* If the forward reaction gives out energy, the reverse must TAKE IN the same amount — it is endothermic.
- [ ] It is endothermic, but it takes in twice as much energy
    - *why wrong:* The energy transferred is the SAME size in both directions, not doubled.
- [ ] No energy change happens in the reverse direction
    - *why wrong:* The reverse direction transfers the same amount of energy as the forward, but in the opposite sense (endothermic).

**Q5. [apply · CFCHTFTH]** When blue hydrated copper(II) sulfate is heated it turns white; adding water turns it blue again. Explain why this is described as a reversible reaction.
- [✔︎] The change can be reversed — heating drives water off to form the white solid, and adding water reforms the blue solid
- [ ] Because heating always makes a reaction reversible
    - *why wrong:* Heating does not make reactions reversible; this one is reversible because the change can be undone by adding water.
- [ ] Because the copper sulfate is used up and cannot come back
    - *why wrong:* The copper sulfate is not used up — it changes back to blue when water is added, which is why it is reversible.
- [ ] Because a gas is given off when it is heated
    - *why wrong:* Giving off a gas does not make it reversible; it is reversible because adding water reforms the original blue solid.

**Q6. [reason · CHTH]** Explain why a reversible reaction can only reach equilibrium in a closed system.
- [✔︎] In an open system some products escape and cannot react back, so the reverse reaction can never balance the forward reaction
- [ ] Because a closed system keeps the reaction warm enough to continue
    - *why wrong:* It is not about temperature; a closed system stops products escaping, so the reverse reaction can balance the forward one.
- [ ] Because a closed system has no reactants to begin with
    - *why wrong:* A closed system is full of reactants; being closed simply stops anything escaping so equilibrium can be established.
- [ ] Because equilibrium needs the pressure to keep rising
    - *why wrong:* Equilibrium does not need rising pressure; it needs a closed system so nothing enters or leaves.

**Q7. [reason · CHTH]** At equilibrium the concentrations are constant. Explain why this does NOT mean that the reactant and product concentrations are equal.
- [✔︎] 'Constant' means unchanging, not equal — the equilibrium can lie mostly towards the reactants or mostly towards the products, depending on the conditions
- [ ] They must be equal, because the two rates are equal
    - *why wrong:* Equal RATES do not mean equal AMOUNTS; the concentrations are steady but usually different.
- [ ] They are equal because the forward and reverse reactions cancel out
    - *why wrong:* The reactions balance in RATE, keeping amounts steady, but those steady amounts are usually not equal.
- [ ] They are always equal in a closed system
    - *why wrong:* A closed system keeps amounts constant, but constant does not mean equal — the position of equilibrium sets the amounts.

**Q8. [reason · CHTH]** Explain why equilibrium is described as 'dynamic' rather than 'static'.
- [✔︎] Both the forward and reverse reactions are still occurring (dynamic), just at equal rates — the reaction has not stopped
- [ ] Because the amounts of reactants and products keep changing
    - *why wrong:* The amounts stay constant at equilibrium; 'dynamic' refers to the reactions still occurring, not the amounts changing.
- [ ] Because the reaction moves the flask around as it goes
    - *why wrong:* 'Dynamic' refers to the ongoing forward and reverse reactions at the particle level, not any movement of the flask.
- [ ] Because the reaction has stopped but could restart
    - *why wrong:* The reactions have not stopped — they continue at equal rates, which is exactly why it is called dynamic.

**Q9. [apply · CHTH]** In a reversible reaction the forward reaction is exothermic. Explain what this tells you about the reverse reaction and why.
- [✔︎] The reverse reaction is endothermic by the same amount, because reversing a reaction reverses the direction of energy transfer and energy is conserved
- [ ] The reverse reaction is also exothermic, releasing energy both ways
    - *why wrong:* Energy cannot be released in both directions; if forward is exothermic, reverse must take the same energy back in (endothermic).
- [ ] The reverse reaction is endothermic but transfers a different amount of energy
    - *why wrong:* The amount of energy is the SAME in both directions; only the direction of transfer is reversed.
- [ ] The reverse reaction releases no energy at all
    - *why wrong:* The reverse reaction transfers the same amount of energy as the forward, but takes it in rather than gives it out.

**Q10. [reason · CHTH]** At the very start of a reversible reaction in a closed container, explain why the forward rate is high and the reverse rate is zero, and how these change until equilibrium is reached.
- [✔︎] At first there are only reactants (high forward rate) and no products (zero reverse rate); as products build up the reverse rate rises and the forward rate falls, until the two rates become equal at equilibrium
- [ ] The forward rate stays high and the reverse rate stays zero forever
    - *why wrong:* As products build up the reverse rate rises and the forward rate falls; they meet at equilibrium, so they do not stay fixed.
- [ ] Both rates start high and both fall to zero at equilibrium
    - *why wrong:* The reverse rate starts at zero (no products yet) and rises; at equilibrium the rates are equal but not zero.
- [ ] The reverse rate is high at first because there is plenty of reactant
    - *why wrong:* Reactant drives the FORWARD reaction; the reverse rate starts at zero because there is no product yet to react back.

**Q11. [apply · TH]** In the reaction N₂ + 3H₂ ⇌ 2NH₃ in a sealed vessel at equilibrium, explain why nitrogen, hydrogen and ammonia are all still present and their amounts no longer change.
- [✔︎] At equilibrium the forward and reverse reactions continue at equal rates, so all three gases remain present but their concentrations stay constant
- [ ] Because the reaction has stopped now that all three gases are present
    - *why wrong:* The reactions have not stopped; they continue at equal rates, which is what keeps the amounts constant.
- [ ] Because the nitrogen and hydrogen have been completely used up
    - *why wrong:* The nitrogen and hydrogen are not used up — all three gases are present because a dynamic equilibrium has been reached.
- [ ] Because ammonia cannot react back into nitrogen and hydrogen
    - *why wrong:* Ammonia does react back (the reverse reaction); at equilibrium the forward and reverse rates are simply equal.

**Q12. [reason · TH]** Explain why, once equilibrium has been reached in a closed system, the total mass of the system stays the same even though the forward and reverse reactions are still happening.
- [✔︎] Nothing enters or leaves the closed system and atoms are conserved, so the total mass is constant even though particles keep changing from reactants to products and back
- [ ] Because the reactions have stopped, so no mass can change
    - *why wrong:* The reactions continue at equal rates; the mass is constant because the system is closed and atoms are conserved.
- [ ] Because equal masses of reactants and products are always present
    - *why wrong:* The masses need not be equal; the TOTAL mass is constant because nothing enters or leaves and atoms are conserved.
- [ ] Because the gases escape at the same rate that they form
    - *why wrong:* In a closed system nothing escapes; the mass stays constant because all the atoms remain inside it.

---

## Effect of Changing Conditions on Equilibrium  ·  `effect-of-conditions-equilibrium`  ·  AQA 5.6.2.4–5.6.2.7

> 🚩 **Triple-depth call (your review):** HIGHER-ONLY — AQA 5.6.2.4–5.6.2.7 (Le Chatelier's principle) is Higher-tier content, present in BOTH Combined-Higher and Triple-Higher. There is no Foundation cell for this page. Triple-Higher = the exact Combined-Higher set + 2 extra Higher/depth questions.

**Common Mistake (mistake-first, three-beat):**

> Students often think that raising the temperature always increases the yield of a reversible reaction, because reactions go faster when they are hotter. This confuses the RATE of the reaction with the POSITION of equilibrium. Raising the temperature does speed the reaction up, but it also shifts the equilibrium in the endothermic direction — so for an exothermic forward reaction (like making ammonia) a higher temperature actually LOWERS the yield. Reaching equilibrium faster is not the same as making more product.

**Question sets by tier** (each item shows the tiers it appears in; ⭐ = full-review flag):

### Combined Higher — 10 questions (0 recall / 10 apply+reason+calc)

**Q1. [apply · CHTH]** State Le Chatelier's principle.
- [✔︎] If a change is made to a system at equilibrium, the position of equilibrium shifts to oppose (counteract) that change
- [ ] If a change is made, the equilibrium shifts to make the change bigger
    - *why wrong:* The equilibrium shifts to OPPOSE the change, reducing its effect — not to make it bigger.
- [ ] If a change is made, the reaction stops until conditions return to normal
    - *why wrong:* The reaction does not stop; the position of equilibrium shifts to counteract the change.
- [ ] The forward and reverse reactions always occur at different rates
    - *why wrong:* That is not Le Chatelier's principle; the principle is about how the equilibrium position responds to a change.

**Q2. [apply · CHTH]** Predict the effect on the position of equilibrium of increasing the concentration of a reactant, and explain.
- [✔︎] The equilibrium shifts towards the products (to the right) to use up the added reactant
- [ ] It shifts towards the reactants to make more of what was added
    - *why wrong:* The equilibrium shifts to OPPOSE the change, i.e. it uses up the added reactant by moving towards the products.
- [ ] It does not move, because concentration has no effect on equilibrium
    - *why wrong:* Concentration does affect the position; adding reactant shifts the equilibrium towards the products.
- [ ] The reaction stops because there is now too much reactant
    - *why wrong:* The reaction does not stop; it shifts towards the products to use up the extra reactant.

**Q3. [apply · CHTH]** For a reaction that is exothermic in the forward direction, predict the effect of increasing the temperature on the yield of product, and explain.
- [✔︎] The yield falls — the equilibrium shifts in the endothermic (reverse) direction to oppose the temperature rise
- [ ] The yield rises — heating always speeds up the forward reaction more
    - *why wrong:* For an exothermic forward reaction, heating shifts the equilibrium the REVERSE (endothermic) way, so the yield falls.
- [ ] The yield is unchanged — temperature does not affect the position of equilibrium
    - *why wrong:* Temperature does affect the position; raising it shifts an exothermic equilibrium backwards, lowering the yield.
- [ ] The yield rises because the equilibrium shifts in the exothermic direction
    - *why wrong:* Raising the temperature shifts the equilibrium in the ENDOTHERMIC direction (here, the reverse), so the yield falls.

**Q4. [apply · CHTH]** For N₂ + 3H₂ ⇌ 2NH₃ (4 moles of gas on the left, 2 moles on the right), predict the effect of increasing the pressure on the amount of ammonia, and explain.
- [✔︎] More ammonia forms — the equilibrium shifts towards the side with fewer moles of gas (the products)
- [ ] Less ammonia forms — high pressure favours the side with more gas moles
    - *why wrong:* The equilibrium shifts to the side with FEWER gas moles to oppose the pressure rise; here that is the ammonia side.
- [ ] The amount of ammonia is unchanged — pressure does not affect equilibrium
    - *why wrong:* Because the two sides have different numbers of gas moles, pressure does shift this equilibrium — towards the ammonia.
- [ ] More ammonia forms because pressure speeds up the forward reaction only
    - *why wrong:* Higher pressure shifts the POSITION towards fewer gas moles; it is not simply that the forward reaction is sped up.

**Q5. [reason · CHTH]** Explain why adding a catalyst does not change the position of equilibrium.
- [✔︎] A catalyst speeds up the forward and reverse reactions equally, so equilibrium is reached faster but its position (and the yield) is unchanged
- [ ] A catalyst speeds up only the forward reaction, so it shifts the equilibrium to the products
    - *why wrong:* A catalyst speeds up BOTH directions equally, so the position of equilibrium does not move.
- [ ] A catalyst shifts the equilibrium towards the side with fewer gas moles
    - *why wrong:* That is the effect of pressure, not a catalyst; a catalyst leaves the position of equilibrium unchanged.
- [ ] A catalyst raises the yield by lowering the activation energy
    - *why wrong:* Lowering the activation energy only speeds the reaction up; it does not change the position of equilibrium or the yield.

**Q6. [apply · CHTH]** Predict the effect of continuously removing a product as it forms on the position of equilibrium.
- [✔︎] The equilibrium keeps shifting towards the products to replace what was removed, which increases the yield
- [ ] The equilibrium shifts towards the reactants
    - *why wrong:* Removing a product shifts the equilibrium TOWARDS the products (to replace it), not towards the reactants.
- [ ] The reaction stops because a product is missing
    - *why wrong:* The reaction does not stop; it shifts towards the products to replace the removed product.
- [ ] There is no effect, because only adding substances changes equilibrium
    - *why wrong:* Removing a substance also shifts the equilibrium — here it moves towards the products to replace what was taken out.

**Q7. [reason · CHTH]** For a reaction that is endothermic in the forward direction, explain how lowering the temperature affects the yield of product.
- [✔︎] The yield falls — the equilibrium shifts in the exothermic (reverse) direction to release energy and oppose the cooling
- [ ] The yield rises, because cooling always favours the forward reaction
    - *why wrong:* For an endothermic forward reaction, cooling shifts the equilibrium the REVERSE (exothermic) way, so the yield falls.
- [ ] The yield is unchanged, because temperature does not move this equilibrium
    - *why wrong:* Temperature does move it; cooling an endothermic-forward reaction shifts it backwards, lowering the yield.
- [ ] The yield rises, because the equilibrium shifts in the endothermic direction
    - *why wrong:* Cooling shifts the equilibrium in the EXOTHERMIC direction (here, the reverse), so the yield falls.

**Q8. [apply · CHTH]** In a gas-phase reaction where the reactants and products have equal numbers of moles of gas, predict the effect of changing the pressure on the position of equilibrium.
- [✔︎] There is no effect — pressure only shifts the equilibrium when the two sides have different numbers of moles of gas
- [ ] The equilibrium always shifts towards the products when pressure rises
    - *why wrong:* Only when the sides differ in gas moles; with equal moles on each side, pressure has no effect.
- [ ] The equilibrium shifts towards the reactants
    - *why wrong:* With equal gas moles on both sides there is no side with fewer moles, so pressure does not shift the equilibrium.
- [ ] The reaction stops when the pressure is changed
    - *why wrong:* The reaction does not stop; with equal gas moles on both sides, changing the pressure simply has no effect on the position.

**Q9. [reason · CHTH]** Explain, in terms of the forward and reverse rates, why increasing the concentration of a reactant shifts the equilibrium to the right.
- [✔︎] Adding reactant speeds up the forward reaction, so it temporarily exceeds the reverse rate; the position shifts right until the two rates become equal again
- [ ] Adding reactant speeds up the reverse reaction, shifting it left
    - *why wrong:* Extra reactant speeds up the FORWARD reaction, so the equilibrium shifts right, not left.
- [ ] Adding reactant stops the reverse reaction completely
    - *why wrong:* The reverse reaction does not stop; the forward simply becomes temporarily faster until the rates re-balance.
- [ ] Adding reactant has no effect on either rate
    - *why wrong:* Extra reactant increases the forward rate, which is why the equilibrium shifts towards the products.

**Q10. [reason · CHTH]** The percentage yield of ammonia in the Haber process is higher at low temperature, but the reaction is then very slow. Explain this compromise in terms of equilibrium and rate.
- [✔︎] A low temperature gives a higher equilibrium yield (the exothermic forward reaction is favoured) but too slow a rate, so a moderate temperature is used as a compromise between yield and speed
- [ ] A low temperature gives both the highest yield and the fastest rate
    - *why wrong:* A low temperature gives a higher yield but a SLOWER rate; that is exactly why a compromise temperature is needed.
- [ ] A high temperature is used because it gives the highest yield of ammonia
    - *why wrong:* A high temperature lowers the yield (exothermic forward); a moderate temperature balances yield against a workable rate.
- [ ] Temperature affects only the rate, so the yield is the same at any temperature
    - *why wrong:* Temperature affects both: it changes the equilibrium yield as well as the rate, which is why a compromise is chosen.

### Triple Higher — 12 questions (0 recall / 12 apply+reason+calc)

**Q1. [apply · CHTH]** State Le Chatelier's principle.
- [✔︎] If a change is made to a system at equilibrium, the position of equilibrium shifts to oppose (counteract) that change
- [ ] If a change is made, the equilibrium shifts to make the change bigger
    - *why wrong:* The equilibrium shifts to OPPOSE the change, reducing its effect — not to make it bigger.
- [ ] If a change is made, the reaction stops until conditions return to normal
    - *why wrong:* The reaction does not stop; the position of equilibrium shifts to counteract the change.
- [ ] The forward and reverse reactions always occur at different rates
    - *why wrong:* That is not Le Chatelier's principle; the principle is about how the equilibrium position responds to a change.

**Q2. [apply · CHTH]** Predict the effect on the position of equilibrium of increasing the concentration of a reactant, and explain.
- [✔︎] The equilibrium shifts towards the products (to the right) to use up the added reactant
- [ ] It shifts towards the reactants to make more of what was added
    - *why wrong:* The equilibrium shifts to OPPOSE the change, i.e. it uses up the added reactant by moving towards the products.
- [ ] It does not move, because concentration has no effect on equilibrium
    - *why wrong:* Concentration does affect the position; adding reactant shifts the equilibrium towards the products.
- [ ] The reaction stops because there is now too much reactant
    - *why wrong:* The reaction does not stop; it shifts towards the products to use up the extra reactant.

**Q3. [apply · CHTH]** For a reaction that is exothermic in the forward direction, predict the effect of increasing the temperature on the yield of product, and explain.
- [✔︎] The yield falls — the equilibrium shifts in the endothermic (reverse) direction to oppose the temperature rise
- [ ] The yield rises — heating always speeds up the forward reaction more
    - *why wrong:* For an exothermic forward reaction, heating shifts the equilibrium the REVERSE (endothermic) way, so the yield falls.
- [ ] The yield is unchanged — temperature does not affect the position of equilibrium
    - *why wrong:* Temperature does affect the position; raising it shifts an exothermic equilibrium backwards, lowering the yield.
- [ ] The yield rises because the equilibrium shifts in the exothermic direction
    - *why wrong:* Raising the temperature shifts the equilibrium in the ENDOTHERMIC direction (here, the reverse), so the yield falls.

**Q4. [apply · CHTH]** For N₂ + 3H₂ ⇌ 2NH₃ (4 moles of gas on the left, 2 moles on the right), predict the effect of increasing the pressure on the amount of ammonia, and explain.
- [✔︎] More ammonia forms — the equilibrium shifts towards the side with fewer moles of gas (the products)
- [ ] Less ammonia forms — high pressure favours the side with more gas moles
    - *why wrong:* The equilibrium shifts to the side with FEWER gas moles to oppose the pressure rise; here that is the ammonia side.
- [ ] The amount of ammonia is unchanged — pressure does not affect equilibrium
    - *why wrong:* Because the two sides have different numbers of gas moles, pressure does shift this equilibrium — towards the ammonia.
- [ ] More ammonia forms because pressure speeds up the forward reaction only
    - *why wrong:* Higher pressure shifts the POSITION towards fewer gas moles; it is not simply that the forward reaction is sped up.

**Q5. [reason · CHTH]** Explain why adding a catalyst does not change the position of equilibrium.
- [✔︎] A catalyst speeds up the forward and reverse reactions equally, so equilibrium is reached faster but its position (and the yield) is unchanged
- [ ] A catalyst speeds up only the forward reaction, so it shifts the equilibrium to the products
    - *why wrong:* A catalyst speeds up BOTH directions equally, so the position of equilibrium does not move.
- [ ] A catalyst shifts the equilibrium towards the side with fewer gas moles
    - *why wrong:* That is the effect of pressure, not a catalyst; a catalyst leaves the position of equilibrium unchanged.
- [ ] A catalyst raises the yield by lowering the activation energy
    - *why wrong:* Lowering the activation energy only speeds the reaction up; it does not change the position of equilibrium or the yield.

**Q6. [apply · CHTH]** Predict the effect of continuously removing a product as it forms on the position of equilibrium.
- [✔︎] The equilibrium keeps shifting towards the products to replace what was removed, which increases the yield
- [ ] The equilibrium shifts towards the reactants
    - *why wrong:* Removing a product shifts the equilibrium TOWARDS the products (to replace it), not towards the reactants.
- [ ] The reaction stops because a product is missing
    - *why wrong:* The reaction does not stop; it shifts towards the products to replace the removed product.
- [ ] There is no effect, because only adding substances changes equilibrium
    - *why wrong:* Removing a substance also shifts the equilibrium — here it moves towards the products to replace what was taken out.

**Q7. [reason · CHTH]** For a reaction that is endothermic in the forward direction, explain how lowering the temperature affects the yield of product.
- [✔︎] The yield falls — the equilibrium shifts in the exothermic (reverse) direction to release energy and oppose the cooling
- [ ] The yield rises, because cooling always favours the forward reaction
    - *why wrong:* For an endothermic forward reaction, cooling shifts the equilibrium the REVERSE (exothermic) way, so the yield falls.
- [ ] The yield is unchanged, because temperature does not move this equilibrium
    - *why wrong:* Temperature does move it; cooling an endothermic-forward reaction shifts it backwards, lowering the yield.
- [ ] The yield rises, because the equilibrium shifts in the endothermic direction
    - *why wrong:* Cooling shifts the equilibrium in the EXOTHERMIC direction (here, the reverse), so the yield falls.

**Q8. [apply · CHTH]** In a gas-phase reaction where the reactants and products have equal numbers of moles of gas, predict the effect of changing the pressure on the position of equilibrium.
- [✔︎] There is no effect — pressure only shifts the equilibrium when the two sides have different numbers of moles of gas
- [ ] The equilibrium always shifts towards the products when pressure rises
    - *why wrong:* Only when the sides differ in gas moles; with equal moles on each side, pressure has no effect.
- [ ] The equilibrium shifts towards the reactants
    - *why wrong:* With equal gas moles on both sides there is no side with fewer moles, so pressure does not shift the equilibrium.
- [ ] The reaction stops when the pressure is changed
    - *why wrong:* The reaction does not stop; with equal gas moles on both sides, changing the pressure simply has no effect on the position.

**Q9. [reason · CHTH]** Explain, in terms of the forward and reverse rates, why increasing the concentration of a reactant shifts the equilibrium to the right.
- [✔︎] Adding reactant speeds up the forward reaction, so it temporarily exceeds the reverse rate; the position shifts right until the two rates become equal again
- [ ] Adding reactant speeds up the reverse reaction, shifting it left
    - *why wrong:* Extra reactant speeds up the FORWARD reaction, so the equilibrium shifts right, not left.
- [ ] Adding reactant stops the reverse reaction completely
    - *why wrong:* The reverse reaction does not stop; the forward simply becomes temporarily faster until the rates re-balance.
- [ ] Adding reactant has no effect on either rate
    - *why wrong:* Extra reactant increases the forward rate, which is why the equilibrium shifts towards the products.

**Q10. [reason · CHTH]** The percentage yield of ammonia in the Haber process is higher at low temperature, but the reaction is then very slow. Explain this compromise in terms of equilibrium and rate.
- [✔︎] A low temperature gives a higher equilibrium yield (the exothermic forward reaction is favoured) but too slow a rate, so a moderate temperature is used as a compromise between yield and speed
- [ ] A low temperature gives both the highest yield and the fastest rate
    - *why wrong:* A low temperature gives a higher yield but a SLOWER rate; that is exactly why a compromise temperature is needed.
- [ ] A high temperature is used because it gives the highest yield of ammonia
    - *why wrong:* A high temperature lowers the yield (exothermic forward); a moderate temperature balances yield against a workable rate.
- [ ] Temperature affects only the rate, so the yield is the same at any temperature
    - *why wrong:* Temperature affects both: it changes the equilibrium yield as well as the rate, which is why a compromise is chosen.

**Q11. [apply · TH]** In the Haber process a pressure of about 200 atmospheres is used. Explain, using Le Chatelier's principle, why a high pressure increases the yield of ammonia in N₂ + 3H₂ ⇌ 2NH₃.
- [✔︎] The forward reaction goes from 4 moles of gas to 2 moles, so a high pressure shifts the equilibrium towards the side with fewer gas moles (the ammonia), increasing the yield
- [ ] High pressure shifts the equilibrium towards the 4 moles of reactant gas
    - *why wrong:* The equilibrium shifts to the side with FEWER gas moles (2, the ammonia), not the side with more.
- [ ] High pressure speeds up the forward reaction, so more ammonia is made overall
    - *why wrong:* High pressure raises the yield by shifting the POSITION towards fewer gas moles, not just by changing the rate.
- [ ] High pressure has no effect because ammonia is a gas like the reactants
    - *why wrong:* Because the two sides differ in the number of gas moles, pressure does shift the equilibrium — towards the ammonia.

**Q12. [reason · TH]** Increasing the pressure raises the yield of ammonia, yet even higher pressures are not used in industry. Suggest why.
- [✔︎] Very high pressures are expensive and dangerous — they need strong, costly equipment and a lot of energy to compress the gases — so a compromise pressure is used
- [ ] Higher pressures would lower the yield of ammonia
    - *why wrong:* Higher pressure would actually raise the yield further; it is avoided because of cost and safety, not yield.
- [ ] Higher pressures would stop the reaction from reaching equilibrium
    - *why wrong:* Higher pressure does not prevent equilibrium; it is avoided because of the cost and danger of the equipment.
- [ ] Higher pressures are not used because they slow the reaction down
    - *why wrong:* Higher pressure does not slow the reaction; it is avoided because of the expense and safety risks of very high pressures.

---
