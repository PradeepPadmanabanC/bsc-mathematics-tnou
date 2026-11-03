"""
Setup:
    python3 -m venv /tmp/venv
    source /tmp/venv/bin/activate
    pip install sympy numpy matplotlib

Run:
    python 3d-plot.py
"""


import numpy as np
import matplotlib.pyplot as plt

# --- Given data ---
R = np.sqrt(24)                      # sphere: x^2 + y^2 + z^2 = 24
P = np.array([1, 2, -1])             # given point (inside the sphere)
near = np.array([2, 4, -2])          # shortest-distance point on sphere
far = np.array([-2, -4, 2])          # longest-distance point on sphere

# --- Verify your results ---
assert np.isclose(near @ near, 24) and np.isclose(far @ far, 24)
d_near = np.linalg.norm(near - P)    # sqrt(6)
d_far = np.linalg.norm(far - P)      # sqrt(54)
print(f"Shortest distance = {d_near:.4f}  (sqrt(6)  = {np.sqrt(6):.4f})")
print(f"Longest distance  = {d_far:.4f}  (sqrt(54) = {np.sqrt(54):.4f})")

# --- Sphere surface ---
u = np.linspace(0, 2 * np.pi, 80)
v = np.linspace(0, np.pi, 40)
X = R * np.outer(np.cos(u), np.sin(v))
Y = R * np.outer(np.sin(u), np.sin(v))
Z = R * np.outer(np.ones_like(u), np.cos(v))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, color="lightblue", alpha=0.25, edgecolor="none")
ax.plot_wireframe(X, Y, Z, color="steelblue", alpha=0.15, linewidth=0.4,
                  rstride=4, cstride=4)

# --- Lines ---
ax.plot(*zip(P, near), color="green", linewidth=3,
        label=rf"Shortest: $\sqrt{{6}}$ ≈ {d_near:.3f}")
ax.plot(*zip(P, far), color="red", linewidth=3,
        label=rf"Longest: $\sqrt{{54}}$ ≈ {d_far:.3f}")

# --- Points ---
ax.scatter(*P, color="black", s=80, label="P (1, 2, -1)")
ax.scatter(*near, color="green", s=80, label="Nearest (2, 4, -2)")
ax.scatter(*far, color="red", s=80, label="Farthest (-2, -4, 2)")

# --- Point labels ---
ax.text(*(P + [0.2, 0, 0.3]), "P(1,2,-1)", fontsize=10)
ax.text(*(near + [0.2, 0, 0.3]), "(2,4,-2)", fontsize=10, color="green")
ax.text(*(far + [0.2, 0, 0.3]), "(-2,-4,2)", fontsize=10, color="red")

# --- Equal aspect so the sphere looks round ---
ax.set_box_aspect((1, 1, 1))
lim = R * 1.1
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title(r"Shortest and longest distance from P to $x^2+y^2+z^2=24$")
ax.legend(loc="upper left")

plt.savefig("sphere_distances.png", dpi=150, bbox_inches="tight")
plt.show()