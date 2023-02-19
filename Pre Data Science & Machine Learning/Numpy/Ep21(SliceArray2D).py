#Slice Array 2D
#Structure => name[start:end:step,start:end:step] (rowกับcolumn)
import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
print(x[:,:]) #print ทั้งหมด
print(x[1:,1:])
print(x[2:,2:])
print(x[2:,1:])
print(x[:,2:])
print(x[1:,:])
print(x[:2,:])
print(x[:2,:2])
print(x[1:2,1:2])
print(x[::2,:])