# Import excel sheet into python
import numpy as np
import pandas as pd
df = pd.read_excel(r"Sahara\TableA17.xlsx")
#print(df)

variables = ["t", "h", "pr", "u", "vr", "s"]
print("---Enter variables input (number)---")
print(" [1] : T ","\n","[2] : H ","\n","[3] : Pr","\n","[4] : u","\n","[5] : vr","\n","[6] : s")
data = int(input("Enter variables you want to input: "))

#Todo: Check conditions which variable was selected
if data == 1: t = float(input("Enter T value: "))
    #หาว่ามีค่า t เป๊ะๆใน column t มั้ย
elif data == 2: h = float(input("Enter h value: "))
elif data == 3: pr = float(input("Enter Pr value: "))
elif data == 4: u = float(input("Enter u value: "))
elif data == 5: vr = float(input("Enter Vr value: "))
elif data == 6: s = float(input("Enter s value: "))
else: print("Wrong input")

print(variables)