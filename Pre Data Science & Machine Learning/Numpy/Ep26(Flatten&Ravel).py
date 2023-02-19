#Flatten => การเปลี่ยน Array หลายมิติ ให้เหลือมิติเดียว
#Flatten => โครงสร้างไม่เปลี่ยนถาวร
#Ravel => ถ้าแก้ไขตัว ravel ตัวเดิมก็จะเปลี่ยนด้วย => ข้อมูลจะ link หากัน
import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print(a)
b=a.flatten() #ทำให้ Array กลายเป็น 1 มิติ
print(b)
c=a.ravel()
print(c)
c[0]=5 #แก้ c แล้ว a จะเปลี่ยนด้วยเพราะ เป็น ravel
print(a)

