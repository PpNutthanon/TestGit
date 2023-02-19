#สร้าง Dataframe จาก List และ Tuple
from numpy import column_stack
import pandas as pd
data=[10,20,30,40,50] #List
df=pd.DataFrame(data) 
print(df)
print("\n")

#กำหนดชื่อ Column เอง
col=["age"] # Column ต้องระุบเป็น List เท่านั้น!
tup=(59,60,78,20) #Tuple
dff=pd.DataFrame(tup,columns=col)
print(dff)




