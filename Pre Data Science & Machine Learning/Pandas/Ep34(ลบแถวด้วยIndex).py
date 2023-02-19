#การลบแถวกรณี Index เป็นตัวเลข
#Structures => df.drop(rows,axis=0,implace=True)เลข Index ที่จะลบ ;rows=2
#Structures การลบแถวหลายแถว => df.drop(rows,axis=0,inolace=True) ;rows=[1,2,4]
import pandas as pd
df=pd.read_excel("Stock.xlsx",encoding="utf-8")
print(df)

#ลบ Index ที่ 9
rows=9
df.drop(rows,axis=0,inplace=True)
print(df)

#ลบ Index ที่ 0,3,10
rowss=[0,3,10]
df.drop(rows,axis=0,inplace=True)
print(df)