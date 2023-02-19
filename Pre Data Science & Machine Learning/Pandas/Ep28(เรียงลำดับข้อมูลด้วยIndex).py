#การจัดเรียงข้อมูลตาม Index
import pandas as pd
df=pd.read_excel("Stock.xlsx",encoding="utf-8",index_col="Name")
print(df)

#เรียงตามพยัญชนะและสระ => ภาษาอังกฤษ และ ตามด้วยภาษาไทย(พยัญชนะไปสระ)
df=df.sort_index()
print(df)

df=df.sort_index(ascending=False) #เรียงสระไปพยัญชนะ
print(df)

df=df.sort_index(ascending=True) 