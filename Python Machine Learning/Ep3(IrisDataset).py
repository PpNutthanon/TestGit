#Iris Dataset => ต้องติดตั้ง Scikit-Learn
from sklearn import datasets
iris_dataset = datasets.load_iris()
print(iris_dataset.keys())
print(iris_dataset["target"])
print(iris_dataset["target_names"]) #ชื่อสายพันธ์
print(iris_dataset["DESCR"]) #Description => นำไปอ้างอิงในงาน Project ต่างๆได้
print(iris_dataset["feature_names"]) #ความก้างความสูงของแต่ละสายพันธ์
print(iris_dataset["data"])
print(iris_dataset["data"][0:10]) #เอา data มาแค่ 10 แถวแรก