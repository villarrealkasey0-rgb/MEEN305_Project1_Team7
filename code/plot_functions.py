import matplotlib.pyplot as plt

def plot_shear_moment(x, V, M, a):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,8), sharex=True)

    # --- Shear Force Diagram ---
    ax1.plot(x, V, color='tab:blue', linewidth=2, label='V(x)')
    ax1.fill_between(x, V, 0, where=(V>=0), color='tab:blue', alpha=0.3)
    ax1.fill_between(x, V, 0, where=(V<=0), color='tab:red', alpha=0.3)
    ax1.axhline(0, color='k', linewidth=0.8)
    ax1.axvline(a, color='k', linestyle='--', linewidth=0.8)
    ax1.set_title("Shear Force Diagram")
    ax1.set_ylabel("V(x) [lb]")
    ax1.grid(True)
    ax1.legend()

    # --- Bending Moment Diagram ---
    ax2.plot(x, M, color='tab:orange', linewidth=2, label='M(x)')
    ax2.fill_between(x, M, 0, where=(M>=0), color='tab:orange', alpha=0.3)
    ax2.fill_between(x, M, 0, where=(M<=0), color='tab:green', alpha=0.3)
    ax2.axhline(0, color='k', linewidth=0.8)
    ax2.axvline(a, color='k', linestyle='--', linewidth=0.8)
    ax2.set_title("Bending Moment Diagram")
    ax2.set_xlabel("x (in)")
    ax2.set_ylabel("M(x) [lb·in]")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.show()