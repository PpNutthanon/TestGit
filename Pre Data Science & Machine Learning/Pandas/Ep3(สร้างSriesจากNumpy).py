import numpy as np
import pandas as pd
data=np.array([10,20,30,"Pp",False])
idx=[1,2,3,4,5]
print(data)
ps=pd.Series(data,index=idx)
print(ps)
