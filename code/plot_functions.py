import matplotlib.pyplot as plt

def plot_shear_moment(x, V, M, a):
    plt.figure(figsize=(10,4))
    plt.plot(x, V, linewidth=2)
    plt.title("Shear Force Diagram")
    plt.xlabel("x (in)"); plt.ylabel("V(x) [lb]")
    plt.grid(True); plt.axhline(0, color='k', linewidth=0.8)
    plt.axvline(a, color='k', linestyle='--', linewidth=0.8)
    plt.tight_layout(); plt.show()

    plt.figure(figsize=(10,4))
    plt.plot(x, M, linewidth=2)
    plt.title("Bending Moment Diagram")
    plt.xlabel("x (in)"); plt.ylabel("M(x) [lb·in]")
    plt.grid(True); plt.axhline(0, color='k', linewidth=0.8)
    plt.axvline(a, color='k', linestyle='--', linewidth=0.8)
    plt.tight_layout(); plt.show()