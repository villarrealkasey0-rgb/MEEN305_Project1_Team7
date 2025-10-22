import numpy as np
import sympy as sp
from sympy.plotting import (plot,plot_parametric)

##Von mises for Rectangular Cross Section
#Disregard: Nx, My, Tx
#von mises = [My*Cz / Iy]

x = sp.symbols('x')
b_x = 8 *x**2

plot(b_x, (x, 0, 5), title="b(x) = 8x^2", xlabel="x", ylabel="b(x)")