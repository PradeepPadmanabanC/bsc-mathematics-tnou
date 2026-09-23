
# Unit 12: Diagonalisation of a Matrix

**Block:** III — Matrices
**Course:** BMSS-11C — Algebra

## Objectives

After completion of this unit, students will be able to:
- diagonalise the given matrix.

## Table of Contents

- [12.1 Diagonalisation of a Matrix](#121-diagonalisation-of-a-matrix)
- [Mathematical Derivation](#mathematical-derivation)
- [Historical Context](#historical-context)
- [Practical Applications](#practical-applications)

## 12.1 Diagonalisation of a Matrix

Procedure for diagonalisation of a matrix is as follows:

1. Find the characteristic equation of a given matrix A and then find the eigen values of the matrix A.
2. Find the eigen vectors of A and form the matrix B whose columns are the eigen vectors of A.
3. Find B⁻¹.
4. Finally, find B⁻¹AB, which is the diagonal matrix whose diagonal elements are the eigen values of A.

### Note 12.1

If the eigen values of the matrix A are distinct, then only we can diagonalise the matrix.

### Example 12.1. Diagonalise the matrix

```
        ┌  2  -2   3 ┐
A   =   │  1   1   1 │
        └  1   3  -1 ┘
```

**Solution.** The characteristic equation of A is |A − λI| = 0, i.e.,

```
λ^3 − S1 λ^2 + S2 λ − S3 = 0
```

Here S1 = Sum of the main diagonal elements = 2 + 1 + (−1) = 2

```
     | 1   1 |   | 2   3 |   | 2  -2 |
S2 = |       | + |       | + |       |  = (−1 − 3) + (−2 − 3) + (2 + 2) = −4 − 5 + 4 = −5
     | 3  -1 |   | 1  -1 |   | 1   1 |

         | 2  -2   3 |
S3 = |A| = | 1   1   1 | = 2(−1 − 3) − (−2)(−1 − 1) + 3(3 − 1) = −8 − 4 + 6 = −6
         | 1   3  -1 |
```

∴ The characteristic equation is **λ^3 − 2λ^2 − 5λ + 6 = 0**

Now, we can find the eigen values. When λ = 1, f(λ) = 1 − 2 − 5 + 6 = 0. Thus, λ = 1 is one of the roots.

Dividing λ^3 − 2λ^2 − 5λ + 6 by (λ − 1):

```
λ^3 − 2λ^2 − 5λ + 6 = 0
(λ − 1)(λ^2 − λ − 6) = 0
⇒ (λ − 1)(λ − 3)(λ + 2) = 0
```

Hence, the eigen values are **1, −2, 3**.

Now, we find the eigen vectors from (A − λI)X = 0:

```
┌ 1 − λ    -2       3    ┐ ┌ x1 ┐
│   1    1 − λ      1    │ │ x2 │ = 0
└   1      3     -1 − λ  ┘ └ x3 ┘
```

**Case 1: λ = 1.** The equation becomes

```
┌  0  -2   3 ┐ ┌ x1 ┐
│  1   0   1 │ │ x2 │ = 0
└  1   3  -2 ┘ └ x3 ┘

x1 − 2x2 + 3x3 = 0
x1 + 0x2 + x3   = 0
x1 + 3x2 − 2x3  = 0
```

By taking the first two equations and solving by the method of cross multiplication:

```
     x1        x2        x3
 -2      3   1      -2
    ╲  ╱   ╲  ╱   ╲  ╱
    ╱  ╲   ╱  ╲   ╱  ╲
  0      1   1      0

x1/(−2·1 − 3·0) = x2/(3·1 − 1·1) = x3/(0·0 − 1·1)

⇒ x1/(−2) = x2/2 = x3/2
⇒ x1/(−1) = x2/1 = x3/1
```

The eigen vector corresponding to λ = 1 is

```
┌ -1 ┐
│  1 │
└  1 ┘
```

**Case 2: λ = −2.** The eigen vector corresponding to λ = −2 is

```
┌ 11 ┐
│  1 │
└-14 ┘
```

**Case 3: λ = 3.** The eigen vector corresponding to λ = 3 is

```
┌ 1 ┐
│ 1 │
└ 1 ┘
```

Hence the new matrix B, whose columns are the eigen vectors, is

```
        ┌ -1  11   1 ┐
B   =   │  1   1   1 │
        └  1 -14   1 ┘
```

```
B⁻¹  =  1/|B| · Adj(B)  =  −1/30 ┌  15  -25   10 ┐   =  1/30 ┌ -15   25  -10 ┐
                                 │   0    2   -2 │           │   0    2   -2 │
                                 └ -15   -3  -12 ┘           └  15    3   12 ┘
```

Diagonal matrix D = B⁻¹AB:

```
     1  ┌ -15   25  -10 ┐ ┌  2  -2   3 ┐ ┌ -1  11   1 ┐
D = ── │   0    2   -2 │ │  1   1   1 │ │  1   1   1 │
    30  └  15    3   12 ┘ └  1   3  -1 ┘ └  1 -14   1 ┘

        ┌ 1  0  0 ┐
    =   │ 0 -2  0 │
        └ 0  0  3 ┘
```

Here the diagonal elements are the eigen values of A.

## Mathematical Derivation

### Why B⁻¹AB is diagonal when the columns of B are eigen vectors

Let B be the matrix whose columns are eigen vectors v₁, v₂, ..., vₙ of A, corresponding respectively to eigen values λ₁, λ₂, ..., λₙ. By definition of an eigen vector, Avᵢ = λᵢvᵢ for each i. Writing this one column at a time,

```
AB = A[v1 | v2 | ... | vn] = [Av1 | Av2 | ... | Avn] = [λ1v1 | λ2v2 | ... | λnvn]
```

The right-hand side is exactly B multiplied on the right by the diagonal matrix D = diag(λ₁, λ₂, ..., λₙ), because multiplying a matrix on the right by a diagonal matrix scales each column by the corresponding diagonal entry:

```
AB = BD
```

Provided B is invertible (which requires its columns — the eigen vectors — to be linearly independent, Note 12.1), pre-multiplying both sides by B⁻¹ gives

```
B⁻¹AB = D
```

which is precisely the diagonal matrix of eigen values, confirming step 4 of the procedure.

### Why distinct eigen values are sufficient for B to be invertible

B is invertible exactly when its columns (the eigen vectors) are linearly independent. Suppose λ₁, λ₂, ..., λₙ are distinct and, for contradiction, that some nontrivial linear combination c₁v₁ + c₂v₂ + ... + cₖvₖ = 0 holds among a minimal dependent subset of the eigen vectors (k as small as possible, all cᵢ ≠ 0). Applying (A − λₖI) to both sides and using (A − λₖI)vᵢ = (λᵢ − λₖ)vᵢ eliminates the vₖ term entirely (since λₖ − λₖ = 0), leaving a shorter nontrivial dependency c₁(λ₁ − λₖ)v₁ + ... + c_{k-1}(λ_{k-1} − λₖ)v_{k-1} = 0 among fewer eigen vectors — each coefficient cᵢ(λᵢ − λₖ) is still nonzero because the λᵢ are distinct. This contradicts the minimality of k. Hence no such dependency can exist: eigen vectors corresponding to distinct eigen values are always linearly independent, so B is invertible and A is diagonalisable. (Note 12.1 states this as a sufficient condition; when eigen values repeat, independent eigen vectors may or may not exist, so diagonalisability is not guaranteed.)

## Historical Context

- The general algebraic framework in which "diagonalising a matrix" is stated — matrices as objects in their own right, matrix multiplication, and the transformation A ↦ P⁻¹AP — was laid down by **Arthur Cayley** in his 1858 paper *A Memoir on the Theory of Matrices* (received by the Royal Society on 10 December 1857, read 14 January 1858), the same foundational memoir already cited in Unit 11 for the Cayley-Hamilton theorem.
- The first rigorous diagonalisation *theorem* — that every real symmetric matrix can be diagonalised (with real eigen values, by an orthogonal change of basis) — is due to **Augustin-Louis Cauchy**, who developed this as part of his broader work on what is now called the spectral theory of matrices in the 1820s–1840s; the historian Thomas Hawkins traces this development in detail in *"Cauchy and the Spectral Theory of Matrices"* (Historia Mathematica, vol. 2, 1975, pp. 1–29). This special case for symmetric matrices is what is known today as the (finite-dimensional) spectral theorem.
- A practical, iterative numerical method for diagonalising real symmetric matrices by hand was given by **Carl Gustav Jacob Jacobi** in 1846, in the context of computing eigenvalues arising from problems in celestial mechanics; a modernized version of his approach (the Jacobi eigenvalue algorithm) is still used today for diagonalising symmetric matrices on a computer.
- The general (non-symmetric) case, including the classification of matrices that fail to be diagonalisable and must instead be reduced to the next-best "almost diagonal" form, was completed later in the 19th century by **Camille Jordan**, whose Jordan normal form (1870) handles repeated eigen values that do not admit enough independent eigen vectors — precisely the situation excluded by Note 12.1 above.

Sources: [Spectral theorem, Wikipedia](https://en.wikipedia.org/wiki/Spectral_theorem); [Matrix similarity, Wikipedia](https://en.wikipedia.org/wiki/Matrix_similarity); [Jacobi eigenvalue algorithm, Wikipedia](https://en.wikipedia.org/wiki/Jacobi_eigenvalue_algorithm); [A Memoir on the Theory of Matrices, Philosophical Transactions of the Royal Society (1858)](https://royalsocietypublishing.org/doi/10.1098/rstl.1858.0002).

## Practical Applications

1. **Solving systems of linear differential equations** — a coupled system X' = AX decouples completely into n independent first-order equations yᵢ' = λᵢyᵢ once A is diagonalised via the substitution X = BY, letting each equation be solved separately as yᵢ = yᵢ(0)e^(λᵢt).

2. **Computing high powers of a matrix efficiently** — since A = BDB⁻¹ gives Aᵏ = BDᵏB⁻¹, and Dᵏ is just each eigen value raised to the power k, this avoids repeated matrix multiplication and is used to find closed-form solutions to linear recurrences (e.g., the Fibonacci sequence) and to analyze long-run behavior of Markov chains.

3. **Vibration and structural analysis** — diagonalising the system matrix of a coupled mechanical system (masses connected by springs, or a building's floors) transforms the coupled equations of motion into independent "normal modes," each vibrating at its own natural frequency (the eigen value).

4. **Principal Component Analysis (statistics)** — diagonalising a dataset's covariance matrix expresses the data in a new basis (the eigen vectors) where the diagonal entries (eigen values) directly give the variance along each new axis, letting high-dimensional data be reduced to its most informative directions.

5. **Quantum mechanics** — diagonalising the Hamiltonian matrix of a quantum system finds its allowed energy levels (the eigen values) and the corresponding stationary quantum states (the eigen vectors), which is the standard method for solving time-independent problems.

6. **Google's PageRank and network analysis** — diagonalising (or finding the dominant eigen vector of) a large adjacency-based matrix representing links between webpages or nodes in a network reveals long-run importance rankings and steady-state behavior of the network.

## References

**Chapter 2:** Section 16.3
