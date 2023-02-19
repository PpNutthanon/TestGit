#2D Array
#Array เริ่มนับคือแถวที่0
import numpy as np
a=np.array([1,2,3])# Array1D
b=np.array([[1,2,3],[4,5,6]]) # Array2D
print(b)
print("The Dimension Of B Is :",b.ndim)

c=[[1,2,3],[4,5,6],[7,8,9]]
d=np.array(c)
print(d)

tup=((3,2,1),(10,20,30))
e=np.array(tup)
print(e)