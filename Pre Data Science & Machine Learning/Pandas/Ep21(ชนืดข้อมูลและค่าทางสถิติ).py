#ชนืดข้อมูลและค่าทางสถิติ
'''
ชนิดข้อมูล(dtypes)
object => ชุดข้อความ(string).unicode
int64 => จำนวนเต็ม
float64 => ทศนิยม
bollean => ค่าทางตรรกศาสตร์(True/False)
datetime64 => วันเวลา
timedelta[ns] => ค่าแตกต่างระหว่าง datetime
category => list ของข้อความ

ค่าทางสถิติเบื้องต้น
mean() => ค่าเฉลี่ย
max() => ค่าสูงสุด
min() => ค่าต่ำสุด
count() => นับจำนวนข้อมูลทั้งหมด
std() => ส่วนเบี่ยงเบนมาตราฐาน
sum() => ผลรวมข้อมูล
'''
import pandas as pd
df=pd.read_excel("dataupdates.xlsx","score",encoding='utf-8',index_col="Name")
print(df)
print(df.Score.max())
print(df.Score.std())
print(df.Score.count())
print(df.Score.sum())
print(df.Score.sum()/df.Score.count())

#แปลงชนิดข้อมูลให้เป็น Category
df.Grade=df.Grade.astype("Category") #แปลงชนิดข้อมูล Grade ให้เป็น Category
