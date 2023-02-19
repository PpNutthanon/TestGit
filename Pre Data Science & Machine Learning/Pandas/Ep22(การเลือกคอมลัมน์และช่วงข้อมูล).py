#การเลือก Column และ เลือกข้อมูลแบบช่วง 
#การเลือก column => Dataframe.columns
#แบบกำหนดช่วง => df[["column1","cloumn2"]][start:stop] , df.column[start:stop]
import pandas as pd
df=pd.read_excel("dataupdates.xlsx","weather",encoding="utf-8",index_col="Day")
print(df.Temperature[1:5])
print(df[["Temperature","Event"]][1:3])
