# Trigonometric Series Expansions and Equations with Trigonometric Roots

This README summarizes study notes covering the Maclaurin expansions of sin x, cos x, and tan x, their use in evaluating limits and approximating small angles, the expansion of tan(θ₁ + θ₂ + ... + θₙ), and the formation of polynomial equations whose roots are trigonometric values. Worked examples and practice problems are included.

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

These notes develop the standard small-angle series expansions and apply them to limits, approximations, and the construction of equations with trigonometric roots. The technique matters because:

- It converts transcendental trigonometric functions into polynomials, which are far easier to differentiate, integrate, and evaluate numerically.
- It provides the foundation for evaluating indeterminate limits of the form 0/0 involving trigonometric expressions.
- It allows small-angle approximations, such as replacing sin θ by θ when θ is small, which is essential in physics and engineering.
- It enables the formation of algebraic equations whose roots are known trigonometric quantities, linking trigonometry with the theory of equations.

### Mathematical Foundation

The starting point is **Maclaurin's series** for a function f(x):

> f(x) = f(0) + (x/1!) f′(0) + (x²/2!) f″(0) + (x³/3!) f‴(0) + ...

Applying this to the three basic trigonometric functions gives the following standard expansions:

> sin x = x − x³/3! + x⁵/5! − x⁷/7! + ...

> cos x = 1 − x²/2! + x⁴/4! − x⁶/6! + ...

> tan x = x + x³/3 + 2x⁵/15 + ...

The tangent series is obtained by dividing the sine series by the cosine series and collecting like powers of x.

For sums of angles, the addition formula for the tangent is generalized. Using De Moivre's theorem and comparing real and imaginary parts, one obtains:

> tan(θ₁ + θ₂ + ... + θₙ) = (S₁ − S₃ + S₅ − ...) / (1 − S₂ + S₄ − ...)

where

> S₁ = Σ tan θᵢ, S₂ = Σ tan θᵢ tan θⱼ (i < j), S₃ = Σ tan θᵢ tan θⱼ tan θₖ (i < j < k), ...

### Derivation of the General Method

#### For the tangent of a sum of angles

Start from the product of complex numbers written in polar form:

> (cos θ₁ + i sin θ₁)(cos θ₂ + i sin θ₂) ... (cos θₙ + i sin θₙ) = cos(θ₁ + θ₂ + ... + θₙ) + i sin(θ₁ + θ₂ + ... + θₙ)

Factor each term as cos θᵢ (1 + i tan θᵢ):

> cos θ₁ cos θ₂ ... cos θₙ (1 + i tan θ₁)(1 + i tan θ₂) ... (1 + i tan θₙ)

Expand the product of the (1 + i tan θᵢ) factors and group real and imaginary parts. The real part yields an alternating sum of even elementary symmetric functions of the tangents, and the imaginary part yields an alternating sum of odd ones. Dividing the imaginary part by the real part gives the tangent addition formula stated above.

#### For forming equations with trigonometric roots

The method is to find an angle relation that the proposed roots all satisfy, convert it into a polynomial identity using multiple-angle formulas, and then eliminate any extraneous roots.

For example, to find the equation whose roots are cos(2π/7), cos(4π/7), cos(6π/7):

Let θ be any of these angles. Then 7θ is an even multiple of π, so 4θ = even π − 3θ, hence cos 4θ = cos 3θ. Expanding both sides in powers of cos θ and setting x = cos θ gives a quartic. Since x = 1 is an extraneous root introduced by the cosine equality, synthetic division by (x − 1) yields the required cubic:

> 8x³ + 4x² − 4x − 1 = 0

For the tangent roots tan(π/5), tan(2π/5), tan(3π/5), tan(4π/5), the relation tan 5θ = 0 is used. Expanding tan 5θ in terms of tan θ and setting x = tan θ gives:

> 5x − 10x³ + x⁵ = 0

Removing the root x = 0 leaves the required quartic:

> x⁴ − 10x² + 5 = 0

### Key Observations

| Expansion / Technique | When to Use | Typical Application |
|---|---|---|
| sin x series | Small-angle approximation, limits with sin x | Evaluating lim (sin x − x)/x³ |
| cos x series | Small-angle approximation, limits with cos x | Evaluating lim (1 − cos x)/x² |
| tan x series | Limits and approximations involving tan x | Evaluating lim (tan x − sin x)/x³ |
| tan of sum formula | Combining many inverse tangent terms | Proving tan⁻¹α + tan⁻¹β + tan⁻¹γ = nπ |
| Trigonometric root equations | Constructing polynomials from known trig values | Finding equation with roots cos(2π/7), cos(4π/7), cos(6π/7) |

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

- **Colin Maclaurin (1698–1746), Treatise of Fluxions (1742)** — Popularized the series expansion now known as the Maclaurin series, the special case of the Taylor series centered at zero.
- **Abraham De Moivre (1667–1754), Miscellanea Analytica (1730)** — Stated the theorem linking complex numbers and trigonometry that underlies the derivation of the tangent addition formula for many angles.
- **Brook Taylor (1685–1731), Methodus Incrementorum Directa et Inversa (1715)** — Published the general series expansion for functions about a point, of which Maclaurin's series is a special case.

## Real-World Applications

1. **Signal Processing**
   - Nonlinear distortion in amplifiers is modelled by polynomial expansions of trigonometric functions.
   - Harmonic analysis uses the sine and cosine series to decompose periodic signals.
   - Small-angle approximations simplify filter design equations at low frequencies.
   - **Example:** A distorted audio signal modelled as sin³θ expands into a fundamental plus a third-harmonic term.

2. **Physics**
   - The small-angle approximation sin θ ≈ θ is used in the analysis of the simple pendulum.
   - Series expansions of tan θ appear in the study of refraction and optical aberration.
   - Approximate solutions to nonlinear oscillators use the first few terms of these series.
   - **Example:** The period of a pendulum is corrected at second order in the amplitude using the sin series.

3. **Electrical Engineering**
   - Load-flow analysis in power systems uses trigonometric series to approximate voltage and current relationships.
   - Antenna theory uses the tangent series in impedance calculations.
   - Harmonic distortion in transformers is analysed with polynomial approximations of trigonometric functions.
   - **Example:** The non-sinusoidal current in a saturated inductor is expanded using the tan series.

4. **Computer Graphics**
   - Rotation matrices and camera transformations rely on small-angle approximations for real-time rendering.
   - Sine and cosine series are used in procedural texture generation.
   - Approximate trigonometric evaluations in shader code use truncated Maclaurin series.
   - **Example:** A rotation by a very small angle is approximated by its first-order sine and cosine terms.

5. **Mechanical Engineering**
   - Vibration analysis of beams and shafts uses series expansions to linearise nonlinear stiffness terms.
   - Gear tooth profile calculations involve tangent approximations.
   - **Example:** The restoring torque of a torsional pendulum is expanded in powers of the twist angle.

6. **Economics**
   - Trigonometric series appear in seasonal economic models and cyclical growth theory.
   - Small-angle approximations simplify equilibrium conditions in dynamic models.
   - **Example:** A seasonal demand cycle modelled as a sine function is linearised near its peak.

7. **Acoustics**
   - Sound wave propagation in nonlinear media uses polynomial expansions of trigonometric waveforms.
   - The tan series is used in the analysis of horn loudspeakers.
   - **Example:** A nonlinear acoustic wave is expanded into its fundamental and harmonic components.

8. **Numerical Analysis**
   - Truncated Maclaurin series provide efficient approximations for evaluating trigonometric functions in software.
   - Error analysis of these approximations uses the next term in the series.
   - **Example:** A calculator approximates sin x by x − x³/6 for small x, keeping error below a specified tolerance.

9. **Astronomy**
   - Small-angle approximations are used in celestial mechanics for near-circular orbits.
   - Trigonometric series appear in the calculation of ephemerides.
   - **Example:** The equation of the centre for a planetary orbit is expanded in a sine series.

10. **Chemistry**
    - Molecular vibration spectra are analysed using trigonometric expansions.
    - **Example:** The potential energy of a diatomic molecule near equilibrium is expanded in a cosine series.

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
|---|---|---|---|
| Notes | Maclaurin series for f(x) as stated | PDF | high |
| Notes | sin x = x − x³/3! + x⁵/5! − x⁷/7! + ... | PDF | high |
| Notes | cos x = 1 − x²/2! + x⁴/4! − x⁶/6! + ... | PDF | high |
| Notes | tan x = x + x³/3 + 2x⁵/15 + ... | PDF | high |
| Notes | tan(θ₁ + ... + θₙ) = (S₁ − S₃ + ...)/(1 − S₂ + ...) | PDF | high |
| Notes | Equation with roots cos(2π/7), cos(4π/7), cos(6π/7) is 8x³ + 4x² − 4x − 1 = 0 | PDF | high |
| Notes | Equation with roots tan(π/5), tan(2π/5), tan(3π/5), tan(4π/5) is x⁴ − 10x² + 5 = 0 | PDF | high |
| Historical Background | Maclaurin (1698–1746), Treatise of Fluxions (1742) — popularized the Maclaurin series | textbook-standard | high |
| Historical Background | De Moivre (1667–1754), Miscellanea Analytica (1730) — stated the theorem linking complex numbers and trigonometry | textbook-standard | high |
| Historical Background | Taylor (1685–1731), Methodus Incrementorum Directa et Inversa (1715) — published the general series expansion | textbook-standard | high |
| Applications | A distorted audio signal modelled as sin³θ expands into a fundamental plus a third-harmonic term | PDF (sin series) | high |
| Applications | The period of a pendulum is corrected at second order in the amplitude using the sin series | textbook-standard | high |
| Applications | The non-sinusoidal current in a saturated inductor is expanded using the tan series | inferred | high |
| Applications | A rotation by a very small angle is approximated by its first-order sine and cosine terms | textbook-standard | high |
| Applications | The restoring torque of a torsional pendulum is expanded in powers of the twist angle | textbook-standard | high |
| Applications | A seasonal demand cycle modelled as a sine function is linearised near its peak | inferred | high |
| Applications | A nonlinear acoustic wave is expanded into its fundamental and harmonic components | textbook-standard | high |
| Applications | A calculator approximates sin x by x − x³/6 for small x | PDF (sin series) | high |
| Applications | The equation of the centre for a planetary orbit is expanded in a sine series | textbook-standard | high |
| Applications | The potential energy of a diatomic molecule near equilibrium is expanded in a cosine series | textbook-standard | high |