import numpy as np
from scipy.stats import permutation_test

# Read data from the .txt file
data = []
with open('test6.txt', 'r') as file:
    next(file)  # Skip header line
    for line in file:
        line = line.strip().split(',')
        data.append([int(x) for x in line[1:]])

# Convert data into numpy array
data_array = np.array(data)

# Calculate mean difference between groups
observed_mean_diff = np.mean(data_array[:, 0]) - np.mean(data_array[:, 1])

# Perform permutation test
num_permutations = 1000  # Number of permutations
perm_mean_diffs = []
for _ in range(num_permutations):
    perm_data = np.random.permutation(data_array)
    perm_mean_diff = np.mean(perm_data[:, 0]) - np.mean(perm_data[:, 1])
    perm_mean_diffs.append(perm_mean_diff)

# Compute p-value
p_value = np.mean(np.abs(perm_mean_diffs) >= np.abs(observed_mean_diff))

# Print results
print("Permutation Test Statistic:", observed_mean_diff)
print("P-value:", p_value)
