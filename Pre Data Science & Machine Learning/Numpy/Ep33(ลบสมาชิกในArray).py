#ลบข้อมูลใน Array
#axis=0 แนวนอน , axis=1 แนวตั้ง
import numpy as np

#Array 1D
#np.delete(array,index)
a=np.arange(1,11)
a=np.delete(a,2) #ลบ index ที่ 2 ออกจาก Array a
print(a)

#Array 2D
#np.delete(array,index,axis)
b=np.arange(1,13).reshape(4,3)
print(b)
b=np.delete(b,2,axis=0)
print(b)