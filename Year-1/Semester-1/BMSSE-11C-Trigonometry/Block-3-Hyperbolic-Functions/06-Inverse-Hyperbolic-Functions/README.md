# Unit 6 — Inverse Hyperbolic Functions

## Topics
- Inverse hyperbolic functions
- Logarithmic forms of inverse hyperbolic functions
- Properties and derivatives

## Logarithmic Forms

### sinh⁻¹ x
- sinh⁻¹ x = ln(x + √(x² + 1))
- Domain: (-∞, ∞)
- Range: (-∞, ∞)

### cosh⁻¹ x
- cosh⁻¹ x = ln(x + √(x² - 1)), x ≥ 1
- Domain: [1, ∞)
- Range: [0, ∞)

### tanh⁻¹ x
- tanh⁻¹ x = ½ ln((1 + x)/(1 - x)), |x| < 1
- Domain: (-1, 1)
- Range: (-∞, ∞)

### coth⁻¹ x
- coth⁻¹ x = ½ ln((x + 1)/(x - 1)), |x| > 1
- Domain: (-∞, -1) ∪ (1, ∞)
- Range: (-∞, 0) ∪ (0, ∞)

### sech⁻¹ x
- sech⁻¹ x = ln((1 + √(1 - x²))/x), 0 < x ≤ 1
- Domain: (0, 1]
- Range: [0, ∞)

### cosech⁻¹ x
- cosech⁻¹ x = ln((1 + √(1 + x²))/x), x ≠ 0
- Domain: (-∞, 0) ∪ (0, ∞)
- Range: (-∞, 0) ∪ (0, ∞)

## Derivatives

### Basic Derivatives
- d/dx(sinh⁻¹ x) = 1/√(x² + 1)
- d/dx(cosh⁻¹ x) = 1/√(x² - 1), x > 1
- d/dx(tanh⁻¹ x) = 1/(1 - x²), |x| < 1
- d/dx(coth⁻¹ x) = 1/(1 - x²), |x| > 1
- d/dx(sech⁻¹ x) = -1/(x√(1 - x²)), 0 < x < 1
- d/dx(cosech⁻¹ x) = -1/(|x|√(1 + x²)), x ≠ 0

## Important Relations
- sinh⁻¹(sinh x) = x
- cosh⁻¹(cosh x) = |x| (principal value)
- tanh⁻¹(tanh x) = x

## Proofs of Logarithmic Forms

### Proof of sinh⁻¹ x = ln(x + √(x² + 1))
Let y = sinh⁻¹ x, then x = sinh y = (eʸ - e⁻ʸ)/2
Solving: eʸ - 2x - e⁻ʸ = 0
Multiply by eʸ: e²ʸ - 2xeʸ - 1 = 0
Using quadratic formula: eʸ = x + √(x² + 1)
Therefore: y = ln(x + √(x² + 1))

## Practice Problems
- [ ] Prove sinh⁻¹ x = ln(x + √(x² + 1))
- [ ] Prove cosh⁻¹ x = ln(x + √(x² - 1))
- [ ] Express tanh⁻¹(1/2) in logarithmic form
- [ ] Find derivative of sinh⁻¹(3x)
- [ ] Calculate cosh⁻¹(2)

## Notes
<!-- Add your study notes here -->
