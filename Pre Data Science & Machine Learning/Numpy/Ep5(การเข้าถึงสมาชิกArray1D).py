#การเข้าถึงสมาชิก Array 1 มิติ
import numpy as np
a=np.array([10,20,30,40,50,60])
print(a[3]) #เรียกตัวที่3ออกมา = 40
print(a[-1])
print(a[5]+a[2])

#แก้ไขสามชิกใน Array
a[3]=100 #เปลี่ยน 40 เป็น 100
print(a)
