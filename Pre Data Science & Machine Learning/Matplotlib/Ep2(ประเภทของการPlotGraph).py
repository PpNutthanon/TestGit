#ประเภทของการ Plot Graph => Line Plot/Line Graph, Bar Graph, Histogram, Scatter PLot, Pie Chart
#ต้องกำหนด ข้อมูลแกนx ข้อมูลแกนy โดบต้องเป็นข้อมูลแบบชุด เช่น List, Numpy, Array, Dataseries, Dataframe
import matplotlib.pyplot as plt
#*Todo Graph x(t)
#x=[-2,-2,-1,-1,0,0,1,1,2]
#y=[0,-1,0,1,1,2,2,1,0]
#*Todo Graph X(-t)
#x=[2,2,1,1,0,0,-1,-1,-2]
#y=[0,-1,0,1,1,2,2,1,0]

x=[0,1,1,2,2]
y=[3,3,1,-1,0]

#Plotเป็น Bar Graph 
plt.show() #ให้แสดงผลเป็นกราฟ

#Plotเป็น Line Graph
plt.title("Graph [x(t) + x(-t)]*u(t) ",loc="center")

plt.grid()
print(plt.plot(x,y))
plt.show()


