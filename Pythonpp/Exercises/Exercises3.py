#Program calculate area of the circle
from math import pi
print("Program Calculate Area of the circle")
r=float(input("Enter the value of radius(m):"))
area=pi*r**2
if r>0:
    print("The area of the circle is :",area)
else:
    print("Area is not defined")
