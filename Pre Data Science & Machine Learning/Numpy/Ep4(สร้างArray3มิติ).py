#Array3D => Array2D มาเรียงซ้อนกันหลายชั้น
import numpy as np
a=np.array([[1,2,3,],[23,45,67]])# Array2D
b=np.array([[[10,20,30],[4,5,6]]]) # Array3D
print(b)
print("The Dimension Of B is :",b.ndim)
