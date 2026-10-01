# Hyperbolic Functions

This set of study notes introduces **hyperbolic functions** — cosh x, sinh x, tanh x, and their reciprocals — defined from the exponential function. The notes derive the fundamental identities connecting hyperbolic functions to circular trigonometric functions via the substitution θ = ix, prove the standard hyperbolic identities, and work through a large collection of problems involving real and imaginary parts of complex trigonometric and hyperbolic expressions. The unit concludes with the technique of expressing powers of sinh x and cosh x (for example sinh⁵x, cosh⁶x) as linear combinations of hyperbolic sines or cosines of multiples of x, using binomial expansion and exponential definitions.

## Table of Contents

1. [Notes](#notes)
   - [Overview](#overview)
   - [Mathematical Foundation](#mathematical-foundation)
   - [Derivation of the General Method](#derivation-of-the-general-method)
     - [For coshⁿx](#for-coshnx)
     - [For sinhⁿx](#for-sinhnx)
   - [Key Observations](#key-observations)
2. [Historical Background](#historical-background)
3. [Real-World Applications](#real-world-applications)
4. [Self-Audit](#self-audit)

## Notes

### Overview

Hyperbolic functions are the exponential analogues of the circular trigonometric functions. They matter because they let us move fluently between exponential, trigonometric, and hyperbolic forms of the same expression — a skill that is essential for complex analysis, differential equations, and engineering.

- They turn products and powers of exponentials into clean sums of hyperbolic functions of multiples, which is the key to linearising expressions.
- They give the real and imaginary parts of complex trigonometric functions directly, without needing to manipulate imaginary arguments from scratch.
- They satisfy identities that mirror the Pythagorean identities, so many trigonometric manipulations carry over with only a sign change.
- They appear naturally in solutions of the wave equation, the heat equation, and the catenary problem, so the algebraic technique of expanding powers of sinh and cosh is used repeatedly in applied work.

### Mathematical Foundation

The two defining expressions are:

> cosh x = (eˣ + e⁻ˣ)/2

> sinh x = (eˣ − e⁻ˣ)/2

From these definitions the notes derive the relations between circular and hyperbolic functions by substituting θ = ix into the circular identities:

> cos(ix) = cosh x

> sin(ix) = i sinh x

> tan(ix) = i tanh x

The fundamental hyperbolic identities are:

> cosh²x − sinh²x = 1

> tanh²x + sech²x = 1

> coth²x − cosech²x = 1

> 2 cosh²x = cosh 2x + 1

> 2 sinh²x = cosh 2x − 1

> sinh 2x = 2 sinh x cosh x

> sinh 3x = 3 sinh x + 4 sinh³x

> cosh 3x = 4 cosh³x − 3 cosh x

### Derivation of the General Method

The goal is to rewrite a power such as sinhⁿx or coshⁿx as a sum of hyperbolic functions of multiples of x. The method is always the same: expand the power of the exponential definition with the binomial theorem, collect terms in pairs eᵏˣ ± e⁻ᵏˣ, and recognise each pair as 2 cosh kx or 2 sinh kx.

#### For coshⁿx

Start from the definition:

> cosh x = (eˣ + e⁻ˣ)/2

Raise both sides to the power n:

> coshⁿx = (1/2ⁿ)(eˣ + e⁻ˣ)ⁿ

Expand the binomial:

> coshⁿx = (1/2ⁿ) Σₖ₌₀ⁿ C(n, k) e⁽ⁿ⁻ᵏ⁾ˣ e⁻ᵏˣ

Combine the exponents:

> coshⁿx = (1/2ⁿ) Σₖ₌₀ⁿ C(n, k) e⁽ⁿ⁻²ᵏ⁾ˣ

Pair the term k with the term n − k, which has exponent −(n − 2k)x. Each pair is:

> e⁽ⁿ⁻²ᵏ⁾ˣ + e⁻⁽ⁿ⁻²ᵏ⁾ˣ = 2 cosh((n − 2k)x)

so the whole sum becomes a linear combination of cosh of multiples of x. The constant term appears when n is even and k = n/2.

**Worked example (cosh⁵x):**

> cosh⁵x = (1/2⁵)(eˣ + e⁻ˣ)⁵

> = (1/2⁵)[e⁵ˣ + 5e³ˣ + 10eˣ + 10e⁻ˣ + 5e⁻³ˣ + e⁻⁵ˣ]

> = (1/2⁵)[(e⁵ˣ + e⁻⁵ˣ) + 5(e³ˣ + e⁻³ˣ) + 10(eˣ + e⁻ˣ)]

> = (1/2⁵)[2 cosh 5x + 5(2 cosh 3x) + 10(2 cosh x)]

> = (1/16)[cosh 5x + 5 cosh 3x + 10 cosh x]

**Worked example (cosh⁶x):**

> cosh⁶x = (1/2⁶)[(e⁶ˣ + e⁻⁶ˣ) + 6(e⁴ˣ + e⁻⁴ˣ) + 15(e²ˣ + e⁻²ˣ) + 20]

> = (1/2⁶)[2 cosh 6x + 6(2 cosh 4x) + 15(2 cosh 2x) + 20]

> = (1/32)[cosh 6x + 6 cosh 4x + 15 cosh 2x + 10]

#### For sinhⁿx

Start from the definition:

> sinh x = (eˣ − e⁻ˣ)/2

Raise both sides to the power n:

> sinhⁿx = (1/2ⁿ)(eˣ − e⁻ˣ)ⁿ

Expand the binomial:

> sinhⁿx = (1/2ⁿ) Σₖ₌₀ⁿ C(n, k) e⁽ⁿ⁻ᵏ⁾ˣ (−1)ᵏ e⁻ᵏˣ

Combine the exponents and the sign:

> sinhⁿx = (1/2ⁿ) Σₖ₌₀ⁿ (−1)ᵏ C(n, k) e⁽ⁿ⁻²ᵏ⁾ˣ

Pair the term k with the term n − k. Because of the alternating sign, the pairs behave differently depending on whether n is even or odd.

- If n is odd, the pairs are of the form eᵏˣ − e⁻ᵏˣ, so the result is a sum of **sinh** of odd multiples of x.
- If n is even, the pairs are of the form eᵏˣ + e⁻ᵏˣ, so the result is a sum of **cosh** of even multiples of x plus a constant.

**Worked example (sinh⁵x):**

> sinh⁵x = (1/2⁵)(eˣ − e⁻ˣ)⁵

> = (1/2⁵)[e⁵ˣ − 5e³ˣ + 10eˣ − 10e⁻ˣ + 5e⁻³ˣ − e⁻⁵ˣ]

> = (1/2⁵)[(e⁵ˣ − e⁻⁵ˣ) − 5(e³ˣ − e⁻³ˣ) + 10(eˣ − e⁻ˣ)]

> = (1/2⁵)[2 sinh 5x − 5(2 sinh 3x) + 10(2 sinh x)]

> = (1/16)[sinh 5x − 5 sinh 3x + 10 sinh x]

**Worked example (sinh⁶x):**

> sinh⁶x = (1/2⁶)(eˣ − e⁻ˣ)⁶

> = (1/2⁶)[e⁶ˣ − 6e⁴ˣ + 15e²ˣ − 20 + 15e⁻²ˣ − 6e⁻⁴ˣ + e⁻⁶ˣ]

> = (1/2⁶)[(e⁶ˣ + e⁻⁶ˣ) − 6(e⁴ˣ + e⁻⁴ˣ) + 15(e²ˣ + e⁻²ˣ) − 20]

> = (1/2⁶)[2 cosh 6x − 6(2 cosh 4x) + 15(2 cosh 2x) − 20]

> = (1/32)[cosh 6x − 6 cosh 4x + 15 cosh 2x − 10]

### Key Observations

| Expression type | Exponential form used | Result contains | Constant term? |
|---|---|---|---|
| coshⁿx, n even | (eˣ + e⁻ˣ)ⁿ / 2ⁿ | cosh of even multiples of x | Yes |
| coshⁿx, n odd | (eˣ + e⁻ˣ)ⁿ / 2ⁿ | cosh of odd multiples of x | No |
| sinhⁿx, n even | (eˣ − e⁻ˣ)ⁿ / 2ⁿ | cosh of even multiples of x | Yes |
| sinhⁿx, n odd | (eˣ − e⁻ˣ)ⁿ / 2ⁿ | sinh of odd multiples of x | No |

The same binomial-expansion method also gives the real and imaginary parts of complex trigonometric functions, by writing the function in exponential form and substituting θ = ix where needed.

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

Leonhard Euler (1707–1783), *Introductio in analysin infinitorum* (1748) — gave the exponential definitions of the trigonometric functions and the formula e^(iθ) = cos θ + i sin θ, which is the starting point for the substitution θ = ix used throughout these notes.

Vincenzo Riccati (1707–1775), *Opusculorum ad res physicas et mathematicas pertinentium* (1757) — introduced the hyperbolic functions and their notation in the course of solving geometric problems.

Johann Heinrich Lambert (1728–1777), *Mémoire sur quelques propriétés remarquables des quantités transcendantes circulaires et logarithmiques* (1768) — established the parallel between circular and hyperbolic trigonometry, including the analogue of the addition formulas.

## Real-World Applications

1. **Signal Processing**
   - Hyperbolic expansions are used to linearise nonlinear distortion products in signal chains.
   - Expressing a power of a sinusoid as a sum of harmonics is the same algebra as expressing sinhⁿx as a sum of sinh kx.
   - Filter design sometimes uses cosh and sinh to shape passband and stopband responses.
   - **Example:** A distorted audio signal modelled as sin³θ expands into a fundamental plus a third-harmonic term.

2. **Physics**
   - Hyperbolic functions describe the shape of a hanging chain (the catenary) and the profile of a soap film.
   - They appear in the solutions of the wave equation and the heat equation in rectangular geometries.
   - Relativistic velocity addition can be written compactly using tanh.
   - **Example:** The displacement of a hanging cable is modelled with cosh x.

3. **Electrical Engineering**
   - Transmission-line equations have solutions built from cosh and sinh of the propagation constant times distance.
   - Power-flow and impedance calculations on long lines use hyperbolic forms.
   - **Example:** The voltage along a lossless line is written as a combination of cosh and sinh of the line length times the propagation constant.

4. **Computer Graphics**
   - Hyperbolic functions are used in some spline and curve constructions.
   - They appear in the parameterisation of certain surfaces and in camera models.
   - **Example:** A curve shaped like a catenary is generated using cosh for the vertical coordinate.

5. **Mechanical Engineering**
   - Catenary solutions for cables and chains use cosh.
   - Hyperbolic functions appear in the analysis of beams on elastic foundations.
   - **Example:** The sag of a uniform cable between two supports is described by a cosh curve.

6. **Economics**
   - Hyperbolic discounting models use hyperbolic forms to describe time preference.
   - Some utility and demand functions are built from hyperbolic expressions.
   - **Example:** A hyperbolic discount function is used to model how a consumer values a future reward.

7. **Acoustics**
   - Standing-wave and duct-mode solutions involve sinh and cosh.
   - Nonlinear acoustic distortion produces harmonics that are analysed with the same power-expansion method.
   - **Example:** A nonlinear acoustic response modelled as a power of a sinusoid produces a set of harmonic terms.

8. **Numerical Analysis**
   - Series expansions of sinh and cosh are used to build stable numerical schemes.
   - Hyperbolic functions appear in the stability analysis of finite-difference schemes.
   - **Example:** A finite-difference stability condition is expressed using a cosh term.

9. **Astronomy**
   - Hyperbolic orbits and trajectories are described with sinh and cosh.
   - The geometry of gravitational slingshots uses hyperbolic functions.
   - **Example:** The position along a hyperbolic orbit is parameterised with sinh.

10. **Chemistry**
    - Hyperbolic functions appear in models of reaction rates and in the solution of diffusion equations.
    - **Example:** A diffusion profile in a semi-infinite medium is written with a cosh term.

11. **Geophysics**
    - Heat-flow and wave-propagation models in layered media use hyperbolic functions.
    - **Example:** The temperature profile in a layered crust is modelled with a cosh term.

12. **Music Theory**
    - Harmonic content of a distorted tone is analysed using the same power-to-multiple expansion.
    - **Example:** A tone with a nonlinear response produces a fundamental plus higher harmonics.

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
|---|---|---|---|
| Historical Background | Euler (1707–1783), *Introductio in analysin infinitorum* (1748) — gave exponential definitions and e^(iθ) = cos θ + i sin θ | textbook-standard | high |
| Historical Background | Riccati (1707–1775), *Opusculorum* (1757) — introduced hyperbolic functions and notation | textbook-standard | high |
| Historical Background | Lambert (1728–1777), *Mémoire* (1768) — established parallel between circular and hyperbolic trigonometry | textbook-standard | high |
| Mathematical Foundation | cosh x = (eˣ + e⁻ˣ)/2 | PDF | high |
| Mathematical Foundation | sinh x = (eˣ − e⁻ˣ)/2 | PDF | high |
| Mathematical Foundation | cos(ix) = cosh x | PDF | high |
| Mathematical Foundation | sin(ix) = i sinh x | PDF | high |
| Mathematical Foundation | tan(ix) = i tanh x | PDF | high |
| Mathematical Foundation | cosh²x − sinh²x = 1 | PDF | high |
| Mathematical Foundation | tanh²x + sech²x = 1 | PDF | high |
| Mathematical Foundation | coth²x − cosech²x = 1 | PDF | high |
| Mathematical Foundation | 2 cosh²x = cosh 2x + 1 | PDF | high |
| Mathematical Foundation | 2 sinh²x = cosh 2x − 1 | PDF | high |
| Mathematical Foundation | sinh 2x = 2 sinh x cosh x | PDF | high |
| Mathematical Foundation | sinh 3x = 3 sinh x + 4 sinh³x | PDF | high |
| Mathematical Foundation | cosh 3x = 4 cosh³x − 3 cosh x | PDF | high |
| Derivation | cosh⁵x = (1/16)[cosh 5x + 5 cosh 3x + 10 cosh x] | PDF | high |
| Derivation | cosh⁶x = (1/32)[cosh 6x + 6 cosh 4x + 15 cosh 2x + 10] | PDF | high |
| Derivation | sinh⁵x = (1/16)[sinh 5x − 5 sinh 3x + 10 sinh x] | PDF | high |
| Derivation | sinh⁶x = (1/32)[cosh 6x − 6 cosh 4x + 15 cosh 2x − 10] | PDF | high |
| Applications | Distorted audio signal modelled as sin³θ expands into fundamental plus third-harmonic term | textbook-standard | high |
| Applications | Hanging cable displacement modelled with cosh x | textbook-standard | high |
| Applications | Transmission-line voltage written with cosh and sinh | textbook-standard | high |
| Applications | Catenary curve generated using cosh | textbook-standard | high |
| Applications | Hyperbolic discounting used in economics | textbook-standard | high |
| Applications | Hyperbolic orbit position parameterised with sinh | textbook-standard | high |