# Import excel sheet into python
import pandas as pd
df = pd.read_excel(r"Sahara\TableA17.xlsx")

# Declare variables for calculation
variables = ["t", "h", "pr", "u", "vr", "s"]
print("---Enter variables input (number)---")
for i, var in enumerate(variables, 1):
    print(f" [{i}] : {var.upper()}")

def find_values(var_index, input_value):
    sorted_df = df.sort_values(by=variables[var_index-1])
    
    less_than_mask = sorted_df[variables[var_index-1]] < input_value
    greater_than_mask = sorted_df[variables[var_index-1]] > input_value
    
    if less_than_mask.any():
        closest_less_than = sorted_df[less_than_mask].iloc[-1]
    else:
        closest_less_than = None
        
    if greater_than_mask.any():
        closest_greater_than = sorted_df[greater_than_mask].iloc[0]
    else:
        closest_greater_than = None
        
    exact_match = sorted_df[sorted_df[variables[var_index-1]] == input_value]
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
        ratio = (value - values_less[data-1])/(values_greater[data-1] - values_less[data-1])
        a = values_less[0] + (ratio * (values_greater[0] - values_less[0]))
        b = values_less[1] + (ratio * (values_greater[1] - values_less[1]))
        c = values_less[2] + (ratio * (values_greater[2] - values_less[2]))
        d = values_less[3] + (ratio * (values_greater[3] - values_less[3]))
        e = values_less[4] + (ratio * (values_greater[4] - values_less[4]))
        f = values_less[5] + (ratio * (values_greater[5] - values_less[5]))
        final_value = [a,b,c,d,e,f]
        print(final_value)
        #? ถ้าใส่ input t, h, pr, u, vr, s จะเอาตัวแปรไหนมาเป็น references ในการคำนวณ 
        #Todo (tb - tl)/(tg-tl) = (x - tl)/(tg-tl)
    else:
        print("Exact match found:")
        print(exact_values)
else:
    print("Wrong input")

print(variables)