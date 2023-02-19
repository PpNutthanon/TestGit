#Identity Matrix
import numpy as np
a=np.identity(4)
print(a)

b=np.identity(5,dtype="float")
print(b,b.dtype)

c=np.eye(5)
print(c)

d=np.eye(3,4)
print(d)

e=np.eye(5,k=1) #ย้ายเลข1 ไปทางขวา
print(e)

#ค่าk => ย้ายตำแหน่งของเส้นแทยงมุมใน Identity Matrix
f=np.eye(5,k=-1) #ย้ายเลข1 ลงมา
print(f)