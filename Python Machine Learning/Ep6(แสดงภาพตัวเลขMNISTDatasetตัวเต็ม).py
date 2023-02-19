#แสดงภาพตัวเลข MNIST Dataset ตัวเต็ม
from scipy.io import loadmat 
import matplotlib.pyplot as plt
mnist_raw = loadmat("mnist-original.mat") #Load File เข้ามาทำงาน
print(mnist_raw)
mnist = {"data":mnist_raw["data"], "target":mnist_raw["label"][0]}
x, y = mnist["data"], mnist["target"]
print(mnist["data"].shape)

number=x[15000]
number_image = number.reshape(28,28)
plt.imshow(number_image,cmap=plt.cm.binary,interpolation="nearest")
plt.show()
print(x.shape)
