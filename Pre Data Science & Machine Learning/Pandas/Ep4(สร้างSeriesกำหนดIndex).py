#การสร้าง Series แบบกำหนดหมายเลข Index
import pandas as pd
data=["Banana","Mango","Grape","Watermelon"]
print(type(data),data)
idx=[1,2,3,4] #กำหนดเลข Index

ps=pd.Series(data)
print("No Assume Index :",ps)

ps1=pd.Series(data,index=idx)
print("Asssume Index :",ps1)