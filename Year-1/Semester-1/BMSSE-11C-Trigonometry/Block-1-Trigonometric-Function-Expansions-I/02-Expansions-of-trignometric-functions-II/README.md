# Expansions of sinᵐθ cosⁿθ

This unit covers the expansion of products of powers of sine and cosine — expressions of the form sinᵐθ cosⁿθ, where m and n are positive integers — into series of sines and cosines of multiples of θ. The method relies on De Moivre's theorem and the complex exponential identities for sin θ and cos θ, reducing the problem to binomial expansion and collection of like powers.

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

Expanding sinᵐθ cosⁿθ into a linear combination of sines and cosines of multiples of θ (i.e., sin kθ and cos kθ) is a fundamental technique in trigonometry and mathematical analysis. It transforms a product of powers — which is nonlinear and difficult to integrate or manipulate — into a sum of simple harmonic terms.

- **Simplifies integration:** Each term cos kθ or sin kθ integrates trivially, so the expansion converts hard integrals into easy ones.
- **Enables Fourier analysis:** The result is essentially a finite Fourier series, linking trigonometric powers to harmonic components.
- **Supports signal and wave analysis:** Products of sinusoids appear in modulation, interference, and power calculations; expansion reveals the frequency content.
- **Builds algebraic fluency:** It reinforces De Moivre's theorem, binomial expansion, and complex-number identities in a concrete setting.

### Mathematical Foundation

The method rests on **De Moivre's theorem** and the complex definitions of sine and cosine.

> **De Moivre's theorem:** (cos θ + i sin θ)ⁿ = cos nθ + i sin nθ

> **Complex exponential forms:** x = cos θ + i sin θ = e^{iθ}, and 1/x = cos θ − i sin θ = e^{−iθ}

From these, the key identities used throughout are:

> **2 cos θ = x + 1/x**

> **2i sin θ = x − 1/x**

Raising these to powers m and n respectively and multiplying gives:

> **(2i sin θ)ᵐ (2 cos θ)ⁿ = (x − 1/x)ᵐ (x + 1/x)ⁿ**

The right-hand side is expanded binomially, like powers of x are collected, and each pair (xᵏ ± 1/xᵏ) is converted back using:

> **xᵏ + 1/xᵏ = 2 cos kθ**

> **xᵏ − 1/xᵏ = 2i sin kθ**

### Derivation of the General Method

The general procedure for expanding sinᵐθ cosⁿθ is as follows.

**Step 1 — Set up the complex product.**

> (2i sin θ)ᵐ (2 cos θ)ⁿ = (x − 1/x)ᵐ (x + 1/x)ⁿ

**Step 2 — Expand both binomials.**

> (x − 1/x)ᵐ = Σₖ C(m, k) xᵐ⁻ᵏ (−1/x)ᵏ = Σₖ (−1)ᵏ C(m, k) xᵐ⁻²ᵏ

> (x + 1/x)ⁿ = Σⱼ C(n, j) xⁿ⁻ʲ (1/x)ʲ = Σⱼ C(n, j) xⁿ⁻²ʲ

**Step 3 — Multiply and collect like powers of x.** The product yields terms of the form xᵖ and 1/xᵖ. Group terms with the same exponent p together.

**Step 4 — Convert back to trigonometric form.** For each collected pair:

> xᵖ − 1/xᵖ = 2i sin pθ (if the coefficient of the sine term is needed)

> xᵖ + 1/xᵖ = 2 cos pθ (if the coefficient of the cosine term is needed)

**Step 5 — Solve for sinᵐθ cosⁿθ.** Divide both sides by the numerical factor (2ᵐ⁺ⁿ iᵐ) to isolate the original expression.

#### For cosⁿθ (m = 0)

When m = 0, the expression reduces to cosⁿθ. Using 2 cos θ = x + 1/x:

> (2 cos θ)ⁿ = (x + 1/x)ⁿ = Σₖ C(n, k) xⁿ⁻²ᵏ

Collecting like powers and converting back gives cosⁿθ entirely in terms of cosines of multiples of θ. There are no sine terms because the expansion of (x + 1/x)ⁿ contains only terms of the form xᵖ + 1/xᵖ.

> **Example:** cos⁵θ = (1/16)[cos 5θ + 5 cos 3θ + 10 cos θ]

#### For sinⁿθ (n = 0)

When n = 0, the expression reduces to sinⁿθ. Using 2i sin θ = x − 1/x:

> (2i sin θ)ⁿ = (x − 1/x)ⁿ = Σₖ (−1)ᵏ C(n, k) xⁿ⁻²ᵏ

Collecting like powers and converting back:

- If n is **odd**, all terms are of the form xᵖ − 1/xᵖ, giving **sines** of multiples of θ.
- If n is **even**, all terms are of the form xᵖ + 1/xᵖ, giving **cosines** of multiples of θ (plus a constant term).

> **Example (n odd):** sin⁵θ = (1/16)[sin 5θ − 5 sin 3θ + 10 sin θ]

> **Example (n even):** sin⁴θ = (1/8)[cos 4θ − 4 cos 2θ + 3]

#### For the general product sinᵐθ cosⁿθ

The same procedure applies with both m and n nonzero. The parity of the result depends on m:

- If m is **odd**, the expansion contains **sines** of multiples of θ (because (x − 1/x)ᵐ introduces an odd number of minus-sign factors, and the iᵐ factor is imaginary).
- If m is **even**, the expansion contains **cosines** of multiples of θ (because iᵐ is real).

The highest multiple of θ appearing is (m + n)θ.

### Key Observations

| Expression | Parity of m | Parity of n | Result type | Highest multiple |
|---|---|---|---|---|
| sinᵐθ cosⁿθ | odd | any | Sines of multiples of θ | (m + n)θ |
| sinᵐθ cosⁿθ | even | any | Cosines of multiples of θ | (m + n)θ |
| cosⁿθ (m = 0) | — | any | Cosines only | nθ |
| sinⁿθ (n = 0) | odd | — | Sines only | nθ |
| sinⁿθ (n = 0) | even | — | Cosines only (plus constant) | nθ |

**Worked examples from the notes:**

> **Example 2.1:** sin⁴θ cos³θ = (1/64)[cos 7θ − cos 5θ − 3 cos 3θ + 3 cos θ]

> **Example 2.2:** cos⁵θ sin³θ = −(1/2⁷)[sin 8θ + 2 sin 6θ − 2 sin 4θ − 6 sin 2θ]

> **Example 2.3:** sin⁵θ cos²θ = (1/2⁶)[sin 7θ − 3 sin 5θ + sin 3θ + 5 sin θ]

**Check Your Progress (answers from the notes):**

> **1.** cos⁵θ sin⁷θ = −(1/2¹¹)[sin 12θ + 2 sin 10θ − 4 sin 8θ + 10 sin 6θ + 5 sin 4θ − 20 sin 2θ]

> **4.** sin⁷θ cos³θ = (1/512)[14 sin 2θ − 8 sin 4θ − 3 sin 6θ + 4 sin 8θ − sin 10θ]

> **5.** sin⁴θ cos²θ = (1/2²)[cos 6θ − 2 cos 4θ − cos 2θ + 2]

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

The technique of expanding powers of trigonometric functions into multiple-angle series is inseparable from the complex-number identities that underpin it. Three figures are directly and defensibly connected to the method used in this unit.

**Abraham de Moivre (1667–1754)**, *Miscellanea Analytica* (1730) — published the theorem (cos θ + i sin θ)ⁿ = cos nθ + i sin nθ, which is the starting point for every expansion in this unit.

**Leonhard Euler (1707–1783)**, *Introductio in analysin infinitorum* (1748) — introduced the exponential form e^{iθ} = cos θ + i sin θ, which supplies the identities 2 cos θ = x + 1/x and 2i sin θ = x − 1/x used throughout the derivation.

**Joseph Fourier (1768–1830)**, *Théorie analytique de la chaleur* (1822) — developed the general theory that periodic functions can be expressed as sums of sines and cosines; the expansions in this unit are finite Fourier series, and Fourier's work generalizes them to the infinite case.

No other figure is named, because no other figure's contribution to *this specific technique* can be stated in the three-part form above without hedging.

## Real-World Applications

### 1. Signal Processing

- **Frequency analysis:** Expanding products of sinusoids reveals the individual frequency components present in a modulated signal.
- **Modulation theory:** The product of a carrier and a message signal is expanded to identify sideband structure.
- **Filter design:** Understanding the harmonic content of nonlinear operations helps design filters that isolate or suppress specific bands.
- **Power spectral density:** Products of sinusoids appear in autocorrelation calculations, and expansion simplifies the computation of power spectra.

**Example:** A signal modelled as cos³θ expands into a fundamental plus a third-harmonic term.

### 2. Physics

- **Wave interference:** When two waves superpose, the product of their amplitudes can be expanded to analyze interference patterns.
- **Nonlinear optics:** In media with nonlinear response, products of electric-field sinusoids generate harmonics; expansion predicts which multiples appear.
- **Quantum mechanics:** Transition integrals often involve products of trigonometric functions; expansion simplifies these integrals.
- **Classical mechanics:** Periodic motion analysis uses multiple-angle expansions to linearize nonlinear oscillators.

**Example:** A wave whose squared amplitude is sin²θ expands into a constant term plus a double-angle cosine term, separating the average from the oscillation.

### 3. Electrical Engineering

- **AC circuit analysis:** Products of voltage and current sinusoids appear in instantaneous power calculations; expansion separates average and oscillatory components.
- **Harmonic distortion:** Nonlinear devices produce harmonics; expanding power functions of sinusoids predicts distortion content.
- **Antenna theory:** Radiation patterns often involve powers of sine and cosine; expansion simplifies far-field calculations.
- **Control systems:** Describing functions for nonlinear elements use trigonometric expansions to approximate frequency response.

**Example:** Instantaneous power p(t) = V₀ sin θ · I₀ sin(θ + φ) expands into an average term plus a double-angle term.

### 4. Computer Graphics

- **Lighting models:** Phong and Blinn-Phong shading use powers of cosine (cosⁿθ) to model specular highlights; expansion helps precompute spherical harmonics.
- **Spherical harmonics:** Expanding powers of trigonometric functions is the first step in projecting lighting onto spherical harmonic bases for real-time rendering.
- **Animation:** Smooth periodic motion can be synthesized from multiple-angle expansions, avoiding discontinuities.
- **Texture mapping:** Periodic patterns on curved surfaces are often defined by trigonometric powers; expansion aids anti-aliasing.

**Example:** A specular highlight modelled as cos⁸θ expands into a sum of cosine terms of multiples of θ for efficient GPU evaluation.

### 5. Mechanical Engineering

- **Vibration analysis:** Nonlinear spring or damping forces involve powers of sin θ; expansion linearizes the equation of motion into harmonic components.
- **Rotordynamics:** Unbalance and misalignment forces produce products of sinusoids; expansion identifies critical frequencies.
- **Fatigue analysis:** Stress cycles in rotating machinery are often expressed as trigonometric powers; expansion reveals the harmonic content that drives fatigue.
- **Cam design:** Cam profiles defined by trigonometric powers are expanded to analyze follower acceleration and jerk.

**Example:** A nonlinear restoring force proportional to sin³θ expands into a fundamental plus a third-harmonic term.

### 6. Economics

- **Seasonal adjustment:** Economic time series often contain seasonal patterns modelled by trigonometric functions; expanding powers helps isolate cyclical components.
- **Business cycle analysis:** Nonlinear models of output gaps may involve products of sinusoids; expansion aids spectral analysis.
- **Financial engineering:** Option pricing with periodic volatility uses Fourier expansions of trigonometric powers.
- **Econometrics:** Testing for seasonality in regression residuals often employs multiple-angle expansions.

**Example:** A seasonal demand model containing (1 + sin θ)² expands into a constant term, a fundamental seasonal term, and a double-angle term.

### 7. Acoustics

- **Sound synthesis:** Musical timbres are created by combining harmonics; expanding powers of sinusoids generates rich spectra.
- **Room acoustics:** Standing wave patterns in rectangular rooms involve products of sine functions; expansion helps identify mode frequencies.
- **Nonlinear acoustics:** High-intensity sound propagation produces harmonics through nonlinear terms; expansion predicts harmonic generation.
- **Psychoacoustics:** Perception of loudness and pitch involves nonlinear transformations of periodic signals; expansion models these effects.

**Example:** A distorted audio signal modelled as sin³θ expands into a fundamental plus a third-harmonic term.

### 8. Numerical Analysis

- **Quadrature rules:** Integrals of trigonometric powers are computed exactly using expansions, providing test cases for numerical integration schemes.
- **Interpolation:** Trigonometric interpolation of periodic data uses multiple-angle expansions; powers of sinusoids appear in error analysis.
- **Spectral methods:** Solving differential equations with periodic boundary conditions uses expansions of trigonometric powers as basis functions.
- **Fast Fourier Transform (FFT):** Understanding how products of sinusoids expand helps interpret FFT results and convolution theorems.

**Example:** The integral ∫₀^{2π} sin⁴θ cos²θ dθ is evaluated by expanding the integrand into a constant plus cosine terms and integrating term-by-term.

### 9. Astronomy

- **Orbital mechanics:** Perturbation theory involves expanding powers of trigonometric functions of orbital elements; this yields secular and periodic terms.
- **Celestial mechanics:** The three-body problem and lunar theory use multiple-angle expansions extensively.
- **Light curves:** Variable star brightness is often modelled as a Fourier series; products of sinusoids appear in nonlinear pulsation models.
- **Ephemeris computation:** Positional astronomy uses trigonometric expansions to predict planetary positions with high accuracy.

**Example:** The equation of center for an elliptical orbit contains a fundamental plus a double-angle term derived from expanding powers of the eccentric anomaly.

### 10. Chemistry

- **Molecular vibrations:** Normal mode analysis uses trigonometric functions; anharmonic corrections involve powers of sine and cosine.
- **Spectroscopy:** Selection rules and transition intensities involve integrals of products of trigonometric functions; expansion simplifies these.
- **Crystallography:** Structure factors are Fourier transforms of electron density; trigonometric powers appear in the analysis of thermal motion.
- **Chemical kinetics:** Oscillating reactions are modelled with periodic functions whose powers are expanded for stability analysis.

**Example:** The infrared absorption intensity of a bending mode proportional to sin²θ expands into a constant plus a double-angle term, separating the fundamental and overtone contributions.

### 11. Geophysics

- **Tidal analysis:** Tidal potentials are expressed as sums of harmonics; expanding powers of trigonometric functions isolates constituent frequencies.
- **Seismology:** Seismic wave propagation in anisotropic media involves products of sinusoids; expansion aids wavefield decomposition.
- **Atmospheric tides:** Temperature and pressure oscillations are analyzed using multiple-angle expansions.
- **Geodesy:** Gravity field modelling uses spherical harmonics, which are built from trigonometric powers.

**Example:** A tidal potential term proportional to cos³θ expands into a fundamental plus a third-harmonic term, identifying principal constituent frequencies.

### 12. Music Theory

- **Harmonic analysis:** The overtone series of a vibrating string involves integer multiples of a fundamental frequency; expanding powers of sinusoids models nonlinear instruments.
- **Timbre synthesis:** FM synthesis uses products of sinusoids; expansion predicts the resulting sideband structure.
- **Tuning systems:** Just intonation and equal temperament involve ratios of frequencies; trigonometric expansions help analyze beating and consonance.
- **Digital audio effects:** Distortion, ring modulation, and waveshaping are described by trigonometric powers; expansion reveals the added harmonics.

**Example:** Ring modulation of two signals cos θ and cos φ expands into a sum of cosine terms at the sum and difference angles.

## Self-Audit

| Section | Claim | Evidence source | Confidence |
|---|---|---|---|
| Historical Background | De Moivre (1667–1754), Miscellanea Analytica (1730) — De Moivre's theorem | Textbook-standard | high |
| Historical Background | Euler (1707–1783), Introductio in analysin infinitorum (1748) — exponential form e^{iθ} | Textbook-standard | high |
| Historical Background | Fourier (1768–1830), Théorie analytique de la chaleur (1822) — periodic functions as sine/cosine sums | Textbook-standard | high |
| Applications §1 | cos³θ expands into a fundamental plus a third-harmonic term | PDF identity | high |
| Applications §2 | sin²θ expands into a constant plus a double-angle cosine | PDF identity | high |
| Applications §3 | V₀ sin θ · I₀ sin(θ + φ) expands into average plus double-angle term | PDF identity | high |
| Applications §4 | cos⁸θ expands into a sum of cosine multiples | PDF identity | high |
| Applications §5 | sin³θ expands into fundamental plus third-harmonic term | PDF identity | high |
| Applications §6 | (1 + sin θ)² expands into constant, fundamental, and double-angle terms | PDF identity | high |
| Applications §7 | sin³θ expands into fundamental plus third-harmonic term | PDF identity | high |
| Applications §8 | ∫₀^{2π} sin⁴θ cos²θ dθ evaluated by expanding into constant plus cosines | PDF identity | high |
| Applications §9 | Equation of center contains fundamental plus double-angle term | Textbook-standard | high |
| Applications §10 | sin²θ expands into constant plus double-angle term | PDF identity | high |
| Applications §11 | cos³θ expands into fundamental plus third-harmonic term | PDF identity | high |
| Applications §12 | cos θ · cos φ expands into sum and difference angle terms | PDF identity | high |