#การสร้าง Dataframe จาก Dictionary
import pandas as pd
product=[
    {"Name":"Keybord","Category":"Computer","Price":400},
    {"Name":"Doll","Category":"Fun","Price":500},
    {"Name":"Mouse","Category":"Computer","Price":300},
    {"Name":"Durian","Category":"Friut","Price":100}
] #สร้าง List โดยสมาชชิกด้านในเป็น Dictionary
df=pd.DataFrame(product)
di=df.set_index(["Name"])
print(df)
print(di)