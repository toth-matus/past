import pandas as pd
import matplotlib.pyplot as plt

GROUP_COLUMN = 'Most_Used_Platform'
VALUE_COLUMN = 'Avg_Daily_Usage_Hours'

def get_group_average(group, value_column=VALUE_COLUMN) -> float:
    raw_data = group[value_column].values
    average = sum(raw_data)/len(raw_data)

    return average

# Load dataset
data = pd.read_csv('data/dataset.csv')

# Select the correct columns
selected_data = data.loc[:,[VALUE_COLUMN, GROUP_COLUMN]]
grouped_data = selected_data.groupby(GROUP_COLUMN)

# Calculate average for all groups
platforms = []
averages = []
for name, group_data in grouped_data:
    group_average = get_group_average(group_data)
    print(f"{name} average screen time: {group_average:.2f} hours")

    averages.append(group_average)
    platforms.append(name)

# Plot data
plt.bar(platforms, averages)
plt.ylabel(f"Average {VALUE_COLUMN}")
plt.show()

