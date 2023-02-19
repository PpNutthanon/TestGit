import numpy as np
from scipy import linalg
a = np.array([[129, 0, -8, 0],
              [-8, 129, 32, -8],
              [8, 0, 129, 0],
              [-32, 8, -8, 129]])
b= np.array([0, 0, 1, 0])
linalg.solve(a, b)
np.linalg.solve(a, b)
