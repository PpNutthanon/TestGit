#Broadcasting => ขนาดและมิติของ Array 2 ตัว ไม่สอดคล้องกัน
import numpy as np
x=np.array([[1,2],[3,4],[5,6]])
y=np.array([1,2])
print(x+y)

a=np.array([2])
b=np.array([[10],[20],[30]])
print(x+a)
print(x+b)