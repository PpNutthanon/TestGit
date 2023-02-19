#การเข้าถึงข้อมูลใน Series
import pandas as pd
data=[10,20,30,40]
a=pd.Series(data)
print(a)
print(a[2],"\n")

color={"Grape":50,"Mango":40,"Banana":30}
b=pd.Series(color)
print(b)
print(b["Mango"])