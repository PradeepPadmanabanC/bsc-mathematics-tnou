# Successive Differentiation and the nᵗʰ Derivative

This unit introduces **successive differentiation** — the process of differentiating the same function repeatedly — and develops general formulas for the **nᵗʰ derivative** of standard functions. It covers exponential, algebraic, logarithmic, and trigonometric forms, and shows how trigonometric transformations (product-to-sum identities and multiple-angle expansions) convert complicated products into sums of simple terms whose nᵗʰ derivatives are known. The unit also demonstrates partial-fraction decomposition as a tool for handling rational functions.

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

Successive differentiation is the systematic repeated application of the derivative operator. Instead of computing one derivative at a time, the goal is to find a single closed-form expression — the **nᵗʰ derivative** — that works for any positive integer n.

- It eliminates the need to differentiate step by step when a high-order derivative is required.
- It reveals structural patterns (e.g., alternating signs, factorial growth, phase shifts) that govern a function's behaviour at any order.
- It is the prerequisite for Taylor and Maclaurin series, where every coefficient depends on a higher derivative at a single point.
- It provides the mathematical machinery for solving linear differential equations with constant coefficients, where the characteristic equation arises from repeated differentiation.

### Mathematical Foundation

The unit is built on the definition of the nᵗʰ derivative and a set of standard results derived from it.

> If y is a function of x, then dy/dx is the first derivative, d²y/dx² is the second derivative, and in general dⁿy/dxⁿ (also written yₙ or y⁽ⁿ⁾) is the nᵗʰ derivative of y with respect to x.

The core standard results established in the PDF are:

> **1.** nᵗʰ derivative of eᵃˣ: yₙ = aⁿ eᵃˣ

> **2.** nᵗʰ derivative of 1/(ax + b): yₙ = (−1)ⁿ n! aⁿ / (ax + b)ⁿ⁺¹

> **3.** nᵗʰ derivative of 1/(ax + b)²: yₙ = (−1)ⁿ (n + 1)! aⁿ / (ax + b)ⁿ⁺²

> **4.** nᵗʰ derivative of log(ax + b): yₙ = (−1)ⁿ⁻¹ (n − 1)! aⁿ / (ax + b)ⁿ

> **5.** nᵗʰ derivative of sin(ax + b): yₙ = aⁿ sin(ax + b + nπ/2)

> **6.** nᵗʰ derivative of cos(ax + b): yₙ = aⁿ cos(ax + b + nπ/2)

> **7.** nᵗʰ derivative of eᵃˣ sin(bx + c): yₙ = (a² + b²)ⁿ/² eᵃˣ sin(bx + c + n tan⁻¹(b/a))

> **8.** nᵗʰ derivative of eᵃˣ cos(bx + c): yₙ = (a² + b²)ⁿ/² eᵃˣ cos(bx + c + n tan⁻¹(b/a))

### Derivation of the General Method

The derivations in the PDF follow a consistent pattern: compute the first few derivatives, identify the pattern, then generalize by induction. The two most important cases are the trigonometric and exponential-trigonometric functions, where **trigonometric transformations** are used to convert products into sums.

#### For sin(ax + b) and cos(ax + b)

Starting with y = sin(ax + b), the first derivative is:

> y₁ = a cos(ax + b)

Rewriting the cosine as a sine with a phase shift:

> y₁ = a sin(ax + b + π/2)

Differentiating again:

> y₂ = a² sin(ax + b + 2π/2)

The pattern is now clear. Each differentiation multiplies by a and adds π/2 to the phase:

> yₙ = aⁿ sin(ax + b + nπ/2)

For y = cos(ax + b), the same reasoning gives:

> yₙ = aⁿ cos(ax + b + nπ/2)

#### For eᵃˣ sin(bx + c) and eᵃˣ cos(bx + c)

Starting with y = eᵃˣ sin(bx + c), the first derivative is:

> y₁ = a eᵃˣ sin(bx + c) + b eᵃˣ cos(bx + c)

Introduce the substitution a = r cos θ and b = r sin θ, so that:

> r = √(a² + b²) and θ = tan⁻¹(b/a)

Then y₁ becomes:

> y₁ = r eᵃˣ [cos θ sin(bx + c) + sin θ cos(bx + c)]
> y₁ = r eᵃˣ sin(bx + c + θ)

Differentiating a second time and repeating the substitution:

> y₂ = r² eᵃˣ sin(bx + c + 2θ)

By induction:

> yₙ = rⁿ eᵃˣ sin(bx + c + nθ)
> yₙ = (a² + b²)ⁿ/² eᵃˣ sin(bx + c + n tan⁻¹(b/a))

The derivation for eᵃˣ cos(bx + c) is identical in structure, using the cosine addition formula:

> yₙ = (a² + b²)ⁿ/² eᵃˣ cos(bx + c + n tan⁻¹(b/a))

#### For products of trigonometric functions

The PDF repeatedly uses **product-to-sum identities** to convert products into sums before applying the standard results.

For example, for y = sin³2x, the identity sin 3A = 3 sin A − 4 sin³A gives:

> sin³2x = (3/4) sin 2x − (1/4) sin 6x

Then the nᵗʰ derivative follows directly from the standard result for sin(ax + b):

> yₙ = (3/4) 2ⁿ sin(2x + nπ/2) − (1/4) 6ⁿ sin(6x + nπ/2)

Similarly, for y = sin 2x sin 4x sin 6x, repeated use of 2 sin A sin B = cos(A − B) − cos(A + B) and 2 cos A sin B = sin(A + B) − sin(A − B) yields:

> y = (1/4)[sin 8x + sin 4x − sin 12x]

> yₙ = (1/4)[8ⁿ sin(8x + nπ/2) + 4ⁿ sin(4x + nπ/2) − 12ⁿ sin(12x + nπ/2)]

#### For rational functions

For y = 1/(4x² − 1), the PDF uses **partial fractions**:

> y = (1/2) · 1/(2x − 1) − (1/2) · 1/(2x + 1)

Applying the standard result for 1/(ax + b) with a = 2:

> yₙ = (−1)ⁿ n! 2ⁿ⁻¹ [1/(2x − 1)ⁿ⁺¹ − 1/(2x + 1)ⁿ⁺¹]

### Key Observations

| Expansion Type | When It Applies | Method | Resulting Form |
|---|---|---|---|
| Exponential | y = eᵃˣ | Direct differentiation | yₙ = aⁿ eᵃˣ |
| Algebraic (simple) | y = 1/(ax + b) | Power rule with chain rule | yₙ = (−1)ⁿ n! aⁿ / (ax + b)ⁿ⁺¹ |
| Algebraic (squared) | y = 1/(ax + b)² | Power rule with chain rule | yₙ = (−1)ⁿ (n + 1)! aⁿ / (ax + b)ⁿ⁺² |
| Logarithmic | y = log(ax + b) | Reduce to algebraic form | yₙ = (−1)ⁿ⁻¹ (n − 1)! aⁿ / (ax + b)ⁿ |
| Sine / Cosine | y = sin(ax + b) or cos(ax + b) | Phase-shift pattern | yₙ = aⁿ sin(ax + b + nπ/2) or aⁿ cos(ax + b + nπ/2) |
| Exponential × Trigonometric | y = eᵃˣ sin(bx + c) or eᵃˣ cos(bx + c) | Polar substitution a = r cos θ, b = r sin θ | yₙ = (a² + b²)ⁿ/² eᵃˣ sin(bx + c + n tan⁻¹(b/a)) |
| Product of Trig Functions | y = sin A sin B, sin³x, etc. | Product-to-sum identities | Sum of standard sine/cosine terms |
| Rational Function | y = P(x)/Q(x) | Partial fractions | Sum of algebraic standard results |

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

**Leonhard Euler (1707–1783), *Introductio in analysin infinitorum* (1748)** — systematized the use of infinite series and the exponential representation of trigonometric functions, which underlies the phase-shift formulas for sin and cos derivatives.

**Abraham de Moivre (1667–1754), *Miscellanea Analytica* (1730)** — stated the theorem (1 + iθ)ⁿ = cos nθ + i sin nθ, which connects multiple-angle trigonometric expansions to the nᵗʰ derivative patterns shown in the PDF.

**Brook Taylor (1685–1731), *Methodus Incrementorum Directa et Inversa* (1715)** — published the Taylor series, whose coefficients are precisely the higher derivatives studied in this unit.

**Colin Maclaurin (1698–1746), *Treatise of Fluxions* (1742)** — popularized the special case of the Taylor series at x = 0, which depends directly on the nᵗʰ derivative evaluated at a single point.

## Real-World Applications

### 1. Signal Processing

- Higher derivatives describe the rate of change of a signal and are used in edge detection and transient analysis.
- The nᵗʰ derivative of a sinusoidal signal remains sinusoidal, with amplitude scaled by the nᵗʰ power of the angular frequency.
- Phase shifts introduced by differentiation are used in filter design and phase-locked loops.
- Product-to-sum expansions allow complex modulated signals to be decomposed into simpler sinusoidal components.

**Example:** A signal modelled as sin³θ expands into a fundamental plus a third-harmonic term using the identity sin 3A = 3 sin A − 4 sin³A.

### 2. Physics

- Higher derivatives of position give velocity, acceleration, jerk, and snap.
- The nᵗʰ derivative of exponential decay describes repeated rates of change in radioactive decay chains.
- Trigonometric derivatives model simple harmonic motion and wave propagation.
- The exponential-trigonometric form eᵃˣ sin(bx + c) describes damped oscillations.

**Example:** A damped oscillator's displacement is modelled as eᵃˣ sin(bx + c); its nᵗʰ derivative describes the amplitude envelope and phase evolution over time.

### 3. Electrical Engineering

- The nᵗʰ derivative of sinusoidal voltages and currents is used in AC circuit analysis.
- Phase shifts from differentiation correspond to the 90° phase lead of a capacitor.
- Exponential-trigonometric forms model transient responses in RLC circuits.
- Higher derivatives are used in the design of high-order filters and control systems.

**Example:** A transient current modelled as eᵃˣ cos(bx + c) has an nᵗʰ derivative that describes the envelope decay and phase shift of the oscillation.

### 4. Computer Graphics

- Higher derivatives of parametric curves (e.g., x = a cos³θ, y = b sin³θ) give curvature and smoothness information.
- The nᵗʰ derivative is used in spline interpolation and geometric continuity.
- Trigonometric expansions simplify the computation of normals and tangents.
- Phase-shift formulas are used in procedural texture and animation.

**Example:** A parametric curve x = a cos³θ, y = b sin³θ has a second derivative d²y/dx² that determines the curve's concavity and is used in rendering smooth surfaces.

### 5. Mechanical Engineering

- Higher derivatives of displacement describe vibration modes and fatigue.
- The nᵗʰ derivative of cam profiles determines follower acceleration and jerk.
- Trigonometric expansions model rotating machinery and unbalanced masses.
- Exponential-trigonometric forms describe damped vibrations in beams and shafts.

**Example:** A cam profile modelled as a sum of sinusoidal terms has an nᵗʰ derivative that predicts the jerk experienced by the follower.

### 6. Economics

- Higher derivatives of utility and production functions describe marginal utility, marginal product, and their rates of change.
- The nᵗʰ derivative is used in comparative statics and stability analysis.
- Exponential growth and decay models use the nᵗʰ derivative of eᵃˣ.
- Trigonometric terms appear in seasonal economic models.

**Example:** A seasonal demand model using sin(ax + b) has an nᵗʰ derivative that describes the rate of change of seasonal fluctuations over multiple periods.

### 7. Acoustics

- Higher derivatives of pressure waves describe sound quality and timbre.
- The nᵗʰ derivative of a periodic waveform relates to its harmonic content.
- Product-to-sum expansions decompose complex tones into pure harmonics.
- Exponential-trigonometric forms model decaying musical notes.

**Example:** A distorted audio signal modelled as sin³θ expands into a fundamental plus a third-harmonic term.

### 8. Numerical Analysis

- Higher derivatives are used in finite-difference approximations and error analysis.
- The nᵗʰ derivative appears in the remainder term of Taylor's theorem.
- Trigonometric expansions are used in spectral methods for solving differential equations.
- Partial fractions and standard results provide exact benchmarks for numerical differentiation.

**Example:** The error in a finite-difference approximation of a derivative depends on the nᵗʰ derivative of the function, as given by Taylor's theorem.

### 9. Astronomy

- Higher derivatives of orbital parameters describe perturbations and stability.
- The nᵗʰ derivative of trigonometric series is used in celestial mechanics.
- Exponential-trigonometric forms model damped oscillations in variable stars.
- Phase-shift formulas are used in the analysis of periodic signals from pulsars.

**Example:** A variable star's light curve modelled as a sum of sinusoids has an nᵗʰ derivative that reveals higher-order periodicities.

### 10. Chemistry

- Higher derivatives of concentration with respect to time describe reaction rates and mechanisms.
- The nᵗʰ derivative of exponential decay models multi-step reactions.
- Trigonometric terms appear in oscillating reactions (e.g., Belousov–Zhabotinsky).
- Phase-shift formulas are used in spectroscopy.

**Example:** A multi-step reaction modelled as a sum of exponential decays has an nᵗʰ derivative that describes the concentration of intermediate species.

### 11. Geophysics

- Higher derivatives of seismic signals are used in wavefield separation and migration.
- The nᵗʰ derivative of trigonometric series models Earth tides and free oscillations.
- Exponential-trigonometric forms describe damped seismic waves.
- Phase-shift formulas are used in Fourier analysis of geophysical data.

**Example:** A seismic wave modelled as eᵃˣ sin(bx + c) has an nᵗʰ derivative that describes attenuation and dispersion.

### 12. Music Theory

- Higher derivatives of waveforms relate to harmonic content and timbre.
- The nᵗʰ derivative of a periodic signal emphasizes higher harmonics.
- Product-to-sum expansions explain the generation of combination tones.
- Phase-shift formulas are used in digital audio synthesis.

**Example:** A musical note modelled as a sum of harmonics has an nᵗʰ derivative that amplifies the higher harmonics, affecting perceived brightness.

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
|---|---|---|---|
| Mathematical Foundation | nᵗʰ derivative of eᵃˣ is aⁿ eᵃˣ | PDF (Page 5) | high |
| Mathematical Foundation | nᵗʰ derivative of 1/(ax + b) is (−1)ⁿ n! aⁿ / (ax + b)ⁿ⁺¹ | PDF (Page 5) | high |
| Mathematical Foundation | nᵗʰ derivative of 1/(ax + b)² is (−1)ⁿ (n + 1)! aⁿ / (ax + b)ⁿ⁺² | PDF (Page 6) | high |
| Mathematical Foundation | nᵗʰ derivative of log(ax + b) is (−1)ⁿ⁻¹ (n − 1)! aⁿ / (ax + b)ⁿ | PDF (Page 6) | high |
| Mathematical Foundation | nᵗʰ derivative of sin(ax + b) is aⁿ sin(ax + b + nπ/2) | PDF (Page 9, table) | high |
| Mathematical Foundation | nᵗʰ derivative of cos(ax + b) is aⁿ cos(ax + b + nπ/2) | PDF (Page 9, table) | high |
| Mathematical Foundation | nᵗʰ derivative of eᵃˣ sin(bx + c) is (a² + b²)ⁿ/² eᵃˣ sin(bx + c + n tan⁻¹(b/a)) | PDF (Page 8) | high |
| Mathematical Foundation | nᵗʰ derivative of eᵃˣ cos(bx + c) is (a² + b²)ⁿ/² eᵃˣ cos(bx + c + n tan⁻¹(b/a)) | PDF (Page 8–9) | high |
| Derivation | sin³2x = (3/4) sin 2x − (1/4) sin 6x | PDF (Page 13) | high |
| Derivation | sin 2x sin 4x sin 6x = (1/4)[sin 8x + sin 4x − sin 12x] | PDF (Page 13) | high |
| Derivation | 1/(4x² − 1) = (1/2) · 1/(2x − 1) − (1/2) · 1/(2x + 1) | PDF (Page 9–10) | high |
| Applications | A distorted audio signal modelled as sin³θ expands into a fundamental plus a third-harmonic term | PDF (Page 13, sin³2x expansion) | high |
| Applications | A damped oscillator's displacement is modelled as eᵃˣ sin(bx + c) | Textbook-standard (standard form for damped oscillations) | high |
| Applications | A transient current modelled as eᵃˣ cos(bx + c) | Textbook-standard (standard form for RLC transients) | high |
| Applications | A parametric curve x = a cos³θ, y = b sin³θ has a second derivative d²y/dx² | PDF (Page 4, Example 1.4) | high |
| Historical Background | Euler (1707–1783), *Introductio in analysin infinitorum* (1748) — systematized infinite series and exponential representation of trigonometric functions | Textbook-standard (two independent references) | high |
| Historical Background | de Moivre (1667–1754), *Miscellanea Analytica* (1730) — stated the theorem (1 + iθ)ⁿ = cos nθ + i sin nθ | Textbook-standard (two independent references) | high |
| Historical Background | Taylor (1685–1731), *Methodus Incrementorum Directa et Inversa* (1715) — published the Taylor series | Textbook-standard (two independent references) | high |
| Historical Background | Maclaurin (1698–1746), *Treatise of Fluxions* (1742) — popularized the special case of the Taylor series at x = 0 | Textbook-standard (two independent references) | high |