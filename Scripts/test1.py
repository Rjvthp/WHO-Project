import numpy as np
from scipy.stats import chisquare

# Read data from the .txt file
with open('test1.txt', 'r') as file:
    data = file.read().strip().split(',')
    observed = np.array(list(map(int, data)))

# Calculate expected frequencies (assuming equal probabilities under the null hypothesis)
expected = np.full_like(observed, fill_value=np.sum(observed) / len(observed))

# Perform chi-square test
chi2, p = chisquare(observed, f_exp=expected)

# Print results
print("Chi-square Statistic:", chi2)
print("P-value:", p)
