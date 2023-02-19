#กำหนดคุณสมบัติของ Label => กำหนดผ่าน Dict, คุณสมบัติผ่าน Properties
#? กำหนดผ่าน Dict
#? data={"size":20,"color":black}
#? plt.xlabel("ข้อความ",data)
#*Todo คุณสมบัติผ่าน Properties
#*Todo plt.xlabel("ข้อความ",size=20,color="black",backgroundcolor="red")
import matplotlib.pyplot as plt
import numpy as np
product=[15,30,10,20,60]
month=np.arange(1,6)
data={"size":15,"color":"white","backgroundcolor":"blue"}
print(plt.plot(month,product,"gx--"))
plt.xlabel("Month",size=20,color="green",backgroundcolor="yellow")
plt.ylabel("Sale",data)
plt.show()
