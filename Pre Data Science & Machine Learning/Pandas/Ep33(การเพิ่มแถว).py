#การเพิ่มข้อมูล/เพิ่มแถว => df.append(newdf)
#newdf=pd.Dataframe(....)
import pandas as pd
df=pd.read_excel("Stock.xlsx",encoding="utf-8",index_col="Name")

#สร้าง Dataframe อันใหม่ (Coumn ต้องตรงกับ Dataframe ที่จะใส่เข้าไป)
products=[["Headphones","Ear Monitor",400,20,500],["Charging Lan","Computer",1400,20,1500]]
cols=["Name","Group","Price","Quantity","Summation"]
newdf=pd.DataFrame(data=products,columns=cols)
newdf=newdf.set_index("Name",inplace=True)

#เพิ่มข้อมูลเข้าไปใน Dataframe อันเก่า
df=df.append(newdf)
print(df)