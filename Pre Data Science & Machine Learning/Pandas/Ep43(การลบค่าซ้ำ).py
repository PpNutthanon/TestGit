#ลบข้อมูลซ้ำ
#df[df.duplicated()] => เช็คว่ามีค่าซ้ำกี่จุด
#ลบข้อมูลที่เป็นค่าซ้ำ => df.drop_duplicates(inplace=True)
import pandas as pd
df=pd.read_excel("Employee.xlsx",encoding="utf-8",index_col="Name")
print(df)
print(df[df.duplicated()]) #เช็คค่าซ้ำ
df.drop_duplicates(inplace=True) #ลบแถวที่ซ้ำ และบันทึกลงไปใน df
print(df)
