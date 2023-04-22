# Import excel sheet into python
import pandas as pd
df = pd.read_excel(r"Sahara\TableA17.xlsx")

#Todo: Declare variables for calculation
variables = ["t", "h", "pr", "u", "vr", "s"]
print("---Enter variables input (number)---")
for i, var in enumerate(variables, 1):
    print(f" [{i}] : {var.upper()}")

#Todo: Create function in order to check the condition 
def find_values(var_index, input_value):
    sorted_df = df.sort_values(by=variables[var_index-1])
    
    less_than_mask = sorted_df[variables[var_index-1]] < input_value
    greater_than_mask = sorted_df[variables[var_index-1]] > input_value
    
    if less_than_mask.any(): #* Bring Boolean:True in less_than_mask for calculation
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

#Todo: Show the data and also interpoled calculation when the value not exactly the same in the excel sheet
if 1 <= data <= 6:
    exact_values, values_less, values_greater = find_values(data, value)
    
    if len(exact_values) == 0:
        print("No exact match found. Closest values:")
        values_less   = values_less.tolist()
        values_greater = values_greater.tolist()
        interpolated_values = []
        ratio = (value - values_less[data-1])/(values_greater[data-1] - values_less[data-1])
        for i in range(len(variables)):
            interpolated = values_less[i] + (ratio * (values_greater[i] - values_less[i]))
            interpolated_values.append(round(interpolated,3))
        print(interpolated_values)
    else:
        print("Exact match found:")
        interpolated_values = exact_values.iloc[0].tolist()
        print(interpolated_values)
else:
    print("Wrong input")
print(variables)

#Todo: We start step3 here
#* Range of Pr = [0.3363, 3464]
#! Conditions Range of Rp
if 3464/interpolated_values[2] > 902.58:
    print("\n**** The range of Rp should be","[",round(0.3363/interpolated_values[2],3),",","902.58","] ****")
else:
    print("\n**** The range of Rp should be","[",round(0.3363/interpolated_values[2],3),",",round(3464/interpolated_values[2],3),"] ****")
r = float(input("Enter values of Rp: "))
Prandtl_number2 = r * interpolated_values[2]


# Call find_values function to check the value of Pr in the Excel sheet
pr_index = 3  # index of Pr in the variables list
pr_values, pr_values_less, pr_values_greater = find_values(pr_index, Prandtl_number2)

if len(pr_values) == 0:
    print("\nNo exact match found for Prandtl_number2. Closest values:")

    if pr_values_less is not None:
        pr_values_less = pr_values_less.tolist()
    if pr_values_greater is not None:
        pr_values_greater = pr_values_greater.tolist()

    pr_interpolated_values = []
    if pr_values_less is not None and pr_values_greater is not None:
        pr_ratio = (Prandtl_number2 - pr_values_less[pr_index-1])/(pr_values_greater[pr_index-1] - pr_values_less[pr_index-1])
        for i in range(len(variables)):
            pr_interpolated = pr_values_less[i] + (pr_ratio * (pr_values_greater[i] - pr_values_less[i]))
            pr_interpolated_values.append(round(pr_interpolated, 3))
    else:
        pr_interpolated_values = pr_values_less if pr_values_less is not None else pr_values_greater
    print(pr_interpolated_values)
else:
    print("\nExact match found for Prandtl_number2:")
    pr_interpolated_values = pr_values.iloc[0].tolist()
    print(pr_interpolated_values)
    

#Todo: Declare constant H3 and Pr3 = f(1273) in Kelvin ; TIT = 1000 celcius degree
H3, Prandtl_number3 = 1363.948, 303.54

#! Not Finish and Not Complete on the way to find the range
if pr_interpolated_values[1] - interpolated_values[1] < 0:
    print("Compressor Efficiency should more than: ",((H3-interpolated_values[1])/(pr_interpolated_values[1]-interpolated_values[1]))*100,"%")
elif pr_interpolated_values[1] - interpolated_values[1] > 0:
    print("Compressor Efficiency should less than: ",((H3-interpolated_values[1])/(pr_interpolated_values[1]-interpolated_values[1]))*100,"%")

compressor_efficiency  = float(input("Enter compressor efficiency(%):"))/100
H2A = interpolated_values[1] + ((pr_interpolated_values[1] - interpolated_values[1])/ compressor_efficiency) 
qin = H3 - H2A
Prandtl_number4 = Prandtl_number3 / r #! The range of Rp should be [0.087, 902.58]

#Todo: Bring Values of Pr to calculate for the 4th time in order to find T4 and H4
pr4_values, pr4_values_less, pr4_values_greater = find_values(pr_index, Prandtl_number4)

if len(pr4_values) == 0:
    print("\nNo exact match found for Prandtl_number4. Closest values:")

    if pr4_values_less is not None:
        pr4_values_less = pr4_values_less.tolist()
    if pr4_values_greater is not None:
        pr4_values_greater = pr4_values_greater.tolist()

    pr4_interpolated_values = []
    if pr4_values_less is not None and pr4_values_greater is not None:
        pr4_ratio = (Prandtl_number4 - pr4_values_less[pr_index-1])/(pr4_values_greater[pr_index-1] - pr4_values_less[pr_index-1])
        for i in range(len(variables)):
            pr4_interpolated = pr4_values_less[i] + (pr4_ratio * (pr4_values_greater[i] - pr4_values_less[i]))
            pr4_interpolated_values.append(round(pr4_interpolated, 3))
    else:
        pr4_interpolated_values = pr4_values_less if pr4_values_less is not None else pr4_values_greater
    print(pr4_interpolated_values)
else:
    print("\nExact match found for Prandtl_number4:")
    pr4_interpolated_values = pr4_values.iloc[0].tolist()
    print(pr4_interpolated_values)

turbine_efficiency = float(input("Enter turbine efficiency(%): "))/100
H4A = H3 - (turbine_efficiency*(H3 - pr4_interpolated_values[1]))
compressor_work = H2A - interpolated_values[1]
turbine_work    = H4A - H3
thermal_efficiency = qin / (turbine_work - compressor_work)
print("\nThermal Efficiency: ",round(thermal_efficiency,3)) 

#? Thermal Efficiency ติดลบไม่ได้ แต่บางครั้ง run program แล้วได้ค่าติดลบ
#! Find suitable range for compressor_efficiency and turbine_efficiency   


#Todo: H2A => State2 Actual ()
# 1 = อากาศภายนอก
# 2 = อัดขึ้นไป 
# s= isentopic