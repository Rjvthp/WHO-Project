import numpy as np
from scipy.stats import chisquare

# Read data from the .txt file
with open('test2.txt', 'r') as file:
    # Initialize lists to store sections and frequencies
    sections = []
    frequencies = []
    # Iterate over each line in the file
    for line in file:
        # Split the line into section and frequency
        section, frequency = line.strip().split()
        # Append section and frequency to lists
        sections.append(section)
        frequencies.append(int(frequency))

# Convert the lists to NumPy arrays
sections = np.array(sections)
observed = np.array(frequencies)

# Calculate the total number of observations
total_obs = np.sum(observed)

# Calculate the expected frequencies based on proportions
expected = np.array([total_obs / len(sections)] * len(sections))

# Perform chi-square test
chi2, p = chisquare(observed, f_exp=expected)

# Print results
print("Chi-square Statistic:", chi2)
print("P-value:", p)
