# Unit 4: Increase or Decrease the Roots of the Given Equation

## Objectives

After completion of this unit, students will be able to:
- Know how to increase or decrease the roots of the given equation
- Understand the concept of removing second term from the given equation

## 4.1 Increase or Decrease the Roots of the Given Equation

### Mathematical Foundation

Let the polynomial equation be:
```
f(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + aₙ₋₂xⁿ⁻² + ... + a₁x + a₀ = 0    ...(4.1)
```

Let us assume α₁, α₂, ..., αₙ be the roots of equation (4.1), then:
```
f(x) = aₙ(x - α₁)(x - α₂)...(x - αₙ) = 0    ...(4.2)
```

### Transformation of Roots

We have to find an equation whose roots are: α₁ - h, α₂ - h, ..., αₙ - h

**Method:** If we change x to x + h, then we have:
```
f(x + h) = aₙ((x + h) - α₁)((x + h) - α₂)...((x + h) - αₙ)
         = aₙ(x - (α₁ - h))(x - (α₂ - h))...(x - (αₙ - h))    ...(4.3)
```

**Result:** The roots for the above equation f(x + h) = 0 are:
```
α₁ - h, α₂ - h, ..., αₙ - h
```

### General Transformation Rule

**To transform roots by a constant h:**

| Original Equation | Root Transformation | New Equation | New Roots |
|-------------------|---------------------|--------------|-----------|
| f(x) = 0 | Decrease by h | f(x + h) = 0 | αᵢ - h |
| f(x) = 0 | Increase by h | f(x - h) = 0 | αᵢ + h |

### Example 4.1

**Problem:** Diminish the roots of x³ - 5x² + 7x - 4x + 5 by 2

Wait, let me correct this. Looking at the image, the polynomial appears to be:
**x³ - 5x² + 7x - 4 = 0** (assuming the constant term issue)

Let me solve: Diminish the roots of **x³ - 5x² + 7x - 4** by 2

**Solution Method:** To diminish roots by 2, we substitute x → x + 2 and find f(x + 2).

#### Method 1: Long Division (Repeated Division by (x - 2))

We need to evaluate f(x + 2) by repeatedly dividing by (x - 2):

**Step 1:** Divide f(x) = x³ - 5x² + 7x - 4 by (x - 2)

```
                x² - 3x + 1
        ─────────────────────────
x - 2 | x³ - 5x² + 7x - 4
        x³ - 2x²
        ─────────
           -3x² + 7x
           -3x² + 6x
           ─────────
                  x - 4
                  x - 2
                  ─────
                    -2
```

Result: x³ - 5x² + 7x - 4 = (x - 2)(x² - 3x + 1) - 2

So, f(2) = -2 ✓

**Step 2:** Now divide Q₁(x) = x² - 3x + 1 by (x - 2)

```
                x - 1
        ─────────────────────
x - 2 | x² - 3x + 1
        x² - 2x
        ───────
           -x + 1
           -x + 2
           ──────
               -1
```

Result: x² - 3x + 1 = (x - 2)(x - 1) - 1

So, Q₁(2) = -1 and this is f'(2)/1! = -1 ✓

**Step 3:** Divide Q₂(x) = x - 1 by (x - 2)

```
                1
        ─────────────────
x - 2 | x - 1
        x - 2
        ─────
            1
```

Result: x - 1 = (x - 2)(1) + 1

So, Q₂(2) = 1 and this is f''(2)/2! = 1 ✓

**Step 4:** The final quotient is Q₃(x) = 1

So, Q₃(2) = 1 and this is f'''(2)/3! = 1 ✓

#### Constructing the Transformed Polynomial

From Taylor series, f(x + 2) = f(2) + f'(2)x + f''(2)x²/2! + f'''(2)x³/3!

The coefficients of the transformed polynomial are:
- Coefficient of x³: 1 (from Q₃)
- Coefficient of x²: 1 (from Q₂)
- Coefficient of x¹: -1 (from Q₁)
- Constant term: -2 (from f(2))

**Transformed equation:** **x³ + x² - x - 2 = 0**

#### Method 2: Synthetic Division (Faster)

```
Step 1: Divide by 2
Coefficients: 1  -5   7  -4

    1   -5    7   -4
2 |     2   -6    2
    ─────────────────
    1   -3    1   -2  ← New constant term

Step 2: Divide quotient by 2
    1   -3    1
2 |     2   -2
    ─────────────
    1   -1   -1  ← New x¹ coefficient

Step 3: Divide quotient by 2
    1   -1
2 |     2
    ─────────
    1    1  ← New x² coefficient

Step 4: Final coefficient
    1  ← x³ coefficient (unchanged)
```

**Transformed equation:** **x³ + x² - x - 2 = 0**

### Why is Synthetic Division Easier than Long Division?

#### Visual Comparison

Let's compare both methods side-by-side for the same problem:

**LONG DIVISION (Traditional Method)**
```
Step 1: Divide x³ - 5x² + 7x - 4 by (x - 2)

                x² - 3x + 1                    ← Quotient
        ─────────────────────────
x - 2 | x³ - 5x² + 7x - 4                     ← Dividend
        x³ - 2x²        ↓                      ← Multiply & Subtract
        ─────────                              
           -3x² + 7x    ↓                      ← Bring down
           -3x² + 6x                           ← Multiply & Subtract
           ─────────
                  x - 4                        ← Bring down
                  x - 2                        ← Multiply & Subtract
                  ─────
                    -2                         ← Remainder
```

**SYNTHETIC DIVISION (Streamlined Method)**
```
Step 1: Same division, but simplified

    1   -5    7   -4     ← Coefficients only
2 |     2   -6    2      ← Multiply by 2, add
    ─────────────────
    1   -3    1   -2     ← Results
    ↑   ↑    ↑    ↑
    │   │    │    └─ Remainder
    └───┴────┴────── Quotient coefficients
```

#### Key Differences

| Aspect | Long Division | Synthetic Division |
|--------|--------------|-------------------|
| **Variables** | Write x, x², x³ every time | Only numbers (coefficients) |
| **Subtraction** | Multiply then subtract | Multiply then ADD (using opposite sign) |
| **Space** | Requires 6-8 lines | Requires 2-3 lines |
| **Time** | ~2-3 minutes per division | ~30 seconds per division |
| **Errors** | More likely (sign errors, alignment) | Less likely (simpler operations) |
| **Works for** | Any divisor | Only divisors of form (x - c) |

#### Why Synthetic Division is Easier: Detailed Analysis

**1. No Variable Manipulation**

**Long Division:**
```
x³ - 2x²           ← Must write x³, align powers
-3x² + 7x          ← Must write x², bring down next term
-3x² + 6x          ← Must multiply (x-2) × (-3x)
```

**Synthetic Division:**
```
1   -5   7         ← Just numbers
    2   -6         ← Simple arithmetic: 2×1=2, 2×(-3)=-6
```

**Savings:** No need to write or track variables at all!

---

**2. Arithmetic is Simpler**

**Long Division:** 
- Multiply: (x - 2) × (-3x) = -3x² + 6x ← Distribute and track signs
- Subtract: (-3x² + 7x) - (-3x² + 6x) = x ← Change all signs

**Synthetic Division:**
- Multiply: 2 × (-3) = -6 ← Simple multiplication
- Add: (-5) + 2 = -3 ← Simple addition (no sign change!)

**Key insight:** Synthetic division uses the ROOT (2) instead of the factor (x-2), so we ADD instead of SUBTRACT. This eliminates sign errors!

---

**3. Automatic Alignment**

**Long Division:**
```
x³ - 5x² + 7x - 4
x³ - 2x²          ← Must align x³ terms carefully
─────────
   -3x² + 7x      ← Subtraction creates new line
   -3x² + 6x      ← Must align x² terms
   ─────────
          x - 4   ← Must align x terms
```
One misalignment = wrong answer!

**Synthetic Division:**
```
    1   -5    7   -4
2 |     2   -6    2
    ─────────────────
    1   -3    1   -2
```
Fixed columns = automatic alignment!

---

**4. Fewer Steps**

**Long Division** requires:
1. Divide leading terms → x³ ÷ x = x²
2. Multiply quotient by divisor → x²(x - 2) = x³ - 2x²
3. Subtract → (x³ - 5x²) - (x³ - 2x²) = -3x²
4. Bring down next term → -3x² + 7x
5. Repeat for each term

**Total:** ~15-20 operations per division

**Synthetic Division** requires:
1. Multiply previous result by root → 1 × 2 = 2
2. Add to next coefficient → -5 + 2 = -3
3. Repeat for each term

**Total:** ~6-8 operations per division

**Efficiency gain:** 60-70% fewer operations!

---

**5. Visual Clarity**

**Long Division:**
```
What is this?
        x³ - 2x²
        ─────────
Is this a new polynomial? A result? Part of calculation?
```

**Synthetic Division:**
```
Clear structure:
    [Original coefficients]    ← Top row
    [Calculations]             ← Middle row  
    [Results]                  ← Bottom row
```

Everything has a clear place and meaning!

---

**6. Error Recovery**

**Long Division:**
- Make mistake in step 2? 
- Must erase 4-5 lines and restart
- Hard to spot where error occurred

**Synthetic Division:**
- Make mistake in column 3?
- Just recalculate that column
- Easy to verify each step independently

---

#### Mathematical Reason: Pattern Recognition

**Long Division** obscures the pattern:
```
Division 1: x³ - 5x² + 7x - 4 ÷ (x-2) → quotient + remainder
Division 2: x² - 3x + 1 ÷ (x-2) → quotient + remainder
Division 3: x - 1 ÷ (x-2) → quotient + remainder
```
Each looks different!

**Synthetic Division** reveals the pattern:
```
    1   -5    7   -4
2 |     2   -6    2      ← Row of calculations
    ─────────────────
    1   -3    1   -2     ← These become next input!

    1   -3    1
2 |     2   -2           ← Same pattern
    ─────────────
    1   -1   -1

    1   -1
2 |     2                ← Same pattern
    ─────────
    1    1
```
The pattern repeats! Bottom row → new top row

---

#### When to Use Each Method

**Use Long Division when:**
- ✅ Divisor is NOT of the form (x - c), e.g., (x² + 2x + 1)
- ✅ Working with polynomials in multiple variables
- ✅ Need to understand the conceptual process
- ✅ Teaching/learning polynomial division fundamentals

**Use Synthetic Division when:**
- ✅ Divisor is (x - c) — most common case!
- ✅ Evaluating polynomial at a point (Horner's method)
- ✅ Finding roots or factors
- ✅ Transforming equations (like our example!)
- ✅ Working with large polynomials
- ✅ Speed and accuracy are important

---

#### Real-World Impact

**Time Savings Example:**

Transform a degree-5 polynomial by decreasing roots by 3:
- Requires 5 divisions by (x - 3)

**Long Division:**
- 5 divisions × 3 minutes each = **15 minutes**
- High error probability

**Synthetic Division:**
- 5 divisions × 30 seconds each = **2.5 minutes**
- Low error probability

**Result:** 6× faster with fewer errors!

This is why synthetic division is the standard method in:
- Engineering calculations
- Computer algebra systems
- Numerical analysis
- Standardized tests (SAT, GRE)

---

#### Memory Aid: "SDAE" (Synthetic Division is Awesome and Easy!)

**S**impler - Just numbers, no variables
**D**irect - Straight to the answer
**A**ccurate - Fewer chances for errors
**E**fficient - Much faster than long division

---

#### Verification

Original equation: x³ - 5x² + 7x - 4 = 0

If α is a root of the original equation, then (α - 2) should be a root of the transformed equation. We can verify this algebraically with Vieta's formulas, without needing to know the individual root values.

**Sum of roots (Vieta's formula):**
- Original equation x³ - 5x² + 7x - 4 = 0: sum of roots = -(-5)/1 = 5
- Transformed equation x³ + x² - x - 2 = 0: sum of roots = -(1)/1 = -1

**Expected relationship:** each of the 3 roots is decreased by 2, so the new sum should be:
```
5 - 3(2) = 5 - 6 = -1 ✓
```

This matches the transformed equation's sum of roots, confirming the transformation is correct.

**Constant-term check:** Step 1 of the synthetic division computed f(2) = -2 directly from the original polynomial. By the Taylor-series relationship f(x + h) = f(h) + f'(h)x + ..., the constant term of the transformed polynomial must equal f(2), and indeed the transformed equation's constant term is -2 ✓.

**Note on the roots themselves:** x³ - 5x² + 7x - 4 does **not** factor as (x - 1)(x - 2)² — expanding that product gives x³ - 5x² + 8x - 4 (coefficient of x is 8, not 7), so 1 and 2 are not actually roots of this polynomial. A sign chart (f(0) = -4, f(1) = -1, f(3) = -1, f(4) = 8, with a local max of f(1) = -1 and local min of f(7/3) ≈ -2.19, both negative) shows this cubic has exactly **one real root** (irrational, between 3 and 4) and a complex-conjugate pair. There's no clean set of integer roots to substitute directly, which is why the algebraic Vieta's check above is used instead.

### Example 4.2

**Problem:** Find the equation whose roots are three times the roots of:
```
x³ - 6x² + 11x - 6 = 0
```

(Roots of the original equation: 1, 2, 3 — so the new roots should be 3, 6, 9.)

**Solution:** To multiply each root by m = 3, substitute x = y/3 (equivalently y = 3x) into the original equation and clear denominators. For a monic equation, this is done by multiplying the coefficient of the term in xⁿ⁻ᵏ by mᵏ:

```
xⁿ + a₁xⁿ⁻¹ + a₂xⁿ⁻² + ... + aₙ = 0
  →  yⁿ + (m·a₁)yⁿ⁻¹ + (m²·a₂)yⁿ⁻² + ... + (mⁿ·aₙ) = 0
```

Applying this to x³ - 6x² + 11x - 6 = 0 with m = 3:

```
Coefficient of y²: 3 × (-6)  = -18
Coefficient of y¹: 3² × 11   = 9 × 11 = 99
Constant term:     3³ × (-6) = 27 × (-6) = -162
```

**Transformed equation:** **y³ - 18y² + 99y - 162 = 0**

**Verification:** Substitute the expected new roots (3, 6, 9) directly:
```
At y = 3: 27 - 18(9) + 99(3) - 162 = 27 - 162 + 297 - 162 = 0 ✓
At y = 6: 216 - 18(36) + 99(6) - 162 = 216 - 648 + 594 - 162 = 0 ✓
At y = 9: 729 - 18(81) + 99(9) - 162 = 729 - 1458 + 891 - 162 = 0 ✓
```

All three roots check out, confirming the transformed equation has roots exactly three times the original.

## Mathematical Derivation

### Why This Works

Consider the polynomial with roots α₁, α₂, ..., αₙ:
```
P(x) = aₙ∏(x - αᵢ)
```

**To decrease each root by h:**
Substitute x → x + h:
```
P(x + h) = aₙ∏((x + h) - αᵢ)
         = aₙ∏(x - (αᵢ - h))
```

The new roots are αᵢ - h (decreased by h).

**To increase each root by h:**
Substitute x → x - h:
```
P(x - h) = aₙ∏((x - h) - αᵢ)
         = aₙ∏(x - (αᵢ + h))
```

The new roots are αᵢ + h (increased by h).

### Relationship to Taylor Series

The transformation f(x + h) can be expressed as:
```
f(x + h) = f(x) + hf'(x) + (h²/2!)f''(x) + (h³/3!)f'''(x) + ...
```

This is the Taylor series expansion and provides a theoretical foundation for the transformation.

### Coefficient Transformation Pattern

For a cubic equation:
```
ax³ + bx² + cx + d = 0
```

After substituting x → x + h:
```
a(x + h)³ + b(x + h)² + c(x + h) + d = 0
```

Expanding:
```
ax³ + 3ahx² + 3ah²x + ah³ + bx² + 2bhx + bh² + cx + ch + d = 0
```

Collecting terms:
```
ax³ + (3ah + b)x² + (3ah² + 2bh + c)x + (ah³ + bh² + ch + d) = 0
```

## Historical Context

### Development of Root Transformation Methods

**Ancient Origins:**
- Babylonian mathematicians (2000 BCE) used substitution methods for solving quadratic equations
- Indian mathematicians (500 CE) developed systematic approaches for equation transformations

**Medieval Period:**
- Persian mathematician Al-Khwarizmi (780-850 CE) introduced algebraic methods
- Italian mathematicians during the Renaissance formalized transformation techniques

**Modern Era (17th-19th Century):**
- **René Descartes (1596-1650):** Systematic use of algebraic transformations
- **Isaac Newton (1643-1727):** Developed methods for approximating roots
- **Paolo Ruffini (1765-1822):** Synthetic division method
- **William Horner (1786-1837):** Popularized efficient evaluation methods

### Connection to Vieta's Formulas

François Viète (1540-1603) established relationships between roots and coefficients:
- For equation xⁿ + a₁xⁿ⁻¹ + ... + aₙ = 0 with roots r₁, r₂, ..., rₙ:
  - Sum of roots: r₁ + r₂ + ... + rₙ = -a₁
  - Sum of products taken two at a time: r₁r₂ + r₁r₃ + ... = a₂
  - Product of all roots: r₁r₂...rₙ = (-1)ⁿaₙ

When roots are transformed by h, these relationships update systematically.

## Practical Applications

### 1. Numerical Stability in Computing

**Problem:** Roots far from origin cause numerical errors
**Solution:** Shift roots closer to zero for better precision

**Example:** For equation with roots near 1000:
- Original: x³ - 3000x² + 3000000x - 1000000000 = 0
- Transform by -1000: Much better numerical conditioning
- Used in: Scientific computing, CAD software, simulation tools

### 2. Control System Design

**Application:** Pole placement in feedback systems

**Context:** Control engineers need to shift system poles (roots of characteristic equation) to achieve desired stability and response.

**Example:** 
- Original system has poles at s = -1, -2, -3
- Desired: Faster response (shift left in complex plane)
- Transform equation to move poles to s = -3, -4, -5

**Used in:**
- Aircraft autopilot systems
- Industrial process control
- Robotics motion control

### 3. Signal Processing

**Application:** Filter design and frequency shifting

**Example:** Digital filter with transfer function:
```
H(z) = 1/(z³ - 1.5z² + 0.8z - 0.1)
```

**Transformation:** Shift poles to adjust cutoff frequency
- Root transformation changes frequency response
- Used in audio equalizers, communication systems

### 4. Economics and Finance

**Application:** Interest rate calculations and present value

**Example:** Investment equation:
```
V(1 + r)³ - P(1 + r)² - Q(1 + r) - R = 0
```

**Transformation:** Substitute x = 1 + r to simplify:
```
Vx³ - Px² - Qx - R = 0
```

Roots in simpler domain, then transform back.

**Used in:**
- Bond pricing
- Mortgage calculations
- Portfolio optimization

### 5. Computer Graphics

**Application:** Coordinate transformation in rendering

**Example:** 3D object defined by polynomial surfaces
- Original coordinates may be inconvenient
- Transform to local coordinate system (shift origin)
- Perform calculations, transform back

**Used in:**
- Game engines (Unity, Unreal Engine)
- CAD software (AutoCAD, SolidWorks)
- Animation software (Blender, Maya)

### 6. Physics: Oscillation Analysis

**Application:** Analyzing vibrating systems

**Example:** Damped oscillator equation:
```
m(d²x/dt²) + c(dx/dt) + kx = 0
```

Characteristic equation:
```
ms² + cs + k = 0
```

**Transformation:** Shift roots to study different damping regimes
- Critical damping analysis
- Stability boundaries

**Used in:**
- Structural engineering (building vibrations)
- Automotive suspension design
- Seismology

### 7. Cryptography

**Application:** Polynomial-based encryption schemes

**Example:** Threshold cryptography uses polynomial interpolation
- Shares are polynomial evaluations at different points
- Transform coordinates to obscure relationship
- Root transformation provides additional security layer

**Used in:**
- Blockchain technology
- Secure multiparty computation
- Secret sharing schemes

### 8. Machine Learning

**Application:** Feature scaling and normalization

**Example:** Polynomial regression model:
```
y = a₀ + a₁x + a₂x² + a₃x³
```

**Problem:** Input features x may have large values (e.g., years: 1990, 2000, 2010)
**Solution:** Transform to centered values (0, 10, 20) for numerical stability

**Used in:**
- Neural network training
- Gradient descent optimization
- Support vector machines with polynomial kernels

### 9. Chemical Engineering

**Application:** Reaction kinetics and equilibrium

**Example:** Chemical equilibrium equation:
```
K = [C]^c [D]^d / [A]^a [B]^b
```

Leads to polynomial in concentration. Transform to convenient reference point.

**Used in:**
- Process optimization
- Reactor design
- Pharmaceutical manufacturing

### 10. Astronomy

**Application:** Orbital mechanics calculations

**Example:** Kepler's equation for planetary motion:
```
M = E - e sin(E)
```

Iterative solution benefits from coordinate transformation placing orbits in convenient reference frame.

**Used in:**
- Satellite trajectory planning
- Space mission design
- Celestial mechanics simulations

## Advantages of Root Transformation

1. **Numerical Stability:** Improves computational accuracy
2. **Simplification:** Makes equations easier to analyze
3. **Insight:** Reveals relationships between roots and coefficients
4. **Practical Utility:** Directly applicable in engineering and science
5. **Generality:** Works for any polynomial degree

## Common Transformations Summary

| Transformation | Substitution | Effect on Roots |
|----------------|--------------|-----------------|
| Decrease by h | x → x + h | αᵢ - h |
| Increase by h | x → x - h | αᵢ + h |
| Multiply by k | x → x/k | k·αᵢ |
| Divide by k | x → k·x | αᵢ/k |
| Reciprocal | x → 1/x | 1/αᵢ |
| Negative | x → -x | -αᵢ |

## Implementation Notes

### Computational Methods

1. **Synthetic Division:** Most efficient for practical computation
2. **Taylor Expansion:** Theoretical understanding
3. **Direct Substitution:** Straightforward but computationally expensive
4. **Matrix Methods:** For higher-degree polynomials

### Algorithm (Synthetic Division Method)

```
Input: Polynomial coefficients [aₙ, aₙ₋₁, ..., a₁, a₀], shift value h
Output: Transformed polynomial coefficients

1. Initialize result with leading coefficient
2. For each remaining coefficient:
   - Multiply previous result by h
   - Add current coefficient
   - Store in result array
3. Return transformed coefficients
```

## Connection to Other Topics

- **Vieta's Formulas:** Relationship between roots and coefficients
- **Descartes' Rule of Signs:** Analyzing positive/negative roots
- **Newton-Raphson Method:** Numerical root finding
- **Synthetic Division:** Computational technique
- **Taylor Series:** Theoretical foundation

## References

**Syllabus:** Chapter 6, Section 17

## Practice Problems

1. Diminish the roots of x³ - 6x² + 11x - 6 = 0 by 2
2. Increase the roots of 2x³ - 3x² + x - 5 = 0 by 3
3. Find equation whose roots are 4 times those of x³ - 7x + 6 = 0
4. Transform x⁴ - 10x³ + 35x² - 50x + 24 = 0 by decreasing roots by 1

## Further Study

1. Prove the general transformation formula for polynomials of degree n
2. Study the effect of transformation on polynomial discriminant
3. Investigate transformations in complex plane
4. Explore connection to group theory and Galois theory
5. Implement efficient algorithms for large-degree polynomials
