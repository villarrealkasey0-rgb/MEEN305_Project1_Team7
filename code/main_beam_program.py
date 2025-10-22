# main_beam_program.py
from subfunctions import beam_analysis
from plot_functions import plot_shear_moment
from section_props_team import rectangular_props, circular_props, square_tube_props, ibeam_props
import numpy as np

print("=== MEEN 305 Beam Analysis Program ===")

# User inputs
L = float(input("Enter span length (in): "))
P = float(input("Enter load (lb): "))
a = float(input("Enter distance from support A (in): "))





# Hole configuration
has_holes = input("Does the beam have holes? (yes/no): ").strip().lower()

if has_holes == "yes":
    n_holes = int(input("Enter number of holes: "))
    d_hole = float(input("Enter hole diameter (in): "))
    x_start = float(input("Enter x-location where holes start (in): "))
    x_end = float(input("Enter x-location where holes end (in): "))
    
    #check if holes are imposssible
    check_valid_hole(shape_type, b0=b0, h0=h0, d0=d0)

else:
    # no holes, set everything to zero
    n_holes = 0
    d_hole = 0.0
    x_start = 0.0
    x_end = 0.0

shape_type = input("\nEnter cross-section type (rectangular / circular / tube / ibeam): ").strip().lower()

# Geometry input based on shape
x = np.linspace(0, L, 200)   # x-positions along beam

if shape_type == "rectangular":
    b0 = float(input("Enter starting width b0 (in): "))
    bL = float(input("Enter ending width bL (in): "))
    h0 = float(input("Enter starting height h0 (in): "))
    hL = float(input("Enter ending height hL (in): "))

    A, Iz, S = rectangular_props(L, x, b0, bL, h0, hL, d_hole, n_holes, x_start, x_end)

elif shape_type == "circular":
    d0 = float(input("Enter starting diameter d0 (in): "))
    dL = float(input("Enter ending diameter dL (in): "))

    A, Iz, S = circular_props(L, x, d0, dL, d_hole, n_holes, x_start, x_end)

elif shape_type == "tube":
    b0 = float(input("Enter starting outer width b0 (in): "))
    bL = float(input("Enter ending outer width bL (in): "))
    t0 = float(input("Enter starting wall thickness t0 (in): "))
    tL = float(input("Enter ending wall thickness tL (in): "))

    A, Iz, S = square_tube_props(L, x, b0, bL, t0, tL, d_hole, n_holes, x_start, x_end)

elif shape_type == "ibeam":
    bf0 = float(input("Enter flange width bf0 (in): "))
    bfL = float(input("Enter flange width bfL (in): "))
    tf0 = float(input("Enter flange thickness tf0 (in): "))
    tfL = float(input("Enter flange thickness tfL (in): "))
    tw0 = float(input("Enter web thickness tw0 (in): "))
    twL = float(input("Enter web thickness twL (in): "))
    h0 = float(input("Enter total height h0 (in): "))
    hL = float(input("Enter total height hL (in): "))

    A, Iz, S = ibeam_props(L, x, bf0, bfL, tf0, tfL, tw0, twL, h0, hL, d_hole, n_holes, x_start, x_end)

else:
    print("\n❌ Invalid shape type entered — exiting.\n")
    exit()

from plot_functions import plot_section_props

# Plot geometry-related results
plot_section_props(x, A, Iz, S, x_start, x_end)







# Run the beam analy5sis
beam_analysis(L, P, a)