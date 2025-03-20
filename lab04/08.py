import numpy as np
# 8. Rozwiąż układ równań liniowych Ax = b, gdzie A = np.array([[4, 2], [3, 5]]) i b
# = np.array([8, 7]) za pomocą funkcji np.linalg.solve().
A = np.array([[4, 2], [3, 5]])
b = np.array([8, 7])
c = np.linalg.solve(A, b)
print(c)