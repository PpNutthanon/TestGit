#แทนค่าข้อมูลด้วยค่าก่อนหน้า
#Structures => df.fillna(method="pad",inplace=True) ;ถ้าอยากเลือก Column เดียวให้ทำเหมือน Ep ที่แล้ว
import pandas as pd
df=pd.read_excel("Employee.xlsx",encoding="utf-8",index_col="Name")
print(df)
df.fillna(method="pad",inplace=True) #ใส่ค่าก่อนหน้าลงไปในข้อมูลที่ว่างอยู่ และ บันทึกลงไปใน df
print(df)
