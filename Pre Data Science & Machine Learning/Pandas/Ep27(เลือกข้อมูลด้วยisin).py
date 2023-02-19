#การเลือกขอมูลด้วย Isin
import pandas as pd
list1=["Mouse","Computer",1200]
list2=["Iphone","Telephone",38000]
list3=["Pizza","Food",400]
col,idx=["Product","Category","Price"],[1,2,3]
df=pd.DataFrame([list1,list2,list3],columns=col,index=idx)
print(df)
print(df.loc[(df.Price==38000)|(df.Product=="Mouse")|(df.Category=="Computer")])
print(df.loc[df.Price.isin([38000,400])]) #ดึงข้อมูลที่มีราคา 38000 กับ 400 มาแสดงผล
