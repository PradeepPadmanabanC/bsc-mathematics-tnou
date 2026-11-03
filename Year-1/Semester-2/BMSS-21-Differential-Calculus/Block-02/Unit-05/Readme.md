# Constrained Maxima and Minima: Lagrange Multipliers

This README summarizes the study notes on **constrained optimization** using the **method of Lagrange multipliers**. The notes cover the theoretical foundation of the method, worked examples involving functions of two and three variables subject to equality constraints, and applications to geometry and practical optimization problems. The goal is to help undergraduate students understand how to locate extrema of a function when its variables are restricted by one or more constraint equations.

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

The method of **Lagrange multipliers** provides a systematic way to find the maxima and minima of a function whose inputs are constrained by an equality relation. Rather than solving the constraint for one variable and substituting (which can be messy or impossible), the method introduces an auxiliary variable (the multiplier λ) and converts the constrained problem into an unconstrained stationary-point problem for a new function F.

- It converts a constrained optimization problem into a system of algebraic equations.
- It handles constraints that are difficult or impossible to solve explicitly for one variable.
- It generalizes naturally from two variables to any number of variables and constraints.
- It is the standard tool behind many applied optimization models in engineering, economics, and physics.

### Mathematical Foundation

Suppose f(x, y) is to be maximized or minimized subject to the constraint g(x, y) = 0. The method forms the **Lagrangian** function:

> F(x, y, λ) = f(x, y) − λ g(x, y)

where λ is the **Lagrange multiplier**, treated as independent of x and y. The necessary conditions for a stationary point are:

> ∂F/∂x = 0, ∂F/∂y = 0, ∂F/∂λ = 0

For three variables with constraint g(x, y, z) = 0, the same structure applies:

> F(x, y, z, λ) = f(x, y, z) − λ g(x, y, z)

> ∂F/∂x = 0, ∂F/∂y = 0, ∂F/∂z = 0, ∂F/∂λ = 0

The constraint equation is recovered from ∂F/∂λ = 0. The method yields **candidate points**; comparison of function values at candidates (and at boundary points satisfying the constraint) determines which are maxima or minima.

### Derivation of the General Method

The method is built on the idea of **coefficient matching** in the differential of f along the constraint surface. Below is the step-by-step reasoning for the general case with one constraint.

#### General case: one constraint

Start with the objective f(x, y) and constraint g(x, y) = 0.

> Step 1: Along the constraint curve, the differential of g vanishes: dg = gₓ dx + gᵧ dy = 0.

> Step 2: At an extremum of f on the constraint, the differential of f also vanishes: df = fₓ dx + fᵧ dy = 0.

> Step 3: The two linear relations in dx and dy must hold simultaneously, so the gradients are proportional: (fₓ, fᵧ) = λ (gₓ, gᵧ) for some scalar λ.

> Step 4: Rearranging gives fₓ − λ gₓ = 0 and fᵧ − λ gᵧ = 0.

> Step 5: Together with g(x, y) = 0, these are exactly the conditions ∂F/∂x = 0, ∂F/∂y = 0, ∂F/∂λ = 0 for F = f − λ g.

#### For cosⁿθ and sinⁿθ expansions (note)

The PDF for this unit does not treat trigonometric power expansions; it focuses on the multiplier method itself. No derivation for cosⁿθ or sinⁿθ appears in the source, so that subsection is not applicable here.

### Key Observations

| Situation | Form of Lagrangian | Conditions to solve | When to use |
|---|---|---|---|
| Two variables, one constraint | F = f(x, y) − λ g(x, y) | Fₓ = 0, Fᵧ = 0, Fλ = 0 | Constraint g(x, y) = 0 is simple or implicit |
| Three variables, one constraint | F = f(x, y, z) − λ g(x, y, z) | Fₓ = 0, Fᵧ = 0, Fz = 0, Fλ = 0 | Geometric or volume/surface constraints |
| Constraint has reciprocals | F = f − λ g with g containing 1/x terms | Differentiate carefully; solve for λ first | Problems like 1/x + 1/y + 1/z = 1 |
| Multiple candidate points | Same Lagrangian | Solve system, then compare f values | When the system yields more than one point |

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

- Joseph-Louis Lagrange (1736–1813), *Mécanique analytique* (1788) — introduced the method of undetermined multipliers for constrained problems in mechanics.
- Leonhard Euler (1707–1783), *Methodus inveniendi lineas curvas* (1744) — developed early variational techniques that motivated multiplier methods.
- Pierre-Simon Laplace (1749–1827), *Traité de mécanique céleste* (1799) — applied multiplier techniques to constrained problems in celestial mechanics.

## Real-World Applications

The method of Lagrange multipliers is used across many fields wherever an objective must be optimized under an equality constraint. Below are conceptual uses in ten distinct fields.

### 1. Signal Processing

- Designing filters that minimize error energy subject to a fixed gain constraint at a specified frequency.
- Allocating power across subchannels to maximize total capacity under a total-power equality constraint.
- Fitting signal models whose parameters must satisfy a normalization condition.
- Constrained beamforming where weights must satisfy a unit-response constraint in a look direction.

**Example:** A filter design problem where the sum of squared tap weights is held fixed while the stopband energy is minimized.

### 2. Physics

- Finding equilibrium configurations of a system that minimize potential energy subject to geometric constraints.
- Maximizing entropy of a statistical distribution subject to fixed mean energy and fixed particle number.
- Determining normal modes of a constrained mechanical system.
- Optimizing thermodynamic potentials under fixed volume or fixed pressure conditions.

**Example:** A particle constrained to move on a curved surface reaches equilibrium where the potential energy is stationary along the surface.

### 3. Electrical Engineering

- Minimizing power loss in a resistive network subject to Kirchhoff-type equality constraints.
- Designing matching networks that maximize power transfer under a fixed reactance constraint.
- Optimal dispatch of generators to minimize cost subject to a total-demand equality constraint.
- Constrained parameter estimation in circuit models.

**Example:** A generator dispatch problem where total output must equal total demand while cost is minimized.

### 4. Computer Graphics

- Fitting smooth curves and surfaces through control points with tangent or curvature constraints.
- Computing constrained deformations of meshes where certain vertices are pinned.
- Optimizing lighting parameters subject to a fixed total energy budget.
- Shape optimization under volume-preservation constraints.

**Example:** A mesh deformation where selected vertices are fixed and the remaining vertices move to minimize elastic energy.

### 5. Mechanical Engineering

- Designing a structure of minimum weight subject to a stress or deflection constraint.
- Optimizing gear ratios under a fixed overall speed-ratio constraint.
- Finding the dimensions of a container that maximize volume for a fixed surface area.
- Constrained trajectory planning for robot arms with joint-limit equalities.

**Example:** A rectangular box without a lid is built from a fixed amount of cardboard; the dimensions that maximize volume are found using one equality constraint on surface area.

### 6. Economics

- Maximizing utility subject to a budget constraint (the classic consumer problem).
- Minimizing cost of production subject to a required output level.
- Portfolio optimization where expected return is maximized for a fixed level of risk.
- Constrained resource allocation across competing uses.

**Example:** A consumer chooses quantities of goods to maximize utility while total expenditure equals income.

### 7. Acoustics

- Designing loudspeaker enclosures that maximize low-frequency output under a fixed volume constraint.
- Optimizing microphone array weights subject to a distortionless-response constraint.
- Constrained room-mode optimization for a fixed room volume.
- Minimizing sound transmission subject to a mass constraint on the partition.

**Example:** An array of microphones is weighted to preserve sound from one direction while suppressing noise, under a unit-gain constraint.

### 8. Numerical Analysis

- Solving constrained least-squares problems where parameters must satisfy linear equalities.
- Computing projections onto constraint manifolds.
- Deriving optimal step sizes in constrained iterative solvers.
- Sensitivity analysis of optimization problems via the multiplier values.

**Example:** A least-squares fit where the fitted parameters are required to sum to a fixed value.

### 9. Astronomy

- Determining orbits that minimize energy subject to a fixed angular momentum.
- Constrained fitting of celestial-mechanics models to observations.
- Optimizing telescope scheduling under fixed observing-time constraints.
- Computing equilibrium shapes of rotating bodies under a fixed volume constraint.

**Example:** An orbit is adjusted to minimize fuel use while keeping the orbital period fixed.

### 10. Chemistry

- Minimizing the free energy of a reacting mixture subject to element-balance constraints.
- Optimizing molecular geometries under fixed bond-length or angle constraints.
- Constrained fitting of kinetic parameters to concentration data.
- Designing mixtures that maximize yield subject to stoichiometric equalities.

**Example:** Equilibrium concentrations in a reacting system are found by minimizing free energy while conserving each element.

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
|---|---|---|---|
| Historical Background | Lagrange introduced the method of undetermined multipliers in *Mécanique analytique* (1788) | textbook-standard | high |
| Historical Background | Euler developed early variational techniques in *Methodus inveniendi* (1744) | textbook-standard | high |
| Historical Background | Laplace applied multiplier techniques in *Traité de mécanique céleste* (1799) | textbook-standard | high |
| Mathematical Foundation | F(x, y, λ) = f(x, y) − λ g(x, y) and the three stationarity conditions | PDF | high |
| Derivation | Gradient proportionality (fₓ, fᵧ) = λ (gₓ, gᵧ) along the constraint | textbook-standard | high |
| Key Observations | Lagrangian forms and conditions for two- and three-variable cases | PDF | high |
| Applications 1–10 | Conceptual uses only; no numerical coefficients or frequencies attached | inferred (standard applications) | high |
| Applications 5 Example | Box without lid: maximize volume under fixed surface area | PDF (Example 5.7) | high |
| Applications 6 Example | Consumer utility maximization under budget constraint | textbook-standard | high |
| Applications 10 Example | Free-energy minimization with element-balance constraints | textbook-standard | high |