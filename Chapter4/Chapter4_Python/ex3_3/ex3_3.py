

import numpy
from sympy import symbols,exp, integrate, Matrix
from scipy.linalg import expm

A = Matrix([[0,6],[-1,-5]])
# Symbolically define time variable t
t = symbols('t')

# Calculate the matrix exponential phi = expm(A*t)
phi = exp(A * t)
# Print the symbolic expression
phi = np.array(phi)
print(phi)

