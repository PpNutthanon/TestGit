#Confusion Matrix
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
import itertools

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
def displayConfusionMatrix(cm,cmap=plt.cm.GnBu):
    classes=["Other Number","Number 5"]
    plt.imshow(cm,interpolation='nearest',cmap=cmap)
    plt.title("Confusion Matrix")
    plt.colorbar()
    trick_marks=np.arange(len(classes))
    plt.xticks(trick_marks,classes)
    plt.yticks(trick_marks,classes)
    thresh=cm.max()/2
    for i , j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
        plt.text(j,i,format(cm[i,j],'d'),
        horizontalalignment='center',
        color='white' if cm[i,j]>thresh else 'black')

    plt.tight_layout()
    plt.ylabel('Actually')
    plt.xlabel('Prediction')
    plt.show()
x,y = mnist["data"],mnist["target"]
x_train, x_test, y_train, y_test = x[:6000], x[6000:], y[:6000], y[6000:]

predict_number = 1000
y_train_0 = (y_train==0)
y_test_0 = (y_test==0)

print(y_train_0.shape,y_train_0)
print(y_test_0.shape,y_test_0)

sgd_cls = SGDClassifier() #Train ข้อมูลลงไป
sgd_cls.fit(x_train,y_train_0)

#*Todo Ep18
y_train_predict = cross_val_predict(sgd_cls,x_train,y_train_0,cv=3)
cm = confusion_matrix(y_train_0,y_train_predict)
plt.figure()
displayConfusionMatrix(cm)

