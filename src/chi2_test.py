import pandas as pd
from scipy.stats import chi2
import numpy as np

SIGNIFICANCE_LEVEL = 0.05
GROUP_COLUMN = 'Most_Used_Platform'
BINARY_DATA_COLUMN = 'Affects_Academic_Performance'

def academic_performance_chi2(dataset, significance_level = SIGNIFICANCE_LEVEL, 
                              group_column = GROUP_COLUMN, data_column = BINARY_DATA_COLUMN) -> None:
    
    # Group data by platform
    grouped_data = dataset.groupby(group_column)

    # Get number of people and number of affected people by platform
    num_of_people = np.array([len(group) for _, group in grouped_data])
    num_of_affected_people = np.array([sum(group[data_column] == 'Yes') for _, group in grouped_data])

    # Calculate the expected number of affected people assuming the null hypothesis holds
    affected_coef = sum(num_of_affected_people) / sum(num_of_people)
    expected_affected_people = affected_coef * num_of_people

    # Calculate the chi_2 statistic
    chi_2 = sum((num_of_people - expected_affected_people)**2 / expected_affected_people)

    print(f"Calculated chi^2: {chi_2:.2f}")
    print(f"Table value chi^2: {chi2.ppf(1 - significance_level, len(num_of_people) - 1):.2f}")
    print(f"(With significance level: {significance_level} and degree of freedom: {len(num_of_people) - 1})")


# Load dataset
data = pd.read_csv('data/dataset.csv')

# Select the correct columns
selected_data = data.loc[:,[BINARY_DATA_COLUMN, GROUP_COLUMN]]

# Do the chi2 test
print("All data chi^2 test:")
academic_performance_chi2(selected_data)
print()

# Remove the LinkedIn "Outliers"
print("Chi^2 test without LinkedIn users:")
data_no_linkedin = selected_data.query(f"{GROUP_COLUMN} != 'LinkedIn'")
academic_performance_chi2(data_no_linkedin)

