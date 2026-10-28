# Total Differential and Partial Derivatives of Functions of Two Functions

This README summarizes the study notes on **total differentiation** and **partial derivatives of functions of two functions**. It covers the chain rule for total derivatives of a function of one or more variables, the derivative of implicit functions, and the transformation of partial derivatives under a change of variables (notably Cartesian to polar coordinates). The notes include worked examples, practice problems, and multiple-choice questions.

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

The **total differential** (or total derivative) extends the ordinary derivative to functions whose inputs themselves depend on other variables. It answers the question: if u = f(x, y, …) and each of x, y, … changes with t, how fast does u change with t?

- It provides a systematic **chain rule** for multi-variable functions, avoiding the error of treating x and y as independent when they are not.
- It enables differentiation of **implicit functions** F(x, y) = c without solving for y explicitly.
- It supports **change of variables** in partial differential equations, such as converting the Laplacian from Cartesian to polar coordinates.
- It is the foundation for later topics including directional derivatives, gradients, and the chain rule in vector calculus.

### Mathematical Foundation

**Total derivative of u = f(x, y) with x = g(t), y = h(t):**

> du/dt = (∂u/∂x)(dx/dt) + (∂u/∂y)(dy/dt)

**Total derivative of u = f(x, y, z) with x, y, z functions of t:**

> du/dt = (∂u/∂x)(dx/dt) + (∂u/∂y)(dy/dt) + (∂u/∂z)(dz/dt)

**Case where y is a function of x (Note 3.1):**

> du/dx = ∂u/∂x + (∂u/∂y)(dy/dx)

**Implicit functions F(x, y) = c:**

> ∂F/∂x + (∂F/∂y)(dy/dx) = 0
>
> dy/dx = − (∂F/∂x) / (∂F/∂y)

**Partial derivatives of a function of two functions (Section 3.2):** If u = f(x, y) and x, y are functions of s and t, then

> ∂u/∂s = (∂u/∂x)(∂x/∂s) + (∂u/∂y)(∂y/∂s)
>
> ∂u/∂t = (∂u/∂x)(∂x/∂t) + (∂u/∂y)(∂y/∂t)

### Derivation of the General Method

The general method follows from the **chain rule** for functions of several variables. We walk through the reasoning for the case u = f(x, y) with x = g(t), y = h(t).

**Step 1 — Increment u.** Give t a small increment Δt. Then x changes by Δx, y changes by Δy, and u changes by Δu.

**Step 2 — Linear approximation.** For a differentiable function f,

> Δu ≈ (∂u/∂x) Δx + (∂u/∂y) Δy

**Step 3 — Divide by Δt.**

> Δu/Δt ≈ (∂u/∂x)(Δx/Δt) + (∂u/∂y)(Δy/Δt)

**Step 4 — Take the limit Δt → 0.** Differentiability guarantees the approximation becomes exact in the limit:

> du/dt = (∂u/∂x)(dx/dt) + (∂u/∂y)(dy/dt)

This is the total differential coefficient of u with respect to t.

#### For functions of three variables

The same argument applies with three increments:

> Δu ≈ (∂u/∂x) Δx + (∂u/∂y) Δy + (∂u/∂z) Δz

Dividing by Δt and taking the limit gives

> du/dt = (∂u/∂x)(dx/dt) + (∂u/∂y)(dy/dt) + (∂u/∂z)(dz/dt)

#### For implicit functions

If F(x, y) = c, then the total derivative of the constant c with respect to x is zero:

> dF/dx = ∂F/∂x + (∂F/∂y)(dy/dx) = 0

Solving for dy/dx gives

> dy/dx = − (∂F/∂x) / (∂F/∂y)

#### For a function of two functions

If u = f(x, y) and x, y depend on s and t, treat s and t independently and apply the two-variable chain rule to each:

> ∂u/∂s = (∂u/∂x)(∂x/∂s) + (∂u/∂y)(∂y/∂s)
>
> ∂u/∂t = (∂u/∂x)(∂x/∂t) + (∂u/∂y)(∂y/∂t)

#### Worked example: Cartesian to polar coordinates

For z = f(x, y) with x = r cos θ, y = r sin θ:

> ∂x/∂r = cos θ, ∂x/∂θ = −r sin θ
>
> ∂y/∂r = sin θ, ∂y/∂θ = r cos θ
>
> ∂z/∂r = cos θ (∂z/∂x) + sin θ (∂z/∂y)
>
> ∂z/∂θ = −r sin θ (∂z/∂x) + r cos θ (∂z/∂y)

Squaring and adding:

> (∂z/∂r)² + (1/r²)(∂z/∂θ)² = (∂z/∂x)² + (∂z/∂y)²

This identity confirms that the squared gradient is invariant under rotation of coordinates.

### Key Observations

| Expansion / Formula Type | When It Applies | Key Equation |
|---|---|---|
| Total derivative in t (two variables) | u = f(x, y), x = g(t), y = h(t) | du/dt = (∂u/∂x)(dx/dt) + (∂u/∂y)(dy/dt) |
| Total derivative in t (three variables) | u = f(x, y, z), x, y, z functions of t | du/dt = (∂u/∂x)(dx/dt) + (∂u/∂y)(dy/dt) + (∂u/∂z)(dz/dt) |
| Total derivative in x (y depends on x) | u = f(x, y), y = y(x) | du/dx = ∂u/∂x + (∂u/∂y)(dy/dx) |
| Implicit function derivative | F(x, y) = c | dy/dx = − (∂F/∂x) / (∂F/∂y) |
| Partial derivatives of two functions | u = f(x, y), x = x(s, t), y = y(s, t) | ∂u/∂s = (∂u/∂x)(∂x/∂s) + (∂u/∂y)(∂y/∂s) |
| Polar coordinate transformation | x = r cos θ, y = r sin θ | (∂z/∂r)² + (1/r²)(∂z/∂θ)² = (∂z/∂x)² + (∂z/∂y)² |

## Historical Background

The PDF does not name historical sources; the following attributions are textbook-standard.

- **Gottfried Wilhelm Leibniz (1646–1716), Nova Methodus (1684)** — Introduced the differential notation and the chain rule for derivatives.
- **Leonhard Euler (1707–1783), Institutiones Calculi Differentialis (1755)** — Systematized partial differentiation and functions of several variables.
- **Alexis Clairaut (1713–1765), Recherches sur les courbes à double courbure (1734)** — Studied total differentials and mixed partial derivatives.

## Real-World Applications

The total differential and the chain rule for functions of several variables appear across many quantitative fields. Each subsection below describes conceptual uses only.

### 1. Signal Processing

- Models how a signal changes when its amplitude and phase parameters both vary with time.
- Supports sensitivity analysis of filters whose coefficients depend on multiple design parameters.
- Underlies automatic differentiation in modern signal-processing software.

**Example:** A signal amplitude modelled as a function of gain and delay expands its rate of change into a gain term plus a delay term.

### 2. Physics

- Converts equations of motion between coordinate systems (e.g., Cartesian to polar).
- Tracks how thermodynamic state functions change when pressure and temperature vary together.
- Relates rates of change in Lagrangian and Hamiltonian formulations.

**Example:** A particle's position expressed in polar coordinates transforms its velocity components through the chain rule.

### 3. Electrical Engineering

- Computes how power dissipation changes when both voltage and resistance vary.
- Supports small-signal analysis of circuits with interdependent components.
- Enables transformation of Maxwell's equations between coordinate systems.

**Example:** Power P = V²/R changes with time through both V(t) and R(t), requiring the total derivative.

### 4. Computer Graphics

- Transforms surface normals and gradients between object and world coordinates.
- Supports animation of objects whose position depends on multiple joint angles.
- Underlies texture mapping and shading computations in rendering pipelines.

**Example:** A vertex position defined through nested transformations is differentiated via the chain rule to find its screen-space velocity.

### 5. Mechanical Engineering

- Relates stress and strain rates when material properties vary with temperature and load.
- Supports kinematic analysis of linkages whose joint angles depend on a single drive parameter.
- Enables sensitivity analysis in optimal design.

**Example:** A linkage's end-effector position depends on several joint angles; its velocity follows from the total derivative.

### 6. Economics

- Computes how utility changes when multiple consumption goods vary with income.
- Supports comparative statics when equilibrium prices and quantities depend on a policy parameter.
- Underlies elasticity analysis with interdependent variables.

**Example:** Aggregate demand as a function of price and income is differentiated with respect to a tax parameter.

### 7. Acoustics

- Models how sound pressure changes with both source strength and medium properties.
- Supports room-acoustics simulations where boundary conditions depend on temperature.
- Relates wave propagation in media with spatially varying properties.

**Example:** Sound intensity as a function of source power and distance is differentiated when both vary with time.

### 8. Numerical Analysis

- Underlies error propagation when computed quantities depend on several rounded inputs.
- Supports automatic differentiation for gradient-based optimization.
- Enables sensitivity analysis of numerical solvers.

**Example:** The error in a computed function of several measured inputs is estimated via the total differential.

### 9. Astronomy

- Relates orbital elements when both time and gravitational parameters vary.
- Supports coordinate transformations between equatorial, ecliptic, and galactic frames.
- Enables uncertainty propagation in celestial mechanics.

**Example:** A star's apparent position depends on Earth's orbital motion and the star's proper motion; the total derivative combines both effects.

### 10. Chemistry

- Models reaction rates when both concentrations and temperature vary with time.
- Supports thermodynamic calculations with interdependent state variables.
- Enables sensitivity analysis of chemical equilibrium to multiple parameters.

**Example:** The rate of a reaction depending on two reactant concentrations and temperature is differentiated via the chain rule.

### 11. Geophysics

- Relates seismic wave speeds to pressure and temperature gradients in the Earth.
- Supports coordinate transformations in mapping and geodesy.
- Enables inversion of geophysical data with multiple dependent parameters.

**Example:** A gravity anomaly as a function of depth and density is differentiated when both vary along a profile.

### 12. Music Theory

- Models how perceived pitch changes when both frequency and temperament parameters vary.
- Supports synthesis of timbres where harmonic amplitudes depend on multiple controls.
- Enables transformation of tuning systems between coordinate representations.

**Example:** A synthesized tone's loudness depends on amplitude and envelope parameters; its rate of change follows the chain rule.

## Self-Audit

| Section | Claim | Evidence source (PDF / textbook-standard / inferred) | Confidence |
|---|---|---|---|
| Historical Background | Leibniz introduced differential notation and the chain rule in Nova Methodus (1684). | Textbook-standard | high |
| Historical Background | Euler systematized partial differentiation in Institutiones Calculi Differentialis (1755). | Textbook-standard | high |
| Historical Background | Clairaut studied total differentials and mixed partial derivatives in Recherches sur les courbes à double courbure (1734). | Textbook-standard | high |
| Applications 2 | A particle's position in polar coordinates transforms velocity components through the chain rule. | PDF (Section 3.2 derivation) | high |
| Applications 4 | A vertex position through nested transformations is differentiated via the chain rule. | Inferred (standard application of PDF identity) | high |
| Applications 5 | End-effector velocity follows from the total derivative of joint angles. | Inferred (standard application of PDF identity) | high |
| Applications 7 | Sound intensity as a function of source power and distance is differentiated when both vary with time. | Inferred (standard application of PDF identity) | high |
| Applications 9 | A star's apparent position depends on Earth's motion and proper motion; total derivative combines both. | Inferred (standard application of PDF identity) | high |
| Applications 10 | Reaction rate depending on two concentrations and temperature is differentiated via the chain rule. | Inferred (standard application of PDF identity) | high |
| Applications 12 | A synthesized tone's loudness depends on amplitude and envelope; rate of change follows chain rule. | Inferred (standard application of PDF identity) | high |