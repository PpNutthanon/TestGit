#การลบแถวกรณี Index เป็นข้อความ
#rows="Mango" Structures => df.drop("rows",axis=0,inplace=True)
#rows=["Mango","Banana"] Sturctures => df.drop(rows,axis=0,inplace=True)
import pandas as pd
df=pd.read_excel("Stock.xlsx",encoding="utf-8",index_col="Name")
print(df)

#ลบ ทีวี ออกจาก Dataframe
rows="ทีวี"
df.drop(rows,axis=0,inplace=True)
print(df)

#ลบ ปากกาก โคมไฟ โซฟา
rowss=["ทีวี","ปากกา","โซฟา"]
df.drop(rowss,axis=0,inplace=True)
print(df)
