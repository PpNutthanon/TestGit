#การเลือกแถวแบบวนรอบ => iterrows()
import pandas as pd
list1=["Mouse","Computer",1200]
list2=["Iphone","Telephone",38000]
list3=["Pizza","Food",400]
col,idx=["Product","Category","Price"],[1,2,3]
df=pd.DataFrame([list1,list2,list3],columns=col,index=idx)
print(df)
for idx,row in df.iterrows():
    print("Price = {} In Type Of {}".format(row.Product,row.Category))
