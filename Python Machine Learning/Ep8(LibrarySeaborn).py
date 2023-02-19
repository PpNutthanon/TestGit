#Library Seaborn
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sb 
iris_dataset = sb.load_dataset("iris") #ชนิดข้อมูลเป็น Dataframe
print(iris_dataset.head())

#? นำข้อมูลมาสร้างเป็นแผนภาพ
sb.set()
sb.pairplot(iris_dataset,hue="species",size=2) # hue => แบ่งสีตามอะไร
plt.show()
