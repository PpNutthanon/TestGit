#Math Operation
import numpy as np

#Array1D
a=np.arange(1,5)
print(a)
print(a+2) #เอาสมาชิกใน a ทุกตัวมา บวก 2
print(a**2)
print(a%2)

b=np.arange(1,5)
print(a.shape)
print(b.shape)
print(a+b) #จะบวกกันได้ shape ต้องเท่ากัน

#Array2D
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[7,8,9],[10,11,12]])
print(x.shape,y.shape)
print(x+y)
print(x*y)
print(x%y)