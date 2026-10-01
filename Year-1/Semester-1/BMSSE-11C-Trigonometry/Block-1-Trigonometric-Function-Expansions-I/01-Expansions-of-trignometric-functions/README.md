# Expansions of cosⁿθ and sinⁿθ

A complete study guide covering the theory, derivation, key observations, historical context, and real-world applications of expanding powers of trigonometric functions into sums of sines and cosines of multiples of the angle.

---

## Table of Contents

1. [Notes](#notes)
2. [Historical Background](#historical-background)
3. [Real-World Applications](#real-world-applications)

---

## Notes

### Overview

The expansion of powers of trigonometric functions into sums of sines and cosines of multiples of the angle is a fundamental technique in trigonometry and mathematical analysis. This method allows us to express cosⁿθ and sinⁿθ (where n is a positive integer) as a linear combination of cos(kθ) and sin(kθ) terms.

This transformation is essential because:

- It linearizes powers, making integration and differentiation simpler.
- It reveals harmonic structure in periodic phenomena.
- It connects algebraic operations on complex numbers to trigonometric identities.

The technique also extends to products of the form cosⁿθ · sinⁿθ, which can be expanded by combining the two standard substitutions.

### Mathematical Foundation

The method rests on **De Moivre's Theorem** and the **Binomial Theorem**.

Let

> x = cos θ + i sin θ

Then by De Moivre's theorem,

> xⁿ = cos nθ + i sin nθ

and since x⁻¹ = cos θ − i sin θ,

> x⁻ⁿ = cos nθ − i sin nθ

Adding and subtracting these gives the two fundamental identities:

> **x + 1/x = 2 cos θ**

> **x − 1/x = 2i sin θ**

More generally, for any positive integer n:

> **xⁿ + 1/xⁿ = 2 cos nθ**

> **xⁿ − 1/xⁿ = 2i sin nθ**

These identities are the bridge between powers of trigonometric functions and multiples of angles.

### Derivation of the General Method

The PDF lists three substitutions:

1. For cosⁿθ: consider (2 cos θ)ⁿ = (x + 1/x)ⁿ
2. For sinⁿθ: consider (2i sin θ)ⁿ = (x − 1/x)ⁿ
3. For cosⁿθ · sinⁿθ: consider the product (x + 1/x)ⁿ (x − 1/x)ⁿ

We use the binomial theorem to expand each right-hand side.

#### For cosⁿθ

We start with

> (2 cos θ)ⁿ = (x + 1/x)ⁿ

Expanding the right-hand side using the binomial theorem:

> (x + 1/x)ⁿ = xⁿ + C(n,1)·xⁿ⁻¹·(1/x) + C(n,2)·xⁿ⁻²·(1/x²) + ... + 1/xⁿ

After simplifying each term, we collect like powers of x. Terms of the form xᵏ + 1/xᵏ are then replaced using

> xᵏ + 1/xᵏ = 2 cos kθ

The constant term (when n is even) appears as C(n, n/2) and is left as is.

#### For sinⁿθ

We start with

> (2i sin θ)ⁿ = (x − 1/x)ⁿ

Expanding using the binomial theorem with alternating signs:

> (x − 1/x)ⁿ = xⁿ − C(n,1)·xⁿ⁻¹·(1/x) + C(n,2)·xⁿ⁻²·(1/x²) − ... + (−1)ⁿ·(1/xⁿ)

Collecting terms of the form xᵏ − 1/xᵏ (for odd n) or xᵏ + 1/xᵏ (for even n) and substituting:

- For odd n: xᵏ − 1/xᵏ = 2i sin kθ
- For even n: xᵏ + 1/xᵏ = 2 cos kθ

The powers of i simplify using i² = −1, i⁴ = 1, etc.

#### For cosⁿθ · sinⁿθ

We consider the product

> (2 cos θ)ⁿ · (2i sin θ)ⁿ = (x + 1/x)ⁿ · (x − 1/x)ⁿ

Simplifying the left side and expanding the right side via the binomial theorem allows us to convert products of powers into sums of sines and cosines of multiples of θ.

### Key Observations

| Expression | Expansion Type | Condition |
|---|---|---|
| cosⁿθ | Cosines of multiples of θ | Always |
| sinⁿθ | Sines of multiples of θ | n odd |
| sinⁿθ | Cosines of multiples of θ | n even |
| cosⁿθ · sinⁿθ | Sines or cosines of multiples | Depends on parity |

---

## Historical Background

The expansion of powers of trigonometric functions has roots in the work of **Abraham de Moivre** (1667–1754), a French mathematician who spent much of his career in England. De Moivre discovered the formula that now bears his name:

> (cos θ + i sin θ)ⁿ = cos nθ + i sin nθ

This result, published in his 1730 work *Miscellanea Analytica*, provided the essential link between complex numbers and trigonometry. While the formula itself was known in various forms before him, De Moivre was the first to state it generally and apply it systematically.

The **binomial theorem**, used alongside De Moivre's theorem in these expansions, has even older roots. It was known to Chinese mathematicians by the 11th century (Jia Xian's triangle) and Persian mathematicians like Omar Khayyam (1048–1131). In Europe, **Blaise Pascal** (1623–1662) formalized the triangular array of binomial coefficients in his *Traité du triangle arithmétique* (1654). **Isaac Newton** (1643–1727) generalized the theorem to non-integer exponents in 1665.

The technique of expanding cosⁿθ and sinⁿθ using complex numbers became a standard tool in the 18th and 19th centuries, particularly in the work of **Leonhard Euler** (1707–1783), who made extensive use of complex exponentials in analysis. Euler's formula e^(iθ) = cos θ + i sin θ, published in 1748, is essentially equivalent to De Moivre's theorem and provided an even more elegant framework for these expansions.

In the 19th century, these expansions became essential tools in **Fourier analysis**, developed by **Joseph Fourier** (1768–1830) for solving the heat equation. Fourier's insight that any periodic function could be expressed as a sum of sines and cosines of multiples of the fundamental frequency relied heavily on the type of trigonometric identities derived in this unit.

---

## Real-World Applications

### 1. Signal Processing

In signal processing, any periodic signal can be decomposed into its harmonic components using Fourier series. The expansions of cosⁿθ and sinⁿθ are used to:

- **Linearize power amplifiers:** When a sinusoidal signal passes through a nonlinear device (e.g., a diode or transistor), the output contains harmonics. Expanding cosⁿθ helps predict the harmonic content.
- **Analyze modulation schemes:** In amplitude modulation (AM), the modulated signal involves products of cosines, which are simplified using these expansions.
- **Filter design:** Understanding how powers of sinusoids expand into harmonics helps in designing filters to remove unwanted frequency components.

**Example:** If a signal x(t) = cos³(2π f₀ t) passes through a system, its expansion (1/4)[cos(6π f₀ t) + 3 cos(2π f₀ t)] reveals the fundamental and third harmonic components.

### 2. Physics — Wave Mechanics and Optics

- **Interference patterns:** In optics, the intensity of light from multiple slits involves powers of cosine terms. Expanding these helps predict fringe patterns.
- **Quantum mechanics:** The probability densities of quantum states often involve sinⁿ or cosⁿ terms. These expansions simplify expectation value calculations.
- **Nonlinear optics:** When intense laser light interacts with matter, the nonlinear response involves powers of the electric field (which is sinusoidal). The expansion reveals harmonic generation (e.g., second-harmonic generation in frequency-doubling crystals).

**Example:** In a Fabry–Perot interferometer, the transmitted intensity involves cos²(δ/2), which expands to (1/2)[1 + cos δ], revealing the Airy function structure.

### 3. Electrical Engineering — Power Systems

- **Harmonic analysis:** Nonlinear loads (e.g., rectifiers, arc furnaces) inject harmonics into power systems. Expanding cosⁿ(ωt) helps quantify total harmonic distortion (THD).
- **Power factor correction:** Understanding harmonic content is essential for designing passive and active filters.
- **Three-phase systems:** Balanced three-phase voltages involve cos(ωt), cos(ωt − 120°), and cos(ωt + 120°). Powers of these appear in power calculations.

**Example:** A nonlinear load drawing current i(t) = I₀ cos³(ωt) has a fundamental component and a third harmonic, which can cause overheating in neutral conductors.

### 4. Computer Graphics and Animation

- **Procedural texture generation:** Powers of sine and cosine are used to create periodic patterns (e.g., wood grain, marble). Expanding these helps optimize rendering.
- **Skeletal animation:** Joint rotations are often represented using sinusoidal functions. Powers of these appear in interpolation formulas.
- **Lighting models:** Lambertian reflectance involves cos θ, and specular highlights involve cosⁿθ. Expanding these allows efficient computation of shading.

**Example:** The Phong specular model uses cosⁿθ for the specular highlight. Expanding it into cosines of multiples of θ allows precomputation of lighting coefficients.

### 5. Mechanical Engineering — Vibrations

- **Nonlinear vibrations:** In systems with nonlinear restoring forces (e.g., a pendulum with large amplitude), the equation of motion involves powers of sin θ. Expanding these leads to the Duffing equation and harmonic balance methods.
- **Rotordynamics:** Unbalance and misalignment produce harmonic forces. Expanding cosⁿ(ωt) helps predict vibration frequencies.
- **Fatigue analysis:** Understanding harmonic content helps predict fatigue life under cyclic loading.

**Example:** A pendulum's restoring torque is proportional to sin θ. For large oscillations, sin θ ≈ θ − θ³/6, and expanding sin³θ reveals the third harmonic in the motion.

### 6. Economics and Finance — Seasonal Cycles

- **Seasonal decomposition:** Economic time series often exhibit seasonal patterns modeled as sums of sines and cosines. Powers of these appear in nonlinear models.
- **Volatility modeling:** Financial volatility has periodic components. Expanding powers of sinusoids helps in GARCH-type models.
- **Business cycle analysis:** Harmonic analysis of macroeconomic data uses these expansions to identify cycle frequencies.

**Example:** Retail sales often follow a pattern like S(t) = A cos(ωt) + B cos²(ωt), where the cos² term expands to introduce a constant and a second harmonic, capturing both level shifts and double-frequency seasonality.

### 7. Acoustics and Music Theory

- **Timbre analysis:** Musical instrument tones are periodic but not purely sinusoidal. The harmonic content is analyzed using Fourier series, where powers of sinusoids appear in nonlinear instrument models.
- **Room acoustics:** Sound reflections involve powers of cosine in directivity patterns.
- **Synthesis:** FM synthesis uses cos(ω_c t + I cos(ω_m t)), which expands via Bessel functions but reduces to powers of cosines in simpler cases.

**Example:** A clipped guitar signal approximates a square wave. Expanding cosⁿ(ωt) for large n shows the odd harmonics that give the distorted tone its character.

### 8. Numerical Analysis and Approximation Theory

- **Chebyshev polynomials:** The expansion cos(nθ) = Tₙ(cos θ) connects trigonometric expansions to polynomial approximation. Powers of cos θ are expressed in terms of Chebyshev polynomials.
- **Galerkin methods:** In spectral methods for PDEs, trigonometric basis functions are used. Powers of these functions appear in nonlinear terms.
- **Quadrature rules:** Gaussian quadrature on trigonometric functions uses these expansions for error analysis.

**Example:** In solving the heat equation with a nonlinear source term u³, expanding u = Σ aₖ cos(kx) leads to products of cosines that are simplified using these identities.

### 9. Astronomy and Celestial Mechanics

- **Perturbation theory:** Planetary orbits are perturbed by gravitational interactions. The perturbing forces involve powers of cos θ, where θ is the angular position.
- **Tidal analysis:** Tidal forces involve cos²θ and higher powers, expanded to predict tidal harmonics.
- **Light curves:** Variable stars and eclipsing binaries have light curves that are periodic. Expanding powers of sinusoids helps model these curves.

**Example:** The tidal potential involves (3 cos²θ − 1), which expands to (3/2) cos 2θ + 1/2, revealing the semi-diurnal tide.

### 10. Chemistry and Spectroscopy

- **Molecular vibrations:** Infrared and Raman spectra involve transitions between vibrational states. The transition dipole moment involves powers of cos θ, where θ is the displacement coordinate.
- **Rotational spectra:** The energy levels of a rigid rotor involve cos²θ terms, expanded to predict line intensities.
- **NMR spectroscopy:** Radiofrequency pulses involve cos(ωt) and its powers in spin dynamics.

**Example:** In Raman spectroscopy, the polarizability tensor involves cos²θ, which expands to give the Stokes and anti-Stokes lines.