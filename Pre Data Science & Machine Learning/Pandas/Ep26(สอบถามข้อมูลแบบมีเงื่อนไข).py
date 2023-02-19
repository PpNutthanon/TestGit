#การเลือกแถวแบบมีเงื่อนไข
import pandas as pd
list1=["Mouse","Computer",1200]
list2=["Iphone","Telephone",38000]
list3=["Pizza","Food",400]
col,idx=["Product","Category","Price"],[1,2,3]
df=pd.DataFrame([list1,list2,list3],columns=col,index=idx)
print(df)
print(df.Price<=30000)
print(df[df.Price<=30000]) #แสดงผลที่ ราคาน้อยกว่า 30,000
print(df[df.Product=="Mouse"])
print(df.loc[(df.Price<=20000)&(df.Category=="Food")]) #และ
print(df.loc[(df.Price<=20000)|(df.Category=="Food")]) #หรือ
