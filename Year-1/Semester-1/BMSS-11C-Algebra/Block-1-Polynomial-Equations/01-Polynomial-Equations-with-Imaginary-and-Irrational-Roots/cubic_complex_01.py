"""
Interactive 3D visualization of f(z) = z^3 - 7z^2 + 17z - 11 over the complex plane,
split into its real and imaginary parts as two separate 3D surfaces.

Left plot:  Re(f(z))
Right plot: Im(f(z))

A root of f(z) is a point where BOTH surfaces cross zero at the same (Re(z), Im(z)) —
i.e. Re(f(z)) = 0 AND Im(f(z)) = 0 simultaneously. That's why a root shows up as a
zero-crossing in both plots at the same (x, y) location.

Roots (from factoring (x - 1)(x^2 - 6x + 11) = 0):
  z1 = 1
  z2 = 3 + i*sqrt(2)
  z3 = 3 - i*sqrt(2)
"""

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
F_re = np.clip(F.real, -40, 40)   # clip so far corners don't dwarf the roots region
F_im = np.clip(F.imag, -40, 40)

# ---- Build side-by-side 3D subplots ----
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{'type': 'surface'}, {'type': 'surface'}]],
    subplot_titles=('Re(f(z))', 'Im(f(z))'),
    horizontal_spacing=0.02
)

# Real part surface
fig.add_trace(go.Surface(
    x=Re, y=Im, z=F_re,
    colorscale='RdBu', reversescale=True,
    cmin=-40, cmax=40,
    opacity=0.9,
    colorbar=dict(title='Re(f(z))', x=0.42, len=0.75),
    name='Re(f(z))',
    hovertemplate='Re(z): %{x:.2f}<br>Im(z): %{y:.2f}<br>Re(f(z)): %{z:.2f}<extra></extra>'
), row=1, col=1)

# Imaginary part surface
fig.add_trace(go.Surface(
    x=Re, y=Im, z=F_im,
    colorscale='RdBu', reversescale=True,
    cmin=-40, cmax=40,
    opacity=0.9,
    colorbar=dict(title='Im(f(z))', x=1.0, len=0.75),
    name='Im(f(z))',
    hovertemplate='Re(z): %{x:.2f}<br>Im(z): %{y:.2f}<br>Im(f(z)): %{z:.2f}<extra></extra>'
), row=1, col=2)

# Zero-reference planes (helps visually spot the zero crossings)
zero_plane = np.zeros_like(F_re)
for col in (1, 2):
    fig.add_trace(go.Surface(
        x=Re, y=Im, z=zero_plane,
        showscale=False, opacity=0.15,
        colorscale=[[0, 'gray'], [1, 'gray']],
        hoverinfo='skip', showlegend=False
    ), row=1, col=col)

# Root markers + vertical guide lines, on both subplots
for r in roots:
    label = f"{r.real:.2f}{'+' if r.imag >= 0 else '-'}{abs(r.imag):.2f}i"
    for col in (1, 2):
        fig.add_trace(go.Scatter3d(
            x=[r.real, r.real], y=[r.imag, r.imag], z=[-40, 40],
            mode='lines',
            line=dict(color='black', width=3, dash='dash'),
            showlegend=False, hoverinfo='skip'
        ), row=1, col=col)
        fig.add_trace(go.Scatter3d(
            x=[r.real], y=[r.imag], z=[0],
            mode='markers+text',
            marker=dict(size=6, color='lime', line=dict(color='black', width=1)),
            text=[label], textposition='top center',
            textfont=dict(size=11, color='black'),
            showlegend=False,
            hovertemplate=f'root: {label}<extra></extra>'
        ), row=1, col=col)

fig.update_layout(
    title_text='f(z) = z³ − 7z² + 17z − 11 — real and imaginary parts (roots = zero crossings in both)',
    width=1500,
    height=800,
    margin=dict(l=0, r=0, t=80, b=0),
    scene=dict(
        xaxis_title='Re(z)', yaxis_title='Im(z)', zaxis_title='Re(f(z))',
        camera=dict(eye=dict(x=1.5, y=-1.7, z=1.0))
    ),
    scene2=dict(
        xaxis_title='Re(z)', yaxis_title='Im(z)', zaxis_title='Im(f(z))',
        camera=dict(eye=dict(x=1.5, y=-1.7, z=1.0))
    )
)

fig.write_html(
    'cubic_re_im_3d_linked.html',
    post_script="""
    var gd = document.getElementsByClassName('plotly-graph-div')[0];
    var syncing = false;

    gd.on('plotly_relayout', function(eventData) {
        if (syncing) return;

        // Figure out which scene's camera changed (scene = left, scene2 = right)
        var sourceScene, targetScene;
        if (eventData['scene.camera'] !== undefined) {
            sourceScene = 'scene'; targetScene = 'scene2';
        } else if (eventData['scene2.camera'] !== undefined) {
            sourceScene = 'scene2'; targetScene = 'scene';
        } else {
            return; // not a camera change (e.g. zoom via other means) - ignore
        }

        var camera = eventData[sourceScene + '.camera'];
        syncing = true;
        var update = {};
        update[targetScene + '.camera'] = camera;
        Plotly.relayout(gd, update).then(function() { syncing = false; });
    });
    """
)

print("Roots:")
for r in roots:
    print(f"  {r}")
print("Saved interactive plot to cubic_re_im_3d_linked.html")
print("Open it with: xdg-open cubic_re_im_3d_linked.html")
print("Rotate either subplot - the other one follows automatically.")