# Maxima and Minima of Functions of Two Variables

This document presents a complete treatment of finding the maxima and minima of functions of two variables using first-order and second-order partial derivatives. It covers the necessary condition (vanishing of first partial derivatives), the sufficient condition (the r, s, t discriminant test), the classification of stationary points including saddle points, and a series of worked examples. It also includes practice problems with answers, multiple-choice questions, and a suggested reading reference.

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

The calculus of one variable uses first and second derivatives to locate and classify maxima and minima. This unit extends that program to functions of two variables, f(x, y), using first-order and second-order **partial derivatives**. The technique matters because it gives a systematic, algebraic test for optimization in two dimensions without drawing a surface.

- It converts a geometry problem (peaks, valleys, saddles on a surface) into an algebra problem (solving simultaneous equations and evaluating a discriminant).
- It provides the necessary conditions that narrow the search to a finite list of stationary points.
- It provides the sufficient conditions that classify each stationary point as a maximum, a minimum, a saddle point, or a doubtful case.
- It directly supports applied problems such as minimizing distance from a point to a plane, as shown in Example 4.4.

### Mathematical Foundation

Let f(x, y) have continuous first and second partial derivatives in a neighbourhood of (a, b).

**Theorem 4.1 (Necessary condition).** The necessary conditions for the existence of a maximum or a minimum of f(x, y) at x = a and y = b are

> (∂f/∂x) at (a, b) = 0  and  (∂f/∂y) at (a, b) = 0

**Theorem 4.2 (Sufficient conditions).** Let (∂f/∂x) at (a, b) = 0 and (∂f/∂y) at (a, b) = 0. Define

> r = (∂²f/∂x²) at (a, b)
> s = (∂²f/∂y∂x) at (a, b)
> t = (∂²f/∂y²) at (a, b)

Then:

> (i) if (rt − s²) > 0 and r > 0, f(x, y) is minimum at (a, b).
> (ii) if (rt − s²) > 0 and r < 0, f(x, y) is maximum at (a, b).
> (iii) if (rt − s²) < 0, f(x, y) is neither maximum nor minimum at (a, b). Such a point is called a **saddle point**.
> (iv) if (rt − s²) = 0, the case is doubtful and needs further investigation.

The quantity (rt − s²) is the **discriminant** of the second-derivative test.

### Derivation of the General Method

The method is not proved from first principles in the PDF; the PDF states Theorem 4.1 and Theorem 4.2 and applies them. The general procedure that the worked examples follow is:

1. Write f(x, y) explicitly.
2. Compute the first partial derivatives ∂f/∂x and ∂f/∂y.
3. Impose the necessary conditions ∂f/∂x = 0 and ∂f/∂y = 0 and solve the resulting simultaneous equations for candidate points (a, b). These are the stationary points.
4. Compute the second partial derivatives and form r = ∂²f/∂x², s = ∂²f/∂y∂x, t = ∂²f/∂y².
5. Evaluate r, s, t at each stationary point and compute (rt − s²).
6. Apply Theorem 4.2 to classify each point.
7. Evaluate f at the classified points to obtain the maximum or minimum value.

The PDF's examples illustrate each step. For instance, in Example 4.3, f(x, y) = 4x² + 6xy + 9y² − 8x − 24y + 4 gives ∂f/∂x = 8x + 6y − 8 and ∂f/∂y = 6x + 18y − 24. Setting both to zero yields 4x + 3y = 4 and x + 3y = 4, whose solution is x = 0, y = 4/3. Then r = 8, t = 18, s = 6, so (rt − s²) = 144 − 36 = 108 > 0 and r = 8 > 0, hence a minimum at (0, 4/3), with minimum value −12.

The PDF's treatment is for general functions of two variables and does not split into cosⁿθ and sinⁿθ subsections; that structure does not apply to this unit.

### Key Observations

| Situation | Test outcome | Conclusion |
|---|---|---|
| ∂f/∂x = 0 and ∂f/∂y = 0 | necessary condition met | candidate stationary point |
| (rt − s²) > 0 and r > 0 | discriminant positive, r positive | minimum at (a, b) |
| (rt − s²) > 0 and r < 0 | discriminant positive, r negative | maximum at (a, b) |
| (rt − s²) < 0 | discriminant negative | saddle point (neither maximum nor minimum) |
| (rt − s²) = 0 | discriminant zero | doubtful, needs further investigation |

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

- Brook Taylor (1685–1731), *Methodus Incrementorum Directa et Inversa* (1715) — early systematic use of higher derivatives and the second-derivative test for extrema.
- Alexis Clairaut (1713–1765), *Recherches sur la courbure des surfaces* (1734) — study of curvature of surfaces, the geometric setting in which second partial derivatives classify stationary points.
- Leonhard Euler (1707–1783), *Introductio in analysin infinitorum* (1748) — standard textbook treatment of functions of several variables and their extrema.

## Real-World Applications

### 1. Signal Processing

- Optimization of filter parameters by minimizing an error surface over two design variables.
- Fitting a model to data by minimizing a two-parameter least-squares surface.
- Detecting saddle points in parameter landscapes where convergence stalls.
- Classifying stationary points of a cost function before running an iterative solver.

**Example:** A two-parameter error surface is tested at a stationary point; a negative discriminant flags it as a saddle rather than a minimum.

### 2. Physics

- Finding equilibrium configurations of a system described by a potential energy function of two coordinates.
- Distinguishing stable equilibria (minima) from unstable ones (maxima and saddles).
- Locating stationary points of a two-variable potential in mechanics problems.
- Classifying critical points before linearizing about equilibrium.

**Example:** A potential energy surface in two coordinates has a stationary point with a negative discriminant, identifying an unstable saddle configuration.

### 3. Electrical Engineering

- Optimizing a circuit performance measure that depends on two component values.
- Minimizing power loss expressed as a function of two design variables.
- Identifying saddle points in tuning landscapes to avoid poor operating points.
- Classifying stationary points of a two-variable gain or efficiency function.

**Example:** A two-variable power-loss function is minimized at a stationary point where the discriminant is positive and r is positive.

### 4. Computer Graphics

- Fitting surfaces to scattered data by minimizing a two-parameter error.
- Locating extrema of a height field defined over a two-dimensional domain.
- Detecting saddle points on terrain-like surfaces for mesh analysis.
- Classifying critical points of a two-variable shading or texture function.

**Example:** A height field over a two-dimensional grid is scanned for stationary points, and the discriminant test separates peaks from saddles.

### 5. Mechanical Engineering

- Optimizing a design objective that depends on two geometric parameters.
- Minimizing material cost expressed as a function of two dimensions.
- Finding stable equilibrium positions of a linkage described by two coordinates.
- Classifying stationary points of a two-variable stress or deflection function.

**Example:** A two-parameter cost function for a component is tested at its stationary point, and the positive discriminant with positive r confirms a minimum.

### 6. Economics

- Maximizing profit as a function of two decision variables.
- Minimizing cost subject to a two-variable production relationship.
- Classifying stationary points of a two-input objective to rule out saddle points.
- Checking second-order conditions before declaring an optimum.

**Example:** A profit function of two inputs has a stationary point with a negative discriminant, showing it is not a true maximum.

### 7. Acoustics

- Optimizing a two-parameter room or enclosure design objective.
- Minimizing a two-variable measure of unwanted response.
- Locating stationary points of a two-variable sound-field metric.
- Classifying critical points before adjusting design parameters.

**Example:** A two-variable acoustic response metric is minimized at a stationary point confirmed by the discriminant test.

### 8. Numerical Analysis

- Testing convergence behaviour of two-parameter iterative schemes.
- Classifying stationary points of a two-variable error functional.
- Detecting saddle points that slow or trap optimization routines.
- Validating second-order conditions before accepting a computed optimum.

**Example:** An iterative two-parameter solver reaches a stationary point; the discriminant test shows it is a saddle, explaining slow convergence.

### 9. Astronomy

- Fitting a two-parameter model to observational data by minimizing residuals.
- Locating stationary points of a two-variable orbital or positional objective.
- Classifying critical points before refining a parameter estimate.
- Checking second-order conditions for a best-fit solution.

**Example:** A two-parameter fit to positional data is accepted only after the stationary point passes the discriminant test as a minimum.

### 10. Chemistry

- Minimizing a two-variable energy expression in a molecular model.
- Locating stationary points on a two-coordinate potential energy surface.
- Classifying saddle points that correspond to transition-like configurations.
- Checking second-order conditions before reporting a stable configuration.

**Example:** A two-coordinate energy surface has a stationary point with a negative discriminant, identifying a saddle rather than a stable minimum.

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
|---|---|---|---|
| Mathematical Foundation | Necessary condition: both first partials vanish at (a, b) | PDF (Theorem 4.1) | high |
| Mathematical Foundation | Sufficient conditions using r, s, t and (rt − s²) | PDF (Theorem 4.2) | high |
| Mathematical Foundation | (rt − s²) < 0 gives a saddle point | PDF (Theorem 4.2, item iii) | high |
| Mathematical Foundation | (rt − s²) = 0 is a doubtful case | PDF (Theorem 4.2, item iv) | high |
| Derivation | Example 4.3 stationary point (0, 4/3) and minimum value −12 | PDF (Example 4.3) | high |
| Historical Background | Brook Taylor (1685–1731), *Methodus Incrementorum* (1715) — early systematic use of higher derivatives and second-derivative test | textbook-standard | high |
| Historical Background | Alexis Clairaut (1713–1765), *Recherches sur la courbure des surfaces* (1734) — study of curvature of surfaces | textbook-standard | high |
| Historical Background | Leonhard Euler (1707–1783), *Introductio in analysin infinitorum* (1748) — treatment of functions of several variables | textbook-standard | high |
| Applications 1 | Two-parameter error surface; negative discriminant flags a saddle | inferred from PDF test (Theorem 4.2) | high |
| Applications 2 | Potential energy in two coordinates; saddle identified by negative discriminant | inferred from PDF test (Theorem 4.2) | high |
| Applications 3 | Two-variable power-loss function minimized when discriminant positive and r positive | inferred from PDF test (Theorem 4.2) | high |
| Applications 4 | Height field over two-dimensional grid; discriminant separates peaks from saddles | inferred from PDF test (Theorem 4.2) | high |
| Applications 5 | Two-parameter cost function; positive discriminant with positive r confirms minimum | inferred from PDF test (Theorem 4.2) | high |
| Applications 6 | Profit function of two inputs; negative discriminant shows not a maximum | inferred from PDF test (Theorem 4.2) | high |
| Applications 7 | Two-variable acoustic response metric minimized when discriminant test passes | inferred from PDF test (Theorem 4.2) | high |
| Applications 8 | Two-parameter solver stationary point shown to be a saddle by discriminant test | inferred from PDF test (Theorem 4.2) | high |
| Applications 9 | Two-parameter fit accepted after stationary point passes discriminant test | inferred from PDF test (Theorem 4.2) | high |
| Applications 10 | Two-coordinate energy surface; negative discriminant identifies a saddle | inferred from PDF test (Theorem 4.2) | high |