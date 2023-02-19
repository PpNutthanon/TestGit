#การจัดเรียงข้อมูลตาม Value
import pandas as pd
df=pd.read_excel("Stock.xlsx",encoding="utf-8",index_col="Name")
print(df)

#ให้เรียงราคาสินค้าจากน้อยไปมาก
result=df.sort_values("Price")
print(result)

#ให้เรียงราคาจากมากไปน้อย
answer=df.sort_values("Price",ascending=False)

#Save ทับใน df ด้วย
ans=df.sort_values("Amount",inplace=True)
print(df,ans) #ans กับ df จะแสดงผลเหมือนกัน