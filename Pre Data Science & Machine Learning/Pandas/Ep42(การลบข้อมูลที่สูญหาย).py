#วิธีการลบข้อมูลสูญหายด้วยการลบ => ลบทิ้งทั้งหมด(แถวและคอลัมน์), ลบแถวบางส่วน , ลบ Column บางส่วน , ลบทั้งแถว, ลบทั้ง Column

import pandas as pd
df=pd.read_excel("Employee.xlsx",encoding="utf-8",index_col="Name")
print(df)

#ลบแถวทั้งหมด => df.dropna(inplace=True)
df.dropna(inplace=True)

#ลบแถวบางส่วนที่มีค่าว่าง => df.dropna(subset=["ชื่อ1","ชื่อ2",...],inplac=True)
df.dropna(subset=["Age","Job"],inplace=True) #ถ้ามีคนไม่ใส่ข้อมูลที่ Column Age กับ Job ให้ลบข้อมูลทิ้ง และบันทึกลงใน df

#ลบ Column ที่ข้อมูลไม่ครบออกไป => df.dropna(axis="columns",inplace=True)
df.dropna(axis="columns",inplace=True) #ลบColumn ที่มีข้อมูลว่างออกไปทั้งหมด และบันทึกลงไปใน df


