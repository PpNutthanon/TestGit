#Histogram แบบต่อเนื่อง =>
import matplotlib.pyplot as plt
import numpy as np
data = np.random.normal(10,2.5,5000)
plt.hist(data,bins=30) #? bins => กำหนดช่วงให้มีกี่ช่วง
plt.show()