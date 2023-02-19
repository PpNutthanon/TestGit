#การกระจายข้อมูล => Scatter
import numpy as np
import matplotlib.pyplot as plt
randoms = np.random
x = randoms.rand(50)*10 #random ตัวเลขมา 10 ชุด (มากกว่า0ทั้งหมด)
c=randoms.randn(50) #randn คือ สุ่มค่าที่ติดลบ
y=2*x + c
print(x)
print(y)

#? y=mx+c
plt.scatter(x,y)
plt.xlabel("X Variables"), plt.ylabel("Y Variables")
plt.title("Linear Regression",loc="center")
plt.show()