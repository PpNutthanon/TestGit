# Face & Edge Color Legend
#? Face Color => สีของแผ่น Legend => plt.legend(facecolor="สีที่ต้องการ")
#*todo Edge Color => สีของขอบ Legend => plt.legend(edgecolor="สีของขอบ Legend ที่ต้องการ")
import numpy as np
import matplotlib.pyplot as plt
product1=np.arange(10,60,10)
product2=[15,30,10,20,60]
month=np.arange(1,6)
data={"size":20,"color":"magenta","backgroundcolor":"black"}
plt.plot(month,product1,"y+-")
plt.plot(month,product2,"rx-")
plt.xlabel("Month",data), plt.ylabel("Sale",data)
plt.title("Top Sales In 2021",loc="center")
plt.legend(["Book","Audio"],loc="best",fontsize=18,facecolor="pink",edgecolor="black") #ทำให้แผ่นของ legend เป็นสีชมพู และ ขอบสีดำ
plt.show()