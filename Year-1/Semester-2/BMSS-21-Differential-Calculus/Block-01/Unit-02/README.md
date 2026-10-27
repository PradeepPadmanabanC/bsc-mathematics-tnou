# Leibnitz's Theorem and Its Applications

This set of study notes covers the formation of differential equations from given relations between variables and the use of **Leibnitz's theorem** to compute the n-th derivative of a product of two functions. It includes worked examples of eliminating arbitrary constants to form second-order differential equations, the general statement of Leibnitz's theorem, and step-by-step applications to products such as x²e³ˣ and x²sin 5x, as well as repeated differentiation of relations to obtain n-th order recurrence equations.

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

The unit treats two linked skills: forming a differential equation from a relation between x and y, and differentiating a product n times.

- **Eliminating arbitrary constants.** Given a relation such as y = a cos 5x + b sin 5x, repeated differentiation lets us eliminate a and b and obtain a differential equation satisfied by y alone.
- **Reducing to a second-order equation.** Most examples produce a relation of the form (1 − x²)y₂ − xy₁ − m²y = 0, which is then the starting point for further work.
- **Computing n-th derivatives of products.** Leibnitz's theorem gives Dⁿ(uv) as a finite binomial-type sum, so products like x²e³ˣ can be differentiated any number of times without repeated manual work.
- **Generating n-th order recurrences.** Applying Leibnitz's theorem to an already-established second-order equation yields a recurrence linking yₙ₊₂, yₙ₊₁, and yₙ.

### Mathematical Foundation

**Leibnitz's theorem.** If u and v are functions of x and n is a positive integer, then

> Dⁿ(uv) = uₙv + ⁿC₁uₙ₋₁v₁ + ⁿC₂uₙ₋₂v₂ + … + ⁿCᵣuₙ₋ᵣvᵣ + … + uvₙ

where Dⁿ(uv) stands for the n-th derivative of uv.

**Derivatives of standard functions used in the notes:**

> Dⁿ(eᵃˣ) = aⁿeᵃˣ

> Dⁿ(sin 5x) = 5ⁿ sin(5x + nπ/2)

**Note 2.1 (from the PDF).**

> 1. This theorem is quite useful to find the n-th derivative of the product of two functions of x.
> 2. While using this formula, we can choose the algebraic function as v.

**Second-order relations established in the PDF:**

> If y = a cos 5x + b sin 5x, then d²y/dx² + 25y = 0.

> If y = eˣ sin x, then d²y/dx² − 2dy/dx + 2y = 0.

> If y = e^(m cos⁻¹x), then (1 − x²)y₂ − xy₁ − m²y = 0.

> If y = a cos(log x) + b sin(log x), then x²y₂ + xy₁ + y = 0.

> If y = (x + √(1 + x²))ᵐ, then (1 + x²)y₂ + xy₁ − m²y = 0.

> If y = sin(m sin⁻¹x), then (1 − x²)y₂ − xy₁ + m²y = 0.

### Derivation of the General Method

#### Step 1 — Form the second-order relation

Start from the given relation in x and y, differentiate once, then differentiate again, and combine the results to eliminate the arbitrary constants a and b.

For y = a cos 5x + b sin 5x:

> dy/dx = −5a sin 5x + 5b cos 5x

> d²y/dx² = −25a cos 5x − 25b sin 5x = −25y

> Hence d²y/dx² + 25y = 0.

For y = e^(m cos⁻¹x), differentiate and clear the square root:

> dy/dx = e^(m cos⁻¹x) · (−m/√(1 − x²))

> √(1 − x²) dy/dx = −my

> (1 − x²)(dy/dx)² = m²y²

Differentiate again and cancel 2 dy/dx:

> (1 − x²)y₂ − xy₁ = m²y

> (1 − x²)y₂ − xy₁ − m²y = 0.

#### Step 2 — Apply Leibnitz's theorem n times

Once a relation of the form P(x)y₂ + Q(x)y₁ + R(x)y = 0 is available, differentiate it n times term by term using Leibnitz's theorem.

For x²y₂ + xy₁ + y = 0:

> (x²y₂)ₙ + (xy₁)ₙ + (y)ₙ = 0

> x²yₙ₊₂ + ⁿC₁yₙ₊₁(2x) + ⁿC₂yₙ(2) + xyₙ₊₁ + ⁿC₁yₙ + yₙ = 0

> x²yₙ₊₂ + 2nx yₙ₊₁ + n(n − 1)yₙ + xyₙ₊₁ + nyₙ + yₙ = 0

> x²yₙ₊₂ + (2n + 1)x yₙ₊₁ + (n² + 1)yₙ = 0.

For (1 − x²)y₂ − xy₁ − m²y = 0:

> (1 − x²)yₙ₊₂ − (2n + 1)x yₙ₊₁ − (n² + m²)yₙ = 0.

#### For cosⁿθ and sinⁿθ

The PDF does not treat powers of cos θ or sin θ; its n-th derivative work is on products of the form x²e³ˣ and x²sin 5x. The relevant standard identity used in the notes is the phase-shift rule:

> Dⁿ(sin 5x) = 5ⁿ sin(5x + nπ/2)

#### Worked pattern for x²e³ˣ

Choose u = e³ˣ and v = x² (algebraic function as v, per Note 2.1). Since v₁ = 2x, v₂ = 2, and v₃ = 0, the series terminates after three terms:

> Dⁿ(x²e³ˣ) = 3ⁿe³ˣx² + ⁿC₁3ⁿ⁻¹e³ˣ(2x) + ⁿC₂3ⁿ⁻²e³ˣ(2)

> = e³ˣ3ⁿ⁻²[9x² + 6nx + n(n − 1)].

#### Worked pattern for x²sin 5x

Choose u = sin 5x and v = x². The series again terminates after three terms:

> Dⁿ(x²sin 5x) = 5ⁿx² sin(5x + nπ/2) + 2nx·5ⁿ⁻¹ sin(5x + (n − 1)π/2) + n(n − 1)5ⁿ⁻² sin(5x + (n − 2)π/2)

> = 5ⁿ⁻²[25x² sin(5x + nπ/2) + 10nx sin(5x + (n − 1)π/2) + n(n − 1) sin(5x + (n − 2)π/2)].

### Key Observations

| Expansion type | When it applies | Behaviour |
| --- | --- | --- |
| Dⁿ(x²e³ˣ) | Product of a polynomial of degree 2 with an exponential | Series terminates after 3 terms because v₃ = 0 |
| Dⁿ(x²sin 5x) | Product of a polynomial of degree 2 with a sine | Series terminates after 3 terms; each term carries a phase shift nπ/2 |
| (1 − x²)yₙ₊₂ − (2n + 1)xyₙ₊₁ − (n² + m²)yₙ = 0 | Relations of the form e^(m cos⁻¹x) | Coefficient of yₙ combines n² and m² |
| x²yₙ₊₂ + (2n + 1)xyₙ₊₁ + (n² + 1)yₙ = 0 | Relations of the form a cos(log x) + b sin(log x) | Coefficient of yₙ is n² + 1 |
| (1 − x²)yₙ₊₂ − (2n + 1)xyₙ₊₁ + (m² − n²)yₙ = 0 | Relations of the form sin(m sin⁻¹x) | Sign of the yₙ coefficient flips relative to the exponential case |

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

Gottfried Wilhelm Leibniz (1646–1716), published statement of the general product rule for higher derivatives (1684) — gave the binomial-type formula for the n-th derivative of a product.

The PDF itself supplies no dates, works, or biographical detail for Leibniz; the entry above is included only because the theorem is named after him and the attribution is standard in undergraduate calculus texts.

## Real-World Applications

### 1. Signal Processing

- Products of polynomials with sinusoids arise when modelling modulated signals.
- Higher derivatives of such products are needed in filter design and stability analysis.
- Leibnitz's theorem gives a closed form instead of repeated numerical differentiation.
- **Example:** A signal modelled as x²sin 5x has an n-th derivative expressible as a sum of three phase-shifted sine terms.

### 2. Physics

- Equations of motion with position-dependent coefficients reduce to relations like (1 − x²)y₂ − xy₁ − m²y = 0.
- Such relations appear in central-force and oscillator problems.
- Repeated differentiation produces recurrences for series solutions.
- **Example:** A particle whose displacement satisfies (1 − x²)y₂ − xy₁ − m²y = 0 is differentiated n times to obtain a recurrence among yₙ₊₂, yₙ₊₁, yₙ.

### 3. Electrical Engineering

- Circuit responses involving eˣ sin x satisfy d²y/dx² − 2dy/dx + 2y = 0.
- Leibnitz's theorem supplies higher derivatives for transient analysis.
- Polynomial-times-exponential products model switched responses.
- **Example:** A damped response y = eˣ sin x satisfies d²y/dx² − 2dy/dx + 2y = 0, which can be differentiated n times.

### 4. Computer Graphics

- Polynomial-times-trigonometric curves are used in animation and spline design.
- Higher derivatives control smoothness and curvature continuity.
- Leibnitz's theorem reduces the cost of computing derivative sequences.
- **Example:** A curve defined as a product of a quadratic and a sine is differentiated term by term using the finite Leibnitz sum.

### 5. Mechanical Engineering

- Vibration models with variable stiffness lead to equations like (1 − x²)y₂ − xy₁ − m²y = 0.
- Recurrence relations from Leibnitz's theorem feed series solutions.
- Products of polynomials and sinusoids model eccentric rotating masses.
- **Example:** A rotating-mass vibration term proportional to x²sin 5x is differentiated n times in closed form.

### 6. Economics

- Difference and differential equations in growth models use product-rule expansions.
- Higher-order derivatives appear in comparative-statics of products of functions.
- Leibnitz's theorem gives compact expressions for derivative sequences.
- **Example:** A growth term formed as a product of a polynomial and a periodic factor is differentiated n times using the Leibnitz expansion.

### 7. Acoustics

- Sound-pressure models combine polynomial envelopes with sinusoidal carriers.
- Higher derivatives describe rate-of-change of pressure.
- Leibnitz's theorem handles the product structure directly.
- **Example:** A pressure envelope proportional to x²sin 5x is differentiated n times to obtain its phase-shifted derivative terms.

### 8. Numerical Analysis

- Finite-difference formulas for products rely on the same binomial-coefficient structure.
- Truncation analysis of product derivatives uses Leibnitz-type expansions.
- Recurrence relations from the theorem support stable computation of derivative sequences.
- **Example:** The terminating series for x²e³ˣ shows why only three terms are needed when one factor is a quadratic.

### 9. Astronomy

- Perturbation series involve products of polynomials and trigonometric terms.
- Higher derivatives of such products appear in orbital expansions.
- Leibnitz's theorem gives systematic derivative formulas.
- **Example:** A periodic perturbation term formed as a quadratic times a sine is differentiated n times in closed form.

### 10. Chemistry

- Rate equations sometimes involve products of concentration polynomials and oscillatory factors.
- Higher derivatives enter sensitivity and stability analysis.
- Leibnitz's theorem provides the product-derivative structure.
- **Example:** A rate term modelled as a polynomial times a periodic factor is differentiated n times using the finite Leibnitz sum.

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
| --- | --- | --- | --- |
| Mathematical Foundation | Dⁿ(uv) = uₙv + ⁿC₁uₙ₋₁v₁ + … + uvₙ | PDF (page 5, Section 2.2) | high |
| Mathematical Foundation | Dⁿ(eᵃˣ) = aⁿeᵃˣ | PDF (used in Example 2.7) | high |
| Mathematical Foundation | Dⁿ(sin 5x) = 5ⁿ sin(5x + nπ/2) | PDF (used in Example 2.8) | high |
| Mathematical Foundation | y = a cos 5x + b sin 5x implies d²y/dx² + 25y = 0 | PDF (Example 2.1) | high |
| Mathematical Foundation | y = eˣ sin x implies d²y/dx² − 2dy/dx + 2y = 0 | PDF (Example 2.2) | high |
| Mathematical Foundation | y = e^(m cos⁻¹x) implies (1 − x²)y₂ − xy₁ − m²y = 0 | PDF (Example 2.3) | high |
| Mathematical Foundation | y = a cos(log x) + b sin(log x) implies x²y₂ + xy₁ + y = 0 | PDF (Example 2.4) | high |
| Mathematical Foundation | y = (x + √(1 + x²))ᵐ implies (1 + x²)y₂ + xy₁ − m²y = 0 | PDF (Example 2.5) | high |
| Mathematical Foundation | y = sin(m sin⁻¹x) implies (1 − x²)y₂ − xy₁ + m²y = 0 | PDF (Example 2.6) | high |
| Derivation | Dⁿ(x²e³ˣ) = e³ˣ3ⁿ⁻²[9x² + 6nx + n(n − 1)] | PDF (Example 2.7) | high |
| Derivation | Dⁿ(x²sin 5x) closed form | PDF (Example 2.8) | high |
| Derivation | x²yₙ₊₂ + (2n + 1)xyₙ₊₁ + (n² + 1)yₙ = 0 | PDF (Example 2.9) | high |
| Derivation | (1 − x²)yₙ₊₂ − (2n + 1)xyₙ₊₁ − (n² + m²)yₙ = 0 | PDF (Example 2.10) | high |
| Derivation | (1 + x²)yₙ₊₂ + (2n + 1)xyₙ₊₁ + (n² − m²)yₙ = 0 | PDF (Example 2.11) | high |
| Derivation | (1 − x²)yₙ₊₂ − (2n + 1)xyₙ₊₁ + (m² − n²)yₙ = 0 | PDF (Example 2.12) | high |
| Key Observations | Leibnitz series for x²e³ˣ terminates after 3 terms | PDF (v₃ = 0 in Example 2.7) | high |
| Historical Background | Gottfried Wilhelm Leibniz (1646–1716), product rule for higher derivatives (1684) | textbook-standard | high |
| Historical Background | PDF names no historical figures or dates | PDF (no historical content) | high |
| Applications | Example: x²sin 5x differentiated n times gives three phase-shifted sine terms | PDF (Example 2.8) | high |
| Applications | Example: y = eˣ sin x satisfies d²y/dx² − 2dy/dx + 2y = 0 | PDF (Example 2.2) | high |
| Applications | Example: (1 − x²)y₂ − xy₁ − m²y = 0 differentiated n times gives recurrence | PDF (Example 2.10) | high |
| Applications | Example: x²e³ˣ requires only three terms | PDF (Example 2.7) | high |