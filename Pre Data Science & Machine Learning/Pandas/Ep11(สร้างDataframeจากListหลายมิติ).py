#การสร้าง Dataframe จาก List แบบหลายมิติ
import pandas as pd
data=[["Keybord","Computer",1000],["Iphone","Telephone",30000],["Pizza","Food",300]]
col=["Product","Categories","Price"]
idx=1,2,3
df=pd.DataFrame(data,columns=col,index=idx)
print(df)
