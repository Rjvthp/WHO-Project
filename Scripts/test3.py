import pandas as pd
from scipy.stats import chi2_contingency

# Read data from the .txt file using pandas
df = pd.read_csv('test3.txt', delim_whitespace=True)
print("Data from file:")
print(df)

# Print column names and data types
print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# Specify columns containing observed frequencies
observed_columns = ['Elective', 'Emergency']

# Convert observed frequencies to numeric values
for column in observed_columns:
    df[column] = pd.to_numeric(df[column])

# Replace NaN values with zeros
df.fillna(0, inplace=True)

# Extract observed frequencies as a NumPy array
observed = df[observed_columns].values
print("\nObserved frequencies:")
print(observed)

# Perform chi-square test of independence
chi2, p, _, _ = chi2_contingency(observed)

# Print results
print("\nChi-square Statistic:", chi2)
print("P-value:", p)

