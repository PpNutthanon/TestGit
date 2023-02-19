#วิธีจัดการข้อมูลสูญหาย => แทนค่าด้วยค่าเฉลี่ย , แทนที่ด้วยค่าตรงๆที่กำหนดขึ้นมา , แทนที่ด้วยค่าก่อนหน้า , แทนที่ด้วยค่าถัดไป , ลบข้อมูล
#แทนค่าด้วยข้อมูลเฉลี่ย  
#df.desribe() => เช็คค่าทางสถิติ
# select="Salary" (เลือก Column ที่ต้องการ)
# df[select]=df[select].fillna(df[selsct].mean())
import pandas as pd
df=pd.read_excel("Employee.xlsx",encoding="utf-8",index_col="Name")
print(df.describe())
select="Salary"
df[select] = df[select].fillna(df[select].mean()) #เอาค่าเฉลี่ยลงไปในข้อมูลที่ว่างใน Column Salary



