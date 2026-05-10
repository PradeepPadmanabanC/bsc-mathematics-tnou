# Relationship between Roots and Coefficients

**Block:** 1 — Polynomial Equations  
**Course:** BMSS-11C — Algebra

## Table of Contents

- [Notes](#notes)
  - [Factor Theorem](#factor-theorem)
    - [Proof](#proof)
    - [Converse](#converse-also-true)
    - [Combined Statement](#combined-statement)
  - [Fundamental Theorem: An nᵗʰ Degree Equation Has Exactly n Roots](#fundamental-theorem-an-nᵗʰ-degree-equation-has-exactly-n-roots)
    - [Proof](#proof-1)
    - [Note on Multiplicity](#note-on-multiplicity)
  - [Location of Roots Theorem (Intermediate Value Theorem for Polynomials)](#location-of-roots-theorem-intermediate-value-theorem-for-polynomials)
    - [Proof](#proof-2)
    - [Geometric Interpretation](#geometric-interpretation)
    - [Important Remarks](#important-remarks)
    - [Worked Example](#worked-example)
  - [Complex Conjugate Root Theorem (Imaginary Roots Occur in Pairs)](#complex-conjugate-root-theorem-imaginary-roots-occur-in-pairs)
    - [Preliminary: Properties of Complex Conjugates](#preliminary-properties-of-complex-conjugates)
    - [Proof](#proof-3)
    - [Important Remarks](#important-remarks-1)
    - [Worked Example](#worked-example-1)
  - [Irrational Conjugate Root Theorem (Irrational Roots Occur in Pairs)](#irrational-conjugate-root-theorem-irrational-roots-occur-in-pairs)
    - [Part (a): Proof](#part-a-proof-that-a--b-and-a--b-occur-together)
    - [Part (b): Proof](#part-b-proof-that-a--b-gives-four-conjugate-roots)
    - [Important Remarks](#important-remarks-2)
    - [Worked Examples](#worked-examples)
  - [Relations between the Roots and Coefficients of Equations](#relations-between-the-roots-and-coefficients-of-equations)
    - [Summary of Relations](#summary-of-relations)
    - [Remark 1.1: Choosing Roots for Special Progressions](#remark-11-choosing-roots-for-special-progressions)
    - [Proof: Roots in H.P. ⟹ Roots of f(1/x) are in A.P.](#proof-roots-in-hp--roots-of-f1x--0-are-in-ap)
- [Examples](#examples)
- [Practice Problems](#practice-problems)

---

## Notes

### Factor Theorem

**Statement:**
Let f(x) = a₀xⁿ + a₁xⁿ⁻¹ + a₂xⁿ⁻² + ... + aₙ₋₁x + aₙ be a polynomial of degree n, where a₀ ≠ 0.

If α is a root of the equation f(x) = 0 (i.e., f(α) = 0), then (x − α) is a factor of f(x).

---

#### Proof

The proof relies on the **Polynomial Division Algorithm**.

**Step 1: Apply the Division Algorithm**

When we divide any polynomial f(x) by a linear polynomial (x − α), the division algorithm guarantees that there exist unique polynomials q(x) (the quotient) and r (the remainder) such that:

> **f(x) = (x − α) · q(x) + r**

where:
- q(x) is a polynomial of degree (n − 1)
- r is the remainder

Since the divisor (x − α) is of degree 1, the remainder r must have degree strictly less than 1. A polynomial of degree less than 1 is a constant. So **r is a constant** (a number, not depending on x).

**Step 2: Substitute x = α**

The identity f(x) = (x − α)·q(x) + r holds for **all** values of x, since it is a polynomial identity. In particular, it holds when x = α. Substituting:

> f(α) = (α − α) · q(α) + r  
> f(α) = 0 · q(α) + r  
> **f(α) = r**

So the remainder r equals f(α).

**Step 3: Use the hypothesis that α is a root**

We are given that α is a root of f(x) = 0, which means:

> **f(α) = 0**

From Step 2, we know r = f(α), therefore:

> **r = 0**

**Step 4: Conclude**

Substituting r = 0 back into the division identity:

> f(x) = (x − α) · q(x) + 0  
> **f(x) = (x − α) · q(x)**

This shows that f(x) is exactly (x − α) multiplied by q(x). By definition, this means **(x − α) is a factor of f(x)**. ∎

---

#### Converse (also true)

If (x − α) is a factor of f(x), then α is a root of f(x) = 0.

**Proof:** If (x − α) is a factor, then f(x) = (x − α)·q(x) for some polynomial q(x). Substituting x = α gives f(α) = (α − α)·q(α) = 0·q(α) = 0. So α is a root. ∎

---

#### Combined Statement

> **α is a root of f(x) = 0 ⟺ (x − α) is a factor of f(x)**

---

### Fundamental Theorem: An nᵗʰ Degree Equation Has Exactly n Roots

**Statement:**
Every polynomial equation of degree n,

> f(x) = a₀xⁿ + a₁xⁿ⁻¹ + a₂xⁿ⁻² + ... + aₙ₋₁x + aₙ = 0, where a₀ ≠ 0

has exactly n roots (counting multiplicity), real or complex.

---

#### Proof

The proof uses two ingredients:
1. **The Fundamental Theorem of Algebra** — every polynomial of degree ≥ 1 has at least one root (real or complex).
2. **The Factor Theorem** (proved above) — if α is a root of f(x) = 0, then f(x) = (x − α)·q(x).

We prove by **mathematical induction** on the degree n.

**Base case (n = 1):**

> f(x) = a₀x + a₁ = 0
> ⟹ x = −a₁/a₀

This gives exactly 1 root. ✓

**Inductive hypothesis:**

Assume every polynomial of degree k (where k < n) has exactly k roots.

**Inductive step (degree n):**

Let f(x) = a₀xⁿ + a₁xⁿ⁻¹ + ... + aₙ, where a₀ ≠ 0.

**Step 1:** By the Fundamental Theorem of Algebra, f(x) has at least one root. Call it α₁, so f(α₁) = 0.

**Step 2:** By the Factor Theorem, since α₁ is a root:

> f(x) = (x − α₁) · q₁(x)

where q₁(x) is a polynomial of degree (n − 1) with leading coefficient a₀.

**Step 3:** q₁(x) is a polynomial of degree (n − 1). By the Fundamental Theorem of Algebra, q₁(x) has at least one root α₂. By the Factor Theorem:

> q₁(x) = (x − α₂) · q₂(x)

So: f(x) = (x − α₁)(x − α₂) · q₂(x), where q₂(x) has degree (n − 2).

**Step 4:** Continuing this process, at the rᵗʰ step:

> f(x) = (x − α₁)(x − α₂)···(x − αᵣ) · qᵣ(x)

where qᵣ(x) has degree (n − r).

**Step 5:** After n steps (r = n), qₙ(x) has degree 0, so it is a constant. Since the leading coefficient is preserved through each factoring, qₙ(x) = a₀. Therefore:

> **f(x) = a₀(x − α₁)(x − α₂)···(x − αₙ)**

**Step 6:** Setting f(x) = 0:

> a₀(x − α₁)(x − α₂)···(x − αₙ) = 0

Since a₀ ≠ 0, we need (x − α₁)(x − α₂)···(x − αₙ) = 0, which gives exactly the solutions x = α₁, α₂, ..., αₙ.

**Step 7 (no extra roots exist):** If β is any root of f(x), then:

> a₀(β − α₁)(β − α₂)···(β − αₙ) = 0

Since a₀ ≠ 0, at least one factor (β − αᵢ) must be zero, so β = αᵢ for some i. Hence every root of f(x) is one of α₁, α₂, ..., αₙ.

**Conclusion:** f(x) = 0 has exactly n roots α₁, α₂, ..., αₙ (not necessarily distinct). ∎

---

#### Note on Multiplicity

The roots α₁, α₂, ..., αₙ need not all be distinct. If αᵢ appears m times, we say αᵢ is a root of **multiplicity m**. The theorem guarantees exactly n roots **counted with multiplicity**.

**Example:** f(x) = (x − 2)³(x + 1) = 0 is degree 4 and has:
- x = 2 with multiplicity 3
- x = −1 with multiplicity 1
- Total: 3 + 1 = 4 roots ✓

---

### Location of Roots Theorem (Intermediate Value Theorem for Polynomials)

**Statement:**
If f(x) is a polynomial and f(a) and f(b) are of **opposite signs** (i.e., one is positive and the other is negative), then at least one root of the equation f(x) = 0 lies between a and b.

In other words: if f(a) · f(b) < 0, then there exists at least one value c with a < c < b such that f(c) = 0.

---

#### Proof

The proof relies on a key property of polynomials: **every polynomial is a continuous function**.

**Step 1: Continuity of polynomials**

A polynomial f(x) = a₀xⁿ + a₁xⁿ⁻¹ + ... + aₙ is a sum of continuous functions (each term aᵢxⁿ⁻ⁱ is continuous), so f(x) itself is **continuous** on all of ℝ. In particular, f(x) is continuous on the closed interval [a, b].

**Step 2: Assume f(a) and f(b) have opposite signs**

Without loss of generality, suppose:

> f(a) < 0 and f(b) > 0

(The case f(a) > 0 and f(b) < 0 is handled identically by symmetry.)

**Step 3: Apply the Intermediate Value Theorem (IVT)**

The Intermediate Value Theorem states:

> If g is a continuous function on [a, b] and d is any value between g(a) and g(b), then there exists at least one c ∈ (a, b) such that g(c) = d.

Since f is continuous on [a, b], and since:

> f(a) < 0 < f(b)

the value 0 lies **between** f(a) and f(b). By the IVT, there exists at least one c with a < c < b such that:

> **f(c) = 0**

Therefore, c is a root of f(x) = 0 lying in the interval (a, b). ∎

---

#### Geometric Interpretation

The graph of y = f(x) is a continuous curve. If the curve is **below** the x-axis at x = a (since f(a) < 0) and **above** the x-axis at x = b (since f(b) > 0), then the curve must **cross** the x-axis at least once between a and b. Each crossing point is a root.

---

#### Important Remarks

1. The theorem guarantees **at least one** root — there may be more than one root between a and b.
2. If f(a) and f(b) have the **same sign**, we **cannot** conclude anything — there may or may not be roots between a and b. (The curve could dip down and come back up without crossing the axis.)
3. This theorem only applies to **real** roots, since we are considering the real-valued graph of f(x).

---

#### Worked Example

Let f(x) = x³ − 4x + 1. Find an interval containing a root.

> f(0) = 0 − 0 + 1 = **1** (positive)  
> f(1) = 1 − 4 + 1 = **−2** (negative)

Since f(0) > 0 and f(1) < 0, by the Location of Roots Theorem, there is at least one root in the interval **(0, 1)**.

We can narrow further:

> f(0.2) = 0.008 − 0.8 + 1 = **0.208** (positive)  
> f(0.3) = 0.027 − 1.2 + 1 = **−0.173** (negative)

So a root lies in **(0.2, 0.3)**.

---

### Complex Conjugate Root Theorem (Imaginary Roots Occur in Pairs)

**Statement:**
If f(x) = a₀xⁿ + a₁xⁿ⁻¹ + ... + aₙ₋₁x + aₙ = 0 is a polynomial equation with **real coefficients** (a₀, a₁, ..., aₙ ∈ ℝ), and if a + ib (where b ≠ 0) is a root, then its complex conjugate a − ib is also a root.

---

#### Preliminary: Properties of Complex Conjugates

Before the proof, recall these key properties. For any complex numbers z and w:

1. **Conjugate of a sum:** conjugate(z + w) = conjugate(z) + conjugate(w)
2. **Conjugate of a product:** conjugate(z · w) = conjugate(z) · conjugate(w)
3. **Conjugate of a power:** conjugate(zⁿ) = (conjugate(z))ⁿ
4. **Conjugate of a real number:** If c is real, then conjugate(c) = c

We denote the conjugate of z as z̄. So these become:

> (z + w)̄ = z̄ + w̄  
> (z · w)̄ = z̄ · w̄  
> (zⁿ)̄ = (z̄)ⁿ  
> If c ∈ ℝ, then c̄ = c

---

#### Proof

Let f(x) = a₀xⁿ + a₁xⁿ⁻¹ + a₂xⁿ⁻² + ... + aₙ₋₁x + aₙ, where all coefficients a₀, a₁, ..., aₙ are **real**.

Suppose α = a + ib (with b ≠ 0) is a root of f(x) = 0. Then:

> f(α) = a₀αⁿ + a₁αⁿ⁻¹ + a₂αⁿ⁻² + ... + aₙ₋₁α + aₙ = 0

**Step 1: Take the complex conjugate of both sides**

> conjugate(f(α)) = conjugate(0)

> conjugate(a₀αⁿ + a₁αⁿ⁻¹ + a₂αⁿ⁻² + ... + aₙ₋₁α + aₙ) = 0

**Step 2: Apply the conjugate-of-a-sum property**

> conjugate(a₀αⁿ) + conjugate(a₁αⁿ⁻¹) + conjugate(a₂αⁿ⁻²) + ... + conjugate(aₙ₋₁α) + conjugate(aₙ) = 0

**Step 3: Apply the conjugate-of-a-product property to each term**

> conjugate(a₀)·conjugate(αⁿ) + conjugate(a₁)·conjugate(αⁿ⁻¹) + ... + conjugate(aₙ₋₁)·conjugate(α) + conjugate(aₙ) = 0

**Step 4: Since all coefficients are real, conjugate(aᵢ) = aᵢ**

> a₀·conjugate(αⁿ) + a₁·conjugate(αⁿ⁻¹) + ... + aₙ₋₁·conjugate(α) + aₙ = 0

**Step 5: Apply the conjugate-of-a-power property: conjugate(αⁿ) = (conjugate(α))ⁿ = ᾱⁿ**

> a₀ᾱⁿ + a₁ᾱⁿ⁻¹ + a₂ᾱⁿ⁻² + ... + aₙ₋₁ᾱ + aₙ = 0

**Step 6: Recognize the left side**

The left side is exactly f(ᾱ). Therefore:

> **f(ᾱ) = 0**

Since ᾱ = conjugate(a + ib) = a − ib, we have shown that **a − ib is also a root** of f(x) = 0. ∎

---

#### Important Remarks

1. The condition that coefficients are **real** is essential. If coefficients are complex, conjugate roots need not occur in pairs.
2. This means for a polynomial with real coefficients, **complex roots always come in conjugate pairs**, so the number of complex (non-real) roots is always **even**.
3. As a consequence, a polynomial of **odd degree** with real coefficients must have **at least one real root** (since complex roots pair off, at least one root is left unpaired and must be real).

---

#### Worked Example

Consider f(x) = x² + 2x + 5 = 0 (all coefficients are real).

Using the quadratic formula:

> x = (−2 ± √(4 − 20)) / 2 = (−2 ± √(−16)) / 2 = (−2 ± 4i) / 2

> x = −1 + 2i  or  x = −1 − 2i

The roots are −1 + 2i and −1 − 2i — a conjugate pair, exactly as the theorem predicts. ✓

---

### Irrational Conjugate Root Theorem (Irrational Roots Occur in Pairs)

**Statement:**
If f(x) = 0 is a polynomial equation with **rational coefficients**, then irrational roots involving square roots occur in conjugate pairs.

**(a)** If a + √b is a root (where a, b are rational and √b is irrational), then a − √b is also a root.

**(b)** If √a + √b is a root (where √a and √b are both irrational and √a, √b are independent), then all four combinations are roots:
- √a + √b
- √a − √b
- −√a + √b
- −√a − √b

---

#### Part (a): Proof that a + √b and a − √b occur together

Let f(x) be a polynomial with rational coefficients, and suppose α = a + √b is a root, where a, b ∈ ℚ and √b ∉ ℚ.

**Step 1: Substitute α = a + √b into f(x) = 0**

Since f has rational coefficients, when we expand f(a + √b), every term is a polynomial expression in a and √b. Collecting terms, we can separate the result into a rational part and an irrational part:

> f(a + √b) = P + Q√b

where P and Q are **rational numbers** (they are rational combinations of the rational coefficients of f and the rational numbers a, b).

**Step 2: Since α is a root, f(α) = 0**

> P + Q√b = 0

**Step 3: Show P = 0 and Q = 0 separately**

Suppose Q ≠ 0. Then:

> √b = −P/Q

Since P and Q are rational, −P/Q is rational. But this contradicts our assumption that √b is irrational. Therefore:

> **Q = 0**

Substituting back: P + 0·√b = 0, so:

> **P = 0**

**Step 4: Evaluate f(a − √b)**

Now consider the conjugate ᾱ = a − √b. When we substitute into f(x):

> f(a − √b) = P − Q√b

(The only change is that every occurrence of √b flips sign, so the irrational part changes from +Q√b to −Q√b, while the rational part P stays the same.)

Since P = 0 and Q = 0:

> f(a − √b) = 0 − 0·√b = **0**

Therefore **a − √b is also a root** of f(x) = 0. ∎

---

#### Part (b): Proof that √a + √b gives four conjugate roots

Let f(x) be a polynomial with rational coefficients, and suppose α = √a + √b is a root, where a, b ∈ ℚ, √a and √b are both irrational, and √a/√b is also irrational (i.e., √a and √b are independent surds).

**Step 1: Substitute α = √a + √b into f(x) = 0**

When we expand f(√a + √b), every term involves powers of √a and √b. Collecting terms by their irrational parts, we can write:

> f(√a + √b) = P + Q√a + R√b + S√(ab)

where P, Q, R, S are all **rational numbers**.

(Here √(ab) = √a · √b appears because products of √a and √b generate this term.)

**Step 2: Since α is a root, f(α) = 0**

> P + Q√a + R√b + S√(ab) = 0

**Step 3: Show P = Q = R = S = 0**

Since √a, √b, and √(ab) are all irrational and **linearly independent over ℚ** (no rational combination of them equals a rational number unless all coefficients are zero), we must have:

> **P = 0, Q = 0, R = 0, S = 0**

**Step 4: Evaluate f at the other three conjugates**

Now substitute each conjugate and observe the sign pattern:

**For √a − √b:** (flip sign of √b)

> f(√a − √b) = P + Q√a − R√b − S√(ab) = 0 + 0 − 0 − 0 = **0** ✓

**For −√a + √b:** (flip sign of √a)

> f(−√a + √b) = P − Q√a + R√b − S√(ab) = 0 − 0 + 0 − 0 = **0** ✓

**For −√a − √b:** (flip signs of both √a and √b)

> f(−√a − √b) = P − Q√a − R√b + S√(ab) = 0 − 0 − 0 + 0 = **0** ✓

Therefore all four values are roots of f(x) = 0. ∎

---

#### Important Remarks

1. The condition that coefficients are **rational** is essential. If coefficients are irrational, conjugate surd roots need not occur in pairs.
2. Part (a) means irrational roots involving a single square root always come in **pairs**, so the number of such irrational roots is always **even**.
3. Part (b) means irrational roots involving two independent square roots come in **groups of four**.
4. These results extend naturally: if a root involves k independent square roots, it generates 2ᵏ conjugate roots.

---

#### Worked Examples

**Example for Part (a):**

Consider f(x) = x² − 6x + 7 = 0 (all coefficients are rational).

> x = (6 ± √(36 − 28)) / 2 = (6 ± √8) / 2 = 3 ± √2

The roots are 3 + √2 and 3 − √2 — a conjugate surd pair. ✓

**Example for Part (b):**

Consider f(x) = x⁴ − 10x² + 1 = 0 (all coefficients are rational).

Let y = x², then y² − 10y + 1 = 0:

> y = (10 ± √(100 − 4)) / 2 = 5 ± 2√6

So x² = 5 + 2√6 or x² = 5 − 2√6.

Note that 5 + 2√6 = (√3 + √2)² and 5 − 2√6 = (√3 − √2)².

Therefore the four roots are:

> x = √3 + √2, √3 − √2, −√3 + √2, −√3 − √2

All four conjugates appear, exactly as the theorem predicts. ✓

---

## Examples

### Worked Example

Let f(x) = x³ − 6x² + 11x − 6.

**Check that x = 1 is a root:**

> f(1) = 1 − 6 + 11 − 6 = 0 ✓

**By the Factor Theorem, (x − 1) is a factor.** Dividing:

> x³ − 6x² + 11x − 6 = (x − 1)(x² − 5x + 6)

Factoring further:

> x² − 5x + 6 = (x − 2)(x − 3)

So:

> f(x) = (x − 1)(x − 2)(x − 3)

The roots are x = 1, 2, 3 — and each corresponding linear factor divides f(x), exactly as the theorem predicts.

---

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

## Practice Problems

<!-- Add practice problems here -->
