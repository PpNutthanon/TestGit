#Dataset => Trainning Set, Test Set
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris_dataset = load_iris()
print(iris_dataset.data.shape)

#? กำหนดให้เป็น 20% and 80%
# 75% and 25% => เป็นค่า Default ของระบบ
x_train,x_test,y_train,y_test = train_test_split(iris_dataset["data"],iris_dataset["target"],test_size=0.2 ,random_state=0) 
#! 0.2คือ Test Set จะมีข้อมูลอยู่ 20%
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

