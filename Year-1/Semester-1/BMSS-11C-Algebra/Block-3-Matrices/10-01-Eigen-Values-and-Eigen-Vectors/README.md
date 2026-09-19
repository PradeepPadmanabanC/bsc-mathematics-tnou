
# Unit 10: Eigen Values and Eigen Vectors

**Block:** III — Matrices
**Course:** BMSS-11C — Algebra

## Objectives

After completion of this unit, students will be able to:
- understand the concept of eigen values and eigen vectors.
- know the properties of eigen values.

## Table of Contents

- [10.1 Eigen Values and Eigen Vectors](#101-eigen-values-and-eigen-vectors)
- [10.2 Properties of Eigen Values and Eigen Vectors](#102-properties-of-eigen-values-and-eigen-vectors)
- [Mathematical Derivation](#mathematical-derivation)
- [Historical Context](#historical-context)
- [Practical Applications](#practical-applications)

## 10.1 Eigen Values and Eigen Vectors

### Definition 10.1. Characteristic Polynomial

If A is a square matrix of order n and I is the identity matrix of the same order, then the expansion |A − λI| is said to be the **characteristic polynomial** of A.

### Definition 10.2. Characteristic Equation

If A is a square matrix of order n and I is the identity matrix of the same order, then the expansion |A − λI| = 0 is said to be the **characteristic equation** of A.

### Definition 10.3. Characteristic Roots

Eigen values are also called **characteristic roots** or **latent roots**. The roots of the characteristic equation are called the **eigen values** of A.

### Definition 10.4. Characteristic Vectors

Let A be a square matrix of order n. If there exists a nonzero vector X, to each eigen value λ satisfying the equation (A − λI)X = 0, X is called the **eigen vector** of A.

### Note 10.1

1. By solving the characteristic equation we get the eigen values.
2. For each and every eigen value, we get eigen vectors by solving the equation (A − λI)X = 0 where

```
        ┌ x1 ┐
        │ x2 │
X   =   │  .  │
        └ xn ┘
```

## 10.2 Properties of Eigen Values and Eigen Vectors

1. The sum of the eigen values of a matrix is equal to the sum of the main diagonal elements.
2. The product of the eigen values of a matrix is equal to the determinant of the matrix.
3. The square matrix A and its transpose A^T have the same eigen values.
4. The eigen values of a triangular matrix are just the elements of the main diagonal of the matrix.

### Example 10.1. Find the sum and product of the eigen values of the matrix

```
        ┌  2  -3 ┐
A   =   │  4  -2 │
        └        ┘
```

**Solution.**

Sum of the eigen values = Sum of the diagonal elements (by property 1)

```
= 2 + (−2) = 0
```

Product of the eigen values = |A| = (2)(−2) − (−3)(4) = −4 + 12 = 8

## Mathematical Derivation

### Why the eigen value equation forces det(A − λI) = 0

An eigen vector X of A is, by Definition 10.4, a nonzero vector satisfying AX = λX for some scalar λ. Rearranging,

```
AX − λX = 0
(A − λI)X = 0
```

This is a homogeneous linear system in X. A homogeneous system (A − λI)X = 0 has a nonzero solution X if and only if the matrix (A − λI) is singular, i.e., if and only if |A − λI| = 0. This is exactly the characteristic equation of Definition 10.2. Hence the eigen values of A are precisely the values of λ for which the characteristic equation holds, and once a particular eigen value λ is substituted back into (A − λI)X = 0, solving that (now singular) system produces the corresponding eigen vector(s).

### Why the sum and product of eigen values equal the trace and determinant

For an n×n matrix A, the characteristic polynomial |A − λI| expands to a degree-n polynomial in λ:

```
(−λ)^n + c_(n−1)λ^(n−1) + ... + c_1λ + c_0 = 0
```

If the eigen values are λ_1, λ_2, ..., λ_n (the roots of this polynomial, repeated according to multiplicity), the polynomial factors as (−1)^n(λ − λ_1)(λ − λ_2)···(λ − λ_n). Comparing the coefficient of λ^(n−1) on both sides shows that this coefficient equals ±(λ_1 + λ_2 + ... + λ_n); expanding |A − λI| directly by cofactors shows the same coefficient is ±(a_11 + a_22 + ... + a_nn), the trace of A. Equating the two gives property 1: the sum of the eigen values equals the trace. Comparing the constant term (setting λ = 0) gives |A| = λ_1λ_2···λ_n directly, since |A − 0·I| = |A|. This is property 2.

### Why A and A^T share the same eigen values

The determinant of a matrix is unchanged by transposition, so |A^T − λI| = |(A − λI)^T| = |A − λI| for every λ (using I^T = I). Since A and A^T have the identical characteristic polynomial |A − λI|, they have exactly the same eigen values, which is property 3. (Their eigen vectors need not coincide.)

### Why the eigen values of a triangular matrix are its diagonal entries

If A is upper (or lower) triangular, then A − λI is also triangular, with diagonal entries (a_11 − λ), (a_22 − λ), ..., (a_nn − λ). The determinant of a triangular matrix is the product of its diagonal entries, so

```
|A − λI| = (a_11 − λ)(a_22 − λ)···(a_nn − λ)
```

Setting this to zero shows the roots of the characteristic equation are exactly λ = a_11, a_22, ..., a_nn — the diagonal entries themselves. This is property 4.

## Historical Context

- Eigen value problems first arose from mechanics rather than matrix algebra: **Leonhard Euler** studied the rotational motion of rigid bodies in the 1750s and proved that every rigid body has a principal axis of rotation (*Du mouvement d'un corps solide quelconque...*, presented 1751, published 1760). **Joseph-Louis Lagrange** later recognized that these principal axes are the eigenvectors of the body's inertia matrix.
- **Augustin-Louis Cauchy**, in the early 19th century, generalized this work to classify quadric surfaces in arbitrary dimensions and coined the term *racine caractéristique* ("characteristic root") for what is now called an eigenvalue, in his 1839 memoir *Mémoire sur l'intégration des équations linéaires* — the term survives today in "characteristic equation" (Definition 10.2 above). Cauchy, building on Fourier's and Sturm's work, also proved that real symmetric matrices always have real eigenvalues.
- **Charles Hermite** extended this result in 1855 to the complex matrices that now bear his name (Hermitian matrices), showing they too always have real eigenvalues.
- The modern term "eigenvalue" comes from the German word *eigen* ("own"/"proper"), first used in this technical sense by **David Hilbert** in 1904 in his study of integral operators (*Grundzüge einer allgemeinen Theorie der linearen Integralgleichungen*); English usage settled on "eigenvalue" over the older term "proper value" during the 20th century.

## Practical Applications

1. **Structural and mechanical vibration analysis** — the natural frequencies of a bridge, building, or tuning fork are the eigen values of its stiffness/mass system, and the eigen vectors describe the shape of each vibration mode; engineers use these to avoid resonance under load.

2. **Principal Component Analysis (statistics and data science)** — the eigen values of a covariance matrix give the variance explained by each principal direction (eigen vector), letting large datasets be reduced to their most informative dimensions.

3. **Quantum mechanics** — measurable quantities (energy, momentum, angular momentum) correspond to the eigen values of Hermitian operators, and the eigen vectors are the corresponding physical states; the property that Hermitian eigen values are real matches the requirement that measured quantities be real numbers.

4. **Google's PageRank algorithm** — a webpage's importance ranking is computed as a component of the principal eigen vector of a large adjacency-based matrix representing the link structure of the web.

5. **Facial recognition (eigenfaces)** — face images are treated as vectors, and the eigen vectors of their covariance matrix ("eigenfaces") form a compact basis used to compress and compare faces for identification.

6. **Stability analysis of dynamical systems** — in population models, control systems, and epidemiology (e.g., the basic reproduction number R₀ of an infectious disease), the sign and magnitude of the dominant eigen value of the governing matrix determines whether the system grows, decays, or oscillates.

## References

**Chapter 2:** Section 16, 16.1, 16.2
