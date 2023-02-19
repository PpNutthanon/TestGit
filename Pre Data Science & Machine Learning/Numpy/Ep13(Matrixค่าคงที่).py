#Matrix ค่าคงที่ => full => เป็นเลขใดเลขนึงทุกๆตัว Ex เป็นเลข 7 ทั้งหมด
import numpy as np
a=np.full(5,10) #จำนวนสมาชิก5ตัว ตัวเลขข้อางหลังเป็นสมาชิกที่เราต้องการใส่
print(a)

b=np.full((3,3),7,dtype="int")
print(b,b.dtype)
