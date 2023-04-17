# Import excel sheet into python
import pandas as pd
df = pd.read_excel(r"Sahara\TableA17.xlsx")

# Declare variables for calculation
variables = ["t", "h", "pr", "u", "vr", "s"]
print("---Enter variables input (number)---")
for i, var in enumerate(variables, 1):
    print(f" [{i}] : {var.upper()}")

def find_values(var_index, input_value):
    less_than_mask = df[variables[var_index-1]] < input_value
    greater_than_mask = df[variables[var_index-1]] > input_value
    
    if less_than_mask.any():
        closest_less_than = df[less_than_mask].iloc[-1]
    else:
        closest_less_than = None
        
    if greater_than_mask.any():
        closest_greater_than = df[greater_than_mask].iloc[0]
    else:
        closest_greater_than = None
        
    exact_match = df[df[variables[var_index-1]] == input_value]
    return exact_match, closest_less_than, closest_greater_than

data = int(input("Enter variables you want to input: "))
value = float(input(f"Enter {variables[data-1].upper()} value: "))

if 1 <= data <= 6:
    exact_values, values_less, values_greater = find_values(data, value)
    
    if len(exact_values) == 0:
        print("No exact match found. Closest values:")
        print("\nRow before:", values_less)
        print("\nRow after:", values_greater)
        values_less   = values_less.tolist()
        values_greater = values_greater.tolist()
        interpolated_values = []
        ratio = (value - values_less[data-1])/(values_greater[data-1] - values_less[data-1])
        for i in range(len(variables)):
            interpolated = values_less[i] + (ratio * (values_greater[i] - values_less[i]))
            interpolated_values.append(round(interpolated,3))
        print(interpolated_values)
        #! Error ตรงที่กรอกค่า Vr ที่ไม่ตรงกลับตาราง แล้วตารางโชว์ Row Before = Rowแรก และ Row After = Rowสุดท้าย ไม่ได้แสดงค่าที่ถูกจริงๆ
    else:
        print("Exact match found:")
        print(exact_values)
else:
    print("Wrong input")

print(variables)