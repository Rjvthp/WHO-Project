import pandas as pd
from scipy.stats import chi2_contingency
import re

# Read data from the .txt file
with open('test4.txt', 'r') as file:
    lines = file.readlines()

# Prepare data
data = []
for line in lines:
    # Split the line by whitespace
    parts = re.split(r'\s{2,}', line.strip())
    data.append(parts)

# Create DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Drop 'Total' column if it exists
if 'Total' in df.columns:
    df.drop('Total', axis=1, inplace=True)

# Prepare observed frequencies array
observed = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0).values

# Print data from file
print("Data from file:")
print(df)
print()

# Print DataFrame shape
print("DataFrame shape:", df.shape)
print()

# Print observed frequencies
print("Observed frequencies:")
print(observed)
print()

# Perform chi-square test of independence
chi2, p, _, _ = chi2_contingency(observed)

# Print results
print("Chi-square Statistic:", chi2)
print("P-value:", p)
