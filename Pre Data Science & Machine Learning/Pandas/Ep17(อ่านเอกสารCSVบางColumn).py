#Dataframe การอ่านเอกสาร CSV(เฉพาะบางคอลัมน์)
#Structures => pd.read_csv("ตำแหน่งไฟล์",encoding="utf-8",usecols=คอลัมน์ที่จะอ่าน)
import pandas as pd
col=["Name","Categories"]
a=pd.read_csv("Product2(Ep15pandas).csv",encoding="utf-8",usecols=col) #อ่านข้อมูล เอามาเฉพาะ Name กับ Categories
print(a)
b=pd.read_csv("Product2(Ep15pandas).csv",encoding="utf-8",usecols=col,index_col="Name") #เอา Name มากำหนดเป็น Index
print(b)
