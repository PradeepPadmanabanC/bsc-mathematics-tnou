# Unit 7 — Logarithms of a Complex Number

## Topics
- Inverse function of exponential functions
- Values of Log(u + iv)
- Complex index (a^(b+ic))

## Complex Exponential Function

### Definition
- e^z = e^(x+iy) = eˣ(cos y + i sin y)
- |e^z| = eˣ
- arg(e^z) = y

### Euler's Formula
- e^(iθ) = cos θ + i sin θ
- e^(-iθ) = cos θ - i sin θ
- cos θ = (e^(iθ) + e^(-iθ))/2
- sin θ = (e^(iθ) - e^(-iθ))/(2i)

## Complex Logarithm

### Definition
If z = re^(iθ), then log z = log r + i(θ + 2nπ), where n ∈ ℤ

### For z = u + iv
- |z| = √(u² + v²)
- arg(z) = tan⁻¹(v/u) (with proper quadrant adjustment)
- log(u + iv) = log√(u² + v²) + i(arg(z) + 2nπ)

### Principal Value (Log)
- Log z = log|z| + i Arg(z)
- where Arg(z) is the principal argument: -π < Arg(z) ≤ π

### Multi-valued Nature
- log z has infinitely many values differing by 2πi
- General logarithm: log z = Log z + 2nπi, n ∈ ℤ

## Properties

### Basic Properties (with caution)
- Log(z₁z₂) = Log z₁ + Log z₂ (up to integer multiples of 2πi)
- Log(z₁/z₂) = Log z₁ - Log z₂ (up to integer multiples of 2πi)
- Log(zⁿ) = n Log z (up to integer multiples of 2πi)

**Note:** These properties hold for principal values only when results are adjusted to principal range.

## Complex Powers

### Definition
- a^(b+ic) = e^((b+ic)log a)
- = e^((b+ic)(log|a| + i arg(a)))
- = e^(b log|a| - c arg(a)) · e^(i(c log|a| + b arg(a)))

### For Real Base a > 0
- a^(b+ic) = a^b · e^(ic log a)
- = a^b[cos(c log a) + i sin(c log a)]

### Special Cases
- i^i = e^(i log i) = e^(i·iπ/2) = e^(-π/2) ≈ 0.2079 (principal value)
- i^i = e^(-π/2 - 2nπ), n ∈ ℤ (all values)
- (-1)^i = e^(i log(-1)) = e^(i·iπ) = e^(-π) ≈ 0.0432

## Important Examples

### Example 1: Log i
- i = e^(iπ/2)
- Log i = log 1 + i(π/2) = iπ/2
- General: log i = i(π/2 + 2nπ)

### Example 2: Log(-1)
- -1 = e^(iπ)
- Log(-1) = log 1 + iπ = iπ
- General: log(-1) = i(π + 2nπ)

### Example 3: Log(1 + i)
- |1 + i| = √2
- arg(1 + i) = π/4
- Log(1 + i) = log√2 + iπ/4 = (log 2)/2 + iπ/4

### Example 4: i^(2+3i)
- i^(2+3i) = e^((2+3i)log i)
- = e^((2+3i)·iπ/2)
- = e^(iπ - 3π/2)
- = e^(-3π/2)[cos π + i sin π]
- = -e^(-3π/2)

## Practice Problems
- [ ] Find Log(1 + i)
- [ ] Find all values of log(-4)
- [ ] Calculate Log(-1 + i√3)
- [ ] Compute i^i (principal value)
- [ ] Evaluate (1+i)^(1+i)
- [ ] Find all values of (-1)^(1/3)
- [ ] Calculate Log(e^(2+3i))

## Notes
<!-- Add your study notes here -->
