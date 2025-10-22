import numpy as np
import matplotlib.pyplot as plt

# Beam Analysis YAY yes
# ===============================
def beam_analysis(L, P, a, nx = 401):

    # Input validation
    # ===============================
    if L <= 0 or L > 9:
        print("Error: Span length must be positive and less than or equal to 9 in.")
        exit()

    if P <= 0:
        print("Error: Load must be positive.")
        exit()

    if a <= 0 or a >= L:
        print("Error: The load position 'a' must be between 0 and L (within the beam span).")
        exit()

    # Reactions
    RA = P * (L-a) / L
    RB = P * a / L

    # Shear & Moment
    x = np.linspace(0.0, L, nx)
    V = np.where(x < a, RA, RA - P)
    M = np.where(x < a, RA * x, RA * x - P * (x-a))

    return x, V, M, RA, RB
        
    


