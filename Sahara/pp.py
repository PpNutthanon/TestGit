# Import excel sheet into python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"Sahara\TableA17.xlsx") #Todo: ดึงข้อมูลมาอ่านจากไฟล์ชื่อ TableA17.xlsx

#Todo: Declare variables for calculation
variables = ["t", "h", "pr", "u", "vr", "s"] #Todo: กำนหดค่าตามตารางชื่อใน excel
print("---Enter variables input (number)---")
for i, var in enumerate(variables, 1):
    print(f" [{i}] : {var.upper()}") #Todo: .upper() ทำให้เป็นตัวใหญ่

#Todo: Create function in order to check the condition (Exact or Interpolated)
def find_values(var_index, input_value):
    sorted_df = df.sort_values(by=variables[var_index-1]) #Todo: ทำให้ค่าเรียงกัน sort
    
    #* leass_than_mask and greater_than_mask จะให้ค่าเป็น True หรือ False เท่านั้น
    less_than_mask = sorted_df[variables[var_index-1]] < input_value #Todo: var_index - 1 เพราะว่า Python เริ่มนับตำแหน่งที่ 0
    greater_than_mask = sorted_df[variables[var_index-1]] > input_value
    
    if less_than_mask.any(): #* Bring Boolean:True in less_than_mask for calculation
        closest_less_than = sorted_df[less_than_mask].iloc[-1]  #Todo: [-1] คือ เอาตัวสุดท้ายมา
    else:
        closest_less_than = None
        
    if greater_than_mask.any():
        closest_greater_than = sorted_df[greater_than_mask].iloc[0] #Todo: [0] คือเอาตัวแรกมา
    else:
        closest_greater_than = None
        
    exact_match = sorted_df[sorted_df[variables[var_index-1]] == input_value]
    return exact_match, closest_less_than, closest_greater_than

data = int(input("Enter variables you want to input: ")) #Todo: Input เข้าไปในโปรแกรมว่าจะเอาตัวแปรไหน 1-6
value = float(input(f"Enter {variables[data-1].upper()} value: ")) #Todo: Input values of variable you selected

#Todo: Show the data and also interpoled calculation when the value not exactly the same in the excel sheet
if 1 <= data <= 6: #*: กำหนดให้ถ้า User ใส่เลข 1-6 มา จะทำงานบรรทัดนี้
    exact_values, values_less, values_greater = find_values(data, value) #Todo: ใช้ function find_values โดยให้ input_values เป็น exact_values, values_less, values_greater
    
    if len(exact_values) == 0: #Todo: ถ้าค่าที่เรากรอก ไม่เจอเลขเป๊ะๆในตาราง
        print("No exact match found. Closest values:")
        values_less   = values_less.tolist() #* เปลี่ยน type จาก pandas => list เพื่อจะได้คำนวณ interpolated ได้
        values_greater = values_greater.tolist()
        interpolated_values = []
        ratio = (value - values_less[data-1])/(values_greater[data-1] - values_less[data-1])
        for i in range(len(variables)):  #Todo: เริ่ม i=0 จบที่ i = ก่อน7 = 6
            interpolated = values_less[i] + (ratio * (values_greater[i] - values_less[i]))
            interpolated_values.append(round(interpolated,3)) #Todo: เพิ่มตัวแปรเข้าไปใน interpolated_values
        print(interpolated_values)
    else:
        print("Exact match found:")
        interpolated_values = exact_values.iloc[0].tolist() #Todo: เปลี่ยน exact_values จาก pandas=>list
        print(interpolated_values)
else:
    print("Wrong input")
print(variables)


#Todo: We start step3 here
#? ค่าของ Rp เป็นค่าอะไรได้บ้าง
#* Range of Pr = [0.3363, 3464]
#! Conditions Range of Rp which control to make the values of Pr2 not exceed than excel sheet
if 3464/interpolated_values[2] > 902.58:
    print("\n**** The range of Rp should be","[",round(0.3363/interpolated_values[2],3),",","902.58","] ****")
else:
    print("\n**** The range of Rp should be","[",round(0.3363/interpolated_values[2],3),",",round(3464/interpolated_values[2],3),"] ****")
r = float(input("Enter values of Rp: "))
Prandtl_number2 = r * interpolated_values[2]


# Call find_values function to check the value of Pr in the Excel sheet
pr_index = 3  # index of Pr in the variables list
pr_values, pr_values_less, pr_values_greater = find_values(pr_index, Prandtl_number2)
#Todo: Write the same prompt but change variables_name and date=3(Pr)

if len(pr_values) == 0:
    print("\nNo exact match found for Pr2. Closest values:")

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
    print("\nExact match found for Pr2:")
    pr_interpolated_values = pr_values.iloc[0].tolist()
    print(pr_interpolated_values)
    

#Todo: Declare constant H3 and Pr3 = f(1273) in Kelvin ; TIT = 1000 celcius degree = 1273 kelvin (เอาค่า T=1273 ไป interpolated)
H3, Prandtl_number3 = 1277.79, 238

compressor_efficiency  = 0.8
H2A = interpolated_values[1] + ((pr_interpolated_values[1] - interpolated_values[1])/ compressor_efficiency) 
qin = H3 - H2A
print("H2A=",round(H2A,3))
print("qin=",round(qin,3))

Prandtl_number4 = Prandtl_number3 / r #! The range of Rp should be [0.087, 902.58]

#Todo: Bring Values of Pr to calculate for the 4th time in order to find T4 and H4
pr4_values, pr4_values_less, pr4_values_greater = find_values(pr_index, Prandtl_number4)

if len(pr4_values) == 0:
    print("\nNo exact match found for Pr4. Closest values:")

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
    print("\nExact match found for Pr4:")
    pr4_interpolated_values = pr4_values.iloc[0].tolist()
    print(pr4_interpolated_values)

turbine_efficiency = 0.8
H4A = H3 - (turbine_efficiency*(H3 - pr4_interpolated_values[1]))
print("H4A=",round(H4A,3),"\n")
compressor_work = H2A - interpolated_values[1]
turbine_work    = H3 - H4A
thermal_efficiency = (turbine_work - compressor_work) / qin 
print("compressor_work:",round(compressor_work,3))
print("Turbine_work:",round(turbine_work,3))
print("\nThermal Efficiency: ",round(thermal_efficiency*100,3),"%") 


#Todo: Plot Graph Thermal Efficiency Vs Rp
x = [3,4,5,6,7,8,9,10,11,12,13,14,15]
y = [15.2, 17.8, 19.5, 20.59, 21.2, 21.6, 21.8, 21.8, 21.7, 21.6, 21.5, 20.59, 20.59]
plt.xlabel("Pressure Ratio")
plt.ylabel("Thermal Efficiency")
print(plt.plot(x,y))
plt.show()

