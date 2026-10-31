"""
3D plot of f(x, y) = 4x^2 + 6xy + 9y^2 - 8x - 24y + 4 with its minimum marked.

Setup:
    python3 -m venv /tmp/venv
    source /tmp/venv/bin/activate
    pip install sympy numpy matplotlib

Run:
    python plot3d.py
"""
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def plot_3d(f, x, y, x_range=(-3, 3), y_range=(-1, 4), n=200, mark_min=True):
    """Plot a sympy expression f(x, y) as a 3D surface, optionally marking its minimum."""
    f_num = sp.lambdify((x, y), f, "numpy")

    X, Y = np.meshgrid(np.linspace(*x_range, n), np.linspace(*y_range, n))
    Z = f_num(X, Y)

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.85, linewidth=0)
    ax.contour(X, Y, Z, levels=20, zdir="z", offset=Z.min(), cmap="viridis")

    if mark_min:
        sol = sp.solve([sp.diff(f, x), sp.diff(f, y)], [x, y], dict=True)[0]
        px, py = sol[x], sol[y]
        pz = f.subs({x: px, y: py})
        print(f"Critical point: ({px}, {py}), f = {pz}")
        px_f, py_f, pz_f = float(px), float(py), float(pz)

        # Highlight the lines x = px and y = py as curves on the surface
        ys = np.linspace(*y_range, n)
        xs = np.linspace(*x_range, n)
        ax.plot(np.full_like(ys, px_f), ys, f_num(px_f, ys),
                color="red", lw=3, label=f"x = {px}")
        ax.plot(xs, np.full_like(xs, py_f), f_num(xs, py_f),
                color="orange", lw=3, label=f"y = {py}")

        ax.scatter([px_f], [py_f], [pz_f],
                   color="black", s=60, label=f"min ({px}, {py}, {pz})")
        ax.legend()

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    ax.set_title(f"$f(x, y) = {sp.latex(f)}$", fontsize=13)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    x, y = sp.symbols("x y")
    f = 4*x**2 + 6*x*y + 9*y**2 - 8*x - 24*y + 4
    plot_3d(f, x, y)