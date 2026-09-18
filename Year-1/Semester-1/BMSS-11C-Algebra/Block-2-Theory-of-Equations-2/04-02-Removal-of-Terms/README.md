# 4.2 Removal of Terms

## Overview

One of the main applications of root transformation is to remove a certain specified term from an equation. This transformation of equation helps in solving the equation easily.

Removing specific terms (especially the second term) simplifies polynomial equations and reveals important properties about the roots.

## Mathematical Foundation

### General Polynomial Equation

Let the given equation be:
```
aₙxⁿ + aₙ₋₁xⁿ⁻¹ + aₙ₋₂xⁿ⁻² + ... + a₁x + a₀ = 0    ...(4.4)
```

### Removing the Second Term

If we substitute **x = y + h** in equation (4.4), we obtain a new equation:

```
aₙ(y + h)ⁿ + aₙ₋₁(y + h)ⁿ⁻¹ + aₙ₋₂(y + h)ⁿ⁻² + ... + a₁(y + h) + a₀ = 0    ...(4.5)
```

If we arrange the above equation in descending powers of y, we get:

```
aₙyⁿ + (naₙh + aₙ₋₁)yⁿ⁻¹ + (n(n-1)/2 · aₙh² + (n-1)aₙ₋₁h + aₙ₋₂)yⁿ⁻² + ... = 0
```

### To Remove the Second Term

In order to remove the second term, we can put:
```
naₙh + aₙ₋₁ = 0

Therefore: h = -aₙ₋₁/(naₙ)
```

Similarly to remove the third term, we can put:
```
n(n-1)/2 · aₙh² + (n-1)aₙ₋₁h + aₙ₋₂ = 0
```
and solve the equation for h.

## Note 4.2

### (i) To remove the second term:

We can diminish the roots of equation by h, where:

```
┌──────────────┐
│  h = -aₙ₋₁   │
│      ────     │
│       naₙ    │
└──────────────┘
```

### (ii) To remove the third term:

We can diminish the roots of the equation by h, where:

```
┌────────────────────────────────────────┐
│  n(n-1)/2 · aₙh² + (n-1)aₙ₋₁h + aₙ₋₂ = 0  │
└────────────────────────────────────────┘
```

## Standard Formulas for Different Degrees

### Cubic Equation (n = 3)

For: **ax³ + bx² + cx + d = 0**

**To remove x² term:**
```
Substitute: x = y - b/(3a)

Result: ay³ + py + q = 0  (Depressed cubic)

Where:
p = c - b²/(3a)
q = d - bc/(3a) + 2b³/(27a²)
```

### Quartic Equation (n = 4)

For: **ax⁴ + bx³ + cx² + dx + e = 0**

**To remove x³ term:**
```
Substitute: x = y - b/(4a)

Result: ay⁴ + py² + qy + r = 0  (Depressed quartic)

Where:
p = c - 3b²/(8a)
q = d - bc/(2a) + b³/(8a²)
r = e - bd/(4a) + b²c/(16a²) - 3b⁴/(256a³)
```

### General Formula

For polynomial of degree n with leading coefficient aₙ:

**To remove the xⁿ⁻¹ term:**
```
h = -aₙ₋₁/(naₙ)
```

## Example 4.6

**Problem:** Remove the second term of the equation:
```
x³ - 12x² + 48x - 72 = 0
```

**Solution:** To remove the second term, we can diminish the roots by:
```
h = -b/(3a) = -(-12)/(3·1) = 12/3 = 4
```

Substitute x = y + 4 using synthetic division:

**Step 1:** Divide by 4
```
     1   -12    48   -72
4  |      4   -32    64
     ──────────────────
     1    -8    16    -8
```

**Step 2:** Divide by 4
```
     1    -8    16
4  |      4   -16
     ─────────────
     1    -4     0  ← Second term eliminated!
```

**Step 3:** Divide by 4
```
     1    -4
4  |      4
     ────────
     1     0
```

**Final:** Coefficient of y³: 1

Thus, the transformed equation is: **y³ + 0·y² + 0·y - 8 = 0**

Or simply: **y³ - 8 = 0**

Now we can put y³ = 8, so y = 2 in the above equation, we get x = y + 4 = 6

## Example 4.7

**Problem:** Remove the second term of the equation:
```
x⁴ - 12x³ + 48x² - 72x + 35 = 0
```

**Solution:** To remove the second term, we can diminish the roots by:
```
h = -b/(na) = -(-12)/(4·1) = 12/4 = 3
```

Substitute x = y + 3 using synthetic division:

**Step 1:** Divide by 3
```
     1   -12    48   -72    35
3  |      3   -27    63   -27
     ────────────────────────
     1    -9    21    -9     8
```

**Step 2:** Divide by 3
```
     1    -9    21    -9
3  |      3   -18     9
     ──────────────────
     1    -6     3     0  ← Second term will be eliminated after next step
```

**Step 3:** Divide by 3
```
     1    -6     3
3  |      3    -9
     ─────────────
     1    -3    -6
```

**Step 4:** Divide by 3
```
     1    -3
3  |      3
     ────────
     1     0
```

Thus, the transformed equation is: **y⁴ - 6y² + 8 = 0**

Now we can put z = y² in the above equation, we get z² - 6z + 8 = 0

This is a quadratic in z that can be easily solved.

## Derivation: Why This Works

### For Cubic Equations

Consider: **ax³ + bx² + cx + d = 0**

Substitute: **x = y + h**

Expanding:
```
a(y + h)³ + b(y + h)² + c(y + h) + d = 0

a(y³ + 3y²h + 3yh² + h³) + b(y² + 2yh + h²) + c(y + h) + d = 0

ay³ + 3ay²h + 3ayh² + ah³ + by² + 2byh + bh² + cy + ch + d = 0

ay³ + (3ah + b)y² + (3ah² + 2bh + c)y + (ah³ + bh² + ch + d) = 0
```

**Coefficient of y²:** 3ah + b

**To eliminate:** Set 3ah + b = 0
```
h = -b/(3a)
```

### For Quartic Equations

Consider: **ax⁴ + bx³ + cx² + dx + e = 0**

Substitute: **x = y + h**

After expansion (using binomial theorem):

**Coefficient of y³:** 4ah + b

**To eliminate:** Set 4ah + b = 0
```
h = -b/(4a)
```

### General Pattern (Degree n)

For: **aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... = 0**

After substituting x = y + h:

**Coefficient of yⁿ⁻¹:** naₙh + aₙ₋₁

**To eliminate:** Set naₙh + aₙ₋₁ = 0
```
h = -aₙ₋₁/(naₙ)
```

This comes from the binomial expansion of (y + h)ⁿ where the coefficient of yⁿ⁻¹ is n·h.

## Historical Background

### Origins of Term Removal

**Ancient Mathematics:**
- Babylonian and Greek mathematicians worked with specific forms of equations
- Often avoided negative numbers and "incomplete" forms

**Islamic Golden Age (9th-12th Century):**
- **Al-Khwarizmi (780-850 CE):** Classified equations into standard forms
- Developed systematic methods for "completing" equations

**Renaissance Period (16th Century):**
- **Gerolamo Cardano (1501-1576):** Used term removal extensively
  - In solving cubic equations, removed x² term to get "depressed cubic"
  - Published in *Ars Magna* (1545), though the underlying method traces to **Scipione del Ferro** (~1515) and was independently found by **Niccolò Tartaglia**; Cardano's book is the one that made it public, with attribution to both
- **Ludovico Ferrari (1522-1565):** Extended to quartic equations

### The Depressed Cubic

**Historical Context:**
- Cardano's formula for solving cubics required eliminating the x² term
- This became known as the "depressed cubic" (missing the second-degree term)
- Fundamental to the solution method

**Original Form:**
```
x³ + px + q = 0
```

This simplified form was essential because:
1. Fewer terms to manipulate
2. Symmetric properties more visible
3. Solution formula becomes cleaner

### François Viète (1540-1603)

- Developed systematic algebraic transformations
- Showed that removing terms reveals relationships between roots
- Connected to his formulas relating roots and coefficients

### Modern Significance

**19th-20th Century:**
- **Évariste Galois (1811-1832):** Used transformations in group theory
- **Emmy Noether (1882-1935):** Abstract algebra perspective
- Term removal became foundation for:
  - Normal forms in differential equations
  - Canonical forms in linear algebra
  - Standard forms in optimization

## Practical Applications

### 1. Solving Cubic Equations (Cardano's Method)

**Application:** Essential first step in Cardano's formula

**Process:**
1. Given: ax³ + bx² + cx + d = 0
2. Remove x² term → y³ + py + q = 0
3. Apply Cardano's formula
4. Transform back to get original roots

**Used in:**
- Computer algebra systems (Mathematica, Maple)
- Engineering calculations
- Scientific computing libraries (NumPy, SciPy)

**Example:** Solving x³ - 6x² + 11x - 6 = 0
- Remove x² term: y³ - y = 0 (much simpler!)
- Factor: y(y² - 1) = 0
- Roots: y = 0, ±1
- Original roots: x = 2, 1, 3

### 2. Solving Quartic Equations (Ferrari's Method)

**Application:** Ferrari's solution requires depressed quartic

**Process:**
1. Remove x³ term
2. Equation becomes: x⁴ + px² + qx + r = 0
3. Apply Ferrari's method (reduces to cubic)
4. Transform back

**Used in:**
- Computer graphics (intersection calculations)
- Robotics (inverse kinematics with 4 DOF)
- Physics (quartic potentials in quantum mechanics)

### 3. Differential Equations

**Application:** Simplifying ODEs to normal form

**Example:** Second-order ODE:
```
y'' + p(x)y' + q(x)y = 0
```

**Transform:** Let y = u·e^(-∫p(x)dx/2)

**Result:** Eliminates first derivative term
```
u'' + Q(x)u = 0  (normal form)
```

**Used in:**
- Quantum mechanics (Schrödinger equation)
- Vibration analysis
- Wave equations

### 4. Control Systems Engineering

**Application:** State-space transformation to controllable canonical form

**Original system:**
```
ẋ = Ax + Bu
y = Cx + Du
```

**Transform to remove unwanted coupling terms**

**Used in:**
- Aircraft control systems
- Robotics control
- Industrial process control

### 5. Optimization Problems

**Application:** Converting to standard form for solution algorithms

**Example:** Minimize f(x) = x⁴ + 6x³ + 9x² + 2x + 1

**Transform:** Let x = y - 3/2 to remove cubic term

**Result:** Simpler optimization landscape

**Used in:**
- Machine learning (neural network training)
- Operations research
- Engineering design optimization

### 6. Computer Graphics: Bézier Curves

**Application:** Converting Bézier curves to power basis

**Bézier Form:** Has specific structure
**Power Basis:** Polynomial form

**Transformation:** May remove certain terms for efficiency

**Used in:**
- Font rendering
- Vector graphics (SVG)
- 3D modeling software

### 7. Signal Processing: Filter Design

**Application:** Designing filters with specific frequency response

**Transfer Function:**
```
H(s) = (s³ + as² + bs + c)/(s³ + ds² + es + f)
```

**Transform:** Remove s² terms for specific filter characteristics

**Used in:**
- Audio equalizers
- Communication systems
- Image processing

### 8. Structural Engineering

**Application:** Analyzing beam vibrations

**Characteristic Equation:**
```
λ⁴ + aλ³ + bλ² + cλ + d = 0
```

**Remove λ³ term:** Simplifies stability analysis

**Used in:**
- Bridge design
- Building vibration analysis
- Earthquake engineering

### 9. Chemistry: Equilibrium Problems

**Application:** Multi-step equilibrium reactions

**Example:** pH calculations with polyprotic acids

**Equation:** May have 3-4 terms
**Simplify:** Remove intermediate terms under certain conditions

**Used in:**
- Pharmaceutical formulations
- Industrial chemistry
- Environmental chemistry

### 10. Economics: Polynomial Cost Functions

**Application:** Analyzing cost structures

**Cost Function:**
```
C(x) = ax⁴ + bx³ + cx² + dx + e
```

**Transform:** Remove certain terms to identify break-even points

**Used in:**
- Business analytics
- Economic modeling
- Production optimization

### 11. Cryptography: Polynomial-Based Schemes

**Application:** Homomorphic encryption

**Context:** Operations on encrypted polynomials

**Transform:** Shift/normalize polynomial coefficients before encoding (this changes the coefficients, not the degree)

**Used in:**
- Secure cloud computing
- Privacy-preserving data analysis
- Blockchain applications

### 12. Machine Learning: Feature Engineering

**Application:** Polynomial feature transformation

**Original:** Multiple polynomial features
**Transform:** Remove redundant or correlated terms

**Used in:**
- Regression models
- Support Vector Machines
- Neural network preprocessing

## Advantages of Term Removal

1. **Simplification:** Fewer terms → easier manipulation
2. **Symmetry Revelation:** Hidden patterns become visible
3. **Solution Methods:** Many techniques require specific forms
4. **Numerical Stability:** Fewer terms → less rounding error
5. **Theoretical Insight:** Reveals root relationships
6. **Computational Efficiency:** Faster algorithms

## Connection to Root Properties

### Vieta's Formulas

For equation: xⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₀ = 0

**Sum of roots:** r₁ + r₂ + ... + rₙ = -aₙ₋₁

**When second term is removed:** aₙ₋₁ = 0

**Therefore:** Sum of roots = 0

**Interpretation:** The roots are centered at the origin (their centroid is 0) — this does *not* mean the individual roots are symmetric in pairs (e.g. {1, 1, −2} sums to 0 without any ±r pairing).

### Geometric Interpretation

**Cubic with x² term:**
```
x³ + bx² + cx + d = 0
Roots: α, β, γ where α + β + γ = -b
```

**After removing x²:**
```
y³ + py + q = 0
New roots: α', β', γ' where α' + β' + γ' = 0
```

**Meaning:** Shifted so the centroid of the roots sits at the origin (not necessarily a symmetric ± pairing of individual roots)

## Why This Matters

### Historical Breakthrough

Removing the second term was **crucial** for:
- First published general solution of cubic equations (Cardano, 1545, building on del Ferro and Tartaglia)
- First general solution of quartic equations (Ferrari, 1540s)
- Understanding that quintic equations can't be solved by radicals (the **Abel–Ruffini theorem**: Ruffini gave an incomplete proof in 1799, Abel gave a complete proof in 1824)

### Modern Relevance

Still fundamental in:
- **Computer Algebra Systems:** Pre-processing step
- **Numerical Methods:** Conditioning for better accuracy
- **Theoretical Mathematics:** Normal forms and canonical representations
- **Applied Mathematics:** Simplifying real-world problems

## Comparison: Before and After

### Example: x³ - 6x² + 11x - 6 = 0

**Before removal (original):**
- Three non-zero terms
- Roots not obvious
- Difficult to factor mentally

**After removal (y³ - y = 0):**
- Only two terms!
- Immediately factorable: y(y² - 1) = 0
- Roots obvious: y = 0, ±1
- Original roots: x = 2, 1, 3

**Simplification factor:** Transformed a complex cubic into trivial factorization!

## Implementation Algorithm

### Pseudocode for Removing Second Term

```python
def remove_second_term(coefficients):
    """
    Remove second term from polynomial equation
    
    Input: [aₙ, aₙ₋₁, aₙ₋₂, ..., a₁, a₀]
    Output: [bₙ, 0, bₙ₋₂, ..., b₁, b₀]
    """
    n = len(coefficients) - 1  # degree
    a_n = coefficients[0]
    a_n_minus_1 = coefficients[1]
    
    # Calculate shift value
    h = -a_n_minus_1 / (n * a_n)
    
    # Apply synthetic division n times
    result = coefficients.copy()
    for i in range(n):
        result = synthetic_divide(result, h)
    
    return result
```

### Verification Check

After transformation, verify that:
- Coefficient of xⁿ⁻¹ term is 0 (or very close to 0)
- Degree remains the same
- Number of roots unchanged

## Common Pitfalls and Solutions

### Pitfall 1: Arithmetic Errors

**Problem:** Sign errors when calculating h
**Solution:** Double-check: h = -aₙ₋₁/(naₙ) with correct signs

### Pitfall 2: Forgetting to Transform Back

**Problem:** Finding roots of transformed equation but not original
**Solution:** Remember: if y is root of transformed, then x = y + h is root of original

### Pitfall 3: Rounding Errors

**Problem:** With complex fractions, small errors accumulate
**Solution:** Use exact fractions or high-precision arithmetic

### Pitfall 4: Wrong Term Removal

**Problem:** Trying to remove wrong term (e.g., removing x term instead of x²)
**Solution:** Always remove xⁿ⁻¹ term (second term) first

## Related Topics

- Vieta's Formulas
- Symmetric Functions of Roots
- Cardano's Formula for Cubics
- Ferrari's Method for Quartics
- Galois Theory
- Normal Forms in ODEs
- Canonical Forms in Linear Algebra

## References

**Syllabus:** Chapter 6, Section 19

## Practice Problems

1. Remove the second term from: x³ + 9x² + 24x + 20 = 0
2. Remove the second term from: x⁴ - 8x³ + 24x² - 32x + 16 = 0
3. Transform 2x³ - 12x² + 18x - 8 = 0 to remove the x² term
4. Show that after removing the second term, the sum of roots equals 0
5. Remove the second term from: x⁵ - 5x⁴ + 10x³ - 10x² + 5x - 1 = 0

## Solutions Guide

### Problem 1: x³ + 9x² + 24x + 20 = 0

h = -9/(3·1) = -3

Substitute x = y - 3:
- Result: y³ - 3y + 2 = 0
- Verify: No y² term ✓

### Problem 2: x⁴ - 8x³ + 24x² - 32x + 16 = 0

h = -(-8)/(4·1) = 2

Substitute x = y + 2:
- Result: y⁴ = 0
- Meaning: y = 0 (quadruple root)
- Original: x = 2 (quadruple root) ✓

## Further Study

1. Prove the general formula for removing the kth term
2. Study term removal in polynomials over complex numbers
3. Investigate connections to group theory and Galois theory
4. Explore numerical stability of transformation methods
5. Research applications in modern computer algebra systems
6. Study term removal in multivariate polynomials
7. Investigate use in solving systems of polynomial equations
