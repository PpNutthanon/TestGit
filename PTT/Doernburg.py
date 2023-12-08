#Import Libraries in order to Read Excel Files
import pandas as pd

#TODO: Read Data From Excel Sheet That We Imported 
file_path = "PTT/DGA.xlsx"
try:
    df = pd.read_excel(file_path)
    print(df)
except FileNotFoundError:
    print(f"File not found: {file_path}")

#TODO: Define GSP Area and Specific Tax ID of Transformers
areas = {
    "GSP1": ["700TR001B", "700TR001A", "700TR002A", "700TR002B", "700TR003A", "700TR003B", "700TR004A", "700TR004B", "700TR006", "700TR007", "700TR005"],
    "GSP2": ["796TR001A", "796TR001B", "797TR011", "797TR012"],
    "GSP3": ["3328TR001A", "3328TR001B", "3328TR002A", "3328TR002B", "3328TR003A", "3328TR003B", "3328TR004A", "3328TR004B", "3328TR005A", "3328TR005B", "3325CLR001", "3325TR001A", "3325TR001B", "3325TR001C", "3328TR006A", "3328TR006B"],
    "GSP5":["3525TR01A", "3525TR01B", "3525TR02", "3528TR01A", "3528TR01B", "3528TR02A", "3528TR02B", "3528TR03", "3528TR03A", "3528TR03B", "3528TR04", "3528TR104", "3528TR105"],
    "GSP6" : ["3625TR01", "3628TR01A", "3628TR01B", "3628TR02A", "3628TR02B", "3628TR03A", "3628TR03B", "3628TR04A", "3628TR04B", "3628TR05A", "3628TR05B", "3628TR06A", "3628TR06B", "3608PM002TR1", "3608PM002TR2", "3621TR01"],
    "CS" : ["3629TR201A", "3629TR201AOLTC", "3629TR201B", "3629TR201BOLTC", "3629TR202"],
    "ESP" : ["3228TR01A", "3228TR01B", "3228TR01C", "3228TR01D", "3228TR02A", "3228TR02B", "3228TR03A", "3228TR03B", "3228TR04A", "3228TR04B", "3225TR02A", "3225TR02B", "3225TR01"],
    "GPPP" : ["300TR001", "300TR001A", "3000TR001", "3000TR002", "5500TR001", "5550TR001", "5550TR002", "5550LBTR001", "5560TR001", "5560TR002", "310TR01A", "310TR01B", "310TR02A", "310TR02B", "5560TR003"],
    "CWWTP": ["3290TR001","3290TR002"]
}

#TODO: Ask Users for Input GSP Area
print("---Enter the number of the GSP Area you want---")
for i, area_name in enumerate(areas, start=1):
    print(f"[{i}] : {area_name}")

user_choice = int(input("Enter GSP Area: ")) - 1

#TODO: Check The User Input The Correct Data of Area
if 0 <= user_choice < len(areas):
    # Get the name of the selected area
    selected_area_name = list(areas.keys())[user_choice]
    
    #TODO: Display tax IDs for User Selected Area
    print(f"---Enter Tax ID number you want in {selected_area_name}---")
    for i, tag_id in enumerate(areas[selected_area_name], start=1):
        print(f"[{i}] : {tag_id}")
    
    tag_id_choice = int(input("Enter Tax ID number: ")) - 1
    print("\n")

    #TODO: Check The User Input The Correct Data of Area
    if 0 <= tag_id_choice < len(areas[selected_area_name]):
        selected_tag_id = areas[selected_area_name][tag_id_choice]
        print(f"Tag ID: {selected_tag_id}")

        #TODO: Show The Data Just only Specific Transformer We Input
        mask_tagid = df['TAGID'] == selected_tag_id

        #TODO: Additional filtering criteria to exclude rows where certain columns have '-'
        columns_to_check = ['H2', 'O2', 'N2', 'C2H2', 'C2H4', 'C2H6', 'CH4', 'CO']
        Blank_Data = (df[columns_to_check] != '-').all(axis=1)
        
        #TODO: Combine The Conditions Together and Display Data 
        final_mask = mask_tagid & Blank_Data
        
        filtered_data = df[final_mask]
        print(filtered_data,"\n")

       #TODO: Extract the data from the columns into separate lists
        H2 = filtered_data['H2'].tolist()
        O2 = filtered_data['O2'].tolist()
        N2 = filtered_data['N2'].tolist()
        C2H2 = filtered_data['C2H2'].tolist()
        C2H4 = filtered_data['C2H4'].tolist()
        C2H6 = filtered_data['C2H6'].tolist()
        CH4 = filtered_data['CH4'].tolist()
        CO = filtered_data['CO'].tolist()

        #TODO: Example: Printing extracted lists
        print("H2:", H2)
        print("O2:", O2)
        print("N2:", N2)
        print("C2H2:", C2H2)
        print("C2H4:", C2H4)
        print("C2H6:", C2H6)
        print("CH4:", CH4)
        print("CO:", CO)

    else:
        print("You entered the wrong input for Tax ID")
else:
    print("You entered the wrong input for GSP Area")

#TODO: Calculate Doernburg Conditions
try:
    Ratio1 = CH4/H2
    Ratio2 = C2H2/C2H4
    Ratio3 = C2H2/CH4
    Ratio4 = C2H6/C2H2
    print(Ratio1)
    print(Ratio2)
    print(Ratio3)
    print(Ratio4)
except:
    print("Cannot Calculate Because Denominators Equal to Zero")

if Ratio1 > 1 and Ratio2 < 0.75 and Ratio3 < 0.3 and Ratio4 > 0.4:
    print(f"Thermal Decomposition in Transformer {selected_tag_id}")
elif Ratio1 < 1 and Ratio3 < 0.3 and Ratio4 > 0.4:
    print(f"Partial Discharge (PD-Low Intensity) in Transformer {selected_tag_id}")
elif 0.1 < Ratio1 < 1 and Ratio2 > 0.75 and Ratio3 > 0.3 and Ratio4 < 0.4:
    print(f"Arcing (PD-High Intensity) in Transformer {selected_tag_id}")