import numpy as np
import sympy as sp

##Von mises for Rectangular Cross Section
#Disregard: Nx, My, Tx
#von mises = [My*Cz / Iy]

x = sp.symbols('x')
equation = sp.Eq(2*x+3,7)
solution = sp.solve(equation, x)
print(solution)