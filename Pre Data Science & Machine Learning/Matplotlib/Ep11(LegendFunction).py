#Legend Function => plt.legend(["ชื่อ1","ชื่อ2"] => ตั้งชื่อเส้นในกราฟให้ไม่สับสน เมื่อมีหลายเส้นในกราฟเดียว
import matplotlib.pyplot as plt 
import numpy as np
product1=np.arange(10,60,10)
product2=[15,30,10,20,60]
month=np.arange(1,6)
data={"size":15,"backgroundcolor":"white"}
plt.plot(month,product1,"g+-"), plt.plot(month,product2,"r*-")
plt.xlabel("Month",data), plt.ylabel("Sale",data)
plt.title("Top Sale In 2021",size=30,loc="center")
plt.legend(["Mouse","Keyboard"]) #ตั้งชื่อ product1="Mouse" และ product2="Keyboard"
plt.show()
