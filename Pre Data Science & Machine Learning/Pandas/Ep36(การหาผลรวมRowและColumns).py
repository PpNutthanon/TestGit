#หาผลรวมข้อมูล Columns และ Rows
# axis=0(บนลลงล่าง) , aixs=1(ซ้ายไปขวา)
#Structures => df.sum(axis=ใส่ค้า) ;ค่าเริ่มต้นคือ axis=0
import pandas as pd
df=pd.read_excel("Stock.xlsx",encoding="utf-8",index_col="Name")
print(df)

# หาผลรวมของราคาของ Price และ Amount
print(df.sum(axis=0)) #ไม่ต้องใส่ axis=0 ก็ได้ เพราะป็นค่าเริ่มต้นอยู่แล้ว

#หาผลรวมของ Price กับ Amount รวมกัน
print(df.sum(axis=1))