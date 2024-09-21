

import control as ctrl
import numpy as np

# System 1 definition
A1 = np.array([[-1, 1, 0],
               [0, -1, 0],
               [0, 0, -2]])
B1 = np.array([[0],
               [1],
               [1]])
C1 = np.array([4, -8, 9])
D1 = np.array([[0]])

sys1 = ctrl.ss(A1, B1, C1, D1)
tf_sys1 = ctrl.ss2tf(sys1)

print("System 1 Transfer Function:")
print(tf_sys1)

# System 2 definition
A2 = np.array([[-1, 0, 0],
               [1, -1, 0],
               [0, 0, -2]])
B2 = np.array([[4],
               [-8],
               [9]])
C2 = np.array([0, 1, 1])
D2 = np.array([[0]])

sys2 = ctrl.ss(A2, B2, C2, D2)
tf_sys2 = ctrl.ss2tf(sys2)

print("\nSystem 2 Transfer Function:")
print(tf_sys2)