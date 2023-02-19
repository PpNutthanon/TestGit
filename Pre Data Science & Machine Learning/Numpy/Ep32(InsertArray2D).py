#Insert Array 2D => np.insert(array,index,number,axis)
import numpy as np
a=np.array([[1,2],[3,4]])
print(a)

a=np.insert(a,1,100,axis=0)
print(a)
a=np.insert(a,1,50,axis=1)
print(a)
a=np.insert(a,1,[10,20,30],axis=1)
print(a)