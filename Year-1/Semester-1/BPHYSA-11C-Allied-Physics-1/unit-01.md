# Simple Harmonic Motion and Lissajous Figures

## Table of Contents

1. [Overview](#overview)
2. [1.1 Simple Harmonic Motion](#11-simple-harmonic-motion)
3. [1.2 Composition of Two Simple Harmonic Motions in a Straight Line](#12-composition-of-two-simple-harmonic-motions-in-a-straight-line)
4. [1.3 Composition of Two Simple Harmonic Motions of Equal Time Period at Right Angles](#13-composition-of-two-simple-harmonic-motions-of-equal-time-period-at-right-angles)
5. [1.4 Experimental Method for Obtaining Lissajous Figures](#14-experimental-method-for-obtaining-lissajous-figures)
6. [1.5 Uses of Lissajous Figures](#15-uses-of-lissajous-figures)
7. [Some Examples of SHM](#some-examples-of-shm)
8. [Problem 1](#problem-1)
9. [Check Your Progress](#check-your-progress)
10. [Let Us Sum Up](#let-us-sum-up)
11. [Unit End Exercises](#unit-end-exercises)
12. [Answers to Check Your Progress](#answers-to-check-your-progress)
13. [Suggested Readings](#suggested-readings)
14. [Web Resources](#web-resources)
15. [History of the Topics](#history-of-the-topics)
16. [Practical Applications](#practical-applications)

## Overview

Any motion that repeats itself after regular intervals of time is known as a **periodic motion**.

If a body moves back and forth repeatedly about a mean position, it is said to possess **oscillatory motion**.

The oscillations can be expressed in terms of simple harmonic functions like sine or cosine function. A harmonic oscillation of constant amplitude and single frequency is called **simple harmonic motion (SHM)**.

This unit discusses simple harmonic motion and Lissajous' Figures.

## 1.1 Simple Harmonic Motion

Let P be a particle moving on the circumference of a circle of radius a with a uniform angular velocity omega (Fig. 1.1). O is the centre of the circle.

A perpendicular PM is drawn from the particle on the diameter YY' of the circle. As the particle P moves round the circle, the foot of the perpendicular M vibrates along the diameter YY'. Since the motion of P is uniform, the motion of M is periodic. As the particle P completes one revolution, the foot of the perpendicular M completes one vertical oscillation. The distance OM is called the **displacement** and denoted by y.

The particle moves from X to P, in time t.

angle POX = angle MPO = theta = omega t

From the triangle MPO:

sin theta = sin omega t = OM / a

OM = y = a sin omega t

OM is called the displacement of the vibrating particle.

The **displacement** of a vibrating particle at any instant can be defined as its distance from the mean position of rest.

The maximum displacement of a vibrating particle is called its **amplitude**.

Displacement = y = a sin omega t

Fig. 1.2 shows the changes in the displacement of a vibrating particle in one complete vibration.

Velocity, v = dy/dt = a omega cos omega t = omega sqrt(a^2 - y^2)

Acceleration = d^2y/dt^2 = -a omega^2 sin omega t = -omega^2 y

Thus, acceleration is directly proportional to displacement and directed towards a fixed point. This type of motion is called simple harmonic motion.

Following are the characteristics of simple harmonic motion:

(i) The motion is periodic.
(ii) The motion is along a straight line about the mean or equilibrium position.
(iii) The acceleration is proportional to displacement.
(iv) Acceleration is directed towards the mean or equilibrium position.

**Definition:**

If a particle moves in a straight line, so that its acceleration is always directed towards a fixed point on the line, and is proportional to its displacement from the fixed point, the particle is said to move with simple harmonic motion.

The equation can be written as:

d^2y/dt^2 + omega^2 y = 0

This is the **differential equation of S.H.M.**

The period = T = 2 pi / omega
The frequency = n = 1 / T = omega / (2 pi)

**Examples of S.H.M.**

1. The vertical oscillations of a spiral spring suspended from a rigid support, and loaded at the lower end. This is a linear type of S.H.M.
2. The vibrations of a simple pendulum. This is an angular type of S.H.M.

**Phase:** Consider a particle starting from S and moving on the circumference of a circle (Fig. 1.3). angle SOX = alpha. The particle moves from S to P in time t.

angle OPM = (omega t + alpha)

Displacement, y = a sin (omega t + alpha)

alpha is called the **initial phase** or **epoch** of the S.H.M.

The angle (omega t + alpha) is called the **phase** of the S.H.M.

## 1.2 Composition of Two Simple Harmonic Motions in a Straight Line

The two simple harmonic vibrations are represented by the equations:

y1 = a1 sin (omega t + alpha1)
y2 = a2 sin (omega t + alpha2)

The y1 and y2 are the displacements of a particle due to the two vibrations. a1 and a2 are the amplitudes of the two vibrations. alpha1 and alpha2 are the epoch angles. The angular frequency omega is the same for both vibrations.

The resultant displacement y of the particle is given by:

y = y1 + y2
y = a1 sin (omega t + alpha1) + a2 sin (omega t + alpha2)
y = a1 (sin omega t cos alpha1 + cos omega t sin alpha1) + a2 (sin omega t cos alpha2 + cos omega t sin alpha2)
y = (a1 cos alpha1 + a2 cos alpha2) sin omega t + (a1 sin alpha1 + a2 sin alpha2) cos omega t ... (3)

We can write the displacement of the resultant motion as:

y = A sin (omega t + phi)
y = A sin omega t cos phi + A cos omega t sin phi ... (4)

A is the amplitude of the resultant motion and phi is the initial phase.

Equating the coefficients of sin omega t and cos omega t in Eqs (3) and (4):

A cos phi = a1 cos alpha1 + a2 cos alpha2 ... (5)
A sin phi = a1 sin alpha1 + a2 sin alpha2 ... (6)

Squaring Eqs. (5) and (6) and adding:

[Note: The source PDF contains a garbled intermediate step on Page 6. The standard result follows.]

A^2 = a1^2 + a2^2 + 2 a1 a2 cos (alpha1 - alpha2) ... (7)

Dividing equation (6) by (5):

tan phi = (a1 sin alpha1 + a2 sin alpha2) / (a1 cos alpha1 + a2 cos alpha2) ... (8)

Equations (7) and (8) give the values of A and phi.

A = sqrt(a1^2 + a2^2 + 2 a1 a2 cos (alpha1 - alpha2))

phi = tan^-1 [ (a1 sin alpha1 + a2 sin alpha2) / (a1 cos alpha1 + a2 cos alpha2) ]

## 1.3 Composition of Two Simple Harmonic Motions of Equal Time Period at Right Angles

Suppose the same particle is simultaneously subjected to two SHM motions along two mutually perpendicular directions (X and Y axes).

Let the displacements of the SHM be:

x = a sin (omega t + alpha) ... (1)
y = b sin omega t ... (2)

alpha = the phase difference between the two SHM.

The resultant motion is obtained by eliminating t from (1) and (2). From equation (2):

sin omega t = y / b
cos omega t = sqrt(1 - y^2 / b^2)

From Eqn (1):

x / a = [ sin omega t cos alpha + cos omega t sin alpha ] ... (3)

x / a = [ (y / b) cos alpha + sqrt(1 - y^2 / b^2) sin alpha ]

x / a - (y / b) cos alpha = sqrt(1 - y^2 / b^2) sin alpha

Squaring both sides:

x^2 / a^2 - (y^2 / b^2) cos^2 alpha - (2xy / ab) cos alpha = (1 - y^2 / b^2) sin^2 alpha

x^2 / a^2 - (y^2 / b^2) [ sin^2 alpha - cos^2 alpha ] - (2xy / ab) cos alpha = sin^2 alpha

[Note: The source PDF contains an apparent sign/grouping error in this step. The standard result is x^2/a^2 + y^2/b^2 - (2xy/ab) cos alpha = sin^2 alpha.]

x^2 / a^2 + y^2 / b^2 - (2xy / ab) cos alpha = sin^2 alpha

This represents the general equation of an ellipse and hence the resultant motion is in general elliptical.

**Special cases:**

(i) If alpha = 0, cos alpha = 1, sin alpha = 0:

x / a - y / b = 0

This represents a straight line AB (Fig. 1.4) of slope b / a.

(ii) If alpha = pi / 2:

x^2 / a^2 + y^2 / b^2 = 1

This represents an ellipse EFGH whose major and minor axes coincide with the coordinate axes.

(iii) If alpha = pi / 2 and a = b, then:

x^2 + y^2 = a^2

This represents a circle of radius a. Hence, the resultant motion is circular.

**Lissajous Figures:**

When a particle is acted upon simultaneously by two S.H. motions at right angles to each other, the resultant path traced by the particle is called **Lissajous figures**.

The shape of the Lissajous Figure depends upon:

(i) The amplitudes.
(ii) The periods of the two component motions.
(iii) The phase difference between them.

## 1.4 Experimental Method for Obtaining Lissajous' Figures

Lissajous figures can be demonstrated using a Cathode Ray Oscillograph. Sinusoidal signals from two audio oscillators are simultaneously applied across the XX and YY plates. The motion of the electron will be the resultant of two S.H. motions at right angles. The spot of light then traces out a Lissajous figure on the screen. The frequency of one oscillator is kept fixed and the frequency of the other altered. The pattern for any desired frequency ratio can be obtained on the screen.

## 1.5 Uses of Lissajous Figures

1. The form of a Lissajous figure enables us to determine the ratio of the time periods of component vibrations. From the Lissajous figure, the number of times the curve touches the horizontal and the vertical sides of a rectangle bounding the Lissajous figure is found. If the curve touches the horizontal side p times and the vertical side q times, the ratio of the time periods is p : q.

2. The Lissajous figures are used for the accurate determination of the frequency of a tuning fork.

3. Lissajous figures are used in obtaining beautiful designs for calico printing in the textile industry.

## Some Examples of SHM

(i) Horizontal and vertical oscillations of a loaded spring.
(ii) Vertical oscillation of water in a U-tube.
(iii) Oscillations of a floating cylinder.
(iv) Oscillations of a simple pendulum.
(v) Vibrations of the prongs of a tuning fork.

## Problem 1

The S.H.M. of a particle is given by the equation y = 3 sin omega t + 4 cos omega t. The amplitude is:

**Solution:**

Resultant amplitude

[Note: Source PDF content on Page 10 was corrupted/incomplete. The solution is incomplete in the source.]

## Check Your Progress

1. Give the definition of SHM — simple harmonic motion.
2. Arrive at the differential equation representing SHM.
3. Define frequency of SHM.
4. What do you mean by initial phase or epoch of SHM or phase of SHM?
5. Discuss the compositions of two SHMs at equal time periods at right angles. Obtain expression and discuss special cases.
6. What are Lissajous's figures? What are its uses?

## Let Us Sum Up

Let us now summarize what you have studied in this unit:

- The simple harmonic motion is defined as oscillatory motion about a fixed point in which the restoring force is always proportional to the displacement and directed always towards that fixed point.
- Velocity = v = dy/dt = a omega cos omega t = omega sqrt(a^2 - y^2)
- Acceleration = d^2y/dt^2 = -a omega^2 sin omega t = -omega^2 y
- When a particle is acted upon simultaneously by two S.H. motions at right angles to each other, the resultant path traced by the particle is called Lissajous figures.

## Unit End Exercises

1. Give the definition of SHM — simple harmonic motion.
2. Arrive at the differential equation representing SHM.
3. Define frequency of SHM.
4. What do you mean by initial phase or epoch of SHM or phase of SHM?
5. Discuss the compositions of two SHMs at equal time periods at right angles. Obtain expression and discuss special cases.
6. What are Lissajous's figures? What are its uses?

## Answers to Check Your Progress

1. T = 2 pi / omega
2. Air friction

[Note: The source PDF only provides answers to two items; the remaining answers are not present in the source.]

## Suggested Readings

1. Allied Physics by R. Murugesan, S. Chand & Co, New Delhi (2008).
2. Allied Physics by K. Thangaraj and D. Jayaraman, Popular Book Depot Chennai (2004).
3. Modern Physics by R. Murugesan, S. Chand & Co, New Delhi (2005).
4. Concepts of Modern Physics by A. Beiser, Tata McGraw Hill Publication, New Delhi (1997).
5. Fundamentals of Physics by Resnick Halliday and Walker, John Wiley and Sons, Asia Pvt. Ltd., 6th edition, Singapore.

## Web Resources

1. Simple harmonic motion - https://www.youtube.com/watch?v=puid7oFvO-8
2. Composition of 2 SHM in straight line - https://www.youtube.com/watch?v=yxJXREddKd8
3. Composition of two SHM at right angles - https://www.youtube.com/watch?v=-tcWmw2Ktok
4. Lissajous figure - https://www.youtube.com/watch?v=xrejP8ZG9Hs

## History of the Topics

**Simple Harmonic Motion.** The study of periodic and oscillatory motion has roots in antiquity, but the mathematical treatment of simple harmonic motion emerged gradually. Galileo Galilei (1564-1642) observed the isochronism of the pendulum around 1583 and used it for timing; however, the precise sinusoidal description of displacement was not available to him. Christiaan Huygens (1629-1695) analyzed the pendulum clock and the cycloidal pendulum in the 1650s-1670s, and his work helped establish the period relationship for small oscillations. The differential equation form d^2y/dt^2 + omega^2 y = 0 and the recognition that acceleration is proportional to displacement and directed toward a fixed point developed through the 17th and 18th centuries, with major contributions from Isaac Newton (1642-1727) in the Principia (1687) and later from Leonhard Euler (1707-1783) and Jean le Rond d'Alembert (1717-1783), who developed systematic methods for solving linear differential equations. The term "simple harmonic motion" came into standard use in the 18th and 19th centuries. The projection of uniform circular motion onto a diameter, used in this unit as a geometric introduction, was a standard pedagogical device in 18th- and 19th-century mechanics texts.

**Composition of Simple Harmonic Motions.** The superposition of two simple harmonic motions along the same line follows from the trigonometric addition formulas and was well understood by the 18th century. The composition of two perpendicular simple harmonic motions of equal period was also studied in the 18th and early 19th centuries as a problem in analytic geometry. The general result that the path is an ellipse (including the special cases of a straight line and a circle) was known to mathematicians such as Euler and others working on celestial mechanics and vibrating systems.

**Lissajous Figures.** The experimental study of the curves formed by two perpendicular vibrations is associated with Jules Antoine Lissajous (1822-1880), a French physicist. In the 1850s he developed optical methods to superimpose two vibrations at right angles and observe the resulting patterns. His name became attached to these figures. Independent work on related curves was done by Nathaniel Bowditch (1773-1838) in the United States in the 1810s, and the curves are sometimes called Bowditch curves, especially in older American literature. The cathode-ray oscilloscope, developed in the late 19th and early 20th centuries (with important contributions by Ferdinand Braun in 1897 and later improvements), became a standard laboratory instrument for displaying Lissajous figures, as described in this unit. The use of Lissajous figures for frequency comparison and tuning-fork calibration became common in physics laboratories in the early 20th century.

[Note: Dates for Lissajous' original publications are often given as the 1850s; specific years vary by source, and the exact first publication date is not stated here with certainty.]

## Practical Applications

### Applications Based on Simple Harmonic Motion (SHM)

1. **Pendulum clocks.** The regular oscillation of a pendulum about its equilibrium position is approximately simple harmonic for small angles. This principle was used by Huygens and others to regulate clock mechanisms.
2. **Quartz oscillators and quartz clocks.** A quartz crystal vibrating in a stable elastic mode executes SHM; its precise frequency is used as a time standard in watches, computers, and laboratory instruments.
3. **Loaded spring oscillations (mass-spring systems).** Vertical or horizontal oscillations of a mass attached to a spring are linear SHM. These are used in vibration isolation mounts, spring balances, and suspension systems.
4. **Tuning forks and musical instruments.** The prongs of a tuning fork vibrate with SHM-like motion and produce a nearly pure tone. This is used for tuning instruments and for frequency standards.
5. **U-tube liquid oscillations.** The vertical oscillation of a liquid column in a U-tube is approximately SHM. This principle appears in some flow meters and in demonstrations of SHM.
6. **Floating cylinder oscillations.** A floating object displaced vertically and released oscillates with SHM. This is used in some hydrometers and buoyancy-based sensors.
7. **Seismometers.** Many seismometer designs use a mass-spring or pendulum system whose response to ground motion is analyzed in terms of SHM and damped harmonic motion.
8. **Accelerometers (spring-mass type).** A proof mass on a spring undergoes displacement proportional to acceleration; the dynamics are governed by the SHM equation.
9. **Vibration isolation tables.** Optical tables and precision instruments use spring and damper systems designed according to SHM theory to isolate vibrations.
10. **Galvanometers and moving-coil meters.** The coil in many analog meters undergoes damped oscillatory motion about its equilibrium position, described by SHM with damping.
11. **Torsional pendulum in clocks and instruments.** A disk suspended by a wire executes angular SHM; this is used in torsion pendulums for measuring moments of inertia and in some clock escapements.
12. **Molecular vibrations (simple models).** The vibration of diatomic molecules about their equilibrium bond length is often modeled as SHM in introductory physics; infrared spectroscopy of such vibrations is used in chemical analysis.

### Applications Based on Composition of Two SHMs in a Straight Line

1. **Interference of sound waves (same line, same frequency).** Two sound waves traveling along the same direction with the same frequency combine to give a resultant amplitude that depends on their phase difference, exactly as in the composition of two collinear SHMs.
2. **Interference of light (two-beam interference).** The superposition of two coherent light waves along the same path produces a resultant amplitude given by the same vector addition of amplitudes.
3. **AC circuit analysis (phasor addition).** Two alternating voltages or currents in series add as collinear SHMs; phasor diagrams use the same amplitude and phase formulas.
4. **Beat phenomenon (slightly different frequencies).** When two collinear SHMs have nearly equal frequencies, the resultant amplitude varies periodically; this is used in tuning musical instruments and in radio receivers.
5. **Vibration testing and modal analysis.** When two harmonic excitations act along the same axis on a structure, the resultant motion is computed by the same superposition formulas.
6. **Noise-cancelling headphones (collinear superposition).** An anti-phase sound wave is added to the ambient noise along the same path, reducing the resultant amplitude by destructive interference.
7. **Active vibration control.** Sensors and actuators add a secondary vibration to cancel an unwanted vibration along the same axis, based on superposition of collinear SHMs.
8. **Audio mixing and signal summation.** Electrical signals from multiple sources add linearly; the resultant amplitude and phase follow the same trigonometric combination rules.
9. **Seismic wave superposition along a ray path.** Two harmonic components traveling along the same path can reinforce or cancel depending on phase.
10. **Phase-locked loops (PLL) in electronics.** The phase detector compares two signals and the loop adjusts one to maintain a fixed phase relationship; the underlying mathematics is the superposition of two harmonic signals.

### Applications Based on Composition of Two SHMs at Right Angles (Lissajous Figures and Elliptical Motion)

1. **Cathode-ray oscilloscope (CRO) for frequency and phase measurement.** Applying two sinusoidal signals to the X and Y plates produces Lissajous figures used to compare frequencies and measure phase difference, as described in the unit.
2. **Tuning-fork frequency determination.** A Lissajous figure formed between a known oscillator and a tuning fork allows accurate determination of the fork's frequency.
3. **Calibration of audio oscillators.** By comparing an unknown oscillator frequency with a reference using Lissajous patterns, the unknown frequency is determined.
4. **Radio and communications engineering (phase comparison).** Lissajous figures were historically used to compare phases of signals in radio transmitters and receivers.
5. **Textile design and calico printing.** Lissajous figures are used to generate repeating ornamental patterns for fabric printing, as noted in the unit.
6. **Vectorcardiograms and medical displays.** In some medical instrumentation, two perpendicular signals (e.g., from orthogonal leads) are displayed as a Lissajous-like loop to show phase relationships.
7. **Polarization of light (elliptical and circular polarization).** Two perpendicular electric field oscillations with a phase difference produce elliptical or circular polarization; this is the same mathematical composition as perpendicular SHMs.
8. **Antenna radiation patterns and polarization diversity.** The superposition of two orthogonal antenna currents with a phase difference produces elliptical or circular polarization, used in satellite and mobile communications.
9. **Vibration analysis of rotating machinery.** The two orthogonal components of vibration of a rotating shaft can be displayed as a Lissajous figure (orbit plot) to diagnose unbalance and misalignment.
10. **Optical beam steering and laser scanning.** Two orthogonal harmonic deflections of a beam (e.g., by galvanometer mirrors) produce a two-dimensional scan pattern; the resulting path is a Lissajous figure.
11. **Particle traps and ion traps (RF fields).** Oscillating electric fields in orthogonal directions can create stable trajectories for charged particles; the stability analysis uses the mathematics of perpendicular oscillatory fields.
12. **Seismology (particle motion diagrams).** Two horizontal components of ground motion plotted against each other produce Lissajous-like particle motion diagrams used to identify wave types.
13. **Quantum optics and atomic physics (cavity QED).** The interaction of a two-level atom with a cavity field can be described by coupled oscillatory equations whose phase-space trajectories resemble Lissajous figures.
14. **Mechanical drawing machines (harmonographs).** A harmonograph uses two pendulums oscillating at right angles to draw Lissajous figures; these were popular in the 19th century and are still used for art and education.

### Applications Based on Lissajous Figures and Phase Measurement

1. **Frequency ratio measurement.** The number of tangencies of a Lissajous figure to the bounding rectangle gives the ratio of frequencies, as stated in the unit.
2. **Phase difference measurement.** The shape of the Lissajous figure indicates the phase difference between two signals; this is used in laboratory phase meters.
3. **Impedance measurement (Lissajous method).** In AC bridge and impedance measurements, Lissajous figures can be used to determine phase angles.
4. **Testing of audio equipment.** Lissajous figures on an oscilloscope are used to check channel balance and phase in stereo systems.
5. **Servo system alignment.** In control systems, Lissajous figures can show the phase relationship between input and output signals for alignment.
6. **Vibration diagnostics in rotating machines.** Orbit plots (Lissajous figures) of shaft vibration are used to detect unbalance, misalignment, and rub.
7. **Sonar and radar signal comparison.** Historically, Lissajous figures were used to compare phases of transmitted and received signals.
8. **Educational demonstrations.** Lissajous figures are widely used in physics teaching to illustrate superposition, phase, and frequency ratios.
9. **Art and design.** Lissajous curves are used in graphic design, animation, and generative art based on harmonic motion.
10. **Laser show scanning.** Two orthogonal oscillating mirrors driven at different frequencies produce Lissajous patterns for laser light shows.

[Note: Some applications listed above go beyond those explicitly mentioned in the PDF, as permitted by the task. They are included only where the connection to the physics of SHM, superposition, and perpendicular composition is direct and well established.]