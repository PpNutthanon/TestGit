#กราฟเส้น => Line Graph
import matplotlib.pyplot as plt
import numpy as np

#หากราฟยอดขายของ 5 เดือนแรก โดยใช้ Line Graph
product1=[10,20,30,40,50]
product2=[15,30,10,20,60]
month=np.arange(1,6)
print(plt.plot(month,product1))
print(plt.plot(month,product2))
plt.show() #เอามา plot รวมกัน ในกราฟเดียว
