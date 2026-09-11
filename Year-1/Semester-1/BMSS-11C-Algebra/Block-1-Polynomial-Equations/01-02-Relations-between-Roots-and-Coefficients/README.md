# Relations between the Roots and Coefficients of Equations

**Block:** 1 — Polynomial Equations  
**Course:** BMSS-11C — Algebra

## Table of Contents

- [Notes](#notes)
  - [Relations between the Roots and Coefficients of Equations](#relations-between-the-roots-and-coefficients-of-equations)
    - [Summary of Relations](#summary-of-relations)
    - [Remark 1.1: Choosing Roots for Special Progressions](#remark-11-choosing-roots-for-special-progressions)
    - [Proof: Roots in H.P. ⟹ Roots of f(1/x) are in A.P.](#proof-roots-in-hp--roots-of-f1x--0-are-in-ap)
- [Real-World Applications](#real-world-applications)
  - [Relations between Roots and Coefficients (Vieta's Formulas)](#relations-between-roots-and-coefficients-vietas-formulas)
  - [Roots in Progressions (A.P., G.P., H.P.)](#roots-in-progressions-ap-gp-hp)
- [Practice Problems](#practice-problems)

---

## Notes

### Relations between the Roots and Coefficients of Equations

Let f(x) = a₀xⁿ + a₁xⁿ⁻¹ + a₂xⁿ⁻² + ... + aₙ₋₁x + aₙ = 0 be an equation of degree n.

If this equation has the roots α₁, α₂, α₃, ..., αₙ and in these roots, some of them may be repeated.

∴ a₀xⁿ + a₁xⁿ⁻¹ + a₂xⁿ⁻² + ... + aₙ₋₁x + aₙ = a₀(x − α₁)(x − α₂)(x − α₃)...(x − αₙ)

Expanding the right side:

> = a₀[xⁿ − (α₁ + α₂ + ... + αₙ)xⁿ⁻¹ + (α₁α₂ + α₂α₃ + ... + αₙα₁)xⁿ⁻² + ... + (−1)ⁿ(α₁ · α₂ · α₃ ... αₙ)]

**By equating the like powers of x, we get:**

> a₁ = −a₀(α₁ + α₂ + ... + αₙ) ⟹ Σαᵢ = −a₁/a₀

> a₂ = a₀(α₁α₂ + ... + αₙα₁) ⟹ Σαᵢαⱼ = a₂/a₀

> a₃ = −a₀(α₁α₂α₃ + α₁α₃α₄ + ...) ⟹ Σαᵢαⱼαₖ = −a₃/a₀

> ⋮

> aₙ = (−1)ⁿ a₀(α₁α₂...αₙ) ⟹ α₁α₂...αₙ = (−1)ⁿ aₙ/a₀

---

#### Summary of Relations

Hence we have:

| Symbol | Meaning | Formula |
|--------|---------|---------|
| S₁ | Sum of the roots | Σαᵢ = −a₁/a₀ |
| S₂ | Sum of the product of roots taken two at a time | Σαᵢαⱼ = a₂/a₀ |
| S₃ | Sum of the product of roots taken three at a time | Σαᵢαⱼαₖ = −a₃/a₀ |
| ⋮ | ⋮ | ⋮ |
| Sₙ | Product of all the roots | α₁α₂α₃...αₙ = (−1)ⁿ aₙ/a₀ |

**General pattern:** Sₖ = (−1)ᵏ aₖ/a₀

---

#### Remark 1.1: Choosing Roots for Special Progressions

**(A) For the third degree equation:** ax³ + bx² + cx + d = 0

| Progression | Roots to assume |
|-------------|-----------------|
| Arithmetic Progression (A.P.) | a − d, a, a + d |
| Geometric Progression (G.P.) | a/r, a, ar |
| Harmonic Progression (H.P.) | If f(x) = 0 has roots in H.P., then f(1/x) = 0 has roots in A.P. |

---

#### Proof: Roots in H.P. ⟹ Roots of f(1/x) = 0 are in A.P.

**Statement:**
If the roots of f(x) = 0 are in Harmonic Progression (H.P.), then the roots of f(1/x) = 0 are in Arithmetic Progression (A.P.).

---

**Preliminary: Definition of Harmonic Progression**

A sequence of numbers h₁, h₂, h₃, ... is said to be in **Harmonic Progression** if and only if their reciprocals 1/h₁, 1/h₂, 1/h₃, ... are in **Arithmetic Progression**.

---

**Proof:**

**Step 1: Let the roots of f(x) = 0 be in H.P.**

Suppose f(x) = 0 has roots α₁, α₂, α₃ which are in Harmonic Progression (taking the cubic case for concreteness).

By the definition of H.P., this means:

> 1/α₁, 1/α₂, 1/α₃ are in Arithmetic Progression.

**Step 2: Find the roots of f(1/x) = 0**

Consider the substitution x → 1/x. If α is a root of f(x) = 0, i.e., f(α) = 0, then for the equation f(1/x) = 0, we need:

> f(1/x) = 0 ⟹ 1/x must be a root of f(t) = 0 ⟹ 1/x = α ⟹ x = 1/α

Therefore, if α₁, α₂, α₃ are roots of f(x) = 0, then **1/α₁, 1/α₂, 1/α₃ are roots of f(1/x) = 0**.

**Step 3: Conclude**

From Step 1, we know 1/α₁, 1/α₂, 1/α₃ are in A.P.

From Step 2, we know 1/α₁, 1/α₂, 1/α₃ are the roots of f(1/x) = 0.

Therefore, the roots of f(1/x) = 0 are in **Arithmetic Progression**. ∎

---

**Practical Application:**

To solve a cubic equation whose roots are in H.P.:

1. Replace x by 1/x in the given equation f(x) = 0 to get a new equation g(x) = f(1/x) = 0.
2. The roots of g(x) = 0 are now in A.P.
3. Assume the roots of g(x) = 0 as a − d, a, a + d.
4. Use the relations between roots and coefficients to find a and d.
5. The roots of the original equation are the reciprocals: 1/(a − d), 1/a, 1/(a + d).

---

**Worked Example:**

Solve 6x³ − 11x² + 6x − 1 = 0, given that the roots are in H.P.

**Step 1:** Replace x by 1/x:

> 6(1/x)³ − 11(1/x)² + 6(1/x) − 1 = 0

> 6/x³ − 11/x² + 6/x − 1 = 0

Multiply through by x³:

> 6 − 11x + 6x² − x³ = 0

> x³ − 6x² + 11x − 6 = 0

**Step 2:** The roots of x³ − 6x² + 11x − 6 = 0 are in A.P. Assume them as a − d, a, a + d.

**Step 3:** Sum of roots = (a − d) + a + (a + d) = 3a = −(−6)/1 = 6

> ∴ a = 2

**Step 4:** Product of roots = (a − d)(a)(a + d) = a(a² − d²) = 6/1 = 6

> 2(4 − d²) = 6 ⟹ 4 − d² = 3 ⟹ d² = 1 ⟹ d = ±1

**Step 5:** Roots of x³ − 6x² + 11x − 6 = 0 are: 1, 2, 3

**Step 6:** Roots of the original equation are the reciprocals: **1, 1/2, 1/3** ✓

(Verify: 1, 1/2, 1/3 — their reciprocals are 1, 2, 3 which are in A.P., so 1, 1/2, 1/3 are in H.P. ✓)

---

**(B) For the biquadratic equation:** ax⁴ + bx³ + cx² + dx + e = 0

| Progression | Roots to assume |
|-------------|-----------------|
| Arithmetic Progression (A.P.) | a − 3d, a − d, a + d, a + 3d |
| Geometric Progression (G.P.) | a/r³, a/r, ar, ar³ |

---

## Real-World Applications

### Relations between Roots and Coefficients (Vieta's Formulas)

**Machine Learning & Statistics**
- Principal Component Analysis (PCA) requires finding eigenvalues of a covariance matrix — which means solving the characteristic polynomial. Vieta's formulas give quick relationships: the sum of eigenvalues equals the trace, the product equals the determinant.

**Economics & Game Theory**
- Equilibrium analysis in multi-agent systems often reduces to solving polynomial systems. Vieta's relations let economists reason about aggregate behavior (sum/product of equilibria) without solving for each equilibrium individually.

**Chemistry**
- pH calculations, chemical equilibrium equations, and reaction kinetics often yield cubic or quartic polynomials. Vieta's formulas help verify solutions and understand how concentrations relate.

**Orbital Mechanics**
- Kepler's equation and trajectory calculations involve polynomial equations whose root relationships directly correspond to orbital parameters (period, eccentricity).

---

### Roots in Progressions (A.P., G.P., H.P.)

**Digital Signal Processing**
- Filter design with equally spaced poles (A.P. of roots) creates linear-phase filters used in audio processing and telecommunications.

**Finance**
- Annuity and amortization calculations involve geometric progressions. When cash flows follow a G.P., the present value equation is a polynomial whose roots in G.P. simplify valuation.

**Acoustics & Music**
- Harmonic series (H.P.) directly relates to overtone frequencies in musical instruments. The mathematical structure of roots in H.P. mirrors how physical resonances are distributed.

---

> **Common Thread:** Whenever a real-world system is modeled by a polynomial equation, these theorems tell you what kinds of solutions are possible, how to find them, and how they relate to the system's parameters — without necessarily solving the equation explicitly.

---

## Practice Problems

<!-- Add practice problems here -->
