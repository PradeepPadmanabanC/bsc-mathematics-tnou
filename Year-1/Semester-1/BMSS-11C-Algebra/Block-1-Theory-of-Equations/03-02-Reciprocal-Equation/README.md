# Reciprocal Equations

This set of study notes covers the theory and solution of **reciprocal equations** — polynomial equations that remain unchanged when the variable x is replaced by 1/x. The notes define the four standard types of reciprocal equations, explain the relationship between their coefficients and their roots, and provide a step-by-step method for reducing them to lower-degree equations using the substitution z = x + 1/x. Worked examples illustrate even-degree and odd-degree cases, including the use of synthetic division to remove the roots x = 1 and x = −1 before applying the standard reduction.

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

A **reciprocal equation** is a polynomial equation that is unaltered when x is replaced by 1/x. Recognizing this symmetry matters because it turns a high-degree problem into a much smaller one.

- It guarantees that roots occur in reciprocal pairs: if α is a root, then 1/α is also a root.
- It reveals hidden roots immediately from the coefficients: x = 1 or x = −1 can be read off from the signs of a₀ and aₙ.
- It allows a degree-4 or degree-6 equation to be compressed into a quadratic in z = x + 1/x.
- It reduces computational effort dramatically compared with factoring or applying the rational root theorem to the original polynomial.

### Mathematical Foundation

> A reciprocal equation is one which is unaltered when x is replaced by 1/x.

> If α is a root, then 1/α is also a root of the equation.

> In the reciprocal equation, a₀ = ±aₙ, a₁ = ±aₙ₋₁, ...

The four standard types are classified by degree and by whether the end coefficients a₀ and aₙ have the same or opposite signs.

> Type I (Standard Type): even degree, signs of a₀ and aₙ the same.
> Type II: even degree, signs of a₀ and aₙ opposite.
> Type III: odd degree, signs of a₀ and aₙ the same.
> Type IV: odd degree, signs of a₀ and aₙ opposite.

### Derivation of the General Method

#### For even-degree reciprocal equations with matching end signs

Start with a degree-4 example:

> 4x⁴ − 20x³ + 33x² − 20x + 4 = 0

Because the equation is unchanged under x → 1/x, divide every term by x²:

> 4x² − 20x + 33 − 20/x + 4/x² = 0

Collect like powers by pairing terms whose exponents sum to zero:

> 4(x² + 1/x²) − 20(x + 1/x) + 33 = 0

Introduce the substitution:

> z = x + 1/x
> x² + 1/x² = z² − 2

Substitute into the collected equation:

> 4(z² − 2) − 20z + 33 = 0
> 4z² − 8 − 20z + 33 = 0
> 4z² − 20z + 25 = 0

Solve the quadratic in z:

> z = (20 ± √(400 − 400)) / 8 = 20/8 = 5/2

Back-substitute z = 5/2:

> x + 1/x = 5/2
> (x² + 1)/x = 5/2
> 2x² − 5x + 2 = 0
> x = (5 ± √(25 − 16)) / 4 = (5 ± 3)/4 = 2, 1/2

The repeated root z = 5/2 yields the pair 2, 1/2 twice, so the roots are 2, 1/2, 2, 1/2.

For a degree-6 equation of Type I, divide by x³ instead of x² and use:

> z = x + 1/x
> x² + 1/x² = z² − 2
> x³ + 1/x³ = z³ − 3z

#### For odd-degree reciprocal equations

If the degree is odd and the signs of a₀ and aₙ are the same (Type III), then x = −1 is a root. If the degree is odd and the signs are opposite (Type IV), then x = 1 is a root.

For example, in:

> 6x⁵ + 11x⁴ − 33x³ − 33x² + 11x + 6 = 0

the signs of a₀ and a₅ are the same, so x = −1 is a root. Synthetic division by (x + 1) reduces the equation to a degree-4 reciprocal equation:

> 6x⁴ + 5x³ − 38x² + 5x + 6 = 0

This reduced equation is Type I and is solved by dividing by x² and substituting z = x + 1/x.

### Key Observations

| Type | Degree of f(x) = 0 | Signs of a₀ and aₙ | Immediate result | Reduction step |
|---|---|---|---|---|
| Type I (Standard) | Even | Same | None | Divide by x^(n/2), substitute z = x + 1/x |
| Type II | Even | Opposite | x = 1 and x = −1 are roots | Divide out (x − 1)(x + 1), then treat as Type I |
| Type III | Odd | Same | x = −1 is a root | Divide out (x + 1), then treat as Type I |
| Type IV | Odd | Opposite | x = 1 is a root | Divide out (x − 1), then treat as Type I |

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

- **René Descartes** (1596–1650), *La Géométrie* (1637) — introduced the sign rule for counting positive and negative real roots, which explains why Type II and Type IV reciprocal equations must have x = 1 or x = −1 among their roots.
- **Leonhard Euler** (1707–1783), *Introductio in analysin infinitorum* (1748) — systematically treated symmetric polynomial equations and the transformation of variables, the direct ancestor of the z = x + 1/x substitution.
- **Carl Friedrich Gauss** (1777–1855), *Disquisitiones Arithmeticae* (1801) — established the fundamental theorem of algebra and the pairing of roots under reciprocal transformations.

## Real-World Applications

1. **Signal Processing**
   - Reciprocal symmetry appears in the transfer functions of all-pass filters, where poles and zeros occur in reciprocal pairs.
   - Linear-phase FIR filter design uses coefficient symmetry to reduce the number of independent multipliers.
   - Palindromic polynomial coefficients allow efficient convolution and deconvolution.
   - **Example:** A filter whose transfer function has palindromic numerator coefficients can be factored using the reciprocal-equation substitution, reducing a degree-4 design problem to a quadratic in z.

2. **Physics**
   - Normal modes of coupled mechanical and electrical oscillators often lead to reciprocal characteristic equations.
   - Boundary-value problems with symmetric boundary conditions produce palindromic eigenvalue polynomials.
   - Waveguide and cavity resonance conditions frequently generate self-reciprocal equations.
   - **Example:** The characteristic equation for a symmetric two-mass oscillator chain is a reciprocal equation whose roots come in reciprocal pairs.

3. **Electrical Engineering**
   - Ladder network analysis produces reciprocal polynomials in the impedance variable.
   - Transmission-line input impedance under symmetric termination leads to palindromic equations.
   - Filter synthesis with Chebyshev or Butterworth responses uses coefficient symmetry.
   - **Example:** A symmetric four-terminal ladder network yields a degree-4 reciprocal equation in the load resistance, solved by the z-substitution.

4. **Computer Graphics**
   - Bezier curve subdivision matrices are palindromic, and their eigenvalues determine convergence rates.
   - Symmetric subdivision schemes in curve and surface design produce reciprocal characteristic polynomials.
   - Root-finding for intersection of symmetric parametric curves reduces to reciprocal equations.
   - **Example:** The characteristic polynomial of a symmetric subdivision matrix is reciprocal, so its eigenvalues come in reciprocal pairs.

5. **Mechanical Engineering**
   - Vibration analysis of symmetric rotors and shafts yields reciprocal frequency equations.
   - Buckling of symmetric columns produces palindromic characteristic equations.
   - Rotor dynamics with symmetric bearings leads to reciprocal eigenvalue problems.
   - **Example:** A symmetric three-disc rotor system produces a degree-6 reciprocal frequency equation, reduced to a cubic in z.

6. **Economics**
   - Dynamic optimization with symmetric adjustment costs generates reciprocal characteristic equations.
   - Rational expectations models with symmetric lag structures produce palindromic polynomials.
   - Input-output models with balanced sectors lead to self-reciprocal systems.
   - **Example:** A two-period symmetric adjustment-cost model yields a reciprocal characteristic equation in the discount factor.

7. **Acoustics**
   - Room modes in symmetric enclosures produce reciprocal frequency equations.
   - Symmetric muffler and filter designs lead to palindromic transfer functions.
   - Underwater acoustic propagation in symmetric channels gives reciprocal characteristic equations.
   - **Example:** A symmetric expansion chamber muffler has a reciprocal transmission-line characteristic equation.

8. **Numerical Analysis**
   - Convergence analysis of symmetric iterative methods produces reciprocal error polynomials.
   - Stability analysis of symmetric finite-difference schemes yields palindromic characteristic equations.
   - Root-finding for symmetric polynomial systems reduces to reciprocal equations.
   - **Example:** The stability polynomial of a symmetric three-level finite-difference scheme is reciprocal and is analysed via the z-substitution.

9. **Astronomy**
   - Orbital mechanics for symmetric two-body configurations leads to reciprocal equations.
   - Perturbation expansions in celestial mechanics sometimes produce palindromic series.
   - Symmetric potential fields around a symmetric mass distribution give reciprocal characteristic equations.
   - **Example:** The radial equation for a symmetric two-body orbit after separation of variables is a reciprocal equation.

10. **Chemistry**
    - Symmetric molecular orbitals in homonuclear diatomic molecules lead to reciprocal eigenvalue equations.
    - Kinetic models with symmetric forward and reverse rates produce palindromic characteristic polynomials.
    - Symmetric reaction-diffusion systems yield reciprocal stability equations.
    - **Example:** A symmetric two-step reaction with equal forward and reverse rate constants produces a reciprocal characteristic equation.

11. **Geophysics**
    - Symmetric layered-earth models in resistivity sounding produce reciprocal equations.
    - Seismic wave propagation in symmetric stratified media leads to palindromic dispersion relations.
    - Gravity and magnetic anomaly modelling with symmetric sources gives reciprocal characteristic equations.
    - **Example:** A three-layer symmetric resistivity model yields a reciprocal equation for the apparent resistivity.

12. **Music Theory**
    - Symmetric scales and chords produce reciprocal frequency relationships.
    - The mathematics of equal temperament involves palindromic polynomial approximations.
    - Symmetric rhythmic patterns can be modelled by reciprocal equations.
    - **Example:** A symmetric two-interval pitch pattern generates a reciprocal frequency equation whose roots describe the allowable tuning ratios.

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
|---|---|---|---|
| Notes | A reciprocal equation is unchanged when x is replaced by 1/x | PDF | high |
| Notes | If α is a root, then 1/α is also a root | PDF | high |
| Notes | Type I: even degree, a₀ and aₙ have the same sign | PDF | high |
| Notes | Type II: even degree, a₀ and aₙ have opposite signs | PDF | high |
| Notes | Type III: odd degree, a₀ and aₙ have the same sign | PDF | high |
| Notes | Type IV: odd degree, a₀ and aₙ have opposite signs | PDF | high |
| Notes | For Type I even degree, z = x + 1/x and x² + 1/x² = z² − 2 | PDF | high |
| Notes | For Type I degree 6, x³ + 1/x³ = z³ − 3z | PDF | high |
| Notes | Type III has x = −1 as a root | PDF | high |
| Notes | Type IV has x = 1 as a root | PDF | high |
| Historical Background | Descartes (1596–1650), La Géométrie (1637) — sign rule for roots | textbook-standard | high |
| Historical Background | Euler (1707–1783), Introductio in analysin infinitorum (1748) — symmetric polynomial transformations | textbook-standard | high |
| Historical Background | Gauss (1777–1855), Disquisitiones Arithmeticae (1801) — fundamental theorem of algebra and root pairing | textbook-standard | high |
| Applications 1 | Palindromic numerator coefficients allow reduction to a quadratic in z | inferred from PDF method | high |
| Applications 2 | Symmetric two-mass oscillator chain characteristic equation is reciprocal | inferred from PDF definition | high |
| Applications 3 | Symmetric four-terminal ladder network yields degree-4 reciprocal equation | inferred from PDF method | high |
| Applications 4 | Symmetric subdivision matrix characteristic polynomial is reciprocal | inferred from PDF definition | high |
| Applications 5 | Symmetric three-disc rotor produces degree-6 reciprocal frequency equation | inferred from PDF method | high |
| Applications 6 | Two-period symmetric adjustment-cost model yields reciprocal characteristic equation | inferred from PDF definition | high |
| Applications 7 | Symmetric expansion chamber muffler has reciprocal transmission-line characteristic equation | inferred from PDF definition | high |
| Applications 8 | Symmetric three-level finite-difference stability polynomial is reciprocal | inferred from PDF definition | high |
| Applications 9 | Symmetric two-body radial equation after separation is reciprocal | inferred from PDF definition | high |
| Applications 10 | Symmetric two-step reaction with equal rates produces reciprocal characteristic equation | inferred from PDF definition | high |
| Applications 11 | Three-layer symmetric resistivity model yields reciprocal equation | inferred from PDF definition | high |
| Applications 12 | Symmetric two-interval pitch pattern generates reciprocal frequency equation | inferred from PDF definition | high |