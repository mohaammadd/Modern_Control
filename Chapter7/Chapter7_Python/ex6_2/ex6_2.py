

import numpy as np
from scipy.signal import place_poles


# Define matrices and vectors
A = np.array([[0, 1, 0], [0, 0, 4.438], [0, -12, -24]])
b = np.array([[0], [0], [20]])
pd = np.array([-24, -3-3j, -3+3j])

# Place poles
result = place_poles(A, b, pd)
k = result.gain_matrix

print("Gain matrix k:")
print(k[0][0], k[0][1], k[0][2])