#Data Type
#ชนิดข้อมูลหลักๆที่ใช้ใน Numpy => Integer , Float , String , Boolean , Complex , Object
import numpy as np
a=np.array([1,2,3,4,5])
print(a.dtype) #เช็คว่าข้อมูลใน a เป็นข่อมูลอะไร

b=np.array([5,6,7,8],dtype="float") #กำหนดให้ข้อมูลใน b เป็น Float
print(b.dtype)
print(b)

c=np.array([[12,34,67],[10,20,30]],dtype="complex") #กำหนดข้อมูลใน c เป็น complex(มีiกับj)
print(c.dtype)
print(c)