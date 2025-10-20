#Statics 

Load = float(input("enter the load in lbs: "))
Distance = float(input("enter the distance at which the load applied at from support A in inches: "))

while Distance > 9:
    print("Distance cannot be greater than 9 inches. Please enter a valid value.")
    Distance = float(input("Enter the distance from support A in inches: "))
   
#For part 1, Load = 5, Distance = 4
#For part 2, Load = 9, Distance = 3.4

Support_B = (Load * Distance)/8
Support_A = Load - Support_B

print("Reaction at Support A =", Support_A, "lbs")
print("Reaction at Support B =", Support_B, "lbs")
