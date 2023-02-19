#Gradient Descent Algorithm (GD) => หาจุดต่ำสุดสูงสุดของฟังก์ชันที่กำหนดขึ้นมา
#? Best Case => จำนวนการวนรอบน้อยที่สุด
#*Todo Worst Case => จำนวนการวนรอบมากที่สุด
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

mnist_raw = loadmat("mnist-original.mat")
mnist={
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0]
}
print(mnist["data"].shape)
print(mnist["target"].shape)

x, y = mnist["data"], mnist["target"]
#แบ่งข้อมูลออกเป็น 2 ชุด => Trainning, Test
# 1-60000 => Train
# 60001-70000 => Test
x_train, x_test, y_train, y_test = x[:60000], x[60000:], y[:60000], y[60000:]
print(x_train.shape), print(x_test.shape), print(y_train.shape), print(y_test.shape)

# Class 0-9 => ทำนายตำแหน่งที่ 5000 เป็นเลขอะไรระหว่าง 0-9 => True or False
#? แยกเป็น Class 0, ไม่ใช่ Class 0
#*Todo ข้อมูล 1 ค่า => model => class 0 ??? => True or False
predict_number = 5000
y_train_0 = (y_train==0)
print(y_train_0)

