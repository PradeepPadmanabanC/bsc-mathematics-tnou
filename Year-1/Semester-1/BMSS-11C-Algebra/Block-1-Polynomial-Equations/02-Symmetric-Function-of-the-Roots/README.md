# Symmetric Function of the Roots

**Block:** 1 — Polynomial Equations  
**Course:** BMSS-11C — Algebra

## Notes

### 2.1 Symmetric Function of the Roots

If a function involving all the roots of an equation and is unaltered in value if any two of the roots are interchanged, is called a *symmetric function of the roots*.

If α, β, γ are the roots of the third degree equation, then the symmetric functions are:

- ∑α = α + β + γ
- ∑αβ = αβ + βγ + γα
- ∑α²β² = α²β² + β²γ² + γ²α²
- ∑α²β = α²β + α²γ + β²α + β²γ + γ²α + γ²β

---

**Note 2.1.** We can use the following identities for solving the problems which involve three roots:

1. ∑α² = α² + β² + γ² = (α + β + γ)² − 2(αβ + βγ + γα)

2. ∑α²β = (α + β + γ)(αβ + βγ + γα) − 3αβγ

3. ∑α³ = α³ + β³ + γ³ = (α + β + γ)[(α + β + γ)² − 3(αβ + βγ + γα)] + 3αβγ

## Newton's Identities (Newton-Girard Formulas) — Generalization to Any Degree

### The General Setup

For a polynomial of degree **n** with roots α₁, α₂, ..., αₙ:

**Elementary symmetric polynomials** (from Vieta's formulas):
- e₁ = ∑αᵢ
- e₂ = ∑αᵢαⱼ (i < j)
- e₃ = ∑αᵢαⱼαₖ (i < j < k)
- ...
- eₙ = α₁α₂...αₙ

**Power sums** (what we often need to compute):
- p₁ = ∑αᵢ = α₁ + α₂ + ... + αₙ
- p₂ = ∑αᵢ² = α₁² + α₂² + ... + αₙ²
- p₃ = ∑αᵢ³
- pₖ = ∑αᵢᵏ

---

### Newton's Identities (General Recursive Formula)

For **any degree n**, the power sums relate to elementary symmetric polynomials by:

| k | Identity |
|---|----------|
| 1 | p₁ = e₁ |
| 2 | p₂ = e₁p₁ − 2e₂ |
| 3 | p₃ = e₁p₂ − e₂p₁ + 3e₃ |
| 4 | p₄ = e₁p₃ − e₂p₂ + e₃p₁ − 4e₄ |
| k ≤ n | pₖ = e₁pₖ₋₁ − e₂pₖ₋₂ + e₃pₖ₋₃ − ... + (−1)ᵏ⁻¹keₖ |
| k > n | pₖ = e₁pₖ₋₁ − e₂pₖ₋₂ + ... + (−1)ⁿ⁻¹eₙpₖ₋ₙ |

The general recursive formula:

> **pₖ = ∑ᵢ₌₁ᵏ (−1)ⁱ⁻¹ eᵢ pₖ₋ᵢ**  (for k ≤ n, with p₀ = n)

---

### Example: Degree 4 (Quartic)

For roots α, β, γ, δ of a quartic equation:

- p₁ = e₁
- p₂ = e₁² − 2e₂
- p₃ = e₁³ − 3e₁e₂ + 3e₃
- p₄ = e₁⁴ − 4e₁²e₂ + 2e₂² + 4e₁e₃ − 4e₄

These are exactly analogous to the degree-3 identities in Note 2.1, just with the extra e₄ term.

---

### How the Degree-3 Identities (Note 2.1) Fit In

| Identity from Note 2.1 | Newton's form |
|-------------------------|---------------|
| ∑α² = (∑α)² − 2∑αβ | p₂ = e₁² − 2e₂ |
| ∑α²β = e₁e₂ − 3e₃ | (mixed symmetric, not a pure power sum) |
| ∑α³ = e₁(e₁² − 3e₂) + 3e₃ | p₃ = e₁p₂ − e₂p₁ + 3e₃ |

These are Newton's identities specialized to n = 3. The same pattern extends to degree 4, 5, 100, or any n.

---

### Why This Matters

- For degree 3, you can memorize a few identities
- For degree 4+, Newton's recursive formula lets you compute **any** power sum pₖ step by step without memorizing individual formulas
- The recursion works the same way regardless of degree — you just have more eᵢ terms to include
- The course focuses on degree 3 because computations are manageable by hand, but the theory is completely general

---

## Real-World Applications

### Statistics & Data Science

**Moments of a distribution**
- The mean, variance, skewness, and kurtosis of a dataset are symmetric functions of the data points. When data points are modeled as roots of a polynomial, power sums (∑αᵏ) directly correspond to the kth moment. This is the mathematical backbone of descriptive statistics.

**Principal Component Analysis (PCA)**
- Eigenvalues of a covariance matrix are roots of the characteristic polynomial. The trace (∑λᵢ = sum of eigenvalues) and determinant (∏λᵢ = product of eigenvalues) are elementary symmetric functions. Higher power sums like ∑λᵢ² measure how "spread out" the variance is across components.

---

### Physics

**Quantum Mechanics — Partition Functions**
- In statistical mechanics, the partition function Z = ∑e^(−βEᵢ) is a symmetric function of energy eigenvalues. Thermodynamic quantities (internal energy, entropy, specific heat) are derived from power sums of these eigenvalues.

**Vibration Analysis**
- A mechanical system with n degrees of freedom has n natural frequencies (roots of the characteristic equation). The total kinetic energy and potential energy can be expressed as symmetric functions of these frequencies — you don't need to know individual frequencies to compute system-level properties.

**Particle Physics**
- Scattering amplitudes in quantum field theory are symmetric functions of particle momenta. Mandelstam variables (s, t, u) are elementary symmetric combinations that simplify calculations enormously.

---

### Engineering

**Control Theory — System Characterization**
- For a system with transfer function poles p₁, p₂, ..., pₙ:
  - ∑pᵢ tells you the overall decay rate
  - ∑pᵢ² relates to the system's energy dissipation
  - ∏pᵢ determines steady-state gain
- Engineers routinely compute these without finding individual poles.

**Signal Processing — Spectral Analysis**
- Power spectral density moments (∑fᵢᵏ weighted by amplitude) are symmetric functions of frequency components. They characterize signal bandwidth, center frequency, and spectral spread.

**Circuit Design**
- When designing filters with multiple poles, symmetric functions determine the overall frequency response shape. Butterworth and Chebyshev filter designs exploit symmetric arrangements of poles.

---

### Computer Science

**Algorithm Design — Elementary Symmetric Polynomials**
- Efficient computation of symmetric functions is key to:
  - Polynomial interpolation (Lagrange, Newton methods)
  - Error-correcting codes (Reed-Solomon codes use symmetric functions to locate errors)
  - Hashing algorithms that need order-independent combinations

**Cryptography**
- Secret sharing schemes (like Shamir's Secret Sharing) use polynomial evaluation. Symmetric functions of the shares allow threshold reconstruction without revealing individual shares.

**Database Systems**
- Aggregate functions (SUM, AVG, PRODUCT) over query results are symmetric functions. Query optimizers exploit this symmetry to reorder computations for efficiency.

---

### Economics & Finance

**Portfolio Theory**
- For a portfolio with n asset returns r₁, r₂, ..., rₙ:
  - ∑rᵢ = total portfolio return
  - ∑rᵢ² relates to portfolio volatility
  - Higher symmetric functions capture tail risk and correlation effects
- Diversification is essentially exploiting the relationship between elementary symmetric functions and power sums.

**Option Pricing**
- Multi-asset options (basket options) have payoffs that are symmetric functions of underlying asset prices. Pricing these requires evaluating symmetric polynomials efficiently.

---

### Chemistry

**Molecular Orbital Theory**
- Energy levels of molecular orbitals are eigenvalues of the Hückel matrix. Symmetric functions of these energies give:
  - Total π-electron energy (∑Eᵢ)
  - Stability measures (∑Eᵢ²)
  - Reactivity indices

**Spectroscopy**
- Spectral line positions in atomic/molecular spectra are roots of characteristic equations. Symmetric combinations reveal selection rules and conservation laws without solving for individual energy levels.

---

> **Key Insight:** The power of symmetric functions is that they let you compute **global properties of a system** (total energy, overall stability, aggregate behavior) **without solving for individual components** (specific roots, individual eigenvalues, particular frequencies). This is why Newton's identities — which convert between power sums and elementary symmetric polynomials — are so practically important: they bridge what you can measure (aggregate quantities) with what the polynomial encodes (coefficients).

---

## Examples

<!-- Add worked examples here -->

## Practice Problems

<!-- Add practice problems here -->
