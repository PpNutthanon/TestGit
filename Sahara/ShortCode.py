# Import excel sheet into python
import pandas as pd
df = pd.read_excel(r"Sahara\TableA17.xlsx")

# Declare variables for calculation
variables = ["t", "h", "pr", "u", "vr", "s"]
print("---Enter variables input (number)---")
for i, var in enumerate(variables, 1):
    print(f" [{i}] : {var.upper()}")

def find_values(var_index):
    value = float(input(f"Enter {variables[var_index-1].upper()} value: "))
    values = df.loc[df[variables[var_index-1]] == value]
    return values

data = int(input("Enter variables you want to input: "))

if 1 <= data <= 6:
    values = find_values(data)
    if len(values) == 0:
        print("Required Equation")
        #Todo: เอาสูตรเข้ามาคำนวณ
    else:
        print(values)
        #Todo ลบให้output ไม่แสดง row(ไม่ทำก็ได้)
else:
    print("Wrong input")

print(variables)
