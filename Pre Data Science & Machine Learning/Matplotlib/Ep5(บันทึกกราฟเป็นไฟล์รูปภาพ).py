#การบันทึกกราฟเป็นไฟล์
#Structures1 => plt.savefig("ชื่อ.png") => ภาพพื้นหลังเป็นสีขาว
#Structures2 => plt.savefig("ชื่อ.png",transparent=True) => ภาพพื้นหลังไม่มี
import numpy as np
import matplotlib.pyplot as plt
product1=np.arange(10,60,10)
product2=[15,30,10,20,60]
month=np.arange(1,6)
print(plt.plot(month,product1))
print(plt.plot(month,product2))
plt.xlabel("Month"),plt.ylabel("Sale")
plt.savefig("Draw.png") #Saveแบบพื้นหลังขาว
plt.savefig("DrawTransparent.png",transparent=True) #Saveแบบไม่มีพื้นหลัง
plt.show()