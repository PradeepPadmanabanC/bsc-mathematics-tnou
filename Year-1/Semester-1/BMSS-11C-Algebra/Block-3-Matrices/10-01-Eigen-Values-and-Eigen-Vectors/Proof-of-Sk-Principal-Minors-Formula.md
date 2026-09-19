# Why the Characteristic Equation Coefficients Are Sums of Principal Minors

This note answers a specific question: **why does the S₁, S₂, S₃, ... shortcut (trace, sum of 2×2 minors, sum of 3×3 minors, ..., determinant) always work, for a matrix of any size, not just 3×3?**

We'll build the proof up slowly: first by brute-force expanding small cases by hand, then generalizing.

## The claim, stated precisely

For an n×n matrix A, the characteristic polynomial |A − λI| always expands as

```
λⁿ − S₁λⁿ⁻¹ + S₂λⁿ⁻² − S₃λⁿ⁻³ + ... + (−1)ⁿSₙ = 0
```

where **Sₖ = the sum of all k×k principal minors of A**.

A *principal minor* of size k is: pick any k of the n row indices, keep only those rows and the *same* columns, delete everything else, and take the determinant of what's left. (For example, in a 3×3 matrix, picking rows/columns {1,2} gives a 2×2 principal minor; there are 3 such choices: {1,2}, {1,3}, {2,3}.)

Note: S₁ is just the trace (each "1×1 principal minor" is a single diagonal entry a_ii), and Sₙ is just det(A) (the only n×n principal minor is the whole matrix).

## Step 1: Work out n = 2 completely by hand

```
        ┌ a₁₁−λ    a₁₂  ┐
A − λI = │                │
        └ a₂₁    a₂₂−λ  ┘
```

Determinant of a 2×2 matrix is (top-left × bottom-right) − (top-right × bottom-left):

```
|A − λI| = (a₁₁ − λ)(a₂₂ − λ) − a₁₂a₂₁
```

Expand the product:

```
= a₁₁a₂₂ − a₁₁λ − a₂₂λ + λ² − a₁₂a₂₁
= λ² − (a₁₁ + a₂₂)λ + (a₁₁a₂₂ − a₁₂a₂₁)
```

Compare this to the claimed form λ² − S₁λ + S₂:

- **S₁ = a₁₁ + a₂₂** — that's the trace. ✓ (matches: sum of the two 1×1 principal minors, {1} and {2})
- **S₂ = a₁₁a₂₂ − a₁₂a₂₁** — that's exactly det(A). ✓ (matches: the one 2×2 principal minor, the whole matrix)

So for n=2, the formula is just... the direct expansion. Nothing hidden yet. The real content shows up at n=3.

## Step 2: Work out n = 3 by hand, and watch S₂ appear

```
        ┌ a₁₁−λ    a₁₂      a₁₃   ┐
A − λI = │ a₂₁     a₂₂−λ     a₂₃   │
        └ a₃₁      a₃₂     a₃₃−λ ┘
```

Expand the determinant along the first row (ordinary cofactor expansion, the same technique you'd use for any 3×3 determinant):

```
|A − λI| = (a₁₁−λ) · | a₂₂−λ   a₂₃  |   −  a₁₂ · | a₂₁   a₂₃  |   +  a₁₃ · | a₂₁   a₂₂−λ |
                     | a₃₂    a₃₃−λ|            | a₃₁   a₃₃−λ|            | a₃₁    a₃₂   |
```

This looks messy, but notice something important: **only the first cofactor (multiplying a₁₁−λ) contains any λ inside the 2×2 minor.** The other two cofactors — the ones multiplying the plain constants a₁₂ and a₁₃ — involve minors built from row 2, row 3, and *both* columns 1 and 3 (or 1 and 2), which never touches a diagonal position twice, so at most one λ can appear inside them, not two. Let's just carefully expand everything and collect powers of λ. This is tedious but mechanical — do it once and you'll trust the pattern forever.

**Piece 1:** (a₁₁ − λ) · [(a₂₂−λ)(a₃₃−λ) − a₂₃a₃₂]

First expand the inner 2×2 piece (same computation as Step 1, applied to the bottom-right 2×2 block):

```
(a₂₂−λ)(a₃₃−λ) − a₂₃a₃₂ = λ² − (a₂₂+a₃₃)λ + (a₂₂a₃₃ − a₂₃a₃₂)
```

Now multiply by (a₁₁ − λ):

```
(a₁₁ − λ)[λ² − (a₂₂+a₃₃)λ + (a₂₂a₃₃−a₂₃a₃₂)]

= a₁₁λ² − a₁₁(a₂₂+a₃₃)λ + a₁₁(a₂₂a₃₃−a₂₃a₃₂)
  − λ³ + (a₂₂+a₃₃)λ² − (a₂₂a₃₃−a₂₃a₃₂)λ
```

Collect by power of λ:

- **λ³:** −λ³
- **λ²:** a₁₁λ² + (a₂₂+a₃₃)λ² = [a₁₁ + a₂₂ + a₃₃]λ²
- **λ¹:** −a₁₁(a₂₂+a₃₃)λ − (a₂₂a₃₃−a₂₃a₃₂)λ = −[a₁₁a₂₂ + a₁₁a₃₃ + a₂₂a₃₃ − a₂₃a₃₂]λ
- **λ⁰:** a₁₁(a₂₂a₃₃−a₂₃a₃₂)

**Piece 2:** −a₁₂ · (a₂₁(a₃₃−λ) − a₂₃a₃₁) = −a₁₂a₂₁(a₃₃−λ) + a₁₂a₂₃a₃₁
= −a₁₂a₂₁a₃₃ + a₁₂a₂₁λ + a₁₂a₂₃a₃₁

- **λ¹:** a₁₂a₂₁λ
- **λ⁰:** −a₁₂a₂₁a₃₃ + a₁₂a₂₃a₃₁

**Piece 3:** a₁₃ · (a₂₁a₃₂ − (a₂₂−λ)a₃₁) = a₁₃a₂₁a₃₂ − a₁₃a₃₁a₂₂ + a₁₃a₃₁λ

- **λ¹:** a₁₃a₃₁λ
- **λ⁰:** a₁₃a₂₁a₃₂ − a₁₃a₃₁a₂₂

**Now add all three pieces together, power by power:**

**λ³ coefficient:** −1 ✓ (matches the theorem's leading term)

**λ² coefficient:** a₁₁ + a₂₂ + a₃₃ — this is the **trace**, i.e., S₁. (Note the sign here is +S₁, not −S₁ — that's because this expansion of |A−λI| comes out as −λ³+S₁λ²−S₂λ+S₃ overall, i.e., −1 times the "textbook" form λ³−S₁λ²+S₂λ−S₃. Both describe the same equation once set to zero, since multiplying an equation by −1 doesn't change its roots — see the total below.)

**λ¹ coefficient:** Adding Piece 1's λ¹ term with Piece 2 and Piece 3's λ¹ terms:

```
−[a₁₁a₂₂ + a₁₁a₃₃ + a₂₂a₃₃ − a₂₃a₃₂]  +  a₁₂a₂₁  +  a₁₃a₃₁
= −a₁₁a₂₂ − a₁₁a₃₃ − a₂₂a₃₃ + a₂₃a₃₂ + a₁₂a₂₁ + a₁₃a₃₁
= −(a₁₁a₂₂ − a₁₂a₂₁) − (a₁₁a₃₃ − a₁₃a₃₁) − (a₂₂a₃₃ − a₂₃a₃₂)
```

Look closely at each bracket: `(a₁₁a₂₂ − a₁₂a₂₁)` is exactly the 2×2 principal minor on rows/columns {1,2}. `(a₁₁a₃₃ − a₁₃a₃₁)` is the principal minor on {1,3}. `(a₂₂a₃₃ − a₂₃a₃₂)` is the principal minor on {2,3}. So the λ¹ coefficient is exactly **−(sum of all three 2×2 principal minors) = −S₂**.

**λ⁰ coefficient:** Adding all three constant terms gives back exactly det(A) = S₃ (you can verify this matches the plain cofactor expansion of |A| along the first row — it's the same expression with λ=0 substituted from the start, which must be true since setting λ=0 in |A−λI| just gives |A|).

**Putting it together for n=3:**

```
|A − λI| = −λ³ + S₁λ² − S₂λ + S₃ = −(λ³ − S₁λ² + S₂λ − S₃)
```

Setting |A − λI| = 0 gives λ³ − S₁λ² + S₂λ − S₃ = 0, matching Example 10.7 exactly, and now you've seen with your own hands *why* S₂ turns out to be the sum of three specific 2×2 minors — it's not a coincidence or a rule to memorize, it just falls out of collecting terms after expanding the determinant.

## Step 3: Why this keeps happening for any n (the general pattern)

Redo the n=3 computation, but pay attention to *where each type of term came from*, rather than the arithmetic:

- The **λⁿ** term always comes from multiplying together all n diagonal factors (a_ii − λ) and taking only the λ from each — this is the only way to get λ to the highest power, since every off-diagonal entry a_ij (i≠j) is a plain constant with no λ in it at all.
- The **λⁿ⁻¹** term comes from taking the λ from *all but one* of the diagonal factors, and the constant a_ii from the one you skip, then summing over which diagonal position you skipped. That produces Σᵢ a_ii = trace = S₁.
- The **λⁿ⁻ᵏ** term, more generally, comes from taking the λ from (n−k) of the diagonal factors and "something else" from the remaining k diagonal positions. That "something else," when you track it through the expansion carefully (as we did by brute force for n=3), always turns out to be the determinant of the k×k principal submatrix sitting on those k skipped positions — not just the product of their diagonal entries, because the off-diagonal entries connecting those k skipped rows/columns also get pulled in through the cofactor expansion (this is exactly what happened with the a₁₂a₂₁ and a₂₃a₃₂ terms above — they came from off-diagonal entries, not diagonal ones, and they combined with diagonal products to form full 2×2 determinants, not just products of diagonal pairs).

This is the crucial insight the brute-force n=3 case demonstrates: **the coefficient isn't just "sum of products of k diagonal entries" — it's "sum of determinants of k×k principal submatrices,"** because expanding the determinant naturally pulls in the off-diagonal cross terms (like a₁₂a₂₁) that turn a plain product into a proper minor.

**A cleaner inductive way to see it holds for every n (once you trust the n=3 case):**

Suppose the formula |M − λI| = Σₖ (−1)^k Sₖ(M) λ^(n−k) is already known to hold for every (n−1)×(n−1) matrix M (that's the induction hypothesis). Take your n×n matrix A and expand |A − λI| along the last row, cofactor-style, exactly as we did for n=3:

```
|A − λI| = (a_nn − λ) · |B − λI|   +   (terms from off-diagonal entries in the last row)
```

where B is the (n−1)×(n−1) matrix obtained by deleting row n and column n from A (the top-left principal submatrix). By the induction hypothesis, |B − λI| already expands correctly in terms of the principal minors of B — and every principal minor of B is automatically also a principal minor of A (just one that happens not to use row/column n). Multiplying by (a_nn − λ) does two things: the "−λ" part raises every power of λ by one (extending the pattern up to λⁿ), and the "a_nn" part adds in exactly the principal minors of A that *do* include index n at size one higher than before. The leftover off-diagonal terms from the last row (the ones like a₁₂a₂₁ we saw directly) combine, after further expansion, to add in the remaining principal minors that include index n paired with some other row/column but not through the diagonal alone.

Doing this bookkeeping fully (it's routine but long — see Horn & Johnson, *Matrix Analysis*, or any graduate linear algebra text, under "characteristic polynomial coefficients" or "elementary symmetric functions of eigenvalues") confirms that every principal minor of every size gets accounted for exactly once, completing the induction.

## Why this matches "sum of eigenvalues" and "product of eigenvalues" too

If λ₁, ..., λₙ are the n roots of the characteristic polynomial (the eigenvalues), then by definition the polynomial also factors as

```
(λ₁ − λ)(λ₂ − λ)···(λₙ − λ)   [up to an overall sign to match the leading λⁿ term]
```

Expanding this factored form by ordinary algebra (the same way you'd expand (x−r₁)(x−r₂)(x−r₃) in a school algebra class) gives coefficients that are the **elementary symmetric polynomials** of λ₁,...,λₙ:

- coefficient of λⁿ⁻¹ ↔ λ₁+λ₂+...+λₙ (sum of eigenvalues)
- coefficient of λ⁰ ↔ λ₁λ₂···λₙ (product of eigenvalues)

Since this factored expansion and the principal-minor expansion above are two ways of writing the *same* polynomial |A−λI|, their coefficients must match term for term. That's why:

```
S₁ = trace(A) = sum of eigenvalues
Sₙ = det(A) = product of eigenvalues
```

which is exactly properties 1 and 2 already stated in the main README, now justified from both directions — principal minors on one side, eigenvalues on the other, forced to agree because they're expanding the same polynomial.
