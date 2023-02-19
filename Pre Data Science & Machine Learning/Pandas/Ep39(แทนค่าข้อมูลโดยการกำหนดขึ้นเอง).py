#แทนค่าข้อมูลด้วยค่าที่กำหนด 
#select="Salary" (เลือก Column ที่ต้องการ)
#df[select] = df[select].fillna(ค่าที่ต้องการใส่เข้าไป)
import pandas as pd
df=pd.read_excel("Employee.xlsx",encoding="utf-8",index_col="Name")
print(df)
select="Salary"
df[select]=df[select].fillna(18000) #ใส่ 18000 ลงไปในข้อมูลที่ว่างใน Column Salary
print(df)
