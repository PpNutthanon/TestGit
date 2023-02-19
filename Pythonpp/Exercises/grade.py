import numpy as np
import pandas as pd
from numpy.core.fromnumeric import transpose
subject,weight,grade,sumgrade=[],[],[],[]
cols=["Subject","Weight","Grade"]
number=int(input("Enter The Number of Subject You Enroll :"))
idx=np.arange(1,number+1)
for i in range(1,number+1):
    sub=input("Enter The Name Of The Subject :")
    mass=float(input("Enter The Weight Of "+sub+" :"))
    get=float(input("Enter The Grade You Got In "+sub+":"))
    print("\n")
    subject.append(sub)
    weight.append(mass)
    grade.append(get)
for j in range(number):
    a=weight[j]*grade[j]
    sumgrade.append(a)
df=pd.DataFrame([subject,weight,grade],index=idx,columns=cols)
print(df)
print("\n")
print("Your Grade Is :",sum(sumgrade)/sum(weight))

