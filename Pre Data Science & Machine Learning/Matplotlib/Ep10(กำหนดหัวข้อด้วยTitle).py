#การกำหนดหัวข้อ(Title) => plt.title("ชื่อที่ต้องการใส่")
#*todo plt.title("ชื่อที่ต้องการใส่","size"=number,"color"="สีที่ต้องการ","backgroundcolor"="สีพื้นหลังที่ต้องการ")
#*todo plt.title("ชื่อที่ต้องการ",loc="ตำแหน่งที่ต้องการให้อยู่") ;มี center,right,left
import matplotlib.pyplot as plt 
import numpy as np
product=np.arange(10,60,10)
month=np.arange(1,6)
data={"size":20,"color":"blue","backgroundcolor":"yellow"}
plt.plot(month,product,"k.-")
plt.xlabel("Month",data), plt.ylabel("Sale",data)
plt.title("Top Sale In 2021",data,loc="left")
plt.show()
