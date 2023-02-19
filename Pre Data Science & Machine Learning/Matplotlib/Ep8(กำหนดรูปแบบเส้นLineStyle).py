#รูปแบบเส้น => Line style
#รูปแบบย่อ => [marker][line][color] or [color][marker][line]
#? "-"=solid, "--"=dashed, "-."=dash-dot, ":"=dotted
import numpy as np
import matplotlib.pyplot as plt 
product=np.arange(10,60,10)
month=np.arange(1,6)

#* print(plt.plot(month,product,color="k",marker="x",linestyle=": ")) #แบบเต็ม
print(plt.plot(month,product,"kx:")) #แบบย่อ
plt.xlabel("Month"),plt.ylabel("Sale")
plt.show()