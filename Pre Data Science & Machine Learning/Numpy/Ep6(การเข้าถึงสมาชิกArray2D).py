#การเข้าถึงสมาชิก Array 2 มิติ => ชื่อArray[แถว][หลัก]
import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print(a)
print(a[1][1]) #เรียกใช้งาน แถวที่1 หลักที่1
print(a[2][0])

#แก้ไขค่าใน Array2D
a[0][1]=200
print(a)

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[2][1])
print(b[-2][-2])