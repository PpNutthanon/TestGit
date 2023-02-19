#จัดการข้อมูลสูญหาย (Missing Value)

#การตรวจสอบข้อมูลสููญหาย
#df.isnull() => ถ้าTrueแสดงว่ามีข้อมูลไม่ครบหรือสูญหาย , ถ้าFalseแสดงว่ามีข้อมูลครบ
#df.isnull().any() => หาว่า Columns ไหน ที่มีค่าว่าง
#df.isnull().sum() => มีค่าว่างกี่แถว

#การตรวจสอบข้อมูลครบถ้วนมั้ย
#df.notnull() => ถ้าTrueแสดงว่ามีข้อมูลครบ , ถ้าFalseแสดงว่าข้อมูลไม่ครบหรือสูญหาย
#df.notnull().any() => หาว่า Columns ไหน ที่มีข้อมูลครบ
#df.notnull().sum() => ข้อมูลมีครบถ้วนกี่แถว

import pandas as pd
df=pd.read_excel("Employee.xlsx",encoding="utf-8",index_col="Name")
print(df)

#หาข้อมูลสูญหาย
print(df.isnull().any())
print(df.isnull().sum())
