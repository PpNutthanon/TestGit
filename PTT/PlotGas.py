import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("PTT/DGA.csv")

# Display the first few rows of the dataframe
print(data.head())

# Define the conditions for each gas
conditions = {
    'H2': [(0, 100), (101, 700), (701, 1800), (1801, float('inf'))],
    'CH4': [(0, 120), (121, 400), (401, 1000), (1001, float('inf'))],
    'C2H2': [(0, 1), (2, 9), (10, 35), (36, float('inf'))],
    'C2H4': [(0, 50), (51, 100), (101, 200), (201, float('inf'))],
    'C2H6': [(0, 65), (66, 100), (101, 150), (151, float('inf'))],
    'CO': [(0, 350), (351, 570), (571, 1400), (1401, float('inf'))],
}

# Define the colors for the conditions
colors = ['green', 'yellow', 'orange', 'red']

# Create the plots
for gas, cond in conditions.items():
    plt.figure(figsize=(10, 6))
    for i, (min_val, max_val) in enumerate(cond):
        subset = data[(data[gas] >= min_val) & (data[gas] <= max_val)]
        plt.hist(subset[gas], bins=30, color=colors[i], alpha=0.5, label=f'Condition {i+1}')
    plt.title(f'Distribution of {gas} Concentrations')
    plt.xlabel('Concentration')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

# Initialize a dictionary to hold the results
percentage_results = {}

# Calculate the percentages for each condition in each gas
for gas, cond in conditions.items():
    percentage_results[gas] = {}
    total_valid_values = data[gas].count()  # exclude NaNs in the count
    for i, (min_val, max_val) in enumerate(cond):
        condition_count = data[(data[gas] >= min_val) & (data[gas] <= max_val)][gas].count()
        percentage = (condition_count / total_valid_values) * 100
        percentage_results[gas][f'Condition {i+1}'] = percentage

# Convert the results to a DataFrame for better visualization
percentage_df = pd.DataFrame(percentage_results)

percentage_df

# Create the plots with percentages
for gas, cond in conditions.items():
    plt.figure(figsize=(10, 6))
    for i, (min_val, max_val) in enumerate(cond):
        subset = data[(data[gas] >= min_val) & (data[gas] <= max_val)]
        # Get the percentage for the current condition
        percentage = percentage_df.loc[f'Condition {i+1}', gas]
        plt.hist(subset[gas], bins=30, color=colors[i], alpha=0.5, 
                 label=f'Condition {i+1} ({percentage:.2f}%)')
    plt.title(f'Distribution of {gas} Concentrations')
    plt.xlabel('Concentration')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
