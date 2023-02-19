#การเลือกข้อมูลและแถวที่ต้องการ
#df[Start:Stop]
#df[Start:Stop].ชื่อColumn
#df.loc[Start:Stop,ชื่อColumn1,ชื่อColumn2]
import pandas as pd
df=pd.read_excel("dataupdates.xlsx","weather",encoding="utf-8",index_col="Day")
print(df[:])
print(df[1:4])
print(df[2:6].Event)
print(df.loc["2020-12-02"]["Event"])