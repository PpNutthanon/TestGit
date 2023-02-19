#Array และ ค่าทางสถิติ
import numpy as np
a=np.array([10,5,4,6,99,100,50,30])

#หาผลสมาชิกใน Array 1D
print(a.sum()) #หาผลรวม
print(a.prod()) #หาผลคูณ
print(a.mean()) #หาค่าเฉลี่ย
print(a.max()) #หาค่าสูงสุด

#หาตำแหน่ง index Array 1D
print(a.argmax()) #ค่าสูงสุดอยู่ที่ index เท่าไหร่

b=np.array([[10,20,30],[40,50,90],[80,100,5]])

#หาค่าใน Array 2D => แนวนอน axis=1 , แนวตั้ง axis=0
print(b)
print(np.min(b,axis=1)) #แนวนอน สมาชิกตัวใดใน b ต่ำที่สุด
print(np.min(b,axis=0)) #แนวตั้ง สมาชิกตัวใดใน b ต่ำที่สุด
print(np.mean(b,axis=1))