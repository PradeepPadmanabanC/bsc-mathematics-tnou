
# Unit 9: Basic Definition of Matrices and Their Properties

**Block:** III — Matrices
**Course:** BMSS-11C — Algebra

## Objectives

After completion of this unit, students will be able to:
- prove the standard properties of symmetric, skew-symmetric, Hermitian, and skew-Hermitian matrices built from a square matrix A.
- express any square matrix as a sum of a symmetric and a skew-symmetric matrix, and as a sum of a Hermitian and a skew-Hermitian matrix.
- apply the decomposition to solve concrete numeric problems.

## Table of Contents

- [9.2 Properties and Problems on Symmetric and Hermitian Matrices](#92-properties-and-problems-on-symmetric-and-hermitian-matrices)
- [Mathematical Derivation](#mathematical-derivation)
- [Historical Context](#historical-context)
- [Practical Applications](#practical-applications)

## 9.2 Properties and Problems on Symmetric and Hermitian Matrices

### Example 9.8. If A is a square matrix of order n, then A + A^T is symmetric and A − A^T is skew-symmetric

**Proof.** It is enough to prove

```
┌ (A + A^T)^T = A + A^T ┐   and   ┌ (A − A^T)^T = −(A − A^T) ┐
```

Now (A + A^T)^T = A^T + (A^T)^T = A^T + A, or A + A^T. i.e. (A + A^T)^T = A + A^T, so A + A^T is symmetric.

Now (A − A^T)^T = A^T − (A^T)^T = A^T − A, or −(A − A^T). i.e. (A − A^T)^T = −(A − A^T), so A − A^T is skew-symmetric. ∎

### Example 9.9. If A is a square matrix of order n, then A + A̅^T is Hermitian and A − A̅^T is skew-Hermitian

**Proof.** It is enough to prove

```
┌ (A + A̅^T)^T = A + A̅^T ┐   and   ┌ (A − A̅^T)^T = −(A − A̅^T) ┐
```

Now (A + A̅^T)‾^T = (A̅ + (A̅^T)‾)^T = (A̅ + A^T)^T = A̅^T + A, or A + A̅^T.

i.e., (A + A̅^T)‾^T = A + A̅^T ∴ A + A̅^T is Hermitian.

Now (A − A̅^T)‾^T = (A̅ − (A̅^T)‾)^T = (A̅ − A^T)^T = A̅^T − A = −(A − A̅^T)

i.e. (A − A̅^T)‾^T = −(A − A̅^T) ∴ A − A̅^T is skew-Hermitian. ∎

### Example 9.10. Every square matrix can be uniquely expressed as a sum of a symmetric matrix and a skew-symmetric matrix

**Proof.** Let A be a square matrix. Then by a theorem, if A is a square matrix of order n, then A + A^T is symmetric and A − A^T is skew-symmetric. Hence

```
┌ A = (1/2)(A + A^T) + (1/2)(A − A^T) ┐
```

Thus we have expressed A as the sum of a symmetric and a skew-symmetric matrix. ∎

### Example 9.11. Every square matrix can be uniquely expressed as a sum of a Hermitian matrix and a skew-Hermitian matrix

**Proof.** Let A be a square matrix. Then by a theorem, if A is a square matrix of order n, then A + A̅^T is Hermitian and A − A̅^T is skew-Hermitian. Hence

```
┌ A = (1/2)(A + A̅^T) + (1/2)(A − A̅^T) ┐
```

Thus we have expressed A as the sum of a Hermitian and a skew-Hermitian matrix. ∎

## Mathematical Derivation

### Why the same argument carries over to the conjugate transpose

Hermitian and skew-Hermitian matrices replace the transpose with the conjugate transpose, A̅^T. Conjugation and transposition each reverse under repeated application — (A̅^T)‾^T = A — so the identical two-line argument above goes through with A̅^T in place of A^T: A + A̅^T is unchanged under conjugate-transposition (Hermitian), and A − A̅^T negates under conjugate-transposition (skew-Hermitian).

### Why the symmetric/skew-symmetric decomposition is unique

Suppose A = S + K = S' + K' are two decompositions with S, S' symmetric and K, K' skew-symmetric. Then S − S' = K' − K. The left side is symmetric (a difference of symmetric matrices is symmetric) and the right side is skew-symmetric (a difference of skew-symmetric matrices is skew-symmetric). A matrix that is both symmetric and skew-symmetric must equal its own negative transpose and its own transpose at once, forcing every entry to be zero. Hence S = S' and K = K', so the decomposition A = (1/2)(A + A^T) + (1/2)(A − A^T) is the only one possible. The identical argument, with A̅^T in place of A^T, proves the Hermitian/skew-Hermitian decomposition is unique as well.

## Historical Context

- The decomposition of a square matrix into symmetric and skew-symmetric parts follows directly from **Arthur Cayley's** 1858 matrix algebra (*A Memoir on the Theory of Matrices*), once addition, scalar multiplication, and transposition of matrices were formally defined — the same source credited for symmetric and skew-symmetric matrices in Unit 9.1. The decomposition itself is known as the **Toeplitz decomposition**, after the German mathematician **Otto Toeplitz (1881–1940)**.
- The Hermitian analogue rests on **Charles Hermite's** 1855 work on self-adjoint bilinear and quadratic forms with complex coefficients, which established the conjugate-transpose condition a_ij = a̅_ji as the natural complex counterpart of symmetry and showed that matrices satisfying it always have real eigenvalues.
- The broader technique of splitting an operator into a "self-adjoint part" and an "anti-self-adjoint part" (of which the symmetric/skew-symmetric and Hermitian/skew-Hermitian decompositions are the finite-dimensional matrix case) became a standard tool in functional analysis in the early 20th century, notably in **David Hilbert's** work on integral equations and operator theory (1904–1910), which later fed into the operator formalism of quantum mechanics.

## Practical Applications

1. **Mechanics and elasticity** — the velocity gradient tensor of a fluid or the displacement gradient of a deformed solid is routinely split into a symmetric part (the strain-rate/strain tensor, describing stretching) and a skew-symmetric part (the vorticity/rotation tensor, describing local rotation), using exactly the A = S + K decomposition proved here.

2. **Quantum mechanics** — any operator representing a physical process can be written as a Hermitian part plus a skew-Hermitian part; the Hermitian part corresponds to observable, energy-conserving behavior while the skew-Hermitian part accounts for decay or gain (e.g., in open quantum systems and non-Hermitian effective Hamiltonians).

3. **Graph theory and network analysis** — the adjacency matrix of a directed graph splits into a symmetric part, which captures the underlying undirected (mutual) connections, and a skew-symmetric part, which captures the net directional flow between nodes.

4. **Numerical optimization** — the Hessian or Jacobian of a general (non-symmetric) system is split into symmetric and skew-symmetric parts to separate curvature information (used by Newton-type solvers) from rotational/circulatory components, which affects the choice and stability of iterative solvers.

5. **Signal and image processing** — decomposing a general transformation matrix into symmetric and skew-symmetric parts separates scaling/shearing effects from pure rotation effects, which is used in image registration and motion-analysis algorithms.

## References

**Chapter 2:** Section 9.2

</content>
