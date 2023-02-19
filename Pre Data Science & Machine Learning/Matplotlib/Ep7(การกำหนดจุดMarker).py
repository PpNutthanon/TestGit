#การกำหนดจุด Marker => mark ตำแหน่งที่จับคู่ข้อมูลเอาไว้
#?  "."=point, "o"=cycle, "x"=xmarker, "+"=plus, "*"=star, "s"=square
#*! "|"=vline, "_"=hline, "v"=down, "^"=up, ">"=right, "<"=left
import numpy as np
import matplotlib.pyplot as plt
product=np.arange(10,60,10)
month=np.arange(1,6)
print(plt.plot(month,product,color="m",marker="o"))
plt.xlabel("Month"),plt.ylabel("Sale")
plt.show()