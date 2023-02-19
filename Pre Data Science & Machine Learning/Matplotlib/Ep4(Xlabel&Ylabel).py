#Xlable => กำหนดชื่อข้อมูลที่อยู่ในแกน x
#Ylable => กำหนดชื่อข้อมูลที่อยู่ในแกน y
#Structures => plt.xlable("ชื่อที่จะตั้งในแกนx"), plt.ylabel("ชื่อที่จะตั้งในแกนy")
import numpy as np
import matplotlib.pyplot as plt
product1=[10,20,30,40,50]
product2=[15,30,10,20,60]
month=np.arange(1,6)
print(plt.plot(month,product1))
print(plt.plot(month,product2))
plt.xlabel("Month")
plt.ylabel("Sale")
plt.show()