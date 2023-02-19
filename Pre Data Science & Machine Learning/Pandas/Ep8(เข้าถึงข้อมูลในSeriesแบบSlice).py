#การเข้าถึงข้อมูลใน Series (แบบช่วงข้อมูล Slice) => เหมือน slice แบบใน array
import pandas as pd
import numpy as np
data=np.array([12,20,5,8,0])
ps=pd.Series(data)
print(ps)
print(ps[1:3]) #แสดงผลของ index ใน series ps indexที่ 1 จนถึง ก่อน 3
print(ps[1:])
print(ps[:3])
