
# Unit 12: Similar Matrices

**Block:** III — Matrices
**Course:** BMSS-11C — Algebra

## Objectives

After completion of this unit, students will be able to:
- understand the concept of similar matrices.
- prove that similar matrices have the same characteristic equation.

## Table of Contents

- [12.2 Similar Matrices](#122-similar-matrices)
- [Mathematical Derivation](#mathematical-derivation)
- [Historical Context](#historical-context)
- [Practical Applications](#practical-applications)

## 12.2 Similar Matrices

### Definition 12.1. Similar Matrices

Two matrices A and B are said to be **similar** if there exists a non-singular matrix P such that

```
P⁻¹AP = B
```

If D is the diagonal matrix whose elements are the eigen values of the matrix A, then A and D are similar matrices — this is exactly the relationship B⁻¹AB = D established in Unit 12.1.

### Theorem 12.1. If A and B are similar matrices, then they have the same characteristic equation.

**Proof.** Since A and B are similar, there exists a matrix P such that B = P⁻¹AP.

```
∴ B − λI  =  P⁻¹AP − λI

  B − λI  =  P⁻¹AP − P⁻¹λIP

           =  P⁻¹(AP − λIP)

           =  P⁻¹(A − λI)P

∴ |B − λI|  =  |P⁻¹(A − λI)P|

            =  |P⁻¹| |A − λI| |P|

            =  |P⁻¹| |P| |A − λI|

            =  |P⁻¹P| |A − λI|

            =  |I| |A − λI|

            =  |A − λI|
```

The characteristic equations of A and B are respectively |A − λI| = 0 and |B − λI| = 0. Hence they are equal. ∎

### Corollary 12.1. Two similar matrices have the same eigen values.

This follows immediately from Theorem 12.1: since A and B share the same characteristic equation, and the eigen values are precisely the roots of that equation, A and B must have the same eigen values.

## Mathematical Derivation

### Why B − λI factors as P⁻¹(A − λI)P

The key algebraic step in the proof of Theorem 12.1 is rewriting λI in the "sandwiched" form P⁻¹λIP. Since λI commutes with every matrix (it is a scalar multiple of the identity), P⁻¹λIP = λP⁻¹IP = λP⁻¹P = λI, so this substitution changes nothing — it simply re-expresses λI in a form that can be factored alongside AP. Once written as P⁻¹AP − P⁻¹λIP, the common factors P⁻¹ on the left and P on the right can be pulled out of both terms, giving P⁻¹(AP − λIP) = P⁻¹(A − λI)P. This is the only place in the proof where the specific structure of B = P⁻¹AP is used; every subsequent step is a property of determinants.

### Why the determinant identity |P⁻¹||A − λI||P| = |A − λI| holds

The proof uses three standard determinant facts in sequence:

1. **Multiplicativity of the determinant**: |MN| = |M||N| for any square matrices M, N of the same order. Applied twice, this turns |P⁻¹(A − λI)P| into |P⁻¹||A − λI||P|.
2. **Commutativity of scalar multiplication of determinants**: although matrix multiplication is not commutative in general, the *determinants* |P⁻¹|, |A − λI|, |P| are ordinary scalars (real or complex numbers), so they can be freely reordered: |P⁻¹||A − λI||P| = |P⁻¹||P||A − λI|.
3. **Inverse property**: |P⁻¹||P| = |P⁻¹P| = |I| = 1, since P⁻¹P is the identity matrix and the determinant of the identity is 1.

Combining these three facts collapses the entire expression back down to |A − λI|, which is exactly what shows |B − λI| = |A − λI| for every value of λ, not merely at the roots. This is a stronger statement than "A and B have the same eigen values" (Corollary 12.1) — it says their characteristic *polynomials* are identical as polynomials in λ, so every coefficient (trace, determinant, and every intermediate symmetric function of the eigen values) also matches.

### Why similarity is an equivalence relation

The definition B = P⁻¹AP (Definition 12.1) satisfies the three properties of an equivalence relation, which is why "A is similar to B" behaves like "A equals B" for many purposes:

- **Reflexive**: A = I⁻¹AI, so A is similar to itself (taking P = I).
- **Symmetric**: if B = P⁻¹AP, then multiplying on the left by P and on the right by P⁻¹ gives PBP⁻¹ = A, i.e., A = (P⁻¹)⁻¹B(P⁻¹), so A is similar to B via the matrix P⁻¹.
- **Transitive**: if B = P⁻¹AP and C = Q⁻¹BQ, substituting gives C = Q⁻¹P⁻¹APQ = (PQ)⁻¹A(PQ), so A is similar to C via the matrix PQ.

Because similarity is an equivalence relation, it partitions all n×n matrices into disjoint similarity classes, and Theorem 12.1 shows that the characteristic polynomial is constant on each class — it is what is called a **similarity invariant**.

## Historical Context

- The underlying idea of "conjugate" objects related by A ↦ P⁻¹AP first appeared in group theory rather than matrix algebra: **Augustin-Louis Cauchy**, in a series of papers written between 1844 and 1846, studied what he called "systems of conjugate permutations," establishing conjugacy as a fundamental equivalence relation among permutations — the same relation that Definition 12.1 applies to matrices.
- The formal machinery of matrix algebra needed to state Definition 12.1 and prove Theorem 12.1 — matrices as objects with their own multiplication and inverses, and determinant identities such as |MN| = |M||N| — was laid down by **Arthur Cayley** in his 1858 paper *A Memoir on the Theory of Matrices* (Philosophical Transactions of the Royal Society, received 10 December 1857, read 14 January 1858), the same memoir already cited in Unit 11 for the Cayley-Hamilton theorem. The Wikipedia article on matrix similarity notes that similar matrices are, in Cayley's algebraic framework, exactly the matrices called **conjugate** in the general linear group — directly carrying over Cauchy's group-theoretic terminology.
- A closely related but distinct result for *symmetric* matrices was proved by **James Joseph Sylvester** in 1852: Sylvester's law of inertia concerns matrices related by congruence (B = PᵗAP, using the transpose rather than the inverse) rather than similarity, and shows that the signs of the eigen values (not their exact values) are the shared invariant. Because congruence and similarity coincide only when P is orthogonal, Sylvester's theorem is a companion result to Theorem 12.1 rather than a special case of it.
- The general theory was consolidated later in the 19th century by **Camille Jordan** (1870), whose Jordan normal form gives the finest possible classification of similarity classes over the complex numbers, refining "same characteristic polynomial" (Theorem 12.1) into a complete similarity invariant.

Sources: [Matrix similarity, Wikipedia](https://en.wikipedia.org/wiki/Matrix_similarity); [History of group theory, Wikipedia](https://en.wikipedia.org/wiki/History_of_group_theory); [Sylvester's law of inertia, Wikipedia](https://en.wikipedia.org/wiki/Sylvester%27s_law_of_inertia); [A Memoir on the Theory of Matrices, Philosophical Transactions of the Royal Society (1858)](https://royalsocietypublishing.org/doi/10.1098/rstl.1858.0002).

## Practical Applications

1. **Change of basis / coordinate transformations** — similar matrices represent the *same* linear transformation viewed in different coordinate systems (bases); Theorem 12.1 guarantees that intrinsic properties of the transformation (eigen values, trace, determinant) do not depend on which coordinate system is used to describe it.

2. **Simplifying computation via diagonalisation** — as in Unit 12.1, replacing A by a similar diagonal matrix D = B⁻¹AB reduces hard problems (solving A^k, systems of differential equations) to trivial ones on D, and Theorem 12.1 is exactly what justifies transferring the eigen values found from D back to A.

3. **Control theory and state-space realizations** — a given physical system can be described by many different (similar) state-space matrices depending on the choice of state variables; Theorem 12.1 ensures that the system's poles (eigen values of the state matrix), which determine stability, are the same in every such representation.

4. **Numerical linear algebra algorithms** — algorithms such as the QR algorithm for computing eigen values work by repeatedly replacing a matrix with a similar one (via orthogonal similarity transformations) that is progressively closer to triangular or diagonal form, relying on Theorem 12.1 to guarantee the eigen values never change along the way.

5. **Graph isomorphism and network comparison** — comparing the characteristic polynomials of two graphs' adjacency matrices (which are similarity invariants when relabeling vertices induces a similarity transformation via a permutation matrix) gives a computationally cheap necessary condition for two networks having the same underlying structure.

## References

**Chapter 2:** Section 16
