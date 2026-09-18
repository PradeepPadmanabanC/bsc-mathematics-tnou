"""
Interactive 3D visualization of f(z) = z^3 - 7z^2 + 17z - 11 over the complex plane.

Opens in your browser. Drag to rotate, scroll to zoom, hover to see values.

Base (x, y) plane = z = x + iy (Re, Im).
Height (z-axis)   = |f(z)|.
Roots are where the surface touches down to 0.

Roots (from factoring (x - 1)(x^2 - 6x + 11) = 0):
  z1 = 1
  z2 = 3 + i*sqrt(2)
  z3 = 3 - i*sqrt(2)
"""

import numpy as np
import plotly.graph_objects as go

# ---- Define the cubic and its roots ----
def f(z):
    return z**3 - 7*z**2 + 17*z - 11

roots = [1 + 0j, 3 + 1j*np.sqrt(2), 3 - 1j*np.sqrt(2)]

# ---- Build a grid over the complex plane ----
re = np.linspace(-1, 5, 250)
im = np.linspace(-3, 3, 250)
Re, Im = np.meshgrid(re, im)
Z = Re + 1j * Im

F = f(Z)
mag = np.abs(F)
mag_clipped = np.clip(mag, 0, 40)  # clip so far corners don't dwarf the roots region

# ---- Build the figure ----
fig = go.Figure()

# Surface
fig.add_trace(go.Surface(
    x=Re, y=Im, z=mag_clipped,
    colorscale='Viridis',
    opacity=0.9,
    colorbar=dict(title='|f(z)|'),
    name='|f(z)|',
    hovertemplate='Re(z): %{x:.2f}<br>Im(z): %{y:.2f}<br>|f(z)|: %{z:.2f}<extra></extra>'
))

# Root markers + vertical guide lines
for r in roots:
    label = f"{r.real:.2f}{'+' if r.imag >= 0 else '-'}{abs(r.imag):.2f}i"
    fig.add_trace(go.Scatter3d(
        x=[r.real, r.real], y=[r.imag, r.imag], z=[0, 40],
        mode='lines',
        line=dict(color='red', width=3, dash='dash'),
        showlegend=False,
        hoverinfo='skip'
    ))
    fig.add_trace(go.Scatter3d(
        x=[r.real], y=[r.imag], z=[0],
        mode='markers+text',
        marker=dict(size=6, color='red', line=dict(color='black', width=1)),
        text=[label],
        textposition='top center',
        textfont=dict(size=12, color='black'),
        name=f'root {label}',
        hovertemplate=f'root: {label}<extra></extra>'
    ))

fig.update_layout(
    title='f(z) = z³ − 7z² + 17z − 11  —  roots where surface meets 0',
    scene=dict(
        xaxis_title='Re(z)',
        yaxis_title='Im(z)',
        zaxis_title='|f(z)|',
        aspectratio=dict(x=1, y=1, z=0.7),
        camera=dict(eye=dict(x=1.5, y=-1.7, z=1.0))
    ),
    width=1000,
    height=800,
    margin=dict(l=0, r=0, t=60, b=0)
)

fig.write_html('cubic_complex_3d_interactive.html')
print("Roots:")
for r in roots:
    print(f"  {r}")
print("Saved interactive plot to cubic_complex_3d_interactive.html")
print("Open it by double-clicking the file, or run: xdg-open cubic_complex_3d_interactive.html")