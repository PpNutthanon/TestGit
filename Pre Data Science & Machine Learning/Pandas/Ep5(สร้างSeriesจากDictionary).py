#การสร้าง Series จาก Dictionary
import pandas as pd
color={"Green":"เขียว","Red":"แดง","Yellow":"เหลือง"}
a=pd.Series(color)
print(a)

age={"John":50,"Steven":25,"Robert":30}
b=pd.Series(age)
print(b)