#Numpy Attribute
import numpy as np
a=np.array([1,2,3,4,5],dtype="float")
b=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],dtype="complex")
print(a.shape) 
print(b.shape)

#เช็คจำนวนสมาชิกใน Array
print(a.size)
print(b.size)

#บอกขนาดของ Array มีกี่ byte
print(a.itemsize)
print(b.itemsize)