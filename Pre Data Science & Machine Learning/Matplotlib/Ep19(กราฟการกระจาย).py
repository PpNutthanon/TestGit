# กราฟการกระจาย(Scatter) => Plotจุด => plt.scatter(x,y,s=sizes,c=colors)
#?  Ex นำไปใช้กระจายรายได้ของประชาร
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,2,5.6,4.5,7]
sizes=[100,200,800,100,300]
colors=["red","orange","green","purple","yellow"]
plt.scatter(x,y,s=sizes,c=colors)
plt.show()