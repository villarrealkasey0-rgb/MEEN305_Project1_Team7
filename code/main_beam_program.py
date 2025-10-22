# main_beam_program.py
from subfunctions import beam_analysis
from plot_functions import plot_shear_moment

print("=== MEEN 305 Beam Analysis Program ===")

# User inputs
L = float(input("Enter span length (in): "))
P = float(input("Enter load (lb): "))
a = float(input("Enter distance from support A (in): "))

# Run the beam analy5sis
beam_analysis(L, P, a)