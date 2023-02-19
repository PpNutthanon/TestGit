#Array => 1D 2D 3D
#Array 2D ได้รับความนิยมมากที่สุด => matrix
import numpy as np
x=np.array(42) #Array 0 มิติ
print(x)
print(x.ndim) #มีกี่มิติ

y=np.array([2,3,5,7])
print(y)
print(y.ndim)
print(type(y))

li=[1,2,3,4]
b=np.array(li)
print(b)

tup=(10,20,30)
a=np.array(tup)
print(a)

c=np.array((1,2,3,4,5))
print(c)
