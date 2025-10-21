import numpy as np
import matplotlib.pyplot as plt
# Beam Analysis
# ===============================
def beam_analysis(L, P, a):

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

    RA = P * (L-a) / L
    RB = P * a / L

    print(f'\nReaction at A = {RA:.2f} lb')
    print(f'\nReaction at B = {RB:.2f} lb')
