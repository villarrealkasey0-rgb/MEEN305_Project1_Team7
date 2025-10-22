# main_beam_program.py
from subfunctions import beam_analysis
from plot_functions import plot_shear_moment

def main():
    print("=== MEEN 305 Beam Analysis Program ===")

    # User inputs
    L = float(input("Enter span length (in): "))
    P = float(input("Enter load (lb): "))
    a = float(input("Enter distance from support A (in): "))

    # Run the beam analysis
    x, V, M, RA, RB = beam_analysis(L, P, a)

    # Print reactions
    print(f'\nReactions:')
    print(f"  RA = {RA:.3f} lb")
    print(f"  RB = {RB:.3f} lb")

    # Plot shear & moment diagrams 
    plot_shear_moment(x,V,M,a)

if __name__ == "__main__":
    main()
    