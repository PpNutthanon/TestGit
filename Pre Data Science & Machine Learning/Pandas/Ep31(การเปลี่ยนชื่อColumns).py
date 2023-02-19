#การเปลี่ยนชื่อ Columns => df.rename(columns=cols,inplace=True)
#cols={"ชื่อเดิม1":"ชื่อใหม่1","ชื่อเดิม2":"ชื่อใหม่2"}
import pandas as pd
df=pd.read_excel("Stock.xlsx",encoding="utf-8",index_col="Name")
cols={"Category":"Group"}
change=df.rename(columns=cols,inplace=True) #เปลี่ยนชื่อ Columns จาก Category เป็น Group
print(df)