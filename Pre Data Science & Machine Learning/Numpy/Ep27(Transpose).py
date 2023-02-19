#Transpose => สลับแถว สลับหลัก => ส่วนใหญ่ใช้กับ Array 2D
#Transpose => รูปร่าง a ไม่เปลี่ยนถาวร
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=a.transpose()
print(a,a.shape)
print(b,b.shape)