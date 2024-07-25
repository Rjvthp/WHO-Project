import numpy as np
from mlxtend.evaluate import permutation_test

# Load data from the text file
with open('test8.txt', 'r') as file:
    lines = file.readlines()

# Parse the data
participant_groups = []
training_data = []

# Skip the header line if it exists
lines = lines[1:] if lines[0].startswith("Participant_Group") else lines

for line in lines:
    parts = line.strip().split(',')
    participant_groups.append(parts[0])
    training_data.append([int(x) if x else 0 for x in parts[1:]])

training_data = np.array(training_data)

# Ensure the dimensions of the arrays are correct
y = training_data[:, 0]
X = training_data[:, 1:].reshape(-1)

# Perform the permutation test
p_value = permutation_test(y, X, method='approximate', num_rounds=10000, seed=0)

# Print the results
print("P-value:", p_value)
