# Summation of Series (Trigonometric Series)

This unit presents systematic methods for finding the sums of finite and infinite series whose general terms involve trigonometric (and, by extension, hyperbolic) functions. The two principal techniques are the companion-series method that forms C + iS and the method of differences that telescopes terms by means of trigonometric identities. Both approaches convert an ostensibly trigonometric problem into an algebraic or complex-exponential one that can be summed by standard geometric, binomial, exponential, logarithmic or Gregory expansions.

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

The techniques developed here allow a student to evaluate sums that appear repeatedly in Fourier analysis, complex analysis and classical mechanics without resorting to ad-hoc trigonometric manipulations for every new series.

- They convert a pair of real trigonometric series into a single complex geometric or binomial series that is already known.
- They supply closed-form expressions for both finite and infinite cases under transparent convergence conditions.
- The difference method yields exact telescoping identities that are independent of complex numbers and are therefore useful when only real arithmetic is desired.
- The same formal patterns extend immediately to hyperbolic functions by the substitution of real exponentials for complex ones.

### Mathematical Foundation

The central device is the companion-series construction. Given

> C = a₀ cos α + a₁ cos(α + β) + a₂ cos(α + 2β) + ⋯  
> S = a₀ sin α + a₁ sin(α + β) + a₂ sin(α + 2β) + ⋯

one forms the complex sum

> C + iS = Σ aₖ e^{i(α + kβ)}.

The right-hand side is then recognised as a geometric progression, a binomial expansion, an exponential series, a logarithmic series or Gregory’s series according to the coefficients aₖ. Equating real and imaginary parts recovers C and S.

Useful elementary identities for the difference method include

> cosec θ = cot(θ/2) – cot θ,  
> tan θ = cot θ – 2 cot 2θ,  
> sec θ sec(θ + β) = cosec β [tan(θ + β) – tan θ],  
> cosec θ cosec(θ + β) = cosec β [cot θ – cot(θ + β)],  
> sin³ α = (1/4)[3 sin α – sin 3α],  
> tan⁻¹((x – y)/(1 + xy)) = tan⁻¹ x – tan⁻¹ y.

### Derivation of the General Method

#### Geometric-progression case

Write

> C + iS = e^{iα} (1 – (c e^{iβ})ⁿ) / (1 – c e^{iβ}).

Multiply numerator and denominator by the conjugate 1 – c e^{-iβ} and separate real and imaginary parts. The resulting formulae for the finite sums are

> S = [sin α – c sin(α – β) – cⁿ sin(α + nβ) + cⁿ⁺¹ sin(α + (n – 1)β)] / (1 – 2c cos β + c²),  
> C = [cos α – c cos(α – β) – cⁿ cos(α + nβ) + cⁿ⁺¹ cos(α + (n – 1)β)] / (1 – 2c cos β + c²).

When |c| < 1 the infinite-sum versions follow at once by letting n → ∞.

#### Binomial case

The coefficients of the binomial expansions

> (1 + x)^{1/2}, (1 – x)^{-1/2}, (1 + x)^{-1/2}, \ldots

are inserted into C + iS. After the substitution x = e^{iφ} the left-hand side becomes a known algebraic function of e^{iφ}; the real part yields the required cosine sum.

#### Exponential case

The series

> 1 + c cos α + (c²/2!) cos 2α + (c³/3!) cos 3α + ⋯  
> c sin α + (c²/2!) sin 2α + (c³/3!) sin 3α + ⋯

combine into

> C + iS = exp(c e^{iα}) = e^{c cos α} [cos(c sin α) + i sin(c sin α)].

#### Logarithmic and Gregory cases

The ordinary Taylor series for log(1 + z) and tan⁻¹ z with z = c e^{iα} produce, after separation of real and imaginary parts, the classical closed forms involving logarithms of moduli and inverse tangents of arguments.

#### Method of differences

Each term of the given series is rewritten, by means of one of the identities listed above, as a pure difference. On summation all intermediate terms cancel, leaving only the first and last contributions.

### Key Observations

| Series type          | Typical coefficients aₖ          | Closed form obtained from          | Convergence condition      |
|----------------------|----------------------------------|------------------------------------|----------------------------|
| Geometric            | cᵏ                               | finite or infinite GP formula      | |c| < 1 for infinite sum   |
| Binomial             | binomial coefficients            | (1 ± e^{iφ})^{±1/2}, etc.          | |e^{iφ}| = 1, branch cuts  |
| Exponential          | cᵏ / k!                          | exp(c e^{iα})                      | entire function            |
| Logarithmic          | (–1)^{k+1} cᵏ / k                | log(1 + c e^{iα})                  | |c| < 1                    |
| Gregory              | (–1)^k c^{2k+1} / (2k+1)         | tan⁻¹(c e^{iα})                    | |c| ≤ 1                    |
| Difference (real)    | product of cosec or sec          | telescoping cot or tan differences | none (finite sum)          |

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

James Gregory (1638–1675), Vera Circuli et Hyperbolae Quadratura (1668) — first published the power series for tan⁻¹ x that is used for the odd-powered trigonometric series.  
Leonhard Euler (1707–1783), Introductio in analysin infinitorum (1748) — systematically employed the complex exponential e^{iθ} = cos θ + i sin θ to convert trigonometric sums into geometric series.  
Abraham de Moivre (1667–1754), Miscellanea Analytica (1730) — established the multinomial theorem that underlies the extraction of real and imaginary parts of (cos θ + i sin θ)ⁿ.  
Brook Taylor (1685–1731), Methodus Incrementorum Directa et Inversa (1715) — supplied the general Taylor expansion that legitimises the exponential, logarithmic and binomial series used throughout the unit.

## Real-World Applications

1. Signal processing  
   - Decomposition of periodic waveforms into harmonic components.  
   - Closed-form evaluation of discrete Fourier sums that arise in filter design.  
   - Analytic continuation of transfer functions containing trigonometric polynomials.  
   **Example:** A clipped sinusoid modelled by a finite Fourier sine series is summed by the geometric C + iS formula to obtain the exact amplitude spectrum.

2. Electrical engineering  
   - Steady-state analysis of AC circuits driven by multi-harmonic sources.  
   - Calculation of average power when voltage and current contain phase-shifted cosines.  
   - Impedance of ladder networks whose successive sections produce geometric phase shifts.  
   **Example:** The input impedance of a transmission line with periodic loading reduces to a geometric series of the form treated in Type I.

3. Acoustics  
   - Synthesis of musical tones from pure partials whose amplitudes follow binomial or exponential decay.  
   - Prediction of beats and combination tones by summing phase-shifted sinusoids.  
   - Room-mode calculations that involve infinite geometric series of reflected waves.  
   **Example:** The pressure field of a uniformly spaced line array of loudspeakers is exactly the geometric sum derived in Example 8.1.

4. Mechanical engineering  
   - Vibration of multi-degree-of-freedom systems whose coupling matrices yield trigonometric characteristic equations.  
   - Balancing of rotating machinery by cancellation of successive harmonic force components.  
   - Fourier analysis of cam profiles expressed as finite trigonometric polynomials.  
   **Example:** The residual force after balancing the first n harmonics is obtained by the finite geometric formula of Type I.

5. Computer graphics  
   - Efficient evaluation of circular arcs and spiral interpolants via complex exponentials.  
   - Anti-aliasing filters whose frequency responses are infinite geometric series of cosines.  
   - Procedural generation of periodic textures by summing phase-shifted sinusoids.  
   **Example:** A soft-edged disk rendered by a radial cosine series is summed in closed form by the binomial expansion of Type II.

6. Numerical analysis  
   - Acceleration of slowly convergent trigonometric series by conversion to exponential form.  
   - Exact summation of the Dirichlet kernel that appears in Fourier projection operators.  
   - Error estimates for truncated Taylor series of analytic functions on the unit circle.  
   **Example:** The partial sum of the Fourier series of a saw-tooth wave is the closed geometric expression given after Example 8.2.

7. Astronomy  
   - Ephemeris calculations that expand planetary perturbations in multiple-angle series.  
   - Fourier analysis of light curves of variable stars.  
   - Summation of the gravitational potential of a ring of equal masses.  
   **Example:** The longitudinal perturbation of a satellite is expressed as an infinite series of the form treated by the logarithmic method (Type IV).

8. Chemistry  
   - Molecular orbital theory for cyclic conjugated systems (Hückel theory) produces geometric sums over e^{2πik/n}.  
   - Vibrational spectroscopy of linear chains whose normal modes are standing waves.  
   - Diffraction intensities from one-dimensional lattices.  
   **Example:** The energy levels of a cyclic polyene are obtained by summing the geometric series that appears in the secular determinant.

9. Geophysics  
   - Modelling of seismic wave trains reflected from parallel interfaces.  
   - Fourier synthesis of Earth-tide potentials.  
   - Gravity anomalies produced by periodic subsurface density variations.  
   **Example:** The reflected pulse train from a stratified medium is an infinite geometric series of the form summed in Example 8.3.

10. Music theory  
    - Construction of just-intonation intervals from infinite products that become logarithmic series.  
    - Spectral analysis of sustained tones whose partial amplitudes follow binomial decay.  
    - Algorithmic composition that superposes phase-shifted sinusoids.  
    **Example:** The amplitude envelope of a plucked string approximated by a binomial series is evaluated by the closed form of Type II.

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
|---------|-------|------------------------------------------------------|------------|
| Historical | James Gregory, Vera Circuli\ldots (1668) — tan⁻¹ series | textbook-standard | high |
| Historical | Leonhard Euler, Introductio\ldots (1748) — complex exponential | textbook-standard | high |
| Historical | Abraham de Moivre, Miscellanea Analytica (1730) — multinomial theorem | textbook-standard | high |
| Historical | Brook Taylor, Methodus Incrementorum (1715) — Taylor series | textbook-standard | high |
| Applications | Geometric sum for line-array pressure field | PDF Example 8.1 identity | high |
| Applications | Transmission-line geometric impedance | PDF Type I formula | high |
| Applications | Binomial expansion for soft-edged disk | PDF Type II binomial | high |
| Applications | Logarithmic series for satellite perturbation | PDF Type IV log formula | high |
| Applications | Cyclic-polyene geometric secular sum | PDF geometric GP formula | high |