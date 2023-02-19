#การเข้าถึง Array 3 มิติ => ชื่อ[dept][row][column]
import numpy as np
a=np.array([[[1,2,3],[4,5,6]]])# Array 3D แบบ 3 ชั้น
print(a)
print("The Dimension Of a is :",a.ndim,"D")
print(a[0][1][1]) #เลข5
print(a[0][0][2]) #เลข3

b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])#Array3D แบบ 2 ชั้น
print(b)
print("The Dimension Of b is :",b.ndim,"D")
print(b[1][0][1]) #เลข8
