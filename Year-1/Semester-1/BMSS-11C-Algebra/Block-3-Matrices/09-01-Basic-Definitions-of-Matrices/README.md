# Unit 9: Basic Definition of Matrices and Their Properties

**Block:** III — Matrices
**Course:** BMSS-11C — Algebra

## Objectives

After completion of this unit, students will be able to:
- classify the different types of matrices.
- understand the properties of matrices.

## Table of Contents

- [9.1 Basic Definitions](#91-basic-definitions)
- [Mathematical Derivation](#mathematical-derivation)
- [Historical Context](#historical-context)
- [Practical Applications](#practical-applications)

## 9.1 Basic Definitions

### Definition 9.1. Symmetric Matrix

A square matrix which is unchanged by transposition is called a **symmetric matrix**, i.e., a square matrix A is said to be symmetric if

```
a_ij = a_ji   for all i and j    [i.e., A = A^T]
```

**For example:**

```
        ┌ a  h  g ┐
A   =   │ h  b  f │
        └ g  f  c ┘
```

### Definition 9.2. Skew-Symmetric Matrix

A square matrix A is said to be **skew-symmetric** if

```
a_ij = -a_ji   for all i and j    [i.e., A = -A^T]
```

**For example:**

```
        ┌  0   h  -c ┐
A   =   │ -h   0   a │
        └  c  -a   0 ┘
```

Note that this forces every diagonal entry to be zero, since a_ii = -a_ii ⟹ a_ii = 0.

### Definition 9.3. Hermitian Matrix

A square matrix A is said to be **Hermitian** if

```
a_ij = a̅_ji   for all i and j    [i.e., A = A̅^T]
```

where a̅_ji denotes the complex conjugate of a_ji.

**For example:**

```
        ┌   2      2+3i    2-i  ┐
A   =   │  2-3i     4      3+i  │
        └  2+i     3-i      6   ┘
```

Every diagonal entry of a Hermitian matrix must be real, since a_ii = a̅_ii forces a_ii to equal its own conjugate.

### Definition 9.4. Skew-Hermitian Matrix

A square matrix A is said to be **Skew-Hermitian** if

```
a_ij = -a̅_ji   for all i and j    [i.e., A = -A̅^T]
```

**For example:**

```
        ┌   2i     2+3i    2-i  ┐
A   =   │  2+3i     0      3-i  │
        └   2-i    -3-i    -6i  ┘
```

Every diagonal entry of a skew-Hermitian matrix must be purely imaginary (or zero), since a_ii = -a̅_ii forces a_ii to be its own negative conjugate.

### Definition 9.5. Orthogonal Matrix

A square matrix A is said to be **orthogonal** if

```
A A^T = I     (or equivalently)     A^T = A^-1
```

### Definition 9.6. Unitary Matrix

A square matrix is said to be **unitary** if

```
A A̅^T = I
```

### Note 9.1

```
A^T   is the Transpose of A
A̅^T   is the conjugate of the transpose of A (the conjugate transpose)
```

Definitions 9.5 and 9.6 are the real and complex analogues of the same idea: an orthogonal matrix uses the plain transpose, a unitary matrix uses the conjugate transpose, and the two coincide whenever A is real.

## Mathematical Derivation

### Why the boxed conditions are equivalent to the matrix equations

**Symmetric / skew-symmetric.** Writing A^T for the transpose, entry (i, j) of A^T equals a_ji. So A = A^T means a_ij = a_ji for every i, j — Definition 9.1 restated entrywise. Likewise A = -A^T means a_ij = -a_ji entrywise, which is Definition 9.2.

**Hermitian / skew-Hermitian.** Writing A̅^T for the conjugate transpose, entry (i, j) of A̅^T equals a̅_ji. So A = A̅^T means a_ij = a̅_ji entrywise (Definition 9.3), and A = -A̅^T means a_ij = -a̅_ji entrywise (Definition 9.4). A real symmetric matrix is automatically Hermitian, since a̅_ji = a_ji when every entry is real.

**Orthogonal ⟺ A^T = A⁻¹.** Starting from A A^T = I, multiply both sides on the left by A⁻¹ (which exists because det(A) ≠ 0, as det(A)·det(A^T) = det(I) = 1 rules out det(A) = 0):

```
A⁻¹(A A^T) = A⁻¹ I
(A⁻¹A) A^T = A⁻¹
       A^T = A⁻¹
```

so the two forms of Definition 9.5 are the same statement.

### Every square matrix splits into symmetric + skew-symmetric parts

For any square matrix A, define

```
S = (1/2)(A + A^T)      K = (1/2)(A - A^T)
```

Then S^T = (1/2)(A^T + A) = S, so S is symmetric, and K^T = (1/2)(A^T - A) = -K, so K is skew-symmetric. Adding them back:

```
S + K = (1/2)(A + A^T) + (1/2)(A - A^T) = A
```

so **A = S + K** — every square matrix is uniquely the sum of a symmetric and a skew-symmetric matrix. The complex analogue holds with the conjugate transpose:

```
A = (1/2)(A + A̅^T) + (1/2)(A - A̅^T) = Hermitian part + Skew-Hermitian part
```

### Orthogonal and unitary matrices preserve length

If A is orthogonal and x is a real column vector, then

```
‖Ax‖² = (Ax)^T(Ax) = x^T A^T A x = x^T (A^T A) x = x^T I x = x^T x = ‖x‖²
```

so multiplying by an orthogonal matrix never changes the length of a vector — it only rotates or reflects it. The identical argument with A̅^T in place of A^T shows a unitary matrix preserves length for complex vectors under the Hermitian inner product.

## Historical Context

- **Symmetric and skew-symmetric matrices** appear implicitly in the study of quadratic forms going back to **Lagrange (1736–1813)** and **Gauss (1777–1855)**, but the matrix formalism itself is due to **Arthur Cayley**, who introduced matrix algebra — including transposition and matrix multiplication — in *A Memoir on the Theory of Matrices* (1858).
- **Hermitian matrices** are named after the French mathematician **Charles Hermite (1822–1901)**, who studied self-adjoint bilinear and quadratic forms with complex coefficients in the 1850s, showing that such forms always have real eigenvalues — the property that later made Hermitian operators central to quantum mechanics.
- **Orthogonal matrices** grew out of 19th-century work on rotations and coordinate transformations in geometry and mechanics; **Euler's** studies of rigid-body rotation (1770s) already used what are now recognized as orthogonal transformations, later formalized within Cayley's matrix framework.
- **Unitary matrices** were introduced by the French mathematician **Léon Autonne (1859–1916)**, who defined them in *Sur l'hermitien* (1901) as the complex generalization of orthogonal matrices; the term and concept became central to physics once **John von Neumann's** formulation of quantum mechanics (1930s) used unitary operators to describe the time evolution of quantum states.

## Practical Applications

1. **Quantum mechanics** — physical observables (position, momentum, energy) are represented by Hermitian operators because Hermitian matrices always have real eigenvalues, matching the requirement that measured quantities be real numbers. Time evolution of a quantum state is governed by a unitary operator, which preserves total probability (the norm of the state vector).

2. **Computer graphics and robotics** — rotation and reflection matrices used to orient 3D objects and camera views are orthogonal matrices; because they preserve length and angle, applying them repeatedly (e.g., in animation or robot arm kinematics) doesn't distort the model.

3. **Structural and civil engineering** — stiffness and mass matrices in finite-element analysis of bridges and buildings are symmetric, which guarantees real eigenvalues (natural vibration frequencies) and simplifies the numerical solvers used to compute them.

4. **Signal processing** — the Discrete Fourier Transform matrix is unitary (up to a scale factor), which is why transforming a signal to the frequency domain and back preserves signal energy (Parseval's theorem).

5. **Statistics and data science** — covariance and correlation matrices are always symmetric (and positive semi-definite), which is exploited by Principal Component Analysis to decompose the matrix into orthogonal eigenvectors representing uncorrelated directions of variance.

6. **Numerical linear algebra** — QR decomposition factors a matrix into an orthogonal matrix Q and an upper-triangular matrix R; because orthogonal matrices don't amplify rounding error, this is the standard stable method for solving least-squares problems and computing eigenvalues.

7. **Cryptography** — orthogonal and unitary transformations are used in lattice-based and code-based cryptographic schemes because they preserve distances/norms, letting error-correction and hardness assumptions carry over exactly after the transformation.

8. **Control systems** — the symmetric Hermitian solution of the algebraic Riccati equation determines the optimal feedback gain in Linear-Quadratic-Regulator (LQR) design, used in aircraft autopilots and industrial process control.

