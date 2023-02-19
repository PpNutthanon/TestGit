#Dataframe การอ่านเอกสารใน Excel
#Structures => pd.read_excel("ตำแหน่งไฟล์","ชื่อSheet",encoding="utf-8")
import pandas as pd
df=pd.read_excel("dataupdates.xlsx","Product",encoding="utf-8")
print(df)