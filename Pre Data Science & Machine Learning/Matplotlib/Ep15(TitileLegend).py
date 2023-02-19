#Title Legend  => plt.legend(title="ชื่อที่ต้องการ",borderpad="ขนาดที่ต้องการ",labelspacing="ระยะที่ต้องการ")
#? ขนาด default=0.4, ระยะ default=0.5
import numpy as np
import matplotlib.pyplot as plt
product1 = np.arange(10,60,10)
product2 = [15,30,10,20,60]
month = np.arange(1,6)
data={"size":20,"color":"magenta","backgroundcolor":"yellow"}
plt.plot(month,product1,"rx-")
plt.plot(month,product2,"b.-")
plt.xlabel("Month",data), plt.ylabel("Sale",data)
plt.title("Top Sale In 2021",fontsize=30,loc="center")
plt.legend(["Mouse","Keyboard"],
title="Report",
facecolor="pink",
edgecolor="black",
fontsize="large",
borderpad=3,
labelspacing=1
)
plt.show()
