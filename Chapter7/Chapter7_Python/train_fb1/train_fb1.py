# -*- coding: utf-8 -*-
"""train_fb1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fosGKMWUDqFkMa_XhAqRJZ_8-T0FzGZI
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def train_fb(t, x):
    A = np.array([
        [0, 0, 0, 0, 1, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, -1, 0],
        [-12.5, 0, 0, 0, -0.75, 0.75, 0, 0, 0, 0],
        [62.5, -62.5, 0, 0, 3.75, -7.5, 3.75, 0, 0, 0],
        [0, 62.5, -62.5, 0, 0, 3.75, -7.5, 3.75, 0, 0],
        [0, 0, 62.5, -62.5, 0, 0, 3.75, -7.5, 3.75, 0],
        [0, 0, 0, 62.5, 0, 0, 0, 3.75, -3.75, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, -1/40]
    ])

    B = np.array([0, 0, 0, 0, 0.005, 0, 0, 0, 0, 0])  # Force input
    b1 = np.array([0, 0, 0, 0, 0.005, 0, 0, 0, 0, 0])  # Force input
    b2 = np.array([0, 0, 0, 0, 250, 0, 0, 0, 0, -1250])  # Constant input

    vd = 25 * (1 - np.exp(-t / 40))
    k = np.array([54.5333, 16.2848, -1.3027, -4.3607, 191.7414, -40.4841, -34.2067, -29.7070, -27.3437, 52.0886])

    dx = np.array([x[1] - 20, x[2] - 20, x[3] - 20, x[4] - 20])
    dv = np.array([x[5] - vd, x[6] - vd, x[7] - vd, x[8] - vd, x[9] - vd])
    z = x[5] - vd
    X = np.concatenate((dx, dv, [z]))

    u = k.dot(X)
    xp = A.dot(x) + b1 * u + b2
    return xp