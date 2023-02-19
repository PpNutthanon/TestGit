#Reshape & Resize
#Reshape => เปลี่ยนแปลงไม่ถาวร
#Resize => เปลี่ยนแปลงถาวร
import numpy as np
a=np.arange(10)
print(a)
b=a.reshape((2,5)) #2dimension 2row 5column
print("New Shape a :",b)
print(a)
a.resize((2,5))
print(a)

