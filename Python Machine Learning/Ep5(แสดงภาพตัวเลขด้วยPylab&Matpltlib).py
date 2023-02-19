import matplotlib.pyplot as plt
import pylab
from sklearn import datasets

#Pylab
digit_dataset = datasets.load_digits()
print(digit_dataset.target[1])
pylab.imshow(digit_dataset.images[1],cmap=pylab.cm.gray_r)
pylab.show()

#Matplotlib
plt.imshow(digit_dataset.images[2],cmap=plt.get_cmap("gray"))
plt.show()
