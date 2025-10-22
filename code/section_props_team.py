#Andrick
import math
import numpy as np
import matplotlib.pyplot as plt





#Validates that hole geometry makes sense for the cross-section
import sys

def check_valid_hole(shape_type, b0=0, h0=0, d0=0, bf0=0, tf0=0, tw0=0, d_hole=0):
    """
    Checks if the given hole size is physically possible for the selected cross-section.
    If invalid, prints an error message and exits the program.
    If valid, it does nothing and lets the program continue.
    """

    too_large = False
    min_dim = 0

    # --- Check per cross-section type ---
    if shape_type == "rectangular":
        min_dim = min(b0, h0)
        if d_hole >= min_dim:
            too_large = True

    elif shape_type == "circular":
        min_dim = d0
        if d_hole >= min_dim:
            too_large = True

    elif shape_type == "tube":
        min_dim = b0
        if d_hole >= min_dim:
            too_large = True

    elif shape_type == "ibeam":
        min_dim = h0
        if d_hole >= min_dim:
            too_large = True

    # --- Handle impossible geometry ---
    if too_large:
        print(f"\n Error: Hole diameter ({d_hole} in) is too large for this {shape_type} section!")
        print(f"Minimum dimension is {min_dim} in — impossible geometry. Program will exit.\n")
        sys.exit()




# Linear taper function
def lin(v0, vL, x, L):
    """Linearly interpolates from v0 at x=0 to vL at x=L."""
    return v0 + (vL - v0) * (x / L)


# RECTANGULAR SECTION
def rectangular_props(L, x, b0, bL, h0, hL, d_hole, n_holes, x_start, x_end):
    """Returns arrays for A(x), Iz(x), and S(x) for a rectangular beam."""
    A = np.zeros(len(x))
    Iz = np.zeros(len(x))
    S = np.zeros(len(x))

    for i in range(len(x)):
        b = lin(b0, bL, x[i], L)
        h = lin(h0, hL, x[i], L)
        A[i] = b * h
        Iz[i] = (b * h**3) / 12

        # Subtract hole effect if inside hole region
        if x_start <= x[i] <= x_end and n_holes > 0:
            I_hole = (math.pi * d_hole**4) / 64
            Iz[i] -= n_holes * I_hole

        S[i] = Iz[i] / (h / 2)
    return A, Iz, S



# CIRCULAR SECTION
def circular_props(L, x, d0, dL, d_hole, n_holes, x_start, x_end):
    """Returns arrays for A(x), Iz(x), and S(x) for a circular beam."""
    A = np.zeros(len(x))
    Iz = np.zeros(len(x))
    S = np.zeros(len(x))

    for i in range(len(x)):
        d = lin(d0, dL, x[i], L)
        A[i] = (math.pi * d**2) / 4
        Iz[i] = (math.pi * d**4) / 64

        if x_start <= x[i] <= x_end and n_holes > 0:
            I_hole = (math.pi * d_hole**4) / 64
            Iz[i] -= n_holes * I_hole

        S[i] = Iz[i] / (d / 2)
    return A, Iz, S


# SQUARE TUBE SECTION
def square_tube_props(L, x, b0, bL, t0, tL, d_hole, n_holes, x_start, x_end):
    """Returns arrays for A(x), Iz(x), and S(x) for a square tube beam."""
    A = np.zeros(len(x))
    Iz = np.zeros(len(x))
    S = np.zeros(len(x))

    for i in range(len(x)):
        b = lin(b0, bL, x[i], L)      # outer width
        t = lin(t0, tL, x[i], L)      # wall thickness
        bi = b - 2 * t                # inner width
        if bi < 0:                     # invalid geometry guard
            bi = 0

        A[i] = b**2 - bi**2
        Iz[i] = (b**4 - bi**4) / 12

        if x_start <= x[i] <= x_end and n_holes > 0:
            I_hole = (math.pi * d_hole**4) / 64
            Iz[i] -= n_holes * I_hole

        S[i] = Iz[i] / (b / 2)
    return A, Iz, S


# I-BEAM SECTION
def ibeam_props(L, x, bf0, bfL, tf0, tfL, tw0, twL, h0, hL,
                d_hole, n_holes, x_start, x_end):
    """Returns arrays for A(x), Iz(x), and S(x) for an I-beam."""
    A = np.zeros(len(x))
    Iz = np.zeros(len(x))
    S = np.zeros(len(x))

    for i in range(len(x)):
        bf = lin(bf0, bfL, x[i], L)
        tf = lin(tf0, tfL, x[i], L)
        tw = lin(tw0, twL, x[i], L)
        h = lin(h0, hL, x[i], L)

        # Outer rectangle minus web cutouts
        A_flange = 2 * bf * tf
        A_web = tw * (h - 2 * tf)
        A[i] = A_flange + A_web

        # Moment of inertia (approximation)
        Iz_flange = 2 * ((bf * tf**3) / 12 + bf * tf * ((h/2 - tf/2)**2))
        Iz_web = (tw * (h - 2*tf)**3) / 12
        Iz[i] = Iz_flange + Iz_web

        if x_start <= x[i] <= x_end and n_holes > 0:
            I_hole = (math.pi * d_hole**4) / 64
            Iz[i] -= n_holes * I_hole

        S[i] = Iz[i] / (h / 2)
    return A, Iz, S



# Plot properties

def plot_section_props(x, A, Iz, S, x_start, x_end):
    # Cross-sectional area
    plt.figure(figsize=(10,4))
    plt.plot(x, A, linewidth=2)
    plt.title("Cross-Sectional Area")
    plt.xlabel("x (in)")
    plt.ylabel("A(x) [in^2]")
    plt.grid(True)
    plt.axvline(x_start, color='k', linestyle='--', linewidth=0.8)
    plt.axvline(x_end, color='k', linestyle='--', linewidth=0.8)
    plt.tight_layout()
    plt.show()

    # Moment of inertia
    plt.figure(figsize=(10,4))
    plt.plot(x, Iz, linewidth=2)
    plt.title("Moment of Inertia")
    plt.xlabel("x (in)")
    plt.ylabel("Iz(x) [in^4]")
    plt.grid(True)
    plt.axvline(x_start, color='k', linestyle='--', linewidth=0.8)
    plt.axvline(x_end, color='k', linestyle='--', linewidth=0.8)
    plt.tight_layout()
    plt.show()

    # Section modulus
    plt.figure(figsize=(10,4))
    plt.plot(x, S, linewidth=2)
    plt.title("Section Modulus")
    plt.xlabel("x (in)")
    plt.ylabel("S(x) [in^3]")
    plt.grid(True)
    plt.axvline(x_start, color='k', linestyle='--', linewidth=0.8)
    plt.axvline(x_end, color='k', linestyle='--', linewidth=0.8)
    plt.tight_layout()
    plt.show()

