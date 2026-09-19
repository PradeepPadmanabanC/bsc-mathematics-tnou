
# Unit 9: Basic Definition of Matrices and Their Properties

**Block:** III — Matrices
**Course:** BMSS-11C — Algebra

## Objectives

After completion of this unit, students will be able to:
- prove the standard algebraic properties of orthogonal matrices.
- recognize that these properties together show the orthogonal matrices of a given order form a group under matrix multiplication.

## Table of Contents

- [9.3 Properties of Orthogonal Matrix](#93-properties-of-orthogonal-matrix)
- [Mathematical Derivation](#mathematical-derivation)
- [Historical Context](#historical-context)
- [Practical Applications](#practical-applications)

## 9.3 Properties of Orthogonal Matrix

### (1) Every orthogonal matrix commutes with its transpose, i.e., P^T P = P P^T

**Proof.** If the matrix P is orthogonal, then P^T = P^-1

```
∴  P P^T = P P^-1 = I    (by premultiply with P)
```

Also

```
P^T P = P^-1 P = I
```

```
∴  P^T P = P P^T.
```
∎

### (2) Product of two orthogonal matrices is orthogonal

**Proof.** Let P and Q be two orthogonal matrices.

```
∴  P^T = P^-1  and  Q^T = Q^-1
```

```
∴  P^T Q^T = P^-1 Q^-1
```

```
i.e.,  (QP)^T = (QP)^-1
```
∎

### (3) The inverse of an orthogonal matrix is orthogonal

**Proof.** Let P be an orthogonal matrix.

```
∴  P^-1 = P^T
```

```
Hence  (P^-1)^-1 = (P^T)^-1 = (P^-1)^T
```

```
Hence P^-1 is orthogonal.
```
∎

## Mathematical Derivation

### Why (QP)^T = P^T Q^T justifies calling the product orthogonal

Property (2) hinges on the transpose-reversal rule for a product of two matrices: (QP)^T = P^T Q^T, not Q^T P^T. Substituting the orthogonality of P and Q, (QP)^T = P^-1 Q^-1. Because matrix inverses also reverse order under a product, (QP)^-1 = P^-1 Q^-1 as well. Both expressions equal P^-1 Q^-1, so (QP)^T = (QP)^-1, which is exactly the defining condition for QP to be orthogonal. The same argument, applied repeatedly, shows any finite product of orthogonal matrices of the same order is orthogonal.

### Why these three properties together mean orthogonal matrices form a group

A set of matrices forms a group under multiplication when it contains the identity, is closed under multiplication, and is closed under taking inverses (associativity is automatic, since matrix multiplication is always associative). The identity matrix I is trivially orthogonal (I^T I = I = I I^T). Property (2) supplies closure under multiplication, and property (3) supplies closure under inverses. Property (1) is not a group axiom but a useful structural fact: it says every orthogonal matrix is a **normal matrix** (it commutes with its own transpose), which is what guarantees an orthogonal matrix can always be diagonalized over the complex numbers with an orthonormal eigenbasis. Together, (1)-(3) establish that the n×n orthogonal matrices form what is known as the **orthogonal group**, denoted O(n).

## Historical Context

- The transpose and inverse notation used in these proofs comes from **Arthur Cayley's** 1858 matrix algebra (*A Memoir on the Theory of Matrices*), the same formalism credited for the symmetric, skew-symmetric, Hermitian, and skew-Hermitian matrices covered in Units 9.1 and 9.2.
- Orthogonal transformations predate the matrix notation: **Leonhard Euler's** 1770s study of rigid-body rotations already used what would now be recognized as orthogonal transformations (Euler's rotation theorem, 1775), and **Augustin-Louis Cauchy** used orthogonal substitutions in his 1829 work on the principal axes of quadratic forms.
- The recognition that the orthogonal matrices of a fixed order form a group under multiplication — precisely the content of properties (2) and (3) above — falls under the broader 19th-century development of group theory. The abstract notion of a "group" was formalized by **Arthur Cayley** in his 1854 paper *On the Theory of Groups, as Depending on the Symbolic Equation θⁿ = 1*, and continuous matrix groups such as the orthogonal group were subsequently studied as **Lie groups**, following **Sophus Lie's** work on continuous transformation groups in the 1870s-1890s.

## Practical Applications

1. **Computer graphics and robotics** — because orthogonal matrices are closed under multiplication (property 2), chaining any number of rotation/reflection matrices to orient a 3D object or a robot arm always yields another orthogonal matrix, so repeated transformations never introduce scaling or shear distortion.

2. **Numerical linear algebra** — QR decomposition and the Gram-Schmidt process rely on orthogonal matrices; because the inverse of an orthogonal matrix is just its transpose (property 3), solving a linear system once it is factored through an orthogonal matrix avoids the more expensive and less stable general matrix inversion.

3. **Signal processing** — the Discrete Cosine Transform and Discrete Fourier Transform matrices are orthogonal (up to scaling); reversing the transform is done by applying the transpose rather than computing a separate inverse, which is exploited for fast, numerically stable implementations.

4. **Physics and crystallography** — the symmetry operations of a rigid body or a crystal lattice (rotations and reflections) are represented by orthogonal matrices; property (2) guarantees that composing two symmetry operations of a crystal always yields another valid symmetry operation, which is the basis for classifying crystallographic point groups.

5. **Control systems and state estimation** — orthogonal (rotation) matrices are used to represent coordinate frame changes in navigation and the Kalman filter; commuting with their transpose (property 1) keeps these matrices normal, which simplifies eigenvalue-based stability analysis of the transformed system.

