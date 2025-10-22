import sympy as sp
from sympy.plotting import (plot,plot_parametric)

#defining variables
x = sp.symbols('x')
Y = 50*10**6 #yield strength in Pa
rectangular = True
solid_circular = False
I_beam = False
square_tube = False


#imported from Andric, so delete later
I_z = x**2

#imported Moment
Mz = 34

#imported base and height
b_x = 2*x + 6
h_x = 3*x + 4

#calculated variables
cy = h_x / 2

##Von mises for Rectangular Cross Section
#Disregard: Nx, My, Tx
#von mises = [Mz*Cy / Iz]
vm_rect = (Mz*cy) / I_z
FoS_rect = Y / vm_rect



##Von mises for Solid Circular Cross Section

#Von mises for I Beam Cross Section

#Von mises for Square tube

if rectangular:
    plot(vm_rect, (x, 0, 5), title="Sample vm stress of rectangle", xlabel="x", ylabel="Von Mises")
    plot(FoS_rect, (x, 0, 5), title="Sample FoS of rectangle", xlabel="x", ylabel="FoS")
elif solid_circular:
    print("todo")
elif I_beam:
    print('todo')
elif square_tube:
    print('todo')
else:
    print('not available')