#การกำหนดสี(Color) => 'b'=blue, 'g'=green, 'r=red, 'c'=cyan, 'm'=magenta, 'y'=yellow, 'k'=black, 'w'=white
import numpy as np
import matplotlib.pyplot as plt
product1=np.arange(10,60,10)
month=np.arange(1,6)
print(plt.plot(month,product1)) #สีเดิม
plt.xlabel("Month"),plt.ylabel("Sale")
plt.show()
print(plt.plot(month,product1,color="g")) #สีใหม่
plt.show()
