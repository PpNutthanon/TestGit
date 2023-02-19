#กำหนดขนาดข้อความใน Legend
#? Structure => plt.legend(fontsize="xx-small")
#?tructures => plt.legend(fontsize="20.5")
#*todo ค่าคงที่ fontsize => 
#*todo xx-large, x-large, large, medium, small, x-small, xx-small
import matplotlib.pyplot as plt
import numpy as np
product1=np.arange(10,60,10)
product2=[15,30,10,20,60]
month=np.arange(1,6)
data={"size":20,"color":"yellow","backgroundcolor":"black"}
plt.plot(month,product1,"r.-")
plt.plot(month,product2,"mx-")
plt.xlabel("Month",data), plt.ylabel("Sale",data)
plt.title("Top Sale In 2021",color="black",loc="center")

plt.legend(["Iphone","Sumsung"],loc="best",fontsize="xx-large")
#* plt.legend(["Iphone","Sumsung"],loc="best",fontsize=ตัวเลข) 
plt.show()