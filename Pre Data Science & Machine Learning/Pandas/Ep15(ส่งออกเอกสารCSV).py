#การสร้าง Dataframe ส่งออก เอกสาร CSV
#Dataframe.to_csv(ตำแหน่งไฟล์,attribute)
#atrribute => header(หัวcolumn) , index
import pandas as pd
name=["Keybord","Iphone","Pizza"]
category=["Computer","Telephone","Food"]
price=[1200,38000,350]

#สร้าง Series
names=pd.Series(name)
categories=pd.Series(category)
prices=pd.Series(price)

#สร้าง Dictionary
frame={"Name":names,"Categories":categories,"Price":prices}

#สร้าง Dataframe
df=pd.DataFrame(frame)
print(df)

#Case1 => มีทั้ง หัวcolumn และ index
a=df.to_csv("Product1(Ep15pandas).csv")
print(a)

#Case2 => ไม่มี index
b=df.to_csv("Product2(Ep15pandas).csv",header=True,index=False)
print(b)

#Case3 => ไม่มี column
c=df.to_csv("Product3(Ep15pandas).csv",header=False,index=True)
print(c)

#Case4 => ไม่มี column และ ไม่มี index
d=df.to_csv("Product4(Ep15pandas).csv",header=False,index=False)
print(d)