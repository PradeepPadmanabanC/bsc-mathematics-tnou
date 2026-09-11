# Unit 8 — Summation of Series

## Topics
- Sums of trigonometrical series
- Applications of binomial, exponential, logarithmic and Gregory's series
- Difference method

## Standard Series

### Binomial Series
(1 + x)ⁿ = 1 + nx + n(n-1)x²/2! + n(n-1)(n-2)x³/3! + ...
Valid for |x| < 1 when n is not a positive integer

### Exponential Series
- eˣ = 1 + x + x²/2! + x³/3! + x⁴/4! + ...
- e^(iθ) = cos θ + i sin θ

### Logarithmic Series
- log(1 + x) = x - x²/2 + x³/3 - x⁴/4 + ... (for -1 < x ≤ 1)
- log(1 - x) = -x - x²/2 - x³/3 - x⁴/4 - ... (for -1 ≤ x < 1)

### Gregory's Series
tan⁻¹x = x - x³/3 + x⁵/5 - x⁷/7 + ... (for |x| ≤ 1)

## Trigonometric Series

### Sum of Sines
∑sin(α + (n-1)β) from n=1 to N
= [sin(Nβ/2) / sin(β/2)] · sin(α + (N-1)β/2)

### Sum of Cosines
∑cos(α + (n-1)β) from n=1 to N
= [sin(Nβ/2) / sin(β/2)] · cos(α + (N-1)β/2)

### Useful Formulas
- sin θ + sin 2θ + sin 3θ + ... + sin nθ
- cos θ + cos 2θ + cos 3θ + ... + cos nθ
- Using complex exponentials: e^(iθ) + e^(2iθ) + ... + e^(niθ)

## Difference Method

### Principle
Express the general term Tₙ as a difference: Tₙ = f(n) - f(n+1)
Then ∑Tₙ = f(1) - f(n+1) (telescoping sum)

### Examples
- 1/(n(n+1)) = 1/n - 1/(n+1)
- 1/((2n-1)(2n+1)) = ½(1/(2n-1) - 1/(2n+1))

### Applications
- Summing series with factored denominators
- Partial fraction decomposition
- Trigonometric expressions

## Special Techniques

### Using Euler's Formula
Convert trigonometric sums to exponential form:
- ∑e^(inθ) = geometric series
- Extract real and imaginary parts

### Product-to-Sum
Convert products to sums for easier summation

### Complex Number Method
Use z = e^(iθ) and geometric series formula

## Practice Problems
- [ ] Find ∑sin nθ from n=1 to n
- [ ] Evaluate ∑cos nθ from n=1 to n
- [ ] Sum: 1/(1·2) + 1/(2·3) + ... + 1/(n(n+1))
- [ ] Find sum of sin θ + sin 3θ + sin 5θ + ... to n terms
- [ ] Evaluate cos θ + cos 2θ + cos 3θ + ... + cos nθ
- [ ] Use Gregory's series to find π/4
- [ ] Sum: 1 + 2x + 3x² + 4x³ + ... to n terms

## Important Applications
1. Fourier series analysis
2. Signal processing
3. Physics (wave summation)
4. Numerical methods

## Notes
<!-- Add your study notes here -->
