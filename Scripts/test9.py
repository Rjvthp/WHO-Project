import numpy as np
from mlxtend.evaluate import permutation_test

try:
    # Load data from the text file
    with open('test9.txt', 'r') as file:
        lines = file.readlines()

    # Parse the data
    participant_groups = []
    checklist_data = []

    # Skip the header line if it exists
    if lines[0].startswith("Participant_Group"):
        lines = lines[1:]

    for line in lines:
        parts = line.strip().split(',')
        participant_groups.append(parts[0])
        checklist_data.append([int(x) for x in parts[1:]])

    if not checklist_data:
        raise ValueError("No data found in the file.")

    checklist_data = np.array(checklist_data)

    # Ensure the dimensions of the arrays are correct
    y = checklist_data[:, 0]
    X = checklist_data[:, 1:]

    # Compute the number of permutations based on data size
    num_permutations = min(10000, np.math.factorial(len(y)))

    # Perform the permutation test
    p_value = permutation_test(y, X.ravel(), method='approximate', num_rounds=num_permutations, seed=0)

    # Print the results
    print("P-value:", p_value)

except FileNotFoundError:
    print("Error: File 'test9.txt' not found.")
except ValueError as ve:
    print("ValueError:", ve)
except Exception as e:
    print("An error occurred:", e)
