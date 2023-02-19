#แทนค่าข้อมูลด้วยค่าถัดไป
#Structures => df.fillna(method="bfill",inplace=True) ;ถ้าอยากเลือก Column เดียวให้ทำเหมือน Ep39
import pandas as pd
df=pd.read_excel("Employee.xlsx",encoding="utf-8",index_col="Name")
print(df)
df.fillna(method="bfill",inplace=True) #แทนข้อมูลที่ว่างโดยแทนข้อมูลถัดไป และบันทึกค่าลงไปใน df
print(df)
