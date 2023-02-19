#Dataframe การอ่านเอกสาร CSV(การกำหนด Header)
import pandas as pd
colname=["ชื่อ","สินค้า","ราคา"]
a=pd.read_csv("Product1(Ep15pandas).csv",encoding="utf-8",names=colname)
print(a)