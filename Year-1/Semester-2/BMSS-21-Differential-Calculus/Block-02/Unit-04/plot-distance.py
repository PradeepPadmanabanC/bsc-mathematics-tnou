"""
Setup:
    python3 -m venv /tmp/venv
    source /tmp/venv/bin/activate
    pip install sympy numpy matplotlib

Run:
    python plot-distance.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Plane: x + 2y + z = 4  ->  n . r = d
n = np.array([1.0, 2.0, 1.0])
d = 4.0
P = np.array([1.0, 0.0, -2.0])

# Distance and foot of the perpendicular
t = (d - n @ P) / (n @ n)
Q = P + t * n
dist = abs(n @ P - d) / np.linalg.norm(n)
print(f"Distance = {dist:.4f}  (exact: 5/sqrt(6))")
print(f"Closest point on plane = {Q}")

# Build a square patch of the plane around Q using two
# orthonormal vectors lying in the plane (keeps true proportions)
a = np.array([1.0, 0.0, 0.0])
u = np.cross(n, a); u /= np.linalg.norm(u)
v = np.cross(n, u); v /= np.linalg.norm(v)

half = 3                                   # half-size of the plane patch
s, w = np.meshgrid(np.linspace(-half, half, 20), np.linspace(-half, half, 20))
X = Q[0] + s * u[0] + w * v[0]
Y = Q[1] + s * u[1] + w * v[1]
Z = Q[2] + s * u[2] + w * v[2]

# Same range for x, y, z: find the overall extent and use one cube
all_pts = np.concatenate([np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=1),
                          P[None, :], Q[None, :]])
center = (all_pts.max(axis=0) + all_pts.min(axis=0)) / 2
R = (all_pts.max(axis=0) - all_pts.min(axis=0)).max() / 2

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, alpha=0.4, color="skyblue")

ax.scatter(*P, color="red", s=60, label="P (1, 0, -2)")
ax.scatter(*Q, color="green", s=60, label="Foot of perpendicular")
ax.plot(*zip(P, Q), color="black", linewidth=2.5,
        label=f"Shortest distance = {dist:.3f}")

# Equal limits on all axes + cubic box => 1:1:1 scale
ax.set_xlim(center[0] - R, center[0] + R)
ax.set_ylim(center[1] - R, center[1] + R)
ax.set_zlim(center[2] - R, center[2] + R)
ax.set_box_aspect((1, 1, 1))

ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.set_title("Shortest distance from a point to a plane")
ax.legend()
plt.show()