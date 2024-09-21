

import numpy as np
import control
from scipy.linalg import null_space

# Define matrices A and B
A = np.array([[-3/2, 1/2],
              [1/2, -3/2]])

B = np.array([[1/2],
              [1/2]])

# Compute the controllability matrix C using control library
C = control.ctrb(A, B)

# Calculate the rank of the controllability matrix
rank_C = np.linalg.matrix_rank(C)

# Calculate the null space of the controllability matrix using scipy
null_C = null_space(C)

print("Controllability matrix (C):")
print(C)

print("\nRank of the controllability matrix:")
print(rank_C)

print("\nNull space of the controllability matrix:")
print(null_C)