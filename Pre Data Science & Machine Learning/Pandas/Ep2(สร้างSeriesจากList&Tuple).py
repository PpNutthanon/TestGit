#สร้าง Series จาก List & Tuple
import pandas as pd
data_ls=[10,20,"Pp",15.05,"Banana",True] #List
data_tp=(10,20,"Pp",15.05,"Python","Banana",True) #Tuple
a=pd.Series(data_ls)
b=pd.Series(data_tp)
print(a,"\n")
print(b)

