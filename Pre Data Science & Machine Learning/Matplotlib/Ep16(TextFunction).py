#Text Function => plt.text(x,y,string,arg***)
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
plt.legend(["Mouse","Keyboard"],title="Report",facecolor="pink",edgecolor="black",fontsize="large",borderpad=3,labelspacing=1)
plt.text(2,10,"Point1",size=15,color="magenta") #แสดงคำว่า Point1 ในพิกัด(2,10)
plt.text(4,25,"Point2",size="xx-large",color="orange") #แสดงคำว่า Point2 ในพิกัด(4,25)
plt.show()
