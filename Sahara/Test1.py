import pandas as pd

def import_excel_data(file_path):
    return pd.read_excel(file_path)

def print_variable_choices(variables):
    print("---Enter variables input (number)---")
    for i, var in enumerate(variables, 1):
        print(f" [{i}] : {var.upper()}")

def get_data_from_user(variables):
    data = int(input("Enter variables you want to input: "))
    value = float(input(f"Enter {variables[data-1].upper()} value: "))
    return data, value

def find_values(df, var_index, input_value, variables):
    sorted_df = df.sort_values(by=variables[var_index-1])
    less_than_mask = sorted_df[variables[var_index-1]] < input_value
    greater_than_mask = sorted_df[variables[var_index-1]] > input_value

    closest_less_than = sorted_df[less_than_mask].iloc[-1] if less_than_mask.any() else None
    closest_greater_than = sorted_df[greater_than_mask].iloc[0] if greater_than_mask.any() else None
    exact_match = sorted_df[sorted_df[variables[var_index-1]] == input_value]

    return exact_match, closest_less_than, closest_greater_than

def get_interpolated_values(exact_values, values_less, values_greater, data, value, variables):
    if len(exact_values) == 0:
        values_less = values_less.tolist()
        values_greater = values_greater.tolist()
        interpolated_values = []
        ratio = (value - values_less[data-1]) / (values_greater[data-1] - values_less[data-1])
        for i in range(len(variables)):
            interpolated = values_less[i] + (ratio * (values_greater[i] - values_less[i]))
            interpolated_values.append(round(interpolated, 3))
    else:
        interpolated_values = exact_values.iloc[0].tolist()

    return interpolated_values

def main():
    file_path = r"Sahara\TableA17.xlsx"
    df = import_excel_data(file_path)
    variables = ["t", "h", "pr", "u", "vr", "s"]

    print_variable_choices(variables)
    data, value = get_data_from_user(variables)

    if 1 <= data <= 6:
        exact_values, values_less, values_greater = find_values(df, data, value, variables)
        interpolated_values = get_interpolated_values(exact_values, values_less, values_greater, data, value, variables)
        print("Interpolated values:", interpolated_values)
    else:
        print("Wrong input")

    r = float(input("Enter values of r: "))
    Prandtl_number2 = r * interpolated_values[2]

    pr_index = 3
    pr_values, pr_values_less, pr_values_greater = find_values(df, pr_index, Prandtl_number2, variables)
    pr_interpolated_values = get_interpolated_values(pr_values, pr_values_less, pr_values_greater, pr_index, Prandtl_number2, variables)
    print("Pr interpolated values:", pr_interpolated_values)

    efficiency = float(input("Enter the efficiency(%):")) / 100
    H2A = interpolated_values[1] + ((pr_interpolated_values[1] - interpolated_values[1]) / efficiency)
    H3, Pr3 = 1363.948, 303.54
    qin = H3 - H2A
    Pr4 = Pr3 / r

    print("qin:", qin)
    print("Pr4:", Pr4)

if __name__ == "__main__":
    main()

