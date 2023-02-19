#การแบ่งข้อมูล Array => split
#Split => np.split(array,แบ่งกี่ส่วน)
import numpy as np

#Array1D
a=np.arange(1,21)
print(len(a))
a=np.split(a,4) #แบ่ง array เป็น 4 ส่วน
print(a,len(a))

#Array 2D
#hsplit => แบ่งเป็นแนวตั้ง
#vsplit => แบ่งเป็นแนวนอน
b=np.arange(1,21).reshape(5,4)
print(b)
b=np.hsplit(b,4)
print(b)
c=np.arange(1,21).reshape(5,4)
c=np.vsplit(c,5)
print(c)
