

import numpy as np
import control
from scipy.linalg import null_space

# Define matrices A and C
A = np.array([[-3/2, 1/2],
              [1/2, -3/2]])

C = np.array([[1, -1]])

# Compute the observability matrix O using control library
O = control.obsv(A, C)

# Calculate the rank of the observability matrix
rank_O = np.linalg.matrix_rank(O)

# Calculate the null space of the observability matrix using scipy
null_O = null_space(O)

print("Observability matrix (O):")
print(O)

print("\nRank of the observability matrix:")
print(rank_O)

print("\nNull space of the observability matrix:")
print(null_O)