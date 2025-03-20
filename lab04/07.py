import numpy as np
# 7. Mając macierze A = np.array([[2, 3], [1, 4]]) i B = np.array([[5, 1], [2,
# 6]]), wykonaj mnożenie macierzowe używając funkcji np.matmul().

A = np.array([[2, 3], [1, 4]])
B = np.array([[5, 1], [2,6]])
C = np.matmul(A, B)
print(C)