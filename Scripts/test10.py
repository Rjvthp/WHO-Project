import numpy as np
from mlxtend.evaluate import permutation_test

try:
    # Load data from the text file
    with open('test10.txt', 'r') as file:
        lines = file.readlines()

    # Parse the data
    participant_groups = []
    checklist_data = []

    # Skip the header line
    lines = lines[1:]

    for line in lines:
        parts = line.strip().split(',')
        participant_groups.append(parts[0])
        checklist_data.append([int(x) if x else 0 for x in parts[1:]])

    checklist_data = np.array(checklist_data)

    # Ensure the dimensions of the arrays are correct
    y = checklist_data[:, 1:]
    X = checklist_data[:, 0]

    # Perform the permutation test
    p_value = permutation_test(X, y.ravel(), method='approximate', num_rounds=10000, seed=0)

    # Print the results
    print("P-value:", p_value)

except FileNotFoundError:
    print("Error: File 'test10.txt' not found.")
except ValueError as ve:
    print("ValueError:", ve)
except Exception as e:
    print("An error occurred:", e)
