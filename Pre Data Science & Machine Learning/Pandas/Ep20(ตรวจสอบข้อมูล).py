#การตรวจสอบข้อมูลใน Dataframe
'''
head() => อ่านข้อมูล 5 แถวแรก
head(n) => อ่านข้อมูล n แถวแรก
tail() => อ่านข้อมูล 5 แถวสุดท้าย
tail(n) => อ่านข้อมูล n แถวสุดท้าย
sample(n) => สุ่มจำนวนข้อมูล n แถว
describe() => ดูค่าทางสถิติ เช่น ค่าต่ำสุด-สูงสุด , ค่าเฉลี่ย เป็นต้น
shape => สำหรับนับจำนวนข้อมูล เช่น (20,4) คือ 20 แถว 4 คอลัมน์
columns => ตรวจสอบว่ามีคอลัมน์อะไรบ้าง
values => อ่านข้อมูลแบบ array
'''

import numpy as np
import pandas as pd
df=pd.read_excel("dataupdates.xlsx","weather",encoding="utf-8",index_col="Day")
print(df.head())
print(df.sample(5))
print(df.describe())
print(df.mean())
print(df.values())