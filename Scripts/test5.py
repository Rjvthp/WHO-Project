import pandas as pd
from scipy.stats import chi2_contingency

# Read the data from the text file
df = pd.read_csv('test5.txt', delim_whitespace=True)

# Drop the 'Participant_Type' column as it is not needed for the analysis
df.drop('Participant_Type', axis=1, inplace=True)

# Remove the 'Unfamiliar' and 'Very_Unfamiliar' columns
df.drop(columns=['Unfamiliar', 'Very_Unfamiliar'], inplace=True, errors='ignore')

# Convert the dataframe to a numpy array for analysis
observed = df.values

# Perform chi-square test of independence
chi2, p, _, _ = chi2_contingency(observed)

# Print the results
print("Observed frequencies:")
print(observed)
print("\nChi-square Statistic:", chi2)
print("P-value:", p)
