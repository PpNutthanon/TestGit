#Append & Insert
#Append => ข้อมูลที่ add เข้าไป จะอยู่หลังสุด
#Insert => แทรกข้อมูลแบบกำหนด index ที่จะให้เข้าไปอยู่ได้
import numpy as np
a=np.array([1,2,4,5,8])

#Append => np.append(array,number want to add)
a=np.append(a,40)
print(a)

#Insert => np.insert(array,index,number want to add)
a=np.insert(a,1,100)
print(a)
a=np.insert(a,(1,3),500) #แทรกใน index ที่ 1 กับ 3
print(a)