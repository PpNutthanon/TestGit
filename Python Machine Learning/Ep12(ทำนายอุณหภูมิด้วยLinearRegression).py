import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv("https://raw.githubusercontent.com/kongruksiamza/MachineLearning/master/Linear%20Regression/Weather.csv")
print(dataset.describe())

#Train & Test Set 
x = dataset["MinTemp"].values.reshape(-1,1)
y = dataset["MaxTemp"].values.reshape(-1,1)

#แบ่งเป็น 80% 20% 
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

#Trainning Algorithm
model = LinearRegression()
model.fit(x_train,y_train)

#Test Model
y_predict = model.predict(x_test)

#Compare True Data & Predict Data
df = pd.DataFrame({"Actually":y_test.flatten(),"Predicted":y_predict.flatten()})
df1 = df.head(20)
df1.plot(kind="bar",figsize=(16,10))
plt.show()