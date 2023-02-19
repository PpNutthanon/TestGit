import matplotlib.pyplot as plt
t=[0,2,2,3,3,4]
x2=[0,1,1,-1,-1,0]
plt.xlabel('t')
plt.ylabel('x2(t)')
plt.title("Graph x2(t) vs t",loc="center")
plt.plot(t,x2)
plt.grid(), plt.show()