

import numpy as np
import control

# Define the matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])

b = np.array([[0],
              [1],
              [0],
              [-1]])

# Controllability matrix

C = control.ctrb(A,b)
a = np.array([0, -19.6, 0, 0])

alpha = np.array([12.86, 63.065, 149.38, 157.0])

Psi = np.array([[1, a[0], a[1], a[2]],
                [0, 1, a[0], a[1]],
                [0, 0, 1, a[0]],
                [0, 0, 0, 1]])

# Compute k
k = np.dot(alpha - a, np.linalg.inv(np.dot(C, Psi)))

print("k:", k)
