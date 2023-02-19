import matplotlib.pyplot as plt
import datetime as dt
import math 
start = dt.datetime(2021,8,2)
final = dt.datetime.now()
print(final-start)

point1=[-3,2,1]
point2=[0.585,-1.607,4.698]
print(math.dist(point1,point2))