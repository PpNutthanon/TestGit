# Linear Regression  => หาความสัมพันธ์ระหว่าง 2 ตัวแปร(ทราบค่า, ไม่ทราบค่า) ; y=mx+c
#? x=ตัวแปรที่ทราบค่า(Predictor), y=ตัวแปรที่ไม่ทราบค่า(Response), m=ความชัน, c=จุดตัดแกนy
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5,5,100) #สุ่มข้อมูล เลข -5ถึง5 จำนวน 100 ตัว
y = 2*x +1 #*Todo Let m=2, c=1
print(x)

#แสดงค่าความสัมพันธ์เป็นกราฟ
plt.plot(x,y,"-r",label="y=2x+1")
plt.xlabel("X Variables"), plt.ylabel("Y Variables")
plt.title("Linear Regression"), plt.legend(loc="best")
plt.grid() #* ทำให้กราฟเป็นเส้น grid
plt.show()
