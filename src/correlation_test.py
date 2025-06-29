import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

X_DATA = 'Avg_Daily_Usage_Hours'
Y_DATA = 'Sleep_Hours_Per_Night'

# Load dataset
data = pd.read_csv('data/dataset.csv')
x = data[X_DATA].values
y = data[Y_DATA].values

# Calculate the correlation
rho, p_value = spearmanr(x, y)
print(f"Spearman rho value: {rho:.2}")
print(f"p-value: {p_value}")

# Plot the data
plt.scatter(x, y, color='blue', marker='o')
plt.xlabel(X_DATA)
plt.ylabel(Y_DATA)
plt.grid(True)
plt.show()
