#Linspace => กำหนดช่วง โดยเว้นระยะเท่าๆกัน
#เหมาะสำหรับการ Plot Graph
import numpy as np
# Structure => a=np.linspace(start,stop,number)
b=np.linspace(1,10) #กำหนดช่วง เลข 1 ถึง 10
print(b)
c=np.linspace(1,5,4)
print(c)
d=np.linspace(1,5,endpoint=False) #1จนถึงก่อนเลข5
print(d)