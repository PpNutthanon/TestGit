#กำหนดตำแหน่ง Legend
#*Todo 0=best, 1=upper right, 2=upper left, 3=lower left, 4=lower right, 5=right
#*? 6=center left, 7=center right, 8=lower center, 9=upper center, 10=center
import matplotlib.pyplot as plt 
import numpy as np 
product1=np.arange(10,60,10)
product2=[15,30,10,20,60]
month=np.arange(1,6)
data={"size":18,"color":"blue","backgroundcolor":"white"}
plt.plot(month,product1,"y.-")
plt.plot(month,product2,"rx-")
plt.xlabel("Month",data), plt.ylabel("Sale",data)
plt.title("Top Sale In 2021",size=25,color="magenta",backgroundcolor="white",loc="center")

plt.legend(["Mouse","keyboard"],loc="upper right") #กำหนดให้ตำแหน่งของ legend ไปอยู่ที่บนขวา ของกราฟ
#*todo เขียนแบบนี้ก็จะแสดงผลเหมือนกัน => plt.legend(["Mouse","Keyboard"],loc=1)
plt.show()
