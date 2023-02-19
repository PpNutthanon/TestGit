#การเพิ่ม Column
import pandas as pd
df=pd.read_excel("Stock.xlsx",encoding="utf-8",index_col="Name")
df=df.sort_values("Price")
df=df["Delivery"]=100  #เพิ่ม Column Delivery โดยมีข้อมูลเป็น 100 
df=df["Total"]=df["Price"]+df["Delivery"] #สร้าง Column total แสดงผลเท่ากับผลรวมของ Price กับ Delivery
