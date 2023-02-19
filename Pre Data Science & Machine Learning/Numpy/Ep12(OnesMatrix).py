#Ones Matrix => สมาชิกภายใน matrix เป็น 1 ทุกตัว
import numpy as np
a=np.ones(10,dtype="int")
print(a)
print(a.dtype)

b=np.ones((2,3),dtype="complex")
print(b)
print(b.dtype)

c=np.ones([3,3],dtype="float")
print(c)
print(c.dtype)