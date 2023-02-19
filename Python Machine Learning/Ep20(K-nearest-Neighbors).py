 #* K-NN => วิธีแบ่งคลาสสำหรับจัดหมวดหมู่ข้อมูล โดยใช้หลักการเปรียบเทียบข้อมูลที่สนใจกับข้อมูลอื่นว่าเหมือนกันขนาดไหน
#! คำนวณได้เฉพาะข้อมูลที่บอกได้ชัดเจน เช่น เพศ, อาชีพ, ข้อมูลที่เป็นกลุ่มที่บอกได้ชัดเจน

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

iris_dataset = load_iris()
x_train ,x_test, y_train, y_test = train_test_split(iris_dataset["data"],iris_dataset["target"],test_size=0.4,random_state=0) #มีข้อมูลอยู่ 40%

#*Todo Create Model K-NN
knn = KNeighborsClassifier(n_neighbors=1) #ให้คิดจุดใกล้เคียง 1 จุด (ค่า Default จะใช้จุดใหล้เคียง 5 จุด)

#*Todo Trainning 
knn.fit(x_train, y_train)
print(x_test[1])
print(y_test[1])

#*Todo Prediction 
pred = knn.predict([x_test[1]])
y_pred = knn.predict(x_test)

print("Predict = ",pred)
print("Group = ",iris_dataset["target_names"][pred])
print(classification_report(y_test,y_pred,target_names = iris_dataset["target_names"]))
print("Accuracy = ",accuracy_score(y_test,y_pred)*100)