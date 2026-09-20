
# Why the Characteristic Equation Coefficients Are Sums of Principal Minors

**The question this answers:** you've learned the shortcut "S₁ = trace, S₂ = sum of 2×2 principal minors, S₃ = sum of 3×3 principal minors, ..., Sₙ = det(A)" for writing down the characteristic equation without full expansion. Why does this always work, for any size matrix?

This note shows two different ways to see why. Both are given in plain steps with a worked 3×3 number example first, then the general idea.

## The claim, in one line

For an n×n matrix A:

```
det(A − λI) = λⁿ − S₁λⁿ⁻¹ + S₂λⁿ⁻² − S₃λⁿ⁻³ + ... + (−1)ⁿSₙ
```

**Sₖ = add up the determinants of every k×k "principal minor."**

A principal minor: pick k row numbers, keep only those rows AND those same-numbered columns, throw away everything else, take the determinant.

Example, 3×3 matrix, picking rows/columns {1,2}: keep the top-left 2×2 block, ignore row 3 and column 3.

- S₁ = a₁₁ + a₂₂ + a₃₃ (just the trace — each 1×1 "minor" is one diagonal entry)
- Sₙ = det(A) (the only n×n principal minor is the whole matrix)

## Proof 1: Just expand a 3×3 example and watch it happen

Let's use an actual number matrix so nothing is hidden behind letters:

```
    ┌ 2   1   0 ┐
A = │ 1   3   1 │
    └ 0   1   2 ┘
```

We want det(A − λI):

```
        ┌ 2−λ    1     0  ┐
A − λI = │  1    3−λ    1  │
        └  0     1    2−λ ┘
```

**Expand along the first row** (this is just the ordinary 3×3 determinant recipe):

```
det(A−λI) = (2−λ) · det[3−λ  1 ; 1  2−λ]  −  1 · det[1  1 ; 0  2−λ]  +  0
```

**First piece:** det[3−λ 1; 1 2−λ] = (3−λ)(2−λ) − 1 = λ² − 5λ + 5. Multiply by (2−λ):

```
(2−λ)(λ² − 5λ + 5) = 2λ² − 10λ + 10 − λ³ + 5λ² − 5λ = −λ³ + 7λ² − 15λ + 10
```

**Second piece:** −1 · [(1)(2−λ) − (1)(0)] = −1 · (2−λ) = λ − 2

**Add them:**

```
det(A−λI) = −λ³ + 7λ² − 15λ + 10 + λ − 2 = −λ³ + 7λ² − 14λ + 8
```

Flip the overall sign to match the standard form (multiplying by −1 doesn't change the roots):

```
λ³ − 7λ² + 14λ − 8 = 0
```

**Now check this against the shortcut directly, using the actual entries of A:**

- **S₁ = trace = 2 + 3 + 2 = 7** ✓ matches the λ² coefficient.
- **S₂ = sum of the three 2×2 principal minors:**
  - rows/cols {1,2}: det[2 1; 1 3] = 6 − 1 = 5
  - rows/cols {1,3}: det[2 0; 0 2] = 4 − 0 = 4
  - rows/cols {2,3}: det[3 1; 1 2] = 6 − 1 = 5
  - Sum: 5 + 4 + 5 = **14** ✓ matches the λ¹ coefficient.
- **S₃ = det(A) = 2(6−1) − 1(2−0) + 0 = 10 − 2 = 8** ✓ matches the constant term.

Every number checks out. That's the whole point of the proof: **when you multiply out det(A − λI), the terms that survive at each power of λ are not random — they always regroup into exactly the principal minor sums.** The 3×3 example makes this concrete; the reason it keeps working for any size is explained next.

### Why it keeps working for any n (the one idea to remember)

Look at what happened in the first piece above. We had (2−λ) times a 2×2 determinant. That 2×2 determinant itself split into a λ² term, a λ¹ term, and a constant — and the constant was already a 2×2 *principal* minor (the bottom-right block). Multiplying by (2−λ) then does two things:

- the "−λ" part shifts every one of those terms up by one power of λ,
- the "2" part (a diagonal entry) adds that same principal minor pattern back in, unshifted.

This is really the same trick as expanding (x + 2)(x + 3) by hand: you get x² + (2+3)x + (2·3), a mix of "both slots contribute x" and "one slot contributes the constant." Here, each diagonal slot (a_ii − λ) contributes either "−λ" or "a_ii" to the product, and whichever k slots contribute their constant a_ii (instead of −λ) determine which k×k principal minor shows up — except it's not just the product of those diagonal entries, it's the full minor determinant, because the off-diagonal numbers (like the 1's connecting rows 1 and 2 in our example) get pulled in too through the cofactor expansion. That's exactly what you saw in the arithmetic above: 5, 4, and 5 aren't just products of diagonal pairs (2·3=6, 2·2=4, 3·2=6) — the off-diagonal 1's shaved a bit off two of them (6→5, 6→5), because det[2 1; 1 3] = 6 − 1, not just 6.

So the general rule is: **the coefficient of λⁿ⁻ᵏ is what's left over after picking, in every possible way, which k diagonal slots "hold still" (contribute a full principal minor) while the rest contribute −λ.** Trust the pattern from the worked example — a full symbolic proof of this for every n by induction is standard but mostly a longer, letter-only version of the exact same arithmetic you just did with numbers.

## Why this matches "sum of eigenvalues" and "product of eigenvalues"

The eigenvalues λ₁, λ₂, λ₃ are just the roots of that same cubic. Any cubic with roots r₁, r₂, r₃ can be written as (r₁−λ)(r₂−λ)(r₃−λ), and expanding that (ordinary school algebra) gives coefficients that are sums and products of the roots. Since this is the *same* polynomial as det(A−λI), written two different ways, the coefficients must agree term for term:

```
S₁ = trace(A) = λ₁ + λ₂ + λ₃  (sum of eigenvalues)
S₃ = det(A)   = λ₁ · λ₂ · λ₃  (product of eigenvalues)
```

You can check this on the example above: the cubic λ³ − 7λ² + 14λ − 8 factors as (λ−1)(λ−2)(λ−4) — its eigenvalues are 1, 2, 4. Sum = 7 = S₁ ✓. Product = 8 = S₃ ✓.

## Proof 2: The same result using derivatives (differentiate at λ = 0)

This is a completely different route to the same conclusion. Instead of multiplying everything out, we use one calculus fact about determinants, plug in λ = 0 (and its derivatives at 0), and the Sₖ's fall out directly — no expanding brackets at all.

### The one calculus fact we need (Jacobi's formula)

For a matrix that changes with a variable, there's a known shortcut for differentiating its determinant:

```
d/dμ [det M(μ)]  =  trace( adj(M(μ)) · M'(μ) )
```

Don't worry about proving this here — treat it as a known tool (it comes from the product-rule expansion of a determinant along its rows). `adj(M)` is the **adjugate**: the matrix of cofactors, transposed. All we need from it is one fact: **the diagonal entries of adj(M) are exactly the principal minors of M, one size smaller.** Concretely, the (1,1) entry of adj(M) is the determinant you get by deleting row 1 and column 1 from M. Same for (2,2), (3,3), etc.

### Set it up with μ instead of λ, so signs stay simple

Instead of A − λI, use A + μI (same idea, opposite sign convention, so every term comes out positive and easy to read):

```
q(μ) = det(A + μI)
```

At μ = 0 this is just det(A) = S₃ (using our example's n=3). We want the derivative rules to hand us S₂ and S₁ too.

### First derivative, evaluated at μ = 0, gives S₂

Apply Jacobi's formula. Since M(μ) = A + μI, its derivative M'(μ) is just the identity matrix I, and multiplying by I does nothing:

```
q'(μ) = trace( adj(A + μI) )
```

Now use the one fact from above: the diagonal entries of an adjugate are principal minors, one size smaller. For our 3×3 example, that means the three diagonal entries of adj(A + μI) are the three 2×2 principal minors of (A + μI) — and at μ = 0, those are exactly the three 2×2 principal minors of A we already computed by hand (5, 4, 5). Trace just adds the diagonal entries:

```
q'(0) = 5 + 4 + 5 = 14 = S₂ ✓
```

matching what we got by brute-force expansion earlier.

### Second derivative, evaluated at μ = 0, gives 2×S₁ (divide by 2! to get S₁)

Differentiate again. Each of the three terms from before is itself a small determinant, so Jacobi's formula applies to each one again, in the same way — trim it down one more size. This peels off *one more* index, and because there are two ways to reach any given 1×1 minor (e.g. "delete row/col 2, then delete row/col 3" or "delete row/col 3, then delete row/col 2" both leave just entry a₁₁), each diagonal entry a_ii gets counted twice:

```
q''(0) = 2 · (a₁₁ + a₂₂ + a₃₃) = 2 · 7 = 14
```

Divide by 2! = 2 (the standard Taylor-coefficient correction) to undo the double-counting:

```
q''(0)/2! = 14/2 = 7 = S₁ ✓
```

Again matches.

### The general pattern

Each time you differentiate, Jacobi's formula trims the matrix down by one more row/column, and the number of ways to reach a given smaller minor by peeling one index at a time is k! (a basic counting fact — k items can be removed one at a time in k! different orders). So dividing the k-th derivative by k! always exactly cancels the overcounting, and you land on Sₙ₋ₖ every time:

```
[k-th derivative of q at 0] / k!  =  Sₙ₋ₖ
```

That's the whole proof: differentiate det(A + μI) repeatedly, evaluate each derivative at 0, divide by the right factorial, and every Sₖ pops out — because Jacobi's formula keeps handing you smaller and smaller principal minors automatically, without ever multiplying out a single bracket.

### Why bother with this second proof

Proof 1 (expand and collect terms) is the direct, hands-on way — you multiply things out and the pattern is visible in the arithmetic itself. Proof 2 (differentiate) never expands anything; it leans entirely on one borrowed calculus fact (Jacobi's formula) plus one counting fact (k! orderings). It's shorter once you accept those two facts, and it explains *why* principal minors specifically show up — they're baked into the definition of a cofactor/adjugate from the start, rather than something you have to notice after expanding brackets.
