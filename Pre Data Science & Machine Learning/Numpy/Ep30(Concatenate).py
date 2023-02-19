#Concatenate => การนำข้อมูลของกลุ่มสมาชิก 2 กลุ่ม มารวมกัน
import numpy as np
#Array 1D
a=np.array([3,4,2,6])
b=np.array([8,6,5,10])

#รวมสมาชิก a กับ b
c=np.concatenate((a,b))
print(c)
a=np.append(a,100) #นำ 100 มาใส่ใน array a
print(a)

#Array 2D
x=np.array([[1,2],[3,4]])
x=np.append(x,[[10],[20]],axis=1) #ใส่เข้าไปในแนวนอน
print(x)

