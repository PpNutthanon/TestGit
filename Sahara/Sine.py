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
    less_than_mask = df[variables[var_index-1]] < value
    greater_than_mask = df[variables[var_index-1]] > value
    
    if less_than_mask.any():
        closest_less_than = df[less_than_mask].iloc[-1]
    else:
        closest_less_than = None
        
    if greater_than_mask.any():
        closest_greater_than = df[greater_than_mask].iloc[0]
    else:
        closest_greater_than = None
        
    exact_match = df[df[variables[var_index-1]] == value]
    return exact_match, closest_less_than, closest_greater_than

data = int(input("Enter variables you want to input: "))

if 1 <= data <= 6:
    exact_values, values_less, values_greater = find_values(data)
    
    if len(exact_values) == 0:
        print("No exact match found. Closest values:")
        print("\nRow before:", values_less)
        print("\nRow after:", values_greater)
        values_less   = values_less.tolist()
        value_greater = values_greater.tolist()
        #Todo: ใส่สูตรคำนวณโดยเอา value_less และ value_greater มาใช้
    else:
        print("Exact match found:")
        print(exact_values)
else:
    print("Wrong input")

print(variables)
