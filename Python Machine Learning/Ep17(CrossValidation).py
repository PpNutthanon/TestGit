# Cross Validation => วัดประสิทธิภาพตัว model => k-fold (จำนวนการทดลองซ้ำ)
# Stochastic Gradient Descent => SGD
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score

def displayimage(x):
    plt.imshow(
    x.reshape(28,28),
    cmap = plt.cm.binary,
    interpolation = "nearest")
    plt.show()

def displaypredict(clf,actually_y,x):
    print("Actually = ",actually_y)
    print("prediction = ",clf.predict([x])[0])

mnist_raw = loadmat("mnist-original.mat")
mnist = {
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0]
}

x,y = mnist["data"],mnist["target"]
x_train, x_test, y_train, y_test = x[:6000], x[6000:], y[:6000], y[6000:]

predict_number = 1000
y_train_0 = (y_train==0)
y_test_0 = (y_test==0)

print(y_train_0.shape,y_train_0)
print(y_test_0.shape,y_test_0)

sgd_cls = SGDClassifier() #Train ข้อมูลลงไป
sgd_cls.fit(x_train,y_train_0)

displayimage(x_test[predict_number])
displaypredict(sgd_cls, y_test_0[predict_number], x_test[predict_number])

#*Todo Ep17
score = cross_val_score(sgd_cls,x_train,y_train_0,cv=3,scoring="accuracy") #cv=k-fold
print(score)