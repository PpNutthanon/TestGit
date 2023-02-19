#การสร้าง Dataframe จาก List ด้วย Zip => ผลลัพธ์ แตกต่างจาก การสร้าง Dataframe จาก list ปกติ
import pandas as pd
item1=["Keybord","Iphone","Pizza"]
item2=["Computer","Telephone","Food"]
item3=[3000,30000,300]
datas=list(zip(item1,item2,item3)) #เอา item1 item2 item3 เก็บลงใน datas
col=["Product","Categories","Price"]
df=pd.DataFrame(datas,columns=col)
print(df)
