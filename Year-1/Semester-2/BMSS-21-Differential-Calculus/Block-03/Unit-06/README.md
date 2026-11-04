# Envelope of a Family of Curves

This README summarizes study notes on the **envelope** of a family of curves. It explains what an envelope is, states the necessary and sufficient condition for its existence, derives the general elimination method for one-parameter families, covers the special quadratic-in-parameter shortcut, and extends the method to two-parameter families linked by a side condition. Worked examples and a self-audit are included.

## Table of Contents

1. [Notes](#notes)
   - [Overview](#overview)
   - [Mathematical Foundation](#mathematical-foundation)
   - [Derivation of the General Method](#derivation-of-the-general-method)
   - [Key Observations](#key-observations)
2. [Historical Background](#historical-background)
3. [Real-World Applications](#real-world-applications)
4. [Self-Audit](#self-audit)

## Notes

### Overview

An **envelope** is a single curve that touches every member of a family of curves, with each point of the envelope being the point of contact with some member of the family. The technique matters because it converts a parametrized family into one boundary curve that captures the family's outer reach.

- It reduces an infinite family of curves to one curve that bounds or wraps the family.
- It identifies the locus of points where neighbouring members of the family meet.
- It gives a direct route from a parameter-dependent equation to a single implicit curve.
- It extends naturally to families with two parameters tied by a side condition.

### Mathematical Foundation

A **one-parameter family of curves** is written as f(x, y, α) = 0, where α is the parameter.

> **Definition 6.1.** A curve K which touches each member of the family of curves C and at each point on K is touched by some member of the family C is called the envelope.

> **Necessary and sufficient condition:** For the family f(x, y, α) = 0, the envelope is obtained from ∂f/∂α = 0.

> **Note 6.1.** Eliminate α between f(x, y, α) = 0 and ∂f/∂α = 0.

For the special case where the parameter appears quadratically,

> aα² + bα + c = 0

with a, b, c functions of x and y, the envelope condition is

> **b² − 4ac = 0**

For a **two-parameter family** f(x, y, α, β) = 0 with a side relation φ(α, β) = 0, differentiate both relations partially with respect to α, treating β as a function of α:

> ∂f/∂α + (∂f/∂β)(∂β/∂α) = 0
> ∂φ/∂α + (∂φ/∂β)(∂β/∂α) = 0

Then eliminate α, β and ∂β/∂α from the four relations to obtain the envelope.

### Derivation of the General Method

#### For a one-parameter family

Step 1. Start with the family equation.

> f(x, y, α) = 0

Step 2. Differentiate partially with respect to the parameter α.

> ∂f/∂α = 0

Step 3. Eliminate α between the two equations. The resulting relation in x and y alone is the envelope.

Worked check — family of lines x cos α + y sin α = p:

> x cos α + y sin α = p
> −x sin α + y cos α = 0

Squaring and adding eliminates the cross terms because cos²α + sin²α = 1:

> (x cos α + y sin α)² + (−x sin α + y cos α)² = p²
> x²(cos²α + sin²α) + y²(cos²α + sin²α) = p²
> x² + y² = p²

So the envelope is the circle x² + y² = p².

#### For the quadratic-in-parameter case

Step 1. Write the family as a quadratic in the parameter.

> aα² + bα + c = 0

Step 2. Differentiate with respect to α.

> 2aα + b = 0, so α = −b/(2a)

Step 3. Substitute back into the quadratic.

> a·(b²/(4a²)) + b·(−b/(2a)) + c = 0
> b²/(4a) − b²/(2a) + c = 0
> b² − 4ac = 0

Worked check — family y = mx + a/m:

> my = m²x + a, so m²x − my + a = 0

Here a = x, b = −y, c = a in the coefficient sense, so

> y² − 4ax = 0, i.e. y² = 4ax

which is the parabola that is the envelope.

#### For a two-parameter family

Step 1. Start with the family and the side condition.

> f(x, y, α, β) = 0
> φ(α, β) = 0

Step 2. Differentiate both with respect to α, treating β as a function of α.

> ∂f/∂α + (∂f/∂β)(∂β/∂α) = 0
> ∂φ/∂α + (∂φ/∂β)(∂β/∂α) = 0

Step 3. Solve the differentiated relations for ∂β/∂α, equate the two expressions, and use the result together with the original relations to eliminate α and β.

Worked check — lines x/a + y/b = 1 with a² + b² = c²:

From the line relation, differentiating with respect to a gives

> −x/a² − (y/b²)(db/da) = 0

From the side condition,

> 2a + 2b(db/da) = 0, so db/da = −a/b

Equating the two expressions for db/da gives x/a³ = y/b³. Combining with the side condition yields

> x^(2/3) + y^(2/3) = c^(2/3)

which is the envelope (an astroid-type curve).

### Key Observations

| Expansion / family type | Condition used | Envelope obtained by |
|---|---|---|
| One-parameter family f(x, y, α) = 0 | ∂f/∂α = 0 | Eliminating α between the family and its partial derivative |
| Quadratic in parameter aα² + bα + c = 0 | b² − 4ac = 0 | Substituting α = −b/(2a), or directly using the discriminant condition |
| Two-parameter family with side condition φ(α, β) = 0 | Partial derivatives of both relations | Eliminating α, β and ∂β/∂α from the four relations |
| Lines x cos α + y sin α = p | ∂/∂α | Squaring and adding to use cos²α + sin²α = 1 |
| Lines x cos³α + y sin³α = a | ∂/∂α | Solving for tan α, then substituting sin α and cos α |

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

- **Alexis Clairaut (1713–1765), *Recherches sur les courbes à double courbure* (1731)** — early systematic treatment of envelopes as curves tangent to a family of surfaces and curves.
- **Gottfried Wilhelm Leibniz (1646–1716), published work of 1692–1694** — introduced the differential calculus methods used to eliminate the parameter and find tangent loci.
- **Gaspard Monge (1746–1818), *Traité de géométrie descriptive* (1799)** — developed envelope theory in the context of descriptive geometry and surfaces.

## Real-World Applications

### 1. Signal Processing

- Envelopes describe the amplitude boundary of a modulated waveform.
- The envelope of a family of shifted or scaled pulses marks the maximum reach of the signal.
- Harmonic distortion analysis uses envelopes to separate a fundamental from added harmonics.
- **Example:** A distorted audio signal modelled as sin³θ expands into a fundamental plus a third-harmonic term.

### 2. Physics

- Envelopes of wave families describe the crest boundary of interfering waves.
- In optics, the envelope of a family of rays forms a caustic curve.
- Envelope methods locate turning points in families of trajectories.
- **Example:** A family of light rays reflected from a curved mirror produces a caustic envelope.

### 3. Electrical Engineering

- The envelope of a family of load lines identifies the operating boundary of a circuit.
- Envelope tracking follows the peak boundary of a modulated supply voltage.
- Families of impedance curves have envelopes marking stability limits.
- **Example:** A family of load lines on a device characteristic has an envelope that bounds safe operation.

### 4. Computer Graphics

- Envelopes of moving or scaled shapes give the swept boundary of an animation.
- The envelope of a family of offset curves defines the outer silhouette.
- Motion envelopes bound the region swept by a rotating object.
- **Example:** The envelope of a family of translated circles traces the swept region of a moving brush.

### 5. Mechanical Engineering

- The envelope of a family of gear-tooth profiles defines the meshing boundary.
- Cam design uses envelopes of follower positions to shape the cam profile.
- The envelope of tool positions bounds the machined surface.
- **Example:** The envelope of a family of cutting-tool positions gives the finished surface profile.

### 6. Economics

- Envelopes of cost curves bound the long-run cost frontier.
- Families of budget lines have envelopes describing expansion paths.
- Envelope theorems relate optimized value functions to parameter changes.
- **Example:** The envelope of a family of short-run cost curves gives the long-run cost boundary.

### 7. Acoustics

- Envelopes describe the decay boundary of a sound over time.
- The envelope of a family of resonance curves marks the peak response boundary.
- Room-mode families have envelopes indicating pressure extremes.
- **Example:** A family of resonance curves for varying damping has an envelope marking peak response.

### 8. Numerical Analysis

- Envelopes of iteration trajectories bound convergence regions.
- Families of approximate solution curves have envelopes indicating error bounds.
- Envelope conditions help detect when a parameter sweep changes qualitatively.
- **Example:** A family of approximate solution curves has an envelope that bounds the error band.

### 9. Astronomy

- Envelopes of orbit families bound the reachable region of a body.
- The envelope of a family of light curves indicates maximum brightness limits.
- Families of projected orbits have envelopes marking apparent paths.
- **Example:** A family of projected orbits on the sky has an envelope marking the apparent path boundary.

### 10. Music Theory

- Envelopes describe the attack-and-decay boundary of a note.
- Families of tuning curves have envelopes marking pitch limits.
- Envelope shapes distinguish instrument timbres.
- **Example:** A family of tuning curves for varying string tension has an envelope marking the playable pitch range.

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
|---|---|---|---|
| Notes | Definition 6.1 of the envelope | PDF | high |
| Notes | Necessary and sufficient condition ∂f/∂α = 0 | PDF | high |
| Notes | Elimination of α between f = 0 and ∂f/∂α = 0 | PDF | high |
| Notes | Quadratic case condition b² − 4ac = 0 | PDF | high |
| Notes | Two-parameter method via partial derivatives of f and φ | PDF | high |
| Notes | Example x cos α + y sin α = p gives x² + y² = p² | PDF | high |
| Notes | Example y = mx + a/m gives y² = 4ax | PDF | high |
| Notes | Example x/a + y/b = 1 with a² + b² = c² gives x^(2/3) + y^(2/3) = c^(2/3) | PDF | high |
| Historical Background | Clairaut, *Recherches sur les courbes à double courbure* (1731) | textbook-standard | high |
| Historical Background | Leibniz, work of 1692–1694 on differential methods | textbook-standard | high |
| Historical Background | Monge, *Traité de géométrie descriptive* (1799) | textbook-standard | high |
| Applications | sin³θ expands into a fundamental plus a third-harmonic term | textbook-standard | high |
| Applications | Envelope of reflected rays forms a caustic | textbook-standard | high |
| Applications | Envelope of short-run cost curves gives long-run boundary | textbook-standard | high |