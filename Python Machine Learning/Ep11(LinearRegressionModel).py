# Linear Regression Models => 

#* Import Function เข้ามาทำงาน
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#? Simulation ข้อมูล
rng = np.random
x = rng.rand(50)*10
y = 2*x +rng.randn(50)

#*Todo Linear Regression Model
model = LinearRegression()
x_new = x.reshape(-1,1)


#! Train Linear Regression Model
model.fit(x_new, y) #Train Algorithm
print(model.score(x_new,y)) #เช็คว่ามีความแม่นแค่ไหน(เปอร์เซ็น)
print(model.intercept_)
print(model.coef_)

#? Trian Linear Regression Model
xfit = np.linspace(-1,11).reshape(-1,1)
print(xfit)
yfit = model.predict(xfit)

#* Ananlysis Linear Regression Model
print(yfit)
plt.scatter(x,y)
plt.plot(xfit,yfit)
plt.title("Linear Regression Model",loc="left")
plt.show()