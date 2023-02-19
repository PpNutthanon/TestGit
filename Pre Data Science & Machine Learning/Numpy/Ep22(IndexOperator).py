#Index Operator => การสร้าง Array ที่มีข้อมูลภายในเป็นหมายเลข index
import numpy as np
#Array1D
x=np.arange(1,10) #Array แบบทั่วไป
y=np.array([1,5,7]) #Array Index
z=np.array([2,4,6,8])
print(x)
print(x[y]) #ทำการเข้าถึงสาชิกภายในx โดยเอาเฉพาะ index 1 5 7 มาใช้งาน
print(x[z])

#Array2D
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[0,2])
print(a[[0,2],[2,0]])

#การเข้าถึงข้อมูลสมาชิก
c=x[[1,4]]
print(c)

#การกรองข้อมูลใน Array โดยการกำหนดเงื่อนไข
d=np.array([[1,-2,-3],[4,-5,-9]])
print(d[d<0])
print(d[d>0]*5)
print(d.dtype)