# Unit 11: Cayley-Hamilton Theorem

**Block:** III — Matrices
**Course:** BMSS-11C — Algebra

## Objectives

After completion of this unit, students will be able to:
- verify Cayley Hamilton theorem for the given matrix.
- find the inverse of a matrix using Cayley-Hamilton theorem.

## Table of Contents

- [11.1 Cayley-Hamilton Theorem](#111-cayley-hamilton-theorem)
- [Worked Examples](#worked-examples)
- [Mathematical Derivation](#mathematical-derivation)
- [Historical Context](#historical-context)
- [Practical Applications](#practical-applications)

## 11.1 Cayley-Hamilton Theorem

### Theorem 11.1. Cayley-Hamilton Theorem

**Every square matrix satisfies its own characteristic equation.**

That is, if A is a square matrix of order n with characteristic equation

```
(−1)^n λ^n + c_(n−1)λ^(n−1) + ... + c_1λ + c_0 = 0
```

then replacing λ by A (and the constant term c_0 by c_0·I) gives a matrix equation that holds identically:

```
(−1)^n A^n + c_(n−1)A^(n−1) + ... + c_1A + c_0 I = 0
```

### Working Rule

**1. For a 3×3 matrix.** If A is a square matrix of order 3,

```
        ┌ a11  a12  a13 ┐
A   =   │ a21  a22  a23 │
        └ a31  a32  a33 ┘
```

then its characteristic equation is |A − λI| = 0, i.e.,

```
λ^3 − S1 λ^2 + S2 λ − S3 = 0
```

where

- S1 = Sum of the main diagonal elements = a11 + a22 + a33
- S2 = Sum of the minors of the main diagonal elements

```
     | a22  a23 |   | a11  a13 |   | a11  a12 |
S2 = |          | + |          | + |          |
     | a32  a33 |   | a31  a33 |   | a21  a22 |
```

- S3 = Determinant of A = |A|

**2. For a 2×2 matrix.** If A is a square matrix of order 2, then its characteristic equation is |A − λI| = 0, i.e.,

```
λ^2 − S1 λ + S2 = 0
```

where

- S1 = Sum of the main diagonal elements = a11 + a22
- S2 = Determinant of A = |A|

### Note 11.1

1. To verify Cayley-Hamilton theorem, first find the characteristic equation for the given square matrix, next substitute λ = A, then check the result equals 0.
2. To find A⁻¹, first find the characteristic equation for the given square matrix, next substitute λ = A, then pre-multiply by A⁻¹ (using AA⁻¹ = I and A⁻¹I = A⁻¹).

## Worked Examples

### Example 11.1. Verify Cayley-Hamilton theorem for the matrix

```
        ┌  1  -1   2 ┐
A   =   │ -2   1   3 │
        └  3   2  -3 ┘
```

**Solution.** The characteristic equation of A is |A − λI| = 0, i.e., λ^3 − S1λ^2 + S2λ − S3 = 0

where S1 = Sum of the main diagonal elements, S2 = Sum of the minors of the main diagonal elements, S3 = Determinant of A = |A|.

```
∴ S1 = 1 + 1 + (−3) = −1

     | 1   3 |   | 1   2 |   | 1  -1 |
S2 = |       | + |       | + |       |
     | 2  -3 |   | 3  -3 |   |-2   1 |

   = (−3 − 6) + (−3 − 6) + (1 − 2) = −9 − 9 − 1 = −19

         | 1  -1   2 |
S3 = |A| = |-2   1   3 | = 1(−3 − 6) − (−1)(6 − 9) + 2(−4 − 3)
         | 3   2  -3 |

   = 1(−9) + 1(−3) + 2(−7) = −9 − 3 − 14 = −26
```

∴ The characteristic equation is λ^3 − (−1)λ^2 − 19λ − (−26) = 0, i.e., **λ^3 + λ^2 − 19λ + 26 = 0**

Cayley-Hamilton states that "every square matrix satisfies its own characteristic equation." So to verify this, we must prove

```
A^3 + A^2 − 19A + 26I = 0    (i.e., put λ = A)
```

Computing A² and A³:

```
        ┌  9   2  -7  ┐            ┌ -16  -21   45  ┐
A^2  =  │  5   9  -10 │    A^3  =  │ -43  -16   67  │
        └-10  -7   21 ┘            └  67   45  -104 ┘
```

Substituting:

```
                ┌ -16  -21   45  ┐   ┌  9   2  -7  ┐   ┌  1  -1   2 ┐   ┌ 1  0  0 ┐
A^3+A^2−19A+26I = │ -43  -16   67  │ + │  5   9  -10 │ − 19│ -2   1   3 │ + 26│ 0  1  0 │
                └  67   45  -104 ┘   └-10  -7   21 ┘   └  3   2  -3 ┘   └ 0  0  1 ┘

                ┌ 0  0  0 ┐
              = │ 0  0  0 │
                └ 0  0  0 ┘
```

Hence Cayley-Hamilton theorem is verified.

### Example 11.2. Verify Cayley-Hamilton theorem for A and hence find A⁻¹

```
        ┌  1   2  -2 ┐
A   =   │  2   5  -4 │
        └  3   7  -5 ┘
```

**Solution.** As before, S1 = 1 + 5 + (−5) = 1

```
     | 5  -4 |   | 1  -2 |   | 1   2 |
S2 = |       | + |       | + |       |  = (−25 − 28) + (−5 + 6) + (5 − 4) = 3 + 1 + 1 = 5
     | 7  -5 |   | 3  -5 |   | 2   5 |

         | 1   2  -2 |
S3 = |A| = | 2   5  -4 | = 1(−25 − 28) − (−2)(−10 + 12) + (−2)(14 − 15) = −53 + 4 + 2 = 1
         | 3   7  -5 |
```

∴ The characteristic equation is λ^3 − λ^2 + 5λ − 1 = 0, so we must prove **A^3 − A^2 + 5A − I = 0**.

```
        ┌ -1  -2   0  ┐            ┌ -5  -12  10 ┐
A^2  =  │  0   1  -4  │    A^3  =  │-10  -23  16 │
        └  2   6  -9  ┘            └-13  -29  17 ┘
```

```
A^3 − A^2 + 5A − I = ┌ -5 -12 10 ┐ − ┌ -1 -2  0 ┐ + 5┌ 1 2 -2 ┐ − ┌1 0 0┐ = ┌ 0 0 0 ┐
                     │-10 -23 16 │   │  0  1 -4 │    │ 2 5 -4 │   │0 1 0│   │ 0 0 0 │
                     └-13 -29 17 ┘   │  2  6 -9 │    │ 3 7 -5 │   │0 0 1│   └ 0 0 0 ┘
```

Hence Cayley-Hamilton theorem is verified.

To find A⁻¹, premultiply A^3 − A^2 + 5A − I = 0 by A⁻¹:

```
A⁻¹(A^3 − A^2 + 5A − I) = 0
⇒ A^2 − A + 5I − A⁻¹ = 0
⇒ A⁻¹ = A^2 − A + 5I
```

```
        ┌ -1  -2   0 ┐   ┌ 1   2  -2 ┐        ┌1 0 0┐   ┌  3  -4   2 ┐
A⁻¹ =   │  0   1  -4 │ − │ 2   5  -4 │ + 5    │0 1 0│ = │ -2   1   0 │
        └  2   6  -9 ┘   └ 3   7  -5 ┘        └0 0 1┘   └ -1  -1   1 ┘
```

### Example 11.3. Using Cayley-Hamilton theorem find the inverse of

```
        ┌ 3   3   4 ┐
A   =   │ 2  -3   4 │
        └ 0  -1   1 ┘
```

**Solution.** S1 = 3 + (−3) + 1 = 1

```
     | -3   4 |   | 3   4 |   | 3   3 |
S2 = |        | + |       | + |       |  = (−3 + 4) + (3 − 0) + (−9 − 6) = 1 + 3 − 15 = −11
     | -1   1 |   | 0   1 |   | 2  -3 |

         | 3   3   4 |
S3 = |A| = | 2  -3   4 | = 3(−3 + 4) − 3(2 − 0) + 4(−2 − 0) = 3 − 6 − 8 = −11
         | 0  -1   1 |
```

∴ The characteristic equation is λ^3 − λ^2 − 11λ + 11 = 0, so **A^3 − A^2 − 11A + 11I = 0**.

Premultiplying by A⁻¹:

```
A^2 − A − 11I + 11A⁻¹ = 0
⇒ 11A⁻¹ = −A^2 + A + 11I
⇒ A⁻¹ = −(1/11)(A^2 − A − 11I)
```

```
        ┌ 15  -4  28 ┐
A^2  =  │  0  11   0 │
        └ -2   2  -3 ┘
```

```
              ┌ 15  -4  28 ┐   ┌ 3   3   4 ┐        ┌1 0 0┐   ┌  1  -7  24 ┐
A^2 − A − 11I = │  0  11   0 │ − │ 2  -3   4 │ − 11  │0 1 0│ = │ -2   3  -4 │
              └ -2   2  -3 ┘   └ 0  -1   1 ┘        └0 0 1┘   └ -2   3 -15 ┘
```

```
              1  ┌  1  -7  24 ┐
∴ A⁻¹  =    −────│ -2   3  -4 │
             11  └ -2   3 -15 ┘
```

### Example 11.4. Using Cayley-Hamilton theorem, find A⁴, where

```
        ┌  2  -2   1 ┐
A   =   │  0   1   2 │
        └  1   0   1 ┘
```

**Solution.** S1 = 2 + 1 + 1 = 4

```
     | 1  2 |   | 2  1 |   | 2 -2 |
S2 = |      | + |      | + |      |  = (1 − 0) + (2 − 1) + (2 − 0) = 1 + 1 + 2 = 4
     | 0  1 |   | 1  1 |   | 0  1 |

         | 2  -2   1 |
S3 = |A| = | 0   1   2 | = 2(1 − 0) − (−2)(0 − 2) + 1(0 − 1) = 2 − 4 − 1 = −3
         | 1   0   1 |
```

∴ The characteristic equation is λ^3 − 4λ^2 + 4λ + 3 = 0, so **A^3 − 4A^2 + 4A + 3I = 0**.

To find A⁴, premultiply by A:

```
A(A^3 − 4A^2 + 4A + 3I) = 0
⇒ A^4 − 4A^3 + 4A^2 + 3A = 0
⇒ A^4 = 4A^3 − 4A^2 − 3A
```

```
        ┌  5  -6  -1 ┐            ┌  9  -16  -8 ┐
A^2  =  │  2   1   4 │    A^3  =  │  8   -3   8 │
        └  3  -2   2 ┘            └  8   -8   1 ┘
```

```
A^4 = 4┌ 9 -16 -8┐ − 4┌ 5 -6 -1┐ − 3┌ 2 -2  1┐ = ┌ 10 -34 -31┐
       │ 8  -3  8│    │ 2  1  4│    │ 0  1  2│   │ 24 -19  10│
       └ 8  -8  1┘    └ 3 -2  2┘    └ 1  0  1┘   └ 17 -24  -7┘
```

∴ **A⁴ = [[10, −34, −31], [24, −19, 10], [17, −24, −7]]**

## Mathematical Derivation

### Why substituting λ = A in the characteristic equation is not a trivial substitution

At first glance, "every matrix satisfies its own characteristic equation" can look like a tautology: the characteristic polynomial p(λ) = |A − λI| is built to vanish exactly at the eigenvalues of A, so it is tempting to think p(A) = 0 just because "p(λ) = 0 for λ = each eigenvalue." This reasoning is invalid — p(λ) = 0 is a *scalar* equation true only for the specific scalar values λ = λ_1, ..., λ_n (the eigenvalues), whereas p(A) = 0 is a *matrix* equation, and A itself is not a scalar. The theorem is a genuine, separate fact: it says the polynomial expression built from powers of the matrix A, using the same coefficients as the characteristic polynomial, produces the zero matrix — not merely that A shares its eigenvalues with the roots of p(λ).

### Derivation via the adjugate (classical proof, matches the working rule above)

For any square matrix M, the adjugate (matrix of cofactors, transposed) satisfies the identity

```
adj(M) · M = |M| · I
```

Apply this with M = A − λI, treating λ as a formal variable:

```
adj(A − λI) · (A − λI) = |A − λI| · I = p(λ) · I
```

The entries of adj(A − λI) are (n−1)×(n−1) cofactors of A − λI, each a polynomial in λ of degree at most n − 1. So adj(A − λI) can be written as a matrix polynomial in λ:

```
adj(A − λI) = B_(n−1)λ^(n−1) + B_(n−2)λ^(n−2) + ... + B_1λ + B_0
```

where each B_i is a fixed n×n matrix (independent of λ) built from the entries of A. Substituting this into the identity above and expanding both sides as polynomials in λ, then matching the coefficient matrices of each power λ^k on the left and right sides, gives a chain of matrix equations relating the B_i's to A and to the scalar coefficients c_i of p(λ) = (−1)^n λ^n + c_(n−1)λ^(n−1) + ... + c_0. Multiplying the k-th equation by A^k and summing all the resulting equations causes every B_i term to cancel out telescopically (this is the key algebraic trick — each B_i appears once with a + sign from one equation and once with a − sign from the adjacent one), leaving exactly

```
(−1)^n A^n + c_(n−1)A^(n−1) + ... + c_1 A + c_0 I = 0
```

which is p(A) = 0, the Cayley-Hamilton theorem. This is why, mechanically, "find the characteristic equation, then substitute λ = A" (Note 11.1) always works: the substitution is legitimate precisely because of this cancellation, not because of a naive scalar-to-matrix analogy.

### Why S1, S2, S3 take the trace / sum-of-principal-minors / determinant form

Expanding |A − λI| for a 3×3 matrix directly by cofactor expansion along the first row and collecting terms by power of λ shows that:

- The coefficient of λ^2 collects exactly one diagonal entry from each of the three 2×2 minors used in the expansion, and summing them reproduces a_11 + a_22 + a_33 — the trace, S1.
- The coefficient of λ^1 collects the three 2×2 principal minors of A (the determinants obtained by deleting one row and the corresponding column through a diagonal position), giving S2.
- The constant term (λ = 0) is simply |A − 0·I| = |A|, giving S3.

This is the same trace/minor/determinant pattern used for eigenvalues in Unit 10 (sum of eigenvalues = trace, product of eigenvalues = determinant), because the roots of |A − λI| = 0 are exactly the eigenvalues — the characteristic equation is shared between the two units, only the *use* of it differs (Unit 10 solves it for λ, Unit 11 substitutes λ = A).

### Why premultiplying by A⁻¹ isolates A⁻¹ (Note 11.1, part 2)

Once p(A) = (−1)^n A^n + ... + c_1 A + c_0 I = 0 is established, every term contains a positive power of A except the constant term c_0 I. Premultiplying the entire equation by A⁻¹ (which exists whenever c_0 = ±|A| ≠ 0, i.e., whenever A is nonsingular) reduces every A^k to A^(k−1) via A⁻¹A^k = A^(k−1), while the constant term becomes c_0 A⁻¹. Solving the resulting equation for A⁻¹ expresses the inverse purely in terms of nonnegative powers of A (up to A^(n−1)) — avoiding cofactor/adjugate computation entirely. This is exactly the manipulation carried out in Examples 11.2 and 11.3 above.

## Historical Context

- **Arthur Cayley** first stated the result in his 1858 paper *A Memoir on the Theory of Matrices* (Philosophical Transactions of the Royal Society), where he announced that every square matrix satisfies its own characteristic equation. Cayley explicitly verified the claim for 2×2 matrices and checked it in several 3×3 examples, but did not give a general proof for arbitrary order n.
- **William Rowan Hamilton**, working independently and earlier in a different setting, had proved a closely related result in 1853 for quaternions (his own 4-dimensional number system, introduced in 1843): a quaternion satisfies a quadratic equation with real coefficients analogous to a characteristic equation. Because quaternions correspond to a special class of real 4×4 (or complex 2×2) matrices, Hamilton's quaternion result is viewed as the special case that anticipated Cayley's matrix statement, which is why both names are attached to the theorem even though Hamilton did not work with matrices in general.
- The theorem remained unproven in general (for arbitrary n×n matrices) for two decades after Cayley's announcement. **Ferdinand Georg Frobenius** supplied the first complete, general proof in 1878, using the adjugate-matrix argument summarized in the derivation above.
- The name "Cayley-Hamilton theorem" and its modern statement (over any commutative ring, not just real/complex numbers) reflect this layered history: Hamilton's 1853 special case, Cayley's 1858 general announcement with partial verification, and Frobenius's 1878 general proof.

Sources: [Cayley–Hamilton theorem, Wikipedia](https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem); [Arthur Cayley, Wikipedia](https://en.wikipedia.org/wiki/Arthur_Cayley); [Ferdinand Georg Frobenius, Wikipedia](https://en.wikipedia.org/wiki/Ferdinand_Georg_Frobenius); [Who, between Cayley and Hamilton, first worked on the theorem — History of Science and Mathematics Stack Exchange](https://hsm.stackexchange.com/questions/14349/who-between-cayley-and-hamilton-first-worked-on-the-theorem-that-bears-their-n/14365).

## Practical Applications

1. **Computing matrix inverses without cofactor expansion** — as shown in Examples 11.2 and 11.3, Cayley-Hamilton reduces A⁻¹ to a short polynomial in A itself (up to A^(n−1)), which is computationally cheaper than the full adjugate/cofactor method for larger matrices and is used in symbolic and numerical linear algebra software.

2. **Efficient computation of high matrix powers** — as in Example 11.4, any power A^k (for k ≥ n) can be rewritten as a linear combination of I, A, A^2, ..., A^(n−1) using the characteristic equation, which is far cheaper than repeated matrix multiplication and is used in fast algorithms for matrix exponentiation (e.g., for Fibonacci-type recurrences and Markov chain analysis).

3. **Control theory and state-space systems** — the theorem is used to simplify the computation of the state-transition matrix e^(At) (via the Cayley-Hamilton-based resolvent method) in linear time-invariant control systems, reducing an infinite matrix exponential series to a finite polynomial in A.

4. **Cryptography and coding theory** — Cayley-Hamilton-based matrix polynomial identities are used to construct and analyze linear recurring sequences and linear feedback shift registers, which underlie stream ciphers and error-correcting codes.

5. **Physics and quantum mechanics** — for low-dimensional operators (e.g., 2×2 or 3×3, as with Pauli or angular-momentum matrices), the theorem gives closed-form expressions for functions of an operator (such as exponentials used in time evolution) directly in terms of the operator and the identity, avoiding infinite series.

6. **Graph theory** — the characteristic polynomial of a graph's adjacency matrix, combined with Cayley-Hamilton, is used to relate powers of the adjacency matrix (which count walks of a given length between vertices) to lower powers, supporting algorithms that count paths and analyze network connectivity.

## References

**Chapter 2:** Section 6.1 to 6.3
