# Inverse Hyperbolic Functions

These notes cover the **inverse hyperbolic functions** sinh⁻¹, cosh⁻¹ and tanh⁻¹ and show how each can be written as a natural logarithm. Each formula is derived from the exponential definition of the hyperbolic function by turning the equation into a quadratic in eʸ (or a linear equation in e²ʸ for tanh⁻¹). The notes close with a worked example that uses tanh⁻¹ to solve a complex-cosine equation, and with the Check Your Progress items from the source unit (B.Sc. Mathematics, I Year, I Sem, Trigonometry, Unit 6).

---

## Table of Contents

1. [Notes](#notes)
2. [Historical Background](#historical-background)
3. [Real-World Applications](#real-world-applications)
4. [Self-Audit](#self-audit)

---

## Notes

### Overview

An **inverse hyperbolic function** undoes a hyperbolic function: if x = sinh y, then y = sinh⁻¹(x). Because sinh, cosh and tanh are built from eʸ and e⁻ʸ, their inverses can be written with the natural logarithm. This matters for four reasons:

- It replaces an implicit definition (y such that x = sinh y) with an explicit formula in x.
- It gives closed forms for solving equations of the type sinh y = x, cosh y = x, tanh y = x.
- It connects hyperbolic functions to logarithms, so results can be simplified with ordinary log rules.
- It makes problems involving complex arguments tractable, such as cos(x + iy) = r(cos θ + i sin θ) in Example 6.4.

### Mathematical Foundation

The three core identities (Examples 6.1 to 6.3 of the PDF), with logₑ written for the natural logarithm:

> **sinh⁻¹(x) = logₑ( x + √(x² + 1) )**

> **cosh⁻¹(x) = logₑ( x + √(x² − 1) )**

> **tanh⁻¹(x) = ½ logₑ( (1 + x) / (1 − x) )**

The derivations use the exponential definitions:

> sinh y = (eʸ − e⁻ʸ)/2
> cosh y = (eʸ + e⁻ʸ)/2
> tanh y = (eʸ − e⁻ʸ)/(eʸ + e⁻ʸ)

The PDF does not state domains. The following are standard and are added here as a note:

- sinh⁻¹(x) is defined for all real x.
- cosh⁻¹(x) requires x ≥ 1.
- tanh⁻¹(x) requires |x| < 1.

### Derivation of the General Method

The general method is to write x as the hyperbolic function of y in terms of eʸ, clear denominators, solve for eʸ (or e²ʸ), and take logₑ. Positivity of eʸ is used to reject any non-positive root.

#### For sinh⁻¹(x)

Let sinh⁻¹(x) = y, so x = sinh y.

> x = (eʸ − e⁻ʸ)/2 = (eʸ − 1/eʸ)/2 = (e²ʸ − 1)/(2eʸ)

> 2x·eʸ = e²ʸ − 1

> (eʸ)² − 2x·eʸ − 1 = 0  (a quadratic in eʸ with a = 1, b = −2x, c = −1)

> eʸ = ( 2x ± √(4x² + 4) ) / 2 = x ± √(x² + 1)

Since eʸ > 0 and √(x² + 1) > |x|, the root with the minus sign is negative and is rejected.

> eʸ = x + √(x² + 1)

> y = logₑ( x + √(x² + 1) )

> **sinh⁻¹(x) = logₑ( x + √(x² + 1) )**

#### For cosh⁻¹(x)

Let cosh⁻¹(x) = y, so x = cosh y.

> x = (eʸ + e⁻ʸ)/2 = (e²ʸ + 1)/(2eʸ)

> 2x·eʸ = e²ʸ + 1

> (eʸ)² − 2x·eʸ + 1 = 0  (a quadratic in eʸ with a = 1, b = −2x, c = 1)

> eʸ = ( 2x ± √(4x² − 4) ) / 2 = x ± √(x² − 1)

The PDF takes the plus sign. Note: for x ≥ 1 both roots are positive and are reciprocals of each other. The plus sign gives y ≥ 0, which is the standard principal value; the PDF does not discuss this choice.

> eʸ = x + √(x² − 1)

> **cosh⁻¹(x) = logₑ( x + √(x² − 1) )**

#### For tanh⁻¹(x)

Let tanh⁻¹(x) = y, so x = tanh y.

> x = (eʸ − e⁻ʸ)/(eʸ + e⁻ʸ)

Multiplying numerator and denominator by eʸ:

> x = (e²ʸ − 1)/(e²ʸ + 1)

> x·e²ʸ + x = e²ʸ − 1

> 1 + x = e²ʸ − x·e²ʸ = e²ʸ(1 − x)

> e²ʸ = (1 + x)/(1 − x)

> 2y = logₑ( (1 + x)/(1 − x) )

> **tanh⁻¹(x) = ½ logₑ( (1 + x)/(1 − x) )**

(The PDF's line "xey + x = e2y − 1" appears to be a typesetting slip for x·e²ʸ + x = e²ʸ − 1; the result is unchanged.)

#### Worked Example (Example 6.4)

Problem: if cos(x + iy) = r(cos θ + i sin θ), prove that y = ½ logₑ[ sin(x − θ) / sin(x + θ) ].

> cos x cos(iy) − sin x sin(iy) = r cos θ + i r sin θ

Using cos(iy) = cosh y and sin(iy) = i sinh y:

> cos x cosh y − i sin x sinh y = r cos θ + i r sin θ

Equating real and imaginary parts:

> cos x cosh y = r cos θ  (6.1)

> −sin x sinh y = r sin θ  (6.2)

Dividing (6.2) by (6.1):

> tanh y = −tan θ / tan x

> y = tanh⁻¹( −tan θ / tan x )

> y = ½ logₑ[ (1 − tan θ/tan x) / (1 + tan θ/tan x) ]

> y = ½ logₑ[ (tan x − tan θ) / (tan x + tan θ) ]

Writing each tangent as sine over cosine and clearing the common factor cos x cos θ:

> y = ½ logₑ[ (sin x cos θ − cos x sin θ) / (sin x cos θ + cos x sin θ) ]

> **y = ½ logₑ[ sin(x − θ) / sin(x + θ) ]**

#### Check Your Progress (from the PDF)

Exercise: prove tanh⁻¹(sin θ) = cosh⁻¹(sec θ). The PDF poses this without a solution. A short derivation from the identities above, assuming cos θ > 0:

> tanh⁻¹(sin θ) = ½ logₑ[ (1 + sin θ)/(1 − sin θ) ]

> (1 + sin θ)/(1 − sin θ) = (1 + sin θ)² / (1 − sin²θ) = (1 + sin θ)² / cos²θ

> tanh⁻¹(sin θ) = logₑ[ (1 + sin θ)/cos θ ] = logₑ( sec θ + tan θ )

> cosh⁻¹(sec θ) = logₑ( sec θ + √(sec²θ − 1) ) = logₑ( sec θ + tan θ )

Both sides agree. ∎

The multiple-choice answers given in the PDF:

| Q | Answer | Result |
|---|--------|--------|
| 1 | (b) | sinh⁻¹x = logₑ[ x + √(x² + 1) ] |
| 2 | (c) | tanh⁻¹x = ½ logₑ[ (1 + x)/(1 − x) ] |
| 3 | (a) | if tanh(x/2) = tan(θ/2), then x = log tan(π/4 + θ/2) |
| 4 | (c) | if cosh u = sec θ, then u = log[ sec θ + tan θ ] |

### Key Observations

| Function | Defined for | Closed form | Quantity that drives the solution |
|----------|-------------|-------------|-----------------------------------|
| sinh⁻¹(x) | all real x | logₑ( x + √(x² + 1) ) | Quadratic in eʸ; the negative root is rejected |
| cosh⁻¹(x) | x ≥ 1 | logₑ( x + √(x² − 1) ) | Quadratic in eʸ; the plus root is taken (principal value) |
| tanh⁻¹(x) | |x| < 1 | ½ logₑ( (1 + x)/(1 − x) ) | Linear equation in e²ʸ |

Other points to remember:

- sinh⁻¹ and cosh⁻¹ both lead to quadratics in eʸ, which differ only in the sign of the constant term (−1 for sinh, +1 for cosh).
- tanh⁻¹ avoids a quadratic because multiplying through by eʸ gives an equation that is linear in e²ʸ.
- Example 6.4 shows the typical use: reduce a complex equation to tanh y = (real quantity), then apply the tanh⁻¹ formula.

---

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

- Vincenzo Riccati (1707–1775), Opuscula ad res physicas et mathematicas pertinentia (1757) — introduced the hyperbolic functions using the unit hyperbola, in analogy with circular functions.
- Johann Heinrich Lambert (1728–1777), "Mémoire sur quelques propriétés remarquables des quantités transcendantes circulaires et logarithmiques" (1768) — developed the hyperbolic functions systematically and brought out their parallels with the trigonometric functions.
- Leonhard Euler (1707–1783), Introductio in analysin infinitorum (1748) — established the exponential and logarithm as foundations of analysis, including the formula linking eⁱᶿ to cos θ and sin θ.

---

## Real-World Applications

### 1. Special Relativity (Physics)

- Describe velocities through rapidity, which adds linearly under successive boosts.
- Convert between rapidity and ordinary velocity.
- Simplify velocity-addition problems.

**Example:** The rapidity φ of a body moving at speed v satisfies tanh φ = v/c, so φ = tanh⁻¹(v/c) = ½ logₑ[ (1 + v/c)/(1 − v/c) ].
Check: apply tanh⁻¹(x) = ½ logₑ[ (1 + x)/(1 − x) ] with x = v/c.

### 2. Structural and Mechanical Engineering

- Model hanging cables and chains whose shape is a hyperbolic cosine curve.
- Recover horizontal position from a measured height on the curve.
- Support design of suspension elements and arches.

**Example:** For a hanging cable y = a cosh(x/a), the horizontal position (on the right branch) is x = a cosh⁻¹(y/a) = a logₑ[ y/a + √((y/a)² − 1) ].
Check: apply cosh⁻¹(u) = logₑ( u + √(u² − 1) ) with u = y/a.

### 3. Electrical Engineering

- Analyze signal attenuation along transmission lines.
- Express propagation constants of lines and filters with hyperbolic functions.
- Invert those relations to find line length or impedance parameters.

**Example:** A transmission-line model gives a hyperbolic relation between input and output quantities, and an inverse hyperbolic function extracts the line parameter from measurements.

### 4. Calculus and Integration

- Provide antiderivatives for expressions with square roots of x² + 1 or x² − 1.
- Offer logarithmic alternatives to inverse trigonometric substitutions.
- Simplify integrals that arise in arc-length and area problems.

**Example:** An integral whose integrand involves 1/√(x² + 1) is evaluated in closed form as a logarithm through the sinh⁻¹ identity.

### 5. Signal Processing

- Model smooth saturating nonlinearities built on tanh.
- Invert such nonlinearities to recover the original signal.
- Analyze how a nonlinear stage distorts a waveform.

**Example:** A saturating amplifier stage modelled by a tanh curve is "undone" by applying tanh⁻¹ to its output, within the range |x| < 1.

### 6. Machine Learning and Computer Graphics

- Use tanh as an activation function, with tanh⁻¹ as its inverse transform.
- Map bounded values back to an unbounded scale for optimisation.
- Support smooth easing and mapping curves in rendering.

**Example:** A bounded output between −1 and 1 is mapped back to an unbounded parameter by tanh⁻¹ so that an optimiser can work on the unbounded scale.

### 7. Statistics

- Apply the Fisher z-transformation, which is tanh⁻¹ of a correlation coefficient.
- Stabilize variance so confidence intervals for correlations are easier to build.
- Map a bounded quantity onto the whole real line.

**Example:** A sample correlation strictly between −1 and 1 is transformed by tanh⁻¹ before building a confidence interval, then transformed back by tanh.

### 8. Fluid Dynamics and Water Waves

- Express wave dispersion relations with tanh of depth-dependent terms.
- Solve those relations for depth or wavenumber using the inverse.
- Study how wave behavior changes between shallow and deep water.

**Example:** A dispersion relation involving tanh of a depth-scaled wavenumber is inverted with tanh⁻¹ to estimate depth from measured wave properties.

### 9. Numerical Analysis

- Provide stable logarithmic forms for evaluating inverse hyperbolic values.
- Serve as test cases for root-finding methods on hyperbolic equations.
- Support change-of-variable tricks in numerical integration.

**Example:** A root-finding routine for sinh y = x can be checked against the closed form logₑ( x + √(x² + 1) ).

### 10. Complex Analysis

- Solve equations such as cos(x + iy) = r(cos θ + i sin θ) by separating real and imaginary parts.
- Relate inverse circular functions of complex arguments to logarithms.
- Reduce complex trigonometric equations to real hyperbolic ones.

**Example:** Example 6.4 reduces cos(x + iy) = r(cos θ + i sin θ) to tanh y = −tan θ / tan x, whose solution is y = ½ logₑ[ sin(x − θ)/sin(x + θ) ].

---

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
|---------|-------|------------------------------------------------------|------------|
| Notes | sinh⁻¹(x) = logₑ( x + √(x² + 1) ) | PDF (Example 6.1) | high |
| Notes | cosh⁻¹(x) = logₑ( x + √(x² − 1) ) | PDF (Example 6.2) | high |
| Notes | tanh⁻¹(x) = ½ logₑ( (1 + x)/(1 − x) ) | PDF (Example 6.3) | high |
| Notes | Example 6.4 result y = ½ logₑ[ sin(x − θ)/sin(x + θ) ] | PDF (Example 6.4), re-derived | high |
| Notes | Domains: sinh⁻¹ all real x; cosh⁻¹ x ≥ 1; tanh⁻¹ |x| < 1 | textbook-standard (not stated in PDF) | high |
| Notes | Plus root chosen for cosh⁻¹ gives the principal value y ≥ 0 | textbook-standard (PDF takes the plus root without comment) | high |
| Notes | tanh⁻¹(sin θ) = cosh⁻¹(sec θ) for cos θ > 0 | PDF exercise; derived here with PDF identities | high |
| Notes | Multiple-choice answers (b, c, a, c) | PDF answer key | high |
| Historical Background | Riccati (1707–1775), Opuscula (1757), introduced hyperbolic functions | textbook-standard | high |
| Historical Background | Lambert (1728–1777), Mémoire (1768), systematic development of hyperbolic functions | textbook-standard | high |
| Historical Background | Euler (1707–1783), Introductio (1748), exponential and logarithm as foundations, eⁱᶿ formula | textbook-standard | high |
| Applications 1 | φ = tanh⁻¹(v/c) = ½ logₑ[ (1 + v/c)/(1 − v/c) ] | PDF identity for tanh⁻¹; definition of rapidity | high |
| Applications 2 | x = a cosh⁻¹(y/a) = a logₑ[ y/a + √((y/a)² − 1) ] | PDF identity for cosh⁻¹ | high |
| Applications 10 | tanh y = −tan θ / tan x and y = ½ logₑ[ sin(x − θ)/sin(x + θ) ] | PDF (Example 6.4) | high |