#การสร้าง Dataframe จาก Series
import pandas as pd

#กำหนด Lists Data
name=["Keybord","Iphone","Pizza"]
category=["Computer","Telephone","Food"]
price=[2000,36000,400]

#นำ Lists มาทำเป็น Series
names=pd.Series(name)
categories=pd.Series(category)
prices=pd.Series(price)

#สร้าง Dictionary โดยสมาชิกคือ Series
frame={"Name":names,"Category":categories,"Price":prices}

#สร้าง Dataframe
df=pd.DataFrame(frame)
print(df)

