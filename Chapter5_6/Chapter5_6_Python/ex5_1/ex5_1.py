

import control
import numpy as np

# Definition of System 1
A = np.array([[0, 1, 0], [0, 0, 1], [-5, -11, -6]])
B = np.array([[0], [0], [1]])
C = np.array([[1, 0, 1]])
D = np.array([[0]])
sys1 = control.ss(A, B, C, D)

# Conversion to Transfer Function (System 1)
tf_sys1 = control.tf(sys1)
print("tf1 = ")
print(tf_sys1)
# Definition of System 2
a = np.array([[0, 0, -5], [1, 0, -11], [0, 1, -6]])
b = np.array([[1], [0], [1]])
c = np.array([[0, 0, 1]])
d = np.array([[0]])
sys2 = control.ss(a, b, c, d)

# Conversion to Transfer Function (System 2)
tf_sys2 = control.tf(sys2)
print("\ntf2 = ")
print(tf_sys2)
# Definition of System 3
A = np.array([[0, 1, 0], [0, 0, 1], [-5, -11, -6]])
B = np.array([[1], [-6], [26]])
C = np.array([[1, 0, 0]])
D = np.array([[0]])
sys3 = control.ss(A, B, C, D)

# Conversion to Transfer Function (System 3)
tf_sys3 = control.tf(sys3)
print("\ntf3 = ")
print(tf_sys3)
# Observability Check (System 3)
observability_matrix = control.obsv(sys3.A, sys3.C)
print("\nobservability_matrix = ")
print(observability_matrix)
# Definition of System 4
A = np.array([[0, 0, -5], [1, 0, -11], [0, 1, -6]])
B = np.array([[1], [0], [0]])
C = np.array([[1, -6, 26]])
D = np.array([[0]])
sys4 = control.ss(A, B, C, D)

# Conversion to Transfer Function (System 4)
tf_sys4 = control.tf(sys4)
print("\ntf4 = ")
print(tf_sys4)
# Controllability Check (System 4)
controllability_matrix = control.ctrb(sys4.A, sys4.B)
print("\ncontrollability_matrix = ")
print(controllability_matrix)
# Conversion from Transfer Function to State-Space (MySys)
num = np.array([1, 0, 1])
den = np.array([1, 6, 11, 5])
sys = control.TransferFunction(num, den)
mysys = control.ss(sys)
A, B, C, D = mysys.A, mysys.B, mysys.C, mysys.D
print("\nA =")
print(A)
print("\nB =")
print(B)
print("\nC =")
print(C)
print("\nD =")
print(D)
print(mysys)