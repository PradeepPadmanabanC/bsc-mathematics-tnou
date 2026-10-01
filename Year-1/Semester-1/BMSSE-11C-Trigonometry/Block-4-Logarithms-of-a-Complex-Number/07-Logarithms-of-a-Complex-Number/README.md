# Logarithms of a Complex Number

These notes explain the **logarithm of a complex number**, including its definition, principal value, general value, base-changing formula, and methods for solving problems involving complex logarithms. The unit develops the logarithm of x + iy from the exponential form of a complex number and applies the result to examples involving i, trigonometric expressions, powers, and related identities.

## Table of Contents

1. [Notes](#notes)
   - [Overview](#overview)
   - [Mathematical Foundation](#mathematical-foundation)
   - [Derivation of the General Method](#derivation-of-the-general-method)
   - [Key Observations](#key-observations)
2. [Historical Background](#historical-background)
3. [Real-World Applications](#real-world-applications)
4. [Self-Audit](#self-audit)

## Notes

### Overview

The logarithm of a complex number extends the familiar real logarithm to complex quantities. If z = eᵘ, then u is called a logarithm of z. Unlike the real logarithm, a non-zero complex number generally has infinitely many logarithms because the argument of a complex number can differ by integer multiples of 2π.

The technique matters because it:

- Provides a systematic way to find the **principal value** of the logarithm of a complex number.
- Gives the **general value**, including all possible logarithms.
- Converts complex logarithm problems into calculations involving the modulus and argument of a complex number.
- Provides tools for solving problems involving complex powers and exponential expressions.

### Mathematical Foundation

Let z = x + iy, where x and y are real numbers.

By definition, if

> **z = eᵘ**

then

> **u = log z**

For the complex number x + iy, write

> **logₑ(x + iy) = α + iβ**

Then

> **x + iy = e^(α + iβ)**

Using the exponential form of a complex number,

> **e^(α + iβ) = eᵅ(cos β + i sin β)**

Equating real and imaginary parts gives

> **x = eᵅ cos β**

> **y = eᵅ sin β**

Squaring and adding,

> **x² + y² = e²ᵅ(cos² β + sin² β)**

Since cos² β + sin² β = 1,

> **x² + y² = e²ᵅ**

Therefore,

> **α = 1/2 log(x² + y²)**

Dividing the two component equations gives

> **y/x = tan β**

and hence, as presented in the PDF,

> **β = tan⁻¹(y/x)**

Therefore the principal-value expression used in the unit is

> **logₑ(x + iy) = 1/2 log(x² + y²) + i tan⁻¹(y/x)**

The general value includes the periodicity of the argument:

> **Logₑ(x + iy) = 1/2 log(x² + y²) + i tan⁻¹(y/x) + 2nπi**

where n is any integer.

The PDF distinguishes the notation as follows:

> **General value: Log(x + iy) = 1/2 log(x² + y²) + i tan⁻¹(y/x) + 2nπi**

> **Principal value: log(x + iy) = 1/2 log(x² + y²) + i tan⁻¹(y/x)**

The base-changing formula given in the unit is

> **Log_b z = Logₑ z / Logₑ b**

with the multivalued logarithms represented explicitly in the PDF as

> **Log_b z = (logₑ z + 2mπi) / (logₑ b + 2nπi)**

The unit also gives

> **logₑ(a) = logₑ a + iπ**

for the logarithm of a negative real quantity as presented in the PDF.

### Derivation of the General Method

#### Step 1: Represent the logarithm

Let

> **Logₑ(x + iy) = α + iβ**

By the definition of the logarithm,

> **x + iy = e^(α + iβ)**

#### Step 2: Use the complex exponential form

> **x + iy = eᵅ eⁱᵝ**

> **x + iy = eᵅ(cos β + i sin β)**

#### Step 3: Match coefficients

Comparing the real and imaginary parts,

> **x = eᵅ cos β**

> **y = eᵅ sin β**

#### Step 4: Determine the real part

Square both equations and add them:

> **x² + y² = e²ᵅ cos² β + e²ᵅ sin² β**

Factor out e²ᵅ:

> **x² + y² = e²ᵅ(cos² β + sin² β)**

Use the identity cos² β + sin² β = 1:

> **x² + y² = e²ᵅ**

Take the logarithm:

> **log(x² + y²) = 2α**

Therefore,

> **α = 1/2 log(x² + y²)**

#### Step 5: Determine the imaginary part

Divide the imaginary-part equation by the real-part equation:

> **y/x = (eᵅ sin β)/(eᵅ cos β)**

Therefore,

> **y/x = tan β**

Thus, using the expression in the PDF,

> **β = tan⁻¹(y/x)**

#### Step 6: Include all possible arguments

The trigonometric functions are periodic with period 2π. Hence the argument can be changed by any integer multiple of 2π:

> **β = tan⁻¹(y/x) + 2nπ**

where n ∈ ℤ.

#### Step 7: Combine the two parts

Substituting α and β into α + iβ gives

> **Logₑ(x + iy) = 1/2 log(x² + y²) + i tan⁻¹(y/x) + 2nπi**

This is the general value of the logarithm according to the method developed in the PDF.

#### Principal Value

The principal value is obtained by taking the expression without the additional 2nπi term:

> **logₑ(x + iy) = 1/2 log(x² + y²) + i tan⁻¹(y/x)**

### Key Observations

| Situation | Expression or method | Purpose |
|---|---|---|
| Definition | z = eᵘ | Defines a logarithm of a complex quantity |
| Complex number | z = x + iy | Cartesian representation |
| Exponential representation | eᵅ(cos β + i sin β) | Separates magnitude and argument |
| Real part | 1/2 log(x² + y²) | Determines the real component of the logarithm |
| Imaginary part | tan⁻¹(y/x) | Determines the argument using the PDF's stated form |
| Principal value | No 2nπi term | Selects the principal logarithm represented in the unit |
| General value | Includes 2nπi | Represents the infinitely many logarithms |
| Base change | Log_b z = Logₑ z / Logₑ b | Converts logarithms between bases |
| Trigonometric form | cos θ + i sin θ | Allows direct use of trigonometric identities |

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

Leonhard Euler (1707–1783), *Introductio in analysin infinitorum* (1748) — developed foundational relationships between exponential and trigonometric functions used in complex analysis.

Abraham de Moivre (1667–1754), *Miscellanea Analytica* (1730) — established the theorem connecting powers of cos θ + i sin θ with multiple angles.

John Napier (1550–1617), *Mirifici Logarithmorum Canonis Descriptio* (1614) — introduced logarithms as a mathematical computational tool.

## Real-World Applications

### 1. Signal Processing

- Complex numbers provide a compact representation of oscillatory signals.
- Complex logarithms can separate magnitude-related and phase-related information.
- Arguments of complex quantities are useful when studying phase changes.
- Periodicity in the argument explains why multiple logarithmic values can occur.

**Example:** A periodic signal represented through a complex exponential can be analysed by separating its magnitude and phase.

### 2. Physics

- Complex exponentials are widely used to represent oscillatory physical quantities.
- Complex logarithms provide a way to recover magnitude and phase information from exponential representations.
- Multivalued arguments are relevant when quantities undergo rotations in the complex plane.
- Complex powers can be analysed through logarithms.

**Example:** A physical oscillation represented using a complex exponential can be converted into magnitude and phase components using the logarithmic representation.

### 3. Electrical Engineering

- Phasor methods represent sinusoidal electrical quantities using complex numbers.
- Magnitude and phase are naturally expressed through complex quantities.
- Complex logarithms can be used when manipulating complex powers and exponential relationships.
- The periodic nature of phase explains the appearance of integer multiples of 2π.

**Example:** A complex impedance can be represented in terms of magnitude and phase, and its logarithmic representation separates these two components.

### 4. Computer Graphics

- Rotations in two-dimensional graphics can be represented using complex numbers.
- The argument of a complex number describes an angular position.
- Complex exponentials provide a compact representation of planar rotations.
- Logarithmic representations can be used when manipulating complex powers.

**Example:** A planar rotation represented by cos θ + i sin θ can be interpreted through its complex argument.

### 5. Mechanical Engineering

- Vibrations and oscillations are commonly represented using sinusoidal functions.
- Complex representations simplify the analysis of periodic motion.
- Magnitude and phase are important when comparing oscillatory responses.
- Complex logarithms provide a mathematical tool for handling exponential representations of oscillations.

**Example:** A vibration response written using a complex exponential can be analysed in terms of its magnitude and phase.

### 6. Acoustics

- Sound signals can be represented using sinusoidal and complex-exponential descriptions.
- Phase is an important component of wave behaviour.
- Complex numbers provide a convenient representation of amplitude and phase.
- Complex logarithms can help analyse complex exponential relationships.

**Example:** A sound component represented by a complex sinusoidal expression can be interpreted through its magnitude and phase.

### 7. Numerical Analysis

- Complex logarithms occur when numerical methods manipulate complex powers.
- Multivalued logarithms must be considered when complex exponentiation is involved.
- The principal value provides a consistent single-valued choice for calculations.
- The general value identifies the complete set of logarithmic solutions.

**Example:** A numerical calculation involving a complex power can use the complex logarithm to transform the power into an exponential expression.

### 8. Astronomy and Wave Analysis

- Complex representations are useful for describing periodic and oscillatory phenomena.
- Magnitude and phase can describe different aspects of a complex signal.
- Complex exponentials simplify calculations involving repeated angular variation.
- Logarithms of complex quantities can be used when solving exponential relationships.

**Example:** A periodic astronomical signal represented through a complex exponential can be studied through its magnitude and phase.

### 9. Chemistry

- Complex numbers can occur in mathematical models involving oscillatory or wave-like behaviour.
- Complex exponentials provide a compact mathematical representation of periodic components.
- Complex logarithms provide a method for handling equations involving complex exponential quantities.
- The distinction between principal and general values is important when complex powers appear.

**Example:** A mathematical model containing a complex exponential can be transformed using the logarithmic relationship developed in this unit.

### 10. Music Theory and Audio Analysis

- Periodic musical signals can be represented using sinusoidal components.
- Complex numbers provide a convenient representation of amplitude and phase.
- The argument of a complex quantity represents angular information.
- Complex exponential notation simplifies the mathematical description of periodic signals.

**Example:** A periodic audio component represented as a complex sinusoidal quantity can be separated conceptually into magnitude and phase.

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
|---|---|---|---|
| Mathematical Foundation | If z = eᵘ, then u is called a logarithm of z | PDF | high |
| Mathematical Foundation | logₑ(x + iy) = 1/2 log(x² + y²) + i tan⁻¹(y/x) | PDF | high |
| Mathematical Foundation | General value includes 2nπi | PDF | high |
| Mathematical Foundation | Log_b z = Logₑ z / Logₑ b | PDF | high |
| Derivation | x = eᵅ cos β and y = eᵅ sin β | PDF | high |
| Derivation | x² + y² = e²ᵅ | PDF | high |
| Derivation | α = 1/2 log(x² + y²) | PDF | high |
| Derivation | y/x = tan β | PDF | high |
| Derivation | β = tan⁻¹(y/x) in the form used by the PDF | PDF | high |
| Historical Background | Euler, Introductio in analysin infinitorum (1748), contribution to exponential and trigonometric relationships | textbook-standard | high |
| Historical Background | De Moivre, Miscellanea Analytica (1730), contribution to powers of cos θ + i sin θ | textbook-standard | high |
| Historical Background | Napier, Mirifici Logarithmorum Canonis Descriptio (1614), contribution to logarithms | textbook-standard | high |
| Real-World Applications | Complex numbers can represent magnitude and phase in signal processing | inferred from standard mathematical use | high |
| Real-World Applications | Complex exponentials are used to represent oscillatory quantities in physics | inferred from standard mathematical use | high |
| Real-World Applications | Phasor methods use complex numbers in electrical engineering | inferred from standard mathematical use | high |
| Real-World Applications | Complex numbers can represent planar rotations in computer graphics | inferred from standard mathematical use | high |
| Real-World Applications | Complex representations are used in vibration analysis | inferred from standard mathematical use | high |
| Real-World Applications | Complex representations are useful in acoustics | inferred from standard mathematical use | high |
| Real-World Applications | Principal and general logarithms matter in numerical calculations involving complex powers | inferred from PDF concepts | high |
| Real-World Applications | Complex representations can describe periodic astronomical signals | inferred from standard mathematical use | high |
| Real-World Applications | Complex exponentials can occur in mathematical models involving wave-like chemical behaviour | inferred from standard mathematical use | high |
| Real-World Applications | Complex numbers provide magnitude and phase representations in audio analysis | inferred from standard mathematical use | high |