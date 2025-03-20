import numpy as np
A = np.arange(1, 26).reshape(5, 5)
B = np.arange(5, 26, 5).T
C = A + B
print(C)
