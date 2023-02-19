#การลบ Columns => df.drop("ชื่อColumns","axis=1")
import pandas as pd
df=pd.read_excel("Stock.xlsx",encoding="utf-8",index_col="Name")
df=df.drop("Delivery",axis=1,inplace=True) #ลบ Column Delivery ออกไป
print(df)