# Import excel sheet into python
import numpy as np
import pandas as pd
df = pd.read_excel(r"Sahara\TableA17.xlsx")
#print(df)

#* Declare variables for calculation
variables = ["t", "h", "pr", "u", "vr", "s"]
print("---Enter variables input (number)---")
print(" [1] : T ","\n","[2] : H ","\n","[3] : Pr","\n","[4] : u","\n","[5] : vr","\n","[6] : s")
data = int(input("Enter variables you want to input: "))


#* Check conditions which variable was selected
if data == 1: 
    t = float(input("Enter T value: "))
    values = df.loc[df[variables[data-1]] == t]
    if len(values) == 0:
        print("Required Equation")
        #Todo: เอาสูตรเข้ามาคำนวณ
    else:
        print(values)
        #Todo ลบให้output ไม่แสดง row 0 


elif data == 2:
    h = float(input("Enter h value: "))
    values = df.loc[df[variables[data-1]] == h]
    if len(values) == 0:
        print("Required Equation")
    else:
        print(values)


elif data == 3: 
    pr = float(input("Enter Pr value: "))
    values = df.loc[df[variables[data-1]] == pr]
    if len(values) == 0:
        print("Required Equation")
    else:
        print(values)


elif data == 4: 
    u = float(input("Enter u value: "))
    values = df.loc[df[variables[data-1]] == u]
    if len(values) == 0:
        print("Required Equation")
    else:
        print(values)


elif data == 5: 
    vr = float(input("Enter Vr value: "))
    values = df.loc[df[variables[data-1]] == vr]
    if len(values) == 0:
        print("Required Equation")
    else:
        print(values)


elif data == 6: 
    s = float(input("Enter s value: "))
    pr = float(input("Enter Pr value: "))
    values = df.loc[df[variables[data-1]] == s]
    if len(values) == 0:
        print("Required Equation")
    else:
        print(values)
else: 
    print("Wrong input")

print(variables)